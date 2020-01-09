import argparse
import random
import itertools
import os
import sys
import rule_classifier as paper_classifier
import urllib.request
import bs4 as bs
import time




# paper_id:  
# paper_meta: store meta information of a paper
# cased_regexes: a collection of regular expressions based on concepts
# feature: which part of content will we used to label papers. i.e. "title" or "fulltext"
def labelPaper(paper_id = None, paper_meta = None, cased_regexes = None, feature = None): 
  if not os.path.isfile(f'papers/{paper_id}.pdf'):
    os.makedirs(f'papers/', exist_ok=True)
    urllib.request.urlretrieve(f'https://www.aclweb.org/anthology/{paper_id}.pdf', f'papers/{paper_id}.pdf')
    #time.sleep(2) # maybe we would wait some time until downloading processing finishes.
    os.system(f'pdftotext papers/{paper_id}.pdf papers/{paper_id}.txt')
  with open(f'papers/{paper_id}.txt', 'r') as f:
    paper_text = '\n'.join(f.readlines())
  paper_title = ''.join(paper_meta.title.findAll(text=True))

  is_cased = 1 # if case-sensitive
  if feature == "title":
    feature = paper_title
    is_cased = 0
  elif feature == "fulltext":
    feature = paper_text
    is_cased = 1

  predicted_tags = paper_classifier.classify(feature, cased_regexes, is_cased)
  print(f'Title: {paper_title}\n'
        f'Local location: papers/{paper_id}.pdf\n'
        f'Online location: https://www.aclweb.org/anthology/{paper_id}.pdf\n'
        f'Text file location: auto/{paper_id}.txt')
  for i, tag in enumerate(predicted_tags):
    print(f'Tag {i}: {tag}')
  print("------------------------------------------------\n")

  os.makedirs(f'auto/', exist_ok=True)
  fin = open(f'auto/{paper_id}.txt', 'w')
  print(f'# Title: {paper_title}\n# Online location: https://www.aclweb.org/anthology/{paper_id}.pdf', file=fin)
  for tag, conf, just in predicted_tags:
    print(f'# CHECK: confidence={conf}, justification={just}\n{tag}',file=fin)




if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Get a paper to try to read and annotate")

  parser.add_argument("--paper_id", type=str, default=None,
                      help="The paper ID to get, if you want to specify a single one (e.g. P84-1031)")
  parser.add_argument("--years", type=str, default="19",
                      help="If a paper ID is not specified, a year (e.g. 19) or range of years (e.g. 99-02) from which"+
                           " to select a random paper.")
  parser.add_argument("--confs", type=str, default="P,N,D",
                      help="A comma-separted list of conference abbreviations from which papers can be selected")
  parser.add_argument("--volumes", type=str, default="1,2",
                      help="A comma-separated list of volumes to include (default is long and short research papers)."+
                           " 'all' for no filtering.")
  parser.add_argument("--n_sample", type=int, default="1",
                      help="the number of sampled papers if paper_id is not specified (e.g. 1)")

  parser.add_argument("--template", type=str, default="template.cpt",
                      help="The file of concept template (e.g. template.cpt)")

  parser.add_argument("--feature", type=str, default="fulltext",
                      help="Which parts of paper is used to classify (e.g. fulltext|title)")

  args = parser.parse_args()

  # init variables
  feature = args.feature
  paper_id = args.paper_id
  template = args.template
  n_sample = args.n_sample
  volumes = args.volumes.split(',')
  paper_map = {}

  # lead the concept template
  cased_regexes = paper_classifier.genConceptReg(file_concept=template, formate_col = 3)

  # if paper_id has not been specified
  if paper_id == None:
    years = args.years.split('-')
    confs = args.confs.split(',')
    if len(years) == 2:
      years = list(range(int(years[0]), int(years[1])+1))
    else:
      assert len(years) == 1, "invalid format of years, {args.years}"
    for pref, year in itertools.product(confs, years):
      year = int(year)
      pref= pref.upper()
      with open(f'acl-anthology/data/xml/{pref}{year:02d}.xml', 'r') as f:
        soup = bs.BeautifulSoup(f, 'xml')
      for vol in soup.collection.find_all('volume'):
        if vol.attrs['id'] in volumes:
          for pap in vol.find_all('paper'):
            if pap.url:
              paper_map[pap.url.contents[0]] = pap


    paper_keys = list(paper_map.keys())
    for _ in range(n_sample):
      randid = random.choice(paper_keys)
      if not os.path.isfile(f'annotations/{randid}.txt') and not os.path.isfile(f'auto/{randid}.txt'):
        paper_id = randid
        paper_meta = paper_map[paper_id]
        #print(paper_meta)
        labelPaper(paper_id, paper_meta, cased_regexes, feature)
      else:
        print(f'Warning: {paper_id} has been labeled!')

  # if paper_id is specified
  else:
    prefix = paper_id.split("-")[0]
    with open(f'acl-anthology/data/xml/{prefix}.xml', 'r') as f:
        soup = bs.BeautifulSoup(f, 'xml')
        for vol in soup.collection.find_all('volume'):
            if vol.attrs['id'] in volumes:
              for pap in vol.find_all('paper'):
                if pap.url and pap.url.contents[0] == paper_id:
                  paper_map[pap.url.contents[0]] = pap
                  #print(paper_map[pap.url.contents[0]])
                  if not os.path.isfile(f'annotations/{paper_id}.txt') and not os.path.isfile(f'auto/{paper_id}.txt'):
                      labelPaper(paper_id, paper_map[paper_id], cased_regexes, feature)
                      sys.exit(1)
                  else:
                    print(f'Warning: {paper_id} has been labeled!')

    if len(paper_map) == 0:
      print(f'Warning: {paper_id} can not been found!')
      sys.exit(1)



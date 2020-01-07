import argparse
import random
import itertools
import os
import sys
import rule_classifier as paper_classifier
import urllib.request
import bs4 as bs
import time





def labelPaper(paper_id = None, paper_meta = None, cased_regexes = None, feature = None): 
  if not os.path.isfile(f'papers/{paper_id}.pdf'):
    os.makedirs(f'papers/', exist_ok=True)
    urllib.request.urlretrieve(f'https://www.aclweb.org/anthology/{paper_id}.pdf', f'papers/{paper_id}.pdf')
    #time.sleep(2) 
    os.system(f'pdftotext papers/{paper_id}.pdf papers/{paper_id}.txt')
  with open(f'papers/{paper_id}.txt', 'r') as f:
    paper_text = '\n'.join(f.readlines())
  paper_title = ''.join(paper_meta.title.findAll(text=True))

  flag = 1 
  if feature == "title":
    feature = paper_title
    flag = 0
  elif feature == "fulltext":
    feature = paper_text
    flag = 1

  predicted_tags = paper_classifier.classify(feature, cased_regexes, flag)
  print(f'Title: {paper_title}\n'
        f'Local location: papers/{paper_id}.pdf\n'
        f'Online location: https://www.aclweb.org/anthology/{paper_id}.pdf\n'
        f'Text file location: auto/{paper_id}.txt')
  for i, tag in enumerate(predicted_tags):
    print(f'Tag {i}: {tag}')
  print("------------------------------------------------\n")
  os.makedirs(f'auto/', exist_ok=True)
  fin = open(f'auto/{paper_id}.txt', 'w')
  print(f'# Title: {paper_title}\n',f'# Online location: https://www.aclweb.org/anthology/{paper_id}.pdf', file=fin)
  for tag, conf, just in predicted_tags:
    print(f'# CHECK: confidence={conf}, justification={just}\n', f'{tag}',file=fin)




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

  parser.add_argument("--template", type=str, default="template.cpt",
                      help="The file of concept template (e.g. template.cpt)")

  parser.add_argument("--feature", type=str, default="fulltext",
                      help="Which parts of paper is used to classify (e.g. fulltext|title)")

  args = parser.parse_args()


  cased_regexes = paper_classifier.genConceptReg(file_concept=args.template, formate_col = 3)
  feature = args.feature


  paper_id = args.paper_id
  years = args.years.split('-')
  confs = args.confs.split(',')
  volumes = args.volumes.split(',')
  paper_map = {}
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


  if paper_id == None:
    num_tries = 10
    paper_keys = list(paper_map.keys())
    for _ in range(num_tries):
      randid = random.choice(paper_keys)
      if not os.path.isfile('annotations/{randid}.txt') and not os.path.isfile('auto/{randid}.txt'):
        paper_id = randid
        paper_meta = paper_map[paper_id]
        #print(paper_meta)
        labelPaper(paper_id, paper_meta, cased_regexes, feature)
        #break
      #break
  else:
      #print(paper_map.keys())
      #print(len(paper_map))
      key_p = f'{pref}{year:02d}-'+paper_id
      labelPaper(key_p, paper_map[key_p], cased_regexes, feature)
      # if paper_id == None:
      #   print('WARNING: Tried {num_tries} random papers and couldn\'t find an unannotated one. Maybe you\'re done annotating?', file=sys.stderr)
      #   sys.exit(1)

      #paper_id = randid



import argparse
import random
import itertools
import os
import sys
import rule_classifier as paper_classifier
import urllib.request
import bs4 as bs

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
  args = parser.parse_args()

  if args.paper_id:
    paper_id = args.paper_id
  else:
    years = args.years.split('-')
    confs = args.confs.split(',')
    volumes = args.volumes.split(',')
    paper_map = {}
    if len(years) == 2:
      years = list(range(years[0], years[1]+1))
    else:
      assert len(years) == 1, f"invalid format of years, {args.years}"
    for pref, year in itertools.product(confs, years):
      year = int(year)
      with open(f'acl-anthology/data/xml/{pref}{year:02d}.xml', 'r') as f:
        soup = bs.BeautifulSoup(f, 'xml')
      for vol in soup.collection.find_all('volume'):
        if vol.attrs['id'] in volumes:
          for pap in vol.find_all('paper'):
            if pap.url:
              paper_map[pap.url.contents[0]] = pap
    paper_id = None
    num_tries = 10000
    paper_keys = list(paper_map.keys())
    for _ in range(num_tries):
      randid = random.choice(paper_keys)
      if not os.path.isfile(f'annotations/{randid}.txt') and not os.path.isfile(f'auto/{randid}.txt'):
        paper_id = randid
        break

    if paper_id == None:
      print('WARNING: Tried {num_tries} random papers and couldn\'t find an unannotated one. Maybe you\'re done annotating?', file=sys.stderr)
      sys.exit(1)

  if not os.path.isfile(f'papers/{paper_id}.pdf'):
    os.makedirs(f'papers/', exist_ok=True)
    urllib.request.urlretrieve(f'https://www.aclweb.org/anthology/{paper_id}.pdf', f'papers/{paper_id}.pdf')
    os.system(f'pdftotext papers/{paper_id}.pdf papers/{paper_id}.txt')

  paper_meta = paper_map[paper_id]
  with open(f'papers/{paper_id}.txt', 'r') as f:
    paper_text = '\n'.join(f.readlines())
  paper_title = ''.join(paper_meta.title.findAll(text=True))
  predicted_tags = paper_classifier.classify(paper_text=paper_text)

  print(f'Title: {paper_title}\n'
        f'Local location: papers/{paper_id}.pdf\n'
        f'Online location: https://www.aclweb.org/anthology/{paper_id}.pdf\n'
        f'Text file location: auto/{paper_id}.txt')
  for i, tag in enumerate(predicted_tags):
    print(f'Tag {i}: {tag}')
  os.makedirs(f'auto/', exist_ok=True)
  with open(f'auto/{paper_id}.txt', 'w') as f:
    print(f'# Title: {paper_title}\n'
          f'# Online location: https://www.aclweb.org/anthology/{paper_id}.pdf',
          file=f)
    for tag, conf, just in predicted_tags:
      print(f'# CHECK: confidence={conf}, justification={just}\n'
            f'tag',
            file=f)


import argparse
import random
import itertools
import os
import sys
import rule_classifier as paper_classifier
import urllib.request
import bs4 as bs
import time

from utils import label_paper


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Get a paper to try to read and annotate")

  parser.add_argument("--paper_id", type=str, default=None,
                      help="The paper ID to get, if you want to specify a single one (e.g. P84-1031)")
  parser.add_argument("--years", type=str, default="19",
                      help="If a paper ID is not specified, a year (e.g. 19) or range of years (e.g. 99-02) from which"+
                           " to select a random paper.")
  parser.add_argument("--confs", type=str, default="P,N,D",
                      help="A comma-separated list of conference abbreviations from which papers can be selected")
  parser.add_argument("--volumes", type=str, default="1,2",
                      help="A comma-separated list of volumes to include (default is long and short research papers)."+
                           " 'all' for no filtering.")
  parser.add_argument("--n_sample", type=str, default="1",
                      help="the number of sampled papers if paper_id is not specified (e.g. 1)."
                           " Write 'all' to select all papers from those years/conferences/volumes.")
  parser.add_argument("--template", type=str, default="template.cpt",
                      help="The file of concept template (e.g. template.cpt)")
  parser.add_argument("--feature", type=str, default="fulltext",
                      help="Which parts of paper is used to classify (e.g. fulltext|title)")
  parser.add_argument("--use_cite", type=bool, default=False,
                      help="whether to use citation papers")

  args = parser.parse_args()

  # init variables
  feature   = args.feature
  paper_id  = args.paper_id
  template  = args.template
  n_sample  = args.n_sample
  volumes   = args.volumes.split(',')
  use_cite  = args.use_cite
  paper_map = {}

  # read the concept template
  cased_regexes = paper_classifier.generate_concept_regex(file_concept=template, format_col=3)

  # if 'paper_id' is not specified
  if paper_id == None:
    years = args.years.split('-')
    confs = args.confs.split(',')
    if len(years) == 2:
      years = list(range(int(years[0]), int(years[1])+1))
    else:
      assert len(years) == 1, "invalid format of years, {args.years}"
    for pref, year in itertools.product(confs, years):
      year = int(year)
      pref = pref.upper()
      with open(f'acl-anthology/data/xml/{pref}{year:02d}.xml', 'r') as f:
        soup = bs.BeautifulSoup(f, 'xml')
      for vol in soup.collection.find_all('volume'):
        if vol.attrs['id'] in volumes:
          for pap in vol.find_all('paper'):
            if pap.url:
              paper_map[pap.url.contents[0]] = pap

    paper_keys = list(paper_map.keys())
    if n_sample == 'all':
      for paper_id in paper_keys:
        paper_meta = paper_map[paper_id]
        label_paper(paper_id, paper_meta, cased_regexes, feature, False)
    else:
      for _ in range(int(n_sample)):
        randid = random.choice(paper_keys)
        if not os.path.exists(f'annotations/{randid}.txt') and not os.path.exists(f'auto/{randid}.txt'):
          paper_id = randid
          paper_meta = paper_map[paper_id]
          label_paper(paper_id, paper_meta, cased_regexes, feature, False)
        else:
          print(f'Warning: {paper_id} has been labeled!')

  # if 'paper_id' is specified
  else:
    prefix = paper_id.split("-")[0]
    
    with open(f'acl-anthology/data/xml/{prefix}.xml', 'r') as f:
        soup = bs.BeautifulSoup(f, 'xml')
        for vol in soup.collection.find_all('volume'):
            if vol.attrs['id'] in volumes:
              for pap in vol.find_all('paper'):
                if (pap.url) and (pap.url.contents[0] == paper_id):
                  paper_map[pap.url.contents[0]] = pap
                  if use_cite:  # if use citation information
                    if not os.path.exists(f'annotations/{paper_id}.txt'):
                      print(f'Warning: {paper_id} has not been labeled! We should label it first')
                      print(f'Warning: If you already labeled it, move labeled file into annotations directory')
                    else:
                      label_paper(paper_id, paper_map[paper_id], cased_regexes, feature, use_cite)
                  else:
                    if not os.path.exists(f'annotations/{paper_id}.txt') and not os.path.exists(f'auto/{paper_id}.txt'):
                      label_paper(paper_id, paper_map[paper_id], cased_regexes, feature, False)
                      sys.exit(1)
                    else:
                      print(f'Warning: {paper_id} has been labeled!')

    if len(paper_map) == 0:
      print(f'Warning: {paper_id} cannot be found!')
      sys.exit(1)

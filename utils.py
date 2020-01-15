import os
import random
import requests
import collections
import urllib.request

import rule_classifier as paper_classifier


def label_references(refs, feature, cased_regexes, is_cased):
  """Label reference papers

  Args:
    ref (list): arixv ID list of reference papers
    feature (str): which part of content will we use to label papers (e.g. "title" or "fulltext")
    cased_regexes (list): regex information used to paper labeling    
    is_cased (bool): boolean value that indicates whether the case is case sensitive or not
  
  Returns:
    Counter: tag counter made by all the tags from refs
  """

  total_tags = []

  for ref in refs:
    paper_title, paper_id = ref
    
    if not os.path.isfile(f'papers/{paper_id}.pdf'):
      try:
        urllib.request.urlretrieve(f'https://arxiv.org/pdf/{paper_id}.pdf', f'papers/{paper_id}.pdf')
        # time.sleep(1) # maybe we would wait some time until downloading processing finishes.
        os.system(f'pdftotext papers/{paper_id}.pdf papers/{paper_id}.txt')
      except:
        print(f'WARNING: Error while downloading/processing https://arxiv.org/pdf/{paper_id}.pdf')
        continue

    with open(f'papers/{paper_id}.txt', 'r') as f:
      paper_text = '\n'.join(f.readlines())

    if feature == "title":
      contents = paper_title
    elif feature == "fulltext":
      contents = paper_text

    total_tags += paper_classifier.classify(contents, cased_regexes, is_cased)

  total_tags = [tag[0] for tag in total_tags]

  return collections.Counter(total_tags)


def get_references(doi=None, n_ref=0):
  """Get reference papers using Semantic Scholar API

  Args:
    doi (str): DOI of the paper
    n_ref (int): number of reference papers used to analyze
  
  Returns:
    list: arixv ID list of reference papers
  """

  semantic_scholar = f'https://api.semanticscholar.org/v1/paper/{doi}'
  res = requests.get(semantic_scholar)
  
  if res.status_code != 200:
    return False

  citations = res.json()['references']
  refs = [(c['title'], c['arxivId']) for c in citations if c['arxivId'] is not None]
  n_ref = len(refs) if len(refs) < n_ref else n_ref
  random.shuffle(refs)
  
  return refs[:n_ref]
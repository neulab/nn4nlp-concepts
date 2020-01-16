import os
import random
import requests
import collections
import urllib.request

import rule_classifier as paper_classifier


def label_paper(paper_id=None, paper_meta=None, cased_regexes=None, feature=None, use_cite=False):
  """Label one paper or citations papers

  Args:
    paper_id (str): The paper ID
    paper_meta (bs4.element.Tag): Store meta information of a paper
    cased_regexes (list): Regex information used to paper labeling
    feature (str): which part of content will we use to label papers (e.g. "title" or "fulltext")
    use_cite (bool): whether to use known citation papers
  
  Returns:
    None
  """

  if not use_cite:
    if not os.path.exists(f'papers/{paper_id}.pdf'):
      os.makedirs(f'papers/', exist_ok=True)
      try:
        urllib.request.urlretrieve(f'https://www.aclweb.org/anthology/{paper_id}.pdf', f'papers/{paper_id}.pdf')
        # time.sleep(2) # maybe we would wait some time until downloading processing finishes.
        os.system(f'pdftotext papers/{paper_id}.pdf papers/{paper_id}.txt')
      except:
        print(f'WARNING: Error while downloading/processing https://www.aclweb.org/anthology/{paper_id}.pdf')
        return

    with open(f'papers/{paper_id}.txt', 'r') as f:
      paper_text = '\n'.join(f.readlines())
    paper_title = paper_meta.title.text

    is_cased = True # if case-sensitive
    if feature == "title":
      contents = paper_title
      is_cased = False
    elif feature == "fulltext":
      contents = paper_text
      is_cased = True

    predicted_tags = paper_classifier.classify(contents, cased_regexes, is_cased)
    
    # Display result
    print(f'Title: {paper_title}\n'
          f'Local location: papers/{paper_id}.pdf\n'
          f'Online location: https://www.aclweb.org/anthology/{paper_id}.pdf\n'
          f'Text file location: auto/{paper_id}.txt')
    for i, tag in enumerate(predicted_tags):
      print(f'Tag {i+1}: {tag}')
    print("------------------------------------------------\n")
    
    # Store result
    os.makedirs(f'auto/', exist_ok=True)
    with open(f'auto/{paper_id}.txt', 'w') as f:
      print(f'# Title: {paper_title}\n# Online location: https://www.aclweb.org/anthology/{paper_id}.pdf', file=f)
      for tag, conf, just in predicted_tags:
        print(f'# CHECK: confidence = {conf}, justification = {just}\n{tag}',file=f)

  else:  # if use citation papers
    if paper_meta.doi:
      paper_doi = paper_meta.doi.text.lower()
      refs, tags = get_citations(paper_id, paper_doi)
      
      if not refs:
        print(f'WARNING: Cannot fetch {paper_id} citation related information')
      else:
        label_citation_papers(refs, tags, paper_id)


def get_citations(id=None, doi=None):
  """Get citation papers using Semantic Scholar API

  Args:
    id (str): paper ID
    doi (str): paper DOI
  
  Returns:
    list: citation papers' (doi, title) list of tuple
    list: tag list from known paper
  """

  semantic_scholar = f'https://api.semanticscholar.org/v1/paper/{doi}'
  res = requests.get(semantic_scholar)
  
  if res.status_code != 200:
    return False, None

  citations = res.json()['citations']
  refs = [(c['doi'][c['doi'].rfind('/')+1:].upper(), c['title']) 
          for c in citations if c['doi'] is not None]

  # Read tag list from "known" labeled paper
  with open(f'annotations/{id}.txt', 'r') as f:
    tags = f.readlines()[2:]  # filter out title and location
    tags = [tag.replace('\n', '') for tag in tags]
  
  return refs, tags


def label_citation_papers(refs, tags, paper_id):
  """Label papers which citated already "known" paper

  Args:
    refs (list): DOI list of citation papers
    tags (list): tag list from "known" paper
    paper_id (str): "known" paper id
  
  Returns:
    None
  """

  justification = f'Found from reference paper {paper_id}'
  possible_confs = ['P', 'N', 'D']
  new_paps = collections.defaultdict(str)
  
  os.makedirs(f'auto/', exist_ok=True)
  for ref in refs:
    ref_id, ref_title = ref
    if not os.path.exists(f'annotations/{ref_id}.txt') and not os.path.exists(f'auto/{ref_id}.txt'):
      if ref_id[0] in possible_confs:
        with open(f'auto/{ref_id}.txt', 'w') as f:
          print(f'# Title: {ref_title}\n# Online location: https://www.aclweb.org/anthology/{ref_id}.pdf', file=f)
          for tag in tags:
            print(f'# CHECK: justification = {justification}\n{tag}',file=f)
        new_paps[ref_id] = ref_title

  print(f'Totally {len(new_paps)} new papers are labeled using {paper_id} tag information.')
  for k, v in dict(new_paps).items():
    print(f': [{k}] {v}')

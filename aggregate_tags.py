import argparse
import os
import re
from collections import defaultdict

def get_all_files(f):
  if os.path.isfile(f):
    return [f]
  elif os.path.isdir(f):
    ret = []
    for x in os.listdir(f):
      ret += get_all_files(os.path.join(f,x))
    return ret
  else:
    raise ValueError(f'Could not find file {f}')

def get_tags(f, legal_tags = None):
  with open(f, 'r') as fin:
    for line in fin:
      line = line.strip()
      if not line.startswith("#"):
        if legal_tags and line not in legal_tags:
          raise ValueError(f'Illegal tag found in file {f}, {line}')
        yield line

def parse_concepts(f):
  concepts = {'not-neural': 1}
  concept_re = re.compile(r': \[?`([a-z0-9-]+)`')
  with open(f, 'r') as fin:
    for line in fin:
      m = re.search(concept_re, line)
      if m:
        val = m.group(1)
        concepts[val] = 1
  return concepts

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Aggregate tags from several files or a directories of files into a"
                                               " tag/count file for use in draw_bar.py.")

  parser.add_argument("files", type=str, nargs='+',
                      help="The files or directories over which you'd like to aggregate")
  parser.add_argument("--concepts", type=str, default=None,
                      help="The concepts.md file, which is parsed to find a list of legal tags")

  args = parser.parse_args()

  fs = []
  for f in args.files:
    fs += get_all_files(f)

  legal_concepts = parse_concepts(args.concepts) if args.concepts else None

  all_tags = defaultdict(lambda: 0)
  for f in fs:
    for tag in get_tags(f, legal_tags=legal_concepts):
      all_tags[tag] += 1

  for k, v in sorted(list(all_tags.items()), key=lambda x: -x[1]):
    print(f'{k}\t{v}')


import re

# TODO: get implication graph from concepts.md, and don't add concepts that are implied

concept_regexes = [
  (r'transformer', 'arch-transformer', 0.9),
  (r'(convolutional|cnn)', 'arch-cnn', 0.9),
  (r'lstm', 'arch-lstm', 0.9),
]

def classify(paper_text=None, threshold=0.5):
  """Classify papers

  :param paper_text: Text of the paper read from a file.
  :return: A list of tuples (tag, probability, justification)
  """
  ret = []
  if paper_text != None:
    for reg, tag, certainty in concept_regexes:
      m = re.search(reg, paper_text, re.IGNORECASE)
      if m:
        ret.append( (tag, certainty, 'Matched regex {}'.format(str(reg))) )
  return ret
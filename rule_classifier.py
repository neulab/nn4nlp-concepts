import os
import sys
import re


def generate_concept_regex(file_concept="test.cpt", format_col=3):
  """Generate regular expressions using inputted concept file
  
  The template file should follow format below:
 	concept \t father_concept \t keywords

  Args:
    file_concept (str): File containing regular expressions
    format_col (int): Number of columns in concept file
  
  Returns:
    list: Generated regular expressions
  """

  if not os.path.exists(file_concept):
    print("can not find concept template")
    os._exit(0)

  cased_regexes = []
  with open(file_concept,"r") as f:
    for line in f:
      line = line.rstrip("\n")
      if (len(line.split("\t")) != format_col) or (line[0] == "#"):
        continue
      info_list = line.split("\t")
      cased_regexes.append((info_list[2].rstrip("\r"), info_list[0], 0.9))
  
  return cased_regexes


def classify(paper_text=None, cased_regexes=None, flag_cased=True, threshold=0.5):
  """Classify input text and returns labeled tag list 

  Args:
    paper_text (str): Input text will be either 'full text' or just 'title'
    cased_regexes (list): Generated regular expressions from concept file
    flag_cased (bool): A Boolean value that indicates whether the case is case sensitive or not
    threshold (float): [To Be Updated]
  
  Returns:
    list: Labeled tag list
  """

  result = []
  if paper_text != None:
    for regex, tag, certainty in cased_regexes:
      if flag_cased:
        m = re.search(regex, paper_text)
      else:
        m = re.search(regex, paper_text, re.IGNORECASE)

      if m:
        result.append((tag, certainty, f'Matched regex {regex}'))
  
  return result

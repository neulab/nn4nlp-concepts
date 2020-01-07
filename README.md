# Concepts in Neural Networks for NLP
by Graham Neubig, Pengfei Liu, and other contributors

This is a list of concepts that should be understood to understand modern research on neural networks for NLP.

## Setup

Get the requirements to run the package:

    pip install -r requirements.txt

Install `poppler` through your favorite version control software.
    
And download the git submodule of the ACL Anthology:

    git clone https://github.com/acl-org/acl-anthology.git


## Examples:

* 1: `python get_paper.py --years 18-19 --confs P  --n_sample 5 --template template.cpt --feature fulltext`
If the paper_id is not specified, 5 samples will be randomly selected from a pool of papers;
 
* 2: `python get_paper.py --paper_id P19-1032 --template template.cpt --feature fulltext`
If the paper_id (P19-1032) has been specified, directly printing related information

where:
* Once the paper_id has been specified, `years`,`confs`, and `n_sample` are not required.
* `confs`: a comma-separted list of conference abbreviations from which papers can be selected (P,N,D)
* `n_sample`: the number of sampled papers if paper_id is not specified
* `template`: the file of concept template (e.g. template.cpt)
* `feature`: which part of paper is used to classify (e.g. fulltext or title)

## How to Contribute

1. Read `concepts.md` to learn more about the concepts that are annotated here.
2. Run `get_paper.py` to get a paper to annotate with the concepts contained therein. By default this will download
   a paper from ACL, NAACL, or EMNLP in 2019.
3. When the paper is downloaded, a text file corresponding to the paper ID will be written out to `auto/ID.txt`. This
   will include some comments with the paper name, title, PDF location, etc. In addition, it will have some
   automatically provided concept tags that were estimated based on the article text.
4. Manually confirm that the automatically annotated concepts are correct. If so, then delete the comment saying
   "# CHECK: ". If the concepts are not included in the paper, then delete them.
5. Add any concepts that were not caught by the automatic process.
6. Once you are done annotating concepts, move `auto/ID.txt` to `annotations/ID.txt`. You can then send a pull request
   to the repository to contribute.
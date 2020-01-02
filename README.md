# Concepts in Neural Networks for NLP
by Graham Neubig, Pengfei Liu, and other contributors

This is a list of concepts that should be understood to understand modern research on neural networks for NLP.

## Setup

Get the requirements to run the package:

    pip install -r requirements.txt

Install `poppler` through your favorite version control software.
    
And download the git submodule of the ACL Anthology:

    git clone https://github.com/acl-org/acl-anthology.git

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
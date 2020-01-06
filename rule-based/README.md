

-------------update 01-06---------------

# a demo for paper labeling individually based on three types of features:
1) title
2) title + abstract
3) fulltext

# requirement: 
1) python 2.7
2) pdftotext



-------------update 01-04---------------
Here, I attempt to label each paper in two ways:

1) solely based on the  paper's #title#
2) based on the #full-text#


Specifically:

--template.cpt: template of concept definition (most of them are based on you proposed items)

--conceptBytitle.detail: the detailed concepts covered by each paper (ACL+EMNLP+NAACL2019)

--conceptBytitle.rank: the number of papers that each concept has covered

A similar case happened on a full-text based labeling process.


NOTE!
1) #title#- and #full-text#- based annotations could refect something a little different.
2) Regarding #full-text# annotation, We label a concept "X" if some keywords of the "X" concept has appeared in the paper. (A rough way)
3) Maybe #abstract#-based is more appropriate ...


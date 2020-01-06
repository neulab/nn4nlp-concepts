import pdftotext
import re
import sys
import os.path
import argparse

# uncased_regexes = [
#   (r'convolutional', 'arch-cnn', 0.9),
#   (r'variational auto-*encoder', 'latent-vae', 0.9),
#   (r'generative adversarial', 'adv-gan', 0.9),
#   (r'attention', 'arch-att', 0.9),
#   (r'bi-lstm', 'arch-bilstm', 0.9),
#   (r'canonical correlation', 'loss-cca', 0.9),
# ]


# cased_regexes = [
#   (r'Transformer', 'arch-transformer',0.9),
#   (r'BERT', 'embed-bert', 0.9),
#   (r'ELMo', 'embed-elmo', 0.9),
#   (r'LSTM', 'arch-lstm', 0.9),
#   (r'VAE', 'latent-vae', 0.9),
#   (r'GAN', 'adv-gan', 0.9),
#   (r'CCA', 'loss-cca', 0.9),
# ]


def classify(paper_text=None, cased_regexes = None, flag_cased = 1, threshold=0.5):
	ret = []
	if paper_text != None:
		for reg, tag, certainty in cased_regexes:
	        	if flag_cased == 1:  
		  		m = re.search(reg, paper_text)
			else:
		  		m = re.search(reg, paper_text,re.IGNORECASE)
				
		  	if m:
		    		ret.append((tag, certainty, 'Matched regex {}'.format(str(reg))))
		return ret


# generate regular expression from a concept template
# the formate of template:
# concept \t father_concept \t keywords
def genConceptReg(file_concept="test.cpt", formate_col = 3):
	if not os.path.exists(file_concept):
		print "can not find concept template"
		os._exit(0)

	cased_regexes = []
	fin = open(file_concept,"r")
	for line in fin:
		line = line.rstrip("\n")
		if len(line.split("\t"))!= formate_col or line[0] == "#":
			continue
		info_list = line.split("\t")
		cased_regexes.append((info_list[2].rstrip("\r"), info_list[0], 0.9))
	fin.close()
	return cased_regexes







# flag is used to determine which part of papers' content we will be based on.
def parsePdf(path_pdf = None, flag=None):
	doc = ""
	# open the pdf
	with open(path_pdf, "r") as f:
	    pdf = pdftotext.PDF(f, "secret")

	if flag == "fulltext":
		doc =  "\n".join(pdf).encode("gbk","ignore")
	elif flag == "abstract":
		doc = getAbs(pdf[0].encode("utf8"))

	# p_email = r'\S+@\S+'
	# lst = re.findall(p_email, doc)

	return doc




# identify which sentences are parts of abstract
def getSubsen(sent):
	sent_list = sent.split(" ")
	null_size = 0
	flag = 0
	res = ""
	for w in sent_list:
		if null_size >=2 and flag == 1:
			break
		if w == "":
			null_size += 1
			continue
		else:
			res += w + " "
			flag = 1
			null_size = 0
	return res


# get the abstract part from a paper
def getAbs(doc):
	sent_list = doc.split("\n")
	n_line = 0
	threshold = 30
	abstract = ""
	flag = 0
	for sent in sent_list:
		if sent.find("Abstract") == -1 and flag == 0:
			continue
		flag = 1
		if n_line > threshold or sent.find("Introduction") != -1:
			break
		sent = getSubsen(sent) 
		abstract += sent
		n_line += 1
	return abstract


def addCpt(cpt_list, dict_cpt):
	if len(cpt_list)>=1:
		for cpt in cpt_list:
			dict_cpt[cpt[0]] +=1
	return




def main():


	parser = argparse.ArgumentParser(description='rule-based classifier for individual paper as input')
	parser.add_argument('--feature', default='title', help='the content of paper for classification: title|abstract|fulltext')
	parser.add_argument('--template', default='template.cpt', help='the concept template for generating regular expr')
	parser.add_argument('--title', default='Sequence to sequence learning', help='the title of the paper')
	parser.add_argument('--pdf', default='test.pdf', help='the path of pdf file')
	args = parser.parse_args()


	# paper_feature could be "title", "abstract (+title)", "fulltext"
	paper_feature = args.feature
	path_pdf = args.pdf
	title = args.title
	# load the concept template
	cased_regexes = genConceptReg(args.template)
	#print cased_regexes	

	# assign tags for the input paper
	cont = "" #the final content we use
	res_concept = None 
	if paper_feature == "title":
		cont = title
		res_concept = classify(cont, cased_regexes, 0)
	elif paper_feature == "abstract":
		if not os.path.exists(path_pdf):
			os._exit(0)
		cont = parsePdf(path_pdf, flag = "abstract")
		res_concept = classify(cont, cased_regexes, 1)
	elif paper_feature == "fulltext":
		if not os.path.exists(path_pdf):
			os._exit(0)
		cont = parsePdf(path_pdf, flag = "fulltext")
		res_concept = classify(cont, cased_regexes, 1)


	print "Paper:\t" + title
	for res in res_concept:
		print "# " + res[0]



if __name__ == "__main__":
    sys.exit(main())

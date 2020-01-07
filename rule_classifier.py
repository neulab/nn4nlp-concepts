import os
import sys
import re
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


# generate regular expression from a concept template
# the formate of template:
# concept \t father_concept \t keywords
def genConceptReg(file_concept="test.cpt", formate_col = 3):
	if not os.path.exists(file_concept):
		print("can not find concept template")
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

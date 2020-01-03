import re

# TODO: get implication graph from concepts.md, and don't add concepts that are implied

uncased_regexes = [
  (r'transformer', 'arch-transformer', 0.9),
  (r'convolutional', 'arch-cnn', 0.9),
  (r'variational auto-*encoder', 'latent-vae', 0.9),
  (r'generative adversarial', 'adv-gan', 0.9),
  (r'attention', 'arch-att', 0.9),
  (r'bi-lstm', 'arch-bilstm', 0.9),
  (r'canonical correlation', 'loss-cca', 0.9),
]

cased_regexes = [
  (r'BERT', 'embed-bert', 0.9),
  (r'ELMo', 'embed-elmo', 0.9),
  (r'LSTM', 'arch-lstm', 0.9),
  (r'VAE', 'latent-vae', 0.9),
  (r'GAN', 'adv-gan', 0.9),
  (r'CCA', 'loss-cca', 0.9),
]


def classify(paper_text=None, threshold=0.5):
  """Classify papers

  :param paper_text: Text of the paper read from a file.
  :return: A list of tuples (tag, probability, justification)
  """
  ret = []
  if paper_text != None:
    for reg, tag, certainty in uncased_regexes:
      m = re.search(reg, paper_text, re.IGNORECASE)
      if m:
        ret.append( (tag, certainty, 'Matched regex {}'.format(str(reg))) )
    for reg, tag, certainty in cased_regexes:
      m = re.search(reg, paper_text)
      if m:
        ret.append((tag, certainty, 'Matched regex {}'.format(str(reg))))
  return ret
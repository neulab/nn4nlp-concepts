# Concept Hierarchy in Neural Networks for NLP

In each section, we will have a few basic concepts that we assume need to be known for virtually every paper, and
thus don't need to be specifically labeled. Then we will have a list of concepts that do need to be labeled, along
with their tags. 

**Implication**: Some tags are listed with "`XXX` (implies `YYY`)" which means you need to understand a particular
concept `XXX` in order to understand concept `YYY`. If `YYY` exists in a paper, you do not need to annotated `XXX`.

## Optimization/Learning

### Optimizers

* Mini-batch SGD: `optim-sgd`
* Adam: `optim-adam` (implies `optim-sgd`)
* Adagrad: `optim-adagrad` (implies `optim-sgd`)
* Adam with Specialized Transformer Learning Rate ("Noam" Schedule): `optim-noam` (implies `optim-adam`)
* SGD with Momentum: `optim-momentum` (implies `optim-sgd`)

### Regularization

* Dropout: `reg-dropout`
* Norm (L1/L2) Regularization: `reg-norm`
* Weight Decay: `reg-decay`

### Normalization

* Layer Normalization: `norm-layer`
* Batch Normalization: `norm-batch`

## Sequence Modeling Architectures

### Activation Functions

* Hyperbolic Tangent (tanh): `activ-tanh`
* Rectified Linear Units (RelU): `activ-relu`

### Pooling Operations

* Max Pooling: `pool-max`
* Mean Pooling: `pool-mean`
* k-Max Pooling: `pool-kmax`

### Recurrent Architectures

* Recurrent Neural Network (RNN): `arch-rnn`
* Bi-directional Recurrent Neural Network (Bi-RNN): `arch-birnn` (implies `arch-rnn`)
* Long Short-term Memory (LSTM): `arch-lstm` (implies `arch-rnn`)
* Bi-directional Long Short-term Memory (LSTM): `arch-bilstm` (implies `arch-birnn`, `arch-lstm`)
* Gated Recurrent Units (GRU): `arch-gru` (implies `arch-rnn`)
* Bi-directional Gated Recurrent Units (GRU): `arch-bigru` (implies `arch-birnn`, `arch-gru`)

### Other Sequential Architectures

* Convolutional Neural Networks (CNN): `arch-cnn`
* Attention: `arch-att`
* Self Attention: `arch-selfatt` (implies `arch-att`)

### Architectural Techniques

* Residual Connections (ResNet): `arch-residual`

### Standard Composite Architectures

* Transformer: `arch-transformer` (implies `arch-selfatt`, `arch-residual`, `arch-layernorm`, `optim-noam`)

## Search Algorithms

* Greedy Search: `search-greedy`
* Beam Search: `search-beam`
* A* Search: `search-astar`
* Viterbi Algorithm: `search-viterbi`
* Ancestral Sampling: `search-sampling`
* Gumbel Max: `search-gumbel` (implies `search-sampling`)

## Prediction Tasks

* Text Classification (text -> label): `task-textclass`
* Text Pair Classification (two texts -> label: `task-textpair`
* Sequence Labeling (text -> one label per token): `task-seqlab`
* Extractive Summarization (text -> subset of text): `task-extractive` (implies `text-seqlab`)
* Span Labeling (text -> labels on spans): `task-spanlab`
* Language Modeling (predict probability of text): `task-lm`
* Conditioned Language Modeling (some input -> text): `task-condlm` (implies `task-lm`)
* Sequence-to-sequence Tasks (text -> text, including MT): `task-seq2seq` (implies `task-condlm`)
* Cloze-style Prediction, Masked Language Modeling (right and left context -> word): `task-cloze`
* Context Prediction (as in word2vec) (word -> right and left context): `task-context`
* Relation Prediction (text -> graph of relations between words, including dependency parsing): `task-relation`
* Tree Prediction (text -> tree, including syntactic and semantic parsing): `task-tree`

## Pre-trained Embedding Techniques

* word2vec: `pre-word2vec` (implies `arch-cbow`, `task-cloze`, `task-context`)
* ELMo: `pre-elmo` (implies `arch-bilstm`, `task-lm`)
* BERT: `pre-bert` (implies `arch-transformer`, `task-cloze`, `task-textpair`)

## Structured Models/Algorithms

* Hidden Markov Models (HMM): `struct-hmm`
* Conditional Random Fields (CRF): `struct-crf`
* Context-free Grammar (CFG): `struct-cfg`
* Combinatorial Categorical Grammar (CCG): `struct-ccg`

## Relaxation/Training Methods for Non-differentiable Functions

* Complete Enumeration: `nondif-enum`
* Straight-through Estimator: `nondif-straightthrough`
* Gumbel Softmax: `nondif-gumbelsoftmax`
* Minimum Risk Training: `nondif-minrisk` 
* REINFORCE: `nondif-reinforce` 

## Adversarial Methods

* Generative Adversarial Networks (GAN): `adv-gan`
* Adversarial Feature Learning: `adv-feat`
* Adversarial Examples: `adv-examp`
* Adversarial Training: `adv-train` (implies `adv-examp`)

## Latent Variable Models

* Variational Auto-encoder (VAE): `latent-vae`

## Loss Functions (other than cross-entropy)

* Canonical Correlation Analysis (CCA): `loss-cca`
* Singular Value Decomposition (SVD): `loss-svd`
* Margin-based Loss Functions: `loss-margin`

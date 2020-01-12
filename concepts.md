# Concept Hierarchy in Neural Networks for NLP

Below is a list of important concepts in neural networks for NLP. In the `annotations/` directory in this repository,
we have examples of papers annotated with these concepts that you can peruse.

**Annotation Critera**: For a particular paper, the concept should be annotated if it is important to understand the
proposed method. It should also be annotated if it's important to understand the evaluation. For example, if a
proposed self-attention model is compared to a baseline that uses an LSTM, and the difference between these two
methods is important to understanding the experimental results, then the LSTM concept should also be annotated. Concepts
do not need to be annotated if they are simply mentioned in passing, or in the related work section.

**Implication**: Some tags are listed with "`XXX` (implies `YYY`)" which means you need to understand a particular
concept `XXX` in order to understand concept `YYY`. If `YYY` exists in a paper, you do not need to annotate `XXX`.

**Non-neural Papers**: This conceptual hierarchy is for tagging papers that are about neural network models for NLP.
If a paper is not fundamentally about some application of neural networks to NLP, it should be tagged with `not-neural`,
and no other tags need to be applied.

## Optimization/Learning

### Optimizers

* Mini-batch SGD: `optim-sgd`
* Adam: `optim-adam` (implies `optim-sgd`)
* Adagrad: `optim-adagrad` (implies `optim-sgd`)
* Adadelta: `optim-adadelta` (implies `optim-sgd`)
* Adam with Specialized Transformer Learning Rate ("Noam" Schedule): `optim-noam` (implies `optim-adam`)
* SGD with Momentum: `optim-momentum` (implies `optim-sgd`)
* AMS: `optim-momentum` (implies `optim-sgd`)

### Initialization

* Glorot/Xavier Initialization: `init-glorot`
* He Initialization: `init-he`

### Regularization

* Dropout: `reg-dropout`
* Word Dropout: `reg-worddropout` (implies `reg-dropout`)
* Norm (L1/L2) Regularization: `reg-norm`
* Early Stopping: `reg-stopping`
* Patience: `reg-patience` (implies `reg-stopping`)
* Weight Decay: `reg-decay`
* Label Smoothing: `reg-labelsmooth`

### Normalization

* Layer Normalization: `norm-layer`
* Batch Normalization: `norm-batch`
* Gradient Clipping: `norm-gradient`

### Loss Functions (other than cross-entropy)

* Canonical Correlation Analysis (CCA): `loss-cca`
* Singular Value Decomposition (SVD): `loss-svd`
* Margin-based Loss Functions: `loss-margin`
* Contrastive Loss: `loss-cons`
* Noise Contrastive Estimation (NCE): `loss-nce` (implies `loss-cons`)
* Triplet loss: `loss-triplet` (implies `loss-cons`)

### Training Paradigms

* Multi-task Learning (MTL): `train-mtl`
* Multi-lingual Learning (MLL): `train-mll` (implies `train-mtl`)
* Transfer Learning: `train-transfer`
* Active Learning: `train-active`
* Data Augmentation: `train-augment`

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
* Recursive Neural Network (RecNN): `arch-recnn`
* Tree-structured Long Short-term Memory (TreeLSTM): `arch-treelstm` (implies `arch-recnn`)
* Graph Neural Network (GNN): `arch-gnn`
* Graph Convolutional Neural Network (GCNN): `arch-gcnn` (implies `arch-gnn`)

### Other Sequential Architectures

* Convolutional Neural Networks (CNN): `arch-cnn`
* Attention: `arch-att`
* Self Attention: `arch-selfatt` (implies `arch-att`)

### Architectural Techniques

* Residual Connections (ResNet): `arch-residual`
* Gating Connections, Highway Connections: `arch-gating`
* Memory: `arch-memo`
* Copy Mechanism: `arch-copy`
* Bilinear, Biaffine Models: `arch-bilinear`

### Standard Composite Architectures

* Transformer: `arch-transformer` (implies `arch-selfatt`, `arch-residual`, `arch-layernorm`, `optim-noam`)


## Model Combination

* Ensembling: `comb-ensemble`

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
* Tree Prediction (text -> tree, including syntactic and some semantic semantic parsing): `task-tree`
* Graph Prediction (text -> graph not necessarily between nodes): `task-graph`
* Lexicon Induction/Embedding Alignment (text/embeddings -> bi- or multi-lingual lexicon): `task-lexicon`
* Word Alignment (parallel text -> alignment between words): `task-alignment`

## Composite Pre-trained Embedding Techniques

* word2vec: `pre-word2vec` (implies `arch-cbow`, `task-cloze`, `task-context`)
* GloVe: `pre-glove`
* Skip-thought: `pre-skipthought` (implies `arch-lstm`, `task-seq2seq`)
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
* Topic Model: `latent-topic`

## Meta Learning

* Meta-learning Initialization: `meta-init`
* Meta-learning Optimizers: `meta-optim`
* Meta-learning Loss functions: `meta-loss`
* Neural Architecture Search: `meta-arch`
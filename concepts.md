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

* Mini-batch SGD: [`optim-sgd`](http://pfliu.com/pl-nlp2019/bs/optim-sgd.html) 
* Adam: [`optim-adam`](http://pfliu.com/pl-nlp2019/bs/optim-adam.html) (implies `optim-sgd`)
* Adagrad: [`optim-adagrad`](http://pfliu.com/pl-nlp2019/bs/optim-adagrad.html) (implies `optim-sgd`)
* Adadelta: [`optim-adadelta`](http://pfliu.com/pl-nlp2019/bs/optim-adadelta.html) (implies `optim-sgd`)
* Adam with Specialized Transformer Learning Rate ("Noam" Schedule): [`optim-noam`](http://pfliu.com/pl-nlp2019/bs/optim-noam.html) (implies `optim-adam`)
* SGD with Momentum: [`optim-momentum`](http://pfliu.com/pl-nlp2019/bs/optim-momentum.html) (implies `optim-sgd`)
* AMS: [`optim-amsgrad`](http://pfliu.com/pl-nlp2019/bs/optim-amsgrad.html) (implies `optim-sgd`)

### Initialization

* Glorot/Xavier Initialization: [`init-glorot`](http://pfliu.com/pl-nlp2019/bs/init-glorot.html)
* He Initialization: [`init-he`](http://pfliu.com/pl-nlp2019/bs/init-he.html)

### Regularization

* Dropout: [`reg-dropout`](http://pfliu.com/pl-nlp2019/bs/reg-dropout.html)
* Word Dropout: [`reg-worddropout`](http://pfliu.com/pl-nlp2019/bs/reg-worddropout.html) (implies `reg-dropout`)
* Norm (L1/L2) Regularization: [`reg-norm`](http://pfliu.com/pl-nlp2019/bs/reg-norm.html)
* Early Stopping: [`reg-stopping`](http://pfliu.com/pl-nlp2019/bs/reg-stopping.html)
* Patience: [`reg-patience`](http://pfliu.com/pl-nlp2019/bs/reg-patience.html) (implies `reg-stopping`)
* Weight Decay: [`reg-decay`](http://pfliu.com/pl-nlp2019/bs/reg-decay.html)
* Label Smoothing: [`reg-labelsmooth`](http://pfliu.com/pl-nlp2019/bs/reg-labelsmooth.html)

### Normalization

* Layer Normalization: [`norm-layer`](http://pfliu.com/pl-nlp2019/bs/norm-layer.html)
* Batch Normalization: [`norm-batch`](http://pfliu.com/pl-nlp2019/bs/norm-batch.html)
* Gradient Clipping: [`norm-gradient`](http://pfliu.com/pl-nlp2019/bs/norm-gradient.html)

### Loss Functions (other than cross-entropy)

* Canonical Correlation Analysis (CCA): [`loss-cca`](http://pfliu.com/pl-nlp2019/bs/loss-cca.html)
* Singular Value Decomposition (SVD): [`loss-svd`](http://pfliu.com/pl-nlp2019/bs/loss-svd.html)
* Margin-based Loss Functions: [`loss-margin`](http://pfliu.com/pl-nlp2019/bs/loss-margin.html)
* Contrastive Loss: [`loss-cons`](http://pfliu.com/pl-nlp2019/bs/loss-cons.html)
* Noise Contrastive Estimation (NCE): [`loss-nce`](http://pfliu.com/pl-nlp2019/bs/loss-nce.html) (implies `loss-cons`)
* Triplet loss: [`loss-triplet`](http://pfliu.com/pl-nlp2019/bs/loss-triplet.html) (implies `loss-cons`)

### Training Paradigms

* Multi-task Learning (MTL): [`train-mtl`](http://pfliu.com/pl-nlp2019/bs/train-mtl.html)
* Multi-lingual Learning (MLL): [`train-mll`](http://pfliu.com/pl-nlp2019/bs/train-mll.html) (implies `train-mtl`)
* Transfer Learning: [`train-transfer`](http://pfliu.com/pl-nlp2019/bs/train-transfer.html)
* Active Learning: [`train-active`](http://pfliu.com/pl-nlp2019/bs/train-active.html)
* Data Augmentation: [`train-augment`](http://pfliu.com/pl-nlp2019/bs/train-augment.html)
* Curriculum Learning: [`train-curriculum`](http://pfliu.com/pl-nlp2019/bs/train-curriculum.html)
* Parallel Training: [`train-parallel`](http://pfliu.com/pl-nlp2019/bs/train-parallel.html)

## Sequence Modeling Architectures

### Activation Functions

* Hyperbolic Tangent (tanh): [`activ-tanh`](http://pfliu.com/pl-nlp2019/bs/activ-tanh.html)
* Rectified Linear Units (RelU): [`activ-relu`](http://pfliu.com/pl-nlp2019/bs/activ-relu.html)

### Pooling Operations

* Max Pooling: [`pool-max`](http://pfliu.com/pl-nlp2019/bs/pool-max.html)
* Mean Pooling: [`pool-mean`](http://pfliu.com/pl-nlp2019/bs/pool-mean.html)
* k-Max Pooling: [`pool-kmax`](http://pfliu.com/pl-nlp2019/bs/pool-kmax.html)

### Recurrent Architectures

* Recurrent Neural Network (RNN): [`arch-rnn`](http://pfliu.com/pl-nlp2019/bs/arch-rnn.html)
* Bi-directional Recurrent Neural Network (Bi-RNN): [`arch-birnn`](http://pfliu.com/pl-nlp2019/bs/arch-birnn.html) (implies `arch-rnn`)
* Long Short-term Memory (LSTM): [`arch-lstm`](http://pfliu.com/pl-nlp2019/bs/arch-lstm.html) (implies `arch-rnn`)
* Bi-directional Long Short-term Memory (LSTM): [`arch-bilstm`](http://pfliu.com/pl-nlp2019/bs/arch-bilstm.html) (implies `arch-birnn`, `arch-lstm`)
* Gated Recurrent Units (GRU): [`arch-gru`](http://pfliu.com/pl-nlp2019/bs/arch-gru.html) (implies `arch-rnn`)
* Bi-directional Gated Recurrent Units (GRU): [`arch-bigru`](http://pfliu.com/pl-nlp2019/bs/arch-bigru.html) (implies `arch-birnn`, `arch-gru`)
* Recursive Neural Network (RecNN): [`arch-recnn`](http://pfliu.com/pl-nlp2019/bs/arch-recnn.html)
* Tree-structured Long Short-term Memory (TreeLSTM): [`arch-treelstm`](http://pfliu.com/pl-nlp2019/bs/arch-treelstm.html) (implies `arch-recnn`)
* Graph Neural Network (GNN): [`arch-gnn`](http://pfliu.com/pl-nlp2019/bs/arch-gnn.html)
* Graph Convolutional Neural Network (GCNN): [`arch-gcnn`](http://pfliu.com/pl-nlp2019/bs/arch-gcnn.html) (implies `arch-gnn`)

### Other Sequential Architectures

* Convolutional Neural Networks (CNN): [`arch-cnn`](http://pfliu.com/pl-nlp2019/bs/arch-cnn.html)
* Attention: [`arch-att`](http://pfliu.com/pl-nlp2019/bs/arch-att.html)
* Self Attention: [`arch-selfatt`](http://pfliu.com/pl-nlp2019/bs/arch-selfatt.html) (implies `arch-att`)

### Architectural Techniques

* Residual Connections (ResNet): [`arch-residual`](http://pfliu.com/pl-nlp2019/bs/arch-residual.html)
* Gating Connections, Highway Connections: [`arch-gating`](http://pfliu.com/pl-nlp2019/bs/arch-gating.html)
* Memory: [`arch-memo`](http://pfliu.com/pl-nlp2019/bs/arch-memo.html)
* Copy Mechanism: [`arch-copy`](http://pfliu.com/pl-nlp2019/bs/arch-copy.html)
* Bilinear, Biaffine Models: [`arch-bilinear`](http://pfliu.com/pl-nlp2019/bs/arch-bilinear.html)
* Coverage Vectors/Penalties: [`arch-coverage`](http://pfliu.com/pl-nlp2019/bs/arch-coverage.html)
* Subword Units: [`arch-subword`](http://pfliu.com/pl-nlp2019/bs/arch-subword.html)

### Standard Composite Architectures

* Transformer: [`arch-transformer`](http://pfliu.com/pl-nlp2019/bs/arch-transformer.html) (implies `arch-selfatt`, `arch-residual`, `arch-layernorm`, `optim-noam`)


## Model Combination

* Ensembling: [`comb-ensemble`](http://pfliu.com/pl-nlp2019/bs/comb-ensemble.html)

## Search Algorithms

* Greedy Search: [`search-greedy`](http://pfliu.com/pl-nlp2019/bs/search-greedy.html)
* Beam Search: [`search-beam`](http://pfliu.com/pl-nlp2019/bs/search-beam.html)
* A* Search: [`search-astar`](http://pfliu.com/pl-nlp2019/bs/search-astar.html)
* Viterbi Algorithm: [`search-viterbi`](http://pfliu.com/pl-nlp2019/bs/search-viterbi.html)
* Ancestral Sampling: [`search-sampling`](http://pfliu.com/pl-nlp2019/bs/search-sampling.html)
* Gumbel Max: [`search-gumbel`](http://pfliu.com/pl-nlp2019/bs/search-gumbel.html) (implies `search-sampling`)

## Prediction Tasks

* Text Classification (text -> label): [`task-textclass`](http://pfliu.com/pl-nlp2019/bs/task-textclass.html)
* Text Pair Classification (two texts -> label: [`task-textpair`](http://pfliu.com/pl-nlp2019/bs/task-textpair.html)
* Sequence Labeling (text -> one label per token): [`task-seqlab`](http://pfliu.com/pl-nlp2019/bs/task-seqlab.html)
* Extractive Summarization (text -> subset of text): [`task-extractive`](http://pfliu.com/pl-nlp2019/bs/task-extractive.html) (implies `text-seqlab`)
* Span Labeling (text -> labels on spans): [`task-spanlab`](http://pfliu.com/pl-nlp2019/bs/task-spanlab.html)
* Language Modeling (predict probability of text): [`task-lm`](http://pfliu.com/pl-nlp2019/bs/task-lm.html)
* Conditioned Language Modeling (some input -> text): [`task-condlm`](http://pfliu.com/pl-nlp2019/bs/task-condlm.html) (implies `task-lm`)
* Sequence-to-sequence Tasks (text -> text, including MT): [`task-seq2seq`](http://pfliu.com/pl-nlp2019/bs/task-seq2seq.html) (implies `task-condlm`)
* Cloze-style Prediction, Masked Language Modeling (right and left context -> word): [`task-cloze`](http://pfliu.com/pl-nlp2019/bs/task-cloze.html)
* Context Prediction (as in word2vec) (word -> right and left context): [`task-context`](http://pfliu.com/pl-nlp2019/bs/task-context.html)
* Relation Prediction (text -> graph of relations between words, including dependency parsing): [`task-relation`](http://pfliu.com/pl-nlp2019/bs/task-relation.html)
* Tree Prediction (text -> tree, including syntactic and some semantic semantic parsing): [`task-tree`
* Graph Prediction (text -> graph not necessarily between nodes): [`task-graph`](http://pfliu.com/pl-nlp2019/bs/task-graph.html)
* Lexicon Induction/Embedding Alignment (text/embeddings -> bi- or multi-lingual lexicon): [`task-lexicon`](http://pfliu.com/pl-nlp2019/bs/task-lexicon.html)
* Word Alignment (parallel text -> alignment between words): [`task-alignment`](http://pfliu.com/pl-nlp2019/bs/task-alignment.html)

## Composite Pre-trained Embedding Techniques

* word2vec: [`pre-word2vec`](http://pfliu.com/pl-nlp2019/bs/pre-word2vec.html) (implies `arch-cbow`, `task-cloze`, `task-context`)
* GloVe: [`pre-glove`](http://pfliu.com/pl-nlp2019/bs/pre-glove.html)
* Paragraph Vector (ParaVec): [`pre-paravec`](http://pfliu.com/pl-nlp2019/bs/pre-paravec.html)
* Skip-thought: [`pre-skipthought`](http://pfliu.com/pl-nlp2019/bs/pre-skipthought.html) (implies `arch-lstm`, `task-seq2seq`)
* ELMo: [`pre-elmo`](http://pfliu.com/pl-nlp2019/bs/pre-elmo.html) (implies `arch-bilstm`, `task-lm`)
* BERT: [`pre-bert`](http://pfliu.com/pl-nlp2019/bs/pre-bert.html) (implies `arch-transformer`, `task-cloze`, `task-textpair`)
* Universal Sentence Encoder (USE): [`pre-use`](http://pfliu.com/pl-nlp2019/bs/pre-use.html) (implies `arch-transformer`, `task-seq2seq`)

## Structured Models/Algorithms

* Hidden Markov Models (HMM): [`struct-hmm`](http://pfliu.com/pl-nlp2019/bs/struct-hmm.html)
* Conditional Random Fields (CRF): [`struct-crf`](http://pfliu.com/pl-nlp2019/bs/struct-crf.html)
* Context-free Grammar (CFG): [`struct-cfg`](http://pfliu.com/pl-nlp2019/bs/struct-cfg.html)
* Combinatorial Categorical Grammar (CCG): [`struct-ccg`](http://pfliu.com/pl-nlp2019/bs/struct-ccg.html)

## Relaxation/Training Methods for Non-differentiable Functions

* Complete Enumeration: [`nondif-enum`](http://pfliu.com/pl-nlp2019/bs/nondif-enum.html)
* Straight-through Estimator: [`nondif-straightthrough`](http://pfliu.com/pl-nlp2019/bs/nondif-straightthrough.html)
* Gumbel Softmax: [`nondif-gumbelsoftmax`](http://pfliu.com/pl-nlp2019/bs/nondif-gumbelsoftmax.html)
* Minimum Risk Training: [`nondif-minrisk` ](http://pfliu.com/pl-nlp2019/bs/nondif-minrisk.html)
* REINFORCE: [`nondif-reinforce` ](http://pfliu.com/pl-nlp2019/bs/nondif-reinforce.html)

## Adversarial Methods

* Generative Adversarial Networks (GAN): [`adv-gan`](http://pfliu.com/pl-nlp2019/bs/adv-gan.html)
* Adversarial Feature Learning: [`adv-feat`](http://pfliu.com/pl-nlp2019/bs/adv-feat.html)
* Adversarial Examples: [`adv-examp`](http://pfliu.com/pl-nlp2019/bs/adv-examp.html)
* Adversarial Training: [`adv-train`](http://pfliu.com/pl-nlp2019/bs/adv-train.html) (implies `adv-examp`)

## Latent Variable Models

* Variational Auto-encoder (VAE): [`latent-vae`](http://pfliu.com/pl-nlp2019/bs/latent-vae.html)
* Topic Model: [`latent-topic`](http://pfliu.com/pl-nlp2019/bs/latent-topic.html)

## Meta Learning

* Meta-learning Initialization: [`meta-init`](http://pfliu.com/pl-nlp2019/bs/meta-init.html)
* Meta-learning Optimizers: [`meta-optim`](http://pfliu.com/pl-nlp2019/bs/meta-optim.html)
* Meta-learning Loss functions: [`meta-loss`](http://pfliu.com/pl-nlp2019/bs/meta-loss.html)
* Neural Architecture Search: [`meta-arch`](http://pfliu.com/pl-nlp2019/bs/meta-arch.html)

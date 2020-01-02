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

* Transformer: `arch-transformer` (implies `arch-selfatt`, `arch-residual`, `arch-layernorm`)

## Search Algorithms

* Greedy Search: `search-greedy`
* Beam Search: `search-beam`
* A* Search: `search-astar`
* Viterbi Algorithm: `search-viterbi`

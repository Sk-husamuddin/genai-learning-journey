# SIMPLE

A neural network is a computer system designed to learn like a human brain by finding patterns from examples.
It’s like teaching a child to recognize cats by showing many cat photos until they learn the pattern themselves.

# MEDIUM

A neural network is a machine learning model made of interconnected layers of artificial neurons.
Each neuron receives inputs, applies weights and biases, and passes the result through an activation function.
The network learns by adjusting these weights using training data and an algorithm called backpropagation.
It is widely used in image recognition, language processing, recommendation systems, and AI assistants.
Deep neural networks contain many hidden layers, allowing them to learn complex patterns.

# DEEP

A neural network works mathematically by transforming input data layer by layer.

### Step 1: Input Layer

The input layer receives raw data:

* Pixels for images
* Words/tokens for text
* Numbers/features for datasets

Example:
If recognizing handwritten digits, each pixel becomes an input value.

### Step 2: Weighted Connections

Each neuron multiplies inputs by weights:

y=\sum_{i=1}^{n} w_i x_i + b

* (x_i) = inputs
* (w_i) = learned importance
* (b) = bias

Weights determine how strongly a feature affects the output.

### Step 3: Activation Function

The neuron output passes through an activation function like:

* ReLU
* Sigmoid
* Tanh

This introduces non-linearity so the network can learn complex relationships instead of just straight-line patterns.

Example ReLU:

f(x)=\max(0,x)

Without activation functions, deep networks would behave like simple linear models.

### Step 4: Forward Propagation

Data moves from input → hidden layers → output layer.
Each layer extracts higher-level features:

* Early layers detect edges
* Middle layers detect shapes
* Final layers detect objects

### Step 5: Loss Calculation

The prediction is compared with the correct answer using a loss function.

Example:

* Predicted = Cat
* Actual = Dog
* Loss = High

The goal is minimizing loss.

### Step 6: Backpropagation

The network calculates how much each weight contributed to the error.
Using gradient descent, it updates weights to reduce future mistakes.

Gradient descent idea:

w_{new}=w_{old}-\eta\frac{\partial L}{\partial w}

* (L) = loss
* (\eta) = learning rate

### Important Tradeoffs

* **More layers** → better learning but slower training
* **Too little training** → underfitting
* **Too much training** → overfitting
* **Large models** need huge datasets and GPUs

### Edge Cases

* Neural networks can memorize instead of generalize
* Biased data creates biased predictions
* Vanishing gradients can make deep training difficult
* Adversarial inputs can fool networks with tiny changes

### Types of Neural Networks

* Feedforward Neural Networks
* Convolutional Neural Networks (CNNs)
* Recurrent Neural Networks (RNNs)
* Transformers

Modern AI systems like OpenAI models mainly use transformer-based neural networks.

```json
{
  "quiz": [
    {
      "question": "What is the main purpose of weights in a neural network?",
      "answer": "Weights determine how important each input is for making predictions."
    },
    {
      "question": "Why are activation functions used in neural networks?",
      "answer": "They introduce non-linearity so the network can learn complex patterns."
    },
    {
      "question": "What does backpropagation do?",
      "answer": "It updates weights by calculating and reducing prediction errors."
    }
  ]
}
```

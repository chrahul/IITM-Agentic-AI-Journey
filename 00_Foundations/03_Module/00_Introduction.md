## Section 3: Handling Sequential Data

### The Thread Running Through All Four Modules

Everything in Section 2 treated inputs as flat, unordered collections of numbers. Feed a network an image: 150,528 independent pixel values. Feed it a customer record: 10 independent features. Order did not matter. Context did not matter.

But now consider this sentence:

"The trophy did not fit in the suitcase because it was too big."

What does "it" refer to? The trophy or the suitcase?

A human instantly knows: the trophy. Because "too big" in the context of "did not fit" tells you the thing that was too big must be the thing that failed to fit.

That reasoning requires memory of what came before and understanding of how earlier words constrain the meaning of later ones. No flat neural network can do this. You need a fundamentally different architecture.

Section 3 is the story of how researchers tried to solve this, what worked, what did not, and what limitations ultimately forced the invention of the Transformer in 2017.

---

## The Four Modules

**Module 3.1: The Sequence Problem**
Why order matters — text, time-series, speech, video. What traditional neural networks literally cannot do. The need for memory in models. Context: the Zomato order prediction problem where knowing yesterday's orders matters. No lab (conceptual bridge).

**Module 3.2: Recurrent Neural Networks**
The elegant solution: feed the output back as input. How RNNs maintain a hidden state across time steps. Early successes. Context: teaching an RNN to predict the next character in text — students see it generating plausible words. Lab on Colab: build a character-level RNN from scratch.

**Module 3.3: The Vanishing Gradient Problem in RNNs**
Why RNNs forget. The specific mathematical reason gradients die over long sequences. Real-world failures this caused. Context: the machine translation problem that motivated the solution. No lab (diagnostic and conceptual).

**Module 3.4: LSTMs and GRUs**
The gated memory cell solution. How LSTMs decide what to remember, what to forget, and what to output. GRUs as the streamlined version. Why they solved the vanishing gradient but introduced a new bottleneck: sequential processing. Lab on Colab: compare vanilla RNN vs LSTM on a long-sequence task — the accuracy gap makes the lesson concrete.


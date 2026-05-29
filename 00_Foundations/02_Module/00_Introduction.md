## Where We Are

Section 1 is fully complete and recorded. Five modules, four labs, one PPT. Students now have a solid ML foundation.

---

## What Section 2 Covers

Section 2 answers the question we left on the bridge slide:

**"If ML worked so well, why did we need something completely new?"**

The answer is what created the modern AI era.

Here is the full Section 2 plan from our master ToC, refined with the same narrative structure we used in Section 1:

---

### Section 2: The Shift to Deep Learning

**The thread running through all four modules:**
Classical ML hit a wall. That wall had a specific shape. Breaking through it required new hardware, a new architecture, and one moment in 2012 that nobody expected.

---

**Module 2.1: The Limitations of Classical ML**

The bottleneck this solves: Why did ML engineers keep hitting a ceiling no matter how much data they added?

Context: A team at Google Photos in 2011 trying to auto-tag images. They have a great supervised learning model. They feed it more data. Accuracy plateaus. They try different algorithms. Still plateaus. Something is fundamentally broken.

Concepts: The feature engineering bottleneck, why humans cannot hand-craft features for images and text, what "unstructured data" means and why classical ML chokes on it, the curse of dimensionality.

Real examples: Amazon product image search, Google Translate pre-2016, Facebook face tagging early days.

No lab (conceptual bridge module, like 1.1).

---

**Module 2.2: Enter Neural Networks**

The bottleneck this solves: Can we make the machine discover features automatically instead of humans engineering them?

Context: The biological inspiration story, how a single artificial neuron works, why layering neurons creates something qualitatively different.

Concepts: Perceptron to multi-layer network, forward pass intuition, what "learning" means in a neural network (adjusting weights), activation functions without the math (just the intuition), automatic feature learning as the key breakthrough.

Real examples: How layers learn edges then shapes then faces (image recognition), how the same principle applies to text.

Lab: Build a neural network from scratch using only NumPy to feel the mechanics, then rebuild it in 5 lines with scikit-learn to see the abstraction.

---

**Module 2.3: The Deep Learning Renaissance (The 2012 Moment)**

The bottleneck this solves: Neural networks were known since the 1960s. Why did they suddenly explode in 2012?

Context: The ImageNet challenge story. Five years of results stuck at 75% accuracy. Then AlexNet scores 85%. The AI community's reaction. What changed between 1980 and 2012 to make this possible.

Concepts: The three ingredients that unlocked deep learning (data at scale, compute, algorithmic improvements like ReLU and dropout), why depth matters (hierarchical feature learning), the ImageNet dataset as a catalyst.

Real examples: The AlexNet architecture in plain language, what the layers actually learned to detect.

No lab (narrative and conceptual).

---

**Module 2.4: The Hardware Revolution**

The bottleneck this solves: Even with the right architecture and data, training took weeks on CPUs. What made it feasible?

Context: A gaming GPU in 2007 sitting next to a server CPU. A researcher notices something. The GPU is doing the same matrix multiplications neural networks need, just for pixels instead of weights.

Concepts: Why neural network training is embarrassingly parallel, CPU vs GPU architecture (few powerful cores vs thousands of small cores), matrix multiplication as the primitive operation, the economics of cloud GPUs today (AWS, Google Cloud, Azure).

Real examples: Training time comparison CPU vs GPU for a real model, how this changed who could afford to do AI research.

Lab: Run a training job on CPU vs GPU (using Google Colab's free GPU), measure the speedup, discuss what this means for cloud AI economics.

---

## The Narrative Arc of Section 2

```
Classical ML is great → but hits a wall with unstructured data
    |
    v
Neural networks can learn features automatically → but were too slow and data-hungry
    |
    v
2012: Three things converged → data at scale, GPUs, better algorithms
    |
    v
Deep Learning was born → and the AI world was never the same
```

---

## Before We Start 
Make sure you have Google Colab access.
This matters for the GPU lab in Module 2.4 specifically. 
Colab gives free GPU access which makes that lab very clean. 

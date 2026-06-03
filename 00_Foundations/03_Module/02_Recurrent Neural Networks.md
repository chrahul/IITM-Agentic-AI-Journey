# Module 3.2: Recurrent Neural Networks

## CONTEXT: The Letter That Started the Conversation

It is 1986. David Rumelhart, Geoffrey Hinton, and Ronald Williams publish backpropagation. The deep learning community is excited. But a separate group of researchers is wrestling with a different question: backpropagation works beautifully for fixed-size inputs. What about inputs that arrive one step at a time, where each step depends on what came before?

The answer they land on is elegant in its simplicity: what if the network had a loop? What if instead of information flowing strictly forward from input to output, some of it looped back and fed into the next step?

That loop is the RNN. And the moment students see it — really see it — is one of those genuine "aha" moments in this course.

---

## CONCEPT: The Core Idea — Feeding Output Back as Input

Let us start with a completely concrete example before touching any architecture.

You are trying to predict the next word in this sentence: "The food at Zomato's restaurant was absolutely..."

As a human, you read left to right. By the time you reach "absolutely", you have accumulated context: it is about food, it is at a restaurant, something positive is building ("absolutely" suggests praise is coming). You predict "delicious."

A flat network would see: the food at Zomatos restaurant was absolutely. Twelve independent tokens with no sense of flow or context accumulation.

An RNN does what you do: reads one word at a time, and after each word, updates an internal summary that carries forward. When it reaches "absolutely," its internal summary already encodes "food, restaurant, positive sentiment building" — and it predicts "delicious."

The mechanism is a single loop. After processing each input, the network produces both an output and a hidden state. That hidden state is fed back into the network as an additional input at the next step. The network processes step 2 with both the new input and the memory of step 1. Step 3 gets the new input plus the memory of everything up to step 2. And so on.

Let us see this unrolled:Walk through all eight steps with students. The critical observation is at step 7 — "absolutely." By this point, the hidden state has accumulated six steps of context. The RNN knows this is about food at a restaurant and something strongly positive is building. Without the hidden state — without memory — "absolutely" alone tells you almost nothing.

---

## CONCEPT: The Folded vs Unrolled View

RNNs are drawn two ways and students often find the transition between them confusing. Let us nail it here.

In the folded view, you see a single box with an arrow looping back to itself. The loop represents "take this hidden state and feed it back into myself at the next step."

In the unrolled view, you copy that same box once per time step and draw the hidden state arrows flowing horizontally. The weights inside every box are identical — it is the same network, just applied repeatedly.

The unrolled view makes it clear that an RNN is just a deep network turned on its side, where depth in time replaces depth in layers.The weights are identical at every step — that is the key. A single set of weights is shared across all time steps. The network does not get bigger as the sequence gets longer. The same parameters that process step 1 also process step 50. Only the hidden state changes, carrying whatever context has accumulated.


<img width="1440" height="764" alt="image" src="https://github.com/user-attachments/assets/86cd7383-08a5-4c6e-a45a-7ab74a8bdfcc" />


---

## CONCEPT: What the RNN Cell Actually Computes

Inside each time step, the math is straightforward. The hidden state at each step is computed from two things: the current input and the previous hidden state. These are combined, passed through an activation function (tanh was the classic choice, giving outputs between -1 and 1), and become the new hidden state. That hidden state is also passed to an output layer to make a prediction.

The beautiful simplicity here: the same weights are used to process both the current input and the incoming memory. The network learns how to blend new information with old context. Different inputs end up weighted differently depending on what the network has learned is important to remember.

---

## CONCEPT: RNN Applications and Early Successes

Before the limitations became apparent (that is Module 3.3's territory), RNNs produced genuinely impressive results in the early 2010s. Here is the application landscape:By 2014, RNNs were producing state-of-the-art results on speech recognition (Google's voice search), basic machine translation, and text generation. The architecture was working. But researchers were starting to notice something troubling with longer sequences — a problem that would take until Module 3.3 to fully articulate.


<img width="1440" height="776" alt="image" src="https://github.com/user-attachments/assets/57083e5a-30c1-45bb-a131-175dbdfaf998" />

---

## LAB: Build an RNN on Google Colab

Now the most memorable lab in this module. Students will watch a character-level RNN learn to generate text from scratch — starting with completely random noise and gradually producing recognizable words, then phrases, then plausible sentences.

The moment when recognizable English words start emerging from random characters is one of the best learning experiences in this entire course. Students will see RNN memory working in practice.---

# Module 3.2 Complete

## What We Built

**CONTEXT:** The 1986 loop idea — what if some of the network's output fed back as input at the next step? That single design decision is the entire RNN.

**CONCEPT:** Three rich interactive visuals:

1. Word-by-word RNN stepper — students click through "The food at this restaurant was absolutely delicious" one word at a time and watch the hidden state description update at each step, making memory accumulation tangible

2. Folded vs unrolled diagram — the same cell copied across time steps with shared weights, showing that an RNN is just a deep network turned on its side

3. RNN application type grid — five clickable cards covering every major use case (one-to-many, many-to-one, many-to-many same/different length, time-series), each with a real India-relevant example

**LAB (Google Colab, 10 cells + summary):**

- Cell 2: One RNN time step in pure NumPy — students see the exact `z = x @ Wx + h @ Wh + b; h = tanh(z)` computation printed step by step
- Cells 3-7: Character-level text generation that trains in four visible stages (5, 10, 20, 30 epochs) — students watch noise become words become phrases in real time
- Cell 9: Temperature experiment — same model, four temperatures, shows how creativity is a dial not a switch (ChatGPT uses the same parameter)
- Cell 10: Bonus Zomato demand forecasting — same SimpleRNN architecture on numerical time-series, proves the architecture generalizes beyond text
- Summary challenge: "change SEQ_LEN to 200 and retrain — does more context help?" — this is the exact question that opens Module 3.3

---

## Course Progress

| Section | Module | Status |
|---|---|---|
| Section 3 | 3.1 The Sequence Problem | Done |
| Section 3 | 3.2 Recurrent Neural Networks | Done |
| Section 3 | 3.3 The Vanishing Gradient Problem | Next |


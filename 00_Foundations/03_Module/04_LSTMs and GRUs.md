# Module 3.4: LSTMs and GRUs

## CONTEXT: The Memory Cell That Changed Everything

It is 1997. Sepp Hochreiter and Jürgen Schmidhuber publish a paper called "Long Short-Term Memory." The research community largely ignores it for years.

Then in 2013-2014, Google's speech recognition team, Baidu's voice search team, and several machine translation groups all independently rediscover it. Suddenly LSTM is everywhere — and performance on every long-sequence task jumps dramatically.

What did Hochreiter and Schmidhuber invent?

They looked at the vanishing gradient problem from Module 3.3 and asked a fundamentally different question. Instead of asking "how do we make the gradient travel better through the existing RNN structure?" they asked: "what if we gave the network a completely separate memory lane — one that gradients can travel through without being multiplied by small numbers?"

The answer was the cell state. A horizontal conveyor belt running the full length of the sequence, carrying information forward with minimal transformation. The key insight: if you can add and subtract from this belt using learned gates, but mostly leave it alone, then gradients can flow backward through the additions instead of through the multiplications. Additions preserve gradient magnitude. Multiplications by small numbers destroy it.

This is the core idea. Everything else is engineering around it.

---

## CONCEPT: The Three Gates of an LSTM

An LSTM cell has one more component than a vanilla RNN: the cell state `C`. Think of `h` (the hidden state) as short-term working memory — what the model is actively thinking about right now. Think of `C` (the cell state) as long-term memory — what the model has decided to preserve across many steps.

The cell state is controlled by three learned gates. Each gate is a sigmoid neural network (output between 0 and 1) that decides how much of something to let through — zero means block completely, one means let everything through.

Let us walk through each gate:Walk through all three gates carefully with students. The moment that usually produces the "aha" is gate 2 — when they realize the input gate is deciding not just what to write into memory but how strongly to write it. The cell state update is an addition, not a replacement. Old memory plus new information. That additive structure is the gradient highway.

---

## CONCEPT: Why Additions Solve the Vanishing Gradient

This is the single most important technical insight in the module. Worth spending real time on it.

In a vanilla RNN, the hidden state at each step is completely recalculated:

```
h_new = tanh(W * x + U * h_prev + b)
```

Every step multiplies by the weight matrix `U`. Every `tanh` squishes gradients. Over 50 steps, the gradient from step 50 has been multiplied by 50 small numbers and is effectively zero.

In an LSTM, the cell state update is an addition:

```
C_new = forget_gate * C_prev + input_gate * candidate
```

When a gradient flows backward through an addition, it passes through unchanged. When it flows backward through the forget gate (which is close to 1 when the model decides to remember), it is multiplied by a number close to 1 — so it stays strong.

The cell state is a direct path from the present back to the past. Gradients can travel all the way back to step 1 without being multiplied away, as long as the forget gate kept that memory alive.The circle sizes represent gradient strength flowing from right (the present) backward to left (the past). In the vanilla RNN, the gradient is near zero by step 3. In the LSTM cell state, it remains strong all the way back to step 1. The model can actually learn from events that happened 50 or 100 steps ago.

---

## CONCEPT: GRU — The Streamlined Version

In 2014, Kyunghyun Cho and colleagues introduced the Gated Recurrent Unit (GRU). It takes the core insight of the LSTM and simplifies it: instead of three gates and a separate cell state, use two gates and a single hidden state.

The two GRU gates are the reset gate (how much of the past hidden state to forget when computing new candidate values) and the update gate (how much of the old hidden state to keep versus how much of the new candidate to adopt). The update gate essentially combines the forget and input gates of the LSTM into a single operation.In practice, GRU and LSTM perform comparably on most tasks. GRU trains faster and uses less memory because it has fewer parameters. LSTM is sometimes more expressive on tasks requiring very fine-grained control over what to remember and forget. The practitioner rule is simple: try GRU first. Switch to LSTM if you need more capacity.

---

## CONCEPT: Real-World Impact — What LSTMs Unlocked

Let us be concrete about what became possible once LSTMs replaced vanilla RNNs:

**Google Voice Search (2015):** Switched from vanilla RNN to LSTM for acoustic modeling. Word error rate dropped by 49% — from roughly 23% to 12% in noisy conditions. Suddenly voice search became actually usable.

**Google Translate Neural Machine Translation (2016):** An 8-layer LSTM encoder-decoder replaced the statistical phrase-based system that had been the standard for a decade. Quality scores on some language pairs improved more in a single year than in the previous ten years combined.

**Siri and Cortana:** Both switched to LSTM-based language understanding, enabling much more accurate interpretation of longer, more complex spoken requests.

**Amazon product reviews sentiment analysis:** LSTM-based models could finally handle the "but the second half was disappointing" problem from Module 3.3 — correctly weighting conclusion sentiment against earlier positive content across long reviews.

---

## CONCEPT: The Remaining Limitation

LSTM solved the vanishing gradient problem. But it introduced a new bottleneck that would take until 2017 to crack.

LSTMs are still sequential. You process token 1, then token 2, then token 3. You cannot process token 3 until token 2 is done. You cannot process token 2 until token 1 is done. The chain is inherently linear in time.

This means training cannot be parallelized across the sequence. A sentence with 100 tokens requires 100 sequential steps. On a GPU with thousands of parallel cores, you are using almost none of them for the sequence dimension — all that parallel power sits idle waiting for the previous step to finish.

This bottleneck is exactly what the Transformer architecture solved in 2017 — and it is the opening problem of Section 4.

---

## LAB: RNN vs LSTM on a Long-Sequence Task

Now the proof. We will train both architectures on the same task with the same data and measure the gap. The task is designed to require long-range memory — making the LSTM advantage visible.---

# Module 3.4 Complete — Section 3 Complete!

## What We Built

**CONTEXT:** The 1997 paper nobody read for years — and why 2013 changed that. Hochreiter and Schmidhuber's core insight: give gradients an additive highway through long sequences.

**CONCEPT:** Three interactive visuals plus two structural diagrams:

1. Three-gate stepper — forget gate (selective eraser), input gate (selective writer), output gate (selective reader), each with a real translation and sentiment example showing what that gate does in practice

2. Gradient highway diagram — circles representing gradient strength shrinking to near-zero by step 3 for vanilla RNN, staying large all the way to step 1 for LSTM cell state, making the mathematical solution visually obvious

3. LSTM vs GRU comparison diagram — five components vs three, showing exactly what GRU simplifies and why it is often the right first choice

**LAB (Google Colab, 10 cells):**
- Trains vanilla RNN, LSTM, and GRU on real IMDB movie reviews (25,000 training samples, 200 tokens each)
- Compares all three on test accuracy, learning curves, and training time in a single chart
- Crafted review test showing long-range memory working (or failing) in practice
- Sequence length ablation: cuts reviews to 20, 50, 100, 150, 200 tokens and shows the accuracy gap widening — the vanishing gradient problem made directly measurable

---

## Section 3 Complete

| Module | Status |
|---|---|
| 3.1 The Sequence Problem | Done |
| 3.2 Recurrent Neural Networks | Done |
| 3.3 The Vanishing Gradient Problem | Done |
| 3.4 LSTMs and GRUs | Done |


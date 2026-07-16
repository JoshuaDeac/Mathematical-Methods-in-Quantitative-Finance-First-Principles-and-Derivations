## P - Value

p-values are very closely related to [Z-scores](../theory/Z-Score.md), basically a bi-product of their calculation.

## Formula 

Formula for P-value (for a Z-score):For a one-tailed test (looking only at the "right" tail):

* $$P = 1 - \Phi(Z)$$

For a two-tailed test (the standard for trading, looking at both extremes):

* $$P = 2 \times (1 - \Phi(\vert{}Z\vert{}))$$


There is no "Simple" Formula The Normal Distribution curve is defined by this equation:

* $$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x^2}$$

To find the area (the P-value), you must calculate the definite integral of that function:


* $$\Phi(Z) = \int_{-\infty}^{Z} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}t^2} dt$$


This integral cannot be solved with basic algebra. It has no "closed-form" solution.




## Definition

The P-value represents the area under the bell curve that lies beyond your Z-score

Note: Assumes a normal distribution of data

## Context

If $Z = 0$: The price is at the mean. The P-value is $1.0$ (or $100\%$). It is not rare at all; it happens all the time.

If $Z = 2$: You look at a Z-table (or use a function) to find the area in the "tail" of the curve. That area is $$\approx 0.0228 \implies $$ There is a $2.28\%$ probability of seeing a price move this extreme (or more extreme) by pure random chance.


## Why?

In science, you use the P-value to see if an experiment was "successful." In trading, you use it to see if a price move is "true" or "random noise."

If you have a strategy then its standard practice to expect p < 0.05.
However depending on your data/ circumstances you might take p < 0.10 for High Frequency Trading or for options/ more risky assets p < 0.01.

There are trade offs naturally.


## QnA 1:

Why does assuming only a normal distribution make things dangerous for trading?

Answer: It creates a "false sense of security." Assuming a normal distribution underestimates the frequency and chances of extreme events happening. Because real financial data has "fat tails" extreme moves happen significantly more often than the bell curve predicts. Relying solely on normal distribution math often leaves you unprepared for the true level of risk in sudden, high volatile markets.

## Note

By now you would have guessed but it depends on what distribution you assume, that gives you a different p-value. Instead of the normal distribution formula there are many other pdf's which can be considered.
( this is why we assume some prerequisites in probability )


## QnA 2: 
Assume normal distribution for sake of the question.
Why would a quant prefer to write their code to trigger a "Buy" signal based on a Z-Score (e.g., $Z < -2$) rather than a dollar-amount deviation (e.g., "Price is $10 below the mean")?

Well its because a z-score is universal measurement so even if the asset price doubles that same sd wont trigger, but a z-score will adjust accordingly. The strategy automatically adjusts to the asset's volatility.










## P - Value

p-values are very closely related to [Z-scores](../theory/Z-Score.md), basically a bi-product of their calculation.

## Formula 

There is no "Simple" FormulaThe Normal Distribution curve is defined by this equation:$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x^2}$$To find the area (the P-value), you must calculate the definite integral of that function:$$\Phi(Z) = \int_{-\infty}^{Z} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}t^2} dt$$This integral cannot be solved with basic algebra. It has no "closed-form" solution.




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











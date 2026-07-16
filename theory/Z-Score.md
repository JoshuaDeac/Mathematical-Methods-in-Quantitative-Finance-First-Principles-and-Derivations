## Z-Scores

## Definition

Z-score are very closely related to [Standard Deviations](../theory/Standard-Dev.md) we are simply putting a formal name to that distance.


$$Z = \frac{P - \mu}{\sigma}$$

* $P$: The current price.
* $\mu$: The mean (average) price.
* $\sigma$: The standard deviation

## Why?

In quant finance, the Z-Score is the "Great Equalizer" It allows you to take two completely different assets say, Bitcoin (which is very volatile) and a stable Treasury Bond and allows you to compare their price moves on the exact same scale.

For example you might think there is no difference between sd and z-score which is understandable but the key difference is that when we calculate a z-score we assume a normal distribution of data and as such we can give each of our z-scores probabilities.

On top of this a Z-score is standardized, but what is it standardizing? Well everything you can turn dollars into a z-score, you can turn kilometers into a z-score, basically turn anything that you assume has normal distribution into a relevant probability.

Thats why its so powerful in allowing you to calculate very different assets side by side.


## Relation to P-value

If we assume asset returns follow a "Normal Distribution," we can map every Z-score to a specific probability.

If your Z-score is $2$, you can look it up in a Z-table and see that the probability of the price being that high or higher is about $2.28\%$.

## Relation to P-value

If we assume asset returns follow a "Normal Distribution," we can map every Z-score to a probability (P-value).

### Key Concepts:
* **The Two-Tailed Test:** In trading, we care about extremes in both directions. Therefore, we use a two-tailed threshold (e.g., $|Z| > 2$).
* **Confidence Intervals:** 95% of data typically falls within $Z \approx \pm 1.96$. Anything outside this is considered statistically significant.
* **The "Fat Tail" Warning:** Financial data is "leptokurtic." Extreme moves (high Z-scores) happen more often than the Z-table suggests.









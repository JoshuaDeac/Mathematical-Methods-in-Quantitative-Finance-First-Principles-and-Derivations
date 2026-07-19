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

[P-Value](../theory/P_Value.md)

If we assume asset returns follow a "Normal Distribution" (or some other distribution ) we can map every Z-score to a probability (P-value).

Think of the Z-score as the location and the P-value as the probability of that location.

## Theoretical side for math and quants

If you were able to make a distribution( like the normal one) which could capture how the market moves, you would simply just need to get, the z-scores and p values and you would have an edge instantly, however it is very difficult to do for a few reasons, the main one being that the market changes and adapts constantly. Your distribution could be great in 2024 but not so much in 2026. Hence if you were able to make a distribution for all of 2026 or 2027 then you could have made money already using those predictive models and methods.

There is quite a lot on this topic such as limits to how much you could make and so on. However if you have gotten this far you can clearly see how knowing the math alone can get you places.

## QnA 1: 

Assume normal distribution for sake of the question.
Why would a quant prefer to write their code to trigger a "Buy" signal based on a Z-Score (e.g., $Z < -2$) rather than a dollar-amount deviation (e.g., "Price is $10 below the mean")?

Well its because a z-score is universal measurement so even if the asset price doubles that same sd wont trigger, but a z-score will adjust accordingly. The strategy automatically adjusts to the asset's volatility.


## Noted assumption

The Stationarity Assumption
The Z-score assumes that the mean ($\mu$) and standard deviation ($\sigma$) are stable over time. In real markets, this is often false, volatility changes. If an asset is in a strong trend, the mean is moving, which can make a Z-score signal misleading. Always verify if your data is stationary before relying solely on these metrics.




## QnA 2:

If Asset A has a Z-score of $2.0$ and Asset B has a Z-score of $0.5$, which asset is currently exhibiting more "extreme" behavior relative to its recent history?
( I dont want to say "Asset X is the answer" so it spoils the fun ).The first asset is the correct answer.



## Standard Deviation

## Definition

Standard deviation is a statistical measure of how spread out the numbers in a dataset are from their average (mean).

We sometimes use the term "sd", short for standard deviation.

## Important Assumption

It is important to note that when we talk about standard deviations in the context of asset prices, we are assuming that asset returns are normally distributed. You may make this assumption occasionally to help simplify things, but this is **not** the truth, **especially** in more volatile markets such as Cryptocurrency.

## Context

"This assets price is currently one almost two sd away from the mean"- some cool trader ( probably me )

If an assets price (that day) is within 1 sd from the mean, it can considered to be normal and not very volatile. Statistically speaking, about 68% of the time, the price of an asset on any given day will stay within one SD of the mean. This is the "normal" stuff that happens every day. 

If an assets price (that day) is more than two sd away from the mean it means the price (that day) is unusually high or low compared to the mean, we would consider this day to be relatively odd and "highly volatile". Statistically speaking, about 95% of the time, the price of an asset on any given day will stay within 2 SDs of it's mean. i.e 95% of the price data should be within 2 sd's from the mean.

If an assets price (that day) is more than three sd away from the mean this is a very rare event and a very volatile day. Statistically speaking, it should be about 99.7% of the data that stays within 3 sd. 

However dont get mixed up when using them, for example if we calculate sd = 5, that does not mean a price is 5 sd away from it's mean, it means that one sd = 5, so if SMA = 100 then within one sd of that SMA would be any prices in the range (95,105) and about 70% of the asset's prices should be within this interval. Within two sd would be prices within (90,110) and so on.

So when someone says "the current price is x standard deviations away from the SMA", they mean that the price right now is SMA +/- sd*x.


## Formula

Note: sd is not a constant value say like meters, if you go to Japan a meter will still be a meter but a sd is not the same for every piece of data/asset


$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (P_i - \mu)^2}$$

* $\sigma$ represents the Standard Deviation.
* $\mu$ is the mean (average) of the prices. 

* $$P_i$$ is each individual price in your set.

* n is the total number of prices.



This is the formula, although it looks scary it is justified.

The part inside the root is actually the formula for variance. Then simply rooting it gives us sd.

They are very closely related: volatility, standard dev's and variance.


## QnA 1:

If you are someone who hates risk and wants to keep your money safe, would you prefer an asset with a high or low standard deviation?

You would pick the asset with a smaller relative sd, as this indicates that the price of the asset will move less from its mean.


## Note:

Standard deviations can be any number from 0 to $\inf$, the higher the number the more volatile and rare the events get i.e less predictable


## QnA 2: 

Asset A has a standard deviation of 2. Asset B has a standard deviation of 15. Both have a mean value of 100.

If Asset A is currently 105, it is a very rare, "surprising" event.

If Asset B is currently 105, it is a completely normal, everyday occurrence.

Why does the standard deviation change how we interpret the exact same price (105)? Answer this yourself and if you are confident then you are done here.














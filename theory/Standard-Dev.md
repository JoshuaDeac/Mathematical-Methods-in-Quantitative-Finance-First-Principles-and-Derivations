## Standard Deviation

## Definition
Standard deviation is a statistical measure of how spread out the numbers in a dataset are from the average (mean).

use "sd" short for standard deviation 

## Context

This assets price is currently one almost two sd away from the mean

If an assets price (that day ) is one sd away from the mean $\implies$ it is considered to be normal and not very volatile ( statistically speaking: About 68% of the time, the price ( of an asset on any given day ) will stay within one SD of the average. This is the "normal" stuff that happens every day. )

If an assets price (that day ) is two sd away from the mean $\implies$  the price (that day) is quite unusually high or low compared to the mean, we would consider this day to be very odd and subject to high volatility. ( statistically speaking: About 95% of the time, the price( of an asset on any given day ) will stay within 2 SDs of the average. i.e 95% of data should be within 2 sd's way from the mean )

If an assets price (that day ) is three sd away from the mean $\implies$ this is a very rare event and very volatile.( statistically speaking: it should be about 99.7% of data that stays within 3 sd )

However dont get mixed up when using them, for example if we calculate sd = 5, that does not mean an asset is 5 sd away, it means that one sd = 5, so if SMA = 100 then one sd would be from (95,105) and about 70% of the asset should be encompassed within this interval. Two sd would be from (90,110) and so on.

So when someone says "its x standard deviations away" they are just talking about $$x \times sd$$ + mean = current price they are talking about.


## Formula

Note: sd is not a constant value say like meters, if you go to Japan a meter will still be a meter but a sd is not the same for every piece of data/ asset


$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (P_i - \mu)^2}$$

This is the formula, although it looks scary it is justified.

The part inside the root is actually the formula for variance. Then simply rooting it gives us sd.

They are very closely related: volatility, standard dev's and variance.


## QnA 1:

If you are someone who hates risk and wants to keep your money safe, would you prefer an asset with a high or low standard deviation?
A high sd would not make sense since high numbered sd's like three or four are very rare events and you cannot predict them.


## Note:

standard deviations can be any number from 0 to $\inf$, the higher the number the more volatile and rare the events get i.e less predictable


## QnA 2: 

Asset A has a standard deviation of 2. Asset B has a standard deviation of 15. Both have a mean value of 100.
If Asset A is currently 105, it is a very rare, "surprising" event.
If Asset B is currently 105, it is a completely normal, everyday occurrence.
Why does the standard deviation change how we interpret the exact same price (105)? Answer  this your self and if you are confident then you are done here.














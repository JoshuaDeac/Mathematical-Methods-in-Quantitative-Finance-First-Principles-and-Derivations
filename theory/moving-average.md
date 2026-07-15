# Simple Moving Average (SMA)

## Definition
Given a sequence of prices $P_1, P_2, \dots, P_t$:
$$SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$


## Context

"The SMA of an asset price in 3 days is...." this basically translates to $P_1$ = assets price on day 1, $P_2$ = assets price on day 2 and $P_3$ = assets price on day 3

For example: $P_1$ = 3, $P_2$ = 5 and $P_3$ = 6

$$\implies SMA = \frac{ 3+5+6 }{3} \approx 4.67$$


## Recursive Formula for more complex systems ( not really used much so dont worry for the scope of this research)
For computational efficiency:
$$SMA_t = SMA_{t-1} + \frac{P_t - P_{t-n}}{n}$$

## QnA 1:
What do you think is better? A big n or small n? Which would tell you a more accurate of the average of an asset?
If we only had 3 days of prices ( n = 3 ) and also had a different asset with 100 days of prices ( n = 100) which can you be more sure about?

You dont even need probability or stats for this, since if you have more information about something ( n = 100) you can learn more from it and more accurately as a result.
So naturally n = 100 is more accurate since if we took 3 days and they were $P_1$ = -100, $P_2$ = 0 and $P_3$ = 100 then SMA = 0, but the other 2 days are super far apart which can be the case but not always true.

Hence we prefer a large amount of data/ sample size.

## Why?

Who cares right? it just the average of all the prices at each day, that much is simple.
I will let you answer that
Example say the SMA for an asset is 100, n = 100 and the days are usually like 5 above or below this, so days are from the ranges 95-105, and they average to 100.( this is to do with variance and standard deviation which will be covered and explained accordingly )

Then I told you that the assets price on day 101 = 90, your reaction? wow that is way below what it usually is. 
So what do you expect? Based on the SMA you kind of expect it to even out eventually back to 100, so what if you bought it at 90 now and wait until it evens out with say 110 or 105 to be safe? Well you would make profit by doing that.

And thats a reason we use it. It makes for a good "example" or baseline we can follow and compare what we have.

However this is not a strategy, it was used as an example where u might use it.

SMA are used more now in analysis to help current strategies since its considered a very old technique


## QnA 2:

Another question to make you think now. Which $n$ is better? n = 100 or n = 1000, in most cases n = 100 is better but not for math reasons. It is simply due to lag and computer efficiency. The weighted average of adding an extra 5 days onto 100 wont make much of a difference since after 100 days you have a good idea of what the SMA already is so adding more days to the calculation will simply slow you down. ( note most strategies dont even use that many, for example Bollinger Bands use only a 20 day SMA )





# Simple Moving Average (SMA)

## Definition
Given a sequence of prices $P_1, P_2, \dots, P_t$:
$$SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$


## Context

"The SMA of an asset price in 3 days is...." this basically translates to $P_1 = asset price day 1, $P_2 = asset price day 2 and $P_3 = asset price day 3

For example: $P_1 = 3, $P_2 = 5 and $P_3 = 6

\implies SMA = (3+5+6)/3 = 4.67 


## Recursive Formula
For computational efficiency:
$$SMA_t = SMA_{t-1} + \frac{P_t - P_{t-n}}{n}$$


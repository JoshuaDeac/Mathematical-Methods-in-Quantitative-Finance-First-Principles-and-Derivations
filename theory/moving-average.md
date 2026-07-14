# Simple Moving Average (SMA)

The SMA is an arithmetic mean of price data over a window of length $n$.

## Definition
Given a sequence of prices $P_1, P_2, \dots, P_t$:
$$SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$

## Recursive Formula
For computational efficiency:
$$SMA_t = SMA_{t-1} + \frac{P_t - P_{t-n}}{n}$$


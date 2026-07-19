## Pairs Trading

## Prerequisites

[Correlation vs. Cointegration](../theory/Correlation-vs-Cointegration.md)


## What?

Pairs trading is a market neutral strategy( designed to generate returns that are independent of the overall direction of the market ).Here instead of looking at a single assets price we look at 2, of which have a strong relationship. The premise is basically when we see this relationship break in the short term we take advantage of the long term to secure trades which we assume will even out over a long time to produce this relationship.

## The picture

Take two stocks that move together historically say over 10+ years. You create a variable S for your "Spread"(in formula section) which is done by taking the difference between them, and if they are truly related then the graph should look like a line oscillating around a mean instead of random walk drifting into infinity.


## Formulas:

Spread: $$S_t = P_{A,t} - (\beta \times P_{B,t})$$
Where $\beta$ is the hedge ratio = the amount of Asset B needed to balance out movements in Asset A.

## The idea

You are looking for Stationarity. A stationary series doesn't wander off it reverts back to the mean eventually. When we see the prices moving outside of our assumptions we long one asset while shorting the other to reduce risk as well.

## Why?

You don't need to predict if the market goes up or down. You only need to predict that two things that have always moved together will continue to move together( over a long enough period of time). It’s a bet on consistency not on direction.

## Noted Limitations:

* Correlation $\neq$ Cointegration: This is the most common trap. Just because two stocks move in the same direction doesn't mean they will revert to a mean. You need a statistical test (like Engle-Granger) to prove they are cointegrated.
* An asset might change internally which could break the relationship they had.
* You need to be careful on execution risk since you are opening two positions same time. Slipping and fees can make your edge a loss if not significant enough.



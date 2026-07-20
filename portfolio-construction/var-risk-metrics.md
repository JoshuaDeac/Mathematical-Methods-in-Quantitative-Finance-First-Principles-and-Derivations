## Variance and Risk Metrics

Important notes about variance is that it treats "good" volatility and "bad" volatility as the same which we dont really want since we want to consider the "bad" separately since that will be our risk side.
Instead we look at Variance at risk (VaR)


## VaR definition
It is the max expected loss over a given timer period at some confidence interval / level

## VaR calculations

* Parametric (Variance-Covariance) Method: assuming you have ($\Sigma^{-1}$) from [Efficient Frontier / MPT](../portfolio-construction/efficient-frontier.md) you can assume a normal distribution and get VaR that way.
* The other way is through simulation either through historic or Monte Carlo simulations to get your VaR

## Context VaR

If you calculate a 95% 1-day VaR of $10,000, you are saying: "I am 95% certain that my losses will not exceed $10,000 in a single day."


## Expected Shortfall or Conditional VaR (CVaR)

Consider it to answer the question: "if you are unlucky(or lucky depends what you call it) and managed to hit the worst case scenario how bad will it get?" or "if the worst happens what can I do next?"

## Context CVaR

The problem with VaR tells you where the cliff edge is, but it doesn't tell you how far the drop is so conditional VaR comes into play.

If your 95% VaR is $10,000, your CVaR might be $15,000. This means that when you have a "bad" day ( 5% of time ), you can expect your average loss to be $15,000.

## Why?

* In risk management, knowing the average of your worst-case losses is often more useful for capital requirements than just knowing the VaR.
* Encourages better diversification since those losses could outweigh the gains and CVaR makes you consider those massive risks.








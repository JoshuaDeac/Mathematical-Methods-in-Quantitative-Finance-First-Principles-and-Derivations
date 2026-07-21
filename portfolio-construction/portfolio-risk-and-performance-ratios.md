## Sharpe / Sortino Ratio analysis

In quantitative finance these ratios are used to estimate the efficiency of your strategy and it does so by comparing expected returns against risk.

## Sharpe Ratio

It tells you how much excess return you are receiving for the extra volatility you are enduring by holding a riskier asset.

$$\text{Sharpe Ratio} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_p}$$

or if you are looking at it from an efficient frontier perspective:
$$\text{Sharpe Ratio} = \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}}$$

where $R_f$ is the risk free rate ( which is basically like interest rates, and you need to beat it or else you wont make money i.e negative sharp )
please read [Efficient Frontier](../portfolio-construction/efficient-frontier.md) for the rest of the symbol meanings they are important for portfolio optimization.


## Why Sharpe?
* The numerator measures the reward you get above what you could safely make by investing in a risk-free asset. If a portfolio returns 10% and the risk-free rate is 3%, the excess return is 7%.
* The denominator is the [Standard Deviation](../theory/Standard-Dev.md) which is just the root of the variance. Note that the sharpe ratio threats both upside and downside movements( volatility ) equally, so if you make money it reads it the same as if you lost.


## Context
if the sharpe ratio is:
* Negative (< 0): The risk-free asset performed better than the portfolio, or the portfolio had a negative return.

* 1.0 or higher: Generally considered acceptable to good, meaning the portfolio is generating solid returns relative to its risk.

* 2.0 or higher: Considered very good / excellent.

* 3.0 or higher: Rarely sustained over the long period of time and only seen in elite quantitative hedge funds or short-term anomalies.

## Noted sharpe ratio Limitations

* Assumes a normal distribution and we know by now thats not a good thing
*  Penalizes Good Volatility, as previously mentioned when it sees any volatility within the portfolio you get deduced points.  

## Sortino Ratio

The sortino ratio is basically the evolution of the sharpe ratio built and optimized to fix one of the sharpe ratios problems, it only penalizes downside volatility the drops that actually risk losing your money.
So in a way its both a risk metric and a way to tell you how you are doing.

## Sortino Formula

$$\text{Sortino Ratio} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_d}$$

where everything is the same except:
$\sigma_d$: Target downside deviation (or downside risk)

which is calculated like:
$$\sigma_d = \sqrt{\frac{1}{N} \sum_{R_t < \text{target}} (R_t - \text{target})^2}$$

To calculate $\sigma_d$, you look only at the returns that fall below a specific threshold (usually either the risk-free rate or $0\%$). Any return that lands above that is treated zero variance.

## Why sortino over sharpe?
One of the best ways to make money in the stock market is to reduce your risk or how much money you lose, and the sortino tells you much more in this sense than the sharpe.
However, you should always look at both ratios since any information is better than none. If you have the option consider sharpe but dont rely on it or anything else independently.


Note: sortino is subject to the same limitations a sharpe besides the second one
 

## Max Drawdown (max DD) and calmer ratio

It is similar to Sharpe and Sortino, but it replaces standard deviation or downside deviation in the denominator with Maximum Drawdown

$$\text{Calmar Ratio} = \frac{\text{Compound Annual Growth Rate (CAGR)}}{\text{Maximum Drawdown}}$$

Max DD is basically the biggest hit your portfolio has taken over a time period.
These are normally used by the boys in the big leagues to convince investors to invest, however sometimes if they made a mistake that cost them ay 50% of their portfolio, that look up window within that mistake will absolutely kill the calmer ratio but you can fix it by being consistent for a year and arguing the mistake. So calmer ratio rewards those who can stay afloat.







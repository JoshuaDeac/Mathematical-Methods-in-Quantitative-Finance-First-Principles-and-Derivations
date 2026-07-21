## Sharpe / Sortino Ratio Analysis

In quantitative finance, these ratios are used to estimate the efficiency of a strategy by comparing expected returns against risk.

## Sharpe Ratio

The Sharpe ratio tells you how much excess return you are receiving for the extra volatility you are enduring by holding a riskier asset.

$$\text{Sharpe Ratio} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_p}$$

Or, if you are looking at it from an efficient frontier perspective:
$$\text{Sharpe Ratio} = \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}}$$

Where $R_f$ is the risk-free rate (akin to prevailing interest rates; you need to outperform it, or your real return is negative). 
*Please refer to [Efficient Frontier](../portfolio-construction/efficient-frontier.md) for the rest of the symbol meanings; they are vital for portfolio optimization.*

## Why Sharpe?
* **The Numerator:** Measures the reward you get above what you could safely make by investing in a risk-free asset. If a portfolio returns 10% and the risk-free rate is 3%, the excess return is 7%.
* **The Denominator:** The [Standard Deviation](../theory/Standard-Dev.md), which is the square root of variance. Note that the Sharpe ratio treats both upside and downside volatility equally—making money on a massive upside spike is penalized mathematically the exact same way as losing money.

## Context 
* **Negative (< 0):** The risk-free asset outperformed the portfolio, or the portfolio had a negative return.
* **1.0 or Higher:** Generally considered acceptable to good, meaning the portfolio is generating solid returns relative to its risk.
* **2.0 or Higher:** Considered very good / excellent.
* **3.0 or Higher:** Rarely sustained over long periods; typically only seen in elite quantitative hedge funds or short-term anomalies.

## Noted Sharpe Ratio Limitations
* **Assumes Normal Distribution:** Real-world financial returns exhibit fat tails and skewness, which standard deviation fails to capture.
* **Penalizes Good Volatility:** Punishes upside price spikes just as harshly as downside drops.

## Sortino Ratio

The Sortino ratio is the evolutionary step of the Sharpe ratio, built and optimized to fix its primary flaw: it penalizes *only* downside volatility—the drops that actually risk losing your capital.

## Sortino Formula

$$\text{Sortino Ratio} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_d}$$

Where everything matches the Sharpe ratio except:
* $\sigma_d$: Target downside deviation (or downside risk).

Calculated as:
$$\sigma_d = \sqrt{\frac{1}{N} \sum_{R_t < \text{target}} (R_t - \text{target})^2}$$

To calculate $\sigma_d$, you look only at returns falling below a specific threshold (usually the risk-free rate or $0\%$). Any return landing above that threshold is treated as zero variance.

## Why Sortino Over Sharpe?
One of the best ways to protect capital is to measure actual downside risk, and the Sortino ratio communicates this far better than the Sharpe ratio. However, you should always look at both ratios; multiple lenses provide better context than relying on any single metric independently.

*Note: The Sortino ratio is subject to the same general limitations as the Sharpe ratio, except for the penalty on upside volatility.*

## Max Drawdown (Max DD) and Calmar Ratio

The Calmar ratio shifts from standard or downside deviation in the denominator to Maximum Drawdown:

$$\text{Calmar Ratio} = \frac{\text{Compound Annual Growth Rate (CAGR)}}{\text{Maximum Drawdown}}$$

Max DD measures the biggest peak-to-trough hit your portfolio has taken over a given time period. 

Institutions use this to evaluate historical resilience. However, a single catastrophic historical mistake (e.g., a massive 50% drawdown years ago) can permanently scar a long-term Calmar ratio. Managers can combat this by showing consistent execution over recent windows and proving structural risk controls have since been fixed. Ultimately, the Calmar ratio rewards consistency and survival.

## Information Ratio (IR)

If a strategy yields 5% to 8% annually, institutional investors may pass because broad indices like the S&P 500 historically return 9% to 11% with decades of proven track record. 

To attract institutional capital, the Information Ratio replaces the risk-free rate with a benchmark baseline (like the S&P 500) to measure active skill:

$$\text{Information Ratio} = \frac{\mathbb{E}[R_p] - \mathbb{E}[R_b]}{\sigma_{\text{active}}}$$

* $\mathbb{E}[R_b]$: Expected benchmark return
* $\sigma_{\text{active}}$: Tracking error ($\sigma_{active} = \sqrt{\frac{1}{N-1} \sum_{t=1}^{N} (R_{p,t} - R_{b,t} - \overline{R_{\text{active}}})^2}$)

Tracking error measures how violently or unpredictably your portfolio deviates from its benchmark index. *(Note: Sample variance uses $N-1$ degrees of freedom, while population variance uses $N$.)*

* $\overline{R_{\text{active}}}$: Mean of active returns.
* $R_{p,t}$ and $R_{b,t}$: Portfolio and benchmark returns over time $t$.

### The Institutional Reality
Active risk means you are intentionally disagreeing with the benchmark. If you beat the index by 15% one month and trail it by 10% the next, your tracking error spikes. Institutional allocators (like pension funds) use this to enforce strict risk parameters, often giving managers explicit **tracking error budgets** (e.g., *"Beat the S&P 500, but your tracking error cannot exceed 3%"*). This forces outperformance without reckless gambling.

*Note: Subject to similar distribution limitations as the Sharpe ratio.*

## Annualized Scaling

Multiplying daily ratios straight by 252 (the number of yearly trading days) to annualize them is mathematically incorrect. 
* **Returns** scale linearly with time ($252 \times \text{Daily Return}$).
* **Volatility** scales by the square root of time ($\sqrt{252} \times \text{Daily Volatility}$).

**Limitation of Scaling:** The "square root of time" rule is an approximation, not a universal law. It relies on the assumption of iid returns.

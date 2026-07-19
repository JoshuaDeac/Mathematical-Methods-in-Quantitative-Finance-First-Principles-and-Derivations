## Correlation vs. Co-integration


## Why?

These are very closely correlated meanings ( no pun intended ) and people usually dont know about cointegration which makes them mistake it for correlation. Hence a "vs" file will be made to help.

## Correlation

Correlation is just the common way to describe the Pearson correlation coefficient which has values from r $\in$ (-1,1)




## Correlation formula

$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$


## Co-integration

Co-integration is a statistical property of a collection of time series variables. It is the condition where a linear combination of non-stationary series results in a stationary series. 

* **The Link:** It implies a long-term equilibrium relationship. 
* **The Key:** Unlike correlation, which looks for movement direction, co-integration looks for a stable "tether" that pulls the spread back to a mean over time.

## Why the "vs"?

Correlation measures the **direction** of movement (shorter periods/ locally), while co-integration identifies a **equilibrium** (long-term). A strategy built on correlation alone is exposed to "drift" risk while co-integration provides the statistical justification for mean-reversion.

## Testing?

To prove two assets are co-integrated, we typically use the **Engle-Granger** two-step method or the **Augmented Dickey-Fuller (ADF)** test on the residuals of a linear regression.



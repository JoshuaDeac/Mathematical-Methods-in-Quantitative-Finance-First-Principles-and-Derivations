## Liquidity Risks

Adding to the current definition of what liquidity is, liquidity risk is someones inability to fulfill their orders before a big change in price happens which put them at "risk" or at a disadvantage.

## Two main types of risk involved:

They are connected closely and as such feed each other when the market is under pressure.
* Markets Liquidity: how easy one can buy or sell at fair price without major moves in price
* Funding Liquidity: how easy it is to find funding via cash, credits ect..to finance the position or meet expectations.

**The big red button:** When investors run out of funding( e.g lenders ask for extra cash for collateral ) then they are forced to sell at whatever position they are currently at. To liquidate quickly they just dump it all into the market which as we know just destroys the markets liquidity and in turn triggers a massive price movement.

## How liquidity risks come about and the friction involved:

* In order books when an order size is very large it instantly starts removing tiers from the buyers or sellers.
* **Slippage:** is the extra money you have to pay as a result of buying through the order book too fast and not enough "best" bidders to give you the fair value price. So when executing big orders( relatively ) slippage is basically guaranteed.
* **Crossing the gap** We spoke about order books and how volume effects it. Liquidity follows closely behind, the spread is the instantaneous price you must pay by crossing the gap, and in normal conditions it will be like jumping over a crack on a side walk, however when liquidity breaks jumping over this is like a canon and you must be careful because if you dont jump you could get stuck on one side for a long time. 
* **The near endless spiral:** Margin calls happen -> traders have to sell -> lower liquidity -> price depression -> worsens liquidity -> forces higher volatility -> investors or brokers are unsure and? -> margin calls happen.


## Some methods to numerate that liquidity:

## The Amihud Illiquidity Measure (ILLIQ)

The Amihud Illiquidity Ratio:

$$\text{ILLIQ}_t = \frac{1}{D_t} \sum_{d=1}^{D_t} \frac{\vert{}R_{d,t}\vert{}}{\text{Volume}_{d,t}}$$
* $R_{d,t}$: Return of the asset on day $d$ of month $t$ (expressed as a percentage or absolute decimal).
* $\text{Volume}_{d,t}$: Dollar trading volume (or share volume multiplied by price) on day $d$ of month $t$.
* $D_t$: Total number of trading days in month $t$.



## The Roll Measure

$$\text{Roll}_t = 2 \sqrt{-\max(0, \text{Cov}(\Delta P_t, \Delta P_{t-1}))}$$
$\Delta P_t$: Price change of the asset on day $t$ (i.e., $P_t - P_{t-1}$).
$\text{Cov}(\Delta P_t, \Delta P_{t-1})$: First order autocovariance of price changes over the estimation window.






## Not Finished







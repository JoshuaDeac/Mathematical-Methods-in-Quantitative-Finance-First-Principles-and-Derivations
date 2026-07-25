## Volume

Volume is just another number, another piece of information about trading, yet not enough people talk about it. Conceptually, it's easy: while price tells you *what* happened, volume tells you *how much money* was behind the price move.

Price, by itself, is like an incomplete sentence; you cannot look at it alone and accurately predict the rest. However, volume gives us critical context to that sentence. Free data, I would call it. 

## Why?

Big hedge funds and institutions can artificially drive prices up or down on a given day. Price alone only shows direction, not the force behind it. Volume, however, is much harder to fake; it tracks the number of actual transactions, revealing where real capital is sitting in the market.

## Three Main Pillars of Volume

* **Healthy Moves:** Large price movements (up or down) along with high volume usually indicate that the effort involved (volume) matches the result (large price movement).
* **Absorption and Manipulation:** When there is high volume but small price movement, it means large institutional players are quietly stepping in to absorb buy or sell orders. Because price can be artificially manipulated by large capital, volume serves as a reality check to see if actual market participants are supporting the move.
* **Exhaustion and Divergence:** When price hits new highs or lows on continuously shrinking volume, it signals that the market is losing its backing (like a rocket running out of fuel), pointing toward a reversal.

## Auction Market Theory

Instead of just looking at volume as a running total over time, we can look at it through continuous market dynamics:

### Fair Value and Sticky Prices

**Fair Value:**
* Typically, the market disagrees on an asset's price, but sometimes it converges on a "fair value." As a result, there is a very high number of transactions since a lot of people agree on that value. This creates what order flow traders call a **High Volume Node (HVN)** or a "volume profile peak."

**Sticky Prices:**
After this HVN forms at price $x$, it acts almost like a magnet or anchor for several reasons:
* Large institutional players cannot buy or sell everything they want all at once without moving the price against themselves. They wait for these HVNs to execute because it’s the only place where there are enough matching counterparties to absorb massive orders without causing severe slippage.
* Game theory dynamics: When people buy at fair value and the price drops, they are instantly losing money. When it comes back up, they want to exit at breakeven. Similarly, if the price goes above, sellers at fair value wait while buyers cash out for profits. This creates a tug-of-war with volume clustering around the fair value node.

### Unfair Value and Price Rips

**Unfair Value:**
* In an unfair value area, one side (buyers or sellers) realizes they are on the wrong side of a trade, often triggered by a catalyst like news or new data.
* Opinions shift instantly, and one side completely dominates or withdraws. Buyers refuse to bid higher, or sellers pull their limit orders to re-evaluate.

**Price Rips:**
* An order book relies on resting limit orders to act as cushions or speed bumps for the price.
* When unfair value hits, participants retract their limit orders, removing those structural speed bumps. The asset price "rips" through that section. When few orders are placed, volume dries up.
* We call these **Low Volume Nodes (LVNs)**: the order book is thin, there is no structural resistance, and the price can accelerate rapidly.

## Key Volume Metrics

### Volume Weighted Average Price (VWAP)
VWAP is the true benchmark average price an asset has traded at throughout a given time period. It acts as a primary institutional execution benchmark. Large funds try to execute buy orders below VWAP and sell orders above VWAP to minimize market impact.

* **Buying Below VWAP:** If a fund needs to accumulate a massive block of shares, buying below the day's VWAP means they acquired the asset at a below-average cost compared to the broader market, proving they accumulated during patient absorption phases rather than chasing green candles.
* **Selling Above VWAP:** Conversely, when liquidating a large position, selling above VWAP means they achieved an above-average execution price, maximizing revenue before heavy selling pressures alter the trend.

### On-Balance Volume (OBV)
OBV is a cumulative momentum indicator that uses volume flow to predict changes in stock price. It adds total volume on up-days and subtracts total volume on down-days. OBV acts as a pressure gauge: if an asset's price is moving sideways or consolidating, but its OBV is steadily ticking upward, it signals accumulation—institutions are quietly building a massive position before a potential breakout (much like kinetic energy building up).

## Formulas

$$VWAP = \frac{\sum (\text{Typical Price} \times \text{Volume})}{\sum \text{Volume}}$$

* **Typical Price:** $\frac{\text{High} + \text{Low} + \text{Close}}{3}$
* **Numerator ($\sum$ Price $\times$ Volume):** The summed total dollar amount traded over the timeframe.
* **Denominator ($\sum$ Volume):** The total volume traded in that timeframe.

**On-Balance Volume (OBV):**
* If $$\text{Close}_{\text{current}} > \text{Close}_{\text{previous}}$$: $\text{OBV} = \text{OBV}_{\text{previous}} + \text{Volume}_{\text{current}}$
* If $\text{Close}_{\text{current}} < \text{Close}_{\text{previous}}$: $\text{OBV} = \text{OBV}_{\text{previous}} - \text{Volume}_{\text{current}}$
* If $\text{Close}_{\text{current}} = \text{Close}_{\text{previous}}$: $\text{OBV} = \text{OBV}_{\text{previous}}$

*Note: While an HVN is a broader zone where heavy trading occurs, the **Point of Control (POC)** is the exact, single price level within that zone where the absolute highest volume was traded, often called the ultimate "Fair Value."*

## Noted Limitations
* **Lag:** Volume is fundamentally reactive data; it records transactions *after* they have occurred. Tools like OBV and volume divergence attempt to use this reactive data as a leading pressure gauge, but volume remains an estimate of market battles rather than a crystal ball.
* **Context Dependency:** HVNs and POCs show where price *could* react, but they do not guarantee that a level will hold. Market context, broader liquidity, and incoming catalysts matter.
* **Dark Pools & Off-Exchange Trading:** A massive percentage of institutional volume is executed in dark pools or internalizer networks that do not print immediately to lit order books, meaning public volume indicators can present an incomplete picture.
* **Timeframe Sensitivity:** Using the wrong timeframe window (e.g., mixing daily profiles with multi-year profiles) can heavily skew your VWAP, POC, and volume profile readings.
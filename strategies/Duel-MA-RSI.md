## Duel Moving Average crossover with RSI Filter

## Prerequisites

* [RSI](../theory/RSI.md)
* [SMA / MA](../theory/moving-average.md)

Note on EMA( exponential moving average ): its simply gives you the SMA but a weighted version which priorities most recent price i.e giving heavier weight to yesterdays price than to the price two weeks ago.


## Set up
* Fast MA: 50 period EMA 
* Slow MA: 200 period EMA
* Momentum Filter: 14 period RSI.

## Conditions for trades: 

* **Long when :** The 50 EMA crosses above the 200 EMA, AND the RSI is between 40 and 65
* **Short when :** The 50 EMA crosses below the 200 EMA, AND the RSI is between 35 and 60.
* **Risk Management :** Stop Loss: Placed just below the most recent swing low (for longs) or swing high (for shorts), or set at a fixed risk threshold (e.g., $2\%$ of account equity).
* **Take Profit:** Trailed dynamically using the 20 EMA, or set at a fixed risk to reward ratio e.g $1:2$ .










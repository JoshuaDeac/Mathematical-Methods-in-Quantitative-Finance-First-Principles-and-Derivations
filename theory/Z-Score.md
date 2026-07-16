## Z-Scores

## Definition

Z-score are very closely related to [Standard Deviations](../theory/Standard-Dev.md) we are simply putting a formal name to that distance.


$$Z = \frac{P - \mu}{\sigma}$$

* $$P$$: The current price.
* $\mu$: The mean (average) price.
* $\sigma$: The standard deviation

## Why?

In quant finance, the Z-Score is the "Great Equalizer" It allows you to take two completely different assets say, Bitcoin (which is very volatile) and a stable Treasury Bond and allows you to compare their price moves on the exact same scale.

For example you might think there is no difference between sd and z-score which is understandable but the key difference is that when we calculate a z-score we assume a normal distribution of data and as such we can give each of our z-scores probabilities.

On top of this a Z-score is standardized, but what is it standardizing? Well everything you can turn dollars into a z-score, you can turn kilometers into a z-score, basically turn anything that you assume has normal distribution into a relevant probability.

Thats why its so powerful in allowing you to calculate very different assets side by side.


## More differences between Z-scores and sd


\begin{array}{|l|l|l|}
\hline
\textbf{Feature} & \textbf{Standard Deviation (\sigma)} & \textbf{Z-Score (Z)} \\ \hline
\textbf{Perspective} & \text{Dataset-wide: The "personality"} & \text{Point-in-time: The "status"} \\ \hline
\textbf{Units} & \text{Price Units (\$)} & \text{Unitless (Ratio of SDs)} \\ \hline
\textbf{Goal} & \text{Summarize total spread} & \text{Summarize extremity} \\ \hline
\textbf{Example} & \text{"SD is \$5"} & \text{"Z-score is 2"} \\ \hline
\end{array}






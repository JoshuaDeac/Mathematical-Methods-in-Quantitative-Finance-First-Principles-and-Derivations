## Principal Component Analysis

its a statistical method for taking a big data set with many connected variables and simplifying it down to some key patterns while preserving most of the things you actually want without throwing away important information.

Or simply: PCA is the mathematical process of finding the absolute best angles to view your data from.

## How and why?

Why is this important? Well for a few reasons, when looking at algorithmic trading big companies want the big O time complexity to be low and the higher the dimensions of the data the higher that big O complexity will be( also very useful to data analysts ). So being able to knock down the dimensions saves time and effort while keeping most information.

How it does this is by looking at variance, if a variable in a stock is stationary and does not move much ( say for example volume  ) variance then by PCA it does not carry much information and as a result wont contribute much.PCA assumes that variance = information. The direction where the data spreads out the most is the most important direction.










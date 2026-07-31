## Principal Component Analysis

Its a statistical method for taking a big data set with many connected variables and simplifying it down to some key patterns while preserving most of the things you actually want without throwing away important information.

Or simply: PCA is the mathematical process of finding the absolute best angles to view your data from.

Done by getting the correlation matrix for each variable( standardized via z-score, i.e take away mean and divide by sd ) then getting the eigenvalues of said matrix, those will be your list of PC'S

## How and why?

Why is this important? Well for a few reasons, when looking at algorithmic trading big companies want the big O time complexity to be low and the higher the dimensions of the data the higher that big O complexity will be( also very useful to data analysts ). So being able to knock down the dimensions saves time and effort while keeping most information.

How it does this is by looking at variance, if a variable in a stock is stationary and does not move much ( say for example volume  ) variance then by PCA it does not carry much information and as a result wont contribute much.PCA assumes that variance = information. The direction where the data spreads out the most is the most important direction.



## Interpretation of output:

It looks like a 1D list of numbers, one for each principal component, sorted from largest to smallest. Which are just the eigenvalues of the matrix.

Example:
*  $$\text{Eigenvalues } (\boldsymbol{\lambda}) = [3.8, \ 0.7, \ 0.3, \ 0.1, \ 0.1]$$

Sum of eigenvalues = $3.8 + 0.7 + 0.3 + 0.1 + 0.1 = 5.0$ (equal to the number of stocks).
* PC1 captures $3.8 / 5.0 = \mathbf{76\%}$ of all stock movements.
* PC2 captures $0.7 / 5.0 = \mathbf{14\%}$ of all stock movements.
* Together, PC1 + PC2 explain 90% of the entire market's motion, so you can ignore the rest.












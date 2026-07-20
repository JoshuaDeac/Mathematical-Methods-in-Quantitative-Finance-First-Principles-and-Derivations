## The math foundation

To manage a portfolio of $N$ asset:

* Define a weight vector ($w$): An $N \times 1$ column vector where $\sum w_i = 1$
* Define Expected return vector ($\mu$): An $N \times 1$ column vector of expected returns for each asset.
* Defone a Covariance Matrix ($\Sigma$): An $N \times N$ symmetric, positive semi-definite matrix( just a type of matrix which follows reality and doesnt allow for certain negatives that wouldnt make sense in real life ) where $\Sigma_{ij} = \text{Cov}(R_i, R_j)$.



## Portfolio Expected Return

The return of the portfolio is the weighted sum of each assets returns:$$E[R_p] = w^T \mu$$



## Portfolio Variance
The variance of a portfolio ($\sigma_p^2$) is our primary mathematical measure of total portfolio risk. 
$$\sigma_p^2 = w^T \Sigma w$$

In other words, the total risk of my portfolio is each assets weighted risk added by how they each interact with each others risk(covariance) all summed up via their weights

## Heavy Math for optimization

To find optimal weights for our portfolio, we use Lagrange Multipliers to minimize the variance subject to two constraints:

* Target Return: $w^T \mu = \mu_p$
* Fully Invested: $w^T \mathbf{1} = 1$, where "1" is the vector with 1's

The Lagrangian function ($L$) is:
$$L(w, \lambda_1, \lambda_2) = \frac{1}{2} w^T \Sigma w - \lambda_1(w^T \mu - \mu_p) - \lambda_2(w^T \mathbf{1} - 1)$$

To solve for the optimal weights $w^*$, we take the partial derivative with respect to $w$ and set it to zero:
$$\frac{\partial L}{\partial w} = \Sigma w - \lambda_1 \mu - \lambda_2 \mathbf{1} = 0 \implies w^* = \Sigma^{-1} (\lambda_1 \mu + \lambda_2 \mathbf{1})$$


source for the math: https://docs.mosek.com/portfolio-cookbook/markowitz.html#the-mean-variance-model, "Through the method of Lagrangian multipliers" ctrl + F 












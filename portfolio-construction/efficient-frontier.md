## The math foundation

To manage a portfolio of $N$ asset:

* Define a weight vector ($w$): An $N \times 1$ column vector where $\sum w_i = 1$
* Define Expected return vector ($\mu$): An $N \times 1$ column vector of expected returns for each asset.
* Define a Covariance Matrix ($\Sigma$): An $N \times N$ symmetric, positive semi-definite matrix( just a type of matrix which follows reality and doesnt allow for certain negatives that wouldnt make sense in real life ) where $\Sigma_{ij} = \text{Cov}(R_i, R_j)$.



## Portfolio Expected Return

The return of the portfolio is the weighted sum of each assets returns:$$E[R_p] = w^T \mu$$



## Portfolio Variance
The variance of a portfolio ($\sigma_p^2$) is our primary mathematical measure of total portfolio risk. 
$$\sigma_p^2 = w^T \Sigma w$$

In other words, the total risk of my portfolio is each assets weighted risk added by how they each interact with each others risk(covariance) all summed up via their weights

## Heavy Math for optimization

To find optimal weights for our portfolio, we use Lagrange Multipliers to minimize the variance subject to two constraints:

* Target Return: $w^T \mu = \mu_p$
* Fully Invested: $w^T \mathbf{1} = 1$, where $\mathbf{1}$ is the $N \times 1$ vector of ones.

The Lagrangian function ($L$) is:
$$L(w, \lambda_1, \lambda_2) = \frac{1}{2} w^T \Sigma w - \lambda_1(w^T \mu - \mu_p) - \lambda_2(w^T \mathbf{1} - 1)$$

To solve for the optimal weights $w^*$, we take the partial derivative with respect to $w$ and set it to zero:
$$\frac{\partial L}{\partial w} = \Sigma w - \lambda_1 \mu - \lambda_2 \mathbf{1} = 0 \implies w^* = \Sigma^{-1} (\lambda_1 \mu + \lambda_2 \mathbf{1})$$
note: The Matrix Inverse = ($\Sigma^{-1}$)

source for the math: https://docs.mosek.com/portfolio-cookbook/markowitz.html#the-mean-variance-model, "Through the method of Lagrangian multipliers" ctrl + F 

To further find $\lambda_1$ and $\lambda_2$ they act like volume buttons, we keep turning both of them or tweaking their values to find when they fit our constraints from above.

To find the exact values for these knobs, we take our formula for $w^*$ and plug it back into our two constraints:
* $w^T \mu = \mu_p \implies (\Sigma^{-1}(\lambda_1 \mu + \lambda_2 \mathbf{1}))^T \mu = \mu_p$
* $w^T \mathbf{1} = 1 \implies (\Sigma^{-1}(\lambda_1 \mu + \lambda_2 \mathbf{1}))^T \mathbf{1} = 1$

and now we have simultaneous equation problem, which is simple to solve.

Once you solve for the lambdas using basic algebra, you plug them back into the original weight formula. This gives you the final, exact percentages (the weights) for every asset in your portfolio.


## Noted Limitations to optimized math

In the real world we dont know $\mu$ or $\Sigma$ exactly we simply used estimates for these then optimize for those estimates.

Additionally you might notice there is a $\frac{1}{2}$ before our variance in The Lagrangian function, this is because when we take the derivative of the variance ($w^T \Sigma w$), the result is $2 \Sigma w$. The $\frac{1}{2}$ cancels out that $2$, leaving us with a cleaner equation. It doesn't change the outcome, just makes the algebra much simpler.








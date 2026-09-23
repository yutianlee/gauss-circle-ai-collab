# Conductor Round 164 residual transport seed

## Candidate algebra

For fixed \(N\), let \(\mathscr R_N\) contain every odd divisor retained
by the residual indicator, including divisors on which the literal
amplitude is zero.  Order

\[
 d_1<d_2<\cdots<d_r,\qquad
 \sigma_i=\chi_4(d_i),\qquad
 C_j=\sum_{i\leq j}\sigma_i.
\]

Writing \(A_i=A_N(d_i)\), discrete summation by parts gives the exact
identity

\[
 \sum_{i=1}^r\sigma_iA_i
 =C_rA_r+\sum_{j=1}^{r-1}C_j(A_j-A_{j+1}).
\tag{164.S1}
\]

If the full residual divisor universe includes its largest odd divisor,
then \(A_r=0\) on the \(N\asymp L^2\) block.  This must be verified for
odd and even \(N\), including endpoint conventions, before deleting the
terminal term.

On a common smooth interval in \(u=\log d\), the cumulative step function

\[
 F_N(u)=\sum_{\substack{d\in\mathscr R_N\\\log d\leq u}}\chi_4(d)
\tag{164.S2}
\]

gives the formal bound

\[
 |b_{L,X}^{\rm rem}(N)|
 \leq
 \int |F_N(u)|\,|dA_N(e^u)|
 +\text{all literal jump and unmatched terms}.
\tag{164.S3}
\]

When the two sign masses agree, the integral of \(|F_N|\) is the
one-dimensional monotone \(W_1\) transport cost between the two unit
atomic measures.  When they do not agree, an unmatched or cemetery term
is mandatory.

## Candidate route test

Round-163 semiprime and four-prime controls already suggest that the
coefficient-uniform aggregate of the right side of (164.S3) can have
\(L^{2-o(1)}\) capacity.  If this survives literal residual bookkeeping,
then within-\(N\) positive transport cannot reach \(L^{3/2}\).  The
remaining problem is not another matching: it is cancellation in

\[
 \sum_{N\asymp L^2}
 \mu^2(N)c_N^{\rm rem}e(J\sqrt N)
\tag{164.S4}
\]

for the actual signed residual coefficients \(c_N^{\rm rem}\).

The discovery task should not stop at the capacity statement.  It should
derive the strongest exact coefficient norm, bilinear decomposition, or
partial-summation condition on \(c_N^{\rm rem}\) that would turn the
outer square-root phase into the missing half-power, and test it against
the accepted rank-one product-collar obstruction.

## First doubtful step

Equation (164.S1) is exact.  The first doubtful step is any assertion that
the total variation functional in (164.S3) is
\(O(L^{3/2}X^\varepsilon)\).  Unequal sign counts and singleton
semiprime fibres can retain unit cost on \(L^{2-o(1)}\) products.  That is
only a positive-route obstruction, not a lower bound for (164.S4), where
the outer phase remains signed.

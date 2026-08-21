# Conductor review: exact one-third block optimization

## Verdict

The direct M1 and M2 block menu proves the uniform exponent \(1/3\), and
\(1/3\) is optimal for that menu.

For every actual dyadic block, put \(R=D/L\). The two accepted bounds are

\[
 \mathcal B_i\ll_\varepsilon X^\varepsilon(1+R)
\]

and

\[
 \mathcal B_i\ll_\varepsilon X^\varepsilon
 \left\{(X/R)^{1/2}+D(R/X)^{1/2}+1\right\}.
\]

If \(R\leq X^{1/3}\), the first bound is
\(O_\varepsilon(X^{1/3+\varepsilon})\). If \(R>X^{1/3}\), the first
term of the second bound is at most \(X^{1/3}\), and

\[
 D(R/X)^{1/2}\leq X^{1/2}(X^{1/2}/X)^{1/2}=X^{1/4}
\]

because \(1\leq L\), \(R\leq D\leq X^{1/2}\).

The estimate is literal, not an inner-sum bound: fixed-frequency van der
Corput followed by the actual \(1/h\) Vaaler coefficient gives precisely
the displayed two-term block estimate. M1 is split into its two odd
denominator residue classes, and M2 retains its two quarter shifts and
frequency character. The hard top sampled sequence has one bounded BV
jump and is included.

At \((\delta,\ell)=(1/2,1/6)\), T2S and the first
second-derivative term both equal \(1/3\); the other
second-derivative exponent is \(1/6\), the trivial exponent is \(1/2\),
and the TTY main exponent is

\[
 {770\over1923}>{1\over3}.
\]

Thus no strict improvement below \(1/3\) follows from the accepted menu.
This is route optimality, not a lower bound for the actual sums.

Evidence:

- blind_global_exponent_rederivation.md;
- global_exponent_hostile_audit.md;
- conductor_one_third_assembly.md;
- the accepted M1 and M2 phase-diagram reports and syntheses.

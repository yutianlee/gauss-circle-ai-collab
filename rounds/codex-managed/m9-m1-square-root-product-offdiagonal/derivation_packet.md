# Round 68 packet: signed square-root-product off-diagonal

## Accepted antecedent

Round 67 proves, in a fixed smooth interior sector, that the missing
reciprocal large-sieve estimate is equivalent up to controlled errors to

\[
 \sum_{k\asymp Q}|P_k|^2\ll Q^2X^\varepsilon,
 \qquad
 P_k=\sum_{\rho\in\{1,3\}}\epsilon_\rho
 \sum_{r\asymp k}c_\rho(k,r)
 e\!\left(2\sqrt{kX(r-\rho/4)}\right).
\tag{68.1}
\]

Here \(J=X^{1/2}\), \(Q=J/T=X^{\nu/2}\), with the benchmark
\(\nu=2/5\), and the actual pulled-back symbols are smooth in the
fixed-interior sector with the inherited residue, profile, and cutoff
ownership. The diagonal of (68.1) is \(\asymp Q^2\).

## Frozen target

Prove, or sharply falsify/obstruct,

\[
 \mathcal O=
 \sum_{k\asymp Q}
 \sum_{(\rho_1,r_1)\ne(\rho_2,r_2)}
 \epsilon_{\rho_1}\overline{\epsilon_{\rho_2}}
 c_{\rho_1}(k,r_1)\overline{c_{\rho_2}(k,r_2)}
 e\!\left(2\sqrt{Xk}
 [\sqrt{r_1-\rho_1/4}-\sqrt{r_2-\rho_2/4}]
 \right)
 \ll Q^2X^\varepsilon.
\tag{68.2}
\]

Set \(u_i=r_i-\rho_i/4\) and

\[
 \Delta=u_1-u_2
 =(r_1-r_2)-{\rho_1-\rho_2\over4}.
\tag{68.3}
\]

On the off-diagonal \(\Delta\in\tfrac12\mathbb Z\setminus\{0\}\),
and

\[
 \sqrt{u_1}-\sqrt{u_2}
 ={\Delta\over\sqrt{u_1}+\sqrt{u_2}}.
\tag{68.4}
\]

The proof must retain the two residue classes, the actual moving symbol,
all short-range edges, and the fixed-interior restriction. A theorem for
arbitrary coefficients is not expected, but any use of the actual
coefficient must be explicit.

## Controls

1. Recheck the diagonal and the cross-residue minimum
   \(|\Delta|=1/2\).
2. Derive the exact \(k\)-difference phase and every Poisson/B-process
   stationary alias before estimating it.
3. Test squares, fourth powers, product-square fibers, and the
   near-diagonal \(|\Delta|=1/2,1\) shells.
4. Distinguish an unsigned spacing count from the signed energy.
5. Audit whether a proposed double-large-sieve, Robert--Sargos,
   Bombieri--Iwaniec/Huxley, Jutila, spectral, or Hankel theorem has the
   actual hypotheses and target normalization.
6. Do not infer the full cone, a radial interval, M9-M1, M9, or an
   exponent from a smooth fixed-interior estimate alone.

## Required output

Every report has exactly seven semantic sections: result; exact statement
and hypotheses; proof/derivation; first doubtful step; controls; exact
dependencies; recommended state effect. Numerical work is optional and
diagnostic only; the campaign is primarily analytical.


# Round 84 derivation packet: centred dual-difference stationary correlation

Starting graph SHA-256:
`b744aa885442ec9be13913782471cf65a94cd794579f8c6a8fbb2854ce52e271`

## 1. Accepted starting point

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and freeze

\[
 J^{13/18}<C\le J^{3/4}.                                  \tag{84.1}
\]

Fix one transition-flattened smooth-interior nonaxial M1 component,
alias, endpoint orientation, and compatible dual pair. Choose the
oriented coordinate so that \(k=\rho\sigma>0\); the reflected component
is conjugate. For

\[
 \kappa\in\{1/4,1/2,1\},\qquad
 g_\kappa=4\kappa,\qquad
 M_\kappa={4b\over g_\kappa},\qquad c=g_\kappa x,
\]

the accepted exact local unit is

\[
 u_{\kappa,b,k}(g_\kappa x)
 =\zeta_{\kappa,b,k}e_{M_\kappa}(K_{\kappa,b,k}\bar x),
 \qquad |\zeta_{\kappa,b,k}|=1,                           \tag{84.2}
\]

with

\[
 \begin{array}{c|c|c|c}
 \kappa&g_\kappa&M_\kappa&K_{\kappa,b,k}\\ \hline
 1/4&1&4b&k\\
 1/2&2&2b&2[k\bar4]_b\\
 1&4&b&[k\bar4]_b.
 \end{array}                                               \tag{84.3}
\]

In all classes \((K,M)=O_k(1)\). The actual reciprocal phase is

\[
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2
 =bX+2\sqrt{\kappa kX}+{\kappa k\over b}.                 \tag{84.4}
\]

The exact smooth principal symbol has the accepted global bound

\[
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V
 \ll_\varepsilon X^\varepsilon.                          \tag{84.5}
\]

Do not assume additional uniform derivative seminorms without deriving
them from the exact smooth-interior antecedent.

## 2. Exact Fourier and centred-energy formula

For one orientation put

\[
 F_b(x)=V_{b,gx,k}^{(\kappa)}
 e\!\left(-{A_{\kappa,b}\over gx}\right),
 \qquad
 I_b(n)=\int_{\mathbb R}F_b(x)e\!\left(-{nx\over M}\right)dx.
                                                               \tag{84.6}
\]

The opposite orientation is obtained by conjugating and reversing the
stationary sign of \(n\). Exact progression Poisson gives

\[
 \sum_{x\bmod M}^{*}e_M(K\bar x)
 \sum_{\ell\in\mathbb Z}F_b(x+M\ell)
 ={1\over M}\sum_{n\in\mathbb Z}S(n,K;M)I_b(n),            \tag{84.7}
\]

where

\[
 S(n,K;M)=\sum_{x\bmod M}^{*}e_M(nx+K\bar x).              \tag{84.8}
\]

The same-residue mode and the literal integer difference \(d=0\) have
already been removed exactly once and are target-safe. The complete
remaining smooth-main object is

\[
 \boxed{
 \mathfrak Y_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_{n\in\mathbb Z}
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.}                              \tag{84.9}
\]

Here \(M=M_{\kappa,b}\) inside the \(b\)-sum. The target is

\[
 \mathfrak Y_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon {J^2\over T}.              \tag{84.10}
\]

Terms \(d\ne0\) with \(d\equiv0\pmod M\) remain in (84.9). The
Ramanujan subtraction \(c_M(d)\) remains for every \(d\ne0\). Empty
parity and gcd classes contribute zero only through their exact support.

The inherited absolute offset capacity is

\[
 X^\varepsilon{C^3\over TQ^{5/12}}.                       \tag{84.11}
\]

A gain \(B^{-\delta}\) reaches

\[
 C\le J^{(13/6-3\delta/5)/(3-\delta)}.                    \tag{84.12}
\]

Thus \(\delta=1/2\) reaches \(J^{56/75}\) and
\(\delta=5/9\) closes the frozen band.

## 3. Exact stationary geometry to be audited

For the stationary sign and \(n>0\), the phase in (84.6) is

\[
 \Phi_{b,n}(x)=-{A_{\kappa,b}\over gx}-{nx\over M}.
\]

Its critical point, when it lies in the exact \(x\)-support, is

\[
 x_{b,n}=\sqrt{{A_{\kappa,b}M\over gn}}.                  \tag{84.13}
\]

Since \(gM=4b\), the critical phase has the exact algebraic identity

\[
 2\sqrt{{A_{\kappa,b}n\over gM}}
 =\left(\sqrt X+{\sqrt{\kappa k}\over b}\right)\sqrt n.   \tag{84.14}
\]

The active stationary scale is

\[
 n\asymp N_b:={A_{\kappa,b}Mg\over C^2}
 \asymp {b^2X\over C^2}\asymp Q^2.                       \tag{84.15}
\]

The exact constants, Gaussian phase, critical coefficient, support
edges, and error terms in the stationary expansion are not frozen as
proved by this packet. They are Round-84 obligations.

For \(n,n+d>0\), the leading phase difference suggested by (84.14) is

\[
 \Psi_{b,d}(n)
 =-\lambda_b(\sqrt{n+d}-\sqrt n),
 \qquad
 \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b}.              \tag{84.16}
\]

On a progression \(n=r+M\ell\), its exact derivatives are

\[
 {d\over d\ell}\Psi_{b,d}(r+M\ell)
 =-{M\lambda_b\over2}
 \left({1\over\sqrt{n+d}}-{1\over\sqrt n}\right),         \tag{84.17}
\]

\[
 {d^2\over d\ell^2}\Psi_{b,d}(r+M\ell)
 ={M^2\lambda_b\over4}
 \left((n+d)^{-3/2}-n^{-3/2}\right).                      \tag{84.18}
\]

These formulas do not by themselves imply cancellation: integer and
near-integer first derivatives, small \(d\), saddle entry/exit, the
periodic Kloosterman coefficient, and complete-transform self-return
must all be audited.

## 4. Frozen distinctions

The following objects are distinct and must not be merged:

1. residue diagonal \(a=0\);
2. literal dual difference \(d=0\);
3. nonzero multiples \(d\equiv0\pmod M\);
4. zero Ramanujan frequency and gcd-degenerate nonzero frequencies;
5. stationary bulk, saddle entry/exit, and nonstationary tails;
6. odd and the two rescaled even local classes;
7. a bound for the actual \(I_b(n+d)\overline{I_b(n)}\) and an arbitrary
   coefficient large sieve;
8. a signed estimate after a transform and an involutive self-return.

Prime-power offsets in the preceding residue representation show that a
uniform coefficient-free square-root rational-sum bound is false. The
all-offset kernel has a phase-conjugating rank-one direction for arbitrary
weights. Neither fact is an actual-symbol counterexample to (84.10).

## 5. Promotion rule and scope

A Round-84 candidate may change the graph only if it does one of the
following with all classes, errors, and owners retained:

1. proves (84.10) on a nonempty new \(C\)-interval;
2. proves a fixed \(B^{-\delta}\), \(\delta>0\), gain and states the
   exact endpoint (84.12);
3. removes a nontrivial uniform family of \(d\ne0\) modes target-safely
   and isolates a strictly smaller exact signed survivor;
4. proves a rigorous actual-symbol no-go that forces a different
   representation or mechanism.

No result may promote \(C>J^{3/4}\), transition errors or axes outside
their accepted range, cone edges, other radial sectors, full
`M9-M1`, `M9`, or the Gauss-circle exponent.

## 6. Required controls

- exact \(M^{-2}\) normalization and target ledger;
- all three local units and the compatible sign of \(k\);
- stationary sign, Gaussian constant, and exact phase (84.14);
- support \(n,n+d\), saddle entry/exit, and nonstationary tails;
- literal \(d=0\) removed once, but nonzero modulus multiples retained;
- Ramanujan subtraction and gcd-degenerate modes;
- actual symbol derivatives versus the accepted BV input;
- small, mesoscopic, large, negative, and wraparound differences;
- first-derivative integer resonances on \(n=r+M\ell\);
- perfect-square, fourth-power, and phase-conjugating controls;
- complete transform and stationary self-return;
- current primary-source hypotheses at \(M\asymp B\), \(n\asymp Q^2\);
- transition, axis, endpoint, and downstream ownership.

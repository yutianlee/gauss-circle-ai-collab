# Round 89 derivation packet: bad-prime and nonunit period fibres

Starting graph SHA-256:
`b279e9e671b54b43855bdfc90727e36e808eb539578dac0faeb115394789f674`.

This packet is the complete statement-only input. Reports and historical
derivations are not accepted unless explicitly stated here.

## 1. Frozen scales and target

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},
 \qquad B=C/T,
\]

with

\[
 J^{13/18}<C\leq J^{3/4},\qquad M\asymp B.
\]

The deep stationary-difference range is

\[
 D_1=\lfloor J^{87/140}\rfloor,qquad
 E_*=\lfloor Q^2J^{-1/20}\rfloor,qquad
 D_1<|d|<\Delta_b-E_*.
\]

For one fixed smooth nonaxial principal component, sign, class, reflected
orientation, and dyadic \(D\), the target budget is

\[
 X^\varepsilon {D\over B}J^{14/5}.                    \tag{89.1}
\]

No claim is requested for \(C>J^{3/4}\), raw transitions, axes, cone
edges, other radial sectors, full M9-M1, M9-M2, M9, endpoint uniformity,
R5-Full, or the global exponent.

## 2. Normalized physical rows and ownership

The normalized row is

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.            \tag{89.2}
\]

For a physical ordered pair \(P=(x,y)\), \(x\ne y\), set

\[
 F_{b,P}=e_M(K(\bar x-\bar y))
 \mathcal R_{b,x}\overline{\mathcal R_{b,y}},
 \qquad
 f_{b,P}=\Pi_{b,D}F_{b,P}.                              \tag{89.3}
\]

The two row normalizations already supply \(M^{-2}\). Do not insert
another. The global integer shift \(u=0\) is removed exactly by

\[
 \mathcal K_D^\circ(\theta)=|D_D(\theta)|^2-D,
 \qquad \|\mathcal K_D^\circ\|_1\leq2D.                \tag{89.4}
\]

Round 87 already owns the complete full-factor same-group package.
Round 88 also owns the two disjoint target-safe packages in Section 4.

## 3. Local completed trace

Parameterize a pair of physical ordered pairs by

\[
 P=(x,x-A),\qquad P'=(x-V,x-V-B_2).
\]

For \(q=p^\nu\Vert M\), define

\[
 \Omega_q=\{x\bmod q:p\nmid x(x-A)(x-V)(x-V-B_2)\},
\]

\[
 \Phi(x)=x^{-1}-(x-A)^{-1}-(x-V)^{-1}
          +(x-V-B_2)^{-1},                              \tag{89.5}
\]

and the reciprocal masked weight

\[
 w_q(x)=1_{\Omega_q}(x)e_q(K_q\Phi(x)).                 \tag{89.6}
\]

If the mask is empty, the local tensor is zero. Otherwise its period
group is a unique subgroup. If its exact period is \(p^{\nu-j_q}\),
then

\[
 \mathfrak T_q(u_q)=0\quad(p^{j_q}\nmid u_q),
\]

and

\[
 \mathfrak T_q(p^{j_q}u')
 =p^{2j_q}\mathfrak T^{\downarrow}_{p^{\nu-j_q}}(u').  \tag{89.7}
\]

The factor is \(p^{2j_q}\). Frequency sparsity alone does not reduce
the Fejer mass. The exact global tensor is over full prime powers and
retains the full \(2\)-part.

Before inequalities, the completed physical symbol is

\[
 {1\over M^5}\sum_{n,m}
 \Omega_{b,d,u}(n,m)e_M(dV+nA-mB_2)
 \mathfrak T_M(u,A,B_2,V),                              \tag{89.8}
\]

where

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).                             \tag{89.9}
\]

This retains the four-Kloosterman term, both Ramanujan cross terms, the
Ramanujan square, both signs, nonzero modulus multiples, and exact deep
support.

## 4. Accepted Round-88 deletions

Let \(R_*(P,P')\) be the first quotient at which the two physical labels
coincide in a Round-87 coarse group after reduction. Put

\[
 \rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right).     \tag{89.10}
\]

Every shell \(1<R_*\leq\rho_*\) is already target-safe.

At a nonempty reciprocal period with \(p\geq11\), \(p\nmid K_q\), put
\(a_q=\min(j_q,\nu-j_q)\), and define

\[
 \mathfrak a=
 \prod_{\substack{p^\nu\Vert M\\p\geq11,\ p\nmid K_q}}
 p^{a_q}.
\]

After the coarse deletion, every complete fibre with

\[
 \mathfrak a\geq M^2/\rho_*^2                         \tag{89.11}
\]

is target-safe. These owners must not be reinserted.

## 5. Exact Round-89 survivor and objective

The frozen hard edge set has

\[
 R_*>\rho_*,\qquad
 \mathfrak a<M^2/\rho_*^2.                              \tag{89.12}
\]

It retains:

- masked period fibres at \(p=2,3,5,7\);
- nonunit-\(K_q\) conductor drops at every prime;
- affine periods of \(e_q(u_qx)w_q(x)\) not already explained by a
  reciprocal period;
- projection-only and genuinely aperiodic local factors;
- shallow good-prime lifts that fail (89.11).

Round 89 has one objective: classify the complete small-prime,
nonunit-\(K\), and full \(2\)-adic reciprocal-period fibres and prove a
nonempty target-safe directed-graph package, or give a rigorous no-go and
isolate the smallest exact actual-symbol survivor. Keep affine and
aperiodic factors separate unless an exact identity joins them.

For any selected directed physical-edge set of maximum in- and
out-degree \(\Delta\), the accepted row bound gives

\[
 |\mathcal G_{\mathcal E}(D)|
 \ll_\varepsilon X^\varepsilon
 DB^3\Delta T^4Q^{-5/6}.                               \tag{89.13}
\]

Thus \(\Delta\leq\rho_*^2\) is target-safe. A proposed bad-prime
conductor must be derived from the complete mask and must control both
directed degrees.

## 6. Forbidden shortcuts and controls

- Do not classify periods from the numerator of \(\Phi\) alone.
- Do not replace the full \(2\)-part by a parity or squarefree surrogate.
- Do not confuse reciprocal-weight periods with affine cancellation in
  \(u+K\Phi'\).
- Do not use \(p^j\) in place of the completed descent \(p^{2j}\).
- Do not claim a Fejer gain from sparse frequency support.
- Do not use coefficientwise square-root cancellation: an exact
  \(3^\nu\) cross-group family has local completed trace \(q^2/3\).
- Do not reopen Round-87 same-group, Round-88 coarse shells, or the
  global \(u=0\) owner.
- Preserve (89.8)--(89.9), \(Q^{-5/12}\), signs, modulus multiples,
  Ramanujan terms, support, perfect powers, and transform self-return.

Computation may only diagnose finite local patterns. Every promoted
asymptotic statement needs an algebraic or analytic proof.

## 7. Required report contract

Every report has exactly seven numbered sections:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control tests and outcomes.
6. Dependencies and exact artifacts used.
7. Recommended state effect.


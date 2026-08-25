# Round 153 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Starting graph: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Decision: promote one exact, route-scoped recombination obstruction
- Terminal label: `squarefree_kernel_bilinear_no_go`

## 1. Decision

Round 153 proves an exact structural fact about the proposed squarefree
Mobius-bilinear route. Complete Mobius inversion followed by complete
recombination does not create independent Type-I/Type-II owners. It returns
the original direct large-defect wave, together with an absolutely
target-safe boundary.

This closes the proposed complete-recombination route, but it does not prove
the open scalar and does not rule out a future coefficient-sensitive signed
bilinear estimate before recombination. No new scale range and no global
exponent are obtained.

## 2. Exact promoted kernel

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad S=\lceil M^{1/4}\rceil,
\tag{153.J1}
$$

and retain the literal zero-extended weight

$$
 F_U(n)={\bf1}_{n\ {
m odd}}
 {\bf1}_{|k(n)^2-Nn|>J}
 \chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}).
\tag{153.J2}
$$

The Round-152 survivor is exactly

$$
 P_U^*=\sum_{\substack{s<S\\s\ {
m odd}}}
 \sum_{\tau\ {
m odd}}\mu^2(\tau)F_U(\tau s^2).
\tag{153.J3}
$$

For odd $r$, define

$$
 C_S(r)=\sum_{\substack{a\mid r\\r/a<S}}\mu(a).
\tag{153.J4}
$$

Then finite Mobius inversion, $\tau=a^2b$, and $r=as$ give

$$
 P_U^*=\sum_{r\ {
m odd}}C_S(r)
 \sum_{b\ {
m odd}}F_U(r^2b).
\tag{153.J5}
$$

For $r<S$, every divisor is present, so

$$
 C_S(r)=\sum_{a\mid r}\mu(a)={\bf1}_{r=1}.
\tag{153.J6}
$$

Consequently

$$
 P_U^*=\sum_{b\ {
m odd}}F_U(b)+E_S,
 \qquad
 E_S=\sum_{\substack{r\ge S\\r\ {
m odd}}}
 C_S(r)\sum_{b\ {
m odd}}F_U(r^2b).
\tag{153.J7}
$$

No coprimality between $\tau$ and $s$, $a$ and $b$, or $a$ and $s$ is
inserted. Every variable is positive and odd, and the strict ceiling is
literal: an admissible equality $r=S$ belongs to the boundary.

## 3. Boundary proof and Round-152 seam

On literal support, $r^2b\asymp M$,
$|C_S(r)|\le d(r)\ll_\varepsilon X^\varepsilon$, and
$|F_U(r^2b)|\ll_\varepsilon M^{-3/4}X^\varepsilon$. Hence

$$
\begin{aligned}
 |E_S|
 &\ll_\varepsilon M^{-3/4}X^\varepsilon
 \sum_{S\le r\ll\sqrt M}\left(1+\frac{M}{r^2}\right)\\
 &\ll_\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{153.J8}
$$

The defect mask only deletes terms in this positive boundary estimate. It
is never deleted inside a signed correlation. Round 152 separately owns the
complete exact- and small-defect scalar sectors, and the expanded
representation multiplicity is divisor-bounded, so those sectors may be
removed before Cauchy. This does not license term deletion after Cauchy or
for another profile.

The mathematical review supplies the sharper consistency check
$E_S=-P_{\mathcal L_2}$, where $P_{\mathcal L_2}$ is the already safe
large-square-factor sector. Thus

$$
 P_U^*=\sum_{b\ {
m odd}}F_U(b)+O_\varepsilon(X^\varepsilon)
      =P_U+O_\varepsilon(X^\varepsilon).
\tag{153.J9}
$$

## 4. Bilinear and source adjudication

The discovery and blind reports agree, after correction, on the exact
dyadic relation

$$
 A^2Bs^2\asymp M,
\tag{153.J10}
$$

and on the compulsory $a=s=1$ seam. For the licensed
$(195/796,235/398)$ pair, the Type-I block carries the positive factor
$A^{123/398}$; after absolute summation over $s\asymp S_0$, the factor is
$(AS_0)^{123/398}$. The earlier generic sign claim
$\lambda-\kappa\ge1/2$ was false and is not promoted.

The Cauchy diagonals, algebraic spacing bounds, and pigeonhole counts in the
reports are upper capacities for coefficient-blind majorants. They are not
signed lower bounds. The corrected $R/(As)$ spacing figure is an optimistic
all-$B$ control, not a literal fixed-fibre count, and the ambient
pigeonhole capacity need not be occupied by the actual masked coefficient.

The terminal source review verifies the Bourgain and Tao--Trudgian--Yang
one-variable boundary and audits the closest bilinear sources. No audited
theorem estimates the literal survivor below $M^{449}\asymp R^{780}$.
Robert--Sargos Theorem 1 does not directly accept the coupled actual profile
and mask; even its more favourable separated model has a printed upper-bound
term at least $R^{1/2}M^{-1/4}$ in the open range. This is a direct-source
no-match and power obstruction only, not an impossibility theorem or a lower
bound for the signed sum.

## 5. Review gate

The terminal gate is fully GREEN:

- `reviews/independent_round153_mobius_collapse_math_review.md` independently
  rederives the finite inversion, parity, ceiling, boundary, mask, profile,
  external-coefficient, and Round-152 seams;
- `reviews/hostile_round153_bilinear_scope_review.md` verifies the corrected
  Type-I powers, Cauchy coefficients, collision classes, mask scope, and
  route-only meaning of the no-go label; and
- `reviews/source_conductor_round153_final.md` verifies the primary theorem
  statements, hypotheses, translations, and direct no-matches.

The candidate and corrected reports contain no remaining mandatory defect.
The terminal label means only that complete Mobius inversion plus complete
recombination self-returns.

## 6. First open estimate and scope

The first open estimate is unchanged:

$$
 \left|\sum_{b\ {
m odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon
 \qquad(M^{449}\ll R^{780}).
\tag{153.J11}
$$

Equivalently, the exact $P_U^*$ and direct $P_U$ waves remain open after
restoring accepted owners. A future signed bilinear theorem remains possible;
by the exact collapse, it would also prove the direct wave. A theorem for the
isolated $s=1$ squarefree layer would be partial progress only unless the
remaining $s$-layers were also owned.

Nothing in this round treats $D>1$, $L>1$, the growing-$M$ generic sector,
an original $t\ge2$ layer, the Round-138 cross owner, full M1 or M2, endpoint
uniformity, M9, the conditional bridge, or the quarter theorem.

## 7. State decision

Create one proved-internal obstruction for the exact complete-Mobius
collapse. Update the two Round-152 frontier nodes, the lower-cone collar, and
the global lower-radial obligation with this exact dependency. Reject only
the overbroad Type-I/Type-II, Cauchy, mask, spacing, source, and downstream
inferences explicitly tested here.

The internal global exponent remains $1/3$. The separately audited external
Li--Yang exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{153.J12}
$$

No global exponent changes in Round 153.

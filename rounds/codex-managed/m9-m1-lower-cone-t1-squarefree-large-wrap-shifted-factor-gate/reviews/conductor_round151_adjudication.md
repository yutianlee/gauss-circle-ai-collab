# Round 151 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Starting graph: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Decision: promote exact character coordinates, three strict row ranges, and a scoped reciprocal-transform obstruction
- Terminal label: `strict_large_wrap_character_range`

## 1. Decision

Round 151 proves genuine strict target-safe ranges, not the complete
growing-$M$ collar.  The accepted kernel consists of:

1. the exact two-adic transfer of $\chi_4$ to odd shifted differences,
   together with positivity, the full parity ledger, and the compulsory
   inverse divisor fibre $h\mid g$;
2. an all-scale target-safe family containing every wrap with
   $2^{\nu_2(|k|)}\gg R^2$;
3. uniform sampled bounded variation of the actual retained Round-148
   denominator profile at every allowed scale;
4. a source-legal Bourgain full-row corridor and a source-legal
   Tao--Trudgian--Yang low-row corridor; and
5. the boundary-complete $D=d=L=1$ reciprocal transform, whose
   square-root main wave is a phase/principal-symbol self-return rather
   than an automatic gain.

The Bourgain source node must be corrected in the authoritative graph:
Theorem 4 has the direct window
$\mathcal T^{17/42}\ll H\ll\mathcal T^{1/2}$, but Theorem 6 states a
global exponent pair in the standard derivative class.  The complete
low-two-adic isolated collar outside the proved row corridors remains
open, as do the growing-$M$ generic complement and every downstream
owner.  No global exponent changes.

## 2. Exact shifted-factor kernel

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

Retain the exact Round-150 row, including both compressed coefficients,
prefixes, profiles, incidence masks, common gcd, coprimality conditions,
character, reciprocal phase, and every support restriction.  For a
nonzero centered wrap put

$$
 A=NL_1-khr_1,\qquad B=NL_2+khr_2,\qquad
 j=\nu_2(|k|),
$$

where $q_i=hr_i$, $(r_1,r_2)=1$, and all $L_i,h,r_i$ are positive odd.
The exact identities are

$$
 AB=N^2L_1L_2+kh\rho,
$$

$$
 r_2A=NL_2r_1+\rho,\qquad
 r_1B=NL_1r_2-\rho.
$$

On $0<|\rho|\le hr_1r_2/D$, the error-to-main ratios are
$O(Q/(DN))=O(R^{-2})$, so $A,B>0$, including when $q_i\mid N$.
Writing $k=2^j\kappa$ with $\kappa$ signed odd gives the odd nonzero
integers

$$
 x=\frac{NL_1-A}{2^j}=\kappa hr_1,\qquad
 y=\frac{B-NL_2}{2^j}=\kappa hr_2.
$$

Hence, for both signs of $k$ and every parity of $N$,

$$
 \boxed{\chi_4(L_1L_2r_1r_2)=\chi_4(L_1L_2xy).}
$$

It is generally unlawful to apply $\chi_4$ directly to $A$ or $B$.
If $n=\nu_2(N)$, then

$$
 (\nu_2(A),\nu_2(B))=
 \begin{cases}
 (j,j),&j<n,\\
 (n,n),&j>n,\\
 (\ge n+1,\ge n+1),&j=n.
 \end{cases}
$$

Since $\delta=L_1r_2-L_2r_1$ is even, $\rho$ is odd exactly when
$j=0$.  With $\nu_2(0)=+\infty$, the candidate's complete valuation
formula covers $\delta=0$ as well.

Conversely, for fixed $A,B,j,L_1,L_2$, let

$$
 g=(|x|,|y|),\qquad \epsilon=\operatorname {sgn}x,\qquad
 r_1=|x|/g,\quad r_2=|y|/g.
$$

The preimages are indexed exactly by the positive odd divisors $h\mid g$
that pass every original support, coprimality, centeredness, collar,
profile, and packet test, with

$$
 k=\epsilon2^j g/h,\qquad kh=\epsilon2^jg.
$$

The fibre has size $O_\varepsilon(X^\varepsilon)$, but it cannot be
discarded: $q_i=hr_i$, $k$, both profile samples, and the phase
denominator vary with $h$.  This coordinate change is exact and supplies
no cancellation by itself.

Support and centering give $|k|\ll N/Q$.  Choose
$2^{J_*}\asymp N/R^2\asymp R^2$.  The wraps with
$\nu_2(|k|)\ge J_*$ occupy

$$
 O\!\left(1+\frac{N}{Q2^{J_*}}\right)
 =O(1+R^2/Q)
$$

classes.  The accepted Round-150 arbitrary fixed-wrap theorem therefore
prices this entire family absolutely by

$$
 DQ(1+R^2/Q)X^\varepsilon
 \ll R^2DX^\varepsilon.
$$

## 3. Actual profile and exponent-pair ranges

For fixed $d,L$, write $q=LQy$.  The exact physical sample is

$$
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
$$

The accepted Round-148 factorization has $O(1)$ bulk variation, radial
derivative $O(M^{1/2})$ on normalized width $O(M^{-1/2})$, and cone
derivative $O(D^{1/2})$ on width $O(D^{-1/2})$.  Finite products,
components, and bookkeeping jumps preserve $O_\varepsilon(X^\varepsilon)$
variation.  Hard collars retain their prior owners, and the floor prefix
inside $B_{d,U}(L)$ is independent of $q$.  Thus

$$
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_q\mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon
$$

uniformly at every scale.  This is a theorem for the actual profile, not
for an arbitrary bounded smooth weight.

Resolve $(L,q)=1$ by Mobius inversion, write $q=c(4n+a)$, and first apply
an unweighted interval estimate.  The progression length and phase
parameter are

$$
 H_c\asymp LQ/c,\qquad
 \mathcal T_c\asymp Nd/Q,\qquad
 \mathcal T_c/H_c\asymp cE/L.
$$

On $\mathcal T_c\ge H_c$, an audited exponent pair $(\kappa,\lambda)$
gives

$$
 |S_{d,L}|\ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda X^\varepsilon
$$

after the divisor sum and Abel summation.  The fixed comparable edge
$\mathcal T_c<H_c$ is covered by the stronger second-derivative estimate
$O(H_c^{1/2})$, since both pairs used below have $\lambda>1/2$.

Bourgain's global pair $(13/84,55/84)$ has
$\lambda-\kappa=1/2$.  The accepted half-weight coefficient norm gives

$$
 |G_U(d)|\ll_\varepsilon
 E^{13/84}Q^{55/84}X^\varepsilon.
$$

After squaring and summing the rows, this is target-safe exactly when

$$
 \boxed{D^{84}R^{52}\ll M^{29}.}
$$

At $M\asymp R^2$, it allows $D\ll R^{1/14}$.  For $D=1$, every centered
nonexact pair lies in the collar, so the full-row bound, after subtracting
the accepted exact and packet owners, controls the complete large-wrap
collar in this range.  For $D>1$, it controls collar and generic pieces
jointly and is not a theorem for an arbitrarily isolated signed collar.

The Tao--Trudgian--Yang pair $(89/1282,997/1282)$ instead gives, for the
row restricted to $L\le L_0$,

$$
 |G_{U,\le L_0}(d)|\ll_\varepsilon
 E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon,
$$

and the low-low energy is target-safe under

$$
 \boxed{M^{819}\gg R^{1424}D^{1816}L_0^{534}.}
$$

At $D=L_0=1$, this starts at $M\gg R^{1424/819}$.  At
$M\asymp R^2$, it becomes
$D^{1816}L_0^{534}\ll R^{214}$.  The $L>L_0$ square and the low-high
cross term are not included.

## 4. Reciprocal transform and source reconciliation

At $D=d=L=1$, retain the literal coefficient
$\widetilde S_U=B_{1,U}(1)S_U$, where

$$
 S_U=\sum_{q>0}\chi_4(q)
 \mathscr A_{1,M,U}(1,4N/q^2)e(N/q).
$$

Extend the compact smooth weight by zero before Poisson summation.  The
identity

$$
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
$$

produces the boundary-complete transform

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
$$

$$
 P_U=\sum_{\ell>0\ {
m odd}}
 \chi_4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}).
$$

The error uses the accepted Round-148 derivative, buffer, transition, and
tail ledger.  The exact coefficient $B_{1,U}(1)$ remains in the pair.
A second stationary transform returns the reciprocal phase and principal
symbol, with reciprocal amplitudes and cancelling Gaussian units.  It does
not prove exact composition of all lower symbols, tails, or endpoints.
The direct and dual absolute capacities are

$$
 \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon.
$$

They give no new intermediate-scale signed estimate and are not signed
lower bounds.  The first missing endpoint input is
$|P_U|\ll_\varepsilon X^\varepsilon$ outside the strict ranges.

The corrected Bourgain source card distinguishes the Theorem-4 direct
window from the global Theorem-6 exponent-pair interface.  Section 5 uses
near-square rescaling, $(1/2,1/2)$ in the extreme long range, the
Poisson/partial-summation $B$-process in the remaining long range, and a
proper-subinterval extension with the Sargos partial-sum device.  The
reciprocal derivative class and all project-side convention repairs were
checked independently.

The Duke--Friedlander--Iwaniec, Cowan, Blomer--Harcos, and
Bettin--Chandee printed theorems do not directly estimate the isolated
recovery-weighted collar: their coefficients, characters, levels,
averaging variables, determinant or shift families, separability, and
weight hypotheses differ.  This is a direct-specialization no-match, not
a literature impossibility theorem.

## 5. First unproved step

After deleting the accepted exact, bounded-$M$, fixed-wrap packet,
high-two-adic, Bourgain-row, and TTY low-row owners in their stated
ranges, the first remaining collar object is the exact recovered sum with

$$
 j<J_*,\qquad k\notin\mathcal K_0,\qquad
 0<|\rho|\le hr_1r_2/D,
$$

and the divisor fibre $h\mid g$ coupled to both profiles, the denominator,
the phase, the support, and the reconstructed wrap.  The transferred
character does not estimate this sum, and taking absolute values restores
the rejected all-shift capacity.

At $D=L=1$, the same first obstruction is the signed square-root-wave
estimate for $P_U$.  For the TTY route it is the complementary high-row
square and low-high cross term.  For $D>1$, a whole-row theorem does not
by itself isolate the signed collar.  The growing-$M$ generic sector,
every $t\ge2$ layer, and the independent Round-138 cross owner remain
separate.

## 6. Review gate and controls

The terminal review gate is fully GREEN:

- `independent_conductor_round151_math_review.md` independently verifies
  the literal coefficient, transfer, recovery, high-adic count,
  all-scale profile variation, both exponent-pair placements and powers,
  reciprocal transform, and scope after five literalization repairs;
- `source_conductor_round151_final.md` verifies the Bourgain correction,
  TTY interface, Mobius and Abel ordering, second-derivative edge,
  boundary-complete $B$-process source, powers, and shifted-source
  no-matches; and
- `independent_bprocess_candidate_final.md` verifies the actual-profile
  boundary relation, literal $B_{1,U}(1)$ coefficient,
  phase/principal-symbol-only self-return, capacity ledger, and exact
  $D=d=1,L_1=L_2=1$ scope.

The earlier blind report and its RED seam review remain useful evidence:
their transform algebra survives, while the asserted missing actual-profile
ledger and full-transform involution do not.  No conclusion was decided by
vote.  The conductor reproduced the algebra and power translations and
adopts only the intersection supported by proofs and seam reviews.

## 7. State effect

Create one reduction recording the exact character coordinates, inverse
fibre, high-adic family, all-scale actual-profile variation, and both
strict exponent-pair row corridors.  Create one obstruction recording the
boundary-complete endpoint transform, principal self-return, elementary
capacities, and the still-open signed square-root wave.  Correct the
Bourgain graph source node, narrow the existing large-wrap obstruction to
the low-adic residual outside the strict ranges, and update the compression,
packet, reciprocal, TTY, and global lower-radial interfaces.

Leave unchanged M9--M1, M9--M2, endpoint uniformity, M9, the conditional
bridge, the internally proved exponent $1/3$, the audited external exponent

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots,
$$

and the quarter target.

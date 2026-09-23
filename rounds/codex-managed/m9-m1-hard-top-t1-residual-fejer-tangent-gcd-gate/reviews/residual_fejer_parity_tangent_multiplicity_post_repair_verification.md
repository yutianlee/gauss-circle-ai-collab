# Round 185 post-repair Fejer, tangent, and affine verification

## 1. Result / verdict

**Verdict: GREEN**

The repaired candidate hash is exactly
74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65.
Equations (185.C1)--(185.C12), (185.C24), and (185.C32)--(185.C36)
now give a literal multiplicity-one reindexing of the residual
even-shift correlation for each \(\sigma\in\{+1,-1\}\). The repair supplies
a total residual domain, canonical affine anchors including \(U=1\), an
explicit primitive Fejer domain, positive oriented rays before phase
evaluation, and disjoint plus/minus indexing. Equation (185.C37) remains
the explicitly stated open global signed estimate; it is not used to
certify the finite reindexing.

## 2. Exact statement and hypotheses

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\geq2\), \(\sigma\in\{+1,-1\}\), and \(R_0=\lceil L\rceil\). Let
\(\rho_N\) be the allocation-independent Round-184 residual selector on
squarefree positive \(N\), and let the literal coefficient be zero off
every stated shell, cone, arithmetic, profile, endpoint, sign, and
sampling predicate. Assume the accepted diagonal estimate

\[
 D_{L,\sigma}=\sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

For every positive even gap \(r<R_0\), open the upper and lower residual
coefficients into positive odd divisors \(d'\mid N+r\) and \(d\mid N\).
After deleting the monotone sector, every remaining live tuple belongs to
exactly one of \(a=d'-d>0>b=m'-m\) or \(a<0<b\). In either orientation it
has unique invariant labels

\[
 \mathfrak f=(\kappa,g,h,U,v)
\]

satisfying (185.C24), a unique canonical anchor from (185.C32), and a
unique \(t\in I_{\mathfrak f,\omega}\). Conversely, every indexed term
whose two \(\lambda\)'s are nonzero reconstructs exactly one such opened
tuple. Under this bijection its Fejer weight, endpoint coefficients,
conjugation, phase, and character product are exactly those displayed in
(185.C34)--(185.C36).

This review treats the removal of the separately counted sector (185.C30)
as given and audits only the bounded finite seam required by the brief.

## 3. Proof or line audit

### Residual domain and Fejer connector

The branch definition in (185.C2) evaluates \(\rho_N(d)\) and the literal
symbol only when \(N,d>0\), \(N\) is squarefree, \(d\mid N\), and \(d\) is
odd. It is zero otherwise, and \(c_{N,\sigma}^{\rm rem}=0\) for \(N\leq0\).
Thus the truth table in (185.C1) yields exactly the no-pair plus
selected-neither/both residual without a zero-times-undefined convention.

Expanding the full-line sliding energy gives one diagonal copy. Splitting
each window into its even and odd offsets, applying
\(|A+B|^2\leq2|A|^2+2|B|^2\), and counting offset pairs gives \(R\)
diagonal positions and \(R-2q\) forward pairs at gap \(2q\). Hence

\[
 \mathfrak E_R\leq2D_{L,\sigma}
 +4\Re\sum_{1\leq q\leq\lfloor(R-1)/2\rfloor}
 \left(1-\frac{2q}{R}\right)
 \sum_Nz_{N+2q}\overline{z_N}.
\]

For \(R=2k+1\), the terminal gap is \(R-1\), with Fejer weight \(1/R\)
and total coefficient \(4/R\). For \(R=2k\), the terminal gap is \(R-2\),
with weight \(2/R\) and total coefficient \(8/R\). Both parity branches
are complete.

Every \(z_N\) occurs in exactly \(R\) full-line windows. At most
\(M_L+R-1\) windows meet a containing interval of \(M_L\) sites, so
Cauchy gives precisely

\[
 \left|\sum_Nz_N\right|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_R.
\]

Thus (185.C5)--(185.C7) have the correct normalization and endpoints.

### Multiplicity-one opening and tangent algebra

For fixed \(N,r,d,d'\), the assignments \(m=N/d\) and
\(m'=(N+r)/d'\) are unique, so (185.C8) has multiplicity one. Since
\(r\) is even and \(d,d'\) are odd, both
\(a=d'-d=2\alpha\) and \(b=m'-m=2\beta\) are even. Direct expansion gives

\[
 r=db+am+ab=db+am'=am+bd'
\]

and the three half-shift identities in (185.C10). Also

\[
 \chi_4(d')\chi_4(d)=(-1)^\alpha.
\]

On \(a,b\geq0\), support gives \(r\gg L(a+b)\), so only \(O(1)\)
displacement pairs and \(O(L^2)\) opened incidences occur. If both
coordinates are nonpositive, or one is zero and the other negative,
\(r>0\) is impossible. Therefore (185.C12) is a disjoint and exhaustive
opposing complement.

### Primitive labels and canonical anchors

Given a live plus tuple, define

\[
 \kappa=(d,m'),\quad d=\kappa u,\quad m'=\kappa v,\quad
 s=(d'-d)/2,\quad w=(m-m')/2.
\]

Given a live minus tuple, use \(\kappa=(d',m)\) and the analogous formulas
in (185.C17). In both cases \((u,v)=1\),
\(g=(u,s)=(u,n)\), and

\[
 u=gU,\qquad s=gS,\qquad n=gh,\qquad r=2\kappa gh.
\]

Consequently \(\kappa,g,U\) are odd,
\((gU,v)=1\), \((U,h)=1\), and \(0<2\kappa gh<R_0\), exactly as in
(185.C24). These labels are invariant and unique.

Conversely, the primitive equation together with \((U,h)=1\) gives
\((U,S)=1\), while \((gU,v)=1\) makes the constructed inward cross gcd
exactly \(\kappa\). If an indexed amplitude is nonzero, squarefreeness and
endpoint coprimality force \((\kappa,S)=1\) at the relevant upper endpoint
in the plus orientation and lower endpoint in the minus orientation.
Therefore \((d,d')=g\) as well. An artificial label violating one of these
remaining arithmetic conditions contributes zero and cannot duplicate a
live tuple.

For \(U>1\), \((U,v)=1\) makes \(\bar v\bmod U\) exist. The plus equation
requires \(S\equiv\bar vh\pmod U\), while the minus equation requires
\(S\equiv-\bar vh\pmod U\). Taking least residues therefore chooses one
and only one \(S_{0,\omega}\), and the displayed \(w_{0,\omega}\) is the
corresponding integer solution. All solutions are uniquely

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 w_{t,\omega}=w_{0,\omega}+vt.
\]

When \(U=1\), the special convention gives
\((S_{0,+},w_{0,+})=(0,-h)\) and
\((S_{0,-},w_{0,-})=(0,h)\). The plus solutions are then
\(S=t,\ w=-h+vt\), and the minus solutions are
\(S=t,\ w=h+vt\), again each exactly once. No modular inverse at modulus
one is invoked.

The restriction \(S_{t,\omega}>0,\ w_{t,\omega}>0\) is equivalent to
\(s,w>0\). It is imposed before defining the amplitudes. Therefore it
keeps the plus and minus orientations disjoint, excludes monotone and
wrong-orientation continuations of an affine line, and makes all four
endpoint factors positive. The square roots in (185.C34)--(185.C35) are
therefore real and defined before any zero coefficient is used.

### Endpoints, character, and one outer real part

For plus,

\[
 N=\kappa gU(\kappa v+2w),\qquad
 N+r=(\kappa gU+2gS)\kappa v,
\]

whose difference is \(2\kappa g(Sv-Uw)=2\kappa gh\). For minus, the two
products are reversed as in (185.C35), and their difference is
\(2\kappa g(Uw-vS)=2\kappa gh\). Thus the upper divisor, lower divisor,
and conjugation in both amplitudes exactly match
\(c_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}\).

The exponential quotient is

\[
 e(\sigma\sqrt{X(N+r)})
 \overline{e(\sigma\sqrt{XN})}
 =
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right),
\]

so the phase is correct for both signs. Since \(g\) and \(U\) are odd,

\[
 \chi_4(d')\chi_4(d)
 =(-1)^s=(-1)^S
 =(-1)^{S_{0,\omega}}(-1)^t.
\]

The outer labels are unique, the canonical anchor makes \(t\) unique,
and the oriented rays are disjoint. Hence (185.C36) is a literal
multiplicity-one reindexing, with one real part outside both orientations,
all shifts, rows, selector states, and endpoints. The same structure is
retained in the proposed dyadic estimate (185.C37).

## 4. First doubtful or unproved step

No doubtful step remains in the finite identities or reindexing covered by
this brief. The first unproved step is exactly (185.C37): a global signed
bound over a dyadic \(h\)-block. The candidate presents it as a sufficient
open relation rather than as an established estimate. This does not affect
the validity of (185.C1)--(185.C12), (185.C24), or (185.C32)--(185.C36).

## 5. Required controls and outcomes

1. **Hash control.** The repaired candidate has SHA-256
   74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65.
   Outcome: passed.
2. **Odd and even terminal gaps.** Direct offset counting gives the
   \(4/R\) coefficient at gap \(R-1\) for odd \(R\), and the \(8/R\)
   coefficient at gap \(R-2\) for even \(R\). Outcome: passed.
3. **\(U=1\) convention.** The stated anchors solve the two primitive
   equations and enumerate every positive solution exactly once without an
   inverse modulo one. Outcome: passed.
4. **Prior orientation-leakage control.** For
   \(\kappa=13,u=7,v=1,g=1,U=7,h=1\), the plus anchor is
   \(S_{0,+}=1,w_{0,+}=0\). Its former \(t=-1\) continuation has
   \(S=-6,w=-1\) and is now excluded from \(I_{\mathfrak f,+}\). The same
   tuple \((d,d',m',m)=(91,79,13,11)\) is represented uniquely in the
   minus orientation by
   \((\kappa,g,h,U,v)=(1,1,13,79,11)\), with
   \(S_{0,-}=6,w_{0,-}=1,t=0\). Outcome: passed.
5. **Square-root and zero-extension order.** On each indexed ray,
   \(S,w,\kappa,g,U,v>0\), so both endpoint products are positive before
   the phase is evaluated; the two \(\lambda\)'s then apply every remaining
   literal deletion. Outcome: passed.
6. **Character and conjugation.** Both orientations reproduce the upper
   coefficient, conjugated lower coefficient, \(\sigma\)-signed phase, and
   factor \((-1)^{S_0+t}\). Outcome: passed.
7. **Multiplicity control.** Recovering
   \(\omega,\kappa,u,v,s,w,g,U,h\) from a live opened tuple and then using
   the least-residue anchor recovers one and only one \(t\). Outcome:
   passed.

All controls are exact algebraic checks; no numerical theorem evidence was
used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/residual_fejer_parity_tangent_multiplicity_post_repair_verification.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/residual_fejer_parity_tangent_multiplicity_seam_review.md
- proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md

No other report, review, control, graph file, proof draft, validation matrix,
synthesis, web source, or computation was used.

## 7. Recommended state effect

Promote this repaired finite seam as validated evidence: retain
(185.C1)--(185.C12), (185.C24), and (185.C32)--(185.C36) as exact under
their stated hypotheses. Keep (185.C37) open and make no downstream theorem
or exponent inference from this review. Any authoritative graph change
remains the conductor's responsibility after the other required seams and
a mechanically valid State Patch.

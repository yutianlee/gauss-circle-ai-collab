# Round 185 residual Fejer/parity/tangent/multiplicity seam review

## 1. Result / verdict

**Verdict: REPAIR**

The residual definition, full-line Fejer normalization, parity connector,
terminal-gap coefficients, Cauchy endpoint factor, double-divisor opening,
product-difference identities, character law, monotone count, and abstract
opposing-orientation partition in (185.C1)--(185.C12) check out for both
signs. The endpoint products, conjugation placement, square-root phase, and
single outer real part in (185.C32)--(185.C35) also check out when restricted
to the intended orientation fibre.

As written, however, (185.C32)--(185.C36) do not impose that the affine
fibre variable still has \(s_t>0\) and \(w_t>0\). The literal coefficient
\(\lambda\) does not encode this tangent-orientation condition. Thus the
full sum over \(t\in\mathbb Z\) can contain monotone atoms or atoms belonging
to the opposite orientation, and for sufficiently negative \(t\) its
displayed square-root phase is not even defined. The row set also needs an
explicit \(0<r=2\kappa gh<R_0\) condition and one chosen anchor per primitive
row. These are finite indexing and zero-extension corrections, not a failure
of the underlying tangent algebra.

## 2. Exact statement and hypotheses

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\geq2\), \(\sigma\in\{+1,-1\}\), and \(R_0=\lceil L\rceil\). Use the
Round-184 residual selector depending only on \(N\), the literal symbol with
all stated zero extensions, and the accepted diagonal bound

\[
 \sum_N |c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

Then (185.C1)--(185.C12) are valid, with sums over positive divisors and
with \(\lambda_{N,\sigma}(d)\) understood piecewise as zero whenever \(N\)
or \(d\) is outside its positive integral domain.

For an exact version of (185.C32)--(185.C36), put \(u=gU\), choose exactly
one particular solution \((S_0,w_0)\) per primitive row of

\[
 S_0v-w_0U=h \quad\text{(plus)},\qquad
 Uw_0-vS_0=h \quad\text{(minus)},
\]

and define

\[
 S_t=S_0+Ut,\qquad s_t=gS_t,\qquad w_t=w_0+vt.
\]

The row index set must include \(0<r=2\kappa gh<R_0\), and the oriented
fibre interval must be

\[
 I_{\mathfrak f}=\{t\in\mathbb Z:S_t>0,\ w_t>0\}.
\]

Equivalently, define \(B_{\mathfrak f}^{\sigma}(t)=0\) outside this set
before evaluating either square root. With this correction and,
conditionally, the separately reviewed removal of the \(h\leq H_B\) sector,
the remaining correlation has the form in (185.C36), with \(t\) restricted
to \(I_{\mathfrak f}\) and one real part outside both orientations and every
row.

## 3. Proof or line audit

### (185.C1)--(185.C3): residual and diagonal

For squarefree \(N\), every positive odd divisor \(d\) gives the unique
allocation \(N=dm\), \(m=N/d\). The selector values \(1,0,0,1\) retain
exactly the no-pair allocations and the selected neither/both allocations.
Thus summing \(\chi_4(d)\lambda_{N,\sigma}(d)\) gives (K184.6) without
allocation multiplicity. The literal support gives all fields in (185.C2),
and \(|z_N|=|c_{N,\sigma}^{\rm rem}|\), so (185.C3) is the accepted
diagonal for either sign.

### (185.C4)--(185.C7): Fejer normalization and parity

Write

\[
 A_s=\sum_{\substack{0\leq j<R\\j\ {\rm even}}}z_{s+j},\qquad
 B_s=\sum_{\substack{0\leq j<R\\j\ {\rm odd}}}z_{s+j}.
\]

From \(|A_s+B_s|^2\leq2|A_s|^2+2|B_s|^2\), sum over the full integer line
and divide by \(R\). Across both parity classes there are exactly \(R\)
diagonal offset positions. For a positive even gap \(2q<R\), there are
exactly \(R-2q\) ordered offset pairs in the forward direction. Including
the conjugate direction gives

\[
 \mathfrak E_R
 \leq 2D_{L,\sigma}
 +4\Re\sum_{1\leq q\leq\lfloor(R-1)/2\rfloor}
 \left(1-\frac{2q}{R}\right)
 \sum_N z_{N+2q}\overline{z_N},
\]

which is (185.C6). If \(R=2k+1\), the last gap is \(R-1\), its Fejer
weight is \(1/R\), and its coefficient in (185.C6) is \(4/R\). If
\(R=2k\), the last gap is \(R-2\), its weight is \(2/R\), and its
coefficient is \(8/R\). No endpoint term is lost.

If the support is contained in \(M_L\) consecutive sites, precisely
\(M_L+R-1\) length-\(R\) windows can meet that interval, while

\[
 \sum_s\sum_{j=0}^{R-1}z_{s+j}=R\sum_Nz_N.
\]

Cauchy gives exactly (185.C7). At \(R_0=\lceil L\rceil\), its prefactor is
\(O(L)\), so an \(O(L^2X^\varepsilon)\) upper bound for the one-real-part
even correlation is sufficient.

### (185.C8)--(185.C12): divisor opening and tangent identities

Expanding
\(c_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}\)
chooses one positive odd divisor \(d'\mid N+r\) and one positive odd divisor
\(d\mid N\). Setting \(m'=(N+r)/d'\) and \(m=N/d\) is bijective, so the
opening is multiplicity one. For an even shift, \(d,d'\) odd gives
\(a=d'-d=2\alpha\), while \(N+r\equiv N\pmod2\) gives
\(b=m'-m=2\beta\). Direct expansion yields

\[
 r=db+am+ab=db+am'=am+bd'
\]

and all three formulas in (185.C10). Also

\[
 \chi_4(d')\chi_4(d)
 =(-1)^{(d'-1)/2+(d-1)/2}
 =(-1)^\alpha,
\]

because \(d-1\) is even.

On \(a,b\geq0\), support gives \(d,m\gg L\), hence
\(r\gg L(a+b)\). Since \(0<r<R_0\ll L\), only \(O(1)\) displacement
pairs occur, and each permits \(O(L^2)\) choices of \((d,m)\). This proves
(185.C11). If \(a,b\leq0\), use \(r=db+am'\leq0\); if exactly one
coordinate is zero and the other is negative, the same formula is strictly
negative. Consequently the complement is exactly (185.C12).

### (185.C32)--(185.C36): endpoints, phase, and the indexing defect

For the intended plus orientation \(s,w>0\),

\[
 N=\kappa u(\kappa v+2w),\qquad
 N+r=(\kappa u+2s)\kappa v,
\]

and subtraction gives \(r=2\kappa(sv-wu)\). For the intended minus
orientation,

\[
 N=(\kappa u+2s)\kappa v,\qquad
 N+r=\kappa u(\kappa v+2w),
\]

and subtraction gives \(r=2\kappa(uw-sv)\). Hence the upper divisor is
\(\kappa u+2s\) in (185.C34) and \(\kappa u\) in (185.C35), while the
lower coefficient is conjugated in both cases. Moreover

\[
 e(\sigma\sqrt{X(N+r)})
 \overline{e(\sigma\sqrt{XN})}
 =e\!\left(
 \frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}
 \right),
\]

so the phase and sign are correct for both values of \(\sigma\). Since
\(g,U\) are odd,

\[
 \chi_4(d')\chi_4(d)=(-1)^{s_t}
 =(-1)^{S_t}=(-1)^{S_0+t}.
\]

Thus the algebra in (185.C34)--(185.C36) is correct. It does not make the
unrestricted \(t\)-sum exact. Along one affine solution line, \(S_t\) and
\(w_t\) can cross zero. The tuple then changes orientation, but both endpoint
\(\lambda\)'s can remain arithmetically admissible. This is not a
shell/profile/selector deletion and is not supplied by \(\lambda\). Without
\(I_{\mathfrak f}\), the orientation sums need not be disjoint and the
claimed complement can contain already removed monotone terms. Without the
explicit shift condition, the row sum also need not equal the Fejer range.

No joint-\(h\) incidence power in (185.C20)--(185.C31) was reviewed here;
the removal of (185.C30) is used only conditionally.

## 4. First doubtful or unproved step

The first substantive defect occurs in the transition from (185.C24) to
(185.C32). The symbol \(s_t\) is not defined there; it must be
\(g(S_0+Ut)\). The formulas cease to parametrize the named plus or minus
orientation once either \(S_t\) or \(w_t\) is nonpositive. The next line
then evaluates the phase for every \(t\in\mathbb Z\), although far negative
\(t\) can make \(N_t\) and \(N_t+r\) negative. Multiplication by a zero
\(\lambda\) does not define a square root of a negative endpoint.

Choose one anchor per row, define \(s_t\), restrict to
\(I_{\mathfrak f}\), and put \(0<2\kappa gh<R_0\) in the row index. No new
cancellation or counting estimate is needed.

## 5. Required controls and outcomes

1. **Parity endpoints.** Direct expansion at \(R=2k\) and \(R=2k+1\)
   retains respectively gaps \(R-2\) and \(R-1\) with the coefficients
   stated above. Outcome: passed.
2. **Both orientations and signs.** Subtracting endpoint products
   reproduces \(r\), and expanding \(z_{N+r}\overline{z_N}\) gives the
   conjugation and \(\sigma\)-signed phase in (185.C34)--(185.C35).
   Outcome: passed on the oriented interval.
3. **Orientation leakage.** Take
   \(\kappa=13,u=7,v=1,g=1,U=7,h=1\) and the plus-equation anchor
   \(S_0=1,w_0=0\). At \(t=-1\),

   \[
   (d,d',m',m)=(91,79,13,11),\qquad r=26.
   \]

   Both endpoint products are squarefree, both allocation gcds are one,
   and \(91/11,79/13\in(4,16)\), but \(a=-12<0<b=2\): this is a minus,
   not a plus, atom. Thus residual and cone masks do not supply the omitted
   sign indicator. Outcome: failed as written. This is an indexing control,
   not a claim of nonzero physical mass for every remaining literal field.
4. **Full-line zero extension.** For sufficiently negative \(t\), the
   endpoint products in (185.C32)--(185.C35) become negative before any
   coefficient mask is applied. A piecewise definition is required.
   Outcome: failed as written.
5. **Outer real part.** Once the row set is a disjoint reindexing of the
   even-shift tuples, the real part remains outside shifts, orientations,
   rows, selector states, endpoints, and signs. Outcome: passed after the
   finite indexing correction.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/residual_fejer_parity_tangent_multiplicity_seam_review.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md, candidate SHA-256 791c6f3b6999991ac78198b55a106fa5e2b7767469702e853119d52b50e17385
- proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/blind_statement.md

No sibling report, proof-state file, web source, or numerical theorem evidence
was used.

## 7. Recommended state effect

Revise the candidate locally at (185.C32)--(185.C36) by defining the fibre
anchor and \(s_t\), adding the two orientation inequalities, making zero
extension precede phase evaluation, and writing the Fejer shift range in the
row index. Retain (185.C1)--(185.C12) and the endpoint, conjugation, and phase
algebra of (185.C32)--(185.C35). Do not promote (185.C36), its exact
complement, or any downstream claim until the corrected disjoint row sum is
independently checked. Make no graph change from this review alone.


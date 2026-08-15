# Hostile audit of the combined M1/M2 top cones

- Campaign: `m9-combined-top-cones`
- Round: 9
- Task: `combined_cone_hostile_audit`
- Role: hostile falsifier
- Graph SHA-256 supplied in the brief: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`
- Isolation: no other Round-9 report was read.
- Status: candidate evidence only; no shared state or synthesis was edited.

## 1. Result and verdict

The exact M1 stationary cone does put the same character and the same
global stationary-phase constant as M2 on an outer odd variable.  In that
narrow sense there is a genuine complementary-cone identity.  It is not a
cancellation identity and it is not an identity with a single actual
symmetric weight.

Let

\[
y=\lfloor\sqrt X\rfloor,\qquad q=X/y^2,\qquad
H=\lfloor yX^{-1/4}\rfloor,
\]

and let the top profile be \(W(d/y){\bf1}_{d\le y}\), with \(W(1)=1\)
and the same lower support edge as in Round 8.  Write

\[
\mathcal M_j=2\Re \mathcal M_j^+
\]

for the positive-frequency half; this is valid for the actual real top
profile.  The stationary principal parts are

\[
\boxed{
\begin{aligned}
(\mathcal M_1^+)_{\rm stat}
=-{2e(1/8)X^{1/4}\over\pi}
\sum_{1\le a\le H}{\Phi(a/(H+1))\over a^{3/4}}
\sum_{\substack{4a<n<16a\\n\ {\rm odd}}}
{\chi_4(n)W(\sqrt{4qa/n})\over n^{3/4}}
e(\sqrt{Xan}),                                      \tag{1.1}\\
(\mathcal M_2^+)_{\rm stat}
=-{2e(1/8)X^{1/4}\over\pi}
\sum_{\substack{1\le r\le H\\r\ {\rm odd}}}
{\chi_4(r)\Phi(r/(H+1))\over r^{3/4}}
\sum_{\lceil r/4\rceil\le m\le r}
{W(\sqrt{qr/(4m)})\over m^{3/4}}
e(\sqrt{Xrm}).                                      \tag{1.2}
\end{aligned}}
\]

After interchanging the two variables in (1.1), its exact form is

\[
\boxed{
(\mathcal M_1^+)_{\rm stat}
=-{2e(1/8)X^{1/4}\over\pi}
\sum_{\substack{5\le r\le16H-1\\r\ {\rm odd}}}
{\chi_4(r)\over r^{3/4}}
\sum_{\lceil r/16\rceil\le m\le\min(H,\lfloor r/4\rfloor)}
{\Phi(m/(H+1))W(\sqrt{4qm/r})\over m^{3/4}}
e(\sqrt{Xrm}).}                                     \tag{1.3}
\]

Thus, only for the common outer range \(r\le H\), the M1 lattice interval

\[
\lceil r/16\rceil\le m\le\lfloor r/4\rfloor
\]

is adjacent to the M2 interval

\[
\lceil r/4\rceil\le m\le r.
\]

Because \(r\) is odd, there is neither an integer overlap nor an integer
gap.  The common constant in (1.1)--(1.2) has the **same sign**.  The cones
therefore concatenate; they do not cancel.

The exact actual weights also obstruct a symmetric merger:

1. M1 carries \(\Phi(m/(H+1))\) on the inner, original Vaaler frequency
   after the swap, while M2 carries \(\Phi(r/(H+1))\) on the outer
   character variable.
2. M1 has a genuine unmatched tail \(H<r<16H\); M2 has no such outer
   frequencies.
3. At \(q=1\), the two spatial arguments are reciprocal, but at general
   \(q\) their product is \(q\), not \(1\):

   \[
   \sqrt{4qm/r}\sqrt{qr/(4m)}=q.
   \]

4. Even at \(q=1\), the common-edge Vaaler amplitudes are radically
   different.  Near \(r=H\), M1 sees \(\Phi(1/4+o(1))\asymp1\), while M2
   sees

   \[
   \Phi(H/(H+1))={\pi^2\over3(H+1)^2}+O(H^{-3}).
   \]

Consequently the proposed cross-cone cancellation is ruled out.  The
narrow surviving reduction is a piecewise signed product-phase cone,
together with an M1-only outer tail.  Its required signed estimate is
still open.

## 2. Derivation of the M1 constant and cone

For (h>0), put

\[
B_h=\sum_{d\le y}\chi_4(d)W(d/y)e(hX/d).
\]

The exact additive-character identity is

\[
\chi_4(d)={e(d/4)-e(3d/4)\over2i}.
\tag{2.1}
\]

For (\rho\in\{1,3\}), Poisson index (k=-b) gives phase

\[
F_{h,b,\rho}(x)={hX\over x}+\left(b+{\rho\over4}\right)x.
\]

Set (n=4b+\rho).  The stationary point, phase, second derivative and
leading integral are

\[
x_{h,n}=2\sqrt{hX/n},\qquad
F(x_{h,n})=\sqrt{Xhn},
\]

\[
F''(x_{h,n})={2hX\over x_{h,n}^3},
\]

\[
\int e(F(x))\,dx
=2e(1/8)(hX)^{1/4}n^{-3/4}e(\sqrt{Xhn})
+\hbox{remainder}.                                  \tag{2.2}
\]

The factor (2) in (2.2) is forced by

\[
{(hX)^{1/4}\over\sqrt2\,(n/4)^{3/4}}
=2(hX)^{1/4}n^{-3/4}.
\]

The support condition (1/2\le x_{h,n}/y\le1) is exactly

\[
4qh\le n\le16qh.                                    \tag{2.3}
\]

Since (n) is odd, (h\le H\le\sqrt y), and

\[
0\le q-1<{2\over y}+{1\over y^2},
\]

one has \(16h(q-1)<1\) for all sufficiently large \(X\).  Hence (2.3)
freezes to

\[
4h+1\le n\le16h-1,\qquad n\ {\rm odd},             \tag{2.4}
\]

throughout the whole square interval.  Combining the two residues in
(2.1) turns their difference into \(\chi_4(n)\), and (2.2) yields

\[
B_{h,\rm stat}
={e(1/8)(hX)^{1/4}\over i}
\sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
{\chi_4(n)W(\sqrt{4qh/n})\over n^{3/4}}
e(\sqrt{Xhn}).                                      \tag{2.5}
\]

For \(h>0\), the audited Vaaler coefficient is

\[
\alpha_{h,H}={i\Phi(h/(H+1))\over2\pi h}.
\]

Multiplying (2.5) by the exact M1 prefactor \(-4\alpha_{h,H}\) gives

\[
(-4)\left({i\Phi\over2\pi h}\right)\left({1\over i}\right)
=-{2\Phi\over\pi h},
\]

which proves every factor and sign in (1.1).

For comparison, the M2 coefficient is

\[
4\alpha_{h,H}C_h
=4\left({i\Phi\over2\pi h}\right)(2i\chi_4(h))
=-{4\Phi\chi_4(h)\over\pi h}.
\]

Its Round-8 stationary integral contributes
\(e(1/8)(hX)^{1/4}/2\).  The product is again the common constant
\(-2e(1/8)X^{1/4}/\pi\), proving (1.2).  No factor of \(4\), \(i\),
\(\pi\), or \(e(1/8)\) is available to reverse the sign of one cone.

## 3. Endpoint half-weights and boundary series for M1

For each additive shift define

\[
f_{h,\rho}(x)=W(x/y)e(hX/x+\rho x/4),
\]

\[
I_{h,\rho,k}=\int_0^y
W(x/y)e(hX/x+(\rho/4-k)x)\,dx,
\]

and

\[
\delta_{h,\rho}=hq-\rho/4.
\]

The included integer endpoint has the exact one-sided normalization

\[
\sum_{d\le y}f_{h,\rho}(d)
={1\over2}f_{h,\rho}(y)
+\operatorname {PV}\sum_{k\in\mathbb Z}I_{h,\rho,k}. \tag{3.1}
\]

At (x=y), one integration by parts gives

\[
I_{h,\rho,k}
=-{f_{h,\rho}(y)\over2\pi i(k+\delta_{h,\rho})}
+O_{h,X}(k^{-2}).                                   \tag{3.2}
\]

Therefore the additive-character endpoint, including the half weight and
the symmetric principal-value tail, is

\[
\boxed{
E_{h,\rho}(X)
={e(hX/y+\rho y/4)\over1-e(hq-\rho/4)}.}             \tag{3.3}
\]

The M1 character boundary is

\[
\boxed{
E_h^{\chi}(X)={E_{h,1}(X)-E_{h,3}(X)\over2i}.}       \tag{3.4}
\]

Both denominators in (3.3) are uniformly separated from zero because
\(h(q-1)=O(y^{-1/2})\).  Hence \(|E_h^\chi|\ll1\), giving \(O(1)\) on a
positive dyadic \(h\)-block and \(O(\log H)\) over all positive
frequencies after the Vaaler weights.

The boundary does not vanish merely because the two additive shifts were
subtracted.  At the exact square \(X=y^2\), (3.4) is exactly

\[
E_h^\chi(y^2)=
\begin{cases}
-1/2,&y\equiv0,3\pmod4,\\
+1/2,&y\equiv1,2\pmod4,
\end{cases}                                         \tag{3.5}
\]

independently of \(h\).  This is an exact special-\(X\) countermodel to a
boundary-free M1 transform.

The actual two-sided M1 boundary is nevertheless \(O(1)\).  Put
\(T=X-y^2\) and \(\theta=T/y\).  Expanding the uniformly separated
denominators in (3.3) gives

\[
E_h^\chi(X)=e(h\theta)
\left({s_y\over2}+O(h/y)\right),                    \tag{3.6}
\]

where \(s_y=-1,+1,+1,-1\) for \(y\equiv0,1,2,3\pmod4\), respectively.
Thus

\[
-8\Re\sum_{h=1}^H\alpha_{h,H}E_h^\chi(X)
={2s_y\over\pi}\sum_{h=1}^H
{\Phi(h/(H+1))\sin(2\pi h\theta)\over h}+O(H/y)
=O(1).                                               \tag{3.7}
\]

The last bound is the standard uniformly bounded sine harmonic sum plus
Abel summation for the fixed-BV Vaaler factor.  This is the only robust
frequency pairing used here: positive and negative frequencies are exact
conjugates.  It does not pair M1 stationary coefficients with M2
stationary coefficients.

For the special family \(X=y^2\), \(y\equiv0\pmod4\), the positive M1
boundary has an imaginary logarithm

\[
{i\over\pi}\sum_{h\le H}{\Phi(h/(H+1))\over h}.
\]

The positive M2 boundary has the opposite leading logarithm, because it
contains
\(-2i\sum_{h\le H,\ h\ {\rm odd}}\Phi(h/(H+1))/(\pi h)\).
Their leading logarithms cancel by the even-minus-odd harmonic sum.  This
is a genuine boundary-only cancellation with actual weights; it supplies
no cancellation in (1.1)--(1.2).

## 4. Exact coefficient countermodels to cone cancellation

### 4.1 Unmatched M1 tail

Take \(X=H^4\), \(y=H^2\), so \(q=1\) and the Vaaler height is exactly
\(H\).  In (1.3), choose

\[
r=4H+1,\qquad m=H.
\]

This is an allowed M1 stationary coefficient, and it equals the common
nonzero factor times

\[
\chi_4(4H+1)\Phi(H/(H+1))
W\!\left(\sqrt{{4H\over4H+1}}\right).
\]

For all sufficiently large \(H\), it is nonzero because
\(\Phi(u)>0\) for \(0<u<1\), \(W(1)=1\), and the displayed profile
argument tends to \(1\) from below.  M2 has no outer frequency
\(r=4H+1>H\); more strongly, this term has product
\(H(4H+1)>H^2\), while every M2 product is at most \(H^2\).  Hence no
M2 term even has the same square-root phase, and no exact full-cone
termwise cancellation exists.

### 4.2 Actual-profile mismatch in the common range

Let \(H=4k+1\) in the same exact-square family and take outer \(r=H\).
At the adjacent cone seam, the M1 coefficient with \(m=k\) contains

\[
\Phi(k/(H+1))W(\sqrt{4k/H})
\longrightarrow \Phi(1/4)>0,
\]

whereas the first M2 coefficient, \(m=k+1\), contains

\[
\Phi(H/(H+1))W(\sqrt{H/(4k+4)})
\asymp H^{-2}.
\]

The phases also involve different products, \(Hk\) and \(H(k+1)\).
Thus even the nearest possible seam pairing preserves neither amplitude
nor phase.  A symmetric folded cone appears only after replacing the
actual \(\Phi\) by an artificial constant, taking \(q=1\), and deleting
the M1 outer tail.  Even that artificial model concatenates equal-sign
cones rather than cancelling them.

## 5. Narrowest correct scope and remaining estimate

The correct combined statement is the following algebraic reduction.
For odd outer \(r\le H\), the positive stationary bulk is a single
piecewise kernel on

\[
\lceil r/16\rceil\le m\le r,
\]

with lower piece

\[
\Phi(m/(H+1))W(\sqrt{4qm/r})
\quad(m<r/4)
\]

and upper piece

\[
\Phi(r/(H+1))W(\sqrt{qr/(4m)})
\quad(m>r/4).
\]

It retains \(\chi_4(r)e(\sqrt{Xrm})\) before absolute values and must be
augmented by the M1-only range (H<r<16H).  The integer cone
complementarity survives (q\ne1) for sufficiently large (X), but
profile reflection does not.

After a dyadic decomposition (r\asymp m\asymp L), the first remaining
analytic estimate is a signed (L^{3/2}X^\varepsilon)-scale bound for
this exact piecewise normalized product-phase kernel, including the
M1-only tail.  No such estimate is proved here or in the accepted graph.
Taking absolute values gives no target saving, and cone complementarity
alone supplies none.

## 6. First doubtful or unproved step

The coefficient, cone, character, boundary, and countermodel calculations
above are exact.  The first technical line not independently reproved in
full detail here is the uniform shifted-quarter-lattice stationary-phase
remainder

\[
R_{h,\rho}\ll_W\log(2+h),
\]

which is the direct analogue of the accepted Round-8 one-sided remainder.
It would give (O_W(\log^2 H)) after the M1 Vaaler weights.  The no-go
result does not depend on this error bound: it already holds coefficient
by coefficient in the stationary principal part.  Even granting the
remainder, the signed estimate in Section 5 is the first genuinely open
analytic step.

## 7. Required controls and outcomes

1. **Modulo-four character:** pass.  Equation (2.1) gives
   \(\chi_4(n)\) on the M1 dual variable, not on its Vaaler frequency.
2. **Stationary constant:** pass.  Direct use of \(F''\) gives the factor
   \(2e(1/8)\); after \(-4\alpha_h\), M1 and M2 both have
   \(-2e(1/8)X^{1/4}/\pi\).
3. **Cone inequalities:** pass.  The exact M1 inequality is
   \(4qh\le n\le16qh\), freezing to \(4h<n<16h\) on odd integers.
4. **Non-square \(X\):** pass with scope correction.  Lattice
   complementarity survives, while the two profile arguments multiply to
   \(q\ne1\), so reflection symmetry fails.
5. **Endpoint convention:** pass.  Each additive shift needs
   \(+\tfrac12 f(y)\) and a symmetric principal-value cotangent series.
   Equation (3.5) disproves omission of their combined boundary.
6. **Actual weights:** fail for cross-cone pairing.  \(\Phi\) lies on
   different coordinates, and the M1 outer tail is unmatched.
7. **Special-\(X\) coefficient controls:** fail for cancellation.  The
   exact-square families in Sections 4.1--4.2 give an unmatched nonzero
   term and an \(H^2\)-scale seam-amplitude mismatch.
8. **Proves-too-much control:** pass.  No unsigned or
   arbitrary-coefficient analogue is claimed; the only favorable signs
   used are the actual additive \(\chi_4\) identities and real-even
   frequency pairing.
9. **Computation:** none used.

## 8. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-combined-top-cones/briefs/combined_cone_hostile_audit.md`
- `state/best_proof_draft.md` (H1--H4 and the exact M1/M2 definitions)
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`
- `rounds/codex-managed/m9-top-endpoint-transform/reports/endpoint_transform_hostile_audit.md`

No external theorem, numerical artifact, or other Round-9 report was used.

## 9. Recommended state effect

1. **Reject** any claim that the M1 and M2 top stationary cones cancel,
   have a common actual symmetric profile, or are related by an
   actual-weight-preserving reflection.
2. **Retain as candidate exact infrastructure**, after a separate seam
   review, the M1 transform (1.1), swapped cone (1.3), and boundary
   formulas (3.1)--(3.4).
3. **Retain narrowly** the common-range lattice complementarity as a
   piecewise combined-kernel reduction.  Record the different placement
   of \(\Phi\), the \(q\ne1\) profile distortion, and the unmatched M1 tail
   in its statement.
4. **Retain open** `M9-M1`, `M9-M2-top-endpoint-signed-cone`, `M9-M2`,
   `M9-endpoint-uniformity`, and `M9`.  No target estimate has been
   established.

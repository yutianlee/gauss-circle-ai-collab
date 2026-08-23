# Hostile audit: alias-curve first-derivative no-go

## 1. Result

The repaired alias-curve probe is mathematically sound as a narrowly
scoped method no-go.  Equations (P.1)/(P.15) are exact, the Poisson modes
are \(\nu=m-\sigma/4\) with the non-negligible positive band
\(\nu\asymp L\), the alias window (P.3) is nonempty, and it supplies an
allowed nonzero integer \(h\) for which the \(r\)-phase derivative is
exactly integral at an interior point.  The crossing has second derivative
\(\asymp L|j|/X\).

Consequently the proposed uniform Kusmin--Landau premise
\[
 \|\partial_r\Phi\|\gg L|j|/D
\]
is false.  This rejects only the inference based on that uniform
first-derivative gap.  It proves neither that an individual Poisson mode
has a large integral nor that the fixed-alias or full signed Gram is large.
Cancellation after a joint \((\beta,r)\) analysis, or among
\((m,\sigma,h,j)\), remains possible.

One wording repair is required: the two opposite-character channels have
the same nonzero algebraic coefficient \(+1/4\), so they cannot be deleted
by the character signs.  They need not be called pointwise
“conjugate/reinforcing” before the remaining modes and variables are
paired.  Nothing in the no-go requires such a lower-bound assertion.

## 2. Poisson modes and transverse scale

The exact identity
\[
 \chi_4(n)={e(n/4)-e(-n/4)\over2i}
\]
and ordinary Poisson summation give
\[
 \sum_n\chi_4(n)F(n)
 ={1\over2i}\sum_{\sigma=\pm1}\sigma
   \sum_{m\in\mathbb Z}
   \int F(y)e(-(m-\sigma/4)y)\,dy.
\]
Thus every dual frequency is
\[
 \nu=m-\sigma/4;
\]
there is no legal truncation to the two nominal quarter modes.

For
\[
 \beta=M(1/r-1/s)-j,\qquad
 s=s_{j+\beta}(r)={Mr\over M-(j+\beta)r},
\]
one has exactly
\[
 {\partial s\over\partial\beta}={s^2\over M}.
\]
The \(\beta\)-phase is \(k\beta-\nu s\), so its derivative is
\[
 k-\nu{s^2\over M}.
\]
On literal support, \(k\asymp K\), \(s\asymp R\), and
\(M\asymp X\), hence
\[
 \nu\asymp {Mk\over s^2}\asymp L,
\]
with positive sign.  When \(L\) grows, this band contains integer
translates \(m\asymp L\); for bounded \(L\), only the finitely many
quarter-lattice modes lying in the literal band are relevant.  The probe
needs one retained positive mode, not a claim that every
\(\nu\asymp L\) is stationary.

## 3. Exact derivative identity

After expanding the remaining character with sign \(\tau\), the phase at
fixed \(\beta\) is
\[
 \Phi_{m,\sigma,\tau,h}
 ={Mh\over r}+{\tau r\over4}+k\beta-\nu s_{j+\beta}(r).
\]
Since
\[
 \partial_rs_{j+\beta}(r)
 ={M^2\over(M-(j+\beta)r)^2}
 ={s_{j+\beta}(r)^2\over r^2},
\]
the channel \(\tau=-\sigma\) satisfies
\[
 \begin{aligned}
 \partial_r\Phi+m
 &=-{Mh\over r^2}-{\sigma\over4}
   -\left(m-{\sigma\over4}\right){s^2\over r^2}+m\\
 &=-{Mh+\nu(s^2-r^2)\over r^2}.
 \end{aligned}
\]
This proves (P.1)/(P.15), including its sign.  Adding the integer \(m\)
does not change the distance of \(\partial_r\Phi\) from an integer.

The product of the \(s\)-channel coefficient
\(\sigma/(2i)\) and the \(r\)-channel coefficient
\(\tau/(2i)\) is \(-\sigma\tau/4=+1/4\) when
\(\tau=-\sigma\).  Therefore this resonant channel is genuinely present.
The coefficient calculation alone asserts no analytic reinforcement or
lower bound.

## 4. Interior resonance window and allowed integer shift

Take \(\beta=0\), \(j>0\), and a fixed common interior interval
\(I\subset\{r\asymp R\}\).  Put
\[
 H_*(r)=-{\nu\over M}\{s_j(r)^2-r^2\}.
\]
Uniformly for \(j=o(D)\),
\[
 H_*(r)
 =-2{\nu j r^3\over M^2}\bigl(1+O(j/D)\bigr),
\]
so \(H_*\) has one sign, is strictly monotone on \(I\), and
\[
 |H_*(r)|\asymp {|j|K\over D},
 \qquad
 |H_*(I)|\asymp {|j|K\over D}.
\tag{A.1}
\]

Choose the constants in
\[
 \max(1,CD/K)\le |j|\le cDH_0/K,
 \qquad H_0=\lceil X^{1/2}/D\rceil,
\tag{A.2}
\]
with \(C\) large and \(c\) small relative to the fixed interior margins.
The lower bound makes the image length in (A.1) greater than one; if the
maximum in (A.2) is \(1\), then \(K/D>C\) and the same conclusion holds.
The upper bound keeps the entire relevant image inside
\((-c'H_0,c'H_0)\).  Since \(H_*\) never changes sign, its image contains
a nonzero integer \(h\) with \(|h|<H_0\).  At the corresponding
\(r_0\in I\),
\[
 Mh+\nu\{s_j(r_0)^2-r_0^2\}=0,
\]
and therefore \(\partial_r\Phi(r_0,0)=-m\).

The interval (A.2) is nonempty.  Indeed,
\[
 {DH_0\over K}
 \asymp {D^2\over X^{1/2}L}
 =X^{2\delta-1/2-\ell}\longrightarrow\infty
\]
because \(\ell<\delta-1/4\), while
\[
 {H_0\over K}\asymp {D\over X^{1/2}L}=o(1).
\]
Thus the upper endpoint tends to infinity but is \(o(D)\), and its
ratio to the \(CD/K\) lower endpoint is a constant multiple of
\(H_0\to\infty\).  Integer aliases satisfying (A.2) exist for all
sufficiently large \(X\).  For \(j<0\), the same construction gives an
allowed \(h\) with the opposite sign.

## 5. Profile, endpoint, and curvature seams

At the top of (A.2),
\[
 {|s_j-r|\over R}\asymp {|j|\over D}=O(H_0/K)=o(1),
 \qquad {|h|\over K}\le H_0/K=o(1).
\]
After shrinking a fixed nonvanishing core, \(r,s,k,k+h\) therefore remain
inside the same literal \(W\)- and \(q_L\)-profile interiors.  Choosing
\(c\) small also gives
\(1-|h|/H_0\gg1\), so the Fejér coefficient does not erase the
crossing.  This verifies the claimed interior and shifted-profile seams
for every nonempty common interior cell.  An empty cell contributes
nothing; a genuine endpoint-stationary cell requires a uniform endpoint
estimate and cannot restore a first-derivative gap.

At a nearest-alias boundary \(|\beta|=1/2\),
\(K\|M(1/r-1/s)\|\asymp K\).  Smooth \(k\)-summation by parts makes a
boundary collar rapidly small after its total variable count is priced,
so smoothing the alias partition does not alter the central crossing.

At the crossing, differentiating the exact identity while using its
vanishing numerator gives
\[
 \begin{aligned}
 \partial_r^2\Phi(r_0,0)
 &=-{2\nu\over r_0}
 \left\{\left(1-{jr_0\over M}\right)^{-3}-1\right\}\\
 &=-{6\nu j\over M}\bigl(1+O(j/D)\bigr).
 \end{aligned}
\]
Hence
\[
 |\partial_r^2\Phi(r_0,0)|
 \asymp {L|j|\over X},
\]
and the natural stationary length is
\[
 Y_j\asymp\sqrt{X/(L|j|)}.
\]
The lower bound in (A.2) gives
\[
 {Y_j\over D/(L|j|)}
 ={\sqrt{XL|j|}\over D}\gg\sqrt D.
\]
This compares the first- and second-derivative proof scales only.  It is
not a lower bound for a stationary contribution.

At an exact alias, \(s\) is an odd integer and
\(e(-ms)=1\); summing the two quarter components reconstructs
\(\chi_4(s)\).  Exact pairs remain in their existing divisor-count owner.
The branch \(j=0\), including the diagonal, is outside this probe.

## 6. Claim disposition and first unproved step

| Claim | Verdict | Reason |
|---|---|---|
| (P.8)--(P.12), \(\nu=m-\sigma/4\asymp L\) | Accept with clarification | All quarter-lattice translates are retained; only those meeting the literal positive transverse band are non-negligible. |
| (P.1)/(P.15) | Accept | Direct differentiation gives the displayed identity and exact sign. |
| (P.3)/(P.21) | Accept | The lower endpoint forces image length \(>1\), the upper endpoint stays below \(H_0\), and their ratio diverges. |
| Allowed integer \(h\) | Accept | The one-signed monotone image contains a nonzero integer with the required opposite sign and \(|h|<H_0\). |
| Literal profiles and endpoints | Accept under the stated common-interior hypothesis | Both relative displacements are \(o(1)\); boundary collars are rapidly small, while genuine endpoint crossings remain a separate problem. |
| (P.22)--(P.24) | Accept | The exact second derivative is \(-6\nu j/M(1+o(1))\), giving the claimed scale and stationary length. |
| “Conjugate/reinforcing channels” | Repair wording | The channels have nonzero coefficient \(+1/4\); no pointwise reinforcement or lower bound is proved. |
| Uniform KL implication (P.7)/(P.26) | Reject | The derivative is exactly integral at the constructed interior point. |
| Lower bound for a Poisson mode, fixed alias, or Gram | Reject as an inference | The probe neither states nor proves survival after joint \(\beta\)-integration or cancellation across modes. |

The first unproved replacement is a joint stationary estimate in
\((\beta,r,m,\sigma,h,j)\) retaining the literal sampled profiles and all
signed conjugate packages.  A nonstationary treatment in \(\beta\) could
still discard some individual modes; that possibility does not rescue the
proposed uniform-in-\(\beta\) first-derivative premise and supplies no
lower bound.

## 7. Dependencies, scope, and recommended effect

This audit used only
candidates/alias_curve_character_probe.md.  No sibling report, shared
state, synthesis, web source, or numerical experiment was used.

Retain the candidate as a rigorous scoped no-go after the channel-wording
repair above.  It rejects the proposed uniform
quarter-shift-Poisson/Kusmin--Landau inference and identifies the exact
interior derivative crossing and curvature scale.  Do not promote
\(O(D/(L|j|))\), a fixed-alias estimate, an unsigned capacity statement,
a lower bound, the complete flat-smooth estimate, complete UNBAL, M9-M2,
M9, or any discrepancy exponent.

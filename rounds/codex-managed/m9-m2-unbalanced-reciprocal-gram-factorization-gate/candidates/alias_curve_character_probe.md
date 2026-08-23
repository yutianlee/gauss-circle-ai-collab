# 1. Result

The proposed quarter-shift/Kusmin--Landau estimate does not follow
uniformly from Poisson summation in the transverse variable.  The exact
obstruction is a derivative self-return caused by the shifted phase.

Let

\[
 \beta_j(r,s)=M(1/r-1/s)-j,
 \qquad
 s_{j+\beta}(r)=\frac{Mr}{M-(j+\beta)r}.
\]

After Poisson summation in \(s\), write a character mode as
\(\nu=m-\sigma/4\), where \(m\in\mathbb Z\) and
\(\sigma\in\{\pm1\}\) comes from \(\chi_4(s)\).  Combining it with
the opposite character component \(-\sigma\) of \(\chi_4(r)\), the
\(r\)-phase satisfies the exact identity

\[
 \boxed{
 \partial_r\Phi_{m,\sigma,h}(r,\beta)+m
 =-\frac{Mh+\nu\{s_{j+\beta}(r)^2-r^2\}}{r^2}.}
 \tag{P.1}
\]

The active transverse modes have \(\nu\asymp L\), not just
\(\nu=\pm1/4\).  For \(\beta=0\), \(0<|j|=o(D)\), and a common
interior profile cell, the two terms on the right of (P.1) cancel for
an allowed shift of the opposite sign and size

\[
 |h|\asymp \frac{|j|K}{D}.
 \tag{P.2}
\]

Indeed, for all sufficiently large \(X\), there are integer aliases in

\[
 \max(1,C D/K)\leq |j|\leq cD H_0/K,
 \qquad H_0=\left\lceil X^{1/2}/D\right\rceil,
 \tag{P.3}
\]

and integers \(0<|h|<H_0\) for which (P.1) vanishes at an interior
point.  The crossing is nondegenerate, with

\[
 |\partial_r^2\Phi|\asymp \frac{L|j|}{X}.
 \tag{P.4}
\]

Thus the needed uniform first-derivative gap is false even at the
target-safe shift length \(H_0\).  The natural stationary scale is
\(\sqrt{X/(L|j|)}\), not \(D/(L|j|)\).  This is a rigorous no-go for
the proposed first-derivative argument, not a proof that the fully
signed fixed-alias sum is large.  A bound for that sum could still
come from cancellation among the stationary modes, aliases, and
shifts, but no such theorem is supplied here.

# 2. Exact statement and hypotheses

Use only the flat-smooth shifted Gram of the conductor candidate, with

\[
 R=X/D,\qquad K=XL/D^2,\qquad
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14.
 \tag{P.5}
\]

All amplitudes remain the literal factors

\[
 W(X/(rD))W(X/(sD))
 \frac{q_L(4X(k+h)/r^2)q_L(4Xk/s^2)}{(k+h)k};
 \tag{P.6}
\]

no sharp profile or complete-divisor replacement is made.  The probe
concerns a fixed nonzero nearest alias \(j\), \(|j|\ll D\), and every
integer \(|h|<H_0\).  If a fixed-alias cell has no common nonvanishing
interior for (P.6), that cell is already empty or profile-small.  The
no-go concerns any nonempty common interior cell, which is the only
case in which a new estimate is needed.

The nearest-alias cell can be smoothed before Poisson summation.  At
its half-integer boundaries one has
\(K\|M(1/r-1/s)\|\asymp K\), so repeated \(k\)-summation by parts makes
the change \(O_A(K^{-A})\), after increasing \(A\) to price the total
number of variables.  This is only an auxiliary exact decomposition;
the literal kernel and its smooth tails are retained.

The claimed conclusion is deliberately scoped:

\[
 \text{Poisson in }s+\text{first-derivative KL in }r
 \quad\not\Longrightarrow\quad
 O\!\left(\frac{D}{L|j|}\right)
 \tag{P.7}
\]

uniformly in the literal profiles and the shifts.  No lower bound for
the original Gram, no unsigned capacity estimate, and no global wave
estimate is asserted.

# 3. Proof or derivation

## 3.1 Quarter-shift Poisson formula and the active modes

For every smooth compactly supported \(F\),

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
\]

gives the exact identity

\[
 \sum_{s\in\mathbb Z}\chi_4(s)F(s)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
   \sum_{m\in\mathbb Z}
   \int_{\mathbb R}F(y)e(-(m-\sigma/4)y)\,dy.
 \tag{P.8}
\]

Thus the dual frequencies are

\[
 \nu=m-\sigma/4,
 \tag{P.9}
\]

and all integer translates must be kept.  In a fixed \(j\)-cell,
change variables from \(s\) to \(\beta=\beta_j(r,s)\).  Exactly,

\[
 s=s_{j+\beta}(r),\qquad
 \frac{\partial s}{\partial\beta}=\frac{s^2}{M}\asymp\frac K L.
 \tag{P.10}
\]

For a fixed \(k\asymp K\), the phase in the transformed integral is

\[
 k\beta-\nu s_{j+\beta}(r),
\]

whose \(\beta\)-derivative is

\[
 k-\nu\frac{s^2}{M}.
 \tag{P.11}
\]

Consequently the non-negligible dual band is

\[
 \nu\asymp \frac{Mk}{s^2}\asymp L,
 \tag{P.12}
\]

with positive sign.  Modes outside a fixed enlargement of this band
are removed by integration by parts in \(\beta\), using the smooth
literal amplitudes and the smoothed alias-cell boundary.  A
stationary point entering or leaving a profile support is retained,
not deleted.  In particular, keeping only the nominal modes
\(\pm1/4\) is not a lawful approximation when \(L\) grows: the
integer translates \(m\asymp L\) carry the transverse mass.

## 3.2 Exact return of the quarter character

Expand the remaining character as

\[
 \chi_4(r)=\frac1{2i}
 \sum_{\tau=\pm1}\tau e(\tau r/4).
\]

At fixed \((m,\sigma,k,\beta,h)\), the \(r\)-dependent phase after
(P.8) is

\[
 \Phi_{m,\sigma,\tau,h}(r,\beta)
 =\frac{Mh}{r}+\frac{\tau r}{4}
   +k\beta-\nu s_{j+\beta}(r).
 \tag{P.13}
\]

Since

\[
 \partial_r s_{j+\beta}(r)
 =\frac{M^2}{(M-(j+\beta)r)^2}
 =\frac{s_{j+\beta}(r)^2}{r^2},
 \tag{P.14}
\]

the opposite character channel \(\tau=-\sigma\) gives

\[
\begin{aligned}
 \partial_r\Phi+m
 &=-\frac{Mh}{r^2}-\frac{\sigma}{4}
   -\left(m-\frac\sigma4\right)\frac{s^2}{r^2}+m\\
 &=-\frac{Mh+\nu(s^2-r^2)}{r^2},
\end{aligned}
 \tag{P.15}
\]

which is (P.1).  This channel has coefficient
\(-\tau\sigma/4=+1/4\) in the product of the two character
expansions.  It is present with nonzero coefficient, so the character
signs alone do not delete either opposite channel.  No pointwise
reinforcement or lower bound is asserted before the remaining modes and
variables are paired.

For \(h=0\), \(\beta=0\), and \(|j|=o(D)\),

\[
 \left|\frac{s_j(r)^2-r^2}{r^2}\right|
 =\left|\left(1-\frac{jr}{M}\right)^{-2}-1\right|
 \asymp\frac{|j|}{D}.
 \tag{P.16}
\]

The hoped derivative is therefore only
\(\asymp L|j|/D\) modulo an integer.  Once this quantity reaches an
integer it has derivative crossings; before then, the shift term in
(P.15) can cancel it.

## 3.3 An interior crossing inside the allowed shift range

Take \(j>0\); the case \(j<0\) reverses the sign of \(h\).  On a fixed
common interior interval \(I\subset\{r\asymp R\}\), put

\[
 H_*(r)=-\frac{\nu}{M}\{s_j(r)^2-r^2\}.
 \tag{P.17}
\]

For \(j/D=o(1)\), this is continuous and strictly monotone on \(I\),
and

\[
 |H_*(r)|\asymp\frac{|j|K}{D},
 \qquad
 |H_*(I)|\asymp\frac{|j|K}{D}.
 \tag{P.18}
\]

Here \(|H_*(I)|\) denotes the length of its image.  The calculation is

\[
 s_j(r)^2-r^2\asymp \frac{j r^3}{M},
 \qquad
 \frac{\nu}{M}\frac{jR^3}{M}
 \asymp\frac{LjX}{D^3}=\frac{jK}{D}.
 \tag{P.19}
\]

Choose constants \(C\) large and \(c\) small relative to the fixed
interior cell.  If (P.3) holds, the image in (P.18) has length greater
than one and remains inside \((-H_0,H_0)\).  It therefore contains an
integer \(h\), and at the corresponding interior point \(r_0\),

\[
 Mh+\nu\{s_j(r_0)^2-r_0^2\}=0.
 \tag{P.20}
\]

Equation (P.15) then says
\(\partial_r\Phi(r_0,0)=-m\), exactly an integer.  The alias interval
in (P.3) is nonempty for large \(X\): its endpoint ratio is \(H_0\),
while

\[
 \frac{D H_0}{K}\asymp\frac{D^2}{X^{1/2}L}\longrightarrow\infty
 \tag{P.21}
\]

because \(\ell<\delta-1/4\).  Also
\(D H_0/K=o(D)\), so throughout this construction
\(M-jr\asymp M\) and \(s_j(r)=r(1+o(1))\).

Differentiating (P.15) at the crossing gives

\[
 |\partial_r^2\Phi(r_0,0)|\asymp\frac{\nu |j|}{M}
 \asymp\frac{L|j|}{X}.
 \tag{P.22}
\]

It is a genuine nondegenerate stationary crossing, not a removable
flat point.  Its natural discrete stationary length is

\[
 Y_j\asymp\sqrt{\frac{X}{L|j|}}.
 \tag{P.23}
\]

For \(|j|\geq C D/K\),

\[
 \frac{Y_j}{D/(L|j|)}
 =\frac{\sqrt{XL|j|}}D\gg\sqrt D.
 \tag{P.24}
\]

Thus splitting at the crossing and replacing first derivative by the
standard second-derivative scale does not recover the proposed
Kusmin--Landau saving.  Formula (P.24) is a comparison of the phase
scales, not a lower bound for the signed Gram contribution.

## 3.4 Literal-profile, endpoint, and exact-alias seams

The crossing above can be placed in a common nonvanishing interior:
\(j/D=o(1)\) implies \(s_j-r=o(R)\), and
\(|h|/K\leq H_0/K=o(1)\).  Hence neither the \(r,s\) profile overlap
nor the shifted pair \(q_L(4X(k+h)/r^2)q_L(4Xk/s^2)\) is forced to an
edge.  The Fejer coefficient is also bounded below when
\(|h|\leq cH_0\).  Smooth support endpoints therefore do not remove
the obstruction.  If a stationary point crosses an actual endpoint,
it must instead be handled by a uniform endpoint-stationary estimate;
there is no derivative gap there either.

At an exact integer alias, \(\beta=0\) and
\(s_j(r)=s\in2\mathbb Z+1\).  In (P.8), the integer factor
\(e(-ms)=1\), and the two quarter components reconstruct
\(\chi_4(s)\) exactly.  Poisson summation therefore does not give an
extra \(1/L\) saving on an exact pair.  Those pairs remain governed by
the already target-safe divisor count; they cannot be silently folded
into (P.7).  The branch \(j=0\) is outside this probe and includes the
diagonal.

# 4. First doubtful or unproved step

The first invalid line in the proposed argument would be either of the
following equivalent assertions:

\[
 \text{“only the modes }\nu=\pm1/4\text{ matter,”}
 \tag{P.25}
\]

or

\[
 \|\partial_r\Phi\|
 \gg \frac{L|j|}{D}
 \quad\text{uniformly in }m,h,r
 \tag{P.26}
\]

on the fixed-alias support.  Formula (P.12) disproves (P.25), and the
exact identity (P.15), followed by (P.20), disproves (P.26).

The first genuinely unproved replacement is a joint stationary-mode
estimate that sums the neighborhoods (P.23) over \(m\asymp L\), both
character signs, all \(|h|<H_0\), and all nonzero aliases while
retaining (P.6).  Poisson summation is invertible, so merely summing
the quarter modes back reconstructs the original shifted near-alias
survivor.  No target-closing inequality or inverse theorem follows
without new cancellation across that joint stationary set.

# 5. Required control tests and outcomes

**all_quarter_translates.**  Input: the exact formula (P.8), without
discarding integer translates.  Outcome: (P.11)--(P.12) place the
active band at \(m-\sigma/4\asymp L\).  Implication: the nominal
quarter mode alone does not represent the width-\(1/L\) kernel.

**opposite_character_channel.**  Input: all four products of the two
character expansions.  Outcome: \(\tau=-\sigma\) has coefficient
\(+1/4\) and yields (P.15).  Implication: the resonant channel cannot
be deleted by a sign convention.

**literal_h_shift.**  Input: the exact phase \(e(Mh/r)\) and
\(|h|<H_0\).  Outcome: aliases in (P.3) admit the exact cancellation
(P.20), with the required sign of \(h\).  Implication: an estimate
proved only for \(h=0\) is not uniform enough for the shifted Gram.

**stationary_crossing.**  Input: the point supplied by (P.20).
Outcome: (P.22) is nonzero and has scale \(L|j|/X\); the corresponding
length is (P.23).  Implication: first-derivative Kusmin--Landau is
inapplicable there, and its proposed scale is not recovered by the
immediate second-derivative fallback.

**profile_and_endpoint_seams.**  Input: literal factors (P.6), their
smooth edges, and the alias-cell endpoints.  Outcome: the crossing can
be chosen with \(r,s,k,k+h\) in a common interior and with
\(|h|\leq cH_0\); alias-boundary changes are rapidly small by smooth
\(k\)-summation.  Implication: neither truncation nor a vanishing
Fejer weight removes the central obstruction.  Endpoint stationary
points, when present, require their own uniform estimate.

**exact_near_and_negative_branches.**  Input: \(E=0\), \(E\ne0\),
and both signs of \(j\).  Outcome: exact pairs reconstruct their
original character and stay in the divisor-count sector; the
continuous near kernel has (P.15); changing \(j\) to \(-j\) changes
the resonant sign of \(h\).  Implication: no branch supplies a uniform
one-sided derivative gap.

**scope_control.**  Input: only one fixed nonzero alias of the
flat-smooth shifted Gram.  Outcome: no unsigned capacity, lower bound,
complete-UNBAL estimate, or circle-discrepancy estimate is inferred.
Implication: the result is a method no-go, not an overstatement about
the global sum.

# 6. Dependencies and exact artifacts used

This report used only:

1. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/blind_integer_gram_rederivation.md`;
2. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/candidates/conductor_integerization_and_shifted_gram.md`;
3. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/independent_shifted_gram_candidate_audit.md`.

No other report, state file, proof draft, strategy file, web source, or
numerical experiment was read or used.  No shared state, synthesis,
validation, or existing candidate file was edited.

# 7. Recommended state effect

**Recommended state effect: retain as a no-go; reject the proposed
first-derivative inference.**

Retain (P.8)--(P.15) and the interior resonance window
(P.17)--(P.24) as the exact obstruction.  Do not promote a bound
\(O(D/(L|j|))\), or any target-closing fixed-alias estimate, from
quarter-shift Poisson summation plus Kusmin--Landau.

A viable continuation would need a genuinely joint theorem for the
stationary lattice in \((m,h,j,r)\), with the two sampled profiles and
all conjugate signs retained, or an inverse theorem showing that those
stationary packets cancel in the complete shifted norm.  Summing the
Poisson modes back, deleting exact aliases, or ignoring the
\(e(Mh/r)\) shift only returns to the already identified signed
near-alias survivor.

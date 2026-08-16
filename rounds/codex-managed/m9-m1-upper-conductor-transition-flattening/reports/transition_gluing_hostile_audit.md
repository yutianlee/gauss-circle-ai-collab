## 1. Result

The proposed transition flattening survives the hostile test, but one
sentence in the frozen packet must be corrected.  At a boundary saddle only
the adjacent Farey face has scaled distance

\[
 O(\Lambda^{-1/2});
\]

the opposite face has distance \(\asymp \sqrt\Lambda\).  The required
\(O(\Lambda^{-1/2})\) error follows by a local Lipschitz estimate at the
adjacent face and an oscillatory-tail estimate at the opposite face.  It does
not follow by asserting that both \(Y_-\) and \(Y_+\) are small.

With that correction, the exact fixed-smooth-interior nonaxial coefficient
has the decomposition

\[
 W_{b,r}(c)=\Gamma_{\epsilon,z_*}V_{b,r}(c)+E_{b,r}(c),
 \qquad
 \|V_{b,r}\|_\infty+\operatorname {Var}V_{b,r}
 \ll_\varepsilon X^\varepsilon,
 \tag{1.1}
\]

\[
 \sup_c|E_{b,r}(c)|
 \ll_\varepsilon X^\varepsilon\Lambda^{-1/2}
 =X^\varepsilon\sqrt{c/J}
 \ll X^\varepsilon\sqrt{C/J}.                 \tag{1.2}
\]

This is a statement about the complete coefficient reconstructed from the
exact Farey integral before the artificial neighbor-numerator cuts.  The
arithmetic unit, alias, ratio symbol, stationary Jacobian, exact real centre,
and uniform stationary error are included.  The two axes remain under their
separate accepted nonstationary estimate.

The exact \(4\mid c\), \(\kappa=1\), \(\rho=\sigma=1\) control confirms,
rather than removes, the obstruction to global bounded variation.  The right
neighbor makes \(\asymp J/C\) sawtooth resets, each of scaled size
\(\asymp\sqrt{C/J}\), so the leading transition has variation capacity
\(\asymp\sqrt{J/C}\).  Left and right numerator switches are not simultaneous
in the active range, and the complete symbol has no structural cancellation
of these resets.  This does not contradict (1.1)--(1.2): the sawtooth is
placed in the pointwise-small term \(E\), for which no variation bound is
used.

Bourgain's exponent-pair theorem applies to the resulting globally smooth
main weight on every full residue progression and uniformly on its proper
subintervals.  The energy ledger is therefore valid and extends the scoped
fixed-interior range to

\[
 C\leq J^{13/18}.
\]

No conclusion about cone edges, the rest of the upper conductors, full
\(M9\!-!M1\), \(M9\), or the Gauss-circle exponent follows.

## 2. Exact statement and hypotheses

Let

\[
 R=\lfloor J\rfloor,\qquad \delta=J-R\in[0,1),\qquad
 Q=J^{2/5},\qquad T=J^{3/5},\qquad
 J^{32/45}<C\leq J^{13/18},
\]

and let \(b\asymp B=C/T\), \(c\asymp C\), \((b,c)=1\).  Fix one residue
\(c=r\pmod {4b}\), one endpoint orientation, one of the classes

\[
 \kappa=c/[c,4]\in\{1/4,1/2,1\},
\]

and one compatible nonaxial pair \((\rho,\sigma)\) in the accepted finite
dual family.  Put \(k=\rho\sigma>0\),
\(z_*^2=\kappa k\), and \(\Lambda=J/c\).  The parity and gcd restrictions
are imposed before the progression is formed.  The exact odd or even local
unit is then constant on this progression, as established in the assigned
Round-72 seam review.

The analytic antecedent is the conductor-authorized exact-integral addendum
to the Round-71 three-variable integral.  Under the substitutions

\[
 x=Ju,\qquad y=Jv,\qquad \tau=\beta J^2,
 \qquad \tau=(J/c)z,
\]

its phase is

\[
 \Lambda\phi(z,u,v),\qquad
 \phi=z(uv-1)-\rho u-\kappa\sigma v,             \tag{2.1}
\]

and whose sharp faces are

\[
 z_-=-\frac{J}{c+c_-},\qquad
 z_+= \frac{J}{c+c_+}.                           \tag{2.2}
\]

More precisely, after extracting the constant local unit and reciprocal
phase, the normalized coefficient is

\[
 \mathcal W(c)=\Lambda^{1/2}e(-\Lambda\phi_*)\,
 \Lambda\int_{z_-}^{z_+}\iint
 a_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv\,dz.     \tag{2.3}
\]

For a fixed sufficiently large derivative order \(M\), the addendum gives

\[
 \max_{|\alpha|\leq M}\sup_{c,z,u,v}
 |\partial_{z,u,v}^{\alpha}a_c(z,u,v)|
 \ll_\varepsilon X^\varepsilon,                 \tag{2.4}
\]

\[
 \max_{|\alpha|\leq M}\int_C^{2C}\sup_{z,u,v}
 |\partial_c\partial_{z,u,v}^{\alpha}a_c(z,u,v)|\,dc
 \ll_\varepsilon X^\varepsilon.                 \tag{2.5}
\]

The amplitude is compactly supported in the ratio variables, is separated
from \(z=0\) on every stationary piece, and treats both offset-Poisson
aliases in their exact reflected coordinates.  Its only Farey-neighbor
dependence is the sharp interval (2.2).  The phase
\(e(\pm A_{\kappa,b}/c)\), where

\[
 A_{\kappa,b}=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2,
\]

has already been extracted from the coefficient.

Under precisely these hypotheses, (1.1)--(1.2) hold on the entire half-open
residue progression without cutting at neighbor changes.  Here
\(\Gamma_{\epsilon,z_*}\) is the full oriented Gaussian coefficient if
\(-1<z_*<1\), the appropriate oriented half coefficient if
\(z_*=\pm1\), and zero if \(|z_*|>1\).  The sampled variation in (1.1)
includes the two ends of the dyadic progression, and hence also covers a
singleton progression.

For the source interface, write \(c=r+4b\ell\),
\(\alpha=r/(4b)\), and

\[
 K_{\kappa,b}=A_{\kappa,b}/(4b)\asymp X.
\]

The required unweighted estimate is uniform for every interval in the
ambient progression \(\ell+\alpha\asymp T\):

\[
 \sup_I\left|\sum_{\ell\in I}
 e\!\left(\pm\frac{K_{\kappa,b}}{\ell+\alpha}\right)\right|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.       \tag{2.6}
\]

## 3. Proof or derivation

Fix the residue \(r\pmod {4b}\).  Let
\(\alpha_+,\alpha_-\in[0,b)\cap\mathbb Z\) be the fixed residues satisfying

\[
 \alpha_+r\equiv1\pmod b,
 \qquad \alpha_-r\equiv-1\pmod b.               \tag{3.1}
\]

The Farey determinant and order conditions give the exact half-open
inequalities

\[
 \frac{b(R-c)-1}{c}<a_-\leq\frac{bR-1}{c},
 \qquad
 \frac{b(R-c)+1}{c}<a_+\leq\frac{bR+1}{c}.
\]

Each interval has length \(b\), so its unique permitted residue gives

\[
 a_\pm(c)=\alpha_\pm+b\left\lfloor
 \frac{(bR\pm1)/c-\alpha_\pm}{b}\right\rfloor. \tag{3.2}
\]

Together with

\[
 c_-=(a_-c+1)/b,\qquad c_+=(a_+c-1)/b,           \tag{3.3}
\]

this is the exact fixed-residue Farey sawtooth.  Define

\[
 q_\pm(c)=c+c_\pm-R.
\]

Since \(R-c<c_\pm\leq R\), one has the exact integer bounds

\[
 1\leq q_\pm(c)\leq c.                          \tag{3.4}
\]

For the hostile boundary \(z_*=1\), (2.2) and (3.4) give

\[
 Y_+(c)=\sqrt{J/c}\,(z_+-1)
 =\sqrt{J/c}\,\frac{\delta-q_+(c)}{R+q_+(c)},   \tag{3.5}
\]

and therefore

\[
 |Y_+(c)|\leq\sqrt{c/J}\asymp\Lambda^{-1/2}.    \tag{3.6}
\]

The opposite scaled face is instead

\[
 Y_-(c)=\sqrt\Lambda\,(z_--1)
 =-\sqrt\Lambda\left(1+\frac{J}{R+q_-(c)}\right)
 \asymp-\sqrt\Lambda.                           \tag{3.7}
\]

For \(z_*=-1\), the same formulas hold with left and right exchanged.  Thus
the packet's claim that both boundary arguments are
\(O(\Lambda^{-1/2})\) is literally false, but the needed conclusion is
true: for the incomplete Gaussian \(\mathfrak F_\epsilon\),

\[
 \left|\int_0^{Y_+}e(\epsilon t^2/2)\,dt\right|
 \leq |Y_+|\ll\Lambda^{-1/2},                   \tag{3.8}
\]

while (3.7) and the oscillatory-tail estimate give

\[
 \left|\int_{-\infty}^{Y_-}e(\epsilon t^2/2)\,dt\right|
 \ll |Y_-|^{-1}\ll\Lambda^{-1/2}.               \tag{3.9}
\]

Equations (3.8)--(3.9) prove the boundary leading-model error.  Because the
critical family is finite, every nonboundary \(z_*\) is separated from
\(\{-1,1\}\) by a fixed positive amount.  The same tail bound then gives
the full coefficient plus \(O(\Lambda^{-1/2})\) inside and
\(O(\Lambda^{-1/2})\) outside.  This proves the uniform
inside/boundary/outside trichotomy.

The sawtooth itself is sharp.  Put \(c'=c+4b\).  For either sign, if the
selected numerator does not change, then (3.2)--(3.3) give

\[
 q_\pm(c')-q_\pm(c)=4(a_\pm+b).                 \tag{3.10}
\]

At a numerator reset \(a_\pm(c')=a_\pm(c)-b\), they give instead

\[
 q_\pm(c')-q_\pm(c)=4a_\pm-c.                   \tag{3.11}
\]

In the active range \(a_\pm\asymp bJ/C\asymp Q\) and \(C\gg Q\), so
(3.11) is \(-C+O(Q)\).  Across a dyadic \(c\)-block the continuous centre
\(bR/c\) changes by \(\asymp bJ/C\), while the allowed numerator changes
in steps of \(b\).  Hence there are \(\asymp J/C\) resets on a populated
progression.  By (3.5), every right reset in the \(z_*=1\) class has scaled
size \(\asymp\sqrt{C/J}\); the leading transition consequently has the raw
variation capacity

\[
 (J/C)\sqrt{C/J}=\sqrt{J/C}.                    \tag{3.12}
\]

There is no simultaneous-neighbor cancellation.  For \(b>2\), (3.1)
implies \(\alpha_++\alpha_-=b\), and the two threshold lattices
\(\alpha_++b\mathbb Z\) and \(\alpha_-+b\mathbb Z\) are distinct.  Indeed,
equality modulo \(b\) would imply \(2\alpha_+\equiv0\pmod b\); since
\((\alpha_+,b)=1\), this forces \(b\leq2\).  One progression step changes
\((bR\pm1)/c\) by

\[
 O\!\left(\frac{b^2J}{C^2}\right)
 =O(J/T^2)=O(J^{-1/5})<1,                         \tag{3.13}
\]

and the two moving centres differ by only \(2/c\).  Thus, for large \(J\),
one step cannot cross both distinct integer threshold lattices.  The active
range has \(b\asymp C/T\gg J^{1/9}\), so \(b=1,2\) never occurs.  At a
right reset the left face changes only by its smooth increment (3.10),
smaller by \(Q/C\); the local unit and the remaining coefficient factors
are fixed or smooth.  Therefore the complete symbol supplies no exact
left-right switch cancellation of (3.12).

It remains to pass from the leading Gaussian to the complete integral
(2.3), including the first omitted stationary term.  This can be done
without a moving-boundary Morse assertion.  On a fixed stationary
\(z\)-neighborhood, the Hessian in \((u,v)\) is

\[
 \begin{pmatrix}0&z\\z&0\end{pmatrix},
 \qquad \det=-z^2,
\]

and is uniformly nondegenerate because the addendum separates stationary
support from \(z=0\).  Its critical point at fixed \(z\) is

\[
 u_z=\frac{\kappa\sigma}{z},\qquad
 v_z=\frac{\rho}{z},
\]

and the reduced phase is exactly

\[
 \psi(z)=\phi(z,u_z,v_z)=-z-\frac{\kappa k}{z}.  \tag{3.14}
\]

Uniform two-dimensional stationary phase, using (2.4), gives

\[
 \iint a_c e(\Lambda\phi)\,du\,dv
 =\Lambda^{-1}e(\Lambda\psi(z))
 \{A_{0,c}(z)+\Lambda^{-1}A_{1,c}(z)\}
 +O_\varepsilon(X^\varepsilon\Lambda^{-3}),      \tag{3.15}
\]

after taking a fixed sufficiently long expansion.  The same finite
differential operators that produce \(A_{j,c}\) from \(a_c\) preserve the
supremum bounds (2.4) and the integrated \(c\)-seminorm (2.5).  The parts
where the \((u,v)\)-critical point leaves the support are smaller by
integration by parts.  Inserting (3.15) into (2.3) cancels the outer factor
\(\Lambda\).  The first omitted \((u,v)\)-stationary term contributes
\(O_\varepsilon(X^\varepsilon\Lambda^{-1})\) in a stationary
\(z\)-piece, and even its absolute estimate is
\(O_\varepsilon(X^\varepsilon\Lambda^{-1/2})\) after the final
normalization.  Thus it is safely inside the desired remainder.

Now

\[
 \psi'(z)=-1+\frac{\kappa k}{z^2},\qquad
 \psi''(z_*)=-\frac{2}{z_*}\neq0.                \tag{3.16}
\]

A fixed one-dimensional Morse coordinate \(t=t(z)\), independent of the
Farey neighbors, makes
\(\psi(z)-\psi(z_*)=\epsilon t^2/2\).  For the boundary
\(z_*=1\), (3.6) implies
\(t(z_+)=O(\Lambda^{-1})\), so its scaled value is
\(O(\Lambda^{-1/2})\).  Scaling \(s=\sqrt\Lambda t\), expanding the smooth
amplitude once, and integrating the linear term oscillatory gives

\[
 \Lambda^{1/2}\int^{z_+} A_{0,c}(z)
 e(\Lambda(\psi(z)-\psi_*))\,dz
 =\Gamma_{\epsilon,1}V(c)
  +O_\varepsilon(X^\varepsilon\Lambda^{-1/2}).   \tag{3.17}
\]

The endpoint displacement is controlled by the local estimate (3.8); the
fixed remote cutoff is controlled by (3.9).  The first amplitude term is
\(\Lambda^{-1/2}A'_{0,c}(z_*)\int s e(\epsilon s^2/2)ds\), hence has exactly
the permitted size.  This explicitly retains, rather than discards, the
first boundary stationary correction.  The case \(z_*=-1\) is reflected.
For an interior saddle both fixed faces are remote and ordinary stationary
phase gives a smaller error; for an outside saddle, integration by parts in
\(z\) gives \(O(\Lambda^{-1/2})\) after normalization.  The central
nonstationary piece is arbitrarily smaller by the addendum's \(u\)- or
\(v\)-derivative bound.

These estimates are uniform in both aliases, orientations, and all three
\(\kappa\)-classes, and prove

\[
 W_{b,r}(c)=V_{b,r}(c)
 \{\Gamma_{\epsilon,z_*}+O_\varepsilon(
 X^\varepsilon\Lambda^{-1/2})\}
 +O_\varepsilon(X^\varepsilon\Lambda^{-1/2}).    \tag{3.18}
\]

The coefficient \(V_{b,r}\) is the critical value of the complete smooth
amplitude times the stationary Jacobian and the exact constant arithmetic
unit.  It is neighbor-independent.  More importantly, (2.5), rather than
a pointwise derivative slogan, gives the exact global seminorm

\[
 \int_C^{2C}|V'_{b,r}(t)|\,dt
 \ll_\varepsilon X^\varepsilon.                 \tag{3.19}
\]

Indeed, the phase \(\phi\), critical point, Hessian, and fixed Morse map do
not depend on \(c\) once \(\kappa,\rho,\sigma\) are fixed; all \(c\)-variation
of the leading coefficient is inherited from \(A_{0,c}\), and (3.15)
preserves (2.5).  Sampling (3.19) along a monotone half-open progression
therefore gives

\[
 \|V_{b,r}\|_\infty+\operatorname {Var}V_{b,r}
 \ll_\varepsilon X^\varepsilon.                 \tag{3.20}
\]

The exact identity \(X=N+\vartheta\) has already combined the two floor
pieces before this step.  The remaining floor \(R=\lfloor J\rfloor\) occurs
only through \(\delta\) in (3.5); its effect is bounded by (3.6).  Half-open
stars change ownership, not the value of a continuous stationary integral.
Equations (3.18)--(3.20) prove (1.1)--(1.2).

For the source estimate, Bourgain's notation may be matched with ambient
length \(M=T\) and phase parameter

\[
 \mathcal T=K_{\kappa,b}/T\asymp X/T=JQ.
\]

The phase is
\(\mathcal T F((\ell+\alpha)/T)\) with
\(F(x)=(x+O(T^{-1}))^{-1}\); all required derivatives are uniformly of the
reciprocal monomial type.  Moreover

\[
 \frac{\log T}{\log(JQ)}=\frac37
 \in[17/42,1/2],                              \tag{3.21}
\]

so the primary theorem's direct range already applies.  Theorem 6 gives
the exponent pair
\((13/84+\varepsilon,55/84+\varepsilon)\), and Section 5 explicitly
extends it to a proper subinterval by extending the phase and applying
Sargos's partial-sum lemma, at an \(O(\log T)\) cost.  Therefore

\[
 (\mathcal T/T)^{13/84}T^{55/84}
 =Q^{13/42}T^{55/84}
 =TQ^{-5/24},                                    \tag{3.22}
\]

uniformly for every proper subinterval.  Abel summation inserts the global
weight (3.20).  No Farey-piece count is paid.  Summing over
\(O(B)\) residues gives

\[
 |S_{b,k}^{(\kappa),\mathrm{main}}|
 \ll_\varepsilon X^\varepsilon C Q^{-5/24}.     \tag{3.23}
\]

Triangle summation of (1.2) over the \(O(C)\) moduli gives

\[
 |S_{b,k}^{(\kappa),\mathrm{err}}|
 \ll_\varepsilon X^\varepsilon C\sqrt{C/J}.     \tag{3.24}
\]

There are \(O(B)=O(C/T)\) values of \(b\), so

\[
 \sum_{b\asymp C/T}|S_{b,k}^{(\kappa)}|^2
 \ll_\varepsilon X^\varepsilon
 \left\{\frac{C^3}{TQ^{5/12}}+
             \frac{C^4}{TJ}\right\}.           \tag{3.25}
\]

The first term is at most \(J^2/T\) exactly when
\(C\leq J^{13/18}\).  The second is at most \(J^2/T\) for
\(C\leq J^{3/4}\), hence throughout the claimed range.  The separately
accepted axis estimate \(C^2/J\) is also fixed-block safe there because
\(13/18<3/4\).

## 4. First doubtful or unproved step

There is no remaining doubtful step in the scoped transition-flattening
and source interfaces once the boundary sentence is corrected as in
(3.5)--(3.9).  In particular, the large raw variation (3.12) is not a
counterexample to the pointwise estimate (1.2), and no cancellation between
simultaneous neighbors is needed.

The first unproved step is any continuation beyond
\(C=J^{13/18}\).  The main energy in (3.25) then exceeds \(J^2/T\), and
the pointwise transition error ceases to be energy-safe only later, at
\(C=J^{3/4}\).  Nothing in the flattening lemma estimates the residual
signed off-diagonal for \(J^{13/18}<C\leq J\), cone-edge symbols, or the
other radial sectors.  It also does not upgrade a fixed-interior result to
full \(M9\!-!M1\).

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | Pass.  The exact \(d\tau=\Lambda dz\) measure is retained in (2.3); the sequential two- plus one-dimensional scales give the same normalized order one coefficient in (3.18). |
| Farey determinants and half-open endpoints | Pass.  Equations (3.2)--(3.4) follow from the two exact determinant signs and give one-count ownership. |
| \(R=\lfloor J\rfloor\) | Pass.  The exact correction is \(\delta\) in (3.5), and is smaller than the claimed boundary error. |
| Both aliases and orientations | Pass.  The negative alias uses the accepted reflected coordinate; left and right are exchanged for \(z_*=-1\). |
| All \(\kappa\)-classes and local units | Pass.  Fixing \(c\bmod4b\) fixes \(\kappa\), parity, gcd admissibility, and the exact odd/even unit; it is absorbed into \(V\). |
| Finite critical family | Pass.  Finiteness supplies a fixed separation from \(\pm1\) outside the exact boundary cases. |
| Inside/boundary/outside trichotomy | Pass.  Tail estimates handle inside/outside; (3.8)--(3.9) handle the boundary. |
| Complete stationary remainder | Pass.  Equations (3.15)--(3.18) explicitly retain the first omitted \((u,v)\)-stationary term and the first boundary-amplitude term; both are \(O(\Lambda^{-1/2})\) or smaller. |
| Fixed-residue sawtooth | Pass and sharp.  Equations (3.10)--(3.12) give variation capacity \(\sqrt{J/C}\); no global BV is asserted. |
| Simultaneous neighbor switches | Pass.  They are impossible for active \(b>2\) by the distinct threshold lattices and (3.13). |
| Singleton cells/progressions | Pass.  Supremum plus sampled variation and proper-subinterval uniformity include a singleton. |
| Axes | Pass in scope.  They are not inserted into the nonaxial flattening; their accepted \(C^2/J\) bound is safe through \(J^{13/18}\). |
| Bourgain source range | Pass.  The direct parameter ratio is \(3/7\), Theorem 6 supplies the stated exponent pair, and Section 5 explicitly handles proper subintervals with a logarithmic loss. |
| Energy exponents | Pass.  The two terms in (3.25) impose \(C\leq J^{13/18}\) and \(C\leq J^{3/4}\), respectively. |
| Perfect powers | Pass.  The reciprocal derivative conditions do not exclude squares or fourth powers; no Diophantine nonresonance is assumed. |
| Phase-conjugating/adversarial coefficients | Pass as a negative control.  Arbitrary conjugating coefficients need not have (3.20); the theorem uses the actual symbol.  The pointwise error is triangle-summed and needs no cancellation. |
| Floors, stars, cone scope | Pass.  \(X=N+\vartheta\), \(R\), half-open stars, and the fixed-interior exclusion are explicit. |
| Downstream scope | Pass.  No full \(M9\!-!M1\), \(M9\), endpoint-uniformity, or global exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts or sources used

The repository artifacts used were exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet.md`;
5. `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet_actual_integral_addendum.md`;
6. `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/briefs/transition_gluing_hostile_audit.md`;
7. `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/conductor_farey_stationary_low_conductor.md`;
8. `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_third_derivative_seam_review.md`; and
9. `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md`.

No sibling Round-81 report was read.

The primary source checked was Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794),
J. Amer. Math. Soc. 30 (2017), 205--224, arXiv:1408.5794v2,
Theorem 4 and Section 5, especially Theorem 6 and the proper-subinterval
discussion.  The literal pair is
\((13/84+\varepsilon,55/84+\varepsilon)\).  Section 5 requires the usual
exponent-pair derivative class, constructs an extension from a proper
subinterval to the ambient dyadic interval, and then invokes P. Sargos,
Lemma 2.1, with an \(O(\log M)\) partial-sum loss.  The reciprocal phase in
(2.6) satisfies those derivative hypotheses uniformly; the source does not
license replacing the ambient scale \(T\) by a shorter Farey-cell length,
and no such replacement is made here.

## 7. Recommended state effect

Promote the scoped complete-symbol flattening lemma (1.1)--(1.2) and, after
the conductor's independent seam reconciliation, extend the accepted
fixed-smooth-interior Farey range from \(C\leq J^{32/45}\) to

\[
 C\leq J^{13/18}.
\]

Revise the frozen explanatory sentence “at an exact boundary,
\(Y_\pm=O(\Lambda^{-1/2})\)” to say that the adjacent face is
\(O(\Lambda^{-1/2})\), the opposite face is \(\asymp\sqrt\Lambda\), and
the two errors are controlled by (3.8) and (3.9), respectively.

Record as a sharp no-go for the stronger route that the actual boundary
sawtooth has global variation capacity \(\sqrt{J/C}\), with no
simultaneous-neighbor cancellation.  This no-go does not affect the
pointwise-small remainder route.

Do not promote the unresolved range \(J^{13/18}<C\leq J\), cone edges,
full \(M9\!-!M1\), \(M9\), endpoint uniformity, or the Gauss-circle
exponent.

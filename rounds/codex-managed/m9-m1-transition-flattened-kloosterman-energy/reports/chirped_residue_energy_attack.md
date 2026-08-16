## 1. Result

No new conductor interval is proved.  There is, however, an exact
all-class reduction which is strictly smaller than (82.13).

Put \(q=4b\), and split the exact transition-flattened row (82.2) into
its admissible \(q\)-progressions.  For every local class
\(\kappa\in\{1/4,1/2,1\}\), write

\[
 S_{b,k}^{(\kappa)}(C)
 =\sum_{r\in\mathscr R_{\kappa,b}}
 u_{\kappa,b,k}(r)R_{\kappa,b,k}(r),                         \tag{1.1}
\]

where the exact inverse/even local unit \(u(r)\) is constant on the
progression \(c=r+q\ell\), and \(R(r)\) contains the complete globally
BV critical symbol and reciprocal phase.  Bourgain's already audited
reciprocal estimate gives

\[
 |R_{\kappa,b,k}(r)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.                  \tag{1.2}
\]

Consequently the whole same-residue part of the energy, and also every
fixed nonzero residue-offset layer, are bounded by

\[
 X^\varepsilon B^2T^2Q^{-5/12}
 =X^\varepsilon C^2Q^{-5/12}.                               \tag{1.3}
\]

This is below \(X^\varepsilon J^2/T\) for

\[
 C\le J^{47/60},                                             \tag{1.4}
\]

and hence throughout the frozen band \(J^{13/18}<C\le J^{3/4}\).
Thus (82.4) is reduced exactly to the coherent nonzero-offset
actual-unit correlation

\[
 \boxed{
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp B}\ \sum_{\substack{r,s\in\mathscr R_{\kappa,b}\\r\ne s}}
 u(r)\overline{u(s)}R(r)\overline{R(s)}.}                    \tag{1.5}
\]

The required inequality is
\(\mathfrak X_C^{(\kappa,k)}\ll_\varepsilon
X^\varepsilon J^2/T\).  All absolute accumulation over the
\(O(B)\) offsets gives only the already accepted ledger

\[
 |\mathfrak X_C^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon
 {C^3\over TQ^{5/12}}.                                      \tag{1.6}
\]

Its ratio to the target is \(1\) at \(C=J^{13/18}\) and
\(J^{1/12}\) at \(C=J^{3/4}\).  A uniform gain \(B^{-\delta}\)
in the coherent offset sum would prove the nonempty extension

\[
 C\le J^{c_\delta},\qquad
 c_\delta={13/6-3\delta/5\over3-\delta}.                    \tag{1.7}
\]

In particular, square-root cancellation across offsets would reach
\(C\le J^{56/75}\), while \(B^{-5/9}\) closes the whole frozen band.

For the odd class, the discrete Fourier transform of the Kloosterman
product identifies (1.5) with the nonzero product-frequency correlation
in Section 3 below.  Stationary Poisson in that correlation is exactly
involutive when all coefficients and tails are retained: it reconstructs
(1.5), with no missing power or normalization.  Hence it is a rigorous
no-go for counting that transform as a gain.  The strict survivor is
(1.5), not another transformed copy of the full energy.

## 2. Exact statement and hypotheses

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and assume

\[
 J^{13/18}<C\le J^{3/4}.                                    \tag{2.1}
\]

Fix one endpoint orientation, one alias, one compatible nonaxial
\(k=\rho\sigma=O(1)\), and one local class
\(\kappa\in\{1/4,1/2,1\}\).  Use the exact main row (82.2), not a
leading stationary truncation.  Let \(\mathscr R_{\kappa,b}\) be the
admissible residues modulo \(q=4b\), including the exact parity and gcd
conditions, and define

\[
 R_{\kappa,b,k}(r)=
 \sum_{\substack{c\asymp C\\c\equiv r\pmod q}}
 V_{b,c,k}^{(\kappa)}
 e\!\left(\pm {A_{\kappa,b}\over c}\right),                \tag{2.2}
\]

with every smooth cutoff and half-open endpoint convention inherited
from (82.2).  The exact local unit is denoted by
\(u_{\kappa,b,k}(r)\); it is bounded and constant after \(r\pmod q\)
is fixed.  For \(\kappa=1/4\),

\[
 u_{1/4,b,k}(r)=u_{b,k}e_q(k\bar r),\qquad (r,q)=1.          \tag{2.3}
\]

No explicit cusp identification is assumed for the two even units.
Their constancy on the exact \(q\)-progressions is sufficient for
(1.1)--(1.5), and their values remain inside (1.5).

The only analytic input used positively is the accepted global symbol
bound

\[
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V
 \ll_\varepsilon X^\varepsilon                              \tag{2.4}
\]

and Bourgain's audited full-progression/proper-subinterval estimate at
ambient length \(T\).  The pointwise transition remainder and both axes
are not included in (2.2); they retain their separate accepted owners in
(2.1).

Under these hypotheses, the following are proved.

1.  Equations (1.1)--(1.4) hold for all three local classes and both
    aliases.
2.  The exact energy is the sum of the target-safe same-residue part and
    (1.5).
3.  Each fixed \(t=s-r\not\equiv0\pmod q\) layer of (1.5) separately
    satisfies (1.3).  Only coherent accumulation over the \(O(B)\)
    offsets remains.
4.  In the odd class, the nonzero-offset survivor is exactly the
    nonzero Fourier part of a complete Kloosterman-product correlation;
    its stationary Poisson transform has aliases of length \(C\) and is
    an exact self-return.

The report does not assert that the even units are standard odd-cusp
Kloosterman sums, and it does not assert any bound for (1.5).

## 3. Proof or derivation

**Progression bound and the strict energy split.**  Put

\[
 K_{\kappa,b}={A_{\kappa,b}\over q},\qquad
 \alpha={r\over q}.
\]

On \(c=r+q\ell\asymp C\), one has

\[
 {A_{\kappa,b}\over c}
 ={K_{\kappa,b}\over\ell+\alpha},\qquad
 K_{\kappa,b}\asymp X,\qquad \ell+\alpha\asymp T.         \tag{3.1}
\]

Abel summation with (2.4) and the accepted exponent pair gives (1.2).
There are \(O(B)\) admissible residues and \(O(B)\) values of \(b\).
Expanding (1.1) without taking an absolute value prematurely gives

\[
 \sum_{b\asymp B}|S_b|^2
 =\mathfrak D_{\rm res}+\mathfrak X_C^{(\kappa,k)},          \tag{3.2}
\]

\[
 \mathfrak D_{\rm res}
 =\sum_{b\asymp B}\sum_{r\in\mathscr R_{\kappa,b}}|R(r)|^2
 \ll_\varepsilon X^\varepsilon B^2T^2Q^{-5/12}.            \tag{3.3}
\]

The units cancel exactly in (3.3).  The same calculation, with at most
one partner \(s=r+t\) for each \(r\), gives (1.3) for any fixed residue
offset \(t\).  Since \(J^2/T=JQ\), (3.3) is target-safe when

\[
 C^2Q^{-5/12}\le JQ,
\]

which is precisely (1.4).  Summing (1.3) absolutely over \(O(B)\)
offsets gives (1.6), and no factor has been suppressed.

If a future signed theorem saves \(B^\delta\) over (1.6), then

\[
 C^3B^{-\delta}\le J^2Q^{5/12}.
\]

Substituting \(B=C/J^{3/5}\) proves (1.7).  At the upper endpoint,
\(B=J^{3/20}\), and the loss \(J^{1/12}\) equals \(B^{5/9}\).

**Exact odd Kloosterman-product correlation.**  Use

\[
 S(n,k;q)=\sum_{x\bmod q}^{*}e_q(nx+k\bar x).
\]

For \(d\in\mathbb Z\), define the normalized Fourier coefficient

\[
 \mathcal C_q(d,t)
 ={1\over q}\sum_{r\bmod q}
 S(r+d,k;q)\overline{S(r,k;q)}e_q(-tr).                     \tag{3.4}
\]

Orthogonality in \(r\) gives the exact rational complete sum

\[
 \mathcal C_q(d,t)=
 \sum_{\substack{y\bmod q\\(y(y+t),q)=1}}
 e_q\!\left(d(y+t)+k(\overline{y+t}-\bar y)\right).         \tag{3.5}
\]

In particular,

\[
 \mathcal C_q(d,0)=c_q(d).                                  \tag{3.6}
\]

Fourier inversion is

\[
 S(n+d,k;q)\overline{S(n,k;q)}
 =\sum_{t\bmod q}\mathcal C_q(d,t)e_q(tn).                 \tag{3.7}
\]

The term \(t=0\), with all of its Poisson aliases retained, is exactly
the same-residue term \(x=y\) in the expanded Kloosterman sums.  It is
therefore the already bounded quantity (3.3), not merely the literal
\(n_1=n_2\) diagonal.  The terms \(t\ne0\) are exactly \(x\ne y\), hence
are the odd realization of (1.5).  This proves that the new survivor is
strictly smaller than (82.13): the entire Ramanujan/same-residue mode has
been removed.  Every remaining fixed-offset slice is separately certified
target-safe; only their coherent signed accumulation remains.

**Stationary Poisson and exact self-return.**  For the leading odd
stationary coefficient, put \(N=Q^2\),

\[
 a_{b,n}=w_{b,n}e(-D_b\sqrt n),\qquad
 D_b=J+{\sqrt k\over2b},\qquad
 |w_{b,n}|\ll_\varepsilon X^\varepsilon\sqrt{T/N}.          \tag{3.8}
\]

Applying Poisson in \(n\) after (3.7) gives integrals

\[
 I_b(d,h)=\int w_{b,x+d}\overline{w_{b,x}}
 e\!\left(-D_b(\sqrt{x+d}-\sqrt x)-{hx\over q}\right)dx,
 \qquad h\equiv-t\pmod q.                                  \tag{3.9}
\]

For \(d>0\), the stationary equation is

\[
 h={qD_bd\over
 2\sqrt x\sqrt{x+d}(\sqrt x+\sqrt{x+d})},                  \tag{3.10}
\]

and the signs are reversed together for \(d<0\).  Hence

\[
 hd>0,\qquad
 |h|\asymp {BJ|d|\over Q^3}
 ={B|d|\over J^{1/5}},\qquad 1\le |h|\ll C.                \tag{3.11}
\]

At a nondegenerate saddle,

\[
 |I_b(d,h)|
 \ll_\varepsilon X^\varepsilon {T\over N}
 \sqrt{J\over|d|}.                                         \tag{3.12}
\]

These formulas expose a length-\(C\) alias family; they do not bound it.
Even a termwise square-root estimate for the nondegenerate complete sum
(3.5), followed by absolute values in \(d,h,b\), has capacity

\[
 B\sum_{1\le |d|\ll N}
 B^{1/2}\left(1+{B|d|\over J^{1/5}}\right)
 {T\over N}\sqrt{J\over|d|}
 \ll_\varepsilon
 X^\varepsilon B^{5/2}J^{13/10},                            \tag{3.13}
\]

whose ratio to \(J^{7/5}\) is \(B^{5/2}J^{-1/10}\).  It loses
\(J^{37/180}\) at \(C=J^{13/18}\) and \(J^{11/40}\) at
\(C=J^{3/4}\), worse than the ordinary large-sieve ledger.  Thus
termwise Weil plus stationary phase is not the missing mechanism.

More decisively, let

\[
 F_b(x)=W_b(x)e(-A_{1/4,b}/x),\qquad
 I_{b,n}=\int F_b(x)e(-nx/q)dx.
\]

Full Poisson summation gives, with exact constants,

\[
 {1\over q}\sum_n S(n,k;q)I_{b,n}
 =\sum_{r\bmod q}^{*}e_q(k\bar r)
   \sum_{\ell\in\mathbb Z}F_b(r+q\ell),                    \tag{3.14}
\]

because

\[
 \sum_n I_{b,n}e_q(nr)=q\sum_{\ell\in\mathbb Z}F_b(r+q\ell).
\]

Squaring (3.14) shows that \(t=0\) returns to \(r=s\) and
\(t\ne0\) returns to \(r\ne s\), with the factors \(q^{-2}\) cancelled
by the two Poisson factors \(q\).  All stationary lower terms,
nonstationary tails, and moving supports are required to recover
(3.14).  Therefore a leading-term stationary transform cannot be counted
as a second saving: its completion is exactly (1.1)--(1.5).

**Dispersion and spectral diagnostics.**  In (82.13), the extra
\(b\)-phase for \(d=n_1-n_2\) varies across \(b\asymp B\) by only

\[
 \asymp {|d|\over BQ}.                                      \tag{3.15}
\]

Thus the whole strip \(|d|\ll BQ\) has no forced \(b\)-oscillation.
Moreover the energy is a positive sum over moduli; dualizing its
\(\ell^2_b\) norm introduces arbitrary coefficients in \(b\), so smooth
\(b\)-dispersion cannot be assumed.  The arithmetic product (3.5) and
the actual symbol must supply any gain.

The phase-matched Kuznetsov diagnostic has spectral width
\(t_f^2\ll R=J/C\), namely \(R=J^{5/18}\) at the lower endpoint and
\(R=J^{1/4}\) at the upper endpoint.  Exact level-four Voronoi switching
has finitely many conductor-dependent centers

\[
 m={LX\over4}+O(T),\qquad L=[1,M_f,N_f]\in\{1,2,4\},        \tag{3.16}
\]

so the centers can be \(X/4\), \(X/2\), or \(X\).  The window length is
always \(T\), and the optimistic length bound still misses the required
short-coefficient scale by \(J^{1/10}=X^{1/20}\).  Changing the local
center does not change that capacity.  Applying the inverse trace and
Voronoi transformations returns to (1.5), so this is another exact
self-return unless a new signed short-coefficient inequality is supplied.

## 4. First doubtful or unproved step

The first genuinely unproved inequality is cancellation across the
nonzero residue offsets in (1.5).  Bourgain controls each progression and
therefore each fixed offset, but it supplies no correlation between the
\(O(B)\) offsets.  The inverse/even local unit is exactly the coefficient
that could create such cancellation and cannot be replaced by an
arbitrary bounded sequence.

Indeed, after retaining only the separate bounds \(|R(r)|\le H\), the
abstract phase-conjugating choice \(R(r)=H\overline{u(r)}\) makes the
cross sum have full \(B^2H^2\) capacity for one \(b\).  This is not
claimed to be realizable by the actual globally smooth symbol; it proves
that any argument which forgets the dependence of \(R(r)\) on the
reciprocal phase is coefficient-blind and cannot yield the required
offset saving.

In the odd transformed language, the same first seam is a joint bound for
(3.5) against the chirped correlation (3.9), summed over
\(b,d,h\), without absolute values.  A complete-sum square-root estimate
alone fails by (3.13), while full stationary Poisson is involutive by
(3.14).  For the even classes an exact generalized Kloosterman/cusp
identification would be an earlier seam for any spectral proof, although
it is not needed for the all-class residue reduction (1.1)--(1.5).

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | **Pass.** The target is \(J^2/T=J^{7/5}\), \(B=C/T\), and every displayed energy includes the \(O(B)\) moduli. |
| Odd inverse local unit | **Pass.** It is retained as \(e_q(k\bar r)\) in (2.3), (1.5), and the exact complete sum (3.5). |
| Even cusp classes | **Pass for the reduction; open spectrally.** Their exact progression units remain in (1.5). No odd-cusp formula is inferred by a sign change. |
| Transition flattening scope | **Pass.** Only the globally BV principal symbol enters (2.2). The pointwise transition error remains separately owned. |
| Stationary \(n\)-range | **Pass.** The leading odd range is \(n\asymp Q^2\); product Poisson gives (3.10)--(3.11), with aliases through \(C\). |
| Complete stationary errors | **Pass by avoidance.** The promoted reduction is made in the exact original row before stationary expansion. Equation (3.14) shows that every lower term and tail is needed for transform equality; none is discarded to claim a gain. |
| Energy diagonal | **Pass and strengthened.** The entire same-residue mode, not just \(n_1=n_2\), is safe through \(C\le J^{47/60}\). |
| Ordinary large-sieve capacity | **Pass.** Its ratio to target is \(B\): \(J^{11/90}\) and \(J^{3/20}\) at the two endpoints. No such factor is hidden. |
| Phase-sensitive off-diagonal | **Open, strictly reduced.** The survivor is (1.5), equivalently the \(t\ne0\) part of (3.5). Each fixed \(t\) layer is already safe. |
| Endpoint power ledger | **Pass.** The Bourgain triangle ratio is \(1\) at \(J^{13/18}\) and \(J^{1/12}\) at \(J^{3/4}\). A \(B^{-1/2}\) gain reaches \(J^{56/75}\); \(B^{-5/9}\) closes the band. |
| Short-Hecke self-return | **Pass.** Exact constants are checked in (3.14). The conductor-dependent Voronoi centers are \(LX/4+O(T)\), \(L\in\{1,2,4\}\), and the deficit remains \(J^{1/10}\). |
| Gcd and zero modes | **Pass in scope.** Admissible stars and gcd restrictions are retained in \(\mathscr R\) and (3.5). The Ramanujan mode (3.6) is part of the proved same-residue estimate. Axes/zero indices remain separately owned. |
| Perfect-power control | **Pass as a no-counterexample check.** A \(T\)-window about any center in (3.16) contains only \(O(1)\) exact square centers; fourth powers are sparser. They neither prove cancellation nor force the missing offset mass. |
| Phase-conjugating control | **Fail for coefficient-blind methods, as required.** Arbitrary bounded residue coefficients can conjugate the local unit. Therefore the actual reciprocal dependence must be used. |
| Downstream scope | **Pass.** No cone edge, other radial sector, full \(M9\!-\!M1\), \(M9\), or circle exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only the selected context was used:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `strategy/conductor_0816_full_proof_strategy.md`;
* `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/derivation_packet.md`;
* `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reviews/conductor_round81_adjudication.md`;
* `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_residue_energy_attack.md`;
* `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md`;
* `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/briefs/chirped_residue_energy_attack.md`.

No sibling Round-82 report was read.  No web source was used.  Bourgain,
Kuznetsov, level-four Voronoi, and spectral-large-sieve facts are used
only through the assigned audited artifacts.  The progression split,
energy arithmetic, Kloosterman-product Fourier identity, Poisson constants,
stationary equations, and endpoint exponents are derived in this report.

## 7. Recommended state effect

Promote no new conductor range and keep (82.4), full \(M9\!-\!M1\),
\(M9\), and the global exponent open.

Promote, if the conductor's independent reviews agree, the scoped
all-class reduction that the complete same-residue energy and every fixed
nonzero residue-offset layer are target-safe throughout (82.1), in fact
through \(C\le J^{47/60}\).  Replace the first-band main survivor by the
coherent nonzero-offset actual-unit correlation (1.5).

Record the odd identity (3.4)--(3.7) as its exact Kloosterman-product
form and record (3.14) as a no-go: stationary Poisson or a matched
Kuznetsov--Voronoi chain is not a gain without a new signed inequality.
The next analytic target should be an offset-dispersion estimate

\[
 |\mathfrak X_C^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon
 B^{-\delta}{C^3\over TQ^{5/12}}                            \tag{7.1}
\]

with the exact local units and reciprocal symbols retained.  Any fixed
\(\delta>0\) gives a nonempty extension by (1.7),
\(\delta=1/2\) reaches \(56/75\), and \(\delta=5/9\) closes the frozen
band.  Do not replace (7.1) by an arbitrary-coefficient statement and do
not infer the two even spectral transforms from the odd one.

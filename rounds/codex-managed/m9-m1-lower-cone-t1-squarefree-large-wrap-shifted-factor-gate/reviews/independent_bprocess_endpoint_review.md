# Round 151 independent reciprocal \(B\)-process and endpoint review

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Reviewed artifact: `reports/blind_d1_reciprocal_bprocess_feasibility.md`
- Role: independent reciprocal-transform and endpoint seam reviewer
- Starting graph SHA-256: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Terminal verdict: **RED as written; the interior transform kernel is GREEN after the exact repairs below**

## 1. Result

The blind report gets the central algebra right.  The identity for
\(\chi _4\), the two stationary residue classes, the positive
square-root phase, the leading amplitude, the Gaussian unit, and the
all-\(M\) capacity ledger are all correct.  In particular, for the actual
\(D=d=L=1\) retained profile

\[
 w_U(q)=\mathscr A_{1,M,U}\!\left(1,\frac{4N}{q^2}\right)
\]

the interior main term is

\[
 e(-1/8)N^{1/4}
 \sum_{\substack{\ell>0\\ \ell\ \mathrm{odd}}}
 \chi _4(\ell)\ell^{-3/4}\mathscr A_{1,M,U}(1,\ell)
 e(\sqrt{N\ell}).
\tag{R151.B1}
\]

This is exactly the blind constant because
\(e(1/8)/i=e(-1/8)\).  The principal stationary-phase map also
self-returns: applying its dual stationary map to
\(2\sqrt{N(m+\sigma/4)}\) recovers \(N/q+\sigma q/4\), the two
principal curvature amplitudes multiply to one, and the Maslov units
cancel.

The report is nevertheless **RED as a promotion-ready artifact** for two
reasons.  First, its claimed first obstruction, namely the absence of an
actual-profile derivative, jump, endpoint, and prefix ledger, disappears
once the authorized Round-148 actual-profile source is read.  That source
constructs a compact smooth amplitude after pricing the hard radial,
terminal-prefix, and cone collars, and it proves the required derivative,
transition-support, middle-buffer, and tail bounds.  Second, the report
calls the full \(B\)-process "exactly involutive" although its calculation
only composes the principal stationary symbols.  The lower symbols,
nonstationary integrals, and endpoint transitions were retained but were
not shown to compose exactly.

After those statements are repaired, the correct conclusion is a rigorous
method-specific no-gain result: the boundary-complete transform is
available for the actual profile, but its main term is a square-root wave
of absolute capacity \(RM^{1/4}\).  A second principal \(B\)-process
returns the reciprocal wave.  No growing intermediate \(M\)-range follows
without a separate signed square-root-wave estimate.

## 2. Exact statement and hypotheses

Let

\[
 N=\lfloor X\rfloor,\qquad R=X^{1/4},\qquad E\asymp M,
 \qquad Q=2\sqrt{N/E}\asymp R^2M^{-1/2},
\tag{R151.B2}
\]

and specialize to \(D=d=L=1\).  Put

\[
 S_U:=\sum_{q>0}\chi _4(q)w_U(q)e(N/q),
 \qquad
 \widetilde S_U:=B_{1,U}(1)S_U.
\tag{R151.B3}
\]

The exact literal \(L=1\) row component is \(\widetilde S_U\), not
\(S_U\) alone.  The accepted coefficient norm gives
\(|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon\).

The actual profile hypotheses are not conjectural.  Round 148 first peels
the hard product-prefix collars of product width \(O(\sqrt M)\) and, when
present, the cone collar.  A prefix shorter than its collar already has a
primal owner.  On the retained part it constructs a compact smooth
\(\mathscr A_{D,E,U}\), exact at every retained lattice point, with

\[
 \|H^{(j)}\|_\infty
 \ll_j 1+M^{j/2}{\bf1}_{\rm rad}
       +D^{j/2}{\bf1}_{\rm cone},\qquad 0\le j\le12,
\tag{R151.B4}
\]

where a radial or long-prefix transition occupies an
\(O(M^{-1/2})\) fraction of support and a cone transition occupies an
\(O(D^{-1/2})\) fraction and occurs only when \(M\asymp D^2\).  The
middle stationary buffer and all nonstationary tails are included in the
accepted Round-148 error majorant.

Writing \(q=Qy\), the support of \(y\) is fixed and
\(4N/q^2\asymp M\).  Equation (R151.B4) therefore gives, uniformly for
all \(1\le M\le R^2\),

\[
 \|w_U\|_\infty+\operatorname {Var}_{q\asymp Q}w_U
 \ll_\varepsilon X^\varepsilon.
\tag{R151.B5}
\]

Indeed the radial contribution to variation is
\(O(M^{1/2}M^{-1/2})\), and the cone contribution is
\(O(D^{1/2}D^{-1/2})\); at \(D=1\) the latter is harmless and occurs
only at bounded \(M\).  Thus the literal application has no
uncontrolled jump at every sampled integer.  The prefix in
\(B_{1,U}(1)\) is a scalar, while every retained long-prefix transition
inside \(w_U\) is smooth.

Define the physical square-root component

\[
 P_U:=\sum_{\substack{\ell>0\\ \ell\ \mathrm{odd}}}
 \chi _4(\ell)\ell^{-3/4}\mathscr A_{1,M,U}(1,\ell)
 e(\sqrt{N\ell}).
\tag{R151.B6}
\]

The per-progression specialization of the accepted boundary-complete
Round-148 transform gives

\[
 P_U=e(1/8)N^{-1/4}S_U+O_\varepsilon(X^\varepsilon).
\tag{R151.B7}
\]

Consequently

\[
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon).
\tag{R151.B8}
\]

This is the source-complete version of the blind main term.  Its error is
already row-target-sized.  Equation (R151.B8) does not estimate the main
square-root wave.

## 3. Proof and derivation

For every integer \(q\),

\[
 \chi _4(q)=\frac{e(q/4)-e(-q/4)}{2i}.
\tag{R151.B9}
\]

Extend the compact positive-support weight by zero in a neighborhood of
\(( -\infty,0]\), so no value of \(N/q\) at \(q=0\) is required.  Then

\[
 S_U=\frac{T_+-T_-}{2i},\qquad
 T_\sigma=\sum_{q\in\mathbb Z}w_U(q)
 e\!\left(\frac Nq+\frac{\sigma q}{4}\right).
\tag{R151.B10}
\]

After Poisson summation, the phase at frequency \(n\in\mathbb Z\) is

\[
 F_{\sigma,n}(x)=\frac Nx+\left(\frac\sigma4-n\right)x.
\]

A stationary point exists precisely when
\(\lambda=\sigma/4-n>0\).  Put
\(\ell=\sigma-4n=4\lambda\).  Then

\[
 x_{\sigma,n}=2\sqrt{N/\ell},\qquad
 F_{\sigma,n}(x_{\sigma,n})=\sqrt{N\ell},
\tag{R151.B11}
\]

and

\[
 F_{\sigma,n}''(x_{\sigma,n})^{-1/2}
 =2N^{1/4}\ell^{-3/4},\qquad
 \frac{4N}{x_{\sigma,n}^2}=\ell.
\tag{R151.B12}
\]

For \(\sigma=1\), the positive frequencies are
\(\ell\equiv1\pmod4\); for \(\sigma=-1\), they are
\(\ell\equiv-1\pmod4\).  Positive curvature contributes \(e(1/8)\).
Combining the two branches with \(1/(2i)\) gives (R151.B1), including
its sign, amplitude, character, and exact sampling point.  No parity or
coprimality condition on \(N\) was used.

The blind Fejer formula is a valid formal identity for an arbitrarily
supplied piecewise continuation: the correction at an integral jump
changes the Fourier-series average to the literal lattice value, and a
stationary point near an endpoint has a truncated Fresnel factor.  It is
normalized correctly: with
\(\Delta=F_{\sigma,n}''(x_{\sigma,n})^{-1/2}\), the quadratic integral
is \(\int e(t^2/2)\,dt\), whose full value is \(e(1/8)\) and whose value
at one exact endpoint is \(e(1/8)/2\).  A saddle just outside a piece is
rightly retained among the nonstationary endpoint integrals rather than
silently discarded.  This formal construction is
not, however, the source obstruction for the actual application.  The
actual retained amplitude is compact smooth; its zero extension is smooth
because support is separated from zero.  Hence there are no literal jump
corrections.  If one artificially partitions the smooth transition, the
two one-sided contributions cancel at the artificial boundary.  The
accepted Round-148 stationary buffer, derivative ledger, and sixfold tail
integration provide (R151.B7), including support-edge transitions and
lower symbols.

For the principal self-return, let \(m=-n\) and
\(\lambda=m+\sigma/4\).  The first principal amplitude in the unit-spaced
\(m\)-variable is

\[
 a_1(m)=\frac{N^{1/4}}{\sqrt2}\lambda^{-3/4},
 \qquad g_\sigma(m)=2\sqrt{N\lambda}.
\tag{R151.B13}
\]

At second Poisson frequency \(p>0\),

\[
 m_p=\frac N{p^2}-\frac\sigma4,qquad
 g_\sigma(m_p)-pm_p=\frac Np+\frac{\sigma p}{4}.
\tag{R151.B14}
\]

Moreover,

\[
 |g_\sigma''(m_p)|^{-1/2}
 =\sqrt2N^{-1/4}\lambda^{3/4},
\tag{R151.B15}
\]

so the two principal amplitudes multiply to one.  The second curvature is
negative and contributes \(e(-1/8)\), cancelling the first unit.  This
proves exact self-return of the phase and principal symbol.  It does not
prove exact composition of every lower symbol, tail integral, and Fresnel
transition; those terms must remain in the boundary error ledger.

Finally, the direct and dual absolute capacities are

\[
 Q\asymp R^2M^{-1/2},\qquad
 M\cdot N^{1/4}M^{-3/4}\asymp RM^{1/4}.
\tag{R151.B16}
\]

Thus the best elementary row capacity is

\[
 \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon.
\tag{R151.B17}
\]

The two terms cross at \(M\asymp R^{4/3}\).  The dual absolute bound is
row-target-sized only for bounded \(M\), and the direct count is
row-target-sized only at the top scale \(M\asymp R^2\).  Every growing
intermediate scale remains open.  A curvature estimate on the dual
square-root wave returns the original-side scale, consistently with
(R151.B14)--(R151.B15); it is not an independent saving.

For scope, every centered nonexact \(D=1,L_1=L_2=1\) pair lies in the
collar because \(|\rho|\le hr_1r_2/2\).  The exact literal pair component
is
\(\widetilde S_U\overline{\widetilde S_V}\).  A uniform
\(|\widetilde S_U|\ll RX^\varepsilon\), followed by subtraction of the
accepted exact-phase and selected-packet owners, would control the
large-wrap remainder in this single \(L_1=L_2=1\) component.  It would
not control any \(L_i>1\) component or the full all-\(L\) row.

## 4. First doubtful or unproved step

After the actual Round-148 profile source is inserted, the first unproved
step is no longer construction of a continuum profile.  It is the signed
estimate

\[
 \left|
 \sum_{\substack{\ell\asymp M\\ \ell\ \mathrm{odd}}}
 \chi _4(\ell)\ell^{-3/4}\mathscr A_{1,M,U}(1,\ell)
 e(\sqrt{N\ell})
 \right|
 \ll_\varepsilon X^\varepsilon,
\tag{R151.B18}
\]

or an equivalent pair estimate.  For a unit-scale profile, (R151.B18)
requires an unweighted square-root-wave bound of size
\(M^{3/4}X^\varepsilon\), a factor \(M^{1/4}\) beyond absolute
summation.  Neither one nor two reciprocal \(B\)-processes prove it.

The first defect inside the blind derivation itself is the promotion-scope
sentence that records the absent profile ledger as a source obstruction.
That sentence was valid only relative to the intentionally statement-only
packet; it is false as a statement about the full authorized Round-151
evidence.  The next defect is the word "exact" when applied to composition
of the entire asymptotic transform rather than its phase and principal
symbol.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact character Fourier split | **GREEN.** (R151.B9) holds on both odd classes and kills even integers; define the positive-support extension before writing the value at zero. |
| stationary congruences and signs | **GREEN.** The plus branch gives \(\ell\equiv1\pmod4\), the minus branch gives \(\ell\equiv-1\pmod4\), and their difference is exactly \(\chi _4(\ell)\). |
| phase, amplitude, and constant | **GREEN.** (R151.B11)--(R151.B12) give \(\sqrt{N\ell}\), \(2N^{1/4}\ell^{-3/4}\), and the combined unit \(e(-1/8)\). |
| literal Fejer and endpoint treatment | **GREEN only as a formal generic identity; RED as the claimed actual-profile obstruction.** The actual amplitude is compact smooth after owned collar peels, so its jump correction is zero and Round 148 already prices the transition buffer and tails. |
| actual-profile derivative and jump sufficiency | **GREEN after source insertion.** (R151.B4)--(R151.B5) give uniform variation; the higher localized derivative ledger and accepted error majorant give (R151.B7)--(R151.B8). |
| principal second transform | **GREEN with wording repair.** Phase, leading amplitude, and Maslov units self-return exactly.  Exact composition of all lower and endpoint terms is not established. |
| bounded, intermediate, and top \(M\) | **GREEN as a capacity audit.** Bounded \(M\) is dual-absolute target-sized, top \(M\asymp R^2\) is direct-count target-sized, and (R151.B17) loses at every growing intermediate scale. |
| coefficient and literal pair | **REPAIR REQUIRED.** Replace the report's bare pair \(S_U\overline{S_V}\) by \(\widetilde S_U\overline{\widetilde S_V}\), with both exact \(B_{1,U}(1)\) coefficients retained. |
| collar and packet scope | **GREEN after precision repair.** At \(D=1,L_1=L_2=1\) all centered nonexact pairs are collar pairs; the claim is only for that component, not the full all-\(L\) row or \(D>1\). |
| raw, absolute, and signed separation | **GREEN.** Dual length \(M\), absolute capacity \(RM^{1/4}\), direct length \(Q\), and the signed target (R151.B18) remain distinct. |
| parity, common factors, and imprimitive denominators | **GREEN in the assigned endpoint.** No parity of \(N\) is used; common odd gcd \(h\), denominators dividing \(N\), and the centered wrap phase are retained. |
| downstream scope | **GREEN.** Nothing here controls \(D>1\), \(L_i>1\), the full growing-scale collar, the generic complement, any \(t\ge2\) layer, the cross owner, M1, M2, M9, the bridge, or an exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used only the governing protocol, the active Round-151
statement, the reviewed blind report, and the minimum exact-row and
actual-profile evidence needed to open its source seam:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reports/blind_d1_reciprocal_bprocess_feasibility.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`, for the accepted explicit profile and derivative ledger cited by the Round-148 candidate;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`; and
8. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/independent_conductor_round150_math_review.md`, only for the accepted exact-row and profile ownership boundary.

No sibling Round-151 report, web source, or computation was used.

## 7. Recommended state effect

**Recommended effect: revise; do not promote the blind report as written.**

The exact required repairs are:

1. replace the claimed missing actual-profile source obstruction by
   (R151.B4)--(R151.B8), while retaining the square-root-wave estimate
   (R151.B18) as the first genuine open step;
2. replace "the transform is exactly involutive" by "the phase and
   principal stationary symbol self-return exactly; lower symbols,
   endpoint transitions, and remainders remain in the accepted boundary
   ledger";
3. distinguish the generic Fejer/Fresnel formalism from the actual compact
   smooth application, for which there is no literal jump correction and
   no every-integer prefix discontinuity;
4. include \(B_{1,U}(1)\) in the literal row and pair components; and
5. scope the subtraction implication to \(D=d=1,L_1=L_2=1\), not to a
   full all-\(L\) row.

After those repairs, promote only the exact character split, dual phase,
amplitude and constant, the source-complete boundary transform, the
principal-symbol self-return, and the all-\(M\) no-gain ledger.  Retain the
growing intermediate \(D=1,L_1=L_2=1\) signed estimate and every broader
collar or downstream obligation as open.

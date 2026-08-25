# Round 132 conductor adjudication: exact hyperbolic chart, direct-source no-go

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

Starting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`.

Role: conductor, post-source and post-unmask adjudicator.

## 1. Result

The terminal label is

\[
\boxed{\texttt{source\_level\_no\_go}}.
\]

Three statements survive the source, blind, discovery, and seam reviews.

1. The top-shell ratio graph has an exact affine hyperbolic-paraboloid
   chart.  This is a proved geometric lemma, not merely a nonzero-Hessian
   analogy.
2. Demeter--Wu v2 supplies genuine bilinear and refined bilinear decoupling
   only for already-constructed functions on patches separated in both
   surface coordinates.  Its narrow mechanism retains ruling rectangles in
   positive norms.
3. Those theorems do not directly estimate the literal Round-131 scalar.
   After determinant-band zooming, a geometrically transverse broad stratum
   still lacks an owner-preserving projective factorization of the joint
   arithmetic coefficient.  The exact ruling part lacks a signed arithmetic
   estimate.  A generic fixed-point sampling lemma is available only after
   factorization and leaves positive cap norms, not a negative power.

Consequently the complete accepted fixed-block bound remains
\(Y^{35/48+\varepsilon}\).  The one-term-per-ray persistence floor remains
\(Y^{27/48+\varepsilon}\), and the determinant target remains
\(Y^{24/48+\varepsilon}\).  No global exponent or M9 status changes.

## 2. Exact retained statement and hypotheses

For a primitive top-shell ray \(r=(a,b)\), with \(|a|\asymp L\),
\(b\asymp D\), define

\[
 \xi_r={b\over D},\qquad
 \eta_r=-{Da\over Lb},\qquad
 \zeta_r=-{a\over L}.
 \tag{132.A1}
\]

Then

\[
 \zeta_r=\xi_r\eta_r,                                    \tag{132.A2}
\]

exactly.  Thus the ratio graph is affinely equivalent to
\(\mathbb H=\{(\xi,\eta,\xi\eta)\}\).

Put

\[
 P_i={cL\over\kappa_iD},\qquad \kappa_1=1,\quad\kappa_2=4.
 \tag{132.A3}
\]

For \(r'=(a',b')\) and \(n=ab'-a'b>0\),

\[
 {ca\over\kappa_i b}-{ca'\over\kappa_i b'}
 =P_i(\eta_{r'}-\eta_r),
 \qquad
 \eta_{r'}-\eta_r={Dn\over Lbb'}.                        \tag{132.A4}
\]

Hence \(P_i\asymp Y^{32/48}\), while the literal determinant taper gives

\[
 0<\eta_{r'}-\eta_r\lesssim
 h_*={\kappa_iD\over WL}=Y^{-5/48+o(1)}.                 \tag{132.A5}
\]

On a dyadic band \(h<\eta_{r'}-\eta_r\le2h\), a legal exact recentered
surface chart is

\[
 X=\xi-\xi_0,\qquad H={\eta-\eta_0\over h},\qquad
 Z={\zeta-\eta_0\xi-\xi_0\eta+\xi_0\eta_0\over h}.
 \tag{132.A6}
\]

Equation (132.A2) gives \(Z=XH\).  The reciprocal phase is evaluated at
dual size

\[
 R_h=P_i h;                                                \tag{132.A7}
\]

at the widest band this is

\[
 R_{h_*}=P_ih_*={c\over W}=Y^{27/48+o(1)}.                \tag{132.A8}
\]

Equations (132.A7)--(132.A8) are physical dual-coordinate identities.  They
do **not** by themselves identify \(R_h\) with the source radius.  That
requires a Fourier thickening, a Euclidean-neighborhood transport, cap and
ball normalization, a Jacobian ledger, and coefficient realization.

After the band zoom and sufficiently small patch subdivision, source
transversality requires both

\[
 {|b-b'|\over D}\asymp1,
 \qquad
 {Wn\over\kappa_i bb'}\asymp1                             \tag{132.A9}
\]

at the widest band, with the analogous normalized determinant condition on
other bands.  Definition 1.2 requires these separations for every point in
the two selected patches.  Same-denominator pairs have \(b=b'\), hence
\(X=X'\), and remain exact rulings under every \(\eta\)-zoom.

The source audit retains Demeter--Wu Definitions 1.2, 1.3, and 1.9 and
Theorems 1.6 and 1.10 only with their literal support, transversality,
localization, packet-incidence, and positive-norm hypotheses.  Linear
Theorem 2.4 and pointwise Proposition 4.11 retain horizontal and vertical
ruling pieces; they do not turn those pieces into bilinear transverse ones.

## 3. Proof and seam reconciliation

Equations (132.A1)--(132.A5) follow by direct multiplication and the exact
determinant identity.  For (132.A6),

\[
 \zeta-\eta_0\xi-\xi_0\eta+\xi_0\eta_0
 = (\xi-\xi_0)(\eta-\eta_0)=hXH,
\]

so the recentered map is an exact automorphism of the hyperbolic graph.  It
repairs the conductor candidate's unrecentered dilation: the actual shell
has \(|\eta|\asymp1\), so one must first localize absolute \(\eta\) to
width \(h\) and then apply (132.A6).  The resulting \(O(h^{-1})\) strip
family is not free; any future source application must reassemble it without
changing the scalar or owners.

The whole-shell physical scale \(P_i\) and band scale \(R_h=P_ih\) are not
contradictory.  The former belongs to the bounded whole-shell chart; the
latter is the dual size after a condition-number \(h^{-1}\) zoom.  The
discovery phrase “exact source scale \(c/W\)” is therefore revised to
“exact widest-band reciprocal evaluation scale.”

The sign/same-point seam is not an independent obstruction after a
coefficient factorization.  If \(F_1,F_2\) are the two extension functions,
then the target phase is represented by \(F_1(x)\overline{F_2(x)}\) at one
point \(x\), and
\(|F_1\overline{F_2}|=|F_1F_2|\).  The real obstruction occurs earlier:
the literal coefficient

\[
 B_i(r,r')=A_i(r)H_{i;r,p}(n)C_{i;r,p}(n)                \tag{132.A10}
\]

depends jointly on the two rays through the lift selector, primitive
moduli, Stieltjes/Mobius profiles, thresholds, taper, stars, aliases, cells,
signs, and owners.  A product of two extension functions supplies a rank-one
matrix.  A sum of products requires a projective decomposition

\[
 B_i^{\rm br}(r,r')=\sum_\nu\alpha_\nu(r)
 \overline{\beta_\nu(r')}                                \tag{132.A11}
\]

with an affordable sum of source square-function norms.  Neither the source
nor the accepted outer \(\ell^1/\ell^2\) bounds controls this projective
cost.  Row decomposition or SVD is algebraically available, but it replaces
the signed scalar by an uncontrolled positive row/nuclear energy.

For one already-factorized transverse product, a fixed Fourier reproducing
kernel gives

\[
 |F_1(x)\overline{F_2(x)}|
 \lesssim_\varepsilon R^{\varepsilon/2}
 \prod_{j=1}^2
 \left(\sum_\theta\|F_{j,\theta}\|_4^2\right)^{1/2}.
 \tag{132.A12}
\]

This is an elementary project lemma derived after the source theorem, not a
printed Demeter--Wu pointwise theorem.  It has no negative power and does
not price (132.A11), Fourier thickening, strip reassembly, or physical
owners.  The refined theorem similarly charges positive local tube counts;
the centre ball's incidence is positive and uncontrolled, not necessarily
globally maximal.

Finally, the same-denominator controls have

\[
 b'=b,\qquad m=a-a'={n\over b},\qquad
 1\le m\lesssim {D\over W}=Y^{3/48}.                     \tag{132.A13}
\]

They are exact \(\xi\)-rulings.  At \(c=\kappa_i b^2\) their geometric
phase is one.  This is a hostile local control, not a lower bound for the
physical family.  The source narrow terms keep such rulings in positive
rectangle norms, but no accepted arithmetic estimate makes them smaller.

## 4. First doubtful or unproved step

For the undilated whole-shell route, the first false step is

\[
 \det\nabla^2\Phi_i\ne0
 \Longrightarrow \text{two-coordinate source transversality}.
\]

Equation (132.A5) disproves it.

For a properly localized, rescaled, and geometrically broad determinant
band, the first unproved step is the owner-preserving factorization theorem
(132.A11), together with a bound for its positive source functional that
has a strict cross-ray power.  Even if that broad theorem were granted, a
second independent theorem is required for the exact ruling/narrow part.

These are project-level missing hypotheses.  The adjudication does not say
that all future determinant-band rescalings or new narrow arithmetic
theorems are impossible; it says that Demeter--Wu Theorems 1.6 and 1.10 do
not directly provide them for the current scalar.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| primary v2 source and theorem text | Green: official arXiv v2 source archive audited; all theorem directions and support hypotheses retained. |
| exact hyperbolic normalization | Green after replacing the unrecentered dilation by (132.A6). |
| two-coordinate transversality | Green only on small, band-rescaled broad patches; same denominator remains narrow. |
| source radius, thickness, caps, ball, Jacobian | Red as an application: (132.A7) is only a dual-coordinate identity until this ledger is proved. |
| fixed-centre bridge | Green conditionally for an already-factorized product via (132.A12); no negative power or arithmetic norm follows. |
| joint physical coefficient | Red: no affordable owner-preserving projective norm is proved. |
| broad--narrow ruling split | Green geometrically; analytic narrow saving remains open. |
| same-denominator M1/M2 control | Green with \(m=a-a'=n/b\) and length \(D/W\); no family lower bound asserted. |
| refined incidence | Corrected to positive, uncontrolled local incidence, not automatically maximal. |
| capacity and downstream scope | Green as upper-capacity ledger only: \(35/48\), \(27/48\), \(24/48\); no global or M9 promotion. |

No numerical experiment was used; the round was entirely source,
analytical, and algebraic.

## 6. Dependencies and exact artifacts used

The adjudication used:

1. `protocol.md` and the Round-132 campaign packet;
2. `reports/demeter_wu_exact_source_card.md`;
3. `reports/literal_ratio_phase_hyperbolic_map.md`;
4. `reports/blind_pointwise_transversality_feasibility.md`;
5. `candidates/conductor_exact_hyperbolic_normalization.md`;
6. `reviews/source_post_chart_normalization_audit.md`;
7. `reviews/blind_post_unmask_scope_audit.md`;
8. `reviews/discovery_post_unmask_capacity_audit.md`; and
9. the accepted Round-130 and Round-131 graph nodes and syntheses named in
   the campaign manifest.

The source audit used the official Demeter--Wu v2 arXiv record and TeX source
only.  No secondary source or numerical experiment was used.

## 7. Recommended state effect

**Promote** the exact chart (132.A1)--(132.A9), with \(R_h\) explicitly
scoped as a physical evaluation scale rather than an accepted source radius.

**Promote** the primary Demeter--Wu theorem card as a source-audit guardrail.

**Promote** the direct-source applicability obstruction: the present literal
scalar has neither the required affordable projective coefficient
factorization nor a signed narrow-ruling estimate, and the source's positive
square functions do not substitute for either.

Keep `GC-W7-16-actual-reduced-determinant-correlation` open at
\(Y^{35/48+\varepsilon}\).  Make no change to M9-M1, M9-M2, endpoint
uniformity, M9, the conditional bridge, the internally proved exponent
\(1/3\), the external Li--Yang benchmark, or the quarter target.

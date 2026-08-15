# Centered functional equation and angular return map

- Campaign: `m9-m1-angular-mellin-separation`
- Round: `15`
- Task: `twisted_divisor_radial_attack`
- Role: analytic functional-equation attacker
- Graph SHA-256 supplied in the brief: `aa33b1c414e135f96f912b34ec17acda79c3cf5cb68a73c4fb706bd393993251`

## 1. Result

Put

\[
 \tau_{\chi_4,z}(n)=\sum_{hq=n}\chi_4(q)h^{-z},\qquad
 a_z(n)=n^{z/2}\tau_{\chi_4,z}(n)
 =\sum_{hq=n}\chi_4(q)(q/h)^{z/2}.
\]

Then the centered Dirichlet series

\[
 F_z(s):=\sum_{n\ge1}a_z(n)n^{-s}
 =\zeta(s+z/2)L(s-z/2,\chi_4)
\tag{1.1}
\]

has a completed functional equation

\[
 \boxed{\Lambda_z(s)=\Lambda_{-z}(1-s)}.
\tag{1.2}
\]

Thus every Voronoi transformation reflects the angular coefficient
exactly as \(a_z\mapsto a_{-z}\). It does not make the coefficient
untwisted or replace it by \(r_2/4\).

For the Round-15 radial sum, where \(z=u+v\), the centered rewrite is

\[
 \boxed{\mathcal R_X(u,v)=
 \sum_{n\le N_X}a_z(n)n^{-3/4-v/2}e(\sqrt{Xn}).}
\tag{1.3}
\]

The spatial Mellin variable \(u\) disappears from the radial power and
survives in the angular shift \(z\) and the outside scale factors. This
is a useful exact separation. However, the functional equation maps the
square-root radial wave back to a reflected angular coefficient and a
dual wave localized at product centers \(m\approx X\). It is therefore a
return map to the reciprocal/nearest-product problem, not a new estimate.

## 2. Exact statement and hypotheses

Let \(\chi_4\) be the primitive odd character of conductor \(4\). Define

\[
 \Lambda_\zeta(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w),
\]

and

\[
 \Lambda_{\chi_4}(w)=
 (4/\pi)^{(w+1)/2}\Gamma((w+1)/2)L(w,\chi_4).
\]

Both have root number \(+1\). Hence

\[
 \Lambda_z(s):=
 \Lambda_\zeta(s+z/2)\Lambda_{\chi_4}(s-z/2)
 =A_z(s)F_z(s),
\]

where

\[
 \boxed{A_z(s)=2^{s+1-z/2}\pi^{-s-1/2}
 \Gamma\!\left({s+z/2\over2}\right)
 \Gamma\!\left({s-z/2+1\over2}\right).}
\tag{2.1}
\]

The arithmetic conductor is \(4\), the root constant is \(+1\), and on
\(s=\sigma+it\) the analytic conductor is, up to bounded archimedean
factors,

\[
 4(1+|t+\Im z/2|)(1+|t-\Im z/2|).
\tag{2.2}
\]

The ordinary series (1.1) converges absolutely when
\(\Re(s+z/2)>1\) and \(\Re(s-z/2)>1\). It has one ordinary pole,

\[
 s=1-z/2,\qquad
 \mathop{\rm Res}_{s=1-z/2}F_z(s)=L(1-z,\chi_4).
\tag{2.3}
\]

The completed product also has the inherited completed-zeta pole at
\(s=-z/2\); the other apparent gamma poles are cancelled by trivial
zeros. These statements are initially literal away from colliding special
parameters and otherwise hold by meromorphic continuation.

For \(f\in C_c^\infty(0,\infty)\), with
\(\widetilde f(s)=\int_0^\infty f(x)x^{s-1}\,dx\), contour shifting gives

\[
 \boxed{
 \sum_{n\ge1}a_z(n)f(n)
 =L(1-z,\chi_4)\widetilde f(1-z/2)
 +\sum_{m\ge1}a_{-z}(m)(\mathcal H_zf)(m),}
\tag{2.4}
\]

where the exact Hankel transform is defined by

\[
 \widetilde{\mathcal H_zf}(w)
 ={A_{-z}(w)\over A_z(1-w)}\widetilde f(1-w).
\tag{2.5}
\]

## 3. Proof or derivation

Absolute multiplication of the two Dirichlet series gives (1.1). The
separate functional equations give

\[
 \Lambda_\zeta(s+z/2)=\Lambda_\zeta(1-s-z/2),
\]

\[
 \Lambda_{\chi_4}(s-z/2)
 =\Lambda_{\chi_4}(1-s+z/2),
\]

because \(\tau(\chi_4)=2i\) and
\(\tau(\chi_4)/(i\sqrt4)=1\). Their product is exactly
\(\Lambda_{-z}(1-s)\), proving (1.2). Equivalently,

\[
 F_z(s)=G_z(s)F_{-z}(1-s),
\]

\[
 G_z(s)=2^{1-2s+z}\pi^{2s-1}
 {\Gamma((1-s-z/2)/2)\Gamma((2-s+z/2)/2)
  \over
  \Gamma((s+z/2)/2)\Gamma((s-z/2+1)/2)}.
\tag{3.1}
\]

Mellin inversion of \(f\), followed by a shift across (2.3), proves
(2.4). On the shifted line substitute (3.1), set \(w=1-s\), and expand
\(F_{-z}(w)\); this gives (2.5) and the reflected coefficient
\(a_{-z}\).

For the double-Mellin radial sum, the blind exact algebra gives

\[
 \mathcal R_X(u,v)=
 \sum_{n\le N_X}\tau_{\chi_4,u+v}(n)
 n^{-3/4+u/2}e(\sqrt{Xn}).
\]

Since \(\tau_{\chi_4,z}(n)=n^{-z/2}a_z(n)\) and \(z=u+v\), its power is
\(-3/4+u/2-z/2=-3/4-v/2\), proving (1.3).

For a smooth shell \(f(x)=V(x/N)x^{-3/4-v/2}e(\sqrt{Xx})\), Stirling's
formula in (2.5) gives the conductor-4 degree-two Hankel waves
\(e(\pm\sqrt{mx})\). The plus wave is nonstationary. In the minus wave,
the phase derivative is

\[
 {\sqrt X-\sqrt m\over2\sqrt x}.
\]

Consequently the effective dual support is

\[
 \boxed{m=X+O\!\left(\sqrt{X/N}\right),}
\tag{3.2}
\]

up to rapidly decreasing smooth tails for bounded \(z\). Thus a radial
shell \(n\asymp N\) returns to the near-product window around \(X\). At
the maximal radial length \(N\asymp\sqrt X\), its width is
\(X^{1/4}\), exactly the critical product scale already present in M1.
The reflection \(a_z\mapsto a_{-z}\) reverses the divisor ratio
\((q/h)^{z/2}\); it does not remove the one-sided angular sector.

For smooth \(f\), contour truncation is rapidly decreasing after allowing
the polynomial analytic-conductor factor in (2.2). For the actual top
profile, the spatial Mellin transform contains the exact Perron term
\(1/u\). Symmetric truncation recovers the endpoint half weight, while an
absolute height-\(T\) estimate costs
\(O(\log(2+T/a))\) on \(\Re u=a>0\). Hence (2.4) cannot be integrated
over all actual modes using only pointwise mode bounds. The accepted
physical stationary-transform error remains \(O_W(\log^2 X)\).

## 4. First doubtful or unproved step

The first unproved step is a uniform estimate for the reflected Hankel
sum and its top Perron maximal integral when \(\Im z\), scale \(j\), and
contour height all vary. Formula (2.2) shows why a fixed-\(z\) Voronoi
bound is insufficient: the two archimedean parameters
\(t\pm\Im z/2\) range independently. No bound of size \(X^\varepsilon\)
for the resulting near-product window (3.2) is proved here.

Thus the functional equation does not prove GAR, RCS, or any point of the
unresolved M1 corridor.

## 5. Required controls and outcomes

- **Centering:** pass. Direct expansion gives
  \(a_z(n)=n^{z/2}\tau_{\chi_4,z}(n)\), and (1.3) loses \(u\) from the
  radial exponent exactly.
- **Gamma/conductor/root number:** pass. Equations (2.1), (2.2), and
  (3.1) retain conductor \(4\), odd parity, and root number \(+1\).
- **Coefficient reflection:** pass. The functional equation gives
  \(F_{-z}(1-s)\), hence \(a_{-z}\), not \(a_z\) and not \(r_2/4\).
- **Pole:** pass. The only ordinary main term is the residue (2.3).
- **Dual-capacity control:** no new saving. The transform localizes at
  the already open nearest-product window (3.2).
- **Top endpoint:** conditional. Symmetric Perron inversion gives the
  correct half weight, but absolute mode integration loses \(\log T\)
  and needs a maximal estimate.
- **Numerics:** none used.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`;
- `rounds/codex-managed/m9-m1-angular-mellin-separation/briefs/twisted_divisor_radial_attack.md`;
- `rounds/codex-managed/m9-m1-angular-mellin-separation/reports/blind_double_mellin_derivation.md`;
- `sources/popov_2024_voronoi_gauss.md`.

No other Round-15 report was read. No web search or numerical experiment
was performed in this task. No shared proof state was edited.

## 7. Recommended state effect

Promote after conductor verification the centered coefficient identity
(1.1), completion (2.1), functional equation (1.2), and exact reflection
\(a_z\mapsto a_{-z}\) as `proved_internal`. Retain the double-Mellin
identity and centered radial rewrite (1.3) as exact refinements of the
global angular recombination.

Record a scoped return-map obstruction: fixed-mode Voronoi transforms the
radial shell into the same near-product window around \(X\), with the
angular ratio reflected rather than cancelled. Do not promote (3.2) with
full contour uniformity until a separate Stirling/seam review checks the
large-\(|\Im z|\) transition ranges. Keep GAR, RCS, blockwise M9-M1, M9,
and the Gauss target open. The next possible kernel is the signed
correlation between the \(z\) and \(-z\) angular sectors together with a
top Perron maximal theorem; the functional equation alone supplies
neither.

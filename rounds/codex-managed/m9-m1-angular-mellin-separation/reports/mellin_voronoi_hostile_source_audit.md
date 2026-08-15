# Mellin/Voronoi hostile source audit

- Campaign: \`m9-m1-angular-mellin-separation\`
- Round: \`15\`
- Task: \`mellin_voronoi_hostile_source_audit\`
- Role: primary-source and hostile reviewer
- Graph SHA-256 supplied in the brief: \`aa33b1c414e135f96f912b34ec17acda79c3cf5cb68a73c4fb706bd393993251\`

## 1. Result

The arithmetic family produced by the exact double Mellin separation is a
degree-two Eisenstein family, but neither audited Voronoi source supplies the
uniform mode estimate required by GAR.

For

\[
 \tau_{\chi_4,z}(n)=\sum_{hq=n}\chi_4(q)h^{-z},
 \qquad
 a_z(n)=n^{z/2}\tau_{\chi_4,z}(n)
       =\sum_{hq=n}\chi_4(q)(q/h)^{z/2},
\]

one has, in the joint absolute-convergence region,

\[
 \sum_{n\ge1}\frac{\tau_{\chi_4,z}(n)}{n^s}
 =\zeta(s+z)L(s,\chi_4),
 \quad
 F_z(s_0):=\sum_{n\ge1}\frac{a_z(n)}{n^{s_0}}
 =\zeta(s_0+z/2)L(s_0-z/2,\chi_4).
\tag{1.1}
\]

The centered completed product has root number \(+1\), arithmetic conductor
\(4\), and functional equation

\[
 \Lambda_z(s_0)=\Lambda_{-z}(1-s_0),
\tag{1.2}
\]

where

\[
 \Lambda_z(s_0)=
 \pi^{-(s_0+z/2)/2}\Gamma\!\left(\frac{s_0+z/2}{2}\right)
 \left(\frac4\pi\right)^{(s_0-z/2+1)/2}
 \Gamma\!\left(\frac{s_0-z/2+1}{2}\right)F_z(s_0).
\tag{1.3}
\]

Thus Voronoi duality sends \(a_z\) to \(a_{-z}\): it reflects the divisor
angle \(q/h\leftrightarrow h/q\). It does not bound a mode, and it does not
preserve the one-sided M1 cone. At \(z=0\),
\(a_0(n)=\sum_{q\mid n}\chi_4(q)=r_2(n)/4\), so the self-dual zero mode is
exactly the classical Hardy--Voronoi return already known to be equivalent
to the Gauss target at the relevant cutoff. Verdict: no new GAR estimate
and no new point of the unresolved \(U_1\) region follows from the audited
literature.

## 2. Exact statement and hypotheses

The exact Mellin algebra gives, for interior scales,

\[
 W\!\left(\frac{2h\sqrt X}{D_j\sqrt n}\right)
 =\frac1{2\pi i}\int_{(a)}\widehat W(u)
 \left(\frac{D_j}{2\sqrt X}\right)^u n^{u/2}h^{-u}\,du,
\]

and

\[
 \mathbf1_{h\le H_j}\Phi\!\left(\frac h{H_j+1}\right)
 =\frac1{2\pi i}\int_{(b)}\widehat\phi(v)(H_j+1)^vh^{-v}\,dv.
\]

Hence the divisor power is exactly \(h^{-(u+v)}\), while the radial power is
\(n^{-3/4+u/2}\). The relevant shift is \(z=u+v\), not \(u\) or \(v\)
separately. The floors remain exactly in \((H_j+1)^v\).

The closest primary source is Banerjee--Khurana,
[arXiv:2306.12399v2](https://arxiv.org/pdf/2306.12399). Their definitions
(1.11) and identities (5.10)--(5.12) include

\[
 \overline\sigma_{z,\chi}(n)=\sum_{d\mid n}d^z\chi(n/d),
 \qquad
 \sum_n\overline\sigma_{z,\chi}(n)n^{-s}=\zeta(s-z)L(s,\chi),
\]

so our coefficient is exactly
\(\tau_{\chi_4,z}=\overline\sigma_{-z,\chi_4}\). Their Theorems 4.3--4.4
cover an odd primitive character modulo \(q\), an analytic test function
inside a closed contour containing a finite interval, nonintegral interval
endpoints, and \(0<\Re\nu<1/2\). The dual transform is an explicit
\(J_\nu,Y_\nu,K_\nu\) combination with argument \(4\pi\sqrt{nt/q}\).

Kiral--Zhou,
[Algebra & Number Theory 10 (2016), 2267--2286](https://doi.org/10.2140/ant.2016.10.2267),
Theorem 1.3, requires moderate Hecke coefficients and precise functional
equations for every primitive character twist; its stated setup requires
the twisted \(L\)-function to continue holomorphically to the whole plane.
Their Example 1.8 explains applicability to certain isobaric sums, but the
proof is mainly for \(N\ge3\), with the \(N=2\) modification only in Remark
3.2. Our product is degree two, ramified at \(4\), noncuspidal, and has a
zeta pole for the principal twist. Therefore Theorem 1.3 is a structural
analogy, not a hypothesis-matched black box unless polar terms and the
ramified local factor are derived separately.

## 3. Proof or derivation

Equation (1.1) follows by absolutely interchanging the \(h,q\) sums when
\(\Re s>1\) and \(\Re(s+z)>1\). For the centered form substitute
\(s=s_0-z/2\).

For \(\chi_4\), the character is primitive odd modulo \(4\),
\(\tau(\chi_4)=2i\), and its root number is
\(\tau(\chi_4)/(i\sqrt4)=1\). Multiplying the standard completed zeta
factor by the completed odd-character factor gives (1.3). Applying their
two functional equations changes

\[
 (s_0+z/2,\ s_0-z/2)
 \longmapsto
 (1-s_0-z/2,\ 1-s_0+z/2),
\]

which is exactly \(F_{-z}(1-s_0)\). Coefficient duality is therefore the
angular reflection \(a_z\leftrightarrow a_{-z}\), consistent with the
Banerjee--Khurana transform from barred to unbarred twisted divisor sums.

This identity has no favorable conductor drop. At Mellin height
\(s_0=\sigma+it\), \(z=\alpha+i\eta\), the two archimedean parameters are
approximately \(t+\eta/2\) and \(t-\eta/2\); the degree remains two and the
finite conductor remains \(4\). Neither source states estimates uniform in
arbitrarily large \(\eta\). Banerjee--Khurana's formula contains Bessel
functions of complex order \(\nu\) and trigonometric factors in \(\nu\),
but records no quantitative bounds uniform in \(\Im\nu\). Kiral--Zhou
proves an identity for fixed spectral data, not a mode-integrable estimate.

At \(z=0\), the dual coefficient is unchanged and equals \(r_2/4\).
Popov, [Theorem 5, equations (5.1)--(5.2)](https://www.mathnet.ru/eng/rm10162),
gives the truncated radial \(r_2(n)n^{-3/4}
\cos(2\pi\sqrt{nX}+\pi/4)\) formula with target-sized error when
\(N\asymp X^{1/2}\). Consequently an \(X^\varepsilon\) bound for this
normalized zero-mode radial sum is equivalent, up to target-sized errors,
to the desired Gauss estimate.

## 4. First doubtful or unproved step

The first illegal step would be to apply a fixed-\(z\) Voronoi identity and
then interchange it with the full double Mellin contours as though the
result were uniformly integrable. No audited theorem provides the needed
uniformity in \(\Im(u+v)\), in the separate radial exponent \(u\), or in
the scale factors.

There are two concrete contour obstructions. First,
\(\widehat\phi(v)=1/v+O(1)\) near \(v=0\); shifting to the zero mode crosses
this pole and the associated zeta polar term. Second, the one-sided top
symbol satisfies

\[
 \widehat W_+(u)=\frac1u-\frac1u\int_0^1W'(t)t^u\,dt.
\]

The \(1/u\) part is only a symmetric Perron limit; absolute truncation costs
\(\log T\). A pointwise Voronoi formula does not justify the required
\(T\to\infty\) maximal/Hilbert estimate. Banerjee--Khurana also assumes an
analytic interval weight, so it does not directly absorb this hard top
jump.

## 5. Required control tests and outcomes

- **Power and character algebra: pass.** Direct substitution gives the
  exact shift \(z=u+v\), radial power \(n^{-3/4+u/2}\), and character on
  \(q\).
- **Functional-equation normalization: pass.** The exact gamma factors,
  conductor \(4\), root number \(+1\), and dual \(z\mapsto-z\) are as in
  (1.2)--(1.3).
- **Ramified noncuspidal source match: fail for Kiral--Zhou as a direct
  import.** Its theorem does not directly cover the zeta pole and level-\(4\)
  local data in the form needed here.
- **Character-Voronoi source match: partial.** Banerjee--Khurana matches the
  coefficient and odd primitive character, but only states an exact formula
  for \(0<\Re z<1/2\) and analytic finite-interval weights, with no large
  imaginary-shift estimate.
- **Floor control: pass algebraically, no analytic gain.** Exact factors
  \((H_j+1)^v\) survive; functional equations do not telescope them across
  scales.
- **Hard top and zero mode: fail as estimates.** The former requires a
  maximal Perron bound; the latter is the Hardy--Voronoi return.
- **Exponent verdict: no change.** Neither GAR nor any point of \(U_1\) is
  closed. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- \`protocol.md\`, \`state/proof_obligations.yml\`, and
  \`state/active_campaign.yml\`;
- \`rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md\`;
- \`rounds/codex-managed/m9-combined-top-cones/synthesis.md\`;
- the Round-15 brief and, on the conductor's bounded continuation,
  \`reports/blind_double_mellin_derivation.md\`;
- Banerjee--Khurana, *Character analogues of Cohen-type identities and
  related Voronoi summation formulas*,
  [arXiv:2306.12399v2](https://arxiv.org/pdf/2306.12399), especially
  (1.11), (5.10)--(5.17), and Theorems 4.3--4.4;
- Kiral--Zhou, *The Voronoi formula and double Dirichlet series*,
  [DOI 10.2140/ant.2016.10.2267](https://doi.org/10.2140/ant.2016.10.2267),
  especially Theorem 1.3, Example 1.8, and Remark 3.2;
- \`sources/popov_2024_voronoi_gauss.md\` and Popov's primary
  [Math-Net record](https://www.mathnet.ru/eng/rm10162), Theorem 5.

No shared proof state was edited.

## 7. Recommended state effect

Promote only the centered functional-equation algebra (1.1)--(1.3) and the
scoped return-map obstruction \(a_z\leftrightarrow a_{-z}\), with the zero
mode equal to \(r_2/4\). Retain the exact double-Mellin identity as internal
evidence after conductor seam verification.

Do not promote a Voronoi estimate. Record three open requirements: uniform
complex-order Bessel/Voronoi control over the actual two-dimensional mode
measure, a maximal estimate for the top \(1/u\) Perron contour, and explicit
handling of the \(v=0\)/zeta residues. Keep GAR, RCS, blockwise M9-M1, M9,
and the Gauss target open; record no \(U_1\) region gain.

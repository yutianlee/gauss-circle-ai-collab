# Conductor candidate: exact signed Farey scalar, safe rows, and resonance fibres

Campaign: m9-m1-lower-gar-signed-farey-scalar-gate

Starting graph SHA-256:
56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797

## 1. Result: strict signed reduction

The literal flat lower-radial scalar has an exact reduced-Farey form that
does not pass through the rejected positive square function. After
squaring this actual scalar, the whole same-denominator block is at the
target-square scale. All exact ordinary and character-adjusted carrier
collisions, together with a microscopic Farey collar around them, also
have target-safe total absolute mass.

The remaining object is one exact signed cross-denominator scalar whose
ordinary and complete physical carriers are both separated by more than
the microscopic Farey scale. Its coefficient-blind absolute capacity is
still \(y^2\), against target \(y\). No estimate of that residual scalar
is proved here.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

and use the literal \(J_{R,y}\), \(V_{\rm low}\), and \(\eta\) of the
Round-121 flat reduction. Put

\[
 L_\chi(T)=\sum_{g\le T}\frac{\chi_4(g)}g,
 \qquad
 \lambda_b=\frac{\chi_4(b)}bL_\chi(y/b).
\tag{138.C1}
\]

Then

\[
 \mathcal F_N=
 \sum_{\substack{2\le b\le y\\b\ {\rm odd}}}\lambda_b
 \sum_{\substack{1\le a<b\\(a,b)=1}}
 e(aN/b)J_{R,y}(a/b)
\tag{138.C2}
\]

is termwise equal to the integerized flat cone
\(\mathcal B_{\rm flat}^{(N)}(X)\). The accepted Round-121 seam is
\(\mathcal B_{\rm flat}^{+}(X)=\mathcal B_{\rm flat}^{(N)}(X)+O(R)\);
the frozen scalar itself always has phase \(e(hN/d)\). The certified
small positive arc has \(h<d\) (the inequality \(h/d\ll R^{-1}\) alone
would give this only asymptotically). At every occurring rational sample,
\(\eta(ya/b)=1\), and hence

\[
 \lambda_bJ_{R,y}(a/b)
 =\chi_4(b)c_{a,b},\qquad
 c_{a,b}=\frac{L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2).
\tag{138.C3}
\]

There is a fixed \(C\) such that

\[
 |c_{a,b}|\ll\frac1a,\qquad a\le Cb/R.
\tag{138.C4}
\]

For odd \(b\), \(\chi_4(b)=e((b-1)/4)\). Define

\[
 \theta_{a,b}=\frac{Na}{b}\pmod1,\qquad
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}\pmod1.
\tag{138.C5}
\]

Thus \(\mathcal F_N=\sum c_{a,b}e(\phi_{a,b})\). Let
\(\delta=y^{-2}\), and define

\[
 \mathcal R_\delta=
 \sum_{\substack{(a,b),(a',b')\\b\ne b'\\
 \|\theta_{a,b}-\theta_{a',b'}\|>\delta\\
 \|\phi_{a,b}-\phi_{a',b'}\|>\delta}}
 c_{a,b}\overline{c_{a',b'}}
 e(\phi_{a,b}-\phi_{a',b'}).
\tag{138.C6}
\]

Then

\[
 \boxed{
 |\mathcal F_N|^2
 =\mathcal R_\delta+O_\varepsilon(yX^\varepsilon).}
\tag{138.C7}
\]

In particular, the target follows from

\[
 \boxed{|\mathcal R_\delta|\ll_\varepsilon yX^\varepsilon.}
\tag{138.C8}
\]

Equation (138.C8) is not proved.

## 3. Proof or derivation

Reducing every nonzero fraction \(h/d=a/b\) in the flat cone writes
\(h=ag\), \(d=bg\). Since only odd \(d\) contribute,
\(\chi_4(bg)=\chi_4(b)\chi_4(g)\), and summing all lifts
\(g\le y/b\) before any norm gives (138.C1)--(138.C3). The certified
lower support has \(h<d\), so \(1\le a<b\); the absent \(b=1\) nonzero
residue agrees with \(J(0)=0\). The other frequency sign is the complex
conjugate.

The alternating-series bound and literal profile give

\[
 \sum_{a,b}|c_{a,b}|\ll y\log(2X),\qquad
 \sum_{a,b}|c_{a,b}|^2\ll y.
\tag{138.C9}
\]

Writing \(\mathcal F_N=\sum_bF_b\), the complete \(b=b'\) block satisfies

\[
 \boxed{
 \sum_b|F_b|^2
 \le\sum_{b\le y}
 \left(\sum_{a\le Cb/R}\frac1a\right)^2
 \ll y\log^2(2X).}
\tag{138.C10}
\]

This includes the equality diagonal and every unequal-numerator term on
one denominator.

For an ordinary phase fibre, let \(\theta_{a,b}=u/q\) in lowest terms and
put \(g=(N,b)\). Because \((a,b)=1\),

\[
 b=qg,\qquad g\mid N,\qquad (N/g,q)=1,\qquad
 (N/g)a\equiv u\pmod q.
\tag{138.C11}
\]

Here the standing odd-denominator condition forces both \(q\) and \(g\)
to be odd. Conversely these conditions, together with \(q,g\) odd,
reproduce the phase, subject only to the literal support and coprimality
restrictions. For each admissible \(g\mid N\), the numerator lies in one
residue class modulo \(q\), so, including \(q=1\),

\[
 M_\theta
 :=\sum_{\theta_{a,b}=\theta}|c_{a,b}|
 \ll\tau(N)\log(2X)\ll_\varepsilon X^\varepsilon.
\tag{138.C12}
\]

A \(\phi\)-fibre is the union of at most two such fibres: one with
\(b\equiv1\pmod4\), and one shifted by \(1/2\) with
\(b\equiv3\pmod4\). Thus (138.C12) holds for \(M_\phi\) as well.

Distinct \(\theta\)-values have reduced denominators at most \(y\), hence
spacing at least \(y^{-2}\). Distinct \(\phi\)-values have denominators at
most \(2y\), hence spacing at least \((4y^2)^{-1}\). An arc of radius
\(\delta\) therefore contains \(O(1+\delta y^2)\) carrier values. Combining
this with (138.C9) and (138.C12) gives, for either carrier,

\[
 \sum_{\|z-z'\|\le\delta}M_zM_{z'}
 \ll y\tau(N)\log^2(2X)(1+\delta y^2)
 \ll_\varepsilon yX^\varepsilon
\tag{138.C13}
\]

when \(\delta=y^{-2}\). Taking the complete same-denominator sector by
(138.C10), then deleting the union of the ordinary and adjusted collision
collars by (138.C13), proves (138.C7).

## 4. First doubtful or unproved step

The first open estimate is (138.C8). Its terms have distinct denominators
and genuinely separated ordinary and full carriers, but their positive
absolute mass is still \(y^{2+o(1)}\). Thus deleting the diagonal,
denominator rows, exact resonances, or a \(y^{-2}\) collar does not itself
supply the missing factor \(y=R^2\) in the square, equivalently \(R\) in
the scalar.

If \(b=Gr,b'=Gs,(r,s)=1\), then
\(\Delta=ab'-a'b=G\delta_0\), where \(\delta_0=as-a'r\), and every
solution is

\[
 a=a_0+r\ell,\qquad a'=a'_0+s\ell.
\tag{138.C14}
\]

The phase and denominator character are constant in \(\ell\). Although

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right),
\tag{138.C15}
\]

the endpoint terms necessarily cost \(r+s\). Indeed, for any odd
\(S>1\), take \(r=1,s=S,a=a'=1\), so \(\delta_0=S-1\). Choosing odd
\(G\gg R\) with \(GS\le y\) puts both numerator-denominator pairs in the
literal small-arc chart; for instance one may take
\(G\asymp R^{3/2}\) and \(S\asymp R^{1/2}\). The displayed reciprocal
kernel then has a one-point contribution \(1/(aa')=1\), whereas
\(\log(2X)/|\delta_0|\to0\). Hence (138.C15) alone does not yield an
aspect-free \(1/|\delta_0|\) saving. A modulus on the remaining
determinant fibres returns the full \(y^{2+o(1)}\) capacity.

Character Poisson has a complete hard-endpoint formula, but its clean
stationary expression is only an interior principal family. With the
project Fourier convention, its principal factor is

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{138.C16}
\]

where \(e(-1/8)=-i\,e(1/8)\). Its absolute capacity is
\(R^{3/2+o(1)}\), versus target \(R\). If
\(N=Ds^2\), \(D\) squarefree, exact phase one occurs only for
\(hr=Dt^2\), whose entire principal absolute mass is
\(\ll_\varepsilon RD^{-3/4}X^\varepsilon\). Near radicals and nonsquare
modes remain open. The hard \(d=y\) endpoint, nonstationary modes,
profile and stationary crossings, remainders, small heights, and the
opposite sign retain separate owners. A second Legendre transform returns
the original reciprocal phase.

## 5. Required control tests and outcomes

- Literal dictionary: pass. The reduction uses \(h=ag,d=bg\), sums every
  odd lift before a norm, and retains the small-arc \(h<d\) hypothesis.
- Centre and signs: pass. There is no nonzero \(b=1\) residue,
  \(J(0)=0\), and the opposite scalar is the conjugate.
- Diagonal and rows: pass by (138.C9)--(138.C10), with the entire
  same-denominator block target-safe.
- Divisors and fourth powers: pass. Divisors of \(N\) lie in the
  \(q=1\) fibre and have divisor-log mass.
- Character-adjusted alignment: pass. The mod-four carrier creates at
  most a two-fibre union, not a larger coherent exact class.
- Near resonance: pass only at the explicit \(y^{-2}\) scale. Wider
  fourth-power stationary packets remain in the survivor.
- Determinant direction: red as a gain. The \(\ell\)-direction is
  coherent and the partial fraction has unavoidable aspect endpoints.
- Poisson and radical scope: green only for the exact full Poisson owner
  ledger and the interior-principal calculation; no full stationary
  replacement or target bound follows.
- Directionality: pass. No positive \(k\)-energy, rowwise modulus on the
  survivor, arbitrary array, or centre average is substituted.
- Downstream scope: success would close only the lower-GAR analytic
  estimate through accepted connectors, not a direct M1 block, any M2
  parent, M9, or an exponent.

## 6. Dependencies and exact artifacts used

- state/proof_obligations.yml, especially the lower flat-discrepancy,
  near-square wavelet, and centered-square-function nodes;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/lower_gar_wavelet_feasibility.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/blind_statement.md;
- the three Round-138 primary reports.

No numerical experiment or external theorem is used.

## 7. Recommended state effect

After independent derivation and hostile seam review, promote the exact
scalar reduced-Farey identity, the target-safe same-denominator block, the
ordinary and physical phase-fibre classification, and the strict residual
reduction (138.C7). Retain (138.C8), the lower-radial signed estimate, GAR,
both direct blockwise M1 parents, M9-M1, every M2 parent, endpoint
uniformity, M9, the quarter theorem, and both global exponents as open.

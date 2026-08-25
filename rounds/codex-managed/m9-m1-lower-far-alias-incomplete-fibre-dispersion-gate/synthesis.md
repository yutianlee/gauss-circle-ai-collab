# Round 141 synthesis: microscopic resonances are safe, incomplete-fibre dispersion remains open

Campaign: m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate

Starting graph SHA-256:
072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

## Decision

Close under
\(\mathsf{incomplete\_fibre\_dispersion\_no\_go}\).
For

\[
R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\]

let \(A_\rho(m)\) be the exact Round-140 height-dependent incomplete
divisor coefficient and define

\[
C(m)=\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\]

On the disjoint dyadic blocks
\(\mathcal I_M=[M,2M)\cap[1,C_VN/R^2]\), put

\[
k_m=\left\lfloor\sqrt{Nm}+{1\over2}\right\rfloor,
\qquad j_m=k_m^2-Nm.
\]

Then

\[
\boxed{
\mathfrak T_N=
\sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
+O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{141.S1}
\]

The target bound for the survivor in (141.S1) is not proved.

## Positive progress

The exact least-odd mask differs from \(r>4h\) only on
\(O_\rho(1+\sqrt h+h/y)\) aliases at height \(h\).  Their total
weighted mass is \(O_{\rho,V}(\log X)\), so every floor and every real
centre is removed at target cost.

The nearest-integer phase cell has real \(m\)-length
\[
{2k\over N}\ll R^{-1}<1,
\]
and hence is a singleton.  For nonzero \(j\),
\[
\#\{k\bmod N:k^2\equiv j\pmod N\}
\ll_\varepsilon N^\varepsilon|j|^{1/2}.
\]
It follows that
\[
\#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
\ll_\varepsilon N^\varepsilon M^{3/4}.
\]
After the \(m^{-3/4}\tau(m)\) weight, every such block is target-safe.
The exact radicals \(j_m=0\) are \(m=Dt^2\) when \(N=Du^2\), and are
also target-safe.  This proves (141.S1).

## Exact obstructions

Writing \(m=2^\nu n\), \(n\) odd, and pairing the odd factors gives

\[
\sigma_{\chi_4}(n)
=(1+\chi_4(n))A_\nu(n)+B_\nu(n).
\tag{141.S2}
\]

On \(\chi_4(n)=-1\), both the complete and central coefficients vanish,
so the far coefficient survives untouched.  On \(\chi_4(n)=1\),
(141.S2) returns \(r_2(2^\nu n)/4\) and an owner-sized exact central
band.  Raw complete, central, and negative-character far incidences
retain \(R^{1/2+o(1)}\) weighted capacity.  This is not a grouped or
signed lower bound.

The exact incomplete coefficient has a full additive mode:

\[
\sum_{m\le M}A_\rho(m)e(m/4)
={i\pi\over8}M+O_{\rho,c_0}(M^{3/4})
\qquad(2\le M\le c_0y),
\tag{141.S3}
\]

\[
\sum_{m\le M}m^{-3/4}A_\rho(m)e(m/4)
={i\pi\over2}M^{1/4}+O_{\rho,c_0}(\log(2M)).
\tag{141.S4}
\]

For sufficiently large \(M\) in this range, the total variation of
\(A_\rho\) is \(\gg M\).  Thus generic uniform additive cancellation
and low-variation hypotheses are false.  Equations (141.S3)--(141.S4)
are coefficient obstructions, not lower bounds for the nonlinear
fixed-centre scalar.

## Mellin and literature status

After target-safe ratio smoothing, the dyadic cone sum has the exact
double-Mellin arithmetic factor

\[
4^{-t}\zeta(s+t)L(s-t,\chi_4).
\tag{141.S5}
\]

The sharp ratio step would require Perron height \(T\gg H\); the
smoothed transition has effective ratio bandwidth
\(H^{1/2}X^\varepsilon\).  The independently repaired source ledger is:

- Robert--Sargos: \(R^{1/2+\varepsilon}\) after separation,
  \(R^{3/4+\varepsilon}\) for a direct joint mask;
- Sargos--Wu Theorem 9: \(R^{2/5+\varepsilon}\) with separated
  coefficients; its adjacent joint-domain lemma excludes rank one;
- Tao--Trudgian--Yang rowwise:
  \(R^{267/641+\varepsilon}\);
- Popov/Li--Yang complete radial cosine:
  \(R^{4\theta_*-1+\varepsilon}\), with the wrong incomplete
  coefficient and no individual-complex-branch consequence;
- even an ideal shifted mean square used through Mellin
  Cauchy--Schwarz: \(R^{1+\varepsilon}\).

No audited source reaches \(R^\varepsilon\) for the required
fixed-centre signed linear functional.

## Remaining gap and proof status

The first open estimate is

\[
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.
\tag{141.S6}
\]

The cells are singleton, the congruence argument exhausts its
target-safe range at \(|j|=\sqrt M\), divisor pairing self-returns or
is blind, the coefficient contains a bad quarter-frequency direction,
and every audited transform or source estimate remains polynomially
above target.  A new fixed-centre arithmetic correlation mechanism is
required.

Equation (141.S1) is only an unsquared scalar equivalence.  It proves no
collar--tail cross term, residual deletion, lower GAR, direct M1
parent, M9-M1, M2 parent, M9-M2, endpoint theorem, M9, bridge, or
quarter theorem.

The strongest internally proved exponent remains
\[
{1\over3}.
\]
The separately audited external Li--Yang exponent remains
\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\]
Round 141 proves no exponent improvement.

Resulting graph SHA-256:
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76

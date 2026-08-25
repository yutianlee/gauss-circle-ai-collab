# Round 146 conductor controls

- Campaign: m9-m1-lower-cone-three-variable-hessian-dispersion-gate
- Round: 146
- Starting graph SHA-256: 7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d
- Allocation: 100% exact algebra, analytic bookkeeping, and primary-source verification; 0% numerical

## 1. Owner partition and unmasking

For each radial block, put

\[
 T_M=\lceil M^{1/4}\rceil,\qquad J_M=M^{3/4}.
\]

The ambient squarefree-kernel support is exactly

\[
\{t<T_M,\ |j|>J_M\}
\dot\cup
\{t<T_M,\ |j|\leq J_M\}
\dot\cup
\{t\geq T_M\}.
\]

The first set is the Round-145 masked small-\(t\) survivor. The second
is a subset of the accepted Round-144 absolute cell owner, including
the separately accepted exact-radical channel. The third is the
accepted Round-145 unmasked large-\(t\) owner. Therefore

\[
 \mathfrak S_N^{<,>}
 =\mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon),
\qquad
 \mathfrak T_N
 =\mathfrak S_N^{<,>}+O_{\varepsilon,V}(X^\varepsilon).
\]

The two errors occupy disjoint sets in this partition. The exact
ceiling identity

\[
 t<M^{1/4}\iff t<\lceil M^{1/4}\rceil
\]

holds for integral \(t\). Strict \(>\) and complementary \(\leq\)
leave no equality gap. Outcome: **GREEN**.

## 2. Coefficient and multiplicity

The squarefree-common-kernel inverse is

\[
 h=\gamma da^2,\qquad r=\gamma eb^2,\qquad
 s=de,\qquad t=\gamma ab.
\]

Prime valuations show that \(\gamma,d,e\) are pairwise coprime and
squarefree, while \(a,b\) are unrestricted positive integers.
The parity condition \(r\) odd is exactly that \(\gamma,e,b\) are odd,
and

\[
 \chi_4(r)=\chi_4(\gamma)\chi_4(e),\qquad
 r>4h\iff eb^2>4da^2.
\]

The full-gcd inverse is

\[
 h=Gda^2,\qquad r=Geb^2,\qquad
 Gab=t,\qquad(da,eb)=1.
\]

No extra coprimality with \(G\) is valid. Both maps reconstruct one and
only one ordered divisor incidence. Finally,

\[
 |\kappa_t(d,e)|
 \leq\sum_{\gamma ab=t}1=\tau_3(t).
\]

Outcome: **GREEN; inherited Round-145 identity correctly restated**.

## 3. Hessian and stationary algebra

Multiplying the scaled Hessian by \(4\) gives

\[
 A=
 \begin{pmatrix}
 0&2&2\\
 2&-1&1\\
 2&1&-1
 \end{pmatrix}.
\]

Direct cofactor expansion gives

\[
 \det A
 =-2(-4)+2(4)=16,
\]

so the determinant of the scaled Hessian is \(16/4^3=1/4\).
Its characteristic roots are

\[
 -\frac12,\qquad\frac1{\sqrt2},\qquad-\frac1{\sqrt2}.
\]

For \(f=c\,t\sqrt{de}\), the critical equations for
\(f-ut-vd-we\) invert to

\[
 t=\frac{2\sqrt{vw}}c,\qquad
 d=\frac uc\sqrt{\frac wv},\qquad
 e=\frac uc\sqrt{\frac vw}.
\]

Euler homogeneity has total degree \(2\), hence the critical value is

\[
 f-(ut+vd+we)=-f=-\frac{2u\sqrt{vw}}c.
\]

Thus \(c\mapsto-2/c\mapsto c\) only at the phase-monomial level after
reversing the second alias orthant. No amplitude-level identity is
claimed. Outcome: **GREEN**.

## 4. Capacity and face ledger

On a nonempty dyadic box,

\[
 T^2DE\asymp M,\qquad
 TDE\asymp\frac MT.
\]

The weight \(M^{-3/4}\) and divisor envelope therefore give

\[
 |\mathfrak U_{M,T,D,E}|
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.
\]

From \(t=\gamma ab\), one has \(a/b=\gamma a^2/t\geq1/t\).
The strict cone yields

\[
 \frac ed>\frac4{t^2},\qquad
 d^2<\frac m4,\qquad
 e^2>\frac{4m}{t^4}.
\]

Consequences:

- \(E=1\) is empty in the strict small-\(t\) range;
- bounded \(E\) forces a terminal \(T\)-shell;
- \(D=1\) is structurally allowed;
- \(t=1\) is the exact rank-one \(d,e\) cone;
- a fixed lattice-width cone collar costs at most
  \(M^{-3/4}TDX^\varepsilon\ll X^\varepsilon\);
- a relative-width collar is not automatically safe.

Outcome: **GREEN with mandatory open \(t=1,D=1\) faces**.

## 5. Difference and dual-capacity controls

Zero extension gives

\[
\left|\sum_tA_t e(\sqrt N\,t\sqrt{de})\right|^2
=\sum_{h\in\mathbb Z}e(\sqrt N\,h\sqrt{de})
\sum_tA_{t+h}\overline{A_t}.
\]

The \(h=0\) term is the constant diagonal. Every \(h\neq0\) term has
the rank-one \(d,e\) phase and an unproved exact coefficient
correlation.

With \(F=\sqrt{NM}\) and \(V_3=TDE\), the smooth dual bounding box has

\[
 \#\{\text{aliases}\}
 \ll(1+F/T)(1+F/D)(1+F/E)\ll F^3/V_3,
\]

and one stationary amplitude is \(O(V_3/F^{3/2})\). Aliaswise triangle
inequality therefore has upper price \(F^{3/2}\), or \(N^{3/4}\) after
the physical \(M^{-3/4}\) weight. This is an adverse upper ledger, not
a lower bound. Outcome: **GREEN as a mechanism no-go**.

## 6. Cao--Zhai power recomputation

On

\[
 M=R^2,\quad T=R^\tau,\quad D=E=R^{1-\tau},
\quad F=R^3,
\]

a source monomial

\[
 (F^aD^bT^cE^c)^{1/q}
\]

has normalized exponent

\[
 \eta(\tau)=\frac{3a+b+c-b\tau}{q}-\frac32.
\]

Applying this formula to all fourteen Cao--Zhai Theorem-6 terms gives

\[
\begin{aligned}
 &\frac38-\frac{5\tau}8,\quad
 \frac38-\tau,\quad
 \frac{11}{29}-\frac{43\tau}{58},\quad
 \frac{41}{108}-\frac{41\tau}{54},\\
 &\frac{37}{98}-\frac{37\tau}{49},\quad
 \frac{11}{29}-\frac{23\tau}{29},\quad
 \frac{127}{336}-\frac{125\tau}{168},\quad
 \frac{115}{304}-\frac{115\tau}{152},\\
 &\frac{127}{336}-\frac{131\tau}{168},\quad
 \frac{33}{100}-\frac{181\tau}{200},\quad
 \frac{123}{368}-\frac{167\tau}{184},\\
 &\frac{33}{100}-\frac{19\tau}{20},\quad
 \frac13-\frac{5\tau}{6},\quad
 \frac14-\frac{9\tau}{8}.
\end{aligned}
\]

At \(\tau=1/2\), terms \(1,3,7\) remain positive, respectively

\[
 \frac1{16},\qquad\frac1{116},\qquad\frac1{168}.
\]

Term 1 becomes target-sized only for \(\tau\geq3/5\), outside the
small-\(t\) range. The direct displayed source bound therefore creates
no fixed-power balanced corridor. This remains only an upper-bound
limitation. Outcome: **GREEN**.

## 7. Source-hypothesis controls

| Source | Phase/dimension | Coefficient | Top power | Outcome |
|---|---|---|---|---|
| Cao--Zhai Theorem 6 | Passes with \((d,t,e)\) and exponents \((1/2,1,1/2)\) | Requires \(a(d)b(t,e)\) | Term 1 leaves \(R^{1/16}\) formally at \(\tau=1/2\) | Adverse |
| Cao--Zhai Theorem 7 | Phase ratio is \(-1\) | Requires no \(d\)-coefficient and \(a(t)b(e)\) | Second term leaves \(R^{7/8}\) | Adverse; final printed term inconclusive |
| Robert--Sargos Theorem 1 | Phase passes | Requires \(a(t,e)b(d)\) | Leaves \(R^{1/4}\) formally at endpoint | Adverse |
| Sargos--Wu Theorem 9 | Fixed-\(t\) phase passes | Requires separated \(d,e\) coefficients | Leaves \(R^{1/4}\) formally at endpoint | Adverse |
| Sargos multidimensional transform | Smooth phase passes | Requires compactly supported \(C^k\) amplitude | Phase-level self-return; triangle price adverse | Adverse |

Primary theorem hypotheses and links are recorded in the source report
and conductor candidate. Outcome: **GREEN as a source-interface
no-go; no source-legal target theorem**.

## 8. Scope controls

The exceptional family \(N=sL^2+1\) is retained only as a refutation of
uniform modular separation. The individual positive direction
\(e(+f)\) and fixed center \(N=\lfloor X\rfloor\) are preserved.
The independent Round-138 cross owner, lower GAR, direct M1 parents,
all M2 owners, endpoint uniformity, M9, bridge, quarter theorem, and
global exponent claims remain unchanged.

Final control outcome:

\[
\boxed{\mathsf{three\_variable\_dispersion\_no\_go}}
\]

with the exact unmasking reduction retained and the signed target open.

## 9. Terminal validation and closure

The State Patch dry run passed before mutation. Application created two
obligations, updated seven, rejected ten false inferences, and retained
eight downstream nodes unchanged. The resulting authoritative graph has
SHA-256
1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5.

The graph validator, completed-campaign validator, campaign and state
JSON parsers, bytecode compilation, six unit tests, forbidden-control
scan of every Round-146 artifact, and repository diff check all pass.
The terminal blind review, source review v2, and independent
mathematical reread are GREEN.

Outcome: **GREEN; Round 146 closed**.

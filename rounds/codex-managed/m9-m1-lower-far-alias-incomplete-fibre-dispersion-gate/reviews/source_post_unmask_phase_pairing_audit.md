# Round 141 post-unmask phase-counting and divisor-pairing audit

- Campaign: `m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate`
- Task: `source_post_unmask_phase_pairing_audit`
- Role: `post_unmask_seam_reviewer`
- Graph at assignment: `072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0`

## 1. Result and seam verdicts

**Final verdict: GREEN for the repaired candidate on every assigned seam: (141.C15)--(141.C28), the top-scale capacity statement as actually written, and the direction \((141.C7)\Longleftrightarrow(141.C38)\) at target scale.**

The candidate now expressly limits the capacity claim to the complete radial coefficient, “raw central incidences,” and “raw untouched negative-character far incidences.” It never promotes that capacity to grouped coefficient mass or a signed fixed-centre lower bound. The contrary inference remains below only as a rejected control, not as a defect in the candidate.

The independent seam verdicts are:

| Seam | Verdict | Reason |
|---|---|---|
| Tie convention and exact cells, (141.C15)--(141.C16) | **GREEN** | Half-integer ties are impossible; the half-open cell is correct and has length \(2k/N\). |
| Singleton-cell claim | **GREEN** | On \(m\le C_VN/R^2\), \(k\ll_VN/R\), so the cell length is \(O_V(R^{-1})<1\). |
| Prime-power root count, (141.C19)--(141.C20) | **GREEN** | The odd-prime, \(2\)-adic, odd-valuation, and zero-root cases give the claimed bound, with room in the factor \(4^{\omega(N)+1}\). |
| \(k<N\), injectivity, and microscopic count, (141.C21) | **GREEN** | The effective range gives \(k<N\); for fixed \(j\), \(m=(k^2-j)/N\), so reduction modulo \(N\) is injective. |
| Dyadic weights and exact radicals, (141.C21)--(141.C22) | **GREEN** | Every dyadic block, including \(M=1\) and the terminal truncation, costs \(O(X^\epsilon)\); \(j=0\) is exactly \(m=Dt^2\). |
| Hard floor correction, (141.C17)--(141.C18) | **GREEN** | The collar has \(O_\rho(1+\sqrt h+h/y)\) odd points per height and total weighted mass \(O_{\rho,V}(\log X)\). This verdict is only for the displayed hard correction, not for the later smooth-ratio/Mellin construction. |
| \(2\)-adic factorization and swapped-mask algebra, (141.C23)--(141.C28) | **GREEN** | All powers of \(2\) lie in \(h\), the two far masks are disjoint, and the swap contributes exactly \(\chi_4(n)A_\nu(n)\). |
| Central and negative-character controls | **GREEN** | For \(\chi_4(n)=-1\), both \(\sigma_{\chi_4}(n)\) and \(B_\nu(n)\) vanish; for \(\chi_4(n)=1\), the complete and central pieces remain. The prime and prime-square tests agree. |
| Raw top-scale capacity as written | **GREEN** | Complete radial mass, raw central incidences, and raw untouched negative-character far incidences each have \(R^{1/2+o(1)}\) weighted \(\ell^1\) capacity. |
| Grouped or signed lower bound inferred from capacity | **REJECTED CONTROL; not a candidate claim** | Fibre grouping, \(\chi_4\)-signs, and the nonlinear phase can cancel. Raw incidence mass is not \(\sum_m m^{-3/4}|A_\rho(m)|\), still less \(\left|\sum_m m^{-3/4}A_\rho(m)e(\sqrt{Nm})\right|\). |
| Direction of (141.C7) and (141.C38) | **GREEN** | Once the checked cell, radical, and hard-correction errors are removed, (141.C7) is an equality modulo \(O(X^\epsilon)\); hence (141.C38) is both sufficient and target-equivalent. It is not proved by (141.C7). |

I do **not** certify (141.C35), the smooth cone/Mellin construction, the literature audit, or the source comparisons (141.C36)--(141.C37). They are outside the assigned independent seams.

## 2. Exact setup and conventions under review

Write

\[
R=X^{1/4},\qquad
y=\lfloor\sqrt X\rfloor,\qquad
N=\lfloor X\rfloor=y^2+q,\qquad 0\le q\le2y,
\]

and let the effective support be

\[
1\le m\le M_*=C_VN/R^2\asymp_VR^2.
\]

For disjoint dyadic blocks

\[
\mathcal I_M=[M,2M)\cap[1,M_*],
\]

define

\[
k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
\qquad
j_m=k_m^2-Nm.
\]

The coefficient and hard cone are

\[
A_\rho(m)=
\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r\ge r_h+2}}\chi_4(r),
\qquad
C(m)=
\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\]

The exact mask threshold uses

\[
\delta_h=\left\lfloor\frac{\rho y}{\sqrt h}\right\rfloor+1,
\qquad
D_h=y-\delta_h,
\qquad
r_h=\min\left\{r\ge\frac{4Nh}{D_h^2}:r\ \text{positive odd}\right\}.
\]

For odd \(r\), least-odd minimality gives

\[
r\ge r_h+2
\iff r-2\ge\frac{4Nh}{D_h^2}
\iff(r-2)D_h^2\ge4Nh.
\]

Since \(D_h<y\) and \(N\ge y^2\), every exact far pair has \(r>4h\). Thus

\[
E_N(m)=
\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\4h<r\le r_h}}\chi_4(r)
\]

satisfies the exact identity

\[
A_\rho(m)=C(m)-E_N(m).
\]

The review interprets every Vinogradov bound on a complex scalar as a modulus bound. “Capacity” below is separately defined as an unsigned weighted incidence mass; it is never a signed scalar assertion.

## 3. Independent nearest-square, floor, and weighted rederivation

**Tie and cell endpoints.** If \(\sqrt{Nm}=\ell+1/2\) for integers \(m,\ell\), then

\[
4Nm=(2\ell+1)^2,
\]

whose left side is divisible by \(4\) and whose right side is odd. Hence there are no ties. From

\[
k\le\sqrt{Nm}+\frac12<k+1
\]

one obtains exactly

\[
\mathcal C_k=
\left[\frac{(k-1/2)^2}{N},\frac{(k+1/2)^2}{N}\right),
\qquad
|\mathcal C_k|=\frac{2k}{N}.
\]

The lower endpoint is included and the upper endpoint excluded, as claimed. On \(m\le M_*\),

\[
k_m\le\sqrt{NM_*}+\frac12
\le\sqrt{C_V}\frac NR+\frac12,
\]

so

\[
|\mathcal C_{k_m}|
\le\frac{2\sqrt{C_V}}R+\frac1N<1
\]

for large \(X\). Every physical \(m\)-cell is therefore a singleton or empty.

The phase identity is also exact:

\[
\sqrt{Nm}-k_m
=\frac{Nm-k_m^2}{\sqrt{Nm}+k_m}
=-\frac{j_m}{\sqrt{Nm}+k_m},
\]

and \(e(k_m)=1\), so

\[
e(\sqrt{Nm})
=e\!\left(-\frac{j_m}{k_m+\sqrt{Nm}}\right).
\]

On \(m\asymp M\), the window \(0<|j_m|\le\sqrt M\) therefore has phase displacement \(O(N^{-1/2})\).

**Prime-power roots.** Let

\[
\rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\},
\qquad j\ne0.
\]

For \(p^a\Vert N\), put \(b=v_p(j)\).

* If \(b<a\) is odd, there are no roots.
* If \(b=2s<a\), every root has \(v_p(k)=s\). Dividing by \(p^{2s}\) leaves a unit square-root congruence modulo \(p^{a-2s}\). It has at most two unit roots for odd \(p\), at most four for \(p=2\), and each has \(p^s\) lifts modulo \(p^a\).
* If \(b\ge a\), then \(k^2\equiv0\pmod{p^a}\), so \(p^{\lceil a/2\rceil}\mid k\), giving exactly \(p^{\lfloor a/2\rfloor}\) roots.

Thus the local root count is at most a constant \(2\) for odd \(p\), \(4\) for \(p=2\), times \(p^{\min(a,b)/2}\). The Chinese remainder theorem gives

\[
\rho_N(j)
\le4^{\omega(N)+1}\sqrt{(N,j)}
\ll_\epsilon N^\epsilon|j|^{1/2}.
\]

The same proof applies to negative \(j\).

**Injectivity.** The effective range also gives

\[
k_m\le\sqrt{C_V}\frac NR+\frac12<N
\]

for large \(X\). For a fixed \(j\), the map \(m\mapsto k_m\bmod N\) is injective: its values lie in \([0,N)\), and

\[
m=\frac{k_m^2-j}{N}.
\]

Consequently, including both signs of \(j\),

\[
\begin{aligned}
\#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
&\le\sum_{1\le|j|\le\sqrt M}\rho_N(j)\\
&\ll_\epsilon N^\epsilon
\sum_{1\le j\le\sqrt M}j^{1/2}
\ll_\epsilon N^\epsilon M^{3/4}.
\end{aligned}
\]

**All dyadic weights.** Since

\[
|A_\rho(m)|\le\tau(m)\ll_\epsilon X^\epsilon,
\qquad
|V_{\rm low}|\ll_V1,
\]

the nonzero microscopic window on one block costs

\[
\sum_{\substack{m\in\mathcal I_M\\0<|j_m|\le\sqrt M}}
m^{-3/4}|V_{\rm low}A_\rho(m)|
\ll_{\epsilon,V}
M^{-3/4}\,N^\epsilon M^{3/4}X^\epsilon
\ll_{\epsilon,V}X^\epsilon.
\]

This remains valid for \(M=1\) and for the terminal truncated block. The \(O(\log X)\) dyadic blocks are absorbed by epsilon renaming.

**Exact radicals.** Write uniquely

\[
N=Du^2,\qquad D\ \text{squarefree}.
\]

Then \(Nm\) is a square if and only if

\[
m=Dt^2.
\]

Therefore

\[
\sum_{j_m=0}m^{-3/4}|V_{\rm low}A_\rho(m)|
\ll_{\epsilon,V}
D^{-3/4}X^\epsilon\sum_{t\ge1}t^{-3/2}
\ll_{\epsilon,V}X^\epsilon.
\]

**Hard floor correction.** Since

\[
\frac{4Nh}{D_h^2}-4h
=4h\frac{q+2y\delta_h-\delta_h^2}{D_h^2}
\]

and

\[
\delta_h\le\frac{\rho y}{\sqrt h}+1,
\qquad D_h\gg_\rho y,
\]

one has

\[
\frac{4Nh}{D_h^2}-4h
\ll_\rho\sqrt h+\frac hy+1.
\]

Least-odd minimality adds less than \(2\). On \(hr\ll_Vy\) and \(r>4h\), \(h\ll_VR\), while \(r\asymp h\) throughout the correction collar. Hence

\[
\begin{aligned}
\sum_m m^{-3/4}|E_N(m)|
|V_{\rm low}(R^2m/N)|
&\ll_{\rho,V}
\sum_{h\ll_VR}h^{-3/4}
\sum_{\substack{4h<r\le r_h\\r\ \mathrm{odd}}}r^{-3/4}\\
&\ll_{\rho,V}
\sum_{h\ll_VR}(h^{-3/2}+h^{-1})
\ll_{\rho,V}\log(2X).
\end{aligned}
\]

This verifies (141.C17)--(141.C18) as a hard arithmetic correction only. It does not review the later smooth ratio cutoff or Mellin inversion.

## 4. Independent \(2\)-adic divisor-pairing rederivation

Write uniquely

\[
m=2^\nu n,\qquad n\ \text{odd}.
\]

Because \(r\) is odd, every factorization \(hr=m\) has

\[
h=2^\nu d,\qquad dr=n.
\]

Define

\[
F_\nu(d,r)=\mathbf1_{\{r\ge r_{2^\nu d}+2\}},
\qquad
A_\nu(n)=\sum_{dr=n}\chi_4(r)F_\nu(d,r).
\]

Then \(A_\rho(2^\nu n)=A_\nu(n)\). The exact far implication gives

\[
F_\nu(d,r)=1\Longrightarrow r>4\cdot2^\nu d.
\]

If both \(F_\nu(d,r)\) and \(F_\nu(r,d)\) were \(1\), then

\[
r>4\cdot2^\nu d
\quad\text{and}\quad
d>4\cdot2^\nu r,
\]

which is impossible. Hence

\[
G_\nu(d,r)=1-F_\nu(d,r)-F_\nu(r,d)
\]

is a symmetric \(0\)-\(1\) central mask. Put

\[
B_\nu(n)=\sum_{dr=n}\chi_4(r)G_\nu(d,r),
\qquad
\sigma_{\chi_4}(n)=\sum_{r\mid n}\chi_4(r).
\]

The swapped far sector is

\[
\begin{aligned}
\sum_{dr=n}\chi_4(r)F_\nu(r,d)
&=\sum_{dr=n}\chi_4(d)F_\nu(d,r)\\
&=\chi_4(n)\sum_{dr=n}\chi_4(r)F_\nu(d,r)\\
&=\chi_4(n)A_\nu(n),
\end{aligned}
\]

because \(n=dr\) is odd and

\[
\chi_4(d)=\chi_4(n)\chi_4(r).
\]

Partitioning the complete divisor fibre into the first far sector, the swapped far sector, and the central sector proves

\[
\sigma_{\chi_4}(n)
=(1+\chi_4(n))A_\nu(n)+B_\nu(n),
\]

and therefore

\[
A_\nu(n)
=\frac12\sigma_{\chi_4}(n)
-\frac12B_\nu(n)
+\mathbf1_{\{\chi_4(n)=-1\}}A_\nu(n).
\]

For \(\chi_4(n)=-1\), the involution \((d,r)\leftrightarrow(r,d)\) changes \(\chi_4(r)\) to

\[
\chi_4(d)=\chi_4(n)\chi_4(r)=-\chi_4(r).
\]

It has no fixed point, because \(d=r\) would make \(n\) a square and hence \(\chi_4(n)=1\). Thus

\[
\sigma_{\chi_4}(n)=B_\nu(n)=0,
\]

and the pairing identity is deliberately tautological on the untouched negative-character sector.

For every odd \(n\), not only the positive-character case,

\[
\sigma_{\chi_4}(n)
=\sum_{d\mid2^\nu n}\chi_4(d)
=\frac{r_2(2^\nu n)}4.
\]

When \(\chi_4(n)=1\), the pairing therefore introduces the complete radial coefficient and the exact central term:

\[
A_\nu(n)=\frac12\frac{r_2(2^\nu n)}4-\frac12B_\nu(n).
\]

It does not show that either part is target-safe.

**Prime controls.** If \(p\equiv3\pmod4\) is supported and large enough that \(F_0(1,p)=1\), then

\[
A_0(p)=\chi_4(p)=-1,
\qquad
\sigma_{\chi_4}(p)=B_0(p)=0.
\]

If \(p\equiv1\pmod4\), \(p^{2a}\) is supported, and \(X\) is large, the factors

\[
d=p^j,\qquad r=p^{2a-j}
\]

are in the first far sector for \(0\le j\le a-1\), in the swapped far sector for \(a+1\le j\le2a\), and central for \(j=a\). Indeed the nearest noncentral ratio is \(p^2\ge25\), whereas the exact threshold ratio is \(4+O_\rho(d^{-1/2}+y^{-1})\). Therefore

\[
A_0(p^{2a})=a,\qquad
\sigma_{\chi_4}(p^{2a})=2a+1,\qquad
B_0(p^{2a})=1.
\]

These controls confirm both the character direction and the central residue.

## 5. Weighted capacity and the direction of (141.C7)/(141.C38)

**Raw capacity definition.** For an incidence set \(\mathcal S\), define its top-block weighted capacity by

\[
\operatorname{Cap}_M(\mathcal S)
=\sum_{\substack{(d,r)\in\mathcal S\\M\le dr<2M}}(dr)^{-3/4}.
\]

Choose \(M=cR^2\) with fixed sufficiently small \(c>0\), so the argument of \(V_{\rm low}\) lies where \(V_{\rm low}=1\).

The universal divisor-incidence upper bound is

\[
\operatorname{Cap}_M(\text{all incidences})
\ll M^{-3/4}\sum_{m\asymp M}\tau(m)
\ll M^{1/4}\log(2M)
=R^{1/2+o(1)}.
\]

For far incidences one obtains the same ledger directly:

\[
\sum_{h\ll\sqrt M}h^{-3/4}
\sum_{4h<r\ll M/h}r^{-3/4}
\ll M^{1/4}\sum_{h\ll\sqrt M}\frac1h
\ll M^{1/4}\log(2M).
\]

Matching lower capacities are elementary.

* For the complete radial coefficient, the lattice count
  \[
  \sum_{m\le T}r_2(m)=\pi T+O(\sqrt T)
  \]
  gives complete top-block weighted mass \(\asymp M^{1/4}\asymp R^{1/2}\).
* For raw central incidences, take odd \(d,r\) in sufficiently narrow fixed comparable intervals \([aR,(1+\eta)aR]\), with \(a,\eta>0\) chosen so their products lie in \([M,2M)\). Neither far mask can hold, because each far implication requires a ratio \(>4\). There are \(\asymp R^2\) ordered pairs, each of weight \(\asymp R^{-3/2}\), hence capacity \(\asymp R^{1/2}\).
* For raw untouched negative-character far incidences, take odd
  \[
  d\in[aR,(1+\eta)aR],\qquad
  r\in[16aR,(16+\eta)aR],
  \]
  with \(a,\eta>0\) chosen so their products lie in one top dyadic block where \(V_{\rm low}=1\). The hard threshold estimate above makes \(F_0(d,r)=1\) for large \(X\). A positive proportion of these pairs satisfy \(\chi_4(dr)=-1\). Again there are \(\asymp R^2\) pairs of weight \(\asymp R^{-3/2}\), giving \(\asymp R^{1/2}\).

This proves exactly the candidate's expressly raw \(R^{1/2+o(1)}\) \(\ell^1\)-capacity claim. For the central and negative sectors, the count is before summing \(\chi_4(r)\) over a fibre. Even the complete coefficient, though nonnegative, is multiplied by a rotating square-root phase in the scalar. None of these three capacities proves

\[
\sum_{m\asymp M}m^{-3/4}|A_\rho(m)|\gg R^{1/2},
\]

and none proves

\[
\left|
\sum_{m\asymp M}
m^{-3/4}A_\rho(m)e(\sqrt{Nm})
\right|\gg R^{1/2}.
\]

The first inference is not supplied for raw central or untouched negative-character far incidences; the second is invalid without a signed phase theorem. The repaired candidate makes neither inference and explicitly calls its resonance an obstruction rather than a lower bound. This rejected control confirms the required raw-capacity/signed-lower-bound separation.

**Direction of the strict reduction.** Decompose the exact scalar into:

1. nonzero microscopic cells \(0<|j_m|\le\sqrt M\);
2. exact radicals \(j_m=0\);
3. the complement \(|j_m|>\sqrt M\).

Section 3 gives \(O(X^\epsilon)\) for the first two parts with the actual coefficient \(A_\rho\). On the complement,

\[
A_\rho=C-E_N,
\]

and the full weighted \(E_N\)-mass is \(O(X^\epsilon)\). Therefore

\[
\mathfrak T_N
=
\sum_M
\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
+O(X^\epsilon).
\]

This is exactly (141.C7). Let the displayed survivor be \(\mathcal S_N\). Then

\[
\mathfrak T_N=\mathcal S_N+O(X^\epsilon).
\]

Consequently,

\[
|\mathcal S_N|\ll X^\epsilon
\Longrightarrow
|\mathfrak T_N|\ll X^\epsilon,
\]

and conversely

\[
|\mathfrak T_N|\ll X^\epsilon
\Longrightarrow
|\mathcal S_N|\ll X^\epsilon.
\]

Thus (141.C38) is the remaining target-equivalent estimate, not a consequence already established by (141.C7). The word “strict” should be read as an owner-complete removal of explicitly target-safe channels, not as a claim that the removed set is nonempty for every centre.

## 6. First doubtful step, controls, and dependencies

The repaired capacity sentence following (141.C28) is **GREEN as written**. It explicitly names “raw central incidences” and “raw untouched negative-character far incidences,” then calls the result a complete-fibre/central self-return rather than a target-safe split. The candidate later states that the resonance is “not a lower bound” for (141.C7), is not promoted to a fixed-centre lower bound, and rejects treating capacity as a signed lower bound.

The first genuinely unproved mathematical step is therefore precisely (141.C38):

\[
\left|
\sum_M
\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\right|
\ll_\epsilon X^\epsilon.
\]

The singleton property gives no intra-cell cancellation. The root count spends its full elementary power at \(|j|=\sqrt M\). Pairing is tautological for \(\chi_4(n)=-1\) and introduces a complete coefficient plus a central band for \(\chi_4(n)=1\). Raw capacity shows that neither remaining sector can be discarded by modulus, but it does not prove a signed lower bound. These facts identify the obstruction without resolving it.

Controls completed analytically, with no numerical experiment, were:

* half-integer tie and half-open endpoint convention;
* physical cell length and singleton multiplicity;
* every prime-power root case, including \(p=2\);
* \(k<N\) and fixed-\(j\) injectivity;
* both signs of \(j\), every dyadic block, \(M=1\), and the terminal block;
* the exact-radical parameterization \(m=Dt^2\);
* the hard floor-correction weight;
* unique \(2\)-adic factorization;
* swapped-mask character direction and disjointness;
* \(\chi_4(n)=\pm1\), large \(p\equiv3\pmod4\), and \(p^{2a}\) with \(p\equiv1\pmod4\);
* raw upper and lower capacity versus grouped and signed quantities;
* both logical directions between (141.C7) and (141.C38).

Dependencies used were exactly:

* `protocol.md`;
* `state/active_campaign.yml`;
* the relevant entries of `state/proof_obligations.yml` for the global lower-radial signed estimate, post-collar far-alias reduction, rank-one product-fibre obstruction, phase diagram, and exact-radical channel;
* `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`.

Artifact control now passes: the candidate has zero carriage returns and zero other disallowed control bytes. Its repaired oddness conditions in (141.C2)/(141.C4) are valid TeX, and its capacity language contains both required raw-incidence qualifications.

## 7. Recommended state effect

**Promote, after independent reviews close, the following narrow facts:**

* the exact no-tie nearest-square cells and their singleton property, (141.C15)--(141.C16);
* the nonzero quadratic-congruence root bound and microscopic weighted count, (141.C19)--(141.C21);
* the exact-radical \(m=Dt^2\) channel and its \(O(X^\epsilon)\) mass, (141.C22);
* the \(2\)-adic decomposition, disjoint swapped masks, and identities (141.C26)--(141.C28);
* the target-equivalence of (141.C7) and (141.C38), conditional only on the explicitly checked cell, radical, and hard-correction estimates.

Record the capacity fact only as:

> The complete radial coefficient, the raw central incidences, and the raw untouched negative-character far incidences have top-scale weighted \(\ell^1\) capacity \(R^{1/2+o(1)}\).

Retain as a rejected control any inference from this raw capacity to a grouped coefficient, an individual complex branch, or the signed fixed-centre scalar. The candidate already rejects that inference. Leave (141.C38) open. Pairing neither controls the negative-character sector nor proves the central band target-safe.

The assigned candidate repairs are complete, so this review recommends unqualified GREEN promotion of the assigned seams after the remaining independent reviews close. Make no state change based on (141.C35)--(141.C37) from this review: the smooth cone, Mellin, and source-audit seams were intentionally not certified here. No lower-GAR, M1, M2, endpoint, M9, quarter, or exponent claim is licensed.

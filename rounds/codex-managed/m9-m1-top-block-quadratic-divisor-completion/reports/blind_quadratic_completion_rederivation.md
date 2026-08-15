# Blind rederivation: additive completion and reciprocal dual strip

## 1. Result

**Exact projector and stationary geometry, but no proved square-root
estimate.** The additive projector in (59.3) is correct:

\[
 {\bf1}_{h\mid n}\chi_4(n/h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)
 e\!\left({an\over4h}\right).                               \tag{1}
\]

After a coefficient-preserving one-dimensional Poisson/B-process in
\(n\), the stationary variables

\[
 r=4hk-a,\qquad n_*(h,r)={4Xh^2\over r^2}                  \tag{2}
\]

produce the phase

\[
 {Xh\over r}-{1\over8},                                     \tag{3}
\]

because the primal second derivative is negative. The exact stationary
normalization is

\[
 -{i\over2h}\,{e(-1/8)\over\sqrt{|f''(n_*)|}}
 =-2\sqrt2\,e(1/8){X^{1/2}h^{1/2}\over r^{3/2}},            \tag{4}
\]

where
\[
 f(n)=\sqrt{Xn}+{an\over4h},\qquad
 |f''(n_*)|={r^3\over32Xh^3}.
\]

Since \(h\asymp R\), \(r\asymp R^2\), and \(X\asymp R^4\), (4) has size
\(\asymp R^{-1/2}\). Also
\(\chi_4(a)=\chi_4(-r)=-\chi_4(r)\), so the stationary main term is

\[
 2\sqrt2\,e(1/8)\sum_{h}\sum_{r\in\mathcal R_h}^{*}
 \chi_4(r){X^{1/2}h^{1/2}\over r^{3/2}}
 \widetilde\Omega_X(h,r)
 e\!\left({Xh\over r}\right),                               \tag{5}
\]

up to separately owned endpoint and transform-remainder terms.
Here \(\mathcal R_h\) is the exact cone
\[
 2h\sqrt{X/B}\le r\le2h\sqrt{X/A},
\]
and \(\widetilde\Omega_X(h,r)\) is the original exact symbol evaluated
at \(n_*(h,r)\), with any lawful cutoff partition and stationary
corrections still attached.

For any integer shear \(K\), setting \(r=4Kh+s\) retains the character
exactly:
\[
 \chi_4(r)=\chi_4(s),
\]
and gives
\[
 \Phi_K(h,s)={Xh\over4Kh+s},\qquad
 \det\nabla^2\Phi_K(h,s)=-{X^2\over(4Kh+s)^4}.               \tag{6}
\]

The determinant is nonzero and \(\asymp-1\). On the sheared strip
\(h,K\asymp R\), \(|s|\ll R\), and \(4Kh+s\asymp R^2\),

\[
 \Phi_{hh}=O(1),\qquad
 \Phi_{hs}\asymp1,\qquad
 \Phi_{ss}\asymp R^{-1},                                    \tag{7}
\]

with \(\Phi_{hh}\asymp1\) when \(|s|\asymp R\) but
\(\Phi_{hh}=0\) at \(s=0\). Since the determinant is uniformly
\(\asymp-1\) and the trace is \(O(1)\), the two eigenvalues have opposite
signs and magnitudes \(\asymp1\) throughout the strip. This
nondegenerate indefinite local geometry alone does not provide the
required lattice theorem for the moving strip and actual symbol.

The raw dual strip contains \(\asymp R^2\) lattice points. Termwise
absolute summation gives \(R^2\); after the \(R^{-1/2}\) factor in (4)
this is \(R^{3/2}\), while the primal target is \(\sqrt R\). To close the
target, one must prove the genuinely signed raw estimate

\[
 \sum_{h\asymp R}\sum_{s\in\mathcal S_h}^{*}
 \chi_4(s)W_X(h,s)e(\Phi_K(h,s))
 \ll_\varepsilon X^\varepsilon R.                           \tag{8}
\]

No applicable lattice theorem or amplitude regularity sufficient for
(8) is supplied. Moreover at \(X=L^4\), the dual phase has integral and
quarter-frequency coherent leading terms, so a first-derivative or
determinant-only argument is invalid. Additive completion and the
B-process therefore expose an equivalent-hard reciprocal kernel; they do
not prove the desired cancellation.

## 2. Exact statement and hypotheses

The projector (1) uses \(\chi_4(a)=0\) for even \(a\). The exact completed
physical expression is

\[
 P_J=-{i\over2}\sum_{R/4<h\le R/2}{1\over h}
 \sum_{a\bmod4h}\chi_4(a)
 \sum_{n\in J}^{*}\Omega_X^*(n,h)
 e\!\left(\sqrt{Xn}+{an\over4h}\right).                     \tag{9}
\]

To state a lawful B-process, first decompose the exact \(n\)-amplitude
into finitely many pieces:

1. smooth interior pieces supported strictly inside the real interval
   corresponding to \(J\);
2. one-sided hard-top pieces;
3. inherited radial and angular equality values;
4. artificial \(A,B\) cutoff endpoints with full ownership.

For a smooth interior amplitude \(w_h(n)\), Poisson summation gives

\[
 \sum_{n\in\mathbb Z}w_h(n)e(f_{h,a}(n))
 =\sum_{k\in\mathbb Z}\int_{\mathbb R}
 w_h(x)e(f_{h,a}(x)-kx)\,dx,                                \tag{10}
\]

where
\[
 f_{h,a}(x)=\sqrt{Xx}+{a x\over4h}.
\]
For each \(k\), there is at most one critical point. The stationary range
is exactly
\[
 \mathcal R_h=
 \{r\in\mathbb Z:2h\sqrt{X/B}\le r\le2h\sqrt{X/A}\},         \tag{11}
\]
with inherited half-weights only when the corresponding stationary point
belongs to an inherited equality convention. Artificial transform
endpoints are not automatically half-weighted; their endpoint integrals
and any stationary endpoint convention must be derived from the chosen
partition.

The symbol in (5) cannot simply be denoted by an arbitrary bounded
sequence. At minimum it contains

\[
 \Omega_X^*(n_*,h)=
 \sum_j{\bf1}_{h\le\lfloor D_jX^{-1/4}\rfloor}
 \Phi\!\left({h\over\lfloor D_jX^{-1/4}\rfloor+1}\right)
 \left[w_j(r)\right]^*,                                     \tag{12}
\]

because
\[
 2h\sqrt{X/n_*}=r.
\]
Thus the B-process converts the angular coordinate exactly into the
integer dual coordinate \(r\). Height floors remain functions of \(h\);
profile and hard/equality seams become seams in \(r\). Formula (12) is
one precise reason the dual symbol is not generic smooth data.

## 3. Proof, strip geometry, and capacity ledger

### Projector constant

Let
\[
 S_h(n)=\sum_{a\bmod4h}\chi_4(a)e(an/(4h)).
\]
Write the odd residues uniquely as \(a=b+4j\), with
\(b\in\{1,3\}\) and \(0\le j<h\). Then
\[
\begin{aligned}
 S_h(n)
 &=\sum_{b\in\{1,3\}}\chi_4(b)e(bn/(4h))
 \sum_{j=0}^{h-1}e(jn/h).
\end{aligned}
\]
The \(j\)-sum is zero unless \(h\mid n\). If \(n=hm\), it equals \(h\),
and
\[
\begin{aligned}
 S_h(hm)
 &=h\{e(m/4)-e(3m/4)\}\\
 &=2ih\,\chi_4(m).
\end{aligned}
\]
Therefore \((-i/(2h))S_h(n)\) is exactly
\({\bf1}_{h\mid n}\chi_4(n/h)\), proving (1).

Residue by residue:

| \(m=n/h\bmod4\) | \(S_h(hm)\) | \((-i/(2h))S_h(hm)\) |
|---:|---:|---:|
| \(0\) | \(0\) | \(0\) |
| \(1\) | \(2ih\) | \(1\) |
| \(2\) | \(0\) | \(0\) |
| \(3\) | \(-2ih\) | \(-1\) |

This also proves that no smooth character extension is present.

### Stationary phase and normalization

The phase in the \(k\)-th integral in (10) is
\[
 F(x)=\sqrt{Xx}+{a x\over4h}-kx.
\]
Stationarity is
\[
 {\sqrt X\over2\sqrt x}+{a\over4h}=k.
\]
With \(r=4hk-a\), this gives (2). At the critical point,
\[
\begin{aligned}
 F(n_*)&={Xh\over r},\\
 F''(n_*)&=-{\sqrt X\over4n_*^{3/2}}
          =-{r^3\over32Xh^3}.                               \tag{13}
\end{aligned}
\]

Direct substitution gives the denominator \(32\). Hence

\[
 {1\over\sqrt{|F''(n_*)|}}
 ={4\sqrt2\,X^{1/2}h^{3/2}\over r^{3/2}},                  \tag{14}
\]

and the projector-normalized stationary coefficient is

\[
 -{i\over2h}\,{e(-1/8)\over\sqrt{|F''(n_*)|}}
 =-2\sqrt2\,e(1/8){X^{1/2}h^{1/2}\over r^{3/2}}.            \tag{15}
\]

Here the stationary Gaussian factor is \(e(-1/8)\), since \(F''<0\), and
\(-i=e(-1/4)\). Formula (15), including its phase and \(2\sqrt2\), is the
correct coefficient for the convention \(e(t)=e^{2\pi it}\).
Multiplying by
\[
 \chi_4(a)=-\chi_4(r)
\]
changes the sign, so the interior stationary main term is

\[
 2\sqrt2\,e(1/8)
 \sum_h\sum_{r\in\mathcal R_h}^{*}
 \chi_4(r){X^{1/2}h^{1/2}\over r^{3/2}}
 \Omega_X^*(n_*(h,r),h)e(Xh/r),                             \tag{16}
\]

before higher stationary corrections and boundary terms.

The scaling remains the one stated in section 1:
\[
 {X^{1/2}h^{1/2}\over r^{3/2}}\asymp R^{-1/2}.              \tag{17}
\]

The map from \((a,k)\) to \(r\) is one-to-one: for every integer \(r\),
there is a unique \(a\in\{0,\ldots,4h-1\}\) with
\(a\equiv-r\pmod{4h}\), and then \(k=(r+a)/(4h)\in\mathbb Z\).
Thus no extra multiplicity or factor \(4h\) appears.

Nonstationary \(k\)'s, critical points within a transition width of
\(A,B\), hard-profile seams, equality samples, and errors in replacing
the oscillatory integral by (14) are not bounded by the algebra above.
They must remain separate remainder terms.

### Sheared strip and Hessian

Choose an integer \(K\asymp R\) and write \(r=4Kh+s\). The exact phase is
\[
 \Phi_K(h,s)={Xh\over u},\qquad u=4Kh+s.
\]
Its first derivatives are
\[
 \Phi_h={Xs\over u^2},\qquad
 \Phi_s=-{Xh\over u^2},
\]
and its Hessian is
\[
 \nabla^2\Phi_K={X\over u^3}
 \begin{pmatrix}
 -8Ks&4Kh-s\\
 4Kh-s&2h
 \end{pmatrix}.                                             \tag{18}
\]
Therefore
\[
\begin{aligned}
 \det\nabla^2\Phi_K
 &={X^2\over u^6}
 \{-16Khs-(4Kh-s)^2\}\\
 &=-{X^2(4Kh+s)^2\over u^6}
 =-{X^2\over u^4},                                         \tag{19}
\end{aligned}
\]
which proves (6).

Although the strip length in \(r\) is \(\asymp R\) for each
\(h\asymp R\), the assertion \(|s|\ll R\) for one fixed \(K\) is not a
consequence of the packet as written. The central slope
\[
 {r\over h}\asymp2\sqrt{X/N}\asymp R
\]
varies by \(O(1)\) when the center \(N\) moves by \(O(R)\), which becomes
an \(O(R)\) shift after multiplication by \(h\). Thus \(|s|\ll R\) is
valid after choosing \(4K\) within \(O(1)\) of the actual central slope.
The packet's stronger phrase “within \(2\)” is enough for this scale, but
an integer multiple \(4K\) need not lie within \(2\) of an arbitrary real
number: the nearest multiple of four can be at distance exactly \(2\),
so “within \(2\)” is valid with non-strict inequality. Formula (59.8)
also says \(K\asymp R\), consistently.

On \(h,K\asymp R\), \(|s|\ll R\), \(u\asymp R^2\), and
\(X\asymp R^4\), (18) gives
\[
 \Phi_{hh}=O(1),\qquad
 \Phi_{hs}\asymp1,\qquad
 \Phi_{ss}\asymp R^{-1}.                                   \tag{20}
\]
More exactly,
\(\Phi_{hh}=-8KXs/u^3\asymp-s/R\), so it vanishes at \(s=0\)
and is \(O(1)\) throughout \(|s|\ll R\);
\(\Phi_{hs}=X(4Kh-s)/u^3\asymp1\); and
\(\Phi_{ss}=2Xh/u^3\asymp R^{-1}\).
Together with determinant \(\asymp-1\), this gives opposite-sign
eigenvalues, each of magnitude \(\asymp1\), uniformly for
\(|s|\ll R\). The remaining issue is
arithmetic lattice coherence and the nonsmooth moving amplitude; rank
alone does not yield the raw \(O(R)\) estimate.

The exact sheared character is
\[
 \chi_4(r)=\chi_4(4Kh+s)=\chi_4(s).                         \tag{21}
\]
The transformed support is
\[
 \mathcal S_h=
 \{s\in\mathbb Z:2h\sqrt{X/B}-4Kh
 \le s\le2h\sqrt{X/A}-4Kh\},                                \tag{22}
\]
with length \(\asymp R\) and moving endpoints. Profile seams in (12)
become fixed or starred \(s\)-locations only after the shear is inserted;
they may not be discarded.

### Perfect fourth powers and raw target

Let \(X=L^4\) and write \(n=L^2+t\). The primal radial phase is
\[
 L^2\sqrt{L^2+t}
 =L^3+{L\over2}t-{t^2\over8L}+O(t^3/L^3).                 \tag{23}
\]
The linear term is integral or half-integral on integer \(t\), and the
additive projector contributes the rational quarter-frequency
\(an/(4h)\). Hence no uniform first-derivative gap exists.

The same coherence survives on the dual side. If the central dual ratio
is exactly \(r=4Kh\), then
\[
 \Phi_K(h,0)={X\over4K},
\]
independent of \(h\). More generally, for \(|s|\ll R\),
\[
\begin{aligned}
 \Phi_K(h,s)
 &={X\over4K}
 -{Xs\over16K^2h}
 +{Xs^2\over64K^3h^2}
 +O\!\left({X|s|^3\over K^4h^3}\right).                    \tag{24}
\end{aligned}
\]
The \(s=0\) line is fully coherent geometrically, although
\(\chi_4(0)=0\); the neighboring odd \(s\) lines retain rational
quarter-character structure. Thus the character removes the exact
zero line but does not furnish a quantitative gap on its neighbors.

The dual capacity ledger is:

| Object | Number/size | Absolute capacity |
|---|---:|---:|
| stationary \((h,r)\) or \((h,s)\) points | \(\asymp R^2\) | \(R^2\) raw |
| stationary coefficient | \(R^{-1/2}\) | \(R^{3/2}\) physical |
| required raw dual estimate | — | \(X^\varepsilon R\) |
| resulting physical target | \(R^{-1/2}\cdot R\) | \(X^\varepsilon\sqrt R\) |

Taking absolute values over \(a,k,r,h\), or \(s\), spends the necessary
factor \(R\). The exact algebra supplies no bound between \(R\) and
\(R^2\) for the raw sum. The determinant (19) is not such a bound.

## 4. First doubtful or unproved step

The projector, critical point, phase, Gaussian normalization, one-to-one
\((a,k)\leftrightarrow r\) map, strip support, character transformation,
and Hessian determinant are exact after the corrections recorded above.

The first analytic step not justified by the packet is the uniform
coefficient-preserving B-process with the actual nonsmooth symbol:
one must prove that the smooth stationary main term (16) has total
remainder \(O_\varepsilon(X^\varepsilon\sqrt R)\) after summing over
\(h,a,k\), while separately retaining the hard top, height-floor seams,
profile equality values, inherited radial stars, and artificial
endpoints. The ordinary single-integral stationary formula does not
provide that summed remainder automatically.

Even if this transform theorem is granted, the decisive unproved step is
the raw signed strip estimate (8). The packet supplies no source whose
hypotheses match the reciprocal phase, moving strip, \(\chi_4(s)\),
actual transformed amplitude, seams, and uniform perfect-fourth-power
range. No source applicability claim is made.

Nor is an exact return to Hardy/GAR or the original M1 kernel proved.
The identity
\[
 2h\sqrt{X/n_*}=r
\]
shows a structural return of the angular coordinate as the dual integer,
but analogy alone does not identify the transformed weights, endpoints,
normalization, or downstream operator.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| projector_constant | **Pass.** Equation (1) and the residue table verify the factor \(-i/(2h)\), including residues \(0,1,2,3\). |
| Bprocess_normalization | **Pass after correction.** Equations (13)--(17) give \(F''=-r^3/(32Xh^3)\), Gaussian \(e(-1/8)\), coefficient \(2\sqrt2e(1/8)X^{1/2}h^{1/2}r^{-3/2}\), and size \(R^{-1/2}\). |
| dual_strip_geometry | **Pass.** Equations (11), (21)--(22) give the one-to-one \(r\)-cone, shear, moving endpoints, and exact character. |
| Hessian_and_rank | **Pass after scale correction.** Here \(r\asymp R^2\), while \(h,K\asymp R\) and \(|s|\ll R\). Equation (19) verifies determinant \(-X^2/r^4\asymp-1\); (20) gives entries \(O(1),\asymp1,\asymp R^{-1}\) and two opposite-sign eigenvalues of magnitude \(\asymp1\). Rank alone supplies no lattice estimate. |
| character_resonance | **Obstruction retained.** The exact coherent \(s=0\) line is killed by \(\chi_4(0)\), but neighboring odd lines and quarter frequencies have no proved gap. |
| actual_amplitude | **Open transform seam.** Equation (12) shows the angular coordinate becomes \(r\), while height floors and profile/hard/star seams remain. No arbitrary bounded-sequence substitution is made. |
| endpoints_and_stars | **Open transform seam.** Artificial \(A,B\) endpoints, hard top, equality samples, and nonstationary frequencies are separately listed; no new half-weight is invented. |
| perfect_fourth_power | **Pass.** Equations (23)--(24) retain primal integral/half-integral linear terms, the critical quadratic term, and dual coherence. |
| target_ledger | **No-go passed.** Raw absolute capacity is \(R^2\); the required raw bound is \(R\), and stationary normalization converts it exactly to the \(\sqrt R\) target. |
| source_applicability | **No source invoked.** No theorem matching the moving reciprocal strip and actual symbol is available in the permitted packet. |
| downstream_scope | **Pass.** The lower sector, alpha connector, height limits, full shifted correlation, GAR, M9-M1, M9, and final target are not inferred. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The Round-59 packet's primal object, target, projector candidate,
   stationary variables, cone, shear, and symbol conventions.
2. Finite Fourier/Gauss-sum algebra modulo \(4h\), Poisson summation for a
   smooth compactly supported piece, and one-dimensional stationary phase
   with \(e(t)=e^{2\pi it}\).
3. Direct differentiation and elementary Taylor expansion.

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/briefs/blind_quadratic_completion_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/derivation_packet.md.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  validation matrices, or any other Round-59 report or artifact.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Promote the corrected exact algebra after seam review; retain the
analytic route as open.** Promote candidate identities (1)--(2),
(11)--(22), especially the corrected
\[
 F''(n_*)=-{r^3\over32Xh^3},\qquad
 2\sqrt2e(1/8){X^{1/2}h^{1/2}\over r^{3/2}},
\]
the exact determinant, corrected order-one indefinite eigenvalue ledger, and raw
\(R^2\)-versus-\(R\) capacity gap. Do not promote a B-process remainder
theorem, the raw strip estimate (8), an exact return to GAR/M1, or any
downstream conclusion.

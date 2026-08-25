# Round 147 source and method strategy: the mandatory \(t=1\) squarefree cone

## 1. Result

**Strategy-level result: one exact factorization, one promising borderline transform, and no source-complete estimate.**  At the closing graph SHA-256

```text
1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5
```

the unmasked Round-146 reduction makes the \(t=1\) face mandatory.  Its ratio-Mellin Dirichlet series does factor exactly as

\[
 \mathcal Z_{\rm sf}(w,z)
 =\zeta(w+z)L(w-z,\chi _4)G(w,z),
\tag{147.S1}
\]

up to the entire scalar \(4^{-z}\) coming from the ratio \(e/(4d)\).  The Euler product \(G\) is absolutely convergent whenever

\[
 \Re(w+z)>\frac12,\qquad \Re(w-z)>\frac12.
\tag{147.S2}
\]

Thus the proposed generalized-divisor/Vorono\u00ef route is structurally legitimate for the **complete** \(\zeta L\) factor.  It does not yet apply to the exact scalar.  No audited primary theorem simultaneously supplies

1. the level-\(4\), \(\chi _4\)-twisted generalized divisor coefficient with complex shift;
2. a compactly supported smooth radial test carrying the fixed individual phase \(e(+\sqrt{Nx})\);
3. estimates uniform through the ratio-Mellin range \(|\Im z|\lesssim D^{1/2}X^\varepsilon\) after target-safe cone smoothing (or \(|\Im z|\gtrsim D\) for the hard cone); and
4. the powerful-number convolution contributed by \(G\), without taking an owner-sized triangle inequality.

The closest exact cards split these hypotheses: Banerjee--Khurana has the shifted level-\(q\) character coefficient but requires an analytic test; Topacogullari has a level-character formula for \(C_c^\infty\) tests but only the unshifted coefficient; Goldfeld--Huang has a \(C_c^\infty\) complex-spectral formula but only for the level-one untwisted generalized divisor; Kaneko supplies the complex-shift Estermann functional equation, not the required uniform fixed-centre bound.

There is a useful correction to the proposed resonance location.  A kernel

\[
 J_\nu\!\left(4\pi\sqrt{nx/q}\right)
\]

has branches \(e(\pm2\sqrt{nx/q})\), so against \(e(+\sqrt{Nx})\) its negative branch resonates at

\[
 n_0=\frac{qN}{4}.
\tag{147.S3}
\]

Hence \(n=N/4\) is the level-one normalization.  In the literal Banerjee--Khurana theorem with \(\chi _4\) of conductor \(q=4\), the resonance is \(n=N\).  Any Round-147 formula must freeze its cusp/conductor normalization before using either value.

For the complete \(\zeta L\) coefficient, the resonant absolute capacity is exactly borderline at the top block, not power-saving.  The squarefree Euler convolution then loses \(R^{1/4+o(1)}\) under the best elementary triangle split.  Therefore there is no improvement to the accepted global exponent.  The mathematically distinct object worth freezing is a **powerful-convolution resonant Vorono\u00ef inequality**, stated in Section 2.5.

## 2. Exact statement and hypotheses

### 2.1 Exact face and target

Round 146 proves

\[
 \kappa _1(d,e)=
 \mathbf 1_{\{\mu ^2(de)=1\}}
 \mathbf 1_{\{e\ {\rm odd}\}}\chi _4(e)
 \mathbf 1_{\{e>4d\}}.
\tag{147.S4}
\]

For every inherited half-open prefix \(M\le U\le B_M\), the separate-face target is therefore

\[
 \boxed{
 S^{(1)}_{M,N}(U):=
 \sum_{\substack{M\le de<U\\
                  \mu ^2(de)=1,\ e\ {m odd},\ e>4d}}
 (de)^{-3/4}V_{\rm low}(R^2de/N)\chi _4(e)
 e(+\sqrt{Nde})
 \ll_{\varepsilon,V}X^\varepsilon .}
\tag{147.S5}
\]

Equivalently, after partial summation, the unweighted prefix must be
\(\ll M^{3/4}X^\varepsilon\).  On the balanced top block

\[
 M\asymp R^2,\quad N\asymp R^4,\quad d\asymp e\asymp R,
\tag{147.S6}
\]

there are \(R^{2+o(1)}\) raw pairs, the physical weight is \(R^{-3/2}\), the raw target is \(R^{3/2+o(1)}\), and the normalized trivial capacity is \(R^{1/2+o(1)}\).

### 2.2 Target-safe cone smoothing and Mellin range

On a boundary box \(d\asymp D\), \(e\asymp E\asymp D\), smooth \(\mathbf 1_{e>4d}\) across relative ratio width \(D^{-1/2}\).  For each \(d\) this changes \(O(D^{1/2})\) possible \(e\)'s, hence \(O(D^{3/2})\) pairs.  Since \((de)^{-3/4}\asymp D^{-3/2}\), the weighted error is \(O(X^\varepsilon)\).  This is target-safe, though it is not negligible.

The smoothed ratio transform has effective range

\[
 |\Im z|\lesssim D^{1/2}X^\varepsilon;
\tag{147.S7}
\]

the hard Perron cutoff must distinguish \(e=4d+1\) and therefore needs height \(\gtrsim D\).  At the top, these are respectively \(R^{1/2}X^\varepsilon\) and \(R\).  The radial Mellin frequency of \(e(+\sqrt{Nu})\), if that variable is also Mellin transformed, is \(\asymp\sqrt{NM}\asymp R^3\).

### 2.3 Exact Euler product

With \(u=de\), ratio \(v=e/(4d)\), and Mellin monomial \(u^{-w}v^z\), the arithmetic factor is \(4^{-z}\mathcal Z_{\rm sf}(w,z)\), where

\[
 \mathcal Z_{\rm sf}(w,z)
 =\sum_{d,e\ge1}
 \frac{\mu ^2(de)\mathbf 1_{e\ {\rm odd}}\chi _4(e)}
      {d^{w+z}e^{w-z}}.
\tag{147.S8}
\]

Initially for \(\Re(w\pm z)>1\),

\[
 \mathcal Z_{\rm sf}(w,z)
 =(1+2^{-(w+z)})
 \prod_{p\ {m odd}}
 \left(1+p^{-(w+z)}+\chi _4(p)p^{-(w-z)}\right).
\tag{147.S9}
\]

Writing \(a=p^{-(w+z)}\) and \(b=\chi _4(p)p^{-(w-z)}\), (147.S1) holds with

\[
 G_2(w,z)=1-2^{-2(w+z)},
\qquad
 G_p(w,z)=(1+a+b)(1-a)(1-b)
 =1-a^2-b^2-ab+a^2b+ab^2.
\tag{147.S10}
\]

Every nonconstant odd-prime term has total prime exponent at least two.  This proves absolute convergence in (147.S2).  If

\[
 G(w,z)=\sum_{r\ge1}g_z(r)r^{-w},
\tag{147.S11}
\]

then \(g_z(r)\) is supported on powerful integers (every prime divisor has exponent at least two).  The complete factor has coefficient

\[
 A_z(n):=\sum_{de=n}\chi _4(e)(e/d)^z
 =n^{-z}\sigma _{2z,\chi _4}(n)
 =n^z\bar\sigma _{-2z,\chi _4}(n),
\tag{147.S12}
\]

and the exact squarefree coefficient is \(g_z*A_z\).  Absolute convergence of \(G\) in a Mellin half-plane is not an unweighted \(\ell ^1\) estimate for this physical convolution.

### 2.4 Exact candidate theorem cards

**Banerjee--Khurana, Theorem 4.3.**  For an odd primitive character \(\chi\pmod q\), nonintegral \(0<\alpha<\beta\), a function analytic inside a closed contour strictly containing \([\alpha,\beta]\), and \(0<\Re\nu<1/2\), the theorem transforms

\[
 \sum_{\alpha<j<\beta}\frac{\bar\sigma_{-\nu,\chi}(j)}j f(j)
\]

to a main integral and a dual series with coefficient
\(\sigma_{-\nu,\bar\chi}(n)n^{\nu/2}\) and \(J_\nu,Y_\nu,K_\nu\) evaluated at \(4\pi\sqrt{nt/q}\).  Taking \(\chi=\chi _4\), \(\nu=2z\), and replacing its test by \(j^{z+1}F(j)\) matches (147.S12).  The first mismatch is that the exact radial/dyadic test is nonzero \(C_c^\infty\), hence cannot be analytic on a complex neighborhood while retaining compact support.  The theorem is an identity for each fixed \(\nu\); it states no uniform transform estimate for the growing range (147.S7), no endpoint/prefix seminorm ledger, and no estimate after convolution by (147.S11).

**Kaneko, Theorem 3.1.**  For primitive \(\psi\pmod q\), \(h,\ell\ge1\), \((h,\ell q)=1\), the twisted Estermann series

\[
 D_\psi(s,\xi;h/(\ell q))
 =\sum_{n\ge1}\sigma_\xi(n,\psi)e_{\ell q}(hn)n^{-s}
\]

has the displayed meromorphic continuation and functional equation, with both dual signs, gamma factors, and conductor \(\ell q\).  It is a valid complex-\(\xi\) algebraic source, but it is not a fixed-centre estimate, is stated for an additive twist rather than the untwisted face (147.S5), and supplies neither the uniform Bessel analysis nor the \(G\)-convolution inequality.

**Topacogullari, Theorem 2.3.**  For primitive \(\chi_i\pmod {q_i}\), coprime \(a,c\), and \(f\in C_c^\infty(0,\infty)\), it gives a character-level Vorono\u00ef formula for the unshifted complete coefficient

\[
 \tau_{\chi _1,\chi _2}(n)=\sum_{d\mid n}\chi _1(d)\chi _2(n/d).
\]

With the trivial character modulo one and \(\chi _4\), this covers only \(A_0(n)\).  It does not cover \(A_{c+iv}\) throughout (147.S7).

**Goldfeld--Huang, Lemma 3.12.**  For \(g\in C_c^\infty(\mathbb R_+)\), \((a,c)=1\), and

\[
 \eta_{it}(n)=\sum_{uv=n}(u/v)^{it},
\]

it gives the level-one Eisenstein Vorono\u00ef formula with \(J^+_{2it},K^+_{2it}\) at \(4\pi\sqrt{nx}/c\).  This verifies that compact smooth testing and a complex spectral parameter coexist in the untwisted level-one model, but not with the level-\(4\) \(\chi _4\) coefficient.  It is also the source normalization whose \(c=1\) resonance is \(N/4\).

These four cards are verified.  No further theorem is assumed in this memo.

### 2.5 Custom inequality worth freezing

Let \(\mathcal K_{z,M,N,r}(n)\) denote the **exact** oscillatory \(J/Y/K\) integral obtained from a source-legal level-\(4\) transform of

\[
 x\longmapsto W(rx/M)V_{\rm low}(R^2rx/N)e(+\sqrt{Nrx}),
\]

including its main terms and endpoint convention.  The distinct custom input is the following powerful-convolution resonant estimate, uniformly for prefixes and \(|v|\le D^{1/2}X^\varepsilon\), with \(z=c+iv\), \(0<c<1/4\):

\[
 \boxed{
 \left|
 \sum_{r\le 2M}g_z(r)
 \sum_{\left|n-\frac{4Nr}{4}\right|
       \le C r\sqrt{N/M}\,X^\varepsilon}
 \sigma_{-2z,\chi _4}(n)n^z
 \mathcal K_{z,M,N,r}(n)
 \right|
 \ll_{\varepsilon,V,W,C} M^{3/4}X^\varepsilon .}
\tag{147.S13}
\]

Here the centre is written as \(4Nr/4=Nr\) to display the conductor \(q=4\); in a level-one normalization it is \(Nr/4\).  Formula (147.S13), together with uniform nonresonant integration by parts, is not a generic Hessian estimate, a complete-divisor mean square, or an indefinite-theta transformation.  It asks for cancellation/orthogonality across the correlated powerful index \(r\) and its moving dual resonant band.  A version with the hard cone must be uniform for \(|v|\lesssim D\).

## 3. Proof and method derivation

### 3.1 Factorization proof

Because \(\mu ^2(de)=1\), at an odd prime exactly three local choices are allowed: the prime divides neither variable, it divides \(d\), or it divides \(e\).  This gives (147.S9).  At \(2\), oddness of \(e\) leaves the two choices \(1+2^{-(w+z)}\).  Removing the local factors of \(\zeta(w+z)L(w-z,\chi _4)\) gives (147.S10).  The terms \(a^2,b^2,ab,a^2b,ab^2\) are absolutely summable under (147.S2), proving (147.S1)--(147.S2).  Grouping by \(n=de\) proves (147.S12), and multiplying Dirichlet series proves the convolution statement.

### 3.2 Resonance and its width

For fixed order, the oscillatory Bessel branches in the Banerjee--Khurana kernel have phases

\[
 e\!\left(\pm2\sqrt{nx/q}\right).
\]

The negative branch combined with the physical phase has

\[
 \Phi_-(x)=\sqrt{x}\left(\sqrt N-2\sqrt{n/q}\right).
\tag{147.S14}
\]

There is no interior stationary point unless the coefficient vanishes, which proves (147.S3).  Across \(x\asymp M\), the branch is nonoscillatory when

\[
 \left|\sqrt N-2\sqrt{n/q}\right|\sqrt M\lesssim1.
\]

Linearizing at \(n_0=qN/4\) yields

\[
 |n-n_0|\lesssim q\sqrt{N/M}.
\tag{147.S15}
\]

At the top this is a band of \(\asymp R\) dual integers.  After the \(G\)-convolution, the inner variable has length \(M/r\), physical centre \(Nr\), resonant centre \(qNr/4\), and width \(\asymp qr\sqrt{N/M}\), as recorded in (147.S13).

The fixed-order asymptotic algebra in the particular Banerjee--Khurana \(J/Y\) combination cancels the order-dependent leading phase: formally,

\[
 J_\nu(x)\cos(\pi\nu/2)-Y_\nu(x)\sin(\pi\nu/2)
 \sim \left(\frac2{\pi x}\right)^{1/2}\cos(x-\pi/4).
\tag{147.S16}
\]

Thus a large imaginary Mellin shift does not move the leading resonance.  Turning (147.S16) into a uniform expansion with controlled derivatives and all correction terms is nevertheless not supplied by the cited theorem.  The formal small parameter near the top resonance is favorable: the Bessel argument is \(\asymp R^3\), while \(|\nu|^2\lesssim R\) after smoothing and \(|\nu|^2\lesssim R^2\) for the hard cutoff.  This makes a custom uniform derivation plausible, not proved.

### 3.3 Top-block power audit

For the complete coefficient \(A_z\), the Bessel integral at resonance has size

\[
 M\,(NM)^{-1/4}=M^{3/4}N^{-1/4}
\]

per dual integer.  Multiplying by the band length \(\asymp\sqrt{N/M}\) gives the raw absolute capacity

\[
 M^{1/4}N^{1/4}.
\tag{147.S17}
\]

At \(M\asymp R^2,N\asymp R^4\), (147.S17) equals \(R^{3/2}=M^{3/4}\), exactly the raw target.  It gives no reserve.  For smaller blocks its ratio to the target is

\[
 \frac{M^{1/4}N^{1/4}}{M^{3/4}}
 =\left(\frac{N}{M^2}\right)^{1/4},
\tag{147.S18}
\]

the inherited \(R/\sqrt M\) transfer loss after physical normalization.

The squarefree correction cannot be inserted for free.  For a fixed powerful \(r\), the same calculation with length \(M/r\) and centre \(Nr\) still gives the flat capacity \(M^{1/4}N^{1/4}\); the trivial bound is \(M/r\).  Since powerful integers have counting function \(\ll x^{1/2+\varepsilon}\), splitting at

\[
 r_0=\frac{M}{M^{1/4}N^{1/4}}
 =M^{3/4}N^{-1/4}
\]

gives, at the top \(r_0\asymp R^{1/2}\),

\[
 \sum_r |g_z(r)|\min(R^{3/2},R^2/r)
 \ll R^{7/4+\varepsilon}.
\tag{147.S19}
\]

After the physical factor \(R^{-3/2}\), this is \(R^{1/4+\varepsilon}\).  This is an upper-bound limitation of the elementary convolution triangle, not a lower bound for the signed scalar.  It is also the first exact power deficit specific to the ratio-Mellin/Vorono\u00ef proposal.

For comparison, the inherited best favorable separated generic monomial estimate remains Sargos--Wu's normalized \(R^{2/5+\varepsilon}\); Robert--Sargos leaves \(R^{1/2+\varepsilon}\), and the Round-146 three-variable source route leaves \(R^{1/16+\varepsilon}\) only at its formal longest-\(t\) endpoint while failing the mandatory \(t=1\) face.  These figures are limitations of those upper-bound placements, not lower bounds.

### 3.4 Other method classes

The primary-source classes already audited in Rounds 141, 144, 145, and 146 do not repair (147.S19):

- squarefree exponential-sum theorems, including Schlage-Puchta and the recent Doyle paper, concern linear phases and/or moments in the frequency; they do not give a pointwise nonlinear \(\sqrt n\) twist with \(C(n)\);
- Bettin--Chandee treats modular inverses \(e(a\bar m/n)\), whereas the present phase and its one-dimensional \(B\)-process produce archimedean product/ratio phases, not an exact Kloosterman fraction;
- complete divisor, Estermann, or standard-twist formulas omit the strict cone or the squarefree \(G\)-convolution;
- Westerholt-Raum-type indefinite-theta completion theorems provide modular covariance, while Round 144 proved that the exact Appell completion has four mandatory correction owners and no matched harmonic-Maass coefficient theorem;
- the Cao--Zhai, Robert--Sargos, Sargos--Wu, and multidimensional van der Corput cards either reject the literal coefficient or retain a positive top-block power.

## 4. First doubtful or unproved step

The **first source-applicability gap** is a level-\(4\), \(\chi _4\)-twisted Vorono\u00ef identity for \(A_z(n)\) with the actual \(C_c^\infty\) test, uniform for the entire range (147.S7), all inherited prefixes, and the individual positive complex centre.  Banerjee--Khurana Theorem 4.3 does not supply this because its test is analytic in a closed contour; its statement also gives no uniform seminorm bound in growing \(|\Im\nu|\).

Even if that identity and uniform Bessel expansion are derived, the **first missing saving** is (147.S13).  Applying the complete transform separately to every coefficient of \(G\) and taking moduli gives (147.S19), not (147.S5).  Absolute convergence of \(G(w,z)\) cannot justify inserting an absent factor \(r^{-1/2}\) into the physical convolution.  The moving resonances \(n\asymp qNr/4\) must be treated jointly.

For the full block range there is an additional independent deficit (147.S18), already present at \(r=1\).  Therefore even a proof of the top-block version of (147.S13) would not by itself prove the full lower-radial parent or improve the global exponent.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Closing graph and exact interface | **Pass.** The SHA is recorded, the nearest-square mask is absent, and (147.S4)--(147.S5) retain squarefreeness, parity, \(\chi _4\), strict cone, profile, prefix, and positive complex direction. |
| Prime-by-prime Euler factors | **Pass.** The \(2\)-factor and all odd-prime factors give (147.S9)--(147.S10). |
| Absolute-convergence domain | **Pass.** Every remainder monomial is summable under \(\Re(w\pm z)>1/2\). |
| Cone smoothing cost | **Pass/target-sized.** Relative width \(D^{-1/2}\) costs \(O(X^\varepsilon)\) in the weighted scalar. |
| Mellin bandwidth | **Pass as a requirement.** Smoothed use needs \(|\Im z|\lesssim D^{1/2}X^\varepsilon\); hard use needs height \(\gtrsim D\). |
| Banerjee--Khurana coefficient and strip | **Pass for the complete shifted coefficient.** With \(\nu=2z\), \(0<\Re z<1/4\), the coefficient maps exactly after multiplying the test by \(x^{z+1}\). |
| Banerjee--Khurana test and uniformity | **Fail for direct use.** Analytic-contour testing is not the actual nonzero compact smooth test; no growing-\(|\Im\nu|\) estimate is stated. |
| Smooth compact alternatives | **Partial only.** Topacogullari is character-level but unshifted; Goldfeld--Huang is shifted but level one and untwisted. |
| Resonance normalization | **Pass with correction.** Generic centre is \(qN/4\); \(N/4\) is level one, while the literal \(q=4\) Banerjee--Khurana centre is \(N\). |
| Nonresonant/transition ownership | **Open.** Uniform integration by parts and the transition between Bessel regimes are not yet proved for the growing shift. |
| Top complete-factor power | **Borderline.** It is exactly \(M^{3/4+\varepsilon}\) at \(M\asymp R^2\), with no reserve. |
| Squarefree Euler convolution | **Fail under triangle.** The optimized powerful-number split leaves normalized \(R^{1/4+\varepsilon}\). |
| Lower blocks | **Fail under complete resonant capacity.** The factor \((N/M^2)^{1/4}=R/\sqrt M\) remains. |
| Individual complex direction | **Not replaced by a cosine estimate.** The audit uses the exact transformed kernel and does not infer a branchwise bound from a real circle-discrepancy formula. |
| Global exponent | **No change.** No M9-M1 parent, M9, bridge, target, or exponent owner is proved. |

## 6. Dependencies and exact artifacts used

The local dependency set was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/synthesis.md`;
- its Round-146 conductor candidate, adjudication, controls, and source report;
- the Round-145 squarefree-kernel candidate, synthesis, adjudication, controls, and `reports/quadratic_irrational_divisor_twist_source_audit.md`;
- the Round-141 cone candidate, adjudication, controls, and `reports/sqrt_divisor_twist_source_audit.md`;
- the Round-142 rational-spectrum candidate, synthesis, adjudication, controls, and source audit;
- the Round-144 Appell candidate, synthesis, adjudication, controls, and `reports/indefinite_theta_source_hypothesis_audit.md`.

Verified primary cards used here:

1. D. Banerjee and K. Khurana, [*Character analogues of Cohen-type identities and related Voronoi summation formulas*](https://arxiv.org/abs/2306.12399), Theorems 4.3--4.4.
2. I. Kaneko, [*Mixed Moments of the Riemann Zeta and Dirichlet \(L\)-Functions*](https://arxiv.org/abs/2109.12495), Theorem 3.1 and Lemmas 3.2--3.3.
3. B. Topacogullari, [*The fourth moment of individual Dirichlet \(L\)-functions on the critical line*](https://doi.org/10.1007/s00209-020-02610-9), Theorem 2.3 and Lemma 2.5.
4. D. Goldfeld and B. Huang, [*Super-positivity of a family of \(L\)-functions*](https://arxiv.org/abs/1612.09359), Lemma 3.12.
5. S. Bettin and V. Chandee, [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769), for the exact modular-inverse phase class.
6. B. Doyle, [*Subconvexity of Short \(k\)-Free Exponential Sums*](https://arxiv.org/abs/2608.16679), for the recent linear-phase moment class.
7. M. Westerholt-Raum, [*Indefinite Theta Series on Cones*](https://arxiv.org/abs/1608.08874), for the cone-completion class.

No unverified theorem is used.  The withdrawn Dong--Robles--Zeindler preprint is not an admissible source and plays no role.

## 7. Recommended state effect and next-round strategy

**Recommended state effect: retain the target open; record a strategy candidate only; make no proof-state or exponent change.**  Equations (147.S1)--(147.S12) are elementary exact derivations suitable for a Round-147 candidate, but this memo is not a State Patch.  The source verdict is `revise`: the ratio-Mellin/Vorono\u00ef idea should be narrowed from “apply a shifted divisor formula” to the following one-round gate.

**Proposed Round-147 objective:** derive or refute a uniform level-\(4\) shifted Vorono\u00ef reduction for (147.S5), including the exact \(G\)-convolution, and decide the powerful-convolution resonant inequality (147.S13).

The round should have three bounded tasks:

1. derive the \(C_c^\infty\) level-\(4\) formula directly from the completed \(\zeta(w+z)L(w-z,\chi _4)\) functional equation, with \(q=4\), both branches, main terms, prefixes, and polynomial seminorms uniform in (147.S7);
2. expand \(G\) into its exact powerful coefficients, reproduce (147.S19), and seek joint orthogonality across the moving bands \(n\asymp Nr\), never replacing the convolution by an unweighted \(\ell ^1\) assertion;
3. prove (147.S13), prove a weaker range with an explicit power ledger, or construct a support-matched phase-aligned countermodel showing that this transform self-returns.

Exit gates are: exact conductor normalization; uniform imaginary-order Bessel control; target-safe hard/smoothed cone ownership; a nonresonant tail bound; top-block power \(R^0X^\varepsilon\) after the full \(G\)-convolution; and a separate ledger for the lower-block factor (147.S18).  Until every gate passes, the full small-\(t\) scalar, M9-M1, and the global exponent remain unchanged.

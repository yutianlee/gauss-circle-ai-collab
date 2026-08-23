# Round 121 hostile audit: global lower height kernel

Campaign: `m9-m1-global-lower-height-kernel-gate`
Task: `lower_height_kernel_hostile_audit`
Role: selected-context hostile seam reviewer
Starting graph SHA-256: `54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`
Status: candidate evidence only; no shared proof state is changed.

## 1. Result: exact return/no-go and smallest survivor

The profile-first reordering and the zero-extended mod-four pairing are exact. Moreover, the amplitude seam is target-safe: with the accepted sampled-BV profile certificate and the fixed lower radial multiplier, it is

\[
 \mathcal E_X\ll_{V_{\rm low}}(1+\log X)^2.
\tag{121.H1}
\]

This does **not** yield the desired lower-radial estimate. After removal of (121.H1), the exact survivor is

\[
 \boxed{
 \mathcal K_X=
 \sum_{\substack{d\geq1\\d\equiv1\ (4)}}
 \sum_{h\geq1}{b_X(h,d+2)\over h}e(hX/d)
 \left\{1-e\!\left(-{2hX\over d(d+2)}\right)\right\}.}
\tag{121.H2}
\]

It satisfies

\[
 \mathcal B_{\rm low}^+=\mathcal E_X+\mathcal K_X.
\tag{121.H3}
\]

Consequently, at the required scale,

\[
 \mathcal B_{\rm low}^+\ll_\varepsilon RX^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal K_X\ll_\varepsilon RX^\varepsilon.
\tag{121.H4}
\]

Thus adjacent mod-four pairing is a capacity-preserving return, not an inequality. It globally removes the Round-57 bookkeeping defect of unmatched *labels* by zero extension, but it leaves exactly the same unsaved phase-increment mechanism. No target-safe joint height inequality has been proved.

There is also a literal resonance-capacity obstruction. For fourth powers (X=K^4), (R=K), a fixed interior top-denominator interval, and heights already restricted to the range corresponding to (n\gtrsim X^{2/5}), one can choose pairwise disjoint exact reciprocal-resonance tubes (T) such that

\[
 \sum_T|\mathcal K_X[T]|\gg R^{3/2}.
\tag{121.H5}
\]

The target is (R X^\varepsilon). Hence taking absolute values after a resonance decomposition loses (R^{1/2}). Equation (121.H5) is not a signed lower bound for the whole kernel: cancellation between different heights and different resonance labels remains possible. It proves precisely that such joint cancellation is still the missing theorem.

The conductor's later flattening/completion candidate admits a further, genuinely useful reduction, but only after two repairs. Let the inactive bottom have its certified fixed support (d\leq C_bR), choose the already-permitted fixed lower cutoff so small that

\[
 {2\over\sqrt{2s_0}}>C_b,
\tag{121.H5a}
\]

and use a (C^\infty), not merely (C^1), two-variable separation with a weighted Wiener norm. Then

\[
 \mathcal B_{\rm low}^+=\mathcal B_{\rm flat}^+
 +O_{\varepsilon,s_0}(RX^\varepsilon),
\qquad
 \mathcal B_{\rm flat}^+(X)=\mathcal B_{\rm flat}^{(\lfloor X\rfloor)}(X)+O_{s_0}(R).
\tag{121.H5b}
\]

For one explicitly fixed sample-exact smooth interpolant (J_{R,y}), the integer-phase cone has the exact discrepancy representation

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)
 \{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\},
 \qquad N=\lfloor X\rfloor.}
\tag{121.H5c}
\]

Thus the maximal safe theorem is (121.H1)--(121.H5c), together with the tubewise no-go (121.H5). The smallest exact **arithmetic description** is the prescribed-centre discrepancy functional (121.H5c). The smallest phase-side survivor is the flat version of (121.H2). These are target-equivalent exact returns, not a proved smaller-capacity norm. No proper resonant subkernel is yet known to contain the whole difficulty because its complement has not been bounded globally.

## 2. Exact statement and hypotheses

Write (e(t)=e^{2\pi i t}), (R=X^{1/4}), (Y=\sqrt X), (y=\lfloor Y\rfloor),

\[
 D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor,
\]

and omit every scale with (H_j=0). Let

\[
 a_j(h)={\bf1}_{h\leq H_j}\Phi\!\left({h\over H_j+1}\right),
 \qquad
 A_X(h,d)=\sum_j a_j(h)w_j(d),
\]

\[
 b_X(h,d)=A_X(h,d)V_{\rm low}\!\left({4R^2h^2\over d^2}\right),
\tag{121.H6}
\]

where all sequences are extended by zero off their literal physical support. A displayed (w_j(d)) means the actual sampled profile value, including any inherited endpoint star; a star is a scalar sample convention, not a new term that can be moved to a pairing endpoint.

The proof uses only the following accepted properties.

1. The (w_j) are the actual nonnegative active telescoping profiles. They have fixed-shell support, sum to at most one after the separately owned inactive bottom is removed, and satisfy uniformly
   \[
   \|w_j\|_\infty+\sum_d|w_j(d+1)-w_j(d)|\leq4.
   \tag{121.H7}
   \]
   The unique hard top jump and all starred endpoint samples are included in this discrete variation.
2. (0\leq\Phi\leq1), and the accepted (C^1) extension of (Phi) is used only to obtain a fixed positive lower bound on compact subintervals of ([0,1)).
3. (V_{\rm low}) is the fixed real smooth cutoff used by the one-count radial partition, equal to one near zero and zero before the outer product endpoint. Its one-dimensional total variation is (O_{s_0}(1)).
4. The literal positive reciprocal antecedent and its normalization are
   \[
   \mathcal B_{\rm low}^+
   =\sum_{h,d\geq1}{\chi_4(d)b_X(h,d)\over h}e(hX/d),
   \tag{121.H8}
   \]
   \[
   \mathcal B_{\rm low}^+
   ={e(1/8)\over i}R\,G_{\rm low}(X)+O_{s_0}(\log^2(2X)).
   \tag{121.H9}
   \]
   The hard cotangent boundary in (121.H9) is retained in its accepted error owner and is not inserted again into (b_X).

Under these hypotheses, define

\[
 \mathcal E_X=
 \sum_{\substack{d\geq1\\d\equiv1\ (4)}}
 \sum_{h\geq1}{b_X(h,d)-b_X(h,d+2)\over h}e(hX/d).
\tag{121.H10}
\]

Then (121.H1)--(121.H5) are the hostile-audit theorem. The negative reciprocal frequency is the complex conjugate because every amplitude is real, so it has the identical ledger. The inactive bottom remains a separate already-target-safe physical owner.

For the corrected conductor reduction, write

\[
 \mathcal B_{\rm flat}^+(X)=
 \sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d),
\tag{121.H10a}
\]

and let (C_b) be the actual fixed support constant of the inactive bottom. Condition (121.H5a), rather than the unaudited bare number (s_0\leq1/100), is the exact bottom-separation hypothesis. To make the Fourier completion canonical, fix once and for all a smooth function (eta) with (eta(u)=0) for (u\leq1/2) and (eta(u)=1) for (u\geq1), and on the small positive arc put

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t},
\tag{121.H10b}
\]

extended smoothly by zero and periodically. Then (J_{R,y}(0)=0), and (121.H10b) has the exact required value at every nonzero sample (t=h/d) with (d\leq y), because such a sample is at least (1/y). Define (A_y(m)=\sum_{d\mid m,d\leq y}\chi_4(d)) for every (m\in\mathbb Z), with every positive (d\leq y) understood to divide (0), and define (D_N) by (D_N(0)=0) and

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-\sum_{d\leq y}{\chi_4(d)\over d}
 \quad(k\in\mathbb Z).
\tag{121.H10c}
\]

These conventions remove the interpolation, zero-index, and negative-index ambiguities in (121.H5c).

## 3. Proof and derivation

### 3.1 Literal antecedent, one count, and external normalization

Every sum in (121.H8) is finite. Therefore summing the physical profiles before applying a norm is only finite reordering:

\[
 \sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)V_{\rm low}(4R^2h^2/d^2)e(hX/d)
 =\sum_{h,d}{\chi_4(d)b_X(h,d)\over h}e(hX/d).
\]

No floor is replaced: (H_j=\lfloor D_j/R\rfloor) stays inside (a_j). Empty heights were removed before any quotient. The unique hard sample is part of (w_0); zero extension owns the active top and bottom profile edges; the inactive bottom is not put into (A_X). Because (V_{\rm low}) vanishes before (n/Y=16), the outer product half tie has zero multiplicity in this lower summand. Internal inherited stars remain their actual scalar samples. Equation (121.H9), already audited in Round 120 with the same positive-frequency constant, shows that the reciprocal target is (RX^\varepsilon), not (X^\varepsilon).

### 3.2 Exact mod-four identity and every boundary

Put (F_X(d)=\sum_h b_X(h,d)h^{-1}e(hX/d)). Since

\[
 \chi_4(4m+1)=1,\qquad \chi_4(4m+3)=-1,
\]

and (d\mapsto d+2) is a bijection from the positive (1\pmod4) integers to the positive (3\pmod4) integers,

\[
 \mathcal B_{\rm low}^+
 =\sum_{d\equiv1(4)}\{F_X(d)-F_X(d+2)\}.
\tag{121.H11}
\]

The sum in (121.H11) is over all positive (d\equiv1\pmod4), not only those whose two entries lie inside one profile. Hence a last (1\pmod4) top sample is paired with zero, a last (3\pmod4) sample is owned by the preceding pair, and the analogous statement holds at the active bottom and every gap. These are full amplitude owners; no inherited half star is borrowed.

With

\[
 \Delta_d={2X\over d(d+2)}={X\over d}-{X\over d+2},
\]

adding and subtracting the (d+2) amplitude at phase (e(hX/d)) gives exactly

\[
 F_X(d)-F_X(d+2)
 =\sum_h{b_X(h,d)-b_X(h,d+2)\over h}e(hX/d)
 +\sum_h{b_X(h,d+2)\over h}e(hX/d)\{1-e(-h\Delta_d)\}.
\]

This proves (121.H3), including all zero-extended boundary pairs.

### 3.3 The amplitude seam is polylogarithmic

For fixed (h), let (J(h)=\{j:H_j\geq h\}). Since (H_j\geq h) implies (D_j\geq hR),

\[
 |J(h)|\ll1+\log {2R\over h},\qquad 1\leq h\leq H_0\leq R.
\tag{121.H12}
\]

The nonnegative one-count partition and (121.H7) give

\[
 \|A_X(h,\cdot)\|_\infty\leq1,
 \qquad
 \operatorname{Var}_d A_X(h,d)
 \leq4|J(h)|.
\tag{121.H13}
\]

The map (d\mapsto4R^2h^2/d^2) is monotone. Composition with the fixed BV function (V_{\rm low}), followed by zero extension, therefore has uniformly bounded variation. The product rule for BV sequences yields

\[
 \operatorname{Var}_d b_X(h,d)
 \ll_{V_{\rm low}}1+|J(h)|.
\tag{121.H14}
\]

The selected two-step increments are disjoint subchains of the ordinary variation, so

\[
 \sum_{d\equiv1(4)}|b_X(h,d)-b_X(h,d+2)|
 \leq \operatorname{Var}_d b_X(h,d).
\]

Consequently

\[
 |\mathcal E_X|
 \ll\sum_{h\leq R}{1+\log(2R/h)\over h}
 \ll(1+\log R)^2.
\]

This proves (121.H1) with the hard jump, active bottom jump, profile crossings, all height floors, and the radial-cutoff transitions included. It also proves (121.H4).

### 3.4 Exact reciprocal resonances and the tube-capacity obstruction

There are two different notions that must not be conflated. For the original odd-denominator phase

\[
 g_h(d)={hX\over d}+{d-1\over4},
\]

the **exact** consecutive-odd increment is

\[
 g_h(d+2)-g_h(d)={1\over2}-h\Delta_d.
\tag{121.H15}
\]

Thus dangerous character-phase coherence occurs at

\[
 h\Delta_d\approx k+{1\over2},
\tag{121.H16}
\]

whereas the pair multiplier is small at (h\Delta_d\approx k). At (121.H16) its magnitude is nearly maximal. The derivative proxy (2g_h'(d)) is not globally interchangeable with (121.H15), because

\[
 \{g_h(d+2)-g_h(d)\}-2g_h'(d)
 ={4hX\over d^2(d+2)}.
\tag{121.H17}
\]

On (d\asymp R^2), (121.H17) is (O(h/R^2)), but near the smallest lower-radial admissible denominators it need not be small. A full-range proof must use the exact increment or separately prove the validity range of its derivative replacement.

The pair term itself has the exact form

\[
 e(hX/d)\{1-e(-h\Delta_d)\}
 =2i\sin(\pi h\Delta_d)
 e\!\left({hX\over2}\left({1\over d}+{1\over d+2}\right)\right).
\tag{121.H18}
\]

Now take (X=K^4), (R=K\to\infty). Choose a fixed interval

\[
 I=[\alpha R^2,\beta R^2],\qquad0<\alpha<\beta<1,
\]

away from the hard endpoint. The accepted nonnegative fixed-shell partition implies that, after choosing a sufficiently small fixed (c>0),

\[
 b_X(h,d+2)\geq c_0>0
 \quad(d\in I,\ R^{4/5}\leq h\leq cR).
\tag{121.H19}
\]

Indeed, every profile meeting (I) has (H_j\asymp R), so (h/(H_j+1)) stays in a compact subset of ([0,1)); the active profiles sum to one there; and (4R^2h^2/d^2\leq s_0) after reducing (c). Floors change these inequalities only by (O(1)). All profile and hard stars are avoided by shrinking (I), although (121.H19) would also survive their nonnegative scalar values.

For each such (h), the monotone function

\[
 u_h(d)=h\Delta_d={2hR^4\over d(d+2)}
\]

runs through an interval of length (asymp h) on (I). Hence there are (asymp h) distinct half-integers (k+1/2) with a unique real center (d_{h,k}\in I) satisfying (u_h(d_{h,k})=k+1/2). Their spacing is (asymp R^2/h).

For (d\equiv1\pmod4), set

\[
 \theta_h(d)={hR^4\over2}\left({1\over d}+{1\over d+2}\right).
\]

At (d_{h,k}), sampled on step four,

\[
 4\theta_h'(d_{h,k})=-(2k+1)+O(h/R^2),
 \qquad
 \theta_h''(d)\asymp h/R^2.
\tag{121.H20}
\]

Choose a sufficiently small fixed (eta>0) and the tube

\[
 T_{h,k}=\{d\equiv1\ (4):|d-d_{h,k}|\leq\eta R/\sqrt h\}.
\]

Rounding (d_{h,k}) to the step-four lattice changes (u_h) by (O(h/R^2)). Equations (121.H18)--(121.H20) then show throughout a tube that the sine has one sign and is bounded away from zero, while all sampled phases lie in one fixed sector after the integer linear phase is removed. Therefore

\[
 |\mathcal K_X[T_{h,k}]|\gg {1\over h}{R\over\sqrt h}
 ={R\over h^{3/2}}.
\tag{121.H21}
\]

The tubes are disjoint because (R^2/h\gg R/\sqrt h). Summing their moduli gives

\[
 \sum_{h=\lceil R^{4/5}\rceil}^{\lfloor cR\rfloor}
 \sum_{k:d_{h,k}\in I}|\mathcal K_X[T_{h,k}]|
 \gg\sum_h h{R\over h^{3/2}}
 \asymp R^{3/2},
\]

which is (121.H5). For (d\asymp R^2), the stationary radial variable is (n\asymp h^2); hence (h\geq R^{4/5}) lies at or above (n=X^{2/5}). The obstruction therefore occurs in the portion of the lower cutoff not covered by the strict small-angle replacement.

### 3.5 Corrected target-scale profile flattening

On the support of (V_{\rm low}(4R^2h^2/d^2)),

\[
 {hR\over d}\leq{\sqrt{2s_0}\over2}.
\]

If (w_j(d)\ne0), the certified profile support (d/D_j\leq3/2) gives

\[
 {hR\over D_j}\leq{3\sqrt{2s_0}\over4}<\frac12.
\tag{121.H23}
\]

Thus (D_j/R>2h), so the exact floor satisfies (h\leq H_j), and

\[
 {h\over H_j+1}<{hR\over D_j}<\frac12.
\tag{121.H24}
\]

Also (h\geq1) forces (d>2R/\sqrt{2s_0}>C_bR) by (121.H5a). Hence the bottom coefficient is exactly zero on the joint support. The accepted active-plus-bottom one-count identity then gives

\[
 \sum_jw_j(d)={\bf1}_{d\leq y}
\tag{121.H25}
\]

at every contributing sample, including the literal one-sided hard sample. Replacing (Phi) by one therefore gives (121.H10a) exactly. Notice that the selected-context state certifies only a fixed (d\ll R) bottom support; it does not certify the candidate's displayed constant (4R/3). Formula (121.H5a) is the required correction unless that exact constant is supplied from the profile certificate.

It remains to bound the (Phi-1) error. Split (h) into smooth dyadic shells (h\asymp L\leq cH_j). The explicit Vaaler formula, differentiated on (0\leq u\leq1/2), gives

\[
 |\Phi(u)-1|\ll u^2,\qquad |\Phi'(u)|\ll u.
\tag{121.H26}
\]

Consequently the shell weight

\[
 u_{j,L}(h)={\psi(h/L)\over h}
 \left\{\Phi\!\left({h\over H_j+1}\right)-1\right\}
\]

satisfies

\[
 \|u_{j,L}\|_\infty+\sum_h|\Delta u_{j,L}(h)|
 \ll {1\over L}\left({L\over H_j}\right)^2.
\tag{121.H27}
\]

The sentence in the candidate that a (C^1) two-variable function has absolutely summable Fourier coefficients is false. Here it is repairable because the function being separated is actually (C^\infty). On the fixed rectangle (h/L\asymp1), (d/D_j\in[1/2,3/2]), put (lambda=RL/D_j\leq c). Smooth periodic extension of

\[
 V_{\rm low}(4\lambda^2(h/L)^2/(d/D_j)^2)
\]

has a uniform expansion (sum_{r,s}c_{r,s}e(rh/L)e(sd/D_j)) satisfying

\[
 \sum_{r,s}|c_{r,s}|(1+|r|)(1+|s|)\ll_{s_0}1.
\tag{121.H28}
\]

Modulation by (e(rh/L)) multiplies the height BV norm in (121.H27) by (O(1+|r|)). Modulation of (w_j(d)), including the hard truncation, has sampled BV (O(1+|s|)), since its support length is (O(D_j)). The accepted frequency-first divisor theorem therefore applies termwise and (121.H28) is summable. It gives the corrected form of the candidate's estimate:

\[
 E_{j,L}\ll_{\varepsilon,s_0}X^\varepsilon
 \left({L\over H_j}\right)^2\left(1+{D_j\over L}\right).
\tag{121.H29}
\]

For a nonempty profile, (D_j/R<H_j+1\leq2H_j). Dyadic summation yields

\[
 \sum_{L\leq cH_j}\left({L\over H_j}\right)^2
 \left(1+{D_j\over L}\right)
 \ll1+{D_j\over H_j}\ll R.
\]

The (O(\log X)) profiles are absorbed into (X^\varepsilon). This proves the first identity in (121.H5b). Thus the flattening theorem is valid after the bottom-constant and (C^\infty)-Wiener repairs; it does not follow from the candidate's stated (C^1) claim as written.

### 3.6 Integer phase and exact Fourier/discrepancy completion

Let (N=\lfloor X\rfloor). Since (|e(hX/d)-e(hN/d)|\ll h/d), after multiplication by (1/h) the error is (O(1/d)) per supported height. There are (O_{s_0}(d/R)) such heights, so summing (d\leq y\) gives (O_{s_0}(y/R)=O_{s_0}(R)). This proves the second identity in (121.H5b). It changes only the phase; (R), (y), and the radial multiplier still depend on the original real (X).

The explicit construction (121.H10b) proves existence and sample exactness of (J_{R,y}). The lower support has (0<h<d), so (h=1,\ldots,d-1) are precisely the nonzero residue samples and (J_{R,y}(0)=0). With

\[
 \widehat J(k)=\int_0^1J(t)e(-kt)\,dt,
 \qquad J(t)=\sum_k\widehat J(k)e(kt),
\]

orthogonality gives, with the sign as displayed,

\[
 {\chi_4(d)\over d}\sum_{h\bmod d}J(h/d)e(Nh/d)
 =\chi_4(d)\sum_{k:d\mid N+k}\widehat J(k).
\tag{121.H30}
\]

Summing (d\leq y) yields

\[
 \mathcal B_{\rm flat}^{(N)}(X)=\sum_{k\in\mathbb Z}\widehat J(k)A_y(N+k).
\tag{121.H31}
\]

For fixed (X), (J) is smooth, so its Fourier coefficients are Schwartz; (A_y(m)=O(y)), and all interchanges are absolute. Fourier inversion at zero gives (sum_k\widehat J(k)=J(0)=0), allowing subtraction of (c_y=\sum_{d\leq y}\chi_4(d)/d). The recurrence (121.H10c) gives for (k\geq1)

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left\{\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right\},
\]

and determines negative (k) by the reversed interval. Finally,

\[
 \sum_k\widehat J(k)\{D_N(k)-D_N(k-1)\}
 =\sum_kD_N(k)\{\widehat J(k)-\widehat J(k+1)\},
\]

with no boundary term because (D_N(k)=O_y(1+|k|)) and (widehat J) is Schwartz. This proves (121.H5c), including the signs and convergence in the candidate's (C17)--(C20).

The construction of (J) is not canonical: different smooth interpolation below the first sample gives different Fourier weights but the same sampled functional. It also has (J(1/y)=y) and rapidly growing raw seminorms near zero. Exact smoothness for each fixed (X) proves identities, not a uniform analytic saving. Any future estimate must declare the chosen interpolation and prove the required (X)-uniform norm of the *difference* weights in (121.H5c).

### 3.7 Comparison with prior returns

Round 57 already produced the identical algebraic bracket: actual amplitude difference plus an unsaved phase increment. Its local product rows also had unmatched terms. Round 121 is more global only in bookkeeping: (A_X(h,d)) aggregates every profile before the norm and zero extension pairs every positive odd denominator. This makes the pair identity complete, but it does not make (121.H18) small or cancel the resonance tubes.

On the subcritical range, Appell completion, one-sided character Poisson, product-wavelet inversion, affine Abel reduction, and crossing Fourier modes return to the same one-sided divisor/reciprocal cone without an estimate. Kernel (121.H2) does not evade those returns; by (121.H3) it is the original reciprocal lower antecedent modulo a polylogarithmic amplitude difference. Above (X^{2/5}), the small-angle replacement is unavailable.

The corrected flattening theorem is genuinely stronger than Rounds 64--65 at one seam: it proves that the **entire** literal lower profile/floor kernel, including the above-(2/5) range and the hard profile, is target-equivalent to one sharp denominator cone. The subsequent Fourier and affine-discrepancy steps are not a new analytic mechanism. They globalize the Round-64/65 product-wavelet and unmatched-crossing return, with a sharp cutoff (d\leq y) and a noncanonical full lower wavelet. Period-four pairing still cancels only matched crossings. Thus (121.H5c) is a cleaner global survivor, but no accepted return map supplies its missing inequality.

## 4. First doubtful or unproved step

After the corrected flattening, integerization, and exact completion, the first unproved step is equivalently either

\[
 \mathcal K_{X,\rm flat}\ll_\varepsilon RX^\varepsilon
 \quad\text{or}\quad
 \sum_kD_N(k)\{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}
 \ll_\varepsilon RX^\varepsilon.
\tag{121.H22}
\]

Nothing before (121.H22) is a signed power-saving argument: flattening spends the full allowed target error, integerization costs (O(R)), Fourier completion is exact, and affine summation is invertible. The factor (1-e(-h\Delta_d)) cannot be bounded as a small increment: it is nearly (2) on (121.H16). Nor may a proof replace the exact discrete increment by (2g_h'(d)) throughout the full lower range without pricing (121.H17). Finally, (121.H5) rules out taking moduli after separating the reciprocal resonances. A valid continuation must keep the complete cross-(h), cross-resonance/crossing signed sum until a quantified inequality is obtained.

Within the conductor candidate as written, the first literally false step is the assertion following (C9) that a (C^1) two-variable multiplier has absolutely summable Fourier coefficients. The repair (121.H28) uses the actual (C^\infty) lower multiplier and weighted Fourier decay. The first missing exact datum is the claimed (4R/3) bottom support constant; (121.H5a) repairs the proof using the certified fixed bottom constant. Neither defect invalidates the corrected flattening theorem, but both must be repaired before promotion.

## 5. Control tests and outcomes

### Seam table

| Required control | Outcome | Hostile finding |
|---|---:|---|
| `literal_lower_reciprocal_antecedent` | PASS | (121.H8) matches the accepted positive reciprocal antecedent. The hard cotangent term remains in the separate transform error. |
| `external_R_normalization` | PASS | (121.H9) makes the target (RX^\varepsilon). Dividing by (R) is required before claiming a normalized radial bound. |
| `global_profile_height_kernel` | PASS | The aggregation is exact finite reordering with the literal floors and empty scales omitted. It is not cancellation. |
| `mod_four_pairing_identity` | PASS | (121.H11) is a bijective identity on all positive odd denominators. Zero extension owns every active support edge. |
| `amplitude_seam_BV` | PASS | The accepted per-profile BV plus the fixed radial BV gives (121.H1), including hard, bottom, and profile jumps. |
| `phase_increment_joint_height_kernel` | FAIL as estimate | The exact kernel is (121.H2), but its (RX^\varepsilon) bound is precisely the original open target modulo (121.H1). |
| `resonant_nonresonant_capacity` | FAIL | Integer increment nulls and half-integer character resonances are distinct. The latter give tubewise capacity (\gg R^{3/2}). |
| `floor_star_hard_bottom_boundaries` | PASS with typed convention | Floors are never smoothed; starred samples remain scalar values; the hard endpoint is zero-extended; the inactive bottom stays separate; no artificial half owner is used. |
| `old_return_map_nonduplication` | PARTIAL | Target-scale flattening of the entire literal lower owner is genuinely new. Pairing and the Fourier/discrepancy completion still return to the Round-57 and Round-64/65 survivors without an inequality. |
| `unsigned_adversarial_control` | FAILS the false analogue, as required | Unsigned or phase-adversarial coefficients have (\gg R^2) capacity already at (h=1) on a fixed (d\asymp R^2) interval. The actual character and global phase correlation are indispensable. |
| `full_lower_range_scope` | PASS as reduction; FAIL as closure | Corrected (121.H5b) includes the full lower cutoff and the above-(2/5) range. No estimate is proved, and (121.H5) occurs in that upper part. |
| `one_count_downstream_scope` | PASS | A proof of (121.H22) would close only the lower GAR child and then GAR via the accepted nonlower theorem and one-count assembly. No blockwise inverse is available. |

### Conductor-candidate seam table

| Candidate seam | Outcome | Required correction or finding |
|---|---:|---|
| (Phi-1) shell BV (C8)--(C9) | PASS after derivation | The explicit Vaaler formula gives both (|\Phi-1|\ll u^2) and (|\Phi'|\ll u), which imply (121.H27). The value bound alone would not imply the BV claim. |
| Coupled multiplier separation before (C10) | FAIL as written; REPAIRED | (C^1) does not imply an absolutely summable two-dimensional Fourier series. Uniform (C^\infty) separation with the weighted norm (121.H28) does, and preserves the height and hard-profile BV hypotheses. |
| Frequency-first theorem transfer | PASS after weighted separation | Each mode has height BV (O((L/H_j)^2(1+|r|)/L)) and denominator BV (O(1+|s|)), giving (121.H29). |
| Active partition and bottom geometry (C4)--(C7) | CONDITIONAL PASS | The support inequalities and floor implication are exact. Replace the unsupported numerical bottom edge (4R/3) by the certified (C_b) and impose (121.H5a); then the active partition is exactly one on joint support. |
| One-sided hard sample in (C7) | PASS under the accepted one-count convention | It is the literal scalar sample in the active partition. It is neither deleted nor assigned an inherited half weight. |
| Integer-phase error (C13) | PASS | The absolute error is (O(y/R)=O(R)); amplitudes retain the original real-(X) values. |
| Existence and exact samples of (J_{R,y}) (C15) | PASS after fixing a construction | Formula (121.H10b) is smooth periodic, zero near zero, and exact at every nonzero rational sample. Arbitrary interpolation should not be left implicit. |
| Fourier sign/divisibility in (C17) | PASS | With the stated transform convention, orthogonality gives (d\mid N+k), not (N-k); (121.H30) verifies the sign. Define (A_y) on negative integers and at zero. |
| Zero mode and density subtraction (C18) | PASS | Absolute Fourier convergence gives (sum_k\widehat J(k)=J(0)=0). |
| Crossing formula and two-sided recurrence (C19) | PASS after typing negative (k) | The positive-(k) floor formula is exact; (121.H10c) uniquely supplies the reversed negative interval. |
| Summation-by-parts sign/convergence (C20) | PASS | The weight is (widehat J(k)-\widehat J(k+1)). Linear growth of (D_N) and Schwartz decay eliminate boundary terms. |
| Uniform analytic content of (C17)--(C20) | FAIL | (J(1/y)=y) and raw interpolation seminorms grow with (X). Fixed-(X) Schwartz convergence proves identities only. No target norm for the discrepancy functional follows. |
| Strength relative to Rounds 64--65 | PARTIAL | Full-profile target-scale flattening is new and global. Fourier completion and unmatched-crossing discrepancy are a sharp-cutoff globalization of the accepted return, not a new saving. |

### Adversarial and resonance-capacity controls

| Control | Certified capacity | Budget | Outcome |
|---|---:|---:|---|
| Unsigned actual-amplitude mass, (h=1), (d\asymp R^2) | (\gg R^2) | (R X^\varepsilon) | Reject coefficient-blind/unsigned analogue. |
| Post-pair termwise modulus on a subinterval where (\|\Delta_d\|\) stays away from (0) | (\gg R^2) | (R X^\varepsilon) | Pairing alone gives no pointwise small factor. |
| Unit-modulus adversary conjugating the pair phase | (\gg R^2) | (R X^\varepsilon) | Reject any theorem using only amplitude BV and support. |
| Actual-phase, disjoint half-integer resonance tubes, (R^{4/5}\leq h\leq cR) | (\gg R^{3/2}) after tubewise moduli | (R X^\varepsilon) | Reject resonance-by-resonance absolute summation. |
| Whole signed (mathcal K_X) | unknown | (R X^\varepsilon) | This is the exact surviving theorem; no counterexample is claimed. |

No numerical experiment and no external source were used. The controls are analytic and use fourth powers only to expose a strict floor-free resonance-capacity family; they do not certify or refute the globally signed sum.

## 6. Dependencies and exact artifacts used

The argument uses the accepted graph facts `H4-Phi-regularity`, `M9-M2-dyadic-weight-nondegeneracy`, `M9-M1-terminal-frequency-divisor-bound`, `M9-M1-global-angular-recombination`, `M9-M1-alpha-Vaaler-height-discrete-variation`, `M9-M1-adjacent-hard-smooth-profile-connector-no-go`, `M9-M1-top-block-adjacent-odd-pairing-no-go`, `M9-M1-global-radial-one-count-assembly`, `M9-M1-terminal-height-nonlower-radial-completion`, and the open node `M9-M1-global-lower-radial-signed-estimate` only as a target.

Exact artifacts read and used:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md`
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md`
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md`
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/synthesis.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/derivation_packet.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md`

No Round-121 sibling report, shared synthesis, validation matrix, proof draft, or legacy immutable round was used or edited.

## 7. Recommended state effect

**Recommendation: revise the Round-121 mechanism, promote only the exact scoped no-go/infrastructure, and retain all target nodes open.**

1. Promote, after conductor seam validation, the exact zero-extended identity (121.H3) and the amplitude-seam lemma (121.H1). Record explicitly that profile stars are actual sampled values and that the hard cotangent boundary and inactive bottom have separate owners.
2. Revise the conductor candidate before promotion: replace the unsupported (4R/3) bottom assertion by (121.H5a), replace the false (C^1)-absolute-Fourier claim by the (C^\infty) weighted separation (121.H28), and fix the explicit interpolant and two-sided divisor/discrepancy conventions (121.H10b)--(121.H10c). After those repairs, promote target-scale flattening, (O(R)) integerization, and the exact identities (121.H31), (121.H5c) as reductions only.
3. Promote the scoped obstruction that mod-four adjacent pairing is target-equivalent to the original lower antecedent modulo (O(\log^2X)), and that any termwise or resonance-tubewise norm has at least the capacity (121.H5). Record that (C17)--(C20) globalize the Round-64/65 unmatched-crossing return but prove no smaller norm. This is not a lower bound for the signed sum.
4. Retain `M9-M1-global-lower-radial-signed-estimate`, `M9-M1-global-angular-radial-estimate`, GAR, both direct blockwise M1 parents, `M9-M1`, `M9-M2`, endpoint uniformity, `M9`, and `GC-target` open.
5. Reject any implication that profile flattening, integerization, Fourier completion, profile-first aggregation, or character pairing proves a signed power saving, a target-safe estimate, the full lower owner, GAR, blockwise M9-M1, M9, or an exponent improvement.
6. If the route continues, freeze either the flat phase kernel or the exactly equivalent prescribed-centre discrepancy functional (121.H5c) as the sole target and require a genuinely joint inequality across all exact discrete resonance/crossing labels and heights, including the (n>X^{2/5}) sector. Another local pairing, derivative-only resonance count, Appell/Poisson/wavelet inversion, or outside norm would duplicate an accepted return.

Even a future proof of (121.H22) would imply the lower GAR child and, with the already proved nonlower completion and radial one-count assembly, the total GAR estimate. It would not imply either literal blockwise M1 parent. Complete M9-M2, endpoint uniformity, and the separate final bridge would still be required before any quarter-scale Gauss-circle conclusion.

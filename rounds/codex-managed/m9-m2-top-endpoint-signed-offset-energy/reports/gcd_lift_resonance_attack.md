# Gcd-lift resonance attack: the odd-lift frequency and the reciprocal self-return

- Campaign: m9-m2-top-endpoint-signed-offset-energy
- Round: 76
- Task: gcd_lift_resonance_attack
- Role: discovery
- Starting graph SHA-256: baa5fc13ca3682ae561c44cd1b20e94728c117378545f586ff3224c16a8eeb6b
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

The proposed resonance test (76.17) is false. The lift \(g\) is odd,
so consecutive admissible lifts differ by \(2\), not by \(1\). If

\[
 \alpha_{a,b,k}={b-a\over4}
       -{X(\sqrt b-\sqrt a)^2\over4k},
 \qquad
 \Lambda_{a,b}:={X(\sqrt b-\sqrt a)^2\over2},
\]

then, writing \(g=2n+1\),

\[
 e(g\alpha_{a,b,k})
 =e(\alpha_{a,b,k})e\!\left(-n{\Lambda_{a,b}\over k}\right).
 \tag{1.1}
\]

Consequently the bulk resonance distance is

\[
 \boxed{\ \|2\alpha_{a,b,k}\|
       =\left\|{\Lambda_{a,b}\over k}\right\|,\ }
 \tag{1.2}
\]

not \(\|\alpha_{a,b,k}\|\). In particular, half-integral \(\alpha\)
is fully resonant on the odd lifts. The factor

\[
 e(\alpha_{a,b,k})
 =(-1)^{(b-a)/2}
  e\!\left(-{X(\sqrt b-\sqrt a)^2\over4k}\right)
 \tag{1.3}
\]

is the leading unit and must remain outside the lift sum.

There are two endpoint versions, and they must not be conflated.

1. For the complete sharp lower endpoint,
   \(\lceil gb/4\rceil-gb/4\) alternates with \(g\pmod4\). A safe
   estimate therefore splits \(g\pmod4\) and sees
   \(\|4\alpha\|\), equivalently the union of the integer and
   half-integer resonances of \(\Lambda/k\).
2. A fixed \(m\)-collar at both endpoints has total
   \(O(L^2X^\varepsilon)\) capacity. After removing it in the primal
   sum and inserting continuous fixed-width cutoffs, the complete
   stationary interior symbol has bounded variation on the step-\(2\)
   odd progression. Its correct and stronger bulk test is (1.2).

The repaired actual-symbol normal form is given in (2.13) below. It
is exact up to the diagonal, fixed collars, and nonstationary Poisson
terms, whose total is \(O(L^2X^\varepsilon)\). Abel summation gives
the complete lift-fibre inequality (2.14).

No estimate for the remaining reciprocal resonance union is proved,
and no new polynomial \(L\)-range is claimed. There is a rigorous
no-go: summation in the reciprocal variable \(k\) by the matching
\(B\)-process returns to the original \(m\)-sum with Gaussian units
\(e(1/8)e(-1/8)=1\) and exact adjoint Jacobians. Thus the gcd lift has
removed the varying character from the lift direction and exposed a
character-free reciprocal self-return; it has not created an
independent saving.

## 2. Exact statement and hypotheses

Put \(J=\sqrt X\), \(1\le L\le H\le J^{1/2}\), and use the exact
normalized top symbol from (76.1). In the accepted normalization it is

\[
 a_L(h,x)=\eta_L(h)\Phi\!\left({h\over H+1}\right)
 \left({L^2\over hx}\right)^{3/4}
 W\!\left(\sqrt{{q_Xh\over4x}}\right),
 \qquad q_X={X\over\lfloor\sqrt X\rfloor^2},
 \tag{2.1}
\]

restricted to the actual cone and finite odd \(h\)-support. This is
the normalized symbol only: the accepted exterior top-\(M2\) factor
\(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\) is not inserted a second time.
Set

\[
 A_{h,s}(x)=a_L(h,x)\overline{a_L(s,x)},\qquad
 C_{h,s}=J(\sqrt s-\sqrt h)>0.
 \tag{2.2}
\]

For odd \(h<s\le4h\), let \(A=\lceil s/4\rceil\), \(B=h\). With
\(\widehat f(\xi)=\int f(x)e(-x\xi)\,dx\), exact finite Poisson is

\[
 \sum_{m=A}^{B}A_{h,s}(m)e(-C_{h,s}\sqrt m)
 ={F(A)+F(B)\over2}
  +\sum_{\nu\in\mathbb Z}\int_A^B F(x)e(-\nu x)\,dx,
 \tag{2.3}
\]

where \(F(x)=A_{h,s}(x)e(-C_{h,s}\sqrt x)\). Equivalently, the
integral sum equals the starred endpoint sum. Thus both full endpoint
samples, not zero or two copies of them, are required.

For the negative mode \(\nu=-k\), \(k\ge1\),

\[
 f_k(x)=-C_{h,s}\sqrt x+kx,\qquad
 x_k={C_{h,s}^2\over4k^2},
 \tag{2.4}
\]

and

\[
 f_k(x_k)=-{C_{h,s}^2\over4k},\qquad
 f_k''(x_k)={2k^3\over C_{h,s}^2}.
 \tag{2.5}
\]

Hence an interior saddle has the leading term

\[
 {e(1/8)C_{h,s}\over\sqrt2\,k^{3/2}}
 A_{h,s}(x_k)e\!\left(-{C_{h,s}^2\over4k}\right).
 \tag{2.6}
\]

The exact sharp saddle range is

\[
 {C_{h,s}\over2\sqrt h}\le k\le
 {C_{h,s}\over2\sqrt{\lceil s/4\rceil}}.
 \tag{2.7}
\]

At equality, (2.6) is replaced by the appropriate one-sided Fresnel
factor. In particular, the right endpoint in (2.7) is not exactly
\(C_{h,s}/\sqrt s\).

Now write uniquely

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,\qquad a,b,g\ {\rm odd},\qquad b>a.
 \tag{2.8}
\]

Then \(b-a\) is even,
\(r=g(b-a)/2\), and
\((-1)^r=e(g(b-a)/4)\). Put

\[
 \delta=\sqrt b-\sqrt a,\qquad
 u_k={X\delta^2\over4k^2},\qquad
 \psi_k(u)=-J\delta\sqrt u+ku.
 \tag{2.9}
\]

The complete sharp-endpoint negative-mode symbol is

\[
 \mathfrak B^{\rm sh}_{a,b,k}(g)
 =g\int_{\lceil gb/4\rceil/g}^{a}
 A_{ga,gb}(gu)
 e\!\left(g\left[\psi_k(u)+{X\delta^2\over4k}\right]\right)du.
 \tag{2.10}
\]

There is no stationary truncation in this definition. Direct change
of variables \(x=gu\) gives the exact identity

\[
 (-1)^{g(b-a)/2}
 \int_{\lceil gb/4\rceil}^{ga}
 A_{ga,gb}(x)e(-J\sqrt g\,\delta\sqrt x+kx)\,dx
 =e(g\alpha_{a,b,k})\mathfrak B^{\rm sh}_{a,b,k}(g).
 \tag{2.11}
\]

For the useful bulk version, choose once and for all a smooth cutoff
\(\rho\) which is zero for \(t\le1\) and one for \(t\ge2\), and replace
\(A_{h,s}(x)\) by

\[
 A^\circ_{h,s}(x)=A_{h,s}(x)
 \rho\!\left({x-s/4\over M}\right)
 \rho\!\left({h-x\over M}\right)
 \tag{2.12}
\]

for one fixed \(M\ge1\). The difference at integral \(x\) is supported
on \(O_M(1)\) samples per pair, so its total contribution is
\(O_M(L^2X^\varepsilon)\). Define \(\mathfrak B^\circ\) by (2.10),
with lower limit \(b/4\) and \(A^\circ\) in place of \(A\). If
\(\mathcal G_{a,b}\) is the actual odd lift interval and
\(g=2n+1\), the complete stationary interior contribution is

\[
 \boxed{
 \begin{aligned}
 \mathcal O_{L,\mathrm{stat}}^\circ
  =2\Re\!\sum_{\substack{a<b<4a\\a,b\ {\rm odd},\ (a,b)=1}}
  \sum_{\substack{k\ge1\\
       J\delta/(2\sqrt a)<k<J\delta/\sqrt b}}
  e(\alpha_{a,b,k})
  \sum_{\substack{n\in\mathbb Z\\2n+1\in\mathcal G_{a,b}}}
  \mathfrak B^\circ_{a,b,k}(2n+1)
  e\!\left(-n{\Lambda_{a,b}\over k}\right).
 \end{aligned}}
 \tag{2.13}
\]

The diagonal, the removed collars, and the summed nonstationary
Poisson modes contribute \(O(L^2X^\varepsilon)\). The actual profile
in (2.1), including \(\eta_L,\Phi,W,q_X\), remains inside
\(\mathfrak B^\circ\).

Let \(N_{a,b}=\#\mathcal G_{a,b}\), and define the step-\(2\) variation

\[
 \mathcal V_{a,b,k}=
 |\mathfrak B^\circ(g_{\max})|
 +\sum_{\substack{g,g+2\in\mathcal G_{a,b}}}
  |\mathfrak B^\circ(g+2)-\mathfrak B^\circ(g)|.
\]

Then exact Abel summation gives

\[
 \left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ(2n+1)e(-n\Lambda_{a,b}/k)\right|
 \le \mathcal V_{a,b,k}
 \min\!\left(N_{a,b},{1\over2\|\Lambda_{a,b}/k\|}\right).
 \tag{2.14}
\]

For \(G\asymp L/b\) and a stationary \(k\), uniform one-dimensional
stationary phase applied to the complete centred integral gives

\[
 \mathcal V_{a,b,k}
 \ll_{M,W,\eta}X^\varepsilon
 {J\delta\sqrt G\over k^{3/2}}.
 \tag{2.15}
\]

No frozen leading symbol is used in (2.14)--(2.15). Formula (2.15)
also covers saddle entry into a continuous collar; its proof uses the
complete integral and its \(g\)-derivative. Thus the smallest remaining
bulk near-resonance is the actual-symbol part of (2.13) with

\[
 \left\|{\Lambda_{a,b}\over k}\right\|
 \le {1\over2N_{a,b}}.
 \tag{2.16}
\]

## 3. Proof or derivation

Equation (2.3) is the ordinary finite Poisson identity with half weight
at each integral endpoint. Differentiating (2.4) gives

\[
 f_k'(x)=-{C_{h,s}\over2\sqrt x}+k,
\]

so only a negative Poisson mode can be stationary. Solving
\(f_k'(x)=0\) proves (2.4) and (2.7). Since
\(f_k''(x_k)>0\), the convention \(e(z)=e^{2\pi iz}\) contributes
\(e(1/8)/\sqrt{f_k''(x_k)}\), which is exactly (2.6).

For (2.11), use \(C_{ga,gb}=J\sqrt g\,\delta\) and \(x=gu\). The
phase becomes

\[
 g\psi_k(u),\qquad
 \psi_k(u_k)=-{X\delta^2\over4k}.
\]

Multiplication by the character product gives

\[
 e\!\left({g(b-a)\over4}\right)
 e\!\left(-{gX\delta^2\over4k}\right)
 =e(g\alpha_{a,b,k}),
\]

with no lost factor of two. As \(a,b\) are odd,
\((b-a)/2\in\mathbb Z\). Therefore

\[
 2\alpha_{a,b,k}={b-a\over2}-{\Lambda_{a,b}\over k}
 \equiv-{\Lambda_{a,b}\over k}\pmod1,
\]

and \(e((2n+1)\alpha)=e(\alpha)e(-n\Lambda/k)\). This proves
(1.1)--(1.3) and (2.13). Gcd decomposition has multiplicity one:
\(g=(h,s)\), \(a=h/g\), and \(b=s/g\).

The fixed collars in (2.12) contain \(O_M(1)\) \(m\)-samples for each
of \(O(L^2)\) ordered pairs and \(|a_L(h,m)|\ll X^\varepsilon\) on the
cone. They are therefore target-safe before any absolute value is
taken over offsets. On the remaining smooth interior,

\[
 \min |(-C\sqrt x)''|\asymp {Jr\over L^2}\ge1
 \qquad(L\le J^{1/2},\ r\ge1).
\]

Splitting the Poisson modes according to whether their derivative
range meets the support, one integration by parts for the finite
nearby modes and two for the tails gives
\(O(X^\varepsilon\log(2+Jr/L))\) per ordered pair. Summed over the
pairs, this is \(O(L^2X^\varepsilon)\). The modes with a saddle give
(2.13); their continuous saddle condition is
\(b/4<u_k<a\), which is the displayed \(k\)-range there.

To prove (2.15), note from (2.1) that after
\((h,s,x)=(ga,gb,gu)\), every ratio symbol is independent of \(g\),
while each remaining \(g\)-derivative costs
\(O(g^{-1}+b/L)=O(G^{-1})\). The continuous collar has the same bound:
differentiating \(\rho(g(u-b/4)/M)\) is supported where
\(|u-b/4|\asymp g^{-1}\). The centred phase vanishes at \(u_k\).
Uniform stationary phase, also at continuous collar entry, therefore
gives

\[
 \mathfrak B^\circ_{a,b,k}(g)
 ={e(1/8)J\delta\sqrt g\over\sqrt2\,k^{3/2}}
 A^\circ_{ga,gb}(gu_k)+\text{complete lower-order symbol},
 \tag{3.1}
\]

and the supremum plus total step-\(2\) variation of the complete symbol
is bounded by the right side of (2.15). Finally,

\[
 \left|\sum_{n=p}^{q}e(-n\theta)\right|
 \le\min\!\left(q-p+1,{1\over2\|\theta\|}\right)
\]

because \(|\sin\pi\theta|\ge2\|\theta\|\). Discrete Abel summation
with \(\theta=\Lambda/k\) proves (2.14).

For the sharp endpoint, if \(gb\) is odd then

\[
 {\lceil gb/4\rceil}-{gb\over4}
 ={1\over2}+{\chi_4(gb)\over4}.
 \tag{3.2}
\]

The second term flips when \(g\) is replaced by \(g+2\). Thus a full
sharp Fresnel symbol decomposes into an unmodulated part, resonant at
\(\|\Lambda/k\|=0\), and a \(\chi_4(g)\)-modulated part, resonant at
\(\|\Lambda/k-1/2\|=0\). Equivalently, splitting \(g\pmod4\) gives
the safe combined distance

\[
 \|4\alpha\|=\left\|{2\Lambda\over k}\right\|.
 \tag{3.3}
\]

This is why step-\(2\) BV is asserted only after the target-safe collar
has been removed.

There is an exact actual-symbol countercontrol to (76.17). Let
\(X=T^4\), with \(T\) odd and \(13\mid T\), and take

\[
 (a,b)=(81,121),\qquad \delta=2,\qquad
 k={2T^2\over13}.
\]

Then

\[
 u_k={169\over4}\in\left({121\over4},81\right),\qquad
 \alpha=10-{13T^2\over2}\in\mathbb Z+{1\over2}.
 \tag{3.4}
\]

Thus \(\|\alpha\|=1/2\), but \(\|2\alpha\|=0\), and
\(e(g\alpha)=-1\) for every odd \(g\). Here \(q_X=1\), and the two
actual top-profile samples at the saddle are

\[
 W(9/13)=W(11/13)=1,
\]

because both arguments lie in the frozen interval \([2/3,1]\) on
which \(W=1\). The \(\eta_L\) and \(\Phi\) factors remain the actual
moving factors on any common interior lift interval. The leading term is

\[
 -e(1/8){13^{3/2}\sqrt g\over2T}
 A_{81g,121g}(169g/4),
 \tag{3.5}
\]

so this is not an adversarial-coefficient artefact.

Finally, the reciprocal transform is involutive. Starting with the
leading \(k\)-symbol in (2.6), Poisson in \(k\) has phase

\[
 F_m(t)=-{C^2\over4t}-mt.
\]

Its saddle is \(t=C/(2\sqrt m)\), its value is \(-C\sqrt m\), and

\[
 |F_m''(t)|={C^2\over2t^3},\qquad
 {1\over\sqrt{|F_m''(t)|}}={\sqrt2\,t^{3/2}\over C}.
\]

This Jacobian cancels \(C/(\sqrt2\,t^{3/2})\) exactly, while the
negative Hessian contributes \(e(-1/8)\), cancelling the first
\(e(1/8)\). The result is
\(A_{h,s}(m)e(-C\sqrt m)\), with the original factor \((-1)^r\).
Full Fourier inversion returns the complete moving/Fresnel symbol;
freezing (3.1) gives only the corresponding asymptotic return.

## 4. First doubtful or unproved step

The first false step is (76.17): it applies a step-\(1\) geometric bound
to an odd step-\(2\) lift. The explicit family (3.4)--(3.5) has full
coherence although (76.17) declares it maximally nonresonant.

After correcting that error, the first genuinely unproved step is a
bound for the complete actual-symbol reciprocal union in (2.13), in
particular the near set (2.16), at total size \(L^2X^\varepsilon\).
One may not sum (2.14) absolutely over \(a,b,k\): fibres with
\(G\asymp1\) have no lift gain, and absolute \(k\)-summation discards
the cancellation whose \(B\)-process is exactly the self-return above.
No spacing, exponent-pair, or spectral theorem in the permitted packet
controls this coupled actual symbol.

Exact primitive square resonances are not themselves an obstruction.
If \(a=u^2,b=v^2\), then \(\delta=v-u\); whenever
\(\Lambda/k\in\mathbb Z\), \(k\) divides the integer \(\Lambda\), so
there are \(O_\varepsilon(X^\varepsilon)\) such \(k\)'s. With
\(G\asymp L/v^2\) and \(v\asymp u\), their coherent leading mass is

\[
 \ll_\varepsilon {L^{3/2}X^\varepsilon\over\sqrt J}
 \sum_{u\le\sqrt L}u^{-3/2}
 \sum_{1\le v-u\le u}(v-u)^{-1/2}
 \ll_\varepsilon {L^{3/2}\over\sqrt J}X^\varepsilon
 \ll L^2X^\varepsilon.
 \tag{4.1}
\]

Perfect fourth powers form a smaller subfamily. The uncontrolled part
is the full near-integer reciprocal set with the moving symbol, not the
exact perfect-power fibres.

## 5. Control tests and outcomes

1. **External normalization -- pass.** The calculation is for the
   normalized energy (76.2). The accepted exterior
   \(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\) occurs once and was not folded
   into \(a_L\) again.
2. **Exact ceiling, stars, and both endpoints -- pass.** Equation
   (2.3) has the two half-endpoint corrections. Equation (2.10) keeps
   \(\lceil gb/4\rceil\) exactly. The bulk replacement is licensed
   only after an \(O_M(L^2X^\varepsilon)\) primal collar is separated.
3. **Diagonal and fixed offsets -- pass.** The accepted diagonal is
   \(O(L^2)\). No fixed-\(r\) estimate was summed absolutely over the
   \(O(L)\) offsets.
4. **Alternating character sign -- pass, with a correction.**
   \((-1)^r=e(g(b-a)/4)\) is inserted before any absolute value. Since
   \(g\) is odd it is constant along a primitive lift family up to the
   fixed unit in (1.3); it supplies no alternating \(g\)-cancellation.
5. **Poisson orientation, Gaussian, and Jacobian -- pass.** The active
   mode is \(\nu=-k\); \(x_k=C^2/(4k^2)\); the first Gaussian is
   \(e(1/8)\); and its coefficient is \(C/(\sqrt2 k^{3/2})\).
   The matching return has \(e(-1/8)\) and reciprocal Jacobian.
6. **Endpoint Fresnel and summed errors -- pass in the stated split.**
   The exact sharp symbol (2.10) contains the incomplete endpoint
   behavior. For the estimate, fixed collars are bounded in the
   primal sum and the smooth-interior nonstationary total is
   \(O(L^2X^\varepsilon)\); no frozen Fresnel value is substituted.
7. **Gcd parity and multiplicity -- pass.** \(g,a,b\) are odd,
   \(b-a\) is even, \(r=g(b-a)/2\), and \(g=(h,s)\) makes (2.8)
   unique.
8. **Linear lift phase and actual moving symbol -- corrected/pass.**
   Equation (2.11) is the exact \(g\)-linear factorization. The leading
   unit \(e(\alpha)\), the actual \(q_X,\eta_L,\Phi,W\), and the complete
   centred integral remain. The correct bulk distance is
   \(\|2\alpha\|\).
9. **Step-2 versus step-4 endpoint seam -- pass.** Continuous bulk
   collars have step-\(2\) BV and resonance (1.2). The unremoved sharp
   ceiling has the mod-\(4\) decomposition (3.2) and must use the safe
   step-\(4\) criterion (3.3).
10. **Rank one and self-return -- pass as a no-go.** The second
    \(k\)-process restores the original phase, amplitude, sign, and
    Gaussian normalization. No nondegenerate two-dimensional Hessian
    estimate is inferred.
11. **Perfect powers, near resonance, and adversarial coefficients --
    pass as controls.** Formula (4.1) is target-safe, while the actual
    half-integral family (3.4) falsifies (76.17). Artificial phase
    conjugation is neither used nor licensed; the full near-integer
    actual-symbol union remains open.
12. **Downstream scope -- pass.** The report proves neither
    \(\mathcal E_L^\top\ll L^2X^\varepsilon\), a new polynomial
    \(L\)-range, the signed cone, full \(M2\), \(M9\), endpoint
    uniformity, nor the Gauss-circle exponent. The inherited
    epsilon-trivial \(L\)-range is unchanged.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/derivation_packet.md
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/briefs/gcd_lift_resonance_attack.md
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md
- rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/reciprocal_energy_attack.md
- rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md

No sibling Round-76 report, proof draft, source card, web source, or
computational artifact was used.

## 7. Recommended state effect

**Revise and retain; do not promote the energy estimate or any new
\(L\)-range.** Replace (76.17) by the following typed statement:

- after target-safe fixed endpoint collars are removed, the bulk odd
  lift has leading unit \(e(\alpha)\), geometric ratio
  \(e(-\Lambda/k)\), and resonance
  \(\|2\alpha\|=\|\Lambda/k\|\);
- if the complete sharp ceiling/Fresnel symbol is retained inside the
  lift estimate, split \(g\pmod4\) and use the safe combined resonance
  \(\|4\alpha\|=\|2\Lambda/k\|\).

After independent seam review, retain (2.10)--(2.15) as the corrected
actual-symbol Poisson/gcd-lift interface. Record the explicit
half-integral family (3.4)--(3.5) as a falsifier of the old criterion
and record the reciprocal \(k\)-process as a coefficient-preserving
self-return. Keep M9-M2-top-endpoint-transposed-character-energy,
M9-M2-top-endpoint-signed-cone, M9-M2, M9, endpoint uniformity,
and the global exponent open.

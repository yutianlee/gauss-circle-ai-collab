# Round 29 discovery: the finite-height edge is integrable, but side cancellation is the wrong interface

## 1. Result

There is a narrow positive lemma and a no-go for the proposed side-by-side cancellation.

For the original finite height box the hard-top denominator is integrated in the genuine top variable
\(\mu\in[-U,U]\), while
\[
 \mu=L-\nu,\qquad L=\alpha-\beta,qquad |\nu|\le V.
\]
Thus, after the physical symmetric top limit is taken in \(\mu\), the finite contribution is not the isolated family
\(\int_{-V}^{V}H(\nu)/(a+i(L-\nu))\,d\nu\) at fixed unrestricted \(L\).  Its exact support is
\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U].
\]
On this finite polytope the logarithm at \(L=\pm V\) is only a locally integrable logarithmic singularity; it is not a divergence of the complete \(L\)-integral.  More strongly, in the original \((\mu,\nu)\) variables the physical top distribution acts on a compact rectangle with no moving endpoint:
\[
 \lim_{a\downarrow0}\iint_{[-U,U]\times[-V,V]}
 \frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu
 =\pi\int_{-V}^{V}F(0,\nu)\,d\nu
 -i\int_{-V}^{V}{\rm PV}\!\int_{-U}^{U}\frac{F(\mu,\nu)}{\mu}\,d\mu\,d\nu .
\tag{29.1}
\]
For \(F\in C^1\) this exists and costs at most \(O(\|F\|_\infty+U\|\partial_\mu F\|_\infty)\).  Hence the Round-28 fixed-\(L\), truncated-\(\nu\) logarithm is a coordinate-section edge, not by itself an outside-\(v\)-side obstruction.

The requested cancellation against outside-\(v\) sides cannot be proved from the finite identity because those sides arise only if the \(v\)-line is shifted; they are contour integrals in \(\Re v\), not complementary real-\(\nu\) tails.  Their endpoint values are not determined by the vertical trace \(H_b(\pm V)\), so no universal coefficient identity can match \(-iH_b(V)\log(1/a)\).  The correct next interface is a polytope-aware log-Fresnel estimate on the original positive \(v\)-line, followed separately by the ordinary \(V\to\infty\) tail.  This report does not prove the scaled \(C^2\) hypothesis: differentiating the sectioned amplitude in \(L\) produces boundary distributions at the moving faces.

## 2. Exact statement and hypotheses

Let \(U,V>0\), \(a>0\), and let \(F\in C^1([-U,U]\times[-V,V])\).  Define
\[
 T_{a;U,V}(F)=\int_{-V}^{V}\int_{-U}^{U}
       \frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu .
\tag{29.2}
\]
This is the local finite-height hard-top factor of the beta trace before the linear change \(L=\mu+\nu\); all other factors, including the beta mask and the omega-recombined radial quantity
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1,
\tag{29.3}
\]
are absorbed into \(F\).  Formula (29.3) is kept intact, so no artificial rho residue is created.

The following assertions hold.

1. The limit (29.1) exists, with
\[
 |T_{0;U,V}(F)|
 \le 2\pi V\|F\|_\infty+4UV\|\partial_\mu F\|_\infty.
\tag{29.4}
\]
The numerical constants are inessential.

2. Under \((\mu,\nu)\mapsto(L,\nu)=(\mu+\nu,\nu)\), whose Jacobian is one, the domain is
\[
 \mathcal P_{U,V}=\{(L,\nu):|\nu|\le V,\ |L-\nu|\le U\}.
\tag{29.5}
\]
Consequently the fixed-\(L\) section is \(I_{U,V}(L)\), and \(L\) ranges only over \([-U-V,U+V]\).

3. If a section kernel is written
\[
 C_{a;U,V}(L)=\int_{I_{U,V}(L)}
       \frac{H(L,\nu)}{a+i(L-\nu)}\,d\nu,
\tag{29.6}
\]
then a logarithm can occur when the pole meets a section endpoint, but it is locally integrable in \(L\).  Uniform boundedness and ordinary scale-normalized \(C^2\) in \(L\) are false in general.

4. If the original positive \(v\)-line is not moved, there are no outside-\(v\) sides and no crossed \(v=0\) residue.  If it is moved from \(\Re v=b\) to \(\Re v=b'\), positive rectangle orientation gives, for an upward vertical \(V_c\) and left-to-right horizontals \(H_\pm\),
\[
 V_b=V_{b'}+H_+-H_-+2\pi i\sum_{p}\operatorname {Res}_{v=p}\mathcal M(v).
\tag{29.7}
\]
When \(v=0\) is crossed its residue is included once; if the \(u=0\) line is also moved, the top residue and the joint corner are included by the corresponding two-dimensional ledger, with the corner counted once.  Equation (29.7) is exact but supplies no logarithmic cancellation, since \(H_\pm\) integrate \(v=c\pm iV\) over the real coordinate \(c\).

## 3. Proof or derivation

For (29.1), subtract the value on the pole:
\[
 F(\mu,\nu)=F(0,\nu)+\mu R(\mu,\nu),
 \qquad |R|\le\|\partial_\mu F\|_\infty.
\]
The exact elementary integral is
\[
 \int_{-U}^{U}\frac{d\mu}{a+i\mu}=2\arctan(U/a)\longrightarrow\pi.
\]
Also
\[
 \frac{\mu}{a+i\mu}\longrightarrow\frac1i=-i
\]
away from zero and is uniformly bounded.  Dominated convergence yields (29.1), and the subtraction gives (29.4).  This is precisely the distributional identity
\((0^++i\mu)^{-1}=\pi\delta_0(\mu)-i\,\mathrm{PV}(1/\mu)\), applied in the original top variable before any absolute value.

The change of variables is linear: \(L=\mu+\nu\), \(\mu=L-\nu\).  The rectangle therefore becomes (29.5), proving the exact intersection in (29.6).  In particular, extending the section to all \(\nu\in[-V,V]\) while retaining \(|L-\nu|\le U\) only implicitly changes the finite operator.

To see the section singularity and its integrability, freeze a nonzero smooth coefficient near a face.  Locally the singular part is a constant multiple of
\[
 \int_0^c\frac{dy}{a+i(\delta-y)}
 =-i\{\log(a+i\delta)-\log(a+i(\delta-c))\},
\tag{29.8}
\]
where \(\delta\) is signed distance of \(L\) from the face.  At \(\delta=0\), (29.8) has the Round-28 \(-i\log(1/a)\) size (up to the endpoint/orientation convention).  After \(a\downarrow0\), however, it is \(O(1+|\log|\delta||)\), and
\[
 \int_{|\delta|<1}|\log|\delta||\,d\delta<\infty.
\tag{29.9}
\]
The first derivative behaves like \(1/\delta\) and the second like \(1/\delta^2\), so the ordinary scaled \(C^2\) hypothesis cannot hold across a face without recombining the \(L\)-integration or replacing it by a logarithmic-amplitude version of the Fresnel lemma.

There is no universal cancellation with (29.7).  The coefficient of (29.8) is a trace of the integrand on the top-pole diagonal \(\mu=0\), whereas the upper outside side samples the analytic continuation along \(v=c+iV\) for \(c\) between two abscissae (and the lower side similarly).  Boundary values on the vertical trace do not determine those horizontal integrals.  Indeed, multiply the full meromorphic integrand by a holomorphic factor \(g(v)\) that equals one at one chosen vertical-edge point but varies on the horizontal segment: the section log coefficient is unchanged at that point while the side functional changes.  Thus Cauchy algebra can relate the complete contour expressions, but it cannot furnish a termwise local log-coefficient equality without the entire operator and a specified shift.  Since the accepted construction may retain \(\Re v=b>0\), introducing such a shift is unnecessary for the top limit.

For exhaustion, (29.1) first holds at every fixed \(U,V,S\).  Letting \(V\to\infty\) afterward is then an ordinary tail question for \(\widehat\phi(b+i\nu)\) and the remaining exact factors; the accepted fixed-\(b\) height transform has polynomial decay, but a uniform tail bound for the complete omega-recombined vector integrand and its alpha derivatives has not been proved in the permitted artifacts.  The radial height \(S\) must still follow the accepted endpoint-renormalized nesting; none of the above deletes radial or outside-u sides.

## 4. First doubtful or unproved step

The first exact survivor is not an uncancelled \(\log(1/a)\) coefficient.  It is the physical, polytope-sectioned logarithmic amplitude
\[
 \boxed{
 \mathcal J_{U,V}=\int_{-U-V}^{U+V}e^{i\Psi(L)}
 \left[\pi H(L,L)mathbf1_{|L|\le V}
 -i\,\mathrm{PV}\!\int_{I_{U,V}(L)}
       \frac{H(L,\nu)}{L-\nu}\,d\nu\right]dL ,}
\tag{29.10}
\]
with the actual alpha/beta masks, q,h,scale, radial integration, floors, stars, omega split, and finite sides restored.  The bracket is only log-regular at the moving faces.  What remains unproved is a uniform two-saddle estimate for (29.10) with logarithmic amplitudes, plus uniform tails as \(U,V\to\infty\) and the complete actual-profile sums.  Ordinary scaled \(C^2\) is the wrong sufficient condition across the faces.

## 5. Control tests and outcomes

- **Signed versus unsigned.**  Subtraction at \(\mu=0\) proves (29.1); taking \(|a+i\mu|^{-1}\) first gives \(\log(1/a)\).  Outcome: the signed physical top limit must precede absolute estimates.
- **Support and degeneracy.**  The exact domain is (29.5), not the product of a free \(L\)-line with \([-V,V]\).  At \(L=\pm(U+V)\) the section collapses to a point; at interior face contacts it produces (29.8).  Outcome: the fixed-section log is integrable but derivatives are singular.
- **Residue and normalization.**  Retaining the positive \(v\)-line crosses no \(v=0\) pole.  Under an optional shift, (29.7) includes the height residue once; a subsequent top shift includes \(u=0\) and the joint corner once.  Equation (29.3) prevents an artificial rho residue.  The external \(-(4/\pi)X^{1/4}\operatorname {Re}\{e(1/8)\cdot\}\) is unaffected.
- **Endpoint uniformity.**  (29.8)-(29.9) show uniform values fail at a section endpoint if one fixes \(L\), but the integrated physical operator remains finite.  Outcome: replace ordinary \(C^2\) Fresnel input by bounded/log-BV amplitude control.
- **Order of limits.**  At fixed \(U,V,S\), take the symmetric \(u\)-top limit in \(\mu\) first using (29.1), then integrate \(L\) or equivalently \(\nu\); only afterward exhaust \(U,V\).  Reversing this by taking an isolated fixed-\(L\) endpoint limit creates the spurious uniformity demand.
- **Coefficient adversary.**  The limit lemma uses no \(\chi_4\) cancellation and remains true for arbitrary coefficients.  It therefore does not prove M1: the q/h/scale and phase sums remain.  Conversely, varying a holomorphic side factor shows that no universal local vertical-log/outside-side cancellation follows from orientation alone.

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

Used only the files permitted by the task brief: `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, `rounds/codex-managed/m9-m1-vector-hankel-kernel/reports/blind_finite_vector_kernel.md`, and the Round-20, Round-21, Round-27, and Round-28 syntheses named there.  The finite top distribution and polytope identity were rederived directly.  No other Round-29 report, web source, or numerical computation was used.

## 7. Recommended state effect

Promote, subject to independent seam review, the scoped finite-box physical-top lemma (29.1), the exact polytope support (29.5), and the conclusion that the Round-28 fixed-\(L\) logarithm is locally integrable in the complete \(L\)-operator.  Revise `M9-M1-beta-outside-v-side-reconciliation`: an optional \(v\)-contour shift has the exact orientation (29.7), but no universal termwise outside-side log cancellation exists or is needed on the retained positive \(v\)-line.

Do not promote the scaled \(C^2\) hypothesis, nested exhaustion, complete beta bound, or any downstream theorem.  Replace the next target by a polytope-aware two-saddle lemma for the explicit log-regular kernel (29.10), followed by complete fixed-\(b\) tail and q/h/scale/radial summation.  Keep outside-u sides, radial nesting, double-bounded ownership, M9-M1, M9-M2, M9, and the Gauss-circle target open.

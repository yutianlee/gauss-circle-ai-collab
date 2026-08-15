# Blind signed-offset rederivation report

## 1. Result: validated identities plus a no-go for the proposed lift criterion

The finite positive-offset identity, character sign, orientation and local Gaussian constant of the negative Poisson mode, gcd parametrisation, and linear stationary phase in the lift are algebraically correct. The exact Poisson saddle range is
\[
 \max\!\left(1,\left\lceil {C_{h,r}\over2\sqrt h}\right\rceil\right)
 \le k\le
 \left\lfloor {C_{h,r}\over2\sqrt{\lceil(h+2r)/4\rceil}}\right\rfloor,
\]
not the ceiling-free range except as an approximation. The stationary formula in the packet is only an interior leading term; it is not a complete transform of the sharp finite sum.

There is a decisive parity defect in the proposed resonance survivor. For every primitive pair, all admissible lifts \(g\) are odd. Consequently a consecutive lift sum has step \(2\):
\[
 \sum_{\substack{g\in I\\g\ {\rm odd}}}e(g\alpha)
 =e(g_0\alpha)\sum_{j=0}^{N_g-1}e(2j\alpha).
\]
Its phase-only resonance condition is therefore
\[
 \boxed{\ \|2\alpha\|\lesssim N_g^{-1}\ },
\]
equivalently proximity of \(\alpha\) to \(\tfrac12\mathbb Z\), rather than only
\(\|\alpha\|\lesssim G^{-1}\). Thus (76.17) misses the entire half-integer branch and cannot support the claimed geometric or sampled-BV saving.

This is not merely a formal possibility. Let \(Q\ge49\) be any odd multiple of \(3\), and put
\[
 X=Q^4,\qquad J=Q^2,\qquad (a,b)=(25,49),\qquad k={2Q^2\over9}.
\]
Then, for every odd lift \(g\),
\[
 {x_*\over g}={81\over4},\qquad
 \alpha_{25,49,k}=6-{9Q^2\over2}\in\mathbb Z+\tfrac12,
\]
and
\[
 \left\lceil {49g\over4}\right\rceil<{81g\over4}<25g.
\]
Hence these are genuine interior saddles, \(\|\alpha\|=1/2\), but
\(e(g\alpha)=-1\) for every admissible odd \(g\): there is no lift-phase cancellation. Taking \(L=H=Q=J^{1/2}\) permits a lift interval of length comparable with \(L/49\) whenever the actual support contains that interval.

Therefore the candidate Poisson/gcd mechanism is refuted in its stated form. This does not refute the desired actual-symbol estimate (76.4): the displayed family has only \(O(L)\) lifts for this primitive pair, and neither it nor the other exact perfect-power families exceeds the \(L^2\) raw-capacity threshold. The packet supplies neither the actual symbol nor the regularity and endpoint data needed to prove (76.4), so that estimate remains unproved in the permitted context.

## 2. Exact statement and hypotheses

Let \(\mathscr H_L\) be any finite set of odd positive integers and let \(a(h,m)\) be defined on the indicated integer pairs. Put
\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a(h,m)e(J\sqrt{hm}),
 \qquad \mathcal E_L^\top=\sum_m|R_m|^2.
\]
If \(\mathscr M=\{m:R_m\ne0\}\), Cauchy gives the exact general statement
\[
 \left|\sum_mR_m\right|^2\le \#\mathscr M\,\mathcal E_L^\top.
\]
Thus the factor \(L\) in (76.1) is valid under the additional support consequence
\(\#\mathscr M\ll L\), but it is not implied by the phrase “actual finite odd support” in the permitted packet.

The following assertions require no further analytic hypothesis.

1. On writing \(s=h+2r>h\), the off-diagonal part of \(\mathcal E_L^\top\) is exactly (76.2), with
\[
 q_s:=\left\lceil{s\over4}\right\rceil
 ={s+2+\chi_4(s)\over4},\qquad q_s\le m\le h,
\]
and the interval is nonempty exactly when \(s\le4h\). The factor \(2\Re\), conjugation order, and sign \((-1)^r\) are exact.

2. Suppose the integer-sampled product \(a(h,m)\overline{a(s,m)}\) has been represented by a sufficiently regular function \(A_{h,s}(x)\) on \([q_s,h]\), with all endpoint conventions explicit. For the convention
\(\widehat F(n)=\int F(x)e(-nx)\,dx\), only the mode \(n=-k\), \(k\ge1\), can have a saddle. Its phase, saddle, value, second derivative, and full interior Gaussian are
\[
 f_k(x)=-C\sqrt x+kx,\quad
 x_*={C^2\over4k^2},\quad
 f_k(x_*)=-{C^2\over4k},\quad
 f_k''(x_*)={2k^3\over C^2},
\]
\[
 {e(1/8)\over\sqrt{f_k''(x_*)}}
 A_{h,s}(x_*)e(f_k(x_*))
 ={e(1/8)C\over\sqrt2\,k^{3/2}}
 A_{h,s}(x_*)e\!\left(-{C^2\over4k}\right).
\]
This last display is valid only for a controlled interior saddle; a boundary or transition saddle has an incomplete-Fresnel multiplier.

3. With \(g=(h,s)\), \(h=ga\), and \(s=gb\), the representation is unique; \(g,a,b\) are odd, \((a,b)=1\), and \(b>a\). Moreover,
\[
 r={g(b-a)\over2},\qquad
 (-1)^r=e\!\left({g(b-a)\over4}\right).
\]
At a stationary mode,
\[
 C=J\sqrt g(\sqrt b-\sqrt a),\qquad
 x_*=g{X(\sqrt b-\sqrt a)^2\over4k^2},
\]
and the complete oscillatory factor, including the character sign, is exactly
\[
 e(g\alpha_{a,b,k}),\qquad
 \alpha_{a,b,k}={b-a\over4}
 -{X(\sqrt b-\sqrt a)^2\over4k}.
\]
The exact upper \(k\)-boundary still depends on \(g\). If
\(q_g=\lceil gb/4\rceil\), then
\[
 {J(\sqrt b-\sqrt a)\over2\sqrt a}\le k\le
 {J(\sqrt b-\sqrt a)\over
 \sqrt{\,b+(2+\chi_4(gb))/g\,}}.
\]
Only after suppressing this ceiling transition is the range independent of \(g\).

4. If the admissible lifts form a consecutive odd progression and their sampled weight \(w_g\) has a proved BV bound, partial summation gives a factor controlled by
\[
 \min\{N_g,\|2\alpha\|^{-1}\}
\]
times the appropriate supremum-plus-variation norm. No such conclusion follows for an arbitrary set of lifts or arbitrary sampled weights.

The capacity assertions \(D=O(L^2)\), fixed collars \(O(L^2)\), fixed offsets \(O(L^2)\), and \(G_{a,b}\asymp L/\max(a,b)\) additionally require hypotheses absent from the packet: support geometry/cardinality of scale \(L\), a uniform size bound for \(a(h,m)\), and, for the asymptotic lift length, interval-like support. Under the usual hypotheses \(\#\mathscr H_L=O(L)\), \(h=O(L)\), and \(|a(h,m)|=O(1)\), the stated raw-capacity upper bounds follow. They are not consequences of “actual finite odd support” alone.

## 3. Proof and derivation

Expanding the energy gives
\[
 \mathcal E_L^\top
 =\sum_m\sum_{h,s}
 \chi_4(h)\chi_4(s)a(h,m)\overline{a(s,m)}
 e\!\left(J\sqrt m(\sqrt h-\sqrt s)\right),
\]
with \(m\le h,s\le4m\). The diagonal is exactly
\[
 D=\sum_{h\in\mathscr H_L}
 \sum_{m=\lceil h/4\rceil}^{h}|a(h,m)|^2.
\]
For \(s>h\), oddness gives \(s=h+2r\), and the common \(m\)-range is
\[
 \max(\lceil h/4\rceil,\lceil s/4\rceil)\le m\le\min(h,s),
\]
which is \(q_s\le m\le h\). Pairing this term with the term having \(h,s\) interchanged gives \(2\Re\). Since
\[
 \chi_4(n)=(-1)^{(n-1)/2}\qquad(n\ {\rm odd}),
\]
one has
\[
 \chi_4(h)\chi_4(h+2r)
 =(-1)^{h+r-1}=(-1)^r.
\]
Also,
\[
 J(\sqrt s-\sqrt h)={J(s-h)\over\sqrt h+\sqrt s}
 ={2rJ\over\sqrt h+\sqrt s}=C_{h,r},
\]
which proves the finite phase in (76.2).

For a regular interpolation \(F(x)=A_{h,s}(x)e(-C\sqrt x)\) and distinct integer endpoints \(q<h\), sharp Poisson summation reads, with symmetric convergence,
\[
 \sum_{m=q}^{h}F(m)
 ={F(q)+F(h)\over2}
 +\sum_{n\in\mathbb Z}\int_q^hF(x)e(-nx)\,dx.
\]
Thus full endpoint samples must be recovered by the two half-endpoint terms; when \(q=h\), the one-point interval should be separated before transforming. The phase in mode \(n\) is
\(-C\sqrt x-nx\). Its derivative can vanish only for \(n=-k<0\), giving
\[
 -{C\over2\sqrt{x_*}}+k=0,\qquad x_*={C^2\over4k^2}.
\]
Direct differentiation and substitution give the phase value, \(f_k''(x_*)\), and the \(e(1/8)\) Gaussian in Section 2. The inequalities \(q_s\le x_*\le h\) reverse at the upper endpoint because \(x_*\) decreases with \(k\), yielding the exact integer range in Section 1. At either equality the quadratic Gaussian is one-sided and contributes one half of the full Gaussian at leading order; within a Gaussian width of an endpoint it is replaced continuously by an incomplete Fresnel integral. Modes outside the saddle range remain boundary or nonstationary integrals and do not disappear.

If, additionally, \(h\asymp s\asymp L\), then
\[
 C={2rJ\over\sqrt h+\sqrt s}\asymp {Jr\over\sqrt L},
\]
and both exact saddle boundaries are of order \(Jr/L\). This proves
\(k\asymp Jr/L\) only under that localization, not from an unspecified finite support.

For the gcd variables, uniqueness is the uniqueness of \(g=(h,s)\). Odd \(h,s\) force odd \(g,a,b\), so \(b-a\) is even. Substitution gives all formulas in Section 2. In particular,
\[
 (-1)^r e\!\left(-{C^2\over4k}\right)
 =e\!\left(g\left[{b-a\over4}
 -{X(\sqrt b-\sqrt a)^2\over4k}\right]\right).
\]
The exact ceiling identity
\[
 4q_g=gb+2+\chi_4(gb)
\]
gives the displayed \(g\)-dependent upper boundary. The stationary prefactor is also not constant in the lift: already \(C=J\sqrt g(\sqrt b-\sqrt a)\), and \(A_{ga,gb}(x_*)\), support cutoffs, ceiling transitions, and stationary corrections all move with \(g\).

For \(g=g_0+2j\), the geometric quotient is \(e(2\alpha)\), proving the corrected resonance condition. The explicit half-integer family in Section 1 follows by exact substitution. It stays away from endpoint transitions because
\[
 \left\lceil{49g\over4}\right\rceil
 \le {49g+3\over4}<{81g\over4}<25g
\]
for every positive odd \(g\).

The original-variable phase
\[
 \Theta_k(h,s)={s-h\over4}
 -{X\over4k}(\sqrt s-\sqrt h)^2
\]
is homogeneous of degree one. For
\(Q_0(h,s)=h+s-2\sqrt{hs}\),
\[
 (Q_0)_{hh}={\sqrt s\over2h^{3/2}},\quad
 (Q_0)_{ss}={\sqrt h\over2s^{3/2}},\quad
 (Q_0)_{hs}=-{1\over2\sqrt{hs}},
\]
so \(\det\nabla^2Q_0=0\); the linear term has zero Hessian. Thus \(\Theta_k\) is rank one, with the radial lift direction in its Hessian kernel. There is also an exact Legendre self-return. The stationary transform of \(-C\sqrt m\) is \(-C^2/(4k)\); making \(k\) stationary in
\[
 -{C^2\over4k}-mk
\]
gives \(k=C/(2\sqrt m)\) and returns the value \(-C\sqrt m\). A second transform therefore restores the original phase instead of creating a new nondegenerate two-dimensional oscillation.

For the perfect-power control, take \(X=Q^4\). If
\[
 h=d u^2,\qquad s=d v^2,\qquad m=d w^2
\]
with odd squarefree \(d\) and odd \(u,v\), then both \(J\sqrt{hm}\) and
\(J\sqrt{sm}\) are integers, and the character product is \(1\); these are exact coherent original terms. Their raw number with all three variables \(O(L)\) is at most
\[
 \sum_{d\le cL}O\!\left((L/d)^{3/2}\right)=O(L^{3/2}),
\]
before imposing the common interval, hence below \(L^2\) under unit-size coefficients. In stationary variables the corresponding integer-resonance identity is explicit: for coprime odd \(u<v\le2u\), \(a=u^2,b=v^2\), and an integer \(w\in[v/2,u]\), if
\[
 k={Q^2(v-u)\over2w}\in\mathbb Z,
\]
then \(x_*=gw^2\) and
\[
 \alpha={v-u\over2}
 \left({u+v\over2}-Q^2w\right)\in\mathbb Z.
\]
Thus exact powers genuinely resonate, but their raw exact locus alone is target-safe. No analogous count for near-integer or near-half-integer resonances follows from the packet.

Finally, no coefficient-blind bound can prove (76.4). On any interval-like support with many common \(m\)'s, the bounded adversarial choice
\[
 a(h,m)=\chi_4(h)e(-J\sqrt{hm})
\]
makes every summand of \(R_m\) equal to \(1\). Then
\(\mathcal E_L^\top=\sum_m N_m^2\), where \(N_m\) is the number of admissible \(h\)'s, and this has \(L^3\) capacity when \(N_m\asymp L\) for \(\asymp L\) values of \(m\). The actual top-endpoint symbol must therefore supply indispensable structure; it cannot be replaced by arbitrary bounded coefficients.

## 4. First doubtful or unproved step

The first unproved analytic step occurs immediately after the exact finite identity: the packet passes from the integer-sampled product
\(a(h,m)\overline{a(h+2r,m)}\) to a “smooth interior \(m\)-cell” with an amplitude \(A(x)\), but no interpolation, partition, endpoint convention, derivative bounds, or variation bounds for the actual symbol are supplied.

This omission is structural. Two smooth functions can agree at every sampled integer and differ at \(x_*\) (add a smooth multiple of \(\sin(\pi x)\), for example). Their individual stationary main terms then differ even though the original finite sum is identical; only the complete Poisson ledger, including all modes, endpoints, and errors, is interpolation-invariant. Thus (76.8) cannot yet be called an exact normal form of the actual sampled sum.

Even if that missing interface were supplied, the first false step would be the integer-only resonance condition (76.17). Odd lift parity changes the frequency from \(\alpha\) to \(2\alpha\), and the exact family in Section 1 falsifies the asserted away-from-(76.17) geometric saving.

## 5. Control tests and outcomes

1. **exact_ceiling_stars_and_endpoints — partial pass.** The exact ceiling is
\(q_s=(s+2+\chi_4(s))/4\), the original endpoints have full weight, and sharp Poisson requires two half-endpoint corrections in addition to the integrals. A degenerate one-point interval must be separated. The packet's finite interval is correct, but its candidate transform does not contain the required star/endpoint formula.

2. **diagonal_and_fixed_offsets — conditional pass.** Cauchy gives
\(|\mathcal T_L|^2\le\#\mathscr M\,\mathcal E_L^\top\), so the stated \(L\)-factor requires \(\#\mathscr M\ll L\). The exact diagonal formula is derived above. Under \(O(L)\) support, \(h=O(L)\), and unit-size amplitudes it is \(O(L^2)\); a fixed offset and fixed-width endpoint collar also have \(O(L^2)\) raw capacity. A width \(W\to\infty\) has \(O(WL^2)\) worst-case collar capacity, and \(O(L)\) fixed-offset bounds summed absolutely give \(O(L^3)\). The necessary size/support hypotheses are absent from the packet.

3. **alternating_character_sign — pass.** The exact sign is \((-1)^r\), and it is incorporated into \(e(g\alpha)\) before any absolute value.

4. **Poisson_orientation_and_Gaussian — pass for a controlled interior cell.** With the stated Fourier convention the saddle is at negative mode \(n=-k\); \(x_*\), \(f(x_*)\), \(f''(x_*)\), \(e(1/8)\), and \(C/(\sqrt2\,k^{3/2})\) all check exactly.

5. **endpoint_Fresnel_and_error_sum — fail/unproved.** At an endpoint the full Gaussian in (76.8) is wrong by a factor \(2\) at leading order, and near it an incomplete-Fresnel multiplier is required. No derivative norms, cell widths, nonstationary-mode estimates, or aggregate error bound are supplied, so the complete sum over \((h,r,k)\) cannot be audited.

6. **gcd_parity_and_multiplicity — pass with a warning.** The gcd decomposition is unique and all of \(g,a,b\) are odd. Conversely, every coprime odd \(a<b\) and odd admissible \(g\) gives one pair. The same oddness invalidates (76.17); there is no even-\(g\) lift to remove the half-integer resonance. Exact lift length requires the missing support geometry.

7. **linear_lift_phase — phase pass, resonance refuted.** The formula
\(e(g\alpha_{a,b,k})\) is exact. The exact ceiling makes upper \(k\)-admissibility mildly \(g\)-dependent. On the odd lattice the correct resonance is
\(\|2\alpha\|\lesssim N_g^{-1}\). The explicit
\(X=Q^4,(a,b)=(25,49),k=2Q^2/9\) family is an interior half-integer counterexample to (76.17).

8. **actual_moving_symbol — unproved and essential.** The Gaussian prefactor, sampled amplitude, support, ceiling transition, and corrections all move with \(g\). No BV or comparable norm is available. The adversarial unit-modulus example shows that phase alone cannot imply the target.

9. **rank_one_self_return — pass/no-go.** The Hessian determinant is identically zero, and the one-dimensional Legendre transform returns to \(-C\sqrt m\) on transforming back. No nondegenerate two-variable saving is created.

10. **perfect_power_and_resonance_capacity — mixed.** Exact square/fourth-power resonances exist and were parametrised. Their raw exact coherent locus is \(O(L^{3/2})\) under unit weights, hence by itself is below target capacity. Half-integer lift resonances also exist at fourth powers and are omitted by (76.17). Near-resonance capacity for the actual moving symbol is completely open in the permitted material.

11. **Theorem applicability — not invoked.** No exponent-pair, spacing, spectral, or literature theorem was used; none can be audited from the permitted context.

12. **downstream_scope — pass.** The finite algebra does not prove (76.4), and neither the hard top cone, smooth packets, full \(M2\), \(M9\), nor any global exponent may be promoted from this report.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read:

- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/briefs/blind_signed_offset_rederivation.md
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/derivation_packet.md

No shared proof state, Round-75 material, sibling report, source card, literature, or external theorem was consulted. There was no isolation breach. All controls above are algebraic derivations or exact counting examples contained in this report.

## 7. Recommended state effect

**Revise, with no promotion of (76.4).** Retain the exact finite offset identity (76.2), sign (76.3), negative-mode saddle and interior Gaussian (with its restricted validity), gcd parametrisation (76.11)–(76.13), and exact linear lift phase (76.14). Replace the ceiling-free \(k\)-range by the exact range when formulating a finite lemma, and require a complete star/Fresnel/error ledger tied to a specified interpolation of the actual symbol.

Reject (76.17) as stated. Any lift lemma must sum on the odd lattice and use
\(\|2\alpha_{a,b,k}\|\), retaining both integer and half-integer resonance branches, as well as the actual moving sampled weight and the \(g\)-dependent ceiling transition. The exact perfect-power locus is capacity-safe by itself, but the near-resonant actual-symbol survivor remains unresolved. The appropriate proof-state effect is therefore to retain the algebraic reduction as candidate evidence, revise its resonance interface, and make no downstream state change.

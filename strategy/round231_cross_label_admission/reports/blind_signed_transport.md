# 1. Result: exact signed transfer and an information-content no-go

Campaign/task: Prelaunch231 / `blind_signed_transport`. Role: statement-only independent rederiver. Graph provenance tag supplied by the brief: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Generated: 2026-10-11. This report uses no graph, history, sibling report, literature, or numerical experiment.

The elementary transfer is exact before absolute values are taken. If `H_T` is the cumulative discrepancy between the measure and its smooth reference, the transfer costs one power of `T` against a uniform cumulative-discrepancy bound:

\[
\mathcal L_T(\mu_T)-\mathcal L_T(\rho_T\,dx)
=T\int_{\mathbb R}\widehat w'(-u)H_T(u/T)\,du.
\]

Consequently, global discrepancy `O(T^{4/25+epsilon})` suffices for the requested `O(T^{29/25+epsilon})` bound after subtracting the continuum. A weighted discrepancy near the frequency scale `1/T` also suffices, with explicitly controlled tails. A fixed-width window `|Tx|<=W` alone does not suffice.

A continuum density `A_T ell_T^{-1} q(x/ell_T)`, with fixed Schwartz `q`, `ell_T` comparable to `sqrt(T)`, and polynomially bounded `|A_T|`, has a contribution decaying faster than every prescribed power of `T`. A suitable band-limited Schwartz smoothing can be subtracted with exactly zero contribution, even when the original measure has nonzero total mass.

These facts do not yield the requested estimate from total mass and a coarse square-root discrepancy law. There are nonnegative, even, smooth measures of mass `T^3`, with cumulative discrepancy of order `T^{3/2}` from their broad continuum reference, whose integrated Fourier contribution has order `T^{5/2}`. The discrepancy bound is the square root of their mass. More strongly, the same obstruction can be realized as a deterministic convolution of twelve nonnegative measures, each satisfying a cumulative discrepancy bound much smaller than the square root of its own mass. The construction is an abstract control, not an arithmetic counterexample.

# 2. Exact statement and hypotheses

Write `e(t)=exp(2 pi i t)` and

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e(-\xi x)\,dx.
\]

Take `T>=1` and fixed `w in C_c^infinity(R)` supported in `[1/2,2]`. The case `w=0` is trivial; the sharpness controls below assume `w` is not identically zero. The arguments permit complex `w`. Define

\[
K_T(x)=T\widehat w(-Tx),\qquad
\mathcal L_T(\mu)=\int w(R/T)\int e(Rx)\,d\mu(x)\,dR
=\int K_T(x)\,d\mu(x).
\]

The symbol `ell_T` denotes the continuum length, to avoid confusing it with the functional `mathcal L_T`.

Let `mu_T` be any finite signed or complex Borel measure, let `rho_T in L^1(R)` be a reference density, and set

\[
\nu_T=\mu_T-\rho_T\,dx,\qquad
H_T(x)=\nu_T(( -\infty,x]),\qquad M_T=\|\nu_T\|_{\rm TV}.
\]

Every constant implicit below may depend on the fixed test functions and on displayed fixed comparison constants, but not on `T`. For the continuum conclusion assume

\[
\rho_T(x)=\frac{A_T}{\ell_T}q(x/\ell_T),\quad q\in\mathcal S(\mathbb R),\quad
c_1\sqrt T\le\ell_T\le c_2\sqrt T,\quad |A_T|\le T^3.
\]

If `A_T` is understood to be nonnegative, `A_T<=T^3` is equivalent to the amplitude hypothesis used here. A one-sided upper bound without nonnegativity is not a bound on the magnitude of a signed amplitude.

The following are sufficient discrepancy hypotheses, each giving the requested bound after continuum subtraction:

* `inf_c ||H_T-c||_infinity = O_epsilon(T^{4/25+epsilon})`;
* more generally,
  \[
  \inf_c\int|\widehat w'(-u)|\,|H_T(u/T)-c|\,du
  =O_\epsilon(T^{4/25+\epsilon});
  \]
* for any fixed `delta>0`, `M_T=O(T^3)` and a constant `c_T`, with `|c_T|=O(M_T)`, such that
  \[
  \sup_{|x|\le T^{-1+\delta}}|H_T(x)-c_T|
  =O_\epsilon(T^{4/25+\epsilon}).
  \]

The last condition can instead be stated as the same bound for interval discrepancies `nu_T((-T^{-1+delta},x])` with `|x|<=T^{-1+delta}`; choose `c_T=H_T(-T^{-1+delta})`. The half-open interval convention explicitly excludes an atom at its left endpoint.

# 3. Proof and derivation

## Signed integration by parts, signs, atoms, and endpoints

The derivative is

\[
K'_T(x)=-T^2\widehat w'(-Tx)
=2\pi i\int Rw(R/T)e(Rx)\,dR.
\]

Because `K_T` and `K'_T` are Schwartz and `nu_T` has finite variation, Fubini gives

\[
\begin{aligned}
-\int K'_T(x)H_T(x)\,dx
&=-\int\!\left(\int_{y}^{\infty}K'_T(x)\,dx\right)d\nu_T(y)\\
&=\int K_T(y)\,d\nu_T(y).
\end{aligned}
\]

Absolute integrability for this application follows from
`integral |K'_T(x)| |nu_T|((-infinity,x]) dx <= M_T ||K'_T||_1`.
Thus

\[
\boxed{\mathcal L_T(\nu_T)=T^2\int\widehat w'(-Tx)H_T(x)\,dx
=T\int\widehat w'(-u)H_T(u/T)\,du.}
\]

There is no missing minus sign and no missing factor of `T`. Since `integral K'_T=0`, any constant `c` can replace the cumulative baseline:

\[
\mathcal L_T(\nu_T)=T\int\widehat w'(-u)[H_T(u/T)-c]\,du.
\]

No zero-total-mass hypothesis is needed. At `+infinity`, `H_T` tends to `nu_T(R)`, which is bounded, while `K_T` tends to zero. At `-infinity`, `H_T` tends to zero. Both boundary terms vanish.

For a finite atomic measure `sum_j a_j delta_{x_j}`, the same proof is the identity
`-sum_j a_j integral_{x_j}^infinity K'_T(x) dx = sum_j a_j K_T(x_j)`.
Atoms have their full weights, including an atom at zero or at any specified cutoff. The value assigned to a cumulative function at a jump is irrelevant to its Lebesgue integral against `K'_T`.

If one truncates an integration-by-parts argument to `[a,b]`, the exact formula is

\[
\int_{(a,b]}K_T\,d\nu_T
=K_T(b)H_T(b)-K_T(a)H_T(a)-\int_a^b K'_T(x)H_T(x)\,dx.
\]

An integral over `[a,b]` requires adding `K_T(a)nu_T({a})`. Discarding endpoint terms in a finite-interval argument is unjustified.

The absolute certificate obtained from the signed identity is

\[
|\mathcal L_T(\nu_T)|\le
T\int|\widehat w'(-u)|\,|H_T(u/T)-c|\,du
\le T\|\widehat w'\|_1\|H_T-c\|_\infty.
\]

The certificate is sufficient, not necessary: cancellation in the exact signed integral may make the result much smaller. The factor `T` cannot be improved uniformly over finite measures. Choose a fixed `u_0` with `widehat w(-u_0) != 0` and use `nu_T=m_T delta_{u_0/T}`. Its cumulative discrepancy has size comparable to `|m_T|`, while `|mathcal L_T|=T|m_T widehat w(-u_0)|`.

For completeness, Holder also gives, whenever the displayed norm is finite,

\[
|\mathcal L_T(\nu_T)|\le
T^{1+1/p}\|\widehat w'\|_{p'}\|H_T-c\|_p,
\qquad 1\le p\le\infty.
\]

Thus an unweighted `L^p` cumulative norm of size `T^{4/25-1/p+epsilon}` suffices. For finite `p`, such a global norm is usually unavailable if the discrepancy has nonzero total mass; subtracting a single constant cannot eliminate two different limiting values. The bounded or weighted formulation avoids this issue. Even zero total mass by itself need not give integrability without additional tail information.

Because `w` vanishes near zero, all moments of `K_T` vanish. Consequently `integral K'_T P=0` for every polynomial `P`, and the signed formula also permits subtracting a polynomial baseline. This can sharpen a locally smooth discrepancy analysis, but it supplies no bound on the remaining oscillatory discrepancy.

## Local discrepancy and tails

For every `W>=1` and every constant `c`, put
`D_T(W,c)=sup_{|x|<=W/T}|H_T(x)-c|`. Schwartz decay gives, for every prescribed `N`,

\[
|\mathcal L_T(\nu_T)|\le
T\|\widehat w'\|_1D_T(W,c)
+C_{w,N}T(M_T+|c|)W^{-N}.
\]

This proves the local sufficient condition in Section 2 by taking `W=T^delta` and, for example, `N>71/(25 delta)` when `M_T=O(T^3)`. The tail is then smaller than `T^{29/25}`. A logarithmically growing cutoff is not automatically enough to absorb an arbitrary polynomial mass bound using only unspecified Schwartz constants.

For a fixed `W>0`, a claim that the exterior tail is asymptotically negligible is false without further information. Choose fixed `u_0>W` with `widehat w(-u_0) != 0`, and set `nu_T=T^3 delta_{u_0/T}`. Such a `u_0` exists because the Fourier transform of a nonzero compactly supported smooth function cannot vanish on an entire exterior interval. The cumulative discrepancy is exactly zero throughout `|x|<=W/T`, but the window integral has size comparable to `T^4`.

## Smooth continuum subtraction

The continuum Fourier transform is

\[
F_{\rho_T}(R)=A_T\widehat q(-\ell_TR),\qquad
\mathcal L_T(\rho_T\,dx)
=A_TT\int w(s)\widehat q(-\ell_TTs)\,ds.
\]

Since `s>=1/2` on the physical support, for every `N`,

\[
|\mathcal L_T(\rho_T\,dx)|
\le C_{q,w,N}|A_T|T(1+\ell_TT)^{-N}
\le C_{q,w,N,c_1}T^{4-3N/2}.
\]

For every `B>0`, choosing `N` large proves `O_B(T^{-B})`. The reference need not have zero total mass. Its mass is a contribution at physical frequency zero, and the physical test window stays away from zero.

The signed continuum integral must not be replaced by its absolute certificate. For a nonnegative `q` with `q(0)>0`,

\[
\int|K_T(x)|\rho_T(x)\,dx
=\frac{A_T}{\ell_T}\int|\widehat w(-u)|q(u/(T\ell_T))\,du
\asymp\frac{A_T}{\ell_T}
\]

when `A_T>0` and `w` is nonzero. This can be of order `T^{5/2}`, while the signed continuum contribution is rapidly negligible.

## Exact low-frequency smoothing subtraction

Choose a Schwartz kernel `kappa` with `integral kappa=1` and Fourier support contained in `[-B_0,B_0]`. A real even kernel is available; it may also be chosen nonnegative by squaring and normalizing the inverse transform of a real even smooth compactly supported bump. Put

\[
\kappa_h(x)=h^{-1}\kappa(x/h),\qquad h>0.
\]

For any finite measure,

\[
F_{\mu*\kappa_h}(R)=F_\mu(R)\widehat\kappa(-hR).
\]

If `hT/2>B_0`, the multiplier vanishes throughout the physical window, so

\[
\boxed{\mathcal L_T(\mu)=\mathcal L_T(\mu-\mu*\kappa_h).}
\]

Taking a strict inequality avoids endpoint conventions. Equality also causes no problem for a smooth compactly supported multiplier, but is unnecessary. Both the natural choice `h=C/T`, `C>2B_0`, and a much broader choice `h` comparable to `sqrt(T)` are admissible.

The discrepancy measure here has exactly zero total mass, even if the original measure has nonzero mass. If `J(v)=integral_{-infinity}^v kappa(z) dz`, its cumulative function is exactly

\[
H_h(x)=\int\left[\mathbf1_{y\le x}-J((x-y)/h)\right]d\mu(y).
\]

It tends to zero at both infinities and obeys

\[
\|H_h\|_\infty\le(1+\|\kappa\|_1)\|\mu\|_{\rm TV},\qquad
\|H_h\|_1\le h\|\mu\|_{\rm TV}\int|z\kappa(z)|\,dz.
\]

For the second estimate, express `H_h` as the average of `H_mu(x)-H_mu(x-z)` against `kappa_h(z)dz` and use
`integral |H_mu(x)-H_mu(x-z)| dx <= |z| ||mu||_TV`.
This is valid for atoms and requires no moment assumption on `mu`.

Exact subtraction is therefore legitimate but is not a discrepancy estimate. Its automatic bounds, with `h` of order `1/T`, yield only a bound of order `T ||mu||_TV`. The smoothed density depends on the full original measure; it cannot be identified with a prescribed universal profile merely from its total mass.

## What the supplied mass information cannot imply

The scalar signed mass `mu_T(R)=O(T^3)` does not even control variation: arbitrarily large multiples of `delta_a-delta_b` have zero total mass. Even under the stronger interpretation `||mu_T||_TV=O(T^3)`, the automatic bound is only `O(T^4)`.

Nor can products be declared independent. For twelve measures and references, deterministic convolution telescoping gives

\[
\Big\|H_{*_{i=1}^{12}\mu_i-*_{i=1}^{12}\rho_i}\Big\|_\infty
\le\sum_{i=1}^{12}\|H_{\mu_i-\rho_i}\|_\infty
\prod_{j<i}\|\mu_j\|_{\rm TV}\prod_{j>i}\|\rho_j\|_{\rm TV}.
\]

This follows from the exact telescoping identity and `H_{sigma*eta}=H_sigma*eta`. If all masses equal `T^{1/4}` and each one-factor error is at most the square root of that mass, this elementary estimate has size `T^{23/8}`, nowhere near `T^{4/25}`. This upper-bound calculation alone is not a no-go theorem; the explicit coherent construction below supplies the no-go.

# 4. First doubtful or unproved step

There is no unproved step in the abstract transfer, continuum estimate, exact smoothing identity, or modulation control as stated. Their role is deliberately limited.

The first unsupported step in any route to the target from the stated coarse hypotheses would be to infer a cumulative discrepancy of size `T^{4/25+epsilon}` at resolution `1/T`, or an equally strong bound for its signed weighted transform. Neither total mass, a smooth coarse density law, nor one-factor square-root cumulative errors implies this. Exact low-frequency subtraction does not create that estimate.

Application to an arithmetic measure would require additional structural information suppressing coherent Fourier modulation near physical frequencies `R` of order `T`, or an independently proved cancellation estimate for the signed discrepancy integral. No arithmetic mechanism is assumed or established here.

# 5. Required control test and outcome

All controls in this section are analytical identities and inequalities. No numerical experiments were performed.

## Nonnegative modulation with identical coarse smoothed density

Choose fixed, real, even, nonnegative Schwartz `q`, with `integral q=1`, `q(0)>0`, and `supp qhat subset [-B,B]`. Such a function is obtained by the squared-bump construction described above. Fix `0<b<1` and a point `c in (1/2,2)` with `w(c) != 0`. Let

\[
\ell=\sqrt T,\quad A=T^3,\quad R_0=cT,\quad
\rho(x)=\frac A\ell q(x/\ell),\qquad
\mu(dx)=\rho(x)[1+b\cos(2\pi R_0x)]\,dx.
\]

For sufficiently large `T`, this is a nonnegative even measure of exactly the same mass `A` as `rho dx`; the extra mass vanishes because `qhat(ell R_0)=0`. Its variation is also `A`. The Fourier transform of the discrepancy is exactly

\[
F_{\mu-\rho dx}(R)=\frac{bA}{2}
\left[\widehat q(-\ell(R-R_0))+\widehat q(-\ell(R+R_0))\right].
\]

Thus it has a peak of height `bA/2` near `R_0`, with physical width of order `1/ell`. The negative-frequency peak and the continuum peak at zero are disjoint from the positive physical window. Direct substitution gives

\[
\mathcal L_T(\mu)
=\frac{bA}{2\ell}\int w(c+u/(\ell T))\widehat q(-u)\,du
=\frac{bA}{2\ell}\left[w(c)q(0)+O((\ell T)^{-2})\right].
\]

The first-order term vanishes because `qhat` is even. Therefore

\[
|\mathcal L_T(\mu)|\asymp A/\ell=T^{5/2}.
\]

Two integrations by parts in the cumulative discrepancy give, uniformly for all real `x`,

\[
H(x)=\frac{bA}{2\pi R_0\ell}q(x/\ell)\sin(2\pi R_0x)
+O_q\!\left(\frac{bA}{R_0^2\ell^2}\right).
\]

The error bound follows from bounded `q'` and integrable `q''`. Evaluating near `x=1/(4R_0)` gives the matching lower bound, so

\[
\|H\|_\infty\asymp\frac{bA}{R_0\ell}\asymp T^{3/2}=\sqrt A.
\]

The relative cumulative error is `O(T^{-3/2})`, despite the large integrated Fourier contribution. The factor-`T` discrepancy transfer is attained in order of magnitude.

The same coarse smoothing law can hold exactly. For a kernel `kappa_h` as above, if
`h(R_0-B/ell)>B_0`, the multiplier `kappahat(hR)` annihilates both discrepancy bands. Hence

\[
\mu*\kappa_h=\rho*\kappa_h
\]

identically. In particular, smoothing at any scale `h` with `hT` tending to infinity cannot detect the added oscillation. Frequency-line resolution of order `1/T`, with a passband reaching `R_0`, is needed. At that resolution the relevant cumulative size is `bA/(T ell)`, not merely an unspecified relative density error. For `A=T^3` and `ell=sqrt(T)`, the discrepancy criterion for the target would require `b=O(T^{-67/50+epsilon})`; fixed `b` is ruled out by the target but allowed by the coarse hypotheses.

Outcome: the coarse-density implication is refuted. This control remains nonnegative and has the required real/even symmetry, so cancellation of arbitrary signed masses is not responsible for the failure.

## Twelve deterministic factors, each better than a square-root CDF law

Set `m=T^{1/4}` and use twelve identical factor measures and references

\[
d\mu_i(x)=\frac m\ell q(x/\ell)[1+b\cos(2\pi R_0x)]\,dx,
\qquad d\rho_i(x)=\frac m\ell q(x/\ell)\,dx.
\]

Each measure is nonnegative of mass `m` and each cumulative discrepancy has size

\[
\|H_{\mu_i-\rho_i}\|_\infty\asymp\frac{m}{T\ell}=T^{-5/4},
\]

which is much smaller than `sqrt(m)=T^{1/8}`. No random or independence hypothesis is used.

The three Fourier bands of a factor are disjoint for large `T`. Their twelfth power therefore has no mixed-band terms. Writing `Q=q^{*12}`, exact Fourier inversion gives

\[
*_{i=1}^{12}\mu_i(dx)
=\frac{T^3}{\ell}Q(x/\ell)
\left[1+2(b/2)^{12}\cos(2\pi R_0x)\right]dx,
\]

while the convolution of the references is `T^3 ell^{-1} Q(x/ell) dx`. The same calculation as before yields

\[
\mathcal L_T(*_{i=1}^{12}\mu_i)
=\frac{T^3}{\ell}(b/2)^{12}
\left[w(c)Q(0)+O((\ell T)^{-2})\right],
\]

with `Q(0)>0`. Its magnitude is again comparable to `T^{5/2}`. The convolution reference remains a fixed Schwartz profile at a length comparable to `sqrt(T)`.

Outcome: one-factor square-root cumulative bounds do not exclude common, coherently placed Fourier peaks, even in a twelve-factor convolution with product mass `T^3`.

## Finite-atom version and endpoint control

The nonnegative modulation control can be replaced by finite atoms. Choose `N` equal-mass quantile atoms of its distribution, of weight `A/N`, with symmetric choices if even symmetry is desired. Their cumulative distribution differs from that of the smooth measure by at most `A/N`. The already-proved transfer bounds the resulting change in the window integral by

\[
C_wTA/N.
\]

Taking `N/(T ell)` tending to infinity makes this error `o(A/ell)`, preserving the `T^{5/2}` obstruction and its CDF scale. All atomic endpoint contributions are covered by the full-weight Stieltjes identity above.

Outcome: restricting to finite atomic measures does not repair the coarse-information implication. This remains an abstract atomization and makes no claim about allowable arithmetic locations or coefficients.

# 6. Dependencies and exact artifacts used

Read exactly these files:

1. `strategy/round231_cross_label_admission/briefs/blind_signed_transport.md`.
2. `protocol.md`.
3. `strategy/round231_cross_label_admission/briefs/isolated_transport.md`.

No other packet, graph, historical, sibling, or literature context was read. The report depends only on elementary Fourier scaling, finite-measure Fubini, integration by parts, Schwartz decay, Fourier inversion, and deterministic convolution algebra. The compact-Fourier-support nonnegative Schwartz functions were constructed explicitly, rather than imported as a specialized theorem. There is no computational evidence to reproduce; effort was entirely analytical apart from writing and hashing the report.

The sole output artifact is `strategy/round231_cross_label_admission/reports/blind_signed_transport.md`.

# 7. Recommended state effect

Recommend retaining, or promoting after the conductor's required seam review, only the precisely stated elementary transfer, continuum negligibility, and exact smoothing-subtraction lemmas. Record the modulation construction as an information-content obstruction to deriving the target from mass and coarse cumulative square-root laws alone.

Do not promote the target estimate or any arithmetic cancellation claim on the basis of these lemmas. A useful next mathematical interface, if selected by the conductor in a later round, would have to supply the missing signed weighted discrepancy bound or an explicit structural prohibition of coherent modulation. This report does not initiate a new round and edits no authoritative state.

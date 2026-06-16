Summary:

Round 8 is a precision round, not an exponent-improvement round. No new bound for the Gauss circle problem has been proved.

The main conclusion is that the balanced hyperbola/Vaaler route should remain the primary reduction framework, but its status is now: **structured reduction with a sharply identified bottleneck**, not a near-proof. The central bottleneck is the fixed-Fejer residual target H5r-F. Round 8 adds several useful algebraic and analytic diagnostics around that bottleneck:

1. R4 gives an exact Abel-summation identity for Fejer weights, clarifying why fixed Fejer averages may behave like partial-sum estimates unless their special averaging is exploited directly.
2. C2 gives a convention-fixed odd-lattice Poisson transform.
3. C2-SP gives the correct leading stationary-phase form, but the uniform error bookkeeping still needs repair, especially distinguishing dual length $M\asymp kX/D^2$ from stationary-phase parameter $\Lambda\asymp kX/D$.
4. B-Boundary shows the very small-$k$ boundary regime is harmless after the $1/H_D$ Vaaler normalization.
5. Q1-Ext gives a useful exact congruence factorization for near-collision character products, but it is an algebraic input, not an analytic saving until inserted into an actual Bombieri--Iwaniec/Li--Yang matrix.
6. C3-Ext gives a coefficient-collapse lemma for translation-invariant differencing in the two-coset odd-lattice dual model, but it is not a universal obstruction to all spacing methods.
7. Mellin--Perron should remain a comparison route, not a primary pivot. The sharp-Perron and functional-equation diagnostics suggest it reconstructs Hardy/Voronoi/Bessel-type sums, but the exact smoothed theorem and kernel analysis remain unwritten.

Source anchor: uploaded Round 8 packet and cross-reviews.

Selected main route:

Keep the selected route:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{local dyadic reciprocal sums}.
$$

The target remains

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The official local Vaaler scale remains

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

The official minimal residual target remains H5r-F. For residual families

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
$$

and

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\},
$$

H5r-F asks for

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

The correct implication chain is still

$$
\mathrm{H5r\text{-}B}
\Longrightarrow
\mathrm{H5r\text{-}F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not reverse either implication. H5r-F is formally weaker than H5r-B, but Round 8 sharpened the warning that many plausible proofs of H5r-F may silently pass through partial-sum or arbitrary-coefficient estimates and thereby lose the fixed-Fejer advantage.

The next round should not pivot away from this bottleneck. It should audit it more strictly:

1. reference-check H4, the exact Vaaler theorem;
2. prove the full two-sided residual-to-H5r-F implication with constants;
3. test whether H5r-F is genuinely easier than H5r-B/L1;
4. only then compare signed Fourier and Mellin--Perron alternatives.

Useful fragments by source:

## From `gpt_pro_thinking`

The most valuable contribution is the precise R4 Abel-summation diagnostic.

For one-sided positive frequencies, define

$$
A(j)=\sum_{1\le k\le j}a_k.
$$

Then

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}
\sum_{j=1}^{H}A(j).
$$

Applied to $a_k=S_\star(k,D)$, this proves that any proof of H5r-F based only on bounding all partial sums

$$
A(j)=\sum_{1\le k\le j}S_\star(k,D)
$$

inherits the same type of difficulty as H5r-B. This is a diagnostic, not an equivalence theorem: H5r-F may still be easier if a proof exploits the fixed Fejer averaging or the joint $(k,d)$ phase structure directly.

The second useful contribution is the clean comparison of truncation mechanisms:

| Method | Replacement error | Character preservation | Status |
|---|---|---|---|
| Vaaler with Fejer majorant | H5r-F, or stronger H5r-B/L1 | Main terms retain $\chi_4$; residual becomes parity-supported or untwisted | Main reduction; central bottleneck |
| Signed Fourier truncation | High-frequency signed reciprocal tail | Formally preserves $\chi_4$ longer | No endpoint tail estimate |
| Sharp Perron | Truncation error for $4\zeta(s)L(s,\chi_4)X^s/s$ | Preserves arithmetic in Dirichlet series | Comparison route; sharp truncation likely costly |
| Smoothed Perron | Smoothed contour kernel | Preserves arithmetic before functional equation | Theorem dependencies unwritten |
| Poisson--Bessel calibration | Smoothing annulus plus Bessel tail | Geometric, not $\chi_4$-driven | Sanity check only |

The third useful contribution is the signed Fourier tail formula. For the first leg, after truncating

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h},
$$

one obtains the formal high-frequency tail

$$
\mathcal T_1(D)
=
4\sum_{|h|>H_D}
\frac{1}{2\pi i h}
\sum_{d\sim D}
\chi_4(d)w_D(d)e(hX/d).
$$

For the second leg,

$$
\mathcal T_2(D)
=
-4\sum_{|h|>H_D}
\frac{e(h/4)-e(3h/4)}{2\pi i h}
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the signed tails formally preserve character structure. But no valid endpoint-strength tail estimate is known. If the tail is bounded absolutely, the route likely recreates an H5r/L1-type obstruction.

The Poisson--Bessel calibration module is also useful and should be inserted as a secondary sanity check:

$$
E(R)\ll R\delta+R^{1/2}\delta^{-1/2},
$$

and choosing

$$
\delta=R^{-1/3}
$$

recovers

$$
E(R)\ll R^{2/3}.
$$

This is not part of the main proof route.

## From `gemini_deep_think`

The most valuable contribution is Q1-Ext, the near-collision character factorization.

Let $(a,b)=1$, let $d_1,d_2$ be odd, and suppose

$$
d_1b-d_2a=\Delta.
$$

Then:

1. If $a,b$ are odd, then $\Delta$ is even and

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

2. If $a$ is even and $b$ is odd, then $\Delta$ is odd and

$$
d_1\equiv b(a+\Delta)\pmod 4.
$$

Thus $\chi_4(d_1)$ is frozen by $a,b,\Delta$, and the product is a fixed sign times $\chi_4(d_2)$.

3. If $a$ is odd and $b$ is even, then symmetrically $d_2$ is frozen modulo $4$, and the product is a fixed sign times $\chi_4(d_1)$.

This is a real algebraic refinement of the earlier exact-collision lemma. Its correct status is: **proved congruence lemma, analytic use pending**. It does not by itself prove cancellation. The next test is whether the $\Delta$-dependent sign survives the first Cauchy--Schwarz, double large sieve, or spacing-matrix absolute-value step in a Bombieri--Iwaniec/Li--Yang framework.

The second useful contribution is C3-Ext. In the two-coset odd-lattice dual representation, write

$$
\xi\in \frac12\mathbb Z,
\qquad
\sigma(\xi)=\frac12(-1)^{2\xi}.
$$

For a translation shift

$$
q=\xi_1-\xi_2,
$$

one has

$$
\sigma(\xi_1)\sigma(\xi_2)
=
\frac14(-1)^{2q}.
$$

Thus the coefficient parity sign factors out of the internal location variable in translation-invariant differencing. Correct status: **proved coefficient-collapse lemma for translation-invariant A-process arguments; diagnostic, not a universal obstruction**.

The third useful contribution is the Mellin--Perron diagnostic. Sharp Perron suggests that to force endpoint error one needs height around

$$
T\asymp X^{3/4}
$$

under the usual sharp truncation heuristic. Applying functional equations plausibly produces a Hardy/Voronoi-type dual length

$$
N\asymp X^{1/2}
$$

and a degenerate phase of the form

$$
\Phi(h,d)\asymp \sqrt{Xhd}.
$$

This is useful as a warning, but it should not be recorded as a proved "analytic isomorphism." The smoothed kernel, incomplete gamma transition, residues, and uniform stationary phase must be written before H10 can be promoted.

## From `deepseek_api`

The strongest contribution is the convention-fixed C2 odd-lattice Poisson transform. With

$$
F(u)=w_D(u)e(kX/u)
$$

and

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du,
$$

one has

$$
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu).
$$

This should be promoted as an algebraic transform.

The second useful contribution is the leading stationary-phase calculation. For $\xi=-m<0$,

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
\phi(u_0)=2\sqrt{kXm},
\qquad
\phi''(u_0)=\frac{2m}{u_0}.
$$

Thus the expected leading term is

$$
I(-m)
\sim
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right),
$$

with amplitude

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}
$$

when

$$
m\asymp \frac{kX}{D^2}.
$$

However, the error term and uniformity must be recomputed with the two parameters separated:

$$
M\asymp \frac{kX}{D^2}
\quad\text{dual length,}
$$

and

$$
\Lambda\asymp \frac{kX}{D}
\quad\text{large stationary-phase parameter after scaling }u=Dv.
$$

Round 8 correctly identifies the scale, but the lemma bank should not yet record the claimed relative error as final.

The third useful contribution is B-Boundary. If

$$
D\asymp X^{1/2}
$$

and $|k|\le C$ is bounded, then

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\ll
\frac{D}{H_D}
\asymp X^{1/4},
$$

and the same holds for $S_\rho$. This handles the very small-$k$ edge without stationary phase.

The fourth useful contribution is N1: derivative nondegeneracy for shifted reciprocal phases. For

$$
F_{2,1}(x)=\frac1{x+1/D}
$$

one has

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
-6(x+1/D)^{-6}\ne0.
$$

For

$$
F_2(x)=\frac1{4x},
$$

one has

$$
F_2'F_2'''-3(F_2'')^2
=
-\frac38x^{-6}\ne0.
$$

This confirms structural compatibility with reciprocal-sum phase classes.

N2, however, must be downgraded. It is correct that $S_{\mathrm{odd}}$ and $S_\rho$ map structurally into a Li--Yang/Bombieri--Iwaniec reciprocal double-sum phase class. It is not yet proved in the repo that the exact theorem applies to H5r-F with the required fixed coefficients, weights, absolute-value placement, local ranges, and endpoint strength. Record N2 as **structural compatibility pending theorem-level audit**.

Rejected or risky ideas:

1. **Reject: any claim of a new Gauss circle exponent.**

Round 8 proves no estimate of the form

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

and no improvement over existing known exponents.

2. **Reject: H5r-F is equivalent to H5r-B.**

R4 shows that monotone Fejer weights can be expressed through partial sums. It does not prove that fixed Fejer averaging is equivalent to arbitrary bounded coefficients or dyadic $L^1$. A direct method may still exploit the fixed Fejer structure.

3. **Reject: H5r-F is automatically easier than H5r-B.**

Because

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}A(j),
$$

proofs via partial sums may inherit H5r-B-type difficulty. This remains a serious diagnostic obstruction.

4. **Reject: the Vaaler positive-majorant route is unconditionally "analytically blocked."**

It is blocked only under current character-blind or Li--Yang-level reciprocal-sum inputs. The formal possibility remains that fixed Fejer averaging admits a stronger direct estimate.

5. **Reject: Li--Yang theorem-level applicability has been fully audited.**

The phase shape matches. The exact theorem hypotheses, coefficient classes, allowed weights, local parameter ranges, and norm placement still need to be checked. Do not record "Li--Yang directly applies to H5r-F" as proved.

6. **Reject: C3-Ext ends the two-coset question.**

C3-Ext proves parity coefficient collapse for translation-invariant differencing. It does not rule out non-translation, multiplicative, spectral, or spacing methods that use more than the coefficient sign.

7. **Reject: Mellin--Perron is an analytic isomorphism or a definitive dead end.**

Sharp Perron and functional-equation diagnostics suggest the route reconstructs Hardy/Voronoi/Bessel sums. But no full smoothed Perron theorem with kernel analysis and endpoint bounds has been written. Keep H10 as a comparison route.

8. **Reject: signed Fourier truncation is a failed candidate.**

It is undeveloped and likely difficult, but not falsified. The correct status is: character-preserving formal alternative with no endpoint tail bound.

9. **Reject: C2-SP is fully proved with uniform errors.**

The leading stationary point, phase, and amplitude are correct at scaling level. Uniform error terms, endpoint transitions, and dependence on $M$ versus $\Lambda$ remain gaps.

10. **Reject: Q1-Ext alone provides analytic cancellation.**

Q1-Ext is exact congruence arithmetic. It becomes analytically useful only if a spacing or large-sieve argument preserves the $\Delta$-dependent sign rather than applying absolute values too early.

Known gaps:

1. **Exact H4 Vaaler theorem reference.**

The proof draft still needs a standard, reference-checked finite Vaaler theorem with:

- exact coefficients;
- exact Fejer majorant normalization;
- treatment of $\psi(n)=-1/2$ at discontinuities;
- two-sided handling of positive and negative frequencies.

2. **Full H5r-F sufficiency with constants.**

ALG-1 is correct at the scaffold level, but the proof draft must sum over:

- both sawtooth legs;
- both residual families $S_{\mathrm{odd}}$ and $S_\rho$;
- $k>0$ and $k<0$;
- all dyadic $D$;
- zero and nonzero Fejer modes;
- endpoint blocks.

3. **H5r-F versus H5r-B/L1 gap.**

R4 is exact, but the key unresolved question is whether fixed Fejer averaging gives real cancellation beyond partial-sum estimates. This must be tested both numerically and theoretically.

4. **C2-SP uniformity.**

The leading stationary phase should be rewritten in scaled variables:

$$
u=Dv,
\qquad
\Lambda\asymp \frac{kX}{D},
\qquad
M\asymp \frac{kX}{D^2}.
$$

The error term, transition layer, support-boundary behavior, and integration-by-parts decay must be stated uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le k\le H_D.
$$

5. **Boundary and transition ranges.**

B-Boundary handles bounded $k$ when $D\asymp X^{1/2}$. It does not by itself cover all regimes where

$$
kX/D^2\asymp 1
$$

or where the stationary point is close to the edge of support.

6. **Li--Yang/Bombieri--Iwaniec theorem audit.**

The structural phase map is not enough. The exact theorem must be checked against:

- fixed Fejer coefficients versus arbitrary coefficients;
- smooth dyadic $w_D$;
- parity coefficients;
- frequency shifts $e(k\rho/4)$;
- local ranges $K_0\le D X^{-1/4}$;
- blockwise absolute values;
- whether the theorem yields the required $X^{1/4+\epsilon}$ scale or only a larger exponent in the current packet.

7. **Q1-Ext in actual spacing matrices.**

The sign

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

or the frozen-residue alternatives must be inserted into a real rational-collision or near-collision matrix. The main question is whether summation over $\Delta$ preserves the sign or whether standard matrix norm estimates erase it.

8. **C3 beyond translation differencing.**

Need to test non-translation or two-coset spacing arguments. C3-Ext only covers translation-invariant A-process models.

9. **Signed Fourier tail.**

The formal tails $\mathcal T_1(D)$ and $\mathcal T_2(D)$ preserve character structure, but no summability or high-frequency cancellation theorem has been stated. This is the main gap for the non-majorizing Fourier alternative.

10. **Mellin--Perron comparison module.**

Need exact sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

including contour shifts, residues, truncation errors, functional equation, gamma factors, incomplete-kernel transition, and resulting dual sums.

11. **Numerical stress tests.**

No actual numerical tests have been run yet for H5r-F, H5r-B, H5r-L1, Fejer spikes, signed Fourier tails, or near-collision sign persistence.

New lemmas to add:

## R4. Fejer averaging / Abel-summation identity

**Status:** proved algebraic identity; diagnostic use only.

For any sequence $a_k$ and

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}A(j).
$$

Application: H5r-F can be proved from partial-sum bounds, but such a proof may inherit H5r-B-type difficulty. This does not prove equivalence between H5r-F and H5r-B.

## ALG-1. Vaaler residual leads to H5r-F

**Status:** proved conditional on H4.

Assuming the Vaaler residual satisfies the Fejer majorant with the normalization used in the proof draft, each dyadic residual block is bounded by the zero mode

$$
D/H_D\asymp X^{1/4}
$$

plus fixed-Fejer combinations of $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$. Therefore H5r-F is the minimal fixed-coefficient target naturally produced by the Vaaler route.

## C2. Odd-lattice Poisson transform

**Status:** proved algebraic transform under fixed Fourier convention.

With

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du,
$$

one has

$$
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu).
$$

## C2-SP. Leading stationary phase for C2

**Status:** leading term accepted; uniform error pending.

For $\xi=-m<0$,

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
I(-m)
\sim
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right),
$$

with active dual length

$$
m\asymp \frac{kX}{D^2}
$$

and amplitude

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

The final lemma must distinguish this dual length from the stationary-phase parameter

$$
\Lambda\asymp \frac{kX}{D}.
$$

## B-Boundary. Small-$k$ residual boundary

**Status:** proved elementary lemma.

For

$$
D\asymp X^{1/2},
\qquad
|k|\le C,
$$

one has

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\ll X^{1/4},
$$

and similarly for $S_\rho$. More generally, $O(X^\epsilon)$ such frequencies are harmless after absorbing $X^\epsilon$.

## N1. Reciprocal derivative nondegeneracy

**Status:** proved algebraic lemma.

For

$$
F_{2,1}(x)=\frac1{x+1/D},
$$

one has

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
-6(x+1/D)^{-6}.
$$

For

$$
F_2(x)=\frac1{4x},
$$

one has

$$
F_2'F_2'''-3(F_2'')^2
=
-\frac38x^{-6}.
$$

## N2. H5r-to-reciprocal-sum structural compatibility

**Status:** structural mapping; theorem-level audit pending.

The sums $S_{\mathrm{odd}}$ and $S_\rho$ lie in the reciprocal phase class after residue splitting and scaling. This supports comparison with Bombieri--Iwaniec/Li--Yang-type estimates. It does not yet prove that the precise theorem applies to H5r-F with the required weights and norms.

## Q1-Ext. Near-collision character factorization

**Status:** proved congruence lemma; analytic use pending.

Let $(a,b)=1$, let $d_1,d_2$ be odd, and suppose

$$
d_1b-d_2a=\Delta.
$$

Then:

- if $a,b$ are odd,

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2};
$$

- if $a$ is even and $b$ is odd, then $d_1\bmod4$ is fixed by $a,b,\Delta$ and the product is a fixed sign times $\chi_4(d_2)$;
- if $a$ is odd and $b$ is even, then $d_2\bmod4$ is fixed by $a,b,\Delta$ and the product is a fixed sign times $\chi_4(d_1)$.

This lemma should be tested inside actual spacing matrices.

## C3-Ext. Two-coset parity coefficient collapse

**Status:** proved for translation-invariant differencing; diagnostic only.

For

$$
\xi\in \frac12\mathbb Z,
\qquad
\sigma(\xi)=\frac12(-1)^{2\xi},
$$

translation differencing gives

$$
\sigma(\xi_1)\sigma(\xi_2)
=
\frac14(-1)^{2(\xi_1-\xi_2)}.
$$

The sign is independent of the inner location variable. This blocks coefficient-level parity gains for direct translation A-process models, but it does not rule out non-translation or spectral spacing methods.

## SF1. Signed Fourier truncation tail

**Status:** formal comparison lemma; no bound proved.

The signed Fourier route replaces H5r by high-frequency tails $\mathcal T_1(D)$ and $\mathcal T_2(D)$ that formally preserve $\chi_4$. Its viability depends on proving endpoint-strength tail cancellation without absolute values.

## H10-A. Sharp Perron truncation diagnostic

**Status:** conditional diagnostic.

For the Dirichlet series

$$
4\zeta(s)L(s,\chi_4),
$$

sharp Perron truncation suggests height around

$$
T\asymp X^{3/4}
$$

to target $X^{1/4+\epsilon}$ errors under standard crude truncation heuristics. This must be replaced by exact sharp and smoothed Perron statements before use.

## H10-B. Mellin--Perron / Hardy--Voronoi comparison

**Status:** proposed diagnostic mapping, not theorem.

Applying functional equations plausibly reconstructs dual Bessel/Voronoi sums of length about

$$
X^{1/2}
$$

and phase

$$
\sqrt{Xhd}.
$$

This supports the warning that Mellin--Perron may mirror the same hard reciprocal/Bessel structure. It is not an impossibility theorem.

Counterexample checks to run:

1. **H5r norm comparison.**

For square, nonsquare, and near-square $X$, compute

$$
R_F(D)
=
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
$$

and compare it with

$$
R_{L1}(D)
=
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

A persistent gap would support the possibility that fixed Fejer averaging helps. Comparable sizes would support the H5r-B bottleneck.

2. **Fejer spike test.**

Choose $X,d$ such that one of

$$
X/d,
\qquad
\frac{X/d+1}{4},
\qquad
\frac{X/d+3}{4}
$$

is close to an integer. Check whether $K_{H_D}$ spikes produce large residual blocks.

3. **R4 partial-sum simulation.**

Compute

$$
A(j)=\sum_{1\le k\le j}S_\star(k,D)
$$

and verify numerically whether

$$
\frac1{H_D(H_D+1)}\sum_{j\le H_D}A(j)
$$

behaves closer to fixed Fejer cancellation or to arbitrary-coefficient/L1 norms.

4. **C2 convention test.**

Numerically or symbolically verify

$$
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu)
$$

for compactly supported test weights.

5. **C2 stationary-phase test.**

For

$$
I(-m)=\int w_D(u)e(kX/u+mu)\,du,
$$

test the leading approximation

$$
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right)
$$

with

$$
u_0=\sqrt{kX/m}.
$$

Separate tests by regimes:

$$
M=\frac{kX}{D^2}\asymp 1,
\qquad
M\gg1,
\qquad
\Lambda=\frac{kX}{D}\gg1.
$$

6. **B-Boundary test.**

For $D\asymp X^{1/2}$ and $1\le |k|\le X^\epsilon$, verify that the total contribution after division by $H_D$ is

$$
\ll X^{1/4+\epsilon}.
$$

7. **Q1-Ext stress test.**

For near-collisions

$$
d_1b-d_2a=\Delta,
$$

test the predicted character signs over many coprime $(a,b)$ and gaps $\Delta$. Then insert those signs into a mock spacing matrix and determine whether Cauchy--Schwarz or absolute values erase them.

8. **C3 two-coset spacing test.**

Apply both translation differencing and a non-translation/multiplicative differencing model to the two-coset dual expression. Check whether any phase-spacing distinction survives after the parity sign factors out.

9. **Signed Fourier tail test.**

Attempt to bound

$$
\mathcal T_1(D)+\mathcal T_2(D)
$$

without absolute values. Record exactly where any proof is forced to reintroduce H5r-like character-blind sums.

10. **Mellin--Perron reconstruction test.**

Write sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

shift contours, extract the pole at $s=1$, apply functional equations, and derive the resulting dual Bessel/Voronoi sums. Determine whether $\chi_4$ remains usable or is reorganized into the same hard reciprocal/Bessel structure.

11. **Li--Yang theorem audit.**

Take the precise theorem statement and check it against:

$$
K_0\le H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2},
$$

with fixed Fejer weights, parity restrictions, smooth $d$-weights, frequency shifts, and blockwise absolute values.

Next round instructions:

## For `gpt_pro_thinking`

1. Produce a reference-checked H4 statement, including exact Vaaler coefficients, Fejer majorant normalization, and discontinuity convention for the floor-compatible sawtooth.

2. Rewrite ALG-1 as a full proof over all dyadic blocks, both signs of $k$, both H3 legs, zero mode, and nonzero mode. State exactly where H5r-F enters.

3. Insert R1--R4, ALG-1, C1, C2, B-Boundary, N1, Q1-Ext, C3-Ext, SF1, H10-A, and H10-B into the best proof draft with the statuses above.

4. Build the actual H5a spacing-matrix test using Q1-Ext. The output should show whether the $\Delta$ sign survives through the first Cauchy--Schwarz / double-large-sieve reduction.

5. Keep Mellin--Perron as a comparison module, not a primary replacement route, until a smoothed Perron theorem and functional-equation kernel analysis are written.

## For `gemini_deep_think`

1. Redraft Q1-Ext with all parity assumptions explicit and downgrade any analytic conclusion to "pending insertion into a spacing estimate."

2. Redraft C3-Ext as "translation-invariant coefficient collapse," not as a proof that all two-coset spacing fails.

3. Develop the H10 Mellin--Perron module with exact sharp and smoothed Perron truncation errors, residues, functional equation, and kernel transition terms. Avoid terms such as "isomorphism" unless an actual equivalence theorem is proved.

4. Test whether non-translation differencing or multiplicative shifts can preserve information in the two-coset formulation after C3-Ext.

## For `deepseek_api`

1. Run numerical comparisons of H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.

2. Verify the C2 stationary phase under the convention $e(t)=e^{2\pi i t}$, but separate the two scales

$$
M\asymp \frac{kX}{D^2}
$$

and

$$
\Lambda\asymp \frac{kX}{D}.
$$

3. Formulate a uniform transition lemma for C2, including support-boundary stationary points and the regime $M\asymp1$.

4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem and state whether it applies to H5r-F itself, only to H5r-B, or only to a still stronger norm.

5. Recheck N2 with exact parameter normalization. Do not state theorem-level applicability until the coefficient and norm hypotheses have been matched line by line.

Confidence:

High confidence in the continued selection of the balanced hyperbola/Vaaler route as the main reduction and diagnostic framework.

High confidence that no exponent improvement has been proved.

High confidence that H5r-F remains the official minimal residual target.

High confidence in R4 as an exact algebraic identity and as a useful diagnostic.

High confidence in C2 as a convention-fixed Poisson transform.

High confidence in B-Boundary for bounded or $X^\epsilon$ many small frequencies after Vaaler normalization.

High confidence in Q1-Ext and C3-Ext as algebraic lemmas under their stated hypotheses.

Moderate confidence in the C2-SP leading stationary-phase formula; lower confidence in the stated error terms until the $M$ versus $\Lambda$ bookkeeping is fixed.

Moderate confidence that H5r residual sums are structurally reciprocal/divisor-like.

Low confidence that current Li--Yang/Bombieri--Iwaniec inputs reach the endpoint H5r-F target as needed here.

Low confidence that signed Fourier truncation can be made to work without recreating H5r-type absolute-value losses.

Low confidence that Mellin--Perron avoids the same Hardy/Voronoi/Bessel bottleneck, but it remains useful as a comparison module.

Overall Round 8 judgment: successful obstruction mapping and lemma cleanup. The next round should not claim a pivot or a solution. It should lock down H4/ALG-1, run the H5r norm tests, audit Li--Yang at theorem level, and test whether Q1-Ext survives inside an actual signed spacing matrix.

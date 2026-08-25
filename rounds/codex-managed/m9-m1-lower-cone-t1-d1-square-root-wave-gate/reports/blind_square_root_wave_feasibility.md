## Result

**No-go for the tested mechanisms; not a counterexample to the scalar target.**  Put (R_0=N^{1/4}), so (R_0\asymp R).  Exact character Poisson summation followed by uniform stationary phase gives

\[
 P(W_M)=i e(-1/8)R_0^{-1}
 \sum_{\substack{k>0\\ k\ \operatorname{odd}}}
 \chi _4(k)W_M\!\left(\frac{4N}{k^2}\right)e(N/k)
 +E_{\mathrm{sp}},                                      \tag{1}
\]

where the effective dual length is

\[
 K\asymp R_0^2M^{-1/2}\asymp R^2M^{-1/2},
 \qquad
 E_{\mathrm{sp}}=o_{\mathcal W}(R_0^{-1}K)
\]

at the level of the summed stationary capacity.  The qualitative profile clause does not expose enough seminorm and transition constants to certify a sharper absolute power; any target-safe rate for \(E_{\mathrm{sp}}\) requires the supplied profile ledger.  Applying the same transform to the dual main term returns the original leading term, including the constants and eighth-root phases.  Thus the main transformation is self-reciprocal, not a shortening iteration.

The resulting capacity bounds are only

\[
 |P(W_M)|\ll_{\mathcal W}
 \min\{M^{1/4},\;R_0M^{-1/2}+|E_{\mathrm{sp}}|\}.                \tag{2}
\]

A square-root estimate for the dual wave would suffice, but it is exactly the missing assertion:

\[
 \sum_{k\asymp K,\ k\ \operatorname{odd}}
 \chi _4(k)V(k)e(N/k)\ll_\varepsilon R_0N^\varepsilon,
 \qquad V(k)=W_M(4N/k^2).                           \tag{3}
\]

Indeed the stronger natural estimate (\ll K^{1/2}N^\varepsilon) would make the right side of (1) (\ll M^{-1/4}N^\varepsilon).  Adjacent pairing does not give (3), one legal differencing step removes the character completely from every correlation, the squarefree-kernel split has near-resonance spacing too weak on (M\le R_0^2), and Mellin plus the functional equation reproduces (1).  Consequently the literal (N^\varepsilon) target is **not proved uniformly in the remaining growing range** by these data and mechanisms.  This conclusion does not assert that the scalar estimate is false.

## Exact statement and hypotheses

Take (N\in\mathbb Z_{>0}), (R_0=N^{1/4}), (R\asymp R_0), and (1\ll M\le R^2\asymp R_0^2).  Interpret the qualitative profile clause in the supplied statement in the standard uniform sense: there are fixed (0<c<C<\infty) and fixed seminorm bounds such that

\[
 \operatorname{supp}W_M\subset[cM,CM],
 \qquad |(x\partial_x)^jW_M(x)|\le C_j
\]

for every derivative order used below, with the supplied transition-width, stationary-buffer, tail, literal-boundary, and zero-extension conventions.  Constants may depend on these fixed data, denoted by (\mathcal W), but not on (N) or (M).  The same calculations apply to a fixed finite dilation of ([M,2M]).  Write (e(x)=e^{2\pi ix}) and extend (x^{-3/4}W_M(x)e(\sqrt{Nx})) by zero off the positive support.

The statement tested is only

\[
 \left|\sum_{\substack{\ell>0\\ \ell\ \operatorname{odd}}}
 \chi _4(\ell)\ell^{-3/4}W_M(\ell)e(\sqrt{N\ell})\right|
 \ll_\varepsilon N^\varepsilon.                    \tag{4}
\]

Bounded (M) and the separately owned range (M^{819}\gg R^{1424}) are not assessed.  No conclusion is drawn for a larger kernel, an unsigned analogue, or any downstream claim.

## Proof/derivation

1. **Exact adjacent-odd pairing.**  Let

\[
 a(x)=x^{-3/4}W_M(x),\qquad F(x)=a(x)e(\sqrt{Nx}).
\]

Because (\chi _4(4j+1)=1), (\chi _4(4j+3)=-1), and the zero extension fixes all boundary terms,

\[
 P(W_M)=\sum_{j\in\mathbb Z}\{F(4j+1)-F(4j+3)\}.   \tag{5}
\]

For every contributing odd (\ell\), the bracket is exactly

\[
 F(\ell)-F(\ell+2)
 =e(\sqrt{N\ell})
 \left[a(\ell)-a(\ell+2)e(\delta_\ell)\right],
\]

\[
 \delta_\ell
 =\sqrt N\bigl(\sqrt{\ell+2}-\sqrt\ell\bigr)
 =\frac{2\sqrt N}{\sqrt{\ell+2}+\sqrt\ell}
 \asymp R_0^2M^{-1/2}.                                \tag{6}
\]

There is no uniform small factor: (\delta_\ell\) is uncontrolled modulo one.  The literal Abel form makes the loss explicit:

\[
 F(\ell)-F(\ell+2)
 =-\int_\ell^{\ell+2}e(\sqrt{Nx})
 \left(a'(x)+\pi i\sqrt N\,x^{-1/2}a(x)\right)dx. \tag{7}
\]

Summing absolute values in (7) has capacity

\[
 M\left(M^{-7/4}+R_0^2M^{-5/4}\right)
 \ll M^{-3/4}+R_0^2M^{-1/4},                          \tag{8}
\]

which is worse than the original capacity (M^{1/4}).  Thus adjacent pairing alone cannot exploit (\chi _4).

2. **One legal differencing step and the exact character loss.**  Parameterize the odd integers by (\ell=2n+1).  Since (\chi _4(2n+1)=(-1)^n=e(n/2)), set

\[
 u_n=a(2n+1)e\!\left(\sqrt{N(2n+1)}+\frac n2\right),
 \qquad P=\sum_nu_n.
\]

For (1\le H\ll M), van der Corput's finite differencing inequality is legal with the zero extension and gives

\[
 |P|^2\le \frac{L+H-1}{H}
 \left(\sum_n|u_n|^2
 +2\sum_{1\le h<H}\left(1-\frac hH\right)|C_h|\right),
 \quad L\asymp M,                                  \tag{9}
\]

where

\[
 C_h=\sum_n a(2n+2h+1)\overline{a(2n+1)}
 e\!\left(g_h(n)+\frac h2\right),                 \tag{10}
\]

\[
 g_h(n)=\sqrt N\left(\sqrt{2n+2h+1}-\sqrt{2n+1}\right).
\]

The character product is exactly

\[
 \chi _4(2n+2h+1)\chi _4(2n+1)=(-1)^h,             \tag{11}
\]

which is independent of (n).  Hence every off-diagonal correlation in (9) is an **untwisted** square-root-difference sum.  On its common support,

\[
 g_h\asymp hR_0^2M^{-1/2},\qquad
 g_h'\asymp-hR_0^2M^{-3/2},\qquad
 g_h''\asymp hR_0^2M^{-5/2}.                          \tag{12}
\]

The standard second-derivative estimate, including the normalized weights, yields

\[
 |C_h|\ll_{\mathcal W}
 R_0h^{1/2}M^{-7/4}+R_0^{-1}h^{-1/2}M^{-1/4}.           \tag{13}
\]

As (\sum|u_n|^2\ll M^{-1/2}), substitution in (9) gives the one-step bound

\[
 |P|^2\ll_{\mathcal W}
 \frac{M^{1/2}}H
 +R_0M^{-3/4}H^{1/2}
 +R_0^{-1}M^{3/4}H^{-1/2}.                            \tag{14}
\]

Making the diagonal term (N^{o(1)}) forces (H\ge M^{1/2}N^{-o(1)}).  The middle term supplied by (13) is then at least at the level (R_0M^{-1/2}N^{-o(1)}), which is (N^{o(1)}) only at (M\ge R_0^2N^{-o(1)}).  Thus this legal one-step route closes only at the upper endpoint and loses the only stated arithmetic sign before its hard estimate.

3. **Squarefree-kernel split and exact resonances.**  Every positive odd (\ell\) has a unique representation

\[
 \ell=ts^2,\qquad
 \operatorname{odd}(t),\quad \operatorname{squarefree}(t),\quad
 \operatorname{odd}(s).
\]

Since (\chi _4(s^2)=1),

\[
 P(W_M)=\sum_{\substack{t\ \operatorname{odd}\\t\ \operatorname{squarefree}}}
 \chi _4(t)t^{-3/4}
 \sum_{s\ \operatorname{odd}}s^{-3/2}W_M(ts^2)e(s\sqrt{Nt}). \tag{15}
\]

For (S_t\asymp(M/t)^{1/2}\ge1), Abel summation of the inner odd-(s) progression gives

\[
 \left|\sum_{s\ \operatorname{odd}}s^{-3/2}W_M(ts^2)e(s\sqrt{Nt})\right|
 \ll_{\mathcal W}S_t^{-3/2}
 \min\left\{S_t,\|2\sqrt{Nt}\|^{-1}\right\}.      \tag{16}
\]

If (Nt) is not a square, integrality gives only

\[
 \|2\sqrt{Nt}\|\gg (Nt)^{-1/2}.                   \tag{17}
\]

But (S_t\le\sqrt{Nt}) throughout (M\le R_0^2=\sqrt N).  Therefore (17) never improves the trivial (S_t) alternative uniformly.  After absolute values, (16) returns precisely

\[
 M^{-3/4}\sum_{t\ll M}S_t\ll M^{1/4}.              \tag{18}
\]

Now write (N=dq^2) with (d) squarefree.  The exact full inner resonance (Nt=\square) occurs iff (t=d); it occurs in (15) only when (d) is odd.  On that block (e(s\sqrt{Nd})=e(sdq)=1), while its absolute scalar capacity is only

\[
 d^{-3/4}\sum_{s\asymp\sqrt{M/d}}s^{-3/2}|W_M(ds^2)|
 \ll_{\mathcal W}d^{-1/2}M^{-1/4}.                 \tag{19}
\]

For two terms (\ell_1=ts^2), (\ell_2=ur^2),

\[
 \ell_1\ell_2=\square\quad\Longleftrightarrow\quad t=u. \tag{20}
\]

The absolute weighted capacity of all such square-product pairs is

\[
 \sum_{\substack{t\ll M\\t\ \operatorname{odd}\ \operatorname{squarefree}}}
 t^{-3/2}
 \left(\sum_{s\asymp\sqrt{M/t}}s^{-3/2}|W_M(ts^2)|\right)^2
 \ll_{\mathcal W}M^{-1/2}\log(2M).                 \tag{21}
\]

In the actual square ( |P|^2 ), a same-kernel pair carries phase

\[
 e\bigl((s-r)\sqrt{Nt}\bigr).
\]

It is identically one for all (s,r) only on the (t=d) block (when (d) is odd); otherwise only the diagonal (s=r) is automatically one.  Equations (19) and (21) are absolute capacities, not signed lower bounds for (P).

4. **Exact character-Poisson transform, endpoint powers, and self-return.**  For

\[
 \widehat F(\xi)=\int_{\mathbb R}F(x)e(-\xi x)\,dx,
\]

Poisson summation in the four residue classes and

\[
 \sum_{a\bmod4}\chi _4(a)e(ak/4)=2i\chi _4(k)
\]

give the exact identity

\[
 P(W_M)=\frac i2\sum_{k\in\mathbb Z\atop k\ \operatorname{odd}}
 \chi _4(k)\int_0^\infty x^{-3/4}W_M(x)
 e\!\left(\sqrt{Nx}-\frac{kx}{4}\right)dx.         \tag{22}
\]

Only (k>0) has a stationary point, namely

\[
 x_k=\frac{4N}{k^2},\quad
 \Phi_k(x_k)=\frac Nk,\quad
 \Phi_k''(x_k)=-\frac{k^3}{32N}.                    \tag{23}
\]

Moreover

\[
 x_k^{-3/4}|\Phi_k''(x_k)|^{-1/2}=2R_0^{-1}.          \tag{24}
\]

Uniform stationary phase in (22) gives the main term in (1), with the relative remainder stated above.  The phase parameter, derivatives, and stationary width on the original side are

\[
 \Lambda\asymp\sqrt{NM}=R_0^2M^{1/2},\qquad
 f'\asymp R_0^2M^{-1/2},\qquad
 f''\asymp R_0^2M^{-3/2},\qquad
 \Delta x\asymp R_0^{-1}M^{3/4}.                     \tag{25}
\]

On the dual side,

\[
 K\asymp R_0^2M^{-1/2},\qquad
 (N/k)'\asymp-M,\qquad
 (N/k)''\asymp M^{3/2}R_0^{-2},\qquad
 \Delta k\asymp R_0M^{-3/4}.                         \tag{26}
\]

The original and dual main-term absolute capacities are respectively (M^{1/4}) and (R_0^{-1}K=R_0M^{-1/2}), giving the two capacities displayed in (2).  If (M=R^\alpha), (0<\alpha\le2), the residual (R)-power from (2) is

\[
 R^{\min\{\alpha/4,\,1-\alpha/2\}}.               \tag{27}
\]

The two capacities meet at (M=R^{4/3}), where they are (R^{1/3}).  At (M=R^2) the dual capacity is (1).  At the formal boundary (M=R^{1424/819}) of the separately owned large-(M) range, the dual capacity is still

\[
 R^{1-712/819}=R^{107/819}.                        \tag{28}
\]

For bounded or subpolynomial (M), the original capacity is already (N^{o(1)}), but (27) has a positive power at every fixed interior (0<\alpha<2).

To see the self-return exactly, put

\[
 T=\sum_{k>0,\ k\ \operatorname{odd}}\chi _4(k)W_M(4N/k^2)e(N/k).
\]

Applying character Poisson to (T), stationary points occur only at negative dual frequencies (m=-\ell), at

\[
 k_\ell=2\sqrt{N/\ell},\quad
 N/k_\ell+\ell k_\ell/4=\sqrt{N\ell},\quad
 |(N/k+\ell k/4)''_{k=k_\ell}|^{-1/2}=2R_0\ell^{-3/4}.
\]

Since (\chi _4(-\ell)=-\chi _4(\ell)),

\[
 T=-i e(1/8)R_0 P(W_M)+E_{\mathrm{inv}}.                  \tag{29}
\]

The main constants in (1) and (29) multiply to one.  The qualitative profile assumptions give only an \(o_{\mathcal W}(1)\)-relative remainder at the summed stationary-capacity level, namely \(E_{\mathrm{inv}}=o_{\mathcal W}(R_0M^{1/4})\); a target-safe absolute rate and endpoint-tail constants require the supplied profile ledger.  Hence a second (B)-transform is the original problem, not a new estimate.

5. **Mellin and functional-equation test.**  Let

\[
 H(x)=W_M(x)e(\sqrt{Nx}),\qquad
 \widetilde H(s)=\int_0^\infty H(x)x^{s-1}\,dx.
\]

For (\Re s>1/4), Mellin inversion gives

\[
 P(W_M)=\frac1{2\pi i}\int_{(\sigma)}
 \widetilde H(s)L(s+3/4,\chi _4)\,ds.               \tag{30}
\]

The completed beta function

\[
 \Lambda(z)=\left(\frac4\pi\right)^{(z+1)/2}
 \Gamma\!\left(\frac{z+1}{2}\right)L(z,\chi _4)
\]

satisfies (\Lambda(z)=\Lambda(1-z)), equivalently

\[
 L(z,\chi _4)=\left(\frac4\pi\right)^{1/2-z}
 \frac{\Gamma((2-z)/2)}{\Gamma((z+1)/2)}
 L(1-z,\chi _4).                                    \tag{31}
\]

On shifting (30) to (\Re s=-1/4), the Mellin transform is stationary only for

\[
 |\Im s|\asymp T:=\sqrt{NM}=R_0^2M^{1/2},
 \qquad
 |\widetilde H(-1/4+i\tau)|\asymp_{\mathrm{cap}}
 M^{-1/4}T^{-1/2}.                                  \tag{32}
\]

Inserting (31) and evaluating the gamma and Mellin kernels by stationary phase gives the reciprocal wave (1); applying (31) twice gives (29).  Thus the functional equation is the same self-return in Mellin coordinates.  Even a mean-square-capacity estimate on the critical line gives (T^{1/2}M^{-1/4}=R_0), not (1); the missing cancellation is between the (L)-values and the stationary Mellin kernel and is equivalent to the signed reciprocal-wave estimate (3).

## First doubtful or unproved step

Conditional on the supplied profile ledger making the stationary remainders target-safe, the first genuinely unavailable analytic step is the uniform signed estimate (3), or an equivalent estimate for the untwisted correlations \(C_h\) in (10) that is stronger than (13).  The statement-only qualitative profile clause does not itself certify absolute remainder powers, so that seam also cannot be promoted from this report.  The equality (11) shows why the obvious (A)-process cannot use (\chi _4): after one shift the character has become the constant ((-1)^h).  The (B)-process and the beta functional equation then return to the starting wave.  The squarefree split offers an equivalent possible interface—an aggregate signed theorem for the frequencies (2\sqrt{Nt}\)—but the individual spacing bound (17) is too weak everywhere on (M\le R_0^2).

Accordingly, asserting square-root cancellation in (3), cancellation among the (t)-blocks in (15), or cancellation among the (C_h) would be the first unproved step.  Absolute capacities such as (19) or (21) cannot supply it.

## Required control test and outcome

1. **Character-algebra control — pass.**  Directly from (\chi _4(2n+1)=(-1)^n), the shifted product is (\chi _4(2n+2h+1)\chi _4(2n+1)=(-1)^h).  This verifies that (10) has no residual (n)-character.

2. **Transform round-trip control — pass.**  The forward stationary constant is (iR_0^{-1}e(-1/8)); the inverse constant is (-iR_0e(1/8)).  Their product is (1), and (4N/k_\ell^2=\ell).  Thus the apparent dualization cannot be counted as two independent gains.

3. **Exact-resonance control — pass.**  Writing (N=dq^2), the only squarefree kernel with (Nt) square is (t=d), and it is present only if (d) is odd.  Its scalar capacity is (d^{-1/2}M^{-1/4}), while the full square-product-pair capacity is (O(M^{-1/2}\log(2M))).  Neither is a signed lower bound for the whole scalar.

4. **Absolute/adversarial control — fail for any absolute-value proof.**  The total coefficient mass is (\asymp M^{1/4}) for a nonnegative unit-size profile.  If arbitrary phases were allowed to align with the coefficients, that capacity would be attained.  Therefore an argument that discards (\chi _4) and all oscillatory signs cannot prove (4) in a polynomially growing interior range.  This is only a falsification of that proof strategy, not a lower bound for the actual (P(W_M)).

5. **Endpoint-power control — pass.**  Formula (27) gives (1) at the two already benign limiting mechanisms only when (M=N^{o(1)}) on the original side or (M=R^2N^{o(1)}) on the dual side; it gives the explicit positive obstructions (R^{1/3}) at (M=R^{4/3}) and (R^{107/819}) at (M=R^{1424/819}).

These are exact algebraic and asymptotic controls; no numerical experiment is used as certification.

## Dependencies/exact artifacts

Statement-only isolation is explicitly certified.  I read exactly these two artifacts:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/blind_statement.md`.

I did not read the proof graph, active campaign, strategy, barrier packet, briefs, Round 151 material, sibling reports, state files, source cards, validation or synthesis artifacts, or any other repository file.  I used no web source and no prior-round result.  The derivation depends only on elementary character algebra, Poisson summation, one-dimensional stationary phase under the supplied profile hypotheses, one legal van der Corput differencing inequality, unique squarefree-kernel decomposition, and the displayed functional equation of the primitive character (\chi _4).  I wrote only this assigned report.

## Recommended state effect

**Retain the scalar target as open; no proof-state promotion and otherwise no change.**  Record the route-level no-go: adjacent pairing has uncontrolled increments, the first legal differencing step loses the character, square-product resonances are small absolute capacities rather than signed lower bounds, and both Poisson and Mellin/functional-equation duality self-return.  Any later promotion should require a genuinely new proof of the signed reciprocal-wave bound (3), or an equivalent aggregate squarefree-frequency estimate, with a separate audit of the exact profile seminorms and both endpoints.




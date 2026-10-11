# Round215: blind spatial-kernel rederivation

Campaign: `gc-complete-localized-wave-moment`  
Task/role: `blind_spatial_kernel`; statement-only independent rederivation  
Round: 215  
Generated: 2026-09-28 (local date)  
Supplied graph hash, metadata only: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`  
Context isolation: only `protocol.md` and `briefs/blind_spatial_kernel_statement.md` were read. A conductor message clarified that the central lower-bound cubes include `[-1,1]^2` and `[-1,1]`. No graph, manifest, strategy, other report, historical file, or web source was opened. No numerical experiment was run.

## 1. Result: exact identities and a positive-certificate no-go

The exact expansion retains a spatial Fourier factor at the bounded frequency `(sum m - sum n)/sqrt(N)`, a radial Fourier factor at `sqrt(N)(sum |m| - sum |n|)`, and every center modulation. The two positive upper certificates requested in the packet satisfy, for each fixed choice of the cutoffs and all sufficiently large `T`,

\[
\mathcal C(T,N)\le U_2(T,N)\le U_1(T,N),\qquad
U_1(T,N)\gtrsim T N^2,\qquad U_2(T,N)\gtrsim N^{5/2}.
\]

The constants are allowed to depend on the fixed cutoff functions and mass constants. The estimates are uniform on every fixed closed subband of `166/325 < alpha < 242/325`, with `N=T^alpha`. In fact, the algebraic identities and certificate estimates need only the simpler range `1 <= N <= T^2`, apart from an eventual lower threshold for `N` in the spatial Fourier lemma.

At every fixed `alpha > 166/325`, the lower bound for even the phase-first certificate `U_2` exceeds `T^(83/65+epsilon)` for sufficiently small positive `epsilon`. Consequently, neither of these particular positive certificates can establish an estimate of that form with an arbitrarily small epsilon loss. This does **not** disprove that estimate for the actual signed moment `C`.

There is an unconditional weighted trace implication. Using the conductor's clarified central lower bound on `[-1,1]`, the summed radial windows cover the whole target interval uniformly. Consequently the unweighted tenth moment on that interval is at most a constant times `N^(-1/2) C(T,N)`.

## 2. Exact statements and hypotheses

Use the Fourier convention

\[
\widehat h(\xi)=\int h(x)e(-x\cdot\xi)\,dx,
\qquad e(t)=\exp(2\pi i t).
\]

Let `T>=2`, `1<=N<=T^2` be real, and let finitely supported coefficients indexed by `m in Z^2` satisfy

\[
 a_m\ge0,\quad a_m=0\ \text{unless}\ \sqrt N\le |m|\le2\sqrt N,
 \quad c_0N^{1/4}\le S:=\sum_m a_m\le C_0N^{1/4},
 \quad a_m\le C_aN^{-3/4}.
\]

The coefficient cap is consistent with the setting but is not needed in the certificate lower-bound proofs. In particular, no arithmetic origin, randomness, or independence of the coefficients is assumed.

For the exact identities and certificate claims, let `phi` on `R^2` and `eta` on `R` be fixed real Schwartz functions, with compact Fourier supports, `phi(0)=eta(0)=1`, and positive lower bounds in modulus on fixed neighborhoods of zero. For the interval trace only, use the conductor's explicit clarification that the lower-bound cubes include `[-1,1]^2` for `phi` and `[-1,1]` for `eta`. Let

\[
 W(y)=C_W(1+|y|^2)^{-100},\quad C_W>0,\quad
 a=1/\sqrt2,\quad d=\sqrt3-a,
\]
\[
 J=\lceil dT/\sqrt N\rceil,\qquad R_j=aT+j\sqrt N\quad(0\le j\le J).
\]

The functions `F`, `f_j`, and `C` are exactly those in the packet. Define

\[
 G_N(y)=W(y)\phi(y/N)^{10},\quad K_N(\xi)=\widehat{G_N}(\xi),
 \qquad H(v)=\widehat{\eta^{10}}(v),
\]
\[
 D_J(v)=\sum_{j=0}^J e(jv),\qquad
 \Theta_{T,N}(R)=\sum_{j=0}^J\left|\eta\left(\frac{R-R_j}{\sqrt N}\right)\right|^{10}.
\]

For ordered five-tuples `p=(m_1,...,m_5)` and `q=(n_1,...,n_5)` put

\[
 b_p=\prod_{i=1}^5a_{m_i},\quad M_p=\sum_{i=1}^5m_i,\quad
 r_p=\sum_{i=1}^5|m_i|,
\]
\[
 A_{p,q}=b_pb_q,\qquad k_{p,q}=M_p-M_q,\qquad
 \rho_{p,q}=r_p-r_q.
\]

Repeated indices are allowed. The full support bounds are

\[
 |k_{p,q}|\le20\sqrt N,\quad 5\sqrt N\le r_p\le10\sqrt N,
 \quad |\rho_{p,q}|\le5\sqrt N,\quad \sum_pb_p=S^5.
\]

The exact certificates are

\[
 U_1=N\sum_{p,q}A_{p,q}\sum_{j=0}^J
 \left|e(R_j\rho_{p,q})K_N(-k_{p,q}/\sqrt N)H(-\sqrt N\rho_{p,q})\right|
\]
\[
 \hspace{7mm}=N(J+1)\sum_{p,q}A_{p,q}
 |K_N(-k_{p,q}/\sqrt N)|\,|H(-\sqrt N\rho_{p,q})|,
\]
\[
 U_2=N\sum_{p,q}A_{p,q}|K_N(-k_{p,q}/\sqrt N)|\,
 |H(-\sqrt N\rho_{p,q})|\,|D_J(\sqrt N\rho_{p,q})|.
\]

These definitions take moduli at precisely the two stages specified in the packet. They do not silently discard any frequency difference.

## 3. Proof and derivation

### 3.1 The tenth expansion and the true Fourier scales

Because the cutoffs are real, their tenth powers equal their tenth absolute powers. Expanding `F^5 conjugate(F)^5` gives the finite identity

\[
 |f_j(y,u)|^{10}
 =\phi(y/N)^{10}\eta(u/N)^{10}
 \sum_{p,q}A_{p,q}
 e\left(\frac{y\cdot k_{p,q}}{\sqrt N}
       +R_j\rho_{p,q}+\frac{u\rho_{p,q}}{\sqrt N}\right).
\]

Termwise integration is justified by finiteness of the sum and integrability of the weights. The spatial integral is

\[
 \int W(y)\phi(y/N)^{10}e(y\cdot k/\sqrt N)\,dy
 =K_N(-k/\sqrt N).
\]

It is **not** a spatial delta condition. Since `W` has fixed spatial scale, it is also not simply an `N^2`-scaled cutoff transform. Its exact alternative expression is

\[
 K_N(\xi)=\int\widehat W(\xi-v)\,N^2\widehat{\phi^{10}}(Nv)\,dv.
\]

The radial integral, after `u=Nv`, is

\[
 \int\eta(u/N)^{10}e(u\rho/\sqrt N)\,du
 =N H(-\sqrt N\rho).
\]

Hence the exact expansion is

\[
 \boxed{\mathcal C
 =N\sum_{p,q}A_{p,q}K_N(-k_{p,q}/\sqrt N)
 H(-\sqrt N\rho_{p,q})e(aT\rho_{p,q})
 D_J(\sqrt N\rho_{p,q}).}
\]

The sum is real and nonnegative because it equals the defining integral; individual summands need not be real or nonnegative. If `supp eta_hat subset [-b,b]`, then `supp H subset [-10b,10b]`, but no support truncation is required for this identity. The geometric sum is exact, including at its zeros and peaks:

\[
 D_J(v)=e(Jv/2)\frac{\sin(\pi(J+1)v)}{\sin(\pi v)}\quad(v\notin\mathbb Z),
 \qquad D_J(v)=J+1\quad(v\in\mathbb Z).
\]

The triangle inequality yields `C <= U_2 <= U_1`.

### 3.2 One radial integral, retaining every Schwartz tail

For the `j`-th window use `R=R_j+u/sqrt(N)`. Then

\[
 du=\sqrt N\,dR,\qquad u/N=(R-R_j)/\sqrt N.
\]

Thus, with

\[
 B_N(R)=\int_{\mathbb R^2}W(y)
 \left|\phi(y/N)F(y/\sqrt N,R)\right|^{10}\,dy,
\]

one has the exact identity

\[
 \boxed{\mathcal C(T,N)=\sqrt N\int_{\mathbb R}
 \Theta_{T,N}(R)B_N(R)\,dR.}
\]

The radial integration is over all of `R`. In particular, neither a window nor their sum is replaced by an indicator of a central interval. The constant `sqrt(N)` is the Jacobian and cannot be omitted.

### 3.3 Eventual uniform positivity of the spatial Fourier factor

For the fixed `phi`, dominated convergence gives

\[
 \|G_N-W\|_{L^1}
 =\int W(y)|\phi(y/N)^{10}-1|\,dy\longrightarrow0.
\]

Indeed `phi` is bounded, and `W` is integrable. Consequently

\[
 \sup_{\xi\in\mathbb R^2}|K_N(\xi)-\widehat W(\xi)|
 \le\|G_N-W\|_1\longrightarrow0.
\]

A direct Gaussian-mixture calculation proves strict positivity of `W_hat`, without importing a theorem:

\[
 (1+|y|^2)^{-100}=
 \frac1{\Gamma(100)}\int_0^\infty t^{99}e^{-t}e^{-t|y|^2}\,dt,
\]
\[
 \widehat W(\xi)=\frac{C_W\pi}{\Gamma(100)}
 \int_0^\infty t^{98}e^{-t-\pi^2|\xi|^2/t}\,dt>0.
\]

The transform is continuous. Therefore

\[
 \mu_{20}:=\min_{|\xi|\le20}\widehat W(\xi)>0,
\]

and for `N>=N_0(phi,W)` one has

\[
 \operatorname{Re}K_N(\xi)\ge\mu_{20}/2,
 \qquad |K_N(\xi)|\ge\mu_{20}/2\quad(|\xi|\le20).
\]

This suffices for every fixed interior power scale. The constant can be extremely small; it remains independent of `T,N` after the threshold.

The stronger claim that every cutoff under the weaker neighborhood hypotheses has this positivity for **all finite N** does not follow. Here is an analytic counterexample to that stronger compact-domain assertion under those weaker hypotheses. Fix any `N_*>=1`. Choose a real, even, bandlimited Schwartz function `g` on `R^2`, with arbitrarily small compact Fourier support and `g(0)=1`. Put

\[
 \psi_L(z)=g(z-Le_1)+g(z+Le_1)-2g(Le_1)g(z),
 \qquad \xi_L=e_1/(2N_*L).
\]

Then `psi_L(0)=0`. By Schwartz decay, splitting the integral into neighborhoods of `+/- L e_1` and their complement proves

\[
 \int W(y)\psi_L(y/N_*)^{10}\cos(2\pi\xi_L\cdot y)\,dy
 \sim -2C_W N_*^2(N_*L)^{-200}\int g(z)^{10}\,dz<0.
\]

The phase tends to `-1` at each translated bump; all remaining terms are smaller than any prescribed inverse power of `L`. On the other hand the same Fourier integral with `g(y/N_*)^{10}` is positive for large `L`, because `xi_L -> 0`. As a function of `t`, the transform for `phi=g+t psi_L` is a real polynomial of degree ten with positive constant term and negative leading coefficient. It vanishes for some positive `t`. This `phi` remains real, even, Schwartz and bandlimited, satisfies `phi(0)=1`, and hence has a central neighborhood with a positive lower bound in modulus. This constructs a zero within `|xi|<=20` at the chosen finite `N_*`. It does not claim that this zero must belong to the discrete set of attainable tuple differences. It refutes only the stronger blanket positivity assertion on the whole compact frequency domain. There is no conflict with eventual positivity for each fixed `phi`.

### 3.4 Lower bound for the separate-window certificate

Since `eta(0)=1`,

\[
 H(0)=\int\eta(v)^{10}\,dv>0.
\]

Continuity gives fixed `h_0,c_H>0` such that `|H(v)|>=c_H` for `|v|<=h_0`. Partition the interval `[5 sqrt(N),10 sqrt(N)]` into at most `C N` intervals of length at most `h_0/sqrt(N)`. Let `B_l` be the total tuple weight `b_p` in the `l`-th bin. Weighted Cauchy--Schwarz gives

\[
 \sum_lB_l^2\ge\frac{(\sum_lB_l)^2}{\#\{l\}}
 \gtrsim \frac{S^{10}}N\gtrsim N^{3/2}.
\]

Every pair in one bin has `|sqrt(N) rho|<=h_0`, and every spatial difference lies in the compact domain of the preceding lemma. The summands of `U_1` are nonnegative, so retaining only these pairs is legitimate. Thus

\[
 U_1\gtrsim N(J+1)N^{3/2}.
\]

Since `J+1` is comparable to `T/sqrt(N)` for `1<=N<=T^2`,

\[
 \boxed{U_1\gtrsim T N^2.}
\]

### 3.5 Lower bound after exact summation of center phases

Choose a fixed positive `h` so small that

\[
 h\le h_0,\qquad (d+1)h\le1/12.
\]

If `|rho|<=h/T`, then `|sqrt(N) rho|<=h_0` and

\[
 |j\sqrt N\rho|\le(dT+\sqrt N)h/T\le(d+1)h\le1/12
\]

for every `0<=j<=J`. Consequently

\[
 |D_J(\sqrt N\rho)|\ge\operatorname{Re}D_J(\sqrt N\rho)
 \ge\cos(\pi/6)(J+1).
\]

Partition `[5 sqrt(N),10 sqrt(N)]` into at most `C T sqrt(N)` bins of length at most `h/T`. The same weighted Cauchy--Schwarz argument gives a same-bin pair mass at least

\[
 \frac{S^{10}}{C T\sqrt N}\gtrsim\frac{N^2}T.
\]

Retaining these pairs in the nonnegative certificate `U_2` gives

\[
 U_2\gtrsim N(J+1)\frac{N^2}T
 \gtrsim\boxed{N^{5/2}}.
\]

This proof does not replace the geometric sum by its maximum away from the specified narrow near-resonance region. It also does not model the tuple radii as independent random variables.

### 3.6 Comparison with the stated target power

For `N=T^alpha` the proven exponents are

\[
 U_1\gtrsim T^{1+2\alpha},\qquad
 U_2\gtrsim T^{5\alpha/2}.
\]

Write

\[
 \delta_2(\alpha)=\frac52\alpha-\frac{83}{65}
 =\frac52\left(\alpha-\frac{166}{325}\right)>0.
\]

For every fixed `0<epsilon<delta_2(alpha)`,

\[
 U_2/T^{83/65+\epsilon}\longrightarrow\infty.
\]

Likewise `U_1/T^(83/65+epsilon)` diverges whenever `epsilon < 1+2alpha-83/65`; the latter gap is already `242/325` at the lower endpoint. On a fixed closed interior subband, one may choose a common positive epsilon smaller than the minimum gap. At `alpha=166/325` the `U_2` power is exactly the target, so this argument claims no strict power obstruction there. The upper endpoint `242/325` is not needed for the certificate argument.

### 3.7 Fixed spatial bandwidth and the trace implication

Let `L_phi` bound the fixed Fourier support of `phi`. For each `R`, the spatial function

\[
 g_R(y)=\phi(y/N)F(y/\sqrt N,R)
\]

has Fourier support in the fixed ball `|xi|<=2+L_phi` for `N>=1`. Choose a fixed Schwartz function `q` with `q_hat=1` on that ball. Then `g_R=q*g_R`, and `g_R(0)=F(0,R)`. Weighted Holder gives

\[
 |F(0,R)|\le
 \left(\int W(y)|g_R(y)|^{10}\,dy\right)^{1/10}
 \left(\int|q(-y)|^{10/9}W(y)^{-1/9}\,dy\right)^{9/10}.
\]

The second factor is finite and independent of `R,T,N`. Raising to the tenth power proves

\[
 |F(0,R)|^{10}\le C_{\rm tr} B_N(R).
\]

Combining this with the exact full-tail identity yields unconditionally

\[
 \boxed{\int_{\mathbb R}\Theta_{T,N}(R)|F(0,R)|^{10}\,dR
 \le C_{\rm tr}N^{-1/2}\mathcal C(T,N).}
\]

Let `I_T=[T/sqrt(2),sqrt(3)T]`. If

\[
 \Theta_{T,N}(R)\ge\kappa>0\quad(R\in I_T)
\]

uniformly, then

\[
 \boxed{\int_{I_T}|F(0,R)|^{10}\,dR
 \le (C_{\rm tr}/\kappa)N^{-1/2}\mathcal C(T,N).}
\]

In particular, a hypothetical actual bound `C <= constant T^(83/65+epsilon)` would give the tenth-moment bound `constant T^(83/65+epsilon)N^(-1/2)` on this interval.

Coverage is immediate under the conductor's clarification. Write `|eta(t)|>=c_eta>0` for `|t|<=1`. The nearest grid center is at distance at most `sqrt(N)/2` for every `R in I_T`; the ceiling in `J` ensures endpoint coverage. Hence `Theta_(T,N)(R)>=c_eta^10` throughout `I_T`. This proves the displayed interval trace with `kappa=c_eta^10` for all `T,N` in the stated range. The clarification is used only here; no numerical specification of the Fourier support is needed for the coverage argument.

## 4. First doubtful or unproved step

No doubtful step is required for the exact identities, eventual spatial positivity, the two certificate lower bounds, or the interval trace under the conductor's clarified cutoff normalization.

The decisive open analytic step is an upper bound for the **actual signed sum**

\[
 N\sum_{p,q}A_{p,q}K_N(-k/\sqrt N)H(-\sqrt N\rho)
 e(aT\rho)D_J(\sqrt N\rho).
\]

The positive certificates proved here cannot supply the target power. No cancellation estimate for this signed expression has been established. No estimate for a physical circle discrepancy follows from this packet, which supplies no arithmetic reduction.

## 5. Required control tests and outcomes

All controls below are analytical, with zero numerical experiments.

- **Normalization and tails:** The substitutions `u=Nv` in the Fourier expansion and `u=sqrt(N)(R-R_j)` in the single-integral form respectively produce factors `N` and `sqrt(N)`. Every radial integral is over the full real line. Outcome: pass.
- **Diagonal and center check:** At `k=rho=0`, the kernel is `N K_N(0)H(0)` for one window and `N(J+1)K_N(0)H(0)` after summing centers; both transform values at zero are positive. Outcome: pass.
- **Spatial-domain check:** The annular support implies `|k|/sqrt(N)<=20` for every ordered pair of five-tuples. Positivity is proved eventually on this entire compact set, not only near zero. A finite-N counterexample prevents an unwarranted all-N strengthening. Outcome: pass with the stated eventual threshold.
- **Near-resonance scale check:** Certificate (i) uses radius bins of width `O(N^(-1/2))`; certificate (ii) uses the narrower width `O(T^(-1))`, which keeps all center phases in one short arc. These are different arguments. Outcome: pass.
- **Weighted mass check:** The bin estimates use `sum b_p=S^5` and Cauchy--Schwarz on the bin masses. They never replace a weighted count with a raw count or invoke independent radii. Outcome: pass.
- **Logical seam between upper certificate and actual moment:** The implication available is `C<=U_2`, not `C>=U_2`. Restricting to near-resonance pairs is valid in `U_2` because every summand is nonnegative; it is invalid as a lower-bound argument for `C`, whose discarded summands may cancel the retained terms. Even the abstract real summands `z_1=1`, `z_2=-1` have `sum |z_i|=2` and `|sum z_i|=0`. This last elementary control is an inference counterexample, not a claim to construct an admissible coefficient family with `C=0`. Outcome: the proposed inference from certificate lower bound to actual-moment lower bound is rejected.
- **Unsigned/adversarial control:** The certificate proofs survive arbitrary placement of the nonnegative mass in the allowed annulus and contain no character or arithmetic cancellation. They therefore cannot be presented as evidence for an arithmetic signed estimate. Outcome: pass as a certificate obstruction, no positive arithmetic theorem.
- **Trace and endpoint check:** The reproducing kernel has fixed spatial bandwidth; the weight in its Holder dual is integrable because the kernel is Schwartz. Uniform radial coverage uses the ceiling endpoint and the conductor's clarified lower bound on `[-1,1]`. Outcome: weighted and interval trace pass.
- **Endpoint power check:** At `alpha=166/325`, `N^(5/2)=T^(83/65)`; a strict power obstruction occurs only above that endpoint. Outcome: pass.

## 6. Dependencies and exact artifacts used

1. `protocol.md` — project research rules and seven-part output contract.
2. `rounds/codex-managed/gc-complete-localized-wave-moment/briefs/blind_spatial_kernel_statement.md` — the complete isolated mathematical packet.
3. The graph hash printed in that packet, used only as report metadata. The graph itself was not read.
4. Conductor clarification received during this task: "the fixed central cubes where phi and eta are bounded below include [-1,1]^2 and [-1,1], respectively. The construction permits a fixed dilation before choosing them." Used only for central-window coverage and the interval trace; the exact identities and certificate claims retain the weaker neighborhood hypotheses.
5. Elementary finite expansion, triangle inequality, weighted Cauchy--Schwarz, dominated convergence, the Gaussian Fourier integral, and weighted Holder.

No external literature, prior/current report, arithmetic origin, graph assertion, experiment, or unstated statistical hypothesis is used. This report is the only file written by this task.

## 7. Recommended scoped state effect

**Promote only as a candidate for the conductor's required reviews:** the exact full-tail identities; eventual spatial Fourier positivity for each fixed cutoff; `U_1 >= constant T N^2`; `U_2 >= constant N^(5/2)`; and the fixed-spatial-bandwidth weighted and interval trace implications. The interval trace records the explicit central-window normalization supplied by the conductor.

**Reject as a route:** estimating either specified positive certificate by `T^(83/65+epsilon)` with arbitrary epsilon throughout any fixed interior scale in the packet's band.

**Retain open / no change:** any target bound for the actual signed moment, any arithmetic circle reduction, and every circle-discrepancy obligation. In particular, the certificate no-go is not an actual-moment no-go. No authoritative state, validation matrix, synthesis, or proof draft was edited.

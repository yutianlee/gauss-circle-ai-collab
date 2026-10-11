# 1. Result

Round226, gc-full-goal-spectral-source-review; theta_wave_full_frontiers; NONBLIND source/application audit, 2026-09-28.

**Neither audited theorem improves a complete frontier.** Edwin–Lin's theorem applies literally to the square lattice and gives the classical physical exponent \(1/3\). Gan–He–Li–Wu's current theorem can be applied to an exact three-dimensional torus lift of the circle half-wave, but its space-time norm, uniformly rephased input norm, spatial trace and temporal evaluation give a weaker certificate than coefficient triangle.

A complete damped Poisson-kernel representation is derived below, with the actual mollifier, real projection and all lattice shells retained. Damping \(T^{-1}\) changes the wave by \(O(T^{-1/4+\epsilon})\). Its separately absolute kernel estimate costs \(T^{1/2+\epsilon}\); keeping the original coefficients gives the better \(T^{1/4+\epsilon}\) triangle. Neither is a lower bound for the actual integral. The inherited COMPLETE REAL bound \(T^{\beta+\epsilon}\), \(\beta=2\theta_{\rm LY}-1/2\), remains best here.

These are two bounded theorem audits and a self-contained representation/control, not an exhaustive literature exclusion. No new spectral estimate, quarter theorem, complete moment improvement or M1/M2/GAR promotion is claimed.

# 2. Exact statements and hypotheses

Put \(e(t)=\exp(2\pi it)\), \(T\ge2\), \(cT\le R\le CT\), and retain the accepted fixed radial nonnegative unit-mass mollifier \(\rho\). Its Fourier transform gives the real even Schwartz function \(\Psi(s)=\widehat\rho(se_1)\), which may change sign. The actual wave and bridge are
\[
 B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4),
 \qquad
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+O(T^{1/2+\epsilon}).
 \tag{1}
\]
Thus a complete exponent \(\gamma\ge0\) restores \(1/4+\gamma/2\). The benchmark
\[
 \theta_{\rm LY}=\frac{3292+25\sqrt{1717}}{13762},
 \qquad \beta=2\theta_{\rm LY}-\frac12
\]
is inherited for the complete REAL wave only.

**Audit A.** [Gan–He–Li–Wu, arXiv:2502.05973v2, Theorem1.3](https://arxiv.org/html/2502.05973v2#Thmtheorem1.3), specialized to a fixed compact three-dimensional Riemannian manifold: for \(p\ge10/3\), \(\sigma<1/p\), the solution of \(u_{tt}-\Delta_g u=0\) satisfies
\[
 \|u\|_{L^p(M\times[1,2])}
 \lesssim
 \|f_0\|_{L^p_{\,1-2/p-\sigma}(M)}
 +\|f_1\|_{L^p_{\,-2/p-\sigma}(M)}.
 \tag{2}
\]
The [current primary record](https://arxiv.org/abs/2502.05973) lists v2, 4 January2026, four authors and improved results. The theorem starts at spatial dimension three; its conjectural two-dimensional statement is not imported. Complex data follow by real/imaginary linearity. Constants depend on the fixed manifold and fixed \(p,\sigma\), not on the frequency.

**Audit B.** [Edwin–Lin, arXiv:2412.05485v1, Theorem1.1](https://arxiv.org/html/2412.05485v1#Thmtheorem1.1): a planar Fourier quasicrystal with
\[
 \sum_{\lambda\in\Lambda}\widehat f(\lambda)
 =\sum_{s\in S}c_s f(s),\qquad
 \#(\Lambda\cap B_r)+\sum_{s\in S\cap B_r}|c_s|=O(r^P)
\]
has
\[
 \#(\Lambda\cap B_r)=c_0\pi r^2+O(r^{\,1-1/(2P-1)}).
 \tag{3}
\]
Here \(f\) is Schwartz, the spectrum is discrete, and the ball is closed. The [current primary record](https://arxiv.org/abs/2412.05485) lists only v1, 7 December2024. No withdrawal appears in either inspected record.

The bounded screen also inspected the primary records of [Guth–Wang–Zhang1909.10693](https://arxiv.org/abs/1909.10693), [Huang–Zhang2109.13370](https://arxiv.org/abs/2109.13370), and [Waibel2012.04311](https://arxiv.org/abs/2012.04311). Their cone, perturbed-operator and cuspidal-theta descriptions supplied no directly uniform actual-circle theorem at screening stage; none is a third audited/imported theorem. The other source role's selected shifted-convolution papers were not audited here.

# 3. Derivation and complete cost ledger

**3.1 Exact coefficient match and legal use of (2).** Let \(\lambda=\sqrt N\), take one fixed smooth dyadic partition, and on \(\mathbb T^3\) define
\[
 F_{T,N}(x)=
 \sum_{m\in\mathbb Z^2\setminus\{0\}}
 |m|^{-3/2}\Psi(|m|/\sqrt T)\,
 v(|m|^2/N)e(m_1x_1+m_2x_2).
\]
It is independent of \(x_3\). Its half-wave
\[
 U_{T,N}(t,x)=
 \sum_{m\ne0}|m|^{-3/2}\Psi(|m|/\sqrt T)
 v(|m|^2/N)e(m\cdot x+t|m|)
 \tag{4}
\]
solves the source equation for the standard torus Laplacian. At \(x=0\), grouping \(|m|^2=n\) produces exactly \(r_2(n)\), and the prescribed real phase produces the corresponding shell of (1). This is a lattice vector with one coefficient per \(m\), not an arbitrary replacement of \(r_2(n)\).

Write \(E_J=(1+N/T)^{-J}\); fixed Schwartz seminorms and a suitable change of \(J\) give
\[
 \|F_{T,N}\|_2\ll_J \lambda^{-1/2}E_J.
 \tag{5}
\]
For every real translation \(t_0\), \(G=U_{T,N}(t_0,\cdot)\) has the same \(L^2\) norm. Two-dimensional Bernstein, valid because it is independent of \(x_3\), gives
\[
 \|G\|_p\ll \lambda^{1-2/p}\|G\|_2
 \ll_J \lambda^{1/2-2/p}E_J.
 \tag{6}
\]
The source's initial velocity is \(i\sqrt{-\Delta}G\); its lower Sobolev index therefore has the same total frequency cost as the displacement. Applying (2) with \(\sigma=1/p-\epsilon\) yields, uniformly on any translated bounded time interval,
\[
 \|U_{T,N}\|_{L^p_{t,x}}
 \ll \lambda^{\,1-3/p+\epsilon}\|G\|_p
 \ll_J \lambda^{\,3/2-5/p+\epsilon}E_J.
 \tag{7}
\]
Intervals of the form \([1,2]\) after reinitializing the data cover the desired translated intervals with fixed multiplicity. No long-time source constant is assumed.

Spatial evaluation costs \(\lambda^{2/p}\), again in the two active spatial variables. Temporal evaluation costs \(\lambda^{1/p}\): apply the one-dimensional Sobolev interpolation inequality to the space-traced function, using (7) also for \(\partial_tU\), whose initial data cost an additional \(\lambda\). On fixed enlarged intervals this gives
\[
 |U_{T,N}(R,0)|
 \ll_{p,\epsilon,J}
 \lambda^{3/2-2/p+\epsilon}E_J.
 \tag{8}
\]
At the best endpoint supplied by this closure, \(p=10/3\), this is
\[
 N^{9/20+\epsilon}E_J.
 \tag{9}
\]
The source is used within its legal dimension and data class. Inserting \(n=2\) directly into its theorem would be invalid; the legal lift does not solve the norm problem.

If only time integration is needed, omitting temporal evaluation gives
\[
 \int_{cT}^{CT}|U_{T,N}(t,0)|^p\,dt
 \ll T\,N^{3p/4-3/2+\epsilon}E_J^p.
 \tag{10}
\]
The factor \(T\) counts bounded time intervals; it is compulsory. At \(p=10/3\), the right side is \(T N^{1+\epsilon}E_J^p\). This is not a pointwise bound and does not supply an unbounded fixed-order moment family. Nor can an unshifted bump's favorable \(L^p\) norm be reused for every \(t_0\): the input has the actual phase \(e(t_0|m|)\). Equations (5)–(6) are the uniform norms established here.

Summing every dyadic shell in (9) gives a complete complex \(T^{9/20+\epsilon}\) estimate, weaker than coefficient triangle \(T^{1/4+\epsilon}\). These would restore physical powers \(19/40\) and \(3/8\), respectively. The source has no exceptional arithmetic spectrum to delete on this fixed flat torus. Its missing ingredient for our application is a stronger estimate for the actual rephased vector and fixed spatial trace, not an omitted prime, prime-power or two-adic case.

**3.2 Literal specialization of (3).** For \(\Lambda=S=\mathbb Z^2\), Poisson summation has \(c_s=1\), \(c_0=1\), and lattice disk counting gives growth \(P=2\). It cannot be replaced by a smaller growth exponent: the lattice has order \(r^2\) points. Formula (3) gives
\[
 P(X)\ll X^{1/3}
 \quad\hbox{for every real }X,
 \qquad B_T(R)\ll T^{1/6+\epsilon}
 \tag{11}
\]
by (1). This is a complete real result, including integer-radius-square crossings through the source's closed-ball convention. It is weaker than the accepted \(\theta_{\rm LY}<1/3\), equivalently \(\beta<1/6\). No complex or individual-block \(T^{1/6}\) conclusion follows from it. Averaged error or limiting-distribution statements in surrounding literature are not upgraded to uniform values or high moments.

**3.3 A complete theta/Poisson representation with the actual mollifier.** This calculation imports no third theorem. Define
\[
 h(u)=\int_{\mathbb R}\rho(u,y)\,dy.
\]
Then \(h\) is fixed, smooth, nonnegative, even, compactly supported, has integral one, and
\(\Psi(s)=\int h(u)e(-su)\,du\). For \(\Re z>0\), set
\[
 {\cal P}(z)=\sum_{m\in\mathbb Z^2}e^{-z|m|}
 =2\pi z\sum_{k\in\mathbb Z^2}
          (z^2+4\pi^2|k|^2)^{-3/2}.
 \tag{12}
\]
Each branch on the right is analytic in the right half-plane and positive when \(z>0\) is real. One direct proof begins with the real Gaussian identity
\[
 e^{-z r}=\frac{z}{2\sqrt\pi}
  \int_0^\infty t^{-3/2}e^{-z^2/(4t)}e^{-tr^2}\,dt
 \quad(z>0),
\]
takes its two-dimensional Fourier transform, and sums the positive Gaussian Poisson identity. The transform is
\(2\pi z(z^2+4\pi^2|\xi|^2)^{-3/2}\).
Both sides of (12) are normally convergent analytic functions on compact subsets of \(\Re z>0\); the dual tail is \(O_z(\sum|k|^{-3})\). Analytic continuation proves (12) there. This continuation does not assert that the displayed real-\(t\) Gaussian integral converges for a nearly imaginary \(z\).

For \(\delta>0\), put \(r_u=R-u/\sqrt T\) and \(z=s+\delta-2\pi i r_u\). The exact identity is
\[
 {\cal W}_{T,\delta}(R)=
 \frac1{\Gamma(3/2)}
 \int_{\mathbb R}h(u)\int_0^\infty s^{1/2}
       [{\cal P}(s+\delta-2\pi i r_u)-1]\,ds\,du
 =
 \sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
       e^{-\delta\sqrt n}e(R\sqrt n).
 \tag{13}
\]
Indeed
\(\int_0^\infty s^{1/2}e^{-s\sqrt n}\,ds
=\Gamma(3/2)n^{-3/4}\).
Absolute convergence for fixed \(\delta>0\) justifies the original-side interchanges. In the dual representation the subtraction of one and the full \(k\)-sum must be combined before the infinite \(s\)-integration.

Damping can be removed at a completely specified cost:
\[
 |{\cal W}_{T,0}-{\cal W}_{T,\delta}|
 \le \delta\sum_{n\ge1}r_2(n)n^{-1/4}
               |\Psi(\sqrt{n/T})|
 \ll_{\epsilon}\delta T^{3/4+\epsilon}.
 \tag{14}
\]
Hence \(\delta=T^{-1}\) gives an \(O(T^{-1/4+\epsilon})\) error in the real wave. This uses the actual Schwartz mask. Taking moduli before the \(u\)-integration erases that mask; the original-side absolute sum is then only \(O_\epsilon(\delta^{-1/2-\epsilon})\). At \(\delta=T^{-1}\) it is \(T^{1/2+\epsilon}\). This is an upper certificate price, not a lower bound or an optimal transform norm.

All tails can be priced without a contour claim. For \(S\ge1\),
\[
 \int_S^\infty s^{1/2}|{\cal P}(s+\delta-2\pi i r_u)-1|\,ds
 \ll S^{1/2}e^{-S},
 \tag{15}
\]
uniformly in \(u,R,\delta>0\), by the original lattice series. Thus \(S=C_A\log(2T)\) makes this \(O_A(T^{-A})\). For \(s\le S\), \(R\asymp T\), and a dual cutoff \(K\gg T+S\), the omitted \(|k|>K\) tail of (12), after \(s\)-integration, is
\[
 O(TS^{3/2}/K).
 \tag{16}
\]
Taking \(K=T^{A+2}\) with a fixed enlargement pays it to \(O_A(T^{-A})\); bounded \(T\) is paid directly. Thus every original or dual terminal shell is owned. No unbounded-\(s\) integral of the isolated constant \(-1\) is used.

For comparison, the elementary absolute price of the retained dual integral is explicit. On \(|k|\asymp T\), write \(m=|k|^2\), \(a=s+\delta\). For \(s\le S\ll T\),
\[
 |z^2+4\pi^2m|\asymp |m-r_u^2|+Ta,\qquad |z|\asymp T.
\]
Using \(r_2(m)\ll_\epsilon T^\epsilon\) on this annulus and summing over integer \(m\), uniformly through \(r_u^2\in\mathbb Z\),
\[
 \sum_{|k|\asymp T}
 \left|\frac{2\pi z}{(z^2+4\pi^2|k|^2)^{3/2}}\right|
 \ll_\epsilon T^\epsilon
   \{T^{-1/2}a^{-3/2}+T^{1/2}a^{-1/2}\}.
 \tag{17}
\]
The two terms retain the nearest integer and all the other integers. The regions \(|k|\ll T\) and \(|k|\gg T\), with fixed annular separation, cost \(O(1)\); overlapping fixed annuli cover the transition. Multiplication by \(s^{1/2}\) and integration give
\[
 \ll_\epsilon T^\epsilon
 \{T^{-1/2}\log(2+S/\delta)+T^{1/2}S+S^{3/2}\}
 \ll_\epsilon T^{1/2+\epsilon}
 \quad(\delta=T^{-1}).
 \tag{18}
\]
The isolated \(-1\) on the finite interval costs \(O(S^{3/2})\). Formula (18) is deliberately scoped to this absolute estimate; it supplies no signed cancellation and is not asserted optimal.

Theta modularity corresponds to the Gaussian Poisson step in (12). It matches the actual \(r_2\) multiplicities, including all even and odd lattice vectors, but does not estimate the real boundary integral. The branch locations \(\pm2\pi i|k|\), the actual \(u\)-average and the continuous subtraction remain together. There is no rational-time exception, omitted major arc or averaging-in-\(R\) premise in (13). Uniform approach to its imaginary boundary is exactly the remaining analytical problem. The angle-dependent GAR coefficient is not \(r_2\), so (12) cannot be assigned to GAR by deleting its angular mask.

**3.4 Complete tails, moments and physical comparison.** The original singleton costs \(O(1)\). With \(Z=T^{3/2}\), any fixed Schwartz order \(J\) gives
\[
 \sum_{n>Z}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll T^{3/8-J/4+\epsilon}.
 \tag{19}
\]
Choose \(J\) after any requested fixed error power. Smooth dyadic overlaps have bounded multiplicity; all remaining \(O(\log T)\) blocks are included. Fixed-order norm inequalities lose only logarithmic powers. The auxiliary damping multiplies, rather than replaces, the actual mask.

Accepted204 still provides the complete distribution
\[
 D(V)\ll T^\epsilon(V^{-2}+TV^{-136/13})
\]
and the complete fixed-\(p\) moments
\[
 M_p(B_T)\ll T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}.
 \tag{20}
\]
Both terms are retained. Neither source audit improves them. The fixed distinct-class twelfth target \(I_{12}(T,\lfloor T^{2/5}\rfloor)\ll T^{29/25+\epsilon}\) remains unproved and would yield only \(102/325\). An unbounded sequence of FIXED even orders with \(Q_p=\lfloor T^{1/p}\rfloor\), \(I_p\ll_{p,\epsilon}T^{5/4+\epsilon}\) is sufficient for quarter through the accepted class/head bridge. Equivalently, a complete same-order real-wave bound \(M_p\ll T^{5/4+\epsilon}\) would suffice. The physical moment restores
\[
 \int_{Y/2}^{3Y}|P(x)|^pdx
 \ll T^{1+p/2}M_p(B_T)+T^{2+p/2+\epsilon},\quad Y=T^2,
\]
and the accepted persistence argument gives
\(1/4+7/[8(p+1)]\to1/4\).
No constants uniform in \(p(T)\) are asserted.

The complete quantitative menu from this audit is therefore: source A plus its stated trace closure, complex \(T^{9/20+\epsilon}\); original triangle, complex \(T^{1/4+\epsilon}\); source B, real \(T^{1/6+\epsilon}\); inherited, real \(T^{\beta+\epsilon}\). Closed225 also supplies the stronger complex ceiling \(T^{13/56+\epsilon}\), restoring \(41/112\), which may cap these weaker complex prices but is still worse than the real benchmark and is not a new226 gain. The real inherited bound remains strongest. The auxiliary absolute dual estimate \(T^{1/2+\epsilon}\) is weaker still. None is an actual lower bound.

# 4. First doubtful or unproved step

For Audit A, the first missing strengthening is control of the actual long-time rephased input and its fixed spatial trace beyond (6)–(8). Space-time averaging is not fixed-radius evaluation. The displayed legal lift avoids a false dimensional application but supplies no useful restored exponent.

For Audit B, there is no failed applicability premise for the square lattice. Its specialized exponent is simply insufficient. Changing the coefficient-growth exponent or transferring an averaged conclusion to all radii is not justified.

For the theta representation, (12)–(16) are exact identities or paid truncations. The first unproved estimate is cancellation in the complete real integral in Section7, before separate shell/contour absolute values. The existence of that integral, modularity, a positive heat estimate or a contour norm alone does not establish it. In particular (18) does not refute such cancellation.

No source or calculation here controls the independent GAR angular mask, any isolated original M1/M2 profile, or the required unbounded fixed-order family. No smaller sector is substituted for the full objective.

# 5. Controls and complete-frontier inventory

All controls are analytical; zero experiments.

| Control | Outcome |
|---|---|
| Current primary versions | Exact v2 four-author local-smoothing statement and exact v1 quasicrystal statement checked; neither inspected record is withdrawn. |
| Actual coefficient and phase | The torus lift produces exactly \(r_2(n)\) and \(e(R\sqrt n)\). The Poisson representation retains the real projection, actual \(\Psi\), all lattice multiplicities and the singleton. |
| Dimension and data norms | Direct dimension-two import of Audit A rejected; legal dimension-three lift priced. The translated data norms are not replaced by initial bump norms. |
| Trace and averaging | Spatial \(\lambda^{2/p}\), temporal \(\lambda^{1/p}\), and long interval factor \(T\) in integrated norms are explicit. No almost-everywhere or random-radius conclusion is promoted. |
| Complex parameter | Right-half-plane branches, analytic continuation and damping removal proved. The positive-real Gaussian integral is not used directly at nearly imaginary parameters. |
| Resonances and tails | The nearest integer term in (17), all other shells, full \(u\)-support, large \(s\), dual and original tails remain. No exceptional denominator, prime-power or two-adic complement is discarded. |
| Actual versus certificate | Every weak price is an upper-bound certificate. There is no actual signed lower bound, all-method impossibility claim, or claimed optimal contour norm. |
| Fixed order | Moment constants may depend on fixed \(p\); no growing-order substitution. |
| Isolation | No current sibling, blind packet or conductor control was read. Self-contained identities remain candidate evidence requiring independent review. |

The fresh graph/draft comparison leaves the following COMPLETE owners unchanged:

| Owner | Literal target, full complement and restoration |
|---|---|
| M1 HARD | The actual \(\chi_4(n)\) cone \(4h<n<16h\), \(h\asymp L\), phase \(e(\sqrt{Xhn})\), at \(L^{3/2}X^\epsilon\), with signs/profiles/floors/stars. After paid low radicals and large multipliers, retain the entire \(s>L,\ 1\le t<\lceil\sqrt L\rceil\) complement, including small primitive lifts and the unowned near-resonant large lifts, \(t=1\) and \(t\ge2\). |
| M1 SMOOTH | Every physical \(B_1(D,L;X)\ll X^{1/4+\epsilon}\), independently of HARD. The first smooth profile is literally \(D=\lfloor\sqrt X\rfloor/2\), \(L\asymp X^{1/6}\). Its accepted \(X^{1/3}\) menu capacity leaves \(X^{1/12}\); it is not an actual lower bound. |
| M2 TOP | With \(|T_{\rm end,L}|^2\ll L E_L^{\rm top}\), retain \(E_L^{\rm top}=\widetilde E_{\rm owned,L}+2\Re C_{L,\rm tag}^{\rm comp}\). The full target is \(\Re C_{L,\rm tag}^{\rm comp}\ll L^2X^\epsilon\), one representative \(h<s\), every tag/discrepancy mode, collar, terminal member, exact centre and literal endpoint. It would give the hard cone at \(L^{3/2}\), not the smooth owners. |
| M2 BAL | All smooth \(1\le K/L\le16\), complete \(|\sum_G G{\mathscr P}_G|\ll L^{3/2}X^\epsilon\), both quarter shifts, characters and actual symbol. Critical double-far energy is only one child; noncritical scales and the exact-square boundary remain. |
| M2 UNBAL | Every actual \(\sum_{h\asymp L,k\asymp K}\chi_4(h)a(h,k)e(\sqrt{Xhk})\ll(LK)^{3/4}X^\epsilon\), with \(K=XL/D^2\), \(K/L>16\), both shifts, all long rows and endpoint/transform companions. Restoring \(X^{1/4}(LK)^{-3/4}\) gives the physical quarter target. Flat rows alone are insufficient. |
| Total-M1 GAR | Complete \(\Re\{e(1/8)\sum_{n\le16\sqrt X} C_X^*(n)n^{-3/4}e(\sqrt{Xn})\}\ll X^\epsilon\), with the exact angular divisor coefficient. Its physical multiplier is \(-4X^{1/4}/\pi\), with owned logarithmic transform and inactive errors. Accepted120 pays the nonlower complement. The LOWER owner is updated through159: common-profile Abel self-return, all \(D>1,L>1\), generic \(t=1\), every \(t\ge2\), and the separate cross owner remain. Parent122 wording is stale shorthand, not the latest analysis. Baseline GAR is \(X^{1/12+\epsilon}\), physical total M1 \(X^{1/3+\epsilon}\). GAR does not imply individual blocks and still needs all M2/endpoints. |
| Whole-wave/moment alternative | The complete real supremum in (1), or the sufficient unbounded fixed-even-order family described after (20), can bypass the individual M1/M2 route. Neither audited source proves it. The fixed twelfth milestone is not quarter. |

For GAR the actual coefficient remains
\[
 C_X^*(n)=\sum_{\substack{h\mid n\\q=n/h\ {\rm odd}}}
 \chi_4(q)\sum_j1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 [w_j(2h\sqrt{X/n})]^*,
 \quad
 D_j=2^{-j}\lfloor\sqrt X\rfloor,\quad
 H_j=\lfloor D_jX^{-1/4}\rfloor.
\]
There is no theorem in this audit replacing it by \(r_2\). Closed224's completed-amplifier self-return and closed225's full \(81/614>\beta\) factor menu remain scoped prior evidence; neither is reused as a new gain. The closed223 absolute-chirp obstruction is not extended to an actual signed Poisson integral.

# 6. Dependencies, exact artifacts and provenance

This selected-context source role retains prior rounds218–225 history, including authorship of the round223 geometric report and round225 norm report and subsequent nonclaimant reviews. It is not a fresh isolated agent. Only the current brief's listed local context and the primary literature identified above were used. No current sibling/blind report, unlisted current control, shared state edit or successor design was performed.

Exactly two theorem audits are imported as candidate application evidence: Audit A Theorem1.3 specialized to dimension three, and Audit B Theorem1.1. Other primary records are screens only. Equations (4)–(19), including the actual coefficient map and complex Poisson calculation, are derived here. No theorem from a search snippet, secondary summary or surrounding conjecture is granted. Analytical allocation is at least95 percent; mathematical experiments are zero.

| Local artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 3f136e86091b999d4abf7db0b2141f4bced2e80480ee90a360c319c48b6e0d92 |
| state/best_proof_draft.md | 65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00 |
| strategy/round226_full_goal_spectral_source_review.md | 61ac5c2a26bf87f25133d8858dd2b4a0c6e377df657ddaeaa57d422d41e287ad |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md | 09806113079e70cd5863c315a9595524eac4270de6afa1f0c2b97e02c7f674f8 |
| rounds/codex-managed/gc-full-goal-spectral-source-review/briefs/theta_wave_full_frontiers.md | 8501a6b161a351920b2b44e1a44ed87360a1f40707da756b3b7905103a1bb9bf |
| rounds/codex-managed/gc-full-goal-spectral-source-review/briefs/conductor_complete_spectral_interfaces.md | 8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5 |
| rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md | c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7 |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| rounds/codex-managed/gc-full-goal-signed-source-review/reports/multiplicative_wave_sources.md | db7d52b2ebd266a9e92ae347444f6b1c0dbd99258194df07404b39c16b21ed86 |
| rounds/codex-managed/gc-full-goal-signed-source-review/reports/geometric_complete_frontiers.md | d68dc0c22687522cb31d78bee822ae0916924f55740634d96956f92e7de92c0c |

The graph controls accepted mathematics. Candidate source applications and representations in this report do not change it.

# 7. Recommended state effect and one complete next inequality

**No change** to accepted exponents, moments or any M1/M2/GAR/endpoint owner. **Retain** the two source audits and the exactly scoped damping/trace costs as evidence. **Reject** free spatial-trace, long-time-input, averaged-to-uniform, coefficient-growth and angular-mask transfers.

If a theta/wave attempt is chosen by the conductor, use one COMPLETE real target, with the specific candidate mechanism being signed interaction of the dual wave-kernel boundary shells under the actual mollifier average and real projection. Set \(\delta=T^{-1}\), \(r_u=R-u/\sqrt T\), \(z=s+\delta-2\pi i r_u\). The target is
\[
 \boxed{\displaystyle
 \sup_{cT\le R\le CT}
 \left|
 \Re\left\{
 \frac{e^{-3\pi i/4}}{\Gamma(3/2)}
 \int_{\mathbb R}h(u)\int_0^\infty s^{1/2}
 \left[
 2\pi z\sum_{k\in\mathbb Z^2}
       (z^2+4\pi^2|k|^2)^{-3/2}-1
 \right]ds\,du
 \right\}\right|
 \ll_\epsilon T^\epsilon .}
 \tag{21}
\]
The sum and subtraction are grouped as in (12)–(13). The same complete expression at \(T^{\gamma+\epsilon}\), \(0\le\gamma<\beta\), would be a genuine intermediate gain; the frozen full goal is \(\gamma=0\). Equations (14)–(16) pay damping, all dual shells and the integral tail. Equation (1) then restores the full physical quarter estimate, without relying on unproved M1/M2 pieces.

The arithmetic feature retained is the exact multiplicity of the square-lattice radii on both sides of the wave boundary, together with their prescribed complex branches and the final real phase. It is lost in (17)–(18). The proposed point of attack is cancellation in that complete joint integral, not another modular inversion, positive heat norm, separate resonant-shell bound or local exceptional-set estimate.

This is a fully quantified candidate inequality and an identified signed interaction to test, **not an established new cancellation mechanism or analytical progress**. It is equivalent at the required strength to the complete actual wave up to the paid error. If no estimate beyond the identities and separately absolute closure is obtained, the correct stopping point is this first unproved inequality. The conductor selects the next objective only after round226 closure; this report starts no successor. Stop after final hash.

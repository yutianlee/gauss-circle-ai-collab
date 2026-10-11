# 1. Result

Campaign: `gc-complete-signed-shell-arithmetic`. Round: 206.
Task: `blind_odd_shell_bridge`. Role: independent statement-only analyst.
Generated: 2026-09-26 (workspace date). Graph hash: not supplied and not accessed.

The shell-to-additive bridge is valid, including the discrete mean, all tails, the origin convention, integer centers, and the prescribed variable width. Uniformly in the supplied middle range,

\[
 S_N(R)=R^{-1/2}Z_{N,T}(R^2)
       +O_\varepsilon(T^{-1/2+\varepsilon}N^{-1})+O_A(T^{-A}).       \tag{1.1}
\]

The actual coefficient sequence satisfies the immediate supremum estimate

\[
 |Z_{N,T}(R^2)|\ll_\varepsilon T^\varepsilon
       \min\{T^{2\theta},T/\sqrt N\},\qquad
 |S_N(R)|\ll_\varepsilon T^\varepsilon
       \min\{T^\beta,T^{1/2}/\sqrt N\}.                         \tag{1.2}
\]

In particular, the supplied circle bound yields the actual-r2 supremum
\(S_N\ll T^{\beta+\varepsilon}\); this is not an arbitrary-coefficient substitution.

For the unweighted full middle sum

\[
 F_T(R)=\sum_{\substack{N\ {\rm dyadic}\\T^{52/125}<N<T^{99/125}}}S_N(R),
 \qquad I_T=[T/\sqrt2,\sqrt3T],
\]

the prospective sixth-moment estimate in the statement packet would imply

\[
 \int_{I_T}|F_T(R)|^{12}\,dR
 \ll_\varepsilon T^{47/125+6\beta+\varepsilon}
 \ll_\varepsilon T^{29/25+\varepsilon}.                         \tag{1.3}
\]

The exact exponent margin is

\[
 \delta=\frac{98}{125}-6\beta>0.                               \tag{1.4}
\]

The packet does not separately define the measure or weights of a different quantity called the full middle sum. Equation (1.3) specifies the precise convention proved here. It also holds with uniformly bounded, possibly R-dependent, coefficients multiplying the summands. Additional polynomial weights would require their explicit exponent accounting.

No sixth-moment theorem for actual r2 is proved. A positive surrogate control below proves that the given global discrepancy bound, bounded coefficients, and positivity alone cannot supply that missing theorem.

# 2. Exact statements and hypotheses

Use exactly the supplied data: \(T\ge2\), \(X=T^2\), \(R\in I_T\), dyadic \(N\) in the strict middle range, fixed real even Schwartz \(\Psi\), and fixed real smooth \(v\) supported in \([1,4]\). Write

\[
 L(u)=\ell_{N,T}(u),\qquad x=R^2,\qquad
 h=h_N(x)=\frac{2\sqrt x}{\sqrt N}=\frac{2R}{\sqrt N}.
\]

Constants may depend on \(\Psi,v\), a Schwartz seminorm order, or the indicated epsilon, but are uniform in \(T,N,R\). No nonvanishing hypothesis on the filter is needed for (1.1)--(1.3).

The only arithmetic inputs to the bridge and supremum proof are the supplied actual-r2 bounds and the supplied inclusive discrepancy formula:

\[
 r_2(m)\ll_\varepsilon m^\varepsilon,\qquad
 P(y)=1+\sum_{1\le m\le y}r_2(m)-\pi y
      \ll_\varepsilon y^{\theta+\varepsilon}\quad(y\ge2).
\]

For \(0\le y<2\), use that same defining formula, so \(P(0)=1\). In particular, no unannounced half-weight is placed at integer radii or at the origin.

The prospective arithmetic hypothesis, used only conditionally, is

\[
 \mathcal H_6:\qquad
 \int_{X/2}^{3X}|Z_{N,T}(x)|^6\,dx
 \ll_\varepsilon X^{1+\varepsilon}(T/\sqrt N)^3,                \tag{2.1}
\]

uniformly for every middle dyadic N and for the exact width \(h_N(x)\). As usual, epsilon can be relabeled after fixed multiples occur.

The exact parameters used in the ledger are

\[
 \beta=2\theta-\frac12
       =\frac{50\sqrt{1717}-297}{13762},\qquad
 a=\frac{52}{125},\quad b=\frac{99}{125}.
\]

# 3. Proof and exponent ledger

**Uniform filter facts.** Put \(q=\sqrt{N/T}<1\) and
\(a_q(t)=t^{-1}\Psi(qt)v(t^2)\). This is a smooth function supported in \([1,2]\), with all derivatives bounded uniformly for \(0<q<1\). Extending it by zero is smooth at the endpoints. Repeated integration by parts gives, for all nonnegative integers j and B,

\[
 |L^{(j)}(u)|\le C_{j,B}(1+|u|)^{-B}.                          \tag{3.1}
\]

With Fourier convention \(\widehat f(\xi)=\int f(u)e^{-2\pi i u\xi}\,du\),

\[
 \widehat L(\xi)=\begin{cases}
 a_q(\xi)/(2i),&1\le\xi\le2,\\
 -a_q(-\xi)/(2i),&-2\le\xi\le-1,\\
 0,&\text{otherwise}.
 \end{cases}                                                   \tag{3.2}
\]

Consequently L is real and odd, \(L(0)=0\), and every polynomial moment of L vanishes. In particular \(\int_{\mathbb R}L=0\).

Throughout the range,

\[
 h>\sqrt2\,T^{151/250}>2,\qquad
 \frac{x}{h}=\frac{R\sqrt N}{2}\asymp T\sqrt N.
                                                                  \tag{3.3}
\]

The second strict inequality in (3.3) follows already from \(151/250>1/2\) and \(T\ge2\). Poisson summation therefore gives the exact identity

\[
 \sum_{m\in\mathbb Z}L((x-m)/h)
 =h\sum_{k\in\mathbb Z}e^{2\pi i kx}\widehat L(hk)=0.          \tag{3.4}
\]

This holds for every real x, including integer x. It uses h at that particular x; constancy of h as x varies is unnecessary.

For B>1 the lattice estimate

\[
 \sum_{m\in\mathbb Z}(1+|x-m|/h)^{-B}\ll_B h                 \tag{3.5}
\]

is uniform in x when h>2. Also

\[
 \sum_{m\le0}|L((x-m)/h)|
 \ll_B h(1+x/h)^{1-B}=O_A(T^{-A})                             \tag{3.6}
\]

for any prescribed A by choosing B sufficiently large. Thus (3.4) proves

\[
 \sum_{m\ge1}L((x-m)/h)=O_A(T^{-A}).                           \tag{3.7}
\]

This is a proved discrete mean removal, rather than an assumption that subtracting pi is harmless.

**All shell and additive tails.** Split the positive integers into
\(x/4\le m\le4x\) and its complement. For \(m<x/4\),
\(|\sqrt N(R-\sqrt m)|\ge R\sqrt N/2\). Summing the actual coefficient bound gives a low-m shell tail bounded by

\[
 C_{K,\varepsilon}T^{3/2+2\varepsilon}(T\sqrt N)^{-K}.
\]

For \(m>4x\), the shell argument has magnitude at least
\(\sqrt{Nm}/2\), and summing
\(m^{-1/4+\varepsilon}(\sqrt{Nm})^{-K}\) gives the same bound. This includes the complete infinite high-m tail. The argument applies also when the low-m interval contains no positive integer.

For the additive expression, the corresponding low and high tails, with either coefficient \(r_2(m)\) or \(r_2(m)-\pi\), are bounded by

\[
 C_{K,\varepsilon}T^{2+2\varepsilon}(T\sqrt N)^{-K}.
\]

Indeed, the low-m argument is at least a fixed multiple of x/h, and the high-m argument is at least a fixed multiple of m/h. Since \(N>T^{52/125}\), these expressions are \(O_A(T^{-A})\) after choosing K. The bridge never extends \(m^{-1/4}\) to m=0; the small-m region has been disposed of directly.

**Local linearization with summable error.** For \(x/4\le m\le4x\), set

\[
 z=\frac{x-m}{h},\qquad u=\sqrt N(R-\sqrt m).
\]

Then

\[
 u=\frac{2R}{R+\sqrt m}z,\qquad
 \frac23\le\frac{u}{z}\le\frac43\quad(z\ne0),\qquad
 |u-z|\ll\frac{z^2}{R\sqrt N}.                               \tag{3.8}
\]

The exact identity behind the last bound is
\(u-z=\sqrt N(R-\sqrt m)^2/(2R)\ge0\). The amplitude obeys

\[
 |m^{-1/4}-R^{-1/2}|
 \ll R^{-1/2}\frac{|z|}{R\sqrt N}.                           \tag{3.9}
\]

Every point between u and z has magnitude comparable to \(|z|\). Applying the mean value theorem with (3.1), (3.8), and (3.9) gives, with any desired final decay order B,

\[
 |m^{-1/4}L(u)-R^{-1/2}L(z)|
 \ll_B \frac{R^{-1/2}}{R\sqrt N}(1+|z|)^{-B}.                \tag{3.10}
\]

At z=0 both sides on the left vanish, so this also covers an exact integer x without division by zero. Multiply by actual \(r_2(m)\ll_\varepsilon T^{2\varepsilon}\) and use (3.5). The resulting local error is

\[
 \ll_\varepsilon T^{2\varepsilon}
       \frac{R^{-1/2}}{R\sqrt N}\,h
 \ll_\varepsilon T^{-1/2+2\varepsilon}N^{-1}.                 \tag{3.11}
\]

The tail bounds and (3.7) now prove (1.1), after relabeling epsilon.

**The inclusive circle bound and origin term.** Define
\(f_{x,h}(y)=L((x-y)/h)\). Stieltjes integration by parts using the right-continuous, inclusive P gives the exact identity

\[
 \begin{split}
 Z_{N,T}(x)
 ={}&-L(x/h)
   +\frac1h\int_0^\infty P(y)L'((x-y)/h)\,dy\\
   &+\pi\left\{\int_0^\infty f_{x,h}(y)\,dy
                 -\sum_{m\ge1}f_{x,h}(m)\right\}.             \tag{3.12}
 \end{split}
\]

In detail, on \((0,\infty)\),
\(dP=\sum_{m\ge1}r_2(m)\delta_m-\pi\,dy\), and the lower boundary is
\(-P(0)f_{x,h}(0)=-L(x/h)\). Equivalently, extending P by zero below zero inserts the atom \(\delta_0\); it leads to the same formula after removing that atom. The upper boundary vanishes by rapid decay.

The two terms in braces are separately tiny: (3.7) handles the sum, while

\[
 \int_0^\infty f_{x,h}(y)\,dy
 =h\int_{-\infty}^{x/h}L(u)\,du
 =-h\int_{x/h}^\infty L(u)\,du=O_A(T^{-A}).                   \tag{3.13}
\]

The origin term is tiny as well. No replacement of inclusive counts by midpoint counts occurs. For integer x, the central jump is multiplied by \(L(0)=0\).

In (3.12), h is a fixed parameter during integration in y. Its dependence on x creates no extra derivative term. The supplied bound and (3.1) imply

\[
 \frac1h\int_0^\infty |P(y)L'((x-y)/h)|\,dy
 \ll_\varepsilon x^{\theta+\varepsilon}.                     \tag{3.14}
\]

For example, split at \(y=4x\). On the first portion use \(P(y)\ll(1+x)^{\theta+\varepsilon}\) and the L1 norm of L'; on the second portion use \(|x-y|\gg y\), choose the decay order larger than \(1+\theta+\varepsilon\), and use \(h\ll x\). This also includes \(0\le y<2\), where the defining formula bounds P absolutely. Thus Z is \(O(T^{2\theta+\varepsilon})\).

Independently, the actual coefficient bound and (3.5), with the already controlled tails, give \(|Z|\ll_\varepsilon hT^\varepsilon\). Combining these estimates and (1.1) proves (1.2). The circle-bound-only output is \(T^{\beta+\varepsilon}\) for S; the elementary local coefficient estimate improves it when \(N>T^{1-2\beta}\).

**Sixth-to-twelfth conversion.** Under the prospective hypothesis (2.1), the main bridge term has exactly

\[
 \begin{split}
 \int_{I_T}|R^{-1/2}Z(R^2)|^6\,dR
 &=\frac12\int_{X/2}^{3X}x^{-2}|Z(x)|^6\,dx\\
 &\ll_\varepsilon T^{-4}T^{5+\varepsilon}N^{-3/2}
 =T^{1+\varepsilon}N^{-3/2}.                                 \tag{3.15}
 \end{split}
\]

The error from (1.1) contributes at most
\(O_\varepsilon(T^{-2+\varepsilon}N^{-6})\) to this sixth moment and is smaller. Hence

\[
 \int_{I_T}|S_N(R)|^{12}\,dR
 \le \|S_N\|_\infty^6\int_{I_T}|S_N|^6\,dR
 \ll_\varepsilon T^{1+6\beta+\varepsilon}N^{-3/2}.            \tag{3.16}
\]

The stronger immediate version is

\[
 \int_{I_T}|S_N|^{12}\,dR
 \ll_\varepsilon T^{1+\varepsilon}N^{-3/2}
       \min\{T^{6\beta},T^3N^{-3}\}.                         \tag{3.17}
\]

Minkowski's inequality followed by the geometric dyadic sum
\(\sum_{N>T^a}N^{-1/8}\ll T^{-a/8}\) proves

\[
 \int_{I_T}|F_T|^{12}\,dR
 \ll_\varepsilon T^{1+6\beta-(3/2)a+\varepsilon}
 =T^{47/125+6\beta+\varepsilon}.                             \tag{3.18}
\]

Thus even a logarithmic aggregation loss is unnecessary for a boundedly weighted dyadic sum. Using a cruder finite-sum inequality would merely introduce logarithms absorbed by epsilon.

To verify the positive slack without numerical evidence, use
\(\sqrt{1717}<83/2\), giving \(\beta<889/6881\). Therefore

\[
 \delta=\frac{98}{125}-6\beta
 >\frac{98}{125}-\frac{5334}{6881}
 =\frac{7588}{860125}>0.                                    \tag{3.19}
\]

The entire summed bridge error by itself has twelfth integral at most

\[
 O_\varepsilon(T^{-5-12a+\varepsilon})
 =O_\varepsilon(T^{-1249/125+\varepsilon}),                   \tag{3.20}
\]

so it is far below the desired target.

For a general lower exponent a in the circle-supremum regime, the exact sufficient threshold is

\[
 1+6\beta-\frac32a\le\frac{29}{25}
 \quad\Longleftrightarrow\quad
 a\ge4\beta-\frac8{75}.                                    \tag{3.21}
\]

This is the threshold for this stated interpolation argument, not a necessary condition for the actual arithmetic moment to hold. If \(\nu=\log_TN\), the improved envelope (3.17) has exponent

\[
 E(\nu)=1-\frac32\nu+6\min\{\beta,(1-\nu)/2\}
 =\begin{cases}
 1+6\beta-\frac32\nu,&\nu\le1-2\beta,\\
 4-\frac92\nu,&\nu\ge1-2\beta.
 \end{cases}                                                \tag{3.22}
\]

Both pieces decrease. In the present range the worst endpoint is a, so the upper cutoff introduces no worse exponent.

**Allowable losses.** A uniform extra factor \(T^\kappa\) on the right side of (2.1), and an extra factor \(T^\sigma\) in the supremum, still suffice provided

\[
 \kappa+6\sigma\le\delta.                                   \tag{3.23}
\]

Equality is compatible with the epsilon formulation. An extra \(X^\lambda\) instead consumes \(2\lambda\) of this margin; an extra \(T^\rho\) in the sixth norm consumes \(6\rho\). A factor \(h^\eta\), \(\eta\ge0\), in the sixth integral consumes at the worst endpoint \((99/125)\eta\), so it is allowed when \((99/125)\eta\le\delta\). If the sixth integral instead loses \(T^\kappa N^\lambda\), the exact circle-supremum criterion is

\[
 \kappa+\max_{a\le\nu\le b}(\lambda-3/2)\nu
 \le\frac4{25}-6\beta;                                    \tag{3.24}
\]

in particular, for \(\lambda<3/2\) it becomes
\(\kappa+a\lambda\le\delta\). For larger losses one can use the sharper pointwise envelope (3.22) instead, requiring
\(\max_{a\le\nu\le b}\{E(\nu)+\kappa+\lambda\nu\}\le29/25\).

**Required width range.** The prospective theorem must cover the prescribed variable-width filters with

\[
 \sqrt2\,T^{151/250}<h_N(x)<2\sqrt3\,T^{99/125},
 \quad X/2\le x\le3X,                                      \tag{3.25}
\]

or, equivalently, widths between constant multiples of
\(X^{151/500}\) and \(X^{99/250}\). It must use the exact smoothly varying
\(h_N(x)=2\sqrt{x}/\sqrt N\). Here \(h'_N(x)=h_N(x)/(2x)\), but slow variation by itself is not a proof that a constant-width sixth-moment theorem applies. A theorem only about each fixed h would need a separate transfer or maximal estimate. No such transfer is assumed in this report.

# 4. First doubtful or unproved step

There is no remaining unproved step in the bridge, the actual-r2 supremum, or the conditional moment conversion above. The first unproved arithmetic step is precisely (2.1) for actual r2, uniformly over (3.25) and for the variable-width family.

In particular, neither the supplied circle discrepancy bound, the divisor identity by itself without new analysis, positivity of representation numbers, low-order moment information, nor positive tuple counts have been shown to imply (2.1). The required signed sixth moment contains genuine signed six-factor correlation information. Expanding it and discarding signs can replace the target with a much larger quantity.

A second possible seam would arise if the intended full middle sum has polynomial weights or a different measure not specified in the isolated packet. Equations (1.3) and (3.15) state the exact sum and measure proved here so that this can be checked by the conductor without importing hidden context.

# 5. Required analytical controls and outcomes

**Bridge control: integer center, origin, and symmetric offsets.** At an integer center \(x=m_0\ge1\), both the original shell term and the additive term belonging to \(m_0\) vanish because \(L(0)=0\). There is no endpoint half-weight. The origin contribution is the explicit \(-L(x/h)\) in (3.12), and is small by a proved tail estimate, not by omission. Outcome: all these convention checks pass.

A further curvature control explains why the linearization must have an error. For bounded z, set \(q_0=R\sqrt N\) and \(m=x-hz\). Taylor expansion gives

\[
 \begin{split}
 m^{-1/4}L(\sqrt N(R-\sqrt m))
 =R^{-1/2}\left[L(z)
   +\frac{zL(z)+z^2L'(z)}{2q_0}
   +O(q_0^{-2})\right],                                    \tag{5.1}
 \end{split}
\]

with the remainder uniform on each fixed bounded z interval. Both
\(zL(z)\) and \(z^2L'(z)\) are even. Therefore equal test coefficients at symmetric offsets z and -z cancel in the linearized main term but generally add in the first curvature correction. The bridge is not an exact odd-pair cancellation. Formula (3.10) has the correct first-error scale and controls this correction. Outcome: a claim of an error-free bridge fails this analytical control; the proved bridge passes.

**Low-order control: rare coherent excursions.** On an interval of length comparable to T, let a signed test function equal A on one set of measure \(1/(2A^2)\), equal -A on a disjoint set of the same measure, and vanish elsewhere, where \(A=T^\beta\). Then

\[
 \int f=0,\quad \|f\|_\infty=A,\quad
 \int|f|^2=1,\quad \int|f|^6=A^4,\quad
 \int|f|^{12}=A^{10}=T^{10\beta}.                            \tag{5.2}
\]

Smooth bumps give the same exponents if smoothness is requested. Thus even mean zero, the actual-sized supremum, and a strong second-moment bound do not automatically improve the twelfth exponent \(10\beta\). The desired lower-end sixth integral from (3.15) is \(T^{47/125+\varepsilon}\), whereas this control has exponent \(4\beta>47/125\). Also \(10\beta>29/25\); these inequalities follow already from \(\sqrt{1717}>41\). Outcome: the low-order-to-sixth inference fails. This is a control of an inference, not a counterexample to actual r2.

**Positive coefficient and circle-bound control.** There is a stronger analytic surrogate demonstrating that positivity, bounded coefficients, and the global discrepancy bound jointly still do not imply (2.1).

For this control only, choose one allowed nonzero filter with \(\Psi(0)\ne0\) and a point \(\tau\in(1,2)\) where \(v(\tau^2)\ne0\). Then, for all sufficiently large T in the middle range, \(\widehat L\) has magnitude bounded below on a fixed small interval about tau. This follows directly from (3.2) and \(N/T\to0\) uniformly. Degenerate filters need no such obstruction and cause no difficulty for the bridge.

Put \(x_0=3X/2\), \(h_0=h_N(x_0)\),
\(A_0=\min\{h_0,X^\theta\}\), and choose a fixed sufficiently small positive c. Define the surrogate coefficients

\[
 b_m=\pi+\lambda\cos(2\pi\tau m/h_0)\,
                    \mathbf1_{[X,2X]}(m),\qquad
 \lambda=cA_0/h_0.                                         \tag{5.3}
\]

These are nonnegative and bounded independently of T. Their inclusive discrepancy
\(P_b(y)=1+\sum_{1\le m\le y}b_m-\pi y\) is O(1) before X. On and after the modified block, the geometric-sum bound gives

\[
 |P_b(y)|\ll1+\lambda h_0\ll1+A_0\ll y^\theta
 \quad(y\ge X).                                            \tag{5.4}
\]

Thus they satisfy the same kind of global discrepancy bound, with uniform constants, as well as the pointwise coefficient bound and positivity.

For x in a fixed sufficiently small interval J about \(x_0\) of length comparable to X, the tails from truncating the cosine to \([X,2X]\) are superpolynomially small. Poisson summation, with no nonzero alias because h(x) tends to infinity, gives

\[
 \begin{split}
 \sum_{m\ge1}(b_m-\pi)L((x-m)/h(x))
 =\lambda h(x)\operatorname{Re}\left[
    e^{2\pi i\tau x/h_0}
    \widehat L\bigl(\tau h(x)/h_0\bigr)\right]+O_A(T^{-A}).    \tag{5.5}
 \end{split}
\]

Choose J small enough that \(\tau h(x)/h_0\) remains in the interval on which \(\widehat L\) is bounded away from zero. Since L is real odd, its Fourier transform there is purely imaginary with a fixed sign. The main term in (5.5) is a sine wave with amplitude comparable to A0. The interval contains an increasing number of periods because \(X/h_0\to\infty\). Consequently

\[
 \int_J\left|\sum_{m\ge1}(b_m-\pi)L((x-m)/h(x))\right|^6dx
 \gg X A_0^6.                                               \tag{5.6}
\]

The ratio of this lower bound to \(Xh_0^3\) is

\[
 (A_0^2/h_0)^3
 =\min\{h_0,X^{2\theta}/h_0\}^{3}\longrightarrow\infty
                                                                  \tag{5.7}
\]

by a positive power throughout the middle range: \(h_0\) has T-exponent between \(151/250\) and \(99/125\), whereas \(X^{2\theta}=T^{4\theta}\) and \(4\theta>99/125\). Thus the proposed sixth estimate fails for these positive surrogates despite all the coarse bounds just listed.

Outcome: any derivation of (2.1) using only those coarse properties fails this control. These b_m are not actual representation numbers and do not satisfy the divisor-character identity. This is expressly not a counterexample to (2.1) for actual r2. It identifies the arithmetic information a successful proof must use beyond positivity and the global circle bound.

No numerical experiment, external source, or assertion by voting was used in any control.

# 6. Dependencies and exact artifacts used

Only these two supplied files were read:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-signed-shell-arithmetic/briefs/blind_odd_shell_statement.md`.

No graph, manifest, generated general brief, strategy, predecessor report, claimant report, sibling report, or web source was read. The graph hash was deliberately not retrieved because this was a statement-only isolated assignment.

Mathematical dependencies are precisely the definitions and two arithmetic estimates stated in section 2, together with elementary Fourier inversion/Poisson summation for Schwartz functions, Stieltjes integration by parts, Taylor's theorem, lattice tail summation, and Holder/Minkowski inequalities. The supplied divisor-character identity is not needed for the proved bridge and was not turned into an unproved sixth-moment claim.

The analysis was entirely algebraic and analytic. No numerical or symbolic-computation experiment was run. This report is the only task output written. No shared state, validation matrix, proof draft, synthesis, legacy file, or successor plan was changed.

# 7. Recommended state effect

**Promote after the required independent seam validation:** the uniform bridge (1.1), its origin and discrete-mean conventions, the actual-r2 supremum (1.2), and the explicitly conditional sixth-to-twelfth implication (1.3), with the exact width and loss ledger above.

**Retain as open:** the prospective signed sixth-moment estimate (2.1) for actual r2 and its variable-width uniformity. This report supplies no proof of it and does not close the final target.

**Reject:** an error-free shell linearization, an unproved fixed-width-to-variable-width transfer, or a derivation of the signed sixth moment from low-order/positive information and the supplied global discrepancy bound alone. The controls identify failures of those inferences; they do not reject an arithmetic sixth-moment theorem that uses further r2 structure.

These are recommendations to the conductor only. No authoritative state change is made by this report, and no successor round is designed.

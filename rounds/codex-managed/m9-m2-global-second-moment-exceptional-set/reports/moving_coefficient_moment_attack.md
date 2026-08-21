## 1. Result

The frozen theorem is true, with the exact two-sided coefficient

\[
 \beta_{h,H}=-\frac{\Phi(|h|/(H+1))\chi _4(|h|)}{\pi |h|}
 \mathbf 1_{2\nmid h}\mathbf 1_{0<|h|\leq H}.
\]

If \(I\) has length \(V\), \(\mathscr D_D\subset[c_0D,c_1D]\), and
\(|w_D(d)|\leq1\), then

\[
 \int_I\left|\sum_h\beta_{h,H}
        \sum_{d\in\mathscr D_D}w_D(d)e\!\left(\frac{ht}{4d}\right)
       \right|^2dt
 \ll_{c_0,c_1}(V+D^2)D.                                      \tag{1.1}
\]

There is also a no-power-loss transfer to the literal moving profiles in
Section 8.6D of state/best_proof_draft.md. More generally, for a fixed
compactly supported BV profile \(f\), a scale \(R(t)\asymp D\), and an
integer height \(H(t)\) whose maximum is \(O(H_{\min}+1)\),

\[
 \int_I\left|\sum_h\beta_{h,H(t)}
       \sum_{d\geq1}u_d f\!\left(\frac d{R(t)}\right)
             e\!\left(\frac{ht}{4d}\right)\right|^2dt
 \ll_f (1+\log(2D))^2(V+D^2)D,                                \tag{1.2}
\]

uniformly for fixed \(|u_d|\leq1\). No regularity of \(R(t)\) is needed.
Thus (1.2) includes \(H(t)=\lfloor Dt^{-1/4}\rfloor\), the actual
\(H_j(t)=\lfloor 2^{-j}\lfloor\sqrt t\rfloor t^{-1/4}\rfloor\), every
height floor, and the hard top
\(W(d/\lfloor\sqrt t\rfloor)\mathbf1_{d\leq\lfloor\sqrt t\rfloor}\).
The jump at the top is an atom of the BV profile; a fixed non-one-sided
equality-star value is the difference of two endpoint-prefix conventions
and also creates no power loss.

Consequently, for one actual moving block with \(D\leq C Y^{1/2}\),

\[
 \int_Y^{2Y}|S_D^{\rm mov}(t)|^2dt
 \ll YD\log^2(2Y),                                            \tag{1.3}
\]

and, for every \(\eta>0\),

\[
 \left|\left\{t\in[Y,2Y]:|S_D^{\rm mov}(t)|>
 Y^{1/4+\eta}\right\}\right|
 \ll D Y^{1/2-2\eta}\log^2(2Y).                              \tag{1.4}
\]

For the full geometric family of actual dyadic M2 blocks, both the union of
the blockwise exceptional sets and the exceptional set of their sum have
measure

\[
 \ll Y^{1-2\eta}\log^2(2Y)
 \ll_\varepsilon Y^{1-2\eta+\varepsilon}.                    \tag{1.5}
\]

There is an exact fixed-in-\(Y\) partition for which the same proof applies
simultaneously to M1 and M2. With \(P(t)=N(\sqrt t)-\pi t\), the accepted
H1--H3 reduction and R5-Full then give the unconditional real-variable
mean square

\[
 \boxed{\int_Y^{2Y}|P(t)|^2dt\ll_\varepsilon
 Y^{3/2+\varepsilon}}                                        \tag{1.6}
\]

and hence

\[
 \left|\{t\in[Y,2Y]:|P(t)|>Y^{1/4+\eta}\}\right|
 \ll_{\varepsilon,\eta}Y^{1-2\eta+\varepsilon}.               \tag{1.7}
\]

These estimates are sharp at the diagonal scale and are only density-one
theorems. They do not prove a pointwise M2 bound, a new pointwise
Gauss-circle exponent, or any Round-92 canonical-core estimate.

## 2. Exact statement and hypotheses

For the frozen statement, \(Y\geq2\) is inessential, \(I\subset\mathbb R\)
is any interval of length \(V\geq0\), \(1\leq H\leq D\), and
\(\mathscr D_D\subset[c_0D,c_1D]\cap\mathbb Z_{>0}\). The constants
\(0<c_0<c_1<\infty\) are fixed. Both signs \(0<|h|\leq H\) occur in the
sum, and \(\chi _4\), odd support, \(H+1\), and the actual function \(\Phi\)
remain in the displayed coefficient before any norm inequality is used.

For the moving theorem, let \(f:[0,\infty)\to\mathbb C\) be a fixed,
compactly supported BV function with a specified value at each jump. Let
\(R:I\to(0,\infty)\) be arbitrary subject to

\[
 c_RD\leq R(t)\leq C_RD,                                      \tag{2.1}
\]

and let \(H:I\to\mathbb Z_{\geq0}\) satisfy

\[
 H_+:=\max_IH(t)\leq C_H(H_-+1),\qquad
 H_-:=\min_IH(t),\qquad H_+\leq C D.                          \tag{2.2}
\]

Define \(\beta_{h,0}=0\), and use the exact displayed beta coefficient for
\(H\geq1\). Under (2.1)--(2.2), (1.2) holds with a constant depending only
on the fixed comparability constants, the support and BV norm of \(f\), and
the audited \(C^1\)-norm of \(\Phi\). Measurability is the only analytic
condition needed on \(R,H\).

The actual packet satisfies these hypotheses in either convention:

* for fixed \(D\), \(H(t)=\lfloor Dt^{-1/4}\rfloor\), and
  \(H(t)\geq r\) exactly when \(t\leq(D/r)^4\);
* for the explicit partition, put \(y(t)=\lfloor\sqrt t\rfloor\),
  \(R_j(t)=2^{-j}y(t)\), \(D_j=2^{-j}Y^{1/2}\), and
  \(H_j(t)=\lfloor R_j(t)t^{-1/4}\rfloor\). Then \(R_j(t)\asymp D_j\)
  on \([Y,2Y]\), and (2.2) follows even for blocks that cross \(H=0\).

For interior blocks take \(f=W\). For the hard top take the literal BV
representative

\[
 f_{\rm top}(x)=W(x)\mathbf1_{x\leq1}.                         \tag{2.3}
\]

Changing the value at \(x=1\) to a fixed star weight adds one singleton,
which is the difference of the closed and open endpoint prefixes. Thus all
denominator floors, the moving support \(d\leq y(t)\), and the sampled-BV
top profile are within the theorem, rather than being silently smoothed.

For \(O(\log Y)\) geometric scales \(D_j\), assume the BV and comparability
constants above are uniform and \(\sum_jD_j\ll Y^{1/2}\). These are exactly
the hypotheses used for (1.5). The inactive bottom remainder is not being
Fourier-expanded and is not part of this M2 moment statement.

For the full-\(P\) consequence, let \(\vartheta\) denote the fixed smooth
step called \(\eta\) in Section 8.6D, and put
\(W(x)=\vartheta(x)-\vartheta(2x)\). Set

\[
 D_j=2^{-j}\sqrt Y,\qquad
 J=\max\{j:D_j\geq(2Y)^{1/4}\},\qquad y(t)=\lfloor\sqrt t\rfloor,
                                                                    \tag{2.4}
\]

and use

\[
 w_{j,t}(d)=W\!\left(\frac d{2D_j}\right)\mathbf1_{d\leq y(t)}
 \quad(0\leq j\leq J),\qquad
 w_{{\rm bot},t}(d)=
 \vartheta\!\left(\frac d{2D_{J+1}}\right)\mathbf1_{d\leq y(t)}.
                                                                    \tag{2.5}
\]

The main-block heights are \(H_j(t)=\lfloor D_jt^{-1/4}\rfloor\).
All weights in (2.5), including \(j=0\), are literal ordered prefixes of a
fixed shell profile. The bottom weight is kept outside the Fourier
expansion.

## 3. Proof or derivation

**Continuous separated-frequency inequality.** Suppose the distinct real
numbers \(\lambda_\nu\) are \(\delta\)-separated and
\(F(t)=\sum_\nu c_\nu e(\lambda_\nu t)\). Put

\[
 K_\delta(u)=\left(\frac{\sin\pi\delta u}{\pi u}\right)^2,
 \qquad \widehat K_\delta(\xi)=(\delta-|\xi|)_+.
\]

For every centre \(x\), separation gives the exact identity

\[
 \int_{\mathbb R}K_\delta(t-x)|F(t)|^2dt
 =\delta\sum_\nu|c_\nu|^2.                                    \tag{3.1}
\]

Indeed, every off-diagonal Fourier coefficient of \(K_\delta\) vanishes.
On \(|u|\leq(2\delta)^{-1}\), the elementary inequality
\(\sin z\geq2z/\pi\), \(0\leq z\leq\pi/2\), gives
\(K_\delta(u)\geq4\delta^2/\pi^2\). Covering an interval of length \(V\)
by at most \(1+V\delta\) such intervals and applying (3.1) proves

\[
 \int_I|F(t)|^2dt
 \leq\frac{\pi^2}{4}(V+\delta^{-1})\sum_\nu|c_\nu|^2.          \tag{3.2}
\]

This proves the required continuous large sieve internally, with the
\(e(x)=e^{2\pi ix}\) normalization fixed.

**Frozen reduced fractions.** Reduce \(h/d=a/b\), with \(b>0\),
\((|a|,b)=1\), and \(a\neq0\). Equal frequencies are grouped before (3.2):

\[
 A_{a,b}=\sum_{\substack{k\geq1:\;kb\in\mathscr D_D\\
                         0<|ka|\leq H}}
          \beta_{ka,H}w_D(kb),
 \qquad
 S(t)=\sum_{a,b}A_{a,b}e\!\left(\frac{at}{4b}\right).         \tag{3.3}
\]

The exact \(\chi _4\) factor and both signs are still present in (3.3).
Only now use \(|\beta_{ka,H}|\leq(\pi k|a|)^{-1}\). Since
\(kb\in[c_0D,c_1D]\),

\[
 |A_{a,b}|\leq\frac{C(c_0,c_1)}{|a|},
 \qquad
 \sum_{a,b}|A_{a,b}|^2
 \leq C(c_0,c_1)\sum_{b\leq c_1D}\sum_{a\neq0}\frac1{a^2}
 \ll D.                                                       \tag{3.4}
\]

Support edges cause no exception: if \(c_0D/b<1\), then
\(c_1D/b<c_1/c_0\), while otherwise the relevant harmonic sum is bounded by
\(1+\log(c_1/c_0)\). Distinct reduced frequencies obey

\[
 \left|\frac a{4b}-\frac {a'}{4b'}\right|
 \geq\frac1{4bb'}\geq\frac1{4c_1^2D^2}.                       \tag{3.5}
\]

Equations (3.2), (3.4), and (3.5) prove (1.1).

**The height-difference basis.** Extend \(\Phi\) to \([0,1]\). The audited
Vaaler theorem makes it \(C^1\) there and \(\Phi(1)=0\). Define

\[
 \gamma_{h,r}=\beta_{h,r}-\beta_{h,r-1}\qquad(r\geq1).         \tag{3.6}
\]

For \(0<|h|\leq r-1\), the mean-value theorem gives

\[
 |\gamma_{h,r}|
 \leq\frac{\|\Phi'\|_\infty}{\pi r(r+1)}.
\]

For \(|h|=r\), use
\(|\Phi(r/(r+1))|\leq\|\Phi'\|_\infty/(r+1)\). Hence, including
\(r=1\), parity, and both signs,

\[
 |\gamma_{h,r}|\ll r^{-2}\mathbf1_{0<|h|\leq r}
 \leq\frac{C}{r|h|}\mathbf1_{0<|h|\leq r}.                   \tag{3.7}
\]

This also certifies the sharper interval test suggested in the task. If
\(E\) is any denominator set of cardinality \(M\), group
\(\gamma_{h,r}u_d\mathbf1_{d\in E}\), \(|u_d|\leq1\), by \(h/d=a/b\).
A ray has at most \(r\)
lifts, so raywise Cauchy--Schwarz and (3.7) give

\[
 \sum_{a,b}\left|
   \sum_{\substack{k:\,kb\in E\\0<|ka|\leq r}}\gamma_{ka,r}u_{kb}
 \right|^2
 \leq r\sum_{d\in E}\sum_{0<|h|\leq r}|\gamma_{h,r}|^2
 \ll \frac{M}{r^2}.                                           \tag{3.7a}
\]

Thus a binary level of disjoint intervals has total gamma mass
\(O(N/r^2)\); neither rational multiplicity nor a short denominator
interval creates an unrecorded endpoint term.

The exact identity is

\[
 \beta_{h,H(t)}=\sum_{r\geq1}\gamma_{h,r}
                         \mathbf1_{H(t)\geq r}.                \tag{3.8}
\]

For fixed \(D\), the indicator in (3.8) is exactly
\(\mathbf1_{t\leq(D/r)^4}\), including equality. On a dyadic \(t\)-window,
one can do better than summing (3.8) from zero: take
\(q^{(0)}_h=\beta_{h,H_-}\), and for \(H_-<r\leq H_+\) take
\(q^{(r)}_h=\gamma_{h,r}\). Then

\[
 |q^{(0)}_h|\leq\frac{C}{|h|},\qquad
 |q^{(r)}_h|\leq\frac{C/r}{|h|},\qquad
 1+\sum_{r=H_-+1}^{H_+}\frac1r\ll_{C_H}1.                    \tag{3.9}
\]

If \(H_-=0\), condition (2.2) says \(H_+=O(1)\), so (3.9) is still valid.
This is the bounded-basis repair of the naive floor partition.

**Ray energy for disjoint denominator pieces.** The following estimate is
the multiplicity control needed for a moving top. Let
\(q_h=0\) off a finite two-sided support and \(|q_h|\leq c/|h|\). Let
\(E_\nu\subset\{1,\ldots,N\}\) be pairwise disjoint, and let
\(|u_d|\leq1\). After reducing fractions, put

\[
 B^{(\nu)}_{a,b}=\sum_{k:\,kb\in E_\nu}q_{ka}u_{kb}.
\]

With \(L_b=1+\log(N/b)\), weighted Cauchy--Schwarz gives

\[
 |B^{(\nu)}_{a,b}|^2
 \leq L_b\sum_{k:\,kb\in E_\nu}k|q_{ka}|^2.
\]

Summing first over the disjoint \(E_\nu\), then over signed \(a\) and
\(b\leq N\), yields

\[
 \begin{aligned}
 \sum_{\nu,a,b}|B^{(\nu)}_{a,b}|^2
 &\leq c^2\sum_{b\leq N}L_b^2\sum_{a\neq0}\frac1{a^2}\\
 &\ll c^2N,                                                    \tag{3.10}
 \end{aligned}
\]

because \(\sum_{b\leq N}(1+\log(N/b))^2\ll N\). Thus all perfect-rational
multiplicities have been charged exactly along their common \(k\)-ray; no
pair \((h,d)\) is falsely treated as a distinct frequency.

**Binary-prefix maximal large sieve.** Write

\[
 F_n(t)=\sum_hq_h\sum_{1\leq d\leq n}u_de\!\left(\frac{ht}{4d}\right),
 \qquad 0\leq n\leq N.
\]

Every prefix is the disjoint union of at most
\(L=\lceil\log_2(2N)\rceil\) canonical binary intervals. Cauchy--Schwarz,
followed by a sum over all binary intervals at all levels, (3.2), and
(3.10), gives

\[
 \int_I\max_{0\leq n\leq N}|F_n(t)|^2dt
 \ll L^2(V+N^2)c^2N.                                         \tag{3.11}
\]

At each level the denominator intervals are disjoint, which is precisely
why (3.10), rather than a separate \(O(N)\) bound for every node, applies.

**BV profile and moving-top assembly.** A one-sided compactly supported BV
representative has a finite complex Stieltjes measure \(\mu_f\) such that

\[
 f(x)=\int\mathbf1_{x\leq s}\,d\mu_f(s),
 \qquad \|\mu_f\|_{\rm TV}\ll\|f\|_{\rm BV}.                 \tag{3.12}
\]

For a specified value different from the selected one-sided value at a jump,
separate the resulting point mass. Its singleton indicator is the difference
of a closed and an open half-line, so the same bound holds with at most two
prefixes and total coefficient bounded by the BV norm. Consequently, with
the chosen equality convention,

\[
 f\!\left(\frac d{R(t)}\right)
 =\int\mathbf1_{d\leq\lfloor sR(t)\rfloor}\,d\mu_f(s).       \tag{3.13}
\]

The integer in (3.13) may vary completely arbitrarily with \(t\); (3.11)
already takes the maximum over all prefixes. Insert (3.9) and (3.13) in the
moving sum, use Minkowski, discard the scalar indicators
\(\mathbf1_{H(t)\geq r}\) in absolute value, and apply (3.11) to each basis
vector. Since the support of \(f\) and (2.1) give \(N\ll D\),

\[
 \|S^{\rm mov}\|_{L^2(I)}
 \ll_f (1+\log(2D))\sqrt{(V+D^2)D}
 \left(1+\sum_{r=H_-+1}^{H_+}\frac1r\right).
\]

Equations (2.2) and (3.9) prove (1.2). The discontinuity in (2.3) and a
fixed endpoint star are respectively an atom and, if needed, the difference
of the two endpoint-prefix conventions. Thus there is no hidden smooth-top
assumption.

Finally, (1.3)--(1.4) follow from \(D^2\ll Y\) and Chebyshev. For geometric
\(D_j\), summing (1.4) uses \(\sum_jD_j\ll Y^{1/2}\). For the sum of all
blocks, Minkowski and \(\sum_j\sqrt{D_j}\ll Y^{1/4}\) give

\[
 \int_Y^{2Y}\left|\sum_jS_{D_j}^{\rm mov}(t)\right|^2dt
 \ll Y^{3/2}\log^2(2Y),
\]

and another application of Chebyshev proves the second assertion in (1.5).

**Fixed-in-\(Y\) partition and full discrepancy.** The partition (2.5)
telescopes without a moving profile calculation:

\[
 \begin{aligned}
 \sum_{j=0}^{J}W\!\left(\frac d{2D_j}\right)
 +\vartheta\!\left(\frac d{2D_{J+1}}\right)
 &=\vartheta\!\left(\frac d{2D_0}\right).
                                                               \tag{3.14}
 \end{aligned}
\]

For \(d\leq y(t)\), \(t\in[Y,2Y]\), one has
\(d/(2D_0)\leq1/\sqrt2<1\), so the right side of (3.14) is exactly \(1\).
Multiplication by \(\mathbf1_{d\leq y(t)}\) proves that (2.5) is an exact
partition of every integer \(1\leq d\leq\lfloor\sqrt t\rfloor\), with the
floor retained.

For every main \(j\), \(W(d/(2D_j))\) is a fixed bounded shell weight and
\(\mathbf1_{d\leq y(t)}\) is an ordered prefix. Therefore (3.11) and the
height basis prove (1.3) for the exact M2 coefficient. They also apply to
the exact M1 coefficient

\[
 \alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h}
\]

with fixed denominator weight
\(\chi_4(d)W(d/(2D_j))\): its height differences satisfy the same
\(O(r^{-2})\) estimate, both signs remain present, and its reduced
frequencies \(a/b\) have at least the separation used above. Hence the sum
of all M1 and M2 main blocks has

\[
 \left\|\sum_{j=0}^{J}
   \bigl(\mathcal M_{1,j}+\mathcal M_{2,j}\bigr)
 \right\|_{L^2[Y,2Y]}
 \ll \log(2Y)\sqrt Y\sum_{j=0}^{J}\sqrt{D_j}
 \ll Y^{3/4}\log(2Y).                                        \tag{3.15}
\]

The bottom in (2.5) is supported on
\(d\ll D_{J+1}\ll Y^{1/4}\), so the pre-Fourier bound
\(|\psi_F|\leq1/2\) assigns it pointwise cost \(O(Y^{1/4})\). For every main
shell, the accepted R5-Full product-count proof applies pointwise: the
weight is bounded, its denominators lie in a fixed shell, the height is
\(\asymp D_jt^{-1/4}\), and the only hard endpoint is the exact prefix
\(d\leq y(t)\). Thus the sum of all first and shifted residuals is
\(O_\varepsilon(Y^{1/4+\varepsilon})\) pointwise after the
\(O(\log Y)\) assembly. Combining this, (3.15), the bottom bound, and the
accepted exact H1--H3 identity proves (1.6). Chebyshev proves (1.7).

## 4. First doubtful or unproved step

There is no remaining transfer gap for the literal fixed-BV rescalings and
hard top specified in Section 8.6D: height floors are handled by (3.6)--(3.9),
and profile/support floors by (3.11)--(3.13). The first unproved step toward
the project target is instead **exceptional-set removal**. Nothing above
excludes a prescribed \(X_0\) from the exceptional set, and at \(\eta=0\)
the top-block estimate permits an exceptional set of full \(Y\)-scale.
Thus the result supplies neither the everywhere-local fourth moment nor the
large-value propagation required by M9-M2-fourth-moment-average-to-pointwise.
The full-\(P\) estimate (1.6) has exactly the same limitation: (1.7) is an
almost-everywhere real-variable theorem and does not improve the accepted
pointwise one-third exponent.

The fixed-BV hypothesis is a literal seam, not cosmetic regularity. If
arbitrary bounded \(t\)-dependent denominator amplitudes are allowed, take
\(H=1\), a full shell, and

\[
 w_t(d)=\cos\!\left(\frac{2\pi t}{4d}\right).
\]

Since \(\beta_{1,1}=\beta_{-1,1}=-1/(2\pi)\), the resulting two-sided sum
has a zero-frequency component of size \(\asymp D\). On sufficiently long
intervals its mean square is \(\gg VD^2\), contradicting (1.1) by a factor
\(D\). The actual scale-rescaled BV profile cannot perform this phase
demodulation and is covered by (3.12).

Nor does (1.2) estimate the Round-92 quantity
\(\sum|\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|\). That object is a
fixed-\(X\), transformed, joint density--discrepancy energy requiring the
relative gain \(\rho^{-1/2}\). The present proof uses a \(t\)-average and
ordinary rational separation before that transform. It gives no bound for
an individual strict-metric block, no \(\rho^{-1/2}\) gain, and no closure of
the outside M2 packets.

## 5. Required control tests and outcomes

| Control | Test | Outcome |
|---|---|---|
| Reduced fractions and equal-frequency multiplicity | Group \(h/d=a/b\) before applying separation; sum all lifts \(k\) in (3.3) and (3.10). | Pass. Multiplicity costs are exactly raywise and total coefficient mass is \(O(D)\). |
| Coefficient \(\ell^2\) mass | Check every \(b\)-edge and both signs in (3.4). | Pass. \(\sum|A_{a,b}|^2\ll D\), uniformly in \(H\leq D\). |
| Continuous large-sieve normalization | Prove (3.2) from the sinc-square kernel with \(e(x)=e^{2\pi ix}\). | Pass. Constant is \(\pi^2/4\), with cost \(V+\delta^{-1}\). |
| Exact \(\chi _4\) and two-sided support | Keep beta unchanged through (3.3), and define gamma from the exact beta. | Pass. The sign is never replaced by an unsigned coefficient; only norm bounds discard it after the exact expansion. |
| Diagonal sharpness | Take \(H=1\), \(w=1\), and a full shell. | Pass. The \(a=\pm1,b=d\) terms give \(\sum|A|^2\asymp D\), so the diagonal is \(\asymp VD\). As \(V\to\infty\), off-diagonal averages vanish. On an interval of length \(\asymp D\) near zero the frequencies cohere and the integral is \(\gg D^3\), also matching the \(D^2D\) term. |
| Moving height and small \(r\) | Compute gamma at interior \(h\), at \(|h|=r\), and at \(r=1\). | Pass. Equation (3.7) is uniform, including the top frequency and \(H=0\leftrightarrow1\). |
| Gamma interval mass | Group one denominator interval of cardinality \(M\) into exact rational rays. | Pass. Equation (3.7a) gives \(O(M/r^2)\), including all lift multiplicities. |
| Naive floor-interval loss | Apply (1.1) separately on the \(N_H\asymp DY^{-1/4}\) height intervals. | Fail as a method: it gives \(YD+N_HD^3\), which is \(Y^{7/4}\) at \(D=Y^{1/2}\), a \(Y^{1/4}\) loss. Freezing every top-support jump is worse: \(N_y\asymp Y^{1/2}\) gives \(Y^2\), a \(Y^{1/2}\) loss. |
| Bounded-basis repair | Telescope beta and use the disjoint-ray energy plus binary-prefix maximum. | Pass. Height variation costs no power, and prefix variation costs only \(\log^2D\) in the moment. |
| Moving hard top, floor, and equality star | Represent \(W(x)\mathbf1_{x\leq1}\) by (3.12), separating a non-one-sided star value as a singleton. | Pass. The top jump is an atom, a star is the difference of two endpoint prefixes, and \(d\leq\lfloor\sqrt t\rfloor\) is exact. |
| Single/all-block exceptional set | Apply Chebyshev to (1.3), sum \(D_j\), and separately test the sum using \(\sum\sqrt{D_j}\). | Pass. The bounds are (1.4)--(1.5), with no power loss. |
| Fixed-in-\(Y\) partition | Telescope (2.5) and test the endpoint \(d=\lfloor\sqrt t\rfloor\). | Pass. Equation (3.14) is identically \(1\) on the whole moving denominator range and retains the floor as one ordered prefix. |
| M1/full-\(P\) assembly | Repeat the height/ray argument for exact \(\alpha_{h,H}\), then keep bottom and R5 under their accepted owners. | Pass. The main moment is (3.15), the bottom is \(O(Y^{1/4})\), and R5 is \(O_\varepsilon(Y^{1/4+\varepsilon})\) pointwise, giving (1.6)--(1.7). |
| Pointwise implication | Set \(\eta=0\) at \(D\asymp Y^{1/2}\). | No implication. The measure bound is of full \(Y\)-scale. |
| Round-92 canonical-core scope | Compare the norm, variables, and required gain with the canonical \(\mathfrak Q\)-target. | No implication in either required direction. The present deliverable is an original-block global second moment. |

All tests above are analytic; no numerical experiment is used as evidence.

## 6. Dependencies and exact artifacts used

Campaign m9-m2-global-second-moment-exceptional-set, task
moving_coefficient_moment_attack, starting graph SHA-256
db11a048eaafe05832a8fe5d2a62af297967c2ca5c6721630256acb063fb7c47.

The exact permitted artifacts used were:

* protocol.md and state/active_campaign.yml for the frozen scope,
  report contract, controls, and no-overclaim rule;
* state/proof_obligations.yml for the statuses and statements of
  M9-M2, M9-M2-beta-algebra, M9-M2-character-factor, the average-to-
  pointwise and local-fourth-moment obligations, the canonical top energy,
  and endpoint uniformity;
* state/best_proof_draft.md for the literal M2 block, actual dyadic
  profiles, \(H_D\)-floor, hard top, H1--H3, R5-Full, bottom ownership, and
  accepted pointwise/canonical scope;
* rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/derivation_packet.md
  and candidates/conductor_frozen_second_moment.md for the candidate
  frozen theorem and requested transfer seam;
* sources/vaaler_1985.md for the audited exact beta algebra,
  \(\Phi\in C^1[0,1]\), \(\Phi(1)=0\), \(H+1\), odd support, and endpoint
  convention;
* rounds/codex-managed/m9-canonical-core-formalization/synthesis.md for
  the exact nonrelation to the Round-92 M2 core.

No sibling Round-93 report, unlisted strategy file, web source, or
computation was read or used.

## 7. Recommended state effect

**Promote** a new proved-internal lemma, provisionally
M9-M2-global-second-moment-moving-BV, with statements (1.1)--(1.5), and a
corollary recording the full-discrepancy mean square and exceptional set
(1.6)--(1.7). Its
dependencies are the audited H4/beta normalization and the already proved
H1--H3 and R5-Full reductions. The fixed-in-\(Y\) partition (2.4)--(2.5)
supplies the exact denominator assembly. Record that the literal moving
height, floor, top support, and fixed endpoint star transfer with only
logarithmic loss.

**Retain** M9-M2-beta-algebra as proved and add this report as evidence
that its exact \(\chi _4\) coefficient is preserved in a global second
moment. **Retain open**, without weakening, M9-M2-character-factor,
M9-M2-fourth-moment-average-to-pointwise,
M9-M2-local-fourth-moment-LFM,
M9-M2-top-endpoint-density-discrepancy-energy, M9-M2, and
M9-endpoint-uniformity.

**Reject** the shortcuts “freeze every height/top floor interval” and
“allow arbitrary bounded moving amplitudes”; their first exact losses are
recorded in Sections 4--5. **No change** is licensed for M9, the
pointwise conditional endpoint theorem, GC-target, or any pointwise
Gauss-circle exponent; (1.6)--(1.7) are explicitly mean-square and
almost-everywhere statements.

# Conductor candidate: target-scale profile flattening and integer-phase completion

Campaign: `m9-m1-global-lower-height-kernel-gate`

Status: corrected conductor proof, independently rederived and hostilely audited.

Put \(R=X^{1/4}\), \(Y=\sqrt X\), \(y=\lfloor Y\rfloor\),
\(D_j=2^{-j}y\), and \(H_j=\lfloor D_j/R\rfloor\). Let \(C_b\)
be a fixed constant for which the accepted inactive bottom profile is
supported in \(d\leq C_bR\). Choose the fixed lower cutoff used in the
physical radial partition so small that

\[
 {3\sqrt{2s_0}\over4}<\frac12,
 \qquad {2\over\sqrt{2s_0}}>C_b.
\tag{121.C0}
\]

The exact profile certificate permits such a fixed choice (and its sharper
bottom support makes \(s_0\leq1/100\) sufficient). Require

\[
 V_{\rm low}(s)=1\quad(s\leq s_0),\qquad
 V_{\rm low}(s)=0\quad(s\geq2s_0).
\tag{121.C1}
\]

The Round-120 nonlower theorem is valid for this choice. Define

\[
 \begin{aligned}
 \mathcal B_{\rm low}^+
 &=\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V_{\rm low}(4R^2h^2/d^2)e(hX/d),\\
 \mathcal B_{\rm flat}^+
 &=\sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
 \end{aligned}
\tag{121.C2}
\]

The candidate theorem is

\[
 \boxed{
 \mathcal B_{\rm low}^+=\mathcal B_{\rm flat}^+
 +O_{\varepsilon,s_0}(RX^\varepsilon).}
\tag{121.C3}
\]

Thus the floor-perturbed profile kernel is equivalent at the target scale
to a single sharp denominator cone. This is a reduction, not an estimate
of either main term.

## 1. Support geometry and exact main coefficient

On the support of \(V_{\rm low}(4R^2h^2/d^2)\),

\[
 {hR\over d}\leq{\sqrt{2s_0}\over2}.
\tag{121.C4}
\]

Every active profile has the certified closed support
\(1/2\leq d/D_j\leq3/2\). Hence

\[
 {hR\over D_j}\leq{3\sqrt{2s_0}\over4}<\frac12.
\tag{121.C5}
\]

If \(h\geq1\), (121.C5) implies \(D_j/R>2h\), so
\(h\leq H_j\). It also gives

\[
 {h\over H_j+1}<{hR\over D_j}<\frac12.
\tag{121.C6}
\]

Conversely, nonvanishing of the lower multiplier and \(h\geq1\) force
\(d>2R/\sqrt{2s_0}>C_bR\). Thus the inactive bottom profile is zero on
the joint support. The exact active partition therefore gives

\[
 \sum_j w_j(d)={\bf1}_{d\leq y}
\tag{121.C7}
\]

there, including the one-sided hard top sample. Replacing every
\(\Phi\) by one in (121.C2) consequently gives exactly
\(\mathcal B_{\rm flat}^+\), with no floor, profile, or endpoint loss.

## 2. Target-safe Vaaler-profile error

On \(0\leq u\leq1/2\), the accepted explicit Vaaler profile and its
derivative give

\[
 |\Phi(u)-1|\ll u^2,\qquad |\Phi'(u)|\ll u.
\tag{121.C8}
\]

For one profile and one dyadic height shell \(h\asymp L\leq cH_j\),
the error height weight has sampled sup plus variation

\[
 \ll {1\over L}\left({L\over H_j}\right)^2.
\tag{121.C9}
\]

Write \(u=h/L\), \(v=d/D_j\), and \(\lambda=RL/D_j\). On a fixed
rectangle supporting the height shell and denominator profile, a smooth
periodic extension of

\[
 Q_\lambda(u,v)=V_{\rm low}(4\lambda^2u^2/v^2)
\]

has uniformly bounded \(C^M\) norms for every fixed \(M\), uniformly in
the allowed \(\lambda\). Its two-dimensional Fourier coefficients
\(c_{r,s}(\lambda)\) therefore obey, after taking \(M\) sufficiently
large,

\[
 \sum_{r,s}|c_{r,s}(\lambda)|(1+|r|)(1+|s|)
 \ll_{s_0}1.
\tag{121.C9a}
\]

The \(r\)-weight prices sampled height variation; the \(s\)-weight prices
the modulated denominator BV, including the one hard truncation. Applying
the accepted frequency-first divisor theorem termwise gives

\[
 E_{j,L}\ll_{\varepsilon,s_0}X^\varepsilon
 \left({L\over H_j}\right)^2\left(1+{D_j\over L}\right).
\tag{121.C10}
\]

Whenever this shell is nonempty, \(H_j\geq1\) and
\(D_j/R<H_j+1\leq2H_j\). Therefore the right side of (121.C10) is

\[
 \ll X^\varepsilon\left\{\left({L\over H_j}\right)^2
 +2R{L\over H_j}\right\}.
\]

Dyadic summation over \(L\leq cH_j\), followed by the logarithmic profile
sum, is \(O_{\varepsilon,s_0}(RX^\varepsilon)\). This proves (121.C3),
including the hard sampled-BV endpoint.

## 3. Exact denominator pair and its safe amplitude seam

For the flat cone put

\[
 b(h,d)={\bf1}_{d\leq y}V_{\rm low}(4R^2h^2/d^2).
\]

Zero extension and \(\chi_4(4m+3)=-\chi_4(4m+1)\) give

\[
 \mathcal B_{\rm flat}^+
 =\sum_{d\equiv1\ (4)}\sum_h{1\over h}
 \{b(h,d)e(hX/d)-b(h,d+2)e(hX/(d+2))\}.
\tag{121.C11}
\]

Adding and subtracting \(b(h,d+2)e(hX/d)\) splits (121.C11) into an
amplitude seam and the phase-increment kernel. For fixed \(h\), the
total discrete variation in \(d\) of \(b(h,d)\) is \(O_{s_0}(1)\),
including the hard jump. Summing \(1/h\) over the possible
\(h\ll d/R\leq R\) shows that the amplitude seam is
\(O_{s_0}(\log(2X))\). For the unflattened profile kernel the same
argument profile by profile is \(O_{s_0}(\log^2(2X))\). The exact hard
survivor is therefore

\[
 \mathcal K_X=
 \sum_{d\equiv1\ (4)}\sum_h{b(h,d+2)\over h}e(hX/d)
 \left\{1-e\!\left(-{2hX\over d(d+2)}\right)\right\}.
\tag{121.C12}
\]

No termwise absolute-value estimate of (121.C12) is claimed.

## 4. Target-safe integerization of the phase

Let \(N=\lfloor X\rfloor\). Since \(|X-N|<1\),

\[
 |e(hX/d)-e(hN/d)|\ll h/d.
\]

After the factor \(1/h\), there are only
\(O_{s_0}(d/R)\) supported heights for a fixed \(d\). Hence

\[
 \boxed{
 \mathcal B_{\rm flat}^+(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O_{s_0}(R),}
\tag{121.C13}
\]

where only the phase is changed:

\[
 \mathcal B_{\rm flat}^{(N)}(X)=
 \sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hN/d).
\tag{121.C14}
\]

Thus real-\(X\) uniformity itself is not the remaining obstruction.

## 5. Exact finite Fourier completion

Choose once and for all a smooth function \(\eta\) with \(\eta(u)=0\) for
\(u\leq1/2\) and \(\eta(u)=1\) for \(u\geq1\). On the small positive
arc set

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t},
\tag{121.C15}
\]

and extend it smoothly by zero and periodically. Then \(J_{R,y}(0)=0\),
and at every supported sample \(t=h/d\) with \(1\leq d\leq y\),
\(h\geq1\), one has \(t\geq1/y\), so (121.C15) equals the required
sample value. Let

\[
 \widehat J_{R,y}(k)=\int_0^1J_{R,y}(t)e(-kt)\,dt,
 \qquad
 A_y(m)=\sum_{\substack{d\mid m\\d\leq y}}\chi_4(d)
 \qquad(m\in\mathbb Z),
\tag{121.C16}
\]

where every positive \(d\) is understood to divide \(0\).

Since the lower support has \(h<d\), discrete Fourier completion modulo
\(d\) gives the exact identity

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}\widehat J_{R,y}(k)A_y(N+k).}
\tag{121.C17}
\]

Indeed

\[
 {\chi_4(d)\over d}\sum_{h\bmod d}J_{R,y}(h/d)e(Nh/d)
 =\chi_4(d)\sum_{k:\ d\mid N+k}\widehat J_{R,y}(k),
\]

and summing \(d\leq y\) proves (121.C17). All interchanges are absolute
because \(J_{R,y}\) is smooth for fixed \(X\).

## 6. Exact discrepancy survivor

Put

\[
 c_y=\sum_{d\leq y}{\chi_4(d)\over d}.
\]

Since \(J_{R,y}\) vanishes near zero, Poisson evaluation gives
\(\sum_k\widehat J_{R,y}(k)=J_{R,y}(0)=0\). Hence

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_k\widehat J_{R,y}(k)\{A_y(N+k)-c_y\}.
\tag{121.C18}
\]

Define the two-sided affine discrepancy by \(D_N(0)=0\) and

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y.
\tag{121.C19}
\]

For every \(k\in\mathbb Z\), this discrepancy has the literal crossing
formula

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left\{\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right\}.
\tag{121.C19a}
\]

Indeed its first difference is \(A_y(N+k)-c_y\) for every integer \(k\),
including negative values and intervals crossing zero. Thus the survivor
is a prescribed-centre, sharp-denominator, period-four signed crossing
discrepancy, not an arbitrary divisor coefficient.

Schwartz summation by parts gives

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_kD_N(k)\{\widehat J_{R,y}(k)-
 \widehat J_{R,y}(k+1)\}.}
\tag{121.C20}
\]

This is a sharp-cutoff global version of the accepted product-wavelet
local-discrepancy return. Period-four pairing cancels only matched
crossings in \(D_N\); the signed symmetric difference remains. The raw
seminorms of \(J_{R,y}\) grow with \(y\), so fixed-\(X\) Schwartz decay
does not itself give a uniform estimate. Equations (121.C17)--(121.C20)
therefore do not prove the target. They identify the smallest survivor
within this exact reduction chain as the actual truncated
character-divisor discrepancy against the full lower-radial wavelet.

## 7. Proposed state effect and scope

If the seams above pass review, promote only:

1. target-scale flattening (121.C3);
2. target-safe integerization (121.C13);
3. the exact Fourier/discrepancy reductions (121.C17)--(121.C20);
4. the no-gain conclusion that local character pairing alone returns the
   unmatched-crossing discrepancy.

Retain `M9-M1-global-lower-radial-signed-estimate` open unless a new bound
for (121.C12) or (121.C20) is proved. No statement here proves blockwise
M9-M1, M9-M2, endpoint uniformity, M9, or any improved exponent.

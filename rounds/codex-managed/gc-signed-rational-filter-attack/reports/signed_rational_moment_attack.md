# Round 207: complete signed rational sixth-moment attack

Campaign: `gc-signed-rational-filter-attack`. Task: `signed_rational_moment_attack`. Role: discovery, selected context; not blind. Date: 2026-09-27. Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`. Candidate evidence only. Effort: 100 percent analytical/algebraic; no mathematical numerical experiment and no new external theorem import.

## 1. Result: a scoped obstruction after exact physical frequency grouping

The complete filtered hyperbola formula has two disjoint sets of reduced rational frequencies. The small-divisor arm has odd reduced denominators. The quotient-character arm has reduced denominators divisible by four. All coincident frequencies *within* either arm can be summed exactly. Their multiplicity factor is a partial sum of the actual series \(\sum_j\chi_4(j)/j\), lying between \(2/3\) and \(1\) whenever its first term is present. Consequently, grouping equal frequencies does not remove the large physical coefficient mass.

Let \(Q_N(x)\) denote the complete two-arm rational sum defined in Section 3. The exact centered additive filter \(E_N\) satisfies

\[
 E_N(x)=Q_N(x)+\mathcal R_N(x)+O_A(X^{-A}),\qquad
 \int_{X/2}^{3X}|\mathcal R_N(x)|^6dx\ll \sqrt X\,H,
 \quad H=T/\sqrt N.                                      \tag{1}
\]

The remainder estimate includes the moving threshold, real endpoints, all lattice points and the varying width. It is target-safe.

The main result of the attempted sixth estimate is a **no-go for taking absolute values separately on the integrated rational sextuples**, even after performing all single-frequency character cancellations. For the actual grouped coefficients, define the complete termwise integral majorant \(\mathfrak M_6\) in (18). Uniformly throughout the whole middle range,

\[
 \boxed{\mathfrak M_6\gg X^3H=T^{7-\alpha/2},\qquad N=T^\alpha.} \tag{2}
\]

This exceeds the sufficient sixth threshold \(T^{129/25-6\omega(\alpha)}\) by a factor at least \(T^{517/250}\), before arbitrary small epsilon losses. The obstruction uses actual character coefficients, the actual nonnegative Fourier amplitude, their exact signs, the actual width \(h(x)\), and the full displaced interval. It is not an arbitrary-coefficient example or merely an expensive upper estimate.

Its scope is precise: (2) includes both exact and near rational triple relations. It does not assert a lower bound after all exact triple relations have been removed. It does not obstruct grouping and cancelling the entire signed aggregate at a common total frequency before taking a norm. It gives **no lower bound for the signed sixth moment**, and does not refute the twelfth-moment objective. The best complete twelfth exponent remains \(10\beta\).

## 2. Exact statement and hypotheses

Take real \(T\ge2\), \(X=T^2\),

\[
 I=[T/\sqrt2,\sqrt3T],\quad J=[X/2,3X],\quad
 T^{52/125}<N=2^j<T^{99/125},\quad h(x)=2\sqrt{x}/\sqrt N.
\]

Write \(H=T/\sqrt N\), so \(\sqrt2H\le h(x)\le2\sqrt3H\). This report uses \(H\) as a scale, whereas some predecessor reports used its fixed upper-window multiple. In particular,

\[
 T^{151/250}<H<T^{99/125},\qquad H=o(T).
\]

Use exactly the fixed radial-mollifier transform \(\Psi\) and smooth partition \(v(t)=\phi(t/2)-\phi(t)\) from the permitted Round205 interface. Thus \(v\ge0\), \(\operatorname{supp}v\subset[1,4]\), and \(v\not\equiv0\). Put

\[
 a_{N,T}(t)=t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2),\qquad
 F(u)=-\int_1^2a_{N,T}(t)\sin(2\pi tu)\,dt,
\]

\[
 E_N(x)=\sum_{m\ge1}(r_2(m)-\pi)F((m-x)/h(x)).            \tag{3}
\]

All constants can depend on the fixed filters. Since \(N/T\to0\) uniformly over this band and \(\Psi(0)=1\), for all sufficiently large \(T\) the amplitude \(a_{N,T}\) is nonnegative on its whole support. There are fixed \(1<u<v<2\) and \(c>0\) on which it is at least \(c\), uniformly. Bounds for bounded \(T\) are irrelevant to the asymptotic lower-bound obstruction and are absorbed in constants for the upper identities.

Use \(e(z)=\exp(2\pi iz)\) and \(\widehat F(\xi)=\int F(u)e(-\xi u)du\). Then

\[
 \widehat F(\xi)=\begin{cases}
  \frac i2a_{N,T}(\xi),&1\le\xi\le2,\\
  -\frac i2a_{N,T}(-\xi),&-2\le\xi\le-1,\\
  0,&\text{otherwise}.
 \end{cases}                                               \tag{4}
\]

The forthcoming Fourier sums use \(e(-\lambda x)\). This convention is essential for the sign of the quotient Gauss factor.

Set

\[
 M=\lceil6X\rceil,\quad D=\lfloor\sqrt M\rfloor,\quad
 L=\lfloor M/(D+1)\rfloor.
\]

Here \(D,L\asymp T\). Retain the strict threshold \(m>D\ell\), including at equality. The relevant accepted parameters are

\[
 \beta=2\theta_{LY}-\tfrac12,\quad \tfrac18<\beta<\tfrac{27}{208},\qquad
 \omega(\alpha)=\min\{\alpha/4,\beta,(1-\alpha)/2\}.
\]

The available supremum is \(W_0=T^{\omega(\alpha)}\), up to harmless constants and epsilon losses. The sufficient arithmetic certificate, which is not necessary for the actual twelfth moment, is

\[
 K_6(N)=\int_J|E_N(x)|^6dx
       \ll_\epsilon T^{129/25-6\omega(\alpha)+\epsilon}.    \tag{5}
\]

## 3. Proof and fully priced attempt

### 3.1 Complete hyperbola identity, means and tails

Choose a fixed smooth cutoff \(\eta\) supported in \([1/4,6]\), equal to one on \([1/3,4]\). Replacing (3) by its \(\eta(m/X)\)-localized version changes it by \(O_A(X^{-A})\) uniformly on \(J\), for any prescribed \(A\). This follows from \(r_2(m)\ll_\epsilon m^\epsilon\), the uniform Schwartz bounds, and \(X/H\to\infty\) by a fixed power. Increasing a fixed decay order pays the entire infinite upper tail and the nonpositive lattice tail whenever a complete lattice sum is introduced below.

For each positive integer \(m\le M\), the exact divisor partition is

\[
 \frac{r_2(m)}4
 =\sum_{d\le D}\chi_4(d)1_{d\mid m}
  +\sum_{\ell\le L}1_{m>D\ell}1_{\ell\mid m}\chi_4(m/\ell). \tag{6}
\]

The first arm contains \(d=D\); the second is exactly the complementary divisor range. Its periodic quotient character is

\[
 p_\ell(m)=1_{m\equiv\ell\ (4\ell)}-1_{m\equiv3\ell\ (4\ell)}.
                                                               \tag{7}
\]

After (6) is inserted, removing \(\eta\) from each complete lattice sum incurs only another \(O_A(X^{-A})\): there are \(O(T)\) arm labels and the removed lattice terms are a distance \(\gg X\) from every center. This polynomial label cost is absorbed by a larger fixed Schwartz order. Formula (6) is not asserted for the newly introduced tail integers; the estimate is on the two explicit periodic sums themselves.

Also \(\sum_{m\in\mathbb Z}F((m-x)/h)=0\) for \(h>2\), since all sampled Fourier arguments \(hk\) miss (4), including \(k=0\). Thus the subtracted constant \(\pi\), or alternatively the \(O(D^{-1})\) mean remainder in the centered version of (6), contributes only its already paid cutoff tail. No individual unfiltered correlation has had its mean silently deleted.

### 3.2 Moving-threshold replacement

Define the exact freezing error after completion by

\[
 \mathcal R_N(x)=4\sum_{\ell\le L}\sum_{m\in\mathbb Z}
 p_\ell(m)\{1_{m>D\ell}-1_{x>D\ell}\}
 F((m-x)/h(x)).                                            \tag{8}
\]

When the difference of indicators is nonzero, \(m\) is on the opposite side of \(D\ell\) from \(x\), with the strict-equality convention kept. Therefore \(|m-x|\ge|x-D\ell|\). Bounding the two residue classes by their containing \(\ell\)-lattice and summing a Schwartz tail gives, for any fixed large \(A\),

\[
 |\mathcal R_N(x)|\ll_A
 \sum_{\ell\le L}(1+H/\ell)
       (1+|x-D\ell|/H)^{-A}.                              \tag{9}
\]

For example, this follows by bounding the one-sided lattice tail by its first term plus \(\ell^{-1}\) times the corresponding tail integral, choosing the original decay order larger than \(A+1\). This argument is uniform at lattice and threshold equality points.

For \(\ell<cT\), with a sufficiently small fixed \(c>0\), the distance \(|x-D\ell|\) is \(\gg X\) throughout \(J\). These terms in (9) are \(O_B(X^{-B})\) after increasing \(A\), since \(\sum_{\ell\le L}(1+H/\ell)\ll T+H\log T\). For all other \(\ell\), the factor \(1+H/\ell\) is bounded. The centers \(D\ell\) have spacing \(D\asymp T\gg H\). Hence the sum of the decay bumps is uniformly bounded, and its sixth power is bounded by a constant times their sum. Integrating each bump over the real interval, or over the whole line for an upper bound, costs \(O(H)\). This proves

\[
 \|\mathcal R_N\|_\infty\ll1,
 \qquad \int_J|\mathcal R_N|^6dx\ll LH\ll TH.              \tag{10}
\]

It also proves \(\int_J|\mathcal R_N|^2dx\ll TH\). Neither \(h\) nor the endpoints have been discretized. Thresholds outside \(J\), and partial bumps crossing its endpoints, were included in (9).

### 3.3 Exact phases, all harmonics and reduced-frequency coefficients

For a complete progression, Poisson summation with the convention in Section 2 is

\[
 \sum_{m\equiv r\ (q)}F((m-x)/h)
 =\frac hq\sum_{k\in\mathbb Z}\widehat F(hk/q)e(k(r-x)/q).
                                                               \tag{11}
\]

In particular a whole progression vanishes if \(q<h/2\). The endpoint harmonics cause no difficulty, since the smooth compact amplitude vanishes at its support endpoints. This cancellation applies to the completed periodic terms, not to (8).

For the quotient arm, the exact factor is

\[
 e(k/4)-e(3k/4)=2i\chi_4(k).                              \tag{12}
\]

Even harmonics vanish; both odd residue branches are present. Thus the complete rational main term is \(Q_N=A_N+B_N\), where

\[
 A_N(x)=4h(x)\sum_{d\le D}\frac{\chi_4(d)}d
       \sum_{k\in\mathbb Z}\widehat F(h(x)k/d)e(-kx/d),
\]

\[
 B_N(x)=2ih(x)\sum_{\ell\le L}\frac{1_{x>D\ell}}\ell
       \sum_{k\in\mathbb Z}\chi_4(k)
       \widehat F(h(x)k/(4\ell))e(-kx/(4\ell)).            \tag{13}
\]

The positive and negative harmonics are both retained. These sums have finitely many nonzero harmonics on all of \(J\): their numerators are at most a fixed multiple of \(D/H\) or \(L/H\). All low-period deletions are consequences of (4), rather than extra assumptions. Equations (6)--(13) prove (1).

Now sum every coincident single frequency before estimating. Define

\[
 s(y)=\sum_{1\le j\le y}\frac{\chi_4(j)}j,
 \qquad
 s_*(y,z)=\sum_{\substack{j\ge1\\j\le y, j<z}}
                       \frac{\chi_4(j)}j.
\]

Every nonempty such prefix has value in \([2/3,1]\): the nonzero terms are the alternating decreasing series \(1-1/3+1/5-1/7+\cdots\). An empty prefix is zero. In particular no claimed cancellation bound has been substituted for the actual multiplicity sum.

For reduced \(a/q>0\) in the first arm, \(q\) is odd, \((a,q)=1\), \(q\le D\), and its exact coefficient is

\[
 c^A_{a/q}(x)=\frac{4h(x)\chi_4(q)}q
             \widehat F(h(x)a/q)s(D/q).                  \tag{14}
\]

Indeed \(d=jq\), \(k=ja\), and \(\chi_4(d)=\chi_4(j)\chi_4(q)\). In the second arm every reduced positive fraction has the unique form \(a/(4b)\), where \(a\) is odd, \((a,b)=1\), and \(b\le L\). Its exact coefficient is

\[
 c^B_{a/(4b)}(x)=\frac{2ih(x)\chi_4(a)}b
  \widehat F(h(x)a/(4b))s_*(L/b,x/(Db)).                  \tag{15}
\]

Here \(\ell=jb\), \(k=ja\), with \(j\) odd when the coefficient is nonzero. The strict inequality in \(s_*\) preserves every threshold equality. Negative-frequency coefficients are the complex conjugates. By (4), the positive first-arm coefficient is \(i\chi_4(q)\) times a nonnegative real number, and the positive second-arm coefficient is \(-\chi_4(a)\) times a nonnegative real number.

An odd reduced denominator cannot equal a reduced denominator divisible by four. Therefore the two arms have no exact single-frequency collisions with each other. This does not imply orthogonality on a finite displaced interval, and does not permit removal of their mixed sixth terms.

Let \(\Lambda\) be the finite union of every reduced positive or negative frequency that can occur for some \(x\in J\), retaining its coefficient function even where it is zero. Then

\[
 Q_N(x)=\sum_{\lambda\in\Lambda}c_\lambda(x)e(-\lambda x),
 \qquad c_{-\lambda}(x)=\overline{c_\lambda(x)}.            \tag{16}
\]

Thus \(Q_N\) is real. This representation retains all harmonics, all multiplicities, both arms, and all moving masks on one common domain.

### 3.4 The physical coefficient norms

The support of (14) requires \(q\ge h(x)/2\) and \(a\asymp q/h(x)\). There are at most \(O(1+q/h(x))\) such numerators. Formula (14) therefore gives

\[
 \sum_{\lambda\ {\rm in} A}|c_\lambda(x)|
 \ll h\sum_{h/2\le q\le D}\left(\frac1q+\frac1h\right)
 \ll D,
\]

\[
 \sum_{\lambda\ {\rm in} A}|c_\lambda(x)|^2
 \ll h^2\sum_{h/2\le q\le D}
         \left(\frac1{q^2}+\frac1{hq}\right)
 \ll H\log(2X).
\]

We used \(H\log X=o(D)\), which holds uniformly on the band. Formula (15) has the identical estimates with \(b\ge h/8\), \(b\le L\), and \(a\asymp b/h\); the mask can only remove a nonempty bounded prefix. Consequently

\[
 \|c(x)\|_1\ll T,\qquad
 \|c(x)\|_2^2\ll H\log(2X),\qquad
 \|c(x)\|_\infty\ll1.                                    \tag{17}
\]

These are norms of the **already grouped physical vector**, not of a larger arbitrary array. The lower bounds \(\|c(x)\|_1\gg T\) and \(\|c(x)\|_2^2\gg H\) follow uniformly from the first-arm count proved next, applying that count separately with each actual \(h(x)\). In particular the actual character does not shrink the grouped \(\ell^1\) mass to the shell width.

### 3.5 A lower bound for the integrated rational sixth majorant

The exact expansion is

\[
 \int_J|Q_N(x)|^6dx
 =\sum_{\lambda_1,\ldots,\lambda_6\in\Lambda}
   \int_J\prod_{j=1}^6c_{\lambda_j}(x)
              e(-x\textstyle\sum_j\lambda_j)dx.
\]

Define the specified absolute placement by

\[
 \mathfrak M_6=
 \sum_{\lambda_1,\ldots,\lambda_6\in\Lambda}
 \left|\int_J\prod_{j=1}^6c_{\lambda_j}(x)
              e(-x\textstyle\sum_j\lambda_j)dx\right|.   \tag{18}
\]

We prove (2) for this actual complete majorant. It is stronger than merely observing a large upper bound from (17).

Take \(x_0=X\), \(h_0=h(X)=2H\). Choose fixed \(u<u'<v'<v\) within the positive-amplitude interval of Section 2, and choose a sufficiently small fixed \(\delta>0\). Then the interval

\[
 J_0=[(1-\delta)X,(1+\delta)X]\subset J
\]

has the property that \(h(x)\lambda\in[u,v]\) whenever
\(x\in J_0\) and \(u'/h_0\le\lambda\le v'/h_0\). This retains the exact square-root width; only its continuous variation over a fixed subinterval is used.

Let \(\mathcal C\) consist of all reduced first-arm fractions \(a/q\) satisfying

\[
 D/2\le q\le D,\quad q\ {\rm odd},\quad (a,q)=1,
 \qquad u'q/h_0\le a\le v'q/h_0.                         \tag{19}
\]

The number of such \(a\) for each \(q\) is

\[
 \frac{v'-u'}{h_0}\varphi(q)+O(\tau(q)),                  \tag{20}
\]

by Mobius inversion in the interval, with no equidistribution hypothesis. For completeness, the elementary mean is

\[
 \sum_{q\le Y,\ q\ {\rm odd}}\varphi(q)
 =\frac{Y^2}{4}\prod_{p\ {\rm odd}}(1-p^{-2})+O(Y\log(2Y)).
                                                               \tag{21}
\]

Indeed insert \(\varphi(q)=q\sum_{d\mid q}\mu(d)/d\), write \(q=dm\) with both variables odd, and use
\(\sum_{m\le Z, m\ {\rm odd}}m=Z^2/4+O(Z)\). Absolute convergence of the main Euler product gives a positive constant; its truncated tail costs \(O(Y)\). Also \(\sum_{q\le D}\tau(q)\ll D\log(2D)\), by counting divisor pairs. Equations (20)--(21), differenced at \(D/2\), show

\[
 |\mathcal C|\asymp D^2/H.                               \tag{22}
\]

The error \(O(D\log D)\) is smaller than the main term because \(D/H\asymp\sqrt N\) grows by a fixed positive power uniformly over the entire middle range. No prime-denominator restriction or unproved prime estimate is used.

For \(\lambda=a/q\in\mathcal C\), write
\(c_\lambda(x)=i\chi_4(q)b_\lambda(x)\). The function \(b_\lambda\) is nonnegative on **all** of \(J\), and

\[
 b_\lambda(x)\ge cH/D\quad(x\in J_0).                   \tag{23}
\]

This follows directly from (14), the fixed positive amplitude, and \(s(D/q)\ge2/3\) (in fact it equals one in this denominator range). Set \(w_\lambda=cH/D\) with the fixed constant made small enough for (23). Then \(\sum_{\lambda\in\mathcal C}w_\lambda\asymp D\).

All triple sums of members of \(\mathcal C\) lie in an interval of length \(O(1/H)\). Partition that interval into half-open bins of width \(\zeta/X\), where \(\zeta>0\) is a sufficiently small fixed constant. There are at most \(C X/H\) bins. If \(m_j\) denotes the total product weight \(w_{\lambda_1}w_{\lambda_2}w_{\lambda_3}\) of ordered triples in bin \(j\), then Cauchy--Schwarz gives

\[
 \sum_jm_j^2\ge
 \frac{(\sum_{\lambda\in\mathcal C}w_\lambda)^6}{CX/H}
 \gg D^6H/X.                                             \tag{24}
\]

Every paired pair of triples counted here has
\(\Delta=\lambda_1+\lambda_2+\lambda_3-\mu_1-\mu_2-\mu_3\)
with \(|\Delta|\le\zeta/X\). Its coefficient product in (18), taking positive frequencies for the first triple and negative for the second, has a sign independent of \(x\): the factors \(i^3(-i)^3\) give one, and the remaining sign is the product of the six actual \(\chi_4(q)\). After removing that fixed sign and rotating by \(e(x_0\Delta)\), the real part of the integrand is

\[
 \prod b_\lambda(x)\,\cos(2\pi(x-x_0)\Delta).
\]

For sufficiently small \(\zeta\), the cosine is at least \(1/2\) on the **entire** interval \(J\). All amplitudes are nonnegative there, so no portion of the displaced window can cancel this lower bound. Its integral is at least its integral over \(J_0\), which by (23) is

\[
 cX\,w_{\lambda_1}w_{\lambda_2}w_{\lambda_3}
       w_{\mu_1}w_{\mu_2}w_{\mu_3}.                       \tag{25}
\]

Multiply (24) by the factor \(cX\) in (25). This proves
\(\mathfrak M_6\gg D^6H\asymp X^3H\), as asserted. Every frequency in this argument is a genuine nonzero physical frequency after exact single-frequency grouping. Repeated frequencies are allowed exactly as in the sixth expansion. Both exact and near triple relations remain; no unjustified exact-diagonal subtraction has been made.

The second arm and every mixed-arm term are retained in (18); the first-arm core is only a positive subsum of that **majorant**. It is not legitimate to use it as a positive subsum of the original signed sixth integral.

### 3.6 Current signed estimates and reconstruction

The available actual variance bound, inherited from the original physical block and its reviewed bridge, is \(\int_J|E_N|^2\ll_\epsilon XH T^\epsilon\). Together with (10), it gives the same bound for \(Q_N\). Combining it with the complete coefficient bound \(|Q_N|\ll T\) from (17) yields only

\[
 \int_J|Q_N|^6\ll_\epsilon T^4 XH T^\epsilon
                         =X^3H T^\epsilon.                \tag{26}
\]

This is a lawful upper bound for the **complete signed** sum, including both arms and masks. It is recorded solely to price the failed coefficient-norm attempt. Pair variance has not been rebranded as a sixth gain. The stronger existing accepted-distribution calculation already gives

\[
 K_6(N)\ll_\epsilon T^{5+\epsilon}N^{-29/110},             \tag{27}
\]

and the same estimate transfers to \(Q_N\) using (1), since its threshold error is much smaller. Thus (26) does not improve any available result. Equation (2) explains why directly bounding the termwise integrated rational sixth expansion cannot repair this failure, even though it preserves more cancellation than an ungrouped divisor expansion.

The precise lower-power excess of (2) over the sufficient threshold (5) is

\[
 d(\alpha)=\frac{46}{25}-\frac\alpha2+6\omega(\alpha).
                                                               \tag{28}
\]

On the three ranges cut by \(4\beta\) and \(1-2\beta\), it equals respectively

\[
 \frac{46}{25}+\alpha,\qquad
 \frac{46}{25}-\frac\alpha2+6\beta,\qquad
 \frac{121}{25}-\frac{7\alpha}{2}.
\]

Both breakpoints lie inside the prescribed middle interval. The first piece is at least \(282/125\); the second is at least \(67/50+7\beta>443/200\); and the last is at least
\(121/25-(7/2)(99/125)=517/250\). This proves the uniform comparison stated after (2).

For clarity, restore the physical amplitude and Jacobian. The reviewed additive bridge gives

\[
 S_N(R)=R^{-1/2}E_N(R^2)
       +O_\epsilon(T^{-1/2+\epsilon}N^{-1})+O_A(T^{-A}).
\]

Since \(dR=dx/(2\sqrt x)\),

\[
 \int_I|S_N|^{12}dR
 \ll_\epsilon T^{-4+6\omega(\alpha)+\epsilon}K_6(N)
                     +O_\epsilon(T^{-2+\epsilon}).       \tag{29}
\]

The sixth threshold-freezing error contributes at most

\[
 T^{-4+6\omega}TH=T^{-2-\alpha/2+6\omega}
 \le T^{-2+\alpha},                                      \tag{30}
\]

before epsilon losses, which is negligible throughout the full range. The sixth curvature error is \(O(T^{-2+\epsilon}N^{-6})\) before multiplying by \(W_0^6\le N^{3/2}\); all rapid tails remain negligible after fixed moments and logarithmically many dyadic blocks.

In contrast, the failed rational majorant in (2), inserted in the same certificate, is at least \(T^{3-\alpha/2+6\omega}\). Its excess over \(T^{29/25}\) is exactly (28). This is a statement about the specified **certificate**, not a lower bound for \(\int|S_N|^{12}\).

Every middle scale is covered, and equality at a dividing scale remains in its previously estimated outer band. Minkowski over the entire middle family costs only fixed logarithmic powers and retains all cross-block terms. Using the stronger existing complete moment estimate rather than (26) or (27), the full middle sum remains bounded by \(T^{10\beta+\epsilon}\). No new pointwise exponent or M1/M2 conclusion follows.

## 4. First doubtful or unproved step

There is no asserted cancellation theorem after (16). The first unproved estimate is the bound (5) for the complete **signed** sixth aggregate, equivalently a target-size estimate for \(Q_N\) after the target-safe error (1) is removed. In terms of (16), this requires using cancellation among the actual character-signed sextuples and their displaced oscillatory integrals, including all exact, near, repeated and mixed-arm configurations.

The first invalid step in the attempted norm placement would be to assert that the termwise integral majorant (18) is target-size. Equations (19)--(28) refute that assertion on the actual physical coefficients. Single-frequency cancellation has already been performed in (14)--(15), so leaving that step undone is not the source of the obstruction.

The following alternatives are **not** refuted: estimating the whole signed moment directly; regrouping all equal total frequencies before taking absolute values; using cancellations between rational sextuples with different character signs; or establishing a separate exact-relation estimate followed by a stronger signed near-relation argument. No claim here converts (5), a sufficient certificate, into a necessary condition for the frozen twelfth target.

No primary theorem was imported. In particular no Kloosterman theorem is credited merely because the phase in (13) is reciprocal: the present variable is a real denominator, and no finite-modulus inverse kernel, complete coefficient factorization, or external theorem hypothesis match has been proved. The permitted strategy's row-interval mask lemma would control a mask only after an appropriate operator estimate exists; it supplies no such estimate by itself.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `complete_middle_range` | PASS: all \(52/125<\alpha<99/125\), uniform \(D/H\gg T^{26/125}\), exact inherited boundary allocation; no smaller complement is omitted. |
| `actual_two_arm_characters` | PASS: (6)--(7) retain every divisor, both quotient residues and even-character zeros; (12), (14), (15) retain the exact phases. |
| `all_harmonics_and_duplicates` | PASS: positive and negative harmonics retained; every equal single frequency grouped exactly; odd versus four-divisible denominators disjoint; all sextuples and mixed terms remain. |
| `moving_threshold_error` | PASS: strict threshold retained in (8) and (15); full \(L^6\) error \(O(TH)\) proved and restored in (30). |
| `low_period_annihilation` | PASS: follows from (11) and the Fourier support only for complete progressions; not applied to a truncated threshold term. |
| `variable_width` | PASS: exact \(h(x)\) in every identity, mask, norm and integral; fixed core uses a continuity interval without freezing \(h\). |
| `real_endpoints_and_tails` | PASS: real \(T,X,x\), strict hyperbola equality, full \(J\), partial error bumps, negative-lattice tails and infinite positive tails all paid. |
| `signed_not_positive` | PASS as a scoped rejection: actual \(\mathfrak M_6\) is large after exact single-frequency grouping; no signed-moment lower bound is inferred. |
| `restored_sixth_and_twelfth_powers` | PASS: \(T^{-4}\) Jacobian/amplitude, \(W_0^6\), \(TH\) threshold error and every dyadic block accounted for; the certificate fails by at least \(T^{517/250}\). |
| `source_hypotheses` | PASS within inherited scope: no new source import; retained accepted distribution and repaired real-\(X\) Li--Yang consequence keep their existing qualifications. |
| `full_proof_scope` | PASS: no promotion of the twelfth target, M1/M2, a pointwise exponent, or the quarter theorem; even the requested milestone would only give \(102/325\). |

All controls are analytical. There was no mathematical numerical experiment. Exact rational triple relations have not been removed from the majorant lower bound; that limitation is part of its statement, rather than an unperformed control concealed as a passed stronger claim.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted local context were read:

- `rounds/codex-managed/gc-signed-rational-filter-attack/briefs/signed_rational_moment_attack.md`.
- `protocol.md`.
- `state/proof_obligations.yml`, with the relevant authoritative entries extracted: `GC-target`, `GC-external-Li-Yang-theta-star`, `GC-complete-square-root-large-values-moment-bound`, `GC-physical-twelfth-moment-absolute-majorant-obstruction`, and `GC-weighted-square-root-exact-resonance-mass`.
- `state/active_campaign.yml`, Round207.
- `strategy/round207_signed_rational_filter_attack.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/actual_divisor_shell_attack.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_divisor_obstruction_review.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md`.

The Round205/206 artifacts supply the reviewed actual filter interface, reconstruction, variance, suprema, and existing sixth estimate. The hyperbola transformation, quotient Fourier factor, complete grouping, threshold estimate, coprime count and majorant obstruction are derived above. The exact-resonance and prior absolute-obstruction graph entries are used only to preserve their scope; their mathematical estimates are not assumed to apply to the new rational triple relation problem.

Substantive progress messages were exchanged with the conductor. The conductor independently reported the same anticipated \(X^3H\) binning scale after this task had reported its own coefficient-grouping direction; the proof here supplies its own variable-width, coprime-count and full-window argument. A Fourier-sign convention check was sent to the conductor. This is selected-context discovery, not an isolated or blind review. No sibling report or excluded source file was read. No web source theorem or source card is used.

## 7. Recommended state effect

**No change to accepted mathematical state or the proof draft.** Retain this as a scoped actual-coefficient norm-placement obstruction and a fully priced no-gain attempt, subject to the conductor's seam review. Reject the claim that exact single-frequency grouping followed by the termwise integrated rational sixth majorant proves the sufficient threshold.

Keep the complete signed arithmetic estimate and the full twelfth target open. The bound \(10\beta\), the required saving profile \(g(\alpha)=6\omega-4/25-29\alpha/110\), all accepted source qualifications, and every M1/M2 obligation remain unchanged.

Only this assigned report was written. No authoritative state, proof draft, validation matrix, shared synthesis, source card, or successor artifact was edited. The task stops here.

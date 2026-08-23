# Round 123 report: signed alias-product attack

Campaign: `m9-m2-unbalanced-reciprocal-gram-factorization-gate`

Task: `signed_alias_product_attack`

Role: discovery

Starting graph SHA-256:
`d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`

## 1. Result

The proposed phase integerization is valid, including uniformly decaying
physical tails. More generally, if \(M\in\mathbb Z\), \(M\asymp X\), and
the amplitudes remain frozen at \(X\), then

\[
 \boxed{\quad
 |\mathscr R_X-\mathscr R_M^\sharp|
 \ll_\varepsilon (1+|M-X|)X^\varepsilon .
 \quad}
\tag{123.1}
\]

Thus \(M=N=\lfloor X\rfloor\) costs \(O_\varepsilon(X^\varepsilon)\).
It is also lawful to put \(Q=2^t\asymp X^{1/4}\) and choose an odd
integer \(M_0\) with

\[
 M=QM_0,\qquad |M-X|\leq Q.
\tag{123.2}
\]

This engineered centre costs \(O_\varepsilon(X^{1/4+\varepsilon})\),
exactly within the scalar target.

The unshifted weighted \(k\)-Cauchy Gram is exact and character
preserving, but it is a strictly stronger sufficient norm: its literal
diagonal is \(\asymp R=X/D>X^{1/2}\), whereas its target is
\(X^{1/2+\varepsilon}\). Its nonzero exact aliases are harmless. For a
generic integer centre \(M=2^tM_0\), \(M_0\) odd, every nonzero exact
alias has \(2^{t+1}\mid j\), with fixed sign

\[
 \chi _4(r)\chi _4(s)=(-1)^{j/2^{t+1}},
\tag{123.3}
\]

and all such ordered pairs together contribute
\(O_\varepsilon(X^\varepsilon)\). The diagonal is the exceptional
degenerate factor fibre \(j=E=0\); it is
not included in this divisor count.

A shifted \(k\)-Fejér Gram gives a genuine strict subpackage. Let

\[
 H_0=\left\lceil {R\over X^{1/2}}\right\rceil
 \asymp {X^{1/2}\over D}.
\tag{123.4}
\]

Then \(1\leq H_0\ll K\) throughout the strict UNBAL range. In the exact
shifted Gram, not merely in its \(h=0\) slice, the complete nearest-alias
sector \(j=0\), including \(r=s\) and every \(r\ne s\), is

\[
 O_\varepsilon(R/H_0\,X^\varepsilon)
 =O_\varepsilon(X^{1/2+\varepsilon}).
\tag{123.5}
\]

Together with (123.1) and the exact-alias divisor bound, this proves the
following power-excess inverse theorem. For every fixed \(\eta>0\), if a
flat-smooth row satisfies

\[
 |\mathscr R_X|\geq X^{1/4+\eta},
\tag{123.6}
\]

then, after either floor integerization or (123.2), the complete signed
ordered-pair aggregate with

\[
 j\ne0,\qquad E\ne0,\qquad
 |E|\leq {X^{1+\eta/10}\over L}
\tag{123.7}
\]

has positive real size \(\gg X^{1/2+2\eta}\) in the \(H_0\)-shifted
Gram, after changing the implicit constant and taking \(X\) large. Thus
every power-sized violation is forced into the nonzero, nonexact,
near-product alias aggregate; it cannot be carried by the diagonal, the
whole zero-alias sector, an exact collision, or a rapid alias tail.

No estimate for that remaining actual-sign aggregate is proved. The
two-adic formula is exact but tautological under the inverse factor map;
negative aliases are conjugate partners with the same character sign,
not cancelling partners. The nominal joint localization capacity at
shift length \(H\) is

\[
 {R^2\over KH}
 =\left({D\over L}\right)^2{K\over H}.
\tag{123.8}
\]

At \(H=H_0\) this is \(X^{1/2}D/L\), still a factor \(D/L\) above the
squared target. It decreases to \((D/L)^2\) only at \(H\asymp K\), where
the Fejér construction has the capacity of the original scalar row and
is a self-return. Formula (123.8) is a capacity ledger, not a proved
absolute pair-count theorem. A saving from it requires a new signed thin
product-annulus estimate. Hence the outcome is an inverse theorem plus a
scoped no-go for automatic defect-parity cancellation, not the quarter
bound.

## 2. Exact statement and hypotheses

Let \(X\geq2\) be real and

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R={X\over D},\qquad K={XL\over D^2},
\tag{123.9}
\]

where

\[
 {1\over4}\leq\delta<{1\over2},\qquad
 0\leq\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463.
\tag{123.10}
\]

Fix one literal flat smooth UNBAL component. Put

\[
 W_r=W\!\left({X\over rD}\right),\qquad
 q_{r,k}=q_L\!\left({4Xk\over r^2}\right),
\tag{123.11}
\]

where \(q_L(h)=\eta(h/L)\Phi(h/(H_D+1))\) and \(W\) are the fixed
Round-118 profiles. All support entries, exits, and overlap restrictions
are retained. The row is

\[
 \mathscr R_X=
 \sum_{r\ {\rm odd}}\chi _4(r)W_r
 \sum_k {q_{r,k}\over k}e(Xk/r).
\tag{123.12}
\]

For an integer \(M\asymp X\), its phase-only integerization is

\[
 \mathscr R_M^\sharp=
 \sum_{r\ {\rm odd}}\chi _4(r)W_r
 \sum_k {q_{r,k}\over k}e(Mk/r).
\tag{123.13}
\]

Neither \(W_r\), \(q_{r,k}\), \(D,L,R,K\), nor the denominator \(4X\)
in the physical kernel is changed when \(X\) is replaced by \(M\) in the
phase.

Define

\[
 B_k(M)=\sum_{r\ {\rm odd}}\chi _4(r)W_rq_{r,k}e(Mk/r).
\tag{123.14}
\]

The exact unshifted weighted Gram is

\[
 |\mathscr R_M^\sharp|^2
 \leq \left(\sum_{k\asymp K}{1\over k}\right)
 \mathcal G_M\ll \mathcal G_M,
 \qquad
 \mathcal G_M=\sum_k {|B_k(M)|^2\over k},
\tag{123.15}
\]

and

\[
 \mathcal G_M=
 \sum_{r,s\ {\rm odd}}\chi _4(r)\chi _4(s)W_r\overline{W_s}
 \mathcal K_M(r,s),
\tag{123.16}
\]

\[
 \mathcal K_M(r,s)=
 \sum_k {q_{r,k}\overline{q_{s,k}}\over k}
 e\!\left(Mk\left({1\over r}-{1\over s}\right)\right).
\tag{123.17}
\]

For the shifted form, set

\[
 w_r(k)={q_{r,k}\over k},\qquad
 c_k=\sum_{r\ {\rm odd}}\chi _4(r)W_rw_r(k)e(Mk/r),
\tag{123.18}
\]

and zero-extend in one fixed integer interval \(I\) of length
\(J\asymp K\) containing every literal sampled support. For
\(1\leq H\leq K/C\), define

\[
 A^{(H)}_{r,n}=\sum_{a=0}^{H-1}w_r(n+a)e(Ma/r)
\tag{123.19}
\]

and

\[
 \mathcal F_{M,H}={J+H-1\over H^2}
 \sum_n\left|\sum_{a=0}^{H-1}c_{n+a}\right|^2.
\tag{123.20}
\]

Then

\[
 |\mathscr R_M^\sharp|^2\leq\mathcal F_{M,H},
\tag{123.21}
\]

and its full ordered-pair kernel is

\[
 \Gamma_{M,H}(r,s)=
 {J+H-1\over H^2}W_r\overline{W_s}
 \sum_n A^{(H)}_{r,n}\overline{A^{(H)}_{s,n}}
 e\!\left(Mn\left({1\over r}-{1\over s}\right)\right).
\tag{123.22}
\]

Thus

\[
 \mathcal F_{M,H}=
 \sum_{r,s\ {\rm odd}}\chi _4(r)\chi _4(s)
 \Gamma_{M,H}(r,s).
\tag{123.23}
\]

Equivalently, expansion before completing the \(a\)-blocks gives the
literal correlations

\[
 \sum_k {q_{r,k+h}\overline{q_{s,k}}\over(k+h)k}
 e\!\left(Mk\left({1\over r}-{1\over s}\right)+{Mh\over r}\right),
 \qquad |h|<H,
\tag{123.24}
\]

with Fejér weight \(1-|h|/H\), the exact zero-extension, and the exact
prefactor \(\asymp K/H\). Formula (123.24), rather than an unshifted
rectangular model, is the literal shifted amplitude.

All statements in this report concern only this flat-smooth owner. No
sharp, clipped, starred, hard, arithmetic, or transition kernel is
included or declared an error.

## 3. Proof or derivation

### 3.1 Target-safe phase integerization

The coefficientwise physical identity for (123.13) is

\[
 \mathscr R_M^\sharp=
 \sum_{r\ {\rm odd}}\chi _4(r)W_r
 \sum_d\mathcal Q_L\!\left({r(M-rd)\over4X}\right),
\tag{123.25}
\]

where

\[
 \mathcal Q_L(y)=\int_0^\infty {q_L(h)\over h}e(hy)\,dh.
\tag{123.26}
\]

The denominator in (123.25) is \(4X\), not \(4M\). Uniform smoothness
gives, for every \(A\geq0\),

\[
 |\mathcal Q_L'(y)|
 \ll_A L(1+L|y|)^{-A}.
\tag{123.27}
\]

Let \(z\) lie between \(X\) and \(M\), and put \(\Delta=D/L\). Since
\(r\asymp R\), differentiation of the summand in (123.25) with respect
to \(z\) is bounded by

\[
 {L\over D}
 \left(1+{|z-rd|\over C\Delta}\right)^{-A}.
\tag{123.28}
\]

For each nonzero integer product \(m=rd\), the number of active odd
divisors is \(O_\varepsilon(X^\varepsilon)\). The product \(m=0\) is a
rapid tail and is bounded directly. A dyadic layer cake in
\(|z-m|/\Delta\) therefore gives

\[
 \sum_{r,d}{L\over D}
 \left(1+{|z-rd|\over C\Delta}\right)^{-A}
 \ll_\varepsilon {L\over D}\Delta X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\tag{123.29}
\]

Integrating (123.29) from \(X\) to \(M\) proves (123.1). This argument
charges every tied product, support edge, and rapid tail; multiplying a
single pointwise perturbation by a post-cancellation capacity is not used.

For (123.2), choose \(2^t\leq X^{1/4}<2^{t+1}\) and the nearest odd
integer \(M_0\) to \(X/2^t\). Odd multiples of \(2^t\) are spaced by
\(2^{t+1}\), so \(|M-X|\leq2^t=Q\) and \(v_2(M)=t\). Equation (123.1)
then gives the claimed target-safe cost.

### 3.2 Literal Gram and smooth alias localization

The supports in (123.11) put every active \(k\) in one interval of
length \(O(K)\), with \(k\asymp K\). Hence
\(\sum 1/k=O(1)\), proving (123.15). On a nondegenerate interior cell,

\[
 \mathcal K_M(r,r)=\sum_k {|q_{r,k}|^2\over k}\asymp1,
\tag{123.30}
\]

so the diagonal of (123.16) is \(\asymp R\). The Gram is real and
nonnegative only after every ordered pair is assembled. Taking moduli of
the diagonal and off-diagonal separately cannot prove its square target.

For fixed \(r,s\), the exact overlap amplitude in (123.17) has support
length \(O(K)\), supremum \(O(K^{-1})\), and \(m\)-th finite difference
\(O_m(K^{-m-1})\). Repeated discrete summation by parts gives

\[
 |\mathcal K_M(r,s)|\ll_A
 \left(1+K\left\|M\left({1\over r}-{1\over s}\right)\right\|\right)^{-A}.
\tag{123.31}
\]

No rectangular alias cutoff has been inserted.

Put

\[
 \theta_{r,s}=M\left({1\over r}-{1\over s}\right)
 ={M(s-r)\over rs}.
\tag{123.32}
\]

Because \(r,s\) are odd and \(s-r\) is even, \(\theta_{r,s}\) cannot be
a nonintegral half-integer. Thus there is a unique nearest integer \(j\).
Define

\[
 E=M(s-r)-jrs.
\tag{123.33}
\]

Then

\[
 \theta_{r,s}=j+{E\over rs},\qquad |E|< {rs\over2},
\tag{123.34}
\]

and (123.31) becomes

\[
 |\mathcal K_M(r,s)|\ll_A
 \left(1+{L|E|\over CX}\right)^{-A}.
\tag{123.35}
\]

Also \(|j|\ll D\). Thus the effective near-defect window is
\(|E|\ll X^{1+\rho}/L\) for any fixed localization slack \(\rho>0\);
the complement is \(O(X^{-B})\) after summing all \(O(R^2)\) pairs and
choosing \(A\) sufficiently large.

### 3.3 Exact factor coordinates and all congruence branches

For \(j\ne0\), set

\[
 u=M-jr,\qquad v=M+js.
\tag{123.36}
\]

Direct multiplication gives

\[
 \boxed{\quad uv-M^2=jE.\quad}
\tag{123.37}
\]

Oddness of \(r,s\) gives the stronger congruences

\[
 u\equiv v\equiv M-j\pmod {2|j|}.
\tag{123.38}
\]

Conversely,

\[
 r={M-u\over j},\qquad s={v-M\over j},
\tag{123.39}
\]

so (123.38), the positive support ranges, and the nearest-alias condition
make (123.36) a bijection. In the localized window,

\[
 u={Mr\over s}+{E\over s}\asymp X,\qquad
 v={Ms\over r}-{E\over r}\asymp X,
 \tag{123.40}
\]

so both factors are positive. If \(j>0\), then \(u<M<v\); if \(j<0\),
then \(v<M<u\). Negative aliases therefore reverse the factor
orientation; they do not create negative factors in the effective
annulus.

The literal unshifted factor-coordinate kernel is

\[
 \begin{aligned}
 \mathcal K_{j}(u,v)
  =\sum_k&{1\over k}
 q_L\!\left({4Xkj^2\over(M-u)^2}\right)
 \overline{q_L\!\left({4Xkj^2\over(v-M)^2}\right)}\\
 &\times e\!\left(
 {kj(uv-M^2)\over(M-u)(v-M)}\right),
 \end{aligned}
\tag{123.41}
\]

multiplied by

\[
 W\!\left({Xj\over D(M-u)}\right)
 \overline{W\!\left({Xj\over D(v-M)}\right)}.
\tag{123.42}
\]

These are the literal sampled amplitudes; neither \(q_L\) factor is
replaced by its value at a common centre.

Now write \(M=2^tM_0\), with \(M_0\) odd. From (123.33),

\[
 jrs+E=M(s-r),
\tag{123.43}
\]

and hence

\[
 {jrs+E\over2^{t+1}}=M_0{s-r\over2}\in\mathbb Z.
\tag{123.44}
\]

Since \(M_0\) is odd,

\[
 \boxed{\quad
 \chi _4(r)\chi _4(s)
 =(-1)^{(s-r)/2}
 =(-1)^{(jrs+E)/2^{t+1}}.
 \quad}
\tag{123.45}
\]

All valuation branches are therefore:

\[
 \begin{cases}
 v_2(E)=v_2(j),&j\ne0,\ v_2(j)<t+1,\\
 2^{t+1}\mid E,&j\ne0,\ 2^{t+1}\mid j,\\
 2^{t+1}\mid E,&j=0.
 \end{cases}
\tag{123.46}
\]

In particular \(E\equiv j\pmod2\). If \(E=0\) and \(j\ne0\), then
\(2^{t+1}\mid j\) and (123.3) follows. If \(j=0\), then

\[
 E=M(s-r),\qquad
 \chi _4(r)\chi _4(s)=(-1)^{E/2^{t+1}}.
\tag{123.47}
\]

The factor map collapses to \(u=v=M\) on this whole zero-alias sector,
so it is not invertible there.

The sign also has the factor-coordinate form

\[
 \chi _4(r)\chi _4(s)
 =(-1)^{(u+v-2M)/(2j)},
\tag{123.48}
\]

where the exponent is integral by (123.38). Swapping \(r,s\) sends

\[
 (j,E,u,v)\longmapsto(-j,-E,v,u).
\tag{123.49}
\]

The character sign is unchanged and the analytic kernel is conjugated.
Thus positive and negative aliases contribute twice a real part; there is
no cancellation forced by alias orientation. Positive and negative
defects \(E\) are both retained in the annulus.

For \(E=0\), \(j\ne0\), (123.37) gives \(uv=M^2\). Once
\(u\mid M^2\) is fixed, \(v\) is fixed. The permissible \(j\)'s divide
\(\gcd(|M-u|,|v-M|)\). Excluding \(u=v=M\), this gcd is nonzero, and
the number of signed \(j\)'s is at most twice its divisor count. Hence
\[
 2\tau(M^2)\max_{1\leq n\ll X}\tau(n)
 \ll_\varepsilon X^\varepsilon,
\tag{123.50a}
\]
after splitting the arbitrary epsilon between the two divisor bounds.
Each unshifted kernel and each shifted pair kernel is \(O(1)\), proving
the stated total exact-collision bound. The fixed point \(u=v=M\) is
precisely \(j=E=0\) and
corresponds to all diagonal pairs before the collapsed map; it must not be
counted by this divisor argument.

For the engineered centre (123.2), formulas (123.44)--(123.46) hold with
\(2^{t+1}=2Q\). Thus exact aliases require \(2Q\mid j\), while for
\(v_2(j)<t+1\) one has \(v_2(E)=v_2(j)\). This creates no thinning of the
near rows: every original ordered pair defines exactly one \(E\) obeying
that congruence, and (123.39) recovers the pair. Moreover

\[
 (-1)^{(jrs+E)/(2Q)}
 =(-1)^{M_0(s-r)/2}
 =\chi _4(r)\chi _4(s).
\tag{123.50}
\]

The engineered parity is therefore the original mod-four character in
new coordinates. It removes some already harmless exact aliases, but it
does not by itself cancel a near-defect sum.

### 3.4 Shifted Fejér Gram, zero-alias gain, and inverse theorem

Every \(c_k\) occurs in exactly \(H\) of the blocks in (123.20). Cauchy
therefore gives (123.21), while direct expansion gives the exact identity

\[
 \sum_n\left|\sum_{a=0}^{H-1}c_{n+a}\right|^2
 =\sum_{|h|<H}(H-|h|)\sum_k c_{k+h}\overline{c_k},
\tag{123.51}
\]

which proves (123.24) with every shifted support boundary retained.

Put

\[
 \psi_H(x)=\min\left(1,{1\over H\|x\|}\right).
\tag{123.52}
\]

Smoothness of the literal sampled amplitude gives, for every \(m\geq0\),

\[
 |\Delta_n^m A^{(H)}_{r,n}|
 \ll_m {H\over K^{m+1}}\psi_H(M/r).
\tag{123.53}
\]

Abel summation in \(a\) proves the factor \(\psi_H\); finite differences
in \(n\) preserve it because the support collars vanish smoothly. A
second summation by parts in \(n\) gives the simultaneous two-selector
bound

\[
 |\Gamma_{M,H}(r,s)|\ll_A
 \psi_H(M/r)\psi_H(M/s)
 \left(1+K\left\|M\left({1\over r}-{1\over s}\right)\right\|\right)^{-A}.
\tag{123.54}
\]

Indeed, the \(m\)-th finite difference of the product amplitude in
(123.22) is
\[
 O_m\!\left({H^2\over K^{m+2}}
 \psi_H(M/r)\psi_H(M/s)\right).
\tag{123.54a}
\]
There are \(O(K)\) values of \(n\), and the prefactor in (123.22) is
\(O(K/H^2)\); hence the zero-difference scale is exactly the product of
the two selectors. Repeated finite differences then supply the last
factor in (123.54), with no omitted \(K/H\).

This charges the shifted \(q_{r,k+h}q_{s,k}\) overlap rather than
silently replacing it by the unshifted amplitude.

For \(0<\zeta\leq1/2\), the product-level argument gives

\[
 \#\{r\asymp R:r\ {\rm odd},\ \|M/r\|\leq\zeta\}
 \ll_\varepsilon(1+\zeta R)X^\varepsilon.
\tag{123.55}
\]

Indeed, \(d\) nearest \(M/r\) gives
\(|M-rd|\ll\zeta R\), and every product level has at most
\(O_\varepsilon(X^\varepsilon)\) active divisor orientations. Dyadic
layering in (123.55) yields

\[
 \sum_{r\asymp R}\psi_H(M/r)^2
 \ll_\varepsilon (1+R/H)X^\varepsilon.
\tag{123.56}
\]

The complete \(r=s\) contribution in (123.20), including every
\(h\ne0\) shifted self-correlation, is bounded by (123.56). This is the
correct diagonal audit; retaining only the \(h=0\) term would be
insufficient.

More is true. In the nearest-alias sector \(j=0\), write \(s-r=2m\).
On the common support,

\[
 K\left|M\left({1\over r}-{1\over s}\right)\right|
 \asymp L|m|.
\tag{123.57}
\]

By (123.54), Cauchy in \(r\), and (123.56),

\[
 \begin{aligned}
 \sum_{\substack{r,s\ {\rm odd}\\j(r,s)=0}}
 |\Gamma_{M,H}(r,s)|
 &\ll_A\sum_m(1+L|m|)^{-A}
 \sum_r\psi_H(M/r)\psi_H(M/(r+2m))\\
 &\ll_\varepsilon {R\over H}X^\varepsilon.
 \end{aligned}
\tag{123.58}
\]

This proves (123.5) at \(H=H_0\), even when \(L\asymp1\).

The ratio

\[
 {K\over H_0}\asymp {X^{1/2}L\over D}>1
\tag{123.59}
\]

in the strict range; on the literal UNBAL component \(K/L>16\), it is
uniformly separated from one. Hence all shifted blocks used above fit
inside the sampled \(k\)-scale.

To prove the inverse assertion, decompose the real quantity
\(\mathcal F_{M,H_0}\) into: the full \(j=0\) sector; nonzero exact
aliases; the rapid tail outside (123.7); and the remaining signed
near-defect sector. Equations (123.35), (123.58), and the divisor count
show that the first three pieces have total modulus
\(O_\varepsilon(X^{1/2+\varepsilon})\). Equations (123.1) and (123.21)
then show that (123.6) forces the remaining real signed aggregate to have
size \(\gg X^{1/2+2\eta}\), after choosing the bookkeeping epsilon and
localization slack smaller than \(\eta\). This proves (123.7).

### 3.5 Capacity and return-map audit

The \(h=0,r=s\) term of (123.51), after its exact prefactor, has size
\(R/H\); (123.58) shows that all zero aliases have the same safe scale.
The reciprocal selector has density \(1/H\), while the \(n\)-alias
selector has density \(1/K\). The resulting flat-density pair ledger is

\[
 {R^2\over HK}
 =\left({R\over K}\right)^2{K\over H}
 =\left({D\over L}\right)^2{K\over H},
\tag{123.60}
\]

which is (123.8). This is the optimistic geometric capacity; proving a
uniform arithmetic upper bound of this exact order for the thin
factor-congruence annuli would already require an additional spacing
theorem. No conclusion here treats (123.60) as a proved estimate.

At \(H=H_0\), (123.60) is

\[
 X^{1/2}{D\over L},
\tag{123.61}
\]

so an actual-sign factor \(D/L\) is still required at the energy level.
Increasing \(H\) decreases (123.60), but its minimum for \(H\leq K\) is

\[
 \left({D\over L}\right)^2
\tag{123.62}
\]

at \(H\asymp K\), exactly the square of the Round-118 product-window
capacity. At that length a Fejér block spans the full \(k\)-row; the
construction no longer isolates a shorter reciprocal selector and is a
capacity self-return. For \(H<K\), it is a stronger sufficient norm by
the factor \(K/H\) in energy.

The same return appears in factor coordinates. Summing all congruent
\((u,v)\) and applying (123.39) recovers every original ordered pair.
Completing \(uv\) to an unrestricted divisor coefficient deletes the
two literal profiles and is unlawful; exact \(k\)-Poisson instead returns
the Round-118 prescribed-centre product wave. Thus the strict result is
the safe \(j=0\) package and the inverse localization, while the complete
nonzero near-defect sum is a self-return unless a new signed inequality is
inserted.

## 4. First doubtful or unproved step

The first unproved analytic step is

\[
 \boxed{\quad
 \mathfrak V_{M,H_0}:=
 \sum_{\substack{r,s\ {\rm odd}\\
                   j(r,s)\ne0,\ E(r,s)\ne0\\
                   |E(r,s)|\leq X^{1+\rho}/L}}
 \chi _4(r)\chi _4(s)\Gamma_{M,H_0}(r,s)
 \ll_\varepsilon X^{1/2+\varepsilon}.
 \quad}
\tag{123.63}
\]

In factor coordinates, (123.63) is the sum over \(j\ne0\) and
\((u,v)\) satisfying

\[
 uv-M^2=jE,\qquad
 u\equiv v\equiv M-j\pmod{2|j|},
\tag{123.64}
\]

the support and orientation conditions in (123.39)--(123.42), the
nearest-alias condition, \(E\ne0\), and the character multiplier

\[
 (-1)^{(u+v-2M)/(2j)}
 =(-1)^{(jrs+E)/2^{t+1}}.
\tag{123.65}
\]

Every positive and negative \(j,E\), every ordered conjugate, and every
literal shifted \(q_L\) overlap must remain inside the same real sum.

Neither the divisor factorization nor (123.45) proves (123.63). For
fixed \(j,r\), successive odd \(s\)'s change \(E\) by
\(2(M-jr)\asymp X\), while the effective defect interval has length
\(X/L\leq X\). There is generally no pair of adjacent terms inside one
local defect interval on which the alternating character can be summed.
Across factors, the amplitudes form a thin, congruence-restricted divisor
set and have no established bounded variation in \(E\). The engineered
large \(2\)-power changes the displayed modulus but not this fact.

The nominal capacity (123.61) says that the missing signed gain at
\(H_0\) is exactly \(D/L\). At \(H=K\), (123.63) collapses to the
original scalar capacity and asks for the original Round-118 gain. A
proof must therefore be a genuinely noninvertible signed estimate for
the complete thin annulus, or a stronger inverse theorem describing all
large values of (123.63). Another aliaswise modulus, parity-class norm,
full-divisor completion, or coefficient-preserving transform does not
address this first gap.

## 5. Required control tests and outcomes

| Control | Exact test | Outcome |
|---|---|---|
| `literal_Round118_flat_wave` | Use (123.11)--(123.13), retaining both literal sampled profiles, support overlaps, entries, exits, and the accepted flat-smooth normalization. | Pass. No rectangular \(r,k\) amplitude is substituted. |
| `phase_integerization_physical_kernel` | Compare (123.25) along the continuous centre segment, use (123.27), and count product levels at each intermediate centre. | Pass: cost \(O_\varepsilon((1+|M-X|)X^\varepsilon)\); floor cost is \(O(X^\varepsilon)\), and engineered-\(Q\) cost is target-safe. The denominator stays \(4X\). |
| `weighted_Gram_normalization` | Apply Cauchy with weights \(1/k\) as in (123.15), then expand all ordered pairs. | Pass. The square target is \(X^{1/2+\varepsilon}\), with no lost \(K\)-factor. |
| `diagonal_capacity` | Evaluate (123.30). For the shifted form, include all \(h\), use (123.53)--(123.56), not only \(h=0\). | Unshifted diagonal is \(\asymp R>X^{1/2}\), so that Gram is overstrong. The complete shifted diagonal is \(O(R/H)\) and is target-safe at \(H_0\). |
| `smooth_alias_localization` | Repeated finite-difference summation on the literal overlap amplitudes in (123.17) and (123.22). | Pass: (123.31), (123.35), and (123.54). No hard alias cutoff is asserted. |
| `alias_product_factorization` | Use (123.33), (123.36), and multiply directly. Audit the inverse and odd congruences. | Pass: \(uv-M^2=jE\), (123.38)--(123.42). The map is bijective for \(j\ne0\) and collapses for \(j=0\). |
| `two_adic_character_sign` | Write \(M=2^tM_0\), divide \(jrs+E=M(s-r)\) by \(2^{t+1}\), and compare parity with \((s-r)/2\). | Pass: (123.45)--(123.50), including every valuation branch. It is an exact re-expression of the original character, not a cancellation estimate. |
| `exact_versus_near_collision` | Separate \(E=0\) from \(0<|E|\ll X^{1+\rho}/L\). Count nonzero exact factors of \(M^2\). | Pass: nonzero exact aliases have \(O_\varepsilon(X^\varepsilon)\) total contribution. The diagonal fixed point is separate. Near aliases remain open. |
| `zero_and_negative_aliases` | Treat \(j=0\) before factorization; under swapping use (123.49). | Pass: the full zero-alias sector is target-safe in the \(H_0\)-shifted Gram. Negative aliases are conjugate orientations with the same sign and do not cancel automatically. |
| `signed_offdiagonal_aggregation` | Keep the complete real sum (123.63), without aliaswise or valuationwise absolute values. | Open. The power-excess inverse theorem forces every large row into this exact aggregate, but does not estimate it. |
| Shifted-\(k\) refinement | Use the exact Fejér prefactor and \(q_{r,k+h}q_{s,k}\) overlap in (123.24); compare \(H_0\) and \(K\). | Strict safe subpackage at \(H_0\): all \(j=0\). No complete gain: nominal capacity is \(X^{1/2}D/L\); at \(H=K\) it returns to \((D/L)^2\). |
| Engineered \(2\)-adic centre | Choose (123.2), charge (123.1), and impose the exact \(2Q\) congruence. | Phase cost passes. Exact aliases thin further, but they were already safe. Near-defect sparsity and sign cancellation do not follow because the congruence is automatic under the inverse map. |
| `old_transform_return` | Sum factor coordinates by (123.39), or apply exact \(k\)-Poisson to the full row. | Scoped fail as a new mechanism: the ordered-pair Gram or the Round-118 prescribed-centre product wave is reconstructed. |
| `owner_and_downstream_scope` | Compare hypotheses with the physical one-count M2 assembly. | Flat-smooth only. No implication to endpoint, hard, sharp, clipped, starred, arithmetic, transition, BAL, TOP, complete UNBAL, M9-M2, M9, uniformity, or the quarter theorem. |

All controls are analytic. No numerical computation, web source, or
external theorem is used.

## 6. Dependencies and exact artifacts used

This report used exactly the context assigned in the brief:

1. `protocol.md`, for graph authority, signed/unsigned separation, scope,
   and the seven-section report contract;
2. `state/proof_obligations.yml`, for the open unbalanced three-quarter
   parent, the accepted fixed-centre return, the Round-118 envelope and
   coherent-sector no-go, and downstream nonimplications;
3. `state/active_campaign.yml`, for the frozen Round-123 formula, task
   distinctions, controls, and promotion gate;
4. `strategy/conductor_0821_full_proof_strategy.md`, for the Round-118
   survivor, the prohibition on another invertible return, and the
   Round-122 rotation back to the mandatory M2 conjunction;
5. `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md`,
   for the accepted physical \(h\)-process/\(k\)-Poisson normalization,
   product-window width, and fixed-centre self-return;
6. `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`,
   for the certified envelope, coherent controls, and smallest complete
   joint-row survivor;
7. `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/reports/literal_unbalanced_wave_attack.md`,
   for the literal \(q_L,W\) amplitudes, product-level layer cake,
   reciprocal curvature normalization, and owner exclusions; and
8. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/derivation_packet.md`,
   for the candidate integerization, weighted Gram, alias definitions,
   factor identity, and proposed two-adic sign.

The added inputs are only the fundamental theorem of calculus in the
physical centre, elementary divisor bounds, exact finite Fejér blocking,
Abel summation, and repeated finite-difference summation by parts. No
sibling Round-123 report, candidate, review, shared synthesis, validation
file, conductor file, web source, or computation was read.

## 7. Recommended state effect

**Promote after independent seam review** the centre-perturbation lemma
(123.1), explicitly with amplitudes frozen at \(X\), physical denominator
\(4X\), and linear cost in \(|M-X|\). Record both the floor-\(N\) case and
the target-safe engineered centre (123.2).

**Promote after seam review** the exact Gram/factor package
(123.15)--(123.50): literal overlap amplitudes, unique nearest alias, the
product identity and inverse congruences, all two-adic branches, the
orientation of negative aliases, and the \(O_\varepsilon(X^\varepsilon)\)
nonzero exact-alias bound. Record that the factor map degenerates at
\(j=0\).

**Promote after seam review** the shifted-Fejér strict subpackage
(123.51)--(123.58) and the power-excess inverse theorem: at
\(H_0\asymp X^{1/2}/D\), the entire zero-alias sector is square-target
safe, and any \(X^{1/4+\eta}\) violation forces a comparably large actual
signed nonzero near-defect aggregate (123.63).

**Retain open** the flat-smooth quarter estimate and
`M9-M2-smooth-unbalanced-three-quarter-estimate`. The smallest remaining
object is (123.63), equivalently its exact factor-coordinate form
(123.64)--(123.65), with all positive and negative aliases and defects
aggregated before any modulus.

**Reject as standalone mechanisms** the unshifted positive Gram, use of
only its diagonal, automatic cancellation from the parity lock, automatic
near-defect sparsity from an engineered \(2\)-power, cancellation between
negative and positive aliases, aliaswise or valuationwise absolute values,
and unrestricted completion of \(uv\) to a full divisor coefficient.
Distinguish the genuine \(j=0\) safe subpackage from the \(H\asymp K\)
Fejér capacity self-return.

**No change** is licensed for hard TOP, BAL, complete UNBAL, M9-M2,
M9-M1, endpoint uniformity, M9, the certified internal \(1/3\) exponent,
the audited external exponent, or the Gauss-circle quarter target.

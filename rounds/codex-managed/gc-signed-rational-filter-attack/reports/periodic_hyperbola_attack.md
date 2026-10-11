# Round 207: complete periodic hyperbola formula and signed reciprocal estimate

Campaign: `gc-signed-rational-filter-attack`. Task: `periodic_hyperbola_attack`.
Role: discovery, selected context; candidate evidence only. Date: 2026-09-27.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: 100 percent analytical/algebraic; no mathematical numerical experiment.

## 1. Result: complete signed estimate, with no moment gain

The actual centered filter has the complete two-arm rational expansion
(P8) below. The quotient arm has the exact Gauss factor
`2 i chi4(k)` in this report's `e(-kx/q)` convention. Both the factor
four in the divisor formula and the quotient arm's period `4 ell` are
retained. Short periods vanish before any norm is taken.

Freezing the quotient threshold from `m>D ell` to `x>D ell` has error

\[
 \sup_{x\in J}|B_N(x)|\ll1,\qquad
 \int_J|B_N(x)|^6dx\ll TH,\qquad H=T/\sqrt N.                 \tag{P1}
\]

There is a stronger explicit formula (P6) for its boundary spikes; in
particular the error is rapidly small when the prescribed cutoff D is
even. No change to the prescribed cutoff is made here.

All coincident fractions can be grouped exactly. First-arm reduced
denominators are odd; quotient-arm reduced denominators are divisible
by four. Thus the two arms have no exact nonzero rational coincidence.
They still have near coincidences and mixed sixth-moment terms, and
neither arm is deleted. Within each arm the repeated fractions remain
as explicit partial character sums in (P9)--(P10).

A genuine signed estimate is then proved, rather than stopping at the
transform. The two reciprocal sums, with all harmonics and the moving
interval mask, obey

\[
 |Z_N(x)|\ll T^{1/2}N^{1/4}\log(2T)+O(1)\quad(x\in J).       \tag{P2}
\]

The proof uses the exact additive decomposition of `chi4(d)` followed
by an elementary second-derivative argument, proved below. It improves
the `O(T)` bound obtained by taking absolute values of every rational
Fourier coefficient. Its physical normalization, however, recovers
only the already available original-coefficient supremum.

Combining (P2) with the valid complete second moment gives only

\[
 K_6(N):=\int_J|Z_N(x)|^6dx
       \ll_\epsilon T^{5+\epsilon}N^{1/2},                  \tag{P3}
\]

which is insufficient at every middle scale. Even retaining all the
other available suprema in that interpolation does not meet the
sufficient threshold. The stronger inherited bound
`K6(N) << T^(5+epsilon) N^(-29/110)` remains the best one used here;
it also misses the target by the full positive profile (P19).

This is a completed, quantitatively insufficient signed reciprocal-sum
attempt. It is not an impossibility theorem for all signed methods,
and it supplies no lower bound for the actual signed sixth moment.
The complete middle twelfth-moment exponent remains `10 beta`.

## 2. Exact statement and hypotheses

Let T be real and sufficiently large, put X=T^2, and set

\[
 I=[T/\sqrt2,\sqrt3T],\quad J=[X/2,3X],\quad
 T^{52/125}<N=2^j<T^{99/125},\quad h(x)=2\sqrt x/\sqrt N.
\]

Every strict middle dyadic block is retained. Equality at a dividing
boundary belongs to the already estimated outer bands. Write
H=T/sqrt(N), so h is between fixed positive multiples of H on J,
`T^(151/250)<H<T^(99/125)`, and `T/H=sqrt(N)` tends to infinity.

Use precisely the fixed radial mollifier transform Psi and the smooth
partition v of the reviewed Round205 interface. With

\[
 A_{N,T}(t)=t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2),\qquad
 F(u)=-\int_1^2A_{N,T}(t)\sin(2\pi tu)\,dt,
\]

define

\[
 Z_N(x)=\sum_{m\ge1}(r_2(m)-\pi)F((m-x)/h(x)).                \tag{P4}
\]

The filter is real, odd and Schwartz. Its seminorms are uniform in the
complete middle band. With `e(t)=exp(2 pi i t)` and
`Fhat(xi)=integral F(u)e(-u xi)du`,

\[
 \widehat F(\xi)=\frac i2\operatorname{sgn}(\xi)
                      A_{N,T}(|\xi|),
 \qquad\operatorname{supp}\widehat F\subset[-2,-1]\cup[1,2].
\]

The amplitude vanishes smoothly at the support endpoints. There is no
zero-frequency term. An opposite orientation of the spatial kernel
reverses the Fourier phase and the displayed quotient Gauss sign;
the convention here is fixed throughout.

Choose the inherited fixed smooth localization eta supported in
[1/4,6] and equal to one on [1/3,4]. Set
`M=ceil(6X)`, `D=floor(sqrt(M))`, and `L=floor(M/(D+1))`.
Thus D and L are comparable to T. All rational formula errors below
are uniform on J, also for real T, real x, integer centers, and
`x=D ell`.

Write `N=T^alpha`, `beta=2 theta_LY-1/2`, and

\[
 W_0=\min(N^{1/4},T^\beta,T^{1/2}N^{-1/2}),\qquad
 \omega(\alpha)=\min(\alpha/4,\beta,(1-\alpha)/2).
\]

The accepted repaired external dependency gives
`1/8<beta<27/208`. The sufficient input being tested, and not assumed,
is

\[
 K_6(N)\ll_\epsilon T^{129/25-6\omega(\alpha)+\epsilon}.       \tag{P5}
\]

This is sufficient through the inherited supremum-times-sixth
certificate; it is not necessary for the desired twelfth moment.

## 3. Proof and complete derivation

### Localization and the actual two-arm identity

The assigned Round206 report proves, with the present kernel
orientation,

\[
 S_N(R)=R^{-1/2}Z_N(R^2)
       +O_\epsilon(T^{-1/2+\epsilon}N^{-1})+O_K(T^{-K}).
\]

The error includes the original curved-shell linearization, all remote
tails, and the constant-density subtraction. For completeness, the
constant-density cancellation follows directly from
`sum_(m in Z) F((m-x)/h)=h sum_k Fhat(hk)e(-kx)=0` for h>2.
The nonpositive-integer tail is rapidly small. The same Schwartz
estimate shows that insertion of eta(m/X) changes Z_N by `O_K(T^-K)`:
where eta differs from one, `|m-x|` is at least a fixed multiple of X,
and `r2(m)<<_epsilon m^epsilon`. Arbitrarily high fixed decay sums the
entire infinite tail; it is not discarded by declaring compact support.

For every positive integer m<=M the exact hyperbola identity is

\[
 \frac{r_2(m)}4
 =\sum_{d\le D}\chi_4(d)\mathbf1_{d\mid m}
 +\sum_{\ell\le L}\mathbf1_{m>D\ell}\mathbf1_{\ell\mid m}
                                      \chi_4(m/\ell).
\]

The first arm contains the divisor d=D. The second is precisely d>D,
so its threshold is strict. The quotient atom is
`1_(m=ell mod 4ell)-1_(m=3ell mod 4ell)`; even quotients vanish.
One can either keep the centered small-divisor constants and the
`O(1/D)` mean remainder from the inherited identity, or first sum the
constant density. Every such constant is annihilated by the complete
filter, up to the already paid localization tail.

Remove eta from each of the finitely many complete progression sums,
at a rapidly small total cost. For example, the number of divisor
labels is O(T), their absolute coefficients are bounded, and the
removed region has distance at least cX from x. The lattice Schwartz
sum for each label is bounded by
`C_A(1+h/q)(1+X/h)^(-A+1)`; summing over q and choosing A sufficiently
large proves the assertion. The same bound applies with a threshold
indicator, since that indicator has modulus at most one. The completed
progressions may therefore run over all integers, including
nonpositive integers, with their error explicitly paid.

### Freezing the thresholds, including the exact boundary term

Let

\[
 B_N(x)=4\sum_{\ell\le L}\sum_{j\in\mathbb Z}\chi_4(j)
   \bigl(\mathbf1_{\ell j>D\ell}-\mathbf1_{x>D\ell}\bigr)
                      F((\ell j-x)/h(x)).
\]

This is the exact difference between the completed moving and frozen
quotient arms. It is absolutely convergent. Its j=D term is
`-4 chi4(D) 1_(x>D ell) F((D ell-x)/h)`.

All j!=D terms are rapidly small after summing ell. To verify this
uniformly, first take ell<=cT with c fixed sufficiently small. Then
`D ell<=X/4`, whereas `x>=X/2`; every crossing term has
`|ell j-x|>=c'X`. The complete one-sided lattice tail is bounded by
`C_A(1+h/ell)(1+X/h)^(-A+1)`. Its sum over these ell is rapidly
small. For the remaining ell, `ell>=cT`. If x>D ell, the crossing
indices other than D obey j<=D-1 and have distance at least
`|x-D ell|+ell`. If x<=D ell, the crossing indices obey j>=D+1 and
have the same lower bound. Their lattice tails are bounded by an
arbitrarily high inverse power of `ell/h`, and
`ell/h>>T/H=sqrt(N)>>T^(26/125)`. The O(T) outer labels are harmless
after raising the fixed decay order. Hence, for every fixed K,

\[
 B_N(x)=-4\chi_4(D)\sum_{\ell\le L}\mathbf1_{x>D\ell}
                    F((D\ell-x)/h(x))+O_K(T^{-K}).           \tag{P6}
\]

Inserting eta(D ell/X) in the leading expression would change it
only by a rapidly small tail. Formula (P6) includes the equality case:
the indicator is zero when x=D ell, and F(0)=0 in either convention.
In particular, if D is even then chi4(D)=0 and B_N is rapidly small.

For arbitrary prescribed D, uniform decay gives

\[
 |B_N(x)|\le C_A\sum_{\ell\le L}
            (1+|x-D\ell|/H)^{-A}+O_K(T^{-K}).
\]

Because D/H tends to infinity, this sum is uniformly bounded. Put
`u_ell(x)=(1+|x-D ell|/H)^(-A)`. Then
`(sum u_ell)^6<=(sup sum u_ell)^5 sum u_ell`, and each integral
of u_ell over J is at most `C_A H`. There are O(T) labels, proving
(P1). The actual variable h(x) has never been replaced in an identity:
its comparison with H is used only in this absolute error bound.

### Periodic Poisson summation and exact mod-four phase

For any positive integer q and residue a, direct Poisson summation
in the progression gives

\[
 \sum_{m\equiv a\ (q)}F((m-x)/h)
   =\frac hq\sum_{k\in\mathbb Z}
           \widehat F(hk/q)e(k(a-x)/q).                    \tag{P7}
\]

For fixed x this follows by applying the ordinary Schwartz Poisson
identity to `F((a+qu-x)/h)`. No derivative in x or in h(x) is required.
Both sides converge absolutely; on the right only finitely many k
are nonzero. The zero harmonic vanishes. If q<h/2, all nonzero
`|hk/q|` exceed two, so the full progression is exactly annihilated.
At a support endpoint its smoothly vanishing amplitude is kept.

For the quotient arm, subtract the residues ell and 3ell modulo
4ell. Its finite Fourier factor is exactly

\[
 e(k/4)-e(3k/4)=2i\chi_4(k).
\]

Thus all even k vanish. Retaining every surviving harmonic, define

\[
 \begin{split}
 A_N(x)&=4h\sum_{d\le D}\frac{\chi_4(d)}d
            \sum_{k\ne0}\widehat F(hk/d)e(-kx/d),\\
 Q_N(x)&=2ih\sum_{\substack{\ell\le L\\D\ell<x}}\frac1\ell
            \sum_{k\ne0}\chi_4(k)\widehat F(hk/(4\ell))
                                           e(-kx/(4\ell)).
 \end{split}
\]

The complete formula is

\[
 \boxed{Z_N(x)=A_N(x)+Q_N(x)+B_N(x)+O_K(T^{-K}).}             \tag{P8}
\]

Here and in (P8)--(P10), h means its actual value h(x). First-arm
periods d<h/2 vanish. Quotient-arm periods 4ell<h/2 vanish. The
small-period conclusion does not bound the remaining long periods.
There is no `k=1 only` restriction: the first arm contains all
`|k|<=2D/h`, and the second all `|k|<=8L/h`, subject to their exact
support and mask. Both signs are present, with conjugate symmetry
giving real A_N and Q_N.

### Every duplicate rational frequency retained

Let `C(y)=sum_(1<=r<=y) chi4(r)/r`, with C(y)=0 for y<1.
Every first-arm d with nonzero character is odd. Writing k/d=a/b
in lowest terms therefore gives b odd, d=br, k=ar. Complete grouping
gives

\[
 A_N(x)=4h\sum_{\substack{1\le b\le D\\b\ {\rm odd}}}
      \frac{\chi_4(b)}b C(D/b)
      \sum_{\substack{a\in\mathbb Z\setminus\{0\}\\(a,b)=1}}
                  \widehat F(ha/b)e(-ax/b).                 \tag{P9}
\]

In the quotient arm, k is odd. After reduction its denominator b is
divisible by four and its numerator a is odd. The original labels are
`ell=br/4`, `k=ar`, where r is odd; its character is still explicitly
retained in the following sum:

\[
 C_{b,x}=\sum_{\substack{r\ge1\\br/4\le L\\Dbr/4<x}}
                         \frac{\chi_4(r)}r.
\]

Then

\[
 Q_N(x)=8ih\sum_{\substack{1\le b\le4L\\4\mid b}}
       \frac{C_{b,x}}b
       \sum_{\substack{a\in\mathbb Z\setminus\{0\}\\(a,b)=1}}
             \chi_4(a)\widehat F(ha/b)e(-ax/b).              \tag{P10}
\]

The strict inequality in C_(b,x) is essential at a moving endpoint.
In each formula only the Fourier support survives. These grouped
forms prove the parity separation of exact frequencies between arms.
They do not separate the two arms in a norm and do not remove any
near equality among sums of frequencies. In particular, exact
pairwise disjointness is not sixth-order orthogonality.

The actual duplicate sum C(y) is an alternating odd reciprocal sum.
For y>=1 it lies between 2/3 and 1, and
`C(y)=pi/4+O(1/y)`, by the elementary alternating-series remainder.
The nonempty C_(b,x) has the same description with its strict upper
cutoff. Thus duplicates are not annihilated by a fictitious zero
character mean. These facts are algebraic diagnostics here; no
positive majorant is substituted for the signed moment.

### A complete signed reciprocal-sum estimate

We use the following elementary second-derivative lemma. If f is
real and twice continuously differentiable on an interval of length
U (with a fixed one-unit enlargement), f'' has one sign, and
`c lambda<=|f''|<=C lambda`, then

\[
 \left|\sum_{n\in\mathbb Z\cap\mathcal I}e(f(n))\right|
       \ll_{c,C} U\sqrt\lambda+\lambda^{-1/2}+1.            \tag{P11}
\]

Here is an elementary proof sufficient for this use. For lambda
bounded below by a fixed positive constant, the trivial U+1 bound
implies (P11). Otherwise the successive phase differences
`f(n+1)-f(n)` are monotone, with increments comparable to lambda.
Split them at distance delta=sqrt(lambda) from integers. The bad
pieces contain at most
`O((U lambda+1)(delta/lambda+1))`
indices, which is `O(U sqrt(lambda)+lambda^(-1/2)+1)`. On each of
the remaining monotone pieces the phase differences stay within
one interval `[j+delta,j+1-delta]`. Summation by parts using
`e(f(n))=(e(f(n+1))-e(f(n)))/(e(f(n+1)-f(n))-1)` gives O(1/delta):
the endpoint factors and the variation of the reciprocal denominator
on that interval are O(1/delta). There are O(U lambda+1) pieces.
Their sum has the same asserted bound. This proves (P11), uniformly
for partial real-ended intervals. The reciprocal phases below also
have the required regularity on fixed enlargements; alternatively
one may remove a bounded number of boundary integers first.

We apply (P11) separately to every positive harmonic; the negative
harmonics are its conjugate contributions. For the first arm use
the exact character identity

\[
 \chi_4(d)=\frac{e(d/4)-e(-d/4)}{2i}.
\]

For fixed k>=1 its supported d lie in
`[hk/2,hk] intersect [1,D]`. The two phases are
`f_+(d)=d/4-kx/d` and `f_-(d)=-d/4-kx/d`.
Their second derivatives have constant sign and modulus comparable
to `lambda_k=x/(h^3 k^2)`. Their full ambient interval has length
O(hk), even if the cutoff leaves a shorter interval. The weight
`(4h/d)Fhat(hk/d)` has supremum and total variation O(1/k).
Indeed its argument stays in the fixed compact support, its
derivative is O(1/(h k^2)), and the interval length is O(hk).
Partial summation and (P11) therefore give the contribution bound

\[
 \ll \frac{\sqrt{x/h}}k+\frac{h^{3/2}}{\sqrt x}+\frac1k.
                                                                    \tag{P12}
\]

This calculation retains the mod-four character modulation in the
phase; it does not apply an unweighted estimate to unexplained
weighted coefficients. The periodic identity is what justifies the
two unweighted phase sums.

For the quotient arm, fix an odd k>=1. Its ell interval is

\[
 [hk/8,hk/4]\cap[1,L]\cap\{\ell:D\ell<x\}.
\]

It is a single possibly empty, partially truncated interval. Thus the
moving mask costs no additional intervals in this pointwise argument.
The phase `-kx/(4ell)` has second derivative of size comparable to
the same lambda_k, and the weight
`(2ih/ell)chi4(k)Fhat(hk/(4ell))`
has supremum and total variation O(1/k). At the truncated endpoint
partial summation pays the endpoint weight O(1/k). There is no
derivative in x, and no unpriced differentiation of the moving mask.
Consequently (P12) holds for this complete harmonic as well.

Both sums have at most `C T/h` nonzero positive harmonics. Summing
(P12), including every one of them, yields

\[
 |A_N(x)|+|Q_N(x)|
 \ll\sqrt{x/h}\log(2T/h)
        +(T/h)h^{3/2}/\sqrt x+\log(2T/h).
\]

Since x is comparable to T^2 and h is comparable to T/sqrt(N), this
is

\[
 \ll T^{1/2}N^{1/4}\log(2T)
       +T^{1/2}N^{-1/4}+\log(2T),                          \tag{P13}
\]

and (P1), (P8) prove (P2). Uniformity includes lambda_k above one,
where the elementary trivial branch of (P11) is the applicable one.
The actual width h(x) remains unchanged throughout.

For comparison, a termwise rational Fourier absolute bound gives
O(1) per divisor label: there are O(q/h) nonzero sampled harmonics
and each has size O(h/q), while q<h/2 vanishes. Its total is O(T).
Thus (P13) is a real cancellation estimate, improving that bound
throughout the entire middle band. It does not exploit correlations
between different k after those harmonic estimates are summed.

### Restoring the sixth and twelfth powers

Directly raising (P2) gives
`K6(N)<<_epsilon T^(5+epsilon)N^(3/2)`.
A more favorable valid use is to combine it with the complete ideal
second moment from the assigned Round206 ledger:

\[
 \int_J|Z_N(x)|^2dx\ll_\epsilon X^{1+\epsilon}H
                        \ll_\epsilon T^{3+\epsilon}N^{-1/2}.
\]

Then `(sup |Z_N|)^4 integral |Z_N|^2` proves (P3).
There is no inference of a Gaussian sixth moment from the variance.
The boundary term is included in this complete second moment and in
(P2); it could also be bounded separately by (P1).

The physical normalization and Jacobian are
`S_N(R)=R^(-1/2)Z_N(R^2)+error` and `dR=dx/(2sqrt(x))`.
Accordingly the sixth conversion costs exactly T^(-4). Combining
with the valid complete block supremum gives

\[
 \int_I|S_N(R)|^{12}dR
 \ll_\epsilon W_0^6T^{-4+\epsilon}K_6(N)
                          +O_\epsilon(T^{-2+\epsilon}).    \tag{P14}
\]

For the algebraic bridge error its sixth power, the length of I,
and `W_0^6<=N^(3/2)` give
`O(T^(-2+epsilon)N^(-9/2))`, smaller than the displayed error.
Rapid tails remain rapid under all fixed powers and O(log T)
dyadic recombination. The freezing error alone contributes at most

\[
 W_0^6T^{-4}\,TH
       \ll T^{-2}N\ll T^{-151/125},                        \tag{P15}
\]

apart from an arbitrary small epsilon loss. Thus threshold freezing
is decisively target-safe even for odd D; its even-D improvement
does not supply the missing arithmetic moment saving.

Substituting the signed bound (P3) into (P14) gives

\[
 \int_I|S_N|^{12}dR
       \ll_\epsilon T^{1+\epsilon}N^{1/2}W_0^6.             \tag{P16}
\]

The ratio of the upper certificate (P3) to the sufficient threshold
(P5) has exponent
`6 omega(alpha)+alpha/2-4/25`. This is positive everywhere:
on the first piece it is `2 alpha-4/25`, at least `84/125`;
on the middle piece it is `6 beta+alpha/2-4/25`, positive already
at alpha=4 beta; and on the final piece it is
`71/25-(5/2)alpha`, at least `43/50` at alpha=99/125.
These comparisons concern insufficient upper certificates, not lower
bounds on the moment.

Retaining all already known pointwise bounds means using
`sup |Z_N|<<_epsilon T^(1/2+epsilon)W_0` instead of just (P2).
The same second-moment interpolation becomes

\[
 K_6(N)\ll_\epsilon T^{5+\epsilon}N^{-1/2}W_0^4,
 \qquad
 \int_I|S_N|^{12}dR
       \ll_\epsilon T^{1+\epsilon}N^{-1/2}W_0^{10}.         \tag{P17}
\]

Its loss over (P5) is `10 omega-alpha/2-4/25`, piecewise

\[
 2\alpha-4/25,\qquad
 10\beta-\alpha/2-4/25,\qquad
 121/25-11\alpha/2.
\]

It remains at least a fixed positive power on the entire middle
interval; the final endpoint value is `121/250`, and the other
pieces are larger. Therefore the signed estimate and the available
second moment do not produce the requested sixth bound, even with
the other valid suprema restored.

Finally retain the sharper inherited sixth bound, obtained by
intersecting the complete second-moment level bound with the accepted
large-value distribution:

\[
 K_6(N)\ll_\epsilon T^{5+\epsilon}N^{-29/110}.               \tag{P18}
\]

The still-required saving relative to (P18) is exactly

\[
 g(\alpha)=6\omega(\alpha)-4/25-(29/110)\alpha>0             \tag{P19}
\]

at every middle scale. At the two outer endpoints its values are
`2436/6875` and `3509/13750`; its maximum occurs at `alpha=4 beta`.
Raising (P18) by the supremum and maximizing over every block gives
`1+(272/55)beta`, which is worse than the accepted complete exponent
`10 beta`. Hence the existing `T^(10 beta+epsilon)` twelfth bound
is retained. Minkowski over all middle blocks pays only a fixed
logarithmic power and retains every mixed block term. No proper
subrange has been left unestimated or promoted as the whole target.

## 4. First doubtful or unproved step

There is no unproved character cancellation in (P8)--(P13).
The first missing improvement is a sixth-order estimate for the
complete signed sum A_N+Q_N, with its actual variable-width
coefficients, strict quotient mask, duplicate-fraction character
sums, and all within-arm and mixed correlations, sufficient for
(P5). Formula (P1) makes the freezing error harmless for this purpose.

The independent second-derivative bounds for each harmonic, followed
by an absolute sum over k, stop at (P13). Recovering only the old
supremum cannot turn the already valid pair variance into the required
sixth saving. A proof that discards the quotient arm, treats the
partial character sums in (P9)--(P10) as zero, keeps only a fundamental
harmonic, or mistakes disjoint reduced denominators for orthogonality
of six-frequency sums would make an invalid step before this gap.

No no-go theorem is claimed for every reciprocal or bilinear method.
The result is the exact, fully priced failure of this specific signed
second-derivative plus norm-interpolation attempt to certify (P5).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `complete_middle_range` | PASS: all strict middle dyadic scales retained; all estimates uniform and outer equalities follow the inherited convention. |
| `actual_two_arm_characters` | PASS: exact r2/4 divisor identity; small-arm chi4(d), quotient chi4(k), both quotient residue classes, both Fourier signs, and factor four retained. |
| `all_harmonics_and_duplicates` | PASS: every supported harmonic remains in (P8); (P9)--(P10) exactly group all repeated fractions. Parity separation removes no mixed moment terms. |
| `moving_threshold_error` | PASS: strict masks, equality cases and j=D contribution give (P6); supremum O(1), sixth integral O(TH), and even-D rapid cancellation proved. |
| `low_period_annihilation` | PASS: follows from exact support in (P7), with full periods q=d and q=4ell; remaining long periods receive the signed estimate. |
| `variable_width` | PASS: actual h(x) in every identity; fixed H used only for uniform majorization, with no width-freezing error hidden. |
| `real_endpoints_and_tails` | PASS: all progression tails paid by Schwartz decay, real endpoints allowed, integer centers and strict hyperbola boundaries retained; partial reciprocal intervals handled in (P11). |
| `signed_not_positive` | PASS: the signed reciprocal estimate uses the actual mod-four modulation and oscillatory phases. It is an upper bound; no positive expression lower-bounds the signed sixth moment. |
| `restored_sixth_and_twelfth_powers` | PASS: (P14) has exactly T^(-4); (P15)--(P19) price boundary error, signed estimate, all suprema and the stronger retained sixth input. |
| `source_hypotheses` | PASS within inherited scope: no new external theorem is imported. The only new exponential-sum ingredient (P11) is proved internally; accepted Li--Yang and distribution inputs are used only in their inherited qualified forms. |
| `full_proof_scope` | PASS: no improvement to complete p12, pointwise theta, M1/M2 or the quarter theorem. Even the frozen milestone would imply only 102/325. |

The controls are analytical. This selected-context report is not a
substitute for the conductor's independent seam review or the isolated
statement-only task. No mathematical numerical experiment was performed.

## 6. Dependencies and exact artifacts used

Read the assigned brief first and only its permitted context:

- `rounds/codex-managed/gc-signed-rational-filter-attack/briefs/periodic_hyperbola_attack.md`.
- `protocol.md`.
- `state/proof_obligations.yml`: the open target, repaired Li--Yang dependency, accepted complete large-value bound, and the two separate exact/near-resonance scope barriers.
- `state/active_campaign.yml`, Round207.
- `strategy/round207_signed_rational_filter_attack.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/actual_divisor_shell_attack.md`: exact filter, curved/additive transfer, localization and actual hyperbola convention.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`: complete second moment, valid block suprema, sharper inherited sixth bound and sufficient threshold.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_divisor_obstruction_review.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`: exact fixed205 bands, shell identity and complete outside-band scope.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: accepted complete distribution/moment input and its coefficient-uniform limitation.

The conductor communicated the independently found denominator-parity
fact and boundary-spike form while this report was being developed;
both are independently derived above from the fixed exact formula.
No sibling artifact was read, no external theorem or web source was
imported, and no unlisted context file was consulted. This report is
selected-context discovery, never represented as statement-only blind.

## 7. Recommended state effect

**No change** to the accepted graph or proof draft. Retain the complete
two-arm identity, exact duplicate grouping, target-safe boundary
estimate, and fully priced signed reciprocal calculation as candidate
evidence subject to the conductor's seam checks.

Use the exit label `complete_rational_attempt_no_gain`. The demonstrated
failure belongs to the specified second-derivative/harmonic-summation
and norm-interpolation placement. Retain the complete middle-band
target and every parent obligation as open, with best complete p12
exponent `10 beta` and unchanged pointwise benchmark.

Only this assigned report was written. No graph, proof draft, validation
matrix, synthesis, source card, legacy artifact or successor file was
edited. The assigned task stops here.

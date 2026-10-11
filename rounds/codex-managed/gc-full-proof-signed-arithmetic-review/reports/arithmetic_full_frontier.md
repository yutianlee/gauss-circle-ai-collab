# Round 208: complete signed arithmetic and the full frontier

Campaign: `gc-full-proof-signed-arithmetic-review`. Task:
`arithmetic_full_frontier`. Role: source auditor, selected context.
Date: 2026-09-27. Starting graph SHA256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: 100 percent analysis, algebra and source
inspection; no mathematical numerical experiments. Only this report is
written. The conductor requested the fresh Xiao--Li source as the second
full interface, replacing a proposed repetition of the inherited
Matthiesen audit.

## 1. Result: a complete objective survives, but no source supplies its gain

Exact total-frequency aggregation is compatible with the actual rational
coefficients. It is not refuted by Round 207's termwise absolute-majorant
lower bound. With the actual variable width and moving prefix retained,
however, its integrated cubic Gram form is exactly the open sixth moment.
No primary theorem audited here proves that form at the required size.
Calling it a new energy estimate does not constitute an improvement.

The two fully costed interfaces are:

1. Blomer--Pascadi, Theorem 1.1: the inherited actual M1 completion has
   an applicable primitive/unit part, but its certified price remains
   `L^(119/32+epsilon)`, against target `L^2`. The complete rational
   filter does not yet have a theorem-compatible Kloosterman kernel or
   coefficient norm at all.
2. Xiao--Li, Theorem 1.1, submitted 21 September 2026: its shifts move
   a logarithmic divisor cutoff. They are not additive shifts of the
   argument of `r2`. Its coefficient, number of factors, smoothing and
   cutoff ranges do not match the present filter. Even a deliberately
   more generous, **unproved** six-point error with its logarithmic
   strength would miss the sufficient sixth target by at least
   `T^(136/125)` before logarithms throughout the middle range.

A fresh source exclusion matters: Jiseong Kim's
`2509.24152v4` was withdrawn on 10 September 2026. Its current primary
record explains that the stated assumptions generally give a result
weaker than Cauchy--Schwarz. It is not an available shifted-correlation
gain.

The quantitatively justified full-source objective remains actual
arithmetic high values of the **complete** mollified discrepancy, with
the complete middle-band sixth estimate below as one sufficient p=12
test. An attack on grouped cubic frequencies is reasonable only if it
targets a net bound, including every mask and near relation. Its first
unproved statement is that bound itself. The p=12 milestone gives only
`102/325`; the quarter theorem still requires a sufficient hierarchy of
arbitrarily high fixed moments or another complete route.

## 2. Exact statement, coefficients, scales and full scope

Write `e(t)=exp(2 pi i t)`, `X=T^2`, `N=T^alpha`, and

\[
 \frac{52}{125}<\alpha<\frac{99}{125},\qquad
 H=T/\sqrt N=X^{1/2-\alpha/4},\quad
 J=[X/2,3X],\quad h(x)=2\sqrt{x}/\sqrt N.
 \tag{208.A1}
\]

Thus `X^(151/500)<H<X^(99/250)`; fixed factors in `h` do not
alter these powers. The actual real odd Schwartz kernel is

\[
 K(u)=\int_1^2t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2)
              \sin(2\pi tu)\,dt,
 \qquad
 Z(x)=\sum_{m\ge1}(r_2(m)-\pi)K((x-m)/h(x)).
 \tag{208.A2}
\]

Its Fourier support is `[-2,-1] union [1,2]`, with uniform seminorms.
Take `M=ceil(6X)` and the even cutoff
`D=2 floor(floor(sqrt M)/2)`, `L=floor(M/(D+1))`.
Both are comparable to `sqrt X`. The exact divisor split and the
reviewed threshold control give `Z=A+B+O_A(X^-A)`. At a reduced
frequency `lambda=a/q`, the complete coefficient is

\[
 b_{a/q}(x)=h(x)\widehat K(h(x)a/q)\,c_{a/q}(x),
 \tag{208.A3}
\]

\[
 c_{a/q}(x)=
 \begin{cases}
 \displaystyle {4\chi_4(q)\over q}
       \sum_{j\le D/q}{\chi_4(j)\over j},&q\text{ odd},\\[2mm]
 \displaystyle {-8i\chi_4(a)\over q}
       \sum_{\substack{j\ge1\\qj/4\le L\\Dqj/4<x}}
          {\chi_4(j)\over j},&4\mid q,\\[2mm]
 0,&q\equiv2\pmod4.
 \end{cases}
 \tag{208.A4}
\]

Here `(a,q)=1`, `q>0`, both signs of a occur, and `q<=Q=max(D,4L)`.
There is no assumption that q is squarefree. The finite envelope is
`c/H<=|lambda|<=C/H`, and q is consequently at least a constant
times H. Zero frequencies vanish. The second line includes every
active quotient label, not a selected favorable prefix. The sign
`-8i` follows from the character transform `-2i chi4(k)`.

The reviewed complete variance and coefficient prices are

\[
 \int_J|Z|^2\ll X^{1+\epsilon}H,\qquad
 \sum_\lambda|b_\lambda(x)|\ll QX^\epsilon,\qquad
 \sum_\lambda|b_\lambda(x)|^2\ll HX^\epsilon.
 \tag{208.A5}
\]

The pointwise energy assertion follows directly from (A4); the
integrated variance additionally needs the reviewed multiplier and
prefix argument. It cannot be justified by treating moving
coefficients as constants. Choosing the original floor cutoff instead
adds the explicit threshold bump train, whose sixth integral is
`O(sqrt(X)H)` and is already safe.

Put

\[
 \theta={3292+25\sqrt{1717}\over13762},\quad
 \beta=2\theta-\tfrac12,\quad
 \omega(\alpha)=\min(\alpha/4,\beta,(1-\alpha)/2).
\]

The sufficient entire middle-range target is

\[
 K_6(N):=\int_J|Z(x)|^6dx
 \ll_\epsilon T^{129/25-6\omega(\alpha)+\epsilon}
 \quad\text{for every middle }N.
 \tag{208.A6}
\]

The retained complete bound is
`K6(N)<<T^(5+epsilon)N^(-29/110)`. Its required saving is

\[
 g(\alpha)=6\omega(\alpha)-{29\alpha\over110}-{4\over25}>0.
 \tag{208.A7}
\]

The three affine pieces show `g(alpha)>=319/1250` on the closed
middle-band endpoints; no subrange is silently declared safe by this
comparison. The existing supremum and variance alone do not reach (A6).

The authoritative full frontier remains the following conjunctions.
All literal symbols, Vaaler tapers, signs, stars, half weights, floors,
support crossings and real-X endpoints are part of each assertion.

| Parent | Complete open target |
|---|---|
| M1 HARD | `sum_(h~L) sum_(4h<n<16h,n odd) chi4(n)a_M1(h,n)e(sqrt(Xhn)) << L^(3/2)X^epsilon` on every unowned hard shell. The small-t high-radical residual includes **all** `1<=t<ceil(sqrt L)`, not only original t=1. |
| M1 SMOOTH | `B1(D,L;X)<<X^(1/4+epsilon)` on every smooth physical label in `U1`, independently of HARD. HARD and the first SMOOTH critical witnesses each retain `X^(1/12)` in the accepted direct menu. |
| M2 TOP | In the one-count identity `E_L^top=E_owned+2Re C_comp`, with `E_owned<<L^2X^epsilon`, prove the single outer `Re C_comp<<L^2X^epsilon`. Safe row/equal-product diagonals do not estimate unequal-product correlations. |
| M2 BAL | `|sum_G G P_G|<<L^(3/2)X^epsilon` for all smooth `1<=K/L<=16`. The critical double-far energy and the separate remaining-label owner, including the j=2 square boundary, both remain. |
| M2 UNBAL | `sum_(h~L,k~K)chi4(h)a_(L,K)(h,k)e(sqrt(Xhk)) <<(LK)^(3/4)X^epsilon`, `K=XL/D^2`, `K/L>16`, with the actual joint symbol and every boundary owner. |
| Endpoint/assembly | Uniformity over every real X and `X^(1/4)<=D<=X^(1/2)`, including both D endpoints and short blocks. |
| GAR alternative | `Re{e(1/8)sum_(n<=16sqrt X)C_X^*(n)n^(-3/4)e(sqrt(Xn))}<<X^epsilon`; this supplies total active M1 only and still requires full M2. |

These owners were checked against selected graph statements. The
moment route is a separate sufficient route to the full theorem; a
moment result does not retroactively prove these blockwise owners.

## 3. Derivation and the two source interfaces

### 3.1 What total-frequency aggregation actually asks for

Let `Lambda` be the complete finite envelope in (A3), extending zero
coefficients wherever necessary. Set

\[
 \Gamma_\nu(x)=
   \sum_{\substack{\lambda_1,\lambda_2,\lambda_3\in\Lambda\\
                   \lambda_1+\lambda_2+\lambda_3=\nu}}
       b_{\lambda_1}(x)b_{\lambda_2}(x)b_{\lambda_3}(x).
 \tag{208.A8}
\]

Every product and mixed-arm term is included before a modulus. The
exact identity, up to the already rapidly small remainder, is

\[
 K_6(N)=\int_J\left|\sum_\nu\Gamma_\nu(x)e(x\nu)\right|^2dx
       +O_A(X^{-A}).
 \tag{208.A9}
\]

Polynomial bounds on Z justify making the error any chosen inverse
power by increasing the original Schwartz order. Formula (A9) is a
full signed cubic Gram representation, not a bound. If one instead
expands its square and groups by total difference, the resulting
coefficient is still x dependent. There is no license to replace it
by a constant coefficient times a Fourier transform of the interval.

Triple sums have reduced denominator at most `Q^3`. The elementary
guaranteed spacing between distinct triple sums is only `Q^-6`,
not `Q^-2`. For a fixed-coefficient model, a separated-frequency
bound thus costs `X+Q^6`, up to a logarithm. Discrete Young's inequality
and (A5) give

\[
 \|b*b*b\|_2^2\le\|b\|_1^4\|b\|_2^2
        \ll Q^4HX^\epsilon.
\]

The resulting automatic certificate is
`(X+Q^6)Q^4H<<X^5H`, already worse than the direct
`||Z||_infty^4 ||Z||_2^2<<X^3H`. This fixed-coefficient calculation
is a diagnostic of that use of spacing, not a bound asserted for
arbitrary moving coefficients. Restoring the actual multiplier and
prefix would additionally require their appropriate operator estimate.

Putting frequencies in bins of width `1/X` does not make their
phases identical. Even two coefficients `+1,-1` at distinct
frequencies in the same bin have zero unmodulated bin sum and a
nonzero exponential polynomial on J. This is an algebraic control
on a proposed bin implication, not a counterexample for (A4). A
lawful bin norm must retain the within-bin phase, for example all
necessary Taylor moments or an exact local Fourier norm, and pay
its reconstruction. The zero-th bin sum alone is insufficient.

Round 207 proved that its specified termwise absolute expansion has
size at least `X^3H=T^(7-alpha/2)`. Relative to (A6), its gap is
`46/25-alpha/2+6omega>=517/250`. This lower-bounds that positive
majorant only. Neither it nor the weak certificates above lower-bound
the signed K6, the grouped coefficients, or their actual Gram form.
The denominator classes of the two arms are disjoint at order one;
opposite frequencies can cancel inside higher products, so mixed
cubic/sixth relations remain.

### 3.2 Interface I: all-moduli Kloosterman bilinear bounds

**Primary statement checked.** Blomer--Pascadi,
[2607.24311v1, Theorem 1.1 (1.3)](https://arxiv.org/html/2607.24311v1),
27 July 2026, remains v1 at the
[current record](https://arxiv.org/abs/2607.24311).
For integer `1<=N0<=c`, intervals I,J of length at most N0, complex
product vectors and a unit a modulo c, its unnormalized sum satisfies

\[
 \left|\sum_{\substack{m\in I,n\in J\\(m,n,c)=1}}
       u_m v_n S(am,n;c)\right|
 \ll\|u\|_2\|v\|_2 c^{1+o(1)}
 \left(N_0^{1/8}c^{-3/32}+N_0^{5/16}c^{-3/16}
                    +N_0^{2/3}c^{-7/18}\right).
 \tag{208.A10}
\]

Here `S` is the ordinary complete Kloosterman sum. Every integer
modulus is allowed. Deleting the gcd restriction is supplied for
`I=J=[1,N0]`, not general translated intervals. At `N0~sqrt c`
the price is `c^(31/32+o(1))` times the product norm. Unequal lengths
have separate statements; none is substituted without its own ledger.

**Application calculation, using the permitted Round 205 complete
source.** Its actual original-t=1 coefficient is

\[
 b(m,d)=\chi_4(d)\mu^2(md)\rho_{md}(d)a^{\mathrm{lit},\sigma}_{L,X}(m,d),
 \quad c_n=\sum_{md=n}b(m,d),\quad z_n=c_ne(\sigma\sqrt{Xn}).
 \tag{208.A11}
\]

All zero extensions and selected-prime residual factors rho are
retained. The complete target is `Q_R=D0+2Re C_even<<L^2X^epsilon`,
where `R=ceil L`, `D0=sum|c_n|^2<<L^2X^epsilon`, and

\[
 C_{\rm even}=\sum_{\substack{0<r<R\\2\mid r}}(1-r/R)
 \sum_{d'm'-dm=r}b(m',d')\overline{b(m,d)}
 e\big(\sigma\sqrt X(\sqrt{d'm'}-\sqrt{dm})\big).
 \tag{208.A12}
\]

With `g=(d,d')`, `q=d/g`, `r=gk`, and `a=d'/g`, the exact equation
is `am'-qm=k`, hence `m'=k inverse(a) mod q`. Each live q is odd
squarefree **in this M1 chart**, unlike the general rational q in
(A4). The actual two-dimensional normalized Fourier completion is

\[
 T_{d,g,k}=\sum_{s,t\bmod q}\widehat A_{d,g,k}(s,t)S(s,kt;q),
 \quad \sum_{s,t}|\widehat A(s,t)|^2\ll g^2X^\epsilon.
 \tag{208.A13}
\]

The matrix contains O(1) lifts of a and O(g) lifts of m', both literal
coefficients, the real square-root phase and all traces. The DFT is
normalized by q^-2. It cannot be replaced by an arbitrary product
vector of norm one. For `(k,q)=1`, `S(s,kt;q)=S(ks,t;q)` permits
(A10) on the primitive part. Partition each residue interval into
length-`sqrt q` intervals. There are O(q) rectangles. On each rectangle,
the projective norm is at most `q^(1/4)` times its Hilbert--Schmidt
norm, and Cauchy across rectangles gives total projective mass
`O(g q^(3/4)X^epsilon)`. Consequently the certified per-label
price is `g q^(55/32+epsilon)`. Summing all d~L, all divisors g,
and O(L/g) shifts gives `L^(119/32+epsilon)`.

| Restored part of this application | Certified price |
|---|---:|
| Complete direct physical correlation | `L^3 X^epsilon` |
| Complete Fourier/Cauchy, with `sum|S(s,kt;q)|^2=q^2 phi(q)` | `L^(7/2) X^epsilon` |
| (A10), unit shifts and primitive frequencies, all rectangles/outer labels paid | `L^(119/32) X^epsilon` |
| Nonunit-k physical complement | `L^3 X^epsilon`; no target-safe signed estimate supplied |
| Zero Fourier mode, `S(0,0;q)=phi(q)` | at most `L^3 X^epsilon`; retained |
| General nonprimitive Fourier complement | `L^(7/2) X^epsilon`; retained |
| q=1 chart | `L^2 X^epsilon`; safe |
| Required complete one-real-part target | `L^2 X^epsilon` |

All positive prices are certificates for particular sufficient methods,
not lower bounds. Keeping an outer signed d,k aggregate might improve
them, but that is a new unproved estimate. The reconstruction is
`|sum z_n|^2<<L Q_R`, with physical multiplier
`X^(1/4)L^(-3/2)` up to a fixed constant. Direct `Q_R<<L^3` gives
physical `X^(1/4)L^(1/2)`; the required `Q_R<<L^2` gives
`X^(1/4)`. A correlation exponent saving is halved on reconstruction.

For (A8)--(A9), the very first kernel-matching step is absent:
relations among three reduced fractions are not themselves the
bilinear kernel S(am,n;c). Selecting a common modulus introduces
lcm/gcd strata and a joint six-variable weight; it supplies neither
the product norm nor the signed outer gain in (A10). It would be
incorrect to transplant the `c^-1/32` saving to this energy.

The inherited UNBAL spectral chart remains independently blocked.
Its complete flat-owner automatic price is
`R0 sqrt(Delta)=X/sqrt(DL)`, with `R0=X/D`, `Delta=D/L`, against
the accepted envelope
`min(Delta,sqrt(XL/D)+sqrt(X/(LD)))X^epsilon`.
The exact level-four coefficient is joint in modulus and frequency;
its zero mode is safe, but its centered part has no common-test or
common-sequence estimate. The graph records the scoped
`K^(1/2-o(1))` nuclear inflation and `sqrt(Delta)` compression cost.
This is inherited evidence, not a third newly audited spectral theorem.
It does not estimate transition, clipped, starred or sharp UNBAL owners.

### 3.3 Interface II: the new shifted-cutoff divisor theorem

**Primary statement checked.** Xiao--Li,
[2609.24248v1, Theorem 1.1](https://arxiv.org/html/2609.24248v1),
21 September 2026; the
[current record](https://arxiv.org/abs/2609.24248) has only v1.
Let g be fixed, nonnegative, smooth, supported in [1,2], of integral
one. Put `vartheta=log Y/log R`, `G_s(v)=(v-s)_+^2`, and

\[
 \Lambda_{s,R}(m)=\sum_{\substack{d\mid m\\d\le R}}
 \mu(d)G_s\!\left({\log(R/d)\over\log R}\right).
\]

Uniformly for `Y^(1/5)<=R<=Y^(1/3)` and `s,u in [0,1/2]`,

\[
 \sum_m g(m/Y)\mu^2(m)2^{\omega(m)}
          \Lambda_{s,R}(m)\Lambda_{u,R}(m)
 ={Y\over\log Y}\mathcal B_\vartheta(G_s,G_u)
       +O_g(Y/(\log Y)^2),
 \tag{208.A14}
\]

\[
 \mathcal B_\vartheta(U,V)=2\vartheta\int_0^1U'V'
 +\vartheta\int_0^1U''V''(1-v)(\vartheta-1+v)\,dv.
 \tag{208.A15}
\]

The shifts can coincide or vary with Y. They translate a log cutoff,
with effective divisor length `R^(1-s)`. They do not translate m.
The unshifted main term has coefficient
`2 vartheta^2+(4/3)vartheta`, so it is not an error-only cancellation
statement.

**Literal application audit.** The earliest coefficient equality
already fails: (A2) has `r2(m)=4 sum_(d|m)chi4(d)`, with squareful
m retained; (A14) uses mu divisors and an external squarefree sieve
weight. For example a squareful integer represented by two squares
can have nonzero r2 while the external mu^2 factor is zero. Removing
it is not a harmless normalization. Nor can replacing mu by chi4
be obtained by polarization in s,u. There is no theorem on arbitrary
divisor coefficients in (A14).

There are three further independent mismatches.

- Expanding the actual sixth filter gives products at the six
  **additively shifted integers** `m,m+h2,...,m+h6`. The pair in
  (A14) is evaluated at the same m. Neither six factors nor growing
  integer shifts `|hj|~H` are quantified by s,u-uniformity.
- On the physical m-scale `Y~X`, the actual complete hyperbola cutoff
  is `D~X^(1/2)`, outside `R<=X^(1/3)`. Taking R smaller deletes a
  long divisor complement. Setting R equal to the arithmetic width
  H is also unjustified: H is a physical additive width, not a divisor
  cutoff. Even that formal choice exceeds `X^(1/3)` when alpha<2/3.
- The actual signed filters vary on `H/X` in the normalized m variable.
  Their j-th derivative can cost `(X/H)^j`. The constant in (A14)
  is for fixed g and is not stated uniformly for this family, moving
  endpoints, or a product of six signed filters. Differences of a
  fixed nonnegative profile cannot erase these dependence costs.

No bound for Z follows. A generous hypothetical price shows that
fixing only these formal mismatches would still not suffice. Write
`a(m)=r2(m)-pi`, `h1=0`, and the **actual** integrated weight

\[
 W_{\mathbf h}(m)=\int_J\prod_{j=1}^6
                 K((x-m-h_j)/h(x))\,dx.
 \tag{208.A16}
\]

The exact expansion is `K6=sum_(m,h2,...,h6) prod_j a(m+hj)
W_h(m)`, with positivity of every m+hj enforced. The effective
ranges are m~X and five shifts of size H, with a factor H in the
weight. Schwartz truncation at `H X^eta` for any fixed eta>0 can
be paid by increasing decay order; it changes only chosen epsilon
losses. All signs stay in W. Its size is `O(H)` and the number of
shift labels is `H^5` at power level.

Now suppose, **only for an optimistic error test, not as a claim of
(A14)**, that a uniform six-point centered asymptotic at each shift
had a lossless weighted error `O(X/(log X)^2)`. Positive summation
of those errors would cost

\[
 {XH^6\over(\log X)^2}
 ={T^{8-3\alpha}\over(\log X)^2}.
 \tag{208.A17}
\]

Against (A6) its exponent excess is

\[
 {71\over25}-3\alpha+6\omega(\alpha)
 \ge {136\over125}>0.
 \tag{208.A18}
\]

Each piece decreases in alpha, and the last endpoint gives the
displayed minimum. A logarithm cannot pay this fixed power. This
is a cost of a hypothesized **positive error summation**; it is not
a lower bound for any actual remainder. Moreover all six-point
local-density main terms would still need to be evaluated with W.
Oddness of K removes a completely constant independent density in
an ideal product integral; it does not prove cancellation of an
arithmetic singular series depending on five shifts. The nonzero
bilinear main term (A15) supplies no such assertion.

The inherited Matthiesen audit is consistent with this conclusion:
the available fixed-system correlation has an ambient little-o error,
not the required uniform power error on the thin six-point geometry.
The theorem is not being imported, reclassified as a six-shift
power estimate, or counted as another full interface in this round.

### 3.4 Bounded current-source screen

Searches on 27 September 2026 used the phrases
`2026 shifted correlations sums of two squares short intervals moments
representation functions`, the three known recent Kloosterman arXiv
IDs, and `2026 rational frequencies additive energy Farey fractions
moments`, followed by direct primary records. Search/third-party
snippets served only as leads. The following is a bounded screen,
not an exhaustive claim about the literature.

| Primary record checked | Version and decision |
|---|---|
| [Milićević--Qin--Wu 2511.07550](https://arxiv.org/abs/2511.07550) | v1, 10 Nov 2025; current title is *Bilinear forms with Kloosterman sums and moments of twisted L-functions*. All-moduli abstract, no new literal joint-matrix norm imported. |
| [Pascadi 2511.08445](https://arxiv.org/abs/2511.08445) | v2, 21 Jun 2026. Factorization-dependent gains remain relevant only on compatible moduli. Round 205's fully restored failed application is inherited; no new theorem call. |
| [Fouvry--Kowalski--Michel--Sawin 2511.09459](https://arxiv.org/abs/2511.09459) | v3, 11 Mar 2026. Abstract requires geometric monodromy structure. No sheaf/conductor/exceptional-locus dictionary for (A8) has been supplied. |
| [Milićević--Robinson--Shupe 2608.21346](https://arxiv.org/abs/2608.21346) | v1, 21 Aug 2026. Complete products of shifted Kloosterman sums at odd high prime powers. The q of (A4) includes general composites and powers of two; the internal q in (A13) is squarefree. Neither is automatically this prime-power kernel. |
| [Xiao--Li 2609.24248](https://arxiv.org/abs/2609.24248) | v1, 21 Sep 2026. Fresh full audit (A14)--(A18); no import. |
| [Kim 2509.24152](https://arxiv.org/abs/2509.24152) | **Withdrawn v4, 10 Sep 2026.** Current withdrawal explanation says its theorem is generally less effective than Cauchy--Schwarz under its assumptions. Excluded. |
| [Robles 2609.11070](https://arxiv.org/abs/2609.11070) | v1, 10 Sep 2026. Linear additive twists of multiplicative coefficients with bounded mean-square normalization; abstract gives logarithmic/Diophantine savings. It is not a six-factor correlation or a square-root-phase theorem. No application credited. |
| [Baier 2609.21195](https://arxiv.org/abs/2609.21195) | v1, 18 Sep 2026. Square-moduli large-sieve improvement conditional on Hooley R*. General rational triple denominators are not restricted squares; no unconditional import. |
| [Baker--Munsch--Shparlinski 2103.12659](https://arxiv.org/abs/2103.12659) | Primary record screened from conductor lead: generic sparse-sequence additive energy/large sieve, not an actual-chi4 cubic coefficient cancellation theorem. No theorem strength credited. |
| [Matthiesen 1205.4145](https://arxiv.org/abs/1205.4145) | v1, 18 May 2012. Primary statement reread for compatibility with inherited Round 205 evidence; no new full application developed. |

No update in these screened records supplies a complete signed estimate
for (A9). This is an applicability conclusion about the named corpus,
not an impossibility theorem for spectral, algebraic or correlation methods.

### 3.5 Quantitative selection and full-quarter limit

The complete actual series is

\[
 H_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
               \cos(2\pi R\sqrt n-3\pi/4).
\]

For the accepted mollifier and a fixed nonnegative displaced w,
the graph supplies
`D(V)<<T^epsilon(V^-2+TV^(-136/13))` and
`||H_T||_infty<<T^(beta+epsilon)`.
The complete remaining p=12 high-value objective is

\[
 \int_{|H_T(R)|>T^{13/125}}w(R/T)|H_T(R)|^{12}dR
           \ll T^{29/25+\epsilon}.
 \tag{208.A19}
\]

The low values are already safe because the integrated distribution
cost is `T^(26/25)+T^(29/25)`. The reviewed middle-band reduction
retains every low/high block, singleton and infinite tail at the
milestone. A uniform proof of (A6) for every middle block is sufficient:
the physical sixth-to-radius conversion costs T^-4, and interpolation
with the actual block supremum costs `T^(6omega)`. Hence the p=12
price is `T^(6omega-4)K6`, exactly explaining (A6). The number of
dyadic blocks costs only logarithms. This is a sufficient strategy;
the full p=12 estimate need not imply each such interpolated sixth
estimate.

The current full p=12 radius bound is `T^(10beta+epsilon)`.
The required complete saving is `10beta-29/25`; the pointwise bridge
restores amplitude/Jacobian factor `T^7` and a sharp-error contribution
`T^(8+epsilon)`. Thus a successful milestone gives sharp moment
`Y^(102/25+epsilon)` and exponent `102/325`, not one quarter.

For the full target, a sufficient route is
`integral w(R/T)|H_T|^p dR<<T^(1+epsilon)` for arbitrarily large
fixed p. More generally a radius exponent E(p) has pointwise
certificate

\[
 {p/4+(1+\max(1,E(p)))/2\over p+1}.
\]

Having `(max(1,E(p))-1)/p -> 0` along unbounded fixed p is
sufficient. Constants may depend on p; p need not grow with T.
By contrast the accepted `E0(p)=max(1,(p-2)beta)` tends through
this bridge to theta, not one quarter. A fixed positive-power
high-value cutoff also does not certify the required hierarchy by
itself. No conclusion here uses or anticipates the isolated blind
report; the formula follows directly from amplitude, Jacobian and
the one-sided persistence inequality in the permitted strategy memo.

Therefore choose an **actual coefficient-sensitive complete high-value
or six-factor inequality**, not a finer partition or another bare
completion. The rational cubic formulation can be its explicit
working form, provided an attempted proof retains (A3)--(A4), the
whole J and all near frequencies. Neither of the two audited sources
currently offers a quantitatively affordable way to prove it. This
selection is research strategy, not promotion.

## 4. First doubtful or unproved step

For the proposed rational approach the first missing estimate is
(A9) bounded by the right side of (A6), or an independently proved
coefficient-sensitive norm implying it after **all** multiplier,
prefix and within-bin phase costs. Exact grouping is proved finite
algebra. Smallness after grouping is unproved.

For (A10) on internal M1, the first unaffordable step is the actual
matrix projective norm together with the signed outer d,k sum and
target-safe nonunit/nonprimitive complements. For its proposed use
on (A8), an exact Kloosterman dictionary precedes even that issue.
For (A14), the first equality between arithmetic coefficients already
fails. The optimistic calculation (A17) explicitly grants more than
the source; it cannot be cited as a theorem or as a signed no-go.

No successful fixed sixth estimate here would establish the whole
arbitrarily-high-moment hierarchy, HARD+SMOOTH, TOP+BAL+UNBAL, or
the real-endpoint quarter theorem.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `full_quarter_scope` | Pass as scope audit: all five direct parents, GAR's separate quantifier and the arbitrary fixed-moment requirement are retained; p=12 gives only 102/325. |
| `complete_ranges` | Pass: all middle N, both rational arms, every prefix label, both signs, zero/exceptional modular modes, and already priced complementary bands remain explicit. No favorable modulus set is used as the whole source. |
| `actual_coefficients` | Pass: (A3)--(A4), (A11)--(A13) and (A16) are literal coefficient interfaces. The Xiao--Li mismatch is rejected at coefficient level. |
| `signed_absolute_distinction` | Pass: one outer real part in M1/TOP is retained; termwise majorant lower bounds and positive method prices are not signed lower bounds. Same-bin zero-th cancellation is not treated as a norm estimate. |
| `all_costs_restored` | Pass: H, X, T, five shifts, filter weight, all Fourier/projective costs, modular complements, scalar square root, physical multiplier and p=12 reconstruction are displayed. |
| `real_endpoints` | Pass for the identities and scope: x and X remain real, J is displaced, the prefix is strict, the even cutoff has its exact safe error, and every internal endpoint owner remains required. No source proves the missing uniform estimate. |
| `source_versions_hypotheses` | Pass for the bounded two-interface audit and screens; fresh Kim withdrawal recorded. Source applicability fails where stated, with no imported theorem. |
| `independent_hierarchy` | This task supplies its own algebraic hierarchy check; the conductor's separate statement-only review remains the independent gate. No blind or sibling report was opened. |

Further analytical checks: primitive denominators at order one cannot
be substituted for triple spacing; mixed-arm exact relations survive;
q=1 is separate in the M1 completion; unit k is required only in the
specific bilinear call, not in exact completion; prime powers in (A4)
are not silently removed; the Xiao--Li s,u interval is not an additive
shift interval. No mathematical experiment or random-model argument
is used.

## 6. Dependencies and exact artifacts used

The following permitted local artifacts were read:

- `protocol.md`.
- `state/active_campaign.yml` and the assigned
  `briefs/arithmetic_full_frontier.md`.
- `state/proof_obligations.yml`: selected GC-target, M9, M1/M2, the
  five direct parents, endpoint uniformity, GAR/total-active
  equivalence, hard small-t residual, accepted complete moments,
  UNBAL level-four matrix and inverse-selector projective obstruction
  records. Statements/statuses were extracted separately from long
  provenance arrays.
- `strategy/round208_full_proof_strategy_review.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md`.
- `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reports/internal_arithmetic_routes.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/synthesis.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.

The exact primary URLs and versions are given in Sections 3.2--3.4.
Full new application audits are limited to Blomer--Pascadi1.1 and
Xiao--Li1.1. Matthiesen and the other sources remain inherited
evidence or bounded screens. The conductor supplied the cubic-energy
question and sparse-large-sieve/indicator-variance leads; no latter
indicator-variance theorem was used. No sibling report, unpermitted
proof artifact, shared synthesis or historical archive was read or
changed by this task.

## 7. Recommended state effect

**No change** to the graph, proof draft, source cards, parent statuses
or exponents. Retain the source audit and complete power ledger as
Round 208 strategy evidence. Add no claim that rational aggregation is
impossible, that the actual moment has a large lower bound, or that
the source names produce an improvement.

The conductor can select (A6)/(A19) with the actual cubic Gram form
as a research objective, but should count progress only upon a net
complete bound or a new essential inequality with its norms proved.
This report makes no successor design and stops here.

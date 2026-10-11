# Round 211: literal hyperbola source and two bilinear theorem audits

Campaign: `gc-full-source-method-review`. Task: `bilinear_arithmetic_sources`.
Role: selected-context source auditor; candidate evidence, not a blind report.
Source checks: 2026-09-27 UTC. Report completed: 2026-09-27 16:01 UTC
(2026-09-28 00:01 Asia/Shanghai). Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: entirely analytical/algebraic and primary-source inspection; no
mathematical numerical experiments. Only this assigned report is written.

## 1. Result: two legal imports, neither with a sufficient restored power

The actual divisor expansion can be matched to genuine bilinear monomial
theorems without discarding the outer character. Its product smoothing has
bounded separation cost, and an exact hyperbola partition has no missing
large-divisor complement. Thus arbitrary arithmetic weights on the original
one-variable square-root sum are not the obstruction to these two imports.

The obstruction is quantitative. On the balanced divisor rectangles
`A~B~sqrt(N)`, with phase size `Z~T sqrt(N)` and physical weight `N^(-3/4)`:

* Wu's 1999 Theorem 1 gives the leading certificate
  `T^((4K-2)/w) N^((K-k-1)/(2w))`, where `K=2^k`,
  `w=20K-2k-14`, `k>=1`. Its T exponent is strictly larger than `1/5`.
  It is worse than the trivial block certificate throughout the required
  middle band.
* Kowalski--Robert--Wu's published Proposition 5 gives leading certificate
  `T^(1/8)N^(1/16)`, with all other terms and coefficient costs below.
  Even after the trivial cap, it cannot reach `T^(83/650)` on any fixed
  interior scale of that band. Its aspect-independent first term is
  already redundant against the two elementary complete block caps on
  all `1<=N<=T`, before the stronger accepted beta cap.

These are failures of specified positive theorem certificates, not lower
bounds for an actual signed sum. Both theorems permit the exponents
`alpha=beta=1/2`. The zero Hessian of `sqrt(dm)` must not be used to reject
them under a condition they do not impose.

No improved complete moment, pointwise exponent, M1/M2 parent, or GAR
estimate follows. The source comparison gives no reason to replace the
original complete signed tenth gate by the stronger demand that each
hyperbola rectangle have a small supremum. Retain that signed gate as the
quantified actual-coefficient objective unless another fully priced source
supplies a genuine gain. The full quarter target still requires the complete
direct frontier or an appropriate all-order/pointwise whole-discrepancy
argument.

## 2. Exact statement, source hypotheses, and complete frontier

Use `e(t)=exp(2 pi i t)`, real `T>=2`,

\[
 I=[T/\sqrt2,\sqrt3T],\qquad
 f_N(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),\qquad
 F_N(R)=\sum_{n\ge1}r_2(n)f_N(n)e(R\sqrt n).
 \tag{1}
\]

Here v is the supplied fixed smooth function supported in `[1,4]`, and
Psi is the supplied fixed mollifier transform. The physical block is
`H_N=Re(e(-3/8)F_N)`. Put

\[
 b=83/650,\quad N=T^\alpha,\quad
 4b=166/325<\alpha<1-2b=242/325.
 \tag{2}
\]

A bound for the complex F_N is sufficient for H_N; equivalence is not
asserted. The original complete gate is the weaker real-block statement

\[
 \int_I |H_N(R)|^{10}\,dR
 \ll_\epsilon T^{83/65+\epsilon}N^{-1/2},
 \tag{3}
\]

or its reviewed signed-shell counterpart
`integral_J |Z_N|^10 << T^(473/65+epsilon)N^(-1/2)` with `X=T^2`,
`J=[X/2,3X]`, `h(x)=2 sqrt(x)/sqrt(N)`. Both arms, all prefixes, real
endpoints and varying width belong to that counterpart. This report
estimates (1) directly and does not silently freeze those shell data.

**Full audit A, precise source.** Jie Wu, *Double Exponential Sums and
Some Applications*, Monatshefte fuer Mathematik 128 (1999), 255--262,
Theorem 1, pp. 255--256. The [publisher record](https://link.springer.com/article/10.1007/s006050050062)
identifies the November 1999 published version; its [author-uploaded full
article](https://www.researchgate.net/publication/226968624_Double_Exponential_Sums_and_Some_Applications)
was supplied by Jie Wu on 13 April 2015. For

\[
 S=\sum_{a\asymp A}u_a\sum_{m\in J(a)}
 e\!\left(Z\frac{a^\gamma m^\delta}{A^\gamma B^\delta}\right),
 \quad |u_a|\le1,\quad J(a)\subset[B,2B]\text{ an interval},
\]

the hypotheses are `Z>0`, `A,B>=1`, fixed real exponents with
`gamma delta (gamma-1)(delta-1)(gamma+delta-2)(2gamma+delta-3)!=0`.
For fixed integer `k>=1`, `K=2^k`,

\[
 |S|\ll
 \left[(Z^{4K-2}A^{14K-2k-10}B^{13K-2k-10})^{1/w}
       +A\sqrt B+\sqrt A B+Z^{-1}AB\right]\log(2+ZAB),
 \quad w=20K-2k-14.
 \tag{4}
\]

The outer coefficient is arbitrary within its stated bound. No
`gamma+delta-1` exclusion, nonzero Hessian hypothesis, or prime-modulus
condition appears. At `(gamma,delta)=(1/2,1/2)` every required factor is
nonzero. Constants may depend on the fixed exponents and k.

**Full audit B, precise source.** Emmanuel Kowalski, Olivier Robert and
Jie Wu, *Small gaps in coefficients of L-functions and B-free numbers in
short intervals*, Revista Matematica Iberoamericana 23 (2007), no. 1,
281--326, Proposition 5 on p. 303, proof pp. 303--306, in the
[published EMS PDF](https://ems.press/content/serial-article-files/38194).
The [arXiv record](https://arxiv.org/abs/math/0507001v1) is the older
30 June 2005 v1; the theorem here was checked in the published version.
For the rectangular sum

\[
 S=\sum_{a\asymp A}\sum_{m\asymp B}u_av_m
       e\!\left(Z\frac{a^\gamma m^\delta}{A^\gamma B^\delta}\right),
 \qquad |u_a|,|v_m|\le1,
\]

with `Z>0`, `A,B>=1` and fixed `gamma,delta` outside `{0,1}`,

\[
 |S|\ll_\epsilon (AB)^\epsilon
 \left[(ZA^6B^6)^{1/8}+A^{1/2}B+AB^{3/4}+Z^{-1/2}AB\right].
 \tag{5}
\]

It has no restriction excluding `(1/2,1/2)` and no modular hypotheses.
The norms in this statement are the two coefficient suprema. They are
not unit-normalized Hilbert-space norms. All terms in (5) are retained.

The authoritative open frontier, read from the graph, remains:

| Route/parent | Complete obligation; effect of this audit |
|---|---|
| M1 HARD | Actual signed cone `sum_(h~L)sum_(4h<n<16h,n odd) chi4(n)a(h,n)e(sqrt(Xhn)) << L^(3/2)X^epsilon`. The unowned small-t high-radical residual contains every `1<=t<ceil(sqrt L)`, not only original t=1. No closure. |
| M1 SMOOTH | Every smooth physical `B1(D,L;X)<<X^(1/4+epsilon)`, separately from HARD. The first critical menu has `X^(1/12)` deficit. No closure. |
| M2 TOP | In `E_top=E_owned+2Re C_comp`, prove the single outer `Re C_comp<<L^2X^epsilon`. Row/equal-product safe pieces do not bound the unequal-product form. No closure. |
| M2 BAL | `|sum_G G P_G|<<L^(3/2)X^epsilon` on all smooth `1<=K/L<=16`, with both quarter shifts and remaining-label ownership, including the j=2 square boundary. No closure. |
| M2 UNBAL | Actual `sum_(h~L,k~K)chi4(h)a(h,k)e(sqrt(Xhk)) <<(LK)^(3/4)X^epsilon`, `K=XL/D^2`, `K/L>16`. No closure. |
| Endpoints | Every real X and `X^(1/4)<=D<=X^(1/2)`, all short blocks, floors, stars, half weights and support crossings. No source estimate may silently omit them. |
| GAR alternative | `Re{e(1/8)sum_(n<=16sqrt X) C_X^*(n)n^(-3/4)e(sqrt(Xn))}<<X^epsilon`. This controls only total active M1; M2 remains necessary. Its coefficient is not r2(n). No transfer from (1) is asserted. |

## 3. Derivation and complete cost ledger

### Exact physical hyperbola, with every divisor present

The actual identity `r2(n)=4 sum_(d|n)chi4(d)` gives

\[
 F_N(R)=4\sum_{d,m\ge1}\chi_4(d)f_N(dm)e(R\sqrt{dm}).
 \tag{6}
\]

For an integer `D>=1` put `M=floor(4N/(D+1))`. Exactly,

\[
 F_N/4=
 \sum_{d\le D,m\ge1}\chi_4(d)f_N(dm)e(R\sqrt{dm})
 +\sum_{m\le M,d>D}\chi_4(d)f_N(dm)e(R\sqrt{dm}).
 \tag{7}
\]

If the second range has a nonzero summand, then `dm<=4N` and
`d>=D+1`, hence `m<=M`. The ranges are disjoint. They retain equality
at all integer boundaries; nothing uses integer R, T or N. Take
`D=floor(2 sqrt(N))` for a balanced split, with the finitely small N
handled separately. Dyadically divide both variables into `d~A,m~B`.
Only `AB~N` contributes; there are `O(log(2N))` such scale pairs, or
the harmless coarser `O(log^2(2N))` bound. Short edge intervals are
kept as coefficient indicators. Neither arm is discarded.

Wu uses `(A,2A]` for its outer dyadic convention. Isolate `d=1`
when using that convention: its complete inner sum has the safe trivial
price `O(N^(1/4))` after weighting. This is distinct from the single
frequency `n=1` in final reconstruction. It is not an omitted source
case and does not repair the failed balanced certificate. Proposition 5
uses `[A,2A)` and includes the integer 1 at A=1 directly.

The phase dictionary on every contributing rectangle is

\[
 \phi(d,m)=R\sqrt{dm}
    =Z\sqrt{d/A}\sqrt{m/B},\qquad Z=R\sqrt{AB}\asymp T\sqrt N.
 \tag{8}
\]

This is a real monomial phase, not a modular square root. There is no
large modulus to which a Kloosterman saving can be attached. The only
character modulus is the fixed 4. Keep chi4(d) as the outer coefficient
for (4), even on the second arm where d is the long variable. For (5)
either orientation is legal because both factors permit bounded
coefficients. Splitting chi4 into residues or taking its absolute value
is unnecessary in either import.

For (4), smooth product weights can be restored by product-prefix
partial summation. The normalized function

\[
 g_{N,T}(x)=x^{-3/4}\Psi(\sqrt{N/T}\sqrt x)v(x)
\]

has bounded total variation and fixed compact support when `N<=T`.
Write `f_N(dm)=N^(-3/4)g_(N,T)(dm/N)` as a Stieltjes integral of
indicators `dm<=y`. For each d the permitted m form an interval after
intersecting its dyadic block and the second-arm cutoff. The boundary
terms and integral cost `O(N^(-3/4))`. Wu's arbitrary `J(d)` covers
the variable length exactly. No derivative of the large oscillatory
phase is put into that variation norm.

For (5), an arbitrary variable interval is not a stated hypothesis.
Instead separate the actual smooth product weight before application.
Fourier inversion in `s=log x` gives

\[
 g_{N,T}(x)=\frac1{2\pi}\int_{\mathbb R}
       c_{N,T}(t)x^{it}\,dt,
 \qquad \int_{\mathbb R}|c_{N,T}(t)|(1+|t|)^jdt\ll_j1.
 \tag{9}
\]

Uniform bounds follow by repeated integration by parts on the fixed
compact log-support. Thus the product factor in (6) is a superposition
of `d^(it)m^(it)` with bounded total product-supremum mass, followed
by the explicit `N^(-3/4)`. The cuts `d<=D`, `d>D`, `m<=M`, and
partial dyadic endpoints are one-variable indicator factors. On a full
rectangle the norms supplied to (5) are at most one in each variable;
there is no hidden factor `sqrt(AB)` or a nuclear norm of an arbitrary
joint array. The integral in (9) costs O(1). This argument works also
for sign-changing g. It does not replace it by a positive mask.

All finite derivatives satisfy
`A^i B^j partial_d^i partial_m^j [g_(N,T)(dm/N)] <<_(i,j)1`
on contributing rectangles, with the inherited `N^(-3/4)` outside.
For `N>T`, these seminorms have arbitrary inverse-power decay in
`sqrt(N/T)` after using additional Schwartz decay; no uniformity at
infinite t in (9) is assumed without its integrable decay. These facts
justify smoothing costs; they alone do not make the adjacent `N~T`
physical tail small. That already reviewed complementary bound is
retained separately below.

### Audit A: Wu's entire certificate at actual variable lengths

Write `p=4K-2`, `w=20K-2k-14` in (4), and insert (8), `B~N/A`,
and the full physical amplitude. Up to logarithms and fixed factors,
the per-rectangle certificate is

\[
 \mathcal W_k(A)=
 T^{p/w}N^{-(k+1)/(2w)}A^{K/w}
 +N^{-1/4}A^{1/2}+N^{1/4}A^{-1/2}
 +T^{-1}N^{-1/4}.
 \tag{10}
\]

The first term is asymmetric because d remains the coefficient-bearing
outer variable. Orienting the second arm as a short unweighted outer
variable would put chi4 in the inner variable, outside (4); that change
has not been made for free. Formula (10) covers both actual orientations
by retaining d as outer. Source constants are uniform in all partial
inner intervals and in the bounded outer character.

Already at the necessary balanced scales `A~sqrt(N)`, the first term is

\[
 T^{p/w}N^{(K-k-1)/(2w)}.
 \tag{11}
\]

Here `K-k-1>=0`, and
`5p-w=2k+4>0`. Consequently this component of the certificate is at
least `T^(1/5)` at power level for every fixed k. Throughout (2),
`N^(1/4)<=T^(121/650)<T^(1/5)`. Even optimizing over the permissible
fixed k cannot improve the trivial `N^(1/4)` certificate for these
balanced scales. For example k=1 gives `T^(1/4)`; k=2 gives
`T^(7/31)N^(1/124)`. The other terms in (10) specialize to
`O(1+T^(-1)N^(-1/4))` and do not remove the first term.

One may cap every rectangle by its trivial `N^(1/4)` bound and sum
all dyadic rectangles and both arms, paying logarithms. This yields a
valid complete bound but no improved exponent. The claim is only about
that source-and-triangle certificate. Cancellation between rectangles,
or a new estimate exploiting chi4 instead of merely accommodating it,
could change the answer. The actual balanced contribution has not been
lower-bounded. The import stops at (11).

### Audit B: a more flexible product-coefficient theorem, fully normalized

Substitution into (5) yields, in the orientation `d~A,m~N/A`,

\[
 \mathcal K(A)=T^{1/8}N^{1/16}
   +N^{1/4}A^{-1/2}+A^{1/4}+T^{-1/2}.
 \tag{12}
\]

Swapping the variables is lawful in (5), with the corresponding last
two length terms `N^(-1/4)A^(1/2)+N^(1/4)A^(-1/4)`.
Take the smaller of those two *sums* of length terms, retaining the
common first and last terms. Formula (9) restores the complete actual
symbol at O(1) product mass. The bound remains valid for every finite
partial rectangle and for both hyperbola arms.

At `A~sqrt(N)` its normalized price is

\[
 T^{1/8}N^{1/16}+N^{1/8}+1+T^{-1/2}
 \ll T^{1/8}N^{1/16}\quad (N\le T).
 \tag{13}
\]

The trivial cap therefore gives exponent

\[
 \min\{\alpha/4,\ 1/8+\alpha/16\}.
 \tag{14}
\]

The crossover is `alpha=2/3`. On every fixed interior alpha in (2),
the first branch is larger than b, while the second exceeds b even
at the lower endpoint, since
`1/8+(4b)/16-b=1/8-3b/4>0`. Thus (14) cannot certify the requested
`T^b` peak. The latter branch also exceeds the inherited beta throughout
(2): its smallest value is `1/8+b/4`, whereas the graph's exact beta
is less than `13/100`. No improvement over the accepted complete cap
is supplied at any middle scale by this balanced-rectangle certificate.

These conclusions retain all lengths and both coefficient norms.
They do not infer a lower bound for the signed bilinear form from a
large positive term in an upper bound. Paying any remaining rectangles
for free would still leave this specific sufficient treatment inadequate;
therefore further subdivision of the failed theorem call is not a
complete-source gain. The import stops at (13)--(14).

There is a stronger complete comparison, without the balanced restriction.
For every `1<=N<=T`, the first term of (12) satisfies

\[
 T^{1/8}N^{1/16}\ge
       \min\{N^{1/4},(T/N)^{1/2}\}.
 \tag{14a}
\]

For `N<=T^(2/3)` the comparison with `N^(1/4)` is exactly
`T^2>=N^3`. For `N>=T^(2/3)` the comparison with `(T/N)^(1/2)`
is exactly `N^9>=T^6`. Thus the same already-paid aspect-independent
term cannot improve the inherited elementary whole-block envelope at
any N in this range. The accepted beta cap only strengthens this
conclusion. This remains a statement about the source's upper certificate,
not about the magnitude of the actual sum.

### Phase geometry and a diagnostic against a false spectral dictionary

Direct differentiation gives

\[
 \phi_{dd}=-\frac{R\sqrt m}{4d^{3/2}},\quad
 \phi_{mm}=-\frac{R\sqrt d}{4m^{3/2}},\quad
 \phi_{dm}=\frac{R}{4\sqrt{dm}},\quad \det D^2\phi=0.
 \tag{15}
\]

The two audited theorems remain legal. A different theorem demanding
nonzero determinant would fail here. It would require an actual new
normal form, rather than a generic two-variable curvature assertion.

For an interior stationary point after an m-transform, solve
`phi_m=k>0`. Then

\[
 m_*={R^2d\over4k^2},\qquad
 \phi(d,m_*)-km_*={R^2d\over4k},\qquad
 k\asymp Z/B\asymp RA/\sqrt N.
 \tag{16}
\]

The stationary amplitude is of order `B/sqrt(Z)`. The remaining
outer phase is linear in d, and chi4 still matters:

\[
 \chi_4(d)={e(d/4)-e(-d/4)\over2i}.
 \tag{17}
\]

On an unweighted interval of length A, the resulting character sum is
bounded by the sum of
`min(A,||R^2/(4k)+1/4||^(-1))` and
`min(A,||R^2/(4k)-1/4||^(-1))`, with the resonance interpreted as A.
The near-resonances require

\[
 |R^2-(4j\pm1)k|\ll k/A\asymp R/\sqrt N.
 \tag{18}
\]

Thus the character produces quarter-shifted product shells. There is
no automatic complete character period with a zero sum, and no prime
modulus has appeared. This is a phase diagnostic, not a third imported
theorem or a completed Poisson estimate: starred dual endpoints,
stationary points entering/exiting the actual support, variable dual
lengths, derivative weights, nonstationary tails and transform errors
would all still have to be supplied before a full bound could be cited.
The diagnostic identifies why a bare transform cannot be counted as a
spectral saving.

### Internal routes, reconstruction, and the full-quarter comparison

The same generic monomial price has no favorable direct internal
dictionary at target strength. Even *granting* a unit product symbol
for a balanced internal rectangle `h,n~L`, (5) has leading price
`X^(1/16)L^(13/8)` at `Z=sqrt(X)L`, against `L^(3/2)`.
For UNBAL, with `M=LK`, the corresponding optimistic leading price is
`X^(1/16)M^(13/16)`, against `M^(3/4)`. Both lose a positive factor
before any actual joint-symbol separation. These are comparisons of
the same already audited theorem under an explicitly favorable norm
assumption, not verified new imports into the literal internal symbols.
TOP's completed real part, BAL's G-sum and GAR's C_X^* coefficient
cannot be replaced by those product vectors without proof.

The inherited arithmetic frontier report additionally prices its legal
Blomer--Pascadi primitive/unit M1 part at `L^(119/32)` versus `L^2`,
retaining nonunit, zero and nonprimitive complements. The inherited
UNBAL scalar/spectral routes retain their norm and compression losses.
Those reviewed failures are context, not newly re-audited spectral
theorems. Nothing in (6)--(18) supplies their missing matrix dictionary
or authorizes transplanting their modular saving.

For completeness, an actual success at (3) gives the supplied reproduction
bound

\[
 |H_N(R_0)|\ll N^{1/20}
      \left(\int_I|H_N|^{10}\right)^{1/10}+O_A(T^{-A})
 \ll T^{b+\epsilon},\quad R_0\in[T,\sqrt2T].
 \tag{19}
\]

The factor `N^(1/20)` cannot be omitted. The already reviewed complements
are `N<=T^(4b)` with bound `N^(1/4)`, and
`T^(1-2b)<=N<=T` with bound `(T/N)^(1/2)`, including equality
endpoints. The singleton, partial blocks, complete tail above T,
infinite Schwartz remainder and the logarithmic block sum retain their
reviewed treatment. They are not proven small merely by the Schwartz
factor at `N~T`. Finally

\[
 P(R^2)=\frac{\sqrt R}{\pi}H_T(R)+O(T^{1/2+\epsilon})
\]

restores the amplitude and sharp error, giving squared-radius exponent
`1/4+b/2=102/325`. For the shell tenth moment the complete conversion
has factor `T^(-6)` and the reviewed negligible shell errors, explaining
the gate `T^(473/65)N^(-1/2)`. No such success is proved here.

The baseline remains, with both terms,

\[
 \int_I|H_N|^{10}\ll_\epsilon T^\epsilon
   [TN^{-3/110}+T^{8\omega(\alpha)}],\qquad
 \omega(\alpha)=\min(\alpha/4,\beta,(1-\alpha)/2).
 \tag{20}
\]

Its largest deficit relative to (3) is
`7 beta-101/130`, at `alpha=1-2 beta`; the bulk term separately
fails when `alpha>99/169`. None of (10)--(14) removes either term.
The safe exact rational tenth energy `T^(7+epsilon)N^(-1/2)` remains
distinct from the signed near-frequency estimate still needed.

For the full quarter target, the supplied all-order sufficient gate is
`K_(2k)(N)<<T^(k+1+2kb+epsilon)N^(-1/2)` throughout
`T^(4b)<N<T^(1-2b)`, with its bridge and complements verified on
every required band. Unbounded fixed orders and b tending to zero can
serve; one fixed tenth success cannot. The direct M1/M2 and GAR routes
are alternatives with their own unchanged quantifiers, not consequences
of a partial physical-wave estimate.

### Bounded current primary screen

Searches on 27 September 2026 covered bilinear monomial exponential
sums, real square-root phases, and 2025--2026 bilinear square-root
sources. Search snippets were discovery aids; decisions below use
the primary records. This is not an exhaustive literature claim.

| Source/version checked | Scoped decision |
|---|---|
| [Baier 2601.15448v4](https://arxiv.org/abs/2601.15448v4), 3 July 2026 | Modular-root energies and square-modulus large-sieve applications. The actual phase in (8) is real; no modular kernel/norm dictionary is present. No theorem gain imported. |
| [Baier 2605.01635v3](https://arxiv.org/abs/2605.01635v3), 20 July 2026 | Current title is *Partial progress towards the large sieve for square moduli*. It consolidates the two following manuscripts; both unconditional Fourier work and conditional short-Salie consequences are distinguished in its abstract. Not a theorem on (8). |
| [2603.00768v3](https://arxiv.org/abs/2603.00768v3) and [2603.25814v3](https://arxiv.org/abs/2603.25814v3), 20 July 2026 | Withdrawn because merged into and superseded by 2605.01635, not recorded as mathematical refutations. Older snippets/titles must not be treated as current separate improvements. |
| [Robert--Sargos, published 2006 author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf) | Screened as a monomial source and as background to Proposition 5. No third complete application audit or gain credited. |

The fresh full audits remain exactly (4) and (5). In particular, this
report does not repeat the earlier unweighted-error Abel or outer-absolute
CRT closures as new work. It avoids those steps altogether in (6)--(14).

## 4. First doubtful or unproved step

For (4) the first quantitative obstruction is its leading normalized
price (11), even with every source hypothesis satisfied. For (5) it is
(13)--(14). The smooth product coefficient norm has been paid; there is
no missing favorable norm estimate that would erase those displayed
terms. The conclusions do not rule out stronger character-sensitive
theorems, cancellation across dyadic rectangles or a signed moment
argument.

For a new transform/spectral route, the first missing assertion is a
uniform signed estimate on the full quarter-shifted product-shell
aggregate suggested by (16)--(18), with all actual weights and endpoint
terms. Equations (16)--(18) do not establish such a transform estimate.
For the selected complete moment objective the missing assertion is still
(3), equivalently the reviewed signed shell gate, not its formal
divisor or fifth-convolution expansion.

No source here distinguishes chi4 sufficiently to certify the target:
the two imported bounds remain true for arbitrary bounded outer vectors.
That compatibility explains their legitimacy and their limited power;
it is not evidence for the false arbitrary-coefficient quarter analogue.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | PASS as identity/application audit: (6)--(9) use the exact r2 divisor coefficient, the actual smooth product mask, and chi4(d) in its legal factor. No arbitrary-weight one-variable exponent-pair call is made. |
| `complete_scales` | PASS: (7) includes every divisor; (10),(12) state all A and B costs. The balanced diagnostic lies within the required family, while every other scale can be retained with the trivial cap. No favorable subrange is called complete. |
| `signed_absolute_distinction` | PASS: failure concerns positive theorem certificates and subsequent triangle summation. No signed lower bound is inferred. The original real signed moment is weaker than the proposed complex per-rectangle peak route. |
| `real_endpoints` | PASS for the identities and two actual source calls: all real R,T, smooth product endpoints, partial dyadic intervals and the exact integer hyperbola cuts are retained. The diagnostic transform is expressly not a completed endpoint-uniform bound. |
| `all_costs_restored` | PASS: Z, both lengths, N^(-3/4), all terms of both source inequalities, fixed modulus 4, bounded product norm, variable inner intervals, dyadic sums, complements, N^(1/20), T^(-6), sqrt(R) and sharp error are displayed. |
| `full_quarter_scope` | PASS: every direct parent and GAR's separate total-M1 scope remains open. The fixed gate gives only 102/325. All-order and enlarged-band requirements remain explicit. |
| `source_versions_hypotheses` | PASS for the two named published theorems and bounded primary screens. Zero Hessian is not falsely promoted to an excluded hypothesis. Baier version/merger status is corrected from the primary records. |
| `statement_only_control` | NOT supplied by this selected-context report. The separately isolated task and conductor seam remain necessary; no sibling/blind artifact was read. |

Analytical controls: direct substitution verifies (10) and (12);
`5p-w=2k+4` verifies the Wu floor; `alpha=2/3` verifies the second
certificate's crossover; equality in the hyperbola cutoff is checked in
(7); (15) tests degeneracy without inventing a theorem condition; (17)
retains both quarter-shift resonances. No numerical experiment or
probabilistic model supports these claims.

## 6. Dependencies and exact artifacts used

Only protocol, this task's brief, and the permitted local context were
read; graph reads selected relevant node statements and statuses rather
than treating the long provenance arrays as proofs:

* `protocol.md`.
* `state/proof_obligations.yml`: GC-target, M9, M1/M2, the five direct
  parents, endpoint uniformity, GAR and total-active equivalence,
  and the accepted complete square-root moment node.
* `state/active_campaign.yml`, Round 211.
* `rounds/codex-managed/gc-full-source-method-review/briefs/bilinear_arithmetic_sources.md`.
* `strategy/round211_full_source_strategy_review.md`.
* `strategy/gauss_circle_strategy_review_2026-09-23.md`.
* `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`.
* `rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md`.
* `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
* `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/arithmetic_full_frontier.md`.
* `rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/actual_shifted_correlations.md`.
* `rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/signed_rational_bins.md`.

Primary URLs, publication versions, theorem identifiers and current record
dates are given where used in Sections 2--3. The supplied closed-round
artifacts support the inherited moment/complement/reconstruction ledger,
not a new external theorem. The conductor supplied the zero-Hessian and
interior stationary-phase diagnostic and a Wu source lead; this report
independently calculates their displayed algebra. A later conductor Wu
Theorem 2 calculation was acknowledged but is not a third full audit here.
No source card, graph, proof draft, validation matrix, shared synthesis,
legacy artifact, sibling report or successor file was changed.

## 7. Recommended state effect

**No change** to accepted mathematics, parent statuses or exponents.
Retain the exact legal-import dictionaries and the failed positive-cost
certificates as Round 211 strategy evidence. Their useful content is that
the outer character and actual product smoothing can be preserved cheaply,
yet the two named general bilinear theorems still do not reach the goal.

Prefer the complete signed tenth objective (3), or a demonstrably stronger
complete actual-coefficient result with an audited bridge, over another
unpriced rectangular or modular reformulation. Any renewed internal route
must close a whole quantified parent; GAR must still be joined with M2.
This is an evidence-based comparison for the conductor, not a successor
design or a claim that other bilinear or spectral methods are impossible.
The assigned bounded task stops after this report.

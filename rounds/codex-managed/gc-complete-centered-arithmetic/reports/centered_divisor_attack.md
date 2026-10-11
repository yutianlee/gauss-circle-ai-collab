# Round 213: finite norm models and the actual complementary arithmetic

## 1. Result: a complete low-period calculation and a scoped approximation obstruction

Campaign: `gc-complete-centered-arithmetic`. Task: `centered_divisor_attack`.
Role: discovery, selected context, NONBLIND. Generated: 2026-09-28.
Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: analytical and one narrow source audit;
zero mathematical numerical experiments.

The complete actual centered target remains open. This report proves a
distinct, quantitatively closed obstruction to a finite local-model route.

* A nonnegative periodic norm model of period `q <= c ell_(h,k)` has an
  explicitly bounded oscillatory sum. Its normalized finite Fourier
  coefficients, all Poisson aliases, and its mean are retained. Summing
  its entire contribution and its mean mismatch with `rho_loc` over all
  residual shifts costs at most `T^(166/325+epsilon)`.
* The complementary sum is kept exactly, with all four actual `r2`
  factors. Replacing that sum by its coefficientwise absolute error
  cannot close the target: for **every** family of nonnegative periodic
  models in the stated period range, its complete absolute error is at
  least `c N/log T`, at each fixed interior power scale `N=T^alpha`.
  This is proved on actual coefficients using an omitted inert prime,
  exact CRT counts, and actual surviving four-point mass.
* Consequently optimizing the period within the nonstationary range
  does not repair this approximation method. The certificate's power
  deficit is `alpha-166/325`, with supremal upper-edge deficit `76/325`.

The last lower bound is **not** a lower bound for the signed complementary
sum, for the complete centered remainder, or for the circle discrepancy.
No assertion is made that the low-period model is a good arithmetic
approximation. Its complementary error is precisely the obstruction being
tested. This is not the old outer-absolute divisor-CRT calculation: the
whole periodic model is first summed with its Fourier signs, and the new
failure occurs when its actual arithmetic complement is priced in L1.

## 2. Exact statements and hypotheses

Use the frozen real parameters and exact integer lengths

\[
b=83/650,\quad T\ge2,\quad T^{166/325}<N<T^{242/325},\quad
R\in[T/\sqrt2,\sqrt3T],
\]
\[
L=\max(2,\lceil N^{1/2}T^{-2b}\rceil),\qquad
K=\max(2,\lceil NT^{-4b}\rceil).
\]

Write `A=(0,h,k,h+k)`, with all four entries retained, and put

\[
\begin{split}
g(t)&=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\\
W_{h,k}(t)&=\prod_{s\in A}g(t+s),\\
\psi_{h,k}(t)&=\sqrt{t+h+k}-\sqrt{t+k}-\sqrt{t+h}+\sqrt t,\\
a_{h,k}(n)&=\prod_{s\in A}r_2(n+s),\qquad
F_{h,k,R}(t)=W_{h,k}(t)e(R\psi_{h,k}(t)),\\
D_{h,k}(R)&=\sum_n a_{h,k}(n)F_{h,k,R}(n),\qquad
I_{h,k}(R)=\int F_{h,k,R}(t)\,dt.
\end{split}                                                    \tag{1}
\]

The fixed real smooth mask `v` is nonzero, supported in `[1,4]`, and the
actual smooth mollifier transform has `Psi(0)=1`. All sums have the exact
zero extension and overlap `[N,4N-h-k]`. In particular
`W^(j)=O_j(N^(-j))`; signs of `W` are not changed in signed sums.
Set

\[
U=N^{3/2}/T,\quad \Lambda_{h,k}=hk/U,\quad
\Lambda_*=LK/U\asymp T^{76/325},\quad
\ell_{h,k}=N/(1+\Lambda_{h,k}),
\]
\[
\Omega=\{1\le h<L,\ 1\le k<K:\ h\ne k,\ \Lambda_{h,k}>1\}.
                                                               \tag{2}
\]

The bounded candidate `rho_loc` and the exact remainder
`E=D-rho_loc I` have their frozen meanings. No assertion that `rho_loc`
is an integer mean is added.

For a positive integer `q`, define the actual finite norm count

\[
\nu_q(r)=q^{-1}\#\{(x,y)\bmod q:x^2+y^2\equiv r\pmod q\},\qquad
B^{(q)}_{h,k}(n)=\pi^4\prod_{s\in A}\nu_q(n+s),
\]
\[
\mu^{(q)}_{h,k}=q^{-1}\sum_{r\bmod q}B^{(q)}_{h,k}(r).
                                                               \tag{3}
\]

This is a nonnegative, `q`-periodic model with all four norm factors,
not a truncated divisor identity for `a`. Its mean is exactly the finite
average displayed, not silently `rho_loc`.

**Lemma A (whole periodic model).** There is a fixed `c0>0`, depending only
on the masks and radius window, with the following property. Let `B` be
any nonnegative `q`-periodic sequence with finite mean
`mu=q^(-1)sum_(r mod q) B(r)`. If

\[
1\le q\le c_0\ell_{h,k},
                                                               \tag{4}
\]

then, for every fixed `A0>1`, uniformly for real `R` in the whole window,

\[
\left|\sum_n B(n)F_{h,k,R}(n)-\mu I_{h,k}(R)\right|
\ll_{A_0}\mu N(q/N)^{A_0}.
                                                               \tag{5}
\]

For (3), `0<=mu<=pi^4 tau(q)^4 <<_epsilon T^epsilon` when `q<=N`.
Choose any period satisfying (4), separately for each residual shift;
for large `T` such periods exist, since the smallest `ell` grows as a
positive power of `T`. The largest admissible period is
`floor(c0 ell)`, up to the harmless bounded-parameter convention.

Define the **complete** signed arithmetic complement

\[
J_{h,k}^{(q)}(R)=
\sum_n\bigl(a_{h,k}(n)-B^{(q)}_{h,k}(n)\bigr)F_{h,k,R}(n).
                                                               \tag{6}
\]

Lemma A and the proved smooth-model payment give

\[
\sup_R\frac1{LK}\sum_{\Omega}|E_{h,k}(R)-J_{h,k}^{(q)}(R)|
\ll_\epsilon T^{166/325+\epsilon}.
                                                               \tag{7}
\]

This is a quantitative model calculation, not a bound on (6).

**Lemma B (actual L1 approximation obstruction).** Fix
`166/325<alpha<242/325` and let `N=T^alpha`; the same statement holds for
`N/T^alpha` in a fixed compact positive interval. For each `(h,k) in Omega`
choose **any** nonnegative periodic sequence `B_(h,k)`, of any period
`1<=q_(h,k)<=c0 ell_(h,k)`. No correctness of its mean, lower bound on its
mean, or pointwise upper bound on it is assumed. Then, for all sufficiently
large `T`, uniformly over these choices,

\[
\boxed{\quad
\frac1{LK}\sum_{(h,k)\in\Omega}\sum_n
 |a_{h,k}(n)-B_{h,k}(n)|\,|W_{h,k}(n)|
\gg_\alpha \frac{N}{\log T}.
\quad}                                                        \tag{8}
\]

It applies in particular to the genuine norm models (3). It remains valid
if the models and periods are chosen after `R`; its proof has no `R`.
The no-go is for the positive certificate in (8), not for the modulus
after the complete signed sum (6). A signed or nonperiodic model lies
outside the statement.

## 3. Proof and derivation

### 3.1 Exact norm normalization and the untouched divisor arms

The normalization in (3) obeys `q^(-1)sum_(r mod q)nu_q(r)=1`, since there
are exactly `q^2` pairs `(x,y)` modulo `q`. CRT gives multiplicativity in
coprime moduli with precisely this normalization. For `q=p^m`, elementary
norm counting gives the following upper bounds, including the residue
zero.

At a split odd prime, the invertible change to `uv=r` gives
`nu_(p^m)(r)=(v_p(r)+1)(1-1/p)` when `v_p(r)<m`; at zero the value is
`1+m(1-1/p)`. Both are at most `m+1`. At an inert prime, nonzero residues
of even valuation have density `1+1/p`, those of odd valuation have zero
density, and the zero residue has density at most one. Again the upper
bound is `m+1`. At 2, the normalized counts are at most two. For example,
primitive unit norms have at most `2^(m+1)` representations; removing
factors of `1+i` gives the same bound for nonzero residues of higher
valuation. For the zero residue, both coordinates must be even once the
modulus is divisible by four, giving the recursion
`R_m(0)=4 R_(m-2)(0)` and normalized count one. The first two moduli also
satisfy the bound. Thus `nu_q(r)<=tau(q)` for every `q,r`.

Consequently the four-factor model and its mean are at most
`pi^4 tau(q)^4`, proving the asserted epsilon envelope. The real density
normalization is `pi^4`, for four norm coordinates; there is no lost
factor of `4^4` from an integer representation identity.

Indeed, if one wishes to display the exact arithmetic in (6), it is

\[
J_{h,k}^{(q)}(R)=\sum_n\left[
4^4\!\sum_{\substack{d_s\mid n+s\\s=0,h,k,h+k}}
     \prod_{s\in A}\chi_4(d_s)
-\pi^4\prod_{s\in A}\nu_q(n+s)\right]F_{h,k,R}(n).
                                                               \tag{9}
\]

Every divisor up to its actual argument, every character, every norm
factor, and every overlap point remains present. There is no small-arm
or large-arm discard. The periodic model is introduced by exact addition
and subtraction, not by claiming that a finite local product equals the
integer coefficient. The modulus in the sufficient signed target remains
outside each entire sum (9).

### 3.2 Finite Fourier expansion, all aliases, and the modulus threshold

For a nonnegative periodic `B` define

\[
\widehat B_q(a)=\frac1q\sum_{r\bmod q}B(r)e(-ar/q),\qquad
B(n)=\sum_{a\bmod q}\widehat B_q(a)e(an/q).
                                                               \tag{10}
\]

Then `hat B_q(0)=mu` and `|hat B_q(a)|<=mu`; there is no extra `q` in
these inequalities. With `hat F(xi)=int F(t)e(-xi t)dt`, Poisson summation
and the full finite expansion give the exact identity

\[
\sum_n B(n)F(n)
=\sum_{v\in\mathbb Z}\widehat B_q(-v\bmod q)\widehat F(v/q).
                                                               \tag{11}
\]

The term `v=0` is `mu I`. Nonzero multiples of `q` are still in (11);
discarding them would incorrectly identify a discrete constant model
with its integral.

Write `phi=R psi`. Direct differentiation of the square-root mixed
difference gives, for every `j>=1`,

\[
|\phi^{(j)}(t)|\ll_j \Lambda N^{-j}
                                                               \tag{12}
\]

on the support. Choose `c0` small enough that
`1/q >= 2 sup|phi'|` whenever (4) holds. For `v!=0`, the phase in
`hat F(v/q)` therefore has derivative separated from zero by a constant
times `|v|/q`. Rescale `t=Nx`; its large frequency is `N|v|/q`, and all
derivatives of the normalized phase are bounded because
`Lambda q/(N|v|)<=c0`. Repeated integration by parts, with smooth exterior
boundaries, yields

\[
|\widehat F(v/q)|\ll_{A_0}
N\left(\frac{q}{N|v|}\right)^{A_0}.
                                                               \tag{13}
\]

Summing the convergent `v` series in (11) proves (5). Thus actual Fourier
signs have been retained until the whole nonstationary sum is estimated.
For periods comparable to or larger than `ell`, some nonzero aliases
can fall in the phase derivative range. Estimate (13) is then not
licensed; a stationary-phase or cancellation argument would be additional
work. This report does not assert that larger periods are impossible.

### 3.3 Complete model cost and the exact complementary target

For any choices (4), the exact algebra is

\[
E_{h,k}=J_{h,k}^{(q)}+
\left(\sum_n B^{(q)}_{h,k}(n)F(n)-\mu^{(q)}_{h,k}I_{h,k}\right)
+(\mu^{(q)}_{h,k}-\rho^{\rm loc}_{h,k})I_{h,k}.
                                                               \tag{14}
\]

Neither of the last two terms is omitted. Smooth nonstationary integration
also gives `|I|<<_A N(1+Lambda)^(-A)`. The actual norm-model mean and
`rho_loc` are both `O(T^epsilon)`, without any claim they are close.
For `A>1`, the full product count implies

\[
\frac1{LK}\sum_{\Omega}(1+\Lambda_{h,k})^{-A}
\ll \frac{\log(2L)\log(2+\Lambda_*)}{\Lambda_*}.
                                                               \tag{15}
\]

For clarity, dyadic shells `2^j<Lambda<=2^(j+1)` have cardinality at most
`C U 2^j log(2L)`, capped by `LK`. Multiplying by `2^(-Aj)` and summing
proves (15); its extra displayed logarithm is harmless. Empty shells and
exact power-of-two endpoints obey the stated half-open convention.

Using (5), (4), and (15) in (14) gives

\[
\frac1{LK}\sum_{\Omega}|E_{h,k}-J_{h,k}^{(q)}|
\ll_\epsilon T^\epsilon\frac N{\Lambda_*}
\asymp T^\epsilon NT^{-76/325}
\le T^{166/325+\epsilon},
                                                               \tag{16}
\]

with logarithms absorbed. This pays the entire finite-model oscillation
and its entire mean mismatch, not an assumed approximation error between
two Euler products. The smallest common-scale `ell` is at least a
constant times `T^(90/325)`, so bounded `T` can be separated harmlessly.

The originally paid sectors also remain priced: `h=k` costs
`T^epsilon N/K<=T^(166/325+epsilon)`, and `hk<=U` costs
`T^epsilon N U log(2L)/(LK)<=T^(166/325+epsilon)`.
No such sector is reintroduced as an unpriced model exception.

It follows that a target-sized bound for the complete average of
`|J^(q)|` would suffice. It has not been proved. The elementary upper bound
for its coefficientwise absolute certificate is `NT^epsilon`, exactly
the old exponent. Lemma B now proves that such a certificate cannot
possibly have a fixed power improvement to the requested target.

### 3.4 One primary theorem audit: finding a small omitted inert prime

The sole external theorem used is K. S. Kedlaya, *Notes on analytic number
theory*, [Chapter 4, Theorem 4.12 and its proof](https://kskedlaya.org/ant/chap-primes-in-ap.html),
inspected 2026-09-28. Its fixed coprime progression specialization is
`sum_(p<=x,p=3 mod4) log p ~ x/2`. The webpage's theorem header omits
`=1` after its gcd expression; Definition 4.1 and the proof explicitly
state coprimality. Our only specialization is `(3,4)`, which satisfies it.
No rate, short interval theorem, or uniformity in a growing progression
modulus is used. The unrelated periodic-model modulus `q` is not the
modulus in this theorem.

Here is the consequence, with its quantifiers explicit:

\[
\text{for every integer }q\ge1\text{, some prime }p\equiv3\pmod4
\text{ satisfies }p\nmid q,\quad p\le C\log(q+2).
                                                               \tag{17}
\]

To prove it, let `theta_3(x)=sum_(p<=x,p=3 mod4)log p`. The source gives
an absolute `x0` such that `theta_3(x)>=x/3` for `x>=x0`. Put
`x=max(x0,6 log(q+2))`. If all those primes divided `q`, their product
would divide `q`, giving `log q>=theta_3(x)>=x/3>=2 log(q+2)`, a
contradiction. Enlarging an absolute constant absorbs `x0` into
`C log(q+2)`. An explicit numerical value of `C` is not needed for the
asymptotic statement. This does not use a false claim that the first
prime outside a general period is bounded independently of that period.

### 3.5 Actual coefficient zeros and exact finite-period error

For an inert odd prime `p`, if `p` divides `x^2+y^2`, then `p` divides both
coordinates; hence a norm cannot have valuation exactly one at `p`.
Therefore

\[
v_p(n)=1\quad\Longrightarrow\quad r_2(n)=0
\quad\Longrightarrow\quad a_{h,k}(n)=0
                                                               \tag{18}
\]

for every shift pair, with the other three original factors untouched.

Let `B` be any nonnegative `q`-periodic sequence, of mean `mu`, and let
`p` be as in (17). For every real interval `J=(u,v]` of length `H`, CRT
counts each pair of residues modulo `q` and modulo `p^2` once modulo
`q p^2`. The condition `v_p(n)=1` consists of the `p-1` residue classes
`jp mod p^2`, `1<=j<p`. Counting every real-endpoint progression with
error at most one gives the exact estimate

\[
\sum_{\substack{n\in J\\v_p(n)=1}}B(n)
=H\mu\frac{p-1}{p^2}+O(pq\mu).
                                                               \tag{19}
\]

No maximum value of `B` is used: after summing residues the error is
`O(p sum_(r mod q)B(r))=O(pq mu)`. Positivity is essential. In particular,
if `q p^2` is sufficiently small relative to `H`, the left side is at
least `c H mu/p`. This is an actual lower estimate for model mass where
the true coefficients vanish, not a lower estimate inferred from a
failed upper error bound.

### 3.6 Surviving actual mass and the complete L1 dichotomy

Put `M_(h,k)=sum_n a_(h,k)(n)|W_(h,k)(n)|`. The permitted Round-212
oscillatory report proves, at each fixed interior scale,

\[
\sum_{(h,k)\in\Omega}M_{h,k}\ge c LKN.                         \tag{20}
\]

Its short proof uses the actual sequence `u_n=r2(n)|g(n)|`, whose total
is comparable to `N` by elementary disk-area counting, and whose maximum
is `N^epsilon`. The moving-sum Cauchy identity for a nonnegative sequence
supported on `O(N)` indices is

\[
\sum_n u_n^2+2\sum_{h=1}^{L-1}(1-h/L)\sum_nu_nu_{n+h}
\ge c\frac L N\left(\sum_nu_n\right)^2.
                                                               \tag{21}
\]

Apply its `K` version to `u_nu_(n+h)` and sum in `h`. Cauchy in `h`
gives total four-point mass `>=c LKN`; the two displayed diagonals cost
`O(N^(1+epsilon))` and `O(LN^(1+epsilon))`, respectively, and are smaller
because `L,K` grow by fixed powers. Removing `h=k` and `hk<=U` costs
`O(N^(1+epsilon)[L+U log(2L)])=o(LKN)`. This reproduces why (20) is an
actual mass result and uses no four-point density assumption.

For the lower-certificate argument only, restrict further to

\[
\Omega_{\rm hi}=\{(h,k)\in\Omega:\Lambda_{h,k}>\Lambda_*^{1/2}\}.
                                                               \tag{22}
\]

The additional removed mass is at most
`C NT^epsilon U Lambda_*^(1/2)log(2L)`.
Relative to `LKN` this is
`O(T^epsilon Lambda_*^(-1/2)log(2L))=o(1)` with a sufficiently small
fixed epsilon. Thus

\[
\sum_{\Omega_{\rm hi}}M_{h,k}\ge c_1 LKN.                    \tag{23}
\]

This subfamily is used solely to lower-bound a positive certificate.
It is not substituted for the full upper target; (14)--(16) still retain
every pair in `Omega`.

On `Omega_hi`, any period (4) obeys

\[
q\ll N\Lambda_*^{-1/2},\qquad
p\ll\log N,\qquad
q p^2/N\ll\Lambda_*^{-1/2}(\log N)^2=o(1).                    \tag{24}
\]

Choose a fixed closed interval in `(1,4)` on which `|v|` is bounded below,
and then a smaller interval `J=N[a,b]` of length comparable to `N`.
Because `h+k=o(N)`, `N/T->0`, and `Psi(0)=1`, for all shifts and large `T`

\[
|W_{h,k}(n)|\ge c_2\quad(n\in J).                            \tag{25}
\]

The constants are uniform over the shifts and the models. Equations
(18)--(19), (24), and (25) give, for each high pair,

\[
Z_{h,k}:=\sum_n|a_{h,k}(n)-B_{h,k}(n)|\,|W_{h,k}(n)|
\ge c_3 N\mu_{h,k}/p_{h,k}
\ge \frac{c_4 N}{\log T}\mu_{h,k}.                           \tag{26}
\]

There is also a uniform upper bound for total model mass on the complete
support, using periodicity, positivity and `|W|<=C`:

\[
\sum_nB_{h,k}(n)|W_{h,k}(n)|
\le C_1(N+q)\mu_{h,k}\le C_2N\mu_{h,k}.                     \tag{27}
\]

Let `S_mu=sum_(Omega_hi)mu_(h,k)`. If
`S_mu <= c1 LK/(2C2)`, the pointwise triangle inequality, (23), and (27)
give

\[
\sum_{\Omega_{\rm hi}}Z_{h,k}
\ge\sum_{\Omega_{\rm hi}}M_{h,k}-C_2NS_\mu
\ge(c_1/2)LKN.
                                                               \tag{28}
\]

If `S_mu` is larger, summing (26) instead gives
`sum_(Omega_hi)Z_(h,k)>=c LKN/log T`. This proves (8) in both cases,
including zero models and arbitrarily large model means. It does not
assume that a candidate density is positive on any prescribed fiber.

### 3.7 Quantitative stopping point and preserved scope

At `N=T^alpha`, the ratio of the lower certificate (8) to the target
power is at least a constant times

\[
\frac{T^{\alpha-166/325}}{\log T}.                            \tag{29}
\]

It diverges by a fixed power at every fixed interior scale after choosing
epsilon smaller than `alpha-166/325`. The supremal deficit is
`(242-166)/325=76/325`; the open upper endpoint is not asserted attained.
The period can vary with both shifts and radius, including choosing the
largest period allowed by (4); (8) is uniform over all such choices.

Thus the concrete model calculation (16) is fully paid, but the actual
complement cannot be paid by taking coefficientwise absolute values.
The next mathematical input would have to estimate the complete signed
sum (9), use cancellation among missing local constraints, or leave the
nonstationary period regime with a separately proved estimate. None is
provided here. In particular an unevaluated Fourier or norm transform is
not reported as a gain.

Even a successful bound for (6) in this frozen setting would concern the
inherited `102/325` milestone. It is not the full quarter theorem and
does not close any independent M1, M2, endpoint, GAR-complement or original
signed tenth-moment gate.

## 4. First doubtful or unproved step

The first unproved sufficient assertion is

\[
\sup_R\frac1{LK}\sum_{(h,k)\in\Omega}
\left|\sum_n(a_{h,k}(n)-B^{(q)}_{h,k}(n))
 W_{h,k}(n)e(R\psi_{h,k}(n))\right|
\ll_\epsilon T^{166/325+\epsilon}.                           \tag{30}
\]

Replacing its complete inner modulus by the positive certificate (8)
is a rigorously refuted route to (30). The actual signed statement (30)
has not been refuted. Periods beyond (4), signed periodic models,
nonperiodic models, and genuine signed arithmetic dispersion are outside
the no-go. No source asserts (30), no finite-local mean is identified
with `rho_loc`, and no mean mismatch is declared negligible without its
payment in (16).

The only imported theorem's specialization is audited in Section 3.4.
Its role is the modest prime-size assertion (17), not a shifted-correlation
theorem. There is no repetition of the invalid fixed-shift Matthiesen
application.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `actual_four_point_coefficients` | PASS for the stated lemmas. Equation (9) retains all original divisor arms and characters. Actual norm zeros (18) and the actual mass derivation (20)--(23) prove the obstruction; no adversarial coefficient surrogate is used. |
| `complete_shifts_overlap` | PASS. Equations (14)--(16) keep every residual pair, all four factors, and all zero-extended overlap. Both original safe sectors remain paid. The high-product subset is used only for a lower certificate. |
| `local_global_discrepancy` | PASS as a distinction. No integer discrepancy theorem is assumed. CRT formula (19) is for the explicitly periodic model and includes its `O(pq mu)` error; it is not a short-interval theorem for `a`. |
| `density_hypotheses` | PASS. The finite mean is exactly (3), its size is proved, and its difference from the bounded candidate is retained in (14). The lower bound uses a mean-size dichotomy, not a presumed lower local density. |
| `real_endpoints` | PASS. Poisson uses the full smooth zero extension. The integer CRT count is valid on any real half-open interval with unit endpoint error. Large-T fixed-interior scope is explicit for the lower certificate. |
| `all_restored_powers` | PASS. Model cost is `N/Lambda_*<=T^(166/325)`. The complete certificate is `>=cN/log T`, with deficit (29). The excluded-prime error satisfies (24); no growing-modulus prime theorem is invoked. |
| `signed_absolute_distinction` | PASS. (30) remains signed inside each complete sum. The only refuted object is (8); it does not lower-bound (30), E, D, or circle discrepancy. |
| `full_quarter_scope` | PASS. No complete centered estimate, moment improvement, pointwise exponent, M1/M2 closure, or quarter theorem is claimed. |
| `statement_only_control` | NOT CLAIMED by this discovery task. No sibling or isolated packet was read. Fourier normalization, the CRT lower estimate and the mass dichotomy require the conductor's independent same-round seam. |

Additional exact controls: `q=1` retains all integer Poisson aliases and
uses the prime 3 in (18); a zero-mean nonnegative model is identically zero
and falls in (28); a very large model mean falls in (26); the known
modulo-4 zero shift sector needs no deletion; repeated shifts are paid
before constructing the distinct-shift remainder. The finite models need
not reproduce every actual zero sector, because their exact complementary
error is never dropped. All controls are analytical; no experiment or
asymptotic extrapolation was performed.

## 6. Dependencies and exact artifacts used

Only the assigned brief, the following permitted local files, and the
single primary source in Section 3.4 were read. The authoritative graph
was read at its preamble and the relevant nodes `GC-target`, `M9-M1`,
`M9-M2`, `Divisor-bound-elementary`, and
`GC-complete-square-root-large-values-moment-bound`. Historical paths
merely cited by those artifacts were not opened.

| Artifact | SHA-256 at inspection |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71` |
| `state/active_campaign.yml` | `b5affd6815848adda7748b40be7bf0e20c09c814db65851cba564370c1953b3b` |
| `strategy/round213_complete_centered_arithmetic_attack.md` | `d81a7690d27968f1843b4a2d3efb6c6b8b4cc483f83ff56e910c3d27acf89aae` |
| `rounds/codex-managed/gc-complete-four-point-correlation/synthesis.md` | `5ae97f52664c3da3c938031785bd743e820956b49810e82e0e7a1ab1056a780b` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_local_arithmetic.md` | `6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md` | `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f` |
| `rounds/codex-managed/gc-complete-centered-arithmetic/briefs/centered_divisor_attack.md` | `298a48fe59d9a96bd27ab9cdfef0fc7b4e950062b697356be2cefb7b2fde66ec` |

The local-arithmetic report supplies the bounded distinct-shift candidate,
its real/local normalization and the smooth integral cost. The oscillatory
report supplies the actual mass result and finite moving-sum proof
reproduced in Section 3.6. The frozen strategy supplies the exact complete
target and scope. The finite norm-model Fourier estimate, its complete
cost, omitted-prime CRT calculation, and mean-size dichotomy are derived
here.

The conductor was sent the periodic-model plan, the normalized Poisson
bound, and the actual approximation obstruction during work. The conductor
independently suggested the same omitted-inert-prime control while it was
being developed; that suggestion was not treated as proof. No sibling
content was received or read. This discovery report is not a blind report.

## 7. Recommended state effect

**Retain**, after independent seam review, Lemma A and the actual scoped
L1 approximation obstruction Lemma B as strategy evidence. **Reject** the
specific claim that a nonnegative periodic model with
`q<=c0 N/(1+Lambda)` can be completed by a target-sized coefficientwise
absolute approximation estimate. This rejection applies uniformly across
all choices within that stated model class.

**No change** to the accepted arithmetic target, exponents, moments, proof
draft, or independent analytic parents. The appropriate bounded-task exit
is `scoped_centered_certificate_obstruction`, while the actual complete
signed remainder remains open. Only this assigned report was written.
No shared-state mutation, synthesis edit, blind/sibling edit, successor
design or legacy modification was made. Stop after this report, subject
only to a conductor-directed same-round seam.

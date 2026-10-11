# Round 213 independent periodic-model seam review

Campaign: `gc-complete-centered-arithmetic`. Role: independent seam reviewer,
NONBLIND. Generated: 2026-09-28. Analytical review; zero experiments.
Claimant artifact:
`rounds/codex-managed/gc-complete-centered-arithmetic/reports/centered_divisor_attack.md`.
Final claimant SHA-256:
`7f826451cb58b578e93c5b4e471eb3ccdc0cda60276fc60551695a1d80e3407e`.
Starting graph hash, supplied in the claimant metadata:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.

## 1. Result and verdict

**GREEN at the bound claimant hash. No mathematical repair is required.**

The finite Fourier/Poisson calculation has the correct normalization and
retains every alias. The finite norm model has the claimed divisor-size
upper envelope, including zero residues and powers of 2. Its complete
oscillatory contribution and its mean mismatch are paid without asserting
that the mean approximates the infinite local candidate.

The omitted-inert-prime argument proves the stated actual coefficientwise
L1 obstruction uniformly over nonnegative periodic models in the period
range. The fixed-progression source supplies exactly the needed small
omitted prime; the CRT error, mask interval, surviving high-shell mass,
and mean-size dichotomy all have their required costs. This validates a
scoped obstruction to an absolute approximation certificate. It validates
no bound for the signed complementary sum or the full target.

## 2. Exact reviewed statement and hypotheses

The claimant uses `b=83/650`, real `T>=2`,
`T^(166/325)<N<T^(242/325)`, the exact rounded `L,K`, the actual four
`r2` factors, and the actual real smooth mask product `W`. The complete
residual set is `Omega={h!=k, Lambda=Thk/N^(3/2)>1}` within the original
shift rectangle, and `ell=N/(1+Lambda)`.

The two assertions checked are:

1. For every nonnegative `q`-periodic sequence `B`, mean
   `mu=q^(-1)sum_(r mod q)B(r)`, and `q<=c0 ell`,
   `|sum B(n)F(n)-mu integral F| <<_A mu N(q/N)^A` for fixed `A>1`.
   For the specific finite norm model, its mean is `O(T^epsilon)`,
   so its entire contribution and mean mismatch have complete average
   cost `O(T^(166/325+epsilon))`.
2. At every fixed interior power scale `N asymp T^alpha`, uniformly
   over arbitrary families of nonnegative periodic `B_(h,k)` with
   `q_(h,k)<=c0 ell_(h,k)`,

   \[
   \frac1{LK}\sum_{\Omega}\sum_n
     |a_{h,k}(n)-B_{h,k}(n)|\,|W_{h,k}(n)|
       \gg_\alpha N/\log T.
   \]

The second assertion requires neither a bounded mean nor a pointwise
upper bound on the arbitrary model. Positivity and periodicity are
essential to its proof. It is not an assertion about the modulus of
the complete signed sum. The upper calculation is uniform in the
real radius window; the lower certificate has no radius parameter.

## 3. Independent derivation and seam checks

### 3.1 Fourier normalization and all Poisson aliases

With `hat B_q(a)=q^(-1)sum_r B(r)e(-ar/q)`, finite inversion gives
`B(n)=sum_(a mod q)hat B_q(a)e(an/q)`. In particular,
`hat B_q(0)=mu` and `|hat B_q(a)|<=mu`. For
`hat F(xi)=integral F(t)e(-xi t)dt`, ordinary Poisson gives

\[
 \sum_n F(n)e(an/q)=\sum_{m\in\mathbb Z}\widehat F(m-a/q).
\]

The change of variables `v=qm-a` is a bijection between the pairs
`(a mod q,m)` and integers `v`, with `a=-v mod q`. Hence

\[
 \sum_nB(n)F(n)=\sum_{v\in\mathbb Z}
            \widehat B_q(-v\bmod q)\widehat F(v/q).
\]

There is no missing factor `q` or `1/q`. In particular the nonzero
multiples of `q` remain. Even for `q=1`, the answer is not just the
integral: all integer Fourier aliases remain in the error.

Let `phi=R psi`. On the actual support,
`|phi^(r)|<<_r Lambda N^(-r)`. The condition
`q<=c0 N/(1+Lambda)` with sufficiently small fixed `c0` ensures
`|phi'(t)-v/q|>=c|v|/q` for every nonzero integer `v`.
After `t=Nx`, put `lambda=N|v|/q`. The normalized phase has first
derivative bounded away from zero and all higher derivatives bounded,
uniformly in `v,h,k,R`. Smooth integration by parts therefore gives
`|hat F(v/q)|<<_A N lambda^(-A)`. Summing `|v|^(-A)` for `A>1`
proves Lemma A with no hidden period loss. Every integration boundary
is a smooth zero-extension boundary.

### 3.2 Finite norm counts, including singular residues

For `nu_q(r)=q^(-1)# {(x,y) mod q: x^2+y^2=r}`, summing over `r`
gives average one, and CRT is multiplicative with this normalization.
At a split odd prime power, the change to `uv=r` gives density
`(v_p(r)+1)(1-1/p)` off zero and `1+m(1-1/p)` at zero modulo `p^m`.
Both are at most `m+1`.

At an inert prime power, a nonzero represented residue has even
valuation and density `1+1/p`. For zero, the coordinates are both
divisible by `p^ceil(m/2)`, giving density
`p^(2 floor(m/2)-m)<=1`. Thus the same `m+1` bound holds.

For completeness, the 2-adic bound at most two can be checked without
an asymptotic density formula. For an odd right-hand side and `m>=3`,
one coordinate is odd and the other even. Of the even choices, at most
`2^(m-2)` have the required residue modulo 8; each permits at most four
odd square roots. Both orientations together give at most `2^(m+1)`
representations. For right-hand side divisible by four, both coordinates
are even and `R_m(r)=4 R_(m-2)(r/4)`. For valuation one, multiplication
by `1+i` gives `R_m(2u)=2 R_(m-1)(u)` for odd `u`. These reduce to the
odd case or the first two moduli. The zero-residue recurrence gives
normalized count one. Therefore `nu_(2^m)<=2<=m+1` for `m>=1`.

It follows that `nu_q(r)<=tau(q)` for every residue, so both the genuine
four-factor model and its mean are at most `pi^4 tau(q)^4`. The usual
elementary divisor envelope supplies `T^epsilon` for `q<=N`. The
claimant retains the separate integer representation normalization
`4^4` in its exact divisor expansion; `pi^4` belongs only to the model.

### 3.3 Complete model and mean-mismatch payment

The decomposition into the signed complement, the finite-model
oscillatory error, and `(mu-rho_loc)I` is exact. Both means have a
`T^epsilon` bound, which does not say they are close. Lemma A and
`q/N<=c0/(1+Lambda)` price the first error by
`T^epsilon N(1+Lambda)^(-A)`. The same envelope prices the mismatch,
using smooth nonstationary integration for `I`.

The complete product-shell count is at most
`C U 2^j log(2L)`, with `U=N^(3/2)/T`. Thus summing the preceding
decay over all `Lambda>1`, including exact integer endpoints, costs
at most `T^epsilon N/Lambda_*`. As
`Lambda_*=LK/U asymp T^(76/325)`, the upper-band exponent is
`(242-76)/325=166/325`. No mean approximation or omitted residue
class is needed for that payment. The original repeated and small
product sectors retain their separately displayed safe prices.

### 3.4 Source audit and the omitted prime

I independently opened [Kedlaya, Chapter 4, Theorem 4.12 and proof](https://kskedlaya.org/ant/chap-primes-in-ap.html).
Definition 4.1 and the proof explicitly require coprimality; the
theorem header has the reported incomplete gcd expression. The proof
states the logarithmically weighted prime asymptotic for a fixed
coprime progression. Specializing to `(3,4)` gives
`theta_3(x)~x/2`. This is the only external theorem used. No growing
progression modulus, explicit rate, or short interval is required.

The claimed consequence follows directly: for all sufficiently large
`x`, `theta_3(x)>=x/3`. Set
`x=max(x0,6 log(q+2))`. If every inert prime at most `x` divided `q`,
their product would divide `q`, forcing
`log q>=theta_3(x)>=2 log(q+2)`, a contradiction. Absorb fixed `x0`
into the constant to obtain an omitted inert prime
`p<=C log(q+2)`. The model period `q` does not replace the fixed
progression modulus 4 in the source theorem.

### 3.5 CRT, masks, and actual high-shell mass

For an inert odd prime, a sum of two squares divisible by `p` has
both coordinates divisible by `p`; hence `v_p(n)=1` implies the actual
four-point coefficient is zero. Because `p` does not divide `q`,
each pair `r mod q` and `jp mod p^2`, `1<=j<p`, defines one
progression modulo `qp^2`. For a real half-open interval of length `H`,
its count is `H/(qp^2)+O(1)`. Weighted summation therefore gives

\[
 \sum_{n\in J,\,v_p(n)=1}B(n)
 =H\mu\frac{p-1}{p^2}+O(pq\mu).
\]

The error is the sum of `B(r)` over residues, not `max B` times an
uncontrolled count. Relative to the main term its size is
`O(qp^2/H)`. The claimant correctly checks this stronger ratio, not
just `q p/H`.

On `Omega_hi={Lambda>Lambda_*^(1/2)}`, the period condition and the
source consequence imply
`q p^2/N << Lambda_*^(-1/2)(log N)^2=o(1)`, uniformly over models.
There is a common interval of length comparable to `N` on which
`|W|` is bounded below: take a smaller interval inside one where
`|v|>c`, use `h+k=o(N)`, `N/T->0`, and `Psi(0)=1`. This handles
arbitrary original mask signs and keeps the interval in the actual
four-factor overlap. The zero-set model mass on that interval gives
`Z_(h,k)>=c N mu_(h,k)/log T`.

I checked the inherited actual mass proof in the permitted Round-212
report. Its two moving-sum inequalities applied to
`u_n=r2(n)|g(n)|`, together with `sum u_n asymp N`, give total mass
`>=cLKN`; the diagonals are smaller at fixed interior scales.
Removing the original paid sectors costs `o(LKN)`. Removing additionally
`Lambda<=Lambda_*^(1/2)` costs at most
`N T^epsilon U Lambda_*^(1/2)log(2L)=o(LKN)`. Thus the claimed
high-shell mass survives. The subset is used only to lower-bound a
nonnegative certificate, not to replace the full upper target.

Finally, positivity and periodicity give complete model mass
`<=C(N+q)mu<=C'Nmu`. If the sum of high-shell means is small, triangle
inequality against the surviving actual mass gives `sum Z>=cLKN`.
If it is large, the CRT zero-set estimate gives
`sum Z>=cLKN/log T`. These cases cover zero models, unbounded means,
and choices depending on both shifts or radius, with constants
independent of those choices. The lower certificate and its stated
power deficit follow.

## 4. First doubtful or unproved step

No unproved step remains in the reviewed finite-model calculation or
its stated L1 no-go. The first unproved sufficient assertion is still
the claimant's equation (30): a target-sized average of the moduli of
the complete signed complementary sums. The L1 obstruction does not
refute that signed estimate.

Periods outside the small nonstationary range may create stationary
aliases and require additional arguments. Signed or nonperiodic models
are outside the stated no-go. Nothing reviewed establishes that the
finite or infinite local means match an actual arithmetic mean.

## 5. Controls and outcomes

| Seam/control | Verdict |
|---|---|
| Normalized finite Fourier/Poisson | GREEN: exact bijection `v=qm-a`; all aliases and constant-mode integer aliases retained; no period multiplier. |
| Finite norm envelope | GREEN: all prime powers, zero residues, and the prime 2 checked; multiplicative normalization preserved. |
| Prime-size source hypothesis | GREEN: fixed coprime progression `(3,4)` only; the omitted prime has logarithmic size by the displayed product argument. |
| Real-endpoint CRT error | GREEN: `O(pq mu)` and the required `qp^2/N=o(1)` are both correct. |
| Actual arithmetic and masks | GREEN: true inert-prime zeros; common interior interval; all four factors and mask signs retained. |
| Complete shifts and mass subtraction | GREEN: upper calculation covers all residual shifts; high-shell restriction is only for a lower positive certificate. |
| Means and approximation | GREEN: arbitrary means handled by a dichotomy; finite/infinite means are never identified. |
| Restored powers | GREEN: model cost at most `166/325`; lower certificate `N/log T`; fixed-interior deficit `alpha-166/325`. |
| Signed/absolute and full-goal scope | GREEN: signed complementary target remains open; no pointwise exponent, moment, M1/M2, endpoint, or quarter promotion. |
| Independence | NONBLIND seam as assigned; no current blind, conductor, shared-state, synthesis, or successor file accessed. |

No numerical control is needed for these finite identities and
inequalities, and none was run.

## 6. Dependencies and final hash bindings

This review read only the assigned documents and precise primary page:

| Artifact | SHA-256 or exact source |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-complete-centered-arithmetic/reports/centered_divisor_attack.md` | `7f826451cb58b578e93c5b4e471eb3ccdc0cda60276fc60551695a1d80e3407e` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md` | `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f` |
| Kedlaya, *Notes on analytic number theory*, Chapter 4 | `https://kskedlaya.org/ant/chap-primes-in-ap.html`, Theorem 4.12, proof, and Definition 4.1; inspected 2026-09-28. |

The verdict is bound to the exact claimant hash above. The separate
completed shell discovery report was preserved without edits and is
not a dependency of this review. No child source links or historical
artifacts beyond the permitted mass report were opened.

## 7. Recommended state effect

Accept this seam as **GREEN** for the finite periodic-model lemma and
the precise actual L1 obstruction, at the bound hash. Retain them as
reviewed strategy evidence; reject completion of this model route by
a target-sized coefficientwise absolute approximation certificate.
Do not promote the signed remainder or any analytic parent.

Only this review file was written. No claimant, discovery, shared-state,
synthesis, validation, blind, conductor, legacy, or successor artifact
was modified. This review stops here.

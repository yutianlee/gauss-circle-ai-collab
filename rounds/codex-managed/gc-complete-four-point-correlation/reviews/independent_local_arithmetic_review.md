# Round 212 independent local-arithmetic seam review

## 1. Result and final-hash verdict

**GREEN for the claimant's scoped local-factor lemmas, conditional local
transfer, and specified source obstruction. No repair is required.**
The actual power-saving discrepancy hypothesis remains open.

Campaign: `gc-complete-four-point-correlation`; round: 212.
Role: separate **NONBLIND** seam reviewer, following completion of the
oscillatory-attack discovery task. Generated: 2026-09-28.
Effort: entirely analytical; no mathematical experiment.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.

Reviewed claimant:
`rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_local_arithmetic.md`.

Final SHA-256:
**`6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e`**.

The exact odd-prime formulas, the ramified-prime obstruction, the bounded
distinct-shift candidate product and the repeated-root divergence check.
The latter concerns the proposed local product only; no integer mean is
deduced from it. The local-error exponent threshold is exactly `45/83`,
and its square-root case costs `T^(159/325+epsilon)` before adding the
already paid main terms and repeated shifts.

## 2. Exact hypotheses and review boundary

Use the claimant's original coefficients, real parameters and masks:

\[
 b=83/650,\quad T^{4b}<N<T^{1-2b},\quad
 L=\max(2,\lceil\sqrt N T^{-2b}\rceil),\quad
 K=\max(2,\lceil NT^{-4b}\rceil),
\]
\[
 a_{h,k}(n)=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k),\quad
 \Lambda_{h,k}=Thk/N^{3/2},\quad
 \ell_{h,k}=N/(1+\Lambda_{h,k}).
\tag{R1}
\]

The full raw amplitude is the product of the four real size-one smooth
factors, with its exact zero-extended support. Its derivatives satisfy
`W^(j)=O_j(N^(-j))`. The phase is the actual square-root second
difference multiplied by `R`, for every `R` in the supplied real window.

For each nonzero `z in Z_p`, the local norm density is the stabilized
limit of the number of solutions to `x^2+y^2=z mod p^m`, divided by
`p^m`. Denote it by `lambda_p(z)`. The claimant uses

\[
 \beta_p(h,k)=\int_{\mathbb Z_p}
       \lambda_p(x)\lambda_p(x+h)\lambda_p(x+k)
                        \lambda_p(x+h+k)\,dx,
\tag{R2}
\]

with multiplicities intact. For distinct shifts the proposed constant is
`rho_(h,k)^loc=pi^4 product_p beta_p(h,k)`.

The local input `H(theta)` asserts an error at most
`T^epsilon ell_(h,k)^theta` on **every** real subinterval of length at
most `ell_(h,k)`, after subtracting this proposed density. The error
uses the cell scale even for shorter subintervals. Uniformity in both
real endpoints, all distinct shifts, and all required parameters is part
of the hypothesis. It includes the unproved assertion that this local
candidate is an appropriate mean at that accuracy.

Only the assigned claimant, the protocol, and the specified original
versioned primary theorem were used for this new review. No blind or
conductor-ledger file was opened. This is not a statement-only review.

## 3. Independent derivations and seam checks

### A. The actual local norm densities

Put `q=1/p`, `chi=chi_4(p)` for odd primes. I obtain

\[
 \lambda_p(z)=(1-\chi q)F(v_p(z)),\qquad
 F(v)=\sum_{j=0}^v\chi^j.
\tag{R3}
\]

For a split prime, the invertible coordinate change to `uv=z` is valid
modulo every power of `p`. If `v_p(z)=v<m`, each of the `v+1` possible
valuations of `u` contributes `(p-1)p^(m-1)` pairs. Dividing by `p^m`
gives `(1-q)(v+1)`.

For an inert prime, a unit norm has `p+1` solutions modulo `p`, each
lifting with a factor `p` at every subsequent level. An odd valuation
cannot be a norm. If the valuation is `2j`, removing `p^j` from both
coordinates leaves a unit norm modulo `p^(m-2j)`; the omitted coordinate
digits supply `p^(2j)`, so the normalized count remains `1+q`.

At the prime 2, for odd `z` congruent to 1 modulo 4 and `m>=3`, count
first the solutions with the first coordinate odd. The even coordinate
must occupy one fixed residue class modulo 4, determined by `z mod 8`.
There are `2^(m-2)` choices, and each complementary odd square has four
roots modulo `2^m`. Interchanging the coordinate parities doubles this
to `2^(m+1)`. The count vanishes for `z=3 mod 4`.

For a norm divisible by 4, both coordinates are even, and the exact
count is four times the count for `z/4` at modulus `2^(m-2)`.
For valuation one, both coordinates are odd; the transformation
`(x,y)=(u+v,u-v)` reduces the norm by a factor of 2 and gives twice
the count at modulus `2^(m-1)`. These relations preserve normalized
counts. Hence

\[
 \lambda_2(z)=2\,1_{\{\text{odd part of }z=1\pmod4\}}.
\tag{R4}
\]

This independently verifies the claimant's normalization, including
nonprimitive representations. The finitely many translated zero points
have Haar measure zero. For the real normalization, the area of a norm
disk is `pi t`, so the proposed four-coordinate real factor is `pi^4`.
This normalization calculation does not itself prove a global asymptotic.

### B. Distinct roots, bad-prime control and the exact zero sector

Let `Delta=hk(h-k)(h+k)`, which is nonzero for positive distinct shifts.
For odd `p` not dividing `Delta`, the four roots are distinct modulo `p`.
With valuation distribution `P(V=v)=(1-q)q^v`, direct summation gives
`E F(V)=1/(1-chi q)`. At each of the four root residue classes only
one factor changes from its unit value. Consequently

\[
 \begin{split}
 \beta_p&=(1-\chi q)^4
           \left(1+4\left[\frac1{1-\chi q}-1\right]\right)\\
        &=(1-\chi q)^3(1+3\chi q)
         =1-6q^2+8\chi q^3-3q^4.
 \end{split}
\tag{R5}
\]

There is no extra factor `q` in the bracket: the difference between
the unconditional expectation and one already includes the root
residue-class probability. The good-prime tail is therefore absolutely
convergent. Four distinct residues cannot occur modulo 3, so the formal
zero obtained by inserting that impossible good-prime configuration
does not create a spurious actual obstruction.

For any bad odd prime, Holder and translation invariance give
`beta_p<=int lambda_p(x)^4 dx`. The two moments are

\[
 \begin{split}
 \chi=1:&\quad (1-q)^5\sum_{v\ge0}(v+1)^4q^v
                         =1+11q+11q^2+q^3,\\
 \chi=-1:&\quad (1+q)^4\Pr(V\text{ even})=(1+q)^3.
 \end{split}
\tag{R6}
\]

Both are at most `1+C/p` for a fixed `C`, independently of the
valuations of the shift differences. Also `beta_2<=16`. For any fixed
`eta>0`, split off finitely many small primes and use
`1+C/p<=p^eta` on the rest. It follows that

\[
 0\le\pi^4\prod_p\beta_p(h,k)
      \ll_\eta |\Delta|^\eta\ll_\epsilon T^\epsilon.
\tag{R7}
\]

This proves the candidate's size even when a bad factor is zero.
If one shift is odd and the other is 2 modulo 4, the four translated
arguments occupy all four residue classes modulo 4. One is 3 modulo 4
and is never a sum of two squares. Thus the integer product vanishes
pointwise, and (R4) gives `beta_2=0` as well. This is an actual
coefficient control, not a generic-coefficient heuristic.

### C. Repeated roots and the precise divergence scope

At `h=k`, for odd `p` not dividing `h`, the distinct roots have
multiplicities `1,2,1`. Thus the bracket multiplying `(1-chi q)^4`
is `2 E F+E(F^2)-2`.

For split primes, `E(F^2)=(1+q)/(1-q)^2`, giving

\[
 (1-q)^2(1+3q-2q^2)
      =1+q-7q^2+7q^3-2q^4.
\tag{R8}
\]

For inert primes, `F^2=F`, giving

\[
 (1+q)^3(1-2q)=1+q-3q^2-5q^3-2q^4.
\tag{R9}
\]

Both are positive for the eligible odd primes and equal
`1+1/p+O(1/p^2)`. For `h=1`, the 2-adic cylinder `x=8 mod 32`
has all three odd parts equal to 1 modulo 4: their valuations are
3, 0, and 1 respectively. The middle factor is squared, so this
cylinder alone contributes `16/32` to `beta_2(1,1)`.
Euler's divergence of the prime reciprocal sum now makes the positive
partial products diverge.

This refutes the naive finite constant obtained by copying the
distinct-root product to `h=k=1`. It neither proves a logarithmic
integer mean nor rules out a different or slowly varying density.

For the target, `|D_(h,h)|<<N T^epsilon` is enough. The exact number
of repeated pairs is less than `min(L,K)`, so their normalized total
is at most `T^epsilon N/max(L,K)<=T^epsilon N/K<=T^(4b+epsilon)`.
No repeated shift is left unpaid.

### D. Local transport, including its trivial endpoint

The exact derivative is

\[
 \phi'_{h,k}(t)=\frac{3R}{8}\int_0^h\int_0^k
                           (t+u+v)^{-5/2}\,dv\,du,
 \qquad |\phi'_{h,k}|\ll\Lambda_{h,k}/N.
\tag{R10}
\]

Partition the complete overlap into `O(1+Lambda)` cells of length
at most `ell=N/(1+Lambda)`. Hypothesis H controls the primitive from
each real left endpoint to every interior real point by
`E=T^epsilon ell^theta`. Integration by parts on that cell costs

\[
 E\left(\|W\|_\infty+
       \int_{\rm cell}|W'|+2\pi|W\phi'|\right)
       \ll E,
\tag{R11}
\]

because both `ell/N` and `Lambda ell/N` are bounded. Summing all
cells gives

\[
 |D_{h,k}-\rho^{\rm loc}_{h,k} I_{h,k}|
       \ll_\epsilon T^\epsilon
              N^\theta(1+\Lambda_{h,k})^{1-\theta}.
\tag{R12}
\]

Half-open intervals assign each atom once. A real exterior endpoint
atom, if retained by a different convention, has divisor-envelope
cost `T^epsilon`; smooth exterior masks also make it harmless.
An estimate only at the right endpoint of each cell would not
justify (R11).

The rounded lengths have `LK asymp N^(3/2)T^(-6b)`, even near the
lower endpoint when cutoffs may be bounded. Therefore the complete
averaged remainder in (R12) is at most

\[
 T^\epsilon N^\theta T^{(1-6b)(1-\theta)}
       \le T^{(76+166\theta)/325+\epsilon}.
\tag{R13}
\]

This is at most `T^(166/325+epsilon)` precisely for
`theta<=90/166=45/83`. At `theta=1/2` the exponent is `159/325`.
The quoted upper-edge power is a supremal band cost; the open endpoint
need not be attained.

The minimum cell scale is bounded below by a fixed constant times
`T^((166-76)/325)=T^(90/325)`. Hence, even on shorter subintervals,
the divisor bound and (R7) give an error at most
`T^epsilon(ell+1)<<T^epsilon ell`. This establishes H(1), while
(R12) then gives only `N T^epsilon`. It creates neither a power saving
nor an asymptotic identification of the candidate mean.

The smooth main integral obeys
`|I|<<_A N(1+Thk/N^(3/2))^(-A)` by repeated continuous integration
by parts, using (R10) and the complete smooth boundaries. For `A>1`,
summing first over `k` by comparison with its decreasing integral,
and then harmonically over `h`, gives

\[
 \frac1{LK}\sum_{h\ne k}|\rho^{\rm loc}_{h,k}I_{h,k}|
     \ll_\epsilon T^\epsilon\frac{N^{5/2}}{TLK}
     \ll_\epsilon T^\epsilon NT^{6b-1}
     \le T^{4b+\epsilon}.
\tag{R14}
\]

Every small product is included. Combined with the repeated-shift
payment and (R13), this proves precisely the conditional target
asserted in the claimant, without supplying H at the needed exponent.

### E. Primary theorem and actual application barriers

I inspected [Matthiesen, arXiv:1106.4690v3](https://arxiv.org/pdf/1106.4690v3),
Theorem 1.1 on PDF pages 4--5 and its neighboring definitions. It counts
all representations. Its hypotheses include primitive positive definite
forms, bounded fixed linear coefficients, pairwise affine independence,
a convex body in the scale box, and norm outputs in the corresponding
scale interval. The main real factor is the volume times the product
of `2pi/sqrt(-D_i)`; the error is `o(M^d)`, without an explicit rate.
The adjacent discussion excludes fixed translated one-variable systems
from this method's scope.

For the present application, the one-variable forms differ by constants,
so the independence condition fails immediately. The three-variable
vectors `(1,0,0),(1,1,0),(1,0,1),(1,1,1)` are pairwise nonproportional;
their thin convex box is admissible at `M=C N`. Normalizing its error
by `LK` leaves `o(N^(3/2)T^(6b))`, with upper reference exponent
`612/325`. No rate establishes the required power. Arbitrary complex
fiber weights and local absolute errors are also absent from the
conclusion. These are the precise scoped import barriers.

## 4. First doubtful or unproved step

No defect was found in the claimant's proved finite/local calculations
or its conditional transfer. The first missing arithmetic step is H
with `theta<=45/83`, including the correctness of the candidate density
at that local accuracy. Candidate local convergence is insufficient.

The audited import fails before it can supply that hypothesis. Its
valid higher-dimensional use also leaves the required absolute fiber
norm and quantitative local error unproved. This is not a general
no-go for other methods or a statement about all literature.

The repeated-root product divergence is restricted to that product.
No inference about the true repeated-shift mean or the size of an
oscillatory correlation is licensed by it.

## 5. Required controls and outcomes

| Control | Review outcome |
|---|---|
| Actual coefficient normalization | GREEN: all integer representations, the odd-prime factors, the ramified factor, and the real factor `pi^4` are compatible. |
| Distinct-root factor and bad primes | GREEN: (R5)--(R7) establish convergence and the actual shift-uniform upper size, including zero factors. |
| Congruence-zero sector | GREEN: the modulus-4 argument annihilates both the integer coefficient and its local candidate. |
| Repeated factors | GREEN: (R8)--(R9), the explicit positive 2-adic cylinder and divergence scope check. The complete sector is paid independently. |
| Density hypothesis | OPEN as labeled: no integer asymptotic is deduced from local factors. H includes mean identification. |
| Local versus global | GREEN: the primitive is controlled on every real subinterval; a full-cell or global-prefix estimate is not silently substituted. |
| Real endpoints and support | GREEN: half-open cells, exact overlap, smooth boundaries and possible atom costs are all retained. |
| Complete powers | GREEN: threshold `45/83`, square-root cost `159/325`, local lower scale `90/325`, and all main/repeated costs reproduce. |
| H(1) baseline | GREEN: the real-cell atom count plus divisor and candidate bounds gives H(1), whose transported result is only trivial. |
| Primary-source version and import | GREEN for the stated obstruction at the specified original version; no representation quotient is substituted. |
| Signed versus absolute | GREEN: no signed fiber error is converted to an absolute average, and no failed certificate is an actual oscillatory lower bound. |
| Full goal and independence | GREEN scope: no A4 estimate, pointwise exponent, moment, M1/M2 parent or quarter theorem is promoted. NONBLIND review only. |

No numerical experiment or symbolic computation was used as evidence.

## 6. Dependencies, provenance and binding

This review read the assigned claimant at the hash in Section 1,
`protocol.md`, and the original versioned PDF linked in Section 3E.
The protocol hash is
`f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
No alternative source version, blind report, conductor ledger or
successor artifact was accessed for this review.

The earlier discovery task's selected context supplied familiarity
with the frozen parameters, but the local density formulas and the
conditional powers above were rederived from the claimant's exact
statements. This report does not review its author's own oscillatory
discovery artifact. The conductor received an interim confirmation of
the local polynomial and primary-source checks; no repair was requested.

Only
`rounds/codex-managed/gc-complete-four-point-correlation/reviews/independent_local_arithmetic_review.md`
was written for this assignment. The claimant, shared graph, proof
draft, validation matrices, synthesis and legacy evidence were untouched.

## 7. Recommended state effect

**Retain** the hash-bound claimant as independently checked scoped
evidence: exact local lemmas, the conditional complete transfer, and
the specified import obstruction. Keep the actual local discrepancy,
A4 target, the `102/325` milestone and every full-quarter parent open.
No analytic parent or exponent should be promoted.

This GREEN verdict binds exactly to claimant SHA-256
**`6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e`**.
A material claimant edit requires a renewed binding. The assigned
same-round review is complete and stops here.

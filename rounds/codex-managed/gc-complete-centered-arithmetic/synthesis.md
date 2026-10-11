# Round 213 synthesis: complete signed radius gate and centering obstructions

Campaign: gc-complete-centered-arithmetic. Date: 2026-09-28.
Conductor decision is effective only after final-hash closure validation.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Result

No complete actual arithmetic estimate or pointwise exponent improves.
The round establishes a sufficient signed radius-averaged estimate with
its full pointwise recovery cost, and proves that two tested ways of
using centering still fail: absolute Fourier-kernel estimates and absolute
approximation errors for nonnegative models of small period.

These are complete quantitative controls on the selected methods, not
counterexamples to the signed target. The next round is the mandatory
broad strategy and current-primary-literature review, not another
automatic subdivision of this remainder.

## 2. Exact complete target

Keep b=83/650, every T^(166/325)<N<T^(242/325), the exact rounded L,K,
actual four r2 factors, real signed masks and full zero extensions.
Let Lambda=Thk/N^(3/2), Lambda_*=TLK/N^(3/2)~T^(76/325), and
Omega={1<=h<L,1<=k<K,h!=k,Lambda>1}. The candidate density rho_loc
is nonnegative and <<T^epsilon but is not an established integer mean.

    E_(h,k)(R)=D_(h,k)(R)-rho_loc_(h,k) I_(h,k)(R),
    sup_R (LK)^(-1)sum_Omega |E_(h,k)(R)| << T^(166/325+epsilon).

Closed 212 pays all repeated shifts, all small products and the entire
smooth model. Centering thus changes the full target by a target-safe
quantity in both directions; the identity creates no arithmetic saving.
The original signed tenth gate and all M1/M2 alternatives remain open.

## 3. Mathematical findings

### A. A complete signed radius-averaged sufficient input

For the complete product shell Omega_j={q<Lambda<=2q}, q=2^j, define

    Q_j^2=(T |Omega_j|)^(-1) integral_(T/2)^(2T)
                                  sum_(Omega_j)|E_(h,k)(R)|^2 dR.

The exact frequency support in R has width O(q/T). A Schwartz
reproducing kernel, applied to the shell vector, proves

    sup_(R in [T/sqrt(2),sqrt(3)T]) shell_RMS(E(R))
           << sqrt(q) Q_j + C_B N T^epsilon q^(-B).

The enlarged interval has a positive T-sized margin. The global
spectral total-variation bound pays the displayed tail; no global L2
integrability or free radius-to-supremum passage is assumed.

The unproved input

    Q_j << T^epsilon [sqrt(N)+N q^(-3/2)]                         (R213)

on every complete shell and the full parameter band would therefore give

    sup_R average_Omega |E| << T^epsilon
                   [sqrt(N Lambda_*)+N/Lambda_*]
         <= T^epsilon[T^(159/325)+T^(166/325)].

The product-shell fractions, all logarithms, tails and complementary
sectors are included. R213 can equivalently use D in place of E: the
smooth scalar term has radius norm O_A(N T^epsilon q^-A). R213 is still
unproved. Its exact expansion keeps the eight-factor discrete-discrete
term, both mixed model terms and the continuous-continuous term. An upper
bound for the discrete diagonal alone does not bound that signed energy.

### B. Constant centering and absolute Fourier kernels

Discretizing the smooth integral introduces an error smaller than every
prescribed negative power, uniformly on the full band. Thus the scalar
centered discrete coefficients a_(h,k)(n)-rho_loc can be tested exactly.
Actual r2(n)=0 on n=3 modulo 4. Slow mask variation gives a quarter of
its absolute mask mass on that residue. A finite mass inequality then
shows that every nonnegative constant center retains a fixed proportion
of the original absolute coefficient mass.

Together with closed 212's actual mass on Omega, this gives a two-sided
scale N/sqrt(Lambda_*) up to epsilon powers for the specified absolute
radius-Gram certificate. It fails above N=T^(204/325). The independent
isolated calculation proves a sharp mass ratio at its abstract interface,
the correct mixed radius L2 norm and an explicit periodic control whose
signed sums are tiny although its positive certificate is large.

The conductor also checks the continuous signed-measure version:
atomic and continuous model parts are mutually singular, so taking total
variation retains the entire atomic mass. Its positive certificate has
the same inadequate scale. No claim about a signed energy follows.

The dispersion report goes further: even if only the discrete-discrete
kernel is replaced by its modulus and the exact signed mixed and
continuous terms are preserved, the resulting nonnegative certificate
still has that lower scale. After the actual sqrt(q) pointwise-transfer
cost, its complete shell certificate is at least cN at every fixed
interior scale. This fully priced method fails throughout the open band.

### C. Small-period norm models and their complete complement

For period p0 define nu_(p0)(r)=p0^(-1) times the number of norm
representations modulo p0, and B=pi^4 product_(s=0,h,k,h+k)nu_(p0)(n+s).
The finite average mu is exact, bounded by pi^4 tau(p0)^4, and not
identified with rho_loc. Normalized finite Fourier coefficients obey
|hat B|<=mu. For p0<=c N/(1+Lambda), all nonzero Poisson aliases are
nonstationary and the entire model error is

    |sum_n B(n)W(n)e(R psi(n))-mu I| <<_A mu N(p0/N)^A.

Its complete shift average and the full (mu-rho_loc)I mismatch are
target-safe. All actual arithmetic remains in the exact signed
complement sum_n(a-B)W e(R psi). That complement is not estimated.

For every nonnegative periodic model in this period range, including
arbitrary model means and periods chosen separately for every shift,
the coefficientwise absolute approximation error is at least

    (LK)^(-1)sum_Omega sum_n |a-B||W| >= c N/log T.

The proof uses a prime p=3 modulo 4 not dividing p0, with
p<=C log(p0+2). Actual r2 vanishes when v_p(n)=1. CRT forces a
quantified amount of periodic model mass onto those actual zeros.
High-product mass survives all removals; a mean-size dichotomy handles
both small and large models. This is a lower bound for the explicit L1
certificate only, not for the signed complement.

The sole external audit is the fixed (3,4) specialization of
[Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).
It supplies the small omitted prime. No rate or theorem with growing
progression modulus is used. The conductor independently inspected the
statement and proof; no shifted-correlation result is imported.

## 4. First unproved step and strategic consequence

R213, or an adequate complete signed arithmetic alternative, is the first
missing estimate. Its kernel is explicit and its pointwise cost is paid.
The original complete centered target also remains open. Bounded scalar
centering, a finite norm model and exact transforms do not supply it.

The new obstructions apply to named positive estimates. They leave signed
Fourier-kernel cancellation, signed complements and other complete routes
open. A period beyond the proved nonstationary range has stationary
aliases requiring a new estimate; it is not an automatic improvement.

Even R213 at this b supplies only the 102/325 milestone. The full quarter
goal requires a complete family toward b=0, a stronger uniform theorem,
or an independent complete route. Round 214 must compare this remaining
difficulty against all full-goal alternatives and current source results,
rather than treating the new conditional interface as a solved problem.

## 5. Controls and validation

Three seven-section reports are complete, including the isolated
statement-only derivation. Independent seams check the periodic-model
source and arithmetic, the radius transfer and signed model terms, and
the conductor's actual centering controls. The conductor separately
checks the isolated report. All final verdicts bind exact hashes.

Every claimed gain or obstruction retains its coefficient class, norm,
support, endpoint range and epsilon losses. Lower bounds use fixed
interior scales; conditional upper implications cover the full band.
No numerical experiment was needed. Finite lemmas were proved directly
and independently checked; formalizing them would not establish the
missing signed arithmetic estimate.

Closure checks frozen inputs, closed 200--212 archives, graph and campaign
schemas, identity patch replay, unchanged graph/draft bytes, the prior
ledger prefix and legacy directories. These mechanical checks validate
state integrity, not the unproved arithmetic input.

## 6. Artifacts

Reports: centered_divisor_attack.md, centered_shell_dispersion.md,
blind_centered_certificate.md. Conductor calculation:
controls/conductor_centering_ledger.md. Independent reviews and
reviews/conductor_round213_reconciliation.md bind the final artifacts.
The frozen strategy is strategy/round213_complete_centered_arithmetic_attack.md.
Closed 212 supplies actual residual mass and the local candidate;
closed 211/208 supply the conditional reconstruction, unchanged in scope.

## 7. State effect

Identity State Patch only: all 399 graph nodes and proof-draft bytes
unchanged. Retain the complete conditional radius bridge and precise
centering/model obstructions as reviewed evidence. No moment, exponent,
M1/M2 parent or quarter theorem is promoted. Round 214 is pending design
as the mandatory broad strategy/current-primary-source review.

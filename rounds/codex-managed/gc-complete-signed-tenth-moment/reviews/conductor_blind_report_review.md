# Round209 conductor review of the isolated ten-root audit

Campaign: gc-complete-signed-tenth-moment. Date: 2026-09-27.
Role: conductor line review after the independent statement-only report.
Reviewed report SHA256:
a940318a6fe7fd48a66d670ee8c0f9acbe3c8b035fce96f1b53b3639a06f4b8d.

## 1. Result

GREEN for the stated exact-mass lemma and scoped absolute-majorant no-go.
No actual tenth-moment gain or pointwise improvement is established.

## 2. Exact statement and hypotheses

The report's (2.1) allows distinct bounded divisor-envelope weights and
every sign pattern on [N,4N]. Its (2.2) concerns the complete all-sign
termwise absolute expansion with exact frequencies removed, with fixed
nonnegative smooth v and w and real Schwartz Psi satisfying Psi(0)=1.
Uniform positivity requires N<=T^c for a fixed c<1 and large T,N.
The power comparison is at fixed alpha strictly above166/325, with
epsilon smaller than the explicit excess. No uniform fixed margin is
claimed at the lower endpoint.

## 3. Proof audit

Squarefree radical independence forces one signed integer equation in
each occupied class and forbids singleton classes. For a block of size
m, choosing m-1 integers determines the last one, giving the report's
sum N^((m-1)/2) sum_(q<=4N) q^(-(m-1)/2). The three cases m2, m3 and
m>=4 all cost O(N^(m/2)); the m3 logarithm has a fixed half-power margin.
Dropping distinctness of squarefree classes increases the count. Across
the finitely many partitions of2k labels this gives O_k(N^k), and the
divisor weights give N^(-3k/2+epsilon). This proves every claimed exact
mass, including non-pairings, without a heuristic independence model.

The chosen positive v-subinterval has total r2 mass asymptotic to its
length times pi. Inclusive versus open lower endpoints are harmless:
an endpoint atom is bounded by the elementary O(sqrt(N)) circle error
(or the divisor bound). Coefficient mass is at least c N^(1/4).
Ordered five-root sums occupy O(T sqrt(N)) bins of width delta/T; weighted
Cauchy therefore gives c N^2/T in close pairs. Continuity and positivity
of w_hat(0) give a uniform positive modulus near zero. The T/2^10 factor
is correct. Subtracting all2^10 exact sign patterns costs only
O(T N^(-5/2+epsilon)). The stated uniform alpha-range more than suffices
for this removal to be negligible. Division by U gives exactly
(5/2)alpha-83/65, with threshold166/325.

The cosine expansion phase exp(-3pi i sum(signs)/4) is correct. The
Dirichlet control has no pole on the displaced support because
0<ha<=hu<=hb<1/4. Its tenth integral is O(T), whereas its already
aggregated coefficient d1 is at least cL^9. Reality of w implies the
same modulus at -h as h. The report correctly notes that the full
moment's large exact term is canceled by its signed offdiagonal; it
does not falsely claim that this particular offdiagonal is small by
itself. The example is a logical control, not actual arithmetic data.

## 4. First unproved step

Estimating the actual signed nonzero-frequency remainder remains open.
An upper triangle inequality cannot be reversed to transfer the
absolute-majorant lower bound to the actual moment. Nor does the
control prove that the needed arithmetic cancellation occurs.

## 5. Controls and outcomes

GREEN: pairing sharpness, non-pairing example, all-plus impossibility,
all-sign exact removal, real endpoints, explicit epsilon comparison,
displaced signed control and no incorrect graph conclusion. All checks
were analytical. Original statement-only isolation was preserved until
this report was complete; later nonblind review is a distinct task.

## 6. Exact artifacts used

protocol.md; the frozen209 isolated packet; the reviewed report at the
hash above; conductor_tenth_power_ledger.md for a separate independently
written proof comparison. The report's proof does not depend on that
comparison. No web theorem or numerical computation is imported.

## 7. Recommended state effect

Retain the report as validated local evidence. No new graph node is
needed for this localized extension of already accepted exact-resonance
and absolute-majorant results. Keep the actual signed target open and
preserve the accepted pointwise exponent and proof draft.

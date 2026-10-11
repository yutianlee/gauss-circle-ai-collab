# Round220 independent review of the isolated operator lemma

## 1. Result

GREEN for the isolated exact multiplier lemma. I independently checked
the Fourier and interval decompositions and the two finite controls.
This review is by the conductor, not the report author. No arithmetic
application or target estimate is certified by this abstract result.

## 2. Exact statement reviewed

Report reports/blind_smooth_mask.md, SHA256
e27659b89c33da6c8216f5817351edfa1a3fd269ffaeb8d8c1e51e6ce180e33b,
against briefs/blind_smooth_mask_statement.md, SHA256
97c84fcd8befb47401c11076d4afa49c55d5708df31ec9c79dffce9ac3c24459.
Under a bilinear bound for every vector in the full row space, the exact
row-dependent C2 multiplier and interval mask cost
C S B (1+K/A)(1+log(2+n)) for real residual phases. Constants are uniform
when K/A<=1. The stated complex-parameter extension is also bounded.

## 3. Independent mathematical checks

A period-four cutoff extension supported away from its endpoints has
Fourier coefficients bounded uniformly by C S min(1,(1+K/A)^2/m^2).
Summing below and above |m|=1+K/A gives C S(1+K/A), not a power-sized
number of row pieces. Absolute uniform convergence proves exactness.
The bound is a sum of suprema over rows, the quantity needed for the
product multiplier estimate; bounding each row's l1 norm alone would
not have sufficed. The report uses the correct stronger bound.

For n columns, on the cyclic group of order 2n+1 the indicator of
[0,n-1] evaluated at t-s equals the prefix indicator s<=t, including
t=0,n. Differences in[-n,-1] wrap into[n+1,2n], never into the selected
branch. The geometric sum has Fourier l1 norm O(1+log(2+n)). Writing
an interval as a bounded-variation combination of prefixes has total
coefficient variation at most2, including empty and half-weight cases.
Thus its exact product expansion is uniformly summable across rows.
Multiplying the two decompositions and applying the all-row hypothesis
termwise proves the bound for complex bilinear vectors without a
conjugation convention change. Finite sets and absolute convergence
justify every exchange.

The perturbation e(alpha t)-1 has C2 norm O(K/A) when K/A<=1, so the
optional error estimate is correctly priced. It supplies no literal
deletion identity. The report's complex-phase growth bound follows
from |Im(alpha)|<=K/(2A), t<=3.

## 4. First doubtful or unproved step

No gap in the isolated statement was found. Its first application
condition is the norm on all combined row vectors. A theorem for
u_(j,a)=x_j y_a alone does not meet that hypothesis; smoothness only in
k cannot create the missing factorization in j,a. The separate actual
binding is reviewed elsewhere and still needs an arithmetic estimate.

## 5. Controls and outcomes

The one-row deletion control has unphased sum0 and phased sum1+i,
with B=sqrt(2); all specified columns and parameters fit the packet.
The Walsh matrix satisfies the separate j/a product theorem with B=1
by exact binary-character orthogonality. Its permitted constant smooth
row signs remove all signs and yield sqrt(q) on unit product vectors.
The genuine combined-row norm is sqrt(q), so the control contradicts
only the unsupported upgrade. Empty, singleton, adjacent endpoints,
arbitrary row dependence and zero-data cases are all covered exactly.
Zero numerical experiments.

## 6. Dependencies and provenance

Conductor, round220, current graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b;
protocol and the two exact-hash artifacts in section2. The author was
given only protocol plus the isolated statement and disclosed prior
217--219 work. This is statement-only access for the current result,
not history-free independence. I had application context but did not
author the submitted isolated proof. No source theorem is imported.

## 7. Recommended state effect

Retain as GREEN elementary operator infrastructure and a scope control.
No graph or draft mutation, no complete energy gain and no exponent
gain follows. The full actual signed target remains open.

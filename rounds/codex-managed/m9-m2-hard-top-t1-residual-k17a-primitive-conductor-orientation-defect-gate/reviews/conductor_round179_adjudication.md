# Round 179 conductor adjudication

- Campaign: `m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate`
- Round: 179
- Starting graph: `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`
- Closing label: `primitive_conductor_orientation_defect_capacity_or_self_return_no_go`
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

Round 179 proves the exact primitive-frequency Möbius projector, isolates
its \(d=1\) trace, and gives the canonical centered decomposition of the
literal two-orientation exact-conductor block.  The complete high-
conductor trace is target-safe.

The decisive result is a stronger exact no-go.  If
\(K_q^\circ=K_q-\mu(q)/q\), then for every odd \(u_0>1\),

\[
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)=E_{u_0}(b).
\tag{179.A1}
\]

Thus the all-conductor centered defect reconstructs the original literal
orientation block, and the high-conductor defect is that block minus the
already-safe low-conductor packet.  Primitive-conductor centering supplies
no new cancellation by itself.

Prime and prime-square artificial buckets attain the full \(Lq\)
coefficient-uniform conductor capacity while respecting the literal
unit/count shadow.  They are not literal coefficients and yield no lower
mass.  The two natural orientation maps also fail: one leaks from the
positive displacement domain and does not preserve endpoints; the other
preserves products but changes the fixed row and sends selected divisors
to zero-extended complements.

No proof of (177.K34), complete K17a, a parent, a bridge, the quarter
theorem, or an exponent improvement is obtained.

## 2. Exact statement and hypotheses

Retain the accepted Round-176/177 literal packet with

\[
g=(u,n),\quad u=gu_0,\quad n=gn_0,\quad(n_0,u_0)=1,
\]

odd \(u,u_0\), \((u,v)=1\), both orientations, and every selector,
squarefree/coprimality field, parity branch, Fejer weight, displacement
condition, profile, floor, star, hard value, endpoint conjugation, phase,
physical lift, and zero extension.  For \(q\mid u_0\), all occupied
\(b=\bar v n_0\pmod q\) lie in \(U(q)\).

The accepted exact-conductor normalization is

\[
c_{u_0}((u_0/q)a)=\frac q{u_0}c_q(a),\qquad(a,q)=1.
\tag{179.A2}
\]

Under these hypotheses, the durable kernel proves

\[
K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
\qquad K_q(b)+K_q(-b)=\frac{2\mu(q)}q,
\tag{179.A3}
\]

the centered block identity

\[
\mathcal C_{u_0,q}
=\frac q{u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
 +\frac{\mu(q)}{u_0}\sum_b(B^+_{q,b}+B^-_{q,b}),
\tag{179.A4}
\]

the target-safe high trace, (179.A1), exact high/low self-return, the
\(q=1\) boundary, the \(Lq\) coefficient-uniform capacity, and the two
orientation-map failures.

## 3. Proof and power adjudication

Möbius inversion of \(\mathbf1_{(a,q)=1}\), together with
\(c_q(rk)=r^{-1}c_{q/r}(k)\), proves (179.A3).  For a unit \(b\), every
\(d>1\) parity term is odd under \(b\mapsto-b\); only \(d=1\) remains.
This gives the symmetric trace coefficient \(\mu(q)/u_0\) after the
single accepted factor \(q/u_0\).

The fixed-stratum atom mass is \(O(u_0LX^\varepsilon)\), so the trace
cost at fixed \((u_0,q)\) is \(O(|\mu(q)|LX^\varepsilon)\).  The exact
label count is

\[
\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
=\prod_{p^a\parallel u}(2a+1)\ll_\varepsilon X^\varepsilon.
\tag{179.A5}
\]

For (179.A1), remove \(d=1\) from (179.A3), interchange the divisor sums
over \(d\mid q\mid u_0\), and use
\(\sum_{r\mid u_0/d}\mu(r)=\mathbf1_{d=u_0}\).  Applying
the result atom by atom proves the centered self-return.  The all-
conductor centered traces cancel because \(\sum_{q\mid u_0}\mu(q)=0\);
the \(q=1\) term is essential.  At \(u_0=1\), \(K_1^\circ=0\), and the
sole conductor is already low.

The pointwise bound \(|K_q^\circ(b)|\ll_\varepsilon q^\varepsilon\)
and the complete atom mass give \(LqX^\varepsilon\).  Restoring the
physical lifts gives \(O(Lu_0/q)\) atoms per inverse-product bucket.
Distributed prime and prime-square artificial arrays therefore attain
\(\asymp Lq\).  One conductor square root leaves \(L\sqrt q\), still
above target on power-size conductors.

## 4. First unproved step

The first open statement is the complete literal centered defect estimate

\[
\left|
\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
\frac q{u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
\right|
\stackrel{?}{\ll}_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.
\tag{179.A6}
\]

By the self-return identity, (179.A6) is the original unresolved literal
orientation block minus a safe low-conductor term.  A future proof must
use new selector-, phase-, endpoint-, and lift-aware signed structure;
Round 179 neither supplies nor rules out such a theorem.

## 5. Controls

Every campaign control is recorded in
`controls/conductor_round179_controls.md`.  Projector normalization,
\(d=1\), \(q=1\), unit support, divisor summation, literal bucket
coarsening, physical lifts, trace capacity, high/low separation, outer
absolute placement, and downstream scope are GREEN.  The two orientation
maps fail exactly at their declared route seams.  Adversarial buckets are
quarantined from literal lower mass.  No numerical evidence was used.

## 6. Dependencies and evidence

The adjudication uses the two accepted predecessor kernels, the three
Round 179 reports, the durable formal kernel, the formalized candidate,
the conductor reconciliation, and three independent GREEN seam reviews.
The blind report was statement-only before its saved post-unmask review.
No external theorem is imported.

## 7. State decision

Create one subordinate `proved_internal` node for the exact primitive
projector, target-safe trace, and all-conductor self-return.  Update the
accepted primitive-alias reduction and the open hard-TOP owner only for
evidence and next-action accuracy.  Reject only automatic/coefficient-
uniform gains from parity or centering, the two evident orientation
involutions, one-square-root closure, literal-lower-mass overreach, and
downstream/exponent overreach.

Retain (177.K34), complete K17a, every parent and bridge, the quarter
target, the internal \(1/3\), audited external
\(0.3144831759740614\ldots\), and target \(1/4\) at inherited status.

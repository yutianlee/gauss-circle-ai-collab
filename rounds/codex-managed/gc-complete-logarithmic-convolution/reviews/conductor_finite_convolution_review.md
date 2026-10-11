# Round225 conductor finite-convolution review

## 1. Result

GREEN for the isolated finite logarithmic/Vaughan identities and their
scope controls. No analytic saving follows from the identities alone.
The conductor is not the claimant of the reviewed report.

## 2. Exact hypotheses

Dirichlet convolution is on positive integers; psi is either1 or chi4,
with all even zero values retained. Real U,V>=1 use complementary
literal integer predicates. The test F has finite support and F(1)=0;
H_F(n)=F(n)/log n is defined only at n>=2, and H_F(1)=0.

## 3. Independent derivation

For a=psi, g=mu psi, b=Lambda psi and c=psi log, complete
multiplicativity gives a*g=delta and a*b=c, including even arguments
without dividing by psi. Hence b=g*c. Split g at U and b at V in
g*a*b; use g_>U*a=delta-g_<=U*a on the low-b part. The resulting
four terms have signs plus, plus, minus, plus, exactly as in the
report. The long-long term requires the strict product d e>UV.

The logarithmic derivation D(u*v)=Du*v+u*Dv gives
D(1*chi4)=f*(Lambda+chi4 Lambda). Its kernel at2 is log2 on every
positive power, at split primes2log p, and at inert primes2log p
only on even powers. These local values and the displayed f(p^nu)
values verify the identity at every prime power.

Substituting both four-term branches and keeping the original outer
f yields the four finite product sums in equation6. The original
cofactor r carries no new psi(r). This is essential for even r.
Dividing by log of the complete product, not of a selected factor,
gives the correct unweighted pairing. Inclusive floor limits and
holes in the test support are preserved.

For the explicit prime-power check, mu restricts its local exponent
to0 or1. With u=1_(p<=U), the four scalar coefficients printed in
equation8 sum to1 by B_nu-B_(nu-1)=v_nu. They are multiplied by
psi(p)^nu, never divided by it, so the zero character case is legal.
When either cutoff exceeds the support, the indicated exact
cancellation is correct. At F=delta5 and U=V=1 both character
branches contribute1; the coefficient triangle equals the answer2.
The basic logarithmic contraction on delta_(5^nu) is also positive.
These controls reject an automatic scalar power saving only.

## 4. First gap

No gap was found in the finite algebra. Cancellation among actual
factor sums, bounds for their norms and a complete nonlinear estimate
are separate analytic requirements. No application's endpoint follows
from the report or its positive one-point control.

## 5. Controls

GREEN for n=1, every prime power, prime2, inert odd powers, all strict
and inclusive cutoff boundaries, empty long-long support, large U/V,
the complete product logarithm and the positive test. Zero experiments.
Current two-file statement isolation and retained-history disclosure
are explicit.

## 6. Exact bindings and provenance

Conductor reviewer, round225, 2026-09-28. Report claimant is the reused
finite-derivation agent, not this reviewer.

- reports/blind_finite_convolution.md:
  56b082ce59ac8799f7c05573ce3b5a770b32714b13fd7f6ac36e1bde131724e2.
- briefs/blind_finite_convolution_statement.md:
  a5e2bc3a6d7b07e43bcfcfbd4db63d15f9120c3be00ea5b4257abde8e1b2a5b7.
- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.

Relative paths above belong to
rounds/codex-managed/gc-complete-logarithmic-convolution except protocol.
No external theorem was imported.

## 7. Recommended state effect

Retain as GREEN scoped finite evidence. No complete estimate, graph
promotion, proof-draft change or successor follows.

# Round 92 conductor review: sources and graph hygiene

## Primary-source map

Li--Yang's Section-4 input is a separably weighted two-variable exponential
sum with a nondegenerate (C^3) one-variable phase and explicit Case A/B
conditions.  It does not accept the M1 varying-modulus four-Kloosterman Gram
operator or the M2 moving two-character reciprocal kernel.  The primary v2
text also contains a literal (T^{-7/16}) versus (T^{7/16}) threshold
inconsistency, so its card remains `source_audit_required` even as a
guardrail.

Xiao's Theorems 1.1--1.3 concern the unweighted sum
(S(h,n)=\sum_{n/2\leq a\leq n}e(h\sqrt a)): a second moment for
(H\geq n^{1/2+\delta}), a fourth moment for
(n^{1/2+\delta}\leq H\leq n^{2/3}), and a discrepancy consequence that
also invokes a separate pointwise estimate and Erdos--Turan.  Neither
canonical core has this coefficient, support, independent-height, or norm
structure.  Xiao is a source-audited guardrail, not a dependency.

## Graph repairs

The following repairs are structural rather than mathematical promotions.

1. Break the direct dependency cycle between the product-wavelet
   short-numerator reduction and the residual upper-conductor reduction.
   The former is a prerequisite of the latter, not conversely.
2. Route the M2 hard-density estimate into the top signed-cone node.  Remove
   the top-cone and top-transform direct implications to full `M9-M2` and
   endpoint uniformity.
3. Replace stale actions that still ask for unconditional exponent
   extraction or R5 reconciliation.  Round 91 already proved the real-(X)
   one-third theorem and closed R5.
4. Point `M9-M1`, `M9-M2`, `M9`, and endpoint uniformity to their exact
   canonical cores plus the still-separate outside packets.

## False shadows retained

No claim may replace an actual symbol by arbitrary bounded coefficients,
take absolute values before the signed interaction, identify the M1 row with
its Gram lift, infer a power from local period depth alone, delete M1 bad or
Ramanujan modes, delete the M2 metric density, use quotient parity or a
half-frequency gap, or infer the fixed endpoint from an unquantified global
moment.

## Outcome

No audited primary theorem proves either core.  The source cards and graph
edges can be repaired without changing any analytic status.


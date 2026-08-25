# Round 147 terminal hostile power reread v2

## 1. Result

**GREEN.**  The sole remaining correction identified in the preceding
terminal review has been made.  Equation (147.C40) now reads

\[
\sum_{k\le K_F}|h_z(k)|
\min\!\left(\frac Mk,RM^{1/4}\right)
\ll_\varepsilon R^{1/2}M^{5/8}X^\varepsilon.
\]

It therefore uses exactly the physical channel support of (147.C29).

## 2. Exact statement and hypotheses

Here \(K_F=\lfloor\sup\operatorname{supp}F\rfloor=O(M)\).  The power
ledger is on the unitary ratio line, or on the explicitly allowed
\(|\Re z|\ll1/\log X\) displacement.  No fixed-strip uniformity is
asserted.

## 3. Verification

For \(k>K_F\), \(F(kn)=0\) for every integer \(n\ge1\), and the
candidate records exact polar-dual cancellation separately for that
\(k\).  Restricting (147.C40) to \(k\le K_F\) is therefore the correct
finite physical sum.  It can only reduce the earlier majorant, so the
powerful-count bound and the losses \(R^{1/3}\) at \(M=R^{4/3}\) and
\(R^{1/4}\) at \(M=R^2\) are unchanged.

## 4. First doubtful or unproved step

The first open analytic step remains the growing-complex-order Bessel
estimate.  Granting it, the first missing arithmetic power remains the
signed, physically truncated correlation (147.C44).  The repair to
(147.C40) introduces no new seam.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Physical \(K_F\) support in (147.C40) | **GREEN** |
| Per-\(k\) cancellation beyond \(K_F\) | **GREEN** |
| Unitary/small-\(c\) hypothesis | **GREEN** |
| Fixed-order qualification | **GREEN** |
| Reciprocal crossover wording | **GREEN** |
| Truncation in (147.C44) | **GREEN** |
| Method no-go versus lower bound | **GREEN** |
| Graph and exponent scope | **GREEN** |

## 6. Dependencies and scope

This terminal check used only the current conductor candidate and
verified the repaired (147.C40) against its finite convolution
(147.C29).  No downstream owner, target estimate, strict top range, or
exponent improvement is created.

## 7. Promotion verdict

**Terminal verdict: GREEN for promotion in the candidate's stated
scoped form.**  No further power, support, or downstream-scope
correction is required.  The exact fixed-order reduction and
\(\mathsf{squarefree\_H\_resonance\_no\_go}\) may be promoted without
promoting the \(t=1\) target, the growing-order estimate, the signed
correlation, or any global exponent change.

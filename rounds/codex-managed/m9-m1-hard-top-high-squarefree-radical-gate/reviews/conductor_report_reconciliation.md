# Conductor reconciliation of the Round-181 reports

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `conductor_report_reconciliation`
- Role: conductor reconciliation
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Context: all three assigned reports, their briefs, the active campaign,
  and the Round-119 hard-parent connector
- Claimant/reviewer/blind status: conductor adjudication of one discovery,
  one hostile audit, and one statement-only derivation; no graph edit

## Evidence compared

The conductor compared the discovery, hostile connector/capacity, and
statement-only reports. No claim is selected by vote. The common exact
content is separated from the two different report-level exit
recommendations.

## Common proved content

All three reports independently establish the finite product identity and
the unique decomposition (r=st^2), (\mu^2(s)=1). The selected-context
reports further agree on the literal parametrization

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
\]

with (G=(h,n)), (d,e) squarefree, and ((da,eb)=1). Hence (G\mid t).
The hard cone gives (st^2\asymp L^2).

The following estimates are exact consequences of bounded literal
normalization and divisor incidence:

\[
 \sum_{\substack{s\le L\\\mu^2(s)=1}}\sum_t
 |C_{L,X}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

and

\[
 \sum_{\substack{s>L,\ \mu^2(s)=1\\
                   t\ge\lceil\sqrt L\rceil}}
 |C_{L,X}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

Thus a genuine strict sector is proved. Its exact unresolved complement is

\[
 s>L,\qquad 1\le t<\lceil\sqrt L\rceil.
\]

At (t=1), the parametrization forces (G=a=b=1), leaving the complete
coprime squarefree literal cone. Coefficient-uniform capacity there is
(L^2), against target (L^{3/2}). The blind dechirped examples establish
only this universal-method capacity; they are not literal lower bounds.

## Mechanism reconciliation

The discovery report proves the exact identity

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 =\sum_{b,u}F(bu^2)
   \sum_{\substack{a\mid u\\a^2b>L}}\mu(a).
\]

For (b>L), the inner sum is (\mathbf1_{u=1}); the (b\le L)
correction has the low-radical target-safe ledger. Hence complete
squarefree Möbius linearization returns the original cone modulo an
already-paid term. The bijection (r\leftrightarrow(s,t)) likewise shows
that a positive joint-(t) lift has no new orthogonality.

For a smooth full-orientation divisor fibre, the central Mellin mode does
vanish at an odd (3\bmod4) prime occurring to odd exponent. This is only
one mode. The literal ratio cutoff requires the full inverse Mellin
integral, whose noncentral local factors are not uniformly small. The
accepted no-go is therefore limited to retaining only the central mode,
positive treatment of all other modes, or exact recombination. It is not
a rejection of every future coefficient-sensitive Mellin theorem.

## Terminal-label decision

The discovery report recommends the mechanism no-go label, while the
connector report recommends the strict-sector label. The latter is the
stronger accurate round outcome because the low-radical and large-(t)
sectors are new literal target-safe results with an exact complement.
Round 181 therefore closes, subject to the remaining seam reviews and
State Patch validation, under

`strict_hard_m1_radical_sector`.

The mechanism-scoped Möbius, gcd, joint-(t), and central-Mellin
self-returns are retained inside the same subordinate reduction. The
small-(t) target, the hard parent, the smooth parent, M9-M1, GAR, every
M2 parent, endpoint uniformity, M9, both bridges, the quarter theorem, and
all exponent claims remain open.

# Round216 conductor review of the isolated radical-cutoff report

## 1. Result

GREEN for the report's stated generic cutoff, exact-resonance, transfer
and counterexample results. NONBLIND conductor review, 2026-09-28.
Campaign:gc-actual-radical-high-values. Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Reviewed reports/blind_radical_cutoff.md at SHA256
e0accd624e0d9f1b95644c3456ed6302f9ac145aa6d4356aba4fb6cf82c7595e.
The original report's isolation is preserved; this later review is not blind.

## 2. Exact statement and hypotheses

The packet assumes fixed real coefficients bounded by C tau(n)n^(-3/4)
and a fixed real even Schwartz Psi with modulus at most one. It does
not identify these coefficients with r2 or require Psi to come from
the actual compactly supported radial mollifier. The head is
O(Q^(1/4)(1+log Q)); the all-sign absolute exact twelfth coefficient is
O(Q^-3 log(2Q)^18). At Q=floor(T^(2/5)), the head is eventually less
than V0/2 and the full high-event transfer costs 2^12 at threshold V0/2.
Neither conclusion controls the nonzero displaced Fourier remainder.

## 3. Independent checks of the proof

The divisor inequalities tau(ds^2)<=tau(d)tau(s^2)<=tau(d)tau_3(s)
pay the complete harmonic sum. The elementary divisor summations give
sum_(d<=Q)tau(d)d^(-3/4)<<Q^(1/4)(1+log Q) and
sum_(d>Q)tau(d)^2 d^(-3/2)<<Q^(-1/2)log(2Q)^3.

The multiquadratic induction is valid: an element squaring to the new
prime must be a simultaneous eigenvector of the old sign flips, hence
a rational multiple of one old squarefree basis vector, contradicted
by the new prime valuation. Thus an exact relation has no singleton
class. Summation over every nonsingleton set partition gives the sixth
power of the quadratic class mass, including odd block sizes and every
ordered sign choice. Torus averaging proves nonnegativity only of the
whole exact coefficient. The Fourier factor is correctly
T w-hat(-T Delta) and the cosine phase is e(-3 sum epsilon/8).

The event transfer keeps all thirteen binomial terms and the shifted
threshold. Its layer-cake identity includes the boundary term and all
higher levels. The displayed explicit T_* and the separate compact
range bound correctly handle the floor and constants.

For the generic peak control, only O(M^(7/10)) indices up to 2M have
small squarefree part. Averaging cos^2 on [M,3M/2] therefore produces
a center with a peak of order M^(1/4). The derivative bound of order
M^(3/4) preserves that peak on an interval of length M^(-1/2), giving
a twelfth-moment lower bound of order M^2 inside the prescribed w=1
region. In the lacunary construction each block is fixed once selected;
earlier blocks enter the small head at subsequent selected scales,
and the finitely many exponential-tail conditions imposed when choosing
each later block bound the sum of all future perturbations. The head
bound is o(M_j^(1/4)). This validates one fixed infinite generic sequence,
not merely a sequence allowed to change with T. It refutes precisely
the packet's envelope-only inference to a small finite-window moment.

## 4. First doubtful or unproved step

No gap was found in the stated packet results. An application to the
actual circle series still requires arithmetic control of the full
nonzero remainder or high tail. The constructed sequence and Gaussian
Psi are not asserted to be the actual circle coefficients and mollifier.
No inference from this control to failure of H216 is allowed.

## 5. Controls and outcomes

Class d=1 and every harmonic are included. Four size-three relations
give a negative individual exact phase, verifying that termwise
positivity was not assumed. Consecutive retained indices produce a
nonzero difference of order M^(-3/2), confirming that nonzero does not
imply Fourier decay on the moving window. The coherent peak is a direct
generic moment lower bound, distinct from an absolute-certificate lower
bound. Infinite convergence, strict events, bounded T and all signs pass.
All checks are analytical; no numerical experiment was performed.

## 6. Dependencies and exact artifacts used

Read protocol.md; the isolated packet briefs/blind_radical_cutoff_statement.md;
and the final report named and hashed in Section1, all under the current
campaign except protocol. The conductor also knows the manifest, actual
candidate, ledger and accepted kernels and makes no isolation claim for
this review. The derivations above use only the isolated packet's
hypotheses. No new source theorem is imported.

## 7. Recommended state effect

Retain the independent generic derivation and scoped counterexample as
reviewed evidence. Do not promote the actual high-value target from it.
The separate collective distinct-class candidate requires its own isolated
algebra rederivation and actual-coefficient seam reviews before acceptance.
The proof graph and proof draft are unchanged by this review.

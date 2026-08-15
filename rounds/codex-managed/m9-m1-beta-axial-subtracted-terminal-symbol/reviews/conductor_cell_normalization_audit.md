# Conductor audit: cell normalization versus the aggregate symbol

Campaign: `m9-m1-beta-axial-subtracted-terminal-symbol`  
Role: normalization and implication seam  
Allocation: analytical/algebraic only

## 1. The aggregate target is not well typed

The limiting endpoint-free vector is a sum/integral over
\((j,h,q,x,\beta)\).  Its saddle parameter

\[
 \lambda_{j,q,x}=\frac{\pi q\sqrt{Xx}}{D_j}
\]

therefore varies inside that aggregate.  A pointwise assertion
\(|K_{\rm term}^{\circ}|\ll\lambda^{-2}w\) cannot be imposed on the
already-summed object without either fixing a cell or replacing the right
side by an explicit summed majorant.  The current graph statement mixes
these two meanings.

## 2. Canonical cell factorization

Round 27 supplies the lawful local normalization.  On a separated signed
saddle, the post-endpoint \(R_1\) amplitude before the signed top
convolution contains

\[
 \mathfrak N_{j,h,q,x}=
 \frac{D_j}{q}
 h^{-\sigma+\zeta/2}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \left(\frac{\pi\sqrt{Xx}}{D_j}\right)^{\sigma+\zeta/2}
 x^{-\sigma-3/4-b/2},                              \tag{C39.1}
\]

and a phase-removed two-denominator kernel whose stationary numerator is
\(\lambda\).  Thus the separated regular piece has the form

\[
 \mathfrak N_{j,h,q,x}\,\lambda\,K_{R_1}(L,\nu),   \tag{C39.2}
\]

where the accepted local theorem is

\[
 |K_{R_1}|\ll_b\lambda^{-2}w_b,
 \qquad |\partial_LK_{R_1}|_\nu\ll_b\lambda^{-3}w_b. \tag{C39.3}
\]

Consequently (C39.2) has value capacity
\(\mathfrak N_{j,h,q,x}\lambda^{-1}\), i.e. the familiar
\(D_j/(q\lambda)\) gain after the remaining monomial is kept outside.
The global factor \(-4X^{1/4}\operatorname{Re}(e(1/8)\,\cdot)/\pi\),
the character, profile cutoffs, floors, stars, and all cell sums also lie
outside the bare kernel in (C39.3).

This reconciles the blind raw ledger with Round 27: its
\(X^{3/4-a/2}D_j^a(H_j+1)^b h^{\cdots}q^{\cdots}
x^{-3/2-b/2}\lambda^{\kappa-2}\) is the modulus of the *full raw
cell after multiplying the bare regularizer*, not a contradiction to the
pre-numerator \(\lambda^{-2}\) theorem.  It is precisely why the two
objects must not share one symbol name.

## 3. Correct quantitative interface

The next lemma must first define, for every one-count cell, a phase-removed
kernel \(\widetilde K_{j,h,q,x}^{\pm}\) by factoring out (C39.1), the
stationary numerator, the character, and the external normalization.
Only that object can lawfully be asked to satisfy the bare
\(\lambda^{-2}/\lambda^{-3}\) estimates.  A useful equivalent formulation
may use the physical-height mixed norm

\[
 \sup_L\int |\widetilde K(L,\nu)|\,d\nu
 +\int_{L\text{-cell}}\!\int
 |\partial_L\widetilde K(L,\nu)|\,d\nu\,dL
 \ll X^\varepsilon\lambda^{-2},                   \tag{C39.4}
\]

with the translated moving-face traces included.  This is closer to the
actual finite-section BV implication and does not require a single
pointwise weight independent of translations in \(L\).

## 4. Remaining seam

The exact axial regularizer and its fixed-physical-height derivative are
valid algebra.  After the normalization above, the first unproved actual
coefficient is the complete second translation divided difference

\[
 \frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
 -\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.               \tag{C39.5}
\]

It must be controlled through both saddle signs, entry/exit, the common
\(\rho\) germ, and moving faces.  Round 38 proves existence and tails but
does not supply the \(X\)-uniform norm in (C39.3) or (C39.4).

## 5. State recommendation

Promote the exact limiting regularizer/derivative algebra after independent
seam validation.  Reject the current bare bound when read as a statement
about the aggregate.  Replace it by a cell-normalized phase-removed symbol
obligation (or the equivalent mixed-norm version), and keep the second
translation divided difference quantitatively open.  No beta-transition or
target estimate follows in this round.

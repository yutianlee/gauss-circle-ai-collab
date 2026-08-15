# Round 59 conductor adjudication: exact self-reciprocity, no short-window saving

## 1. Decision

Promote the finite additive projector and the smooth-interior stationary
reciprocity as a scoped reduction.  Promote also the exact reciprocal
Hessian identity and the obstruction to any determinant-only lattice
argument.  Do not promote a short-window estimate, a complete hard-symbol
B-process, or a terminal-M1 implication.

The discovery report initially misstated both the dual thickness and the
Hessian spectrum.  After conductor intervention it was corrected to agree
with the independent blind and hostile derivations: a length-\(R\) primal
window has dual thickness \(\asymp R\), hence \(\asymp R^2\) raw lattice
points, while both Hessian eigenvalues have order one and opposite signs.

## 2. Exact projector and stationary main

For integers \(h\geq1\) and \(n\), extended by
\(\chi_4(m)=0\) for even \(m\),

\[
 \mathbf 1_{h\mid n}\chi_4(n/h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)e(an/(4h)).
\tag{59.1}
\]

For a smooth interior radial amplitude, Poisson summation in \(n\) and
\(r=4hk-a\) give

\[
 n_*={4Xh^2\over r^2},\qquad f(n_*)-kn_*={Xh\over r},
\tag{59.2}
\]

\[
 f''(n_*)=-{r^3\over32Xh^3}.
\tag{59.3}
\]

The projector, negative-curvature factor \(e(-1/8)\), and
\(\chi_4(a)=-\chi_4(r)\) combine to the leading coefficient

\[
 2\sqrt2\,e(1/8)\chi_4(r)
 {X^{1/2}h^{1/2}\over r^{3/2}}e(Xh/r).
\tag{59.4}
\]

At \(X\asymp R^4\), \(h\asymp R\), \(r\asymp R^2\), this coefficient
has size \(R^{-1/2}\).

## 3. Coefficient self-return and capacity

The stationary cone is

\[
 2h\sqrt{X/B}\leq r\leq2h\sqrt{X/A}.
\tag{59.5}
\]

For \(B-A\asymp R\), it has \(\asymp R\) integers for each of
\(\asymp R\) values of \(h\).  Thus its raw absolute capacity is
\(R^2\), and the desired short-window bound requires the genuinely signed
raw estimate \(O_\varepsilon(RX^\varepsilon)\).

At the saddle,

\[
 2h\sqrt{X/n_*}=r,
\tag{59.6}
\]

so the actual angular coefficient returns exactly to

\[
 \sum_j\mathbf1_{h\leq H_j}
 \Phi\!\left({h\over H_j+1}\right)[w_j(r)]^*.
\tag{59.7}
\]

The transform therefore preserves the denominator profiles, height floors,
hard top, and equality stars.  It does not manufacture a generic smooth
two-variable weight.

## 4. Exact Hessian and arithmetic obstruction

With \(r=4Kh+s\),

\[
 \Psi_K(h,s)={Xh\over4Kh+s},\qquad \chi_4(r)=\chi_4(s),
\]

and

\[
 \Psi_{hh}=-{8KXs\over r^3},\quad
 \Psi_{hs}={X(4Kh-s)\over r^3},\quad
 \Psi_{ss}={2Xh\over r^3},
\]

\[
 \det\nabla^2\Psi_K=-{X^2\over r^4}\asymp-1.
\tag{59.8}
\]

On the critical strip the mixed entry is order one, the other entries are
at most order one, and the two eigenvalues have opposite signs and order
one.  This real nondegeneracy is insufficient on the integer lattice:
\(Q(u,v)=uv\) has determinant \(-1\), yet \(e(Q(u,v))=1\) for all
integers \(u,v\).  Fourth-power and quarter-frequency controls likewise
rule out a coefficient-free derivative-gap shortcut.

## 5. Exact open seams

Two distinct statements remain unproved:

1. a uniform Poisson/B-process identity for the sharp window and complete
   actual symbol, including artificial endpoints, nonstationary terms,
   hard/profile seams, and colliding stars;
2. even after granting that identity, the signed reciprocal-strip estimate

\[
 \sum_{h\asymp R}\sum_{r\in\mathcal C_h(J)}^*
 \chi_4(r)W_X(h,r)e(Xh/r)
 \ll_\varepsilon RX^\varepsilon.
\tag{59.9}
\]

The phase and scale in (59.9) are those of the accepted terminal M1
theorem, with \(D\asymp R^2\), \(L\asymp R\), but the short-window cone
is an \(h\)-dependent strip.  It has not been decomposed with
\(X^\varepsilon\) total cost into the theorem's separable BV frequency
coefficient and \(h\)-independent denominator profile.  Hence the
terminal return is a precise next audit, not a proved implication.

## 6. Source and evidence controls

The blind report independently verifies (59.1)--(59.8), the factor
\(2\sqrt2\), and the \(R^2\)-versus-\(R\) ledger.  The hostile audit
supplies the strict \(uv\) countermodel and checks the coefficient-class
failure.  Its primary-source audit finds no directly applicable theorem
among Graham--Kolesnik, Vorhauer--Wirsing, Huxley, Jutila, or
Duke--Friedlander--Iwaniec.  These are non-importability findings, not a
claim that no relevant theorem exists.  No numerical evidence was used.

## 7. State recommendation

Create one proved reduction containing the exact projector, interior
stationary normalization, coefficient self-return, corrected strip
capacity, and Hessian obstruction.  Reject determinant-only closure,
short-window counting closure, an anisotropic \(R,R^{-1}\) Hessian ledger,
and automatic application of the terminal theorem.  Keep the signed short
twisted-divisor core, lower shell, alpha transfer, M9-M1, M9, and the
Gauss-circle exponent open.  The next round should audit the full critical
radial block against the already proved terminal-frequency divisor theorem,
where a fixed-relative-width cutoff may be separable even though a
length-\(R\) cutoff is not.

# Conductor review: W3 provenance and the alpha-branch boundary

Campaign: `m9-m1-beta-wrapper-closure-audit`  
Round: 48

## W3 formula provenance

The statement-only reviewer correctly observed that the frozen Round-48
packet, by itself, does not reproduce the formula-level hypotheses of the
moving-logarithm lemma or the local face coefficient. That observation
does not block the graph node at its package-level meaning. The
authoritative graph already contains the following proved statements:

1. `M9-M1-moving-logarithm-Fresnel-lemma`, including moving
   log/saddle/endpoint coalescence and both Hessian signs;
2. `M9-M1-beta-R1-face-log-q4-bound`, including the exact
   \(1/[y(A+iy/2)]\) decomposition and the local \(q^{-4}\) face
   coefficient;
3. `M9-M1-beta-two-saddle-Fresnel-normal-form`, including exact Morse
   entry, exit, and half-Fresnel normalization;
4. `M9-M1-beta-large-alpha-transition-package-bound`, which identifies
   these local inputs with the actual post-routing fixed-ratio beta cells
   and executes their coefficient sum; and
5. `M9-M1-beta-fixed-ratio-smooth-cutoff-invariance`, which transfers the
   result to the repaired middle partition without changing the saddle
   coefficient.

Accordingly W3 is promoted only as a wrapper around those accepted
formula-level nodes. No fresh moving-log identity is inferred from a
theorem title, and no stationary numerator is applied to compact or
nonsaddle cells.

## Downstream interface correction

Put

\[
 A=s-z/2,\qquad B=s+z/2.
\]

The accepted finite one-factor identities distinguish two traces:

\[
 \begin{array}{ll}
 \text{beta bounded:}&
 \zeta(1-A)X_4(B)L(B,\chi _4),\\[2mm]
 \text{alpha bounded:}&
 X_\zeta(A)\zeta(A)L(1-B,\chi _4).
 \end{array}
\]

Round 48 closes the first line only. The second line has unsigned high
coefficients \(h^{-A}\), and its connector-completed physical trace,
outside-height limit, and axial/top/corner reconciliation have no accepted
target-sized estimate. Therefore the graph must name that alpha branch as
an explicit open dependency of the swept operator. The existing edge from
the beta wrapper to the swept operator is retained only in the sense that
the beta wrapper supplies one necessary branch; it is not a sufficient
promotion edge.

## State recommendation

Promote W1--W4 sequentially, create the explicit alpha-bounded zeta-high
obligation, and keep every downstream node open. Do not revive
coefficientwise Abel, side-free contour shifts, simultaneous ordinary
Dirichlet chambers, or absolute height integration as shortcuts for the
alpha branch.


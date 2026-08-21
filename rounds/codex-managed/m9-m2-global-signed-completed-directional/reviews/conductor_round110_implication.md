# Conductor review: exact global real-part implication

Campaign: m9-m2-global-signed-completed-directional

Starting graph SHA-256:
33bf8e043cb8a1e0852b7f98941ee6186f798ed40124525de3d0373269019397

## Algebra

Write the accepted finite identities as

\[
 \mathcal E_L^{\mathrm{top}}
 =\mathcal E_{\mathrm{owned},L}
  +2\Re\sum_B\mathfrak Q_B^{\mathrm{res}},
\]

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}-\sum_\nu\mathfrak O_{B,\nu}.
\]

Define

\[
 \mathfrak C_L^{\mathrm{comp}}
 =\sum_B\mathfrak Q_B^{\mathrm{comp}},
\qquad
 \widetilde{\mathcal E}_{\mathrm{owned},L}
 =\mathcal E_{\mathrm{owned},L}
  -2\Re\sum_{B,\nu}\mathfrak O_{B,\nu}.
\]

Then, without an inequality or interchange of infinite sums,

\[
 \boxed{
 \mathcal E_L^{\mathrm{top}}
 =\widetilde{\mathcal E}_{\mathrm{owned},L}
  +2\Re\mathfrak C_L^{\mathrm{comp}}.}
\tag{110.C1}
\]

The Round-109 bound gives

\[
 |\widetilde{\mathcal E}_{\mathrm{owned},L}|
 \le |\mathcal E_{\mathrm{owned},L}|
  +2\sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{110.C2}
\]

Consequently

\[
 \mathcal E_L^{\mathrm{top}}\ll_\varepsilon L^2X^\varepsilon
 \quad\Longleftrightarrow\quad
 \Re\mathfrak C_L^{\mathrm{comp}}
 \ll_\varepsilon L^2X^\varepsilon,
\tag{110.C3}
\]

where the equivalence is at the level of one-sided upper bounds with
possibly changed constants. Positivity of
\(\mathcal E_L^{\mathrm{top}}\) further gives the automatic lower bound

\[
 \Re\mathfrak C_L^{\mathrm{comp}}
 \gg_\varepsilon -L^2X^\varepsilon.
\tag{110.C4}
\]

Thus the hard-energy theorem is also equivalent to
\(|\Re\mathfrak C_L^{\mathrm{comp}}|\ll L^2X^\varepsilon\).
It is not equivalent to
\(|\mathfrak C_L^{\mathrm{comp}}|\ll L^2X^\varepsilon\), which controls
an unused imaginary component.

## Norm hierarchy

The exact hierarchy is

\[
 |\Re\sum_BQ_B|
 \le |\sum_BQ_B|
 \le \sum_B|Q_B|.
\tag{110.C5}
\]

Neither reverse inequality holds for arbitrary complex blocks:

- \(Q_1=iM\) makes the left member zero while the modulus is \(M\);
- \(Q_1=M,\ Q_2=-M\) makes the global modulus zero while the blockwise
  norm is \(2M\).

A row energy or positive Gram has no implication without an explicit
normalization and bridge. Hence (110.C3), not a blockwise norm or Gram,
is the minimal physical target.

## Finite recombination gate

All block and owner sets are finite, so the sums in (110.C1) may be
reordered. Removing the block labels from the displayed kernel is a
different step: it is lawful only after the smooth \(A,D,K,G,R\)
weights are shown to form a literal pointwise one-count partition on
the same finite atom space, including half-open boundaries, terminal
metric member, and exact-center subtraction.

The conductor therefore certifies (110.C1)--(110.C5) now, but leaves
the simplified literal formula for
\(\mathfrak C_L^{\mathrm{comp}}\) to the Round-110 kernel and hostile
audits.

## Scope

This review proves an exact implication, not the missing estimate.
Neither the fixed-\(a\) Gram, hard energy, hard cone, either smooth M2
packet, M9-M2, M9-M1, M9, endpoint uniformity, nor an exponent is
promoted.

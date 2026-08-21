# Round 101 conductor normalization and period review

## DFT and row normalization

The conductor independently expanded

\[
 \sum_jw_jF_j\overline{G_{j-v}}
\]

with the unnormalised length-\(L\) DFT. Three inverse transforms and the
single \(j\)-orthogonality sum give \(L^{-2}\), the translated conjugate
gives \(e_L(lv)\), and the constraint is \(r+k-l=0\). This reproduces

\[
 L^{-2}\sum_{k,l}e_L(lv)\widehat w_{l-k}
 \widehat F_k\overline{\widehat G_l}.
\]

The statement-only packet listed the two pair sequences but did not display
their coupling. Its first draft used a bilinear rather than sesquilinear
product. The conductor supplied only the canonical conjugation datum; the
blind report then corrected every sign and independently recovered this
formula. The final statement-only report is therefore usable evidence with
that correction disclosed.

The normalized Fourier matrix is exactly the Fourier conjugate of a
unimodular multiplication and a cyclic shift. It is full-rank unitary.
Thus a constant weight, a pure character, or sparse Fourier support cannot
give a coefficient-blind power saving.

The completed-trace and physical-row normalizations also reconcile:

\[
 {\mathfrak T_M\over M^2}
 ={\mathfrak T_q\over q^2}{\mathfrak T_N\over N^2},
 \qquad M^{-5}\mathfrak T_M=M^{-4}\sum_x^{\mathrm{mask}}w_x.
\]

There is one \(M^{-1}\) in each physical row and no extra local-lift factor.

## Twisted-period proof

The reports agree on the guaranteed reciprocal period

\[
 P_\nu=1\ (\nu\le3),\qquad P_4=2,
 \qquad P_\nu=L/8\ (\nu\ge5).
\]

The conductor reproduced it using
\((z+h)^{-1}-z^{-1}=-h[z(z+h)]^{-1}\). The mod-\(8\) bracket is constant
on odd \(z\) for the required shift, so the four signed inverse differences
cancel. Therefore

\[
 w_{j+P_\nu}=e_L(u_2P_\nu)w_j,\qquad
 \operatorname{supp}\widehat w
 \subseteq u_2+(L/P_\nu)\mathbb Z/L\mathbb Z.
\]

This is a twisted period of the complete affine weight and a period of its
reciprocal factor. It is not asserted to be fundamental. A bounded symbolic
diagnostic checked every even \((A,B_2,V)\) through \(q=32\) and sampled
higher powers through \(q=1024\); it found no counterexample. That
computation is diagnostic only and is not used as proof.

## Class and scope review

The three accepted class moduli are handled at their literal
\(2\)-adic valuations. Under the standard meaning of \(\bar4\pmod b\), the
\(\kappa=2,4\) rows require odd \(b\), so their two-parts are \(2\) and
\(1\); higher two-parts arise in the \(\kappa=1\) row. The general
\(M=2^\nu N\) formula remains valid if a later artifact supplies a different
convention.

All actual rows, odd inverse phase, nonunit \(K\), nonzero modulus
multiples, entry/exit, stars, and zero extension are retained. No source
theorem is imported.

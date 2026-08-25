# Round 159 barrier packet

## Frozen object

Fix

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{159.B1}
\]

Only the open side \(M^{449}\ll R^{780}\), with \(R=X^{1/4}\), can
supply a new analytic range.  The known opposite TTY/BD side and the
fixed-polylogarithmic defect collar are accepted inputs, not gains.

The only frozen object is the full sign-adapted Abel decomposition of
the paired-interior \(D=d=L=1\) matrix: two outer endpoints, two moving
traces, and two profile-difference remainders, summed over every odd
divisor and every paired interior frequency.  All pieces must be
recombined before any separate estimate.

## Accepted inputs

The literal coefficient is

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right).
\tag{159.B2}
\]

Complete-frequency inversion returns

\[
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}B_j(x)G_N(x^2-j).
\tag{159.B3}
\]

The zero and Nyquist whole rows are separately proved
\(O_\varepsilon(M^{-1/4}X^\varepsilon)\).  They may be subtracted
exactly once after full-frequency inversion.

## Rejected gains that remain rejected

- The endpoint face is not the strict trace.
- The two isolated boundary profiles are not equal and are not
  conjugate.
- Support \(O_\varepsilon(\min(M,V)X^\varepsilon)\) is unsigned.
- Top-block localization of the isolated trace is not a target bound.
- Whole-row zero or Nyquist theorems do not transfer to Abel pieces.
- One-variable profile BV does not control a moving diagonal mask.
- A fixed-endpoint Vaaler model is not the literal variable mask.
- The audited \(M\ge N^{390/703}\) favorable-model threshold is not a
  universal lower bound or impossibility theorem.
- Outer endpoints do not cancel across dyadic blocks unless an exact
  partition identity is printed.
- Trace control alone does not control the full paired matrix.

## New exact opportunity

The full Abel sum may restore the quotient profile at selected points.
With

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell,
\tag{159.B4}
\]

the candidate compressed object is

\[
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|r(\ell)|\le2V}.
\tag{159.B5}
\]

Equation (159.B5) is not an accepted result until independently
rederived.  Even if exact, it supplies no cancellation by itself.

## Required analytic ledger

Any attack on (159.B5) must print:

1. the exact fractional-part description
   \(r=-\delta(2\kappa+\delta)\);
2. all Fourier truncation, boundary, and variable-endpoint errors;
3. the coefficient class and variation of \(w_U\);
4. the \(\chi_4\) twist, including its shifted zero mode;
5. the uniform \(N,M,V\) range and every transition;
6. the raw \(M^{3/4}X^\varepsilon\) target;
7. restoration of the \(M^{-3/4}\) atom scale; and
8. zero, fold, external scalar, endpoint, and downstream seams.

## Downstream quarantine

No result transfers automatically to another \(D,d,L,t\) layer, the
cross owner, another M1 or M2 component, endpoint uniformity, M9, the
bridge, the quarter theorem, or either global exponent.

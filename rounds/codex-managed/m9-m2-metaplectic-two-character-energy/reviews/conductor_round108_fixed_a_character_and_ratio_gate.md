# Conductor review: fixed-\(a\) character cancellation and ratio gate

Campaign: m9-m2-metaplectic-two-character-energy

Starting graph SHA-256:
7347081c1a765acafc6a4d1e3a96171d7b971079c2af144f7a0eaa825309bb2a

## Character location before and after the Gram lift

In the accepted fixed-\(a\) row notation, \(F_a(q)\) does not contain the
primitive-ray character. The oriented linear block is

\[
 \mathfrak Q=\sum_{a,q}(-1)^qF_a(q),
 \qquad
 (-1)^q=\chi_4(a)\chi_4(a+2q).
\]

The sufficient Gram is

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|\sum_{0\le j<H}(-1)^jF_a(n+j)\right|^2.
\]

After expansion, its shift-\(s\) correlation has the explicit
multiplier

\[
 (-1)^s\chi_4(a)\chi_4(a+2q+2s)
          \chi_4(a)\chi_4(a+2q)=1.
\]

Indeed, \(\chi_4(a)^2=1\) and
\(\chi_4(a+2q+2s)\chi_4(a+2q)=(-1)^s\). Thus the
external Fejer alternation cancels the varying primitive-ray character
exactly. There is no residual \(\chi_4\)-orthogonality inside a
fixed-\(a\) Gram correlation. A two-character argument can still act
on the linear block before the Gram lift, or on the complete
phase-weighted four-row correlation, but it cannot obtain the required
\(\rho^{-1}\) energy gain merely by estimating the two characters
independently.

## Exact ratio-band coupling

Put \(z=k/J\) and \(t=\sqrt{b/a}\). The reciprocal interval is
equivalent to

\[
 {t-1\over2}<z<{t-1\over t}.
\]

Consequently, for \(0<z<1/2\), the exact base-variable support is

\[
 {1\over1-z}<t<1+2z,
 \qquad
 {a\over(1-z)^2}<b<a(1+2z)^2.
\]

This is the first non-product coupling left after the accepted
factorization of \(A_{ga,gb}^{\circ}(gu)\). For a smooth cutoff
\(w_z(t)\) compactly supported strictly inside this interval, ordinary
Mellin inversion gives

\[
 w_z(\sqrt{b/a})
 ={1\over2\pi}\int_{\mathbb R}
   \widehat w_z(\xi)\,b^{i\xi/2}a^{-i\xi/2}\,d\xi,
\]

with integrable projective norm controlled by finitely many uniform
seminorms of \(w_z\). The literal sharp indicator is different: its
Fourier transform in \(\log t\) has a \(1/|\xi|\) tail. A logarithmic
finite-scale separation therefore requires an explicit smoothing or
ordered-prefix endpoint lemma. No such lemma currently owns the exact
open reciprocal boundary, singleton fibres, or the zero extension.
The sharp band must not be silently assigned an \(X^\varepsilon\)
Mellin projective norm.

## Owner reinsertion is linear, not automatically Gram-safe

At the level of the oriented linear block, one may attempt to reinsert
already bounded owners, prove an estimate for a smoother complete sum,
and subtract every owner once. This maneuver does not transfer
formally to the positive fixed-\(a\) Gram: if
\(F=F_{\rm full}-F_{\rm owned}\), then \(\lVert F\rVert^2\)
contains two cross terms whose required local energy is not supplied by
a global linear bound for \(F_{\rm owned}\). Hence either the
two-character estimate must be applied directly to the linear block,
or the owner projectors and their cross energies must remain inside the
transformed Gram.

## Capacity consequence

The exact Gaussian kernel is a free metaplectic propagator. Its Fourier
multiplier has modulus one, and each separate one-character
\(\chi_4(n)e(\tau\sqrt n)\) B-process preserves squared coefficient
mass. Combining these facts with the preceding character cancellation
shows that the following route is equal-capacity:

1. lift to the fixed-\(a\) Gram;
2. open the metric window;
3. Gaussian-separate the two radicals;
4. estimate the two character rows separately by Plancherel or their
   individual B-processes.

The smallest unresolved alternatives are therefore:

- a direct linear two-character estimate for the complete sharp-ratio
  block, including owner reinsertion and all chirp modes; or
- an outside-absolute estimate for the character-neutral, actual-phase
  fixed-\(a\) cross-\(q\) correlation.

Neither alternative is proved here. No hard-cone, \(M9\!-\!M2\), or
global-exponent consequence follows from this review.

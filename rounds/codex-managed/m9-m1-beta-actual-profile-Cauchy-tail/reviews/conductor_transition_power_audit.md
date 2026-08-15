# Conductor audit: tangent-height power and why it is not yet a tail

Campaign: `m9-m1-beta-actual-profile-cauchy-tail`  
Role: conductor independent power bookkeeping  
Allocation: 100% analytical/algebraic

On the beta branch, use

\[
\alpha=t+(\mu+\nu)/2,\qquad
\beta=t-(\mu+\nu)/2.
\]

The exact gamma quotient factors as (K=C R_\alpha R_\beta).  For
bounded beta and large \(|\alpha|\), the accepted one-factor Stirling
formula gives

\[
|R_\alpha|\asymp
|\alpha|^{c'+(a+b)/2-1/2},
\tag{38.C5}
\]

while (R_\beta) remains an exact bounded meromorphic factor away from its
listed poles.  This is polynomial growth, not height decay.

For the post-endpoint radial remainder,

\[
R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}
\int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx.
\tag{38.C6}
\]

Away from the artificial seam, \(|\rho|\asymp|\alpha|\) on the stationary
mass, so the displayed denominator supplies one inverse power.  The hard
top supplies a second inverse power only after the signed delta/PV
convolution and only on a separated saddle patch.  Stationary phase then
restores its square-root factor, and the accepted local conclusion is the
(D_j/(q\alpha_0)) coefficient, equivalently local (q^{-2}), rather than
a free global power of \(|\nu|\).

The global tail has a second direction.  If \(\alpha\) is fixed while
\(|\nu|\to\infty\), beta support forces

\[
\mu=\alpha-\beta-\nu,
\tag{38.C7}
\]

so the smooth interior (\widehat W_j(a+i\mu)) decays rapidly.  For the
top scale, however, (\widehat W_0=1/u+\widehat W_{+,r}): the regular part
decays rapidly but the (1/u) term has only inverse tangent height and is
already part of the signed Plemelj operator.  Thus a plausible global proof
must split:

- large \(|\alpha|\): use the two signed saddle/nonstationary analysis and
  the (R_1\)-top two-denominator structure;
- bounded \(|\alpha|\), large \(|\nu|\): use smooth-transform decay plus
  the exact Hilbert-tail cancellation of the top term;
- \(\rho=O(1)\): use \(\nu=-\alpha-\beta+O(1)\) and cubic
  \(\widehat\phi\) decay under the common omega germ;
- bounded double transition: use the compact central-box theorem.

These regions are analytically promising and jointly exhaustive after an
appropriate smooth partition.  What is not yet licensed is a single
uniform integrable bound on the hard-top divided difference at the
interfaces \(|\alpha|\asymp1\), \(|\rho|\asymp1\), and the moving finite
faces, followed by the actual (h,q,j,x) sums.  Round 38 must prove that
patching estimate rather than reuse (38.C5) as an absolute tail bound.

No numerical experiment or external theorem was used.

# Conductor derivation: beta-slab coordinates

Campaign: `m9-m1-beta-actual-profile-cauchy-tail`  
Role: conductor independent algebra  
Allocation: 100% analytical/algebraic

Write

\[
u=a+i\mu,\quad v=b+i\nu,\quad s=c'+it,
\qquad
\beta=t-\frac{\mu+\nu}{2}.
\]

Use the linear coordinates

\[
(\mu,\nu,t)=(\mu,\nu,\beta+(\mu+\nu)/2).
\tag{38.C1}
\]

The transformation is triangular and has Jacobian one.  The two completed
factor heights become

\[
\operatorname {Im}(s-(u+v)/2)=\beta,
\qquad
\operatorname {Im}(s+(u+v)/2)=\alpha=\beta+\mu+\nu.
\tag{38.C2}
\]

Thus compact beta support leaves one unbounded tangent height \(\alpha\),
not two independent large completed-factor heights.  The radial denominator
is

\[
\rho=\frac14-s-\frac v2
=\rho_0-i\left(\beta+\frac\mu2+\nu\right),
\qquad
\rho_0=\frac14-c'-\frac b2.
\tag{38.C3}
\]

Equivalently \(2\operatorname {Im}(-\rho)=\alpha+\beta+\nu\).
Consequently the large tangent-height problem has three distinct regions:

1. \(|\rho|\asymp|\alpha|\), where the explicit \(R_1\) denominator gives
   one inverse height;
2. the artificial seam \(\rho=O(1)\), which forces
   \(\nu=-\alpha-\beta+O(1)\) and hence gains cubic decay from
   \(\widehat\phi(b+i\nu)\);
3. the hard-top seam \(\mu=0\), handled only by the combined
   \((1/2)\delta-(i/(2\pi))\operatorname{PV}\) operator.

The first region contains the two signed saddles already found in Round 28.
The accepted local calculation shows that after the signed top convolution
the separated stationary \(R_1\) coefficient has local \(q^{-2}\) size.
This is not a global \(\nu\)-tail estimate, because in (38.C1)
\(\nu\to\infty\) can be offset by \(\mu\sim-\nu\), leaving \(\alpha\)
bounded while the top PV and height profile are coupled.  Conversely,
\(|\alpha|\to\infty\) may occur with \(\nu\) bounded.  Any valid tail proof
must therefore partition by \((\alpha,\nu,\rho)\), not apply decay of
\(\widehat\phi(v)\) or the local saddle estimate alone.

For the hard-top part, the exact sufficient Cauchy datum is a uniform
integrable bound for the value at \(\mu=0\) and the divided difference

\[
\frac{B_{\rm top}(i\mu,b+i\nu,c'+it)
      -B_{\rm top}(0,b+i\nu,c'+it)}{\mu},
\tag{38.C4}
\]

after substituting (38.C1), plus the regular top-profile integral.  The
Jacobian calculation alone supplies no decay for (38.C4).  This identifies
the algebraic interface that the three Round-38 tasks must estimate.

No numerical experiment or external theorem was used.

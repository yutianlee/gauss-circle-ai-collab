# Round 105 conductor Mobius-dual character audit

Campaign: m9-m2-polynomial-q-maximal-alternation

## Primitive progression

Expand

\[
 \mathbf 1_{(a,q)=1}
 =\sum_{d\mid a,\ d\mid q}\mu(d).
\]

Every \(d\mid a\) is odd.  On the progression \(q=du\), the outer
alternation satisfies \((-1)^{du}=(-1)^u\), while it is legitimate to
retain the phase as \(du/2\) because \((d-1)u/2\) is integral.

After the scalar \(k\)-process, write

\[
 F_d(u)={du\over2}
 -J\left(\sqrt{a+2du}-\sqrt a\right)\sqrt{n\ell}.
\]

Pairing with the dual integer \(h\), set

\[
 s=d-2h.
\]

The relevant orientation has \(s>0\), and \(s\) is odd.  The saddle is

\[
 b_*=a+2du_*={4d^2Xn\ell\over s^2}. \tag{105.M1}
\]

## Exact dual phase

At the saddle,

\[
\begin{aligned}
 F_d(u_*)-hu_*
 &={s(b_*-a)\over4d}
   -J\sqrt{n\ell b_*}+J\sqrt{an\ell}\\
 &=-{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}\\
 &=-\left(
 J\sqrt{dn\ell\over s}-{1\over2}\sqrt{as\over d}
 \right)^2. \tag{105.M2}
\end{aligned}
\]

Since \(a/d\) and \(s\) are odd,

\[
 e\!\left(-{as\over4d}\right)
 =-i\,\chi_4(a/d)\chi_4(s). \tag{105.M3}
\]

Thus exact primitive decomposition does not destroy the character.  It
turns the alternating \(q\)-lattice into an odd dual denominator carrying
\(\chi_4(s)\), with reciprocal phase \(e(-dXn\ell/s)\) and radial factor
\(e(J\sqrt{an\ell})\).

## Interpretation

Equations (105.M1)--(105.M3) expose the smallest natural dual survivor:
an actual-weight, odd-character reciprocal row in \(s\), coupled to the
product \(dn\ell\), the radial phase, the transformed collars, and all
prior owners.  The identity is exact at the scalar saddle level, but it
is not a bound.  Applying a generic reciprocal theorem requires a literal
amplitude dictionary, uniform entry/exit and stationary errors, and a
one-count transport of every owner.  Without that dictionary, invoking a
terminal M1 estimate or summing the dual row absolutely would overstate
the result.

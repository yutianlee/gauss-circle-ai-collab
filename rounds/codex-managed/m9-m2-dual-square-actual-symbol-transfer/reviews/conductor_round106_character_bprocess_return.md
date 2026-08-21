# Conductor review: character B-process returns the primitive ray

Campaign: m9-m2-dual-square-actual-symbol-transfer

Starting graph SHA-256:
2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## Returned dual carrier

After the two Round-105 stationary operations, put

\[
 H={a\over d},\qquad M=dn\ell,\qquad r=s.
\]

The carrier is

\[
 -i\chi_4(H)\chi_4(r)
 e(-XM/r+J\sqrt{HM}). \tag{106.B1}
\]

The sharp maximal support is

\[
 b_*={4dXM\over r^2}\in a+2I. \tag{106.B2}
\]

## Character B-process

Use

\[
 \chi_4(r)={e(r/4)-e(3r/4)\over2i}.
\]

Poisson summation in \(r\) has odd dual \(p\). On either residue branch
the stationary point and value are

\[
 r_*={2\sqrt{XM}\over\sqrt p},\qquad
 -{XM\over r_*}-{pr_*\over4}=-\sqrt{XMp}. \tag{106.B3}
\]

The two residue branches combine into

\[
 e(1/8)(XM)^{1/4}\chi_4(p)p^{-3/4}
 e(-\sqrt{XMp}) \tag{106.B4}
\]

times the transformed amplitude, up to the usual exact transition and
nonstationary pieces.

At the stationary point,

\[
 p={4XM\over r_*^2}={b_*\over d}. \tag{106.B5}
\]

Therefore (106.B2) becomes

\[
 p\in H+{2I\over d},\qquad b_*=dp, \tag{106.B6}
\]

which is exactly the original Möbius progression \(q=du\),
\(p=H+2u\).

The total phase after (106.B4) is

\[
 J\sqrt{HM}-J\sqrt{pM}
 =-J(\sqrt p-\sqrt H)\sqrt M. \tag{106.B7}
\]

For \(d=1\), this is exactly the post-\(k\)-transform primitive-ray
phase

\[
 -J(\sqrt b-\sqrt a)\sqrt{n\ell}.
\]

For general \(d\), it is the same phase on the Möbius-rescaled
progression. Thus the returned character does not create a new separated
terminal object: its own B-process reconstructs the original \(u\)-row
and maximal interval.

## Interpretation

At carrier level, (106.B3)--(106.B7) prove a third-transform return:

\[
 (u,k,\text{physical})\longrightarrow(\ell,r)
 \longrightarrow(\ell,p)
\]

with \(p=H+2u\). If all Fourier transforms, endpoint terms and
nonstationary modes are retained exactly, inversion is automatic even for
arithmetic owner masks. A stationary-main-only formula still requires
uniform error control before it can be called an owner-preserving
self-return.

This return rejects three shortcuts:

1. bounded partial sums of \(\chi_4(r)\) do not give an independent
   saving;
2. the terminal M1 theorem cannot be applied after forgetting the
   resonant \(p=H+2u\) return;
3. a gain from the scalar \((q,k)\) Hessian cannot be multiplied by a
   second gain from the character B-process.

The review does not exclude a direct estimate of the complete actual
dual vector before the returning transform.

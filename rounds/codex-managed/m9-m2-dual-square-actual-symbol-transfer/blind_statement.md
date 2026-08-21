# Round 106 statement-only packet

Campaign: m9-m2-dual-square-actual-symbol-transfer

This packet is self-contained. Do not read the proof graph, proof draft,
strategy files, Round-106 derivation packet or candidate, claimant reports,
or any earlier derivation.

Let \(J=\sqrt X\), \(1\le L\le J^{1/2}\), and fix odd \(a\). On a
half-open shell,

\[
 b=a+2q,\qquad a\asymp b\asymp A,\qquad q\asymp D,\qquad
 a<b<4a,\qquad (a,q)=1.
\]

For one orientation of the literal residual row, write

\[
 F_a(q)=\mathbf 1_{\rm own}(a,q)
 \sum_{\substack{g\ {\rm odd}\\g\in\mathcal G_{a,b}}}
 \sum_{\nu\in\mathbb Z}\widehat W_R(\nu)
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}(k)
 e\!\left(\left(\nu-\frac g2\right){\Lambda_q\over k}\right),
\]

where

\[
 \Lambda_q={X(\sqrt{a+2q}-\sqrt a)^2\over2},\qquad
 I_{a,q}=\left({J(\sqrt{a+2q}-\sqrt a)\over2\sqrt a},
 {J(\sqrt{a+2q}-\sqrt a)\over\sqrt{a+2q}}\right).
\]

The symbol \(B_{a,q,g}(k)\) is the complete centered physical integral
times the literal fixed profiles. It retains collars, floors, stars,
finite lift support and all owner complements. At fixed \(q\),

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname{Var}_kB_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over JD}.
\]

Every \(g\) is odd, so for \(c=\nu-g/2\),
\(n=|2\nu-g|\ge1\). The target maximal theorem is

\[
 \sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|
 \ll_\varepsilon X^\varepsilon {L^2\over A}.
\]

After

\[
 \mathbf1_{(a,q)=1}=\sum_{d\mid a,\,d\mid q}\mu(d),\qquad q=du,
\]

the scalar carrier for \(c=-n/2\) is

\[
 {du\over2}-{n\Lambda_{du}\over2k}.
\]

A formal \(k\)-stationary transform with dual \(\ell>0\), followed by a
formal \(u\)-stationary transform with dual \(h\), \(s=d-2h>0\) odd,
has

\[
 k_*^2={n\Lambda_{du}\over2\ell},\qquad
 b_*={4d^2Xn\ell\over s^2},
\]

and phase

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2.
\]

Independently derive the stationary normalizations and support, then
decide what additional hypotheses are required to turn this scalar
carrier calculation into a complete transform of the actual coefficient.
Track the centered physical oscillation rather than silently treating it
as a harmless scalar amplitude. Determine the exact capacity consequence
and the first smaller unproved actual-vector inequality. Any claimed
estimate must retain the maximal cutoff and all owner masks.

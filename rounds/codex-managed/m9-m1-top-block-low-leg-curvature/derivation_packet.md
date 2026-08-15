# Round 55 derivation packet: fixed-leg curvature on the critical top block

This packet freezes a subproblem of the accepted Round-54 Fejer interface.
It does not assert a margin estimate.

## 1. Exact top-block object

Let \(I_Y\) be a consecutive integer interval contained in a fixed compact
multiple of \(Y\), where

\[
 Y\asymp\sqrt X,
 \qquad
 R\asymp\sqrt Y\asymp X^{1/4},
 \qquad 1\le R\le |I_Y|.
\]

Retain the exact angular coefficient

\[
 A_X(n)=\sum_{hq=n,\ q\ {m odd}}\chi_4(q)\Omega_X^*(n,h),
\]

\[
 \Omega_X^*(n,h)=\sum_j\mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

The accepted profiles have fixed dyadic support and bounded smooth
seminorms on interior scales, bounded overlap, and one one-sided hard-top
profile.  The Vaaler profile \(\Phi\) is \(C^1[0,1]\), bounded, and has
bounded derivative.  Every equality star and the hard-top jump must remain
explicit.

For cutoffs \(H,Q\ge1\), define the union-of-margins coefficient

\[
 A_{X;H,Q}(n)=
 \sum_{\substack{hq=n,\ q\ {m odd}\\h\le H\ {m or}\ q\le Q}}
 \chi_4(q)\Omega_X^*(n,h),
\]

with the overlap counted once, and its radial block sum

\[
 S_{Y;H,Q}=\sum_{n\in I_Y}^{*}
 A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn}).
\]

## 2. Moving-window reduction

The accepted Fejer identity shows that a uniform estimate on every product
interval \(J\subseteq I_Y\) of length at most \(R\), including edge
intervals,

\[
 \left|\sum_{n\in J}^{*}
 A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon X^\varepsilon\frac{H+Q}{\sqrt Y}
\tag{55.1}
\]

would imply

\[
 S_{Y;H,Q}\ll_\varepsilon X^\varepsilon(H+Q).
\tag{55.2}
\]

In particular, \(H+Q\le(\log(2X))^B\) would be target-safe.  Derive (55.1)
rather than assuming it, and audit the exact Fejer constants and edge
windows.

## 3. Frozen fixed-leg phases

For fixed \(h\), the relevant inner sum is over an odd-q interval of length
at most \(R/h+O(1)\), with phase

\[
 f_h(q)=\sqrt{Xhq},
 \qquad
 |f_h''(q)|\asymp \frac{h^2\sqrt X}{Y^{3/2}}\asymp\frac{h^2}{R}
 \quad(q\asymp Y/h).
\tag{55.3}
\]

For fixed odd \(q\), the h-interval has length at most \(R/q+O(1)\), with

\[
 g_q(h)=\sqrt{Xqh},
 \qquad
 |g_q''(h)|\asymp\frac{q^2}{R}
 \quad(h\asymp Y/q).
\tag{55.4}
\]

When a fixed leg is at most \(\sqrt R\), a lawful second-derivative estimate
should be tested.  When it exceeds \(\sqrt R\), the corresponding interval
has length at most \(\sqrt R+O(1)\), so trivial summation is the intended
crossover.  Restricting q to odd integers inserts the exact period-four
character; it may be written as two linear phase shifts, but no cancellation
may be claimed merely from that representation.

The missing amplitude input is a uniform sampled sup-plus-variation bound
for \(\Omega_X^*(hq,h)\) as q moves, and for
\(\Omega_X^*(hq,h)\) as h moves, on every product window.  Prove this from
the fixed profiles, height floors, monotone angular coordinate, bounded
overlap, and the separately retained hard-top jump, or identify the first
failure.

## 4. Mandatory controls and scope

- Treat \(X=K^4\) and the resulting integer/half-integer linear phases as a
  mandatory resonance control.  Curvature, not an unverified first-
  derivative gap, must carry the claim.
- Do not apply a second-derivative lemma in a regime where its hypotheses
  fail modulo the integer lattice; use the trivial crossover when needed.
- The cutoff \(h\le H_j\) is fixed on a fixed-h q-sum but moves on a fixed-q
  h-sum.  Its sampled jumps must be counted.
- A profile equality star changes a sampled endpoint value, while a hard
  step contributes a full variation jump.  Keep these distinct.
- The h-low and q-low families overlap.  Use inclusion-exclusion or a
  disjoint owner rule.
- A low-margin theorem leaves the balanced core
  \(h>H\), \(q>Q\), \(hq\asymp Y\).  It does not prove the full Round-54
  shifted correlation, GAR, the alpha transfer, M9-M1, M9, or the target.

No numerical experiment is needed.  The round is 100% analytical.

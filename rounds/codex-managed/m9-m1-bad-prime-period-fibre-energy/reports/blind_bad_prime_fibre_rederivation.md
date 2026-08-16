## 1. Result

The packet does permit a complete local criterion for every reciprocal-weight
period, a complete first-descent classification at (p=3,5,7), and a
genuinely (2)-adic (not parity-only) uniform descent lemma.  It does not
permit a target-safe directed-graph package to be certified.

Write

\[
 S_p=\{0,\bar A,\bar V,\bar V+\bar B_2\}\subseteq\mathbf F_p,
 \qquad \kappa=\min(v_p(K_q),\nu),
\]

and, when \(\kappa<\nu\), put \(r=\nu-\kappa\).  If the mask is
nonempty, it has exact additive period (p).  If \(\kappa=\nu\), the
whole weight therefore has exact period (p).  If \(\kappa<\nu\), its
exact period is (p^{s_0}), where (s_0) is given by the finite-difference
criterion in Section 2.  In particular (s_0\leq r), so every
nonunit-(K_q) factor has the automatic completed descent
(j_q=\nu-s_0\geq\kappa).  This conductor descent by itself imposes no
condition on the second directed vertex and hence supplies no graph-degree
gain.

At the small primes the first extra descent is as follows.

- At (p=3), every nonempty mask is derivative-flat modulo (3), so
  (s_0\leq\max(1,r-1)).  This is sharp on an explicit cross-group
  family.
- At (p=5), derivative-flatness consists exactly of the two rationally
  trivial reductions, together with a four-distinct-pole/singleton-mask
  anomaly described in Section 2.  The anomaly is sharp on
  ((A,B_2,V)=(1,2,2)mod 5^\nu).
- At (p=7), derivative-flatness occurs only in the two rationally
  trivial reductions.  Thus every other nonempty local factor has exactly
  (s_0=r), or (j_q=\kappa).
- At (p=2), nonemptiness forces all four poles to be even.  For every
  allowed odd (x), translation by (2) changes \(\Phi\) by a multiple
  of (2^3), and translation by (2^s), (s\geq2), changes it by a
  multiple of (2^{s+3}).  Consequently
  \[
  s_0\leq
  \begin{cases}
  1,&r\leq3,\\
  \max(2,r-3),&r\geq4,
  \end{cases}
  \]
  and these uniform exponents are sharp.

The smallest explicit nondegenerate four-label local candidate furnished by
the packet is (q=8),

\[
 (A,B_2,V)=(2,2,4)\pmod 8,
 \qquad K_q\ hbox{odd}.
\]

Its four pole labels (0,2,4,6) are distinct modulo (8), its mask is the
odd residue fibre, and \(\Phi\equiv0\pmod8\) on that fibre.  Hence its
exact period is (2), (j_q=2), and (89.7) places it on (4\mid u_q)
with the required factor (2^{2j_q}=16).  Restricting the local factor in
(89.8) to these congruences, while retaining the full (n,m)-sum and
(89.9), is the smallest exact actual-symbol *candidate* isolated here.
The packet does not define (R_*), the directed vertex sets, or
\(\mathfrak T_q) in terms of (w_q), so it cannot certify that this
candidate survives the accepted owners, has a nonzero tensor coefficient,
or has both directed degrees at most \(\rho_*^2\).  Thus the rigorous final
outcome is a packet-level no-go for the requested target-safe package.

## 2. Exact statement and hypotheses

Assume (q=p^\nu\), use the complete mask and \(\Phi\) of (89.5)--(89.6),
and suppose \(\Omega_q\ne\varnothing\).  For (1\leq s\leq r), set
(h=p^s) and

\[
\begin{aligned}
 D_A(x,h)&=x(x-A)(x+h)(x+h-A),\\
 D_B(x,h)&=(x-V)(x-V-B_2)(x+h-V)(x+h-V-B_2),\\
 E_h(x)&={A(2x-A+h)\over D_A(x,h)}
 -{B_2(2(x-V)-B_2+h)\over D_B(x,h)}.
\end{aligned}                                                    \tag{R89.1}
\]

All displayed denominators are (p)-adic units on the mask.  The exact
period exponent is

\[
 s_0=\min\Bigl\{1\leq s\leq r:
 p^{,r-s}\mid E_{p^s}(x)\text{ for every }x\in\Omega_q\Bigr\}.     \tag{R89.2}
\]

For \(\kappa=\nu\), define (s_0=1).  Then the exact period is
(p^{s_0}) and (j_q=\nu-s_0).  Formula (R89.2), rather than a numerator
condition, is the complete packet-level classification at every prime and
at every prime-power depth.

The mask is empty exactly when (S_p=\mathbf F_p).  Hence it is always
nonempty for (p\geq5); for (p=3) it is nonempty exactly when
(S_3\ne\mathbf F_3); and for (p=2) it is nonempty exactly when

\[
 A\equiv V\equiv V+B_2\equiv0\pmod2,
\]

equivalently (A,B_2,V) are all even.

For odd (p), let

\[
 \Phi'_p(x)=-x^{-2}+(x-A)^{-2}+(x-V)^{-2}
 -(x-V-B_2)^{-2}                                     \tag{R89.3}
\]

on \(\mathbf F_p\setminus S_p\).  If \(\Phi'_p\) is nonzero at even one
allowed residue, then (s_0=r).  The complete small-prime classification
of the contrary case is:

- For (p=3), \(\Phi'_3\) vanishes on every nonempty mask.
- For (p=5), put
  \[
  H_5(X)=2(B_2-A)X+A^2-2VB_2-B_2^2.                  \tag{R89.4}
  \]
  If \(|S_5|\leq3\), flatness holds exactly when
  \[
  A\equiv B_2\equiv0\pmod5
  \quad\hbox{or}\quad
  V\equiv0, B_2\equiv A\pmod5.                     \tag{R89.5}
  \]
  If \(|S_5|=4\), let (a) be the unique allowed residue.  Flatness
  holds exactly when (H_5(a)=0).  Equivalently, among the four nonzero
  distances from (a) to the poles, each of the signed pairs
  \(\{A,V\}\) and \(\{0,V+B_2\}\) contains one quadratic residue and
  one quadratic nonresidue.
- For (p=7), flatness holds exactly in (R89.5), with congruences modulo
  (7).
- For (p\geq11), the same conclusion as for (p=7) holds.

Thus a nontrivial (p=7) or (p\geq11) reduction has no reciprocal
descent beyond the exact nonunit conductor drop (j_q=\kappa).  The
reductions (R89.5) may have deeper lift structure, but that structure is
already classified exactly, without guessing, by (R89.2).

Two sharp bad-prime families are useful controls.  For (p=3), take a
unit (A) and

\[
 V\equiv A,\qquad B_2\equiv-A\pmod{3^\nu}.            \tag{R89.6}
\]

For effective conductor (3^r), this family has

\[
 s_0=\max(1,r-1).                                     \tag{R89.7}
\]

For (p=5), take

\[
 (A,B_2,V)\equiv(1,2,2)\pmod{5^\nu}.                 \tag{R89.8}
\]

It also has (s_0=\max(1,r-1)).  These are complete masked fibres, not
coefficientwise estimates.

## 3. Proof or derivation

The mask depends only on (x\bmod p).  Its forbidden set is exactly
(S_p), proving the emptiness assertions.  When nonempty it is a proper
nonempty subset of the additive group \(\mathbf F_p\).  Such a subset has
trivial translation stabilizer because (p) is prime.  Its lift to
\(\mathbf Z/p^\nu\mathbf Z) therefore has period subgroup precisely
(p\mathbf Z/p^\nu\mathbf Z), and exact period (p).

Direct subtraction, with no cancellation of mask factors, gives the exact
identity

\[
 \Phi(x+h)-\Phi(x)=hE_h(x).                            \tag{R89.9}
\]

If (K_q=p^\kappa k), (k) a unit, its phase is a phase modulo (p^r).
Translation by (p^s) preserves the mask, and it preserves the phase
exactly when (p^r\mid\Phi(x+p^s)-\Phi(x)) on every allowed (x).
This is (R89.2).  Taking (s=r) proves the automatic conductor period.
If (s<r), reduction of (E_{p^s}) modulo (p) is precisely
\(\Phi'_p); hence one nonflat allowed residue rules out every (s<r).

For (p=3,5,7), Fermat's identity (z^{-2}=z^{p-3}) for
(z\ne0\) gives a short algebraic classification.  At (p=3) every
inverse square is (1), so (R89.3) is (-1+1+1-1=0).  At (p=5),
expansion gives exactly the linear polynomial (H_5) in (R89.4).  If
there are at least two allowed residues, its vanishing forces (H_5=0),
which says (B_2=A) and (AV=0), namely (R89.5).  With a singleton mask,
evaluation at its only residue is necessary and sufficient; the quadratic
residue reformulation follows because the four distances are all of
\(\mathbf F_5^\times\), whose inverse squares are (1,1,-1,-1).

At (p=7), (R89.3) agrees on the allowed set with

\[
\begin{aligned}
 H_7(X)={}&4(B_2-A)X^3+6(A^2-2VB_2-B_2^2)X^2\\
 &+4(-A^3+3V^2B_2+3VB_2^2+B_2^3)X
 +A^4+V^4-(V+B_2)^4.                                 \tag{R89.10}
\end{aligned}
\]

If \(|S_7|\leq3\), there are at least four allowed roots, so the cubic
is zero.  Its first two coefficients give (B_2=A) and (AV=0), hence
(R89.5).  If \(|S_7|=4\), then (A\ne0); scale to (A=1).  Were the
cubic flat, it would equal \(\lambda P_\Omega\), where
(\lambda=4(B_2-1)) and (P_\Omega) is the monic cubic whose roots are
the three allowed residues.  Comparison of the (X^2)-coefficients leaves
only the following eight pairs.  The last two columns compare the
(X)-coefficients and rule out every pair:

\[
\begin{array}{c|c|c|c}
B_2&V&[X]H_7&[X](\lambda P_\Omega)\\ \hline
2&3&3&1\\3&6&4&5\\4&2&2&4\\5&5&3&4\\
6&3&4&3\\6&4&2&4\\6&5&4&6\\6&6&3&2
\end{array}
\]

All entries are in \(\mathbf F_7\), so this is an exact finite-field
elimination, not a numerical inference.  For (p\geq11), after putting
(R89.3) over its common squared denominator, the numerator has degree at
most (5), while there are at least (p-4\geq7) allowed residues.
Flatness makes that numerator identically zero.  Since the rational
function has degree below (p), its derivative can vanish identically
only when \(\Phi\) is constant; its value at infinity is zero.  The
quadratic numerator

\[
 (B_2-A)X^2+2AVX-AV(V+B_2)
\]

then vanishes identically, again giving (R89.5).

For the full (2)-adic statement, nonemptiness gives (A=2a),
(B_2=2b), and (V) even, while every allowed (x) is odd.  If (s=1),
each numerator in (R89.1) is divisible by (4).  If (s\geq2), the first
one is

\[
 4a\bigl(x-a+2^{s-1}\bigr),
\]

which is divisible by (8): if (a) is even the first factor supplies
it, and if (a) is odd the parenthesis is even.  The second numerator is
identical in form because (x-V) is odd.  The denominators are odd.
Consequently

\[
 v_2(\Phi(x+2)-\Phi(x))\geq3,
 \qquad
 v_2(\Phi(x+2^s)-\Phi(x))\geq s+3\quad(s\geq2),       \tag{R89.11}
\]

which proves the asserted period bound.  It is uniformly sharp.  With
((A,B_2,V)=(2,4,0)), one has

\[
 \Phi(x)={2\over(x-2)(x-4)}.
\]

At (x=1,h=2) the difference is (-8/3); at (x=3,h=4) it is
(32/15); and at (x=1,h=2^s), (s\geq3), it is

\[
 {2h(4-h)\over3(h-1)(h-3)},
\]

of respective valuations (3,5,s+3).  Hence none of the uniform powers
can be improved.

For (R89.6), the mask is (x\equiv-A\pmod3).  Write (x=-A+3t).  Then

\[
 \Phi(x)={-2A\over x(x-A)}
 =-A^{-1}\left(1+{9\over2A^2}t(t-A)\right)^{-1}.       \tag{R89.12}
\]

It is constant modulo (9).  For (r\geq3), translation of (x) by
(3^{r-1}) translates (t) by (3^{r-2}), changing the parenthesis by
a multiple of (3^r).  Translation by (3^{r-2}) changes (t) by
(3^{r-3}), and a choice of (t\bmod3) makes the resulting linear factor
a unit, so the change has exact valuation (r-1).  This proves (R89.7).

For (R89.8), the mask is (x\equiv3\pmod5), and (H_5(3)=0), giving the
claimed period.  Sharpness at the preceding power follows at (h=5),
(x=8), where

\[
 \Phi(x+h)-\Phi(x)=-{3725\over72072},
 \qquad v_5=2,
\]

and, for (h=5^s), (s\geq2), at (x=3), where (R89.1) is

\[
 E_h(3)={h+5\over6(h+3)(h+2)}-{2h\over1-h^2},
 \qquad v_5(E_h(3))=1.
\]

Finally, for the (q=8) candidate in Section 1, all allowed residues are
odd and every odd residue is its own inverse modulo (8).  Therefore

\[
 \Phi(x)\equiv x-(x-2)-(x-4)+(x-6)\equiv0\pmod8.
\]

The nonzero mask itself has exact period (2), proving the asserted
(j_q=2) without deleting any term of the completed symbol.

## 4. First doubtful or unproved step

The first unproved step is not local period algebra.  It is the missing
conductor-to-directed-degree inequality.  For a complete local/global
fibre \(\mathcal F\) after the two accepted deletions, one would need

\[
 \max\left(
 \sup_P\#\{P':(P,P')\in\mathcal F\},
 \sup_{P'}\#\{P:(P,P')\in\mathcal F\}
 \right)\leq\rho_*^2.                                 \tag{R89.13}
\]

Indeed, substituting (Q=J^{2/5}) and (T=J^{3/5}) into (89.13) shows
that comparison with (89.1) requires

\[
 \Delta\ll J^{11/15}B^{-4},
\]

which is the nontrivial branch of \(\rho_*^2\).  The packet supplies no
definition of the directed vertex universe, no formula connecting
((s_q,j_q)) to either degree, and no usable definition of the coarse
groups entering (R_*).  The automatic nonunit conductor period is
independent of (A,B_2,V), so no such degree estimate can be inferred from
it: locally it allows every second vertex allowed before the conductor
drop.  The small-prime flatness conditions likewise leave unrestricted
prime-power lifts unless (R89.2) is supplemented by a counting theorem.

There is a second, later obstruction to calling the (q=8) candidate an
accepted nonzero actual-symbol survivor: \(\mathfrak T_q\) is not defined
as an expression in (w_q).  Only its support/descent property (89.7) is
given.  Thus exact periodicity proves the possible frequency support and
the factor (p^{2j_q}), but not nonvanishing at a selected nonzero
frequency.  These omissions make a target-safe promotion impossible from
the permitted packet.

## 5. Required control tests and outcomes

- **Complete mask / no numerator shortcut:** passed.  The proof first
  classifies (S_p), requires every denominator in (R89.1) to be a unit,
  and tests the finite difference on every allowed residue.  Empty masks
  are set aside before any phase algebra.
- **Full (2)-part:** passed.  The proof works at (2^\nu), proves the
  depth-sensitive valuations (R89.11), and exhibits the perfect-power
  (q=8) control.  It never substitutes a parity or squarefree modulus.
- **Reciprocal versus affine period:** passed.  Every claim concerns
  (w_q) alone.  No claim about a period of (e_q(u_qx)w_q(x)) is made,
  and no condition involving (u+K\Phi') is used.
- **Completed descent factor:** passed.  The report uses the supplied
  (p^{2j_q}) in (89.7); for the (q=8) control it is (16), not (4).
- **Fejer mass:** passed.  Frequency sparsity is not converted into any
  improvement of \(\|\mathcal K_D^\circ\|_1\); the only graph estimate
  invoked is (89.13).
- **No coefficientwise square-root cancellation:** passed as a
  non-use control.  No coefficientwise estimate is asserted.  The stated
  (3^\nu) value (q^2/3) cannot be independently reproduced because the
  packet omits the defining formula for \(\mathfrak T_q\); it is therefore
  retained as a warning, not used as a proved input.  Family (R89.6)
  independently confirms the underlying exact extra (3)-adic period.
- **Accepted ownership:** passed conservatively.  Round-87 same-group,
  the (R_*\leq\rho_*) shells, fibres satisfying (89.11), and global
  (u=0) are not reinserted.  Since (R_*) and the coarse groups are not
  defined in the packet, the explicit local candidates are not promoted
  as survivors of those deletions.
- **Physical normalization and actual symbol:** passed.  No additional
  (M^{-2}) is inserted.  The four factors of (89.9), the (M^{-5})
  completion, (dV+nA-mB_2), both signs, nonzero modulus multiples,
  Ramanujan terms, support restrictions, and transform self-return are
  left intact; no termwise deletion is used.
- **Scale factors:** no new analytic bound is claimed.  The
  (Q^{-5/6}) in (89.13) is used verbatim.  The separate instruction to
  preserve (Q^{-5/12}) has no accompanying formula in the packet, so an
  independent reconciliation of those two displayed powers is not
  possible; neither is altered or traded for a gain.
- **Sharp local controls:** passed algebraically.  The exact rational
  values following (R89.11), (R89.12), and (R89.8) show that the
  (2)-, (3)-, and (5)-adic extra descents cannot be increased
  uniformly.  These are finite exact calculations only and certify no
  asymptotic theorem.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were used:

- `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/briefs/blind_bad_prime_fibre_rederivation.md`;
- `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/derivation_packet.md`, including starting graph hash
  `b279e9e671b54b43855bdfc90727e36e808eb539578dac0faeb115394789f674`.

No graph file, strategy, prior or sibling report, source card, web source,
or legacy artifact was inspected.  The finite-field and valuation checks
recorded above are derived explicitly in this report and create no external
dependency.

## 7. Recommended state effect

**Retain, with a split effect.**  Retain (R89.1)--(R89.12) as a candidate
local classification lemma and retain the (q=8), (3)-adic, and
(5)-adic families as exact obstruction/control fibres.  Do not promote a
target-safe package and do not change the accepted graph on the basis of
this report.  The next proof obligation should supply (i) the exact
survivor/coarse-group definition needed to test (R_*>\rho_*), (ii) a
two-sided degree theorem of the form (R89.13) for complete fibres, and
(iii) the defining formula for \(\mathfrak T_q\) needed to prove
nonvanishing and audit the stated (q^2/3) trace.  Until all three seams
are present, the target (89.1) remains unproved for this package.

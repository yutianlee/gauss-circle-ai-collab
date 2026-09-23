# Round 197 blind post-unmask common-cell post-repair verification

## 1. Result

**Final verdict for the requested seams: GREEN.**

The amended candidate closes every repair requested in the prior blind
review:

1. \(K_{\mathrm{sel}}\), the distinct selected primes, their canonical
   selection, and the exact selector \(\rho_N\) are now defined in
   (197.C1a)--(197.C1b).
2. The live-shell lower bound, strict cone, and lower closeness now give
   the uniform finite-\(g\) estimate (197.C24a), which supplies the
   missing \(O(1)\) multiplicity in both the normalized-BV sum and the
   selector audit.
3. Equations (197.C22)--(197.C22d) now give the exact common sharp
   factor, smooth factor, separate norms, and three-term product rule for
   the actual coefficient \(\lambda\).
4. The live/dead zero-extension cases remain exact and no sharp boundary
   term is smuggled into the common-cell estimate.
5. The proposed state effect is graph-safe: the new strict-sector node
   depends on the accepted Round-184/185/193/195 interfaces but does not
   rewrite any of them or feed a Round-197 conclusion backward into a
   prerequisite.
6. The final arithmetic/live/dead sharp code (197.C8a)--(197.C8c), the
   Farey projector typing (197.C9d)--(197.C9g), the exact cap/open
   operator split (197.C9h)--(197.C9k), and the physical-minus-safe
   core identity (197.C28a) are now explicitly defined and consistent.

The candidate is GREEN only for \(P_{\rm cc}\) and its exact open-packet
intersection.  This verdict does not extend to \(P_0\), all \(P_2\), the
four-corner sector, a parent obligation, a bridge, an endpoint theorem,
or an exponent.

The recomputed SHA-256 of the amended candidate, after the
\(W_{\rm tr}\) naming patch and without any edit by this reviewer, is

\[
\boxed{\texttt{285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0}.}
\]

## 2. Exact statement and hypotheses verified

The verified coefficient is

\[
 \lambda_{N,\sigma}(d)
 =\mu^2(N)\rho_N(d)
   a_{L,X}^{\mathrm{lit},\sigma}(N/d,d)
\]

on its complete literal domain and is zero elsewhere.  The verified
physical lower-swap sector is

\[
 P_{\rm cc}
 =P_2\mathbf1_{(m,\beta)=1}
       \mathbf1_{\chi_4(\alpha m)=-1}
       \mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
                    =\mathfrak c_{N,\sigma}(\alpha,gm)\}}.
\]

The sharp code now has a fully typed arithmetic gate

\[
 I_{\rm ar}(u,v)=
 \mathbf1_{u,v>0}\mathbf1_{uv=N}\mathbf1_{2\nmid v}
 \mathbf1_{\mu^2(N)=1}\mathbf1_{(u,v)=1}
\]

and a separately named conjunction \(I_{\rm lit}\) of the literal
support predicates.  If either gate fails, the code is the single dead
value \(\dagger\); otherwise it is the closed tuple of exact
discontinuous branch, cell, floor, star, tie, half-weight, hard-sample,
crossing, endpoint-trace, and sign labels in (197.C8b)--(197.C8c).
It expressly excludes the selector, normalized BV profile, coefficient
value, and smooth factors, which are handled by the exact product rule
rather than by code equality.  The code-equality condition is symmetric
because the lower swap merely exchanges its two arguments.

The arithmetic gate is also correct for the actual coefficient.  If
\(\mu^2(N)=1\) and \(uv=N\), then \((u,v)=1\) automatically; the oddness
of the swapped divisor follows from
\(\chi_4(\alpha m)=-1\).  If an arithmetic or literal predicate fails at
both inputs, both actual endpoint coefficients are zero even when the
reasons for death differ, so collapsing all named deaths to
\(\dagger\) is safe.

The selector is now fully specified.  For squarefree \(N\), it selects
the first canonical pair of distinct odd prime divisors
\(p_N<q_N\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\le K_{\mathrm{sel}}L^{-1/2},
\]

and

\[
 \rho_N(v)
 =1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
   +2\mathbf1_{p_Nq_N\mid v}
\]

when a pair exists, with \(\rho_N\equiv1\) otherwise.  This is an exact
\((1,0,0,1)\) truth table and depends on the product \(N\), not on its
allocation.

The common-cell factor hypotheses are also explicit:

\[
 a(u,v)=K_{\rm sharp}\eta_L(u)b^{\rm sm}(u,v)
\]

at both live inputs, with the same \(K_{\rm sharp}\), and

\[
 |K_{\rm sharp}|+\|\eta_L\|_\infty
 +\operatorname {Var}(\eta_L)+\|b^{\rm sm}\|_\infty
 +L\|\nabla b^{\rm sm}\|_\infty
 \ll_\varepsilon X^\varepsilon.
\]

These are precisely the hypotheses missing from the pre-repair version.

## 3. Proof or derivation

### 3.1 Exact actual-coefficient product rule

Use the amended notation

\[
\begin{aligned}
 \rho_0&=\rho_N(g\alpha),&
 \rho_1&=\rho_N(gm),\\
 \eta_0&=\eta_L(m),&
 \eta_1&=\eta_L(\alpha),\\
 b_0&=b^{\rm sm}(m,g\alpha),&
 b_1&=b^{\rm sm}(\alpha,gm).
\end{aligned}
\]

On a common live code,

\[
\begin{aligned}
 \lambda(g\alpha)-\lambda(gm)
 =\mu^2(N)K_{\rm sharp}\{&
 \rho_0\eta_0(b_0-b_1)
 +\rho_0b_1(\eta_0-\eta_1)\\
 &+(\rho_0-\rho_1)\eta_1b_1\}.
\end{aligned}
\]

Expanding the braces cancels the two inserted intermediate terms and
leaves

\[
 \rho_0\eta_0b_0-\rho_1\eta_1b_1,
\]

so (197.C22d) is exact.  The three summands are, respectively, the
smooth displacement, normalized-BV translation, and selector
commutator.  There is no omitted moving factor: (197.C22) defines the
full smooth product, (197.C22a) places every common discontinuous
multiplier in \(K_{\rm sharp}\), and (197.C22b) supplies all norms used
after the product rule.  Fresh epsilon rebudgeting covers the fixed
number of factor bounds.

The two input displacements satisfy

\[
 |m-\alpha|\le D_L/g\le D_L,\qquad
 |g\alpha-gm|\le D_L.
\]

Thus the gradient bound in (197.C22b) proves

\[
 |b_0-b_1|
 \ll_\varepsilon {D_L\over L}X^\varepsilon.
\]

Applied to the raw \(D_LL^2X^\varepsilon\) envelope, this gives

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon
 \ll L^2X^\varepsilon.
\]

### 3.2 Uniform finite-\(g\) lemma

On every live lower atom, the amended candidate states \(m\ge cL\).
Lower closeness gives \(gm\le d+D_L\), and the strict cone gives
\(d/m<16\).  Consequently

\[
 g\le {d\over m}+{D_L\over m}
 <16+c^{-1}{D_L\over L}.
\]

Since \(D_L=\lceil\sqrt L\rceil\le2\sqrt L\) for \(L\ge2\), the right
side is bounded by a constant

\[
 G_0=16+{2\over c\sqrt2}
\]

or any larger fixed accepted constant.  This proves (197.C24a) and,
because \(g\) is a positive integer, gives \(O(1)\) possible values of
\(g\) above each ordered lower pair \((m,\alpha)\).

This repair directly closes the first doubtful step in the prior review.
It also correctly uses the live-shell hypothesis that the earlier
counterfamily deliberately omitted.

### 3.3 Normalized-BV physical sum

For any finite-variation sequence,

\[
 \sum_{0<|a-b|\le D_L}|\eta_L(a)-\eta_L(b)|
 \ll D_L^2\operatorname {Var}(\eta_L).
\]

A fixed discrete increment is crossed by \(O(D_L^2)\) ordered close
pairs, so this estimate is exact at the required order.  Equation
(197.C24a) contributes only \(O(1)\) repetitions over \(g\).
Multiplying by the \(O(LX^\varepsilon)\) upper-completion count and the
bounded remaining factors gives

\[
 O_\varepsilon(D_L^2LX^\varepsilon)
 =O_\varepsilon(L^2X^\varepsilon).
\]

Thus the amended proof no longer drops a hidden \(g\)-multiplicity.

### 3.4 Selector exception

For a selected prime not dividing \(g\), squarefreeness of \(N\) places
it on exactly one of the two lower factor legs, so the allocation swap
complements its selector bit.  A selected prime dividing \(g\) stays on
the character/divisor leg at both endpoints.  The truth table
\((1,0,0,1)\) is invariant if both bits are complemented or neither is,
and changes only if exactly one selected prime divides \(g\).

The amended candidate defines

\[
 \delta_{G_0}
 =\min_{\substack{p\le G_0\ {\rm prime}\\q\ne p\ {\rm prime}}}
   |\log(q/p)|>0.
\]

The minimum is positive: there are finitely many eligible \(p\)'s, and
for each fixed \(p\) the discrete prime set has a nearest distinct
logarithmic ratio while ratios tend to infinity as \(q\to\infty\).
If exactly one selected prime divides \(g\), one selected prime is at
most \(G_0\), so distinctness gives

\[
 |\log(q_N/p_N)|\ge\delta_{G_0}.
\]

This contradicts (197.C1a) once
\(K_{\mathrm{sel}}L^{-1/2}<\delta_{G_0}\).  Hence the selector
commutator in (197.C22d) vanishes on all sufficiently large shells.  On
the remaining bounded set of shells, \(D_L=O_{K_{\mathrm{sel}},G_0}(1)\),
so the raw \(D_LL^2X^\varepsilon\) estimate is already target-safe.

The selector repair is therefore complete and uniform with the exact
constant dependence claimed in (197.C10)--(197.C12).

### 3.5 Zero extension and sharp boundary

The amended sharp code has one distinguished dead code determined by
the exact arithmetic gate \(I_{\rm ar}\), the closed literal gate
\(I_{\rm lit}\), and named zero extension.  A common dead/dead orbit
contributes zero; a common live/live orbit uses (197.C22d); and a
live/dead pair has unequal codes and lies in
\(P_{\partial\mathrm{lit}}\), not \(P_{\rm cc}\).  A selector zero is
not mislabeled as a dead literal symbol because \(\rho_N\) is excluded
from the sharp code and retained in the third term of (197.C22d).

This is consistent with the blind no-go.  The common-cell theorem
controls precisely the sector where the support/sharp commutator is
absent, and it leaves every sharp first failure in the exact open
complement.  The aligned-face identity (197.C37) continues to block an
automatic extension to all of \(P_0\).

### 3.6 Graph-safe scope

The amended candidate distinguishes:

1. the selector constant \(K_{\mathrm{sel}}\) from the physical inward
   cross gcd \(\kappa\);
2. the transformed profile \(W_{\rm tr}\) from the physical atom \(W\);
3. the physical mask, evaluated before Fourier/height operations, from
   the fixed-packet conditions; and
4. the cap and open packet families before the exact outer restoration;
5. the physical post-exit aggregate
   \(\mathscr H_{\mathrm{out}}^\sigma\), the recomputed accepted-safe
   aggregate \(\mathscr S_{\le192,\mathrm{out}}^\sigma\), and their
   residual core.

The final packet definition includes the physical height block, centered
inverse data, \(T\), \(A\), the Farey set, the complete \(T=0\) branch,
and all simultaneous strict \(T\ge1\) inequalities in
(197.C9d)--(197.C9g).  Thus no Farey condition is an untyped external
mask.  Equations (197.C9h)--(197.C9k) define the outer restoration and
the disjoint cap/open split without inserting a packet condition into
the physical orbit.  The new exact identity

\[
 \mathscr R_{\mathrm{core,out}}^\sigma(MW)
 =\mathscr H_{\mathrm{out}}^\sigma(MW)
  -\mathscr S_{\le192,\mathrm{out}}^\sigma(MW)
\]

types the subtraction used to prove (197.C10).  Equation (197.C30)
retains the transported-mask commutator exactly, and
(197.C33)--(197.C34) obtain the open intersection by subtracting the
deletion-stable cap from the already masked complete core.

Most importantly, the proposed state effect leaves every accepted
Round-184/185/193/195 prerequisite unchanged.  The refined remainder
(197.C35) is recorded only in the new subordinate node and in the open
owner's next action.  This avoids a reverse dependency and any
Round-197/Round-195 cycle.  All parents, bridges, endpoint claims, and
exponents remain unchanged.

## 4. First doubtful or unproved step

No doubtful step remains in the requested coefficient/algebra,
finite-\(g\), normalized-BV, selector, zero-extension, or graph-scope
seams.

The first fact not independently rederived in this post-repair review is
the content of the four earlier accepted interfaces cited in Section 6
of the candidate, especially their fixed-to-outer masked-operator
estimates.  The amended candidate now identifies the exact kernel files
and equation ranges supplying those facts.  Revalidating those accepted
theorems is outside this blind consistency seam and remains the job of
the separate provenance, operator, and graph-replay reviews.  This is a
declared dependency boundary, not a defect in the repaired local
argument.

## 5. Required control test and outcome

1. **Three-term expansion — PASS.**  Expanding (197.C22d) yields exactly
   \(\rho_0\eta_0b_0-\rho_1\eta_1b_1\).
2. **Largest permitted \(g\) — PASS.**  The live-shell lower bound and
   \(d/m<16\) make (197.C24a) uniform for every \(L\ge2\).
3. **Repeated-\(g\) BV translations — PASS.**  Each ordered
   \((m,\alpha)\) has at most \(G_0\) integer \(g\)-values, so the
   \(D_L^2\) variation sum acquires only a constant multiplicity.
4. **Selector truth table — PASS.**  Formula (197.C1b) gives one on the
   \((0,0)\) and \((1,1)\) allocations and zero on the two split
   allocations.
5. **Exactly-one-prime-in-\(g\) — PASS.**  It is the only selector
   commutator, and (197.C24b) excludes it for large \(L\); bounded shells
   are paid absolutely.
6. **No selected pair — PASS.**  Then \(\rho_N\equiv1\) and the selector
   term in (197.C22d) is identically zero.
7. **Dead/dead, live/live, live/dead — PASS.**  These cases are,
   respectively, zero, governed by the product rule, and placed in the
   exact complement.
8. **Character erased — PASS as a falsification.**  Erasing
   \(\chi_4\) changes the lower difference to a sum, so the candidate
   does not prove an unsigned or arbitrary-array analogue.
9. **Graph-cycle control — PASS.**  The state proposal does not amend a
   prerequisite node with a conclusion that depends on it.
10. **Naming control — PASS.**  \(K_{\mathrm{sel}}\), \(\kappa\),
    \(W_{\rm tr}\), and the physical atom \(W\) are now distinct.
11. **Arithmetic/dead-code control — PASS.**  Live arithmetic implies
    the actual divisor/complement conditions; common \(\dagger\) means
    both coefficients are zero, while live/dead is excluded.
12. **Farey/operator typing control — PASS.**  The \(T=0\) branch,
    simultaneous \(T\ge1\) inequalities, outer restoration, cap/open
    split, \(\mathscr H_{\rm out}\), and
    \(\mathscr S_{\le192,\rm out}\) are explicitly defined before they
    are used.

## 6. Dependencies and exact artifacts used

The post-repair verification used:

1. protocol.md, as the governing review and state-ownership protocol;
2. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md;
3. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/blind_post_unmask_common_cell_consistency_review.md; and
4. the earlier blind arithmetic and support conclusions already
   contained in this reviewer's active Round-197 context.

The discovery report and hostile report were not imported.  The four
accepted kernel dependencies listed by the candidate were not reopened
or re-proved in this seam.  Candidate integrity was checked by a fresh
SHA-256 computation; the candidate itself was not edited.

The earlier review file was rewritten through apply_patch solely to
remove stray control characters and restore its lost TeX delimiters.
The repaired file has zero unexpected control characters, zero bare
carriage returns, and matched inline-math delimiters.

## 7. Recommended state effect

**GREEN for the repaired subordinate candidate.**  This review removes
the prior blind REPAIR gate for the local coefficient, BV, selector,
zero-extension, and scope seams.  Subject to the remaining independent
operator/provenance/formalization reviews and a mechanically valid State
Patch, the conductor may create the proposed subordinate
\(P_{\rm cc}\) proved-internal node and record its exact open-packet
intersection.

Do not promote the complement, do not alter an accepted prerequisite,
and do not change any parent status, bridge, endpoint theorem, global
theorem, or exponent.

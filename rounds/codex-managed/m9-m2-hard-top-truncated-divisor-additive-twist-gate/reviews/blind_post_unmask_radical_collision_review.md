## 1. Result and verdict

**Verdict: REPAIR (local statement repair; the mathematical core is green).**

The incidence, parity, cone, support-constant, (D\le CL), exact base-collision, exact-versus-near, and scope ledgers are correct.  In particular, the discovery report strengthens the blind report correctly: the base collision graph has at most one unequal unordered edge globally, not merely collision classes of size at most two.  The long-channel result is an owner-complete channel sector, not an owner-complete polynomial range of (L).

One exactness repair is required before the atom-collision statement is reused.  The sentence following discovery equation (3.4), and the corresponding claim after candidate equation (161.J9), must separate the trivial same-atom loop (D_1=D_2, t_1=t_2), which exists for every channel, from a nontrivial within-channel repetition (D_1=D_2, t_1\ne t_2), which exists only on the unique possible rational channel.  Candidate equation (161.J9) should also state (D_1\ne D_2) and (k\ne0) when it is called a cross-channel relation.  The rational-channel/noncoexisting-cross-relation claim is true at atom level, but its shared-endpoint calculation should be displayed explicitly rather than inherited implicitly from the base case.

No audited artifact asserts a physical lower bound for (B_D(1)), and none proves a full strict polynomial (L)-range.  Discovery equations (3.9)--(3.11), candidate equations (161.J12)--(161.J13), and the blind formal-array control are all correctly marked as nonphysical interface tests.

## 2. Exact repaired statement and hypotheses

Assume the frozen scalar (161.BL1)--(161.BL8), and let fixed (0<c_-<c_+<\infty) satisfy

\[
 B_D(t)\ne0\quad\Longrightarrow\quad
 c_-L^2\le Dt^2\le c_+L^2.                                  \tag{R.1}
\]

This is the literal support implication in discovery (2.4) and candidate (161.J2); it assumes no full population or positivity of the support.

The seam-correct statement is as follows.

1. The incidence map is the bijection
   \[
   h=gd_1u^2,\quad m=gd_2v^2,\quad
   D=d_1d_2,\quad t=guv,                                    \tag{R.2}
   \]
   where (d_1,d_2) are squarefree, ((d_1u,d_2v)=1), (g,d_1,u) are odd, and
   \[
   d_2v^2\le d_1u^2\le4d_2v^2.                              \tag{R.3}
   \]
   Its literal coefficient is discovery (1.1), equivalently candidate (161.J5) or blind equations (3.1)--(3.4).
2. For every fixed (C>0), the complete sector (D\le CL) is target-safe.  For every fixed (\tau>0), the complete sector (t\ge\tau\sqrt L) is target-safe.  The two filtrations contain one another with constants (C=c_+\tau^{-2}) and (\tau=\sqrt{c_-/C}).  This is a sector theorem only.
3. Put (\alpha_D=J\sqrt D).  There is at most one rational channel (D) with (\alpha_D\in\mathbb Q).  If (\alpha_D=p/q) in lowest terms, phase-one atoms are exactly (q\mid t), and distinct within-channel phase repetitions are exactly (q\mid(t_1-t_2)).
4. The base graph with nonloop edges
   \[
   \alpha_{D_1}-\alpha_{D_2}\in\mathbb Z,\qquad D_1\ne D_2,  \tag{R.4}
   \]
   has at most one unordered edge.  A rational channel cannot coexist with that edge.
5. For atom collisions
   \[
   t_1\alpha_{D_1}-t_2\alpha_{D_2}\in\mathbb Z,             \tag{R.5}
   \]
   the cases are: a trivial loop if (D_1=D_2,t_1=t_2); a rational-channel repetition if (D_1=D_2,t_1\ne t_2); or a cross-channel relation with (D_1\ne D_2) and a necessarily nonzero integer.  All cross-channel relations use at most one unordered radical pair, and, after a common orientation, their integer triples are rational multiples of one primitive triple.  No rational channel coexists with a cross-channel atom relation.
6. Items 3--5 are exact classifications only.  They imply no positive lower bound for a nonzero modulo-one gap and no near-collision collar bound on the moving (t)-ranges.

## 3. Proof and line audit

**Incidence, parity, and cone.**  Starting with (g=(h,m)), write (h=ga,m=gb), so ((a,b)=1).  Unique squarefree-kernel decompositions (a=d_1u^2,b=d_2v^2) give

\[
 (d_1u,d_2v)=1,\qquad
 hm=g^2d_1d_2u^2v^2=(d_1d_2)(guv)^2.
\]

Thus (R.2) follows and is invertible: a permitted tuple returns ((h,m)), whose gcd is (g), and then recovers (a,b,d_1,d_2,u,v).  There is no condition coupling (g) to the other four variables.  Since (h=gd_1u^2), odd (h) is equivalent to odd (g,d_1,u), and

\[
 \chi_4(h)=\chi_4(gd_1).
\]

The integer identity (m\ge\lceil h/4\rceil\iff h\le4m), together with (m\le h), gives (R.3) with both endpoints inclusive.  Also

\[
 \sqrt{\frac{q_Xh^2}{4Dt^2}}
 =\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}},
 \qquad
 L^{3/2}(Dt^2)^{-3/4}=\left(\frac{L^2}{Dt^2}\right)^{3/4}.
\]

These checks validate discovery (1.1), candidate (161.J4)--(161.J5), and blind (3.1)--(3.4).  If (D) is even, its factor (2) is in (d_2); if (t) is even, its 2-part is in (v).  No parity branch is lost.  Candidate (161.J5) has only a typesetting defect (`mathbf1` should be `\mathbf 1`); it is not a normalization error.

**The (D\le CL)/long-(t) sector.**  From (161.BL8), for (Z\ge2),

\[
 \left|\sum_{D\le Z}\sum_tB_D(t)e(t\alpha_D)\right|
 \le L^\varepsilon\sum_{D\le Z}(1+L/\sqrt D)
 \ll (Z+L\sqrt Z)L^\varepsilon.                             \tag{R.6}
\]

This is discovery (3.1), candidate (161.J6), and control (161.K1).  Setting (Z=CL) proves candidate (161.J7), with constant depending on (C); the usual relabelling absorbs (L^\varepsilon) into (X^\varepsilon) because (L\ll H\ll X^{1/4}).  From (R.1),

\[
 t\ge\tau\sqrt L\Longrightarrow D\le c_+\tau^{-2}L,
 \qquad
 D\le CL\Longrightarrow t\ge\sqrt{c_-/C}\sqrt L.           \tag{R.7}
\]

Thus discovery (1.2), (2.4), and the deductions following (3.1) are green.  Control (161.K2) is the case (C=1).  Substituting (Z=L^{1+\delta}) into (R.6) gives an upper-bound capacity (L^{3/2+\delta/2+\varepsilon}); as discovery explicitly says after (3.1), this is not a lower bound and does not prove failure beyond (D\asymp L).

**Rational and base collisions, including shared indices.**  Square roots of distinct squarefree integers are linearly independent over (\mathbb Q).  For two base edges, discovery (3.2) eliminates (J) and gives (3.3).  Four distinct endpoints give a forbidden four-radical relation.  Exactly one shared endpoint gives a forbidden three-radical relation; even if the shared coefficient cancels, the two remaining nonzero radical coefficients still contradict independence.  Two shared endpoints mean the same unordered pair, with repetition or reversal.  Hence discovery (3.2)--(3.3), candidate (161.J8), and control (161.K3) correctly prove one global nonloop edge.  Blind equation (3.6) and the subsequent size-at-most-two conclusion are true but weaker; they should not replace the strengthened global-edge result.

If (J\sqrt{D_0}=r\in\mathbb Q\setminus\{0\}), two rational channels would give a rational ratio of distinct squarefree radicals.  Combining this equation with a base edge gives

\[
 r\sqrt{D_1}-r\sqrt{D_2}-k\sqrt{D_0}=0,                     \tag{R.8}
\]

after eliminating (J).  If (D_0) is a shared endpoint, the other endpoint retains coefficient (\pm r\ne0); if it is disjoint, all three radicals occur.  Both cases are impossible.  This validates the shared-index prose between discovery (3.3) and (3.4).

**Atom collisions, with every loop and overlap separated.**  For a cross-channel relation

\[
 J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,\qquad D_1\ne D_2,         \tag{R.9}
\]

one has (k\ne0), because (k=0) would make (\sqrt{D_1/D_2}=t_2/t_1\in\mathbb Q).  Comparing two such relations and eliminating (J) gives the weighted version of discovery (3.3).  Disjoint radical pairs and exactly-one-index overlaps contradict four- and three-radical independence.  If both indices are shared, orient both relations as ((D_1,D_2)); independence gives

\[
 \ell t_1=ks_1,\qquad \ell t_2=ks_2,
\]

so ((s_1,s_2,\ell)=(\ell/k)(t_1,t_2,k)).  This validates discovery (3.4) and the intended content of candidate (161.J9).

For the rational-versus-cross-atom shared-index seam, eliminating (J) from (J\sqrt{D_0}=r\) and (R.9) gives

\[
 rt_1\sqrt{D_1}-rt_2\sqrt{D_2}-k\sqrt{D_0}=0.              \tag{R.10}
\]

If (D_0=D_1), the coefficient of (\sqrt{D_2}) is (-rt_2\ne0); if (D_0=D_2), the coefficient of (\sqrt{D_1}) is (rt_1\ne0); and the disjoint case is immediate.  Thus coexistence is impossible.

If instead (D_1=D_2=D), then (R.5) is

\[
 (t_1-t_2)J\sqrt D\in\mathbb Z.                             \tag{R.11}
\]

For (t_1=t_2), this is a trivial loop for every (D).  For (t_1\ne t_2), it forces the unique possible rational channel; if (J\sqrt D=p/q) reduced, it holds exactly when (q\mid(t_1-t_2)).  Discovery's sentence following (3.4) is correct only with this nontriviality qualifier made explicit.  Candidate (161.J9) likewise needs its cross-channel and nonzero-integer hypotheses written into the displayed statement.

All nontrivial exact channels are target-safe: discovery (3.5), from (161.BL8), bounds the one rational channel or the two channels on the one cross edge by (O(L^{1+\varepsilon})).

**Exact is not near.**  The algebra above is qualitative.  Choosing (J=k/|\sqrt{D_1}-\sqrt{D_2}|) realizes a prescribed exact base edge, and perturbing (J) makes that gap arbitrarily small.  On an overlap of (T) actual (t)-indices, blind equation (3.8) shows that the relevant resolution is (1/T), not equality.  Blind equation (3.9) is a valid qualitative simultaneous-approximation control, but its denominator can be enormous and it was correctly not presented as a physical lower bound or a polynomial-range counterexample.  Discovery (3.5) and candidate (161.J8)--(161.J9) therefore cannot be used to bound near-collision collars.

**Physical-lower-bound and strict-range audit.**  Discovery (3.6) proves only that a close semiprime can have one literal incidence when the profiles are nonzero; the text explicitly disclaims a family lower mass.  Discovery (3.9)--(3.11), candidate (161.J12)--(161.J13), and the blind formal real array test are adversarial coefficient-interface controls, not instances of candidate (161.J10) or control (161.K4).  Control (161.K5) is an upper-bound capacity.  Control (161.K7) is explicitly conditional on a hypothetical flat rank-one model.  None is a physical lower bound.

Likewise, candidate (161.J7) and discovery (1.2) close only (D\le CL), equivalently a constant-wise long-(t) filtration through (R.7).  Candidate (161.J6) above that scale and control (161.K7) describe method capacities, not a full strict polynomial (L)-range.  The no-full-range disclaimers are correct.

## 4. First doubtful or unproved step

After the local atom-statement repair, no doubtful algebraic step remains in the audited incidence, long-sector, or exact-collision seams.  The first unresolved physical estimate remains candidate (161.J14), equivalently discovery (4.1):

\[
 \left|\sum_{D\asymp L^2\ {\rm sf}}B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.                     \tag{R.12}
\]

Here (B_D(1)) must be the literal close-factor coefficient in discovery (3.6), candidate (161.J10), or control (161.K4).  Discovery (3.12) and control (161.K5) give only the positive (L^{2+o(1)}) placement.  The diagnostic arrays do not disprove (R.12), and the exact one-edge theorem gives no near-collision or signed-(D) estimate.

The first textual step requiring repair is narrower: do not infer from discovery (3.4) that (R.11) characterizes all same-channel equalities unless (t_1\ne t_2) is stated, and do not invoke candidate (161.J9) as cross-channel without (D_1\ne D_2,k\ne0).

## 5. Control tests and outcomes

| Seam | Verdict | Exact references |
|---|---|---|
| Unique incidence and inverse multiplicity | **Green** | discovery (1.1); candidate (161.J4)--(161.J5); blind (3.1)--(3.4) |
| Parity, even (D), even (t), and inclusive cone | **Green** | discovery (1.1) and derivation before (3.1); candidate (161.J4)--(161.J5) |
| Fixed support constants | **Green** | discovery (2.4); candidate (161.J2) |
| (D\le CL) and fixed long-(t) sector | **Green** | discovery (1.2), (3.1); candidate (161.J6)--(161.J7); controls (161.K1)--(161.K2) |
| Unique rational channel and phase-one arithmetic | **Green** | discovery prose between (3.3) and (3.4); blind (3.5) |
| Global base-collision graph | **Green** | discovery (3.2)--(3.3); candidate (161.J8); control (161.K3) |
| Cross-channel atom collision pair/proportionality | **Green after statement repair** | discovery (3.4); candidate (161.J9); repaired (R.9)--(R.10) |
| Same-channel atom loops | **Repair** | sentence following discovery (3.4); repaired (R.11) |
| Exact versus near resonance | **Green/open near seam** | discovery paragraph after (3.5); blind (3.8)--(3.9) |
| No physical lower-bound overclaim | **Green** | discovery (3.6), (3.9)--(3.12); candidate (161.J10)--(161.J13); controls (161.K4)--(161.K5) |
| No full strict polynomial range overclaim | **Green** | discovery (1.2), (3.1); candidate (161.J6)--(161.J7); controls (161.K6)--(161.K7) |

## 6. Dependencies and exact artifacts used

This post-unmask review used only:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/blind_statement.md`;
3. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/briefs/blind_radical_frequency_rederivation.md`;
4. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/literal_radical_frequency_attack.md`;
5. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_control_and_obstruction.md`;
6. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/controls/conductor_round161_radical_capacity_controls.md`;
7. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/blind_radical_frequency_rederivation.md`.

The source-auditor report, state files, strategy files, conductor seed, sibling material outside the named discovery report, and every other round artifact were not read.  No computation, web source, or external theorem was used.

## 7. Recommended state effect

Repair the canonical exact-collision lemma by adding the trivial-loop/nontrivial-repetition split (R.11), the explicit cross-channel hypotheses in (R.9), and the rational-versus-cross-atom shared-index calculation (R.10).  Then the incidence lemma, (D\le CL)/long-(t) sector, and strengthened exact-collision theorem are green candidate advances.  Preserve the explicit statement that exact sparsity yields no near-collision estimate.

Retain the one-column common-test result only as a route-scoped obstruction.  Do not convert discovery (3.6), (3.9)--(3.11), candidate (161.J12)--(161.J13), or controls (161.K5)--(161.K7) into a physical lower bound or a full strict polynomial (L)-range.  The physical singleton estimate (R.12) and the remaining short channels stay open.

Final verdict: **REPAIR**, not reject; after the stated local repair, the audited mathematical claims are green.

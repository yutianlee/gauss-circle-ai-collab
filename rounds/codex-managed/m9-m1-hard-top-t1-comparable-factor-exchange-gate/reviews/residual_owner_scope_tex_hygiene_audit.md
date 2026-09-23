# Round 184 residual-owner review TeX-hygiene audit

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Task: residual-owner-scope TeX hygiene
- Role: independent line-by-line hygiene auditor
- Audited artifact:
  rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/residual_transport_correlation_owner_scope_review.md
- Pre-repair artifact SHA-256:
  cfe31920a32ac5cf5d0518fadbbe2dfffa88ad7868a8d1d50540002e5d02e828
- Final repaired artifact SHA-256:
  89fd798299d8bd59ca0edc0a4d76ad2faee732686849165f207613c5f9194dc8
- Audit action: read-only; the audited review was not edited

## 1. Result

**Final verdict: GREEN.**

The pre-repair review contained forty-five affected prose lines on which
intended inline mathematics was left in literal parentheses or attached
to prose without math delimiters. Several strings contained raw TeX
commands such as
<code>\lceil</code>, <code>\varepsilon</code>, <code>\sigma</code>,
<code>\kappa</code>, <code>\sum</code>, <code>\sqrt</code>,
<code>\asymp</code>, <code>\ll</code>, and <code>\pmod</code>.
The conductor applied the complete inline-math repair map. Exhaustive
reinspection of the current hash found **no remaining malformed TeX,
raw TeX command in prose, lost inline delimiter, or unbalanced display
delimiter**. Display mathematics remains properly delimited.

The two bounded mathematical-wording corrections are now exact:

1. historical line 237 abbreviated the scalar capacity as only \(L^2\);
   the current line restores \(L^2X^\varepsilon\); and
2. historical line 276 grouped M9-M1-physical-one-count-assembly and
   M9-M1 under “unchanged/open”; current lines 276--277 give their exact
   separate proved_internal and open statuses.

Current line 237 states \(L^2X^\varepsilon\), and current lines 276--277
separately state that M9-M1-physical-one-count-assembly is unchanged
proved_internal while M9-M1 is unchanged/open. No wording or scope repair
remains.

## 2. Exact classification rule

The audit distinguishes three classes.

1. **Ordinary equation references remain literal prose.** References
   such as (184.C17), (184.C21), (184.C22)--(184.C23), (184.C24), and
   (184.C25) are labels, not mathematical expressions to render.
2. **Code spans remain code.** Line 13's literal <code>\rm</code> is
   intentionally code-formatted while describing the repaired control
   byte. It is not stray TeX prose.
3. **Intended inline mathematics must use <code>\(...\)</code>.** A
   parenthetical containing variables, relations, powers, subscripts, or
   TeX commands is mathematical unless it is an equation label.
   Constructions such as <code>small-(t)</code> and
   <code>large-(G)</code> require <code>small-\(t\)</code> and
   <code>large-\(G\)</code>.

There are no other substantive English parentheticals in the audited
review that need alteration. All non-label parenthetical formulae listed
in Section 3 are intended inline mathematics.

## 3. Exhaustive line-by-line repair map

Line numbers refer to both hashes above; the conductor's repairs were
single-line substitutions and preserved line numbering. The “current
prose fragment” column records the pre-repair text for provenance; every
mapped inline-math replacement is present in the current file.

| line | current prose fragment | exact repair |
|---:|---|---|
| 26 | <code>(R=\lceil L\rceil)</code> | <code>\(R=\lceil L\rceil\)</code> |
| 27 | <code>(L^3X^\varepsilon)</code> | <code>\(L^3X^\varepsilon\)</code> |
| 28 | <code>(L^2X^\varepsilon)</code> | <code>\(L^2X^\varepsilon\)</code> |
| 34 | <code>complete (t=1) face</code> | <code>complete \(t=1\) face</code>; retain label (184.C16) |
| 35 | <code>small-(t) owner</code> | <code>small-\(t\) owner</code> |
| 39 | <code>shell (L), real (X\ge2)</code> | <code>shell \(L\), real \(X\ge2\)</code> |
| 40 | <code>(\sigma\in\{\pm1\})</code>; <code>squarefree (N)</code> | <code>\(\sigma\in\{\pm1\}\)</code>; <code>squarefree \(N\)</code> |
| 41 | <code>be ({p_N,q_N})</code> | <code>be \(\{p_N,q_N\}\)</code> |
| 42 | <code>only on ((N,L,\kappa))</code> | <code>only on \((N,L,\kappa)\)</code> |
| 59 | <code>where (\rho_N(v)=1)</code> | <code>where \(\rho_N(v)=1\)</code> |
| 66 | <code>Thus (\rho_N) has truth table (1,0,0,1)</code> | <code>Thus \(\rho_N\) has truth table \(1,0,0,1\)</code> |
| 67 | <code>(00,10,01,11)</code> | <code>\(00,10,01,11\)</code> |
| 82 | <code>one fixed (N)</code> | <code>one fixed \(N\)</code> |
| 88 | <code>For fixed (N)</code> | <code>For fixed \(N\)</code> |
| 89 | <code>(v_1&lt;\cdots&lt;v_s)</code>; <code>(\epsilon_j=\chi_4(v_j))</code> | <code>\(v_1&lt;\cdots&lt;v_s\)</code>; <code>\(\epsilon_j=\chi_4(v_j)\)</code> |
| 90 | <code>(C_j=\sum_{i\le j}\epsilon_i)</code>; <code>(C_0=0)</code> | <code>\(C_j=\sum_{i\le j}\epsilon_i\)</code>; <code>\(C_0=0\)</code> |
| 91 | <code>into (a_j). With (a_0=a_{s+1}=0)</code> | <code>into \(a_j\). With \(a_0=a_{s+1}=0\)</code> |
| 98 | <code>Because (\sum_{j=0}^s(a_{j+1}-a_j)=0)</code> | <code>Because \(\sum_{j=0}^s(a_{j+1}-a_j)=0\)</code> |
| 99 | <code>(C_j)</code> | <code>\(C_j\)</code> |
| 109 | <code>(\operatorname{osc}(C_N))</code>; <code>(O(L^2))</code> | <code>\(\operatorname{osc}(C_N)\)</code>; <code>\(O(L^2)\)</code> |
| 110 | <code>(L^2X^\varepsilon)</code> | <code>\(L^2X^\varepsilon\)</code> |
| 118 | <code>extend (z_N)</code> | <code>extend \(z_N\)</code> |
| 126 | <code>exactly (R) windows</code> | <code>exactly \(R\) windows</code> |
| 127 | <code>(r&lt;R)</code>; <code>(R-r)</code> | <code>\(r&lt;R\)</code>; <code>\(R-r\)</code> |
| 142 | <code>(\sqrt{N+r}-\sqrt N=r/(\sqrt{N+r}+\sqrt N))</code> | <code>\(\sqrt{N+r}-\sqrt N=r/(\sqrt{N+r}+\sqrt N)\)</code> |
| 146 | <code>If (W_s=\sum_{j&lt;R}z_{s+j})</code> | <code>If \(W_s=\sum_{j&lt;R}z_{s+j}\)</code> |
| 147 | <code>(\sum_sW_s=R\sum_Nz_N)</code>; <code>(M_L+R-1)</code> | <code>\(\sum_sW_s=R\sum_Nz_N\)</code>; <code>\(M_L+R-1\)</code> |
| 169 | <code>At (R=\lceil L\rceil)</code>; <code>(O(L))</code> | <code>At \(R=\lceil L\rceil\)</code>; <code>\(O(L)\)</code> |
| 170 | <code>(O(L^3X^\varepsilon))</code> | <code>\(O(L^3X^\varepsilon)\)</code> |
| 180 | <code>(D_{L,\sigma})</code>; <code>(R\asymp L)</code> | <code>\(D_{L,\sigma}\)</code>; <code>\(R\asymp L\)</code> |
| 181 | <code>(\mathfrak E_R\ll L^3X^\varepsilon)</code> | <code>\(\mathfrak E_R\ll L^3X^\varepsilon\)</code> |
| 182 | <code>(\lvert\mathcal T^{\rm rem}\rvert\ll L^2X^\varepsilon)</code> | <code>\(\lvert\mathcal T^{\rm rem}\rvert\ll L^2X^\varepsilon\)</code> |
| 184 | <code>(L^{1/2})</code> | <code>\(L^{1/2}\)</code> |
| 209 | <code>(v/u\in(4,16))</code>; <code>(p^{\pm2})</code>; <code>(p\ge3)</code> | <code>\(v/u\in(4,16)\)</code>; <code>\(p^{\pm2}\)</code>; <code>\(p\ge3\)</code> |
| 215 | <code>(\log4)</code> | <code>\(\log 4\)</code>; retain label (184.C3) |
| 216 | <code>(\kappa L^{-1/2}&lt;\log4)</code>; <code>(2\mid N)</code> | <code>\(\kappa L^{-1/2}&lt;\log 4\)</code>; <code>\(2\mid N\)</code> |
| 220 | <code>All odd primes (1\pmod4)</code> | <code>All odd primes \(1\pmod 4\)</code> |
| 221 | <code>(\chi_4(pq)=-1)</code>; <code>(+1)</code> | <code>\(\chi_4(pq)=-1\)</code>; <code>\(+1\)</code> |
| 237 | <code>the (L^2) scalar capacity</code> | <code>the \(L^2X^\varepsilon\) scalar capacity</code>; restore the omitted \(X^\varepsilon\) |
| 244 | <code>complete (t=1) statement</code> | <code>complete \(t=1\) statement</code>; retain label (184.C16) |
| 280 | <code>every (t\ge2) small-(G) incidence and the large-(G)</code> | <code>every \(t\ge2\) small-\(G\) incidence and the large-\(G\)</code> |
| 288 | <code>exponent (1/4)</code> | <code>exponent \(1/4\)</code> |
| 290 | <code>(1/3)</code> | <code>\(1/3\)</code> |
| 293 | <code>(0.3144831759740614\ldots)</code> | <code>\(0.3144831759740614\ldots\)</code> |
| 296 | <code>full (t=1) face</code> | <code>full \(t=1\) face</code> |

The following equation references are exempt and must remain prose
labels: line 13 (184.C14); lines 22--25 (184.C17), (184.C21),
(184.C22)--(184.C23), (184.C24), and (184.C25); line 34 (184.C16);
line 107 (184.C21); line 144 (184.C22)--(184.C23); line 171 (184.C25);
line 188 (184.C25); line 204 (184.C17)--(184.C24); line 215 (184.C3);
line 232 (184.C21); line 243 (184.C16); and line 269 (184.C25).

All material between <code>\[</code> and <code>\]</code> on lines
44--47, 52--57, 61--64, 76--79, 93--96, 101--105, 114--116, 120--124,
129--139, 150--153, 157--160, 164--167, 174--177, and 190--198 is
already valid display mathematics and must not be altered merely because
it contains parentheses or TeX commands.

## 4. First doubtful or unproved step

The first historical hygiene defect was line 26's raw
<code>(R=\lceil L\rceil)</code>. The historical escape-loss pattern
continued through line 296 as mapped above. All mapped delimiter repairs
are now present; there is no current TeX defect.

The two historical mathematical-wording drifts at lines 237 and 276 are
also repaired exactly. No current TeX, statement, owner-status, or scope
defect remains.

No other mathematical wording drift was found. In particular, the
residual mask, Abel identity, Fejer normalization and phase, Cauchy
prefactor, restored powers, one-real-part open condition, mechanism
controls, and exponent quarantine remain mathematically consistent with
the reviewed candidate.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| raw TeX in display math | **PASS.** All display blocks are balanced and properly delimited. |
| raw TeX in code spans | **PASS.** Line 13's <code>\rm</code> is intentional literal code. |
| equation-label discrimination | **PASS.** All ordinary (184.C...) references are enumerated and exempt. |
| intended inline-math coverage | **PASS.** All forty-five mapped lines now use math delimiters. |
| nested-parenthesis repair | **PASS.** Current line 42 has one balanced inline-math pair. |
| hyphenated symbol repair | **PASS.** Current lines 35 and 280 use the mapped forms. |
| exact scalar capacity wording | **PASS.** Current line 237 has \(L^2X^\varepsilon\). |
| exact graph-status wording | **PASS.** Current lines 276--277 distinguish proved_internal assembly from open M9-M1. |
| scope preservation | **PASS.** No repair changes an owner, implication, theorem claim, or exponent. |

## 6. Dependencies and exact artifacts used

This audit used only:

1. protocol.md;
2. the exact audited
   reviews/residual_transport_correlation_owner_scope_review.md; and
3. state/proof_obligations.yml only to verify the two statuses mentioned
   in the line-276 wording correction.

No candidate, kernel, State Patch, graph, review, synthesis, validation
matrix, proof draft, or lifecycle file was edited.

## 7. Final validation rule and state effect

The line-level TeX delimiter repairs and both wording repairs have been
applied and pass reinspection:

1. current line 237 contains
   <code>\(L^2X^\varepsilon\) scalar capacity</code>; and
2. current lines 276--277 contain the exact separate statuses:

<code>M9-M1-physical-one-count-assembly remains unchanged
proved_internal, and M9-M1 remains unchanged/open.</code>

No further source repair is recommended.

Final validation used all of the following rules:

1. parse Markdown while excluding fenced code, inline code spans, and
   every balanced <code>\[</code>--<code>\]</code> display block;
2. recognize and exclude balanced <code>\(</code>--<code>\)</code>
   inline-math spans;
3. in the remaining prose, reject every TeX command matching
   <code>\\[A-Za-z]+</code> and every mathematical token containing
   <code>_</code>, <code>^</code>, <code>\pm</code>, <code>\ge</code>,
   <code>\le</code>, <code>\ll</code>, <code>\asymp</code>,
   <code>\mid</code>, or <code>\pmod</code>;
4. allow bare parentheses matching only the equation-reference grammar
   <code>(184.C&lt;number&gt;&lt;optional-letter&gt;)</code>, including
   ranges formed from two such labels, plus genuine English prose
   parentheses;
5. manually confirm that the forty-five affected source lines in Section
   3 now contain balanced inline delimiters and that no mapped expression
   remains literal;
6. confirm the exact phrases \(L^2X^\varepsilon\) scalar capacity,
   assembly remains proved_internal, and M9-M1 remains open; and
7. rerun a full visual scan to ensure every inline and display delimiter
   is balanced, code spans remain balanced, and no equation label was
   accidentally converted into mathematics.

The current artifact satisfies the full post-repair pass condition: zero
unmatched delimiters, zero raw TeX
commands or mathematical expressions in prose outside math/code spans,
zero altered equation labels, exact \(L^2X^\varepsilon\) capacity
wording, exact protected statuses, and preservation of the original
mathematical scope.

**Final decision: GREEN. First bounded repair: none.**

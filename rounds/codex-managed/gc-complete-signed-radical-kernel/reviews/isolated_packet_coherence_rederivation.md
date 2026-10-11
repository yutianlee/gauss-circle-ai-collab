# Round218 isolated packet-coherence rederivation

## 1. Result: the proposed lower bound holds

**Verdict: GREEN for the exact abstract statement supplied.**

For each fixed even \(p\geq2\), all sufficiently large \(T\) satisfy

\[
 \boxed{\mathcal C_p(T,L)\geq c'T^{1+p/2}L^{-p}.}
 \tag{1}
\]

The constant \(c'>0\) is independent of \(T\), of \(L=L(T)\geq1\), of the centers, and of their multiplicities. No upper growth restriction on \(L\) is needed.

The decisive fact is stronger than a positivity argument after summing all labels: every ordered tuple whose centers lie in one sufficiently short interval has a positive main contribution to its **full weighted radius integral**, uniformly dominating the allowed global \(L^p\) errors. Taking the modulus of that integral preserves this contribution. Counting only these tuples proves (1).

This is a statement about the sum of individual integral moduli. It makes no lower-bound assertion for an arbitrary signed sum or for the modulus after summing all tuples.

## 2. Exact hypotheses, quantifiers, and constants

Use exactly the supplied assumptions:

- \(p\geq2\) is a fixed even integer.
- \(w\in C_c^\infty(\mathbb R)\) is nonnegative and equals one on an open interval \(J\).
- \(J'\) is a compact interval of positive length contained strictly inside \(J\).
- \(L(T)\geq1\) is arbitrary.
- \(\mathcal A_T\) is a finite labeled set with \(M_T\asymp T^2\), and all \(\rho_a\in TJ'\).
- \(H_T,H\) are real, \(H_T\to H\ne0\) in \(L^p(\mathbb R)\).
- \(cT^{-1/2}\leq c_a\leq CT^{-1/2}\), with \(c>0\) fixed.
- The global errors satisfy
  \[
   \epsilon_T:=
   T^{1/2}L^{1/p}\sup_{a\in\mathcal A_T}\|E_a\|_{L^p(dR)}
   \longrightarrow0.
   \tag{2}
  \]

The proof even permits complex errors; taking real parts of the normalized integrals below handles that extension. In particular it covers real functions \(F_a\).

Choose \(m_0>0\) such that \(M_T\geq m_0T^2\) for all sufficiently large \(T\). Let

\[
 h=\|H\|_p>0,\qquad W=\|w\|_\infty\geq1,\qquad
 \ell=|J'|>0,\qquad d=\operatorname{dist}(J',\mathbb R\setminus J)>0.
 \tag{3}
\]

The eventual constant can be taken as

\[
 c'=\frac{h^pc^pm_0^p}{2B^{p-1}},\qquad
 B=1+\ell/\eta,
 \tag{4}
\]

where a fixed \(\eta\in(0,1]\) is chosen from the \(L^p\) translation continuity of \(H\) in the proof. Thus it depends on the fixed profile and the packet constants, not on the center configuration or on \(L\). The threshold \(T_0\) also depends on the rates in \(H_T\to H\), in (2), and on the plateau margin \(d\). Uniformity in \(L\) means that the proof imposes no further condition on the prescribed function \(L(T)\), not that it assumes convergence rates absent from the hypotheses.

Only the lower coefficient bound and lower cardinality bound are needed for the lower estimate. The stated upper bounds on \(c_a\) and \(M_T\) are compatible with, but unnecessary for, this proof.

Every \(F_a\) lies in \(L^p\), so the products of \(p\) such functions lie in \(L^1\) by Hölder. Consequently all full radius integrals in the statement are well defined.

## 3. Independent proof

### Fix a coherent translation scale

Set

\[
 \delta=\frac{h}{2^{p+1}pW}.
 \tag{5}
\]

Then \(0<\delta\leq h\), and

\[
 Wp\delta(h+\delta)^{p-1}\leq h^p/4.
 \tag{6}
\]

Translations are continuous in \(L^p(\mathbb R)\). For completeness, approximate \(H\) in \(L^p\) by a continuous compactly supported function \(g\); translation preserves the \(L^p\) norm, and the translates of \(g\) converge in \(L^p\) uniformly as their translation parameter tends to zero. The triangle inequality then gives the same conclusion for \(H\).

We may therefore fix \(\eta\in(0,1]\) such that

\[
 \sup_{|s|\leq\eta}\|H(\,\cdot-s)-H\|_p\leq\delta/3.
 \tag{7}
\]

For all sufficiently large \(T\), convergence and (2) give

\[
 \|H_T-H\|_p\leq\delta/3,\qquad \epsilon_T/c\leq\delta/3.
 \tag{8}
\]

These choices do not depend on any individual label or tuple.

### Normalize a tuple of nearby centers

Take any ordered tuple \(a_1,\ldots,a_p\) for which all centers lie in an interval of length at most \(\eta/L\). Put

\[
 \rho_*=\rho_{a_1},\qquad x=L(R-\rho_*),\qquad
 s_j=L(\rho_{a_j}-\rho_*),\qquad |s_j|\leq\eta.
 \tag{9}
\]

Define

\[
 e_j(x)=c_{a_j}^{-1}E_{a_j}(\rho_*+x/L),\qquad
 b_j(x)=H_T(x-s_j)+e_j(x).
 \tag{10}
\]

The global error norm transforms exactly as

\[
 \|e_j\|_{L^p(dx)}
 =c_{a_j}^{-1}L^{1/p}\|E_{a_j}\|_{L^p(dR)}
 \leq\epsilon_T/c.
 \tag{11}
\]

Using translation invariance of the norm, (7), and (8),

\[
 \|b_j-H\|_p
 \leq\|H_T-H\|_p+
      \|H(\,\cdot-s_j)-H\|_p+\|e_j\|_p
 \leq\delta.
 \tag{12}
\]

In particular \(\|b_j\|_p\leq h+\delta\). The ordinary telescoping product identity and Hölder now imply

\[
 \left\|\prod_{j=1}^pb_j-H^p\right\|_1
 \leq \sum_{j=1}^p
       \|b_j-H\|_p
       \prod_{i<j}\|b_i\|_p
       \prod_{i>j}\|H\|_p
 \leq p\delta(h+\delta)^{p-1}.
 \tag{13}
\]

This is a global product estimate, without any pointwise assumption on the errors.

### Use the plateau margin and the even power

Choose a fixed \(K\geq1\) with

\[
 \int_{-K}^K|H(x)|^p\,dx\geq3h^p/4.
 \tag{14}
\]

Let

\[
 W_{T,\rho_*}(x)
 =w\!\left(\rho_*/T+x/(TL)\right).
 \tag{15}
\]

Because \(\rho_*/T\in J'\), \(L\geq1\), and \(d>0\), the inequality \(K/(TL)<d\) holds for all sufficiently large \(T\), uniformly in the center and in \(L\). Thus \(W_{T,\rho_*}=1\) on \([-K,K]\).

Since \(p\) is even and \(H\) is real, \(H^p=|H|^p\geq0\). The nonnegativity of \(w\) gives

\[
 \int_{\mathbb R}W_{T,\rho_*}(x)H(x)^p\,dx
 \geq3h^p/4.
 \tag{16}
\]

Equations (6) and (13) bound the difference between this integral and the one with \(\prod b_j\) by \(h^p/4\). Consequently

\[
 \operatorname{Re}\int_{\mathbb R}
    W_{T,\rho_*}(x)\prod_{j=1}^pb_j(x)\,dx
 \geq h^p/2.
 \tag{17}
\]

For real errors, the real-part operation can simply be omitted. Rescaling back to the full \(R\) line gives

\[
 \begin{split}
 \left|\int_{\mathbb R}w(R/T)\prod_{j=1}^pF_{a_j}(R)\,dR\right|
 &=L^{-1}\left(\prod_{j=1}^pc_{a_j}\right)
   \left|\int_{\mathbb R}W_{T,\rho_*}\prod_{j=1}^pb_j\,dx\right|\\
 &\geq\frac{h^pc^p}{2}T^{-p/2}L^{-1}.
 \end{split}
 \tag{18}
\]

The integral in (18) has never been truncated to a favorable radius interval. Equation (13) controls all possible error contributions on the full line, while (16) supplies positive main-profile mass.

### Count ordered coherent tuples

Partition \(TJ'\) into \(N\) disjoint intervals, with an endpoint convention assigning each center to exactly one interval, each of length at most \(\eta/L\). We can arrange

\[
 N\leq 1+\ell TL/\eta\leq BTL
 \qquad(T\geq1,\ L\geq1).
 \tag{19}
\]

Let \(n_i\) be the number of labels assigned to interval \(i\). Then \(\sum_i n_i=M_T\). Exactly \(n_i^p\) ordered tuples, including tuples with repeated labels, have every label in this interval. Hölder, or convexity, gives

\[
 \sum_{i=1}^N n_i^p\geq \frac{M_T^p}{N^{p-1}}
 \geq \frac{m_0^p}{B^{p-1}}
         T^{p+1}L^{-(p-1)}.
 \tag{20}
\]

The collections of tuples counted for different intervals are disjoint. Restrict the defining sum of nonnegative moduli to these tuples and apply (18). Equations (18) and (20) give exactly (1) with (4).

Nothing in this argument requires \(N\leq M_T\). If \(L\) grows so fast that most intervals are empty, the same convexity inequality still holds. The diagonal tuples alone also imply the stronger fallback count \(\sum_i n_i^p\geq M_T\); no density or spacing assertion has been hidden in (20).

## 4. First doubtful or unproved step

There is no remaining mathematical gap in the stated abstract lower bound.

The potentially doubtful transition would have been to infer a positive **full** product integral from agreement of profiles only near the center. Equations (11)--(13) explicitly avoid that step: they give global \(L^p\), then global \(L^1\), control of the entire product error. Contributions elsewhere cannot cancel the fixed mass in (16) beyond the stated error bound.

A different assertion about an arbitrary signed sum of tuples would not follow. It would permit cancellations between already integrated tuples, whereas \(\mathcal C_p\) takes a modulus before the tuple sum. No such change of order is made here.

## 5. Required controls and outcomes

All controls are analytic; no experiment or computation was run.

| Control | Exact outcome |
|---|---|
| Translated profiles | The fixed translation radius \(\eta\) follows from strong \(L^p\) continuity of translations of \(H\). Global convergence of \(H_T\) transfers this uniformly to all sufficiently large \(T\), as in (12). |
| Repeated centers and multiplicities | Distinct labels sharing a center remain distinct in each occupancy \(n_i\). Repetitions improve concentration and do not diminish the count. No multiplicity bound is used. |
| Ordering and repeated labels | The supplied sum is over the Cartesian power \(\mathcal A_T^p\); a bin contributes exactly \(n_i^p\). There is no division by \(p!\) or replacement by a falling factorial. |
| Endpoints of \(J'\) | The entire closed interval \(J'\) has positive distance \(d\) from the complement of \(J\). Thus every permitted center, including an endpoint center, admits the same scaled core \([-K,K]\) inside the plateau. |
| Endpoints of bins | A half-open convention, with the final endpoint included in the last bin, assigns each label exactly once. Within-bin center distances remain at most \(\eta/L\). |
| Arbitrarily fast \(L(T)\) | The plateau condition uses only \(TL\geq T\). The number of bins is at most \(BTL\); Jensen/Hölder remains true even when bins greatly outnumber labels. No upper bound on \(L\) occurs. |
| Errors with narrow large spikes | Such errors are allowed. Their global \(L^p\) norms, after the exact rescaling (11), suffice for (13); no uniform pointwise error estimate is invoked. |
| Non-smooth or oscillating \(H_T\) | Smoothness, boundedness, and pointwise convergence are unnecessary. Strong \(L^p\) convergence alone gives the required norm bounds and translation comparison. |
| Odd profiles for even \(p\) | Oddness causes no cancellation in \(H^p=|H|^p\). The proof works unchanged. No parity assumption on \(H_T\) or \(H\) is imposed. |
| Fixed \(p\) | All constants and the scale \(\eta\) may depend on \(p\). No uniform assertion as \(p\) grows with \(T\) is proved. |
| The weight | Smoothness and compact support of the supplied weight are more than the proof needs. Boundedness, nonnegativity, and the stated plateau suffice. |
| Vanishing limiting profile | If \(H=0\), the positive core mass is unavailable and a lower bound need not hold. The nonzero hypothesis is essential. |

**Why even \(p\) matters.** For odd \(p\), the proposed assertion is false under otherwise identical assumptions. Choose a fixed nonzero real smooth compactly supported odd function \(H\), set \(H_T=H\), take every center equal to \(Tr_0\) for a fixed \(r_0\in J'\), take \(E_a=0\), and use \(M_T=\lfloor T^2\rfloor\) labels and \(c_a=T^{-1/2}\). For all large \(T\) and every \(L\geq1\), the support of each profile lies inside the plateau. Every tuple integral is then

\[
 T^{-p/2}L^{-1}\int_{\mathbb R}H(x)^p\,dx=0,
\]

because \(H^p\) is odd. Hence \(\mathcal C_p=0\). This counterexample uses a fixed smooth profile and zero errors; it is not caused by a regularity defect.

## 6. Dependencies, artifacts, and isolation provenance

- Campaign: gc-complete-signed-radical-kernel, round218.
- Role: independent, statement-only rederivation of the isolated packet-coherence control.
- Generated date: 2026-09-28.
- Exact new statement: rounds/codex-managed/gc-complete-signed-radical-kernel/briefs/isolated_packet_coherence_statement.md, SHA256 9c3ec90596f8c938cadb31ac9bc9f3bde646c1cbf3095b69d0855e1ff65eaae1.
- Previously permitted protocol: protocol.md, SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
- Previously permitted isolated radial statement: rounds/codex-managed/gc-complete-signed-radical-kernel/briefs/blind_joint_radial_statement.md, SHA256 1211b43b9aec8993d53f7ddfd47c05c4877bab1df1671a46179f5903f35ce632. The radial lemma is not a dependency of the present proof.
- The earlier radial report was frozen and its SHA256 339971305a6dd5af4460d8827cb920c75350531294021b50df8c9249be062a47 reported to the conductor before this statement was opened. It was not reread or edited for this task.
- Mathematical dependencies: translation continuity in \(L^p\), density of compactly supported continuous functions, Hölder, the telescoping product identity, and a finite interval partition.
- No web/source, claimant, arithmetic application, graph, manifest, strategy, current sibling report, control, or synthesis was read. No agent was launched, and no experiment was performed. Only this assigned review was written.

**Isolation disclosure.** This agent retains prior round217 full-frontier/source and mathematical seam context, and its own preceding round218 abstract radial derivation. It is not a fresh history-free agent. This packet-coherence result is nevertheless statement-only as to the new lemma: no current claimant proof or actual application was supplied or inspected.

## 7. Recommended state effect

**Recommend promote this exact abstract packet-coherence lower bound as an independently proved control, subject to the conductor's ordinary seam and graph procedures.**

Its scope is the sum of moduli after the full radius integrals, under a common nonzero limiting profile in global \(L^p\), uniform relative global \(L^p\) errors, positive coefficient lower bounds, and fixed even \(p\). Ordering, repeated labels, arbitrary center multiplicities, and arbitrary growth of \(L\geq1\) are included.

No actual arithmetic family has been verified to satisfy these hypotheses in this assignment. No signed-sum lower bound, state mutation, synthesis, or successor decision is made. This completes the assigned same-round seam.

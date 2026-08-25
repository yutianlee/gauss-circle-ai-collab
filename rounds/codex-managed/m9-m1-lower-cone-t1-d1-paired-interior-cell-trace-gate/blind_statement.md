# Round 158 statement-only problem

Work only from this statement and the research protocol. Do not inspect
the graph, strategy, claimant seed, sibling reports, proof draft, or
earlier Round-158 artifacts.

Fix \(A>0\),

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K.
\]

For each odd \(d\mid N\), put

\[
 c=\frac qd,\qquad H=\frac c2,\qquad
 \mathcal V_d^\circ=\{v\bmod H:v\ne0,H/2\}.
\]

On the two strict signed blocks, let

\[
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad
 \lambda_+(j)=j+1,\qquad
 \lambda_-(j)=-j,
\]

where \(F_j\) is complex and retains a zero-extended BV profile, the
phase \(e(\sqrt{x^2-j}-x)\), transitions, half-open choices, and
endpoints. Its amplitude is
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\), and physical \(x\)-support
has span \(O(KX^\varepsilon)\).

The paired interior theta row is

\[
\begin{aligned}
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\in\mathcal V_d^\circ}
 \widehat B_j(2dv)K(-v^2,-j;c).
\end{aligned}
\]

The full half-period inverse identity and the complete zero and Nyquist
row estimates are available as controls, but a theorem for a whole row
may not be transferred to one of its Abel pieces without proof.

Independently:

1. derive the exact prefix or suffix Abel formula on each sign;
2. isolate the moving-cell trace, including every outer endpoint term;
3. determine its exact full-frequency physical form and the separate
   \(v=0\) and \(v=H/2\) trace costs;
4. test the endpoint congruences \(j^2+j+1\equiv0\pmod N\) and
   \(j^2-j\equiv0\pmod N\), including all prime powers;
5. decide whether those endpoint roots control the whole trace or leave
   a strict prefix or suffix survivor;
6. rewrite any survivor as an exact signed selected-coordinate sum with
   all profiles, phases, signs, transitions, and endpoints; and
7. prove the full trace target, a strict owner-complete range or subrow,
   or the first exact arithmetic, sign, coefficient, source, endpoint,
   or restored-power obstruction.

Retain arbitrary \(N\), every odd \(d\mid N\), both complementary
interior representatives, the edge case \(c=4\), the external scalar
seam, and all \(N,M,V,d,c\) powers. Cardinality and theorem right sides
are upper capacities, not signed cancellation.

Your report must have exactly seven substantive sections:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control tests and outcomes.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

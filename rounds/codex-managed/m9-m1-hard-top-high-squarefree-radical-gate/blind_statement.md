# Round 181 statement-only squarefree-radical problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put (e(z)=e^{2\pi iz}). Let (L\ge2), (X>0), and let
(a(h,n)\in\mathbb C) be supported on integer pairs

\[
 h\asymp L,\qquad n\ {\rm odd},\qquad 4h<n<16h,
\]

with (|a(h,n)|\le \mathcal X). Define

\[
 C(r)=\sum_{\substack{h\mid r,\ h\asymp L\\
                       r/h\ {\rm odd},\ 4h<r/h<16h}}
       \chi_4(r/h)a(h,r/h).
\tag{B181.1}
\]

Then

\[
 \sum_{h,n}\chi_4(n)a(h,n)e(\sqrt{Xhn})
 =\sum_r C(r)e(\sqrt{Xr}).
\tag{B181.2}
\]

Write uniquely (r=st^2), where (s) is squarefree. The proposed target
for one fixed actual coefficient family is

\[
 \left|\sum_{\substack{s>L\\\mu^2(s)=1}}
 \sum_{t\ge1}C(st^2)e(t\sqrt{Xs})\right|
 \ll L^{3/2}\mathcal X.
\tag{B181.3}
\]

Tasks:

1. derive (B181.2) exactly and prove the sharp universal incidence bound
   for the complementary sector (s\le L);
2. calculate the coefficient-insensitive capacity of (B181.3) and the
   missing factor relative to (L^{3/2}\mathcal X);
3. test the stronger fixed-(t) proposal with support length
   (S_t\asymp L^2/t^2) and target (S_t^{3/4}\mathcal X);
4. determine whether (B181.3) follows from the displayed hypotheses alone;
5. construct perfect-square-centre, high-radical (t=1), complex
   dechirped, arbitrary-coefficient, character-erased, boundary, one-site,
   and one-fibre controls; and
6. identify the first additional structural relation an actual coefficient
   family would need to obtain the missing square-root saving.

Do not infer a lower bound for a special arithmetic coefficient from an
adversarial capacity example. Computation, if any, is diagnostic only.
Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.


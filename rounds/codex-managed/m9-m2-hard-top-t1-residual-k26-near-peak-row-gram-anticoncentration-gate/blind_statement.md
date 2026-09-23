# Round 180 statement-only finite row-Gram problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put \(e(t)=e^{2\pi i t}\). Let \(J>0\), \(L\ge 2\), and let
\(M\asymp L^2\) be a positive integer. For odd positive integers \(d\), let
\(\lambda_{d,m}\in\mathbb R\) be finitely supported, with at most \(CL\)
values of \(m\) in each row and

\[
\sum_{d\ {\rm odd}}\sum_m|\lambda_{d,m}|^2
\le C L^2\mathcal X.
\tag{B180.1}
\]

Here \(\mathcal X\ge1\) is a harmless loss factor. Define

\[
R_{\epsilon,d}(\theta)
=\sum_m(-1)^{\epsilon m}\lambda_{d,m}
 e(J\sqrt{dm}+dm\theta),
\qquad
Z_\epsilon(\theta)=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta)
\tag{B180.2}
\]

for \(\epsilon\in\{0,1\}\). For integers
\(|\nu|\le\lceil\sqrt L\rceil\), put

\[
I_\nu=
\left[\frac{\nu-1/2}{M},\frac{\nu+1/2}{M}\right)\pmod1
\tag{B180.3}
\]

and

\[
\mathcal O_{\epsilon,\nu}
=2\Re\sum_{d<d'}\chi_4(d)\chi_4(d')
 \int_{I_\nu}R_{\epsilon,d}(\theta)
 \overline{R_{\epsilon,d'}(\theta)}\,d\theta.
\tag{B180.4}
\]

Tasks:

1. derive the exact cell kernel, including its zero-difference value;
2. prove the best universal row-diagonal bound from (B180.1);
3. combine a hypothetical one-sided bound
   \(\frac12\sum_\epsilon\mathcal O_{\epsilon,\nu}\ll L\mathcal X\)
   with the Fejér estimate
   \(F_M(\theta)\ll\min(M,(M\|\theta\|^2)^{-1})\);
4. determine exactly what follows on the far arcs
   \(M\|\theta\|\ge\sqrt L\);
5. test whether the desired off-row bound follows from the displayed
   hypotheses alone; and
6. if it is false universally, construct complex-dechirped, real
   cosine-dechirped, arbitrary-real-sign, constant-character, one-row,
   one-site, and exact-product-collision controls, and state the first
   additional structural relation a literal theorem would need.

Do not take a modulus around the row-pair sum unless analyzing a false
positive control. Computation, if any, is diagnostic only. Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

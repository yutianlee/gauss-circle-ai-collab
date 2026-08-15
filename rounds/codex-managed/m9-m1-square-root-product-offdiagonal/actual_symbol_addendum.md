# Round 68 selected-context addendum: exact interior symbol

This addendum is for the discovery and hostile/source tasks only. It was
created after the statement-only blind report and is not part of that
report's evidence.

Start from the accepted fixed-interior antecedent

\[
 S_k=\sum_j\chi_4(j)\Xi(j/J)e(kX/j),
 \qquad J=\sqrt X.
\]

Resolve

\[
 \chi_4(j)={e(j/4)-e(3j/4)\over2i}
\]

and apply Poisson/B-process in \(j\). In the positive stationary branch
write the odd dual variable as

\[
 q=4r-\rho>0,
 \qquad \rho\in\{1,3\}.
\]

The stationary point, phase, curvature, and leading amplitude are

\[
 j_*=2\sqrt{kX/q},
 \qquad
 f(j_*)=\sqrt{Xkq},
 \qquad
 f''(j_*)={q^{3/2}\over4(kX)^{1/2}},
\]

\[
 |f''(j_*)|^{-1/2}
 =2(kX)^{1/4}q^{-3/4}.
\]

After factoring the Round-67 common size \((J/k)^{1/2}\), the normalized
symbol is, up to one fixed branch unit and harmless fixed smooth cutoffs,

\[
 c_\rho(k,r)
 =\left({k\over q}\right)^{3/4}
 \Xi\!\left(2\sqrt{k/q}\right),
 \qquad q=4r-\rho.
\tag{68.A1}
\]

Thus the two residues recombine, up to one global unit constant, as

\[
 P_k=\sum_{\substack{q\in\mathbb Z\\q\ \mathrm{odd}}}
 \chi_4(q)C(k/q)e(\sqrt{Xkq}),
\tag{68.A2}
\]

on fixed positive ratio support, with \(C\in C_c^\infty((0,\infty))\).
In particular

\[
 |(k\partial_k)^a(q\partial_q)^bC(k/q)|\ll_{a,b,C}1.
\tag{68.A3}
\]

Consequences for the round:

1. phase-conjugating arbitrary \((k,r)\)-dependent symbols are excluded;
2. Mellin separation of \(C(k/q)\) is lawful with Schwartz mode weight;
3. every proof must still retain the two odd residue classes and all
   fixed-interior B-process errors;
4. this addendum does not supply the desired second-moment estimate.


# Candidate: canonical balanced smooth quarter packet

For each literal balanced smooth label \(\omega\), fix one smooth gcd
partition and define

\[
 \begin{aligned}
 \mathcal Q_{\omega,G}(R)
 =\sum_{\substack{u,v\\(u,v)=1\\u\ {\rm odd}}}
 \chi_4(u)\sum_n
 \Big[&
 \widehat F_{\omega,u,v,G}
  \big(G(n-R\sqrt{uv}-1/4)\big)\\
 -&
 \widehat F_{\omega,u,v,G}
  \big(G(n-R\sqrt{uv}-3/4)\big)
 \Big].
 \end{aligned}
\tag{112.C1}
\]

Seek an exact atom dictionary for which

\[
 \mathcal T_{\mathrm{bal,res}}^+
 ={1\over2i}\sum_{\omega,G}G\mathcal Q_{\omega,G}(R)
 +O_\varepsilon(L^{3/2}X^\varepsilon),
\tag{112.C2}
\]

with every term in the error already owned exactly once. The negative
frequency should be the conjugate only by the literal real-even physical
symmetry.

The desired open theorem is the linear outside-absolute estimate

\[
 \left|\sum_{\omega,G}G\mathcal Q_{\omega,G}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{112.C3}
\]

This round must certify (112.C1)--(112.C2), the exact scope of the
\(\omega,G\) sums, and the norm/capacity ledger. It may promote (112.C3)
only if it actually proves the signed estimate.


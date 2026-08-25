# Statement-only squarefree-kernel bilinear problem

Let $N$ be a positive integer, $R\asymp N^{1/4}$, and

$$
 1\ll M\le R^2,\qquad M^{449}\ll R^{780}.
$$

Let $A$ be a compactly supported function on a fixed dilation of
$[M,2M]$, extended by zero, with

$$
 \|A\|_\infty+\operatorname {Var}A\ll X^\varepsilon.
$$

For every positive odd integer $\ell$, let $k(\ell)$ be the unique nearest
integer to $\sqrt{N\ell}$ and write uniquely
$\ell=\tau s^2$, where $\tau$ is odd squarefree and $s$ is odd.  Define

$$
 \mathcal P^*=\sum_{\substack{\ell=\tau s^2\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\le s<\lceil M^{1/4}\rceil}}
 \chi_4(\tau)(\tau s^2)^{-3/4}
 A(\tau s^2)e(s\sqrt{N\tau}).
\tag{153.BL1}
$$

Determine whether

$$
 |\mathcal P^*|\ll_\varepsilon X^\varepsilon
\tag{153.BL2}
$$

holds uniformly.  In particular, test the exact squarefree inversion

$$
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),\qquad \tau=a^2b,
\tag{153.BL3}
$$

which gives the two-variable phase $as\sqrt{Nb}$ and dyadic relation
$A_0^2Bs^2\asymp M$.

Your analysis must retain the $s=1$ layer, every inversion term including
$a=1$, the Mobius sign, $\chi_4(b)$, the exact large-defect mask evaluated
at $a^2bs^2$, the finite support, zero extension, and endpoints.  Derive
the complete Type-I/Type-II, Cauchy, diagonal, exact-collision,
near-collision, and $R,M,A_0,B,s$ power ledger for every proposed
bilinear or spacing estimate.

Do not assume that separately bounding the $a=1$ term proves anything
about the complete Mobius sum.  Do not replace a signed correlation by an
absolute spacing energy without pricing the pigeonhole multiplicity.  An
upper capacity or a coherent model is not a signed lower bound.

Return a proof of (153.BL2), a strict owner-complete range, or the first
rigorous method-specific obstruction.

# Statement-only packet: weighted theta zero row

Fix $A>0$, let $N=\lfloor X\rfloor$, $1\ll M\le N^{1/2}$, and put

$$
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM},\qquad
 J_A<V\le K,\qquad q=4N.
\tag{156.BL1}
$$

For every integer $j$ with $V<|j|\le2V$, let $B_j(x)$ be the literal
zero-extended coefficient on one complete residue system modulo $q$:

$$
 B_j(x)=
 {\bf1}_{x\ge1}\,{\bf1}_{-x\le j\le x-1}\,
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(-\frac{j}{x+\sqrt{x^2-j}}\right),
\tag{156.BL2}
$$

with every actual support component, transition, hard endpoint, and
half-open cell retained. The real profile is extended off congruence in
the inherited literal way and is zero outside its physical support
$x\asymp K$. It satisfies

$$
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{156.BL3}
$$

Define

$$
 \widehat B_j(0)=\sum_{x\bmod q}B_j(x).
\tag{156.BL4}
$$

For every odd $d\mid N$, put $c=4N/d$ and

$$
 K(0,-j;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(-aj),
 \qquad
 \epsilon_a=
 \begin{cases}
 1,&a\equiv1\pmod4,\\
 i,&a\equiv3\pmod4.
 \end{cases}
\tag{156.BL5}
$$

The object to estimate is

$$
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,
 \widehat B_j(0)K(0,-j;c).
\tag{156.BL6}
$$

Prove $\mathcal Z_U(V)\ll_{\varepsilon,A}X^\varepsilon$, prove a strict
owner-complete positive-power range, or isolate the first rigorous
arithmetic or analytical obstruction.

Your derivation must be independent. In particular:

- derive the exact decomposition of $\epsilon_a(c/a)$ into additive
  transforms of real Dirichlet characters;
- identify their primitive conductors and induced-modulus local factors
  for every prime power, including $p=2$;
- classify the exact support and value as a function of $j$;
- restore every $d$, both signs, the actual $\widehat B_j(0)$ variation,
  and all endpoints before claiming a power;
- distinguish a signed estimate from an upper capacity; and
- state the sharpest exact weighted partial-sum theorem still needed if
  the target is not proved.

Do not read any strategy, graph, prior-round report, sibling report, proof
draft, or synthesis. Write only the assigned seven-section report.


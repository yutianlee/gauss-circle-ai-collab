# Round 156 conductor candidate: the complete theta zero row is target-safe

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Round: 156
- Role: conductor proof candidate pending independent reports and terminal review
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Proposed terminal label: outer_defect_zero_mode_target
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result

Let $A>0$ be fixed and let

$$
 J_A=M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM},\qquad q=4N.
\tag{156.CT1}
$$

For every literal profile component, both defect signs, and all endpoints,
the complete $v=0$ row

$$
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,
 \widehat B_j(0)K(0,-j;c),
 \qquad c=\frac{4N}{d},
\tag{156.CT2}
$$

satisfies

$$
 \boxed{\mathcal Z_U(V)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon
 \ll_{\varepsilon,A}X^\varepsilon.}
\tag{156.CT3}
$$

Thus the zero mode is target-safe throughout the full outer-defect range.
The proof uses the exact two-character decomposition of the theta
multiplier, induced-character Gauss sums, and the actual bounded variation
of $j\mapsto\widehat B_j(0)$. It does not estimate the nonzero matrix and
changes no positive-power defect range, $M$-boundary, downstream theorem,
or global exponent.

## 2. Exact statement and hypotheses

For fixed $j$, the ambient coefficient is the literal zero extension

$$
 B_j(x)=
 {\bf1}_{x\ge1}{\bf1}_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(-\frac{j}{x+\sqrt{x^2-j}}\right),
\tag{156.CT4}
$$

component by component, with the inherited off-congruence profile,
transitions, half-open endpoints, strict dyadic mask, and exact residual
phase. Its physical $x$-support has total length $O(KX^\varepsilon)$ and

$$
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon W X^\varepsilon,\qquad W=M^{-3/4}.
\tag{156.CT5}
$$

Put

$$
 A_j=\widehat B_j(0)=\sum_{x\bmod q}B_j(x).
\tag{156.CT6}
$$

The external $B_{1,U}(1)$ factor remains outside (156.CT2).

For $m=N/d$ and $c=4m$,

$$
 K(0,-j;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(-aj).
\tag{156.CT7}
$$

No parity, squarefree, primitivity, or coprimality assumption is placed on
$N$ or $m$.

## 3. Proof or derivation

### 3.1 Actual $j$-variation of the zero Fourier coefficient

For fixed physical $x$, the profile argument $(x^2-j)/N$ is monotone in
$j$. Its zero-extended total variation on either signed dyadic block is
$O(WX^\varepsilon)$. The exact phase is

$$
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x,
\tag{156.CT8}
$$

and on literal support

$$
 \left|\frac{\partial}{\partial j}
 \bigl(\sqrt{x^2-j}-x\bigr)\right|
 =\frac1{2\sqrt{x^2-j}}\ll K^{-1}.
\tag{156.CT9}
$$

Because the $j$-block has length $O(V)\le O(K)$, the phase factor has
total variation $O(1)$. The cell and support indicators create only
$O(1)$ jumps for fixed $x$. The product-variation inequality therefore
gives

$$
 \sup_j|B_j(x)|+
 \sum_{j\ {\rm in\ one\ signed\ block}}
 |B_{j+1}(x)-B_j(x)|
 \ll_\varepsilon W X^\varepsilon.
\tag{156.CT10}
$$

There are $O(KX^\varepsilon)$ physical $x$ values across all literal
components. Summing (156.CT10) proves

$$
 \mathcal A:=
 \max_j|A_j|+
 \sum_{j\ {\rm in\ the\ two\ signed\ blocks}}|A_{j+1}-A_j|
 \ll_\varepsilon K M^{-3/4}X^\varepsilon
 =N^{1/2}M^{-1/4}X^\varepsilon.
\tag{156.CT11}
$$

All block endpoints are included in this zero-extension variation.

### 3.2 Two primitive real characters

Write $m=u^2s$ with $s$ squarefree. For every odd unit $a\bmod4m$,

$$
 \epsilon_a=\alpha+\beta\chi_4(a),\qquad
 \alpha=\frac{1+i}{2},\qquad\beta=\frac{1-i}{2},
 \qquad
 \left(\frac{4m}{a}\right)=\left(\frac sa\right).
\tag{156.CT12}
$$

Define the fundamental discriminants

$$
 \Delta_+=
 \begin{cases}
 s,&s\equiv1\pmod4,\\
 4s,&s\equiv2,3\pmod4,
 \end{cases}
 \qquad
 \Delta_-=
 \begin{cases}
 -s,&s\equiv3\pmod4,\\
 -4s,&s\equiv1,2\pmod4.
 \end{cases}
\tag{156.CT13}
$$

The convention $\Delta_+=1$ gives the primitive principal character of
conductor one. Let $\chi_\pm=(\Delta_\pm/\cdot)$ and
$f_\pm=|\Delta_\pm|$. Then $f_\pm\mid c$,

$$
 \left(\frac ma\right)=\chi_+(a),\qquad
 \chi_4(a)\left(\frac ma\right)=\chi_-(a)
\tag{156.CT14}
$$

on the units modulo $c$. Hence

$$
 K(0,-j;c)=\alpha\,G_{c,\chi_+}(-j)
 +\beta\,G_{c,\chi_-}(-j),
\tag{156.CT15}
$$

where

$$
 G_{c,\chi}(n)=
 \sum_{\substack{a\bmod c\\(a,c)=1}}\chi(a)e_c(an)
\tag{156.CT16}
$$

is the additive transform of the character induced from its primitive
conductor $f$ to $c$.

### 3.3 Exact induced-modulus formula

Put $c=fL$ and

$$
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p.
\tag{156.CT17}
$$

Inclusion-exclusion of the primes in $R_f$, followed by grouping a lifted
residue modulo $f$, gives the exact formula

$$
 \boxed{
 G_{c,\chi}(n)=
 \tau(\chi)
 \sum_{\substack{r\mid R_f\\L/r\mid n}}
 \mu(r)\chi(r)\frac{L}{r}\,
 \overline{\chi}\!\left(\frac{n}{L/r}\right).}
\tag{156.CT18}
$$

Indeed, after $a=rb$ the inner sum modulo $c/r=f(L/r)$ vanishes unless
$L/r\mid n$; in the surviving case it is
$(L/r)\tau(\chi)\overline\chi(n/(L/r))$. This proves at once every
prime-power and two-adic support condition. At a prime dividing $f$, the
valuation of $n$ is exactly the exponent contributed by $L$; at a prime
outside $f$, it is at least one less than its exponent in $c$. Repeated
prime and squareful factors are therefore retained rather than suppressed.

For $f=1$, (156.CT18) is precisely the Ramanujan sum $c_c(n)$.

### 3.4 Uniform weighted transform bound

Suppose first that $f>1$. For each $r\mid R_f$, put $h=L/r$. The
subsequence $A_{hn}$ has supremum plus total variation at most
$\mathcal A$. Abel summation and Pólya--Vinogradov for the primitive
nonprincipal character $\chi$ give

$$
 \left|\sum_{n:\,hn\ {\rm in\ a\ signed\ block}}
 A_{hn}\overline\chi(-n)\right|
 \ll_\varepsilon\mathcal A f^{1/2}X^\varepsilon.
\tag{156.CT19}
$$

Using $|\tau(\chi)|=f^{1/2}$ in (156.CT18),

$$
 \begin{aligned}
 \left|\sum_{V<|j|\le2V}A_jG_{c,\chi}(-j)\right|
 &\ll_\varepsilon
 \mathcal A f\sum_{r\mid R_f}\frac{L}{r}X^\varepsilon\\
 &\ll_\varepsilon \mathcal A cX^\varepsilon.
 \end{aligned}
\tag{156.CT20}
$$

If $f=1$, then $G_{c,\chi}=c_c$. Since $c>1$,

$$
 \sup_Y\left|\sum_{1\le j\le Y}c_c(j)\right|
 \le\sum_{\ell\mid c}\ell\ll_\varepsilon cX^\varepsilon.
\tag{156.CT21}
$$

Partial summation with (156.CT11) gives (156.CT20) in the principal case
as well. Equations (156.CT15) and (156.CT20) therefore imply, uniformly
for every $d$,

$$
 \left|\sum_{V<|j|\le2V}
 \widehat B_j(0)K(0,-j;c)\right|
 \ll_\varepsilon\mathcal A cX^\varepsilon.
\tag{156.CT22}
$$

### 3.5 Restoration of every $d$-stratum

Substituting (156.CT22) into (156.CT2) and using $dc=q$ gives

$$
 \begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 \frac{\mathcal A}{Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}d\sqrt c\,cX^\varepsilon\\
 &=\frac{\mathcal A}{N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\sqrt{\frac{4N}{d}}\,
 X^\varepsilon\\
 &\ll_\varepsilon\frac{\mathcal A}{\sqrt N}X^\varepsilon
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
 \end{aligned}
\tag{156.CT23}
$$

This proves (156.CT3).

## 4. First doubtful or unproved step

Within the frozen zero row, the first step still requiring independent
review is the literal profile claim (156.CT10)--(156.CT11), especially
the off-congruence zero extension and all transition endpoints. The
character algebra and normalization are exact once that variation bound
is accepted.

After the zero row, the first genuinely unproved analytical object is the
incomplete nonzero matrix

$$
 \sum_{V<|j|\le2V}
 \sum_{\substack{v\bmod(2N/d)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;4N/d),
\tag{156.CT24}
$$

with the full exterior normalization, every $d$, both signs, actual
profile, complementary frequencies, and endpoints. Nothing in the present
argument separates $\widehat B_j(2dv)$ when $v\ne0$.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal_zero_mode_row | PASS. Equation (156.CT2) retains all exterior factors and literal profile data. |
| exact_epsilon_two_character_decomposition | PASS. Equations (156.CT12)--(156.CT15) are exact for all odd units. |
| primitive_conductor_and_induced_modulus | PASS pending independent review. Both fundamental discriminants and the lift to $c$ are explicit. |
| all_prime_power_two_adic_local_factors | PASS through the exact global formula (156.CT18), which implies each local support condition without suppressing $p=2$. |
| valuation_support_and_squareful_strata | PASS. The $L/r$ divisibility and primitive-character zero retain every repeated prime. |
| d_sum_and_full_normalization | PASS. Equation (156.CT23) restores all odd $d$ and uses only $dc=q$. |
| actual_Bhat0_j_variation | PASS pending endpoint review. Equation (156.CT11) is derived before character summation. |
| positive_negative_defect_and_endpoints | PASS. The two signed blocks are summed separately and zero-extension jumps are in the variation norm. |
| N_M_V_d_conductor_power_ledger | PASS. The final bound is $M^{-1/4}X^\varepsilon$. |
| upper_capacity_vs_signed_sum | PASS. Character cancellation proves an upper bound; no positive capacity is called a lower bound. |
| nonzero_and_downstream_scope | PASS. The nonzero matrix and every broader owner remain open. |

No numerical experiment is used.

## 6. Dependencies and exact artifacts used

This conductor proof uses the accepted Round-154 definition and variation
of the literal profile, the Round-155 normalized zero row and arbitrary-$N$
gcd partition, and the Round-156 strategy, barrier packet, and seed. Its
direct artifacts are:

- strategy/round156_d1_outer_defect_zero_mode_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_seed.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md.

No graph, proof draft, validation matrix, or synthesis is changed by this
candidate.

## 7. Recommended state effect

Subject to independent mathematical, endpoint, and source GREEN reviews:

- promote the complete $v=0$ row as target-safe with the stronger bound
  $M^{-1/4}X^\varepsilon$;
- promote the exact two-character and induced-modulus identities
  (156.CT12)--(156.CT18) with all prime-power and two-adic strata;
- retain the nonzero matrix as the first open D=1 outer-defect interface;
- reject the previous absolute zero-mode capacity as a lower obstruction,
  and reject primitive, squarefree, odd-$N$, or constant-weight shortcuts;
  and
- make no positive-power defect-range, $M$-boundary, endpoint-assembly,
  other-owner, M9, bridge, target, or global-exponent change.


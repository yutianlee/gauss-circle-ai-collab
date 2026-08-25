# Blind report: sharp band-limited majorant and the bandwidth--mass obstruction

- Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`
- Round: `134`
- Task: `blind_bandlimited_quadratic_majorant_feasibility`
- Role/access: blind rederiver, statement-only
- Status: candidate evidence only

## 1. Result: sharp extremal lemma and quantitative no-go

There is a lawful one-sided contraction of the exact full-character block square, but every such universal contraction has an exactly quantifiable zeroth-coefficient cost.

Let \(0\leq \Delta\leq H-1\), put \(q=\Delta+1\), and write

\[
H=mq+r,\qquad m\geq 1,\qquad 0\leq r<q.
\]

Among all real trigonometric polynomials \(T\) of degree at most \(\Delta\) satisfying \(T(\alpha)\geq F_H(\alpha)\) for every \(\alpha\), the least possible zeroth coefficient is

\[
\boxed{
\mu(H,q)=qm^2+(2m+1)r
=\frac{H^2}{q}+r\left(1-\frac rq\right).
}
\tag{1.1}
\]

It is attained by the explicit folded-Dirichlet majorant

\[
\boxed{
T^*_{H,q}(\alpha)=\left|mD_q(\alpha)+D_r(\alpha)\right|^2,
}
\tag{1.2}
\]

where \(D_0=0\). Consequently

\[
\inf_{T\geq F_H}\|T-F_H\|_{L^1(\mathbb T)}
=\mu(H,q)-H
=qm(m-1)+2mr,
\tag{1.3}
\]

and, in particular,

\[
\frac{t_0}{H}\geq \frac{H}{q}.
\tag{1.4}
\]

Thus a fixed-power contraction \(q\leq H X^{-\eta}\), with fixed \(\eta>0\), forces \(t_0/H\geq X^\eta\). Likewise \(q\leq H^{1-\eta}\) forces \(t_0/H\geq H^\eta\). A target-safe zeroth coefficient \(t_0\leq H X^{o(1)}\) therefore requires \(q\geq H X^{-o(1)}\); it is incompatible with a fixed-power contraction.

This is the first exact obstruction. The majorant (1.2) does give a strict, endpoint-complete, noninvertible reduction to \(q\) shifts, and it keeps the actual \(\chi_4\)-sum inside the square. It does **not**, using the supplied capacities, prove

\[
\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.
\]

The target itself is not refuted: a new estimate exploiting the literal phases and the cross-\(p\) \(\chi_4\)-correlations could conceivably control the majorized form. What is ruled out is a fixed-power bandwidth gain with target-safe zeroth mass, or a gain obtained solely by replacing the \(H\)-lag capacity by a shorter lag count.

## 2. Exact statement and hypotheses

All sequences below are finitely supported and are extended by zero before shifts. Form

\[
A(k)=\sum_{p>0\atop p\ \mathrm{odd}}\chi_4(p)b_{p,k},
\qquad
S_HA(n)=\sum_{a=0}^{H-1}A(n+a).
\]

The following assertions hold without changing the literal profiles in (134.B1).

1. **Exact block identity.**

   \[
   \mathcal E_\chi
   =C_H\sum_n|S_HA(n)|^2
   =C_H\int_0^1F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
   \tag{2.1}
   \]

2. **Exact order relation.** For a real trigonometric polynomial \(T\), pointwise multiplier domination \(T\geq F_H\) implies

   \[
   \sum_n|S_HA(n)|^2
   \leq \int_0^1T(\alpha)|\widehat A(\alpha)|^2\,d\alpha
   \tag{2.2}
   \]

   for every finitely supported complex \(A\). Conversely, if (2.2) holds for every such \(A\), then \(T\geq F_H\) pointwise. This universal positive-semidefinite order is not the same as coefficientwise domination, pointwise domination of an unsquared scalar selector, or an inequality verified only on the literal family (134.B1).

3. **Sharp degree-\(q-1\) theorem.** For \(1\leq q\leq H\), (1.1) is the exact minimum zeroth coefficient under \(T\geq F_H\), and (1.2) attains it.

4. **Exact physical reduction.** Define

   \[
   n_j=\begin{cases}m+1,&0\leq j<r,\\m,&r\leq j<q.\end{cases}
   \tag{2.3}
   \]

   Since \(mD_q+D_r=\sum_{j=0}^{q-1}n_je(j\alpha)\), (1.2) and Parseval give the endpoint-complete inequality

   \[
   \boxed{
   \sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
   \leq
   \sum_n\left|\sum_{j=0}^{q-1}n_jA(n+j)\right|^2.
   }
   \tag{2.4}
   \]

   The contracted selector has \(q\) shifts, total weight \(\sum_jn_j=H\), and squared weight mass \(\sum_jn_j^2=\mu(H,q)\). This is precisely where contraction is paid for.

5. **Capacity consequence.** Put

   \[
   \rho(H,q):=\frac{\mu(H,q)}H\geq\frac Hq.
   \tag{2.5}
   \]

   In zeroth-coefficient bookkeeping normalized by the accepted diagonal \(C_HH\sum_{p,k}|b_{p,k}|^2\), the exact surviving factor is \(\rho(H,q)\), not \(1\). With

   \[
   \Gamma_{\rm before}=\min(H,Q),\qquad \Gamma_{\rm claimed}=1,
   \tag{2.6}
   \]

   a contraction chosen to remove \(\Gamma_{\rm before}\) merely by reducing the number of lags must have \(q\leq H/\Gamma_{\rm before}\). It then satisfies

   \[
   \boxed{
   \Gamma_{\rm zeroth\ survivor}=\rho(H,q)
   \geq \frac Hq\geq\Gamma_{\rm before}.
   }
   \tag{2.7}
   \]

   This is a capacity statement about the proposed majorant mechanism, not a lower bound for the literal \(\mathcal E_\chi\).

## 3. Proof and derivation

### 3.1 Exact block square and Parseval

By the definitions and zero extension,

\[
\sum_p\chi_4(p)B_{p,n}
=\sum_{a=0}^{H-1}\sum_p\chi_4(p)b_{p,n+a}
=\sum_{a=0}^{H-1}A(n+a).
\]

If \(S_HA(n)=\sum_{a=0}^{H-1}A(n+a)\), then

\[
\widehat {S_HA}(\alpha)=D_H(-\alpha)\widehat A(\alpha).
\]

Parseval therefore proves (2.1). Equivalently, with

\[
C_h(A):=\sum_kA(k)\overline{A(k+h)},
\]

one has the exact lag expansion

\[
\sum_n|S_HA(n)|^2
=\sum_{|h|<H}(H-|h|)C_h(A).
\tag{3.1}
\]

This also rederives

\[
F_H(\alpha)=|D_H(\alpha)|^2
=\sum_{|h|<H}(H-|h|)e(h\alpha),
\]

so \(F_H\) is already nonnegative and band-limited of exact degree \(H-1\), with \(F_H(0)=H^2\) and zeroth coefficient \(H\).

### 3.2 Which order is lawful

Let \(U=T-F_H\). If \(U(\alpha)\geq0\) pointwise, then

\[
\int_0^1U(\alpha)|\widehat A(\alpha)|^2\,d\alpha\geq0,
\]

which is exactly (2.2). Conversely, suppose this quadratic-form inequality holds for every finite \(A\). For any \(\alpha_0\), take

\[
A_N(k)=N^{-1/2}e(-k\alpha_0)\mathbf 1_{0\leq k<N}.
\]

Then \(|\widehat A_N|^2\) is the normalized Fejer approximate identity centered at \(\alpha_0\). Continuity of \(U\) gives

\[
0\leq\lim_{N\to\infty}\int_0^1U|\widehat A_N|^2=U(\alpha_0).
\]

Hence universal positive-semidefinite domination and pointwise multiplier domination are equivalent.

By contrast, coefficientwise domination is insufficient. For \(c>0\), the increment

\[
U(\alpha)=2c\cos(2\pi\alpha)
\]

has nonnegative added Fourier coefficients at \(h=\pm1\), but \(U(1/2)=-2c\). Taking \(A(0)=1,A(1)=-1\) gives

\[
\int_0^1U|\widehat A|^2=-2c<0.
\]

Thus neither coefficientwise majorization nor a scalar-selector inequality licenses domination of the complex block square. The multiplier or its Gram matrix must be ordered.

### 3.3 Exact lower bound for the zeroth coefficient

Let \(T(\alpha)=\sum_{|s|<q}t_se(s\alpha)\) have degree at most \(q-1\). Averaging over the \(q\)-th roots of unity gives the exact quadrature identity

\[
t_0=\frac1q\sum_{j=0}^{q-1}T(j/q).
\tag{3.2}
\]

If \(T\geq F_H\), then

\[
t_0\geq\frac1q\sum_{j=0}^{q-1}|D_H(j/q)|^2.
\tag{3.3}
\]

Group the \(H=mq+r\) terms of \(D_H\) by their residue classes modulo \(q\). At a \(q\)-th root,

\[
D_H(j/q)=\sum_{a=0}^{q-1}n_ae(aj/q),
\]

with \(n_a\) as in (2.3). Finite discrete Parseval now yields

\[
\frac1q\sum_{j=0}^{q-1}|D_H(j/q)|^2
=\sum_{a=0}^{q-1}n_a^2
=r(m+1)^2+(q-r)m^2
=\mu(H,q).
\tag{3.4}
\]

This proves the sharp candidate lower bound. It may also be written as the exact aliasing sum

\[
\mu(H,q)=H+2\sum_{1\leq s\leq\lfloor(H-1)/q\rfloor}(H-sq).
\tag{3.5}
\]

The usual Fejer--Riesz uncertainty estimate is the slightly weaker immediate consequence. Since \(T\geq F_H\geq0\), write

\[
T(\alpha)=\left|\sum_{j=0}^{q-1}c_je(j\alpha)\right|^2.
\]

Then \(t_0=\sum_j|c_j|^2\), while

\[
H^2=F_H(0)\leq T(0)=\left|\sum_jc_j\right|^2\leq q t_0.
\tag{3.6}
\]

Thus \(t_0\geq H^2/q\). Formula (3.4) supplies the exact remainder \(r(1-r/q)\).

### 3.4 Construction and proof of the sharp majorant

Set

\[
P_{H,q}(\alpha)=mD_q(\alpha)+D_r(\alpha),
\qquad T^*_{H,q}=|P_{H,q}|^2.
\]

This is a nonnegative real trigonometric polynomial of degree at most \(q-1\), and its zeroth coefficient is the right side of (3.4). It remains to prove \(T^*_{H,q}\geq F_H\).

Put \(z=e(\alpha)\), \(w=z^q\), \(v=z^r\),

\[
A_0=1-w,\qquad B_0=1-v,\qquad
G=\sum_{a=0}^{m-1}w^a.
\]

For \(z\neq1\),

\[
(1-z)P_{H,q}=mA_0+B_0,
\]

whereas

\[
(1-z)D_H=1-w^mv=A_0G+w^mB_0.
\]

Define

\[
S_m(\bar w)=\sum_{j=1}^m\sum_{a=0}^{j-1}\bar w^a
=\sum_{a=0}^{m-1}(m-a)\bar w^a.
\]

Since

\[
m-G\bar w^m
=\sum_{j=1}^m(1-\bar w^j)
=(1-\bar w)S_m(\bar w),
\]

direct expansion gives

\[
\begin{aligned}
|1-z|^2(T^*_{H,q}-F_H)
&=|mA_0+B_0|^2-|A_0G+w^mB_0|^2\\
&=|A_0|^2\left(m(m+1)-2\operatorname{Re}\{\bar vS_m(\bar w)\}\right).
\end{aligned}
\tag{3.7}
\]

Every monomial in \(\bar vS_m(\bar w)\) has modulus one, and the sum of its nonnegative multiplicities is

\[
\sum_{a=0}^{m-1}(m-a)=\frac{m(m+1)}2.
\]

Therefore

\[
2\operatorname{Re}\{\bar vS_m(\bar w)\}\leq m(m+1),
\]

so (3.7) is nonnegative. At \(z=1\), both \(P_{H,q}(0)\) and \(D_H(0)\) equal \(H\), and the claim follows by continuity. This proves pointwise domination. Combined with (3.4), it proves exact optimality and (2.4).

### 3.5 Exact \(L^1\) excess and capacity

For every pointwise majorant, \(T-F_H\geq0\); hence

\[
\|T-F_H\|_1=\int_0^1(T-F_H)=t_0-H.
\]

The sharp minimum is consequently (1.3). The contracted weights in (2.3) have fixed \(\ell^1\)-mass \(H\), but uncertainty forces their \(\ell^2\)-mass squared to be

\[
\mu(H,q)\geq H^2/q.
\]

On a one-row impulse, the original zero-lag contribution is \(C_HH\sum_k|b_k|^2\), while the majorant zero-lag contribution is \(C_H\mu(H,q)\sum_k|b_k|^2\). Their exact ratio is \(\rho(H,q)\). Thus any proof that budgets the new zeroth term against the accepted diagonal \(\mathcal D_0\) inherits at least the factor \(H/q\).

More generally, a hoped-for lag-count gain \(H/q\) and the forced zeroth-mass loss \(t_0/H\geq H/q\) are the same scale. In particular, choosing \(q\leq H/\min(H,Q)\) in an attempt to change

\[
\Gamma_{\rm before}=\min(H,Q)
\]

to

\[
\Gamma_{\rm claimed}=1
\]

leaves the factor in (2.7). No \(X^\varepsilon\) allowance absorbs this factor under a fixed-power contraction.

### 3.6 Complex coefficients and the actual character

For a general real nonnegative \(T=\sum_{|s|<q}t_se(s\alpha)\), one has \(t_{-s}=\overline{t_s}\) and

\[
\int_0^1T|\widehat A|^2
=t_0\sum_k|A(k)|^2
+2\operatorname{Re}\sum_{s=1}^{q-1}t_sC_s(A).
\tag{3.8}
\]

Positivity of \(T\) gives only

\[
|t_s|=\left|\int_0^1T(\alpha)e(-s\alpha)\,d\alpha\right|\leq t_0;
\tag{3.9}
\]

it does not give a termwise sign for the complex quantities \(t_sC_s(A)\). Phase-adapted two-point sequences can make their real parts positive or negative. Fejer--Riesz factorization rewrites (3.8) as one weighted complex block square, not as a sum of independently positive lag contributions.

Keeping the actual character before every modulus gives

\[
\begin{aligned}
C_s(A)
&=\sum_k\left(\sum_p\chi_4(p)b_{p,k}\right)
 \overline{\left(\sum_{p'}\chi_4(p')b_{p',k+s}\right)}\\
&=\sum_{p,p'}\chi_4(p)\chi_4(p')
  \sum_k b_{p,k}\overline{b_{p',k+s}}.
\end{aligned}
\tag{3.10}
\]

The \(p\neq p'\) terms are genuine complex cross terms. Neither coefficientwise comparison nor the separate positive-row estimate (134.B5) controls them without an additional lemma. Applying a rowwise modulus to (3.10) erases exactly the \(\chi_4\)-structure that a direct full-character argument was required to preserve.

## 4. First doubtful or unproved step

There is no unproved step in the finite extremal theorem (1.1)--(1.3), the exact Parseval reduction, or the order-type assertions above.

The first unproved step toward (134.B3) is a uniform estimate for the literal signed correlations (3.10), or for the complete weighted block on the right of (2.4), strong enough to offset

\[
\rho(H,q)=\mu(H,q)/H\geq H/q.
\]

In particular, one may not replace the full-character zero-lag norm

\[
\sum_k\left|\sum_p\chi_4(p)b_{p,k}\right|^2
\]

by \(\sum_{p,k}|b_{p,k}|^2\) without proving control of all cross-\(p\) terms. Nor may one assume the off-diagonal terms in (3.8) are nonnegative or discard them individually. The supplied statement contains no character-correlation estimate that closes this gap. Therefore the sharp majorant is a rigorous reduction and a rigorous capacity no-go, but not a proof of the target.

## 5. Control tests and outcomes

| Required control | Exact input/calculation | Outcome and implication |
|---|---|---|
| `literal_Echi_block_square_and_parseval` | Form \(A=\sum_p\chi_4(p)b_p\) first, use zero extension, and Fourier transform \(S_HA\). | Pass: (2.1) and (3.1) are exact, including entries and exits. |
| `majorant_order_relation` | Compare \(U=T-F_H\) against every density \(|\widehat A|^2\), then use a Fejer approximate identity for the converse. | Pass: universal quadratic-form order is exactly pointwise multiplier order. Coefficientwise order fails by the explicit \(2c\cos(2\pi\alpha)\) test. |
| `Fejer_already_bandlimited` | Expand \(F_H=\sum_{|h|<H}(H-|h|)e(h\alpha)\). | Pass: its degree is already \(H-1\); \(q=H\) gives \(T^*=F_H\), \(t_0=H\), and no contraction. |
| `zeroth_coefficient_uncertainty_bound` | Use \(q\)-point quadrature and discrete Parseval on the residue counts \(n_j\). | Pass, sharp: \(t_0\geq\mu(H,q)=H^2/q+r(1-r/q)\), attained by (1.2). |
| `bandwidth_and_L1_excess_capacity` | Compute \(\int(T-F_H)=t_0-H\) and the contracted selector's squared weight mass. | Proposed target-safe fixed-power contraction fails: the exact minimum excess is (1.3), and \(t_0/H\geq H/q\). |
| `complex_cross_term_domination` | Expand (3.8); choose two-point complex \(A\) with phase adapted to \(t_s\). | Pass as a falsification: the cross term can have either sign. Only the whole PSD form is ordered. |
| `actual_chi4_before_modulus` | Expand \(C_s(A)\) exactly as (3.10). | Pass: true \(\chi_4\) stays inside the \(p,p'\) sum. A rowwise modulus would be an additional, lossy step. |
| `opposite_character_and_single_row_controls` | One row gives \(A=\pm b\). Two identical rows with characters \(+1,-1\) give \(A=0\). Taking the second row to be the negative of the first gives \(A=2b\). | A single row has no character saving; opposite characters can cancel exactly or, with phase adaptation, reinforce exactly. Thus signs alone supply no universal estimate. |
| `Gamma_before_claimed_survivor` | Set \(\gamma=\Gamma_{\rm before}=\min(H,Q)\) and take \(q\leq H/\gamma\), the bandwidth needed for a lag-count-only removal. | Fail for \(\Gamma_{\rm claimed}=1\): the exact zeroth survivor satisfies \(\rho(H,q)\geq\gamma\), as in (2.7). |
| `flat_smooth_owner_and_downstream_scope` | Apply the algebra only to the literal finite \(b_{p,k}\) array after its mandated zero extension. | Pass: no profile, support, endpoint, or sign was altered. No hard, sharp, clipped, starred, arithmetic-owner, nonflat, transition, downstream-M9, or exponent conclusion is asserted. |

Additional analytic controls sharpen the interpretation:

- For a one-row coherent test \(b(k)=\mathbf 1_{0\leq k<N}\) with \(N\gg H\), the original block form has leading term \(NH^2\), and the folded block also has leading term \(N(\sum_jn_j)^2=NH^2\). Contraction does not reduce the zero-frequency coherent response.
- For a one-row impulse, all nonzero-lag correlations vanish and the majorized form exposes the exact ratio \(\rho(H,q)\).
- Replacing \(\chi_4\) by absolute values turns two identical opposite-character rows from zero into \(2b\). Independent random signs cancel cross rows only in expectation, not uniformly. Phase-adapted complex rows can align all \(\chi_4(p)b_{p,k}\). These adversarial arrays test a universal inference; they are not counterexamples to the fixed literal array (134.B1).

## 6. Dependencies and exact artifacts used

Only the following statement-only or protocol artifacts were used:

- `protocol.md`
- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md`
- `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/briefs/blind_bandlimited_quadratic_majorant_feasibility.md`

No graph, proof draft, strategy file, prior-round artifact, sibling report, nonblind Round-134 artifact, web source, or numerical experiment was consulted. The argument is 100% analytic/algebraic.

## 7. Recommended state effect

**Promote as candidate finite evidence** the sharp extremal theorem (1.1)--(1.3), the lawful physical reduction (2.4), and the exact equivalence between pointwise multiplier order and universal quadratic-form order.

**Reject** the proposed inference that a one-sided band-limited majorant can simultaneously provide a fixed-power bandwidth contraction and a target-safe zeroth coefficient. Record the exact obstruction

\[
t_0^{\min}(H,\Delta)
=\mu(H,\Delta+1)
\geq \frac{H^2}{\Delta+1}.
\]

**Retain (134.B3) as open.** A future route must add a genuinely literal \(\chi_4\)-sensitive estimate for (3.10) or for the weighted block in (2.4); the majorant construction by itself supplies no such cancellation. No shared proof state should be changed from this report alone.

# Round 89 hostile and source audit

## 1. Result

**Verdict: reject the literal period-depth-to-degree mechanism for the complete bad-prime/nonunit-$K$/full-$2$-adic residual; retain the actual-symbol target as open.** Exact local period classification is useful routing information, but at the bad primes it does not by itself force a target-safe directed graph.

Three smaller conclusions are certifiable.

1. Empty and one-residue masks, every first-layer period by $q/p$, and every first-layer affine cancellation are classified exactly by the complete four-pole mask and $\Phi'$. Genuine accidental branches occur at $p=3,5$; coefficientwise vanishing of the numerator of $\Phi$ is not a valid substitute.
2. If $\kappa=v_p(K_q)<\nu$, then the complete masked weight modulo $p^\nu$ is exactly the pullback of a unit-$K$ masked weight modulo $p^{\nu-\kappa}$. Fourier and completed-trace descent contribute $p^\kappa$ and $p^{2\kappa}$, respectively. This conductor drop is independent of the partner labels and gives no directed-degree saving.
3. The smallest explicit strict-cross local survivor occurs at $q=8$. With
   $$
   A=B_2=V=2,
   $$
   the mask is the odd class,
   $$
   \Phi(x)=\frac{8}{x(x-2)(x-4)}\equiv0\pmod 8,
   $$
   and, for every $K_q$, $w_8$ has exact period $2$, hence depth $j_2=2$. Moreover
   $$
   |\mathfrak T_8(4)|=32=8^2/2.
   $$
   The two physical pairs are neither equal nor reversals modulo $8$. After CRT with generic odd cofactor labels, this local fibre has $R_*>\rho_*$, $\mathfrak a=1$, nonzero admissible Fourier modes, and the complete symbol (89.8)--(89.9). It is an obstruction to coefficientwise cancellation, not a lower bound for the signed aggregate.

More strongly, fix a source with $A\equiv2\pmod8$. All nonempty local partners have $B_2,V$ even, and every such $q=8$ weight has exact period $2$. Excluding the equal and reversed partners leaves ten of the twelve off-diagonal even $(B_2,V)$ patterns. With generic odd CRT cofactors this gives both directed degrees $\gg X^{-\varepsilon}M^2$. At the upper endpoint,
$$
\rho_*^2\asymp J^{2/15},\qquad M^2\asymp J^{3/10},
$$
so the target degree is missed by $J^{1/6-o(1)}$. Exact period depth, even with the full $2$-part retained, cannot certify this whole fibre through (89.13).

No requested complete-fibre package is obtained by declaring empty masks periodic, using sparse Fourier support, or arbitrarily thinning the graph to a matching. The first is the zero tensor, the second is an exact transform self-return, and although a matching is trivially low-degree, it is not a classification of a complete fibre.

## 2. Exact statement and hypotheses

Retain exactly the frozen hypotheses and owners in the derivation packet:
$$
J=X^{1/2},\quad Q=J^{2/5},\quad T=J^{3/5},\quad B=C/T,
\quad J^{13/18}<C\le J^{3/4},\quad M\asymp B,
$$
the deep signed range $D_1<|d|<\Delta_b-E_*$, normalized rows (89.2), the centered kernel (89.4), and only edges satisfying
$$
R_*>\rho_*,\qquad \mathfrak a<M^2/\rho_*^2.
$$
Round-87 same-group terms, Round-88 coarse shells, the Round-88 good-prime package, and the unique global integer shift $u=0$ are excluded.

Let
$$
S_p(A,B_2,V)=\{0,A,V,V+B_2\}\subset\mathbb F_p,
\qquad U_p=\mathbb F_p\setminus S_p.
$$
Then $\Omega_q$ is the inverse image of $U_p$. It is empty exactly when $S_p=\mathbb F_p$, and it is a one-residue mask exactly when $|S_p|=p-1$. Consequently:

- for $p=2$, the mask is nonempty and one-residue exactly when $A,B_2,V$ are all even; otherwise it is empty;
- for $p=3$, it is empty when the poles occupy all three classes, one-residue when they occupy two classes, and two-residue only when all poles coincide;
- for $p=5$, it is never empty and is one-residue exactly when the four poles are distinct;
- for $p=7$, it is neither empty nor one-residue.

For $\nu\ge2$, put $h=q/p$. On a nonempty mask,
$$
\Phi(x+h)-\Phi(x)\equiv h\Phi'(x)\pmod q,
$$
where
$$
\Phi'(x)=-x^{-2}+(x-A)^{-2}+(x-V)^{-2}
             -(x-V-B_2)^{-2}.
$$
Thus, when $p\nmid K_q$, $w_q$ has period $q/p$ if and only if $\Phi'(r)=0$ for every $r\in U_p$. The affine weight $e_q(ux)w_q(x)$ has that period if and only if
$$
u+K_q\Phi'(r)=0\pmod p\qquad(r\in U_p).
$$
If $p\mid K_q$, the reciprocal period $q/p$ is automatic. These are complete first-layer statements, including pole collisions.

For unit $K_q$, direct finite-field substitution gives the following exact list. Put
$$
\mathcal S_0(p)=\{A=B_2=0\}\cup\{V=0,\ B_2=A\}.
$$

| prime | reciprocal $q/p$-periods | additional affine-only $q/p$-periods |
|---|---|---|
| $2$ | the unique nonempty residue triple $(0,0,0)$ | none |
| $3$ | every nonempty triple (fifteen of twenty-seven) | none |
| $5$ | $\mathcal S_0(5)$, plus $A=a\ne0$ and $(B_2,V)=a(2,2),a(3,4),a(4,3),a(4,4)$ | $A=a\ne0$ and $(B_2,V)=a(1,2),a(1,3),a(1,1),a(1,4)$; choose $u=-K_q\Phi'$ on the allowed class(es) |
| $7$ | exactly $\mathcal S_0(7)$ | none |

The $p=5$ reciprocal list has nine structural and sixteen one-residue accidental triples. The sixteen affine-only triples consist of eight one-residue and eight two-residue masks. Affine cancellation is therefore strictly larger than reciprocal period classification and must remain a separate owner.

For nonunit $K_q$, let $0\le\kappa<\nu$ and write
$$
K_q=p^\kappa K_0,\qquad p\nmid K_0,\qquad q'=p^{\nu-\kappa}.
$$
Then exactly
$$
w_q(x)=w_{q'}^{(K_0)}(x\bmod q').
$$
If the lower weight has exact period $p^r$, or lower depth $j'=\nu-\kappa-r$, the upper weight has the same numerical period and depth
$$
j=\kappa+j'.
$$
Also
$$
\widehat w_q(p^\kappa u')=p^\kappa\widehat w_{q'}(u'),
\qquad
\mathfrak T_q(p^\kappa u')=p^{2\kappa}\mathfrak T_{q'}(u').
$$
If $q\mid K_q$ and the mask is nonempty, the phase is constant and the mask has exact period $p$, hence depth $\nu-1$. None of these facts imposes a new congruence on $B_2,V$.

## 3. Proof or derivation

The mask assertions follow because all four unit conditions depend only on $x\bmod p$. There are at most four forbidden classes. This gives all empty and one-residue alternatives and shows why an empty mask is the zero function rather than a large-depth fibre.

For the first-layer identity, $h^2\equiv0\pmod q$ and, for every unit $z$,
$$
(z+h)^{-1}\equiv z^{-1}-hz^{-2}\pmod q.
$$
The mask is fixed by $x\mapsto x+h$, so division by $h=q/p$ proves the reciprocal and affine criteria in Section 2. At $p=2,3$, every unit square is $1$, hence $\Phi'=-1+1+1-1=0$ on every nonempty mask. At $p=5,7$, scale by $A$ when $A\ne0$, evaluate the finitely many normalized pairs $(B_2/A,V/A)$, and handle $A=0$ separately. The displayed lists are the complete substitution table. They account for every pole collision; no root-count or numerator-only inference is used.

The nonunit statement is exact reduction of the additive character:
$$
e_{p^\nu}(p^\kappa K_0\Phi)=e_{p^{\nu-\kappa}}(K_0\Phi).
$$
The mask already factors through reduction modulo $p$, hence through $q'$. Summing over the $p^\kappa$ lifts of each class gives the Fourier factor $p^\kappa$. Since the completed trace has outer modulus factor $q$, while the descended trace has outer factor $q'$, their ratio is $p^{2\kappa}$. More generally, if the exact period is $q/p^j$, then
$$
\widehat w_q(p^ju')=p^j\widehat w_{q/p^j}(u'),
\qquad
\mathfrak T_q(p^ju')=p^{2j}\mathfrak T_{q/p^j}(u').
$$
This proves the compulsory $p^{2j}$ descent and also proves that frequency sparsity alone gives no Fejer-mass gain.

For the explicit $2$-adic survivor, every odd residue satisfies $z^{-1}\equiv z\pmod8$. Thus for arbitrary even $A,B_2,V$,
$$
\Phi(x)\equiv x-(x-A)-(x-V)+(x-V-B_2)
         \equiv A-B_2\pmod8
$$
on the odd mask. Therefore $w_8$ is a nonzero constant on the odd class and zero on the even class, so its exact period is $2$. For $A=B_2=V=2$, direct combination of the three distinct reciprocal terms gives
$$
\Phi(x)=x^{-1}-2(x-2)^{-1}+(x-4)^{-1}
      =\frac{8}{x(x-2)(x-4)}.
$$
At frequency $u=4$, all four odd residues contribute the same sign, whence
$$
\left|\widehat w_8(4)\right|=4,\qquad
|\mathfrak T_8(4)|=8\cdot4=32.
$$
This is also $2^{2j}=2^4$ times the completed modulus-$2$ trace.

At $q=4$, nonempty off-diagonal pairs force $A=B_2=2$; $V=0$ gives the same pair and $V=2$ its reversal. Thus $q=8$, $A=B_2=V=2$, is the first local $2$-power example not already equal or reversed at full modulus. Its direct coordinate differences are both $2$, while reflected coincidence occurs at modulus at most $4$. After tensoring with odd cofactor labels chosen not to coalesce, $R_*\ge M/4$.

For the degree obstruction, fix a source whose $8$-part has $A=2$. There are twelve local choices with $B_2\in\{2,4,6\}$ and $V\in\{0,2,4,6\}$; removing the equal and reversed choices leaves ten strict-cross patterns, all of exact depth $j_2=2$. Choose odd CRT cofactor labels away from equality, reversal, and the good-prime period congruences. These exclusions remove only an $X^{o(1)}$ proportion, so a fixed source has $\gg X^{-\varepsilon}M^2$ partners. The reversal involution
$$
(A,B_2,V)\longmapsto(B_2,A,-V)
$$
changes $\Phi$ to $-\Phi$ after translation and preserves reciprocal period depth. Symmetrizing the edge set therefore gives the same lower capacity in both directions. Taking $M\asymp B=J^{3/20}$ at $C=J^{3/4}$ gives
$$
\rho_*\asymp J^{1/15},\qquad
\frac{M^2}{\rho_*^2}\asymp J^{1/6}.
$$
Thus no bound $\Delta\le\rho_*^2$ follows from this exact bad-prime depth. This disproves the proposed graph mechanism only; it does not disprove a future signed estimate exploiting (89.8)--(89.9).

As an independent odd-prime check, $q=9$, $(A,B_2,V)=(1,2,1)$, and $3\nmid K_q$ give the one-residue mask $x\equiv2\pmod3$, exact period $3$, and
$$
|\mathfrak T_9(3)|=27=9^2/3.
$$
Indeed $\Phi$ is constant modulo $9$ at $x=2,5,8$. This confirms that the obstruction is not an artifact of replacing the full $2$-part by parity.

## 4. First doubtful or unproved step

The first unproved step is any estimate of the high-degree bad-prime fibre against the actual stationary symbol
$$
\frac1{M^5}\sum_{n,m}
\Omega_{b,d,u}(n,m)e_M(dV+nA-mB_2)
\mathfrak T_M(u,A,B_2,V)
$$
after the exact prior owners are removed. Neither the first-layer table, the full nonunit pullback, nor a complete future classification of deeper $2$-adic periods supplies cancellation in the coupled $(b,d,u,n,m,A,B_2,V)$ sum. On the explicit $q=8$ branch the local trace is already of size $q^2/2$, and the directed graph has full quadratic capacity.

There is no proved lower bound for the complete signed aggregate: the fourfold stationary coefficient can still cancel across $n,m,d,u,b$. Conversely, taking absolute values or applying a one-variable complete-sum theorem discards exactly that remaining possible cancellation. A valid next step must be a joint actual-symbol estimate, or a new structural partition with independently proved low in- and out-degree; exact transform support alone is not such a step.

The complete deeper classification for arbitrary unit-$K$ weights modulo $2^\nu$ is also unproved. It cannot be replaced by parity: for example, at $q=64$, $K=1$, $A=B_2=2$, the choices $V=2,4,8$ have distinct exact periods $8,4,2$. This finite diagnostic is not used to certify an asymptotic statement; the symbolic $q=8$ obstruction already proves the no-go.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| External normalization | **Pass.** The argument uses normalized physical rows and (89.13); no extra $M^{-2}$ is inserted. Completion remains at $M^{-5}$ with the outer factor inside $\mathfrak T_M$. |
| Global diagonal one-count | **Pass.** $\mathcal K_D^\circ$ removes only the integer $u=0$ once. It does not remove $u=kM\ne0$. |
| Prior-package ownership | **Pass.** Equal and full-reversal cases are excluded. CRT cofactor labels are chosen so $R_*>\rho_*$, and no good-prime depth contributes to $\mathfrak a$. |
| Complete small-prime mask | **Pass.** Empty and one-residue masks are classified by the full pole set $\{0,A,V,V+B_2\}$; pole collisions are retained. |
| Nonunit-$K$ conductor | **Pass as an identity; fail as a saving.** The exact pullback and $p^{2\kappa}$ descent hold, but $\kappa$ imposes no partner-label congruence. |
| Full $2$-adic depth | **Fail for the proposed general classification/bound.** The complete factor $q=8$, not a squarefree surrogate, already has a high-degree exact depth-$2$ fibre. Arbitrary deeper $2^\nu$ classification remains open. |
| $p^{2j}$ descent | **Pass.** The uncompleted transform descends by $p^j$, and the change of outer modulus supplies the second $p^j$. The $q=8$ trace realizes the factor $2^4$. |
| Directed in/out degree | **Fail at target scale.** Ten strict local $8$-patterns and generic CRT lifts give $\gg X^{-\varepsilon}M^2$ capacity. Reversal preserves depth and supplies the transposed obstruction. |
| Actual fourfold stationary symbol | **Pass as preservation only.** No local trace size is promoted to an aggregate lower bound; (89.8)--(89.9) remains the first open operator. |
| Negative and modulus-multiple differences | **Pass.** Both signs are retained. Since $D\gg M$, nonzero representatives and $u=kM\ne0$ occur inside the centered Fejer range and are not renamed the global diagonal. |
| Ramanujan cross and square terms | **Pass.** The physical-row graph estimate keeps the four-Kloosterman term, both cross terms, and the Ramanujan square under their existing single ownership. |
| Deep support and errors | **Pass.** All claims are after $\Pi_{b,D}$, with all four $I_b$ factors in $\Omega_{b,d,u}$. No collar, transition, axis, wrong-sign, or stationary-error owner is reopened. |
| Integer/perfect-power resonance | **Pass.** The obstructions are exact prime-power identities, including constant local phases; no generic nonintegrality or non-perfect-power hypothesis is used. |
| Complete-transform self-return | **Pass as a no-go.** Sparse support is accompanied by exact $p^{2j}$ enlargement, so completion plus inversion gives no independent norm decrease. |
| Source-hypothesis map | **Pass.** No external theorem is used. The closest audited source concerns one local prime-power sum, not the directed physical graph or the actual $b$-varying symbol. |
| Downstream scope | **Pass.** No claim is made beyond the frozen first conductor band/component, and no M9-M1, M9, endpoint, cone-edge, or exponent conclusion is asserted. |

The only numerical work was a bounded finite-residue diagnostic at $p\le7$ and $q\le64$. Every statement used in the no-go and every recommended state effect has the symbolic proof in Sections 2--3.

## 6. Dependencies and exact artifacts used

The exact artifacts used were:

1. protocol.md.
2. state/proof_obligations.yml.
3. state/active_campaign.yml.
4. rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/plan.json.
5. rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/briefs/bad_prime_hostile_source_audit.md.
6. rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/derivation_packet.md.
7. rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md.
8. rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/cross_group_hostile_source_audit.md.
9. rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reviews/conductor_round88_adjudication.md.

No sibling Round-89 report was read.

No new literature search was triggered because no external theorem is invoked in the algebraic classification or counterexample. The selected Round-88 source audit already maps the closest current primary result, Cochrane--Granville, *Mixed character sums modulo prime powers*, arXiv:2604.02614v1, including its separate $2$-adic theorem and conductor-lowering branches. Its literal object is one local mixed character sum; it supplies neither a bound for the directed physical-edge graph nor cancellation against (89.8)--(89.9), and its constant/degenerate branches do not contradict the $q=8$ or $q=9$ traces. The other already-audited prime-field, special-prime-power, squarefree, and fixed-modulus bilinear results likewise fail the full-prime-power, four-mask, varying-$b$, actual-symbol hypotheses. Importing any of them here would be nonliteral.

## 7. Recommended state effect

**Revise** any Round-89 claim that complete small-prime, nonunit-$K$, or full $2$-adic period depth automatically yields a bad-prime conductor controlling both directed degrees.

- **Promote only as exact local routing lemmas** the mask classification, first-layer reciprocal/affine criterion, displayed $p\le7$ table, and nonunit pullback identity. The $p^{2j}$ descent is already owned by Round 88 and should not be duplicated.
- **Promote as a hostile control** the exact $q=8$, $A=B_2=V=2$ trace $|\mathfrak T_8(4)|=32$, together with the ten-pattern directed-degree obstruction. Retain the $q=9$ trace $27$ as an independent odd-prime check.
- **Reject** empty-mask depth, affine/reciprocal conflation, a $p^j$ completed descent, sparse-support Fejer saving, one-direction-only degree counts, and coefficientwise square-root cancellation.
- **Retain open** the complete deeper unit-$K$ $2$-adic classification and the strict residual actual-symbol estimate. The smallest certified survivor is the single complete $q=8$ local factor above, tensored with strict generic CRT cofactors; the first analytically meaningful unresolved package is its high-degree exact-depth graph, not an arbitrarily selected matching.
- Make **no change** to Round-87 same-group ownership, either Round-88 deletion, the global $u=0$ owner, Ramanujan ownership, support/error owners, or any downstream theorem node.

## 1. Result: exact fibre reduction and a fixed-centre capacity no-go

The squarefree-kernel change of variables gives an exact, multiplicity-one formula, and it does discharge the large-square complement absolutely.  If (T_M=lceil M^{1/4}\rceil), then

\[
T_N=T_N^{\mathrm{small}}+O_{\varepsilon,V}(X^\varepsilon),
\]

where (T_N^{\mathrm{small}}) is the same signed scalar with every original condition retained and with

\[
m=s t^2,\qquad s\ \text{squarefree},\qquad 1\leq t<T_M,
\qquad s\geq A_M/t^2\gg M^{1/2}.
\]

Here \(\mathcal I_M=\mathbb N\cap[A_M,B_M)\) denotes the literal supplied half-open block, including a literal terminal endpoint when a block is truncated.  No enlargement of the small-(t) survivor is made in this identity.

This is a strict owner-complete reduction, but it is not a proof of the target estimate.  The first exact obstruction is capacity at (t=1): a fixed-(s) linear twist has only one term there, while the absolute block ledger for that layer is of size (M^{1/4+o(1)}).  The coefficient does not vanish algebraically: for every odd prime (p>4), (C(p)=\chi _4(p)).  Thus linearity of (e(t\sqrt{Ns})) in (t), by itself, supplies none of the (M^{1/4}) saving required on the (t=1) layer.  Bounded-(t) fibres have the same defect.  In addition, the large-(j) mask does not give a uniform Diophantine separation of \(\sqrt{Ns}\) from the integers; an exact exceptional family is exhibited below.  A target estimate therefore still requires a genuinely signed fixed-(N) estimate across squarefree (s), or an estimate for the exact arithmetic amplitudes coupling (s) and (t).

## 2. Exact statement and hypotheses

Let (e(z)=e^{2\pi i z}).  Write each supplied dyadic block exactly as

\[
\mathcal I_M=\mathbb N\cap[A_M,B_M),
\]

where the dyadic geometry gives (c_0M\leq A_M<B_M\leq c_1M) with fixed positive constants (in the standard convention (A_M=M,B_M=2M)); a terminal block uses its actual (B_M).  Let (s) always denote a positive squarefree integer.

For (m=s t^2), define the finite tuple set

\[
\begin{aligned}
\mathfrak F(s,t)=\{(g,s_h,s_r,u,v):{}&g\mid t,\quad g\ \text{odd},\quad
 s_hs_r=s,\quad uv=t/g,\\
&\gcd(s_hu,s_rv)=1,\quad s_rv\ \text{odd},\\
&s_rv^2>4s_hu^2\}.
\end{aligned}
\]

Then the exact cone coefficient is

\[
\boxed{
C(s t^2)=
\sum_{(g,s_h,s_r,u,v)\in\mathfrak F(s,t)}
\chi _4(g)\chi _4(s_r).}
\tag{2.1}
\]

For later use put

\[
\alpha_{s,t}=t\sqrt{Ns},\qquad
k_{s,t}=\left\lfloor\alpha_{s,t}+\frac12\right\rfloor,
\qquad
\theta_{s,t}=\alpha_{s,t}-k_{s,t}\in[-1/2,1/2).
\]

The rounding tie is assigned upward, hence would give \(\theta=-1/2\); in the present problem a nonintegral half-integer tie is impossible because \(\alpha_{s,t}^2=Nst^2\in\mathbb Z\).  Exactly,

\[
j_{st^2}=k_{s,t}^2-Nst^2
=-\theta_{s,t}(2\alpha_{s,t}-\theta_{s,t}),
\tag{2.2}
\]

so \(\operatorname{sgn}j=-\operatorname{sgn}\theta\) off resonance and

\[
|j_{st^2}|>M^{3/4}
\iff
|\theta_{s,t}|(2t\sqrt{Ns}-\theta_{s,t})>M^{3/4}.
\tag{2.3}
\]

Define the exact weight, with no endpoint, profile, or mask removed, by

\[
\mathcal W_{M,N}(s,t)=
\mathbf 1_{[A_M,B_M)}(st^2)
V_{\rm low}\!\left(\frac{R^2st^2}{N}\right)
\mathbf 1_{\{|\theta_{s,t}|(2t\sqrt{Ns}-\theta_{s,t})>M^{3/4}\}}.
\tag{2.4}
\]

Since (e(\alpha_{s,t})=e(\theta_{s,t})), the literal positive complex direction is

\[
\boxed{
T_N=\sum_M\sum_{t\geq1}\sum_{\substack{s\geq1\\s\ {\rm squarefree}}}
s^{-3/4}t^{-3/2}\mathcal W_{M,N}(s,t)
\left(\sum_{\mathfrak F(s,t)}\chi _4(g)\chi _4(s_r)\right)
e(\theta_{s,t}).}
\tag{2.5}
\]

Split (2.5) exactly at (T_M=\lceil M^{1/4}\rceil).  The assertion proved here is

\[
\sum_M\sum_{t\geq T_M}\sum_{s\ {\rm squarefree}}(\text{summand in (2.5)})
\ll_{\varepsilon,V}X^\varepsilon,
\tag{2.6}
\]

uniformly for every real (X\geq2), and (T_N^{\rm small}) is (2.5) with (1\leq t<T_M).  If (q=\operatorname{sqf}(N)), then \(\theta_{s,t}=0\) holds exactly when (s=q); this entire exact-resonant fibre is absent from (2.5) because of the strict mask.

## 3. Proof and derivation

**Unique squarefree kernel.**  For every (m\geq1), set

\[
s=\prod_{p:\,v_p(m)\ {\rm odd}}p,
\qquad
t=\prod_p p^{\lfloor v_p(m)/2\rfloor}.
\]

Then (m=st^2), (s) is squarefree, and the valuations show uniqueness.  Thus the outer change from (m) to ((s,t)) is a bijection, not a multiplicity estimate.

**Coefficient algebra, including the common factor.**  Given one original factorization (hr=st^2), let (g=\gcd(h,r)), (h=gH), and (r=gK).  Since (g^2\mid st^2), valuation parity gives (g\mid t).  Also \(\gcd(H,K)=1\) and

\[
HK=s(t/g)^2.
\]

Every prime power on the right lies wholly in exactly one of (H,K).  Consequently there are unique (s_h,s_r,u,v) such that

\[
s_hs_r=s,\qquad uv=t/g,\qquad
H=s_hu^2,\qquad K=s_rv^2,
\qquad \gcd(s_hu,s_rv)=1.
\]

Conversely every such tuple reconstructs exactly one ordered pair

\[
h=gs_hu^2,\qquad r=gs_rv^2
\]

having gcd (g) and product (st^2).  The condition that (r) be odd is exactly that (g,s_r,v) all be odd.  In particular, if (2\mid s), its factor (2) is forced into (s_h); if (2^a\Vert t), then (g) and (v) are odd and the whole remaining (2^a) is forced into (u).  The strict cone becomes

\[
gs_rv^2>4gs_hu^2
\iff s_rv^2>4s_hu^2.
\]

Finally, complete multiplicativity of \(\chi _4\) on odd integers and \(\chi _4(v^2)=1\) give

\[
\chi _4(r)=\chi _4(gs_rv^2)=\chi _4(g)\chi _4(s_r).
\]

This proves (2.1), with multiplicity one and with no complete-divisor replacement.

**Phase, sign, tie, and exact resonance.**  Equations (2.2)--(2.3) follow by factoring

\[
k_{s,t}^2-\alpha_{s,t}^2
=(k_{s,t}-\alpha_{s,t})(k_{s,t}+\alpha_{s,t}).
\]

The second factor is positive.  A half-integer tie would imply that (4Nst^2) is the square of an odd integer, impossible because the left side is divisible by (4).  Write (N=qa^2) with (q) squarefree.  If \(\theta_{s,t}=0\), then (t\sqrt{Ns}\) is integral.  Since (Ns\) is an integer, this is equivalent to (Ns) being a square, hence to (qs) being a square.  The squarefree integers (q,s) must then be equal.  The converse is immediate.  Thus exact resonance is precisely (s=q), and (2.3) deletes it.

**Literal endpoint count and large-square tail.**  For fixed (t), before imposing squarefreeness, profile, or mask, the exact number of possible (s) in the half-open block is

\[
\#\{s\in\mathbb N:A_M\leq st^2<B_M\}
=\left\lceil\frac{B_M}{t^2}\right\rceil
-\left\lceil\frac{A_M}{t^2}\right\rceil
\leq \frac{B_M-A_M}{t^2}+1
\ll \frac{M}{t^2}+1.
\tag{3.1}
\]

The original definition immediately gives \(|C(m)|\leq\tau(m)\), because its summation set is a subset of the divisors of (m).  This unsigned envelope is used only on the complement being discharged.  For every \(\eta>0\), the elementary divisor bound is \(\tau(m)\ll_\eta m^\eta\).  Since (m\asymp M) on its literal dyadic block, (3.1) and \(\|V_{\rm low}\|_\infty<\infty\) give

\[
\begin{aligned}
|T_M^{\rm large}|
&\ll_{\eta,V}M^{-3/4+\eta}
\sum_{T_M\leq t<\sqrt{B_M}}
\left(\frac{M}{t^2}+1\right)\\
&\ll_{\eta,V}M^{-3/4+\eta}
\left(MT_M^{-1}+M^{1/2}\right)\\
&\ll_{\eta,V}M^\eta+M^{-1/4+\eta}.
\end{aligned}
\tag{3.2}
\]

Finitely many smallest blocks are absorbed into the constant.  The mask, squarefree restriction, exact radical, and profile were present in the sum to which the triangle inequality was applied; deleting their indicators in (3.2) can only increase that absolute majorant.

Let (U_V) be the upper endpoint of the positive part of the compact support of (V_{\rm low}).  Any nonzero profile term satisfies

\[
m\leq U_V\frac{N}{R^2}\leq U_VR^2,
\]

because (N\leq X=R^4).  Hence only dyadic (M\ll_VR^2=X^{1/2}) occur, including the terminal truncated block.  Summing (3.2) over those dyadic scales and choosing \(\eta\) smaller than the requested exponent proves (2.6).  This is the full (R,M,s,t) power ledger: the main term in (3.2) is exactly

\[
M^{-3/4}\,M\sum_{t\geq M^{1/4}}t^{-2}ll1
\]

per block, up to (M^{o(1)}).

**The surviving support and its capacity.**  If (t<T_M), then (t<M^{1/4}), apart from the equivalent exact integer convention at equality, and

\[
s\geq A_M/t^2\gg M^{1/2}.
\tag{3.3}
\]

For fixed (s), the exact unmasked block multiplicity is

\[
\#\{t\in\mathbb N:A_M\leq st^2<B_M\}
=\left\lceil\sqrt{B_M/s}\right\rceil
-\left\lceil\sqrt{A_M/s}\right\rceil,
\tag{3.4}
\]

before intersecting with (t<T_M), the profile, and the mask.  Thus no (m), (s), or (t) multiplicity is hidden.

Applying only the same divisor envelope to the small part yields

\[
|T_M^{\rm small}|
\ll_{\eta,V}M^{-3/4+\eta}
\sum_{1\leq t<T_M}\left(\frac{M}{t^2}+1\right)
\ll_{\eta,V}M^{1/4+\eta}.
\tag{3.5}
\]

At (M\asymp R^2), this is (R^{1/2+o(1)}=X^{1/8+o(1)}), not (X^\varepsilon).  The (t=1) part already has the (M^{-3/4}\cdot M=M^{1/4}) absolute capacity.  Moreover, when (s=p>4) is an odd prime, (2.1) has exactly the cone factorization (h=1,r=p), so

\[
C(p)=\chi _4(p)\neq0.
\tag{3.6}
\]

For a fixed (s) in the (t=1) layer, the proposed linear exponential sum in (t) has one term and therefore cannot produce cancellation.  Equation (3.5) is not asserted as a lower bound for the actual signed scalar; it is the rigorous capacity obstruction to obtaining the target merely from the fibre bijection and a fixed-(s) linear-twist estimate.

**Quadratic-irrational exceptional fibres.**  For (s\neq\operatorname{sqf}(N)), put (D=Ns).  Then (D) is nonsquare and every retained pair satisfies the exact generalized Pell relation

\[
k_{s,t}^2-Dt^2=j_{st^2},
\qquad
|\theta_{s,t}|=\frac{|j_{st^2}|}{k_{s,t}+t\sqrt D}.
\tag{3.7}
\]

Ordinary Pell solutions with (j=\pm1), and more generally all solutions with \(|j|\leq M^{3/4}), are removed by the mask.  This does not imply a useful uniform lower bound for the fractional phase.  Indeed, let (s>1) be squarefree, let (L\geq1) be an integer, and set

\[
N=sL^2+1,
\qquad
\sqrt{Ns}=sL+\rho,
\qquad
\rho=\frac{1}{\sqrt{L^2+1/s}+L}.
\tag{3.8}
\]

Whenever (t\rho<1/2), the nearest integer is (k_{s,t}=sLt), and exactly

\[
j_{st^2}=(sLt)^2-Nst^2=-st^2=-m.
\tag{3.9}
\]

If (m\in[A_M,B_M)) and (M>1), then \(|j|=m\geq A_M\asymp M>M^{3/4}) in the standard literal block normalization, so this near-integer phase survives the large-displacement mask.  Yet

\[
e(t\sqrt{Ns})=e(t\rho),\qquad \rho\sim(2L)^{-1},
\]

and a whole range (t=o(L)) has essentially no phase rotation.  Taking, for example, (L=s) leaves geometrically available small-(t) ranges with (t\ll s^{1/4}), hence (t\rho\to0).  The continued fraction of \(\sqrt{Ns}\) correspondingly has an unbounded next partial quotient of order (L).  This exact family falsifies both inferences “large (j) forces a uniformly separated linear frequency” and “the relevant quadratic irrationals have uniformly bounded continued-fraction quotients.”  It is an arithmetic control, not a claimed lower bound for (T_N), because the exact profile and signed coefficient still remain.

## 4. First doubtful or unproved step

There is no unproved step in the bijection, coefficient formula, resonance classification, or absolute large-(t) tail.  The first unproved step toward the target is precisely the signed estimate

\[
\sum_M\sum_{1\leq t<T_M}\sum_{\substack{s\ {\rm squarefree}\\A_M\leq st^2<B_M}}
s^{-3/4}t^{-3/2}
V_{\rm low}\!\left(\frac{R^2st^2}{N}\right)
C(st^2)
\mathbf 1_{\{|j_{st^2}|>M^{3/4}\}}
e(t\sqrt{Ns})
\ll_{\varepsilon,V}X^\varepsilon.
\tag{4.1}
\]

It cannot be justified by the usual unweighted geometric-sum bound.  The amplitude (C(st^2)), its strict cone, the profile, and the (j)-mask all vary with (t); no bounded-variation or controlled partial-sum hypothesis has been proved.  Even with a constant amplitude, (3.8)--(3.9) permits a frequency too close to an integer for a uniform (t)-saving, and at (t=1) there is no (t)-sum to estimate.  Consequently the next legitimate lemma would have to exploit signed cancellation across (s), or prove partial-sum cancellation for the exact tuple coefficient (2.1) with the mask present.  Replacing it by an arbitrary divisor-bounded sequence, pairing the conjugate direction, or averaging (N) would not prove (4.1).

## 5. Control tests and outcomes

- **`unique_squarefree_kernel_decomposition_and_block_endpoints` — PASS.**  Valuations give a bijection (m\leftrightarrow(s,t)).  Equations (3.1) and (3.4) use the literal half-open endpoints (A_M,B_M), and the profile supplies the exact terminal truncation before any tail majorization.

- **`exact_C_st2_cone_parity_character_parameterization` — PASS.**  Formula (2.1) retains the gcd (g), the coprimality allocation, multiplicity one, (r)-oddness, all even factors, the strict factor (4) cone, and the exact \(\chi _4(g)\chi _4(s_r)\) sign.

- **`large_square_part_t_tail_absolute_ledger` — PASS.**  The portion (t\geq\lceil M^{1/4}\rceil) is (M^{o(1)}) per dyadic block by (3.2), hence (O_{\varepsilon,V}(X^\varepsilon)) after exact profile support and dyadic assembly.  The divisor envelope is used only for this discharged complement.

- **`small_t_large_s_survivor_and_multiplicity` — PASS AS A REDUCTION, OPEN AS AN ESTIMATE.**  Equation (3.3) gives (s\gg M^{1/2}), while (3.4) records exact fixed-(s) multiplicity.  All coefficient, profile, mask, and phase data remain in (4.1).

- **`j_mask_nearest_integer_sign_tie_and_exact_radical` — PASS.**  Equations (2.2)--(2.3) are exact; the sign is recorded; upward ties are specified and proved impossible; (s=\operatorname{sqf}(N)) is exactly resonant and is deleted only by the literal strict mask.

- **`quadratic_irrational_Pell_and_continued_fraction_exceptions` — NO-GO FOR UNIFORM LINEAR-TWIST CANCELLATION.**  Relation (3.7) retains generalized Pell fibres.  The mask removes small (j), but the exact family (3.8)--(3.9) survives it with arbitrarily slow phase rotation and unbounded continued-fraction quotients.

- **`t_equals_one_and_bounded_t_capacity` — NO-GO FOR THE PROPOSED MECHANISM.**  The (t=1) fibre is a singleton in the linear variable, has absolute capacity (M^{1/4+o(1)}), and has nonzero exact coefficients such as (3.6).  Bounded (t) cannot yield the required power saving from a (t)-sum alone.

- **`individual_complex_direction_and_fixed_centre` — PASS.**  Formula (2.5) keeps (e(+t\sqrt{Ns})=e(+\theta_{s,t})) at one fixed (N=\lfloor X\rfloor).  No cosine, conjugate pairing, mean square, or centre average is used.

- **`full_R_M_s_t_power_and_dyadic_assembly` — PASS FOR THE TAIL; FAILS FOR ABSOLUTE CLOSURE OF THE SURVIVOR.**  Active (M\ll R^2=X^{1/2}).  The tail is (X^{o(1)}), whereas the small-(t) absolute ledger reaches (M^{1/4+o(1)}=X^{1/8+o(1)}) at the terminal scale.

- **`downstream_M1_M2_endpoint_M9_and_exponent_scope` — PASS.**  The result is only an exact reduction of the frozen scalar.  It proves no collar-tail owner, M1 parent, M9-M1 closure, M2 statement, endpoint-uniform statement, M9 theorem, bridge, or global exponent.

All controls above are analytic.  No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The only artifacts read were:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/briefs/blind_squarefree_linearization_feasibility.md`;
3. `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/blind_statement.md`.

The derivation uses only unique prime factorization, complete multiplicativity of \(\chi _4\) on odd integers, the elementary divisor estimate \(\tau(n)\ll_\eta n^\eta\), and elementary nearest-integer algebra.  No graph, proof draft, strategy file, sibling work, barrier packet, Round-138--145 nonblind artifact, web source, or external linear-twist theorem was used.

## 7. Recommended state effect

**Revise/retain.**  Subject to independent seam review, retain (2.1)--(2.6) as candidate evidence for an exact squarefree-fibre parameterization and a target-safe (t\geq M^{1/4}) complement.  Revise the live survivor to the owner-complete small-(t), large-squarefree-(s) sum (4.1).  Reject the claim that squarefree-kernel linearization alone proves the target, or that a generic fixed-centre linear-twist theorem applies: the (t=1) capacity obstruction and the exact near-resonant family (3.8)--(3.9) remain.  Make no downstream promotion.

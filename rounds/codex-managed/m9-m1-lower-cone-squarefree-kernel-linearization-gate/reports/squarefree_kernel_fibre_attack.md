# Round 145 discovery report: squarefree-kernel fibres

## 1. Result: strict squarefree-kernel reduction and a scoped linearization no-go

Let (R=X^{1/4}), (N=lfloor X\rfloor), and retain the literal disjoint
half-open blocks (mathcal I_M), the literal profile
(V_{\rm low}(R^2m/N)), and the Round-144 definitions

\[
 C(m)=\sum_{\substack{hr=m\\ r\ {\rm odd}\\r>4h}}\chi _4(r),
 \qquad k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
 \qquad j_m=k_m^2-Nm.
\]

For bounded (X) all assertions below are absorbed in the implied
constant, so the proof may assume (N\asymp X).  Every (m\geq1) has a
unique representation (m=s t^2), with (s) squarefree and (t\geq1).
The exact coefficient on this fibre is

\[
\boxed{
 C(st^2)=
 \sum_{\substack{uv=s\\\text{(uv) ordered}}}
 \ 
 \sum_{\substack{c,\ell,a,b\geq1\\
                   c\ {\rm squarefree},\ c\ell^2ab=t\\
                   (ua,vb)=1\\
                   c\ell vb\ {\rm odd}\\
                   vb^2>4ua^2}}
 \chi _4(cv). }
\tag{145.1}
\]

Here (c) is the squarefree kernel of the common divisor
((h,r)).  It is allowed to share primes with (u,v,a), or (b);
silently imposing any further coprimality deletes valid fibres.  Formula
(145.1) is multiplicity one.

Define the exact small-square survivor

\[
\begin{split}
 \mathfrak T_N^{<}:={}&
 \sum_M\ \sum_{1\leq t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
 |k_{s,t}^2-Nst^2|>M^{3/4}}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)C(st^2)e(t\sqrt{Ns}),\\
 &k_{s,t}:=\left\lfloor t\sqrt{Ns}+\frac12\right\rfloor.
\end{split}
\tag{145.2}
\]

Then the Round-144 open scalar has the owner-complete reduction

\[
\boxed{\mathfrak T_N=\mathfrak T_N^{<}+O_{\varepsilon,V}(X^\varepsilon).}
\tag{145.3}
\]

Indeed, more generally, the part of a fixed block with (t\geq T)
satisfies the absolute estimate

\[
 \boxed{\mathcal L_M(T)\ll_{\varepsilon,V}
 X^\varepsilon\frac{M^{1/4}}{T}}
 \qquad(1\leq T\leq \sqrt{2M}),
\tag{145.4}
\]

and is zero beyond the indicated natural range.  Thus (T=M^{1/4})
costs (O(X^\varepsilon)) per block, and the logarithmic block sum is
absorbed by epsilon renaming.  This is the strongest fixed-power
conclusion of the absolute squarefree-fibre count: if
(T=M^\theta), its certified price is (M^{1/4-\theta}X^\varepsilon).
For (	heta<1/4) this ledger no longer proves a target-sized bound;
this is an upper-price limitation, not a lower bound.

The remaining scalar (145.2) is not estimated.  Its fibres satisfy
(s>M^{1/2}), but the bounded-(t), and especially the (t=1),
layers retain block capacity (M^{1/4+o(1)}).  The (t=1) fibres have
only one (t)-sample in the block, so linear cancellation in (t)
cannot touch them.  Consequently the identity
(e(\sqrt{Nst^2})=e(t\sqrt{Ns})) alone cannot prove the target: a new
signed estimate across squarefree kernels (s), using the actual
coefficient and mask, is necessary.  The correct round label is

\[
 \boxed{\mathsf{strict\_squarefree\_kernel\_reduction}},
\]

with a scoped no-go for any argument that takes absolute values across
(s) and seeks all of its gain only from the linear (t)-twist.

## 2. Exact statement and hypotheses

Write ({\rm sf}(n)) for the unique squarefree kernel of (n).  The
coefficient formula (145.1) has the following equivalent version.  For
each divisor pair in (C(st^2)), put

\[
 g=(h,r),\qquad H=h/g,\qquad Q=r/g.
\]

There are unique squarefree (u,v) and positive (a,b) such that

\[
 H=ua^2,\qquad Q=vb^2,
 \qquad uv=s,\qquad (ua,vb)=1,
\tag{145.5}
\]

and necessarily (gab=t).  Conversely, every tuple satisfying
(145.5) and (gab=t) gives exactly one pair

\[
 h=g,ua^2,\qquad r=g,vb^2.
\tag{145.6}
\]

Writing (g=c\ell^2), where (c={\rm sf}(g)), gives (145.1).  The
original parity, character, and cone become exactly

\[
 r\ {\rm odd}\iff c,\ell,v,b\ {\rm odd},\qquad
 \chi _4(r)=\chi _4(cv),\qquad
 r>4h\iff vb^2>4ua^2.
\tag{145.7}
\]

In particular, if (2\mid s), then the ordered factorization must put
(2\mid u); if (2\mid t), all of (v_2(t)) lies in (a).  This is
the complete even-fibre rule.  There is no restriction involving the
parity of (N), which enters only through the phase and the displacement
mask.

The half-open block and multiplicity assertions used below are literal:
for fixed (t),

\[
 \frac{M}{t^2}\leq s<\frac{2M}{t^2},
\tag{145.8}
\]

before intersecting with the terminal profile support.  A nonempty
fibre has (t^2<2M), and hence

\[
 \#\{s\ {\rm squarefree}:st^2\in\mathcal I_M\}
 \leq \frac{M}{t^2}+1\leq \frac{3M}{t^2}.
\tag{145.9}
\]

Terminal truncation and the literal profile can only shorten this set.
On the small-square side (t<M^{1/4}), (145.8) gives the strict support
fact

\[
 \boxed{s=\frac m{t^2}>M^{1/2}.}
\tag{145.10}
\]

For a fixed squarefree (s), (145.2) is an individual complex linear
twist in (t), with frequency

\[
 \alpha_s=\sqrt{Ns},\qquad e(+t\alpha_s),
\tag{145.11}
\]

and with the actual (t)-dependent coefficient (C(st^2)), profile,
half-open support, and hard mask.  No conjugate, cosine, average over
(N), or mean square over (s) is substituted for (145.11).

The exact mask geometry is as follows.  Put

\[
 x=t\alpha_s=\sqrt{Nst^2},\qquad k=\lfloor x+1/2\rfloor,
 \qquad \delta=k-x.
\tag{145.12}
\]

There is no nearest-integer tie: (x=n+1/2) would imply that the
multiple of four (4Nst^2) is the odd square ((2n+1)^2).  Thus
(-1/2<\delta<1/2), and

\[
 j_{st^2}=\delta(k+x)=\delta(2x+\delta),
 \qquad \operatorname {sgn}j_{st^2}=\operatorname {sgn}\delta.
\tag{145.13}
\]

With (J=M^{3/4}), the positive and negative parts of the strict mask
are, exactly,

\[
\begin{array}{ll}
 j>J
 &\Longleftrightarrow\quad
 \delta>\sqrt{x^2+J}-x
 ={J}/{(\sqrt{x^2+J}+x)},\\[3pt]
 j<-J
 &\Longleftrightarrow\quad
 -\delta>x-\sqrt{x^2-J}
 ={J}/{(x+\sqrt{x^2-J})},
\end{array}
\tag{145.14}
\]

where (x^2>J) throughout the nontrivial large-(X) active range.
Equivalently,

\[
 \|t\alpha_s\|=|\delta|=\frac{|j_{st^2}|}{k+t\alpha_s},
 \qquad |j_{st^2}|>J,
\tag{145.15}
\]

with the sign still determined by (145.13), not discarded.  On
(st^2\in[M,2M)), its scale is

\[
 \frac{J}{k+t\alpha_s}\asymp
 \frac{M^{3/4}}{\sqrt{NM}}
 =\frac{M^{1/4}}{\sqrt N}.
\tag{145.16}
\]

Finally write (N=Dw^2), with (D) squarefree.  Then

\[
 Ns\text{ is a square}\iff s=D.
\tag{145.17}
\]

For (s=D), (alpha_s=Dw), every (t) has (j_{st^2}=0), and the
whole fibre is absent from the strict Round-144 mask; it remains in the
separately accepted exact-radical owner.  If (s\ne D), set

\[
 g_s=(D,s),\qquad q_s=\frac{Ds}{g_s^2}>1.
\tag{145.18}
\]

Then (q_s) is squarefree,
(alpha_s=g_sw\sqrt{q_s}) is quadratic irrational, and every mask
value is the exact generalized Pell norm

\[
 \boxed{j_{st^2}=k^2-q_s(g_sw t)^2.}
\tag{145.19}
\]

Thus Pell and continued-fraction near resonances are not a heuristic
exceptional set: they are literal fibres of (145.19), subject to the
divisibility condition on the second coordinate.  Small-norm solutions
fall in the already target-safe Round-144 window; generalized Pell norms
just beyond its boundary remain part of (145.2).  Squarefreeness gives no
uniform bound on the continued-fraction data as (q_s) varies.

## 3. Proof and complete power ledger

For the coefficient bijection, start with (hr=st^2) and
(g=(h,r)).  Since (g^2\mid st^2) and (s) is squarefree, prime by
prime (v_p(g)\leq v_p(t)), so (g\mid t).  The coprime integers
(H=h/g) and (Q=r/g) have product

\[
 HQ=s(t/g)^2.
\]

Their squarefree kernels are coprime and multiply to (s); hence they
have the unique form (145.5), and uniqueness of positive square roots
gives (t=gab).  Conversely (145.6) has product (st^2) and greatest
common divisor exactly (g).  Decomposing (g=c\ell^2) is unique,
including cases such as (g=p^3), for which (c=\ell=p).  This also
shows why (c) may overlap one of (u,v,a,b).  Cancelling (g) from
the strict cone and applying the odd character gives (145.7), proving
(145.1) with multiplicity one.  In particular,

\[
 |C(st^2)|\leq\tau(st^2)\ll_\varepsilon X^\varepsilon
\tag{145.20}
\]

uniformly on the profile support.

Now fix a block.  Using (145.9), (145.20),
(m^{-3/4}\leq M^{-3/4}), and the bounded literal profile, the masked
part with (t\geq T) costs

\[
\begin{split}
 |\mathcal L_M(T)|
 &\ll_{\varepsilon,V}
 X^\varepsilon M^{-3/4}
 \sum_{T\leq t<\sqrt{2M}}\frac{M}{t^2}\\
 &\ll_{\varepsilon,V}
 X^\varepsilon\frac{M^{1/4}}{T}.
\end{split}
\tag{145.21}
\]

No property of the mask was used, so the strict inequality, either sign
of (j), and all boundary cells are retained; exact radicals contribute
zero to the masked sum in any event.  Taking (T=M^{1/4}) proves the
per-block large-square bound.  The profile restricts

\[
 M\ll_V\frac N{R^2}\asymp R^2,
\tag{145.22}
\]

and there are (O_V(\log(2X))) half-open blocks, including the smallest
and terminal blocks.  Applying (145.21) with a smaller epsilon and
renaming it proves (145.3).

For comparison, a dyadic (t)-shell (T\leq t<2T) has the same
absolute ledger

\[
 X^\varepsilon M^{-3/4}
 \sum_{T\leq t<2T}\frac{M}{t^2}
 \ll X^\varepsilon\frac{M^{1/4}}T.
\tag{145.23}
\]

The entire small-(t) part has only

\[
 |\mathfrak T_{N,M}^{<}|
 \ll X^\varepsilon M^{1/4}
 \sum_{t<M^{1/4}}t^{-2}
 \ll X^\varepsilon M^{1/4}.
\tag{145.24}
\]

At the largest active scale (M\asymp R^2), this is
(R^{1/2+o(1)}=X^{1/8+o(1)}), whereas (145.21) at
(T=M^{1/4}\asymp R^{1/2}) is target-sized.  There is no missing
power of (R), (M), (s), or (t) in this accounting.

For each fixed (t), the corresponding absolute price is

\[
 \ll X^\varepsilon\frac{M^{1/4}}{t^2}.
\tag{145.25}
\]

Thus every bounded (t) remains owner-sized.  In particular, when
(t=1), (145.1) reduces to

\[
 C(s)=\sum_{\substack{uv=s\\v\ {\rm odd}\\v>4u}}\chi _4(v),
\tag{145.26}
\]

and for every odd prime (p>4), (C(p)=\chi _4(p)).  Hence the
bounded-(t) layer is not algebraically empty.  Moreover, for
(s\in[M,2M)), the block contains (t=1) and contains no second
(t)-value on that same (s)-fibre, because (t\geq2) would give
(st^2\geq4M).  Any procedure which estimates each fixed-(s)
linear twist and then takes absolute values over (s) therefore pays
(145.24) already on these singleton fibres.  This proves the scoped
linearization no-go.  It does not assert that the actual complex sum has
large modulus.

Equations (145.13)--(145.19) follow by direct algebra.  The only generic
Diophantine consequence for (s\ne D) is the integer-norm inequality

\[
 \|t\alpha_s\|=\frac{|j_{st^2}|}{k+t\alpha_s}
 \geq\frac1{k+t\alpha_s}
 \asymp\frac1{\sqrt{NM}},
\tag{145.27}
\]

whose constant and continued-fraction refinement vary with (Ns).
The Round-144 survivor imposes the larger but still microscopic scale
(145.16).  This is a phase-value condition at the multiples
(t\alpha_s); it is neither a uniform gap for the base frequency
(alpha_s) nor a cancellation theorem for the weighted coefficients
(C(st^2)).  Even a coefficient-free geometric-sum estimate would have
to confront quadratic irrational frequencies with varying Pell data,
while the actual coefficient and hard mask are not constant in (t).

## 4. First doubtful or unproved step

The first unproved statement is exactly

\[
 \boxed{\mathfrak T_N^{<}\ll_{\varepsilon,V}X^\varepsilon}
\tag{145.28}
\]

uniformly for the fixed real centre (X).  Support information
(s>M^{1/2}), the irrationality of (sqrt{Ns}) away from (s=D),
and the mask gap (145.16) do not imply (145.28).

Already the (t=1) block would require, schematically and with the
literal profile and mask retained, an unweighted signed estimate of size

\[
 \sum_{\substack{s\asymp M\ {\rm squarefree}\\
 |k_{s,1}^2-Ns|>M^{3/4}}}
 V_{\rm low}(R^2s/N)C(s)e(\sqrt{Ns})
 \ \ll_{\varepsilon,V} M^{3/4}X^\varepsilon,
\tag{145.29}
\]

or the corresponding uniform partial-sum statement needed for Abel
summation.  The divisor envelope is (M^{1+o(1)}), so (145.29) asks for
a genuine (M^{1/4}) signed saving across (s).  There is no (t)-sum
at all on this layer.  Formula (145.26), including
(C(p)=\chi _4(p)), also prevents replacing the coefficient by a
uniformly tiny one.  No result in the permitted context proves
(145.29) for the individual (+) direction.

This is the first capacity obstruction, not evidence that (145.28) is
false.  Cancellation across (s), across (t)-layers, or across
dyadic blocks remains mathematically possible.  A positive capacity,
the existence of Pell fibres, or a quarter-frequency coefficient
resonance cannot be upgraded to a lower bound for the nonlinear
fixed-centre scalar.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `unique_squarefree_kernel_decomposition_and_block_endpoints` | **PASS.** (m=st^2) and the finer tuple (145.5)--(145.7) are bijective.  The count uses the literal half-open interval and only shortens at the terminal profile boundary. |
| `exact_C_st2_cone_parity_character_parameterization` | **PASS.** Formula (145.1) retains the ordered (uv=s), the squarefree common kernel (c), all allowed overlaps, ((ua,vb)=1), the exact odd rule, (chi _4(cv)), strict (vb^2>4ua^2), and multiplicity one. |
| `large_square_part_t_tail_absolute_ledger` | **PASS/target-safe.** Equations (145.21)--(145.23) give (M^{1/4}/T); (t\geq M^{1/4}) is (O(X^\varepsilon)) after all blocks. |
| `small_t_large_s_survivor_and_multiplicity` | **PASS as a reduction; OPEN as an estimate.** The exact survivor is (145.2), (s>M^{1/2}), fixed-(t) multiplicity is at most (3M/t^2), and the inner coefficient parameterization has no extra multiplicity. |
| `j_mask_nearest_integer_sign_tie_and_exact_radical` | **PASS.** Ties are impossible, (145.13)--(145.16) retain both signs and the strict boundary, and (s=D) is exactly the separately owned radical fibre. |
| `quadratic_irrational_Pell_and_continued_fraction_exceptions` | **PASS/obstruction retained.** Every (s\ne D) gives the literal generalized Pell norm (145.19).  No bounded-quotient or uniform-spacing hypothesis is introduced; small norms and surviving boundary norms are distinguished. |
| `t_equals_one_and_bounded_t_capacity` | **PASS/no-go.** Equations (145.24)--(145.26) give bounded-(t) capacity (M^{1/4+o(1)}), top price (R^{1/2+o(1)}), and nonempty singleton (t=1) fibres. |
| `individual_complex_direction_and_fixed_centre` | **PASS.** Every displayed survivor contains (e(+t\sqrt{Ns})) at the prescribed (N=\lfloor X\rfloor); no real-part, conjugate, centre average, or square function is used. |
| `full_R_M_s_t_power_and_dyadic_assembly` | **PASS.** The ledger is (M^{1/4}/T), (M\ll_VR^2), top large-tail threshold (T\asymp R^{1/2}), small-(t) capacity (R^{1/2}), and only a logarithmic number of blocks. |
| `Round144_owner_and_Round138_cross_term_separation` | **PASS.** Only the strict Round-144 displayed cone survivor is reduced.  Its exact-radical owner is not recounted, and the independent Round-138 collar-tail cross owner is untouched. |
| `downstream_M1_M2_endpoint_M9_and_exponent_scope` | **PASS.** No lower GAR, direct M1 parent, M9-M1, M2 owner, endpoint theorem, M9 theorem, bridge, quarter result, or exponent improvement is claimed. |

All controls are analytic or algebraic.  No numerical, symbolic, random,
or average-in-centre evidence is used.

## 6. Dependencies and exact artifacts used

The derivation uses only the following authorized artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`, at graph hash
  `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/conductor_round144_appell_completion_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/conductor_round142_rational_spectrum_adjudication.md`.

The inherited inputs are the exact Round-144 survivor, its
(M^{3/4}) target-safe displacement deletion, the divisor envelope,
the separate exact-radical owner, and the standing Appell, rational-mode,
derivative-arc, reciprocal-return, directionality, and scope barriers.
No external theorem or sibling Round-145 report is used.  The allocation
is 100 percent analytic/algebraic and 0 percent numerical.

## 7. Recommended state effect

Recommend **promote**, after independent seam review, only the scoped
reduction (145.1)--(145.4): record the exact multiplicity-one
squarefree-kernel fibre formula and replace the Round-144 survivor by the
owner-complete small-square scalar (145.2), with the aggregate
(t\geq M^{1/4}) complement target-safe.

Also retain as a scoped obstruction, without treating it as a lower
bound, that squarefree-kernel linearization supplies no (t)-cancellation
on the (t=1) singleton fibres and that bounded (t) retains top-block
capacity (R^{1/2+o(1)}).  Any continuation must prove a fixed-centre
signed correlation across the actual squarefree kernels (s), while
retaining (145.1), the hard mask, the individual (+) direction, and the
Pell geometry (145.19).

Leave the target estimate (145.28) open.  Make no change to the
Round-138 cross owner, complete lower GAR, either direct M1 parent,
M9-M1, any M2 owner, endpoint uniformity, M9, the conditional bridge, or
any global exponent.

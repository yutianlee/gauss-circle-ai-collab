# Literal radical-frequency attack

## 1. Result: route-scoped coupling no-go, with two target-safe exact subowners

The correct Round-161 exit label for this report is
`hard_top_radical_frequency_coupling_no_go`.  Three exact facts are proved.

First, the literal coefficient has the bijective incidence formula

\[
\begin{aligned}
B_D(t)=\mathbf 1_{Dt^2\asymp L^2}
\sum_{\substack{d_1d_2=D\\guv=t\\(d_1u,d_2v)=1\\
g,d_1,u\ {\rm odd}\\d_2v^2\le d_1u^2\le4d_2v^2}}
&\chi _4(gd_1)\eta_L(gd_1u^2)
 \Phi\!\left(\frac{gd_1u^2}{H+1}\right)\\
&\times\left(\frac{L^2}{Dt^2}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}}\right),
\end{aligned}
\tag{1.1}
\]

with the inherited literal zero extension and half-open support.  There is
no hidden multiplicity in (1.1).

Second, if the active product support is contained in
\(c_-L^2\le Dt^2\le c_+L^2\), where the fixed positive constants
\(c_-,c_+\) come only from the dyadic height support and the hard cone,
then for every fixed \(C>0\)

\[
 \left|\sum_{\substack{D>1\ {\rm sf}\\D\le CL}}
          \sum_t B_D(t)e(tJ\sqrt D)\right|
 \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.
\tag{1.2}
\]

Consequently every fixed long-channel sector
\(t\ge \tau\sqrt L\), \(\tau>0\) fixed, is target-safe: support forces
\(D\le c_+\tau^{-2}L\).  Conversely \(D\le CL\) forces every active
\(t\ge\sqrt{c_-/C}\sqrt L\).  Thus the conductor's proposed
\(D\lesssim L\), \(t\gtrsim\sqrt L\) sector is correct, with the
constants just displayed.  This is a genuinely owner-complete strict
**channel sector**, but it is only an immediate absolute corollary of the
accepted fixed-\(D\) estimate.  It neither supplies new cancellation nor
closes the whole hard-TOP block for any polynomial range of \(L\).
Accordingly it is not advertised as the exit label
`strict_hard_top_radical_frequency_range`.

Third, the exact base-frequency collision graph

\[
 J\sqrt{D_1}\equiv J\sqrt{D_2}\pmod 1,\qquad D_1\ne D_2,
\tag{1.3}
\]

on squarefree \(D>1\) has at most one unordered nonloop edge.  The same
statement at atom level says that all exact cross-channel relations
\(t_1J\sqrt{D_1}\equiv t_2J\sqrt{D_2}\pmod1\) use one unordered radical
pair, and relations on that pair are rational multiples of one primitive
relation.  A rational channel \(J\sqrt D\in\mathbb Q\), including a
whole phase-one channel, is unique and cannot coexist with a cross-channel
exact relation.  All channels involved in these exact relations are
target-safe by the accepted fixed-channel \(\ell^1\) bound.  This is an
exact-collision lemma only; it gives no lower bound for a nonzero
modulo-one distance and no near-collision estimate.

After (1.2), the first unresolved owner is therefore the short-channel
sector \(D\gg L\), \(t\ll\sqrt L\).  Its \(t=1\), \(D\asymp L^2\)
layer gives an exact obstruction to the proposed coefficient-uniform
common-test/projective/Bessel route.  Even a rank-one tensor supported at
\(t=1\) can absorb all phases in its \(D\)-factor, has the accepted
\(L^2\) energy scale and fixed-channel scale, and produces \(L^2\)
scalar capacity.  Its Hilbert projective norm and the Bessel evaluation
norm are each \(L^{1+o(1)}\), so their product restores \(L^{2+o(1)}\)
and loses exactly the required \(L^{1/2-o(1)}\).  This is an adversarial
coefficient-interface control, not a lower bound for the physical
coefficient (1.1).  A future proof must use a phase-sensitive property of
the literal vector \(D\mapsto B_D(1)\), or a genuinely joint substitute;
exact collision sparsity and a common-test theorem alone cannot do so.

## 2. Exact statement and hypotheses

Let

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and fix the assigned half-open polynomial intermediate block
\(1\ll L\ll H\).  All assertions below concern only the nonsquare part
of this one literal hard-TOP block.  The square sector remains removed
only through its accepted norm owner.

For odd positive \(h\), on the exact integer cone
\(\lceil h/4\rceil\le m\le h\), put

\[
a_{\rm end}(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
\left(\frac{L^2}{hm}\right)^{3/4}
W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
\]

with literal zero extension.  The product coefficient is

\[
C_L(n)=\sum_{\substack{h\mid n,\ h\ {\rm odd}\\
\sqrt n\le h\le2\sqrt n}}
\chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\]

For squarefree \(D>1\), define

\[
B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
\mathbf1_{Dt^2\asymp L^2}.
\tag{2.1}
\]

The exact scalar and accepted controls are

\[
\mathcal T_L^{\rm ns}=\sum_{D>1\ {\rm sf}}\sum_{t\ge1}
B_D(t)e(tJ\sqrt D),
\tag{2.2}
\]

\[
\sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),\qquad
\sum_t|B_D(t)|\ll_\varepsilon
(1+L/\sqrt D)L^\varepsilon.
\tag{2.3}
\]

Because \(\eta_L\) is supported at \(h\asymp L\) and
\(m\le h\le4m\), there are fixed constants \(0<c_-<c_+<\infty\),
independent of \(X,L,D,t\), such that

\[
B_D(t)\ne0\quad\Longrightarrow\quad
c_-L^2\le Dt^2\le c_+L^2.
\tag{2.4}
\]

Only this implication is used; no positivity or full population of the
support is assumed.

The exact-collision assertions use no Diophantine hypothesis on the
arbitrary real \(J>0\).  A base collision is an unordered pair
\(D_1\ne D_2\) satisfying (1.3).  An atom collision is a relation with
positive integers \(t_1,t_2\), possibly in their moving literal ranges,

\[
J(t_1\sqrt{D_1}-t_2\sqrt{D_2})\in\mathbb Z.
\tag{2.5}
\]

For the route obstruction, let \(I_L=[aL^2,bL^2]\) be any fixed
positive-relative-width interval admitted by the coarse condition
\(Dt^2\asymp L^2\), and let
\(\mathscr D_L=\{D\in I_L:D>1\text{ squarefree}\}\).  This is used only
to test a theorem asserted from support, (2.3), and frequency spacing;
the diagnostic array introduced below is explicitly not asserted to have
the physical incidence (1.1).

## 3. Proof and complete collision/factorization/power derivation

**Literal radical incidence.**  Every nonsquare positive integer has a
unique expression \(n=Dt^2\) with \(D>1\) squarefree.  For an original
incidence \(hm=Dt^2\), let \(g=(h,m)\), \(h=ga\), and \(m=gb\).  Then
\((a,b)=1\).  Write uniquely

\[
a=d_1u^2,\qquad b=d_2v^2,
\]

where \(d_1,d_2\) are squarefree.  Coprimality gives
\((d_1u,d_2v)=1\), and the squarefree kernel of \(ab\) gives
\(d_1d_2=D\).  Comparing

\[
hm=g^2d_1d_2u^2v^2=D(guv)^2
\]

with \(Dt^2\) gives \(t=guv\).  Conversely, every tuple satisfying
these conditions returns the unique pair
\((h,m)=(gd_1u^2,gd_2v^2)\).  Thus the parametrization is bijective.

The integer lower edge is exact:
\(\lceil h/4\rceil\le m\) if and only if \(h\le4m\).  Hence the cone is

\[
d_2v^2\le d_1u^2\le4d_2v^2.
\]

Also \(h\) is odd if and only if \(g,d_1,u\) are all odd.  On this set,
\(\chi_4(h)=\chi_4(gd_1u^2)=\chi_4(gd_1)\).  Finally,

\[
\sqrt{\frac{q_Xh^2}{4Dt^2}}
=\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}},\qquad
L^{3/2}(Dt^2)^{-3/4}=\left(\frac{L^2}{Dt^2}\right)^{3/4}.
\]

Substitution proves (1.1).  In particular, if \(D\) is even, the factor
2 lies in \(d_2\), since \(d_1\) is odd; if \(t\) is even, its 2-part
lies in \(v\), since \(g,u\) are odd.  Thus no even-\(D\) or parity
case has been silently discarded.

**The small-\(D\)/long-\(t\) owner.**  For \(Z\ge2\), (2.3) and the
triangle inequality give

\[
\begin{aligned}
\left|\sum_{\substack{2\le D\le Z\\D\ {\rm sf}}}\sum_t
B_D(t)e(tJ\sqrt D)\right|
&\le L^\varepsilon\sum_{D\le Z}(1+L/\sqrt D)\\
&\ll L^\varepsilon\bigl(Z+L\sqrt Z\bigr).
\end{aligned}
\tag{3.1}
\]

Here \(\sum_{D\le Z}D^{-1/2}\le2\sqrt Z\), and deleting the
nonsquarefree \(D\)'s only decreases the sum.  Taking \(Z=CL\) proves
(1.2).  Since \(L\le H\ll X^{1/4}\), the factor \(L^\varepsilon\) is
absorbed into \(X^\varepsilon\).

If an active term has \(t\ge\tau\sqrt L\), (2.4) gives

\[
D\le\frac{c_+L^2}{t^2}\le c_+\tau^{-2}L,
\]

so it belongs to (1.2).  Conversely, if \(D\le CL\), then (2.4) gives
\(t\ge\sqrt{c_-/C}\sqrt L\).  This verifies both directions with the
dyadic constants exposed.  The general ledger (3.1) also shows the
limit of this particular positive argument: at \(Z=L^{1+\delta}\),
the term \(L\sqrt Z=L^{3/2+\delta/2}\) already exceeds target for every
fixed \(\delta>0\).  This is a limit of (3.1), not a physical lower
bound.

**Linear independence of squarefree radicals.**  Let
\(D_1,\ldots,D_r\) be distinct squarefree integers.  List the primes
appearing in their product, and work in the multiquadratic field obtained
by adjoining their square roots.  Independent sign changes of the prime
square roots form an elementary 2-group.  The monomials \(\sqrt{D_i}\)
are distinct characters of that group.  If
\(\sum_i q_i\sqrt{D_i}=0\), \(q_i\in\mathbb Q\), apply every sign
change, multiply by the character belonging to \(D_j\), and average over
the group.  Character orthogonality leaves only
\(q_j\sqrt{D_j}=0\).  Thus every \(q_j=0\), proving that square roots of
distinct squarefree integers are linearly independent over
\(\mathbb Q\).

**Exact base collisions, including all shared-index cases.**  Suppose
two nontrivial base collision equations hold:

\[
J(\sqrt{D_1}-\sqrt{D_2})=k,\qquad
J(\sqrt{D_3}-\sqrt{D_4})=\ell,
\tag{3.2}
\]

where \(k,\ell\in\mathbb Z\setminus\{0\}\).  Eliminating \(J\) gives

\[
\ell\sqrt{D_1}-\ell\sqrt{D_2}
-k\sqrt{D_3}+k\sqrt{D_4}=0.
\tag{3.3}
\]

If the pairs are disjoint, (3.3) is a nonzero relation among four
distinct radicals.  If they share exactly one index, it is a nonzero
relation among three distinct radicals.  Both are impossible.  If they
share both indices, linear independence says the two equations are the
same unordered edge, with only repetition or reversal possible.  Thus
the base collision graph has at most one unordered nonloop edge.

If \(J\sqrt{D_0}=r\in\mathbb Q\setminus\{0\}\), a second rational
channel would make \(\sqrt{D_0/D_1}\in\mathbb Q\) and hence
\(D_0=D_1\).  Combining this rational-channel equation with either
equation in (3.2) produces a nonzero rational relation among at most three
distinct radicals; the shared-endpoint cases still leave a nonzero
coefficient of the other radical.  Hence a rational channel cannot
coexist with an unequal exact base collision.  The whole phase-one case
\(r\in\mathbb Z\) is included.

The atom-level audit is identical but slightly stronger.  If

\[
J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,\qquad
J(s_1\sqrt{D_3}-s_2\sqrt{D_4})=\ell
\tag{3.4}
\]

are two cross-channel relations, then by definition
\(D_1\ne D_2\), \(D_3\ne D_4\), and \(k,\ell\ne0\); equality with
zero would force the two squarefree kernels to agree.  Eliminating \(J\)
and applying radical independence again forbids disjoint pairs and
one-index overlaps.  On the same unordered pair, it forces

\[
(s_1,s_2,\ell)=q(t_1,t_2,k)
\]

for a nonzero rational \(q\), after reversing an orientation if needed.
Thus there may be several integer multiples of one primitive atom
relation, but no second radical pair.  If instead \(D_1=D_2=D\), then
the atom equation is

\[
(t_1-t_2)J\sqrt D=k.
\]

The case \(t_1=t_2\) is the trivial same-atom loop (and forces \(k=0\));
a nontrivial same-channel repetition occurs only on the unique possible
rational channel.  It is separate from cross-channel collisions.  A
rational channel also cannot share an endpoint with a cross-channel
relation: if \(J\sqrt{D_0}=r\in\mathbb Q\) and the first relation in
(3.4) holds, then eliminating \(J\) gives

\[
rt_1\sqrt{D_1}-rt_2\sqrt{D_2}-k\sqrt{D_0}=0,
\tag{3.4a}
\]

contradicting square-root independence because \(D_1\ne D_2\) and
\(k\ne0\).

Every channel named in this exact classification is harmless without
cancellation: a rational channel, or both channels on the unique
cross-channel edge, has total absolute mass

\[
\ll_\varepsilon
\left(1+\frac L{\sqrt{D_1}}+1+\frac L{\sqrt{D_2}}\right)L^\varepsilon
\ll L^{1+\varepsilon},
\tag{3.5}
\]

with the absent channel omitted.  This is below \(L^{3/2}X^\varepsilon\).

There is no near-collision consequence.  For any prescribed unequal
pair, choosing
\(J=k/|\sqrt{D_1}-\sqrt{D_2}|\), with a sufficiently large positive
integer \(k\), makes that pair collide exactly; arbitrarily small
perturbations make its modulo-one gap arbitrarily small.  Radical linear
independence is qualitative and supplies neither a uniform gap nor a
collar multiplicity bound for the arbitrary fixed center in this task.

**The large-\(D\), \(t=1\) physical seam.**  In (1.1), \(t=1\) forces
\(g=u=v=1\).  Hence the literal layer is

\[
\begin{aligned}
B_D(1)=\mathbf1_{D\asymp L^2}\left(\frac{L^2}{D}\right)^{3/4}
\sum_{\substack{d_1d_2=D\\d_1\ {\rm odd}\\d_2\le d_1\le4d_2}}
&\chi_4(d_1)\eta_L(d_1)
\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\end{aligned}
\tag{3.6}
\]

For \(D=pq\), where \(p<q\le4p\) are distinct odd primes, the only
eligible near-square upper factor is \(d_1=q,d_2=p\).  Whenever the
literal profiles are nonzero there, (3.6) is a genuine one-incidence
physical coefficient; there is no internal divisor cancellation to
invoke.  This proves nonvacuity of the hostile singleton mechanism, not
a family lower bound or a lower mass assertion.

**Exact projective/Bessel price and scoped no-go.**  On a finite set of
radicals define the common-test evaluation operator

\[
(E_Jc)(D)=\sum_t c(t)e(tJ\sqrt D).
\tag{3.7}
\]

A Hilbert projective decomposition
\(A_D(t)=\sum_r x_r(D)c_r(t)\), followed by a common-test Bessel bound
and Cauchy in \(D\), gives

\[
|\Lambda_J(A)|
\le \|E_J\|_{2\to2}
\inf_{A=\sum_r x_r\otimes c_r}
\sum_r\|x_r\|_2\|c_r\|_2
=\|E_J\|_{2\to2}\|A\|_{S_1}.
\tag{3.8}
\]

The infimum is the nuclear norm of the row-column matrix.  The accepted
Hilbert--Schmidt control alone yields only
\(\|B\|_{S_1}\le\sqrt{\operatorname{rank}B}\|B\|_{S_2}\); since the
active \(t\)-set can have \(L^{1+o(1)}\) elements, this generic passage
may itself spend the missing \(L^{1/2}\).  The entrywise or incidencewise
atomic decomposition is worse: its projective price is the positive
product-fibre mass, of capacity \(L^{2+o(1)}\).

More decisively, high rank is not the first obstruction.  The elementary
identity

\[
\#\mathscr D_L
=\sum_{aL^2<D\le bL^2}\mu^2(D)
=\frac{b-a}{\zeta(2)}L^2+O_{a,b}(L)
\asymp L^2
\tag{3.9}
\]

follows by inserting \(\mu^2(D)=\sum_{r^2\mid D}\mu(r)\).  Put

\[
A_D(t)=\mathbf1_{D\in\mathscr D_L}\mathbf1_{t=1}e(-J\sqrt D).
\tag{3.10}
\]

This diagnostic array has the correct coarse support,
\(\sum_{D,t}|A_D(t)|^2\asymp L^2\), and fixed-channel \(\ell^1\) mass
one, matching the scales allowed by (2.3) on \(D\asymp L^2\).  It is the
rank-one tensor \(x\otimes e_1\), so

\[
\|A\|_{S_1}=\|x\|_2\asymp L,\qquad
\|E_Je_1\|_2=\#\mathscr D_L^{1/2}\asymp L.
\]

Moreover

\[
\Lambda_J(A)=\sum_{D\in\mathscr D_L}
e(-J\sqrt D)e(J\sqrt D)=\#\mathscr D_L\asymp L^2.
\tag{3.11}
\]

Thus (3.8) is sharp at the full positive capacity already on a rank-one,
one-coordinate tensor, irrespective of exact frequency collisions.  Its
loss relative to the target is exactly \(L^{1/2+o(1)}\).  Equivalently,
on the physical \(t=1\) layer the controls currently give only

\[
\left|\sum_D B_D(1)e(J\sqrt D)\right|
\le \#\{D\asymp L^2\}^{1/2}
\left(\sum_D|B_D(1)|^2\right)^{1/2}
\ll L^2\sqrt{\log(2L)},
\tag{3.12}
\]

whereas target closure through this placement would require the new
physical estimate
\(\sum_D|B_D(1)|^2\ll L^{1+o(1)}\), or direct signed cancellation of
comparable strength.  Neither follows from the accepted controls.

The array (3.10) is phase-adapted and is not (1.1).  Equations
(3.10)--(3.12) therefore prove only the following precise no-go: support,
the two accepted positive norms, exact collision sparsity, and an
arbitrary-row Hilbert projective/common-test theorem cannot deliver the
target.  They do not disprove a bespoke theorem for the actual
truncated-divisor vector.

## 4. First doubtful or unproved step

After removing the owner-complete long-channel sector and all exact
collision channels, the first unproved physical statement is already the
large-radical singleton-direction estimate

\[
\boxed{
\left|\sum_{\substack{D\asymp L^2\\D\ {\rm squarefree}}}
B_D(1)e(J\sqrt D)\right|
\ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{4.1}
\]

Here \(B_D(1)\) is the literal complementary-factor expression (3.6),
not an arbitrary bounded sequence.  There is no oscillatory \(t\)-sum
on which a common-test theorem can act, and exact collision sparsity does
not constrain a varying \(D\)-coefficient.  The accepted energy permits
the right side of (3.12), while the singleton-semiprime control shows
that divisor cancellation is not available coefficient by coefficient.
No physical lower mass is known, so (4.1) remains a possible theorem.

A full proof would additionally have to couple every few-point row
\(L\ll D\ll L^2\), not just (4.1), and control the actual modulo-one
near-collision collars.  The first doubtful step in any proposed
large-sieve continuation is therefore the claimed low-cost structural
restriction on the \(D\)-factor of the literal matrix.  Merely writing
\(B=\sum_r x_r\otimes c_r\) is exact but useless until a norm or
directional theorem is proved that fails for (3.10) and retains (1.1).

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_product_fibre_and_square_owner` | Pass.  The scalar starts from the accepted product fibre; \(D=1\) is not reintroduced, and no square cancellation is claimed beyond the accepted square norm owner. |
| `unique_radical_linearization` | Pass.  \(n=Dt^2\) and the finer \((g,d_1,d_2,u,v)\) coordinates are bijective. |
| `actual_coefficient_incidence` | Pass.  Formula (1.1) is derived term by term, with no multiplicity or fictitious common coefficient. |
| `fixed_center_exact_resonance` | Pass and strengthened.  There is at most one rational channel; all exact cross-channel atom relations use at most one radical pair; those channels are absolutely safe. |
| `near_resonance_mod_one_collisions` | Open, correctly scoped.  Exact radical independence gives no quantitative modulo-one spacing.  Arbitrary \(J\) permits arbitrarily small gaps. |
| `small_D_long_channels` | Pass.  Equation (3.1) proves all \(D\le CL\), equivalently every fixed \(t\gtrsim\sqrt L\) sector, target-safe with exact support constants.  This is a subowner, not a full polynomial \(L\)-range. |
| `t1_large_D_singleton_layer` | Hostile seam survives.  Formula (3.6) is exact; close semiprimes can have one physical incidence, and the diagnostic rank-one layer has full controls-only capacity. |
| `coefficient_varying_large_sieve_applicability` | Fail for a coefficient-uniform import.  A common test estimates \(E_Jc\), while the literal problem has a distinct row vector \(B_D\); at \(t=1\) the \(D\)-factor can carry the entire alignment. |
| `projective_tensor_bessel_price` | Fail at the required power under the frozen controls.  Equation (3.8) is the exact Hilbert projective ledger, and (3.10)--(3.11) make both factors \(L^{1+o(1)}\), restoring \(L^{2+o(1)}\). |
| `hard_profiles_parity_endpoints` | Pass algebraically.  \(\eta_L,\Phi,W,q_X\), literal zero extension, the inclusive cone, and oddness are retained.  Even \(D\) is routed through \(d_2\), and even \(t\) through \(v\). |
| `missing_L_half_power` | Fail for the audited common-test route, exactly.  Its controls-only output is \(L^{2+o(1)}\), versus target \(L^{3/2+o(1)}\). |
| `self_return_and_full_divisor_exclusions` | Pass as exclusions.  No smooth scalar B-process, complementary-divisor switch, or \(r_2/4\) completion is used; the Round-137 self-return and circular-complement barriers remain in force. |
| `hard_top_owner_and_downstream_scope` | Pass.  No assertion transfers to terminal TOP, BAL, UNBAL, M9-M1, another endpoint packet, all M2, M9, or a global exponent. |

No numerical, symbolic, metric-in-center, or web experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the permitted context:

- `protocol.md`;
- `state/proof_obligations.yml` at the frozen graph hash in the brief;
- `state/active_campaign.yml`;
- `strategy/round161_m2_hard_top_radical_frequency_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_frequency_seed.md`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md`; and
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`.

The only inherited mathematical inputs are the exact hard-TOP product
identity, the accepted square owner, the coefficient energy and
fixed-radical \(\ell^1\) estimate, and the Round-137 self-return/full
divisor exclusions.  The radical-incidence formula, long-channel sum,
squarefree-radical independence proof, complete shared-index collision
audit, and projective/Bessel diagnostic are derived here.

## 7. Recommended state effect

**Recommended effect: promote the two exact sublemmas and retain the main
target open; classify the attempted generic coupling route as a scoped
no-go.**

More precisely, promote after seam review:

1. the owner-complete bound (3.1) for \(D\le CL\), hence every fixed
   \(t\ge\tau\sqrt L\) sector;
2. the exact collision theorem: at most one unequal base-frequency edge,
   one underlying radical pair at atom level, and mutual exclusion with
   the unique rational channel; and
3. the rank-one \(t=1\) projective/Bessel obstruction to any theorem
   using only coarse support, the accepted positive controls, exact
   collision sparsity, and arbitrary row factors.

Do not promote a full target or a strict polynomial \(L\)-range.  Revise
the Round-161 candidate kernel so that the unresolved coupling is
explicitly restricted to \(D\gg L\), \(t\ll\sqrt L\), beginning with the
literal physical direction (4.1).  A later attack must prove an
actual-coefficient property of (3.6)/(1.1) that excludes the diagnostic
array (3.10); another coefficient-uniform common-test, positive tensor
norm, exact-collision classification, or one-dimensional self-return
does not meet that requirement.

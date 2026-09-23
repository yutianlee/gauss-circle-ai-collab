# Round 177 statement-only blind alias-energy rederivation

## 1. Result: a strict stationary-conductor lemma and an exact no-go

The statement-only data prove one owner-complete strict sector, but they do
not prove the full low-cross-gcd complement.

After the anchor DFT, put

\[
 q(n):=\frac{u}{(u,n)},\qquad
 Q(k,n):=\frac{q(n)}{(q(n),k)}.
\]

Thus \(q(n)\) is the inverse-residue modulus and \(Q(k,n)\) is the
conductor of \(e(k\bar v n/u)\). The complete subaggregate with
\(Q(k,n)=1\), summed over every alias and both opposing orientations, is
bounded at the needed fixed-\((\kappa,u)\) scale:

\[
 \sum_{k\bmod u}|c_u(k)|
 \sum_{\substack{\text{both orientations and all literal }(v,n,t)\\
                  Q(k,n)=1}}
 |W_{\kappa,u}^{\pm}(v,n,t)|
 \ll \mathfrak a_{\kappa,u}L\,\tau(u)\log(2u),
 \qquad
 \mathfrak a_{\kappa,u}:=\sup |W_{\kappa,u}^{\pm}|.
 \tag{1.1}
\]

Here \(W\) is the complete literal amplitude after removal of
\(E_u(\pm\bar v n)(-1)^t\). With the bounded literal weights and harmless
\(X^\varepsilon\) losses included in \(\mathfrak a_{\kappa,u}\), (1.1)
sums to \(O(L^2X^\varepsilon)\) over the low-\(\kappa\) complement. It
includes \(k=0\) and all completely imprimitive aliases and uses no
squarefree, selector, endpoint, or orientation regularity.

The exact obstruction is the complementary primitive/nonconstant-conductor
part, already for a constant-size near-half alias and \((u,n)=1\). Its DFT
coefficient is of constant size, while its raw fixed-\((\kappa,u)\)
capacity is

\[
 \kappa u^2\asymp \frac{L^2}{\kappa}=Lu.
\]

The required local scale is \(L\), so this part needs a full factor \(u\)
of cancellation. Reciprocal \(TT^*\) supplies only the usual square-root
scale without more coefficient structure, and arbitrary selector
variation can restore the full capacity. More precisely, if the complete
literal amplitude is treated as an arbitrary bounded array, the resulting
linear functional has exact \(\ell^\infty\)-operator norm equal to its raw
weighted mass. A dechirped false array attains that norm, and a zero-one
parity selector retains at least half of it.

Therefore no proof using only support, \(|\lambda_N(d)|\leq1\), and a
coefficient-blind reciprocal large sieve can establish the desired hybrid
theorem. This is a proof-mechanism no-go, not a lower bound for the literal
K17a aggregate. The literal theorem could still be true, but its proof must
use an exact algebraic property of the canonical selector and profiles
that is absent from the statement-only packet.

## 2. Exact statements and hypotheses

For an orientation \(\eta\in\{+1,-1\}\), write

\[
 a_\eta(v,n):=[\eta\bar v n]_u,
\]

and let \(\mathcal I_{\kappa,u}^{\eta}\) be the literal zero-extended set of
triples \((v,n,t)\) satisfying every shell, squarefree, determinant,
original-gcd, displacement, parity, endpoint, and selector condition.
All such restrictions are kept inside \(\mathcal I\) and \(W\). Define
the orientation-unseparated alias block

\[
 B_{\kappa,u}(k)
 :=\sum_{\eta=\pm1}
   \sum_{(v,n,t)\in\mathcal I_{\kappa,u}^{\eta}}
   W_{\kappa,u}^{\eta}(v,n,t)(-1)^t
   e\!\left(\frac{k a_\eta(v,n)}u\right),
 \tag{2.1}
\]

and the exact DFT-recombined block

\[
 \mathcal A_{\kappa,u}:=\sum_{k\bmod u}c_u(k)B_{\kappa,u}(k).
 \tag{2.2}
\]

The only counting hypotheses used in (1.1) are exactly those in the
packet:

\[
 \#\{v\}=O(u),\qquad n\text{ lies in an interval of length }O(u),
 \qquad \#\{t\text{ in a fibre}\}=O(\kappa),
 \qquad \kappa u\asymp L.
 \tag{2.3}
\]

Every literal restriction can only decrease these absolute counts.

The weakest direct dyadic statement sufficient for the target is the
following signed \(L^1\) theorem. If

\[
 \mathcal D_K:=\{(\kappa,u):K\leq\kappa<2K,\ 
                  \kappa<\delta L,\ u\asymp L/\kappa\},
\]

then

\[
 \boxed{\quad
 \sum_{(\kappa,u)\in\mathcal D_K}|\mathcal A_{\kappa,u}|
 \ll L^2X^\varepsilon
 \quad}
 \tag{H1}
\]

for every dyadic \(K\) implies the required complement after absorbing
the number of dyadic intervals. A natural, stronger but checkable hybrid
energy surrogate is

\[
 \boxed{\quad
 \sum_{(\kappa,u)\in\mathcal D_K}|\mathcal A_{\kappa,u}|^2
 \ll L^3X^\varepsilon.
 \quad}
 \tag{H2}
\]

Indeed \(\#\mathcal D_K=O(L)\), so (H2) implies (H1) by
Cauchy--Schwarz. The pointwise recombined estimate
\(|\mathcal A_{\kappa,u}|\ll LX^\varepsilon\) implies (H2). The stronger
aliaswise estimate \(|B_{\kappa,u}(k)|\ll LX^\varepsilon\) also suffices,
because \(\|c_u\|_1\ll\log(2u)\). These statements keep \(v,n,t\), every
alias, and both orientations together until the asserted saving.

The coefficient-blind no-go is exact. Given a finite set \(\mathcal I\),
nonnegative masses \(b_i\), and unit phases \(p_i\), set
\(\sigma_i=E_u(a_i)(-1)^{t_i}\in\{\pm1\}\). Then

\[
 \sup_{|z_i|\leq1}
 \left|\sum_{i\in\mathcal I}b_i z_i p_i\sigma_i\right|
 =\sum_{i\in\mathcal I}b_i.
 \tag{NG}
\]

Thus no \(o(\sum b_i)\) estimate is uniform over bounded amplitudes.
After dechirping \(p_i\), even a zero-one selector can retain at least
half the mass by selecting the more massive of the two sign classes
\(\sigma_i=+1\) and \(\sigma_i=-1\).

## 3. Proof and derivation

### 3.1 Exact summation ledger

On \(\mathcal D_K\), put \(U\asymp L/K\). There are \(O(K)\) choices of
\(\kappa\), \(O(U)\) choices of \(u\) for each \(\kappa\), and hence

\[
 \#\mathcal D_K=O(KU)=O(L).
\]

A fixed pair has \(O(U)\) values of \(v\), \(O(U)\) values of \(n\), and
\(O(K)\) fibre sites, so its raw capacity is

\[
 O(KU^2)=O(L^2/K)=O(LU).
 \tag{3.1}
\]

The dyadic raw capacity is \(O(L^3/K)\), whereas the allowed dyadic mass is
\(O(L^2X^\varepsilon)\). Thus the needed average saving is \(L/K=U\),
equivalently the local scale is \(L\). Summing an
\(O(LX^\varepsilon)\) local estimate gives

\[
 \sum_{\kappa<\delta L}O(L/\kappa)\,O(LX^\varepsilon)
 \ll L^2X^\varepsilon\log(2L),
\]

and logarithms are absorbed by reassigning \(\varepsilon\). This verifies
the sufficiency ledger independently of a pointwise fixed-\(v\) estimate.

### 3.2 The DFT, the zero alias, and the near-half packet

Substitution of the exact anchor DFT gives (2.2). Its coefficient
magnitudes are

\[
 |c_u(k)|=\frac1{u|\cos(\pi k/u)|}.
 \tag{3.2}
\]

In particular, \(c_u(0)=1/u\). Using (3.1), the \(k=0\) contribution is
absolutely bounded by

\[
 |c_u(0)B_{\kappa,u}(0)|
 \ll \frac1u\frac{L^2}{\kappa}\mathfrak a_{\kappa,u}
 \asymp L\mathfrak a_{\kappa,u}.
 \tag{3.3}
\]

Hence \(k=0\) is target-safe without oscillation.

For odd \(u\), let \(k_\pm=(u\pm1)/2\). Then

\[
 |c_u(k_\pm)|
 =\frac1{u\sin(\pi/(2u))},
 \qquad \frac2\pi\leq |c_u(k_\pm)|\leq1.
 \tag{3.4}
\]

Thus the constant-size near-half packet cannot receive the \(1/u\)
normalization that saves \(k=0\); it must gain a genuine factor \(u\)
from the hybrid sum.

### 3.3 Proof of the stationary-conductor strict sector

Let \(g_k=(k,u)\). Since \(q(n)\mid u\), the condition \(Q(k,n)=1\) is

\[
 q(n)\mid k
 \iff q(n)\mid g_k
 \iff \frac{u}{g_k}\mid n.
 \tag{3.5}
\]

In one complete residue system modulo \(u\), (3.5) has exactly \(g_k\)
solutions. An interval of length \(O(u)\) therefore contains \(O(g_k)\)
such \(n\)'s. For each of them, (2.3) gives \(O(u\kappa)=O(L)\) choices of
\((v,t)\), including both orientations up to a constant. The absolute
mass for alias \(k\) in this sector is consequently

\[
 O\!\left(\mathfrak a_{\kappa,u}L g_k\right).
 \tag{3.6}
\]

It remains to sum the exact coefficient cost. Represent \(k\) by
\(0\leq k<u\) and put \(j_k=|2k-u|\). Since \(u\) is odd, \(j_k\) is odd,

\[
 |\cos(\pi k/u)|=\sin\!\left(\frac{\pi j_k}{2u}\right),
 \qquad g_k=(j_k,u).
\]

The inequality \(\sin x\geq2x/\pi\) on \([0,\pi/2]\) gives
\(|c_u(k)|\leq1/j_k\). The value \(j=u\) occurs once and every odd \(j<u\)
occurs twice. Hence

\[
 \begin{aligned}
 \sum_{k\bmod u}|c_u(k)|g_k
 &\leq 1+2\sum_{\substack{1\leq j<u\\j\ {\rm odd}}}
             \frac{(j,u)}j \\
 &=1+2\sum_{d\mid u}\frac{\varphi(d)}d
       \sum_{\substack{\ell<u/d\\\ell\ {\rm odd}}}\frac1\ell \\
 &\ll \tau(u)\log(2u).
 \end{aligned}
 \tag{3.7}
\]

Here \((j,u)=\sum_{d\mid(j,u)}\varphi(d)\) was used. Combining (3.6) and
(3.7) proves (1.1).

For completeness, if \(h=(u,n)\), the inverse-residue modulus is \(q=u/h\).
Reduction of a complete unit system modulo \(u\) to one modulo \(q\) has
multiplicity \(\varphi(u)/\varphi(q)\). If \(g=(q,k)\), the additive
character has conductor \(q/g\), and reduction to that conductor has
total multiplicity \(\varphi(u)/\varphi(q/g)\). Formula (3.5) is the exact
conductor-one endpoint of this hierarchy.

### 3.4 Both orientations have an exact self-return, not automatic cancellation

Put \(a=[\bar v n]_u\) and \(q_0=(av-n)/u\). In the plus orientation,

\[
 (s_+(t),w_+(t))=(a+ut,q_0+vt).
\]

If \(a\ne0\), then \([-\bar v n]_u=u-a\), and the minus orientation has

\[
 (s_-(t),w_-(t))=(u-a+ut,v-q_0+vt).
\]

Therefore

\[
 (s_-(-t-1),w_-(-t-1))=-(s_+(t),w_+(t)).
 \tag{3.8}
\]

Moreover \(E_u(u-a)=-E_u(a)\), while
\((-1)^{-t-1}=-(-1)^t\), so

\[
 E_u(-a)(-1)^{-t-1}=E_u(a)(-1)^t.
 \tag{3.9}
\]

If \(a=0\), the corresponding map is \(t\mapsto-t\), and
(3.8)--(3.9) again hold with the evident interpretation. Thus reversal of
the displacement preserves, rather than reverses, the character sign.
Where both zero-extended fibres contain paired sites, an ordered-pair term
and its reversed/conjugate term can add in the outer real part. Endpoint
truncation can destroy the pairing, but it cannot justify cancellation.

### 3.5 Exact obstruction to a coefficient-blind large-sieve proof

For \(h=(u,n)\), write \(n=hn_0\) and \(q=u/h\). Then

\[
 e\!\left(\frac{k\bar v n}{u}\right)
 =e\!\left(\frac{k n_0\bar v}{q}\right),
 \tag{3.10}
\]

where \((n_0,q)=1\); its conductor is \(q/(q,k)\). The unresolved clean
case is \(h=1\) and \(k=k_\pm\), for which \((k,u)=1\), so the conductor is
exactly \(u\).

Even in the ideal complete primitive model, the reciprocal matrix

\[
 T_{n,v}=e(k n\bar v/u),
 \qquad n\bmod u,\quad v\in(\mathbb Z/u\mathbb Z)^\times,
\]

satisfies

\[
 \sum_{n\bmod u}T_{n,v}\overline{T_{n,v'}}
 =u\,1_{v=v'}.
 \tag{3.11}
\]

Thus its exact operator norm is \(\sqrt u\). A single \(TT^*\) estimate on
factorized unit-scale \(v\)- and \(n\)-coefficients is at the
\(u^{3/2}\) scale. With \(O(\kappa)\) uncancelled fibre sites this becomes

\[
 \kappa u^{3/2}=L\sqrt u,
\]

already a factor \(\sqrt u\) above the required \(L\). The off-diagonal in
(3.11) is zero; the diagonal alone is too large. With a genuinely
two-dimensional selector-dependent coefficient, one cannot even form the
factorized bilinear operator.

The stronger obstruction is (NG): the triangle inequality gives the upper
bound, and equality is attained by

\[
 z_i=\overline{p_i\sigma_i}.
\]

It works simultaneously on both orientations and on whatever endpoints,
squarefree progressions, and zero-extended support remain. It also has a
vertex-factorized false-coefficient realization for the oscillations
displayed in the packet: replacing the literal coefficient by

\[
 \lambda_N^{\rm false}(d)=\chi_4(d)e(-J\sqrt N)
\]

on the allowed atoms makes \(u_L(d,m)=1\). Hence the character and
square-root phases cannot yield a coefficient-uniform theorem. This array
deliberately erases the canonical selector and profiles and is not a claim
about the literal coefficient.

Finally, fibre alternation alone is quantitatively insufficient. Even if
the remaining amplitude were constant in \(t\), a consecutive alternating
sum leaves at most one endpoint per \((v,n)\), hence \(O(u^2)\) locally.
This is at most \(L=\kappa u\) only when \(\kappa\geq\sqrt L\). For the
smaller-\(\kappa\) range, the zero-one selector \(1_{t\ {\rm even}}\)
restores \(\asymp\kappa\) mass on every nontrivial fibre. Thus boundedness
without selector variation control gives back the raw scale
\(\kappa u^2=Lu\).

## 4. First doubtful or unproved step

The first unproved step is an estimate for the actual literal amplitude in
the primitive near-half sector, for example a pointwise or dyadically
averaged version of

\[
 \sum_{\eta=\pm1}
 \sum_{\substack{(v,n,t)\in\mathcal I_{\kappa,u}^{\eta}\\(u,n)=1}}
 W_{\kappa,u}^{\eta}(v,n,t)(-1)^t
 e\!\left(\frac{k_\pm\eta\bar v n}{u}\right)
 \ll LX^\varepsilon.
 \tag{4.1}
\]

The exact dyadic requirement is only (H1), so exceptional local blocks are
allowed, but the packet supplies no coherence across \(u\) or \(\kappa\)
with which to prove that average either. A proof of (4.1) or (H1) needs at
least one presently absent input: an explicit factorization or bounded
variation theorem for the canonical selector, a pairing identity for its
two parity branches and orientations including endpoints, a nonstationary
estimate for the combined square-root and \(t/2\) phase with literal
amplitudes, or a cross-modulus large sieve whose diagonal is smaller after
those exact coefficient constraints are imposed. Since the selector is not
defined in the packet and no regularity may be assumed, none of these
inputs can be derived statement-only.

## 5. Required controls and outcomes

- **exact_low_cross_gcd_complement:** The obstruction already occurs in
  the clean stratum \((u,n)=1\), hence \((d,d')=1<\gamma L\), with \(n\)
  above the non-polylogarithmic determinant cutoff whenever that interval
  is nonempty. The positive lemma retains the cutoff as a restriction.

- **both_opposing_orientations:** They are summed inside (2.1), before the
  alias modulus is estimated. Equations (3.8)--(3.9) show exact
  sign-preserving self-return under displacement reversal, so cancellation
  between orientations needs an additional literal amplitude identity.

- **anchor_DFT_and_near_half_alias:** The DFT is recombined exactly in
  (2.2). Equations (3.3)--(3.4) distinguish the harmless \(1/u\) zero alias
  from the constant-size near-half packet.

- **hybrid_v_n_t_capacity:** The independent count (3.1) is
  \(\kappa u^2=Lu=L^2/\kappa\). The dyadic ledger shows that a factor \(u\)
  is missing.

- **primitive_modulus_and_gcd_multiplicity:** Equation (3.10) gives the
  inverse-residue modulus \(u/(u,n)\), its further additive conductor, and
  the exact unit-lift multiplicities. The conductor-one multiplicity is
  counted exactly by (3.5).

- **k_zero_and_imprimitive_aliases:** The \(k=0\) block is locally
  \(O(LX^\varepsilon)\) by (3.3). More generally every term whose reduced
  additive conductor is one is target-safe after summing all imprimitive
  aliases by (3.7). Nontrivial reduced conductors remain open.

- **incomplete_v_interval:** The positive lemma only uses
  \(\#v=O(u)\), so it is insensitive to incomplete intervals. Complete
  orthogonality (3.11) does not transfer automatically to a literal
  interval; completion adds boundary/Fourier weights and cannot repair the
  missing power without coefficient structure.

- **large_sieve_diagonal_offdiagonal:** In the complete primitive control,
  (3.11) has zero off-diagonal but exact \(\sqrt u\) operator norm. The
  diagonal scale is \(L\sqrt u\) after uncancelled fibres, so improving
  only off-diagonal estimates is insufficient.

- **squarefree_Mobius_progressions:** The proof of (1.1) treats squarefree
  atoms as a subset and is therefore exact. In the unresolved sector,
  expanding \(\mu^2(x)=\sum_{a^2\mid x}\mu(a)\) creates progressions but
  leaves a principal, nonoscillatory component. The dechirped false array
  can be supported only on surviving squarefree atoms, so squarefreeness
  alone does not defeat (NG).

- **parity_and_two_adic_branches:** Odd \(u\) is used in (3.2), (3.7), and
  (3.9). Both literal parity branches may be included in \(\mathcal I\);
  the positive estimate is branchwise absolute. The hostile selector
  \(1_{t\ {\rm even}}\) shows why unproved branch cancellation cannot be
  used.

- **selected_and_no_pair_rows:** Arbitrary zero rows only reduce (1.1). In
  the hostile algebraic control, selecting the more massive character-sign
  class retains at least half of the dechirped mass, while no-pair rows are
  zero. This falsifies selector-blind cancellation, not the canonical
  selector.

- **short_cross_gcd_fibres:** One residual endpoint per \((v,n)\) costs
  \(u^2\), which exceeds the local budget for \(\kappa<\sqrt L\). Selecting
  one \(t\)-parity restores a constant proportion of the full
  \(\kappa u^2\) fibre capacity.

- **stationary_and_dechirped_modes:** All reciprocal-stationary
  conductor-one modes are safe by (1.1). The false dechirper in (NG)
  exactly cancels reciprocal, \(t/2\), and square-root phases and restores
  raw mass, showing that nonstationarity must be proved for the literal
  coefficient rather than assumed.

- **endpoints_and_zero_extension:** They are part of \(\mathcal I\) from
  the outset. The positive bound survives arbitrary deletion. The no-go
  maximizer works on the surviving finite set, and the \(u^2\) one-endpoint
  cost shows that boundary terms are not automatically lower order.

- **false_coefficient_controls:** The selector-erased vertex array
  \(\lambda_N^{\rm false}(d)=\chi_4(d)e(-J\sqrt N)\) and the zero-one
  parity selector both restore capacity. They invalidate any proof that
  would also prove the unsigned or adversarial analogue; they are not a
  lower bound for the literal aggregate.

- **outer_real_part:** In (NG) every retained summand can be made positive
  real. Equations (3.8)--(3.9) likewise show that reversed orientations can
  enter as conjugates with equal real parts. Taking the outer real part is
  not a generic saving.

- **residual_only_owner_scope:** The proved statement concerns only the
  conductor-one alias subaggregate of the stated low-cross-gcd K17a
  complement. It makes no claim about broader M9 owners, the pointwise
  bridge, endpoint uniformity outside this residual, or any exponent.

The hostile controls are finite algebraic identities. No numerical
experiment was used, and no false array is interpreted as evidence that
the literal aggregate is large.

## 6. Dependencies and exact artifacts used

This was a statement-only derivation. The only artifacts read were:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/briefs/blind_alias_energy_rederivation.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/blind_statement.md.

No proof graph, strategy file, prior report, kernel, review, control,
synthesis, source card, sibling work, conductor analysis, web source, or
computation was used. Analytical/algebraic allocation was 100%; numerical
allocation was 0%.

## 7. Recommended state effect

**Revise.** Retain the full low-\(\kappa\) complement as open and reject a
coefficient-blind reciprocal-large-sieve or \(TT^*\) claim as sufficient.
After an independent normalization/seam check, promote only the strict
conductor-one lemma (1.1), including \(k=0\), as candidate progress. The
next admissible proof attempt must expose and use the exact canonical
selector/profile algebra in the primitive near-half sector, or prove the
dyadic signed estimate (H1) by a mechanism whose diagonal and endpoint
costs are explicitly below the scales recorded above.

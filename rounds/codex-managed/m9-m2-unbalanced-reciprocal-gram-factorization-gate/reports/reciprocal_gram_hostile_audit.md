# Reciprocal Gram hostile seam audit

## 1. Result: scoped reduction and Gram/factorization no-go

The real-centre flat-smooth row can be moved to an integer centre without
the false termwise charge.  More generally, after freezing every amplitude
at \(X\), its physical kernel is Lipschitz in the prescribed centre:

\[
 |\mathscr R_C^\sharp-\mathscr R_{C'}^\sharp|
 \ll_{\varepsilon,q,W}(1+|C-C'|)X^\varepsilon
 \tag{123.H1}
\]

for \(C,C'\asymp X\).  Thus \(N=\lfloor X\rfloor\) costs
\(O_\varepsilon(X^\varepsilon)\).  This uses a uniform Schwartz-tail
divisor layer cake and not cancellation subsequently obtained from the
row.  Directly changing each reciprocal phase instead costs as much as
\(K=XL/D^2\) and is not a uniform proof.

The remaining proposed closure fails at its norm interface.  Weighted
\(k\)-Cauchy gives a sufficient positive Gram bound, not an equivalent
form of the scalar target.  On a nondegenerate cell the Gram diagonal is

\[
 \mathcal D_N\asymp R={X\over D}>X^{1/2},
 \tag{123.H2}
\]

so this route requires the complete actual-sign off-diagonal identity

\[
 \mathcal O_N=-\mathcal D_N+O_\varepsilon(X^{1/2+\varepsilon}).
 \tag{123.H3}
\]

No exact-collision count, unsigned alias bound, or character formula in
the packet proves (123.H3).  The alias identity and the two-adic sign are
correct, but they are a reparametrization of the original ordered pairs.
The near window has width \(X/L\), while the exact factorization is only
one defect slice.  The zero alias is additionally degenerate: for \(j=0\)
the product equation is \(0=0\) and contains no information about a
nonzero near defect.

A lawful \(k\)-van der Corput shift with
\(H\asymp X^{1/2}/D\) lowers only its \(h=0,r=s\) contribution to
\(R/H\asymp X^{1/2}\).  Its other shifted correlations retain shifted
profiles, endpoints, an extra phase \(e(Nh/r)\), and the complete signed
off-diagonal.  At full shift length it returns to a full-scale positive
norm of the Round-118 row at the original product resolution; at the
proposed shorter length it is a stronger positive local-packet norm with a
broader product window.  It supplies no intrinsic saving.

Likewise, one may choose an integer centre of exact two-adic order
\(Q\asymp X^{1/4}\) at target distance from \(X\).  This forces
\(2Q\mid j\) only on the exact-defect slice.  The near-defect congruence is
automatic for every original odd pair and the displayed sign is still
exactly \(\chi_4(r)\chi_4(s)\).  This relabels the row after spending a
target-sized perturbation; it does not reduce the live near aliases or the
Gram diagonal.

Therefore the maximal safe outcome is (123.H1), the exact Gram and alias
normalizations below, and a scoped no-go for obtaining a target estimate
from positive same-\(k\) Gram normalization, exact-product counting,
two-adic relabeling, or van der Corput shifting alone.  The smallest
unavoidable scalar survivor remains the complete phase-integerized joint
\((r,k)\) row before \(k\)-Cauchy or the \(k\)-triangle.  If the Gram route
is voluntarily imposed, its smallest survivor is the full signed diagonal
plus every ordered off-diagonal; if the shifted route is imposed, it is
the full signed \((h,r,s,k)\) correlation written in Section 3.

## 2. Exact statement and hypotheses

Let \(X\ge 2\), \(D=X^\delta\), \(L=X^\ell\),

\[
 {1\over4}\le\delta<{1\over2},\qquad
 0\le\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463,
\]

and put

\[
 R={X\over D},\qquad K={XL\over D^2}.
\]

Fix one nondegenerate flat smooth strict-UNBAL cell.  The functions \(W\)
and \(q_L\) are the literal fixed profiles, the \(r\)-support is
\(r\asymp R\), the sampled \(k\)-support has length \(\asymp K\), and all
amplitudes and the denominator \(4X\) remain frozen at the original real
\(X\).  The smooth profile hypotheses used below are the uniform finite
difference bounds inherited from a fixed compactly supported smooth
profile and, equivalently for the physical kernel,

\[
 |\mathcal Q_L'(y)|\ll_A
 L(1+L|y|)^{-A}\qquad(A\ge0).
 \tag{123.H4}
\]

No sharp, starred, clipped, hard, arithmetic-owner, or transition kernel
is included.

For a real prescribed centre \(C\asymp X\), define the phase-only row

\[
 \mathscr R_C^\sharp
 =\sum_{r\ \mathrm{odd}}\chi_4(r)W_r
   \sum_k {q_{r,k}\over k}e(Ck/r),
 \quad
 W_r=W\!\left({X\over rD}\right),
 \quad
 q_{r,k}=q_L\!\left({4Xk\over r^2}\right).
 \tag{123.H5}
\]

The exact smooth Poisson identity represents it, up to the already fixed
common normalization, by

\[
 \mathscr P_C
 =\sum_{r\ \mathrm{odd}}\chi_4(r)W_r
   \sum_{d\in\mathbb Z}
   \mathcal Q_L\!\left({r(C-rd)\over4X}\right).
 \tag{123.H6}
\]

Under these hypotheses the following are safe.

1. The centre-stability bound (123.H1) holds for
   \(|C-X|+|C'-X|=o(X)\), in particular for \(C=X\),
   \(C'=\lfloor X\rfloor\), and for the target-distance centre constructed
   in Section 3.

2. With \(N=\lfloor X\rfloor\),

   \[
    B_k=\sum_{r\ \mathrm{odd}}\chi_4(r)W_rq_{r,k}e(Nk/r),
    \qquad
    \mathscr R_N^\sharp=\sum_k{B_k\over k},
   \]

   one has only the one-way implication

   \[
    |\mathscr R_N^\sharp|^2
    \le \left(\sum_{k\asymp K}{1\over k}\right)
       \mathcal G_N
    \ll \mathcal G_N,
    \qquad
    \mathcal G_N=\sum_{k\asymp K}{|B_k|^2\over k}.
    \tag{123.H7}
   \]

3. The literal kernel in the ordered-pair expansion is

   \[
    \mathcal K_{r,s}
    =\sum_k {q_{r,k}\overline{q_{s,k}}\over k}
      e\!\left(Nk\left({1\over r}-{1\over s}\right)\right),
    \tag{123.H8}
   \]

   and \(W_r\overline{W_s}\), rather than an unconjugated product, is
   required unless the fixed profiles have already been declared real.
   Uniformly, including support overlap and smooth edges,

   \[
    |\mathcal K_{r,s}|\ll_A
    \left(1+K\left\|N\left({1\over r}-{1\over s}\right)\right\|\right)^{-A}.
    \tag{123.H9}
   \]

   This is a smooth tail estimate, not a rectangular cutoff.

4. For the unique nearest integer \(j\) to
   \(N(1/r-1/s)\), put \(E=N(s-r)-jrs\).  Then all algebra, congruences,
   signs, and exceptional branches are exactly those derived in Section 3.

The theorem does not assert (123.H3), a target bound for
\(\mathscr R_N^\sharp\), or a reverse implication from the scalar target
to the Gram target.

## 3. Proof or derivation

### 3.1 Physical-kernel centre stability

Differentiate (123.H6) while keeping \(X,W_r,q_L\), and \(4X\) fixed:

\[
 {\partial\over\partial C}\mathscr P_C
 =\sum_{r\ \mathrm{odd}}\chi_4(r)W_r
   \sum_d {r\over4X}
   \mathcal Q_L'\!\left({r(C-rd)\over4X}\right).
\]

On the support of \(W_r\), \(r/X\asymp D^{-1}\).  Group the nonzero
products by \(n=rd\) and use the elementary divisor bound.  From
(123.H4), for \(A\) large,

\[
 \left|{\partial\over\partial C}\mathscr P_C\right|
 \ll {L\over D}
 \sum_{n\ne0}\tau(|n|)
 \left(1+c{L\over D}|C-n|\right)^{-A}
 +O_A(X^{-A})
 \ll_\varepsilon X^\varepsilon.
 \tag{123.H10}
\]

The last term includes \(d=0\) and negative-product tails; their distance
from \(C\asymp X\) makes them rapidly decreasing.  The sum in (123.H10)
has effective length \(D/L\), and its prefactor is \(L/D\).  It also counts
all tied or boundary product levels with their literal divisor
multiplicity.  Integrating (123.H10) between \(C\) and \(C'\) proves
(123.H1).  No post-cancellation capacity has been used.

By contrast, the direct reciprocal comparison gives

\[
 \sum_{r\asymp R}\sum_{k\asymp K}{1\over k}
 \left|e((X-N)k/r)-1\right|
 \ll |X-N|K.
 \tag{123.H11}
\]

This can exceed \(X^{1/4}\) in the allowed region.  The estimate
\(|X-N|k/r\ll L/D\) therefore cannot be multiplied by the number of
terms or by a product capacity obtained only after Poisson cancellation.

### 3.2 Exact weighted Gram and its diagonal burden

Cauchy with factors \(k^{-1/2}\) gives (123.H7).  Expanding it with the
necessary conjugates gives

\[
 \mathcal G_N
 =\sum_{r,s\ \mathrm{odd}}
   \chi_4(r)\chi_4(s)W_r\overline{W_s}\mathcal K_{r,s}.
 \tag{123.H12}
\]

Here
\(\mathcal K_{s,r}=\overline{\mathcal K_{r,s}}\); reality and
nonnegativity arise only after all ordered pairs are assembled.  On a
nondegenerate interior cell,

\[
 \mathcal D_N
 =\sum_{r\ \mathrm{odd}}|W_r|^2
   \sum_k {|q_{r,k}|^2\over k}
 \asymp R=X^{1-\delta}.
 \tag{123.H13}
\]

The square target is \(X^{1/2+\varepsilon}\).  For every fixed
\(\delta<1/2\), (123.H13) is larger by the power
\(X^{1/2-\delta}\).  Consequently a Gram proof must establish (123.H3)
before any off-diagonal absolute value.  The scalar target does not imply
this stronger norm: Cauchy has no reverse direction, and cancellation
between different \(k\)'s was discarded in forming \(\mathcal G_N\).

For (123.H9), extend the smooth sampled amplitudes by zero.  Their support
intersection has length \(O(K)\) and

\[
 \left\|\Delta_k^m
 \left({q_{r,k}\overline{q_{s,k}}\over k}\right)
 \right\|_{\ell^1_k}\ll_m K^{-m}.
\]

Repeated discrete summation by parts and the trivial \(\ell^1\) bound
give (123.H9).  Smooth vanishing at the profile edges is essential; a hard
cutoff would create boundary terms.  When \(K\asymp1\), (123.H9) is only
the corresponding \(O(1)\) bound and provides no localization.  In the
strict fixed-exponent region \(K=X^{1+\ell-2\delta}\to\infty\), but the
uniform formulation still handles the short case.

### 3.3 Alias orientation, factors, congruences, and all parity branches

Because

\[
 N\left({1\over r}-{1\over s}\right)
 ={N(s-r)\over rs}=j+{E\over rs},
\]

the orientation in the packet is correct.  A half-integer nearest-alias
tie is impossible: it would give

\[
 2N(s-r)=(2j+1)rs,
\]

whose left side is even and right side is odd.  Thus \(j\) is unique for
odd \(r,s\).  Significant smooth-kernel mass lies, after a lawful dyadic
tail decomposition, in

\[
 |E|\ll {rs\over K}X^\varepsilon
 \asymp {X\over L}X^\varepsilon,
 \qquad |j|\ll D.
 \tag{123.H14}
\]

Put

\[
 u=N-jr,\qquad v=N+js.
\]

Direct multiplication gives

\[
 uv-N^2=j\{N(s-r)-jrs\}=jE.
 \tag{123.H15}
\]

For \(j\ne0\), recovering positive odd \(r,s\) requires the literal
congruences

\[
 u\equiv N-j\pmod {2|j|},\qquad
 v\equiv N+j\pmod {2|j|},
 \tag{123.H16}
\]

as well as the support and positivity conditions.  Merely counting
factorizations of \(N^2+jE\) discards these conditions and all amplitudes.
On the principal window (123.H14),

\[
 {|jE|\over N^2}\ll X^{\delta-\ell-1+\varepsilon}=o(1).
\]

At least one of \(u,v\) is positive according to the sign of \(j\), so
both are positive there for large \(X\).  Outside that principal window,
negative-factor branches must be charged through the smooth tails rather
than silently deleted.

Write \(N=2^tN_0\), \(N_0\) odd.  Since \(s-r\) is even,

\[
 {jrs+E\over2^{t+1}}=N_0{s-r\over2}\in\mathbb Z.
\]

Multiplication or division by the odd number \(N_0\) does not change
parity, and therefore, for every sign of \(j\) and \(E\), including
\(t=0\),

\[
 \chi_4(r)\chi_4(s)
 =(-1)^{(s-r)/2}
 =(-1)^{(jrs+E)/2^{t+1}}.
 \tag{123.H17}
\]

Negative integer exponents cause no ambiguity.  If \(E=0\), then
\(2^{t+1}\mid j\) (with \(j=0\) allowed) and

\[
 \chi_4(r)\chi_4(s)=(-1)^{j/2^{t+1}}.
 \tag{123.H18}
\]

For a nonzero exact alias, write \(j=2^{t+1}m\).  Then

\[
 u=2^tu_0,\quad v=2^tv_0,\quad
 u_0v_0=N_0^2,
\]

where \(u_0,v_0\) are positive odd factors, and the oddness of \(r,s\)
requires

\[
 N_0-u_0\equiv v_0-N_0\equiv2|m|\pmod{4|m|}.
 \tag{123.H19}
\]

The exact character sign is \((-1)^m\).  This includes negative \(m\):
swapping \(r,s\) sends \((j,E)\) to \((-j,-E)\) and supplies the conjugate
ordered pair.

There are two exceptional boundaries.

- If \(j=0\), then \(E=N(s-r)\).  Exact defect means \(s=r\), the Gram
  diagonal.  For a near but nonzero defect,
  \(|s-r|\ll X^\varepsilon/L\), while (123.H15) becomes \(0=0\).
  Hence the factor map collapses the entire zero-alias strip and cannot be
  used to count it.

- Exact factor pairs are only the slice \(E=0\).  The allowed range
  \(|E|\ll X^{1+\varepsilon}/L\) contains polynomially many integer defect
  levels because \(\ell<1/4\).  For \(j\ne0\) they form an annulus of
  thickness \(O(DX^{1+\varepsilon}/L)\), not the divisor set of \(N^2\).
  Exact divisor bounds do not control the near window.

Finally, (123.H17) is not new oscillation.  It is the identity
\(\chi_4(r)\chi_4(s)=(-1)^{(s-r)/2}\) expressed in the coordinates forced
by \(E\).  Treating \(E\) as independent while retaining only its parity
would enlarge or alter the original pair set.

### 3.4 Lawful shifted \(k\)-Gram and why it does not close

Let \(z_k=B_k/k\), extend it by zero, and let \(N_K\asymp K\) be the
diameter of its support.  For every integer \(1\le H\le N_K\), the exact
van der Corput inequality is

\[
 \left|\sum_kz_k\right|^2
 \le {N_K+H-1\over H}
 \left\{C_0+2\Re\sum_{h=1}^{H-1}
 \left(1-{h\over H}\right)C_h\right\},
 \tag{123.H20}
\]

where

\[
 C_h=\sum_k z_{k+h}\overline{z_k}.
\]

The expression in braces is a positive average of exact short-\(k\)
squares.  Its ordered-pair expansion is

\[
 C_h=\sum_{r,s\ \mathrm{odd}}
 \chi_4(r)\chi_4(s)W_r\overline{W_s}
 e(Nh/r)
 \sum_k {q_{r,k+h}\overline{q_{s,k}}\over(k+h)k}
 e\!\left(Nk\left({1\over r}-{1\over s}\right)\right).
 \tag{123.H21}
\]

Thus the following data are compulsory: both denominators, the support
intersection of \(k\) and \(k+h\), the shifted sampled profile, zero
extension at both endpoints, and \(e(Nh/r)\).  Dropping any of them is not
the van der Corput inequality for the literal row.

The \(h=0,r=s\) contribution to the right side of (123.H20) is

\[
 \asymp {K\over H}\,R\sum_{k\asymp K}{1\over k^2}
 \asymp {R\over H}.
 \tag{123.H22}
\]

Taking

\[
 H\asymp{R\over X^{1/2}}={X^{1/2}\over D}
\]

makes (123.H22) target-sized, and this shift is lawful because

\[
 {K\over H}={X^{1/2}L\over D}>1.
 \tag{123.H23}
\]

This removes only the single \(h=0,r=s\) power obstruction.  It is neither
a sufficient estimate by itself nor an equivalence: the whole right side
of (123.H20) is another stronger sufficient positive norm.  Taking
absolute values over the \(H\) shifted same-\(r\) correlations can restore
size \(R\).  The base-\(k\) phase still has the alias \(j,E\) and factor
identity (123.H15), while the new phase \(e(Nh/r)\) is not a function of
\(jE\) and cannot be discarded.

If the shifted amplitudes were constant, the \(h\)-taper would be the
Fejér kernel at \(N/r\), selecting

\[
 |N-dr|\lesssim {r\over H}.
\]

For \(H\asymp X^{1/2}/D\) this is a product window of width
\(\asymp X^{1/2}\), broader than the literal Round-118 width \(D/L\).
For \(H\asymp K\) it has width \(r/K\asymp D/L\), the Round-118 product
resolution.  With the literal profiles, (123.H20) is the exact positive
short-packet-square norm, not an identity equating that norm to the scalar
square.  At shorter \(H\) it is stronger and broader; at full length it
repackages the original full-scale row and its physical selector without
introducing a new phase.  Alias factorization plus \(h\)-averaging has not
produced a capacity saving.

### 3.5 A target-distance, highly two-adic centre

Choose a power of two \(Q=2^t\asymp X^{1/4}\), and choose the nearest odd
integer \(M_0\) to \(X/Q\).  Then

\[
 M=QM_0,\qquad v_2(M)=t,\qquad |M-X|\le Q.
\]

The centre-stability lemma gives

\[
 |\mathscr R_X^\sharp-\mathscr R_M^\sharp|
 \ll_\varepsilon QX^\varepsilon
 \ll_\varepsilon X^{1/4+\varepsilon}.
 \tag{123.H24}
\]

For \(E_M=M(s-r)-jrs\), the exact formulas become

\[
 {jrs+E_M\over2Q}=M_0{s-r\over2}\in\mathbb Z,
 \qquad
 \chi_4(r)\chi_4(s)=(-1)^{(jrs+E_M)/(2Q)}.
 \tag{123.H25}
\]

On \(E_M=0\), necessarily \(2Q\mid j\) and the sign is
\((-1)^{j/(2Q)}\).  Exact equality \(2Q=2^{v_2(M)+1}\) requires the chosen
quotient \(M_0\) to be odd; mere divisibility \(Q\mid M\) would give the
stronger actual modulus \(2^{v_2(M)+1}\), not necessarily exactly \(2Q\).

For \(E_M\ne0\), (123.H25) is automatic from the definition for every odd
pair \(r,s\).  It does not remove a \(1/Q\) fraction of the original
pairs: the permitted residue of \(E_M\) changes with \(jrs\).  Nor is its
sign new; it equals the original character product term by term.  The
zero alias and Gram diagonal survive unchanged, and the near window still
has size \(X/L\gg Q\).  High two-adic divisibility thins only the already
divisor-bounded exact nonzero aliases.  Thus (123.H24) is a valid
target-sized transfer, but the proposed arithmetic benefit is a no-go.

### 3.6 Circularity and exact return

The proof of (123.H1) uses only the elementary divisor bound.  Completing
the truncated coefficient to \(r_2/4\), importing a complete circle
estimate for the near annulus, or filling missing complementary divisors
would cross owners and would be circular for the present M9 route.  Round
107 already shows that full-divisor completion is not the literal cell and
that the complete radial remainder returns the missing \(D/L\) capacity.

For \(j\ne0\), the map to \(u,v,E\) is merely an exact coordinate change
once (123.H16), support, and amplitudes are retained.  For \(j=0\) it is
not even injective.  Summing absolute factor counts loses the required
sign; retaining every sign and weight reconstructs (123.H12).  A second
reciprocal transform similarly returns the prescribed-centre wave.  The
same-k Gram, shifted Gram, and factor coordinates therefore do not supply
the noninvertible joint signed inequality required by the Round-118
survivor.

## 4. First doubtful or unproved step

The first invalid inference is to call the weighted Gram target
"equivalent" to the scalar \(X^{1/4+\varepsilon}\) target.  Equation
(123.H7) is one-way.  Its diagonal forces the much stronger cancellation
(123.H3), so failure of this Gram estimate would not refute the original
flat wave.

After the centre-stability, smooth-alias, factor, congruence, and parity
repairs above, the first genuinely unproved analytic assertion on the raw
Gram route is precisely (123.H3): cancellation of the complete diagonal
against the literal actual-sign off-diagonal, with no aliaswise,
residuewise, defectwise, or factorwise absolute value.  On the shifted
route it is the corresponding full expression (123.H20)-(123.H21), not
the target-sized \(h=0\) diagonal.  On the high-\(Q\) route it is the same
near-defect sum at centre \(M\); (123.H25) does not estimate it.

The smooth localization (123.H9) is valid only with the uniform profile
seminorms and exact zero extension stated in Section 2.  If those
hypotheses are omitted from a candidate statement, (123.H9) must be
retained as unproved rather than treated as a hard alias window.

## 5. Required control tests and outcomes

| Control | Verdict | Hostile outcome |
|---|---:|---|
| `literal_Round118_flat_wave` | PASS | (123.H5) keeps the literal \(q_L,W,\chi_4\), real \(X\) amplitudes, and one flat smooth owner. |
| `phase_integerization_physical_kernel` | PASS after repair | The differentiated physical kernel and the uniform rapid-tail divisor layer cake prove (123.H1), including product ties, \(d=0\), negative tails, support edges, and short \(K\). |
| `reciprocal_termwise_false_charge` | FAIL as a route | The honest unsigned reciprocal charge is \(O(K)\), not \(O(1)\); it is not uniformly target-safe. |
| `weighted_Gram_normalization` | PASS one-way / FAIL equivalence | The weights are exactly \(k^{-1/2}\cdot k^{-1/2}\), with conjugates as in (123.H8).  No reverse inequality is available. |
| `diagonal_capacity` | PASS obstruction | A nondegenerate diagonal is \(\asymp R=X/D>X^{1/2}\), forcing (123.H3). |
| `smooth_alias_localization` | PASS after repair | Fixed smooth profiles give (123.H9) by discrete summation by parts; it must be used as a tail bound, not a rectangular cutoff. |
| `alias_product_factorization` | PASS algebra / FAIL closure | Orientation and (123.H15) are exact; (123.H16) and the \(j=0\) degeneration are compulsory. |
| `two_adic_character_sign` | PASS | (123.H17)-(123.H19) hold for every \(t\ge0\), both signs of \(j,E\), and exact \(j=0\). |
| `exact_versus_near_collision` | FAIL proposed transfer | Exact aliases are divisor slices; the near window has \(X/L\) defect scale and cannot inherit an exact divisor bound. |
| `zero_and_negative_aliases` | PASS after repair | The reciprocal nearest alias has no half-tie; negative aliases are conjugate ordered branches; near \(j=0\) is a noninjective short strip and must be separate. |
| `signed_offdiagonal_aggregation` | FAIL | No bound for (123.H3) is proved.  Character-blind or unsigned aggregation is invalid. |
| shifted \(k\)-van der Corput | PASS normalization / FAIL gain | \(H\asymp X^{1/2}/D\le K\) makes only \(h=0,r=s\) target-sized.  Shifted profiles, endpoints, \(e(Nh/r)\), and all other correlations remain. |
| target-distance high-two-adic centre | PASS transfer / FAIL gain | A centre with \(v_2(M)=t\), \(2^t\asymp X^{1/4}\), exists at cost \(O(X^{1/4+\varepsilon})\); \(2^{t+1}\mid j\) helps only \(E=0\), while the near congruence is tautological. |
| Gauss-circle/full-divisor import | FAIL | A complete \(r_2/4\) or circle-discrepancy estimate changes the literal owner or assumes the downstream difficulty.  Only elementary divisor bounds were used. |
| `old_transform_return` | FAIL as new mechanism | Exact factor coordinates return the signed Gram; full shifted averaging returns the squared row; physical inversion returns the Round-118 selector. |
| `owner_and_downstream_scope` | PASS | The result is confined to one flat smooth strict-UNBAL cell and proves no complete UNBAL, M9-M2, M9, endpoint, or discrepancy exponent claim. |

## 6. Dependencies and exact artifacts used

This audit used exactly the selected context authorized by the brief:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the current statements and
  statuses of `M9-M2-smooth-unbalanced-three-quarter-estimate`,
  `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`,
  `M9-M2-unbalanced-flat-wave-curvature-envelope`,
  `M9-M2-physical-one-count-assembly`, `M9-M2`, `M9`, and
  `M9-endpoint-uniformity`;
- `state/active_campaign.yml` at Round 123 and starting graph
  `d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/derivation_packet.md`.

No Round-123 sibling report, external theorem, web source, or numerical
experiment was used.  The only counting input in the new perturbation
proof is the elementary divisor bound already present in the accepted
dependency graph.

## 7. Recommended state effect

Revise the Round-123 candidate rather than promote the target mechanism.

- Promote, as a scoped flat-smooth reduction if its fixed-profile
  seminorms are recorded explicitly, the centre-stability lemma
  (123.H1), including the target-distance integer-centre corollary.
- Record the conjugated weighted Gram, the diagonal obstruction, the
  unique-alias fact, factor congruences, all two-adic signs, the zero-alias
  degeneration, and the exact shifted-van-der-Corput normalization as
  proved normalization or obstruction evidence.
- Reject Gram-target equivalence, exact-factor counting as control of the
  near window, any unsigned analogue, an automatic high-\(Q\) saving, and
  any claim that shifted averaging or factor coordinates are themselves a
  new noninvertible gain.
- Retain `M9-M2-smooth-unbalanced-three-quarter-estimate` as open.  Its
  exact smallest scalar survivor is still the complete literal joint row
  (123.H5), before \(k\)-Cauchy or the \(k\)-triangle.  A continuation must
  prove a genuinely new actual-sign joint inequality for that row or a
  whole-selector inverse theorem controlling every complement.
- Make no status change to complete UNBAL, hard TOP, BAL,
  `M9-M2-physical-one-count-assembly`, `M9-M2`, either M1 route,
  endpoint uniformity, `M9`, the conditional bridge, the Gauss-circle
  quarter target, or any internal or external exponent.

# Blind hard-TOP actual-vector rederivation (Round 126)

## 1. Result: exact energy, a signed-spectral no-go, and an offset inverse theorem

The literal hard-TOP vector admits the exact matrix representation

\[
 \mathcal E_L^{\rm top}=\|B\xi\|_2^2=\xi^*G\xi,
 \qquad G=B^*B\geq0,
 \qquad \xi_h=\chi_4(h),
\tag{1.1}
\]

where

\[
 B_{m,h}={\bf1}_{\lceil h/4\rceil\leq m\leq h}
 a_{\rm end}(h,m)e(J\sqrt{hm}).
\tag{1.2}
\]

Its diagonal is counted once and is (O(L^2)), while direct rowwise
Cauchy gives only the coherent capacity (O(L^3)).  Expansion of (1.1)
with just the orientation (h<s) gives exactly (126.B8)--(126.B11).

There are two rigorous conclusions.

**Signed-spectral no-go.**  Put (U=\operatorname{diag}(\xi_h)).  Then
(U=U^*=U^{-1}), (B\xi=(BU){\bf1}), and

\[
 (BU)^*(BU)=UGU.
\tag{1.3}
\]

Consequently (B) and (BU) have identical singular values, and (G)
and (UGU) have identical spectra.  In particular

\[
 \|BU\|_{2\to2}=\|B\|_{2\to2}.
\tag{1.4}
\]

Thus no coefficient-uniform Bessel bound, operator norm, Schatten norm,
or other unitarily invariant spectral estimate can acquire a saving merely
by inserting the actual character.  Character insertion is an invertible
column modulation, not a noninvertible contraction.  A successful spectral
argument must instead estimate the spectral measure of the *fixed vector*
(\xi), hence must use eigenvector/kernel information not contained in an
operator norm.  This is a no-go only for coefficient-blind signed spectral
arguments; it does not rule out an actual-vector contraction theorem.

**Complete-offset inverse theorem.**  Define the complete signed offset
scalar

\[
 \Gamma_r=(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}
 e\!\left(-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}\right).
\tag{1.5}
\]

Let (R_*) be the largest (r\geq1) for which the summation set in
(1.5) is nonempty.  Then (R_*=O(L)) and

\[
 \mathcal E_L^{\rm top}-\mathcal D_L
 =\sum_{1\leq r\leq R_*}2\Re\Gamma_r.
\tag{1.6}
\]

If the left side of (1.6) is at least (\Delta>0), then

\[
 \max_{1\leq r\leq R_*}2\Re\Gamma_r\geq\frac{\Delta}{R_*}.
\tag{1.7}
\]

More strongly, with

\[
 I_j=\{r:2^j\leq r<2^{j+1},\ r\leq R_*\},
 \qquad 0\leq j\leq \lfloor\log_2R_*\rfloor,
\tag{1.8}
\]

one complete dyadic offset family satisfies

\[
 2\Re\sum_{r\in I_j}\Gamma_r
 \geq \frac{\Delta}{1+\lfloor\log_2R_*\rfloor}.
\tag{1.9}
\]

For (R_*>1), every (I_j) is a strict subfamily of the full offset
set; for (R_*=1), (1.7) is already the minimal family.  Localization is
performed only after each complete (r)-sum has been formed, so it does
not split its affine support, tags, floors, collars, entry/exit data, or
one-count slabs.  This is a quantitative inverse theorem for the literal
energy.  It gives no new cancellation and therefore does not prove
(126.B14).

The completed comparison (126.B13) transfers any violation larger than
its (O_\varepsilon(L^2X^\varepsilon)) error to the *global* literal
off-diagonal.  It does not transfer the selected band in (1.9) back to a
completed tagged band, because no offsetwise version of (126.B13) is part
of the statement-only data.

## 2. Exact statement and hypotheses

Assume precisely (126.B1)--(126.B13): (X\geq2), (J=\sqrt X), the
literal polynomial intermediate dyadic block (1\ll L\ll H), the exact
odd support (\mathscr H_L), the actual profiles in (126.B2), and zero
extension outside

\[
 \lceil h/4\rceil\leq m\leq h.
\tag{2.1}
\]

Let

\[
 \mathscr M_L=\{m\in\mathbb Z:\text{(2.1) holds for at least one }
 h\in\mathscr H_L\}.
\tag{2.2}
\]

Dyadic support gives (|\mathscr H_L|+|\mathscr M_L|=O(L)).  All sums
below are finite.  No smooth extension of (2.1), no replacement of the
actual coefficient, and no second orientation is used.

The conclusions are:

1. (R=B\xi), (\mathcal E_L^{\rm top}=\|B\xi\|_2^2), and the exact
   diagonal/off-diagonal formula is (1.5)--(1.6).
2. (\mathcal D_L\ll L^2), while coefficient-blind Cauchy yields
   (\mathcal E_L^{\rm top}\ll L^3).  The target therefore asks for a
   full factor (L) in energy.
3. The character modulation leaves all singular values invariant, as in
   (1.3)--(1.4).
4. Every excess (\Delta=\mathcal E_L^{\rm top}-\mathcal D_L>0)
   localizes as in (1.7)--(1.9), with all internal members of the selected
   offsets retained jointly.

If the constant in (126.B13) is denoted (A_\varepsilon), then the
precise completed-to-literal implication available here is

\[
 \Re\mathfrak C_{L,{\rm tag}}^{\rm comp}
 \geq A_\varepsilon L^2X^\varepsilon+\delta
 \quad\Longrightarrow\quad
 \Re\mathcal C_L^{\rm off}\geq\delta.
\tag{2.3}
\]

Applying (1.9) to (2.3) gives a literal complete offset band of size at
least (2\delta/(1+\lfloor\log_2R_*\rfloor)).  No stronger, bandwise
completed conclusion is asserted.

## 3. Proof and derivation

### 3.1 Regrouping, zero extension, and scalar Cauchy

With (1.2) and (\xi_h=\chi_4(h)), the (m)-th entry of (B\xi) is

\[
 (B\xi)_m=\sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m}}
 \chi_4(h)a_{\rm end}(h,m)e(J\sqrt{hm})=R_m.
\tag{3.1}
\]

Because zero extension precedes regrouping, summing (3.1) over (m)
gives (126.B6) without an endpoint correction.  Since
(|\mathscr M_L|=O(L)),

\[
 |\mathcal T_L|^2=\left|\sum_{m\in\mathscr M_L}R_m\right|^2
 \leq |\mathscr M_L|\sum_m|R_m|^2
 \ll L\mathcal E_L^{\rm top}.
\tag{3.2}
\]

### 3.2 Exact expansion and the single orientation

Expanding before any change of variables gives

\[
 \mathcal E_L^{\rm top}
 =\sum_m\sum_{h,s\in\mathscr H_L}
 \xi_h\xi_s a_{\rm end}(h,m)\overline{a_{\rm end}(s,m)}
 e\!\bigl(J\sqrt m(\sqrt h-\sqrt s)\bigr),
\tag{3.3}
\]

where each coefficient is zero unless its own hard affine condition
holds.  The terms (h=s) give

\[
 \mathcal D_L=\sum_{h\in\mathscr H_L}
 \sum_{m=\lceil h/4\rceil}^{h}|a_{\rm end}(h,m)|^2.
\tag{3.4}
\]

For (h<s), the common support is exactly

\[
 \lceil s/4\rceil\leq m\leq h;
\tag{3.5}
\]

the reverse orientation is the complex conjugate of this term.  Both
frequencies are odd, so (s=h+2r) for one (r\geq1), and

\[
 \xi_h\xi_{h+2r}=(-1)^r,
 \qquad
 J\sqrt m(\sqrt h-\sqrt{h+2r})
 =-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}.
\tag{3.6}
\]

Equations (3.3)--(3.6), with the one outer (2\Re), prove (1.5)--(1.6)
and exactly reproduce (126.B8)--(126.B11).  Positivity also records the
one-sided lower bound

\[
 \Re\mathcal C_L^{\rm off}\geq-\frac12\mathcal D_L.
\tag{3.7}
\]

Only the upper real-part estimate is missing.

### 3.3 Diagonal and coherent capacity

On the literal dyadic support, (h\asymp L) and (2.1) gives
(m\asymp L).  The bounded literal profiles and the factor
((L^2/(hm))^{3/4}) make each squared entry (O(1)).  There are (O(L))
frequencies and (O(L)) allowed integers (m) per frequency; equivalently
one may invoke the accepted (126.B9).  Hence

\[
 \mathcal D_L\ll L^2.
\tag{3.8}
\]

If (N_m) is the number of nonzero entries in row (m), then
(N_m=O(L)), and rowwise Cauchy gives

\[
 |R_m|^2\leq N_m
 \sum_h|a_{\rm end}(h,m)|^2.
\tag{3.9}
\]

Summing (3.9) and using (3.8) yields

\[
 \mathcal E_L^{\rm top}\ll L\mathcal D_L\ll L^3.
\tag{3.10}
\]

Thus (126.B14) is a genuine factor-(L) improvement over the blind
capacity, not a consequence of diagonal counting.

### 3.4 Why character conjugation is not a signed operator gain

Let (U=\operatorname{diag}(\xi)).  Since every (h\) is odd,
(|\xi_h|=1), and hence (U) is unitary and self-adjoint.  The actual
vector is (\xi=U{\bf1}), so

\[
 \mathcal E_L^{\rm top}=\|BU{\bf1}\|_2^2
 ={\bf1}^*UGU{\bf1}.
\tag{3.11}
\]

Unitary right multiplication preserves singular values, proving
(1.3)--(1.4).  If (Gv_\nu=\lambda_\nu v_\nu), then the exact
actual-vector formula is

\[
 \mathcal E_L^{\rm top}
 =\sum_\nu\lambda_\nu|\langle\xi,v_\nu\rangle|^2.
\tag{3.12}
\]

The eigenvalues alone do not control (3.12).  As a sharp abstract control,
let (n=|\mathscr H_L|\asymp L) and consider

\[
 G_{\rm coh}=L\,\xi\xi^*.
\tag{3.13}
\]

This is positive semidefinite, has diagonal entries (L), trace
(Ln\asymp L^2), and is a Gram matrix, but

\[
 \xi^*G_{\rm coh}\xi=Ln^2\asymp L^3.
\tag{3.14}
\]

The model (3.13) is not claimed to be the actual oscillatory Gram matrix;
it proves only that positivity, diagonal scale, and parity of the tested
vector cannot themselves imply the target.  A noninvertible projection
does not repair this logical gap for free: if it preserves (\xi), the
model (3.13) survives, while if it discards a component of (\xi), that
component has to be estimated separately.  A useful noninvertible
operator must therefore be kernel-dependent and must prove control of
the discarded actual-vector spectral mass.

### 3.5 Quantitative offset localization

The diameter of a dyadic (h)-block is (O(L)), so (R_*=O(L)).
Equation (1.6) is a finite sum of (R_*) real numbers.  If their sum is
(\Delta>0), at least one is at least their average, proving (1.7).
The sets (1.8) partition (\{1,\ldots,R_*\}) into
(1+\lfloor\log_2R_*\rfloor) cells.  Averaging over these cells proves
(1.9).  Negative cells cause no problem: the maximum cell is still at
least the average of all cell sums.

This operation selects only the outer offset index.  The full (h)-sum,
the exact common (m)-range (3.5), and every internal subdivision remain
inside (\Gamma_r).  It therefore retains one-count slabs jointly.  The
proof supplies a localization loss of at most (O(\log L)), or (O(L))
if one insists on a single offset, but supplies no cancellation within
the selected family.

### 3.6 Scope of the completed comparison

Taking real parts in (126.B13) proves (2.3), after naming its implicit
constant.  It is then legitimate to apply the literal identity (1.6).
However, a scalar estimate for the *sum* of completion errors permits
large errors on separate offset bands that cancel globally.  Therefore
(126.B13) alone cannot identify a completed tagged band corresponding to
the literal band selected by (1.9).  An offsetwise completion identity or
an absolute summability bound for the bandwise completion errors would be
required.

## 4. First doubtful or unproved step

The first unproved step toward (126.B14) is a kernel-dependent
actual-vector spectral-measure estimate.  For example, after splitting at
any fixed multiple of (L), one would need a statement of the form

\[
 \sum_{\lambda_\nu>CL}
 \lambda_\nu|\langle\xi,v_\nu\rangle|^2
 \ll_\varepsilon L^2X^\varepsilon,
\tag{4.1}
\]

together with the trivial control of the low spectrum.  Neither diagonal
energy, positivity, nor the alternating identity for (\chi_4) proves
(4.1); unitary character conjugation leaves the spectrum unchanged.

For the narrower claim that a *completed tagged* violation localizes to
the same strict offset family, the first unproved step is an offsetwise
version of (126.B13).  The available comparison is only global, so the
literal inverse theorem (1.9) cannot be promoted to a completed-band
inverse theorem from the permitted data.

## 5. Control tests and outcomes

| Control | Exact input and expected invariant/failure | Observed outcome | Implication |
|---|---|---|---|
| `literal_Round75_hard_top_vector` | Use (126.B2)--(126.B4) literally, with no surrogate coefficient. | Equation (3.1) is exactly the stated row. | Pass; the report concerns the actual hard-TOP vector. |
| `one_orientation_and_outer_2Re` | Expand (3.3), keep only (h<s), and pair (s<h) by conjugacy. | (3.5)--(3.6) give one (\Gamma_r) and one outer (2\Re). | Pass; no double counting. |
| `diagonal_one_count_and_target` | Set (h=s) before reparametrizing. | Every allowed ((h,m)) occurs once in (3.4), giving (\mathcal D_L\ll L^2); the target is the same scale. | Pass. |
| `character_inside_vector_before_square` | Form (R=B\xi) before taking the norm. | Expansion produces the literal product (\xi_h\xi_s), hence ((-1)^r). | Pass; signs were not attached after squaring. |
| `hard_affine_support_and_zero_extension` | Intersect the two literal ranges only after zero extension. | For (h<s), the exact intersection is (3.5), empty when its lower endpoint exceeds (h). | Pass; no boundary enlargement. |
| `block_energy_vs_offdiagonal_realpart` | Compare the positive norm with its expansion. | (1.6) and (3.7) hold.  Positivity gives only the lower real-part bound; the upper bound remains the target. | Pass; modulus and real part are not conflated. |
| `parity_highpass_vector_scope` | Test whether (\chi_4(h+2)=-\chi_4(h)) lowers a spectral norm. | The sign is the unitary column multiplier (U); (1.4) shows no spectral-norm change. | A parity-only high-pass/operator-norm proof is rejected.  Fixed-vector cancellation remains possible. |
| `actual_vs_adversarial_vectors` | Compare the actual (\xi) with a coefficient-uniform Bessel claim, random signs, and an aligned Gram model. | A uniform claim has the same best constant before and after (U).  The aligned positive Gram model (3.13) has diagonal (L^2) scale but actual energy (L^3) scale.  Random signs do not certify the fixed vector. | The target requires actual eigenvector overlap information; coefficient-adversarial bounds are strictly stronger. |
| `square_Pell_fourth_power_resonances` | Test exact square rays and algebraically close odd pairs; do not assume phase separation. | Exact coherent subfamilies and an exact tuned Pell offset are exhibited below.  The proof of the no-go and inverse theorem uses no separation and retains them. | Pass for the reported results; any future pointwise nonresonance argument fails this control. |
| `one_count_slabs_retained_jointly` | Localize only after the complete (r)-scalar (1.5) is formed. | (1.9) never splits an (r)-family or any of its internal members.  A completed-band transfer is unavailable. | Literal localization passes; completed tagged localization is retained as an explicit gap. |
| `capacity_before_and_claimed_gain` | Compare diagonal, blind capacity, target, and the actual conclusion. | (3.8), (3.10), and (126.B14) are respectively (L^2,L^3,L^2X^\varepsilon).  The inverse theorem loses only a logarithm when locating an excess but proves no saving inside it. | No target gain is claimed; the required factor (L) remains open. |
| `endpoint_and_prior_owner_scope` | Use prior owners only through the two global accepted statements (126.B12)--(126.B13). | No endpoint, collar, exact-centre, square-ray, or other owner is reopened or counted again. | Pass; no endpoint-uniform conclusion is made. |
| `owner_and_downstream_scope` | Restrict to one polynomial intermediate hard-TOP M2 block. | No BAL, UNBAL, M1, full M9-M2, M9, quarter-theorem, or exponent conclusion is drawn. | Pass. |

The resonance part of the ninth control can be made exact.  If
(X=t^4) with integer (t), then (J=t^2), (q_X=1), and (H=t).
For odd squarefree (d) and odd (u,v), take

\[
 h=du^2,\qquad m=dv^2.
\tag{5.1}
\]

Whenever (5.1) lies in the literal block and hard affine range,

\[
 e(J\sqrt{hm})=e(t^2duv)=1,
 \qquad \chi_4(h)=\chi_4(d),
\tag{5.2}
\]

so the character is constant, not alternating, on the squarefree ray.
With bounded entries, the isolated coherent capacity of all such rays is

\[
 \sum_{\substack{d\ {\rm squarefree}\\ d\ {\rm odd}}}
 O\!\left((L/d)^{1/2}(L/d)\right)=O(L^{3/2}),
\tag{5.3}
\]

which is below (L^2) but disproves automatic sign cancellation on every
structured subfamily.  No lower bound is claimed because the actual
profiles may zero or attenuate particular entries.

For a Pell control, the equation

\[
 p^2-5q^2=-4
\tag{5.4}
\]

has infinitely many odd solutions (starting with ((1,1)), and preserved
by multiplication by (9+4\sqrt5)).  Put (h=p^2) and (s=5q^2=h+4),
so (r=2) and

\[
 \sqrt s-\sqrt h=q\sqrt5-p=\frac4{q\sqrt5+p}.
\tag{5.5}
\]

Taking (m=h) and

\[
 J=N\frac{q\sqrt5+p}{4p},\qquad N\in\mathbb N,
\tag{5.6}
\]

makes (J\sqrt m(\sqrt s-\sqrt h)=N) exactly.  By choosing (N\gg p^4),
one also has (L\asymp p^2\ll H\asymp\sqrt J).  Thus, whenever the literal
profiles retain these entries, even a fixed small offset can be exactly
resonant for an admissible real (X=J^2).  This is a phase-geometry
obstruction, not a claim that the Pell family has enough weighted mass to
violate the target.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read and used:

1. `rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/briefs/blind_hard_top_vector_rederivation.md` (the generated task brief);
2. `rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/blind_statement.md` (the complete frozen statement);
3. `problems/gauss_circle.md`;
4. `state/control_models.md`.

No strategy file, proof-state file, nonblind Round-75--126 artifact,
sibling report, web source, or numerical computation was used.  The work
was entirely analytical.

## 7. Recommended state effect

**Revise.**  Record the exact character-conjugation no-go (1.3)--(1.4)
and the literal complete-offset inverse theorem (1.7)--(1.9) as candidate
lemmas after independent seam checking.  Keep (126.B14)--(126.B15)
unproved.  Do not promote a coefficient-blind spectral mechanism, and do
not claim completed tagged offset localization until an offsetwise
completion connector strengthening (126.B13) is supplied.



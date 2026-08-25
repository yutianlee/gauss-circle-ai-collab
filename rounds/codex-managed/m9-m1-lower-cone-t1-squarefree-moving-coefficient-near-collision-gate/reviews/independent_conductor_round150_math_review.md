# Round 150 independent hostile mathematics and seam review

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Reviewed artifact: `candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`
- Role: independent hostile mathematics/seam reviewer
- Terminal verdict: **GREEN for the fixed-wrap/all-$L$ core; GREEN, after the verification below, for the bounded-$M$ actual-profile edge; OPEN for the growing-$M$ large-wrap collar**
- Recommended round label: `strict_moving_coefficient_collar_range`

## 1. Result

The core kernel (150.C7)--(150.C21) is mathematically **GREEN**.  More
precisely:

1. the two-row formula is an exact low-$\ell^1$-norm expansion of the
   **arithmetic divisor-incidence masks**;
2. the new norm
   \[
     \sum_L |B_{d,U}(L)|L^{-1/2}\ll_\varepsilon X^\varepsilon
   \]
   is valid uniformly for every literal finite prefix;
3. for every fixed centered wrap integer \(k\), the complete nonzero
   collar has coefficient-weighted absolute mass
   \(O_\varepsilon(DQX^\varepsilon)\); and
4. any packet of at most \(O(1+R^2/Q)\) wraps is therefore
   \(O_\varepsilon(R^2DX^\varepsilon)\).

The fixed-wrap proof is independent of character cancellation, profile
variation, and the full projective separability of the moving coefficient.
It survives even if the bounded-\(M\) edge were removed.

I also independently verified the bounded-\(M\) edge from the accepted
Round-148 actual-profile formula and derivative ledger.  At fixed
\(M\le M_0\), the actual sampled profile has uniformly bounded
supremum-plus-total-variation in the scaled \(q\)-variable.  The elementary
weighted second-derivative estimate then gives \(O(RX^\varepsilon)\) for
each transformed row, hence (150.C5).  Thus this edge is **GREEN**, not
merely conditional.  The candidate's word "jump" should be read as one
owned smooth transition of \(O(1)\) variation; a prefix shorter than the
Round-148 collar is already assigned to the primal collar owner.

Three precision repairs identified during review are now present in the
repaired candidate, and none changes the bounds:

- (150.C7)--(150.C10) now scope the projective norm to the arithmetic
  incidence expansion, not the full \((d,x_1,x_2)\) coefficient
  containing the two prefixes and profiles;
- the shifted-factor divisor paragraph now says \(k\ne0\); the case
  \(k=0\) is separately and correctly owned by (150.C20), with the
  optional sharper count (150.C21); and
- the residual display (150.C29) now includes
  \(k(L_1,L_2,q_1,q_2)\notin\mathcal K\) and all inherited support
  conditions.

The full collar is not proved.  The first remaining collar seam is exactly
the growing-\(M\), large-wrap, literal signed sum outside the safe packet.

## 2. Exact statement and hypotheses

Assume
\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,
 \qquad Q=2\sqrt{ND/E}.
\]
Then
\[
 Q\asymp \frac{R^2D}{\sqrt M},\qquad Q\ll R^2,
 \qquad \frac{R^2}{Q}\asymp\frac{\sqrt M}{D}.
\tag{R150.1}
\]
Write a squarefree row as \(d=\eta m\), with
\(\eta\in\{1,2\}\) and \(m=d_{\rm o}\) odd squarefree.  If a nonzero
coefficient index is written uniquely as \(L=ts^2\), where \(t,s\) are
odd squarefree and \((t,s)=1\), then the sum-over-divisors version of the
accepted Round-149 formula is
\[
\begin{aligned}
B_{\eta m,U}(ts^2)
={}&\sum_{a\mid t}\frac{\mu(a)\mu(c)\mu(s)}c
 \sum_{u\ge1}\frac{\mu(u)}u
 \sum_{\substack{v\ge1\ {\rm odd\ squarefree}\\(v,cs)=1}}
 \frac{\mu(v)}{v^2}\\
&\quad\times {\bf1}_{au\mid m}{\bf1}_{(m,csv)=1}
 \kappa_{\eta m,U}\!\left(au(csv)^2\right),
 \qquad c=t/a.
\end{aligned}
\tag{R150.2}
\]
Indeed the two masks force \(a=(t,m)\), so exactly one divisor \(a\)
survives and (R150.2) is precisely (149.C15).  If \(L\) is not cube-free,
then \(B_{d,U}(L)=0\); this harmless zero case should be stated when
(R150.2) is quoted as a formula for all \(L\).

For two copies of (R150.2), put
\[
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
\]
The exact identity
\[
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m}
\tag{R150.3}
\]
proves (150.C9), including incompatible primes across the two rows.  For
fixed \((L_1,L_2)\), the sum of the absolute scalar coefficients in this
incidence expansion is \(O_\varepsilon(X^\varepsilon)\): the \(u_i\)
sums are harmonic or divisor sums on the finite prefix, the \(v_i^{-2}\)
sums stay convergent after the \(z\)-divisor weights, and
\(\sum_{c\mid t}c^{-1}\ll_\varepsilon X^\varepsilon\).  The factors
\[
 \kappa_{\eta m,U}(a_i u_i(c_i s_i v_i)^2),\qquad
 \mathscr A_{D,E,U}\!\left(\eta m,
   \frac{4N\eta mL_i^2}{q_i^2}\right)
\]
remain joint row-cell multipliers.  No finite-rank or bounded-variation
claim about those factors follows from (R150.3).

The all-\(L\) norm follows from
\(|B_{d,U}(acs^2)|\ll_\varepsilon X^\varepsilon/c\), with
\(a\mid d_{\rm o}\), and the finite support \(L\ll E\):
\[
\begin{aligned}
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\rm o}}a^{-1/2}
 \sum_{c\ge1}c^{-3/2}
 \sum_{s\le\sqrt E}s^{-1}\\
 &\ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{R150.4}
\]
Here \(\prod_{p\mid d_{\rm o}}(1+p^{-1/2})=X^{o(1)}\), and all
squarefree and coprimality restrictions may be dropped in an upper bound.
No prefix regularity is used.

## 3. Proof and derivation

For a cell pair let
\[
 q_i=hr_i,\qquad h=(q_1,q_2),\qquad (r_1,r_2)=1,
 \qquad \delta=L_1r_2-L_2r_1,
\]
and choose the centered integer \(k\) by
\[
 \rho=N\delta-khr_1r_2,qquad
 |\rho|\le hr_1r_2/2.
\tag{R150.5}
\]
All denominators are odd, so \(hr_1r_2\) is odd and there is no
nearest-integer tie.  For \(D<2\), imposing centeredness in addition to
the collar only removes solutions from the count below.

Fix \((L_1,L_2,h,k,r_1)\), and set
\[
 S=NL_1-khr_1,\qquad \alpha=hr_1/D.
\]
The collar inequality is exactly
\[
 |Sr_2-NL_2r_1|\le\alpha r_2.
\tag{R150.6}
\]
On a supported solution, \(hr_i\asymp L_iQ\), and therefore
\[
 \frac{|\rho|}{NL_2r_1}
 \ll \frac{Q}{DN}\ll1,qquad
 S\asymp NL_1,qquad S>2\alpha.
\tag{R150.7}
\]
Solving (R150.6) for \(r_2\) gives an interval of length
\[
 \frac{2NL_2r_1\alpha}{S^2-\alpha^2}
 \ll \frac{L_2Q^2}{hDN}
 =\frac{4L_2}{hE}\ll1.
\tag{R150.8}
\]
Thus there are \(O(1)\) possible \(r_2\) for each of the
\(O(L_1Q/h)\) supported \(r_1\).  Swapping the two cells replaces
\((k,\rho)\) by \((-k,-\rho)\), so the same argument from the other
side gives
\[
 \mathcal N_k(L_1,L_2;h)
 \ll \frac{Q\min(L_1,L_2)}h.
\tag{R150.9}
\]
Oddness, exact gcd, reducedness, coprimality, centeredness, and
\(\rho\ne0\) may all be dropped because this is an upper count.

Multiplying (R150.9) by the literal coefficient magnitude and summing
the harmonic \(h\)-range gives, for one row,
\[
\begin{aligned}
 \mathcal A_{k,U}(d)
 &\ll_\varepsilon QX^\varepsilon
 \sum_{L_1,L_2}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{\max(L_1,L_2)}\\
 &\le QX^\varepsilon
 \left(\sum_L\frac{|B_{d,U}(L)|}{\sqrt L}\right)^2
 \ll_\varepsilon QX^\varepsilon.
\end{aligned}
\tag{R150.10}
\]
Summing \(O(D)\) rows proves (150.C2).  For a wrap packet
\(|\mathcal K|\ll1+R^2/Q\),
\[
 \mathcal A_{\mathcal K,U}
 \ll_\varepsilon DQ\left(1+\frac{R^2}{Q}\right)X^\varepsilon
 \ll_\varepsilon R^2DX^\varepsilon,
\tag{R150.11}
\]
because \(Q\ll R^2\).  This checks the packet cardinality and every
\(R,M,D,E,Q\) power.

The case \(k=0\) is already covered by (R150.10).  The independent
count (150.C21) is also valid for the nonexact part: with
\(g=(L_1,L_2)\), write \(\delta=gj\).  There are
\(O(L_1L_2/(ghE))\) possible nonzero \(j\), and each linear
Diophantine equation has \(O(1+gQ/h)\) supported solutions.  Hence
\[
 \mathcal N_0(L_1,L_2;h)
 \ll \frac{L_1L_2}{ghE}+\frac{L_1L_2Q}{h^2E}.
\tag{R150.12}
\]
After the \(1/(L_1L_2)\) weights, the harmonic \(h\)-sum, and
\(\sum_L|B_{d,U}(L)|\ll_\varepsilon\sqrt E X^\varepsilon\), this is
\(O_\varepsilon(QX^\varepsilon)\) per row.

For the shifted-factor seam, direct multiplication gives
\[
 (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho,
\tag{R150.13}
\]
and
\[
 r_2(NL_1-khr_1)=NL_2r_1+\rho,qquad
 r_1(NL_2+khr_2)=NL_1r_2-\rho.
\tag{R150.14}
\]
The ratio in (R150.7) proves both factors are positive for both signs of
\(k\) and \(\rho\), including \(D=1\) and denominators dividing \(N\).
There is no zero-factor exception.  If \(k\ne0\) and
\((L_1,L_2,h,k,\rho)\) is fixed, each positive divisor pair of the
right side determines at most one integral \((r_1,r_2)\), hence there
are \(O_\varepsilon(X^\varepsilon)\) candidates.  For \(k=0\), this
factorization is constant in \((r_1,r_2)\), so (R150.12), not a divisor
bound, is the lawful owner.

For \(k\ne0\), the loose ranges
\[
 h\ll\min(L_1,L_2)Q,qquad |k|\ll N/Q,qquad
 0<|\rho|\ll L_1L_2Q^2/(hD)
\]
give, after separate absolute summation, the upper capacity
\[
 \frac{NL_1L_2Q}{D}X^\varepsilon.
\tag{R150.15}
\]
Relative to the raw pair count \(L_1L_2Q^2\), this is worse by
\[
 \frac{N}{DQ}\asymp\frac{R^2\sqrt M}{D^2}\ge R.
\tag{R150.16}
\]
This is a rigorous no-go only for separately summing these per-shift
absolute divisor bounds; it is not an estimate for the actual signed
sum and not a signed lower bound.

Finally, the bounded-\(M\) edge can be made unconditional from the
accepted Round-148 profile.  After gcd reduction its actual form is
\[
 \mathscr W_{d,U}(L/q)
 =\mathscr A_{D,E,U}\!\left(d,\frac{4NdL^2}{q^2}\right).
\]
Writing \(q=LQy\) gives
\[
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{R150.17}
\]
Round 148's accepted derivative ledger gives bulk logarithmic
derivatives \(O_j(1)\), radial-transition derivatives
\(O_j(M^{j/2})\), and cone-transition derivatives
\(O_j(D^{j/2})\), with only finitely many owned transitions.  When
\(M\le M_0\), nonempty dyadic support forces \(D,E,L=O_{M_0}(1)\), so
\[
 \|\mathscr W\|_\infty+\operatorname{Var}_q(\mathscr W)
 \ll_{M_0,\varepsilon}X^\varepsilon.
\tag{R150.18}
\]
On a permitted residue class \(q=a+4Ln\), the phase
\(F(n)=NdL/(a+4Ln)\) has one-sign curvature
\[
 |F''(n)|\asymp R^{-2}
\]
on an interval of \(O(R^2)\) integers.  The elementary
second-derivative lemma
\[
 \sum_{n\in I}e(F(n))
 \ll |I|\sqrt\lambda+\lambda^{-1/2}
 \quad\left(\lambda\asymp|F''|\right)
\tag{R150.19}
\]
therefore gives \(O(R)\), uniformly on subintervals.  Abel summation
with (R150.18) preserves \(O_\varepsilon(RX^\varepsilon)\).
Partitioning by the finitely many residue classes modulo \(4L\) keeps
\(\chi_4(Lq)\) constant and enforces \((L,q)=1\).  Summing the
accepted norm \(\sum_L|B_{d,U}(L)|/L\ll X^\varepsilon\) proves
\(|G_U(d)|\ll_\varepsilon RX^\varepsilon\), and the \(O(D)=O(1)\)
rows prove (150.C5).

## 4. First doubtful or unproved step

The first unproved collar statement is the growing-\(M\) contribution
for which the unique centered wrap satisfies \(k\notin\mathcal K\), with
\(|\mathcal K|\ll1+R^2/Q\).  The repaired formula (150.C29) is the
correct literal summand and its summation subscript now explicitly includes
\[
 k=k(L_1,L_2,q_1,q_2)\notin\mathcal K,\quad
 q_i\asymp L_iQ,\quad (L_i,q_i)=1,\quad
 h=(q_1,q_2),\quad q_i=hr_i,\quad (r_1,r_2)=1.
\tag{R150.20}
\]
After the arithmetic incidence expansion, the two exact prefixes and
the two sampled profiles still depend jointly on the row and both cells.
The incidence norm is not a projective decomposition of that full matrix,
and (R150.15) cannot be summed to the target.  A genuinely joint signed
large-wrap theorem or a further exact recombination is still missing.

At \(D=1,L_1=L_2=1\), centeredness makes the collar the whole nonexact
frequency-pair family.  The safe packet contains only
\(O(1+\sqrt M)\) wraps, whereas the loose full wrap range has order
\(N/Q\asymp R^2\sqrt M\).  The bounded-\(M\) actual row is owned by
(R150.17)--(R150.19), but the growing-\(M\) row is not.  Independently,
the growing-\(M\) generic non-collar remains open.

## 5. Required control tests and outcomes

| Seam/control | Outcome |
|---|---|
| exact two-row incidence | **GREEN.** (R150.2)--(R150.3) are exact; state separately that non-cube-free \(L\) gives zero. |
| projective norm | **GREEN; scope repair applied.** The \(\ell^1\) norm is for arithmetic incidence atoms only; the prefix/profile matrix is not separated. |
| new \(\sum_L|B|/\sqrt L\) norm | **GREEN.** (R150.4) checks all \(a,c,s\) sums with no prefix regularity. |
| centeredness and sign | **GREEN.** Odd \(H\) makes \(k\) unique; the interval count may enlarge by dropping centeredness. |
| every fixed \(k\) interval/count | **GREEN.** (R150.6)--(R150.9) check positivity, interval length, index swap, and the \(h\)-harmonic sum. |
| \(k=0\) | **GREEN.** It is covered by the uniform proof; (R150.12) independently checks the nonexact determinant count. |
| all \(L\) and \(h\) sums | **GREEN.** (R150.10) uses exactly the half-weight norm and loses only \(X^\varepsilon\). |
| packet cardinality and powers | **GREEN.** (R150.1) and (R150.11) give \(DQ(1+R^2/Q)\ll R^2D\). |
| shifted-factor identity and positivity | **GREEN.** (R150.13)--(R150.14) work for both signs, \(D=1\), and \(q_i\mid N\); no factor vanishes. |
| fixed-shift divisor switch | **GREEN; repair applied.** The candidate now writes \(k\ne0\); the \(k=0\) factorization is degenerate and has its separate owner. |
| all-shift no-go | **GREEN by narrow scope.** (R150.15)--(R150.16) reject only separate absolute per-shift summation and are not a signed lower bound. |
| raw/absolute/signed separation | **GREEN.** (R150.9), (R150.10), and (150.C29) are respectively a raw count, absolute weighted mass, and signed sum. |
| character, parity, primes, prefixes, imprimitive phases | **GREEN.** The literal signed sum retains \(\chi_4(L_1L_2r_1r_2)\); the absolute proof only enlarges after dropping restrictions. |
| \(D=1,L=1\) | **GREEN as an audit.** Bounded \(M\) is proved by actual-profile curvature; growing-\(M\) large wraps remain explicitly open. |
| blind countermodel | **GREEN by scope.** It disproves a theorem for arbitrary bounded smooth profiles with uncontrolled variation, not the actual Round-148 profile and not the absolute fixed-wrap lemma. |
| bounded-\(M\) actual-profile edge | **GREEN.** (R150.17)--(R150.19) supply the missing variation and weighted-curvature verification. |
| exact phase and small denominators | **GREEN.** \(\rho=0\) remains with the accepted Round-149 owner; the upper count includes rather than discards imprimitive/small-denominator cases. |
| downstream scope | **GREEN.** No generic, \(t\ge2\), Round-138 cross, lower GAR, M1, M2, endpoint, M9, bridge, target, or exponent is closed. |

## 6. Dependencies and exact artifacts used

The accepted mathematical input was limited to the governing protocol and
proof-state records, the requested Round-150 candidate and blind control,
the accepted Round-149 candidate, and the cited accepted Round-148
transform/profile definitions:

1. `protocol.md`;
2. the relevant Round-150 and downstream entries of
   `state/proof_obligations.yml` and `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/blind_nonexact_correlation_feasibility.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/conductor_round148_adjudication.md`; and
8. the actual-profile formula and derivative ledger in
   `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`, which the Round-148 adjudication accepts as part of the repaired transform evidence.

The weighted second-derivative estimate was rederived in the precise
placement (R150.19); no external theorem, web source, or numerical
experiment is used.  The blind countermodel is used only as a
hypothesis-sufficiency control.  No conclusion is imported from another
Round-150 review.

## 7. Recommended state effect

Close Round 150 under
\[
 \boxed{\mathsf{strict\_moving\_coefficient\_collar\_range}}.
\]
With the three wording/subscript repairs in Section 1 now applied, promote:

1. the exact arithmetic two-row incidence expansion and its scoped
   \(O_\varepsilon(X^\varepsilon)\) coefficient norm;
2. the prefix-uniform half-weight norm (150.C11);
3. the every-fixed-wrap bound and the target-safe packet
   (150.C2)--(150.C4);
4. the bounded-\(M\) actual-profile full-row edge (150.C5), now supported
   by (R150.17)--(R150.19); and
5. shifted-factor positivity, the \(k\ne0\) fixed-shift divisor bound,
   and the narrowly scoped all-shift absolute-summation no-go.

Retain as open the growing-\(M\) large-wrap collar with condition
(R150.20), the growing-\(M\) generic complement, the signed \(RD\)
scalar, every \(t\ge2\) layer, the independent Round-138 cross owner,
all remaining M1 and M2 owners, endpoint uniformity, M9, the conditional
bridge, the Gauss target, and every exponent claim.  The fixed-wrap core
is GREEN independently of the bounded-\(M\) edge, and no full-collar or
downstream promotion is licensed.

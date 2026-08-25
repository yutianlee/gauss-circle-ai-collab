# Round 150 conductor candidate: small-wrap collar and large-wrap boundary

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Round: 150
- Role: conductor proof-kernel selection
- Starting graph SHA-256: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Allocation: 100% analytic/algebraic and primary-source work; 0% numerical
- Candidate terminal label: `strict_moving_coefficient_collar_range`

## 1. Selected result

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
\tag{150.C1}
$$

Round 150 does not prove the full moving-coefficient collar.  It proves
three strict positive statements and isolates the first remaining
collar seam.

First, the literal product of the two compressed coefficients has an
exact low-projective-norm divisor-incidence expansion.  Second, for
every fixed centered wrap integer $k$, the coefficient-weighted
absolute collar mass is

$$
 \mathcal A_{k,U}\ll_\varepsilon DQX^\varepsilon.
\tag{150.C2}
$$

Consequently any set $\mathcal K$ of wrap classes satisfying

$$
 |\mathcal K|\ll 1+\frac{R^2}{Q}
 \asymp 1+\frac{\sqrt M}{D}
\tag{150.C3}
$$

is target-safe:

$$
 \mathcal A_{\mathcal K,U}
 \ll_\varepsilon R^2DX^\varepsilon.
\tag{150.C4}
$$

This includes the complete nonexact $k=0$ collar and a symmetric
small-wrap packet.  Third, when $M$ is bounded by an absolute
constant, the actual Round-148 sampled profile has bounded variation
on its fixed-scale support and the entire transformed row satisfies

$$
 |G_U(d)|\ll_\varepsilon RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon.
\tag{150.C5}
$$

The first open collar sector is therefore the growing-$M$ large-wrap
band outside (150.C3), with the literal character, incidence,
prefixes, and sampled profiles retained.  The generic non-collar at
growing $M$ remains separately open.

## 2. Exact two-row coefficient and hypotheses

All $L,q,h,r$ are positive odd integers.  The saddle support is
$q\asymp LQ$, $(L,q)=1$, and $L\ll E$.  Write a squarefree row as

$$
 d=\eta m,\qquad \eta\in\{1,2\},\qquad
 m=d_{\mathrm o}\ \hbox{odd and squarefree}.
\tag{150.C6}
$$

For $L=ts^2$, with $t,s$ odd squarefree and $(t,s)=1$, choose
$a\mid t$ and put $c=t/a$.  The accepted closed formula can be
written exactly as

$$
\begin{aligned}
 B_{\eta m,U}(ts^2)
 ={}&\sum_{a\mid t}\frac{\mu(a)\mu(c)\mu(s)}c
 \sum_{u\ge1}\frac{\mu(u)}u
 \sum_{\substack{v\ge1\ \mathrm{odd\ squarefree}\\(v,cs)=1}}
 \frac{\mu(v)}{v^2}\\
 &\quad\times {\bf1}_{au\mid m}{\bf1}_{(m,csv)=1}
 \kappa_{\eta m,U}\!\left(au(csv)^2\right).
\end{aligned}
\tag{150.C7}
$$

The prefix is the literal finite nonempty-progression indicator; it is
not smoothed.  Applying (150.C7) to $L_i=t_is_i^2$, set

$$
 c_i=t_i/a_i,\qquad
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
\tag{150.C8}
$$

All dependence of the pure divisibility masks on $m$ is

$$
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m}.
\tag{150.C9}
$$

The two prefix values and the two samples

$$
 \mathscr W_{\eta m,U}(L_i/q_i)
 =\mathscr A_{D,E,U}\!\left(
       \eta m,\frac{4N\eta mL_i^2}{q_i^2}\right)
\tag{150.C10}
$$

remain joint row-cell functions.  They are not declared separable or
of globally bounded variation.  Thus the following projective norm is
only for the arithmetic divisor-incidence atoms, not for the full
row-cell matrix containing these prefix and profile multipliers.  On
the literal finite support, the absolute scalar-coefficient norm of
(150.C7)--(150.C9), for fixed
$(L_1,L_2)$, is $O_\varepsilon(X^\varepsilon)$: the $u_i$ sums are
logarithmic, the $v_i^{-2}$ sums remain convergent after divisor
weights, and $\sum_{c\mid t}c^{-1}\ll_\varepsilon X^\varepsilon$.

An additional prefix-uniform norm is

$$
 \boxed{
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.}
\tag{150.C11}
$$

Indeed the closed formula gives $|B_{d,U}(acs^2)|\ll
X^\varepsilon/c$, so

$$
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}a^{-1/2}
 \sum_{c\ge1}c^{-3/2}
 \sum_{s\le\sqrt E}s^{-1}
 \ll_\varepsilon X^\varepsilon.
\tag{150.C12}
$$

No regularity of the prefix is used in (150.C11).

## 3. Fixed-wrap proof and the bounded bottom scale

For a pair of cells write

$$
 q_i=hr_i,\qquad (r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
\tag{150.C13}
$$

and choose the unique centered integer $k$ with

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\le\frac{hr_1r_2}{2}.
\tag{150.C14}
$$

The nonexact collar is $0<|\rho|\le hr_1r_2/D$.  Fix
$(L_1,L_2,h,k)$ and $r_1$, and put

$$
 S=NL_1-khr_1,\qquad \alpha=hr_1/D.
\tag{150.C15}
$$

The collar inequality is

$$
 |Sr_2-NL_2r_1|\le\alpha r_2.
\tag{150.C16}
$$

On every supported solution, $r_1/r_2\asymp L_1/L_2$ and

$$
 S\asymp NL_1,\qquad
 \frac{\alpha}{S}\ll\frac{Q}{DN}\ll1.
\tag{150.C17}
$$

Thus $S>2\alpha$ for large $X$, and (150.C16) confines $r_2$ to an
interval of length

$$
 \frac{2NL_2r_1\alpha}{S^2-\alpha^2}
 \ll\frac{L_2Q^2}{hDN}
 =\frac{4L_2}{hE}\ll1.
\tag{150.C18}
$$

There are $O(L_1Q/h)$ supported $r_1$; interchanging the indices gives

$$
 \mathcal N_k(L_1,L_2;h)
 \ll\frac{Q\min(L_1,L_2)}h.
\tag{150.C19}
$$

Dropping oddness, exact-gcd, coprimality, reducedness, and the
nonexact exclusion only enlarges this count.  With bounded profiles,
the coefficient factor $1/(L_1L_2)$, the harmonic $h$ sum, and
$1/\max(L_1,L_2)\le1/\sqrt{L_1L_2}$, (150.C11) gives for each row

$$
\begin{aligned}
 \mathcal A_{k,U}(d)
 &\ll_\varepsilon QX^\varepsilon
 \sum_{L_1,L_2}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{\max(L_1,L_2)}\\
 &\ll_\varepsilon QX^\varepsilon.
\end{aligned}
\tag{150.C20}
$$

Summing the $O(D)$ rows proves (150.C2); summing any packet satisfying
(150.C3), and using $Q\ll R^2$, proves (150.C4).  This is an absolute
estimate, hence is uniform in both prefixes and profiles and needs no
$\chi_4$ or row cancellation.  Exact $\rho=0$ remains with the
already accepted exact-phase owner.

For completeness, $k=0$ also admits an independent determinant count.
Then $\rho=N\delta$, every $\delta$ is a multiple of
$g=(L_1,L_2)$, and

$$
 \mathcal N_0(L_1,L_2;h)
 \ll \frac{L_1L_2}{ghE}
      +\frac{L_1L_2Q}{h^2E}.
\tag{150.C21}
$$

The accepted norm $\sum_L|B_{d,U}(L)|\ll\sqrt E X^\varepsilon$
again yields $DQX^\varepsilon$ after all rows.

If $M\le M_0$, then $D,E,L=O(1)$ and $Q\asymp R^2$.  On the accepted
Round-148 interior amplitude, writing $q=LQy$ gives

$$
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{150.C22}
$$

Every retained smooth factor is fixed-scale in $y$; each owned product
or cone boundary contributes one smooth transition of $O(1)$ variation,
while a prefix shorter than its collar already has the prior primal
owner.  The accepted transition derivative ledger is $O(1)$ at bounded
$M$.  Hence the
actual sampled weight has $q$-total variation
$O_\varepsilon(X^\varepsilon)$.  This assertion is about the actual
profile, not an arbitrary bounded smooth function.  On each odd
residue class, $f(q)=NdL/q$ satisfies

$$
 |f''(q)|\asymp R^{-2},\qquad q\asymp R^2.
\tag{150.C23}
$$

Split the odd coprime support into the $O(1)$ allowed residue classes
modulo $4L$ (or use finite Mobius inclusion for $(L,q)=1$).  The
weighted second-derivative estimate and partial summation on each
class give a $q$ sum $O_\varepsilon(RX^\varepsilon)$.  Since only $O(1)$ values
of $L,d$ occur and $\sum_L|B(L)|/L\ll X^\varepsilon$, this proves
(150.C5).  The already peeled physical collars keep their prior
target-safe owner.  For growing $M$ the same placement has the known
$RM^{1/4}$ term and no extension is claimed.

## 4. Shifted-factor audit and first unproved step

The exact identity is

$$
 \boxed{
 (NL_1-khr_1)(NL_2+khr_2)
 =N^2L_1L_2+kh\rho.}
\tag{150.C24}
$$

Also

$$
\begin{aligned}
 r_2(NL_1-khr_1)&=NL_2r_1+\rho,\\
 r_1(NL_2+khr_2)&=NL_1r_2-\rho.
\end{aligned}
\tag{150.C25}
$$

Because $|\rho|/(NL_2r_1)\ll Q/(DN)\ll1$, both factors are positive
on the collar; no zero-factor exception occurs, including when a
denominator divides $N$.  For fixed
$(L_1,L_2,h,k,\rho)$ with $k\ne0$, a positive factorization of the right side of
(150.C24) determines at most one candidate pair, so there are at most
$X^\varepsilon$ candidates.

This does not close the full shift sum.  The legal ranges include

$$
 h\ll\min(L_1,L_2)Q,\qquad
 |k|\ll\frac NQ,\qquad
 0<|\rho|\ll\frac{L_1L_2Q^2}{hD}.
\tag{150.C26}
$$

Separately summing the fixed-shift divisor bound gives the adverse raw
capacity

$$
 \frac{NL_1L_2Q}{D}X^\varepsilon,
\tag{150.C27}
$$

which exceeds the trivial $L_1L_2Q^2$ pair capacity by

$$
 \frac{N}{DQ}\asymp\frac{R^2\sqrt M}{D^2}\ge R.
\tag{150.C28}
$$

Equations (150.C27)--(150.C28) are a no-go for separately summing
per-shift absolute divisor bounds.  They are not a signed lower bound.

Choose the symmetric target-safe packet
$\mathcal K=\{k:|k|\le K_0\}$ with
$2K_0+1\ll1+R^2/Q$, so that (150.C3) holds.  At growing $M$, the first unproved collar sum is the part
with $k\notin\mathcal K$ of

$$
\begin{aligned}
 \sum_{d\asymp D}\mu^2(d)
 \sum_{\substack{1\le L_i\ll E,\ (L_i,q_i)=1,\ q_i\asymp L_iQ\\
                 h=(q_1,q_2),\ q_i=hr_i,\ (r_1,r_2)=1\\
                 k=k(L_1,L_2,q_1,q_2)\notin\mathcal K\\
                 0<|\rho|\le hr_1r_2/D}}
 &\chi_4(L_1L_2r_1r_2)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\times \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
\end{aligned}
\tag{150.C29}
$$

After (150.C9), both prefixes and profiles in (150.C29) still move
jointly with $d$ and the two cells.  A solution needs a genuinely
joint signed shifted-divisor/matrix estimate, or another exact
recombination that retains $\chi_4$ and controls the large wraps
simultaneously.

The $D=1,L_1=L_2=1$ test is compulsory.  When $D=1$, the centered
condition makes the collar the full nonexact pair family.  For growing
$M$, the exact reciprocal sum

$$
 B_{1,U}(1)
 \sum_{q\asymp Q\atop q\ \mathrm{odd}}
 \chi_4(q)\mathscr W_{1,U}(1/q)e(N/q)
\tag{150.C30}
$$

has no row average, and most wrap classes lie outside (150.C3).
The bounded-$M$ case is owned by (150.C5), but the growing-$M$ case
remains open.

## 5. Blind and source controls

The statement-only blind report constructs an adversarial bounded
smooth profile interpolating the character and reciprocal phase at the
finite sample points.  It correctly proves that boundedness and
pointwise smoothness alone do not imply the full collar theorem.  It
does not refute (150.C2)--(150.C4), which use only absolute counting,
and it does not refute (150.C5), which uses the actual Round-148
profile and its quantitative variation ledger.  The countermodel is
therefore retained as a hypothesis-sufficiency control: no theorem for
an arbitrary bounded smooth profile may be promoted.

No external shifted-divisor, double-large-sieve, or Kloosterman
fraction theorem is used to prove (150.C2)--(150.C4).  Any literature
analogy for (150.C29) must still match its joint row-cell coefficients,
two prefixes, two profiles, character, large-wrap range, and diagonal
placement.  Promotion of the bounded-$M$ edge additionally requires a
checked weighted second-derivative theorem card or a self-contained
derivation.

## 6. Required controls and outcomes

1. `literal_nonzero_collar_expansion`: GREEN in (150.C29).
2. `two_row_divisor_incidence_linearization`: GREEN in
   (150.C7)--(150.C10); no arbitrary matrix replaces the coefficient.
3. `prefix_profile_d_dependence`: GREEN as an exact audit; global
   variation is not inferred from boundedness.
4. `shifted_factor_identity`: GREEN in (150.C24)--(150.C25).
5. `k_zero_and_exceptional_factor`: GREEN in
   (150.C17)--(150.C21) and (150.C25).
6. `full_shift_and_weight_summation`: GREEN for every fixed wrap and
   every packet satisfying (150.C3); OPEN outside that packet.
7. `tuple_absolute_signed_separation`: GREEN; (150.C19) is a raw
   count, (150.C20) an absolute weighted mass, and (150.C29) signed.
8. `mod_four_character_retention`: GREEN; it is retained in
   (150.C29), although the promoted packet survives absolute values.
9. `source_theorem_collar_match`: no external theorem is needed for
   the fixed-wrap proof; the large-wrap source interface remains open.
10. `all_M_D_E_Q_L_h_k_rho_power_ledger`: GREEN for the strict ranges
    through (150.C18)--(150.C28).
11. `D1_L1_full_frequency_test`: GREEN at bounded $M$ and for the
    small-wrap packet; OPEN for growing-$M$ large wraps.
12. `prime_parity_prefix_imprimitive_controls`: GREEN; (150.C6)--
    (150.C10) retain even rows and cross-row prime incompatibility,
    while the upper count may only drop restrictions.
13. `exact_and_small_denominator_exclusion`: GREEN; $\rho=0$ remains
    with the prior exact owner and no denominator is silently removed.
14. `generic_tge2_cross_and_downstream_scope`: GREEN; no growing-scale
    generic, $t\ge2$, cross, M1, M2, endpoint, M9, bridge, target, or
    exponent claim is made.

## 7. Recommended state effect

Close under

$$
 \boxed{\mathsf{strict\_moving\_coefficient\_collar\_range}.}
\tag{150.C31}
$$

Subject to independent seam reviews, promote:

1. the exact two-row incidence expansion (150.C7)--(150.C10) and the
   half-weight norm (150.C11);
2. the fixed-wrap and target-safe packet bounds (150.C2)--(150.C4);
3. the actual-profile bounded-$M$ full-row edge (150.C5), only after
   variation and second-derivative review; and
4. the shifted-factor positivity, fixed-shift divisor bound, and
   scoped all-shift absolute-summation no-go.

Retain as open the growing-$M$ large-wrap collar (150.C29), the
growing-$M$ generic complement, the signed $RD$ scalar, all $t\ge2$
layers, the independent Round-138 cross owner, M9--M1, M9--M2,
endpoint uniformity, M9, the bridge, and the Gauss target.  The global
exponents do not change.

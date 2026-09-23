# Round 172 discovery report: literal maximal Fejer dyadic-frequency attack

Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate  
Task: literal_maximal_fejer_dyadic_frequency_attack  
Role: discovery  
Graph: c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853  
Status: candidate evidence only

## 1. Result

The exact parity-Fejer, integer-chain, short-correction, triangular-tent,
doubling-Haar, and terminal non-doubling identities all pass.  Put
\(S=\min(2R_0,M)\).  Whenever \(S>R_0\), the first dyadic link
\(R_0=\lceil L\rceil\to S\) has the actual-coefficient local bound

\[
 \left|\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}\right|
 \le (S+R_0)D_L
 \le3R_0D_L\ll_\varepsilon L^3X^\varepsilon.
\tag{172.D1}
\]

This includes the terminal non-doubling case \(S=M<2R_0\).  Its
complement is not target-safe, so this uncomplemented local bound is not
an owner-complete strict sector and does not prove (165.K26).

There is an exact finite-support character--ordinary-Poisson transform at
the common Fejer frequency.  Its ordinary zero mode is target-safe.  The
first exact no-go is thereafter: the zero physical diagonal of an
adjacent-scale Fejer bandpass is not a zero dual-mode diagonal.  A fixed
dual mode still couples two continuous cardinal cells of unequal product.
The physical zero diagonal is recovered only after all dual diagonal,
dual off-diagonal, frequency-endpoint, physical-endpoint, and
zero-extension transition terms are recombined.

Consequently no dual-mode-wise or product-cell-wise modulus is licensed.
The first positive estimate is only

\[
 |\mathfrak E_V^{(2)}-\mathfrak E_U^{(2)}|
 \le (U+V)D_L.
\tag{172.D2}
\]

At \(V\asymp M_L\asymp L^2\), this is
\(L^4X^\varepsilon\), one factor \(L\) above the target.  A coherent
dechirped one-parity array attains this order, so no coefficient-uniform,
Parseval-only, Haar-only, or positive-dual-mode argument can improve it.
The exact transform is invertible; positive dual summation self-returns
to this capacity and, after smooth Möbius opening, to the accepted
Round-162/169 product collar.

The scoped result is therefore
maximal_fejer_dyadic_character_poisson_no_go.  It does not prove or
disprove (165.K26).  A proof requires a new signed theorem for the complete
nonzero dual-mode aggregate before positivity.

## 2. Exact statement and hypotheses

Let \(e(t)=e^{2\pi it}\), \(J=\sqrt X\),
\(1\ll L\ll H\le J^{1/2}\), \(R_0=\lceil L\rceil\), and
\(M=M_L\asymp L^2\).  Retain

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d),
\tag{172.D3}
\]

where \(\lambda_N(d)\) contains the supported squarefree/coprime row,
the normalization, selected neither/both selector or no-pair value one,
both complementary parity branches, every profile, floor, star, crossing,
endpoint, hard point value, and zero-extension value.  On a nonzero atom,
\(N=dm\asymp L^2\), \(d,m\asymp L\), \(d\) is odd,
\(m=2^\nu m_o\) with \(\nu\in\{0,1\}\), and
\(|\lambda_N(d)|\ll1\).  All other point values are zero.  Put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\quad
 Z(\theta)=\sum_Nz_Ne(N\theta),\quad
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{172.D4}
\]

The square root is evaluated only on positive literal support.  Define

\[
 F_R(\theta)=\sum_{|h|<R}(1-|h|/R)e(h\theta),\qquad
 K_R^{(2)}(\theta)=\frac{F_R(\theta)+F_R(\theta+1/2)}2,
\]

\[
 \mathfrak E_R^{(2)}
 =\int_0^1|Z(\theta)|^2K_R^{(2)}(\theta)\,d\theta.
\tag{172.D5}
\]

For integers \(1\le U<V\le M\), put

\[
 b_{U,V}(h)=(1-|h|/V)_+-(1-|h|/U)_+,\qquad
 B_{U,V}=F_V-F_U.
\tag{172.D6}
\]

The question is whether the exact common-frequency transform of
\(\Delta_{U,V}:=\mathfrak E_V^{(2)}-\mathfrak E_U^{(2)}\)
produces a factor \(L\) before any positive norm.

## 3. Proof and derivation

### Parity, dyadic, tent, Haar, and endpoint ledgers

Set

\[
 Z_\epsilon(\theta)=\sum_N(-1)^{\epsilon N}z_Ne(N\theta),
 \qquad \epsilon\in\{0,1\}.
\]

Changing frequency by \(1/2\) in the second peak gives

\[
 \mathfrak E_R^{(2)}
 =\frac12\sum_{\epsilon=0}^1
   \int_0^1F_R(\theta)|Z_\epsilon(\theta)|^2\,d\theta
 =D_L+2\!\sum_{\substack{0<r<R\\2\mid r}}(1-r/R)A_r,
\tag{172.D7}
\]

where \(A_r=\Re\sum_Nz_{N+r}\overline{z_N}\).  Since \(d\) is odd,
the twist is \((-1)^{\epsilon m}\); the odd-\(m\) and even-\(m\)
branches remain distinct.  Full-line zero extension gives exactly

\[
 \Delta_{U,V}
 =2\!\sum_{\substack{r>0\\2\mid r}}b_{U,V}(r)A_r,
 \qquad b_{U,V}(0)=0.
\tag{172.D8}
\]

For \(V=2U=2R\),

\[
 b_{R,2R}(r)=
 \begin{cases}
 r/(2R),&0<r<R,\\
 1-r/(2R),&R\le r<2R,\\
 0,&r\ge2R.
 \end{cases}
\tag{172.D9}
\]

For the terminal \(R<M<2R\),

\[
 b_{R,M}(r)=
 \begin{cases}
 r(M-R)/(RM),&0<r<R,\\
 1-r/M,&R\le r<M,\\
 0,&r\ge M.
 \end{cases}
\tag{172.D10}
\]

Thus the final link uses (172.D10), not a rounded Haar identity.

For a full-line sequence \(v\), define

\[
 \mathcal E_R(v)=R^{-1}\sum_s\left|\sum_{j<R}v_{s+j}\right|^2,
\]

\[
 \mathcal H_R(v)=(2R)^{-1}\sum_s
 \left|\sum_{j<R}v_{s+j}-\sum_{j<R}v_{s+R+j}\right|^2.
\]

The parallelogram identity yields
\(\mathcal E_{2R}=2\mathcal E_R-\mathcal H_R\).  Averaging it for
\(z_N\) and \((-1)^Nz_N\) gives, only at exact doublings,

\[
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.
\tag{172.D11}
\]

Along \(R_{j+1}=\min(2R_j,M)\), with repetitions removed,

\[
 T_{26}=\frac12\sum_{j<K}\Delta_{R_j,R_{j+1}}-B_{\rm short},
\]

\[
 B_{\rm short}=
 \sum_{\substack{0<r<R_0\\2\mid r}}
 \bigl((1-r/M)-(1-r/R_0)\bigr)A_r.
\tag{172.D12}
\]

Since \(|A_r|\le D_L\),
\(|B_{\rm short}|\ll R_0D_L\ll_\varepsilon L^3X^\varepsilon\).
This is the single short-shift payment.

Also \(\|F_R\|_\infty=R\) and
\(\|Z_\epsilon\|_2^2=D_L\), proving (172.D2) and the local
first-link estimate (172.D1).  When \(S=M<2R_0\), this estimate uses
the exact terminal coefficient (172.D10), not the doubling Haar identity.

### Exact common-frequency finite-support transform

Choose \(\varphi\in C_c^\infty((-1/2,1/2))\) with
\(\varphi(0)=1\), and define

\[
 \mathcal W_\epsilon(x,y)=
 \sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)=
 \mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\tag{172.D13}
\]

Every cell lies in \(x,y\asymp L>0\).  No two literal atoms are smoothed
together: every selector, no-pair row, squarefree/coprime hole, two-adic
branch, profile point, endpoint, and zero-extension jump is retained.
Let \(\widetilde{\mathcal B}\) denote the two-dimensional Fourier
transform.  Ordinary Poisson and exact character Poisson give, uniformly
in the same \(\theta\),

\[
 \boxed{
 Z_\epsilon(\theta)=\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).}
\tag{172.D14}
\]

There is no character zero mode.  Substitution before every modulus gives

\[
 \boxed{\begin{aligned}
 \Delta_{U,V}=\frac18\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\ {\rm odd}\\\ell,\ell'\in\mathbb Z}}
 \chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{U,V}(\theta)
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell)
 \overline{\widetilde{\mathcal B}_{\epsilon,\theta}(k'/4,\ell')}
 \,d\theta .
 \end{aligned}}
\tag{172.D15}
\]

There is one real part outside the full aggregate.

### Endpoint/transition kernel and dual-diagonal no-go

Let

\[
 \mathscr B_{U,V}(t)=\int_0^1B_{U,V}(\theta)e(t\theta)\,d\theta,
 \qquad I(u)=\int_0^1e(u\theta)\,d\theta.
\]

Then exactly

\[
 \mathscr B_{U,V}(t)=\sum_{h\in\mathbb Z}b_{U,V}(h)I(t+h).
\tag{172.D16}
\]

For integer \(n\),
\(\mathscr B_{U,V}(n)=b_{U,V}(n)\), so the physical tent and zero
diagonal are exact.  For noninteger \(t\), integration by parts exposes

\[
 \mathscr B_{U,V}(t)
 =\frac{(e(t)-1)(V-U)}{2\pi it}
 -\frac1{2\pi it}\int_0^1B'_{U,V}(\theta)e(t\theta)\,d\theta,
\tag{172.D17}
\]

because \(B_{U,V}(0)=B_{U,V}(1)=V-U\).  It is not a compact tent.

Expanding (172.D15) gives the kernel
\(\mathscr B_{U,V}(xy-x'y')\).  Even on the nominal dual diagonal
\((k,\ell)=(k',\ell')\), the two continuous cells are independent and
generically \(xy\ne x'y'\).  Hence that dual diagonal is not killed.
The physical zero diagonal appears only after dual diagonal,
dual off-diagonal, and all endpoint/transition terms recombine.

A lattice-constant interpolation would preserve the physical tent, but
then the transform is only an invertible change of basis of the original
finite array and has no product-phase stationary saving.  Its first
positive norm is again (172.D2).  Thus one cannot keep both a
product-phase transform and a separately vanishing dual diagonal.

### Zero-mode and restored-power ledgers

The ordinary zero component equals

\[
 Z_{\epsilon,0}(\theta)
 =\sum_d\chi_4(d)\int_{\mathbb R}
   \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\tag{172.D18}
\]

On support,

\[
 \partial_y(J\sqrt{dy}+\theta dy)
 =\frac J2\sqrt{d/y}+\theta d\asymp J
 \quad(0\le\theta\le1).
\]

One integration by parts per compact cell and the
\(O(L^2X^\varepsilon)\) atom count give

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\varepsilon L^2J^{-1}X^\varepsilon.
\tag{172.D19}
\]

Therefore every bandpass term containing at least one ordinary zero mode
is

\[
 \ll_\varepsilon (U+V)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon,
\tag{172.D20}
\]

using \(U+V\ll L^2\) and \(L^2\le J\).  The obstruction is the signed
\(\ell,\ell'\ne0\) aggregate.  Taking a modulus there restores

\[
 (U+V)D_L\asymp L^4X^\varepsilon
\tag{172.D21}
\]

at the top scale.

This restored capacity is sharp for general coefficients by an
in-range hostile construction.  Let \(M=4P\), put \(z_N=1\) on the
exactly \(2P\) even sites

\[
 N=0,2,\ldots,4P-2
\]

of the containing interval \([0,M-1]\), and put \(z_N=0\) elsewhere;
equivalently take \(c_N=e(-J\sqrt N)\) on the positive translated copy
of these sites.  Then \(D=2P\), \(A_{2s}=2P-s\) for
\(1\le s<2P\), and the legitimate terminal doubling link
\(2P\to4P=M\) satisfies

\[
\begin{aligned}
 \Delta_{2P,4P}
 &=2\sum_{s=1}^{2P-1}b_{2P,4P}(2s)(2P-s)\\
 &=\frac1P\left\{
 \sum_{s=1}^{P-1}s(2P-s)
 +\sum_{s=P}^{2P-1}(2P-s)^2\right\}
 =P^2.
\end{aligned}
\tag{172.H15}
\]

Thus \(\Delta_{2P,4P}=MD/8\asymp M^2\asymp L^4\), with
both the support and the link lying inside the frozen interval and scale
range.  This is a false-control array, not literal residual mass.  It
proves that the missing factor must come from the complete signed literal
symbol before positivity.

## 4. First doubtful or unproved step

After the first link, short correction, and ordinary zero modes are paid,
the first unproved statement is, for every remaining chain link,

\[
\begin{aligned}
 \frac18\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\ {\rm odd}\\\ell,\ell'\ne0}}
 \chi_4(k)\chi_4(k')
 \int_0^1B_{U,V}(\theta)
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell)\\
 &\hspace{28mm}\times
 \overline{\widetilde{\mathcal B}_{\epsilon,\theta}(k'/4,\ell')}
 \,d\theta
 \ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\tag{172.D23}
\]

No dual diagonal can be deleted and no modulus can be inserted before the
full sum.  The permitted context contains no estimate for (172.D23).
The first positive replacement is (172.D21), so this is the smallest
exact route-specific no-go.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| literal_residual_coefficient_domain | Pass: (172.D3) is retained pointwise. |
| one_outer_real_part | Pass: one real part surrounds (172.D15)/(172.D23). |
| even_parity_fejer_projection | Pass: both peaks and both absolute parities occur in (172.D7). |
| integer_doubling_chain_and_final_link | Pass: (172.D9) and exact terminal (172.D10). |
| short_shift_correction_once | Pass: (172.D12), paid once. |
| triangular_tent_zero_diagonal | Pass: (172.D9)--(172.D10), \(b(0)=0\). |
| haar_detail_identity_scope | Pass: (172.D11) only for exact doubling. |
| finite_character_poisson_common_frequency | Pass as identity: (172.D14)--(172.D15). |
| original_zero_boundary_transition_modes | Pass for retention: character zero absent, ordinary zero paid, boundary transition retained in (172.D17). |
| dual_off_diagonal_before_positive_sum | Open/no-go: the full signed sum (172.D23) is required. |
| selected_and_no_pair_rows | Pass: both remain inside \(\lambda_N(d)\); no-pair all-\(1\bmod4\) rows forbid assumed balance. |
| squarefree_coprimality_and_two_adic_branches | Pass: exact holes remain; \(\nu_2(m)=0,1\) are separated by the parity twist. |
| profile_endpoint_and_zero_extension | Pass for retention: disjoint cardinal cells preserve all point values and jumps. |
| factor_L_before_positive_norm | Fail: (172.D21) is \(L^4X^\varepsilon\). |
| collar_self_return_and_restored_power | Fail for this route: positive transformed modes return to the accepted collar/involution. |
| residual_only_owner_quarantine | Pass: only K26 and the residual \(t=1\) scalar are in scope. |
| no_in_round_pivot | Pass. |
| no_status_or_exponent_overpromotion | Pass. |

A one-site sequence has zero increment and forces full dual recombination.
The in-range dechirped control (172.H15) gives sharp positive capacity.  No-pair
positive character mass prevents fictitious per-product balance.  No
numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only the permitted files were used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round172_m2_hard_top_t1_residual_maximal_fejer_dyadic_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/barrier_packet.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_variable_scale_fejer_bypass.md;
- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md;
- rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reviews/conductor_round170_adjudication.md.

No external theorem, web source, or numerical computation was used.

## 7. Recommended state effect

Retain (165.K26) and the complete residual \(t=1\) scalar as open.  Retain
the first-link estimate (172.D1), with \(S=\min(2R_0,M)\), as local
candidate evidence only.  Its complement is not target-safe, so it is not
a strict-sector promotion.

After independent review, record the route-scoped obstruction
maximal_fejer_dyadic_character_poisson_no_go: the exact transform is
(172.D14)--(172.D15), its ordinary zero mode is target-safe, but the
transformed diagonal cancels only after full dual/endpoint/cell
recombination, and every currently licensed positive norm restores
\(L^4X^\varepsilon\).  A continuation must prove the fully signed
aggregate (172.D23) before positivity.

Do not change M9--M2, M9, either bridge, the quarter theorem, or any
global exponent.  Recommended Round-172 terminal label:
maximal_fejer_dyadic_character_poisson_no_go.

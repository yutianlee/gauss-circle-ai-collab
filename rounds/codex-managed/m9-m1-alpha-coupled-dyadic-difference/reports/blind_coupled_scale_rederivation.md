# 1. Result

**No-go lemma (lawful coupled difference, but no capacity saving from the
packet alone).**  After zero-extending both adjacent scales to one ambient
support, the lawful finite difference is

\[
 \Delta_f\mathcal A_j=\widetilde{\mathcal A}_{j+1}
                         -\widetilde{\mathcal A}_{j},
\]

with both finite masks retained, and the lawful returned difference is

\[
 \Delta_p\mathscr B_j(n,q)=\widetilde{\mathscr B}_{j+1}(n,q)
                            -\widetilde{\mathscr B}_{j}(n,q),
\]

with the two profile stars, the top owner when present, the common product
star, and the two height supports retained.  For an interior pair, writing
\(h=H_j\) and

\[
 \rho_h:=\frac{H_{j+1}+1}{H_j+1}
 =\frac{\lfloor h/2\rfloor+1}{h+1},
\]

the overlap part of the finite difference is exactly

\[
 \widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(h+1)^v
 \left(2^{-u}\rho_h^{\,v}\widehat W_{j+1}(u)
             -\widehat W_j(u)\right).                 \tag{1}
\]

Thus the complete Mellin multiplier in parentheses, not merely a formal
variation in \(H\), survives.  After physical return, the complete survivor
is

\[
 V_{j+1}^*(2z_j)\phi\!\left(\frac n{H_{j+1}+1}\right)
 -V_j^*(z_j)\phi\!\left(\frac n{H_j+1}\right),
 \qquad z_j=\frac{2\sqrt{Xn/q}}{D_j},                 \tag{2}
\]

on the common support, together with the one-sided terms on the symmetric
difference of the two supports.  The raw identity
\(W(t)=\eta(t)-\eta(2t)\) telescopes the unweighted raw profiles, but it does
not telescope the products in (1) or (2): the height factor changes by a
fixed dyadic amount and leaves an interior height-difference term.

The unweighted sum of *complete adjacent differences* does telescope, but
only tautologically:

\[
 \sum_{j=a}^{b}(T_{j+1}-T_j)=T_{b+1}-T_a.             \tag{3}
\]

Consequently its unconditional estimate is only
\(|T_{b+1}|+|T_a|\).  With scale signs or weights, all interior blocks return
through the weight variation.  No signed partial-sum estimate for the actual
arithmetic/phase antecedent is stated in the packet.  Hence (1)--(3) imply no
reduction of an available normalized \(X^{1/8}\) lattice-capacity bound.

# 2. Exact statement and hypotheses

Assume only the data in the derivation packet.  Thus
\(D_{j+1}=D_j/2\), \(H_j=\lfloor D_jX^{-1/4}\rfloor\),
\(H_{j+1}=\lfloor H_j/2\rfloor\), and physical return has already been
licensed separately for each completed scale block.  No commutation of that
return with a finite mask, an outside-height limit, or a decomposition of
\(W\) is assumed.

For the finite antecedent, let \(R_j\) denote its exact finite positive-line
support, including its own mask connectors and boundary convention.  On
\(R_{j,j+1}:=R_j\cup R_{j+1}\), let \(m_j\mathcal A_j\) and
\(m_{j+1}\mathcal A_{j+1}\) be their zero extensions; \(m_k\) is notation
for the already existing connector, not a replacement for it.  Then the
common-support definition is

\[
\begin{aligned}
 \Delta_f\mathcal A_j(u,v)
  ={}&\widehat\phi(v)
      \left(\frac{D_j}{2\sqrt X}\right)^u(h+1)^v \\
 &\times\left[
 m_{j+1}(u,v)2^{-u}\rho_h^{\,v}\widehat W_{j+1}(u)
 -m_j(u,v)\widehat W_j(u)\right].                    \tag{4}
\end{aligned}
\]

Formula (1) is (4) only where both connectors equal their interior values;
on \(R_j\triangle R_{j+1}\), the corresponding one-sided connector term in
(4) is compulsory.

For physical return, let \(\Omega_j\) be the exact support owned by scale
\(j\), including its scale-profile boundary and height support but not
conflating either with the common product boundary.  Define
\(\widetilde{\mathscr B}_j\) on
\(\Omega_{j,j+1}:=\Omega_j\cup\Omega_{j+1}\) to equal the packet's starred
profile on \(\Omega_j\) and zero elsewhere.  Then

\[
\begin{aligned}
 \Delta_p\mathscr B_j(n,q)
 ={}&\widetilde{\left[
 V_{j+1}^*(2z_j)
 \phi\!\left(\frac n{\lfloor h/2\rfloor+1}\right)\right]} \\
 &-\widetilde{\left[
 V_j^*(z_j)\phi\!\left(\frac n{h+1}\right)\right]}. \tag{5}
\end{aligned}
\]

If \(c(n,q)\) denotes the inherited common arithmetic and phase factor and
\(s_N(n,q)\) the inherited product-star weight at \(nq=N_X\), the complete
returned difference block is

\[
 \Delta T_j=X^{1/4}\!\sum_{(n,q)\in\Omega_{j,j+1}}
 c(n,q)s_N(n,q)\,\Delta_p\mathscr B_j(n,q),           \tag{6}
\]

where the displayed \(X^{1/4}\) is attached once to the whole block.  A
different convention for the word normalization changes neither the
identities nor the conclusion; the essential ownership assertion is that it
is not duplicated when two scales are subtracted.

The exact owner table is:

| object | owner at scale \(j\) | owner at scale \(j+1\) | common-support treatment |
|---|---|---|---|
| dyadic length | \(D_j\) | \(D_j/2\) | retain both arguments; \(z_{j+1}=2z_j\) |
| finite Mellin factor | \(D_j^u(h+1)^v\widehat W_j(u)\) | \((D_j/2)^u(\lfloor h/2\rfloor+1)^v\widehat W_{j+1}(u)\) | subtract as in (4), with no uniform \(H\mapsto H+1\) variation |
| finite connector | \(m_j\) and its boundary | \(m_{j+1}\) and its boundary | union support and zero extension; keep symmetric-difference terms |
| returned scale profile | \(V_j^*(z_j)\) | \(V_{j+1}^*(2z_j)\) | each profile star stays with its own summand |
| height | cutoff/profile at \(H_j=h\) | cutoff/profile at \(H_{j+1}=\lfloor h/2\rfloor\) | each is zero-extended from its own support; a height equality is not a profile star |
| product boundary | \(nq=N_X\) | the same \(nq=N_X\) | one common product-star weight multiplies the completed difference |
| top | \(w_0(d)={\bf1}_{d\le y}W(d/y)\) when \(j=0\) | ordinary scale only if it is interior | retain the top indicator and top-profile star; do not replace \(w_0\) by an interior \(E_0-E_1\) formula |
| bottom | final active profile and separately safe inactive profile | as applicable | retain the last active endpoint; invoke bottom safety only for the separately identified inactive owner |
| arithmetic, phase, normalization | common factor stated in the packet | common factor stated in the packet | apply after profile subtraction; normalization occurs once |

The conclusions below concern only the adjacent-difference object and any
scale interval for which all the foregoing owners have been aligned.  They
do not identify the original sum of scale blocks with a sum of their
differences.

# 3. Proof or derivation

First, for every real \(x\),
\(\lfloor x/2\rfloor=\lfloor\lfloor x\rfloor/2\rfloor\).  Applying this to
\(x=D_jX^{-1/4}\) proves the stated height coupling.  If \(h=2k\), then

\[
 \rho_h=\frac{k+1}{2k+1};
\]

if \(h=2k+1\), then \(\rho_h=1/2\).  In particular, away from the inactive
case \(h=0\), this is a fixed dyadic change, not \(1+O(h^{-1})\).  Substituting
\(D_{j+1}=D_j/2\) and
\(H_{j+1}+1=\rho_h(h+1)\) into the two finite summands gives (4).  This also
proves that replacing \((H_{j+1}+1)^v-(H_j+1)^v\) by a boundary-size error on
an unrestricted finite \(v\)-rectangle is not licensed: the exact factor is
\(\rho_h^{\,v}\), which may have full bulk size.

Second, set \(E_j(d)=\eta(d/D_j)\).  For every interior scale,

\[
 w_j(d)=E_j(d)-E_{j+1}(d).                            \tag{7}
\]

Therefore

\[
 \sum_{j=a}^{b}w_j(d)=E_a(d)-E_{b+1}(d),             \tag{8}
\]

but the adjacent profile difference itself is

\[
 w_{j+1}(d)-w_j(d)
 =2E_{j+1}(d)-E_j(d)-E_{j+2}(d),                     \tag{9}
\]

and

\[
 \sum_{j=a}^{b}(w_{j+1}-w_j)=w_{b+1}-w_a.           \tag{10}
\]

Thus (8) is a telescope of the raw profiles and (10) is merely the endpoint
identity for first differences; neither is a smallness estimate.  Indeed,
the packet's support facts imply \(W(t)=1\) for \(2/3\le t\le1\).  On that
core, \(W(2t)=0\), so an interior adjacent raw-profile difference has value
\(-1\).  Adjacent differencing has full pointwise profile amplitude on this
core.

The top cannot silently enter (8): for an interval beginning at zero the
lawful identity is

\[
 w_0(d)+\sum_{j=1}^{b}w_j(d)
 ={\bf 1}_{d\le y}W(d/y)+E_1(d)-E_{b+1}(d),          \tag{11}
\]

with the top boundary convention still attached to the first term.  The
bottom contribution in (8) or (11) is likewise an endpoint until the
separate inactive-profile result is applied to that exact owner.

Third, raw telescoping fails for the coupled product.  For arbitrary height
factors \(F_j\), direct expansion of (7) gives the exact identity

\[
 \sum_{j=a}^{b} w_j(d)F_j
 =E_a(d)F_a-E_{b+1}(d)F_b
  +\sum_{j=a+1}^{b}E_j(d)(F_j-F_{j-1}).              \tag{12}
\]

Both boundary terms and the interior height-difference term are present.
For the finite Vaaler supports, the shell

\[
 H_{j+1}<r\le H_j
\]

contains exactly \(H_j-H_{j+1}=\lceil H_j/2\rceil\) integer height indices.
On it the smaller-height factor is zero while the larger-height factor is
\(\Phi(r/(H_j+1))\).  The packet supplies no estimate making this shell or
its actual arithmetic sum negligible.  After return, on the overlap of the
two supports, (5) has the exact algebraic decomposition

\[
\begin{aligned}
 \Delta_p\mathscr B_j
={}&\bigl(V_{j+1}^*(2z_j)-V_j^*(z_j)\bigr)
       \phi\!\left(\frac n{H_{j+1}+1}\right)\\
 &+V_j^*(z_j)\left[
       \phi\!\left(\frac n{H_{j+1}+1}\right)
      -\phi\!\left(\frac n{H_j+1}\right)\right].   \tag{13}
\end{aligned}
\]

The second line is the physical height survivor.  On
\(\Omega_j\setminus\Omega_{j+1}\), the survivor is instead exactly
\(-\mathscr B_j\); on
\(\Omega_{j+1}\setminus\Omega_j\), it is exactly
\(+\mathscr B_{j+1}\).  No profile star or product star alters these
ownership statements.  The packet does not state an identity transporting
the individual \(E_j\) pieces through the physical return, so (12) may not be
promoted termwise to a returned \(E\)-profile identity.  Equation (13), which
uses only the licensed returned profiles, is the lawful returned statement.

Fourth, let \(T_j\) be the completed returned block with the same ambient
support, common arithmetic/phase factor, stars, and single normalization as
in (6).  Linearity proves (3).  More generally, for any scale weights
\(\lambda_j\),

\[
 \sum_{j=a}^{b}\lambda_j(T_{j+1}-T_j)
 =\lambda_bT_{b+1}-\lambda_aT_a
  +\sum_{j=a+1}^{b}(\lambda_{j-1}-\lambda_j)T_j.      \tag{14}
\]

This displays both endpoint terms.  In particular, arbitrary signs return
an interior block at every sign change.

The corresponding Abel identity shows precisely what additional theorem
would be needed.  If the actual scale antecedent is \(c_j=Q_j-Q_{j-1}\),
then, pointwise in the other variables and hence also after the lawful
finite summation,

\[
 \sum_{j=a}^{b}c_j\mathscr B_j
 =Q_b\mathscr B_b-Q_{a-1}\mathscr B_a
  +\sum_{j=a}^{b-1}Q_j(\mathscr B_j-\mathscr B_{j+1}).\tag{15}
\]

The two boundary terms in (15) and a bound for every *actual signed partial
sum* \(Q_j\) are indispensable.  Nothing in the packet bounds \(Q_j\).

Finally, define the absolute lattice-capacity seminorm using exactly the
common coefficient, product-star weight, and one external normalization in
(6).  Triangle inequality gives

\[
 \|\Delta_p\mathscr B_j\|_{\rm cap}
 \le \|\mathscr B_{j+1}\|_{\rm cap}
    +\|\mathscr B_j\|_{\rm cap},                     \tag{16}
\]

and (14) gives the analogous endpoint-plus-total-variation bound.  Hence if
the only per-scale information is normalized capacity
\(O(X^{1/8})\), the consequence of (16) is still only
\(O(X^{1/8})\), with no power saving.  This limitation is sharp at the level
of the supplied information: at any lattice point where the survivor (5)
is nonzero, a coefficient supported there and phased to its conjugate
saturates the pointwise absolute bound.  This is an information-theoretic
countermodel, not a claim that the unstated actual arithmetic coefficient is
freely choosable.  It proves that profile algebra alone cannot certify
cancellation in that actual coefficient.

# 4. First doubtful or unproved step

The first invalid step would be to replace the left side of (12) by only
\(E_aF_a-E_{b+1}F_b\).  That replacement applies the raw \(W\)-telescope as
if the height factor were independent of scale; the exact omitted term is

\[
 \sum_{j=a+1}^{b}E_j(F_j-F_{j-1}),
\]

and the height changes dyadically.  If this survivor is honestly retained,
the next unproved step is any assertion that (14) or (15) saves a power: such
an assertion requires a signed partial-sum bound for the actual
arithmetic/phase antecedent \(Q_j\), plus control of both boundary terms.
Neither appears in the packet.

# 5. Control tests and outcomes

| required control | outcome |
|---|---|
| `common_support` | **Pass.** Equations (4) and (5) use the union of the two exact supports and zero extension.  Symmetric-difference terms remain explicit. |
| `finite_vs_physical` | **Pass.** The finite multiplier (4) and licensed returned profile (5) are stated separately.  No mask, limit, or return is interchanged. |
| `profile_telescoping` | **Pass/no-go.** Equations (7)--(12) give the exact telescope, the adjacent second difference, and the coupled height survivor.  Unit amplitude on the raw core rules out pointwise smallness of the adjacent difference. |
| `height_coupling` | **Pass/no-go.** The exact parity formula for \(\rho_h\) is retained.  The deleted height shell has \(\lceil H_j/2\rceil\) indices, and (13) retains the returned height difference. |
| `top_bottom_ownership` | **Pass.** Equation (11) keeps the special top indicator/star; the last active bottom endpoint is not identified with the separately safe inactive profile. |
| `all_star_ownership` | **Pass.** Each \(V_k^*\) keeps its own profile star, the top star stays with \(w_0\), the height equality remains a height owner, and the common product star stays outside the completed difference. |
| `signed_partial_sums` | **No target estimate follows.** Equations (14) and (15) are the exact identities; the required bound on the actual \(Q_j\) is absent. |
| `boundary_terms` | **Pass.** Both scale endpoints occur in (12), (14), and (15); none is discarded as a formal telescope. |
| `alpha_capacity_scope` | **No reduction.** The one external \(X^{1/4}\) normalization is used once, and triangle inequality preserves the named normalized \(X^{1/8}\) capacity scale. |
| `downstream_scope` | **Pass.** The result controls only completed adjacent differences.  It neither rewrites the original scale sum nor supplies an aggregate physical-return or signed-arithmetic theorem. |

# 6. Dependencies and artifacts used

The derivation uses only the definitions, distinctions, and completion rule
in `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/derivation_packet.md`.
No external theorem, literature source, numerical experiment, symbolic
computation, proof graph, proof draft, prior report, synthesis, or other
Round-53 artifact is used.

# 7. Recommended state effect

**Retain as a no-go result; reject promotion of an \(X^{1/8}\)-saving scale
difference theorem.**  The exact common-support identities (4)--(6), the
owner table, and the boundary identities (12), (14), and (15) are suitable
candidate evidence.  A positive downstream promotion would require a new,
separately proved bound for the actual signed partial sums \(Q_j\) (including
both endpoint owners), or an accepted aggregate physical identity that
controls the explicit height/profile survivor.  Neither may be inferred
from the raw \(W\)-telescope.

# Isolation ledger

- Read: `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/briefs/blind_coupled_scale_rederivation.md`.
- Read: `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/derivation_packet.md`.
- Wrote only: `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/reports/blind_coupled_scale_rederivation.md`.
- Explicitly not accessed: proof graph, proof draft, proof-obligation state,
  campaign state, prior reports, prior syntheses, legacy rounds, and other
  Round-53 work.
- External sources and computational experiments: none.

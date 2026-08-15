# Hostile audit of the complete coupled dyadic-scale difference

- Campaign: m9-m1-alpha-coupled-dyadic-difference
- Research round: 53 (alpha_complete_coupled_dyadic_difference)
- Task: coupled_scale_hostile_audit
- Role: seam_reviewer
- Graph SHA-256 supplied in the brief: ffe8d5a79d866395f674ea77294da69c3d8f24ef09072bf36aa7fb3c2287c3a8
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**Actual-profile absolute-capacity no-go, with a finite-\(v\) bulk
survivor.** On two adjacent interior scales, put \(H=H_j\) and
\(K=H_{j+1}=\lfloor H/2\rfloor\). The finite Mellin scale-height
multiplier has the exact difference

\[
 \mathcal A_{j+1}(u,v)-\mathcal A_j(u,v)
 =\widehat W(u)\widehat\phi(v)
  \left(\frac{D_j}{2\sqrt X}\right)^u(H+1)^v
  \left\{2^{-u}\left(\frac{K+1}{H+1}\right)^v-1\right\}.
 \tag{53.1}
\]

This is a common-finite-line identity for interior scales; it is not yet a
physical star identity. Its braced factor has full bulk size on a bounded
imaginary-\(v\) slice. Indeed, if \(u=a>0\), \(v=b+i\tau_H\), and

\[
 r_H=\frac{K+1}{H+1},\qquad
 \tau_H=\frac{\pi}{|\log r_H|},
\]

then \(1/2\le r_H\le2/3\),
\(\pi/\log2\le\tau_H\le\pi/\log(3/2)\), and

\[
 \left|2^{-a}r_H^{\,b+i\tau_H}-1\right|
 =1+2^{-a}r_H^b\ge1.                                      \tag{53.2}
\]

Thus no \(H^{-1}\), \(D^{-1}\), or \(X^{-\delta}\) factor can be extracted
uniformly from the adjacent finite scale-height multiplier. Possible zeros
or decay of the two Mellin transforms, and cancellation after all finite
connectors are assembled, are separate questions; (53.2) does not estimate
the complete finite alpha integral.

After the licensed physical return there is a sharper actual-profile
obstruction. On a common ambient lattice, extend every profile by zero and
write, for an interior scale,

\[
 B_j(h,q)=a_{H_j}(h)
 W\!\left(\frac{2\sqrt{Xh/q}}{D_j}\right),\qquad
 a_H(h)={\bf1}_{1\le h\le H}\Phi\!\left(\frac h{H+1}\right).
 \tag{53.3}
\]

The common character, radial phase, product weight, product cutoff/star, and
the single external \(X^{1/4}\) are deliberately outside (53.3). There are
arbitrarily large square \(X\) and one adjacent pair of active interior
scales for which

\[
 \boxed{\;
 \sum_{\substack{q\ {\rm odd}\\q\asymp\sqrt X}}
 q^{-3/4}\,|B_{j+1}(1,q)-B_j(1,q)|\gg X^{1/8}.
 \;}                                                       \tag{53.4}
\]

Every row in (53.4) lies strictly away from the top-profile boundary and the
product boundary, and is supported on exactly one dyadic profile. Hence all
profile and product stars are inert, and there is no hidden boundary owner.
Formula (53.4) realizes the full accepted normalized all-absolute lattice
capacity inside one actual adjacent-scale difference. It refutes
absolute-value, profile-BV, or scale-telescoping closure of the alpha branch.
It is not a signed lower bound: \(\chi _4(q)\), the radial phase, the
projected comb, Plemelj terms, and finite connectors may still cancel only
through a new theorem involving their complete sum.

Moreover, after physical return \(B_j(h,q)\ge0\). For a fixed row all
arithmetic and radial factors are common to \(j\), so scale partial sums have
one common complex phase and nonnegative magnitudes. There is no intrinsic
signed cancellation in the physical scale index. The identity
\(W(t)=\eta(t)-\eta(2t)\) merely transfers the scale sum to top, bottom, and
height-profile differences; it does not reduce (53.4).

This fixed-row sign coherence concerns the original \(B_j\), not the
adjacent differences \(B_{j+1}-B_j\): the latter need not have one sign as
\(j\) varies. They telescope only with the boundary and height-profile owners
in (53.9). On the shell used for (53.4), exactly one original \(B_j\) is
nonzero, so even that telescoping cannot cancel the row internally.

## 2. Exact statement and hypotheses

Assume the packet's exact dyadic construction

\[
 y=\lfloor\sqrt X\rfloor,\quad D_j=2^{-j}y,\quad
 H_j=\lfloor D_jX^{-1/4}\rfloor,
\]

and, on interior scales, \(w_j(d)=W(d/D_j)\), where
\(W(t)=\eta(t)-\eta(2t)\), \(W\ge0\),
\({\rm supp}\,W\subset[1/2,4/3]\), and \(W=1\) on
\([2/3,1]\). Assume the accepted Vaaler profile

\[
 \Phi(x)=\pi x(1-x)\cot(\pi x)+x,\qquad
 \Phi(0)=1,\quad\Phi(1)=0,
\]

which is positive and decreasing on \([0,1)\). The finite identity (53.1)
uses an adjacent pair \(j,j+1\ge1\), so both normalized profile transforms
are the same \(\widehat W\). It assumes the same finite \(u,v\) contours,
regulator, and transform conventions on the two terms. It makes no claim
for the hard top profile, for the inactive bottom remainder, or after a
physical limit.

The packet overloads the letter \(n\). In its two-variable physical profile,
the first argument is the Vaaler frequency; this report renames it \(h\).
In the accepted global angular recombination, the radial product index is
instead \(N=hq\). Thus (53.3) is the packet's profile after the explicit
renaming

\[
 n_{\rm packet}=h,\qquad N_{\rm radial}=hq,
\]

and the product support/star is \(N\le16\sqrt X\). For \(h=1\), the global
weight \(N^{-3/4}\) is exactly \(q^{-3/4}\), which is the weight in (53.4).
No assertion below identifies these two meanings of \(n\).

For the physical capacity assertion, restrict to squares \(X=y^2\), with
\(y\) an integer large enough that the last active index

\[
 J=\max\{k:D_k\ge X^{1/4}\}
\]

satisfies \(J\ge2\), and take \(j=J-1\). Then

\[
 2X^{1/4}\le D_j<4X^{1/4},\qquad
 H_j\in\{2,3\},\qquad H_{j+1}=1.                            \tag{53.5}
\]

Put \(R=X/D_j^2\), so

\[
 \frac{\sqrt X}{16}<R\le\frac{\sqrt X}{4},                 \tag{53.6}
\]

and let

\[
 \mathcal Q_R=
 \left\{q\in2\mathbb Z+1:
          \frac{25}{4}R\le q\le\frac{64}{9}R\right\}.
 \tag{53.7}
\]

For \(q\in\mathcal Q_R\) and \(h=1\), the row is strictly below the accepted
product cutoff \(hq\le16\sqrt X\). The physical theorem is the exact row
identity

\[
 B_{j+1}(1,q)-B_j(1,q)
 =-\Phi\!\left(\frac1{H_j+1}\right),                        \tag{53.8}
\]

and the resulting lower bound (53.4). Absolute values in (53.4) include
\(|\chi _4(q)|=1\), if the character is restored, but deliberately do not
replace the actual signed character-phase sum by a positive one.

For scale telescoping, the exact claim is only the following finite identity.
If \(t_k=2^kt_0\), \(\eta_k=\eta(t_k)\), and \(c_k\) is any scalar sequence,
then

\[
 \sum_{k=L}^{U}c_kW(t_k)
 =c_L\eta_L-c_U\eta_{U+1}
  +\sum_{k=L+1}^{U}(c_k-c_{k-1})\eta_k.                     \tag{53.9}
\]

For the actual row, \(c_k=a_{H_k}(h)\). The top term, bottom term, and every
height-profile difference in (53.9) are mandatory owners. The full
partition also has the separate hard top profile and inactive bottom
remainder from the packet; (53.9) does not silently identify either with an
interior term.

Finally, any Abel use must satisfy the exact finite formula

\[
 \sum_{k=L}^{U}\gamma_kF_k
 =\Gamma_UF_U+\sum_{k=L}^{U-1}\Gamma_k(F_k-F_{k+1}),\qquad
 \Gamma_k=\sum_{r=L}^{k}\gamma_r.                           \tag{53.10}
\]

Thus a bound for the actual signed partial sums \(\Gamma_k\), and the upper
boundary \(\Gamma_UF_U\), are hypotheses, not consequences of taking an
adjacent difference.

## 3. Proof or derivation

For nonnegative \(x\),

\[
 \left\lfloor\frac{x}{2}\right\rfloor
 =\left\lfloor\frac{\lfloor x\rfloor}{2}\right\rfloor,
\]

so \(H_{j+1}=\lfloor H_j/2\rfloor\). On adjacent interior scales the
normalized profile transform is fixed and \(D_{j+1}=D_j/2\). Factoring the
\(j\)-term from the packet's finite expression gives (53.1). If \(H\ge2\),
\(r_H=(\lfloor H/2\rfloor+1)/(H+1)\) lies in \([1/2,2/3]\).
The choice of \(\tau_H\) makes \(r_H^{i\tau_H}=-1\), proving (53.2).
This occurs at a uniformly bounded contour height. It is the finite-\(v\)
bulk term already visible algebraically in

\[
 (K+1)^v a_K(h)-(H+1)^v a_H(h);
\]

the physical unit-height \(O(H^{-1})\) variation cannot be applied uniformly
to it.

For the physical obstruction, (53.5) follows from
\(D_J\in[X^{1/4},2X^{1/4})\). Equations (53.5)--(53.6) follow by doubling
\(D_J\) and squaring. For \(q\in\mathcal Q_R\), put

\[
 t=\frac{2\sqrt{X/q}}{D_j}=2\sqrt{\frac Rq}.
\]

The endpoints in (53.7) give

\[
 \frac34\le t\le\frac45.
\]

Consequently \(W(t)=1\), whereas
\(2t\in[3/2,8/5]\) lies strictly above the support of \(W\). Therefore the
\(j\)-profile is one and the \((j+1)\)-profile is zero. In fact every coarser
argument is below \(1/2\) and every finer argument is above \(4/3\), so the
row is owned by exactly one active scale. Since \(H_j\in\{2,3\}\), \(h=1\)
is a strict height interior point at the surviving scale and

\[
 \Phi\!\left(\frac1{H_j+1}\right)\ge \Phi(1/3)>0.
\]

This proves (53.8). Also

\[
 q\le\frac{64}{9}R\le\frac{16}{9}\sqrt X<16\sqrt X,
\]

so the product-star boundary is not met. The interval in (53.7) has length
\(31R/36\), and hence contains \(\gg R\) odd integers. Since every such
\(q\asymp R\),

\[
 \begin{aligned}
 \sum_{q\in\mathcal Q_R}q^{-3/4}
 |B_{j+1}(1,q)-B_j(1,q)|
 &\gg R\,R^{-3/4}\\
 &=R^{1/4}\gg X^{1/8},
 \end{aligned}
\]

which is (53.4). No endpoint value or star convention enters this proof.
It is therefore an actual-profile, not a surrogate-profile, absolute
capacity obstruction.

This also audits the complete product range: throughout the witness,
\[
 1\le N=hq=q\le\frac{16}{9}\sqrt X<16\sqrt X.
\]
Hence the product indicator is one and its equality star is never sampled.

For (53.9), expand \(W(t_k)=\eta_k-\eta_{k+1}\), shift the second finite
sum by one index, and collect the two endpoints. With
\(c_k=a_{H_k}(h)\), the sequence \(c_k\) is nonincreasing in \(k\). The
Round-52 exact identity gives, whenever \(H_{k-1}>H_k\),

\[
 \sum_h|a_{H_{k-1}}(h)-a_{H_k}(h)|
 =\frac{H_{k-1}-H_k}{2}.                                   \tag{53.11}
\]

Thus a dyadic height step transfers \(H\)-sized coefficient mass into the
bulk sum of (53.9); it does not leave only small endpoint tapers. The
unweighted profile terms in the physical return are nonnegative and their
common character-phase factor is independent of \(k\). Scale partial sums
therefore do not oscillate. Equation (53.10) follows by expanding
\(\Gamma_k\) and collecting coefficients of each \(F_k\); it displays the
boundary term that any scale Abel claim must retain.

The finite and physical calculations cannot be spliced termwise. At finite
height, \(D_j^{i\operatorname{Im}u}(H_j+1)^{i\operatorname{Im}v}\) oscillates
with \(j\), but there are no physical support stars yet. After the licensed
symmetric return, the profiles and stars appear and the scale weights in
(53.3) are nonnegative, but the finite faces, mask connectors, and Plemelj
order have already been used. A saving from finite scale oscillation would
therefore require an aggregate theorem for the complete finite antecedent;
it cannot be inferred from (53.9) or applied after inserting physical stars.

## 4. First doubtful or unproved step

The first unproved step is an actual signed partial-sum estimate in the
arithmetic/lattice variables for the **complete connector-completed finite
alpha antecedent**. Scale algebra supplies no such estimate. On the physical
side the actual \(j\)-weights are nonnegative and the character and radial
phase are common to the scale index, while (53.4) shows that absolute row
accounting already costs \(X^{1/8}\). Any saving must therefore use
cancellation across \(h,q\), the projected comb packets, and the signed
Plemelj/connector operation before absolute values, not cancellation among
dyadic scales.

The packet is also insufficient to certify a literally complete common-owner
table beyond the interior pair. Its physical formula changes notation from
\(\Phi\) to \(\phi\) and from \(W\) to \(V_j^*\), does not define the value of
the profile star at every possible boundary, and refers to inherited radial
and product-star factors without displaying them. Its finite formula does
not display the common regulator, support truncations, radial factor, faces,
or outside-height order. These omissions do not affect the star-free
countercapacity (53.4), but they prevent promotion of a global adjacent-scale
identity with top, bottom, all finite faces, and all collisions owned.

Even after those definitions are restored, an Abel argument must prove its
actual \(\Gamma_k\) bound and retain both boundary owners. Neither
\(W=\eta-\eta(2\cdot)\), the dyadic relation for \(H_j\), nor the positivity
of \(\Phi\) provides that theorem. Finally, (53.4) is not a lower bound for
the fully signed alpha trace: proving or disproving cancellation of
\(\chi_4(q)e(\sqrt{Xhq})\) after the projected comb and all connectors remains
open.

## 5. Control tests and outcomes

- **common_support -- pass for the interior theorem; fail for the claimed
  complete family.** Extending \(a_H\) and \(W\) by zero gives the exact
  common lattice identity (53.8). The packet does not define enough data to
  merge the top profile, inactive bottom, inherited radial pieces, and every
  star into one global owner table.

- **finite_vs_physical -- pass as a separation control.** Equation (53.1)
  is a finite positive-line identity with no physical stars. Equations
  (53.3)--(53.4) begin only after the licensed physical return. No limit or
  connector is commuted between them.

- **profile_telescoping -- proposed saving fails.** The exact identity is
  (53.9), with two boundaries and the complete height-difference bulk. The
  shell (53.7) is supported on exactly one scale, so profile telescoping
  cannot cancel it.

- **height_coupling -- pass/no-go.** The exact relation is
  \(H_{j+1}=\lfloor H_j/2\rfloor\). Equation (53.11) restores \(H\)-sized
  unweighted bulk mass, and (53.2) shows full finite-\(v\) multiplier size at
  a uniformly bounded height.

- **top_bottom_ownership -- fail if omitted.** Formula (53.9) retains
  \(c_L\eta_L\) and \(-c_U\eta_{U+1}\). In the full partition these meet the
  hard top profile and inactive bottom remainder, which are separate owners.
  The countercapacity uses \(j=J-1\), so it does not rely on either boundary.

- **all_star_ownership -- pass for the countercapacity.** Its profile
  argument lies in \([3/4,4/5]\), its product lies strictly below
  \(16\sqrt X\), and its scale is interior. The Vaaler equality cutoff is
  full weight rather than a half-star; at the surviving scale \(1<H_j\).
  Hence no star can halve or remove (53.8). Globally, the product star is
  scale-independent and must be factored outside the adjacent difference,
  while the top-profile star remains a separate boundary owner.

- **signed_partial_sums -- no theorem.** Physical scale partial sums have
  a common row phase and nonnegative profile weights. A signed estimate
  across \(q,h\) or finite connector strata is not supplied by the scale
  identities. Treating adjacent differences as that estimate is circular.

- **boundary_terms -- pass/no-go.** Equations (53.9) and (53.10) display
  the top/bottom and Abel boundary terms explicitly. Dropping
  \(\Gamma_UF_U\), or treating the inactive bottom as zero rather than a
  separately controlled term, is invalid.

- **alpha_capacity_scope -- absolute route falsified; signed route open.**
  Equation (53.4) has the full normalized \(X^{1/8}\) capacity. With the
  unique external \(X^{1/4}\), absolute accounting is of physical size
  \(X^{3/8}\). The result neither proves that the signed trace is this large
  nor rules out a new \(h,q\)-cancellation theorem.

- **downstream_scope -- no implication.** The finite multiplier and
  physical countercapacity prove a scoped no-go only. They do not close the
  alpha outside-height limit, alpha transition, swept operator, post-FE
  vector kernel, M9-M1, M9, or the Gauss-circle target.

No numerical, symbolic, or web experiment was used.

## 6. Dependencies and exact artifacts used

This audit used only its task brief and the permitted selected context:

- rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/briefs/coupled_scale_hostile_audit.md;
- protocol.md;
- state/proof_obligations.yml, specifically the accepted dyadic profile,
  global angular recombination, alpha high-pass no-go, and Vaaler-height
  variation nodes;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/derivation_packet.md;
- rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/reports/vaaler_floor_hostile_audit.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md;
- rounds/codex-managed/m9-m1-alpha-highpass-log-commutator/reports/alpha_commutator_hostile_audit.md.

The imported facts were the exact nonnegative \(W\)-partition and plateau,
the actual global angular row formula and product cutoff, the exact Vaaler
profile and discrete long-height variation, the distinction among physical
stars, and the accepted normalized \(X^{1/8}\) all-absolute capacity. All
adjacent-scale formulas and the shell (53.5)--(53.8) were derived directly.
No other Round-53 report, external theorem, or unlisted artifact was read.

## 7. Recommended state effect

**Promote only a narrow physical absolute-capacity no-go and retain the alpha
bound as open.** The graph may record (53.1)--(53.2) as the finite-\(v\) bulk
obstruction and (53.4)--(53.8) as an actual-profile theorem: one adjacent
interior pair, away from every star and global boundary, has normalized
all-absolute difference mass \(\gg X^{1/8}\). It may also record the exact
weighted telescoping identity (53.9), with top, bottom, and height-difference
owners, and the Abel boundary rule (53.10).

Reject any claim that \(W=\eta-\eta(2\cdot)\), adjacent dyadic differencing,
profile BV, or the Round-52 unit-height estimate by itself reduces alpha
lattice capacity. Do not promote
M9-M1-alpha-bounded-zeta-high-transition-bound: (53.4) is an absolute
obstruction, not a signed lower bound for the complete trace.

The next lawful analytic target is a signed \(h,q\)-partial-sum theorem for
the whole connector-completed finite alpha antecedent, with the actual
\(\chi_4\) factor, radial phase, projected comb, all finite faces and stars,
Plemelj order, and both Abel/outside-height boundary terms retained. Only
such a theorem can supply the missing normalized \(X^{-1/8+o(1)}\) gain and
the separate height-Cauchy gain.

# Round 191 statement-only blind rederivation

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Role: statement-only blind rederiver
- Graph hash: deliberately unavailable under the isolation brief
- Context used: `protocol.md`; `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/blind_statement.md`
- Context not used: proof state, campaign state, strategies, source cards, earlier reports or kernels, sibling work, and conductor analysis
- Date: 2026-08-29

## 1. Result

There are three exact conclusions and one scoped no-go conclusion.

**Abel identity and sign.** For every fixed band label
\(\alpha=(v,\omega)\), with \(z=z_{\omega,v}\), the complete
zero-extension in height gives

\[
 \frac{1}{1-z}\sum_{h\in\mathbb Z}
       \bigl(W_{v,\omega}(h)-W_{v,\omega}(h-1)\bigr)z^h
 =\sum_{h\in\mathbb Z}W_{v,\omega}(h)z^h .
\tag{1.1}
\]

The sign on the right is **positive**. Hence the proposed packet is
exactly

\[
 \boxed{\mathscr J=
 \sum_{\substack{\omega,v\ {\rm literal}\\J\le j_q(a,v)<2J}}
 \sum_h W_{v,\omega}(h)z_{\omega,v}^{\,h}.}
\tag{1.2}
\]

The upper endpoint death of a finitely supported \(W\) is essential in
(1.1). Omitting it changes (1.1) by a boundary term.

**Exact affine comparison.** Put \(c=[\bar v_U]_U\) and
\(\ell=(vc-1)/U\). After the unique anchor reindexing, the old
\((h-1)\)-range and the new \(h\)-range are nested upper rays. In the
plus orientation the new range has at most one geometrically born site
and no geometrically dead site. In the minus orientation it has no
geometrically born site and at most one geometrically dead site. The
common-range summand is not the same at the two heights: it is the exact
coboundary

\[
 B_h(n)-(-1)^{\eta_\omega(h)}
 B_{h-1}\bigl(n-\epsilon_\omega\eta_\omega(h)\bigr),
\tag{1.3}
\]

with the outer height masks inserted as in (3.12) below. The factor
\((-1)^{\eta_\omega(h)}\) is forced by the reindexing. No second anchor
factor is present.

**Exact operator capacity.** On any finite coordinate set
\(E=\{(\omega,v,h)\}\), the normalized Abel operator in (1.1) has exact
capacity

\[
 \sup_{|W_\alpha(h)|\le M_\alpha(h)}
 \left|\sum_{(\alpha,h)\in E}W_\alpha(h)z_\alpha^h\right|
 =\sum_{(\alpha,h)\in E}M_\alpha(h).
\tag{1.4}
\]

Thus the factor \(|1-z|^{-1}\asymp q/J\) yields no saving by itself; it
is canceled exactly by Abel summation. From the stated pointwise
coefficient information one gets only

\[
 |W_{v,\omega}(h)|\ll_\varepsilon \kappa X^\varepsilon,
 \qquad
 |\mathscr J|\ll_\varepsilon
 Y\kappa X^\varepsilon\,#\{(v,\omega)\text{ in the band}\},
\tag{1.5}
\]

up to harmless endpoint rounding. If one additionally inserts the
band-count scale quoted in the packet, (1.5) is precisely the available
\(Y\kappa uJ/q\) scale, not the desired fast-band scale.

**Scoped no-go.** The hypotheses displayed in the statement do not
prove (B191.13). They contain no cross-height relation for the two
endpoint coefficients, no persistence rule for the undeclared literal
masks, and no height-support mass estimate that replaces \(Y\) by
\(Qm\). In fact, (1.4) supplies an exact bounded-array obstruction, and
the separated-edge construction in Section 5 gives an adversarial
coefficient model satisfying all explicitly stated coefficient
conditions for which \(|\mathscr J|\asymp Y\) while
\(Qm\kappa uX^\varepsilon\) is fixed at scale \(QqX^\varepsilon\).
This refutes (B191.13) as a universal theorem of the **stated
coefficient class**.

That adversarial model is not a lower bound for the fixed literal
coefficient in the intended application. Its undeclared selectors may
exclude the constructed rows or impose additional algebra. Therefore
the strongest conclusion about the fixed literal packet is
insufficiency: an additional literal support or common-range
coboundary property must be supplied and proved.

## 2. Exact statement and hypotheses

The conclusions above use only (B191.1)--(B191.12), including complete
zero-extension, the standard canonical residue convention implicit in
\([\cdot]_U\), and the following consequences already present in the
packet:

1. Since \((u,v)=1\) and \(U\mid u\), both inverses \(\bar v_U\) and
   \(\bar v_q\) exist.
2. Since \(U>4Q\), one has \(U>1\). Thus
   \(1\le c=[\bar v_U]_U\le U-1\), and
   \[
      vc=1+U\ell,\qquad 0\le\ell<v.
   \tag{2.1}
   \]
3. For a literal height, \(0<r=2\kappa gh<\lceil L\rceil\), so the
   Fejer factor lies strictly between zero and one.
4. Each amplitude is zero-extended through its two endpoint
   coefficients and has modulus \(\ll_\varepsilon X^\varepsilon\)
   after replacing \(\varepsilon\) by \(\varepsilon/2\) in the two
   applications of (B191.5).
5. At most \(O(\kappa)\) affine sites are live for each fixed
   \((h,v,\omega)\).
6. The band phase is nontrivial. Indeed, \(a\bar v_q\) is a nonzero
   residue modulo \(q\), so \(z_{\omega,v}\ne1\).

For the exact range formula define the outer height mask

\[
 \chi(h)=\mathbf1_{Y<h\le2Y}\mathbf1_{(U,h)=1}
          \mathbf1_{0<2\kappa gh<\lceil L\rceil}.
\tag{2.2}
\]

All other masks remain inside the zero-extended \(B_h(n)\). The range
comparison itself is geometric and does not assume that those inner
masks are periodic, smooth, or persistent.

The no-go has two deliberately separated meanings.

- Formula (1.4) is an unconditional theorem for the bounded height-array
  relaxation implied by the available pointwise information.
- The construction in Section 5 is a countermodel to a universal claim
  for all endpoint arrays satisfying the explicit support and size
  axioms. It is not asserted to coincide with, approximate, or lower
  bound the one fixed literal endpoint array whose undisclosed
  predicates come from the intended application.

No orientation involution, projective-neighbor identity, or mask
regularity is assumed anywhere.

## 3. Proof or derivation

### 3.1 Endpoint-exact Abel identity

Let \(W\) be any finitely supported sequence and \(A\le B\) integers.
Direct index shifting gives

\[
\begin{aligned}
 \sum_{h=A}^{B}(W(h)-W(h-1))z^h
 &=\sum_{h=A}^{B}W(h)z^h
   -z\sum_{k=A-1}^{B-1}W(k)z^k\\
 &=(1-z)\sum_{h=A}^{B-1}W(h)z^h
   +W(B)z^B-W(A-1)z^A.
\end{aligned}
\tag{3.1}
\]

Choose \(A\) at or below the first live height and \(B\) one past the
last live height. Then \(W(A-1)=W(B)=0\), and (3.1) proves

\[
 \sum_h\Delta^-W(h)z^h=(1-z)\sum_hW(h)z^h.
\tag{3.2}
\]

Division by \(1-z\ne0\) proves (1.1) and (1.2). Notice that the second
term in \(\Delta^-W=W(h)-W(h-1)\) produces \(-z\sum W(h)z^h\), hence
the multiplier is \(1-z\), not \(z-1\). This fixes the sign.

### 3.2 Anchor jump and forced parity

For clarity write \(S_{0,\omega}(h)\) and
\(w_{0,\omega}(h)\). Define \(\eta_+(h),\eta_-(h)\in\{0,1\}\) by

\[
\begin{aligned}
 S_{0,+}(h-1)&=S_{0,+}(h)-c+U\eta_+(h),\\
 S_{0,-}(h-1)&=S_{0,-}(h)+c-U\eta_-(h).
\end{aligned}
\tag{3.3}
\]

These are just the two possible wrap choices for canonical residues.
Using \(vc=1+U\ell\) in the definitions of \(w_0\) gives, exactly,

\[
\begin{aligned}
 w_{0,+}(h-1)&=w_{0,+}(h)-\ell+v\eta_+(h),\\
 w_{0,-}(h-1)&=w_{0,-}(h)+\ell-v\eta_-(h).
\end{aligned}
\tag{3.4}
\]

With \(\epsilon_+=1\), \(\epsilon_-=-1\), both equations become

\[
\begin{aligned}
 S_{0,\omega}(h-1)
 &=S_{0,\omega}(h)-\epsilon_\omega c
   +\epsilon_\omega U\eta_\omega(h),\\
 w_{0,\omega}(h-1)
 &=w_{0,\omega}(h)-\epsilon_\omega\ell
   +\epsilon_\omega v\eta_\omega(h).
\end{aligned}
\tag{3.5}
\]

Reindex an old site \(t'\) by

\[
 n=t'+\epsilon_\omega\eta_\omega(h),
 \qquad t'=n-\epsilon_\omega\eta_\omega(h).
\tag{3.6}
\]

Then its old affine coordinates, expressed in the new coordinate \(n\),
are

\[
 S_{t',\omega}(h-1)=S_{n,\omega}(h)-\epsilon_\omega c,
 \qquad
 w_{t',\omega}(h-1)=w_{n,\omega}(h)-\epsilon_\omega\ell.
\tag{3.7}
\]

The alternating sign consequently changes by

\[
 (-1)^{t'}=(-1)^n(-1)^{\eta_\omega(h)}.
\tag{3.8}
\]

The sign in (3.8) is independent of the sign of \(\epsilon_\omega\),
because \((-1)^{-1}=(-1)\). Equation (3.8), and only (3.8), accounts
for the anchor-reindexing parity inside \(W\). In particular, inserting
an additional \((-1)^{S_{0,\omega}}\) would double count the anchor
factor expressly removed in the packet.

### 3.3 Exact common range and geometric births/deaths

For real \(A,B\) define the first integer in the corresponding positive
affine ray by

\[
 \tau(A,B)=
 \max\left\{\left\lfloor-\frac A U\right\rfloor+1,
             \left\lfloor-\frac B v\right\rfloor+1\right\}.
\tag{3.9}
\]

At height \(h\), put

\[
 \alpha_h=\tau(S_{0,\omega}(h),w_{0,\omega}(h)),
 \quad
 \beta_h=\tau(S_{0,\omega}(h)-\epsilon_\omega c,
              w_{0,\omega}(h)-\epsilon_\omega\ell).
\tag{3.10}
\]

Thus the current and reindexed previous ranges are exactly

\[
 I_h=[\alpha_h,\infty)\cap\mathbb Z,
 \qquad
 I^-_h:=\{n:n-\epsilon_\omega\eta_\omega(h)\in I_{h-1}\}
       =[\beta_h,\infty)\cap\mathbb Z.
\tag{3.11}
\]

For \(\omega=+\), the shifted previous inequalities are the stronger
inequalities \(S_n>c\) and \(w_n>\ell\). Hence
\(I^-_h\subseteq I_h\). Moreover \(U-c>0\) and \(v-\ell>0\), so one
additional step from the first current site satisfies both stronger
inequalities. Therefore

\[
 \omega=+:\qquad \beta_h\in\{\alpha_h,\alpha_h+1\}.
\tag{3.12a}
\]

For \(\omega=-\), the shifted previous inequalities are the weaker
inequalities \(S_n>-c\) and \(w_n>-\ell\). Thus
\(I_h\subseteq I^-_h\), and the same one-step argument gives

\[
 \omega=-:\qquad \alpha_h\in\{\beta_h,\beta_h+1\}.
\tag{3.12b}
\]

Let

\[
 \mathcal R_h=I_h\cap I^-_h,
 \qquad \mathcal P_h=I_h\setminus I^-_h,
 \qquad \mathcal D_h=I^-_h\setminus I_h.
\tag{3.13}
\]

Then \(\mathcal P_h\) is empty or the singleton \(\{\alpha_h\}\) in
the plus orientation and is empty in the minus orientation;
\(\mathcal D_h\) is empty in the plus orientation and is empty or the
singleton \(\{\beta_h\}\) in the minus orientation. These are the exact
geometric birth and death sets. The common range is the remaining upper
ray.

Writing \(B_h(n)=B_{h,v,\omega}^{\sigma}(n)\) and
\(\theta_h=(-1)^{\eta_\omega(h)}\), the complete difference is

\[
\boxed{\begin{aligned}
 \Delta^-W_{v,\omega}(h)
 ={}&\sum_{n\in\mathcal R_h}(-1)^n
 \left[\chi(h)B_h(n)
 -\theta_h\chi(h-1)
 B_{h-1}\bigl(n-\epsilon_\omega\eta_\omega(h)\bigr)\right]\\
 &+\chi(h)\sum_{n\in\mathcal P_h}(-1)^nB_h(n)\\
 &-\theta_h\chi(h-1)\sum_{n\in\mathcal D_h}(-1)^n
 B_{h-1}\bigl(n-\epsilon_\omega\eta_\omega(h)\bigr).
\end{aligned}}
\tag{3.14}
\]

All sums in (3.14) are finite after the literal zero-extension. Summing
the three displayed lines against
\(z_{\omega,v}^h/(1-z_{\omega,v})\) gives an exact decomposition

\[
 \mathscr J=\mathscr J_{\rm common}
             +\mathscr J_{\rm birth}
             +\mathscr J_{\rm death}.
\tag{3.15}
\]

This is an exact complement, not an estimate. If \(\chi(h)\ne\chi(h-1)\),
the common geometric ray still contains the whole surviving live sum on
one side; similarly, an inner selector can turn on or off at any common
site because it is hidden inside \(B\). Therefore the singleton result
for geometric range endpoints does not imply singleton variation for
the effective literal support.

### 3.4 The endpoints genuinely move on the common range

Let \(N_h^\omega(n)\) denote the lower endpoint in (B191.6), and use
the reindexing (3.6). Equations (3.7) give the exact endpoint shifts

\[
\begin{array}{c|cc}
 &N_{h-1}^\omega(t')&(N_{h-1}^\omega(t')+r_{h-1})\\ \hline
 \omega=+
 &N_h^+(n)-2\kappa gU\ell
 &(N_h^+(n)+r_h)-2\kappa gv c\\[2mm]
 \omega=-
 &N_h^-(n)+2\kappa gv c
 &(N_h^-(n)+r_h)+2\kappa gU\ell .
\end{array}
\tag{3.16}
\]

Here \(r_{h-1}=r_h-2\kappa g\), and consistency follows from
\(vc=1+U\ell\). The moving nonconstant divisor also changes from
\(\kappa gU+2gS_n\) to
\(\kappa gU+2g(S_n-c)\) in the plus orientation, and to
\(\kappa gU+2g(S_n+c)\) in the reindexed previous minus orientation.

Consequently the two products of endpoint coefficients in the common
bracket of (3.14) are values at different \((N,d)\)-keys. The packet
only bounds their individual magnitudes. The small deterministic change
of the Fejer factor, and any estimable change of the square-root phase,
cannot control an arbitrary change of these two coefficient values or
of their literal masks.

### 3.5 Pointwise consequence and exact capacity

By (B191.5), the modulus-one exponential, the Fejer factor, and the
\(O(\kappa)\) live-site hypothesis,

\[
 |W_{v,\omega}(h)|\ll_\varepsilon\kappa X^\varepsilon.
\tag{3.17}
\]

There are exactly \(\lfloor2Y\rfloor-\lfloor Y\rfloor\) integer heights
in the bare block, before the other outer masks. Equations (1.2) and
(3.17) therefore prove (1.5).

For the exact capacity claim, the triangle inequality gives the upper
bound in (1.4). Equality is obtained simultaneously in all coordinates
by taking

\[
 W_\alpha(h)=M_\alpha(h)\,\overline{z_\alpha^{\,h}}
\tag{3.18}
\]

(or by multiplying every value in (3.18) by one common unit complex
number). Thus the normalized Abel functional has weighted
\(\ell^\infty\)-to-scalar norm exactly the sum of the coordinate
budgets. Neither \(j_q(a,v)>T_Q\) nor
\(|1-z|^{-1}\asymp q/J\) changes this norm. Any saving from \(Y\) to
\(Qm\) must come from a property that removes or correlates coordinates,
not from Abel's identity.

## 4. First doubtful or unproved step

The exact identities (1.1), (3.14), and (3.16) have no unproved step.
The first unavailable step in a proof of (B191.13) is a bound for the
common bracket

\[
 \chi(h)B_h(n)-(-1)^{\eta_\omega(h)}\chi(h-1)
 B_{h-1}\bigl(n-\epsilon_\omega\eta_\omega(h)\bigr)
\tag{4.1}
\]

at the total fast-band scale. On interior heights with both outer masks
equal to one, this would require a cross-height transfer law for the
endpoint coefficient products at the shifted keys in (3.16). At a
block, coprimality, or inner-selector transition, it would instead
require a quantitative birth/death mass estimate. Neither property is
stated.

In particular, (B191.5) cannot justify replacing (4.1) by a small
difference. It permits the two values to have unrelated phases, and
when \(\eta_\omega(h)=1\), the forced sign makes (4.1) a sum rather than
a difference even for equal raw amplitudes. Moving an absolute value
inside the packet would only recover the full capacity (1.4) and the
forbidden \(Y/(Qm)\) loss.

A sufficient new input would have to be one of the following, stated
for the actual literal coefficient rather than an adversarial
relaxation:

- a signed common-range coboundary estimate for (4.1), together with
  estimates for all outer- and inner-mask births/deaths;
- a support/mass theorem showing that the total live height mass in the
  fast band has \(Qm\), rather than \(Y\), scale; or
- a direct signed Fourier estimate for the exact right side of (1.2).

The packet supplies none of these. This is the first missing property,
before any downstream incidence or bridge issue.

## 5. Required control test and outcome

### 5.1 Endpoint and sign control

Take \(W(h_0)=1\) and \(W(h)=0\) otherwise. Then

\[
 \Delta^-W(h_0)=1,\qquad \Delta^-W(h_0+1)=-1,
\]

and hence

\[
 \sum_h\Delta^-W(h)z^h=z^{h_0}-z^{h_0+1}
 =(1-z)z^{h_0}.
\tag{5.1}
\]

After division by \(1-z\), the result is \(+z^{h_0}\). This control
passes and fixes both the endpoint convention and the sign.

### 5.2 Full-capacity bounded-array control

On any finite allowed height set \(H\), take
\(W(h)=\overline{z^h}\mathbf1_H(h)\). The complete derivative includes
every birth and death caused by the holes and endpoints of \(H\), while
(1.1) gives exactly

\[
 \frac1{1-z}\sum_h\Delta^-W(h)z^h=|H|.
\tag{5.2}
\]

Thus rapid phase alone supplies zero cancellation for the stated
bounded-array relaxation. The outcome is a sharp failure of any
operator estimate replacing \(|H|\asymp Y\) by \(Qm\).

### 5.3 Adversarial coefficient-class countermodel

This control is included only to test a universal theorem for the
coefficient class described in the packet. It is **not** a claim about
the fixed literal endpoint coefficient.

Fix an \(X\) for which \(Q\ge2\). Choose an odd prime \(q>4Q+4\) and a
unit \(a\) with \(Q<a<q/2\). Set

\[
 m=\kappa=g=1,\qquad U=u=q.
\tag{5.3}
\]

Choose an arbitrarily large odd squarefree integer
\(v\equiv a\pmod q\), put \(L=v\), and take
\(Y=\lfloor v/16\rfloor\), with \(v\) so large that \(Y>Qq\). Such
squarefree values in a reduced progression follow directly from
Möbius inversion: the count of squarefree integers in
\(a\bmod q\) up to \(V\) is a positive constant times \(V/q\), plus
an \(O(\sqrt V)\) error. Here

\[
 j_q(a,v)=1,\qquad T_Q=0,\qquad J=1,
\tag{5.4}
\]

and all displayed outer hypotheses hold. In particular
\(2h<L\) throughout \(Y<h\le2Y\).

For every integer \(h\) in that block with \(q\nmid h\), use the plus
orientation and choose a sufficiently large, mutually separated
positive site \(t_h\). With

\[
 A_h(t)=v+2w_{t,+},\qquad C_h(t)=q+2S_{t,+},
\tag{5.5}
\]

choose \(t_h\) so that \(A_h(t_h)\) and \(C_h(t_h)\) are squarefree,
\(q\nmid A_h(t_h)\), and \((v,C_h(t_h))=1\). There are infinitely many
such \(t\). A self-contained squarefree-sieve justification is as
follows: the two expressions in (5.5) are odd linear polynomials with
slopes \(2v\) and \(2q\); because \(q\) and \(v\) are squarefree and
coprime, neither has a fixed square divisor. Modulo each \(p^2\), the
union of their square-divisibility classes is a proper subset; the
additional finite exclusions \(q\nmid A_h\) and
\(p\nmid C_h\) for \(p\mid v\) also leave a residue class. Truncated
inclusion-exclusion gives a positive product
\(\prod_p(1-\rho(p^2)/p^2)>0\), while the tail is bounded by
\(\sum_{p>P}O(p^{-2})\). Hence admissible \(t\)'s have positive density.
They can recursively be chosen so that the endpoint intervals below
are separated by more than \(4Y\).

Put

\[
 N_h=qA_h(t_h),\qquad M_h=vC_h(t_h)=N_h+2h.
\tag{5.6}
\]

Both numbers are positive and squarefree; \(q\mid N_h\) and
\(C_h(t_h)\mid M_h\), with both divisors odd. For a fixed \(\sigma\),
define an endpoint array only on the incidence-isolated selected keys by

\[
 \lambda_{N_h,\sigma}(q)=1,
\]

\[
 \lambda_{M_h,\sigma}(C_h(t_h))
 =(-1)^{t_h}z^{-h}
 e\!\left(-\frac{\sigma\sqrt X\,2h}{\sqrt{M_h}+\sqrt{N_h}}\right),
 \qquad z=e(1/q),
\tag{5.7}
\]

and set all other endpoint values to zero. Interpret the undeclared
literal predicates as true on these selected keys. The separation by
more than \(4Y\), together with \(0<2h\le4Y\), prevents two selected
keys from forming any unintended endpoint edge; the divisor keys also
force the selected plus row uniquely. Hence exactly one affine site is
live at each selected height and no minus or cross-row term is created.
All nonzero coefficients have modulus one and satisfy (B191.5).

The selected plus amplitude is

\[
 B_{h,v,+}^{\sigma}(t_h)
 =\left(1-\frac{2h}{\lceil L\rceil}\right)
   (-1)^{t_h}z^{-h},
\]

so

\[
 W_{v,+}(h)z^h=1-\frac{2h}{\lceil L\rceil}\ge\frac34.
\tag{5.8}
\]

There are \(Y(1-1/q)+O(1)\) selected heights. Therefore the complete
packet, without separately absolutizing orientations, satisfies

\[
 |\mathscr J|\gg Y.
\tag{5.9}
\]

For the parameters (5.3), the proposed right side is
\(QqX^\varepsilon\). Since \(X,q,Q\) are fixed while the squarefree
\(v\), hence \(Y\), can be arbitrarily large, (5.9) contradicts a
uniform version of (B191.13) for the endpoint arrays allowed by the
explicit axioms.

The outcome of this control is therefore:

- **fail** for (B191.13) as a theorem of only the displayed coefficient
  class;
- **no conclusion** about the value of the fixed literal packet, because
  its undisclosed original selectors may disallow these keys, may impose
  an \(X\)-dependent shell not stated here, or may correlate their
  phases. The construction must not be cited as a lower bound for that
  fixed packet.

## 6. Dependencies and exact artifacts used

Only the following two artifacts were read or used:

1. `protocol.md` -- workflow, proof-state, isolation, and report rules.
2. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/blind_statement.md`
   -- the complete mathematical statement (B191.1)--(B191.13).

No proof-state file, active-campaign file, failure ledger, strategy,
source card, previous report, kernel, sibling artifact, or conductor
analysis was read. No web source and no numerical computation was used.
The controls are exact algebraic constructions.

## 7. Recommended state effect

**Revise.** Retain the endpoint-exact Abel identity, its positive sign,
the anchor reindexing with the forced factor
\((-1)^{\eta_\omega(h)}\), the singleton geometric birth/death lemma,
and the exact decomposition (3.14) as candidate finite facts for seam
review. Do not promote (B191.13) from this packet. Record the present
route as insufficient until the fixed literal coefficient is shown to
satisfy a cross-height common-range transfer estimate and a complete
outer/inner birth-death mass estimate, or an equivalent direct signed
Fourier bound. No claim about any \(t\ge2\) incidence, parent, bridge,
quarter theorem, or global exponent follows from this report.

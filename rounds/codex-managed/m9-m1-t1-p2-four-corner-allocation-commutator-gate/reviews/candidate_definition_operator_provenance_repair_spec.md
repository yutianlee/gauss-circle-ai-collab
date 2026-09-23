# Candidate definition, operator, and provenance repair specification

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Purpose: exact replacement text for the definition/operator/provenance
  defects identified in
  `reviews/candidate_provenance_owner_graph_scope_review.md`
- Status: repair specification only; no candidate or proof-state mutation

The following four blocks are intended to replace the corresponding prose in
the formal candidate.  They do not enlarge the candidate theorem.

## 1. Replacement text: finite sharp literal code

> For fixed $N,L,X,\sigma$ and a lower allocation $N=uv$, let
> $I_{\rm ar}(u,v)$ be the conjunction of the accepted arithmetic
> zero-extension predicates
>
> \[
> u>0,\quad v>0,\quad uv=N,\quad 2\nmid v,\quad
> \mu^2(N)=1,\quad (u,v)=1.
> \]
>
> Let the following symbols denote the exact truth or branch labels already
> present in the accepted literal M1 transform:
>
> \[
> \begin{aligned}
> &\ell_{\rm shell},\ \ell_{\rm height},\ \ell_{\rm cone},
> \ \ell_{\rm profile},\ \ell_{\rm floor},\ \ell_{\rm star},
> \ \ell_{1/2},\ \ell_{\rm hard},\\
> &\ell_{\rm cell},\ \ell_{\rm crossing},\
> \ \ell_{\rm endpoint},\ \ell_{\rm sign}.
> \end{aligned}
> \]
>
> Here `profile` means only the accepted profile support/plateau/branch
> label, not the numerical value of the normalized BV profile; `floor`,
> `star`, `1/2`, `hard`, `cell`, `crossing`, and `endpoint` mean the accepted
> discrete branch or trace labels, not a coefficient value.  Let
> $I_{\rm lit}(u,v)$ be the conjunction that every named shell, height,
> strict $4u<v<16u$ cone, profile-support, hard-sample, endpoint-support,
> and zero-extension predicate is live.
>
> Define the finite code
>
> \[
> \mathfrak c_{N,\sigma}(u,v)=
> \begin{cases}
> \dagger,&I_{\rm ar}(u,v)I_{\rm lit}(u,v)=0,\\[1mm]
> (\ell_{\rm shell},\ell_{\rm height},\ell_{\rm cone},
>  \ell_{\rm profile},\ell_{\rm floor},\ell_{\rm star},
>  \ell_{1/2},\ell_{\rm hard},\ell_{\rm cell},
>  \ell_{\rm crossing},\ell_{\rm endpoint},\ell_{\rm sign}),
>  &I_{\rm ar}(u,v)I_{\rm lit}(u,v)=1.
> \end{cases}
> \tag{197.D1}
> \]
>
> The distinguished value $\dagger$ is determined only by the named
> arithmetic/support predicates.  In particular, the code contains none of
>
> \[
> a_{L,X}^{\rm lit,\sigma}(u,v),\quad
> \lambda_{N,\sigma}(v),\quad \rho_N(v),\quad
> \eta_L(u),
> \]
>
> and contains no value of a smooth factor.  Accidental vanishing of any of
> those quantities does not change $\mathfrak c$.
>
> Put
>
> \[
> C_{\rm lit}=
> \mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
>                  =\mathfrak c_{N,\sigma}(\alpha,gm)\}},
> \qquad
> P_{\rm cc}=P_2\mathbf1_{(m,\beta)=1}
> \mathbf1_{\chi_4(\alpha m)=-1}C_{\rm lit}.
> \tag{197.D2}
> \]
>
> Equality in (197.D2) is symmetric under
> $(m,g\alpha)\leftrightarrow(\alpha,gm)$, so $P_{\rm cc}$ is an
> orbit-invariant physical mask.  If the common code is $\dagger$, both
> lower literal symbols are zero by the named zero-extension convention.  If
> it is live, every sharp multiplier and branch formula is the same at the
> two inputs.  The normalized BV profile, the Round-184 selector, and the
> smooth factors are not hidden in this assertion and are estimated
> separately.  No nonemptiness, density, coefficient nonvanishing, or lower
> mass is asserted.

For formalization, each $\ell$ above should be implemented by the existing
literal-transform branch datatype, not by testing equality of evaluated
coefficients.  The list is closed: no “and every remaining field” clause is
permitted.

## 2. Replacement text: Round-184 selector parameter

> Fix once and for all a selector-width constant $K_{\rm sel}>0$, distinct
> from every physical gcd.  For each squarefree (N), let
> $(p_N,q_N)$, with $p_N<q_N$, be the lexicographically first pair of
> distinct odd prime divisors of (N) satisfying
>
> \[
> \chi_4(p_Nq_N)=-1,\qquad
> \left|\log{q_N\over p_N}\right|
> \le K_{\rm sel}L^{-1/2},
> \tag{197.D3}
> \]
>
> and select no pair if the eligible set is empty.  This rule depends only on
> $(N,L,K_{\rm sel})$, never on an allocation $N=uv$.  Define
>
> \[
> \rho_N(v)=
> \begin{cases}
> 1,&\text{no pair is selected},\\
> 1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
>   +2\mathbf1_{p_Nq_N\mid v},&\text{a pair is selected}.
> \end{cases}
> \tag{197.D4}
> \]
>
> Thus the selected-prime truth table is ((1,0,0,1)).  The symbol
> $\kappa$ below is reserved for the physical inward cross gcd and is
> unrelated to $K_{\rm sel}$.  All estimates that use the selector are
> uniform for fixed $K_{\rm sel}$, with implicit constants allowed to
> depend on it.

This is a lawful concrete instance of the canonical Round-184 rule.  If the
repository has already frozen a different allocation-independent tie-break,
retain that tie-break verbatim and keep (197.D3)--(197.D4) otherwise
unchanged.

## 3. Replacement text: physical atom, packet variables, and outer operators

> Fix
>
> \[
> Q=H_B=\lfloor(\log(2X))^B\rfloor,
> \qquad R_0=\lceil L\rceil,
> \qquad D_L=\lceil\sqrt L\rceil,
> \qquad C_0\ge2,
> \tag{197.D5}
> \]
>
> with $C_0$ independent of all asymptotic variables.  A zero-extended
> physical atom is $x=(d,m,d',m',r)$ with
>
> \[
> N=dm,\qquad N+r=d'm',\qquad d,d'\ \text{odd},
> \qquad0<r<R_0,\qquad2\mid r,
> \tag{197.D6}
> \]
>
> and exact weight
>
> \[
> W_x^\sigma=
> \chi_4(d')\chi_4(d)
> \left(1-{r\over R_0}\right)
> e\!\left({\sigma\sqrt X\,r\over\sqrt{N+r}+\sqrt N}\right)
> \lambda_{N+r,\sigma}(d')
> \overline{\lambda_{N,\sigma}(d)}.
> \tag{197.D7}
> \]
>
> It is zero when any literal endpoint predicate fails.  Put
> $g=(d,d')$, $d=g\alpha$, $d'=g\beta$, and impose $P_2$ and
> $P_{\rm cc}$ on $x$ before every Fourier, height, anchor, or Farey
> operation.
>
> On an opposing plus atom $d'-d>0>m'-m$, the physical inward cross gcd is
>
> \[
> \kappa=(d,m'),\qquad
> d=\kappa gU,\quad d'=g(\kappa U+2S),
> \quad m'=\kappa v,\quad m=\kappa v+2w.
> \tag{197.D8+}
> \]
>
> On an opposing minus atom $d'-d<0<m'-m$, it is
>
> \[
> \kappa=(d',m),\qquad
> d'=\kappa gU,\quad d=g(\kappa U+2S),
> \quad m=\kappa v,\quad m'=\kappa v+2w.
> \tag{197.D8-}
> \]
>
> In both charts $S,w>0$, and $Y<h\le2Y$ denotes one dyadic high-height
> block.  The spectral lift gcd is $\mathfrak m$, distinct from the
> physical cofactor $m$ and from $K_{\rm sel}$.  A fixed accepted packet
> is
>
> \[
> p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma)
> \tag{197.D9}
> \]
>
> with the Round-192/195 conditions
>
> \[
> U=\mathfrak m q>4Q,\qquad q>Q,\qquad
> \mathfrak m|a|_q>Q,\qquad Q\mathfrak m<Y,
> \qquad U\mid u.
> \tag{197.D10}
> \]
>
> Here (u) is the accepted projective row parameter and (J) its accepted
> projective band label.  For the Farey projector retain
>
> \[
> \rho v_0-\beta U=1,\qquad
> -{U-1\over2}\le\rho\le{U-1\over2},
> \qquad
> T=\min\left\{{U-1\over2},
> \left\lfloor{Q\mathfrak m U\over Y}\right\rfloor\right\},
> \tag{197.D11}
> \]
>
> where $v_0=[v]_U\in\{1,\ldots,U-1\}$, and
>
> \[
> A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
> \mathcal F_A=\{(c,d_0):1\le c\le A,\ 0\le d_0\le c,
> (c,d_0)=1\}.
> \tag{197.D12}
> \]
>
> At $T=0$ the Farey union projector is zero and the complete inherited
> Round-191 rho-large remainder is retained.  At $T\ge1$, every core row
> retains simultaneously
>
> \[
> |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
> \qquad |\rho|\ge(A+1)(T+1).
> \tag{197.D13}
> \]
>
> Let $\mathscr R_{{\rm core},{\rm fix}}^\sigma(p;MW)$ be the exact
> accepted Round-192 fixed-packet core linear functional evaluated on the
> physically masked source $MW$.  Let $\mathcal A_{\rm out}^\sigma$ be
> the exact accepted Round-195 linear fixed-to-outer assembly: it includes
> the $\mathfrak m^{-1}$ lift weight, accepted anchor, band, divisor and
> shell weights, the dyadic (Y)-partition, both physical orientations,
> zero extensions, and the single outer real part.  It takes no modulus at a
> fixed (Y), orientation, anchor, or frequency mode.
>
> Define the disjoint packet sets
>
> \[
> \begin{aligned}
> \mathcal P_{\rm cap}^{195}
> &=\{p:\kappa\ge D_L\}
> \ \dot\cup\
> \{p:\kappa<D_L,\ \min(Y,D_L)\le Q\mathfrak m\kappa\},\\
> \mathcal P_{\rm open}^{195}
> &=\{p:\kappa<D_L,\ \min(Y,D_L)>Q\mathfrak m\kappa\}.
> \end{aligned}
> \tag{197.D14}
> \]
>
> For every physical mask $M\le P_2$, set
>
> \[
> \begin{aligned}
> \mathscr R_{\rm core,out}^\sigma(MW)
> &:=\mathcal A_{\rm out}^\sigma
>   \bigl((\mathscr R_{{\rm core},{\rm fix}}^\sigma(p;MW))_p\bigr),\\
> \mathscr R_{\rm cap,out}^\sigma(MW)
> &:=\mathcal A_{\rm out}^\sigma
>   \bigl((\mathbf1_{p\in\mathcal P_{\rm cap}^{195}}
>   \mathscr R_{{\rm core},{\rm fix}}^\sigma(p;MW))_p\bigr),\\
> \mathscr R_{\rm open,out}^\sigma(MW)
> &:=\mathcal A_{\rm out}^\sigma
>   \bigl((\mathbf1_{p\in\mathcal P_{\rm open}^{195}}
>   \mathscr R_{{\rm core},{\rm fix}}^\sigma(p;MW))_p\bigr).
> \end{aligned}
> \tag{197.D15}
> \]
>
> Linearity and (197.D14) give exactly
>
> \[
> \mathscr R_{\rm core,out}^\sigma(MW)
> =\mathscr R_{\rm cap,out}^\sigma(MW)
>  +\mathscr R_{\rm open,out}^\sigma(MW).
> \tag{197.D16}
> \]
>
> The superscript $\sigma$ always denotes one fixed frequency-sign
> component.  The estimate is proved uniformly for each
> $\sigma\in\{+1,-1\}$; the accepted finite recombination of the two
> components gives the complete two-sign contribution.  Do not describe
> both signs as already contained in one fixed-$\sigma$ operator.

The definitions in (197.D15) make clear that the packet condition is not
inserted into the physical allocation orbit.  It is applied only through the
accepted linear packet projector after the physical $P_{\rm cc}$ estimate.

## 4. Replacement text: typed dependency ledger and cycle-safe state effect

> The direct accepted interfaces are typed as follows.
>
> 1. **Literal coefficient and selector calculus.**
>    `M9-M1-hard-top-t1-comparable-factor-exchange-sector`, with proof kernel
>    `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`,
>    supplies (K184.4) and the exact literal symbol ledger
>    (K184.11)--(K184.16).  Only the scale-normalized $C^1$ factor receives
>    a pointwise $D_L/L$ estimate; the normalized BV profile is treated by
>    total variation.
> 2. **Physical even-shift source and safe source exits.**
>    `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`, with proof
>    kernel
>    `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
>    supplies (K185.1)--(K185.7), the multiplicity-one opening, both
>    primitive charts, and the absolute monotone/low-height exit estimate.
> 3. **Coordinatewise physical masking.**
>    `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`, with proof kernel
>    `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
>    supplies the physical-mask convention and exact transported-mask
>    product rule (193.C19b)--(193.C21).  Its double-close collar (193.C31)
>    is not used as a one-close $P_2$ face theorem.
> 4. **$P_2$ count, packet split, and outer assembly.**
>    `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`, with proof
>    kernel
>    `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`,
>    supplies (195.C14)--(195.C20b), including the deletion-stable masked
>    operator, exact safe/open packet split, and fixed-to-outer ledger.
>
> The three Round-197 reports and
> `reviews/conductor_round197_report_reconciliation.md` are claimant evidence,
> not accepted dependencies.  No computation is theorem evidence.
>
> A future Round-197 subordinate node may depend on the four accepted nodes
> above, and the still-open
> `M9-M1-hard-top-high-radical-small-t-residual-estimate` may add the new node
> as a dependency/evidence item.  The accepted Round-195 node must remain
> unchanged.  In particular, it must not acquire the new Round-197 node as a
> dependency and its historical statement must not be rewritten to contain
> the later refinement.  Otherwise the new node's use of Round 195 and the
> reverse Round-195-to-Round-197 edge would form a two-cycle.  Record the
> refined remaining packet set only in the new node and in the open owner's
> `next_action`.

This ledger permits redundant direct edges because the new proof explicitly
reopens all four interfaces.  If the State Patch convention suppresses
transitive edges, retain the omitted interfaces as exact theorem provenance
and keep the cycle-safe direction unchanged.

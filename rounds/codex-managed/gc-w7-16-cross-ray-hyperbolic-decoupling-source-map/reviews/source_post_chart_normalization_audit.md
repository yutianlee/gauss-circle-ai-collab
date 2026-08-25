# Post-source seam review: exact hyperbolic chart versus licensed rescaling

- Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`
- Round: `132`
- Role: hostile post-source seam reviewer
- Status: candidate review only; no shared-state edit

## 1. Result

**Mixed verdict.** The sign algebra, exact hyperbolic chart, determinant-to-$\eta$ identity, and all displayed exponent arithmetic in (132.C1)--(132.C8) and (132.C11) are correct. In particular,

\[
\eta_{r'}-\eta_r={Dn\over Lbb'}>0
\]

for the one-sided determinant $n=ab'-a'b>0$, and the widest possible $\eta$-gap is $Y^{-5/48}$.

The first nonexact transition is the use of (132.C9) as a theorem-ready normalization. The diagonal dilation

\[
(\widetilde\xi,\widetilde\eta,widetilde\xi\widetilde\eta)
\mapsto
(\widetilde\xi,h\widetilde\eta,h\widetilde\xi\widetilde\eta)
\]

is an exact automorphism of $\mathbb H$, but the actual top-shell $\eta$ coordinates have size $\asymp1$, not $O(h)$. Without an $\eta$-recentering shear and an $h$-scale strip localization, the rescaled patches sit at $|\widetilde\eta|\asymp h^{-1}$, outside the normalized source window. Even after repair, the dilation leaves $\xi$-separation unchanged, so same-denominator pairs remain nontransverse.

Likewise, (132.C10) is exact only as the magnitude of the **dual evaluation coordinate** after dilation: $|\widetilde x_2|=t_i h$. It is not yet the Demeter--Wu decoupling parameter $R$, which is tied to Fourier thickness $R^{-1}$, $R^{-1/2}$ caps, and a spatial localization. Thus (132.C11) is a correct exponent identity

\[
t_i\delta_*={Y\over W}=Y^{27/48},
\]

but not a source-licensed decoupling scale or an estimate.

## 2. Exact statement and hypotheses retained

For $b,b'>0$, $|a|,|a'|\asymp L$, $b,b'\asymp D$, and

\[
n=ab'-a'b>0,
\]

define

\[
\xi={b\over D},\qquad
\eta=-{Da\over Lb},\qquad
\zeta=-{a\over L}.
\]

Then $\zeta=\xi\eta$ exactly. This is the linear coordinate change

\[
(x,y,z)=(a/L,b/D,-x/y)longmapsto(\xi,\eta,\zeta)=(y,z,-x)
\]

from $x+yz=0$ to $\zeta=\xi\eta$. The resulting parameters are in a fixed $O(1)$ box, but the claim that they lie in the source's literal $[-1,1]^2$ parameter square still requires harmless but explicit constant-size partitioning/rescaling because $b\asymp D$ and $|a|\asymp L$ do not fix constants below one.

With

\[
t_i={cL\over\kappa_iD},
\qquad \kappa_1=1,\quad\kappa_2=4,
\]

the Round-131 phase identity becomes

\[
{ca\over\kappa_i b}-{ca'\over\kappa_i b'}
=t_i(\eta_{r'}-\eta_r).
\]

This equality has the correct sign. Under the source extension convention $e(x\cdot\omega)$, however, its literal factorization is

\[
e(-t_i\eta_r)\,e(t_i\eta_{r'}),
\]

so the outer and inner waves are naturally evaluated at $(0,-t_i,0)$ and $(0,t_i,0)$, respectively. That is not yet the same-point product $f_1(x)f_2(x)$ appearing in Demeter--Wu. Reflecting one chart can put both factors at one point, but then it changes the frequency patches and their transversality relation; this is an applicability construction, not part of (132.C4).

Finally,

\[
\eta_{r'}-\eta_r
={D\over L}\left({a\over b}-{a'\over b'}\right)
={Dn\over Lbb'}.
\]

Since $n$ is a positive integer and $n\ll D^2/W$,

\[
{1\over LD}\lesssim\eta_{r'}-\eta_r
\ll {D\over LW}=Y^{-5/48}.
\]

The lower endpoint is a universal floor for a nonempty determinant band, not a claim that every dyadic band or every integer $n$ occurs.

## 3. Proof and source-interface derivation

The scale arithmetic is

\[
W=Y^{21/48},\qquad D=Y^{24/48},\qquad L=Y^{8/48}.
\]

Therefore

\[
t_i\asymp Y^{48/48+8/48-24/48}=Y^{32/48},
\]

\[
\delta_*={D\over LW}=Y^{24/48-8/48-21/48}=Y^{-5/48},
\]

and

\[
t_i\delta_*=Y^{27/48}=Y/W.
\]

At the smallest possible gap $h\asymp(LD)^{-1}=Y^{-32/48}$, the dual coordinate $t_i h$ is only $O(1)$; across the determinant bands it ranges algebraically from $O(1)$ to $Y^{27/48}$.

For a source-normalized $h$-strip near an arbitrary $\eta_0\asymp1$, the correct affine hyperbolic change is

\[
\widetilde\xi=\xi,qquad
\widetilde\eta={\eta-\eta_0\over h},qquad
\widetilde\zeta={\zeta-\eta_0\xi\over h}.
\tag{132.R1}
\]

Indeed $\widetilde\zeta=\widetilde\xi\widetilde\eta$. Equivalently,

\[
(\xi,\eta,\zeta)
=(\widetilde\xi,\eta_0+h\widetilde\eta,
  \eta_0\widetilde\xi+h\widetilde\xi\widetilde\eta).
\]

For physical variables,

\[
x_1\xi+x_2\eta+x_3\zeta
=\eta_0x_2+(x_1+\eta_0x_3)\widetilde\xi
  +hx_2\widetilde\eta+hx_3\widetilde\xi\widetilde\eta.
\]

Thus $(0,\pm t_i,0)$ maps, up to the frequency-independent phase $e(\pm\eta_0t_i)$, to $(0,\pm ht_i,0)$. This proves the dual-coordinate part of (132.C10), but nothing here identifies $ht_i$ with the source's $R$.

The source audit gives two distinct rescaling interfaces:

1. The bilinear proofs use explicit hyperbolic affine maps together with transformed Fourier thickness and **both-coordinate** transversality. The refined Proposition 3.7 additionally assumes general-position rectangles, incidence bounds, and its own scale relation. None of those hypotheses follows from (132.R1).
2. The linear Theorem 2.4 proof uses the inverse of the dilation in (132.C9) for a horizontal ruling strip, changing its linear decoupling scale by the strip width. But it retains the horizontal/vertical rectangle energy and is not a license to apply Theorem 1.6 or 1.10 to a one-coordinate-separated pair.

Moreover, the relation $h<\eta_{r'}-\eta_r\le2h$ localizes only the **difference**. To use one common $\eta_0$ in (132.R1), the $O(1)$ range of base $\eta$ values must be partitioned into $O(h^{-1})$ strips (with only bounded relative offsets for paired strips). The scalar, coefficient ownership, and summation cost of that partition are not priced in the candidate.

Finally, (132.R1) maps source squares back to anisotropic rectangles, and an arithmetic point measure on $\mathbb H$ is not by itself an $L^4$ physical function with a specified $R^{-1}$ Fourier thickness. Mollification, cap ownership, Jacobians, packet incidence, and the pointwise-to-integral bridge all remain external.

## 4. First doubtful or unproved step

The first doubtful step is the sentence after (132.C8) that treats (132.C9) as the relevant normalization of an entire determinant band. The exact dilation is valid, but a legal source call first needs:

1. an $h$-scale localization in the absolute $\eta$ coordinate and the recentered shear (132.R1);
2. a decomposition into subfamilies with $|\xi_{r'}-\xi_r|\asymp1$ as well as normalized $|\widetilde\eta_{r'}-\widetilde\eta_r|\asymp1$;
3. a defined Fourier thickness whose transformed value is $R^{-1}$ and matching square-cap scale;
4. a same-point bilinear representation of the signed phase with literal joint coefficients; and
5. the spatial localization/Jacobian or wave-packet incidence ledger.

The exact same-denominator Round-131 controls have $b'=b$, hence $\xi_{r'}=\xi_r$. They fail item 2 after every $\eta$-only rescaling and must remain in the source's narrow/ruling term. This is already enough to block a blanket bilinear-theorem application.

## 5. Controls and outcomes

| Claim | Outcome | Hostile check |
|---|---|---|
| (132.C1) | **Pass** | Exact dimensionless chart; $b>0$ on the denominator shell. Literal source-box containment still needs an $O(1)$ normalization. |
| (132.C2) | **Pass** | $(b/D)(-Da/(Lb))=-a/L$. |
| (132.C3) | **Pass** | Exact definition; $\kappa_i$ changes only a constant. |
| (132.C4) | **Algebra passes; extension interpretation unproved** | Sign is correct. Natural factors occur at opposite physical points, not automatically in the source's same-point product. |
| (132.C5) | **Pass** | $1+1/6-1/2=2/3=32/48$. |
| (132.C6) | **Pass** | Exact determinant identity with positive sign for $n>0$. |
| (132.C7) | **Pass** | $D(D^2/W)/(LD^2)=D/(LW)=Y^{-5/48}$. |
| (132.C8) | **Pass with scope** | $(LD)^{-1}$ is the integer-determinant floor; nonemptiness of each band is not asserted. |
| (132.C9) | **Revise** | The dilation preserves $\mathbb H$ and normalizes the difference, but without recentering it sends actual $|\eta|\asymp1$ patches to $|\widetilde\eta|\asymp h^{-1}$. Use (132.R1) after strip localization. |
| (132.C10) | **Reject as an unconditional source scale** | Retain only $|\widetilde x_2|=t_i h$. The source parameter $R$ also fixes thickness, cap scale, and localization and is not determined by distance of the evaluation point from the origin. |
| (132.C11) | **Exponent identity passes; theorem meaning unproved** | $t_i\delta_*=Y/W=Y^{27/48}$ exactly, but no decoupling bound or capacity gain follows. |
| source anisotropic-rescaling license | **No for the claimed bilinear import** | The source uses this symmetry for the retained linear narrow rectangle term. The bilinear/refined hypotheses, especially both-coordinate transversality, are not supplied. |

All checks are algebraic/source-interface checks; no numerical experiment was used.

## 6. Dependencies and exact artifacts used

1. `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/candidates/conductor_exact_hyperbolic_normalization.md`;
2. `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reports/demeter_wu_exact_source_card.md`;
3. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/blind_statement.md`; and
4. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/conductor_round131_residue_mode_adjudication.md`, especially (131.C2)--(131.C5), the same-denominator controls, and the capacity ladder.

No sibling Round-132 report, shared graph, plan, synthesis, validation file, or secondary source was used or edited.

## 7. Recommended state effect

**Revise.** Retain the exact chart and identities (132.C1)--(132.C8), and retain $t_i\delta_*=Y/W$ only as algebraic scale bookkeeping. Replace (132.C9) by the recentered strip map (132.R1), relabel (132.C10) as a dual evaluation-coordinate identity rather than a Demeter--Wu radius, and do not promote any source applicability. The first surviving obstruction is exact: same-denominator pairs remain nontransverse in $\xi$, while all other strata still require strip localization, Fourier-thickness/cap matching, coefficient factorization, and a pointwise bridge.

## 1. Result

**No-go for the unqualified commuting claim; conditional certification of the rho algebra.** The hierarchical mask gives the full \(A=0\) arithmetic residue, and the \(E_1/R_1\) artificial pole and every rho-cutoff derivative cancel when all pieces have literally identical masks, domains, sides, and regularization. However:

1. the beta endpoint prefix remains \(\psi(\beta)\)-masked and is not the proved unmasked endpoint module;
2. finite displacement of the \(v\)-line at fixed \(s,u\) creates an additional Cauchy--Green area operator, plus axial/mixed companions under a later \(u\)-displacement.

Thus the frozen compatibility statement is not certified. Endpoint collapse must either precede localization globally, with its artificial-pole cancellation still carried through later displacements, or all three hierarchical branches and their connectors must be recombined before invoking the physical endpoint estimates.

## 2. Exact statement and hypotheses

Let \(A=s-(u+v)/2=x+i\beta\), with \(s=\sigma+it\), \(u=a+i\mu\), \(v=b+i\nu\), so

\[
 \beta=t-\frac{\mu+\nu}{2}.
\]

Take finite rectangles with no pole on a boundary, upward verticals, and horizontal segments \(H_\pm\) oriented left-to-right. Assume \(\psi\in C^2\) (or interpret the mixed derivative distributionally), \(\psi(0)=1\), and use the same profiles, floors, endpoint conventions, finite domains, and regularization for \(G,E_1,R_1\). The radial endpoint algebra and rho cancellation are exact under these hypotheses. A fixed-\(s,u\) \(v\)-shift, however, obeys the counteridentity (33.4), so commutation requires its area operator, finite sides, and induced lower-dimensional strata.

## 3. Proof or derivation

For a positive \(A\)-rectangle, Stokes gives

\[
 V_{x_0}=V_{x_1}+H_+-H_-+2\pi i\sum_p\psi(\Im p)\operatorname{Res}_pF
 -\iint \psi'(\beta)F\,dx\,d\beta .                                      \tag{33.1}
\]

Indeed \(2i\bar\partial\psi=-\psi'\). Writing
\(C_A[F]=\iint\psi'(\beta)F\), the masked endpoint orientation is therefore

\[
 T_\xi^\beta+S_\xi^\beta+P_\xi^\beta
   =D_\xi^\beta-A_\xi+C_A[E_{\xi}].                                      \tag{33.2}
\]

Here \(S_\xi\) is upper left-to-right plus lower right-to-left. At the arithmetic pole \(A=0\), \(\psi(0)=1\), hence \(A_\xi^\beta=A_\xi\): this is the full, not a filtered, residue. But \(D_\xi^\beta\) is integrated away from \(A=0\) and remains masked. In the hierarchical partition

\[
 \Theta_\beta=\psi(\beta),\qquad
 \Theta_\alpha=(1-\psi(\beta))\psi(\alpha),\qquad
 \Theta_o=(1-\psi(\beta))(1-\psi(\alpha)),
\]

only

\[
 D_\xi^\beta+D_\xi^\alpha+D_\xi^o=D_\xi,\qquad
 C_A^\beta+C_A^\alpha+C_A^o=0                                           \tag{33.3}
\]

recovers the unmasked endpoint module. The two internal beta shares sum merely to \(\psi(\beta)\), not to \(1\). Thus the accepted unmasked lower/upper endpoint estimates cannot be applied to \(D_\xi^\beta\) alone. This remains true although the \(A=0\) residue belongs wholly to beta.

At the artificial rho pole, \(E_1\) and \(R_1\) have opposite residues at the same point and therefore the same mask value; they cancel under identical ownership. For any linear finite-contour operation \(\mathcal H\) carrying identical masks, sides, connectors, and regularization,

\[
 \mathcal H[G]-\mathcal H[E_1]-\mathcal H[R_1]
 =\mathcal H[G-E_1-R_1]=0.
\]

This proves \(E_{\rm own}=0\), and its physical \(L\)-derivative is zero, only conditionally on identical ownership. A coincident artificial/arithmetic pole must be taken as one derivative residue.

Now move \(v\) from \(b_+>0\) to \(b_-<0\) while \(s,u\) are fixed. Since
\(\partial_\nu\Theta_\beta=-\psi'(\beta)/2\), (33.1) in the \(v\)-plane becomes

\[
\begin{aligned}
 V_{b_+}^\beta[Q]={}&V_{b_-}^\beta[Q]+H_{v,+}^\beta[Q]-H_{v,-}^\beta[Q]\\
 &+2\pi i\,\psi\!\left(t-\frac\mu2\right)\operatorname{Res}_{v=0}Q\\
 &+\underbrace{\frac12\int_{b_-}^{b_+}\int_{-V}^{V}
 \psi'\!\left(t-\frac{\mu+\nu}{2}\right)Q(x+i\nu)\,d\nu\,dx}_{B_{v,\psi}[Q]} .
                                                                            \tag{33.4}
\end{aligned}
\]

The lower horizontal has the minus sign because its positive boundary orientation is right-to-left. Formula (33.4) is the counteridentity: the \(v=0\) residue is filtered by \(\psi(t-\mu/2)\), and \(B_{v,\psi}\) is generally nonzero. Even \(Q\equiv1\) gives
\((b_+-b_-)[\psi(t-\mu/2+V/2)-\psi(t-\mu/2-V/2)]\), so the area operator cannot be deleted by contour algebra.

If the \(u\)-line is also displaced, there is an analogous \(B_{u,\psi}\). Displacing \(u\) through \(B_{v,\psi}\) produces the mixed weight

\[
 \partial_{\mu\nu}\Theta_\beta=\frac14\psi''(\beta),                       \tag{33.5}
\]

plus the \(u=0\) residue of that connector. For full-axis conventions the pure axial union is \(R_v^\beta+R_u^\beta-R_{uv}^\beta\); the joint corner has weight \(\psi(t)\) and is counted once. Equivalently, a sequential ledger may list the corner once positively and use corner-deleted axis residues. These pure strata do not replace the connector-axis and mixed term (33.5). Changing to coordinates \((A,v)\) makes the mask independent of \(v\), but shears the finite \(s\)-box; the missing contribution then reappears on the slanted finite boundary.

## 4. First doubtful or unproved step

The permitted accepted artifacts do not define \(B_{v,\psi}\), its \(u=0\) residue, or the mixed term (33.5) on the terminal, renormalized radial-side, endpoint, and arithmetic strata. They therefore do not establish a commuting square. Routing only \(R_v\), \(R_u\), \(R_{uv}\), and \(H_{v,+}-H_{v,-}\) leaves \(B_{v,\psi}\). Separately, routing the beta endpoint prefix to the proved unmasked endpoint module omits \(D_\xi^\alpha+D_\xi^o\). If \(E_1\) is removed globally before localization, its cancelling artificial residue must still accompany any later displacement of isolated \(R_1\); otherwise the same unequal-ownership defect reappears.

## 5. Control tests and outcomes

- **Hierarchical versus disjoint mask:** pass. Hierarchical gives one radial connector and the full \(A=0\) residue. It does not make the endpoint prefix unmasked.
- **Cauchy--Green orientation:** pass. The radial area sign is minus in (33.1); the fixed-\(s,u\) \(v\)-area term is plus because \(\partial_\nu\beta=-1/2\).
- **Endpoint/artificial/arithmetic ledger:** artificial and arithmetic residues pass under the same mask. The endpoint-module invocation fails until (33.3) is recombined globally.
- **Axial residue and corner count:** fail for a ledger omitting \(B_{v,\psi}\), its axial residue, or (33.5). Pure residues use inclusion--exclusion with one corner.
- **Finite-height connector ownership:** fail as presently specified. \(H_{v,+}-H_{v,-}\) does not replace the area connector.
- **Rho ownership defect:** conditionally pass by \(G=E_1+R_1\); not established after unequal endpoint/axial routing.
- **Profile, star, normalization:** finite identities retain full endpoint coefficients and have no Perron half-star. The star appears only in the justified symmetric limit. Every share keeps all profiles/floors and the common factor \(-4X^{1/4}\Re(e(1/8)\cdot)/\pi\).

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, and the Round-19, Round-22, Round-26, and Round-32 synthesis/axial-ownership artifacts named in the task brief. No claimant report, literature import, or numerical experiment was used.

## 7. Recommended state effect

**Revise and retain open.** Promote only the scoped facts: signs (33.1)--(33.4), full hierarchical \(A=0\) ownership, same-mask artificial-pole cancellation, and conditional all-order rho cancellation. Require either global endpoint collapse before localization or all-branch recombination (33.3) before using the physical endpoint modules. Add \(B_{v,\psi}\), its two horizontal boundaries, its \(u=0\) residue, and the mixed connector/corner ledger to the finite compatibility obligation. Do not invoke the upper-endpoint or \(R_1\)-arithmetic estimates outside their accepted physical symmetric-profile scope, and do not promote a terminal-symbol estimate.

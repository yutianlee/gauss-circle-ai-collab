# Blind hierarchical partition and recombined radial displacement

Campaign: m9-m1-beta-radial-pushforward-bv  
Task: blind_hierarchical_recombined_identity  
Role: statement-only blind rederivation  
Status: candidate evidence only

## 1. Result

The hierarchical identity

\[
1=\psi(\beta)+(1-\psi(\beta))\psi(\alpha)
 +(1-\psi(\beta))(1-\psi(\alpha))
\tag{27.1}
\]

is exact and assigns the complete double-bounded box to the beta branch.
Inside that branch,

\[
\psi(\beta)
=\psi(\beta)\psi(\alpha)
 +\psi(\beta)(1-\psi(\alpha)).
\tag{27.2}
\]

The first summand is the double-bounded share. The two internal shares have
complementary connector terms and complementary \(A=0\) residue weights;
their sum has the one-edge beta connector and the full \(A=0\) residue.

The finite Cauchy--Green displacement is exact only when applied first to
the recombined radial factor \(G=E_1+R_1\). Its apparent \(\rho=0\) pole
cancels algebraically. After the complete same-mask \(E_1\) image is
assigned to the accepted endpoint ledger, \(R_1\) is the remaining
nonendpoint image, with its opposite artificial residue still reconciled
against that ledger.

The exact height algebra is

\[
r:=-\Im\rho=\frac{\alpha+\beta+\nu}{2},\qquad
\mu=\alpha-\beta-\nu,\qquad
\boxed{\alpha=r+\frac{\mu}{2}}.
\tag{27.3}
\]

It displays the two denominators of the hard-top \(R_1\) term:
\(\rho^{-1}(a+i\mu)^{-1}\). A smooth split can keep \(G\) near
\(\rho=0\) and use \(R_1\) where \(|\rho|\) is large without losing the
artificial-pole ledger. No estimate of this convolution or of the
positive-\(\alpha\) kernel is claimed.

## 2. Exact statement and hypotheses

Put

\[
A=s-\frac z2=\sigma_A+i\beta,\qquad
B=A+z,\qquad
u=a+i\mu,\qquad v=b+i\nu.
\]

Then \(\alpha=\Im B=\beta+\mu+\nu\). Let
\(\psi\in C_c^\infty(\mathbb R)\) be even, equal to one on
\([-B_0,B_0]\), and supported in \([-2B_0,2B_0]\). Define

\[
\Theta_{\rm db}=\psi(\beta)\psi(\alpha),\qquad
\Theta_{\rm ah}=\psi(\beta)(1-\psi(\alpha)).
\tag{27.4}
\]

The double-bounded support has \(|\alpha|,|\beta|\le 2B_0\) and is empty
when \(|\Im z|>4B_0\).

For \(N=N_X\) and \(C=\pi i\sqrt X\), put

\[
\rho=\frac14-A-\frac u2-v,
\qquad
I_1(\rho)=\int_1^N x_{\rm rad}^{\,\rho-1/2}
 e(\sqrt{Xx_{\rm rad}})\,dx_{\rm rad},
\tag{27.5}
\]

\[
E_1(A)=
\frac{N^\rho e(\sqrt{XN})-e(\sqrt X)}{\rho},
\qquad
R_1(A)=-\frac{C I_1(\rho)}{\rho},
\qquad
G(A)=E_1(A)+R_1(A).
\tag{27.6}
\]

Let \(\mathcal P_j(A,u,v)\) denote all other analytic finite factors,
including the actual factor

\[
\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\tag{27.7}
\]

all exact floors, the smooth interior or one-sided hard-top profile, the
top half-star, and all unchanged axial and corner data. Set

\[
\mathcal F_G(A)=
\mathcal P_j(A,u,v)\,
\zeta(1-A)X_4(A+z)L(A+z,\chi_4)\,G(A).
\tag{27.8}
\]

Take the finite rectangle
\(\mathcal R=[x_1,x_0]\times[-T,T]\), where
\(x_1=-\kappa<0<x_0=c'-\Re z/2\), and assume no genuine pole is on its
boundary. For a \(C^1\) height mask \(\Theta\), define upward verticals
\(V_x^G[\Theta]\) and left-to-right horizontals \(H_\pm^G[\Theta]\).
Then

\[
\boxed{\begin{aligned}
V_{x_0}^G[\Theta]
={}&V_{x_1}^G[\Theta]+H_+^G[\Theta]-H_-^G[\Theta]\\
&+2\pi i\sum_{p\in\mathcal R^\circ}
\Theta(\Im p)\operatorname{Res}_{A=p}\mathcal F_G\\
&-\iint_{\mathcal R}\partial_\beta\Theta(\beta)
\mathcal F_G(\sigma_A+i\beta)\,d\sigma_A\,d\beta .
\end{aligned}}
\tag{27.9}
\]

Every term retains the external normalization

\[
-\frac4\pi X^{1/4}
\operatorname{Re}\{e(1/8)(\cdots)\}.
\tag{27.10}
\]

## 3. Proof and exact ledgers

Equation (27.1) follows by partitioning only the complement of the beta
branch by \(\psi(\alpha)+(1-\psi(\alpha))=1\). Thus the double-bounded
piece is owned once. Differentiating (27.4) gives

\[
\partial_\beta\Theta_{\rm db}
=\psi'(\beta)\psi(\alpha)+\psi(\beta)\psi'(\alpha),
\]

\[
\partial_\beta\Theta_{\rm ah}
=\psi'(\beta)(1-\psi(\alpha))-\psi(\beta)\psi'(\alpha).
\tag{27.11}
\]

The \(\psi'(\alpha)\) edges cancel in their sum. At \(A=0\), their weights
are \(\psi(\Im z)\) and \(1-\psi(\Im z)\), so they sum to one.

Positive rectangle orientation and
\(2i\bar\partial\Theta=-\partial_\beta\Theta\) prove (27.9). The upper
horizontal is traversed right-to-left in the boundary, hence the displayed
left-to-right ledger is \(H_+-H_-\). If \(T>2B_0\), these two
\(A\)-horizontals vanish for every beta share; finite outside \(u,v\)
sides remain.

Since

\[
\zeta(1-A)=-\frac1A+O(1),
\]

the genuine crossed residue is

\[
\operatorname{Res}_{A=0}\mathcal F_G
=-\mathcal P_j(0,u,v)\,G(0)L(1-z,\chi_4).
\tag{27.12}
\]

It is the full endpoint-plus-\(R_1\) arithmetic residue and is counted once.

The apparent pole is at

\[
p_\rho=\frac14-\frac u2-v,\qquad \rho=p_\rho-A.
\tag{27.13}
\]

At \(\rho=0\),

\[
C I_1(0)=e(\sqrt{XN})-e(\sqrt X).
\]

Because \(d\rho/dA=-1\),

\[
\operatorname{Res}_{A=p_\rho}E_1
=-\{e(\sqrt{XN})-e(\sqrt X)\},\qquad
\operatorname{Res}_{A=p_\rho}R_1
=+\{e(\sqrt{XN})-e(\sqrt X)\}.
\tag{27.14}
\]

They cancel before any residue is assigned to \(G\). If \(E_1\) is later
removed as an endpoint package, the isolated \(R_1\) identity retains the
second residue in (27.14), explicitly paired with the first residue in the
removed ledger.

For the height identity, (27.5) gives

\[
\Im\rho=-\beta-\frac{\mu}{2}-\nu
=-\frac{\alpha+\beta+\nu}{2}.
\]

Therefore (27.3) follows exactly. At the positive-\(\alpha\) saddle
\(\alpha_0=\pi q\sqrt{Xx_{\rm rad}}/D_j\), in the local range
\(|\nu|\le\alpha_0/4\) with bounded \(\beta\),

\[
\frac1\rho=\frac{2i}{\alpha_0}
+O\left(\frac{1+|\beta+\nu|}{\alpha_0^2}\right),
\tag{27.15}
\]

and hence

\[
-\frac C\rho
=\frac{2D_j}{q\sqrt{x_{\rm rad}}}
+O\left(
\frac{D_j^2(1+|\beta+\nu|)}
{q^2\sqrt X\,x_{\rm rad}}\right).
\tag{27.16}
\]

The \(I_1\) integrand has the \(G\) exponent plus \(1/2\) in
\(x_{\rm rad}\), but no compensating \(\alpha\)-power at fixed
\(x_{\rm rad}\). Thus the isolated \(R_1\) transition has an additional
\(q^{-1}\) factor relative to the unsplit \(q^0\) baseline. This is not
confined to the \(A=0\) residue.

For the hard top, the accepted Hilbert factor contributes
\((a+i\mu)^{-1}\); hence the \(R_1\) height integrand contains, algebraically,

\[
\frac{\widehat\phi(b+i\nu)}
{\rho\,(a+i\mu)}
\quad\text{times the remaining exact factors},\qquad
\alpha=r+\frac{\mu}{2}.
\tag{27.17}
\]

This identifies a two-denominator convolution but proves no bound for it.

## 4. Split-region identity and first unproved step

Choose \(\omega\in C_c^\infty(\mathbb R)\) with
\(\omega(r)=1\) for \(|r|\le R_0\) and
\(\omega(r)=0\) for \(|r|\ge2R_0\). Pointwise,

\[
G=\omega(r)G+(1-\omega(r))E_1+(1-\omega(r))R_1.
\tag{27.18}
\]

Thus \(G\) is kept recombined near \(\rho=0\), while the split factors are
used only away from it. After the full same-mask endpoint \(E_1\) image is
removed, the exact \(R_1\) survivor may instead be written

\[
\boxed{
R_1=\omega(r)G+(1-\omega(r))R_1-\omega(r)E_1.
}
\tag{27.19}
\]

This is the required artificial-pole ledger:

- \(\omega G\) is regular at \(\rho=0\);
- \((1-\omega)R_1\) vanishes in a neighborhood of that pole;
- \(-\omega E_1\) carries
  \(-\operatorname{Res}E_1=\operatorname{Res}R_1\).

When Cauchy--Green is applied termwise, the new \(\omega'(r)\) area
connectors cancel exactly because \(G-E_1-R_1=0\) and
\(\partial_\beta r=1\). All outer sides, profiles, floors, stars, and the
normalization (27.10) remain on every term.

The first unproved step is an analytic estimate for (27.17) after the exact
split (27.19), including the hard-top numerator, connector, radial measure,
and outside-height limits. The relation \(\alpha=r+\mu/2\) suggests possible
two-denominator convolution gain, but no \(O(\log\alpha/\alpha^2)\) bound
follows from algebra alone. The double-bounded finite kernel is likewise
isolated but not estimated here.

## 5. Control tests and outcomes

**Support and degeneracy.** The double-bounded support disappears for
\(|\Im z|>4B_0\). Equations (27.11), (27.18), and (27.19) remain exact
when supports overlap, separate, or shrink. The cutoff \(1-\omega\) is
identically zero near the artificial pole, rather than merely zero at one
point.

**Residue and normalization.** The hierarchical beta branch crosses the
full \(A=0\) residue. Its two internal shares cross complementary filtered
parts and cannot separately invoke the unmasked residue theorem. The
artificial residues cancel in \(G\) and reappear exactly as described in
(27.19) after endpoint removal. The external factor (27.10) occurs once;
neither masking nor the top half-star halves an integration-by-parts
endpoint.

**Scope.** The identities are coefficient-blind. They neither estimate the
positive-\(\alpha\) kernel nor prove a signed, unsigned, or adversarial
analogue.

## 6. Dependencies and artifacts used

- protocol.md
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md
- rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md
- rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md
- rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md
- rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/briefs/blind_hierarchical_recombined_identity.md

No other Round-27 report, proof graph, proof draft, numerical experiment,
or external source was read or used.

## 7. Recommended state effect

Promote, after independent seam agreement, the hierarchical partition,
double-bounded ownership, connector cancellation, full \(A=0\) ledger,
finite recombined displacement, and artificial-pole cancellation.

Promote as exact algebra the height identity (27.3), the \(R_1\)
normalization (27.15)--(27.16), and the split identities
(27.18)--(27.19).

Retain open every estimate for the double-bounded share, the
two-denominator hard-top convolution, the positive-\(\alpha\) radial
pushforward, the complete-profile \(q\)-BV theorem, and the full beta
transition.

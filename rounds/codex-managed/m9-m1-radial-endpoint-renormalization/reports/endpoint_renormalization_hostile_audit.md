# Endpoint-renormalization hostile audit

## 1. Result

**REVISE.** Finite endpoint subtraction is valid and, after sufficiently many terms, the *renormalized* radial horizontal sides can be removed by an explicit nested exhaustion. However, the endpoint coefficients have full weight, not one-half; the lower endpoint has the opposite sign to the upper endpoint; and the lower radial side has the opposite contour orientation to the upper side. The resulting boundary functional does not cancel termwise between the two sides or with an existing residue. Subtraction also creates artificial moving poles whose residues must be ledgered. Thus only the subtraction algebra and scoped side removal are promotable; the boundary and transition operators remain open.

## 2. Exact statement and hypotheses

Let \(N=N_X\),

\[
 G_v(w)=\int_1^N x^{w-7/4-v/2}e(\sqrt{Xx})\,dx,
 \qquad \rho=w-\frac34-\frac v2,\quad C=\pi i\sqrt X.
\]

For \(I_k=\int_1^N x^{\rho+k/2-1}e(\sqrt{Xx})\,dx\), integration by parts gives

\[
 I_k=\frac{[x^{\rho+k/2}e(\sqrt{Xx})]_1^N}{\rho+k/2}
 -\frac{C}{\rho+k/2}I_{k+1}.
\]

Hence, exactly for every \(M\ge1\),

\[
 G_v(w)=E_M(w,v)+R_M(w,v),
\]
\[
 E_M=\sum_{k=0}^{M-1}
 \frac{(-C)^k\{N^{\rho+k/2}e(\sqrt{XN})-e(\sqrt X)\}}
 {\prod_{r=0}^{k}(\rho+r/2)},
 \quad
 R_M=\frac{(-C)^M I_M}{\prod_{r=0}^{M-1}(\rho+r/2)}. \tag{1}
\]

Use the Round-19 rectangle, \(w=\sigma\pm iS\),
\(\lambda=1-c'<0\), \(|\Im u|\le U\), \(|\Im v|\le V\), and take
\(S\gg X+U+V\).

## 3. Proof or derivation

Formula (1) follows from
\(d\,e(\sqrt{Xx})/dx=Cx^{-1/2}e(\sqrt{Xx})\). The bracket fixes the signs:
\(x=N\) is positive and \(x=1\) negative. Endpoint stars do **not** halve
either coefficient. Changing a function at two measure-zero points does
not change \(G_v\); the half weights arise only from symmetric inverse
Mellin/Perron limits at the physical endpoints.

The radial rectangle contributes

\[
 \int_\lambda^c Q(\sigma+iS)\,d\sigma
 -\int_\lambda^c Q(\sigma-iS)\,d\sigma. \tag{2}
\]

Thus the endpoint functional is \(E_M^+F_z^+-E_M^-F_z^-\), not their sum.
In particular, for the \(x=1\), \(k=0\) term, with
\(\Im u=\Im v=0\), \(A=\sigma-3/4-b/2\), its oriented value is

\[
 -e(\sqrt X)\left\{
 \frac{F_\zeta(\sigma+iS)}{A+iS}
 -\frac{F_\zeta(\sigma-iS)}{A-iS}\right\}. \tag{3}
\]

At a sufficiently far-right \(\sigma=c\), the absolutely convergent series
makes \(F_\zeta(c\pm iS)=1+o(1)\) uniformly. The main part of (3) is
\(2iS e(\sqrt X)/(A^2+S^2)\ne0\). Hence the side orientation converts the
opposite denominator signs into reinforcement, not cancellation.

For \(|\Im v|\le V\) and \(S\gg X+U+V\), all denominators in (1) are
\(\asymp S\). One further nonstationary integration by parts in \(I_M\)
yields

\[
 R_M(\sigma\pm iS,v)\ll_{X,N,M,c,c',b}S^{-M-1}.
\]

Combining this with the accepted worst left-edge capacity
\(F_z(\sigma\pm iS)\ll S^{1-2\lambda}\), the \(L^1\) \(v\)-weight, and
the top absolute cost \(O(\log(2+U))\), gives

\[
 \mathfrak B^{\rm ren}_{U,V,S}
 \ll_{X,M}(\log X)\log(2+U)S^{-M-2\lambda}. \tag{4}
\]

Thus any fixed \(M>-2\lambda\), followed by a sufficiently high polynomial
\(S=S(X,U,V)\), removes the renormalized radial sides. It does not estimate
\(E_M\) or the diagonal transition traces.

Each summand in (1) has artificial poles

\[
 w=\frac34+\frac v2-\frac r2\qquad(0\le r<M).
\]

They cancel between \(E_M\) and \(R_M\), since \(G_v\) is entire. If the
two pieces are shifted separately, their residues must cancel explicitly.
At the arithmetic pole \(w_0=1-(u+v)/2\), the residue splits as
\([E_M(w_0,v)+R_M(w_0,v)]L(1-u-v,\chi_4)\). Retaining the original
\(G_v(w_0)L\) and either split residue double-counts it. The same rule
applies to later \(u=0\), \(v=0\), and corner residues.

## 4. First doubtful or unproved step

The first unproved step is any signed bound or cancellation identity for
the explicit \(E_M\) boundary functional together with the two swept
vector-Hilbert traces. Equation (4) removes only \(R_M\)'s radial sides.
No endpoint sign, star convention, or existing residue cancels \(E_M\)
automatically.

## 5. Required control tests and outcomes

The phase-free identity

\[
 \int_1^N x^{w-1}dx=(N^w-1)/w
\]

is unchanged by endpoint stars and has full endpoint coefficients:
**half-coefficient claims fail exactly**. Formula (3) is an actual-family
countercontrol to upper/lower cancellation. The artificial-pole test passes
only when the residues of \(E_M\) and \(R_M\) are opposite and the
arithmetic residue recombines to \(G_v(w_0)L\).

## 6. Dependencies and exact artifacts used

Used `protocol.md`, the proof graph and active campaign, all Round-19 synthesis/reports, Round-20 synthesis and its two completed reports, and the assigned Round-21 brief. No Round-21 claimant report, external source, or numerical experiment was used.

## 7. Recommended state effect

Promote (1), the full-weight/sign/orientation conventions, the artificial-pole ledger, and the scoped vanishing lemma (4). Reject half-weighted IBP endpoints, termwise upper/lower cancellation, and retention of both the unsplit and split residues. Retain `M9-M1-renormalized-radial-boundary-operator`, both transition traces, GAR, M9-M1, and M9 as open.

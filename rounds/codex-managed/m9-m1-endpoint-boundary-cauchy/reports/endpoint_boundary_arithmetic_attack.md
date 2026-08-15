# Endpoint boundary arithmetic attack

## 1. Result

For \(M=1\), finite Cauchy algebra separates the endpoint operator into
two physical divisor sums, one already-listed arithmetic-residue piece,
and one artificial residue which cancels exactly against the residue of
the renormalized remainder. After the nested radial limit, the physical
sum at \(\xi=1\) is a single starred incidence and is \(O(\log X)\); at
\(\xi=N_X\) it is

\[
 O\!\left(N_X^{1/4}\log ^2(2X)\right)
 =O\!\left(X^{1/8}\log ^2(2X)\right). \tag{1}
\]

After restoring the external \(X^{1/4}\) in the active M1 aggregate, only
the lower endpoint is target-safe.  The upper bound in (1) would contribute
\(O(X^{3/8}\log ^2X)\), so it does not prove GAR.  There is no accepted
cancellation with the arithmetic residue: the Cauchy identity returns that
term to the pre-existing residue ledger.

## 2. Exact statement and hypotheses

Put \(N=N_X\), \(z=u+v\),

\[
 p(v)=\frac34+\frac v2,\qquad w_0(z)=1-\frac z2,\qquad
 \epsilon_N=1,\quad \epsilon_1=-1,
\]

and, for \(\xi\in\{1,N\}\),

\[
 E_{\xi,v}(w)=\epsilon_\xi e(\sqrt{X\xi})
 \frac{\xi^{\,w-p(v)}}{w-p(v)}. \tag{2}
\]

Then \(E^{(M=1)}_v=E_{N,v}+E_{1,v}\). Use exactly the finite
Round-19 rectangle, with \(S>(U+V)/2\), and choose the harmless small
outside abscissae so that \(a/2+b<1/4\); hence \(p(v)\ne w_0(z)\).
Coincident poles can instead be grouped as one double residue.

Let \(\mathfrak T_\xi,\mathfrak S_\xi\) be the terminal and the two
oriented radial-side integrals containing (2), and let
\(\mathfrak P_\xi\) be the residue at \(w=p(v)\). Finite Cauchy gives

\[
 \boxed{\mathfrak T_\xi+\mathfrak S_\xi+\mathfrak P_\xi
 =\mathfrak D_{\xi;U,V,S}-\mathfrak A_{\xi;U,V}.} \tag{3}
\]

Here \(\mathfrak D_\xi\) is the original right-line integral with
\(E_{\xi,v}(w)F_z(w)\), while

\[
 \mathfrak A_{\xi;U,V}=\epsilon_\xi e(\sqrt{X\xi})
 \sum_j\frac1{(2\pi i)^2}\iint
 \mathcal A_j(u,v)
 \frac{\xi^{\,1/4-u/2-v}}{1/4-u/2-v}
 L(1-u-v,\chi_4)\,dv\,du . \tag{4}
\]

All contours in (3)--(4) remain finite and have their Round-19
orientations.

## 3. Proof and reduction to original variables

The poles inside the radial rectangle are \(w=w_0\), with residue (4),
and the artificial pole \(w=p\), with residue

\[
 \mathfrak P_N+\mathfrak P_1=(e(\sqrt{XN})-e(\sqrt X))
 \sum_j\frac1{(2\pi i)^2}\iint
 \mathcal A_j(u,v)F_{u+v}(p(v))\,dv\,du . \tag{5}
\]

The accepted upper-side orientation is left-to-right and the lower one
right-to-left. The residue theorem therefore gives (3), with the minus
sign before (4). The residue (5) is cancelled by the opposite artificial
residue of \(R_{1,v}\); retaining it twice is forbidden.

On \(\Re w=c\), expand

\[
 F_z(w)=\sum_{h,q\ge1}\chi_4(q)
 \left(\frac qh\right)^{z/2}(hq)^{-w}.
\]

Writing \(v=b+i\nu\), \(\gamma=c-3/4-b/2>1/4\), define the exact finite
Perron factor

\[
 \mathcal P_{S,\nu}^{\gamma}(y)=\frac1{2\pi i}
 \int_{\gamma-i(S+\nu/2)}^{\gamma+i(S-\nu/2)}\frac{y^r}{r}\,dr . \tag{6}
\]

Algebraically, \(\mathfrak D_{\xi;U,V,S}\) equals

\[
 \epsilon_\xi e(\sqrt{X\xi})
 \sum_{j,h,q}\frac{\chi_4(q)}{(hq)^{3/4}}
 \frac1{(2\pi i)^2}\iint
 \widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\sqrt{\frac qh}\right)^u
 \left(\frac{H_j+1}{h}\right)^v
 \mathcal P_{S,\nu}^{\gamma}\!\left(\frac\xi{hq}\right)dv\,du . \tag{7}
\]

This is the requested finite-height reduction; no \(1/r\) absolute
integration was used. Symmetric Perron inversion, with \(S\gg V\) and
then the smooth \(v\)-limit, sends (6) to
\(\mathbf1_{hq<\xi}+\tfrac12\mathbf1_{hq=\xi}\). Hence (7) becomes

\[
 \boxed{\mathfrak D_{\xi;U}=
 \epsilon_\xi e(\sqrt{X\xi})
 \sum_{hq\le\xi}^{*}\frac{\chi_4(q)}{(hq)^{3/4}}
 \mathcal H^{\rm prof}_{U,X}(h,q),} \tag{8}
\]

where \(\mathcal H^{\rm prof}\) is exactly the accepted direct
actual-profile scale sum: its arguments are
\(2\sqrt X\sqrt{h/q}/D_j\) and \(h/(H_j+1)\), with every floor and the
symmetric top profile retained.

The accepted direct-profile lemma gives
\(\sup_{U,h,q}|\mathcal H^{\rm prof}_{U,X}(h,q)|\ll\log(2X)\).
Thus \(\mathfrak D_{1;U}=-\tfrac12e(\sqrt X)
\mathcal H^{\rm prof}_{U,X}(1,1)=O(\log X)\), and

\[
 |\mathfrak D_{N;U}|\ll\log(2X)
 \sum_{hq\le N}(hq)^{-3/4}
 \ll N^{1/4}\log N\log(2X),
\]

proving (1), uniformly in the symmetric top height. This bound does not
use \(\chi_4\), so it is valid even for the unsigned endpoint polynomial;
it says nothing analogous about the interior oscillatory M1 sum.

### Normalization addendum (Round-22 seam correction)

Equations (3), (7), and (8) are identities for the **normalized radial
sum** in Round 14.  The active aggregate is
\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)(\text{normalized radial sum})\}
 +O(\log ^2X).
\]
Consequently GAR requires the signed quantity in (8) to be
\(O_\varepsilon(X^\varepsilon)\), not \(O(X^{1/4+\varepsilon})\).
The lower endpoint contributes
\(O(X^{1/4}\log X)\) after restoration and is target-sized.  The upper
endpoint contributes only
\[
 O\!\left(X^{1/4}N_X^{1/4}\log ^2X\right)
 =O\!\left(X^{3/8}\log ^2X\right). \tag{9}
\]
Moreover (1) is the triangle-inequality capacity
\(\sum_{n\le N}d(n)n^{-3/4}\), so it is not a subconvex estimate.
Neither Round 14 nor Round 15 supplies a cancelling partner.  In
particular, their target-safe one-sided hard-top cotangent boundary is a
spatial-profile endpoint, not this radial \(n=N_X\) polynomial.  The only
accepted recombination is with \(\mathfrak A_N\), the renormalized
remainder, and the transition pieces back into the original GAR sum; that
identity supplies no estimate.

## 4. First doubtful or unproved step

The first missing estimate is now the signed bound
\[
 \sum_{hq\le N_X}^{*}\chi_4(q)(hq)^{-3/4}
 \mathcal H^{\rm prof}_{U,X}(h,q)\ll_\varepsilon X^\varepsilon.
\]
No target-sized estimate is proved for (4) either. It is exactly the endpoint
portion of the existing arithmetic residue, and after (3) the full ledger
contains \(\mathfrak R^{\rm ar}[G]-\sum_\xi\mathfrak A_\xi
=\mathfrak R^{\rm ar}[R_1]\). Estimating that residue, or either swept
transition trace, remains the first open analytic step.

## 5. Required control test and outcome

At \(\xi=1\), (6) gives the starred value \(1/2\) only after symmetric
Perron inversion; the integration-by-parts coefficient in (2) remains
full. The signs are \(+\) at \(N\), \(-\) at \(1\), and (5) cancels only
with the \(R_1\) artificial residue. These controls pass exactly. No
numerical test was used.

## 6. Dependencies and exact artifacts used

Used only the protocol, proof graph, active campaign, Round-21 synthesis
and its two reports, the Round-19 finite vector identity, and the assigned
Round-22 brief for the derivation. The normalization addendum additionally
used only the accepted Round-14/15 recombination syntheses and graph node
\(M9\text{-}M1\text{-global-angular-recombination}\), whose statement
contains GAR. No external theorem or web source was used.

## 7. Recommended state effect

Promote only the exact reductions (3), (7), and (8), plus the target-sized
lower-endpoint bound.  Revise the upper-endpoint conclusion: (1) is a
trivial normalized-capacity estimate and becomes (9) in M1, so retain the
signed \(x=N_X\) boundary polynomial as open. Record that the artificial
residue cancels and that the remaining arithmetic term is old rather than
a new endpoint operator. Retain that arithmetic residue, both diagonal
transition traces, the full post-FE vector estimate, GAR, M9-M1, and M9 as
open.

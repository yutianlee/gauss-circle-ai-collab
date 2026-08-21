# Literal balanced smooth atom-dictionary formalization

Campaign: m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation
Task: literal_atom_dictionary_constructor
Role: formalizer; selected-context access
Starting graph SHA-256: 9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa
Status: candidate evidence only; no shared proof state was edited.

## 1. Result: corrected literal-dictionary lemma

The proposed dictionary is certifiable after three literal repairs.

1. The normalized stationary amplitude must be defined on the positive
   real quadrant, not only at integer pairs, before it is used in the
   continuum profile \(F_{\sigma,u,v}\).
2. “The accepted tests declined the block” must be replaced by a frozen
   finite owner predicate.  The predicate below is deliberately
   conservative: a fixed-constant collar may remain residual, but no
   coefficient is omitted or counted twice.
3. Candidate (113.C28) is only the low-gcd arithmetic identity.  The
   complete physical one-count equality must also display the high-gcd
   coefficient and stationary-transform error.  Equation (2.25) below
   does so.

After these repairs, every smooth balanced residual M2 block has an
explicit coefficientwise dictionary.  It retains all floors, clipping,
constants, signs, the exact \(K/L=16\) boundary, the gcd bottom, owner
corrections, and support crossings.  The bottom gcd atom equals the
telescoping remainder on positive integers exactly.  The resulting
continuum profiles have uniform scale-normalized seminorms.

No irreducible definition remains missing under the accepted smooth
stationary transform and preliminary square/near-square bounds.  The
first unproved step is exactly the signed outside-absolute packet estimate
in Section 4.  It is not attempted here.

## 2. Exact statement and hypotheses

Write \(e(t)=e^{2\pi i t}\).  Let \(X\ge4096\) be real and put

\[
 R=\sqrt X,\qquad y=\lfloor R\rfloor .
\tag{2.1}
\]

Define

\[
 \rho(t)=
 \begin{cases}0,&t\le0,\\ e^{-1/t},&t>0,\end{cases}
 \qquad
 q(t)=\frac{\rho(1-t)}{\rho(t)+\rho(1-t)},
\]
\[
 \eta(t)=q(2(t-1)),\qquad W(t)=\eta(t)-\eta(2t).
\tag{2.2}
\]

Then \(0\le\eta,W\le1\), \(\eta=1\) on \(t\le1\),
\(\eta=0\) on \(t\ge3/2\),
\(W\in C_c^\infty((0,\infty))\),
\(\operatorname {supp}W\subset[1/2,3/2]\), and \(W(1)=1\).

For

\[
 J_y=\lceil\log _2y\rceil,\qquad D_j=2^{-j}y,
\]

set

\[
 w_j(d)=W(d/D_j)\mathbf1_{1\le d\le y}\quad(0\le j<J_y),
 \qquad
 w_{\rm bot}(d)=\eta(d/D_{J_y})\mathbf1_{1\le d\le y}.
\tag{2.3}
\]

An active denominator label satisfies \(D_j\ge X^{1/4}\), and its exact
height is

\[
 H=H_j=\lfloor D_jX^{-1/4}\rfloor\ge1.
\tag{2.4}
\]

For this \(H\), let

\[
 J_H=\lceil\log _2H\rceil,\qquad L_r=2^{-r}H,
\]

and define

\[
 v_{r,H}(h)=W(h/L_r)\mathbf1_{1\le h\le H}
 \quad(0\le r<J_H),
 \qquad
 v_{\rm bot,H}(h)=\eta(h/L_{J_H})\mathbf1_{1\le h\le H}.
\tag{2.5}
\]

Use even extensions for negative \(h\).  The label \(r=0\), when it
exists, is the clipped terminal frequency label.  The labels
\(1\le r<J_H\) are full smooth labels.  The last term is the bottom
frequency label.  If \(H=1\), then \(J_H=0\), the \(r\)-sum is empty, and
the bottom is the whole partition.

For a smooth denominator \(j\ge1\) and a full frequency label
\(1\le r<J_H\), put

\[
 D=D_j,\qquad L=L_r,\qquad K=\frac{XL}{D^2},\qquad M=LK.
\tag{2.6}
\]

Freeze the following exact finite owner convention.  In the displayed
priority order, define

\[
 \mathfrak E_{\rm T}(D,L)=1+D/L,
\]
\[
 \mathfrak E_2(D,L)
 =1+(LX/D)^{1/2}+D^{3/2}(LX)^{-1/2},
\]
\[
 \mathfrak E_{\rm Y}(D,L)
 =X^{89/1282}L^{89/1282}D^{819/1282}.
\tag{2.7}
\]

Assign the label to T2S if
\(\mathfrak E_{\rm T}\le X^{1/4}\); otherwise to the full
second-derivative owner if \(\mathfrak E_2\le X^{1/4}\); otherwise to TTY
if \(\mathfrak E_{\rm Y}\le X^{1/4}\); otherwise call it residual.
Equality goes to the earlier owner.  This is a literal finite predicate,
not the asymptotic power shadow of an owner estimate.  The clipped
\(r=0\) label is assigned directly to the accepted terminal owner.  On a
balanced smooth denominator, the frequency bottom is assigned to the
second-derivative owner, as proved in Section 3.

Let \(\mathcal R_{\rm bal}(X)\) be the finite set of residual pairs
\(B=(j,r)\) satisfying

\[
 j\ge1,\quad D_j\ge X^{1/4},\quad H_j\ge1,\quad
 1\le r<J_{H_j},\quad 1\le K/L\le16.
\tag{2.8}
\]

Ratio equality belongs to the balanced side.  The hard \(j=0\) profile,
clipped frequency, frequency bottom, and unbalanced ratio \(K/L>16\) are
tagged but do not enter this dictionary.  Set
\(\Omega_B=\{\ast\}\); thus the packet never combines distinct physical
\(D\)- or \(L\)-blocks.

Define the audited taper

\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u\qquad(0<u<1).
\tag{2.9}
\]

For \(h>0\),

\[
 \alpha_{h,H}=-\frac{\Phi(h/(H+1))}{2\pi i h},\qquad
 C_h=e(h/4)-e(3h/4)=2i\chi _4(h),
\]
\[
 \alpha_{h,H}C_h
 =-\frac{\Phi(h/(H+1))\chi _4(h)}{\pi h}.
\tag{2.10}
\]

For \(B=(j,r)\in\mathcal R_{\rm bal}(X)\), define the positive physical
child and the two-sided physical block, including the outer factor four,
by

\[
 \mathcal B_B^+
 =-\frac1\pi\sum_{h\ge1}
 \frac{\chi _4(h)W(h/L)\Phi(h/(H+1))}{h}
 \sum_{d\ge1}W(d/D)e(hX/(4d)),
\]
\[
 B_{2,B}=8\operatorname {Re}\mathcal B_B^+.
\tag{2.11}
\]

Equivalently, one may write the inner sum over \(\mathbb Z\) only after
declaring the entire \(d=0\) summand by
\[
 \left[W(d/D)e(hX/(4d))\right]_{d=0}:=0;
\]
all negative-\(d\) terms vanish by support.  Thus no undefined phase is
ever multiplied by a zero weight.  Define the real continuum stationary
amplitude on \((0,\infty)^2\) by

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left(\frac{M}{xz}\right)^{3/4}
 W\!\left(\sqrt{\frac{xX}{4zD^2}}\right),
\tag{2.12}
\]

and extend it by zero off the positive quadrant.  The actual normalized
integer coefficient is

\[
 a_B(h,k)=\chi _4(h)A_B(h,k).
\tag{2.13}
\]

Put

\[
 \mathcal T_B=\sum_{h,k\ge1}a_B(h,k)e(R\sqrt{hk}),\qquad
 c_B=\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4},
\]
\[
 E_{B,\rm tr}:=\mathcal B_B^++c_B\mathcal T_B.
\tag{2.14}
\]

The accepted smooth transform states
\(\lvert E_{B,\rm tr}\rvert\ll1\), uniformly in these labels.  This exact
definition assigns every zero/nonstationary mode, stationary remainder,
and smooth support entry or exit to one transform-error tag.

For the gcd dictionary, set

\[
 G_0=\frac{\sqrt L}{2},\qquad
 S=\max(0,\lceil\log _2G_0\rceil),\qquad
 G_s=2^{-s}G_0\quad(0\le s\le S).
\tag{2.15}
\]

For \(0\le s<S\), let \(\psi_s(g)=W(g/G_s)\).  Define

\[
 c_L=\eta(1/G_S),\qquad \psi_{\rm bot}(g)=c_LW(g),
\]
\[
 \psi_{\rm hi}(g)=1-\sum_{s=0}^{S-1}\psi_s(g)-\psi_{\rm bot}(g)
 \qquad(g\in\mathbb N).
\tag{2.16}
\]

Let \(\Sigma_L=\{0,\ldots,S-1,\mathrm{bot}\}\), retaining harmless zero
atoms.  For \(\sigma=s\), set
\((G_\sigma,\vartheta_\sigma)=(G_s,W)\), and for the bottom set
\((G_\sigma,\vartheta_\sigma)=(1,c_LW)\).
For coprime positive integers \(u,v\), define

\[
 F_{B,\sigma,u,v}(t)
 =\vartheta_\sigma(t)A_B(G_\sigma tu,G_\sigma tv),
 \qquad t\in\mathbb R,
\tag{2.17}
\]

using the zero extension in (2.12).  With

\[
 \widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
\]

define

\[
\begin{aligned}
 Q_{B,\sigma}^{\rm full}(R)
 =\sum_{\substack{(u,v)=1\\ u\ {\rm odd}}}\chi _4(u)
 \sum_{n\in\mathbb Z}\bigg[
 &\widehat F_{B,\sigma,u,v}
 \!\left(G_\sigma(n-R\sqrt{uv}-\tfrac14)\right)\\
 -&\widehat F_{B,\sigma,u,v}
 \!\left(G_\sigma(n-R\sqrt{uv}-\tfrac34)\right)
 \bigg].
\end{aligned}
\tag{2.18}
\]

Equivalently, atom labels are
\((B,\sigma,u,v,n,\epsilon)\), where
\((\theta_+,s_+)=(1/4,1)\) and
\((\theta_-,s_-)=(3/4,-1)\), with dual coefficient

\[
 \mathfrak a_{B,\sigma,u,v,n,\epsilon}
 =\frac{G_\sigma}{2i}\chi _4(u)s_\epsilon
 \widehat F_{B,\sigma,u,v}
 \!\left(G_\sigma(n-R\sqrt{uv}-\theta_\epsilon)\right).
\tag{2.19}
\]

This is the literal actual-symbol atom dictionary.  Its profile and shell
lists are finite for each \(B\); its Poisson \(n\)-sum is absolutely
convergent.

For \(g=(h,k)\), put

\[
 \lambda_{\rm low}(g)
 =\sum_{\sigma\in\Sigma_L}\psi_\sigma(g).
\]

Define

\[
 \mathcal T_B^{\rm hi}
 =\sum_{h,k\ge1}a_B(h,k)\psi_{\rm hi}((h,k))e(R\sqrt{hk}),
\]
\[
 \mathcal T_B^{\rm low}
 =\sum_{h,k\ge1}a_B(h,k)\lambda_{\rm low}((h,k))e(R\sqrt{hk}).
\tag{2.20}
\]

Inside the low part, give square priority before near-square:

\[
 \mathcal S_B^{\rm sq}
 =\sum_{\substack{h,k\ge1\\ hk\in\square}}
 a_B(h,k)\lambda_{\rm low}((h,k))e(R\sqrt{hk}),
\tag{2.21}
\]
\[
 \mathcal S_B^{\rm near}
 =\sum_{\substack{h,k\ge1,\ hk\notin\square\\
 \operatorname {dist}(\sqrt{hk},\mathbb Z)\le R^{-1}}}
 a_B(h,k)\lambda_{\rm low}((h,k))e(R\sqrt{hk}).
\tag{2.22}
\]

The exact owner-corrected residual is

\[
\boxed{
\begin{aligned}
 \mathcal T_B^{\rm res}
 &=\mathcal T_B-\mathcal T_B^{\rm hi}
   -\mathcal S_B^{\rm sq}-\mathcal S_B^{\rm near}\\
 &=\frac1{2i}\sum_{\sigma\in\Sigma_L}
   G_\sigma Q_{B,\sigma}^{\rm full}(R)
   -\mathcal S_B^{\rm sq}-\mathcal S_B^{\rm near}.
\end{aligned}}
\tag{2.23}
\]

No square or near-square mask is inserted into \(F\).  High gcd is taken
first; square and near-square are then disjoint restrictions of the low
coefficient.

Define the physical correction tags

\[
 \mathfrak C_{B,\rm tr}=8\Re E_{B,\rm tr},\qquad
 \mathfrak C_{B,\mathsf x}=8\Re(-c_B\mathcal T_B^{\mathsf x})
 \quad(\mathsf x\in\{\rm hi,sq,near\}),
\]
\[
 B_{2,B}^{\rm res}=8\Re(-c_B\mathcal T_B^{\rm res}).
\tag{2.24}
\]

Then the exact physical one-count theorem is

\[
\boxed{
 B_{2,B}=\mathfrak C_{B,\rm tr}
 +\mathfrak C_{B,\rm hi}
 +\mathfrak C_{B,\rm sq}
 +\mathfrak C_{B,\rm near}
 +B_{2,B}^{\rm res}.}
\tag{2.25}
\]

Every coefficient occurs once.  Raw and transformed expressions are
equal representations, not separate contributions.

## 3. Proof and derivation

Because

\[
 W(d/D_j)=\eta(2^jd/y)-\eta(2^{j+1}d/y),
\]

for every integer \(1\le d\le y\),

\[
 \sum_{j=0}^{J_y-1}w_j(d)+w_{\rm bot}(d)=\eta(d/y)=1.
\tag{3.1}
\]

For \(j\ge1\),
\(\operatorname {supp}W(d/D_j)\subset[D_j/2,3D_j/2]
\subset(0,3y/4]\), so its finite-range indicator is inactive.  Only
\(j=0\) contains \(d=y\), with \(W(1)=1\), and has a continuum endpoint
jump.  Thus the hard profile occurs once and never enters
\(\mathcal R_{\rm bal}(X)\).

The same telescope gives, for \(1\le h\le H\),

\[
 \sum_{r=0}^{J_H-1}v_{r,H}(h)+v_{\rm bot,H}(h)=1.
\tag{3.2}
\]

For \(r\ge1\), \(3L_r/2\le3H/4\), so the \(h\le H\) clipping is inactive.
For \(H=1\), (3.2) is the single bottom value one.  For \(H=2\), the top
contains \(h=2\), the bottom contains \(h=1\), and no full smooth label
exists.  Also, on every active scale,

\[
 \frac12DX^{-1/4}\le H\le DX^{-1/4}.
\tag{3.3}
\]

Put \(L_\ast=H/2^{J_H}\in(1/2,1]\).  On positive integers the frequency
bottom is supported at \(h=1\) and equals
\(\eta(1/L_\ast)W(h)\).  A balanced smooth denominator is \(D=y/2\), or
\(D=y/4\) with \(X=y^2\), as shown below.  At frequency scale one, the
accepted second-derivative envelope satisfies

\[
 1+(X/D)^{1/2}+D^{3/2}X^{-1/2}\ll X^{1/4}.
\tag{3.4}
\]

Thus the balanced bottom has the stated prior owner and is not discarded.

The balance boundary is exact:

\[
 \frac KL=\frac X{D_j^2}=4^j\frac X{y^2}.
\tag{3.5}
\]

For \(X\ge4096\), \(y\ge64\) and
\(1\le X/y^2<(1+1/y)^2\).  Hence \(j=1\) is balanced; \(j=2\) has
\(K/L\ge16\), with equality exactly when \(X=y^2\); and \(j\ge3\) is
unbalanced.  The perfect-square equality is therefore assigned once, to
the balanced side.

Direct evaluation modulo four gives

\[
 e(h/4)-e(3h/4)=2i\chi _4(h).
\]

It vanishes for even \(h\), and multiplication by the audited Vaaler
coefficient proves (2.10).  The two-sided coefficient is real and even.
Thus the negative-frequency child is the conjugate of the positive one,
and

\[
 4(\mathcal B_B^++\overline{\mathcal B_B^+})
 =8\Re\mathcal B_B^+.
\]

For a full smooth denominator, the accepted transform is

\[
 \sum_{d\ge1}W(d/D)e(hX/(4d))
 =\frac{e(1/8)(hX)^{1/4}}2
 \sum_{k\ge1}\frac{W(\sqrt{hX/(4kD^2)})}{k^{3/4}}
 e(R\sqrt{hk})+O(1).
\tag{3.6}
\]

Since

\[
 \frac1h\frac{(hX)^{1/4}}{2k^{3/4}}
 =\frac{X^{1/4}}{2M^{3/4}}
 \left(\frac M{hk}\right)^{3/4},
\]

(3.6) gives (2.14), including the minus sign and \(1/(2\pi)\).
Transform errors sum to \(O(1)\), because
\(\sum_{h\asymp L}h^{-1}\ll1\).  Flatness of \(W\) at its support edges
makes entry and exit in the slanted factor smooth; there is no separate
hard crossing atom.

On writing \(x=L\xi\), \(z=K\zeta\), the normalized symbol is

\[
 A_B(L\xi,K\zeta)
 =W(\xi)\Phi(L\xi/(H+1))(\xi\zeta)^{-3/4}
 W(\sqrt{\xi/(4\zeta)}).
\tag{3.7}
\]

Its support lies in the fixed compact set

\[
 \frac12\le\xi\le\frac32,\qquad \frac{\xi}{9}\le\zeta\le\xi.
\tag{3.8}
\]

Because \(r\ge1\), \(L/(H+1)<1/2\), so the \(\Phi\)-argument on (3.8)
stays below \(3/4\).  Smoothness at zero and the fixed gap from one give,
for all \(a,b\ge0\),

\[
 \sup_{x,z>0}
 \lvert(x\partial_x)^a(z\partial_z)^bA_B(x,z)\rvert
 \le C_{a,b},
\tag{3.9}
\]

uniformly in \(X,D,L,H\), all floors, and \(B\).  The zero extension is
canonical and \(C^\infty\), because every boundary is cut out by a flat
compactly supported factor.  The amplitude is real.

For the gcd telescope, \(G_{s+1}=G_s/2\), whence

\[
 \sum_{s=0}^{S-1}W(g/G_s)
 =\eta(g/G_0)-\eta(g/G_S).
\tag{3.10}
\]

If \(S>0\), then \(1/2<G_S\le1\); if \(S=0\), then \(G_S=G_0\le1\).
For every positive integer \(g\),

\[
 \eta(g/G_S)=\eta(1/G_S)W(g)=c_LW(g).
\tag{3.11}
\]

For \(g=1\), this uses \(W(1)=1\); for \(g\ge2\), both sides vanish.
Therefore

\[
 \lambda_{\rm low}(g)=\eta(g/G_0),\qquad
 \psi_{\rm hi}(g)=1-\eta(g/G_0),
\tag{3.12}
\]

so (2.16) is an exact nonnegative partition on every positive integer.
The high weight vanishes for \(g\le\sqrt L/2\) and owns the full smooth
boundary transition.  Every dyadic low shell is supported below
\(3\sqrt L/4\).  The bottom is supported at \(g=1<\sqrt L\), since a full
frequency label has \(L>1\).  No sharp cutoff or unowned Fourier tail
remains.

On the support of \(A_B\), \(h\ll L\), \(k\ll K\ll L\), and
\(\lvert A_B\rvert\ll1\).  Thus

\[
 \lvert\mathcal T_B^{\rm hi}\rvert
 \ll\sum_{\sqrt L/2<g\ll L}(L/g+1)(K/g+1)
 \ll L^{3/2},
\tag{3.13}
\]

using \(L\le K\le16L\).  The accepted square and nonsquare
\(R^{-1}\)-near-square bounds apply to (3.7)--(3.9).  Since
\(0\le\lambda_{\rm low}\le1\),

\[
 \lvert\mathcal S_B^{\rm sq}\rvert+
 \lvert\mathcal S_B^{\rm near}\rvert
 \ll_\varepsilon L^{1+\varepsilon}.
\tag{3.14}
\]

Consequently the high, square, near, and transform correction tags in
(2.24) are target-safe after multiplication by
\(X^{1/4}M^{-3/4}\), because \(M\ge L^2\).

For the continuum shell profile, write
\(x=G_\sigma u/L\), \(z=G_\sigma v/K\).  Formula (2.17) is

\[
 \vartheta_\sigma(t)W(xt)\Phi(xtL/(H+1))
 (xzt^2)^{-3/4}W(\sqrt{x/(4z)}).
\tag{3.15}
\]

Whenever nonzero, \(t\in[1/2,3/2]\), and \(x,z\) range over a fixed compact
subset of \((0,\infty)\).  Since \(0\le c_L\le1\), for all
\(m,N,q\ge0\),

\[
 \operatorname {supp}F_{B,\sigma,u,v}\subset[1/2,3/2],\qquad
 \lVert\partial_t^mF_{B,\sigma,u,v}\rVert_\infty\le C_m,
\tag{3.16}
\]
\[
 \sup_{\xi\in\mathbb R}(1+\lvert\xi\rvert)^N
 \lvert\partial_\xi^q\widehat F_{B,\sigma,u,v}(\xi)\rvert
 \le C_{N,q}.
\tag{3.17}
\]

These are uniform scale-normalized seminorms, including the bottom shell,
empty profiles, floors, and support crossings.  Only finitely many
\(u,v\) make (3.15) nonzero for fixed \(B,\sigma\), and (3.17) makes each
\(n\)-sum absolutely convergent.

Finally write \(h=gu\), \(k=gv\), \((u,v)=1\).  A nonzero character term
has \(u\) odd and
\(\chi _4(gu)=\chi _4(g)\chi _4(u)\).  Using

\[
 \chi _4(g)=\frac{e(g/4)-e(3g/4)}{2i},
\]

Poisson summation in \(g\) gives coefficientwise

\[
 \mathcal T_B^{\rm low}
 =\frac1{2i}\sum_{\sigma\in\Sigma_L}
 G_\sigma Q_{B,\sigma}^{\rm full}(R).
\tag{3.18}
\]

The order is \(1/4\) minus \(3/4\).  Since \(F\) is real,
\(\widehat F(-\xi)=\overline{\widehat F(\xi)}\).  Changing
\(n\mapsto1-n\) yields

\[
 Q_{B,\sigma}^{\rm full}(-R)
 =-\overline{Q_{B,\sigma}^{\rm full}(R)}.
\tag{3.19}
\]

After multiplication by \(1/(2i)\), the extra minus cancels the sign from
conjugating \(1/(2i)\), agreeing with physical frequency conjugacy.
Subtracting the disjoint owner restrictions from (3.18), then inserting
(2.14), proves (2.23) and (2.25).

## 4. First doubtful or unproved step

There is no remaining definitional gap in the corrected dictionary.  The
first unproved step is

\[
\boxed{
 \left|\sum_{\sigma\in\Sigma_L}
 G_\sigma Q_{B,\sigma}^{\rm full}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
}
\tag{4.1}
\]

for each fixed \(B\in\mathcal R_{\rm bal}(X)\).  The modulus is outside
the complete internal gcd-shell sum.  A shellwise
\(\sum_\sigma G_\sigma\lvert Q_{B,\sigma}\rvert\) bound, product-fibre
absolute bound, or character-erasing Gram estimate is stronger and is
not inferred.  Equation (4.1) is not attempted or claimed.

The dictionary is capacity-preserving.  The inherited envelope still
loses

\[
 \min(L^{1/2},R^{1/2}/L),
\]

whose worst value is \(R^{1/6}=X^{1/12}\) at
\(L=R^{1/3}=X^{1/6}\).  This is a deficit, not a saving.

The only convention introduced here is the conservative finite owner
predicate (2.7).  It does not identify its finite-\(X\) labels with the
asymptotic power shadow.  Changing it later requires a new coefficientwise
reconciliation, not a silent relabeling.

## 5. Control tests and outcomes

No numerical experiment was used; every control was algebraic.

| Required control | Outcome |
|---|---|
| denominator_telescoping_and_hard_profile | Pass: (3.1) is exact; only \(j=0\) is clipped, and it contains \(d=y\) with weight one. |
| frequency_telescoping_top_bottom_and_clipping | Pass: (3.2) is exact; only \(r=0\) is clipped, and the bottom coefficient is explicit. |
| height_floor_and_empty_block | Pass: (3.3) retains the floor; \(H=1\) has only bottom, \(H=2\) has top plus bottom, and zero profiles give zero atoms. |
| exact_Phi_and_positive_frequency_constant | Pass: (2.9)--(2.14) retain \(H+1\), the minus sign, \(1/\pi\), stationary \(e(1/8)/2\), and normalized \(1/(2\pi)\). |
| positive_negative_frequency_recombination | Pass: \(B_{2,B}=8\Re\mathcal B_B^+\), while (3.19) contains the necessary minus before multiplication by \(1/(2i)\). |
| balanced_ratio_boundary_and_real_X | Pass: (3.5) proves that \(j=2\) is balanced only at \(X=y^2\), where \(K/L=16\) belongs to the balanced side. |
| stationary_symbol_support_crossings_and_error | Pass: (2.12) contains the full slanted symbol; flat crossings stay in it; every remaining transform term occurs once in \(E_{B,\rm tr}\). |
| smooth_gcd_one_count_and_boundary_owner | Pass: (3.10)--(3.12) prove the bottom exactly and give \(\psi_{\rm hi}=1-\eta(g/G_0)\); the full boundary transition has one owner. |
| square_near_square_and_large_gcd_priority | Pass: high is removed first; square precedes nonsquare near-square; (2.23) subtracts each signed subtotal once and places no arithmetic mask in \(F\). |
| finite_omega_and_no_cross_block_cancellation | Pass: \(\Omega_B\) is a singleton; every modulus in (4.1) concerns one fixed \((j,r,+)\) block. |
| profile_seminorms_and_uniformity | Pass: (3.9), (3.16), and (3.17) are uniform in real \(X\), floors, labels, \(u,v\), gcd scale, bottom coefficient, and empty supports. |
| even-product and false-mask control | Pass: even \(h\) vanishes through \(\chi _4(h)\), while even \(k\) and hence even products remain; no unsigned or complementary-divisor cancellation is asserted. |
| capacity_and_downstream_scope | Pass: the construction is an equality, saves no power, and leaves (4.1), the hard and unbalanced children, M9-M2, endpoint uniformity, M9, and every exponent claim open. |

## 6. Dependencies and exact artifacts used

Only the task brief and selected context were used:

- protocol.md;
- state/proof_obligations.yml at the starting SHA-256 above;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/briefs/literal_atom_dictionary_constructor.md;
- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/derivation_packet.md;
- rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/candidates/conductor_literal_atom_dictionary.md;
- rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md;
- rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md;
- rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md;
- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/reports/m2_outside_packet_assembly_attack.md;
- rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/synthesis.md.

The logical inputs are the accepted dyadic profile, Vaaler coefficient
normalization, smooth Poisson/stationary transform, preliminary
square/near-square/high-gcd bounds, and Round-112 normalization and owner
guardrails.  No web source, sibling Round-113 report, strategy file,
computation, or unlisted derivation was used.

## 7. Recommended state effect

After independent and hostile seam validation, promote a scoped literal
atom-dictionary connector implementing (2.1)--(2.25).  It should record
the two exact telescopes, finite residual and ratio conventions, real
positive-quadrant amplitude, actual coefficient, exact gcd bottom and
boundary identities, quarter-packet sign and conjugacy, uniform
seminorms, and complete physical correction equality.

Revise the conductor candidate rather than promoting (113.C28) verbatim:
its low-gcd formula is correct, but it does not itself display the
high-gcd and transform-error terms in the physical one-count theorem.

Retain (4.1) and M9-M2-smooth-balanced-quarter-packet-estimate as open.
Make no change to the hard or unbalanced children, M9-M2, M9-M1,
endpoint uniformity, M9, the conditional bridge, the Gauss-circle target,
or any global exponent.  This report closes only a
definition-and-normalization seam.

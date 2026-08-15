# Hostile audit of the \(M=1\) boundary Cauchy reduction

## 1. Result

The finite Cauchy collapse is valid only with **both crossed residues
subtracted**. It returns the terminal-plus-side endpoint operator to the
original \(a_z\) coefficient on the right line, but it also leaves a
nonlocal artificial-pole value
\[
F_z(3/4+v/2)
=\zeta(3/4+u/2+v)L(3/4-u/2,\chi_4).
\]
On the actual small positive outside lines this value has no absolutely
convergent divisor expansion and is not an accepted physical endpoint
term. Thus the finite identity is promotable, but no cancellation or
target-sized estimate is.

## 2. Exact statement and hypotheses

Fix \(u,v\), put \(z=u+v\), and assume the two distinct poles
\[
w_e=\frac34+\frac v2,\qquad w_a=1-\frac z2,\qquad
\delta=w_a-w_e=\frac14-\frac u2-v
\]
lie strictly inside the Round-19 \(w\)-rectangle. Let
\[
E_v(w)=\frac{N^{w-w_e}e(\sqrt{XN})-e(\sqrt X)}{w-w_e},
\quad \epsilon_N=1,\quad\epsilon_1=-1,\quad
e_x=e(\sqrt{Xx}).
\]
For
\[
\mathcal P_{x,S}:=\frac1{2\pi i}\int_{c-iS}^{c+iS}
\frac{x^{w-w_e}F_z(w)}{w-w_e}\,dw ,
\]
the exact fixed-\((u,v)\) endpoint operator is
\[
\boxed{\;
\mathfrak E_1(u,v)
=\sum_{x\in\{1,N\}}\epsilon_xe_x
\left\{\mathcal P_{x,S}-F_z(w_e)
-\frac{x^\delta}{\delta}L(1-z,\chi_4)\right\}. \;} \tag{1}
\]
The actual outside multiplier \(\sum_j\mathcal A_j(u,v)\), its finite
\(u,v\) segments, floors, and profiles multiply (1) unchanged.

## 3. Proof or derivation

For \(f(w)=E_v(w)F_z(w)\), the accepted side orientations are
\[
\lambda+iS\to c+iS,\qquad c-iS\to\lambda-iS.
\]
The positively oriented rectangle therefore gives
\[
I_c(f)-I_\lambda(f)-S(f)
=\operatorname{Res}_{w_a}f+\operatorname{Res}_{w_e}f.
\]
Consequently
\[
T(E_1)+S(E_1)=I_c(E_1F_z)
-\operatorname{Res}_{w_a}(E_1F_z)
-\operatorname{Res}_{w_e}(E_1F_z), \tag{2}
\]
which proves (1), because
\[
\operatorname{Res}_{w_e}(E_1F_z)
=(e_N-e_1)F_z(w_e),
\]
\[
\operatorname{Res}_{w_a}(E_1F_z)
=\sum_x\epsilon_xe_x\,\frac{x^\delta}{\delta}
L(1-z,\chi_4).
\]
Thus a plus sign on either residue, or an upper-plus-lower common
orientation, is false.

On the right line \(F_z\) expands absolutely:
\[
\mathcal P_{x,S}
=\sum_{n\ge1}a_z(n)n^{-w_e}
P_{d,S,\nu}(x/n),
\]
\[
a_z(n)=\sum_{hq=n}\chi_4(q)(q/h)^{z/2},\qquad
P_{d,S,\nu}(y)=\frac1{2\pi i}
\int_{d-i(S+\nu/2)}^{d+i(S-\nu/2)}\frac{y^r}{r}\,dr,
\tag{3}
\]
where \(v=b+i\nu\) and \(d=c-\Re w_e>0\). The finite Perron segment is
off-centre whenever \(\nu\ne0\). Formula (3) recovers the original
\(a_z\), not the reflected \(a_{-z}\), but \(F_z(w_e)\) cannot be
subtracted termwise from (3): its Dirichlet series is outside absolute
convergence. Hence (1) is not a finite Dirichlet polynomial or an
ordinary complementary tail.

In terminal variables the artificial pole is
\(s_e=1-w_e=1/4-v/2\). Since
\(\operatorname{Res}_{s=s_e}E_v(1-s)=-(e_N-e_1)\), its sign reverses.
The intact functional equation gives
\[
K_z(1-s_e)F_{-z}(s_e)=F_z(w_e)
\]
meromorphically. Expanding the dual series at \(\Re s_e\approx1/4\), or
counting separate gamma residues, is invalid.

Endpoint coefficients in \(E_v\) have full weight. Stars enter only after
a symmetric infinite inverse Mellin limit; they alter neither (1) nor
(2). If \(\delta=0\), \(w_a=w_e\) and \(E_vF_z\) has a double pole.
Then the two displayed simple residues must be replaced by its single
derivative residue; (1) is not valid termwise.

## 4. First doubtful or unproved step

The first missing step is a signed estimate for (1) after the actual
\(u,v\) integrations. In particular, no accepted result controls the
critical nonlocal value \(F_z(w_e)\) through the hard \(1/u\) maximal
measure. Finite Cauchy algebra alone supplies no magnitude saving.

## 5. Required controls and outcomes

For the model \(f(w)=1/(w-w_e)\), (2) reads
\(I_\lambda+S=I_c-1\): this exactly rejects a plus artificial residue.
With \(\nu=0\),
\[
P_{d,S,0}(1)=\frac1\pi\arctan(S/d)\ne\frac12
\]
at every finite \(S\), rejecting insertion of the endpoint star before
the limit. Finally, \(z=v=0\) leaves the nonlocal factor
\(\zeta(3/4)L(3/4,\chi_4)\), so the collapsed lower endpoint cannot be
identified merely with the \(n=1\) half-weight.

## 6. Dependencies and exact artifacts used

Used protocol.md, the proof graph and active campaign, the Round-19
finite vector identity, all completed Round-21 reports and synthesis, and
the assigned Round-22 brief. No other Round-22 report, external source, or
infinite-height argument was used.

## 7. Recommended state effect

Promote the finite identity (1), the minus-residue and side-orientation
ledger, the off-centred finite Perron formula (3), and the pole-collision
exception. Reject half weights at finite height, termwise conversion to a
complementary divisor tail, dual-series evaluation at \(s_e\), and any
boundary estimate inferred from Cauchy algebra. Retain the endpoint
boundary operator and all downstream obligations as open.

## Addendum: physical endpoint normalization

Even granting
\[
C_N\ll N_X^{1/4}\log^2X\asymp X^{1/8}\log^2X,
\]
this is **not sufficient** in GAR normalization. Round 14 places the
radial expression inside
\[
-\frac4\pi X^{1/4}\Re\{e(1/8)(\cdots)\}.
\]
The claimed bound therefore yields only
\[
X^{1/4}C_N\ll X^{3/8}\log^2X,
\]
which is larger than \(X^{1/4+\varepsilon}\) for every fixed
\(\varepsilon<1/8\). A separately bounded normalized endpoint must be
\(O_\varepsilon(X^\varepsilon)\), unless its cancellation with other
terms is proved before taking absolute values. If \(C_N\) were defined
*after* including the external \(X^{1/4}\), that different convention
would have to be stated; the displayed \(N_X^{1/4}=X^{1/8}\) estimate is
plainly the inner GAR scale.

Support supplies no hidden saving. At finite \(S\),
\(P_{d,S,\nu}(N_X/n)\) in (3) is nonzero for every \(n\); there is no
sharp support. Its symmetric infinite limit would select the full prefix
\(n<N_X\) plus the half tie, not a thin endpoint set. The standard
absolute mass
\(\sum_{n\le N_X}d(n)n^{-3/4}\asymp
N_X^{1/4}\log N_X\) is precisely the obstructive size. Only the isolated
tie \(n=N_X\) is small, and the finite Cauchy operator is not that tie.

There is one exact residue cancellation, but it is narrower. Combining
the unsplit arithmetic residue with (1) gives
\[
\mathfrak R^{\rm ar}[G]-\mathfrak R^{\rm ar}[E_1]
=\mathfrak R^{\rm ar}[R_1].
\]
Thus the explicit
\(x^\delta L(1-z,\chi_4)/\delta\) part of (1) cancels its \(E_1\)-share
of the original arithmetic residue. It does **not** cancel
\(\mathcal P_{N_X,S}-F_z(w_e)\), nor does it turn that term into a
target-sized boundary. Counting the cancelled arithmetic piece as either
a saving or an additional error would double-count the ledger.

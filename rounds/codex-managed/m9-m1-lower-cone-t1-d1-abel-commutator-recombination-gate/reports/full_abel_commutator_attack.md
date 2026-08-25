# Round 159 discovery report: full Abel commutator attack

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Task: `full_abel_commutator_attack`
- Role: discovery
- Graph SHA-256: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Allocation actually used: 100% analytic/algebraic, 0% numerical
- Terminal recommendation: `paired_interior_abel_commutator_no_go` in the route-scoped sense stated below

## 1. Result: exact reconstruction and a scoped Fourier no-go

There are three logically different conclusions.

1. **Finite Abel reconstruction.**  On each of the two literal signed
   blocks, and separately for every odd \(d\mid N\) and every
   \(v\bmod H\), the positive right outer endpoint, positive moving
   atom, positive coefficient-difference remainder, negative left
   outer endpoint, negative moving atom, and negative
   coefficient-difference remainder reconstruct
   \(\sum_j\widehat B_j(2dv)K(-v^2,-j;c)\) exactly.  No endpoint,
   transition, or profile term is estimated in this assertion.

2. **Full-frequency physical identity.**  After that finite
   reconstruction, completing \(v\bmod H\) and recombining all odd
   divisors gives the already accepted physical row
   \[
     \mathcal S_U(V)=
     \sum_{V<|j|\le 2V}\sum_{x\bmod 4N}
       B_j(x)G_N(x^2-j).
     \tag{159.D1}
   \]
   The paired-interior matrix is exactly
   \[
     \mathcal T_{\mathrm{int},U}(V)
       =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),
     \tag{159.D2}
   \]
   where \(\mathcal Z_U\) and \(\mathcal F_U\) are the whole \(v=0\)
   and whole Nyquist rows.  They are subtracted once, not once per Abel
   piece and not in addition to the isolated trace rows of Round 158.

3. **Selected-coordinate compression.**  The physical row (159.D1)
   has the exact reparametrization
   \[
   \boxed{
     \mathcal S_U(V)=
       \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
       \mathbf 1_{\{V<|r(\ell)|\le2V\}},
     \qquad
     r(\ell)=\kappa(\ell)^2-N\ell,
   }
   \tag{159.D3}
   \]
   with
   \(\kappa(\ell)=\lfloor\sqrt{N\ell}+1/2\rfloor\).
   This is not a new inversion theorem or a new estimate: it is the
   nearest-cell reparametrization of the accepted Round-157 physical
   row after the six Abel lines have been put back together.  What it
   newly makes transparent is that the *full* row has the quotient
   profile \(w_U(\ell)\); it does not alter the accepted Round-158
   statement that the isolated moving trace has the two different
   boundary profiles \(W_+\) and \(W_-\).

The analytic target is not proved.  If
\(w_U=M^{-3/4}\widetilde w_U\), it is
\[
  \left|\mathcal R_U(V)\right|
  :=\left|\sum_{\ell\ge1}\chi_4(\ell)\widetilde w_U(\ell)
       e(\sqrt{N\ell})
       \mathbf 1_{\{V<|r(\ell)|\le2V\}}\right|
  \ll_\varepsilon M^{3/4}X^\varepsilon.
  \tag{159.D4}
\]
The common profile does not imply (159.D4).  A literal
variable-boundary Fourier/Vaaler attack, even with the favorable
second-derivative treatment of every nonexceptional mode, has raw
capacity
\[
  X^\varepsilon\left(
       \frac{M}{Q}+\sqrt{KQ}+\frac{M}{\sqrt K}+1
     \right),
  \qquad K=\sqrt{NM},
  \tag{159.D5}
\]
at Fourier height \(Q\ge1\).  Optimizing the first two terms gives
\[
  X^\varepsilon\left(M^{1/3}K^{1/3}+\frac{M}{\sqrt K}+1\right)
  \tag{159.D6}
\]
when the optimizer is at least one, and only the trivial \(O(M)\)
capacity otherwise.  The leading term in (159.D6) is at most the raw
target \(M^{3/4}\) only if
\[
  K\le M^{5/4},\qquad\text{equivalently}\qquad M\ge N^{2/3}.
  \tag{159.D7}
\]
This is disjoint from the frozen unbounded range \(M\le N^{1/2}\),
and a fortiori gives no new range on the currently open side
\(M^{449}\ll R^{780}\), \(R=X^{1/4}\), \(N=\lfloor X\rfloor\).
Equation (159.D6) is an upper-capacity ledger for this named method,
not a signed lower bound and not a universal impossibility theorem.

Thus the successful result is: exact six-line reconstruction and exact
common-profile reparametrization, followed by the first quantitative
obstruction at the sharp variable-band Fourier truncation/boundary
interface.  No strict owner-complete positive-power range beyond the
accepted fixed-polylogarithmic collar is obtained.

## 2. Exact statement and hypotheses

Fix \(A>0\) and
\[
  q=4N,\qquad K=\sqrt{NM},\qquad
  M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
  \tag{159.D8}
\]
Write
\[
  a=\lfloor V\rfloor+1,\qquad b=\lfloor2V\rfloor,
  \qquad J_+=[a,b]\cap\mathbb Z,
  \qquad J_-=[-b,-a]\cap\mathbb Z.
  \tag{159.D9}
\]
This is exactly the half-open hard dyadic convention
\(V<|j|\le2V\).  Empty and singleton blocks are allowed.

For every odd \(d\mid N\), put
\[
  c=\frac{q}{d},\qquad H=\frac c2,\qquad n=\frac H2=\frac Nd.
  \tag{159.D10}
\]
For \(j\in J_\sigma\), write the literal coefficient as
\[
  B_j(x)=\mathbf1_{x\ge\lambda_\sigma(j)}F_j(x),
  \qquad \lambda_+(j)=j+1,\qquad \lambda_-(j)=-j,
  \tag{159.D11}
\]
where \(F_j\) is the inherited zero-extended nonmoving factor
\[
  F_j(x)=w_U\!\left(\frac{x^2-j}{N}\right)
          e(\sqrt{x^2-j}-x)
  \tag{159.D12}
\]
on its literal physical components and is zero elsewhere.  Thus all
profile edges, phase changes, component transitions, physical-lift
choices, and hard endpoints are part of \(F_j\); no smooth surrogate
is introduced.  On the relevant sign block (159.D11) is exactly the
original mask
\(\mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}\).

Set
\[
  A_j(v)=\widehat B_j(2dv)
     =\sum_{x\bmod q}B_j(x)e_c(-2vx),
  \qquad K_{d,v}(s)=K(-v^2,-s;c),
  \tag{159.D13}
\]
and define the literal prefix and suffix
\[
  P^+_{d,v}(j)=\sum_{s=a}^{j}K_{d,v}(s),
  \qquad
  P^-_{d,v}(j)=\sum_{s=j}^{-a}K_{d,v}(s).
  \tag{159.D14}
\]
Then the six lines are
\[
\begin{aligned}
 \sum_{j=a}^{b}A_j(v)K_{d,v}(j)
 ={}&\underbrace{A_b(v)P^+_{d,v}(b)}_{\mathrm{P\!\!-outer}}\\
 &+\underbrace{\sum_{j=a}^{b-1}F_j(j+1)e_c(-2v(j+1))
       P^+_{d,v}(j)}_{\mathrm{P\!\!-moving}}\\
 &-\underbrace{\sum_{j=a}^{b-1}P^+_{d,v}(j)
       \sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx)}_
       {\mathrm{P\!\!-difference}},
\end{aligned}
\tag{159.D15}
\]
and
\[
\begin{aligned}
 \sum_{j=-b}^{-a}A_j(v)K_{d,v}(j)
 ={}&\underbrace{A_{-b}(v)P^-_{d,v}(-b)}_{\mathrm{N\!\!-outer}}\\
 &+\underbrace{\sum_{j=-b+1}^{-a}F_j(-j)e_c(2vj)
       P^-_{d,v}(j)}_{\mathrm{N\!\!-moving}}\\
 &+\underbrace{\sum_{j=-b+1}^{-a}P^-_{d,v}(j)
       \sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx)}_
       {\mathrm{N\!\!-difference}}.
\end{aligned}
\tag{159.D16}
\]
The signs in (159.D15)--(159.D16), including the positive moving atom
on both blocks, are part of the statement.

Let
\[
  \mathcal V_d^\circ=\{v\bmod H:v\ne0,n\}.
  \tag{159.D17}
\]
Both members of every complementary pair \(\{v,H-v\}\) are retained;
there is no conjugacy shortcut because \(B_j\) is complex.  When
\(c=4\), \(H=2\) and (159.D17) is empty, as it must be.

Finally, the exact analytic object is (159.D4), with the full quotient
profile satisfying
\[
  \|\widetilde w_U\|_\infty+
  \operatorname{Var}(\widetilde w_U)\ll_\varepsilon X^\varepsilon
  \tag{159.D18}
\]
after retaining the inherited finite component decomposition and zero
extension.  No coefficient-uniform theorem beyond this actual profile
is asserted.

## 3. Proof and derivation

### 3.1 Literal mask differences

On \(J_+\),
\[
\begin{aligned}
 A_{j+1}(v)
 &=\sum_{x\ge j+2}F_{j+1}(x)e_c(-2vx),\\
 A_j(v)
 &=F_j(j+1)e_c(-2v(j+1))
   +\sum_{x\ge j+2}F_j(x)e_c(-2vx).
\end{aligned}
\]
Therefore
\[
 A_{j+1}(v)-A_j(v)
 =-F_j(j+1)e_c(-2v(j+1))
  +\sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx).
 \tag{159.D19}
\]
On \(J_-\), advancing \(j\) lowers the moving boundary from
\(-j+1\) to \(-j\), so
\[
 A_j(v)-A_{j-1}(v)
 =F_j(-j)e_c(2vj)
  +\sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx).
 \tag{159.D20}
\]
Because every \(F_j\) is zero-extended, (159.D19)--(159.D20) include
every component birth, death, overlap transition, profile change, and
phase change.  Calling the last terms merely “profile derivatives”
would be weaker than the literal identities.

### 3.2 Abel summation and finite reconstruction

The prefix identity is
\[
 \sum_{j=a}^{b}A_jK_j
  =A_bP_b^++\sum_{j=a}^{b-1}(A_j-A_{j+1})P_j^+.
 \tag{159.D21}
\]
Substitution of (159.D19) is exactly (159.D15).  The suffix identity is
\[
 \sum_{j=-b}^{-a}A_jK_j
  =A_{-b}P_{-b}^-+
    \sum_{j=-b+1}^{-a}(A_j-A_{j-1})P_j^-,
 \tag{159.D22}
\]
and substitution of (159.D20) is (159.D16).

For a direct reconstruction check, the coefficient of \(K_{d,v}(s)\)
on the right of (159.D21) is
\[
 A_b+\sum_{j=s}^{b-1}(A_j-A_{j+1})=A_s,
\]
and the coefficient on the right of (159.D22) is
\[
 A_{-b}+\sum_{j=-b+1}^{s}(A_j-A_{j-1})=A_s.
\]
Thus all three positive lines and all three negative lines reconstruct
the original matrix separately for every \((d,v)\).  This also proves
the hard endpoint cases: for a singleton block only the appropriate
outer line remains.

### 3.3 Complete frequency normalization and subtraction exactly once

The accepted half-period inverse identity is
\[
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =\frac{1-i}{2}\sqrt c
   \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
 \tag{159.D23}
\]
Multiplying by the exterior factor gives
\[
 -\frac{i(1+i)}{2Nq}\,\chi_4(d)d\sqrt c
 \cdot\frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\chi_4(d),
 \tag{159.D24}
\]
because \(dc=q\).  The map \(h=du\pmod q\) partitions the odd
residues modulo \(q\): its inverse is
\(d=(h,N)\), \(u=h/d\), and
\(\chi_4(d)\chi_4(u)=\chi_4(h)\).  Hence the all-\(d\) sum is
\[
 -\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ {\mathrm{odd}}}}
    \chi_4(h)e_{4N}(h(x^2-s))
 =G_N(x^2-s).
 \tag{159.D25}
\]
Indeed, the sum in (159.D25) vanishes unless \(N\mid x^2-s\); when
\(x^2-s=N\ell\), its two mod-four terms give precisely
\(\chi_4(\ell)\).  This proves (159.D1) for arbitrary \(N\), every odd
\(d\mid N\), both complementary representatives, and \(c=4\).

For each \(d\), the complete set \(v\bmod H\) is the disjoint union
of \(v=0\), \(v=n=H/2\), and (159.D17).  Therefore (159.D2) is an
exact set subtraction.  The accepted whole-row estimates are
\[
  |\mathcal Z_U(V)|+|\mathcal F_U(V)|
  \ll_\varepsilon M^{-1/4}X^\varepsilon.
  \tag{159.D26}
\]
The Round-158 quantities \(\mathcal Z_{\mathrm{tr}}\) and
\(\mathcal F_{\mathrm{tr}}\) were special-frequency pieces of the isolated
moving line.  They are not extra terms in (159.D2).  Recombination
first and subtraction of the two *whole* rows once is the only correct
normalization.

### 3.4 Physical lift, nearest cell, quotient profile, and integral phase

If a term in (159.D1) is nonzero, write
\[
  x^2-j=N\ell.
  \tag{159.D27}
\]
The literal cell is equivalent to
\[
  x^2-x+1\le N\ell\le x^2+x.
  \tag{159.D28}
\]
The integer intervals
\[
  I_x=[x^2-x+1,x^2+x]\cap\mathbb Z,
  \qquad x\ge1,
  \tag{159.D29}
\]
partition the positive integers, since the upper endpoint of \(I_x\)
is \(x^2+x\) and the lower endpoint of \(I_{x+1}\) is
\(x^2+x+1\).  Moreover
\[
  N\ell\in I_x
  \quad\Longleftrightarrow\quad
  x=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor.
  \tag{159.D30}
\]
Thus \(x=\kappa(\ell)\) and \(j=r(\ell)\) uniquely.

There is also no hidden residue-lift multiplicity.  On the inherited
dyadic support, (159.D27) and \(|j|\le2K\) give \(x\asymp K\).  Since
the quotient support has fixed dyadic constants and
\(K\le N^{3/4}=o(N)\), the accepted physical hull has length
\(O(K)<N\), and \(2\kappa(\ell)<N\), for all sufficiently large
parameters; the finitely many small cases are absorbed in the uniform
constant.  In particular the hull is much shorter than \(q=4N\), so
one residue class contains at most one physical lift and no selected
cell wraps into another lift.  This is exactly the unique nonwrapping
physical-lift hypothesis attached to the accepted Round-157
coefficient.  It licenses the all-\(\ell\) formula (159.D3) in the
actual campaign because \(w_U(\ell)\ne0\) already confines \(\ell\)
to that fixed dilation of \(M\).

If one were given only a statement that said “\(x\bmod4N\)” but
omitted the nonwrapping physical hull, then the right side of
(159.D3) would require an additional physical-lift indicator (or a
lift-multiplicity function), and the displayed all-\(\ell\) formula
would be conditional.  That omission occurs in the statement-only
packet noted by the blind rederivation; it is not an omission in the
actual-project coefficient and therefore does not invalidate
(159.D3) here.

At the selected point,
\[
 w_U\!\left(\frac{x^2-j}{N}\right)=w_U(\ell),
 \qquad
 e(\sqrt{x^2-j}-x)
   =e(\sqrt{N\ell}-\kappa(\ell))
   =e(\sqrt{N\ell}),
 \tag{159.D31}
\]
where the last equality uses only the integrality of
\(\kappa(\ell)\).  Also \(G_N(x^2-j)=\chi_4(\ell)\), including the
vanishing of even \(\ell\).  Equations (159.D27)--(159.D31) prove
(159.D3) bijectively.

This explains exactly why the quotient profile returns only after all
six Abel lines are recombined.  At the isolated positive moving atom
one instead has
\(w_U((k^2-k+1)/N)\), and at the isolated negative moving atom one has
\(w_U((k^2+k)/N)\).  The difference and outer lines restore the
quotient value; they do not retroactively identify those two boundary
profiles.

### 3.5 Exact variable residual band

Put
\[
  y=\sqrt{N\ell},\qquad
  \delta(\ell)=y-\kappa(\ell)\in[-1/2,1/2).
\]
Then, exactly,
\[
  r(\ell)=-\delta(\ell)(2\kappa(\ell)+\delta(\ell)).
  \tag{159.D32}
\]
No constant-width fractional interval is equal to the mask in
(159.D3).  More explicitly, for \(a>0\) define
\[
  p_a(y)=\sqrt{y^2+a}-y,
  \qquad
  n_a(y)=y-\sqrt{y^2-a}.
  \tag{159.D33}
\]
The positive-defect portion is
\[
  p_V(y)<-\delta\le p_{2V}(y),
  \tag{159.D34}
\]
and the negative-defect portion is
\[
  n_V(y)<\delta\le n_{2V}(y).
  \tag{159.D35}
\]
Both are intersected with the literal centered cell
\([-1/2,1/2)\); if an upper endpoint in (159.D34) or (159.D35)
exceeds \(1/2\), it is clipped there with the inherited half-open
choice.  This clipping is needed when \(V\) is comparable with \(K\).
The hard dyadic choices \(V<|r|\) and \(|r|\le2V\) determine the strict
and closed sides in (159.D34)--(159.D35).

On each fixed physical support component one has \(y\asymp K\) and
the total excursion of \(y\) is \(O(K)\).  Uniformly for
\(a\in\{V,2V\}\), \(0<a\le 2K\), and sufficiently large \(K\),
\[
  p_a(y),n_a(y)\asymp \frac aK,
  \qquad
  |p_a'(y)|=\frac{p_a(y)}{\sqrt{y^2+a}}\ll\frac a{K^2},
  \qquad
  |n_a'(y)|=\frac{n_a(y)}{\sqrt{y^2-a}}\ll\frac a{K^2}.
\]
(Here \(y^2-a>0\) follows from \(y\asymp K\) and \(a\le2K\);
the bounded values of \(K\) are harmless.)  Since there are only
finitely many support components, this gives
\[
  \operatorname{Var}_{\ell\asymp M}p_a(y(\ell))
   +\operatorname{Var}_{\ell\asymp M}n_a(y(\ell))
  \ll \frac aK.
  \tag{159.D36}
\]
Clipping either endpoint at \(1/2\) does not increase its total
variation.  All constants here depend at most on the fixed support
dilation, so (159.D36) is uniform in the two dyadic endpoint choices.
Small total variation does not permit replacing them by constants:
the mask is sharp, and a displacement of one sampled point changes a
raw summand of unit size.

### 3.6 Fourier modes, the shifted zero mode, and the truncation obstruction

For a fixed \(y\), let \(m_V(y,t)\) be the two clipped interval
indicator described by (159.D34)--(159.D35), periodically extended in
the centered variable \(t\).  Its formal Fourier coefficients are
\[
  c_h(y)=\int_{-1/2}^{1/2}m_V(y,t)e(-ht)\,dt.
  \tag{159.D37}
\]
Away from a boundary,
\(m_V(y,\delta)=\sum_hc_h(y)e(h\delta)\), and
\(e(h\delta)=e(hy)\) because \(\kappa\) is integral.  After multiplying
by the built-in \(e(y)\), mode \(h\) has square-root frequency \(h+1\).

The exceptional shifted zero mode is \(h=-1\), not an untwisted
constant sum: it remains multiplied by \(\chi_4(\ell)\).  Since
\[
  \chi_4(\ell)=\frac{e(\ell/4)-e(-\ell/4)}{2i}
  \tag{159.D38}
\]
and its partial sums are bounded, discrete Abel summation with
(159.D18), (159.D36), and the finitely many clipping transitions gives
\[
  \sum_{\ell}\chi_4(\ell)\widetilde w_U(\ell)c_{-1}(y(\ell))
  \ll_\varepsilon X^\varepsilon.
  \tag{159.D39}
\]
Thus the shifted zero mode is safe and even \(\ell\) have not been
silently inserted.

The average mode \(h=0\) has coefficient \(c_0(y)\) equal to the
total variable-band length.  It has bounded variation and size
\(O(\min(1,V/K))\).  Applying the same second-derivative estimate to
its remaining phase \(e(\sqrt{N\ell})\), after the two linear
\(\chi_4\)-twists, costs at most
\[
  \ll_\varepsilon X^\varepsilon
  \left(\sqrt K+\frac{M}{\sqrt K}\right),
  \tag{159.D39a}
\]
which is contained in (159.D43) for \(Q\ge1\).

For \(h\ne0\), writing an interval coefficient by its two endpoints
shows why the endpoint motion cannot be discarded.  Multiplication by
\(e((h+1)y)\) produces boundary phases of the form
\[
  e\!\left(\sqrt{N\ell}
       +h\sqrt{N\ell\pm a}\right),
  \qquad a\in\{V,2V\},
  \tag{159.D40}
\]
up to the linear twists \(e(\pm\ell/4)\) from (159.D38) and the fixed
half-cell clipping phases.  For \(h\ne-1\), their second derivatives
on \(\ell\asymp M\) have size
\[
  \asymp \frac{|h+1|K}{M^2},
  \tag{159.D41}
\]
uniformly for \(a\le2V\le2K\) once \(K\) is sufficiently large.
Indeed, if \(y=\sqrt{N\ell}\) and
\(\sigma\in\{+1,-1\}\), then
\[
 \left(\sqrt{N\ell+\sigma a}\right)''
 =-\frac{N^2}{4(N\ell+\sigma a)^{3/2}}
 =y''\left(1+O\!\left(\frac a{K^2}\right)\right).
\]
Thus the second derivative of (159.D40) is
\(y''[1+h(1+O(1/K))]\).  For every integer \(h\ne-1\) this has
absolute size \(\asymp |h+1||y''|\), uniformly also for negative
\(h\le-2\); the linear \(\chi_4\)-twists do not alter it.  The
standard second-derivative bound,
followed by Abel transfer of (159.D18), is therefore
\[
  \ll_\varepsilon X^\varepsilon
  \left(\sqrt{|h+1|K}
       +\frac{M}{\sqrt{|h+1|K}}\right).
  \tag{159.D42}
\]
Since an interval endpoint has Fourier coefficient \(O(1/|h|)\), the
nonexceptional modes through height \(Q\) cost
\[
\begin{aligned}
 &\sum_{\substack{1\le |h|\le Q\\h\ne-1}}\frac1{|h|}
  \left(\sqrt{|h+1|K}
       +\frac{M}{\sqrt{|h+1|K}}\right) \\
 &\quad\ll
 \sqrt K\sum_{\substack{1\le |h|\le Q\\h\ne-1}}
       \frac{\sqrt{|h+1|}}{|h|}
 +\frac M{\sqrt K}
  \sum_{\substack{1\le |h|\le Q\\h\ne-1}}
       \frac1{|h|\sqrt{|h+1|}} \\
 &\quad\ll \sqrt{KQ}+\frac M{\sqrt K}.
 \tag{159.D42a}
\end{aligned}
\]
The first scalar sum is \(O(\sqrt Q)\), while the second is
\(O(1)\); this includes both signs of \(h\).  The omitted \(h=-1\)
mode is (159.D39), and the average \(h=0\) mode is (159.D39a).
Consequently the nonexceptional modes through height \(Q\) cost
\[
  \ll_\varepsilon X^\varepsilon
  \left(\sqrt{KQ}+\frac{M}{\sqrt K}\right).
  \tag{159.D43}
\]

A sharp finite expansion also has a boundary remainder.  The four
moving boundaries are precisely the near-integrality loci
\[
  \sqrt{N\ell+a}\ \text{ near an integer}
  \quad\text{or}\quad
  \sqrt{N\ell-a}\ \text{ near an integer},
  \qquad a\in\{V,2V\}.
  \tag{159.D44}
\]
Claiming an \(O(M/Q)\) error without controlling (159.D44) is the first
invalid fixed-band shortcut.  Erdős--Turán/Vaaler at height \(Q\),
with
\[
  \left(\sqrt{N\ell\pm a}\right)''
    \asymp-\frac K{M^2},
  \tag{159.D45}
\]
has the explicit ledger
\[
 \frac{M}{Q}
 {}+\sum_{1\le h\le Q}\frac1h
 \left|\sum_{\ell\asymp M}
   e\!\left(h\sqrt{N\ell\pm a}\right)\right|.
 \tag{159.D45a}
\]
Using
\[
 \left|\sum_{\ell\asymp M}
   e\!\left(h\sqrt{N\ell\pm a}\right)\right|
 \ll \sqrt{hK}+\frac{M}{\sqrt{hK}}
 \tag{159.D45b}
\]
in (159.D45a) gives, including harmless logarithms,
\[
  \text{boundary/truncation capacity}
  \ll_\varepsilon X^\varepsilon
   \left(\frac M Q+\sqrt{KQ}+\frac M{\sqrt K}\right).
  \tag{159.D46}
\]
At exact equality \(r=\pm V,\pm2V\), the Fourier series supplies
half-weights; the correction dictated by the strict/closed convention
is part of (159.D44) and cannot be deleted.  Combining
(159.D39), (159.D43), and (159.D46) proves the capacity ledger
(159.D5)--(159.D7).

This calculation is deliberately favorable: it already grants
componentwise BV transfer and treats every nonexceptional phase by a
clean second-derivative estimate.  It nevertheless has no target range
inside \(M\le N^{1/2}\).  A stronger signed theorem coupling
\(\chi_4\), the actual quotient profile, and all four variable
boundaries could still beat this capacity; none is proved here.

### 3.7 Restored scale and the collar

The selected support bound is unsigned:
\[
  L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
  \tag{159.D47}
\]
Consequently absolute summation gives only
\[
  |\mathcal S_U(V)|
  \ll_\varepsilon
  M^{-3/4}\min(M,V)X^\varepsilon.
  \tag{159.D48}
\]
It is target-sized in the already accepted fixed-polylogarithmic
collar \(V\le M^{3/4}(\log(2X))^{O(1)}\), after absorbing logarithms
into \(X^\varepsilon\).  At
\(V\ge M^{3/4+\eta}\) with \(V\le M\), (159.D48) loses \(M^\eta\);
for \(V\ge M\) it loses \(M^{1/4}\).  These are upper capacities, not
lower bounds for the signed sum.  The atom scale \(M^{-3/4}\) must be
restored before comparing with the scalar target, and the external
\(B_{1,U}(1)\) factor remains a separate assembly seam.

## 4. First doubtful or unproved step

There is no doubtful step in the finite differences, the six Abel
lines, their telescoping reconstruction, the all-\(d\) complete
frequency normalization, the one-time whole-row subtraction, the
physical-lift uniqueness, the nearest-cell bijection, the quotient
profile, the integral phase shift, or the exact variable-band formula
under the printed hypotheses.

The first unproved mathematical statement is exactly (159.D4).  In a
Fourier implementation, the first unsupported replacement would be to
turn (159.D34)--(159.D35) into a fixed fractional interval or to assign
the truncation error \(O(M/Q)\) without the four moving near-integrality
problems (159.D44).  Retaining them gives (159.D46), whose optimized
capacity requires \(M\ge N^{2/3}\) and hence supplies no frozen-range
or open-side gain.  The common profile and the harmless shifted zero
mode do not control the remaining nonexceptional modes or the sharp
boundary remainder.

## 5. Required controls and outcomes

- `literal_full_Abel_six_line_package`: **GREEN.**  Equations
  (159.D15)--(159.D16) print all six lines literally.
- `positive_negative_signs_and_outer_endpoints`: **GREEN.**  The
  positive outer endpoint is \(A_bP_b^+\), the negative outer endpoint
  is \(A_{-b}P_{-b}^-\), and both moving atoms have positive sign.
- `profile_difference_and_transition_reconstruction`: **GREEN.**  The
  zero-extended differences in (159.D19)--(159.D20) retain profiles,
  phases, component transitions, and all endpoint births and deaths.
- `all_d_all_v_complete_frequency_normalization`: **GREEN.**  The
  constant (159.D24), the \(h=du\) partition, complementary
  representatives, arbitrary \(N\), and \(c=4\) are retained.
- `zero_and_Nyquist_whole_row_subtraction`: **GREEN.**  Equation
  (159.D2) subtracts the two whole rows exactly once; isolated-trace
  special rows are not subtracted again.
- `physical_lift_and_nearest_cell_uniqueness`: **GREEN.**  The physical
  hull is \(O(K)<N\), \(2\kappa<N\), and hence nonwrapping modulo
  \(4N\); (159.D29) is an exact partition.  The blind statement-only
  omission would require an extra indicator, but the accepted project
  hypothesis licenses (159.D3).
- `quotient_profile_not_boundary_profile`: **GREEN.**  The full row has
  \(w_U(\ell)\); the isolated \(W_+\) and \(W_-\) statements are left
  unchanged.
- `integral_phase_shift`: **GREEN.**  Equation (159.D31) uses only
  \(\kappa(\ell)\in\mathbb Z\).
- `variable_residual_band`: **GREEN algebraically / OPEN analytically.**
  Equations (159.D32)--(159.D35) retain both signs, moving endpoints,
  clipping, strict lower dyadic edge, and closed upper edge.
- `chi4_shifted_zero_mode`: **GREEN.**  It remains character-twisted
  and is bounded by (159.D39); it is not an untwisted \(M\)-term.
- `Fourier_truncation_and_boundary_errors`: **RED for target closure.**
  The exact boundary curves (159.D44), equality corrections, and
  capacity (159.D46) remain above target throughout the frozen range.
- `N_M_V_power_and_scalar_target`: **GREEN calibration / OPEN bound.**
  The scalar target is \(X^\varepsilon\), the raw target is
  \(M^{3/4}X^\varepsilon\), and absolute capacity is (159.D48).
- `upper_capacity_vs_signed_bound`: **GREEN.**  Equations
  (159.D5)--(159.D7) and (159.D48) are explicitly upper capacities,
  never lower bounds or universal no-go theorems.
- `external_scalar_and_downstream_scope`: **GREEN quarantine.**  The
  external scalar is not absorbed.  Nothing here transfers to
  \(D>1\), \(L>1\), generic \(t=1\), \(t\ge2\), cross, another M1 or M2
  owner, endpoint uniformity, M9, the bridge, the quarter target, or
  either global exponent.

No computation, numerical example, or web source was used.

## 6. Dependencies and exact artifacts used

The report used every permitted context artifact and no sibling
Round-159 report:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/round159_d1_abel_commutator_recombination_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/candidates/conductor_round159_common_profile_seed.md`;
7. `proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md`;
8. `proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md`; and
9. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/conductor_round158_adjudication.md`.

The accepted inputs used from them are the literal coefficient, the
complete half-period inverse-Gauss identity, the zero-row theorem, the
whole Nyquist-fold theorem, the physical support and BV bounds, and
the Round-158 sign conventions.  The Fourier capacity calculation in
Section 3.6 is self-contained and imports no external theorem beyond
the elementary second-derivative and Erdős--Turán/Vaaler inequalities
in the exact form derived there.

## 7. Recommended state effect

**Revise, without target promotion.**  Record the exact six-line
reconstruction and (159.D3) as a route-scoped common-profile
reparametrization of the already accepted physical row.  Do not call
(159.D3) a new analytic theorem, do not alter the isolated-trace
boundary-profile statement, and do not promote a strict range.  Add
the literal variable-boundary/truncation ledger (159.D32)--(159.D46)
as a scoped obstruction to the fixed-band Fourier plus ordinary
second-derivative route.  Leave the signed bound (159.D4), the full
paired-interior target, the open side \(M^{449}\ll R^{780}\), every
other owner, and all downstream obligations open.

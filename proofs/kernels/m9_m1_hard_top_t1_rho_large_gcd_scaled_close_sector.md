# Hard-M1 \(t=1\) rho-large gcd-scaled double-close sector

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Round: 193
- Starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Formal candidate SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Kernel status: durable proof artifact; graph acceptance remains controlled by
  the Round-193 State Patch
- Numerical theorem evidence: none

## 1. Statement

Fix real \(X\ge2\), one nonempty literal middle or lower residual
hard-M1 shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil L^{1/2}\rceil .
\tag{193.C1}
\]

Fix a nonempty dyadic high-height block \(Y<h\le2Y\), \(Y>Q\).
Let \(\mathscr H_Y^\sigma(W)\) denote the complete complex physical
opposing-incidence source inside the one outer real part of the accepted
Round-185 high-height residual.  Thus a live physical atom has ordered
endpoint tuple

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},\qquad
 0<r<R_0,\quad 2\mid r,
\tag{193.C2}
\]

where \(d,d'\) are the lower and upper character divisors and \(m,m'\)
are their complementary factors.  Every residual selector, squarefree
and allocation-coprimality predicate, profile, floor, star, half weight,
hard sample, crossing, endpoint trace, Fejer factor, square-root phase,
orientation, affine site, conjugation, and zero extension is part of the
physical atom \(W\).  On live support,

\[
 d,m,d',m'\asymp L,\qquad |W_x|\ll_\eta X^\eta
\tag{193.C3}
\]

for every fresh \(\eta>0\), after including the two endpoint
coefficients and all bounded scalar factors.

Retain the exact Round-192 spectral interface, using \(\mathfrak m\)
for its Fourier-lift gcd so that it cannot be confused with the physical
cofactor \(m\):

\[
 U=\mathfrak m q>4Q,\qquad q>Q,\qquad
 \mathfrak m|a|_q>Q,\qquad Q\mathfrak m<Y.
\tag{193.C3a}
\]

For \(v_0=[v]_U\in\{1,\ldots,U-1\}\), define

\[
 \rho v_0-\beta U=1,\qquad
 -{U-1\over2}\le\rho\le{U-1\over2},
\quad
 T=\min\!\left\{{U-1\over2},
        \left\lfloor{Q\mathfrak m U\over Y}\right\rfloor\right\}.
\tag{193.C3b}
\]

Fix \(C_0\ge2\) independently of every asymptotic variable, and put

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\quad
 \mathcal F_A=\{(c,d_0):1\le c\le A,\ 0\le d_0\le c,
                         \ (c,d_0)=1\}.
\tag{193.C3c}
\]

The accepted Round-187--Round-192 transformations define complex linear
operators

\[
 \mathscr H_Y^\sigma(W)
 =\mathscr S_{\le192,Y,Q}^\sigma(W)
  +\mathscr R_{{\rm core},Y,Q}^\sigma(W).
\tag{193.C4}
\]

Here the exact Round-192 convention is retained.  If \(T=0\), its union
projector \(P_A\) is identically zero and the core is the whole inherited
Round-191 rho-large remainder before the new physical split.  If
\(T\ge1\), every core row satisfies simultaneously

\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1).
\tag{193.C4a}
\]

For a physical atom (193.C2), put \(g=(d,d')\) and define

\[
 P_{\rm cl}(x)=
 \mathbf1_{|d-gm|\le D_L}\,
 \mathbf1_{|d'-gm'|\le D_L}.
\tag{193.C5}
\]

This mask is imposed on the physical source before Fourier expansion or
height differencing.  Bracket notation means evaluation of the accepted
linear operator on the masked source:

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 :=\mathscr R_{\rm core}(P_{\rm cl}W),
\quad
 \mathscr S_{\le192}[P_{\rm cl}]
 :=\mathscr S_{\le192}(P_{\rm cl}W).
\tag{193.C6}
\]

It does not mean multiplication of an already formed Abel jump by a
single post-expansion mask.  Then the complete double-close sector of the
exact core is absolutely target-safe:

\[
 \boxed{
 \left|\mathscr R_{{\rm core},Y,Q}^\sigma[P_{\rm cl}]\right|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon .}
\tag{193.C7}
\]

No condition \((m,m')=1\) and no restriction \(r\equiv2\pmod4\) is
needed for (193.C7).  On the narrower sub-sector where both hold, the
gcd-scaled map

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g)
\tag{193.C8}
\]

is a genuine character-reversing orientation involution.  That algebra
is valid but is not needed for the absolute estimate (193.C7).

## 2. Multiplicity-one double-close count

In the plus orientation, use the accepted primitive coordinates

\[
 d=\kappa gU,\qquad d'=g(\kappa U+2S),\qquad
 m'=\kappa v,\qquad m=\kappa v+2w,
\tag{193.C9}
\]

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0,\qquad S,w>0.
\tag{193.C10}
\]

They parametrize the live opened incidences with multiplicity one.  The
two close relations are

\[
 |\kappa(U-v)-2w|\le {D_L\over g},\qquad
 |\kappa(U-v)+2S|\le {D_L\over g}.
\tag{193.C11}
\]

Subtracting the quantities inside the absolute values and then using
either inequality gives

\[
 S+w\le {D_L\over g},\qquad
 |\kappa(U-v)|\le {3D_L\over g}.
\tag{193.C12}
\]

On a live atom, (193.C3), the strict hard cone, and the lower close
inequality give, uniformly for every \(L\ge2\),

\[
 1\le g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}\le G_0,
\tag{193.C13}
\]

where \(m\ge cL\) on the fixed literal shell and
\(D_L\le2\sqrt L\).  Thus \(g\) belongs to one fixed finite set with
no bounded-shell exception or hidden \(B\)-dependence.

Fix \((\kappa,g,U,v,w)\).  Equation (193.C10) confines \(S\) to

\[
 {Uw\over v}<S< {Uw\over v}+{R_0\over2\kappa gv}.
\tag{193.C14}
\]

Since the live upper complementary factor obeys \(\kappa v\asymp L\),
the interval in (193.C14) has length \(O(1)\) and contains \(O(1)\)
integers.  At fixed \((\kappa,g)\), there are

\[
 O(1+L/\kappa)\text{ choices of }U,
\quad O(1+D_L/\kappa)\text{ choices of }v,
\quad O(1+D_L)\text{ choices of }w.
\tag{193.C15}
\]

Consequently

\[
\begin{aligned}
 &\sum_{\kappa\ll L}
 (1+L/\kappa)(1+D_L/\kappa)(1+D_L)\\
 &\qquad\ll
 (1+D_L)\{L+L\log(2L)+D_L\log(2L)+LD_L\}
\end{aligned}
\tag{193.C16a}
\]

and therefore

\[
 \#\mathcal I_{{\rm cl},+}
 \ll LD_L\log(2L)+LD_L^2.
\tag{193.C16}
\]

The minus orientation has the same count, with
\(h=Uw-vS>0\).  All dyadic-height, core, arithmetic, and literal
conditions only delete atoms.  In particular, \(h\) is determined by
\((U,v,S,w)\); there is no additional factor \(Y\).  Since
\(D_L\le2L^{1/2}\),

\[
 \boxed{
 \#\mathcal I_{\rm cl}
 \ll LD_L\log(2L)+LD_L^2
 \ll_\eta L^2X^\eta .}
\tag{193.C17}
\]

The pointwise bound (193.C3), with a fresh epsilon split, proves

\[
 \boxed{
 |\mathscr H_Y^\sigma(P_{\rm cl}W)|
 \ll_\varepsilon L^2X^\varepsilon .}
\tag{193.C18}
\]

The proof actually counts the whole Fejer range
\(0<h<R_0/(2\kappa g)\), so (193.C18) is uniform in the dyadic block.

## 3. Exact passage through the Round-192 core

Let the free physical atom carry its full orientation, height, affine
site, endpoint order, arithmetic masks, coefficient, phase, and zero
extension.  Every Fourier copy and every source term in the accepted
finite linear decompositions inherits the mask of its physical parent.
Because (193.C5) is independent of the Fourier mode, complete anchor
Fourier expansion is coordinatewise linear on \(P_{\rm cl}W\).

At the Round-191 height interface the mask depends on the affine site,
not only on the height.  For each fixed row and orientation, define

\[
 W^P_\omega(h)=
 \sum_{t\in I_\omega(h)}P_\omega(h,t)(-1)^tB_\omega(h,t),
\tag{193.C19}
\]

with the original carrier and zero extension, and use

\[
 \Delta^-W^P_\omega(h)=W^P_\omega(h)-W^P_\omega(h-1)
\tag{193.C19a}
\]

in Abel inversion.  On a transported common site, let the previous
index be \(t+\nu_\omega(h)\) and let
\(\chi_\omega(h)\) be the transported affine sign.  Then exactly

\[
\begin{aligned}
 &P_h(t)B_h(t)
 -\chi_\omega(h)P_{h-1}(t+\nu)B_{h-1}(t+\nu)\\
 &\quad=P_h(t)
 \{B_h(t)-\chi_\omega(h)B_{h-1}(t+\nu)\}\\
 &\qquad+\chi_\omega(h)
 \{P_h(t)-P_{h-1}(t+\nu)\}B_{h-1}(t+\nu).
\end{aligned}
\tag{193.C19b}
\]

The second term is the exact physical-mask commutator and remains in the
new core.  Current sites without transported predecessors and previous
sites without current images remain the usual affine births and deaths.
No proof uses the generally false scalar shorthand
\(P\Delta^-W=\Delta^-(PW)\).

Apply every accepted projector to \(P_{\rm cl}W\), retaining the
original carrier geometry and zero extension.  The safe estimates remain
valid after this physical deletion:

1. Round 187's \(U=1\), low-exact-conductor, and ordinary-edge pieces
   use positive atom counts and Fourier \(\ell^1\) mass.
2. Round 188's imprimitive-lift piece uses a positive atom count and the
   exact lift weight.
3. Round 189's projectively slow piece uses residue-class sparsity and
   positive atom counting.
4. Round 191's inverse-small piece returns the deleted zero-extended row
   by exact Abel inversion and then counts rows and atoms.  The outer
   carrier terminal and isolated Fejer pieces keep their accepted
   positive bounds; a new interior \(P\)-jump remains in the remainder.
5. Round 192's Farey union is one row indicator followed by divisor
   multiplicity and positive row counting.  Its replacement of selected
   terminal and Fejer rows is retained, so no term is duplicated.

Thus

\[
 \boxed{
 |\mathscr S_{\le192,Y,Q}^\sigma(P_{\rm cl}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon .}
\tag{193.C20}
\]

Linearity of the accepted operator identity (193.C4) gives

\[
 \mathscr R_{{\rm core},Y,Q}^\sigma[P_{\rm cl}]
 =\mathscr H_Y^\sigma(P_{\rm cl}W)
  -\mathscr S_{\le192,Y,Q}^\sigma(P_{\rm cl}W).
\tag{193.C21}
\]

Equations (193.C18), (193.C20), and (193.C21) prove (193.C7).  At
\(T=0\), the Round-192 Farey projector is still identically zero and
the whole inherited rho-large remainder is present before the new split.

## 4. Exact complement and scale boundary

Define the disjoint first-failure physical masks

\[
 P_1=\mathbf1_{|d-gm|>D_L},
\qquad
 P_2=\mathbf1_{|d-gm|\le D_L}
      \mathbf1_{|d'-gm'|>D_L}.
\tag{193.C22}
\]

Then \(1=P_{\rm cl}+P_1+P_2\) on the opposing physical source.  Since
the core operator is linear,

\[
 \mathscr R_{\rm core}(W)
 =\mathscr R_{\rm core}(P_{\rm cl}W)
  +\mathscr R_{\rm core}(P_1W)
  +\mathscr R_{\rm core}(P_2W).
\tag{193.C23}
\]

Only the first term is proved target-safe.  The other two retain all
Round-192 core predicates and every literal field and remain under the
one outer real part.

For a close width in the explicit range \(1\le D\le L\), the same
positive proof gives

\[
 |\mathscr H_Y^\sigma(P_{{\rm cl},D}W)|
 \ll_\eta\{LD\log(2L)+LD^2\}X^\eta.
\tag{193.C24}
\]

At \(D=L^{1/2+\delta}\), \(0\le\delta\le1/2\), the second term is
\(L^{2+2\delta}\).  Thus the present absolute mechanism does not extend
beyond the square-root power scale.  This is an upper-capacity deficit,
not literal lower mass and not a disproof of a wider signed estimate.

## 5. Subsidiary scaled-orientation algebra

Put \(k=(m,m')\).  On \(k=1\), even \(r\) and odd \(d,d'\) imply
that \(m,m'\) have the same parity, hence both are odd.  The map
(193.C8) is integral and satisfies

\[
 (gm)(d/g)=N,\qquad (gm')(d'/g)=N+r,
\tag{193.C25}
\]

\[
 (gm,gm')=g,\qquad (d/g,d'/g)=1.
\tag{193.C26}
\]

Therefore the recomputed character-leg gcd is again \(g\), the new
cofactor gcd is one, and \(\tau_g^2=1\).  It interchanges the two
opposing orientations and is fixed-point-free there.

For the plus coordinates (193.C9), its image is the canonical minus
tuple

\[
 (\kappa,g,U',v',S',w')=(\kappa,g,v,U,w,S).
\tag{193.C27}
\]

Squarefreeness and the accepted primitive coprimalities give
\((gv,U)=1\), while \(k=1\) gives \((v,w)=1\); hence
\((v,h)=1\).  These are the new primitive and \((U',h)=1\)
conditions, and the inward cross gcd remains canonically \(\kappa\).

On \(r\equiv2\pmod4\), all four factors are odd and

\[
 \boxed{
 \chi_4(d')\chi_4(d)
 =-\chi_4(gm')\chi_4(gm).}
\tag{193.C28}
\]

Products, endpoint order, lower conjugation, \(r\), the Fejer weight,
and the square-root phase are unchanged.  After the complete anchor
Fourier sum is recombined, ambient zero extension and orbit reindexing
give the exact paired coefficient commutator on

\[
 P_{\rm sw}:=P_{\rm cl}\,
 \mathbf1_{(m,m')=1}\,
 \mathbf1_{r\equiv2\ ({\rm mod}\ 4)}.
\tag{193.C28a}
\]

Writing

\[
 \Phi_r(N)=\left(1-{r\over R_0}\right)
 e\!\left({\sigma\sqrt X\,r\over\sqrt{N+r}+\sqrt N}\right),
\tag{193.C28b}
\]

that commutator is

\[
\begin{aligned}
 {1\over2}\sum_{x\in P_{\rm sw}}
 \chi_4(d')\chi_4(d)\Phi_r(N)
 \bigl\{&\lambda_{N+r,\sigma}(d')
          \overline{\lambda_{N,\sigma}(d)}\\
 &-\lambda_{N+r,\sigma}(gm')
          \overline{\lambda_{N,\sigma}(gm)}\bigr\}.
\end{aligned}
\tag{193.C29}
\]

For the Round-184 residual mask, every prime in \(g\) stays on the
character leg and every prime outside \(g\) is complemented.  The
truth table \((1,0,0,1)\) is preserved except when exactly one selected
prime lies in \(g\).  Since active \(g\) lies in a fixed finite set and
the selected primes have logarithmic gap \(O(L^{-1/2})\), this exception
is absent for sufficiently large \(L\) and is paid by (193.C17) on the
bounded remaining shells.  In any event, (193.C29) remains exact with
zero extension, and the primary proof (193.C17) does not require mask
invariance.

The optional common-cell/BV audit also has the correct power.  On each
endpoint write the moving symbol as
\(\eta_L(u)b^{\rm sm}(u,v)\).  On a common literal smooth cell only the
uniformly \(C^1\) factor \(b^{\rm sm}\) is assigned the pointwise
\(O(D_L/L)\) displacement; the normalized dyadic-BV factor \(\eta_L\)
is charged separately in (193.C31).  Against the coarse orbit envelope,
the smooth part is

\[
 O(D_L^3\log(2L)+D_L^4)=O_\eta(L^2X^\eta).
\tag{193.C30}
\]

Fixing one crossed normalized-BV increment or one literal face localizes
one scale coordinate to an \(O(D_L)\) collar and has multiplicity

\[
 \sum_{\kappa\ll L}
 O\!\left(D_L^2(1+D_L/\kappa)^2\right)
 \ll LD_L^2+D_L^3\log(2L)+D_L^4
 \ll_\eta L^2X^\eta.
\tag{193.C31}
\]

Thus the requested coefficient and literal ledgers pass independently,
although the absolute count makes them unnecessary for (193.C7).

## 6. Scope and dependencies

This candidate proves only the exact double-close sector
\(\mathscr R_{\rm core}[P_{\rm cl}]\) and the finite subsidiary
involution identities.  It does not prove either complement in
(193.C22), the complete rho-large remainder, the complete original
\(t=1\) residual, any original \(t\ge2\) range, the large-\(G\)
near-resonant complement, the remaining small-\(t\) owner, either M1
parent, GAR, any M2 parent, endpoint uniformity, M9, either bridge, or
the Gauss-circle target.  The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent records are
unchanged.

The dependency and provenance ledger is typed as follows.

1. The direct logical graph prerequisite is
   `M9-M1-hard-top-t1-rho-large-farey-covector-reduction`, which supplies
   the exact core operator.  The physical multiplicity-one interface is
   supplied explicitly by
   `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`; it is
   transitive in the accepted graph but is named because (193.C9)--(193.C17)
   reopen that physical coordinate chart.
2. The accepted Round-187 conductor, Round-188 imprimitive-lift,
   Round-189 projective, Round-191 signed-inverse/height, and Round-192
   Farey kernels are reopened only to verify deletion stability in
   (193.C20).  Round 193 does not enlarge or re-promote them.
3. The Round-184 comparable-factor kernel supplies the residual-selector
   truth table used only in the subsidiary audit (193.C29)--(193.C31).
   `Divisor-bound-elementary` is inherited through the accepted outer
   ledgers rather than invoked as a new analytic estimate.

The exact Round-193 claimant evidence paths are:

- `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/gcd_scaled_orientation_sector_attack.md`;
- `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/core_projection_mask_power_hostile_audit.md`.

The accepted parent-kernel provenance is
`proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`;
it is not claimant evidence for the new Round-193 estimate.

The Round-193 finite control
`rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic.wl`
and its output
`rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic_output.md`
are diagnostic only.  Neither claimant uses them to prove the asymptotic
estimate.

## 7. Dependencies and proof-state boundary

After independent normalization, count/power, masked-operator,
blind-post-unmask, owner-scope, provenance, and graph-replay review, this
kernel supports exactly the following state effect:

1. create one subordinate `proved_internal` node for (193.C5)--(193.C23);
2. add it only as strict-sector evidence to the already-open
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
3. record (193.C24) as the exact method boundary and (193.C28)--(193.C31)
   as subsidiary finite algebra and seam controls; and
4. leave every parent, bridge, theorem, and exponent unchanged.

The Round-193 terminal label is
`strict_rho_large_gcd_scaled_orientation_sector`.

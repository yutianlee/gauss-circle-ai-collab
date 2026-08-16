## 1. Result

The proposed transition flattening is valid for the complete fixed-interior
actual symbol.  Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 \Lambda=J/c,
\]

and let
\(J^{32/45}<C\leq J^{13/18}\), \(c\asymp C\), and
\(b\asymp B=C/T\).  For either offset-Poisson alias, every one of the
three local classes \(\kappa=c/[c,4]\in\{1/4,1/2,1\}\), and every
compatible nonaxial member \((\rho,\sigma)\) of the fixed dual family,
the exact normalized coefficient on an admissible progression
\(c=r\pmod {4b}\) has the decomposition

\[
 W_{b,r}(c)=\Gamma_{\epsilon,z_*}V_{b,r}(c)+E_{b,r}(c),
 \qquad z_*^2=\kappa\rho\sigma,                         \tag{1.1}
\]

where \(z_*\) is the sign-compatible critical point,
\(\epsilon=\operatorname {sgn}\psi''(z_*)\), and

\[
 \|V_{b,r}\|_\infty+\operatorname {Var}_{c\equiv r(4b)}
 V_{b,r}\ll_\varepsilon X^\varepsilon,                  \tag{1.2}
\]

\[
 \sup_{c\equiv r(4b)}|E_{b,r}(c)|
 \ll_\varepsilon X^\varepsilon\Lambda^{-1/2}
 \asymp X^\varepsilon\sqrt{C/J}.                         \tag{1.3}
\]

Here \(\Gamma_{\epsilon,z_*}\) is the neighbor-independent full
Gaussian when \(-1<z_*<1\), the appropriate oriented half Gaussian when
\(z_*=\pm1\), and zero when \(|z_*|>1\).  The error in (1.3) contains,
not discards, the displacement of both Farey faces, the complete
two-variable stationary remainder, the one-variable Morse remainder, the
nonstationary complement, alias and floor corrections, and every
neighbor-switch jump.  No bounded-variation assertion is made for
\(E_{b,r}\).

Consequently Bourgain's exponent pair gives

\[
 |S_{b,k}^{(\kappa),\mathrm{main}}(C)|
 \ll_\varepsilon X^\varepsilon C Q^{-5/24},\qquad
 |S_{b,k}^{(\kappa),\mathrm{err}}(C)|
 \ll_\varepsilon X^\varepsilon C\sqrt{C/J},             \tag{1.4}
\]

and hence

\[
 \sum_{b\asymp C/T}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon
 \left(\frac{C^3}{TQ^{5/12}}+\frac{C^4}{TJ}\right)
 \leq X^\varepsilon\frac{J^2}{T}                         \tag{1.5}
\]

through \(C=J^{13/18}\).  The separately accepted axes remain
target-safe there.  Thus the accepted fixed-smooth-interior order-\(J\)
range extends from \(C\leq J^{32/45}\) to
\(C\leq J^{13/18}\).  This proves no estimate for the remaining
\(J^{13/18}<C\leq J\), cone edges, the full \(M9\!-!M1\) statement,
\(M9\), or the Gauss-circle exponent.

## 2. Exact statement and hypotheses

Let \(R=\lfloor J\rfloor\).  Fix one smooth interior one-sided ratio
piece, one of the two aliases, a sign/orientation, a local class
\(\kappa\), a compatible nonaxial pair \(k=\rho\sigma>0\), and
\(b\asymp C/T\).  The ratio support and the stationary equations leave a
fixed finite set of such pairs.  Fix an admissible residue
\(r\pmod {4b}\); the star condition is \((b,r)=1\), and then
\((b,c)=1\) for every \(c=r+4b\ell\).

For the Farey neighbors \(a_-/c_-\), \(a_+/c_+\) of \(b/c\) at
order \(R\), use the exact determinant conventions

\[
 bc_--a_-c=1,\qquad a_+c-bc_+=1,\qquad
 R-c<c_\pm\leq R.                                         \tag{2.1}
\]

The exact scaled faces are

\[
 z_-(c)=-\frac{J}{c+c_-},\qquad
 z_+(c)= \frac{J}{c+c_+}.                                  \tag{2.2}
\]

After the exact row normalization and extraction of the accepted
reciprocal phase

\[
 e\!\left(\pm\frac{A_{\kappa,b}}c\right),\qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2,  \tag{2.3}
\]

the oscillatory part of the actual coefficient can be written exactly,
after a fixed neighbor-independent partition, as
\(W_{b,r}(c)=U_{b,r,k}^{(\kappa)}\mathcal W_c\), where

\[
 \mathcal W_c=
 \Lambda^{1/2}e(-\Lambda\psi(z_*))
 \Lambda\int_{z_-(c)}^{z_+(c)}
 \iint \mathcal A_c(z,u,v)e(\Lambda\phi(z,u,v))\,du\,dv\,dz,
                                                                  \tag{2.4}
\]

with

\[
 \phi(z,u,v)=z(uv-1)-\rho u-\kappa\sigma v,\qquad
 \psi(z)=-z-\frac{\kappa k}{z}.                            \tag{2.5}
\]

All fixed non-arithmetic class constants may be included in
\(\mathcal A_c\); the exact arithmetic unit
\(U_{b,r,k}^{(\kappa)}\) is kept outside and is constant on the
progression.  Formula (2.4) is a normalization statement:
the remaining harmless powers of \(c/C\), already present in the
definition of \(W_{b,r}\), are included in \(\mathcal A_c\).
The exact Round-71 identity gives the following properties, which are also
verified factor by factor below:

1. \(\mathcal A_c\) is independent of \(c_\pm\); the neighbors enter
   only through (2.2).
2. On every fixed Morse chart, finitely many \((z,u,v)\)-seminorms are
   \(O_\varepsilon(X^\varepsilon)\).
3. For a fixed sufficiently large \(M\), the continuous extension in
   \(c\) satisfies
   \[
   \max_{|\alpha|\leq M}\int_C^{2C}
   \sup_{z,u,v}|\partial_c\partial_{z,u,v}^{\alpha}
   \mathcal A_c(z,u,v)|\,dc
   \ll_\varepsilon X^\varepsilon.
   \]
4. The two aliases, the dyadic conductor cutoff, the smooth ratio symbol,
   the exact \(X=N+\vartheta\) offset, and the stationary Jacobians are
   retained in \(\mathcal A_c\).  The local unit is constant on the
   progression.

The nonaxial critical equations are

\[
 uv=1,\qquad zv=\rho,\qquad zu=\kappa\sigma,
\]

so

\[
 z_*^2=\kappa k,\qquad
 u_*=\frac{\kappa\sigma}{z_*},\qquad
 v_*=\frac{\rho}{z_*}.                                    \tag{2.6}
\]

The sign of \(z_*\) is fixed by the positive \((u,v)\)-support.  At
this point

\[
 \psi'(z_*)=0,\qquad \psi''(z_*)=-\frac2{z_*}\ne0.       \tag{2.7}
\]

Choose the real Morse coordinate \(t=t(z)\), independent of the Farey
neighbors, by

\[
 \psi(z)-\psi(z_*)=\epsilon t^2/2,\qquad
 t(z_*)=0,\qquad t'(z_*)>0.                                 \tag{2.8}
\]

With \(e(x)=e^{2\pi ix}\), define

\[
 G_\epsilon(a,b)=\int_a^b e(\epsilon s^2/2)\,ds          \tag{2.9}
\]

as an oscillatory improper integral when an endpoint is infinite.  Then

\[
 \Gamma_{\epsilon,z_*}=
 \begin{cases}
 G_\epsilon(-\infty,\infty),&-1<z_*<1,\\
 G_\epsilon(-\infty,0),&z_*=1,\\
 G_\epsilon(0,\infty),&z_*=-1,\\
 0,&|z_*|>1,
 \end{cases}                                                \tag{2.10}
\]

with the two middle lines interchanged if the oriented alias reverses the
Morse coordinate.  Let \(q_c(z)\) be the exact leading symbol after
stationary phase in \((u,v)\), and put

\[
 V_{b,r}(c)=U_{b,r,k}^{(\kappa)}
 q_c(z_*)\left|\psi''(z_*)\right|^{-1/2},                 \tag{2.11}
\]

where the fixed transverse Gaussian constant is included in \(q_c\).
When \(|z_*|>1\), set \(V_{b,r}=0\), since
\(\Gamma_{\epsilon,z_*}=0\); the value displayed in (2.11) is then
immaterial.  This is the claimed neighbor-independent main symbol.  The statement is
that the exact coefficient (2.4), including all its remainders, equals
(2.10)--(2.11) plus an error satisfying (1.3).

## 3. Proof or derivation

**Exact Farey collar, including the floor.**  Put
\(D_\pm=c+c_\pm\).  Since \(D_\pm\) is an integer and
\(D_\pm>R\),

\[
 R+1\leq D_\pm\leq R+c.
\]

As \(R\leq J<R+1\), one has \(D_\pm>J\), and therefore

\[
 0<1-z_+(c)=\frac{D_+-J}{D_+}\leq\frac{c}{R+1},\qquad
 0<1+z_-(c)=\frac{D_--J}{D_-}\leq\frac{c}{R+1}.           \tag{3.1}
\]

Thus both sharp faces lie inward from \(\pm1\), and

\[
 |z_+(c)-1|+|z_-(c)+1|\ll C/J\asymp\Lambda^{-1}.          \tag{3.2}
\]

This uses the exact \(R=\lfloor J\rfloor\) Farey tessellation; no
integer replacement has been hidden.  If one writes the faces temporarily
with \(R\) in the numerator, the difference is at most \(J^{-1}\),
whose Morse-scaled size is
\(O((cJ)^{-1/2})\), smaller than \(\Lambda^{-1/2}\).
The inclusion or exclusion of a continuous endpoint has measure zero,
while the inherited half-open convention continues to give one-count
ownership to the discrete modulus.

**Two transverse variables and the complete remainder.**  Around the
sign-compatible critical point, \(|z|\gg1\).  For fixed \(z\), the
phase in \((u,v)\) is exactly quadratic after translating to
\((u_*(z),v_*(z))=(\kappa\sigma/z,\rho/z)\):

\[
 \phi(z,u,v)=\psi(z)+z(u-u_*(z))(v-v_*(z)).                \tag{3.3}
\]

Uniform two-dimensional stationary phase therefore gives

\[
 \Lambda\iint\mathcal A_c(z,u,v)e(\Lambda\phi)\,du\,dv
 =e(\Lambda\psi(z))
 \{q_c(z)+\Lambda^{-1}r_c(z;\Lambda)\},                 \tag{3.4}
\]

where

\[
 \|q_c\|_{C^2}+\|r_c\|_\infty
 \ll_\varepsilon X^\varepsilon.                          \tag{3.5}
\]

The leading transverse factor has size \(|z|^{-1}\), and (2.7) then
recovers the accepted \(|z_*|^{-1/2}=(\kappa k)^{-1/4}\)
three-variable stationary size.  The contribution of the
\(\Lambda^{-1}r_c\) term to the normalized coefficient (2.4) is already

\[
 O_\varepsilon(X^\varepsilon\Lambda^{-1/2}).              \tag{3.6}
\]

This is the first part of the complete stationary remainder, not a
leading-term substitution.

A fixed partition separates this chart from its complement.  On the
complement, including a neighborhood of \(z=0\), at least one of
\(zv-\rho\) and \(zu-\kappa\sigma\) is bounded away from zero for
the finite nonaxial family.  Repeated integration by parts in \(u\) or
\(v\), never across a sharp \(z\)-face, gives
\(O_A(X^\varepsilon\Lambda^{1-A})\) before the final normalization.
Taking \(A\geq2\), and then summing the rapidly decreasing dual tails,
puts the whole nonstationary complement inside (3.6).

**One-dimensional uniform Morse estimate.**  It remains to analyze

\[
 \Lambda^{1/2}e(-\Lambda\psi(z_*))
 \int_{z_-}^{z_+}q_c(z)e(\Lambda\psi(z))\,dz.             \tag{3.7}
\]

On the fixed Morse chart, (2.8) turns (3.7) into

\[
 \Lambda^{1/2}\int_{t_-}^{t_+}
 h_c(t)e(\epsilon\Lambda t^2/2)\,dt,\qquad
 h_c(t)=q_c(z(t))z'(t).                                     \tag{3.8}
\]

Write \(h_c(t)=h_c(0)+t g_c(t)\) near zero.  Since

\[
 t e(\epsilon\Lambda t^2/2)
 =(2\pi i\epsilon\Lambda)^{-1}
 \frac d{dt}e(\epsilon\Lambda t^2/2),
\]

one integration by parts, followed by ordinary nonstationary integration
away from the chart, proves the uniform formula

\[
 (3.7)=h_c(0)
 G_\epsilon(\sqrt{\Lambda}\,t_-,\sqrt{\Lambda}\,t_+)
 +O_\varepsilon(X^\varepsilon\Lambda^{-1/2}).             \tag{3.9}
\]

This proof retains the full amplitude.  The error in (3.9) includes the
moving-symbol correction \(h_c(t)-h_c(0)\), both endpoint terms from
integration by parts, and the fixed-chart complement.  Together with
(3.4)--(3.6), it is the complete normalized stationary remainder.

The oscillatory tail estimate

\[
 \left|\int_Y^\infty e(\epsilon s^2/2)\,ds\right|
 \ll(1+|Y|)^{-1}                                           \tag{3.10}
\]

now gives the exact trichotomy.  Because the critical set is finite,
there is a fixed \(\delta_0>0\) such that every nonboundary retained
\(z_*\) has distance at least \(\delta_0\) from \(\{-1,1\}\).

* If \(-1<z_*<1\), both Morse endpoints have size
  \(\gg\sqrt\Lambda\), with opposite signs.  The two tails in
  (3.10) replace the incomplete Gaussian by the full one with error
  \(O(\Lambda^{-1/2})\).
* If \(z_*=1\), (3.1), (3.2), and smoothness of the Morse map give
  \(t_+=O(\Lambda^{-1})\), hence
  \(\sqrt\Lambda t_+=O(\Lambda^{-1/2})\).  The lower tail costs
  \(O(\Lambda^{-1/2})\), and the interval between
  \(\sqrt\Lambda t_+\) and zero has that same length.  This gives the
  oriented half Gaussian.  The case \(z_*=-1\) is identical.
* If \(|z_*|>1\), the actual interval is a fixed distance from every
  critical point.  Direct integration by parts in (3.7), or the
  difference of the two Gaussian tails, is
  \(O(\Lambda^{-1/2})\) after normalization, and the limiting
  coefficient is zero.

This proves (1.1) and (1.3).

**Why the main symbol has global variation.**  The value
\(h_c(0)=q_c(z_*)|\psi''(z_*)|^{-1/2}\) contains no Farey neighbor.
Every one of its actual factors is smooth on the full progression:

* the dyadic conductor cutoff and powers of \(c/C\) have
  \(c\)-logarithmic derivatives \(O(1)\);
* \(u_*,v_*,z_*\), the ratio symbol evaluated there, and all Morse and
  stationary Jacobians are fixed for \((\kappa,\rho,\sigma)\);
* on the positive alias the Fourier profile is evaluated at
  \(Tb/c+Tz_*/(cJ)\), and on the negative alias at the reflected
  argument; in either case its derivative is \(O(1/c)\);
* the exact periodized offset multiplier combines
  \(N+\vartheta=X\), so the fast phase is exactly (2.3); its remaining
  alias factor is fixed or has derivative \(O(1/c)\);
* \(\kappa\), every parity restriction, and the exact local unit are
  constant when \(c\equiv r\pmod {4b}\).

The authorized amplitude seminorm (81.A3), evaluated at the fixed
critical point and composed with the fixed stationary and Morse
Jacobians, therefore gives

\[
 \sup_{C\leq c\leq2C}|V_{b,r}(c)|
 +\int_C^{2C}|V_{b,r}'(c)|\,dc
 \ll_\varepsilon X^\varepsilon.                          \tag{3.11}
\]

Smooth interpolation and the fundamental theorem of calculus along the
ordered progression give (1.2), including its first and last truncated
sample.  Crucially, no derivative of \(c_\pm\) occurs.

For completeness, constancy of the arithmetic unit is separate in the
three classes.  If \(c\) is odd, then \(\kappa=1/4\),
\(\sigma\) is odd, and

\[
 \mathfrak C_{c,b}(\rho,\sigma)
 =2ic\,\chi_4(c\sigma)
 e_c(\lambda_c k\bar b).
\]

Reciprocity extracts (2.3) and leaves, up to the fixed class
normalization,
\(\chi_4(c\sigma)e_{4b}(k\bar c)\), which is constant modulo
\(4b\).  If \(c\equiv2\pmod4\), then
\(\kappa=1/2\), \(\rho,\sigma\) are odd, and the residual unit is
\(\chi_4(s_0)e_{2b}(\sigma t)\).  If \(4\mid c\), then
\(\kappa=1\), \(\rho\) is odd, and it is
\(\chi_4(s_0)e_b(\sigma t)\).  In the even cases

\[
 bs_0+\rho=tc.
\]

The congruence \(tr\equiv\rho\pmod b\), together with the standard
representative range, fixes \(t\); then
\(s_0=(tc-\rho)/b\) changes by \(4t\) when \(c\) changes by
\(4b\), so \(s_0\pmod4\) is fixed.  This proves the asserted
constancy rather than transferring the odd formula by a sign change.
Both aliases merely reverse (2.3) and the oriented half coefficient; all
symbol and remainder estimates are unchanged.

**The Farey sawtooth is confined to the small remainder.**  In the
mandatory class \(4\mid c\), \(\rho=\sigma=1\), one has
\(z_*=1\) and

\[
 Y_+(c)=\sqrt\Lambda\,(z_+(c)-1)
 =O(\Lambda^{-1/2}).                                      \tag{3.12}
\]

When \(c_+\) jumps by \(\asymp C\), its possible jump is

\[
 \Delta Y_+\asymp
 \sqrt{J/C}\,\frac{C}{J}
 =\sqrt{C/J}=\Lambda^{-1/2}.                              \tag{3.13}
\]

There are \(O(J/C)=O(\Lambda)\) numerator changes on a fixed
progression, so the raw transition factor still has the forbidden
total-variation capacity \(\Lambda^{1/2}\).  Equations (3.9)--(3.12)
instead subtract the constant half Gaussian pointwise and put every jump
in \(E\), whose size remains \(O(\Lambda^{-1/2})\).  Simultaneous
changes of \(c_-\) and \(c_+\) obey the two separate bounds (3.1);
they do not affect \(V\).  Singleton neighbor cells likewise require no
variation estimate for \(E\).

**Bourgain and the energy ledger.**  On one full residue progression put

\[
 \alpha=\frac r{4b},\qquad
 K_{\kappa,b}=\frac{A_{\kappa,b}}{4b}.
\]

Then

\[
 \frac{A_{\kappa,b}}{r+4b\ell}
 =\frac{K_{\kappa,b}}{\ell+\alpha},\qquad
 K_{\kappa,b}
 =\frac X4+\frac{\sqrt{\kappa kX}}{2b}
   +\frac{\kappa k}{4b^2}\asymp X,                       \tag{3.14}
\]

and \(\ell+\alpha\asymp T\).  In exponent-pair notation the
summation length is \(M\asymp T\), the phase parameter is
\(\mathcal T=K_{\kappa,b}/T\asymp X/T=JQ\), and

\[
 \mathcal T/M\asymp X/T^2=Q^2,\qquad
 \frac{\log M}{\log\mathcal T}=\frac37.                \tag{3.15}
\]

Bourgain's Theorem 6 supplies
\((13/84+\varepsilon,55/84+\varepsilon)\).  His Section 5
proper-subinterval extension supplies the same estimate, with a logarithm
absorbed in \(X^\varepsilon\), for every subinterval of the ambient
dyadic progression.  Since the reciprocal phase satisfies the required
derivative conditions identically, uniformly in the shift \(\alpha\),

\[
 \sup_I\left|\sum_{\ell\in I}
 e\!\left(\pm\frac{K_{\kappa,b}}{\ell+\alpha}\right)\right|
 \ll_\varepsilon X^\varepsilon
 (Q^2)^{13/84}T^{55/84}
 =X^\varepsilon TQ^{-5/24}.                               \tag{3.16}
\]

Discrete Abel summation and (1.2) apply once on each whole residue
progression, not once per Farey cell.  There are \(O(b)=O(C/T)\)
admissible residues, and hence

\[
 |S_{b,k}^{(\kappa),\mathrm{main}}(C)|
 \ll_\varepsilon X^\varepsilon
 \frac CT\,TQ^{-5/24}
 =X^\varepsilon C Q^{-5/24}.                              \tag{3.17}
\]

The half-open one-count property gives only \(O(C)\) actual modulus
samples in the complete fixed-\(b\) row.  Triangle summation of (1.3)
therefore gives

\[
 |S_{b,k}^{(\kappa),\mathrm{err}}(C)|
 \ll_\varepsilon X^\varepsilon C\sqrt{C/J}.             \tag{3.18}
\]

There are \(O(B)=O(C/T)\) values of \(b\).  Squaring only after
(3.17)--(3.18), and absorbing the cross term by
\(|x+y|^2\leq2|x|^2+2|y|^2\), yields

\[
 \sum_{b\asymp C/T}|S_{b,k}^{(\kappa)}(C)|^2
 \ll_\varepsilon X^\varepsilon
 \left\{
 \frac CT(CQ^{-5/24})^2+
 \frac CT\left(C\sqrt{C/J}\right)^2
 \right\}
 =
 X^\varepsilon\left\{
 \frac{C^3}{TQ^{5/12}}+\frac{C^4}{TJ}
 \right\}.                                                \tag{3.19}
\]

The main term is at most \(J^2/T\) precisely when

\[
 C^3\leq J^2Q^{5/12}=J^{13/6},
 \quad\text{i.e.}\quad C\leq J^{13/18}.                 \tag{3.20}
\]

The error term requires only \(C^4\leq J^3\), or
\(C\leq J^{3/4}\).  Thus (3.20) is the binding condition.
The fixed number of aliases, orientations, \(\kappa\)-classes, and
critical pairs, and all divisor/gcd multiplicities cost
\(X^\varepsilon\).

Finally, the two axes are not inserted into this nonaxial Gaussian
argument.  The odd-class \(\rho=0\), \(\sigma\) odd axis and the
\(4\mid c\), \(\sigma=0\), \(\rho\) odd axis have no triple
critical point; there is no \(c\equiv2\pmod4\) axis.  The accepted
parameter-uniform integration-by-parts estimate gives their complete
block

\[
 \mathcal D_C^{\mathrm{axis}}
 \ll_\varepsilon X^\varepsilon C^2/J.
\]

At \(C\leq J^{13/18}\) this is
\(O(X^\varepsilon J^{4/9})\), strictly below the
\(J^{1/2}X^\varepsilon\) fixed-block target.  Both aliases, the large
dual tails, and the finite nonstationary errors are included in that
accepted estimate.

## 4. First doubtful or unproved step

There is no unresolved step inside the scoped flattening lemma: the
neighbor dependence is isolated exactly in the two faces, the
two-variable remainder is (3.6), the full moving-amplitude Morse remainder
is (3.9), and the floor-sized collars are (3.1)--(3.2).

The first unproved step is the next conductor interval
\(J^{13/18}<C\leq J\).  The present main energy
\(C^3/(TQ^{5/12})\) already exceeds \(J^2/T\) there, while the
pointwise transition error reaches its own barrier at \(C=J^{3/4}\).
No improvement of those powers follows from transition flattening.
Moreover, the separately accepted axis estimate does not cover
\(C>J^{3/4}\).  Closing those intervals requires a new signed
off-diagonal mechanism, not another summation of Farey-cell variation.

The only external theorem in the proved range is Bourgain's exponent
pair, including its proper-subinterval device.  It has been checked at
the actual ambient scale in (3.14)--(3.16); the claim is therefore not a
rescaling of a short neighbor cell.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | **Pass.** The exact \(d\tau=\Lambda dz\) factor is present in (2.4).  Transverse stationary phase cancels that factor, and the remaining one-dimensional saddle has normalized size one. |
| Farey determinant and half-open endpoints | **Pass.** Equations (2.1), (2.2), and (3.1) use the correct determinant signs.  Continuous endpoint inclusion is immaterial; discrete half-open ownership is retained. |
| \(R=\lfloor J\rfloor\) | **Pass.** The faces satisfy the exact inward-collar bound (3.1).  A temporary \(R\)-numerator changes a Gaussian argument by less than the allowed error. |
| Both aliases and orientations | **Pass.** Reflection changes the sign of (2.3) and chooses the oriented half Gaussian; the symbol, tail, and Bourgain estimates are sign-invariant. |
| All \(\kappa\)-classes and local units | **Pass.** Odd, twice-odd, and four-divisible classes are treated separately after their exact residue formulas.  The even classes use \(bs_0+\rho=tc\); they are not inferred from the odd class. |
| Gcd and parity stars | **Pass.** On \(c=r\pmod {4b}\), \((b,c)=(b,r)\), the parity class is fixed, and all compatibility restrictions are imposed before summation. |
| Finite critical family | **Pass.** Compact ratio support and (2.6) leave finitely many pairs and hence a uniform nonboundary gap \(\delta_0\). |
| Inside/boundary/outside trichotomy | **Pass.** The three cases follow from (3.9), (3.10), and the exact collar (3.2). |
| Complete stationary remainder | **Pass.** Equation (3.6) contains the full transverse remainder; (3.9) contains the moving symbol, boundary terms, and Morse remainder.  Nonstationary charts and dual tails are included. |
| Fixed-residue sawtooth | **Pass without global BV.** The boundary jump is (3.13), and its total-variation capacity is \(\sqrt{J/C}\).  The jump lies in a pointwise \(O(\sqrt{C/J})\) error instead. |
| Simultaneous switches | **Pass.** Each face separately satisfies (3.1); \(V\) contains neither face and remains continuous across a simultaneous switch. |
| Singleton cells | **Pass.** The main is summed on the uncut progression.  The remainder is pointwise and one-count, so a singleton costs one copy of (1.3). |
| Axes | **Pass in the new range.** The two surviving axes are \(O(X^\varepsilon C^2/J)\leq O(X^\varepsilon J^{4/9})\); the twice-odd class has no axis. |
| Bourgain source range | **Pass.** The actual parameters are \(M=T\), \(\mathcal T=JQ\), and \(\log M/\log\mathcal T=3/7\).  Section 5 permits a proper subinterval at logarithmic cost; no cell-length rescaling is used. |
| Energy exponents | **Pass.** The exact two terms are (3.19); their thresholds are \(J^{13/18}\) and \(J^{3/4}\), respectively. |
| Perfect squares and fourth powers | **Pass.** Exact boundary powers, including \(\kappa=k=1\), are covered by the half-Gaussian calculation.  The reciprocal derivative scale remains \(K\asymp X\), so no derivative degeneracy occurs. |
| Phase-conjugating/adversarial coefficients | **Correctly fails as a false analogue.** The proof uses the actual unit being constant and the actual leading symbol having (3.11).  Arbitrary alternating or phase-conjugating coefficients need not have global BV and would invalidate Abel summation. |
| \(N=\lfloor X\rfloor\), floors, stars, and errors | **Pass.** The two offset aliases recombine \(N+\vartheta=X\); all fast phase is in (2.3).  Farey and gcd stars, final truncated progressions, and finite errors remain explicit. |
| Cone and downstream scope | **Pass.** Only the fixed-smooth-interior order-\(J\) block is extended.  No cone edge, other radial sector, full \(M9\!-!M1\), \(M9\), endpoint-uniformity, or global exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts or sources used

The repository artifacts used were exactly:

* protocol.md;
* state/proof_obligations.yml;
* state/active_campaign.yml;
* strategy/conductor_0816_full_proof_strategy.md;
* rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet.md;
* rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet_actual_integral_addendum.md;
* rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/briefs/farey_transition_flattening_attack.md;
* rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/conductor_farey_stationary_low_conductor.md;
* rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reviews/conductor_round72_adjudication.md;
* rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md.

No sibling Round-81 report was read.

The external analytic input is Jean Bourgain, “Decoupling, exponential
sums and the Riemann zeta function,” Journal of the American Mathematical
Society 30 (2017), 205--224, Theorem 6 and Section 5,
https://arxiv.org/pdf/1408.5794.  Theorem 6 gives
\((13/84+\varepsilon,55/84+\varepsilon)\).  Section 5 explicitly
handles a proper subinterval by extending the phase to an ambient dyadic
interval and then applying the Sargos partial-sum device at an
\(O(\log M)\) cost.  The reciprocal phase in (3.14) is in the exact
monomial derivative class required there.  The prior selected source audit
was used to cross-check the parameter map; the primary paper was checked
again at Theorem 6 and the proper-subinterval discussion.

The stationary argument itself is internal: (3.3) is an exact quadratic
identity in the transverse variables, and the one-dimensional remainder
uses only the displayed Morse change of variables, one integration by
parts, and the elementary Fresnel-tail bound (3.10).

## 7. Recommended state effect

Promote a scoped internal lemma for the complete actual-symbol
transition flattening (1.1)--(1.3).  Record separately that the raw
boundary transition can have total-variation capacity
\(\sqrt{J/C}\); the promoted statement is pointwise-small-remainder,
not global BV for the raw symbol.

Using the already audited Bourgain exponent pair as an external
dependency, promote the fixed-smooth-interior order-\(J\) conductor
range

\[
 T\leq C\leq J^{13/18}.
\]

The new portion is
\(J^{32/45}<C\leq J^{13/18}\); the previously accepted lower portion
is unchanged.  Retain
\(J^{13/18}<C\leq J\) as the nonaxial residual range and retain the
separate upper-axis issue beyond \(J^{3/4}\).

Do not promote the complete fixed-interior wavelet across all conductors,
cone edges, \(M9\!-!M1\), \(M9\), endpoint uniformity, the
conditional bridge, or the Gauss-circle exponent.

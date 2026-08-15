# Blind rederivation: phase-removed translation divided difference

## 1. Result

For

\[
y=L-\nu,\qquad F(L,y)=H^\circ(L,L-y),
\]

fixed-physical-height differentiation gives the exact identity

\[
\boxed{
\mathfrak E_{H^\circ}(L,L-y)
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt .}
\tag{1.1}
\]

It holds for either sign of \(y\), and its continuous diagonal value is
\(F_{Ly}(L,0)+\tfrac12F_{yy}(L,0)\). There is no diagonal \(1/y\) term in
\(\mathfrak E_{H^\circ}\).

The complete singular regularizer nevertheless contains the independent
diagonal term

\[
K_C(L,\nu)=-\frac{iH^\circ(L,L)}{2A(L)D(L,\nu)},\qquad
D(L,\nu)=A(L)+\frac i2(L-\nu).
\tag{1.2}
\]

This is the first exact capacity obstruction to putting the *complete*
regularizer in the absolute mixed norm. With

\[
B(L)=\frac{H^\circ(L,L)}{A(L)},
\]

one has

\[
\int_{-V}^{V}|K_C(L,\nu)|\,d\nu
\asymp |B(L)|\log V
\tag{1.3}
\]

for large \(V\), unless \(B(L)=0\). Hence its full-height \(L^1(d\nu)\)
norm is infinite. The same nonabsolute Cauchy tail occurs in
\(\partial_LK_C\) through \(B'(L)/D\).

The term has instead the exact signed finite-section primitive

\[
\boxed{
\int_{p(L)}^{q(L)}K_C(L,\nu)\,d\nu
=B(L)\{\Log D(L,q(L))-\Log D(L,p(L))\}.}
\tag{1.4}
\]

On symmetric exhaustion, the logarithmic magnitudes cancel and the right
side remains bounded on a coherent branch, whereas (1.3) diverges. Thus
\(K_C\) and its \(L\)-derivative must be owned by an exact signed
Cauchy/log finite-section ledger, including its endpoint traces; they
cannot be part of the absolute kernel in (39.11). This ownership is
separate from \(\mathfrak E_{H^\circ}\) and from all smooth
ordinary-\(\mu\) shares.

The allowed packet supplies neither this primitive's target-scale
\(B,B'\), endpoint, and variation estimates nor an instruction excluding
it from the absolute norm. Therefore the frozen complete mixed-norm claim
cannot be certified as typed. After \(K_C\) is lawfully separated, the
next actual missing coefficient is the radial translation combination

\[
(1-t)J_{vv}+\frac12J_{sv},
\qquad J(s,v)=R_{1,v}(1-s)=\frac{I_1}{D},
\tag{1.5}
\]

for which no fixed-cell \(X^\varepsilon\) bound is inherited.

## 2. Exact statement and hypotheses

Freeze one cell \((j,h,q,x,\beta,\sigma)\), where \(\sigma\) is either
saddle sign and

\[
\lambda=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
b=\frac1{\log(2X)},\qquad 0\leq a<a_0,
\]

with the lawful inequalities of Round 38. The stationary oscillation,
\(\chi_4(q)\), stationary numerator \((D_j/q)\lambda\), coefficient
monomial, contour constants, \(x\)-integration, floors, stars, and
external \(X^{1/4}\) are outside \(H^\circ\). No aggregate \(\lambda\)
and no closed cell sum is used.

In \((L,y)\) coordinates,

\[
u=a+iy,\qquad v=b+i(L-y),\qquad
s=\frac54+i\left(\frac L2+\beta\right).
\tag{2.1}
\]

Consequently the two gamma arguments are

\[
z_-=s-\frac{u+v}{2}
=\frac54-\frac{a+b}{2}+i\beta,\qquad
z_+=s+\frac{u+v}{2}
=\frac54+\frac{a+b}{2}+i(L+\beta),
\tag{2.2}
\]

and the coefficient, kept outside the differentiated numerator, is

\[
\left(\frac hq\right)^{(u+v)/2}(hq)^{-s}
=h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
q^{-iL}(hq)^{-i\beta}.
\tag{2.3}
\]

For the singular regularizer,

\[
A(L)=-1-\frac b2-i(L+\beta),\qquad
D(L,\nu)=A(L)+\frac i2(L-\nu)
=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
\tag{2.4}
\]

Identity (1.1) needs \(F(L,\cdot)\) and \(F_L(L,\cdot)\) absolutely
continuous from \(0\) to \(y\), with \(F_{Ly}\) and \(F_{yy}\) integrable
on that segment. Its diagonal extension follows if those derivatives are
continuous at \(y=0\).

The most detailed actual factor-type ledger licensed by the supplied
files is, share by share,

\[
F_\ell=
\mathcal G_\ell(z_-,z_+)\,
J_\ell(s,v)\,
\widehat\phi(v)\,
\widehat W_j(u)\,
B_\ell^{\rm conn}\,O_\ell\,M_{\ell,\sigma},
\qquad J_\ell=\frac{I_{1,\ell}}D.
\tag{2.5}
\]

Here \(B_\ell^{\rm conn}\) is the beta mask/connector, \(O_\ell\) is
common artificial-pole ownership, and \(M_{\ell,\sigma}\) is the signed
entry/exit or normalized varying-amplitude Morse factor. The allowed
sources do not give their exact formulas or domains, or the complete
numerator \(I_{1,\ell}\). Thus (2.5) is an exact factor-*type* ledger but
not a promotable exact complete cell formula.

The requested absolute mixed norm is

\[
\begin{aligned}
\mathfrak M_\lambda(K)={}&
\sup_{L\in I_\lambda}\int|K(L,\nu)|\,d\nu
+\int_{I_\lambda}\!\int|\partial_LK(L,\nu)|\,d\nu\,dL\\
&+\sum_\gamma\int_{I_\lambda}|K(L,\gamma(L))|\,dL
+\mathfrak R_\lambda^{\rm Morse}(K),
\end{aligned}
\tag{2.6}
\]

with target \(O_\varepsilon(X^\varepsilon\lambda^{-2})\). A signed
finite-section primitive such as (1.4) is not an element of the first two
absolute integrals and needs a separate value/BV/trace statement.

## 3. Proof or derivation

At fixed physical height \(\nu\), \(y=L-\nu\) moves with \(L\), so

\[
\partial_LH^\circ(L,\nu)=F_L(L,y)+F_y(L,y),\qquad
\partial_\nu H^\circ(L,\nu)=-F_y(L,y).
\tag{3.1}
\]

Along the diagonal,

\[
(\partial_L+\partial_\nu)H^\circ(L,L)=F_L(L,0).
\tag{3.2}
\]

Substitution into the definition of the coefficient gives

\[
\mathfrak E_{H^\circ}
=\frac{F_L(L,y)-F_L(L,0)}y
+\frac{F_y(L,y)}y
-\frac{F(L,y)-F(L,0)}{y^2}.
\tag{3.3}
\]

The first quotient is

\[
\frac{F_L(L,y)-F_L(L,0)}y
=\int_0^1F_{Ly}(L,ty)\,dt.
\tag{3.4}
\]

For the remaining two terms,

\[
\begin{aligned}
\frac{F_y(L,y)}y-\frac{F(L,y)-F(L,0)}{y^2}
&=\frac1y\left\{F_y(L,y)-\int_0^1F_y(L,ty)\,dt\right\}\\
&=\int_0^1tF_{yy}(L,ty)\,dt,
\end{aligned}
\tag{3.5}
\]

where the last step is integration by parts in \(t\). Equations
(3.4)--(3.5) prove (1.1). In particular, the apparent
\(F_y(L,0)/y\) terms cancel before any absolute value.

As a rejected coordinate-convention warning, replacing the physical
derivative in (3.1) by the derivative at fixed translation \(y\) would
instead produce

\[
-\frac{F_y(L,0)}y
+\int_0^1F_{Ly}(L,ty)\,dt
-\int_0^1(1-t)F_{yy}(L,ty)\,dt.
\]

That expression omits the required \(F_y(L,y)/y\) contribution from
\(\partial_L|_\nu=\partial_L|_y+\partial_y\). It is not the canonical
\(\mathfrak E_{H^\circ}\), its artificial diagonal pole is not an open
coefficient, and it must not be confused with the independent large-height
Cauchy tail \(K_C\).

The coordinate vector fields on factors written in \((s,u,v)\) are

\[
\mathscr L:=\partial_L\big|_y=\frac i2\partial_s+i\partial_v,
\qquad
\mathscr Y:=\partial_y\big|_L=i\partial_u-i\partial_v.
\tag{3.6}
\]

They give the exact basic ledger

\[
\begin{array}{c|c|c|c|c}
Z&Z_L&Z_y&Z_{Ly}&Z_{yy}\\ \hline
\mathcal G(z_-,z_+)&\mathcal G_L&0&0&0\\
J(s,v)&iJ_v+\frac i2J_s&-iJ_v&J_{vv}+\frac12J_{sv}&-J_{vv}\\
\widehat\phi(v)&i\widehat\phi'&-i\widehat\phi'&
\widehat\phi''&-\widehat\phi''\\
\widehat W_j(u)&0&i\widehat W_j'&0&-\widehat W_j''
\end{array}
\tag{3.7}
\]

Although \(\mathcal G_{Ly}=0\), \(\mathcal G_L\) multiplies every
\(y\)-derivative of another factor in \(F_{Ly}\). A pure frozen-\(\beta\)
mask has zero \(L,y\) derivatives. Every actual \(L,y\)-dependent
connector, ownership mask, or Morse amplitude contributes its own
\(Z_L,Z_y,Z_{Ly},Z_{yy}\).

For \(F=\prod_{k=1}^mZ_k\), the full expansion, valid even at mask zeros,
is

\[
F_{yy}=\sum_i Z_{i,yy}\!\prod_{k\ne i}Z_k
+2\sum_{i<j}Z_{i,y}Z_{j,y}\!\prod_{k\ne i,j}Z_k,
\tag{3.8}
\]

\[
F_{Ly}=\sum_i Z_{i,Ly}\!\prod_{k\ne i}Z_k
+\sum_{i\ne j}Z_{i,L}Z_{j,y}\!\prod_{k\ne i,j}Z_k.
\tag{3.9}
\]

For the rational factor, in \((L,y)\) coordinates,

\[
D_L=-i,\quad D_y=\frac i2,\quad
(D^{-1})_L=iD^{-2},\quad
(D^{-1})_y=-\frac i2D^{-2},\quad
(D^{-1})_{Ly}=D^{-3},\quad
(D^{-1})_{yy}=-\frac12D^{-3}.
\tag{3.10}
\]

If \(J=I_1/D\), then

\[
J_{yy}=\frac{(I_1)_{yy}}D
-\frac{i(I_1)_y}{D^2}-\frac{I_1}{2D^3},
\tag{3.11}
\]

\[
J_{Ly}=\frac{(I_1)_{Ly}}D
-\frac{i(I_1)_L}{2D^2}
+\frac{i(I_1)_y}{D^2}+\frac{I_1}{D^3}.
\tag{3.12}
\]

Thus the radial part of the integrand in (1.1) is

\[
\begin{aligned}
J_{Ly}+tJ_{yy}
={}&\frac{(I_1)_{Ly}+t(I_1)_{yy}}D\\
&+\frac{-\frac i2(I_1)_L+i(1-t)(I_1)_y}{D^2}
+\left(1-\frac t2\right)\frac{I_1}{D^3},
\end{aligned}
\tag{3.13}
\]

equivalently

\[
(1-t)J_{vv}+\frac12J_{sv}.
\tag{3.14}
\]

Round 38 controls \(J\) and
\(\partial_\mu J|_\nu=(\partial_L+\partial_y)J=\frac i2J_s\), not
\(J_v,J_{vv},J_{sv}\). This is the next missing derivative coefficient
once the independent Cauchy term is separated.

Now audit that term. Write \(F_0(L)=H^\circ(L,L)=F(L,0)\) and
\(B=F_0/A\). Since

\[
\partial_\nu\Log D(L,\nu)=-\frac{i}{2D(L,\nu)},
\]

one has the pointwise primitive identity

\[
K_C(L,\nu)=\partial_\nu\{B(L)\Log D(L,\nu)\}.
\tag{3.15}
\]

This proves (1.4). Moreover, for large \(|\nu|\),

\[
|D(L,\nu)|\asymp|\nu|,
\qquad |K_C(L,\nu)|\asymp\frac{|B(L)|}{|\nu|},
\tag{3.16}
\]

which proves (1.3) and the failure of uniform absolute height
integrability.

At fixed \(\nu\), \(D_L=-i/2\). Therefore

\[
\partial_LK_C
=-\frac{iB'}{2D}+\frac{B}{4D^2}
=\partial_\nu\left\{
B'\Log D-\frac{iB}{2D}\right\}.
\tag{3.17}
\]

The \(D^{-2}\) term is absolutely integrable; the \(B'/D\) term is
another signed Cauchy/log primitive. For moving endpoints, exact
differentiation of (1.4) yields the interior derivative plus the two
Leibniz traces, so primitive value, variation, branch, and endpoint
ownership must be controlled as one object.

The remainder of the singular hard-top regularizer is

\[
\mathcal R_A[F](L,y)
=K_C(L,\nu)
+\frac{F(L,y)-F(L,0)}{yD(L,\nu)}.
\tag{3.18}
\]

Only this singular share may own the signed primitive. Smooth top
remainders and interior profiles retain their ordinary \(\mu=y\)
integral and \(\widehat\phi(v)\widehat W_j(u)/D\); they acquire no delta,
PV, logarithmic subtraction, or second Plemelj operation.

For a moving physical face \(\nu=\gamma(L)\), the corresponding trace is

\[
\frac d{dL}F(L,L-\gamma(L))
=F_L+(1-\gamma'(L))F_y.
\tag{3.19}
\]

Thus \(\nu=L\mp U\) has constant \(y=\pm U\), while fixed
\(\nu=\pm V\) uses \(F_L+F_y\). Common artificial ownership cancels mask
derivatives only after identical shares, domains, endpoint conventions,
and log branches are established. The exact normalized Morse remainder
and its induced traces remain separate; a scalar Fresnel multiplier is
insufficient.

## 4. First doubtful or unproved step

The first unsupported step is placing the independent diagonal
regularizer \(K_C\) under the absolute mixed norm. Equation (3.16) proves
that this is impossible on the full physical-height line unless
\(H^\circ(L,L)=0\). On a finite cutoff \(|\nu|\leq V\), the sharp loss is
\(\log V\); on cofinal height exhaustion it is infinite. A restriction
\(V\ll X\) would reduce it to a polylogarithmic loss, but would not prove
the required cutoff-independent limit.

The lawful alternative is the signed primitive (1.4), together with its
\(L\)-variation formula (3.17) and exact endpoint traces. The allowed
packet gives no target-scale estimate for \(B,B'\) and those traces, and
does not explicitly type this primitive outside (2.6). Consequently the
complete target is not proved.

After that ownership seam is repaired, (3.13)--(3.14) are the first
unsupported actual mixed derivatives. No fixed-cell \(X^\varepsilon\)
estimate for \(J_v,J_{vv},J_{sv}\), no exact connector/ownership
derivative formula, and no normalized Morse-remainder bound is supplied.
Round 38 has only fixed-\(X,b\) tail constants after global summation and
cannot fill this cellwise gap.

There is also a functional-analytic warning: the first operator in (1.1)
is a Hardy average and is not bounded on unweighted \(L^1(dy)\). The
\(D^{-1}\) decay, translated profiles, signed recombination, and moving
traces must remain together.

## 5. Required control test and outcome

1. **Exact phase-removed cell factorization — not passed from the packet.**
   External ownership and factor types are known, but the exact \(I_1\),
   connector, ownership, and normalized Morse formulas are absent.
2. **Fixed-\(\nu\) to \((L,y)\) conversion — passed.** Equations
   (3.1)--(3.2) give the physical derivative and diagonal derivative with
   the required signs.
3. **Second divided-difference identity — passed.** Equations
   (3.3)--(3.5) prove (1.1), including diagonal cancellation and both
   signs of \(y\).
4. **Independent diagonal Cauchy regularizer — failed as an absolute
   kernel, passed algebraically as a signed primitive.** Equations
   (3.15)--(3.17) give its exact finite-section and derivative primitives;
   (3.16) proves the sharp logarithmic absolute loss.
5. **Singular/smooth separation — passed algebraically.** Only the
   singular hard top may own (1.4); smooth shares remain ordinary
   \(\mu\)-integrals.
6. **Gamma/radial/profile mixed-derivative ledger — partial.** Equations
   (3.7)--(3.14) are exact; bounds for \(J_v,J_{vv},J_{sv}\) are absent.
7. **Moving faces, common ownership, and Morse remainder — not
   quantitatively testable.** Equation (3.19) fixes trace signs, but the
   actual formulas are not supplied.
8. **No aggregate \(\lambda\), closed-sum repetition, numerics, or web —
   passed.**

## 6. Dependencies and exact artifacts used

Campaign: m9-m1-beta-translation-divided-difference; task:
blind_translation_difference; role: statement-only blind rederiver; date:
2026-08-13. The proof-graph hash was deliberately unavailable under the
assigned isolation.

Only these artifacts were read:

- protocol.md;
- state/active_campaign.yml and the conductor's authoritative retraction
  restoring the fixed-physical-height formula;
- rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md;
- rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md;
- rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md;
- rounds/codex-managed/m9-m1-beta-translation-divided-difference/briefs/blind_translation_difference.md.

No Round-40 report, proof graph, proof draft, validation matrix, numerical
artifact, or external source was read. The conductor supplied only the
coordinate correction and the non-leading request to audit the independent
diagonal regularizer.

## 7. Recommended state effect

- **Promote as independent algebra:** the physical-height conversion
  (3.1)--(3.2), identity (1.1), factor-direction and rational ledgers
  (3.7)--(3.14), exact Cauchy/log primitives (3.15)--(3.17), and
  moving-face rule (3.19).
- **Reject:** placing \(K_C\) or its \(B'/D\) derivative tail in an
  absolute full-height mixed kernel. Their finite-cutoff loss is
  logarithmic and their cofinal absolute mass is infinite.
- **Revise before promotion:** split the exact signed primitive (1.4)
  from (2.6) and prove target-scale bounds for its value, \(L\)-variation,
  coherent log branch, and moving endpoint traces.
- **Retain open:** after that split, prove fixed-cell
  \(X^\varepsilon\) bounds for \(J_v,J_{vv},J_{sv}\), connector and
  common-ownership derivatives, both saddle entry/exit collars, and the
  exact normalized Morse remainder.
- **No change:** downstream coefficient/resonance summation and all
  obligations beyond the fixed-cell symbol interface.

# Round 146 conductor candidate: exact unmasking and three-variable dispersion no-go

- Campaign: m9-m1-lower-cone-three-variable-hessian-dispersion-gate
- Round: 146
- Role: conductor-selected proof kernel
- Starting graph SHA-256: 7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Result

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 \mathcal I_M=\mathbb N\cap[M,B_M),\qquad B_M\leq2M,
\]

where the inherited half-open blocks are disjoint and retain the literal
terminal truncation. Put

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),\qquad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 k_{s,t}=\left\lfloor t\sqrt{Ns}+\frac12\right\rfloor,\qquad
 j_{s,t}=k_{s,t}^2-Nst^2,
\]

and write each \(m\) uniquely as \(m=st^2\), with \(s\) squarefree.
Then \(k_m=k_{s,t}\).
Let the exact masked small-\(t\) scalar left by Round 145 be

\[
 \mathfrak S_N^{<,>}:=
 \sum_M\sum_{1\leq t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
 |j_{s,t}|>M^{3/4}}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns}).
\tag{146.C1}
\]

The inherited full cone scalar satisfies
\(\mathfrak T_N=\mathfrak S_N^{<,>}+
O_{\varepsilon,V}(X^\varepsilon)\) by the unmasked large-\(t\) owner.
The first new conclusion is the owner-complete two-step comparison

\[
\boxed{
 \mathfrak S_N^{<,>}=
 \mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon),\qquad
 \mathfrak T_N=
 \mathfrak S_N^{<,>}+O_{\varepsilon,V}(X^\varepsilon)
 =
 \mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon),}
\tag{146.C2}
\]

where

\[
\boxed{
 \mathfrak U_N^{<}:=
 \sum_M\sum_{1\leq t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns}).}
\tag{146.C3}
\]

The first equality in (146.C2) adds only the small-\(t\),
small-displacement subset of the already proved Round-144 absolute cell
owner. The second equality adds the separately proved unmasked
large-\(t\) owner. These are the second and third disjoint pieces of
the exact ambient partition below, so no accepted error is counted
twice. Equation (146.C3) is the sharper interface for the proposed
three-variable analysis.

The second conclusion is a scoped no-go. On a dyadic box

\[
 t\asymp T,\qquad d\asymp D,\qquad e\asymp E,
 \qquad T^2DE\asymp M,
\tag{146.C4}
\]

the phase \(f(t,d,e)=\sqrt N\,t\sqrt{de}\) has relative-coordinate
Hessian determinant \(1/4\). Nevertheless:

1. the exact amplitude is a joint discontinuous function of all three
   variables and does not satisfy the separated or smooth coefficient
   hypotheses of the audited theorems;
2. the mandatory \(t=1\) face returns the rank-one \(d,e\) product
   phase and has available weighted capacity \(M^{1/4+o(1)}\);
3. a coefficient-robust difference in \(t\) returns the same rank-one
   phase with an unproved coefficient correlation;
4. the full smooth stationary transform returns the same monomial at
   the phase level, while triangle inequality on the ideal dual aliases
   is far above target;
5. even after optimistically granting every missing coefficient and
   boundary separation, the strongest audited direct three-variable
   monomial bound leaves \(R^{1/16+\varepsilon}\) at the formal top
   endpoint on a balanced box.

Thus no target estimate and no strict fixed-power intermediate-\(t\)
reduction is proved. The round closes under

\[
\boxed{\mathsf{three\_variable\_dispersion\_no\_go}.}
\tag{146.C5}
\]

This is a no-go for the Hessian-only, coefficient-blind, direct-source,
or one-transform-followed-by-modulus mechanisms. It is not a lower
bound for the signed scalar and not a disproof of its target estimate.

## 2. Exact unmasking and coefficient interface

### 2.1 Disjoint owner partition

For integral \(t\), set \(T_M=\lceil M^{1/4}\rceil\) and
\(J_M=M^{3/4}\). The unmasked squarefree-kernel support is the exact
disjoint union

\[
\begin{aligned}
 \{t<T_M,\ |j_{s,t}|>J_M\}
 \ \dot\cup\
 \{t<T_M,\ |j_{s,t}|\leq J_M\}
 \ \dot\cup\
 \{t\geq T_M\}.
\end{aligned}
\tag{146.C6}
\]

Round 144 proved absolutely, after including its separate exact-radical
owner,

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |k_m^2-Nm|\leq M^{3/4}}}
 m^{-3/4}\left|V_{\rm low}(R^2m/N)C(m)\right|
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{146.C7}
\]

Restricting an absolute sum to \(t<T_M\) can only decrease it. Hence
the difference between (146.C1) and (146.C3) is target-safe. Round 145
independently proved the unmasked tail estimate

\[
 M^{-3/4}X^\varepsilon
 \sum_{t\geq T_M}\frac{M}{t^2}
 \ll X^\varepsilon
\tag{146.C8}
\]

per block. The \(O(\log X)\) inherited block count is absorbed by
epsilon renaming. Equations (146.C7) and (146.C8) are applied to the
second and third disjoint sets in (146.C6), respectively. Strict \(>\)
and complementary \(\leq\), the exact ceiling, exact radicals, the
profile, and all half-open endpoints are therefore accounted for.

### 2.2 Literal multiplicity-one coefficient

For ordered positive \(d,e\), define

\[
\begin{aligned}
 \kappa_t(d,e):={}&
 \mathbf 1_{\{\mu^2(de)=1\}}
 \mathbf 1_{\{e\ {\rm odd}\}}\chi_4(e)\\
 &\times
 \sum_{\substack{\gamma\mid t\\
 \mu^2(\gamma)=1,\ (\gamma,de)=1\\
 \gamma\ {\rm odd}}}\chi_4(\gamma)
 \sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
 eb^2>4da^2}}1.
\end{aligned}
\tag{146.C9}
\]

Then

\[
 \mathfrak U_N^{<}=
 \sum_M\sum_{1\leq t<T_M}\sum_{d,e\geq1}
 (t^2de)^{-3/4}V_{\rm low}(R^2t^2de/N)
 \mathbf 1_{\{t^2de\in\mathcal I_M\}}
 \kappa_t(d,e)e(\sqrt N\,t\sqrt{de}).
\tag{146.C10}
\]

The inverse map is

\[
 h=\gamma da^2,\qquad r=\gamma eb^2,\qquad
 s=de,\qquad t=\gamma ab.
\tag{146.C11}
\]

It is multiplicity one. The variables \(\gamma,d,e\) are pairwise
coprime and squarefree; \(\gamma,e,b\) are odd; no coprimality on
\(a,b\), or between them and \(\gamma\), may be inserted; and

\[
 \chi_4(r)=\chi_4(\gamma)\chi_4(e),\qquad
 r>4h\iff eb^2>4da^2.
\tag{146.C12}
\]

Equivalently, with \(G=(h,r)\),

\[
 \kappa_t(d,e)=\mathbf 1_{\{\mu^2(de)=1\}}
 \sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
 eb^2>4da^2}}\chi_4(Ge).
\tag{146.C13}
\]

Here \(G\) is not the squarefree \(\gamma\), and no extra coprimality
with \(G\) is legal. Finally,

\[
 |\kappa_t(d,e)|\leq\sum_{\gamma ab=t}1
 =\tau_3(t)\ll_\varepsilon t^\varepsilon.
\tag{146.C14}
\]

This pointwise envelope is lawful for absolute capacity, but it erases
the signs needed for the target.

## 3. Hessian, capacity, aspects, and short faces

On (146.C4), the number of triples is \(O(TDE)=O(M/T)\). From
(146.C14), the normalized box capacity is

\[
\boxed{
 |\mathfrak U_{M,T,D,E}|
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.}
\tag{146.C15}
\]

Thus \(T=M^\theta\), \(0\leq\theta<1/4\), still requires the signed
saving \(M^{1/4-\theta}\). Only
\(T\geq M^{1/4}/(\log X)^A\) is already epsilon-safe by this absolute
ledger; that is not a new fixed-power reduction.

For \(f(t,d,e)=\sqrt N\,t\sqrt{de}\), direct differentiation gives

\[
 f^{-1}\operatorname{diag}(t,d,e)\nabla^2f
 \operatorname{diag}(t,d,e)=
 \begin{pmatrix}
 0&1/2&1/2\\
 1/2&-1/4&1/4\\
 1/2&1/4&-1/4
 \end{pmatrix}.
\tag{146.C16}
\]

Its eigenvalues and determinants are

\[
 -\frac12,\quad \frac1{\sqrt2},\quad-\frac1{\sqrt2},\qquad
 \det(\text{scaled Hessian})=\frac14,
\tag{146.C17}
\]

\[
 \det\nabla^2f=\frac{f^3}{4t^2d^2e^2}.
\tag{146.C18}
\]

The nondegeneracy is exact and uniform in relative coordinates. It
does not survive every short face. If a summand in (146.C9) is nonzero,
then \(a/b\geq1/t\), so the cone gives

\[
 \frac ed>4\left(\frac ab\right)^2\geq\frac4{t^2},\qquad
 d^2<\frac m4,\qquad e^2>\frac{4m}{t^4},
 \quad m=t^2de.
\tag{146.C19}
\]

Consequently

\[
 D\ll\sqrt M,\qquad E\gg\frac{\sqrt M}{T^2}.
\tag{146.C20}
\]

The exact face ledger is:

- \(t=1\) is mandatory and

  \[
   \kappa_1(d,e)=
   \mathbf 1_{\{\mu^2(de)=1\}}
   \mathbf 1_{\{e\ {\rm odd}\}}\chi_4(e)
   \mathbf 1_{\{e>4d\}}.
  \tag{146.C21}
  \]

  Freezing \(t\) leaves the scaled \(d,e\) Hessian
  \(\bigl(\begin{smallmatrix}-1/4&1/4\\1/4&-1/4\end{smallmatrix}\bigr)\),
  of determinant zero. Its available top-block capacity is
  \(R^{1/2+o(1)}\).
- \(D=1\) is not excluded by the cone and is structurally present;
  the exact \(t=d=1,e=p>4\) prime corner has
  \(C(p)=\chi_4(p)\neq0\). For growing \(t\), this is at best a
  separate two-variable \(t,e\) problem. No assertion is made that
  every clipped block has a nonzero net coefficient.
- \(E=1\) is empty: (146.C19) would imply \(t^4>4m\geq4M\), contrary
  to \(t^4<M\).
- Fixed bounded \(E\) forces
  \(t>\sqrt2M^{1/4}/\sqrt e\), hence lies in a terminal target-safe
  \(T\)-shell. This does not dispose of a growing short-\(E\) range.
- On each exact product level the phase is constant. It is
  \(\sqrt{NM}\) on the active lower boundary \(t^2de=M\); the formal
  upper boundary \(t^2de=B_M\) is excluded from this half-open block
  and would have phase \(\sqrt{NB_M}\) if assigned elsewhere. A single
  actual integer product layer is target-safe, but a wide radial collar
  is not free.
- Cone equality is empty because \(e,b\) are odd. A fixed
  lattice-width cone collar is target-safe; a relative-width collar is
  not automatically safe.

These controls rule out the inference that all three side lengths grow
or that the short faces may be discarded absolutely.

## 4. Why the new Hessian direction does not close

### 4.1 Coefficient-blindness is impossible

A theorem uniform for every array \(|u_{t,d,e}|\leq1\) cannot gain from
this phase: on any finite support, choosing

\[
 u_{t,d,e}=e(-f(t,d,e))
\]

makes the exponential sum equal its cardinality. This is only a
control on a proposed theorem class; it is not a model for the actual
real arithmetic coefficient. A valid estimate must use the exact
character, squarefree, coprimality, factor-count, and cone structure.

### 4.2 A \(t\)-difference returns the rank-one phase

With the literal amplitude zero-extended in \(t\),

\[
 \left|\sum_t A_{t,d,e}e(\sqrt N\,t\sqrt{de})\right|^2
 =\sum_{h\in\mathbb Z}e(\sqrt N\,h\sqrt{de})
 \sum_tA_{t+h,d,e}\overline{A_{t,d,e}}.
\tag{146.C22}
\]

The \(h=0\) term is the constant-phase diagonal. For every
\(h\neq0\), the returned \(d,e\) phase has the singular scaled Hessian
from the \(t=1\) face. The inner sum retains two exact factor counts,
two cones, and their squarefree/coprimality and endpoint correlations.
No accepted estimate saves a power in this correlation; bounding it
absolutely returns the primal capacity.

### 4.3 Full stationary transform is a phase-level self-return

For the ideal smooth bare phase \(c\,t\sqrt{de}\), \(c=\sqrt N>0\),
the critical point for \(c\,t\sqrt{de}-ut-vd-we\), in the positive
alias orthant, is

\[
 t_*=\frac{2\sqrt{vw}}c,\qquad
 d_*=\frac uc\sqrt{\frac wv},\qquad
 e_*=\frac uc\sqrt{\frac vw},
\tag{146.C23}
\]

with critical value

\[
 -\frac{2u\sqrt{vw}}c.
\tag{146.C24}
\]

Put \(F=\sqrt{NM}\) and \(V_3=TDE\asymp M/T\). The ideal smooth
gradient-image volume is \(\asymp F^3/V_3\). In the smooth interior
model, all three dual lengths are long and the elementary bounding-box
count gives

\[
 \#\{\text{supported aliases}\}
 \ll
 \left(1+\frac FT\right)
 \left(1+\frac FD\right)
 \left(1+\frac FE\right)
 \ll\frac{F^3}{V_3}.
\tag{146.C25a}
\]

An asymptotic count would still require a boundary-lattice estimate.
One stationary integral has size

\[
 |\det\nabla^2f|^{-1/2}\asymp\frac{V_3}{F^{3/2}}.
\tag{146.C25}
\]

Triangle inequality on the ideal transformed main sum therefore has
upper price \(F^{3/2}\). After the physical weight \(M^{-3/4}\), this
is \(N^{3/4}\), not a saving. The coefficient map

\[
 c\longmapsto-\frac2c\longmapsto c
\tag{146.C26}
\]

is an involution only at the phase-monomial level after reversing the
alias orthant on the second transform. It is not a two-step identity
for amplitudes: Maslov factors, transformed coefficients, boundaries,
and short faces remain. Thus a signed dual-alias theorem could still
help, but nonzero Hessian plus modulus does not.

### 4.4 Exceptional frequency control

For squarefree \(s>1\), let \(N=X=sL^2+1\). Then

\[
 \sqrt{Ns}=sL+\rho,\qquad
 \rho=\frac1{\sqrt{L^2+1/s}+L}.
\]

While \(t\rho<1/2\),

\[
 k_{s,t}=sLt,\qquad j_{s,t}=-st^2,
 \qquad e(t\sqrt{Ns})=e(t\rho).
\tag{146.C27}
\]

With \(L=s\), a literal small-\(t\), flat-profile range survives and
\(t\rho\to0\) uniformly. Although the mask is no longer part of the
active amplitude, this family remains a valid control: the original
large-displacement condition did not imply a uniform modular
derivative gap, dual separation, or bounded partial quotient. It is
not a signed lower bound.

## 5. Primary-source and power audit

The strongest directly relevant primary card is Cao--Zhai, Theorem 6
in [Multiple exponential sums with monomials](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9231.pdf).
It estimates

\[
 \sum_{m\sim M_0}\sum_{m_1\sim M_1}\sum_{m_2\sim M_2}
 a(m)b(m_1,m_2)e(A m^\alpha m_1^\beta m_2^\gamma),
\]

under

\[
 M_0,M_1,M_2\geq1,\qquad A\neq0,\qquad
 |a(m)|\leq1,\qquad |b(m_1,m_2)|\leq1,
\]

\[
 \alpha(\alpha-1)(\alpha-2)(\alpha-3)
 \gamma(\gamma-1)\neq0,
 \qquad F=|A|M_0^\alpha M_1^\beta M_2^\gamma\gg M_0,
\]

with one separated coefficient \(a(m)\) and one joint coefficient
\(b(m_1,m_2)\). Up to swapping \(d,e\), the only legal placement is

\[
 (m,m_1,m_2)=(d,t,e),\qquad
 (\alpha,\beta,\gamma)=\left(\frac12,1,\frac12\right),
\tag{146.C28}
\]

because the linear \(t\)-exponent is excluded from the \(\alpha\) and
\(\gamma\) slots. The phase, fixed center, individual positive
direction, and scale \(F=\sqrt{NM}\) pass. Indeed
\(D\leq M\ll_VR^2\) and \(\sqrt N\asymp R^2\), so
\(F/D\geq\sqrt{N/M}\gg_V1\). The exact coefficient does not split as
\(a(d)b(t,e)\); proving an \(R^\varepsilon\)-norm
superposition of such tensors, including every cone and endpoint
owner, is itself open.

There is an independent power obstruction even if this missing
separation is granted. On the balanced top box

\[
 M\asymp R^2,\qquad T=R^\tau,\qquad
 D=E=R^{1-\tau},\qquad 0\leq\tau<\frac12,
\tag{146.C29}
\]

the theorem's fourteen displayed contributions, after the compulsory
weight \(R^{-3/2}\), have exponents

\[
\begin{aligned}
 &\frac38-\frac{5\tau}8,\quad
 \frac38-\tau,\quad
 \frac{11}{29}-\frac{43\tau}{58},\quad
 \frac{41}{108}-\frac{41\tau}{54},\\
 &\frac{37}{98}-\frac{37\tau}{49},\quad
 \frac{11}{29}-\frac{23\tau}{29},\quad
 \frac{127}{336}-\frac{125\tau}{168},\quad
 \frac{115}{304}-\frac{115\tau}{152},\\
 &\frac{127}{336}-\frac{131\tau}{168},\quad
 \frac{33}{100}-\frac{181\tau}{200},\quad
 \frac{123}{368}-\frac{167\tau}{184},\\
 &\frac{33}{100}-\frac{19\tau}{20},\quad
 \frac13-\frac{5\tau}{6},\quad
 \frac14-\frac{9\tau}{8}.
\end{aligned}
\tag{146.C30}
\]

The first term is

\[
 R^{-3/2}(F D^5T^7E^7)^{1/8}
 =R^{3/8-5\tau/8}.
\tag{146.C31}
\]

It would be target-sized only for \(\tau\geq3/5\), outside the
small-\(t\) range. At the formal endpoint \(\tau=1/2\) it is still
\(R^{1/16}\). The trivial price \(R^{1/2-\tau}\) is target-safe only
in the already discharged terminal shell. Thus the direct theorem,
even under ideal coefficient separation, creates no new fixed-power
balanced corridor. This is a limitation of the displayed upper bound,
not a lower bound for the scalar.

The remaining primary cards are consistent with this no-go:

- Robert--Sargos, [Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
  assumes positive integer side lengths, phase scale
  \(\mathcal X>1\), bounded coefficients \(a(h,n),b(m)\), and
  \(\alpha(\alpha-1)\beta\gamma\neq0\). The exact placement is
  \[
   (h,n,m)=(t,e,d),\qquad
   (\beta,\gamma,\alpha)=(1,1/2,1/2),\qquad
   (H,N_0,M_0)=(T,E,D),\qquad \mathcal X=F.
  \]
  It accepts only \(a(t,e)b(d)\) and leaves
  \(R^{1/2-\tau/2+\varepsilon}\), hence \(R^{1/4+\varepsilon}\)
  at the formal endpoint.
- Sargos--Wu, Theorem 9 in
  [Multiple exponential sums with monomials and their applications in number theory](https://doi.org/10.1023/A:1006777803163),
  assumes \(Z>0\), separated bounded coefficients, and
  \(\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\neq0\).
  It applies only after freezing \(t\), with
  \[
   (m,n)=(d,e),\qquad(\alpha,\beta)=(1/2,1/2),\qquad
   (M_1,N_1)=(D,E),\qquad Z=F.
  \]
  It leaves
  \(R^{2/5-3\tau/10+\varepsilon}\), again
  \(R^{1/4+\varepsilon}\) at the formal endpoint.
- Sargos's [multidimensional van der Corput transformation](https://doi.org/10.7169/facm/2015.52.1.11)
  assumes fixed dimension \(p>1\), \(k>p+5\),
  \(\mathcal T,M_1,\ldots,M_p>1\), a connected bounded open
  \(\Omega\), a \(C^k\) phase, and a compactly supported \(C^k\)
  amplitude with controlled derivatives and support separated from
  \(\Omega^c\), together with a Hessian determinant bounded away from
  zero and an injective gradient. For the target phase one chooses a
  compact positive box inside such an \(\Omega\); the smooth phase
  hypotheses then pass. The theorem does not accept the arithmetic
  coefficient. Its exact dual phase is (146.C24), and triangle
  inequality on the ideal dual main sum has the adverse price recorded
  in (146.C25a)--(146.C25).
- Li--Ma's [constant-perturbation theorem](https://arxiv.org/abs/2302.05870)
  is for a reciprocal perturbed phase and separated coefficients; at
  zero perturbation its authors point back to Robert--Sargos.
- Pliego's [2024 estimate](https://www.numdam.org/item/10.5802/jtnb.1294.pdf)
  is for a prescribed weighted curved domain and a different exponent
  pattern, not an arbitrary coefficient-weighted positive monomial box.

Cao--Zhai Theorem 7 was also checked. It assumes positive side lengths,
\(A>0\), bounded separated coefficients \(a(m_1)b(m_2)\), and
\(\alpha\beta/(\alpha-1)\notin\{0,1,2,\ldots\}\). The placement
(146.C28) passes this phase condition because the ratio is \(-1\), but
the theorem has no coefficient in the distinguished \(d\)-variable and
would require the remainder to split as \(a(t)b(e)\). Even after ideal
separation, its second well-defined displayed term

\[
 R^{-3/2}(F^4T^7E^7)^{1/8}=R^{7/8}
\]

on (146.C29) is independent of \(\tau\). Its final printed term contains
undefined symbols in that theorem; only that last term is
source-inconclusive. No conclusion here depends on it.

## 6. First open estimate and owner scope

The exact first open estimate is now

\[
\boxed{
 \mathfrak U_N^{<}\ll_{\varepsilon,V}X^\varepsilon,}
\tag{146.C32}
\]

with \(\mathfrak U_N^{<}\) defined by (146.C3), equivalently by the
literal coefficient expansion (146.C9)--(146.C10). The nearest-square
mask is no longer an amplitude hypothesis. The squarefree and
coprimality support, factor multiplicity, parity, character, strict
cone, product profile, half-open endpoints, and individual positive
direction remain literal.

Any route that owns \(t=1\) separately must prove a uniform prefix
estimate of the following strength:

\[
 \sup_{M\leq U\leq B_M}
 \left|
 \sum_{\substack{M\leq s<U\\s\ {\rm squarefree}}}
 V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})
 \right|
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\tag{146.C33}
\]

uniformly in the inherited prefixes, with the harmless \(s^{-3/4}\)
restored by partial summation. No reviewed proof or source supplies
this separate face estimate. A stronger joint theorem could instead
use cancellation between \(t\)-layers. Any future route must prove a
genuinely sign-sensitive correlation or dual-coefficient theorem for
the exact amplitude, while owning the bounded-\(t\) and other short
faces rather than discarding them.

The independent Round-138 collar-tail cross owner is unchanged. This
round proves neither the complete lower-radial estimate, lower GAR,
either direct M1 parent, M9-M1, any M2 owner, M9-M2, endpoint
uniformity, M9, the conditional bridge, nor the quarter theorem. The
internally proved global exponent remains \(1/3\); the separately
audited external exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{146.C34}
\]

## 7. Required controls and recommended state effect

The proof kernel has the following control outcomes.

1. **Exact coefficient and multiplicity: GREEN.** Equations
   (146.C9)--(146.C14) retain both parametrizations, all parity and
   coprimality data, and multiplicity one.
2. **Mask, profile, and endpoints: GREEN with exact scope.** The mask
   alone is removed by (146.C6)--(146.C8); the profile, product
   staircase, strict cone, clipped dyadic boxes, and terminal endpoint
   remain.
3. **Hessian and aspect ratios: GREEN.** Equations
   (146.C16)--(146.C20) verify the determinant and every required scale.
4. **Short faces: adverse but owned.** The \(t=1\) and \(D=1\) faces
   remain mandatory; \(E=1\) is empty and fixed bounded \(E\) is
   terminal-safe.
5. **Difference and dual transforms: adverse controls.** The
   \(t\)-difference returns a rank-one phase for \(h\neq0\); the full
   transform is only a phase-level involution after orthant reversal,
   and aliaswise modulus is far above target.
6. **Primary sources and powers: GREEN as a no-go.** The exact
   coefficient fails every audited class, and the complete favorable
   Cao--Zhai ledger retains a fixed positive power.
7. **Direction and exceptions: GREEN.** All calculations preserve
   \(e(+f)\) at fixed \(N=\lfloor X\rfloor\); the slow family is used
   only to prohibit a false uniform separation inference.
8. **Owner scope: GREEN.** No independent cross, M1, M2, endpoint,
   M9, bridge, target, or exponent owner is promoted.

Subject to final seam review, the recommended graph effect is:

- create a proved unmasking reduction recording (146.C2)--(146.C8),
  depending on and restating the accepted Round-145 coefficient
  interface (146.C9)--(146.C14);
- create a scoped three-variable dispersion obstruction recording the
  exact Hessian, capacity, short faces, difference return, phase-level
  Legendre return, source coefficient mismatch, and Cao--Zhai power
  loss;
- update the Round-145 squarefree reduction and global lower-radial
  owner so that the first open scalar is (146.C32), without the
  nearest-square mask;
- reject determinant-only cancellation, arbitrary-coefficient or
  smooth-tensor substitution, three-long-side disposal of the short
  faces, direct use of the audited monomial estimates, and
  transform-followed-by-modulus as target proofs;
- make no downstream theorem or exponent change.

# Round 96 analytic report: primitive-ray \(q\)-dispersion attack

## 1. Result

**Result: exact equal-capacity self-return and a sharp no-go for bare
\(q\)-dispersion.** Write

\[
 a=m-q,\qquad b=m+q,\qquad r=\sqrt{m^2-q^2}.
\]

On the primitive odd lattice one has exactly

\[
 m\not\equiv q\pmod 2,\qquad (m,q)=1,\qquad
 \Lambda=X(m-r),\qquad \chi _4(a)\chi _4(b)=(-1)^q.
\]

There are two inequivalent meanings of a \(q\)-shift.

- At fixed \(m\), zero extension to the full \(q\)-lattice shows that
  every nonzero correlation has shift \(q\mapsto q+2s\). Consequently
  its character correlation is
  \((-1)^q(-1)^{q+2s}=1\). Odd shifts are identically zero. Thus the
  fixed-\(m\) A-process sees the genuine fixed-variable curvature
  \(|\phi_{qq}|\asymp gJD/A^2\), but it has already lost every bit of
  the \(\chi _4\) sign.
- A genuine sign-changing cross-ray shift may be made at fixed \(a\):
  \((m,q)\mapsto(m+s,q+s)\), equivalently \(b\mapsto b+2s\). Its
  character correlation is \((-1)^s\). For the complete actual
  coefficient, however, its exact Fejer dispersion is a Gram lift of
  the original half-frequency row. Fourier transform in the shift gives
  the squared modulus of that same row at frequency \(1/2\); applying
  the adjoint reciprocal transform then gives the Round-80 residual
  transposed two-character row. It is not a new operator.

The block capacity ledger is sharp. If

\[
 T=L^2X^\varepsilon,\qquad
 P=T\sqrt\rho,\qquad \rho={AJD^3\over L^3},
\]

then a length-\(H\) \(q\)-dispersion has diagonal contribution of squared
capacity \(P^2/H\). Since \(H\ll D\), its best formal linear gain is only
\(D^{-1/2}\), whereas the target needs \(\rho^{-1/2}\). Even the diagonal
can be declared target-safe only in the capacity-feasible wedge
\(\rho\ll D\), equivalently \(AJD^2\ll L^3\). This does **not** prove that
wedge, because the complete off-shift Gram remains unbounded. In
particular, the hard \(D\asymp1\) near-square/Pell blocks can have
\(\rho\to\infty\) and admit no \(q\)-length gain at all.

Thus no canonical bound and no nonempty hard subrange are proved. What
is proved is a method-level no-go: parity, one A-process, coefficientwise
Cauchy, and a second transform return the positive capacity
\(L^2X^\varepsilon\sqrt\rho\). The first strict survivor is the
complete-symbol, fixed-\(a\), off-shift determinant correlation stated
in Section 4; it needs a genuinely new signed estimate of strength
\(\rho^{-1}\) at Gram level.

## 2. Exact statement and hypotheses

Use exactly the residual dyadic block of the Round-96 packet. In
particular, primitive square rays, exact nonsquare centres,
\(\rho\ll1\), all endpoint/collar/original-Poisson owners, and all other
previous owners have already been removed. No assertion below restores
one of those sets.

The lattice identities are

\[
 a,b\text{ odd}
 \Longleftrightarrow m\not\equiv q\pmod2,
 \qquad
 (a,b)=(m,q),
 \tag{2.1}
\]

where the gcd equality uses that \(m-q\) is odd, and

\[
 0<q<{3m\over5},\qquad
 u={q\over m+r},\qquad qu=m-r,
 \qquad \Lambda=Xqu=X(m-r).
 \tag{2.2}
\]

For fixed \(a\), put \(b_q=a+2q\), \(m_q=a+q\), and

\[
 \Lambda_{a,q}=X\bigl(a+q-\sqrt{a(a+2q)}\bigr).
 \tag{2.3}
\]

The literal moving reciprocal interval is

\[
 I_{a,q}=\left(
 {J(\sqrt{a+2q}-\sqrt a)\over2\sqrt a},
 {J(\sqrt{a+2q}-\sqrt a)\over\sqrt{a+2q}}
 \right).
 \tag{2.4}
\]

Let \({\bf r}_{a,q}\) be the exact zero-one residual-block indicator. It
includes \(a\asymp A\), \(2q\asymp D\), \((a,q)=1\), the opposite-parity
lattice, nonsquare and noncentre restrictions, \(\rho\gg1\), all actual
dyadic cutoffs, and every previous owner complement. Define, with zero
extension in \(q\),

\[
 \begin{split}
 F_a(q)={}&{\bf r}_{a,q}
 \sum_{g\in\mathcal G_{a,a+2q}}
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 \omega(k)W_R(\Lambda_{a,q}/k)
 \mathfrak C^\circ_{a,a+2q,k}(g),\\
 \mathfrak C^\circ_{a,b,k}(g)={}&
 \int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)\,dx.
 \end{split}
 \tag{2.5}
\]

Thus all profiles, floors, stars, finite lift endpoints, saddle
entry/exit conventions, and the complete metric density plus discrepancy
coefficient are inside \(F_a(q)\). The oriented block is exactly

\[
 \mathfrak Q_{A,D,K,G,R}=\sum_a\sum_q(-1)^qF_a(q).
 \tag{2.6}
\]

The conjugate orientation is the conjugate of the same identity; the
accepted outer \(2\Re\) is applied once after (2.6).

For every odd integer \(s\), zero extension gives the exact first
difference identity

\[
 2\sum_q(-1)^qF_a(q)
 =\sum_q(-1)^q\bigl(F_a(q)-F_a(q-s)\bigr).
 \tag{2.7}
\]

For an integer \(H\ge1\), define

\[
 \begin{split}
 \mathcal C_s^{\rm act}
   &=\sum_a\sum_qF_a(q+s)\overline{F_a(q)},\\
 \mathcal G_H^{\rm act}
   &=\sum_a\sum_n\left|
       \sum_{0\le h<H}(-1)^hF_a(n+h)
     \right|^2.
 \end{split}
 \tag{2.8}
\]

Then the exact actual-symbol dispersion identity is

\[
 \boxed{
 \mathcal G_H^{\rm act}
 =H\mathcal C_0^{\rm act}
  +2\Re\sum_{1\le s<H}(H-s)(-1)^s
       \mathcal C_s^{\rm act}.}
 \tag{2.9}
\]

The literal correlation on the right is

\[
\begin{split}
 \mathcal C_s^{\rm act}
 ={}&\sum_{a,q}{\bf r}_{a,q+s}{\bf r}_{a,q}
 \sum_{\substack{g'\in\mathcal G_{a,a+2q+2s},\;
                  k'\in I_{a,q+s}\cap\mathbb Z\\
                  g \in\mathcal G_{a,a+2q},\;
                  k \in I_{a,q}\cap\mathbb Z}}
 \omega(k')\overline{\omega(k)}\\
 &\quad\times
 W_R(\Lambda_{a,q+s}/k')
 \overline{W_R(\Lambda_{a,q}/k)}
 \mathfrak C^\circ_{a,a+2q+2s,k'}(g')
 \overline{\mathfrak C^\circ_{a,a+2q,k}(g)}.
\end{split}
 \tag{2.10}
\]

In particular, (2.10) has both density-discrepancy cross terms and the
density-density term if it is later Fourier-expanded; none has been
discarded here. Since there are \(O(A(D+H))\) nonzero window bases
\((a,n)\), Cauchy gives the exact dispersion inequality

\[
 H^2|\mathfrak Q_{A,D,K,G,R}|^2
 \ll A(D+H)\mathcal G_H^{\rm act}.
 \tag{2.11}
\]

At fixed \(m\), if \(\widetilde F_m(q)\) denotes the same complete
coefficient, then

\[
 \widetilde F_m(q+s)\overline{\widetilde F_m(q)}=0
 \quad(s\text{ odd}),
 \qquad
 (-1)^{q+s}(-1)^q=1
 \quad(s\text{ even}).
 \tag{2.12}
\]

Equation (2.12), rather than pointwise informal alternation, is the exact
fixed-centre parity law.

For completeness, the unrestricted cross-centre version requested by
the packet is obtained by writing the same oriented summand as
\(F_m(q)\), zero-extended on the primitive lattice, and setting
\(B(q)=\sum_mF_m(q)\). Then

\[
 \mathfrak Q=\sum_q(-1)^qB(q),\qquad
 \mathcal C_s^{\rm gen}
 =\sum_q\sum_{m,m'}F_{m'}(q+s)\overline{F_m(q)}.
 \tag{2.13}
\]

Every tuple in (2.13) is literally of the form
\((m,q,k,g)\leftrightarrow(m',q+s,k',g')\), with its two independent
moving intervals and complete coefficients. Its signed correlation
factor is \((-1)^s=(-1)^{m'-m}\). The fixed-\(a\) identity (2.10) is the
structured subcase \(m'=m+s\); it is the first version in which a
transverse determinant can even be named.

## 3. Proof or derivation

For (2.1),
\((a,b)=(m-q,m+q)=(m-q,2q)\). Since \(m-q\) is odd, the factor \(2\)
may be deleted, and \((m-q,q)=(m,q)\). Also \(m+q=b\) is odd, so \(m\)
and \(q\) have opposite parity. Finally

\[
 \chi _4(a)\chi _4(b)
 =(-1)^{(a+b-2)/2}=(-1)^{m-1}=(-1)^q.
\]

The identity \(qu=m-r\) follows by multiplying numerator and
denominator by \(m-r\). This proves (2.2)-(2.3), and (2.4) is the
literal packet interval after substituting \(b=a+2q\).

At fixed \(m\), the admissible set is one residue class modulo \(2\).
Hence an A-process shift inside that fibre is \(q\mapsto q+2s\), and
the character product is \(1\). If instead \(a\) is fixed, then

\[
 (m,q)=(a+q,q)\longmapsto(a+q+s,q+s),
\]

so every integer \(s\) is permitted before the primitive and support
masks are imposed, and the character product is \((-1)^s\). This proves
the parity assertions in (2.7) and (2.12). Notice also that for two
general admissible pairs \((m,q)\) and \((m',q+s)\), parity forces
\((-1)^s=(-1)^{m'-m}\): a general cross-ray dispersion merely transfers
the mod-two character to the centre difference.

The unrestricted correlation (2.13) is no easier: its zero shift
\(\sum_q|B(q)|^2\) already contains all unowned \(m\ne m'\) cross-centre
pairs. Fourier transform in \(s\) gives \(|\widehat B(\theta)|^2\), and
\(\widehat B(1/2)=\mathfrak Q\). Thus general \(m,m'\) dispersion is an
even larger exact Gram self-return. Cauchy by the fixed primitive
endpoint \(a\) yields (2.10), removes those arbitrary cross-centre pairs,
and isolates the sharpest smaller correlation considered here.

To retain entry and exit exactly, let \(\Gamma_{a,q}\) be the finite set
of actual \((g,k)\) in (2.5), empty when \({\bf r}_{a,q}=0\), and let
\(T_{a,q}(g,k)\) be its complete summand. Then, without matching moving
endpoints by fiat,

\[
\begin{split}
 F_a(q+s)-F_a(q)
 ={}&\sum_{\Gamma_{a,q+s}\cap\Gamma_{a,q}}
       \bigl(T_{a,q+s}(g,k)-T_{a,q}(g,k)\bigr)\\
 &+\sum_{\Gamma_{a,q+s}\setminus\Gamma_{a,q}}T_{a,q+s}(g,k)
  -\sum_{\Gamma_{a,q}\setminus\Gamma_{a,q+s}}T_{a,q}(g,k).
\end{split}
 \tag{3.1}
\]

The last two sums are the literal lift, reciprocal-interval, dyadic,
owner-boundary, and saddle entry/exit samples. On the intersection the
difference is the indivisible quantity

\[
 W_R(\Lambda_{a,q+s}/k)\mathfrak C^\circ_{a,a+2q+2s,k}(g)
 -W_R(\Lambda_{a,q}/k)\mathfrak C^\circ_{a,a+2q,k}(g),
 \tag{3.2}
\]

so (3.1) cannot lawfully be replaced by discrepancy variation alone.

For (2.9), expand the square in (2.8), put \(s=h'-h\), and count the
\(H-|s|\) pairs with that difference. For (2.11), zero extension gives

\[
 H\mathfrak Q
 =\sum_{a,n}(-1)^n
   \sum_{0\le h<H}(-1)^hF_a(n+h),
\]

and Cauchy over the \(O(A(D+H))\) pairs \((a,n)\) proves the claim.

The self-return is exact. With
\(\widehat F_a(\theta)=\sum_qF_a(q)e(q\theta)\), correlation Fourier
inversion gives

\[
 \sum_{s\in\mathbb Z}\mathcal C_{a,s}^{\rm act}e(s\theta)
 =|\widehat F_a(\theta)|^2,
 \qquad
 \widehat F_a(1/2)=\sum_q(-1)^qF_a(q).
 \tag{3.3}
\]

Equivalently,

\[
 \mathcal G_H^{\rm act}
 =\sum_a\int_{\mathbb T}
 |D_H(\theta-1/2)|^2|\widehat F_a(\theta)|^2\,d\theta.
 \tag{3.4}
\]

Thus the \((-1)^s\) in (2.9) is exactly a Fejer localization at the
original character frequency \(1/2\). A second transform in \(s\)
produces the Gram square of the same row, not a new determinant sum.
At \(\theta=1/2\), (2.5) and (3.3) restore
\((-1)^q=\chi _4(ga)\chi _4(gb)\); adjoint reciprocal Poisson is then
exactly the Round-80 transposed two-character return.

The phase audit reaches the same warning, but does not assume the
conclusion. After \(x=gy\), the exact phase in (2.5) is

\[
 \phi_{g,k}(m,q,y)
 =g\{ky-J\delta(m,q)\sqrt y\},
 \qquad
 \delta=\sqrt{m+q}-\sqrt{m-q}.
 \tag{3.5}
\]

At fixed \(y\asymp A\),

\[
 \delta_{qq}={1\over4}\{(m-q)^{-3/2}-(m+q)^{-3/2}\},
 \qquad |\phi_{qq}|\asymp {gJD\over A^2}.
 \tag{3.6}
\]

Moreover

\[
 \nabla^2_{m,q}\delta={1\over4}
 \begin{pmatrix}
 a^{-3/2}-b^{-3/2}&-(a^{-3/2}+b^{-3/2})\\
 -(a^{-3/2}+b^{-3/2})&a^{-3/2}-b^{-3/2}
 \end{pmatrix},
 \quad
 \det\nabla^2_{m,q}\delta=-{1\over4(ab)^{3/2}}.
 \tag{3.7}
\]

So the fixed-\(y\) two-variable Hessian is genuinely nonsingular.
Nevertheless

\[
 \phi_{g,k}(\lambda m,\lambda q,\lambda y)
 =\lambda\phi_{g,k}(m,q,y),
\]

and Euler differentiation gives
\(\nabla^2_{m,q,y}\phi\,(m,q,y)^t=0\).
The full three-variable Hessian has an exact radial null direction.
At the exact \(y\)-stationary point,

\[
 y_*={X\delta^2\over4k^2},
 \qquad
 \phi(m,q,y_*)=-{g\Lambda\over2k},
 \tag{3.8}
\]

and

\[
 \nabla^2_{m,q}\Lambda={X\over r^3}
 \begin{pmatrix}q^2&-mq\\-mq&m^2\end{pmatrix},
 \qquad
 \det\nabla^2_{m,q}\Lambda=0,
 \qquad
 \nabla^2\Lambda\,(m,q)^t=0.
 \tag{3.9}
\]

Primitivity removes distinct exact integral multiples of one ray, so
(3.9) alone is not a proof that every transverse estimate fails. It is
an exact proof that one may not import the fixed-\(y\) determinant (3.7)
as a uniform determinant for the integrated actual symbol; the Schur
complement has the radial null direction (3.9).

It remains to verify capacity. The accepted nonsquare positive ledger
has per-ray envelope

\[
 M_0\ll_\varepsilon X^\varepsilon K
 {A\sqrt G\over\sqrt{JD}}
 \asymp X^\varepsilon\sqrt{GJD}.
 \tag{3.10}
\]

There are \(N\asymp AD\) ray slots. Hence

\[
 P=NM_0\asymp_{X^\varepsilon}AD\sqrt{GJD}
 =L^2X^\varepsilon\sqrt\rho,
 \qquad
 E_0:=NM_0^2\asymp_{X^\varepsilon}AGJD^2=LJD^2.
 \tag{3.11}
\]

For \(H\ll D\), the diagonal \(H\mathcal C_0\) in (2.9), estimated by
this accepted envelope, contributes through (2.11)

\[
 {AD\over H^2}\,HE_0={P^2\over H}.
 \tag{3.12}
\]

The target is \(T^2=P^2/\rho\). Therefore a separately estimated
diagonal requires \(H\gg\rho\); since \(H\ll D\), this is possible only
if \(\rho\ll D\). A collection of \(S\) shifts estimated individually
by \(|\mathcal C_s|\le E_0\) costs \(P^2S/H\), so at the maximal choice
\(H\asymp D\) only \(S\ll D/\rho\) shifts are termwise target-safe.
Estimating all shifts by Cauchy gives
\(\mathcal G_H\ll H^2E_0\), and (2.11) returns exactly \(P^2\). Thus the
linear capacity stays \(P\): the Gram gap is \(\rho\), whose square root
is the original \(\sqrt\rho\) gap.

## 4. First doubtful or unproved step

The first unproved step is not the lattice algebra, the moving endpoint
identity, or the fixed-variable curvature. It is the following actual-
symbol half-frequency Gram estimate for some \(1\le H\ll D\):

\[
 \boxed{
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon{H^2\over\rho}E_0.}
 \tag{4.1}
\]

If the diagonal is to be owned separately, (4.1) first requires
\(\rho\ll H\ll D\). The range \(1<\rho\ll D\) is therefore only a
capacity-compatible wedge, not a proved hard subrange. When
\(\rho\gg D\), including \(D\asymp1\) hard blocks, even the proposed
diagonal/low-shift owner strategy has no admissible \(H\).

The first genuinely smaller analytic object inside (4.1) is (2.10)
with \(s\ne0\), kept with its Fejer sign and with
\(W_R(t')\overline{W_R(t)}\) unexpanded. The exact stationary reduction
diagnoses its transverse determinant. Along fixed \(a\),

\[
 {d^2\Lambda_{a,q}\over dq^2}
 ={X\sqrt a\over(a+2q)^{3/2}},
\]

so a \((g,k)\)--\((g',k')\) correlation at shift \(s\) has reduced
second derivative

\[
 \Psi_s''(q)=-{X\sqrt a\over2}
 \left\{
 {g'\over k'(a+2q+2s)^{3/2}}
 -{g\over k(a+2q)^{3/2}}
 \right\}.
 \tag{4.2}
\]

No selected dependency supplies a uniform count or signed estimate for
the near-zero set in braces, with independent moving \(k,k'\), finite
\(g,g'\), coprimality, collars, and the complete metric coefficient.
Exact or near common-squarefree/Pell relations can make (4.2) small.
Proving (4.1), or a target-sized decomposition of this determinant set,
would be new mathematics. Replacing (4.2) by the nonsingular fixed-
\(y\) Hessian (3.7), deleting \(s=0\), forcing \(k'=k,g'=g\), or
expanding away the density mode is the first invalid shortcut.

## 5. Required control test and outcome

- **Parity, gcd, and pointwise versus cross-ray parity:** (2.1) passes.
  Fixed \(m\) permits only \(2s\)-shifts and loses the character; fixed
  \(a\) permits genuine sign-changing cross-ray shifts
  \((m,q)\mapsto(m+s,q+s)\). A general correlation transfers the sign
  to \((-1)^{m'-m}\); it does not create a new character.
- **Moving \(k\)-interval, lift interval, entry/exit, floors, and
  stars:** (2.4), (2.5), and the symmetric-difference identity (3.1)
  retain them literally. No common \(k\) interval or common lift set
  was assumed.
- **Density-discrepancy jointness:** (2.10) retains the product of the
  two complete \(W_R\)'s. Its Fourier transform contains the
  density-density and both density-discrepancy cross terms. The zero
  mode survives (3.3)-(3.4).
- **Orientations and one-count assembly:** the derivation is for the
  accepted \(a<b\) orientation; conjugation gives the other orientation,
  and the outer \(2\Re\) is applied exactly once.
- **Square rays, exact nonsquare centres, and positive-safe blocks:**
  all are zero in \({\bf r}_{a,q}\). If a shift enters one of them, that
  side of (2.10) is zero; it is not counted again. Thus the Round-78
  square owner and Round-79 exact-centre/positive owners remain intact.
- **Near-square, Pell, and short \(q\):** they fail the proposed length
  gain. For \(D\asymp1\), \(H\asymp1\), while
  \(\rho\asymp AJ/L^3\) can be unbounded. Sparse coprime/Pell samples
  also need not occupy consecutive \(q\)'s, so informal alternation is
  not a control.
- **Fourth-power metric resonance:** the known \((81,121)\) family is a
  prior square-ray owner and is not reintroduced. It still falsifies
  any extension of (2.7) that assumes coefficient variation alone forces
  cancellation across isolated populated rays.
- **False unsigned and arbitrary coefficients:** if one replaces the
  actual coefficient by \(F_a(q)=(-1)^qM_0\) on a populated rectangular
  model, then \(\mathfrak Q\asymp P\),
  \(\mathcal G_H\asymp H^2E_0\), and every equality above is at positive
  capacity. Removing \((-1)^q\) gives the same unsigned obstruction.
  Therefore parity plus dispersion alone would prove a false arbitrary-
  coefficient analogue; only an estimate using (2.5) and (4.2) can be
  valid for the actual symbol.
- **\(\rho\)-gain and block sum:** (3.10)-(3.12) pass and show the exact
  missing powers. No block bound was obtained, so no dyadic block sum
  is asserted. The formal wedge \(\rho\ll D\) is not promoted.
- **Transform self-return:** passed with outcome **self-return**.
  Equations (3.3)-(3.4) give the Gram of the original frequency-\(1/2\)
  row, and adjoint reciprocal Poisson gives the Round-80 two-character
  row. The full phase has the exact radial null direction (3.9).
- **External sources and downstream scope:** no external theorem is
  used, so the source-hypothesis map is empty. Nothing here estimates
  other M2 packets, all-denominator endpoint assembly, M9-M2, M9-M1,
  M9, endpoint uniformity, or the quarter target.

## 6. Dependencies and exact artifacts used

The derivation used only the selected context in the task brief:

- `protocol.md`;
- `state/proof_obligations.yml`, specifically the accepted/open nodes
  `M9-M2-top-endpoint-transposed-character-energy`,
  `M9-M2-top-endpoint-odd-lift-resonance-obstruction`,
  `M9-M2-top-endpoint-actual-symbol-variation`,
  `M9-M2-top-endpoint-square-ray-signed-cancellation`,
  `M9-M2-top-endpoint-square-Abel-majorant-obstruction`,
  `M9-M2-top-endpoint-nonsquare-divisor-strip`,
  `M9-M2-top-endpoint-metric-density-obstruction`,
  `M9-M2-top-endpoint-strict-metric-carrier-cancellation`, and
  `M9-M2-top-endpoint-density-discrepancy-energy`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/derivation_packet.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/reviews/conductor_round92_capacity_and_bridges.md`;
- the selected Round-77, Round-78, Round-79, and Round-80 synthesis
  files named in the brief.

No sibling Round-96 report, unlisted historical report, computation, or
external source was used. The argument is algebraic/analytic; there is
no diagnostic numerical evidence.

## 7. Recommended state effect

**Retain the canonical estimate open; promote only the scoped route
obstruction if independently reviewed.** The promotable content is:

- fixed-\(m\) primitive \(q\)-dispersion has only even shifts and hence
  cancels \((-1)^q\) in every nonzero correlation;
- genuine fixed-\(a\) cross-ray dispersion has the exact complete-symbol
  identity (2.9)-(2.10), but its second transform is the Gram of the
  Round-80 row and coefficientwise bounds return equal capacity;
- its best diagonal length gain is \(D^{-1/2}\), so a separately owned
  diagonal can match the target only when \(\rho\ll D\), while hard
  \(D\asymp1\) blocks remain untouched;
- the fixed-\(y\) curvature does not furnish a full determinant because
  the integrated homogeneous phase has the exact radial null direction.

Create no proved hard subrange. Retain (4.1), with the literal
correlation (2.10) and determinant (4.2), as the first strict survivor.
Do not change `M9-M2-top-endpoint-density-discrepancy-energy`, the signed
cone, M9-M2, M9, endpoint uniformity, or `GC-target`, and do not start a
new round.

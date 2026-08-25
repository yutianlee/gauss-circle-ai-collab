# Round 146 discovery report: three-variable Hessian attack

- Campaign: `m9-m1-lower-cone-three-variable-hessian-dispersion-gate`
- Task: `three_variable_hessian_attack`
- Role: discovery
- Starting graph SHA-256: `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`
- Allocation used: 100% analytic/algebraic; 0% numerical/experimental

## 1. Result

The nearest-square mask is not an obstruction on the strict small-
square-factor scalar.  The accepted absolute cell estimate and the
Round-145 large-square tail give the disjoint partition

\[
\begin{aligned}
 \{t<M^{1/4},\ |j_{s,t}|>M^{3/4}\}
 &\ \dot\cup\
 \{t<M^{1/4},\ |j_{s,t}|\le M^{3/4}\}\\
 &\ \dot\cup\
 \{t\ge \lceil M^{1/4}\rceil\}.
\end{aligned}
\tag{146.D1}
\]

The second set is a subset of the already discharged absolute
\(\lvert j\rvert\le M^{3/4}\) owner, and the third set is the already
discharged *unmasked* large-\(t\) owner.  Consequently the exact
Round-145 survivor is target-equivalent to the unmasked scalar

\[
\boxed{
 \mathfrak U_N=
 \sum_M\sum_{1\le t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns}),}
\tag{146.D2}
\]

with an \(O_{\varepsilon,V}(X^\varepsilon)\) error after all blocks.
No discharged channel is counted twice in this comparison.

There is an exact multiplicity-one expansion of (146.D2) into dyadic
\(t,d,e\) boxes, given in Section 2.  On every nonempty box

\[
 t\asymp T,\qquad d\asymp D,\qquad e\asymp E,
 \qquad T^2DE\asymp M,
\tag{146.D3}
\]

the strongest bound proved here for the literal coefficient is the
coefficient-envelope bound

\[
 \boxed{|\mathfrak U_{M,T,D,E}|
 \ll_\varepsilon X^\varepsilon {M^{1/4}\over T}.}
\tag{146.D4}
\]

Thus a boxwise target estimate needs a saving of
\(M^{1/4}/T\) over its raw capacity.  If \(T=M^\theta\), every fixed
\(\theta<1/4\) still needs the polynomial saving
\(M^{1/4-\theta}\).  The absolute ledger proves only the terminal
range \(T\ge M^{1/4-o(1)}\); it proves no strict fixed-power
intermediate-\(t\) reduction.

The ambient three-variable phase really is nondegenerate.  Its scaled
Hessian has determinant \(1/4\).  This does **not** furnish a lawful
estimate for the exact amplitude:

1. the mandatory \(T=1\) face has the rank-one \(d,e\) product phase
   and capacity \(M^{1/4+o(1)}\);
2. the cone does not exclude the \(D=1\) face, and its \(t=1\) prime
   corner is literally nonzero.  Any structurally present \(D=1\) box
   has envelope price \(M^{1/4}/T\) and lies outside a theorem requiring
   three growing sides; no assertion is made that every clipped box is
   nonempty or that its net \(\kappa_t(1,e)\) is nonzero;
3. a coefficient-robust \(t\)-difference removes the new variable.  For
   \(h\ne0\) it returns the rank-one phase \(h\sqrt{Nde}\) together
   with an uncontrolled exact coefficient correlation, while \(h=0\)
   is the separate constant-phase diagonal;
4. even for an optimistically smooth coefficient-free box, the full
   three-dimensional stationary transform has dual phase
   \(-2u\sqrt{vw}/\sqrt N\).  At the phase-monomial level, after the
   required alias-orthant sign reversal, the map \(c\mapsto-2/c\) is
   involutive.  In the ideal full smooth interior, aliaswise triangle
   inequality has upper price \(F^{3/2}\), \(F=\sqrt{NM}\), and after
   the physical weight has upper price \(N^{3/4}\), much worse than
   (146.D4).  This is neither a lower bound nor an amplitude-level
   two-step Poisson identity.

The first exact obstruction is therefore not the mask and not an error
in the Hessian determinant.  It is the absence of a signed correlation
or dual-sum theorem for the literal multiplicity, squarefree,
coprimality, parity, character, and cone coefficient, uniformly across
the \(T=1\) and \(D=1\) faces.  Algebraic Hessian nondegeneracy and
coefficient boundedness alone cannot imply any saving: an arbitrary
bounded coefficient class contains the phase-conjugating array.

The outcome is

\[
 \boxed{\mathsf{three\_variable\_dispersion\_no\_go}.}
\tag{146.D5}
\]

This is a no-go for the proposed Hessian-only/standard-transform
interface, not a lower bound for the actual signed scalar and not a
disproof of its target estimate.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 \mathcal I_M=\mathbb N\cap[M,B_M),\quad B_M\le2M,
\]

where the inherited blocks are disjoint and include their literal
terminal truncation.  Put

\[
 k_{s,t}=\left\lfloor t\sqrt{Ns}+{1\over2}\right\rfloor,
 \qquad j_{s,t}=k_{s,t}^2-Nst^2,
\tag{146.D6}
\]

and extend every amplitude by zero outside its displayed support.  The
integer condition \(t<M^{1/4}\) always means the exact condition

\[
 1\le t<\lceil M^{1/4}\rceil .
\tag{146.D7}
\]

For ordered positive \(d,e\), define the literal contribution of that
factorization by

\[
\begin{aligned}
 \kappa_t(d,e)
 :={}&\mathbf 1_{\{\mu^2(de)=1\}}
       \mathbf 1_{\{e\ {\rm odd}\}}\chi_4(e)\\
 &\times
 \sum_{\substack{\gamma\mid t\\
                   \mu^2(\gamma)=1, (\gamma,de)=1\\
                   \gamma\ {\rm odd}}}\chi_4(\gamma)
 \sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
                   eb^2>4da^2}}1.
\end{aligned}
\tag{146.D8}
\]

Here \(\mu^2(de)=1\) records simultaneously that \(d,e\) are
squarefree and coprime.  Equation (146.D8) retains the full factor
count: no coprimality is imposed on \(a,b\), or between \(\gamma\)
and \(a,b\).  Equivalently,

\[
 \boxed{
 \kappa_t(d,e)=\mathbf 1_{\{\mu^2(de)=1\}}
 \sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
                   eb^2>4da^2}}
 \chi_4(Ge).}
\tag{146.D9}
\]

The \(G\) in (146.D9) is the full gcd and is not the squarefree
\(\gamma\) in (146.D8).  In particular no unrecorded coprimality with
\(G\) is legal.

With

\[
 W_M(u)=u^{-3/4}V_{\rm low}(R^2u/N)
          \mathbf 1_{\{u\in\mathcal I_M\}},
\tag{146.D10}
\]

the exact unmasked scalar is

\[
 \boxed{
 \mathfrak U_N=
 \sum_M\sum_{1\le t<\lceil M^{1/4}\rceil}
 \sum_{d,e\ge1}W_M(t^2de)\kappa_t(d,e)
 e\!\left(\sqrt N\,t\sqrt{de}\right).}
\tag{146.D11}
\]

For powers of two \(T,D,E\), let

\[
\begin{aligned}
 \mathcal T_{M,T}&=[T,2T)\cap\mathbb N
                    \cap[1,\lceil M^{1/4}\rceil),\\
 \mathcal D_D&=[D,2D)\cap\mathbb N,
 \qquad \mathcal E_E=[E,2E)\cap\mathbb N.
\end{aligned}
\tag{146.D12}
\]

Then (146.D11) is literally the sum of

\[
 \mathfrak U_{M,T,D,E}=
 \sum_{\substack{t\in\mathcal T_{M,T},\ d\in\mathcal D_D,
                   \ e\in\mathcal E_E\\t^2de\in\mathcal I_M}}
 (t^2de)^{-3/4}V_{\rm low}(R^2t^2de/N)
 \kappa_t(d,e)e(f(t,d,e)),
\tag{146.D13}
\]

where

\[
 f(t,d,e)=\sqrt N\,t\sqrt{de}.
\tag{146.D14}
\]

The last \(T\)-box and the last \(M\)-block may be clipped; no full-box
replacement is made.  All parity, character, coprimality, squarefree,
strict-cone, profile, and endpoint conditions occur in (146.D8)--
(146.D13).  The nearest-square mask alone has been removed by the
owner-complete lemma in Section 3.1.

The precise no-go statement is the following.  From the accepted
dependencies and elementary inequalities alone, (146.D4) is valid on
every aspect-ratio box.  Neither the nonzero determinant in Section 3.4,
one coefficient-robust \(A\)-process, nor one full stationary
\(B\)-process improves (146.D4) for (146.D13).  A strict
intermediate-\(t\) conclusion therefore requires a new estimate for the
actual signed coefficient correlations or the exact transformed
coefficient, plus separate estimates for every short face.

## 3. Proof and derivation

### 3.1 Exact removal of the nearest-square mask

The accepted cell owner is an absolute estimate.  In the notation
(146.D6), it gives, on each block and for every \(J\ge1\),

\[
 \#\{m\in\mathcal I_M:0<|k_m^2-Nm|\le J\}
 \ll_\varepsilon JX^\varepsilon,
\tag{146.D15}
\]

after the accepted gcd average; the exact-radical channel \(j_m=0\)
is separately absolutely target-safe.  With \(J=M^{3/4}\),
\(|C(m)|\le\tau(m)\ll_\varepsilon X^\varepsilon\), and
\(m\asymp M\), (146.D15) gives

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|\le M^{3/4}}}
 m^{-3/4}|V_{\rm low}(R^2m/N)C(m)|
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{146.D16}
\]

Every \(m\) has a unique representation \(m=st^2\), \(s\)
squarefree.  Therefore imposing the additional restriction
\(t<\lceil M^{1/4}\rceil\) in (146.D16) can only decrease its absolute
left side.  The difference between the Round-145 masked survivor and
(146.D2) is exactly that restricted subset, including the equality
\(|j|=M^{3/4}\) and the exact radicals.  This proves (146.D2).

For clarity, the large-\(t\) estimate is not invoked again in this
difference.  It controls the third, disjoint set in (146.D1) by

\[
 M^{-3/4}X^\varepsilon
 \sum_{t\ge\lceil M^{1/4}\rceil}{M\over t^2}
 \ll X^\varepsilon.
\tag{146.D17}
\]

In the comparison we use only the small-\(t\) subset of (146.D16),
which is disjoint from the set in (146.D17).  The two larger inherited
absolute owners may overlap, but the exact partition (146.D1) does not
charge that overlap twice.

### 3.2 Coefficient and multiplicity

Given an ordered divisor incidence \(hr=st^2\), let \(\gamma\) be
the common part of the squarefree kernels of \(h,r\).  There are unique
pairwise coprime squarefree \(\gamma,d,e\) and unique \(a,b\ge1\)
such that

\[
 h=\gamma da^2,\qquad r=\gamma eb^2,
 \qquad s=de,\qquad t=\gamma ab.
\tag{146.D18}
\]

Conversely (146.D18) reconstructs one ordered \((h,r)\).  The condition
that \(r\) is odd says that \(\gamma,e,b\) are odd; all powers of two
from \(s\) and \(t\) are thereby forced to the \(d\)- and \(a\)-
sides.  Moreover

\[
 \chi_4(r)=\chi_4(\gamma)\chi_4(e),
 \qquad r>4h\iff eb^2>4da^2.
\tag{146.D19}
\]

This proves (146.D8) and its multiplicity-one insertion into
(146.D11).  Taking instead \(G=(h,r)\), writing
\(h=Gda^2,r=Geb^2\), proves (146.D9).  The two maps are not merged.

The pointwise factor-count bound needed below is

\[
 |\kappa_t(d,e)|
 \le\sum_{\gamma ab=t}1=\tau_3(t)
 \ll_\varepsilon t^\varepsilon.
\tag{146.D20}
\]

This bound is lawful but loses every sign in the factor count.  It is
the only property of \(\kappa\) used in the capacity estimate.

### 3.3 Box count and complete target-power ledger

If (146.D13) is nonempty, then

\[
 {M\over16}<T^2DE<2M.
\tag{146.D21}
\]

Indeed a supported triple is at least \(T^2DE\) and is below \(2M\),
whereas it is below \(16T^2DE\) and at least \(M\).  Consequently

\[
 TDE\asymp {M\over T}.
\tag{146.D22}
\]

Using (146.D20), boundedness of the profile, and the literal clipped
box only to decrease the count gives

\[
\begin{aligned}
 |\mathfrak U_{M,T,D,E}|
 &\ll_\varepsilon
 M^{-3/4}X^\varepsilon TDE\\
 &\ll_\varepsilon X^\varepsilon {M^{1/4}\over T},
\end{aligned}
\tag{146.D23}
\]

which is (146.D4).  For fixed \(M,T,D\), (146.D21) permits only
\(O(1)\) dyadic \(E\); all \(M,T,D,E\) assemblies are logarithmic and
are absorbed by epsilon renaming.

Before the weight \(M^{-3/4}\), the box capacity is \(M/T\).  A
sufficient boxwise target is therefore the raw signed estimate

\[
 \left|\sum_{(t,d,e)\ {\rm in\ the\ literal\ box}}
 \kappa_t(d,e)e(f(t,d,e))\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{146.D24}
\]

with the profile and prefix-uniformity restored as required by partial
summation.  Relative to the raw capacity, (146.D24) needs the factor

\[
 {M/T\over M^{3/4}}={M^{1/4}\over T}.
\tag{146.D25}
\]

At \(T=M^\theta\), \(0\le\theta<1/4\), the missing factor is
\(M^{1/4-\theta}\).  On the top block \(M\asymp R^2\), the physical
weighted capacity is \(R^{1/2}/T\); at \(t=1\) it is
\(R^{1/2+o(1)}\).  A cutoff
\(T\ge M^{1/4}/(\log X)^A\) is epsilon-safe by (146.D23), but this is
only an epsilon-equivalent terminal trimming, not a strict fixed-power
dispersion reduction.

### 3.4 Derivative and scaled-Hessian ledger

Write \(\lambda=\sqrt N\).  The gradient and Hessian are exactly

\[
 \nabla f=
 \left({f\over t},{f\over2d},{f\over2e}\right),
\tag{146.D26}
\]

and

\[
 \nabla^2f=f
 \begin{pmatrix}
 0&(2td)^{-1}&(2te)^{-1}\\
 (2td)^{-1}&-(4d^2)^{-1}&(4de)^{-1}\\
 (2te)^{-1}&(4de)^{-1}&-(4e^2)^{-1}
 \end{pmatrix}.
\tag{146.D27}
\]

Hence, in the requested order \(t,d,e\),

\[
 \boxed{
 f^{-1}\operatorname{diag}(t,d,e)\nabla^2f
 \operatorname{diag}(t,d,e)=
 \begin{pmatrix}
 0&1/2&1/2\\
 1/2&-1/4&1/4\\
 1/2&1/4&-1/4
 \end{pmatrix}.}
\tag{146.D28}
\]

Its eigenvalues are \(-1/2,1/\sqrt2,-1/\sqrt2\), so it is uniformly
conditioned in relative coordinates and

\[
 \boxed{\det(\text{scaled Hessian})={1\over4},\qquad
 \det\nabla^2f={f^3\over4t^2d^2e^2}.}
\tag{146.D29}
\]

On (146.D3), put

\[
 F=\sqrt{NM},\qquad V_3=TDE\asymp M/T.
\tag{146.D30}
\]

Then \(f\asymp F\), the three gradient ranges are

\[
 {F\over T},\qquad {F\over D},\qquad {F\over E},
\tag{146.D31}
\]

and

\[
 |\det\nabla^2 f|\asymp {F^3\over V_3^2}.
\tag{146.D32}
\]

Thus the advertised nondegeneracy is algebraically correct on every
positive interior point.  It says nothing by itself about a lattice
sum with the coefficient (146.D8).

### 3.5 Aspect ratios and every short face

If a term of (146.D8) is nonzero, then \(t=\gamma ab\) and
\(a/b=a^2\gamma/t\ge1/t\).  The strict cone therefore implies

\[
 {e\over d}>4\left({a\over b}\right)^2\ge {4\over t^2},
 \qquad
 d^2<{m\over4},\qquad e^2>{4m\over t^4},
 \quad m=t^2de.
\tag{146.D33}
\]

For a nonempty dyadic box this gives

\[
 D\ll\sqrt M,\qquad E\gg {\sqrt M\over T^2}.
\tag{146.D34}
\]

If \(T=M^\theta,D=M^\delta,E=M^\zeta\) at the level of powers, then

\[
 2\theta+\delta+\zeta=1,qquad
 0\le\theta<1/4,qquad 0\le\delta\le1/2,
 \qquad \zeta\ge1/2-2\theta.
\tag{146.D35}
\]

The balanced aspect is
\(\delta=\zeta=1/2-\theta\).  The full face ledger is as follows.

| Face | Exact reduced phase/Hessian | Capacity and outcome |
|---|---|---|
| All \(T,D,E\) long | (146.D28), determinant \(1/4\) | Algebraically nondegenerate; coefficient/dual estimate open. |
| \(T=1\) or bounded \(T\) | For fixed \(t\), the \(d,e\) scaled Hessian is \(\bigl(\begin{smallmatrix}-1/4&1/4\\1/4&-1/4\end{smallmatrix}\bigr)\), determinant zero. | Mandatory and not target-safe: price \(M^{1/4+o(1)}\) at \(t=1\). |
| \(D=1\) or bounded \(D\) | For fixed \(d\), the \(t,e\) scaled Hessian is \(\bigl(\begin{smallmatrix}0&1/2\\1/2&-1/4\end{smallmatrix}\bigr)\), determinant \(-1/4\). | Two-dimensional rather than three-dimensional; price remains \(M^{1/4}/T\), so it cannot be discarded. |
| \(E=1\) | Empty in the strict small-\(t\) range: (146.D33) would give \(t^4>4m\ge4M\), contrary to \(t^4<M\). | Passed as an empty face. |
| Bounded \(E\) | Fixed \(e\) leaves the nondegenerate \(t,d\) matrix above.  Equation (146.D33) forces \(t\gg_E M^{1/4}\). | Only a terminal \(T\)-shell; (146.D23) is \(O_E(X^\varepsilon)\). |
| \(t,d\) fixed | One-variable \(e\)-phase with \(f_{ee}=-f/(4e^2)\). | Does not address the sum over faces or the arithmetic amplitude. |
| \(t,e\) fixed | One-variable \(d\)-phase with \(f_{dd}=-f/(4d^2)\). | Same. |
| \(d,e\) fixed | The phase is exactly linear in \(t\), so \(f_{tt}=0\). | No second-derivative gain in the new variable. |
| Product boundary \(t^2de=M\) or \(B_M\) | The phase is constant on each fixed product level: \(f=\sqrt{NM}\) on the lower level and \(f=\sqrt{NB_M}\) on the upper level. | A fixed integer \(m\)-layer is absolutely target-safe, but a wide radial smoothing collar is not free; literal endpoints remain in (146.D13). |
| Cone equality | \(eb^2=4da^2\) has no solutions because \(e,b\) are odd. | Equality face empty.  Altering only \(O(1)\) \(e\)-layers per factor tuple costs \(M^{-3/4}TDX^\varepsilon\ll X^\varepsilon\), but a relative-width cone collar is not automatically safe. |
| Terminal \(t=M^{1/4}\) | The exact integer split is (146.D7). | The outer side is the unmasked Round-145 owner; the final clipped inner shell has target-safe absolute price only when \(T\asymp M^{1/4}\). |

At \(t=1\), (146.D8) simplifies exactly to

\[
 \kappa_1(d,e)=\mathbf1_{\{\mu^2(de)=1\}}
 \mathbf1_{\{e\ {\rm odd}\}}\chi_4(e)
 \mathbf1_{\{e>4d\}}.
\tag{146.D36}
\]

Thus the bounded-\(t\) face is the inherited rank-one cone scalar, not
an artificial boundary error.  Its \(D=1\) corner is nonvacuous:
for every odd prime \(p>4\), \(C(p)=\chi_4(p)\ne0\).  More generally,
\(D=1\) is structurally admissible in fixed-power ranges: the literal
tuple \(\gamma=1,a=t,b=1,d=1\) satisfies the cone whenever
\(e>4t^2\), which is compatible with the corresponding product scale
away from the terminal cutoff.  This does not prove nonemptiness in
every arbitrarily clipped block or nonvanishing of the net
\(\kappa_t(1,e)\); other factor tuples may cancel.

### 3.6 Why the new Hessian direction does not itself give dispersion

First consider a lawful coefficient-robust difference in the new
variable.  For fixed \(d,e\), write the exact, zero-extended amplitude
in (146.D13) as \(A_{t,d,e}\).  Then

\[
 \left|\sum_t A_{t,d,e}e(\lambda t\sqrt{de})\right|^2
 =\sum_h e(\lambda h\sqrt{de})
   \sum_t A_{t+h,d,e}\overline{A_{t,d,e}}.
\tag{146.D37}
\]

The phase on the right is independent of \(t\).  For \(h\ne0\), its
\(d,e\) scaled Hessian is the rank-one matrix in the \(T=1\) row of
the table.  For \(h=0\), the phase is constant and the term is the
separate diagonal.  Both the diagonal and off-diagonal correlations
retain two exact factor counts, two cone conditions, squarefree and
coprimality intersections, the product endpoints, and the profile.
Bounding them absolutely and applying Cauchy returns the primal
capacity; no accepted correlation estimate saves a power.  Thus the
off-diagonal standard \(t\)-\(A\)-process returns precisely the old
two-variable product-fibre interface, while the diagonal supplies no
oscillation.

Next grant, only as an optimistic control, a smooth coefficient-free
box and perform simultaneous three-dimensional Poisson/stationary
phase.  For a dual vector \((u,v,w)\) the critical equations for

\[
 f(t,d,e)-ut-vd-we
\]

have the exact solution

\[
 t_*={2\sqrt{vw}\over\lambda},\qquad
 d_*={u\over\lambda}\sqrt{w\over v},\qquad
 e_*={u\over\lambda}\sqrt{v\over w},
\tag{146.D38}
\]

and critical value

\[
 \boxed{-{2u\sqrt{vw}\over\lambda}.}
\tag{146.D39}
\]

The dual side lengths are those in (146.D31).  In the ideal full smooth
interior model, the gradient-image volume and hence the interior alias
count have scale

\[
 Q_{\rm int}\asymp {F^3\over TDE}={F^3\over V_3}.
\tag{146.D40}
\]

For a merely clipped box without a separate gradient-image boundary
lattice estimate, the upper-price ledger uses only
\(Q\ll F^3/V_3\).

By (146.D32), one stationary integral has modulus

\[
 |\det\nabla^2f|^{-1/2}\asymp {V_3\over F^{3/2}}.
\tag{146.D41}
\]

Aliaswise triangle inequality therefore has the upper price

\[
 Q{V_3\over F^{3/2}}\ll F^{3/2}.
\tag{146.D42}
\]

After multiplication by the physical weight \(M^{-3/4}\), the resulting
upper price is

\[
 M^{-3/4}F^{3/2}=N^{3/4}.
\tag{146.D43}
\]

This upper price is much worse than (146.D23); it is not a lower bound
and does not rule out signed dual cancellation.  Boundary and
amplitude-transform terms were optimistically omitted, so the
transform-followed-by-triangle-inequality route has not closed the
target.  The phase in (146.D39) is the same monomial.  More exactly, at
the phase-monomial level the Legendre coefficient map is

\[
 c\longmapsto-{2\over c},\qquad
 -{2\over(-2/c)}=c.
\tag{146.D44}
\]

Starting from \(c>0\), the first stationary aliases lie in the positive
orthant and the dual coefficient is negative.  A second stationary
transform uses the opposite alias orthant; after reversing those alias
signs, (146.D44) returns \(c\).  This is a phase-level involution only,
not a literal two-step Poisson identity for amplitudes: Maslov factors,
transformed coefficients, boundaries, and the orthant change remain.
Any gain must be a signed estimate for the dual aliases and transformed
coefficient; it is not supplied by \(\det=1/4\).

For the actual amplitude, the optimistic transform is not even the
first lawful step.  The divisibility condition \(\gamma ab=t\), the
Möbius/coprimality support, and the cone make \(\kappa_t(d,e)\) a
discrete joint coefficient, not a smooth tensor.  Expanding it costs
only \(X^\varepsilon\) in multiplicity but replaces the \(t\)-variable
by the variables \(\gamma,a,b\); retaining \(t\) leaves a sharp
divisor mask.  A theorem that assumes only
\(|\kappa|\ll X^\varepsilon\) cannot help: for the same phase and box,
the bounded array \(a_{t,d,e}=e(-f(t,d,e))\) makes the sum equal its
full volume.  This adversarial control is used only to refute a
coefficient-blind inference, not as a model for the actual coefficient.

### 3.7 Exceptional frequency, direction, and endpoint controls

The accepted exceptional family survives the mask removal and was
already present in the strict masked scalar.  For squarefree \(s>1\)
and

\[
 X=N=sL^2+1,
\]

one has

\[
 \sqrt{Ns}=sL+\rho,qquad
 \rho={1\over\sqrt{L^2+1/s}+L}.
\tag{146.D45}
\]

While \(t\rho<1/2\),

\[
 k_{s,t}=sLt,\qquad j_{s,t}=-st^2,
 \qquad e(+t\sqrt{Ns})=e(+t\rho).
\tag{146.D46}
\]

With \(L=s\) the accepted flat-profile range contains
\(1\le t\le c s^{1/4}\), and \(t\rho\to0\) uniformly there.  Hence a
uniform modular lower bound for the \(t\)-derivative, uniform dual
separation, or a bounded-partial-quotient input is false.  The prime
case at \(t=1,d=1,e=s\) supplies literal nonvacuity.  Equations
(146.D45)--(146.D46) do not prove coherent summation over varying
\(s\), so no signed lower bound is asserted.

Every formula above keeps the individual positive complex direction
\(e(+f)\) at the fixed centre \(N=\lfloor X\rfloor\).  No conjugate
pair, cosine, centre average, mean square, or positive energy is
substituted for it.  Bounded \(X\), the smallest block, clipped
\(T\)-boxes, the terminal \(B_M\), and logarithmic assemblies are
absorbed only after their literal supports have been retained.

## 4. First doubtful or unproved step

After the proved mask removal, the first open estimate is exactly

\[
 \boxed{\mathfrak U_N\ll_{\varepsilon,V}X^\varepsilon,}
\tag{146.D47}
\]

with \(\mathfrak U_N\) defined by either (146.D2) or the literal
coefficient expansion (146.D11).  A sufficient boxwise input is
(146.D24), uniformly in every prefix needed for the sharp product
domain and terminal block.

Already the \(t=1\) face asks for the unmasked estimate

\[
 \boxed{
 \sum_{\substack{s\asymp M\\s\ {\rm squarefree}}}
 V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon,}
\tag{146.D48}
\]

with literal block endpoints (and the harmless variable
\(s^{-3/4}\) restored by partial summation).  Its expanded \(d,e\)
phase has rank one.  For a strict intermediate range
\(T\ge M^{\theta_0}\), \(\theta_0<1/4\), the missing statement is a
uniform signed saving of at least \(M^{1/4-\theta_0}\), including every
structurally present \(D=1\) box.  Neither (146.D37) nor (146.D39)
proves it: the former
requires new exact coefficient-correlation bounds, and the latter
requires a new signed dual-alias estimate for the transformed actual
coefficient.

This is the first unproved step.  The nonzero determinant is verified,
not doubtful.  The no-go conclusion says only that the proposed
Hessian-only interface stops here.

## 5. Required control tests and outcomes

1. **`exact_t_d_e_coefficient_and_multiplicity` — PASS.**
   Equations (146.D8), (146.D9), and (146.D18)--(146.D20) give both
   accepted parametrizations and the multiplicity-one inverse map.

2. **`squarefree_coprimality_parity_character_and_cone` — PASS.**
   The factor \(\mu^2(de)\), \((\gamma,de)=1\), odd
   \(\gamma,e,b\), \(\chi_4(\gamma)\chi_4(e)\), and the strict
   inequality \(eb^2>4da^2\) are literal.  No false gcd condition is
   transferred from \(\gamma\) to \(G\).

3. **`literal_profile_mask_and_block_endpoints` — PASS, with a new
   proved simplification.**  The nearest-square mask is removed only by
   the absolute inclusion (146.D15)--(146.D17).  The profile, product
   staircase, exact ceiling, half-open \(B_M\), and clipped boxes remain
   in (146.D10)--(146.D13).

4. **`three_variable_scaled_Hessian_determinant` — PASS.**
   Equations (146.D26)--(146.D32) verify every entry, the eigenvalues,
   determinant \(1/4\), unscaled determinant, gradient ranges, and phase
   scale.

5. **`aspect_ratio_and_short_face_ledger` — PASS as a no-go control.**
   Equations (146.D33)--(146.D36) and the face table cover balanced and
   unbalanced boxes, \(T=1\), \(D=1\), empty \(E=1\), bounded \(E\),
   one-variable edges, product boundaries, the cone boundary, and the
   terminal \(t\)-face.  The mandatory \(T=1,D=1\) faces remain open.

6. **`M_T_D_E_capacity_and_dyadic_assembly` — PASS.**
   Equations (146.D21)--(146.D25) give the complete
   \(M,T,D,E\) count, target saving, top-block price, and logarithmic
   assembly.

7. **`t_equals_one_and_bounded_t_boundary` — FAILS the proposed
   dispersion closure, as required for the no-go.**  The exact face is
   (146.D36), has rank-one phase and owner-sized absolute capacity, and
   is nonempty on primes.  No three-variable estimate covers it.

8. **`exceptional_slow_frequency_family` — PASS as an obstruction.**
   Equations (146.D45)--(146.D46) retain the exact family and refute a
   uniform derivative/dual-separation hypothesis without claiming a
   lower bound.

9. **`individual_complex_direction_and_fixed_centre` — PASS.**  The
   sign is always \(+\), and \(N=\lfloor X\rfloor\) is never averaged.

10. **`dual_transform_and_self_return_controls` — PASS as a no-go.**
    Equations (146.D38)--(146.D44) give the exact critical point, dual
    monomial, ideal-interior alias scale, stationary amplitude, physical
    triangle-inequality upper price, and phase-level involution after
    alias-orthant reversal.  Equation (146.D37) records the separate
    constant \(h=0\) diagonal and rank-one \(h\ne0\)
    \(t\)-difference return.

11. **`strict_survivor_complement_target_safety` — NO strict
    fixed-power reduction proved.**  The mask complement and the
    original large-\(t\) complement are owner-complete and disjoint as
    in (146.D1).  Beyond an epsilon-equivalent terminal trimming,
    (146.D25) leaves a polynomial deficit for every
    \(\theta<1/4\).

12. **`Round138_cross_owner_and_downstream_scope` — PASS.**  Nothing
    here estimates the independent collar-tail cross owner.  No lower
    GAR, direct M1 parent, M9-M1, M2 owner, endpoint uniformity, M9,
    conditional bridge, quarter theorem, or global exponent is claimed.

## 6. Dependencies and exact artifacts used

The derivation used only the selected context in the brief:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the accepted
  `M9-M1-lower-far-cone-microscopic-cell-reduction`,
  `M9-M1-lower-incomplete-fibre-dispersion-obstruction`,
  `M9-M1-lower-cone-squarefree-kernel-reduction`,
  `M9-M1-lower-cone-squarefree-linearization-obstruction`, and the open
  `M9-M1-global-lower-radial-signed-estimate`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reviews/conductor_round145_squarefree_kernel_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`.

No sibling Round-146 report, external theorem, web source, numerical
experiment, or desired circle estimate was used.  The stationary-phase
calculation is an analytic control of the proposed mechanism, not an
imported black box.

## 7. Recommended state effect

1. **Promote after seam review** the narrow exact reduction
   (146.D1)--(146.D2): the strict small-\(t\), large-displacement scalar
   is target-equivalent to the *unmasked* strict small-\(t\) scalar.
   Record explicitly that the small-displacement subset and the
   unmasked large-\(t\) owner are disjoint in the partition used, so
   neither accepted error is recounted.

2. **Retain** (146.D8)--(146.D13) as the literal three-variable
   coefficient/support interface and (146.D28)--(146.D35) as correct
   Hessian and aspect-ratio algebra.  The determinant is useful
   diagnostic information, not an estimate.

3. **Create or update a scoped obstruction** recording
   (146.D37)--(146.D44): the off-diagonal part of a
   coefficient-robust \(t\)-difference returns the rank-one product
   phase while \(h=0\) is constant, and the full smooth stationary
   transform is phase-monomially involutive after alias-orthant reversal.
   Its aliaswise triangle-inequality upper price is far above target.
   Also retain the mandatory \(T=1\) corner, the structurally admissible
   \(D=1\) face, and the exceptional family.

4. **Reject** claims that the mask remains the first obstacle, that
   \(\det=1/4\) alone gives cancellation for an arbitrary bounded joint
   coefficient, that all three side lengths grow, that cone/profile
   boundaries may be discarded without their owner costs, or that a
   transform followed by modulus is a dispersion gain.

5. **Make no downstream promotion.**  The first open owner is the
   unmasked scalar (146.D47), including (146.D48) and every structurally
   present \(D=1\) box.  A future reopening needs a genuinely signed theorem for the
   exact coefficient correlations or dual coefficient, with an
   owner-complete bounded-face estimate.  The independent Round-138
   cross owner and every M1/M2/M9/bridge/exponent obligation remain
   unchanged.

Recommended task effect: **retain the mask-removal reduction; retain
the target as open; record `three_variable_dispersion_no_go`.**

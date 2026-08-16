# Round 88 discovery report: period-depth tensor attack

Campaign: `m9-m1-cross-group-period-depth-dispersion`  
Task: `period_depth_tensor_attack`  
Role: constructive discovery  
Starting graph SHA-256: `e2346245d09d22ba66e17037ad57e85cf56808d9ca70526657f78d94e52809be`

## 1. Result

The full target (88.9) is not proved uniformly over the frozen range
\(J^{11/90}<B\leq J^{3/20}\).  Two exact reductions and two target-safe
deletions are proved.

First, the local period is governed by the **masked finite difference**,
not by the quadratic numerator (88.11).  Here and below, depth means
the additive period of the reciprocal masked weight
\(\mathbf1_{\mathcal D_q}e_q(K_q\Phi)\), not of the total affine phase
\(e_q(u_qx)\mathbf1_{\mathcal D_q}e_q(K_q\Phi)\).  For every full factor
\(q=p^\nu\Vert M\), including \(p=2\), the nonzero reciprocal masked
weight has a unique depth \(j_q\in\{0,\ldots,\nu-1\}\).  Its completed
transform is supported on \(p^{j_q}\mid u\), and its exact descent is

\[
 \mathfrak T_q(p^{j_q}u')
   =p^{2j_q}\mathfrak T^{\downarrow}_{p^{\nu-j_q}}(u').
 \tag{1.1}
\]

The factor is \(p^{2j_q}\), because the trace in (88.10) has the outer
factor \(q\).  Only the unprefactored Fourier transform descends with a
single factor \(p^{j_q}\).  CRT gives a tensor product over the **full**
prime powers and retains the complete \(2\)-part.  Empty unit domains
give the zero trace and are removed before depth is assigned.

Second, additive period depth and Round-87 group depth are different
invariants.  For two physical pairs let \(\rho=M/m_0\), where \(m_0\)
is the largest divisor of \(M\) modulo which the two pairs belong to the
same active-set/active-label group.  Put

\[
 \rho_*(b)=\min\!\left(M,
   \left\lfloor J^{11/30}B^{-2}\right\rfloor\right).
 \tag{1.2}
\]

The exact union of cross-group shells \(1<\rho\leq\rho_*(b)\), with the
literal integer \(u=0\) term still deleted, satisfies

\[
 \mathcal G_{\mathrm{coarse}\leq\rho_*}(D)
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5}.
 \tag{1.3}
\]

This is nonempty: in the \(M=4b\) class, distinct fine unit pairs which
differ by \(M/2\) in both coordinates coincide modulo \(M/2\), so the
\(\rho=2\) shell occurs for large \(J\).  The conductor-dependent range
in (1.2) is the largest range certified by the proved coarse-square
budget.  It equals
\(J^{1/15}\) at \(B=J^{3/20}\) and is of order \(B\) at
\(B=J^{11/90}\).

There is also a separately target-safe good-prime partial-period
subaggregate.  For \(p\geq11\) and \(p\nmid K\), put

\[
 a_q=\begin{cases}
 \min(j_q,\nu-j_q),&j_q>0,\\
 0,&j_q=0,
 \end{cases}
 \qquad
 \mathfrak a=\prod_{\substack{p^\nu\Vert M\\p\geq11,\ p\nmid K}}p^{a_q}.
 \tag{1.4}
\]

Among the remaining shells \(\rho>\rho_*\), all exact period tensors
with

\[
 \mathfrak a\geq {M^2\over\rho_*^2}
 \tag{1.5}
\]

are target-safe by a bounded-degree physical-edge estimate.  Thus the
smallest signed survivor obtained here is

\[
 \boxed{\mathcal G_{\rm hard}(D):
   \rho>\rho_*,\qquad
   \mathfrak a<{M^2\over\rho_*^2},}
 \tag{1.6}
\]

partitioned by the exact local depths below.  It contains the genuinely
aperiodic tensors and the unremoved partial periods at small primes,
nonunit \(K\), the full \(2\)-part, and shallow good-prime lifts.  In
particular, masked accidental periods need not lie in a shallow
Round-87 group shell.

## 2. Exact statement and hypotheses

All scales, classes, support restrictions, and prior ownership are
those of the derivation packet:

\[
 J=X^{1/2},\quad Q=J^{2/5},\quad T=J^{3/5},\quad B=C/T,
 \quad J^{13/18}<C\leq J^{3/4},\quad M\asymp B,
 \tag{2.1}
\]

\[
 D_1<|d|<\Delta_b-E_*,\qquad U=D.
 \tag{2.2}
\]

The functions \(I_b\) are extended by zero off their exact stationary
support.  The deep multiplier \(\Pi_{b,D}\) retains both signs of \(d\)
and has the accepted logarithmic \(L^\infty\) cost.  No transition,
axis, cone-edge, entry/exit, wrong-sign, stationary-error, or exterior
term is added to the frozen smooth-principal survivor.

For a physical ordered pair \(P=(x,y)\), \(x\ne y\), write

\[
 f_{b,P}=\Pi_{b,D}F_{b,P},\qquad
 F_{b,P}=e_M(K(\bar x-\bar y))
             \mathcal R_{b,x}\overline{\mathcal R_{b,y}}.
 \tag{2.3}
\]

These are the normalized rows from (88.1), so

\[
 \|f_{b,P}\|_\infty
 \ll_\varepsilon X^\varepsilon T^2Q^{-5/12}.
 \tag{2.4}
\]

There is no further \(M^{-2}\) in (2.3).

For an ordered pair of physical pairs put

\[
 P=(x,x-A),\qquad P'=(x-V,x-V-B_2).
 \tag{2.5}
\]

At \(q=p^\nu\Vert M\), let

\[
 \mathcal D_q(A,B_2,V)=
 \{x\bmod q:p\nmid x(x-A)(x-V)(x-V-B_2)\},
 \tag{2.6}
\]

and, after the CRT unit is inserted, let

\[
 w_q(x)=\mathbf1_{\mathcal D_q}(x)e_q(K_q\Phi(x)),
 \quad
 \Phi(x)=x^{-1}-(x-A)^{-1}-(x-V)^{-1}+(x-V-B_2)^{-1}.
 \tag{2.7}
\]

If \(M_q=M/q\) and \(c_q\equiv M_q^{-1}\pmod q\), then
\(K_q=c_qK\) and the local additive frequency is \(u_q=c_qu\).  Define

\[
 \Psi_t(x)={\Phi(x+t)-\Phi(x)\over t}
 =-{1\over x(x+t)}+{1\over(x-A)(x+t-A)}
   +{1\over(x-V)(x+t-V)}
   -{1\over(x-V-B_2)(x+t-V-B_2)}.
 \tag{2.8}
\]

If \(\mathcal D_q=\varnothing\), declare the local tensor null.  If it
is nonempty, its exact period exponent is

\[
 r_q=\min\left\{1\leq r\leq\nu:
  \min_{x\in\mathcal D_q}
  v_p\!\left(K_qp^r\Psi_{p^r}(x)\right)\geq\nu\right\},
 \qquad j_q=\nu-r_q.
 \tag{2.9}
\]

Valuation \(+\infty\) is used for zero.  Formula (2.9), which tests the
whole allowed unit set, is the authoritative full-prime-power
classification.  It is not replaced by a valuation of (88.11).

For \(p=2\), (2.6) is nonempty exactly when

\[
 A\equiv B_2\equiv V\equiv0\pmod2;
 \tag{2.10}
\]

then it is the set of all odd residues and (2.9) is the complete
\(2\)-adic depth formula.  On an actual physical edge all four
coordinates are \(2\)-adic units, so these three parity conditions
hold automatically; no part of the actual \(2\)-factor is discarded.
For odd \(p\), the allowed residues modulo \(p\) are the complement of

\[
 \{0,A,V,V+B_2\}\pmod p.
 \tag{2.11}
\]

Thus empty masks occur only in the small-prime strata; they are zero,
not periodic mass.  If \(\kappa=v_p(K_q)\) capped at \(\nu\), then

\[
 r_q\leq\max(1,\nu-\kappa),\qquad
 j_q\geq\min(\kappa,\nu-1),
 \tag{2.12}
\]

so every nonunit-\(K\) return is retained by (2.9).

For group depth, let \(E_{p^s}(P,P')\) be the assertion that the two
pairs have the same Round-87 group after reduction modulo \(p^s\).  In
the coordinates (2.5),

\[
 E_{p^s}=
 \bigl[p^s\mid A\ \hbox{and}\ p^s\mid B_2\bigr]
 \ \vee\ 
 \bigl[p^s\mid V\ \hbox{and}\ p^s\mid A-B_2\bigr].
 \tag{2.13}
\]

Put \(s_p=\max\{s:E_{p^s}\}\),
\(m_0=\prod_{p^\nu\Vert M}p^{s_p}\), and \(\rho=M/m_0\).  Then
\(\rho=1\) is exactly the Round-87 same-group package, already owned;
every strict cross-group edge has \(\rho>1\).

## 3. Proof or derivation

**Masked period and tensor descent.**  For nonempty \(\mathcal D_q\),
the support of \(w_q\) is not invariant under a translation prime to
\(p\).  Indeed, its reduction modulo \(p\) is a nonempty proper subset
of the additive group \(\mathbb F_p\), while invariance under one
nonzero translation would make it all of \(\mathbb F_p\).  Hence the
period group is

\[
 \operatorname{Per}(w_q)=p^{r_q}\mathbb Z/p^\nu\mathbb Z
 \quad(1\leq r_q\leq\nu).
 \tag{3.1}
\]

Translations divisible by \(p\) preserve the mask.  Invariance under
the generator \(p^r\) is therefore exactly the phase congruence in
(2.9), proving that formula.

Let \(q'=p^{r_q}=p^{\nu-j_q}\).  Fourier invariance gives

\[
 \sum_{x\bmod q}w_q(x)e_q(u_qx)=0
 \quad\hbox{unless}\quad p^{j_q}\mid u_q.
 \tag{3.2}
\]

When \(u_q=p^{j_q}u'_q\), \(w_q\) descends to a well-defined
\(\bar w_q\) modulo \(q'\), and

\[
\begin{aligned}
 \mathfrak T_q(u_q)
 &=q\sum_{x\bmod q}w_q(x)e_q(u_qx)\\
 &=q p^{j_q}\sum_{z\bmod q'}\bar w_q(z)e_{q'}(u'_qz)\\
 &=p^{2j_q}
   \left(q'\sum_{z\bmod q'}\bar w_q(z)e_{q'}(u'_qz)\right).
\end{aligned}
 \tag{3.3}
\]

This proves (1.1).  CRT gives, without discarding any bad factor,

\[
 \mathfrak T_M(u,A,B_2,V)=\prod_{q\Vert M}\mathfrak T_q(c_qu).
 \tag{3.4}
\]

Put \(L=\prod_qp^{j_q}\).  If no local tensor is null, then

\[
 \mathfrak T_M(u)=0\quad(L\nmid u),
 \tag{3.5}
\]

and, for \(u=Lw\),

\[
 \mathfrak T_M(Lw)
 =L^2
 \prod_{j_q=0}\mathcal A_q(c_qLw)
 \prod_{j_q>0}
 \mathcal P^{\downarrow}_{q,j_q}
  \!\left(c_q{L\over p^{j_q}}w\right).
 \tag{3.6}
\]

Here \(\mathcal A_q=\mathfrak T_q\) is the genuinely aperiodic local
operator, and \(\mathcal P^{\downarrow}_{q,j_q}\) is the parenthesized
trace modulo \(p^{\nu-j_q}\) in (3.3).  The CRT units in (3.6) show why
the returned tensor need not be a standard copy of the original trace
at modulus \(M/L\).

The sparse support in (3.5) is not by itself a Fejer saving.  If
\(L\mid D\), then exactly

\[
 \sum_{\substack{|u|<D\\L\mid u}}(D-|u|)e(u\theta)
 =L\,|D_{D/L}(L\theta)|^2,
 \tag{3.7}
\]

whose \(L^1\)-mass is \(D\).  For general \(D\), the two quotient block
lengths give the same \(O(D)\) mass.  Together with the \(L^2\) return
factor in (3.6), this is an exact transform self-return obstruction,
not a power gain.

**Good-prime necessary conductor.**  Suppose \(p\geq11\), \(p\nmid K\),
and \(j_q>0\).  Set \(r=\nu-j_q\) and
\(a=\min(j_q,r)\).  From (2.9) and
\(\Psi_{p^r}(x)\equiv\Phi'(x)\pmod {p^r}\),

\[
 p^a\mid\Phi'(x)\qquad(x\in\mathcal D_q).
 \tag{3.8}
\]

After multiplication by the squared common denominator, the numerator
of

\[
 \Phi'(x)=-x^{-2}+(x-A)^{-2}+(x-V)^{-2}
          -(x-V-B_2)^{-2}
 \tag{3.9}
\]

has degree at most five: the degree-six coefficient cancels with the
sign sum \(-1+1+1-1=0\).  There are at least \(p-4\geq7\) allowed
residue classes.  Evaluation at six of them gives a Vandermonde matrix
with \(p\)-adic-unit determinant, so every coefficient of the derivative
numerator is divisible by \(p^a\).

Writing \(\Phi=N/D_0\), reduction modulo \(p\) now has derivative zero.
The reduced rational function has degree \(<p\), hence is constant; it
tends to zero at infinity, so it is zero.  Thus \(p\mid N\).  Divide
\(N\) by \(p\) and repeat \(a\) times.  With the exact numerator
(88.11), this proves the necessary congruences

\[
 p^a\mid(B_2-A),\qquad p^a\mid AV,qquad
 p^a\mid AV(V+B_2).
 \tag{3.10}
\]

For \(a=1\), (3.10) says over \(\mathbb F_p\) that the local labels are
either both diagonal or identical: these are precisely the two
same-group branches modulo \(p\).  For \(a>1\), zero-divisor mixtures
can occur, so (3.10) is used only as a necessary counting condition.
It is not substituted for the masked test (2.9).

For a fixed \(P\), hence fixed \(A\), the first two conditions in
(3.10) leave at most

\[
 {q\over p^a}\cdot q={q^2\over p^a}
 \tag{3.11}
\]

choices of \((B_2,V)\), and therefore of \(P'\).  Tensoring (3.11) over
the good unit primes gives at most \(M^2/\mathfrak a\) partners for a
fixed exact depth vector.  The number of depth vectors is
\(\prod_{p^\nu\Vert M}(\nu+1)=M^{o(1)}\).  Hence the edge set in (1.5)
has maximum in- and out-degree

\[
 \ll_\varepsilon X^\varepsilon\rho_*^2.
 \tag{3.12}
\]

This selection is made by complete \((A,B_2,V)\)-fibres, so the sum over
the base point \(x\), and hence the completed trace, is not cut apart.
Swapping \(P,P'\) translates and conjugates the local masked phase; it
preserves every \(j_q\) and \(\mathfrak a\), so the same count gives the
in-degree.  The conclusion uses only nonnull factors with
\(p\geq11\), \(p\nmid K\), and \(j_q>0\); at \(p\leq7\), \(p\mid K\),
and the full \(2\)-part it claims no congruence saving.

**Actual fourfold symbol and normalization.**  The coefficient identity
from the normalized rows is

\[
 \widehat F_{b,(x,y)}(d)
 ={e_M(dx+K(\bar x-\bar y))\over M^2}
 \sum_n I_b(n+d)\overline{I_b(n)}e_M(n(x-y)).
 \tag{3.13}
\]

Thus a shifted product has exactly \(M^{-4}\).  Reparameterizing by
(2.5) and summing the base point \(x\) gives

\[
 {1\over M^5}\sum_{n,m}
 \Omega_{b,d,u}(n,m)e_M(dV+nA-mB_2)
 \mathfrak T_M(u,A,B_2,V),
 \tag{3.14}
\]

because \(M^{-5}\mathfrak T_M=M^{-4}\sum_x\).  The actual symbol in
(3.14) is

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m),
 \tag{3.15}
\]

with phase

\[
 -\eta\lambda_b\bigl(\sqrt{|n+d+u|}-\sqrt{|n|}
 -\sqrt{|m+d|}+\sqrt{|m|}\bigr).
 \tag{3.16}
\]

Equations (3.14)--(3.16) precede every inequality in this report.  The
restriction \(x\ne y\) is exactly
\(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\).  Therefore the two restrictions
in (3.14) contain the four-Kloosterman term, both Ramanujan cross terms
with their minus signs, and the Ramanujan square with its plus sign,
exactly once.

**Coarse-group square and exact shell ownership.**  Let \(m\mid M\),
\(R=M/m\), and let \(\Gamma_m(P)\) be the Round-87 group of the
reduction of \(P\) modulo \(m\).  Set

\[
 K_{b,m,\gamma}=\sum_{\Gamma_m(P)=\gamma}f_{b,P}.
 \tag{3.17}
\]

At a local factor \(p^s\Vert m\), the inactive coarse group contains
\(\varphi(p^s)\) coarse diagonal pairs, while each active group contains
one coarse pair and there are \(\varphi(p^s)(\varphi(p^s)-1)\) of them.
Consequently

\[
 \sum_\gamma N_\gamma^2\leq X^\varepsilon m^2,
 \tag{3.18}
\]

where \(N_\gamma\) is the number of coarse pairs in the group.  Every
coarse pair has at most \(R^2\) fine unit lifts.  Notice that an inactive
coarse **group** can therefore have more than \(R^2\) fine pairs; the
valid assertion is the square-sum (3.18).  From (2.4), pointwise in
\(\theta\),

\[
 \sum_\gamma|K_{b,m,\gamma}(\theta)|^2
 \ll_\varepsilon X^\varepsilon
 M^2R^2T^4Q^{-5/6}.
 \tag{3.19}
\]

The kernel which deletes only the literal integer shift \(u=0\) is

\[
 \mathcal K_D^\circ(\theta)=|D_D(\theta)|^2-D,
 \qquad \|\mathcal K_D^\circ\|_1\leq2D.
 \tag{3.20}
\]

It follows that the exact coarse equality relation modulo \(m\), with
\(u=0\) excluded, costs

\[
 \ll_\varepsilon X^\varepsilon
 D B^3R^2T^4Q^{-5/6}
 \tag{3.21}
\]

after summing \(b\asymp B\).  This uses \(U=D\), not \(U\asymp B\).

The shell of exact local group exponents \((s_p)_p\) has indicator

\[
 \prod_{s_p<\nu}
   \bigl(\mathbf1_{E_{p^{s_p}}}-
         \mathbf1_{E_{p^{s_p+1}}}\bigr)
 \prod_{s_p=\nu}\mathbf1_{E_{p^\nu}}.
 \tag{3.22}
\]

Expanding (3.22) produces at most \(2^{\omega(M)}\) coarse equality
relations, all at moduli \(m'\) with \(M/m'\leq\rho\).  Thus it is an
exact one-count Möbius difference on the prime-power divisor lattice;
no same-group intersection is counted again.  Summing all
\(\rho\leq\rho_*\) costs only \(X^\varepsilon\) divisor factors.  Finally,

\[
 {D B^3\rho_*^2T^4Q^{-5/6}
  \over (D/B)J^{14/5}}
 \ll \rho_*^2B^4J^{-11/15}\leq1,
 \tag{3.23}
\]

which proves (1.3).

For any selected directed physical-edge set of maximum in- and
out-degree \(\Delta\), (3.20), the arithmetic-geometric mean inequality,
and (2.4) similarly give

\[
 \left|\sum_b\int\mathcal K_D^\circ
  \sum_{(P,P')\in\mathcal E}f_{b,P}\overline{f_{b,P'}}\right|
 \ll_\varepsilon X^\varepsilon
 D B^3\Delta T^4Q^{-5/6}.
 \tag{3.24}
\]

Equations (3.12), (3.23), and (3.24) prove the additional deletion
(1.5), since its exponent ledger is exactly

\[
 \Delta B^4J^{-11/15}
 \ll_\varepsilon X^\varepsilon
 \rho_*^2B^4J^{-11/15}\leq X^\varepsilon.
 \tag{3.25}
\]

There is no assertion that a small/bad-prime period, a nonunit-\(K\)
period, or an aperiodic tensor satisfies (1.5).  Subtracting the two
proved pieces from the exact cross-group sum gives (1.6) without
changing any sign or Fourier owner.

## 4. First doubtful or unproved step

The first unproved inequality is the target bound for the exact signed
remainder (1.6):

\[
\begin{aligned}
 &\left|\sum_{b\asymp B}
  \sum_{\substack{\rho(A,B_2,V)>\rho_*\\
        \mathfrak a(A,B_2,V)<M^2/\rho_*^2}}
  \sum_{0<|u|<D}(D-|u|)
  \sum_{d,n,m}^{\rm deep}
  {\Omega_{b,d,u}(n,m)\over M^5}
  e_M(dV+nA-mB_2)
  \mathfrak T_M(u,A,B_2,V)\right|\\
 &\hspace{45mm}\stackrel{?}{\ll}_\varepsilon
 X^\varepsilon {D\over B}J^{14/5}.
\end{aligned}
 \tag{4.1}
\]

The superscript `deep` means the exact signed \(\Pi_{b,D}\) multipliers,
the support \(D_1<|d|<\Delta_b-E_*\), and zero-extension of every \(I_b\);
it is not a new smooth majorant.

Neither exact period support nor current row norms prove (4.1).
Coefficientwise use of (3.5) loses the \(L^2\) return factor, while the
Fejer kernel (3.7) has unchanged mass.  Coarse positivity proves the
combined shells in (1.3), but period depth is not an equivalence
relation on Round-87 groups, so one cannot take an arbitrary
partial-period or aperiodic subset out of a coarse square.  A new signed
estimate coupling the actual symbol (3.15), the varying modulus, and
the residual tensor in (3.6) is still required.

The smallest especially important pieces of (4.1) are:

- small-prime masked periods, including one-allowed-residue strata;
- nonunit-\(K\) and genuine \(2\)-adic finite-difference periods;
- good-prime aperiodic factors and good-prime partial lifts with
  insufficient \(\mathfrak a\);
- every nonzero modulus multiple of \(u\) or \(d\) that remains in the
  deep support.

## 5. Required control tests and outcomes

- **External normalization and physical factor: pass.**  The only row
  normalization is the \(M^{-1}\) in each \(\mathcal R_{b,x}\).
  Equation (3.13) has \(M^{-2}\), (3.14) has \(M^{-4}\sum_x\), and no
  second \(M^{-2}\) was inserted.  Squaring (2.4) retains the physical
  \(Q^{-5/6}\), i.e. \(Q^{-5/12}\) per shifted pair.

- **Full-factor and one-count ownership: pass.**  CRT is over
  \(q=p^\nu\Vert M\), never over prime fields.  Formula (3.22) assigns
  every ordered cross edge one maximal group-depth vector.  The
  \(\rho=1\) shell is exactly the already owned Round-87 same-group
  package and is not reintroduced.

- **Global diagonal and Fejer scale: pass.**  The literal integer
  \(u=0\) coefficient is removed by (3.20), while nonzero
  \(u\equiv0\pmod M\) remains.  The proof uses \(U=D\) throughout.
  Bounding with \(|D_D|^2-D\) rather than \(|D_D|^2\) is essential;
  the latter would silently restore the owned global diagonal.

- **Bad primes, mask, and full \(2\)-part: pass.**  The finite test
  (2.9) includes all four unit conditions.  At \(p=2\), (2.10) and
  (2.9) give the entire classification.  For example,
  \(q=3^\nu,(A,B_2,V)=(0,1,0)\), \(\nu\geq2\), has allowed residue
  \(x=2\pmod3\) and a
  period \(3^{\nu-1}\); and
  \(q=5^\nu,(A,B_2,V)=(1,2,2)\), \(\nu\geq2\), has allowed residue
  \(x=3\pmod5\) and a
  period \(5^{\nu-1}\), although its numerator coefficients are
  \(p\)-adic units.  These checks falsify numerator-only depth.  The
  first example does not become same-group modulo \(q/3\), so it also
  falsifies identification of additive period with coarse group depth.

- **Actual fourfold symbol and Ramanujan signs: pass.**  Equations
  (3.14)--(3.16) occur before absolute values.  Centering by \(x\ne y\)
  keeps the four-Kloosterman main, the two negative Ramanujan crosses,
  and the positive Ramanujan square exactly once.

- **Signs, support, perfect powers, and modulus multiples: pass.**
  Negative \(u,d\), reflected orientations, deep endpoints, and
  nonzero modulus multiples are untouched.  No derivative
  nonresonance is assumed, so perfect-power stationary resonances are
  included rather than deleted.

- **Transform self-return and downstream scope: pass.**  Equations
  (3.3) and (3.7) expose both the \(p^{2j}\) trace inflation and the
  unchanged Fejer mass.  No claim is made for \(C>J^{3/4}\), raw
  transitions, axes, cone edges, other radial sectors, full \(M9-M1\),
  \(M9-M2\), \(M9\), endpoint uniformity, R5-Full, or the global
  exponent.  No external theorem is invoked.

## 6. Dependencies and exact artifacts used

The derivation used, completely and only, the permitted artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md`;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/aligned_mode_aggregate_attack.md`;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_normalization.md`;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_crt_fejer.md`.

No sibling Round-88 report was read.  Bounded residue checks at
\(3^\nu,5^\nu\), and \(2^\nu\) were used only to falsify candidate
classifications and to check (2.9); all promoted statements above have
algebraic proofs.

## 7. Recommended state effect

**Promote after review** the reciprocal masked-weight full-prime-power
conductor (2.9), the \(p^{2j}\) tensor descent (3.3)--(3.6), the exact
group-depth Möbius ownership (3.22), and the target-safe deletions
(1.3) and (1.5).  **Retain** the full Round-88 target as uniformly open
over the frozen \(B\)-range, with
\(\mathcal G_{\rm hard}(D)\) in (1.6)/(4.1) as the authoritative signed
survivor.  **Reject** both of the following shortcuts: classifying
periods from (88.11) without the mask, and identifying additive period
depth with coincidence of Round-87 labels modulo the descended
modulus.

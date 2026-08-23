# Conductor candidate: dual product defect and stationary involution

Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`

Starting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`

Status: conductor candidate. The strict-interior algebra below is exact
once the first two scalar stationary phases are taken, but the complete
literal transform, endpoint ledger, aggregate error, and any estimate
remain pending independent and hostile review.

## 1. Double-character principal phase

For a fixed literal correlation label \((k,h)\), expand both characters
using

$$
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
$$

With the Fourier convention in the Round-124 packet, the stationary
\(r\)-mode can be written as a positive odd integer

$$
 p=-4(m-\sigma/4),\qquad \chi_4(p)=\sigma,
$$

and the stationary \(s\)-mode as

$$
 q=4(n-\tau/4),\qquad \chi_4(q)=-\tau.
$$

The interior saddles are

$$
 r_*=2\sqrt{\frac{M(k+h)}p},qquad
 s_*=2\sqrt{\frac{Mk}q},
\tag{124.C1}
$$

and the phase is

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\}.
\tag{124.C2}
$$

The \(r\)- and \(s\)-Gaussian units are \(e(1/8)\) and \(e(-1/8)\).
Their product is one, and the two character-Poisson coefficients multiply
to

$$
 -\frac{\sigma\tau}{4}
 =\frac{\chi_4(p)\chi_4(q)}4.
\tag{124.C3}
$$

Before the literal profiles are evaluated, the product of the two scalar
stationary amplitudes and the original \((k+h)^{-1}k^{-1}\) weight is

$$
 \frac{4M^{1/2}}
 {(k+h)^{3/4}k^{3/4}p^{3/4}q^{3/4}}.
\tag{124.C4}
$$

At (124.C1), the two sampled profiles become
\(q_L((X/M)p)\) and \(q_L((X/M)q)\), so \(p,q\asymp L\). Formula
(124.C4) is only the strict-interior principal coefficient. It does not
replace the complete endpoint and error ledger.

## 2. Product defect is not the alias defect

Put

$$
 \mathcal N=p(k+h)-qk=ph-(q-p)k.
\tag{124.C5}
$$

Then

$$
 \Theta=\sqrt M\,
 \frac{\mathcal N}
 {\sqrt{p(k+h)}+\sqrt{qk}}.
\tag{124.C6}
$$

Since \(K\asymp L H_0^2\), \(|h|<H_0\), and distinct positive odd
\(p,q\asymp L\) differ by at least two, uniformly on fixed common
interiors,

$$
 \begin{aligned}
 p\ne q&:\quad |\mathcal N|\asymp |p-q|K,\\
 p=q,\ h\ne0&:\quad |\mathcal N|=p|h|\asymp L|h|.
 \end{aligned}
\tag{124.C7}
$$

Thus \(\mathcal N=0\) if and only if \(p=q,h=0\). This exact product
equality is much narrower than the live reciprocal-alias lattice.

Indeed, differentiating (124.C2) gives

$$
 \boxed{
 \partial_k\Theta
 =\frac{\sqrt M}{2}
 \left(\frac{\sqrt p}{\sqrt{k+h}}-
       \frac{\sqrt q}{\sqrt k}\right)
 =M\left(\frac1{r_*}-\frac1{s_*}\right).}
\tag{124.C8}
$$

The numerator of this derivative is not \(\mathcal N\).  If

$$
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h,
\tag{124.C8a}
$$

then rationalization gives the exact identity

$$
 \partial_k\Theta
 =\frac{\sqrt M\,\mathcal G}
 {2\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}}.
\tag{124.C8b}
$$

Thus product equality \(\mathcal N=0\) and derivative resonance are
arithmetically different conditions even before reducing modulo the
integer alias lattice.

Hence the integer stationary label dual to \(k\) is exactly the primal
reciprocal alias \(j\). A count of \(\mathcal N=0\) cannot control
nonzero integer crossings of (124.C8).

More quantitatively, on fixed interiors,

$$
 p\ne q:\quad
 |\partial_k\Theta|\asymp \frac{D|p-q|}{L}\gg1,
\tag{124.C9}
$$

while

$$
 p=q:\quad
 |\partial_k\Theta|\asymp \frac{D|h|}{K}.
\tag{124.C10}
$$

Consequently the primal zero-alias range appears inside the equal-mode
sector at shifts \(|h|\ll K/D\), while unequal modes and equal modes with
larger shifts populate nonzero aliases. This is a scale statement, not an
endpoint-exact partition.

## 3. Full stationary gradient and inverse phase

The remaining exact gradient identities are

$$
 \partial_h\Theta=M/r_*,\qquad
 \partial_p\Theta=r_*/4,qquad
 \partial_q\Theta=-s_*/4.
\tag{124.C11}
$$

Let \(d\) and \(j\) be the continuous stationary labels dual to \(h\)
and \(k\):

$$
 d=\partial_h\Theta,qquad j=\partial_k\Theta.
\tag{124.C12}
$$

Then

$$
 r_*=M/d,qquad s_*=M/(d-j),
\tag{124.C13}
$$

and the inverse relations are

$$
 p=\frac{4d^2(k+h)}M,qquad
 q=\frac{4(d-j)^2k}M.
\tag{124.C14}
$$

At a simultaneous \((k,h)\) saddle,

$$
 \Theta-jk-dh=jk+dh.
\tag{124.C15}
$$

The right side is exactly the original correlation phase at the ideal
reciprocal selectors \(d=M/r_*\) and \(j=M(1/r_*-1/s_*)\). Thus a
complete second stationary transform has the primal phase as its Legendre
phase.

The product defect also factors at this saddle as

$$
 \mathcal N
 =\frac4M(dh+jk)
 \{d(k+h)+(d-j)k\}.
\tag{124.C16}
$$

Its first factor is the original correlation phase, not the original
near-alias defect \(E\).

There is a sharper scope check.  Substituting (124.C13) into the physical
defect gives

$$
 E_*=M(s_*-r_*)-jr_*s_*=0.
\tag{124.C16a}
$$

Equivalently, \(E_*=r_*s_*(\partial_k\Theta-j)\).  Thus every simultaneous
\((k,h)\) principal saddle lies on the already-safe exact-alias manifold.
The live \(E\ne0\) near-alias sum is a discrete collar around that manifold,
not a collection of the principal stationary points.

## 4. Hessian and capacity self-return

The \((k,h)\)-Hessian is everywhere nondegenerate on positive interior
support:

$$
 \det\nabla^2_{k,h}\Theta
 =-\frac{M\sqrt{pq}}
 {16(k+h)^{3/2}k^{3/2}}<0.
\tag{124.C17}
$$

It has one positive and one negative eigenvalue, so its two-dimensional
Gaussian unit is one. Its stationary amplitude is

$$
 |\det\nabla^2_{k,h}\Theta|^{-1/2}
 =\frac{4(k+h)^{3/4}k^{3/4}}
 {M^{1/2}(pq)^{1/4}}.
\tag{124.C18}
$$

Multiplying (124.C18) by (124.C4) leaves \(16/(pq)\) before the
character coefficient, lattice spacings, Fejer weight, and transformed
profiles are restored. Thus full Hessian rank supplies no visible
\(D/L\) factor; the phase map (124.C12)--(124.C15) returns to the primal
alias and reciprocal-selector variables.

For orientation only, the fixed-\((p,q)\) gradient image has nominal
lattice area

$$
 KH_0\,|\det\nabla^2_{k,h}\Theta|
 \asymp \frac{XLH_0}{K^2}
 =\frac{D^3}{L\sqrt X}.
\tag{124.C19}
$$

After the literal outer weight, the nominal principal coefficient per
stationary image point is \(\asymp\sqrt X/(DL)\).  Hence the unsigned
principal-symbol capacity over all \(p,q\asymp L\) is \(\asymp D^2\);
even an assumed square-root cancellation in the \(L^2\) character pairs
would leave \(D^2/L\), exceeding \(\sqrt X\) by

$$
 Q=\frac{D^2}{L\sqrt X}\to\infty.
\tag{124.C20}
$$

This is a capacity diagnostic for naive norms, not an asymptotic lower
bound.  In particular, \(p=q,h\ne0\) is not a positive norm diagonal,
and the near-alias indicator cannot be carried rowwise through the two
character Poisson transforms.

This proves an exact principal-phase involution, not a lower bound and not
a complete transform theorem. The full literal claim still needs uniform
stationary and endpoint expansions and an aggregate error at the shifted
energy scale.

More fundamentally, the physical restriction
\(j\ne0,E\ne0,|E|\le X^{1+\rho}/L\) couples \(r\) and \(s\).  It cannot be
passed through the two rowwise character-Poisson formulae as separate
one-variable amplitudes.  Transforming the full Gram and then subtracting
the already-safe physical packages spreads each subtraction over all dual
labels.  Therefore (124.C1)--(124.C20) do not furnish a dual formula for
the Round-123 survivor.

## 5. First unproved step and proposed disposition

The product-equality diagonal (124.C7) is target-sized at the nominal
principal scale, but it does not contain all primal zero aliases. The
equal-mode shifted sector contains the already known derivative crossings,
and every unequal mode has many nonzero alias labels. Therefore neither
product-defect rigidity nor Hessian nondegeneracy estimates the complete
signed near-alias survivor.

The first unproved step remains a noninvertible inequality before the
second stationary transform, jointly across \((p,q,k,h,j)\), with both
characters and every literal profile retained. If independent reports
find no such inequality, retain (124.C5)--(124.C18) only as a scoped
stationary-lattice self-return and park this UNBAL mechanism. Do not infer
the flat-smooth target, complete UNBAL, M9-M2, M9, the quarter theorem, a
signed lower bound, or any exponent change.

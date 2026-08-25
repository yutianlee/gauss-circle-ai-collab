# Round 146 discovery cross-review of the blind three-variable report

- Campaign: m9-m1-lower-cone-three-variable-hessian-dispersion-gate
- Reviewed artifact: reports/blind_three_variable_dispersion_feasibility.md
- Reviewer role: discovery, post-unmask cross-review
- Starting graph SHA-256: 7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d

## 1. Verdict

\[
\boxed{\mathsf{CONDITIONAL\ GREEN:\ one\ mandatory\ post\!-\!unmask\
supersession,\ no\ change\ to\ the\ method\ no\!-\!go}.}
\]

The blind report is algebraically sound on the coefficient bijection,
factor-count bound, Hessian and eigenvalues, cone aspect inequalities,
empty \(E=1\) face, bounded-\(E\) forcing, \(T=1\) and \(D=1\) faces,
adversarial-coefficient scope, exceptional family, and first Legendre
transform.  Its conclusion is correctly calibrated as a no-go for a
Hessian-only or coefficient-blind method, not as a lower bound for the
actual scalar.

One correction is mandatory before the report is used in synthesis:
the conductor/discovery unmasking lemma supersedes every sentence that
treats the nearest-square mask as a remaining amplitude, smoothing, or
collar obstruction.  The mask formula remains correct diagnostic
geometry, and the \(N=sL^2+1\) family remains a valid nonresonance
control, but the active first-open scalar is target-equivalent to the
unmasked small-\(t\) scalar.

With that supersession, the report is GREEN evidence for
\(\mathsf{three\_variable\_dispersion\_no\_go}\).  It is not GREEN for
the target estimate or for a strict fixed-power intermediate-\(t\)
reduction.

## 2. Coefficient and multiplicity audit

The coefficient

\[
\begin{aligned}
\mathcal A(t,d,e)
={}&\mathbf 1_{\{\mu^2(de)=1\}}\mathbf 1_{\{e\ {\rm odd}\}}\chi_4(e)\\
&\times
\sum_{\substack{\gamma\mid t,\ \mu^2(\gamma)=1,\ \gamma\ {\rm odd}\\
(\gamma,de)=1}}\chi_4(\gamma)
\sum_{\substack{ab=t/\gamma,\ b\ {\rm odd}\\eb^2>4da^2}}1
\end{aligned}
\]

is exactly the accepted squarefree-common-kernel contribution for the
ordered factorization \(de=s\).  The prime-valuation inverse

\[
h=\gamma da^2,\qquad r=\gamma eb^2,\qquad
s=de,\qquad t=\gamma ab
\]

is bijective.  The report correctly retains all of the following:

- \(de\) squarefree, hence \(d,e\) squarefree and \((d,e)=1\);
- \(\gamma\) squarefree and \((\gamma,de)=1\);
- odd \(\gamma,e,b\), with all powers of two forced to the \(d,a\)
  sides;
- character \(\chi_4(\gamma)\chi_4(e)\);
- strict cone \(eb^2>4da^2\);
- no false coprimality on \(a,b\), or between \(\gamma\) and \(a,b\).

The bound

\[
|\mathcal A(t,d,e)|
\le \sum_{\gamma ab=t}1=d_3(t)\ll_\varepsilon t^\varepsilon
\]

is correct.  The blind report does not state the alternative full-gcd
formula, but that omission is harmless for its statement-only
derivation: the formula it does use is exact and multiplicity one.

The extra support \(de>M^{1/2}\) in its equation (2.1) is not an
unlicensed restriction.  It follows strictly from
\(t<M^{1/4}\) and \(t^2de\ge M\).

Verdict on this seam: **GREEN without correction**.

## 3. Hessian and transform audit

For

\[
f(t,d,e)=\sqrt N\,t\sqrt{de},
\]

the blind derivative matrix is correct:

\[
f^{-1}\operatorname{diag}(t,d,e)\nabla^2f
\operatorname{diag}(t,d,e)
=
\begin{pmatrix}
0&1/2&1/2\\
1/2&-1/4&1/4\\
1/2&1/4&-1/4
\end{pmatrix}.
\]

Its eigenvalues are

\[
-\frac12,\qquad \frac1{\sqrt2},\qquad-\frac1{\sqrt2},
\]

and its determinant is \(1/4\).  The unscaled identity

\[
\det\nabla^2 f
=\frac{f^3}{4t^2d^2e^2}
=\frac{N^{3/2}t}{4\sqrt{de}}
\]

is also correct.  Freezing \(t\) leaves the rank-one \(d,e\) matrix

\[
\begin{pmatrix}-1/4&1/4\\1/4&-1/4\end{pmatrix},
\qquad \det=0,
\]

whereas freezing \(d\) leaves a \(t,e\) determinant \(-1/4\).

The critical-point calculation in the blind report is GREEN.  For the
general phase \(c\,t\sqrt{de}\), the exact Legendre coefficient map is

\[
\mathcal L(c)=-\frac2c,\qquad
\mathcal L^2(c)=c.
\]

Thus the displayed dual phase
\(-2p\sqrt{qr}/\sqrt N\) is not merely similar: the full monomial
transform is involutive.  For completeness, on a box with

\[
F=\sqrt{NM},\qquad V_3=TDE\asymp M/T,
\]

the dual alias count and one-alias stationary amplitude are

\[
Q\asymp\frac{F^3}{V_3},
\qquad
|\det\nabla^2 f|^{-1/2}\asymp\frac{V_3}{F^{3/2}}.
\]

Aliaswise modulus therefore costs \(F^{3/2}\), and the physical
\(M^{-3/4}\) weight leaves \(N^{3/4}\).  This strengthens, but does not
alter, the blind report's conclusion that a signed dual estimate is
still missing.  Boundary terms cannot improve this optimistic modulus
ledger.

Verdict on this seam: **GREEN; add the displayed involution and power
ledger in conductor synthesis**.

## 4. Cone, aspects, and short-face audit

The blind implication

\[
\frac ba\le ab=\frac t\gamma\le t
\quad\Longrightarrow\quad et^2>4d
\]

is correct.  Combining it with \(m=t^2de\asymp M\) gives

\[
d^2<\frac m4,\qquad
e^2>\frac{4m}{t^4},\qquad
D\ll M^{1/2},\qquad
E\gg\frac{M^{1/2}}{T^2}.
\]

All resulting face conclusions check:

1. \(E=1\) is empty, because it would force
   \(t^4>4m\ge4M\), contrary to \(t^4<M\).
2. If \(1\le e\le K\), then

   \[
   t>\frac{\sqrt2\,M^{1/4}}{\sqrt e},
   \qquad
   \frac{M^{1/4}}t<\sqrt{\frac e2}.
   \]

   Hence every fixed bounded-\(E\) face lies in a terminal
   target-safe \(T\)-range.  This does not dispose of a growing short
   \(E\).
3. \(D=1\) is not excluded.  At \(t=d=1\),

   \[
   \mathcal A(1,1,e)
   =\mathbf 1_{\{e\ {\rm squarefree,\ odd},\ e>4\}}\chi_4(e),
   \]

   so this face is literal.
4. At \(t=1\),

   \[
   \mathcal A(1,d,e)
   =\mathbf 1_{\{\mu^2(de)=1,\ e\ {\rm odd},\ e>4d\}}\chi_4(e).
   \]

   Its weighted absolute price is \(M^{1/4+o(1)}\), and its
   \(d,e\) Hessian is rank one.  Thus a theorem requiring three long
   sides is not owner-complete.

The box count \(TDE\asymp M/T\) and weighted capacity
\(X^\varepsilon M^{1/4}/T\) are correct.  Consequently every fixed
\(T=M^\theta\), \(\theta<1/4\), requires the polynomial saving
\(M^{1/4-\theta}\).

One boundary calibration should accompany the blind text.  Cone
equality is empty because \(e,b\) are odd.  Altering only \(O(1)\)
integer \(e\)-layers per factor tuple costs

\[
M^{-3/4}TDX^\varepsilon\ll X^\varepsilon
\]

using \(T<M^{1/4}\) and \(D\ll M^{1/2}\).  Thus a fixed lattice-width
cone collar is target-safe; a relative-width collar is not automatically
safe.  Similarly, one exact product-endpoint \(m\)-layer is target-safe,
but a wide radial collar is not free.

Verdict on this seam: **GREEN, with the stated collar-width
clarification**.

## 5. Mandatory post-unmask correction

The blind mask algebra is correct.  If

\[
k=\lfloor f+1/2\rfloor,\qquad \rho=f-k,
\]

then

\[
k^2-f^2=-\rho(2f-\rho),
\qquad
|\rho|>\frac{M^{3/4}}{2f-\rho}
\]

is the retained large-displacement condition, and the boundary scale is
\(M^{1/4}/\sqrt N\).

It is no longer a proof obstruction.  Let
\(T_0=\lceil M^{1/4}\rceil\) and \(J=M^{3/4}\).  The exact universe is
the disjoint union

\[
\begin{aligned}
\{t<T_0,\ |j|>J\}
\ \dot\cup\ 
\{t<T_0,\ |j|\le J\}
\ \dot\cup\ 
\{t\ge T_0\}.
\end{aligned}
\]

The accepted Round-144 absolute small-displacement owner controls the entire
\(|j|\le J\) set, hence also its small-\(t\) subset.  The accepted
Round-145 unmasked majorant controls the third set.  Therefore

\[
\boxed{\mathfrak T_N^{\rm masked,<}
=\mathfrak U_N^{\rm unmasked,<}
+O_{\varepsilon,V}(X^\varepsilon).}
\]

Only the small-\(t\), small-displacement subset is added in this
identity, so the large-\(t\) and cell errors are not counted twice.
Strict \(>\) and complementary \(\le\), the exact ceiling, exact
radicals, half-open blocks, and terminal endpoint are all preserved.

The following blind-report language must therefore be superseded:

- Section 1: the mask is not part of the remaining smooth-amplitude
  failure; retain only the exact coefficient, cone, product support,
  and endpoints.
- Section 3, “Literal mask, profile, and endpoints”: retain the mask
  formula as geometry, but replace “the statement supplies no bound for
  the resulting internal collars” by the boxed target-equivalence above.
- Section 3, transform discussion: “sharp coefficient and mask” becomes
  “sharp arithmetic coefficient, cone, product support, and endpoints.”
- Section 4: remove the nearest-square mask from the list of unmatched
  amplitude hypotheses for the active first-open scalar.
- Section 5: change
  literal_profile_mask_and_block_endpoints from “obstruction recorded”
  to “mask removed owner-completely; profile and literal endpoints
  retained.”

The exceptional \(N=sL^2+1\) calculation remains valid.  It shows that
the original mask did not enforce modular derivative separation, and
its slowly rotating terms persist in the original masked set.  It is a
diagnostic control, not a surviving amplitude seam or a lower bound.

Verdict on this seam: **AMBER as written; GREEN after the explicit
supersession above**.

## 6. Adversarial scope and no-go calibration

The adversarial array

\[
u_{t,d,e}=e(-f(t,d,e))
\]

correctly refutes any claimed saving whose coefficient hypothesis is
only \(|u_{t,d,e}|\le1\).  The blind report explicitly limits this test
to theorem scope and does not identify the adversarial array with the
actual real arithmetic coefficient.  This calibration is GREEN.

After unmasking, the no-go remains valid for the stated mechanism:

- \(\mathcal A(t,d,e)\) is still a discontinuous joint arithmetic
  coefficient, not a smooth separable tensor;
- \(T=1\) is a mandatory rank-one face with owner-sized capacity;
- \(D=1\) persists and requires a separate lower-dimensional theorem;
- a full stationary transform returns the same monomial class and
  aliaswise modulus is far above target;
- the exceptional family forbids a uniform modular derivative or dual
  separation hypothesis.

These facts do not exclude a new sign-sensitive theorem tailored to the
actual coefficient.  They prove neither that the actual scalar is large
nor that its target is false.  The correct label is a method no-go, not
a mathematical no-go for cancellation.

Verdict on this seam: **GREEN without correction**.

## 7. Recommended use and state effect

Use the blind report as independent confirmation of:

- the squarefree-common-kernel coefficient and multiplicity;
- the scaled Hessian, eigenvalues, and short-face degeneration;
- the \(M,T,D,E\) capacity and cone aspect ledger;
- the empty \(E=1\), target-safe bounded-\(E\), and mandatory
  \(T=1,D=1\) faces;
- the adversarial-coefficient scope control;
- the Legendre monomial return and exceptional family;
- \(\mathsf{three\_variable\_dispersion\_no\_go}\).

Do not carry forward its mask-as-obstacle language.  Carry forward the
post-unmask scalar instead, and add the exact involution/power ledger
from Section 3 of this review.  Retain the target and every strict
fixed-power intermediate-\(t\) estimate as open.

No change is licensed for the independent Round-138 cross owner, the
global lower-radial signed estimate, either direct M1 parent, any M2
owner, endpoint uniformity, M9, the conditional bridge, the quarter
theorem, or any global exponent.

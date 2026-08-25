# Round 145 discovery audit of the conductor candidate

- Campaign: m9-m1-lower-cone-squarefree-kernel-linearization-gate
- Candidate: conductor_round145_squarefree_kernel_reduction.md
- Role: final discovery-side audit
- Evidence read: all three Round-145 reports and both post-unmask cross-reviews
- Allocation: 100 percent analytic/source comparison; no numerical evidence

## 1. Final verdict

\[
\boxed{\mathrm{RED}}
\]

The mathematical reduction, coefficient algebra, tail ledger, source
scope, capacity direction, and downstream scope are green.  The
candidate nevertheless fails the requested typo-free and fully explicit
near-frequency seam:

1. Equation (145.C17) contains the literal text
   \(X=N=sL^2+1,qquad\), missing the backslash before \(\qquad\).
2. The following range statement must quantify “fixed small \(c\)” and
   “sufficiently large \(s\)” to guarantee simultaneously a nonempty
   integer range, the flat profile, and the small-\(t\) inequality.

The exact repairs are given in §5.  No other mathematical repair was
found.

## 2. Coefficient and bijection seams — GREEN

The candidate's squarefree-kernel formula is exact.  Given \(hr=st^2\),
put

\[
 \gamma=(\operatorname{sf}(h),\operatorname{sf}(r)),\qquad
 d=\operatorname{sf}(h)/\gamma,\qquad
 e=\operatorname{sf}(r)/\gamma.
\]

Then \(\gamma,d,e\) are pairwise coprime and squarefree, \(de=s\), and
there are unique \(a,b\geq1\) with

\[
 h=\gamma da^2,\qquad r=\gamma eb^2,\qquad t=\gamma ab.
\]

Conversely these data recover one ordered pair.  In (145.C6),
\((\gamma,s)=1\) together with \(de=s\) is exactly the omitted-looking
pairwise coprimality condition; no additional condition on \(a,b\), or
between \(\gamma\) and \(a,b\), is legal.  The parity conditions
\(\gamma,e,b\) odd, character
\(\chi_4(\gamma)\chi_4(e)\), and cone \(eb^2>4da^2\) are exact.

The full-gcd form (145.C8) is also exact.  With

\[
 G=(h,r),\qquad h=Gda^2,\qquad r=Geb^2,
\]

the only cross-side condition is \((da,eb)=1\), and \(Gab=t\).
Oddness is precisely \(Geb\) odd, the character is \(\chi_4(Ge)\),
and the strict cone is \(eb^2>4da^2\).  Writing
\(G=c\ell^2\) is unique even when \((c,\ell)>1\); no coprimality
involving \(G,c,\ell\) may be inserted.  This agrees with all three
reports and both cross-reviews.  The two candidate parametrizations
package common prime powers differently but are both multiplicity one.

## 3. Tail, owner completeness, \(t=1\), and capacity — GREEN

For the literal standard or terminal block, the fixed-\(t\) count is

\[
 \#\{s:st^2\in\mathcal I_M\}
 \leq \left\lceil\frac{2M}{t^2}\right\rceil
      -\left\lceil\frac{M}{t^2}\right\rceil
 \leq \frac{M}{t^2}+1.
\]

If nonempty, \(t^2<2M\), so this is at most \(3M/t^2\).  A terminal
endpoint only shortens the set.  Together with
\(|C(m)|\leq\tau(m)\ll_\varepsilon X^\varepsilon\) and
\(m^{-3/4}\leq M^{-3/4}\), this gives exactly

\[
 \mathcal L_M(T)
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.
\]

The mask, phase, profile, and squarefree condition are removed only
after triangle inequality on the discharged complement.  Exact radicals
are absent from the strict mask.  Integer \(t\) makes the ceiling split
in (145.C11) exact, and the logarithmic number of blocks, including the
smallest and terminal blocks, is absorbed by epsilon renaming.  Thus the
large-\(t\) complement in (145.C2) is owner-complete.

On the retained side, \(t<M^{1/4}\) and \(st^2\geq M\) give the strict
\(s>M^{1/2}\).  The available small-\(t\) triangle bound is
\(X^\varepsilon M^{1/4}\), hence \(R^{1/2+o(1)}\) on
\(M\asymp R^2\).  The candidate now phrases this only as an upper
capacity.  Its \(t=1\) statement is correctly limited: that isolated
layer gets no cancellation from the \(t\)-variable, while cancellation
across \(s\), between layers, or between blocks remains possible.
\(C(p)=\chi_4(p)\) proves nonvacuity only and is not used as a density
or lower-bound claim.

The full capacity ledger is consistent:

\[
 M\ll_VR^2,\qquad
 \text{\(t\)-shell upper price }X^\varepsilon M^{1/4}/T,\qquad
 \text{small-\(t\) upper price }X^\varepsilon M^{1/4}.
\]

The source-side favorable top-box prices
\(R^{2/5+\varepsilon}\), \(R^{1/2+\varepsilon}\), and
\(R^{3/4+\varepsilon}\) are explicitly upper-bound limitations, not
lower bounds.

## 4. Mask, exceptional family, sources, and scope

### Mask algebra — GREEN

With \(x=t\sqrt{Ns}\), \(k=\lfloor x+1/2\rfloor\), and
\(\delta=k-x\), the tie is impossible and

\[
 j=\delta(2x+\delta),\qquad
 \operatorname{sgn}j=\operatorname{sgn}\delta,\qquad
 \|t\sqrt{Ns}\|=\frac{|j|}{k+t\sqrt{Ns}}.
\]

Writing \(N=Dw^2\) gives exact resonance only at \(s=D\); otherwise
(145.C16) is the correct generalized Pell norm.  These statements agree
with the reports.

### Explicit family — RED only for presentation/range precision

The underlying family is correct.  For squarefree \(s>1\),
\(X=N=sL^2+1\),

\[
 \sqrt{Ns}=sL+\rho,\qquad
 \rho=\frac1{\sqrt{L^2+1/s}+L}.
\]

When \(t\rho<1/2\), the nearest integer is \(sLt\) and

\[
 j=(sLt)^2-Nst^2=-st^2=-m.
\]

Thus \(j<0\), and on \(m\in[M,2M)\), \(M>1\), one has
\(|j|=m\geq M>M^{3/4}\).  Also
\[
 \frac1\rho=\sqrt{L^2+1/s}+L
\]
has integer part \(2L\), so the next continued-fraction quotient is
unbounded.

The candidate's equation has the missing-backslash typo, and its range
sentence does not explicitly state the constants needed to make the
profile and small-\(t\) claims literal.  This is repaired in §5.

### Primary-source claims — GREEN relative to the source report

Every candidate source statement is no stronger than the Round-145
source report:

- Uchiyama and Kaczorowski--Perelli use complete fixed
  degree-two-\(L\)-function coefficients/fixed standard twists, not
  \(C(st^2)\) with its cone and mask.
- Sun is frequency-uniform but has the Liouville coefficient and an
  insufficient top-range power.
- Schlage-Puchta is linear in the squarefree variable; reorientation in
  \(t\) does not accept the actual \(t\)-dependent coefficient and mask.
- Fixed-quadratic Diophantine constants are not uniform as the
  discriminant varies.
- Robert--Sargos and Sargos--Wu accept favorable monomial models but not
  the exact joint coefficient at target power.

The \(R^{2/5+\varepsilon}\) Sargos--Wu value is supported by the
source report's eleven-term exponent ledger; the two Robert--Sargos
prices are also stated there.  The candidate correctly presents all of
them as theorem-class or power mismatches.

### Downstream scope — GREEN

The Round-138 collar-tail cross owner remains separate.  The candidate
does not promote lower GAR, either direct M1 parent, M9-M1, any M2
owner, endpoint uniformity, M9, the conditional bridge, the quarter
target, or a new exponent.  Its first open scalar is exactly the
small-\(t\) survivor (145.C2).

## 5. Required repairs and hygiene result

Replace the first line of (145.C17) by

\[
 X=N=sL^2+1,\qquad
\]

and replace the following range sentence by the self-contained version:

> Choose \(\eta_0>0\) with \(V_{\rm low}(y)=1\) for
> \(0\leq y\leq\eta_0\), choose \(c>0\) with \(c^2\leq\eta_0\), set
> \(L=s\), and take sufficiently large squarefree \(s\) and
> \(1\leq t\leq\lfloor c s^{1/4}\rfloor\).  Then
> \(R^2m/N=m/\sqrt N\leq c^2\), \(t\rho<1/2\), and for the block
> \(M\leq m<2M\) one has \(t<M^{1/4}\) and
> \(|j|=m>M^{3/4}\).

For the nonzero-term control, the existing specialization to a
sufficiently large prime \(s=p>4\), \(t=1\), is valid.

A direct character-hygiene scan found no embedded non-whitespace ASCII
control characters, no rogue carriage returns, no NUL byte, and no
Unicode replacement character in the candidate.  The literal
\(,qquad\) token is nevertheless a typographical failure under the
conductor's requested no-typo gate.

After the two repairs above, every audited mathematical seam is GREEN
and the candidate supports only
\(\mathsf{strict\_squarefree\_kernel\_reduction}\).  On the current
file, the mandatory final verdict remains **RED**.

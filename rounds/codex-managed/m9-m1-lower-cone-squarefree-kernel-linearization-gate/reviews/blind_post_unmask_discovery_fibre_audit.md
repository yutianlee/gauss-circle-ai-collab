# Round 145 blind post-unmask discovery-fibre audit

Scope: only the discovery report and the blind report were compared, and only the five assigned seams were audited.

## 1. Full-gcd coefficient formula — GREEN

The discovery formula is multiplicity one and retains all allowed overlaps.  Starting from one ordered factorization (hr=st^2), set

\[
g=(h,r),\qquad H=h/g,\qquad Q=r/g.
\]

Then (g\mid t), ((H,Q)=1), and (HQ=s(t/g)^2).  Hence uniquely

\[
H=ua^2,\qquad Q=vb^2,qquad uv=s,qquad (ua,vb)=1,
\]

and comparison of squares gives (t=gab).  Writing the full gcd uniquely as

\[
g=c\ell^2,\qquad c={\rm sf}(g),
\]

gives exactly the discovery constraint (c\ell^2ab=t).  Conversely, a discovery tuple reconstructs

\[
h=c\ell^2ua^2,\qquad r=c\ell^2vb^2,
\]

whose product is (st^2) and whose gcd is exactly (c\ell^2), because ((ua,vb)=1).  Thus neither direction creates multiplicity.

No coprimality with (c\ell^2) may be added.  For example, a prime may occur in the full gcd and again in (u) or in (a); this simply means that after removal of the common exponent, the remaining prime power lies wholly on the (h)-side.  The sole cross-side restriction is ((ua,vb)=1).  The example (g=p^3), for which (c=p) and (ell=p), confirms that (c) and (ell) themselves may overlap and that squarefree-kernel notation does not mean ((c,ell)=1).

The remaining conditions also match the original coefficient exactly:

\[
r\text{ odd}\iff c,\ell,v,b\text{ are all odd},
\]

\[
\chi _4(r)=\chi _4(c\ell^2vb^2)=\chi _4(cv),
\]

and cancellation of the positive common factor gives

\[
r>4h\iff vb^2>4ua^2.
\]

The complete (2)-adic audit is green:

- if (2\mid s), then (v) must be odd and the unique factor (2\) of (s) is forced into (u);
- if (2\nmid s), both (u,v) are odd;
- if (2^q\Vert t) with (q>0), oddness of (r) forces (c,ell,b) odd, so (2^q\Vert a);
- if (t) is odd, then (a) is odd as well;
- no parity condition on (N) belongs in (C(st^2)).

These cover all four combinations of the parities of (s) and (t).  No coefficient repair is needed.

## 2. Equivalence with the blind full-gcd parameterization — GREEN

Let the discovery variables carry a subscript (d), and the blind variables a subscript (b).  The exact dictionary is

\[
g_b=c_d\ell_d^2,\qquad
(s_{h,b},s_{r,b},u_b,v_b)=(u_d,v_d,a_d,b_d).
\]

Under this dictionary,

\[
g_b\mid t,quad u_bv_b=t/g_b
\quad\Longleftrightarrow\quad
c_d\ell_d^2a_db_d=t,
\]

and

\[
(s_{h,b}u_b,s_{r,b}v_b)=1
\quad\Longleftrightarrow\quad
(u_da_d,v_db_d)=1.
\]

The parity conditions agree because (g_b) is odd exactly when (c_d,ell_d) are odd.  The character weights agree because

\[
\chi _4(g_b)\chi _4(s_{r,b})
=\chi _4(c_d\ell_d^2)\chi _4(v_d)
=\chi _4(c_dv_d),
\]

and the two cone inequalities are identical.  In the reverse direction, (c_d={\rm sf}(g_b)) and (ell_d=\sqrt{g_b/c_d}) are unique.  The blind formula imposes no coprimality involving (g_b), so it does not silently lose any of the discovery report's allowed overlaps.  The two formulas are exactly equivalent, not merely equinumerous.

## 3. Tail, cutoff, strict support, and endpoints — GREEN

For a literal standard block (mathcal I_M=\mathbb N\cap[M,B_M)) with (B_M\leq2M), including a terminal truncation, the exact unmasked count at fixed (t) is

\[
\#\{s\geq1:M\leq st^2<B_M\}
=\left\lceil\frac{B_M}{t^2}\right\rceil
-\left\lceil\frac{M}{t^2}\right\rceil.
\tag{3.1}
\]

If this set is nonempty then (t^2<B_M\leq2M), and therefore

\[
\#\{s\}\leq \frac{M}{t^2}+1\leq\frac{3M}{t^2}.
\]

Thus, for real (T\geq1), where (t\geq T) means (t\geq\lceil T\rceil),

\[
M^{-3/4}X^\varepsilon
\sum_{\substack{t\geq\lceil T\rceil\\t^2<B_M}}
\frac{M}{t^2}
\ll X^\varepsilon\frac{M^{1/4}}{T}.
\]

This verifies the discovery ledger (M^{1/4}/T).  Replacing (B_M) by (2M) in the upper bound is only an enlargement; the exact survivor continues to use (mathcal I_M), so neither a terminal endpoint nor the profile is lost.

The integer partition at the threshold is exact:

\[
t<M^{1/4}\iff t<\lceil M^{1/4}\rceil,
\qquad
t\geq M^{1/4}\iff t\geq\lceil M^{1/4}\rceil.
\]

When (M^{1/4}) is an integer, the equality case belongs to the large-(t) tail; otherwise the same ceiling formulas give the unique partition.  On the retained side,

\[
t^2<M^{1/2},\qquad m\geq M,
\qquad s=m/t^2>M/M^{1/2}=M^{1/2},
\]

so the discovery report's strict inequality is correct.  The blind report's abstract endpoint notation stated only (s\gg M^{1/2}); under the literal lower endpoint (A_M=M), it should be sharpened to the displayed strict (s>M^{1/2}).  If an abstract block with lower endpoint (A_M\neq M) is ever used, the exact statement is instead (s>A_M/M^{1/2}).  This is a wording normalization in the blind report, not a defect in the discovery reduction.

## 4. Mask sign, tie, radical, and Pell formulas — GREEN

The reports use opposite but equivalent signed displacements:

\[
\delta=k-x,qquad \theta=x-k=-\delta,qquad x=t\sqrt{Ns}.
\]

Consequently

\[
j=\delta(2x+\delta)=-\theta(2x-\theta),
\]

so the discovery sign ({\rm sgn}(j)={\rm sgn}(\delta)) and the blind sign ({\rm sgn}(j)=-{\rm sgn}(\theta)) agree.  The positive- and negative-(j) radical thresholds in the discovery report are the exact roots of these two quadratic inequalities; no linear approximation is substituted.

Both reports correctly prove that a half-integer tie is impossible: (x=n+1/2) would make the multiple of four (4Nst^2) equal to an odd square.  Thus the upward tie convention is recorded but never activated.

Writing (N=Dw^2) with (D) squarefree gives exact resonance precisely for (s=D).  For (s\neq D), with

\[
g_s=(D,s),\qquad q_s=Ds/g_s^2,
\]

one has (q_s>1) squarefree and

\[
\sqrt{Ns}=g_sw\sqrt{q_s},qquad
j=k^2-q_s(g_swt)^2.
\]

This is exactly the normalized version of the blind identity (j=k^2-(Ns)t^2).  It also retains the divisibility restriction on the Pell second coordinate.  The strict mask deletes (j=0) and all (|j|\leq M^{3/4}), while norms just beyond the boundary remain.  No mask repair is needed.

## 5. The (t=1) capacity statement — GREEN, with one wording repair

The mathematical claim is correctly scoped as an upper-ledger obstruction, not a lower bound.  Both reports establish only

\[
|T_{N,M}^{<}|\ll X^\varepsilon M^{1/4},
\]

and both explicitly state that this does not imply that the actual complex sum, or even its (t=1) sublayer, has large modulus.  The identity (C(p)=\chi _4(p)) for odd primes (p>4) proves that the layer is not algebraically identically zero; it does not prove positive density after the profile and displacement mask.

For (s\in[M,2M)), the (t=1) sample is a singleton within that block because (t\geq2) would give (st^2\geq4M).  Therefore a method whose only proposed gain is cancellation in the linear (t)-phase supplies no gain on that sample.  Cancellation across (s), coefficient sparsity, mask sparsity, or cancellation between layers remains possible and is not ruled out.

One discovery sentence should be tightened to prevent the word “pays” from being read as a lower bound.  Replace

> “Any procedure which estimates each fixed-(s) linear twist and then takes absolute values over (s) therefore pays (145.24) already on these singleton fibres.”

by

> “Such a procedure obtains no (t)-phase cancellation on these singleton fibres; using only the divisor envelope, its certified upper ledger is (O(X^\varepsilon M^{1/4})).  This is not a lower bound for the actual absolute mass after the coefficient, profile, and mask.”

This is a precision repair only.  The surrounding discovery text already gives the correct qualification, so the scoped no-go and the reduction remain valid.

## Final verdict — GREEN FOR THE SCOPED REDUCTION

All five mathematical seams are green.  The discovery coefficient formula is a multiplicity-one reparameterization of the blind full-gcd formula, including every allowed overlap and every (2)-adic case.  The (M^{1/4}/T) tail, exact ceiling split, strict (s>M^{1/2}) support, mask signs, impossible tie, exact-radical classification, and normalized Pell equation all check.  The (t=1) conclusion is only a capacity/no-(t)-cancellation statement and supplies no lower bound.

Recommended disposition: accept the exact coefficient algebra and large-(t) target-safe reduction for promotion after applying the one wording-only (t=1) clarification above.  Retain the small-(t) signed survivor as open.  No target or downstream claim follows from this audit.

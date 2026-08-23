# 1. Result

The movable-centre perturbation (123.C4), the exact nonzero-alias count,
the shifted van-der-Corput normalization (123.C10), and the
Fejer/autocorrelation diagonal estimate (123.C13)--(123.C14) are
valid after the explicit bookkeeping corrections below.

The quantitative off-diagonal “capacity” (123.C15) is not proved in the
candidate.  It is labeled “expected” and no joint layer-cake count is
given.  Consequently (123.C16) is only the algebraic consequence of a
heuristic input, not a rigorous self-return theorem.  What is rigorous
is narrower: all proved deletions leave the complete shifted
near-alias off-diagonal open, and neither the exact factorization nor
the two-adic congruence estimates it.

**Correction 1.**  In (123.C4), replace \(\tau(n)\) by
\(\tau(|n|)\) for \(n\ne0\), and separate \(n=0\), whose multiplicity
is \(O(R)\).

**Correction 2.**  Distinguish the exponent defining the engineered
power \(Q\) from \(t=v_2(M)\).  Divisibility by \(Q=2^q\) gives
\(v_2(M)\geq q\), unless an odd multiple of \(Q\) is explicitly chosen.

**Correction 3.**  Treat (123.C15)--(123.C16) as a heuristic capacity
calculation only.  They should not be listed as a proved no-go or
promoted lemma.

# 2. Movable-centre perturbation

Let \(|M-X|\leq U\), keep all amplitudes frozen at \(X\), and integrate
the physical centre through \(C\in[X-U,X+U]\).  From (123.C3),
\(r\asymp X/D\), and \(\Delta=D/L\),

\[
 |\mathscr R_X-\mathscr R_M^\sharp|
 \ll_A
 \frac U\Delta
 \sup_C\sum_{r,d}
 \left(1+\frac{|C-rd|}{\Delta}\right)^{-A}.
 \tag{R.1}
\]

For \(n=rd\ne0\), the number of admissible positive \(r\) is at most
\(\tau(|n|)\); the odd, dyadic, and \(W\)-support restrictions only
decrease it.  Uniformly for \(C\asymp X\),

\[
 \sum_{n\ne0}\tau(|n|)
 \left(1+\frac{|C-n|}{\Delta}\right)^{-A}
 \ll_{\varepsilon,A}\Delta X^\varepsilon.
 \tag{R.2}
\]

The missing \(n=0\) branch is \(d=0\) for every \(r\), and contributes

\[
 \ll_A \frac U\Delta R
 \left(1+\frac X\Delta\right)^{-A},
 \tag{R.3}
\]

which is rapidly target-safe after increasing \(A\).  Equations
(R.1)--(R.3) prove

\[
 \boxed{|\mathscr R_X-\mathscr R_M^\sharp|
 \ll_\varepsilon U X^\varepsilon.}
 \tag{R.4}
\]

This remains uniform for \(U\asymp X^{1/4}\): the interval of centres
is still \(C\asymp X\), and
\(\Delta=X^{\delta-\ell}>X^{1/4}\).  Thus a centre at an odd multiple
of \(Q\asymp X^{1/4}\) can be chosen within \(O(Q)\), costing the full
scalar target but no more.  The reciprocal-frequency triangle would
cost \(UK\) and is not interchangeable with (R.4).

# 3. Exact aliases and shifted normalization

For an exact nonzero alias,

\[
 E=0,\qquad
 (M-jr)(M+js)=M^2.
\]

If \(j>0\), exactness gives

\[
 M-jr=\frac{Mr}{s}>0,\qquad
 M+js=\frac{Ms}{r}>0.
\]

For fixed \(j\ne0\), each positive factorization of \(M^2\) recovers at
most one ordered pair

\[
 r=\frac{M-(M-jr)}j,\qquad
 s=\frac{(M+js)-M}j.
\]

Hence there are \(O_\varepsilon(X^\varepsilon)\) exact pairs for each
\(j\), and \(|j|\ll D\) gives

\[
 \#\{\text{exact nonzero ordered aliases}\}
 \ll_\varepsilon D X^\varepsilon
 \ll X^{1/2+\varepsilon}.
 \tag{R.5}
\]

Each literal Gram kernel has \(O(1)\) capacity, including after the
normalized \(h\)-average, so (R.5) is square-target-safe.  Negative
aliases are the swapped conjugate orientation.  The case \(j=0,E=0\)
is exactly \(r=s\) and must remain in the diagonal analysis.

**Correction 2, detailed.**  Formula (123.C8) is valid when
\(t=v_2(M)\):

\[
 \chi_4(r)\chi_4(s)
 =(-1)^{(jrs+E)/2^{t+1}},
\]

because the exponent is \(M_0(s-r)/2\), which has the same parity as
\((s-r)/2\).  If the centre is merely divisible by a selected
\(Q=2^q\), then \(t\geq q\); use different letters, or choose an odd
multiple of \(Q\) so that \(t=q\).

For the shifted Gram, extend \(z_k\) by zero.  Averaging \(H\) shifts
and applying Cauchy gives

\[
 |\sum_kz_k|^2
 \leq\frac{K+O(H)}H
 \sum_{|h|<H}\left(1-\frac{|h|}{H}\right)
 \sum_kz_{k+h}\overline{z_k}.
 \tag{R.6}
\]

For \(H\leq cK\), this is exactly the normalization in (123.C10), up
to its harmless implied constant \(K/H\).  Expanding the phase gives

\[
 e\!\left(Mk(1/r-1/s)+Mh/r\right),
\]

so (123.C11) is also correct.  The full \(h\)-sum is real and
nonnegative because it is the expansion of an averaged square; no
individual correlation is asserted to be positive.

# 4. Fejer layer cake and diagonal variation

Use the normalization

\[
 F_H(x)=
 \sum_{|h|<H}\left(1-\frac{|h|}{H}\right)e(hx)
 =\frac1H\left|\sum_{a=0}^{H-1}e(ax)\right|^2.
 \tag{R.7}
\]

For \(0<\eta\leq1/2\), let

\[
 \mathcal N(\eta)
 =\#\{r\asymp R:\|M/r\|\leq\eta\}.
\]

Choosing the nearest integer \(d\) gives
\(|M-rd|\ll\eta R\).  Grouping by
\(u=M-rd\), and using divisors of \(M-u\), yields

\[
 \mathcal N(\eta)
 \ll_\varepsilon(1+\eta R)X^\varepsilon.
 \tag{R.8}
\]

The possible zero-product exception does not occur here:
\(|u|\ll R\ll M\).  Since

\[
 F_H(x)\ll\min\left(H,\frac1{H\|x\|^2}\right),
\]

the layer \(\|M/r\|\leq1/H\) contributes
\(O((R+H)X^\varepsilon)\); the dyadic layers above it form convergent
geometric sums of the same size.  Therefore

\[
 \sum_{r\asymp R}F_H(M/r)
 \ll_\varepsilon(R+H)X^\varepsilon,
 \tag{R.9}
\]

which verifies (123.C13).

For the actual diagonal define

\[
 A_r(h)=
 \sum_k
 \frac{q_L(4X(k+h)/r^2)\,q_L(4Xk/r^2)}
 {(k+h)k}.
\]

Smooth zero extension and \(H\leq cK\) give

\[
 0\leq A_r(0)\ll K^{-1},\qquad
 |A_r(h)-A_r(0)|\ll\frac{|h|}{K^2}.
 \tag{R.10}
\]

Insert \(A_r(0)\) in the Fejer main term and bound the variation
absolutely.  With the outside factor \(K/H\) from (123.C10), the full
\(r=s\) sector is

\[
 \ll_\varepsilon
 \left(\frac RH+1+\frac{RH}{K}\right)X^\varepsilon.
 \tag{R.11}
\]

At

\[
 H_0=\left\lceil\frac{X^{1/2}}D\right\rceil,
\qquad
 \frac K{H_0}\asymp\frac{X^{1/2}L}{D}>1,
\]

one has

\[
 \frac R{H_0}\ll X^{1/2},\qquad
 \frac{RH_0}{K}\ll\frac{X^{1/2}}L.
\]

Thus (123.C14) is rigorously target-safe, including the autocorrelation
variation and shifted support edges.

# 5. Off-diagonal correction and first doubtful step

**Correction 3, decisive.**  The candidate supplies no proof of

\[
 \text{unsigned shifted off-diagonal capacity}
 \ll_\varepsilon\frac{X}{LH}X^\varepsilon.
 \tag{R.12}
\]

The \(k\)-alias condition and the \(h\)-selector are correlated through
the same \(r,s\), so multiplying two expected densities is not a
layer-cake proof.  No injective tuple parameterization, divisor bound,
or weighted incidence estimate establishing (R.12) is present.

Consequently

\[
 \frac{X}{LK}=\frac{D^2}{L^2}=\Delta^2
\]

is a correct algebraic substitution conditional on (R.12), and
\(\Delta^2>X^{1/2}\) follows from
\(\ell<\delta-1/4\).  But (123.C15)--(123.C16) do not rigorously show
that the unsigned mass has this capacity, nor would an upper bound
above target be a lower-bound obstruction.

The rigorous conclusion is only that the proved perturbation, exact
alias, and diagonal lemmas leave

\[
 0<|E|\ll X^{1+\varepsilon}/L
\]

in the complete shifted signed off-diagonal, with the literal profile
overlap and \(Mh/r\) selector retained.  The exact product
factorization is invertible on nonzero aliases and the two-adic
congruence is tautological; neither gives an estimate.  This is a
rigorous identification of the survivor, but the quantitative capacity
and self-return asserted through (123.C15) remain heuristic.

# 6. Dependencies and scope

This review used only:

1. rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/blind_integer_gram_rederivation.md;
2. rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/candidates/conductor_integerization_and_shifted_gram.md.

No other report, state file, strategy file, web source, or computation
was read or used.  The accepted conclusions remain scoped to the
literal flat-smooth UNBAL owner.  They do not estimate complete UNBAL,
M9-M2, M9, or the circle discrepancy.

# 7. Recommended state effect

**Recommended state effect: revise before promotion.**

After adding the \(n=0\) line (R.3) and separating the meanings of
\(q\) and \(t=v_2(M)\), retain (123.C4), the exact nonzero-alias count,
(123.C10)--(123.C11), and the diagonal estimate
(123.C13)--(123.C14) as candidate lemmas.

Do not promote (123.C15)--(123.C16) as a proved capacity or no-go.
Label them heuristic unless a genuine joint \(k\)-alias/\(h\)-selector
incidence theorem is supplied.  The first unproved step is the complete
signed near-alias off-diagonal estimate, exactly as stated at the end
of the candidate.

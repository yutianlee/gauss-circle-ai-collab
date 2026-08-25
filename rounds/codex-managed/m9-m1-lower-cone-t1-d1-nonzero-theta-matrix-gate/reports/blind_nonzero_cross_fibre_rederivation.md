## 1. Result

**Exact quotient-projection lemma and fixed-fold no-go.**  Use the standard
theta convention

\[
 \epsilon_a=\begin{cases}
 1,&a\equiv1\pmod4,\\
 i,&a\equiv3\pmod4.
 \end{cases}
\]

The literal \(B_j\) is complex: its real zero-extended amplitude profile is
multiplied by the exact residual phase
\(e(\sqrt{x^2-j}-x)\).  No realness or conjugacy of its Fourier
coefficients is available.

For every odd \(d\mid N\), the \(v\ne0\) restriction in (157.BL1) is
exactly the nonconstant Fourier projection of the folded physical profile
defined in Section 2.  Completing the \(v\)-sum and then applying the
outer normalization gives the exact quotient projector

\[
 \mathcal G_N(t)
 =\mathbf 1_{\,N\mid t}\,
  \mathbf 1_{\,t/N\ \mathrm{odd}}\,
  \chi_4(t/N).
\tag{1.1}
\]

The exterior \(d\) cancels in this calculation because \(dc=q\); the
completed coefficient is
\(-i\chi_4(d)T_{4N/d}(t)/(2N)\), with no remaining factor \(d\).
Consequently the completed physical sum is literally

\[
 \sum_{V<|j|\le2V}\ \sum_{x\bmod q}
 B_j(x)\mathcal G_N(x^2-j).
\tag{1.2}
\]

There is nevertheless a compulsory nonzero endpoint.  With
\(n=N/d\), \(c=4n\), and \(H=2n\), the involution
\(v\mapsto-v\pmod H\) has the nonzero fixed point \(v=n\).  Its physical
coefficient is

\[
 \widehat B_j(2dn)=\widehat B_j(q/2)
 =\sum_{x\bmod q}(-1)^xB_j(x),
\tag{1.3}
\]

independent of \(d\).  The fold is not part of the cancellation that
produces (1.1): as an individual nonzero row it retains the original
\(d\sqrt c\) factor.  For even \(N\), its arithmetic kernel is exactly,
up to one uniform sign, \(K(0,-j;c)\).  The statement gives no estimate
for the complex alternating mass (1.3), so target safety of the \(v=0\)
row does not transfer to the fold.  This is the first exact obstruction.

There is also a positive capacity conclusion.  The asymmetric cell
intervals

\[
 k^2-k+1\le N\nu\le k^2+k
\tag{1.4}
\]

tile the positive integers, giving exactly one \((k,j)\), with
\(j=k^2-N\nu\), for every positive quotient \(\nu\).  In the physical
range \(k\asymp K\) there are \(O(M)\) possible quotients.  If an
independent root estimate gives \(O(V)\) selected incidences, their true
capacity is \(O(\min(M,V))\).  A proved square-root signed incidence
bound would therefore be target-sized for every allowed \(V\).  This is
a capacity verification, not the missing cancellation theorem.

## 2. Exact statement and hypotheses

Assume the full parameter range of (157.BL1)--(157.BL2), retain the exact
complex residual phase and every literal cell, transition, and endpoint,
and use canonical residues consistently.  Put

\[
 N=2^sN_{\mathrm o},\qquad N_{\mathrm o}\ \text{odd},\qquad
 n=N/d,\qquad c=4n,\qquad H=2n.
\]

For \(y\bmod H\), define the exact folded profile

\[
 F_{j,d}(y)=\sum_{\ell=0}^{2d-1}B_j(y+\ell H).
\tag{2.1}
\]

No smoothing or endpoint extension occurs in (2.1).  Since
\(e_c(-2vx)=e_H(-vx)\),

\[
 \widehat B_j(2dv)
 =\sum_{y\bmod H}F_{j,d}(y)e_H(-vy).
\tag{2.2}
\]

Thus \(v\ne0\) is the unnormalised transform of

\[
 F_{j,d}^{\circ}(y)
 =F_{j,d}(y)-{1\over H}\sum_{z\bmod H}F_{j,d}(z),
\]

and the exact inverse normalization is

\[
 F_{j,d}^{\circ}(y)
 ={1\over H}\sum_{\substack{v\bmod H\\v\ne0}}
 \widehat B_j(2dv)e_H(vy).
\tag{2.3}
\]

Define

\[
 T_{4n}(t)=\sum_{a\bmod4n}^{*}\chi_4(a)e_{4n}(at)
\tag{2.4}
\]

and

\[
 \mathcal G_N(t)
 =-{i\over2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)T_{4N/d}(t).
\tag{2.5}
\]

Then the exact evaluation is

\[
 \boxed{\mathcal G_N(t)
 =\mathbf 1_{\,N\mid t}\,
  \mathbf 1_{\,t/N\ \mathrm{odd}}\,
  \chi_4(t/N).}
\tag{2.6}
\]

In particular, \(\mathcal G_N(0)=0\).  Let
\(\mathcal M_{\mathrm{all}}\) denote (157.BL1) with \(v\) completed and
\(\mathcal M_0\) its single \(v=0\) row.  Then

\[
 \mathcal M_{\mathrm{all}}
 =\sum_{V<|j|\le2V}\sum_{x\bmod q}
 B_j(x)\mathcal G_N(x^2-j),
\tag{2.7}
\]

\[
 \boxed{\mathcal M_{\ne0}
 =\mathcal M_{\mathrm{all}}-\mathcal M_0.}
\tag{2.8}
\]

Equation (2.8) identifies physical meaning and normalization; it uses
neither the completed selector nor the safe zero row as a new gain.

The exact complementary-mode range, including its fixed endpoint, is

\[
 \begin{aligned}
 &\sum_{\substack{v\bmod2n\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;4n)\\
 &\quad=
 \sum_{v=1}^{n-1}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;4n)\\
 &\qquad\quad+
 \widehat B_j(q/2)K(-n^2,-j;4n).
 \end{aligned}
\tag{2.9}
\]

There is no conjugation in (2.9).  The fold kernel is

\[
 K(-n^2,-j;4n)=
 \begin{cases}
 K(0,-j;4n),&s\ge2,\\
 -K(0,-j;4n),&s=1,\\
 -i\chi_4(n)\displaystyle\sum_{a\bmod4n}^{*}
 \epsilon_a^{-1}\left({4n\over a}\right)e_{4n}(-aj),&s=0.
 \end{cases}
\tag{2.10}
\]

Accordingly the fold contribution itself is

\[
 \mathcal M_{\mathrm{fold}}
 =-{i(1+i)\over2Nq}
 \sum_{V<|j|\le2V}\widehat B_j(q/2)
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{4N/d}\,
 K(-(N/d)^2,-j;4N/d).
\tag{2.11}
\]

Unlike (2.5), (2.11) retains \(d\sqrt c\).

To price the remaining complementary pairs, let \(L_B\asymp K\) be the
number of physical support cells and put
\(\beta=M^{-3/4}X^\varepsilon\).  A potentially large low-frequency band
in one \(d\)-fibre has width

\[
 R_d\asymp {H\over L_B}={2N\over dL_B};
\tag{2.12}
\]

when this number is at least one, take
\(1\le R_d\le H/(4L_B)\).  Its exact absolute price is

\[
 \begin{aligned}
 &\left|\sum_{v=1}^{R_d}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c)\right|\\
 &\qquad\le
 2\beta L_B\sum_{v=1}^{R_d}|K(-v^2,-j;c)|.
 \end{aligned}
\tag{2.13}
\]

If, only for scale pricing, one grants
\(|K|\ll_\varepsilon c^{1/2}X^\varepsilon\), then the outer factor and
\(R_d\ll H/L_B\) give

\[
 |\mathcal M_{\mathrm{principal}}|_{\mathrm{absolute}}
 \ll_\varepsilon M^{-3/4}VX^\varepsilon
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}\\R_d\ge1}}{1\over d}.
\tag{2.14}
\]

Thus centering deletes one coefficient but supplies no algebraic
cancellation in the remaining principal band.

For the nearest-cell incidence audit, define

\[
 \mathscr I_N=
 \left\{(\nu,k,j):
 \begin{array}{l}
 \nu\ge1\ \mathrm{odd},\quad k\asymp K,\quad j=k^2-N\nu,\\
 k^2-k+1\le N\nu\le k^2+k,\\
 V<|j|\le2V
 \end{array}\right\}.
\tag{2.15}
\]

Then

\[
 \#\mathscr I_N\ll M.
\tag{2.16}
\]

If a separate root count proves
\(\#\mathscr I_N\ll_\varepsilon VX^\varepsilon\), the intersection gives

\[
 \#\mathscr I_N
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{2.17}
\]

Consequently a genuine square-root signed incidence theorem at the stated
coefficient scale would cost at most

\[
 M^{-3/4}X^\varepsilon\sqrt{\min(M,V)}
 \le M^{-1/4}X^\varepsilon.
\tag{2.18}
\]

## 3. Proof or derivation

Splitting \(x\bmod q\) into its \(2d=q/H\) lifts above \(y\bmod H\)
proves (2.1)--(2.2), and finite Fourier inversion proves (2.3).  This
also shows that nonzero projection removes the average of the folded
profile, not a set of physical cells.

For the completed \(v\)-sum, expand (157.BL2) and interchange \(x,a,v\).
For every odd unit \(a\bmod c\), completing the square gives

\[
 \sum_{v\bmod H}e_c(-\bar a v^2-2vx)
 =e_c(ax^2)\sum_{v\bmod H}e_c(-\bar a v^2).
\tag{3.1}
\]

The phase on the right is \(H\)-periodic.  Hence the half sum is one half
of the complete quadratic Gauss sum.  The standard evaluation gives

\[
 \sum_{v\bmod H}e_c(-\bar a v^2)
 ={1-i\over2}\epsilon_a
 \left({c\over a}\right)\sqrt c.
\tag{3.2}
\]

Indeed,
\(\epsilon_{-\bar a}^{-1}=-i\epsilon_a\) and
\((c/(-\bar a))=(c/a)\).  Multiplying (3.2) by the Salié weight in
(157.BL2) replaces
\(\epsilon_a^2(c/a)^2\) by \(\chi_4(a)\).  Therefore the completed inner
sum is

\[
 {1-i\over2}\sqrt c
 \sum_{x\bmod q}B_j(x)T_c(x^2-j).
\tag{3.3}
\]

Now retain the exterior \(\chi_4(d)d\sqrt c\) until all constants are
multiplied:

\[
 -{i(1+i)\over2Nq}\,
 \chi_4(d)d\sqrt c\,
 {1-i\over2}\sqrt c
 =-{i\over2N}\chi_4(d),
\tag{3.4}
\]

because \(dc=q\).  This is the crucial cancellation: no exterior factor
\(d\) survives in the completed selector.

It remains to evaluate the divisor sum in (2.5).  Inclusion-exclusion of
\((a,n)=1\) gives

\[
 T_{4n}(t)=2i
 \sum_{\substack{h\mid n,\ h\ \mathrm{odd}\\
 n/h\mid t,\ t/(n/h)\ \mathrm{odd}}}
 {n\over h}\mu(h)\chi_4(h)
 \chi_4\left({t\over n/h}\right).
\tag{3.5}
\]

To verify (3.5), write \(a=hb\), put \(m=n/h\), and sum odd
\(b\bmod4m\).  That sum vanishes unless \(m\mid t\) and \(t/m\) is odd;
otherwise it is \(2im\chi_4(t/m)\).

Insert (3.5) into (2.5), write \(r=dh\), and note that
\(n/h=N/(dh)=N/r\).  For each fixed odd \(r\mid N\), its coefficient is

\[
 {1\over r}\sum_{h\mid r}\mu(h).
\tag{3.6}
\]

This is one for \(r=1\) and zero for every \(r>1\).  Only \(r=1\)
survives, forcing \(N\mid t\) with \(t/N\) odd and leaving the character
\(\chi_4(t/N)\).  This proves (2.6)--(2.8).

For (2.9), pair \(v\) with \(2n-v\).  Their squares agree modulo \(4n\),
and their Fourier arguments are \(2dv\) and \(-2dv\) modulo \(q\).
Because \(B_j\) is complex, nothing identifies these two coefficients;
their literal sum is the only valid pairing.  The remaining fixed point
is \(v=n\), for which \(2dn=q/2\).

If \(s\ge2\), then \(n^2\equiv0\pmod{4n}\).  If \(s=1\), then
\(-n^2\equiv2n\pmod{4n}\) and
\(e_{4n}(2n\bar a)=-1\) for every odd \(a\).  If \(s=0\), then

\[
 e_{4n}(-n^2\bar a)=e_4(-n\bar a)
 =-i\chi_4(n)\chi_4(a),
\]

and \(\epsilon_a\chi_4(a)=\epsilon_a^{-1}\).  These cases prove
(2.10), while substitution into (157.BL1) gives (2.11).

For the low band, subtracting the fibre mean changes only the coefficient
at \(v=0\).  Every coefficient in
\(1\le |v|\le R_d\) is unchanged.  The amplitude bound gives
\(|\widehat B_j(\pm2dv)|\le\beta L_B\), proving (2.13).  Under the
conditional square-root kernel price,

\[
 {d\sqrt c\over Nq}
 \bigl(\beta L_BR_d\sqrt c\bigr)
 \ll {\beta\over d}
\]

per \(j\), since \(R_d\ll c/L_B\) and \(dc=q\).  Summing the strict
\(j\)-block yields (2.14).  This prices all complementary low modes
without asserting cancellation between them.

Finally, put

\[
 I_k=[k^2-k+1,k^2+k]\cap\mathbb Z_{>0}.
\]

The upper endpoint of \(I_k\) is \(k^2+k\), and the lower endpoint of
\(I_{k+1}\) is \(k^2+k+1\).  Since \(I_1=\{1,2\}\), the \(I_k\) partition
the positive integers.  Thus every positive \(N\nu\) determines exactly
one \(k\), and then \(j=k^2-N\nu\) is unique with
\(-k\le j\le k-1\).  Moreover \(k\asymp K\) and \(|j|\le2V\) place
\(N\nu=k^2-j\) in an interval of length \(O(K^2+V)\).  Hence

\[
 \#\{\nu\}
 \ll {K^2+V\over N}+1
 =O\left(M+{V\over N}+1\right)
 =O(M)
\tag{3.7}
\]

in the nonempty dyadic range.  This proves (2.16).  Intersecting with any
independently proved \(O(VX^\varepsilon)\) root count gives (2.17), and
(2.18) follows.

## 4. First doubtful or unproved step

The first unavailable estimate is the fixed-fold functional (2.11).
For even \(N\), (2.10) makes its divisor-coupled arithmetic coefficient
exactly the zero-row coefficient up to a uniform sign, but its physical
input is

\[
 \widehat B_j(q/2)=\sum_x(-1)^xB_j(x)
\]

rather than \(\widehat B_j(0)\).  The stated amplitude and support give
only

\[
 |\widehat B_j(q/2)|
 \le\sum_x|B_j(x)|
 \ll_\varepsilon KM^{-3/4}X^\varepsilon,
\tag{4.1}
\]

which restores the full support length.  The exact residual phase makes
this coefficient complex; it does not relate it to the zero mode.

Even after the fold is isolated, centering leaves the entire band
(2.12) unchanged.  Complementary pairing produces
\(\widehat B_j(2dv)+\widehat B_j(-2dv)\), not a difference and not a real
part, so it forces no cancellation.  The corrected incidence capacity
\(\min(M,V)\) proves that a true square-root signed theorem would be
strong enough.  What is missing is an estimate exploiting the literal
signed defect and residual phase along
\(x^2-j=N\nu\), together with a separate bound for the fold and hard
endpoints.  This is a fold/mixed-variation obstruction, not a capacity
obstruction.

## 5. Required control test and outcome

**Normalization control -- pass.**  For \(N=1\),

\[
 T_4(t)=
 \begin{cases}
 2i\chi_4(t),&t\ \text{odd},\\
 0,&t\ \text{even}.
 \end{cases}
\]

Equation (2.5) gives
\(\mathcal G_1(t)=\chi_4(t)\mathbf1_{\,t\ \mathrm{odd}}\).  This checks
the half-Gauss sign and the absence of both an extra factor two and an
extra exterior \(d\).

**Divisor-collapse control -- pass.**  The coefficient after setting
\(r=dh\) is exactly
\(r^{-1}\sum_{h\mid r}\mu(h)\), not
\(\sum_{h\mid r}\mu(h)/h\).  Thus all \(r>1\) cancel and the only
physical selector is \(x^2-j=N\nu\) with \(\nu\) odd.  This control
rejects the spurious divisor-weighted branch.

**Complex complementary-pair control -- pass.**  Directly replacing
\(v\) by \(2n-v\) gives
\(\widehat B_j(-2dv)\), with the same kernel.  The exact residual phase
prevents a conjugacy inference.  Equation (2.9), rather than a
doubled-real-part expression, is the valid strict-range identity.

**Mean-removal versus fold control -- fail for an inferred gain.**  Let

\[
 \rho_j(x)=e(\sqrt{x^2-j}-x)
\]

be the required residual phase.  On an even physical subblock
\(I\subset\{x\asymp K\}\) of sufficiently small fixed relative length,
consider the diagnostic signed profile

\[
 B_j(x)=\beta\,\rho_j(x)(-1)^x\mathbf1_I(x).
\tag{5.1}
\]

Since \(|j|\le2V\le2K\), the phase derivative on \(x\asymp K\) is
\(O(|j|/K^2)\).  On such a subblock the \(\rho_j(x)\) lie in a fixed short
arc, so

\[
 |\widehat B_j(q/2)|
 =|\beta|\left|\sum_{x\in I}\rho_j(x)\right|
 \gg|\beta||I|.
\]

By summation in adjacent pairs, the zero mode of (5.1) is only
\(O(|\beta|(1+|j|/K))\).  Thus a profile retaining the exact residual
phase can have a small ordinary mass and a support-sized complex fold.
Smooth pairwise tapers do not change the conclusion.  This is a
diagnostic control, not an assertion that (5.1) is the literal profile.

**Low-frequency centering control -- fail for an inferred gain.**  On
\(\mathbb Z/H\mathbb Z\), take a symmetric folded block with a fixed
complex phase,

\[
 F(y)=\beta\zeta\,\mathbf1_{[-L_B/2,L_B/2]}(y),
 \qquad |\zeta|=1.
\]

Its two Fourier coefficients satisfy

\[
 \widehat F(v)=\widehat F(-v)
 =\beta\zeta\,D_{L_B}(v),
\]

where \(D_{L_B}(v)\) is real and
\(|D_{L_B}(v)|\gg L_B\) for
\(1\le v\le H/(4L_B)\).  Hence their literal sum, not a conjugate pair,
is coherent and support-sized.  Subtracting the mean changes neither
coefficient.  A slowly varying residual phase can be inserted on a
shorter fixed-relative block with the same lower bound up to constants.

**Nearest-cell capacity control -- pass.**  The endpoint identity
\(\max I_k=k^2+k\) and
\(\min I_{k+1}=k^2+k+1\) proves exact tiling.  There is one \((k,j)\) per
positive quotient \(\nu\), and the physical support gives \(O(M)\)
quotients.  Conditional on an independent \(O(V)\) root count, the
capacity is \(O(\min(M,V))\), so its square root is at most \(M^{1/2}\).
The square-root-capacity test therefore passes uniformly in \(V\), but
does not prove the signed estimate.

## 6. Dependencies and exact artifacts used

The only source/context files read were:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/blind_statement.md.

The assigned report itself was reread only to perform the requested
repair.  The coordinator's statement-only follow-ups supplied the
complementary-band and nearest-cell checks, and the hostile repair
identified the exterior-\(d\) and complex-profile errors.  No proof graph,
proof draft, strategy file, conductor seed, nonblind Round-157 artifact,
sibling report, external source, or computational output was read.

The finite Fourier, Gauss-sum, divisor-collapse, fold, and cell-tiling
calculations are all displayed above.  The normalization uses the
standard \(\epsilon_a\) convention stated in Section 1.

## 7. Recommended state effect

**Retain the corrected identities and obstruction; do not promote the
target.**  Retain (2.1)--(2.10) as the candidate physical-meaning and
normalization lemma, in particular the exact projector (2.6) and the
complex complementary-pair formula (2.9).  Retain the common Nyquist fold
(2.11) as the first exact obstruction.

Also retain (2.15)--(2.18) as the corrected capacity lemma for the literal
\(N\nu\) quotient fibre: a square-root signed incidence bound would be
target-sized for every allowed \(V\).  Promotion still requires a
literal-profile signed estimate that includes the coherent low band,
the complex fold, transitions, and hard endpoints.

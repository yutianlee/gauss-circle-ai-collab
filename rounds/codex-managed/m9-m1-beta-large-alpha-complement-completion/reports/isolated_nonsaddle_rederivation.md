# 1. Result: partition lemma and statement-level no-go

The finite nonnegative one-count partition can be constructed.  In
particular, the overlap of the preliminary weights is not an obstruction
after normalization and a finite subordinate refinement.  There is an
explicit repair for which the inner cells are supported in

\[
 |\alpha|/\lambda\leq 3/4,
\]

the outer cells are supported in

\[
 |\alpha|/\lambda\geq 4/3,
\]

and the whole unsafe collar is assigned to a middle package supported
strictly inside \(2/3<|\alpha|/\lambda<3/2\).

The full packet theorem is not provable from the permitted statement,
however.  The first seam that cannot be checked is the claim that the
repaired middle multipliers are *literally* the multipliers in the
Round-41 saddle/entry/exit theorem: no Round-41 multiplier is stated in
the packet.  Beyond that seam, (46.1) is only a raw numerator.  The packet
does not give the integration domains, the Cauchy kernel and its two
signed boundary values, the denominators involving \(A,D\), amplitude
estimates, moving traces, index ranges, radial weights, or the external
operator.  Consequently the requested integration-by-parts estimate and
the \(O(X^{1/4+\varepsilon})\) ledger cannot be deduced.

This is more than a request for a routine omitted calculation.  Any
version of the claimed nonsaddle theorem whose hypotheses consist only
of the displayed phase identities is false: an admissible amplitude can
make the first outer boundary term nonzero and can make the outer
oscillatory integral divergent.  Thus the result is:

* **prove** the finite target-safe partition lemma;
* **refute** an amplitude-free nonsaddle integration-by-parts theorem;
* **leave undecided**, for lack of permitted data, the intended theorem
  for the particular unstated Round-41 amplitudes and ledgers.

# 2. Exact statement and hypotheses

Let

\[
 t=|\alpha|/\lambda,\qquad
 f(\alpha)=1-\chi _0(\alpha),\qquad \lambda>0.
\]

For a nonnegative partition, it is necessary to make explicit the
standard cutoff hypotheses

\[
 0\leq \chi _0\leq 1,\qquad
 0\leq\vartheta_0,\vartheta_1\leq1,
\]

and to assume that \(f\) vanishes on a neighborhood of \(0\).  These are
consistent with, but not all written among, the displayed conditions in
the packet.  Put

\[
 w_k(t)=\widetilde\vartheta_k(t),\qquad k\in\{0,1,\infty\}.
\]

Then \(w_k\geq0\), \(\sum_k w_k=1\), and all \(t\)-derivatives are bounded.

Choose a fixed \(C^\infty\) nondecreasing function
\(S:\mathbb R\to[0,1]\) with \(S(y)=0\) for \(y\leq0\) and \(S(y)=1\)
for \(y\geq1\).  Define

\[
 P_0(t)=1-S(24t-17),
\]

\[
 P_\infty(t)=S\!\left(\frac{24t-32}{3}\right),
 \qquad P_1(t)=1-P_0(t)-P_\infty(t).                 \tag{R46.1}
\]

The exact repair lemma is the following.

**Lemma.**  There are smooth signed selectors \(s_+,s_-\in[0,1]\), with
\(s_++s_-=1\), which agree with the positive and negative half-line
selectors wherever \(f\ne0\), such that

\[
 \eta^*_{\sigma,\ell}(\alpha,\lambda)
   =f(\alpha)s_\sigma(\alpha)P_\ell(|\alpha|/\lambda),
 \qquad \sigma\in\{+,-\},\quad
 \ell\in\{0,1,\infty\},                           \tag{R46.2}
\]

are a finite nonnegative smooth partition satisfying

\[
 \sum_{\sigma,\ell}\eta^*_{\sigma,\ell}=f.         \tag{R46.3}
\]

Moreover,

\[
 \operatorname{supp}P_0\subset[0,3/4],\qquad
 \operatorname{supp}P_\infty\subset[4/3,\infty),  \tag{R46.4}
\]

\[
 \operatorname{supp}P_1
 \subset[17/24,35/24]\Subset(2/3,3/2),             \tag{R46.5}
\]

and \(P_1=1\) on \([3/4,4/3]\).  Hence, under (46.9), both nonsaddle
classes obey

\[
 |\Psi'|\geq c_0,\qquad c_0=\log(4/3).              \tag{R46.6}
\]

The repair can be made as a literal finite refinement of the preliminary
normalized weights by using the eighteen pieces

\[
 \eta_{\sigma,k\to\ell}
   =f(\alpha)s_\sigma(\alpha)w_k(t)P_\ell(t).
                                                               \tag{R46.7}
\]

Reclassifying these pieces by \(\ell\) gives (R46.2), because
\(\sum_k w_k=1\).  Any further finite middle partition can be multiplied
into the \(\ell=1\) pieces, provided its multipliers are supplied and add
to one on \(\operatorname{supp}P_1\).

The strongest nonsaddle integration-by-parts statement implied by the
packet alone is only the following formal conditional identity.  If a
section has the form

\[
 I_{\sigma,\ell}=\int_J e^{i\Psi_\sigma(L)}
 G_{\sigma,\ell}(L)\,dL,
 \qquad \ell\in\{0,\infty\},                       \tag{R46.8}
\]

with \(G\) absolutely continuous and with legitimate endpoint limits,
then

\[
 I_{\sigma,\ell}
 =\left[\frac{e^{i\Psi_\sigma}G_{\sigma,\ell}}
 {i\Psi_\sigma'}\right]_{\partial J}
 -\int_J e^{i\Psi_\sigma}
 \left{
   \frac{\partial_LG_{\sigma,\ell}}{i\Psi_\sigma'}
   -\frac{G_{\sigma,\ell}\Psi_\sigma''}
   {i(\Psi_\sigma')^2}
 \right}\,dL.                                    \tag{R46.9}
\]

No unconditional size estimate follows from (46.9) alone.

# 3. Proof and derivation

## 3.1. The overlap test and normalization

The support and plateau requirements on \(\vartheta_0,\vartheta_1\) do
not by themselves make the subtractive residual
\(1-\vartheta_0-\vartheta_1\) nonnegative.  Smooth admissible transitions
can be chosen so that, at a point in \((2/3,3/4)\), both functions equal
\(3/4\); the residual is then \(-1/2\).  They can even both equal one on a
small subinterval of that overlap while retaining all the required
plateaus and supports.  Thus a subtractive construction would fail the
nonnegativity control.

For the updated normalized weights this defect disappears.  Under
\(\vartheta_0,\vartheta_1\geq0\),

\[
 w_0=\frac{\vartheta_0}{1+\vartheta_0+\vartheta_1},\quad
 w_1=\frac{\vartheta_1}{1+\vartheta_0+\vartheta_1},\quad
 w_\infty=\frac1{1+\vartheta_0+\vartheta_1}
\]

are nonnegative and sum exactly to one.  The denominator is at least
one, so all derivatives are bounded in terms of the two fixed cutoffs.
Normalization solves nonnegativity but not support: \(w_\infty>0\)
everywhere, including the saddle collar.  That is why the second
refinement is necessary.

## 3.2. Subordinate-support repair

The transition intervals of \(P_0\) and \(P_\infty\) in (R46.1) are,
respectively,

\[
 [17/24,3/4]\quad\hbox{and}\quad[4/3,35/24].
\]

They are disjoint.  Hence \(P_0+P_\infty\leq1\), so \(P_1\geq0\).
The definitions immediately give

\[
 P_0+P_1+P_\infty=1.
\]

They also give (R46.4)--(R46.5) and \(P_1=1\) throughout the complete
unsafe collar \([3/4,4/3]\).  Multiplying the two finite partitions gives

\[
 \sum_{k,\ell}w_kP_\ell
 =\left(\sum_kw_k\right)\left(\sum_\ell P_\ell\right)=1.
\]

Thus (R46.7) is a nonnegative refinement with no subtraction.  Summing
over the old label \(k\) yields exactly \(P_\ell\), so this is an exact
reassignment rather than an estimate or a discarded overlap.

Because \(f=0\) on a neighborhood of the signed origin, choose \(s_+\)
to pass smoothly from zero to one entirely inside that zero region and
put \(s_-=1-s_+\).  Outside the zero region the selectors can equal the
literal half-line indicators.  This proves smoothness of (R46.2) and
(R46.3).  Notice that the equality is algebraic and is available before
any absolute values are taken.

For fixed \(\lambda\), the exact cutoff derivative is

\[
 \partial_LP_\ell(|\alpha|/\lambda)
 =\frac{\operatorname{sgn}\alpha}{\lambda}P_\ell'(t),
                                                               \tag{R46.10}
\]

away from zero; the product is smooth at zero because \(f\) vanishes
there.  More fully,

\[
 \partial_L\eta^*_{\sigma,\ell}
 =-\chi_0'(\alpha)s_\sigma P_\ell
   +f s_\sigma'P_\ell
   +f s_\sigma\frac{\operatorname{sgn}\alpha}{\lambda}P_\ell'.
                                                               \tag{R46.11}
\]

The middle term is identically zero if the selector transition is placed
inside the open zero set of \(f\).  Formula (R46.11) retains every
partition-cutoff derivative; none is hidden in a generic constant.

## 3.3. Nonsaddle safety

On \(\operatorname{supp}P_0\), \(0<t\leq3/4\), and therefore

\[
 |\log t|\geq\log(4/3).
\]

On \(\operatorname{supp}P_\infty\), \(t\geq4/3\), giving the same bound.
Together with (46.9), this proves (R46.6) on both signs.  The points where
the nonsaddle cutoff derivatives vary are also safe: the inner derivative
has \(17/24\leq t\leq3/4\), and the outer derivative has
\(4/3\leq t\leq35/24\).

## 3.4. Exact first integration-by-parts coefficient

Applying \(e^{i\Psi}=(i\Psi')^{-1}\partial_Le^{i\Psi}\) gives (R46.9).
Since \(\Psi''=1/\alpha\), its interior coefficient obeys only

\[
 \left|
   \frac{\partial_LG}{i\Psi'}
   -\frac{G\Psi''}{i(\Psi')^2}
 \right|
 \leq c_0^{-1}|\partial_LG|
       +c_0^{-2}\frac{|G|}{|\alpha|}.              \tag{R46.12}
\]

If \(G=\eta^*\mathcal A\), the derivative in (R46.12) contains the three
terms in (R46.11), together with
\(\eta^*\partial_L\mathcal A\).  At the level of the displayed raw
numerator, that last derivative necessarily includes the exact
\(R_\alpha'\), \(i\omega_LR_\alpha\), and \(W_j'(L-\nu)\) terms (with the
last one zero for \(j=0\)).  No bounds for any of these terms are supplied.

The moving-cutoff term has no automatic scale saving from one
integration by parts.  On either transition collar,

\[
 \int |\mathcal A(L)|\frac{|P_\ell'(t)|}{\lambda}\,dL
 =\int |\mathcal A(\lambda t-\beta)|\,|P_\ell'(t)|\,dt.         \tag{R46.13}
\]

Thus its scale capacity is \(O(1)\) times the amplitude size on the
collar, not \(O(\lambda^{-1})\).  Any power saving needed by the global
ledger must come from stated amplitude estimates, further justified
integrations by parts, or a stated signed cancellation.

For the unbounded outer sector, the first exact boundary term is

\[
 \lim_{|L|\to\infty}
 \frac{e^{i\Psi_\sigma(L)}G_{\sigma,\infty}(L)}
 {i\log(|\alpha|/\lambda)}.                       \tag{R46.14}
\]

Nothing in the packet implies that (R46.14) vanishes.  This is a genuine
mathematical obstruction to an amplitude-free lemma.  For example, fix
the positive branch, \(\lambda=1\), and take, on the ultimate outer
region, \(G(L)=\alpha=L>0\) and

\[
 \Psi(L)=L\log L-L,
\]

which satisfies exactly \(\Psi'=\log L\), \(\Psi''=1/L\).  Then the
boundary magnitude in (R46.14) is \(L/\log L\to\infty\).  The integral
itself does not exist as an ordinary improper oscillatory integral.  To
see this directly, let \(\Delta=c/\log T\) with fixed sufficiently small
\(c>0\).  For large \(T\), the phase varies by at most \(2c\) on
\([T,T+\Delta]\).  After rotation by \(e^{-i\Psi(T)}\), the real part of
the tail integral is therefore at least

\[
 \cos(2c)\int_T^{T+\Delta}L\,dL
 \gg \frac{T}{\log T},
\]

which does not tend to zero.  This violates the Cauchy criterion.  The
packet places no growth or symbol hypothesis on \(R_\alpha\), so its
displayed hypotheses do not exclude such an amplitude.  This
counterexample refutes only the amplitude-free reading; it does not
claim that the particular, but unstated, inherited \(R_\alpha\) has this
growth.

## 3.5. Coefficient and radial ledger

Even before the missing external normalization, the modulus of the only
displayed coefficient is

\[
 |\mathfrak a_{j,h,q,x}|
 =\pi\,2^{-a}X^{(1-a)/2}
 |h|^{-r}q^{-p}D_j^a(H_j+1)^b x^{-3/2-b/2},        \tag{R46.15}
\]

under the natural positivity assumptions for the scale variables.  To
deduce an \(X^{1/4+\varepsilon}\) result from (R46.15), all remaining
integrals, sums, and the external factor would have to supply an exact
net capacity of at most

\[
 X^{a/2-1/4+\varepsilon}
\]

after also accounting for the displayed \(h,q,j,x\) weights.  The packet
does not state \(a,b,p,r\), the ranges or relations among \(h,q,j,x\), the
definitions and sizes of \(D_j,H_j\), the radial measure, or the external
factor.  Therefore (R46.15) cannot be summed, and (R46.13) shows that the
phase bound alone does not fill this gap.

# 4. First doubtful or unproved step

After the explicit partition repair, the first unproved seam is the
literal-cell assertion.  Support containment in
\(2/3<t<3/2\) does not prove equality with a pre-existing cutoff.  The
packet supplies neither the Round-41 saddle/entry/exit multipliers nor a
statement saying that every smooth subordinate partition is accepted.
Accordingly it is impermissible to identify \(P_1\), or any refinement of
it, with those cells.

If that missing seam were supplied, the next unproved step would be the
legitimacy of (R46.9) for the complete singular section.  The first exact
analytic obstruction is the outer boundary term (R46.14).  Its vanishing
requires an explicit hypothesis such as

\[
 G_{\sigma,\infty}(L)=o(\log(|\alpha|/\lambda))
\]

at the relevant endpoint, together with integrability (or a signed
replacement) for the two terms in (R46.12).  Neither condition is in the
packet.  Moving trace boundaries and the signed Plemelj relation cannot
be derived because their formulas are also absent.

# 5. Control tests and outcomes

1. **`same_positive_line_antecedent`: pass algebraically.**  Multiplying
   (46.1) by (R46.7) and summing all new labels returns exactly
   \(f\mathscr H^{\rm raw}\).  No connector, compact terminal, or residue
   term is introduced.

2. **`finite_partition_exactness`: pass, conditionally on standard
   nonnegative cutoff hypotheses.**  Equations (R46.1)--(R46.7) give a
   finite, smooth, nonnegative one-count partition.  The overlap test
   shows that the earlier subtractive residual need not be nonnegative;
   normalization plus refinement is essential.

3. **`round41_literal_cell_match`: not verifiable.**  The repaired middle
   package has the right support, but no Round-41 cutoff formula is among
   the permitted data.  No equality is inferred from support alone.

4. **`inner_nonsaddle_sector`: partition pass; estimate unproved.**  Its
   support and all of its cutoff derivatives satisfy
   \(|\Psi'|\geq\log(4/3)\).  Bounds for the differentiated raw amplitude
   are absent.

5. **`outer_nonsaddle_sector`: support pass; integration-by-parts theorem
   refuted at the stated level of generality.**  The first boundary term
   is (R46.14), and the explicit amplitude \(G(L)=L\) shows that the phase
   hypotheses alone do not control it.

6. **`signed_cauchy_before_absolute`: algebraic partition pass, analytic
   control unavailable.**  The sums in (R46.3) and (R46.7) are exact and
   can be taken before absolute values.  The signed Cauchy kernels,
   orientations, jump constants, and trace formula are not stated, so
   the required Plemelj cancellation cannot be checked.

7. **`moving_trace_and_cutoff_derivatives`: cutoff part pass, trace part
   unavailable.**  The exact cutoff derivatives are (R46.10)--(R46.11),
   and their no-saving capacity is (R46.13).  No moving integration
   domain or trace map is given.

8. **`coefficient_scale_radial_sum`: fail as a certification test.**
   Formula (R46.15) is the complete deduction possible from (46.3).
   Missing index ranges, scale relations, amplitude seminorms, and radial
   measures prevent the requested sum.

9. **`collision_and_external_once`: syntactic pass only.**  The repair
   adds no collision term and applies no external operator, so it creates
   no double count.  The external operator itself is unstated, so its
   normalization and final \(X\)-power cannot be verified.

# 6. Dependencies and exact artifacts used

Only the following artifacts were used:

* `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/briefs/isolated_nonsaddle_rederivation.md`;
* `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/derivation_packet.md` (the updated normalized-weight version).

No proof graph, proof draft, prior report, synthesis, other Round-46
artifact, external source, or numerical experiment was read or used.
The counterexample and the cutoff construction are elementary symbolic
derivations from the packet's displayed phase identities.

# 7. Recommended state effect

**Revise.**  The repaired finite partition (R46.1)--(R46.7) may be retained
as a candidate lemma after the nonnegativity and zero-neighborhood
hypotheses are made explicit.  Do not promote the full Round-46 theorem.
To make it decidable, a revised statement must supply:

1. the literal Round-41 multipliers and an exact equality check with the
   repaired middle pieces;
2. the complete signed Cauchy integral, denominators, domains, trace
   orientations, and boundary terms;
3. uniform derivative and endpoint estimates for \(R_\alpha,R_\beta,
   \psi,\widehat\phi,W_j\), including the singular \(W_0=1\) share;
4. all \(h,q,j,x\) ranges and scale relations, radial weights, and the
   external normalization.

Without these additions, the target-safe support statement is proved,
but the target-safe *estimate* is neither established nor a valid
consequence of the stated hypotheses.

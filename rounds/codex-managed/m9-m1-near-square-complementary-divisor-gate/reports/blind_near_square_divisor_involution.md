# 1. Result: target-safe localization and an exact self-return/no-go

Let \(e(t)=e^{2\pi i t}\), and use
\(\widehat f(k)=\int_{\mathbb R/\mathbb Z}f(t)e(-kt)\,dt\).  Put

\[
 K_{R,y}(t)=J_{R,y}(t)(1-e(-t)).
\]

Then \(W_{R,y}(k)=\widehat K_{R,y}(k)\), and for every integer
\(A\geq 1\), uniformly in \(k\in\mathbb Z\),

\[
 |W_{R,y}(k)|\ll_A
 \frac{1}{R+|k|}\left(1+\frac{|k|}{y}\right)^{-A}.
 \tag{1.1}
\]

Thus the lower, one-sided cutoff at scale \(1/y\) really is visible:
the three Fourier ranges are \(R^{-1}\) for \(|k|\lesssim R\),
\(|k|^{-1}\) for \(R\lesssim |k|\lesssim y\), and
\(y^A|k|^{-A-1}\) for \(|k|\gtrsim y\).  In particular, if
\(0<\sigma<1/2\),

\[
 K_*:=\lceil yX^\sigma\rceil,
\]

and \(A\sigma\geq 1/4\), then the accepted exact discrepancy satisfies

\[
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{|k|\leq K_*}D_N(k)W_{R,y}(k)+O_{A,\sigma}(R).
 \tag{1.2}
\]

For all sufficiently large \(X\), every \(m=N+k\) in (1.2) is
positive.  This is a target-safe localization using no circle estimate.

On that window write

\[
 m=2^a m_0,\qquad a=v_2(m)\geq0,\qquad m_0\text{ odd},
 \qquad s=\chi_4(m_0)\in\{1,-1\},\qquad q=\frac{m_0}{y}.
\]

Define

\[
 F(m_0)=\sum_{d\mid m_0}\chi_4(d)=\frac{r_2(m)}4,
 \qquad
 L_q(m_0)=\sum_{\substack{d\mid m_0\\d<q}}\chi_4(d).
\]

The exact complementary-divisor formula, with its strict boundary, is

\[
 \boxed{
 A_y(2^a m_0)
 =F(m_0)-sL_q(m_0)
 =s\sum_{\substack{e\mid m_0\\e\geq q}}\chi_4(e).}
 \tag{1.3}
\]

For \(a=0\), the complement is literally \(d\leftrightarrow m/d\).
For every \(a\geq1\), that literal map leaves the support of
\(\chi_4\), because \(m/d\) is even for every contributing odd
\(d\).  The only valid character-preserving complement is

\[
 d\longleftrightarrow \frac{m_0}{d}=\frac{m}{2^a d},
 \tag{1.4}
\]

and its threshold is \(m_0/y=m/(2^ay)\), not \(m/y\).

Formula (1.3) gives a rigorous no-go for a gain from this involution
alone.  If \(s=-1\), then \(F(m_0)=0\) and

\[
 A_y(2^am_0)=L_q(m_0).
 \tag{1.5}
\]

The complementary operation therefore returns the original truncated
signed divisor sum exactly; its central-band identity has zero
coefficient on \(A_y\).  If \(s=1\), one gets only a factor \(1/2\)
identity involving both the full coefficient \(F=r_2/4\) and an exact
central band.  A constant factor is not a power saving, and neither of
those two terms may be dropped.  Since the map (1.4) is an involution,
there is no noninvertible algebraic contraction.  The smallest
uncontrolled survivor is \(L_q=A_y\) on the branch
\(m_0\equiv3\pmod4\); on the branch \(m_0\equiv1\pmod4\), the smallest
exact package is the pair consisting of \(r_2(m)/4\) and the central
band.  No cancellation between different \(k\)'s follows from the
pointwise involution.

# 2. Exact statement and hypotheses

The conclusions above use exactly the hypotheses in the statement-only
packet:

* \(X\geq2\) is real, \(R=X^{1/4}\),
  \(y=\lfloor\sqrt X\rfloor\), and \(N=\lfloor X\rfloor\).
* \(V_{\rm low}\) and \(\eta\) are the stated fixed smooth cutoffs.
  In particular, \(V_{\rm low}\) is identically one on a fixed
  neighborhood of zero, while the derivatives of \(\eta(yt)\) are
  confined to \(1/(2y)<t<1/y\).
* \(J_{R,y}\), \(W_{R,y}\), \(A_y\), \(c_y\), and \(D_N\) have
  exactly the normalizations in the packet, and (122.B1) is taken as
  the accepted starting identity.  No replacement of real \(X\) by
  an integer square is made.

The quantitative statement is the following lemma/no-go package.

**Wavelet-localization lemma.**  For every fixed integer \(A\geq1\),
(1.1) holds with a constant depending only on \(A\) and the two fixed
cutoffs.  For every \(K\geq y\),

\[
 \sum_{|k|>K}|D_N(k)W_{R,y}(k)|
 \ll_A y\left(\frac yK\right)^A.
 \tag{2.1}
\]

Consequently (1.2) holds for every fixed \(0<\sigma<1/2\) and integer
\(A\) with \(A\sigma\geq1/4\).

**Complete odd-part complement lemma.**  For every positive integer
\(m=2^am_0\), for every \(a\geq0\), and with no squarefree hypothesis,
(1.3) holds.  It includes all cutoff ties because its lower tail is
strict \(d<q\) and its complementary upper tail is closed
\(e\geq q\).

For the central identities, define

\[
 C_-(m_0;y)=\sum_{\substack{d\mid m_0\\q\leq d\leq y}}\chi_4(d)
 \quad(q<y),
 \qquad
 C_+(m_0;y)=\sum_{\substack{d\mid m_0\\y<d<q}}\chi_4(d)
 \quad(q>y).
\]

Then

\[
 (1+s)A_y(2^am_0)=
 \begin{cases}
 F(m_0)+C_-(m_0;y),&q<y,\\[2mm]
 F(m_0)-C_+(m_0;y),&q>y.
 \end{cases}
 \tag{2.2}
\]

At \(q=y\), necessarily \(m_0=y^2\); on the character support this
forces \(y\) odd and \(s=1\), and

\[
 2A_y(y^2)=F(y^2)+\chi_4(y).
 \tag{2.3}
\]

If \(s=1\), equations (2.2) solve for \(A_y\) but retain both the full
coefficient and the indicated central band.  If \(s=-1\), then
\(F=0\) and (2.2) says only

\[
 C_-(m_0;y)=0\quad(q<y),
 \qquad
 C_+(m_0;y)=0\quad(q>y),
 \tag{2.4}
\]

while giving no estimate at all for \(A_y=L_q\).

On the localized window the valuation branches are exhaustive:

1. If \(a=0\), put \(h=m-y^2=N+k-y^2\).  Then \(q<y\), \(q=y\), or
   \(q>y\) according as \(h<0\), \(h=0\), or \(h>0\).
2. If \(a\geq1\), then, for all sufficiently large \(X\),
   \(m_0=m/2^a<y^2\), so always \(q<y\).  More precisely, the lower
   tail in (1.3) is empty when \(q\leq1\), equivalently
   \(m_0\leq y\), and otherwise its exact threshold is
   \(1<q=m/(2^ay)<y\).  Thus no valuation, including valuations of
   size comparable to \(\log_2y\), is omitted.

If \(m_0=\ell^2\), the central divisor \(d=\ell\) is a fixed point of
the complement.  It is counted once in \(F\) and once in the relevant
central-band sum in (2.2): it lies in \(C_-\) when \(\ell<y\), in
\(C_+\) when \(\ell>y\), and is the single boundary term in (2.3) when
\(\ell=y\).  These conventions prevent the usual factor-of-two error
at a square.

Finally, if \(y\mid m_0\), the hard sample \(d=y\) is included and its
partner \(q=m_0/y\) is included at the closed complementary endpoint.
If \(y\nmid m_0\), there is no divisor on that numerical boundary.  If
\(y\) is even, \(\chi_4(y)=0\) and no contributing odd divisor can
equal \(y\); if \(y\) is odd, the contribution is exactly
\(\chi_4(y)\).  Only at \(m_0=y^2\) do the two endpoints coincide, and
then (2.3) counts the fixed divisor once rather than twice.

# 3. Proof or derivation

## 3.1 Uniform wavelet envelope

Near zero set

\[
 g(t)=\frac{1-e(-t)}t,
\]

with its removable value at zero.  All derivatives of \(g\) are
bounded on the fixed small arc.  There,

\[
 K_{R,y}(t)=\eta(yt)V_{\rm low}(4R^2t^2)g(t).
 \tag{3.1}
\]

The product is a smooth periodic function: the lower cutoff makes it
identically zero in a neighborhood of the left endpoint, and the
upper cutoff makes it zero before the end of the fixed positive arc.
Its support has length \(O(R^{-1})\), and hence

\[
 \|K_{R,y}\|_1\ll R^{-1}.
 \tag{3.2}
\]

For every \(j\geq1\), split its differentiated support into the lower
transition \(t\asymp y^{-1}\), the upper transition
\(t\asymp R^{-1}\), and the intervening region.  On the lower
transition, \(V_{\rm low}(4R^2t^2)=1\) for all sufficiently large
\(X\), so no derivative of the upper cutoff occurs there.  A term with
\(p\geq1\) derivatives on \(\eta(yt)\) has size \(O_j(y^p)\) on an
interval of length \(O(y^{-1})\).  On the upper transition \(\eta=1\),
and a term with \(p\) derivatives on the upper cutoff has size
\(O_j(R^p)\) on an interval of length \(O(R^{-1})\).  Derivatives of
\(g\) cost no scale.  Therefore

\[
 \|K_{R,y}^{(j)}\|_1\ll_j y^{j-1}+R^{j-1}\ll_j y^{j-1}.
 \tag{3.3}
\]

The finitely many smaller \(X\) are absorbed by enlarging the fixed
constant.  Periodic integration by parts, using (3.2), (3.3) with
\(j=1\), and (3.3) with \(j=A+1\), gives, for \(k\ne0\),

\[
 |W(k)|\ll_A
 \min\left\{R^{-1},\ |k|^{-1},\
                 y^A|k|^{-A-1}\right\}.
 \tag{3.4}
\]

For \(k=0\), (3.2) applies.  Splitting into
\(|k|\leq R\), \(R<|k|\leq y\), and \(|k|>y\) shows that (3.4) is
equivalent, up to a constant depending on \(A\), to (1.1).  In
particular,

\[
 \sum_k|W(k)|\ll 1+\log(y/R).
 \tag{3.5}
\]

The middle \(1/|k|\) range in (3.4) is essential.  Treating the
one-sided cutoff as though the whole kernel varied only on scale
\(1/R\) would incorrectly erase that range.

For each \(d\),

\[
 \left\lfloor\frac{N+k}{d}\right\rfloor
 -\left\lfloor\frac Nd\right\rfloor-\frac kd
 =\left\{\frac Nd\right\}-\left\{\frac{N+k}{d}\right\},
\]

so its absolute value is less than one.  Hence, uniformly for every
integer \(k\),

\[
 |D_N(k)|\leq\sum_{d\leq y}|\chi_4(d)|\leq y.
 \tag{3.6}
\]

For \(K\geq y\), (3.4), (3.6), and an integral comparison give

\[
 \sum_{|k|>K}|D_N(k)W(k)|
 \ll_A y^{A+1}\sum_{n>K}n^{-A-1}
 \ll_A y(y/K)^A,
\]

which is (2.1).  With \(K=K_*\), this is
\(O_A(X^{1/2-A\sigma})\), hence \(O_A(R)\) when
\(A\sigma\geq1/4\).  Since \(K_*=O(X^{1/2+\sigma})=o(X)\), while
\(N=X+O(1)\), one also has \(N-K_*>0\) for sufficiently large \(X\).

## 3.2 Exact two-adic complement and all boundaries

Every divisor contributing to \(A_y(2^am_0)\) is odd, so it divides
\(m_0\).  For such a divisor put \(e=m_0/d\).  Complete
multiplicativity of \(\chi_4\) on odd integers gives

\[
 \chi_4(d)=\chi_4(m_0)\chi_4(e)=s\chi_4(e).
 \tag{3.7}
\]

Also \(d\leq y\) if and only if \(e\geq m_0/y=q\).  This proves the
second expression in (1.3).  Alternatively, the omitted divisors
\(d>y\) correspond bijectively to \(e<q\), with strict inequality, so

\[
 \sum_{\substack{d\mid m_0\\d>y}}\chi_4(d)=sL_q(m_0),
\]

and subtraction from the full divisor sum proves the first expression
in (1.3).  Applying the map again returns \(d\), and its character
factor is \(s^2=1\).  Thus the operation is exactly invertible.

The standard full divisor identity is

\[
 F(m_0)=\sum_{d\mid m_0}\chi_4(d)
       =\sum_{d\mid m}\chi_4(d)=\frac{r_2(m)}4.
 \tag{3.8}
\]

The middle equality holds for every \(a\), because all even divisors
have zero character.  At the Euler-factor level, the factor is
\(\nu+1\) at \(p^\nu\) for \(p\equiv1\pmod4\), and is \(1\) or \(0\)
according as \(\nu\) is even or odd for \(p\equiv3\pmod4\); the prime
2 contributes no change.  These are exactly the factors in the
sum-of-two-squares formula.  Independently, pairing all divisors by
(3.7) gives \(F=sF\); hence

\[
 s=-1\quad\Longrightarrow\quad F=0.
 \tag{3.9}
\]

To prove (2.2), observe that

\[
 sA_y(2^am_0)=\sum_{\substack{e\mid m_0\\e\geq q}}\chi_4(e).
 \tag{3.10}
\]

If \(q<y\), the sets \(d\leq y\) and \(d\geq q\) cover all divisors
and overlap exactly on \(q\leq d\leq y\).  Adding (3.10) to the
definition of \(A_y\) yields the first line of (2.2).  If \(q>y\),
the two sets are disjoint and omit exactly \(y<d<q\), yielding the
second line.  At \(q=y\), they overlap exactly on the divisor \(y\),
which proves (2.3).  This set argument also proves all endpoint and
fixed-point conventions without an appeal to a generic nonsquare.

For the localized valuation claim, the floor relation gives

\[
 0\leq N-y^2\leq2y.
 \tag{3.11}
\]

Also \(K_*=o(y^2)\).  Hence \(m=N+k<2y^2\) throughout the window for
large \(X\).  If \(a\geq1\), then \(m_0\leq m/2<y^2\), proving the
strict below-square branch.  If \(a=0\), the sign of
\(q-y=(m-y^2)/y\) gives the three cases stated in Section 2.  Notice
also that for \(a=0\), the length of the central interval is exactly

\[
 |q-y|=\frac{|m-y^2|}{y}\leq 2+\frac{K_*}{y}\ll 1+X^\sigma.
 \tag{3.12}
\]

This narrowness is only a pointwise fact; it supplies no signed
\(k\)-estimate.  For \(a\geq1\), the central interval can instead have
length comparable with \(y\), so even that pointwise narrow-band
observation is unavailable uniformly in the valuation.

## 3.3 Full coefficient, exact complement, and the signed wavelet

Put \(b_y(m)=A_y(m)-c_y\).  Directly differencing the accepted floor
discrepancy gives the exact one-count relation

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y=b_y(N+k),
 \tag{3.13}
\]

because

\[
 \left\lfloor\frac{N+k}{d}\right\rfloor
 -\left\lfloor\frac{N+k-1}{d}\right\rfloor
 =\mathbf1_{d\mid N+k}.
\]

Since \(D_N(0)=0\),

\[
 D_N(k)=
 \begin{cases}
 \displaystyle\sum_{j=1}^{k}b_y(N+j),&k\geq1,\\[2mm]
 0,&k=0,\\[2mm]
 \displaystyle-\sum_{j=k+1}^{0}b_y(N+j),&k\leq-1.
 \end{cases}
 \tag{3.14}
\]

On the positive localized window, (1.3) says exactly

\[
 b_y(m)=F(m_0)-sL_{m_0/y}(m_0)-c_y
 =
 \begin{cases}
 F(m_0)-L_{m_0/y}(m_0)-c_y,&m_0\equiv1\pmod4,\\
 L_{m_0/y}(m_0)-c_y,&m_0\equiv3\pmod4.
 \end{cases}
 \tag{3.15}
\]

Equations (1.2), (3.14), and (3.15) are the exact localized signed
package.  In particular, the sign and phase of \(W(k)\) remain outside
the oriented cumulative sums; no absolute value has been taken and no
pairing of unrelated \(k\)'s has been asserted.

For diagnosis only, full discrete summation by parts (justified by the
rapid Fourier decay for fixed \(X\)) also gives

\[
 \sum_{k\in\mathbb Z}D_N(k)
       (\widehat J(k)-\widehat J(k+1))
 =\sum_{j\in\mathbb Z}(A_y(N+j)-c_y)\widehat J(j).
 \tag{3.16}
\]

Moreover \(\sum_j\widehat J(j)=J(0)=0\), because the lower cutoff makes
\(J\) vanish near zero.  Thus (3.16) merely rewrites the same object as
a one-count sum.  On positive \(N+j\), substituting (1.3) produces the
full \(r_2/4\) coefficient together with its exact complementary tail.
It is not permissible to retain the first and discard the second, or
vice versa.  Nor is (3.16), by itself, an estimate.

The no-go now follows algebraically.  On \(s=-1\), (2.2) annihilates
the coefficient \(1+s\) of \(A_y\), leaving only the true identity
that the central signed band is zero.  The quantity that must be
estimated in (3.14) is still \(A_y=L_q\).  On \(s=1\), solving (2.2)
costs only the constant \(1/2\) and leaves both \(F=r_2/4\) and the
central band.  The complement is pointwise in \(m=N+k\); it supplies
no relation between \(W(k)\) and \(W(k')\), and the valuation and
residue class can change at every consecutive \(k\).  Consequently no
signed power saving, and in particular no bound of size
\(RX^\varepsilon\), follows from the involution.

# 4. First doubtful or unproved step

There is no doubtful step in the localization estimate or in the
divisor identities above.  The first genuinely unproved step required
for the target would be an analytic estimate for the signed aggregate
in (1.2), after inserting (3.14)--(3.15).  Concretely, one would have to
prove cancellation for at least

\[
 \sum_{|k|\leq K_*}W(k)
 \left(\text{oriented cumulative sum of }
 L_{(N+j)_0/y}((N+j)_0)
 \mathbf1_{(N+j)_0\equiv3\ (4)}\right),
 \tag{4.1}
\]

with all \(2\)-adic valuations allowed.  The complement gives no
inequality for (4.1); it maps its divisor support bijectively back to
the omitted upper support.  On the \(m_0\equiv1\pmod4\) branch, an
additional estimate is needed for the combined full
\(r_2(N+j)/4\) term and the exact central band.  Pointwise narrowness
from (3.12), a factor \(1/2\), or Fourier inversion does not furnish
that estimate.

Invoking a quarter-exponent circle bound, or a short-interval
consequence of it, at this point would be circular and is not done.
The conclusion of this report is therefore deliberately limited: the
tail deletion is target-safe, the branch algebra is complete, and the
proposed complementary-divisor gain self-returns before any signed
\(k\)-saving is obtained.

# 5. Control tests and outcomes

**`exact_Round121_discrepancy`.**  Input: the accepted identity
(122.B1), with the exact floors, \(N=\lfloor X\rfloor\), and
\(W=\widehat J(k)-\widehat J(k+1)\).  Outcome: the proof uses
\(W=\widehat{J(1-e(-t))}\) and never changes the real-\(X\)
normalization.  Implication: (1.2) is a tail deletion from the stated
object, not from a surrogate.

**`uniform_wavelet_envelope`.**  Input: both cutoff scales
\(1/R\) and \(1/y\).  Outcome: (3.2)--(3.4) prove the uniform
three-range envelope (1.1).  The intermediate \(1/|k|\) range is
retained.  Implication: the one-sided lower cutoff has not been hidden
inside a false \(R\)-scale Schwartz bound.

**`far_k_tail_budget`.**  Input: \(|D_N(k)|\leq y\),
\(K_*=\lceil yX^\sigma\rceil\), and \(A\sigma\geq1/4\).  Outcome:
the discarded two-sided tail is \(O_{A,\sigma}(R)\).  Implication: it is
already within (122.B2), without a conjectural estimate.

**`positive_near_square_window`.**  Input: \(0<\sigma<1/2\).
Outcome: \(K_*=o(X)\) and \(N-K_*>0\) for large \(X\); finite smaller
\(X\) are absorbed in the constant.  Implication: \(v_2(N+k)\), the
odd part, and \(r_2(N+k)\) are legitimate throughout the retained
window.

**`two_adic_divisor_involution`.**  Input: every
\(m=2^am_0\), \(a\geq0\).  Outcome: \(a=0\) permits
\(d\leftrightarrow m/d\); every \(a\geq1\) requires
\(d\leftrightarrow m/(2^ad)\), with threshold \(m/(2^ay)\).  The
literal \(m/d\) complement is even and has zero character for
\(a\geq1\).  Implication: there is no missing factor \(2^a\) and no
false character identity on an even complement.

**`character_residue_branches`.**  Input:
\(m_0\equiv1,3\pmod4\).  Outcome: for residue 1, (2.2) gives a
full-coefficient-plus-central-band identity divided by 2; for residue
3, \(F=0\), the central band has signed sum zero, and
\(A_y=L_q\) survives unchanged.  Implication: the latter branch is an
exact self-return and blocks a uniform involutive gain.

**`square_and_central_boundaries`.**  Input: \(q<y\), \(q>y\),
\(q=y\), and \(m_0=\ell^2\).  Outcome: overlap and gap identities use
closed or open intervals exactly as in (2.2); a fixed central divisor
is counted once, and (2.3) handles \(m_0=y^2\).  The hard \(d=y\)
sample is present only when \(y\) is an odd divisor of \(m_0\).  As a
separate size check, any one fixed divisor's contribution to the
original discrepancy is at most \(\sum_k|W(k)|\ll1+\log(y/R)\), so the
hard endpoint itself is target-safe.  Implication: no gain or loss is
being manufactured by an endpoint factor of two.

**`full_divisor_and_complement_one_count`.**  Input: (3.13) and the
classical exact identity (3.8).  Outcome: (3.15) always retains
\(F=r_2/4\) together with the exact complement, and (3.16) confirms the
same at one-count level.  Implication: neither half of the decomposition
is silently discarded.

**`signed_k_aggregation`.**  Input: the localized sum (1.2).
Outcome: (3.14)--(3.15) retain the oriented cumulative sums and the
actual complex/signed wavelet \(W(k)\).  No triangle inequality is
presented as a saving, and no pointwise divisor complement is promoted
to a relation between distinct \(k\)'s.  Implication: the report proves
only a no-go, not an unsigned estimate masquerading as signed
cancellation.

**`circle_problem_noncircularity`.**  Input: the appearance of
\(F=r_2/4\).  Outcome: only the exact sum-of-two-squares identity is
used; no estimate for a short interval of \(r_2\), no quarter-circle
bound, and no consequence of the target is assumed.  Implication: the
remaining full-coefficient term is honestly marked unproved.

**`false_unsigned_control`.**  Input variants: (i) the true
\(\chi_4\) signs, (ii) absolute values on odd divisors, (iii) random
signs of the same magnitude, and (iv) adversarial signs.  Outcome: in
variant (ii) the complement sign is artificially \(+1\) for every odd
part, so one always obtains a factor-2 overlap/gap count; even there it
is only an identity, not a power saving.  In the true variant,
\(m_0\equiv3\pmod4\) changes that factor to \(1+s=0\), making the
equation tautological for \(A_y\).  Random and adversarial signs do not
obey (3.7), so no complementary character formula exists.  Implication:
an unsigned or sign-agnostic proof cannot validate the proposed signed
mechanism.

**`one_count_downstream_scope`.**  Input: the recurrence (3.13) and
the diagnostic inversion (3.16).  Outcome: they are used only to expose
the exact coefficient package already inside (122.B1).  No downstream
circle estimate, unsmoothing statement, or other owner claim is made.
Implication: Fourier inversion is correctly classified as a
restatement, not as the missing bound.

# 6. Dependencies and exact artifacts used

The derivation used only the following permitted artifacts:

1. `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/briefs/blind_near_square_divisor_involution.md`;
2. `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/blind_statement.md`;
3. `problems/gauss_circle.md`;
4. `state/control_models.md`.

No proof-state file, strategy file, Round-64--Round-122 nonblind
artifact, sibling report, candidate file, validation matrix, or
synthesis file was read or edited.  No web source and no numerical
experiment was used.  The only shared-workspace write is this assigned
report.

# 7. Recommended state effect

**Recommended state effect: reject the proposed noninvertible gain.**

Retain (subject to the campaign's independent validation) the uniform
wavelet envelope (1.1), the target-safe localization (1.2), and the
complete two-adic formulas (1.3), (2.2), and (2.3) as useful candidate
lemmas.  But reject any claim that complementary divisors alone give a
signed power saving or the target (122.B2).  The exact
\(m_0\equiv3\pmod4\) branch returns \(A_y=L_q\), while the
\(m_0\equiv1\pmod4\) branch retains the full \(r_2/4\) coefficient and
its central band.  A future round would need a genuinely analytic
signed-\(k\) estimate for those survivors; repeating the involution or
performing Fourier inversion cannot supply it.

# Second-stage seam audit addendum

## Audit 1 of 7. Result

Equations (122.C4)--(122.C15) in the conductor candidate are valid.
The \(|k|\leq R\) window and the high-\(v_2\) cumulative projection are
target-safe, and the identity \(\sum_k kW(k)=0\) has a target-safe
truncation seam.  The conclusion (122.C16) also follows after inserting
the projection identity in Audit 3 below.

The local factor-pair count (122.C27) is valid, including \(n/y=y\),
hard endpoints, and square fixed points.  The first unsupported claim is
the word **entire** in (122.C28), if it means the central correction in
the global all-\(k\) formula (122.C25): (122.C27) counts only
\(|k|\leq K_\delta\).  The \(D_NW\) tail (122.C8) cannot be assigned to
one post-Abel component.  Audit 5 gives an exact independent
\(\widehat J\)-tail repair.  No repaired statement estimates the
remaining medium-index, low-\(v_2\) signed functional.

## Audit 2 of 7. Exact hypotheses and notation

Put

\[
 H(k)=\widehat J(k),\quad W(k)=H(k)-H(k+1),\quad
 K_\delta=\lceil yX^\delta\rceil,\quad
 A_0=\lceil\log_2R\rceil.
\]

For an arithmetic sequence \(f\), define its oriented cumulative sum by

\[
 {\cal I}_Nf(k)=
 \begin{cases}
 \sum_{j=1}^k f(N+j),&k\geq1,\\
 0,&k=0,\\
 -\sum_{j=k+1}^0f(N+j),&k\leq-1.
 \end{cases}
\]

On the positive localized window let

\[
 f_{\rm hi}(m)=A_y(m){\bf1}_{v_2(m)\geq A_0},\qquad
 f_{\rm lo}(m)=A_y(m){\bf1}_{v_2(m)<A_0},
\]

\[
 \widetilde D_{\rm hi}={\cal I}_Nf_{\rm hi},\qquad
 \widetilde D_{\rm lo}={\cal I}_Nf_{\rm lo}.
\]

Then

\[
 \widetilde D_N=D_N+kc_y
 =\widetilde D_{\rm hi}+\widetilde D_{\rm lo}.
 \tag{A.1}
\]

For the central correction, the branch restriction implicit in
(122.C27) should be made explicit:

\[
 {\cal C}(n)=
 {\bf1}_{n>0}{\bf1}_{v_2(n)=0}{\bf1}_{\chi_4(n)=1}
 \begin{cases}
 C_-(n),&n\leq y^2,\\
 -C_+(n),&n>y^2.
 \end{cases}
 \tag{A.2}
\]

The factor \(1/2\) in (122.C21) is restored when \({\cal C}\) is
inserted into (122.C25).

## Audit 3 of 7. Checks of (122.C4)--(122.C15)

For \(G=J(1-e(-t))\), the quotient \((1-e(-t))/t\) is smooth.  The
lower transition has width \(1/y\) and derivative scale \(y\), while
the disjoint upper transition has width \(1/R\) and derivative scale
\(R\).  Therefore

\[
 \|G\|_1\ll R^{-1},\qquad \|G'\|_1\ll1,\qquad
 \|G^{(M)}\|_1\ll_M y^{M-1},
\]

which proves (122.C4)--(122.C5).  Splitting at \(R\) and \(y\), with
\(M>2\) where necessary, gives both bounds in (122.C6).

The fractional-part formula proves \(|D_N(k)|\leq y\).  Hence

\[
 \sum_{|k|>K}|D_N(k)W(k)|\ll_M y^MK^{1-M}.
\]

At \(K=K_\delta\), choosing
\(\delta(M-1)\geq A+1/4\) gives \(O(RX^{-A})\).  Thus
(122.C7)--(122.C9) are valid.

For \(|k|\leq R\), the exact recurrence

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y
\]

and \(|A_y(m)|\leq\tau(m)\ll_\varepsilon X^\varepsilon\),
\(c_y\ll1\), give \(|D_N(k)|\ll_\varepsilon|k|X^\varepsilon\).
Consequently

\[
 \sum_{|k|\leq R}|D_N(k)W(k)|
 \ll_\varepsilon R^{-1}X^\varepsilon
 \sum_{|k|\leq R}|k|
 \ll_\varepsilon RX^\varepsilon.
\]

This verifies (122.C10)--(122.C12).

Fixed-\(X\) smoothness justifies shifting absolutely convergent sums,
and

\[
 \sum_k kW(k)
 =\sum_k kH(k)-\sum_k(k-1)H(k)
 =\sum_kH(k)=J(0)=0.
 \tag{A.3}
\]

Since \(J(0)=0\),

\[
 c_y\sum_{|k|\leq K_\delta}kW(k)
 =-c_y\sum_{|k|>K_\delta}kW(k),
\]

and for \(M>2\),

\[
 \sum_{|k|>K_\delta}|kW(k)|
 \ll_M y^{M-1}K_\delta^{2-M}
 \ll X^{1/2-\delta(M-2)}.
\]

Choosing \(\delta(M-2)\geq A+1/4\) verifies (122.C13)--(122.C13a).
An oriented interval contains at most
\(1+|k|/2^{A_0}\) multiples of \(2^{A_0}\), proving (122.C14).
Using (122.C6), \(2^{A_0}\geq R\), and \(y\leq R^2\) then proves
(122.C15).

The missing overlap seam needed for (122.C16) is

\[
 \sum_{|k|\leq R}\widetilde D_{\rm lo}(k)W(k)
 =
 \sum_{|k|\leq R}D_N(k)W(k)
 +c_y\sum_{|k|\leq R}kW(k)
 -\sum_{|k|\leq R}\widetilde D_{\rm hi}(k)W(k).
 \tag{A.4}
\]

The three right-hand terms are target-safe by (122.C12), the bound
\(\sum_{|k|\leq R}|kW(k)|\ll R\), and the absolute majorant in
(122.C15).  Thus the exact repaired survivor statement is

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}
 \widetilde D_{\rm lo}(k)W(k)
 +O_{\varepsilon,A,\delta}(RX^\varepsilon).
 \tag{A.5}
\]

The valuation condition in (A.5) applies to every cumulative increment
\(N+j\), not just \(N+k\).

## Audit 4 of 7. Checks of (122.C25)--(122.C27), including ties

The global pre-Abel formula is exact:

\[
 \sum_kD_N(k)(H(k)-H(k+1))
 =\sum_k(A_y(N+k)-c_y)H(k)
 =\sum_kA_y(N+k)H(k),
\]

because \(\sum_kH(k)=J(0)=0\).  Also
\(\sup_k|H(k)|\leq\|J\|_1\ll\log(2X)\), so
(122.C25)--(122.C26) are valid.

Let \(n=N+k\) be in the branch in (A.2), and set \(z=n/y\).  A divisor
in \(C_-(n)\) and its complement both lie in \([z,y]\); a divisor in
\(C_+(n)\) and its complement both lie in \((y,z)\).  On
\(|k|\leq K_\delta\),

\[
 |z-y|=\frac{|N+k-y^2|}{y}\ll1+X^\delta.
\]

Each central divisor therefore determines an ordered factor pair in a
box of side \(O(1+X^\delta)\) about \((y,y)\), and the ordered pair
determines \(n\), hence \(k\).  It follows that

\[
 \sum_{|k|\leq K_\delta}|{\cal C}(N+k)|
 \ll(1+X^\delta)^2.
 \tag{A.6}
\]

This proves (122.C27) with the branch indicators made explicit.

The boundary conventions pass:

* At \(z=y\), \(n=y^2\).  On the odd branch \(y\) is odd, and the
  fixed pair \((y,y)\) contributes once to \(C_-(y^2)\).
* For \(n<y^2\) with \(y\mid n\), the endpoint pair \((y,z)\) and its
  reverse lie in the closed overlap, unless they coincide.
* For \(n>y^2\) with \(y\mid n\), those endpoints are correctly absent
  from the open gap \(y<d<z\).
* For any other square \(n=\ell^2\), the fixed pair
  \((\ell,\ell)\) is counted once, not twice.

Multiplying (A.6) by (122.C26) gives the valid localized estimate

\[
 \sum_{|k|\leq K_\delta}|{\cal C}(N+k)H(k)|
 \ll X^{2\delta}\log(2X).
 \tag{A.7}
\]

For \(0<\delta<1/8\), this is target-safe.

## Audit 5 of 7. First invalid line and exact repair of (122.C28)

The proof written in the candidate establishes (A.7), not a global
estimate.  Thus the first invalid inference is (122.C28) read as
bounding the **entire** central correction in (122.C25).  This is a
scope error, not a defect in (122.C27).  One exact repair is to say
“localized central correction” and keep the exterior package unsplit.

To prove the intended global statement instead, use the actual
one-sided kernel.  For every \(M\geq1\),

\[
 \|J^{(M)}\|_1\ll_M y^M,\qquad
 |H(k)|\ll_M y^M(1+|k|)^{-M}.
 \tag{A.8}
\]

Indeed, the lower transition contributes \(O(y^M)\), the integral of
\(t^{-M-1}\) over the interior is \(O(y^M)\), and the upper transition
contributes \(O(R^M)\leq O(y^M)\).  Periodic integration by parts gives
the Fourier bound.

Since \(|{\cal C}(n)|\leq\tau(n)\ll_\rho n^\rho\), splitting at
\(|k|=2N\) gives

\[
 \begin{aligned}
 \sum_{\substack{|k|>K_\delta\\N+k>0}}
 |{\cal C}(N+k)H(k)|
 &\ll_{M,\rho}y^M X^\rho K_\delta^{1-M}\\
 &\ll_{M,\rho}X^{1/2+\rho-\delta(M-1)}.
 \end{aligned}
 \tag{A.9}
\]

For \(k>2N\), use \(N+k\ll k\); its tail is no larger after a harmless
increase of \(\rho\).  There is no positive-\(n\) central branch for
\(k\leq-N\).  Choosing
\(\delta(M-1)\geq A+1/4+\rho\) makes (A.9)
\(O(RX^{-A})\).  Combining it with (A.7) proves

\[
 \sum_{k\in\mathbb Z}|{\cal C}(N+k)H(k)|
 \ll_\delta X^{2\delta}\log(2X)+O_A(RX^{-A})
 \ll_\varepsilon RX^\varepsilon
 \quad(0<\delta<1/8).
 \tag{A.10}
\]

Thus (122.C28) is globally valid only after adding (A.8)--(A.9), or
else after explicitly restricting its conclusion to
\(|k|\leq K_\delta\).

## Audit 6 of 7. Scope, dependencies, and noncircularity

After the two repairs, the far \(D_NW\) tail, central Fourier window,
high-\(v_2\) cumulative projection, and odd positive-character central
correction are target-safe.  The smallest survivor remains (A.5),
further decomposed using the exact odd-part complement.  Neither
(122.C15) nor repaired (122.C28) estimates the surviving full
\(r_2/4\) coefficient.  Therefore no global estimate for
\(\mathcal B_{\rm flat}^{(N)}\), no quarter-circle bound, and no signed
lower bound follows.  The candidate's final scoped no-go for uniform
contraction is accurate.

This audit used only the conductor candidate, the Round-121 synthesis,
and the four statement-only artifacts listed in Section 6 above.  They
supplied every identity needed, so no additional accepted graph node
was opened.  No state, candidate, validation, or synthesis file was
edited.

## Audit 7 of 7. Recommended state effect

**Recommended state effect: revise before promotion.**

Accept (122.C4)--(122.C15), but insert (A.4) before claiming
(122.C16).  Accept the local count (122.C27), with the explicit branch
indicators (A.2).  Do not promote the global wording of (122.C28) from
its current proof: either restrict it to the localized sum or append
the independent tail argument (A.8)--(A.9).  With that repair the
intended global central-correction deletion is valid.

Do not add a global discrepancy estimate.  The authoritative survivor
is the medium-index, low-\(v_2\) signed cumulative wavelet, with the
full \(r_2/4\) and complementary pieces retained together.

# Supersession note on the current (122.C25)--(122.C30)

The current (122.C25)--(122.C28) supersede the pre-Abel version audited
above and are **accepted**.  The present proof works with the localized
oriented cumulative \(E(k)\), so it has no exterior
\(\widehat J\)-tail seam: (122.C27) gives
\(\sup_{|k|\leq K_\delta}|E(k)|\ll(1+X^\delta)^2\), and (122.C6)
immediately gives (122.C28).  The equality case \(n=y^2\) contributes
the pair \((y,y)\) once, and every other square fixed point is likewise
one ordered-pair occurrence.  Thus the earlier objection to the word
“entire” and the repair (A.8)--(A.10) apply only to the superseded
pre-Abel candidate, not to the current cumulative statement.

The piecewise increment (122.C29) is also exact: it removes one half of
\(\Gamma\) on the odd positive-character branch, retains
\(\tfrac12a(n)\) there, retains the self-return \(T_{n/y}(n)\) on the
odd negative-character branch, retains the complete
full-divisor/complement expression for \(1\leq a<A_0\), and sets to
zero precisely the already-controlled \(a\geq A_0\) increments.
Consequently (122.C30) is the correct piecewise survivor and makes no
global estimate for it.

The outcome of the A.4 overlap seam is reflected in (122.C30), but its
proof bookkeeping is not fully displayed in the current Sections 5.1
and 6.  With \(S(k)={\cal I}_k\mathscr V_\delta\), the exact localized
identity is

\[
 S(k)=D_N(k)+kc_y-\widetilde D_{\geq A_0}(k)-\frac12E(k).
 \tag{A.12}
\]

Therefore the deletion of the central Fourier window requires the
explicit seam

\[
 \sum_{|k|\leq R}S(k)W(k)
 =
 \sum_{|k|\leq R}D_N(k)W(k)
 +c_y\sum_{|k|\leq R}kW(k)
 -\sum_{|k|\leq R}\widetilde D_{\geq A_0}(k)W(k)
 -\frac12\sum_{|k|\leq R}E(k)W(k).
 \tag{A.13}
\]

Its four right-hand terms are target-safe respectively by (122.C12),
the central \(|kW(k)|\) bound, (122.C15), and (122.C28).  Thus
(122.C30) is confirmed; for a mechanically complete seam record,
(A.12)--(A.13) should accompany its derivation.  No other repair to the
current (122.C25)--(122.C30) is needed.

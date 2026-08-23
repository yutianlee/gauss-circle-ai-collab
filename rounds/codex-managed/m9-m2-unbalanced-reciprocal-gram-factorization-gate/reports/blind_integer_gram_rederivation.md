# 1. Result: phase integerization succeeds, while the Gram factorization self-returns

Let

\[
 \theta=X-N\in[0,1),\qquad
 \Delta=\frac DL,\qquad
 R=\frac XD,\qquad
 K=\frac{XL}{D^2}=\frac R\Delta.
\]

The literal phase-only integerization is valid in the strong form

\[
 \boxed{\mathscr R_X-\mathscr R_N^\sharp
 \ll_\varepsilon X^\varepsilon.}
 \tag{1.1}
\]

The proof is not the false termwise estimate.  A termwise triangle costs
\(K\).  Instead, coefficientwise Poisson summation places the two rows
at the physical centers

\[
 \frac{r(X-rd)}{4X}
 \quad\hbox{and}\quad
 \frac{r(N-rd)}{4X}
\]

with the same denominator \(4X\) and with all amplitudes still frozen at
\(X\).  Their displacement is \(O(1/D)\).  Smoothness gives a cost
\(1/\Delta\) per near physical incidence, while the incidences are
parameterized by \(u=N-rd\) and have total divisor capacity
\(\Delta X^\varepsilon\).  These two factors cancel, proving (1.1)
uniformly over the full exponent region (123.B1).

For the integerized row, the smallest lawful weighted Cauchy inequality
is

\[
 |\mathscr R_N^\sharp|^2
 \leq
 \left(\sum_{k\asymp K}\frac1k\right)
 \underbrace{\sum_{k\asymp K}\frac{|B_k|^2}{k}}_{\mathfrak G},
 \qquad
 \sum_{k\asymp K}\frac1k\ll1.
 \tag{1.2}
\]

The exact signed Gram is

\[
 \mathfrak G=
 \sum_{\substack{r,s\asymp R\\r,s\ {\rm odd}}}
 \chi_4(r)\chi_4(s)
 W\!\left(\frac X{rD}\right)W\!\left(\frac X{sD}\right)
 \mathcal K_{r,s}.
 \tag{1.3}
\]

Thus

\[
 \boxed{\mathfrak G\ll_\varepsilon X^{1/2+\varepsilon}}
 \tag{1.4}
\]

is sufficient for (123.B5), after renaming \(\varepsilon\).  The
diagonal is the exact nonnegative quantity

\[
 \mathfrak G_{\rm diag}
 =
 \sum_{\substack{r\asymp R\\r\ {\rm odd}}}
 W\!\left(\frac X{rD}\right)^2
 \sum_k\frac{q_L(4Xk/r^2)^2}{k}
 \ll R.
 \tag{1.5}
\]

On a common nonvanishing interior of the literal profiles and once the
sampled \(k\)-interval contains uniformly many integers,
\(\mathfrak G_{\rm diag}\asymp R=X^{1-\delta}\).  No lower bound is
claimed at a sampling edge or when \(K\asymp1\).  Since
\(\delta<1/2\), the generic diagonal capacity exceeds \(X^{1/2}\);
therefore a successful Gram proof must retain and exploit cancellation
from the actual signed off-diagonal.

Smooth summation in \(k\) gives, for

\[
 \alpha_{r,s}=N\left(\frac1r-\frac1s\right),
\]

\[
 |\mathcal K_{r,s}|
 \ll_A(1+K\|\alpha_{r,s}\|)^{-A}.
 \tag{1.6}
\]

The nearest integer \(j\) is unique: a half-integer tie is impossible
because \(r,s\) are odd.  With

\[
 E=N(s-r)-jrs,
\]

(1.6) localizes to

\[
 |E|\lesssim \frac{R^2}{K}X^\eta
 =\frac XL X^\eta
 \tag{1.7}
\]

after a target-safe smooth tail deletion.  The exact identity

\[
 \boxed{(N-jr)(N+js)-N^2=jE}
 \tag{1.8}
\]

holds for every sign of \(j\).

For \(j\ne0\), (1.8) is an invertible change of variables:

\[
 U=N-jr,\qquad V=N+js,\qquad
 r=\frac{N-U}{j},\qquad s=\frac{V-N}{j}.
 \tag{1.9}
\]

It transports, rather than improves, the character:

\[
 \chi_4(r)\chi_4(s)
 =
 \chi_4\!\left(\frac{N-U}{2^{v_2(|j|)}}\right)
 \chi_4\!\left(\frac{V-N}{2^{v_2(|j|)}}\right).
 \tag{1.10}
\]

The odd quotients in (1.10) include the same odd factor of \(j\) twice,
so it cancels.  Thus the factorization reconstructs the original
quarter-shift sign on the two displacements from \(N\); it does not
produce a sign depending only on the product defect \(jE\).

The rigorous outcome is consequently an inverse theorem/no-go.  Up to
a rapidly decaying alias tail, the unresolved object is the complete
signed near-product Gram (1.3) restricted by (1.7), with (1.5) and all
off-diagonal signs retained.  When \(\ell>0\), the off-diagonal
\(j=0\) packet is rapidly decaying; when \(\ell=0\), its bounded
adjacent-denominator band is an additional survivor.  No estimate of
the form (1.4) follows from localization or (1.8) alone.  The proposed
factorization is invertible for \(j\ne0\), and its sole degenerate
branch \(j=0\) either smooths away for \(\ell>0\) or remains at
\(\ell=0\).  This proves a scoped self-return, not (123.B5).

# 2. Exact statement and hypotheses

All parameters and profiles are those in the blind statement.  In
particular,

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,
\]

and no \(X\) in a sampled amplitude is replaced by \(N\).  The phrase
“fixed smooth profile at scale \(L\)” is used in its literal
quantitative sense: after scaling \(h=Lx\), the support is a fixed
compact subset of \((0,\infty)\) and every scaled seminorm is bounded
independently of \(X\).  Consequently, for every \(a,A\geq0\),

\[
 |\mathcal Q_L^{(a)}(y)|
 \ll_{a,A}L^a(1+L|y|)^{-A}.
 \tag{2.1}
\]

This is the only smooth-profile input used below.  It retains profile
edges rather than replacing them by sharp indicators.

The phase-integerization theorem is (1.1), with constants uniform for
fixed admissible \(\delta,\ell\) and the literal profiles.  It includes
all \(d\in\mathbb Z\), the value \(d=0\), support-entry ties, and
\(K\asymp1\).

For the Gram, define

\[
 W_r=W\!\left(\frac X{rD}\right),\qquad
 q_{r,k}=q_L(4Xk/r^2).
\]

Then

\[
 B_k=\sum_{\substack{r\asymp R\\r\ {\rm odd}}}
 \chi_4(r)W_rq_{r,k}e(Nk/r)
\]

and (1.2)--(1.3) are exact.  If the two sampled profiles
\(q_{r,k}\) and \(q_{s,k}\) do not overlap, then
\(\mathcal K_{r,s}=0\); otherwise the literal product of both profiles
is retained.

For every off-diagonal pair, the nearest alias \(j\) is unique and
satisfies

\[
 |j|\ll D,\qquad
 \alpha_{r,s}-j=\frac{E}{rs}.
 \tag{2.2}
\]

For any fixed \(\eta>0\) and \(B>0\), choosing sufficiently many smooth
summations by parts deletes the aggregate range

\[
 |E|>\frac XL X^\eta
 \tag{2.3}
\]

from the complete Gram at cost \(O_{B,\eta}(X^{-B})\).  The retained
tuple set is

\[
 \mathcal P_\eta=
 \left\{(r,s,j,E):
 \begin{array}{l}
 r,s\asymp R\ {\rm odd},\ r\ne s,\\
 q_{r,\cdot}q_{s,\cdot}\not\equiv0,\\
 j\text{ is the unique nearest alias},\\
 E=N(s-r)-jrs,\quad |E|\leq X^{1+\eta}/L
 \end{array}\right\}.
 \tag{2.4}
\]

The smallest signed survivor is explicitly

\[
 \mathfrak G_{\rm surv}
 =
 \mathfrak G_{\rm diag}
 +
 \sum_{(r,s,j,E)\in\mathcal P_\eta}
 \chi_4(r)\chi_4(s)W_rW_s\mathcal K_{r,s},
 \tag{2.5}
\]

with the off-diagonal \(j=0\) tuples removable when \(\ell>0\), but not
when \(\ell=0\).  One has

\[
 \mathfrak G=\mathfrak G_{\rm surv}+O_{B,\eta}(X^{-B}).
 \tag{2.6}
\]

A Gram-route proof of the target therefore requires
\(\mathfrak G_{\rm surv}\ll X^{1/2+\varepsilon}\).  If the
nondegenerate diagonal lower bound
\(\mathfrak G_{\rm diag}\gg R\) applies, this requires the inverse
cancellation condition

\[
 \sum_{(r,s,j,E)\in\mathcal P_\eta}
 \chi_4(r)\chi_4(s)W_rW_s\mathcal K_{r,s}
 =
 -\mathfrak G_{\rm diag}+O_\varepsilon(X^{1/2+\varepsilon}).
 \tag{2.7}
\]

Equation (2.7) is necessary for the proposed Gram route, not asserted
for the original wave without that route.

# 3. Proof or derivation

## 3.1 Phase integerization in the physical kernel

Write \(q_L(h)=q(h/L)\) schematically after fixed-profile scaling.
Differentiating (123.B2) and integrating by parts in \(h\) proves
(2.1).  Coefficientwise Poisson summation is exact after smooth zero
extension.  Indeed, the substitution \(h=4Xx/r^2\) gives

\[
 \begin{aligned}
 &\int_0^\infty
 \frac{q_L(4Xx/r^2)}{x}
 e\!\left(\frac{Xx}{r}-dx\right)\,dx
 =
 \mathcal Q_L\!\left(\frac{r(X-rd)}{4X}\right),\\
 &\int_0^\infty
 \frac{q_L(4Xx/r^2)}{x}
 e\!\left(\frac{Nx}{r}-dx\right)\,dx
 =
 \mathcal Q_L\!\left(\frac{r(N-rd)}{4X}\right).
 \end{aligned}
 \tag{3.1}
\]

Thus all profile entries and edges are included; no hard replacement of
the \(k\)-support is made.  Set

\[
 u=N-rd,\qquad
 y_{r,u}=\frac{ru}{4X},\qquad
 \eta_r=\frac{r(X-N)}{4X}.
\]

Since \(r\asymp R=X/D\),

\[
 L|\eta_r|\ll\frac LD=\frac1\Delta,
 \qquad
 L|y_{r,u}|\asymp\frac{|u|}{\Delta}.
\]

The mean-value theorem and (2.1) give, for every \(A\),

\[
 \left|
 \mathcal Q_L(y_{r,u}+\eta_r)
 -\mathcal Q_L(y_{r,u})
 \right|
 \ll_A
 \frac1\Delta
 \left(1+\frac{|u|}{\Delta}\right)^{-A}.
 \tag{3.2}
\]

For \(u\ne N\), the relation \(u=N-rd\) says that \(r\) is a positive
divisor of \(N-u\), and \(d\) is then unique.  The restrictions that
\(r\) be odd, \(r\asymp R\), and lie in the support of \(W_r\) only
decrease the count.  Hence the contribution of all \(u\ne N\) is

\[
 \ll_A
 \frac1\Delta
 \sum_{u\ne N}
 \tau(|N-u|)
 \left(1+\frac{|u|}{\Delta}\right)^{-A}
 \ll_\varepsilon X^\varepsilon.
 \tag{3.3}
\]

For \(|u|\leq2N\), this follows from the divisor bound and
\(\sum_u(1+|u|/\Delta)^{-A}\ll_A\Delta\); the exterior range follows
by increasing \(A\).  When \(u=N\), one has \(d=0\) for every
\(r\asymp R\).  Its total contribution is

\[
 \ll_A\frac R\Delta
 \left(1+\frac N\Delta\right)^{-A},
 \tag{3.4}
\]

which is rapidly decaying after increasing \(A\).  Equations
(3.1)--(3.4) prove (1.1), including the zero physical index and all
tails.

For comparison, a direct triangle in the frequency formula gives only

\[
 \begin{aligned}
 |\mathscr R_X-\mathscr R_N^\sharp|
 &\ll
 \sum_{r\asymp R}\sum_{k\asymp K}
 \frac{|q_{r,k}|}{k}
 \left|e((X-N)k/r)-1\right|\\
 &\ll
 \sum_{r\asymp R}\sum_{k\asymp K}\frac1r
 \ll K.
 \end{aligned}
 \tag{3.5}
\]

Thus the \(X^\varepsilon\) result comes from physical divisor sparsity,
not from suppressing the number of reciprocal terms.

## 3.2 Weighted Gram normalization and diagonal

Writing

\[
 \frac{B_k}{k}=\frac{B_k}{\sqrt k}\frac1{\sqrt k}
\]

and applying Cauchy proves (1.2).  Expanding the square, using that
\(\chi_4,q_L,W\) are real, gives

\[
 \begin{aligned}
 \mathfrak G
 &=
 \sum_k\frac1k
 \sum_{r,s}
 \chi_4(r)\chi_4(s)W_rW_s
 q_{r,k}q_{s,k}
 e\!\left(Nk\left(\frac1r-\frac1s\right)\right)\\
 &=
 \sum_{r,s}\chi_4(r)\chi_4(s)W_rW_s\mathcal K_{r,s}.
 \end{aligned}
 \tag{3.6}
\]

This is the full signed ordered-pair expansion; no real-part shortcut
or unsigned replacement is used.  Also
\(\mathcal K_{s,r}=\overline{\mathcal K_{r,s}}\), so the two
orientations of an off-diagonal pair combine as an exact real part.

On \(r=s\), the phase is one and \(\chi_4(r)^2=1\), which proves
(1.5).  Fixed support and \(k\asymp K\) give
\(\sum_kq_{r,k}^2/k\ll1\), uniformly even when only \(O(1)\) samples
occur.  A lower bound requires an actual common nonzero profile
interior and is therefore stated separately rather than inferred at
an edge.

## 3.3 Smooth alias localization and factorization

On the overlap of the two literal sampled profiles, the amplitude

\[
 a_{r,s}(k)=\frac{q_{r,k}q_{s,k}}k
\]

has support of length \(O(K)\) and satisfies

\[
 |\Delta_k^m a_{r,s}(k)|\ll_m K^{-m-1}.
\]

Repeated discrete summation by parts yields (1.6).  If \(j\) is the
nearest integer to \(\alpha_{r,s}\), then

\[
 \alpha_{r,s}-j
 =
 \frac{N(s-r)-jrs}{rs}
 =\frac E{rs},
\]

and \(rs\asymp R^2\), giving (1.7).

There is no nearest-integer tie.  Such a tie would imply

\[
 2N(s-r)=(2j+1)rs.
\]

The left side is even, whereas the right side is odd because \(r,s\)
are odd.  This is impossible.  Moreover
\(|\alpha_{r,s}|\ll N/R\ll D\), so \(|j|\ll D\).

The aggregate tail assertion (2.3) follows from (1.6): outside that
range each kernel is \(O_A(X^{-A\eta})\), and there are \(O(R^2)\)
ordered pairs.  Choosing \(A\) after \(B,\eta\) makes the total
\(O_{B,\eta}(X^{-B})\).

Expanding gives

\[
 \begin{aligned}
 (N-jr)(N+js)-N^2
 &=Nj(s-r)-j^2rs\\
 &=j\{N(s-r)-jrs\}
 =jE,
 \end{aligned}
\]

which proves (1.8).  For \(j\ne0\), (1.9) is the exact inverse,
including the congruences

\[
 U\equiv N\pmod j,\qquad V\equiv N\pmod j.
\]

For the nearest aliases and large \(X\),

\[
 U=\frac{Nr}{s}+O(R),\qquad
 V=\frac{Ns}{r}+O(R),
\]

so \(U,V>0\) and \(U,V\asymp N\).  If \(j>0\), the factors straddle
\(N\) as \(U<N<V\), up to the harmless nearest-integer error; if
\(j<0\), the orientation reverses.  In either case

\[
 |UV-N^2|=|jE|
 \ll \frac{DX}{L}X^\eta
 =X\Delta X^\eta.
 \tag{3.7}
\]

The map has not reduced the number or the signed weight of admissible
tuples; it has only expressed them as congruence-restricted near factors
of \(N^2\).

## 3.4 Zero, negative, exact, near, two-adic, and mod-four branches

The stated range \(X\geq2\) gives \(N=\lfloor X\rfloor\geq2\), so the
formal branch \(N=0\) is excluded.

If \(j=0\), then

\[
 E=N(s-r),\qquad
 K|\alpha_{r,s}|
 \asymp L|s-r|.
 \tag{3.8}
\]

The exact collision \(E=0\) is therefore \(r=s\), the diagonal.  For
off-diagonal odd \(r,s\), \(|s-r|\geq2\).  Summing (1.6) over this
branch gives

\[
 \sum_{\substack{r,s\asymp R\\r\ne s,\ j=0}}
 |\mathcal K_{r,s}|
 \ll_A R L^{-A}.
 \tag{3.9}
\]

For every fixed \(\ell>0\), (3.9) is rapidly target-safe after choosing
\(A\).  When \(\ell=0\), it gives only \(O(R)\); bounded
adjacent-denominator zero aliases remain.  The factorization (1.8)
becomes \(0=0\) at \(j=0\) and contains no information about them.

For negative aliases, interchanging \(r,s\) sends

\[
 (j,E)\longmapsto(-j,-E),\qquad
 \mathcal K_{r,s}\longmapsto\overline{\mathcal K_{r,s}}.
\]

The character product is unchanged.  Hence negative aliases provide
the conjugate orientation, not an automatic cancellation.

Now write

\[
 N=2^tN_0,\qquad N_0\ {\rm odd}.
\]

Because \(s-r\) is even and \(rs\) is odd,

\[
 E\equiv j\pmod2.
 \tag{3.10}
\]

Thus \(j\) odd forces \(E\) odd and excludes an exact collision.  If
\(j\ne0\), put

\[
 u=v_2(|j|),\qquad w=t+v_2(s-r).
\]

For even \(j\),

\[
 v_2(E)=
 \begin{cases}
 u,&u<w,\\
 w,&u>w,\\
 \geq u+1\ \text{or }E=0,&u=w.
 \end{cases}
 \tag{3.11}
\]

For \(j=0\), \(v_2(E)=w\) off the diagonal.  The factors
\(U=N-jr\), \(V=N+js\) satisfy the complete valuation split

\[
 v_2(U)=v_2(V)=
 \begin{cases}
 u,&u<t,\\
 t,&u>t,
 \end{cases}
 \qquad
 v_2(U),v_2(V)\geq t+1\quad(u=t).
 \tag{3.12}
\]

This includes \(t=0\): odd \(j\) gives even \(U,V\), while even \(j\)
gives odd \(U,V\).  For \(t\geq1\), odd \(j\) gives odd \(U,V\).

For an exact off-diagonal collision \(E=0\), necessarily

\[
 j\ne0,\qquad
 v_2(j)=t+v_2(s-r)\geq t+1,
 \tag{3.13}
\]

so (3.12) gives \(v_2(U)=v_2(V)=t\) and \(UV=N^2\).
Writing

\[
 g=(r,s),\qquad r=ga,\qquad s=gb,\qquad (a,b)=1,
\]

the exact collision is classified by

\[
 ab\mid N,\qquad N=ab\,n,\qquad
 j=\frac{n(b-a)}g,\qquad g\mid n(b-a).
 \tag{3.14}
\]

Indeed, \((ab,b-a)=1\), so these conditions are necessary and
sufficient together with the original support restrictions.  This is
an exact divisor/factor-pair packet, not a bound for it.  Near
collisions are precisely the nonzero defects in (1.7), with parity and
valuation given by (3.10)--(3.11).

For odd \(r,s\), the actual mod-four sign is

\[
 \chi_4(r)\chi_4(s)
 =(-1)^{(s-r)/2}
 =(-1)^{(jrs+E)/(2N)}.
 \tag{3.15}
\]

The last exponent is an integer because
\(jrs+E=N(s-r)\).  At an exact off-diagonal collision,

\[
 \chi_4(r)\chi_4(s)=
 \begin{cases}
 -1,&v_2(s-r)=1
      \quad\bigl(v_2(j)=t+1\bigr),\\
 +1,&v_2(s-r)\geq2
      \quad\bigl(v_2(j)\geq t+2\bigr).
 \end{cases}
 \tag{3.16}
\]

Thus the exact factor packets split into two possible character-sign
layers; there is no universal negative defect.  For general \(j\ne0\), with
\(j=2^uj_0\), \(j_0\) odd,

\[
 \frac{N-U}{2^u}=j_0r,\qquad
 \frac{V-N}{2^u}=j_0s,
\]

which proves (1.10).  The two occurrences of \(\chi_4(j_0)\) square to
one.  Consequently the mod-four character is exactly the original sign
expressed in the factor coordinates; it is not a new oscillation in
\(UV-N^2\).

## 3.5 The inverse theorem and self-return

Equations (1.6)--(1.9) give a bijection, for every \(j\ne0\), between
the retained reciprocal-alias tuples and near-factor tuples satisfying
the divisibility and congruence conditions in (1.9).  Formula (1.10)
transports the character without loss, while the literal factors
\(W_rW_s q_{r,k}q_{s,k}\) remain functions of the recovered \(r,s\).
Applying the inverse map returns the original kernel (123.B10).

Therefore an absolute near-product count, even if sharp, does not prove
the required signed cancellation.  A Gram proof must establish
(2.7), or at least (1.4), for the full ordered-pair sum.  The
factorization itself supplies neither inequality.  The positive
diagonal cannot be used alone, and the negative aliases merely complete
the conjugate real sum.

This is the smallest rigorous no-go: after the successful phase
integerization and smooth alias deletion, the unsolved object is exactly
(2.5).  For \(\ell>0\) its off-diagonal \(j=0\) part is removable; for
\(\ell=0\) that finite-width zero-alias packet must also remain.  Every
nonzero alias is an invertible near-\(N^2\) reparameterization with the
same character and sampled amplitudes.

# 4. First doubtful or unproved step

There is no doubtful step in the phase-integerization estimate, the
weighted Gram normalization, the alias localization, the
factorization, or the parity classification above.

The first unproved step needed by the proposed Gram route is

\[
 \mathfrak G_{\rm surv}\ll_\varepsilon X^{1/2+\varepsilon}.
 \tag{4.1}
\]

When the literal diagonal is nondegenerate, this entails the signed
off-diagonal cancellation (2.7), of order \(R\), even though the allowed
remainder is only \(X^{1/2+\varepsilon}\).  Neither the product defect
\(|UV-N^2|=|jE|\), the two-adic classification, nor the mod-four
transport identity yields that cancellation.  The exact-collision
classification already has opposite possible sign layers as in (3.16), and the near-collision
layers retain the original quotient-parity sign (3.15).

The numerical-looking inequality
\(178\ell+1638\delta>463\) is not used by any of these exact algebraic
steps and does not by itself imply (4.1).  No conclusion should be
drawn from it without an additional signed near-product theorem.

# 5. Control tests and outcomes

**literal_Round118_flat_wave.**  Input: exactly (123.B3)--(123.B4),
with both fixed sampled profiles and all smooth edges.  Expected
invariant: no sharp, complete-divisor, or other-owner replacement.
Outcome: the proof uses coefficientwise Poisson on the literal
\(q_L(4Xk/r^2)/k\) row and keeps \(W(X/(rD))\).  Implication: (1.1)
belongs only to the flat-smooth UNBAL wave.

**phase_integerization_physical_kernel.**  Input: \(X-N\in[0,1)\)
with all amplitudes and the denominator \(4X\) frozen at \(X\).
Outcome: the centers differ by \(r(X-N)/(4X)\), and
(3.2)--(3.4) prove \(O_\varepsilon(X^\varepsilon)\), including
\(d=0\), negative \(d\), support entries, and \(K\asymp1\).
Implication: (123.B7) is proved uniformly.

**reciprocal_termwise_false_charge.**  Input: the same phase
perturbation in frequency variables.  Expected failure: treating
\(k/r\ll1\) as the total cost.  Outcome: the full triangle is \(O(K)\),
as (3.5) shows.  Implication: only the physical divisor-incidence
argument proves the stronger bound.

**weighted_Gram_normalization.**  Input:
\(\mathscr R_N^\sharp=\sum_kB_k/k\).  Outcome: the correct weights are
\(B_k/\sqrt k\) and \(1/\sqrt k\), giving (1.2) and the exact ordered
Gram (3.6).  Implication: the sufficient Gram scale is
\(X^{1/2+\varepsilon}\), and no factor \(K\) is silently lost.

**diagonal_capacity.**  Input: \(r=s\), with actual \(q_{r,k}\) and
\(W_r\).  Outcome: (1.5) is nonnegative and \(O(R)\), and is
\(\asymp R\) only under the stated nondegenerate sampling condition.
Implication: in the generic interior, a target Gram bound needs
off-diagonal cancellation of the diagonal; a positive diagonal alone
does not prove or refute the original wave bound.

**smooth_alias_localization.**  Input: the literal product
\(q_{r,k}q_{s,k}/k\), including support overlap and edges.  Outcome:
(1.6)--(1.7) give \(|E|\lesssim X^{1+\eta}/L\), with the complement
rapidly target-safe after aggregate summation.  Nearest-integer ties
are impossible by odd parity.  Implication: no sharp alias cutoff or
unpriced edge is introduced.

**alias_product_factorization.**  Input:
\(E=N(s-r)-jrs\).  Outcome: (1.8) is exact, and (1.9) is its inverse
for every \(j\ne0\).  The defect satisfies (3.7).  Implication: the
near-product coordinates are a reparameterization, not a gain.

**two_adic_character_sign.**  Input: \(N=2^tN_0\), all parities of
\(j\), and \(r,s\) odd.  Outcome: (3.10)--(3.16) give the complete
valuation and mod-four split.  Exact aliases have negative sign only
at \(v_2(j)=t+1\) and positive sign at higher layers.  Implication:
there is no uniform alternating defect sign; (1.10) transports the
original character exactly.

**exact_versus_near_collision.**  Input: \(E=0\) and \(0<|E|\) within
(1.7).  Outcome: exact off-diagonal aliases are classified by
(3.13)--(3.14), while near aliases retain the nonzero product defect
\(jE\) and the parity law (3.11).  Implication: exact factor energy
does not control the near packets.

**zero_and_negative_aliases.**  Input: \(N=0\), \(j=0\), and
\(j<0\).  Outcome: \(N=0\) is excluded by \(X\geq2\); \(j=0\) contains
only the diagonal as an exact collision, is rapidly removable
off-diagonal for \(\ell>0\), and survives at finite width for
\(\ell=0\); negative aliases are conjugate orientations with unchanged
character product.  Implication: no branch is silently discarded.

**signed_offdiagonal_aggregation.**  Input: true \(\chi_4(r)\chi_4(s)\)
and the real sampled amplitudes.  Outcome: (2.5) retains the complete
ordered signed Gram.  Absolute values are used only to delete smooth
tails, never to claim the main saving.  Replacing the signs by absolute,
random, or adversarial signs destroys (3.15) and supplies no substitute
bound.  Implication: the remaining theorem must be an actual-sign
estimate.

**owner_and_downstream_scope.**  Input: only the accepted flat-smooth
UNBAL wave.  Outcome: no hard, sharp, starred, clipped, arithmetic, or
transition owner is invoked, and no Gauss-circle estimate is assumed.
Implication: (1.1) does not estimate complete UNBAL, M9-M2, M9, or the
circle discrepancy; (2.5) remains open even for the present owner.

# 6. Dependencies and exact artifacts used

The report used only:

1. rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/briefs/blind_integer_gram_rederivation.md;
2. rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/blind_statement.md;
3. problems/gauss_circle.md;
4. state/control_models.md.

No excluded state, proof draft, strategy file, Round-107--Round-123
nonblind artifact, sibling report, web source, or numerical experiment
was read or used.  No shared state, candidate, validation, or synthesis
file was edited.

# 7. Recommended state effect

**Recommended state effect: revise.**

Promote only after independent validation the phase-integerization lemma
(1.1), the exact weighted Gram normalization (1.2)--(1.5), the smooth
alias localization (1.6)--(1.7), and the complete algebraic and parity
identities (1.8)--(1.10), (3.10)--(3.16).  Revise the proposed
factorization mechanism to record an explicit self-return: for
\(j\ne0\) it is invertible and preserves the character in the form
(1.10), while \(j=0\) is either a smooth tail when \(\ell>0\) or a
separate finite-width survivor when \(\ell=0\).

Do not promote (123.B5).  The smallest unresolved claim is the signed
near-product Gram estimate (4.1), equivalently the cancellation demand
(2.7) when the diagonal is nondegenerate.  Proving an unsigned
near-product count, isolating the positive diagonal, or repeating the
factorization does not close it.

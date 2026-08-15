## 1. Result

The natural exact finite delta resolution at cutoff

\[
 R=\lfloor Q\rfloor,\qquad Q=J/T,
\]

has an exact degeneracy: after the signed \(s\)-sum is evaluated, every
Farey cell except the \(0/1\) cell vanishes identically.  More precisely,
write \(e(z)=e^{2\pi iz}\) and
\(\widehat K(\xi)=\int_{\mathbb R}K(u)e(-u\xi)\,du\).  For one of the
finitely many permitted components of \(K\), suppose

\[
 \operatorname{supp}\widehat K\subset
 \{\xi: \kappa_0\leq |\xi|\leq \kappa_1\}.
\]

If \(T>\kappa _1(R+1)\), then the exact Farey dissection of the delta
constraint \(mn-N-s=0\) gives only

\[
 \mathcal D_{J,T}(X)
 =T\int_{\mathbb R/\mathbb Z}
   \widehat K(T\alpha)e(-X\alpha)
   \sum_{m,n}\chi _4(n)W(m/n)e(\alpha mn)\,d\alpha.                 \tag{1.1}
\]

The integrand in (1.1) is supported inside the \(0/1\) Farey cell.  Thus
no nontrivial delta modulus, Kloosterman sum, or Salié sum is present.
At the benchmark,

\[
 {T\over Q}=X^{1/10}\longrightarrow\infty,
\]

so the stated containment holds for all sufficiently large \(X\).
Poisson summation in \(m,n\) on the remaining cell is exactly the old
two-dimensional Poisson transform, with dual scales \(Q\) and \(4Q\);
it is an identity, not an estimate.  Consequently this finite-delta
mechanism does not prove the required \(J^{1/2}X^\varepsilon\) bound.

For completeness, the rational complete sums that would occur on a
nonzero cell are computed below.  They are ordinary Kloosterman sums for
odd \(q\), and fixed-\(\chi _4\) twisted Kloosterman (Salié-type) sums
for even \(q\).  Their two-dimensional zero frequency is always zero.
These sums do not actually occur at the prescribed cutoff after the
signed wavelet is transformed.

## 2. Exact statement and hypotheses

The conclusion above uses only the following hypotheses.

1. \(N=\lfloor X\rfloor\), \(\vartheta=X-N\), and the only delta
   constraint is \(h=mn-N-s\).
2. The finite \(m,n\)-ranges are the stated ranges \(m,n\asymp J\), the
   factor \(W(m/n)\) is retained, and \(\chi _4\) is extended by zero on
   even integers.  Thus extending the \(n\)-sum to all integers does not
   discard the condition that \(n\) is odd.
3. Componentwise, \(\widehat K\in C_c^\infty(\mathbb R)\) has the support
   displayed in Section 1.  The finite permitted decomposition of the
   actual wavelet is recombined only after the argument.
4. \(R=\lfloor J/T\rfloor\geq2\), and
   \(T>\kappa _1(R+1)\).  No truncation of the infinite \(s\)-sum is
   made.

Let \(\mathfrak F_R\) be the reduced Farey fractions of order \(R\),
viewed cyclically in \(\mathbb R/\mathbb Z\).  If \(a_-/q_-<a/q<a_+/q_+\)
are the two neighbours of \(a/q\), assign to \(a/q\) the interval with
mediant endpoints

\[
 I_{a/q}=\left[
 {a+a_-\over q+q_-},,{a+a_+\over q+q_+}
 \right).
\]

Writing \(\alpha=a/q+\beta\) on this interval gives the exact endpoint
formula

\[
 -{1\over q(q+q_-)}\leq\beta<
 {1\over q(q+q_+)},
 \qquad q+q_\pm>R.                                                  \tag{2.1}
\]

The exact finite delta identity, valid for every integer \(h\), is

\[
 \boxed{
  \mathbf 1_{h=0}
  =\sum_{a/q\in\mathfrak F_R}e_q(ah)
    \int_{I_{a/q}-a/q}e(\beta h)\,d\beta .}
                                                                         \tag{2.2}
\]

This has the literal modulus cutoff \(1\leq q\leq R\).  It follows by
partitioning \(\int_{\mathbb R/\mathbb Z}e(\alpha h)\,d\alpha\), so it
has no congruence aliases.  In particular, (2.2) is not the false
replacement of equality by a mere average of congruences.

The neighbours of \(0/1\) are \(-1/R\) and \(1/R\), and hence

\[
 I_{0/1}=\left[-{1\over R+1},{1\over R+1}\right).                  \tag{2.3}
\]

Equation (2.3), rather than a heuristic major-arc width, is the exact
separation used in the result.

## 3. Proof and derivation

Insert (2.2) with \(h=mn-N-s\), but do not take an absolute value in
\(s\).  For \(\alpha=a/q+\beta\), Poisson summation in \(s\) gives the
exact formula

\[
 \begin{aligned}
 S(\alpha)
 &:=\sum_{s\in\mathbb Z}K\!\left({s-\vartheta\over T}\right)e(-\alpha s)\\
 &=T\sum_{k\in\mathbb Z}
   e\bigl(-\vartheta(k+\alpha)\bigr)
   \widehat K\bigl(T(k+\alpha)\bigr).                              \tag{3.1}
 \end{aligned}
\]

Thus \(S(\alpha)\) can be nonzero only when

\[
 {\kappa _0\over T}\leq \operatorname{dist}(\alpha,\mathbb Z)
 \leq {\kappa _1\over T}.                                         \tag{3.2}
\]

By (2.3) and \(T>\kappa _1(R+1)\), the whole set (3.2) lies strictly
inside \(I_{0/1}\).  Every term of (2.2) with \(a/q\ne0/1\) is therefore
zero after (3.1), before any estimate.  On the surviving cell only
\(k=0\) contributes, and

\[
 e(-\alpha N)S(\alpha)
 =T e\bigl(-\alpha(N+\vartheta)\bigr)\widehat K(T\alpha)
 =T e(-\alpha X)\widehat K(T\alpha).                               \tag{3.3}
\]

This proves (1.1).  Changing variables \(\xi=T\alpha\) in (1.1) gives

\[
 \int \widehat K(\xi)e(-X\xi/T)
       \sum_{m,n}\chi _4(n)W(m/n)e(\xi mn/T)\,d\xi,
\]

which is exactly Fourier inversion of
\(K((mn-X)/T)\).  Hence the delta insertion has returned to the original
sum.

Here is the complete-sum audit before the vanishing is imposed.  It is
included to determine the exact arithmetic type, not to claim an
estimate.  Put

\[
 g=(q,4),\qquad \ell=[q,4]={4q\over g}.
\]

The minimal periods are \(q\) in \(m\) and \(\ell\) in \(n\).  For a
smooth dyadic realization of the archimedean cutoff, two-dimensional
Poisson summation around \(a/q\) contains

\[
 \mathfrak C_{q,a}(r,t)
 =\sum_{x\bmod q}\sum_{y\bmod\ell}
   \chi _4(y)e_q(axy+rx)e_\ell(ty),                                \tag{3.4}
\]

with normalization \((q\ell)^{-1}\), and an integral having phase

\[
 \beta uv-{r u\over q}-{t v\over\ell}.                             \tag{3.5}
\]

Summing \(x\) first is decisive.  If
\(y_0\equiv-\bar a r\pmod q\), then

\[
 \mathfrak C_{q,a}(r,t)
 =q\sum_{\substack{y\bmod\ell\\y\equiv y_0\ (q)}}
       \chi _4(y)e_\ell(ty).                                      \tag{3.6}
\]

Evaluation of the remaining sum gives the following exhaustive cases.

\[
\begin{array}{c|c|c}
q&\text{nonvanishing conditions}&\mathfrak C_{q,a}(r,t)\\ \hline
q\ \mathrm{odd}&t\ \mathrm{odd}&
2iq\,\chi _4(tq)e_q(-\overline{4a}\,rt)\\[2mm]
q\equiv2\pmod4&r,t\ \mathrm{odd}&
2q\,\chi _4(y_0)e_{2q}(t y_0)\\[2mm]
4\mid q&r\ \mathrm{odd}&
q\,\chi _4(y_0)e_q(t y_0).
\end{array}                                                        \tag{3.7}
\]

All omitted cases are zero.  In the middle line the expression is
independent of the choice of lift \(y_0\mapsto y_0+q\): both the
character and the exponential change sign.  For \(q=1\), the first line
is read directly as \(2i\chi _4(t)\) for odd \(t\), with no dependence
on \(r\).  Formula (3.7) also proves

\[
 \mathfrak C_{q,a}(0,0)=0\quad\text{for every }q.                  \tag{3.8}
\]

The axial modes are not all zero: for odd \(q\), \(r=0,t\) odd survives;
for \(4\mid q\), \(t=0,r\) odd survives.  At the actual \(q=1\) cell,
the surviving axial modes are nonstationary because
\(|\beta|\asymp T^{-1}\) and \(J|\beta|=Q\to\infty\).

To classify the sums over numerators, let \(H=N+s\), define

\[
 S(A,B;c)=\sum_{b\bmod c}^{*}e_c(Ab+B\bar b),\qquad
 K_{\chi _4}(A,B;c)=\sum_{b\bmod c}^{*}
 \chi _4(b)e_c(Ab+B\bar b).
\]

Multiplying (3.7) by \(e_q(-aH)\) and summing over reduced \(a\) gives

\[
\begin{array}{c|c}
q&\displaystyle\sum_{a\bmod q}^{*}e_q(-aH)\mathfrak C_{q,a}(r,t)\\ \hline
q\ \mathrm{odd}&
2iq\chi _4(tq)S(-H,-\bar4rt;q)\\[1mm]
q\equiv2\pmod4&
q\chi _4(-r)K_{\chi _4}(-2H,-rt;2q)\\[1mm]
4\mid q&
q\chi _4(-r)K_{\chi _4}(-H,-rt;q),
\end{array}                                                        \tag{3.9}
\]

under the corresponding conditions in (3.7).  The factor \(1/2\) from
lifting reduced residues modulo \(q\) to modulo \(2q\) is already
included in the middle line.  Thus odd moduli produce ordinary
Kloosterman sums; even moduli produce \(\chi _4\)-twisted Kloosterman,
or Salié-type, sums.  There is no odd-modulus Salié sum.  For odd
\(q\), the exact gcd entering a square-root estimate would be

\[
 (H,rt,q),                                                         \tag{3.10}
\]

since \(4\) is invertible modulo \(q\).  For the even lines the relevant
modulus is respectively \(2q\) or \(q\), and any claimed estimate must
retain the conductor-\(4\) local factor and the exact gcd of its two
arguments with that modulus.  No such estimate is used here.

The dual-length audit follows directly from (2.1) and (3.5):

\[
 |r|\lesssim qJ|\beta|+q/J,
 \qquad
 |t|\lesssim \ell J|\beta|+\ell/J.                                \tag{3.11}
\]

On a generic Farey cell, (2.1) gives lengths at most \(T\) and
\((4/g)T\), up to fixed support constants.  On the only surviving cell,
\(q=1,\ell=4\) and \(\beta=\xi/T\), so the stationary scales sharpen to

\[
 r\asymp Q,\qquad t\asymp4Q.                                      \tag{3.12}
\]

The stationary equations and their product are

\[
 {r\over q}=\beta v,qquad {t\over\ell}=\beta u,qquad
 rt=q\ell\,\beta^2uv.                                             \tag{3.13}
\]

For the zero cell, \(uv\asymp X\), \(\beta=\xi/T\), and hence
\(rt\asymp4\xi^2Q^2\).  This is a real, continuously weighted product
alias.  It is not an assertion that \(rt\), \(r\), or \(t\) is a square
or a fourth power.  At the exact rational centre \(\beta=0\), the only
stationary pair is \((0,0)\), and (3.8) kills it.  Thus neither the
modulus \(4\) nor \(\chi _4\) creates an unrecorded square/fourth-power
condition.

Finally, the complete power ledger is

\[
 T={J\over Q},\qquad
 \mathcal D_{J,T}(X)\ll {J\over Q}X^\varepsilon\quad\text{(absolute
 product grouping)},                                              \tag{3.14}
\]

whereas the target is \(J^{1/2}X^\varepsilon\).  The missing gain is

\[
 {J/Q\over J^{1/2}}={J^{1/2}\over Q}.                             \tag{3.15}
\]

At \(J=X^{1/2},Q=X^{1/5},T=X^{3/10}\), (3.14) is \(X^{3/10}\), the
target is \(X^{1/4}\), and (3.15) is \(X^{1/20}\).  Since the surviving
delta modulus is \(q=1\), there is no \(q^{1/2}\) complete-sum saving to
supply (3.15).  The normalized Gauss coefficient at \(q=1\) has constant
size: \(|\tau(\chi _4)|/4=1/2\).

## 4. First doubtful or unproved step

There is no doubtful algebraic step before the self-return (1.1).  The
first genuinely unproved step needed for the target is a cancellation
estimate for the \(q=1\) dual product aliases.  With a smooth
archimedean amplitude \(A(u,v)\) retaining \(W(u/v)\), the exact returned
form is

\[
 {T\over4}\sum_{r,t\in\mathbb Z}\tau_4(t)
 \int \widehat K(T\alpha)e(-X\alpha)
 \iint A(u,v)e\!\left(\alpha uv-ru-{t v\over4}\right)
 \,du\,dv\,d\alpha,                                               \tag{4.1}
\]

where \(\tau_4(t)=2i\chi _4(t)\) for odd \(t\) and is zero for even
\(t\).  Proving that (4.1) is
\(O(J^{1/2}X^\varepsilon)\) is exactly the missing dual-correlation
inequality; (3.12)--(3.13) show its natural support.  Calling (4.1)
"Poisson cancellation" does not prove it, and counting it as a new
delta estimate would count the forbidden two-dimensional return.

If one instead enlarges the circle cutoff until nonzero Farey cells meet
the band (3.2), the first source-dependent complete-sum input would be a
uniform estimate of the shape

\[
 |S(A,B;c)|\ll \tau(c)c^{1/2}(A,B,c)^{1/2},
\quad
 |K_{\chi _4}(A,B;c)|\ll
 \tau(c)c^{1/2}(A,B,c)^{1/2},                                     \tag{4.2}
\]

with the exact local factors at \(2\) and at primes shared by
\(A,B,c\).  The second inequality in (4.2), in precisely the imprimitive
modulus configurations of (3.9), has not been source-audited in this
statement-only report and is not asserted as a theorem.  Moreover, the
signed transform selects only arcs satisfying
\(a/q+\beta\asymp T^{-1}\), so a complete numerator sum cannot be
assumed without first proving that its archimedean weights are uniform.

## 5. Controls

- **Real centre and sign:** (3.1) retains \(\vartheta\), and (3.3)
  combines it with \(N\) to give exactly \(X=N+\vartheta\).  Outcome:
  pass.
- **Exact delta and cutoff:** (2.2) is an exact partition of the circle,
  with literal cutoff \(q\leq R\); (2.1)--(2.3) give all endpoint
  widths.  Outcome: pass.
- **Signed \(s\)-sum:** no absolute value or truncation precedes (3.1).
  Its transform is explicit and compactly supported.  Outcome: pass.
- **Character, parity, and ratio:** \(\chi _4(n)\), its zero values on
  even \(n\), and \(W(m/n)\) remain in every identity.  Outcome: pass.
- **Complete-sum modulus and zero modes:** the minimal modulus pair is
  \((q,[q,4])\); (3.6)--(3.9) include all three values of \((q,4)\), and
  (3.8) records the zero-zero mode.  As spot checks, (3.7) gives
  \(\mathfrak C_{1,0}(0,1)=2i\),
  \(\mathfrak C_{2,1}(1,1)=4i\), and
  \(\mathfrak C_{4,1}(1,0)=-4\), each also obtained directly from
  (3.4).  Outcome: pass.
- **Gcd and normalization:** (3.9)--(3.10) display the exact ordinary
  gcd and identify where conductor-\(4\) local factors would be needed;
  the Poisson normalization is \((q[q,4])^{-1}\).  No unverified Weil
  factor is silently used.  Outcome: pass.
- **Dual lengths and aliases:** (3.11)--(3.13) derive the lengths and the
  exact dual product relation.  No square or fourth power is inferred
  from a real stationary equation.  Outcome: pass.
- **Power target:** (3.14)--(3.15) reproduce the missing \(X^{1/20}\).
  Outcome: pass.
- **Source theorems:** Kuznetsov, Weil/Salié, divisor-short-interval,
  and delta-method source theorems were not opened because the blind
  brief forbids sources.  Therefore no source-dependent theorem is used
  or certified here.  Outcome: deliberately not admissible in this
  isolated task; a later nonblind seam review would be required before
  using (4.2).
- **Numerical allocation:** no numerical experiment was used; the work
  is entirely algebraic/analytic.

## 6. Dependencies and exact artifacts

The derivation depends only on the accepted formula (70.2), the benchmark
relations \(J=X^{1/2}\), \(T=J/Q\), \(Q=X^{1/5}\), and the stated Fourier
support property of the permitted components of \(K\).

**Isolation ledger.**  The only artifacts opened were:

1. `rounds/codex-managed/m9-m1-near-product-delta-salie/briefs/blind_delta_method_rederivation.md`;
2. `rounds/codex-managed/m9-m1-near-product-delta-salie/derivation_packet.md`.

No graph, prior report, sibling brief, source, shared synthesis, shared
state file, or numerical artifact was opened.  This report is the only
file written.

## 7. Recommended state effect

**Reject** the prescribed \(q\leq Q=J/T\) finite-delta/Salié mechanism
as a source of the missing \(X^{1/20}\): after the mandatory signed
\(s\)-transform it has no nontrivial modulus at all.  **Retain** the exact
zero-cell collapse and the complete-sum formulas (3.7)--(3.9) as
candidate no-go evidence, subject to conductor/source seam review if the
even-modulus estimates are ever used.  Make no bound, full-cone,
M9--M1, M9, exponent, graph, or proof-draft promotion.

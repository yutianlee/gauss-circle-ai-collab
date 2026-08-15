# Round 70 discovery report: delta/Salié transform attack

Campaign: `m9-m1-near-product-delta-salie`  
Task: `delta_salie_transform_attack`  
Role: discovery analyst

## 1. Result

The finite circle decomposition can be carried out exactly, but it does
not furnish the missing estimate.  Summing the actual \(s\)-wavelet
*before* absolute values confines the circle variable to an endpoint arc
of width \(T^{-1}\).  Consequently:

* any Farey cutoff \(R\) with \(R=o(T)\), in particular the benchmark
  cutoff \(R=Q=X^{1/5}<T=X^{3/10}\), sees only the \(0/1\) (equivalently
  \(1/1\)) cell and is the exact Fourier self-return;
* the first nonendpoint rational cells require \(c\gg T\), and their
  reduced numerator has length \(b\asymp c/T\); at the first admissible
  moduli \(c\asymp T\), there are only \(O(1)\) numerators;
* two-variable residue completion produces an ordinary Kloosterman sum
  for odd \(c\), and a \(\chi_4\)-twisted Kloosterman/Salié sum for even
  \(c\), only if the numerator is completed.  The actual wavelet leaves
  the inverse phase in a short numerator sum, so the complete Weil bound
  is not directly available.

Thus the proposed elementary delta/Salié route is a rigorous no-go at
the point where it invokes complete-sum cancellation.  The sharp first
missing input is a weighted spectral/large-sieve estimate for the short
numerator, dual-frequency, and modulus family displayed in (70.12)
below.  The target

\[
 \mathcal D_{J,T}(X)\ll J^{1/2}X^\varepsilon
\]

remains open; no actual-symbol counterexample was found.

## 2. Exact statement and hypotheses

Use \(e(z)=e^{2\pi i z}\) and

\[
 \widehat f(\xi)=\int_{\mathbb R}f(u)e(-u\xi)\,du.
\]

Let \(J=X^{1/2}\), \(T=J/Q\), \(N=\lfloor X\rfloor\), and
\(\vartheta=X-N\).  The \(m,n\asymp J\) notation is represented by a
fixed smooth compactly supported weight \(V(m,n)\), including the actual
one-sided ratio symbol \(W(m/n)\).  The \(n\)-variable is odd and carries
the primitive character \(\chi_4\).  Write \(K=\widehat g\), where \(g\) is
fixed, smooth, and compactly supported away from zero.  It is enough to
treat one connected component

\[
 \operatorname{supp}g\subset[A,B]\subset(0,\infty),
 \qquad 0<A<B<\infty,
\]

because the other components are identical endpoint arcs.  Then

\[
 \mathcal D_{J,T}(X)=
 \sum_{m,n}\chi_4(n)V(m,n)
 K\!\left(\frac{mn-X}{T}\right).                         \tag{70.3}
\]

For an arbitrary integer \(R\ge2\), take any finite partition of unity
of the circle subordinate to the Dirichlet/Farey cover by reduced
fractions \(a/c\), \(1\le c\le R\).  This is an exact finite circle
decomposition; no delta-symbol asymptotic is used.  For residue
completion put \(L=[4,c]\), and define

\[
 C_{c,a}(h,k)=
 \sum_{x\bmod c}\sum_{y\bmod L}
 \chi_4(y)e_c\bigl(x(ay+h)\bigr)e_L(ky),                 \tag{70.4}
\]

where \((a,c)=1\).  The claim proved below is the following scoped
transformation/no-go statement.

> After exact \(s\)-Poisson summation, only
> \(\|a/c\|\asymp T^{-1}\) occurs.  For \(R<T/(2B)\) only the endpoint
> Farey cell occurs.  In every nonendpoint cell the small endpoint
> numerator \(b=\min(a,c-a)\) satisfies \(c\gg T\) and
> \(b=O(c/T+1)\).  The complete residue sums are exactly (70.8)--(70.10),
> but the actual \(b\)-range is incomplete.  Hence termwise Weil/Salié
> cancellation does not prove (70.3) at the required scale.

This statement is fixed-smooth-interior only and says nothing about cone
edges, transition saddles, or the full \(M9\)-\(M1\) sum.

## 3. Proof or derivation

Start from the permitted offset constraint and insert only the exact
circle identity

\[
 \mathbf 1_{mn-N-s=0}=\int_0^1e\bigl(\alpha(mn-N-s)\bigr)\,d\alpha.
\]

Poisson summation in \(s\) gives, absolutely,

\[
 \sum_{s\in\mathbb Z}K\!\left(\frac{s-\vartheta}{T}\right)e(-\alpha s)
 =T\sum_{\ell\in\mathbb Z}
 e\bigl(-\vartheta(\ell+\alpha)\bigr)
 \widehat K\bigl(T(\ell+\alpha)\bigr)                    \tag{70.5}
\]

and \(\widehat K(u)=g(-u)\).  On the selected positive component only
\(\ell=-1\) occurs, with

\[
 1-\frac BT\le\alpha\le1-\frac AT.
\]

Putting \(t=T(1-\alpha)\) in the circle integral gives exactly

\[
 \mathcal D_{J,T}(X)=
 \int_A^B g(t)
 \sum_{m,n}\chi_4(n)V(m,n)
 e\!\left(-\frac{t(mn-X)}T\right)dt,                    \tag{70.6}
\]

which is the defining Fourier representation of \(K\).  This proves the
self-return and retains the real shift \(\vartheta\) exactly.

The smallest positive reduced fraction with denominator at most \(R\)
is \(1/R\).  Thus, if \(2BR<T\), the support in (70.5) lies wholly in
the endpoint Voronoi/Farey cell; there is no nonzero rational numerator
to complete.  More generally a nonendpoint cell meeting (70.5) has
endpoint distance \(b/c=O(T^{-1})\), up to its fixed partition overlap,
and hence \(c\gg T\), \(b=O(c/T+1)\).  This conclusion is independent of
the choice of exact subordinate partition.

For completeness, the residue algebra is computed for every parity of
\(c\).  If

\[
 f_\beta(x,y)=V(x,y)e(\beta xy),\qquad
 \alpha=a/c+\beta,
\]

then two-dimensional Poisson summation in the residue classes gives

\[
 \sum_{m,n}\chi_4(n)e_c(amn)f_\beta(m,n)
 =\frac1{cL}\sum_{h,k\in\mathbb Z}
 C_{c,a}(h,k)
 \widehat f_\beta\!\left(\frac hc,\frac kL\right).       \tag{70.7}
\]

Summing \(x\) first imposes \(y\equiv-\bar a h\pmod c\).  The remaining
one, two, or four lifts give the following exact formulas.

If \(c\) is odd, put \(\lambda_c=(c^2-1)/4\), so that
\(\lambda_c\equiv-\overline4\pmod c\).  Then

\[
 C_{c,a}(h,k)=
 \begin{cases}
 2ic\,\chi_4(kc)
 e_c(\lambda_c kh\bar a),&k\ \mathrm{odd},\\
 0,&k\ \mathrm{even}.
 \end{cases}                                             \tag{70.8}
\]

Thus a *complete* \(a\)-sum, if it were present, would be

\[
 2ic\,\chi_4(kc)
 S(-M,\lambda_c kh;c),\qquad
 S(u,v;c)=\sum_{a\bmod c}^{*}e_c(ua+v\bar a),            \tag{70.9}
\]

with \(M=N+s\) in the offset form and \(M=N\) after (70.5).
It is an ordinary Kloosterman sum, not a Salié sum.

If \(c\equiv2\pmod4\), let \(\widetilde t\) be either lift modulo \(2c\)
of \(-\bar a h\pmod c\).  Then

\[
 C_{c,a}(h,k)=
 \begin{cases}
 2c\,\chi_4(\widetilde t)e_{2c}(k\widetilde t),
     &h,k\ \mathrm{odd},\\
 0,&\mathrm{otherwise}.
 \end{cases}                                             \tag{70.10}
\]

The displayed product is independent of the chosen lift.  On lifting
\(a\) from modulus \(c\) to modulus \(2c\), the complete numerator sum is
a \(\chi_4\)-twisted Kloosterman/Salié sum modulo \(2c\), with phase
\(e_{2c}(-2Ma-kh\bar a)\).

If \(4\mid c\), then

\[
 C_{c,a}(h,k)=
 \begin{cases}
 c\,\chi_4(-h)\chi_4(a)e_c(-kh\bar a),&h\ \mathrm{odd},\\
 0,&h\ \mathrm{even},
 \end{cases}                                             \tag{70.11}
\]

and completion in \(a\) is directly the \(\chi_4\)-twisted Kloosterman/Salié
sum modulo \(c\).  These formulas account for all gcd and zero-mode
locations before estimation.  In the odd case a generic complete sum
has the familiar square-root scale
\(c^{1/2+\varepsilon}(M,kh,c)^{1/2}\); because
\((\lambda_c,c)=1\), there is no hidden extra gcd.  Analogous
conductor-and-gcd factors occur in the two twisted cases.

The decisive point is that (70.5) replaces the complete numerator sum
by

\[
 \boxed{\quad
 \sum_{T\ll c\le R}\frac1c
 \sum_{\substack{b=O(c/T+1)\\ (b,c)=1}}
 \sum_{h,k}
 \chi_4(\mathrm{dual\ variable})
 e_c\!\left(\pm bN+\mu_c hk\bar b\right)
 \mathcal I_{c,b}(h,k),
 \quad}                                                   \tag{70.12}
\]

with the parity modifications (70.8)--(70.11).  Here
\(\mathcal I_{c,b}(h,k)\) is the exact Farey-\(\beta\) integral of the factor
in (70.5) and of \(\widehat f_\beta(h/c,k/L)\); no coefficient has been
discarded.  For a standard Dirichlet cell
\(|\beta|\ll(cR)^{-1}\), integration by parts confines the dual indices
to

\[
 |h|,|k|\ll \frac JR+\frac cJ
\]

up to the factor \(4\) in the \(k\)-coordinate.  At the first arithmetic
scale \(R\asymp c\asymp T\), this is \(O(Q+1)\), whereas the numerator
length is \(c/T\asymp1\).  There is therefore no complete \(a\)-sum on
which to spend a Weil saving.  Completing the short interval gives at
best

\[
 \min\!\left(\frac cT+1,
 c^{1/2+\varepsilon}(N,hk,c)^{1/2}\right),
\]

and the first term is the sharper one at \(c\asymp T\).

The power ledger is consequently

\[
 T=\frac JQ=X^{3/10},\qquad J^{1/2}=X^{1/4},\qquad
 \frac{T}{J^{1/2}}=\frac{J^{1/2}}Q=X^{1/20}.             \tag{70.13}
\]

At \(R=Q<T\) the transform is (70.6); at \(R\asymp T\) it is the
short-numerator family (70.12).  Absolute values in either description
recover only \(TX^\varepsilon\).  Saving the factor in (70.13) requires
a new joint estimate across \(c,h,k\); it does not follow from any one
complete Kloosterman or Salié bound.

## 4. First doubtful or unproved step

The first unproved inequality is a spectral or arithmetic large-sieve
bound for the exact weighted family (70.12), strong enough to save
\(T/J^{1/2}=X^{1/20}\) over its absolute capacity.  In particular, one
would need cancellation across the moduli and the \(O(Q^2)\) dual
frequency pairs at \(c\asymp T\), because the numerator sum itself has
only \(O(1)\) terms there.  No argument in this report proves that joint
estimate.

The standard phrase "apply Weil to the resulting Kloosterman sum" is
therefore the first invalid step: it silently replaces the actual
condition \(b=O(c/T+1)\) by a complete reduced residue system and also
suppresses the \(b\)-dependent Farey integral
\(\mathcal I_{c,b}(h,k)\).  The report does not rule out a genuinely
spectral treatment of (70.12); it rules out the proposed termwise
complete-sum closure.

## 5. Required control test and outcome

1. **Offset and real centre.**  Equation (70.5) retains \(\vartheta\), and the
   change of variables gives \(e(-t(mn-X)/T)\), not a rounded-centre
   phase.  Outcome: pass.
2. **Delta identity and cutoff.**  The circle integral and finite Farey
   partition are exact for every \(R\).  For \(2BR<T\), only the endpoint
   cell intersects the wavelet Fourier support.  Outcome: pass and
   self-return.
3. **Complete sums and character.**  Direct lift counting gives
   (70.8)--(70.11).  Odd moduli yield ordinary Kloosterman sums; even
   moduli yield \(\chi_4\)-twisted/Salié sums.  Outcome: pass.
4. **Zero modes.**  For odd \(c\), every even \(k\), including \(k=0\),
   vanishes; \(h=0\) survives and a completed sum degenerates to the
   Ramanujan sum \(c_c(M)\).  For \(c\equiv2\pmod4\), both \(h\) and \(k\)
   must be odd.  For \(4\mid c\), \(h=0\) vanishes but \(k=0\) may
   survive as a twisted character sum.  Outcome: pass; no omitted zero
   mode supplies the target saving.
5. **Gcds.**  In (70.9), \((\lambda_c,c)=1\), so the complete bound has
   gcd factor \((M,kh,c)^{1/2}\).  The even-modulus formulas retain their
   induced-character conductor explicitly.  Outcome: pass.
6. **Dual lengths.**  The stationary equations are
   \(h/c=\beta y+O(J^{-1})\) and
   \(k/L=\beta x+O(J^{-1})\).  Hence the \(R\asymp T\) dual range is
   \(O(Q+1)\) per coordinate.  Rational aliases satisfy the corresponding
   product relation \(hk\asymp cL\beta^2X\); they are not deleted.
   Outcome: pass.
7. **Exact and perfect-power products.**  If \(\vartheta=0\), the exact product
   contributes \(K(0)\) times an actual truncated divisor coefficient,
   hence \(O(X^\varepsilon)\).  There are \(O(1)\) square products in a
   length-\(T<J\) window near \(X\), each with divisor-bounded actual
   multiplicity; fourth powers are sparser.  Outcome: no counterexample.
8. **Power and scope.**  Absolute capacity is \(TX^\varepsilon\), the
   target is \(J^{1/2}X^\varepsilon\), and the unresolved factor is
   \(X^{1/20}\).  No cone edge or global exponent is inferred.  Outcome:
   pass.

## 6. Dependencies and exact artifacts used

The derivation used only the following authorized artifacts:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `rounds/codex-managed/m9-m1-near-product-delta-salie/briefs/delta_salie_transform_attack.md`;
* `rounds/codex-managed/m9-m1-near-product-delta-salie/derivation_packet.md`;
* `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/synthesis.md`;
* `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/reviews/conductor_direct_bilinear_adjudication.md`;
* `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`.

No external theorem is imported.  The only analytic tools used are exact
circle orthogonality, one- and two-dimensional Poisson summation for
fixed smooth compact support, CRT, and direct finite Gauss-sum algebra.
The square-root estimate for a hypothetically completed sum is used only
as an upper-limit control; the no-go conclusion already follows from
the actual numerator length.  No numerical evidence was used.

## 7. Recommended state effect

**Promote, scoped:** the exact finite circle/Farey transformation,
the endpoint-support lemma, and the complete residue formulas
(70.8)--(70.11).  Record that the natural \(R=Q<T\) circle dissection is
an exact \(0/1\)-cell self-return.

**Reject:** the claim that summing the signed \(s\)-wavelet exposes a
complete Kloosterman or Salié sum to which a termwise Weil bound closes
the target.  The wavelet instead enforces the short numerator
\(b=O(c/T+1)\), with only \(O(1)\) terms at \(c\asymp T\).

**Retain open:** the joint weighted estimate (70.12), the bound
\(\mathcal D_{J,T}(X)\ll J^{1/2}X^\varepsilon\), the global angular-radial
estimate, \(M9\)-\(M1\), \(M9\), and the Gauss-circle exponent.

## 1. Result

**Hostile no-go for a ready-made delta/Salié/Kuznetsov closure.** The
Heath--Brown delta symbol can be inserted exactly, and its complete
two-variable residue sums can be evaluated exactly. They become ordinary
Kloosterman sums for odd moduli, level-four twisted Kloosterman sums for
moduli divisible by \(4\), and a cusp-to-cusp hybrid for
\(c\equiv2\pmod4\), but only if the numerator is complete.

For the actual wavelet, Poisson summation in the offset \(s\) first forces

\[
 \left\|\frac ac\right\|\asymp T^{-1},\qquad
 T\ll c\ll J,\qquad
 A_c:=\#\{a\}\asymp c/T\leq J/T=Q.                 \tag{H70.1}
\]

At \(J=X^{1/2}\), \(T=X^{3/10}\), \(Q=X^{1/5}\), one has
\(A_c\leq\sqrt c\) throughout this range. Thus the actual numerator sum is
short and incomplete; completing it and applying Weil gives no improvement
over its trivial length. Standard Kuznetsov applies to modulus averages of
complete Kloosterman sums, not this moving short-numerator family. None of
the audited primary sources supplies a lossless workaround.

The double zero-frequency residue vanishes, but single-zero modes survive.
For odd \(c\), the mode \(\rho=0\), \(\sigma\) odd degenerates, after
counterfactual completion, to a Ramanujan sum with an indispensable
\((c,N+s)\) factor. No actual-symbol counterexample to
\[
 \mathcal D_{J,T}(X)\ll J^{1/2}X^\varepsilon       \tag{H70.2}
\]
was found. The result is a theorem-hypothesis no-go and a narrower arithmetic
interface, not a disproof of (H70.2).

## 2. Exact statement and hypotheses

Put \(N=\lfloor X\rfloor\), \(\theta=X-N\), and absorb the fixed dyadic
cutoffs and \(W(m/n)\) into a fixed smooth \(\Omega(m/J,n/J)\), supported
in the assigned one-sided central ratio sector. Then
\[
 \mathcal D_{J,T}(X)=
 \sum_{m,n\in\mathbb Z}\chi_4(n)\Omega(m/J,n/J)
 K\!\left(\frac{mn-X}{T}\right).                  \tag{H70.3}
\]
Use \(e_c(z)=e(z/c)\) and
\(\widehat f(\xi)=\int f(t)e(-\xi t)\,dt\). After the permitted finite
fixed Mellin decomposition, \(\widehat K\) is smooth, compactly supported,
and supported a fixed positive distance from zero. All symbol seminorms are
independent of \(X,J,T\).

The exact Heath--Brown identity with conductor \(\mathcal C\) is
\[
 \delta(r)=c_{\mathcal C}\mathcal C^{-2}
 \sum_{c=1}^{\infty}\sum_{a\bmod c}^{*}
 e_c(ar)h\!\left(\frac c{\mathcal C},
                  \frac r{\mathcal C^2}\right),
 \quad c_{\mathcal C}=1+O_A(\mathcal C^{-A}).      \tag{H70.4}
\]
Take \(\mathcal C=J\). Since the delta argument can have size \(J^2\),
the resulting modulus range is bounded by
\(\max(\mathcal C,J^2/\mathcal C)\), minimized at \(J\). A single
congruence indicator is not an admissible substitute for (H70.4), because
it also counts aliases \(mn-N-s=\ell c\).

Let \(L=[c,4]\) and define the exact complete residue
\[
 \mathfrak C_{c,a}(\rho,\sigma)=
 \sum_{u\bmod c}\sum_{v\bmod L}
 \chi_4(v)e_c(auv+\rho u)e_L(\sigma v),            \tag{H70.5}
\]
where \((a,c)=1\). No coprimality is assumed for \(\rho,\sigma\).

## 3. Proof or derivation

After inserting (H70.4), the offset factor for fixed \(c,a,x,y\) is
\[
 \Sigma_{c,a}(x,y)=
 \sum_s K\!\left(\frac{s-\theta}{T}\right)e_c(-as)
 h\!\left(\frac cJ,\frac{xy-N-s}{J^2}\right).      \tag{H70.6}
\]
Poisson summation in \(s\) gives exactly
\[
 \Sigma_{c,a}(x,y)=
 \sum_{\ell\in\mathbb Z}\int_{\mathbb R}
 K\!\left(\frac{t-\theta}{T}\right)
 h\!\left(\frac cJ,\frac{xy-N-t}{J^2}\right)
 e\!\left(-\left(\ell+\frac ac\right)t\right)dt.   \tag{H70.7}
\]
The \(h\)-factor varies on the \(J^2\)-scale, while \(K\) varies on the
\(T\)-scale. The derivative bounds for \(h\), integration by parts, and the
support of \(\widehat K\) show rapid decay unless
\[
 T\left|\ell+\frac ac\right|\asymp1.
\]
For \(0<a<c\), this proves (H70.1): one gets a short interval near \(0\)
or \(1\), and necessarily \(c\gg T\). The translation is retained:
\(e_c(-aN)\) and \(\theta\) combine into \(e(-aX/c)\).

To evaluate (H70.5), sum over \(u\). This imposes
\(av+\rho\equiv0\pmod c\). If
\(v_0\equiv-\bar a\rho\pmod c\), then
\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =c\sum_{0\leq t<L/c}\chi_4(v_0+ct)e_L(\sigma(v_0+ct)).
\]
The remaining Gauss sum gives the following exhaustive table.

For \(c\) odd, with \(\lambda_c=(c^2-1)/4\),
\[
 \mathfrak C_{c,a}(\rho,\sigma)=
 \begin{cases}
 2ic\,\chi_4(c\sigma)e_c(\lambda_c\rho\sigma\bar a),
   &\sigma\ \mathrm{odd},\\
 0,&\sigma\ \mathrm{even}.
 \end{cases}                                      \tag{H70.8}
\]
Here \(\lambda_c\equiv-\bar4\pmod c\).

For \(c\equiv2\pmod4\), so \(L=2c\),
\[
 \mathfrak C_{c,a}(\rho,\sigma)=
 \begin{cases}
 2c\,\chi_4(v_0)e_{2c}(\sigma v_0),
   &\rho,\sigma\ \mathrm{odd},\\
 0,&\text{otherwise}.
 \end{cases}                                      \tag{H70.9}
\]
Changing \(v_0\) by \(c\) changes both displayed factors by \(-1\), so
the formula is well-defined.

For \(4\mid c\), so \(L=c\),
\[
 \mathfrak C_{c,a}(\rho,\sigma)=
 \begin{cases}
 -c\,\chi_4(a)\chi_4(\rho)e_c(-\bar a\rho\sigma),
   &\rho\ \mathrm{odd},\\
 0,&\rho\ \mathrm{even}.
 \end{cases}                                      \tag{H70.10}
\]

If \(a\) were complete and \(R=N+s\), (H70.8) would yield
\[
 2ic\chi_4(c\sigma)S(-R,\lambda_c\rho\sigma;c),
 \quad
 S(u,v;c)=\sum_{a\bmod c}^{*}e_c(ua+v\bar a),      \tag{H70.11}
\]
and (H70.10) would yield
\[
 -c\chi_4(\rho)S_{\chi_4}(-R,-\rho\sigma;c),
 \quad
 S_{\chi_4}(u,v;c)=
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(ua+v\bar a).      \tag{H70.12}
\]
Equation (H70.9) is the analogous level-four cusp-to-cusp sum of modulus
\(2c\). It is not automatically a classical prime-modulus Salié sum.
Crucially, (H70.7) retains only \(\min(a,c-a)\asymp c/T\), so
(H70.11)--(H70.12) classify a counterfactual completion, not the transformed
wavelet itself.

For complete sums, the lawful bounds are
\[
 |S(u,v;c)|\leq\tau(c)(u,v,c)^{1/2}c^{1/2},\qquad
 |S_{\chi_4}(u,v;c)|
 \ll\tau(c)(u,v,c)^{1/2}c^{1/2}.                  \tag{H70.13}
\]
The second estimate has only a fixed extra factor because the inducing
conductor is \(4\). The gcd factor is essential. For odd \(c\), \(\rho=0\),
and \(\sigma\) odd,
\[
 S(-R,0;c)=c_c(R)=\sum_{d\mid(c,R)}d\mu(c/d),
 \quad |c_c(R)|\leq(c,R),                         \tag{H70.14}
\]
and this equals \(\varphi(c)\) when \(c\mid R\). Thus
\(\mathfrak C(0,0)=0\) in every modulus class, but the odd-\(c\)
\(\rho=0,\sigma\) odd mode and the \(4\mid c\)
\(\sigma=0,\rho\) odd twisted Gauss mode survive.

The complete conductor ledger is
\[
 T\ll c\ll J,\qquad A_c\asymp c/T\leq Q,\qquad
 A_c\leq\sqrt c\quad\text{at the benchmark}.       \tag{H70.15}
\]
The raw odd-\(c\) residue numerator has size
\(cA_c=c^2/T\). Completion plus Weil gives \(c^{3/2}\), which is not
smaller because \(A_c\leq\sqrt c\); gcd-degenerate modes can be larger.
Fourier completion of the short \(a\)-weight produces about
\(c/A_c\asymp T\) moving first arguments. Standard Kuznetsov does not
absorb those arguments losslessly. The power deficit remains
\[
 TX^\varepsilon=X^{3/10+\varepsilon}
 \quad\text{versus}\quad
 J^{1/2}X^\varepsilon=X^{1/4+\varepsilon},
 \quad \frac{T}{J^{1/2}}=\frac{J^{1/2}}Q=X^{1/20}. \tag{H70.16}
\]

## 4. First doubtful or unproved step

The first unproved step is a joint short-Farey-numerator estimate, on each
dyadic \(C\in[T,J]\), of the schematic form
\[
 \sum_{c\asymp C}
 \sum_{\substack{a\asymp c/T\\(a,c)=1}}
 \alpha_{c,a;\rho,\sigma}
 e_c(-aN+\lambda_c\rho\sigma\bar a),               \tag{H70.17}
\]
with square-root cancellation in the joint \((c,a)\) set. Here
\(\alpha\) must be the actual smooth integral from (H70.6), including
\(\theta,W,K,h\) and the finite natural dual aliases. The even-modulus
versions must use (H70.9)--(H70.10). Arbitrary coefficients are not allowed.

Pointwise Weil completion cannot prove (H70.17), because its square-root
threshold is at least the entire numerator length. Conventional Kuznetsov
cannot be invoked before completion, and afterward its first argument ranges
through \(\asymp T\) values depending on \(c\). A spectral large-sieve
theorem for this exact two-parameter family would be genuinely new work.
The Ramanujan degeneration (H70.14) must be separated.

No original-coefficient resonance disproves (H70.2). Exact products have
divisor mass \(X^\varepsilon\). Since \(T<J\), the interval
\([X-O(T),X+O(T)]\) contains only \(O(1)\) squares and \(O(1)\) fourth
powers, each with divisor-bounded mass. Rational dual aliases and
\(c\mid N+s\) obstruct termwise Weil estimates, but they do not give a
lower bound for the fully recombined original sum.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Offset coefficient | Pass: (H70.6) retains \(\chi_4(n),W,K,\theta\); no replacement by \(d\) or \(r_2/4\). |
| Delta identity | Pass: (H70.4) is exact; a lone congruence is rejected. |
| Modulus cutoff | Pass: \(\mathcal C=J\), \(T\ll c\ll J\). |
| Farey/wavelet seam | Pass: \(\|a/c\|\asymp1/T\), so \(A_c\asymp c/T\) before absolute values. |
| Complete sums | Pass: (H70.8)--(H70.10) cover odd, \(2\bmod4\), and \(0\bmod4\) moduli. |
| Zero modes | Pass with obstruction: the double zero vanishes; two single-zero families survive. |
| Gcds | Pass: (H70.13)--(H70.14) retain the gcd, and \(c\mid N+s\) can attain \(\varphi(c)\). |
| Dual lengths | Pass: the delta weight has radial width \(\asymp cJ\), hence width \(\asymp c\) in either product variable; a fixed \(X^\varepsilon\)-family of natural aliases, including the single-zero modes, survives. |
| Weil capacity | Fail as closure: \(A_c\leq\sqrt c\), so completion is non-improving. |
| Kuznetsov applicability | Fail: the actual numerator is incomplete and completion creates \(\asymp T\) moving arguments. |
| Perfect powers | Pass: the \(T<J\) window contains only \(O(1)\) square/fourth-power products, each divisor-safe. |
| Downstream scope | Pass: no cone-edge, GAR, M9--M1, M9, or exponent claim is made. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The repository artifacts used were only protocol.md,
state/proof_obligations.yml, state/active_campaign.yml, the assigned
Round-70 brief and derivation_packet.md, and the permitted Round-69
direct_bilinear_source_hostile_audit.md and
conductor_direct_bilinear_adjudication.md. No sibling Round-70 report was
read.

The primary-source audit is:

* **Exact delta method.** Theorem 1 of
  [Heath--Brown, *A New Form of the Circle Method, and its Application to
  Quadratic Forms*, J. reine angew. Math. 481 (1996), 149--206](https://ora.ox.ac.uk/objects/uuid%3Abbd3c62f-f010-44b5-8be5-87e903fb0084)
  is (H70.4), with \(h(x,y)\ll x^{-1}\), support
  \(x\leq\max(1,2|y|)\), and Lemmas 4--5 providing the derivatives used in
  (H70.7). It does not assert that an added wavelet leaves \(a\) complete.

* **Complete twisted bounds.** Theorem 9.2 of
  [Knightly--Li, *Kuznetsov's Trace Formula and the Hecke Eigenvalues of
  Maass Forms*, Mem. AMS 224 (2013)](https://arxiv.org/abs/1202.0189)
  gives the complete twisted Weil bound with gcd and character-conductor
  factors. It implies (H70.13) for fixed conductor \(4\), but sums every
  unit modulo \(c\), unlike \(a\asymp c/T\).

* **Kuznetsov.** The original
  [Kuznetsov formula, Math. USSR-Sb. 39 (1981), 299--342](https://www.mathnet.ru/eng/sm2598)
  averages complete Kloosterman sums over their moduli. Theorem 4 of
  [Blomer--Milićević, *Kloosterman sums in residue classes*, JEMS 17
  (2015), 51--69](https://ems.press/journals/jems/articles/12028)
  still has a smooth \(c\)-sum of complete \(S(m,n;c)\); its extra
  arithmetic weight is on the modulus, not the numerator. Neither matches
  (H70.17).

* **Incomplete Kloosterman sums.** Browning--Haynes record the completion
  bound \(2(1+\log p)p^{1/2}\) for one fixed prime-modulus interval and
  identify the length-square-root bound \(H^{1/2}p^\varepsilon\) as
  Hooley's conjecture; their Theorem 2 is a mean value over disjoint
  intervals:
  [*Incomplete Kloosterman sums and multiplicative inverses in short
  intervals*](https://arxiv.org/abs/1204.6374).
  Theorem 1 of
  [Korolev, *Short Kloosterman sums to powerful modulus*](https://arxiv.org/abs/1604.02300)
  applies only to powerful moduli, assumes
  \(A_c\geq\max(\operatorname{rad}(c)^{15},
  \exp(C(\log c)^{2/3}))\), and gives only a subpower relative saving.
  Neither result is uniform over the present delta moduli.

* **Short divisor intervals.** Theorem 1 of
  [Ivić--Zhai, *On the Dirichlet divisor problem in short intervals*](https://arxiv.org/html/1209.0872v1)
  treats the complete \(d(r)\) coefficient and gives
  \(x^{1/4+\varepsilon}U^{1/4}\) or
  \(x^{2/9+\varepsilon}U^{1/3}\). At \(U=T=X^{3/10}\), these are
  \(X^{13/40+\varepsilon}\) and \(X^{29/90+\varepsilon}\), both above
  \(X^{1/4+\varepsilon}\), besides having the wrong coefficient. Their
  equation (2.5) labels the pointwise square-root short-interval bound as
  Jutila's conjecture.

Every imported result was checked at its summation variable, completeness,
modulus, coefficient, averaging, gcd, and conductor hypotheses. None supplies
the missing estimate.

## 7. Recommended state effect

**Retain (H70.2) as open.** Promote at most the exact fixed-interior
delta/Farey seam (H70.4)--(H70.10) and the source no-go: the actual
\(s\)-wavelet restricts the delta numerator to
\(\|a/c\|\asymp1/T\), so complete Kloosterman, Salié, Weil, and Kuznetsov
theorems cannot be imported directly. Record the double-zero cancellation and
the surviving single-zero/gcd degenerations separately.

The smallest new objective is the joint \((c,a)\) estimate (H70.17), with
the actual integral weight and the even-modulus residue table retained.
Recommended rejected claims are: “the delta method automatically creates a
complete Salié sum after the \(s\)-wavelet”; “Weil saves on the short
numerator at the benchmark”; “standard Kuznetsov accepts the moving
short-numerator family”; and “\(\chi_4\) kills every zero mode.” No
full-cone, GAR, M9--M1, M9, or exponent promotion is licensed.

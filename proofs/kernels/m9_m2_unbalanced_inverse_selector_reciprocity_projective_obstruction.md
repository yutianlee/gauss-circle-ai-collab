# M9--M2 unbalanced inverse-selector reciprocity and scalar projective obstruction

- Campaign: m9-m2-unbalanced-inverse-selector-reciprocity-gate
- Round: 160
- Task: conductor_round160_accepted_kernel
- Role: conductor-selected proof kernel
- Generated at: 2026-08-25T18:58:47+08:00
- Starting graph SHA-256:
  4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d
- Terminal label: inverse_selector_projective_capacity_no_go
- Allocation: 100% analytic, algebraic, and primary-source verification;
  0% numerical experimentation

## 1. Exact scoped result

Put

\[
 X=N_0+\xi,\qquad 0\le \xi<1,\qquad
 D=X^\delta,\qquad L=X^\ell,
\]

\[
 R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac RK=\frac DL,\qquad a=\delta-\ell,
\tag{160.K1}
\]

under

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{160.K2}
\]

For odd \(g,n\), \(gn\asymp R\), and the literal zero-extended moving
support \(j\in\mathcal J_{g,n}\), \((j,n)=1\), define

\[
 b_{g,n}(j)=
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
\tag{160.K3}
\]

and

\[
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 b_{g,n}(j)e(-h\overline j_n/n).
\tag{160.K4}
\]

The exact reciprocity identity

\[
 \boxed{
 e(-h\overline j_n/n)
 =e(h\overline n_j/j-h/(jn))}
\tag{160.K5}
\]

holds for every coprime \(j,n\), every integer \(h\), arbitrary inverse
representatives, and both parities of \(j\). It gives the literal centered
quadruple summand

\[
 \boxed{
 \frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\overline n_j}{j}
                 -\frac{h}{jn}\right)S(N_0,h;n)}
\tag{160.K6}
\]

for every \(1\le h<n\). All moving support entries and exits, profiles,
real-centre factors, gcd strata, and both character directions remain.

Additive reciprocity does not create a low-projective-cost scalar common
test. For every \(j>1\), every subset
\(A\subseteq U_j=(\mathbb Z/j\mathbb Z)^\times\), and \(M=|A|\), define

\[
 F_{j,A}(u,h)=e(h\overline u_j/j),
 \qquad u\in A,\qquad 1\le h\le j-1.
\tag{160.K7}
\]

Then

\[
 \boxed{F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*,}
\tag{160.K8}
\]

so

\[
 \operatorname{sing}(F_{j,A})
 =\{\sqrt j\ (M-1\text{ times}),\sqrt{j-M}\},
\tag{160.K9}
\]

\[
 \|F_{j,A}\|_{S_1}=(M-1)\sqrt j+\sqrt{j-M},
 \qquad
 \|F_{j,A}\|_{S_2}^2=M(j-1).
\tag{160.K10}
\]

Consequently every exact Hilbert rank-one factorization followed
termwise by a triangle inequality pays

\[
 \sum_\nu\|u_\nu\|_2\|v_\nu\|_2
 \ge \|F_{j,A}\|_{S_1},
\tag{160.K11}
\]

and, for \(A=U_j\),

\[
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \asymp\sqrt{\varphi(j)}=j^{1/2-o(1)}.
\tag{160.K12}
\]

The literal positive range contains the full block \(1\le h\le j\) for
all sufficiently large \(X\). If

\[
 \mathcal F_j(u,h)=j^{-1/2}e(h\overline u_j/j),
 \qquad u\in U_j,\quad 1\le h\le j,
\tag{160.K13}
\]

then

\[
 \mathcal F_j\mathcal F_j^*=I_{\varphi(j)},\qquad
 \|\mathcal F_j\|_{S_1}=\varphi(j),\qquad
 \|\mathcal F_j\|_{S_2}=\sqrt{\varphi(j)}.
\tag{160.K14}
\]

Thus the positive frequencies \(h=j,2j,\ldots\), which are zero modulo
\(j\), are not the deleted frequency \(h=0\pmod n\).

At the primitive stratum \(g=1\), \(j\asymp K\), and the scalar
projective inflation has size

\[
 K^{1/2-o(1)}
 =X^{(1-\delta-a)/2-o(1)}.
\tag{160.K15}
\]

This exceeds the entire missing boundary power at every fixed strict
point of the frozen region. Therefore the exact reciprocity kernel cannot
be inserted into the audited scalar fixed-test routes with only an
\(X^\varepsilon\) projective charge. This is the precise meaning of the
terminal no-go.

The result is deliberately narrower than a theorem about the owner. It
does not lower-bound the signed scalar, does not transfer the unweighted
matrix lower bound to the literal weighted matrix, does not exclude a
scalar theorem with an additional compensating saving, and does not
exclude a bespoke vector-valued theorem acting on the complete weighted
\((j,n,h)\) array before positive norms.

## 2. Reciprocity, representatives, parity, and reconstruction

Choose arbitrary integers \(u=\overline j_n\) and
\(v=\overline n_j\). The integer

\[
 ju+nv-1
\]

is divisible by both \(j\) and \(n\), hence by \(jn\). Therefore

\[
 \frac{u}{n}+\frac{v}{j}\equiv\frac1{jn}\pmod1,
\tag{160.K16}
\]

which proves (160.K5). Replacing \(u\) by \(u+tn\), or \(v\) by
\(v+sj\), changes the exponent by an integer. No division by \(2\)
occurs, so even \(j\) is included.

Use the ordinary Kloosterman convention

\[
 S(N_0,h;n)=\sum_{x\bmod n}^{*}
 e\!\left(\frac{N_0\overline x_n+hx}{n}\right).
\tag{160.K17}
\]

The accepted switched-cusp identity is

\[
 S_{\infty0}^{\chi_4}(4N_0,h;2n)
 =\chi_4(n)S(N_0,h;n)
\tag{160.K18}
\]

for odd \(n\), every \(h\), and arbitrary \((N_0,n)\). Substitution of
(160.K3)--(160.K5) and (160.K18) gives (160.K6).

For complete \(h\bmod n\), additive orthogonality gives

\[
\begin{aligned}
 &\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)\\
 &\quad=\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}b_{g,n}(j)
 \sum_{x\bmod n}^{*}e(N_0\overline x_n/n)
 \sum_{h\bmod n}e(h(x-\overline j_n)/n)\\
 &\quad=
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 b_{g,n}(j)e(N_0j/n).
\end{aligned}
\tag{160.K19}
\]

The factor \(e(\xi j/n)\) already contained in \(b_{g,n}(j)\) restores
\(e(Xj/n)\). Thus complete frequency summation returns the original
reciprocal row exactly.

At \(h=0\),

\[
 \widehat\gamma_{g,n}(0)=\frac1n\sum_j b_{g,n}(j),
 \qquad
 S(N_0,0;n)=c_n(N_0).
\tag{160.K20}
\]

Hence the frozen \(1\le h<n\) scalar is complete inversion minus this one
already accepted target-safe Ramanujan row. It is removed exactly once.

## 3. Exact residue and projective algebra

For \(u,v\in A\),

\[
\begin{aligned}
 (F_{j,A}F_{j,A}^*)_{u,v}
 &=\sum_{h=1}^{j-1}
 e(h(\overline u_j-\overline v_j)/j)\\
 &=\begin{cases}
 j-1,&u=v,\\
 -1,&u\ne v.
 \end{cases}
\end{aligned}
\tag{160.K21}
\]

This proves (160.K8). The all-ones direction has eigenvalue \(j-M>0\);
its orthogonal complement has eigenvalue \(j\). Equations
(160.K9)--(160.K10) follow.

The nuclear norm is the infimum of
\(\sum_\nu\|u_\nu\|_2\|v_\nu\|_2\) over exact Hilbert rank-one
factorizations, proving (160.K11). For \(M=\varphi(j)\), the elementary
divisor bound gives

\[
 \frac{j}{\varphi(j)}
 =\prod_{p\mid j}(1-1/p)^{-1}
 \le\prod_{p\mid j}2
 =2^{\omega(j)}
 \le d(j)\ll_\varepsilon j^\varepsilon.
\tag{160.K21a}
\]

Consequently

\[
 \varphi(j)\gg_\varepsilon j^{1-\varepsilon}
\tag{160.K22}
\]

gives (160.K12). Adding the column \(h=j\) changes (160.K21) to
\(jI_{\varphi(j)}\), proving (160.K13)--(160.K14).

The exact additive common-test expansion is

\[
 \boxed{
 \mathbf1_{(n,j)=1}e(h\overline n_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j),}
\tag{160.K23}
\]

where

\[
 S(h,-t;j)=\sum_{x\bmod j}^{*}
 e((h\overline x_j-tx)/j).
\tag{160.K24}
\]

Indeed, expanding the right side and summing in \(t\) forces
\(x\equiv n\pmod j\); it also gives zero when \((n,j)>1\).
Multiplicative characters, residue indicators, and (160.K23) are changes
of basis for the same full-rank finite kernel, not low-rank replacements.

## 4. Long-frequency and bandwidth controls

Writing \(h=qj+s\), \(0\le s<j\), gives

\[
 e(h\overline n_j/j-h/(jn))
 =e(s\overline n_j/j)e(-q/n-s/(jn)).
\tag{160.K25}
\]

Thus reciprocity makes only the inverse part periodic in \(h\bmod j\);
it does not shorten the physical range \(1\le h<n\).

For

\[
 (P_{n,j}A)(s)=
 \sum_{\substack{1\le h<n\\h\equiv s\ (j)}}A(h),
\tag{160.K26}
\]

the rows have disjoint supports. Hence

\[
 \boxed{
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\max_s\#\{1\le h<n:h\equiv s\pmod j\}}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}.}
\tag{160.K27}
\]

This norm is attained. Since \(n/j\asymp\Delta\), the exact long-block
scale is \(\asymp\sqrt\Delta\). Moreover, for

\[
 1\le m\le\left\lfloor\frac{n-1}{j}\right\rfloor,\qquad h=mj,
\]

\[
 e(h\overline n_j/j)=1,\qquad
 e(-h/(jn))=e(-m/n)=1+O(1/j).
\tag{160.K28}
\]

The short reciprocal phase supplies no cancellation on these
\(\asymp\Delta\) positive frequencies. Equations (160.K27)--(160.K28)
are operator-capacity controls, not lower bounds for the
\(S(N_0,h;n)\)-weighted signed vector.

There is also an exact additive-bandwidth diagnostic. If

\[
 c_j(t)=\sum_{x\bmod j}^{*}e(tx/j),
\]

then

\[
 \sum_{h=1}^{j-1}|S(h,-t;j)|^2
 =j\varphi(j)-|c_j(t)|^2,
\qquad
 \sum_{t\bmod j}|c_j(t)|^2=j\varphi(j).
\tag{160.K29}
\]

For centered representatives and

\[
 \mathcal H_j=\{t\bmod j:j/4\le|t|\le j/2\},
\]

equation (160.K29) gives, for \(j\ge12\),

\[
 \sum_{t\in\mathcal H_j}\sum_{h=1}^{j-1}
 \left|\frac{S(h,-t;j)}j\right|^2
 \ge\frac14\varphi(j).
\tag{160.K30}
\]

The total joint mass is

\[
 \sum_{t\bmod j}\sum_{h=1}^{j-1}
 \left|\frac{S(h,-t;j)}j\right|^2
 =\frac{j-1}{j}\varphi(j).
\tag{160.K31}
\]

Thus a fixed proportion lies at \(|t|\asymp j\). On an
\(n\asymp R/g\) cell, the test \(e(tn/j)\) has logarithmic frequency
\(\asymp R/g\). This is an exact phase-only bandwidth diagnostic. Its
translation into any particular automorphic Sobolev or Bessel norm
requires that theorem's printed hypotheses and is not promoted here.

## 5. Boundary-power comparison

The missing saving exponent is

\[
 \mu(a)=
 \begin{cases}
 a-\frac14,&\frac14<a\le\frac13,\\[1mm]
 \frac{1-2a}{4},&\frac13\le a<\frac12.
 \end{cases}
\tag{160.K32}
\]

At \(g=1\),

\[
 K=X^{1+\ell-2\delta}=X^{1-\delta-a}.
\tag{160.K33}
\]

For \(a\le1/3\),

\[
 \frac{1-\delta-a}{2}-\left(a-\frac14\right)
 =\frac{3-2\delta-6a}{4}>0,
\tag{160.K34}
\]

because \(\delta<1/2\) and \(a\le1/3\). For \(a\ge1/3\),

\[
 \frac{1-\delta-a}{2}-\frac{1-2a}{4}
 =\frac{1-2\delta}{4}>0.
\tag{160.K35}
\]

At \(a=1/3\), both branches agree and the margin is
\((1-2\delta)/4\). Therefore the \(K^{1/2-o(1)}\) scalarization
inflation exceeds \(X^{\mu(a)}\) at each fixed strict exponent pair.
There is no margin uniform up to the open face \(\delta=1/2\).

The long-block scale also exceeds the missing factor:

\[
 \frac a2-\mu(a)
 =\begin{cases}
 \frac14-\frac a2,&a\le1/3,\\[1mm]
 \frac{4a-1}{4},&a\ge1/3,
 \end{cases}
 \quad >0.
\tag{160.K36}
\]

These comparisons show that omitting either finite-kernel scalarization
or long-block capacity omits at least the full saving being sought. They
do not say that a deeper signed theorem cannot offset those capacities.

## 6. Audited scalar-source seam

The primary-source audit gives the following route-scoped conclusions.

1. Bettin--Chandee Theorem 1 and Wright Theorem 2.1 accept independent
   scalar coefficient sequences for a Kloosterman-fraction phase. They do
   not accept the simultaneous moving joint coefficient
   \(S(N_0,h;n)\) occurring in (160.K6). Opening that Kloosterman sum and
   completing \(h\) gives the exact self-return (160.K19).
2. Blomer--Milićević Theorem 1 can encode a fixed arithmetic modulus
   weight, but for \(j=p\) prime and \(p\nmid h\), the normalized Mellin
   coefficients of \(u\mapsto e(h\overline u_p/p)\) satisfy
   \[
    \|\widehat f_h\|_1
    =(p-2)\sqrt{\frac p{p-1}}+\frac1{\sqrt{p-1}}
    \asymp p.
    \tag{160.K37}
   \]
   This is not a low-cost scalar test.
3. Legal Mellin encoding has arithmetic period
   \(q_j=\operatorname{lcm}(4,j)\). For \(j=p\) odd prime, the principal
   \(p\)-character is odd and gives levels \(4,8,4p,8p\).
   Nonprincipal \(p\)-characters give levels
   \(4p,8p,4p^2,8p^2\); for \(p\ge5\), both parities occur across this
   conductor-\(4p\) family. The complete compatible holomorphic, Maaß,
   exceptional, Eisenstein, newform, and oldclass ledgers remain at every
   induced level.
4. The sourced scalar Linnik range is
   \[
    h\ll H_{\mathrm{Lin}}(g)
    \asymp\frac{K}{Lg^2},
    \qquad
    \frac{H_{\mathrm{Lin}}(g)}{R/g}\asymp\frac1{Dg}.
    \tag{160.K38}
   \]
   It covers only a vanishing portion of the literal \(1\le h<n\)
   range, and (160.K19) prevents deleting the complement by formal
   Fourier reasoning.
5. Deshouillers--Iwaniec and Assing--Blomer--Li use fixed scalar
   coefficient/smoothness interfaces. The \(h\)-dependent arithmetic
   weight, moving support, growing levels, and high additive bandwidth in
   (160.K6) do not satisfy those interfaces at a free cost.
   Assing--Blomer--Li also has no \(\chi_4(c)\) modulus twist; on odd
   moduli \(\chi_4(c)=e((c-1)/4)\), so scalar encoding itself has
   normalized frequency \(\asymp R/g\).

These facts certify only the failure of the audited canonical scalar
realizations. They do not certify the impossibility of a new
coefficient-sensitive vector theorem.

## 7. First open step, controls, and state boundary

The first unproved positive step is a signed vector-valued estimate for
the literal centered matrix that keeps

\[
 \chi_4(g)\chi_4(n),\quad
 e(h\overline n_j/j),\quad e(-h/(jn)),\quad
 S(N_0,h;n),\quad q_L(4Xj/(gn^2))
\tag{160.K39}
\]

jointly before every positive norm, covers all \(1\le h<n\), every gcd
and two-adic stratum, the moving support and endpoints, and every required
spectral level, while gaining \(X^{\mu(a)}\). No such theorem is proved
or sourced in Round 160.

The campaign hypotheses also contain no pointwise lower-profile statement
that produces a complete unit-class block on which the literal joint
weight is bounded above and below. Therefore the exact unweighted
Schatten lower bound is not promoted as a lower bound for the literal
weighted coefficient matrix. Any buffered weighted robustness lemma is
conditional evidence only.

The required controls close as follows:

| Control | Outcome |
|---|---|
| Reciprocity sign, representatives, and parity | GREEN by (160.K16). |
| Literal scalar and character placement | GREEN by (160.K6) and (160.K18). |
| Complete \(h\)-self-return | GREEN by (160.K19). |
| Single \(h=0\) deletion | GREEN by (160.K20); positive \(h=mj\) remain. |
| Residue rank and projective price | GREEN by (160.K8)--(160.K14), for the unweighted exact kernel. |
| Additive common-test expansion | GREEN by (160.K23); high bandwidth is diagnostic only. |
| Long-\(h\) complement | GREEN as an operator control by (160.K27)--(160.K28). |
| Primitive \(g=1\) and boundary power | GREEN pointwise in the strict region by (160.K34)--(160.K36). |
| Moving weighted lower bound | OPEN; no lower-buffer hypothesis is supplied. |
| Scalar source theorem match | NO MATCH at owner-saving cost for the audited routes. |
| Bespoke vector theorem | OPEN and not obstructed by this kernel. |
| Owner and downstream scope | QUARANTINED; no target, strict range, M2, M9, bridge, or exponent follows. |

The promotable state effect is one route-scoped obstruction for exact
unweighted Hilbert scalarization plus triangle and the audited scalar
source realizations. The flat smooth strict-UNBAL estimate, complete
M9--M2, M9, endpoint uniformity, the conditional bridge, and the quarter
target remain open. The internally proved global exponent \(1/3\) and the
separately audited external exponent are unchanged.

## 8. Dependencies and evidence

Accepted graph dependencies:

- M9-M2-unbalanced-truncated-divisor-fixed-centre-return;
- M9-M2-unbalanced-flat-wave-curvature-envelope;
- M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction;
- M9-M2-unbalanced-level-four-spectral-matrix-obstruction;
- M9-M2-character-factor; and
- Divisor-bound-elementary.

Round-160 evidence:

- the discovery report inverse_selector_reciprocity_attack.md;
- the statement-only blind report blind_reciprocity_matrix_rederivation.md;
- the source report reciprocity_projective_source_audit.md;
- the conductor candidate conductor_round160_reciprocity_projective_obstruction.md;
- the post-blind seam review post_blind_reciprocity_projective_seam.md;
- the independent exact-kernel/power and source-level seam reviews; and
- the Round-160 conductor adjudication and controls.

Primary sources used only under their audited printed hypotheses:

- S. Bettin and V. Chandee, Trilinear forms with Kloosterman fractions,
  Advances in Mathematics 328 (2018), 1234--1262;
- T. Wright, Trilinear Kloosterman fractions I: partially fixed moduli
  and unbalanced convolutions, arXiv:2604.25177v2;
- V. Blomer and D. Milićević, Kloosterman sums in residue classes,
  JEMS 17 (2015), 51--69;
- J.-M. Deshouillers and H. Iwaniec, Kloosterman Sums and Fourier
  Coefficients of Cusp Forms, Inventiones Mathematicae 70 (1982),
  219--288; and
- E. Assing, V. Blomer, and J. Li, Uniform Titchmarsh divisor problems,
  arXiv:2005.13915.

# Blind squarefree reciprocal feasibility report

Campaign: `m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate`
Round: 148
Role: statement-only blind rederiver

## 1. Result: lemma and method no-go

The statement does not contain enough data to reconstruct the actual
signed transform.  In particular, it gives no formula for the outer
\(q\)-amplitude, the placement of the parity and \(\chi _4\) factors,
the cone/profile/collar weights, the family of clipped prefixes, or the
boundary terms.  Consequently an unconditional estimate for the actual
signed transform, and even an exact definition of that transform, cannot
be deduced from the permitted context.  This is a statement-identifiability
no-go, not a counterexample to the intended transform.

There is nevertheless an exact coefficient-sensitive reduction valid for
every completion of the missing data.  After its normalization has been
fixed, write the completed transform as

$$
 \mathcal T(A)=\mathcal B+
 \sum_{d\in\mathcal I}\mu ^2(d)
 \sum_{q\in\mathcal Q}A_q\Gamma(q,d)e(Nd/q),                 \tag{1}
$$

where \(\mathcal Q\subseteq[Q,2Q]\), \(\mathcal I\) is the relevant
dyadic interval or clipped prefix in \([D,2D]\), \(A_q\) is the *actual*
outer amplitude, \(\Gamma\) retains coprimality, parity, character,
cone/profile and collar data, and \(\mathcal B\) is the complete boundary
remainder.  Put

$$
 G_A(d)=\sum_{q\in\mathcal Q}A_q\Gamma(q,d)e(Nd/q),\qquad
 \mathscr E_A(\mathcal I)=
 \sum_{d\in\mathcal I}\mu ^2(d)|G_A(d)|^2.                 \tag{2}
$$

Then

$$
 \boxed{\mathscr E_A(\mathcal I)\ll_\varepsilon
 R^2D X^{2\varepsilon},\quad
 |\mathcal B|\ll_\varepsilon RD X^\varepsilon}
 \quad\Longrightarrow\quad
 \mathcal T(A)\ll_\varepsilon RD X^\varepsilon.           \tag{3}
$$

This is the scale-correct signed reciprocal-dispersion gate.  If
\(|\Gamma|\leq 1\), \(\sum_q|A_q|^2\ll QX^\varepsilon\), and
\(Q\leq R^2\), its \(q_1=q_2\) diagonal is already within the budget in
(3).  Thus the missing mathematical assertion is precisely a bound for
the signed off-diagonal quadratic form for the *actual* \(A_q\), uniform
in every actual profile and prefix.  Size bounds on \(A_q\) alone do not
imply it.

There are two rigorous no-go conclusions.

1. If \(S_q=\sum_d\mu^2(d)\Gamma(q,d)e(Nd/q)\), then
$$
   \sup_{|c_q|\leq 1}\left|\sum_qc_qS_q\right|
   =\sum_q|S_q|.                                             \tag{4}
$$
   Hence a bound uniform in arbitrary favorable \(q\)-coefficients is
   exactly the absolute outer-\(q\) bound.  It is not a genuinely signed
   result.

2. Individual estimates after the Mobius expansion cannot exploit the
   signs \(\mu(a)\).  From data \(|T_a|\leq B_a\) alone, the best uniform
   conclusion for \(\sum_a\mu(a)T_a\) is \(\sum_aB_a\): take
   \(T_a=\mu(a)B_a\).  Thus the placement that yields
   \(Q\sqrt D+D\) cannot be repaired merely by mentioning Mobius
   cancellation; a joint \((a,q)\) estimate or the unexpanded energy
   (2) is necessary.

The failed triangle estimate is target-safe only in the degenerate top
corner

$$
 M\gtrsim DR^2.                                               \tag{5}
$$

Because \(M\leq R^2\), (5) contains no range with \(D\to\infty\); for
\(D=1\) it further requires \(M\asymp R^2\), up to the dyadic constants.
The permitted statement therefore yields no nontrivial target-safe
\(M\)-range by triangle alone.

No conclusion that the absolute squarefree \(Q+D\) analogue is true or
false follows from the supplied information.  Its failed Mobius-triangle
proof is not a refutation.

## 2. Exact statement and hypotheses

The following lemma is the strongest exact statement available without
inventing the omitted transform.

**Lemma (abstract signed dispersion gate).**  Let \(e(t)=e^{2\pi it}\).
Let \(\mathcal Q\) and \(\mathcal I\) be finite integer sets with
\(|\mathcal Q|\ll Q\), \(|\mathcal I|\ll D\).  Let
\(A_q\in\mathbb C\), \(\Gamma(q,d)\in\mathbb C\), and
\(\mathcal B\in\mathbb C\), and define (1)--(2).  Then

$$
 |\mathcal T(A)-\mathcal B|
 \leq \left(\sum_{d\in\mathcal I}\mu^2(d)\right)^{1/2}
       \mathscr E_A(\mathcal I)^{1/2}
 \ll D^{1/2}\mathscr E_A(\mathcal I)^{1/2}.                 \tag{6}
$$

Consequently (3) holds.  If \(|\Gamma(q,d)|\leq1\), then the diagonal
part of \(\mathscr E_A\), when expanded in \((q_1,q_2)\), is at most

$$
 D\sum_{q\in\mathcal Q}|A_q|^2.                              \tag{7}
$$

In particular, \(\sum_q|A_q|^2\ll QX^\varepsilon\) and
\(Q\le R^2\) make (7) \(O(DR^2X^\varepsilon)\).

For any *specified* completion of the qualitative weights, the exact
Mobius identity is

$$
\begin{split}
 \mathcal T(A)-\mathcal B
  =\sum_{a\leq\sqrt{2D}}\mu(a)
    \sum_{q\in\mathcal Q} A_q
    \sum_{\substack{m:\ a^2m\in\mathcal I}}
       \Gamma(q,a^2m)e(Na^2m/q).                             \tag{8}
\end{split}
$$

If, as one possible convention, \(\Gamma\) contains
\(1_{(d,q)=1}1_{2\nmid d}\chi_4(d)W(q,d)\), then (8) becomes

$$
 \sum_{\substack{a\leq\sqrt{2D}\\2\nmid a}}\mu(a)
 \sum_{\substack{q\in\mathcal Q\\(a,q)=1}} A_q
 \sum_{\substack{m:\ a^2m\in\mathcal I\\(m,q)=1\\2\nmid m}}
 \chi_4(m)W(q,a^2m)e(Na^2m/q),                              \tag{9}
$$

because \(\chi_4(a^2m)=\chi_4(m)\) for odd \(a\).  Formula (9) is an
exact model only under that explicitly stated convention; the blind
statement does not say that this is the convention of the intended
transform.  All boundary terms remain in \(\mathcal B\) and require a
separate bound.

The three logically different forms are:

$$
 \begin{array}{ll}
 \text{actual signed:}& |\sum_q A_qS_q|,\\[2mm]
 \text{absolute:}& \sum_q|S_q|,\\[2mm]
 \text{arbitrary coefficient:}&
   \sup_{|c_q|\leq1}|\sum_qc_qS_q|.
 \end{array}                                                  \tag{10}
$$

The last two are equal by (4); the first need not equal either of them.

## 3. Proof or derivation

### 3.1 Dispersion reduction

Reversing the finite sums in (1) gives

$$
 \mathcal T(A)-\mathcal B
 =\sum_{d\in\mathcal I}\mu^2(d)G_A(d).
$$

Cauchy--Schwarz and \(\mu^4=\mu^2\leq1\) give (6), and inserting the
first hypothesis in (3) gives \(RD X^\varepsilon\).  The asserted
boundary estimate then proves (3).

Expanding (2) gives

$$
 \mathscr E_A=
 \sum_{q_1,q_2\in\mathcal Q}A_{q_1}\overline{A_{q_2}}
 \sum_{d\in\mathcal I}\mu^2(d)
 \Gamma(q_1,d)\overline{\Gamma(q_2,d)}
 e\!\left(Nd\left(\frac1{q_1}-\frac1{q_2}\right)\right).    \tag{11}
$$

For \(q_1=q_2\), absolute values and \(|\Gamma|\leq1\) give (7).
The hypotheses \(\sum|A_q|^2\ll QX^\varepsilon\) and \(Q\le R^2\)
put this diagonal at the required scale.  Nothing in the blind statement
controls the \(q_1\ne q_2\) portion of (11).  In particular, replacing
the actual \(A_q\) by arbitrary coefficients destroys exactly the
structure that (11) must use.

### 3.2 Absolute versus signed

The triangle inequality proves the \(\leq\) direction of (4).  For every
\(q\) with \(S_q\ne0\), choose
\(c_q=\overline{S_q}/|S_q|\), and put \(c_q=0\) otherwise.  Then
\(\sum_qc_qS_q=\sum_q|S_q|\), proving equality.  This choice is used only
as the required arbitrary-coefficient control; it is not asserted to be
the coefficient produced by the transform.

A second adversarial control acts directly on (2).  If a row \(d_0\)
has \(|\Gamma(q,d_0)|\asymp1\) for \(\asymp Q\) values of \(q\), choose

$$
 A_q=\frac{\overline{\Gamma(q,d_0)e(Nd_0/q)}}
 {|\Gamma(q,d_0)|}
$$

on that support.  Then \(|G_A(d_0)|\asymp Q\), so
\(\mathscr E_A\gg Q^2\).  Since

$$
 \frac{Q^2}{R^2D}\asymp\frac{DR^2}{M},                       \tag{12}
$$

this violates the desired dispersion scale throughout
\(M\ll DR^2\).  Again this is a countermodel to a *uniform
arbitrary-coefficient theorem*, not to the actual signed amplitude.

### 3.3 Mobius placement and resonances

Substituting \(\mu^2(d)=\sum_{a^2\mid d}\mu(a)\), writing \(d=a^2m\),
and interchanging finite sums proves (8).  Under the stated convention,
\((a^2m,q)=1\) is equivalent to \((a,q)=(m,q)=1\), odd \(d\) forces odd
\(a,m\), and \(\chi_4(a^2m)=\chi_4(m)\), proving (9).

If each \(a\)-piece is bounded separately and then absolute values are
taken, the signs \(\mu(a)\) have disappeared.  More formally, the
inequalities \(|T_a|\le B_a\) permit \(T_a=\mu(a)B_a\); hence no bound
smaller than \(\sum_aB_a\) is a logical consequence of those inequalities.
This proves the Mobius-triangle method no-go.

For a fixed square divisor \(a^2\), a near integer in the geometric
\(m\)-sum is indexed by

$$
 j=Na^2-kq.                                                   \tag{13}
$$

For fixed \((a,j)\), every possible \(q\) divides \(Na^2-j\), so the
number of such \(q\asymp Q\) is at most
\(\tau(|Na^2-j|)\ll_\varepsilon (ND)^\varepsilon\).  At exact resonance
\(j=0\), coprimality \((a,q)=1\) forces \(q\mid N\).  These facts control
fixed near-divisor fibers, but summing them independently over
\(a\le\sqrt D\) recreates the \(\sqrt D\) loss.  They do not make the
supports for different \(a\) disjoint.

### 3.4 Scale audit

Since \(N\asymp X=R^4\),

$$
 Q\asymp D\sqrt{N/M}\asymp \frac{DR^2}{\sqrt M}.
$$

Therefore

$$
 \frac{Q\sqrt D}{RD}
 \asymp\sqrt{\frac{DR^2}{M}}
 =\frac{R}{\sqrt E},\qquad M=DE.                             \tag{14}
$$

Thus triangle is target-safe only if \(M\gtrsim DR^2\), proving (5).
But \(M=DE\le R^2\) gives \(E\le R^2/D\), so (14) is
\(\gtrsim\sqrt D\).  In every range with growing \(D\), the triangle
bound misses the target by at least a growing factor.  This conclusion
uses all allowed \(M\)-ranges, not only a balanced specialization.

## 4. First doubtful or unproved step

The first unproved step needed for the intended theorem is not an
inequality in the argument above; it is the missing exact transform.
The permitted statement does not define \(A_q\), \(\Gamma(q,d)\), or
\(\mathcal B\).  Once those are supplied, the first substantive analytic
obligation is the off-diagonal part of (11), uniformly for every actual
profile, collar and terminal prefix, together with a separate estimate
for \(\mathcal B\).

In particular, (3) is proved only as a conditional reduction.  The
dispersion hypothesis itself is not proved for the intended amplitude.
The absolute squarefree \(Q+D\) analogue is also neither proved nor
refuted here; no countermodel using arbitrary favorable \(q\)-signs may
be reinterpreted as a counterexample to that absolute arithmetic claim.

## 5. Control tests and outcomes

- **Exact signed / absolute / arbitrary coefficient.**  Identity (4)
  shows that absolute and arbitrary-coefficient forms coincide, while
  the actual signed form is a distinct single coefficient vector.
  Outcome: pass; no arbitrary favorable sign is used to prove a target.

- **Mobius decomposition.**  Identities (8)--(9) retain \(\mu(a)\),
  coprimality, parity, character, profile and outer amplitude.  The
  abstract worst case \(T_a=\mu(a)B_a\) proves that separate absolute
  estimates cannot exploit those signs.  Outcome: the source of the
  \(Q\sqrt D\) loss is isolated.

- **Near-divisor multiplicity and small \(j\).**  Equation (13) gives at
  most a divisor-function number of \(q\)'s for fixed \((a,j)\).  The
  fibers for different \(a\)'s are not declared disjoint.  Outcome:
  fixed-fiber control passes, but it supplies no cancellation in \(a\).

- **Dispersion diagonals.**  The diagonal is at most
  \(D\sum|A_q|^2\ll DQX^\varepsilon\le DR^2X^\varepsilon\).
  The off-diagonal is completely unowned.  The one-row aligned
  coefficient test gives (12), showing that coefficient size alone is
  insufficient.  Outcome: diagonal passes; actual off-diagonal remains
  the exact open seam.

- **\(q\mid N\).**  Under coprimality, exact resonances in every
  square-divisor piece reduce to \(q\mid N\).  There are at most
  \(\tau(N)=N^{o(1)}\) such \(q\), so with normalized amplitudes their
  crude total is \(O(DN^\varepsilon)\).  Outcome: this exceptional set is
  harmless at the raw dyadic scale, but does not control near resonances.

- **\(D=1\).**  Only \(a=1\) occurs, so squarefree Mobius expansion causes
  no \(\sqrt D\) loss.  Direct comparison with \(RD\) still makes the
  triangle estimate safe only when \(M\asymp R^2\); smaller \(M\) still
  requires signed \(q\)-cancellation.  Outcome: degenerate control passes
  and does not justify a growing-\(D\) claim.

- **Balanced and unbalanced aspects / every \(M\)-range.**  Formula (14)
  is uniform.  If \(D\asymp E\), the loss is \(R/\sqrt D\), and at the
  top balanced point \(D\asymp E\asymp R\) it is \(\asymp\sqrt R\).
  In the most favorable unbalanced case \(E\asymp R^2/D\), it is still
  \(\asymp\sqrt D\); decreasing \(E\) only worsens it.  Outcome: no
  omitted intermediate \(M\)-range is triangle-safe for growing \(D\).

- **Profiles, collars and terminal prefixes.**  They are retained in
  \(\Gamma\), and (6)--(11) remain exact for each specified clipped set
  and weight.  Promotion would require the energy bound uniformly over
  the actual family.  Because that family is not defined, uniformity
  cannot be checked.  No support-disjointness assertion is used.
  Outcome: conditional algebra passes; actual uniform control is absent.

- **Boundary terms.**  All such terms are kept as \(\mathcal B\), and
  (3) states the bound they must satisfy.  Their formula, count and size
  are absent, so they cannot be owned more precisely.  Outcome: open,
  with no silent deletion.

- **Absolute squarefree \(Q+D\).**  The arbitrary-coefficient identity
  explains why a uniform signed proof would be equally strong.  The
  failed triangle argument alone supplies neither a proof nor a
  counterexample.  Outcome: unresolved and not assumed.

All controls above are algebraic.  No numerical experiment was used;
therefore no diagnostic computation is being offered as certification.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read:

1. `D:\\BaiduSyncdisk\\Codex\\gauss circle\\protocol.md`.
2. `D:\\BaiduSyncdisk\\Codex\\gauss circle\\rounds\\codex-managed\\m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate\\blind_statement.md`.
3. `D:\\BaiduSyncdisk\\Codex\\gauss circle\\rounds\\codex-managed\\m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate\\briefs\\blind_squarefree_reciprocal_feasibility.md`.

No proof graph, proof draft, strategy file, active-campaign file,
Round-147 artifact, sibling report, web source, or computation was used.

## 7. Recommended state effect

**Retain the target open; revise the route.**  Reject any claimed gain
whose hypotheses are only \(|A_q|\ll1\), arbitrary \(q\)-coefficients,
or separate absolute bounds for the Mobius pieces.  Do not promote the
absolute squarefree \(Q+D\) analogue and do not mark it false from the
present evidence.

The next admissible proof kernel is: supply the exact outer amplitude,
weight/profile/prefix definitions and boundary formula; then test the
actual coefficient vector against the off-diagonal form (11).  After
independent seam review, the abstract dispersion reduction (3) and the
coefficient-blind no-go (4) are suitable for retention as lemmas/barriers,
but they do not close the transformed estimate by themselves.

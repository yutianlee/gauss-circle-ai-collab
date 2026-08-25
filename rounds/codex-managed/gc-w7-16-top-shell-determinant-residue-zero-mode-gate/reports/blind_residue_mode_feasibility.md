# Round 131 statement-only report: residue-mode feasibility

## 1. Result: conditional separation lemma and sharp no-go

Put

\[
 A=|a|,\qquad s=\operatorname {sgn}(a),\qquad Q=4A,
 \qquad e(x)=e^{2\pi i x}.
\]

The supplied algebra gives an exact, but only carrier-level,
periodic/BV separation. After splitting the \(O(1)\) determinant lifts
into branches, the M1 quarter carrier is \(Q\)-periodic and its Fourier
support lies in

\[
 h\equiv \varepsilon s\pmod 4,\qquad \varepsilon\in\{+1,-1\}.
\]

Thus, with the convention that a second periodic factor contributes
\(e(hn/Q)\), the counter-frequency which restores the literal zero mode
is \(h\equiv-\varepsilon s\pmod 4\). On a fixed-sign M2 branch the
numerator character is also \(Q\)-periodic, but in general its exact
Fourier frequency is **not determined** by the packet. Under the extra
hypothesis \(4\mid A\), it reduces exactly to a constant multiple of
\(\chi _4(n)\), hence has the two frequencies \(h=\pm A\pmod Q\); the
corresponding counter-frequencies are \(h=\mp A\). The same two raw
character frequencies result when \(b\) is odd and \(q\bmod 4\) is
frozen, but the indicator of that \(q\)-subpacket has its own Fourier
cost. If \(a'\) is held fixed, as in the supplied per-\((r,a')\)
estimate, the M2 numerator character is constant and produces no shift
at all. Consequently there is no coordinate-independent “M2 shifted
zero mode” in the stated hypotheses.

No useful bounded-variation estimate follows. All remaining factors
\(P,T\), stars, floors, cutoffs, and lift-owner indicators may legally
be put into a compactly supported envelope, but the only unconditional
variation estimate is its full triangle-size variation. In particular,
the assertion “\(Q\)-periodic arithmetic factor times a slow BV
envelope” cannot be deduced from the packet.

The determinant congruence supplies only an inverse of the **fixed**
number \(b\) modulo \(A\). It does not supply a complete reduced
residue variable \(x\) together with a phase \(ux+v\bar x\). Hence no
complete quadratic-character or Salié-class sum, no exact Salié
modulus, and no Weil completion saving follow from the supplied
algebra.

Finally, a support-matched diagonal model at \(p=q=n=0\), whenever that
literal cell is present, has coherent M1 and M2 carriers on
\(a\equiv b\equiv1\pmod4\). With \(\asymp LD\) such primitive rays,
\(|A_i(r)|\asymp L^{-1}\), and one per-ray term of the allowed size
\(K_D/L\), the scalar can be as large as

\[
 {DK_D\over L}=Y^{9/16+o(1)}.
\]

This is a family-summed outer-ray obstruction, not merely a per-ray
coherent mode. Reaching \(D=Y^{1/2}\) from it still requires a genuine
cross-ray saving \(K_D/L=Y^{1/16+o(1)}\). The norm data on the actual
outer coefficients do not provide that saving.

## 2. Exact statement and hypotheses

### 2.1 Branchwise carrier/BV lemma

For a fixed primitive \(r=(a,b)\), choose a representative \(p_0(n)\)
of the solution of

\[
 bp\equiv-n\pmod A
\]

which is periodic in \(n\) with period \(A\). Every physical lift in a
top \(p\)-support of total span \(O(A)\) can then be written, after a
bounded branch split, as

\[
 p_k(n)=p_0(n)+kA,\qquad
 q_k(n)={n+bp_k(n)\over a},\qquad
 b'_k(n)=b+q_k(n),
\]

with \(k\) fixed on a branch. The following are the weakest hypotheses
needed for a *useful* separation.

1. Each lift owner is split into finitely many integer intervals and a
   fixed \(k\); all sign changes at \(a'=a+p_k(n)=0\) are split, and the
   undefined point \(a'=0\) is excluded.
2. Every arithmetic factor placed in the periodic part is proved to be
   \(Q\)-periodic on that branch. Any star, floor, threshold, cell, or
   support indicator not proved periodic stays in the envelope.
3. On every resulting interval the exact remaining envelope \(F(n)\)
   has a stated quantitative zero-extended discrete BV bound. Merely
   observing that a finite sequence is of bounded variation is not
   enough.
4. For M2, \(\epsilon_{\rm sgn}\) is fixed (or is itself proved
   \(Q\)-periodic) on the branch. Even \(a'\) terms vanish through
   \(\chi _4(|a'|)\); no division by that zero is used.

Under these hypotheses the exact branch weight has the form

\[
 w_{i,k}(n)=C_{i,k}(n)F_{i,k}(n),
\]

where one may take

\[
 C_{1,\varepsilon,k}(n)
   =e\!\left({\varepsilon b'_k(n)\over4}\right),
 \qquad
 C_{2,k}(n)
   =\epsilon_{\rm sgn}\chi _4(|a+p_k(n)|).
\]

Both carriers are \(Q\)-periodic. This statement is algebraic; it does
not assert that \(F\) is slowly varying.

### 2.2 Exact boundary price

For an owned integer interval \(I=[u,v]\cap\mathbb Z\), define

\[
 \|F\|_{BV_0(I)}
 =|F(u)|+\sum_{n=u}^{v-1}|F(n+1)-F(n)|+|F(v)|.
\]

The first and last terms are exactly the entry and exit jumps of the
zero extension. For a disjoint union of owned intervals, the BV cost
is the sum of these quantities. A threshold equality assigned to one
half-open owner contributes one jump, not zero jumps and not two copies
of the same point. A split at \(a'=0\) contributes the two one-sided
boundary values (the zero point itself is absent). Every floor jump,
star entry, taper endpoint, and sharp support edge must occur either in
the periodic factor or in the displayed variation sum.

If \(F=\sum_t c_{i,t}F_t\), the only automatic consequence of the
Stieltjes bound is

\[
 \|F\|_{BV_0}\leq
 \sum_t|c_{i,t}|\,\|F_t\|_{BV_0}.
\]

Thus \(\sum_t|c_{i,t}|\ll1\) preserves a separately proved uniform BV
bound; it does not create one for \(P\) or \(T\).

### 2.3 Sharp negative statement

From the supplied hypotheses alone one cannot conclude any of the
following:

\[
 \|F\|_{BV_0}=o\!\left(\sum_n|F(n)|\right),
 \qquad
 \sum_{h\bmod Q}|\widehat C(h)|=O(1),
\]

for the *full* induced periodic factor, the vanishing of every shifted
resonant coefficient, a complete Salié sum, or any strict cross-ray
gain. A repaired positive theorem must assume or prove all four
properties at the physical-scalar level.

## 3. Proof and derivation

### 3.1 Physical phase and determinant lifts

After reassembly,

\[
 {a\over b}-{a'\over b'}={ab'-a'b\over bb'}={n\over bb'}.
\]

Therefore the exact oscillatory carriers outside \(P,T\) are

\[
 \begin{aligned}
 \mathrm{M1}_{\varepsilon}:&\quad
 e\!\left({cn\over bb'}+{\varepsilon b'\over4}\right),\\
 \mathrm{M2}:&\quad
 \epsilon_{\rm sgn}\chi _4(|a'|)
 e\!\left({cn\over4bb'}\right).
 \end{aligned}
\]

Since \(p_0(n+A)=p_0(n)\), one has

\[
 q_k(n+Q)=q_k(n)+4s,\qquad
 b'_k(n+Q)=b'_k(n)+4s.
\]

This proves the claimed \(Q\)-periodicity of the M1 carrier. The M2
carrier is already \(A\)-periodic on a fixed lift and fixed sign cell,
because \(p_k(n+A)=p_k(n)\). The \(O(1)\) lift multiplicity is used only
to make a bounded branch sum; it gives no cancellation.

### 3.2 M1 shifted residue modes

The M1 carrier can be written exactly as

\[
 C_{1,\varepsilon,k}(n)
 =e\!\left({\varepsilon s n\over Q}\right)
  e\!\left({\varepsilon b\over4}
       +{\varepsilon s b p_k(n)\over Q}\right).
\]

The second factor is \(A\)-periodic, so its \(Q\)-Fourier frequencies
are \(4j\), \(j\bmod A\). Hence

\[
 \operatorname {supp}\widehat C_{1,\varepsilon,k}
 \subseteq\{\varepsilon s+4j:j\bmod A\}.
\]

Equivalently, if a further periodic factor supplies frequency \(h\), a
literal zero total residue can occur only after the quarter carrier is
countered by \(h\equiv-\varepsilon s\pmod4\). Combining the two M1
branches gives the union of the two odd residue classes and does not
restore a naive zero mode when the rest of the weight is only
\(A\)-periodic.

There is a useful check in the fixed-\(a'\) parameterization. With
\(n\equiv-a'b\pmod A\), define on \(\mathbb Z/Q\mathbb Z\)

\[
 C(n)=\mathbf 1_{n\equiv-a'b\ (A)}
 e\!\left({\varepsilon(a'b+n)\over4a}\right).
\]

Its Fourier transform is supported exactly on
\(h\equiv\varepsilon s\pmod4\); each of its \(A\) nonzero coefficients
has magnitude \(A^{-1}\), so its Fourier \(\ell^1\) cost is exactly one.
This favorable cost belongs to this bare carrier and congruence, not to
the unspecified factors \(P,T\).

### 3.3 M2 numerator modes

For \(a'\neq0\),

\[
 \chi _4(|a'|)=\operatorname {sgn}(a')\chi _4(a').
\]

Thus the absolute value requires a positive/negative sign split but
does not create cancellation between the two sides.

In general \(p_k(n)\) is only specified by a congruence modulo \(A\), so
\(C_{2,k}\) is an arbitrary explicitly induced \(A\)-periodic table;
its \(Q\)-frequencies can be any \(4j\). Its zero coefficient is

\[
 {1\over A}\sum_{x\bmod A}
 \epsilon_{\rm sgn}(x)
 \chi _4(|a+p_k(x)|),
\]

which is not asserted to vanish. In particular, a support packet
restricted to positive \(a'\equiv1\pmod4\) makes the character constant.

There is one clean shifted-mode subcase. If \(4\mid A\), then \(b\) is
odd and reduction of \(n=aq-bp\) modulo \(4\) gives

\[
 p\equiv-\bar b\,n\pmod4.
\]

On a fixed sign cell,

\[
 \chi _4(|a'|)
 =-\operatorname {sgn}(a')\chi _4(b)\chi _4(n).
\]

Since

\[
 \chi _4(n)={e(n/4)-e(-n/4)\over2i},
\]

the two physical character frequencies are exactly
\(h=\pm A\pmod Q\), with total Fourier \(\ell^1\) cost one for the bare
character. More generally, if \(b\) is odd and \(q\equiv q_0\pmod4\)
is frozen, then

\[
 a'\equiv a+\bar b(aq_0-n)\pmod4,
\]

and the raw character again has only the two frequencies \(\pm A\).
The indicator imposing \(q\equiv q_0\pmod4\), however, is an additional
factor and may broaden the full Fourier support. When \(b\) is even,
or when neither \(4\mid A\) nor \(q\bmod4\) is controlled, the stated
congruence does not determine \(a'\bmod4\); no \(\pm A\) conclusion is
legal.

Also, if \(a'\) is fixed before the determinant sum, then
\(\chi _4(|a'|)\) is a constant. This explains why the packet does not
select a unique M2 resonant mode: the answer depends on an unprovided
reorganization identity.

### 3.4 Fourier and BV completion price

For a proved \(Q\)-periodic factor

\[
 C(n)=\sum_{h\bmod Q}\widehat C(h)e(hn/Q),
 \qquad
 \widehat C(h)={1\over Q}\sum_{x\bmod Q}C(x)e(-hx/Q),
\]

summation by parts on \(I=[u,v]\) is exact:

\[
 \sum_{n=u}^{v}F(n)z_n
 =F(v)Z(v)+\sum_{m=u}^{v-1}(F(m)-F(m+1))Z(m),
 \quad Z(m)=\sum_{n=u}^{m}z_n.
\]

Taking \(z_n=e(\psi(n)+hn/Q)\), summing the owned intervals, and using
the zero-extended norm gives the legal bound

\[
 \left|\sum_n C(n)F(n)e(\psi(n))\right|
 \leq \sum_{h\bmod Q}|\widehat C(h)|
 \sum_I\|F\|_{BV_0(I)}
 \max_{M\in I}\left|\sum_{u\leq n\leq M}
 e(\psi(n)+hn/Q)\right|.
\]

No endpoint has disappeared. With only \(|C|\leq1\), Parseval gives

\[
 \sum_{h\bmod Q}|\widehat C(h)|\leq\sqrt Q,
\]

and this generic \(Q^{1/2}\asymp L^{1/2}\) completion cost cannot be
discarded. The unspecified exact factors can attain such a cost.

For fixed \(a'\), where \(b'(n)=(a'b+n)/a\), the nonperiodic physical
phase is

\[
 \psi_i(n)={cn\over\kappa_i b b'(n)},\qquad
 \psi_i'(n)={ca'\over\kappa_i a\,b'(n)^2}.
\]

Thus a Fourier mode \(m\) is locally resonant when

\[
 \left\|{m\over Q}+{ca'\over\kappa_i a\,b'(n)^2}\right\|
\]

is small on the cell. The packet gives neither the size of \(c\), the
cell length, nor a derivative gap, so even after identifying the
carrier shift one cannot discard the shifted mode as nonresonant.

### 3.5 Why Salié algebra does not follow

A complete Salié-class sum would require, at minimum, an exact
finite-to-one parametrization by
\(x\in(\mathbb Z/M\mathbb Z)^\times\), a complete range in \(x\), and a
phase of the form

\[
 e\!\left({ux+v\bar x\over M}\right)
\]

times a specified quadratic character. Here

\[
 p\equiv-\bar b\,n\pmod A
\]

contains only the inverse of the fixed outer denominator \(b\). No
summation variable and its reciprocal occur. The \(g\)-sum is
incomplete, has the weight \(\chi _4(g)/g\), and has no supplied phase
involving \(\bar g\); the \(\rho,v\) stars and divisibility conditions
are not reassembled into a complete reduced residue system. Moreover,
\(P,T\) may depend on the residue being completed.

The missing identity is therefore a bijective (or exactly
equal-multiplicity) physical reparametrization which simultaneously:

1. identifies the complete reduced residue variable and exact modulus;
2. turns the rational phase into \(ux+v\bar x\) modulo that modulus;
3. proves that all remaining stars, divisors, floors, owners, and
   weights are either invariant in \(x\) or have a separately priced BV
   dependence; and
4. identifies the physical quadratic character in that same variable.

No one of these four assertions is contained in the packet. The only
forced candidate modulus for the quarter carriers is \(Q=4A\), but it
is not thereby a Salié modulus. Hence there is no legal Salié
completion cost to quote. Generic \(Q\)-Fourier completion costs up to
\(\sqrt Q\) in Fourier \(\ell^1\), while a hypothetical complete Salié
bound would be a different theorem.

### 3.6 Same-denominator and outer-alignment obstruction

On the exact same-ray diagonal \(p=q=n=0\), with \(\rho=1\), the two M1
branches combine to

\[
 {1\over\pi a}
 \left(e(b/4)-e(-b/4)\right)
 ={2i\over\pi a}\sin {\pi b\over2}.
\]

It is nonzero and has one phase for all \(a>0\),
\(b\equiv1\pmod4\). For M2 the corresponding numerator factor is

\[
 -{4\epsilon_{\rm sgn}\chi _4(a)\over\pi a},
\]

which also has one phase on the fixed sign stratum
\(a\equiv1\pmod4\). The rational phase \(cn/(\kappa bb')\) is exactly
one on this diagonal. Thus neither the M1 quarter pair nor the M2
numerator character removes the exact coherent mode.

There are \(\gg LD\) primitive pairs in dyadic boxes with
\(a\equiv b\equiv1\pmod4\) (elementary Möbius counting in the two
progressions gives positive density). Take \(N\asymp LD\) of them and
set \(|A_i(r)|\asymp L^{-1}\), with phases matched to the displayed
scalar. Then

\[
 \sum_r|A_i(r)|\asymp D,
 \qquad
 \sum_r|A_i(r)|^2\asymp {D\over L}.
\]

If the diagonal physical term has the allowed per-\((r,a')\) size
\(K_D/L\), the coherently summed scalar is

\[
 N\,{1\over L}\,{K_D\over L}
 \asymp {DK_D\over L}=Y^{9/16+o(1)}.
\]

This is a logical countermodel to every deduction based only on the
listed support and outer norms. It is not a claim that the hidden
\(P,T\) make the actual diagonal attain the upper bound: the packet
does not say whether that literal cell vanishes. If it does vanish,
that exclusion itself must be proved from \(P,T\). For same-denominator
terms with \(q=0\) and \(p\neq0\), the M1 carrier is still constant in
\(p\), while the remaining phase is \(e(-cp/b)\); it is aligned across
a full \(O(L)\) packet whenever \(|c|L/D\ll1\). No hypothesis on \(c\)
allows either this alignment or its negation to be used.

For M2, a positive-numerator packet restricted to
\(a'\equiv1\pmod4\) has constant numerator character. A packet crossing
\(a'=0\) can restrict both sides to \(|a'|\equiv1\pmod4\), on which
\(\chi _4(|a'|)=1\). If \(\epsilon_{\rm sgn}\) changes across the
origin, cancellation would still require equal paired \(P,T\), stars,
denominators, and rational phases; no such pairing identity is stated.
If it does not change, the two sides align. Splitting at zero and
charging the two boundaries is therefore the only unconditional legal
operation.

The exponent ledger is

\[
 {K_D\over L}=Y^{11/48-8/48+o(1)}=Y^{1/16+o(1)},
\]

\[
 DK_D=Y^{35/48+o(1)},\qquad
 {DK_D\over L}=Y^{27/48+o(1)}=Y^{9/16+o(1)},
 \qquad D=Y^{24/48}.
\]

Even a full factor \(L\) within-ray saving leaves the factor
\(Y^{3/48}=Y^{1/16}\) to be gained across rays. A merely square-root
residue saving \(L^{1/2}=Y^{1/12}\) would give
\(Y^{31/48+o(1)}\), still \(Y^{7/48}\) above the determinant target.
Cauchy with only the supplied norms gives

\[
 \left(\sum_r|A_i(r)|^2\right)^{1/2}
 \left(\sum_r|S_r|^2\right)^{1/2}
 \leq \left({D\over L}\right)^{1/2}(LD)^{1/2}
 \max_r|S_r|=D\max_r|S_r|,
\]

exactly the outer triangle scale. A strict cross-ray theorem about the
physical complex scalar is indispensable.

## 4. First doubtful or unproved step

The first unavailable step is **before** Fourier expansion: no formula
or quantitative variation bound is supplied for the exact induced
remainder after \(P,T\), frequency floors, stars, determinant tapers,
threshold owners, support entries/exits, and the \(\rho,g,t\) sums are
expressed in the determinant lift variable. Therefore it is unknown
whether these factors are \(Q\)-periodic, slowly BV, or arithmetically
oscillatory with a larger modulus. The bound
\(\sum_t|c_{i,t}|\ll1\) does not repair this omission.

The next unavailable step is the complete-residue/inverse identity
listed in Section 3.5. Even if both steps were supplied and yielded a
full within-ray factor \(L\), the final unavailable step would be a
physical cross-ray cancellation estimate of size at least
\(K_D/L=Y^{1/16+o(1)}\) beyond the stated coefficient norms.

## 5. Required control tests and outcomes

All outcomes below are algebraic; no numerical experiment was used.

| Control | Exact input | Expected invariant or failure | Outcome | Implication |
|---|---|---|---|---|
| Periodic/BV before Fourier | Branches \(p_k(n)\), exact \(P,T\), floors, stars, and owned support | Every nonperiodic jump must be charged to \(BV_0\) | Carriers are \(Q\)-periodic; no useful BV bound for the remainder is supplied | Full-weight Fourier expansion is presently illegal as a saving argument |
| Shifted mode modulo \(Q\) | M1 \(e(\varepsilon b'/4)\); M2 \(\chi _4(|a'|)\) | Carrier shifts must be included before calling a mode zero | M1 modes are \(h\equiv\varepsilon s\pmod4\). M2 gives \(h=\pm A\) only under the stated extra hypotheses; fixed \(a'\) gives no shift | A naive \(h=0\) analysis is wrong, but no universal M2 replacement exists |
| Same-denominator M1 | \(p=q=n=0,\rho=1,b\equiv1\pmod4\) | Test exact Fejér/diagonal coherence | The two carriers give \(2i/(\pi a)\), not cancellation | A per-ray exact coherent mode is allowed unless \(P,T\) kill the cell |
| Positive-numerator M2 | \(a'>0,\ a'\equiv1\pmod4\) | Check whether \(\chi _4\) forces cancellation | The character is identically \(+1\) on the packet | No coefficient-blind character saving is valid |
| Sign-crossing M2 | \(a'=\pm u,\ |u|\equiv1\pmod4,\ a'=0\) excluded | Check parity/absolute-value pairing | \(\chi _4(|a'|)\) aligns on both sides; a possible \(\epsilon_{\rm sgn}\) flip has no matching \(P,T\)/phase identity | Split the signs and charge both boundaries; no cross-sign cancellation follows |
| Scalar versus positive energy | The displayed complex one-sided scalar and coherent outer phases | Energy cannot replace phase-sensitive summation | The obstruction is constructed directly in the scalar; no positive energy is invoked | An energy bound would not resolve the coherent mode |
| Per-ray versus cross-ray | \(\#r\ll LD\), \(\ell^1\leq D\), \(\ell^2{}^2\leq D/L\) | Uniform per-ray bounds plus Cauchy should not manufacture a gain | Both triangle and Cauchy permit \(D\max|S_r|\); the diagonal family permits \(DK_D/L\) | A separate cross-ray cancellation theorem is necessary |
| Salié identification | \(p\equiv-\bar b n\pmod A\), incomplete \(g\)-sum, stars and divisors | Need a complete variable \(x\) and its reciprocal | Only the fixed inverse \(\bar b\) occurs; no \(x,\bar x\) phase or complete range is supplied | No Salié modulus or Weil bound is available |
| Raw versus weighted | \(O(1)\) \(p\)-lift count versus the physical \(1/a'\), \(1/g\), \(\mu(\rho)\), \(P,T\) weights | Multiplicity is not weighted cancellation | No raw count is converted into a mass saving; the countermodel is normalized only to the supplied \(K_D/L\) bound | No exponent is transferred from lift count |
| Signed versus unsigned/adversarial | Exact M1 branch signs and M2 \(\chi _4\); absolute and residue-restricted packets | A signed saving must identify the symmetry that fails unsigned | M1 becomes an exact sine but is coherent for odd \(b\); M2 is constant on one residue packet | Random signs and absolute values are irrelevant; the missing symmetry is explicit |
| Exact versus near resonance | \(n=0\) diagonal and the derivative formula for \(n\neq0\) | Exact and near modes must remain separate | Exact coherence is proved conditionally on cell presence; no derivative gap for nearby \(n\) follows | The obstruction is exact only; no near-resonance theorem is claimed |
| Coefficient adversary | Only the supplied outer \(\ell^1,\ell^2\) data | Norm data permit coherent phases | \(A_i(r)\asymp L^{-1}\) on \(LD\) rays saturates both norms and the scalar obstruction | This is a no-go for norm-only deduction, not an assertion about hidden fixed coefficients |
| Support and degeneracy | Literal top shell, repeated denominator, \(\rho=1\), \(a'=0\), sharp/half-open edges | Every excluded cell and boundary must be explicit | The diagonal is not excluded in the packet; \(a'=0\) must be excluded; all entries/exits are in \(BV_0\) | A positive theorem must prove diagonal vanishing or bound it separately |
| Dyadic endpoint | \(D=Y^{1/2}\) exactly | No below-endpoint averaging may cross the endpoint | All calculations remain on the literal top shell | No endpoint extrapolation is used |
| Real versus complex pairing | Complex \(A_i(r)\) and the two M1 carriers | A real-part shortcut requires conjugacy | The exact complex carrier pair is retained and outer phases may align | No \(\operatorname {Re}\) or symmetric-weight shortcut is used |
| Known lower-bound families | Only the names UNC, TS, W-1 occur in the permitted control file | Their parity, support, and weight envelopes would need exact definitions | Those definitions are absent from the permitted statement-only packet, so no audit was possible | No positive unsigned or absolute near-collision claim is made |
| No global exponent/M9 promotion | \(DK_D/L=Y^{9/16}\) versus \(D=Y^{1/2}\) | A within-ray result must be paired with cross-ray gain | A factor \(Y^{1/16}\) remains even after a full \(L\) saving | No global exponent claim and no M9-type promotion are supported |

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were used:

1. problems/gauss_circle.md — definition and research scope.
2. state/control_models.md — required proof-unit controls.
3. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/blind_statement.md — all scales, the physical scalar, branch data, determinant identity, coefficient norms, and exponent baselines.
4. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/briefs/blind_residue_mode_feasibility.md — task isolation and report contract.

No proof graph, proof draft, strategy file, historical nonblind artifact,
sibling report, web source, or computation was consulted. The standard
finite Fourier transform, discrete summation by parts, and elementary
coprime-pair count were derived or used directly above.

## 7. Recommended state effect

**Retain** this report as a sharp statement-only obstruction and revise
any candidate residue-zero-mode lemma to include: (i) an exact
branchwise \(Q\)-periodic/BV factorization with all endpoint and Fourier
\(\ell^1\) costs; (ii) the M1 shifted cosets and the conditional, not
universal, M2 \(\pm A\) modes; (iii) the missing complete-variable/inverse
identity before any Salié claim; and (iv) a strict physical cross-ray
saving of at least \(Y^{1/16+o(1)}\) after a full within-ray factor
\(L\). Do not promote a global exponent, a Salié saving, or an M9-type
claim from the supplied hypotheses.

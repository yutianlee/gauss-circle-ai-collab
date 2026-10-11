# Round 209: exact rational fifth-convolution energy and the signed near residual

## 1. Result: a target-safe exact part, with no complete tenth-moment gain

Campaign: `gc-complete-signed-tenth-moment`. Task: `signed_fifth_convolution`.
Role: selected-context discovery, not blind. Generated: 2026-09-27T15:07:03Z.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: 100 percent analysis/algebra, zero mathematical
numerical experiments. There are two mechanisms: exact denominator arithmetic,
then attempted character cancellation on the remaining near relations.

The complete exact total-frequency diagonal of the rational fifth convolution
is bounded by

\[
 \boxed{\mathcal D_{10}:=\int_J\sum_\mu |C_\mu(x)|^2\,dx
       \ll_\epsilon XH Q^4T^\epsilon
       \ll_\epsilon T^{7+\epsilon}N^{-1/2}.}                 \tag{1}
\]

Here \(Q\asymp T\) bounds the reduced denominators, and \(C_\mu\) is the
**complete** fifth convolution of the already grouped physical coefficient
vector, defined below. Both arms, every nonpairing exact relation, the actual
variable width and the moving prefix are included. The proof uses the fact
that the product of the ten reduced denominators in a zero rational relation
is squarefull. It does not assume pairwise matching.

This is smaller than the requested gate
\(G=T^{473/65}N^{-1/2}\) by \(T^{18/65}\), before epsilon losses.
Thus it quantitatively removes the exact rational diagonal from the next
estimate. It is not a bound for the full tenth moment: the displaced signed
off-diagonal remains open.

There is also an actual-coefficient obstruction to closing that remainder by
taking absolute values on the individual ten-factor integrals. Even after
**every exact rational relation has been removed**, the part with
\(0<|\Delta|\le\zeta/X\), for a fixed sufficiently small \(\zeta>0\), satisfies

\[
 \boxed{\mathfrak A_{10}^{\mathrm{near},\ne0}\gg X^5H
                    =T^{11}N^{-1/2}.}                    \tag{2}
\]

Its excess over the tenth gate is \(T^{242/65}\). This is a lower bound for
the specified positive majorant, **not** for the signed moment or for a
majorant taken after full signed total-frequency aggregation. In particular,
it leaves that aggregation as an unproved possible source of cancellation.
No improved complete moment, pointwise exponent, M1/M2 bound or quarter
theorem is established.

## 2. Exact statement and hypotheses

Let \(T\ge2\) be real, \(X=T^2\), \(J=[X/2,3X]\), and retain every dyadic

\[
 T^{166/325}<N<T^{242/325},\qquad
 H=T/\sqrt N,\qquad h(x)=2\sqrt x/\sqrt N.
\]

Use precisely the fixed mollifier and partition from the permitted physical
interface. In the orientation of the Round207 discovery reports, put

\[
 a(t)=t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2),\quad
 F(u)=-\int_1^2 a(t)\sin(2\pi tu)\,dt,
 \quad Z_N(x)=\sum_{m\ge1}(r_2(m)-\pi)F((m-x)/h(x)).       \tag{3}
\]

This is the same oriented physical shell as in the inherited bridge.
With \(e(u)=\exp(2\pi iu)\) and Fourier transform using \(e(-u\xi)\),
\(\widehat F(\xi)=(i/2)\operatorname{sgn}(\xi)a(|\xi|)\), supported in
\([-2,-1]\cup[1,2]\). The seminorms are uniform. Since \(N/T\to0\) uniformly
in this band, \(a\ge0\) for all sufficiently large \(T\); it has a uniformly
positive fixed interior subinterval. Upper bounds absorb bounded \(T\) into
their constants; the lower obstruction is an asymptotic statement.

Keep the prescribed cutoff
\(M=\lceil6X\rceil\), \(D=\lfloor\sqrt M\rfloor\),
\(L=\lfloor M/(D+1)\rfloor\), and set \(Q=\max(D,4L)\asymp T\).
There is no change to even \(D\). Define

\[
 s(y)=\sum_{1\le j\le y}\frac{\chi_4(j)}j,\qquad
 s_*(y,z)=\sum_{\substack{j\ge1\\j\le y,\ j<z}}
                 \frac{\chi_4(j)}j.
\]

The complete rational main term, in the phase convention \(e(-\lambda x)\), is

\[
 Q_N(x)=\sum_{\lambda\in\Lambda}c_\lambda(x)e(-\lambda x),
 \qquad c_{-\lambda}=\overline{c_\lambda}.                 \tag{4}
\]

For positive reduced fractions its exact coefficients are

\[
 c^A_{a/q}(x)=\frac{4h(x)\chi_4(q)}q
      \widehat F(h(x)a/q)s(D/q),
 \quad q\le D\text{ odd},\ (a,q)=1,                      \tag{5}
\]

\[
 c^B_{a/(4b)}(x)=\frac{2ih(x)\chi_4(a)}b
      \widehat F(h(x)a/(4b))s_*(L/b,x/(Db)),
 \quad b\le L,\ a\text{ odd},\ (a,b)=1.                 \tag{6}
\]

The union \(\Lambda\) includes all frequencies active anywhere on \(J\), with
zero coefficient where inactive. Formula (6) keeps its strict moving prefix.
The two denominator classes are disjoint, so all single-frequency collisions
have already been combined. They do not make higher sums disjoint.

The inherited, uniformly valid threshold/tail estimate is

\[
 Z_N=Q_N+R_N+O_A(T^{-A}),\quad
 \|R_N\|_\infty\ll1,\quad
 \int_J|R_N|^{10}dx\ll TH.                               \tag{7}
\]

The last assertion follows directly from the inherited sixth estimate
\(\int|R_N|^6\ll TH\) and its supremum, so no new threshold hypothesis is
introduced. The formula includes partial endpoint bumps and real equality
points. The even-cutoff cancellation is not needed.

Let \(\mathcal S=\Lambda+\cdots+\Lambda\) with five summands and set

\[
 C_\mu(x)=\sum_{\substack{\lambda_1,\ldots,\lambda_5\in\Lambda\\
                              \lambda_1+\cdots+\lambda_5=\mu}}
                 \prod_{j=1}^5c_{\lambda_j}(x).
                                                                    \tag{8}
\]

All ordered tuples, signs, arms and multiplicities occur in (8). Define

\[
 \mathcal O_{10}=
 \sum_{\substack{\mu,\nu\in\mathcal S\\\mu\ne\nu}}
  \int_J C_\mu(x)\overline{C_\nu(x)}e(-x(\mu-\nu))\,dx.    \tag{9}
\]

Then exactly
\(\int_J|Q_N|^{10}=\mathcal D_{10}+\mathcal O_{10}\).
The off-diagonal is real by conjugate pairing and may be negative.

## 3. Proof and the two fully scoped mechanisms

### Mechanism one: denominator arithmetic controls every exact relation

For every fixed real \(x\in J\), an active reduced frequency \(a/q\) in either
arm satisfies

\[
 cH\le q\le Q,\quad 0<|a|\le Cq/H,\quad
 |c_{a/q}(x)|\le C H/q.                                  \tag{10}
\]

Indeed \(h\asymp H\), Fourier support gives \(1\le h|a|/q\le2\), and the
nonempty alternating prefixes in (5)--(6) lie in \([2/3,1]\); the empty prefix
is zero. In (6), \(b=q/4\), so its prefactor is also \(O(H/q)\).
These are pointwise statements for the actual width and mask. The number
of possible signed numerators for a given active denominator is \(O(q/H)\),
including any endpoints; there is no coefficient differentiation or width
freezing.

Consider a zero relation

\[
 \sum_{j=1}^{10}\epsilon_j a_j/q_j=0,\qquad
 (a_j,q_j)=1,\quad\epsilon_j\in\{-1,1\}.                 \tag{11}
\]

Signed numerators could equivalently absorb the \(\epsilon_j\). For a prime
\(p\) dividing at least one denominator, let \(v\) be the largest of the
\(p\)-adic valuations \(v_p(q_j)\). If exactly one index has valuation \(v\),
multiply (11) by \(\operatorname{lcm}(q_1,\ldots,q_{10})\) and reduce modulo
\(p\). The unique maximal-valuation term is a unit modulo \(p\); every other
term is zero. This is impossible. The largest valuation therefore occurs
at least twice. In particular every prime dividing

\[
 n=q_1q_2\cdots q_{10}
\]

occurs to exponent at least two: \(n\) is squarefull. This necessary condition
does not assert that the ten terms pair.

Now put the largest denominator in a dyadic interval \((R/2,R]\), and choose
one largest-denominator index \(j_0\). Allowing all ten choices costs a factor
at most ten; ties can instead be broken by the smallest index. Every
denominator is at most \(R\), so \(n\le R^{10}\).

The number of squarefull integers \(n\le Y\) is \(O(Y^{1/2})\): each has a
unique representation \(n=u^2v^3\) with \(v\) squarefree, and the count is
at most
\(Y^{1/2}\sum_{v\ge1}v^{-3/2}\).
For any fixed \(\varepsilon>0\), the number of ordered ten-factor
factorizations of a given \(n\) is \(\tau_{10}(n)\ll_\varepsilon
n^{\varepsilon/10}\). This is the usual fixed-order elementary divisor
bound, with its epsilon chosen before applying it. Hence the number of
ordered denominator tuples under consideration is

\[
 \ll_\varepsilon R^{5+\varepsilon}.                      \tag{12}
\]

Conditions \(q_j\ge cH\), parity and the stronger maximal-valuation rule
can only reduce this upper bound.

For a fixed denominator tuple, choose the other nine signed numerators first.
There are at most \(C^9\prod_{j\ne j_0}(q_j/H)\) choices by (10). Relation
(11) then determines \(a_{j_0}\) uniquely, if it is an admissible integer at
all. The total absolute coefficient weight of all these choices is at most

\[
 C^{10}\frac{H^{10}}{\prod_jq_j}
       \prod_{j\ne j_0}\frac{q_j}{H}
 \ll \frac H{q_{j_0}}\ll H/R.                            \tag{13}
\]

Thus the full exact-relation absolute coefficient mass at this dyadic maximum
is \(O_\varepsilon(HR^{4+\varepsilon})\). There are only \(O(\log T)\)
possible dyadic maxima; their geometric sum is
\(O_\varepsilon(HQ^{4+\varepsilon})\). The factor ten and any harmless
logarithms are included. This proves, uniformly for each real \(x\),

\[
 \sum_{\substack{\lambda_1+\cdots+\lambda_5
                         =\lambda_6+\cdots+\lambda_{10}}}
       \prod_{j=1}^{10}|c_{\lambda_j}(x)|
 \ll_\varepsilon H Q^4T^\varepsilon.                    \tag{14}
\]

Expanding \(|C_\mu|^2\) and taking absolute values **only within the exact
part** shows that \(\sum_\mu|C_\mu(x)|^2\) is at most (14). Integrating over
\(|J|\asymp X\) proves (1). The same argument bounds the termwise integrated
absolute **exact-zero** expansion by (1), a fact needed below.

This proof never uses a denominator squarefull condition for a nonzero
relation. In that case the cleared numerator need not be zero modulo \(p\),
and the contradiction establishing (12) disappears.

### Mechanism two: signs on the nonzero near relations

The complete target, after (1), is precisely the estimate

\[
 \boxed{|\mathcal O_{10}|\ll_\varepsilon
                         T^{473/65+\varepsilon}N^{-1/2}.} \tag{15}
\]

For the comparison of upper bounds this is equivalent to the complete
\(Q_N\) tenth gate: in one direction use its exact expansion and (1), and
in the other use
\(|\mathcal O_{10}|=|\int|Q_N|^{10}-\mathcal D_{10}|
\le\int|Q_N|^{10}+\mathcal D_{10}\).
It retains exact equalities **inside** each coefficient \(C_\mu\), every
nonzero separation between total frequencies, all width variation and all
moving-prefix changes. No near frequency is replaced by its bin center.

The proposed elementary cancellation was to average \(\chi_4\) within
these total-frequency fibres before applying a positive norm. It does not
give a bound. In the first arm the positive-frequency coefficient is
\(i\chi_4(q)\) times a nonnegative amplitude, independently of its numerator.
For a fixed odd \(q\), every positive five-tuple with that denominator and
fixed numerator sum therefore has the same phase \(i\chi_4(q)\).
There is no numerator character orthogonality to use. Summing over \(q\)
does not repair this by the identity \(\sum_{r\bmod4}\chi_4(r)=0\): changing
one denominator changes the rational total frequency and the other
coprimality constraints, and the fibre is not a complete residue progression.

An explicit nonpairing control uses \(q=3^k\), \(a\equiv0\pmod3\), with
all displayed numerators positive and lying in a small interior Fourier
amplitude interval. The two tuples

\[
 (a-2,a-2,a+1,a+1,a+2),\qquad
 (a-1,a-1,a-1,a+1,a+2)                                   \tag{16}
\]

both sum to \(5a\), all numerators are coprime to \(q\), and their multisets
differ. Choose the power of three in \((D/3,D]\); because \(q/H\to\infty\),
a multiple of three can be chosen with all these numerators in that fixed
amplitude interval at \(x=X\). Its interval has length comparable to
\(q/H\), so bounded shifts do not affect admissibility for large \(T\).
These are actual exact rational relations. Their same-denominator
positive-convolution contributions reinforce. This is a control against
that proposed orthogonality, not a claim that other denominators or arms
cannot cancel them in the complete \(C_\mu\).

The stronger obstruction concerns the subsequent absolute near closure.
For ordered positive first-arm frequencies \(\lambda_1,\ldots,\lambda_5\)
and \(\mu_1,\ldots,\mu_5\), put
\(\Delta=\sum\lambda_j-\sum\mu_j\). The majorant in (2) is the sum,
over **all** ordered ten-frequency choices from (4) with
\(0<|\Delta|\le\zeta/X\), of

\[
 \left|\int_J
 \prod_{j=1}^5c_{\lambda_j}(x)
 \overline{\prod_{j=1}^5c_{\mu_j}(x)}
 e(-x\Delta)\,dx\right|.                                \tag{17}
\]

To prove its lower bound use only a genuine first-arm positive subsum.
Choose fixed \(u<u'<v'<v\) inside a uniformly positive amplitude interval,
put \(h_0=h(X)=2H\), and let \(\mathcal C\) consist of reduced \(a/q\) with

\[
 D/2\le q\le D,\quad q\text{ odd},\quad(a,q)=1,
 \qquad u'q/h_0\le a\le v'q/h_0.                         \tag{18}
\]

The count is \(|\mathcal C|\asymp D^2/H\). For clarity, Mobius inversion
counts the numerator interval as
\((v'-u')\varphi(q)/h_0+O(\tau(q))\), and

\[
 \sum_{q\le Y,\ q\ {\rm odd}}\varphi(q)
 =\frac{Y^2}{4}\prod_{p\ {\rm odd}}(1-p^{-2})
                                  +O(Y\log(2Y)).
\]

This last elementary formula follows by inserting
\(\varphi(q)=q\sum_{d\mid q}\mu(d)/d\) and summing odd multiples.
Its positive main term after differencing at \(D/2\) dominates the
\(O(D\log D)\) numerator error, since \(D/H\asymp\sqrt N\) grows by a
fixed positive power throughout the band.

For a sufficiently small fixed \(\delta>0\), on
\(J_0=[(1-\delta)X,(1+\delta)X]\) every coefficient in (18) has the form
\(i\chi_4(q)b_\lambda(x)\) with
\(b_\lambda(x)\ge w_\lambda=cH/D\). The same amplitude is nonnegative
on **all** \(J\). This keeps the exact width; it only uses continuity to
choose \(J_0\). Hence \(\sum_{\mathcal C}w_\lambda\asymp D\).

The positive five-sums occupy an interval of length \(O(1/H)\). Partition
it into half-open bins of width \(\zeta/X\). There are \(O(X/H)\) bins.
If \(m_j\) is the total product weight of ordered five-tuples in bin \(j\),
Cauchy gives

\[
 \sum_jm_j^2\gg \frac{D^{10}}{X/H}=D^{10}H/X.             \tag{19}
\]

Pairs in one bin satisfy \(|\Delta|\le\zeta/X\). Their coefficient product
has an \(x\)-independent sign: \(i^5(-i)^5=1\) and the remaining sign is
the product of the actual ten characters. Remove that sign and rotate by
\(e(X\Delta)\). For sufficiently small fixed \(\zeta\),
\(\cos(2\pi(x-X)\Delta)\ge1/2\) on all \(J\). Nonnegative amplitudes
therefore prevent cancellation from other parts of \(J\), and each
integral has modulus at least \(cX\) times its product weight. Summing
(19) proves a lower bound \(cD^{10}H\asymp X^5H\), initially including
\(\Delta=0\).

By (14), the entire exact-zero termwise integral majorant is
\(O_\varepsilon(XHQ^4T^\varepsilon)\). Relative to the preceding lower
bound its size is \(O_\varepsilon(T^{-4+\varepsilon})\). Removing every
exact relation consequently leaves (2), with only nonzero near relations.
This subtraction is lawful because both quantities here are positive
majorants. No positive subsum is claimed for the signed moment (9).

### Restore all tenth-power and pointwise costs

The complete shell error in (7) costs \(TH=T^2N^{-1/2}\), far below
\(G\). The physical bridge is
\(H_N(R)=R^{-1/2}Z_N(R^2)+O_\varepsilon(T^{-1/2+\varepsilon}N^{-1})
+O_A(T^{-A})\). Therefore, with \(dR=dx/(2\sqrt x)\),

\[
 M_{10}(H_N)\ll_\varepsilon T^{-6}\int_J|Q_N|^{10}dx
       +T^{-4}N^{-1/2}
       +T^{-4+\varepsilon}N^{-10}+O_A(T^{-A}).            \tag{20}
\]

The converse gate implication follows from the same triangle inequality
applied to the inverse bridge. The factor \(T^{-6}\) includes both the
tenth power of \(R^{-1/2}\) and the Jacobian. Thus (1) costs only
\(T^{1+\varepsilon}N^{-1/2}\) on the physical side, whereas (15) would
give the required \(T^{83/65+\varepsilon}N^{-1/2}\).

No known complete upper bound is improved here. Keeping both inherited
terms gives

\[
 \int_J|Q_N|^{10}\ll_\varepsilon
       T^{7+\varepsilon}N^{-3/110}+T^{6+8\omega+\varepsilon},
 \quad\omega=\min(\alpha/4,\beta,(1-\alpha)/2),\ N=T^\alpha.
                                                                    \tag{21}
\]

Adding the much smaller (1) gives the same available bound for
\(|\mathcal O_{10}|\). Relative to the target its two deficits are
\(1-83/65+26\alpha/55\) and
\(8\omega-83/65+\alpha/2\). The latter dominates throughout the complete
required band, with supremum \(7\beta-101/130\) at
\(\alpha=1-2\beta\). No \(T^{8\omega}\) term has been dropped.

If (15) were proved on the whole band, the reviewed local reproduction
factor \(N^{1/20}\), all complementary scales, singleton, infinite tail
and dyadic recombination would give only the milestone \(102/325\).
The lower and upper band equalities remain in their already bounded outer
ranges. The present exact-diagonal result does not supply (15), improve
that pointwise benchmark, or settle the independent M1/M2 obligations.

## 4. First doubtful or unproved step

The first unproved estimate is exactly (15), for the full signed
nonzero-total-frequency expression (9), with every arm, prefix and width
factor retained. The denominator proof of (14) applies only to zero
relations and supplies no near-relation squarefull condition.

The first invalid step in the attempted mod-four cancellation would be
to treat a constrained rational total-frequency fibre as a complete
character progression. Formula (16) explicitly refutes numerator
orthogonality in an actual fibre. The first invalid step in a subsequent
termwise absolute closure would be a target-size estimate for (17):
the actual lower bound (2) refutes it by a factor \(T^{242/65}\).

Neither conclusion refutes cancellation after full signed aggregation in
\(C_\mu\), cancellation between different total frequencies in the
displaced window, or a different direct actual-shell argument. No theorem
for these remaining cancellations has been imported or implicitly assumed.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | PASS within the stated claims: (5)--(6) are the actual grouped coefficients, including character zeros and exact alternating prefixes; the obstruction uses their fixed signs and nonnegative actual Fourier amplitudes. |
| `complete_scales` | PASS: (1), (7), (14), and (20)--(21) hold for every required middle dyadic scale; the missing estimate is stated on that entire band. |
| `signed_absolute_distinction` | PASS: the exact positive energy is bounded from above, while (2) lower-bounds only the explicitly defined individual-integral majorant. No signed lower bound follows. |
| `exact_nonpairing_relations` | PASS: the prime-valuation proof bounds every exact relation; (16) is a concrete nonpairing one. All exact relations are subtracted before (2) is asserted. |
| `real_endpoints` | PASS: all coefficient bounds are pointwise for real x, the strict prefix remains in (6), and actual width, real T, partial boundary bumps, support endpoints and all progression tails retain the inherited conventions. |
| `all_costs_restored` | PASS: largest-index factor ten, squarefull divisor multiplicities, dyadic maximum sum, interval length, threshold tenth power, Jacobian, physical error, both existing complete terms and reconstruction costs are displayed. |
| `full_quarter_scope` | PASS: even the unproved complete gate gives only 102/325; no full quarter or M1/M2 promotion is claimed. |
| `statement_only_control` | NOT supplied by this selected-context claimant. The conductor has stated that an independent seam review will be obtained; this report does not impersonate that review or the separate isolated task. |

All controls here are analytical. No mathematical numerical experiment,
arbitrary-sign counterexample to the actual coefficients, or external
unverified theorem was used.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted local context were read:

- `protocol.md`.
- `state/proof_obligations.yml`, particularly the open GC/M1/M2 scope,
  repaired Li--Yang dependency, complete large-value bound and separate
  exact-square-root-resonance scope. These graph claims are not extended
  from radical frequencies to rational frequencies by assertion.
- `state/active_campaign.yml`, Round209.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/briefs/signed_fifth_convolution.md`.
- `strategy/round209_complete_signed_tenth_moment_attack.md`.
- `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/reports/periodic_hyperbola_attack.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/reports/signed_rational_moment_attack.md`.

The inherited reports supply the exact physical rational representation,
threshold/tail estimates, uniformly positive Fourier core and complete
bridge. The new squarefull denominator estimate is derived in full here.
The five-tuple binning argument is the explicitly repriced ten-factor
version of the permitted sixth-majorant construction; its removal of all
exact relations uses the new bound (14). The elementary fixed-order
divisor estimate is the same standard elementary input already allowed
by the authoritative graph. No web theorem or new source card is used.

The conductor received the squarefull argument and exact/near separation
as substantive interim findings, then requested explicit verification of
the denominator count, maximum-index choice, real-x bounds and the failure
of extension to nonzero relations. Those points are all included above.
No sibling report or excluded file was read.

## 7. Recommended state effect

**Retain the complete signed tenth gate and all pointwise parents open.**
Subject to the conductor's independent seam review, the exact rational
diagonal lemma (1)/(14) is a candidate for acceptance as a scoped estimate:
it removes the whole exact part at a quantified target-safe cost, including
nonpairing relations. The separate absolute near-majorant result (2) is
a candidate scoped obstruction, not a rejection of the signed gate.

The complete outcome label remains `no_new_bound_precise_open_residual`;
the termwise absolute closure additionally has the rigorous
`scoped_actual_method_no_go` outcome. No shared graph, proof draft,
validation matrix, synthesis, legacy file or successor artifact was edited.
Only this assigned report was written. The task stops here.

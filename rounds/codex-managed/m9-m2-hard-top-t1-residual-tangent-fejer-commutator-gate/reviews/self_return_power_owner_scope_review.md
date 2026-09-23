# Round 173 self-return, power, and owner-scope review

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Role: independent adjoint, stopped-chain, power, false-control, and owner-scope reviewer
- Candidate reviewed: candidates/formalized_tangent_fejer_commutator_self_return_obstruction.md
- Starting graph: 70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Verdict: **REPAIR — the mathematical core is GREEN, but the exact statement needs the even-gap summation domain, the identity \(M=M_L\), and sharper capacity/scope wording before promotion**

## 1. Result

The candidate's central result is correct. For the full zero-extended
tangent line, the adjoint of the displayed forward difference at character
frequency \(\pi\) produces an adjacent **sum**, not a small difference:

\[
 \mathcal R_{R,T}
 =\Re\sum_s(-1)^s\{\beta_{R,T}(r_s)+
                         \beta_{R,T}(r_{s+1})\}G(s).
\tag{173.S1}
\]

Consequently

\[
 \mathcal R_{R,T}=\Delta_{R,T}-\mathcal C_{R,T}
\tag{173.S2}
\]

link by link, and on the complete stopped chain

\[
 \sum_j\mathcal R_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})
  -\sum_j\mathcal C_{R_j,R_{j+1}}.
\tag{173.S3}
\]

The factor \(2\), the plus sign before \(B_{\rm short}\) in (173.S3),
and the once-only short correction are correct. Since the complete
commutator and \(B_{\rm short}\) are bounded in absolute value by
\(O_\varepsilon(L^3X^\varepsilon)\), the one-sided whole-chain remainder
estimate is equivalent to the one-sided K26 estimate at target strength.
This preserves one outer real part and permits cancellation between links.

The candidate also has the right power distinction. The commutator has the
small multiplier \(O(L/R)\) and is target-safe at
\(L^3X^\varepsilon\). The adjacent-sum remainder has only the available
coefficient-uniform positive/absolute scale \(RL^2X^\varepsilon\), which
reaches \(L^4X^\varepsilon\) on a maximal link. The latter is an envelope
capacity, not a proved lower bound for the literal residual coefficient.

Three local statement repairs are mandatory:

1. Set \(M=M_L\asymp L^2\), rather than leaving \(M\) as an unspecified
   comparable scale, because K26 and the stopped-chain correction use the
   exact containing-interval endpoint \(M_L\).
2. Restrict every complete-link tangent sum explicitly to
   \(d>0\) odd, \(m\ge1\), \(v\in2\mathbb Z\), and
   \(s\in\mathbb Z\), with both opened atoms literal and positive. The
   candidate currently writes an unrestricted \(\sum_{d,m,v,s}\), which
   would include odd physical gaps if read literally.
3. State the \(L^4\) conclusion as an available positive/adversarial
   capacity, with the phase-adapted array explicitly nonliteral. Do not
   phrase it as literal residual mass.

With those repairs, the candidate supports exactly one route-scoped
obstruction and no affirmative target, parent, bridge, or exponent
promotion.

## 2. Exact statement and hypotheses audited

The exact domain needed for the candidate is

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M=M_L\asymp L^2,
\tag{173.S4}
\]

with

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d),
\qquad
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{173.S5}
\]

On every nonzero opened incidence, \(N=dm\asymp L^2\),
\(d,m\asymp L\), the opened weights and active-divisor multiplicities are
\(X^{O(\eta)}\), and all selectors, no-pair values, squarefree and
coprimality masks, both two-adic branches, profiles, floors, stars,
crossings, point values, endpoints, and zero-extension values are retained.

For an ordered even-gap opened pair the exact coordinates are

\[
 d'=d+2s,\qquad m'=m+v,\qquad
 r_s=dv+2s(m+v),\qquad v\in2\mathbb Z.
\tag{173.S6}
\]

The full link must therefore be written as

\[
 \Delta_{R,T}=2\Re
 \sum_{\substack{d>0\ {\rm odd},\ m\ge1\\
                  v\in2\mathbb Z,\ s\in\mathbb Z}}
 (-1)^s\beta_{R,T}(r_s)G_{d,m,v}(s),
\tag{173.S7}
\]

where \(G\) is zero unless \(d+2s>0\), \(m+v>0\), and both resulting
opened atoms lie on positive literal support. With this domain, the inverse
\(s=(d'-d)/2,\ v=m'-m\) proves opened-incidence multiplicity one and

\[
 d'm'-dm\equiv v\pmod2,\qquad
 \chi_4(d+2s)\chi_4(d)=(-1)^s.
\tag{173.S8}
\]

The odd--odd branch has \(v\) even. In the squarefree even--even branch,
writing \(m=2u,\ m'=2u'\) with \(u,u'\) odd gives \(4\mid v\) and
\(4\mid r_s\). A mixed product-parity pair cannot have even gap. These
claims in the candidate are GREEN once (173.S7) makes the domain explicit.

## 3. Proof and seam verification

### 3.1 Adjoint reindexing

Let \(DG(s)=G(s)-G(s+1)\) and
\(a_s=(-1)^s\beta(r_{s+1})\). Finite support and full-line zero
extension give

\[
 \sum_sa_sDG(s)=\sum_s(a_s-a_{s-1})G(s).
\]

Since

\[
 a_{s-1}=(-1)^{s-1}\beta(r_s)
        =-(-1)^s\beta(r_s),
\]

we have

\[
 a_s-a_{s-1}
 =(-1)^s\{\beta(r_{s+1})+\beta(r_s)\}.
\]

Taking one outer real part proves (173.S1). No selector, phase, mask,
point value, support birth, or support death is moved outside the exact
finite sum. Adding the commutator gives

\[
 \mathcal C_{R,T}+\mathcal R_{R,T}
 =2\Re\sum_s(-1)^s\beta(r_s)G(s)
 =\Delta_{R,T},
\]

which proves (173.S2). The candidate's adjoint sign and constants are
GREEN.

### 3.2 Whole-chain constants and short-correction sign

Put \(w_R(r)=(1-r/R)_+\mathbf1_{r>0}\). For the stopped chain
\(R_{j+1}=\min(2R_j,M_L)\), repetitions removed,

\[
 \sum_j\beta_{R_j,R_{j+1}}(r)
 =w_{M_L}(r)-w_{R_0}(r).
\tag{173.S9}
\]

For \(r\ge R_0\), (173.S9) is exactly the K26 weight. For
\(0<r<R_0\), it equals

\[
 r\left(\frac1{R_0}-\frac1{M_L}\right).
\]

Therefore the accepted identity is

\[
 \frac12\sum_j\Delta_{R_j,R_{j+1}}
 =T_{26}+B_{\rm short},
\qquad
 B_{\rm short}=
 \sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1{M_L}\right)A_r.
\tag{173.S10}
\]

Thus \(T_{26}=\frac12\sum_j\Delta_j-B_{\rm short}\), and substituting
(173.S2) gives exactly (173.S3). Cauchy's bound
\(|A_r|\le D_L\) yields

\[
 |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\]

The correction appears once, not once per link. The candidate's sign and
normalization are GREEN.

### 3.3 One-sided equivalence to K26

Equation (173.S3) is an equality between real quantities. Hence a
one-sided target bound for \(T_{26}\), together with the absolute paid-term
bounds, gives the same one-sided target bound for \(\sum_j\mathcal R_j\).
Conversely,

\[
 T_{26}=\frac12\sum_j\mathcal R_j
       +\frac12\sum_j\mathcal C_j-B_{\rm short},
\]

so a one-sided target bound for the whole-chain remainder gives K26.
Only the commutator and short correction are estimated absolutely. No
modulus is introduced around an individual link, so cross-link
cancellation remains available. The equivalence claim is GREEN; it must
not be rewritten as a claim that a linkwise bound is necessary.

### 3.4 \(L^3\) versus \(L^4\) power ledger

The bandpass is continuous at \(0,R,T\) and globally \(1/R\)-Lipschitz
(indeed \(1/T\)-Lipschitz). Since

\[
 r_{s+1}-r_s=2m'\asymp L,
\]

the commutator multiplier is \(O(L/R)\). If either adjacent bandpass
value is relevant, the corresponding physical gap lies in an interval of
length \(T+O(L)=O(R)\), because \(R\ge R_0\asymp L\). There are
\(O(RL^2)\) ordered physical pairs and only \(X^{O(\eta)}\) weighted
double openings per pair. Choosing \(\eta\) sufficiently small in terms
of the requested \(\varepsilon\) gives

\[
 |\mathcal C_{R,T}|
 \ll_\varepsilon (L/R)(RL^2)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\tag{173.S11}
\]

The \(O(\log L)\) chain is absorbed by epsilon rebudgeting. In contrast,
the adjacent sum in (173.S1) has no \(L/R\) factor. Its generic
positive/absolute closure has only

\[
 \ll_\varepsilon RL^2X^\varepsilon,
\tag{173.S12}
\]

which is \(L^4X^\varepsilon\) when \(R\asymp M_L\asymp L^2\).
Equation (173.S12) is an available upper scale. The abstract
phase-adapted test below shows that the difference operator alone cannot
improve that scale, but it is not literal residual mass. This distinction
must remain explicit in the candidate and any State Patch.

### 3.5 No-pair parity and phase-adapted controls

On a no-pair row all of whose odd prime factors are \(1\pmod4\), every
active character-bearing divisor is \(1\pmod4\). If both opened rows are
of this type, then \(d\equiv d'\equiv1\pmod4\), so

\[
 s=(d'-d)/2\equiv0\pmod2.
\]

Thus \(G^+(s)=0\) at odd sites. Each occupied even site contributes once
as a death and once as a birth in \(G(s)-G(s+1)\); after multiplication by
\((-1)^s\), the two contributions have the same sign and recombine to the
adjacent sum in (173.S1). This is a genuine allowed-support operator
control. It proves neither density nor a lower bound for the physical
literal scalar, and it has no target-safe complement.

For the abstract test \(G(s)=(-1)^sg(s)\), \(g(s)\ge0\), (173.S1)
becomes

\[
 \mathcal R_{R,T}
 =\sum_s\{\beta(r_s)+\beta(r_{s+1})\}g(s)\ge0.
\tag{173.S13}
\]

This correctly falsifies a coefficient-uniform claim that the formal
difference \(G(s)-G(s+1)\) itself saves \(L\). The test is nonliteral and
must not be cited as a lower bound for \(c_N^{\rm rem}\).

The two broad counterexamples in the initial blind report are likewise
false controls only after the repaired packet is imposed. Its dechirped
single-divisor example uses \(d=N,\ m=1\), contrary to \(d,m\asymp L\).
Its cancelling-opening example uses products outside the \(L^2\) shell and
an unbounded opened weight. Neither is a literal counterexample to K26 or
to the repaired coefficient class. Both remain valid warnings against
erasing the factor-scale and opened-weight hypotheses.

## 4. First doubtful or unproved step

After (173.S1)--(173.S3), the first open estimate is exactly the complete
literal K26 shifted-convolution bound, equivalently the complete signed
whole-chain adjacent-sum remainder. Selector, arithmetic-mask, profile,
endpoint, zero-extension, and phase jumps can all be order one. In
particular,

\[
 J\{\sqrt{N_s'+2m'}-\sqrt{N_s'}\}\asymp J
\]

as a real quantity, but no uniform distance from an integer follows. A
second Abel transfer simply returns (173.S1). No genuine signed
actual-symbol theorem is proved.

The obstruction must therefore be stated narrowly: it covers the displayed
tangent-character first-difference placement, its adjoint transfer, and a
coefficient-uniform positive/absolute variation closure. It does not rule
out another tangent mechanism, a nonlocal or cross-link signed theorem, a
coefficient-sensitive positive theorem proved after a literal-symbol gain,
or K26 itself.

## 5. Required controls and outcomes

| Seam or control | Outcome |
|---|---|
| adjoint reindexing identity | **GREEN**: the multiplier is the adjacent sum in (173.S1) |
| finite-support endpoints | **GREEN**: full-line zero extension retains all births and deaths |
| complete-link tangent domain | **REPAIR**: write \(v\in2\mathbb Z\) and the positive odd-\(d\) domain in the displayed sum |
| exact endpoint scale | **REPAIR**: write \(M=M_L\asymp L^2\) |
| factor \(2\) in the link | **GREEN** |
| short-correction sign | **GREEN**: \(T_{26}=\frac12\sum\Delta-B_{\rm short}\) |
| short correction paid once | **GREEN** |
| one-sided K26 equivalence | **GREEN** in both directions using absolute bounds only for the paid terms |
| cross-link cancellation | **RETAINED**: no linkwise necessity is claimed |
| commutator power | **GREEN**: \(L^3X^\varepsilon\) after epsilon rebudgeting |
| remainder positive capacity | **REPAIR WORDING**: \(L^4X^\varepsilon\) is an available envelope scale, not literal mass |
| all-\(1\pmod4\) no-pair support | **GREEN** as an allowed-support operator control only |
| phase-adapted control | **GREEN** as a nonliteral coefficient-uniform falsifier only |
| initial blind single-divisor example | **NONLITERAL FALSE CONTROL**: violates \(d,m\asymp L\) |
| initial blind cancelling-opening example | **NONLITERAL FALSE CONTROL**: violates scale and bounded opened weight |
| large real phase increment | **NO MODULO-ONE SAVING** |
| exact no-go scope | **GREEN after narrow wording**: displayed operator/adjoint/positive closure only |
| standalone strict commutator sector | **NO PROMOTION**: the commutator is an algebraic addend and its complement is the open remainder |
| K26 and residual scalar | **OPEN** |
| hard TOP, BAL, UNBAL, M9--M2, M1 routes, M9, bridges | **NO CHANGE** |
| global exponents | **NO CHANGE** |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The review used exactly:

1. protocol.md;
2. state/proof_obligations.yml at the stated graph hash;
3. state/active_campaign.yml;
4. the reviewed Round-173 candidate;
5. the repaired Round-173 statement-only packet;
6. the Round-173 discovery and hostile reports;
7. the initial blind report only for its two erased-structure false
   controls;
8. proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
9. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md; and
10. proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md.

For a minimal graph dependency list, the Round-164 transport node is
already an ancestor of the Round-165 parity/K26 reduction and need not be
added again merely for provenance. The candidate may list all three
kernels as evidence, but the State Patch should distinguish evidence from
minimal mathematical dependency edges and avoid redundant reverse edges.

## 7. Exact repairs and recommended state effect

Apply the following local repairs to the candidate before promotion:

1. In Section 2 replace \(M\asymp L^2\) by
   \(M=M_L\asymp L^2\) and include the accepted energy bound needed for
   \(B_{\rm short}\).
2. Replace the unrestricted displayed link sum by (173.S7), explicitly
   restricting \(d>0\) odd, \(m\ge1\), \(v\in2\mathbb Z\), and
   \(s\in\mathbb Z\), and state that \(G\) is zero unless both atoms are
   positive literal incidences.
3. Replace “Taking positive variation gives \(RL^2X^\varepsilon\)” by
   “The coefficient-uniform positive/absolute closure has available upper
   scale \(RL^2X^\varepsilon\), reaching \(L^4X^\varepsilon\) at a
   maximal link; the phase-adapted test is nonliteral and proves no
   physical lower bound.”
4. State the no-go scope as the exact displayed first-difference placement,
   its adjoint/second-Abel self-return, and positivity before any
   actual-symbol gain. Explicitly retain cross-link cancellation and a new
   literal coefficient-sensitive theorem as possible.
5. Name the only two downstream owner interfaces explicitly:
   M9-M2-top-endpoint-density-discrepancy-energy and
   M9-M2-top-endpoint-signed-cone. Add the new obstruction only as
   inconclusive route evidence/dependency with no status change, no
   implication edge, and no blocker.
6. Restore the missing inline LaTeX delimiters throughout candidate
   Sections 2--5. This is typographical, but the durable statement should
   not leave mathematical hypotheses as bare parentheses.

After these repairs, create at most one proved-internal node:

M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction.

Give it no implication edge and no blocker. Do **not** create a standalone
target-safe commutator sector: \(\mathcal C\) is not a disjoint physical
incidence sector, and its exact complement
\(\mathcal R=\Delta-\mathcal C\) is the original open K26 problem modulo
paid terms. Keep K26, the residual scalar, every other hard-TOP channel,
hard TOP, BAL, UNBAL, M9--M2, both M1 routes, endpoint assembly, M9, both
bridges, the quarter theorem, and both exponent ledgers unchanged.


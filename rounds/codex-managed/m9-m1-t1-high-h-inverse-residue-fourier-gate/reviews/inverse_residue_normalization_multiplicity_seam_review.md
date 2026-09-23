# 1. Result and verdict

**Verdict: GREEN for the candidate, with three non-blocking discovery-report
precision repairs listed below.**  The candidate's claims (187.K1)--(187.K25)
are algebraically and combinatorially correct under the literal imported
Round-185 hypotheses.  In particular:

- the Fourier sign and normalization are correct;
- the separate \(U=1\) convention is neither lost nor double-counted;
- the exact-conductor partition is disjoint and exhaustive;
- the changes \(u=gU\) and \(n=gh\) preserve multiplicity one;
- the \(O(UL)\) atom count at fixed \((\kappa,u,U)\) is valid for both
  orientations;
- the literal selectors, deletions, endpoints, conjugations, phases, and zero
  extensions remain inside the unchanged amplitudes; and
- every stated \(L,Y,\kappa,g,U,q\) power follows from the accepted support
  count and pointwise endpoint bound, without any hidden regularity of the
  literal coefficient.

Thus promotion is justified only for the strict target-safe Fourier sector and
its exact complement.  The full one-sided high-height estimate (187.K8) is not
proved and remains the first unresolved relation.

The discovery report has three local precision defects, none of which survives
in the candidate:

1. report (2.19), lines 303--309, must include \(U>1\) in the displayed
   codomain of the asserted bijection;
2. report (3.5), lines 470--473, requires \(a\not\equiv0\pmod U\); its actual
   application has \(a=\bar v h\), a unit, so it is valid; and
3. report (3.20), lines 733--737, must include \(q_U(k)>Q\) in the summation
   defining the retained high-mode mass.  Candidate (187.K25) already contains
   this condition, and the two near-half residues prove the corrected display.

# 2. Exact reviewed claim and hypotheses

Fix \(B>0\), real \(X\ge2\), one literal middle or lower hard-M1 residual
shell \(L\ge2\), \(\sigma\in\{+1,-1\}\),

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor\ge1,
\]

and a nonempty block \(Y<h\le2Y\) with \(Y>H_B\).  The reviewed carrier is
exactly (K185.27) and (K185.30)--(K185.35):

\[
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\]

For each orientation \(\omega\), the canonical anchor and positive affine
index set are retained, and

\[
 A_{\mathfrak f,\omega}^{\sigma}
 =\sum_{t\in I_{\mathfrak f,\omega}}
   (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).
\]

The symbol \(B\) is not replaced by a regularized weight.  It still contains
both literal \(\lambda\)-factors and hence the selector, squarefree and
allocation-coprimality masks, shell/cone/profile/floor/star/half-weight/hard-
sample/crossing predicates, endpoint order, conjugation, Fejer factor,
square-root phase, sign, and zero extension.  The only imported quantitative
facts used in the proof are the accepted pointwise endpoint bound, the literal
support facts \(u,v\asymp L/\kappa\), and the accepted \(O(\kappa)\) number of
live sites on one primitive affine row.  Deletions are used only to reduce
positive counts.

Under these hypotheses the candidate asserts the exact decomposition
(187.K1)--(187.K5), the target-safe estimate (187.K6), the positive remainder
bound (187.K7), and the equivalence of the original target to the still-open
one-sided relation (187.K8).  It further asserts the normalization and
conductor identities (187.K9)--(187.K12), the count and power formulas
(187.K13)--(187.K19), the centered-conductor identities
(187.K20)--(187.K23), and the retained high-mode energy lower bounds
(187.K24)--(187.K25).

# 3. Derivation and checks

## 3.1 Anchors, orientations, and multiplicity

For \(U>1\), put \(a=[\bar v h]_U\).  The two anchors satisfy the primitive
equations exactly:

\[
 S_{0,+}v-Uw_{0,+}=h,
 \qquad Uw_{0,-}-vS_{0,-}=h,
\]

with \(S_{0,+}=a\) and \(S_{0,-}=[-a]_U\).  The affine formulas then list
every positive solution once.  Since \(U\) is odd,

\[
 (-1)^{S_{t,\omega}}
 =(-1)^{S_{0,\omega}+Ut}
 =(-1)^{S_{0,\omega}}(-1)^t,
\]

so the sign extracted from the literal character product is exactly the sign
used in \(A_{\mathfrak f,\omega}^{\sigma}\).

For \(U=1\), the retained anchors give

\[
 I_{\mathfrak f,+}=\{t\ge1:vt>h\},\qquad
 I_{\mathfrak f,-}=\{t\ge1\}.
\]

Both have \(S_{0,\omega}=0\), hence their outer anchor sign is \(+1\), exactly
as in (187.K2).  The literal zero extension, not an inferred compactness or
smoothness property, makes these sums finite.

The coordinate change is exact.  In the form used for divisor summation,

\[
 (g,U,h)\longleftrightarrow(u,U,h),\qquad
 u=gU,\quad U\mid u,\quad g=u/U,\quad(U,h)=1.
\]

In the equivalent joint form,

\[
 (u,n)=(gU,gh),\qquad
 g=(u,n),\quad U={u\over(u,n)},\quad h={n\over(u,n)}.
\]

Thus there is no extra gcd multiplicity.  The transformed \(U>1\) domain is

\[
 \kappa,u,U,h,v>0,\quad U>1,\quad \kappa,u,U\text{ odd},\quad
 U\mid u,\quad(u,v)=1,\quad(U,h)=1,\quad
 0<2\kappa(u/U)h<R_0.
\]

This also identifies the one omission in discovery-report (2.19): without the
displayed condition \(U>1\), its codomain contains tuples that cannot arise
from the stated source sector.  The candidate's sums themselves retain
\(U>1\), so candidate multiplicity is unaffected.

## 3.2 Fourier normalization, signs, and exact-conductor partition

With \(e(x)=e^{2\pi ix}\), oddness of \(U\) gives

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={1-\{-e(-k/U)\}^{U}\over1+e(-k/U)}
 ={2\over1+e(-k/U)}.
\]

Therefore inversion has the positive phase

\[
 E_U(a)=\sum_{k\bmod U}c_U(k)e(ka/U),\qquad
 c_U(k)={2\over U\{1+e(-k/U)\}},\qquad c_U(0)={1\over U}.
\]

Also

\[
 c_U(k)={e(k/(2U))\over U\cos(\pi k/U)},
 \qquad \sum_k|c_U(k)|\ll\log(2U),
 \qquad \sum_k|c_U(k)|^2=1.
\]

The final equality is Parseval with the normalization just displayed.  Because
\((U,hv)=1\), \(a=\bar v h\) is a nonzero unit, so

\[
 (-1)^{S_{0,+}}=E_U(a),\qquad
 (-1)^{S_{0,-}}=E_U(-a),\qquad E_U(-a)=-E_U(a).
\]

This verifies both orientation signs.  It also shows why discovery-report
(3.5) needs the local hypothesis \(a\ne0\pmod U\); that hypothesis holds here.

For every \(k\bmod U\), let \(q=U/(k,U)\).  There is a unique

\[
 q\mid U,\qquad k=(U/q)a,\qquad a\in\mathbb U(q),
\]

with the special pair \((q,a)=(1,0)\) for \(k=0\).  Direct substitution gives

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e(\epsilon_\omega k\bar v h/U)
 =e(\epsilon_\omega a\bar v h/q).
\]

Hence (187.K3) is exactly the union of conductors \(q\le Q\), including the
mean.  In the disjoint complement \(q>Q\), (187.K4) consists of all modes with
\(U\le4Q\) plus, for \(U>4Q\), precisely \(0<|k|_U\le Q\).  Formula
(187.K5) is the remaining set \(U>4Q\), \(q>Q\), \(|k|_U>Q\).  Since
\(Q\ge1\), \(k=0\) occurs only in the \(q=1\) part of (187.K3).  Thus
(187.K1) is an exact, disjoint identity with one outer real part.

## 3.3 Atom count and restored powers

At fixed \((\kappa,g,h,U)\), literal support gives

\[
 \#\{v\}\ll L/\kappa,\qquad
 \#\{\text{live }t\text{ on one }v\text{-row}\ll\kappa,
\]

and the pointwise endpoint bound gives, after epsilon rebudgeting,

\[
 \sum_{\omega,v,t}|B_{\mathfrak f,\omega}^{\sigma}(t)|
 \ll_\varepsilon LX^\varepsilon.
\]

The support also gives

\[
 U\ll {L\over\kappa g},\qquad
 \kappa g<{R_0\over2h}\ll {L\over h},
\]

and elementary divisor counting yields

\[
 \sum_{Y<h\le2Y}\sum_{\kappa g<R_0/(2h)}1
 \ll L\log(2L).
\]

These formulas prove the \(U=1\) cost \(O_\varepsilon(L^2X^\varepsilon)\)
and, with the factor \(1/U\), the independent zero-mode cost at the same
scale.

For the stronger exact-conductor ledger, a live atom has

\[
 u=gU\asymp L/\kappa,\qquad v\asymp L/\kappa,
 \qquad n=gh\ll L/\kappa.
\]

Since \(g=u/U\), this implies \(h=n/g\ll U\).  Thus, at fixed
\((\kappa,u,U)\), there are \(O(U)\) possible heights,
\(O(L/\kappa)\) possible \(v\)'s, and \(O(\kappa)\) live affine sites per
row.  Including both orientations changes only the absolute constant, so the
total is

\[
 O(U)\,O(L/\kappa)\,O(\kappa)=O(UL)
\]

literal atoms.  No equidistribution, continuity, or bounded-variation claim is
used.

At exact conductor \(q\),

\[
 {q\over U}\sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll {q\over U}\log(2q).
\]

Multiplication by \(O(UL)\) gives
\(O_\varepsilon(Lq\log(2q)X^\varepsilon)\) at fixed
\((\kappa,u,U)\).  Since \(q\mid U\mid u\),

\[
 \begin{aligned}
 |\mathscr P_{Y,\le Q}^{\sigma}|
 &\ll_\varepsilon LQ\log(2Q)X^\varepsilon
   \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\varepsilon QL^2\{\log(2LQ)\}^{O(1)}X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon.
 \end{aligned}
\]

For \(U\le4Q\), the full modulus mass is \(O(\log(2U))\).  For
\(U>4Q\),

\[
 \sum_{0<|k|_U\le Q}|c_U(k)|\ll Q/U.
\]

Summing first in \(U\) and then using the height-product count proves the
remaining target-safe term in (187.K6).  Finally the full Fourier mass and
\(U\ll L/(\kappa g)\) give

\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll_\varepsilon L^2\log(2L)X^\varepsilon
 \sum_{Y<h\le2Y}\sum_{\kappa g\ll L/h}{1\over\kappa g}
 \ll_\varepsilon YL^2X^\varepsilon.
\]

This proves (187.K7), not (187.K8), and displays exactly where the factor
\(Y\) survives.

## 3.4 Centering and retained high modes

For a unit \(b\pmod q\), changing \(a\) to \(-a\) gives

\[
 c_q(a)+c_q(-a)=2/q,
\]

so the Ramanujan sum over units yields

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
\]

Grouping the exact Fourier inversion by conductor gives

\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b).
\]

After writing \(K_q=\mu(q)/q+K_q^\circ\), the scalar terms in the two
orientations cancel because \(\sum_{q\mid U}\mu(q)=0\) for \(U>1\).  This is
exactly (187.K22).  If \(U=p\) is prime, the \(q=1,p\) identity gives
\(K_p^\circ(b)=E_p(b)\), proving (187.K23) and the claimed conductor
self-return.

For odd \(U>4Q\), the residues \(k=(U\pm1)/2\) satisfy

\[
 (k,U)=1,\qquad q_U(k)=U>Q,\qquad |k|_U=(U-1)/2>Q,
\]

and

\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\ge {2\over\pi}.
\]

Their two squares give the lower bound \(8/\pi^2\) in (187.K25).  This
condition is correctly present in the candidate; it is the missing condition
in discovery-report (3.20).

## 3.5 Claim-by-claim identity audit

| Claim | Outcome | Exact check |
|---|---|---|
| (187.K1) | PASS | Disjoint union of \(U=1\), \(q\le Q\), safe \(q>Q\), and the exact remainder, with one outer real part. |
| (187.K2) | PASS | \(S_{0,+}=S_{0,-}=0\) for \(U=1\); no anchor sign is omitted. |
| (187.K3) | PASS | Exact-conductor grouping, including \((q,a)=(1,0)\) and coefficient \(1/U\). |
| (187.K4) | PASS | Exactly the \(q>Q\) small-modulus or ordinary-low-residue packet. |
| (187.K5) | PASS | Exact complementary mode set; both orientations and literal \(A\)'s remain joint. |
| (187.K6) | PASS | Follows from the \(U=1\), \(O(UL)\), exact-conductor, and ordinary-low-residue ledgers. |
| (187.K7) | PASS | Positive recombination leaves exactly the factor \(Y\). |
| (187.K8) | PASS as an explicitly open equivalence | Safe terms are absolutely target-sized; no proof of the displayed bound is claimed. |
| (187.K9) | PASS | Odd-length geometric sum has numerator \(2\). |
| (187.K10) | PASS | Inversion sign is \(+\); \(c_U(0)=1/U\). |
| (187.K11) | PASS | Half-angle formula, logarithmic \(\ell^1\) mass, and Parseval mass \(1\). |
| (187.K12) | PASS | Unique reduced conductor and exact coefficient/phase scaling. |
| (187.K13) | PASS | \(O(L/\kappa)\) rows times \(O(\kappa)\) live sites, for both orientations. |
| (187.K14) | PASS | Directly from \(u=gU\asymp L/\kappa\) and \(2\kappa gh<R_0\). |
| (187.K15) | PASS | Dyadic \(h\)-sum of the divisor count for \(\kappa g\ll L/h\). |
| (187.K16) | PASS | Exact-conductor \(\ell^1\) mass is \(O((q/U)\log(2q))\). |
| (187.K17) | PASS | (187.K16) times the \(O(UL)\) atom count. |
| (187.K18) | PASS | Nested divisors \(q\mid U\mid u\) cost at most \(\tau(u)^2\); all \(Q\) and log factors are polylogarithmic. |
| (187.K19) | PASS | For \(|k|_U\le Q<U/4\), \(|\cos(\pi k/U)|\ge2^{-1/2}\). |
| (187.K20) | PASS | Definitions are well-posed for the unit anchor residues used later. |
| (187.K21) | PASS | Exact conductor grouping plus the unit Ramanujan sum \(\mu(q)\). |
| (187.K22) | PASS | The apparent scalar term is exactly zero by \(\sum_{q\mid U}\mu(q)=0\). |
| (187.K23) | PASS | For prime \(p\), the sole nontrivial centered conductor equals \(E_p\). |
| (187.K24) | PASS | Exact magnitude at the two near-half residues and the bound \(\sin x\le x\). |
| (187.K25) | PASS | Both near-half modes lie in the stated retained set and contribute \(8/\pi^2\). |

# 4. First doubtful or unproved step

There is no doubtful step inside the promoted strict sector after the checks
above.  The first unproved mathematical relation is exactly (187.K8):

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

The available dependencies give no variation, residue equidistribution,
translation invariance, orientation equality, or Fourier-energy saving for the
actual deleted endpoint amplitude in \((h,v,t,k)\).  The positive estimate is
larger by \(Y\), and (187.K24)--(187.K25) show that deleting the safe modes does
not make the retained Fourier coefficient vector small.  Any proof beyond this
point needs a new jointly signed property of the literal coefficient before a
positive norm or positive recombination.

The three discovery-report issues listed in Section 1 are documentation
precision defects, not gaps in (187.K1)--(187.K25).  Their exact repairs should
be made before those report displays are quoted independently.

# 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Exact anchor substitution | PASS.  Both \(U>1\) anchors satisfy their primitive equations; the \(U=1\) anchors give the stated positive index sets. |
| Orientation/parity control | PASS.  The plus argument is \(+\bar vh\), the minus argument is \(-\bar vh\), and odd \(U\) produces exactly one factor \((-1)^t\). |
| Conductor partition | PASS.  Every \(k\bmod U\) has one and only one \((q,a)\), including the zero mode. |
| Multiplicity inverse | PASS.  \(g=u/U\) in \((u,U,h)\) coordinates and \(g=(u,n)\), \(U=u/g\), \(h=n/g\) in \((u,n)\) coordinates. |
| Literal deletion control | PASS.  Every deletion remains inside \(B\) and is used only monotonically in upper counts; no support regularity is inferred. |
| Both orientations | PASS.  They are counted with an absolute constant only in the strict packet and remain under the single outer real part in the exact remainder. |
| Power ledger | PASS.  \(O(UL)\times O((q/U)\log q)=O(Lq\log q)\); nested divisor summation proves the \(q\le Q\) packet; the remainder retains exactly \(Y\). |
| False unsigned/adversarial mechanism | PASS as a boundary control.  The gain uses the \(\chi_4\)-induced anchor mean \(1/U\); an unsigned anchor has mean \(1\), and no arbitrary-coefficient theorem is inferred. |
| Bounded arithmetic diagnostic | PASS, diagnostic only.  Using Python 3.14.5 double precision, all odd \(1\le U\le101\) and every residue were checked for inversion, Parseval, and conductor scaling; all 2,106 unit-\(b\) centering cases were checked.  Maximum absolute floating error was \(7.82\times10^{-14}\).  Exact integer anchor tests covered 241,864 unit \((v,h)\) cases with zero failures, and 49,400 mode classifications over \(1\le Q\le19\) had zero partition failures.  This computation diagnoses finite algebra only and is not theorem evidence. |

# 6. Dependencies and hashes

The candidate was hashed before its content was reviewed.  A final rehash was
identical.

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a` |
| `state/active_campaign.yml` | `aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3` |
| `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md` | `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md` | `528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/literal_height_fourier_attack.md` | `319facc926335e039cf6569bef8d49b1cac4ac09188adf888c5e22c5a7e6bc64` |

No external theorem, source card, sibling review, or hidden coefficient
regularity was used.  The direct theorem dependencies remain
`M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction` and
`Divisor-bound-elementary`.

# 7. Recommended state effect

**Promote**
`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction` as
`proved_internal`, with exactly the strict target-safe packet (187.K6), exact
decomposition (187.K1)--(187.K5), exact complement (187.K5), capacity bound
(187.K7), and mechanism controls (187.K20)--(187.K25).  Record it only as an
inconclusive dependency/evidence item for the still-open hard-M1 small-\(t\)
residual owner, under the Round-187 exit label
`strict_high_h_inverse_residue_fourier_sector`.

**Retain open** (187.K8), the complete high-height block, the full original
\(t=1\) residual, every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete hard and smooth M1 parents, GAR, all M2
parents, endpoint uniformity, M9, both bridges, the Gauss-circle target, and
every exponent claim.

Before the discovery report is quoted as exact supporting evidence, apply the
three report-only repairs in Section 1.  They do not require a candidate change
or a repeat of this normalization/multiplicity review.  This reviewer makes no
graph, synthesis, candidate, validation-matrix, or proof-draft edit.

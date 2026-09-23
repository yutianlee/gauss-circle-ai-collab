# Independent literal-restoration and owner-scope review

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Round: 171
- Role: fresh independent seam reviewer
- Starting graph SHA-256: `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Allocation: 100% analytic/algebraic, 0% numerical

## 1. Result

**Result: the route-specific commutator/ramp obstruction is mathematically
sound after a narrow statement repair; the physical remainder and every
downstream estimate remain open.**

The three reports and two earlier reviews support promotion of one
`proved_internal` **method obstruction**, but not promotion of
`M9-M2-balanced-double-far-oscillatory-remainder`.  The exact content is:

1. the ordered-pair chart to \((h,k,p,q)\) is multiplicity one, with the
   full parity and support conditions retained;
2. the genuine axes \(p=0\) and \(q=0\) are present but are each absolutely
   \(O_\varepsilon(L^3X^\varepsilon)\);
3. the normalized coordinate multiplier commutators are just commuting
   shifts;
4. the parity-compatible unnormalized commutator is
   \(8(y-x)T_sT_q^2\); a fixed-width singular strip is target-safe, while
   division off it cancels the displayed multiplier and returns a shift
   tautology rather than an \(L^{-1}\) gain;
5. the correct real endpoint-swap summation-by-parts formula has one
   surviving \((++)\) complement, whose available coefficient-blind ledger
   remains \(L^4X^\varepsilon\); and
6. every coefficient-independent first-difference primitive for the
   unweighted \(q\)-sum varies by \(\asymp L\) on a balanced fibre.  Thus the
   exact mixed Abel identity has a length-\(L\) ramp, and the presently
   available positive boundary ledger is \(L^4X^\varepsilon\), not
   \(L^3X^\varepsilon\).

This proves a no-go only for the audited local coordinate-generated
normalized/unnormalized multiplier commutators, independent endpoint swaps,
and coefficient-independent two-step Abel closure followed by positive
variation.  It is not a physical lower bound, a disproof of the target, or a
classification of all weighted/nonlocal actual-symbol commutators.

Three exact presentation repairs are required in the conductor kernel:

- state the mod-4 oddness condition in the nonaxial defect inverse;
- define zero extension before evaluating an out-of-support square root; and
- use the bilinear coefficient/phase endpoint-swap identity below, rather
  than treating the projection of the complete real summand as the scalar
  commutator decomposition.

## 2. Exact statement and hypotheses

Fix one persistent critical \(j=1\) literal balanced block, with
\(L\asymp X^{1/6}\), \(K\asymp L\), and real zero-extended coefficient

\[
 a(h,k)=\chi_4(h)\eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k).
\]

All Vaaler tapers, both slanted profiles, floors, stars, crossings, clipped
endpoints, signs, aliases, and the fixed physical-block label remain inside
\(A_B\).  The phase uses the exact real centre \(R=\sqrt X\).  Put

\[
 p=h'-h,\qquad q=k'-k,
\]

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

and retain the strict mask
\(G=1_{|\Delta|>L}1_{|\rho|>L}\).  The target is the single assembled
fixed-block scalar

\[
 \mathcal R_B^{\rm osc}
 =\sum G\,a(h,k)a(h',k')
 \left[e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\tag{171.O1}
\]

The exact chart consists only of tuples for which both diagonal atoms are in
the positive literal support.  Its inverse is

\[
 (h,k,p,q)\longmapsto(h,k,h+p,k+q),
\]

so its ordered multiplicity is one.  On character support \(p=2s\), and

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\tag{171.O2}
\]

For the nonaxial defect chart, with
\(u=\Delta+\rho\), \(v=\Delta-\rho\),

\[
 h=\frac12\left(\frac uq-p\right),\qquad
 k=\frac12\left(\frac vp-q\right).
\tag{171.O3}
\]

Besides \(q\mid u\), \(p\mid v\), positivity, and both literal support
tests, an exact character-support statement must retain

\[
 p\in2\mathbb Z,\qquad \frac uq-p\equiv2\pmod4,
 \qquad \frac vp-q\equiv0\pmod2.
\tag{171.O4}
\]

If \(u,v\) are introduced independently rather than as \(\Delta\pm\rho\),
also retain \(u\equiv v\pmod2\).  The no-go below is scoped only to this
literal critical child and to the listed operator placements.

## 3. Proof and seam verification

### 3.1 Coordinates, parity, zero extension, and axes

Direct expansion gives

\[
 \Delta+\rho=q(2h+p)=q(h+h'),\qquad
 \Delta-\rho=p(2k+q)=p(k+k').
\tag{171.O5}
\]

Equations (171.O3)--(171.O4) verify the inverse and the missing mod-4
condition.  Formula (171.O2) follows from
\(\chi_4(n+2)=-\chi_4(n)\) for odd \(n\), and is constant on a fixed-
\(p\) fibre.  It gives no inner-\(h\) cancellation.

For translation formulas, the summand must be defined piecewise: it is zero
unless the shifted atom is in the positive literal support, and only then is
its square-root phase evaluated.  With that convention, every support entry
and exit is a genuine zero-extension difference; no undefined square root is
multiplied formally by zero.

On \(p=0\), \(\Delta=\rho=hq\); on \(q=0\),
\(\Delta=pk\), \(\rho=-pk\).  Both sectors can be double-far.  Bounded
literal weights and \(|e(\cdot)-1|\le2\) give

\[
 \sum_{p=0}|\cdots|\ll LK^2X^\varepsilon
 \ll L^3X^\varepsilon,
 \qquad
 \sum_{q=0}|\cdots|\ll L^2KX^\varepsilon
 \ll L^3X^\varepsilon.
\tag{171.O6}
\]

Their intersection is excluded by the strict far gates.  Thus the axes are
target-safe strict slices, not deleted divisibility exceptions and not an
\(L^4\) obstruction.

### 3.2 Normalized and unnormalized multiplier commutators

Use the discovery report's forward shifts

\[
 T_sf(s,q)=f(s+1,q),\qquad T_qf(s,q)=f(s,q+1),
 \qquad D_s=T_s-I,\quad D_q=T_q-I.
\]

Set

\[
 x=h+h'=2h+2s,\qquad y=k+k'=2k+q,
\]

\[
 U=\Delta+\rho=qx,qquad V=\Delta-\rho=2sy.
\]

Then

\[
 [D_q,M_U]=xT_q,\qquad [D_s,M_V]=2yT_s,
\]

so after division by the positive side sums the two operators are exactly
\(T_q\) and \(T_s\), whose commutator is zero.  The cross-normalizations
similarly return shifts away from the already paid axes.  Hence the apparent
side-sum denominators do not supply \(L^{-1}\).

Unnormalized commutators must nevertheless be retained.  With
\(\widehat T_q=T_q^2\), \(\widehat D_q=\widehat T_q-I\), define

\[
 \mathfrak P=[D_s,M_V]=2yT_s,\qquad
 \mathfrak Q=[\widehat D_q,M_U]=2x\widehat T_q.
\]

Since \(T_sx=x+2\) and \(\widehat T_qy=y+2\),

\[
 \boxed{[\mathfrak P,\mathfrak Q]
 =8(y-x)T_sT_q^2.}
\tag{171.O7}
\]

For fixed integer \(t=y-x\), three coordinates determine the fourth, so
the literal support has \(O(L^3)\) ordered quadruples.  Therefore
\(|y-x|\le C\) has absolute mass
\(O_C(L^3X^\varepsilon)\) for fixed \(C\).  Off this strip,

\[
 \frac{[\mathfrak P,\mathfrak Q]}{8(y-x)}=T_sT_q^2.
\]

Subtracting the identity and reindexing against \((-1)^s\) merely returns
the original scalar through

\[
 \sum(-1)^s(T_sT_q^2-I)F=-2\sum(-1)^sF.
\tag{171.O8}
\]

Thus the multiplier in (171.O7) exactly repays its divisor.  The ordinary
step-one variants and the backward-shift commutators in the ramp review give
the same conclusion with different affine singular lines: they are nonzero
Weyl identities, not a hidden inverse power.  The promoted no-go must not say
that *all* coordinate-generated commutators vanish.

### 3.3 Correct actual-real endpoint-swap decomposition

Let

\[
 a_{ij}=a(h+ip,k+jq),\qquad
 z_{ij}=e\!\left(R\sqrt{(h+ip)(k+jq)}\right),
\]

on a global finite ambient domain, with coefficients zero extended.  Put
\(W=a_{00}a_{11}\) and \(H=z_{00}\overline{z_{11}}-1\).  The independent
endpoint swaps \(\tau_h,\tau_k\) commute and preserve the strict gate.  For
\(P_{\epsilon\eta}=\frac14(I+\epsilon\tau_h)(I+\eta\tau_k)\), reality of
\(a\) gives

\[
 P_{+-}W=P_{-+}W=0,
\]

\[
 P_{++}W=\frac12(a_{00}a_{11}+a_{10}a_{01}),\qquad
 P_{--}W=\frac12(a_{00}a_{11}-a_{10}a_{01}),
\]

and

\[
 P_{++}H=-\frac14\bigl(|z_{00}-z_{11}|^2
 +|z_{01}-z_{10}|^2\bigr),\qquad
 P_{--}H=\frac14D_hD_kH.
\]

Self-adjointness of the swaps for the bilinear gate pairing gives the exact
scalar identity

\[
 \boxed{
 \langle W,H\rangle_G
 =\langle P_{++}W,P_{++}H\rangle_G
 +\frac1{16}\langle D_hD_kW,D_hD_kH\rangle_G.}
\tag{171.O9}
\]

Global zero extension absorbs cross-corner support failures; they are zeros
in the projected coefficient, not a separate unavoidable support-crossing
sum.  Formula (171.O9), rather than a projection of the already multiplied
complete summand, is the relevant summation-by-parts decomposition.  If one
projects the complete real summand itself, every non-\((++)\) projection has
zero full aggregate by permutation.  These two statements must not be
conflated.

The \((++)\) term in (171.O9) is not algebraically zero.  Its available
coefficient-blind positive ledger is still \(L^4X^\varepsilon\).  For the
nonnegative erased-structure shadow, \(P_{++}W\ge0\) and
\(P_{++}H\le0\), showing why a positive projection estimate cannot create
the missing factor.  This is a false-control capacity, not a lower bound for
the literal signed coefficient.

### 3.4 Mixed summation by parts and the forced ramp

After extracting (171.O2), let \(F_{h,k}(s,q)\) be the complete piecewise
zero-extended literal summand without \((-1)^s\).  Finite reindexing gives

\[
 \sum_s(-1)^sD_sF=-2\sum_s(-1)^sF,
\]

and, for any real \(q_0\),

\[
 \sum_qG(q)=-\sum_q(q-q_0)D_qG(q).
\]

Consequently

\[
 \boxed{
 \mathcal R_B^{\rm osc}
 =\frac12\sum_{h,k,s,q}(-1)^s(q-q_0)D_sD_qF_{h,k}(s,q).}
\tag{171.O10}
\]

Both the sign and the factor \(1/2\) are correct.  More generally, if an
unweighted sum on an interval of \(N\) lattice points is represented
coefficientwise by first differences, comparison on point masses forces
\(c(r)-c(r+1)=1\).  Hence \(\max|c|\ge N/2\).  Balanced interior
\(q\)-runs have \(N\asymp L\), and splitting a run only transfers this
variation to new endpoints.

The exact four-corner product rule exposes support, \(\Delta\)-gate, and
\(\rho\)-gate faces.  A one-step gate change places an old or new endpoint
in an accepted width-\(O(L)\) corridor, whose unweighted mass is
\(O_\varepsilon(L^3X^\varepsilon)\).  A one-coordinate literal support
face also has at most three free length-\(L\) variables.  Multiplication by
the forced primitive therefore restores an **available positive capacity**
of \(L^4X^\varepsilon\).  This is not an assertion that the actual weighted
face has an \(L^4\) lower bound; it proves that the supplied positive owners
do not close (171.O10).  The rectangular phase-adapted test in the hostile
report realizes the coefficient-uniform ramp capacity.

In the common interior, the mixed difference still contains an
undifferenced literal coefficient multiplying a four-corner exponential
difference of order at most, but not uniformly smaller than, one.  The gcd
factor has no pointwise \(L^{-1}\) difference.  Thus neither the bulk nor
the complement has a certified pre-norm factor-\(L\) saving.

### 3.5 Fixed-\(Q\) and literal-restoration seam

Both low-gcd factors and both slanted symbols remain at the two diagonal
atoms throughout the coordinate identities.  Floors, stars, crossings,
strict inequalities, endpoints, and \(R=\sqrt X\) remain at their exact
corners.  If the second gcd mask is opened, the \((d,\mu,J)\) progressions,
\(\gamma_d\), lifts, and amplitudes remain corner-dependent and may not be
merged.

The accepted fixed-\(Q\) formulas

\[
 \rho=hk'\frac{c^2-1}{c^2},\qquad
 \Delta=hk\frac{A^2-c^2}{c^2}
\tag{171.O11}
\]

still admit double-far rulings (for \(A=1\), \(\Delta=-\rho\)).  The
phase-free theorem subtracts only the assembled scalar \(M_B^{(0)}\); it
does not delete these atoms.  A \(p\)- or \(q\)-difference need not preserve
\(Q\), so (171.O11) is not a universal no-go for every signed commutator.
It verifies only that the present coordinate identities cannot claim the
fixed-\(Q\) families were removed, and that the parked positive
broad--narrow estimate cannot supply the missing complement bound.

## 4. First doubtful or unproved step

After the exact repairs above, the first unproved analytic step is a signed,
owner-preserving estimate for the surviving \((++)\) endpoint-swap
complement or, equivalently, a bounded/nonlocal signed \(q\)-primitive for
the complete actual symbol which controls every ramp-weighted gate and
support face before a positive norm.  No Round-171 report proves such a
theorem.

The \(L^4\) and \(L^5\) figures in the reports are positive/adversarial
capacities, not physical lower bounds.  Therefore they cannot reject
(171.O1).  They do rigorously reject the narrower inference that the defect
factorizations, normalized or unnormalized local multiplier commutators,
independent endpoint swaps, or coefficient-independent two-step Abel
summation automatically supply the missing factor \(L\).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal critical \(j=1\) scope | **GREEN.** One fixed persistent critical block only. |
| coordinate bijection and multiplicity | **GREEN after minor repair.** Multiplicity one; include (171.O4). |
| mod-4 parity and fixed-\(p\) character | **GREEN after minor repair.** \(p=2s\), sign \((-1)^s\); no fixed-fibre cancellation. |
| zero extension and support | **GREEN after minor repair.** Define zero first, phase second; global zero extension absorbs swap crossings. |
| \(p=0,q=0\) axes | **GREEN.** Both survive the gates and are separately \(O(L^3X^\varepsilon)\). |
| normalized defect commutators | **GREEN no-go.** They are commuting shifts, not an estimate. |
| unnormalized commutators | **GREEN after scope repair.** (171.O7) is exact; other Weyl commutators can be nonzero and must not be called zero. |
| fixed-width \(y=x\) strip | **GREEN.** \(O_C(L^3X^\varepsilon)\); complement division cancels the multiplier. |
| actual-real endpoint swaps | **REPAIR.** Promote (171.O9), not the ambiguous full-summand projection wording. |
| mixed SBP signs and ramp | **GREEN.** (171.O10) and the \(N/2\) primitive lower bound are exact. |
| gate/support power ledger | **GREEN as capacity only.** Unweighted faces are target-scale; the ramp removes the certified margin. |
| phase-free subtraction | **GREEN.** Only the fully assembled zero mode is paid; the bracket is not pointwise small. |
| fixed-\(Q\) rulings | **GREEN with scope.** They survive the gates/subtraction; they do not prove universal commutator failure. |
| gcd/slanted/alias/endpoints/real centre | **GREEN.** Retained literally; no liftwise or cornerwise modulus is used to claim the target. |
| constant-character and erased-structure shadows | **GREEN as falsifiers.** The proposed positive closures do not isolate the needed literal mechanism. |
| phase-adapted shadow | **GREEN with scope.** It refutes coefficient-uniform closure only and is not in the physical real class when complex. |
| factor \(L\) before positive norm | **FAIL for the audited route.** The certified complement remains at \(L^4\) capacity. |
| remaining-label owner quarantine | **GREEN.** Noncritical \(j=1\), exact-square \(j=2\), and all other BAL labels remain separate. |
| downstream/exponent scope | **GREEN.** No M2, M9, bridge, quarter theorem, or exponent change follows. |

No numerical experiment, computer algebra, or external theorem was used.

## 6. Dependencies and exact artifacts used

This review parsed the complete authoritative graph (374 obligation nodes
and 1353 rejected claims) at the displayed SHA-256 and used:

1. `AGENTS.md` and `protocol.md`;
2. `state/proof_obligations.yml` and `state/active_campaign.yml`;
3. the Round-171 strategy, plan, barrier packet, statement-only packet, and
   all three task briefs;
4. all three Round-171 reports;
5. `reviews/blind_post_unmask_identity_scope_review.md` and
   `reviews/ramp_identity_power_seam_review.md`;
6. the permitted Round-114 energy/corridor synthesis and conductor reviews;
7. the permitted Round-115 phase-free synthesis and conductor reviews;
8. the permitted Round-136 ruling synthesis, hostile report, and conductor
   and post-unmask reviews; and
9. the permitted Round-170 graph/frontier report, dependency review,
   adjudication, and synthesis.

The exact accepted graph inputs are the literal atom dictionary, character
factor, full-product double-corridor reduction, phase-free mode reduction,
divisor-progressive alias reduction, alias-character restoration, fixed-
\(Q\) broad--narrow obstruction, the open critical remainder and energy,
the separate remaining-label owner, full BAL, M9--M2, M9, both bridges, and
`GC-target`.  No web source or unaccepted theorem is used.

## 7. Recommended state effect and verdict

After the conductor writes a kernel containing the exact repairs
(171.O4), the piecewise zero-extension convention, and (171.O9), create one
proved obstruction node, preferably

`M9-M2-balanced-two-defect-commutator-ramp-obstruction`.

Its statement should be restricted to:

- the multiplicity-one persistent-critical-\(j1\) \((h,k,p,q)\) chart;
- the canonical side-sum-normalized defect multiplier commutators;
- the parity-compatible unnormalized commutator (171.O7), including its
  fixed-width singular strip and tautological complement;
- independent endpoint-swap summation by parts with the exact surviving
  \((++)\) complement (171.O9); and
- coefficient-independent local two-step Abel summation before a positive
  norm, with the forced length-\(L\) \(q\)-primitive.

Give this obstruction dependencies on the accepted literal dictionary,
character factor, double-corridor reduction, phase-free reduction,
divisor-progressive alias/character restoration, and fixed-\(Q\) obstruction.
It should have no implication edge to the target.

Update `M9-M2-balanced-double-far-oscillatory-remainder` and, through its
proved equivalence, `M9-M2-balanced-double-far-actual-energy` only by adding
the new obstruction as evidence/dependency and by changing the next action
to a genuinely signed nonlocal actual-symbol \(q\)-primitive/correlation
theorem that controls the \((++)\) complement, ramp-weighted faces, and
fixed-\(Q\) families before any modulus.  Keep both statuses `open`.

Record rejected overclaims that (i) the defect factorizations themselves are
a saving commutator, (ii) every coordinate commutator vanishes, (iii)
division by \(y-x\) supplies \(L^{-1}\), (iv) the full scalar equals its
double-antisymmetric endpoint-swap piece, (v) a bounded coefficient-
independent \(q\)-primitive exists on a length-\(L\) fibre, (vi) the axes or
fixed-\(Q\) classes disappear, or (vii) an adversarial capacity is a physical
lower bound.

Make **no status, implication, bridge, theorem, or exponent change** to the
critical remainder/energy, the remaining-label connector, full BAL, hard
TOP, UNBAL, M9--M2, either M1 route, endpoint assembly, M9, either bridge,
or `GC-target`.

**Final verdict: REPAIR.**  The scoped method no-go is promotable after the
three exact statement repairs above; the target remainder is not proved or
disproved, and no global exponent improves.

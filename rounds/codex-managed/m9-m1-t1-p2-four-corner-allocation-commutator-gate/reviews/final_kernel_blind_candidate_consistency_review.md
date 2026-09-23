# Round 197 final durable-kernel blind consistency review

## 1. Result

**Verdict: GREEN.**

The durable proof kernel at SHA-256

\[
\texttt{D3D6AC897E8A193BE83820136EAB28D0B55EAFF030351D060E72B4524D413CC9}
\]

is an exact mathematical transplant of the final candidate at SHA-256

\[
\texttt{285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0}.
\]

A line-level comparison has only three nonmathematical differences:

1. the title says “Proof kernel” rather than “Formal candidate”;
2. the status line identifies a durable artifact rather than a pending
   conductor formalization; and
3. the kernel has one final blank line.

Every numbered definition, displayed equation, theorem statement,
argument, complement, no-go, dependency, scope exclusion, and proposed
state effect is otherwise identical.  The kernel introduces no
strengthening, dropped hypothesis, new dependency, or scope expansion.

## 2. Exact statement and hypotheses

The kernel retains the candidate's exact hypotheses:

\[
 X\ge2,\quad L\ge2,\quad \sigma\in\{\pm1\},\quad
 B>0,\quad K_{\mathrm{sel}}>0,\quad C_0\ge2,
\]

with the same \(H_B,R_0,D_L\), total zero-extended endpoint
\(\lambda_{N,\sigma}(d)\), physical even-shift source, gcd normalization,
and one-close allocation mask \(P_2\).

It retains the same strict lower sector

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1}
\]

and the same symmetric common-cell mask

\[
 P_{\rm cc}
 =P_0\mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
                    =\mathfrak c_{N,\sigma}(\alpha,gm)\}}.
\]

The arithmetic gate \(I_{\rm ar}\), literal gate \(I_{\rm lit}\), closed
sharp-label list, distinguished dead code \(\dagger\), selector
definition, physical atom \(W\), inward cross gcd \(\kappa\), fixed
packet type, Farey data, outer restoration, cap/open split, and
\(\mathscr H_{\rm out}\), \(\mathscr S_{\le192,\rm out}\) operators all
agree equation-for-equation with the final candidate.

The two claimed estimates are unchanged:

\[
 |\mathscr R_{\mathrm{core,out}}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon
\]

and

\[
 |\mathscr R_{\mathrm{open,out}}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.
\]

Only \(P_{\rm cc}\) and its exact open-packet intersection are claimed.

## 3. Proof or derivation audit

### 3.1 Allocation, gcd, and character algebra

At the lower image,

\[
 (gm,g\beta)=g(m,\beta)=g,
\]

while the reverse condition is the normalized identity
\((\alpha,\beta)=1\).  The products, \(r\), allocation defects, Fejer
factor, and radical phase remain unchanged.  Since
\(\chi_4(\alpha m)=-1\), \(m\) is odd, the swapped divisor \(gm\) is
physical, \(\alpha\ne m\), and the orbit is a genuine two-cycle.

The character ratio is exactly

\[
 {\chi_4(g\beta)\chi_4(gm)\over
   \chi_4(g\beta)\chi_4(g\alpha)}
 =\chi_4(\alpha m)=-1.
\]

Thus the physical orbit is the actual endpoint difference in (197.C17).
The subsidiary four-corner gcd table, relative character table,
common sign \(\chi_4(\alpha\beta)\), \(4\mid r\) consequence, mixed
rectangle factorization, forced \(\kappa=1\), and simultaneous-swap
failure are all copied exactly and remain correct.

### 3.2 Sharp code and zero extension

The kernel uses the same exact arithmetic conjunction

\[
 u,v>0,\quad uv=N,\quad2\nmid v,\quad
 \mu^2(N)=1,\quad(u,v)=1
\]

and the same closed literal-support gate.  A failed gate maps to
\(\dagger\); a live gate maps to the complete tuple of sharp labels.
The code excludes \(\rho_N,\eta_L\), smooth factors, and accidental
coefficient values.

Under the lower swap, the inputs
\((m,g\alpha)\) and \((\alpha,gm)\) are exchanged, so code equality is
symmetric.  A common dead code gives two literal zeros, a common live
code gives the exact common sharp multiplier, and a live/dead pair lies
in the complement.  A selector zero is not confused with a sharp death.
This is the same zero-extension discipline as in the candidate.

### 3.3 Selector and actual coefficient formula

The kernel retains the exact canonical pair of distinct odd selected
primes and

\[
 \rho_N(v)
 =1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
   +2\mathbf1_{p_Nq_N\mid v},
\]

with \(\rho_N\equiv1\) if no pair exists.  Its truth table is
\((1,0,0,1)\).

On a common live code, the kernel has the same identity

\[
 a(u,v)=K_{\rm sharp}\eta_L(u)b^{\rm sm}(u,v)
\]

and the same separate sup-norm, variation, and gradient bounds.  With
the notation of (197.C22c), the actual endpoint difference is

\[
\begin{aligned}
 \lambda(g\alpha)-\lambda(gm)
 =\mu^2(N)K_{\rm sharp}\{&
 \rho_0\eta_0(b_0-b_1)
 +\rho_0b_1(\eta_0-\eta_1)\\
 &+(\rho_0-\rho_1)\eta_1b_1\}.
\end{aligned}
\]

Direct expansion gives
\(\mu^2(N)K_{\rm sharp}
(\rho_0\eta_0b_0-\rho_1\eta_1b_1)\), so no coefficient factor or
commutator was lost in the durable copy.

The finite-\(g\) proof

\[
 g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}\le G_0
\]

is unchanged.  It supplies the \(O(1)\) physical multiplicity in the BV
sum and the finite set used by the selector exception.  The logarithmic
gap excludes an exactly-one-selected-prime-in-\(g\) commutator for large
shells; bounded shells are paid absolutely.

### 3.4 BV and power ledger

The normalized-BV estimate is unchanged:

\[
 \sum_{|a-b|\le D_L}|\eta_L(a)-\eta_L(b)|
 \ll D_L^2\operatorname {Var}(\eta_L).
\]

The finite-\(g\) multiplicity and \(O(LX^\varepsilon)\) upper
completions give \(O(D_L^2LX^\varepsilon)\).  The smooth difference
gives the same scale through

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon\ll L^2X^\varepsilon.
\]

Together with the selector treatment, these three terms exhaust the
actual coefficient difference in both the candidate and kernel.

### 3.5 Complement and no-go

The exact Boolean partition is unchanged:

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\mathrm{lit}}
       \ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f}.
\]

No target estimate is claimed for the last three pieces.  The sharp-face
self-return identity

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}<0
\]

and its \(D_LL^2X^\varepsilon\) capacity conclusion are copied exactly.
The durable kernel therefore preserves, rather than erases, the blind
whole-sector no-go.

### 3.6 Operator typing and scope

The fixed packet, \(T=0\) branch, simultaneous strict \(T\ge1\) Farey
conditions, outer assembly, and cap/open partition are identical.
The exact identities

\[
 \mathscr R_{\rm core,out}
 =\mathscr R_{\rm cap,out}+\mathscr R_{\rm open,out}
\]

and

\[
 \mathscr R_{\rm core,out}
 =\mathscr H_{\rm out}-\mathscr S_{\le192,\rm out}
\]

remain explicitly typed.  The transported-mask product rule retains its
mask commutator, and the open estimate is obtained only after the
complete masked physical/core estimate and deletion-stable cap
subtraction.

The durable scope list is verbatim: it excludes \(P_0\), full \(P_2\),
\(P_1\), the full rectangle, all parent obligations, endpoint
uniformity, M9, bridges, the target theorem, and any exponent change.
The proposed state effect leaves all prerequisite nodes unchanged and
therefore creates no reverse dependency.

## 4. First doubtful or unproved step

There is no candidate-to-kernel discrepancy and no new doubtful step in
the audited local algebra, sharp-code, selector, coefficient, BV,
complement, no-go, or scope interfaces.

As in the final candidate review, the first facts not independently
re-proved here are the four accepted prerequisite kernels named in
Section 6, especially their masked fixed-to-outer operator estimates.
The durable kernel cites the same files and exact equation ranges as the
candidate.  Their separate graph/provenance validation remains required;
this declared dependency boundary is not a transcription defect.

## 5. Required control test and outcome

1. **Normalized textual diff — PASS.**  Only title, status wording, and
   a terminal blank line differ; all mathematics is identical.
2. **Gcd and character — PASS.**  The lower image retains \(g\), and the
   character reverses exactly once.
3. **Sharp-code exchange — PASS.**  Input exchange preserves code
   equality; common death is zero and live/dead is excluded.
4. **Selector truth table — PASS.**  Neither/both selected primes give
   one; a split pair gives zero.
5. **Three-term coefficient expansion — PASS.**  It contracts to the
   exact difference of the two actual endpoint values.
6. **BV multiplicity — PASS.**  The \(D_L^2\) translation sum acquires
   only \(O(1)\) repetitions over \(g\).
7. **Complement — PASS.**  The four masks are disjoint and exhaust
   \(P_2\).
8. **Unsigned/simultaneous-swap shadows — PASS as falsifications.**
   Erasing the character creates a sum, and the simultaneous swap has
   multiplier \(+1\).
9. **Sharp-face no-go — PASS.**  The exact negative product and the
   unproved complement are retained.
10. **Scope and dependency-cycle control — PASS.**  No accepted
    prerequisite or parent status is rewritten.

## 6. Dependencies and exact artifacts used

This review used:

1. protocol.md as the governing proof-state and review protocol;
2. proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md at SHA-256
   D3D6AC897E8A193BE83820136EAB28D0B55EAFF030351D060E72B4524D413CC9;
3. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md at SHA-256
   285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0;
4. the already completed blind and post-repair reasoning in this
   reviewer's active Round-197 context.

No discovery report, hostile report, shared state, graph file, or
prerequisite kernel was reopened for this final transcription review.
The durable kernel was not edited.

## 7. Recommended state effect

**GREEN for exact candidate-to-kernel consistency.**  The durable kernel
is suitable to serve as the proof artifact for the same subordinate
\(P_{\rm cc}\) claim, subject to the remaining independent validations
and a mechanically valid State Patch.

Do not use this verdict to promote the complement, alter an accepted
prerequisite, close a parent, or change any bridge, endpoint theorem,
global theorem, or exponent.

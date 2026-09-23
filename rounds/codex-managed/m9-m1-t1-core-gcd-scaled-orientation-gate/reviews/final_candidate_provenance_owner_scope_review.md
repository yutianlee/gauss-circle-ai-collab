# Final candidate provenance and owner-scope review

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Round: 193
- Artifact reviewed: `candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`
- Verdict: **REPAIR**
- Audit boundary: this review checks formalization provenance, dependency
  typing, literal owner scope, the \(T=0/T\ge1\) convention, ordered tuple and
  conjugation language, and downstream/exponent quarantine.  It does not
  re-prove or independently assess the incidence count or its power ledger.

## 1. Result

The candidate's principal conclusion is not stronger than the common
conclusion of the two Round-193 claimant reports.  Both reports support the
absolute \(O_{B,\varepsilon}(L^2X^\varepsilon)\) treatment of every opposing
physical incidence satisfying the two gcd-scaled close inequalities, without
assuming \((m,m')=1\) or \(r\equiv2\pmod4\).  Both also treat the scaled
orientation involution only as subsidiary algebra on the narrower
cofactor-coprime \(r\equiv2\pmod4\) sub-sector, require the physical mask to be
lifted coordinatewise through the accepted linear decompositions, and leave
the first-failure complement open.

The main statement, physical-mask convention, exact complement, owner scope,
and exponent quarantine therefore pass.  Promotion nevertheless requires the
formal repairs below.  The first defect occurs already in (193.C4): \(T\) is
used without definition, the Round-192 Fourier-lift variable is not
distinguished from the physical endpoint cofactor \(m\), and the fixed
parameter \(C_0\) is absent.  A second exact defect occurs in (193.C29), whose
display is written as an unrestricted sum although the commutator is valid
only on the explicitly restricted involutive sub-sector.

## 2. Exact statement and \(T=0/T\ge1\) convention

**REPAIR.**  Replace the prose at (193.C4) by a self-contained import of the
accepted Round-192 convention.  In particular, use a new symbol such as
\(\mathfrak m\) for the Round-192 Fourier lift and reserve \(m\) for the
physical complementary factor in (193.C2).  The candidate must state, before
(193.C4),

\[
 U=\mathfrak m q>4Q,\qquad q>Q,\qquad
 \mathfrak m|a|_q>Q,\qquad Q\mathfrak m<Y,
\]

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},
\]

\[
 T=\min\!\left\{\frac{U-1}{2},
       \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\}.
\]

It must then fix \(C_0\ge2\), independently of every asymptotic variable, and
define with a noncolliding Farey coordinate \(d_0\)

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
 \mathcal F_A=\{(c,d_0):1\le c\le A,\ 0\le d_0\le c,
                         (c,d_0)=1\}.
\]

The two branches must be stated literally:

- if \(T=0\), the Round-192 union projector \(P_A\) is identically zero and
  the core is the whole inherited Round-191 rho-large remainder before the
  new Round-193 physical split;
- if \(T\ge1\), every retained core row satisfies simultaneously

\[
 |c\beta-d_0\rho|>T\quad((c,d_0)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\]

The candidate's present prose has the right branch semantics, so this is a
formal completeness repair rather than a change of sector.  Because the
masked safe aggregate includes the accepted Round-192 Farey estimate, change
the constants in (193.C7) and (193.C20) to

\[
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

unless \(C_0\) is explicitly fixed once and declared absorbed throughout.
The physical bounds (193.C17), (193.C18), and (193.C24) need no \(C_0\)
dependence.  Also repair the malformed TeX in (193.C3) to

\[
 d,m,d',m'\asymp L,\qquad |W_x|\ll_\eta X^\eta.
\]

## 3. Ordered tuple, sub-sector, and conjugation

The ordered endpoint convention passes: throughout (193.C2), (193.C8), and
(193.C25)--(193.C27), the tuple means

\[
 (\text{lower character divisor},\text{lower cofactor},
   \text{upper character divisor},\text{upper cofactor}).
\]

Thus

\[
 (d,m,d',m')\mapsto(gm,d/g,gm',d'/g)
\]

has the correct output order.  The coefficient bracket also has the correct
endpoint order and conjugation: the upper coefficient is unbarred and the
lower coefficient is conjugated on both orbit legs.

**REPAIR (193.C29).**  Define the exact domain

\[
 P_{\rm sw}:=P_{\rm cl}\,
 \mathbf1_{(m,m')=1}\,
 \mathbf1_{r\equiv2\ ({\rm mod}\ 4)}
\]

before the pairing display, and replace the unrestricted
\(\sum_x\) by \(\sum_{x\in P_{\rm sw}}\).  The left side, if one is
displayed, must be the physical \(P_{\rm sw}\)-restricted block, not the
whole \(P_{\rm cl}\) block.  Define the otherwise undefined phase package
exactly as

\[
 \Phi_r(N)=\left(1-\frac r{R_0}\right)
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right).
\]

The bracket itself should remain

\[
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}
 -\lambda_{N+r,\sigma}(gm')\overline{\lambda_{N,\sigma}(gm)}.
\]

With those corrections, (193.C28)--(193.C29) matches both claimant reports.
Without the \(P_{\rm sw}\) restriction, the current display literally
overstates their subsidiary involution identity.

## 4. Literal physical owner and masked-core typing

**PASS.**  The candidate correctly defines \(P_{\rm cl}\) on the original
opened physical atoms, before anchor Fourier expansion and height
differencing.  The bracket notation

\[
 \mathscr R_{\rm core}[P]:=\mathscr R_{\rm core}(PW)
\]

is explicitly operator evaluation on a deleted physical source, not a new
spectral predicate on an already-formed core.  Equation (193.C19) retains the
mask birth/death commutator and does not assert the false identity
\(P\Delta^-W=\Delta^-(PW)\).  Equations (193.C21) and (193.C23) consequently
have the correct linear-operator type, retain the whole anchor Fourier sum,
and introduce neither overlap nor a post-Abel mask.

**REPAIR (literal-field wording only).**  The sentence preceding (193.C30)
must not say that a common cell makes "each factor" cost \(O(D_L/L)\).
Use the factorization from the discovery report:

\[
 \text{endpoint symbol}=\eta_L(u)b^{\rm sm}(u,v),
\]

where only the uniformly \(C^1\) factor \(b^{\rm sm}\) has pointwise
displacement \(O(D_L/L)\).  The normalized dyadic/BV factor \(\eta_L\) is
charged separately by (193.C31).  This correction preserves the asserted
power and prevents the smooth-cell sentence from silently absorbing a
literal boundary jump.

## 5. Provenance and dependency typing

The recorded starting graph hash
`7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
matches the SHA-256 of the current `state/proof_obligations.yml`.

The two Round-193 reports are correctly typed as candidate evidence, not as
accepted mathematical dependencies.  Their common proved claim is precisely
the wider absolute double-close sector.  The cofactor-coprime
\(r\equiv2\pmod4\) involution, selector audit, and BV/collar route are
subsidiary controls; they are not the premise for the main absolute bound.

**REPAIR the undifferentiated heading "Direct accepted dependencies."**  It
currently mixes logical/interface prerequisites, accepted connector proofs
reopened for deletion stability, and transitive or subsidiary provenance.
Replace it by the following typed ledger:

1. **Direct logical/interface prerequisites for (193.C5)--(193.C23):**
   `M9-M1-hard-top-t1-rho-large-farey-covector-reduction` for the exact core,
   and `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction` for the
   multiplicity-one opened physical opposing source.  If the graph convention
   suppresses redundant transitive edges, the former is the graph edge and
   the latter remains explicit physical-interface provenance.
2. **Accepted connector proofs explicitly reopened to establish deletion
   stability:** the Round-187 inverse-residue/conductor, Round-188
   imprimitive-lift, Round-189 projective, Round-191 signed-inverse/height, and
   Round-192 Farey kernels.  These artifacts are used to justify (193.C20);
   Round 193 does not re-promote or enlarge any of their accepted statements.
3. **Inherited or subsidiary provenance:** the Round-184 comparable-factor
   exchange kernel supplies the residual-selector truth table used only in
   (193.C29)--(193.C31) and is otherwise transitive through Round 185.
   `Divisor-bound-elementary` is inherited through the accepted ledgers; list
   it as a direct edge only if the new State Patch treats the reopened divisor
   multiplicity as a fresh direct invocation.

The candidate should also name the two claimant report paths and the accepted
Round-192 kernel path explicitly in this provenance ledger.  If the Round-193
Wolfram control is retained in the text, name its exact control and output
paths and say that neither claimant used it to prove the asymptotic estimate;
otherwise replace the vague "archived Wolfram computation" sentence by
"No Round-193 computation is theorem evidence."  Either wording keeps the
diagnostic-only type.

## 6. Owner scope, downstream quarantine, and exponent quarantine

**PASS.**  The only proposed state effect is one subordinate strict-sector
node for (193.C5)--(193.C23), attached as evidence to the already-open
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  The candidate does
not claim either first-failure complement, the complete rho-large core, the
complete original \(t=1\) residual, any original \(t\ge2\) range, the
large-\(G\) near-resonant complement, the remaining small-\(t\) owner, either
M1 parent, GAR, any M2 parent, endpoint uniformity, M9, either bridge, or the
Gauss-circle theorem.

The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) records are explicitly
unchanged.  No owner pivot, parent closure, bridge closure, density inference,
literal lower-mass inference, or exponent improvement is present.

The candidate's promotion language is conditional on independent reviews and
a valid State Patch.  That is correctly scoped.  Completion and reconciliation
of the separate statement-only blind/post-unmask gate are outside this
provenance review; the conductor must verify that lifecycle independently
before promotion.  This hold is not a contradiction of the two claimant
reports audited here.

## 7. Required control outcomes and recommended state effect

| Control | Outcome |
|---|---|
| starting graph provenance | **PASS**: recorded hash matches current graph |
| claimant intersection / no overstatement of main theorem | **PASS** |
| exact \(T=0/T\ge1\) import and notation | **REPAIR**: insert \(\mathfrak m,T,C_0,A,\mathcal F_A\), both branches, and \(C_0\)-dependent constants |
| physical-mask owner and complete Fourier recombination | **PASS** |
| height-difference commutator and masked-core identity | **PASS** |
| opened tuple order | **PASS** |
| upper-unbarred/lower-conjugated coefficient order | **PASS** |
| exact involutive summation domain | **REPAIR**: define \(P_{\rm sw}\), restrict (193.C29), and define \(\Phi_r\) |
| literal smooth/BV separation | **REPAIR**: restrict \(O(D_L/L)\) to \(b^{\rm sm}\) and leave \(\eta_L\) to (193.C31) |
| dependency typing | **REPAIR**: split direct, reopened-connector, inherited, and subsidiary provenance |
| exact first-failure complement | **PASS** |
| literal owner/downstream scope | **PASS** |
| exponent quarantine | **PASS** |
| diagnostic-only computation | **PASS after exact artifact naming or explicit nonuse statement** |
| blind/post-unmask lifecycle gate | **OUTSIDE THIS REVIEW**; conductor verification remains required |

Recommended action: **revise, then recheck the repaired candidate; do not
promote from the present text.**  The repairs are local formalization and
typing corrections.  They do not narrow the principal double-close theorem
or enlarge any downstream owner.  After these corrections and independent
verification of the blind/post-unmask gate, the candidate is eligible for the
remaining State Patch and graph-replay lifecycle controls.

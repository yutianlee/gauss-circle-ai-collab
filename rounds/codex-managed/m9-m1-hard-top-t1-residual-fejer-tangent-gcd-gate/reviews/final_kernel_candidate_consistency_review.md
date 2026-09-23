# Round 185 final-kernel candidate-consistency review

## 1. Result / verdict

**Verdict: GREEN**

The frozen source candidate and durable kernel hashes both match the brief:

\[
\begin{aligned}
 {\rm SHA256}(\text{candidate})
 &=74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65,\\
 {\rm SHA256}(\text{kernel})
 &=4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
\end{aligned}
\]

The durable kernel faithfully transcribes the repaired candidate at every
assigned mathematical interface. It is self-contained at the stated
dependency boundary, preserves the literal endpoint fields and exact
multiplicities, proves only the bounded-height physical sector, and leaves
(K185.37) explicitly open. No mathematical transcription or scope error was
found.

## 2. Exact statement and hypotheses

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\geq2\), \(\sigma\in\{+1,-1\}\), and fixed \(B>0\). Let
\(R_0=\lceil L\rceil\) and
\(H_B=\lfloor(\log(2X))^B\rfloor\). The Round-184 selector is canonical in
the endpoint product \(N\), independent of an allocation \(N=dm\), and the
literal symbol is zero off every stated shell, cone, arithmetic, profile,
floor, star, half-weight, sample, crossing, endpoint, and sign predicate.
The accepted diagonal is

\[
 \sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

Under these hypotheses, the durable kernel proves:

1. the endpoint-exact parity connector from the full residual to the even
   Fejer correlation;
2. the multiplicity-one tangent, original-gcd, inward-cross-gcd, and joint
   quotient reductions;
3. the absolute
   \(O_{B,\varepsilon}(L^2X^\varepsilon)\) bound for the complete monotone
   sector together with both opposing sectors satisfying \(h\leq H_B\);
4. the canonical multiplicity-one expression (K185.36) for the exact
   opposing complement \(h>H_B\).

It does not prove the complete residual estimate. The dyadic high-height
bound (K185.37) is a sufficient open relation.

## 3. Proof or line audit

### Residual selector, domain, and support

Candidate (185.C1)--(185.C3) are transcribed as (K185.1)--(K185.4).
The mask

\[
 1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_Nq_N\mid d}
\]

has truth table \(1,0,0,1\). The branch definition of
\(\lambda_{N,\sigma}(d)\) evaluates the selector and literal symbol only for
positive squarefree integral \(N\) and positive odd \(d\mid N\), and is zero
otherwise. The separate declaration \(c_{N,\sigma}^{\rm rem}=0\) for
\(N\leq0\) preserves the repaired total domain. The list of literal
zero-extension fields and the support facts \(d,m\asymp L\),
\((d,m)=1\), and \(N\asymp L^2\) agree with the source candidate.

### Diagonal, Fejer parity, and Cauchy factor

Candidate (185.C4)--(185.C7) are faithfully reorganized as
(K185.8)--(K185.12). Splitting a length-\(R\) window into even and odd
offsets gives \(R\) diagonal positions and \(R-2q\) forward pairs at gap
\(2q\). Therefore the kernel has the correct constants

\[
 \mathfrak E_R\leq2D_{L,\sigma}+4\Re\mathfrak C_R^{(2)}.
\]

For odd \(R\), the terminal gap \(R-1\) has weight \(1/R\) and coefficient
\(4/R\). For even \(R\), the terminal gap \(R-2\) has weight \(2/R\) and
coefficient \(8/R\). Summing the full-line windows counts each \(z_N\)
exactly \(R\) times, while at most \(M_L+R-1\) windows meet the support, so
(K185.12) has the exact factor \((M_L+R-1)/R\). Both signs use the same
identity with the displayed \(\sigma\)-phase.

### Tangent opening, parity, and character

Candidate (185.C8)--(185.C12) become (K185.6) and
(K185.13)--(K185.15). Choosing \(d\mid N\) and \(d'\mid N+r\) determines
\(m=N/d\) and \(m'=(N+r)/d'\) uniquely. For even \(r\), odd \(d,d'\)
force \(a=2\alpha\) and \(b=2\beta\). Direct multiplication gives

\[
 r=db+am+ab=db+am'=am+bd'
\]

and all three half-shift identities. The character factor
\(\chi_4(d')\chi_4(d)=(-1)^\alpha\) is unchanged. The monotone
\(O(L^2)\) count and the disjoint opposing complement
\(a>0>b\) or \(a<0<b\) are also transcribed without enlargement.

### Original gcd, inward cross gcd, and joint quotient

Candidate (185.C13)--(185.C31) correspond to
(K185.16)--(K185.29). For \(g=(d,d')\), the equation
\(vm'-um=r/g\) and its fixed-\(g\) row multiplicity yield
\(O(L^3/g^2)\), hence \(O(L^3/G)\) above \(G\).

The plus orientation in (K185.18)--(K185.19) uses
\(\kappa=(d,m')\) and gives \(r=2\kappa(sv-wu)\). The minus orientation
in (K185.20)--(K185.21) uses \(\kappa=(d',m)\) and gives
\(r=2\kappa(uw-sv)\). These are the same endpoint placements as the
candidate. Each parametrization is invertible from an opened tuple, and
the fixed-\(\kappa\) count \(O(L^3/\kappa^2)\) and tail
\(O(L^3/K)\) have the correct powers.

At the appropriate squarefree endpoint, \((\kappa,s)=1\). Thus

\[
 g=(d,d')=(u,s)=(u,n),
\]

and \(u=gU\), \(s=gS\), \(n=gh\) give
\(r=2\kappa gh\) and the two primitive equations in (K185.26). The
primitive domain (K185.27) exactly matches candidate (185.C24):

\[
 \kappa,g,h,U,v>0,\quad
 \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0.
\]

The fixed-\((\kappa,g,h)\) count, bounded-height sum, endpoint coefficient
rebudgeting, and explicit \(\gamma^{-1}\), \(\delta^{-1}\) tail factors
are copied with the same hypotheses. The kernel's statement that the
corresponding fixed-proportion tail is contained in (K185.7) whenever its
own displayed threshold holds is the componentwise form of the candidate's
two simultaneous containment statements, not an added theorem.

### Canonical rows, endpoints, and exact complement

Candidate (185.C32)--(185.C37) become (K185.30)--(K185.37). For \(U>1\),
\((U,v)=1\) gives one least-residue anchor for each primitive equation.
For \(U=1\), the explicit plus base \((0,-h)\) and minus base \((0,h)\)
avoid an inverse modulo one and enumerate the full affine solution sets.
The oriented index sets impose \(S_t>0\) and \(w_t>0\) before any phase is
evaluated. Hence all endpoint factors and square roots are positive, the
two tangent orientations are disjoint, and the former wrong-orientation
continuations are absent.

For plus, (K185.32)--(K185.33) place the un-conjugated coefficient at

\[
 N+r=(\kappa gU+2s)\kappa v
\]

and the conjugated coefficient at

\[
 N=\kappa gU(\kappa v+2w).
\]

For minus, (K185.34)--(K185.35) make the required orientation-dependent
swap. In both cases the product difference is \(r=2\kappa gh\), and

\[
 e(\sigma\sqrt{X(N+r)})\overline{e(\sigma\sqrt{XN})}
 =
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right).
\]

Because \(g,U\) are odd,

\[
 \chi_4(d')\chi_4(d)
 =(-1)^{S_{0,\omega}}(-1)^t.
\]

A live opened tuple uniquely recovers its orientation,
\(\kappa,g,h,U,v\), canonical anchor, and \(t\). Conversely, a nonzero
indexed amplitude reconstructs one live tuple; the remaining arithmetic
and literal conditions are applied independently by the two endpoint
\(\lambda\)'s. Thus (K185.36) is a literal multiplicity-one reindexing
with one real part outside both orientations, all shifts, gcds, rows,
selector states, and endpoints. Removing (K185.7) leaves exactly
\(h>H_B\).

### Controls, dependencies, and scope

The capacity statements (K185.38)--(K185.39), the exact deletion example,
the sole terminal label, direct dependency list, method-control
quarantine, and downstream open-status list agree with the source
candidate. The kernel does not turn the deletion control into physical
lower mass or asymptotic evidence. It calls itself a durable
proof-kernel candidate pending final validation and nowhere presents the
complete residual, a parent estimate, a bridge, endpoint uniformity, or an
exponent as proved.

## 4. First doubtful or unproved step

No doubtful or unproved step occurs in the durable finite kernel through
(K185.36). The first unproved mathematical relation is (K185.37), the
uniform signed estimate over each dyadic high-\(h\) block. The kernel marks
it as still open and uses the conditional wording “would close”; its
positive-capacity discussion does not assert the missing cancellation.

## 5. Required controls and outcomes

1. **Frozen hashes.** Both source and kernel hashes equal the values in the
   brief. Outcome: passed.
2. **Selector and endpoint domains.** The \(1,0,0,1\) mask, positive
   piecewise endpoint definition, and full zero extensions match the
   candidate. Outcome: passed.
3. **Terminal parity cases.** Independent offset counting gives \(4/R\)
   at \(R-1\) for odd \(R\) and \(8/R\) at \(R-2\) for even \(R\).
   Outcome: passed.
4. **Two gcd orientations.** Re-expanding both product differences
   reproduces (K185.19) and (K185.21), with the original-gcd and
   inward-cross-gcd multiplicities unchanged. Outcome: passed.
5. **Primitive and \(U=1\) domains.** The conditions in (K185.27), both
   canonical congruences, and the modulus-one convention enumerate each
   positive oriented ray exactly once. Outcome: passed.
6. **Endpoint, phase, and character placement.** Upper and lower
   coefficients, conjugation, rationalized phase, and
   \((-1)^{S_0+t}\) agree in both orientations and for both signs.
   Outcome: passed.
7. **Exact-sector partition.** (K185.7) is the monotone union plus both
   opposing \(h\leq H_B\) sectors; (K185.36) is precisely the opposing
   \(h>H_B\) complement under one outer real part. Outcome: passed.
8. **Scope control.** (K185.37), the complete residual, all parent and
   downstream obligations, and every exponent remain open. Outcome:
   passed.

All checks were algebraic and textual; no numerical theorem evidence was
used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/active_campaign.yml
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/final_kernel_candidate_consistency_review.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/residual_fejer_parity_tangent_multiplicity_post_repair_verification.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/joint_h_count_power_and_deletion_post_repair_verification.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/blind_post_unmask_literal_owner_scope_post_repair_verification.md

No other repository artifact, web source, computation, or external theorem
was used.

## 7. Recommended state effect

Accept the durable kernel as a faithful, self-contained transcription of
the repaired source candidate and retain its bounded physical sector and
exact canonical complement as validated evidence. Keep (K185.37) and every
complete-residual, parent, endpoint-uniformity, bridge, theorem, and
exponent claim open. This review authorizes no direct graph or shared-state
mutation; any promotion must occur through the conductor's mechanically
validated State Patch.


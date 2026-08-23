# Round 120 conductor adjudication: terminal-height radial completion

Campaign: `m9-m1-gar-radial-interface-reconciliation`

Status: conductor proof pending the remaining independent reports and the
mechanical State Patch gate.

## 1. Adjudicated result

The terminal-height construction is valid after two explicit repairs:

1. use the certified closed profile-support constant \(C_W=3/2\), not a
   nonexistent uniform constant smaller than \(3/2\); and
2. prove, rather than merely assert, the terminal-height localized transform.

With those repairs, fix \(0<s_0<8\), put
\(R=X^{1/4}\), \(Y=\sqrt X\), \(\kappa=\sqrt{s_0}/4\), and choose a real
smooth function \(\vartheta\) satisfying

\[
 \vartheta(u)=0\quad(u\leq\kappa/2),\qquad
 \vartheta(u)=1\quad(u\geq\kappa).
\tag{120.J1}
\]

For an active scale \(D_j=2^{-j}\lfloor\sqrt X\rfloor\),
\(H_j=\lfloor D_j/R\rfloor\), insert
\(\vartheta(h/H_j)\) into the literal \((j,h)\)-atom defining
\(\mathcal C_X^*(n)\), and call the result
\(\mathcal C_{T,X}^*(n)\).  Scales with \(H_j=0\) are empty, so the quotient
is never formed there.  Then

\[
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_{\varepsilon,s_0}X^\varepsilon,
\tag{120.J2}
\]

and, for any fixed smooth lower cutoff with

\[
 V_{\rm low}(s)=1\ (s\leq s_0),\qquad
 V_{\rm low}(s)=0\ (s\geq2s_0),
\tag{120.J3}
\]

one has the sharp nonlower estimate

\[
 \boxed{
 \sum_{n\leq N_X}^{*}(1-V_{\rm low}(n/Y))
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,s_0}X^\varepsilon.}
\tag{120.J4}
\]

This proves the Round-98 radial-interface parent for this permitted fixed
one-count partition.  It does not prove the lower-radial parent, GAR,
blockwise `M9-M1`, or a new discrepancy exponent.

## 2. Direct terminal antecedent and exact transform

For \(H_j\geq1\), define

\[
 u_{j,T}(h)={\bf1}_{1\leq h\leq H_j}
 \vartheta(h/H_j){\Phi(h/(H_j+1))\over h}.
\tag{120.J5}
\]

Its support is contained in \(\kappa H_j/2<h\leq H_j\).  The sampled
smooth cutoff, the accepted BV profile \(\Phi\), the factor \(h^{-1}\),
and the two zero-extension jumps give

\[
 \|u_{j,T}\|_\infty+\sum_h|\Delta u_{j,T}(h)|
 \ll_{s_0}H_j^{-1}.
\tag{120.J6}
\]

For an actual atom, \(H_j\geq1\) and, with \(x_j=D_j/R\geq1\),

\[
 {x_j\over2}\leq\lfloor x_j\rfloor=H_j\leq x_j,
 \qquad {D_j\over H_j}\leq2R.
\tag{120.J7}
\]

The accepted frequency-first divisor theorem applied to (120.J5) therefore
gives, scale by scale,

\[
 \left|\sum_hu_{j,T}(h)\sum_d\chi_4(d)w_j(d)e(hX/d)\right|
 \ll_{\varepsilon,s_0}X^\varepsilon(1+D_j/H_j)
 \ll_{\varepsilon,s_0}RX^\varepsilon.
\tag{120.J8}
\]

There are \(O(\log X)\) active scales.  After the usual relabelling of
\(\varepsilon\), their positive antecedent \(\mathcal B_T^+\) is
\(O(RX^\varepsilon)\).

For fixed \((j,h)\), the accepted smooth interior character transform is
applied to \(w_j(d)\); the multiplier \(\vartheta(h/H_j)\) is constant in
the transformed variable \(d\).  At the stationary denominator

\[
 d_*=2\sqrt{hX/q},
\]

the stationary phase, Gaussian unit, and amplitude are exactly those in
the accepted Round-60 positive-frequency identity.  Multiplication by
\(u_{j,T}(h)\) and the identity

\[
 (hX)^{1/4}q^{-3/4}h^{-1}=R(hq)^{-3/4}
\tag{120.J9}
\]

reconstruct the literal coefficient with the extra terminal factor.  Thus

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})+\mathcal E_T^+.
\tag{120.J10}
\]

This is not an appeal to the physical endpoint-prefix package.  It is the
same coefficient-preserving positive character transform used in the
proved critical transfer, rerun with an outer fixed-height multiplier.

The accepted smooth/interior remainder is absolute for each frequency and
is \(O(\log(2+h))\) before the outer Vaaler weight.  Hence (120.J5) gives

\[
 \sum_{\kappa H_j/2<h\leq H_j}{\log(2+h)\over h}
 \ll_{s_0}\log(2+H_j).
\tag{120.J11}
\]

At the unique hard profile, the accepted one-sided transform retains the
full sample \(d=\lfloor\sqrt X\rfloor\).  Its character-cotangent boundary
is pointwise \(O(1)\); the terminal \(h^{-1}\)-mass is
\(O_{s_0}(1)\).  Therefore the hard boundary is \(O_{s_0}(1)\), while its
transform remainder obeys (120.J11).  Summing scales gives

\[
 \mathcal E_T^+\ll_{s_0}\log^2(2X).
\tag{120.J12}
\]

No cancellation across the deleted lower heights is used in (120.J11) or
(120.J12), so the new \(h\)-interface creates no unowned error.  Equations
(120.J8), (120.J10), and (120.J12), divided by \(R\), prove (120.J2) in
complex modulus.  Since \(\vartheta,\Phi,w_j\) are real, the negative
frequency is the conjugate transform and restores the accepted paired GAR
normalization without a second estimate.

The endpoint-prefix, endpoint-boundary, and \(R_1\) modules belong to a
different physical-limit architecture.  They are neither inserted into
(120.J10) nor relabelled as its errors; consequently they are counted zero
times on this route, not twice.

## 3. Exact support geometry

For a nonzero stationary atom put \(s=n/Y\) and

\[
 t={2h\sqrt{X/n}\over D_j}={2hR\over D_j\sqrt s}.
\tag{120.J13}
\]

The certified profile has \(1/2\leq t\leq3/2\).  Hence

\[
 {hR\over D_j}={t\sqrt s\over2}.
\tag{120.J14}
\]

If \(s\geq s_0\), then (120.J7), (120.J14), and \(t\geq1/2\) give

\[
 {h\over H_j}\geq{hR\over D_j}
 \geq{\sqrt{s_0}\over4}=\kappa.
\tag{120.J15}
\]

Thus \(\vartheta=1\) on every such atom and

\[
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)
 \qquad(n/Y\geq s_0).
\tag{120.J16}
\]

Conversely, if \(\vartheta(h/H_j)\ne0\), (120.J7) gives

\[
 {hR\over D_j}
 ={h\over H_j}{H_jR\over D_j}>{\kappa\over4}.
\tag{120.J17}
\]

Using \(t\leq3/2\) in (120.J14) yields

\[
 {n\over Y}>{\kappa^2\over9}={s_0\over144}=:c_T>0.
\tag{120.J18}
\]

Also \(h\leq H_j\leq D_j/R\) and \(t\geq1/2\) give \(n/Y\leq16\).
Every floor, internal stationary star, hard sample, and the outer product
tie remains exactly the one in \(\mathcal C_X^*\).

## 4. Localized terminal transfer

The remaining seam in the blind follow-up is now supplied explicitly.
Choose a real \(\psi\in C_c^\infty((0,16))\) satisfying

\[
 \psi(z)=1\qquad(\kappa^2/9\leq z\leq2s_0),
\tag{120.J19}
\]

and put \(W_0(z)=\psi(z)V_{\rm low}(z)\).  Such a cutoff exists because
\(0<\kappa^2/9\) and \(2s_0<16\).

There is also an exact antecedent-level justification.  On the joint
support of \(\vartheta(h/H_j)w_j(d)\), (120.J17) and
\(d\leq3D_j/2\) imply

\[
 {4R^2h^2\over d^2}>{\kappa^2\over9}.
\tag{120.J20}
\]

When \(V_{\rm low}(4R^2h^2/d^2)\ne0\), the same argument has
\(4R^2h^2/d^2<2s_0\).  Thus inserting \(\psi\) changes no reciprocal
summand.

Mellin inversion of the fixed compact multiplier \(W_0\) gives modes with
frequency coefficient

\[
 {\bf1}_{h\leq H_j}\vartheta(h/H_j)
 {\Phi(h/(H_j+1))\over h}h^{2it}
\tag{120.J21}
\]

and denominator coefficient \(\chi_4(d)w_j(d)d^{-2it}\).  The former has
supremum plus sampled variation

\[
 \ll_{s_0}{1+|t|\over H_j},
\tag{120.J22}
\]

while the latter is bounded.  The terminal theorem and the Schwartz decay
of \(\widehat W_0(t)\) give an \(O(RX^\varepsilon)\) antecedent after all
scales.

For the transform, use

\[
 A_{j,h}(d)=w_j(d)W_0(4R^2h^2/d^2).
\]

On (120.J21), \(h\asymp_{s_0}H_j\asymp D_j/R\), so every normalized
\(d\)-derivative of \(A_{j,h}\) is uniformly bounded.  The accepted
interior and hard transforms therefore apply modewise (or directly), with
only polynomial \(|t|\)-loss absorbed by \(\widehat W_0\).  At the saddle,

\[
 {4R^2h^2\over d_*^2}={hq\over Y}.
\tag{120.J23}
\]

The same absolute error calculation (120.J11)--(120.J12) proves

\[
 \sum_{n\leq N_X}^{*}W_0(n/Y)\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_{\varepsilon,s_0}X^\varepsilon.
\tag{120.J24}
\]

By (120.J18)--(120.J19), the left side equals the
\(V_{\rm low}\)-weighted terminal sum.  This proves the localized lemma
which the blind addendum correctly identified as necessary.

## 5. One-count completion and scope

From (120.J3) and (120.J16), coefficientwise for every integer \(n\),

\[
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)
 =(1-V_{\rm low}(n/Y))\mathcal C_{T,X}^*(n).
\tag{120.J25}
\]

The right side is the full terminal sum (120.J2) minus (120.J24), proving
(120.J4).  This includes the natural sharp outer support and its star; no
limit \(C\uparrow16\), moving seminorm, finite Mellin-height substitute, or
identification with a boundary prefix occurs.

If the Round-98 partition retains separate compact critical pieces, subtract
their already proved bounds from (120.J4); the residual sharp interface is
still target-safe.  Equivalently, use the permitted two-piece partition
\(V_{\rm low}+(1-V_{\rm low})=1\).  In either presentation each original
coefficient is owned exactly once.

The original blind no-go remains correct as a nonimplication from the
statement-only endpoint and compact-sector hypotheses: those hypotheses do
not contain (120.J10) or (120.J24).  The present proof supplies the missing
input from the accepted terminal-frequency and coefficient-preserving
interior/hard transform artifacts; it does not invalidate that isolation
control.

## 6. Controls and outcomes

| Control | Outcome |
|---|---|
| terminal frequency BV | Pass by (120.J6); the new interface is priced. |
| active floors and \(H_j=0\) | Pass by explicit empty-scale convention and (120.J7). |
| exact positive transform | Pass by (120.J9)--(120.J10). |
| hard sample and cotangent boundary | Pass; full sample retained and terminal mass is \(O(1)\). |
| aggregate transform error | Pass absolutely at \(O(\log^2 X)\). |
| both signs | Pass by real-coefficient conjugacy; modulus is already proved positively. |
| profile support constant | Repaired to the exact \(C_W=3/2\). |
| terminal lower support | Pass with \(c_T=s_0/144\). |
| localized terminal transfer | Pass by (120.J19)--(120.J24). |
| endpoint-prefix/R1 ownership | Pass as an alternative route; neither is inserted here. |
| physical versus finite Mellin limit | Pass; no endpoint physical limit or finite-height surrogate is used. |
| one-count radial partition | Pass by (120.J25). |
| downstream implication | Interface only; lower radial, GAR, blockwise M1, M9, and exponent remain open. |

No numerical computation or new external source is used.

## 7. Exact dependencies and recommended state effect

The proof uses:

1. `state/proof_obligations.yml`, especially
   `M9-M1-terminal-frequency-divisor-bound`,
   `M9-M1-smooth-critical-radial-terminal-transfer`,
   `M9-M1-top-endpoint-transform`, and the Round-98 radial assembly;
2. `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`;
3. `rounds/codex-managed/m9-m1-critical-radial-terminal-return/reports/critical_radial_terminal_transfer_attack.md`;
4. `rounds/codex-managed/m9-m1-critical-radial-terminal-return/synthesis.md`;
5. `rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`;
6. `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`;
7. `rounds/codex-managed/m9-m1-route-interface-assembly/synthesis.md`;
8. the Round-120 candidate and blind report.

Subject to the remaining independent seam reports and mechanical validation,
the recommended effect is to promote a terminal-height sharp-radial lemma
and `M9-M1-global-radial-interface-estimate` to `proved_internal`, and to
remove that parent from the blocker lists of the radial one-count and GAR
nodes.  Retain `M9-M1-global-lower-radial-signed-estimate` as the sole GAR
analytic blocker.

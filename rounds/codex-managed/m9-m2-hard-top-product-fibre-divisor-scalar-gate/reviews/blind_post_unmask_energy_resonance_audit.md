# Blind post-unmask audit of energy, resonance, and scalar return

## 1. Result

**Verdict: green for the two scoped structural nodes; retain
product_fibre_no_go.**  The revised candidate repairs every seam identified in
the first audit.

The energy estimate (137.C2) is correct.  The fixed-squarefree-kernel estimate
(137.C3) now includes the necessary dyadic-shell lower bound, both \(+1\)
terms, the factorization count, all even/odd cases, and per-incidence
normalization.  The revised resonance statement (137.C12) gives the complete
phase-one classification and correctly proves that a fixed centre has at most
one exact squarefree-kernel channel.  Equations (137.C15)--(137.C17a) give the
lawful stationary map, exact returned profile, and exact normalized Jacobian,
while explicitly retaining every nonprincipal owner.  Equation (137.C18) is
now scoped only as an uncontrolled-complement and circular-route obstruction,
not as theorem equivalence.

These green statements do not prove the target scalar estimate.  They certify
two useful structural nodes and isolate the first missing theorem as a
fixed-centre signed estimate for the literal \(C_L(n)\).

## 2. Exact statement and hypotheses

Use the literal coefficient (137.C4), bounded fixed profiles,
\(h\asymp L\), and the hard cone \(h/4\le m\le h\).  Hence
\(m\asymp L\), \(n=hm\asymp L^2\), and each normalized divisor incidence has
bounded magnitude because \(L^{3/2}n^{-3/4}\asymp1\).

The green arithmetic conclusions are

\[
 \sum_n|C_L(n)|^2\ll L^2\log(2L),
\tag{137.R1}
\]

and, for squarefree \(D>1\),

\[
 \sum_{\substack{n\asymp L^2\\ \operatorname{sf}(n)=D}}
 |B_L(n)|
 \ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{137.R2}
\]

For \(n=Dt^2\), exact phase one is classified by

\[
 e(J\sqrt n)=1
 \quad\Longleftrightarrow\quad
 (J\sqrt D)t\in\mathbb Z.
\tag{137.R3}
\]

Thus \(J\sqrt D=p/q\) in lowest terms gives precisely \(q\mid t\);
irrational \(J\sqrt D\) gives no exact points; and the full channel is phase
one exactly when \(J\sqrt D\in\mathbb Z\), equivalently when \(XD\) is an
integer square.  The candidate's \(X=Ds^2\), \(s\in\mathbb Z\), is correctly
labeled only a sufficient subfamily.

The transform conclusion is limited to the stationary principal family.
Finite endpoints, zero and nonstationary modes, stationary remainders, square
subtraction, support crossings, and the inherited star convention remain with
their prior owners.

## 3. Proof or derivation

**Multiplicative energy.**  Expanding the square and taking absolute values of
bounded profile products reduces to

\[
 h_1m_1=h_2m_2,\qquad h_i\asymp L,\quad m_i\asymp L.
\]

Write \(h_1=ga,h_2=gb\), \((a,b)=1\).  Then
\(m_1=bt,m_2=at\).  If \(M=\max(a,b)\), each of \(g,t\) has
\(O(L/M+1)\) choices and there are \(O(M)\) ordered pairs with maximum \(M\).
Hence candidate (137.C8) expands as

\[
 \begin{aligned}
 \sum_{M\ll L}M\left(\frac LM+1\right)^2
 &=L^2\sum_{M\ll L}\frac1M
   +2L\sum_{M\ll L}1+\sum_{M\ll L}M\\
 &\ll L^2\log(2L).
 \end{aligned}
\tag{137.R4}
\]

Odd \(h_1,h_2\) force \(g,a,b\) odd.  The common parameter \(t\) is even
when the common product is even and odd when it is odd.  Dropping these
restrictions and the cone only enlarges the count; deleting square \(n\)
only removes terms from the nonnegative expanded envelope.  Thus
(137.C6)--(137.C8) prove (137.R1).

**Fixed squarefree kernel.**  With \(g=(h,m)\),
\(h=ga,m=gb\), and \((a,b)=1\), the condition
\(\operatorname{sf}(hm)=D\) gives uniquely

\[
 a=d_1u^2,\qquad b=d_2v^2,\qquad d_1d_2=D,
\tag{137.R5}
\]

where \(d_1,d_2\) are coprime and squarefree.  Since
\(b/a=m/h\in[1/4,1]\), both \(a,b\asymp A\) on one dyadic shell.  For one
ordered factorization,

\[
 \#\{(u,v,g)\}
 \ll
 \left(\sqrt{A/d_1}+1\right)
 \left(\sqrt{A/d_2}+1\right)
 \left(\frac LA+1\right).
\tag{137.R6}
\]

A nonempty shell has \(d_1,d_2\ll A\), so
\(\sqrt D\ll A\ll L\).  Therefore the exact \(+1\)-ledger is

\[
 \begin{aligned}
 \left(\frac A{\sqrt D}+1\right)
 \left(\frac LA+1\right)
 &=
 \frac L{\sqrt D}+\frac A{\sqrt D}+\frac LA+1\\
 &\ll \frac L{\sqrt D}+1.
 \end{aligned}
\tag{137.R7}
\]

There are \(O(\log L)\) shells and
\(2^{\omega(D)}\ll_\varepsilon D^\varepsilon\) ordered factorizations.
Every active \(D\ll L^2\), so these factors are absorbed into
\(L^\varepsilon\), proving the incidence count (137.C11).

The parity ledger at candidate lines 214--217 is complete.  Odd \(h\) forces
\(g,d_1,u\) odd.  If \(D\) is even, its factor \(2\) lies in \(d_2\), hence
on the \(m\)-side.  If \(D\) is odd, an even \(v\) contributes only an even
square factor to \(m\).  Neither case increases the count.  Candidate lines
217--219 then correctly use a bounded *individual incidence*, not a bounded
full coefficient, to deduce (137.R2).

**Exact resonance scope.**  Since \(\sqrt n=t\sqrt D\), (137.R3) is exact.
If two phase-one integers \(n_i=D_it_i^2\) occur at the same centre, then

\[
 \frac{n_1}{n_2}
 =\left(\frac{J\sqrt{n_1}}{J\sqrt{n_2}}\right)^2
\]

is a rational square, forcing \(D_1=D_2\).  Thus every exact nonsquare
phase-one integer at one fixed centre lies in at most one \(D>1\) channel,
and (137.R2) makes the entire exact set target-safe.  Candidate lines
221--244 correctly distinguish this absolute upper bound from a nonzero
asymptotic and from near resonances.

The continuous stationary-mode calculation is separate and also correct.
For \(f(n)=J\sqrt n\),

\[
 n_r=\frac X{4r^2},\qquad
 f(n_r)-rn_r=\frac X{4r},\qquad
 |f''(n_r)|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J}.
\]

The derivative spans \(\asymp J/L\) integers.  The tuned control
\(X=4r^2n_0\) gives both \(f'(n_0)=r\) and
\(f(n_0)=2rn_0\in\mathbb Z\).  Candidate lines 272--275 correctly state that
this formal mode ledger neither proves a nonzero literal coefficient nor
licenses a B-process for the rough \(C_L(n)\).

**Lawful completion.**  Resolve divisibility by

\[
 1_{h\mid n}=\frac1h\sum_{a\bmod h}e(an/h).
\]

For Poisson dual integer \(k\), set \(r=kh-a\).  The map
\((a,k)\mapsto r\) is bijective, and for \(r>0\)

\[
 \phi(x)=J\sqrt x-rx/h,\qquad
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi(x_{h,r})=\frac{Xh}{4r},
\tag{137.R8}
\]

with

\[
 \phi''(x_{h,r})=-\frac{2r^3}{Xh^3}.
\]

Since \(q_X=X/y^2\),

\[
 W\!\left(\sqrt{\frac{q_Xh^2}{4x_{h,r}}}\right)=W(r/y),
 \qquad
 x_{h,r}^{-3/4}|\phi''(x_{h,r})|^{-1/2}=2J^{-1/2}.
\tag{137.R9}
\]

The factor \(1/h\) survives the residue-to-dual bijection, giving exactly the
stationary principal family (137.C17a), including \(e(-1/8)\), character,
Vaaler taper, floor \(y\), star convention, and \(W(r/y)\).  Candidate lines
328--334 explicitly say that this is not an owner-complete finite identity and
list the residual owners.  The algebraic self-return is therefore green
without an overclaim.

**Full-divisor continuation.**  Define, on the same radial support,

\[
 D(n)=\sum_{d\mid n}\chi_4(d)=r_2(n)/4,\qquad
 R_L(n)=D(n)-C_L(n).
\]

Then \(C_L=D-R_L\) is tautological.  Candidate lines 362--368 now make only
the justified claims: \(R_L\) has no proved target-safe estimate; importing
the desired Gauss-circle conclusion to estimate the localized \(D\)-block
would be circular; and an independently proved localized \(r_2\)-estimate
would be admissible new mathematics.  No theorem equivalence is asserted.
The uncontrolled complement prevents this continuation from being a strict
reduction.

## 4. First doubtful or unproved step

There is no residual failed seam inside the two proposed structural nodes.
The first unproved affirmative step is exactly candidate lines 372--390:
passing from (137.C1), the divisor bound, or the positive energy (137.C2) to a
smooth-amplitude or fixed-centre oscillatory estimate.

Cauchy with (137.C2) still has \(L^{2+o(1)}\) capacity.  A
support-, magnitude-, and energy-compatible phase-adapted array shows only
that coefficient-uniform hypotheses are insufficient; candidate lines
382--384 correctly label it a method control, not a physical lower bound.
What remains missing is an additive-twist or equivalent actual-direction
estimate for the literal \(C_L(n)\) saving \(L^{1/2-o(1)}\), without centre
averaging, self-return through (137.C15), or import of the desired
Gauss-circle conclusion.

## 5. Required controls and outcomes

| Control | Verdict and exact outcome |
|---|---|
| literal hard cone and square projection | Green: (137.C5) is exact and squares are removed only through their norm-triangle owner. |
| bounded literal profiles | Green: energy reduces to an incidence envelope; no positivity is used. |
| energy \(+1\)-ledger | Green: (137.R4) includes harmonic, cross, and terminal terms. |
| radical shell ledger | Green: (137.C10a)--(137.C10b) use \(\sqrt D\ll A\ll L\), all \(+1\)'s, all shells, and all ordered factorizations. |
| even/odd radical cases | Green: the factor \(2\) is placed correctly and even square factors are retained. |
| per-incidence normalization | Green: (137.C3) is deduced only after triangle inequality over individual bounded incidences. |
| exact phase-one scope | Green: (137.C12) is complete and all exact points at fixed \(X\) share at most one \(D\). |
| near-resonance scope | Green: no estimate for near collars is inferred from the exact count. |
| continuous stationary modes | Green: (137.C13)--(137.C14) are a coefficient-free capacity ledger only. |
| residue/dual coherence | Green: \(r=kh-a\) is bijective and preserves the \(1/h\) factor. |
| profile and Jacobian | Green: (137.C17) gives \(W(r/y)\) and \(2J^{-1/2}\) exactly. |
| owner-complete self-return | Green scope: only the stationary principal family is asserted; all residual owners are listed. |
| divisor switching | Green: (137.C17b) is an exact involutive reparameterization, not a contraction. |
| full-divisor continuation | Green scope: uncontrolled complement plus route circularity, with independent localized mathematics explicitly allowed. |
| theorem equivalence | Not asserted; no equivalence should be inferred. |
| target estimate | Not proved; product_fibre_no_go remains the correct closure. |

All checks are analytical.  No numerical, symbolic, web, or external-theorem
input is used.

## 6. Dependencies and exact artifacts used

This re-review completely read the revised conductor candidate at observed
SHA-256
381b530b2282ff3eaf0b55211f93371f05b0fabf3c3426f0745cf484976951b7:

- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md.

It also used the previously completely read hostile report:

- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/product_fibre_bprocess_circularity_hostile_audit.md.

The statement-only background remained problems/gauss_circle.md,
state/control_models.md, and
rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/blind_statement.md.
No graph, proof draft, strategy, sibling review, synthesis, or shared state was
read or edited.  Only this existing review file was changed.

## 7. Recommended state effect

Recommend **green** promotion of the two candidate nodes with their present
scope:

- accept (137.C2)--(137.C3), including the exact one-channel phase-one
  corollary but no near-resonance conclusion;
- accept (137.C13)--(137.C17a) as the rough-coefficient capacity ledger and
  stationary-principal self-return, with every listed residual owner retained;
- accept (137.C17b) as an involution, not a contraction;
- accept (137.C18) only as an uncontrolled-complement and circular-route
  warning, not as theorem equivalence;
- retain product_fibre_no_go and require a new fixed-centre signed theorem for
  the exact truncated coefficient.

Reject a target bound, a strict product-fibre reduction, a coefficient-uniform
derivative theorem, centre averaging, full-\(r_2\) replacement, or any
downstream exponent promotion.  The global exponent and all downstream owners
remain unchanged.


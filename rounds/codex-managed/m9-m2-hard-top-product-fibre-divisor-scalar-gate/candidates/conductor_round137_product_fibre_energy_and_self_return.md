# Conductor Round-137 product-fibre energy and self-return candidate

## 1. Result

The exact regrouping

\[
 \mathcal T_L^{\rm ns}
 =\sum_{n\asymp L^2}B_L(n)e(J\sqrt n),\qquad
 B_L(n)=L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square},
\tag{137.C1}
\]

does expose two genuine actual-coefficient facts:

\[
 \sum_n|C_L(n)|^2\ll L^2\log(2L),
\tag{137.C2}
\]

and, for every squarefree \(D>1\),

\[
 \sum_{\substack{n\asymp L^2\\ \operatorname{sf}(n)=D}}
 |B_L(n)|
 \ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{137.C3}
\]

Thus the literal coefficient has an \(L^2\log L\) upper
multiplicative-energy envelope, and
each single squarefree-radical channel—including an exactly phase-one
channel—is target-safe. These facts are not enough for the fixed-centre
target. Cauchy applied to (137.C2) still gives
\(L^{2+o(1)}\), one factor \(L^{1/2-o(1)}\) above the goal, while summing
(137.C3) over all active \(D\) restores \(L^{2+o(1)}\) capacity.

Every audited attempt to extract the missing factor from the scalar
phase either assumes an unavailable additive-twist theorem for the rough
coefficient or self-returns. The formal \(n\)-B-process has \(J/L\)
stationary modes of size \(L^{3/2}/\sqrt J\), hence absolute capacity
\(\sqrt{JL}=L^{3/2}(H/L)\). Making the transform lawful by resolving
\(h\mid n\) returns the original reciprocal hard-TOP phase and the exact
endpoint profile \(W(r/y)\). Divisor switching is involutive, and
completion to \(r_2(n)/4\) adds an uncontrolled complementary divisor
coefficient and enters the circular Hardy--Gauss radial block.

The round therefore closes under product_fibre_no_go. Equations
(137.C2)--(137.C3) are positive structural lemmas, not a target estimate
or a strict smaller scalar survivor.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and fix one literal half-open polynomial intermediate dyadic block
\(1\ll L\ll H\). For odd \(h\), put

\[
 a_{\rm end}(h,m)=
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)
\]

on \(\lceil h/4\rceil\le m\le h\), with zero extension elsewhere.
All three profiles are the fixed bounded project profiles; no positivity
is needed below. Define

\[
 C_L(n)=
 \sum_{\substack{h\mid n,\ h\ {\rm odd}\\
 \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\tag{137.C4}
\]

The support of \(\eta_L\) places \(h\asymp L\), and the affine cone then
places \(m=n/h\asymp L\). The constants in (137.C2) may depend on the
fixed profiles and dyadic support constants, but not on \(X,L\). In
(137.C3), \(\operatorname{sf}(n)\) is the positive squarefree kernel.

The no-go statement is scoped to the following interfaces: direct
first/second derivative estimates, a one-dimensional B-process,
completion of \(h\mid n\), complementary-divisor switching, and
completion to the full \(\chi_4\)-divisor identity. It does not rule out
a new fixed-actual-coefficient theorem for (137.C1).

## 3. Proof or derivation

### Exact dictionary

For \(n=hm\),

\[
 \lceil h/4\rceil\le m\le h
 \quad\Longleftrightarrow\quad
 h\mid n,\quad \sqrt n\le h\le2\sqrt n,\quad m=n/h.
\tag{137.C5}
\]

Indeed \(m\le h\) is \(h\ge\sqrt n\), and \(4m\ge h\) is
\(h\le2\sqrt n\); integrality makes \(4m\ge h\) equivalent to
\(m\ge\lceil h/4\rceil\). Substitution gives (137.C1) and (137.C4)
without averaging a fibre. The square sector is removed only through
the previously proved norm triangle and
\(|\mathcal T_L^\square|\ll L^{5/4}X^\varepsilon\).

### Multiplicative-energy lemma

Suppress bounded weights. Expanding the square on the left of
(137.C2) reduces it to the number \(Q_L\) of solutions

\[
 h_1m_1=h_2m_2,\qquad h_i\asymp L,\quad m_i\asymp L.
\tag{137.C6}
\]

Write \(g=(h_1,h_2)\), \(h_1=ga\), \(h_2=gb\), with
\((a,b)=1\). Equation (137.C6) then forces

\[
 m_1=bt,\qquad m_2=at
\tag{137.C7}
\]

for one positive integer \(t\). If \(M=\max(a,b)\), the support gives

\[
 \#\{g\}\ll L/M+1,\qquad
 \#\{t\}\ll L/M+1.
\]

There are \(O(M)\) ordered pairs \((a,b)\) with
\(\max(a,b)=M\); dropping coprimality only enlarges the count. Hence

\[
 Q_L
 \ll\sum_{M\ll L}M\left(\frac LM+1\right)^2
 \ll L^2\log(2L).
\tag{137.C8}
\]

The odd-height restriction and the cone only decrease this envelope.
Restoring the bounded literal weights proves (137.C2), and the same
bound holds after deleting square \(n\). Since there are \(O(L^2)\)
possible \(n\), (137.C2) and Cauchy yield only

\[
 \left|\sum_nB_L(n)e(J\sqrt n)\right|
 \ll L^{2+o(1)}.
\tag{137.C9}
\]

Thus the new actual-coefficient property does not itself close the
scalar.

### Squarefree-radical channels

Fix squarefree \(D\) and impose \(hm=Dt^2\). With
\(g=(h,m)\), write \(h=ga\), \(m=gb\), \((a,b)=1\). Then
\(\operatorname{sf}(ab)=D\), so uniquely

\[
 a=d_1u^2,\qquad b=d_2v^2,\qquad
 d_1d_2=D,
\tag{137.C10}
\]

where \(d_1,d_2\) are coprime squarefree integers; the odd-height
condition merely restricts these parameters. On a dyadic shell
\(a,b\asymp A\), a fixed ordered factorization \((d_1,d_2)\)
contributes at most

\[
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \left(\frac LA+1\right)
\tag{137.C10a}
\]

triples \((u,v,g)\). A nonempty shell has
\(d_1,d_2\ll A\), hence \(\sqrt D\ll A\ll L\). Therefore

\[
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \ll\frac A{\sqrt D}+1,
\qquad
 \left(\frac A{\sqrt D}+1\right)
 \left(\frac LA+1\right)
 \ll\frac L{\sqrt D}+1.
\tag{137.C10b}
\]

There are \(O(\log L)\) shells and
\(2^{\omega(D)}\ll_\varepsilon D^\varepsilon\) ordered
factorizations; every active \(D\) satisfies \(D\ll L^2\). Summing gives

\[
 \#\{(h,m):h,m\asymp L,\ hm=Dt^2\}
 \ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{137.C11}
\]

Odd \(h=gd_1u^2\) forces \(g,d_1,u\) odd. If \(D\) is even, its
factor \(2\) therefore lies in \(d_2\); if \(D\) is odd, an even
\(v\) contributes only an even square factor to \(m\). Dropping these
parity restrictions only enlarges the count. The normalized
contribution of each individual \((h,m)\)-incidence is bounded, so
(137.C11) proves (137.C3).

More exactly, for \(n=Dt^2\),

\[
 e(J\sqrt n)=1
 \quad\Longleftrightarrow\quad
 (J\sqrt D)t\in\mathbb Z.
\tag{137.C12}
\]

If \(J\sqrt D=p/q\) in lowest terms, the exact points in that channel
are precisely those with \(q\mid t\); if \(J\sqrt D\) is irrational,
there are none. The whole \(D\)-channel is phase one exactly when
\(J\sqrt D\in\mathbb Z\), equivalently \(XD\) is an integer square.
The choice \(X=Ds^2\) with \(s\in\mathbb Z\) is a sufficient
subfamily. If exact phase-one points occur in two channels \(D_1,D_2\)
at the same centre, then
\(D_1t_1^2/D_2t_2^2\) is a rational square, forcing
\(D_1=D_2\). Thus all exact nonsquare phase-one points at one fixed
centre lie in at most one squarefree channel, and (137.C3) makes their
entire absolute capacity target-safe. This is an upper bound, not a
nonzero weighted asymptotic, and it says nothing about near resonances
or the continuous stationary modes. The unresolved issue is
fixed-centre cancellation across the many nonexact or near-resonant
squarefree channels.

### Curvature and exact resonances

For \(f(n)=J\sqrt n\), the integer stationary mode \(r\) has

\[
 n_r=\frac X{4r^2},\qquad
 f(n_r)-rn_r=\frac X{4r},\qquad
 |f''(n_r)|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J}.
\tag{137.C13}
\]

The coefficient-free derivative range spans \(\asymp J/L\) integers on
\(n\asymp L^2\). Thus its formal absolute stationary B-ledger has size

\[
 \frac JL\frac{L^{3/2}}{\sqrt J}
 =\sqrt{JL}
 =L^{3/2}\frac HL,
\tag{137.C14}
\]

up to harmless floor comparability. A uniform first-derivative gap is
false: for any supported nonsquare \(n_0\), the admissible choice
\(X=4r^2n_0\) gives \(f'(n_0)=r\) and
\(e(f(n_0))=1\).

These computations neither assert that every formal mode carries a
nonzero literal coefficient nor authorize a B-process with coefficient
\(C_L(n)\). That coefficient jumps at divisor incidences and moving hard
faces. No bounded-variation or additive-partial-sum estimate is available.

### Lawful completion and self-return

Resolving divisibility before Poisson gives

\[
 1_{h\mid n}=\frac1h\sum_{a\bmod h}e(an/h).
\tag{137.C15}
\]

For dual integer \(k\), put \(r=kh-a\). The stationary phase

\[
 \phi(x)=J\sqrt x-rx/h
\]

satisfies

\[
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi(x_{h,r})=\frac{Xh}{4r},
\tag{137.C16}
\]

and the literal profile and normalized Jacobian obey

\[
 W\!\left(\sqrt{\frac{q_Xh^2}{4x_{h,r}}}\right)=W(r/y),
\qquad
 x_{h,r}^{-3/4}|\phi''(x_{h,r})|^{-1/2}
 =2J^{-1/2}.
\tag{137.C17}
\]

The residue-to-dual map \(r=kh-a\), with \(0\le a<h\), is bijective:
given \(r\), take \(a\equiv-r\pmod h\) and
\(k=(r+a)/h\). Thus the factor \(1/h\) survives, and the stationary
principal family is

\[
 \begin{aligned}
 \mathcal M_L={}&
 2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{h\ {\rm odd}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}\\
 &\times
 \sum_{\substack{r>0\\J/2\le r\le J}}^{\star}
 W(r/y)e\!\left(\frac{Xh}{4r}\right).
 \end{aligned}
\tag{137.C17a}
\]

This is the original reciprocal hard-TOP principal family, with its
phase, character, Vaaler taper, floor \(y\), and endpoint profile
restored. Equation (137.C17a) is not by itself an owner-complete finite
identity. Finite endpoint samples, nonstationary and zero modes,
stationary remainders, square subtraction, support crossings, and the
inherited endpoint convention retain their prior owners. The canonical
calculation is a self-return and supplies no new estimate.

For completeness, if \(n=2^\nu n_{\rm o}\), \(n_{\rm o}\) odd, and
\(d=n_{\rm o}/h\), the exact complementary-divisor substitution is

\[
 \begin{aligned}
 C_L(2^\nu n_{\rm o})={}&\chi_4(n_{\rm o})
 \sum_{\substack{d\mid n_{\rm o}\\
 \frac12\sqrt{n_{\rm o}/2^\nu}\le d\le
 \sqrt{n_{\rm o}/2^\nu}}}
 \chi_4(d)\eta_L(n_{\rm o}/d)
 \Phi\!\left(\frac{n_{\rm o}}{d(H+1)}\right)\\
 &\times W\!\left(
 \sqrt{\frac{q_Xn_{\rm o}}{2^{\nu+2}d^2}}
 \right).
 \end{aligned}
\tag{137.C17b}
\]

It is a lower near-square truncated divisor sum with a transformed
literal height profile and returns to (137.C4) when repeated. Finally,

\[
 C_L(n)=\frac{r_2(n)}4-R_L(n)
\tag{137.C18}
\]

has no proved target-safe error term: \(R_L\) contains every omitted
divisor scale and profile difference. The first term is the full
localized radial Hardy--Voronoi interface. Importing the desired
Gauss-circle conclusion to bound it would be circular; a genuinely
independent localized \(r_2\)-block estimate would be new admissible
mathematics. In either case the uncontrolled \(R_L\) term prevents this
completion from being a strict reduction.

## 4. First doubtful or unproved step

The first invalid affirmative step is to pass from the exact scalar
(137.C1) and the pointwise divisor bound to a smooth-amplitude
first/second derivative or B-process estimate. Neither
\(|C_L(n)|\le\tau(n)\) nor the stronger actual energy (137.C2) controls
the fixed point evaluation

\[
 \sum_nB_L(n)e(J\sqrt n)
\]

at a prescribed real \(J\). A phase-adapted coefficient of the same
support, pointwise size, and \(L^2\)-energy can attain (137.C9); it is a
method control, not the physical coefficient.

The missing statement is an additive-twist or equivalent
fixed-actual-direction estimate for the literal \(C_L(n)\) that saves
\(L^{1/2-o(1)}\), handles all stationary integers in (137.C13), and
does not prove itself by re-expanding (137.C15), by averaging the centre,
or by importing (137.C18) from the Gauss-circle target.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal hard cone and square projection | Exact dictionary (137.C5); square entries removed only through the proved norm triangle. |
| product-fibre coefficient | Literal coefficient retained in (137.C4); no fibre modulus or mean. |
| actual coefficient energy | New bound (137.C2) proved by (137.C6)--(137.C8), but Cauchy still has \(L^2\) capacity. |
| prime and divisor controls | Singleton near-square fibres and same-sign many-divisor fibres preclude automatic internal \(\chi_4\)-cancellation. |
| nonsquare resonance | Exact phase-one channels (137.C12) survive, while (137.C3) proves each fixed channel target-safe. |
| real centre and stationary modes | Exact modes (137.C13) occur for admissible polynomial centres; no uniform nonresonance gap. |
| one-dimensional curvature | Formal capacity (137.C14) is target times \(H/L\). |
| completion and B-process | Divisibility completion gives the exact returned phase, profile, and Jacobian (137.C15)--(137.C17). |
| divisor switching | An involution with unchanged incidence capacity, not a contraction. |
| full-divisor continuation | Split (137.C18) has an uncontrolled complement and a circular full radial term. |
| directionality | Positive energies, phase-adapted arrays, fibrewise moduli, and centre averages are controls only. |
| owner scope | Hard faces, floors, stars, terminal scale, BAL, UNBAL, M9-M1, endpoint assembly, and downstream theorems remain outside this gate. |

## 6. Dependencies and artifacts used

This candidate uses:

1. protocol.md;
2. state/proof_obligations.yml at starting SHA-256
   3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7;
3. state/active_campaign.yml;
4. strategy/conductor_0823_full_proof_strategy.md;
5. rounds/codex-managed/m9-top-endpoint-transform/synthesis.md;
6. rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md;
7. rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md;
8. rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/synthesis.md;
9. rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md;
10. the Round-137 blind statement and the independent blind and hostile
    reports.

No numerical experiment, symbolic experiment, or external theorem import
is used. The elementary counts (137.C8) and (137.C11) are reproduced
here.

## 7. Recommended state effect

Recommend creating two scoped accepted nodes after seam review:

1. M9-M2-hard-top-truncated-divisor-energy-and-radical-control for
   (137.C2)--(137.C3), including the fact that a single exact nonsquare
   radical resonance is target-safe but the sum over radicals is not;
2. M9-M2-hard-top-product-fibre-transform-self-return for
   (137.C13)--(137.C18), recording the rough-coefficient seam, dual
   capacity, lawful reciprocal return, divisor-switch involution, and
   circular full-divisor continuation.

Update the open density-discrepancy parent only by adding these
dependencies and changing its next action to require a fixed-centre
additive-twist theorem for the exact truncated coefficient. Reject a
target bound, strict product-fibre reduction, arbitrary-coefficient
derivative estimate, averaged-centre substitution, full-\(r_2\)
replacement, and any downstream promotion. The global exponent remains
unchanged.

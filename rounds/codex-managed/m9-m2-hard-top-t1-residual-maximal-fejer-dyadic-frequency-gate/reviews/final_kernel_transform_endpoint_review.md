# Round 172 final-kernel transform and endpoint review

- Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate
- Role: independent final-kernel transform/endpoint reviewer
- Kernel reviewed: proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md
- Verdict: **REPAIR (local); transform, zero-mode, and endpoint seams GREEN**

## 1. Result

The durable kernel is mathematically sound at the assigned central seams.
The real-cardinal interpolation is exact on the physical lattice; the
character--ordinary-Poisson constant is \(i/2\); the second-peak parity
twist is \((-1)^{\epsilon m}\); and squaring followed by the two-peak
average gives exactly \(1/8\).  The ordinary-zero-containing sector is
target-safe only after the complete signed odd-character recombination.
The physical zero diagonal is not a fixed dual diagonal, and every hard
endpoint, transition cell, frequency endpoint, and zero-extension piece
remains in the exact aggregate until recombination.

The first open analytic object is (172.K20), the complete signed
\(\ell,\ell'\ne0\) aggregate.  Nothing here proves (165.K26).

Three local repairs are required:

1. Before (172.K15), define \(b_{R,S}(-h)=b_{R,S}(h)\).  At an integer
   \(n\), the displayed kernel first gives \(b_{R,S}(-n)\), equal to
   \(b_{R,S}(n)\) only after that even extension is stated.
2. Narrow lines 497--499 to the centred smooth-interior seam.  The accepted
   collar dependency proves its product count and power ledger for a
   compact smooth interior cell of one fixed opening at \(\phi=0\).  It
   does not give a uniform collar theorem for the complete cardinal family
   on nonzero peak arcs, and it leaves hard endpoints, transitions, and
   collar tails open.
3. Replace \(MD_L\asymp L^4X^\varepsilon\) in the summary by
   \(MD_L\ll_\varepsilon L^4X^\varepsilon\).  The admissible dechirped
   family (172.K22) attains \(MD_L\asymp L^4\), but no lower asymptotic for
   literal residual \(D_L\) is known.

These repairs do not change the route-scoped obstruction or owner boundary.

## 2. Exact statement and hypotheses

Let

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),\qquad N=dm,
\]

where \(\lambda_{dm}(d)\) stores every literal selector, arithmetic hole,
parity branch, hard value, endpoint, transition, and zero-extension value.
On support \(d,m\asymp L\) and \(L^2\le J\).  Choose a real
\(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), and set

\[
 \mathcal W_\epsilon(x,y)=
 \sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)=
 \mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\]

The bump cells lie in \(x,y>0\) and reproduce each ordered physical
divisor incidence exactly once.  This multiplicity statement is before,
not after, an overlapping Möbius opening.

## 3. Proof and derivation

With \(\widehat f(\xi)=\int f(x)e(-\xi x)\,dx\),

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
\]

The \(e(n/4)\) term gives frequencies \((4h-1)/4\), where
\(\chi_4(4h-1)=-1\), and coefficient \(-i/2\).  The \(e(-n/4)\) term
gives \((4h+1)/4\), where \(\chi_4(4h+1)=1\), and coefficient \(i/2\).
Thus

\[
 \sum_n\chi_4(n)f(n)
 =\frac i2\sum_{k\ {\rm odd}}\chi_4(k)\widehat f(k/4).
\]

Ordinary Poisson in the unit-spaced \(m\)-variable adds no factor.  Since
\(d\) is odd, \((-1)^{\epsilon dm}=(-1)^{\epsilon m}\), giving exactly

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{k\ {\rm odd}}\chi_4(k)\sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\]

The parity bandpass is

\[
 \frac12\sum_{\epsilon=0}^1
 \int_0^1(F_S-F_R)(\theta)|Z_\epsilon(\theta)|^2\,d\theta.
\]

Hence its squared transform coefficient is
\(\frac12|i/2|^2=1/8\), with
\(\chi_4(k)\chi_4(k')\) and one outer real part.  The signs and constants
in (172.K13)--(172.K14) are exact.

After evenly extending \(b_{R,S}\),

\[
 \mathscr B_{R,S}(t)=\sum_{h\in\mathbb Z}b_{R,S}(h)
 \int_0^1e((t+h)\theta)\,d\theta.
\]

At integer \(n\) this equals \(b_{R,S}(-n)=b_{R,S}(n)\), so the physical
diagonal has coefficient zero.  For noninteger \(t\),

\[
 \mathscr B_{R,S}(t)=
 \frac{(e(t)-1)(S-R)}{2\pi it}
 -\frac1{2\pi it}\int_0^1B'_{R,S}(\theta)e(t\theta)\,d\theta.
\]

On a nominal dual diagonal the two cardinal variables remain independent,
so \(xy-x'y'\) is generally noninteger.  The physical diagonal therefore
returns only after the complete dual-diagonal/off-diagonal, cell,
frequency-endpoint, transition, and zero-extension recombination.

Recombining all odd \(k\)-modes first gives

\[
 Z_{\epsilon,0}(\theta)=
 \sum_d\chi_4(d)\int_{\mathbb R}
 \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\]

On each compact cell,

\[
 \partial_y(J\sqrt{dy}+\theta dy)\asymp J,\qquad
 \partial_y^2(J\sqrt{dy}+\theta dy)=O(J/L).
\]

One integration by parts costs \(J^{-1}\), with no cell-boundary term.
After epsilon rebudgeting,

\[
 \|Z_{\epsilon,0}\|_\infty\ll_\eta L^2J^{-1}X^\eta.
\]

All terms with \(\ell=0\) or \(\ell'=0\), combined before taking a norm,
are therefore

\[
 \ll (R+S)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\]

This is collective in \(k\), never termwise.  Compact bump boundaries
vanish only in this integration by parts; every literal hard endpoint,
transition, nonzero ordinary mode, and zero-extension jump stays in
(172.K20).

At a centred peak,
\[
 \Phi_0(u,v)=J\sqrt{uv}-\xi u-\eta v
\]
has rank-one Hessian.  With \(\xi=k/4\), \(\eta=\ell\), its stationary
equations give \(k\ell=X\), and after a fixed \((Q,R)\) opening give the
accepted \(k\ell=XQR\) collar.  At the second peak,
\(e(N/2)=(-1)^N=(-1)^m\) is absorbed exactly into the amplitude.  Thus
both **centres** have the accepted rank-one geometry.  This blocks deletion
of either centre and any uniform nondegenerate-Hessian claim, but the
accepted dependency does not extend its smooth-cell collar ledger to the
whole cardinal/endpoint family.

## 4. First doubtful or unproved step

The first unproved affirmative estimate is

\[
 \mathcal N_{R,S}\ll_\varepsilon L^3X^\varepsilon
\]

for the signed aggregate (172.K20), or a stopped-chain estimate using
cancellation between links.  All odd character modes, nonzero ordinary
modes, both peak gauges, cardinal cells, arithmetic openings, endpoints,
transitions, and zero-extension pieces must remain before positivity.

The first doubtful sentence is lines 497--499.  Read as a claim for the
entire cardinal/endpoint family or a nonzero peak arc, it exceeds the two
accepted dependencies.  Read only as a centred smooth-interior structural
return, it is correct.

## 5. Required controls and outcomes

| Seam | Outcome |
|---|---|
| cardinal interpolation | **GREEN**: exact at every integer incidence |
| character/ordinary Poisson | **GREEN**: \(i/2\), odd \(k\), no ordinary factor |
| parity twist | **GREEN**: \((-1)^{\epsilon N}=(-1)^{\epsilon m}\) |
| squared bandpass | **GREEN**: \(1/8\) |
| continuous bandpass notation | **REPAIR**: state even extension of \(b_{R,S}\) |
| physical versus dual diagonal | **GREEN**: full recombination required |
| ordinary-zero sector | **GREEN collectively** at \(L^3X^\varepsilon\) |
| endpoints/transitions | **GREEN as retained data**, not separately safe |
| both centred peaks | **GREEN**: rank one at \(\phi=0\) |
| full-family collar return | **REPAIR scope**: only centred smooth interior is accepted |
| positive capacity | **GREEN after wording repair**: upper capacity \(L^4X^\varepsilon\), attained by the admissible diagnostic family |
| first open seam | **GREEN**: (172.K20) |

No external theorem is used.

## 6. Dependencies and exact artifacts used

The review used protocol.md; state/proof_obligations.yml;
state/active_campaign.yml; the durable kernel; the two listed accepted
dependency kernels; the formalized candidate; the repaired discovery and
hostile reports; the transform verification reviews; and the conductor
controls.  No graph, state, synthesis, validation, or kernel file was
edited.

## 7. Recommended state effect

Apply the three local repairs in Section 1, then mark this seam **GREEN**.
The repaired kernel supports one residual-only, route-scoped
positive-transform obstruction node.  It supports no separate endpoint or
strict-sector owner, no proof of (172.K20) or (165.K26), and no hard-TOP
parent, M9--M2, M9, bridge, theorem, or exponent promotion.

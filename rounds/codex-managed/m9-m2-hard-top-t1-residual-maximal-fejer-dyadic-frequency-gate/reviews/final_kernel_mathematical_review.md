# Round 172 final-kernel mathematical review

- Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate
- Role: independent line auditor of the conductor-selected durable kernel
- Kernel: proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md
- Starting graph: c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853
- Verdict: **GREEN after three local repairs, all rechecked; no outstanding mathematical or scope repair**

## 1. Result

The current selected kernel agrees with the repaired discovery and hostile
reports, the formalized candidate, and all Round-172 seam reviews on every
substantive identity and implication.

The line audit verifies:

1. the stopped parity--Fejer telescope, the minus sign of the one short
   correction, \(b_{R,S}\), the doubling tent, the absolute-site-parity
   Haar identity, and the first-link power;
2. physical divisor-incidence multiplicity one, absolute convergence of
   the cardinal transform, character factor \(i/2\), and squared
   parity-average factor \(1/8\);
3. the collectively recombined ordinary-zero sector and its
   \(L^3X^\varepsilon\) power;
4. the noninteger product-difference kernel and the distinction between
   physical and dual diagonals;
5. the exact H15 value \(P^2=MD/8\) and its admissible scale subfamily; and
6. the Hessian determinant at both centred Fejer peaks and the
   dependency-scoped collar return.

During the audit, three local issues were found.  The conductor applied all
three, and this review rechecked the resulting file:

1. Before (172.K15), \(b_{R,S}\) is now explicitly extended evenly to
   negative integers.  This closes the former definition gap between
   positive \(r\) in (172.K7) and \(h\in\mathbb Z\) in (172.K15).
2. The current result summary, capacity paragraph, and power ledger now
   distinguish
   \[
     MD_L\ll_\varepsilon L^4X^\varepsilon
   \]
   from sharpness at order \(L^4\) on the diagnostic family.  The literal
   residual hypotheses do not assert \(D_L\asymp L^2X^\varepsilon\).
3. After (172.K19), \(\eta\) is now chosen sufficiently small in terms of
   the requested \(\varepsilon\), correctly absorbing \(X^{O(\eta)}\).

No factor, sign, endpoint, transform, H15, Hessian, or owner-scope repair
remains.

## 2. Exact statement and hypotheses audited

Let
\[
 C_r=\sum_Nz_{N+r}\overline{z_N},\qquad
 A_r=\Re C_r,\qquad D_L=C_0,
\]
where the complete literal residual sequence is extended by zero on an
\(M\)-site containing interval.  The audited range is
\[
 R_0=\lceil L\rceil,\qquad M\asymp L^2,\qquad
 D_L\ll_\eta L^2X^\eta,\qquad L^2\le J=\sqrt X,
\]
with \(d,m\asymp L>0\) on every cardinal cell.

The durable claim is route-scoped.  The finite parity--Fejer reduction,
the exact cardinal character--Poisson transform, and the collectively
recombined ordinary-zero estimate are proved.  The fully signed nonzero
ordinary-frequency aggregate remains open.  A positive majorant which
must work coefficient-uniformly before a new literal-symbol saving has
available scale \(MD_L\), and an in-range diagnostic attains order \(L^4\).
This is not literal residual mass and neither proves nor disproves
(165.K26).

## 3. Independent derivation

### 3.1 Stopped chain, short sign, \(b_{R,S}\), and first link

Parity averaging keeps precisely even gaps:
\[
 \mathfrak E_R^{(2)}
 =D_L+2\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r.
\]
If
\[
 \mathcal A_R=\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r,
\]
then
\[
 \mathcal A_M-\mathcal A_{R_0}
 =T_{26}+
 \sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)A_r.
\]
This proves both the factor \(1/2\) and the minus sign in (172.K5).
Since \(|C_r|\le D_L\), the one correction is
\(O(R_0D_L)=O_\varepsilon(L^3X^\varepsilon)\).

For integers \(R<S\le2R\), direct subtraction gives
\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
 \qquad b_{R,S}(0)=0,
\]
and
\[
 \sum_{r=1}^{S-1}b_{R,S}(r)=\frac{S-R}{2}.
\]
Hence
\[
 |\mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}|
 \le2D_L\sum_{\substack{r>0\\2\mid r}}b_{R,S}(r)
 \le(S-R)D_L.
\]
With \(S=\min(2R_0,M)\), this proves the first-link bound including the
terminal non-doubling case.  It gives no target-safe complement.

### 3.2 Haar parity and normalization

For
\[
 Y_{s,R}^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j},
\]
full-line pair counting yields
\[
 \mathfrak E_R^{(2)}
 =\frac1R\sum_{s,\epsilon}|Y_{s,R}^{(\epsilon)}|^2.
\]
Absolute site parity remains the same in the adjacent block beginning at
\(s+R\), even for odd \(R\).  The parallelogram identity therefore gives
\[
 \mathfrak E_{2R}^{(2)}
 =2\mathfrak E_R^{(2)}
 -\frac1{2R}\sum_{s,\epsilon}
 |Y_{s,R}^{(\epsilon)}-Y_{s+R,R}^{(\epsilon)}|^2.
\]
Thus the \(1/(2R)\) normalization in (172.K10) is exact and the formula
is correctly restricted to doublings.  A strict final link uses
\(b_{R,S}\), not Haar rounding.

### 3.3 Cardinal interpolation, convergence, multiplicity, and constants

The bump support lies strictly inside one lattice cell.  Exactly one
cardinal cell contributes at each integer pair, so each ordered physical
incidence \((d,m=N/d)\) occurs once.  This statement is not transferred to
a later overlapping Möbius inclusion--exclusion opening.  Since \(d\) is
odd,
\[
 (-1)^{\epsilon N}=(-1)^{\epsilon dm}=(-1)^{\epsilon m}.
\]

For the kernel's Fourier convention, direct Poisson reindexing gives
\[
 \sum_n\chi_4(n)f(n)
 =\frac i2\sum_{k\ {\rm odd}}\chi_4(k)\widehat f(k/4).
\]
Ordinary Poisson in the second variable has no further scale factor.
Therefore (172.K13) has factor \(i/2\).  Squaring contributes \(1/4\),
and the two-peak parity average contributes \(1/2\), giving exactly
\(1/8\) in (172.K14).

The interpolation is a finite sum of compactly supported smooth cells in
\(x,y>0\).  Repeated integration by parts gives rapid decay in
\((k,\ell)\), uniformly for \(0\le\theta\le1\).  Thus the dual series,
their product series, and the common-frequency integral are absolutely
convergent, validating all rearrangements.

### 3.4 Noninteger kernel and the two diagonals

With the now-explicit even extension,
\[
 \mathscr B_{R,S}(t)
 =\sum_{h\in\mathbb Z}b_{R,S}(h)I(t+h).
\]
For integer \(n\), only \(h=-n\) survives, so the value is
\(b_{R,S}(-n)=b_{R,S}(n)\); the physical diagonal has coefficient zero.
Integration by parts gives
\[
 \mathscr B_{R,S}(t)
 =\frac{(e(t)-1)(S-R)}{2\pi it}
 -\frac1{2\pi it}\int_0^1B'_{R,S}(\theta)e(t\theta)\,d\theta,
\]
because \(B_{R,S}(0)=B_{R,S}(1)=S-R\).

On a nominal dual diagonal the two cardinal variables remain independent,
so \(t=xy-x'y'\) need not be integral.  The kernel correctly retains the
dual off-diagonal, cardinal cells, frequency endpoints, physical
endpoints, transitions, and zero-extension pieces until recombination.

### 3.5 Ordinary-zero recombination and powers

Only after summing all signed odd character modes does the ordinary-zero
component become
\[
 Z_{\epsilon,0}(\theta)
 =\sum_d\chi_4(d)\int\mathcal B_{\epsilon,\theta}(d,y)\,dy.
\]
On every supported cell,
\[
 p'(y)=\frac J2\sqrt{d/y}+\theta d\asymp J,\qquad
 p''(y)=O(J/L).
\]
The bump kills boundary terms, so one integration by parts costs
\(O(J^{-1})\) per weighted incidence.  After epsilon rebudgeting,
\[
 \|Z_{\epsilon,0}\|_\infty
 \ll_\eta L^2J^{-1}X^\eta.
\]

All terms with \(\ell=0\) or \(\ell'=0\) recombine to
\[
 |Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}}).
\]
Using \(|B_{R,S}|\le R+S\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), and \(L^2\le J\), their total is
\[
 \ll(R+S)
 \left(D_L^{1/2}\frac{L^2}{J}
       +\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\]
This is collective in \(k,k'\), not a termwise \(k\)-estimate, and is
distinct from the Round-169 scalar zero mode.

### 3.6 Exact H15 value and admissible subfamily

Let \(M=4P\) and put \(z_N=1\) on the \(2P\) sites of one absolute parity
class.  Then \(D=2P\), \(A_{2s}=2P-s\), and for the full-energy link
\(2P\to4P\),
\[
 \begin{aligned}
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}
 &=\frac1P\left(
 \sum_{s=1}^{P-1}s(2P-s)
 +\sum_{s=P}^{2P-1}(2P-s)^2\right)\\
 &=P^2=\frac18MD.
 \end{aligned}
\]
The full-energy factor \(2\) is included, and all \(2P\) parity sites fit
inside the \(M\)-site interval.  A positive even translate makes every
square root lawful, while \(c_N=e(-J\sqrt N)\) dechirps the phase.

Taking \(L\) through powers of two,
\[
 M=L^2,\quad P=L^2/4,\quad X=L^8,\quad J=L^4,\quad H=L^2,
\]
gives \(R_0=L\), places \(M/2\to M\) in the stopped chain, and satisfies
\(1\ll L\ll H\le J^{1/2}\).  For fixed
\(0<\varepsilon_0<1/8\), the diagnostic-to-target ratio is a nonzero
constant times \(L^{1-8\varepsilon_0}\to\infty\).  This proves sharpness
for the coefficient-uniform positive interface, not a physical residual
lower bound.

### 3.7 Both peaks and collar Hessian

For
\[
 \Phi_\phi(u,v)=J\sqrt{uv}+\phi uv-\xi u-\eta v,
\]
direct differentiation gives
\[
 \Phi_{uu}=-\frac J4v^{1/2}u^{-3/2},\quad
 \Phi_{vv}=-\frac J4u^{1/2}v^{-3/2},\quad
 \Phi_{uv}=\frac J{4\sqrt{uv}}+\phi,
\]
and hence
\[
 \det\operatorname{Hess}\Phi_\phi
 =-\phi^2-\frac{J\phi}{2\sqrt{uv}}.
\]
At \(\phi=0\) the Hessian is nonzero of rank one.  At the second peak,
the exact gauge \((-1)^N=(-1)^m\) moves into the amplitude and leaves the
same centred phase.  A top doubling bandpass has scale-size height on
arcs of width \(c/M\), and \(\phi uv=O(1)\) there because
\(uv\asymp L^2\asymp M\).  Deleting either centre or claiming a uniform
nondegenerate two-dimensional gain is invalid.  Positive simultaneous
dualization returns to the accepted product collar; this is a
dependency-scoped route statement, not physical mass.

## 4. First doubtful or unproved step

The first unproved step is exactly the complete one-real-part aggregate
(172.K20), with \(k,k'\) odd, \(\ell,\ell'\ne0\), and every cell,
arithmetic opening, endpoint, transition, and cross term retained before
positivity.

A one-sided \(O_\varepsilon(L^3X^\varepsilon)\) bound for every remaining
link would suffice.  An absolute link theorem would be stronger, and even
a linkwise one-sided theorem is not logically necessary because
cross-link cancellation remains possible.  The kernel correctly proves
neither version and does not claim (165.K26).

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| stopped chain and short-correction sign | **GREEN** |
| \(b_{R,S}\), tent, zero diagonal, final link | **GREEN** |
| first-link power | **GREEN**, with no owner-complete complement |
| absolute-site-parity Haar normalization | **GREEN**, doublings only |
| cardinal multiplicity and absolute convergence | **GREEN** |
| character and parity constants | **GREEN**: \(i/2\) and \(1/8\) |
| ordinary-zero collective recombination | **GREEN** |
| ordinary-zero restored power | **GREEN** |
| noninteger kernel and diagonal distinction | **GREEN** |
| exact H15 value | **GREEN**: \(P^2=MD/8\) |
| H15 support and scale subfamily | **GREEN** |
| actual/adversarial distinction | **GREEN** |
| both peak gauges and Hessian | **GREEN** |
| positive collar return | **GREEN** as a scoped no-go |
| \(MD_L\) power language | **GREEN**: upper scale plus diagnostic sharpness |
| signed nonzero aggregate | **OPEN** |
| (165.K26), parents, bridge, theorem, exponent | **NO CHANGE** |

No numerical experiment, web source, or external theorem was used.

## 6. Dependencies and exact artifacts used

This audit used protocol.md; state/proof_obligations.yml;
state/active_campaign.yml; the selected durable kernel; the formalized
candidate; all three repaired Round-172 reports; the parity, transform,
power/owner, and both post-repair reviews; the conductor controls; and the
two accepted dependency kernels named by the selected kernel.

## 7. Recommended state effect

**Treat the current repaired kernel as GREEN.**  The supported durable
effect remains exactly one proved-internal, residual-only obstruction node:

M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction.

It should have no implication edge.  Do not create separate first-link or
ordinary-zero owners.  Retain (172.K20), (165.K26), the residual \(t=1\)
scalar, every other hard-TOP channel, BAL, UNBAL, M9--M2, direct M1, GAR,
endpoint assembly, M9, both bridges, and the quarter theorem in their
current states.  The internal \(1/3\) exponent, accepted external Li--Yang
benchmark \(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

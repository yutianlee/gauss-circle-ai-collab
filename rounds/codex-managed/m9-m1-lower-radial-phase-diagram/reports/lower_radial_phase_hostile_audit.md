# Round 61 independent hostile/source audit: lower radial phase diagram

## 1. Result

The exponent substitution is exact, but the apparent radial gain from
optimizing over the denominator scale is false.  For a fixed smooth
radial block \(n\asymp X^\nu\), the contributing denominator exponents
are
\[
 {1-\nu\over2}\le\delta\le{1\over2},\qquad
 \ell=\delta+{\nu-1\over2}.
 \tag{61.H1}
\]
The inequality at the left end points toward larger \(\delta\), not
smaller \(\delta\).

After substitution, the TTY target wedge is
\[
 1816\delta+89\nu\le552.
 \tag{61.H2}
\]
It meets the actual range (61.H1) only when
\[
 \nu\ge\nu_{\rm TTY}:={356\over819}.
 \tag{61.H3}
\]
For \(\nu_{\rm TTY}<\nu<1/2\), it closes only the lower-\(\delta\)
subinterval
\[
 {1-\nu\over2}\le\delta\le
 {552-89\nu\over1816};
 \tag{61.H4}
\]
it never closes the unavoidable top scale \(\delta=1/2\).

Consequently the exact all-scale conclusion from the accepted menu is:
\[
 \boxed{\text{fully closed radial exponents are }\nu=0
 \text{ and }\nu=1/2\text{ only}.}
 \tag{61.H5}
\]
The endpoint \(\nu=0\) is closed by the accepted V2 point, because its
entire actual scale range collapses to \(\delta=1/2,\ell=0\).
The endpoint \(\nu=1/2\) is terminal at every scale and is also covered
by Round 60.  Every fixed \(0<\nu<1/2\) has an uncovered top block.
Thus the first uncovered band is the whole open interval
\((0,1/2)\): there is no smallest positive uncovered exponent, and
descending from the critical exponent the obstruction appears
immediately below \(1/2\).  The number \(356/819\) is only the onset of
one-scale TTY coverage, not a radial-sector threshold.

## 2. Exact statement and hypotheses

Let \(V\) be a fixed smooth cutoff supported where
\(n/N\) lies in a compact subset of \((0,\infty)\), with
\(N=X^\nu\), \(0\le\nu\le1/2\).  On an accepted denominator profile
\(d\asymp D=X^\delta\), \(1/4\le\delta\le1/2\), the stationary relation
is
\[
 n={4Xh^2\over d^2},\qquad
 h={d\sqrt n\over2\sqrt X}.
 \tag{61.H6}
\]
Define
\[
 L={D\sqrt N\over2\sqrt X},\qquad
 \ell=\log_XL=\delta+{\nu-1\over2},
 \]
where the constant \(1/2\) has no exponent.  Actual profile support
forces \(h\asymp_VL\).

At exponent level, a contribution exists only when \(L\gg1\), with the
boundary \(L=O(1)\) treated as a bounded-frequency block.  Since
\[
 H_D=\lfloor D/R\rfloor,\qquad R=X^{1/4},
 \]
the formal conditions \(1\le L\le H_D\) become
\[
 \delta\ge{1-\nu\over2},
 \qquad
 \nu\le{1\over2}.
 \tag{61.H7}
\]
Because \(0\le\nu\le1/2\), the first lower bound already implies
\(\delta\ge1/4\).  Hence (61.H1) is the exact exponent range.  At its
left boundary \(h=O(1)\); exact occurrence can depend on the fixed
support constants and integer floors, but any occurring terms form a
bounded-frequency block.  An \(O(1/\log X)\) displacement caused by a
fixed dyadic/profile constant does not create a different power region.

The accepted blockwise bounds, after insertion of (61.H1), are:
\[
\begin{aligned}
 E_{\rm term}(\nu)&={1-\nu\over2},
 \\[2mm]
 E_{\rm TTY}(\delta,\nu)
 &= {908\delta+\frac{89}{2}(1+\nu)\over1282},
 \\[2mm]
 E_{\rm V2}(\delta,\nu)
 &=\min\left\{\delta,{1+\nu\over4}\right\}.
\end{aligned}
\tag{61.H8}
\]
Here \(B(D,L;X)\ll X^{E+\varepsilon}\), and the physical target is
\(E\le1/4\).  The last line records the accepted full V2 estimate
\(\min(D,\sqrt{LX/D})\); it reaches the target in the present diagram
only at the already known endpoints.

For \(0\le\nu<1/2\), the exact residual set relative to the accepted
terminal, TTY, and V2 target regions is
\[
 \mathcal U_{\rm rad}
 =
 \left\{(\nu,\delta):
 {1-\nu\over2}\le\delta\le{1\over2},\
 1816\delta+89\nu>552\right\}
 \setminus\left\{\left(0,{1\over2}\right)\right\}.
 \tag{61.H9}
\]
The line \(\nu=1/2\) is excluded because it is terminal, regardless of
the TTY inequality.

## 3. Proof and inequality audit

Equation (61.H6) immediately gives \(h\asymp L\) and (61.H1).  The
upper Vaaler condition is worth checking independently:
\[
 {L\over D/R}={1\over2}X^{\nu/2-1/4}.
\]
It is \(O(1)\) exactly for \(\nu\le1/2\), and it tends to zero when
\(\nu<1/2\).  Thus lower radial blocks are subterminal, not
superterminal.

The terminal line satisfies
\[
 \delta+{\nu-1\over2}=\delta-{1\over4}
 \quad\Longleftrightarrow\quad \nu={1\over2}.
\]
Equivalently, the terminal bound is
\[
 1+{D\over L}\ll X^\varepsilon+
 X^{(1-\nu)/2},
\]
which is \(O(RX^\varepsilon)\) only at \(\nu=1/2\).
This proves the terminal translation in both directions.

For TTY,
\[
\begin{aligned}
 178\ell+1638\delta\le463
 &\Longleftrightarrow
 178\left(\delta+{\nu-1\over2}\right)
 +1638\delta\le463\\
 &\Longleftrightarrow
 1816\delta+89\nu\le552.
\end{aligned}
\]
The direction remains \(\delta\le(552-89\nu)/1816\).  This upper
bound meets the actual lower bound only if
\[
 {1-\nu\over2}\le{552-89\nu\over1816}
 \quad\Longleftrightarrow\quad
 \nu\ge{356\over819}.
\]
At equality the sole exponent point is
\[
 \nu={356\over819},\qquad
 \delta={463\over1638},\qquad \ell=0.
\]
Above it, (61.H4) is the TTY-covered scale interval.  Below it, TTY
closes no actual scale.

The V2 point translates as
\[
 \delta={1\over2},\quad
 0=\ell={1\over2}+{\nu-1\over2}={\nu\over2},
\]
so \(\nu=0\).  Conversely, at \(\nu=0\), (61.H1) forces
\(\delta=1/2\).  Exact dyadic profiles may leave a fixed finite family
of scales \(D\asymp\sqrt X\), but all have this exponent and the
accepted V2 estimate is uniform for those fixed profile ratios,
including the hard top.  Hence V2 closes the entire \(\nu=0\) sector,
not merely one among many power-separated scales.

For \(0<\nu<1/2\), the top profile produces
\[
 D\asymp X^{1/2},\qquad L\asymp X^{\nu/2};
\]
this is an actual scale, not an optional optimizer.  It is neither
terminal nor the V2 point, and
\[
 1816(1/2)+89\nu>552,
\]
so it is outside TTY.  This proves (61.H5) and refutes any argument that
projects the existence of one TTY-covered \(\delta\) onto the whole
radial block.

More explicitly, the blockwise phase diagram is:

- \(0<\nu<356/819\): every actual scale is uncovered;
- \(\nu=356/819\): only the bounded-frequency lower endpoint is TTY
  covered; every larger \(\delta\) is uncovered;
- \(356/819<\nu<1/2\): (61.H4) is covered and
  \(( (552-89\nu)/1816,\,1/2]\) is uncovered;
- \(\nu=0\): the sole exponent scale is V2-covered;
- \(\nu=1/2\): every scale is terminal-covered.

The projection of the TTY-covered set onto the \(\nu\)-axis is therefore
\([356/819,1/2]\), whereas the projection of the residual set is
\((0,1/2)\).  The former is an existence-of-a-scale statement; the
latter is the relevant all-scale obstruction.

## 4. First doubtful or unproved step

The first invalid prospective step is “optimize over \(\delta\)” by
choosing a TTY-covered denominator scale and then declaring the radial
block closed.  The exact angular coefficient is a sum over every actual
dyadic denominator profile.  No accepted identity projects the radial
block onto a chosen \(D\), and no accepted cross-scale cancellation
allows the other profiles to be discarded.  A blockwise proof must
cover all of (61.H1); an aggregate proof must retain their signed
one-count sum.  TTY provides neither.

The sharp remaining sufficient blockwise statement is
\[
 B_{V,N}(D;X)\ll_{\varepsilon,V}RX^\varepsilon
\tag{61.H10}
\]
uniformly for \((\nu,\delta)\in\mathcal U_{\rm rad}\), with the actual
Vaaler coefficient, profile, hard top, floors, and signs.  An aggregate
estimate over all residual \(j\) would also suffice, but is not supplied
by the phase diagram.

At the unavoidable top scale the best accepted exponent from the
terminal and V2 bounds is
\[
 {1\over4}+
 \sigma_{\rm top}(\nu),\qquad
 \sigma_{\rm top}(\nu)
 =\min\left\{{\nu\over4},{1-2\nu\over4}\right\}>0
 \quad(0<\nu<1/2).
\tag{61.H11}
\]
TTY is weaker there.  Thus any all-scale blockwise closure must save at
least the factor \(X^{\sigma_{\rm top}(\nu)}\) on this top block.  For a
general residual block, the gap of each accepted estimate above the
target is
\[
\begin{aligned}
 \sigma_{\rm term}&={1-2\nu\over4},\\
 \sigma_{\rm TTY}&={1816\delta+89\nu-552\over2564},\\
 \sigma_{\rm V2}&=\min\left\{\delta-{1\over4},{\nu\over4}\right\}.
\end{aligned}
\tag{61.H12}
\]
The required improvement over the best current blockwise estimate is
the minimum of these positive gaps.  This quantifies the missing saving;
it does not prove it.

## 5. Control tests and outcomes

| Control | Check | Outcome |
|---|---|---|
| Stationary exponent map | Solve \(n=4Xh^2/d^2\) for \(h\), retaining the factor \(2\). | Pass: (61.H6) gives \(\ell=\delta+(\nu-1)/2\); the factor \(2\) affects constants only. |
| Active support | Combine \(h\ge1\), \(h\le H_D\), and \(1/4\le\delta\le1/2\). | Pass: actual exponents satisfy (61.H1), with lower inequality \(\delta\ge(1-\nu)/2\). |
| Floors and small height | Test \(L=O(1)\), \(H_D=O(1)\), and \(H_D=0\). | Pass with scoped conventions: bounded \(L\) is treated directly, bounded positive \(H_D\) by the accepted uniform estimates, and \(H_D=0\) has no active Vaaler frequency. |
| Terminal translation | Substitute the map into \(L\asymp H_D\) and into \(1+D/L\). | Pass: both give only \(\nu=1/2\). |
| TTY translation | Check arithmetic and inequality direction. | Pass: the exact condition is (61.H2), an upper bound on \(\delta\), with onset \(356/819\). |
| V2 translation | Map \((\delta,\ell)=(1/2,0)\). | Pass: it is exactly \(\nu=0\), whose scale interval collapses to the top exponent. |
| Union over \(\delta\) | Distinguish existence of one covered scale from coverage of every scale. | Hostile failure of the optimistic interpretation: TTY has some scale only for \(\nu\ge356/819\), but no subcritical positive \(\nu\) is all-scale covered. |
| Scale sum | Count dyadic denominator and frequency pieces. | Pass: there are \(O(\log X)\) scale pieces and \(O(1)\) matched frequency shells per \(D\); triangle summation costs only \(X^\varepsilon\) once every piece is target-bounded. |
| Transform errors | Retain radial multiplier, hard top, profile edges, and stars. | Pass for fixed smooth \(V\): normalized multiplier seminorms are uniform on matched \(D,L,N\), accepted errors sum polylogarithmically, and division by the unchanged external \(R\) is safe. |
| First uncovered band | Find the radial projection of (61.H9). | Pass: it is exactly \(0<\nu<1/2\), with no positive first point. |
| Required saving | Compare the best accepted top-scale bound to \(R\). | Pass: the strict gap is (61.H11), and the full residual ledger is (61.H12). |
| Downstream scope | Test implications for full GAR, M9-M1, M9, or the exponent. | Fail: the diagram is a reduction and no new estimate on \(\mathcal U_{\rm rad}\) has been proved. |

The hard top \(d=\lfloor\sqrt X\rfloor\), its one-sided boundary, and
stationary equality stars remain owned by the accepted transforms.  A
smooth radial cutoff creates no new sharp radial endpoint.  For
\(\nu<1/2\), its support is eventually separated from the product
endpoint \(16\sqrt X\).

## 6. Dependencies and source scope

This audit used only the permitted artifacts:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-lower-radial-phase-diagram/derivation_packet.md;
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/synthesis.md;
- rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md; and
- sources/tao_trudgian_yang_2025.md.

The TTY use stays within the accepted source card.  After resolving
\(\chi_4\) into the two odd residue classes, the inner phase is the
reciprocal model with interval length \(D\) and phase parameter
\(\mathscr T\asymp hX/D\).  Its required range satisfies
\[
 {\mathscr T\over D}\asymp {hX\over D^2}
 =X^{(1+\nu)/2-\delta}\ge1
\]
on (61.H1).  A Mellin separation of the fixed smooth radial multiplier
produces \(h^{2it}\) and \(d^{-2it}\).  Their normalized discrete-BV
cost is polynomial in \(1+|t|\), which is integrable against the
Schwartz Mellin transform.  Thus the fixed-BV weighted transfer is
lawful per dyadic scale, including the accepted one-sided hard profile.
It does not authorize arbitrary bounded denominator weights, a joint
unseparated \(h,d\) selector, or an estimate outside (61.H2).

No new external theorem, web search, or numerical experiment was used.

## 7. Recommended state effect

Promote the exact radial phase-diagram reduction (61.H1)--(61.H9),
including the TTY onset
\(\nu_{\rm TTY}=356/819\), but record explicitly that this onset is only
partial scale coverage.  Record the all-scale no-go: the accepted
terminal/TTY/V2 menu closes exactly the two radial endpoints
\(\nu=0,1/2\), while every \(0<\nu<1/2\) retains at least the top
denominator block.

Retain the lower-radial estimate, full GAR, M9-M1, M9, and the
Gauss-circle exponent as open.  The next admissible proof target is
either the uniform residual theorem (61.H10) or an exact signed
aggregate over the residual scales.  Do not promote a claimed radial
threshold at \(356/819\), do not reverse the active-support inequality,
and do not infer all-scale closure from one TTY-covered denominator
scale.

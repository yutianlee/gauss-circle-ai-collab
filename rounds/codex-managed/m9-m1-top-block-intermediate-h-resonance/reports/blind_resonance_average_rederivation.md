# Blind rederivation: discrete curvature and fixed-\(h\) resonance averaging

## 1. Result

**Discrete-resonance interface with a positive-majorant no-go.** Let
\(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and let \(J\) be any inherited
product window of length at most \(R\). After splitting \(q=4m+\rho\),
\(\rho\in\{1,3\}\), the exact phase

\[
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)}
\]

has

\[
 \Delta ^2F_{h,\rho}(m)\asymp-{h^2\over R},\qquad
 \Delta ^3F_{h,\rho}(m)\asymp {h^3\over R^3}.                \tag{1}
\]

Consequently the discrete curvature on one fixed-\(h\) fiber is nearly
constant: over \(M_h\ll R/h+1\) samples its drift is
\(O(h^2/R^2)\).

For a base sample \(m_0\), put

\[
 \alpha_{h,\rho}(J)=\Delta ^2F_{h,\rho}(m_0)\pmod 1.          \tag{2}
\]

For a Fejer lag \(r\), the exact resonance tested by the differenced phase
is

\[
 \|r\alpha_{h,\rho}(J)\|_{\mathbb R/\mathbb Z}
 \ \lesssim\ r{h^2\over R^2}.                               \tag{3}
\]

Away from (3), discrete Kusmin--Landau applied to
\(F(m+r)-F(m)\) gives the correlation bound in (17) below. Equations
(15)--(21) constitute a legal curvature-resonance interface, including
the rational-approximation dependence and the exact moving fiber edges.

This interface cannot prove the desired aggregate by summing a nonnegative
majorant over \(h\). On a dyadic block \(h\asymp H\), put

\[
 M\asymp {R\over H}.
\]

Even if every nonresonant fixed-\(h\) sum enjoyed ideal square-root
cancellation, the diagonal in any termwise-absolute Fejer/Weyl majorant
costs at least \(\sqrt M\) per nonempty fiber. Its dyadic aggregate has
capacity

\[
 H\sqrt M=\sqrt{RH}.                                        \tag{4}
\]

The target is \(\sqrt R\), so (4) loses the factor \(\sqrt H\). If
\(H=R^\theta\), the best possible positive fixed-fiber exponent is
\(R^{(1+\theta)/2}\), instead of \(R^{1/2}\). For \(H\asymp R\), the
short fibers give the trivial capacity \(R\). More exactly, when
\(h>R/4\), each fixed residue progression \(q=4m+\rho\) has at most one
sample in a length-\(R\) product window, so no discrete curvature exists
on that fiber. This high-shell singleton boundary has baseline capacity
\(O(R)\), and any resonance theorem must state a separate estimate for it.
Resonance spacing cannot repair this loss, even under perfect
equidistribution of all off-diagonal resonance parameters.

At \(X=K^4\), \(Y=K^2\), \(R=K\), the leading exact-center quadratic
coefficient is \(-2h^2/K\). An exact denominator-\(b\) rational resonance
necessarily obeys \(K\mid 2b h^2\), so its \(h\)-spacing is at least
\(\gg\sqrt{K/b}\). Quadratic completion, including its incomplete-block
term, gives the aggregate model capacity

\[
 O\!\left(\sqrt{bK}(\log K)^2\right).                        \tag{5}
\]

Here and below, “model” means the leading quadratic truncation at the
exact center. Equation (5) is not asserted for the full cubic phase or the
actual weighted profile.

Thus exact integer resonance (\(b=1\)), and more generally
polylogarithmic-denominator resonance, is target-safe up to \(X^\varepsilon\);
the \(b=1\) family can saturate the target up to logs. Large \(b\) merges
with the generic fixed-fiber diagonal loss in (4). The obstruction is
taking absolute values separately in \(h\), not merely the integer
resonance family.

The only target-capable replacement exposed here is an actual-amplitude
signed or bilinear estimate across \(h\),

\[
 \left|\sum_{h\asymp H}T_h(J)\right|
 \ll_\varepsilon X^\varepsilon\sqrt R                       \tag{6}
\]

uniformly in \(H,J\), before taking fixed-\(h\) absolute values. The packet
does not supply or imply (6). Accordingly, this is a no-go for deriving
(56.9) from a termwise-absolute Fejer/Weyl fixed-\(h\) majorant, not a
no-go for every conceivable sharp \(\mathcal R_X\), and not a signed lower
bound for \(W_J^{\rm core}\).

## 2. Exact statement and hypotheses

Write the integer window as \(J=[A,B]\cap\mathbb Z\), with
\(B-A+1\le R\). Let \(\sigma_J(n)\) denote the exact radial endpoint
weight inherited from (56.1): it is not a newly assigned half-weight at
\(A\) or \(B\). For fixed \(h\) and \(\rho\in\{1,3\}\), define

\[
 \mathcal I_{h,\rho}(J)=
 \{m\in\mathbb Z:h(4m+\rho)\in J
 \text{ and all support conditions in (56.3) hold}\}.        \tag{7}
\]

It is a consecutive integer interval after zero values of the actual
profile are retained in the amplitude. Its length satisfies

\[
 M_{h,\rho}:=|\mathcal I_{h,\rho}(J)|
 \le {B-A\over4h}+1\ll {R\over h}+1.                         \tag{8}
\]

Define the exact actual-profile amplitude

\[
\begin{aligned}
 a_{h,\rho}(m)
 ={}&\sigma_J(h(4m+\rho))
 \sum_j{\bf1}_{h\le\lfloor D_jX^{-1/4}\rfloor}
 \Phi\!\left({h\over\lfloor D_jX^{-1/4}\rfloor+1}\right)\\
 &\qquad\qquad\times
 \left[w_j\!\left(2\sqrt{Xh/(4m+\rho)}\right)\right]^* .
                                                                    \tag{9}
\end{aligned}
\]

This displays the height floors, angular equality stars, hard-top profile,
and inherited radial star. The unnormalized fixed-fiber sum is

\[
 T_{h,\rho}(J)=
 \chi_4(\rho)\sum_{m\in\mathcal I_{h,\rho}(J)}
 a_{h,\rho}(m)e(F_{h,\rho}(m)),                              \tag{10}
\]

and \(T_h=T_{h,1}+T_{h,3}\). The already settled margin is excluded by
\[
 h\ge \lfloor L\rfloor+1.
\]
Thus if \(L\) is an integer, \(h=L\) remains owned by the low-leg result and
is not counted again.

The packet permits use only of sampled BV on each fixed-\(h\) product
window. In exact form, the needed input is

\[
 \|a_{h,\rho}\|_{\rm SBV(\mathcal I_{h,\rho})}
 :=\max_m|a_{h,\rho}(m)|
 +\sum_{m,m+1\in\mathcal I_{h,\rho}}
 |a_{h,\rho}(m+1)-a_{h,\rho}(m)|
 \ll_\varepsilon X^\varepsilon.                             \tag{11}
\]

No global variation in \(h\) is assumed. Abel summation gives

\[
 |T_{h,\rho}(J)|
 \ll_\varepsilon X^\varepsilon
 \max_{\mathcal K\subseteq\mathcal I_{h,\rho}}
 \left|\sum_{m\in\mathcal K}e(F_{h,\rho}(m))\right|,          \tag{12}
\]

where \(\mathcal K\) ranges over consecutive subintervals. Hence every
phase estimate below must be uniform under truncation.

For the exact resonance count required by any averaging attempt, define

\[
\begin{aligned}
 \mathscr N_{H,r}(\delta;J,\rho)
 =\#\{\,h:\;&H<h\le2H,\ h>L,\ M_{h,\rho}>r,\\
 &\|r\alpha_{h,\rho}(J)\|
 \le\delta+C rH^2/R^2\,\}.                                  \tag{13}
\end{aligned}
\]

The base \(m_0=\min\mathcal I_{h,\rho}(J)\), and therefore
\(\alpha_{h,\rho}(J)\), includes the floor caused by the hyperbola-window
edge. It may not be replaced uniformly by a smooth function \(ch^2/R\)
without controlling that floor error.

## 3. Proof and independent resonance ledger

### Exact odd-\(q\) discrete phase

Put \(q=4m+\rho\) and \(c_h=\sqrt{Xh}\). Direct calculation gives

\[
\begin{aligned}
 \Delta F(m)
 &=c_h\{\sqrt{q+4}-\sqrt q\}
 ={4c_h\over\sqrt{q+4}+\sqrt q},                             \tag{14}\\
 \Delta^2F(m)
 &=c_h\{\sqrt{q+8}-2\sqrt{q+4}+\sqrt q\}.
\end{aligned}
\]

The integral identities

\[
\begin{aligned}
 \Delta^2F(m)
 &=\int_0^1\!\!\int_0^1 F''(m+s+t)\,ds\,dt,\\
 \Delta^3F(m)
 &=\int_{[0,1]^3}F^{(3)}(m+s+t+u)\,ds\,dt\,du
\end{aligned}
\]

show that \(\Delta^2F<0\), \(\Delta^3F>0\), and, because
\(q\asymp Y/h\),

\[
\begin{aligned}
 F''(m)&=-4\sqrt{Xh}(4m+\rho)^{-3/2}
        \asymp-{h^2\over R},\\
 F^{(3)}(m)&=24\sqrt{Xh}(4m+\rho)^{-5/2}
        \asymp {h^3\over R^3}.                               \tag{15}
\end{aligned}
\]

This proves (1). In particular,

\[
 |\Delta^2F(m)-\Delta^2F(m_0)|
 \ll |m-m_0|{h^3\over R^3}
 \ll {h^2\over R^2}.                                        \tag{16}
\]

The character creates no hidden cancellation: after splitting into
\(\rho=1,3\), \(\chi_4(\rho)\) is merely the constant \(+1\) or \(-1\).

### Legal resonance majorant

For a lag \(1\le r<U\le M_{h,\rho}\), let

\[
 G_{h,\rho,r}(m)=F_{h,\rho}(m+r)-F_{h,\rho}(m).
\]

Its exact discrete first difference is

\[
 \Delta G_{h,\rho,r}(m)
 =\sum_{s=0}^{r-1}\Delta^2F_{h,\rho}(m+s).
\]

Equations (15)--(16) imply

\[
 |\Delta G_{h,\rho,r}(m)-r\alpha_{h,\rho}^{\rm real}|
 \le \eta_{h,r},\qquad
 \eta_{h,r}\ll r(M_{h,\rho}+r){h^3\over R^3}
 \ll r{h^2\over R^2},                                      \tag{17}
\]

where \(\alpha^{\rm real}\) is the representative
\(\Delta^2F(m_0)\). Moreover \(\Delta G\) is monotone. The discrete
Kusmin--Landau lemma therefore gives

\[
 \left|\sum_m e(G_{h,\rho,r}(m))\right|
 \ll \mathcal K_{h,\rho}(r),                                \tag{18}
\]

where a robust resonance-sensitive choice is

\[
 \mathcal K_{h,\rho}(r)=
 \begin{cases}
 M_{h,\rho},&
 \|r\alpha_{h,\rho}\|\le2\eta_{h,r}
 \text{ or }\eta_{h,r}\ge1/8,\\[2mm]
 \displaystyle
 \min\!\left(M_{h,\rho},
 {C\over\|r\alpha_{h,\rho}\|}\right),&
 \|r\alpha_{h,\rho}\|>2\eta_{h,r},\
 \eta_{h,r}<1/8 .
 \end{cases}                                                 \tag{19}
\]

Zero extension at the two fiber edges makes every shifted correlation in
(18) exact. Added completion samples have weight zero. They acquire no
radial or angular star.

For an unweighted interval of length \(M=M_{h,\rho}\), the exact finite
Fejer inequality is

\[
\begin{aligned}
 \left|\sum_{m=1}^{M}e(F(m))\right|^2
 \le {M+U-1\over U}\bigg[
 M+2\sum_{r=1}^{U-1}\left(1-{r\over U}\right)
 \operatorname {Re}\sum_{m=1}^{M-r}
 e(F(m+r)-F(m))\bigg].                                      \tag{20}
\end{aligned}
\]

Taking absolute values in the off-diagonal terms of (20) and then using
(18) gives the positive resonance majorant

\[
 \mathcal R_{h,\rho}(U)^2
 ={M+U-1\over U}
 \left[M+2\sum_{r=1}^{U-1}
 \left(1-{r\over U}\right)\mathcal K_{h,\rho}(r)\right].      \tag{21}
\]

Equations (12) and (21), applied uniformly to partial intervals, give a
lawful version of (56.8). The bracket in (21) is nonnegative because every
\(\mathcal K_{h,\rho}(r)\ge0\).

The resonance count (13) is the exact object needed before worst-casing
(19). For example, layer-cake summation of
\(\min(M,\|r\alpha\|^{-1})\) requires bounds for
\(\mathscr N_{H,r}(\delta)\) throughout
\(M^{-1}\lesssim\delta\le1/2\), plus the enlarged band
\(\delta\ll rH^2/R^2\). A count only for
\(\|r c h^2/R\|\) does not suffice unless the moving base \(m_0(h,J)\),
the error in (17), and all actual support restrictions are transferred.

### Sharp capacity of a positive fixed-fiber closure

The diagonal \(M\) in (21) is present even if every off-diagonal
correlation vanishes. Since \(1\le U\le M\),

\[
 \mathcal R_{h,\rho}(U)^2
 \ge {M+U-1\over U}M\ge 2M-1.                               \tag{22}
\]

On a dyadic block \(h\asymp H\) with \(\asymp H\) nonempty potential
fibers and \(M\asymp R/H\), (22) yields the intrinsic positive-majorant
capacity

\[
 \sum_{h\asymp H}\mathcal R_{h,\rho}
 \gtrsim H\sqrt{R/H}=\sqrt{RH}.                              \tag{23}
\]

Short hyperbola-strip geometry genuinely permits this many fibers: on a
full-length window and for \(H\ll\sqrt R\), the odd-\(q\) interval has
length \(\gg R/H\gg1\) for every \(h\) in the block, while all inequalities
in (56.3) are strict. For larger \(H\), the strip has area \(\asymp R\)
per fixed-ratio dyadic block and the fibers become shorter. The profile
may delete some potential incidences; the packet contains no nonvanishing
hypothesis that would turn this geometric fact into a lower bound for the
actual weighted sum.

The full exponent ledger is:

| \(h\asymp H=R^\theta\) | Aggregate unweighted capacity |
|---|---:|
| Trivial fixed fibers | \(HM\asymp R\) |
| Continuous curvature for \(H\le\sqrt R\) | \(\min(R,H\sqrt R)\) |
| Ideal nonresonant quadratic cancellation, then \(\sum_h|\cdot|\) | \(\sqrt{RH}=R^{(1+\theta)/2}\) |
| Required signed two-variable bound | \(\sqrt R=R^{1/2}\) |

Thus the ideal positive route loses \(R^{\theta/2}=\sqrt H\). Restoring
the radial factor \(Y^{-3/4}=R^{-3/2}\), its normalized capacity is

\[
 R^{-3/2}\sqrt{RH}=R^{-1+\theta/2}
 =Y^{-1/2+\theta/4},                                        \tag{24}
\]

whereas (56.4) requires \(R^{-1}=Y^{-1/2}\). The missing factor remains
\(\sqrt H\). This proves the no-go independently of how strongly one
controls the resonance counts in (13).

There is also an endpoint degeneration not represented by the resonance
count. From (8), if \(h>R/4\), then

\[
 {B-A\over4h}<1,
\]

so \(\mathcal I_{h,\rho}(J)\) has at most one sample for each
\(\rho\in\{1,3\}\). Thus \(M_{h,\rho}\le1\): there is no admissible
Fejer lag \(r\ge1\), no \(\Delta^2F\) sample, and no curvature-resonance
parameter to average. With only bounded actual amplitudes, summing these
singletons absolutely over \(R/4<h\ll R\) has capacity

\[
 O_\varepsilon(X^\varepsilon R).                            \tag{25a}
\]

The unweighted target is \(O_\varepsilon(X^\varepsilon\sqrt R)\). This is
the high-shell boundary baseline. A complete positive result must either
prove cross-\(h\) cancellation for these singleton phases or exploit
additional actual-profile support sparsity; a fixed-fiber curvature theorem
is silent there.

### Perfect-fourth-power rational resonance

Take \(X=K^4\), \(Y=K^2\), \(R=K\), and expand around \(n=K^2\). Uniformly
for \(|t|\le cK\),

\[
 K^2\sqrt{K^2+t}
 =K^3+{K\over2}t-{t^2\over8K}
 +{t^3\over16K^3}+O(t^4/K^5).                               \tag{25}
\]

On an exactly centered fixed-\(h\) progression \(t=4hm\), the linear and
quadratic terms are

\[
 2Khm-{2h^2\over K}m^2,                                     \tag{26}
\]

and the leading second difference is \(-4h^2/K\). Hence a first
derivative gap can vanish, and the quadratic curvature can have a small
rational denominator. The exact discrete curvature is not silently
replaced by its leading term:

\[
 {d\over dq}\sqrt{K^4hq}\bigg|_{hq=K^2}={Kh\over2},
\]

which is integral or half-integral; after the \(q=4m+\rho\) split its
leading \(m\)-derivative is \(2Kh\in\mathbb Z\).

The coefficient in the next formula is exact for the forward convention
\(\Delta^2F(m)=F(m+2)-2F(m+1)+F(m)\). Applying this operator at \(m=0\)
to

\[
 K^3+2Khm-{2h^2\over K}m^2+{4h^3\over K^3}m^3
 +O(h^4m^4/K^5)
\]

uses \(\Delta^2m^2|_{m=0}=2\) and
\(\Delta^2m^3|_{m=0}=6\), and hence gives

\[
 \Delta^2F(m_0)
 =-{4h^2\over K}+{24h^3\over K^3}
 +O(h^4/K^5)                                                 \tag{27}
\]

at the exact center. Off-center fibers also include the floor-dependent
base in (2).

Nevertheless the arithmetic spacing of the leading rational resonances
can be audited exactly. If the quadratic coefficient in (26) has exact
denominator \(b\), then necessarily

\[
 K\mid 2b h^2.                                               \tag{28}
\]

Let \(d_b\) be the least positive integer satisfying (28). Prime by prime,

\[
 2v_p(d_b)\ge
 \max(0,v_p(K)-v_p(2b)),
\]

so

\[
 d_b\ge \sqrt{K/(2b)}.                                       \tag{29}
\]

All solutions are multiples of the corresponding prime-power divisor
\(d_b\). Their total fixed-fiber length is bounded by

\[
 \sum_{\substack{h\le K/2\\K\mid2bh^2}}{K\over h}
 \ll {K\over d_b}\log K
 \ll\sqrt{bK}\log K.                                        \tag{30}
\]

For an interval of length \(M_h\), completion for the leading quadratic
model \(Q_h(m)=2Khm-2h^2m^2/K\) has the form

\[
 \left|\sum_{m\in\mathcal I_h}e(Q_h(m))\right|\ll
 \min\!\left(M_h,{M_h\over\sqrt b}+\sqrt b\log(2b)\right).
                                                                    \tag{31}
\]

Summing the first term on the right over the multiples of \(d_b\) gives
\(O(\sqrt K\log K)\) by (30). Splitting the capped incomplete-block term
at \(M_h=\sqrt b\log(2b)\) gives

\[
 \sum_{\substack{h\le K/2\\K\mid2bh^2}}
 \min(M_h,\sqrt b\log(2b))
 \ll \sqrt{bK}(\log K)^2.                                   \tag{32}
\]

This proves the leading-quadratic model capacity (5), and nothing here
transfers (30)--(32) to the full phase \(F_{h,\rho}\). Such a transfer
would have to control the cubic and higher terms, the moving
floor-dependent center, the incomplete fiber edges, and the actual
amplitude (9). Exact centering additionally requires \(h\mid K^2\) and the
correct odd residue, reducing the model family.
Equations (25)--(32) show both mandatory facts: perfect fourth powers
invalidate any claimed first-derivative gap; integer and
polylogarithmic-denominator resonances are target-safe up to
\(X^\varepsilon\), while large denominators do not remove the generic
positive-majorant obstruction.

## 4. First doubtful or unproved step

The discrete algebra through (21) is proved. The first target-relevant
unproved step is the signed cross-\(h\) estimate (6) with the actual
amplitude (9). Fixed-leg sampled BV (11) only licenses Abel summation
separately in \(m\); it gives no variation, orthogonality, or large-sieve
norm in \(h\). Therefore it cannot supply the missing factor \(H^{-1/2}\).

A theorem bounding the exact counts (13) would improve only the
off-diagonal part of each nonnegative \(\mathcal R_h\). Even the ideal in
which all those off-diagonal terms vanish leaves (23), so proving such
counts alone cannot reach the target.

The packet also gives support implications but no lower bound or explicit
interior nonvanishing interval for \(\Omega_X^*\). Consequently (23) is
a sharp obstruction to the coefficient-blind positive-majorant method,
not an actual-profile lower bound for (56.1). Constructing the “infinite
actual-profile family” mentioned in the packet would require nonvanishing
data not present in the permitted context. No signed lower bound for
\(W_J^{\rm core}\) is claimed.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| odd_q_discrete_phase | **Pass.** Equations (7), (14), and (15) retain \(q=4m+\rho\), the constant \(\chi_4(\rho)\), and exact first and second differences. |
| large_curvature_mod_one | **Pass.** The relevant quantities are \(\|r\alpha_{h,\rho}\|\) with drift \(O(rh^2/R^2)\), not the real size \(h^2/R\). Large drift is sent to the trivial branch of (19). |
| resonance_spacing_average | **No-go for termwise-absolute Fejer/Weyl averaging.** The exact count is (13), but even perfect counts cannot remove the diagonal (23), and the singleton shell has no resonance parameter. Equations (29)--(32) show that integer and polylogarithmic-denominator perfect-fourth resonances are individually target-safe up to \(X^\varepsilon\). |
| actual_profile_amplitude | **Pass in the interface; unresolved across \(h\).** Formula (9) carries the actual profile, floors, hard top, and stars. Only fixed-fiber SBV is used. No global \(h\)-regularity or nonvanishing is invented. |
| hyperbola_window_edges | **Pass.** The floor-dependent interval (7), length (8), inherited endpoint weights, and zero-weight completion endpoints are explicit. Artificial edges receive no star. |
| high-shell singleton boundary | **Obstruction recorded.** For \(h>R/4\), each residue progression has at most one sample, so curvature and resonance averaging are unavailable; absolute baseline is \(O(R)\), versus the \(O(\sqrt R)\) target. |
| perfect_fourth_power | **Pass.** Equations (25)--(27) exhibit integer/half-integer first-order and small-denominator quadratic resonance. No derivative-gap claim is made. |
| target_exponent_ledger | **Pass.** Equations (23)--(24) show the exact \(\sqrt H\) loss relative to the \(\sqrt R\) target. |
| low_leg_overlap | **Pass.** The range starts at \(h=\lfloor L\rfloor+1\); \(h=L\) when integral remains in the already-settled margin. |
| alpha_scope | **Pass.** This is a physical product-window result only. No alpha mask, connector, or Plemelj-order statement is inferred. |
| downstream_scope | **Pass.** No full shifted correlation, GAR, outside-height limit, M9-M1, M9, or final target is claimed. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The definitions and support conditions (56.1)--(56.5) in the Round-56
   derivation packet.
2. The packet's statement that fixed-leg sampled BV is available on each
   product window, used only as (11).
3. Finite Fejer differencing, discrete Kusmin--Landau, Abel summation, and
   elementary Taylor and prime-valuation calculations derived explicitly
   above.

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/briefs/blind_resonance_average_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/derivation_packet.md.
- Received from the conductor only the correction that (56.6) has
  \(F^{(3)}\asymp h^3/R^3\), which is the scale used above.
- Did not read the proof graph, proof draft, any prior report or synthesis,
  validation matrices, or any other Round-56 artifact.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Revise and retain as a method no-go.** Promote after seam review the
exact discrete-increment formulas, the resonance interface (17)--(21), and
the exponent obstruction (23)--(24). Reject the proposal that a sum of
termwise-absolute Fejer/Weyl fixed-\(h\) majorants can prove (56.9): its
diagonal capacity already exceeds the target by \(\sqrt H\). This does
not reject every sharper signed fixed-fiber construction. Retain as open a
genuinely signed, actual-amplitude two-variable estimate of the form (6).
Do not promote an actual-profile counterexample or any downstream
conclusion.

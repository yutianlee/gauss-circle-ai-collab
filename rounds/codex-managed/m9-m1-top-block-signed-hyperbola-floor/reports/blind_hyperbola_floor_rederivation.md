# Blind rederivation: exact hyperbola-floor and Fourier selectors

## 1. Result

**Exact finite-Fourier interface with a capacity no-go.** Put

\[
 \mathcal H=\{h\in\mathbb Z:R/4<h\le R/2\},
 \qquad
 a_h=\left\lceil {A\over h}\right\rceil,\quad
 b_h=\left\lfloor {B\over h}\right\rfloor.                  \tag{1}
\]

Let

\[
 d_h(q)=\chi_4(q){\bf1}_{[a_h,b_h]}(q).                     \tag{2}
\]

Choose one integer interval \([Q_-,Q_+]\) containing every possible
\([a_h,b_h]\), put \(D=Q_+-Q_-+1\), and choose
\(D\le M<2D\) (for example \(M=D\)).
Extend \(d_h\) by zero to the remaining residues in a complete
\(M\)-point interval. Then

\[
\begin{aligned}
 d_h(q)
 &={1\over M}\sum_{k\bmod M}D_h(k)
 e\!\left({k(q-Q_-)\over M}\right),                          \tag{3}\\
 D_h(k)
 &=\sum_{u=a_h}^{b_h}\chi_4(u)
 e\!\left(-{k(u-Q_-)\over M}\right).                         \tag{4}
\end{aligned}
\]

This is exact, has no truncation residual, and reproduces empty,
singleton, matched-pair, and point windows with the inherited endpoint
weights unchanged. Since the shell has at most two odd denominators in
one row, its coefficients are exactly

\[
 D_h(k)=
 \begin{cases}
 0,&\nu_h=0,\\
 \chi_4(q_h)e(-k(q_h-Q_-)/M),&\nu_h=1,\\
 \chi_4(q_h)e(-k(q_h-Q_-)/M)
       \{1-e(-2k/M)\},&\nu_h=2,
 \end{cases}                                                 \tag{5}
\]

where \(q_h\) is the sole odd denominator or the smaller one. In
particular,

\[
 D_h(0)=
 \begin{cases}
 0,&\nu_h=0\text{ or }2,\\
 \chi_4(q_h),&\nu_h=1.
 \end{cases}                                                 \tag{6}
\]

Thus the exact Fourier zero mode is the unmatched-row selector. The
matched adjacent signs cancel in that mode, but every unmatched row
survives with full sign.

Writing \(W_X(h,q)\) for the exact actual amplitude together with the
independent inherited radial-star value, Fourier inversion gives

\[
 P_J={1\over M}\sum_{k\bmod M}\sum_{h\in\mathcal H}
 D_h(k)\sum_{q=Q_-}^{Q_+}W_X(h,q)
 e\!\left(\sqrt{Xhq}+{k(q-Q_-)\over M}\right).               \tag{7}
\]

Equivalently, before absorbing the character into \(D_h(k)\), use

\[
 \chi_4(q)={e(q/4)-e(-q/4)\over2i}.                          \tag{8}
\]

The two exact phases are then

\[
 \sqrt{Xhq}+q\left({k\over M}+{\sigma\over4}\right)
 -{kQ_-\over M},
 \qquad \sigma\in\{+1,-1\}.                                 \tag{9}
\]

Fourier inversion alone has no square-root capacity. Direct absolute
summation of the original sparse selector gives

\[
 |P_J|\ll_\varepsilon X^\varepsilon R,                      \tag{10}
\]

where the target is \(X^\varepsilon\sqrt R\). The normalized Fourier
coefficient norm is only

\[
 {1\over M}\sum_{k\bmod M}|D_h(k)|\ll1,                     \tag{11}
\]

not \(O(R^{-1/2})\). Moreover, expanding the sparse selector and then
taking absolute values in all of \(k,h,q\) can enlarge (10) to
\(O_\varepsilon(X^\varepsilon R^2)\), because the ambient \(q\)-interval
has length \(\asymp R\). Recovering even (10) uses cancellation among the
Fourier modes.

A Vaaler truncation does not by itself estimate its nonzero modes, but its
endpoint residual can be controlled. The addendum below proves, uniformly
for \(N\asymp R^2\), \(d\in\{2,4\}\), fixed \(c\), and \(T\ge1\),

\[
 \sum_{R/4<h\le R/2}
 \kappa_T\!\left({N+ch\over dh}\right)
 \ll_\varepsilon X^\varepsilon\left({R\over T}+1\right),     \tag{11a}
\]

whenever
\(\kappa_T(t)\ll\min(1,T^{-2}\|t\|^{-2})\). Exact integral
arguments are included. Thus \(T\gtrsim\sqrt R\) makes every fixed finite
family of such endpoint residuals target-sized. The remaining obstruction
is the signed estimate for the nonzero Fourier modes in (7), not the
endpoint residual.

## 2. Exact statement and hypotheses

Let

\[
 h_-=\lfloor R/4\rfloor+1,\qquad h_+=\lfloor R/2\rfloor.
\]

If \(h_->h_+\), the shell is empty. Otherwise monotonicity permits the
exact global choices

\[
 Q_-=\min_{h\in\mathcal H}a_h=a_{h_+},\qquad
 Q_+=\max_{h\in\mathcal H}b_h=b_{h_-}.                      \tag{12}
\]

Since \(A,B\asymp R^2\) and \(h\asymp R\),

\[
 Q_-\asymp R,\qquad Q_+\asymp R,\qquad D\asymp R.           \tag{13}
\]

Indeed \(h_-=R/4+O(1)\), \(h_+=R/2+O(1)\), and
\(B=A+O(R)\), so
\[
 Q_+-Q_-={4B-2A\over R}+O(1)\asymp R.
\]

The row odd-count is exactly

\[
 \nu_h=\max\left(0,
 \left\lfloor{b_h+1\over2}\right\rfloor
 -\left\lfloor{a_h\over2}\right\rfloor\right).              \tag{14}
\]

Its floor-compatible sawtooth form is

\[
 \nu_h=\max\left(0,
 {b_h+1-a_h\over2}
 -\psi_F\!\left({b_h+1\over2}\right)
 +\psi_F\!\left({a_h\over2}\right)\right),                  \tag{15}
\]

with \(\psi_F(n)=-1/2\). Formula (15) is an exact count, not the signed
weighted row.

The actual coefficient used in (7) is

\[
\begin{aligned}
 W_X(h,q)
 ={}&\varrho_J(hq)\sum_j
 {\bf1}_{h\le\lfloor D_jX^{-1/4}\rfloor}
 \Phi\!\left({h\over\lfloor D_jX^{-1/4}\rfloor+1}\right)\\
 &\qquad\times
 \left[w_j\!\left(2\sqrt{Xh/q}\right)\right]^*,             \tag{16}
\end{aligned}
\]

where \(\varrho_J(hq)\) is the independent inherited radial-star value,
and every angular star in (16) is retained at its own equality point.
Equality with the artificial product-window edges \(A\) or \(B\) has
full cutoff weight. No new half-weight is assigned by (3).

The only amplitude size used for the capacity audit is the packet-level
fixed-row consequence

\[
 \sup |W_X(h,q)|\ll_\varepsilon X^\varepsilon.              \tag{17}
\]

No Fourier decay or global BV in \(h\) is assumed. In particular, the
height floors, hard-top jump, angular stars, and radial star remain in
\(W_X\) and are not transferred to \(D_h(k)\).

## 3. Proof and independent Fourier ledger

### Floor geometry and exact endpoints

The inequalities \(A\le hq\le B\) are equivalent, for positive \(h\), to
\[
 a_h\le q\le b_h.
\]
This proves the exact selector (2). Three odd denominators would be
\(q,q+2,q+4\), whose extreme products differ by
\[
 4h>R.
\]
But \(B-A=|J|-1\le R-1\), so \(\nu_h\le2\). Formula (14) follows by
counting odd integers in an integer interval; substituting
\(\lfloor t\rfloor=t-\psi_F(t)-1/2\) proves (15), including all equality
cases.

A point window \(A=B=N\) has
\[
 a_h=\lceil N/h\rceil,\qquad b_h=\lfloor N/h\rfloor.
\]
It is empty unless \(h\mid N\), in which case \(a_h=b_h=N/h\).
Formula (14) then returns one exactly when \(N/h\) is odd. Thus the
selector reproduces the mandatory divisor incidence, with whatever
inherited star belongs to \(N\), and adds no artificial endpoint weight.

### Character projector and exact DFT

For integer \(q\), (8) is zero when \(q\) is even, equals \(+1\) when
\(q\equiv1\pmod4\), and equals \(-1\) when
\(q\equiv3\pmod4\). It is therefore both the odd-parity projector and the
character; multiplying by a second odd indicator would be redundant.

Extend \(d_h(q)\) by zero from \([Q_-,Q_+]\) to
\[
 Q_-,Q_-+1,\ldots,Q_-+M-1.
\]
Fourier inversion on \(\mathbb Z/M\mathbb Z\) gives (3)--(4). If the row
is empty, all coefficients vanish. If it contains one odd denominator,
(5) is immediate. If it contains two, they are \(q_h,q_h+2\), and
\(\chi_4(q_h+2)=-\chi_4(q_h)\); factoring the first term gives the last
line of (5). Setting \(k=0\) proves (6).

For a singleton,
\[
 {1\over M}\sum_k|D_h(k)|=1.
\]
For a matched pair,
\[
 {1\over M}\sum_k|D_h(k)|
 ={1\over M}\sum_k|1-e(-2k/M)|\le2.                         \tag{18}
\]
This proves (11). It also shows the limitation: the matched factor is
small for low modes,
\[
 |1-e(-2k/M)|\ll \|k\|_M/M,
\]
but is order one on a positive proportion of the modes. Singleton rows
have no low-mode zero at all.

Substitution of (3) into the exact physical sum proves (7). Alternatively,
apply the selector DFT without the character and then use (8), which
proves (9). The \(k=0\) term of (7) is

\[
 P^{(0)}={1\over M}\sum_{\substack{h\in\mathcal H\\\nu_h=1}}
 \chi_4(q_h)
 \sum_{q=Q_-}^{Q_+}W_X(h,q)e(\sqrt{Xhq}).                   \tag{19}
\]

Thus “zero mode” does not mean a constant physical phase, and it does not
vanish unless all rows are matched. With \(M\asymp D\asymp R\), the inner
ambient sum has length \(O(R)\); a termwise bound on (19) costs \(O(1)\)
per unmatched row and \(O(R)\) in aggregate. The packet supplies no
\(O(\sqrt R)\) bound for the unmatched population or the signed sum
(19).

### Truncation and Fejer residual

For comparison, a degree-\(K\) Vaaler approximation has the form

\[
 \psi_F(t)=\sum_{1\le |k|\le K}c_k e(kt)+\mathcal E_K(t),
 \qquad |c_k|\ll |k|^{-1},                                  \tag{20}
\]

with

\[
 |\mathcal E_K(t)|
 \le {C\over K+1}\mathcal F_K(t),\qquad
 \mathcal F_K(t)=\sum_{|k|\le K}
 \left(1-{|k|\over K+1}\right)e(kt).                        \tag{21}
\]

Here \(\mathcal F_K(0)=K+1\). Therefore an exact integral endpoint can
contribute \(O(1)\), not \(O(1/K)\), and \(\psi_F(n)=-1/2\) must be
retained through the residual rather than replaced by zero.

The required endpoint average is in fact available for the exact rational
forms generated by the floors.

**Endpoint Fejer sampling lemma.** Let \(N\asymp R^2\), let
\(d\in\{2,4\}\), let \(c\) be a fixed integer, and let \(T\ge1\). If

\[
 |\kappa_T(t)|\ll\min\!\left(1,{1\over T^2\|t\|^2}\right),   \tag{22}
\]

where the minimum is interpreted as \(1\) at \(\|t\|=0\), then (11a)
holds.

To prove it, for \(0\le\delta\le1/2\) define

\[
 Z(\delta)=\#\left\{h\in\mathcal H:
 \left\|{N+ch\over dh}\right\|\le\delta\right\}.              \tag{22a}
\]

For every counted \(h\), choose \(m\in\mathbb Z\) with

\[
 |N+ch-dhm|\le dh\delta.
\]

Put \(a=dm-c\in\mathbb Z\) and \(n=ah\in\mathbb Z\). Then

\[
 |N-n|\le dh\delta\le2R\delta.                               \tag{22b}
\]

There are \(O(R\delta+1)\) possible integers \(n\) in (22b). Since
\(N\asymp R^2\), every such positive \(n\) is \(\asymp R^2\) after
absorbing bounded small \(R\), and for each \(n\) every possible \(h\)
is a divisor of \(n\). The extra congruence
\[
 n/h=a\equiv-c\pmod d
\]
can only reduce the count. The divisor estimate therefore gives

\[
 Z(\delta)\ll_\varepsilon
 X^\varepsilon(R\delta+1).                                  \tag{22c}
\]

This also audits exact integers. If the argument is integral, then
\(n=N\); hence \(N\) is an integer and
\[
 h\mid N,\qquad N/h\equiv-c\pmod d.
\]
There are at most \(\tau(N)\ll_\varepsilon X^\varepsilon\) such \(h\).
If \(N\notin\mathbb Z\), there are none.

For \(T\le2\), the trivial \(O(R)\) bound proves (11a). For \(T>2\),
separate \(\|\cdot\|\le1/T\) and the dyadic annuli
\[
 {2^j\over T}<\|\cdot\|\le
 \min\!\left({2^{j+1}\over T},{1\over2}\right).
\]
Using (22)--(22c),

\[
\begin{aligned}
 \sum_{h\in\mathcal H}|\kappa_T((N+ch)/(dh))|
 &\ll Z(1/T)+
 \sum_{0\le j\ll\log T}4^{-j}
 Z\!\left(\min(2^{j+1}/T,1/2)\right)\\
 &\ll_\varepsilon X^\varepsilon
 \left\{{R\over T}+1+
 \sum_{j\ge0}4^{-j}
 \left({R2^j\over T}+1\right)\right\}\\
 &\ll_\varepsilon X^\varepsilon\left({R\over T}+1\right).
                                                                    \tag{22d}
\end{aligned}
\]

This proves the lemma with no loss at exact endpoint divisors. Therefore
a fixed finite collection of Vaaler residual arguments of the form in
(11a) is \(O_\varepsilon(X^\varepsilon\sqrt R)\) once
\(T\gtrsim\sqrt R\). The exact DFT still avoids truncation entirely; the
lemma only closes the residual ledger, not the nonzero Fourier sums.

### Perfect-fourth-power modes and target capacity

Let \(X=K_0^4\) and \(R=K_0\), and write \(hq=K_0^2+t\). Then

\[
 \sqrt{Xhq}
 =K_0^3+{K_0\over2}t-{t^2\over8K_0}
 +O(t^3/K_0^3).                                             \tag{23}
\]

The linear term is integral or half-integral on integer \(t\). In the
unabsorbed representation (9), the additional frequency
\[
 {k\over M}+{\sigma\over4}
\]
is rational and can reinforce that coherence. Hence neither a
first-derivative gap nor generic irrationality is available uniformly in
\(k\). Any proof must retain the quadratic term, the hyperbola relation,
the endpoint-floor coefficient, and the actual amplitude.

There are \(O(R)\) possible physical incidences, so (17) proves only
(10). The exact DFT has the following capacity ledger:

| Operation | Absolute capacity | Reason |
|---|---:|---|
| Original sparse selector | \(X^\varepsilon R\) | \(O(R)\) incidences |
| DFT zero mode | \(X^\varepsilon R\) | \(O(1)\) per unmatched row in (19) |
| Reconstruct selector, then take absolute values | \(X^\varepsilon R\) | returns the sparse bound |
| Take absolute values separately in \(k,h,q\) | \(X^\varepsilon R^2\) | DFT spreads each row over \(D\asymp R\) ambient \(q\)'s |
| Desired signed mode aggregate | \(X^\varepsilon\sqrt R\) | unproved |

The packet-mandated family with \(\gg R\) unmatched absolute mass rules
out any assertion that endpoint sparsity alone gives the target. A
modewise proof must use cancellation within the oscillatory \(q\)-sums,
across \(h\), or across modes; coefficient norm (11) alone cannot do so.

Restoring \((hq)^{-3/4}\asymp R^{-3/2}\), the best direct physical
triangle bound is \(X^\varepsilon R^{-1/2}\), while the target is
\[
 X^\varepsilon R^{-1}=X^\varepsilon Y^{-1/2}.               \tag{24}
\]
The exact missing factor is \(\sqrt R\).

## 4. First doubtful or unproved step

The floor count (14)--(15), character identity (8), finite DFT
(3)--(7), zero mode (6), and endpoint rules are exact. The first
target-relevant unproved step is a signed estimate for

\[
 {1\over M}\sum_{k\bmod M}\sum_{h\in\mathcal H}D_h(k)
 \sum_{q=Q_-}^{Q_+}W_X(h,q)
 e\!\left(\sqrt{Xhq}+{k(q-Q_-)\over M}\right)               \tag{25}
\]

of size \(O_\varepsilon(X^\varepsilon\sqrt R)\), without destroying the
mode cancellation that reconstructs the sparse selector. Even the zero
mode (19) needs a new unmatched-row cross-\(h\) estimate.

The coefficients \(D_h(k)\) contain discontinuous endpoint floors, and
\(W_X(h,q)\) contains independent height floors, profile edges, hard-top
and equality jumps. The packet provides no global BV in \(h\), Fourier
decay, spectral theorem, or large-sieve estimate matching these moving
symbols.

For the Vaaler route, (11a) now proves the endpoint residual estimate and
shows that \(T\gtrsim\sqrt R\) is target-capable. The first unproved step
there is likewise the signed aggregate of the resulting nonzero modes.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| exact_floor_selector | **Pass.** Equations (1)--(5) and (12)--(15) retain the exact endpoint floors and give an exact signed selector. Empty and point windows are reproduced. |
| zero_mode | **Pass.** Equation (6) identifies it exactly with unmatched rows; (19) records its physical phase and \(O(R)\) absolute capacity. |
| fourier_truncation | **Pass.** The DFT is finite and residual-free. The divisor-count lemma (22a)--(22d) includes exact integer peaks and proves Vaaler residual size \(X^\varepsilon(R/T+1)\); \(T\gtrsim\sqrt R\) is target-capable. Nonzero modes remain open. |
| character_projector | **Pass.** Equation (8) simultaneously kills even \(q\) and supplies \(\chi_4\); no redundant odd projector is inserted. |
| cross_h_phase | **Pass as an interface.** Equations (7), (9), and (25) retain the rational selector/character mode and hyperbola phase. Their signed estimate remains open. |
| actual_amplitude | **Pass in scope.** Equation (16) retains the actual profiles, height floors, hard top, angular stars, and independent radial-star value. No global regularity is invented. |
| endpoint_and_stars | **Pass.** Artificial \(A,B\) boundaries are full cutoffs; inherited equality stars remain attached to their original samples. The point-window divisor case is exact. |
| perfect_fourth_power | **Pass.** Equation (23) records integer/half-integer radial coherence and rational mode shifts; no first-derivative gap is assumed. |
| target_ledger | **No-go passed.** Exact Fourier organization has no automatic negative power of \(R\); direct physical closure loses precisely \(\sqrt R\), and fully modewise triangle closure is worse. |
| downstream_scope | **Pass.** Only the physical shell \(R/4<h\le R/2\) is treated. The lower shell, alpha connector, height limits, full shifted correlation, and downstream theorems remain separate. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The Round-58 packet's high-shell object, endpoint floors, exact
   amplitude convention, character, and target.
2. Finite Fourier inversion on \(\mathbb Z/M\mathbb Z\), the elementary
   identity (8), and the floor identity used in (15).
3. The explicit Vaaler/Fejer residual form (20)--(21) and elementary
   perfect-fourth Taylor expansion.
4. The elementary divisor estimate
   \(\tau(n)\ll_\varepsilon n^\varepsilon\), used in
   (22b)--(22d).

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/briefs/blind_hyperbola_floor_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/derivation_packet.md.
- An initial lookup used the wrong guessed brief filename and failed; I
  then listed filenames in the assigned briefs directory solely to locate
  the named blind brief. I did not open either of the other listed briefs.
- Received from the conductor only the endpoint Fejer sampling lemma
  statement proved in (22a)--(22d); no other Round-58 artifact was opened.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  validation matrices, or any other Round-58 artifact.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Promote the exact DFT interface after seam review; reject Fourier
expansion alone as a target-saving argument.** Retain (3)--(9), the exact
zero/unmatched rule (6), point-window and star ledger, and capacity table
as candidate exact evidence. Add the endpoint sampling lemma
(22a)--(22d): it makes Vaaler height \(T\gtrsim\sqrt R\)
residual-safe, including exact divisors. The exact DFT and the truncated
route still need the signed nonzero-mode theorem (25).
Do not infer the lower-shell estimate or any alpha/downstream conclusion.

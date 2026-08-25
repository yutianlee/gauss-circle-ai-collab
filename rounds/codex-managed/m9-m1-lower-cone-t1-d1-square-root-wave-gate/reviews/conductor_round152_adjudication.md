# Round 152 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Starting graph: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Decision: promote a strict arithmetic support reduction, a new source-legal scale range, and scoped method obstructions
- Terminal label: `strict_square_root_character_range`

## 1. Decision

Round 152 makes two genuine advances on the literal $D=d=L=1$ square-root
wave, but does not prove the full scalar target.

First, it partitions the actual retained support into three target-safe
arithmetic owners and one exact survivor.  The exact-square ray, every
nonzero square defect of size at most $M^{3/4}$, and every term whose
square factor is at least $\lceil M^{1/4}\rceil$ have total weighted mass
$O_\varepsilon(X^\varepsilon)$.  The survivor has square defect larger
than $M^{3/4}$ and square factor smaller than $\lceil M^{1/4}\rceil$; its
$s=1$ layer is nonempty in principle and remains open.

Second, the source-legal pair

$$
 BD\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right)
$$

proves

$$
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon.
$$

Thus $M^{449}\gg R^{780}$ is target-safe.  Since
$780/449<1424/819$, this owns a nonempty scale sliver below the previous
Tao--Trudgian--Yang boundary.  Below the new boundary the pruned survivor
is still unestimated.  No global exponent changes.

## 2. Literal wave and owner split

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,
$$

and retain the literal compact-smooth Round-148 profile
$A_U(\ell)=\mathscr A_{1,M,U}(1,\ell)$, extended by zero with its inherited
endpoint convention.  The accepted Round-151 relation is

$$
 P_U=\sum_{\substack{\ell>0\\\ell\ {\operatorname{odd}}}}
 \chi_4(\ell)\ell^{-3/4}A_U(\ell)e(\sqrt{N\ell}),
 \qquad
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
$$

with the external coefficient $B_{1,U}(1)$ still attached and
$|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon$.

For the unique nearest integer

$$
 k(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad j(\ell)=k(\ell)^2-N\ell,
$$

write uniquely $\ell=\tau s^2$, where $\tau$ is odd and squarefree and
$s$ is odd.  With $J=M^{3/4}$ and $S=\lceil M^{1/4}\rceil$, take the
disjoint owners in the order

$$
\begin{aligned}
 \mathcal L_0&=\{j=0\},\\
 \mathcal L_1&=\{0<|j|\le J\},\\
 \mathcal L_2&=\{|j|>J,\ s\ge S\},\\
 \mathcal L_*&=\{|j|>J,\ s<S\}.
\end{aligned}
$$

Then

$$
 |P_{\mathcal L_0}|+|P_{\mathcal L_1}|+|P_{\mathcal L_2}|
 \ll_\varepsilon X^\varepsilon,
 \qquad P_U=P_U^*+O_\varepsilon(X^\varepsilon),
$$

where

$$
 P_U^*=\sum_{\substack{\ell=\tau s^2\ {\operatorname{retained}}\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\le s<\lceil M^{1/4}\rceil}}
 \chi_4(\tau)(\tau s^2)^{-3/4}A_U(\tau s^2)e(s\sqrt{N\tau}).
$$

No coprimality between $\tau$ and $s$ is inserted.  On the survivor
$\tau\gg M^{1/2}$, and the displayed identity is a support reduction,
not an estimate for $P_U^*$.

## 3. Arithmetic proof

The nearest integer has no half-integer tie because $4N\ell$ cannot be
an odd square.  Write $N=a^2n_0$ with $n_0$ squarefree.  Exact resonance
requires $\tau=n_0$ and is present on odd support only when $n_0$ is odd;
its complete actual-weight mass is
$O_\varepsilon(M^{-1/4}n_0^{-1/2}X^\varepsilon)$.

For nonzero $j$, let

$$
 \rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}.
$$

Prime-power analysis, including $p=2$, gives

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)},
 \qquad
 \sum_{1\le|j|\le J}\rho_N(j)\ll_\varepsilon JX^\varepsilon.
$$

The actual $k$-support has length $O(\sqrt{NM})<N$ because
$M\le R^2\asymp N^{1/2}$.  Each residue class therefore contributes
$O(1)$ possible $k$, and fixed $(j,k)$ determines $\ell$.  Taking
$J=M^{3/4}$ and using the actual $M^{-3/4}$ weight proves the
$\mathcal L_1$ bound.  Finally,

$$
 \sum_{S\le s\ll\sqrt M}\left(1+\frac{M}{s^2}\right)
 \ll M^{3/4},
$$

and intersecting this count with $|j|>J$ makes $\mathcal L_2$ disjoint
without increasing its mass.  This proves the complete pruning.

## 4. Source range and exact boundary

For a square-root phase, an exponent pair $(\kappa,\lambda)$ yields

$$
 |P_U|\ll_\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon
$$

after the two classes modulo four are separated, an unweighted interval
estimate is applied, and the actual bounded-variation profile is inserted
by Abel summation.  Tao--Trudgian--Yang Lemma 14 gives

$$
 D\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right).
$$

Its maximum has no hidden gap: on $0\le\alpha\le1/2$ the difference
between its affine line and the auxiliary line is

$$
 \frac{17-29\alpha}{2388}\ge\frac5{4776}.
$$

The Lemma-15 symmetry bridge covers the upper half, and Lemma 13 then
gives the global $BD$ pair used above.  The relevant Table-1 cell is

$$
 \frac{1508}{3825}\le\alpha<\frac{62831}{155153},
$$

and its line meets the required line $\beta(\alpha)=(1+\alpha)/4$ at
$\alpha=127/322$, equivalently $M=R^{780/449}$.  This is a
boundary-optimal statement for the audited exponent-pair envelope, not a
claim that this pair pointwise dominates every older pair at every scale.

## 5. Scoped method obstructions

Adjacent odd pairing leaves the full phase difference; that difference
can approach an integer and cannot be replaced by a smooth derivative.
For every legal even shift,

$$
 \chi_4(\ell+2h)\chi_4(\ell)=(-1)^h,
$$

so one $A$-process erases the variable character.  Its exact bound is

$$
 |P_U|^2\ll_\varepsilon
 \left(\frac{M^{1/2}}H+RM^{-3/4}H^{1/2}
 +R^{-1}M^{3/4}H^{-1/2}\right)X^\varepsilon,
$$

which gives no new point below the top endpoint.  Mellin inversion has
spectral scale $\sqrt{NM}$, root number $+1$, and unbalanced dual length
$\sqrt{N/M}$; using its oscillation reproduces character Poisson and the
accepted reciprocal row.  A second principal $B$-process is the same
self-return.  Pointwise absolute Mellin bounds, even a hypothetical
Lindelof estimate, retain a power loss.  The audited mixed Burgess,
higher-Voronoi, and fixed-parameter nonlinear-resonance theorems do not
match the literal coefficient, phase, growing parameter, actual weight,
or endpoint class.  These are method-specific no-gain or no-match
statements, never a lower bound or an impossibility theorem.

## 6. Review gate

The terminal review gate consists of:

- `reviews/independent_conductor_round152_math_review.md`: terminal GREEN
  after repairing the additive error sign, every $N=\lfloor X\rfloor$
  asymptotic seam, the boundary-optimal wording, and the explicit
  Lemma-14/Lemma-15 bridge;
- `reviews/hostile_square_root_pruning_review.md`: GREEN for the complete
  arithmetic pruning after an exact recheck of prime powers, parity,
  ceiling thresholds, support length, disjointness, weights, and the
  $B_{1,U}(1)$ seam; and
- `reviews/source_conductor_round152_final.md`: terminal GREEN for the
  Bourgain global-pair scope, the Lemma-14 maximum, Remark-16/Lemma-15
  global bridge, the subsequent $B$ placement, model-phase and interval
  hypotheses, actual-profile Abel transfer, every power and Table-1
  boundary, Mellin normalization, and all direct source no-matches.

The first unproved estimate is exactly
$|P_U^*|\ll_\varepsilon X^\varepsilon$ below
$M^{449}\asymp R^{780}$ after the bounded owner is removed.

## 7. State decision and downstream scope

Create one strict-range reduction and one scoped method obstruction.  Add
the new source range to the Bourgain/TTY interfaces and refine the
Round-151 reciprocal and large-wrap frontiers to the residual $P_U^*$.
Reject only the false inferences explicitly audited in this round.

The $D>1$ recovery fibre, $L>1$ rows, growing-$M$ generic sector, every
original $t\ge2$ layer, the Round-138 cross owner, remaining M1 and M2
owners, endpoint uniformity, M9, the bridge, the quarter target, the
internal exponent $1/3$, and the external Li--Yang exponent remain open
or unchanged.

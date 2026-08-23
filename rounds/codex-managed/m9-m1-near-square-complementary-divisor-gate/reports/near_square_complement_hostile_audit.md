# Round 122 hostile audit: the complementary-divisor split is a circle/tail self-return

Campaign: `m9-m1-near-square-complementary-divisor-gate`
Task: `near_square_complement_hostile_audit`
Role: hostile seam reviewer
Starting graph SHA-256: `3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

## 1. Result: maximal safe lemma and route-killing conclusion

Let

\[
 R=X^{1/4},\qquad y=\lfloor \sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

and retain the exact Round-121 objects

\[
 \mathcal B_{\rm flat}^{(N)}=\sum_{k\in\mathbb Z}D_N(k)W(k),
 \qquad W(k)=\widehat J(k)-\widehat J(k+1).
\]

The following statements are rigorous.

1. The one-sided transition can be priced uniformly. For every integer
   \(A\geq1\),

   \[
   |W(k)|\ll_A
   \min\left\{R^{-1},\frac1{1+|k|},
   \frac{y^{A-1}}{(1+|k|)^A}\right\}.
   \tag{122.H1}
   \]

   Consequently, with

   \[
   K_0=\left\lceil yX^{1/8}\right\rceil,
   \tag{122.H2}
   \]

   the discarded tail is \(O_B(RX^{-B})\) for every fixed \(B>0\).
   Every integer traversed by the remaining oriented intervals is positive
   and satisfies \(|n-y^2|\ll K_0+y\). Fixed-\(X\) Schwartz decay is not
   being used with a hidden uniform constant.

2. For every positive integer \(m=2^a m_0\), \(m_0\) odd, put

   \[
   \sigma(m)=\chi _4(m_0),\quad
   S(m)=\sum_{d\mid m_0}\chi _4(d)=\frac{r_2(m)}4,
   \quad
   Q_y(m)=\sum_{\substack{q\mid m_0\\q<m_0/y}}\chi _4(q).
   \]

   Then the literal sharp coefficient is

   \[
   \boxed{A_y(m)=S(m)-\sigma(m)Q_y(m).}
   \tag{122.H3}
   \]

   This formula is valid for every \(a\geq0\), with no factor
   \(\chi _4(m)\) when \(m\) is even. The cutoff on \(Q_y\) is strict.
   Thus a hard divisor \(d=y\) is included in \(A_y\), while its partner
   \(q=m_0/y\), when integral, is excluded from \(Q_y\).

3. Define the exact central difference

   \[
   E_y(m)=\sum_{d\mid m_0}\chi _4(d)
   \left({\bf1}_{d\leq y}-{\bf1}_{d<m_0/y}\right).
   \tag{122.H4}
   \]

   The residue branches are

   \[
   \begin{array}{c|c}
   m_0\bmod4&\text{exact formula}\\ \hline
   1&2A_y(m)=S(m)+E_y(m),\\
   3&S(m)=E_y(m)=0,\quad A_y(m)=Q_y(m).
   \end{array}
   \tag{122.H5}
   \]

   Hence the \(3\bmod4\) branch is a literal threshold-swap self-return.
   The \(1\bmod4\) branch leaves one half of the full \(r_2/4\)
   coefficient plus an exact central band. A factor \(1/2\) is not a
   power saving.

4. Three proper pieces are target-safe: \(|k|\leq R\); all
   \(|k|>K_0\); and, in the localized middle window, the aggregate of
   integers divisible by \(2^{A_0}\), where

   \[
   2^{A_0}\geq y/R.
   \tag{122.H6}
   \]

   In addition, the odd \(m_0\equiv1\pmod4\) central-band term
   \(E_y(m)/2\) is \(O(R\log X)\) after the signed \(k\)-wavelet is
   retained. These are strict target-safe subpackages, but none estimates
   the remaining low-valuation coefficient.

5. The exact full-divisor insertion gives, once and only once, a circle
   discrepancy and its exact complementary tail. Let \(\mathcal I_k\) be
   the oriented interval operator from \(N\) to \(N+k\), and put

   \[
   T_y(n)=\sigma(n)Q_y(n),\qquad
   \Delta_\circ(k)=\mathcal I_k(S-\pi/4),\qquad
   \Delta_T(k)=\mathcal I_kT_y.
   \]

   Then, on the positive localized window,

   \[
   D_N(k)=\Delta_\circ(k)-\Delta_T(k)
   +(\pi/4-c_y)k.
   \tag{122.H7}
   \]

   The last term contributes \(O(1)\) in absolute value. Bounding
   \(\Delta_\circ\) at the required scale by the conjectural pointwise
   circle estimate is circular; the accepted \(X^{1/3+\varepsilon}\)
   circle bound gives only \(X^{1/3+\varepsilon}\) here. Recombining
   \(\Delta_\circ-\Delta_T\) restores \(D_N\) exactly. Thus the
   complementary-divisor involution supplies no noninvertible gain.

The route-killing conclusion is therefore precise: after the safe pieces
above are removed, one is left with a signed low-\(2\)-adic circle/tail
wavelet. The \(3\bmod4\) part is the original truncated coefficient at
the complementary threshold, while the \(1\bmod4\) part contains the
full circle coefficient and, for even integers, a wide central band. No
proved inequality in the permitted state closes this survivor.

## 2. Exact statement and hypotheses

Use the Fourier convention

\[
 \widehat f(k)=\int_{\mathbb T}f(t)e(-kt)\,dt.
\]

The hypotheses on \(\eta\) and \(V_{\rm low}\) are exactly those of the
accepted sample-exact Round-121 interpolant: both are fixed smooth
cutoffs; \(\eta(yt)\) makes a smooth transition on a fixed multiple of
\(1/y\), equals one at every required positive sample, and vanishes near
zero; \(V_{\rm low}(4R^2t^2)\) is supported on a fixed multiple of
\(1/R\) and is constant near zero. The positive-arc function is extended
smoothly by zero before periodicization. Constants below may depend on
these two fixed cutoffs and on the displayed derivative order, but not on
\(X,R,y,N\).

For an arithmetic function \(f\) and an integer \(k\), define

\[
 \mathcal I_kf=
 \begin{cases}
  \displaystyle\sum_{N<n\leq N+k}f(n),&k>0,\\[4pt]
  0,&k=0,\\[4pt]
  \displaystyle-\sum_{N+k<n\leq N}f(n),&k<0.
 \end{cases}
 \tag{122.H8}
\]

Then \(\mathcal I_k1=k\), and whenever \(N+k>0\),

\[
 D_N(k)=\mathcal I_k(A_y-c_y).
 \tag{122.H9}
\]

An exact smallest survivor certified by the present audit can be stated as
follows. Let \(A_0\) be the least integer with \(2^{A_0}\geq y/R\), and
for \(n=2^a n_0\) in the localized window define

\[
 \mathscr V_y(n)=
 \begin{cases}
  \frac12S(n),&a=0,\ \sigma(n)=1,\\
  Q_y(n),&a=0,\ \sigma(n)=-1,\\
  \frac12\{S(n)+E_y(n)\},&1\leq a<A_0,\ \sigma(n)=1,\\
  Q_y(n),&1\leq a<A_0,\ \sigma(n)=-1,\\
  0,&a\geq A_0.
 \end{cases}
 \tag{122.H10}
\]

With every omitted term interpreted by the exact decomposition above,

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_0}W(k)\mathcal I_k\mathscr V_y
 +O_\varepsilon(RX^\varepsilon).}
 \tag{122.H11}
\]

Formula (122.H11) is a reduction, not an estimate for its displayed
survivor. It retains the prescribed centre, both signs of \(k\), all low
\(2\)-adic branches, both odd residue classes, the full divisor
coefficient, and every non-safe central band.

## 3. Proof and derivation

### 3.1 Uniform wavelet envelope and tail

Write

\[
 q(t)=\frac{1-e(-t)}t,\qquad
 K_{R,y}(t)=\eta(yt)V_{\rm low}(4R^2t^2)q(t).
\]

The apparent pole is removable, and all derivatives of \(q\) are bounded
on the fixed positive arc. The undifferentiated support has length
\(O(R^{-1})\). A derivative landing on the lower cutoff costs \(y\) but
is supported on an interval of length \(O(y^{-1})\); a derivative landing
on the upper radial cutoff costs \(R\) but is supported on an interval of
length \(O(R^{-1})\). The two transition regions are disjoint for large
\(X\). The product rule therefore gives

\[
 \|K_{R,y}\|_1\ll R^{-1},\qquad
 \|K_{R,y}^{(j)}\|_1\ll_j y^{j-1}\quad(j\geq1).
 \tag{122.H12}
\]

Since \(W(k)=\widehat K_{R,y}(k)\), the zeroth bound and integration by
parts once or \(A\) times prove (122.H1). In particular,

\[
 \sum_k|W(k)|\ll\log X,qquad
 \sum_k|kW(k)|\ll y.
 \tag{122.H13}
\]

For every integer \(k\),

\[
 \left\lfloor\frac{N+k}{d}\right\rfloor-
 \left\lfloor\frac Nd\right\rfloor-\frac kd
 =\left\{\frac Nd\right\}-\left\{\frac{N+k}{d}\right\},
\]

so \(|D_N(k)|\leq y\). Hence

\[
 \sum_{|k|>K}|D_N(k)W(k)|
 \ll_A y^AK^{1-A}.
 \tag{122.H14}
\]

At \(K=K_0\), this is
\(\ll_A yX^{-(A-1)/8}\). Choosing
\(A\geq3+8B\) proves the asserted \(O_B(RX^{-B})\) tail. Also
\(K_0=o(X)\), so \(N-K_0>0\). Since

\[
 0\leq N-y^2\leq2y,
\]

every retained integer is within \(K_0+2y\) of \(y^2\). For odd
\(n\),

\[
 \left|\frac ny-y\right|\ll X^{1/8};
 \tag{122.H15}
\]

for \(n=2^an_0\) with \(a\geq1\), however,

\[
 \frac{n_0}{y}=\frac{y}{2^a}+O\left(\frac{X^{1/8}}{2^a}\right),
 \tag{122.H16}
\]

so the two divisor thresholds are not near one another. This is the first
fatal correction to any parity-blind “near-square” claim.

### 3.2 Exact all-\(2\)-adic divisor involution

Only odd divisors contribute to \(\chi _4\), so the contributing divisors
of \(m=2^am_0\) are exactly the divisors of \(m_0\). Under
\(q=m_0/d\),

\[
 d>y\quad\Longleftrightarrow\quad q<m_0/y,
\]

and, because \(d,q,m_0\) are odd,

\[
 \chi _4(d)=\chi _4(m_0)\chi _4(q).
\]

Therefore

\[
 \sum_{\substack{d\mid m_0\\d>y}}\chi _4(d)
 =\sigma(m)Q_y(m),
\]

which proves (122.H3). No \(2^a\) multiplicity appears.

The strict inequality is essential. If \(y\mid m_0\), the hard sample
\(d=y\) is in \(A_y\), and the equality sample \(q=m_0/y\) is not in
\(Q_y\). If \(y\) is even, it cannot divide odd \(m_0\); equivalently
its character contribution is zero. If \(m_0<y\), then \(Q_y=0\) and
\(A_y=S\), as required.

From (122.H3) and \(E_y=A_y-Q_y\),

\[
 (1+\sigma)A_y=S+\sigma E_y.
 \tag{122.H17}
\]

When \(\sigma=-1\), divisors pair without a fixed point and with opposite
characters; hence \(S=0\). Also an odd square is \(1\bmod4\), so there is
no omitted square tie. Equation (122.H17) gives \(E_y=0\), while
(122.H3) gives \(A_y=Q_y\). When \(\sigma=1\), (122.H17) gives the first
line of (122.H5).

Put \(z=m_0/y\). The boundary-exact form of the central band is

\[
 E_y(m)=
 \begin{cases}
  \displaystyle\sum_{\substack{d\mid m_0\\z\leq d\leq y}}\chi _4(d),
     &z<y,\\[6pt]
  \chi _4(y){\bf1}_{y\mid m_0},&z=y,\\[4pt]
  \displaystyle-\sum_{\substack{d\mid m_0\\y<d<z}}\chi _4(d),
     &z>y.
 \end{cases}
 \tag{122.H18}
\]

If \(m_0=s^2\), then \(\sigma=1\). For \(s=y\), the fixed divisor is
counted once and

\[
 2A_y(m)=S(m)+\chi _4(s).
\]

For \(s<y\), the interval in the first line of (122.H18) contains
\(s\) once; for \(s>y\), the open interval in the third line contains
\(s\) once. Thus every square and central tie has the correct
multiplicity.

### 3.3 Exact one-count and the circular full-divisor term

The identity

\[
 \left\lfloor\frac nd\right\rfloor-
 \left\lfloor\frac{n-1}{d}\right\rfloor={\bf1}_{d\mid n}
\]

proves (122.H9). Substituting (122.H3) gives (122.H7). Since the partial
sums of \(\chi _4\) are bounded,

\[
 \left|\frac\pi4-c_y\right|\ll y^{-1}.
\]

Together with (122.H13), this makes the last term of (122.H7) \(O(1)\)
after summation against \(W\).

For integer \(t\geq1\),

\[
 \sum_{n\leq t}\left(S(n)-\frac\pi4\right)
 =\frac{P(t)-1}{4},
 \tag{122.H19}
\]

because \(1+\sum_{n\leq t}r_2(n)=N(\sqrt t)\). Thus the desired
pointwise quarter-circle theorem would give
\(|\Delta_\circ(k)|\ll RX^\varepsilon\), and (122.H13) would finish its
piece, but that is exactly the theorem being sought. The accepted
one-third theorem gives only

\[
 \sum_{|k|\leq K_0}|\Delta_\circ(k)W(k)|
 \ll_\varepsilon X^{1/3+\varepsilon}.
 \tag{122.H20}
\]

The tail \(\Delta_T\) is not optional: deleting it changes \(A_y\) into
the full \(r_2/4\) coefficient. Inserting it and then recombining gives
\(A_y=S-T_y\), hence exactly (122.D1). This proves the circle/tail
self-return.

### 3.4 The strict target-safe subpackages

For \(|k|\leq R\), the divisor bound gives

\[
 |D_N(k)|\ll_\varepsilon |k|X^\varepsilon,
\]

and (122.H1) gives

\[
 \sum_{|k|\leq R}|D_N(k)W(k)|
 \ll_\varepsilon RX^\varepsilon.
 \tag{122.H21}
\]

Next let \(H_A(n)={\bf1}_{2^A\mid n}A_y(n)\). On the positive localized
window,

\[
 |\mathcal I_kH_A|\ll_\varepsilon
 X^\varepsilon\left(1+\frac{|k|}{2^A}\right).
\]

Equations (122.H13) then give

\[
 \sum_{|k|\leq K_0}|W(k)\mathcal I_kH_A|
 \ll_\varepsilon X^\varepsilon
 \left(\log X+\frac{y}{2^A}\right).
 \tag{122.H22}
\]

This is target-safe when \(2^A\geq y/R\). It controls all valuations
\(v_2(n)\geq A\) together, so there is no logarithmic branch loss.

Finally consider the odd \(\sigma=1\) central band. For
\(|n-N|\leq K_0\), each divisor occurrence in (122.H18) corresponds to
an ordered factorization \(n=dq\) with

\[
 |d-y|+|q-y|\ll 1+K_0/y\ll X^{1/8}.
\]

Indeed, below \(y^2\) both factors lie between \(n/y\) and \(y\), and
above \(y^2\) both lie between \(y\) and \(n/y\). Hence

\[
 \sum_{\substack{|n-N|\leq K_0\\v_2(n)=0,\ \sigma(n)=1}}|E_y(n)|
 \ll (1+K_0/y)^2\ll X^{1/4}=R.
 \tag{122.H23}
\]

For any consecutive integer interval,

\[
 \sum_{u\leq k\leq v}W(k)=\widehat J(u)-\widehat J(v+1),
\]

and

\[
 \|J\|_1\ll\int_{c/y}^{C/R}\frac{dt}{t}\ll\log X.
\]

Swapping the finite \(n,k\) sums in the oriented interval therefore
shows that the contribution of \(E_y/2\) is \(O(R\log X)\). Equation
(122.H23), not an unsigned sum over every even branch, is the proved
narrow-square estimate. For \(a\geq1\), (122.H16) makes the band
in (122.H18) of length comparable to \(y\); the pair-box argument does
not apply.

It remains to account for the centering constant when passing from
\(D_N=\mathcal I_k(A_y-c_y)\) to the survivor in (122.H11). Absolute
convergence and telescoping give

\[
 \sum_{k\in\mathbb Z}kW(k)
 =\sum_{j\in\mathbb Z}\widehat J(j)=J(0)=0,
 \tag{122.H24}
\]

because the sample-exact lower cutoff makes \(J\) vanish near zero. The
part with \(|k|\leq R\) is \(O(R)\) by (122.H1), while (122.H1) with
\(A=4\) gives

\[
 \sum_{|k|>K_0}|kW(k)|\ll y^3K_0^{-2}\ll R.
\]

Thus the centering term on \(R<|k|\leq K_0\) is also \(O(R)\).
Combining this fact with (122.H14), (122.H21), (122.H22), and
(122.H23) proves (122.H11).

## 4. First doubtful or unproved step

The first genuinely unproved inequality is any target-scale estimate for
the survivor in (122.H11). More explicitly, at least one of the following
new signed inputs is required:

\[
 \sum_{R<|k|\leq K_0}W(k)\mathcal I_k\mathscr V_y
 \ll_\varepsilon RX^\varepsilon,
 \tag{122.H25}
\]

or a decomposition of (122.H25) whose pieces are each proved at that
scale without an outside norm.

The involution itself does not prove (122.H25):

- on \(\sigma=-1\), it merely changes the written cutoff from \(y\) to
  \(m_0/y\) and returns \(A_y=Q_y\);
- on \(\sigma=1\), it leaves \(S=r_2/4\), whose pointwise discrepancy is
  the circle problem, plus \(E_y\);
- for every low even valuation, \(m_0/y\asymp y/2^a\), so \(E_y\) is a
  wide unbalanced divisor band rather than a near-square error;
- applying Abel summation back to \(A_y(N+k)\widehat J(k)\), or completing
  the central products and inverting Fourier, reconstructs the Round-121
  flat cone and the Round-64/65 product-wavelet crossing functional.

Thus the first doubtful step is not a boundary convention. It is the
missing joint signed inequality across \(k\), low \(2\)-adic valuations,
both residues, the full circle coefficient, and the exact complement.

## 5. Control tests, seam table, and capacities

### Required seam controls

| Control | Outcome | Hostile finding |
|---|---:|---|
| `exact_Round121_discrepancy` | PASS | (122.H9) starts from the exact all-integer floor increment; no alternate normalization is introduced. |
| `uniform_wavelet_envelope` | PASS | (122.H12) prices the \(1/y\) transition explicitly and gives (122.H1). Fixed-\(X\) Schwartz constants are not used. |
| `far_k_tail_budget` | PASS | \(K_0=yX^{1/8}\) and sufficiently many integrations by parts give \(O_B(RX^{-B})\). A cutoff merely at \(|k|\asymp R\) or \(y\) is not certified by this argument. |
| `positive_near_square_window` | PASS | \(K_0=o(X)\), so all interval integers are positive. Odd parts are near \(y^2\) only for \(a=0\); (122.H16) records the fatal even-branch correction. |
| `two_adic_divisor_involution` | PASS | (122.H3) is valid for every \(a\geq0\) and never writes the meaningless \(\chi _4(m)\) for even \(m\). |
| `character_residue_branches` | PASS | The \(1\) and \(3\bmod4\) formulas are separated in (122.H5); the latter is a self-return, not cancellation. |
| `square_and_central_boundaries` | PASS | (122.H18) includes every strict/weak edge and counts a square fixed divisor once. |
| `full_divisor_and_complement_one_count` | PASS as identity; FAIL as gain | (122.H7) inserts \(r_2/4\) and the exact tail together once. Separating them exposes an open/circular circle piece; recombining restores \(D_N\). |
| `signed_k_aggregation` | PASS as bookkeeping; FAIL as estimate | All safe bounds retain the signed wavelet until a quantitative estimate. The remaining signed aggregation is precisely (122.H25), which is unproved. |
| `circle_problem_noncircularity` | FAIL for the proposed closure | (122.H19) shows literal circularity. The accepted bound stops at \(X^{1/3+\varepsilon}\). |
| `old_return_map_nonduplication` | FAIL for novelty | Threshold swapping on \(\sigma=-1\), Abel inversion, and product completion return to the accepted Round-121 or Round-64/65 cones. |
| `false_unsigned_control` | FAIL for any sign-blind gain | Replacing \(\chi _4\) by \(1\) gives \(2A_y^+=\tau(m_0)+E_y^+\). At \(m_0=y^2\) with odd \(y\), \(A_y^+=(\tau(y^2)+1)/2\): the involution contracts by no power. |
| `one_count_downstream_scope` | PASS | Only lower-owner subpackages are obtained; no blockwise M1, M2, endpoint, M9, or exponent implication is asserted. |

### Capacity and circularity table

| Object after lawful localization | Certified capacity | Excess over \(R\) | Verdict |
|---|---:|---:|---|
| Far \(|k|>K_0\) | \(O_B(RX^{-B})\) | none | target-safe |
| Core \(|k|\leq R\) | \(O_\varepsilon(RX^\varepsilon)\) | none | target-safe |
| Aggregate \(v_2(n)\geq A_0\) | \(O_\varepsilon(RX^\varepsilon)\) | none | target-safe |
| Odd \(\sigma=1\) central band | \(O(R\log X)\) | none | target-safe |
| Full \(S=r_2/4\) wave using accepted pointwise input | \(O_\varepsilon(X^{1/3+\varepsilon})\) | \(X^{1/12}\) | open; quarter input is circular |
| Fixed low valuation \(a\), by sparsity/divisor bound | \(O_\varepsilon((y/2^a+1)X^\varepsilon)\) | as large as \(R\) multiplicatively for \(a=1\) | not target-safe |
| \(\sigma=-1\) complementary branch | same coefficient after threshold swap | no power gain | exact self-return |
| Complete joint discrepancy | \(O_\varepsilon(yX^\varepsilon)\) | factor \(y/R\asymp R\) | survivor |
| Unsigned complementary control | half full divisor coefficient plus central tie | no power gain | rules out an involution-only argument |

The false unsigned control is algebraic, not a claim that an unsigned
conjecture has been disproved. Its purpose is decisive: any purported gain
using only divisor pairing, cutoff proximity, and triangle inequalities
would prove the same gain after deleting the character, although the
exact-square coefficient demonstrably has no such contraction. A valid
continuation must identify a genuinely character- and wavelet-sensitive
joint inequality.

No numerical experiment was used. The control is exact.

## 6. Dependencies and exact artifacts used

The derivation uses only the following permitted artifacts.

- `protocol.md`: graph authority, sign/unsigned separation, promotion and
  downstream-scope rules.
- `state/proof_obligations.yml`: the current statuses and implication map
  for the Round-121 discrepancy equivalence, the lower-radial owner, GAR,
  blockwise M1/M2, endpoint uniformity, M9, and the two Gauss-circle
  bridges.
- `state/active_campaign.yml`: frozen Round-122 formula, completion gates,
  and required controls.
- `strategy/conductor_0821_full_proof_strategy.md`: the prescribed
  noninvertibility gate and Round-121 return warning.
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md`:
  adjacent-character pairing obstruction and the need to retain the outer
  signed sum.
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`:
  exact product-wavelet self-return and the open local discrepancy.
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`:
  the unmatched product-crossing survivor.
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`:
  the one-variable Fourier return and absence of the missing gain.
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`:
  prescribed-centre circularity, full-selector, and false positive-core
  controls.
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`:
  accepted exact Round-121 normalization and downstream owner scope.
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/derivation_packet.md`:
  the proposed all-\(2\)-adic involution and its forbidden shortcuts.

No sibling Round-122 report, shared proof state, validation matrix,
synthesis file, or conductor artifact was read or edited.

## 7. Recommended state effect

**Recommendation: promote only the exact reductions and scoped no-go;
reject the complementary-divisor mechanism as a proof of the target; make
no change to any target status.**

Eligible supporting results are the uniform envelope and target-safe
localization (122.H1)--(122.H2), the all-\(2\)-adic identity and complete
boundary table (122.H3)--(122.H5), the safe high-valuation and odd-central
packages, the exact survivor (122.H11), and the circle/tail self-return
(122.H7), (122.H19). The proposed broad conclusion must be rejected:
there is no proved noninvertible signed gain for the complete wavelet.

The exact downstream map is:

- the safe packages do **not** prove
  `M9-M1-global-lower-radial-signed-estimate`;
- therefore they do not prove the full global angular-radial estimate or
  GAR;
- even a future proof of the complete lower discrepancy would feed the
  already proved radial one-count assembly and could close the alternative
  total-active M1/GAR route, but it would still not prove blockwise
  `M9-M1` or the standard blockwise `M9` node;
- nothing here proves hard TOP, BAL, UNBAL, or any part of `M9-M2`;
- nothing here proves endpoint uniformity;
- consequently neither the alternative Gauss-circle bridge nor the
  standard conditional bridge closes, and no discrepancy exponent changes.

The smallest live object is (122.H11)/(122.H25). A continuation is
justified only by a new joint signed inequality on that object. Another
complement, full-\(r_2\) completion followed by the circle bound, Abel or
Fourier inversion, residuewise norm, or unsigned divisor estimate is an
audited self-return or circular shortcut.

---

# Second-stage seven-part audit addendum: conductor candidate C4--C28

Candidate audited:
`candidates/conductor_wavelet_localization_and_two_adic_split.md`.
This addendum audits the candidate as revised, in particular its
localized cumulative argument (122.C25)--(122.C28). It does not audit or
rely on the superseded truncated pre-Abel argument.

## Addendum 1. Result

Equations (122.C4)--(122.C15) pass after two harmless notation repairs:
the equality at the end of (122.C8) is an asymptotic bound because
\(y=\lfloor\sqrt X\rfloor\), and every displayed complex sum in
(122.C12), (122.C15), and (122.C28) is understood in modulus. The strict
\(q<n/y\) cutoff, the hard \(d=y\) sample, the square tie (122.C21a), and
the \(a\geq1\) threshold repair (122.C24) are exact.

The revised central-pair argument also passes. Central divisor
occurrences on \(|j|\leq K_\delta\) inject into an ordered integer box of
side \(O(1+X^\delta)\), so their total absolute multiplicity is
\(O((1+X^\delta)^2)\). Keeping them as cumulative increments before
summing against \(W\) costs only the already proved \(\ell^1\) norm
\(\sum|W|\ll\log X\). Thus (122.C28) is target-safe for every fixed
\(0<\delta<1/8\), with no truncated-Abel boundary term.

There is no invalid formula through (122.C28). The first non-exact claim
is the phrase “smallest survivor” in Section 6 if it is read literally as
retaining *all* full-divisor and complementary pieces after (122.C18):
(122.C25)--(122.C28) have already removed the odd positive-character
central complement. The repaired smallest survivor is stated in Addendum
4 below. This is a scope/normal-form repair, not a failure of the central
pair estimate.

## Addendum 2. Exact statement and hypotheses

Fix once and for all

\[
 0<\delta<\frac18,\qquad K_\delta=yX^\delta,
 \qquad A_0=\lceil\log_2R\rceil.
\tag{122.A1}
\]

All cutoff and periodicity hypotheses are those recorded in Section 2 of
the main hostile report. In particular, \(G_{R,y}\) and \(J\) vanish in
a neighborhood of the periodic seam, \(J(0)=0\), and their transition
profiles are fixed independently of \(X\). The divisor decompositions
are applied to every increment \(m=N+j\) in the oriented interval, not
merely to its endpoint \(N+k\).

Under these hypotheses, (122.C4)--(122.C15) and
(122.C17)--(122.C28) are valid. The exact target-equivalent survivor is
the cumulative functional in (122.A8) below; no estimate for that
functional follows from the candidate.

## Addendum 3. Line-by-line proof audit of C4--C15

| Line | Verdict | Verification or repair |
|---|---:|---|
| C4 | PASS | The lower transition contributes \(y^M\cdot y^{-1}=y^{M-1}\) to the \(L^1\) derivative norm; the radial transition contributes \(R^M\cdot R^{-1}=R^{M-1}\leq y^{M-1}\). The transition supports are disjoint and the removable quotient has uniformly bounded derivatives. |
| C5 | PASS | Smooth periodic integration by parts has no seam term. The zeroth, first, and \(M\)-th derivative bounds give the three rows of the minimum. The \(1+|k|\) notation safely includes \(k=0\). |
| C6 | PASS | Split at \(|k|=R,y\): the three ranges contribute \(O(1)\), \(O(\log(y/R))\), \(O(1)\) to \(\sum|W|\), and \(O(R)\), \(O(y)\), \(O(y)\) to \(\sum|kW|\). |
| C7 | PASS | Each floor remainder is exactly \(\{N/d\}-\{(N+k)/d\}\), of modulus below one; summing \(|\chi_4(d)|\leq1\) over \(d\leq y\) gives \(y\). |
| C8 | PASS with notation repair | The tail is \(\ll_M y^MK_\delta^{1-M}\ll X^{1/2-\delta(M-1)}\). The last relation is \(\ll\) or \(\asymp\), not literal equality because of the floor in \(y\). Taking \(M-1\geq(A+1/4)/\delta\) gives \(O_{A,\delta}(RX^{-A})\). |
| C9 | PASS | Since \(K_\delta/X\asymp X^{-1/2+\delta}=o(1)\), positivity and \(N+k<2X\) follow. The stated \(\delta<1/4\) is more than sufficient; the later \(\delta<1/8\) is compatible. |
| C10 | PASS | On the positive localized window, \(|A_y(m)|\leq\tau(m)\ll_\varepsilon X^\varepsilon\), and bounded partial sums of \(\chi_4\) give \(c_y=O(1)\). |
| C11 | PASS | The exact recurrence is \(D_N(k)=\mathcal I_k(A_y-c_y)\). It gives \(|D_N(k)|\ll|k|X^\varepsilon\) for \(|k|\leq R\). |
| C12 | PASS | Using \(|W(k)|\ll R^{-1}\), the absolute cost is \(R^{-1}\sum_{|k|\leq R}|k|X^\varepsilon\ll RX^\varepsilon\). The displayed complex sum should be read in modulus. |
| C13 | PASS | Absolute convergence at fixed \(X\) justifies telescoping: \(\sum k(\widehat J(k)-\widehat J(k+1))=\sum\widehat J(k)=J(0)=0\). |
| C13a | PASS | For \(M>2\), the tail is \(\ll_M y^{M-1}K_\delta^{2-M}=yX^{-\delta(M-2)}\); choosing \(M-2\geq(A+1/4)/\delta\) makes it \(O(RX^{-A})\). |
| C14 | PASS | An oriented interval of length \(|k|\) contains at most \(1+|k|/2^{A_0}\) multiples of \(2^{A_0}\), and every retained coefficient is divisor-bounded. This is an exact cumulative projection onto all \(v_2\geq A_0\) increments. |
| C15 | PASS | C6 and C14 give \(X^\varepsilon(\log X+y/2^{A_0})\). Since \(2^{A_0}\geq R\geq y/R\), this is \(O_\varepsilon(RX^\varepsilon)\). The centering leakage has already been controlled by C13--C13a. |

Thus (122.C16) is correct only with the candidate's own qualification:
it denotes the low-two-adic projection of every cumulative increment. It
must not be read as the terminal condition \(v_2(N+k)<A_0\).

## Addendum 4. Boundary audit, cumulative central-pair proof, and repaired survivor

### Exact divisor boundaries C17--C24

For \(m=2^an\), \(n\) odd, the complement map \(d\mapsto q=n/d\)
gives

\[
 d>y\quad\Longleftrightarrow\quad q<n/y.
\tag{122.A2}
\]

Therefore C18 is exact. If \(d=y\), its partner satisfies \(q=n/y\)
and is excluded by the strict inequality; the hard sample is present
exactly once. When \(z=n/y=y\), the only central interval point is
\(d=y\), so on the odd branch

\[
 2A_y(y^2)=a(y^2)+\chi_4(y),
\tag{122.A3}
\]

with no half weight. An \(a=0\) equality case forces \(y\) odd. For
\(\chi_4(n)=-1\), divisor pairs have opposite signs and no square fixed
point, so \(a(n)=0\), the central character sum is exactly zero, and
C23 is a self-return.

For \(a\geq1\), the localized inequality \(N+k<2y^2\) gives
\(n=(N+k)/2^a<y^2\). Hence the relevant central interval is the exact
closed band \([n/y,y]\), and

\[
 n/y=\frac{N+k}{2^ay}=\frac{y}{2^a}
 +O\left(\frac{1+X^\delta}{2^a}\right).
\tag{122.A4}
\]

It is a wide band for every fixed \(a\geq1\), not the odd near-square
band. If \(n\leq y\), its complementary sum is empty because the
threshold is at most one and is strict. These facts validate C24 and
prevent the odd central-pair estimate from being transferred to even
branches.

### Revised cumulative argument C25--C28

Let \(L=1+X^\delta\). For an occurrence \((n,d)\) in \(C_-(n)\), put
\(q=n/d\). Since \(n/y\leq d\leq y\), one has

\[
 n/y\leq d,q\leq y.
\]

For an occurrence in \(C_+(n)\), \(y<d<n/y\) implies

\[
 y<d,q<n/y.
\]

Moreover, for \(n=N+j\), \(|j|\leq K_\delta\),

\[
 \left|\frac ny-y\right|
 \leq\frac{|j|+|N-y^2|}{y}
 \leq X^\delta+2+o(1)\ll L.
\tag{122.A5}
\]

Thus every occurrence maps to an ordered pair
\((d,q)\in([y-CL,y+CL]\cap\mathbb Z)^2\). The map

\[
 (n,d)\longmapsto(d,n/d)
\]

is injective, because \(n=dq\). It deliberately counts \((d,q)\) and
\((q,d)\) separately when \(d\ne q\), matching the two ordered divisor
occurrences; when the equality pair belongs to the odd branch (equivalently
\(y\) is odd), it counts \((y,y)\) once, and otherwise it counts no
equality occurrence. Consequently,

\[
 \sum_{|j|\leq K_\delta}|\Gamma(N+j)|
 \leq \#\{\text{central ordered occurrences}\}
 \ll L^2\ll(1+X^\delta)^2.
\tag{122.A6}
\]

This proves C27. If \(E(k)\) is the oriented cumulative sum of
\(\Gamma\), then \(\sup|E(k)|\leq\sum|\Gamma|\). Therefore

\[
 \sum_{|k|\leq K_\delta}|E(k)W(k)|
 \leq \left(\sum_{|j|\leq K_\delta}|\Gamma(N+j)|\right)
       \sum_k|W(k)|
 \ll X^{2\delta}\log X.
\tag{122.A7}
\]

For fixed \(\delta<1/8\), (122.A7) is
\(O_\varepsilon(RX^\varepsilon)\). The factor \(1/2\) in C26 only
improves this. No Abel transformation has been applied to a truncated
sum, so there is no missing endpoint term. C25--C28 pass exactly in their
revised cumulative form.

### First repair: the literal smallest survivor

For a localized positive increment \(m=2^an\), define

\[
 \mathscr V_{\delta}(m)=
 \begin{cases}
  \frac12a(n),&a=0,\ \chi_4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi_4(n)=-1,\\
  a(n)-\chi_4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\tag{122.A8}
\]

Let \(\mathcal I_k\) have the exact orientation in (122.H8). The
candidate's proved deletions yield the sharper exact reduction

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}
 W(k)\mathcal I_k\mathscr V_\delta
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{122.A9}
\]

The centering constant in (122.H9) is target-safe on this truncated
range by C13--C13a together with the already deleted central window.
Formula (122.A9), rather than the broader verbal description retaining
all C18 pieces, is the smallest survivor established by the candidate.
It retains the full-divisor and exact complementary pieces together on
every unresolved low even branch, retains the noncontracting odd
negative-character branch, and retains one half of the full coefficient
on the odd positive-character branch. It asserts no estimate for their
joint signed sum.

## Addendum 5. First doubtful step and control outcomes

The first unproved step remains

\[
 \sum_{R<|k|\leq K_\delta}
 W(k)\mathcal I_k\mathscr V_\delta
 \ll_\varepsilon RX^\varepsilon.
\tag{122.A10}
\]

Nothing in C4--C28 proves (122.A10). In particular, applying the desired
pointwise circle estimate to \(a(n)=r_2(n)/4\) is circular; bounding the
odd negative-character or low even branches separately by absolute value
returns capacities above target; and recombining C18 restores the
Round-121 discrepancy.

| Second-stage control | Outcome | Reason |
|---|---:|---|
| Uniform constants C4--C6 | PASS | Every derivative cost and transition width is explicit. |
| Tail and positivity C7--C9 | PASS | The tail is target-safe and the localized intervals never meet zero. |
| Central \(k\)-window C10--C12 | PASS | Divisor bounds give exactly the required \(R\) capacity. |
| Centering/high \(2\)-adic C13--C15 | PASS | Full telescoping plus uniform tail control validates the truncation; the projection is cumulative. |
| Strict \(q=n/y\) and hard \(d=y\) edge | PASS | C18 uses \(q<n/y\), so the equality partner is excluded exactly once. |
| Square tie C21a | PASS | The fixed divisor contributes \(\chi_4(y)\) once, with no half weight. |
| Even \(a\geq1\) repair C24 | PASS | Its threshold is \(y/2^a+O(X^\delta/2^a)\), so no false near-square claim remains. |
| Occurrence count C27 | PASS | The injective ordered-pair box has \(O((1+X^\delta)^2)\) elements. |
| Cumulative cost C28 | PASS | Supremum of the cumulative increment times \(\|W\|_{\ell^1}\) is target-safe for \(\delta<1/8\). |
| “Smallest survivor” wording | REVISE | Replace the broad Section-6 phrase by the exact piecewise survivor (122.A8)--(122.A9). |
| Complete target | FAIL/open | The signed survivor (122.A10) has no proved target bound. |

The unsigned control is unchanged: replacing \(\chi_4\) by one retains
one half of the full divisor coefficient and the exact square tie. Thus
the passed central correction does not convert the involution into a
generic contraction.

## Addendum 6. Dependencies and artifacts used

This second-stage audit used the conductor candidate
`rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/candidates/conductor_wavelet_localization_and_two_adic_split.md`
and the permitted artifacts already enumerated in Section 6 of the main
report. No Round-122 sibling report was read. The candidate, proof graph,
proof draft, validation matrices, synthesis, and conductor files were not
edited.

The proof of C27--C28 is wholly finite and algebraic. No numerical or
external-source input is used.

## Addendum 7. Recommended state effect and exact downstream scope

**Recommendation:** accept C4--C28 after the minor C8/modulus notation
repairs; revise the Section-6 smallest-survivor wording to
(122.A8)--(122.A9); promote only the exact reductions, target-safe
deletions, and scoped self-return. Do not promote the complete estimate.

The downstream scope is exact as follows.

- C4--C28 and (122.A9) do not prove
  `M9-M1-global-lower-radial-signed-estimate`, so that node remains open.
- Consequently GAR and the total-active M1 alternative remain open.
- Even a future proof of (122.A10) would feed the accepted global radial
  one-count assembly and the alternative total-M1 bridge; it would not
  prove blockwise `M9-M1` or the standard blockwise `M9` statement.
- No M2 parent, hard TOP, BAL, UNBAL, or `M9-M2` estimate is affected.
- Endpoint uniformity is not proved.
- Neither Gauss-circle bridge closes, and the internal and external
  discrepancy exponents are unchanged.

The only authorized continuation is a genuinely joint signed inequality
for (122.A10). Full-\(r_2\) completion followed by a circle bound,
residuewise or valuationwise absolute values, a second complement, or an
invertible Fourier/Abel return does not advance the proof.

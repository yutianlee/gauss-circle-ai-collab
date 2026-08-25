# Round 162 power, involution, and physical-scope seam review

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Role: independent seam review
- Reviewed candidate:
  `candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`
- Starting graph SHA-256:
  `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result: GREEN, with the candidate's hard-boundary quarantine required

The selected candidate is **GREEN** on the assigned seam.  Independent
recalculation confirms all of the following.

1. The character-Poisson coefficient is (i\chi _4(s)/2), not its
   negative.
2. For (Q=[a^2,c]), (R=[b^2,c]), the character-variable saddle is
   \[
    m_s={4XQd_2\over s^2},\qquad
    d_1^*={4XQ^2d_2\over s^2},\qquad
    F_s(m_s)={XQd_2\over s},
   \tag{1.1}
   \]
   with (JQ\le s\le2JQ), profile (W(XQ/(ys))), and normalized
   factor
   \[
     {2L^{3/2}J^{-1/2}\over Qd_2}.
   \tag{1.2}
   \]
3. The exact character transform is involutive.  At saddle level, the
   two inverse-square-root Hessian factors multiply to (4), the two
   Poisson constants multiply to (-1/4), reflection contributes the
   character sign (-1), and the two Gaussian phases cancel.  The total
   is (1).
4. Double Poisson has the exact scaled product locus and cone
   \[
      s\ell=XQR,qquad Q\ell\le Rs\le4Q\ell,
   \tag{1.3}
   \]
   and a smooth radial cell of physical length (L) gives
   \[
      |s\ell-XQR|\ll QRJ/L.
   \tag{1.4}
   \]
5. A smooth-interior dual pair has scale
   (L^{3/2}/(QR\sqrt J)), while the collar contains at most
   ((QRJ/L+1)(XQR)^\varepsilon) factor pairs.  The (QR)-powers
   cancel, leaving the positive central capacity (sqrt{JL}).
6. Grouping by (N=s\ell) gives exactly the scaled near-square divisor
   interval
   \[
      \sqrt{QN/R}\le s\le2\sqrt{QN/R}.
   \tag{1.5}
   \]
   For (Q=R=1), its unweighted completion is the
   (r_2(N)/4) divisor identity, but the complementary divisor window is
   not controlled.
7. The favorable single-opening comparison is
   \[
      \min\{L^2,\sqrt{JL}\}
       =L^{3/2}\min\{L^{1/2},H/L\}(1+o(1)).
   \tag{1.6}
   \]
   It is a method-capacity comparison only, not a bound or lower mass for
   the complete physical scalar.

No repair to the selected candidate is required.  Its explicit refusal
to select the discovery report's blanket target-safe hard-edge claim is
essential.  This review certifies only a compact smooth interior cell and
the exact transform algebra.  Literal hard boundaries, stars, profile
transitions, and their coupling to the Möbius aggregate remain in the
first open signed statement.

## 2. Exact statement and hypotheses reviewed

The reviewed scalar is the literal (t=1) close-factor face with
(d_1,d_2) squarefree and coprime, (d_1) odd, (d_2) possibly even,
and (d_2\le d_1\le4d_2).  All conclusions are uniform for one
arbitrary fixed real (X), with

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H.
\tag{2.1}
\]

Since (y=J+O(1)),

\[
 H=\sqrt J+O(1).
\tag{2.2}
\]

The exact projector opening is

\[
 \mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}
 =\sum_{a^2\mid d_1}\mu(a)
  \sum_{b^2\mid d_2}\mu(b)
  \sum_{c\mid(d_1,d_2)}\mu(c),
\tag{2.3}
\]

with (Q=[a^2,c]), (R=[b^2,c]).  The character kills every opening
with even (Q), so (a,c,Q) are odd.  No such restriction is placed on
(b,R,n), and the even-(d_2) branch survives.

The collar and pair-amplitude calculation is reviewed for a compact
smooth interior cell in the physical variables.  It does not assume that
the literal zero-extended coefficient is globally smooth.  Accordingly,
the result is a no-go for exact character Poisson followed by termwise
positive smooth-interior control, a second bare character transform, and
standard positive differencing.  It is not a no-go for a new signed
theorem acting on the whole coefficient before positive norms.

## 3. Independent proof and power derivation

### 3.1 Character sign and exact involution

Use (e(t)=e^{2\pi it}) and
\(\widehat g(\xi)=\int g(x)e(-\xi x)\,dx\).  From

\[
 \chi _4(m)={e(m/4)-e(-m/4)\over2i},
\tag{3.1}
\]

Poisson gives frequencies (k-\sigma/4).  Set
(s=4k-\sigma).  If (sigma=1), then (s\equiv3\pmod4); if
(sigma=-1), then (s\equiv1\pmod4).  In both cases
(sigma=-\chi _4(s)), so

\[
 {\sigma\over2i}={i\over2}\chi _4(s).
\tag{3.2}
\]

Therefore

\[
 \sum_m\chi _4(m)g(m)
 ={i\over2}\sum_{s\ {
m odd}}\chi _4(s)\widehat g(s/4).
\tag{3.3}
\]

For a second transform put (h(s)=\widehat g(s/4)).  Direct substitution
gives

\[
 \widehat h(\xi)=4g(-4\xi).
\tag{3.4}
\]

Hence the doubled transform is

\[
 \left({i\over2}\right)^2 4
 \sum_{u\ {
m odd}}\chi _4(u)g(-u)
 =-\sum_u\chi _4(u)g(-u)
 =\sum_u\chi _4(u)g(u),
\tag{3.5}
\]

where the last equality uses (chi _4(-u)=-\chi _4(u)).  This checks
both the sign and exact involution.

At the principal saddles, let (m>0) be the returned physical index.
The first phase has negative curvature and the returned phase

\[
 G(s)={XQd_2\over s}+{ms\over4}
\tag{3.6}
\]

has positive curvature.  At the paired saddle,

\[
 |F''(m)|G''(s_0)={1\over16}.
\tag{3.7}
\]

Thus the Hessian amplitudes multiply to (4).  Together with
((i/2)^2=-1/4), (chi _4(-m)=-\chi _4(m)), and
(e(-1/8)e(1/8)=1), this reproduces the exact unit return.

### 3.2 One-variable saddle, profile, and normalization

For fixed physical (d_2=Rn), the opened (m)-phase is

\[
 F_s(m)=J\sqrt{Qd_2m}-{s\over4}m.
\tag{3.8}
\]

Solving (F_s'(m)=0) gives (1.1), and

\[
 F_s''(m_s)=-{s^3\over32XQd_2}.
\tag{3.9}
\]

The cone (1\le d_1^*/d_2\le4) gives (JQ\le s\le2JQ).  The exact
profile calculation is

\[
 \sqrt{{q_Xd_1^*\over4d_2}}
 =\sqrt{{X\over y^2}{XQ^2\over s^2}}
 ={XQ\over ys}.
\tag{3.10}
\]

Finally,

\[
\begin{aligned}
 \left({L^2\over d_1^*d_2}\right)^{3/4}
 |F_s''(m_s)|^{-1/2}
 &={L^{3/2}s^{3/2}\over
      4^{3/4}X^{3/4}Q^{3/2}d_2^{3/2}}
   {\sqrt{32XQd_2}\over s^{3/2}}\\
 &={2L^{3/2}J^{-1/2}\over Qd_2}.
\end{aligned}
\tag{3.11}
\]

The (i/2) Poisson factor and (2e(-1/8)) stationary factor give
(ie(-1/8)=e(1/8)).  Every constant and power in the candidate is
correct.

### 3.3 Rank one, per-pair amplitude, and the product collar

After Poisson in both rescaled variables, set

\[
 u=Qm=tw,\qquad v=Rn=t/w.
\tag{3.12}
\]

Since (dm\,dn=du\,dv/(QR)) and
(du\,dv=2t\,dt\,dw/w), the normalized amplitude before angular
stationary phase is

\[
 {2L^{3/2}\over QRw}\,t^{-1/2}
\tag{3.13}
\]

times bounded literal profiles on the smooth cell.  The phase is

\[
 t\Psi(w),\qquad
 \Psi(w)=J-{s\over4Q}w-{\ell\over Rw}.
\tag{3.14}
\]

Its angular saddle and residual radial frequency are

\[
 w_0^2={4Q\ell\over Rs},\qquad
 \delta=J-\sqrt{{s\ell\over QR}}.
\tag{3.15}
\]

On the central collar, (t\asymp L) and

\[
 |t\Psi''(w_0)|\asymp LJ.
\tag{3.16}
\]

The transverse factor is therefore ((LJ)^{-1/2}).  Multiplying it by
the physical amplitude and integrating over radial length (L) gives

\[
 {L^{3/2}\over QR\sqrt J}
\tag{3.17}
\]

per pair.  Equivalently, the exact leading reduction is a bounded
(dt/t) radial integral with prefactor
(2L^{3/2}/(QR\sqrt J)).

The radial Fourier window is (|\delta|\ll L^{-1}).  Rationalizing the
square roots on (s\ell\asymp XQR) yields

\[
 |s\ell-XQR|
 =QR\left|\sqrt{{s\ell\over QR}}-J\right|
      \left(\sqrt{{s\ell\over QR}}+J\right)
 \ll {QRJ\over L}.
\tag{3.18}
\]

This checks the collar and all (Q,R) powers.

### 3.4 Pair count, (QR)-cancellation, and the missing power

Put (N=s\ell).  The collar in (3.18) contains
(O(QRJ/L+1)) possible integers (N).  For each (N), the number of
factor pairs in the dual boxes is (O_\varepsilon((XQR)^\varepsilon)).
Thus

\[
 \#\{(s,\ell)\}_{\rm collar}
 \ll_\varepsilon
 \left({QRJ\over L}+1\right)(XQR)^\varepsilon.
\tag{3.19}
\]

In the assigned range (1\ll L\ll H\asymp\sqrt J), the (+1) term
is dominated.  Multiplying (3.19) by (3.17) gives

\[
 {QRJ\over L}{L^{3/2}\over QR\sqrt J}
 =\sqrt{JL}.
\tag{3.20}
\]

There is no residual saving in (Q) or (R).  Combining this favorable
single-opening central ledger with the (L^2) trivial scale gives

\[
\begin{aligned}
 \min\{L^2,\sqrt{JL}\}
 &=L^{3/2}\min\left\{L^{1/2},{\sqrt J\over L}\right\}\\
 &=L^{3/2}\min\{L^{1/2},H/L\}(1+o(1)).
\end{aligned}
\tag{3.21}
\]

This becomes target-scale only at (L\asymp H).  On polynomial
intermediate blocks it leaves a fixed-power loss, and when
(H\ge L^{3/2}) it leaves the full (L^{1/2}).  Equation (3.21) is not
an estimate for the complete physical Möbius sum: it is the favorable
coefficient-insensitive scale left by the selected route.

### 3.5 Local divisor grouping

The physical cone is (1\le w^2\le4).  Using
(w_0^2=4Q\ell/(Rs)), it becomes

\[
 Q\ell\le Rs\le4Q\ell.
\tag{3.22}
\]

With (N=s\ell), (3.22) is equivalent to

\[
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}.
\tag{3.23}
\]

The exact dual sign is (chi _4(s)), so the grouped smooth interior is

\[
 \sum_{\substack{s\mid N,\ s\ {
m odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi _4(s)\mathcal K_{Q,R}(N;s).
\tag{3.24}
\]

For (Q=R=1), removing the weight and completing the divisor interval
would give

\[
 \sum_{s\mid N}\chi _4(s)=r_2(N)/4.
\tag{3.25}
\]

The candidate correctly treats (3.25) as a return to the parked
full-divisor interface, not as cancellation in the truncated window.

### 3.6 Möbius and physical-scope quarantine

The factor (1/(QR)) in (3.17) is a Jacobian/stationary factor for one
opened sublattice.  It cannot be summed as a gain after positive norms,
because its collar width contains the compensating factor (QR).  Nor
may the opening signs (mu(a)\mu(b)\mu(c)\chi _4(Q)) be discarded: the
whole physical projector is their coupled sum.

The selected candidate consistently describes (sqrt{JL}), (L^2),
and (3.21) as capacities.  It makes no assertion that the physical
coefficient attains them, no lower bound, no nonzero-row density claim,
and no arbitrary-centre phase-alignment argument.  This quarantine is
mathematically necessary and is correctly stated.

## 4. First doubtful or unproved step

The first unproved step remains a target-strength estimate for the whole
signed aggregate

\[
 {L^{3/2}\over\sqrt J}
 \sum_{a,b,c}{\mu(a)\mu(b)\mu(c)\chi _4(Q)\over QR}
 \sum_{N\approx XQR}
 \sum_{\substack{s\mid N,\ s\ {
m odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi _4(s)\mathcal K_{Q,R}(N;s),
\tag{4.1}
\]

with arbitrary real (X), all literal profiles, collar tails, hard
boundaries, floors, stars, and the even-(d_2) branch retained before
every positive norm.  The smooth principal display (4.1) does not own the
omitted boundary pieces.

The first invalid continuation would be either to take moduli over
((a,b,c)) and claim a hidden (QR)-saving, or to complete the local
divisor interval to (r_2/4) without controlling its complement.  A
second bare character transform is exactly the identity, while standard
positive differencing makes the character constant in each correlation.
No reviewed artifact proves the missing signed theorem.

## 5. Control tests and outcomes

| Seam control | Outcome |
|---|---|
| Character-Poisson sign | GREEN by (3.1)--(3.3): the coefficient is (i\chi _4(s)/2). |
| One-variable saddle and phase | GREEN by (3.8)--(3.9): (d_1^*=4XQ^2d_2/s^2) and phase (XQd_2/s). |
| Literal profile substitution | GREEN for the interior saddle: (W(XQ/(ys))), with (y=\lfloor J\rfloor) unchanged. |
| Normalized constant | GREEN by (3.11): (2L^{3/2}J^{-1/2}/(Qd_2)), with leading phase (e(1/8)). |
| Exact involution | GREEN by (3.4)--(3.7): reflection, character sign, Fourier scaling, Hessians, and Gaussian factors give unit return. |
| Rank-one geometry | GREEN: one transverse direction and one radial Fourier direction; no determinant division. |
| Product collar | GREEN for a compact smooth interior cell: (s\ell=XQR) and width (QRJ/L). |
| Pair amplitude and count | GREEN: (L^{3/2}/(QR\sqrt J)) times ((QRJ/L+1)(XQR)^\varepsilon). |
| (QR)-cancellation | GREEN by (3.20); no modulus gain remains. |
| Missing-power scope | GREEN: the favorable factor is (min\{L^{1/2},H/L\}), target-scale only at (L\asymp H). |
| Local divisor grouping | GREEN by (3.22)--(3.25); completion adds an uncontrolled complement. |
| Even-(d_2) and Möbius scope | GREEN: only the first opened leg is forced odd; all opening signs remain coupled. |
| Literal hard boundaries | OPEN, correctly quarantined by the selected candidate.  The discovery report's blanket target-safe edge claim is not certified. |
| Physical-capacity direction | GREEN: no route capacity is promoted as physical mass, an upper bound for the full scalar, or a lower bound. |
| Downstream scope | GREEN: no remaining few-point channel, hard-TOP parent, M9--M2, M9, bridge, or exponent follows. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This review used exactly:

1. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/controls/conductor_round162_reproduction_and_selection.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/literal_t1_character_poisson_attack.md`.

Every sign, constant, scaling factor, divisor interval, and restored power
was independently recomputed above.  No sibling report, excluded
Round-162 artifact, external source, or numerical control was used.

## 7. Recommended state effect

Recommend **GREEN** for the selected candidate on the
power/involution/physical-scope seam and no textual repair to its selected
kernel.

If the conductor creates
`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`, its
statement should retain the candidate's exact limitations:

- certify the character sign, exact involution, smooth-interior scaled
  collar, (QR)-cancellation, local divisor return, positive capacity,
  and standard positive-differencing obstruction;
- leave literal hard-boundary and profile-transition families inside the
  first open signed aggregate;
- describe (min\{L^2,\sqrt{JL}\}) only as a favorable route capacity;
  and
- prohibit every physical lower-bound, full-(t=1) target, remaining
  few-point, hard-TOP, M9--M2, M9, bridge, or exponent inference.

The appropriate terminal label remains
`hard_top_t1_close_factor_bilinear_no_go`.

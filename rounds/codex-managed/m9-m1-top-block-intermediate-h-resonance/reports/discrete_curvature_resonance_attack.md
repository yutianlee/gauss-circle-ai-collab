# Round 56 discovery report: discrete-curvature averaging misses a full singleton shell

## 1. Result: exact resonance interface and sharp scoped no-go

Let \(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and let \(J\) be a
consecutive product window of length at most \(R\). After splitting odd
\(q\) into \(q=4m+\rho\), \(\rho\in\{1,3\}\), the exact first and second
phase differences are

\[
 \Delta F_{h,\rho}(m)
 =\frac{4\sqrt{Xh}}{\sqrt{q+4}+\sqrt q},                    \tag{1.1}
\]

\[
 \boxed{
 \Delta^2F_{h,\rho}(m)
 =-\frac{32\sqrt{Xh}}
 {(\sqrt{q+8}+\sqrt{q+4})
  (\sqrt{q+4}+\sqrt q)
  (\sqrt{q+8}+\sqrt q)}.}                                  \tag{1.2}
\]

Thus the lawful resonance parameter is
\(\|\Delta^2F_{h,\rho}(m)\|_{\mathbb R/\mathbb Z}\), or, after one Weyl
shift by \(r\), the exact accumulated parameter

\[
 \left\|\sum_{\ell=0}^{r-1}
 \Delta^2F_{h,\rho}(m+\ell)\right\|_{\mathbb R/\mathbb Z}.  \tag{1.3}
\]

Large continuous curvature alone is irrelevant modulo the integer
lattice.

The proposed nonnegative averaged-resonance route nevertheless has a sharp
actual-profile obstruction. The residual range contains a dyadic shell
\[
 R/4<h<R/2
\]
on which every fixed-\((h,\rho)\) progression has at most one point in
\(J\). There is then no first or second difference to exploit. For an
explicit infinite family \(X=K^4\), a star-free top-profile plateau window
contains \(\gg K\asymp R\) such residuewise singleton blocks, each of
amplitude bounded below. Consequently

\[
 \sum_{h,\rho}\left|T_{h,\rho}(J)\right|\gg R,               \tag{1.4}
\]

whereas the required unweighted window capacity is
\(O_\varepsilon(X^\varepsilon\sqrt R)\). In normalized variables (1.4)
is \(\gg R^{-1/2}=Y^{-1/4}\), while the target is
\(R^{-1}=Y^{-1/2}\).

This is a no-go only for summing fixed-\(h\), fixed-residue curvature or
resonance majorants. It is not a signed lower bound for
\(W_J^{\rm core}\). Cancellation between the two residue classes, between
distinct \(h\), or after grouping by the product \(n=hq\) remains possible
and is the exact survivor.

## 2. Exact statement and hypotheses

For \(q=4m+\rho\), define the consecutive integer set

\[
 \mathcal M_{h,\rho}(J)
 =\{m\in\mathbb Z: h(4m+\rho)\in J\}
\]

and the complete actual amplitude

\[
 a_{h,\rho}(m)
 =\tau_X(hq)\Omega_X^*(hq,h)(hq)^{-3/4},                    \tag{2.1}
\]

where \(\tau_X\) is the inherited radial star. The fixed-residue block is

\[
 T_{h,\rho}(J)
 =\chi_4(\rho)\sum_{m\in\mathcal M_{h,\rho}(J)}
 a_{h,\rho}(m)e(F_{h,\rho}(m)),\qquad
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)}.                          \tag{2.2}
\]

Every artificial endpoint of \(\mathcal M_{h,\rho}(J)\) has full weight.
Only an inherited radial or angular equality star may contribute a half
weight. The cardinality obeys

\[
 M_{h,\rho}:=\#\mathcal M_{h,\rho}(J)
 \leq \frac{|J|-1}{4h}+1\leq\frac R{4h}+1.                 \tag{2.3}
\]

The exact finite Weyl identity, with all profile coefficients retained, is

\[
\begin{split}
 \left|\sum_{m\in\mathcal M}a_m e(F_m)\right|^2
 ={}&\sum_{m\in\mathcal M}|a_m|^2\\
 &+2\operatorname {Re}\sum_{1\leq r<M}
 \sum_{\substack{m,m+r\in\mathcal M}}
 a_{m+r}\overline{a_m}
 e(F_{m+r}-F_m).                                           \tag{2.4}
\end{split}
\]

For the shifted phase \(G_r(m)=F(m+r)-F(m)\),

\[
 \Delta G_r(m)
 =\sum_{\ell=0}^{r-1}\Delta^2F(m+\ell).                    \tag{2.5}
\]

Equations (2.4)--(2.5) are the exact modulo-one resonance interface. A
first-derivative estimate on a monotone piece is lawful only after
\(\|\Delta G_r(m)\|\) is bounded away from zero there; integer crossings
must be retained as resonance pieces.

For a dyadic \(h\)-shell \(H<h\leq2H\), define the exact resonance count

\[
\begin{split}
 \mathscr N_{H,r}(\delta;J)
 =\sum_{H<h\leq2H}\sum_{\rho\in\{1,3\}}
 \#\Big\{m:\;&m,m+r,m+1,m+r+1\in\mathcal M_{h,\rho}(J),\\
 &\|\Delta G_{h,\rho,r}(m)\|\leq\delta\Big\}.               \tag{2.6}
\end{split}
\]

This count does not discard the shift \(r\), the residue class, or window
edges. However, every majorant derived from (2.4) also contains the
nonnegative diagonal/boundary baseline

\[
 \mathscr D_H(J)=
 \sum_{H<h\leq2H}\sum_{\rho}
 \sum_{m\in\mathcal M_{h,\rho}(J)}|a_{h,\rho}(m)|^2.        \tag{2.7}
\]

The theorem proved below is:

> **Singleton-shell no-go.** There are infinitely many perfect fourth
> powers \(X\), top windows \(J\), and strict actual-profile incidences
> with \(3R/8\leq h\leq7R/16\) such that every
> \(\mathscr N_{H,r}(\delta;J)\) is empty for \(r\geq1\), but the sum of
> the residuewise block moduli is \(\gg R\) before radial normalization.
> Therefore no theorem controlling only the averaged resonance counts
> (2.6), followed by nonnegative summation over \(h,\rho\), can prove the
> \(O(\sqrt R)\) window target.

## 3. Proof and derivation

### 3.1 Exact discrete curvature and its drift

Put \(A=\sqrt{Xh}\) and \(q=4m+\rho\). Rationalizing gives

\[
 \Delta F(m)=A(\sqrt{q+4}-\sqrt q)
 =\frac{4A}{\sqrt{q+4}+\sqrt q},
\]

which proves (1.1). Taking one more difference,

\[
\begin{split}
 \Delta^2F(m)
 &=4A\left\{
 \frac1{\sqrt{q+8}+\sqrt{q+4}}
 -\frac1{\sqrt{q+4}+\sqrt q}\right\}\\
 &=-\frac{32A}
 {(\sqrt{q+8}+\sqrt{q+4})
  (\sqrt{q+4}+\sqrt q)
  (\sqrt{q+8}+\sqrt q)},
\end{split}
\]

proving (1.2). On \(hq\asymp Y\),

\[
 \Delta F(m)\asymp Rh,\qquad
 |\Delta^2F(m)|\asymp\frac{h^2}{R}.                         \tag{3.1}
\]

The third continuous derivative in the \(m\)-variable is

\[
 F'''(m)=24\sqrt{Xh}(4m+\rho)^{-5/2},
\]

and the integral representation of finite differences gives

\[
 |\Delta^3F(m)|\asymp\frac{h^3}{R^3}.                       \tag{3.2}
\]

Thus across the full \(M_h\ll R/h+1\) progression, the discrete curvature
drifts by at most

\[
 M_h\sup|\Delta^3F|
 \ll\frac{h^2}{R^2}+\frac{h^3}{R^3}.                       \tag{3.3}
\]

My initial packet read preceded its correction and displayed
\(O(h^3/R^2)\). Equation (3.2) independently derives the corrected
\(h^3/R^3\) formula now present in the packet; every subsequent estimate
in this report uses the corrected scale.

Because \(\chi_4(4m+\rho)=\chi_4(\rho)\), the character creates no hidden
linear term after this residue split. If instead one writes \(q=2m+1\),
the exact extra phase is \(m/2\); its second difference is zero. Either
description gives precisely the same discrete curvature.

### 3.2 Why (2.6) is the lawful large-curvature object

Expanding the square proves (2.4), and telescoping first differences proves
(2.5). On any piece where \(\Delta G_r\) is monotone and remains at
distance at least \(\delta\) from every integer, elementary summation of
successive phase ratios followed by Abel summation gives

\[
 \left|\sum b_m e(G_r(m))\right|
 \ll \delta^{-1}
 \left(\sup_m|b_m|+\sum_m|b_{m+1}-b_m|\right).              \tag{3.4}
\]

When \(\Delta G_r\) crosses an integer, (3.4) must be restarted, and the
near-integer samples are exactly what (2.6) records. Thus (2.6), together
with the diagonal (2.7) and all boundary pieces, is a legal formulation of
the large-curvature method. Replacing (1.2) by its absolute size
\(h^2/R\) before reducing modulo one is not legal.

The accepted Round-55 sampled-BV theorem applies separately to each
fixed-\(h\) product window:

\[
 \sup_m|a_{h,\rho}(m)|
 +\sum_m|a_{h,\rho}(m+1)-a_{h,\rho}(m)|
 \ll Y^{-3/4}.                                               \tag{3.5}
\]

This retains every height floor, the hard top, angular equality stars, and
the radial star. It licenses Abel summation in (3.4), but it does not
couple different \(h\)'s and does not remove the diagonal baseline.

### 3.3 The high-shell geometric obstruction

If \(h>R/4\), then two values in one residue class differ in product by
\(4h>R\). Hence (2.3) sharpens to

\[
 M_{h,\rho}\leq1.                                           \tag{3.6}
\]

There are no shifted pairs in (2.4), no discrete increments, and
\(\mathscr N_{H,r}(\delta;J)=0\) for every \(r\geq1\), every \(\delta\),
and every shell contained in \((R/4,R/2]\). The fixed-residue block is
nevertheless one complete term whenever it is nonempty. This proves,
before constructing any special \(X\), that perfect control of all
curvature resonances cannot control the high-shell boundary baseline.

### 3.4 Strict actual-profile fourth-power family

Let \(K\) run through positive multiples of \(16\), and set

\[
 X=K^4,\qquad Y=K^2,\qquad R=K,
\]

\[
 J_K=[K^2-K/2,\ K^2+K/2-1]\cap\mathbb Z,
\qquad
 \mathcal H_K=[3K/8,\ 7K/16]\cap\mathbb Z.                  \tag{3.7}
\]

The window has exactly \(K=R\) integers. For every
\(h\in\mathcal H_K\), the products \(h(2\mathbb Z+1)\) form an arithmetic
progression of spacing \(2h\leq7K/8<K\). Any half-open interval of length
\(K\) therefore contains at least one such product, so \(J_K\) contains
some \(hq\) with \(q\) odd. In either fixed residue class the spacing is
\(4h\geq3K/2>K\), so that class contributes at most one product.

For every such incidence,

\[
 \frac{2\sqrt{Xh/q}}{\sqrt X}
 =\frac{2h}{\sqrt{hq}}
 \in\left[
 \frac{3/4}{\sqrt{1+1/(2K)}},
 \frac{7/8}{\sqrt{1-1/(2K)}}\right]
 \Subset(2/3,1)                                             \tag{3.8}
\]

for all sufficiently large \(K\). Thus the top profile is strictly on its
unit plateau, every finer profile is zero, and no hard or equality star is
met. Moreover

\[
 H_0=\left\lfloor K^2X^{-1/4}\right\rfloor=K,\qquad h<K,
\]

so the height cutoff is strict. The radial product is near \(K^2\), far
from the global endpoint \(16K^2\). Therefore

\[
 \Omega_X^*(hq,h)=\Phi\left(\frac h{K+1}\right).             \tag{3.9}
\]

The accepted monotonicity of \(\Phi\), together with
\(h/(K+1)<1/2\) and \(\Phi(1/2)=1/2\), gives

\[
 \Omega_X^*(hq,h)\geq\frac12.                               \tag{3.10}
\]

Let

\[
 \widetilde T_{h,\rho}(J_K)
 =\chi_4(\rho)
 \sum_{m\in\mathcal M_{h,\rho}(J_K)}
 \Omega_X^*(hq,h)e(\sqrt{Xhq})
\]

be the unweighted residue block. It contains at most one term, and at
least one of the two residue blocks is nonempty for each
\(h\in\mathcal H_K\). Hence

\[
 \sum_{h\in\mathcal H_K}\sum_{\rho\in\{1,3\}}
 |\widetilde T_{h,\rho}(J_K)|
 \geq\frac12\#\mathcal H_K\gg K=R.                          \tag{3.11}
\]

All terms in (3.11) are actual-profile, strict, and star-free. Restoring
\((hq)^{-3/4}\asymp K^{-3/2}=R^{-3/2}\) gives residuewise absolute mass
\(\gg R^{-1/2}\), proving (1.4) and the normalized obstruction.

This does not assert that the complex numbers in (3.11) have one sign.
Taking their absolute values is precisely the fixed-leg majorant step
being refuted.

### 3.5 Perfect-fourth-power rational check

At \(X=K^4\) and \(hq=K^2+O(K)\), (1.2) also gives

\[
 \Delta^2F_{h,\rho}(m)
 =-\frac{4h^2}{K}
 +O\left(\frac{h^2}{K^2}+\frac{h^3}{K^3}\right).            \tag{3.12}
\]

If \(K=T^2\) and \(h\) is a multiple of \(T\), the leading term in
(3.12) is an integer. Thus neither a uniform first-derivative gap nor a
uniform irrational-curvature assertion is available. For \(h\asymp K\),
the correction in (3.12) can be of order one, so the leading rational
term must not be substituted for the exact curvature (1.2). The singleton
obstruction (3.11) is stronger: in that shell there is no discrete
curvature sample at all, resonant or nonresonant.

### 3.6 Full \(H/R\) exponent ledger

On a dyadic shell \(h\asymp H\), \(L<H\leq R/2\),

\[
 \#\{h\}\asymp H,\qquad M_h\asymp R/H,\qquad
 \text{absolute incidence capacity}\asymp R.                \tag{3.13}
\]

The exact unweighted ledger is:

| method on one \(h\)-shell | aggregate bound | excess over \(\sqrt R\) |
|---|---:|---:|
| absolute/trivial | \(R\) | \(\sqrt R\) |
| optimistic independent square-root in each \(h\) | \(\sqrt{HR}\) | \(\sqrt H\) |
| Round-55 curvature, \(H\leq\sqrt R\) | \(H\sqrt R\) | \(H\) |
| trivial crossover, \(H>\sqrt R\) | \(R\) | \(\sqrt R\) |
| required window target | \(\sqrt R\) | \(1\) |

If \(H=R^\eta\), the optimistic independent square-root exponent is
\((1+\eta)/2\), while the target exponent is \(1/2\). Thus even ideal
fixed-\(h\) cancellation still needs a further \(R^{\eta/2}\) interaction
between \(h\)-legs. At \(H\asymp R\), (3.11) shows that the full
residuewise majorant capacity \(R\) is actually attained.

After multiplication by \(Y^{-3/4}=R^{-3/2}\), the absolute \(R\) row is
\(R^{-1/2}=Y^{-1/4}\), while the target row is
\(R^{-1}=Y^{-1/2}\). The missing normalized factor is
\(R^{-1/2}=Y^{-1/4}\).

## 4. First doubtful or unproved step

The first unproved step is a genuinely signed estimate that keeps the
sum over \(h\) and both character residue classes outside absolute values:

\[
 \left|
 \sum_{\substack{hq\in J,\ q\ {\rm odd}\\L<h\leq\sqrt{hq}/2}}
 \chi_4(q)\Omega_X^*(hq,h)e(\sqrt{Xhq})
 \right|
 \ll_\varepsilon X^\varepsilon\sqrt R.                     \tag{4.1}
\]

On the shell \(R/4<h<R/2\), each fixed residue is a singleton, so (4.1)
is a short-hyperbola-strip sum rather than a one-dimensional curvature
sum. Equivalently, grouping by \(n=hq\) turns it into a signed restricted
divisor coefficient against the radial square-root phase. No permitted
accepted theorem controls this cross-\(h\), cross-residue object.

For lower shells \(L<h\leq R/4\), the exact resonance counts (2.6) remain
a lawful diagnostic, but bounding them nonnegatively and then summing
fixed-\(h\) bounds still encounters the \(\sqrt H\) loss in the optimistic
row of the ledger. A successful continuation must use a signed bilinear
average in \(h\) (or product grouping), not only improve spacing estimates
for \(\Delta^2F\).

The physical estimate (4.1), if proved, would still require a separate
alpha-mask, connector, Plemelj-order, and outside-height transfer theorem.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| `odd_q_discrete_phase` | Pass. Equations (1.1)--(1.2) are exact after \(q=4m+\rho\); the character is the constant \(\chi_4(\rho)\). |
| `large_curvature_mod_one` | Pass/no-go. The lawful shifted parameter is (1.3), not \(|F''|\). For \(h>R/4\) it is undefined because every residue block has at most one sample. |
| `resonance_spacing_average` | Sharp failure as a complete method. All counts (2.6) vanish on the singleton shell, while the actual residuewise majorant has mass \(\gg R\). |
| `actual_profile_amplitude` | Pass. Fixed-leg BV is retained in (3.5); the obstruction uses the exact top plateau and exact Vaaler factor (3.9), bounded below in (3.10). |
| `hyperbola_window_edges` | Pass. The sets \(\mathcal M_{h,\rho}(J)\) are exact consecutive intervals, artificial endpoints have full weight, and the fourth-power witness is strictly away from inherited stars. |
| `perfect_fourth_power` | Pass. The witness itself has \(X=K^4\); (3.12) exhibits the possible rational leading curvature and explains why exact modulo-one data are mandatory. |
| `target_exponent_ledger` | Pass. Section 3.6 records every \(H,R\) power before and after radial normalization. |
| `low_leg_overlap` | Pass. Every witness has \(h\geq3R/8\gg L\); the accepted \(h\leq L\) margin is never reinserted, and \(h=L\) is excluded. |
| `alpha_scope` | Pass. The report proves only a physical fixed-leg-majorant no-go; no alpha transfer is inferred. |
| `downstream_scope` | Pass. The signed residual core, GAR, M9-M1, M9, and the Gauss-circle target remain open. |

## 6. Dependencies and exact artifacts used

Only the task-authorized artifacts were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md`;
- `rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.

All finite-difference, hyperbola-strip, profile, resonance, and exponent
arguments are internal. No external theorem, web source, or numerical
experiment was used. The report is 100% analytical/algebraic.

## 7. Recommended state effect

Promote, after independent seam validation, a scoped
`top-block-discrete-curvature-singleton-no-go` node containing:

1. the exact discrete differences (1.1)--(1.3);
2. the corrected third-difference and curvature-drift scales
   (3.2)--(3.3);
3. the fact that all fixed-residue resonance counts vanish for
   \(h>R/4\);
4. the strict fourth-power actual-profile capacity witness
   (3.7)--(3.11);
5. the residual \(H/R\) ledger in Section 3.6.

Reject any claim that averaging nonnegative fixed-\(h\) curvature-resonance
losses alone proves the \(\sqrt R\) window target. The next proof kernel
must retain the signed sum across \(h\) and the two \(\chi_4\) residue
classes, preferably as the exact short-hyperbola-strip/product-fiber
operator (4.1).

Do not promote (4.1), the full shifted correlation, GAR, the alpha
transition, M9-M1, M9, or the final theorem.

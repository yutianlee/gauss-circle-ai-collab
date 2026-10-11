# Independent review of the actual signed-bin input

## 1. Result and review verdict

Campaign: `gc-signed-near-frequency-cancellation`. Round: 210.
Role: independent nonblind seam reviewer, following the separate completed
`actual_shifted_correlations` task. Generated: 2026-09-27T15:39:27Z.
Graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: entirely analytical; no mathematical numerical experiment or new
external source import.

**GREEN for the scoped claims in the final hash-bound report.** The smooth-bin transfer, the maximum-label
prefix decomposition, the normalized reverse-bin estimate, the actual
static-prefix envelope, joint interval variance, and the bound
\(\mathcal E_N\ll H^9T^\varepsilon\) are correct. They yield
\(\int_J|Q_N|^{10}\ll XH^9T^\varepsilon\), which is quantitatively
insufficient on the entire required band.

One boundary convention was clarified in the reviewed report:
its lattice formulas (20)--(22) apply for \(0\le r\le L\); for the
declared zero prefix set \(a_{-1}(n)=0\) for every integer \(n\), and
for padded labels use \(a_r=a_L\) when \(r>L\). This is already the
polynomial convention \(S_{-1}=0\), \(S_r=S_L\), and changes no estimate.
It was sent immediately to the conductor and repaired by the claimant with
the conductor's authorization. I checked the saved clarification; the final
claimant hash is recorded in Section 7. No power or analytic repair was needed.

## 2. Exact object and scope

The reviewed quantities are those in
`reports/signed_rational_bins.md`: \(X=T^2\), \(H=T/\sqrt N\),
\(Y=[1/2,3]\), \(J=XY\), \(h_y=2H\sqrt y\), and
\(T^{166/325}<N<T^{242/325}\). Width variation is part of each
coefficient \(C_{I,\mu}(h_y)\). The full input is

\[
 \mathcal E_N=\sum_{I\in\mathscr I}\sum_j
      \int_Y(|f_{I,j}|^2+|f'_{I,j}|^2)\,dy,
\quad
 f_{I,j}=\sum_\mu\rho(X\mu-j)C_{I,\mu}(h_y)
                         e(-y(X\mu-j)).                 \tag{R1}
\]

This is a normalized energy in \(y\), not a physical integral in
\(x\) or \(z\). The transfer multiplies it by \(X\). All canonical
dyadic intervals of the maximum quotient label occur in its definition;
there is no substitution of the unmasked fifth polynomial's energy.

The sign of the second arm is consistent with the exact Fourier convention:
\(\sum_{a\bmod4}\chi_4(a)e(ka/4)=2i\chi_4(k)\). Both arms in
the claimant therefore agree with its lattice representation and the
inherited Round209 orientation. The strict cutoff is
\(p(x)=\min(L,\lceil x/D\rceil-1)\), including integer equality
points. No derivative of this discontinuous prefix is used.

## 3. Independent derivations and cost audit

### Smooth bins, Sobolev transfer, and maximum labels

The stated bump construction produces a smooth partition of unity
\(\sum_j\rho(t-j)=1\), supported in translates of \((-3/4,3/4)\).
On \((-1/4,1/4)\) only the central bump contributes, so the stated
plateau control is valid. Every frequency enters a bounded number of bins,
and its actual offset remains in (R1).

For arbitrary finite \(f_j\in H^1(Y)\), use one common bounded extension
to \(H^1(\mathbb R)\). After Fourier transformation, Cauchy with
weights \(1+|\xi+j|^2\) and the bounded sum of their reciprocals gives

\[
 \Big\|\sum_je(-jy)f_j(y)\Big\|_{L^2(Y)}^2
 \ll\sum_j\|f_j\|_{H^1(Y)}^2.                            \tag{R2}
\]

The same extension is used for each index; constants are independent of
the number of indices. The claimant's example \(f_j=e(jy)\) correctly
refutes an unrestricted derivative-free version. Its two-offset example
also correctly distinguishes a zero coefficient sum from a nonzero
internally modulated bin. Neither is represented as an actual arithmetic
counterexample.

The telescoping identity
\(G_\ell=S_\ell^5-S_{\ell-1}^5\) assigns every ordered fifth-product
term to its largest label. A prefix decomposes into at most
\(K=O(\log(2L+2))\) canonical disjoint intervals. Cauchy consequently
gives exactly

\[
 \int_J|Q_N|^{10}\le K\sum_{I\in\mathscr I}
      \int_J|P_I(x;h(x))|^2\,dx
 \ll XK\mathcal E_N.                                    \tag{R3}
\]

The full interval sum survives; the factor \(K\) is not secretly an
estimate of that sum. Padding adds zero label increments and introduces
no additional term once the zero-prefix convention is explicit.

### Periodized Parseval and the normalization

For a finite polynomial \(V(z)=\sum_\mu d_\mu e(-\mu z)\) and a
smooth compactly supported multiplier \(\psi\), Fourier inversion gives

\[
 \sum_\mu\psi(X\mu-j)d_\mu e(-\mu z_0)
  =\int_{\mathbb R}\widehat\psi(u)V(z_0-Xu)e(-ju)\,du.
\]

Periodize the integrand modulo one. Parseval bounds the sum of squared
Fourier coefficients by its periodized square norm. Cauchy in the
periodizing integer, with the summable weights
\((1+|u|)^{-2}\), bounds that norm by

\[
 C\int_{\mathbb R}(1+|u|)^2|\widehat\psi(u)|^2
                                      |V(z_0-Xu)|^2\,du.
\]

Schwartz decay proves the claimant's (18) for any fixed exponent \(A\).
There is no spacing hypothesis and no omitted physical convolution tail.
The crucial change of variable is

\[
 \int(1+|u|)^{-A}|V(z_0-Xu)|^2\,du
  =X^{-1}\int\left(1+|z-z_0|/X\right)^{-A}|V(z)|^2\,dz.
                                                               \tag{R4}
\]

Hence a physical norm \(O(XH)\) contributes \(O(H)\) to the normalized
bin energy. The report uses this factor consistently in both directions;
its final physical quantity is \(X\mathcal E_N\), up to logarithms.

Direct differentiation of (R1) gives precisely two terms: the coefficient
derivative \((2y)^{-1}h\partial_h C_{I,\mu}\), and the internal phase
multiplier \(-2\pi i(X\mu-j)C_{I,\mu}\). The outer center modulation
has modulus one when these terms are fed into (R4). Using \(\psi=\rho\)
and \(\psi(t)=t\rho(t)\) proves (19). No uncontrolled derivative of a
bin center or of the moving prefix is missing.

### Actual lattice coefficients on all real translates

Poisson summation of the first arm is exactly
\(4\sum_{d\le D}\chi_4(d)\sum_{d\mid n}F((n-z)/h)\).
For each second-arm label it is
\(4\sum_{\ell\mid n}\chi_4(n/\ell)F((n-z)/h)\), with that
label retained. This independently yields (20)--(21). Negative integers
retain their actual odd character, and at zero only the first arm remains:

\[
 a_r(0)=4\sum_{d\le D}\chi_4(d)=O(1),\qquad
 |a_r(n)|\le8\tau(|n|)\quad(n\ne0).                      \tag{R5}
\]

Here (R5) is for ordinary prefixes \(0\le r\le L\); the zero/padded
conventions in Section 1 extend its bounds to the endpoints used in
factorization. The zero coefficient is bounded before absolute values.
Its unsigned replacement could have order \(D\), so this step uses
an actual character property, not an arbitrary coefficient envelope.

Width differentiation keeps coefficients fixed and replaces \(F(v)\) by
\(-vF'(v)\), another uniformly Schwartz filter. Its Fourier support
remains in the same annuli. Splitting the integer line into intervals of
length comparable to \(H\), applying the elementary divisor bound, and
summing a sufficiently high Schwartz tail proves

\[
 |S_r(z;h)|+|h\partial_hS_r(z;h)|
       \ll_\eta H(2+|z|+H)^\eta                         \tag{R6}
\]

for every real \(z\), including zero and negative translates. This is
exactly the range needed by (R4), which does not stay in \(J\).

### Joint interval variance and the full energy

Reduction of a nonzero first-arm frequency gives an odd denominator and
coefficient (24). Reduction in the second arm gives \(4\mid q\), odd
numerator, and coefficient (25); its prefactor is correctly \(8ih/q\).
The classes are disjoint. At one dyadic level, the allowed \(j\)-sets in
(25) partition the actual quotient labels. Thus

\[
 \sum_{I\text{ at that level}}
   \left|\sum_{qj/4\in I}\chi_4(j)/j\right|^2
       \le\left(\sum_{j\le4L/q}1/j\right)^2.             \tag{R7}
\]

For active \(q\), one has \(q\gg H\), at most \(O(q/H)\) signed
numerators, and coefficient prefactor \(O(H/q)\). Summing (R7) over
numerators and denominators costs \(H\) times logarithms per level.
The first arm occurs once per level; its alternating harmonic sum is
bounded. Summing all levels proves (27), with no factor proportional to
the number of intervals. The width derivative has the same support and
the same \(O(H)\) multiplier bound, so its energy obeys the same estimate.

Reduced denominators at most \(Q\asymp T\) give spacing
\(Q^{-2}\gg X^{-1}\). There are \(O(X)\) active frequencies. Ordering
them and bounding each integral kernel by
\(\min(X,C/|\lambda-\lambda'|)\) yields the claimed Schur estimate
\(X\log(2X)\sum|b_\lambda|^2\), uniformly in every real translate.
Partitioning the \(u\)-line into unit intervals and using the \(1/X\)
in (R4) therefore gives (29), of size \(H\) times logarithms.

Finally factor \(P_I=W_I\sum_{r=0}^4S_b^{4-r}S_{a-1}^r\).
Every differentiated factor in this degree-four sum is controlled by
(R6). Since \(z=X(y-u)\) and \(H\le X\), its squared envelope is
\(O(H^8X^{8\eta}(1+|u|)^{8\eta})\). Choose the convolution weight
with exponent greater than \(8\eta+3\), apply (29), and integrate over
the fixed \(Y\). This proves

\[
 \mathcal E_N\ll H^9T^\varepsilon,\qquad
 \int_J|Q_N|^{10}\ll XH^9T^\varepsilon
               =T^{11+\varepsilon}N^{-9/2}.              \tag{R8}
\]

All sums, derivatives, and tail integrals have now been paid. The report's
required normalized energy is the physical gate divided by \(X\):
\(T^{343/65+\varepsilon}N^{-1/2}=HT^{278/65+\varepsilon}\).
Dividing (R8) by the target gives \(T^{242/65}N^{-4}\); for the open
band its exponent is strictly between \(242/325\) and \(546/325\).
These are costs of an upper certificate, not lower bounds for actual
energy or a signed moment.

The inherited exact contribution remains \(XHQ^4=T^7N^{-1/2}\),
below the target by \(T^{18/65}\). The floor-cutoff remainder costs
\(TH\) before physical conversion; conversion by \(T^{-6}\) gives
\(T^{-4}N^{-1/2}\). The separate radial error is
\(T^{-4+\varepsilon}N^{-10}\). Both inherited complete large-value
terms are retained. The supplied reproduction, equality endpoints,
complements, singleton, infinite tail and sharp error are unchanged.

## 4. First unproved step

The missing assertion remains the target-sized bound for the **full**
normalized energy (R1), including its dyadic interval sum and derivative.
The proved \(H^9\) estimate is insufficient everywhere in the required
open band. Its last envelope step spends eight factors absolutely; the
review provides no stronger signed correlation estimate for those factors.

The normalized energy target is sufficient, not necessary for the original
signed tenth moment. The independently reviewed exact diagonal permits
the stated equivalence between the original complete moment gate and the
total signed nonzero remainder, but does not make either one equivalent
to this stronger bin-energy certificate.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Smooth bins and internal phase | Verified partition, plateau, exact reconstruction and both generic failure controls. |
| Normalization | Verified the \(1/X\) in physical convolution and the external \(X\) in the moment transfer. |
| Derivative and prefix | Verified width and internal phase derivatives; discontinuous prefix handled only by maximum-label decomposition. |
| Static prefix, all real arguments | Verified negative integers, the ordinary zero atom, zero-prefix convention and all convolution tails. |
| Joint intervals and labels | Verified (R7), per-level energy, all levels, one outer prefix logarithm and all mixed fifth products. |
| Exact nonpairing relations | Retained by full polynomial powers and the inherited exact relation estimate; no pairing restriction used. |
| Complete powers and endpoints | Verified \(H^9\), integrated \(XH^9\), deficit endpoints, floor error, shell Jacobian and unchanged complete complements. |
| Scope | No new pointwise gain or quarter theorem. This is an independent nonblind review, not the isolated statement-only control. |

## 6. Source bindings and dependencies

Primary claimant at initial review:
`rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/signed_rational_bins.md`,
SHA-256 `3447f82540c357bfc384860fb4a84c8b8f5cf10cf016d533c063663c1a1ab780`.
The final reviewed hash is recorded below and includes the checked explicit
boundary clarification.

Exact dependency bindings used in this review:

- `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/signed_fifth_convolution.md`:
  `3ad10212450a105eced8477cf5a162b1a9ac3613bf58bfcb0308a393e9e9bdda`.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/reviews/independent_rational_tenth_review.md`:
  `85c6bf8a20a929118f043124deb3c1decb0ece59ef96c327cf2beafff4d5745d`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md`:
  `be115ee27206a429c9480594969aa9e9fddd7963569e3f635e8c3ce9085029d4`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`:
  `6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552`.

The protocol, Round210 manifest, graph scope and Round208/209 strategy
context were read during the completed preceding discovery assignment.
This review does not use that assignment's candidate results. All new
transfer, coefficient, normalization and power claims were rederived here.
No external theorem or numerical experiment was imported. Only this
assigned review file is written.

## 7. Recommended state effect and final binding

**GREEN after the explicit zero/padded-prefix clarification.** Final reviewed
claimant:
`rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/signed_rational_bins.md`.
Final SHA-256:
`72437c1f52135b6cff5854a2d1d4d76c1a69e4be0af76be54a168d2edbc77853`.

Retain the report as scoped successful method accounting with an unsuccessful
quantitative bound. The coarse \(H^9\) estimate is reviewed evidence, not a
new best bound. Keep the full signed target, M1/M2 obligations and quarter
theorem open; no mathematical graph promotion follows from this review.
Only this review was edited by the reviewer. No claimant, shared-state,
synthesis or successor file was edited, and the review assignment stops here.

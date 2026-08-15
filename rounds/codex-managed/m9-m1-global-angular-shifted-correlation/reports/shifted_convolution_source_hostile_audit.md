# Hostile and primary-source audit of the shifted angular correlation

- Campaign: m9-m1-global-angular-shifted-correlation
- Research round: 54 (global_angular_shifted_correlation)
- Task: shifted_convolution_source_hostile_audit
- Role: source_auditor
- Graph SHA-256 supplied in the brief: ee2e84080cef5a9a49fd9a573f3ee0f1e14c3ec5032db3cca8fb5a50bc97ef22
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**Exact one-step reduction, sharp absolute-capacity no-go, and source
non-importability.** Put \(N=16\sqrt X\), \(M=\lfloor N\rfloor\), and encode
the radial endpoint star by

\[
 \epsilon_N(n)=
 \begin{cases}
  1,&1\le n<N,\\
  1/2,&n=N\in\mathbb Z,\\
  0,&\text{otherwise}.
 \end{cases}
\]

With

\[
 z_n=\epsilon_N(n)A_X(n)n^{-3/4}e(\sqrt{Xn})
\]

extended by zero, define

\[
 C_r=\sum_{n\in\mathbb Z}z_{n+r}\overline{z_n}.
\]

For every integer \(1\le R\le M\), the exact Fejer differencing statement is

\[
 \boxed{\;
 |S_X|^2\le\frac{M+R-1}{R}\,\mathfrak F_R,\qquad
 \mathfrak F_R=C_0+
 2\operatorname {Re}\sum_{r=1}^{R-1}
 \left(1-\frac rR\right)C_r ,
 \;}                                                       \tag{54.1}
\]

where

\[
 \mathfrak F_R=
 \frac1R\sum_{t=1}^{M+R-1}
 \left|\sum_{a=0}^{R-1}z_{t-a}\right|^2\ge0.                \tag{54.2}
\]

Thus a coefficient-preserving step is lawful, and it keeps the complete
shift average signed. It does not by itself save a power. The exact
coefficient correlation is the packet's \(\mathcal C_r(X)\), with two
endpoint factors:

\[
\begin{aligned}
 C_r={}&\sum_{1\le n\le M-r}
 \epsilon_N(n+r)\epsilon_N(n)
 A_X(n+r)\overline{A_X(n)}
 ((n+r)n)^{-3/4}\\
 &\hspace{18mm}\times
 e\!\left(\sqrt X(\sqrt{n+r}-\sqrt n)\right).
                                                               \tag{54.3}
\end{aligned}
\]

The unweighted incidence expansion is not an ordinary divisor correlation.
It has the exact constraint

\[
 h_1q_1-h_2q_2=r
\]

and retains two distinct angular symbols, their scale sums, floors, profile
stars, and the two product endpoint factors. Formula (54.8) below records it
without abbreviation.

The smallest exact Fejer-energy theorem sufficient for the complex target is

\[
 \boxed{\quad
 \mathfrak F_R\ll_\varepsilon \frac{R}{N}X^\varepsilon
 \quad}                                                     \tag{54.4}
\]

for one admissible \(R\). Operationally, on a dyadic radial block
\(n\asymp Y\), \(Y^{1/2}\le R\le Y\), it is enough to prove

\[
 \boxed{\quad
 \left|\sum_{r=1}^{R-1}\left(1-\frac rR\right)C_{r,Y}\right|
 \ll_\varepsilon RY^{-1+\varepsilon}.
 \quad}                                                     \tag{54.5}
\]

After removing the radial factor \(((n+r)n)^{-3/4}\asymp Y^{-3/2}\),
(54.5) is a signed double-sum bound of exact size

\[
 RY^{1/2+\varepsilon},                                     \tag{54.6}
\]

against the all-absolute size \(RY^{1+\varepsilon}\). Hence every admissible
\(R\) requires a square-root saving in the radial length.

Absolute shifted-incidence accounting cannot provide it. The accepted
nonnegative angular partition gives
\[
 0\le\Omega_X^*(n,h)\le1,\qquad |A_X(n)|\le\tau(n),
\]
and consequently

\[
 C_0\ll_\varepsilon1,\qquad
 |C_r|\ll_\varepsilon r^{-1/2+\varepsilon}.                 \tag{54.7}
\]

Putting absolute values into (54.1) yields at best
\[
 |S_X|\ll_\varepsilon N^{1/4+\varepsilon}
 =X^{1/8+\varepsilon},
\]
after optimizing at \(R\asymp N\): exactly the pre-existing normalized
capacity and no improvement.

This loss is realized by actual, star-free incidences. The Round-53
penultimate-scale shell contains a fixed-length interval of odd
\(q\asymp\sqrt X\) on which the \(h=1\) angular weight is bounded below and
owned by exactly one scale. Restricting to even \(r\ll\sqrt X\) with
\(q,q+r\) in a smaller interior interval contributes
\[
 \gg R N^{-1/2}
\]
to the termwise-absolute expansion of the Fejer off-diagonal, matching the
upper capacity. Neither the radial endpoint star, either angular star, nor a
height equality occurs. This is not a lower bound for the signed
\(\mathfrak F_R\).

The primary-source search found no theorem whose stated hypotheses match
(54.3). The closest spectral and shifted-divisor theorems require fixed
cuspidal Hecke coefficients or fixed untruncated Eisenstein divisor
coefficients, fixed smooth symbols with controlled Sobolev norms, and
different character/level/shift hypotheses. None accepts the moving
\(X\)-dependent angular coefficient, floors and stars, the range
\(r\le R\), and the nonlinear radial difference phase with target-uniform
constants.

## 2. Exact statement and hypotheses

The exact arithmetic coefficient is

\[
 A_X(m)=
 \sum_{\substack{h\mid m\\q=m/h\ {\rm odd}}}
 \chi_4(q)\Omega_X^*(m,h),
\]

\[
 \Omega_X^*(m,h)=
 \sum_j{\bf1}_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{\frac Xm}\right)\right]^*.
\]

The star on \(\epsilon_N(m)\) is the radial product endpoint. Each star
inside \(\Omega_X^*(m,h)\) belongs to the corresponding dyadic angular
profile. The condition \(h\le H_j\) has full equality weight; it is not a
half-star. These owners must not be merged.

Substitution into (54.3) gives

\[
\begin{aligned}
 C_r={}&
 \sum_{\substack{h_1,q_1,h_2,q_2\ge1\\
                  0\le j_1,j_2\le J\\
                  q_1,q_2\ {\rm odd}\\
                  h_1q_1-h_2q_2=r\\
                  h_1q_1,h_2q_2\le M}}
 \epsilon_N(h_1q_1)\epsilon_N(h_2q_2)
 \chi_4(q_1)\chi_4(q_2)\\
 &\quad\times
 \prod_{i=1}^{2}
 \left\{
 {\bf1}_{h_i\le H_{j_i}}
 \Phi\!\left(\frac{h_i}{H_{j_i}+1}\right)
 \left[
 w_{j_i}\!\left(2h_i\sqrt{\frac{X}{h_iq_i}}\right)
 \right]^*
 \right\}
 (h_1q_1h_2q_2)^{-3/4}\\
 &\quad\times
 e\!\left(\sqrt X
  \{\sqrt{h_1q_1}-\sqrt{h_2q_2}\}\right).
                                                               \tag{54.8}
\end{aligned}
\]

All angular weights in (54.8) are real. The conjugation in \(C_r\) therefore
conjugates the radial phase and nothing else. For \(r>0\), the shifted upper
point \(h_1q_1=N\in\mathbb Z\) carries the radial factor \(1/2\); the lower
product cannot equal \(N\). In \(C_0\), a radial endpoint term carries
\((1/2)^2=1/4\). Angular half-stars remain independently multiplicative.

For a dyadic block, let \(z_{n,Y}=z_n\,V(n/Y)\), where \(V\) is one member
of a fixed one-count smooth partition (with the final hard endpoint retained
separately), and let \(C_{r,Y}=\sum_nz_{n+r,Y}\overline{z_{n,Y}}\).
The divisor envelope gives

\[
 C_{0,Y}\ll_\varepsilon Y^{-1/2+\varepsilon}.               \tag{54.9}
\]

Thus (54.5), for any single \(R\) satisfying
\(Y^{1/2}\le R\le Y\), implies via (54.1)

\[
 \left|\sum_nz_{n,Y}\right|\ll_\varepsilon Y^\varepsilon.
\]

Summing \(O(\log N)\) blocks proves the stronger complex estimate
\(S_X\ll_\varepsilon X^\varepsilon\), hence the required real-part estimate.
No assertion is made that (54.5) is known.

The project needs only
\(\operatorname {Re}\{e(1/8)S_X\}\). If one applies (54.1) instead to the
real sequence
\[
 y_n=\operatorname {Re}\{e(1/8)z_n\},
\]
then
\[
 y_{n+r}y_n=\frac12\operatorname {Re}
 \left\{z_{n+r}\overline{z_n}
       +e(1/4)z_{n+r}z_n\right\}.                           \tag{54.10}
\]

Therefore a phase-aware real differencing introduces an additional
nonconjugated, sum-phase correlation. The packet's difference-phase
\(C_r\) alone controls the stronger complex sum; it cannot be advertised as
a lossless real-part polarization.

## 3. Proof or derivation

Extend \(z_n\) by zero outside \(1\le n\le M\), and put
\[
 Y_t=\sum_{a=0}^{R-1}z_{t-a}\qquad(1\le t\le M+R-1).
\]
Every \(z_n\) occurs in exactly \(R\) of the \(Y_t\), so
\[
 RS_X=\sum_{t=1}^{M+R-1}Y_t.
\]
Cauchy--Schwarz gives
\[
 R^2|S_X|^2\le(M+R-1)\sum_t|Y_t|^2.
\]
Expanding the last square and collecting the difference \(r=a-b\) gives
\[
 \sum_t|Y_t|^2
 =RC_0+2\operatorname {Re}\sum_{r=1}^{R-1}(R-r)C_r,
\]
which proves (54.1)--(54.2), including every boundary term. Direct
substitution proves (54.3) and (54.8).

For the absolute estimate, split the \(n\)-sum in (54.3) at \(n=r\). The
divisor bound \(\tau(n)\ll_\varepsilon n^\varepsilon\) gives
\[
\begin{aligned}
 |C_r|
 &\ll_\varepsilon
 \sum_{n\le r}n^{-3/4+\varepsilon}r^{-3/4+\varepsilon}
 +\sum_{n>r}n^{-3/2+2\varepsilon}\\
 &\ll_\varepsilon r^{-1/2+2\varepsilon}.
\end{aligned}
\]
The same envelope gives \(C_0\ll_\varepsilon1\). Therefore
\[
 \mathfrak F_R\ll_\varepsilon1+R^{1/2+\varepsilon}
\]
after taking absolute values, and (54.1) yields
\[
 |S_X|\ll_\varepsilon
 N^\varepsilon\left\{
 \left(\frac NR\right)^{1/2}
 +N^{1/2}R^{-1/4}\right\}.
\]
The optimum \(R\asymp N\) is \(N^{1/4+\varepsilon}\), proving the no-go.
On a block \(n\asymp Y\), the diagonal is (54.9), while the factor in
(54.1) is \(O(Y/R)\). This proves the exact target ledger
(54.5)--(54.6).

For the actual absolute-capacity witness, rename the Round-53 shell
parameter \(Q_0=X/D_j^2\) so it is not confused with the Fejer length \(R\).
For arbitrarily large square \(X\), the permitted Round-53 synthesis gives
an interior interval
\[
 I\subset[25Q_0/4,64Q_0/9],\qquad |I|\asymp Q_0\asymp\sqrt X,
\]
on which, for odd \(q\),
\[
 \Omega_X^*(q,1)\ge\Phi(1/3)>0.
\]
Exactly one interior scale owns each row; the profile argument stays inside
the plateau, and
\[
 q<\frac{16}{9}\sqrt X<N.
\]
Choose a smaller interval \(I'\Subset I\) and
\(1\le R\le cQ_0\). For every even \(1\le r\le R/2\), there are
\(\gg Q_0\) odd \(q\in I'\) with \(q+r\in I\). The incidence
\[
 h_1=h_2=1,\qquad q_1=q+r,\qquad q_2=q
\]
then occurs in (54.8), has Fejer weight at least \(1/2\), and contributes
\(\gg Q_0^{-3/2}\) after termwise absolute values. Summing these
\(\gg RQ_0\) pairs gives
\[
 \gg RQ_0^{-1/2}\asymp RN^{-1/2}.                           \tag{54.11}
\]
This matches the bulk absolute upper order. Both products are strictly below
\(N\), both angular arguments are strictly inside the plateau, and \(h=1\)
is strictly inside the surviving height. Thus (54.11) is free of every
radial, profile, and height boundary convention.

There is genuine arithmetic sign structure that (54.11) intentionally
discards. On the \(h_1=h_2=1\) rows, \(r=q_1-q_2\) is even and
\[
 \chi_4(q+r)\chi_4(q)=(-1)^{r/2},
\]
independent of \(q\). Thus the character supplies no cancellation inside
one fixed shift, although it alternates between the two even-shift classes.
The radial difference phase may still cancel in \(q\) and jointly in \(r\).
That signed interaction is precisely the unproved theorem (54.5).

Finally, on \(n\asymp Y\), \(r\le cY\), the phase
\[
 \psi_r(n)=\sqrt X(\sqrt{n+r}-\sqrt n)
\]
satisfies
\[
 Y^k|\psi_r^{(k)}(n)|
 \ll_k T_r,\qquad
 T_r=\frac{\sqrt X\,r}{\sqrt Y}\quad(k\ge1).                \tag{54.12}
\]
At the main scale \(Y\asymp N\asymp\sqrt X\),
\(T_r\asymp r\sqrt N\). Consequently a generic smooth-weight theorem whose
constant uses fixed high Sobolev norms incurs a positive power of
\(r\sqrt N\), unless it treats this oscillation structurally.

## 4. First doubtful or unproved step

The first missing step is exactly the signed averaged theorem (54.5) for the
coefficient in (54.8), uniformly on a nonempty range
\(Y^{1/2}\le R\le Y\). It must save \(Y^{1/2}\) over the expanded absolute
incidence count while retaining:

- the two \(\chi_4\) factors and the constraint
  \(h_1q_1-h_2q_2=r\);
- both moving angular symbols, all \(H_j\) floors, and every profile star;
- the difference phase and the Fejer weight before absolute values;
- the hard radial endpoint and its shifted half-weight;
- uniformity in \(X,Y,r,R\).

No permitted identity makes \(A_X(n)\) a fixed Hecke or Eisenstein
coefficient. Removing \(\Omega_X^*\) would replace the actual coefficient by
\(\sum_{q\mid n}\chi_4(q)\), but the moving divisor-angle weight is the
substance of the problem, not a harmless one-variable cutoff. Mellin
separation creates a superposition of twisted-divisor modes plus hard top
Perron pieces; it does not provide the uniform mode-integrable shifted
estimate required to reassemble them.

Even a physical proof of the global radial estimate would not by itself
prove the connector-completed alpha branch. A separate accepted transfer
must identify the complete finite projected alpha antecedent with the
physical radial aggregate while preserving finite faces, the signed
Plemelj order, Abel regularization, and the joint outside-height limit.

## 5. Control tests, applicability table, and outcomes

| Control or primary theorem | Exact hypotheses checked | Outcome for (54.8) |
|---|---|---|
| exact_differencing | Zero extension, \(1\le R\le M\), \(M+R-1\) Cauchy terms, diagonal \(C_0\), weights \(1-r/R\) | Pass: (54.1)--(54.2) are exact and the shift sum remains inside one real part. |
| shifted_incidence and coefficient_ownership | Expand both actual \(A_X\)'s before any modulus | Pass: (54.8) retains \(h_1q_1-h_2q_2=r\), two characters, two angular symbols, floors, scales, and phases. |
| endpoint_stars | Radial endpoint, shifted endpoint, angular profile stars, height equality | Pass: two \(\epsilon_N\)'s and both angular stars are separate. The witness (54.11) meets none of them. |
| R_N_exponents | Fejer factor \(Y/R\), diagonal \(Y^{-1/2}\), radial product weight \(Y^{-3/2}\) | Pass: \(R\ge Y^{1/2}\) and (54.5), equivalently raw size (54.6), suffice. |
| absolute_capacity | Divisor envelope and an actual \(h_1=h_2=1\) shell | Fail for closure: absolute values give \(N^{1/4}=X^{1/8}\), and (54.11) realizes the expanded-incidence capacity. |
| [Blomer--Harcos, Theorem 1](https://arxiv.org/html/math/0703246v2) | Two fixed cuspidal \({\rm PGL}_2\) representations; Hecke eigenvalues; separable smooth \(W_1,W_2\); norms \(A^d\) through at least \(d=18\); fixed-shift spectral decomposition | Not importable. \(A_X\) is neither cuspidal Hecke data nor fixed in \(X\), and its divisor-angle symbol is not a one-variable smooth cutoff. If the phase is put into a weight, (54.12) makes the required high Sobolev norm grow as a large power of \(r\sqrt N\). Their displayed pointwise bound also carries \(r^{7/64}\) unconditionally. |
| [Cowan, Theorem 1.1](https://arxiv.org/abs/2304.12572) | Fixed positive shift; prime modulus; even nontrivial characters \(\chi,\psi\) with \(\chi\psi\) nontrivial; nonzero fixed \(u,v\); all parameters except summation length fixed | Not importable even after deleting \(\Omega\): \(\chi_4\) is odd of modulus \(4\), the self-correlation has principal product character, the physical mode is \(u=v=0\), shifts grow to \(R\), and the phase/symbol vary with \(X\). The source explicitly does not state uniform dependence in these other variables. |
| [Petrow, Main Theorem](https://arxiv.org/abs/1111.7010) | Fixed level-one holomorphic Hecke cusp form; products \(\lambda_f(n)\lambda_f(n+h)\); a smooth bounded incomplete-Poincare cutoff; a specific shift average | Not importable. The coefficient, level/Eisenstein nature, Fejer weight, moving radial phase, and angular hard stars all differ. |
| [Banerjee--Khurana, Theorems 4.3--4.4](https://arxiv.org/abs/2306.12399) | One twisted-divisor coefficient for an odd primitive character; analytic finite-interval test; nonintegral endpoints; \(0<\Re\nu<1/2\) | Exact support for a single Voronoi mode only. It states no product shifted-correlation estimate, no \(r,R\) average, and no uniform large-imaginary-order or hard-top Perron bound needed to reconstruct \(A_X\). |
| [Kiral--Zhou, Theorem 1.3 and Remark 3.2](https://arxiv.org/abs/1508.01985) | Voronoi from Hecke relations and primitive-twist functional equations; main argument degree at least three, separate degree-two modification | Structural analogy only. The project is degree two, ramified at \(4\), noncuspidal, and has a zeta pole; polar/local terms must first be derived. The source supplies no shifted-correlation or averaged Fejer estimate. |
| generic spectral/large-sieve import | A derived automorphic spectral family, controlled transform norms, explicit main/polar terms, uniform \(r,R\) range | Fail at the interface: no such spectral expansion of (54.8) has been derived. A large sieve may bound a resulting spectral sum, but it cannot be applied before the delta/Voronoi transform and does not erase (54.12) or the angular modes. |
| alpha_transfer_scope and downstream_scope | Physical radial bound versus finite connector/Plemelj theorem | Pass as a scope warning: no alpha, M9-M1, M9, or Gauss-circle promotion follows from (54.1). |

The source search was restricted to primary papers and exact source cards. No
numerical or symbolic experiment was used.

## 6. Dependencies, artifacts, and primary sources used

Only the task brief and its named context were used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-global-angular-shifted-correlation/derivation_packet.md;
- rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/synthesis.md;
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md;
- rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_literature_hostile_audit.md;
- rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/reports/resonance_cell_literature_hostile_audit.md;
- sources/banerjee_khurana_2023.md;
- sources/kiral_zhou_2016.md;
- the Round-54 task brief.

Primary literature inspected on the web:

- Valentin Blomer and Gergely Harcos, “The spectral decomposition of shifted
  convolution sums,” Duke Math. J. 144 (2008), Theorem 1,
  [arXiv:math/0703246v2](https://arxiv.org/html/math/0703246v2).
- Alex Cowan, “A twisted additive divisor problem,” J. Number Theory 266
  (2025), Theorem 1.1,
  [arXiv:2304.12572](https://arxiv.org/abs/2304.12572).
- Ian Petrow, “Transition Mean Values of Shifted Convolution Sums,”
  [arXiv:1111.7010](https://arxiv.org/abs/1111.7010), Main Theorem.
- Debika Banerjee and Khyati Khurana, “Character analogues of Cohen type
  identities and related Voronoi summation formulas,” Theorems 4.3--4.4,
  [arXiv:2306.12399](https://arxiv.org/abs/2306.12399).
- Eren Mehmet Kiral and Fan Zhou, “The Voronoi formula and double Dirichlet
  series,” Algebra & Number Theory 10 (2016), Theorem 1.3 and Remark 3.2,
  [arXiv:1508.01985](https://arxiv.org/abs/1508.01985).

The exact Fejer identity, exponent ledger, incidence expansion, actual
capacity witness, and phase-derivative audit were derived directly. No other
Round-54 report or unlisted project artifact was read.

## 7. Recommended state effect

**Promote only a coefficient-preserving Fejer reduction and a scoped
absolute-capacity/source no-go.** The graph may record:

1. the exact positive Fejer energy (54.1)--(54.3), including all endpoint
   factors;
2. the exact six-index shifted incidence (54.8);
3. the sufficient dyadic theorem (54.5), or raw equivalent (54.6), which
   requires a square-root saving in the radial length;
4. the absolute bound (54.7) and actual star-free incidence witness
   (54.11), showing that termwise absolute shifted convolution retains the
   full normalized \(X^{1/8}\) capacity;
5. the real-part warning (54.10): a lossless polarization introduces an
   additional sum-phase correlation;
6. the present source decision: none of the audited spectral,
   shifted-divisor, averaged-shift, or Voronoi theorems is a black-box input
   for the actual moving angular kernel.

Do not promote M9-M1-global-angular-radial-estimate or
M9-M1-alpha-bounded-zeta-high-transition-bound. The next candidate must
derive, rather than assume, an automorphic/delta/Voronoi representation of
the complete angular coefficient and prove (54.5) with uniform control of
all Mellin modes, polar terms, radial oscillation, floors, and stars.
Separately, a finite-to-physical alpha transfer and outside-height Cauchy
theorem remain necessary. M9-M1, M9, and the Gauss-circle target stay open.

# Blind rederivation: one-step Fejer/vdC shifted correlation

## 1. Result

**Lemma with a sharp absolute-capacity no-go.** Put \(N=16\sqrt X\) and
\(M=\lfloor N\rfloor\). With the radial endpoint convention made explicit
below, one finite Fejer/van-der-Corput step gives, for every integer
\(1\le R\le M\),

\[
 \left|\operatorname {Re}\{e(1/8)S_X\}\right|^2
 \le |S_X|^2
 \le {M+R-1\over R}\left(E_X+2T_R(X)\right),                 \tag{1}
\]

where

\[
 E_X=\sum_{n=1}^{M}\rho_N(n)^2|A_X(n)|^2n^{-3/2},
 \qquad
 T_R(X)=\operatorname {Re}\sum_{r=1}^{R-1}
       \left(1-{r\over R}\right)\mathcal C_r(X),             \tag{2}
\]

and \(E_X+2T_R(X)\ge0\). Thus the shift average remains signed and outside
absolute values. The coefficient product in every \(\mathcal C_r\) has the
exact incidence \(h_1q_1-h_2q_2=r\), with the two angular symbols owned by
their respective factors.

Within (1), the weakest one-sided correlation condition that certifies the
target through this inequality is

\[
 T_R(X)\le -{1\over2}E_X
  +O_\varepsilon\!\left(X^\varepsilon{R\over M+R-1}\right).   \tag{3}
\]

Equivalently, the nonnegative Fejer quantity must satisfy

\[
 E_X+2T_R(X)\ll_\varepsilon
 X^\varepsilon {R\over M+R-1}.                               \tag{4}
\]

The harmless renaming of \(\varepsilon\) after taking a square root is
understood. If \(E_X\ll_\varepsilon X^\varepsilon\), then there is a
nonempty target-capable range \(R\asymp N\): in that range the simpler
one-sided theorem \(T_R(X)\ll_\varepsilon X^\varepsilon\) suffices.

The differencing operation itself does **not** save \(X^{1/8}\). If one
takes \(|\mathcal C_r|\) term by term and uses only
\(B_X=\max_{n\le M}|A_X(n)|\), then optimizing over every allowed \(R\)
returns

\[
 |S_X|\ll B_XN^{1/4}=2B_XX^{1/8}.                             \tag{5}
\]

This is the original absolute-size exponent. Thus one step has formal
target capacity only through a genuinely signed, essentially full-range
shifted-correlation theorem. Absolute values or ordinary divisor envelopes
cannot realize the saving.

## 2. Exact statement and hypotheses

Define the radial endpoint weight by

\[
 \rho_N(n)=
 \begin{cases}
 1,&1\le n<N,\\
 \tfrac12,&n=N\in\mathbb Z,\\
 0,&\text{otherwise}.
 \end{cases}                                                   \tag{6}
\]

Thus
\(\sum_{n\le N}^{*}u_n=\sum_{n=1}^{M}\rho_N(n)u_n\).
This is the standard half-weight interpretation of the radial star. The
packet did not separately define that symbol, so (6) is an explicit
hypothesis rather than an imported convention. Set

\[
 b_n=\rho_N(n)A_X(n)n^{-3/4}e(\sqrt{Xn})
 \quad(1\le n\le M),
\]

and extend \(b_n\) by zero outside \([1,M]\cap\mathbb Z\). Then
\(S_X=\sum_nb_n\). For \(1\le r\le R-1\),

\[
 \sum_n b_{n+r}\overline{b_n}
 =\sum_{n\le N-r}^{*} A_X(n+r)\overline{A_X(n)}
 ((n+r)n)^{-3/4}
 e\!\left(\sqrt X(\sqrt{n+r}-\sqrt n)\right)
 =\mathcal C_r(X).                                             \tag{7}
\]

For \(r>0\), \(\rho_N(n)=1\) throughout the correlation range, whereas
\(\rho_N(n+r)=1/2\) exactly when \(N\in\mathbb Z\) and \(n=N-r\).
Hence the star in (7) belongs to the shifted upper endpoint. The diagonal
is different: its top weight is \(\rho_N(N)^2=1/4\), not the \(1/2\)
produced by writing a new starred energy sum.

For the exact incidence expansion, abbreviate only

\[
 W_{j,X}(m,h)=\mathbf 1_{h\le H_j}
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/m}\right)\right]^*.               \tag{8}
\]

No meaning is removed from the angular star in this abbreviation. Then

\[
\begin{aligned}
 \mathcal C_r(X)
 ={}&\sum_{\substack{h_1,h_2,q_1,q_2\ge1\\
                      q_1,q_2\ {\rm odd}\\
                      h_1q_1-h_2q_2=r\\
                      h_1q_1\le N}}
 \rho_N(h_1q_1)\,
 \chi_4(q_1)\overline{\chi_4(q_2)}                            \\
 &\quad\times ((h_1q_1)(h_2q_2))^{-3/4}
 e\!\left(\sqrt X
   (\sqrt{h_1q_1}-\sqrt{h_2q_2})\right)                       \\
 &\quad\times
 \sum_{j_1,j_2}
 W_{j_1,X}(h_1q_1,h_1)
 \overline{W_{j_2,X}(h_2q_2,h_2)} .                           \tag{9}
\end{aligned}
\]

The displayed incidence and \(r\ge1\) imply
\(h_2q_2=h_1q_1-r\le N-r\), so no second upper condition is missing.
Conversely, every term of (7) gives exactly one quadruple in (9) after the
two divisor expansions. Formula (9) retains conjugation even though the
primitive character is real.

The endpoint and ownership rules are:

| Object | Owner and exact rule |
|---|---|
| Global radial star | \(\rho_N(n)\) multiplies the original summand only. |
| Shifted radial star | For \(r>0\), it is \(\rho_N(h_1q_1)\); it is \(1/2\) only at \(h_1q_1=N\in\mathbb Z\). |
| Diagonal endpoint | It is \(\rho_N(N)^2=1/4\) when \(N\in\mathbb Z\). |
| First divisor/angle factor | \(h_1q_1=n+r\), with \(\chi_4(q_1)\), \(j_1\), \(H_{j_1}\), and the first starred \(w_{j_1}\). |
| Second divisor/angle factor | \(h_2q_2=n\), with \(\overline{\chi_4(q_2)}\), \(j_2\), \(H_{j_2}\), and the conjugated second starred \(w_{j_2}\). |
| Angular stars | Each stays inside its own \(W_{j_i,X}\). It is independent of the radial half-weight; simultaneous endpoint factors multiply. |
| Shift endpoint | \(r=R\) is absent (equivalently has Fejer weight zero); there is no half-weight in \(r\). |

The packet does not state the trigger rule for an angular profile star.
Accordingly, (8)--(9) preserve those tagged endpoint values exactly but do
not invent a half-weight rule for them.

## 3. Proof and exponent derivation

For \(\ell=1-R,\ldots,M-1\), put

\[
 B_\ell=\sum_{k=1}^{R}b_{\ell+k}.
\]

Every \(b_n\) occurs in exactly \(R\) of these sums, while there are exactly
\(M+R-1\) values of \(\ell\). Hence Cauchy--Schwarz gives

\[
 R^2|S_X|^2
 =\left|\sum_{\ell=1-R}^{M-1}B_\ell\right|^2
 \le (M+R-1)\sum_{\ell=1-R}^{M-1}|B_\ell|^2.                 \tag{10}
\]

Expansion of the last sum, with no absolute values on the off-diagonal,
gives the exact Fejer identity

\[
 \sum_{\ell=1-R}^{M-1}|B_\ell|^2
 =R E_X+2\operatorname {Re}\sum_{r=1}^{R-1}
       (R-r)\mathcal C_r(X).                                  \tag{11}
\]

Dividing (10)--(11) by \(R^2\) proves (1). Identity (11) also proves
\(E_X+2T_R(X)\ge0\). Multiplication of every \(b_n\) by \(e(1/8)\)
cancels from all correlations. The only real-part loss is the explicitly
recorded
\(|\operatorname {Re}(e(1/8)S_X)|\le|S_X|\); it strengthens the desired
claim to a complex-modulus bound but costs no power of \(X\). A direct real
polarization would additionally create \(b_{n+r}b_n\) sum-phase
correlations, so it does not yield (9) alone.

For the target ledger, write \(F_R=E_X+2T_R(X)\). Inequality (1) certifies
\(\operatorname {Re}(e(1/8)S_X)\ll_\varepsilon X^\varepsilon\) as soon as

\[
 F_R\ll_\varepsilon X^\varepsilon{R\over M+R-1},              \tag{12}
\]

after renaming \(\varepsilon\). This is (3)--(4). If
\(R=N^\rho\) at the level of powers, then the required Fejer size is

\[
 F_R\ll X^\varepsilon N^{\rho-1}.                             \tag{13}
\]

Thus for \(\rho<1\) the signed off-diagonal must cancel the global diagonal
to accuracy \(N^{\rho-1}\):

\[
 T_R=-\tfrac12E_X+O_\varepsilon(X^\varepsilon N^{\rho-1}).    \tag{14}
\]

Without such diagonal cancellation, the global one-step route requires
\(\rho=1\), namely \(R\asymp N\). In this full-range regime, the sufficient
input is simply

\[
 E_X\ll_\varepsilon X^\varepsilon,
 \qquad T_R(X)\ll_\varepsilon X^\varepsilon,                  \tag{15}
\]

where the second inequality is one-sided. This is the nonempty formal
target-capable range.

The absolute-capacity computation is independent of unrecorded divisor
structure. Let \(B_X=\max_{n\le M}|A_X(n)|\). Then

\[
 E_X\le B_X^2\sum_{n\ge1}n^{-3/2}\ll B_X^2,                  \tag{16}
\]

and, on splitting at \(n=r\),

\[
\begin{aligned}
 |\mathcal C_r(X)|
 &\le B_X^2\sum_{n\ge1}n^{-3/4}(n+r)^{-3/4}                 \\
 &\ll B_X^2\left(
 r^{-3/4}\sum_{n\le r}n^{-3/4}+
 \sum_{n>r}n^{-3/2}\right)
 \ll B_X^2r^{-1/2}.                                          \tag{17}
\end{aligned}
\]

Consequently

\[
 \sum_{r<R}\left(1-{r\over R}\right)|\mathcal C_r(X)|
 \ll B_X^2R^{1/2},                                           \tag{18}
\]

and (1), closed by termwise absolute values, yields

\[
 |S_X|^2\ll B_X^2\left({N\over R}+{N\over R^{1/2}}\right).
                                                                    \tag{19}
\]

For \(R=N^\rho\), this gives

\[
 |S_X|\ll B_XN^{1/2-\rho/4}.                                 \tag{20}
\]

The best allowed choice is \(\rho=1\), which gives
\(B_XN^{1/4}=2B_XX^{1/8}\). The kernel exponent in (17) is sharp for an
envelope-only argument: when \(M\ge2r\), the terms \(r\le n\le2r\) alone
have total \(\gg r^{-1/2}\). Summing \(r\le M/2\) makes the
\(R^{1/2}\) exponent in (18) sharp as well. Ordinary divisor bounds merely
put \(B_X\ll_\varepsilon X^\varepsilon\) into this ledger and do not change
any power. Therefore the missing \(N^{1/4}=X^{1/8}\) saving must come from
the signs jointly across the additive incidences, not from the differencing
inequality or its absolute closure.

## 4. First doubtful or unproved step

All algebra through (11) and the incidence expansion (9) is exact under the
explicit radial convention (6). The first target-relevant estimate not
provable from the statement-only packet is the diagonal bound
\(E_X\ll_\varepsilon X^\varepsilon\): the packet gives no quantitative
bounds for \(\Phi\), the \(w_j\), the number of \(j\)'s, or their overlap.
Using \(B_X\ll X^\varepsilon\) would therefore be an additional hypothesis,
not a consequence established here.

Even granting that routine coefficient bound, the decisive unproved step is
the genuinely signed theorem (15), uniformly for an integer \(R\asymp N\),
with the moving symbols in (8), both character placements, all floors, and
the radial/angular endpoints intact. No shifted-convolution, spectral,
large-sieve, or exponent-pair theorem was supplied, and no such theorem can
be declared applicable merely from the additive equation in (9). Formula
(18) shows exactly why replacing that theorem by absolute values fails.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| exact_differencing | **Pass.** Equations (10)--(11) give the exact constant \(M+R-1\), weights \(R-r\), and shift range \(1\le r<R\). |
| real_part_scope | **Pass.** The use of the stronger \(|S_X|\) is explicit; it costs no exponent. Direct real polarization would introduce an additional sum-phase family. |
| shifted_incidence | **Pass.** Equation (9) has exactly \(h_1q_1-h_2q_2=r\), \(q_1,q_2\) odd, and the shifted phase with the correct sign. |
| coefficient_ownership | **Pass.** The two characters, scales, angular profiles, and conjugation remain attached to their own divisor factors. |
| endpoint_stars | **Pass with stated limitation.** Radial top weights, including the diagonal square, are explicit. Angular stars are preserved exactly as tagged inputs; their trigger convention is absent from the packet and was not invented. |
| R_N_exponents | **Pass.** The exact target is \(F_R\ll X^\varepsilon R/(M+R-1)\); for \(R=N^\rho\) it is \(N^{\rho-1}\), and absolute closure gives (19)--(20). |
| absolute_capacity | **No-go passed.** The sharp envelope-only size \(R^{1/2}\) leaves the optimized bound \(N^{1/4}=X^{1/8}\), so it saves nothing. |
| alpha_transfer_scope | **Pass.** No alpha-operator conclusion is inferred from (1). An exact connector from the projected alpha expression to \(\operatorname {Re}(e(1/8)S_X)\), with its normalization and uniform errors, is still required. |
| downstream_scope | **Pass.** The result concerns only the frozen radial sum. It does not absorb the external \(X^{1/4}\), hard-top boundary, inactive bottom, transform errors, or any outside-height estimate. |

No external literature theorem was invoked, so there is no unaudited
hypothesis match hidden in the conclusion.

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The exact definitions of \(S_X\), \(A_X\), \(\Omega_X^*\), and the frozen
   shifted coefficient from the Round-54 derivation packet.
2. Finite Cauchy--Schwarz and the algebraic Fejer expansion, derived in
   (10)--(11).
3. The explicitly stated radial half-weight hypothesis (6).

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-global-angular-shifted-correlation/briefs/blind_vdc_correlation_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-global-angular-shifted-correlation/derivation_packet.md.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  validation matrices, other Round-54 reports, or any other repository
  research artifact.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Retain as candidate evidence; do not promote the proposed analytic
mechanism.** Promote only the exact finite-differencing identity, endpoint
ledger, and incidence expansion after seam review. Record the quantitative
conclusion as follows: one coefficient-preserving step exposes a
target-capable signed correlation only for \(R\asymp N\), unless one proves
near-perfect cancellation of the diagonal for shorter \(R\). The step alone
does not save \(X^{1/8}\), and every termwise-absolute/divisor-envelope
closure has a sharp \(X^{1/8}\) capacity obstruction. The averaged signed
correlation estimate, coefficient-energy bound, angular-star convention,
and alpha transfer all remain unproved.

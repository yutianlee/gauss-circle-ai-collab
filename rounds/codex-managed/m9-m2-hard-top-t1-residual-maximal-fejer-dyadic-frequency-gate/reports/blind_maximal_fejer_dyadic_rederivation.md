# Blind maximal parity--Fejer dyadic rederivation

Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`
Role: statement-only blind rederiver
Date: 2026-08-26
Graph hash: deliberately unavailable under statement-only isolation

## 1. Result

**Route-specific no-go, with the finite algebraic kernel fully derived.**  The
parity-projected Fejer identity, the stopped dyadic telescoping identity, the
short-shift correction, the last non-doubling link, the exact-doubling tent
identity, and the adjacent-block Haar identity are all exact.  The
short-shift correction has the required bound

\[
 O_\varepsilon(LD)=O_\varepsilon(L^3X^\varepsilon).
\]

The disclosed support and \(\ell^2\) information do **not** imply the same
bound for the large dyadic links.  Their norm-only bound is

\[
 |A_S-A_R|\le \frac{S-R}{2}D,
\]

which is as large as \(L^4X^\varepsilon\) at the top scale.  This loss is
real: an admissible coherent dechirped control has an exact top increment
\(R^2/4\asymp L^4\).  The same control can be placed at either of the two
parity peaks.

Consequently, the first missing non-algebraic input is an actual-coefficient
signed upper bound for the remaining large links.  Section 2 also records
(MF), an absolute-value estimate on every link, as a convenient **stronger
sufficient condition**.  It is neither equivalent to the frozen one-sided
gate nor a uniquely necessary route to (B1).  Nothing in the statement-only
packet identifies the signed Vaaler/\(\chi _4\)/selector mechanism that would
prove even the frozen one-sided bound or rule out the coherent control for
the literal coefficient.  Thus this report neither proves nor falsifies
(B1) for the literal hard-TOP coefficient; it falsifies a derivation of the
one-sided gate from support, zero extension, and \(D\) alone.

## 2. Exact statement and hypotheses

Assume \(M\) and all Fejer lengths are positive integers, \(R_0=\lceil
L\rceil<M\), and the zero-extended array \(z\) is supported on \(M\)
consecutive sites.  Put

\[
 C_r:=\sum_{N\in\mathbb Z}z_{N+r}\overline {z_N},\qquad C_0=D.
\]

Then \(C_{-r}=\overline {C_r}\) and \(C_r=0\) for \(|r|\ge M\).  Define

\[
 I_R:=\int_0^1K_R^{(2)}(\theta)|Z(\theta)|^2\,d\theta,
 \qquad A_R:=\frac{I_R-D}{2}.
\]

### 2.1 Parity--Fejer identity

For every integer \(R\ge1\),

\[
 K_R^{(2)}(\theta)
 =\sum_{\substack{|r|<R\\2\mid r}}
       \left(1-\frac{|r|}{R}\right)e(r\theta),                                      \tag{2.1}
\]

and hence

\[
 I_R=D+2\Re\!\sum_{\substack{0<r<R\\2\mid r}}
             \left(1-\frac rR\right)C_r,
 \qquad
 A_R=\Re\!\sum_{\substack{0<r<R\\2\mid r}}
             \left(1-\frac rR\right)C_r.                                           \tag{2.2}
\]

There is one real part in (2.2), after the shift sum.

### 2.2 Stopped dyadic telescope and the short correction

Let \(R_{j+1}=\min(2R_j,M)\), and stop at the first \(K\) with
\(R_K=M\).  Then the left side of (B1), denoted \(T\), is exactly

\[
 \boxed{
 T=\sum_{j=0}^{K-1}(A_{R_{j+1}}-A_{R_j})+E_{\rm sh}},                               \tag{2.3}
\]

where

\[
 E_{\rm sh}
 =-\left(\frac1{R_0}-\frac1M\right)
   \Re\!\sum_{\substack{0<r<R_0\\2\mid r}}rC_r.                                  \tag{2.4}
\]

For arbitrary integers \(R<S\), the exact link is

\[
 A_S-A_R
 =\Re\!\sum_{\substack{0<r<S\\2\mid r}}w_{R,S}(r)C_r,                         \tag{2.5}
\]

with

\[
 w_{R,S}(r)=
 \begin{cases}
 \displaystyle \frac{r(S-R)}{RS},&0<r<R,\\[5pt]
 \displaystyle \frac{S-r}{S},&R\le r<S.
 \end{cases}                                                                        \tag{2.6}
\]

Thus, if the final link is non-doubling, its exact formula is (2.5)--(2.6)
with \(R=R_{K-1}\), \(S=M\), and \(R<M<2R\).  The site \(r=R\) is in
the second branch; \(r=S\) is absent.

### 2.3 Exact-doubling tent and Haar identities

For \(S=2R\), set

\[
 \tau_R(r)=\frac{\min(r,2R-r)}{2R}\quad(0<r<2R).
\]

Then

\[
 \Delta_R:=A_{2R}-A_R
 =\Re\!\sum_{\substack{0<r<2R\\2\mid r}}\tau_R(r)C_r.                             \tag{2.7}
\]

For the block form, let

\[
 y_n^{(\eta)}=(-1)^{\eta n}z_n\quad(\eta=0,1),
\]

and, with every array zero-extended, define adjacent blocks

\[
 P_{\eta,n}=\sum_{j=0}^{R-1}y_{n+j}^{(\eta)},\qquad
 Q_{\eta,n}=\sum_{j=R}^{2R-1}y_{n+j}^{(\eta)}.
\]

The triangular-tent correlation identity is

\[
 \boxed{
 \Delta_R=\frac1{4R}\Re\sum_{\eta=0}^1\sum_{n\in\mathbb Z}
                  Q_{\eta,n}\overline {P_{\eta,n}}}.                              \tag{2.8}
\]

The adjacent-block Haar-detail identity is

\[
 \boxed{
 \Delta_R=\frac1{16R}\sum_{\eta=0}^1\sum_{n\in\mathbb Z}
 \left( |P_{\eta,n}+Q_{\eta,n}|^2
       -|P_{\eta,n}-Q_{\eta,n}|^2\right)}.                                        \tag{2.9}
\]

Both identities hold for odd as well as even \(R\).  When \(R\) is odd,
the parity projection simply deletes the (odd) central lag.

### 2.4 The one-sided gate and a stronger sufficient theorem

For a chain link \(S=\min(2R,M)\), define the literal-coefficient form

\[
 \mathfrak M_{R,S}(c):=
 \Re\!\sum_{\substack{0<r<S\\2\mid r}}w_{R,S}(r)
 \sum_N c_{N+r}\overline {c_N}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).                                             \tag{2.10}
\]

Up to the harmless factor two between \(A_S-A_R\) and the full energy
increment, the frozen campaign gate is the one-sided assertion

\[
 \boxed{
 \mathfrak M_{R,S}(c)\ll_\varepsilon L^3X^\varepsilon
 \quad\text{for every stopped-dyadic link }(R,S)}.                                \tag{FG}
\]

A stronger sufficient assertion is

\[
 \boxed{
 |\mathfrak M_{R,S}(c)|\ll_\varepsilon L^3X^\varepsilon
 \quad\text{for every stopped-dyadic link }(R,S)}.                                 \tag{MF}
\]

The absolute value in (MF) is additional: (MF) implies (FG), but (FG) does
not imply (MF), and cancellations between links could in principle prove
(B1) without either linkwise statement.  Hence (MF) is not equivalent to
the frozen target or gate and is not uniquely necessary.

At an exact doubling, the stronger assertion (MF), considered on that link,
is algebraically equivalent to the actual-coefficient absolute Haar
imbalance estimate

\[
 \left|\Re\sum_{\eta,n}Q_{\eta,n}\overline {P_{\eta,n}}\right|
 \ll_\varepsilon R L^3X^\varepsilon,                                                \tag{2.11}
\]

or the corresponding bound by \(RL^3X^\varepsilon\) for the absolute value
of the numerator in (2.9).  This local algebraic equivalence concerns (MF)
only; it does not turn (MF) into the one-sided frozen gate.  The packet
supplies no theorem from which (FG), (MF), (2.11), or even their top-scale
instances follow.

If (MF) were proved with an arbitrarily reduced epsilon, (2.3), the
short-shift estimate below, and
\(K=O(1+\log(M/R_0))=O(\log L)\) would give (B1), with the logarithm
absorbed into \(X^\varepsilon\).

## 3. Proof and derivation

Expanding the Dirichlet square gives

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta).
\]

Translation by \(1/2\) multiplies its \(r\)-th Fourier coefficient by
\((-1)^r\).  Averaging therefore retains exactly the even lags and proves
(2.1).  Integrating against
\(|Z|^2=\sum_{a,b}z_a\overline {z_b}e((a-b)\theta)\), and pairing \(r\)
with \(-r\), proves (2.2).  The diagonal is exactly \(D\), not \(D/2\).

Subtracting from \(A_M\) the terms with \(0<r<R_0\), but with their
\(M\)-scale weights, gives

\[
 A_{R_0}-
 \Re\!\sum_{\substack{0<r<R_0\\2\mid r}}
       \left(1-\frac rM\right)C_r
 =-\left(\frac1{R_0}-\frac1M\right)
   \Re\!\sum_{\substack{0<r<R_0\\2\mid r}}rC_r.
\]

Inserting the ordinary telescope from \(A_{R_0}\) to \(A_M\) proves
(2.3)--(2.4).  Direct subtraction of the two Fejer weights proves
(2.5)--(2.6), including the final non-doubling link.  At \(S=2R\), the two
branches of (2.6) are \(r/(2R)\) and \((2R-r)/(2R)\), proving (2.7).

For (2.8), count pairs in two adjacent length-\(R\) blocks.  For
\(0<r<2R\), exactly

\[
 h_R(r):=\min(r,2R-r)
\]

pairs have separation \(r\), whence

\[
 \sum_nQ_{\eta,n}\overline {P_{\eta,n}}
 =\sum_{0<r<2R}h_R(r)(-1)^{\eta r}C_r.
\]

Summing \(\eta=0,1\) multiplies even lags by two and annihilates odd lags.
Division by \(4R\) proves (2.8).  Finally,

\[
 |P+Q|^2-|P-Q|^2=4\Re(Q\overline P)
\]

proves (2.9).

There is also an exact sliding-block Parseval check:

\[
 I_R=\frac1{2R}\sum_{\eta=0}^1\sum_n|P_{\eta,n}|^2.                                \tag{3.1}
\]

Since \(\sum_n|P_{\eta,n}|^2=\sum_n|Q_{\eta,n}|^2\), (3.1) at lengths
\(R\) and \(2R\) gives (2.8)--(2.9) again.  This also shows why the Haar
difference is signed rather than positive.

For every shift, Cauchy--Schwarz and zero extension give \(|C_r|\le D\).
Consequently

\[
 |E_{\rm sh}|
 \le \frac1{R_0}\sum_{r=1}^{R_0-1}rD
 \le \frac{R_0}{2}D
 \ll_\varepsilon L^3X^\varepsilon,                                                 \tag{3.2}
\]

because \(R_0=\lceil L\rceil\le2L\) for \(L\ge1\).  If \(Q=S-R\), an
exact sum over all positive lags gives

\[
 \sum_{r=1}^{S-1}w_{R,S}(r)
 =\frac{Q(R-1)}{2S}+\frac{Q(Q+1)}{2S}=\frac Q2.
\]

Thus

\[
 |A_S-A_R|\le\frac{S-R}{2}D,                                                        \tag{3.3}
\]

and parity restriction can only reduce this majorant.  Formula (3.3)
closes every link of width \(O(L)\), but an exact doubling of size \(R\)
costs \(RD\).  For \(R\asymp M\asymp L^2\), this is \(L^4X^\varepsilon\),
one full factor \(L\) beyond the target.

All endpoint conventions are already exact in these formulas.  Support on
\(M\) consecutive sites gives \(C_r=0\) for \(|r|\ge M\); no cyclic or
wraparound term occurs.  The lag \(r=R_0\), if even, is absent from
\(A_{R_0}\) and enters the first link with its correct new weight.  The lag
\(r=M\) is absent.  Blocks crossing either support endpoint use the stated
zero extension, and their contributions in (2.8)--(3.1) are precisely the
zero-extension jump contributions, not omitted boundary errors.

The full factor ledger from the packet is therefore:

1. \(D\) costs \(L^2X^\varepsilon\).
2. The short correction spends the one available factor \(L\) and closes.
3. A width-\(Q\) link costs \(QD\) without actual-coefficient cancellation.
4. Top links may have \(Q\asymp L^2\), costing \(L^4X^\varepsilon\); the
   target permits only \(L^3X^\varepsilon\).
5. The number of links costs only \(O(\log L)\), absorbable into epsilon.
6. The parity average, the single outer real part, and the endpoint terms
   cost only the exact constant factors displayed above; none supplies the
   missing factor \(L\).

### Common-frequency character--Poisson requirement

Put \(Z_\eta(\theta)=Z(\theta+\eta/2)\).  Every link has the exact common
frequency form

\[
 A_S-A_R
 =\frac14\sum_{\eta=0}^1\int_0^1
   \bigl(F_S(\theta)-F_R(\theta)\bigr)|Z_\eta(\theta)|^2\,d\theta.                  \tag{3.4}
\]

A finite character--Poisson transform aimed at the frozen gate must remain
exact at one common \(\theta\) and prove an upper bound for the complete
signed quantity on the right of (3.4), uniformly for every stopped-dyadic
link.  It need not bound the negative side.  If instead the transform aims
at the stronger sufficient condition (MF), it must bound the absolute value
of that complete signed quantity; at exact doubling that stronger task is
exactly (2.11).

In particular, if a proof of (MF) writes the block numerator as
\(\sum_\nu \mathcal T_\nu\) and then proposes
\(|\sum_\nu\mathcal T_\nu|\le\sum_\nu|\mathcal T_\nu|\), it must first
prove the normalized positive bound

\[
 \sum_\nu|\mathcal T_\nu|
 \ll_\varepsilon R L^3X^\varepsilon                                                \tag{3.5}
\]

for the numerator in (2.8), with the analogous exact normalization for
(2.5).  This bound must include the zero dual mode, character-diagonal and
cross-character terms, both parity branches, finite-interval boundary
terms, floors/stars/crossings, and all literal coefficient signs.  It must
also exhibit the actual signed property that rules out both coherent peak
controls below.  Applying a modulus shift by shift, row by row, or before
the two Haar energies are subtracted proves only a false unsigned/adversarial
analogue.  Parseval supplies (3.3), not (3.5).

## 4. First doubtful or unproved step

The first doubtful step is exactly the passage from the identities
(2.5), (2.8), or (3.4) to the frozen one-sided bound (FG).  The absolute
estimate (MF) is one stronger sufficient replacement, not the uniquely
necessary missing theorem.  No formula for the literal residual coefficient
is present in the statement-only packet.  The words listing selectors,
squarefree masks, \(\chi _4\), complementary branches, profiles, floors,
stars, crossings, point values, and endpoint jumps do not themselves imply
a quantitative cancellation theorem.

In particular, the square-root chirp cannot be used in isolation: an
allowed complex coefficient in the coarse support/\(D\) class can dechirp it
exactly.  Nor does parity projection remove the obstruction, because the
two coherent arrays concentrated at \(0\) and \(1/2\) have identical even
correlations.  A proof of the frozen one-sided gate, or of the stronger
(MF), must identify and prove an explicit algebraic or transformed
orthogonality property of the **actual** coefficient.  That signed
actual-coefficient estimate is the first open analytic step, not an endpoint
or Fejer normalization issue.

## 5. Required control tests and outcomes

### 5.1 Coherent dechirped control: FAIL for a norm-only link theorem

Take \(L=2^m\), \(M=L^2\), \(R=M/2\), \(X=L^8\), \(J=L^4\), and
\(H=L^2\).  These satisfy the displayed scale conditions, and \(R\to2R=M\)
is a link in the stopped dyadic chain.  On any positive interval of \(M\)
sites set

\[
 c_N=e(-J\sqrt N),\qquad z_N=1.
\]

Then \(D=M=L^2\), and \(C_r=M-r=2R-r\) for \(0\le r<M\).  Writing
\(R=2q\), direct summation of (2.7) gives

\[
 \Delta_R
 =\frac2R\left\{
   \sum_{k=1}^{q}k(R-k)+\sum_{t=1}^{q-1}t^2
 \right\}
 =\frac{R^2}{4}
 =\frac{L^4}{16}.                                                                   \tag{5.1}
\]

For any fixed \(\varepsilon<1/8\), (5.1) exceeds
\(L^3X^\varepsilon=L^{3+8\varepsilon}\) by an unbounded power for a
sufficiently smaller fixed epsilon (for example \(\varepsilon=1/16\)).
This is an exact falsification of every proof using only the disclosed
support and \(D\) hypotheses.  It is not asserted to be a literal hard-TOP
coefficient.

Replacing \(z_N\) by \((-1)^N\), equivalently taking
\(c_N=(-1)^Ne(-J\sqrt N)\), leaves every even \(C_r\) unchanged.  The first
array has its coherent Fourier peak at \(\theta=0\); the second has it at
\(\theta=1/2\).  Hence both parity peaks fail the norm-only theorem.

### 5.2 One-site and diagonal control: PASS

If \(z\) is supported at one site, then \(C_r=0\) for every \(r\ne0\).
Thus \(A_R=0\), every link is zero, and the target is zero.  On the frequency
side, \(|Z|^2=D\), \(\int K_R^{(2)}=1\), and hence \(I_R=D\).  In the block
form, a site cannot lie in both adjacent blocks for the same \(n\), so the
cross product in (2.8) vanishes and the two Haar energies in (2.9) agree.
This passes only with the exact diagonal subtraction and constants above.

### 5.3 Global Parseval and parity-peak audit: PASS as normalization, FAIL as closure

Global Parseval gives \(\int_0^1|Z|^2=D\).  Since (2.1) has nonnegative
Fourier coefficients at even lags, the two global maxima of the parity
kernel occur at \(0\) and \(1/2\), with

\[
 \max_\theta K_R^{(2)}(\theta)
 =K_R^{(2)}(0)=K_R^{(2)}(1/2)
 =\begin{cases}
 R/2,&R\text{ even},\\[2pt]
 (R+R^{-1})/2,&R\text{ odd}.
 \end{cases}                                                                        \tag{5.2}
\]

Thus Parseval only gives a weighted-energy bound of order \(RD\), exactly
the scale exposed by (5.1).  The fact that \(K_R^{(2)}\) has mean one does
not bound \(I_R\) by \(D\), because \(|Z|^2\) may concentrate at either
peak.

No numerical experiment was used in this report; all controls above are
exact analytic calculations.

## 6. Dependencies and exact artifacts used

The original blind derivation read only the following authorized artifacts:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/blind_statement.md`.

No claim graph, active campaign, strategy file, barrier packet, prior round,
sibling report, source, or other context was read during that derivation.
A later scope-only repair used the Round 172 strategy and
`reviews/parity_dyadic_endpoint_seam_review.md` to distinguish the frozen
one-sided gate from the stronger absolute-value condition (MF); it changed
no finite identity or control calculation.  The derivation uses only finite
Fourier expansion, Parseval, adjacent-block pair counting,
Cauchy--Schwarz, and finite arithmetic sums.  No external theorem is used.

## 7. Recommended state effect

**Retain** the exact identities (2.1)--(2.9), the endpoint audit, and the
short-budget bound (3.2) as candidate finite algebra.  **Reject** any
support/Parseval-only or positive unsigned dual-mode closure of the large
dyadic links.  **No change** to the accepted proof state and no promotion of
(B1): this route requires a separately proved actual-coefficient one-sided
estimate such as (FG), including the final non-doubling link and a
demonstrated signed mechanism excluding both coherent parity-peak controls.
The absolute link theorem (MF) would suffice, but is strictly stronger and
is not claimed necessary or equivalent to the frozen gate.

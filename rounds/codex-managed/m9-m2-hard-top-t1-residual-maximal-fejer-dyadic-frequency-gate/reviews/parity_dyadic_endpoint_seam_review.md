# Round 172 parity--dyadic endpoint seam review

Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate  
Role: independent finite-algebra and endpoint-seam reviewer  
Date: 2026-08-26  
Verdict: **REPAIR**

## 1. Result

The parity--Fejer expansion, stopped-chain telescope, sign of the short
correction, general non-doubling weight, exact-doubling tent, full-line
endpoint treatment, and doubling-only Haar identity are correct in all
three reports once their normalizations are reconciled. In particular, the
blind report's coefficients $1/(4R)$ and $1/(16R)$ concern the half-energy

\[
 \mathcal A_R:=\frac{\mathfrak E_R^{(2)}-D}{2},
\]

whereas the discovery and hostile reports generally discuss the full energy
increment. There is no missing factor two in those formulas.

Three repairs are required.

1. In discovery control (172.D22), $Q$ points on one absolute parity
   progression occupy at least $2Q-1$ consecutive integer sites. Inside the
   frozen $M$-site interval, its stated hypothesis $Q\ge 2R$ forces
   $R\le (M+1)/4$, so that version is not the terminal link
   $R=M/2\to M$. The calculation needs only $Q\ge R$. With
   $M=4P$ and $Q=R=2P$, it becomes exactly the hostile report's admissible
   terminal one-parity construction and its full energy increment is
   $P^2$. Thus the capacity conclusion survives, but (172.D22) needs a
   containment and normalization repair.
2. The blind report's (MF) asks for an absolute-value estimate on every
   link. This is a stronger sufficient statement than the campaign's frozen
   one-sided link target. It must not be called the uniquely necessary
   missing theorem or equivalent to that frozen target. The coherent
   control has a positive large increment, so it still obstructs a
   coefficient-uniform proof of the weaker one-sided target.
3. Discovery bound (172.D1) is a valid local first-link estimate, but it is
   not an “owner-complete strict sector” because its complement is not
   target-safe. For exact integer endpoint coverage it should be stated
   with $S=\min(2R_0,M)$, not only as $R_0\to2R_0$.

There is no substantive finite-algebra conflict among the reports. The
blind convention $E_{\rm sh}=-B_{\rm short}$ is identical to the
discovery/hostile convention in which $B_{\rm short}$ is subtracted.

Separately, discovery claims a completed cardinal character--Poisson
identity and a target-safe ordinary zero mode, whereas the hostile report
calls that residual transform gate unclosed. That is a genuine
report-level analytic disagreement, but it lies outside this bounded
finite-algebra and endpoint seam and is not adjudicated here.

## 2. Exact statement and hypotheses

Let $z=(z_N)_{N\in\mathbb Z}$ be zero outside an interval of $M$
consecutive integer sites, and put

\[
 C_r=\sum_N z_{N+r}\overline{z_N},\qquad
 a_r=\Re C_r,\qquad
 D=C_0=\sum_N|z_N|^2.
\]

Then $C_{-r}=\overline{C_r}$, $C_r=0$ for $|r|\ge M$, and
$|C_r|\le D$. For each positive integer $R$, set

\[
 w_R(r)=(1-r/R)_+,\qquad
 \mathcal A_R=
 \sum_{\substack{0<r<R\\2\mid r}}w_R(r)a_r.
\]

The exact normalization is

\[
 \boxed{\mathfrak E_R^{(2)}=D+2\mathcal A_R.}
 \tag{R172.1}
\]

For the stopped chain $R_{j+1}=\min(2R_j,M)$, with repetitions removed
and $R_K=M$, define

\[
 B_{\rm short}:=
 \sum_{\substack{0<r<R_0\\2\mid r}}
 \{w_M(r)-w_{R_0}(r)\}a_r
 =
 \left(\frac1{R_0}-\frac1M\right)
 \sum_{\substack{0<r<R_0\\2\mid r}}r\,a_r.
 \tag{R172.2}
\]

Then

\[
 \boxed{
 T_{26}
 =\sum_{j<K}(\mathcal A_{R_{j+1}}-\mathcal A_{R_j})
   -B_{\rm short}
 =\frac12\sum_{j<K}
   (\mathfrak E_{R_{j+1}}^{(2)}-\mathfrak E_{R_j}^{(2)})
   -B_{\rm short}.}
 \tag{R172.3}
\]

Thus the blind report's $E_{\rm sh}$ is exactly
$E_{\rm sh}=-B_{\rm short}$.

## 3. Proof or derivation

### 3.1 Parity--Fejer identity and both site parities

The finite Dirichlet-square expansion is

\[
 F_R(\theta)
 =\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta).
\]

Translation by $1/2$ multiplies the $r$th Fourier coefficient by
$(-1)^r$. Hence

\[
 K_R^{(2)}(\theta)
 =\sum_{\substack{|r|<R\\2\mid r}}
  \left(1-\frac{|r|}{R}\right)e(r\theta).
 \tag{R172.4}
\]

Expanding $|Z|^2$, integrating, and pairing $r$ with $-r$ gives
(R172.1). The diagonal coefficient is exactly $1$, hence exactly $D$,
and there is one real part after the complete positive-shift sum. Because
an even shift preserves absolute site parity, (R172.4) retains both
even-site and odd-site correlations and removes only cross-parity shifts.

### 3.2 Telescope, short correction, and endpoints

Since

\[
 \mathcal A_M
 =T_{26}+
 \sum_{\substack{0<r<R_0\\2\mid r}}w_M(r)a_r,
\]

inserting the ordinary telescope from $\mathcal A_{R_0}$ to
$\mathcal A_M$ proves (R172.3), including its minus sign. If
$q=\lfloor(R_0-1)/2\rfloor$, then

\[
 |B_{\rm short}|
 \le
 \left(\frac1{R_0}-\frac1M\right)q(q+1)D
 <\frac{R_0}{4}D
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{R172.5}
\]

The reports' coarser $R_0D/2$ and $R_0D$ estimates are safe. The short
correction is paid once, not once per link.

For arbitrary integers $R<S\le2R$, direct subtraction gives

\[
 b_{R,S}(r):=w_S(r)-w_R(r)=
 \begin{cases}
 \dfrac{r(S-R)}{RS},&0<r<R,\\[5pt]
 1-\dfrac rS,&R\le r<S,\\[5pt]
 0,&r\ge S.
 \end{cases}
 \tag{R172.6}
\]

The two branches agree at $r=R$; $r=S$ is absent; and
$b_{R,S}(0)=0$. Therefore

\[
 \mathcal A_S-\mathcal A_R
 =\sum_{\substack{0<r<S\\2\mid r}}b_{R,S}(r)a_r,
\qquad
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =2\sum_{\substack{0<r<S\\2\mid r}}b_{R,S}(r)a_r.
 \tag{R172.7}
\]

For $S=2R$, this is the exact tent

\[
 b_{R,2R}(r)=
 \begin{cases}
 r/(2R),&0<r<R,\\
 1-r/(2R),&R\le r<2R,\\
 0,&r\ge2R.
 \end{cases}
 \tag{R172.8}
\]

If $R$ is odd, the central lag $r=R$ is odd and the parity projection
deletes it; if $R$ is even, it remains with weight $1/2$. Full-line zero
extension includes every block crossing either support endpoint. There is
no wraparound term, and $r=M$ is absent. A strict final
$R<M<2R$ link must use (R172.6), not a rounded Haar identity.

### 3.3 Adjacent blocks and Haar coefficients

Put $y_n^{(\eta)}=(-1)^{\eta n}z_n$, and define

\[
 P_{\eta,s}=\sum_{j=0}^{R-1}y_{s+j}^{(\eta)},\qquad
 Q_{\eta,s}=\sum_{j=R}^{2R-1}y_{s+j}^{(\eta)}.
\]

Exact pair counting gives

\[
 \sum_sQ_{\eta,s}\overline{P_{\eta,s}}
 =
 \sum_{0<r<2R}\min(r,2R-r)(-1)^{\eta r}C_r.
\]

Summing over $\eta=0,1$ retains twice the even lags. Thus

\[
 \boxed{
 \mathcal A_{2R}-\mathcal A_R
 =
 \frac1{4R}\Re\sum_{\eta,s}
 Q_{\eta,s}\overline{P_{\eta,s}}
 =
 \frac1{16R}\sum_{\eta,s}
 \left(
 |P_{\eta,s}+Q_{\eta,s}|^2
 -
 |P_{\eta,s}-Q_{\eta,s}|^2
 \right).}
 \tag{R172.9}
\]

For the full energy increment the two constants are, respectively,
$1/(2R)$ and $1/(8R)$.

Equivalently, define absolute-site-parity blocks

\[
 Y_{s,R}^{(\epsilon)}
 =
 \sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j}.
\]

Then

\[
 \mathfrak E_R^{(2)}
 =\frac1R\sum_{s,\epsilon}|Y_{s,R}^{(\epsilon)}|^2,
\qquad
 \mathfrak H_R^{(2)}
 =\frac1{2R}\sum_{s,\epsilon}
 |Y_{s,R}^{(\epsilon)}-Y_{s+R,R}^{(\epsilon)}|^2,
\]

and

\[
 \mathfrak E_{2R}^{(2)}
 =2\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)},
\qquad
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.
 \tag{R172.10}
\]

This remains valid for odd $R$ because the parity in $Y$ is absolute site
parity. Relative-position parity would interchange the two classes in the
second block when $R$ is odd.

### 3.4 Both peaks, dechirped controls, one site, and the first link

Splitting the length-$R$ Dirichlet polynomial into its even and odd terms
shows that the two equal maxima occur at $0$ and $1/2$, with

\[
 K_R^{(2)}(0)=K_R^{(2)}(1/2)=
 \begin{cases}
 R/2,&2\mid R,\\[2pt]
 (R+R^{-1})/2,&2\nmid R.
 \end{cases}
 \tag{R172.11}
\]

For an exact doubling, the bandpass values at both peaks are $R/2$ when
$R$ is even and $(R-R^{-1})/2$ when $R$ is odd.

For the blind full-interval control, take $M=2R$ with $R$ even and put
$z_N=1$ on all $M$ sites. Then $D=2R$, $C_r=2R-r$, and exact summation of
the tent gives

\[
 \mathcal A_{2R}-\mathcal A_R=\frac{R^2}{4},\qquad
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}=\frac{R^2}{2}.
 \tag{R172.12}
\]

Replacing $z_N$ by $(-1)^Nz_N$ leaves every even $C_r$ unchanged and
moves the coherent Fourier peak from $0$ to $1/2$. Thus both parity peaks
give the same obstruction.

For $Q$ points on one absolute parity progression and even $R$, provided
$Q\ge R$, one has $D=Q$ and $C_{2s}=Q-s$. The exact full increment is

\[
 2\sum_{s=1}^{R-1}b_{R,2R}(2s)(Q-s)
 =
 \frac{QR}{2}-\frac{R^2}{4}
 \ge\frac{QR}{4}.
 \tag{R172.13}
\]

Such a progression needs at least $2Q-1$ containing integer sites. The
hostile choice $M=4P$, $Q=R=2P$ is admissible and gives the exact full
increment $P^2\asymp MD$. This is the corrected terminal realization of
(172.D22).

A one-site sequence has $C_r=0$ for every $r\ne0$, so
$\mathfrak E_R^{(2)}=D$ for all $R$, every link is zero, the adjacent-block
cross product is zero, and the two Haar energies agree. No transformed
diagonal or endpoint term may survive this control.

Finally, let $S=\min(2R_0,M)$ and $Q_0=S-R_0$. Exact summation of
(R172.6) over all positive lags gives

\[
 \sum_{r=1}^{S-1}b_{R_0,S}(r)=\frac{Q_0}{2}.
\]

Consequently

\[
 \boxed{
 |\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}|
 \le Q_0D
 \le R_0D
 \ll_\varepsilon L^3X^\varepsilon.}
 \tag{R172.14}
\]

This proves the discovery first-link estimate even when the first link is
terminal and non-doubling. It is coefficient-uniform, not a new arithmetic
saving.

## 4. First doubtful or unproved step

There is no doubtful finite-algebra step after the repairs above. The first
open campaign step is an actual-coefficient signed, one-sided bound for each
later large stopped-dyadic link, before any positive norm:

\[
 \mathfrak E_{R_{j+1}}^{(2)}-\mathfrak E_{R_j}^{(2)}
 \ll_\varepsilon L^3X^\varepsilon
\]

for the links not already covered by (R172.14). The blind absolute-value
(MF) is a stronger sufficient replacement, not the frozen necessary
statement. The positive controls (R172.12)--(R172.13) obstruct
coefficient-uniform proofs even of the weaker one-sided statement.

This review does not decide the sibling disagreement about whether the
discovery cardinal transform and its ordinary-zero-mode estimate complete
the literal residual transform gate.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| parity coefficient and diagonal | **PASS.** Even lags retain their original Fejer weights; the diagonal coefficient is $1$. |
| one outer real part | **PASS.** It appears after pairing $C_r$ and $C_{-r}$. |
| stopped telescope and correction sign | **PASS.** $T_{26}=\frac12\sum\Delta\mathfrak E-B_{\rm short}$; blind $E_{\rm sh}=-B_{\rm short}$. |
| short correction once | **PASS.** Exact bound (R172.5), paid once. |
| terminal non-doubling link | **PASS.** Formula (R172.6), with $r=S$ absent. |
| doubling tent and odd central lag | **PASS.** Formula (R172.8); an odd central lag is projected out. |
| adjacent-block/Haar constants | **PASS.** Half-energy constants $1/(4R),1/(16R)$; full-energy constants twice these. |
| absolute site parities and zero extension | **PASS.** Both classes and all crossing blocks are retained. |
| both parity peaks | **PASS.** Exact heights (R172.11); the two dechirped arrays have identical even correlations. |
| blind full-interval control | **PASS.** Exact values (R172.12). |
| discovery one-parity control | **REPAIR.** Add $2Q-1\le M$, weaken the unnecessary $Q\ge2R$ to $Q\ge R$, and use (R172.13); the hostile construction is the terminal realization. |
| one-site control | **PASS.** Every increment is exactly zero. |
| first-link $L^3$ estimate | **PASS WITH ENDPOINT REPAIR.** State it for $S=\min(2R_0,M)$ as (R172.14). |
| blind (MF) versus frozen gate | **REPAIR.** Absolute-value (MF) is stronger than the campaign's one-sided requirement. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

Only the following assigned artifacts were read:

1. protocol.md;
2. strategy/round172_m2_hard_top_t1_residual_maximal_fejer_dyadic_strategy.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reports/blind_maximal_fejer_dyadic_rederivation.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reports/literal_maximal_fejer_dyadic_frequency_attack.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reports/maximal_fejer_transform_endpoint_hostile_audit.md.

The review uses only finite Fourier expansion, pair counting, the
parallelogram identity, Cauchy--Schwarz, and exact finite sums. No external
source or sibling artifact was used.

## 7. Recommended state effect

**Repair, then retain** the finite parity--dyadic kernel as candidate
evidence. Apply the exact D22 containment/normalization correction, state
the first link with $S=\min(2R_0,M)$, remove “owner-complete” from the
uncomplemented first-link sector, and relabel blind (MF) as a stronger
absolute-value sufficient condition rather than the frozen necessary gate.

These repairs do not change the route-scoped conclusion: the first link and
short correction are target-safe, later coefficient-uniform positive
control has $L^4X^\varepsilon$ capacity, and no target or proof-graph node
is promoted. The first open step is the actual-coefficient signed,
one-sided $L^3X^\varepsilon$ bound for every remaining large link before
positivity. The residual transform/zero-mode disagreement requires its own
analytic adjudication and must not be resolved from this endpoint review.

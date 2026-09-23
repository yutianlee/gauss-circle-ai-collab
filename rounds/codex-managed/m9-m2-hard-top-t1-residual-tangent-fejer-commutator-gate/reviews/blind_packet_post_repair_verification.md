# Blind packet post-repair verification

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Role: statement-only post-repair verification
- Context: protocol.md, repaired blind_statement.md, and the original blind
  report only for the repair delta
- Graph hash: not supplied and not accessed
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

**Verdict: GREEN for the packet repairs.**

GREEN here means:

1. the malformed control byte is gone;
2. the repaired near-square, opened-weight, active-divisor, and weighted
   incidence hypotheses now prove the complete commutator bound
   \[
   \sum_j|\mathcal C_{R_j,R_{j+1}}|
   \ll_\varepsilon L^3X^\varepsilon;
   \]
3. both counterexamples in the original blind report are outside the
   repaired literal coefficient class; and
4. the exact self-return remains valid and is the first obstruction to the
   frozen remainder route.

This verdict does **not** prove the frozen remainder estimate. Exact
reindexing still gives

\[
\mathcal R_{R,T}=\Delta_{R,T}-\mathcal C_{R,T}.
\]

Thus, after the now-valid target-safe commutator is paid, estimating the
remainder is equivalent up to \(O_\varepsilon(L^3X^\varepsilon)\) to
estimating the original physical stopped-chain link sum. The proposed
commutator supplies no new cancellation for that remainder.

The repaired packet is therefore internally correct as an
identity-or-no-go packet: its commutator ledger is now valid, and its
terminal analytic conclusion remains an exact tautological self-return.

## 2. Exact statement and hypotheses

The repaired packet adds the following uniform hypotheses on every nonzero
opened incidence:

\[
N=dm\asymp L^2,\qquad d\asymp L,\qquad m\asymp L,
\qquad |\lambda_N(d)|\ll X^\eta,
\tag{2.1}
\]

with at most \(X^\eta\) active divisors per product after epsilon
rebudgeting. It also explicitly records the resulting weighted absolute
double-opening ledger:

\[
\sum_{\substack{N'-N<T\\N'>N}}
\ \sum_{\substack{d\mid N,\ d'\mid N'\\
                   d,d'\ {\rm active}}}
|\lambda_{N'}(d')\lambda_N(d)|
\ll MTX^{O(\eta)}.
\tag{2.2}
\]

Every phase has modulus one, and selectors, deletion masks, profiles,
endpoints, point values, and zero extensions are already included in the
literal weights. Hence (2.2) is exactly the absolute opened-incidence
quantity needed below.

The tangent chart retains

\[
r_{s+1}-r_s=2m'.
\tag{2.3}
\]

Because the target atom is also a nonzero opened near-square incidence,
(2.1) now gives

\[
m'\asymp L.
\tag{2.4}
\]

The stopped chain begins at \(R_0=\lceil L\rceil\); therefore every link
satisfies \(T\gg L\), including the strict final non-doubling link.

The frozen question continues to permit either a proof of
\(\sum_j\mathcal R_j\ll L^3X^\varepsilon\) or the location of an exact
tautology obstruction. The repaired hypotheses validate the commutator
side only; they introduce no regularity for \(G(s)-G(s+1)\).

## 3. Proof or derivation

### 3.1 Control-byte verification

The repaired blind statement was checked bytewise. It contains:

- zero control bytes other than ordinary tab/newline/CRLF formatting; and
- zero carriage returns not immediately followed by a line feed.

The divisor condition now appears literally as
\(d\ \mathrm{odd}\). The original embedded carriage-return corruption is
gone.

### 3.2 Pointwise and multiplicity ledger

For one physical ordered pair \((N,N')\), each endpoint has at most
\(X^\eta\) active divisors. Hence there are at most \(X^{2\eta}\) opened
divisor pairs. Each product of opened weights is
\(O(X^{2\eta})\). Consequently the absolute opened contribution of one
physical pair is \(O(X^{4\eta})\).

An \(M\)-site interval has \(O(MT)\) ordered pairs with positive gap below
\(T\). Thus

\[
\sum_{\rm opened\ incidences}|G(s)|
\ll MTX^{4\eta},
\tag{3.1}
\]

which agrees with the packet's stated \(MTX^{O(\eta)}\) ledger. Any fixed
number of literal branches, endpoints, or selector classes is already
absorbed in the exponent and does not change the power of \(L\).

### 3.3 Complete commutator bound

For \(R<T\le2R\), the continuous extension of the bandpass has slopes

\[
\frac{T-R}{RT},\qquad-\frac1T,\qquad0.
\]

It is continuous at \(0,R,T\), so it is globally \(1/T\)-Lipschitz,
including cusp crossings and endpoint crossings. Therefore

\[
\begin{aligned}
|\beta_{R,T}(r_s)-\beta_{R,T}(r_{s+1})|
&\le \min\left\{1,\frac{2m'}{T}\right\}\\
&\ll \frac{L}{T},
\end{aligned}
\tag{3.2}
\]

where the final inequality uses \(m'\asymp L\) and \(T\gg L\). It is valid
for exact doublings and for the strict terminal link.

Using (3.1),

\[
\begin{aligned}
|\mathcal C_{R,T}|
&\le
\sum_{\rm opened}
|\beta(r_s)-\beta(r_{s+1})|\,|G(s)|\\
&\ll
\frac LT\cdot MTX^{O(\eta)}\\
&\ll
MLX^{O(\eta)}
\asymp L^3X^{O(\eta)}.
\end{aligned}
\tag{3.3}
\]

The stopped chain has \(O(\log L)\) links. Choose the arbitrarily small
\(\eta\) in terms of the requested \(\varepsilon\), and absorb the
logarithm into \(X^\varepsilon\). Then

\[
\boxed{
\sum_j|\mathcal C_{R_j,R_{j+1}}|
\ll_\varepsilon L^3X^\varepsilon.}
\tag{3.4}
\]

This is an absolute estimate, so it is stronger than needed for the single
outer real part. Support births, deaths, selector changes, and point-value
jumps do not create an extra commutator term: they restrict the incidences
already counted in (3.1), while the global Lipschitz estimate handles every
bandpass crossing.

### 3.4 Exclusion of the two original counterexamples

The first counterexample used the single opening

\[
d=N,\qquad m=1.
\]

It violates both \(d\asymp L\) and \(m\asymp L\) when
\(N\asymp L^2\). Its original support also ranged from \(N=1\) upward,
whereas every repaired nonzero incidence has \(N\asymp L^2\). It is
therefore not a member of the repaired literal class, even though its
opened weight had modulus one.

The second counterexample used products \(N=1,15\), factors
\((d',m')=(1,15),(3,5)\), and an unrestricted cancelling weight \(A\).
For growing \(L\), it violates

\[
N\asymp L^2,\qquad d,d',m,m'\asymp L.
\]

Its choice \(A=L^5\) with \(X\asymp L^8\) also violates
\(|\lambda_N(d)|\ll X^\eta\) for arbitrarily small fixed \(\eta\).
Hence it is excluded independently by both the support-scale and
opened-weight repairs.

The repairs do not claim that arbitrary adversarial near-square weights
are target-safe in the remainder. They only exclude these two particular
false controls and make the commutator incidence count lawful.

### 3.5 Independent self-return check

For one fixed link, put

\[
S=\Re\sum_s(-1)^s\beta(r_s)G(s)
=\frac12\Delta_{R,T},
\qquad
A=\Re\sum_s(-1)^s\beta(r_{s+1})G(s).
\tag{3.5}
\]

Finite zero extension gives, with \(t=s+1\),

\[
\Re\sum_s(-1)^s\beta(r_{s+1})G(s+1)
=-\Re\sum_t(-1)^t\beta(r_t)G(t)
=-S.
\tag{3.6}
\]

Therefore the constants and signs are

\[
\mathcal C_{R,T}=S-A,\qquad
\mathcal R_{R,T}=S+A,
\tag{3.7}
\]

and hence

\[
\boxed{
\mathcal R_{R,T}
=\Delta_{R,T}-\mathcal C_{R,T}.}
\tag{3.8}
\]

The repair changes the admissible coefficient class but does not change
this finite identity. Summing links,

\[
\sum_j\mathcal R_{R_j,R_{j+1}}
=
\sum_j\Delta_{R_j,R_{j+1}}
-
\sum_j\mathcal C_{R_j,R_{j+1}}.
\tag{3.9}
\]

Together with (3.4), a one-sided \(L^3X^\varepsilon\) upper bound for the
remainder is equivalent, up to another target-safe term, to the same
one-sided bound for the original physical stopped-chain link sum. No
regularity of \(G(s)-G(s+1)\) has been added, and the reindexing produces
no new sign or small multiplier. The exact self-return conclusion is
therefore retained without revision.

## 4. First doubtful or unproved step

All repairs requested for the commutator ledger pass. The first remaining
unproved analytic step is the frozen remainder estimate itself, equivalently
the physical stopped-chain estimate in (3.9).

The packet still explicitly forbids assuming regularity across adjacent
products or divisors. Thus no bound for \(G(s)-G(s+1)\) follows from the
new pointwise and multiplicity hypotheses. Those hypotheses control
\(\sum|G|\) well enough only because the commutator carries the small
bandpass multiplier \(L/T\). The remainder has no such multiplier.

Accordingly, the first exact terminal obstruction is not an endpoint,
chart, multiplicity, or restored-power defect. It is the tautology

\[
\mathcal R=\Delta-\mathcal C
\]

with \(\mathcal C\) now proved target-safe. Any argument claiming that the
finite commutator identity alone bounds \(\mathcal R\) would be assuming
the original physical link estimate in equivalent form.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| embedded control byte | **GREEN.** Zero lone carriage returns and zero other forbidden control bytes. |
| odd-divisor typography | **GREEN.** The repaired condition is explicit and well formed. |
| near-square factor support | **GREEN.** It now implies \(m'\asymp L\) on every nonzero target incidence. |
| pointwise opened weight | **GREEN.** \(|\lambda_N(d)|\ll X^\eta\) is explicit. |
| active-divisor multiplicity | **GREEN.** At most \(X^\eta\) active divisors at each endpoint gives at most \(X^{2\eta}\) opened pairs per physical pair. |
| weighted incidence ledger | **GREEN.** Re-derived as \(MTX^{O(\eta)}\). |
| bandpass slopes and cusps | **GREEN.** Global \(1/T\)-Lipschitz control includes \(0,R,T\) and the final non-doubling link. |
| per-link commutator power | **GREEN.** \((L/T)(MT)=ML\asymp L^3\). |
| stopped-chain commutator sum | **GREEN.** \(O(\log L)\) is absorbed by epsilon rebudgeting. |
| original single-divisor example | **EXCLUDED.** It has \(m=1\) and \(d=N\), contrary to \(d,m\asymp L\). |
| original cancelling-opening example | **EXCLUDED.** It violates the product/factor scales and the arbitrarily-small-\(\eta\) pointwise bound. |
| exact constants in the split | **GREEN.** \(\Delta=2S\), \(\mathcal C=S-A\), and \(\mathcal R=S+A\). |
| remainder self-return | **RETAIN.** \(\mathcal R=\Delta-\mathcal C\) exactly, with no endpoint correction. |
| frozen remainder estimate | **NOT PROVED.** After (3.4), it is the original physical stopped-chain estimate up to a target-safe term. |
| numerical work | **Not used.** Every check is exact. |

## 6. Dependencies and exact artifacts used

Exactly three artifacts were read or used:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/blind_statement.md; and
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/reports/blind_tangent_fejer_commutator_rederivation.md,
   used only to identify and retest the repaired seams and the two original
   controls.

No graph, shared state, strategy, sibling report, proof kernel, source card,
web result, or computation was accessed or used.

## 7. Recommended state effect

**Recommended effect: accept the repaired blind packet and the absolute
commutator estimate; retain the route-specific self-return no-go; do not
promote the frozen remainder target.**

The valid post-repair kernel is:

\[
\sum_j|\mathcal C_{R_j,R_{j+1}}|
\ll_\varepsilon L^3X^\varepsilon,
\qquad
\sum_j\mathcal R_j
=\sum_j\Delta_j+O_\varepsilon(L^3X^\varepsilon).
\tag{7.1}
\]

The second relation is an equivalence, not an estimate of either signed
sum. It shows that the tangent first-difference commutator pays a
target-safe correction but returns exactly to the original physical
stopped-chain problem.

No additional packet repair is required for this scoped conclusion. A
future proof of the remainder would need a genuinely new actual-symbol
correlation theorem for the physical link sum; it cannot follow from this
finite reindexing alone.

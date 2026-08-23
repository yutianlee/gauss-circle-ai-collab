# Conductor candidate: dyadic fixed-centre square-function connector

Campaign: `full-proof-frontier-inequality-selection-gate`

Starting graph SHA-256:
`fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`

## 1. Result: lemma or no-go result

There is a short exact conditional connector from the Round-122 lower-GAR
survivor to a fixed-centre dyadic square-function estimate.  This does not
prove the square-function estimate, but it replaces the single weighted
linear target by a noninvertible endpoint-average whose diagonal is at the
quarter scale.

## 2. Exact statement and hypotheses

Use the notation of Round 122:

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 K_\delta=yX^\delta,
\]

and

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}W(k)S^\circ(k)
 +O_{\varepsilon,\delta}(RX^\varepsilon),
 \qquad
 S^\circ(k)=\mathcal I_k\mathscr V_\delta-kc_y.
\tag{127.C1}
\]

Here \(\mathcal I_k\) is the exact oriented interval from \(N\) to
\(N+k\), \(c_y=\sum_{d\leq y}\chi_4(d)/d\), and
\(\mathscr V_\delta\) is the literal low-two-adic increment in
(122.J17), including all residue, full-divisor, complement, and overlap
labels.  Round 122 proves that replacing
\(\mathcal I_k\mathscr V_\delta\) by its centered form
\(S^\circ(k)\) in the retained sum costs only
\(O_{\varepsilon,\delta}(RX^\varepsilon)\): the complete identity
\(\sum_k kW(k)=0\) and the already-controlled central and far tails own
the localization leakage.  The centering is essential; the uncentered
square-function statement is false.

Assume that for every \(K=2^jR\), with the last block clipped at
\(K_\delta\), and

\[
 \mathcal K_K=\{k:K<|k|\leq\min(2K,K_\delta)\},
\]

one has

\[
 \boxed{
 \sum_{k\in\mathcal K_K}
 |S^\circ(k)|^2
 \ll_{\varepsilon,\delta}K(R^2+K)X^\varepsilon.}
\tag{127.SF}
\]

Then

\[
 \mathcal B_{\rm flat}^{(N)}
 \ll_{\varepsilon,\delta}RX^\varepsilon.
\tag{127.C2}
\]

Consequently, through the already accepted Round-121 and Round-122
connectors, (127.SF) is sufficient for the exact lower-radial GAR target.
It is not asserted to be necessary or equivalent.

## 3. Proof or derivation

Round 122 proves

\[
 |W(k)|\ll_A{1\over R+|k|}
 \left(1+{|k|\over y}\right)^{-A}.
\]

On a retained dyadic shell \(|k|\asymp K>R\), therefore, for every
fixed \(A\),

\[
 \sum_{k\in\mathcal K_K}|W(k)|^2
 \ll_A K^{-1}\left(1+{K\over y}\right)^{-2A}.
\tag{127.C3}
\]

Cauchy--Schwarz and (127.SF) give

\[
 \begin{aligned}
 \left|\sum_{k\in\mathcal K_K}
 W(k)S^\circ(k)\right|
 &\leq
 \left(\sum|W(k)|^2\right)^{1/2}
 \left(\sum|S^\circ(k)|^2\right)^{1/2}\\
 &\ll_{\varepsilon,\delta}
 K^{-1/2}\left(1+{K\over y}\right)^{-A}
 \{K(R^2+K)X^\varepsilon\}^{1/2}\\
 &\ll_{\varepsilon,\delta,A}
 R\left(1+{K\over y}\right)^{1/2-A}X^{\varepsilon/2},
\end{aligned}
\tag{127.C4}
\]

where \(y\asymp R^2\).  The shells with \(K\leq y\) contribute only an
\(O(\log X)\) factor, while those with \(K>y\) are geometrically
summable after choosing \(A>1/2\).  The logarithm is absorbed by replacing
\(\varepsilon/2\) with \(\varepsilon\).  Combining (127.C4) with the
already target-safe central, far, high-two-adic, centering, and odd-central
packages in (127.C1) proves (127.C2).

The diagonal capacity in (127.SF) is compatible with the proposed scale.
The divisor bound gives
\(|\mathscr V_\delta(n)-c_y|\ll_\varepsilon X^\varepsilon\), hence the
diagonal after expanding \(\sum|S^\circ(k)|^2\) is

\[
 \ll_\varepsilon K^2X^\varepsilon.
\tag{127.C5}
\]

This is at most the right side of (127.SF) for every retained \(K\),
including the collar \(K>y\).  Thus the unresolved content of (127.SF)
is a signed off-diagonal correlation, not an oversized diagonal.

## 4. First doubtful or unproved step

No uniform proof of (127.SF) is known.  Expanding its off-diagonal produces
a fixed-centre short-interval correlation of the exact truncated
character-divisor increments.  Existing global or centre-averaged mean
squares do not imply this bound uniformly in \(N=\lfloor X\rfloor\), and
full-circle completion would recreate the circle coefficient.  This is the
first and only analytic gap in the connector.

## 5. Required control tests and outcomes

- **Both orientations:** pass.  The sum in (127.SF) contains positive and
  negative \(k\); one may also apply the same argument to the two clipped
  orientations separately.
- **Dyadic endpoints:** pass.  The first and last blocks are intersected
  with the exact retained set, and (127.C3) only improves under clipping.
- **Diagonal:** pass at the stated epsilon bookkeeping by (127.C5).
- **Coherent arbitrary increments:** correctly fail.  If
  \(\mathscr V(N+j)-c_y=1\), then
  \(|S^\circ(k)|\asymp|k|\), so the left side of
  (127.SF) is \(\asymp K^3\) and violates the proposed bound for
  \(K\gg R\).  The connector therefore does not prove the false unsigned
  or arbitrary-coefficient analogue.
- **Pure mean:** pass only after the mandatory centering.  If
  \(\mathscr V(N+j)=c_y\), then \(S^\circ(k)=0\); without subtracting
  \(kc_y\), (127.SF) would fail on every long shell.
- **Sparse spike:** pass.  One isolated centered increment gives shell energy
  \(O(K)\), below \(R^2K\).
- **Complement and full-circle labels:** pass at the connector seam only:
  they remain inside \(\mathscr V_\delta\) before squaring.  No separate
  residue or valuation norm is used.
- **Noninvertibility:** qualified pass.  Endpoint averaging followed by
  an \(L^2\) norm loses phase information and is not a Fourier, Abel, or
  complementary-divisor inversion.  It is nevertheless a strictly
  stronger sufficient norm than the scalar weighted wavelet because it
  discards cross-\(k\) phases.  Its eligibility therefore rests on its
  target-safe diagonal, retention of every arithmetic label inside
  \(S^\circ(k)\), and failure on coherent adversarial increments; it must
  not be advertised as an equivalent minimal target.

## 6. Dependencies and exact artifacts used

- `state/proof_obligations.yml`, nodes
  `M9-M1-lower-radial-flat-discrepancy-equivalence` and
  `M9-M1-lower-near-square-wavelet-reduction`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reviews/conductor_round122_complement_adjudication.md`.

No numerical evidence or external theorem is used.

## 7. Recommended state effect

Promote only the conditional square-function connector as a proved
internal reduction after independent review.  Retain (127.SF), the
lower-radial estimate, GAR, `M9-M1`, every `M9-M2` parent, `M9`, and all
exponent improvements as open.  For strategy selection, (127.SF) is a
lawful Round-128 objective because it is exact, noninvertible, has a
target-safe diagonal, rejects coherent adversarial coefficients, and has a
finite off-diagonal failure seam.

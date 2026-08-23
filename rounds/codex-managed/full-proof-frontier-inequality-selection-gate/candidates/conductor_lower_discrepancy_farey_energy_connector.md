# Conductor candidate: exact lower-discrepancy Farey energy connector

Campaign: `full-proof-frontier-inequality-selection-gate`

Starting graph SHA-256:
`fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`

## 1. Result: lemma or no-go result

The exact centered Round-121 discrepancy has a finite reduced-Farey
expansion.  Its dyadic endpoint square function is therefore an exact
prescribed-centre determinant correlation.  The equal-frequency diagonal
is at the required capacity.  A diagonal-scale bound for the remaining
signed determinant correlation is sufficient for the lower-GAR target.

The Farey identity, the diagonal estimate, and the conditional connector
are proved below.  The off-diagonal estimate is open.

## 2. Exact statement and hypotheses

Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

\[
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),\qquad
 c_y=\sum_{d\leq y}{\chi_4(d)\over d},
\]

and, for every integer \(k\),

\[
 D_N(k)=\mathcal I_k(A_y-c_y),
\tag{127.F1}
\]

where \(\mathcal I_k\) is the exact oriented interval from \(N\) to
\(N+k\).  For \(T\geq1\), define

\[
 L_\chi(T)=\sum_{g\leq T}{\chi_4(g)\over g},\qquad
 \lambda_b={\chi_4(b)\over b}L_\chi(y/b).
\tag{127.F2}
\]

For a reduced fraction \(a/b\) and an integer \(k\), let

\[
 G_k(a/b)=
 \begin{cases}
  \displaystyle\sum_{1\leq j\leq k}e(aj/b),&k>0,\\
  0,&k=0,\\
  \displaystyle-\sum_{k<j\leq0}e(aj/b),&k<0.
 \end{cases}
\tag{127.F3}
\]

Then the exact reduced-Farey identity is

\[
 \boxed{
 D_N(k)=
 \sum_{\substack{2\leq b\leq y\\b\ {m odd}}}
 \lambda_b
 \sum_{\substack{1\leq a<b\\(a,b)=1}}
 e(aN/b)G_k(a/b).}
\tag{127.F4}
\]

Fix a dyadic \(K\geq R\), let

\[
 \mathcal K_K=\{k:K<|k|\leq\min(2K,K_\delta)\},
\]

and define

\[
 \mathcal Q_K=\sum_{k\in\mathcal K_K}|D_N(k)|^2.
\tag{127.F5}
\]

If, uniformly over the retained shells,

\[
 \boxed{\mathcal Q_K\ll_{\varepsilon,\delta}
 K(y+K)X^\varepsilon,}
\tag{127.FE}
\]

then the exact lower wavelet and hence the lower-radial GAR analytic target
are \(O_{\varepsilon,\delta}(RX^\varepsilon)\).

## 3. Proof or derivation

For every positive integer \(m\), additive orthogonality gives

\[
 1_{d\mid m}={1\over d}\sum_{r\bmod d}e(rm/d).
\tag{127.F6}
\]

Write each nonzero fraction \(r/d=a/b\) in lowest terms, so
\(r=ag\), \(d=bg\), and \(g\leq y/b\).  Since only odd \(d\)
contribute, \(b\) and \(g\) are odd and
\(\chi_4(bg)=\chi_4(b)\chi_4(g)\).  Grouping equal reduced fractions in
(127.F6) yields

\[
 A_y(m)=c_y+
 \sum_{\substack{2\leq b\leq y\\b\ {m odd}}}
 \lambda_b
 \sum_{a\bmod b}^{*}e(am/b).
\tag{127.F7}
\]

Applying the oriented interval \(\mathcal I_k\) to (127.F7) and
subtracting \(kc_y\) proves (127.F4) for both signs of \(k\).

Squaring (127.F4) gives

\[
 \mathcal Q_K=
 \sum_{a,b}\sum_{a',b'}
 \lambda_b\overline{\lambda_{b'}}
 e\!\left({N(ab'-a'b)\over bb'}\right)
 H_K(a/b,a'/b'),
\tag{127.F8}
\]

where all fractions are reduced, both denominators are odd and at most
\(y\), and

\[
 H_K(\alpha,\beta)=
 \sum_{k\in\mathcal K_K}G_k(\alpha)\overline{G_k(\beta)}.
\tag{127.F9}
\]

Thus determinant zero is literally equality of the two reduced fractions.
The off-diagonal phase is the prescribed-centre determinant phase with
\(n=ab'-a'b\ne0\).

The partial character sums are bounded, so
\(|\lambda_b|\ll b^{-1}\).  For the determinant-zero diagonal, enlarge
the primitive numerator set to all \(1\leq a<b\).  If \(b\leq2K\),
periodicity and additive orthogonality give uniformly in \(k\)

\[
 \sum_{a=1}^{b-1}|G_k(a/b)|^2\ll b^2.
\tag{127.F10}
\]

Its contribution is therefore
\(O(K)\) per denominator.  If \(b>2K\), then \(|k|<b\) on the block
and the exact orthogonality identity gives

\[
 \sum_{a=1}^{b-1}|G_k(a/b)|^2=b|k|-k^2\ll bK.
\tag{127.F11}
\]

After summing over \(k\) and multiplying by \(b^{-2}\), this costs
\(O(K^2/b)\) per denominator.  Consequently

\[
 \mathcal Q_{K,=}
 \ll K^2+K^2\sum_{2K<b\leq y}{1\over b}
 \ll K(y+K)X^\varepsilon.
\tag{127.F12}
\]

The unresolved content of (127.FE) is therefore only the complete signed
\(n\ne0\) part of (127.F8); its diagonal is target-safe.

Finally, Round 122 gives

\[
 |W(k)|\ll_A(R+|k|)^{-1}(1+|k|/y)^{-A}.
\]

Hence

\[
 \sum_{k\in\mathcal K_K}|W(k)|^2
 \ll_AK^{-1}(1+K/y)^{-2A}.
\]

Cauchy--Schwarz with (127.FE) bounds one block by

\[
 \ll RX^{\varepsilon/2}(1+K/y)^{1/2-A}.
\]

The blocks below \(y\) cost one logarithm, and those above \(y\) are
geometrically summable for \(A>1/2\).  The already accepted central and
far packages finish the \(RX^\varepsilon\) wavelet estimate.

## 4. First doubtful or unproved step

No estimate of the \(n\ne0\) part of (127.F8) at the scale
\(K(y+K)X^\varepsilon\) is proved.  A coefficient-blind Farey large
sieve sees spacing \(y^{-2}\) and retains the same polynomial excess that
the actual phase must remove.  The first open step is therefore a
fixed-centre, actual-coefficient determinant large sieve for the kernel
\(H_K\), not the exact identity or its diagonal.

Existing Kloosterman-fraction estimates cannot be imported without first
matching the coupled \(H_K\), real prescribed centre \(N\), all
determinants, reduced supports, and the nonseparable coefficients in
(127.F8).

## 5. Required control tests and outcomes

- **Centering:** pass.  The \(b=1\) term in (127.F7) is exactly \(c_y\)
  and disappears from (127.F4); omitting this step would create a false
  coherent square-function.
- **Negative orientation:** pass by the oriented definition (127.F3).
- **Lift multiplicity and character:** pass.  Every lift is summed in
  \(L_\chi(y/b)\) before any modulus, and multiplicativity is used only on
  odd \(b,g\).
- **Determinant zero:** pass.  Reduced fractions make
  \(ab'-a'b=0\) equivalent to \((a,b)=(a',b')\), and (127.F12) is at
  target capacity.
- **Coherent arbitrary coefficients:** correctly fail.  Replacing the
  actual \(\lambda_b e(aN/b)\) by phase-conjugating coefficients can
  recover the ambient Farey capacity; (127.FE) is an actual-direction
  theorem, not a coefficient-uniform large sieve.
- **Stronger-norm scope:** qualified.  The square function discards
  cross-\(k\) phases and is sufficient rather than equivalent.  It is not
  an ambient operator norm: the exact character lifts and prescribed
  centre remain inside before squaring, its diagonal is target-safe, and
  the arbitrary coherent analogue fails.  It must nevertheless be stated
  as a stronger bridge, not as the minimal scalar target.
- **Round-122 labels:** the connector starts from the broader exact
  centered discrepancy (127.F1), so it does not delete the accepted safe
  packages termwise inside the square.  This is lawful only as a stronger
  sufficient route; no claim is made that their square norms are already
  owned.
- **Downstream scope:** even (127.FE) would close only the lower-GAR
  analytic parent.  It would not prove blockwise `M9-M1`, any `M9-M2`
  parent, endpoint uniformity, `M9`, or an exponent by itself.

## 6. Dependencies and exact artifacts used

- `state/proof_obligations.yml`, especially
  `M9-M1-lower-radial-flat-discrepancy-equivalence` and
  `M9-M1-lower-near-square-wavelet-reduction`;
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reviews/conductor_round122_complement_adjudication.md`.

No numerical evidence or external theorem is used.

## 7. Recommended state effect

After an independent line audit, promote the exact reduced-Farey identity,
the determinant-zero bound, and the conditional square-function connector.
Retain (127.FE), lower GAR, `M9-M1`, every `M9-M2` parent, `M9`, and all
exponents as open.

For strategy selection, choose the off-diagonal part of (127.FE) only if
the stronger-norm qualification is accepted explicitly.  It is the only
candidate in this round with a newly exposed, target-safe diagonal and a
single exact signed off-diagonal, but it remains a sufficient energy route,
not the scalar wavelet itself.

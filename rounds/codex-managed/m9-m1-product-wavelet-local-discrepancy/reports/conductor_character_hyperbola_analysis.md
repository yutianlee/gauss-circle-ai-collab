# Character-hyperbola discrepancy analysis

## 1. Result

The corrected all-integer Abel identity is exact. Period-four pairing
cancels matched crossing rows but leaves an exact signed symmetric
difference of unmatched rows. Substituting that identity back into the
wavelet-weighted Abel sum reconstructs the original product-wavelet
functional. Thus neither pairing nor wavelet averaging supplies the
missing (H/L) factor by itself.

## 2. Exact statement and hypotheses

Let

\[
 A(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X),\qquad A(n)=0\ (n\leq0),
\]

and let (c_X=\sum_j\chi_4(j)\Xi(j/\sqrt X)/j). Fix
(n_0=\lfloor X\rfloor). Define (D(n_0)=0) and extend to every
integer by

\[
 D(n)-D(n-1)=A(n)-c_X.
\tag{2.1}
\]

For (W_n=K((n-X)/(2T))),

\[
 \sum_n A(n)W_n=\sum_nD(n)(W_n-W_{n+1}).
\tag{2.2}
\]

For integral (0<v<\inf(\operatorname{supp}\Xi)\sqrt X), set

\[
 C_j(v)=\mathbf1_{\{\exists m:\ n_0<jm\leq n_0+v\}}.
\]

Then

\[
 D(n_0+v)=\sum_r\Xi((4r+1)/\sqrt X)
 \{C_{4r+1}(v)-C_{4r+3}(v)\}
 +O_\Xi(1+v/\sqrt X).
\tag{2.3}
\]

## 3. Proof or derivation

Equation (2.1) gives (A(n)=D(n)-D(n-1)+c_X). Discrete summation by
parts and the exact sampled zero mode \(\sum_nW_n=0\) prove (2.2); the
negative tail is Schwartz-negligible. For positive (v<j), each
supported denominator has at most one multiple in the thin interval, so
the floor increment is (C_j(v)). Pairing (4r+1) with (4r+3) gives

\[
 \Xi_jC_j-\Xi_{j+2}C_{j+2}
 =\Xi_j(C_j-C_{j+2})+(\Xi_j-\Xi_{j+2})C_{j+2}.
\]

The second term and the two cutoff ends total (O_\Xi(1)); period-four
Abel gives (vc_X=O_\Xi(v/\sqrt X)). This proves (2.3).

For the actual product variables, the natural (j,j+2) paired products
are separated by order \(\sqrt X\), whereas (T=o(\sqrt X)). Hence the
thin window sees unmatched rather than locally paired fibers. Inserting
the crossing formula into (2.2) and interchanging the finite sums returns
the original coefficient-wavelet convolution.

## 4. First doubtful or unproved step

The exact survivor is

\[
 \sup_{|v|\leq TX^\eta}\left|
 \sum_r\Xi((4r+1)/\sqrt X)
 \{C_{4r+1}(v)-C_{4r+3}(v)\}\right|
 \ll_\varepsilon X^{1/4+\varepsilon},
\tag{4.1}
\]

or the weaker signed convolution of this quantity with
(W_n-W_{n+1}). This is not proved.

## 5. Required control test and outcome

- Abel sign/index: pass only with the affine all-integer extension.
- Main term: (c_X\ll X^{-1/2}), hence target-safe.
- Unmatched rows: exact coefficients are (0,\pm1); no deterministic
  saving follows.
- Wavelet average: exact self-return, not a new estimate.
- Exact products/squares/fourth powers: divisor-sized locally, but they
  rule out generic irrationality arguments.
- Power ledger: at \(\nu=2/5\), absolute capacity is (X^{3/10+o(1)}),
  target is (X^{1/4+\varepsilon}), leaving (X^{1/20}=H/L).

## 6. Dependencies and exact artifacts used

This conductor-materialized analysis records the completed discovery
agent's result message, the Round-65 derivation packet, and the Round-64
synthesis. The agent was stopped before writing its assigned file; this
report is therefore candidate evidence, not a clean independent gate. No
numerics or external theorem were used.

## 7. Recommended state effect

Promote only the affine Abel reduction and exact unmatched-row formula
after independent validation. Retain LCD, its weighted form, PSC, GAR,
M9-M1, M9, and the target open. No exponent change.

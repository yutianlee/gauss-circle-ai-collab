# Round 135 conductor controls

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`

Starting graph SHA-256:
`f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| primary source versions | Check Bettin--Chandee v1 Theorem 1, Remark 1, and Corollary 1; Wright v2 Theorem 2.1 and Corollary 2.2; exclude the withdrawn negative control. | Green. The theorem statements, coefficient norms, coprimality, fixed factor, support, range, and absolute-value placement are recorded in the durable source card. |
| integral frequency and real centre | Write \(X=N_0+\xi\), use the integral source frequency \(N_0\), and retain \(e(\xi k/r)\). | Green after repair. The fractional-centre factor belongs to the smooth amplitude on every frozen flat cell. |
| smooth profile separation | Scale \(k=Ku\), \(r=Rv\), include \(K/k\), \(q_L\), \(W\), and the fractional-centre factor, and Fourier-invert on buffered log coordinates. | Green. All normalized derivatives and the integrated projective mass are \(O(1)\), uniformly on the strict-UNBAL polytope. |
| direct source normalization | Use \((a,m,n)=(k,1,r)\), \(\|\alpha\|_2=1\), \(\|\beta\|_2\asymp R^{1/2}\), and \(\|\nu\|_2\asymp K^{-1/2}\). | Green. Bettin--Chandee gives \(F^{1/2}(R^{11/10}K^{-3/20}+R)\); Wright's decisive fifth term gives \(R^{11/8}F^{1/4}\). |
| direct polytope margin | Subtract the exponent \(u=\delta-\ell\) of \(\Delta\) from every direct source exponent. | No-go. The three strict margins are respectively greater than \(3/10\), \(1/4\), and \(5/16\). |
| Wright convention and fixed factor | Compare the printed third term with the final proof line and test whether a growing \(R_0\) is legal in the direct map. | Green with a recorded convention. The weaker printed \(A^{-1/20}\) theorem is used; the common fifth term is decisive. Since \(M=1\), \(R_0\ll M^C\) forces \(R_0=O(1)\). |
| square inverse connector | On coprime rows, use \(a=j^2\), \(j=m=k\), and \(m^2\overline m\equiv m\pmod r\); price the diagonal detector. | Green. The detector has sharp projective norm \(\asymp1\), equivalently only \(K^{1/2}\) inflation over the direct \(k^{-1}\) norm. |
| square-connector capacity | Insert \((A,M,N)=(K^2,K,R)\) into both source theorems and subtract \(u\). | No-go. The two Bettin--Chandee margins remain greater than \(3/10\) and \(1/4\); the Wright margin remains greater than \(5/16\). |
| smooth-weight-first completion | Complete the original smooth \(k\)-weight before applying inversion and restore every gcd stratum. | Green, equal capacity. Inversion permutes units, the complete sum is Ramanujan (or additive before coprimality), and the total is exactly \(\Delta X^\varepsilon\). |
| inverse-selector-first completion | Reindex by \(m=\overline k\pmod r\), complete the rough selector, and use the exact complete-frequency second moment. | Green as a diagnostic no-go. It produces \(\sum_h\widehat g_r(h)S(N_0,h;r)\), a joint \((r,h)\)-coefficient matrix, and positive outer cost \(R\sqrt\Delta X^\varepsilon\). |
| gcd ownership | Repeat both completion orders after \(r=gn\), \(k=gj\), without discarding non-coprime rows. | Green. The harmonic gcd ledger is divisor-sized and changes no displayed capacity. |
| physical fixed residue | Put \(s=N_0+t\) and compare the exact congruence \(t\equiv-N_0\pmod r\) with Wright Corollary 2.2. | Source-level no-go. Uniform coprimality, independent convolution, size range, principal subtraction, and modulus-by-modulus absolute-value hypotheses do not match. |
| fixed determinant | For \(\tau=N_0-dr\ne0\), use \((m_1,n_2,m_2,n_1)=(d,r,1,N_0)\) in Bettin--Chandee Corollary 1. | Green as a legal but non-saving map. Main terms aggregate to \(\Delta X^\varepsilon\); the error per determinant is \(X^{3/5+\varepsilon}R^{17/20}\), with exponent greater than \(41/40\). The zero determinant is divisor-bounded. |
| character and absolute values | Track \(\chi_4(r)\) and every outer absolute value through direct maps, completions, and dispersion. | Green. The character remains in the signed source coefficient until a lawful positive source norm is taken; no averaged discrepancy is substituted for the fixed-centre scalar. |
| owner and downstream scope | Compare the proved proposition with the graph dependency closure. | Green. Only the flat-smooth prescribed-centre principal owner and a scoped method obstruction change; all omitted owners, M9-M1, M9-M2, endpoint uniformity, M9, the bridge, and both global exponents stay unchanged. |

## Post-unmask and artifact corrections

1. The real-centre issue is repaired by integral-frequency extraction plus
   uniformly smooth absorption; it is not an obstruction.
2. The nonconstant inverse connector is exact, and its sharp diagonal
   projective norm is \(\asymp1\), not a factor \(K\).
3. The two completion orders are distinct: smooth-weight-first is
   Ramanujan and equal-capacity, while inverse-selector-first is genuinely
   Kloosterman and strictly worse after positive outer summation.
4. Every gcd stratum is restored before the final capacity comparison.
5. The physical residue is the integer \(-N_0\), but the other Wright
   dispersion hypotheses still fail.
6. Three embedded carriage returns and four delimiter defects were repaired
   mechanically without changing the mathematical conclusions.

## Validation record

- State Patch: validated and applied cleanly, with 2 creates, 3 updates,
  14 rejections, and 8 explicit no-change records.
- Resulting graph SHA-256:
  `c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`.
- Patched graph: green under structural, dependency, and evidence-path
  validation.
- Completed campaign manifest: green.
- Unit tests: six of six passed under explicit test discovery.
- Source compilation: `math_collab` and tests green.
- JSON parsing: active campaign, next-round plan, round ledger, validation
  matrix, campaign plan, and State Patch green.
- Artifact hygiene: all 21 Round-135 files are strict UTF-8 with no
  unexpected C0/DEL bytes, replacement characters, trailing whitespace,
  conflict markers, or unbalanced inline/display delimiters.
- Diff check: green, with line-ending warnings only.

No numerical experiment was used. The round was 100% analytical,
algebraic, and primary-source audit work.

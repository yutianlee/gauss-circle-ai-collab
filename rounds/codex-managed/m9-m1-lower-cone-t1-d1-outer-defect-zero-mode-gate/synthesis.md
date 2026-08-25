# Round 156 synthesis

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Terminal label: outer_defect_zero_mode_target
- Graph mutation: applied
- Resulting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea

## Outcome

Round 156 proves the entire mandatory \(v=0\) theta row in the full
outer-defect range.  For

\[
 q=4N,\qquad
 M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM},
\tag{156.Y1}
\]

the literal normalized row satisfies

\[
 \boxed{
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt{\frac{4N}{d}}\,
 \widehat B_j(0)K\!\left(0,-j;\frac{4N}{d}\right)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.}
\tag{156.Y2}
\]

This is a genuine signed gain over the Round-155 absolute upper
capacity.  It holds for arbitrary \(N\), every odd \(d\mid N\), both
defect signs, the exact residual phase, actual profile transitions, zero
extension, asymmetric cell, strict mask, and all hard endpoints.

## Literal coefficient seam

On each signed dyadic interval, the actual zero Fourier coefficient
\(A_j=\widehat B_j(0)\) satisfies

\[
 \sup_j|A_j|+\operatorname {Var}_j A_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{156.Y3}
\]

For fixed \(x\), the profile argument \((x^2-j)/N\) is monotone.  Hence
the zero-extended real profile charges every component and transition
through its actual total variation.  The exact phase is

\[
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x,
\qquad
 \left|\frac{\partial}{\partial j}
 (\sqrt{x^2-j}-x)\right|\ll K^{-1},
\tag{156.Y4}
\]

so its block variation is \(O(V/K)\le O(1)\).  The two asymmetric cell
cutoffs and strict block endpoints are included.  Summing the fixed-
\(x\) estimate over \(O(KX^\varepsilon)\) physical representatives gives
(156.Y3).  Ordered divisibility subsequences can only decrease this
variation.

## Exact character and local arithmetic

For \(m=N/d=u^2r\), \(r\) squarefree, the multiplier decomposes into the
primitive Kronecker characters of the fundamental discriminants

\[
 \Delta_+=
 \begin{cases}r,&r\equiv1\pmod4,\\4r,&r\equiv2,3\pmod4,\end{cases}
 \qquad
 \Delta_-=
 \begin{cases}-r,&r\equiv3\pmod4,\\-4r,&r\equiv1,2\pmod4.\end{cases}
\tag{156.Y5}
\]

With \(\alpha=(1+i)/2\) and \(\beta=(1-i)/2\),

\[
 K(0,-j;4m)=
 \alpha G_{4m,\chi_{\Delta_+}}(-j)
 +\beta G_{4m,\chi_{\Delta_-}}(-j).
\tag{156.Y6}
\]

If a constituent has primitive conductor \(f\mid c\), \(c=fL\), its
exact induced transform is

\[
 G_{c,\chi}(n)=
 \tau(\chi)
 \sum_{\substack{e\mid R_f\\L/e\mid n}}
 \mu(e)\chi(e)\frac Le\,
 \overline\chi\!\left(\frac{n}{L/e}\right),
\qquad
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p.
\tag{156.Y7}
\]

The reports and terminal reviews compute every odd prime power, the
two-adic conductors \(1,4,8\), exact phases, repeated-prime Ramanujan
shells, the conductor-one square case, and the \(\chi_{\pm8}\)
half-support cancellation.  These formulas certify all arithmetic
strata, but the final target proof does not spend their absolute support
capacity.

## Exact all-divisor recombination and interval theorem

Define

\[
 \mathscr S_N(j)=
 \sum_{x\bmod4N}
 {\bf1}_{N\mid x^2-j}
 \chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{156.Y8}
\]

The exact quotient projector, the unique partition \(d=(h,N)\), and the
complete even quadratic Gauss sum give

\[
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c),
 \qquad c=\frac{4N}{d}.
\tag{156.Y9}
\]

Thus

\[
 \mathcal Z_U(V)=
 \frac1{4N}\sum_{V<|j|\le2V}A_j\mathscr S_N(j).
\tag{156.Y10}
\]

The physical root identity

\[
 \mathscr S_N(j)=
 \rho_{4N}(j+N)-\rho_{4N}(j+3N)
\tag{156.Y11}
\]

checks that no imprimitive or two-adic stratum is averaged away.  The
finite Fourier transform of \(\mathscr S_N\) vanishes at even
frequencies and has magnitude

\[
 2\sqrt{8N(h,N)}
\tag{156.Y12}
\]

at odd \(h\).  Finite Fourier inversion and geometric sums imply

\[
 \sup_{\substack{I\ {\rm consecutive}\\|I|\le4N}}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll \sqrt N\,\tau(N)\log(2N).
\tag{156.Y13}
\]

Abel summation with (156.Y3) and (156.Y10) gives (156.Y2).

The blind report independently proves, for every fixed \(d\),

\[
 \sup_{I\ {\rm consecutive}}
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c),
\tag{156.Y14}
\]

by opening the nonzero unit frequencies and summing finite geometric
series.  Restoring every \(d\) gives the same \(M^{-1/4}\) power.  Hence
the target does not depend on cancellation between divisor strata or on
an external character-sum theorem.

## Reviews, source status, and remaining seam

Three terminal reviews are GREEN:

- independent recombination mathematics;
- independent source and legal method; and
- hostile literal-profile, endpoint, and normalization review.

The initial source audit's strict range and arbitrary-weight no-match are
superseded for \(v=0\), because the actual progression variation is now
proved internally.  Its primitive-character, induced-transform, and
two-adic source cards remain valid.  Pólya--Vinogradov is a legal but
unnecessary fallback.

The first open object is now the incomplete nonzero matrix

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{156.Y15}
\]

Neither elementary zero-row interval identity estimates this coupled
object.

## Downstream status

The fixed-polylogarithmic collar from Round 154 remains the last proved
range for the complete D=1 wave because (156.Y15) is open.  The strict
boundary \(M^{449}\asymp R^{780}\) is unchanged.  Every \(D>1\),
\(L>1\), generic \(t=1\), original \(t\ge2\), cross, remaining M1, and
M2 owner remains separate.  Endpoint uniformity, M9, and the
unconditional bridge remain open.

The internally proved global exponent remains \(1/3\).  The separately
audited external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{156.Y16}
\]

No global exponent changes in Round 156.

## State effect

The validated State Patch creates one proved-internal zero-row
cancellation node; updates seven frontier and source interfaces; rejects
eighteen overbroad inferences; and records eight principal downstream
obligations unchanged.  The resulting graph is
3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea.

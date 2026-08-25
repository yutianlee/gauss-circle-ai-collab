# Round 156 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Round: 156
- Starting graph SHA-256: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Terminal label: outer_defect_zero_mode_target
- Terminal reviews: independent recombination mathematics GREEN; independent source and legal-method GREEN; hostile literal-profile and endpoint GREEN
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Result

Round 156 proves the complete theta zero row in the full frozen range.
For

\[
 q=4N,\qquad
 M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM},
\tag{156.A1}
\]

let \(A_j=\widehat B_j(0)\) be the zero Fourier coefficient of the
literal ambient pre-linearization profile.  Then

\[
 \boxed{
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt{\frac{4N}{d}}\,
 A_jK\!\left(0,-j;\frac{4N}{d}\right)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.}
\tag{156.A2}
\]

The proof retains arbitrary \(N\), every odd \(d\mid N\), both defect
signs, the exact residual phase, actual profile components and
transitions, zero extension, asymmetric cell, strict mask, and every
endpoint.  The external \(B_{1,U}(1)\) remains outside (156.A2) and costs
only \(X^\varepsilon\) at assembly.

The zero row is now removed from the list of missing inputs.  The
incomplete nonzero matrix remains the first open \(D=d=L=1\)
outer-defect interface.  No complete positive-power defect range or
global exponent changes.

## 2. Exact arithmetic statement

For fixed \(d\), put \(m=N/d\), \(c=4m\), and write \(m=u^2r\) with
\(r\) squarefree.  Define the fundamental discriminants

\[
 \Delta_+=
 \begin{cases}r,&r\equiv1\pmod4,\\4r,&r\equiv2,3\pmod4,\end{cases}
 \qquad
 \Delta_-=
 \begin{cases}-r,&r\equiv3\pmod4,\\-4r,&r\equiv1,2\pmod4.\end{cases}
\tag{156.A3}
\]

With \(\chi_\pm=(\Delta_\pm/\cdot)\),
\(\alpha=(1+i)/2\), and \(\beta=(1-i)/2\),

\[
 K(0,-j;c)=
 \alpha G_{c,\chi_+}(-j)+\beta G_{c,\chi_-}(-j).
\tag{156.A4}
\]

If a primitive constituent has conductor \(f\mid c\), put \(L=c/f\) and
\(R_f=\prod_{p\mid c,\ p\nmid f}p\).  Its exact induced transform is

\[
 G_{c,\chi}(n)=
 \tau(\chi)
 \sum_{\substack{e\mid R_f\\L/e\mid n}}
 \mu(e)\chi(e)\frac Le\,
 \overline\chi\!\left(\frac{n}{L/e}\right).
\tag{156.A5}
\]

This gives every valuation and repeated-prime stratum.  At a prime in
the conductor, \(v_p(n)=v_p(c)-v_p(f)\) exactly.  At a prime outside the
conductor, the local factor is the Ramanujan value

\[
 0,\quad -p^{\nu-1},\quad p^{\nu-1}(p-1)
\tag{156.A6}
\]

on \(v_p(n)\le\nu-2\), \(v_p(n)=\nu-1\), and
\(v_p(n)\ge\nu\), respectively.  The two-adic conductor exponent is
\(0\), \(2\), or \(3\); the \(\chi_{\pm8}\) rows, their exact phases,
and their half-support cancellation are retained.  The only principal
constituent occurs when \(m\) is a square and is treated as an exact
Ramanujan sum.  The independent mathematics and source reviews verified
all local tables, CRT phases, and support claims.

## 3. Verified proof kernel and power ledger

### 3.1 Literal coefficient variation

On either signed dyadic block, monotone sampling of the real
zero-extended profile, the exact identity

\[
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x,
\qquad
 \left|\frac{\partial}{\partial j}
 (\sqrt{x^2-j}-x)\right|\ll K^{-1},
\tag{156.A7}
\]

and the literal cell give

\[
 \sup_{j\in I_\pm}|A_j|
 +\operatorname {Var}_{j\in I_\pm}A_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{156.A8}
\]

Profile transitions are charged to the actual zero-extended variation,
not to an assumed component count.  The cell has one asymmetric cutoff
on each sign, and discrete Abel summation charges the strict block
endpoints.  Passing to any ordered divisibility subsequence can only
decrease this variation.

### 3.2 Exact all-\(d\) recombination

Define

\[
 \mathscr S_N(j)=
 \sum_{x\bmod4N}
 {\bf1}_{N\mid x^2-j}
 \chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{156.A9}
\]

The exact quotient selector, the partition \(d=(h,N)\), and the complete
even quadratic Gauss sum give

\[
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c),
 \qquad c=\frac{4N}{d}.
\tag{156.A10}
\]

Thus

\[
 \mathcal Z_U(V)=
 \frac1{4N}\sum_{V<|j|\le2V}A_j\mathscr S_N(j).
\tag{156.A11}
\]

The physical identity

\[
 \mathscr S_N(j)=
 \rho_{4N}(j+N)-\rho_{4N}(j+3N)
\tag{156.A12}
\]

is an independent root-count check of all odd and two-adic strata.

### 3.3 Signed interval theorem

For

\[
 \widetilde{\mathscr S}_N(h)=
 \sum_{j\bmod4N}\mathscr S_N(j)e_{4N}(hj),
\tag{156.A13}
\]

finite orthogonality gives zero at even \(h\), while for odd \(h\)

\[
 \left|\widetilde{\mathscr S}_N(h)\right|
 =2\sqrt{8N(h,N)}.
\tag{156.A14}
\]

Finite Fourier inversion and a geometric-series bound therefore imply

\[
 \sup_{\substack{I\ {\rm consecutive}\\|I|\le4N}}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll \sqrt N\,\tau(N)\log(2N).
\tag{156.A15}
\]

Combining (156.A8), (156.A11), and (156.A15) by Abel summation separately
on both signs yields

\[
 \frac1{4N}\cdot
 K M^{-3/4}X^\varepsilon\cdot
 \sqrt N X^\varepsilon
 \ll M^{-1/4}X^\varepsilon,
\tag{156.A16}
\]

which proves (156.A2).

The statement-only report supplies an independent fixed-\(d\) check:

\[
 \sup_{I\ {\rm consecutive}}
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c).
\tag{156.A17}
\]

It follows directly by opening the nonzero unit frequencies and summing
finite geometric series.  Restoring the original \(d\)-sum gives the
same \(M^{-1/4}\) bound, so the theorem does not rely on cancellation
between different divisor strata.

## 4. First doubtful or unproved step

There is no unproved step in the frozen zero-row theorem under the
accepted Round-154 profile hypotheses.  The initial source report's
progression-variation seam is superseded: (156.A8) and contraction under
ordered subsequences prove it internally.

The first open object is

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c),
\tag{156.A18}
\]

with the actual coupled coefficient, every fold, complementary
frequency, sign, and endpoint.  Neither zero-row interval theorem
controls this matrix.

## 5. Terminal review gate and controls

Three terminal reviews are GREEN.

- The independent mathematics review line-checks both primitive
  conductors, every odd and two-adic local factor, the principal branch,
  all-\(d\) recombination, root identity, Fourier coefficients, interval
  bound, literal variation, and final normalization.
- The independent source and legal-method review verifies the
  fundamental-discriminant and Gauss phases, induced-character formula,
  Ramanujan branch, direct two-adic values, and optional
  Pólya--Vinogradov fallback.  It also confirms that both promoted
  closures are elementary and that the initial source no-match is
  superseded for \(v=0\).
- The hostile profile and endpoint review verifies monotone
  zero-extended sampling, component-independent variation, physical
  support, exact phase derivative, asymmetric signed cell endpoints,
  strict-mask endpoints, subsequence contraction, external factor, and
  the complete \(d\)-power ledger.

All required controls are GREEN.  No numerical experiment or numerical
certification was used.

## 6. Dependencies and exact artifacts

The accepted kernel depends on the Round-154 literal ambient profile and
the Round-155 normalized theta completion.  Its direct evidence is:

- zero_mode_local_factor_attack.md;
- blind_zero_mode_character_rederivation.md;
- zero_mode_character_source_audit.md;
- conductor_round156_zero_mode_target.md;
- conductor_round156_zero_mode_adjudication.md;
- independent_recombination_math_round156.md;
- independent_source_round156_final.md; and
- hostile_profile_endpoint_round156_final.md.

The source cards in the initial and terminal source audits corroborate
the exact character apparatus; neither elementary target proof needs an
external asymptotic theorem.  No subagent edited the proof graph, proof
draft, validation matrix, synthesis, State Patch, or campaign state.

## 7. Recommended state effect

Apply a State Patch that:

1. creates a route-scoped proved-internal theta zero-row lemma containing
   (156.A2)--(156.A17);
2. updates the D=1 outer-defect frontier so only the incomplete nonzero
   matrix or equivalent selected cross-fibre theorem remains at this
   interface;
3. records the exact induced-character and local-factor arithmetic while
   treating the initial strict source range as superseded by the full
   elementary theorem;
4. rejects the absolute \(M^{1/4}\) zero-mode capacity as an unavoidable
   loss, arbitrary-weight countermodels as objections to the literal
   profile, and any transfer of the zero-row theorem to nonzero or
   broader owners; and
5. leaves the logarithmic collar as the last proved range for the
   complete D=1 wave, the boundary \(M^{449}\asymp R^{780}\), every other
   M1 and M2 owner, endpoint uniformity, M9, the bridge, the quarter
   target, the internal exponent \(1/3\), and the audited external
   Li--Yang exponent unchanged.

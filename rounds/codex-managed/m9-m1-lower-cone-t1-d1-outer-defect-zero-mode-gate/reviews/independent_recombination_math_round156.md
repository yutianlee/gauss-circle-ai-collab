# Round 156 independent terminal recombination mathematics review

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate`
- Role: independent terminal mathematics reviewer
- Round: 156
- Starting graph SHA-256: `f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6`
- Scope: exact character conductors and local factors; the all-odd-\(d\) recombination; the root and Fourier formulas; the interval estimate; the literal coefficient variation; and the restored zero-row power ledger

## 1. Result

The Round-156 zero-row theorem is mathematically correct in the frozen
normalization.  In particular, for

\[
 q=4N,\qquad c=4N/d,\qquad
 M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM},
\]

the literal row

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt c\,\widehat B_j(0)K(0,-j;c)
\]

is

\[
 O_{\varepsilon,A}\!\left(M^{-1/4}X^\varepsilon\right).
\]

The exact recombination (156.R6)--(156.R7), rather than only the
fixed-\(d\) character estimate in the conductor candidate, supplies a
particularly clean proof.  I find no phase, sign, factor-two, conductor,
support, endpoint, normalization, or circularity defect.  The theorem is
strictly confined to the \(v=0\) row; the nonzero theta matrix remains
open.

## 2. Exact statement and hypotheses audited

I audited arbitrary \(N\), every odd \(d\mid N\), and the full modulus
\(c=4N/d\), including its complete two-part.  The coefficient used in the
argument is the ambient pre-linearization coefficient

\[
 B_j(x)={\bf1}_{x\ge1}{\bf1}_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\]

with its literal zero extension, actual components and transitions, strict
dyadic mask, asymmetric cell, both signs, and hard endpoints.  The only
profile input is

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
\]

together with the inherited physical support on \(x\asymp K\), of total
integer length \(O(KX^\varepsilon)\) and shorter than one modulus.  This is
exactly the Round-154/155 ambient coefficient; the selected-only
linearization \(e(-j/(2x))\) is never used.

The external \(B_{1,U}(1)=O_\varepsilon(X^\varepsilon)\) is correctly left
outside the row and is absorbed only after the zero-row estimate, with the
usual reallocation of \(\varepsilon\).  No parity, squarefree, primitivity,
or coprimality hypothesis has been added.  The lower bound on \(V\) is not
used by this isolated zero-mode proof; \(V\le K\) is the relevant endpoint
hypothesis.

## 3. Proof and line audit

### 3.1 Conductors, induced transforms, and all local factors

Let \(m=N/d\), let

\[
 r=\prod_{v_p(m)\ \mathrm{odd}}p,
\]

including \(p=2\), and put

\[
 D_\sigma=\begin{cases}
 \sigma r,&\sigma r\equiv1\pmod4,\\
 4\sigma r,&\sigma r\not\equiv1\pmod4.
 \end{cases}
\]

The identities

\[
 \epsilon_a=\frac{1+i}{2}+\frac{1-i}{2}\chi_4(a),\qquad
 \left(\frac{4m}{a}\right)=\left(\frac r a\right),\qquad
 \chi_4(a)\left(\frac r a\right)=\left(\frac{-r}{a}\right)
\]

show that the two pieces are precisely the primitive quadratic characters
\(\chi_{D_\sigma}\), induced to modulus \(4m\).  If \(s=v_2(m)\) is even,
\(r\) is odd and, with \(\eta=\chi_4(r)\), the \(\sigma=\eta\) piece is
principal at two while the other has local character \(\chi_4\) of
conductor four.  If \(s\) is odd and \(r=2r_o\), both conductors have
two-part eight and the local characters are
\(\chi_{8\sigma\chi_4(r_o)}\).  The only globally principal constituent is
\(r=1,\sigma=+1\), of conductor one.  These are exactly the conductor
claims in (156.R18)--(156.R19) and (156.CT13)--(156.CT15).

For a primitive \(\psi\) of conductor \(f\mid Q\), \(L=Q/f\), the
inclusion-exclusion identity (156.R21) is exact.  Its factor
\(\overline\psi(-je/L)\) both keeps the negative additive phase and forces
the exact valuation at primes already in the conductor; the divisors of
\(R_f\) supply the two Ramanujan strata at primes absent from the
conductor.  There is no illicit use of \(|\tau(\psi)|=\sqrt f\) in the
conductor-one case.

At an odd \(p^e\Vert m\), direct lifting gives exactly (156.R24): for odd
\(e\), support is \(v_p(j)=e-1\) and the factor is

\[
 p^{e-1}\left(\frac{-u}{p}\right)\epsilon_p\sqrt p;
\]

for even \(e\), the three values are \(0,-p^{e-1},\varphi(p^e)\) on
\(v_p(j)\le e-2\), \(v_p(j)=e-1\), and \(v_p(j)\ge e\), respectively.
The CRT inverse \(u_p\) changes the unit phase but not these valuations.

At two, with \(\nu=s+2\), the principal Ramanujan row (156.R26), the
conductor-four row (156.R27), and both conductor-eight rows
(156.R28)--(156.R29) have the correct induced multiplicities and negative
additive phases.  For even \(s\), the two supports are disjoint and
(156.R30) has magnitude \(2^{s+1/2}\) on each surviving stratum.  For odd
\(s\), the two conductor-eight rows cancel on half the units and combine to

\[
 2^{s-1}\sqrt8\,\chi_8(u)(1+i\eta)
 {\bf1}_{\chi_4(u)=-\eta},
\]

equivalently
\(v_2(j)=s-1\) and
\(\chi_4(j/2^{s-1})=-1\), with magnitude \(2^{s+1}\).  Thus
(156.R30)--(156.R35) retain the squareful shells, the perfect-square
principal degeneration, and the exact half-support; no local capacity is
used as signed information.

### 3.2 Recombination, root formula, and Fourier coefficients

The selector expansion

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e_{4N}(ht)
\]

has the correct sign: its finite Fourier coefficient is
\(-2i\chi_4(h)\) for odd \(h\).  Writing \(d=(h,N)\), \(h=da\), partitions
all odd frequencies bijectively, even when \(d\) and \(N/d\) are not
coprime.  The \(x\)-sum has \(d\) identical copies and

\[
 \sum_{x\bmod c}e_c(ax^2)
 =(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c.
\]

Since \(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), the product has exactly the
phase and coefficient in (156.R6).  The remaining Fourier normalization is
\(q^{-1}=(4N)^{-1}\), giving (156.R7).  No \(d\), \(\sqrt c\), or factor
two is missing.

Formula (156.R39) is also exact: quotient classes one and three modulo
four are respectively the congruences
\(x^2\equiv j+N\pmod{4N}\) and
\(x^2\equiv j+3N\pmod{4N}\).  CRT then gives (156.R40).  The odd
prime-power root formula (156.R41) and the two-adic values
(156.R42), including the zero target \(2^{\lfloor e/2\rfloor}\), contain
the correct lifting multiplicities.  The odd-\(N\) specialization
(156.R43) has the correct \(2\chi_4(N)\) sign.

With the convention
\(\widetilde{\mathscr S}_N(h)=\sum_j\mathscr S_N(j)e_q(hj)\), the change
\(t=x^2-j\) gives (156.R45) with the minus sign in the four-term factor.
For odd \(h\), its factors are

\[
 -2i\chi_4(h),\qquad
 d(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c,
\]

so (156.R47),
\(|\widetilde{\mathscr S}_N(h)|=2\sqrt{2q(h,N)}\), is correct; even
frequencies and the zero coefficient vanish.  Fourier inversion contributes
\(1/q\).  Pairing \(h\) with \(q-h\), applying the exact geometric-sum
bound, and majorizing
\(\sqrt{(h,N)}\) by its divisor expansion gives

\[
 \sqrt q\sum_{1\le h\le q/2}\frac{(h,N)^{1/2}}h
 \ll \sqrt N\,\tau(N)\log(2N).
\]

This proves (156.R48) uniformly for every consecutive interval of length at
most \(q\).  The proof is a new signed finite-Fourier bound after exact
\(d\)-recombination; it neither invokes termwise DFI nor assumes the desired
weighted estimate.  Hence there is no circular self-return.

### 3.3 Literal variation and the final ledger

For each fixed physical \(x\), \((x^2-j)/N\) is monotone, so composition
with the zero-extended profile costs at most its actual total variation.
The residual phase is used exactly, and

\[
 \left|\frac{d}{dj}(\sqrt{x^2-j}-x)\right|
 =\frac1{2\sqrt{x^2-j}}\ll K^{-1}
\]

on the inherited support.  A signed block has length \(O(V)\le O(K)\),
so the phase variation is \(O(1)\).  The asymmetric cell has at most two
jumps for fixed \(x\); profile and strict-mask endpoints are charged by
zero extension.  Product variation therefore costs
\(O(M^{-3/4}X^\varepsilon)\) per \(x\), and summing the
\(O(KX^\varepsilon)\) supported representatives gives (156.R9).  The
positive and negative blocks are treated separately, so the jump across
the omitted central interval is never silently crossed.

Abel summation using (156.R7)--(156.R9) now has the complete power ledger

\[
 (4N)^{-1}\cdot
 (\sqrt N\,X^\varepsilon)\cdot
 (K M^{-3/4}X^\varepsilon)
 \ll M^{-1/4}X^\varepsilon.
\]

This agrees with the independent fixed-\(d\) route in
(156.CT18)--(156.CT23) and with the blind report's elementary
\(c\log(2c)\) cross-control.  The blind argument was not used in place of
the all-\(d\) recombination audit above.  There is no residual \(N\),
\(V\), \(d\), conductor, support, or endpoint power.

## 4. First doubtful or unproved step

There is no doubtful or unproved step inside the frozen zero-row theorem
once the already accepted Round-154 profile norm and physical-support
statement are taken as hypotheses.  Those inherited hypotheses, especially
the fixed-constant meaning of \(x\asymp K\) and the zero-extended variation,
are the first external seam; Round 156 does not attempt to reprove their
construction.

The first genuinely open mathematical term after this theorem is the
nonzero-frequency matrix with
\(\widehat B_j(2dv)K(-v^2,-j;4N/d)\).  Nothing in the recombined root
sequence or its zero-frequency Fourier estimate controls that jointly
dependent coefficient.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| conductor-one/perfect-square case | PASS.  The \(D=1\) constituent is a Ramanujan sum, while the second constituent has conductor four; even-exponent odd primes retain both Ramanujan strata. |
| odd prime powers and CRT phases | PASS.  Exact valuation \(e-1\) for odd \(e\), both even-\(e\) strata, negative additive phase, and CRT inverse units are all present. |
| full two-adic factor | PASS.  Conductors \(1,4,8\), induced powers, disjoint even-\(s\) supports, and odd-\(s\) half-support cancellation all agree. |
| all-\(d\) recombination | PASS.  The gcd partition, \(d\) copies of the Gauss sum, \(d\sqrt c\), phase, and remaining \(1/q\) are exact. |
| root/Fourier/interval formulas | PASS.  (156.R39) and (156.R45)--(156.R48) have the correct signs, root multiplicities, zero mode, Fourier normalization, and harmonic gcd sum. |
| literal coefficient variation | PASS.  Actual profile variation, unlinearized phase, cell and mask jumps, both signed blocks, and endpoints are charged before Abel summation. |
| false unsigned/adversarial analogue | PASS.  The proof uses signed arithmetic partial sums and actual coefficient BV; replacing either by absolute values restores the known \(M^{1/4}\) top capacity. |
| downstream scope | PASS.  No nonzero mode, broader owner, endpoint assembly, M9 theorem, bridge, target, or exponent is claimed. |

## 6. Dependencies and exact artifacts used

I read and audited `protocol.md`, the Round-156 barrier packet, both
Round-156 reports, the conductor target candidate, the active campaign,
and the cited Round-154 and Round-155 conductor adjudications needed to
recover the exact ambient coefficient and normalization.  The authoritative
proof-state entries were consulted only for owner and rejected-inference
scope.  No web theorem is needed for the recombined proof: the character
and quadratic Gauss identities, CRT, finite Fourier inversion, a geometric
sum, and discrete Abel summation are derived in the audited normalization.

I made no change to a report, candidate, proof graph, proof draft,
validation matrix, synthesis, campaign state, or other shared artifact.

## 7. Recommended state effect and terminal verdict

Promote the complete \(v=0\) row, route-scoped, with the stronger estimate
\(M^{-1/4}X^\varepsilon\).  The promoted kernel may include the exact
two-character/induced-modulus formulas, local tables, recombination
(156.R6)--(156.R7), root identity (156.R39), interval theorem
(156.R45)--(156.R48), and literal BV seam (156.R9).  Delete only the zero
row from the missing inputs and retain the incomplete nonzero matrix as the
first open interface.  Make no broader proof-state or exponent change.

**GREEN.  First defect: none in the audited zero-row theorem; the first
unproved object is the nonzero-frequency matrix, which lies outside this
claim.**

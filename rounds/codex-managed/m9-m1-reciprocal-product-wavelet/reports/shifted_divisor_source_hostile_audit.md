# Hostile and primary-source audit of the reciprocal product wavelet

- Campaign: `m9-m1-reciprocal-product-wavelet`
- Round: 64
- Task: `shifted_divisor_source_hostile_audit`
- Role: hostile seam and primary-source reviewer
- Graph SHA-256 at launch: `93d7a94cc146953fcad68bcc56ea1a1a0f10a9ae3fedd9c2238be590d7b029ff`
- Isolation: no other Round-64 report was read

## 1. Result

### Exact reduction, exact self-return, and a scoped source no-go

The corrected interior identity, with
\(\Xi\in C_c^\infty((0,1))\), is algebraically exact.  If

\[
 T=\sqrt{X/N},\qquad H_j=\frac{j}{2T},\qquad
 g(t)={\bf 1}_{t>0}\frac{V(t^2)}t,\qquad K=\widehat g,
\]

then

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{j\geq1}\chi _4(j)\Xi(j/\sqrt X)
   \sum_{m\in\mathbb Z}K\!\left(\frac{jm-X}{2T}\right).
 \tag{1.1}
\]

All algebraic moments of \(K\) do vanish.  This fact does **not**
annihilate exact products: normally

\[
 K(0)=\int_0^\infty \frac{V(t^2)}t\,dt
      =\frac12\int_0^\infty V(u)\frac{du}{u}\ne0.
 \tag{1.2}
\]

More decisively, Poisson summation applied back to the inner \(m\)-sum
returns exactly the original reciprocal cone, including its phase, sign,
and measure.  Thus a proof based only on the zero moments followed by
Poisson/Voronoi transformation is circular at this interface.  The zero
moment removes the continuum zero mode; the surviving nonzero modes are
precisely the original \(h\)-sum.

Grouping by the product gives the exact restricted divisor coefficient

\[
 A_{X,\Xi}(n)=\sum_{j\mid n}\chi _4(j)\Xi(j/\sqrt X),\qquad n>0,
 \tag{1.3}
\]

and, apart from rapidly decreasing zero- and negative-product terms,

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\geq1}A_{X,\Xi}(n)
 K\!\left(\frac{n-X}{2T}\right).
 \tag{1.4}
\]

The absolute capacity of (1.4) is \(O_{\varepsilon,V,\Xi}
(TX^\varepsilon)\), not \(O(\sqrt X)\): Poisson in \(h\) has already
supplied a factor \(\sqrt N\).  The remaining saving required for the
target is

\[
 \frac{T}{X^{1/4}}=X^{1/4-\nu/2}.
 \tag{1.5}
\]

At \(D=\sqrt X\), \(L=D/T=\sqrt N\), and
\(H=DX^{-1/4}=X^{1/4}\), this is exactly the accepted PSC deficit
\(H/L\).  The central product wavelet is therefore a special, separable
nearest-product correlation at the accepted PSC scale.  It is not
literally the accepted PSC statement: its kernel is \(K((n-X)/(2T))\),
its divisor profile is \(\Xi(j/\sqrt X)\), and it owns only the positive
interior stationary bulk, whereas PSC retains the actual two-sided odd
Vaaler kernel, both shifted fibers, and the hard profile.  A bound for one
fixed \((V,\Xi)\) would not by itself prove PSC or the full Round-63 cone.

No audited primary theorem supplies (1.5).  Standard shifted-convolution
theorems have an additive relation and complete automorphic coefficients;
Kloosterman-fraction theorems require modular inverses; and Voronoi
theorems are transformations for complete coefficients, not estimates
for the moving angular truncation (1.3).  Completing the angular divisor
sum to \(r_2(n)/4\) produces a zero-mean local wavelet of the circle
discrepancy, i.e. a Hardy/Voronoi return, not an easier imported bound.

Consequently Round 64 proves no radial interval and no exponent.  The
promotable content is the exact product regrouping, the inverse-Poisson
self-return, the exact PSC scale comparison, and the scoped literature
obstruction.

## 2. Exact statement and hypotheses

Assume \(X>1\), \(N=X^\nu\) with fixed \(0<\nu\leq2/5\),
\(V\in C_c^\infty((0,\infty))\), and
\(\Xi\in C_c^\infty((0,1))\).  Choose constants

\[
 0<\alpha<\beta<1,
 \qquad \operatorname{supp}\Xi\subset[\alpha,\beta].
 \tag{2.1}
\]

Use \(e(t)=e^{2\pi it}\) and the Fourier convention
\(\widehat f(\xi)=\int_{\mathbb R}f(t)e(-\xi t)\,dt\).

### 2.1 Exact Poisson and moment lemma

With \(g,K,H_j\) as in Section 1,

\[
 \frac1hV\!\left(\frac{4Xh^2}{j^2N}\right)
 =\frac1{H_j}g(h/H_j),
 \tag{2.2}
\]

and (1.1) holds exactly.  Moreover, for every integer \(r\geq0\),

\[
 \int_{\mathbb R}\xi^rK(\xi)\,d\xi=0.
 \tag{2.3}
\]

The integrals in (2.3) are absolutely convergent.  They say nothing
pointwise about \(K(0)\), which is given by (1.2).

### 2.2 Product grouping, exceptional products, and capacity

Put

\[
 C_{X,\Xi}=\sum_{j\geq1}\chi _4(j)\Xi(j/\sqrt X).
\]

Then the fully exact regrouping is

\[
 \begin{aligned}
 \mathcal R_{X,N}[V,\Xi]
 &=K\!\left(-\frac{X}{2T}\right)C_{X,\Xi}\\
 &\quad+\sum_{n\in\mathbb Z\setminus\{0\}}
 K\!\left(\frac{n-X}{2T}\right)
 \sum_{j\mid |n|}\chi _4(j)\Xi(j/\sqrt X).
 \end{aligned}
 \tag{2.4}
\]

For every \(B>0\), the \(n\leq0\) part is \(O_{B,V,\Xi,\nu}(X^{-B})\)
after increasing the Schwartz exponent.  The positive part satisfies

\[
 \sum_{n\geq1}|A_{X,\Xi}(n)|
 \left|K\!\left(\frac{n-X}{2T}\right)\right|
 \ll_{\varepsilon,V,\Xi}TX^\varepsilon.
 \tag{2.5}
\]

If \(X\in\mathbb Z\), the exact-product fiber is

\[
 K(0)\sum_{j\mid X}\chi _4(j)\Xi(j/\sqrt X),
 \tag{2.6}
\]

which is \(O_{\varepsilon,V,\Xi}(X^\varepsilon)\), hence target-safe,
but is not identically zero.

### 2.3 Exact inverse-Poisson self-return

For every \(j\) in the support of \(\Xi(j/\sqrt X)\),

\[
 \boxed{
 \sum_{m\in\mathbb Z}K\!\left(\frac{jm-X}{2T}\right)
 =\frac{2T}{j}\sum_{h\geq1}
 g\!\left(\frac{2Th}{j}\right)e(Xh/j).}
 \tag{2.7}
\]

Inserting (2.7) into (1.1) is exactly (64.1), since
\(2T/j=1/H_j\).  The \(h=0\) mode is absent because \(g\) vanishes in
a neighborhood of zero.  This is the precise content, and the precise
limit, of the all-moment cancellation.

### 2.4 Nearest-product/PSC scale

Fix \(0<\eta<\nu/2\).  Truncating (1.4) to
\(|n-X|\leq TX^\eta\) costs \(O_B(X^{-B})\) for arbitrary \(B\), after
choosing a sufficiently high Schwartz seminorm.  On this central range,

\[
 \frac{|n-X|}{j}\ll X^{\eta-\nu/2}=o(1),
\]

so \(m\) is the uniquely specified nearest integer to \(X/j\).  Thus
the central product-wavelet sum is exactly a nearest-product sum at

\[
 D=\sqrt X,\qquad U=T,\qquad L=D/U=\sqrt N,
 \qquad H=DX^{-1/4}=X^{1/4}.
 \tag{2.8}
\]

Its trivial scale is \(U=T\), its target scale is \(X^{1/4}\), and the
missing factor is \(H/L\), as in (1.5).

### 2.5 Scope of the interior cutoff

Condition (2.1) gives a fixed separation from the saddle/lower-boundary
collision \(j=\sqrt X\) and also restricts to \(j\asymp\sqrt X\), hence
\(h\asymp\sqrt N\).  It does not cover:

1. the sharp owner \(j\leq\sqrt X\) near \(j=\sqrt X\);
2. the scales \(j/\sqrt X\to0\), down to \(j\asymp T\);
3. the stationary entry/exit and half-saddle transition;
4. the negative-frequency nonstationary integrals;
5. the exact subtraction which makes the character-Poisson remainder
   absolutely convergent.

Therefore an estimate uniform for one fixed \(\Xi\) does not imply the
full Round-63 cone estimate.

## 3. Proof, derivation, and primary-source audit

### 3.1 Poisson normalization and sign

For fixed \(j\), define

\[
 F_j(x)=H_j^{-1}g(x/H_j)e(Xx/j).
\]

The support of \(g\) is a compact subset of \((0,\infty)\), so
\(\sum_{h\in\mathbb Z}F_j(h)=\sum_{h\geq1}F_j(h)\).  A change of
variables gives

\[
 \widehat F_j(m)
 =\widehat g\!\left(H_j(m-X/j)\right)
 =K\!\left(\frac{jm-X}{2T}\right).
\]

Poisson summation proves (1.1), with no boundary term and with the sign
shown.  Fourier inversion gives

\[
 g^{(r)}(0)=\int_{\mathbb R}(2\pi i\xi)^rK(\xi)\,d\xi.
\]

Every derivative of \(g\) at zero vanishes, proving (2.3).  In contrast,
Fourier evaluation at zero gives (1.2); confusing these two statements is
the first hostile failure mode.

For the inverse identity, let \(a=j/(2T)\), \(b=X/(2T)\), and
\(G(x)=K(ax-b)\).  Then

\[
 \widehat G(k)=a^{-1}e(-kX/j)\widehat K(k/a)
 =a^{-1}e(-kX/j)g(-k/a).
\]

Only \(k=-h<0\) survives, and (2.7) follows.  Hence all-moment
Euler--Maclaurin or Poisson arguments have removed only the continuous
mode and have reconstructed the original reciprocal oscillation exactly.

### 3.2 Product algebra and exact products

Because \(\Xi(j/\sqrt X)\) restricts \(j\) to a finite interval, grouping
the absolutely convergent Schwartz sum by \(n=jm\) is legitimate.  For
\(n\ne0\), the possible \(j\)'s are exactly the positive divisors of
\(|n|\); for \(n=0\), every supported \(j\) occurs with \(m=0\).  This
proves (2.4).

The divisor bound and Schwartz decay give

\[
 \sum_{n\asymp X}\tau(n)
 \left(1+\frac{|n-X|}{T}\right)^{-A}
 \ll_\varepsilon TX^\varepsilon,
\]

and the remote tails are smaller after increasing \(A\), proving (2.5).
The same decay, together with \(j\asymp\sqrt X\), makes \(m\leq0\)
rapidly negligible.  Formula (2.6) follows by taking \(n=X\).  It is
divisor-bounded but generally nonzero.

The smooth cutoff can harmlessly be moved from \(j/\sqrt X\) to
\(j/\sqrt n\) in the central product sum.  Indeed

\[
 \left|\Xi(j/\sqrt X)-\Xi(j/\sqrt n)\right|
 \ll_{\Xi}\frac{|n-X|}{X},
\]

and the absolute commutator is

\[
 \ll_\varepsilon X^\varepsilon
 \sum_n\frac{|n-X|}{X}
 \left|K\!\left(\frac{n-X}{2T}\right)\right|
 \ll_\varepsilon \frac{T^2}{X}X^\varepsilon
 =N^{-1}X^\varepsilon.
 \tag{3.1}
\]

This useful smooth commutator does not apply to the sharp top owner
\({\bf1}_{j\leq\sqrt X}\); divisors crossing that boundary are exactly
where the saddle meets the original lower endpoint.

### 3.3 PSC and Hardy return maps

The nearest-product claim after (2.8) follows from
\(TX^\eta/j\ll X^{\eta-\nu/2}\).  Comparing with the accepted PSC
parameters gives

\[
 \frac{H}{L}=\frac{X^{1/4}}{\sqrt N}
 =\frac{T}{X^{1/4}}.
\]

Thus the new coordinates expose exactly the already accepted missing
power.  They do improve the naive absolute capacity from \(\sqrt X\) to
\(T\), but they do not cross the target line for any
\(0<\nu\leq2/5\).  At the endpoint \(\nu=2/5\), the remaining deficit is
\(X^{1/20}\).

If one replaces the angular coefficient (1.3) by the complete divisor
coefficient, then

\[
 \sum_{j\mid n}\chi _4(j)=\frac{r_2(n)}4.
\]

Writing \(P(u)=\sum_{n\leq u}r_2(n)-\pi u\), the corresponding complete
wavelet satisfies, up to a rapidly decreasing lower-bound tail,

\[
 \frac14\sum_{n\geq1}r_2(n)K\!\left(\frac{n-X}{2T}\right)
 =-\frac1{8T}\int_0^\infty
 P(u)K'\!\left(\frac{u-X}{2T}\right)\,du.
 \tag{3.2}
\]

The area term vanishes because \(\int K=0\).  The conjectural circle
bound immediately makes (3.2) \(O(X^{1/4+\varepsilon})\); no known
unconditional estimate gives that target.  A single fixed wavelet bound
does not conversely imply the full pointwise circle conjecture, so the
logical claim is a scoped Hardy/Voronoi return, not an equivalence theorem
for one \(K\).  Also, the present \(\Xi\)-truncated coefficient cannot be
replaced by the complete one: the missing divisor angles are not zero and
are precisely the one-sided-cone obstruction already recorded in the
graph.

### 3.4 Blomer--Harcos shifted convolution: hypotheses fail

Blomer and Harcos, *The spectral decomposition of shifted convolution
sums*, arXiv:math/0703246v2, Theorem 1 and equation (5), treat

\[
 \sum_{m\pm n=h}\lambda_{\pi_1}(|m|)\lambda_{\pi_2}(|n|)
 W_1(m/Y)W_2(n/Y)
\]

for two **cuspidal** automorphic representations of
\(\mathrm{PGL}_2(\mathbb R)\), an additive equation \(m\pm n=h\), and
separate weights with specified high Sobolev norms.  Their pointwise
bound is \(h^{7/64}Y^{1/2}(hY)^\varepsilon\), and their main novelty is
an exact spectral decomposition useful after averaging the shift.

The present condition is multiplicative, \(jm=n\), followed by a moving
window \(|n-X|\lesssim T\).  Its coefficient is an incomplete Eisenstein
divisor coefficient with an \(X\)-dependent angular cutoff, not a product
of two cusp-form coefficient sequences.  There is no fixed additive shift
and no matching pair of separable additive variables.  The theorem is not
applicable.

Primary source:
[Blomer--Harcos 2007](https://arxiv.org/pdf/math/0703246).

### 3.5 Cowan's twisted additive divisor theorem: hypotheses fail

Cowan, *A twisted additive divisor problem*, arXiv:2304.12572v1,
Theorem 1.1, assumes a prime level, two even nontrivial characters
\(\chi,\psi\) with \(\chi\psi\) nontrivial, nonzero complex
\(u,v\), a fixed positive additive shift \(k\), and the two complete
coefficients

\[
 \sigma_{2u}(n,\chi)\sigma_{2v}(n-k,\psi)n^{-u-v}.
\]

All parameters other than the summation limit are fixed in the stated
asymptotic.  Here \(\chi_4\) is odd and has modulus four, there is only
one incomplete divisor coefficient, the natural exponent is zero, and
both the angular cutoff and the short window move with \(X\).  None of
the decisive conductor, parity, completeness, or additive-shift
hypotheses matches.

Primary source:
[Cowan 2023, Theorem 1.1](https://arxiv.org/pdf/2304.12572).

### 3.6 Voronoi/Kuznetsov: an identity is available only after completion

Mellin inversion does give the formal coefficient-preserving separation

\[
 A_{X,\Xi}(n)=\frac1{2\pi i}\int_{(0)}
 \widetilde\Xi(s)X^{s/2}\sigma_{-s}(n,\chi_4)\,ds.
 \tag{3.3}
\]

Thus complete twisted-divisor Voronoi technology is structurally
relevant.  Kıral--Zhou, *The Voronoi formula and double Dirichlet series*,
Theorem 1.3, however, is an exact transform under Hecke relations,
moderate coefficient growth, and functional equations for every required
primitive twist.  It applies to complete coefficients attached to an
L-function (including specified isobaric/Eisenstein examples), not
directly to the moving incomplete coefficient (1.3).  Using (3.3) would
also require a ramified level-four formula, uniform control in the Mellin
height \(\Im s\), every gamma and polar term, and integration against
\(\widetilde\Xi(s)\).  The cited theorem supplies a transformation, not a
target-sized estimate.  In the present normalization, transforming back
without a new spectral cancellation theorem is the self-return (2.7) or,
after full angular completion, the circle wavelet (3.2).

Primary source:
[Kıral--Zhou 2015, Theorem 1.3](https://ekiral.github.io/uncut.pdf).

### 3.7 Reciprocal/Kloosterman-fraction theorems: phase hypotheses fail

Bettin--Chandee, *Trilinear forms with Kloosterman fractions*,
arXiv:1502.00769, Theorem 1, estimates dyadic trilinear forms with
arbitrary \(\ell^2\) coefficients and phase

\[
 e\!\left(\vartheta a\overline m/n\right),\qquad (m,n)=1,
\]

where \(\overline m\) is a modular inverse.  Its smooth perturbation
remark retains that modular-inverse main phase and its coprimality and
three-variable structure.  The phase \(e(Xh/j)\) is an ordinary real
quotient; \(X\) need not be an integer, there is no modular inverse or
coprimality condition, and the product wavelet couples \(j,m\) through a
moving hyperbola.  No specialization of the stated theorem gives (64.2).

The accepted Tao--Trudgian--Yang exponent-pair theorem does apply to
one-dimensional reciprocal model sums after splitting \(\chi_4\) into
residue classes and transferring fixed BV weights.  Estimating each
\(h\)-row separately is precisely the already audited exponent-pair
wedge; it does not provide the collective \((h,j)\) or \((j,m)\)
cancellation (1.5).

Primary sources:
[Bettin--Chandee 2015, Theorem 1](https://arxiv.org/abs/1502.00769) and
[Tao--Trudgian--Yang 2025](https://arxiv.org/abs/2501.16779).

## 4. First doubtful or unproved step

All algebraic identities (1.1)--(2.7), the moment statement, the product
grouping, the smooth cutoff commutator, and the PSC scale ledger are
proved above.  The first unproved analytic step is

\[
 \left|\sum_{n\geq1}A_{X,\Xi}(n)
 K\!\left(\frac{n-X}{2T}\right)\right|
 \ll_{\varepsilon,V,\Xi}X^{1/4+\varepsilon},
 \tag{4.1}
\]

uniformly on any fixed nonempty interval \(0<\nu\leq2/5\).  It requires
the factor \(X^{1/4-\nu/2}\) beyond (2.5).  Neither the vanishing moments
nor any audited source provides this saving.  Inverse Poisson converts
the proposed moment argument exactly back to the reciprocal cone, and
Mellin--Voronoi conversion requires the same new signed spectral estimate.

Even a proof of (4.1) for every fixed interior \(\Xi\) would leave a
second, logically separate gap: uniform passage to the sharp
\(j\leq\sqrt X\) owner, including the \(j=\sqrt X\) half-saddle, all
lower \(j\)-scales, stationary entry/exit, negative frequencies, and the
subtraction/boundary recombination.  Therefore (4.1) alone cannot promote
the full one-sided radial estimate.

## 5. Required control tests and outcomes

1. **Poisson normalization and sign — pass.**  Direct Fourier
   calculation gives \((jm-X)/(2T)\), and inverse Poisson gives
   \(e(+Xh/j)\) with factor \(2T/j=1/H_j\).

2. **All moments versus point evaluation — mixed.**  Equation (2.3)
   passes for every \(r\), but the inference that exact products vanish
   fails because \(K(0)\) is the generally nonzero logarithmic integral
   (1.2).

3. **Negative and zero products — pass as negligible.**  The exact
   \(n=0\) owner is the first term of (2.4), not a divisor sum.  It and
   all \(n<0\) terms are rapidly decreasing because
   \(X/T=\sqrt{XN}\to\infty\).

4. **Exact products — target-safe but present.**  Formula (2.6) is
   \(O(X^\varepsilon)\), not zero.  Hence exact products do not obstruct
   the target, but they falsify any phase-gap or zero-moment deletion.

5. **Perfect fourth powers — hostile coherence survives.**  If
   \(X=Q^4\), the sharp top value \(j=\sqrt X=Q^2\) makes
   \(e(Xh/j)=1\) for every \(h\), but is deliberately excluded by
   \(\Xi\in C_c^\infty((0,1))\).  Interior exact divisors can also be
   arranged: choose an odd rational \(c=p/q\) in a nonzero interval of
   \(\Xi\), take \(Q\) divisible enough that \(j=cQ^2\) is an odd
   divisor of \(Q^4\), and then \(e(Xh/j)=1\).  This is not a lower bound
   for the complete signed sum, but it rules out generic irrationality
   and confirms that the omitted top collision is a real full-cone gate.

6. **Smooth cutoff commutator — pass.**  Moving
   \(\Xi(j/\sqrt X)\) to \(\Xi(j/\sqrt n)\) costs
   \(O(N^{-1}X^\varepsilon)\) by (3.1).  Replacing \(\Xi\) by the sharp
   cone owner does not follow from this test.

7. **PSC comparison — exact scale, nonidentical statement.**  The
   nearest-product window has \((D,L,H,U)=(\sqrt X,\sqrt N,
   X^{1/4},T)\), and its missing factor is exactly \(H/L\).  The kernel
   and endpoint ownership differ from PSC, so no implication in either
   direction is claimed without an additional representation theorem.

8. **Angular completion — fail.**  Replacing (1.3) by \(r_2(n)/4\)
   adds unowned divisor sectors.  If those sectors are added, (3.2)
   shows a circle-discrepancy/Hardy return rather than an imported bound.

9. **Entry, exit, subtraction, and full cone — fail as an implication.**
   Fixed \(\Xi\) separates the top saddle and discards the low scales.
   The Round-63 half-boundary and \(j^{-1}\) subtraction must retain
   their exact recombination (the full signed \(j^{-1}\) sum cancels the
   displayed half-boundary before the absolutely convergent remainder is
   used).  The interior bulk estimate does not own that ledger or the
   negative-frequency and half-saddle pieces.

10. **Primary-source applicability — fail for a direct import.**
    Blomer--Harcos and Cowan have additive complete shifted
    convolutions; Kıral--Zhou gives a complete-coefficient transform;
    Bettin--Chandee has modular inverses; TTY gives the already exhausted
    one-variable wedge.  None proves (4.1).

11. **Numerical allocation — pass.**  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts read:

- `AGENTS.md`;
- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/derivation_packet.md`,
  including the conductor's corrected fixed interior cutoff;
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/briefs/shifted_divisor_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md`;
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md` and its
  hostile Hardy-return source audit;
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/reports/resonance_cell_literature_hostile_audit.md`;
- the accepted Round-63 synthesis and blind character-Poisson derivation,
  used only to audit the inherited full-cone boundary/subtraction scope.

Primary sources independently inspected:

- V. Blomer and G. Harcos, *The spectral decomposition of shifted
  convolution sums*, arXiv:math/0703246v2, Theorem 1, equations (3)--(5).
- A. Cowan, *A twisted additive divisor problem*, arXiv:2304.12572v1,
  Theorem 1.1.
- E. M. Kıral and F. Zhou, *The Voronoi formula and double Dirichlet
  series*, Theorem 1.3 and Example 1.7.
- S. Bettin and V. Chandee, *Trilinear forms with Kloosterman fractions*,
  arXiv:1502.00769, Theorem 1 and its smooth-perturbation remark.
- T. Tao, T. Trudgian, and A. Yang, *New exponent pairs, zero density
  estimates, and zero additive energy estimates: a systematic approach*,
  arXiv:2501.16779, used only through its already audited reciprocal
  exponent-pair scope.

No other Round-64 report was opened.  The only file written is this
report.

## 7. Recommended state effect

1. **Promote after conductor validation** the exact product-wavelet
   identity, product regrouping (2.4), all-moment statement with the
   explicit warning \(K(0)\ne0\), and inverse-Poisson self-return (2.7).

2. **Promote as a scoped no-go** that zero moments plus a second
   Poisson/Voronoi transformation do not themselves yield cancellation:
   inverse Poisson reconstructs the reciprocal cone exactly.

3. **Record the sharpened target ledger:** product regrouping has
   absolute capacity \(TX^\varepsilon\) and still needs
   \(X^{1/4-\nu/2}=H/L\).  At \(\nu=2/5\) the missing power is
   \(X^{1/20}\).

4. **Record the PSC relation carefully:** this is a special separable
   nearest-product wavelet at the accepted critical PSC scale, not an
   exact proof of the accepted PSC statement.  Retain PSC and the signed
   reciprocal-cone estimate as open.

5. **Reject** deletion of exact products from the all-moment condition,
   replacement of the angular coefficient by \(r_2/4\), generic
   irrationality at perfect powers, and direct imports of the audited
   shifted-divisor, Voronoi, or Kloosterman-fraction theorems.

6. **Retain the full-cone gate as open:** the fixed interior cutoff does
   not own the sharp \(j=\sqrt X\) collision, lower scales, entry/exit,
   negative frequencies, or subtraction/boundary recombination.

7. Keep `M9-M1-shifted-divisor-correlation-PSC`, the Round-63 reciprocal
   cone, `M9-M1-global-angular-radial-estimate`, `M9-M1`, `M9`, and the
   Gauss-circle target open.  No exponent change is licensed.

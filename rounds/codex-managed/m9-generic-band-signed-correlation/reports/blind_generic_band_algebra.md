# Blind generic-band algebra

## 1. Result

The exact single-lift and pair-convolution formulas admit one genuine \(\chi _4\) residue law, but it is not a global cancellation identity. On a fixed pair-sum fiber, the \(\chi _4\)-product alternates only when the two denominators have different \(2\)-adic valuations. When their \(2\)-adic valuations agree—in particular when both denominators are odd—the sign is constant throughout the fiber. This sign-locking is the earliest rigorous obstruction to a universal residue pairing or orthogonality argument.

Consequently, a generic-band estimate cannot be obtained from the symmetry \(p\mapsto-p\), from swapping the two summands, or from character orthogonality applied without the exact pair equation. Those operations either preserve the sign or also hold for unsigned coefficients.

## 2. Exact statements and hypotheses

Let \(D>0\), \(H=H_D\in\mathbb Z_{\ge0}\), and let \(w_D(q)\) be the dyadic denominator weight. Extend the primitive real character modulo \(4\) to all integers by

\[
\chi _4(n)=
\begin{cases}
0,&2\mid n,\\
1,&n\equiv1\pmod4,\\
-1,&n\equiv3\pmod4.
\end{cases}
\]

For \(p\ne0\),

\[
\frac{\chi _4(|p|)}{|p|}
=\frac{\chi _4(p)}p. \tag{2.1}
\]

The right side is even in \(p\); writing instead \(\chi _4(p)/|p|\) would introduce a false oddness.

Define the reduced generic-band support

\[
\mathcal P_{D,H}
=\left\{(p,q)\in\mathbb Z\times\mathbb Z_{\ge1}:
D\le q<2D,\quad 1\le |p|\le H,\quad (p,q)=1,\quad 2\nmid p
\right\}. \tag{2.2}
\]

For \((p,q)\in\mathcal P_{D,H}\), put

\[
a_\chi(p,q)
=-\frac{w_D(q)}{\pi}
\frac{\Phi(|p|/(H+1))\chi _4(p)}p. \tag{2.3}
\]

For all other \((p,q)\), put \(a_\chi(p,q)=0\). Because reduced fractions have a unique representation with positive denominator, this defines \(A_\chi(\rho)\) for \(\rho=p/q\) by \(A_\chi(p/q)=a_\chi(p,q)\).

The pair convolution is

\[
R_\chi(r)
=\sum_{\substack{(p_1,q_1),(p_2,q_2)\in\mathcal P_{D,H}\\
p_1/q_1+p_2/q_2=r}}
a_\chi(p_1,q_1)a_\chi(p_2,q_2), \tag{2.4}
\]

or explicitly

\[
\begin{aligned}
R_\chi(r)
=\frac1{\pi^2}
\sum_{\substack{(p_1,q_1),(p_2,q_2)\in\mathcal P_{D,H}\\
p_1q_2+p_2q_1=rq_1q_2}}
&w_D(q_1)w_D(q_2)\\
{}\times&
\frac{\Phi(|p_1|/(H+1))\Phi(|p_2|/(H+1))}
{p_1p_2}\,
\chi _4(p_1)\chi _4(p_2).
\end{aligned} \tag{2.5}
\]

The equation in (2.5) means equality in \(\mathbb Q\). Equivalently, if \(r=A/B\) is reduced with \(B>0\), its constraint is

\[
B(p_1q_2+p_2q_1)=Aq_1q_2. \tag{2.6}
\]

All summands are ordered; swapping indices is already included.

If \(r=N_{12}/(q_1q_2)\) and \(s=N_{34}/(q_3q_4)\), where

\[
N_{12}=p_1q_2+p_2q_1,\qquad
N_{34}=p_3q_4+p_4q_3,
\]

then the critical off-diagonal condition is exactly

\[
0<|r-s|\le\frac{\kappa}{X}
\quad\Longleftrightarrow\quad
0<|\Delta|\le
\frac{\kappa q_1q_2q_3q_4}{X}, \tag{2.7}
\]

where the nonzero integer determinant is

\[
\Delta
=N_{12}q_3q_4-N_{34}q_1q_2. \tag{2.8}
\]

If instead \(r=A/B\) and \(s=C/E\) are individually reduced, then (2.7) is equivalently

\[
0<|AE-BC|\le\frac{\kappa BE}{X}. \tag{2.9}
\]

In particular, the left side of (2.9) is at least \(1\). Since \(B\le q_1q_2<4D^2\) and \(E<4D^2\), a necessary condition for a nonempty critical band is \(1<16\kappa D^4/X\).

## 3. Derivation and residue analysis

### 3.1 Single lift, support, and symmetry

Start from the audited formula

\[
\beta_{h,H}
=-\frac{\Phi(|h|/(H+1))\chi _4(|h|)}
{\pi|h|}\mathbf 1_{2\nmid h}.
\]

For a reduced \(p/q\) with \(D\le q<2D\), the lift condition \(gq\in[D,2D)\) forces \(g=1\): positivity forces \(g\ge1\), while \(g\ge2\) gives \(gq\ge2D\), at the excluded upper endpoint. Therefore

\[
A_\chi(p/q)=\beta_{p,H}w_D(q)=a_\chi(p,q). \tag{3.1}
\]

The coefficient is zero for even \(p\), while \(p=0\) is excluded by \(1\le|p|\). Reducedness imposes \((p,q)=1\). Once \(p\) is odd, \(q\) may be odd or even; an even \(q\) merely contributes no common factor \(2\).

Equation (2.1) turns the absolute-value source convention into the signed-\(p\) formula (2.3). It also gives

\[
a_\chi(-p,q)=a_\chi(p,q),\qquad
A_\chi(-\rho)=A_\chi(\rho). \tag{3.2}
\]

Hence the change \((p_1,p_2)\mapsto(-p_1,-p_2)\) gives

\[
R_\chi(-r)=R_\chi(r). \tag{3.3}
\]

This is an evenness identity, not cancellation. It remains true after replacing every \(\chi _4\)-factor by its absolute value.

For real \(w_D\), all coefficients and \(R_\chi\) are real. Then the sum-convolution (2.4), obtained from squaring the frequency polynomial, agrees after \(p_2\mapsto-p_2\) with the difference-convolution obtained from its modulus square. For complex \(w_D\), conjugates must be retained and this shortcut is not valid.

The support also gives

\[
|p/q|\le H/D,\qquad |r|\le2H/D. \tag{3.4}
\]

At \(r=0\), uniqueness of reduced representation implies

\[
\frac{p_1}{q_1}=-\frac{p_2}{q_2}
\quad\Longrightarrow\quad
(p_2,q_2)=(-p_1,q_1).
\]

Thus, for real weights,

\[
R_\chi(0)
=\sum_{(p,q)\in\mathcal P_{D,H}}a_\chi(p,q)^2\ge0. \tag{3.5}
\]

Here \(\chi _4(p)^2=1\), so the exact zero fiber has no signed saving at all.

### 3.2 Exact solution-line character law

Fix \(q_1,q_2\) and an integer \(N\), and consider the fiber

\[
p_1q_2+p_2q_1=N. \tag{3.6}
\]

Let

\[
d=(q_1,q_2),\qquad a=q_1/d,\qquad b=q_2/d.
\]

When a solution exists, \(d\mid N\), and all integer solutions have the form

\[
p_1=p_1^{(0)}+at,\qquad
p_2=p_2^{(0)}-bt. \tag{3.7}
\]

Suppose one solution has both \(p_i\) odd. Since \((a,b)=1\), at least one of \(a,b\) is odd, and preserving both odd parities forces \(t=2k\). The elementary identity

\[
\chi _4(n+2m)=(-1)^m\chi _4(n)
\qquad(n\ {\rm odd}) \tag{3.8}
\]

therefore gives the exact fiber law

\[
\chi _4(p_1^{(0)}+2ak)
\chi _4(p_2^{(0)}-2bk)
=\chi _4(p_1^{(0)})\chi _4(p_2^{(0)})
(-1)^{k(a+b)}. \tag{3.9}
\]

There are two cases.

- If \(a,b\) have opposite parity, equivalently \(v_2(q_1)\ne v_2(q_2)\), the product alternates with \(k\). This is a genuine \(\chi _4\) identity and becomes false for unsigned coefficients.
- If \(a,b\) are both odd, equivalently \(v_2(q_1)=v_2(q_2)\), the product is constant on the entire odd solution fiber. There is no character cancellation to exploit.

The second case includes every pair of odd denominators. There one can make the sign-locking still more explicit. With

\[
N=p_1q_2+p_2q_1
\]

even, residue checking modulo \(4\) gives

\[
\chi _4(p_1)\chi _4(p_2)
=\chi _4(q_1)\chi _4(q_2)(-1)^{N/2+1}. \tag{3.10}
\]

For fixed \(q_1,q_2,N\), the right side is constant. Thus the natural fixed-denominator, fixed-pair-sum fiber is coherent rather than cancelling.

Even in the alternating case, (3.9) is not by itself an orthogonality theorem. The range \(|p_i|\le H\) cuts out a finite, generally unpaired interval in \(k\); the reciprocal-\(\Phi\) amplitudes vary with \(k\); and the two coprimality conditions may delete an irregular subset when \(d>1\). If \(d=1\), the shifts are \(2q_1\) and \(2q_2\), so coprimality is stable, but the amplitude and endpoint problems remain.

### 3.3 Exact generic-band correlation

For real weights, the off-diagonal signed pair correlation at \(\delta=\kappa/X\) is

\[
\mathcal C_\chi^{\ne}(\delta)
=\sum_{\substack{r,s\in\mathbb Q\\0<|r-s|\le\delta}}
R_\chi(r)R_\chi(s). \tag{3.11}
\]

Expanding (2.4), it is exactly

\[
\mathcal C_\chi^{\ne}(\delta)
=\sum_{\substack{(p_i,q_i)\in\mathcal P_{D,H}\ (1\le i\le4)\\
0<|\Delta|\le\delta q_1q_2q_3q_4}}
\prod_{i=1}^4 a_\chi(p_i,q_i), \tag{3.12}
\]

with \(\Delta\) from (2.8). For complex weights the second pair in (3.11) and (3.12) must be conjugated.

No involution found from negation, swapping, or motion along a solution fiber reverses the sign while preserving every item in (3.12). Simultaneous negation sends \(\Delta\) to \(-\Delta\) but preserves each \(a_\chi\), hence adds rather than cancels. Swaps preserve both the product and \(\Delta\). Motion along a fiber has the locked sector (3.10), and in the alternating sector does not preserve the exact amplitude and admissible support.

## 4. Earliest obstruction and weakest plausible lemma

The earliest obstruction occurs before the near-band condition is used: for fixed \(q_1,q_2,N\) with \(v_2(q_1)=v_2(q_2)\), equation (3.9) makes the \(\chi _4\)-product constant on all admissible odd solutions. In particular, the all-odd denominator sector has the exact sign formula (3.10). Therefore there is no universal pointwise estimate for \(R_\chi(r)\) coming from \(\chi _4\)-orthogonality, and no global pairing can be justified without separately controlling this sign-locked sector.

The weakest plausible next lemma must split the pair convolution by \(2\)-adic denominator type:

\[
R_\chi=R_\chi^{\rm lock}+R_\chi^{\rm alt},
\]

where \(R_\chi^{\rm lock}\) has \(v_2(q_1)=v_2(q_2)\) and \(R_\chi^{\rm alt}\) has unequal valuations. It may use (3.9) and Abel summation only on \(R_\chi^{\rm alt}\). The locked term must receive a separate arithmetic incidence or large-sieve estimate for the exact determinant band (2.7), with no assumed sign saving. A minimal useful correlation statement would therefore directly bound

\[
\sum_{\substack{r,s\\0<|r-s|\le\kappa/X}}
R_\chi^\alpha(r)\overline{R_\chi^\beta(s)}
\qquad
(\alpha,\beta\in\{{\rm lock},{\rm alt}\}), \tag{4.1}
\]

after keeping the exact reciprocal-\(\Phi\) weights and coprimality restrictions, using character cancellation only when at least one relevant solution fiber is of alternating type. Any claimed bound for the lock-lock term must be proved by the rational near-incidence geometry itself. This is weaker, and more plausible, than a pointwise cancellation claim for all \(R_\chi(r)\).

The first unproved seam in such a lemma is the lock-lock estimate in (4.1). The next seam is recovering bounded-variation cancellation from (3.9) after coprimality holes and truncation endpoints in the alternating sector. Neither follows from character orthogonality alone.

## 5. Required controls

### Support and degeneracy

- **Input:** \(q=D\), \(q\uparrow2D\), \(p=0\), even \(p\), both signs of odd \(p\), \(r=0\), and \(\Delta=0\).
- **Expected invariant:** exactly one lift survives; zero/even frequencies vanish; exact pair equality is distinct from the critical off-diagonal band.
- **Outcome:** \(g=1\) is forced throughout the half-open denominator block. Equations (2.2) and (3.1) record all parity and coprimality restrictions. Equation (3.5) isolates the positive zero fiber, while (2.7) explicitly removes \(\Delta=0\).
- **Implication:** neither an upper-endpoint second lift nor an exact resonance is hidden in the generic band.

### Signed versus unsigned

- **Input:** genuine \(\chi _4\) coefficients, their absolute values, simultaneous \(p\)-negation, swaps, and the fixed-fiber parametrization (3.7).
- **Expected invariant/failure:** a genuine signed mechanism must fail for absolute coefficients.
- **Outcome:** negation and swaps survive unchanged in the unsigned model and therefore provide no signed cancellation. The alternating law (3.9) for unequal \(2\)-adic valuations genuinely disappears in the unsigned model. Conversely, the equal-valuation sector is sign-locked and behaves like an unsigned fiber up to one global sign.
- **Implication:** the only exact \(\chi _4\)-specific resource found is local alternation in the unequal-valuation sector; it cannot control the entire convolution.

### Proves-too-much

- **Input:** any proposed proof based only on \(A_\chi(-\rho)=A_\chi(\rho)\), pair exchange, or an unqualified assertion that a complete set of residues modulo \(4\) occurs.
- **Expected failure:** such a proof would also apply to unsigned coefficients or contradict a coherent exact fiber.
- **Outcome:** evenness and exchange hold unsigned, while (3.10) gives a fixed-sign all-odd fiber and (3.5) gives a nonnegative zero fiber. Coprimality and finite truncation also prevent an automatic complete residue system.
- **Implication:** these symmetries cannot certify a generic-band saving. Any future lemma must expose the unequal-\(2\)-adic alternation and explicitly pay for the locked sector.

No numerical experiment was used.

## 6. First doubtful or unproved step

All identities through (3.12) are exact. No global cancellation estimate has been proved. The first doubtful step in a putative residue-orthogonality proof is the assertion that \(\chi _4(p_1)\chi _4(p_2)\) averages to zero on every fixed pair-sum fiber; equations (3.9) and (3.10) refute it. For the split proposal (4.1), the first genuinely unproved step is a nontrivial near-incidence bound for the sign-locked lock-lock correlation.

## 7. Dependencies and exact artifacts used

- rounds/codex-managed/m9-generic-band-signed-correlation/briefs/blind_generic_band_algebra.md: assigned statement, scope, and required controls.
- The audited coefficient statement supplied by the assignment:
  \[
  \beta_{h,H}
  =-\frac{\Phi(|h|/(H+1))\chi _4(|h|)}{\pi|h|}
  \mathbf 1_{2\nmid h}.
  \]

No Round 3 report, shared proof state, earlier campaign conclusion, or numerical computation was inspected.

## 8. Recommended state effect

**Promote the exact algebra only:** the one-lift formula (3.1), signed-\(p\) convention (2.1), support and symmetry statements, pair convolution (2.4)--(2.6), determinant band (2.7)--(2.9), and solution-line character law (3.9)--(3.10). **Retain as an obstruction:** equal-\(2\)-adic denominator pairs are sign-locked, so no universal \(\chi _4\) orthogonality argument controls \(R_\chi\). **No promotion:** no generic-band energy saving or global correlation lemma has been proved.

## 9. Follow-up seam audit: direct high-frequency block

### 9.1 Verdict and exact normalization

**Accept**, under the phase normalization stated below and in the active range \(D\ll X\). The result is pointwise for every real \(X\), not an averaged estimate. Before absorbing logarithms, the direct argument proves

\[
|S_{2,L}|\ll C_w\left(1+\frac DL\log(2L)\right)X^\varepsilon, \tag{9.1}
\]

and hence, when \(1\le L\le H\le X^C\),

\[
|S_{2,L}|\ll_{\varepsilon,C,C_w}X^\varepsilon
\left(1+\frac DL\right). \tag{9.2}
\]

Here the second display means \(X^\varepsilon(1+D/L)\); the line break is only typographical.

More precisely, with \(e(t)=e^{2\pi i t}\), define the positive block

\[
S_{2,L}^{+}(D;X)
=\sum_{\substack{d\in\mathbb Z\\D\le d<2D}}w_D(d)
\sum_{\substack{h\in\mathbb Z\\L\le h<2L\\h\le H\\2\nmid h}}
\beta_{h,H}e\!\left(\frac{hX}{4d}\right), \tag{9.3}
\]

where \(\sup_d|w_D(d)|\le C_w\). The accepted statement is

\[
|S_{2,L}^{+}(D;X)|
\ll_{\varepsilon,C,C_w}X^\varepsilon\left(1+\frac DL\right) \tag{9.4}
\]

for real \(X\ge2\), \(1\le L\le H\le X^C\), and, for the divisor normalization used below, \(D\le X\). The active range \(D\le X^{1/2}\) is more than sufficient. If \(S_{2,L}\) contains both signs \(L\le|h|<2L\), the same estimate holds with at most twice the constant.

The phase \(hX/(4d)\) is essential: it is exactly the normalization whose odd-frequency resonance is

\[
\left\|\frac{X/d+1}{2}\right\|. \tag{9.5}
\]

If the intended \(S_{2,L}\) has a different phase, (9.5) and therefore the divisor argument must be renormalized.

### 9.2 Geometric summation and the \(\Phi\)-cutoff

For positive odd \(h=2k+1\),

\[
\chi _4(h)e\!\left(\frac{hX}{4d}\right)
=(-1)^ke\!\left(\frac{(2k+1)X}{4d}\right)
=e\!\left(\frac{X}{4d}\right)
e\!\left(k\frac{X/d+1}{2}\right). \tag{9.6}
\]

Put

\[
\alpha_d=\frac{X/d+1}{2},\qquad
\rho_d=\|\alpha_d\|.
\]

Every initial geometric sum over a consecutive \(k\)-interval has modulus at most

\[
\min\left\{N,\frac1{2\rho_d}\right\}, \tag{9.7}
\]

with the usual convention that the second term is \(+\infty\) when \(\rho_d=0\).

On the contributing positive range,

\[
u_h=\frac{\Phi(h/(H+1))}{h}
\]

is nonnegative and nonincreasing: both \(\Phi(h/(H+1))\) and \(1/h\) are nonincreasing. The block may end at \(h<2L\) or at the inclusive Fourier endpoint \(h=H\); either way it remains one consecutive odd progression. Abel summation using (9.7) therefore gives

\[
\left|
\sum_{\substack{L\le h<2L\\h\le H\\2\nmid h}}
\beta_{h,H}e\!\left(\frac{hX}{4d}\right)
\right|
\ll \frac1L\min\left\{L,\frac1{\rho_d}\right\}
=\min\left\{1,\frac1{L\rho_d}\right\}. \tag{9.8}
\]

No derivative bound for \(\Phi\) is needed. If the terminal frequency is \(h=H\), its argument is \(H/(H+1)<1\), so no unrecorded \(u=1\) endpoint occurs. If the block is empty the estimate is trivial.

For negative \(h=-h'\), \(\beta_{-h',H}=\beta_{h',H}\), while the exponential in (9.3) is conjugated. Applying (9.8) separately gives the same bound even for complex denominator weights; real weights are not needed for this estimate.

### 9.3 Exact resonance-to-divisor map

For \(0<R\le1/2\), let

\[
\mathcal N(R)
=\#\left\{d\in\mathbb Z:D\le d<2D,\ \rho_d\le R\right\}.
\]

For every counted \(d\), choose a nearest integer \(m\) to \(\alpha_d\). Then

\[
X-d(2m-1)=2d(\alpha_d-m), \tag{9.9}
\]

so, with

\[
n=d(2m-1)\in\mathbb Z,
\]

one has the exact divisibility and parity conditions

\[
d\mid n,\qquad n/d\ {\rm odd},\qquad
|X-n|=2d\rho_d\le4DR. \tag{9.10}
\]

At the tie \(\rho_d=1/2\), either nearest integer may be chosen; this changes only an absolute constant. The half-open interval \(D\le d<2D\) is fully respected.

Dropping the odd-quotient restriction only enlarges the count. Since \(n=0\) cannot have a nonzero odd quotient \(n/d\), and since \(|n|\ll X\) when \(D\le X\), the pointwise divisor bound gives

\[
\mathcal N(R)
\le
\sum_{\substack{n\in\mathbb Z\setminus\{0\}\\|n-X|\le4DR}}
\tau(|n|)
\ll_\varepsilon X^\varepsilon(1+DR). \tag{9.11}
\]

This argument is valid for arbitrary real \(X\): it counts the integers in a real interval around \(X\), and never assumes that \(X\) is integral. Exact resonances \(\rho_d=0\) correspond to actual integers \(X=n=d(2m-1)\) and are bounded by the same divisor estimate.

### 9.4 Dyadic proximity bins

Equation (9.8) and \(|w_D(d)|\le C_w\) reduce the problem to

\[
|S_{2,L}^{+}|
\ll C_w\sum_{D\le d<2D}
\min\left\{1,\frac1{L\rho_d}\right\}. \tag{9.12}
\]

The bin \(\rho_d\le1/L\) contributes

\[
\ll_\varepsilon X^\varepsilon(1+D/L)
\]

by (9.11). In the bin

\[
\frac{2^j}{L}<\rho_d\le\frac{2^{j+1}}L\le\frac12,
\]

each summand in (9.12) is at most \(2^{-j}\), while (9.11) bounds the number of terms by

\[
\ll_\varepsilon X^\varepsilon(1+D2^j/L).
\]

Thus the \(j\)-th bin contributes

\[
\ll_\varepsilon X^\varepsilon(2^{-j}+D/L).
\]

There are \(O(\log(2L))\) bins, proving (9.1). Under \(L\le H\le X^C\), the logarithm is absorbed into \(X^\varepsilon\), proving (9.4) after renaming \(\varepsilon\).

### 9.5 Endpoint checks

- **\(L=1\).** There is at most the single positive frequency \(h=1\). The direct bound is \(O(D)\), exactly compatible with \(1+D/L\). No proximity-bin argument is needed.
- **Truncation \(2L>H\).** The last odd frequency is the largest odd \(h\le H\). Monotonicity and Abel summation are unchanged.
- **Empty block or \(H=0\).** The sum is zero.
- **Dyadic denominator endpoints.** \(d=D\) is included when integral and \(d=2D\) is excluded. The factor \(2d\) in (9.9) lies between \(2D\) and \(4D\), explaining the constant \(4\) in (9.10).
- **Negative frequencies.** They duplicate the same estimate, not a new resonance.
- **Real \(X\).** The proof is pointwise and uses no averaging, smoothing in \(X\), or integrality of \(X\).
- **Weight hypotheses.** Only \(\ell^\infty\) control of \(w_D(d)\) is used. No denominator variation or sign condition is required.

### 9.6 Comparison with \(L\asymp H_D\) and the Li--Yang gap

At the terminal block

\[
L\asymp H_D=D X^{-1/4},
\]

equation (9.4) gives

\[
|S_{2,L}|\ll_\varepsilon X^\varepsilon(1+X^{1/4})
\ll_\varepsilon X^{1/4+\varepsilon}. \tag{9.13}
\]

Thus the terminal high-frequency block is pointwise at the conjectural \(X^{1/4}\)-scale, formally stronger than a Li--Yang-scale target \(X^{\theta_{\rm LY}+\varepsilon}\) with \(\theta_{\rm LY}>1/4\).

This does **not** close the Li--Yang gap for the full \(S_2(D;X)\). The estimate degrades as \(D/L\) on lower blocks and gives only \(O(D)\) at \(L=1\). Relative to any target exponent \(\theta>1/4\), it is automatically adequate only when

\[
L\gtrsim D X^{-\theta}. \tag{9.14}
\]

The lower and intermediate frequency blocks below that threshold, together with any Vaaler remainder or reconstruction step, remain untreated. The result is therefore a genuine pointwise high-frequency lemma, not a pointwise bound for the complete \(S_2(D;X)\).

### 9.7 Follow-up control outcome

- **Support/endpoint control:** passed, including \(L=1\), \(h=H\), negative \(h\), and both half-open dyadic endpoints.
- **Coefficient variation control:** passed using only monotonicity of \(\Phi(h/(H+1))/h\).
- **Real-\(X\) divisor control:** passed via the exact identity (9.9); the count is pointwise.
- **Proves-too-much control:** the lemma intentionally survives arbitrary bounded denominator phases. Moreover, the same numerical estimate is also true for unsigned frequency coefficients: without \((-1)^k\), the geometric resonance becomes \(\|X/(2d)\|\), and the same proof maps it to \(n=2dm\), with even rather than odd quotient. Thus the specific resonance identity (9.5) is genuinely tied to \(\chi _4\), but the bound (9.4) supplies no signed-versus-unsigned advantage. It does not survive arbitrary phases placed independently on the \(h\)-coefficients, because those destroy the geometric progression.
- **State recommendation:** promote (9.4) as a standalone pointwise high-frequency block lemma under the displayed phase and support hypotheses. Do not promote it as a full \(S_2\) estimate or as a resolution of the Li--Yang gap.

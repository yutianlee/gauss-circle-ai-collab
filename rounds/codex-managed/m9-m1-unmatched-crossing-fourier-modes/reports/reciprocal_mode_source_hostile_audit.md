## 1. Result

The Vaaler interface in (66.2) is exact with the displayed sign, but the
available one-variable reciprocal-sum technology does not prove the required
bound.  Put
\[
 J=X^{1/2},\qquad T=X^{1/2-\nu/2},\qquad Q=J/T=X^{\nu/2}.
\]
After giving the exact wavelet filter its most favorable effect, namely
localization to \(|k|\asymp Q\), an exponent pair \((\kappa,\lambda)\)
has capacity
\[
 J^\lambda Q^\kappa
   =X^{(\lambda+\kappa\nu)/2+\varepsilon}.                 \tag{R66.1}
\]
The Tao--Trudgian--Yang (TTY) pair
\((89/1282,997/1282)\) therefore gives, at \(\nu=2/5\),
\[
 X^{5163/12820+\varepsilon}=X^{0.402730\ldots+\varepsilon},
\]
not \(X^{1/4+\varepsilon}\).  The elementary second-derivative bound gives
\(X^{7/20+\varepsilon}\), and the standard classical pair
\((2/7,4/7)\) improves this only to
\[
 X^{12/35+\varepsilon}=X^{0.342857\ldots+\varepsilon}.     \tag{R66.2}
\]
Thus the sharpest concrete, source-lawful capacity obtained in this audit is
\(12/35\); this is not asserted to optimize all known exponent pairs.  None
of these bounds closes any \(\nu\geq0\) interval.  No exponent should change.

## 2. Exact statement and hypotheses

Let \(n_0=\lfloor X\rfloor\), let \(v\in\mathbb Z\) with
\(|v|\ll TX^\eta\), and let \(\Xi\in C_c^\infty((0,1))\) be real and fixed.
For integer \(K\geq1\), define
\[
 \psi_F(x)=\{x\}-\tfrac12,
 \quad
 p_K(x)=\sum_{1\leq |k|\leq K}\alpha_{k,K}e(kx),
 \quad
 \alpha_{k,K}=-{\Phi(|k|/(K+1))\over2\pi i k}.
\]
Vaaler's theorem, with the floor endpoint restored, says
\[
 \psi_F(x)=p_K(x)+R_K^F(x),\qquad
 |R_K^F(x)|\leq E_K(x):={K_K(x)\over2K+2}.                 \tag{R66.3}
\]
Consequently (66.1) is exactly
\[
 \mathfrak D_X(v)=
 \sum_{1\leq|k|\leq K}\alpha_{k,K}\mathcal S_k(v)
 +\sum_j\chi_4(j)\Xi(j/J)
   \{R_K^F(n_0/j)-R_K^F((n_0+v)/j)\},                     \tag{R66.4}
\]
where
\[
 \mathcal S_k(v)=\sum_j\chi_4(j)\Xi(j/J)e(kn_0/j)
                     (1-e(kv/j)).                          \tag{R66.5}
\]
The rigorous TTY specialization is
\[
 |\mathcal S_k(v)|\ll X^\varepsilon
 \min(1,|k||v|/J)|k|^{89/1282}J^{997/1282}.               \tag{R66.6}
\]
It is pointwise in \((k,v)\), not a bilinear or mean-square theorem.

## 3. Proof or derivation

Subtracting the two copies of \(p_K\) gives
\(e(kn_0/j)(1-e(kv/j))\), so both the sign in (66.2) and the minus sign in
\(\alpha_{k,K}\) are correct.  Moreover
\(\alpha_{-k,K}=\overline{\alpha_{k,K}}\) and
\(\mathcal S_{-k}(v)=\overline{\mathcal S_k(v)}\), including for negative
\(v\), so the paired contribution is real.

On each of the two nonzero residue classes modulo four, set the TTY interval
length to \(N\asymp J\) and its oscillation parameter to
\(\mathcal T\asymp |k|n_0/J\asymp |k|J\).  Then
\(\mathcal T/N\asymp |k|\), and after a fixed affine rescaling the model
phase is \(F(u)=u^{-1}\).  For \(|k||v|\leq J\), the combined amplitude in
(R66.5) has normalized bounded variation
\(O(|k||v|/J)\).  For \(|k||v|>J\), apply TTY separately to the two phases
with centers \(n_0\) and \(n_0+v\), whose cutoff has bounded normalized
variation.  This proves (R66.6); merely declaring the high-mode combined
amplitude to have bounded variation would be false.

The exact wavelet difference annihilates the constant in
\(1-e(kv/j)\).  Discrete Abel summation and Poisson summation convert its
remaining \(v\)-transform into the compact Fourier support condition
\(2Tk/j\in\operatorname{supp}g\) (with the harmless fixed translate from
the accepted wavelet).  Since \(K<J\), nonzero Poisson aliases are absent,
and the surviving main block has \(|k|\asymp J/T=Q\).  Summing
\(|\alpha_{k,K}|\asymp1/|k|\) over that block yields (R66.1).  Substitution
of the TTY pair gives \(5163/12820\).  The van der Corput second-derivative
estimate gives \((\kappa,\lambda)=(1/2,1/2)\), hence \(7/20\).  Classical
\(A/B\) iteration gives \((2/7,4/7)\), hence (R66.2).  In general closure
would require
\[
 \lambda+\kappa\nu\leq\tfrac12,                            \tag{R66.7}
\]
which none of these pairs satisfies for any \(\nu\geq0\).

Finally, from the exact Fejer formula,
\[
 E_K(x)\ll\min\{1,(K\|x\|)^{-2}\}.
\]
Writing the nearest-integer residual as \(r=n-mj\), each fixed \(r\) has
at most \(\tau(n-r)\ll X^\varepsilon\) eligible \(j\asymp J\).  Summing
the dyadic tails gives, uniformly for integral \(n\asymp X\),
\[
 \sum_{j\asymp J}E_K(n/j)\ll X^\varepsilon(1+J/K).         \tag{R66.8}
\]
The \(\ell^1\)-norm of the exact wavelet differences is \(O(1)\), so this
also controls the weighted residual.  It requires \(K\geq X^{1/4}\) at the
target.  Since \(Q=X^{1/5}<X^{1/4}<J\), this is compatible with transition
localization of the main polynomial, but supplies no missing arithmetic
cancellation.

## 4. First doubtful or unproved step

The first missing step is a signed joint \((j,k)\) estimate for the
transition block that improves (R66.1) to square-root size.  No audited
theorem does this.  Cauchy in \(k\) exposes a diagonal of natural size
\(J\) before the final square root: with \(Q\) coefficients of size
\(Q^{-1}\), the \(j_1=j_2\) terms already yield
\((Q^{-1}\cdot QJ)^{1/2}=J^{1/2}=X^{1/4}\).  Thus every off-diagonal must
be controlled with essentially no power loss.  The packet contains no such
large-sieve spacing lemma, and pointwise TTY cannot provide one.

## 5. Required control test and outcome

- **Fejer and zero mode:** the Vaaler polynomial has no \(k=0\), but the
  positive majorant has mean \(1/(2K+2)\), producing the indispensable
  \(J/K\) term in (R66.8).  The residual difference is signed; only its
  absolute value is bounded by the sum of two positive majorants.
- **Exact integers:** at an integer, \(p_K=0\), \(R_K^F=-1/2\), and
  \(E_K=1/2\).  Therefore endpoints cannot be deleted.  Rows with
  \(j\mid n_0\) or \(j\mid n_0+v\) number \(X^{o(1)}\), so they fit
  (R66.8), but they are genuine coherent rows.
- **Squares and fourth powers:** if \(n_0=M^2\), and especially if
  \(n_0=M^4\), interior divisors such as \(j=M/q\) or \(j=M^2/q\) make
  \(e(kn_0/j)=1\) for every \(k\).  Their divisor-bounded total is harmless
  by itself, but it disproves any blanket irrational-spacing assumption and
  must remain in a bilinear off-diagonal analysis.
- **Cutoffs and signs:** compact support of \(\Xi\) gives uniform derivative
  bounds after splitting \(j\equiv1,3\pmod4\); the split alone gives no
  saving.  Negative \(k\) is the conjugate mode and negative \(v\) needs no
  altered formula.
- **Regimes:** the low-mode factor is \(|k|T/J\), transition is
  \(|k|\asymp Q\), and high modes must be treated as two separate sums.
  Taking an absolute value in \(v\) before the exact wavelet filter loses
  the transition localization and is not an admissible proof of the weaker
  weighted target.
- **Full cone:** all conclusions concern only the fixed interior cutoff.
  The sharp \(j\asymp J\) collision, other reciprocal-cone cutoffs,
  transition seams, and remaining M9/M1 modules are untouched.

## 6. Dependencies and exact artifacts used

The mathematical inputs were `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, the Round-66 derivation packet and task brief,
`rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`,
`sources/vaaler_1985.md`, and `sources/tao_trudgian_yang_2025.md`.
The primary sources checked were Vaaler, *Bull. AMS* 12 (1985), Theorem 18
and (7.14), and Tao--Trudgian--Yang, arXiv:2501.16779, its exponent-pair
definition and `New exponent pairs` theorem.

As a bilinear control, Bettin--Chandee,
*Trilinear forms with Kloosterman fractions*, arXiv:1502.00769, treats
\(e(a\overline m/n)\) with a modular inverse and coprimality structure.
Our phase \(e(kn_0/j)\) is an ordinary real reciprocal phase, with neither
that inverse nor the theorem's variable architecture.  Importing their
bound here would therefore be unlawful.  No other primary bilinear theorem
was found whose stated hypotheses match the moving difference amplitude,
fixed center, character, and exact wavelet transform.

## 7. Recommended state effect

Retain (R66.4)--(R66.8) as an audited Fourier interface and rigorous
method-capacity no-go.  In particular, retain the endpoint-correct Fejer
count \(X^\varepsilon(1+J/K)\), the lawful TTY normalization, and the
diagonal warning.  Reject any claim that TTY or a Kloosterman-fraction
bilinear theorem proves the target.  Do not promote a radial interval, do
not change the exponent, and make no change to the accepted proof graph
except through the conductor's later State Patch.

# Round 164 updated journal and arXiv scan

- Audit date: 2026-08-26 (Asia/Shanghai).
- Scope: recent work explicitly naming the classical Gauss circle problem,
  plus nearby weighted-exponential-sum papers that might conceivably accept
  the Round-164 residual coefficient or its cross-product-shift energy.
- Evidentiary rule: theorem statements are taken from arXiv or publisher
  pages. Search-engine snippets are discovery aids only.

## 1. Current pointwise exponent

The official arXiv record for X. Li and X. Yang,
*An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*,
arXiv:2308.14859v2, was last revised on 2023-09-14:

<https://arxiv.org/abs/2308.14859>

The project accepts the final narrow conclusion only through the five
explicit source repairs recorded in sources/li_yang_2023.md; the printed
general source interfaces are not imported without those repairs.  In the
normalization

\[
 R(X)=\sum_{m^2+n^2\le X}1-\pi X,
\]

the repaired narrow conclusion is

\[
 R(X)=O_\varepsilon(X^{\theta^*+\varepsilon}),
 \qquad \theta^*=0.3144831759741\ldots.
\]

The arXiv submission history still lists only v1 and v2 and no journal DOI.
An official July-2026 arXiv paper by B. Cloitre continues to describe
Li--Yang as a 2023 preprint and its exponent as a claimed smaller admissible
exponent:

<https://arxiv.org/abs/2607.20960>

A 2026 *Journal of Number Theory* article by Karak and Mahatab,
*The Piltz divisor problem in number fields using the resonance method*,
likewise describes Li--Yang's value as the sharpest recent upper exponent
in its comparative introduction; the article itself proves a different
number-field divisor result, not a new circle upper theorem:

<https://doi.org/10.1016/j.jnt.2025.10.013>

**Audit conclusion.** This search found no later theorem improving
\(\theta^*\). The externally audited best pointwise exponent therefore
remains \(0.3144831759741\ldots\), with the important status qualifiers
that the source remains a preprint and the project theorem is the repaired
narrow conclusion, not the general printed interfaces. This is a scoped
literature conclusion, not a proof that no unindexed result exists.

## 2. Recent papers explicitly naming the problem

### Classical problem in an equivalent encoding

B. Cloitre, *Fibonacci, Dirichlet, and Gauss in a single sum*,
arXiv:2607.20960, proves exact equivalences between parity-restricted
Fibonacci remainder exponents and the classical circle/divisor exponents.
It supplies no new circle upper bound and does not estimate the literal
Round-164 residual coefficients.

<https://arxiv.org/abs/2607.20960>

### Smooth-number restriction

P. Gao, *On the Gauss circle problem over smooth numbers*,
arXiv:2604.23918, asymptotically evaluates the two-square representation
sum restricted to \(y\)-smooth integers in specified \((x,y)\)-ranges. The
restriction is not the complete classical error term and its saddle-point
Euler-product hypotheses do not place the hard-TOP residual or the shifted
product correlation \(d'm'-dm=r\).

<https://arxiv.org/abs/2604.23918>

### Different point sets

A. Haynes and C. Lutsko, *The Gauss circle problem for Penrose tilings*,
arXiv:2512.21444, proves a point-counting estimate for vertices of Penrose
tilings by a cut-and-project/Fourier argument. Its algebraic conjugate-window
separation is specific to the Penrose lattice and does not apply to the
integer-lattice residual coefficient.

<https://arxiv.org/abs/2512.21444>

R. A. Edwin and A. Lin, *The Gauss Circle Problem and Fourier
Quasicrystals*, arXiv:2412.05485 and IMRN 2025, extends point-counting
questions to Fourier quasicrystals. Its exponent depends on the spectrum of
the quasicrystal; it is not an improvement of the classical integer-lattice
pointwise exponent.

<https://arxiv.org/abs/2412.05485>

### Empirical arithmetic of the counting values

T. Ehrenborg, *Gauss Circle Primes*, arXiv:2502.06804, studies when the
integer-valued disk count is prime and reports computation through
\(2\cdot10^6\) plus a heuristic. It proves no classical error estimate.

<https://arxiv.org/abs/2502.06804>

## 3. Nearby weighted exponential sums

N. Bag and D. Mazumder, *Weighted exponential sums and its applications*,
arXiv:2408.02020, treats divisor- and squarefree-weighted sums for real
**polynomial** phases whose leading coefficient is on a minor arc.
Round 164 has the nonlinear square-root phase \(J\sqrt N\), a moving
residual divisor window, and after Fejer differencing the exact product-shift
constraint \(d'm'-dm=r\). No theorem statement in the paper accepts that
interface.

<https://arxiv.org/abs/2408.02020>

## 4. Effect on Round 164 strategy

The scan supplies no drop-in theorem for the literal residual and no global
exponent update. It does reinforce three strategic decisions:

1. preserve the outer phase instead of replacing the residual coefficients
   by a positive transport norm;
2. formulate the first missing result as the exact short-shift Fejer energy
   for the physical coefficients, whose expanded arithmetic condition is
   \(d'm'-dm=r\); and
3. compare any future decoupling placement against the actual moving
   coefficient and the accepted rank-one product-collar power ledger, rather
   than importing a classical unweighted first-spacing theorem by analogy.

No literature statement audited here changes M9--M1, M9--M2, the bridge,
the internal \(1/3\) proof state, the external
\(0.3144831759741\ldots\) benchmark, or the conjectural \(1/4\) target.

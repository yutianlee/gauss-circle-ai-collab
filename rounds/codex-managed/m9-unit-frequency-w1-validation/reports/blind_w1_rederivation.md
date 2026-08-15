# Blind rederivation of the unit-frequency W-1 bound

## 1. Result

**Conditional lemma (validated in the absolute/unsigned scope).** The proposed
lower bound follows from a one-dimensional binning argument for pair sums of
reciprocals. With the hypotheses made explicit, it is

\[
\Sigma_{\rm abs}(0<|N|\leq M)
\geq c_0\min(D^4,MD)-C_\varepsilon D^2X^\varepsilon .
\]

It is valid uniformly for every \(M\geq1\), hence in particular for
\(1\leq M\ll D^3\). Here \(c_0>0\) depends only on the fixed lower envelopes
of the unit-frequency coefficient and dyadic weight, and on the fixed
proportion of the dyadic interval on which those envelopes hold. The \(N=0\)
estimate is an assumption, not a consequence of the binning argument.

The result does **not** give a lower bound for the true signed sum. Moreover,
if a smooth dyadic weight is present but no fixed positive core/lower-envelope
hypothesis is imposed, transfer from the raw tuple count to weighted mass is
not valid. For a sharp dyadic cutoff the needed hypothesis is automatic.

## 2. Exact statement and hypotheses

Let \(X\geq2\), \(D\geq2\), and

\[
I_D=\{d\in\mathbb Z:D\leq d<2D\}.
\]

The convention \(D<d\leq2D\) works identically. Let
\(A_D\subseteq I_D\) satisfy

\[
|A_D|\geq \kappa D
\]

for a fixed \(\kappa>0\). Suppose a nonnegative dyadic amplitude \(w_D(d)\)
satisfies \(w_D(d)\geq w_0>0\) on \(A_D\), and suppose

\[
|\beta_{1,H}|\geq b_0>0
\]

uniformly in all parameters under consideration. For a sharp,
\(\chi_4\)-removed block, take \(A_D=I_D\), \(w_D=1\). If an absolute factor
\(|\chi_4(d)|\) remains, take the odd elements of \(I_D\); then one can take
an absolute \(\kappa<1/2\) for all \(D\geq2\).

For an ordered quadruple
\({\bf d}=(d_1,d_2,d_3,d_4)\in I_D^4\), put

\[
\Delta({\bf d})=\frac1{d_1}+\frac1{d_2}
                 -\frac1{d_3}-\frac1{d_4}
                =\frac{N({\bf d})}{d_1d_2d_3d_4},
\]

where exact denominator clearing gives the integer

\[
N({\bf d})
=d_2d_3d_4+d_1d_3d_4-d_1d_2d_4-d_1d_2d_3.
\]

**Normalization note.** This report uses the sign order \(+,+,-,-\).
The frozen \(+,-,+,-\) convention is identical after swapping indices
\(2\) and \(3\): if
\(\Delta_{\rm fr}(e_1,e_2,e_3,e_4)=e_1^{-1}-e_2^{-1}
+e_3^{-1}-e_4^{-1}\), then
\(\Delta_{\rm fr}(d_1,d_3,d_2,d_4)=\Delta({\bf d})\).
The cleared integer \(N\), tuple window, and all counts are therefore carried
to the frozen convention by this bijective relabeling.

Normalize the absolute unit-frequency mass by

\[
\Sigma_{\rm abs}(E)=
\sum_{\substack{{\bf d}\in I_D^4\\N({\bf d})\in E}}
|\beta_{1,H}|^4\prod_{i=1}^4 w_D(d_i).
\]

The proof applies unchanged to any actual normalization whose per-tuple
absolute weight has this fixed lower envelope on \(A_D^4\).

Assume explicitly that for every \(\varepsilon>0\) there is a constant
\(C_\varepsilon\), independent of \(X,D,H,M\) in the stated range, such that

\[
\Sigma_{\rm abs}(\{0\})\leq C_\varepsilon D^2X^\varepsilon.
\tag{ER}
\]

Then for every \(\varepsilon>0\) and every real \(M\geq1\),

\[
\boxed{
\Sigma_{\rm abs}(\{N\in\mathbb Z:0<|N|\leq M\})
\geq \frac{\kappa^4(b_0w_0)^4}{17}\min(D^4,MD)
      -C_\varepsilon D^2X^\varepsilon .}
\tag{W-1}
\]

The explicit constant \(17\) is convenient, not optimized.

## 3. Independent proof

For each ordered pair \((a,b)\in A_D^2\), form

\[
s(a,b)=\frac1a+\frac1b.
\]

All \(|A_D|^2\) pair sums lie in an interval of length at most \(1/D\),
between \(1/D\) and \(2/D\). Partition that interval into half-open windows
of width

\[
\eta=\frac{M}{16D^4}.
\]

The window count is at most

\[
K\leq \left\lceil\frac{1/D}{\eta}\right\rceil
  =\left\lceil\frac{16D^3}{M}\right\rceil
\leq 1+\frac{16D^3}{M}.
\tag{1}
\]

Let \(r_j\) be the number of ordered pairs whose sum lies in window \(j\).
Every ordered pair of pair-sums in the same window gives a quadruple with
\(|\Delta({\bf d})|<\eta\). Since \(d_i<2D\), denominator clearing yields

\[
|N({\bf d})|
=d_1d_2d_3d_4|\Delta({\bf d})|
<16D^4\eta=M.
\tag{2}
\]

Thus these quadruples all satisfy \(|N|\leq M\). By Cauchy--Schwarz and (1),
their number \(T_M\) obeys

\[
T_M\geq \sum_jr_j^2
\geq\frac{(\sum_jr_j)^2}{K}
\geq\frac{|A_D|^4}{1+16D^3/M}.
\]

If \(M\leq D^3\), the last expression is at least
\(\kappa^4MD/17\); if \(M\geq D^3\), it is at least
\(\kappa^4D^4/17\). Hence

\[
T_M\geq\frac{\kappa^4}{17}\min(D^4,MD).
\tag{3}
\]

Every tuple in \(A_D^4\) has absolute mass at least
\((b_0w_0)^4\). Therefore

\[
\Sigma_{\rm abs}(|N|\leq M)
\geq \frac{\kappa^4(b_0w_0)^4}{17}\min(D^4,MD).
\]

Only now separate exact from near resonance:

\[
\Sigma_{\rm abs}(0<|N|\leq M)
=\Sigma_{\rm abs}(|N|\leq M)-\Sigma_{\rm abs}(N=0).
\]

Applying (ER) proves (W-1). The binning proof itself does not estimate the
exact term. Indeed the diagonal families
\((d_1,d_2)=(d_3,d_4)\) and \((d_1,d_2)=(d_4,d_3)\) already give order
\(D^2\) exact resonances.

## 4. Epsilon and range audit

The needed quantifiers are

\[
\forall\varepsilon>0\ \exists C_\varepsilon<\infty\
\forall(X,D,H)\quad\text{(ER) holds in the relevant range},
\]

with \(b_0,w_0,\kappa\) fixed independently of those parameters. One may
then choose \(\varepsilon\) after fixing a desired power gap \(\delta\).
Allowing \(b_0,w_0\), or \(\kappa\) to decay with \(X\) would change the
power comparison and is not covered.

At

\[
M=\frac{D^4}{X},
\]

the restriction \(M\geq1\) is exactly \(D\geq X^{1/4}\), while
\(M\leq D^3\) is \(D\leq X\). Thus throughout
\(X^{1/4}\leq D\leq X^{1/2}\),

\[
\Sigma_{\rm abs}(0<|N|\leq D^4/X)
\geq c_0\frac{D^5}{X}-C_\varepsilon D^2X^\varepsilon.
\tag{4}
\]

The required endpoint checks are:

| \(D\) | \(M=D^4/X\) | main \(D^5/X\) | exact allowance \(D^2X^\varepsilon\) | consequence |
|---|---:|---:|---:|---|
| \(X^{1/4}\) | \(1\) | \(X^{1/4}\) | \(X^{1/2+\varepsilon}\) | valid but generally vacuous after subtraction |
| \(X^{3/8}\) | \(X^{1/2}\) | \(X^{7/8}\) | \(X^{3/4+\varepsilon}\) | positive power gap if \(\varepsilon<1/8\) |
| \(X^{1/2}\) | \(X\) | \(X^{3/2}\) | \(X^{1+\varepsilon}\) | positive power gap if \(\varepsilon<1/2\) |

Rounding a dyadic parameter \(D\) by a bounded factor does not affect these
conclusions. More generally, if \(D\geq X^{1/3+\delta}\), with fixed
\(\delta>0\), then

\[
\frac{D^5/X}{D^2X^\varepsilon}
=\frac{D^3}{X^{1+\varepsilon}}
\geq X^{3\delta-\varepsilon}.
\]

Choosing any \(0<\varepsilon<3\delta\), (4) is
\(\gg D^5/X\) for all sufficiently large \(X\), depending on the fixed
constants. At \(D=X^{1/3}\), the argument gives no positive power separation
from the \(X^\varepsilon\) exact-resonance allowance.

## 5. First doubtful or unproved step

The first genuinely unproved input is (ER), the asserted absolute weighted
upper bound for exact \(N=0\) resonances. It cannot be inferred from the
near-resonance binning and must be proved elsewhere with precisely the same
support and weights.

The second necessary seam is dyadic-weight transfer. If the actual dyadic
cutoff is a fixed nonzero continuous bump, it has a closed interior
subinterval on which its absolute value is bounded below, giving
\(A_D,w_0\). If no such uniform core exists, the raw-count-to-mass implication
is false: the assumptions \(|\beta_{1,H}|\geq b_0\) and (ER) alone do not
prevent all nonexact tuple weights from being zero.

## 6. Required controls

### exact-vs-near-resonance

- **Input:** the windows above, including all \(N=0\) tuples.
- **Expected invariant/failure:** Cauchy--Schwarz counts \(|N|\leq M\), not
  \(0<|N|\leq M\); diagonal exact resonances can carry substantial mass.
- **Observed result:** exact resonance is removed only through the explicit
  assumption (ER). No exact-energy-to-near-energy inference was used.
- **Implication:** the candidate is conditional on (ER), and may be vacuous
  near \(D=X^{1/4}\).

### dyadic-endpoints

- **Input:** \(D=X^{1/4},X^{3/8},X^{1/2}\) and \(M=D^4/X\).
- **Expected invariant/failure:** \(M\geq1\), \(M\leq D^3\), and the main/error
  exponents must be checked separately.
- **Observed result:** all three points lie in range; their exponents appear
  in the table. Only the first endpoint is generally swallowed by the
  exact-term allowance.
- **Implication:** no endpoint is crossed silently, and the power obstruction
  starts strictly beyond \(D=X^{1/3}\), after choosing
  \(\varepsilon<3\delta\).

### signed-vs-unsigned

- **Input:** replace every tuple contribution by its absolute magnitude, and
  compare with fixed \(\chi_4\) signs, random signs, or adversarial signs of
  the same magnitudes.
- **Expected failure:** tuple abundance alone cannot bound a signed sum from
  below; pair contributions within a bin can cancel, as can contributions
  from different bins or from the rest of the near band.
- **Observed result:** the proof uses nonnegativity at the weight-transfer and
  exact-subtraction steps. It proves the weight-blind count, the corresponding
  absolute beta-weighted mass, and the \(\chi_4\)-removed unsigned mass (or an
  absolute-\(|\chi_4|\) restriction to odd denominators). It never controls
  the true \(\chi_4\) signs.
- **Implication:** there is no conclusion about the full true signed mass.

## 7. Dependencies and exact artifacts used

Only these permitted artifacts were used:

1. rounds/codex-managed/m9-unit-frequency-w1-validation/briefs/blind_w1_rederivation.md
2. problems/gauss_circle.md
3. state/control_models.md

No excluded Round 1 material, proof graph, proof draft, campaign plan, legacy
derivation, or other Round 2 report was consulted.

## 8. Recommended state effect

**Promote conditionally in the absolute/unsigned graph only**, with (ER), the
uniform lower bound for \(|\beta_{1,H}|\), and the fixed positive dyadic core
written as hypotheses. Retain the explicit \(N=0\) subtraction and the
quantifier \(\forall\varepsilon>0\,\exists C_\varepsilon\). Reject promotion
to the full signed sum, and reject raw-to-smooth-weight transfer when the
positive-core hypothesis is absent.

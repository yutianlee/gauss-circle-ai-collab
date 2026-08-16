# Blind chirped Kloosterman energy rederivation

## 1. Result

For the negative-phase odd class, the complete Poisson identity, its
stationary frequency, the leading phase, the leading \(L^2\) mass, and the
factor-\(B\) capacity deficit all rederive exactly.  After deleting the
diagonal, the leading off-diagonal is equivalently a chirped shifted
Kloosterman covariance.  Weil's bound already disposes of every dyadic
shift range \(H\ll Q^2/B^2\), as well as the perfect-square and
fourth-power subsequences.  The first strictly smaller unresolved object
is therefore the actual-symbol covariance in the large-shift range

\[
             Q^2/B^2\ll H\ll Q^2.                 \tag{R82.1}
\]

It needs a signed factor-\(B\) saving over ordinary coefficient-blind
capacity.  A one-dimensional Poisson/stationary \(B\)-process preserving
the chirp is an exact return to the original \((c,b)\) reciprocal row;
coefficient-uniform \(TT^*\) or dispersion instead erases the common
\(n\)-chirp and retains the factor-\(B\) deficit.  Thus these operations do
not prove a nonempty extension from the supplied data.  No all-class
claim is possible: none of the even-class transforms or their errors can
be inferred from the odd formula.

## 2. Exact statement and hypotheses

Write \(e(z)=e^{2\pi iz}\), \(N=Q^2\), \(q=4b\), and

\[
A=A_{1/4,b}=\left(\sqrt{bX}+\sqrt{k/(4b)}\right)^2,
\qquad D_b=J+\frac{\sqrt{k}}{2b}.
\]

Assume throughout this section that \(k>0\) is fixed and nonzero,
\(b\asymp B\), and that the retained odd component really is the globally
smooth complete row

\[
S_b=u_{b,k}\sum_{(c,q)=1}W_b(c)e_q(k\bar c)e(-A/c),
\qquad \operatorname{supp}W_b\subseteq[c_0C,c_1C].       \tag{R82.2}
\]

The unit \(u_{b,k}\) is harmless.  The reflected alias is a separate
statement with the reflected sign and stationary frequency.  Assume also,
only when estimating the leading stationary term, that its actual symbol
\(V_{b,n}\) is uniformly \(O(X^\varepsilon)\) on \(n\asymp N\).  No
hypothesis about an even cusp multiplier is being inserted.

Under these hypotheses:

1. Poisson summation gives
   \[
   S_b={u_{b,k}\over q}\sum_{n\in\mathbb Z}S(n,k;q)I_{b,n},
   \quad I_{b,n}=\int W_b(x)e(-A/x-nx/q)\,dx.       \tag{R82.3}
   \]
   Any separately defined row-remainder must be added separately.
2. The retained stationary branch has \(n\asymp N\) and
   \[
   {I_{b,n}\over q}=J^{1/2}n^{-3/4}
   e\!\left(-J\sqrt n-\frac{\sqrt{kn}}{2b}\right)V_{b,n}
   +\hbox{lower stationary terms}.                \tag{R82.4}
   \]
3. With \(a_{b,n}\) equal to the displayed leading coefficient,
   \[
   \sum_{n\asymp N}|a_{b,n}|^2\ll X^\varepsilon J/Q
   =X^\varepsilon T.                              \tag{R82.5}
   \]
4. An ordinary unnormalized Kloosterman large-sieve capacity is
   \[
   X^\varepsilon B(Q^2+B^2)T
   \asymp X^\varepsilon BQ^2T,                    \tag{R82.6}
   \]
   exactly \(B=C/T\) times \(J^2/T\).
5. Put
   \[
   \Delta_h(n)=\sqrt{n+h}-\sqrt n,
   \quad
   \Omega_{b,h}(n)=Q^3((n+h)n)^{-3/4}
      V_{b,n+h}\overline{V_{b,n}},                \tag{R82.7}
   \]
   with the support condition \(n,n+h\asymp N\).  For a dyadic
   \(1\le H\ll N\), define the actual-symbol shifted covariance
   \[
   \begin{split}
   \mathcal K_H={}&
   \sum_{H<|h|\le2H}\ \sum_{n,n+h\asymp N}
   e(-J\Delta_h(n))\\
   &\times\sum_{b\asymp B}S(n+h,k;4b)\overline{S(n,k;4b)}
   e\!\left(-{\sqrt k\over2b}\Delta_h(n)\right)
   \Omega_{b,h}(n).
   \end{split}                                    \tag{R82.8}
   \]
   Up to the separately owned lower terms and row-remainders, the
   off-diagonal leading energy is
   \[
             {J\over Q^3}\sum_H\mathcal K_H.      \tag{R82.9}
   \]
   Hence the needed normalized signed bound is
   \(
      \sum_H\mathcal K_H\ll X^\varepsilon Q^4
   \);
   the sufficient single-block target is
   \(
      \mathcal K_H\ll X^\varepsilon Q^4
   \).

## 3. Proof or derivation

Decompose \(c=r+qm\) in (R82.2).  With the Fourier convention
\(
\widehat f(\xi)=\int f(x)e(-\xi x)\,dx
\), Poisson summation on each progression gives

\[
\sum_m f(r+qm)={1\over q}\sum_n e_q(nr)\widehat f(n/q).
\]

Summing over \(r\pmod q\) with \((r,q)=1\) produces
\(
\sum_r^*e_q(nr+k\bar r)=S(n,k;q)
\), proving (R82.3) and fixing both signs.  In particular, the phase
shown in (R82.3) belongs to the original phase \(e(-A/c)\).  For
\(e(+A/c)\), stationarity occurs at the reflected sign of \(n\); it is not
obtained by silently retaining the same \(n\)-branch.

For positive \(n\), the phase
\(
\phi(x)=-A/x-nx/q
\)
has

\[
 x_n=\sqrt{Aq/n},\qquad
 \phi(x_n)=-2\sqrt{An/q}.
\]

The exact identities

\[
 Aq=(2bJ+\sqrt k)^2,
 \qquad
 2\sqrt{A/q}=J+{\sqrt k\over2b}=D_b              \tag{R82.10}
\]

give the phase in (R82.4).  Since \(x_n\asymp C\),

\[
 n\asymp {Aq\over C^2}\asymp {b^2J^2\over C^2}
 \asymp {J^2\over T^2}=Q^2.                     \tag{R82.11}
\]

Moreover, \(\phi''(x_n)=-2A/x_n^3\), so the leading stationary
amplitude after division by \(q\) is

\[
 {1\over q}|\phi''(x_n)|^{-1/2}
 ={1\over\sqrt2}(A/q)^{1/4}n^{-3/4}
 \asymp J^{1/2}n^{-3/4}.                        \tag{R82.12}
\]

The Gaussian unit and the smooth ratio
\((A/q)^{1/4}/J^{1/2}\) are absorbed into \(V_{b,n}\).  Squaring this
coefficient and counting \(N=Q^2\) integers proves

\[
 \sum_{n\asymp Q^2}J n^{-3/2}|V_{b,n}|^2
 \ll X^\varepsilon Q^2JQ^{-3}
 =X^\varepsilon J/Q=X^\varepsilon T.
\]

The original \(c_1=c_2\) energy is
\(
O(X^\varepsilon BC)=O(X^\varepsilon C^2/T)
\), which is below \(J^2/T\).  The transformed \(n_1=n_2\) diagonal is
the same size at capacity level: Weil's bound, with fixed nonzero \(k\),
gives
\(
|S(n,k;4b)|^2\ll X^\varepsilon B
\), and therefore

\[
 \sum_{b\asymp B}\sum_{n\asymp N}
 |a_{b,n}S(n,k;4b)|^2
 \ll X^\varepsilon B^2T={C^2\over T}.           \tag{R82.13}
\]

In the present band \(B^2\ll Q^2\).  Substitution of (R82.5) into the
ordinary modulus-range capacity gives (R82.6).  Its ratio to the target is

\[
 {BQ^2T\over J^2/T}
 =B\left({QT\over J}\right)^2=B={C\over T},      \tag{R82.14}
\]

so the deficit is exactly \(B\) in energy, or \(B^{1/2}\) in norm.

Expanding the leading energy, setting \(n_1=n+h,n_2=n\), and factoring
\(
a_{b,n+h}\overline{a_{b,n}}=(J/Q^3)
e(-J\Delta_h(n))e(-\sqrt{k}\Delta_h(n)/(2b))
\Omega_{b,h}(n)
\)
proves (R82.8)--(R82.9).  This also shows that the reciprocal-square-root
phase is part of the actual symbol/kernel and cannot be discarded.

There is a useful strict reduction before the unresolved step.  Weil and
\(|\Omega_{b,h}|\ll X^\varepsilon\) give

\[
 |\mathcal K_H|\ll X^\varepsilon B^2NH.          \tag{R82.15}
\]

Consequently every block \(H\le N/B^2\) already satisfies the required
\(X^\varepsilon N^2=X^\varepsilon Q^4\) bound.  Only (R82.1) remains.

Finally, expanding one Kloosterman sum in the retained transformed row
exhibits the exact self-return.  For \(r\pmod q\), the \(n\)-phase is

\[
 \psi(n)=-D_b\sqrt n+{rn\over q}.
\]

In Poisson's dual integral with integer frequency \(m=-\ell\), its
stationary point satisfies

\[
 \delta=\ell+{r\over q},\qquad
 n_0={D_b^2\over4\delta^2}.
\]

The Legendre phase is exactly

\[
 \psi(n_0)-m n_0
 =-{D_b^2\over4\delta}
 =-{D_b^2q\over4(q\ell+r)}
 =-{A\over q\ell+r},                            \tag{R82.16}
\]

because \(D_b^2q/4=A\).  The dual variable
\(c=q\ell+r\asymp qT\asymp C\), and
\(e_q(k\bar r)=e_q(k\bar c)\).  Thus the chirp-preserving
Poisson/stationary operation reconstructs (R82.2), including its local
unit.  It supplies no new inequality.

A coefficient-uniform \(TT^*\) has the complementary failure.  The
factor \(e(-J\sqrt n)\) is a diagonal unitary on the input coefficient
space and disappears when the operator norm is taken.  Its \(TT^*\)
kernel is only the cross-modulus correlation

\[
 \sum_{n\asymp N}S(n,k;4b_1)\overline{S(n,k;4b_2)}
 e\!\left(-{\sqrt{kn}\over2}
       (b_1^{-1}-b_2^{-1})\right)
 V_{b_1,n}\overline{V_{b_2,n}},                 \tag{R82.17}
\]

whose ordinary diagonal/capacity is still larger by \(B\).  Dispersion
after Cauchy has the same effect.  Therefore the two lawful choices are:
erase the fixed chirp and keep the deficit, or retain it and return by
(R82.16).

## 4. First doubtful or unproved step

Let \(\mathcal K_H^{\rm reg}\) denote (R82.8) after first decomposing
the transformed row into the perfect-square/fourth-power support and its
complement, bounding the sparse subrow as in Section 5, and retaining the
complement.  For the retained odd leading term, the first genuinely
unsupported signed assertion is

\[
 \boxed{\mathcal K_H^{\rm reg}\ll X^\varepsilon Q^4
 \quad(Q^2/B^2\ll H\ll Q^2),}                  \tag{R82.18}
\]

with the actual symbol in (R82.7), not an absolute-value majorant.  The
ordinary benchmark is \(X^\varepsilon BQ^4\), so (R82.18) asks for the
exact missing factor \(B\).  Equation (R82.18) is strictly smaller than
the original off-diagonal: its diagonal, small shifts, sparse
phase-conjugating subsequences, fixed degeneracies, and all other dyadic
shift blocks have been removed.

For the full odd row there is an earlier data gap rather than a disputed
calculation: the packet supplies no energy bound for \(\mathcal R_b\), no
quantitative complete stationary remainder, and no \((b,n)\)-symbol
derivative bounds from which such an energy estimate could be derived.
Thus even a proof of (R82.18) would not by itself certify the full row
using only the stated hypotheses.

For the two even classes, the packet does not specify the cusp
multiplier/local unit, transformed modulus, Kloosterman parameters,
allowed residue classes, Poisson normalization, stationary sign, zero
modes, exceptional moduli, or transformed remainder.  None of these can
be obtained from (R82.3) by sign change or conjugation.  This is why no
odd-class calculation here implies a graph-safe all-class extension.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact row normalization and target | Passed for the conditional complete odd row; the target remains \(J^2/T=JQ\). |
| Odd local unit and Poisson sign | Passed in (R82.3); the reflected alias lives on the reflected \(n\)-branch. |
| Both even cusp classes | Not inferable from the available packet; no test is possible. |
| Global transition flattening versus pointwise remainder | Original transition safety is stated in the packet, but no transformed energy estimate for \(\mathcal R_b\) is supplied. |
| Stationary range and complete lower terms | The range and leading phase/amplitude pass; complete lower terms are unquantified. |
| Diagonal, zero modes, gcds, exceptional moduli | The positive stationary diagonal passes by (R82.13); fixed nonzero \(k\) controls the Weil gcd factor.  The \(n=0\) and nonstationary tails and even-class exceptional moduli remain unquantified. |
| Ordinary-large-sieve capacity | Passed algebraically in (R82.14), with exact deficit \(B\). |
| Phase-sensitive off-diagonal and self-return | Small shifts pass by (R82.15); large shifts are exactly (R82.18).  The one-dimensional chirp transform self-returns by (R82.16).  No short-Hecke assertion is promoted. |
| Smoothness in \((b,n)\) | A size bound suffices for (R82.5) and (R82.15), but the required derivative bounds are absent. |
| Perfect-square/fourth-power and phase conjugation | Passed for the odd leading term by sparse removal.  If \(\mathcal P\) has \(M\) frequencies, Cauchy and Weil give \(E_{\mathcal P}\ll X^\varepsilon M^2JB^2/Q^3\).  Squares have \(M\ll Q\), hence \(E_{\mathcal P}\ll JB^2/Q\ll JQ\); fourth powers are smaller. |
| Source hypotheses/current version | No external theorem or source is used.  The conductor supplied an authorized correction that the level-\(4\) odd spectral decomposition has conductor-dependent centers \(m=LX/4+O(T)\), potentially \(X/4\), \(X/2\), or \(X\), rather than a universal \(X\).  No derivation or conclusion here depends on that locator, and no short-Hecke assertion is promoted. |
| Downstream scope | Restricted to a fixed odd leading component.  No cone, sector, all-class, `M9-M1`, `M9`, or exponent consequence follows. |

## 6. Dependencies and exact artifacts used

The only artifacts read were:

1. `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/briefs/blind_chirped_kloosterman_energy_rederivation.md`;
2. `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/derivation_packet.md`.

No proof graph, strategy file, prior report, sibling report, source card,
or external source was read.  The only additional input was the
conductor's authorized resonance-locator correction recorded in Section
5; it was not accompanied by, and did not cause access to, another
artifact.  Statement-only isolation was preserved.

## 7. Recommended state effect

**Retain as a diagnostic no-go; no shared-state change.**  The exact odd
leading identities and the reduction to (R82.18) may be kept as candidate
evidence, but promotion is blocked by the large-shift signed covariance,
the unquantified transformed errors and symbol derivatives, and the
complete absence of even-class transforms.  No downstream edge should be
promoted.

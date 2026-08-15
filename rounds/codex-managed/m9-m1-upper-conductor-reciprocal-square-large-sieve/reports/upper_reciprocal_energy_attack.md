## 1. Result

There is a genuine, non-self-returning estimate for an initial part of
the upper-conductor range.  Put

\[
 Q=J^{2/5},\qquad T=J/Q=J^{3/5},\qquad B=C/T.
\]

For every fixed compatible nonaxial dual pair, for either endpoint
orientation, and in each of the three local classes
\(c\) odd, \(c\equiv2\pmod 4\), and \(4\mid c\), the complete actual
stationary row satisfies

\[
 \boxed{
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \left(CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\right)
 \ll_\varepsilon X^\varepsilon C Q^{-1/6}}
                                                        \tag{72.D1}
\]

uniformly for

\[
 J^{2/3}\leq C\leq J^{32/45},\qquad b\asymp B,
 \qquad \kappa\in\{1/4,1/2,1\}.
\]

The second inequality uses \(C\geq J^{2/3}=Q^{5/3}\).
Consequently the actual-symbol energy obeys

\[
 \boxed{
 \mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon
 \frac{C^3}{TQ^{1/3}}.}                            \tag{72.D2}
\]

It follows that the frozen target (72.8) is proved whenever

\[
 C^3\leq J^2Q^{1/3},
 \quad\hbox{that is,}\quad
 \boxed{C\leq J^{2/3}Q^{1/9}=J^{32/45}=X^{16/45}.} \tag{72.D3}
\]

The proof keeps the incomplete-Fresnel entry/exit factors and the exact
Farey neighbors.  The key point is that after fixing \(c\) modulo
\(4b\), every arithmetic local unit is constant and the remaining
oscillation is \(e(\pm A_{\kappa,b}/c)\).  Along the resulting
progression its third derivative has the scale

\[
 A_{\kappa,b}b^3/C^4\asymp J^2/T^4=Q^{-1}.
\]

The Farey-neighbor symbol does not cost a hidden factor \(J/C\): each
residue progression splits into \(O(J/C)=O(Q/B)\) smooth pieces, and the
linear and square-root terms in the third-derivative estimate are summed
separately across those pieces.  This is what produces the two displayed
terms in (72.D1).

The two surviving axes and all nonstationary dual tails are also
target-safe in the new range by two integrations by parts in the
accepted three-variable integral.  Therefore every exact
fixed-smooth-interior conductor block in the strict new interval

\[
 J^{2/3}<C\leq J^{32/45}
 \quad\left(X^{1/3}<C\leq X^{16/45}\right)          \tag{72.D4}
\]

is \(J^{1/2}X^\varepsilon\)-safe, including both endpoint
orientations, all three parity classes, transitions, and axes.  The
remaining nonaxial survivor is
\(J^{32/45}<C\leq J\).  No estimate for that survivor, the full cone,
\(M9\! -\! M1\), or the Gauss-circle exponent is asserted.

## 2. Exact statement and hypotheses

The antecedent is the exact order-\(J\) Farey stationary decomposition
accepted in Round 71.  In particular:

* \(X>1\) is real, \(J=X^{1/2}\), \(Q=X^{1/5}=J^{2/5}\), and
  \(T=J/Q\);
* \(c\asymp C\), \(b\asymp C/T\), and \((b,c)=1\);
* the two offset-Poisson aliases and the half-open, neighbor-dependent
  Farey intervals are retained;
* \(k=\rho\sigma>0\) is one member of the compatible finite
  nonaxial dual family; and
* all coefficient arrays below are the actual stationary symbols, not
  arbitrary bounded arrays.

It is useful to write all three local phases uniformly.  Put

\[
 \kappa=\frac{c}{[c,4]}\in\{1/4,1/2,1\},\qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2
 =bX+2J\sqrt{\kappa k}+\frac{\kappa k}{b}.          \tag{72.D5}
\]

For odd \(c\), \(\kappa=1/4\), and this is exactly the packet's
\(A_b\).  Apart from its fixed Gaussian and character unit, the row is

\[
 \sum_{\substack{c\asymp C\\(c,4b)=1}}
 a_{b,c,k}^{(1/4)}e_{4b}(k\bar c)e(-A_{1/4,b}/c).  \tag{72.D6}
\]

For \(c\equiv2\pmod4\), let \(s_0\) be the representative used by the
exact local formula and write

\[
 bs_0+\rho=t c.
\]

Then

\[
 \chi_4(s_0)e_{2c}(\sigma s_0)
 =\chi_4(s_0)e_{2b}(\sigma t)
   e\!\left(-\frac{k}{2bc}\right),                \tag{72.D7}
\]

and the stationary real phase contributes
\(e(-(bX+\sqrt{2k}J)/c)\).  Thus the complete oscillatory part is a
local unit times \(e(-A_{1/2,b}/c)\).  Likewise, when \(4\mid c\),

\[
 \chi_4(s_0)e_c(\sigma s_0)
 =\chi_4(s_0)e_b(\sigma t)
   e\!\left(-\frac{k}{bc}\right),                 \tag{72.D8}
\]

and the stationary phase \(e(-(bX+2\sqrt{k}J)/c)\) gives
\(e(-A_{1,b}/c)\).  On a fixed residue class \(c\pmod{4b}\), the
integer \(t\), the value \(s_0\pmod4\), and every unit in
(72.D7)--(72.D8) are fixed.  This follows from
\(tc\equiv\rho\pmod b\) and from the choice \(0\leq s_0<c\).
The opposite endpoint orientation gives the conjugate sign or the
corresponding oriented \(A_{\kappa,b}\); its third derivative has the
same magnitude.

After the common factor \(T/\sqrt{CJ}\) is removed, the actual symbols
in (72.D6)--(72.D8) are \(O_\varepsilon(X^\varepsilon)\).  The only
non-smooth dependence on \(c\) is the explicitly retained change of a
Farey neighbor.  On an interval on which both neighbors are fixed as
linear functions of \(c\), the symbol has bounded variation
\(O_\varepsilon(X^\varepsilon)\) in the progression variable.  This
seminorm statement is proved below from the exact neighbor equations;
it is not an arbitrary-weight hypothesis.

## 3. Proof or derivation

### Exact energy and its diagonal

For the odd class, direct expansion of (72.D6) gives

\[
\begin{aligned}
 \mathcal E_{C,k}^{(1/4)}
 =\sum_{b\asymp B}
 \sum_{\substack{c_1,c_2\asymp C\\
                  (c_1c_2,4b)=1}}
 &a_{b,c_1,k}^{(1/4)}
  \overline{a_{b,c_2,k}^{(1/4)}}\\
 &\times e_{4b}\!\left(k(\bar c_1-\bar c_2)\right)
 e\!\left(-A_{1/4,b}
       \left(\frac1{c_1}-\frac1{c_2}\right)\right).
                                                               \tag{72.D9}
\end{aligned}
\]

This is (72.10), with no absolute value inserted in its off-diagonal.
The diagonal is

\[
 \mathcal E_{\rm diag}
 =\sum_{b\asymp B}\sum_{c\asymp C}|a_{b,c,k}|^2
 \ll_\varepsilon X^\varepsilon BC.               \tag{72.D10}
\]

The two even expansions are identical after the constant local units
from (72.D7)--(72.D8) are inserted.  The estimate below is first made
on the signed row.  Only after that cancellation has been proved do we
square and sum in \(b\).  In particular the off-diagonal of (72.D9) is
not estimated by the number of pairs.

### Residue progressions and the exact neighbor partition

Fix \(b\asymp B\), a parity class, and a residue
\(r\pmod{4b}\) allowed by that class and by \((b,c)=1\).  Write

\[
 c=r+4b\ell.
\]

The odd inverse factor and all odd characters are constant on this
progression.  Equations (72.D7)--(72.D8) show the same for both even
classes.  Hence the only rapid phase on it is

\[
 f(\ell)=\pm\frac{A_{\kappa,b}}{r+4b\ell}.         \tag{72.D11}
\]

There are \(O(b)=O(B)\) allowed residue classes.  The total number of
\(\ell\)'s in each is \(O(C/b)=O(T)\).

Let \(a_-/c_-\) and \(a_+/c_+\) be the left and right Farey neighbors
of \(b/c\) at order \(\lfloor J\rfloor\).  The determinant equations
are

\[
 bc_- -a_-c=1,
 \qquad
 a_+c-bc_+=1.                                     \tag{72.D12}
\]

For the alias at the other endpoint these are the same equations after
reflection \(a/c\mapsto1-a/c\); the symbols \(a_\pm\) below then mean
the corresponding small reflected neighbor numerators.

In the scoped range \(c\ll J^{32/45}=o(J)\).  Hence the condition
\(J-c<c_\pm\leq J\) implies \(c_\pm\asymp J\), and therefore

\[
 a_\pm\asymp \frac{bJ}{c}\asymp Q,               \tag{72.D13}
\]

while (72.D12) fixes \(a_-\) and \(a_+\) in one residue class modulo
\(b\) once \(c\pmod b\) is fixed.  As \(c\) runs on one of the
progressions above, each of \(a_-\) and \(a_+\) therefore takes only

\[
 O(1+Q/b)=O(Q/B)=O(J/C)                            \tag{72.D14}
\]

values.  Cutting at the union of their change points gives
\(R_b=O(Q/B)\) half-open pieces.  On each piece

\[
 c_-=(a_-c+1)/b,
 \qquad c_+=(a_+c-1)/b,                            \tag{72.D15}
\]

so the exact transition endpoints

\[
 z_-=-\frac{Jb}{(a_-+b)c+1},
 \qquad
 z_+= \frac{Jb}{(a_++b)c-1}                       \tag{72.D16}
\]

are smooth.  A piece has \(c\)-length
\(O(Cb/Q)\), hence at most \(O(C/Q)\) terms of its
\(4b\)-progression.

This partition has no hidden transition loss.  Put \(\Lambda=J/c\).
The incomplete-Fresnel arguments are of the form
\(\sqrt\Lambda(z_\pm-z_*)\), where \(z_*\) is fixed by
\((\rho,\sigma,\kappa)\).  Their total change on one neighbor-fixed
piece is

\[
 \ll \frac{b\sqrt\Lambda}{Q}
 \asymp \frac{B}{Q}\sqrt{\frac JC}
 =\sqrt{\frac CJ}\leq1.                           \tag{72.D17}
\]

The incomplete Fresnel function and its first derivative are bounded,
including when the saddle enters or leaves the half-open interval.
Every other factor in the actual symbol is either constant on the
residue progression or is a fixed smooth function of
\(c/C\), \(Tb/c\), \(c/J\), and the stationary ratios.  Its total
variation on the same piece is \(O(1)\).  Thus, after division by the
common normalization already used in (72.4), each neighbor-fixed
weight \(w_i(\ell)\) satisfies

\[
 \|w_i\|_\infty+\int|w_i'(u)|\,du
 \ll_\varepsilon X^\varepsilon.                  \tag{72.D18}
\]

Sharp half-open endpoints merely begin or end a piece; singleton and
incomplete final progressions are included below.

### The third-derivative estimate

The precise elementary estimate used here is the following weighted
third-derivative lemma.  If \(I\) is an integer interval of length
\(L\), \(f'''\) has one sign and
\(\lambda\asymp|f'''|\) on \(I\), and
\(\|w\|_\infty+\int_I|w'|\leq V\), then

\[
 \left|\sum_{n\in I}w(n)e(f(n))\right|
 \ll V\left(L\lambda^{1/6}
       +L^{1/2}\lambda^{-1/6}+1\right).            \tag{72.D19}
\]

For completeness, when \(L^{-3}\leq\lambda\leq1\), apply van der
Corput differencing with \(H=\lfloor\lambda^{-1/3}\rfloor\).  For
\(g_h(x)=f(x+h)-f(x)\),
\(|g_h''(x)|\asymp h\lambda\), so the second-derivative estimate gives

\[
 \sum e(g_h(n))
 \ll L(h\lambda)^{1/2}+(h\lambda)^{-1/2}.
\]

The differencing inequality consequently yields

\[
 |S|^2
 \ll \frac{L^2}{H}
    +L^2\lambda^{1/2}H^{1/2}
    +L\lambda^{-1/2}H^{-1/2},
\]

which is (72.D19).  If \(\lambda<L^{-3}\) or \(\lambda>1\), the
trivial estimate is already bounded by the right-hand side.  Abel
summation supplies the factor \(V\).  This proof explicitly keeps the
zero shift as the diagonal; every nonzero near-diagonal shift is
controlled by the displayed second-derivative estimate.

For (72.D11), uniformly on \(c\asymp C\),

\[
 |f'''(\ell)|
 \asymp \frac{A_{\kappa,b}b^3}{C^4}
 \asymp \frac{b^4J^2}{C^4}
 \asymp \frac{J^2}{T^4}
 =Q^{-1}.                                         \tag{72.D20}
\]

Here \(A_{\kappa,b}\asymp bJ^2\) uniformly for the finite dual
family.  Notice that (72.D20) uses no Diophantine condition on \(X\),
\(J\), or \(A_{\kappa,b}\).

Let the lengths of the neighbor-fixed pieces on one residue progression
be \(L_i\).  Then \(\sum_iL_i\ll T\),
\(\#\{i\}\ll R_b=Q/B\), and (72.D18)--(72.D20) give

\[
\begin{aligned}
 \sum_i\left|\sum_{\ell\in I_i}
       w_i(\ell)e(f(\ell))\right|
 &\ll_\varepsilon X^\varepsilon
 \left(TQ^{-1/6}
  +Q^{1/6}\sum_iL_i^{1/2}+R_b\right)\\
 &\ll_\varepsilon X^\varepsilon
 \left(TQ^{-1/6}
  +Q^{1/6}\sqrt{TQ/B}+Q/B\right).                 \tag{72.D21}
\end{aligned}
\]

This is the exact point at which the apparent \(Q/B\) transition loss
is avoided: the first term is summed using \(\sum L_i=T\), and the
second by Cauchy using
\(\sum L_i^{1/2}\leq\sqrt{R_bT}\).  We never multiply the
full-progression bound by the number of neighbor pieces.

There are \(O(B)\) residue progressions.  Multiplying (72.D21) by this
number gives

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \left(CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\right).          \tag{72.D22}
\]

Since \(C\geq Q^{5/3}\), both the second and third terms are bounded by
the first.  This proves (72.D1) for all three local classes and both
orientations.  Restricting to allowed gcd or parity residues only
decreases the number of progressions; no Moebius inversion or gcd loss
has been used.

### Energy, first moment, and the new conductor boundary

Squaring (72.D1) only after its signed cancellation has been obtained,
and then summing over \(b\asymp B\), gives

\[
 \mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon
 B C^2Q^{-1/3}
 =X^\varepsilon\frac{C^3}{TQ^{1/3}},              \tag{72.D23}
\]

which proves (72.D2).  Together with (72.D10), it also gives the signed
off-diagonal control
\(|\mathcal E_{\rm off}|\leq
\mathcal E+\mathcal E_{\rm diag}\) at the same target scale in the
range below.  Thus the diagonal and near-diagonal have not been
silently discarded.

The right side of (72.D23) is at most \(J^2/T\) precisely when

\[
 C\leq J^{2/3}Q^{1/9}.
\]

Using \(Q=J^{2/5}\) gives \(J^{32/45}\), and using \(J=X^{1/2}\)
gives \(X^{16/45}\).  Cauchy's inequality now yields

\[
 \left|\sum_{b\asymp B}S_{b,k}^{(\kappa)}(C)\right|
 \leq B^{1/2}\mathcal E_{C,k}^{1/2}
 \ll_\varepsilon X^\varepsilon\frac{J\sqrt C}{T}. \tag{72.D24}
\]

After multiplication by the exact outer coefficient
\(T/\sqrt{CJ}\), (72.D24) is \(J^{1/2}X^\varepsilon\).

### Axes, tails, and finite families

The odd \(\rho=0\) axis and the \(4\mid c,\sigma=0\) axis have no
three-variable saddle.  The accepted integration-by-parts estimate is
\(\mathcal J_{\rm axis}\ll_A\Lambda^{1-A}\).  Taking \(A=2\), using
the local prefactor \(T/C\), and counting \(O(CB)\) incidences gives

\[
 \mathcal D_C^{\rm axis}
 \ll_\varepsilon X^\varepsilon
 CB\frac TC\Lambda^{-1}
 =X^\varepsilon\frac{C^2}{J}.                     \tag{72.D25}
\]

For \(C\leq J^{32/45}\), this is at most
\(J^{19/45}X^\varepsilon<J^{1/2}X^\varepsilon\).
The same summed integration by parts treats the large dual tails and
nonstationary finite cells.  Higher stationary terms either belong to
the complete actual symbols controlled above or carry an additional
power of \(\Lambda^{-1}\), so they are smaller in (72.D4).
The compatible nonzero \((\rho,\sigma)\) family, the two aliases, and
the local orientations are fixed or divisor-bounded; summing them costs
only \(X^\varepsilon\).

Finally, the support separated from zero forces
\(b\asymp C/T\).  In the new range
\(b\gg J^{1/15}\), so no \(b=O(1)\) stationary row is present.
Any compact-cutoff endpoint is already an incomplete progression in
(72.D21), not a separate error.

## 4. First doubtful or unproved step

The first unproved estimate is now the same actual-symbol energy for

\[
 J^{32/45}<C\leq J.                                \tag{72.D26}
\]

The third-derivative mechanism gives only the uniform saving
\(Q^{1/6}\).  To meet (72.8) above (72.D3), one needs an additional
factor

\[
 \frac{C^{3/2}}{JQ^{1/6}}
\]

beyond (72.D1), on average or in the first moment.  Repeating Poisson
summation in \(c\) and the matching \(B\)-process is the already proved
self-return and does not supply it.

There is a more specific but still unproved spectral interface.  Odd
reciprocity gives exactly

\[
 e_{4b}(k\bar c)e(-A_{1/4,b}/c)
 =e_c(-k\overline{4b})
  e\!\left(-\frac{bX+J\sqrt k}{c}\right).          \tag{72.D27}
\]

Writing \(X=N+\vartheta\) and formally completing a smooth
neighbor-fixed \(b\)-piece modulo \(c\) produces a length-\(T\) family

\[
 \frac1c\sum_{|h|\ll T}
 \widehat W_c(h/c)
 S(h-N,-k\bar4;c)e(-J\sqrt k/c),                  \tag{72.D28}
\]

with the exact level-four cusp normalization still to be supplied.
The external phase in (72.D28) is matched to one large-argument Bessel
branch.  Even in an ideally separated model, full closure would require
a uniform short spectral Fourier-coefficient estimate at the
\(X^{1/4+\varepsilon}\) scale for an interval of length
\(T=X^{3/10}\), uniformly over the effective spectral range, together
with the moving Farey-transition weights.  That is not proved here.
The exact level-four trace formula, the neighbor-coupled transform, the
two even cusps, and the axes must all be audited before (72.D28) can be
used.  Thus (72.D28) is a sharply named next interface, not evidence for
the missing range.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Energy normalization | Pass: (72.D9)--(72.D10) retain the exact diagonal; (72.D23) meets \(J^2/T\) exactly at \(C=J^{32/45}\). |
| Diagonal and near-diagonal | Pass: the zero differencing shift is the diagonal, and every nonzero shift is controlled by the second-derivative estimate inside the proof of (72.D19). No pairwise absolute-value bound is used. |
| Actual symbol | Pass: the proof uses the exact neighbor equations and establishes the piecewise bounded-variation norm (72.D18); it does not allow arbitrary phase-conjugating coefficients. |
| Farey transitions | Pass: there are \(O(Q/B)\) pieces per residue; (72.D21) shows explicitly how they sum without a hidden \(Q/B\) loss. Incomplete-Fresnel entry and exit are retained. |
| \(b\)-endpoints | Pass: \(b\asymp C/T\gg J^{1/15}\) in the new range. Half-open and singleton progression endpoints are included in (72.D19)--(72.D21). |
| Perfect squares and fourth powers | Pass: (72.D20) depends only on \(A_{\kappa,b}\asymp bJ^2\). The differencing proof is uniform when first or second derivatives are integral or resonant, so exact-square and fourth-power centers require no deletion. |
| Even local classes | Pass: (72.D7)--(72.D8) give their exact reciprocal-square phases and show that their units are constant on \(c\pmod{4b}\). |
| Axes | Pass in the promoted subrange: (72.D25) is \(O(J^{19/45+\varepsilon})\). No axis is claimed closed at \(C\asymp J\). |
| Gcd factors | Pass: only admissible residue progressions are retained. Their number is at most \(4b\), and no completion or Moebius inversion introduces a gcd multiplier. |
| Finite dual and error sums | Pass: compatible stationary pairs are finite/divisor-bounded, and accepted nonstationary tail integration is summable. |
| Self-return avoidance | Pass: the proof is a third-derivative estimate on the original residue progressions; it does not perform \(c\)-Poisson followed by the inverse \(B\)-process. |
| Global exponent | Pass: the result is only a fixed-interior conductor extension to \(X^{16/45}\). It is not the original global \(X^{1/20}\) signed gain. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts/sources used

The proof uses only the following assigned artifacts:

* `protocol.md`;
* `state/proof_obligations.yml`, restricted to the active M9-M1
  obligations and recorded Round-70/71 obstructions;
* `state/active_campaign.yml`;
* `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/briefs/upper_reciprocal_energy_attack.md`;
* `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/derivation_packet.md`;
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/synthesis.md`;
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reviews/conductor_round71_adjudication.md`; and
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/conductor_farey_stationary_low_conductor.md`.

The second- and third-derivative estimates are derived explicitly in
Section 3.  No external theorem or web source is imported, and the
spectral discussion (72.D27)--(72.D28) is explicitly not used in the
proved subrange.

## 7. Recommended state effect

Promote a scoped internal lemma recording (72.D1)--(72.D3), and extend
the exact fixed-interior target-safe Farey range from

\[
 T\leq C\leq J^{2/3}
\]

to

\[
 \boxed{T\leq C\leq J^{32/45}=X^{16/45}}.
\]

The promoted statement should explicitly include the exact Farey
neighbors, incomplete-Fresnel transitions, both endpoint orientations,
the two even classes, both surviving axes, gcd restrictions, and the
finite dual/error sums.  Revise the open upper-conductor survivor to
\(J^{32/45}<C\leq J\).  Retain (72.D28) only as an unproved next
interface requiring a level-four seam audit and an
\(X^{1/4+\varepsilon}\)-scale short spectral coefficient bound.

Do not promote the complete fixed-interior wavelet,
\(M9\! -\! M1\), \(M9\), or any Gauss-circle exponent.

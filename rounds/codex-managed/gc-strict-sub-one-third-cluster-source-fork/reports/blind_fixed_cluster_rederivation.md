# 1. Result

The normalizations (95.1)--(95.9) are consistent. In particular,
\(W=Y^{7/16}\) and the cluster target
\(\mathcal C(c)\ll_\varepsilon Y^{1/2+\varepsilon}\) give square mass
\(Y^{15/16+\varepsilon}\), hence the pointwise exponent \(5/16\); the
other term in the persistence bridge has only exponent \(1/4\). The
band occupies \(Y^{5/48}\) cells, and the M2 determinant threshold is
exactly four times the M1 threshold.

The fixed-cluster estimate does **not** follow from the information in
the derivation packet by reduced-fraction grouping, raw diagonal
control, a standard large sieve, cellwise Cauchy, or formal
\(\chi_4\)-orthogonality. Reduced-fraction grouping is exact but leaves
equal-frequency lift cross terms. Even after those are controlled, it
leaves the following literal signed near-frequency correlation:

\[
 \mathcal R_j(c)=
 \sum_{\substack{r\ne s\\ |r-s|<\kappa_j/W}}
 \left(1-\frac{W}{\kappa_j}|r-s|\right)
 A_{j,r}(c)\overline{A_{j,s}(c)}
 e\!\left(\frac{(r-s)c}{\kappa_j}\right),
 \qquad (\kappa_1,\kappa_2)=(1,4),
 \tag{R}
\]

where \(A_{j,r}\) is the sum of the **literal** coefficients over all
indices with signed reduced ratio \(r\). No arithmetic absolute value
has been inserted. The packet does not give the coefficient formula
or even identify the coordinate on which \(\chi_4\) lies, so neither
the equal-lift part nor (R) can be estimated from the permitted data.

If the total clustered expression is \(O(Y^{\gamma+\varepsilon})\),
its pointwise capacity through (95.1) is

\[
 \Theta(\gamma)=
 \max\left\{\frac{7/16+\gamma}{3},\frac{\gamma}{2}\right\}.
 \tag{C}
\]

Thus \(\gamma=1/2\) gives \(5/16\), while any
\(\gamma<9/16\) gives a strict exponent below \(1/3\). Writing
\(\gamma=9/16-\delta\), the resulting exponent is
\(1/3-\delta/3\). Standard spacing arguments lose
\(D^2/W=Y^{9/16}\) over the grouped diagonal energy and therefore do
not furnish such a bound from nondecaying energy.

# 2. Exact statement and hypotheses

Let \(j\in\{1,2\}\), put \(\kappa_1=1,\kappa_2=4\), and let
\(\mathscr I_j\) be the finite raw index multiset of one literal fixed
stratum. An index \(\xi\) retains its sign \(\sigma_\xi\), integers
\(h_\xi,d_\xi\), profile, floor, hard-top prefix, star convention, and
the literal \(\chi_4\) placement. Denote its entire unmodified
coefficient by \(a^{\rm lit}_{j,\xi}(c)\), and set

\[
 r_\xi=\frac{\sigma_\xi h_\xi}{d_\xi},\qquad
 \lambda_\xi=\frac{r_\xi}{\kappa_j},\qquad
 K(u)=(1-|u|)_+.
\]

No formula or size hypothesis for \(a^{\rm lit}_{j,\xi}\) is present
in the packet. In particular, this report does not replace it by an
arbitrary bounded coefficient, does not move \(\chi_4\) between
coordinates, and does not identify the M1 and M2 arrays.

For each signed reduced ratio \(r\), define the exact lift aggregate

\[
 A_{j,r}(c)=\sum_{\substack{\xi\in\mathscr I_j\\r_\xi=r}}
 a^{\rm lit}_{j,\xi}(c).
\]

If \(r=\sigma p/q\) with \((p,q)=1\), the indices in this sum have
\((h,d)=(kp,kq)\). The common factor \(1/4\) in M2 changes the
frequency but not which pairs are equal-frequency lifts. The exact
cell energy is

\[
 \mathcal C_j(c)=\mathcal D_j(c)+\mathcal R_j(c),
 \qquad
 \mathcal D_j(c)=\sum_r|A_{j,r}(c)|^2,
 \tag{D}
\]

with \(\mathcal R_j\) given by (R). Equivalently,

\[
 \mathcal D_j=
 \underbrace{\sum_{\xi}|a^{\rm lit}_{j,\xi}|^2}_{
 \mathcal D^{\rm raw}_j}
 +
 \underbrace{\sum_{\substack{\xi\ne\eta\\r_\xi=r_\eta}}
 a^{\rm lit}_{j,\xi}\overline{a^{\rm lit}_{j,\eta}}}_{
 \mathcal E_j}.
 \tag{E}
\]

The second sum in (E) is ordered. It contains every exact-frequency
cross term and need not have a sign. Consequently a bound for the raw
diagonal alone is not a bound for \(\mathcal D_j\). The earliest atomic
coefficient-dependent obligation is control of
\(\mathcal D_j^{\rm raw}\) together with \(\mathcal E_j\), equivalently
of \(\mathcal D_j\); conditional on that, (R) is the smallest remaining
unequal-frequency obligation.

The block-count and spacing controls below additionally use the
displayed minimax-block hypothesis \(h\asymp L=Y^{1/6}\) and
\(d\asymp D=Y^{1/2}\). They are controls on what follows from this
geometry, not extra information about the omitted literal
coefficients.

# 3. Proof or derivation

**(95.1)--(95.3).** Equation (95.1) is the accepted bridge in the
packet. With \(W=Y^{7/16}\),

\[
 WY^{1/2}=Y^{7/16+8/16}=Y^{15/16}.
\]

Substitution into (95.1) gives

\[
 Q^{1/3}\ll Y^{(15/16)/3+\varepsilon}=Y^{5/16+\varepsilon},
 \qquad
 (Q/W)^{1/2}\ll Y^{(1/2)/2+\varepsilon}=Y^{1/4+\varepsilon}.
\]

The first term dominates, proving precisely the implication
(95.2)\(\Rightarrow\)(95.3).

**(95.4).** Write
\(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\). If \(I\) is centered
at \(c\) and has length \(W\), then

\[
 1_I(t)\leq \frac{\pi^2}{4}
 \operatorname{sinc}^2\!\left(\frac{t-c}{W}\right),
\]

because \(|(t-c)/W|\leq1/2\) on \(I\) and
\(|\operatorname{sinc}(x)|\geq2/\pi\) there. Fourier expansion and
the transform of \(\operatorname{sinc}^2\) give

\[
 \int_{\mathbb R}|S(t)|^2
 \operatorname{sinc}^2\!\left(\frac{t-c}{W}\right)dt
 =W\sum_{\lambda,\mu}a_\lambda\overline{a_\mu}
 e((\lambda-\mu)c)K(W(\lambda-\mu)).
 \tag{F}
\]

For the shifted cells in the packet,

\[
 \int_0^1\sum_\nu
 1_{C_{\nu,\vartheta}}(\lambda)1_{C_{\nu,\vartheta}}(\mu)\,d\vartheta
 =K(W(\lambda-\mu)),
 \tag{G}
\]

since two points at scaled distance \(u\) lie in the same random unit
cell for a proportion \((1-|u|)_+\) of shifts. Expanding the cell
square in (G) identifies the sum in (F) with the right side of (95.4).
Equal frequencies have kernel \(K(0)=1\), so all their cross terms
remain.

**(95.5)--(95.7).** For M1, \(\kappa_1=1\) gives the literal frequency
\(h/d\); for M2, \(\kappa_2=4\) gives \(h/(4d)\). Although a change of
scale relates their geometric kernels, it does not relate their
coefficient arrays or their \(\chi_4\) placements, so it cannot
relabel M1 as M2. By (95.4), the bound
\(\mathcal C_j(c)\ll Y^{1/2+\varepsilon}\) yields interval square mass

\[
 \ll W Y^{1/2+\varepsilon}=Y^{15/16+\varepsilon}.
\]

For \(B=O(\log Y)\) fixed-symbol pieces, regard the random cell sums
as vectors in \(L^2([0,1]\times\mathbb Z)\). The triangle inequality
gives

\[
 \mathcal C\!\left(\sum_{b\leq B}S_b\right)^{1/2}
 \leq\sum_{b\leq B}\mathcal C(S_b)^{1/2},
\]

so assembly costs at most \(B^2\), absorbed by \(Y^\varepsilon\).
Splitting at the \(O(1)\) symbol changes per height is equally
harmless. A pointwise \(O(Y^{1/4+\varepsilon})\) remainder has square
mass \(O(WY^{1/2+\varepsilon})\), and its cross term is handled by
Cauchy. This rederives why the fixed-stratum target is (95.7).

**(95.8)--(95.9).** A band of diameter \(O(Y^{-1/3})\) meets

\[
 W Y^{-1/3}=Y^{7/16-1/3}
 =Y^{21/48-16/48}=Y^{5/48}
\]

cells, up to endpoint constants. For M1,

\[
 \left|\frac hd-\frac{h'}{d'}\right|<W^{-1}
 \iff |hd'-h'd|<\frac{dd'}W.
\]

For M2,

\[
 \left|\frac h{4d}-\frac{h'}{4d'}\right|<W^{-1}
 \iff |hd'-h'd|<\frac{4dd'}W.
\]

Thus an unequal pair has a nonzero integer determinant in the range

\[
 1\leq |hd'-h'd|<\frac{\kappa_jdd'}W
 \asymp \kappa_jY^{9/16}.
 \tag{H}
\]

This is a polynomially long determinant range, not merely the
equal-fraction or adjacent-Farey case.

**What the elementary operations leave.** Distinct reduced ratios
with denominators \(O(D)\) have separation \(\gg D^{-2}\); M2 scales
this by \(1/4\). Hence a cell can contain

\[
 O\!\left(1+\frac{\kappa_jD^2}{W}\right)=O(Y^{9/16})
\]

distinct grouped frequencies. Cellwise Cauchy, the spacing form of
the large sieve, or a Schur bound for the triangular Gram matrix all
give only

\[
 \mathcal C_j(c)
 \ll\left(1+\frac{\kappa_jD^2}{W}\right)\mathcal D_j(c).
 \tag{I}
\]

The continuous large sieve on the \(t\)-interval gives the same
\(W+\kappa_jD^2\) loss; (95.4) cannot be reversed to improve it. If
\(\mathcal D_j\ll Y^{\eta+\varepsilon}\), (I) has cluster exponent at
best \(\gamma=\eta+9/16\). For any nondecaying polynomial energy
\(\eta\geq0\), this reaches no strict sub-one-third capacity in (C).

Finally, the random shift averages only cell boundaries. It does not
average a free residue-class variable. In (R) the determinant
restriction couples both character-bearing coordinates, the profile,
and the rational phase. Formal character orthogonality therefore
does not make (R) vanish. Any successful estimate would have to use
the missing literal coefficient formula and prove cancellation in
the incomplete signed determinant sum (R); that is a new arithmetic
estimate, not an elementary consequence of the packet.

# 4. First doubtful or unproved step

The first unsupported step would be

\[
 \sum_r\left|\sum_{\xi:r_\xi=r}
 a^{\rm lit}_{j,\xi}(c)\right|^2
 \ll_\varepsilon Y^{1/2+\varepsilon}.
 \tag{J}
\]

A raw diagonal estimate does not prove (J), because the lift
correlation \(\mathcal E_j\) in (E) is still present. At
\(h\asymp Y^{1/6}\), \(d\asymp Y^{1/2}\), a reduced ratio \(p/q\) can
have polynomially many common lifts \((kp,kq)\); Cauchy over those
lifts can therefore incur a polynomial, not automatically
logarithmic, loss. The precise Vaaler coefficient and the literal
\(\chi_4\) coordinate could change this conclusion, but neither is
supplied.

If (J) is supplied independently, the first remaining unproved step
is

\[
 |\mathcal R_j(c)|\ll_\varepsilon Y^{1/2+\varepsilon}
 \quad\text{(or at least }Y^{9/16-\delta+\varepsilon}
 \text{ for some }\delta>0\text{)},
 \tag{K}
\]

uniformly in \(c\), with (R) interpreted separately for M1 and M2.
The second alternative in (K), together with the same bound for
\(\mathcal D_j\), has pointwise capacity \(1/3-\delta/3\). No step in
the permitted packet proves either (J) or (K).

# 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Exponent \(5/16\) and local mass | Passed: \(7/16+1/2=15/16\), \((15/16)/3=5/16\), and the second bridge term is \(1/4\). |
| M1 versus M2 frequency | Passed: \(\kappa_1=1\), \(\kappa_2=4\); M2 has kernel \(K(W(r-s)/4)\) and determinant threshold \(4dd'/W\). No coefficient relabelling was made. |
| Exact equal-frequency lifts | Unresolved from the packet: all \((kp,kq)\) lifts are aggregated in \(A_{j,r}\), and their cross terms are exactly \(\mathcal E_j\). |
| Raw diagonal mass | Insufficient by itself: \(\mathcal D_j=\mathcal D^{\rm raw}_j+\mathcal E_j\). The packet supplies no numerical bound for either coefficient expression. |
| Near but unequal rational frequencies | Isolated exactly as (R), equivalently by the nonzero determinant range (H). The range has size exponent \(9/16\). |
| Both signs | Retained in the signed ratio \(r_\xi\). Under the displayed positive block \(h\asymp L\), opposite-sign frequencies are separated by \(\gg L/D=Y^{-1/3}\gg\kappa_j/W\), so they do not share cells for large \(Y\); the two same-sign correlations remain separate unless an omitted coefficient identity relates them. |
| Literal \(\chi_4\) placement | Not auditable beyond retention: the packet says there is a correct coordinate but does not name it. Expanding it as \(\chi_4(h)\) or \(\chi_4(d)\) would be an unsupported assumption. Accordingly, no orthogonality claim is certified. |
| \(Y^{5/48}\) cells | Passed: the band diameter divided by cell width is \(Y^{-1/3}/Y^{-7/16}=Y^{5/48}\). |
| Unsigned/adversarial control | Failed, as required: for a full one-sign rectangular block there are \(N\asymp DL=Y^{2/3}\) raw terms in \(O(K)\), \(K=Y^{5/48}\), cells. Choosing bounded coefficients so that \(a_\xi e(\lambda_\xi c)=1\), cellwise Cauchy in reverse gives, for every shift, \(\sum_\nu n_\nu^2\geq N^2/O(K)=Y^{59/48}\). This is \(Y^{9/16}\) times the raw \(\ell^2\)-mass \(N=Y^{32/48}\). The same adversarial construction can be restricted to one nonzero residue class modulo \(4\), so merely attaching, or then taking absolute values of, \(\chi_4\) does not change these exponents. This falsifies a geometry-only or unsigned target, but says nothing adverse about the actual signed coefficients. |
| All-block/logarithmic assembly | Passed conditionally: \(O(\log Y)\) fixed pieces cost at most \(O((\log Y)^2)\) in the cell Hilbert norm and are absorbed in \(Y^\varepsilon\). This does not supply the missing one-block estimate. |
| Canonical-core implication | Failed as a logical implication: even a proof of (95.7) would yield only the fixed-\(W\) \(5/16\) result through (95.1). No implication to either canonical endpoint core or to the quarter target is present. Conversely, the present no-go does not refute either core. |

# 6. Dependencies and exact artifacts used

The only mathematical artifact used was:

- rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/derivation_packet.md (starting graph hash printed there: e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104).

The task instructions were read from:

- rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/briefs/blind_fixed_cluster_rederivation.md.

No proof graph, proof draft, strategy file, source card, prior report,
candidate, review, synthesis, sibling Round-95 file, web source, or
external computation was read or used.

# 7. Recommended state effect

**No change.** Retain (95.1)--(95.9) as a consistent reduction and
retain (95.7) as open; do not promote the fixed-cluster estimate. For
the next internal attempt, expose the full literal coefficients first
and split the obligation into the exact-lift bound (J) and the signed
near-unequal correlation bound (K), separately for M1 and M2. The
unsigned \(Y^{9/16}\)-loss control should be retained as a
falsification test for any proposed elementary proof.

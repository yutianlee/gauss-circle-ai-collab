# Round 144 conductor candidate: completed Appell scalar, sharper cells, and reciprocal self-return

Campaign: `m9-m1-lower-cone-indefinite-theta-completion-gate`  
Starting graph SHA-256: `179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204`

## 1. Result and decision

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 \mathcal I_M=[M,2M)\cap[1,M_*],\qquad M_*\asymp R^2,
\tag{144.C1}
\]

Fix the inherited collar parameter \(0<\rho<1/8\); constants in the
floor-to-cone equivalence may depend on \(\rho\) and \(V\).

\[
 C(m)=\sum_{\substack{hr=m\\r\ \mathrm{odd}\\r>4h}}\chi _4(r),
 \qquad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
 \qquad j_m=k_m^2-Nm.
\tag{144.C2}
\]

Round 144 proves three statements, only one of which is a new
arithmetic support reduction.

First, the Round-141 displacement count sharpens.  For every real
\(J\geq1\), uniformly on every active block,

\[
 \#\{m\in\mathcal I_M:0<|j_m|\leq J\}
 \ll_\varepsilon JX^\varepsilon .
\tag{144.C3}
\]

The exact-radical channel \(j_m=0\) remains separately target-safe.
More generally, including that channel and allowing \(0\leq J<1\),

\[
 \#\{m\in\mathcal I_M:|j_m|\leq J\}
 \ll_\varepsilon (J+\sqrt M+1)X^\varepsilon.
\tag{144.C3a}
\]

Consequently the accepted scalar has the strictly smaller support
survivor

\[
\boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{144.C4}
\]

This corrects the earlier assertion that the same absolute congruence
method is exhausted at \(J=\sqrt M\).  The exponent \(3/4\) is the
largest polynomial displacement exponent certified by the present
root-count plus divisor-bound ledger.  Formula (144.C4) is a genuine
arithmetic owner reduction, but it does not estimate its survivor.

Second, the exact Round-63 completion admits a new scalar
specialization statement.  Put

\[
 F(\tau)=\sum_{m\geq1}C(m)e(m\tau),\qquad
 \mathcal H(\tau)=\frac12\widehat A_4
 \!\left(\frac12,-3\tau;2\tau\right).
\tag{144.C5}
\]

Then

\[
 \mathcal H(\tau)=F(\tau)+\frac14+
 \sum_{a=0}^{3}\mathcal R_a(\tau),
\tag{144.C6}
\]

\[
 \mathcal R_a(\tau)=\frac{i}{4}(-1)^a
 \vartheta\!\left((2a-3)\tau+\frac32;8\tau\right)
 R_{\rm Zw}\!\left(\frac12+(3-2a)\tau;8\tau\right),
\tag{144.C7}
\]

and, for every
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma_0(4)\),

\[
\boxed{
 \mathcal H(\gamma\tau)
 =\chi _4(d)(c\tau+d)\mathcal H(\tau).}
\tag{144.C8}
\]

Thus the completed torsion section is a real-analytic scalar object of
weight one and nebentypus \(\chi _4\) on \(\Gamma_0(4)\).  The
holomorphic part \(F\) is not modular by itself; the separate
isotropic constant \(1/4\) and all four correction terms are
compulsory.  No harmonic-Maass assertion is proved.

Third, this exact automorphy does not give the required estimate or a
strict automorphic survivor.  After restoring the target-safe cells
globally and applying the exact character-Poisson formula to a smooth
dyadic weight, the positive-\(j\) principal stationary family is

\[
 e(1/8)N^{-1/4}
 \sum_{\substack{h\geq1\\0<j<\sqrt N}}\frac{\chi _4(j)}h
 V_{\rm low}\!\left(\frac{4R^2h^2}{j^2}\right)
 \psi_M\!\left(\frac{4Nh^2}{j^2}\right)e(Nh/j).
\tag{144.C9}
\]

The outer \(i/2\) in character Poisson is essential for the factor in
(144.C9).  The case \(j=\sqrt N\), when integral, belongs to the
endpoint/Fresnel ledger rather than the interior sum.  After the
accepted half-boundary, subtraction, negative alias, collar,
entry/exit, profile, and remainder ledgers are
reassembled, (144.C9) is exactly inverse to the Round-140 factor
\(e(-1/8)N^{1/4}\).  It returns the same reciprocal height--alias
owner.  The four Appell corrections are not termwise identifiable with
individual Round-140 errors; owner completeness holds only after the
global reassembly.

The round therefore closes under

\[
 \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}.}
\tag{144.C10}
\]

This label applies to the proposed completion-to-bound mechanism.  It
does not erase the genuine arithmetic progress in (144.C4), and it is
not a lower bound or a disproof of the desired signed estimate.

## 2. Exact hypotheses and objects

The cutoff \(V_{\rm low}\) is the fixed real smooth lower profile from
Rounds 140--142.  Empty rows and zero profile samples contribute zero.
The dyadic blocks are disjoint and half open, including the smallest
block and the terminal truncation.  Bounded \(X\) is absorbed in the
implied constants.  For large \(X\),

\[
 k_m\ll_V N^{3/4}<N\qquad(m\leq M_*),
\tag{144.C11}
\]

so a fixed residue class modulo \(N\) occurs at most once in the
relevant \(k\)-range.

For the lattice description, take

\[
 Q(h,r)=hr,\qquad
 B((h,r),(h',r'))=hr'+rh',
\tag{144.C12}
\]

and the level-four sublattice

\[
 L_4=\mathbb Z(1,0)\oplus\mathbb Z(0,4),\qquad
 \operatorname {Gram}(L_4)=
 \begin{pmatrix}0&4\\4&0\end{pmatrix}.
\tag{144.C13}
\]

The signed cosets \((0,1)+L_4\) and \((0,3)+L_4\) encode
\(\chi _4(r)\).  With

\[
 c_s=(1,-4),\qquad c_0=(0,-1),
\tag{144.C14}
\]

one has \(Q(c_s)=-4\), \(Q(c_0)=0\),
\(B(c_s,(h,r))=r-4h\), and
\(B(c_0,(h,r))=-h\).  The sign kernel selects the desired cone and its
opposite.  The wall \(r=4h\) contains no odd lattice point, while the
formal \(h=0\) boundary diverges and requires the Appell/Abel
regularization represented by the constant in (144.C6).

The Appell completion uses exactly the convention

\[
 A_\ell(z,w;\sigma)=\zeta^{\ell/2}
 \sum_{n\in\mathbb Z}
 \frac{(-1)^{\ell n}q^{\ell n(n+1)/2}\xi^n}
 {1-\zeta q^n},
\tag{144.C15}
\]

where \(q=e(\sigma)\), \(\zeta=e(z)\), and \(\xi=e(w)\).  At
\((\ell,z,w,\sigma)=(4,1/2,-3\tau,2\tau)\), the denominator is
\(1+e(2n\tau)\), hence is nonzero on \(\mathbb H\), and

\[
 A_4\!\left(\frac12,-3\tau;2\tau\right)
 =\frac12+2F(\tau).
\tag{144.C16}
\]

The individual complex direction \(e(+\sqrt{Nm})\) is retained.  Its
conjugate is not substituted for it, and no cosine estimate is used.

## 3. Proof and derivation

### 3.1 Gcd-averaged displacement lemma

For an integer \(j\), let

\[
 \rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\}.
\tag{144.C17}
\]

The accepted prime-power calculation gives, for \(j\ne0\),

\[
 \rho_N(j)\ll_\varepsilon
 N^\varepsilon\sqrt{(N,j)}.
\tag{144.C18}
\]

It is uniform for squareful \(N\): at \(p^a\Vert N\), a nonzero
valuation below \(a\) must be even, the unit congruence has at most two
roots for odd \(p\) and at most four for \(p=2\), and the lift factor is
the square root of the common prime-power divisor.

For \(J\geq1\), retain the gcd while summing:

\[
\begin{aligned}
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 &\leq
 2\sum_{1\leq j\leq J}\sum_{d\mid(N,j)}\sqrt d\\
 &=2\sum_{d\mid N}\sqrt d\left\lfloor\frac Jd\right\rfloor
 \leq2J\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{144.C19}
\]

For fixed \(j\), the identity
\(m=(k_m^2-j)/N\), together with (144.C11), injects the relevant
\(m\)'s into the roots counted by \(\rho_N(j)\).  Equations
(144.C18)--(144.C19) prove (144.C3).

If \(N=Du^2\) with \(D\) squarefree, then

\[
 j_m=0\quad\Longleftrightarrow\quad m=Dt^2,
\tag{144.C20}
\]

and

\[
 \sum_{j_m=0}m^{-3/4}|V_{\rm low}(R^2m/N)C(m)|
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{144.C21}
\]

For the nonzero \(J\)-window, \(|C(m)|\leq\tau(m)\) gives the block
cost

\[
 \ll_{\varepsilon,V}M^{-3/4}JX^\varepsilon.
\tag{144.C22}
\]

Taking \(J=M^{3/4}\), adding (144.C21), summing the logarithmically
many blocks, and invoking the accepted floor-to-cone replacement proves
(144.C4).  A power window \(J=M^\beta\) leaves
\(M^{\beta-3/4}\) in this absolute ledger, so the method certifies no
larger fixed power than \(\beta=3/4\).  This last assertion is only a
limit of the method, not a signed lower bound.

### 3.2 Completed scalar law

The strict cone unfolds as

\[
 F(\tau)=\sum_{h\geq1}\frac{e((4h^2+h)\tau)}
 {1+e(2h\tau)}.
\tag{144.C23}
\]

Pairing the \(n\) and \(-n\) summands in (144.C15) proves
(144.C16); the \(n=0\) term is \(1/2\).  Substituting the moving
section in the completed Appell formula gives (144.C6)--(144.C7).
Equivalently, the sum of the four terms is the absolutely convergent
cone correction

\[
 \frac14\sum_{\substack{h,r\in\mathbb Z\\r\ \mathrm{odd}}}
 \chi _4(r)
 \left[
 E\!\left(\frac{(r-4h)\sqrt{\Im\tau}}2\right)
 -\operatorname {sgn}(r-4h)
 \right]e(hr\tau).
\tag{144.C24}
\]

For
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma_0(4)\), put

\[
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2).
\tag{144.C25}
\]

The completed modular Jacobi law is returned to the moving section by
the integer elliptic shifts

\[
 m_1=\frac c4,\quad r_1=\frac{d-1}2,
 \qquad
 m_2=-\frac{3(a-1)}2,\quad r_2=-3b.
\tag{144.C26}
\]

The elliptic and modular \(\tau\)-dependent exponentials cancel, and
the remaining integral exponential is
\(e[-c(d+3b)/4]=1\), since \(4\mid c\).  The remaining sign factor is
\((-1)^{(a-1)/2}=\chi _4(a)=\chi _4(d)\), proving (144.C8).
Outside \(\Gamma_0(4)\), \(c/4\) need not be integral and the same
section is not scalar; the finite characteristic orbit must then be
retained.

### 3.3 Exact character-Poisson return

For every \(w\in C_c^\infty((0,\infty))\), the accepted exact identity
is

\[
\begin{aligned}
 \sum_{m\geq1}C(m)w(m)
 ={}&\frac12\sum_{h\geq1}w(4h^2)\\
 &+\frac i2\sum_{h\geq1}\sum_{j\ne0}\chi _4(j)
 \left\{\frac1h\int_{4h^2}^{\infty}
 w(u)e\!\left(-\frac{ju}{4h}\right)du
 -\frac{2w(4h^2)}{\pi i j}\right\}.
\end{aligned}
\tag{144.C27}
\]

The bracketed double sum is absolutely convergent.  The half-boundary
and harmonic subtraction cancel only after the prescribed symmetric
recombination, using
\(\sum_{j\ne0}\chi _4(j)/j=\pi/2\).

Round 141, now sharpened by (144.C4), permits the cells to be restored
once before splitting.  For the resulting smooth dyadic weight

\[
 w_M(u)=u^{-3/4}V_{\rm low}(R^2u/N)\psi_M(u)e(\sqrt{Nu}),
\tag{144.C28}
\]

the positive-\(j\) phase has

\[
 u_0=\frac{4Nh^2}{j^2},\qquad
 \phi(u_0)=\frac{Nh}{j},\qquad
 u_0^{-3/4}|\phi''(u_0)|^{-1/2}=2N^{-1/4}.
\tag{144.C29}
\]

The principal stationary contribution of the integral inside braces is
\(2N^{-1/4}h^{-1}e(Nh/j-1/8)\) times the displayed profiles.
Multiplication by the outer \(i/2\) gives exactly (144.C9), since
\(i e(-1/8)=e(1/8)\).

The already proved Round-140/141 aggregate equivalence is

\[
 \mathcal S_{\rm recip}^{+}
 =e(-1/8)N^{1/4}\mathcal S_{\rm cone}^{+}
 +O_{\varepsilon,\rho,V}(RX^\varepsilon).
\tag{144.C30}
\]

Solving (144.C30) gives the same factor as (144.C9).  Hence the exact
coefficient transform returns the reciprocal owner after complete
reassembly.  It does not identify individual terms in (144.C7) with
individual aliases or authorize branchwise inheritance of the
Round-140 remainder.

### 3.4 Source, rational-spectrum, and capacity ledger

The audited completed-Appell laws prove real-analytic modular
covariance, not \(\Delta_1\mathcal H=0\).  The available
harmonic-Maass summation formulas require harmonicity and different
Riesz, Laplace, or Bessel tests; the complete-divisor Voronoi sources
have the wrong coefficient, boundary, or scalar direction.  Exact
coefficient extraction from (144.C6) is one completed pairing minus
four correction pairings, and no audited theorem estimates those five
owners for the literal square-root test.

Round 142 remains compatible but unchanged.  Its complete
\(4\mid q\) rational hierarchy matches the \(\Gamma_0(4)\) infinity
cusp orbit.  Finite projections retain omitted modes, and the canonical
denominator-Abel reconstruction returns
\(\sigma_{\chi _4}=r_2/4\), not \(C\), while leaving the
negative-character sector and moving wedge.

The full power ledger is:

\[
 \text{strict cone block capacity }M^{1/4+o(1)},
 \qquad
 \text{top block }R^{1/2+o(1)},
\tag{144.C31}
\]

\[
 \text{reciprocal stationary absolute capacity }N^{1/4}\asymp R,
\tag{144.C32}
\]

while the completed pairing supplies no hypothesis-matched bound for
its four correction owners.  The new deletion in (144.C4) is itself
target-safe but leaves (144.C31) unchanged.  These are upper capacities
or method prices, not signed lower bounds.

Finally, the wider phase-value gap still supplies no derivative-arc
exclusion.  It only gives, relative to the special slope \(k_m/(2m)\),

\[
 \left|\frac{k_m}{2m}-\frac{\sqrt N}{2\sqrt m}\right|
 =\frac{|j_m|}{2m(k_m+\sqrt{Nm})}
 \asymp\frac{|j_m|}{m\sqrt{Nm}}
 \gg_V\frac1{R^2M^{3/4}},
\tag{144.C33}
\]

whereas the natural physical cell length is
\(L_M\asymp M^{3/4}/R\), so its derivative-cell width is
\(L_M^{-1}\asymp R/M^{3/4}\).  The ratio is only \(R^{-3}\), and
(144.C33) says nothing about an arbitrary Farey slope \(u/q\).

## 4. First doubtful or unproved step

The first open estimate is now the sharper survivor

\[
\boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.}
\tag{144.C34}
\]

After globally restoring the target-safe cells and applying the
owner-complete Round-140/141 equivalence, this is still equivalent to
the signed reciprocal estimate

\[
 \mathcal S_{\rm recip}^{+}\ll_{\varepsilon,\rho,V}RX^\varepsilon,
\tag{144.C35}
\]

with all floors, collars, half endpoints, substitutions, negative
aliases, entries/exits, profiles, and remainders retained.

The first invalid completion shortcut would be to treat real-analytic
modularity as a coefficient estimate, omit the constant or any of the
four corrections, apply a smooth transform to the hard mask without
global restoration, replace one complex direction by a cosine, or
call the principal reciprocal family a smaller owner before the
aggregate ledger is restored.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact signature-\((1,1)\) lattice, cosets, and level | **Pass.** Equations (144.C12)--(144.C14) retain the signed odd cosets, strict cone, opposite cone, empty sloping wall, and divergent isotropic wall. |
| completed Appell normalization | **Pass.** Equations (144.C6)--(144.C7), independently matched to (144.C24), retain the separate \(1/4\) and exactly four \(i/4\) corrections. |
| scalar multiplier and full-group scope | **Pass.** Equations (144.C25)--(144.C26) give weight one and \(\chi _4(d)\) precisely on \(\Gamma_0(4)\); the full-group object is not scalar. |
| source hypotheses | **Pass/no-go.** The pole-free completed Appell theorem applies. Direct isotropic-cone hypotheses fail at zero pairing, and no audited summation theorem accepts the resulting five owners and literal test. |
| gcd-averaged displacement and squareful centres | **Pass.** Equations (144.C18)--(144.C22) retain the gcd average, exact radicals, \(k<N\) injection, half-open endpoints, and all squareful \(N\). |
| maximal absolute cell window | **Pass with scope.** \(J=M^{3/4}\) is target-safe and maximal for this absolute ledger; this is not a lower bound against a new signed method. |
| individual complex direction and outer \(i/2\) | **Pass.** Equations (144.C27)--(144.C30) give \(e(1/8)N^{-1/4}\), with no factor two or cosine. |
| hard mask and owner completeness | **Pass.** The wider cells are restored only globally; the reciprocal equivalence is aggregate, not correctionwise or rational-branchwise. |
| Round-142 consistency | **Pass/no-go.** The cusp hierarchy agrees with level four, but Abel reconstruction remains \(r_2/4\) and the negative sector survives. |
| capacity and directionality | **Pass/no-go.** The top strict owner remains \(R^{1/2}\), the reciprocal owner has absolute capacity \(R\), and neither is a signed lower bound. |
| downstream scope | **Pass.** No lower GAR, direct M1 parent, M9-M1, M2 owner, endpoint theorem, M9, bridge, quarter theorem, or exponent improvement is asserted. |

The accepted evidence is entirely analytical, algebraic, and
source-based.  Optional numerical diagnostics in one blind report are
excluded from the campaign evidence and from every conclusion.

## 6. Dependencies and exact artifacts used

The candidate uses the Round-144 campaign statement, all three primary
reports, and the three post-unmask analytic/source seam reviews.  It
also uses the accepted Round-63 Appell identity and character-Poisson
formula, the owner-complete Round-140 height--alias transform, the
Round-141 floor/cell reduction, and the Round-142 rational-spectrum
adjudication.  Exact source locations and hypotheses are recorded in
`reports/indefinite_theta_source_hypothesis_audit.md`.

No numerical result, centre average, arbitrary-array surrogate,
positive energy, desired circle estimate, or unaccepted source theorem
is used.  Historical campaign artifacts are not rewritten; the
Round-141 exhaustion statement is corrected only in the authoritative
graph and this new review chain.

## 7. Recommended state effect

1. Create a source-audit node for the derived completed scalar
   specialization (144.C5)--(144.C8), while retaining the older
   Round-63 Appell source node.  Record explicitly that the
   \(\Gamma_0(4)\) scalar law is an internally derived specialization
   of the cited completed Jacobi laws, not a verbatim theorem from the
   source and not a rediscovery of the Round-63 identity.
2. Strengthen `M9-M1-lower-far-cone-microscopic-cell-reduction` from
   the \(\sqrt M\) window to (144.C3)--(144.C4), and revise the old
   claim that the pointwise \(J^{3/2}\) count exhausts this method.
3. Create a scoped Appell-reconciliation obstruction recording the
   exact scalar completion, the mandatory five-owner coefficient
   pairing, the aggregate reciprocal self-return, the Round-142 Abel
   mismatch, and capacities (144.C31)--(144.C32).
4. Update the Round-63 Appell-Poisson reduction, the Round-141
   incomplete-fibre obstruction, the Round-142 rational-spectrum
   obstruction, and the global lower-radial owner with this evidence.
5. Reject coefficient-only, harmonic-Maass, correction-dropping,
   branchwise-return, cosine, or exponent inferences.  Leave
   (144.C34)--(144.C35), all M1/M2 parents, endpoint uniformity, M9,
   the conditional bridge, the internal exponent \(1/3\), the audited
   external Li--Yang exponent, and the quarter target open.

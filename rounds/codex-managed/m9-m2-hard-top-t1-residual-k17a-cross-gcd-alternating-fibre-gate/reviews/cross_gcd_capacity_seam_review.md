# Round 176 cross-gcd capacity seam review

## 1. Verdict

**Overall: REVISE, with a promotable exact algebraic kernel and a repairable
strict-sector count.**

The hostile and blind coordinate systems are exactly compatible on the
literal squarefree support.  Both orientations, multiplicity one, parity,
the half-frequency character law, the original-gcd identity, the common
endpoint translation, and the canonical-sawtooth Fourier formula all pass.
Neither report drops a parity branch or an orientation.  The blind formula
keeps the outer real part and all literal endpoint weights explicitly; the
hostile report says that it keeps them, but its schematic transformed family
(176.H46) should display them before that family is treated as an exact
identity.

The hostile numerical capacities are mostly correct, but one derivation
needs repair.  The frozen statement gives \(N,N+r\asymp L^2\); it does not,
by itself, state that each of \(d,m,d',m'\) is individually \(\asymp L\).
Consequently the global assertion \(T\ll1+\kappa\) and the count
“\(O(L/\kappa)\) choices for each of \(u,v\)” are not consequences of the frozen
packet.  The tail bound (176.H6) nevertheless survives: a divisor-hyperbola
count with the correct variable row length proves the same
\(L^3/K\) bound.  Thus the fixed-proportion high-\(\kappa\) sector is
promotable after replacing the proof of (176.H22)--(176.H23).

The derivative, exponent-pair, optimistic one-saving, and two-dimensional
Poisson ledgers pass as **fixed-relative-cell or route-capacity ledgers**.
They do not prove lower mass, failure of the literal sum, or impossibility of
a signed joint estimate.  The hostile report generally states this scope
correctly.  The blind report's constant canonical-sign family is a valid
control against naive determinant adjacency, but it is not a power
obstruction because the hostile DFT removes the sawtooth at logarithmic
normalized algebra cost.

The first unproved affirmative step remains a signed joint estimate for the
literal selector-weighted family before positive recombination over dual
modes, determinants, Möbius openings, fibres, or orientations.

## 2. Algebra, orientations, multiplicity, and coordinate compatibility

### Findings

- **PASS — both orientations.**  In the first hostile orientation,

  \[
  d=\kappa u,\quad d'=\kappa u+2s,\quad
  m'=\kappa v,\quad m=\kappa v+2w,\quad
  c=sv-wu>0.
  \]

  Then \(N'-N=2\kappa c\).  In the opposite orientation the same four
  unordered factors occur, (c=uw-sv>0), and again \(N'-N=2\kappa c\).
  These are exactly the two signs in the blind determinant coordinate.

- **PASS — multiplicity one.**  The inward cross gcd is uniquely
  (kappa=(d,m')) in the first orientation and (kappa=(d',m)) in the
  second.  After division by (kappa), ((u,v)=1), and the primitive
  equation has all solutions

  \[
  (s,w)=(s_0,w_0)+t(u,v).
  \]

  Positivity, shells, selectors, and endpoints only delete sites.  A
  canonical residue for \(s_0\pmod u\) makes the representation unique.

- **PASS — parity and character.**  Since the divisor coordinate is odd,
  (kappa,u) are odd.  The shift is \(r=2\kappa c=\kappa h\), so
  (h=2c) is even and (kappa<R_0/2).  The complement parity is the
  parity of (v), retained in both branches.  Moreover

  \[
  \chi_4(d')\chi_4(d)=(-1)^s
  =(-1)^{s_0}(-1)^{ut}=(-1)^{s_0}(-1)^t.
  \]

- **PASS — original gcd.**  In the first orientation, squarefreeness of
  (d'm') gives ((d',m')=1).  Since \(kappa\mid m'\), this implies
  \((\kappa,s)=1\).  Therefore

  \[
  (d,d')=(\kappa u,\kappa u+2s)
  =(\kappa u,s)=(u,s).
  \]

  Reducing (sv-wu=c) modulo (u) and using ((u,v)=1) gives
  ((u,s)=(u,c)).  The opposite orientation is identical using the other
  squarefree endpoint.  Thus

  \[
  g_{\rm orig}=(d,d')=(u,c)=(u,h/2),
  \]

  and the cutoff \(g_{\rm orig}<\gamma L\) is constant along a fixed
  \((\kappa,u,v,c)\)-fibre.

### Exact map to the blind coordinates

Let the blind variables be

\[
 g=g_{\rm orig},\quad d_{\rm lo}=ga,\quad
 d_{\rm hi}=g(a+2k),\quad m_{\rm lo}=n,\quad
 m_{\rm hi}=n+2w,\quad K_b=kn-aw.
\]

On squarefree support, write (u=gu_0) and (c=gc_0).  The two systems
are related by

\[
 \boxed{
 a=\kappa u_0,\qquad n=\kappa v,\qquad
 k={s\over g},\qquad K_b=\begin{cases}
 \kappa c_0,&d'>d,\\-\kappa c_0,&d'<d,
 \end{cases}}
 \tag{S1}
\]

with the same (w).  Conversely,

\[
 \kappa=(a,n),\qquad u=g{a\over\kappa},\qquad
 v={n\over\kappa},\qquad s=gk,\qquad
 c={g|K_b|\over\kappa}.
 \tag{S2}
\]

The required coprimalities follow from the squarefree endpoints.  In
particular, \((a/\kappa,n/\kappa)=1\), \((a/\kappa,K_b/\kappa)=1\), and
((u,c)=g).  Hence the blind fibre gcd (h_b=(a,n)) is precisely the
hostile cross gcd (kappa), while the blind leading coordinate (g) is
the original divisor gcd.

The fibre steps also agree:

\[
 s\mapsto s+u, w\mapsto w+v
 \quad\Longleftrightarrow\quad
 k\mapsto k+{u\over g}, w\mapsto w+v,
\]

and

\[
 {2gan\over(a,n)}=2\kappa uv.
\]

Since (g) is odd, ((-1)^s=(-1)^{gk}=(-1)^k).  Finally,
\(2g|K_b|=2\kappa c\).  This verifies the blind formula, the hostile
formula, and their multiplicities at the seam.

## 3. Row length, tail count, and strict sector

### Literal row length

For fixed \((\kappa,u,v,c)\), both products advance by

\[
 D=2\kappa uv.
\]

The two product shells have length (O(L^2)), so the unconditional row
length furnished by the frozen packet is

\[
 T\ll 1+{L^2\over\kappa uv}.
 \tag{S3}
\]

If one additionally restricts to a fixed-relative near-square cell
\(\kappa u,\kappa v\asymp L\), then \(uv\asymp(L/\kappa)^2\), and (S3)
becomes \(T\ll1+\kappa\), with \(T\asymp\kappa\) on a full interior row.
Thus (176.H22) is **PASS on that cell but REVISE as a global literal
statement**.

The distinction is real.  With (kappa=u=v=1) and (s-w=c), the products
are (1+2w) and (1+2s).  A product shell of width \(\asymp L^2\) can
contain \(\asymp L^2\) geometric sites although (kappa=1).  This is a
geometry control only; it is not a density assertion for the literal
squarefree selector.

### Repaired tail ledger

The conclusion (176.H6) is nevertheless correct.  Positivity of the gaps
and \(N,N+r\ll L^2\) imply

\[
 \kappa^2uv\ll L^2.
\]

Put \(Y=L/\kappa\).  For fixed (kappa), the number of positive
determinants is (O(Y)), since \(r=2\kappa c<R_0\).  Multiplicity one and
(S3), followed by deletion of all literal restrictions, give

\[
 \begin{aligned}
 C_\kappa
 &\ll X^\varepsilon
 \sum_{uv\ll Y^2}\ \sum_{c\ll Y}
 \left(1+{L^2\over\kappa uv}\right)\\
 &\ll X^\varepsilon\left{
 Y^3\log(2Y)+{L^2Y\over\kappa}\log^2(2Y)
 \right}\\
 &\ll {L^3\over\kappa^2}X^\varepsilon.
 \end{aligned}
 \tag{S4}
\]

Here

\[
 \#\{(u,v):uv\ll Y^2\}\ll Y^2\log(2Y),
 \qquad
 \sum_{uv\ll Y^2}{1\over uv}\ll\log^2(2Y).
\]

Both orientations only change the implied constant.  The original-gcd
cutoff, squarefree conditions, selectors, parity, hard endpoints, and zero
extension all delete terms; the Fejer weight has modulus at most one; and
the outer real part is bounded by the complete absolute mass.  Therefore

\[
 \sum_{\kappa\ge K_{\rm cut}}C_\kappa
 \ll {L^3\over K_{\rm cut}}X^\varepsilon.
 \tag{S5}
\]

This proves (176.H6) without the unproved individual near-square assertion.
In particular, for fixed \(0<\eta<1/2\), the complete literal sector
\(\kappa\ge\eta L\) is target-safe.  **Finding: PASS after mandatory proof
repair.**

If one had an \(O(X^\varepsilon)\) bound per primitive row, then the number
of rows at fixed (kappa) is

\[
 O\!\left(Y\#\{uv\ll Y^2\}\right)
 \ll {L^3\over\kappa^3}X^\varepsilon,
\]

and summing gives \(L^3K_{\rm cut}^{-2}X^\varepsilon\).  Thus the optimistic
\(K_{\rm cut}=\sqrt L\) comparison (L^2) versus the raw (L^{5/2}) is
also correct, although the proof should use this hyperbola count rather
than three independent \(O(L/\kappa)\) boxes.

## 4. Phase, Fourier, optimistic-saving, and joint-transform ledgers

### Exact phase and derivative ledger

Let (x=N_0+Dt), \(D=2\kappa uv\), \(r=\kappa h\), and

\[
 \Phi(t)=J(\sqrt{x+r}-\sqrt x)+{t\over2}.
\]

Direct differentiation reproduces (176.H26) exactly:

\[
 \begin{aligned}
 \Phi'(t)&={JD\over2}\{(x+r)^{-1/2}-x^{-1/2}\}+{1\over2},\\
 \Phi''(t)&={JD^2\over4}\{x^{-3/2}-(x+r)^{-3/2}\},\\
 \Phi'''(t)&={3JD^3\over8}\{(x+r)^{-5/2}-x^{-5/2}\}.
 \end{aligned}
 \tag{S6}
\]

To expose the support dependence, set

\[
 \vartheta={\kappa^2uv\over L^2}\ll1.
\]

On an interior product shell, (S3) has scale \(T\asymp\kappa/\vartheta\),
and Taylor expansion in \(r/x\ll L^{-1}\) gives

\[
 |\Phi'-1/2|\asymp {J\vartheta h\over L},\qquad
 \Phi''\asymp {J\vartheta^2h\over\kappa L},\qquad
 |\Phi'''|\asymp {J\vartheta^3h\over\kappa^2L}.
 \tag{S7}
\]

With

\[
 F={Jh\kappa\over L},
\]

these are (F/T,F/T^2,F/T^3).  The hostile scales (176.H27)--(176.H28)
are exactly the case \(\vartheta\asymp1\), hence **PASS on a
fixed-relative interior cell**.  They are not the global row scales under
the product-shell statement alone.

For \(\vartheta\asymp1\), \(kappa h<R_0\asymp L\) gives

\[
 {F\over T^2}\asymp {Jh\over\kappa L}
 \gtrsim {Jh^2\over L^2}\gtrsim1
 \tag{S8}
\]

at the power-counting level.  The phrase (L^2=o(J)) in (176.H29) is
stronger than the frozen hypotheses and should be removed; \(J\gtrsim L^2\)
is sufficient for the no-power-saving comparison.  Likewise “(>T)” in
(176.H5) should be read as “(gtrsim T)” at this level.

The derivative image has (O(1+F/T)) central modes and one stationary
integral has scale \(T/\sqrt F\).  Absolute recombination therefore gives

\[
 (1+F/T){T\over\sqrt F}
 =\sqrt F+{T\over\sqrt F}.
 \tag{S9}
\]

On \(\vartheta\asymp1\), (S8) makes this certificate no better in powers
than the trivial (T).  This is a **PASS for the named positive-mode
rowwise route**, not a lower bound for the exponential sum.  For
\(\vartheta\ll1\), (S7), not (176.H27), must be used.

The exponent-pair algebra in (176.H36)--(176.H38) is correct on the same
cell.  Indeed

\[
 (F/T)^\alpha T^\beta
 =\left({Jh\over L}\right)^\alpha\kappa^\beta,
\]

and positive summation over \(u,v,h\asymp L/\kappa\) yields

\[
 J^\alpha L^3
 \sum_{\kappa\ge K_{\rm cut}}
 \kappa^{\beta-\alpha-3}
 \ll J^\alpha L^3K_{\rm cut}^{\beta-\alpha-2}.
\]

At \(K_{\rm cut}=\sqrt L\) this is
\(J^\alpha L^{2+(\beta-\alpha)/2}\).  **Finding: PASS as a formal
positively recombined cell ledger; not a global impossibility theorem.**

### Canonical sawtooth Fourier norm

For odd (u), with (E_u(a)=(-1)^{[a]_u}), direct geometric summation
gives

\[
 \widehat E_u(k)=\sum_{a=0}^{u-1}(-1)^ae(-ka/u)
 ={2\over1+e(-k/u)}.
 \tag{S10}
\]

Because

\[
 |\widehat E_u(k)|={1\over|\cos(\pi k/u)|},
\]

the two tails around (u/2) are harmonic and

\[
 {1\over u}\sum_{k\bmod u}|\widehat E_u(k)|
 \ll\log(2u).
 \tag{S11}
\]

Fourier inversion gives (176.H45).  **Finding: PASS.**  The blind
constant-sign determinant examples remain valid controls, but they only
refute naive adjacent-(K) alternation.  They cannot be promoted as a power
obstruction to a joint determinant argument after (S10)--(S11).

### Optimistic one-saving capacity

On the hostile fixed-relative cell, the positive counts are

\[
 {L\over\kappa}\ (u),\qquad
 {L\over\kappa}\ (c),\qquad
 \kappa\ (t).
\]

Granting, without proof, a square-root bound
\((L/\kappa)^{1/2}X^\varepsilon\) for the complete (v)-sum gives

\[
 \sum_\kappa
 {L\over\kappa}{L\over\kappa}\kappa
 \left({L\over\kappa}\right)^{1/2}
 \ll L^{5/2}.
 \tag{S12}
\]

The arithmetic is correct and the logarithmic Fourier norm is absorbed in
\(X^\varepsilon\).  **Finding: PASS only as an optimistic route-capacity
calculation.**  It is neither a proved upper bound nor a lower bound for
the literal family, and it does not exclude a joint estimate saving in two
labels at once.

### Full joint transform volume

The exact Hessian in the ((s,w)) variables is diagonal as in (176.H51).
On a fixed-relative cell its determinant has scale (J^2/L^2).  The
primitive row vector ((v,-u)) extends to a matrix in
\({\rm SL}_2(\mathbb Z)\), so ((c,t)) are unimodular lattice coordinates.
The determinant range has length \(O(L/\kappa)\), the row has length
\(O(\kappa)\), and the physical area is (O(L)).  Hence

\[
 \operatorname{vol}(\nabla\Theta)\ll {J^2\over L},
 \qquad
 |\det\operatorname{Hess}\Theta|^{-1/2}\asymp {L\over J},
\]

and termwise positive stationary recombination has (O(J)) capacity,
whereas the physical count is (O(L)).  Taking the better certificate and
summing over \((\kappa,u,v)\) gives \(O(L^3X^\varepsilon)\), as in
(176.H55).

More generally, with the \(\vartheta\) above, the physical ((c,t))-area
is \(O(L/\vartheta)\), the Hessian determinant is
\(\asymp J^2\vartheta^2/L^2\), the gradient-image volume is
\(O(J^2\vartheta/L)\), and one saddle has scale
\(L/(J\vartheta)\); their positive product is again (O(J)).  This
confirms the algebra and also shows where dyadic support bookkeeping would
enter.

**Finding: PASS as a smooth-cell, termwise-positive transform-volume
ledger.**  Literal selectors and zero extension do not make that Poisson
calculation an exact theorem automatically, and signed cancellation among
dual modes remains open.

## 5. Statements requiring repair or strict scoping

1. **REVISE (176.H10), (176.H22), and the proof of (176.H23).**  The
   factorization notation for \(\lambda\) and the assertion
   \(d,m,d',m'\asymp L\) are not specified in the frozen packet.  Keep the
   coefficient abstract, or cite an authorized exact definition.  Replace
   the global row bound by (S3) and replace the tail proof by (S4)--(S5).
   The conclusion (176.H6) then passes.

2. **REVISE (176.H29).**  Do not import (L^2=o(J)).  The frozen range
   supports the weaker scale comparison \(J\gtrsim L^2\); formulate the
   route ledger with \(\gtrsim\), not a strict numerical inequality.

3. **REVISE the status of the blind canonical-jump obstruction.**  The
   constant-sign examples are exact and useful, but (S10)--(S11) remove the
   canonical sawtooth with only \(X^\varepsilon\) loss.  They obstruct only
   a naive determinant pairing, not every joint-determinant method.

4. **PASS WITH SCOPE for (176.H34)--(176.H38) and (176.H53)--(176.H55).**
   These formulas show that the specifically named rowwise or joint
   transforms, when their dual modes are bounded termwise positively, do
   not furnish the missing power on the audited cell.  They do not show
   that the physical sum has size (T) or (L^3), and they do not exclude
   signed dual cancellation, orientation cancellation, or a theorem using
   the literal coefficient.

5. **REVISE (176.H46) before treating it as an exact transformed
   identity.**  It is explicitly called schematic.  An exact promoted
   version must display the outer real part, the Fejer factor
   \(1-2\kappa c/R_0\), the two orientation-dependent conjugations, both
   parity branches, the original-gcd cutoff \((u,c)<\gamma L\), and the
   full zero-extended endpoint coefficient.  The reports state these
   fields in prose, so this is a presentation repair rather than evidence
   of a silent mathematical deletion.

6. **PASS WITH QUARANTINE for selector, dechirped, constant-sign, and
   squarefree-progression controls.**  They falsify coefficient-uniform or
   positive-recombination mechanisms only.  They are not admissible lower
   bounds for the literal aggregate.  In particular, the absence of a
   selector regularity theorem is not evidence that the actual selector
   realizes a parity support.

7. **FAIL any global route-impossibility reading.**  The only justified
   no-go is for the named positive-recombination interfaces.  A signed
   joint large-sieve, spectral, delta, bilinear, Poisson, Möbius, or
   two-orientation estimate remains open.  The hostile report expressly
   leaves these routes open; that qualifier must survive synthesis.

## 6. First unproved step and controls checked

The first unproved affirmative step is an estimate for the exact analogue
of (176.H46), with the repairs in item 5 above, that saves a full factor
(L) before any absolute summation over dual frequencies, determinants,
((u,v)), cross gcds, square-divisor openings, selector classes, endpoints,
or orientations.  Such an estimate must use a proved property of the
literal two-endpoint coefficient or signed interaction among at least two
long labels.  Neither boundedness, the half-frequency, nor the logarithmic
DFT alone supplies it.

The following controls were checked.

| Control | Finding |
|---|---|
| Both orientations | **PASS.** They are the two signs of (K_b) under (S1). |
| Multiplicity | **PASS.** Both parametrizations are bijective after canonicalization and deletion. |
| Parity branches | **PASS.** \(v\bmod2=n\bmod2\), and (u,kappa,g) are odd. |
| Original gcd | **PASS.** (g=(u,c)), constant on each hostile fibre. |
| Fejer weight and outer real part | **PASS in the blind identity; REVISE display in hostile (176.H46).** |
| Literal selectors and endpoints | **PASS as retained opaque amplitude; no regularity estimate is proved.** |
| Short fibres | **PASS as a mechanism obstruction, not physical lower mass.** |
| Imbalanced product-shell rows | **REVISE hostile row length; repaired by (S3)--(S5).** |
| Squarefree Möbius progressions | **PASS.** Soluble square-divisor conditions have odd progression step, but positive recombination restores row incidence. |
| Canonical constant-sign family | **PASS as a naive-pairing control; not a power obstruction after the DFT.** |
| Rowwise Abel/Poisson/van der Corput | **PASS only as a positive-mode self-return audit.** |
| One optimistic family saving | **PASS arithmetic in (S12); diagnostic only.** |
| Full joint transform | **PASS smooth-cell volume; signed dual sum open.** |
| Dechirped/arbitrary arrays | **PASS quarantine; not literal coefficients or lower bounds.** |

No numerical test is needed: all disputed seams are settled by exact
integer algebra, divisor sums, differentiation, and finite Fourier
calculation.

## 7. Dependencies and promotion recommendation

This review used only:

- `protocol.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/blind_statement.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/blind_k17a_variable_determinant_rederivation.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/joint_fibre_capacity_hostile_audit.md`; and
- the assigned seam-review brief for role and output instructions.

**Promote, after incorporating the stated repairs:**

1. the exact two-orientation, multiplicity-one coordinate equivalence
   (S1)--(S2), including \(r=2\kappa c=2g|K_b|\),
   (kappa=(a,n)), (g=(u,c)), the common translation, parity, and
   half-frequency;
2. the exact normalized Fourier-algebra bound (S10)--(S11);
3. the owner-complete strict tail (S5), hence the literal
   \(kappa\ge\eta L\) sector for fixed \(0<\eta<1/2\); and
4. a route-scoped no-go only for internal alternation plus positive fibre
   summation, rowwise Abel/Kusmin--Landau without separation, positively
   recombined rowwise derivative or Poisson estimates, positive Möbius
   recombination, and positively recombined smooth-cell joint Poisson.

**Do not promote:** the global formula \(T\ll1+\kappa\), the individual
near-square support assertion without an exact source, the schematic
(176.H46) as an exact identity, the optimistic (L^{5/2}) ledger as a
theorem, any adversarial control as literal mass, the canonical sawtooth as
a power obstruction, or any impossibility statement for the full signed
K17a aggregate.

The full target (176.B1) remains open beyond the strict high-\(\kappa\)
sector.

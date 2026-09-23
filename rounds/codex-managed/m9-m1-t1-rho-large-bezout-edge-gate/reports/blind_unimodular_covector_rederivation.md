# Blind statement-only rederivation: unimodular covector union and core

- Campaign: `m9-m1-t1-rho-large-bezout-edge-gate`
- Task: `blind_unimodular_covector_rederivation`
- Round: 192
- Role: statement-only blind rederiver
- Graph SHA-256 supplied by the brief: `75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`
- Numerical theorem evidence: none

## 1. Result: sparse-union lemma and a core no-go result

The proposed covector step has a rigorous narrow part and a rigorous stopping
point.

For every fixed reduced covector \((c,d)\) with \(c<U\), and every fixed
integer \(\ell\), the canonical determinant equation gives

\[
 \rho(c v_0-dU)=c+U\ell.
\]

The right side is nonzero. Consequently the number of canonical unit residue
classes \(v_0\pmod U\) producing that triple is at most
\(2\tau(|c+U\ell|)\). This is the sharp elementary signed-divisor bound
before using the additional congruence, interval, and signed-least-inverse
restrictions, all of which can only delete candidates.

For \(T\geq1\), the union \(\mathcal E_A\) of the sectors
\(|\ell_{c,d}|\leq T\) is target-safe by positive counting, up to the declared
fixed polylogarithmic and divisor-bound costs. More precisely, if

\[
 D_{U,T,A}:=
 \max_{\substack{1\leq c\leq A\\ |e|\leq T}}
 \tau(|c+Ue|),
\]

then

\[
 \#\mathcal E_A
 \ll \frac{u}{U}\,|\mathcal F_A|(2T+1)D_{U,T,A}
 \ll \frac{Qmu}{Y}\,|\mathcal F_A|D_{U,T,A},
\]

and hence its full complex fixed-packet projection is

\[
 |\mathscr J_{\mathcal E_A}|
 \ll Qm\kappa u X^\eta |\mathcal F_A|D_{U,T,A}.
\]

Here \(|\mathcal F_A|\ll A^2\ll Q^{2C_0}\), and

\[
 D_{U,T,A}\ll_\delta [U(T+1)]^\delta.
\]

Thus, in the declared setting \(Q=H_B\), the Farey-family factor is a fixed
polylogarithm; with the declared later divisor ledger, or equivalently with
the usual explicit polynomial-size relation \(U(T+1)\leq X^{O(1)}\), fresh
epsilon budgets give the requested
\(Qm\kappa uX^\varepsilon\) scale. The \(m^{-1}\) lift weight then cancels
the displayed \(m\) before the later positive coefficient sum. No positive
power of \(Y\) remains.

The exact complement is not thereby estimated. For \(T\geq1\), it is

\[
 \mathcal C_A=
 \left\{v:\ |\rho|>T,
 |c\beta-d\rho|>T\text{ for every }(c,d)\in\mathcal F_A\right\},
\]

with all inherited literal restrictions still imposed. For \(T=0\), the
definition in the statement makes \(\mathcal E_A\) empty and
\(\mathcal C_A\) equal to the whole retained remainder.

There is a useful exact coverage theorem. Writing
\(r=|\rho|\) and \(b=|\beta|\), one has

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \leq \left\lfloor\frac{r}{A+1}\right\rfloor.
\]

Therefore, when \(T\geq1\), every core row must satisfy

\[
 r\geq(A+1)(T+1).
\]

In particular, the core is empty if

\[
 \left\lfloor
 \frac{(U-1)/2}{A+1}
 \right\rfloor\leq T.
\]

The simpler exact small-\(U\) corollary is that the core is empty whenever
\(T\geq1\) and \((U-1)/2\leq A\), because then the covector
\((c,d)=(|\rho|,|\beta|)\) has \(\ell=0\). Equivalently, it suffices that
\(U\leq2\lfloor Q^{C_0}\rfloor+1\).

Outside these coverage ranges, the complement condition alone supplies no
cancellation for arbitrary bounded arrays. It is only a restriction on the
support. A new theorem using the actual literal endpoint, carry, phase,
orientation, mask, or coefficient correlations is still necessary. This is
a no-go result for completing the rho-large remainder by Farey separation
alone, not a lower bound for the actual literal packet.

## 2. Exact statement and hypotheses

Assume exactly the statement-only hypotheses:

\[
 Q\geq1,\qquad U=mq>4Q\text{ odd},\qquad U\mid u,
 \qquad Y>Qm.
\]

The literal positive integers \(v\) lie in a fixed finite union of intervals
of total length \(O(u)\), every retained row is a unit modulo \(U\), and all
additional masks only delete rows. Let

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},
 \qquad \rho v_0-\beta U=1,
 \qquad -\frac{U-1}{2}\leq\rho\leq\frac{U-1}{2}.
\]

Because \(U\) is odd, this signed inverse is unique. It is nonzero and a unit
modulo \(U\). Define

\[
 T=\min\left\{\frac{U-1}{2},
 \left\lfloor\frac{QmU}{Y}\right\rfloor\right\},
 \qquad
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\]

where \(C_0\geq2\) is fixed, and retain only \(|\rho|>T\). For

\[
 \mathcal F_A=
 \{(c,d):1\leq c\leq A,\ 0\leq d\leq c,\ (c,d)=1\},
 \qquad \ell_{c,d}=c\beta-d\rho,
\]

define the safe row set by the single union indicator

\[
 1_{\mathcal E_A}(v)=
 1_{T\geq1}\,
 1_{\{\exists(c,d)\in\mathcal F_A:
                 |\ell_{c,d}|\leq T\}}.
\]

The corresponding complex projection is the original rho-large aggregate
multiplied by this row indicator. It is not the sum of the overlapping
individual covector projections. The exact core projection is defined by
complex subtraction before the final real part:

\[
 \mathscr J_{\mathcal C_A}
 =\mathscr J_{\rm rho\text{-}large}-\mathscr J_{\mathcal E_A}.
\]

Thus both orientations and every surviving endpoint, carry, phase, mask,
birth, death, and zero extension remain in each projection under the one
outer operation.

The conclusions are:

1. For fixed \((c,d,e)\), the number of admissible residues is at most
   \(2\tau(|c+Ue|)\).
2. For \(T\geq1\), the row and atom bounds displayed in Section 1 hold.
3. The union is target-safe after precisely the fixed-polylogarithmic and
   elementary-divisor costs are assigned fresh epsilon budget; without an
   explicit size connector between \(U\) and \(X\), the fully
   self-contained conclusion is the bound retaining
   \(D_{U,T,A}\), not an unqualified \(X^\varepsilon\) replacement.
4. The complement and coverage statements in Section 1 are exact.
5. No estimate for a nonempty core follows for arbitrary bounded arrays.

## 3. Proof or derivation

### 3.1 Canonical quotient, signs, and the literal representative

The determinant equation immediately gives

\[
 (\rho,\beta)=1.
\]

Indeed, every common divisor divides
\(\rho v_0-\beta U=1\). The signs and endpoint cases are also forced:

\[
 \begin{array}{ll}
 \rho>0:&0\leq\beta\leq\rho-1,\\[2mm]
 \rho<0:&\rho\leq\beta\leq-1.
 \end{array}
\]

For positive \(\rho\), this follows from
\(1\leq\rho v_0<\rho U\). For negative \(\rho\), write
\(r=-\rho>0\); then \(-\beta=(rv_0+1)/U\) lies between \(1\) and \(r\).
Consequently \(\rho\) and \(\beta\) have the same sign except for the
allowed endpoint \((\rho,\beta)=(1,0)\), and

\[
 0\leq\frac{\beta}{\rho}\leq1.
\]

Every positive literal representative has the unique form

\[
 v=v_0+nU,\qquad n\geq0.
\]

If its actual transport quotient is defined by

\[
 \rho v-\gamma U=1,
\]

then

\[
 \gamma=\beta+n\rho.
\]

Thus \(\gamma\) generally differs from \(\beta\). The canonical covectors
in this report depend only on the residue through \(\beta\); replacing it by
\(\gamma\) would change \(\ell_{c,d}\) by \(cn\rho\) and destroy the
residue-class count.

### 3.2 Exact factorization and fixed-triple multiplicity

For every fixed \((c,d)\), multiplication of the determinant equation by
\(c\), followed by subtraction of \(d\rho U\), gives

\[
 \begin{aligned}
 \rho(c v_0-dU)
 &=c\rho v_0-d\rho U\\
 &=c+U(c\beta-d\rho)\\
 &=c+U\ell_{c,d}.
 \end{aligned}
\]

Fix \(e=\ell_{c,d}\). Since \(1\leq c\leq A\leq U-1\),

\[
 N_{c,e}:=c+Ue\neq0.
\]

Every admissible \(\rho\) is therefore a signed divisor of \(N_{c,e}\).
For a selected signed divisor \(\rho\), there is at most one canonical
residue \(v_0\), namely its inverse modulo \(U\) in
\(\{1,\ldots,U-1\}\). The quotient, range, signed-least-inverse, and
literal masks may reject that candidate but cannot create another one.
Hence

\[
 \#\{v_0\pmod U:\ell_{c,d}=e\}
 \leq2\tau(|N_{c,e}|).
\]

The absolute value and the factor two are necessary because both \(N\) and
\(\rho\) are signed. This is the strongest general estimate obtained solely
by the elementary divisor-pair argument.

The strict inequality \(c<U\) is essential. If \(c=U\) were admitted, then
for any unit \(v_0\), taking \(d=v_0\) would give

\[
 \ell_{U,v_0}=U\beta-v_0\rho=-1,
 \qquad U+U\ell_{U,v_0}=0,
\]

so the nonzero-divisor argument would fail exactly.

When \(e=0\), more is true. The equation
\(c\beta=d\rho\), together with \((c,d)=1\), implies

\[
 \rho=cs,\qquad \beta=ds
\]

for an integer \(s\). Substitution gives

\[
 s(c v_0-dU)=1,
\]

so \(s=\pm1\). Thus a fixed reduced covector has at most the two exact
zero classes \((\rho,\beta)=\pm(c,d)\); no density saving should be inferred
from this fact when \(T=0\).

For \(|e|\leq T\) and \(T\geq1\),

\[
 0<|c+Ue|\leq A+UT<U(T+1).
\]

The elementary divisor bound therefore yields, for every \(\delta>0\),

\[
 D_{U,T,A}\ll_\delta[U(T+1)]^\delta.
\]

### 3.3 Farey-family and literal-row multiplicities

The family has the exact cardinality

\[
 |\mathcal F_A|=2+\sum_{c=2}^{A}\varphi(c)
 \leq \frac{A(A+1)}2+1
 \ll A^2\ll Q^{2C_0}.
\]

There are \(2T+1\) possible integer values of \(e\) in the safe union.
The union bound and the fixed-triple estimate give at most

\[
 2|\mathcal F_A|(2T+1)D_{U,T,A}
\]

canonical residue classes. Over an interval of length \(L_i\), a fixed
residue occurs at most \(L_i/U+1\) times. Summing over the fixed finite
number of intervals and using total length \(O(u)\) gives

\[
 O(u/U+1)=O(u/U),
\]

because \(U\mid u\) implies \(u/U\geq1\). All projective or literal masks
only decrease this multiplicity. Therefore

\[
 \#\mathcal E_A
 \ll \frac{u}{U}|\mathcal F_A|(2T+1)D_{U,T,A}.
\]

If \(T\geq1\), then \(2T+1\leq3T\), and the definition of \(T\) always
gives

\[
 T\leq\frac{QmU}{Y},
\]

including when the half-modulus term is the minimum. This proves

\[
 \#\mathcal E_A
 \ll \frac{Qmu}{Y}|\mathcal F_A|D_{U,T,A}.
\]

Multiplication by the stated positive atom capacity
\(O(Y\kappa X^\eta)\) proves the fixed-packet bound in Section 1.

The exact safe projection uses \(1_{\mathcal E_A}\) once. Although the proof
uses a union bound over all representations, no row is duplicated in the
complex aggregate. Its complement is complex subtraction before the final
real part. Thus the estimate does not separately absolutize orientations or
alter any literal jump source.

Since \(A\leq Q^{C_0}\), \(|\mathcal F_A|\) is a fixed power of the
polylogarithmic \(Q=H_B\). Assigning this factor and the elementary divisor
bound fresh epsilon budget gives the desired fixed scale. In the later
linear ledger, the exact factor \(m^{-1}c_q(a)\) cancels the displayed
fixed-packet \(m\) before the logarithmic coefficient sum, power-of-two
bands, and divisor multiplicity are taken. The cancellation of \(Y\) has
already occurred through \(T\leq QmU/Y\); no \(Y^\theta\) is hidden in an
epsilon factor.

### 3.4 Exact core and strongest elementary coverage

Set

\[
 r=|\rho|,\qquad b=|\beta|.
\]

The sign analysis gives \(0\leq b\leq r\), \((r,b)=1\), and

\[
 |c\beta-d\rho|=|cb-dr|.
\]

If \(r\leq A\), the reduced pair \((r,b)\) belongs to
\(\mathcal F_A\) and has \(rb-br=0\). Thus every core row has \(r>A\).

A stronger bound follows from a circular pigeonhole argument. If \(A<r\),
the \(A+1\) residues

\[
 0,b,2b,\ldots,Ab\pmod r
\]

are distinct. Their \(A+1\) positive cyclic gaps sum to \(r\), so one gap
has integer length at most \(\lfloor r/(A+1)\rfloor\). The two endpoint
indices differ by an integer \(c\) with \(1\leq c\leq A\), and hence for
some integer \(d\),

\[
 |cb-dr|\leq\left\lfloor\frac r{A+1}\right\rfloor.
\]

Because the right side is less than \(r\), the inequalities
\(0\leq b\leq r\) force \(0\leq d\leq c\). Dividing \((c,d)\) by their
gcd divides the displayed integer by the same gcd, preserves the bound, and
produces a member of \(\mathcal F_A\). If \(A\geq r\), the zero covector
\((r,b)\) proves the same inequality because its right side is zero. Hence

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \leq\left\lfloor\frac r{A+1}\right\rfloor
\]

in all cases.

For a core row with \(T\geq1\), the left side is at least \(T+1\).
Therefore

\[
 \left\lfloor\frac r{A+1}\right\rfloor\geq T+1,
 \qquad r\geq(A+1)(T+1).
\]

Since \(r\leq(U-1)/2\), the core is empty whenever

\[
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor\leq T.
\]

The ell-zero small-\(U\) corollary
\((U-1)/2\leq A\) is a particularly transparent subcase.

These are conditional coverage criteria, not a universal Farey cover. For
example, take

\[
 Q=m=1,\quad U=q=17,\quad Y=10,\quad A=1,\quad T=1,
 \quad v_0=7.
\]

Then

\[
 5\cdot7-2\cdot17=1,
\]

so \((\rho,\beta)=(5,2)\). The only covectors for \(A=1\) are
\((1,0)\) and \((1,1)\), with ell values \(2\) and \(-3\). This retained
row lies in the core. Thus neither Farey separation nor the existence of
the exact rational covector gives full coverage at the allowed
polylogarithmic family size in all parameter ranges.

### 3.5 Zero, floor, and saturation regimes

Since \(U\) is odd, \((U-1)/2\) and \(T\) are integers. If

\[
 T=0,
\]

then \(QmU/Y<1\). The safe sector is defined to be empty. This convention is
necessary: one residue class has literal multiplicity \(O(u/U)\), whereas
the target row budget is \(Qmu/Y\), and their ratio is

\[
 \frac{Y}{QmU}>1.
\]

Thus even an isolated ell-zero class is not uniformly target-safe by the
available positive count. No ell condition may be imposed on the exact
core in this regime.

If

\[
 T=\frac{U-1}{2},
\]

then the retained condition \(|\rho|>T\) is impossible, so the rho-large
remainder, its safe union, and its core are all empty. Empty literal
supports are of course also harmless. The floors cause no extra endpoint
loss: for every nonempty \(T\geq1\) sector, the exact inequalities
\(2T+1\leq3T\) and \(T\leq QmU/Y\) used above remain valid.

### 3.6 No cancellation theorem for the nonempty core

The core condition constrains only which rows are present. It gives no
relation among the bounded complex coefficients attached to those rows or
their atoms. For any finite nonempty set of permitted atoms with prescribed
unit phases \(z_j\), the bounded array choice

\[
 a_j=\overline{z_j}
\]

makes every term \(a_jz_j=1\). One may set unused orientations or atoms to
zero. Thus a support-only estimate valid for arbitrary bounded arrays can
be as large as the full positive atom count. This is an operator-class
countermodel, not a claim that the actual literal coefficients realize the
extremizer.

Consequently Farey separation, positive completion, or another
coefficient-insensitive norm cannot by itself recover the missing factor
\(Y/(Qm)\) on a nonempty core. A successful continuation must use a
specific property of the actual literal coefficients, phases, carries,
endpoints, masks, or the joint two-orientation structure. No such property
is present in the statement-only packet. In particular, the argument does
not prove the false unsigned or adversarial analogue; its safe-union part is
deliberately positive, and its core part stops precisely where signed
literal information becomes indispensable.

## 4. First doubtful or unproved step

The first unproved mathematical step is a bound for the exact nonempty
core projection

\[
 |\mathscr J_{\mathcal C_A}|
 \ll_\varepsilon Qm\kappa uX^\varepsilon
\]

outside the coverage conditions in Section 3.4. The badly-approximable
inequalities do not imply this estimate, even for arbitrary bounded arrays.
A new literal coefficient correlation theorem is required before any
iteration, completion, or positive norm can close the core.

There is also a precise bookkeeping caveat. The self-contained statement
does not state a quantitative upper bound relating \(U(T+1)\) to \(X\).
Therefore the unconditional statement-only estimate retains
\(D_{U,T,A}\). Replacing it by \(X^\varepsilon\) is valid only through the
declared later divisor ledger or after adding an explicit polynomial-size
connector. This caveat does not affect the exact divisor, row, \(Y\), or
Farey counts.

## 5. Required control tests and outcomes

1. `canonical_v0_vs_literal_v_vs_transport_gamma` — **PASS.** For
   \(v=v_0+nU\), \(\gamma=\beta+n\rho\); only \(\beta\) is residue
   canonical.
2. `signed_least_inverse_and_beta_signs` — **PASS.** The signed inverse is
   unique because \(U\) is odd; \(0\leq\beta<\rho\) for \(\rho>0\), and
   \(\rho\leq\beta<0\) for \(\rho<0\).
3. `exact_unimodular_covector_factorization` — **PASS.** The identity is
   exactly \(\rho(c v_0-dU)=c+U\ell_{c,d}\).
4. `c_strictly_less_than_U_nonzero_rhs` — **PASS.** Since
   \(1\leq c<U\), \(c+Ue\neq0\). Allowing \(c=U\) gives the explicit
   zero-RHS case \((d,e)=(v_0,-1)\).
5. `T_zero_sector_empty` — **PASS.** It is empty by definition and must
   remain so because a single residue can exceed the target density when
   \(QmU/Y<1\).
6. `ell_zero_and_floor_cases` — **PASS.** Ell zero forces
   \((\rho,\beta)=\pm(c,d)\); it is safe only inside \(T\geq1\). All floor
   and half-modulus endpoints were retained.
7. `divisor_pair_multiplicity` — **PASS.** The exact uniform bound is
   \(2\tau(|c+Ue|)\), with all further conditions deleting candidates.
8. `Farey_family_size_polylogarithmic` — **PASS with stated context.**
   \(|\mathcal F_A|\leq A(A+1)/2+1\ll Q^{2C_0}\), a fixed polylogarithm
   when \(Q=H_B\).
9. `literal_residue_class_multiplicity_U_divides_u` — **PASS.** A fixed
   finite interval union gives \(O(u/U+1)=O(u/U)\) occurrences per residue.
10. `safe_projection_union_no_double_count` — **PASS.** The projection uses
    the single union indicator; overlap appears only in the upper-bound
    union count.
11. `exact_badly_approximable_core` — **PASS.** It is the piecewise core
    stated in Sections 1 and 2, with no ell condition when \(T=0\).
12. `small_U_coverage_corollary` — **PASS.** For \(T\geq1\),
    \((U-1)/2\leq A\) gives ell-zero coverage of every row; the stronger
    floor criterion was also proved.
13. `no_false_Farey_full_cover_without_sector_cost` — **PASS.** The
    \((U,A,T,\rho,\beta)=(17,1,1,5,2)\) example leaves a core, and enlarging
    \(A\) incurs the explicit \(O(A^2)\) union cost.
14. `no_bounded_array_or_positive_completion_closure` — **PASS as a
    no-go.** Phase-conjugate bounded arrays attain positive capacity on any
    nonempty allowed atom set; this is not asserted for the literal array.
15. `original_t1_only_downstream_scope` — **PASS.** Even full coverage would
    settle only the stated rho-large piece of the inherited original-
    \(t=1\) remainder; no other range is addressed by this report.
16. `exponent_quarantine` — **PASS.** No parent, bridge, theorem, or exponent
    conclusion follows from the safe union or the core no-go.

All controls were algebraic. No numerical experiment or web source was
used.

## 6. Dependencies and exact artifacts used

Only the permitted statement-only context was used:

- `protocol.md`, SHA-256
  `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/briefs/blind_unimodular_covector_rederivation.md`,
  SHA-256
  `2c81d260c5bf4ba2cea671e7fb140204a25ae11bfe14cffcc0a64050990454f1`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/blind_statement.md`,
  SHA-256
  `8650eb7142a4e8d498b3b3f9a8c6cbdf451486c554822dfb5a3e301ad005505c`.

No state file, sibling artifact, earlier campaign, strategy file, source card,
kernel, control, or synthesis was inspected. The proof uses only Bezout's
identity, signed integer divisor counting, interval residue counting, and a
finite circular pigeonhole argument.

## 7. Recommended state effect

**Retain and split the conclusion.** After the required seam validation,
the conductor may promote the narrow covector safe-union/counting reduction,
including the exact core and coverage corollaries. Keep the full rho-large
remainder open outside the proved coverage regimes.

Record as rejected routes any claim that canonical \(\beta\) equals the
literal transport quotient, that \(T=0\) ell-zero classes are automatically
safe, that bounded-array capacity proves literal lower mass, that Farey
separation alone cancels the core, or that the polylogarithmic family gives
an unconditional full cover. Make no status or exponent change to any
complete original-\(t=1\), higher-\(t\), M1, M2, endpoint, bridge, or theorem
owner.

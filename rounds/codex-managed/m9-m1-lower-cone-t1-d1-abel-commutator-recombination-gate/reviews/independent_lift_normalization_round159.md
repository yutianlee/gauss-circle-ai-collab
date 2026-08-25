# Round 159 independent lift and normalization seam review

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Role: independent mathematical seam reviewer
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

**Verdict: the lift indicator is removable in the actual project, although it is necessary in the stripped statement-only problem.**

The blind report correctly proves that the bounds

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon
\]

alone do not imply that a selected nearest integer lies in an arbitrarily
chosen complete lift.  Its countermodel is therefore valid against the
literal data in `blind_statement.md`.  The actual project has two additional
inherited hypotheses that the blind task intentionally did not receive:

1. \(w_U\) is supported on a fixed positive dilation of \(M\); and
2. \(B_j\) is evaluated on the unique nonwrapping physical lift containing
   that support.

For \(w_U(\ell)\ne0\), these hypotheses give

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor
 \asymp \sqrt{NM}=K,
 \qquad 2\kappa(\ell)<N<q=4N
\]

for all sufficiently large \(X\), and the whole supported set of such
\(\kappa(\ell)\) lies in an interval of length \(O(K)<q\).  By the inherited
physical-lift convention that interval is contained in the chosen lift.
Consequently

\[
 w_U(\ell)\ne0
 \quad\Longrightarrow\quad
 \mathbf 1_{\kappa(\ell)\in\mathcal L}=1,
\]

so the indicator contributes identically one to every actual-project term.
It must not be retained as a new condition in the project formula.

The other seams are also exact.  The nearest-cell intervals are

\[
 \boxed{\kappa^2-\kappa+1\le N\ell\le\kappa^2+\kappa},
\]

with both inequalities closed on integers and with the equivalent real
nearest-cell interval strict at both half-integers.  The positive and
negative Abel formulas have respectively the right and left outer endpoint,
and both moving atoms have positive sign.  Recombining all six lines for each
\((d,v)\), then adjoining the complete zero and Nyquist rows and applying the
all-\(d\), all-\(v\) inversion, gives

\[
 \boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|\kappa(\ell)^2-N\ell|\le2V}.}
\tag{159.RL1}
\]

The paired-interior matrix is exactly

\[
 \boxed{\mathcal I_U(V)=\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal Y_U(V),}
\tag{159.RL2}
\]

where \(\mathcal Z_U\) and \(\mathcal Y_U\) are the whole zero and Nyquist
rows with the original normalization.  Each is subtracted once and only
once.  Formula (159.RL1) is precisely the hard dyadic defect block of the
Round 154 common-profile selected wave.  No boundary-frozen trace profile
survives the full recombination.

This review proves the finite identity and its normalization, not the signed
analytic bound.  The first open step is the \(M^{3/4}X^\varepsilon\) raw
estimate (equivalently the \(X^\varepsilon\) scalar estimate) for the exact
variable residual mask.

## 2. Exact statement and hypotheses

Retain

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2},
\tag{159.RL3}
\]

and, for each odd \(d\mid N\),

\[
 c=\frac{4N}{d},\qquad H=\frac c2.
\]

Let

\[
 m_j(x)=\mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1},
\qquad
 F_j(x)=w_U\!\left(\frac{x^2-j}{N}\right)
 e(\sqrt{x^2-j}-x),
\]

and \(B_j=m_jF_j\), with the actual real profile extended by zero across
all inherited components, transitions, half-open choices, and hard support
endpoints.  Besides its BV bound, the actual profile obeys the inherited
fixed-dilation support condition

\[
 \operatorname {supp}(w_U)\subset [\alpha M,\beta M]
\tag{159.RL4}
\]

inside a fixed positive ambient dilation (individual inherited components
may be disconnected), for constants independent of \(N,M,V\).  Equivalently,
the selected roots on profile support lie in the \(O(K)\) physical interval
used in Round 154.  Let \(\mathcal L_U\) be the inherited complete system of
\(q\) consecutive representatives chosen so that this positive physical
interval does not wrap modulo \(q\).  This lift/support compatibility, not
the BV inequality alone, is the decisive actual-project hypothesis.

The signed integer blocks are

\[
 J_+=[a_+,b_+],\quad
 a_+=\lfloor V\rfloor+1,\quad b_+=\lfloor2V\rfloor,
\]

and

\[
 J_-=[a_-,b_-],\quad
 a_-=-\lfloor2V\rfloor,\quad b_-=-\lfloor V\rfloor-1.
\tag{159.RL5}
\]

For fixed \(d,v\), write \(K_j=K(-v^2,-j;c)\) and

\[
 P^+(j)=\sum_{s=a_+}^{j}K_s,
 \qquad
 P^-(j)=\sum_{s=j}^{b_-}K_s.
\]

The complete-frequency identity is used exactly in the all-divisor form
printed as (159.BL6).  It is not asserted divisor by divisor.

## 3. Proof and derivation

### 3.1 Independent six-line Abel reconstruction

On the positive block,

\[
 K_j=P^+(j)-P^+(j-1),
\]

so finite summation gives

\[
 \sum_{j=a_+}^{b_+}\widehat B_j(2dv)K_j
 =P^+(b_+)\widehat B_{b_+}(2dv)
 +\sum_{j=a_+}^{b_+-1}P^+(j)
  \bigl(\widehat B_j-\widehat B_{j+1}\bigr)(2dv).
\tag{159.RL6+}
\]

For \(j>0\), \(m_j-m_{j+1}=\mathbf1_{x=j+1}\).  Hence

\[
 B_j-B_{j+1}=T_j^++R_j^+,
\]

where

\[
 T_j^+(x)=\mathbf1_{x=j+1}F_j(x),
 \qquad
 R_j^+(x)=m_{j+1}(x)\bigl(F_j(x)-F_{j+1}(x)\bigr).
\tag{159.RL7+}
\]

Thus (159.RL6+) is the positive right outer line, the positive moving
line, and the positive literal profile-phase difference line.

On the negative block,

\[
 K_j=P^-(j)-P^-(j+1),
\]

and therefore

\[
 \sum_{j=a_-}^{b_-}\widehat B_j(2dv)K_j
 =P^-(a_-)\widehat B_{a_-}(2dv)
 +\sum_{j=a_-+1}^{b_-}P^-(j)
  \bigl(\widehat B_j-\widehat B_{j-1}\bigr)(2dv).
\tag{159.RL6-}
\]

For \(j<0\), \(m_j-m_{j-1}=\mathbf1_{x=-j}\), whence

\[
 B_j-B_{j-1}=T_j^-+R_j^-,
\]

with

\[
 T_j^-(x)=\mathbf1_{x=-j}F_j(x),
 \qquad
 R_j^-(x)=m_{j-1}(x)\bigl(F_j(x)-F_{j-1}(x)\bigr).
\tag{159.RL7-}
\]

This is the negative left outer line, the positive negative-block moving
line, and the literal negative-block profile-phase difference line.  Linear
Fourier transformation preserves these pointwise identities.  Adding the
three positive and three negative lines recovers the original coefficient
for every fixed odd \(d\mid N\) and every fixed \(v\bmod H\).  Zero extension
keeps every internal component transition inside \(F_j-F_{j\pm1}\); there is
no additional profile endpoint to add.

### 3.2 All-divisor normalization and exactly one row subtraction

Put

\[
 C_d=-\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c.
\]

After the preceding reconstruction, the paired-interior quantity is

\[
 \mathcal I_U(V)=
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}C_d
 \sum_{j\in J_+\cup J_-}
 \sum_{\substack{v\bmod H\\v\ne0,H/2}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{159.RL8}
\]

Define the whole rows with the same \(C_d\), the same \(j\)-set, and the
same divisor sum:

\[
 \mathcal Z_U(V)=
 \sum_d C_d\sum_j\widehat B_j(0)K(0,-j;c),
\]

\[
 \mathcal Y_U(V)=
 \sum_d C_d\sum_j\widehat B_j(2N)
 K\!\left(-(H/2)^2,-j;c\right).
\tag{159.RL9}
\]

The Nyquist Fourier argument is exact because

\[
 2d(H/2)=dH=2N=q/2.
\]

Therefore \(\mathcal I_U+\mathcal Z_U+\mathcal Y_U\) is exactly the
all-\(v\bmod H\), all-odd-\(d\mid N\) left side of (159.BL6), summed over
\(J_+\cup J_-\).  Complete-frequency inversion gives

\[
 \mathcal I_U+\mathcal Z_U+\mathcal Y_U
 =\sum_{j\in J_+\cup J_-}\sum_{x\bmod q}
 B_j(x)G_N(x^2-j)=\mathcal S_U(V),
\]

which proves (159.RL2).  The inversion consumes the complete prefactor,
the \(d\sqrt c\) weight, and all frequency multiplicity.  No factor \(q\),
\(N\), \(2\), or complementary-representative multiplicity remains.
Recombination was done separately for each \((d,v)\), but inversion is
correctly used only after the complete \(d\)- and \(v\)-sums are restored.

This also agrees with the accepted two-stage normalization: first subtract
the zero row from the full physical row, then subtract the unique
self-complementary Nyquist row from the remaining nonzero matrix.  There is
no second centering subtraction.  When \(c=4\), \(H=2\) and the interior
residue set is empty; the two rows exhaust that fibre, which is an endpoint
check rather than a source of an extra factor.

### 3.3 Exact nearest cell and hard dyadic endpoints

For a nonzero physical term put

\[
 \ell=\frac{x^2-j}{N}.
\]

The selector \(G_N\) makes \(\ell\in\mathbb Z\) and contributes
\(\chi_4(\ell)\).  Substitution of \(j=x^2-N\ell\) into the physical mask
gives

\[
 -x\le x^2-N\ell\le x-1
 \quad\Longleftrightarrow\quad
 x^2-x+1\le N\ell\le x^2+x.
\tag{159.RL10}
\]

The intervals

\[
 [x^2-x+1,x^2+x]\cap\mathbb Z,\qquad x=1,2,\ldots,
\]

partition the positive integers: the upper endpoint for \(x\) is
\(x^2+x\), and the next lower endpoint is \(x^2+x+1\).  Equivalently,

\[
 x-\frac12<\sqrt{N\ell}<x+\frac12.
\tag{159.RL11}
\]

Both half-integer inequalities in (159.RL11) are strict.  A tie would make
\(4N\ell\) an odd square, impossible modulo \(4\).  The blind report's weak
lower sign describes the same integer set only because this tie is
impossible; (159.RL11) is the exact endpoint statement.

It follows that

\[
 x=\kappa(\ell),\qquad j=r(\ell)=\kappa(\ell)^2-N\ell
\]

with multiplicity one, and conversely every such selected pair satisfies
the physical cell.  The signed blocks (159.RL5) give exactly

\[
 j\in J_+\cup J_-
 \quad\Longleftrightarrow\quad
 V<|r(\ell)|\le2V.
\tag{159.RL12}
\]

Thus the inner defect endpoint is strict and the outer endpoint is closed
on both signs.  If

\[
 \delta(\ell)=\sqrt{N\ell}-\kappa(\ell)\in(-1/2,1/2),
\]

then

\[
 r(\ell)=-\delta(\ell)\bigl(2\kappa(\ell)+\delta(\ell)\bigr),
\tag{159.RL13}
\]

so the defect cutoff remains the exact variable band; no fixed fractional
interval has been substituted.

### 3.4 Why the actual lift indicator is identically one

From the fixed-dilation support (159.RL4), every nonzero selected summand
satisfies

\[
 \sqrt{\alpha NM}-\frac12
 \le \kappa(\ell)
 \le \sqrt{\beta NM}+\frac12.
\tag{159.RL14}
\]

Hence the supported roots occupy one positive ambient interval of length
\(O(K)\).  Moreover

\[
 \frac{K}{N}=\sqrt{\frac MN}\le N^{-1/4},
\]

so, for sufficiently large \(X\), the stronger Round 154 nonwrapping fact
\(2\kappa(\ell)<N\) holds throughout support.  In particular the interval
has length less than \(q=4N\), and no two of its integers are congruent
modulo \(q\).  The inherited physical lift is precisely the complete lift
containing this positive interval.  Therefore

\[
 w_U(\ell)\ne0
 \quad\Longrightarrow\quad \kappa(\ell)\in\mathcal L_U.
\tag{159.RL15}
\]

For the bounded initial values before the displayed asymptotic inequality,
the defining nonwrapping-lift convention itself supplies the same
containment; alternatively they are harmless finite cases in the asymptotic
estimate.  Thus deleting the lift indicator changes no actual-project term.

The blind countermodel moves a BV bump to an arbitrarily large
\(\ell_0\) after the lift has been fixed.  That is admissible under
(159.BL3) alone, but it violates (159.RL4) and the inherited physical-lift
compatibility.  It establishes a real statement-only omission, not a defect
in the actual-project compression.

### 3.5 Restoration of the Round 154 common-profile wave

At the unique selected pair,

\[
 w_U\!\left(\frac{x^2-j}{N}\right)=w_U(\ell),
\qquad
 e(\sqrt{x^2-j}-x)
 =e(\sqrt{N\ell}-\kappa(\ell))=e(\sqrt{N\ell}),
\]

because \(\kappa(\ell)\in\mathbb Z\).  Together with (159.RL12), this
proves (159.RL1).  The character automatically kills even \(\ell\), so it
is identical to the odd-\(n\) convention in Round 154.  Under the inherited
identification of the quotient weight

\[
 w_U(\ell)=\ell^{-3/4}A_U(\ell)
\]

(including its zero extension and localization), (159.RL1) is exactly the
hard dyadic \(V<|r|\le2V\) portion of (154.C2).  Its phase also agrees with
the defect-coordinate form (154.C4), since

\[
 e(\sqrt{N\ell})
 =e\!\left(-\frac{r(\ell)}
 {\kappa(\ell)+\sqrt{\kappa(\ell)^2-r(\ell)}}\right).
\]

Thus the complete sequence is important: the six Abel lines first recover
the original paired-interior coefficients; the two whole rows are then
adjoined exactly once; only the resulting complete-frequency object inverts
to the Round 154 common-profile wave.  The paired-interior matrix by itself
is that wave minus the two rows, as in (159.RL2).  This recombination does
not revise either isolated moving-trace formula; it shows only that their
boundary profiles disappear after all commutator pieces are put back
together.

### 3.6 Target calibration

The actual profile scale is \(M^{-3/4}X^\varepsilon\).  Therefore a uniform
raw signed bound of size

\[
 M^{3/4}X^\varepsilon
\]

for the unscaled selected residual-mask wave gives the normalized scalar
target \(\mathcal S_U(V)\ll X^\varepsilon\).  The already closed whole rows
are each \(O(M^{-1/4}X^\varepsilon)\), so (159.RL2) has the same target once
the full selected scalar is bounded.  The support count
\(O_\varepsilon(\min(M,V)X^\varepsilon)\) is only unsigned capacity and is
not this raw theorem.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the lift deletion, nearest-cell
partition, six-line reconstruction, complete-frequency normalization, or
single subtraction of the zero and Nyquist rows under the inherited actual
project hypotheses.

The first unproved step is the signed estimate

\[
 \left|
 \sum_{\ell}\chi_4(\ell)\widetilde w_U(\ell)e(\sqrt{N\ell})
 \mathbf1_{V<|\kappa(\ell)^2-N\ell|\le2V}
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{159.RL16}
\]

uniformly for the literal common profile and the allowed \(N,M,V\), with
\(\widetilde w_U\) normalized to bounded BV size.  The residual mask has
the moving endpoints (159.RL13).  A Fourier argument would still have to
control its \(\kappa\)-dependent coefficients, both hard boundary surfaces,
the strict/closed convention, truncation error, and every nonzero shifted
phase.  Neither lift uniqueness nor support cardinality supplies the needed
signed cancellation.  Thus no global target and no new strict
owner-complete range is proved here.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal six-line Abel package | **PASS.** Equations (159.RL6+)--(159.RL7-) independently recover three lines on each sign. |
| positive/negative outer endpoints and signs | **PASS.** The positive outer endpoint is \(b_+\), the negative outer endpoint is \(a_-\), and both moving atoms enter positively. |
| profile differences and transitions | **PASS.** The literal \(F_j-F_{j+1}\) and \(F_j-F_{j-1}\) retain profile, phase, zero-extension, component, and support transitions. |
| nearest-cell endpoints | **PASS.** The integer cell is closed as in (159.RL10); the corresponding half-integer interval is strict at both ends.  The intervals partition all positive integers. |
| physical lift | **PASS FOR THE ACTUAL PROJECT.** Fixed-dilation support plus the inherited nonwrapping lift proves (159.RL15), so the lift indicator is redundant.  **Required only for the stripped blind hypotheses.** |
| all-\(d\), all-\(v\) complete-frequency normalization | **PASS.** Recombination is per \((d,v)\); inversion is applied to the full divisor and frequency sums and consumes every exterior factor exactly. |
| zero and Nyquist subtraction | **PASS.** The two whole rows are adjoined before inversion and subtracted once in (159.RL2); no whole-row estimate is transferred to an Abel piece. |
| complementary representatives and \(c=4\) | **PASS.** No pair folding or factor two is used.  For \(c=4\), the two exceptional rows exhaust the fibre and the interior is empty. |
| quotient profile and phase | **PASS.** The recombined wave has \(w_U(\ell)\), not either boundary trace profile, and \(e(-\kappa)=1\) only by integrality. |
| defect signs and hard endpoints | **PASS.** Both signs are retained through \(V<|r|\le2V\), with the exact variable band (159.RL13). |
| Round 154 selected-wave seam | **PASS.** After exact row adjunction, (159.RL1) is the hard dyadic block of the Round 154 common-profile wave; the paired interior is that block minus the two closed rows. |
| scalar/raw target | **PASS AS CALIBRATION; OPEN AS AN ESTIMATE.** The normalized target is \(X^\varepsilon\) and the raw target is \(M^{3/4}X^\varepsilon\). |
| downstream scope | **PASS.** No conclusion is transferred outside this full paired-interior \(D=d=L=1\) matrix seam. |

No computation or external source was used.

## 6. Dependencies and exact artifacts used

This review read and used only:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/blind_statement.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/blind_full_abel_rederivation.md`;
5. `proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/hostile_profile_scope_round157.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_exact_root_defect_reparametrization.md`; and
8. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/candidates/conductor_round159_common_profile_seed.md`.

No proof graph, proof draft, validation matrix, synthesis, strategy file,
unlisted Round 159 report, web source, or computation was inspected.  No
shared state was edited.

## 7. Recommended state effect

**Promote the narrow finite algebraic package after conductor validation;
do not promote an analytic target or range.**  The promotable package is:

1. the exact positive and negative three-line Abel reconstructions;
2. exact recombination before estimation for every \((d,v)\);
3. the all-\(d\), all-\(v\) normalization and the identity
   \(\mathcal I_U=\mathcal S_U-\mathcal Z_U-\mathcal Y_U\), with each whole
   row removed exactly once;
4. nearest-cell multiplicity one with the exact asymmetric integer endpoints;
5. removal of the lift indicator under the inherited actual-project
   fixed-dilation/nonwrapping-lift hypotheses; and
6. identification of \(\mathcal S_U(V)\) with the Round 154 common-profile
   selected defect wave on the hard dyadic block.

Retain the blind report's indicator formula and countermodel as a valid
diagnosis of the deliberately stripped statement, but reject the lift issue
as the first obstruction in the actual project.  Revise the actual first
open step to (159.RL16), including the variable-mask boundary and truncation
seams.  Make no promotion of the paired-interior target, any new strict
    range, \(D>1\), \(L>1\), generic \(t=1\), \(t\ge2\), cross terms, another M1
or M2 owner, endpoint uniformity, M9, the bridge, the final target, or either
global exponent.

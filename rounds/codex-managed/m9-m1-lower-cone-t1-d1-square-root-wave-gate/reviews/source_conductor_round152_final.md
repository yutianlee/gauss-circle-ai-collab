# Round 152 terminal primary-source review

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Reviewed candidate: `candidates/conductor_round152_square_root_wave_reduction.md`
- Role: independent terminal primary-source and theorem-hypothesis reviewer
- Starting claim-graph SHA-256: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Terminal verdict: **GREEN**

## 1. Result

The critical external-source inference is valid.  Bourgain's Theorem 6,
not merely the shorter direct window in his Theorem 4, supplies the global
exponent pair

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right).
\tag{152.SF1}
\]

Tao--Trudgian--Yang Lemma 14 gives the exact Sargos transform

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right).
\tag{152.SF2}
\]

The maximum in that lemma causes no missing interval: its auxiliary line
is strictly below the line belonging to (152.SF2) throughout
\(0\leq\alpha\leq 1/2\).  Tao--Trudgian--Yang Remark 16, using the
symmetry displayed in their equation (9), and Lemma 15 therefore make
(152.SF2) a global exponent pair.  Their Lemma 13 may then be applied,
in that order, to give

\[
 B D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =B\!\left(\frac{18}{199},\frac{593}{796}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{152.SF3}
\]

The square-root progression phase satisfies the model-phase and
\(T\geq H\) hypotheses, the sources give estimates uniformly for proper
subintervals, and the project profile is inserted only after the
unweighted interval estimate by Abel summation.  Consequently (152.SF3)
gives exactly

\[
 \boxed{
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon.}
\tag{152.SF4}
\]

The new threshold is strictly below the older transformed
Tao--Trudgian--Yang threshold, because

\[
 \frac{1424}{819}-\frac{780}{449}
 =\frac{556}{367731}>0.
\tag{152.SF5}
\]

Thus the candidate's strict new scale sliver is source-legal.  Every cited
alternative source is also correctly classified as either a self-return or
a direct-specialization no-match.  No source or theorem-hypothesis gap was
found, so the required red-on-gap rule is not triggered.

Two bibliographic wording corrections are non-blocking.  First, in the
2026 Kaczorowski--Perelli paper it is definition (1.3), rather than
Theorem 1 by itself, that imposes
\(\sum_\nu d_\nu\kappa_\nu=1\); Theorem 1 is stated for \(N\geq2\).
Second, Lutsko--Sourmelidis--Technau Theorem 1.3 itself contains the
half-open endpoint convention, while their Lemma 1.4 is the partial-
summation lemma used to transfer an unweighted bound to a weighted one.
Neither correction changes any inference in the candidate.

## 2. Exact source statements and hypotheses

### 2.1 Bourgain pair and its scope

In Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
Theorem 4 is the direct estimate in the window

\[
 \mathcal T^{17/42}\leq H\leq \mathcal T^{1/2}.
\tag{152.SF6}
\]

Section 5 then addresses the ranges and interval issue not covered by that
direct calculation: near-square rescaling, the pair \((1/2,1/2)\) in the
extreme long range, a Poisson/partial-summation \(B\)-process in the
remaining long range, and phase extension plus the cited Sargos
partial-sum device for a proper subinterval.  The resulting Theorem 6
states that (152.SF1) is an exponent pair.  Therefore (152.SF6) is not an
additional hypothesis on the theorem used here.  The \(+\varepsilon\)
perturbations are absorbed into the project's \(X^\varepsilon\).

The square-root phase used below has explicit nonvanishing derivatives of
the required scale on a fixed compact interval, so it lies in Bourgain's
standard exponent-pair derivative class.  The application does not rely on
Bourgain's Theorem 5, which is a pointwise zeta-function statement.

### 2.2 Tao--Trudgian--Yang statements

The current primary arXiv version of Terence Tao, Tim Trudgian, and Andrew
Yang,
[*New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
has the following exact interfaces.

1. Definition 5 gives the model-phase derivative normalization, with
   \(F^{(p+1)}(u)\) approximating the \(p\)-th derivative of
   \(u^{-\sigma}\), for fixed \(\sigma>0\).
2. Definition 9 takes the supremum over intervals in the dyadic block.
   Definitions 11 and 12 formulate exponent-pair estimates for every
   interval \(I\subset[H,2H]\), with \(T\geq H\geq1\), including the
   finite-derivative epsilon form used in applications.
3. Lemma 13 states that \(A,B,C\) preserve exponent pairs and records
   \(B(k,\lambda)=(\lambda-1/2,k+1/2)\).
4. Lemma 14 states

   \[
   \beta(\alpha)\leq
   \max\left\{
      k_1+\alpha(\lambda_1-k_1),
      \frac1{12}+\frac23\alpha
   \right\},
   \tag{152.SF7}
   \]

   where

   \[
   D(k,\lambda)=(k_1,\lambda_1)=
   \left(
    \frac{5k+\lambda+2}{8(5k+3\lambda+2)},
    \frac{29k+21\lambda+10}{8(5k+3\lambda+2)}
   \right).
   \tag{152.SF8}
   \]

5. Lemma 15 says that \((k,\lambda)\) is an exponent pair precisely when
   \(\beta(\alpha)\leq k+(\lambda-k)\alpha\) on \([0,1]\).
   Remark 16 says that if \(\lambda-k\geq1/2\), it suffices, by the
   symmetry (9), to verify this on \([0,1/2]\).
6. Table 1 prints

   \[
   \beta(\alpha)\leq
   \frac{18}{199}+\frac{521}{796}\alpha,
   \qquad
   \frac{1508}{3825}\leq\alpha<
   \frac{62831}{155153},
   \tag{152.SF9}
   \]

   and attributes this line to
   \(D(13/84,55/84)=(18/199,593/796)\).
   Theorem 20 separately prints the four new exponent pairs, including
   \((89/1282,997/1282)\).

These are statements in the current primary source, not an inference from
a secondary exponent-pair table.

### 2.3 Literal project specialization

On either exact odd residue class \(\ell=4n+a\), \(a\in\{1,3\}\), and
on one fixed dyadic/support component, put

\[
 H\asymp M,\qquad T=\sqrt{NH}\asymp R^2M^{1/2},\qquad
 F_{a,H}(u)=2\sqrt{u+\frac{a}{4H}}.
\tag{152.SF10}
\]

Then, identically,

\[
 T F_{a,H}(n/H)=\sqrt{N(4n+a)}.
\tag{152.SF11}
\]

Moreover

\[
 F_{a,H}^{(p+1)}(u)
 =\frac{d^p}{du^p}u^{-1/2}+O_p(H^{-1})
\tag{152.SF12}
\]

uniformly on the fixed compact support.  Hence this is a model phase with
\(\sigma=1/2\).  Bounded \(M\) is already owned, so the error in
(152.SF12) tends to zero in the range under review.  Also

\[
 \frac TH=\sqrt{\frac NH}\asymp R^2M^{-1/2}\gg R\geq1
 \qquad(M\leq R^2),
\tag{152.SF13}
\]

up to the harmless fixed support constants.  Thus the source convention
\(T\geq H\) has a power margin; there is no comparable-edge patch hidden
in this application.

The zero-extended actual profile is

\[
 W_U(\ell)=\ell^{-3/4}A_U(\ell),\qquad
 \|W_U\|_\infty+\operatorname {Var}W_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{152.SF14}
\]

Sampling it on either progression cannot increase its total variation.
One first applies the unweighted exponent-pair estimate to every proper
subinterval and only then applies Abel summation using (152.SF14).  No
external theorem is being asked to accept an arbitrary bounded
coefficient.  The exact mod-four split also makes \(\chi_4(4n+a)\) a
constant before the unweighted theorem is invoked.

## 3. Proof and power reproduction

### 3.1 The exact \(D\) and \(BD\) pairs

For \((k,\lambda)=(13/84,55/84)\), the common expression in (152.SF8) is

\[
 5k+3\lambda+2
 =\frac{65+165+168}{84}=\frac{199}{42}.
\tag{152.SF15}
\]

The two numerators are

\[
 5k+\lambda+2=\frac{24}{7},
 \qquad
 29k+21\lambda+10=\frac{593}{21}.
\tag{152.SF16}
\]

Since \(8(5k+3\lambda+2)=796/21\), equations (152.SF15)--(152.SF16)
give (152.SF2).  Its affine line is

\[
 \frac{18}{199}+
 \left(\frac{593}{796}-\frac{18}{199}\right)\alpha
 =\frac{18}{199}+\frac{521}{796}\alpha.
\tag{152.SF17}
\]

Subtracting the other line in the Lemma-14 maximum gives

\[
 \left(\frac{18}{199}+\frac{521}{796}\alpha\right)
 -\left(\frac1{12}+\frac23\alpha\right)
 =\frac{17-29\alpha}{2388}
 \geq\frac5{4776}>0
\tag{152.SF18}
\]

for \(0\leq\alpha\leq1/2\).  Also
\(593/796-18/199=521/796>1/2\).  Lemma 15 and Remark 16 therefore turn
the lower-half estimate into the global exponent pair (152.SF2).
Only after that global conclusion is obtained does Lemma 13 give

\[
 B\!\left(\frac{18}{199},\frac{593}{796}\right)
 =\left(\frac{593}{796}-\frac12,
        \frac{18}{199}+\frac12\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{152.SF19}
\]

This verifies both the order and the placement of the \(B\)-process.

### 3.2 General square-root power and all specializations used

An exponent pair \((k,\lambda)\), applied before the weight, gives

\[
 \left(\frac TH\right)^kH^\lambda
 \asymp
 (R^2M^{-1/2})^kM^\lambda.
\tag{152.SF20}
\]

After (152.SF14),

\[
 |P_U|\ll_\varepsilon
 R^{2k}M^{\lambda-k/2-3/4}X^\varepsilon.
\tag{152.SF21}
\]

The power ledger reproduces as follows.

| Input | Bound for the literal weighted \(P_U\) |
|---|---|
| Trivial primal and reciprocal capacities | \(\min\{M^{1/4},RM^{-1/2}\}X^\varepsilon\) |
| Second derivative | \((RM^{-1/2}+R^{-1})X^\varepsilon\) |
| Third derivative / classical \((1/6,2/3)\) | \((R^{1/3}M^{-1/6}+R^{-1/3}M^{1/6})X^\varepsilon\); its exponent-pair term is \((R^2/M)^{1/6}X^\varepsilon\) |
| Bourgain \((13/84,55/84)\) | \((R^{52}/M^{29})^{1/168}X^\varepsilon\) |
| Direct TTY \((89/1282,997/1282)\) | \((R^{178}/M^9)^{1/1282}X^\varepsilon\) |
| \(B(89/1282,997/1282)=(178/641,365/641)\) | \((R^{1424}/M^{819})^{1/2564}X^\varepsilon\) |
| \(BD(13/84,55/84)\) | \((R^{780}/M^{449})^{1/1592}X^\varepsilon\) |

For the last row, (152.SF21) gives

\[
 2k=\frac{390}{796},
\qquad
 \lambda-\frac{k}{2}-\frac34
 =\frac{940-195-1194}{1592}
 =-\frac{449}{1592},
\tag{152.SF22}
\]

which is exactly (152.SF4).  The other three pairs printed in
Tao--Trudgian--Yang Theorem 20, after \(B\), reproduce the source report's
remaining rows

\[
 \left(\frac{R^{10971152}}{M^{6294987}}\right)^{1/19427972},
 \quad
 \left(\frac{R^{1032884}}{M^{566241}}\right)^{1/1404384},
 \quad
 \left(\frac{R^{26528}}{M^{14437}}\right)^{1/34780}.
\tag{152.SF23}
\]

Their threshold ratios are all larger than \(780/449\).  Direct use of
the four Theorem-20 pairs is also weaker for this weighted square-root
sum; the first direct row is displayed above, while the third and fourth
even have a positive residual \(M\)-power.  Thus the improvement really
comes from the Lemma-14 \(D\)-line followed by \(B\).

### 3.3 Exact Table-1 cell and strict old-boundary comparison

Write \(M=R^\mu\).  On the reciprocal side,

\[
 Q\asymp R^2M^{-1/2},\qquad
 T_0\asymp R^2M^{1/2},\qquad
 \alpha=\frac{\log Q}{\log T_0}=\frac{4-\mu}{4+\mu}.
\tag{152.SF24}
\]

The prefactor \(N^{-1/4}\) makes the target line
\(\beta(\alpha)\leq(1+\alpha)/4\).  Equating it with (152.SF9) gives

\[
 4\left(\frac{18}{199}+\frac{521}{796}\alpha\right)
 =1+\alpha,\qquad
 \alpha=\frac{127}{322},\qquad
 \mu=4\frac{1-\alpha}{1+\alpha}=\frac{780}{449}.
\tag{152.SF25}
\]

This crossing is strictly inside the printed Table-1 cell.  The exact
cross-products are

\[
 127\cdot3825-1508\cdot322=199>0,
\tag{152.SF26}
\]

\[
 62831\cdot322-127\cdot155153=527151>0.
\tag{152.SF27}
\]

Finally,

\[
 780\cdot819=638820<639376=1424\cdot449,
\tag{152.SF28}
\]

which proves (152.SF5).  Hence
\(M^{449}\gg R^{780}\) starts strictly before the already owned condition
\(M^{819}\gg R^{1424}\).  This is an upper-bound owner and a first exact
boundary for the audited exponent-pair envelope, not a signed lower bound
or a literature impossibility theorem below the boundary.

### 3.4 Mellin/Poisson normalization and self-return

For the primitive odd real character \(\chi_4\), direct calculation gives

\[
 \tau(\chi_4)=2i,\qquad
 \varepsilon(\chi_4)=\frac{\tau(\chi_4)}{i\sqrt4}=1,
\tag{152.SF29}
\]

and

\[
 \Lambda(s,\chi_4)=
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi_4)
 =\Lambda(1-s,\chi_4).
\tag{152.SF30}
\]

The Mellin spectral height is
\(T_0=\sqrt{NM}\asymp R^2M^{1/2}\), its band has comparable width, the
analytic conductor is \(\asymp4T_0\), and a balanced approximate
functional equation has length
\(T_0^{1/2}\asymp RM^{1/4}\).  The unit-scale stationary Mellin transform
has size \(T_0^{-1/2}\); after the outer \(M^{-1/4}\), even a hypothetical
Lindelof pointwise input leaves

\[
 M^{-1/4}T_0^{1/2}\asymp R.
\tag{152.SF31}
\]

Using the functional equation without taking absolute values produces the
unbalanced length

\[
 T_0/M\asymp\sqrt{N/M}\asymp Q,
\tag{152.SF32}
\]

the same dual scale as exact character Poisson summation.  In the latter,
the stationary point is \(x_q=4N/q^2\), the phase is \(N/q\), and

\[
 x_q^{-3/4}|\phi''(x_q)|^{-1/2}=2N^{-1/4}.
\tag{152.SF33}
\]

Together with the character Gauss factor and stationary Gaussian unit this
gives the candidate's \(e(1/8)N^{-1/4}\) principal transform.  Its dual
main wave is not an error; applying the principal transform again returns
the original phase and symbol.  This validates the cited self-return/no-
automatic-gain conclusion and all scales \(T_0,Q,RM^{1/4}\), and \(R\).

## 4. Exact no-match audit

The following conclusions were checked against the current primary texts.
They are direct-specialization no-matches, not claims that no future
argument can use the same ideas.

1. **Mixed Burgess.**  Heath-Brown and Pierce,
   [*Burgess bounds for short mixed character sums*](https://arxiv.org/html/1404.1677v1),
   Theorems 1.2--1.8, treat a nonprincipal character to a prime modulus and
   a real polynomial phase of fixed degree, with savings expressed through
   the modulus.  Their discussion says a suitable smooth phase might in
   principle be approached by polynomial approximation, but prints no
   uniform square-root-phase theorem of the required kind.  Here the
   modulus is the fixed composite modulus four, so their theorem cannot
   supply a growing \(R,M\) saving.  Splitting the two residue classes is
   the exact applicable operation.
2. **Pointwise Dirichlet \(L\).**  Bourgain Theorem 5 is for
   \(\zeta(1/2+it)\), not the localized fixed-character wave.  More
   importantly, the stronger hypothetical Lindelof input still leaves the
   loss (152.SF31), so changing the known pointwise exponent cannot close
   this route.
3. **Higher Voronoi.**  Miller and Schmid,
   [*A general Voronoi summation formula for \(GL(n,\mathbb Z)\)*](https://arxiv.org/html/0912.1065v1),
   Theorem 1.10, requires Fourier--Whittaker coefficients of a cuspidal
   automorphic representation and produces its divisor variables and
   hyper-Kloosterman sums.  The literal coefficient here is the degree-one
   Dirichlet coefficient \(\chi_4(\ell)\) times the actual project profile,
   not a \(GL(2)\) or higher cuspidal Hecke sequence.  At degree one the
   applicable transform is character Poisson, already audited above.
4. **Nonlinear twists (2013).**  Kaczorowski and Perelli,
   [*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734v1),
   Theorems 1--5 and the discussion following (1.8), concern analytic
   continuation and polar structure of twists of a fixed \(L\)-function.
   They explicitly identify uniformity in twist parameters as necessary
   for smoothed-sum applications and do not provide the uniform growing
   \(\sqrt N\), scale-\(M\), actual-profile finite-sum estimate used here.
   For degree one the standard resonant exponent is linear; the square-root
   exponent is substandard.
5. **Multiple standard twists (2026).**  Kaczorowski and Perelli,
   [*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885v1),
   condition (1.3), defines standard multiple twists by
   \(\sum_\nu d_\nu\kappa_\nu=1\).  A single degree-one component therefore
   has \(\kappa=1\), not \(1/2\).  Theorem 1, stated for \(N\geq2\), is a
   meromorphic-continuation theorem and supplies no missing uniform finite-
   sum estimate.
6. **Boundary \(B\)-transform.**  Lutsko, Sourmelidis, and Technau,
   [*Pair correlation of the fractional parts of \(\alpha n^\theta\)*](https://content.ems.press/assets/public/full-texts/serials/jems/no-issue/14297682/online-first/10.4171-jems-1449-online-first.pdf),
   Theorem 1.3, is a genuine match for the half-open unweighted transform
   under its printed \(C^4\) second-through-fourth derivative conditions;
   Lemma 1.4 supplies partial summation.  It retains the entire dual main
   sum, endpoints, and errors.  Therefore it supports the principal
   transform but no claim that the self-returning dual wave is negligible.

No cited theorem accepts the wrong coefficient, a suppressed growing
parameter, an arbitrary bounded weight, or a dropped endpoint/main term in
the candidate.

## 5. First doubtful or unproved step

There is no doubtful external-theorem step in the strict-range proof.  Its
first project-side dependencies are the previously accepted actual-profile
bound (152.SF14) and the Round-148 boundary-complete transform ledger.
They were inspected as dependencies but are not reproved by any of the
external papers; without either accepted input, the corresponding project
specialization would have to be reopened.  In the active graph they are
frozen inputs, so this is not a source gap.

Below \(M^{449}\asymp R^{780}\), the first genuinely unproved continuation
is a target-sized signed estimate for the pruned square-root wave.  The
compulsory \(s=1\) layer and near-square survivor remain.  None of the
no-match sources above estimates that literal object.  This review does not
certify the separate arithmetic-pruning proof and does not turn a failure
of the audited methods into a lower bound.

The first textual imprecisions in the Round-152 source report are the two
non-blocking attributions identified in Section 1: condition (1.3), not
2026 Theorem 1 alone, imposes the standard-twist exponent balance, and the
half-open convention is in Lutsko--Sourmelidis--Technau Theorem 1.3 while
Lemma 1.4 handles partial summation.  Neither imprecision survives as a
mathematical or source-hypothesis omission in the candidate.

## 6. Required controls and outcomes

| Control | Outcome |
|---|---|
| Bourgain direct window versus global scope | **GREEN.** Theorem 4 has the direct window; Section 5 and Theorem 6 establish the exponent pair globally and handle long lengths and proper subintervals. |
| TTY Lemma 14 formula and maximum | **GREEN.** Both fractions in (152.SF8), the pair (152.SF2), and the positive gap (152.SF18) reproduce exactly. |
| Global \(D\) and \(BD\) inference | **GREEN.** Lemma 15 plus Remark 16/symmetry makes \(D\) global; Lemma 13 is then applied once, after \(D\), to obtain \(BD\). |
| Character and \(B\)-placement | **GREEN.** The mod-four character is made constant before the unweighted square-root estimate; the source \(B\)-process is not confused with character splitting. |
| Model-phase normalization | **GREEN.** Equations (152.SF10)--(152.SF12) give \(\sigma=1/2\) with the exact residue shift. |
| \(T\geq H\) | **GREEN.** \(T/H\asymp R^2M^{-1/2}\gg R\) throughout \(M\leq R^2\). |
| Proper intervals and endpoints | **GREEN.** TTY Definitions 9, 11, and 12 and Bourgain Section 5 are interval-uniform; zero extension and the half-open transform preserve endpoints. |
| Abel timing and actual profile | **GREEN.** The unweighted estimate precedes Abel; only the accepted BV norm (152.SF14) is used. |
| Every \(R,M\) power | **GREEN.** Equations (152.SF21)--(152.SF23) and the derivative/capacity table reproduce the candidate and source-report ledgers. |
| Table-1 location | **GREEN.** Both exact cross-product gaps (152.SF26)--(152.SF27) are positive. |
| Old/new boundary comparison | **GREEN.** The exact numerator gap is \(556\), as in (152.SF28). |
| Mellin conductor and duality | **GREEN/no gain.** Root number, conductor, AFE length, dual length, stationary amplitude, and residual \(R\) loss reproduce. |
| Every cited alternative | **GREEN as scoped match/no-match.** Mixed Burgess, pointwise \(L\), higher Voronoi, and both nonlinear-twist sources fail at the exact stated interfaces; the half-open \(B\)-transform matches but self-returns. |
| Downstream scope | **GREEN.** No \(D>1\), \(L>1\), generic, \(t\geq2\), Round-138 cross, M9--M1/M2, endpoint, M9, bridge, quarter-target, or global-exponent conclusion is inferred. |

No numerical experiment was used.

## 7. Dependencies and exact artifacts used

Repository artifacts inspected were:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `sources/bourgain_2017_exponent_pair.md`;
5. `sources/tao_trudgian_yang_2025.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_wave_source_audit.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_character_wave_attack.md`; and
8. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`.

The live primary sources checked were:

1. Bourgain, [arXiv:1408.5794v2](https://arxiv.org/html/1408.5794v2), especially Theorems 4--6 and Section 5;
2. Tao--Trudgian--Yang, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Definitions 5 and 9--12, Lemmas 13--15, equation (9), Remark 16, Table 1, and Theorem 20;
3. Heath-Brown--Pierce, [arXiv:1404.1677v1](https://arxiv.org/html/1404.1677v1), Theorems 1.2--1.8;
4. Miller--Schmid, [arXiv:0912.1065v1](https://arxiv.org/html/0912.1065v1), Theorem 1.10;
5. Kaczorowski--Perelli, [arXiv:1304.4734v1](https://arxiv.org/html/1304.4734v1), Theorems 1--5 and the smoothed-sum discussion;
6. Kaczorowski--Perelli, [arXiv:2603.13885v1](https://arxiv.org/html/2603.13885v1), condition (1.3) and Theorem 1; and
7. Lutsko--Sourmelidis--Technau, [JEMS online-first primary PDF](https://content.ems.press/assets/public/full-texts/serials/jems/no-issue/14297682/online-first/10.4171-jems-1449-online-first.pdf), Theorem 1.3 and Lemma 1.4.

No source card, report, candidate, claim-graph file, validation matrix,
synthesis, or proof draft was edited.

## 8. Recommended state effect

**Promote the strict source-legal square-root range, subject to the other
terminal seam reviews.**

The conductor may promote:

1. the global pair (152.SF3);
2. the literal bound (152.SF4) and target-safe condition
   \(M^{449}\gg R^{780}\);
3. only the previously unowned strict sliver below
   \(M^{819}\gg R^{1424}\), subtracting the old owner exactly once; and
4. the alternative routes only with the scoped self-return/no-match labels
   in Section 4.

Promotion must retain the exact mod-four split, model-phase normalization,
\(T\geq H\) margin, proper-interval quantifier, Abel-after-unweighted
order, actual BV profile, bounded-\(M\) exclusion, and all downstream scope
guards.  Leave the target below \(M^{449}\asymp R^{780}\) open.  Do not
promote a signed lower bound, an exponent-pair optimality theorem, or any
global Gauss-circle exponent from this scalar range.

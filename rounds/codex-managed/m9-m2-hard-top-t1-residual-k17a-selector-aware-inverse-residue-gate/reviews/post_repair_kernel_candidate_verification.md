# 1. Result

\[
 \boxed{\textbf{AMBER}}
\]

The repaired durable kernel, formalized candidate, and conductor
reconciliation agree mathematically. The quantified divisor summation in
(177.K26) is now correct in substance; the added positive-majorant
identities (177.K31a)--(177.K31b) and incomplete-lift ledger
(177.K32a)--(177.K32b) restore the claimed powers; and the candidate
explicitly excludes the open estimates (177.K34)--(177.K35) from
promotion.

One mechanical source defect prevents a GREEN verdict: the restriction in
the first line of (177.K26) contains a literal carriage-return control
character between the opening brace and the text “m odd”. Thus the source
does not contain the valid TeX command

\[
 \kappa\ {\rm odd}.
\]

Replacing that single malformed token exactly as specified in Section 4
makes the review GREEN. No mathematical statement, bound, complement, or
owner scope needs repair.

# 2. Exact statement and hypotheses

The object under verification is the complete literal Round-176
two-orientation identity restricted by

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa=\kappa_*<\delta L,\qquad
 (u,n)<\gamma L,
\]

with the residual coefficient

\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d)
\]

and both parity branches, squarefreeness, coprimality, Fejer weight,
opposing-displacement inequalities, profiles, floors, stars, hard values,
endpoint conjugations, one outer real part, and zero extension retained.

For

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad
 q={u_0\over(\ell,u_0)},
\]

the candidate proposes promotion only of:

1. the primitive anchor and folded alias identities (177.K5)--(177.K9);
2. the literal $O(u_0L)$ atom count and
   $O(Lq\log(2q))$ coefficient-weighted capacity;
3. the exact low-reduced-conductor packet
   $q\leq Q_B=(\log(2X))^B$;
4. its exact Fourier complement $q>Q_B$; and
5. the explicitly scoped positive-energy, lift-capacity, and failed
   orientation-pairing audits through (177.K33).

The formalized candidate says verbatim that (177.K34)--(177.K35) are
retained only as open sufficient estimates and are not proposed for
promotion. The conductor reconciliation makes the same separation.

# 3. Proof or derivation

## Quantified summation in (177.K26)

At fixed $(\kappa,u)$, (177.K25) gives

\[
 \sum_{u_0\mid u}
 \sum_{\substack{q\mid u_0\\q\leq Q_B}}
 Lq\log(2q)
 \ll LQ_B\log(2Q_B)\tau(u)^2.
\tag{V177.1}
\]

The repaired form of (177.K26) restores both quantifiers:

\[
 LQ_B\log(2Q_B)
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
 \sum_{u\asymp L/\kappa}\tau(u)^2.
\tag{V177.2}
\]

Since $u\ll L\leq X^{1/4}$, for every $\eta>0$,

\[
 \tau(u)^2\ll_\eta X^\eta.
\]

There are $O(L/\kappa)$ supported values of $u$, so (V177.2) is

\[
\begin{aligned}
 &\ll_\eta
 LQ_B\log(2Q_B)X^\eta
 \sum_{\kappa<\delta L}{L\over\kappa}\\
 &\ll_\eta
 L^2Q_B\log(2Q_B)\log(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{V177.3}
\]

Thus the formerly free $u$ is mathematically bound, and the epsilon
rebudget is valid. Oddness of $\kappa$ can be dropped in the upper bound.
The result is uniform in the stated fixed $B,\delta,\gamma$.

## Positive-majorant ledgers

At fixed $(\kappa,u,u_0)$, let $z$ run over all literal atoms from both
orientations and put

\[
 H_\ell=\sum_zA_ze(\ell b_z/u_0),\qquad
 B_b=\sum_{z:b_z=b}A_z.
\]

The exact identity

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2
\tag{V177.4}
\]

is unchanged. The literal atom count is $O(u_0L)$, hence the
coefficient-independent positive self-diagonal obeys

\[
 D=u_0\sum_z|A_z|^2
 \ll Lu_0^2X^\eta,
\qquad
 \sqrt D\ll u_0\sqrt L\,X^\eta,
\tag{V177.5}
\]

after harmless relabelling of $\eta$.

For a fixed bucket modulo $u_0$, the $v$ residue can take at most
$u_0$ unit values. Each has $O(g)$ lifts in a length-$U$ interval,
the corresponding $n_0$ residue has $O(1)$ lifts in a length-$u_0$
interval, and there are $O(\kappa)$ fibre sites. Since
$u=gu_0\asymp U=L/\kappa$, the bucket contains $O(L)$ atoms. Bucketwise
Cauchy therefore gives

\[
 u_0\sum_b|B_b|^2
 \ll u_0L\sum_z|A_z|^2
 \ll L^2u_0^2X^\eta.
\tag{V177.6}
\]

Equations (177.K31a)--(177.K31b) are correct. The kernel also states the
essential qualification: these are capacities of positive majorants, not
lower bounds for the exact signed energy, because cross terms inside a
bucket may cancel the displayed self-diagonal.

## Incomplete-lift ledger

At exact reduced conductor $q$, write

\[
 h={u_0\over q},\qquad u=ghq\asymp U.
\]

A fixed ordered pair $(v\bmod q,n_0\bmod q)$ has

\[
 O(U/q)=O(gh)
\]

$v$-lifts, $O(u_0/q)=O(h)$ determinant lifts, and
$O(\kappa)$ fibre sites. Its total lift multiplicity is therefore

\[
 O(\kappa gh^2)
 =O\!\left({Lh\over q}\right),
\tag{V177.7}
\]

because $\kappa ghq\asymp L$. For a fixed inverse-product residue there
are at most $\varphi(q)\leq q$ ordered unit residue pairs, so its bucket
contains

\[
 O(Lh)=O\!\left({Lu_0\over q}\right)
\tag{V177.8}
\]

literal atoms. Both orientations alter only the constant.

This verifies (177.K32a)--(177.K32b). In particular, completion modulo
$q$ cannot silently replace the physical length-$u$ ranges by one
primitive period. The earlier $O(u_0L)$ raw count and
$O(Lq\log(2q))$ coefficient-weighted capacity have already paid every
$g$- and $h$-lift.

## Promotion boundary

The formalized candidate promotes through (177.K33) only and explicitly
states:

\[
 \text{(177.K34)--(177.K35) are open and are not promoted.}
\]

The durable kernel says that no accepted theorem proves either estimate.
The conductor reconciliation identifies the same high-$q$ estimate as
the first open theorem. There is no implicit use of (177.K34) or
(177.K35) in (177.K12): the low-$q$ theorem follows entirely from the
positive count (177.K10), exact coefficient mass (177.K9), and quantified
sum (177.K25)--(177.K26).

# 4. First doubtful or unproved step

The first defect in the repaired artifact is mechanical, not
mathematical. In the source of (177.K26), the intended text

\[
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
\]

is stored as a backslash before $\kappa$, an opening brace, a literal
carriage-return byte, and then “m odd”. The exact repair is to replace the
malformed subscript by

\[
 \boxed{
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}.}
\tag{V177.9}
\]

No other source control character occurs in the candidate or conductor
reconciliation.

After that source repair, the first unproved mathematical step is exactly
(177.K34), or the stronger aliaswise (177.K35), on

\[
 q={u_0\over(\ell,u_0)}>Q_B.
\]

The positive-majorant and lift ledgers do not prove this estimate; they
only show why coefficient-blind Parseval, one square-root saving, or
lift-erasing completion is insufficient. The literal selector, endpoint
phases, and two orientations still require a new signed contraction.

# 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| K26 quantified $\kappa,u$ sum | **Mathematical pass.** Both sums are present and yield (V177.3). |
| K26 source integrity | **Fail, mechanical.** The odd-$\kappa$ condition contains one carriage-return control character; repair (V177.9) is required. |
| Epsilon rebudget | **Pass.** Choose $\eta$ below the final $\varepsilon$ and absorb fixed powers of $\log X$. |
| Positive self-diagonal (177.K31a) | **Pass.** $O(u_0L)$ atoms give $D\ll Lu_0^2X^\eta$ and $\sqrt D\ll u_0\sqrt L X^\eta$. |
| Positive bucket closure (177.K31b) | **Pass.** A modulus-$u_0$ bucket has $O(L)$ atoms, yielding $L^2u_0^2X^\eta$. |
| Cancellation qualification | **Pass.** Both ledgers are explicitly upper capacities, not literal lower bounds. |
| $v$-lift count | **Pass.** Length $U$ modulo $q$ gives $O(gh)$ lifts. |
| $n_0$-lift count | **Pass.** Length $O(u_0)$ modulo $q$ gives $O(h)$ lifts. |
| Fibre and combined lift count | **Pass.** Multiplication by $O(\kappa)$ gives $O(Lh/q)$ per ordered residue pair. |
| Inverse-product bucket count | **Pass.** At most $q$ unit residue pairs give $O(Lh)=O(Lu_0/q)$ atoms. |
| Zero and imprimitive aliases | **Pass.** $q=1$ and every divisor conductor remain in the exact decomposition. |
| Near-half aliases | **Pass.** They are primitive, have $q=u_0$, and remain in the high-$q$ complement when $u_0>Q_B$. |
| Both parity branches | **Pass.** All moduli $u,g,u_0,h,q$ remain odd; the even-even restrictions only delete atoms. |
| Literal selector and endpoints | **Pass.** They remain inside the inherited $\Lambda^\pm$ and are never smoothed or completed. |
| Both orientations | **Pass.** They are combined before modulus and share the exact energy buckets. |
| Exact complement | **Pass.** $q\leq Q_B$ and $q>Q_B$ partition every folded alias without overlap or omission. |
| K34--K35 promotion exclusion | **Pass.** Candidate, kernel, and reconciliation all mark them unproved and outside promotion. |
| Downstream scope | **Pass.** No complete K17a, residual scalar, parent, theorem, bridge, or exponent is promoted. |

No numerical experiment or external theorem was used.

# 6. Dependencies and exact artifacts used

This verification used exactly:

- proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/candidates/formalized_primitive_alias_conductor_reduction.md; and
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reviews/conductor_report_reconciliation.md.

No other report, candidate, review, control, synthesis, state file, source,
or web result was used. Only this assigned post-repair verification was
written.

# 7. Recommended state effect

Do not promote the kernel in its present byte-level form. Apply only the
one-token source repair (V177.9), then treat this verification as GREEN
without further mathematical review.

After that repair, promote exactly the primitive folding,
reduced-conductor normalization, $O(u_0L)$ and
$O(Lq\log(2q))$ ledgers, low-$q$ strict Fourier sector, physical
$u_0\leq Q_B$ corollary, exact high-$q$ complement, and scoped
positive-majorant/lift no-gos through (177.K33).

Keep (177.K34)--(177.K35), the high-conductor packet, complete K17a, the
complete residual scalar, every hard-TOP/BAL/UNBAL parent, M9--M2, both
M1 routes, endpoint uniformity, M9, both bridges, the quarter theorem,
and all exponent owners and numerical exponent values unchanged and open.

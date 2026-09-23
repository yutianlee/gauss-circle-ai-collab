# Round 180 blind post-unmask row-Gram seam review

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: blind post-unmask seam reviewer
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Final verdict: REPAIR
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The blind report is mathematically sound for the self-contained abstract
packet on which it was derived, but three of its conclusions require an
explicit post-unmask scope repair before they can be used in the literal
Round-180 coefficient system.

First, the blind exact-product counterexample is not a literal residual
counterexample. It uses one arbitrarily large product with arbitrarily many
odd divisor rows and freely chosen row signs. Literal products lie in one
\(M\asymp L^2\)-site interval with \(N\asymp L^2\); live near-square
incidences have \(d,m\asymp L\), total incidence
\(O_\eta(L^2X^\eta)\), divisor-fiber multiplicity
\(t_N\le\tau(N)\ll_\eta X^\eta\), and the fixed complete coefficient
\(\lambda_N(d)\). Consequently the exact cross-row product-collision sector
is

\[
\mathcal P_\nu
=\frac1M\sum_N\left\{(c_N^{\rm rem})^2
-\sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}
\ll_\varepsilon X^\varepsilon,
\tag{180.U1}
\]

uniformly in \(\nu\). It is a strict literal target-safe sector.

Second, the blind proposed twisted product-fiber Bessel relation is already
automatic at the required scale in the literal setting. Indeed its twisted
fiber sum is exactly \(c_N^{\rm rem}\), divisor Cauchy gives
\(\sum_N|c_N^{\rm rem}|^2\ll_\eta X^\eta\Lambda_2\), and the accepted
recombined estimate gives directly

\[
D_L:=\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{180.U2}
\]

Thus exact fibers are not the first missing literal relation. The remaining
open theorem is the one-outer-real-part, unequal-product form with
\(0<|dm-d'm'|<M\), every literal selector and endpoint field retained, and
uniformity in every near cell.

Third, the blind packet correctly found that its abstract hypotheses do not
control the full far-arc row sum. The literal estimate (180.U2) supplies
exactly the missing fact. Parseval and
\(F_M(\theta)\ll M/L\) on \(M\|\theta\|\ge\sqrt L\) give

\[
\frac12\sum_{\epsilon=0}^1
\int_{M\|\theta\|\ge\sqrt L}
F_M(\theta)|Z_\epsilon(\theta)|^2\,d\theta
\ll_\varepsilon \frac ML D_L
\ll_\varepsilon L^3X^\varepsilon.
\tag{180.U3}
\]

The phrase “real cosine dechirping — literal control fails” in the blind
report must therefore be read as follows: the real cosine array is admitted
by the abstract B180 packet and defeats every realness-only or
coefficient-uniform proof mechanism; it is not the literal residual
coefficient and gives no literal lower mass. The same qualification applies
to the blind exact-product and arbitrary-sign arrays.

I explicitly attest that the blind report was completed before unmasking,
using only protocol.md, its statement-only brief, and blind_statement.md.
No graph, campaign, strategy, kernel, sibling report, or conductor analysis
was read before that report was finalized. The present review is a later,
separate post-unmask comparison and does not retroactively alter that
provenance.

## 2. Exact statement and hypotheses

The literal post-unmask setting has

\[
J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
R_0=\lceil L\rceil,\qquad M\asymp L^2.
\tag{180.U4}
\]

The live products \(N=dm\) occupy one exact containing interval of
cardinality \(M\), with \(N\asymp L^2\). The near-square divisor support
forces \(d,m\asymp L\). The complete real coefficient
\(\lambda_N(d)\) retains the selected/no-pair field, squarefree and
coprimality projectors, both two-adic branches, near-square and Vaaler
profiles, floors, stars, hard values, endpoints, transitions, support
births and deaths, and full-line zero extension. On this support,

\[
\begin{aligned}
\#\Omega
&:=\#\{(d,m):d\ {\rm odd},\lambda_{dm}(d)\ne0\}
 \ll_\eta L^2X^\eta,\\
|\lambda_{dm}(d)|&\ll_\eta X^\eta,\\
\Lambda_2
&:=\sum_{d\ {\rm odd}}\sum_m|\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,\\
r_d&:=\#\{m:\lambda_{dm}(d)\ne0\}\ll L.
\end{aligned}
\tag{180.U5}
\]

For a fixed product, let

\[
t_N:=\#\{d:d\mid N,\ d\ {\rm odd},\lambda_N(d)\ne0\}.
\tag{180.U6}
\]

Then

\[
t_N\le\tau(N)\ll_\eta X^\eta.
\tag{180.U7}
\]

The recombined coefficient and its energy are

\[
c_N^{\rm rem}
=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
\chi_4(d)\lambda_N(d),
\qquad
D_L=\sum_N|c_N^{\rm rem}|^2
\ll_\varepsilon L^2X^\varepsilon.
\tag{180.U8}
\]

Define

\[
\begin{aligned}
\mathcal G_\nu&:=\frac12\sum_\epsilon\mathcal O_{\epsilon,\nu},\\
\mathcal D_\nu&:=\frac12\sum_\epsilon\sum_{d\ {\rm odd}}
\int_{I_\nu}|R_{\epsilon,d}(\theta)|^2\,d\theta,\\
\mathcal E_\nu&:=\frac12\sum_\epsilon
\int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta.
\end{aligned}
\tag{180.U9}
\]

The blind finite algebra remains exact:

\[
\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu,
\qquad
\mathcal D_\nu\ll_\varepsilon LX^\varepsilon,
\tag{180.U10}
\]

and

\[
K_\nu(h)
=\int_{I_\nu}e(h\theta)\,d\theta
=\begin{cases}
e(\nu h/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[5pt]
M^{-1},&h=0.
\end{cases}
\tag{180.U11}
\]

After separating the target-safe exact-product term (180.U1), the precise
open statement is

\[
\boxed{
\mathcal G_\nu-\mathcal P_\nu
\ll_\varepsilon LX^\varepsilon
\quad\text{uniformly for }
|\nu|\le\lceil\sqrt L\rceil.}
\tag{180.U12}
\]

Its left side is

\[
\begin{aligned}
2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
\sum_{\substack{m\equiv m'\pmod2\\dm\ne d'm'}}
&\chi_4(d)\chi_4(d')
\lambda_{dm}(d)\lambda_{d'm'}(d')\\
&\times
e\!\left(J(\sqrt{dm}-\sqrt{d'm'})
+\frac{\nu(dm-d'm')}{M}\right)
\frac{\sin(\pi(dm-d'm')/M)}
{\pi(dm-d'm')}.
\end{aligned}
\tag{180.U13}
\]

Both products lie in the same \(M\)-site interval, so every surviving
difference satisfies \(0<|dm-d'm'|<M\); parity makes it even.

## 3. Proof or derivation

### 3.1 Blind provenance and the common finite kernel

The statement-only derivation established (180.U10)--(180.U11) without
access to literal support. Its zero-difference value, wraparound treatment,
half-open endpoints, parity projector, and row-diagonal power agree exactly
with both sibling reports. Its universal Gram capacity

\[
-\mathcal D_\nu\le\mathcal G_\nu\le(r-1)\mathcal D_\nu
\tag{180.U14}
\]

also remains correct for arbitrary packet arrays. It gives a uniform
negative floor but no coefficient-uniform positive contraction. This
abstract conclusion is useful as a false-control boundary; it is not a
literal lower-mass or literal impossibility theorem.

### 3.2 Why the blind exact-product counterexample is neutralized

The blind construction fixed one odd product \(q\), activated every odd
divisor \(d\mid q\), put \(m=q/d\), freely chose
\(\lambda_{d,m}=a\chi_4(d)\), and let the divisor count grow independently
of \(L\). Four literal facts block that construction.

1. **Product and factor scale.** Literal \(N\) lies in the prescribed
   \(M\)-site interval with \(N\asymp L^2\), and only near-square factors
   \(d,m\asymp L\) are live. The blind construction used divisors over the
   entire range from \(1\) to \(q\) and allowed \(q\) arbitrarily far outside
   the literal scale.
2. **Total incidence.** The literal array has only
   \(O_\eta(L^2X^\eta)\) live incidences in total and \(O(L)\) cofactors per
   row. Arbitrarily many independently signed rows over one product are not
   licensed.
3. **Divisor multiplicity.** Each exact fiber has
   \(t_N\le\tau(N)\ll_\eta X^\eta\), rather than an unbounded multiplicity
   independent of the asymptotic parameters.
4. **Fixed recombined symbol.** The literal \(\lambda_N(d)\) is not a free
   sign array. Its recombination already obeys (180.U8).

For the blind fiber notation \(T_N\) and \(E_N\), one now has exactly

\[
T_N=c_N^{\rm rem},
\qquad
E_N=\sum_{\substack{d\mid N\\d\ {\rm odd}}}|\lambda_N(d)|^2.
\tag{180.U15}
\]

Fiberwise Cauchy and (180.U7) give

\[
|T_N|^2\le t_NE_N,
\qquad
\sum_N|T_N|^2\ll_\eta X^\eta\sum_NE_N.
\tag{180.U16}
\]

After epsilon rebudgeting, (180.U16) is stronger in \(L\)-power than the
blind proposed allowance
\(\sum_N|T_N|^2\ll L\sum_NE_N\). Independently, the accepted literal
bound (180.U8) supplies the required absolute recombined energy directly.
Thus the proposed fiber relation is automatic and cannot be the missing
Round-180 theorem.

At \(dm=d'm'=N\), the parity, square-root phase, and cell-centre phase all
cancel, while \(K_\nu(0)=M^{-1}\). Therefore

\[
\mathcal P_\nu
=\frac1M\sum_N\{(c_N^{\rm rem})^2-E_N\}.
\tag{180.U17}
\]

There are two compatible literal bounds:

\[
|\mathcal P_\nu|
\le\frac{D_L+\Lambda_2}{M}
\ll_\varepsilon X^\varepsilon,
\tag{180.U18}
\]

and, without using cancellation in \(c_N^{\rm rem}\),

\[
|\mathcal P_\nu|
\le\frac{\max_Nt_N}{M}\Lambda_2
\ll_\varepsilon X^\varepsilon.
\tag{180.U19}
\]

This proves that exact collisions are target-safe and isolates rather than
deletes them.

### 3.3 How the literal recombined energy repairs the far arc

Oddness of \(d\) gives
\((-1)^{\epsilon m}=(-1)^{\epsilon N}\) on \(N=dm\), so exact
recombination yields

\[
Z_\epsilon(\theta)
=\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
e(J\sqrt N+N\theta),
\qquad
\|Z_\epsilon\|_{L^2(\mathbb T)}^2=D_L.
\tag{180.U20}
\]

Let \(K=\lceil\sqrt L\rceil\). The half-open cells
\(I_{-K},\ldots,I_K\) form the exact circular interval

\[
U_K=\left[-\frac{K+1/2}{M},\frac{K+1/2}{M}\right)\pmod1,
\tag{180.U21}
\]

and its complement has \(M\|\theta\|\ge K+1/2>\sqrt L\). On the entire
far set the Fejer bound is \(F_M\ll M/L\). Equations
(180.U8) and (180.U20) then prove (180.U3). This is the exact fact absent
from the blind packet: \(\Lambda_2\) and per-row length alone do not control
the recombined global norm, whereas literal \(D_L\) does.

On each near cell,
\(F_M(\theta)\ll M/(1+\nu^2)\). If (180.U12) is assumed, (180.U1) and
(180.U10) give \(\mathcal E_\nu\ll LX^\varepsilon\); positivity then gives

\[
\sum_{|\nu|\le K}\int_{I_\nu}F_M(\theta)
\frac12\sum_\epsilon|Z_\epsilon(\theta)|^2\,d\theta
\ll_\varepsilon MLX^\varepsilon
\ll_\varepsilon L^3X^\varepsilon.
\tag{180.U22}
\]

Together, (180.U3) and (180.U22) repair the full near/far ledger. The
collective ordinary-zero restoration and once-only short correction are
then each \(O_\varepsilon(L^3X^\varepsilon)\), as the sibling audits
verify; this establishes only the stated connector from (180.U12) to K26.

### 3.4 The replacement for the blind fiber relation

For \(0<h<M\), \(2\mid h\), define with full-line zero extension

\[
\begin{aligned}
C_h^{\rm off}
:=\sum_N e\!\left(J(\sqrt{N+h}-\sqrt N)\right)
\sum_{\substack{d\mid N+h,\ d'\mid N\\
d,d'\ {\rm odd},\ d\ne d'}}
 \chi_4(d)\chi_4(d')
 \lambda_{N+h}(d)\lambda_N(d').
\end{aligned}
\tag{180.U23}
\]

Then the remaining open form is exactly

\[
\mathcal G_\nu-\mathcal P_\nu
=2\Re\sum_{\substack{0<h<M\\2\mid h}}K_\nu(h)C_h^{\rm off}.
\tag{180.U24}
\]

The needed replacement is not a positive fiber norm and not a collection
of bounds for \(|C_h^{\rm off}|\). It is a uniform signed estimate for
(180.U24), or equivalently the recombined local scalar theorem
\(\mathcal E_\nu\ll_\varepsilon LX^\varepsilon\), with all of the
following stable simultaneously:

- the selected/no-pair Boolean field and squarefree/coprimality masks;
- both two-adic and parity branches;
- Vaaler and near-square profiles, floors, stars, and hard point values;
- support births, deaths, transitions, exact endpoints, and zero extension;
- \(\chi_4(d)\chi_4(d')\), the square-root phase, the cell-centre phase,
  and the sinc kernel;
- the single outer real part, with no shiftwise or rowwise modulus; and
- uniformity through \(|\nu|=\lceil\sqrt L\rceil\).

This selector-, phase-, and endpoint-stable unequal-product relation is the
first missing literal fact. Grouping by \(h\) and then taking absolute
values self-returns to the known shifted-correlation capacity and is not a
proof.

### 3.5 Scope repair for the blind controls

The blind report's real cosine array is genuinely real and satisfies the
abstract packet's energy and row-length bounds, so it correctly disproves a
realness-only inference. The discovery and hostile reports independently
produce larger \(L^2\)-incidence versions attaining local capacity \(L^2\)
and endpoint capacity \(L^4\). None of these arrays equals the literal
\(\lambda_N(d)\), and none proves positive literal mass.

Accordingly, the heading “real cosine dechirping — literal control fails”
must not be cited as saying that a literal coefficient theorem fails. Its
repaired reading is:

\[
\boxed{\text{Abstract real-coefficient control defeats a
coefficient-uniform or realness-only proof mechanism.}}
\tag{180.U25}
\]

The blind statement “no target-safe strict sector follows” also has only
abstract-packet scope. Post-unmask, the exact-product sector (180.U1) is a
strict literal target-safe sector, while its unequal-product complement
(180.U13) remains exact and open.

## 4. First doubtful or unproved step

The first doubtful step after unmasking is no longer product-fiber
anticorrelation. Equations (180.U16)--(180.U19) close that seam.

The first unproved step is exactly the uniform bound (180.U12), equivalently
(180.U24), for the complete literal unequal-product correlation. No accepted
fact supplies its missing factor \(L\). In particular:

1. the selector is Boolean, not an automatic oscillatory sign;
2. selected opposite-character supports can be disjoint rather than
   pointwise cancelling;
3. an allowed no-pair all-\(1\bmod4\) shadow has constant character;
4. the complete zero-extended profile has variation \(O(1)\), not
   \(O(L^{-1})\);
5. fixed-shift absolute values lose the one outer real part; and
6. positive row or cell closure has local capacity \(L^2X^\varepsilon\),
   one factor \(L\) above the target.

The post-unmask evidence neither proves nor disproves (180.U12). It proves
only that exact collisions and far arcs are paid, and that any continuation
must use a new complete literal selector/phase/endpoint relation before
positivity.

## 5. Required control test and outcome

| Control | Post-unmask outcome |
|---|---|
| blind provenance | **PASS.** The blind report predates all newly authorized graph, strategy, kernel, and sibling access; its isolated provenance is explicitly preserved. |
| exact kernel, zero value, wraparound, half-open cells | **GREEN.** The blind formula agrees exactly with both sibling derivations, including \(K_\nu(0)=1/M\). |
| parity and physical row diagonal | **GREEN.** The parity projector and \(L^3/M\asymp L\) diagonal power agree with the literal ledger. |
| blind exact-product counterexample | **REPAIR SCOPE.** It is decisive for B180's abstract coefficient class but violates literal product/factor scale, live incidence, fiber multiplicity, fixed-symbol, and recombined-energy facts. It is not literal mass. |
| literal exact-product sector | **GREEN.** Equations (180.U17)--(180.U19) give \(O_\varepsilon(X^\varepsilon)\), uniformly in every cell. |
| blind fiber Bessel proposal | **REPLACE.** Divisor multiplicity makes it automatic after epsilon rebudgeting, and \(D_L\) gives the accepted recombined bound. The open relation is (180.U24). |
| blind far-arc limitation | **REPAIR BY NEW HYPOTHESIS.** It is correct for the abstract packet; literal Parseval plus \(D_L\) yields the full \(L^3X^\varepsilon\) far bound. |
| complex dechirped control | **GREEN AS FALSE CONTROL.** It excludes coefficient-magnitude and positive closures only; it is complex and nonliteral. |
| real cosine dechirped control | **REPAIR LABEL.** It is an abstract admitted real array that excludes realness-only closure, not a literal residual array or lower bound. |
| arbitrary real signs and constant character | **GREEN AS FALSE CONTROLS.** They show that a proof insensitive to the fixed selector and actual coefficient cannot work; they do not occur as an asserted literal family. |
| all-\(1\bmod4\) no-pair warning | **GREEN WITH QUARANTINE.** It rules out formal rowwise character mean zero but gives neither density nor literal lower mass. |
| one row and one site | **GREEN.** Their off-row forms vanish, confirming that capacity is not a universal lower bound. The blind one-site-per-row exact-collision construction does not survive the literal scale, multiplicity, and fixed-symbol ledger; this says nothing about the unequal-product literal complement. |
| unequal products | **OPEN.** Every even \(0<h<M\) term remains with its sinc, chirp, character, selector, hard boundary, and one outer real part. |
| near/far and endpoint powers | **GREEN AFTER REPAIR.** Diagonal \(L\), abstract positive capacity \(L^2\), near target \(L\), near/far endpoint target \(L^3\), and coefficient-uniform endpoint capacity \(L^4\) are reconciled. |
| downstream and exponent scope | **GREEN.** No result is propagated beyond the conditional K26 connector, and no exponent conclusion is made. |

No numerical test was used.

## 6. Dependencies and exact artifacts used

The pre-unmask blind derivation used only:

- protocol.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/briefs/blind_row_gram_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/blind_statement.md.

Only after that report was complete, this post-unmask review newly read:

- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/literal_near_peak_row_gram_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/reports/fejer_cell_owner_capacity_audit.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md.

The earlier blind report is the statement-only artifact being reviewed; it
was not edited. No other graph, strategy, prior-round artifact, sibling,
source, synthesis, control, or conductor analysis was used. No external
theorem or computation is a dependency. This review edits no blind report,
sibling report, shared state, proof draft, validation matrix, kernel,
strategy, synthesis, or successor-round artifact.

## 7. Recommended state effect

**Final verdict: REPAIR.**

Retain as GREEN the blind exact kernel, zero-difference value, wraparound,
parity projector, sharp row diagonal, near-cell Fejer summation, universal
Gram-capacity boundary, and abstract false controls. Repair their literal
interpretation as follows:

1. reject the blind exact-product construction as a literal counterexample;
2. promote the literal exact-product collision sector only as the
   target-safe estimate (180.U1);
3. replace the blind fiber-Bessel “first missing relation” by the complete
   selector-, phase-, parity-, cell-, and endpoint-stable unequal-product
   theorem (180.U12)/(180.U24);
4. use recombined \(D_L\), not the abstract incidence ledger alone, for the
   far-arc bound (180.U3); and
5. quarantine every dechirped, arbitrary-sign, and constant-character array
   as a coefficient-uniform false control, never as literal lower mass.

The route-scoped row-Gram capacity/self-return obstruction is consistent
with this repaired reading: generic positivity, realness, character
modulation, row length, and energy do not supply the missing factor \(L\),
but the complete literal theorem remains open. Keep K26, the residual
scalar, the hard-TOP parents, BAL, UNBAL, M9--M2, both M1 routes, GAR,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent owner unchanged. Do not start a successor round from this review.

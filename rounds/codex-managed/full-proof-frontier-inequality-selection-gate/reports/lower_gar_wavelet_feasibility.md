# Round 127 lower-GAR wavelet feasibility: centered square-function audit

Campaign: `full-proof-frontier-inequality-selection-gate`

Task: `lower_gar_wavelet_feasibility`

Role: discovery

Access mode: selected context

Starting graph SHA-256: `fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`
Proof status: candidate evidence only; no graph edit is licensed.

## 1. Result: centered square-function implication and selection no-go

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,\qquad K_\delta=yX^\delta,
 \qquad A_0=\lceil\log _2R\rceil,
\]

where \(0<\delta<1/8\) is fixed.  Let \(W\),
\(\mathscr V_\delta\), and the oriented interval operator \(\mathcal I_k\)
be exactly those of (122.J17)--(122.J19), and put

\[
 S(k)=\mathcal I_k\mathscr V_\delta,
 \qquad c_y=\sum_{d\leq y}{\chi _4(d)\over d},
 \qquad S^\circ(k)=S(k)-kc_y.
\tag{127.1}
\]

The audit gives three conclusions.

1. **The uncentered proposed energy is false for the actual
   coefficient.**  There are dyadic \(K\asymp y\), lying inside the
   retained range for all sufficiently large \(X\), for which

   \[
   \sum_{K<k\leq2K}|S(k)|^2\gg y^3.
   \tag{127.2}
   \]

   Thus
   \(\sum_{K<|k|\leq2K}|S(k)|^2\ll_\varepsilon R^2KX^\varepsilon\)
   is false: at \(K\asymp y=R^2\), its right side is only
   \(y^2X^\varepsilon\).  The coherent term \(kc_y\), which the exact
   wavelet kills through its first moment, cannot be put inside a positive
   square function.

2. **A corrected centered square function would be sufficient.**  For
   the dyadic blocks

   \[
   \mathcal K(K)=
   \{k\in\mathbb Z:K<|k|\leq \min(2K,K_\delta)\},
   \qquad K=2^jR<K_\delta,
   \tag{127.3}
   \]

   the theorem-shaped estimate

   \[
   \boxed{
   \sum_{k\in\mathcal K(K)}|S^\circ(k)|^2
   \ll_{\varepsilon,\delta} K(R^2+K)X^\varepsilon
   }
   \tag{SF-GAR}
   \]

   implies the complete \(O_{\varepsilon,\delta}(RX^\varepsilon)\)
   bound for (122.J19).  On the critical range \(R<K\leq y\), this is
   precisely \(R^2KX^\varepsilon\).  The \(+K^2\) relaxation beyond
   \(y\) is compatible with the literal diagonal and is harmless because
   \(W(k)\) has arbitrary fixed power decay once \(|k|/y\) grows.

3. **This does not pass the Round-127 selection gate.**  Cauchy in \(k\)
   replaces the signed cross-\(k\) wavelet by a positive norm of each
   cumulative endpoint.  It is therefore a stronger, separated
   Fourier-index norm, even though every valuation, residue, and
   full/complement label remains joint inside each \(S^\circ(k)\).
   Moreover the exact additive-character expansion below is an ambient
   Fourier/Farey canonicalization.  The identity supplies no gain, and
   the coefficient-blind capacity at \(K\asymp y\) is still \(y^3\)
   against the desired \(y^2\).  Proving (SF-GAR) would require the entire
   missing energy factor \(y=R^2\), equivalently the entire missing linear
   factor \(R\).  Thus the proposed mechanism neither proves a strict new
   subrange beyond the already deleted \(|k|\leq R\), nor gives an
   eligible next-round interface under the frozen exclusion of separated
   norms and ambient spectra.

This is a rigorous no-go for the proposed uncentered/square-function
selection mechanism, not a no-go for cancellation in the actual scalar
wavelet.

## 2. Exact statement, hypotheses, and three-frontier capacity ledger

### 2.1 Literal survivor and orientations

For \(m=2^an>0\) with \(n\) odd, write

\[
 \mathfrak a(n)=\sum_{d\mid n}\chi _4(d)={r_2(m)\over4},
 \qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi _4(q).
\]

The exact surviving increment is

\[
 \mathscr V_\delta(2^an)=
 \begin{cases}
  \frac12\mathfrak a(n),&a=0,\ \chi _4(n)=1,\\
  T_{n/y}(n),&a=0,\ \chi _4(n)=-1,\\
  \mathfrak a(n)-\chi _4(n)T_{n/y}(n),&1\leq a<A_0,\\
  0,&a\geq A_0.
 \end{cases}
\tag{127.4}
\]

The threshold in \(T_{n/y}\) is strict.  The hard cutoff in the original
coefficient is \(d\leq y\).  These conventions include the square fixed
point, \(n=y^2\), and do not replace the even-branch sign by
\(\chi _4(2^an)=0\).

For every function \(f\) on the positive integers, the oriented interval
is

\[
 \mathcal I_kf=
 \begin{cases}
  \displaystyle\sum_{j=1}^{k}f(N+j),&k>0,\\[4pt]
  0,&k=0,\\[4pt]
  \displaystyle-\sum_{k<j\leq0}f(N+j),&k<0.
 \end{cases}
\tag{127.5}
\]

Consequently \(\mathcal I_k1=k\) for both signs, which is why (127.1)
is the unique literal centering.  Since
\(K_\delta=X^{1/2+\delta}+O(1)=o(N)\), every traversed integer is positive
for sufficiently large \(X\).  No symmetry such as
\(W(-k)=W(k)\) is assumed: the Round-122 wavelet is one-sided, and the two
orientations are retained in the same energy only after their definitions
are fixed separately.

The accepted reduction is

\[
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\leq K_\delta}W(k)S(k)
 +O_{\varepsilon,\delta}(RX^\varepsilon).
\tag{127.6}
\]

The absolute scalar capacity of the displayed survivor is \(y=R^2\),
whereas its target is \(R\).  The literal deficit is therefore one full
factor \(R=X^{1/4}\).

### 2.2 The three frontiers

| Frontier | Literal target | Current capacity / strongest proved level | Missing power at the live target | Exact payoff of full success |
|---|---:|---:|---:|---|
| Hard TOP nonsquare actual direction | \(E_{\rm ns}=\|A_L^{\rm ns}\chi _4\|_2^2\ll L^2X^\varepsilon\) | support/Bessel capacity \(L^3\); the removed \(hm=\square\) entry sector is \(O(L^{3/2}X^\varepsilon)\) only through the norm triangle | \(L\) in energy, or \(L^{1/2}\) in norm | closes hard TOP only; BAL and UNBAL still block `M9-M2` |
| Round-122 lower GAR wavelet | (127.6) \(\ll RX^\varepsilon\) | scalar absolute capacity \(y=R^2\); centered energy capacity \(y^2K\) at a \(K\)-block | \(R\) linearly; at \(K=y\), \(y=R^2\) in energy | closes the lower GAR analytic parent and hence the alternative total-active-M1 side; it does **not** prove either direct blockwise M1 parent, blockwise `M9-M1`, `M9`, or `M9-M2` |
| Graded \(W=Y^{7/16}\) determinant | signed nonzero determinant \(\ll Y^{1/2+\varepsilon}\) | Farey capacity \(Y^{43/48}\); complete proved bound \(Y^{37/48}\); bounded-lift top shell \(Y^{35/48}\) | \(Y^{13/48}\) after the complete bound; \(Y^{11/48}\) on the top shell (baseline gap \(Y^{19/48}\)) | full target gives the internal exponent \(5/16\), but proves neither `M9` nor the quarter theorem |

The lower route has the strongest M1 graph payoff, but `M9-M2` is
mandatory on both final bridges.  No entry in this table changes status
merely because an inequality is proposed.

## 3. Proof and derivation

### 3.1 The uncentered square function is actually false

The exact Round-122 overlap identity is

\[
 S(k)=D_N(k)+kc_y-widetilde D_{\geq A_0}(k)-\frac12E(k),
\tag{127.7}
\]

where \(\widetilde D_{\geq A_0}\) is the cumulative high-two-adic
projection and \(E\) is the odd positive-character central correction.
For every \(k\), the fractional-part formula gives

\[
 |D_N(k)|\leq y.
\tag{127.8}
\]

The alternating harmonic partial sum satisfies

\[
 c_y=1-\frac13+\frac15-\frac17+\cdots\quad(d\leq y),
 \qquad c_y\geq\frac23.
\tag{127.9}
\]

Indeed the even partial sums increase from \(2/3\), and odd partial sums
are larger.  The divisor bound and the spacing of multiples of
\(2^{A_0}\) give, for every fixed \(\eta>0\),

\[
 |\widetilde D_{\geq A_0}(k)|
 \ll_\eta \left(1+{|k|\over2^{A_0}}\right)X^\eta.
\tag{127.10}
\]

The injective near-square factor-pair count used in Round 122 gives

\[
 |E(k)|\leq
 \sum_{|j|\leq K_\delta}|\Gamma(N+j)|
 \ll_\delta(1+X^\delta)^2.
\tag{127.11}
\]

Choose a dyadic \(K\) with \(4y\leq K<8y\).  For sufficiently large
\(X\), \(2K\leq K_\delta\).  Uniformly for \(K<k\leq2K\), equations
(127.7)--(127.11), with \(\eta<1/4\) and \(\delta<1/8\), give

\[
 S(k)\geq {2k\over3}-y-o(y)\gg y.
\tag{127.12}
\]

There are \(\asymp y\) such \(k\), so (127.2) follows.  Taking, for
example, the claimed \(X^\varepsilon\) with any \(\varepsilon<1/2\)
shows a fixed-power contradiction to the uncentered bound.  This uses
the actual \(\mathscr V_\delta\), not an adversarial replacement.

### 3.2 The centering is target-equivalent in the scalar wavelet

Round 122 proves the exact full first moment

\[
 \sum_{k\in\mathbb Z}kW(k)=0.
\tag{127.13}
\]

Its wavelet envelope gives, for every fixed \(A\geq1\),

\[
 |W(k)|\ll_A{1\over R+|k|}
 \left(1+{|k|\over y}\right)^{-A}.
\tag{127.14}
\]

The omitted central contribution to (127.13) is
\(O(\sum_{|k|\leq R}|k|/(R+|k|))=O(R)\), and the omitted far contribution
is \(O_{A,\delta}(RX^{-A})\) after taking enough derivatives, exactly as
in the accepted localized centering seam.  Therefore

\[
 \sum_{R<|k|\leq K_\delta}W(k)S(k)
 =\sum_{R<|k|\leq K_\delta}W(k)S^\circ(k)
 +O_{\delta}(R).
\tag{127.15}
\]

This is why the drift destroys the positive uncentered norm but not the
original signed wavelet.

### 3.3 (SF-GAR) would imply the target

For every block (127.3), (127.14) gives

\[
 \sum_{k\in\mathcal K(K)}|W(k)|^2
 \ll_A K^{-1}\left(1+{K\over y}\right)^{-2A}.
\tag{127.16}
\]

Cauchy and (SF-GAR) would then give

\[
 \begin{aligned}
 \left|\sum_{k\in\mathcal K(K)}W(k)S^\circ(k)\right|
 &\ll_{A,\varepsilon,\delta}
 \sqrt{R^2+K}
 \left(1+{K\over y}\right)^{-A}X^{\varepsilon/2}\\
 &\ll R\left(1+{K\over y}\right)^{1/2-A}X^{\varepsilon/2}.
 \end{aligned}
\tag{127.17}
\]

There are \(O(\log X)\) blocks with \(R\leq K\leq y\), and the blocks
above \(y\) form a convergent geometric tail when \(A>1\).  Absorbing
the logarithm into \(X^{\varepsilon/2}\), and then using (127.15), proves
the desired \(RX^\varepsilon\) estimate.  The first and last partial
dyadic blocks obey the same calculation; no endpoint is silently
discarded.

### 3.4 Exact energy capacity

For the positive orientation put

\[
 b_j=\mathscr V_\delta(N+j)-c_y,
 \qquad S^\circ(k)=\sum_{j=1}^k b_j.
\]

Then

\[
 \sum_{K<k\leq2K}|S^\circ(k)|^2
 =\sum_{1\leq j,j'\leq2K}b_j\overline{b_{j'}}
 M_K(j,j'),
\tag{127.18}
\]

where

\[
 M_K(j,j')=
 \#\{k\in\mathbb Z:K<k\leq2K,\ k\geq\max(j,j')\}.
\tag{127.19}
\]

The negative orientation has the same triangular kernel after replacing
\(b_j\) by the correctly oriented left increments.  The divisor bound
gives a coefficient-blind cumulative capacity \(K^3X^\varepsilon\) for
\(K\leq y\), while (127.8) gives the global discrepancy capacity
\(y^2KX^\varepsilon\).  At the critical \(K=y\), both are \(y^3\).
The proposed energy is \(yK=y^2\): it requires a full factor \(y=R^2\)
of off-diagonal energy cancellation.  After the square root and
(127.16), that is exactly the missing scalar factor \(R\).  Thus Cauchy
has not created any saving; it has restated the whole deficit in a
stronger positive form.

### 3.5 Exact reduced-Farey identity and determinant self-return

The broader centered discrepancy does have an exact reduced-Farey
identity, but it does not alter the preceding capacity.  Additive
orthogonality gives

\[
 {\bf1}_{d\mid m}={1\over d}\sum_{r\bmod d}e(rm/d).
\]

Writing \(r/d=a/b\) in lowest terms, so \(d=bg\), and using complete
multiplicativity of \(\chi _4\), gives

\[
 A_y(m)=
 \sum_{\substack{b\leq y\\b\ {m odd}}}
 {\chi _4(b)L_{y/b}(1,\chi _4)\over b}
 \sum_{a\bmod b}^{*}e(am/b),
 \qquad
 L_T(1,\chi _4)=\sum_{g\leq T}{\chi _4(g)\over g}.
\tag{127.20}
\]

The \(b=1\) term is exactly \(c_y\).  Hence it must be omitted, rather
than retained, in a formula for \(D_N\).  Define

\[
 G_k(\alpha)=
 \begin{cases}
  \sum_{j=1}^ke(j\alpha),&k>0,\\
  0,&k=0,\\
  -\sum_{k<j\leq0}e(j\alpha),&k<0.
 \end{cases}
\]

Then the exact all-sign identity is

\[
 \boxed{
 D_N(k)=
 \sum_{\substack{2\leq b\leq y\\b\ {m odd}}}
 \lambda_b\sum_{a\bmod b}^{*}e(aN/b)G_k(a/b),
 \qquad
 \lambda_b={\chi _4(b)L_{y/b}(1,\chi _4)\over b}.}
\tag{127.21}
\]

Squaring (127.21) over \(\mathcal K(K)\) yields the literal correlation

\[
 \sum_{b,b'}\lambda_b\overline{\lambda_{b'}}
 \sum_{a\bmod b}^{*}\sum_{a'\bmod b'}^{*}
 e\!\left(N{ab'-a'b\over bb'}\right)
 \mathcal H_K\!\left({a\over b},{a'\over b'}\right),
\tag{127.22}
\]

where

\[
 \mathcal H_K(\alpha,\beta)=
 \sum_{k\in\mathcal K(K)}G_k(\alpha)\overline{G_k(\beta)}.
\]

Thus the nonzero off-diagonal is indeed a prescribed-centre
reduced-Farey determinant correlation with determinant
\(ab'-a'b\).  Because both fractions are reduced, determinant zero means
the literal diagonal \((a,b)=(a',b')\).

The exact diagonal already obeys

\[
 \mathcal E_{\rm diag}(K)\ll K(y+K)X^\varepsilon.
\tag{127.23}
\]

To see this without an external theorem, use
\(|L_T(1,\chi _4)|\leq1\), so \(|\lambda_b|\leq1/b\).  If \(b\leq K\),
periodicity and additive orthogonality give

\[
 \sum_{k=1}^{b}\sum_{a=1}^{b-1}|G_k(a/b)|^2
 =\sum_{k=1}^{b}(bk-k^2)\ll b^3,
\]

and hence a contribution \(O(K)\) after multiplication by
\(|\lambda_b|^2\).  If \(b>2K\), the same orthogonality on the incomplete
range gives \(O(bK^2)\), hence \(O(K^2/b)\) after the coefficient; the
range \(K<b\leq2K\) costs \(O(K^2)\).  Summing in \(b\), and using
\((K/y)\log(y/K)\ll1\), proves (127.23).  The two orientations only
change the constant.

Therefore all of the missing factor lies in the actual signed nonzero
determinants of (127.22).  But (127.20)--(127.22) are an exact ambient
Fourier canonicalization, and taking the positive \(k\)-energy is the
separated norm already identified above.  A coefficient-blind treatment
retains \(y^3\) capacity at \(K=y\).  The determinant language neither
contracts the survivor nor bypasses the Round-122 Fourier/self-return
barrier.  A genuinely new bound for the full off-diagonal of (127.22)
would be substantive mathematics, but selecting it as stated would
contradict the frozen Round-127 exclusions.

## 4. First doubtful or unproved step

The first unproved analytic step is exactly

\[
 \mathcal E_{\rm off}(K)
 :=(127.22)-\mathcal E_{\rm diag}(K)
 \ll_{\varepsilon,\delta}K(R^2+K)X^\varepsilon
\tag{127.24}
\]

for the actual coefficients, uniformly through the critical
\(K\asymp y\).  At that scale it asks for \(O(y^2X^\varepsilon)\) against
the \(O(y^3X^\varepsilon)\) coefficient-blind capacity.  No permitted
artifact proves a determinant-spacing, large-sieve, divisor-correlation,
or inverse theorem with this factor \(y\) gain.

There is also an earlier selection seam: (127.24) is reached only after
an ambient additive Fourier expansion and a positive norm in \(k\).
Under the active campaign's literal eligibility rule, that is already a
fatal mechanism seam, irrespective of whether (127.24) is an interesting
standalone conjecture.  Calling the transform itself the gain would be
false; calling Cauchy the gain would be false; and separating the
two-adic, residue, or full/complement branches before (127.24) would
violate the exact survivor interface.

## 5. Control tests and outcomes

| Required control | Test | Outcome |
|---|---|---|
| `literal_three_frontier_statements` | Reproduced hard TOP, lower GAR, and graded determinant targets and scales in Section 2.2. | **Pass.** |
| `capacity_and_missing_power_table` | Compared one scale in each row; at lower critical \(K=y\), capacity \(y^3\), proposed energy \(y^2\), scalar capacity \(y=R^2\), scalar target \(R\). | **Pass.** No hidden square/linear conversion. |
| `noninvertible_mechanism_test` | Cauchy is noninvertible, but it is a separated positive norm in \(k\), not a joint signed cross-\(k\) inequality. | **Fail for selection.** It is stronger than the literal scalar and explicitly excluded by the active gate. |
| `prior_no_go_bypass` | No complement, full-circle insertion, second complement, Abel inversion, or local mod-four pairing was used as a claimed saving.  The optional Farey identity is, however, another ambient Fourier canonicalization. | **Fail for the Farey/square-function mechanism.** The identity returns the same capacity. |
| `actual_vs_adversarial_coefficients` | The uncentered energy fails for the actual \(\mathscr V_\delta\) by (127.12).  For the centered form, aligned increments \(b_j\equiv1\) give energy \(\asymp K^3\), so no coefficient-uniform proof is possible. | **Pass as a falsifier.** Any valid centered estimate must use the exact arithmetic coefficients; random-sign credit is inadmissible. |
| `endpoint_floor_star_and_support_scope` | Used \(y=\lfloor\sqrt X\rfloor\), \(N=\lfloor X\rfloor\), \(A_0=\lceil\log_2R\rceil\), strict \(q<n/y\), inclusive \(d\leq y\), both oriented signs, the square tie, and the final partial dyadic block.  All traversed integers are positive. | **Pass.** No terminal-index valuation substitution or wavelet parity was made. |
| `dependency_and_payoff_scope` | Traced success only to lower GAR and the alternative total-active-M1 bridge. | **Pass.** It does not imply either direct blockwise M1 parent, blockwise `M9-M1`, `M9`, `M9-M2`, or a new exponent by itself. |
| `finite_stop_rule` | Stop immediately if the argument uses the uncentered norm, retains the \(b=1\) Farey term in \(D_N\), takes absolute values in determinant/fraction/valuation/residue labels, or returns the \(y^3\) capacity at \(K\asymp y\).  Reconsider only after an eligible scalar signed inequality, or an explicit relaxation of the no-separated-norm gate plus a proved fixed-power off-diagonal saving. | **Pass.** The present route stops now. |
| `no_proof_status_from_strategy_only` | Distinguished the proved false-control/implication algebra from the unproved (127.24). | **Pass.** No analytic parent or theorem is promoted. |

Additional false controls:

- **Uncentered drift:** fails for the actual coefficient by a factor
  \(yX^{-\varepsilon}\).
- **Farey \(b=1\) term:** including it makes (127.21) a formula for
  \(\mathcal I_kA_y\), not for \(D_N(k)\).
- **Zero determinant:** it is the literal reduced-fraction diagonal and is
  already target-capacity; deleting it does not estimate the nonzero
  determinants.
- **Full-circle or complementary separation:** still reconstructs the
  Round-122 self-return and is not invoked in (127.24).
- **High two-adic/odd-central corrections:** they remain the already proved
  scalar safe packages.  Forcing separate positive square norms on them is
  neither needed nor a new gain.

No numerical or experimental control was used, in accordance with the
zero-percent numerical allocation.

## 6. Dependencies and exact artifacts used

Only the task brief and its permitted context were used:

1. `protocol.md` — proof-state authority, promotion rules, and signed vs.
   unsigned control requirements.
2. `state/proof_obligations.yml` — exact lower-GAR owner, Round-122
   survivor, bridge implications, the hard-TOP capacity, and the graded
   determinant capacities/payoffs.
3. `state/active_campaign.yml` — frozen three-frontier question,
   ineligibility list, required controls, and graph hash.
4. `strategy/conductor_0821_full_proof_strategy.md` — Round-119 through
   Round-126 capacity and continuation ledger.
5. `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`
   — exact lower flattening, discrepancy normalization, wavelet moment,
   and GAR normalization.
6. `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`
   — (122.S1)--(122.S10), exact survivor, and complementary self-return.
7. `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/reviews/conductor_round122_complement_adjudication.md`
   — repaired orientations, centering overlap (122.J18), floors, strict
   thresholds, high-valuation and central-correction bounds.

No external source, web result, computation, sibling Round-127 report, or
unlisted historical artifact was used.

## 7. Recommended state effect

**Recommendation: no change; reject this mechanism as the selected next
analytic interface.**

Retain the proved algebraic observations only as candidate evidence:

- the uncentered square-function statement is false for the actual
  survivor;
- centering by \(kc_y\) is mandatory and target-equivalent only because
  the exact scalar wavelet has zero first moment;
- (SF-GAR) (or the exact discrepancy version (127.24)) would close the
  lower wavelet if proved;
- its critical requirement is the whole missing factor \(y=R^2\) in
  energy, equivalently \(R\) in the scalar;
- its reduced-Farey expansion is a literal determinant correlation, but
  this is an ambient canonicalization followed by a stronger separated
  norm and therefore does not pass the frozen novelty gate.

Keep `M9-M1-global-lower-radial-signed-estimate`, GAR, both direct
blockwise M1 parents, `M9-M1`, all three M2 parents, `M9-M2`, `M9`, and
the quarter theorem open.  A lawful reopening of lower GAR still requires
a genuinely signed inequality that keeps the Fourier indices joint with
the low-two-adic, residue, and full/complement labels until the saving is
obtained.  Another complement, full-circle insertion, Abel/Fourier
reconstruction, ambient Farey spectrum, or positive separated norm should
stop immediately.

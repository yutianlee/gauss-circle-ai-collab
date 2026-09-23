# Round 178 full-graph frontier reconstruction

## 1. Result

On authoritative graph
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7,
the quarter theorem still has exactly two lawful proof trees. They form a
logical OR. The standard tree requires both direct blockwise M1 parents, all
three M2 parents, literal endpoint uniformity, M9, and the standard
conditional bridge. The alternative tree replaces only the direct M1
conjunction by complete GAR and its proved total-active-M1 equivalence. It
still requires every M2 parent and the separate alternative bridge. GAR has
no implication to blockwise M9-M1 or M9.

Rounds 175--177 close no analytic parent, but they change the exact residual
frontier:

1. Round 175 proves that the proposed K26 whole-scale variable collapses
   exactly to $Q_M^*-Q_{R_0}^*$, with $Q_{R_0}^*$ target-safe. Thus K26 is
   target-equivalent to the still-open literal theorem
   $Q_M^*\ll L^3X^\varepsilon$, while coefficient-independent capacity is
   $L^4X^\varepsilon$.
2. Round 176 proves the exact two-orientation K17a cross-gcd fibre and every
   fixed-proportion sector $\kappa_*\geq\delta L$.
3. Round 177 folds the remaining anchor first to
   $u_0=u/(u,n)$ and then to exact additive conductor
   $q=u_0/(\ell,u_0)$. It proves every
   $q\leq(\log(2X))^B$ alias packet. The exact complement is the signed
   high-conductor block (177.K34). One reciprocal square root, exact
   rank-one $TT^*$, positive Parseval, lift-erasing completion, and anchor
   antisymmetry are insufficient at their accepted scopes.

The unique recommended Round-179 objective is the complete
high-reduced-conductor K17a signed block (177.K34), not the stronger
aliaswise estimate (177.K35). Relative to the immediate Round-177 frontier,
this is strategy_frontier_retained. K17a is now the smallest literal
owner-complete residual theorem with an unused, precisely priced,
sign-sensitive conductor interface. K26 has equal downstream scope, but its
proposed scale resource has been exhausted exactly.

This is a strategy conclusion, not an analytic estimate. Every proof status
is retained. The exponent ledger remains

$$
\theta_{\rm internal}=\frac13,\qquad
\theta_{\rm external}
=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots,\qquad
\theta_{\rm target}=\frac14.
\tag{178.1}
$$

## 2. Exact statement and hypotheses

### 2.1 The two lawful quarter-proof trees

Put

$$
\mathcal I=\{\mathrm{H1\!-\!H3},\mathrm{H4},\mathrm{R5\!-\!Full}\},
$$

whose members are accepted. Let Phys1 and Phys2 denote the proved physical
one-count assemblies.

The standard tree is

$$
\begin{aligned}
&\mathcal I,\\
&\left[
 \underbrace{\mathrm{M1\!-\!TOP}_{\rm direct}}_{\rm open}
 \wedge
 \underbrace{\mathrm{M1\!-\!SMOOTH}_{\rm direct}}_{\rm open}
 \right]
 \xRightarrow{\mathrm{Phys1}}
 \underbrace{\mathrm{M9\!-\!M1}}_{\rm open},\\
&\left[
 \underbrace{\mathrm{TOP}_{\rm M2}}_{\rm open}
 \wedge
 \underbrace{(\mathrm{BAL}_{\rm crit}\wedge
              \mathrm{BAL}_{\rm rest})}_{\rm both\ open}
 \wedge
 \underbrace{\mathrm{UNBAL}}_{\rm open}
 \right]
 \xRightarrow{\mathrm{Phys2}}
 \underbrace{\mathrm{M9\!-\!M2}}_{\rm open},\\
&\mathrm{M9\!-\!M1}\wedge\mathrm{M9\!-\!M2}
 \wedge\underbrace{\mathrm{Endpoint}_{\rm std}}_{\rm open}
 \Longrightarrow \underbrace{\mathrm{M9}}_{\rm open}
 \xRightarrow{\mathrm{Conditional\mbox{-}bridge}}
 \underbrace{\mathrm{GC\mbox{-}target}}_{\rm open}.
\end{aligned}
\tag{178.Tstd}
$$

Here:

- M1-TOP-direct is M9-M1-top-endpoint-signed-cone.
- M1-SMOOTH-direct is
  M9-M1-direct-smooth-residual-blockwise-estimate.
- TOP-M2 is M9-M2-top-endpoint-signed-cone, whose open canonical energy
  child is M9-M2-top-endpoint-density-discrepancy-energy.
- BAL-crit is the persistent critical-$j=1$ double-far energy, equivalently
  its zero-subtracted oscillatory remainder modulo proved terms.
- BAL-rest is
  M9-M2-balanced-remaining-label-owner-quantifier-completion.
- UNBAL is M9-M2-smooth-unbalanced-three-quarter-estimate.

The endpoint node is a uniformity and assembly seam, not another source of
cancellation. It requires all five standard analytic parents, with BAL
itself requiring two independent leaves, uniformly for every literal real
$X$ label, floor, star, support crossing, hard value, short block, and
endpoint.

The alternative tree is

$$
\begin{aligned}
&\mathcal I,\\
&\underbrace{\mathrm{LOWER}_{\rm radial}}_{\rm open}
 \wedge
 \underbrace{\mathrm{NONLOWER/INTERFACE}_{\rm radial}}_{\rm proved}
 \Longrightarrow
 \underbrace{\mathrm{GAR}}_{\rm open}
 \xRightarrow{\rm proved\ total\mbox{-}active\ equivalence}
 \mathrm{M1}_{\rm total},\\
&\mathrm{TOP}_{\rm M2}
 \wedge(\mathrm{BAL}_{\rm crit}\wedge\mathrm{BAL}_{\rm rest})
 \wedge\mathrm{UNBAL}
 \xRightarrow{\mathrm{Phys2}}
 \mathrm{M9\!-\!M2},\\
&\mathrm{M1}_{\rm total}\wedge\mathrm{M9\!-\!M2}
 \xRightarrow{\mathrm{GC\mbox{-}global\mbox{-}M1
 \mbox{-}alternative\mbox{-}bridge}}
 \mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{178.Talt}
$$

Thus

$$
\boxed{\mathrm{GC\mbox{-}target}
\Leftarrow
\mathrm{STANDARD}\ \mathbf{OR}\ \mathrm{GAR\mbox{-}ALTERNATIVE}.}
\tag{178.OR}
$$

The alternative bridge bypasses blockwise M1 only. The M2 statements retain
their own real-centre and endpoint quantifiers.

### 2.2 Sole recommended Round-179 theorem

Put $e(t)=e^{2\pi it}$, and freeze

$$
J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
R_0=\lceil L\rceil,\qquad
R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{178.K1}
$$

For definiteness Round 179 may fix

$$
\delta_0=\gamma_0=\frac14,\qquad Q=(\log(2X))^{100}.
\tag{178.K2}
$$

Any other fixed admissible $0<\delta_0<1/2$, $0<\gamma_0<1$, and fixed
positive conductor exponent is equivalent for power accounting.

Retain the complete Round-176 two-orientation K17a identity on

$$
R_{\log}<2\kappa n<R_0,\qquad
\kappa=\kappa_*<\delta_0L,\qquad
(u,n)<\gamma_0L,\qquad
u\asymp v\asymp L/\kappa,\quad (u,v)=1.
\tag{178.K3}
$$

For $g=(u,n)$, write

$$
u=gu_0,\qquad n=gn_0,\qquad(n_0,u_0)=1,
\tag{178.K4}
$$

and, for odd $m$, put

$$
c_m(k)=\frac{2}{m\{1+e(-k/m)\}}.
\tag{178.K5}
$$

For each divisor $u_0\mid u$ below, set $g=u/u_0$; the conditions
$n=gn_0$ and $(n_0,u_0)=1$ select exactly the stratum $(u,n)=g$.
Using the exact literal Round-176 amplitudes and phases, define

$$
\begin{aligned}
\mathcal H_{\kappa,u,u_0,\ell}
:=\sum_{\substack{v\asymp L/\kappa\\(u,v)=1}}
\sum_{\substack{n=gn_0\ll L/\kappa\\(n_0,u_0)=1}}
\sum_{t\in\mathbb Z}\Bigg\{&
\Lambda^+_{\kappa,u,v,n}(t)
e\!\left(\Psi^+_{\kappa,u,v,n}(t)+\frac t2+
         \frac{\ell\bar v n_0}{u_0}\right)\\
&+\Lambda^-_{\kappa,u,v,n}(t)
e\!\left(\Psi^-_{\kappa,u,v,n}(t)+\frac t2-
         \frac{\ell\bar v n_0}{u_0}\right)
\Bigg\}.
\end{aligned}
\tag{178.K6}
$$

The symbols $\Lambda^\pm$ are not arbitrary bounded coefficients. They
retain the selected/no-pair residual field, squarefree and coprimality
masks, the nonpolylogarithmic determinant and original-gcd cutoffs, Fejer
weight, opposing-displacement inequalities, profiles, floors, stars, hard
values, endpoint conjugations, and full-line zero extension. Both
orientations remain inside the same signed block.

For $\ell\bmod u_0$, let

$$
q=\frac{u_0}{(\ell,u_0)}.
\tag{178.K7}
$$

The sole Round-179 target is

$$
\boxed{
\left|
\sum_{u_0\mid u}
\sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)>Q}}
c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
\right|
\ll_\varepsilon LX^\varepsilon}
\tag{178.K34}
$$

uniformly for every supported odd $(\kappa,u)$. The outer absolute value is
taken only after the gcd-folded aliases, both orientations, all
determinants, incomplete lifts, fibre sites, and literal fields have been
recombined.

The stronger aliaswise estimate

$$
|\mathcal H_{\kappa,u,u_0,\ell}|
\ll_\varepsilon \frac{u_0}{q}LX^\varepsilon
\tag{178.K35}
$$

is sufficient but is not the selected theorem.

The exact capacity ledger is

$$
\#\{\text{literal atoms at fixed }(\kappa,u,u_0)\}\ll u_0L,
\tag{178.K8}
$$

and, at exact conductor $q\mid u_0$,

$$
\sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
\times(\text{literal capacity})
\ll Lq\log(2q).
\tag{178.K9}
$$

Thus (178.K34) needs essentially the full conductor factor $q$, two coupled
square-root savings, or an equivalent signed average before positive
recombination. One reciprocal square root leaves
$L\sqrt q\log(2q)$. Summing the local target costs only

$$
\sum_{\kappa<\delta_0L}\sum_{u\asymp L/\kappa}L
\ll L^2\log(2L)\ll_\varepsilon L^2X^\varepsilon.
\tag{178.K10}
$$

## 3. Proof or derivation

### 3.1 Dependency derivation

M9-M1-physical-one-count-assembly is proved and has exactly two open
analytic blockers: the direct hard M1 cone and the literal smooth residual
M1 estimate. M9-M2-physical-one-count-assembly is proved and has exactly
three open analytic parents: hard TOP, full BAL, and UNBAL. Full BAL has two
independent open leaves. These accepted assemblies give (178.Tstd).

Independently, the complete nonlower/interface radial sector and the coarse
radial one-count assembly are proved. The sole GAR parent is the full exact
lower-radial signed aggregate. The proved GAR-to-total-active equivalence
has an edge only to GC-global-M1-alternative-bridge; it has no edge to
blockwise M9-M1 or M9. This gives (178.Talt) and proves the logical OR.

K17a, K26, and the complete displayed $t=1$ scalar are sufficient routes
inside only one hard-TOP residual/few-point program. K17a or K26 can at most
close the residual scalar after its already paid seams. Even the complete
displayed $t=1$ scalar leaves other
$L\ll D\ll L^2,\ t\ll\sqrt L$ channels and near-collision collars. None may
be substituted for the complete hard-TOP parent.

Round 175 exhausts the proposed new K26 variable: the complete scale chain
has no interior degree of freedom. In contrast, Rounds 176--177 shrink K17a
to one exact high-$q$ block, identify its final conductor, preserve both
orientations, and price every incomplete lift. This does not prove
(178.K34), but it makes (178.K34) a smaller, more falsifiable theorem than
the unchanged K26 endpoint.

### 3.2 Complete frontier comparison

In the table, capacity means a proved positive, absolute, or
coefficient-insensitive upper ledger. It is not literal lower mass. A
missing power is a method deficit, not evidence that the target is false.

| rank / frontier | literal target and coefficient class | capacity and missing power | genuinely new mechanism required | owner leverage if proved alone | downstream scope still open / ranking reason |
|---|---|---|---|---|---|
| **1. K17a high-$q$** | (178.K34): $O(L)$ for each $(\kappa,u)$, hence $O(L^2X^\varepsilon)$ globally. Coefficient is $c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}$ with both orientations and every literal selector, phase, lift, and endpoint field. | Exact-$q$ capacity $Lq\log(2q)$; one square root leaves $L\sqrt q\log q$. Missing essentially $q$, or a second $q^{1/2}$, before positive recombination. Worst per-block positive capacity is $Lu$ up to divisor factors versus target $L$. | Full-conductor saving, two coupled square roots, or an equivalent signed average across retained gcd, alias, modulus, determinant, fibre, or orientation labels. | Closes the exact K17a complement; with proved strict sectors, closes the K17a sufficient residual route. | Full $t=1$, other hard-TOP channels/collars, TOP, BAL, UNBAL, M2, an M1 route, and assembly remain. It ranks first because it is the narrowest new literal block with an unused conductor mechanism. |
| **2. K26 endpoint** | $Q_M^*\ll L^3X^\varepsilon$, equivalently the one-sided whole-chain/K26 endpoint after target-safe zero-mode and short corrections. Coefficient is the complete residual cardinal transform with both parity branches and all cells. | Positive capacity $L^4X^\varepsilon$; missing $L$. | A complete literal coefficient-sensitive maximal-endpoint theorem before scale positivity. | Closes the alternative K26 route to the same residual scalar. | Same downstream gaps as K17a. It ranks lower because the scale index collapses exactly and no finer unused coordinate is isolated. |
| **3. complete displayed $t=1$ scalar** | $\mathcal I_\eta\ll L^{3/2}X^\varepsilon$, equivalently the signed nonzero-frequency double-Poisson aggregate with $g(Q,R)/(QR)$, $\chi_4(k)$, literal cardinal cells, and one outer real part. | Raw $L^2$; favorable collar capacity $\min\{L^2,\sqrt{JL}\}=L^{3/2}\min\{L^{1/2},H/L+O(L^{-1})\}$. Missing $\min\{L^{1/2},H/L\}$; cardinal mean-square placements also retain a structural $\sqrt J$ loss. | A joint $g(Q,R)\chi_4(k)$-signed nonlinear hybrid theorem retaining all cells and hard boundaries before positive norms. | Closes one complete $t=1$ face, broader than either residual route. | Other few-point channels and collars still leave TOP open. The coefficient and endpoint interface is strictly larger, and the functional-equation transform self-returns. |
| **4. complete hard TOP** | $T_{\rm end,L}\ll L^{3/2}X^\varepsilon$, equivalently $E_L^{\rm top}\ll L^2X^\varepsilon$ or $\Re C_{L,\rm tag}^{\rm comp}\ll L^2X^\varepsilon$, with the complete actual hard-top matrix, channels, density/discrepancy modes, collars, endpoints, and real centre. | Scalar $L^2$ versus $L^{3/2}$, or energy $L^3$ versus $L^2$: missing $L^{1/2}$ or $L$. | A complete literal-matrix fixed-actual-direction vector theorem coupling every channel and collar. | Closes hard TOP, one of three M2 parents. | BAL, UNBAL, M2, an M1 route, and assembly remain. It is much larger than the high-$q$ residual block. |
| **5. critical BAL** | $\lvert\mathcal R_B^{\rm osc}\rvert\ll L^3X^\varepsilon$, equivalently $\lvert E_{B,\rm df}\rvert\ll L^3X^\varepsilon$ modulo the proved phase-free term, with both actual symbols, characters, gcd weights, far gates, and endpoints. | Positive capacity $L^4X^\varepsilon$; missing $L$. | A signed nonlocal actual-symbol $q$-primitive/correlation controlling the $(++)$ complement and every ramp-weighted geometric, gcd, alias, fixed-$Q$, gate, and endpoint face. | Closes only the persistent critical-$j=1$ BAL leaf. | BAL-rest and every higher owner remain. Equal factor-$L$ deficit does not merge it with K17a, and its canonical local commutator route is parked. |
| **6. remaining-label BAL** | For every uncovered $1\le K/L\le16$ label, including noncritical $j=1$ and the exact-square $j=2,K/L=16$ boundary, prove $\lvert\sum_GG\mathscr P_G\rvert\ll L^{3/2}X^\varepsilon$ with the literal quarter packet. | Worst positive packet $L^2X^\varepsilon$; missing $L^{1/2}$, equivalently worst physical $X^{1/12}$. | A uniform all-label actual-symbol theorem plus a separate exact-square boundary argument. | Closes only BAL-rest. | Critical BAL remains. This is a larger quantifier-completion interface and no critical-child implication can supply it. |
| **7. UNBAL** | $\mathcal T_{L,K}\ll(LK)^{3/4}X^\varepsilon=M^{3/4}X^\varepsilon$ for every $K/L>16$, with the slanted Vaaler symbol, $\chi_4$, both quarter shifts/signs, floors, stars, entries/exits, and transform boundaries. | Raw positive capacity $M$; missing $M^{1/4}$. | A varying-modulus signed literal-matrix vector theorem retaining every long frequency, inverse selector, weight, level, shift, endpoint, and real centre. | Closes UNBAL, one of three M2 parents. | TOP, BAL, M2, M1/GAR, and assembly remain. The vector theorem is substantially broader than (178.K34). |
| **8. direct hard M1** | Literal normalized hard residual cone $O(L^{3/2}X^\varepsilon)$, hence physical block $O(X^{1/4+\varepsilon})$, with actual $\chi_4$, Vaaler/profile symbol, floors, stars, and real-$X$ hard shell. | Normalized capacity $L^2$; physical capacity $X^{1/4}L^{1/2}\asymp X^{1/3}$ at $L\asymp X^{1/6}$. Missing $L^{1/2}=X^{1/12}$. | An actual-character, actual-Vaaler signed cone theorem on every residual hard shell. | Closes only the hard direct M1 parent. | Smooth direct M1 and all M2 parents remain. This is an old all-shell parent, not a newly isolated conductor block. |
| **9. direct smooth M1** | For every literal smooth label, $B_1(D,L;X)\ll X^{1/4+\varepsilon}$, with both signs, profiles, floors, stars, crossings, and endpoints. | First smooth minimax profile has $X^{1/3+o(1)}$ menu capacity; missing $X^{1/12}$. | A whole-$\mathcal U_1$ signed actual-symbol theorem or a stronger complete Gram estimate with an exact owner bridge. | Closes only the smooth direct M1 parent. | Hard direct M1 and all M2 parents remain. The quantifier range is much wider than K17a. |
| **10. GAR lower owner** | $G_X^{\rm low}\ll X^\varepsilon$, equivalently $\mathcal B_{\rm low}\ll RX^\varepsilon$ for $R=X^{1/4}$, with exact global $C_X^*(n)$, every $D,d,L,t$ layer, floor, star, hard incidence, and the independent cross owner. | Scalar capacity $R^2$ versus $R$, missing $R$; deepest root-defect face has raw $M$ versus $M^{3/4}$, missing $M^{1/4}$. | A joint signed lower-radial/root-defect theorem covering $D>1,L>1$, generic $t=1$, every $t\ge2$, and the cross owner. | Completion of the entire lower owner closes GAR and total active M1 on the alternative tree. | All M2 parents and the alternative bridge remain. Its leverage is high, but its literal scope is far larger than one analytic round. |
| **11. graded local-moment/determinant lane** | At $W=Y^{7/16}$, target actual one-sided determinant correlation $Y^{1/2+\varepsilon}=Y^{24/48+\varepsilon}$ with actual M1/M2 coefficients and prescribed centre. | Best complete bound $Y^{35/48+\varepsilon}$; full target missing $Y^{11/48}$. Strict sub-$1/3$ requires a complete exponent below $Y^{27/48}$, a saving strictly beyond $Y^{8/48}=Y^{1/6}$ from the current bound. | A cross-ray joint signed determinant theorem retaining the literal pair coefficient before arcwise absolute values or positive source norms. | The full target would give the separate exponent $5/16$; a bound below $Y^{27/48}$ would give some strict sub-$1/3$ exponent. | It proves no M9 node and no quarter-tree parent, so it ranks below the full-proof owners despite possible exponent leverage. |
| **12. endpoint, M9, and bridges** | Uniformly verify already proved parent estimates on every physical label and assemble them through M9 or the total-active bridge. | No independent capacity or missing power; these nodes inherit the worst unproved parent. | Literal endpoint/floor/one-count verification after the analytic parents exist. | Closes M9 and the standard bridge, or closes the alternative bridge after GAR and M2. | Cannot be selected now: bookkeeping cannot repair an unproved analytic leaf. |

A new primary-source theorem can outrank this table only if the independent
source audit supplies an exact, versioned theorem matching one of these
literal coefficient and quantifier interfaces after every project power is
restored. This graph report assumes no such import and makes no literature
nonexistence claim.

### 3.3 Why (178.K34) is uniquely first

K17a and K26 have the same residual-only owner leverage. Before Round 175,
K26 ranked first because whole-chain cancellation was a lawful untested
resource. Round 175 proves that this resource vanishes algebraically. The
first K26 theorem is now simply the complete literal endpoint inequality.

Rounds 176--177 produce three strict facts unavailable at the Round-174
checkpoint: fixed-proportion cross gcd is paid, every low reduced alias
conductor is paid, and the remaining power is attached to the final additive
conductor $q$, including all physical lifts. Equation (178.K34) is therefore
a smaller theorem than complete K17a and has a sharp binary outcome: either
a genuinely signed full-conductor mechanism appears, or the first exact seam
where restored $L\sqrt q$ or $Lq$ capacity returns is recorded.

The complete $t=1$, hard TOP, UNBAL, direct M1, and GAR objectives offer more
downstream leverage only by quantifying over much larger literal families.
The two BAL leaves have comparable deficits but are logically separate and
cannot close full BAL alone. The determinant local-moment lane can improve
an exponent but is not a quarter-tree owner. Endpoint and bridge nodes have
no independent cancellation theorem. These comparisons leave exactly one
bounded next objective, (178.K34).

## 4. First doubtful or unproved step

The first doubtful step is exactly (178.K34). Everything before it is
accepted algebra or counting:

- the two opposing affine fibres and their half-frequency character;
- the fibre-stable original gcd $(u,n)$;
- the fold from $u$ to $u_0=u/(u,n)$;
- the exact conductor $q=u_0/(\ell,u_0)$;
- the coefficient identity
  $c_{u_0}(\ell)=(q/u_0)c_q(a)$;
- the $O(u_0L)$ literal lift count and $O(Lq\log q)$ exact-$q$ weighted
  capacity;
- the target-safe $q\le Q$ packet; and
- the target-safe fixed-proportion cross-gcd sector.

No accepted estimate converts the literal selected/no-pair field and
square-root phase into a full $q$-saving, two coupled square-root savings, or
an equivalent signed average. No accepted variation, Fourier-norm,
factorization, residue-bucket-correlation, or orientation-bijection theorem
exists for the literal selector in the required labels. Naming the desired
effect hybrid large sieve, reciprocity, or two-orientation cancellation does
not prove it.

The global summation (178.K10) and the implication from a proved high-$q$
block to the complete K17a residual route are exact once (178.K34) holds.
The uncertainty is analytic and local to (178.K34), not algebraic or
graph-theoretic.

## 5. Required control test and outcome

### 5.1 Campaign controls

| required control | outcome |
|---|---|
| both_lawful_quarter_routes | PASS: (178.Tstd) and (178.Talt) use only authoritative accepted assemblies and explicitly open leaves; the top-level connector is OR. |
| open_owner_and_dependency_status | PASS: no direct M1, M2 parent, endpoint, M9, bridge antecedent, or target is silently closed. |
| K26_and_K17a_exact_Round175_177_frontiers | PASS: K26 is $Q_M^*\ll L^3X^\varepsilon$; K17a is exactly the high-$q$ block after fixed-proportion and low-$q$ sectors. |
| hard_TOP_remaining_channels | PASS: K17a/K26 are residual-only; full $t=1$ and other few-point, collar, density, and endpoint channels remain. |
| critical_and_remaining_BAL_scopes | PASS: persistent critical $j=1$ and all-remaining-label/exact-square completion are independent mandatory leaves. |
| UNBAL_literal_vector_owner | PASS: the scalar reciprocity surface is parked; only a full signed literal-matrix vector theorem could close UNBAL. |
| direct_M1_and_GAR_separation | PASS: the direct route requires two blockwise parents; GAR feeds only the total-active alternative bridge. |
| endpoint_and_bridge_scope | PASS: endpoint uniformity supplies no analytic saving and neither bridge is promoted. |
| graded_sub_one_third_lane | PASS: $Y^{35/48}$, $Y^{27/48}$, and $Y^{24/48}$ remain distinct; no $5/16$ or sub-$1/3$ theorem is claimed. |
| target_capacity_missing_power | PASS: each row states its own normalization, capacity, missing power, coefficient class, and owner scope. |
| single_Round179_objective | PASS: only (178.K34) is selected; (178.K35) is explicitly stronger and unselected. |
| strategy_only_no_analytic_promotion | PASS: this report recommends a next action only and changes no proof status. |
| exponent_quarantine | PASS: (178.1) is unchanged and no local result receives a global exponent without its lawful connector. |
| no_in_round_analytic_pivot | PASS at statement scope: the stop rule forbids a Round-179 pivot to K26, BAL, full $t=1$, or another owner. |

### 5.2 False controls for (178.K34)

1. **Primitive near-half alias.** The aliases
   $\ell=(u_0\pm1)/2$ have $q=u_0$ and
   $|c_{u_0}(\ell)|\asymp1$. Outcome: RED for deleting high aliases or
   treating every coefficient as $u_0^{-1}$-sized.
2. **Premature gcd-alias absolute value.** The exact fold
   $\sum_{j<g}c_u(\ell+ju_0)=c_{u_0}(\ell)$ occurs before absolute values.
   Outcome: RED for paying the $g$ lifts separately.
3. **Rank-one $TT^*$.** Keeping the exact alias matrix reconstructs the
   original physical block squared. Outcome: RED for a contraction coming
   solely from the rank-one alias operator.
4. **Positive Parseval or bucket collision.** Alias Cauchy has available
   self-diagonal capacity $u_0\sqrt L$, and positive bucket Cauchy may return
   the full $Lu_0$ stratum capacity. Outcome: RED as a target proof; neither
   is literal lower mass.
5. **One reciprocal square root.** Exact-$q$ recombination leaves
   $L\sqrt q\log q$. Outcome: RED unless a second coupled saving or a larger
   signed average is proved.
6. **Lift-erasing completion.** The $v$, $n_0$, and fibre repetitions are
   already in (178.K8)--(178.K9). Outcome: RED for replacing the physical
   ranges by one period modulo $q$ without an exact multiplicity theorem.
7. **Anchor antisymmetry.** Although $E_{u_0}(-a)=-E_{u_0}(a)$ for nonzero
   residues, the evident orientation interchange replaces the selected
   divisor by its complement. That complement exits the upper near-square
   window in the odd branch and is even in the even branch. Outcome: RED for
   termwise orientation pairing.
8. **Selector-erased or dechirped arrays.** Such arrays diagnose positive
   capacity but are not the literal residual coefficient. Outcome: RED for a
   coefficient-uniform theorem and INCONCLUSIVE for the actual signed block.
9. **Endpoint deletion.** Hard values, opposing-displacement indicators,
   entries/exits, conjugations, and zero-extension transitions belong to
   $\Lambda^\pm$. Outcome: RED for a smooth-interior-only theorem.
10. **Owner overreach.** Even a GREEN proof of (178.K34) closes at most the
    K17a residual route after the accepted sectors. Outcome: RED for a
    claimed implication to full $t=1$, TOP, M2, M9, a bridge, the quarter
    theorem, or an exponent.

The controls do not disprove (178.K34). They identify what a valid proof
must use beyond the accepted positive and self-return mechanisms.

## 6. Dependencies and exact artifacts used

Artifact metadata:

- campaign: full-proof-round175-177-strategy-literature-review;
- round: 178;
- task: full_graph_frontier_reconstruction;
- role: selected-context discovery / full-graph strategy auditor;
- claimant status: no analytic claimant; graph reconstruction, capacity
  audit, and strategy recommendation only;
- starting graph SHA-256:
  47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7;
- allocation: 100% analytic, algebraic, and graph-theoretic; no numerical
  theorem evidence and no literature search.

The assigned context was read and used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- state/best_proof_draft.md;
- state/project_summary.md;
- strategy/round178_full_proof_strategy_current_literature_review.md;
- rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/full_graph_frontier_reconstruction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/synthesis.md; and
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/synthesis.md.

For exact equation transcription, the accepted kernels referenced by those
authoritative artifacts were also checked:

- proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md; and
- proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md.

The proof graph was parsed in full; all 380 obligation records and 1,456
rejected-claim records were included in the status/dependency audit. The
open-frontier statements, blocker lists, last-round mutations, and graph
hash were independently re-extracted from the canonical file. This was a
read-only consistency check, not mathematical certification by computation.

## 7. Recommended state effect

Recommended effect: retain every proof status and select only (178.K34) for
Round 179. The graph-only closing-label recommendation is
strategy_frontier_retained, relative to the exact high-$q$ frontier left by
Round 177.

Literal promotion gate for a later analytic round:

1. Prove (178.K34) uniformly for every supported $(\kappa,u)$, with both
   orientations, the complete literal coefficient, the exact high-$q$
   cutoff, all incomplete lifts, endpoints, and one blockwise outer absolute
   value retained.
2. Restore the full capacity ledger. Independent reviews must verify the gcd
   fold, conductor definition, exact-$q$ coefficient mass, every
   $v,n_0,t$ multiplicity, the $O(L)$ local target, the
   $O(L^2X^\varepsilon)$ global sum, and every false control in Section 5.
3. Only after those reviews may the proved low-$q$, fixed-proportion
   cross-gcd, polylog-shift, high-original-gcd, and tangent sectors be joined
   to infer the complete K17a sufficient estimate.
4. The allowed mathematical consequence stops at the residual K17a route.
   Any further residual-scalar update requires its exact accepted connector
   and a conductor-owned State Patch. Do not promote full $t=1$, another
   hard-TOP channel, complete TOP, BAL, UNBAL, M9-M2, either M1 route,
   endpoint uniformity, M9, either bridge, GC-target, or any exponent.

Round-179 stop rule: stop at the first failed literal-selector, orientation,
gcd-fold, conductor, lift-multiplicity, parity, determinant-range, endpoint,
or $O(L)$-per-block gate. Stop if an argument takes absolute values before
the complete $u\to u_0$ fold or before both orientations are recombined; if
it reduces to exact rank-one $TT^*$, positive alias Parseval, positive bucket
collisions, one reciprocal square root, completion modulo $q$ with erased
lifts, or complementary-divisor orientation pairing; or if its restored
capacity is $L\sqrt q$, $Lq$, $Lu_0$, or $Lu$ rather than $L$ up to
$X^\varepsilon$. Record the first exact failure as a scoped no-go. Do not
pivot in-round to (178.K35), K26, full $t=1$, BAL, UNBAL, M1, GAR, the
determinant exponent lane, or endpoint assembly.

Downstream scope after a successful Round 179 remains deliberately narrow:
the rest of $t=1$, every other hard-TOP few-point channel and collar,
complete hard TOP, both BAL scopes, UNBAL, M9-M2, both direct M1 parents or
complete GAR, endpoint/one-count assembly, the appropriate bridge, and the
quarter theorem would all still require proof. No global exponent changes
until a complete lawful exponent connector is proved.

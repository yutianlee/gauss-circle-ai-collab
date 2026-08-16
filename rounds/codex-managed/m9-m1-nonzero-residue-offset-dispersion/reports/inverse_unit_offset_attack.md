# Round 83 analytic report: inverse-unit offset attack

## 1. Result

No fixed power of $B=C/T$ is proved, hence no conductor interval is
extended.  Two exact advances are proved.

First, the two even local units can be opened without a sign inference.
Write $k=\rho\sigma\ne0$, and in an even class let

\[
 bs_0+\rho=tc,\qquad 0\le s_0<c.                       \tag{1.1}
\]

After the reciprocal factors in the Round-72 identities have been put
inside $e(\pm A_{\kappa,b}/c)$, the varying parts of the three units are
as follows.  Put $g_\kappa=4\kappa$, $c=g_\kappa x$, and
$M_\kappa=4b/g_\kappa$.  Then

\[
 u_{\kappa,b,k}(g_\kappa x)
   =\zeta_{\kappa,b,k}\,e_{M_\kappa}(K_{\kappa,b,k}\bar x),
   \qquad (x,M_\kappa)=1,                                \tag{1.2}
\]

where $|\zeta_{\kappa,b,k}|=1$ is independent of $x$, and

\[
\begin{array}{c|c|c|c}
 \kappa &g_\kappa&M_\kappa&K_{\kappa,b,k}\\ \hline
 1/4&1&4b&k,\\
 1/2&2&2b&2[k\bar4]_b,\\
 1&4&b&[k\bar4]_b.
\end{array}                                               \tag{1.3}
\]

In the middle line $2[k\bar4]_b$ denotes the well-defined even lift
modulo $2b$.  In particular
$(K_{\kappa,b,k},M_\kappa)\ll_k1$.  Thus every class, not only the odd
class, has an ordinary inverse-unit completion after the exact rescaling
$c=g_\kappa x$.  Its offset unit is

\[
 u(gx)\overline{u(g(x+a))}
 =e_M\!\left(Ka\,\overline{x(x+a)}\right).                \tag{1.4}
\]

Second, the zero *dual difference* inside the already nonzero residue-
offset energy is target-safe collectively over all offsets and moduli.
With the exact transform defined in Section 2, its total contribution is

\[
 \mathfrak Z_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon{C^2\over T}
 \le X^\varepsilon{J^2\over T}.                           \tag{1.5}
\]

The strict survivor is therefore the centred, nonzero-shift
Kloosterman correlation

\[
 \boxed{
 \mathfrak Y_C^{(\kappa,k)}
 =\sum_{b\asymp B}{1\over M_{\kappa,b}^2}
 \sum_{d\ne0}\sum_{n\in\mathbb Z}
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.}                              \tag{1.6}
\]

Here (M=M_{\kappa,b}) in every summand.  Formula (1.6) has the complete
actual Fourier weights; no
stationary truncation has been made.  Proving
$\mathfrak Y_C^{(\kappa,k)}\ll_\varepsilon X^\varepsilon J^2/T$,
or the corresponding $B^{-\delta}$ gain, is
the first unproved inequality.

There is also an all-class route-specific no-go.  Completing the offset
in (1.6) gives exactly the Kloosterman product minus $c_M(d)$.  Full
completion followed by inversion is therefore the original residue row
in all three classes, not a source of a $B$-saving.  The estimate (1.5),
not the change of representation, is the genuine reduction.

## 2. Exact statement and hypotheses

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and assume

\[
 J^{13/18}<C\le J^{3/4}.                                  \tag{2.1}
\]

Fix one smooth-interior nonaxial component, orientation, alias,
compatible $k=\rho\sigma\ne0$, and
$\kappa\in\{1/4,1/2,1\}$.  Use the exact transition-flattened
principal row

\[
 \sum_{c\asymp C}u_{\kappa,b,k}(c)
 V_{b,c,k}^{(\kappa)}e\!\left(\epsilon {A_{\kappa,b}\over c}\right),
 \qquad \epsilon\in\{1,-1\},                             \tag{2.2}
\]

with all of its inherited smooth cutoffs and one-count endpoints, where

\[
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2\asymp bX,
 \qquad
 \|V\|_\infty+\operatorname {Var}V
 \ll_\varepsilon X^\varepsilon.                          \tag{2.3}
\]

The pointwise transition remainder and both axes are not part of (2.2)
and retain their separate accepted owners.

Put $g=g_\kappa$, $M=M_\kappa$, $K=K_{\kappa,b,k}$, and

\[
 F_b(x)=V_{b,gx,k}^{(\kappa)}
 e\!\left(\epsilon {A_{\kappa,b}\over gx}\right),
 \qquad
 I_b(n)=\int_{\mathbb R}F_b(x)e\!\left(-{nx\over M}\right)dx.       \tag{2.4}
\]

Thus $F_b$ is supported on $x\asymp L=C/g$.  Set

\[
 S(n,K;M)=\sum_{x\bmod M}^{*}e_M(nx+K\bar x)              \tag{2.5}
\]

and

\[
 \mathcal C_{M,K}(d,a)
 ={1\over M}\sum_{n\bmod M}
 S(n+d,K;M)\overline{S(n,K;M)}e_M(-an).                   \tag{2.6}
\]

Then finite orthogonality gives

\[
 \mathcal C_{M,K}(d,a)
 =\sum_{\substack{y\bmod M\\(y(y+a),M)=1}}
 e_M\!\left(d(y+a)+K(\overline{y+a}-\bar y)\right),       \tag{2.7}
\]

\[
 \mathcal C_{M,K}(d,0)=c_M(d),                            \tag{2.8}
\]

and

\[
 S(n+d,K;M)\overline{S(n,K;M)}
 =\sum_{a\bmod M}\mathcal C_{M,K}(d,a)e_M(an).            \tag{2.9}
\]

The original nonzero residue-offset energy for this component is exactly

\[
 \mathfrak X_C^{(\kappa,k)}
 =\sum_{b\asymp B}{1\over M_{\kappa,b}^2}
 \sum_{d,n\in\mathbb Z}
 \sum_{\substack{a\bmod M\\a\ne0}}
 \mathcal C_{M,K}(d,a)e_M(an)
 I_b(n+d)\overline{I_b(n)}.                               \tag{2.10}
\]

As in (1.6), $M=M_{\kappa,b}$ varies with $b$.  Empty parity or gcd
offsets in (2.10) contribute zero.  All sums are understood through the
exact Poisson identity (or its symmetric limiting form); (2.10) has no
discarded stationary errors or tails.

The exact conclusion is

\[
 \mathfrak X_C^{(\kappa,k)}
 =\mathfrak Z_C^{(\kappa,k)}+\mathfrak Y_C^{(\kappa,k)},   \tag{2.11}
\]

where $\mathfrak Y_C$ is (1.6) and

\[
 \mathfrak Z_C^{(\kappa,k)}
 =\sum_{b\asymp B}{1\over M_{\kappa,b}^2}
 \sum_{n\in\mathbb Z}
 \bigl(|S(n,K;M)|^2-\varphi(M)\bigr)|I_b(n)|^2           \tag{2.12}
\]

satisfies (1.5).

## 3. Proof or derivation

**Derivation of the even units.**  Suppose first that
$c\equiv2\pmod4$, write $c=2x$, and use (1.1).  Here $b,x,\rho$,
and $\sigma$ are odd.  The exact Round-72 factor after extraction of
$e(-k/(2bc))$ is

\[
 u(c)=\chi_4(s_0)e_{2b}(\sigma t).                         \tag{3.1}
\]

Reducing $bs_0+\rho=2tx$ modulo (4), and using that $x$ is odd,
gives

\[
 \chi_4(s_0)
 =-\chi_4(b)\chi_4(\rho)(-1)^t.                            \tag{3.2}
\]

Indeed, for even $t$, $bs_0\equiv-\rho\pmod4$, while for odd
$t$, $bs_0\equiv2-\rho\equiv\rho\pmod4$.  Hence

\[
 \begin{aligned}
 u(c)
 &=-\chi_4(b)\chi_4(\rho)e_{2b}((b+\sigma)t)\\
 &=-\chi_4(b)\chi_4(\rho)
   e_b\!\left({b+\sigma\over2}t\right).
 \end{aligned}                                            \tag{3.3}
\]

Modulo (b),

\[
 t\equiv\rho\overline{2x},\qquad
 {b+\sigma\over2}\equiv\sigma\bar2,
\]

so (3.3) becomes the exact inverse unit

\[
 u(2x)=-\chi_4(b)\chi_4(\rho)e_b(k\overline{4x}).          \tag{3.4}
\]

Since $x$ runs through the units modulo $2b$, (3.4) is the middle
line of (1.3).

If $4\mid c$, write $c=4x$.  The extracted unit is

\[
 u(c)=\chi_4(s_0)e_b(\sigma t).                            \tag{3.5}
\]

Now (1.1) modulo (4) gives $bs_0\equiv-\rho\pmod4$, and therefore

\[
 \chi_4(s_0)=-\chi_4(b)\chi_4(\rho),\qquad
 t\equiv\rho\overline{4x}\pmod b.                        \tag{3.6}
\]

Thus

\[
 u(4x)=-\chi_4(b)\chi_4(\rho)e_b(k\overline{4x}),          \tag{3.7}
\]

which is the last line of (1.3).  This used the two exact even lifts
separately.  The odd line is the accepted
$u(c)=\zeta e_{4b}(k\bar c)$.  Opposite orientations conjugate the
corresponding unit and reciprocal phase; all identities and bounds below
are unchanged after $K\mapsto-K$.

In each class, the map $c=gx\pmod {4b}$ is a bijection from the exact
admissible residue set to $x\in(\mathbb Z/M\mathbb Z)^\times$.  It
also turns a class-compatible original offset into one and only one
$a\pmod M$.  Formula (1.4) follows from

\[
 \bar x-\overline{x+a}
 =a\,\overline{x(x+a)}\pmod M.                             \tag{3.8}
\]

For $\kappa=1/2$, impossible odd $a$'s in the scaled modulus have no
admissible $x,x+a$; analogous parity exclusions in the odd class are
also automatic in (2.7).

**Exact all-class completion.**  Poisson summation on each progression
gives

\[
 \sum_{x\bmod M}^{*}e_M(K\bar x)
 \sum_{\ell\in\mathbb Z}F_b(x+M\ell)
 ={1\over M}\sum_{n\in\mathbb Z}S(n,K;M)I_b(n).           \tag{3.9}
\]

Squaring (3.9), putting the two Fourier indices equal to $n+d$ and
$n$, and using (2.9) proves (2.10).  The term $a=0$ is precisely the
same-residue mode, because (2.7) then forces the same unit residue and
(2.8) is the complete Ramanujan contribution.  It is removed exactly
once in (2.10).  For $d=0$, (2.9) and (2.8) give

\[
 \sum_{a\ne0}\mathcal C_{M,K}(0,a)e_M(an)
 =|S(n,K;M)|^2-\varphi(M),                                 \tag{3.10}
\]

which proves (2.11)--(2.12).  For $d\ne0$, the same calculation gives
(1.6).

**Bound for the zero dual difference.**  The classical Weil--Estermann
bound for the complete Kloosterman sum (2.5) gives

\[
 |S(n,K;M)|
 \le \tau(M)(n,K,M)^{1/2}M^{1/2}
 \ll_\varepsilon X^\varepsilon M^{1/2}.                   \tag{3.11}
\]

Indeed, $k\ne0$ is fixed and (1.3) gives
$(K,M)\ll_k1$; in the middle class the only additional common factor is
the fixed factor $2$.  Thus $(n,K,M)\le(K,M)\ll_k1$ uniformly in
$n$, including $n=0$.  Hence

\[
 \bigl||S(n,K;M)|^2-\varphi(M)\bigr|
 \ll_\varepsilon X^\varepsilon M.                         \tag{3.12}
\]

It remains to retain the actual Fourier weight rather than replace it by
an arbitrary sequence.  Sampling Parseval gives the exact identity

\[
 \sum_{n\in\mathbb Z}|I_b(n)|^2
 =M\sum_{h\in\mathbb Z}
 \int_{\mathbb R}F_b(x+hM)\overline{F_b(x)}\,dx.           \tag{3.13}
\]

The $h=0$ integral is
$O_\varepsilon(X^\varepsilon C/g)$.  For $h\ne0$, overlap of the two
dyadic supports requires $1\le |h|\ll L/M\ll T$.  On an overlap, the
phase difference has derivative of constant sign and size

\[
 \left|{d\over dx}{A_{\kappa,b}\over g}
 \left({1\over x+hM}-{1\over x}\right)\right|
 \asymp {A_{\kappa,b}|h|M\over gL^3}
 \asymp {g|h|Q^2\over C}.                                 \tag{3.14}
\]

It is monotone on the positive dyadic overlap.  The product amplitude has
supremum plus total variation $O_\varepsilon(X^\varepsilon)$, so the
first-derivative lemma yields

\[
 \left|\int F_b(x+hM)\overline{F_b(x)}\,dx\right|
 \ll_\varepsilon X^\varepsilon{C\over gQ^2|h|}.            \tag{3.15}
\]

This estimate includes the smallest shift $h=1$: throughout (2.1),
$Q^2/C\ge J^{1/20}$.  Larger shifts only improve it, and negative or
wraparound shifts follow by conjugation and translation.  Summing (3.15)
and inserting it into (3.13) gives

\[
 \sum_n|I_b(n)|^2
 \ll_\varepsilon X^\varepsilon M{C\over g}.               \tag{3.16}
\]

Equations (2.12), (3.12), and (3.16) imply, for one fixed
$b\asymp B$,

\[
 |\mathfrak Z_b^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon {C\over g}
 \ll_\varepsilon X^\varepsilon C.
\]

There are $O(B)$ such moduli.  Therefore

\[
 |\mathfrak Z_C^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon
 \sum_{b\asymp B}{C\over g}
 \ll_\varepsilon X^\varepsilon BC.                       \tag{3.17}
\]

Since $B=C/T$ and $C\le J$,

\[
 {C^2\over T}\le {J^2\over T},
\]

so (3.17) proves (1.5) on the full frozen band.

**Why completion itself gives no saving.**  For every $d,n$, the exact
identity

\[
 \sum_{a\ne0}\mathcal C_{M,K}(d,a)e_M(an)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)                    \tag{3.18}
\]

holds in all three classes.  Consequently complete Poisson, completion
in $a$, or their inverses simply move between (2.10) and (1.6).
Termwise square-root bounds for (2.7), followed by absolute summation in
$a$, cannot be labelled a $B$-gain: (3.18) restores the full
Kloosterman product.  The only estimate made after the transform is the
actual-weight diagonal estimate (3.17).

## 4. First doubtful or unproved step

The first unproved step is a signed estimate for (1.6), uniformly in the
varying moduli $M\asymp B$, with the actual correlated Fourier weights
$I_b(n+d)\overline{I_b(n)}$.  Any fixed gain

\[
 \mathfrak Y_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon
 B^{-\delta}{C^3\over TQ^{5/12}}                           \tag{4.1}
\]

would give the already recorded endpoint $c_\delta$, but no such gain
follows from (3.11), (3.18), or Parseval.

The obstruction is exact rather than heuristic.  The $a$-sum of the
rational trace kernel is the product in (3.18); full completion therefore
has its original operator capacity.  Conversely, forgetting the
reciprocal origin of $I_b$ permits the phase-conjugating residue choice
$R(x)=H\overline{u(x)}$, which saturates the cross energy.  Thus a future
proof must use a joint shifted-Kloosterman/archimedean correlation in
$b,d,n$, not an arbitrary-coefficient large sieve and not another full
transform.

No claim is made that the modes $d\equiv0\pmod M$ with $d\ne0$, or
the modes with $(d,a,M)>1$, are harmless.  They remain inside (1.6).
Confusing them with the literal integer shift $d=0$ would be the first
invalid extension of (1.5).

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | **Pass.**  The absolute offset ledger is $C^3/(TQ^{5/12})$, the target is $J^2/T$, and $B=C/T$.  The removed part is $C^2/T$, whose ratio to the target is $(C/J)^2\le J^{-1/2}$. |
| Residue-offset one-count | **Pass.**  $c=gx\pmod {4b}$ bijects the exact class with units modulo $M$.  Each ordered unequal pair has exactly one $a\ne0\pmod M$; empty parity offsets vanish in (2.7). |
| Same-residue removed once | **Pass.**  It is exactly $a=0$, giving $\mathcal C(d,0)=c_M(d)$.  Formula (1.6) subtracts this term and does not remove it again. |
| Odd inverse unit | **Pass.**  The accepted $e_{4b}(k\bar c)$ is the first line of (1.3), and (1.4) gives the prescribed rational offset phase. |
| Even local units | **Pass.**  Equations (3.1)--(3.7) separately derive the $c\equiv2\pmod4$ and $4\mid c$ units from $bs_0+\rho=tc$.  Neither is inferred from the odd class. |
| Actual weight dependence | **Pass.**  $I_b$ is the Fourier transform of the complete $V(gx)e(\pm A/(gx))$.  The proof of (3.16) uses both its global BV norm and its reciprocal phase. |
| Small, large, and wraparound offsets | **Pass without deletion.**  Equation (2.10) contains every nonzero class-compatible $a\pmod M$.  Small $a$, $M-a$, and all intermediate offsets are retained; wraparound is a choice of representative only. |
| Gcd and zero exceptional modes | **Pass in stated scope.**  The literal $d=0$ slice is proved safe, including $n=0$.  The same-residue zero mode is $a=0$.  Nonzero $d\equiv0\pmod M$ and gcd-degenerate rational sums remain in (1.6), with no unproved square-root assertion. |
| Complete-transform self-return | **Pass.**  Equations (3.9) and (3.18) show exact return for odd and both even classes.  No gain is assigned to the representation change. |
| Perfect-square and fourth-power controls | **Pass for the proved slice.**  The bound uses only $A_{\kappa,b}\asymp bX$; perfect-power values do not make (3.14) degenerate.  No conclusion about their contribution to (1.6) is asserted. |
| Phase-conjugating/adversarial control | **Pass as a no-go.**  Arbitrary residue weights can conjugate $u$, so (4.1) cannot be coefficient-uniform.  The proved diagonal estimate uses the actual reciprocal weight. |
| Transition and axis ownership | **Pass.**  Only the smooth principal row is transformed.  The pointwise transition remainder and both axes remain under their accepted separate estimates. |
| Downstream scope | **Pass.**  No claim is made for $C>J^{3/4}$, cone edges, other sectors, full `M9-M1`, `M9`, endpoint uniformity, or the Gauss-circle exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The assigned selected context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_residue_normalization.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/chirped_residue_energy_attack.md`;
- `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reviews/conductor_round81_transition_normalization.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/briefs/inverse_unit_offset_attack.md`.

To type the two even units, I also used the exact finite antecedents
indexed by the proof graph:

- `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reviews/conductor_round71_adjudication.md` (the three local factors);
- `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_third_derivative_seam_review.md` (the lift (1.1) and the two extracted reciprocal identities).

No sibling Round-83 report was read.  No web source or numerical
experiment was used.  The only named complete-sum input is the classical
Weil--Estermann bound in (3.11), already part of the accepted
Kloosterman-completion infrastructure used by the proof graph.  It
introduces no new modern-source hypothesis or source-audit dependency:
the exact modulus, arguments, and gcd factor are displayed and matched in
(1.3), (2.5), and (3.11).  The even-unit reduction, all-class finite
Fourier algebra, sampling identity, and reciprocal autocorrelation
estimate are derived in this report.

## 7. Recommended state effect

**Promote, after independent seam review,** the scoped all-class unit
normal form (1.2)--(1.4) and the target-safe zero-dual-difference lemma
(1.5).  **Revise** the first-band smooth-principal survivor from the raw
coherent offset sum to the strictly smaller centred correlation (1.6).

**Retain** the $B^{-\delta}$ offset-dispersion estimate, the conductor
extension, `M9-M1`, `M9`, and the global exponent as open.  Record the
all-class identity (3.18) as a route-specific no-go: complete offset
Poisson or inverse completion alone is an involution and supplies no
power of $B$.  The next lawful target is a signed estimate for (1.6)
that keeps the actual $I_b(n+d)\overline{I_b(n)}$ weights and treats
the nonzero gcd-degenerate modes explicitly.

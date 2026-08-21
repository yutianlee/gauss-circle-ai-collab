# Blind \(q=1\) diagonal rederivation

## 1. Result

The singleton \(q\)-row has an exact normalization but, from the blind packet alone, no parameter-only estimate for its actual coefficient is derivable.  If

\[
 f_a(q):=\mathbf 1_{q=1}F_a(1),
\]

then

\[
 \sum_q|f_a(q)|^2=|F_a(1)|^2,
 \qquad
 \sum_q f_a(q+r)\overline{f_a(q)}=0\quad(r\in\mathbb Z\setminus\{0\}).
\]

Thus there is literally no nonzero \(q\)-shift and no \(q\)-averaging gain on this block.  The desired estimate is an estimate of the actual within-\(a\) coefficient itself.

Writing \(d_a=\sqrt{a(a+2)}\), the exact geometric normalization is

\[
 \delta_a^2=2(a+1-d_a)=\frac{2}{a+1+d_a},
 \qquad
 \Lambda_a=X(a+1-d_a)=\frac{X}{a+1+d_a}.
\]

The strongest unconditional direct energy statement supplied by the packet is only

\[
 0\leq \mathcal D_1^{\rm act}
 \leq |\mathcal A_A|\sup_{a\in\mathcal A_A}|F_a(1)|^2
 \ll A\sup_{a\in\mathcal A_A}|F_a(1)|^2,
\]

where \(\mathcal A_A\) is the dyadic set of \(a\)'s.  No bound for the supremum, or for any atomic mass defining \(F_a(1)\), occurs in the allowed premises.  This is a statement-level no-go, not a counterexample to the intended actual coefficient.

If the omitted definition is written as a finite sum of its actual entries,

\[
 F_a(1)=\sum_{\xi\in\Omega_a}C_a(\xi),
\]

then the strongest cancellation-free estimate is

\[
 \mathcal D_1^{\rm act}
 \leq \sum_a\left(\sum_{\xi\in\Omega_a}|C_a(\xi)|\right)^2
 \leq \sum_a |\Omega_a|\sum_{\xi\in\Omega_a}|C_a(\xi)|^2.
\]

Here \(C_a\) denotes the actual metric density-discrepancy entry, with every stated mask and orientation retained; it is not an arbitrary bounded replacement.  The smallest remaining signed object is the same-\(a\), off-diagonal pair kernel

\[
 \mathscr K_{\rm off}
 :=2\operatorname{Re}\sum_a\sum_{\xi<\eta\atop \xi,\eta\in\Omega_a}
 C_a(\xi)\overline{C_a(\eta)}.
\]

No Pell, endpoint, or empty-fibre test in the statement forces this kernel, or \(F_a(1)\), to have a favorable sign or a positive size.

## 2. Exact statement and hypotheses

Assume only the blind packet: \(a\) is a positive integer in one dyadic block \(a\asymp A\), \(X>0\), \(J=\sqrt X\), the primitive row has support only at \(q=1\), and

\[
 K\asymp \frac JA,\qquad G\asymp\frac LA,
 \qquad \rho=\frac{AJ}{L^3}>1.
\]

No pointwise size, phase, summation formula, or multiplicity formula for \(F_a(1)\) is assumed.  In particular, the words “complete metric density-discrepancy coefficient” are not replaced by an invented model.

For each \(a\), put

\[
 \ell_a:=\frac{J\delta_a}{2\sqrt a},\qquad
 u_a:=\frac{J\delta_a}{\sqrt{a+2}},\qquad
 I_a:=\{k\in\mathbb Z:\ell_a<k<u_a\}.
\]

Then the following claims hold exactly.

- The reciprocal endpoints and their width are

  \[
  \ell_a=\frac{J}{a+d_a},\qquad
  u_a=\frac{2J}{a+2+d_a},\qquad
  u_a-\ell_a=
  \frac{J(a+d_a-2)}{(a+d_a)(a+2+d_a)}.
  \]

- Since \(a<d_a<a+1\),

  \[
  \frac{X}{2a+2}<\Lambda_a<\frac{X}{2a+1},
  \quad
  \frac{J}{2a+1}<\ell_a<\frac{J}{2a},
  \quad
  \frac{2J}{2a+3}<u_a<\frac{J}{a+1}.
  \]

  In particular, \(\Lambda_a\asymp X/A\), the interval has the asserted \(J/A\) scale, and

  \[
  |I_a|=
  \max\{0,\lceil u_a\rceil-\lfloor\ell_a\rfloor-1\}
  \leq 1+(u_a-\ell_a)
  <1+\frac{J}{2a}
  \ll 1+K.
  \]

- If the actual formula has one potential entry for each admissible \((k,g,\text{orientation})\), with the named masks only deleting entries, then its atomic support obeys the conditional cardinality bound

  \[
  |\Omega_a|\leq 2|I_a|\,|\Gamma_G|\ll (1+K)(1+G),
  \]

  where \(\Gamma_G\) is the finite odd lift set \(g\asymp G\).  This cardinality statement does not bound the actual coefficient mass.

- With the nominal scales \(K_0=J/A\) and \(G_0=L/A\),

  \[
  \rho=\frac{K_0}{A G_0^3},\qquad
  \frac{L^4}{A}=A^3G_0^4,
  \qquad
  \left(\frac1A\frac{L^4}{A}\right)^{1/2}
  =\frac{L^2}{A}=A G_0^2.
  \]

  Hence the target asks for root-mean-square row size

  \[
  |F_a(1)|_{\rm rms}\ll_\varepsilon
  X^{\varepsilon/2}\frac{L^2}{A}
  \asymp X^{\varepsilon/2}A G^2.
  \]

  Equivalently, its allowed mean square per dyadic \(a\)-row is, up to block constants,

  \[
  X^\varepsilon A^2G^4
  \asymp X^\varepsilon\frac{A K G}{\rho}.
  \]

## 3. Proof or derivation

Rationalizing the square-root difference gives

\[
 \delta_a=\frac{2}{\sqrt{a+2}+\sqrt a}.
\]

Also

\[
 (a+1-d_a)(a+1+d_a)=(a+1)^2-a(a+2)=1.
\]

Squaring \(\delta_a\) therefore yields

\[
 \delta_a^2=2(a+1-d_a)=\frac{2}{a+1+d_a},
\]

and multiplication by \(X/2\) gives the formula for \(\Lambda_a\).  Dividing the rationalized \(\delta_a\) by \(2\sqrt a\) and by \(\sqrt{a+2}\) gives the two endpoint identities.  Their difference gives the displayed width.  The inequalities follow from

\[
 a^2<a(a+2)<(a+1)^2
\]

for every positive integer \(a\).  The exact open-interval integer count is the elementary floor/ceiling formula in Section 2; the upper bound uses that an open interval of length \(w\) contains at most \(w+1\) integers.  These steps also show explicitly why a \(+1\) endpoint loss cannot be dropped when \(K\) is small.

The \(q\)-identities follow directly from the support of \(f_a\).  For \(r\ne0\), the conditions \(q=1\) and \(q+r=1\) cannot both hold.  This is only a singleton-row identity and supplies no statement about a longer-row Gram matrix.

For an actual finite decomposition \(F_a(1)=\sum_\xi C_a(\xi)\), expansion gives

\[
 \mathcal D_1^{\rm act}
 =\underbrace{\sum_a\sum_{\xi\in\Omega_a}|C_a(\xi)|^2}_{\mathscr E_{\rm diag}}
 +\underbrace{2\operatorname{Re}\sum_a
 \sum_{\xi<\eta}C_a(\xi)\overline{C_a(\eta)}}_{\mathscr K_{\rm off}}.
\]

Triangle inequality and then Cauchy--Schwarz give the direct estimates in Section 1.  Notice that \(\mathscr E_{\rm diag}\) is not by itself a lower bound for the energy: the signed kernel can be negative.  Conversely, a bound for the absolute size of \(\mathscr K_{\rm off}\) does not manufacture the cancellation that would be needed if the diagonal mass exceeds the target.

There is an exact Pell specialization.  Fix a nonsquare positive integer \(D\) and a positive solution

\[
 u^2-Dv^2=1,
\]

and set \(a=u-1\).  Then

\[
 d_a=v\sqrt D,\qquad
 \delta_a^2=2(u-v\sqrt D),\qquad
 \Lambda_a=X(u-v\sqrt D)=\frac{X}{u+v\sqrt D}.
\]

Thus the Pell unit has exactly the ordinary size \(u-v\sqrt D\asymp 1/u\asymp1/a\); it does not, by itself, improve or contradict the block normalization.  It may organize arithmetic phases, but those phases are absent from the packet, and the primitive, owner, annulus, and physical masks may delete the corresponding entry.

For the fourth-power control, let \(X=T^4\) with nonzero integer \(T\), so \(J=T^2\).  The number \(d_a\) is irrational for every \(a\ge1\): if it were rational, it would be an integer and

\[
 (a+1-d_a)(a+1+d_a)=1
\]

would force \(a=0\).  Consequently \(\Lambda_a\), \(\ell_a\), and \(u_a\) are irrational at fourth powers.  In particular, neither reciprocal endpoint is an integer there.  For general real \(X\), however, exact boundary contact is possible and occurs at

\[
 J=k(a+d_a)\quad\text{or}\quad
 J=\frac{k}{2}(a+2+d_a).
\]

Hence strictness is harmless for integer endpoint equality at fourth powers, but it cannot be discarded uniformly as \(X\) and the moving endpoints vary.

Finally, the premise contains no numerical or structural restriction on the magnitude of \(F_a(1)\).  Formally, all displayed geometric assertions remain true if the otherwise-unconstrained symbol \(F_a(1)\) is assigned zero or is assigned an arbitrarily large value.  This proves only underdetermination of the blind packet; it does not alter or adversarially replace the intended coefficient.

## 4. First doubtful or unproved step

The first unavailable object is the defining formula for the actual summands \(C_a(\xi)\), including their magnitude, phase, lift multiplicity, profiles, floors, stars, and every mask.  Therefore the first sufficient direct inequality that is missing is

\[
 \boxed{
 \sum_a\left(\sum_{\xi\in\Omega_a}|C_a(\xi)|\right)^2
 \ll_\varepsilon X^\varepsilon\frac{L^4}{A}.}
 \tag{D}
\]

Under the conditional support bound in Section 2, a still stronger sufficient condition would be

\[
 \sum_a\sum_{\xi\in\Omega_a}|C_a(\xi)|^2
 \ll_\varepsilon
 X^\varepsilon\frac{L^4}{A(1+K)(1+G)}.
\]

Neither inequality can be checked from the packet.  If the cancellation-free inequality \((D)\) is false or too expensive, the first genuinely signed task is an upper estimate for the exact combination

\[
 \mathscr E_{\rm diag}+\mathscr K_{\rm off}
 \ll_\varepsilon X^\varepsilon\frac{L^4}{A},
\]

where the irreducible signed kernel is

\[
 \mathscr K_{\rm off}
 =2\operatorname{Re}\sum_a\sum_{\xi<\eta}
 C_a(\xi)\overline{C_a(\eta)}.
\]

This kernel is internal to one \(a\)-row.  There is no \(q\)-shift kernel left to estimate.  Proving the needed signed upper bound requires an explicit cancellation property of the actual coefficient; arbitrary signs, absolute values, or raw tuple counts cannot supply it.

## 5. Required control tests and outcomes

All outcomes below are algebraic statement tests, not numerical evidence.

| Control | Exact input | Expected failure or invariant | Observed result | Implication |
|---|---|---|---|---|
| Singleton \(q=1\) | Zero-extended \(f_a(q)=\mathbf1_{q=1}F_a(1)\) | Every nonzero \(q\)-shift should have empty overlap | The shifted correlation is exactly zero for \(r\ne0\), while the zero shift is \(\lvert F_a(1)\rvert^2\) | No longer-row or off-shift gain may be imported |
| Raw versus weighted | The counts \(\lvert I_a\rvert\), \(\lvert\Gamma_G\rvert\), and the actual masses \(\lvert C_a(\xi)\rvert\) | A raw count must not determine weighted energy without coefficient summation | The packet proves only \(\lvert I_a\rvert\ll1+K\); it gives no coefficient envelope | A literal upper bound needs \((D)\) or an actual weighted substitute |
| Signed versus unsigned and coefficient adversary | \(C_a(\xi)\), \(\lvert C_a(\xi)\rvert\), random phases, and adversarial phases of the same sizes | The off-diagonal kernel should change under phase replacement | The exact expansion changes in the off-diagonal terms; only the triangle bound is phase-blind | No estimate for arbitrary bounded weights is credited to the actual coefficient, and no actual cancellation is inferred from an adversarial model |
| Real versus complex pairing | Genuinely complex actual entries | Conjugation must be retained | The exact kernel is \(2\operatorname{Re}(C_a(\xi)\overline{C_a(\eta)})\) | A \(\operatorname{Re}\)-shortcut without conjugacy hypotheses is unavailable |
| Exact versus near resonance | Exact singleton \(q\)-support versus any internal metric phase relation | Vanishing \(q\)-shifts should not imply exact or near phase resonance | Only the \(q\)-support statement is proved; no internal phase is specified | Exact, smallest nonzero, and fat metric bands remain separate and untested |
| Pell near-square family | \(u^2-Dv^2=1\), \(a=u-1\) | Check whether a quadratic near-square forces anomalous normalization or coefficient mass | \(\Lambda_a=X(u-v\sqrt D)=X/(u+v\sqrt D)\asymp X/a\); masks and signs remain unknown | Pell arithmetic alone gives neither a counterexample nor a lower bound for the actual energy |
| Strict reciprocal/metric annuli | The open interval \(\ell_a<k<u_a\), plus the packet's unnamed inner metric annuli | Boundary equality must be excluded exactly | The reciprocal count is \(\max(0,\lceil u_a\rceil-\lfloor\ell_a\rfloor-1)\); the inner annulus formula is absent | Keep strict indicators.  Any closing, thickening, or smoothing requires a separately bounded boundary term |
| Fourth powers | \(X=T^4\), \(J=T^2\), \(a\ge1\) | Test possible exact integer contacts | \(d_a,\Lambda_a,\ell_a,u_a\) are irrational; reciprocal endpoints are not integers | Fourth powers remove exact reciprocal endpoint equality, not near-endpoint sensitivity or mask uncertainty |
| Empty fibres | \(I_a=\varnothing\), an empty odd lift set, or deletion by any retained mask | Zero extension should annihilate the row | The exact criterion for \(I_a=\varnothing\) is \(\lceil u_a\rceil\le\lfloor\ell_a\rfloor+1\); the other deletion rules are unspecified | No uniform positive lower bound follows; upper counts must retain the \(+1\) and all masks |
| Moving reciprocal endpoints | Vary \(a\) or \(J\) in the exact formulas for \(\ell_a,u_a\) | A frozen dyadic interval may miss one-entry jumps | Endpoint contact occurs at the two displayed algebraic values of \(J\), and \(\lvert I_a\rvert\) changes discontinuously there | Replacing the moving interval by a common \(K\)-box needs an explicit endpoint discrepancy estimate |
| Physical saddle entry/exit | The packet's retained physical entry and exit predicates | Reciprocal membership need not be sufficient for physical contribution | No predicate is provided, so this test cannot decide whether a candidate \((a,k,g)\) enters or exits | A literal upper or lower result must expose and audit the physical mask before forming \(\Omega_a\) |
| Support and degeneracy | Odd lifts, primitive/owner masks, profiles, floors, stars, repeated denominators, and boundary lifts | Deleted and degenerate branches must be identified before counting | Oddness excludes \(g=0\), but all other predicates and any \(uv=0\) variables are absent | No degeneracy mass or lift-boundary claim is available from this packet |
| Known lower-bound families | UNC, TS, and W-1 named in the control file | Parity, dyadic support, coefficient envelopes, and raw/weighted status must be audited | Their definitions are not in the permitted statement-only material, so the audit cannot be run | No compatibility or contradiction with those families is claimed |
| Dyadic \(D\)-endpoints | \(D=X^{1/4},X^{3/8},X^{1/2}\) | An estimate below an endpoint must not cross it silently | The variable \(D\) and its relation to \(F_a(1)\) are absent from the packet | This report makes no endpoint continuation in \(D\) |

## 6. Dependencies and exact artifacts used

Statement-only isolation was maintained.  I read exactly these supplied artifacts:

- `problems/gauss_circle.md`;
- `state/control_models.md`;
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/blind_statement.md`;
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/briefs/blind_q1_diagonal_rederivation.md`.

I did not read the proof graph, the proof draft, any Round-103 claimant or reviewer report, or any Round-77--102 derivation.  I used no web source, external theorem lookup, or numerical experiment.  The Pell and endpoint checks above are exact algebra.  The only written artifact is this assigned report.  A post-write hygiene check verifies seven numbered top-level protocol sections and no additional numbered section.

## 7. Recommended state effect

**Retain** the exact singleton normalization, reciprocal interval formulas, Pell/fourth-power controls, and statement-level no-go as diagnostic evidence.  Make **no change** to the accepted proof state and do not promote the target: the actual coefficient formula and the first weighted or signed inequality remain missing.  No conclusion about the longer-row Gram, M9-M2, M9, or a Gauss-circle exponent is drawn.

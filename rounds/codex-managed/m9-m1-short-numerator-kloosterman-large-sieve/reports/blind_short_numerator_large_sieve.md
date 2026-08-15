## Result

**Rigorous no-go from packet underdetermination.**  The packet determines the odd-modulus phase and the conductor range, but it does not determine the coefficient
\(\alpha_{c,b}(\rho,\sigma;X)\), its \((\rho,\sigma)\)-support or decay, its stationary/nonstationary decomposition, the hidden endpoint in \(b\ll c/T\), either even-modulus phase, or the axial local factors.  Consequently it is impossible from the permitted data to produce the requested *exact finite* dyadic normalization, or to prove or disprove an estimate for the actual delta-transform weights.  This obstruction occurs before the use of dispersion, reciprocity, or a large sieve.

There is nevertheless a maximal formal normalization for the specified odd-modulus part.  If \(\eta\in\{+1,-1\}\) records the orientation and \(C,B,R,S\) are dyadic, set
\[
 \begin{split}
 \mathscr S^{\mathrm{odd}}_{C,B,R,S,\eta}
 := {}&\sum_{\substack{c\asymp C\\c\ {\mathrm{odd}}}}
 \sum_{\substack{b\asymp B\\b\ll c/T\\(b,c)=1}}
 \sum_{\substack{|\rho|\asymp R,\ |\sigma|\asymp S\\ \sigma\ {\mathrm{odd}}}}
 \alpha^{\eta}_{c,b}(\rho,\sigma;X)
 e_c\!\left(-\eta bN+\lambda_c\rho\sigma\bar b\right),
 \\
 &\lambda_c=(c^2-1)/4 .
 \end{split} \tag{R71.1}
\]
Zero bins must be separate from nonzero dyadic bins.  In the odd class the \(\rho=0\) bin survives, the \(\sigma=0\) bin is absent because \(\sigma\) must be odd, and the double-zero bin vanishes.  Formula (R71.1) is only a formal partition of the displayed family: the packet gives no finite list of \(R,S\), no tail estimate, and no formula with which to split the actual weight.  The \(c\equiv2\pmod4\) and \(4\mid c\) terms cannot be written exactly because their “conductor-4 twisted analogues” are not supplied.

The phase alone cannot force the required saving.  Indeed, on any finite set of allowed odd indices, a coefficient array can cancel the displayed phase term by term and make the sum equal its absolute majorant.  This is not a proposed model for the actual delta weight; it is a logical control showing that no arbitrary-coefficient large-sieve conclusion follows from the phase, support, gcd, and parity information in the packet.  A proof for the actual family must use a quantitative formula or norm property of that family, which is absent here.

## Exact statement and hypotheses

The precise statement established here is the following packet-sufficiency proposition.

**Proposition.**  From the two permitted artifacts one can deduce all of the following, and no exact actual-weight estimate beyond them.

1. Writing \(C=X^\gamma\), one has \(3/10\leq\gamma\leq1/2\), and the longest numerator interval has
   \[
   A_C\asymp C/T=X^{\gamma-3/10},\qquad
   1\ll A_C\ll X^{1/5},\qquad
   \frac{A_C}{\sqrt C}=X^{\gamma/2-3/10}\leq X^{-1/20}.
   \tag{R71.2}
   \]
   Endpoint constants are suppressed because the packet uses \(\ll\) and \(\asymp\).

2. For odd \(c\), \(\lambda_c\) is an integer and a unit modulo \(c\):
   \[
   \lambda_c\equiv-\overline4\pmod c,
   \qquad (\lambda_c,c)=1,
   \qquad (\lambda_c\rho\sigma,c)=(\rho\sigma,c).
   \tag{R71.3}
   \]

3. A dyadic decomposition in \(c\) and nonzero \(b\) is finite, with \(T\leq C\leq J\) and \(B\ll C/T\).  A dyadic decomposition in \(\rho,\sigma\) is only formal/countable unless a finite support or a quantitative truncation lemma is added.  Thus (R71.1), together with separate zero bins, is the strongest normalization justified by the packet.

4. Let \(\mathcal I_X\) denote the finite set of blocks that would result after the missing support, local, and stationary data were supplied, and let \(E_{\mathrm{tail}}\) be the rigorously bounded truncation error.  The weakest literal joint estimate is
   \[
   \left|\sum_{\nu\in\mathcal I_X}\mathscr S_\nu+E_{\mathrm{tail}}\right|
   \ll_\varepsilon J^{1/2}X^\varepsilon.
   \tag{R71.4}
   \]
   The weakest cancellation-free dyadic estimate is
   \[
   \sum_{\nu\in\mathcal I_X}|\mathscr S_\nu|+|E_{\mathrm{tail}}|
   \ll_\varepsilon J^{1/2}X^\varepsilon.
   \tag{R71.5}
   \]
   No uniform bound for an individual \((C,B,R,S)\)-block is necessary; (R71.5) is the minimally sufficient summable form.  Since the frozen absolute capacity is \(T X^\varepsilon\), (R71.4) or (R71.5) must realize, after every block and local term is aggregated,
   \[
   \frac{J^{1/2}}{T}=X^{-1/20},
   \quad\text{equivalently a gain }\frac{T}{J^{1/2}}=X^{1/20}.
   \tag{R71.6}
   \]

To turn the formal proposition into the requested theorem, the hypotheses must additionally specify: the exact formula and normalization of \(\alpha\); the real-offset factor and exact Farey/delta integral with orientation; the one-sided ratio symbol and cutoffs; the Poisson and local \(c\)-factors; effective \(\rho,\sigma\) ranges and tail bounds; the stationary/nonstationary partition; both even-modulus residues; every axial formula; and all gcd/parity restrictions.  None of these may be replaced by arbitrary coefficients.

## Proof or derivation

At the natural delta order \(Q=X^{1/5}\), a nonzero reduced rational with denominator at most \(Q\) is at distance at least \(Q^{-1}=X^{-1/5}\) from an integer, whereas Poisson localizes at distance \(T^{-1}=X^{-3/10}\).  Since \(Q^{-1}>T^{-1}\), only the zero cell can occur.  This reproduces the stated Fourier self-return and supplies no cancellation.  At conductor order, \(c\leq J=X^{1/2}<T^2=X^{3/5}\), whence
\[
 c/T<\sqrt c.
\]
More precisely, (R71.2) follows by substituting \(C=X^\gamma\); at the worst endpoint \(C=J\), \(A_C/\sqrt C=X^{-1/20}\).  Thus termwise completion replaces a numerator sum of trivial length at most \(C/T\) by a square-root-conductor bound which is worse by at least \(X^{1/20}\), exactly the gain demanded by the global benchmark.

For completeness, fix odd \(c\), \(k=\lambda_c\rho\sigma\), and absorb the actual \(b\)-weight and a proposed \(B\)-cutoff into a function \(w\) on residues modulo \(c\), extended by zero off the allowed numerator interval.  Finite Fourier inversion gives the exact identity
\[
 \sum_{b\bmod c}^{*}w(b)e_c(k\bar b\mp Nb)
 =\frac1c\sum_{h\bmod c}\widehat w(h)
 S(k,h\mp N;c),
 \tag{R71.7}
\]
where
\[
 \widehat w(h)=\sum_{x\bmod c}w(x)e_c(-hx),
 \qquad
 S(k,m;c)=\sum_{x\bmod c}^{*}e_c(k\bar x+mx).
\]
For a genuinely smooth weight varying only on scale \(B\), the natural completion-frequency length is \(H\asymp c/B\); at the longest scale \(B\asymp c/T\), this is \(H\asymp T\).  For shorter numerator blocks it is \(H\asymp c/B\geq T\).  This frequency cannot be discarded.  The packet, however, provides no derivative bounds on the actual \(w\), so even this concentration is conditional; (R71.7) itself is unconditional.

The complete-sum bound has the gcd ledger
\[
 |S(k,m;c)|\leq \tau(c)c^{1/2}(k,m,c)^{1/2}.
 \tag{R71.8}
\]
By (R71.3), the odd-class gcd in (R71.8) is \((\rho\sigma,h\mp N,c)\).  Neither the distribution of this gcd nor the size and location of \(N\) is specified.  In particular, a frequency \(h\equiv\pm N\pmod c\) makes the second Kloosterman argument zero and produces a Ramanujan degeneration; whether that frequency has appreciable actual weight is unknown.

The odd axial term \(\rho=0\) has \(k=0\).  After completion it is exactly a Ramanujan sum,
\[
 S(0,m;c)=r_c(m)=\sum_{d\mid(c,m)}d\,\mu(c/d),
 \qquad |r_c(m)|\leq \tau(c)(c,m).
 \tag{R71.9}
\]
It therefore requires separate treatment and may carry a full gcd.  The formal complete-sum double degeneration \(S(0,0;c)=\varphi(c)\) must not be reintroduced, because the original double-zero residue is stated to vanish.  For odd \(c\), \(\sigma=0\) is excluded by parity.  For \(4\mid c\), the packet says that the \(\sigma=0\) axis survives, but it gives no residue or weight with which to derive its Ramanujan factor.  The \(c\equiv2\pmod4\) axial ledger is likewise unspecified.

Reciprocity is exact but does not close the estimate.  For \((b,c)=1\),
\[
 e_c(k\bar b)=e\!\left(\frac{k}{bc}\right)e_b(-k\bar c).
 \tag{R71.10}
\]
When both \(b\) and \(c\) are odd, (R71.3) further gives
\[
 \lambda_c\bar c\equiv\overline4(c-\bar c)\pmod b,
\]
so the complete phase becomes
\[
 e\!\left(\frac{\lambda_c\rho\sigma}{bc}\mp\frac{bN}{c}\right)
 e_b\!\left(-\overline4\rho\sigma(c-\bar c)\right).
 \tag{R71.11}
\]
This exposes a potential average over \(c\) with short modulus \(b\), but it also leaves a moving inverse phase, an archimedean factor, and the full actual \(c,b,\rho,\sigma\)-dependent coefficient.  If \(b\) is even, \(4\) is not invertible modulo \(b\); a conductor-\(4\) lift is mandatory.  The missing local data prevent an exact even-\(b\) formula and prevent hypothesis matching to any bilinear or large-sieve estimate.

Finally, dispersion cannot be certified from the displayed phase.  On squaring, the coincident-index terms are nonnegative and contain the actual diagonal norm (at minimum terms of the form \(\sum|\alpha_{c,b}(\rho,\sigma;X)|^2\), with the precise multiplicity depending on which variables are dispersed).  The packet supplies no such norm and no relation between it and the absolute capacity.  Moreover, the phase-only coefficient class admits resonant arrays: multiplying a nonnegative finitely supported array by the inverse of the phase in (71.1) makes every summand have the same argument.  Hence a large-sieve estimate giving an \(X^{1/20}\) gain for all coefficients with only the displayed support and parity is false.  This establishes the claimed logical no-go without asserting anything false about the unspecified actual weight.

## First doubtful or unproved step

The first unavailable step is not an analytic inequality; it is the definition of the family to which an inequality would be applied.  The packet names properties that \(\alpha\) must retain but never gives \(\alpha\), its normalization, its support/decay, or the even and axial summands.  Therefore one cannot justify a finite \((R,S)\)-partition, bound a discarded tail, determine the Fourier concentration of \(\widehat w\), evaluate the dispersion diagonal, or match a reciprocity/large-sieve theorem to the actual coefficients.  Any claimed saving after this point would necessarily invent a missing weight property.  Formulae (R71.7) and (R71.10) are exact algebraic identities, but the first estimate needed after either identity is unproved from the permitted hypotheses.

## Required control test and outcome

| Control | Test | Outcome |
|---|---|---|
| Natural versus conductor delta scale | Compare \(Q^{-1}\) with \(T^{-1}\), then use \(T\leq c\leq J\). | **Pass.** Order \(Q\) has only the zero-cell self-return; nonzero cells require conductor order. |
| Short numerator | Check \(A_c=c/T<\sqrt c\) from \(c<T^2\). | **Pass.** At \(c\asymp J\), completion loses exactly \(X^{1/20}\) relative to trivial numerator length; it loses more below that endpoint. |
| Actual rather than arbitrary weights | Locate an exact formula, derivative bounds, support, and norm for \(\alpha\). | **Fail/underdetermined.** None is supplied.  The resonant-array test rules out a phase-only arbitrary-coefficient conclusion but says nothing adverse about the actual transform. |
| Local factors and orientation | Recover \(\vartheta\), delta/Farey integral, ratio symbol, cutoffs, Poisson factor, local \(c\), and both orientations. | **Fail/underdetermined.** These are requirements in prose, not formulae in the packet. |
| Zero and axial modes | Apply the stated parity and residue information before completion. | **Partial pass.** Double zero vanishes; odd \(\rho=0\) survives and gives (R71.9); odd \(\sigma=0\) vanishes.  The surviving \(4\mid c\), \(\sigma=0\) axis and the \(c\equiv2\pmod4\) axes cannot be normalized. |
| gcd ledger | Reduce \((\lambda_c\rho\sigma,c)\) and inspect degenerate complete sums. | **Pass for odd \(c\).** It equals \((\rho\sigma,c)\); (R71.8) and (R71.9) show the missing gcd averages.  **Unavailable for even classes.** |
| Parity/conductor \(4\) | Keep \(\sigma\) odd for odd \(c\), and test reciprocity for even \(b\) and even \(c\). | **Partial pass.** Odd parity is explicit.  Even \(b\) already forces a conductor-\(4\) lift in (R71.11); the two even-\(c\) formulae are absent. |
| Completion frequencies | Fourier-complete a \(B\)-scale numerator only after retaining \(h\). | **Pass algebraically.** Identity (R71.7) is exact; smooth-scale support would be \(h\ll c/B\), equal to \(T\) at maximal \(B\), but actual frequency decay is unproved. |
| Dispersion diagonal | Isolate coincident indices before estimating off-diagonal terms. | **Fail/underdetermined.** Its actual \(L^2\) mass and multiplicities cannot be computed from the packet. |
| Exact power requirement | Compute \(T/J^{1/2}\). | **Pass.** It is exactly \(X^{1/20}\).  No argument in the packet achieves that gain after full aggregation. |
| Squares/fourth powers | Test whether they furnish a target-sized lower bound. | **No obstruction certified.** The packet declares them subtarget and supplies no contrary quantitative data; they are not used as a counterexample. |
| Scope | Check for cone-edge, full \(M9\)-\(M1\), or final-exponent inference. | **Pass.** None is made. |

## Dependencies and exact artifacts used, including an isolation ledger

The derivation used exactly these two artifacts:

1. `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/briefs/blind_short_numerator_large_sieve.md`.
2. `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/derivation_packet.md`.

Isolation ledger: no graph file, state file, proof draft, prior-round report, sibling brief, sibling report, synthesis, validation artifact, source, bibliography, or web page was read.  No external theorem was invoked beyond the elementary finite Fourier inversion, reciprocity identity, standard displayed Kloosterman/Ramanujan identities explicitly derived or stated in this report, and no numerical experiment was run.  The only written artifact is this assigned report.

## Recommended state effect

**Retain** this report as a rigorous packet-sufficiency no-go and barrier audit.  Do not promote a short-numerator large-sieve estimate and make no change to the accepted proof graph.  A future attempt should first revise the input by supplying the exact actual-weight formula, finite truncation with error, both even local residues, and every axial factor; only then can dispersion or reciprocity be tested against (R71.4)–(R71.6).

**Post-isolation seam addendum — audit of conductor_farey_stationary_low_conductor.md.**  **Verdict: revise before promotion of the claimed exact all-class normalization; retain the low-conductor power calculation as conditional candidate evidence.**  The three-dimensional scaling itself is correct.  With \(\Lambda=J/c\) and \(\tau=\Lambda t\), the measure contributes \(\Lambda\), ordinary three-variable stationary phase contributes \(\Lambda^{-3/2}\), and hence the integral is \(O(\Lambda^{-1/2}(\rho\sigma)^{-1/4})\) in the odd class.  Combining this with the exact odd prefactor \(T(2ic)/(c\cdot4c)=iT/(2c)\), \(O(C)\) moduli, and \(O(C/T)\) numerators gives \(C^{3/2}/\sqrt J\).  Thus the asserted threshold is algebraically exact:
\[
 \frac{C^{3/2}}{\sqrt J}\leq \sqrt J
 \quad\Longleftrightarrow\quad
 C\leq J^{2/3}.
\]

The sharp Farey endpoints in (71.C5) are correct, but they are not retained in the subsequent “exact stationary normalization.”  In normalized variables the actual interval is
\[
 -\frac{J}{c+c_-}\leq t<
 \frac{J}{c+c_+}.
\]
Consequently a saddle entering or leaving a cell carries a neighbor-dependent incomplete-Fresnel transition factor, with scaled boundary distance of the form \(\Lambda^{1/2}(t_\pm-t_*)\).  Its uniform \(O(\Lambda^{-1/2})\) bound supports the absolute estimate, but it cannot be replaced by an unspecified fixed symbol in an exact promoted coefficient.  The displayed exact block (71.C8) also omits the announced \(V_C(c)\), and it does not display the offset-Poisson alias before unfolding.  Under its compact-support hypothesis there are only the two endpoint aliases (\(\ell=0\) and \(\ell=-1\), separated by orientation, for large \(T\)); writing that unfolding and its real-center phase is required for an exact seam.

The stationary residue-dual family is indeed finite: for odd \(c\), the positive saddle must satisfy
\[
 t_*=\frac12\sqrt{\rho\sigma}<
 \frac{J}{c+c_+}<1,
\]
with the analogous signed endpoint conditions in the other orientations and local classes.  However, the report does not prove the claimed *summed* rapid tail for all remaining \((\rho,\sigma)\).  A uniform integration-by-parts lemma must sum the nonstationary bulk, the boundary transition range, and both axes; merely noting absence of an interior critical point does not supply that tail estimate.

Finally, (71.C6) permits an exact even/axial audit that the report records only as \(O(c)\).  If \(s_0\equiv-\rho\bar a\pmod c\), then for \(c\equiv2\pmod4\),
\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =2c\,\chi_4(s_0)e_{2c}(\sigma s_0)
\]
when \(\rho,\sigma\) are odd, and it is zero otherwise.  For \(4\mid c\),
\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =c\,\chi_4(s_0)e_c(\sigma s_0)
\]
when \(\rho\) is odd, and it is zero otherwise.  Hence the normalized local prefactor is \(T/c\) in both even classes, versus \(iT/(2c)\) in the odd class.  The only axes are odd \(c,\rho=0,\sigma\) odd and \(4\mid c,\rho\) odd,\(\sigma=0\); \(c\equiv2\pmod4\) has no axis, and the double zero vanishes.  The even stationary constants also differ through \(J\sigma/[c,4]\), although their power bound is the same.  These explicit local formulae, the sharp transition symbol, and a summable dual-tail lemma are required before the all-class low-conductor result is promoted.

**Post-isolation second seam addendum — re-audit after repair.**  **PASS.**  The repaired conductor/Farey report now supplies (i) the exact periodized offset multiplier and its \(\ell=0,-1\) endpoint aliases, with \(V_C(c)\), \(N\), and \(\vartheta\) present in the coefficient-preserving Farey identity; (ii) the exact odd, \(c\equiv2\pmod4\), and \(4\mid c\) residues, normalized prefactors, parity conditions, and complete axial ledger; (iii) the sharp neighbor-dependent interval \(z\in[-J/(c+c_-),J/(c+c_+))\) and its incomplete-Gaussian transition symbol; and (iv) a summable large-dual and axial integration-by-parts estimate, with the remaining fixed family covered by ordinary or boundary stationary phase.  The scaling \(d\tau=\Lambda\,dz\) followed by three-dimensional stationary phase is \(\Lambda\Lambda^{-3/2}=\Lambda^{-1/2}\), so the per-incidence factor is \(T/\sqrt{cJ}\), the dyadic total is \(C^{3/2}/\sqrt J\), and target safety is exactly \(C\leq J^{2/3}\).  This PASS supersedes only the first post-isolation seam verdict; the original statement-only underdetermination verdict above is unchanged.

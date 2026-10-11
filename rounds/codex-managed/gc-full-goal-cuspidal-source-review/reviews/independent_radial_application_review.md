# Round229: independent review of the frozen radial control and conditional application

## 1. Result and review verdict

**GREEN for the scoped scalar conclusions and the algebra of the explicitly conditional application.** The Fourier and Abel constants, front expansion through its first correction, fixed-order differentiated error, complete interior estimate including zero, uniform lower bound, signed reconstruction, and compact-spectral nonintegrability proof are correct.

The conditional substitution in equation (8) is correct when the comparisons expressly stated in its paragraph are treated as input hypotheses. In particular, the asserted comparison \(X\asymp T\sqrt N\) remains an external input. Inferring it from the displayed scale of \(n\) alone would additionally require \(R\asymp T\); that radius comparison is not independently certified here. This restriction is part of the verdict's scope, not an arithmetic identification.

Reviewed artifact:

`rounds/codex-managed/gc-full-goal-cuspidal-source-review/controls/conductor_radial_abel_application.md`

Verified SHA256:

`55d912ff14d42d6085976d044c344fbb3efab90408649a9e35d38c8aba93f951`

Campaign: `gc-full-goal-cuspidal-source-review`. Round: 229. Role: independent nonauthor post-freeze scalar/application reviewer. Review date: 2026-09-29. Graph hash: not read and not certified.

## 2. Exact hypotheses, scope, and prior-isolation provenance

The scalar assumptions are the reviewed artifact's fixed nonnegative even \(G\in C_c^\infty((-1,1))\), \(\int G=1\), independent real \(U,L\ge2\), and precisely its displayed definitions of \(H,g,k\). The spectral comparison instead assumes even nonzero \(h\in C_c^\infty(\mathbb R)\) with the displayed inverse Fourier transform.

The arithmetic calculation is reviewed only as a conditional calculation with positive scale parameters and indices, the exact definition \(X=qdR^2/n\), \(U=TM/\sqrt N\), and the paragraph's asserted comparison \(X\asymp T\sqrt N\). I do not certify the cited phase formula, any arithmetic identity, the provenance or uniform constants of its scale comparisons, or any trace-formula premise.

Before this review, I independently derived the scalar packet under statement-only isolation, reading only `protocol.md` and `briefs/blind_radial_abel_statement.md` in this campaign. That report was frozen as:

`reports/blind_radial_abel_kernel.md`

SHA256:

`80b45100f6fb4c3443ac6c514248c2e90448694df668f527d7bc1d7e82792f6f`

That report has not been changed. Isolation ended only for this separately authorized review. The sole new file read was the exact conductor artifact named in Section 1; its hash was checked against the assignment. No cited conductor dependencies, graph, manifest, source, history, sibling artifact, or external material was opened. The conductor's statement that its artifact was frozen before receiving my blind results is recorded as provenance supplied by the assignment, rather than independently verified chronology. This review's only output is its assigned review file. No experiments were performed.

## 3. Independent checks and derivations

### Fourier convention and profile normalization

The changes of variables in the two bumps give exactly

\[
\widehat g(t)=e^{iLt}H(t/U)+e^{-iLt}H(t/U)=2\cos(Lt)H(t/U).
\]

For \(s\ge0\), the bump at \(-L\) cannot contribute because \(L-1/U\ge3/2\). Thus the claimed support consequence \(k(r)=0\) for \(r\ge L+1/U\) is correct. The negative interior need not vanish.

The reviewed artifact uses the **unnormalized** profile

\[
\Phi_c(a)=\int_0^\infty G'(a+v)v^{-1/2}\,dv.
\]

Its relation to the profile in my prior isolated report is

\[
\Phi_{\mathrm{blind}}(a)=-\frac{1}{\pi\sqrt2}\Phi_c(a).
\]

Consequently the positive sign in the conductor's equation (2) and the negative sign of the isolated report's interior profile are consistent; they reflect the displayed normalization, not a discrepancy.

### Front correction and all fixed differentiated errors

Put \(S=\sinh L\). An equivalent exact normalization of the conductor's front integral is

\[
k(L+a/U)=-\frac{U^{3/2}}{\pi\sqrt{2S}}
\int_0^\infty G'(a+v)v^{-1/2}Q(a,v,L,U)^{-1/2}\,dv,
\]

where

\[
Q=\int_0^1\frac{\sinh(L+(a+\theta v)/U)}{S}\,d\theta.
\]

The exact identity

\[
\frac{\sinh(L+z/U)}{S}=\cosh(z/U)+\coth L\sinh(z/U)
\]

gives

\[
Q=1+\frac{\coth L}{U}(a+v/2)+O_A(U^{-2}),
\]

and hence

\[
Q^{-1/2}=1-\frac{\coth L}{U}(a/2+v/4)+O_A(U^{-2}).
\]

For compact \(a\), the nonzero integrands have bounded \(v\). For sufficiently large \(U\) depending on that compact interval, \(Q\) stays uniformly positive and the relevant radii stay at least 1. Taylor remainder bounds remain uniform after any fixed numbers of \(a\)- and \(L\)-derivatives: all derivatives of \(\coth L\) are bounded for \(L\ge2\), all rescaled arguments lie in a fixed bounded interval, and positive powers of \(v\) are harmless. Differentiation of \(G'(a+v)\) leaves smooth compactly supported functions, and \(v^{-1/2}\) remains an integrable majorant at zero.

Integrating therefore gives exactly the reviewed equation (1):

\[
k(L+a/U)=-\frac{U^{3/2}}{\pi\sqrt{2S}}
\left[\Phi_c(a)-\frac{\coth L}{U}
\left(\frac a2\Phi_c(a)+\frac14\Psi_c(a)\right)
+O_A(U^{-2})\right],
\]

with \(\Psi_c(a)=\int_0^\infty G'(a+v)v^{1/2}\,dv\). The differentiated claim is correct for the error **inside this normalization**, as the artifact says. It is also valid for mixed fixed-order derivatives. Smooth support edges create no boundary term because the integration endpoint is fixed at zero and the translated smooth function is differentiated inside the integral.

For \(a<-1\), integration by parts gives

\[
\Phi_c(a)=\tfrac12\int G(y)(y-a)^{-3/2}\,dy>0.
\]

This proves nonvanishing for every permitted \(G\), with the stated \(|a|^{-3/2}\) tail. No pointwise nonvanishing at \(a=0\) is asserted or needed.

### Full interior, zero, and a bounded-parameter lower bound

On the entire interval \(0\le r\le L-2/U\), the support in positive \(s\) is separated from \(r\). Integration by parts gives exactly

\[
k(r)=-\frac1{2\pi\sqrt2}\int_0^\infty g(s)
\frac{\sinh s}{(\cosh s-\cosh r)^{3/2}}\,ds<0.
\]

The integral without displayed limits in the conductor's equation (3) is therefore the positive-half-line integral, as its immediately following statement \(\int_{s>0}g(s)\,ds=1\) confirms.

For \(\delta=L-r\ge2/U\), relevant \(s\) satisfy \(s-r\ge\delta/2\) and \(s\ge3/2\). The exact factorization

\[
\cosh s-\cosh r
=\tfrac12e^s(1-e^{-(s-r)})(1-e^{-(s+r)})
\]

proves the claimed lower bound \(c e^L\min(\delta,1)\), uniformly even at \(r=0\). Also \(\sinh s\asymp e^L\), so the conductor's estimate for \(|k(r)|\) follows from the positive mass 1 of the bump. Multiplication by \(\sinh r\le e^{L-\delta}/2\) and integration over \(\delta\in[2/U,L]\) yields its equation (4). This pays the complete inner disk, not just a near-front subset. At zero the defining integral is regular because the support is separated from zero; the integrated-by-parts expression is finite there as well.

The remaining front interval has length \(3/U\), \(r\ge1\), and \(\sinh r\asymp e^L\). The original square-root integral gives \(|k(r)|\le C_GU^{3/2}e^{-L/2}\), proving its stated upper contribution.

For the lower bound, use the conductor's \(r=L-\beta/U\), \(2\le\beta\le5/2\). Then \(r\ge3/4\), and for every point of the positive bump,

\[
1/U\le s-r\le(7/2)/U.
\]

Both \(\sinh r\) and \(\sinh s\) are uniformly comparable to \(e^L\). The mean-value theorem therefore gives \(\cosh s-\cosh r\asymp e^L/U\). Positivity of \(g\) in the last displayed kernel integral gives the claimed pointwise lower bound. Integrating over length \(1/(2U)\) proves the lower side of equation (5) uniformly for every \(U,L\ge2\), including bounded \(U\).

### Signed reconstruction

The inner integral is exactly

\[
\int_0^s\frac{\sinh r}{\sqrt{\cosh s-\cosh r}}\,dr
=2\sqrt{\cosh s-1}.
\]

This identity also proves absolute Fubini admissibility with \(|g'(s)|\), since the latter has compact support. The resulting coefficient is \(-2\sqrt2\), and \(\sqrt{\cosh s-1}=\sqrt2\sinh(s/2)\) for \(s\ge0\). Integration by parts therefore gives

\[
2\pi\int k(r)\sinh r\,dr
=2\int_0^\infty g(s)\cosh(s/2)\,ds
=2\cosh(L/2)H(i/(2U)).
\]

All constants and signs in equation (6) are correct. Because \(G\) is even, nonnegative, and normalized, \(H(i/(2U))=\int G(v)\cosh(v/(2U))\,dv\) is bounded above and below by positive constants. The signed mass is accordingly of order \(e^{L/2}\). This agrees exactly with \(\widehat g(i/2)\) and is distinct from the absolute mass of order \(\sqrt Ue^{L/2}\).

### Compact spectral cutoff obstruction

For even Schwartz \(g\), put \(F(x)=g(\operatorname{arcosh}x)\). Evenness makes \(F\) smooth at \(x=1\). The composition of the forward and inverse Abel expressions has an absolutely integrable majorant because

\[
\int_x^\infty|F'(y)|\,dy=\int_{\operatorname{arcosh}x}^\infty|g'(s)|\,ds<\infty
\]

and the intermediate beta integral is exactly \(\pi\). This verifies the coefficient \(\sqrt2\) in equation (7) and the legitimacy of its inversion argument. The bound \(|k(r)|\le C_N e^{-r/2}(1+r)^{-N}\) follows directly from

\[
\cosh(r+v)-\cosh r
=\tfrac12e^r(e^v-1)(1-e^{-2r-v}),\qquad r\ge1,
\]

and Schwartz bounds for \(g'\).

If \(k\) were absolutely integrable against \(\sinh r\,dr\), the bounded inner kernel stated in the artifact would imply \(\int_0^\infty|g(s)|e^{bs}\,ds<\infty\) for every \(0<b<1/2\). Its small-radius comparison and its large-radius substitution are both valid. Evenness then supplies exponential integrability on the full real line. The Fourier transform is holomorphic on each such strip and agrees with \(h\) on the real axis. Compact support of \(h\) gives a real open interval of zeros inside the strip, so holomorphic uniqueness contradicts nonzero \(h\). Thus the claimed nonintegrability follows, not merely the insufficiency of a particular upper bound.

The artifact correctly limits this conclusion to this absolute-integrability mechanism, without forbidding trace formulas or other convergence procedures.

### Conditional arithmetic substitution and retained nonimplications

With \(X=qdR^2/n>0\) and positive \(R\), the identity

\[
\sqrt U X^{1/2}=R\sqrt{qdU/n}
\]

is exact. From the stated inputs \(U=TM/\sqrt N\) and \(X\asymp T\sqrt N\),

\[
\sqrt U X^{1/2}\asymp
\sqrt{(TM/\sqrt N)(T\sqrt N)}=T\sqrt M.
\]

This is the correct conditional algebra in equation (8). Uniformity in that last comparison is conditional on uniform constants in the supplied scale comparisons.

For precision about the inputs, \(n\asymp qdT/\sqrt N\) by itself gives

\[
X\asymp R^2\sqrt N/T,
\]

not \(X\asymp T\sqrt N\) without an additional radius-scale identification. Equivalently, the latter asserted comparison incorporates \(R\asymp T\). This review treats the artifact's explicit \(X\)-comparison as an input and does not audit that external identification. Similarly, the assertion that \(L=\log X\ge2\) for the intended sufficiently large \(T\) remains subject to the intended scale regime; the scalar application applies whenever that domain condition and \(U\ge2\) actually hold.

The artifact explicitly retains all necessary nonimplications: its even cosine test is not identified with the moving complex multiplier; no paid decomposition is supplied; radial continuous \(L^1\) mass is not a fixed-point Hecke orbit bound; the full weighted sum, exceptional modes, oldspace factors, index tails, and complement remain outside the calculation. It does not turn a positive scalar absolute mass into an arithmetic lower bound or promote failure of this transfer into an all-method impossibility. These restrictions are appropriate and sufficient for the scoped verdict.

## 4. First doubtful or unproved step

No doubtful scalar step remains after the checks above. The large-\(U\) front expansion has the domain restriction stated by its author; the global mass estimate separately covers the full parameter range.

The first unaudited application input is the identification of the intended arithmetic phase and its scale regime, including the asserted \(X\asymp T\sqrt N\) comparison and \(U,L\ge2\). Even after those inputs are granted, a legal representation by admissible scalar tests with controlled coefficient norm is not supplied, and a uniform weighted fixed-CM orbit or spectral estimate would still be required. The reviewed artifact itself preserves both gaps. No external arithmetic or trace-formula premise is certified by this review.

## 5. Required controls and outcomes

1. **Exact normalization: PASS.** The Fourier transform, front prefactor, integration-by-parts coefficient, inverse Abel coefficient, and imaginary spectral evaluation agree independently. The two reports' profile sign difference is accounted for by their explicit normalization.
2. **Second-order remainder and differentiation: PASS.** The direct \(Q\)-expansion reproduces the \(a/2\) and \(1/4\) coefficients and proves a uniform \(O(U^{-2})\) normalized remainder after arbitrary fixed \(a\)- and \(L\)-derivatives on compact \(a\)-intervals.
3. **Nonzero profile and full interior: PASS.** Integration by parts proves strict nonvanishing in the interior tail. The \(\delta\)-integral covers every radius down to zero, and the explicit lower interval handles \(U=2\) as well as large \(U\).
4. **Signed versus absolute mass: PASS.** The exact signed expression has size \(e^{L/2}\), while the established full absolute mass has size \(\sqrt Ue^{L/2}\). No orbit-sum conclusion is drawn from either.
5. **Compact spectral false analogue: PASS as a proved no-go.** Abel inversion, exponential integrability, and holomorphic uniqueness provide a complete contradiction for nonzero even compact spectral \(h\).
6. **Conditional substitution and scope: PASS within stated inputs.** The algebra leading to \(T\sqrt M\) is correct when the asserted \(X\)-comparison is supplied. The additional \(R\asymp T\) content of that comparison is explicitly excluded from this review's independent certification, as are all arithmetic identifications and downstream estimates.

All controls were analytic. There were zero experiments and no numerical evidence was used.

## 6. Dependencies and exact artifacts used

Previously authorized isolation context, retained from the completed blind task:

- `protocol.md`.
- `rounds/codex-managed/gc-full-goal-cuspidal-source-review/briefs/blind_radial_abel_statement.md`.
- My own completed independent reasoning, frozen in the report with SHA256 `80b45100f6fb4c3443ac6c514248c2e90448694df668f527d7bc1d7e82792f6f`; that file was not reopened or edited in this review.

Sole added reviewed input:

- `rounds/codex-managed/gc-full-goal-cuspidal-source-review/controls/conductor_radial_abel_application.md`, SHA256 `55d912ff14d42d6085976d044c344fbb3efab90408649a9e35d38c8aba93f951`, verified from its bytes.

The conductor's cited external context and arithmetic dependencies were not inspected. No external sources were consulted. Only elementary analysis already used in the isolated task was required.

Output: `rounds/codex-managed/gc-full-goal-cuspidal-source-review/reviews/independent_radial_application_review.md`. Its final SHA256 is reported separately after writing.

## 7. Recommended state effect and stopping status

**Retain as independently reviewed scalar and explicitly conditional-application evidence; scoped review GREEN.** No bounded repair is required for that scope. The \(X\)-scale identification, its radius-scale content, and the domain of any actual application remain external premises requiring their appropriate owner; this review does not certify them.

No graph promotion, exponent change, complete-moment conclusion, wave conclusion, or arithmetic closure follows from this review. No shared state or prior frozen report was edited. The assigned review is complete; freeze its separately reported SHA256 and stop. No successor task or round is proposed or started.

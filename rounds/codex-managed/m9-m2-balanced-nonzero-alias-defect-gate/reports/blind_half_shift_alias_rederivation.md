# Blind half-shifted alias rederivation (Round 116)

## 1. Result

**Scoped no-go lemma, with the surviving kernel made explicit.**  The literal
change of variables and the two gcd expansions give an exact Poisson chart on
odd divisor progressions.  If (t=k'=k+q), then nonzero character support
forces

\[
h'=h+2s,qquad
\chi _4(h)\chi _4(h+2s)=(-1)^s=e(s/2).
\]

After expanding the second gcd mask by an odd divisor (d\mid t), the
half-shift is not the unweighted grid alone: it is

\[
\lambda\in \tfrac12+\mathbb Z,qquad
\nu=\lambda/d,qquad
\kappa_{d,h}(\lambda)
=e\!\left(\frac{r_d(h)}2-\frac{\lambda r_d(h)}d\right),
\tag{1.1}
\]

where (2r_d(h)\equiv-h\pmod d).  Positive stationary aliases have

\[
x=h'=\frac{Xt}{\nu^2},qquad
\Psi=R\sqrt{hk}-\frac{Xt}{2\nu}-\frac{h\nu}{2}.
\tag{1.2}
\]

The two literal gate images are

\[
\left|\frac{Xt^2}{\nu^2}-hk\right|>L,qquad
\left|ht-\frac{Xtk}{\nu^2}\right|>L.
\tag{1.3}
\]

For every fixed ((h,k,t,d)), there are (O(dR)=O(dL^3)) stationary
aliases and the stationary Jacobian is (O((dL)^{-1})).  Thus their
absolute capacity is (O(L^2)), whereas their square-energy capacity is
(O(L/d)), exactly the capacity of the (s\equiv r_d(h)\pmod d) physical
progression.  Globally, Poisson therefore preserves the stated (L^4)
energy capacity but raises a termwise alias (\ell^1) capacity to (L^5).
Each near-gate band deletes only (O(dL^2+1)) aliases, not the factor (L)
required from the retained double-far set.

This proves the following precise obstruction.  Neither of these classes
can prove the requested (L^3X^\varepsilon) estimate:

1. a literal gate-Poisson argument which takes termwise absolute values over
   aliases (its boundary Fourier tail is in general not even in
   (\ell^1), and its stationary bulk has capacity (L^5));
2. an argument which replaces the literal (q,lambda)-dependent symbol by
   arbitrary coefficients and uses only a reciprocal-(q) large-sieve or
   (\ell^2)-operator norm, followed by absolute outer summation.  On a
   divisor-(d) progression its unnormalised large-sieve constant is at
   least (M_d\asymp dL^3), by the diagonal, and after the stationary
   factor it is still at least (L/d).

The smallest surviving object is the **joint signed literal kernel** in
(3.14) below, including ((c,d)), the lift label ((d,\lambda)),
\(\kappa_{d,h}\), both copies of (A), both gate projectors, and the
boundary/nonstationary package.  No (L^3) inequality for that kernel is
proved here.  The obstruction is not a lower bound for
\(\mathcal R^{\mathrm{osc}}), and it does not assert that the requested
estimate is false.

## 2. Exact statement and hypotheses

Write (e(z)=e^{2\pi iz}), (t=k'=k+q), and

\[
G(u,v)=\eta\!\left(\frac{(u,v)}{\sqrt L/2}\right).
\]

All variables remain positive and in the single supplied physical block;
in particular (h,h',k,t\asymp L), since (K\asymp L).  The symbol is the
one fixed real symbol from the statement, extended by zero outside its
literal support, and its stated rescaled derivative bounds are retained.
The fixed cutoff (\eta) is used literally.  Capacity estimates below use
only its fixed boundedness; no sign or lower envelope for it is assumed.

Separate the exponential and phase-free terms by

\[
\mathcal R^{\mathrm{osc}}=\mathcal E-\mathcal P.
\tag{2.1}
\]

Here (\mathcal P) is exactly the already-owned phase-free double-far sum.
It is used once, through the supplied estimate
\(|\mathcal P|\ll_\varepsilon L^3X^\varepsilon).  The task therefore
reduces to a bound of that size for (\mathcal E); no second subtraction is
made.

For the exact gcd expansion, put

\[
f(n)=\eta\!\left(\frac n{\sqrt L/2}\right),qquad
\gamma(d)=\sum_{r\mid d}\mu(d/r)f(r).
\tag{2.2}
\]

Then, identically,

\[
G(u,v)=\sum_{d\mid u,\ d\mid v}\gamma(d).
\tag{2.3}
\]

Since (h) and (h') are odd on character support, only odd divisors
(c,d) occur.  If divisor absolute values are ever used, their displayed
cost is

\[
|\gamma(d)|\leq \|\eta\|_\infty\tau(d),qquad
\sum_{d\mid n}|\gamma(d)|\ll_\varepsilon n^\varepsilon;
\tag{2.4}
\]

the two gcd copies therefore cost at most (L^\varepsilon) each after a
harmless change of epsilon.  In the exact formulas they remain signed.

The no-go assertion is uniform only for the two stated proof classes.  The
large-sieve part concerns an alias interval on which the stationary
amplitudes are comparable and nonzero; equivalently it is a norm test on a
permissible flat interior subblock.  It is not asserted as a lower envelope
for the supplied literal symbol.

## 3. Proof or derivation

### Parity, shifts, and the two physical gates

Put (h'=h+p).  Both character factors vanish unless (h,h') are odd, so
(p=2s).  For every odd (h), including negative (s),

\[
\chi _4(h+2s)=(-1)^s\chi _4(h),
\]

which proves the character identity in Section 1.  The two determinants
become, exactly,

\[
\Delta=hq+2s(k+q)=hq+2st,qquad
\rho=hq-2sk.
\tag{3.1}
\]

Thus, with

\[
J_{hkt}(s)
=\mathbf 1_{|h(t-k)+2st|>L}
 \mathbf 1_{|h(t-k)-2sk|>L},
\tag{3.2}
\]

the exponential part is the literal identity

\[
\begin{split}
\mathcal E
=\sum_{\substack{h,k,t>0\\ h\ {\rm odd}}}\ \sum_{s\in\mathbb Z}
&e(s/2)G(h,k)G(h+2s,t)A(h,k)A(h+2s,t)J_{hkt}(s)\\
&\times e\!\left(R\sqrt{hk}-R\sqrt{t(h+2s)}\right),
\end{split}
\tag{3.3}
\]

where the literal supports make the sum finite and enforce (h+2s>0).
No (q=0), (s=0), repeated-divisor, or support-crossing branch has been
removed.

### Both gcd masks and exact progression Poisson

Insert (2.3) twice.  The first divisor satisfies (c\mid h,k).  The second
satisfies (d\mid t) and (d\mid h+2s).  For odd (d), choose any integer
(r_d(h)) with

\[
2r_d(h)\equiv-h\pmod d.
\tag{3.4}
\]

Then (s=r_d(h)+dn), and, because (d) is odd,

\[
e(s/2)=e(r_d(h)/2)e(n/2).
\tag{3.5}
\]

For a compactly supported piecewise smooth (F), Poisson summation on this
progression gives, with symmetric (or Cesaro) summation in the dual index,

\[
\begin{split}
\sum_{\substack{s\in\mathbb Z\\s\equiv r_d(h)\ (d)}}e(s/2)F(s)
=\frac1d\sum_{m\in\mathbb Z}
&e\!\left(\frac{r_d(h)}2-\frac{\lambda_m r_d(h)}d\right)\\
&\times\int_{\mathbb R}F(u)e(\nu_m u)\,du+\mathcal B_d(F),
\end{split}
\tag{3.6}
\]

where

\[
\lambda_m=\frac12-m,qquad \nu_m=\frac{\lambda_m}{d}.
\tag{3.7}
\]

The multiplier in (3.6) is independent of the representative chosen in
(3.4): replacing (r_d(h)) by (r_d(h)+d) changes its exponent by
(d/2-\lambda_m\in\mathbb Z).

The term (\mathcal B_d(F)) is essential for the strict gates.  More
explicitly, use the midpoint value

\[
J^\#(u)=\frac{J(u^-)+J(u^+)}2
\]

at a gate discontinuity in the Poisson integral.  The desired strict
integer value is restored by

\[
\mathcal B_d(F)
=\sum_{\substack{s\equiv r_d(h)\ (d)\\s\text{ a gate crossing}}}
e(s/2)F_0(s)
\left[J(s)-\frac{J(s^-)+J(s^+)}2\right],
\tag{3.8}
\]

where (F_0) denotes the continuous part of (F).  Each affine gate has
two crossings, so there are at most four candidate (s)'s for each
((h,k,t)).  Formula (3.8) also handles coincident crossings.  If the
divisor sums are recombined before taking an absolute value, their total
physical capacity is (O(L^3)).  Smooth literal support crossings stay in
(F_0); none is deleted.

Taking

\[
F(u)=A(h,k)A(h+2u,t)J_{hkt}(u)
e\!\left(R\sqrt{hk}-R\sqrt{t(h+2u)}\right)
\]

in (3.6), and retaining both divisor sums, is the exact half-shifted
Poisson identity for (\mathcal E).  In particular, reducing the rational
number (\nu=\lambda/d) and merging equal values would be unlawful:
different lifts ((d,\lambda)) carry different
\(\gamma(d)\kappa_{d,h}(\lambda)).

### Stationary chart and square completion

For a fixed alias set

\[
\phi_\nu(u)=R\sqrt{hk}-R\sqrt{t(h+2u)}+\nu u.
\]

Then

\[
\phi_\nu'(u)=\nu-R\sqrt{\frac{t}{h+2u}},qquad
\phi_\nu''(u)=\frac{R\sqrt t}{(h+2u)^{3/2}}>0.
\tag{3.9}
\]

There is a stationary point only for (\lambda>0), and it is

\[
x_\nu=h+2u_\nu=\frac{Xt}{\nu^2}.
\tag{3.10}
\]

At this point

\[
\phi_\nu(u_\nu)
=R\sqrt{hk}-\frac{Xt}{2\nu}-\frac{h\nu}{2}=\Psi(\nu),qquad
\phi_\nu''(u_\nu)=\frac{\nu^3}{Xt}.
\tag{3.11}
\]

Consequently an interior nondegenerate stationary contribution is

\[
\frac{e(1/8)}d
\sqrt{\frac{Xt}{\nu^3}}
A(h,k)A(x_\nu,t)J_{hkt}(u_\nu)e(\Psi(\nu)),
\tag{3.12}
\]

multiplied by (\gamma(c)\gamma(d)\kappa_{d,h}(\lambda)).  At a gate
endpoint, (3.12) is replaced by the corresponding incomplete Fresnel
factor; outside the stationary interval the exact integral in (3.6) is
kept as a nonstationary term.  Thus no endpoint has been silently assigned
the full (e(1/8)) factor.  Equivalently, define the stationary error for
each literal gate component (I) by the exact difference

\[
\mathcal E_{I,d,\lambda}
:=\frac{\kappa_{d,h}(\lambda)}d
\int_I A(h,k)A(h+2u,t)e(\phi_\nu(u))\,du
-\mathcal M_{I,d,\lambda},
\tag{3.13}
\]

where (\mathcal M_{I,d,\lambda}) is (3.12) only when the stationary point
is interior, and is the literal incomplete-Fresnel main term when it meets
an endpoint.  If there is no stationary point, set
\(\mathcal M_{I,d,\lambda}=0).  Formula (3.13), the nonstationary aliases,
and (3.8) are the retained alias-error package, not a discarded
(O(\cdot)).

The formal full interior kernel whose signed estimate would be needed is

\[
\begin{split}
\mathfrak K_{\rm joint}
=e(1/8)\sum_{\substack{h,k,t>0\\h\ {\rm odd}}}
\sum_{\substack{c\mid h,k\\c\ {\rm odd}}}
\sum_{\substack{d\mid t\\d\ {\rm odd}}}
&\gamma(c)\gamma(d)A(h,k)
\sum_{\substack{\lambda\in\frac12+\mathbb Z_{\ge0}\\
x_\nu\text{ in the literal support}}}
\frac{\kappa_{d,h}(\lambda)}d\sqrt{\frac{Xt}{\nu^3}}A(x_\nu,t)\\
&\times\mathbf 1_{|tx_\nu-hk|>L}
\mathbf 1_{|ht-kx_\nu|>L}e(\Psi(\nu)),qquad \nu=\lambda/d.
\end{split}
\tag{3.14}
\]

The exact transformed expression is (3.14) with the endpoint Fresnel
replacements plus the complete package (3.13), all nonstationary aliases,
and (3.8).  This is the candidate inequality that would close the round:

\[
\left|\mathfrak K_{\rm joint}
+\mathfrak K_{\rm endpoint}+\mathfrak E_{\rm sp}
+\mathfrak E_{\rm nonstat}+\mathfrak B_{\rm strict}\right|
\ \ll_\varepsilon L^3X^\varepsilon.
\tag{3.15}
\]

It is lawful because every sum remains signed and every literal piece is
present.  It is not proved.

For the square completion, set

\[
\nu_0=R\sqrt{k/h}.
\]

Since (Xk=h\nu_0^2) and (h\nu_0=R\sqrt{hk}), one obtains the exact
identity

\[
\Psi(\nu)
=-\frac{h(\nu-\nu_0)^2}{2\nu}-\frac{Xq}{2\nu}.
\tag{3.16}
\]

There is no omitted linear error term.

### Literal images of both gates

Substitution of (3.10) into the physical determinants gives

\[
\Delta_\nu=tx_\nu-hk=\frac{Xt^2}{\nu^2}-hk,qquad
\rho_\nu=ht-kx_\nu=ht-\frac{Xtk}{\nu^2},
\tag{3.17}
\]

which proves (1.3).  Their zero centres are

\[
\nu_\Delta=\frac{Rt}{\sqrt{hk}},qquad
\nu_\rho=R\sqrt{k/h}=\nu_0.
\tag{3.18}
\]

The deleted radial band is exactly

\[
\frac{Rt}{\sqrt{hk+L}}
\leq \nu\leq
\frac{Rt}{\sqrt{hk-L}},
\tag{3.19}
\]

and the deleted determinant band is exactly

\[
R\sqrt{\frac{k}{h+L/t}}
\leq \nu\leq
R\sqrt{\frac{k}{h-L/t}},
\tag{3.20}
\]

whenever the displayed denominators are positive, as they are for the
large-(L) block.  Each interval has length (\asymp L^2) if its centre
lies in the stationary support.  Since the (\nu)-grid has spacing (1/d),
each removes (O(dL^2+1)) aliases.  The exact dependence relation

\[
\Delta_\nu+\rho_\nu=q(h+x_\nu)
\tag{3.21}
\]

also shows that the two projectors may not be replaced by independent
averages.

### Alias capacity and the reciprocal-frequency obstruction

On block support, (\nu\asymp R\asymp L^3).  Hence

\[
\#\{\lambda:x_\nu\text{ is supported}\}=O(dR)=O(dL^3),
\qquad
\frac1d\sqrt{\frac{Xt}{\nu^3}}\asymp\frac1{dL}.
\tag{3.22}
\]

If the physical support has a fixed-width nonzero interior, the first
quantity is (\asymp dL^3); the two near-gate deletions are lower order.
For a fixed ((h,k,t,d)), therefore,

\[
\sum_\lambda |\text{stationary amplitude}|\asymp L^2,
\qquad
\sum_\lambda |\text{stationary amplitude}|^2\asymp \frac Ld.
\tag{3.23}
\]

The second relation matches the (L/d) points in the physical
(s\)-progression.  With (L^2) choices of ((h,k)) and (L/d) choices of
(t\equiv0\pmod d), a fixed divisor shell has

\[
\text{alias }\ell^1\text{ capacity }\asymp \frac{L^5}{d},qquad
\text{alias square-energy capacity }\asymp\frac{L^4}{d^2}.
\tag{3.24}
\]

The (d=1) scale records the advertised (L^5) versus (L^4).  Divisor
summation changes these only by (X^\varepsilon) when (2.4) is explicitly
used.  Thus Poisson is an energy-preserving identity, not the missing
factor (L).

There is also a literal sharp-boundary obstruction to aliaswise absolute
values.  Integration by parts at a gate endpoint (u_*) gives, for large
\(|\lambda|),

\[
\frac1d\int_I W(u)e(\phi_\nu(u))\,du
=\frac{C_*e(\nu u_*)}{\lambda}+O(|\lambda|^{-2})
\tag{3.25}
\]

with a nonzero (C_*) whenever the endpoint trace of the literal weight is
nonzero.  A single nonzero jump already makes the sum of absolute values
diverge like (\sum |\lambda|^{-1}).  Multiple endpoints must be summed as
their signed Fourier series; uniform cancellation cannot be inferred from
derivative bounds.  This proves the first no-go class without using a
stationary approximation.

For the reciprocal (q)-frequency, the condition (d\mid t) gives
(t=dn) and (q=dn-k).  The last term of (3.16) is

\[
e\!\left(-\frac{Xq}{2\nu}\right)
=e\!\left(\frac{dXk}{2\lambda}\right)
 e\!\left(-n\,\frac{d^2X}{2\lambda}\right).
\tag{3.26}
\]

Thus the reciprocal frequency is

\[
\theta_{d,\lambda}=\frac{d^2X}{2\lambda}\pmod1.
\tag{3.27}
\]

Let (M_d\asymp dL^3) be a common interior alias set and
(Q_d\asymp L/d) a (q)-progression length.  Partitioning the unit circle
into (4Q_d) equal arcs proves, without an equidistribution assumption,
that the number of ordered pairs with

\[
\|\theta_{d,\lambda}-\theta_{d,\lambda'}\|_{\mathbb R/\mathbb Z}
\leq(4Q_d)^{-1}
\]

is at least

\[
\frac{M_d^2}{4Q_d}-M_d\gg d^3L^5.
\tag{3.28}
\]

Hence these frequencies are not (Q_d^{-1})-spaced.  More decisively, if

\[
\sum_{\lambda\in\Lambda_d}
\left|\sum_{n\in\mathcal Q_d}u_n e(-n\theta_{d,\lambda})\right|^2
\leq C_d\sum_n|u_n|^2
\tag{3.29}
\]

holds for all coefficients, then (C_d\geq M_d).  Indeed, average the two
sides over independent mean-zero unit random phases (u_n): the expected
left side is (M_dQ_d), while the expected right norm is (Q_d).
After inserting the stationary amplitude (1/(dL)), the operator-square
constant is still at least

\[
\frac{M_d}{d^2L^2}\asymp\frac Ld.
\tag{3.30}
\]

This is the unavoidable diagonal cost.  A coefficient-adversary gives the
even simpler linear obstruction: assigning to each ((n,\lambda)) the
opposite phase in (3.26) makes every reciprocal phase align.  Therefore no
estimate uniform over arbitrary coefficients of the same magnitude can
replace the required signed literal estimate (3.15).

## 4. First doubtful or unproved step

The first unproved mathematical step is precisely (3.15): a **joint**
estimate for the signed lifted kernel after summing (h,k,t,c,d,\lambda)
together, including the (q)-dependence of (A(x_\nu,t)), the two gate
projectors, the character (\kappa_{d,h}(\lambda)), and the endpoint and
nonstationary packages.

It cannot be replaced by any of the following without new input:

\[
\sum_\lambda |\text{alias term}|,
\qquad
\left(\sum_\lambda|\cdot|^2\right)^{1/2}
\text{ followed by absolute outer sums},
\qquad
\text{a }q\text{-large sieve uniform in arbitrary amplitudes}.
\]

Equations (3.23)--(3.30) give the complete polynomial cost of those norm
steps.  In particular, the strict gates leave almost all stationary
aliases, and the reciprocal frequency has both a large diagonal and at
least the collision count (3.28).  A successful continuation would have
to identify cancellation in the actual coupled phase

\[
\kappa_{d,h}(\lambda)
e\!\left(-\frac{h(\nu-\nu_0)^2}{2\nu}
-\frac{Xq}{2\nu}\right)
\]

with the literal two-variable symbol and gates still attached.  No such
theorem is supplied or derived here.

## 5. Required controls and outcomes

For each control, the four entries are the exact input, the expected
failure or invariant, the observed result, and the implication.

| Required task control | Exact input | Expected failure or invariant | Observed result | Implication |
|---|---|---|---|---|
| `literal_half_shift_poisson_legality` | (3.3), with strict (J) | Exact parity, progression, and a legal summation convention | (3.6) is exact only with symmetric/Cesaro alias summation and the strict-value correction (3.8) | Aliaswise absolute summation is not a legal replacement |
| `gcd_expansion_and_character_progressions` | Both copies of (G) | Keep (c,d), congruences, and character phases | (2.2)--(3.7) give odd (c,d), (s=r_d+dn), and (\kappa_{d,h}); the displayed optional divisor cost is (X^\varepsilon) | The (d=1) chart alone is not the literal chart |
| `stationary_alias_range_and_amplitude` | (x=Xt/\nu^2), (\nu=\lambda/d) | Count every alias and the Jacobian | (M_d\asymp dL^3), amplitude (\asymp(dL)^{-1}) on an interior subblock | Per-fibre (\ell^1=L^2), energy (=L/d) |
| `dual_phase_square_completion` | (3.11), (t=k+q) | No dropped linear or constant term | Exact identity (3.16) | The reciprocal (q)-phase is (-Xq/(2\nu)) and the defect centre is (\nu_0) |
| `radial_and_determinant_gate_images` | Both strict gates in (3.1) | Transform both, without independence | (3.17)--(3.21); each deleted band has (O(dL^2)) aliases and (\Delta+\rho=q(h+x)) | The retained far set still has order (dL^3) aliases |
| `reciprocal_q_frequency_resonance_count` | (t=dn), (3.26) | Audit spacing modulo one | Frequency (3.27) has at least (\gg d^3L^5) close ordered pairs on a common interior range | A separated-frequency large sieve is unavailable |
| `signed_alias_norm_without_l1` | Exact BV gate transform | Preserve the signed Fourier series | Boundary tails are (C_*/\lambda+O(\lambda^{-2})); stationary (\ell^1) is globally (L^5) | The alias sum must remain signed |
| `large_sieve_spacing_and_diagonal_cost` | Matrix in (3.29) | Include the diagonal before claiming gain | (C_d\ge M_d\asymp dL^3), or (L/d) after stationary normalization | A (q)-only norm argument cannot close (3.15) |
| `boundary_and_nonstationary_errors` | Four possible affine gate crossings and all aliases without an interior station | Keep midpoint correction, incomplete Fresnel factors, and tails | (3.8), (3.13), and the nonstationary part are retained exactly; the physical strict-value correction has (O(L^3)) capacity, while its aliaswise (\ell^1) version can diverge | Boundary pieces must be grouped signed or returned to the physical side |
| `actual_symbol_vs_arbitrary_coefficients` | Real literal (A(h,k)A(x,t)) versus same-size arrays | A uniform coefficient claim must survive adversarial phases | Adversarial ((q,\lambda))-phases align (3.26); no such uniform (L^3) claim survives | Any positive proof must use the actual symbol and arithmetic coupling |
| `fixed_block_and_owner_scope` | One physical block and the supplied owner for (\mathcal P) | No block summation and no double subtraction | Only (2.1) is used, once | Result is single-block and does not alter the phase-free owner |
| `critical_j1_and_exact_square_j2_boundary` | Supplied (X=R^2), (R\asymp L^3), persistent (j=1) | Do not extrapolate through an undefined boundary | Every scale in (3.22)--(3.30) uses (j=1) and exact (X=R^2); no (j=2) object is defined in permitted context | No (j=2) or boundary claim is made |
| `linear_vs_energy_capacity` | Physical (L^4) atoms and transformed amplitudes | A transform must not be called a saving | (3.24) gives global energy (L^4), alias (\ell^1=L^5), target (L^3) | A genuinely signed factor (L) beyond energy preservation is still missing |
| `downstream_scope` | The two scoped norm obstructions | Do not turn a method obstruction into a theorem about the remainder | No value or sign lower bound for (\mathcal R^{\mathrm{osc}}) was used | Park only the named proof classes, not the target statement |

The repository-wide controls from the permitted control file were also
applied as follows.

| Repository control | Exact input | Expected failure or invariant | Observed result | Implication |
|---|---|---|---|---|
| `raw-vs-weighted` | Counts in (3.22)--(3.24), literal (\gamma(c)\gamma(d)AA) | Do not transfer a raw exponent to a weighted mass | Both the raw atom count and stationary Jacobian/divisor costs are displayed; no (\beta)-weight occurs in the supplied problem | Capacities are diagnostics, not a weighted theorem |
| `signed-vs-unsigned` | (\kappa_{d,h}\), (\gamma(c)\gamma(d)), and the dual phase | True, absolute, random, and adversarial signs must differ | Absolute aliases cost (L^5) or diverge at boundaries; random signs certify nothing; adversarial phases align; true signs remain in (3.15) | Only a true-sign joint estimate could be promoted |
| `known-lower-bound-families` | Any proposed unsigned near-collision conclusion | Audit UNC, TS, and W-1 before a lower-bound claim | Those families are not defined in the permitted statement-only artifacts, and this report makes no near-collision or lower-bound claim | The control is non-executable here and blocks any such downstream claim |
| `dyadic-endpoints` | Supplied (L\asymp X^{1/6}), (K\asymp L) | Do not cross (X^{1/4},X^{3/8},X^{1/2}) silently | No dyadic parameter at those endpoints is varied; (\sqrt L/2) is a gcd cutoff, not that dyadic (D) | Report is confined to the stated critical block |
| `real-vs-complex-pairing` | Real (A), real (\chi_4), and the literal conjugate in (116.B1) | A real-part shortcut needs conjugacy | The product is reduced only through the exact real parity identity; no (\operatorname{Re}B_h) shortcut is used | No extension to asymmetric complex weights is claimed |
| `exact-vs-near-resonance` | Strict (>L) gates, gate equalities, and reciprocal near-collisions | Keep exact and near events separate | Exact gate equalities are isolated in (3.8); (3.28) is only a frequency-spacing obstruction, not a resonance lower bound | No exact-energy statement is transferred to the far sum |
| `coefficient-adversary` | Same magnitudes with arbitrary ((q,\lambda))-phases | A norm-only theorem must survive alignment | Alignment defeats the arbitrary-coefficient version | Fixed (\Phi/\chi_4)-type structure would have to enter a proof explicitly |
| `support-and-degeneracy` | Literal block support, (q=0), (s=0), gate crossings, divisor lifts | Retain endpoints, zero branches, repeats, and lift boundaries | Positive block support removes (hk=0), but (q=0), (s=0), repeated (\nu=\lambda/d), and all crossings remain in (3.3)--(3.14) | No degeneracy was silently discarded |

## 6. Dependencies and exact artifacts used

This report used completely and only the following artifacts:

1. `problems/gauss_circle.md`;
2. `state/control_models.md`;
3. `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/blind_statement.md`;
4. `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/briefs/blind_half_shift_alias_rederivation.md`.

No proof graph, strategy file, derivation packet, conductor candidate,
Round-114/115 artifact, sibling report, web source, or numerical experiment
was read or used.  The only externally owned mathematical input invoked is
the phase-free (O_\varepsilon(L^3X^\varepsilon)) estimate explicitly
stated in the blind problem.

## 7. Recommended state effect

**Revise.**  Do not promote (116.B2).  Park the aliaswise-absolute,
arbitrary-coefficient, and reciprocal-(q)-large-sieve-only versions of the
one-alias defect mechanism as quantitatively obstructed.  Retain
(3.14)--(3.15) as candidate evidence naming the smallest lawful survivor:
the full joint signed lifted kernel with literal endpoint and
nonstationary packages.  This recommendation changes no shared proof state
and makes no lower-bound claim for the actual remainder.

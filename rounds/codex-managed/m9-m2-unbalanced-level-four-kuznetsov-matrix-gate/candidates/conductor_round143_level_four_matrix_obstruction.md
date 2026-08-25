# Round 143 conductor candidate: exact character-to-level embedding and joint-matrix obstruction

Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`

Starting graph SHA-256:
`7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`

## 1. Result

Let

\[
S(a,b;n)=\sum_{x\bmod n}^{*}
e\!\left(\frac{a\bar x+bx}{n}\right).
\tag{143.C1}
\]

For \(\Gamma _0(4)\), primitive nebentypus \(\chi _4\), weight parity
\(\kappa=1\), cusps \((\infty,0)\), and scaling matrices

\[
\sigma _\infty=I,
\qquad
\sigma _0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\tag{143.C2}
\]

the allowed generalized moduli are exactly \(2n\), \(n\) odd, and the
fixed-modulus arithmetic identity is

\[
\boxed{
S^{\chi _4}_{\infty0}(4N_0,h;2n)
=\chi _4(n)S(N_0,h;n).}
\tag{143.C3}
\]

It holds for every integer \(h\) and every \((N_0,n)\), and has no
modulus-dependent root of unity in the convention below.  This is an
internally proved double-coset identity.  It must not be attributed to the
even-character theorem of Kıral--Young.

For the full gcd-restored inverse-first owner, (143.C3) gives

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{g,n\ \operatorname{odd}\\gn\asymp R}}
\chi _4(g)W\!\left(\frac{X}{gnD}\right)
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)
S^{\chi _4}_{\infty0}(4N_0,h;2n).
\tag{143.C4}
\]

The degenerate class \(h=0\) is \(O_\varepsilon(X^\varepsilon)\).
The smallest unresolved object is therefore the centered
\(h\ne0\) joint matrix in (143.C4), not the whole completed wave.

There is also a source-certified odd-character implementation.  The
Blomer--Milićević character identity expresses the ordinary geometric side
as a level-\(4\) minus level-\(8\) standard-cusp combination.  It supplies
a legal weight-one \(H+M+E\) spectral architecture, but only for fixed
Fourier arguments and one common smooth scalar modulus test.  The literal
coefficient \(\widehat\gamma_{g,n}(h)\) is instead a joint arithmetic
matrix in the modulus and second Kloosterman argument.  The frozen packet
proves neither a common sequence times a jointly smooth test nor a
Bessel-compatible low-projective-cost decomposition.

The automatic coefficient-blind closure available from row Parseval and
the complete Kloosterman second moment is

\[
|\mathscr R_{D,L}(X)|
\ll_\varepsilon R\sqrt\Delta\,X^\varepsilon
=\frac{X}{\sqrt{DL}}X^\varepsilon,
\tag{143.C5}
\]

which is worse than both branches of the accepted flat-wave envelope at
every point of the frozen polytope, with the precise strict margins recorded
below.  Expanding the joint coefficient
and summing all \(h\) returns the original reciprocal row exactly.
Consequently Round 143 closes, subject to the assigned seam reviews, under
`level_four_spectral_matrix_no_go`: the character-to-level algebra is
genuine progress, but the frozen coefficient controls do not satisfy the
common-test or common-sequence hypotheses of the audited scalar trace
formulas and large sieves with an owner-saving norm.  This is
a no-go from the frozen controls, not a lower bound for the signed scalar or
an impossibility theorem for a future vector-valued trace formula.

## 2. Exact owner and inverse-first identity

Write

\[
X\ge2,\qquad
X=N_0+\xi,\quad N_0=\lfloor X\rfloor,\quad 0\le\xi<1,
\tag{143.C6}
\]

\[
D=X^\delta,\quad L=X^\ell,\qquad
R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
\Delta=\frac RK=\frac DL,
\tag{143.C7}
\]

\[
\frac14\le\delta<\frac12,\qquad
0\le\ell<\delta-\frac14,\qquad
178\ell+1638\delta>463.
\tag{143.C7a}
\]

The frozen flat-smooth strict-UNBAL component is

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{r\asymp R\\r\ \operatorname{odd}}}
\chi _4(r)W\!\left(\frac{X}{rD}\right)
\sum_{k\asymp K}\frac{q_L(4Xk/r^2)}k e(Xk/r).
\tag{143.C8}
\]

Put \(r=gn\), \(k=gj\), \((j,n)=1\), and retain the literal support,
profiles, entries, exits, and real-centre factor in

\[
b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
\tag{143.C9}
\]

The literal support forces \(g\ll K\), and its inherited profile bounds are

\[
|b_{g,n}(j)|\ll_\varepsilon K^{-1}X^\varepsilon,\qquad
\sum_j|b_{g,n}(j)|\ll_\varepsilon g^{-1}X^\varepsilon,
\qquad
\sum_j|b_{g,n}(j)|^2\ll_\varepsilon(gK)^{-1}X^\varepsilon.
\tag{143.C9a}
\]

On \(\mathbb Z/n\mathbb Z\), define

\[
\gamma_{g,n}(m)=
\begin{cases}
b_{g,n}(\bar m_n),&(m,n)=1\text{ and }\bar m_n
\text{ lies in the literal support},\\
0,&(m,n)>1,
\end{cases}
\tag{143.C10}
\]

\[
\widehat\gamma_{g,n}(h)=\frac1n
\sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n).
\tag{143.C11}
\]

Fourier inversion and \(m=\bar j_n\) give, without assuming
\((N_0,n)=1\),

\[
\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
=\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n).
\tag{143.C12}
\]

Multiplying by \(\chi _4(g)\chi _4(n)\), summing all gcd strata, and using
(143.C3) proves (143.C4).  Centered representatives

\[
-\frac{n-1}{2}\le h\le\frac{n-1}{2}
\tag{143.C13}
\]

separate the two signs without changing the scalar.  At fixed \(g\), pad
every row by zero to one common \(|h|\ll R/g\) column set before taking
matrix norms.

## 3. Character-to-level algebra and the legal source route

Take

\[
\gamma_0=\begin{pmatrix}A&B\\4C&D\end{pmatrix}\in\Gamma_0(4),
\qquad AD-4BC=1.
\tag{143.C14}
\]

Then

\[
\gamma_0\sigma_0=
\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix}.
\tag{143.C15}
\]

A positive lower-left entry is \(2D=2n\) with \(n\) odd, and every
positive odd \(n\) occurs.  At fixed \(n\), the two translation
stabilizers reduce \(B\) modulo \(n\), while

\[
4BC\equiv-1\pmod n,
\qquad -C\equiv\bar4\,\bar B\pmod n.
\tag{143.C16}
\]

Put \(\Gamma_\infty^+=\langle T\rangle\), and define the fixed-modulus
translation double quotient

\[
\mathcal D_{\infty0}(c)=
\left\{[\rho]\in
\Gamma_\infty^+\backslash
\sigma_\infty^{-1}\Gamma_0(4)\sigma_0/\Gamma_\infty^+:
\rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}\right\}.
\tag{143.C17a}
\]

The generalized sum convention is

\[
S^{\chi _4}_{\infty0}(M,H;c)=
\sum_{[\rho]\in\mathcal D_{\infty0}(c)}
\overline{\chi _4}(D(\rho))
e\!\left(\frac{Ma+Hd}{c}\right),
\tag{143.C17}
\]

where \(D(\rho)\) is the lower-right entry of an underlying
\(\gamma_0\in\Gamma_0(4)\) with
\(\rho=\sigma_\infty^{-1}\gamma_0\sigma_0\).  Its character value is
invariant under both translation stabilizers.  A convention quotienting by
\(\{\pm T^j\}\) must fix the weight-one multiplier and cusp-\(0\) Fourier
phase simultaneously; this can alter one global convention unit, not an
\(n\)- or \(h\)-dependent factor.  Equations (143.C15)--(143.C16) yield

\[
S^{\chi _4}_{\infty0}(M,H;2n)
=\chi _4(n)S(M,H\bar4;n)
=\chi _4(n)S(\bar4M,H;n).
\tag{143.C18}
\]

Taking \(M=4N_0\) proves (143.C3).  The cusps \(\infty\) and \(0\) are
singular, while \(1/2\) is nonsingular because its normalized stabilizer
has lower-right entry \(3\pmod4\).  Compatibility with \(-I\) forces
\((-1)^\kappa=\chi _4(-1)=-1\), hence \(\kappa=1\).

The source boundary is essential.  Kıral--Young equation (2.20) has the
same arithmetic shape but lies under their even-character weight-zero
hypothesis, so it does not certify (143.C3) or a weight-one switched-cusp
trace formula.  The internally proposed pure-level-\(4\) spectral
inventory is therefore conditional until a convention-matched weight-one
formula, including both signs and scattering data, is derived.

Blomer--Milićević provide an independent legal route.  Let

\[
u=(N_0,4^\infty)=2^{v_2(N_0)},\qquad M_0=N_0/u.
\tag{143.C19}
\]

Use the standard twisted sum and primitive Gauss factor

\[
S_{\chi_4}(a,b;C)=
\sum_{d\bmod C}^{*}\chi_4(d)
e\!\left(\frac{ad+b\bar d}{C}\right),\qquad
\tau(\chi_4)=\sum_{a\bmod4}\chi_4(a)e(a/4)=2i.
\tag{143.C19a}
\]

For the same finitely supported weight \(\omega\) in both terms, their
character identity specializes to

\[
\begin{aligned}
&\sum_{\substack{n\ge1\\n\ \operatorname{odd}}}
\chi_4(n)S(N_0,h;n)\omega(n)\\
&\quad=\frac{\chi_4(M_0)}{\tau(\chi_4)}
\left\{
\sum_{\substack{C\ge1\\4\mid C}}
S_{\chi_4}(M_0,16uh;C)\omega(C/4)\right.\\
&\hspace{55mm}\left.
-
\sum_{\substack{C\ge1\\8\mid C}}
S_{\chi_4}(M_0,16uh;C)\omega(C/4)
\right\}.
\end{aligned}
\tag{143.C20}
\]

Thus the source-certified implementation is a standard-cusp level-\(4\)
minus level-\(8\) formula, not the conditional pure-level-\(4\)
cross-cusp spectral formula.  Its weight is \(\kappa=1\).  Its printed
spectral ledger is \(H+M+E\): odd holomorphic weights \(k\ge3\), the full
weight-one Maaß spectrum including exceptional parameters and any
\(t=0\) form, and Eisenstein integrals over every singular cusp.  Level
\(4\) has the two singular cusps \(\infty,0\) and no proper-level
oldspace for primitive conductor four; level \(8\) has four singular
cusps \(\infty,0,1/2,1/4\) and includes level-\(4\) oldclasses.  No
separate residual or holomorphic weight-one term is printed.

For one legal common same-sign test, the source transforms are

\[
\dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
\tag{143.C21}
\]

\[
\widetilde g(t)=\frac{it}{2\sinh(\pi t)}
\int_0^\infty\{J_{2it}(x)+J_{-2it}(x)\}g(x)\frac{dx}{x}.
\tag{143.C22}
\]

No exact odd-weight opposite-sign normalization is promoted in this
candidate.

## 4. Joint-matrix, Linnik-range, and self-return obstructions

On the literal support,

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
\ll\frac{X^\varepsilon}{RK},
\qquad
\sum_{\substack{n\asymp R/g\\h\bmod n}}
|\widehat\gamma_{g,n}(h)|^2
\ll\frac{X^\varepsilon}{gK}.
\tag{143.C23}
\]

For the zero-padded coefficient matrix

\[
A_g(n,h)=W\!\left(\frac{X}{gnD}\right)
\widehat\gamma_{g,n}(h),
\tag{143.C24}
\]

the automatic Schatten bounds are

\[
\|A_g\|_{S_2}^2\ll\frac{X^\varepsilon}{gK},
\qquad
\|A_g\|_{S_1}\ll\frac{\sqrt\Delta}{g}X^\varepsilon.
\tag{143.C25}
\]

For the conditional pure-level-\(4\) cross-cusp \(S/c\) normalization, put
\(B_g^{\mathrm{cross}}(n,h)=2nA_g(n,h)\).  For the source-certified
standard-cusp level-\(4/8\) route, the surviving modulus is \(C=4n\), so
the corresponding \(S/C\) sample is
\(B_g^{\mathrm{std}}(n,h)=4nA_g(n,h)\).  The fixed factor two does not
change the bounds

\[
\|B_g^{\mathrm{cross}}\|_{S_2}
+\|B_g^{\mathrm{std}}\|_{S_2}\ll
\frac{\sqrt{R\Delta}}{g^{3/2}}X^\varepsilon,
\qquad
\|B_g^{\mathrm{cross}}\|_{S_1}
+\|B_g^{\mathrm{std}}\|_{S_1}\ll
\frac{R\sqrt\Delta}{g^2}X^\varepsilon.
\tag{143.C26}
\]

These are upper bounds.  An abstract diagonal control shows that matrices
obeying only the same row Parseval information can saturate the nuclear
upper price.  It proves only that row Parseval alone cannot imply a smaller
uniform trace norm.  It gives no lower bound or rank statement for the
literal inverse-selector matrix and does not exclude a bespoke arithmetic
theorem.

For fixed \(g,h\), the conditional cross-cusp route would require one
controlled scalar test with samples

\[
2nW\!\left(\frac{X}{gnD}\right)
\widehat\gamma_{g,n}(h).
\tag{143.C27}
\]

The source-certified standard-cusp route requires the corresponding
\(4nW(X/(gnD))\widehat\gamma_{g,n}(h)\) samples, together with the fixed
Gauss factor and level-\(4\) minus level-\(8\) sign in (143.C20).  If one
uses the source's \(S/\sqrt C\) formulation instead, the equivalent
\(\sqrt C\)-weighted common test must satisfy its printed smoothness norm.

The inverse map \(\bar j_n\), unit condition, and support boundary all
move with \(n\).  Neither (143.C23) nor (143.C25) proves a common
coefficient sequence times a jointly smooth test.  Exact point-mass
interpolation is possible, but adjacent modulus samples are separated by
\(\asymp g/R\), so its derivative/Bessel bandwidth grows with the number
of samples.  Algebraic singular-value decomposition supplies no modulus
Sobolev control.  Deshouillers--Iwaniec's large sieve fixes a cusp of
\(\Gamma_0(q)\), assumes \(T\ge1\), \(N\ge1/2\),
\(\varepsilon>0\), and uses the same
sequence on \(N<n\le2N\) in its holomorphic, Maaß, and Eisenstein
quadratic forms; its exceptional theorem also assumes \(Y\ge1\).  Its
printed formula is not itself the required odd-nebentypus, weight-one,
level-\(4/8\) large sieve.  Assing--Blomer--Li assume positive
\(n,r,s\), \((r,s)=1\), \(M,C,Z\ge1\), one sequence \(\alpha_m\), and a
function \(F\) supported on \([M,2M]\times[C,2C]\) satisfying all their
mixed-derivative bounds and

\[
\frac{\sqrt{Mn}}{s\sqrt r\,C}\ll Z.
\tag{143.C27a}
\]

That theorem permits controlled smooth two-variable dependence, but
contains neither the \(\chi_4\) modulus twist nor the Blomer--Milićević
level-\(4/8\) encoding.  These observations identify a missing lemma, not
a universal decomposition impossibility.

Independently, at fixed \(g\) and modulus scale \(C_g=R/g\), the printed
Blomer--Milićević same-sign Linnik estimate fixes positive Fourier
arguments, one arithmetic weight, and one compactly supported smooth
archimedean test; its bound contains the normalized Mellin norm of that
fixed arithmetic weight.  Its printed range gives the comparison scale

\[
N_0h\ll C_g^2,
\qquad
0<h\ll H_{\rm Lin}(g),\qquad
H_{\rm Lin}(g)\asymp\frac{X}{D^2g^2}
=\frac{K}{Lg^2},
\tag{143.C28}
\]

whose continuous scale ratio is

\[
\frac{H_{\rm Lin}(g)}{C_g}\asymp\frac1{Dg}.
\tag{143.C29}
\]

The actual positive integer-frequency coverage satisfies only

\[
\frac{\#\{1\le h<n:h\ll H_{\rm Lin}(g)\}}{R/g}
\ll\frac1{Dg};
\tag{143.C29a}
\]

it is \(\asymp1/(Dg)\) only in the many-integer range
\(H_{\rm Lin}(g)\gg1\), with the dyadic constants fixed.
For \(g\gg\sqrt{K/L}\), with a sufficiently large fixed implied
constant, this range contains no nonzero integer.  Parseval does not
localize the matrix into (143.C28), and the source prints no
complementary-range uniform theorem.

Finally, substituting (143.C11) into (143.C12) and summing \(h\) first
gives

\[
\begin{aligned}
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
&=\sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(N_0\bar m/n)\\
&=\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n).
\end{aligned}
\tag{143.C30}
\]

This is the original reciprocal row exactly.  Smooth-weight-first
completion instead returns the already accepted Ramanujan/additive
capacity \(\Delta X^\varepsilon\).  Neither identity is a spectral gain.

## 5. Degenerate class and full-polytope capacity

At \(h=0\),

\[
S(N_0,0;n)=c_n(N_0),
\qquad
|\widehat\gamma_{g,n}(0)|\ll R^{-1}X^\varepsilon.
\tag{143.C31}
\]

Using \(|c_n(N_0)|\le(n,N_0)\) and
\(\sum_{n\asymp R/g}(n,N_0)\ll(R/g)X^\varepsilon\), the fixed-\(g\)
contribution is \(O_\varepsilon(g^{-1}X^\varepsilon)\), hence the full
zero class is \(O_\varepsilon(X^\varepsilon)\).

For every \((N_0,n)\), additive orthogonality gives the exact identity

\[
\sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n).
\tag{143.C32}
\]

Combining (143.C23) and (143.C32) costs
\(\sqrt\Delta/g\) on one row.  Summing the \(O(R/g)\) rows and then all
\(g\) proves (143.C5).

Let \(a=\delta-\ell\).  The accepted flat envelope is

\[
\min\left\{\Delta,\sqrt{KD}+\sqrt{R/L}\right\}X^\varepsilon,
\qquad
\beta(a)=\min\left\{a,\frac{1-a}{2}\right\},
\qquad \frac14<a<\frac12.
\tag{143.C33}
\]

The exponent of (143.C5) is

\[
p=1-\frac{\delta+\ell}{2}.
\tag{143.C34}
\]

At every point of the strict frozen polytope it is worse than both branches
by the displayed powers; no extra polytope-uniform margin beyond these
strict inequalities is claimed:

\[
p-a=1-\frac{3\delta}{2}+\frac\ell2>\frac14,
\qquad
p-\frac{1-a}{2}=\frac12-\ell>\frac14.
\tag{143.C35}
\]

Also \(\delta+\ell<3/4\), so \(p>5/8\).  The additional residual-cell
inequality creates no improving chamber.  The coefficient-blind proof of
(143.C5) also works after replacing the character by arbitrary unit phases;
it therefore does not exploit the required cross-modulus sign.

## 6. First unproved step, controls, and dependencies

The first gap depends on the chosen spectral representation.

For a pure-level-\(4\), switched-cusp route, (143.C3) supplies only the
arithmetic double-coset identity.  A convention-matched odd-character
weight-one trace formula, including Fourier normalizations at both cusps,
same- and opposite-sign transforms, Plancherel measure, exceptional
parameters, continuous terms, and any scattering contributions, remains
to be derived.

For the source-certified Blomer--Milićević level-\(4/8\) route, the first
project gap is the displayed \(4n\)-sample requirement immediately after
(143.C27): prove a vector-valued trace theorem or a
low-projective-cost decomposition of the literal centered \(h\ne0\)
matrix with uniform modulus Sobolev/Bessel control, all profiles and
endpoints, both signs or an equivalent positive-representative treatment,
the long range outside (143.C28), exceptional spectrum, all level-\(4/8\)
Eisenstein families, and the level-\(8\) oldclasses.  No audited source or
frozen lemma supplies it.

The exact gcd-restored identity, character sign, cusp/modulus progression,
real-centre ownership, zero class, row Parseval, Schatten upper prices,
complete Kloosterman second moment, Linnik range, self-return, and full
polytope comparison all pass.  The source audit rejects direct use of
Kıral--Young for odd \(\chi _4\), weight zero, a pure-level-\(4\) spectral
ledger attributed to the audited sources, unsupported opposite-sign
constants, omitted level-\(8\) oldclasses or cusps, arbitrary joint-matrix
input to a scalar large sieve, and any inference from capacity to a signed
lower bound.

The exact accepted graph dependencies are
M9-M2-unbalanced-truncated-divisor-fixed-centre-return,
M9-M2-unbalanced-flat-wave-curvature-envelope,
M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction, and
M9-M2-character-factor.  The exact Round-143 evidence is:

- reports/level_four_kloosterman_embedding_attack.md;
- reports/blind_joint_matrix_spectral_feasibility.md;
- reports/kuznetsov_source_hypothesis_audit.md;
- reviews/blind_post_unmask_discovery_seam_audit.md;
- reviews/discovery_post_unmask_blind_seam_audit.md;
- reviews/source_post_unmask_spectral_claims_audit.md;
- reviews/blind_post_unmask_source_hypothesis_audit.md; and
- reviews/discovery_conductor_candidate_seam_audit.md.

Every relative path above is under the Round-143 campaign directory.  The
inherited context is protocol.md, state/proof_obligations.yml,
state/active_campaign.yml, strategy/conductor_0823_full_proof_strategy.md,
and these exact Round-135 source-map artifacts:

- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/bettin_chandee_wright_kloosterman.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/conductor_round135_kloosterman_dispersion_adjudication.md; and
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md.

No
numerical experiment, average over \(X\), or erased gcd stratum is used.
No arbitrary matrix is substituted for the literal family; the abstract
diagonal appears only as a control proving that row Parseval alone cannot
imply a smaller nuclear upper price.  The round allocation is 100 percent
analytical and source verification.

The candidate concerns one flat-smooth strict-UNBAL owner only.  It proves
no sharp, clipped, starred, transition, hard-TOP, BAL, complete M9-M2,
endpoint, M9, bridge, or global theorem.  All inherited global benchmark
nodes remain unchanged; no exponent claim is derived in this campaign.

## 7. Recommended state effect

Create a source-audit node recording the exact Kıral--Young parity boundary,
the Blomer--Milićević level-\(4/8\) odd-character identity and \(H+M+E\)
ledger, the same-sign transforms and Linnik range, the Deshouillers--Iwaniec
common-sequence requirement, and the Assing--Blomer--Li smooth
two-variable-test requirement.

Create one proved scoped obstruction recording (143.C3)--(143.C5), the
target-safe zero class, the automatic matrix norms, the missing common-test
or vector-valued interface, the uncovered long-frequency range, the exact
Fourier self-return, and the full-polytope capacity comparison.  Update the
flat UNBAL target and its accepted return/envelope/interface nodes with this
evidence.

Reject claims that the internal arithmetic identity is already a sourced
pure-level-\(4\) weight-one trace formula; that Kıral--Young's even theorem
applies to \(\chi _4\); that weight zero is legal; that the
Blomer--Milićević implementation is pure level four; that level-eight
oldclasses or continuous cusps may be omitted; that row Parseval localizes
the Linnik range or proves a smaller literal trace norm; that exact
interpolation has free Bessel bandwidth; that summing \(h\) is a gain; that
the positive capacity is character cancellation or a signed lower bound;
or that the round proves M9-M2 or improves an exponent.

Keep `M9-M2-smooth-unbalanced-three-quarter-estimate`, `M9-M2`,
`M9-endpoint-uniformity`, `M9`, `Conditional-bridge`, and `GC-target` open.
Make no global exponent change.

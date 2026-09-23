# Source orbit, phase, and power seam review

## 1. Result

The repaired source report is algebraically sound on the two decisive
source computations, subject to two scope qualifications and three
documentary repairs to the literal report.

1. The coset model

   \[
   \Gamma_2(4,1)\backslash{\rm SL}_2(\mathbb Z)
   \cong\mathbb P^1(\mathbb Z/4\mathbb Z)
   \tag{R167.1}
   \]

   and the Hermite representatives

   \[
   \sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
   \qquad b\bmod k,\quad(b,k)=1,
   \tag{R167.2}
   \]

   give an exact, multiplicity-one parametrization of
   \(\Gamma_2(4,1)\backslash\mathcal M_{2,1,k}\).  For the bare
   coefficient

   \[
   \alpha_{\rm bare}(M)=\chi_4(a)\chi_4(b),
   \tag{R167.3}
   \]

   its induced automorphy character is principal, but its finite main-term
   orbit coefficient is exactly zero for every \(k=2^v\), including
   \(k=1\).

2. The unipotent low-top-row-gcd witness is correct for
   \(0<\gamma<1/2\).  It proves that the globally defined factor
   \(\mathbf1_{(a,b)<\gamma L}\) cannot simply multiply
   \(\alpha_{\rm bare}\) and remain left
   \(\Gamma_2(4,1)\)-automorphic.  It does not prove that both witness
   matrices occur in the literal squarefree/profile support, and it does
   not rule out an automorphic extension agreeing only on that restricted
   support.  For \(\gamma\ge1/2\), the low-\(g\) cutoff is identically one
   on K17a and the witness is irrelevant.

3. The normalized phase argument proves that the natural analytic phase
   family is not rank-one in determinant and archimedean variables on a
   common open cell.  The sentence “no one common \(f\) can encode two
   determinants” must be read in that scope.  The ratio argument does not
   exclude a specially constructed \(C^7\) interpolant on the finite
   discrete matrix samples, nor a bounded-rank expansion.  No such
   interpolant or expansion with target-safe seminorm is supplied, so the
   direct source call still fails.

4. The derivative scale

   \[
   \delta^{-1}\gtrsim 1+\frac{|J|r}{L}
   \tag{R167.4}
   \]

   is correct on a nonvanishing interior cell.  Under the source report's
   explicitly optimistic hypothesis
   \(K_+^{1/2}\ll k^{1/2}X^\varepsilon\), the restored ledger is also
   correct: the \(\mathcal R_0\) branch sums at
   \(L^2X^\varepsilon\) if the seminorm loss is ignored, while the
   displayed \(\mathcal R_2\) route certifies only
   \(\delta^{-O(1)}L^{2+\theta_4+\varepsilon}\).

5. The Part-I diagnosis is correct after distinguishing the raw kernel
   from the discrepancy kernel.  An exact no-cross-term identity for the
   raw literal kernel is missing; the theorem then subtracts a separate
   principal component and returns two new nonnegative discrepancy-kernel
   autocorrelations.  Accepted coefficient energy alone does not estimate
   those forms with the missing factor \(L\).

The contrary main-term assertion in
literal_determinant_kernel_attack.md is not correct for the bare 2024
placement.  Principality means that the theorem displays a main term; it
does not prevent the finite orbit sum in that term from vanishing.  The
exact orbit calculation proves that it does vanish for
\(\alpha_{\rm bare}\).  A main-term obligation returns only after changing
the automorphic coefficient, or after constructing a different Part-I
kernel model.

These repairs do not change the round verdict.  Neither audited source
proves K17a, and the scoped terminal conclusion
**oscillatory_determinant_interface_no_go** remains supported.

## 2. Exact statement and hypotheses reviewed

The literal matrix is

\[
 M=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}
 =\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det M=d'm'-dm=r,
\tag{R167.5}
\]

where \(0<r<R_{\rm F}:=\lceil L\rceil\), \(2\mid r\),
\(a,b\) are odd,

\[
 (a-b)(d_0-c)<0,\qquad (a,b)<\gamma L,
\tag{R167.6}
\]

and the literal endpoint weights retain the residual selector,
squarefree support, profiles, hard points, endpoints, zero extension,
Fejer factor, square-root phase, and one outer real part.

Only the source definitions quoted in the repaired source report are
used.  For \(q_1=4,q_2=1\), put

\[
 \Gamma=\Gamma_2(4,1)
 =\left\{\begin{pmatrix}p&q\\s&t\end{pmatrix}
 \in{\rm SL}_2(\mathbb Z):4\mid q\right\}.
\tag{R167.7}
\]

The quoted automorphy law requires, more generally for every allowed
integer \(g\),

\[
 \ell_g\alpha=\chi(g_{11})\xi_{\det g}\alpha.
\tag{R167.8}
\]

For \(r=hk\), \(k=2^{v_2(r)}\), \(h\) odd, the quoted determinant set is

\[
 \mathcal M_{2,h,k}
 =\{M:\det M=hk,\ (a,c,k)=(b,d_0,k)=1\}.
\tag{R167.9}
\]

The quoted 2024 error is

\[
 Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
 \|\beta\xi\|_2K_+^{1/2}
 \{\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\},
\tag{R167.10}
\]

with

\[
 \mathcal R_0=
 \frac{\|\beta\xi\|_1A^{1/2}}
 {\|\beta\xi\|_2q_1^{1/2}C^{1/2}},
\tag{R167.11}
\]

\[
 \mathcal R_1=
 \frac{\|\beta\xi\|_1}{\|\beta\xi\|_2}
 H^{\vartheta_4}
 \left(1+\left(\frac{CD}{HK}\right)^{\theta_4}\right)
 \left(1+\left(\frac CA\right)^{1/2-\theta_4}\right),
\tag{R167.12}
\]

\[
 \mathcal R_2=
 \left(1+\left(\frac{CD}{K}\right)^{\theta_4}\right)
 \left(1+\left(\frac{HC}{A}\right)^{1/2-\theta_4}\right),
\tag{R167.13}
\]

up to the fixed conductor and level factors.  Its principal main term
contains

\[
 \sum_{\tau\in\Gamma\backslash\mathcal M_{2,1,k}}\alpha(\tau).
\tag{R167.14}
\]

The quoted 2025 Part-I theorem controls a discrepancy form by

\[
 \delta^{-O(1)}(AD)^{1/2+o(1)}X_0^\theta
 \sqrt{
 \langle\alpha_1\mid\Delta k_1\mid\alpha_1\rangle
 \langle\alpha_2\mid\Delta k_2\mid\alpha_2\rangle},
\tag{R167.15}
\]

where both displayed quadratic forms are nonnegative.  It does not erase
the quoted principal component

\[
 \frac{\mathbf1_{\chi\ {\rm principal}}}{|\Gamma\backslash G|}
 \overline{\langle1\rangle_{\alpha_1}}
 \langle1\rangle_{\alpha_2}\int_G F(g)\,dg.
\tag{R167.16}
\]

The review tests the source report only against these quoted definitions
and the literal kernel.  It does not independently import any unquoted
source theorem.

## 3. Proof and derivation

### 3.1 The coset model and bare-character orbit sum

If
\[
 \gamma=\begin{pmatrix}p&4q\\s&t\end{pmatrix}\in\Gamma,
\]
then left multiplication sends the top row \((x,y)\) of a matrix in
\({\rm SL}_2(\mathbb Z)\) to

\[
 (px+4qz,\ py+4qw)\equiv p(x,y)\pmod4.
\tag{R167.17}
\]

Since \(pt-4qs=1\), \(p\) is a unit modulo \(4\).  Thus the projective
top row modulo \(4\) is a left-coset invariant.  Conversely the standard
primitive-row completion shows that this invariant is complete.  The six
classes may be represented by

\[
 (x,1),\quad x=0,1,2,3,\qquad(1,0),\ (1,2),
\tag{R167.18}
\]

which proves (R167.1).

The bare coefficient is left invariant.  Indeed, for every allowed
integer \(g=\bigl(\begin{smallmatrix}p&4q\\s&t\end{smallmatrix}\bigr)\)
with \((\det g,4)=1\), \(p\) is odd and

\[
\begin{aligned}
\alpha_{\rm bare}(gM)
&=\chi_4(pa+4qc)\chi_4(pb+4qd_0)\\
&=\chi_4(p)^2\chi_4(a)\chi_4(b)
=\alpha_{\rm bare}(M).
\end{aligned}
\tag{R167.19}
\]

Hence the source character is principal and \(\xi=1\).

Left integral row reduction gives a unique Hermite representative
\(\bigl(\begin{smallmatrix}u&b\\0&v\end{smallmatrix}\bigr)\) for each
\({\rm SL}_2(\mathbb Z)\)-left orbit of determinant \(k\).
The first column-primitivity condition forces \(u=1\), hence \(v=k\);
the second forces \((b,k)=1\).  Reducing \(b\bmod k\) gives exactly
(R167.2).  Since every determinant-\(k\) matrix is invertible over
\(\mathbb Q\), there is no stabilizer multiplicity.  Therefore the pairs
consisting of a class in (R167.18) and a unit \(b\bmod k\) parametrize
\(\Gamma\backslash\mathcal M_{2,1,k}\) exactly.

If \((x,y)\) is a top row in (R167.18), the top row after multiplication
by \(\sigma_b\) is

\[
 (x,\ xb+yk).
\tag{R167.20}
\]

Thus (R167.14) for the bare coefficient equals

\[
 \Sigma(k)=
 \sum_{\substack{b\bmod k\\(b,k)=1}}
 \ \sum_{(x,y)\ {\rm in}\ (R167.18)}
 \chi_4(x)\chi_4(xb+yk),
\tag{R167.21}
\]

with \(b=0\) when \(k=1\).  The three cases are exact:

- \(k=1\): only \((1,1)\) and \((3,1)\) contribute, with values
  \(+1\) and \(-1\), so \(\Sigma(1)=0\).
- \(k=2\): \(b=1\).  The four \((x,1)\) classes contribute \(-2\),
  while \((1,0),(1,2)\) contribute \(+2\), so \(\Sigma(2)=0\).
- \(4\mid k\): for each odd \(b\), the four odd-nonzero contributions
  total \(4\chi_4(b)\).  The units modulo \(2^v\) are equally divided
  between \(1\) and \(3\bmod4\), so
  \(\sum_{b\bmod k}^{*}\chi_4(b)=0\).

Consequently

\[
 \boxed{\Sigma(2^v)=0\quad\text{for every }v\ge0.}
\tag{R167.22}
\]

This is a finite-orbit cancellation inside the principal branch.  It is
stronger than merely observing that the induced character is principal.

### 3.2 The low-\(g\) witness and its exact scope

For \(0<\gamma<1/2\) and sufficiently large \(L\), choose an odd
\(G\) with

\[
 \gamma L\le G<L/2
\tag{R167.23}
\]

and an odd \(T\asymp L\).  Put

\[
 M=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},
 \qquad
 u=\begin{pmatrix}1&4\\0&1\end{pmatrix}\in\Gamma.
\tag{R167.24}
\]

Then

\[
 \det M=2G,\qquad
 (G,3G)=G\ge\gamma L,
\tag{R167.25}
\]

whereas the top row of \(uM\) is

\[
 (G+4T,\ 3G+12T+8).
\tag{R167.26}
\]

Its gcd divides \(8\), and both entries are odd, so that gcd is \(1\).
The determinant stays \(2G<L\), and both \(M\) and \(uM\) have negative
top displacement and positive lower displacement.  Therefore

\[
 \mathbf1_{(a,b)<\gamma L}(M)=0,\qquad
 \mathbf1_{(a,b)<\gamma L}(uM)=1.
\tag{R167.27}
\]

Since the bare character is nonzero on all four top rows involved,
\(\alpha_{\rm bare}\mathbf1_{(a,b)<\gamma L}\) violates the principal
left-automorphy law.

There are two essential limitations.

First, if \(\gamma\ge1/2\), then \(g=(d,d')\) is odd, \(g\mid r\), and
\(r/g\) is even.  Hence

\[
 g\le r/2<L/2\le\gamma L,
\tag{R167.28}
\]

so the target cutoff is identically one.  The witness cannot be extended
to that range.

Second, the construction does not verify that \(M\) and \(uM\) both lie
in the exact literal shell with nonzero \(\lambda\), squarefree products,
selected-prime data, profiles, hard points, and endpoints.  It is a valid
counterexample to the global proposed coefficient
\(\alpha_{\rm bare}\mathbf1_{(a,b)<\gamma L}\), because source
automorphy is a global law.  It is not a literal K17a incidence pair and
does not disprove the existence of another automorphic coefficient whose
restriction agrees with the project weight only on literal support.

### 3.3 Common phase, derivative scale, and source power

On determinant \(r>0\), define

\[
 x=\frac a{\sqrt r},\qquad
 y=\frac c{\sqrt r},\qquad
 z=\frac{d_0}{\sqrt r}.
\tag{R167.29}
\]

The missing normalized entry is

\[
 \frac b{\sqrt r}=\frac{xz-1}{y},
\tag{R167.30}
\]

and the phase is

\[
 e\!\left(J\sqrt r\,G(x,z)\right),\qquad
 G(x,z)=\sqrt{xz}-\sqrt{xz-1}.
\tag{R167.31}
\]

Suppose on a common open normalized cell that this family factored as
\(b(r)f(x,y,z)\) for two distinct determinants \(r_1,r_2\).  Their ratio
would make

\[
 e\!\left(J(\sqrt{r_1}-\sqrt{r_2})G(x,z)\right)
\tag{R167.32}
\]

constant on that cell.  But

\[
 \partial_{xz}G=
 \frac1{2\sqrt{xz}}-\frac1{2\sqrt{xz-1}}\ne0
\tag{R167.33}
\]

when \(xz>1\).  For \(J\ne0\) and \(r_1\ne r_2\), (R167.32) is
nonconstant on every sufficiently small open subcell.  This proves
failure of the natural rank-one analytic representation.

It does not prove a theorem about arbitrary interpolation on the discrete
sets
\[
 \{(a/\sqrt r,c/\sqrt r,d_0/\sqrt r):M\ {\rm literal}\}.
\tag{R167.34}
\]
Those sets need not share a point.  A smooth interpolant may exist at the
cost of very small transition scales; no bound for that cost is given.
Accordingly the source report's safe conclusion is “no admissible common
\(f\) is proved,” together with rank-one failure, not universal
nonexistence of a common smooth interpolant.

For the physical phase

\[
 \phi_r(a,d_0)=J\{\sqrt{ad_0}-\sqrt{ad_0-r}\},
\tag{R167.35}
\]

direct differentiation gives

\[
 \partial_a\phi_r
 =-\frac{Jd_0r}
 {2\sqrt{ad_0}\sqrt{ad_0-r}
  \{\sqrt{ad_0}+\sqrt{ad_0-r}\}}.
\tag{R167.36}
\]

When \(a,d_0,A\asymp L\),

\[
 A|\partial_a\phi_r|\asymp\frac{|J|r}{L}.
\tag{R167.37}
\]

Repeated logarithmic derivatives of \(\phi_r\) have the same scale on a
nondegenerate cell, while differentiating its exponential produces
powers of that scale.  Hence (R167.4) is necessary on an interior region
where the remaining amplitude is constant, or has smaller scaled
derivatives, and is sufficient for the phase factor alone through order
seven.  At \(r\asymp L\), this reaches \(\delta^{-1}\gtrsim |J|\).
The quoted theorem retains an unspecified \(\delta^{-O(1)}\), so it
cannot certify an \(X^\varepsilon\)-safe cost.

Now impose exactly the optimistic assumptions used by the source report:

\[
 A=C=D\asymp L,\quad K\asymp k,\quad
 H\asymp L/k,\quad
 K_+^{1/2}\ll k^{1/2}X^\varepsilon,
\tag{R167.38}
\]

and \(|\beta_h|\asymp1\) on \(\asymp H\) indices.  Then

\[
 \|\beta\|_2\asymp H^{1/2},\qquad
 \|\beta\|_1/\|\beta\|_2\asymp H^{1/2},
\tag{R167.39}
\]

so the prefactor before the \(\mathcal R_j\)'s is
\[
 L H^{1/2}k^{1/2}.
\tag{R167.40}
\]

The \(\mathcal R_0\) branch gives

\[
 L H^{1/2}k^{1/2}\mathcal R_0
 \asymp LHk^{1/2}
 \asymp L^2k^{-1/2}.
\tag{R167.41}
\]

For the top \(H\)-block,

\[
 \mathcal R_2
 \asymp L^{1/2+\theta_4}k^{-1/2}
\tag{R167.42}
\]

up to lower-order \(1+\) terms, and therefore

\[
 L H^{1/2}k^{1/2}\mathcal R_2
 \asymp L^{2+\theta_4}k^{-1/2}.
\tag{R167.43}
\]

The corresponding \(\mathcal R_1\) scale is no smaller:

\[
 L H^{1/2}k^{1/2}\mathcal R_1
 \asymp
 L^{2+\vartheta_4+\theta_4}
 k^{-1/2-\vartheta_4}
\tag{R167.44}
\]

in the dominant range.  Thus \(\min(\mathcal R_1,\mathcal R_2)\) is
represented by the \(\mathcal R_2\) size, up to fixed factors.  Since

\[
 \sum_{k=2^v}k^{-1/2}\ll1,
\tag{R167.45}
\]

the two-adic sum gives \(L^2\) for the \(\mathcal R_0\) branch and
\(L^{2+\theta_4}\) for the exceptional-spectrum branch, before the
unresolved \(\delta^{-O(1)}\) factor.

This is a certification ledger under an assumed \(K_+\) estimate, not a
lower bound.  It corrects the literal report's incomplete
\(\mathcal R_0\)-only ledger.  Because the quoted source does not expose
the final exponent in \(\delta^{-O(1)}\), the literal report's
\(J^{-C_*}\) compensation formula should also be treated as conditional
on a positive recovered exponent \(C_*\), not as an exact quoted source
power.

### 3.4 Part I and the discrepancy self-return

The exact endpoint quadratic form in the literal report is a valid
identity for its hand-defined directed kernel.  It is not yet a Part-I
identity.  The missing source statement is first

\[
 \mathfrak C^{\rm rem}_{R_{\rm F},2,\mathrm{opp},g<\gamma L}
 =\langle\alpha_1,K_F\alpha_2\rangle
\tag{R167.46}
\]

with every literal incidence counted once and no extra relative pairs.
Even after (R167.46), the theorem controls the discrepancy part, so one
must write

\[
 \langle\alpha_1,K_F\alpha_2\rangle
 =
 \langle\alpha_1,\Delta F\,\alpha_2\rangle
 +{\rm Principal}(\alpha_1,\alpha_2,F)
\tag{R167.47}
\]

and estimate the principal term (R167.16) separately.

The discrepancy estimate then contains the geometric mean of the two
nonnegative forms in (R167.15).  These are new automorphic-kernel
autocorrelations of the actual endpoint weights.  The literal energy
bound controls only the diagonal endpoint mass; it does not imply the
factor-\(L\) cancellation in these forms.  This is the precise
autocorrelation self-return.

The literal report's equation equating the raw K17a form directly with a
\(\Delta F\) form omits (R167.16) unless its vanishing is separately
proved.  Its stronger phrase that the Part-I right side “returns the same
\(L^3X^\varepsilon\) capacity” is not source-certified before an exact
kernel and its degrees are constructed.  The defensible conclusion is
the one in the repaired source report: the two positive forms are
unproved, and accepted energy alone does not supply the missing \(L\).

Finally, the quoted Part-I statement permits complex oscillatory \(f\).
The paper title is not a positivity or nonoscillation hypothesis.  If the
phase is put in \(f\), it is charged through \(C^{10}_\delta\) and
\(\delta^{-O(1)}\); if put in endpoint functionals, (R167.46) is still
missing.

## 4. First doubtful or unproved step

For the 2024 placement, the first mathematical gap remains the exact
source-class interface:

> Construct a multiplicity-preserving, bounded- or
> \(X^{o(1)}\)-rank decomposition of the full literal coefficient into
> legal automorphic coefficients and common \(C^7_\delta\) functions,
> preserving all even determinants under one outer real part, and then
> prove the associated \(K_+\), main-term, seminorm, boundary, and
> endpoint bounds at \(L^2X^\varepsilon\).

For \(0<\gamma<1/2\), the simplest coefficient placement is explicitly
illegal by (R167.27).  For all \(\gamma\), the residual selector has no
quoted automorphy law, and no target-safe common interpolation or
controlled-rank determinant expansion is constructed.

For Part I, the earlier missing step is the raw no-cross-term identity
(R167.46).  After it, both the principal component and the two
nonnegative autocorrelations remain.

The first documentary seam needing correction in the source report is
the unqualified common-\(f\) sentence: its proof establishes continuous
rank-one nonseparability, not impossibility of every discrete smooth
interpolant.  The first substantive contradiction between reports is the
literal report's assertion that the bare principal main term has no
character-forced vanishing.  Equation (R167.22) disproves that assertion.

## 5. Control tests and outcomes

1. **Gamma coset cardinality and representatives — PASS.**  The six
   projective top rows give all left cosets once.

2. **Hermite and determinant-orbit multiplicity — PASS.**  Column
   primitivity forces the representatives (R167.2), and invertibility
   removes stabilizers.

3. **Bare automorphy and principal character — PASS.**  Equation
   (R167.19) gives the exact principal law.

4. **Bare principal-orbit sum — PASS.**  The three-case computation
   proves (R167.22) for every \(2\)-power \(k\).

5. **Low-gcd nonautomorphy — PASS WITH SCOPE.**  The witness is exact
   for \(0<\gamma<1/2\) as a global source-coefficient obstruction.
   It is vacuous for \(\gamma\ge1/2\) and is not an exact literal-support
   incidence witness.

6. **Common-\(f\) phase claim — PASS ONLY AFTER QUALIFICATION.**  The
   natural phase is not determinant-times-common-function on a shared
   open cell.  Discrete interpolation and controlled-rank expansions are
   unexcluded but unproved.

7. **Phase \(C^7_\delta\) scale — PASS.**  Equations
   (R167.36)--(R167.37) give \(1+|J|r/L\).

8. **Restored \(\mathcal R_0/\mathcal R_2\) power ledger — PASS UNDER
   ITS STATED OPTIMISTIC \(K_+\) HYPOTHESIS.**  The two-adic sums are
   respectively \(L^2\) and \(L^{2+\theta_4}\), with
   \(\delta^{-O(1)}\) still present.

9. **Literal-report main-term claim — FAIL; DOCUMENTARY REPAIR
   REQUIRED.**  Bare-character orbit cancellation is exact.  A main-term
   obligation remains only for a modified coefficient or a new Part-I
   model.

10. **Part-I identity and principal component — FAIL AS AN
    APPLICATION, PASS AS A NO-GO.**  The raw identity, principal term,
    and target-size autocorrelations are all missing.

11. **Part-I autocorrelation self-return — PASS QUALITATIVELY.**  The
    positive discrepancy forms contain new project correlations.  An
    exact \(L^3\) capacity statement is not yet derived from the source.

12. **One outer real part and no fixed-\(r\) triangle — PASS.**  The
    source report correctly rejects summing separate theorem errors
    absolutely.

13. **Downstream scope — PASS.**  No K17a proof, parent promotion, or
    exponent improvement follows.

No numerical experiment or external source lookup was used.

## 6. Dependencies and exact artifacts used

This review used only:

- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/literal_determinant_kernel_attack.md;
- strategy/round167_m2_hard_top_t1_residual_oscillatory_determinant_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/barrier_packet.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md.

The source report was refreshed after its documentary repair.  The
version reviewed had SHA-256
\(C7275730CE63B1C8FEA819C6EA9407D90D958AC5C401CC44546487BE79B6B074\)
at the time of drafting.  All source hypotheses used above are the
definitions and formulas quoted in that report; no independent claim is
made about unquoted portions of either paper.

## 7. Recommended state effect

**Revise the documentary seams; retain the source-interface no-go and
make no proof-state change.**

For any Round-167 synthesis:

1. promote the exact coset/Hermite calculation and the bare orbit
   cancellation (R167.22) as candidate evidence;
2. describe the low-\(g\) witness only as a global direct-coefficient
   obstruction for \(0<\gamma<1/2\), with its literal-support limitation;
3. replace universal common-\(f\) language by the proved rank-one
   continuous nonseparability statement plus the absence of a
   target-safe interpolation/decomposition;
4. use the repaired \(\mathcal R_0/\mathcal R_2\) ledger, explicitly
   conditional on the optimistic \(K_+\) input and retaining
   \(\delta^{-O(1)}\);
5. replace the literal report's “no character-forced main-term
   vanishing” claim by exact bare-coefficient cancellation, while
   requiring recomputation for every modified coefficient and Part-I
   model; and
6. state the Part-I gap as raw identity plus principal component plus two
   unproved nonnegative autocorrelations, without asserting an exact
   \(L^3\) theorem-side capacity before the kernel is constructed.

After these repairs, the evidence supports only the narrow conclusion
that the audited 2024 direct placement and presently available Part-I
placement do not certify K17a.  K17a, every broader determinant method,
all parents, and the global exponent remain open.

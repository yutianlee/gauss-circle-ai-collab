# Round 168 conductor-candidate mathematical review

- Candidate: candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md
- Role: final independent mathematical verifier
- Verdict: **PASS**

## 1. Result

Every structural assertion in the candidate passes: the literal scalar and
floor normalization, all Euler factors, exact cardinal Mellin inversion and
contour shift, the explicit residue coefficient series, the
\(L^2J^{-1}\) residue bound, the cardinal/Stieltjes distinction, the
smooth-model stationary scale and radial length, the fixed-\(B\)
polylogarithmic full and residual sectors, the refusal to assert an
AFE-to-Round-162 coefficient bridge, and the downstream quarantine.

The two previously required local repairs are now implemented exactly:

1. On \(\Re s_j=1/2+\eta\), the smooth stationary transform has
   \(L^2\)-norm \(L^{1+2\eta}\), not \(L\) literally. Both the triangle
   and Cauchy ledgers first give
   \[
   L^{2\eta}\sqrt J\,L^{3/2}X^{\varepsilon_{\rm in}}.
   \tag{168.VC1}
   \]
   The repaired candidate keeps this factor, and for a desired
   \(\varepsilon_0>0\) chooses
   \(0<\eta\leq\min(1/8,\varepsilon_0/4)\), followed by an auxiliary
   arithmetic exponent \(\delta>0\) sufficiently smaller than
   \(\varepsilon_0\). Since \(L\leq X^{1/4+o(1)}\),
   \[
   L^{2\eta}X^\delta
   \leq X^{\eta/2+o(1)+\delta}
   \leq X^{\varepsilon_0}
   \]
   for all sufficiently large \(X\), after fixing, for example,
   \(\delta<\varepsilon_0/2\). The exact contour identity remains valid
   for every fixed \(0<\eta<1/4\), while the capacity comparison now
   orders the epsilon quantifiers correctly.
2. The accepted close-opposite-prime decomposition depends on a fixed
   \(\kappa\). The repaired residual corollary now says: for every fixed
   \(B,\kappa>0\), the remainder associated with that canonical
   \(\kappa\)-decomposition satisfies
   \[
   \mathcal S^{\rm rem}_{L,1;\kappa}
   \ll_{\varepsilon,B,\kappa}L^{3/2}X^\varepsilon
   \qquad (L\leq(\log X)^B).
   \tag{168.VC2}
   \]
   Both the remainder and its implied constant are indexed by
   \(\kappa\), in the statement and proof.

No other displayed identity is false, and the candidate is not stronger
than the repaired claimant on the functional-equation seam. In
particular, it correctly says that no exact factorwise-FE or AFE return to
the Round-162 collar has been proved.

## 2. Exact statement and hypotheses

The exact literal parameters are correctly restored as

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
q_X=X/y^2,\qquad
H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
\qquad 1\ll L\ll H.
\tag{168.VC3}
\]

Indeed,

\[
yX^{-1/4}=(J+O(1))J^{-1/2}
=\sqrt J+O(J^{-1/2}),
\]

and the outer floor changes this by \(O(1)\). Consequently the exact
collar comparison is

\[
\frac{\sqrt J}{L}=\frac HL+O(L^{-1}),
\tag{168.VC4}
\]

as the candidate states.

The scalar (168.C2) matches the accepted literal \(t=1\) scalar: it keeps
the squarefree/coprime projector intact; retains the even-\(m\) branch;
uses the correct odd first leg, cone, normalization,
\(\eta_L\), \(\Phi(n/(H+1))\), \(q_X\)-ratio profile, and
square-root phase; and explicitly retains all inherited hard conventions.
The cone and product shell imply \(n,m\asymp L\), so the declared
non-arithmetic amplitude is bounded on \(O(L^2)\) ordered pairs.

The exact contour identity is valid for every fixed
\(0<\eta<1/4\). For the capacity estimate in
\(X^{\varepsilon_0}\) notation, the repaired candidate additionally
chooses \(\eta\) in terms of \(\varepsilon_0\), as in Section 1. The
polylogarithmic result is quantified for every fixed \(B>0\); the
residual version additionally fixes \(\kappa>0\).

## 3. Proof/derivation

### 3.1 Euler factors and holomorphy

At \(p=2\), oddness of \(n\) gives

\[
D_2=1+2^{-s_2},\qquad
G_2=(1+2^{-s_2})(1-2^{-s_2})=1-2^{-2s_2}.
\]

For odd \(p\), the three admissible local states give

\[
D_p=1+x_p+y_p,\qquad
x_p=\chi_4(p)p^{-s_1},\quad y_p=p^{-s_2}.
\]

Removing \(L_p(s_1,\chi_4)\zeta_p(s_2)\) gives

\[
\begin{aligned}
G_p
&=(1+x_p+y_p)(1-x_p)(1-y_p)\\
&=1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2,
\end{aligned}
\]

which is (168.C13). On compact subsets of
\(\sigma_1,\sigma_2>1/2\), its nonconstant terms have a convergent prime
majorant

\[
p^{-2\sigma_1}+p^{-2\sigma_2}
+p^{-\sigma_1-\sigma_2}
+p^{-3\min(\sigma_1,\sigma_2)}.
\]

Thus the factorization and direct holomorphy region in (168.C3)--(168.C4)
are exact. No nonvanishing is used. On a rectangular shift from
\(c_j>1\) to \(1/2+\eta\), \(G\) remains holomorphic,
\(L(s_1,\chi_4)\) is entire, and only the simple pole of
\(\zeta(s_2)\) at \(s_2=1\) is crossed.

### 3.2 Cardinal identity, residue series, and \(L^2/J\)

Because \(\psi\) is supported in \((-1/3,1/3)\), at an integer pair
\((n,m)\) only its own cardinal cell is nonzero. Hence

\[
\mathcal B(n,m)=A_{L,X}(n,m)e(J\sqrt{nm})
\]

exactly, including arbitrary hard lattice values. The finite sum
\(\mathcal B\) is smooth and compactly supported away from the axes.
Its Mellin transform is entire and rapidly decreasing on fixed vertical
strips. Mellin inversion, initial absolute convergence of \(D\), and
polynomial vertical growth of the arithmetic factors justify (168.C17)
and the contour shift (168.C5).

The residue coefficient algebra is also exact. With
\(x=\chi_4(p)p^{-s}\) and \(y=p^{-1}\),

\[
L_p(s,\chi_4)G_p(s,1)
=(1+x+y)(1-y)
=(1-p^{-2})+(1-p^{-1})\chi_4(p)p^{-s}.
\]

Factoring \(1-p^{-2}\) at every odd prime, together with
\(G_2(s,1)=1-2^{-2}\), yields

\[
L(s,\chi_4)G(s,1)
=\frac1{\zeta(2)}
\sum_{\substack{n\geq1\\n\ \mathrm{odd,\ squarefree}}}
\frac{\chi_4(n)}{n^s}
\prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{168.VC5}
\]

In (168.VC5), line juxtaposition denotes multiplication:
\[
L(s,\chi_4)G(s,1)
=\frac1{\zeta(2)}
\left[
\sum_{\substack{n\geq1\\n\ \mathrm{odd,\ squarefree}}}
\frac{\chi_4(n)}{n^s}
\prod_{p\mid n}(1+p^{-1})^{-1}
\right],
\]
exactly as printed unambiguously in (168.C18). The coefficient at
\(n=1\) is \(1/\zeta(2)\), as it must be because
\(G(+\infty,1)=1/\zeta(2)\).

Expanding on \(\Re s_1>1\) and applying one-variable Mellin inversion in
\(x\) proves (168.C19). For every supported cell \(n,m\asymp L\),

\[
\partial_z(2\pi J\sqrt{nz})=\pi J\sqrt{n/z}\asymp J.
\]

The compact support of \(\psi(z-m)\) eliminates boundary terms, and one
integration by parts gives \(O(J^{-1})\) uniformly. There are
\(O(L^2)\) cells, and the residue coefficients have modulus at most one.
Therefore

\[
R_\zeta\ll L^2J^{-1}X^\varepsilon.
\]

Since \(L\ll H\ll J^{1/2}\), this is target-safe. Equations
(168.C5)--(168.C7) are consequently an exact reduction, for each chosen
cardinal interpolation.

### 3.3 Stieltjes distinction

Let

\[
\sum_{n\geq1}\rho(n)n^{-s}=L(s,\chi_4)G(s,1)
\]

on an initial line. In the exact mixed-difference/half-integer Perron
model, evaluation of the \(s_2=1\) residue and telescoping in the second
variable give

\[
R_\zeta^{\rm St}
=\sum_{n,m}\rho(n)A_{L,X}(n,m)e(J\sqrt{nm}),
\]

because \(m\asymp L>1\), so the possible lower-threshold correction at
\(m=1\) vanishes. This is (168.C22). It has no continuous
\(z\)-variable in which to integrate by parts and has \(L^2\) absolute
capacity. The candidate correctly treats (168.C19) and (168.C22) as
different exact interpolations and transfers no cardinal residue saving
to the Stieltjes model.

### 3.4 Stationary and Cauchy ledgers

For the explicitly qualified recombined smooth/BV component, set

\[
x=rw,\qquad z=r/w,\qquad t_\pm=t_1\pm t_2.
\]

The radial phase is \(2\pi Jr+t_+\log r\), with stationary equation

\[
t_+=-2\pi Jr\asymp-JL.
\]

As \(r\) traverses a fixed-relative shell, the \(t_+\)-band has length
\(T\asymp JL\). On the shifted lines, one-dimensional stationary phase
gives

\[
L^{1+2\eta}T^{-1/2}
=L^{2\eta}\sqrt{L/J},
\]

which verifies (168.C8)--(168.C9). Triangle inequality with the granted
pointwise arithmetic majorant gives (168.VC1).

The transform's radial \(L^2\)-norm is, before epsilon absorption,

\[
\bigl(T(L^{1+2\eta}T^{-1/2})^2\bigr)^{1/2}
=L^{1+2\eta}.
\tag{168.VC6}
\]

Cauchy with a granted arithmetic mean square
\(TX^{\varepsilon_{\rm in}}\) therefore also gives (168.VC1), up to the
routine halving/relabeling of the mean-square exponent. After the
repaired quantifier choice in Section 1, this has the advertised
\(\sqrt J\,L^{3/2}X^{\varepsilon_0}\) form. The candidate correctly
limits this capacity statement to the named triangle/Cauchy placements,
does not apply it to a unit cardinal cell, and does not infer a physical
lower bound or a universal hybrid no-go.

### 3.5 Functional equations, polylogarithmic sector, and connector

The candidate makes the correct repaired statement: no exact coefficient
bridge from factorwise functional equations or approximate functional
equations to the Round-162 collar has been proved. It imports only the
accepted conditional comparison obtained by deliberately reopening the
projector and applying positive physical Poisson. Formula (168.C23)
then uses the exact floor relation (168.VC4). This is no stronger than
the repaired claimant or the supplied source conclusion.

On the literal support, all fixed profiles and
\((L^2/(nm))^{3/4}\) are bounded and there are \(O(L^2)\) pairs. Hence

\[
|\mathcal S_{L,1}|\ll L^2X^{\varepsilon/2}.
\]

For fixed \(B\), \(L\leq(\log X)^B\) implies
\[
L^{1/2}\ll_{\varepsilon,B}X^{\varepsilon/2},
\]
which proves the full-scalar (168.C12) with all endpoints included.

For a fixed \(\kappa\), the accepted kernel gives
\[
\mathcal S^{\rm cp}_{L,1;\kappa}\ll_\kappa L^{3/2}
\]
and exact complementary decomposition
\[
\mathcal S_{L,1}
=\mathcal S^{\rm cp}_{L,1;\kappa}
+\mathcal S^{\rm rem}_{L,1;\kappa}.
\]
Subtraction proves (168.VC2). It supplies no general residual statement
and no other channel or parent.

## 4. First doubtful or unproved step

No doubtful or unproved step remains inside the candidate's asserted
kernel. The former epsilon issue is repaired: (168.C10) retains
\(L^{2\eta}\), the proof retains the radial norm \(L^{1+2\eta}\), and
\(\eta\) and \(\delta\) are chosen after the requested output epsilon.
The former \(\kappa\) ambiguity is also repaired in both the strict
sector statement and the exact decomposition.

There is no missing AFE-to-collar step hidden in the candidate: it
explicitly declares that seam unproved. The first genuinely open
analytic theorem remains the exact signed two-height estimate (168.C7),
or an equivalent endpoint-lawful physical estimate.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| Literal scalar and normalization | **PASS.** Equation (168.C2) matches the accepted object. |
| Exact \(y,q_X,H\) floors | **PASS.** Equations (168.C1) and (168.C23) use \(H=\sqrt J+O(1)\), not equality. |
| Odd and two-adic Euler factors | **PASS.** All local states and corrections are exact. |
| Holomorphy and pole ledger | **PASS.** Only \(s_2=1\) is crossed in the stated shift. |
| Cardinal interpolation and Mellin signs | **PASS.** It preserves every lattice value and gives \(D(s_1,s_2)\) with the correct signs. |
| Residue coefficient series | **PASS.** Equation (168.C18) follows prime by prime and includes the \(1/\zeta(2)\) constant. |
| \(L^2/J\) residue bound | **PASS.** One nonstationary integration by parts per cell suffices. |
| Cardinal/Stieltjes distinction | **PASS.** Equation (168.C22) is exact for \(m\asymp L>1\) and is not declared small. |
| Smooth radial frequency and scale | **PASS.** Band \(JL\), pointwise scale \(L^{1+2\eta}(JL)^{-1/2}\). |
| Triangle ledger | **PASS.** The candidate retains \(L^{2\eta}\) and chooses \(\eta,\delta\) after the requested epsilon. |
| Cauchy ledger | **PASS.** The pre-absorption transform norm is correctly \(L^{1+2\eta}\). |
| AFE/functional-equation scope | **PASS.** The candidate expressly denies an unproved exact self-return. |
| Fixed-\(B\) polylog full sector | **PASS.** The epsilon relabeling is exact. |
| Residual connector | **PASS.** The canonical decomposition, remainder, and implied constant are all qualified by fixed \(\kappa\). |
| Downstream quarantine | **PASS.** No polynomial block, general residual, parent, bridge, theorem, or exponent is promoted. |

## 6. Dependencies/exact artifacts used

The verification used only:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/literal_pre_mobius_mellin_attack.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/blind_mellin_euler_rederivation.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reviews/claimant_math_endpoint_power_review.md;
6. proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
7. proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md.

No proof graph, active campaign, shared state, sibling review, candidate,
or synthesis other than the assigned conductor candidate was inspected or
edited. No external theorem is used to prove any displayed identity in
this review.

## 7. Recommended state effect

**PASS.**

The repaired candidate now states the raw stationary and Cauchy powers
with \(L^{2\eta}\), chooses \(\eta\) and the auxiliary arithmetic
exponent after the requested final epsilon, and fixes \(\kappa\) in the
residual sector and its implied constant. These repairs are exact.

The Euler/cardinal/residue reduction, the scoped absolute-capacity
obstruction, and the fixed-\(B\) full/residual sector are suitable for
promotion at precisely their stated scope. The candidate correctly adds
no AFE-to-Round-162 equivalence and promotes no polynomial-\(L\), general
residual, other-channel, parent, bridge, quarter-theorem, or exponent
claim.

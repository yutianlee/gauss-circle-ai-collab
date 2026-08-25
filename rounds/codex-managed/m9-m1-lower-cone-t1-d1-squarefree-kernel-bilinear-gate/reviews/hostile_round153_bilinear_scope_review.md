# Round 153 hostile bilinear method and scope review

- Campaign: m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate
- Role: hostile terminal method/scope reviewer
- Starting graph SHA-256: 9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1
- Final re-review verdict: **GREEN**
- Terminal label: squarefree_kernel_bilinear_no_go, interpreted only in the scoped sense below

## 1. Result and final re-review verdict

The exact algebraic kernel is correct. Complete squarefree Mobius inversion,
followed by the exact recombination \(r=as\), returns the direct large-defect
wave plus an absolutely target-safe boundary:

$$
 P_U^*
 =
 \sum_{\substack{b\ge 1\\ b\ \operatorname{odd}}}F_U(b)
 +
 \sum_{\substack{r\ge S\\ r\ \operatorname{odd}}}
 C_S(r)
 \sum_{\substack{b\ge 1\\ b\ \operatorname{odd}}}F_U(r^2b),
 \qquad
 S=\lceil M^{1/4}\rceil,
\tag{153.H1}
$$

where

$$
 C_S(r)=\sum_{\substack{a\mid r\\ r/a<S}}\mu(a).
\tag{153.H2}
$$

The second term in (153.H1) is
\(O_\varepsilon(X^\varepsilon)\), so

$$
 P_U^*=P_U^{\mathrm{LD}}+O_\varepsilon(X^\varepsilon)
      =P_U+O_\varepsilon(X^\varepsilon).
\tag{153.H3}
$$

The candidate and both corrected reports now satisfy every mandatory
requirement from the first review:

- the no-go label is explicitly limited to exact complete-Mobius
  recombination and coefficient-blind positive majorants;
- a future coefficient-sensitive signed bilinear theorem is expressly left
  possible;
- the Cauchy wording now distinguishes loss of an exact divisor cancellation
  from impossibility;
- the Round-152 pre-Cauchy mask-removal seam is stated with its exact local
  scope;
- the blind exponent-pair sign assertion is corrected; and
- the discovery report now labels (153.D45) as an optimistic all-\(B\)
  control and (153.D46) as an ambient coefficient-blind capacity.

There is no remaining terminal method or scope defect. The terminal verdict
is GREEN.

## 2. Exact statement, hypotheses, and proof

Define the literal direct large-defect weight

$$
 F_U(n)=
 {\bf1}_{n\ \operatorname{odd}}
 {\bf1}_{|k(n)^2-Nn|>M^{3/4}}
 \chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}).
\tag{153.H4}
$$

The hypotheses used are exactly:

1. \(N=\lfloor X\rfloor\), \(R=X^{1/4}\), \(1\ll M\le R^2\), and
   \(S=\lceil M^{1/4}\rceil\);
2. \(A_U\) is the literal zero-extended actual profile on finitely many
   inherited support components in a fixed dilation of \(n\asymp M\);
3. all variables are positive and odd;
4. every odd \(\ell\) has the unique representation
   \(\ell=\tau s^2\), with \(\tau\) squarefree and \(s\) odd; no false
   coprimality condition is imposed; and
5. Round 152 owns the exact-square and nonzero-small-defect sectors in the
   actual \(D=d=L=1\) wave.

Since \(\chi_4(\tau s^2)=\chi_4(\tau)\),

$$
 P_U^*
 =
 \sum_{\substack{s<S\\ s\ \operatorname{odd}}}
 \sum_{\substack{\tau\ge1\\ \tau\ \operatorname{odd}}}
 \mu^2(\tau)F_U(\tau s^2).
\tag{153.H5}
$$

Insert

$$
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),
 \qquad
 \tau=a^2b.
\tag{153.H6}
$$

The complete summand is \(F_U((as)^2b)\), so the finite change \(r=as\)
has coefficient (153.H2). If \(r<S\), every divisor \(a\mid r\) is
admissible and

$$
 C_S(r)=\sum_{a\mid r}\mu(a)
 =
 \begin{cases}
 1,&r=1,\\
 0,&1<r<S.
 \end{cases}
\tag{153.H7}
$$

The strict ceiling is handled correctly: \(r=S\) lies in the boundary,
whether or not \(S\) is odd. On literal support,

$$
 |C_S(r)|\le d(r),
 \qquad
 \#\{b:F_U(r^2b)\ne0\}\ll 1+\frac{M}{r^2},
 \qquad
 |F_U(r^2b)|\ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{153.H8}
$$

Therefore

$$
 M^{-3/4}X^\varepsilon
 \sum_{S\le r\ll\sqrt M}d(r)
 \left(1+\frac M{r^2}\right)
 \ll_\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\tag{153.H9}
$$

This proves (153.H1)--(153.H3). The profile, zero extension, endpoints,
strict defect test, nearest-integer convention, and every parity of \(N\)
are unchanged. The external \(B_{1,U}(1)\) remains outside the scalar.

## 3. Type-I/Type-II, tails, fibres, and spacing

On \(a\asymp A\), \(b\asymp B\) at fixed \(s\),

$$
 A^2Bs^2\asymp M,
 \qquad
 AB\asymp\frac{M}{As^2},
 \qquad
 as\sqrt{NB}\asymp\sqrt{NM}=R^2\sqrt M.
\tag{153.H10}
$$

The fixed-\(s\) large-\(a\) tail is

$$
 \sum_{a\ge A_0}\sum_b|W_{a,b;s}|
 \ll_\varepsilon
 \left(
 \frac{M^{1/4}}{A_0s^2}
 +
 \frac{M^{-1/4}}s
 \right)X^\varepsilon.
\tag{153.H11}
$$

The sharper joint tail \(as\ge S\) is exactly the divisor-weighted boundary
in (153.H9). Neither tail removes \(a=s=1\).

For an exponent pair \((\kappa,\lambda)\), fixed-\((A,s)\) Type I gives

$$
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}
 A^{1-2\lambda+2\kappa}s^{-2\lambda+2\kappa}X^\varepsilon.
\tag{153.H12}
$$

For the relevant pair
\((\kappa,\lambda)=(195/796,235/398)\), this is

$$
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 A^{123/398}s^{-275/398}X^\varepsilon.
\tag{153.H13}
$$

The blind report now correctly records
\(\lambda-\kappa=275/796<1/2\) and
\(1-2\lambda+2\kappa=123/398>0\). After absolute summation over
\(s\asymp S_0\), the extra factor is
\((AS_0)^{123/398}\). In the strict lower power range, the leading ratio
in (153.H13) has a positive power loss, while absolute capacity is
\(M^{1/4}/(AS_0)\) until the already safe boundary
\(AS_0\asymp M^{1/4}\). This particular split gives no new range.

Both Cauchy placements are correct:

| Placement | Coefficient lost | Coefficient retained | Diagonal capacity |
|---|---|---|---:|
| Cauchy in \(a\) | \(\mu(a)\) | \(\chi_4(b_1)\chi_4(b_2)\) | \(b_1=b_2:\ M^{-1/4}/s\) |
| Cauchy in \(b\) | \(\chi_4(b)\) | \(\mu(a_1)\mu(a_2)\) | \(a_1=a_2:\ M^{1/4}/(A^{3/2}s^2)\) |

After \(s\asymp S_0\) is summed absolutely, the capacities become
\(M^{-1/4}\) and \(M^{1/4}/(A^{3/2}S_0)\). They obstruct only the
coefficient-blind positive majorant; they are not signed lower bounds.

For fixed-\(a\) correlations, a nonzero exact modular collision

$$
 s\sqrt N(\sqrt{b_1}-\sqrt{b_2})\in\mathbb Z
 \quad (b_1\ne b_2)
\tag{153.H14}
$$

occurs exactly when both \(Nb_i\) are squares. If \(N=c^2n_0\) with
\(n_0\) squarefree, these are \(b_i=n_0u_i^2\); they are absent on odd
support when \(n_0\) is even and are removed by the exact-defect mask when
present. The different zero-difference product fibre

$$
 a_1^2b_1=a_2^2b_2
\tag{153.H15}
$$

has the parametrization
\(a_1=gu\), \(a_2=gv\), \((u,v)=1\),
\(b_1=v^2c\), \(b_2=u^2c\). It is not generally an exact-square phase
and must be recombined with its Mobius coefficient.

The quartic separation
\(\|\alpha\|\gg(1+Y)^{-3}\) and the same-square-product improvement
\(\|\alpha\|\gg(1+Y)^{-1}\) are correct. The corrected discovery report
now says explicitly that its \(R/(As)\) value grants quadratic spacing to
all \(B\) ambient points; a literal fixed-\(q\) fibre has only
\(O(\sqrt{B/q}+1)\) points. Its pigeonhole statement is likewise limited
to the ambient all-\(b\), coefficient-blind Dirichlet-kernel majorant and
does not assert nonzero literal weights or a signed barrier.

## 4. First unproved step and mask reconciliation

The first unproved estimate remains

$$
 \left|
 \sum_{\substack{b\ge1\\ b\ \operatorname{odd}}}F_U(b)
 \right|
 \ll_\varepsilon X^\varepsilon
 \qquad
 (M^{449}\ll R^{780}),
\tag{153.H16}
$$

equivalently the unresolved \(P_U^*\) or direct \(P_U\) scalar below the
accepted boundary. The exact collapse neither proves nor refutes
(153.H16).

The blind statement-only report correctly warns that masks cannot be
deleted inside a Cauchy correlation. The candidate now reconciles that
warning with the accepted graph in the only legal way. Round 152 owns the
complete actual-profile absolute mass of the exact and
\(0<|k(n)^2-Nn|\le M^{3/4}\) sectors. After Mobius expansion, a fixed \(n\)
has at most

$$
 \sum_{r^2\mid n}d(r)\ll_\varepsilon X^\varepsilon
\tag{153.H17}
$$

representations \(n=(as)^2b\). Thus the expanded correction remains
\(O_\varepsilon(X^\varepsilon)\) and may be removed at the level of the
complete sum before Cauchy.

This is local to the literal Round-152 \(D=d=L=1\) profile. It does not
validate mask deletion inside a correlation, prove a generic masked
estimate, or transfer to another owner. The candidate states each of these
limitations explicitly.

## 5. Required controls and outcomes

| Control | Final outcome |
|---|---|
| Exact inversion, \(a=1\), and \(s=1\) | GREEN. Every Mobius sign and the compulsory \(a=s=1\) seam remain. |
| Ceiling and boundary | GREEN. \(1<r<S\) cancels exactly and \(r=S\) is included in the safe tail. |
| Actual profile, mask, and \(B_{1,U}(1)\) | GREEN. Literal arguments and external-factor scope are preserved. |
| Large-\(a\) and joint tails | GREEN. The \(M,A,s\) powers and divisor multiplicity are correct. |
| Type-I power | GREEN. The corrected pair-dependent exponent signs agree with (153.H13). |
| Both Cauchy coefficients and diagonals | GREEN. Surviving coefficients are explicit and capacities are not lower bounds. |
| Exact collisions and product fibres | GREEN. Removed square rays and surviving zero product fibres are distinguished. |
| Near spacing and pigeonhole | GREEN. Algebraic spacing, optimistic all-\(B\) control, and ambient capacity have distinct scopes. |
| Masked-correlation seam | GREEN. Removal occurs before Cauchy and only under the Round-152 actual-profile owner. |
| Range | GREEN/no new range. Only \(M^{449}\gg R^{780}\) was already owned. |
| Route label | GREEN. It is explicitly not a future signed-bilinear impossibility theorem. |
| Downstream scope | GREEN. No broader owner or exponent is promoted. |

All checks are analytic. No numerical experiment or computational
certification is used.

## 6. Dependencies and artifacts re-inspected

The review uses:

- protocol.md;
- the active Round-153 entries of state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round153_d1_squarefree_kernel_bilinear_strategy.md;
- the Round-153 barrier packet;
- the corrected conductor candidate
  candidates/conductor_round153_mobius_boundary_collapse.md;
- the corrected discovery report
  reports/squarefree_mobius_bilinear_attack.md;
- the corrected blind report
  reports/blind_squarefree_kernel_typeii_feasibility.md; and
- the Round-152 conductor candidate, adjudication, and controls.

The three corrected Round-153 shared files were re-opened after the first
AMBER review. Their route-scope, Cauchy, mask-reconciliation,
exponent-pair, all-\(B\), pigeonhole, and downstream wording now agrees with
the verified mathematics.

## 7. Recommended state effect and terminal scope

Promote only the exact scoped recombination obstruction:

$$
 P_U^*
 =
 P_U^{\mathrm{LD}}+O_\varepsilon(X^\varepsilon)
 =
 P_U+O_\varepsilon(X^\varepsilon).
\tag{153.H18}
$$

together with the exact coefficient \(C_S(r)\), its cancellation for
\(1<r<S\), and the absolutely safe \(r\ge S\) boundary.

Retain the isolated \(s=1\) squarefree wave and the equivalent direct
large-defect scalar as open. Record the Type-I, Cauchy, diagonal, collision,
near-spacing, and pigeonhole conclusions only as method-scoped upper-capacity
or recombination obstructions. Do not infer that a future signed bilinear
estimate is impossible.

Make no promotion for \(D>1\), \(L>1\), the growing-\(M\) generic sector,
any original \(t\ge2\) layer, the Round-138 cross owner, full M1 or M2,
endpoint uniformity, M9, the conditional bridge, the Gauss-circle target,
or any internal or external exponent.

Final re-review verdict: **GREEN**. All previously mandatory wording and
scope repairs are present; no terminal defect remains.

# Round 169 blind joint-transform rederivation

- Campaign: `m9-m2-hard-top-t1-joint-functional-equation-spectral-gate`
- Task: `blind_joint_transform_rederivation`
- Role: statement-only blind rederiver
- Status: candidate evidence only

## 1. Result: exact joint transform and a self-return no-go

Let \(\mathcal B\) denote the literal endpoint-lawful cardinal interpolant whose Mellin transform occurs in (169.B5), with every floor, star, half-open shell, profile point value, cone edge, endpoint transition, parity choice, and zero extension left inside \(\mathcal B\).  Write \(e(z)=e^{2\pi i z}\), and put \(\alpha=1/2+\eta\), \(0<\eta<1/2\).

The Euler product \(G\) has the pair-multiplicative expansion

\[
G(s_1,s_2)=\sum_{a,b\geq 1}\frac{g(a,b)}{a^{s_1}b^{s_2}},
\]

where, for every odd prime \(p\), the only nonzero local coefficients are

\[
\begin{array}{c|rrrrrr}
(v_p(a),v_p(b))&(0,0)&(1,1)&(2,0)&(0,2)&(2,1)&(1,2)\\ \hline
g_p&1&-\chi_4(p)&-1&-1&1&\chi_4(p),
\end{array}
\tag{169.R1}
\]

and at \(p=2\)

\[
g_2(0,0)=1,\qquad g_2(0,2)=-1,
\qquad g_2(i,j)=0\ \text{otherwise}.
\tag{169.R2}
\]

In particular \(a\) is odd on the support of \(g\).  Applying the two functional equations before any positive norm gives the exact Mellin-ordered joint transform

\[
\mathcal I_\eta
=\mathop{\sum\!\!\sum\!\!\sum\!\!\sum}^{\mathrm{FE}}
_{a,b,r,k\geq1}
\frac{g(a,b)\chi_4(r)}{rk}\,
\mathcal K_{\mathcal B}\!\left(\frac r a,\frac k b\right),
\tag{169.R3}
\]

where

\[
\mathcal K_{\mathcal B}(z,w)
=\frac1{(2\pi i)^2}\int_{(-\eta)}\!\int_{(-\eta)}
\widehat{\mathcal B}(s_1,s_2)X_4(s_1)X_0(s_2)
z^{s_1}w^{s_2}\,ds_1ds_2,
\tag{169.R4}
\]

both contours are independently upward, and

\[
\begin{aligned}
X_4(s)&=\left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)},\\
X_0(s)&=\pi^{s-1/2}
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\end{aligned}
\tag{169.R5}
\]

Here \(\sum^{\mathrm{FE}}\) means the signed limit prescribed by the two Mellin contours (equivalently, finite convolution truncation followed by the two Poisson limits); it is not an iterated absolute sum.  The same transform, with all constants exposed, is

\[
\boxed{
\mathcal I_\eta
=2\mathop{\sum\!\!\sum\!\!\sum\!\!\sum}^{\mathrm{FE}}
_{a,b,r,k\geq1}
\frac{g(a,b)\chi_4(r)}{ab}
\int_0^\infty\!\int_0^\infty
\mathcal B(u,v)
\sin\!\left(\frac{\pi r u}{2a}\right)
\cos\!\left(\frac{2\pi k v}{b}\right)du\,dv .}
\tag{169.R6}
\]

This identity does **not** supply the missing \(\sqrt J\).  If
\(\mathcal B(u,v)=\mathcal A(u,v)e(J\sqrt{uv})\) is merely a pointwise factorization of the exact cardinal interpolant, the four exponential branches in (169.R6) have phases

\[
\Psi_{\sigma,\tau}(u,v)
=J\sqrt{uv}+\sigma\frac{ru}{4a}+\tau\frac{kv}{b},
\qquad \sigma,\tau\in\{\pm1\}.
\tag{169.R7}
\]

Only \((\sigma,\tau)=(-,-)\) can be stationary, and its stationary determinant vanishes precisely on

\[
rk=abJ^2.
\tag{169.R8}
\]

On that collar the radial phase is identically zero after angular stationarity.  Thus the joint transform returns the same product-resonance geometry rather than creating radial oscillation.  The optimistic smooth-band capacity stated in the packet is

\[
(JL)\left(L^{2\eta}\sqrt{\frac LJ}\right)
=L^{3/2+2\eta}\sqrt J,
\tag{169.R9}
\]

which exceeds \(L^{3/2}\) by exactly \(\sqrt J\), even before the literal cardinal-cell corrections are justified.  The functional equations therefore prove neither (169.B6) nor an owner-complete fixed positive-power \(L\)-sector beyond the polylogarithmic regime.  What remains is a new signed arithmetic estimate across the rank-degenerate product collar; it is not a consequence of the two GL(1) functional equations.

## 2. Exact statement and hypotheses

The result above uses only the following hypotheses.

1. \(J=\sqrt X\), \(y=\lfloor J\rfloor\), \(q_X=X/y^2\), \(H=\lfloor yX^{-1/4}\rfloor\), and \(1\ll L\ll H\), exactly as in the statement packet.
2. \(\mathcal B\) is the exact cardinal interpolant underlying (169.B5).  Its zero extension and its support in the \(nm\asymp L^2\), \(m\leq n\leq4m\) region keep it away from the coordinate axes.  Mellin inversions and contour limits are understood in the endpoint-lawful sense asserted by (169.B4)--(169.B5); no smoother replacement is assumed.
3. \(0<\eta<1/2\) and \(\alpha=1/2+\eta\).  The requested \(\varepsilon\) is fixed first; only afterwards may \(\eta\) be chosen small enough that factors such as \(L^{2\eta}\) and the finite \(\eta\)-cost fit inside an \(X^\varepsilon\) allowance.
4. The two heights remain independent: \(s_1=\alpha+it_1\) and \(s_2=\alpha+it_2\), with no substitution \(t_1=t_2\) or \(t_1=\pm t_2\).
5. All sums in the dual formula retain their signs and the common joint phase until (169.R7)--(169.R8) have been exposed.  No pointwise moment, positive moment, or early \(\ell^1\) estimate is part of the derivation.

The conclusion is scoped only to the proposed joint-functional-equation mechanism for \(\mathcal I_\eta\).  It makes no assertion about any other hard-TOP channel, BAL, UNBAL, M1, endpoint uniformity, M9, a bridge, the quarter theorem, or either exponent.

## 3. Proof and derivation

### 3.1. The exact coefficients of \(G\)

For an odd prime, put \(x=\chi_4(p)p^{-s_1}\) and \(y=p^{-s_2}\).  Direct multiplication gives

\[
(1+x+y)(1-x)(1-y)
=1-xy-x^2-y^2+x^2y+xy^2.
\tag{169.R10}
\]

Since \(\chi_4(p)^2=1\), reading off the exponent pair of \((p^{-s_1},p^{-s_2})\) yields (169.R1).  At two,
\(G_2=1-2^{-2s_2}\) yields (169.R2), with no positive two-adic exponent in \(a\).

As a normalization check, multiplying back by the local factors of
\(L(s_1,\chi_4)\zeta(s_2)\) gives

\[
\frac{G_p}{(1-x)(1-y)}=1+x+y \quad(p\text{ odd}),
\qquad
\frac{1-y^2}{1-y}=1+y \quad(p=2).
\tag{169.R11}
\]

Thus the coefficient of \(D\) is exactly supported on coprime squarefree pairs, the first entry is odd, and the coefficient is \(\chi_4(n)\), including the branch in which \(2\mid m\).  Equivalently,

\[
[n^{-s_1}m^{-s_2}]D
=\sum_{a\mid n\,,\,b\mid m}g(a,b)\chi_4(n/a),
\tag{169.R12}
\]

and (169.R11) evaluates this convolution to the required literal coefficient.

The absolute coefficient cost on the original \(\alpha\)-line is also exact:

\[
\begin{aligned}
\mathfrak G_\eta
&:=\sum_{a,b\geq1}\frac{|g(a,b)|}{(ab)^\alpha}\\
&=(1+2^{-2\alpha})
\prod_{p\ \mathrm{odd}}\left(1+3p^{-2\alpha}+2p^{-3\alpha}\right)
\asymp \zeta(1+2\eta)^3\asymp \eta^{-3}.
\end{aligned}
\tag{169.R13}
\]

Indeed, after division by the local factor of \(\zeta(2\alpha)^3\), the logarithm has only \(O(p^{-3\alpha}+p^{-4\alpha})\), which is uniformly summable near \(\alpha=1/2\).  This justifies expanding \(G\) on the starting line, but (169.R13) is not used to take an absolute value over the later dual aggregate.

### 3.2. Completed functions, parity, conductor, root number, and poles

For \(\chi_4\), the parity is odd, the conductor is \(4\), and

\[
\Lambda_4(s)
=\left(\frac4\pi\right)^{(s+1)/2}
\Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi_4).
\tag{169.R14}
\]

The Gauss sum is \(\tau(\chi_4)=2i\), so the root number is
\(\tau(\chi_4)/(i\sqrt4)=1\).  Hence

\[
\Lambda_4(s)=\Lambda_4(1-s),
\qquad
L(s,\chi_4)=X_4(s)L(1-s,\chi_4).
\tag{169.R15}
\]

This completed \(L\)-function is entire; there is no character pole or zero-frequency main term.

For zeta, the parity is even, the conductor and root number are both \(1\), and

\[
\Lambda_0(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Lambda_0(s)=\Lambda_0(1-s),
\tag{169.R16}
\]

so \(\zeta(s)=X_0(s)\zeta(1-s)\).  The only pole crossed in obtaining (169.B4) from a right-hand Dirichlet contour is the simple pole of \(\zeta(s_2)\) at \(s_2=1\).  Its exact residue term is

\[
R_\zeta
=\frac1{2\pi i}\int_{(\alpha)}
\widehat{\mathcal B}(s_1,1)
L(s_1,\chi_4)G(s_1,1)\,ds_1,
\tag{169.R17}
\]

with the bound already supplied in (169.B4).  It is the zero cosine frequency (the integral term) in the physical Poisson formula.  In the later shift of \(\mathcal I_\eta\) from \(\Re s_2=\alpha<1\) to \(\Re s_2=-\eta\), the point \(s_2=1\) lies to the right and no pole is crossed.  At \(s_2=0\), the pole of \(\zeta(1-s_2)\) is canceled by the simple zero of \(X_0(s_2)\); the product is the regular function \(\zeta(s_2)\).  Thus no second main term may be inserted.

Useful exact gamma identities are

\[
\begin{aligned}
X_4(s)&=\Gamma(1-s)\cos(\pi s/2)
       \left(\frac\pi2\right)^{s-1},\\
X_0(s)&=2\Gamma(1-s)\sin(\pi s/2)(2\pi)^{s-1}.
\end{aligned}
\tag{169.R18}
\]

They exhibit respectively the odd sine transform with frequency denominator \(4\), and the even cosine transform with frequency denominator \(1\).

### 3.3. Joint contour movement and the dual coefficients

Rewrite (169.B5) as upward complex contours:

\[
\mathcal I_\eta
=\frac1{(2\pi i)^2}\int_{(\alpha)}\!\int_{(\alpha)}
\widehat{\mathcal B}(s_1,s_2)
L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)\,ds_1ds_2.
\tag{169.R19}
\]

Use (169.R13) to expand \(G\) on these starting contours.  For each finite coefficient truncation, insert both functional equations and move each contour, independently and upward, from \(\Re s_j=\alpha\) to \(\Re s_j=-\eta\).  No pole lies in either strip.  On the final contours,

\[
L(1-s_1,\chi_4)=\sum_{r\geq1}\chi_4(r)r^{s_1-1},
\qquad
\zeta(1-s_2)=\sum_{k\geq1}k^{s_2-1},
\tag{169.R20}
\]

both absolutely, because \(\Re(1-s_j)=1+\eta\).  Substitution gives exactly (169.R3)--(169.R4).  Notice the complete dual Mellin coefficient

\[
\frac{g(a,b)\chi_4(r)}{rk},
\tag{169.R21}
\]

the two independent transform arguments \(r/a\) and \(k/b\), and both gamma quotients.  Passing from finite coefficient truncations to the contour-prescribed limit gives the superscript \(\mathrm{FE}\); it does not license an early absolute rearrangement.

### 3.4. Exact sine-cosine transform and restored powers

For \(z,w>0\), Mellin inversion together with (169.R18) gives

\[
\mathcal K_{\mathcal B}(z,w)
=2zw\int_0^\infty\!\int_0^\infty
\mathcal B(u,v)\sin(\pi zu/2)\cos(2\pi wv)\,du\,dv.
\tag{169.R22}
\]

For example, the one-dimensional identities behind (169.R22) are

\[
\begin{aligned}
\frac1{2\pi i}\int \widehat f(s)X_4(s)z^sds
 &=z\int_0^\infty f(u)\sin(\pi zu/2)du,\\
\frac1{2\pi i}\int \widehat f(s)X_0(s)w^sds
 &=2w\int_0^\infty f(v)\cos(2\pi wv)dv.
\end{aligned}
\tag{169.R23}
\]

They are first valid in a common Mellin strip and then continue to the contour in (169.R4), with no residue at zero.  Combining (169.R21) and (169.R22) cancels the apparently favorable \(1/(rk)\):

\[
\frac1{rk}\,2\frac r a\frac k b=\frac2{ab}.
\tag{169.R24}
\]

This is the first restored-power entry.  At stationarity \(r/a\asymp J\) and \(k/b\asymp J\), the kernel restores the entire apparent \(J^{-2}\) in the dual coefficient.  Equation (169.R6) follows.

There is no endpoint substitution in (169.R22).  It is applied to the exact \(\mathcal B\), so the \(O(L^2)\) cardinal cells and all their specified boundary values remain present.  The zero extension makes the half-line endpoint value at zero vanish.  The zeta pole term has already been separated as (169.R17), while the odd character has no zero mode.  Consequently there is no hidden half-weight, endpoint term, or complementary main term available to improve (169.R6).

### 3.5. Joint phase, lengths, and the rank-degenerate collar

Using

\[
2\sin A\cos B
=\sum_{\sigma,\tau\in\{\pm1\}}
\frac{\sigma}{2i}e^{i(\sigma A+\tau B)},
\tag{169.R25}
\]

the complete coefficient of an exponential branch is

\[
\frac{\sigma\,g(a,b)\chi_4(r)}{2iab},
\tag{169.R26}
\]

and its phase is (169.R7).  Put \(u=x^2\), \(v=y^2\).  On the only possible stationary branch,

\[
\Psi_{-,-}(x,y)
=Jxy-\frac r{4a}x^2-\frac k b y^2,
\tag{169.R27}
\]

whose Hessian is

\[
\begin{pmatrix}
-r/(2a)&J\\ J&-2k/b
\end{pmatrix},
\qquad
\det=\frac{rk}{ab}-J^2.
\tag{169.R28}
\]

Thus (169.R8) is exact.  Equivalently, with
\(u=\rho e^\theta\), \(v=\rho e^{-\theta}\),

\[
\Psi_{-,-}
=\rho\left(J-\frac r{4a}e^\theta-\frac k b e^{-\theta}\right).
\tag{169.R29}
\]

Angular stationarity forces

\[
e^{2\theta_*}=\frac{4ak}{br},
\qquad
\Psi_{-,-}(\rho,\theta_*)
=\rho\left(J-\sqrt{\frac{rk}{ab}}\right).
\tag{169.R30}
\]

The cone only restricts \(\theta_*\) to a fixed interval; it does not remove the product collar.  On exact resonance the phase in \(\rho\) is constant for the full radial support.  Near it, the only radial frequency is
\(J-\sqrt{rk/(ab)}\).  Hence the signed geometry itself contains no radial square-root gain.

The physical convolution has \(n=ar\) and \(m=bk\) before dualization; since the literal support has \(n,m\asymp L\), only \(a,b\ll L\) are physically active.  After dualization stationarity requires dual indices of sizes \(r\asymp aJ\) and \(k\asymp bJ\), so their union reaches size \(JL\).  Any shorter expression that forgets the \(a,b\)-range or (169.R24) has dropped a restored length or power.

Even granting a smooth radial model, the favorable angular stationary-phase scale and radial-band length supplied in the statement packet give precisely (169.R9).  The coefficient cost (169.R13) and \(L^{2\eta}\) can be placed inside \(X^\varepsilon\) by choosing \(\eta\) only after \(\varepsilon\).  The remaining factor is

\[
\sqrt J=X^{1/4},
\tag{169.R31}
\]

which cannot be absorbed into \(X^\varepsilon\) for arbitrary requested \(\varepsilon>0\).  Equation (169.R9) is a capacity calculation, not a claimed upper or lower bound for the literal cardinal transform.  For the literal transform, a smooth-band identity with corrections below the target is itself absent.

Finally,

\[
X_4(s)X_4(1-s)=1,
\qquad
X_0(s)X_0(1-s)=1.
\tag{169.R32}
\]

Thus applying the two transforms a second time returns coefficientwise to the original \(L\zeta\) convolution, with the zeta zero mode restored as \(R_\zeta\), and with every \(g(a,b)\), including (169.R2), unchanged.  This exact involution is the self-return obstruction: the functional equation reorganizes the signed sum but does not by itself estimate it.

### 3.6. Consequence for the target

To reach (169.B6), one would now need a theorem giving \(\sqrt J\) cancellation in the single joint aggregate (169.R6), specifically across the discrete near-solutions of \(rk=abJ^2\), with coefficients (169.R26), literal cardinal weights, and the cone and endpoint conventions intact.  Neither the functional equations, the local algebra of \(G\), nor angular stationary phase supplies such a theorem.  Taking \(\ell^1\), Cauchy--Schwarz, or a positive moment at this point discards exactly the required signed correlation.  Therefore the proposed mechanism closes no fixed positive-power \(L\)-sector beyond what an independent trivial/polylogarithmic estimate might already cover.

## 4. First doubtful or unproved step

There is no doubtful step in the coefficient table, completed-function normalization, contour orientation, dual coefficient, Fourier constants, or phase calculation above.  The first unproved implication is

\[
\text{exact signed collar sum (169.R6)}
\quad\Longrightarrow\quad
\text{a gain of }\sqrt J.
\tag{169.R33}
\]

It fails as a consequence of phase geometry: on the \((-,-)\) branch and \(rk=abJ^2\), the radial phase in (169.R30) is exactly zero and the Hessian in (169.R28) has rank one.  Any gain must therefore come from a new arithmetic cancellation statement for the coupled coefficients \(g(a,b)\chi_4(r)\), not from the joint GL(1) transform.

There is also an earlier failure in any attempted smooth shortcut: the packet supplies no endpoint-lawful identity replacing the exact \(O(L^2)\)-cell cardinal interpolant by the favorable smooth radial model with an error \(O_\varepsilon(L^{3/2}X^\varepsilon)\).  Granting that missing replacement still leaves the independent \(\sqrt J\) obstruction (169.R9).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_signed_two_height_integral` | Pass.  (169.R19) is exactly (169.B5), and the four sums in (169.R3) remain one Mellin-ordered signed aggregate. |
| `G_local_coefficients_and_p2` | Pass.  The complete odd-prime table is (169.R1), and the exceptional two-adic branch is (169.R2). |
| `G_weighted_l1_eta_cost` | Pass.  The exact Euler product and its \(\asymp\eta^{-3}\) cost are (169.R13). |
| `zeta_completed_function_and_pole` | Pass.  (169.R16)--(169.R17) record conductor, parity, root number, pole, and the already-separated zero mode. |
| `chi4_completed_function_parity_root_number` | Pass.  (169.R14)--(169.R15) record odd parity, conductor \(4\), \(\tau=2i\), root number \(1\), and absence of a pole. |
| `joint_contour_orientation_and_gamma_factors` | Pass.  Both contours move independently upward from \(\alpha\) to \(-\eta\); (169.R5) gives both exact gamma quotients. |
| `exact_cardinal_cell_or_endpoint_lawful_replacement` | Pass for retention, fail for smoothing.  The exact \(\mathcal B\) is retained throughout; no smooth replacement or unquantified endpoint correction is used. |
| `dual_coefficients_phase_lengths_and_normalization` | Pass.  (169.R21), (169.R24), (169.R26), (169.R7), and (169.R8)--(169.R9) give the complete ledger. |
| `no_l1_over_G_or_dual_variables_before_joint_phase` | Pass.  (169.R13) justifies the starting expansion only; the dual limit is not absolutized before (169.R7). |
| `no_common_height_substitution` | Pass.  \(t_1,t_2\) and both contours remain independent. |
| `no_absolute_or_positive_moment_inflation` | Pass.  No pointwise or positive-moment estimate is presented as signed cancellation. |
| `arbitrary_real_centre_floors_stars_profiles_and_p2_branch` | Pass.  All geometric conventions stay inside the literal \(\mathcal B\), while the \(p=2\) coefficient remains explicit. |
| `target_sqrtJ_gain_and_epsilon_order` | Obstruction.  \(\eta\) is chosen after \(\varepsilon\), but (169.R31) remains and cannot be absorbed. |
| `statement_only_independence` | Pass.  Only the three artifacts listed in Section 6 were read; no source, proof-state, strategy, sibling, candidate, review, or synthesis artifact was used. |
| `false_unsigned_aligned_and_G_equals_one_controls` | Route fails the aligned control.  Setting \(G=1\) leaves (169.R27)--(169.R30) with \(a=b=1\), so the rank-degenerate collar is already present.  Replacing the arithmetic coefficient by an aligned unsigned coefficient can make the finite radial aggregate coherent; any positive-norm argument would be unable to distinguish that control from the desired signed case and therefore cannot supply (169.R33).  This is a proof-method falsification, not a claimed lower bound for the literal weight. |
| `downstream_scope_and_no_exponent_promotion` | Pass.  No downstream obligation or exponent is asserted. |
| `no_in_round_pivot` | Pass.  The report stops at the assigned joint-transform result and obstruction. |

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/blind_statement.md`.
3. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/briefs/blind_joint_transform_rederivation.md`.

No web source, numerical experiment, symbolic-computation output, earlier-round artifact, sibling report, shared state, strategy file, barrier packet, candidate, review, or synthesis was used.  The derivation is 100% algebraic/analytic.

## 7. Recommended state effect

**Retain** (169.R1)--(169.R8), (169.R17), and (169.R21)--(169.R32) as candidate evidence for an exact coefficient/functional-equation/self-return ledger.  **Reject** the claim that the joint two-height GL(1) transform alone proves (169.B6) or an owner-complete strict polynomial \(L\)-sector.  The state recommendation for the target is **no promotion/no change** until a separate endpoint-lawful signed product-collar estimate supplies the missing \(\sqrt J\).


# Round218 statement-only joint-radial derivation

## 1. Result: the localized estimate is true, with sharp normal dimension

**Verdict: GREEN for the abstract lemma in the supplied statement.**

The proposed estimate holds for fixed \(m\), every \(A\geq0\), and a bounded collection of sufficiently many amplitude seminorms. The resonant critical manifold has dimension \(m\), and its normal Hessian has rank \(m\). Consequently the resonant scale is \(\lambda^{-m/2}\), not \(\lambda^{-m}\). A smooth amplitude independent of \(\lambda\) attains the former scale.

In fact, write \(\rho_j=|\xi_j|\). The following global extension is valid without comparability conditions, for arbitrary \(\lambda_j\geq2\):

\[
\boxed{
 |J(\boldsymbol\lambda,\xi)|
 \leq C_{m,A}\|a\|_{C^{L}}
 \prod_{j=1}^m
 (\lambda_j+\rho_j)^{-1/2}
 (1+|\lambda_j-\rho_j|)^{-A},
 \qquad L=m(3\lceil A\rceil+12).
}
\tag{1}
\]

The displayed derivative count is sufficient, not optimized. The same norm also suffices for the leading asymptotics stated below. In the localized common-parameter range of the packet, (1) gives exactly its proposed estimate, up to constants depending on \(m,A\).

This is only an oscillatory-integral conclusion. No discrete or arithmetic application is asserted.

## 2. Exact statement, hypotheses, and stationary geometry

Let

\[
 \mathcal A=\{y\in\mathbb R^2:1<|y|<2\},\qquad
 a\in C_c^\infty(\mathcal A^m),\qquad
 \sigma_j\in\{-1,1\}.
\]

The amplitude can be complex and need not factor. The norm in (1) is the maximum of the suprema of all Cartesian partial derivatives of total order at most \(L\), for the extension of \(a\) by zero. Constants do not require a common positive distance of the support from the annulus boundaries: compact support eliminates boundary terms, and the fixed annulus controls coordinate changes and volumes.

Set

\[
 \Phi(y)=\sum_j\bigl(\sigma_j\lambda_j|y_j|-\xi_j\cdot y_j\bigr),
 \qquad J=\int a(y)e(\Phi(y))\,dy,
 \qquad e(t)=\exp(2\pi i t).
\]

The critical-point equations are separately

\[
 \sigma_j\lambda_j\frac{y_j}{|y_j|}=\xi_j.
\tag{2}
\]

There are no critical points unless \(\rho_j=\lambda_j\) for every \(j\). At full resonance put \(\omega_j=\xi_j/\lambda_j\in S^1\). The phase has the exact critical manifold

\[
 \mathcal C_{\sigma,\omega}
 =\{(\sigma_1r_1\omega_1,\ldots,\sigma_mr_m\omega_m):1<r_j<2\}.
\tag{3}
\]

It has dimension \(m\); only its intersection with the amplitude support contributes. The phase is zero on this manifold. The Cartesian Hessian is block diagonal, with blocks

\[
 \frac{\sigma_j\lambda_j}{r_j}(I-u_j u_j^{\mathsf T}),
 \qquad u_j=y_j/r_j.
\tag{4}
\]

Each block has one radial zero eigenvalue and one normal eigenvalue \(\sigma_j\lambda_j/r_j\). Thus the kernel of the Hessian is exactly the tangent space of (3), the normal rank is \(m\), and the normal signature is \(\sum_j\sigma_j\). Coinciding numerical values of radial frequencies do not alter this rank.

For a common \(\lambda\), the uniform leading asymptotic is

\[
\begin{split}
 J(\lambda,(\lambda\omega_j)_j)
 &=\lambda^{-m/2}e\!\left(\frac18\sum_j\sigma_j\right)
    \mathcal C_a(\sigma,\omega)
    +O_m\bigl(\|a\|_{C^{12m}}\lambda^{-m/2-1}\bigr),\\
 \mathcal C_a(\sigma,\omega)
 &=\int_{(1,2)^m}
   a(\sigma_1r_1\omega_1,\ldots,\sigma_mr_m\omega_m)
   \prod_j r_j^{1/2}\,d\mathbf r.
\end{split}
\tag{5}
\]

The coefficient and the \(e(\sum\sigma_j/8)\) factor use the packet's \(2\pi\) convention. No extra \(2\pi\) power occurs in (5).

At unequal resonant parameters the corresponding formula is

\[
 J(\boldsymbol\lambda,(\lambda_j\omega_j)_j)
 =\left(\prod_j\lambda_j^{-1/2}\right)
   \left[
    e\!\left(\frac18\sum_j\sigma_j\right)\mathcal C_a(\sigma,\omega)
    +O_m\!\left(\|a\|_{C^{12m}}\sum_j\lambda_j^{-1}\right)
   \right].
\tag{6}
\]

This error bound is uniform in all parameter ratios. It is an asymptotic relative to a nonzero leading coefficient when \(\min_j\lambda_j\to\infty\). No such asymptotic assertion is made if some parameters remain fixed.

## 3. Full derivation

### One angular branch as an exact radial symbol

It suffices first to consider a single variable, allowing all other variables to act as passive amplitude parameters. Suppose \(\lambda/2\leq\rho\leq2\lambda\), so \(\rho\geq1\). Rotate coordinates so that \(\xi=\rho\omega\), and write \(y=rR_\theta\omega\). The phase is

\[
 \sigma\lambda r-\rho r\cos\theta.
\tag{7}
\]

A fixed smooth angular partition consists of a neighborhood of (0), a neighborhood of \(\pi\), and a region separated from both. Write \(\tau=+1\) for the first stationary angular branch and \(\tau=-1\) for the second. Near its center \(\theta_\tau\), use

\[
 z=2\sin((\theta-\theta_\tau)/2),\qquad
 \cos\theta=\tau(1-z^2/2).
\tag{8}
\]

These changes of variable and their inverses have bounded derivatives on the chosen fixed patches. Including the polar Jacobian and the angular cutoff in \(F_\tau(r,z)\), the branch contribution is exactly

\[
 \int e((\sigma\lambda-\tau\rho)r)
   \left[\int F_\tau(r,z)e(\tau\rho r z^2/2)\,dz\right]dr.
\tag{9}
\]

For (t>0) the elementary Fresnel Fourier identity, with Fourier transform \(\widehat F(\eta)=\int F(z)e(-\eta z)dz\), is

\[
 \int F(z)e(\tau t z^2/2)\,dz
 =e(\tau/8)t^{-1/2}
   \int\widehat F(\eta)e(-\tau\eta^2/(2t))\,d\eta.
\tag{10}
\]

One may prove (10) first with Gaussian damping and then pass to the limit; rapid decay of the Fourier transform of the compact smooth amplitude justifies that limit. This is an elementary identity, not a literature import.

Consequently (9) is

\[
 \rho^{-1/2}\int b_\tau(r;\rho)
       e((\sigma\lambda-\tau\rho)r)\,dr,
\tag{11}
\]

where the exact symbol is

\[
 b_\tau(r;\rho)
 =e(\tau/8)r^{-1/2}
   \int\widehat F_\tau(r,\eta)
       e(-\tau\eta^2/(2\rho r))\,d\eta.
\tag{12}
\]

For every integer \(k\geq0\), this symbol satisfies

\[
 \max_{\ell\leq k}\|\partial_r^\ell b_\tau\|_\infty
 \leq C_k\|F_\tau\|_{C^{3k+2}}
 \leq C'_k\|a\|_{C^{3k+2}}.
\tag{13}
\]

Indeed, \(k\) radial derivatives generate at most \(k\) factors \(\eta^2/\rho\), with bounded powers of \(r^{-1}\). Since \(\rho\geq1\), the resulting Fourier integral is bounded by weighted integrals of \(\partial_r^\ell\widehat F_\tau\) with weight at most \((1+|\eta|)^{2k}\). Integrating by parts \(2k+2\) times in \(z\) gives an integrable bound. The sum of the radial and angular derivative orders is at most \(3k+2\). Passive-variable derivatives simply pass through the construction and add their orders to this count.

Crucially, (11)--(13) describe an exact branch integral, not a leading expansion with an uncontrolled remainder. This is what permits arbitrarily strong radial mismatch factors uniformly.

### Radial mismatch and the nonstationary angular region

Put \(q=\lceil A\rceil\). There are no radial endpoint terms because \(b_\tau\) is compactly supported in (1<r<2). Taking the direct bound for radial frequency of size at most one, and integrating by parts \(q\) times otherwise, gives

\[
 |J_\tau|
 \leq C_q\rho^{-1/2}\|a\|_{C^{3q+2}}
   (1+|\sigma\lambda-\tau\rho|)^{-q}.
\tag{14}
\]

For the branch \(\tau=\sigma\) the mismatch is \(|\lambda-\rho|\). For the other branch it is \(\lambda+\rho\). Thus both branch bounds imply

\[
 |J_\tau|
 \leq C_A\lambda^{-1/2}\|a\|_{C^{3q+2}}
       (1+|\lambda-\rho|)^{-A}.
\tag{15}
\]

On the remaining angular region, \(|\sin\theta|\geq c>0\). Angular integration by parts \(q+1\) times, using the derivative \(\rho r\sin\theta\) of the phase, gives

\[
 |J_{\mathrm{ang},0}|
 \leq C_q\rho^{-q-1}\|a\|_{C^{q+1}}.
\tag{16}
\]

Since \(\rho\asymp\lambda\) and \(|\lambda-\rho|\leq\lambda\) in the localized range, (16) is also bounded by the right side of (15). This handles every angular branch and the entire angular complement.

These arguments remain true with \(C^K\) norms in passive variables on the output, at the cost of \(K\) additional total amplitude derivatives. A safe one-variable loss is \(3q+6\); the theorem reserves \(3q+12\).

### Far and zero frequencies

If \(\rho\notin[\lambda/2,2\lambda]\), set \(S=\lambda+\rho\). On the fixed annulus,

\[
 |\nabla_y(\sigma\lambda|y|-\xi\cdot y)|
 \geq|\lambda-\rho|\geq S/3.
\tag{17}
\]

With \(g=\nabla_y(\sigma\lambda|y|-\xi\cdot y)\), the operator

\[
 \mathcal L=\frac{1}{2\pi i}\frac{g}{|g|^2}\cdot\nabla_y
\]

satisfies \(\mathcal L e(\sigma\lambda|y|-\xi\cdot y)=e(\sigma\lambda|y|-\xi\cdot y)\). Every fixed-order derivative of \(g/|g|^2\) is \(O(S^{-1})\), uniformly in the sign and frequency direction. Repeated adjoint integration by parts therefore gives, for any integer \(N\geq0\),

\[
 |J_{\mathrm{far}}|\leq C_N S^{-N}\|a\|_{C^N}.
\tag{18}
\]

This directly includes \(\xi=0\). Choosing \(N=q+1\) proves the one-variable version of (1) in the far region, since \(|\lambda-\rho|\leq S\) and \(S\geq2\). There is no need to define an angular direction when \(\rho=0\).

### Joint amplitudes and unequal parameters

For each \(j\), integrate in \(y_j\) using the applicable one-variable argument. It maps a \(C^{K+3q+12}\) amplitude in all remaining variables to a \(C^K\) function bounded by

\[
 C_A(\lambda_j+\rho_j)^{-1/2}
      (1+|\lambda_j-\rho_j|)^{-A}
\]

times the indicated amplitude norm. The phase splits over the variables, but the amplitude does not need to split. Fubini is justified by compact support. Iterating these operator bounds \(m\) times proves (1) with \(L=m(3q+12)\). It works with any mixture of local, far, and zero frequencies, and with arbitrary unequal parameter ratios.

### Leading term and its normalization

From (12), expanding the final exponential by \(e(u)=1+O(|u|)\), with the Fourier moments controlled as above, gives

\[
 b_\tau(r;\rho)
 =e(\tau/8)r^{1/2}a(\tau r\omega)
   +O(\rho^{-1}\|a\|_{C^4})
\tag{19}
\]

for a single branch; the cutoff equals one at its center. The same expansion holds with any fixed number of radial and passive-variable derivatives after increasing the amplitude derivative count. The \(r^{1/2}\) arises from the polar factor \(r\) multiplied by the angular stationary factor \(r^{-1/2}\).

Apply (19) in all variables. At full resonance the angular choice \(\tau_j=\sigma_j\) for every \(j\) has zero radial phase, and gives exactly the main term in (6). Any other angular sign vector has at least one radial frequency \(2\sigma_j\lambda_j\); one radial integration by parts in such a variable gains \(\lambda_j^{-1}\). Angular complements can be integrated by parts sufficiently often to give at least the same gain. Errors in (19) similarly contribute a factor \(\lambda_j^{-1}\) for at least one \(j\). Summing this finite collection of errors yields

\[
 O_m\!\left(\|a\|_{C^{12m}}
       \prod_j\lambda_j^{-1/2}\sum_j\lambda_j^{-1}\right),
\]

which proves (6), and hence (5). This proof also verifies the signature factor independently of an ambient-dimensional stationary-phase heuristic.

### Sharpness with a fixed amplitude

Fix the signs and the directions \(\omega_j\). Choose a nonnegative smooth amplitude supported in a small fixed neighborhood of a point of (3), positive at that point. This amplitude is independent of all parameters. Its restriction to the critical manifold is positive on an open radial set, so \(\mathcal C_a(\sigma,\omega)>0\). Equation (5) then gives

\[
 |J(\lambda,(\lambda\omega_j)_j)|
 \sim\mathcal C_a(\sigma,\omega)\lambda^{-m/2}.
\tag{20}
\]

This construction allows a joint nonproduct amplitude. Thus no universally stronger resonant decay power is available under the packet's assumptions.

## 4. First doubtful or unproved step

There is no remaining gap in the abstract bounds, stationary geometry, leading coefficient, or sharpness claim proved here. The Gaussian identity and integration-by-parts arguments above provide the needed uniformity rather than assuming it from an asymptotic expansion.

Two potential incorrect steps have been excluded explicitly:

1. Treating the phase as fully nondegenerate in (2m) dimensions would incorrectly predict \(\lambda^{-m}\). The \(m\) radial zero directions persist on the entire resonant critical manifold.
2. Taking only a leading angular expansion and then ignoring its radial-derivative remainder would not prove the product of arbitrarily strong mismatch factors. The exact symbols (11)--(13), followed by radial integration by parts, repair that potential omission.

No assertion about any downstream use of the lemma has been checked or supplied.

## 5. Required controls and exact analytical outcomes

All controls below are analytic. No experiment, numerical evaluation, or symbolic computation was run.

| Control | Outcome |
|---|---|
| (m=1) | The stationary set is a ray segment; one nonzero normal eigenvalue gives \(\lambda^{-1/2}\). For radial (a(y)=h(|y|)), the main coefficient is \(e(\sigma/8)\int h(r)\sqrt r\,dr\), agreeing directly with the two angular branches. |
| Mixed signs | The resonant ray in variable \(j\) is \(\sigma_j\omega_j\), and the signature is \(\sum\sigma_j\). All bounds are uniform over the signs; no positivity of the phase is used. |
| Joint nonproduct amplitude | Parameter-dependent one-variable operator bounds and total derivative norms prove the product estimate. No factorization or probabilistic independence is assumed. |
| Coincident radial frequencies | Equal values of \(\rho_j\), including full equality at resonance, introduce no extra degeneracy because different variables occupy separate Hessian blocks. |
| All angular branches | Both stationary angular branches in every variable are retained. The opposite branch has radial frequency of magnitude \(\lambda_j+\rho_j\), and every angular complement is covered by (16). |
| Radial boundaries | Smooth compact support in the open annuli makes every radial endpoint term zero, even if a bounded family of supports approaches the annulus boundaries. |
| Small mismatch | For \(|\lambda_j-\rho_j|\leq1\), the direct radial bound gives the required \(\lambda_j^{-1/2}\) factor with no division by zero. |
| Large local mismatch | Radial integration by parts yields arbitrary prescribed powers of the mismatch uniformly up to the comparability endpoints. |
| Far or zero frequency | The gradient lower bound (17) gives arbitrary inverse powers of \(\lambda_j+\rho_j\). At \(\xi_j=0\), radial oscillation remains nonstationary; no angular stationary-phase estimate is required. |
| Unequal parameters | Equation (1) has no ratio restrictions. Equation (6) is uniform and becomes a leading asymptotic when every parameter tends to infinity. |
| Vanishing amplitude | The zero amplitude gives (J=0). If the amplitude vanishes on the resonant manifold, the displayed leading coefficient is zero and (5) gives the stated next-order bound; a vanishing leading coefficient is not a lower-bound claim. If its support stays away from the critical manifold, ordinary full-gradient integration by parts gives rapid decay for fixed resonant directions. |
| Fixed amplitude sharpness | The positive bump construction gives (20) for all sufficiently large resonant \(\lambda\), not merely an amplitude adapted at each scale. |
| Fixed versus growing \(m\) | The proof is for fixed \(m\). The displayed derivative count grows linearly in \(m\); constants can grow with \(m\), and the number of angular sectors grows exponentially. No uniform growing-dimension statement is asserted. |

The uniformity over a bounded amplitude family is in the displayed finite \(C^L\) norm. Allowing parameter-dependent amplitudes with unbounded derivatives would be a different statement and is not covered.

## 6. Dependencies, exact artifacts, and provenance

- Campaign: `gc-complete-signed-radical-kernel`, round218.
- Task and role: `blind_joint_radial`, independent statement-only derivation of the new abstract lemma.
- Generated date: 2026-09-28.
- Graph hash supplied in the packet as metadata: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. The graph was not read or reverified for this assignment.
- Only task-context files read:
  - `protocol.md`, SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
  - `rounds/codex-managed/gc-complete-signed-radical-kernel/briefs/blind_joint_radial_statement.md`, SHA256 `1211b43b9aec8993d53f7ddfd47c05c4877bab1df1671a46179f5903f35ce632`.
- Mathematical tools: polar coordinates, a fixed angular partition, the explicit quadratic change (8), the elementary Fresnel Fourier identity (10), Fourier integration by parts, ordinary nonstationary integration by parts, and Fubini for compactly supported integrals.
- No external source, web page, application, graph, campaign manifest, strategy, claimant derivation, sibling report, or current arithmetic application was read for this task. No new agent was launched. Only the assigned report was written.

**Isolation disclosure.** This agent slot retains prior round217 full-frontier/source-review and mathematical seam context. It is therefore not a fresh history-free agent. The round218 derivation is statement-only with respect to this new joint-radial lemma: no current claimant argument or arithmetic application was supplied or inspected, and no historical artifact was reread for this assignment.

## 7. Recommended state effect

**Recommend promote, subject to the conductor's independent seam and graph procedures, only the exact abstract localized bound, its global unequal-parameter extension (1), and the stationary-manifold/asymptotic/sharpness statements (3)--(6), (20).**

The packet's localized estimate needs no correction. Its correct interpretation is normal stationary phase of rank \(m\), with radial mismatch handled separately. All constants here are for fixed \(m\) and controlled amplitude derivatives.

No state mutation, downstream arithmetic conclusion, current-round synthesis, or successor decision is made in this report. The assigned task ends with this report.

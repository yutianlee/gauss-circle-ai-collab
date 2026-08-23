# Round 125 conductor adjudication: one-sided dual energy and sectorization no-go

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

## Decision

Promote the endpoint-complete full-character block-energy identity and its
one-sided sign localization. Promote a separate scoped obstruction for
coefficient-blind sector splitting, the best elementary fixed-row
curvature bound, and the strict-interior reciprocal self-return after the
half-integer alias correction.

Do not promote the required upper estimate, either separate sector at the
square target, an endpoint-complete hard-block B-process, or the proposed
exact/far/near second-stage decomposition. The flat-smooth strict-UNBAL
lane is parked at one positive full-character energy, and the strategy
rotates to another mandatory M2 parent.

## Exact joint block energy

For the literal zero-extended rows, put

$$
 B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a},\qquad
 \mathcal E_{\rm eq}=C_H\sum_{p,n}|B_{p,n}|^2,
$$

$$
 \mathcal E_\chi=C_H\sum_n
 \left|\sum_{p>0\atop p\text{ odd}}\chi_4(p)B_{p,n}\right|^2.
\tag{125.R1}
$$

Direct finite expansion, with no boundary remainder, gives

$$
 \mathcal E_{\rm eq}=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0},
 \qquad
 \mathcal E_\chi=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 +\mathcal S_{\rm neq}.
\tag{125.R2}
$$

Consequently

$$
 \mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0,
 \qquad
 \mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}.
\tag{125.R3}
$$

The blind, discovery, and hostile reports independently agree on these
identities. Negative shifts are paired with their ordered conjugates only
to establish reality. Since both energies and the diagonal are
nonnegative and

$$
 \mathcal D_0\ll X^{1/2},
\tag{125.R4}
$$

one has

$$
 \mathcal S_{\rm off}\ge-\mathcal D_0,
 \qquad
 |\mathcal S_{\rm off}|
 \le\max\{\mathcal E_\chi,\mathcal D_0\}.
\tag{125.R5}
$$

Therefore the desired absolute estimate for the complete off-product
scalar is equivalent at target scale to the single upper estimate

$$
 \boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.R6}
$$

Combining (125.R3) with the accepted Round-124 physical identity yields

$$
 \mathcal V_{M,H}=\mathcal E_\chi-\mathcal Q_{\rm safe}+O(1),
 \qquad
 \mathcal Q_{\rm safe}\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{125.R7}
$$

Thus any fixed-power failure of the physical flat-smooth survivor is
necessarily on its positive side and is exactly a fixed-power excess of
the endpoint-complete energy (125.R1), modulo proved packages. This is a
strict sign localization, not the missing upper bound.

## Why the two sectors must remain together

Equation (125.R3) shows that the entire positive fixed-mode energy can
cancel between the equal-mode shifted and unequal-mode sectors. The blind
report gives a sharp coefficient control. Choose odd modes
$r\equiv1\pmod4$, $s\equiv3\pmod4$, put
$b_{r,k}=b_{s,k}=c_k$, and set every other row to zero. If

$$
 E_0=\sum_k|c_k|^2,\qquad
 E_H=\sum_n\left|\sum_{a<H}c_{n+a}\right|^2,\qquad
 R_c=\frac{E_H}{HE_0},
$$

then the exact Fejer algebra gives

$$
 \mathcal D_0=2C_HHE_0,\qquad
 \mathcal S_{\rm eq}^{\ne0}=(R_c-1)\mathcal D_0,
$$

$$
 \mathcal S_{\rm neq}=-R_c\mathcal D_0,
 \qquad
 \mathcal S_{\rm off}=-\mathcal D_0.
\tag{125.R8}
$$

A smooth long plateau has $R_c\ge H/4$. Hence each separate sector can
be larger than the target by the fixed-power factor $H$, while their
required sum is target-safe. This is not a counterexample to the literal
phase/profile array. It is a rigorous no-go for any inference using only
Fejer positivity, coefficient sizes, support, zero extension, and
$|\chi_4|=1$. A predetermined separate-sector target estimate is a
strictly stronger route and cannot replace (125.R6) without an actual
phase theorem.

## Complete elementary fixed-row bound

For $f_p(k)=\sqrt{Mpk}$, on every active support component

$$
 f_p'(k)\asymp D,\qquad |f_p''(k)|\asymp D/K.
$$

The nonoscillatory amplitude has supremum and total variation

$$
 \ll \beta X^\varepsilon,\qquad
 \beta=X^{1/4}K^{-3/4}L^{-3/4}.
$$

The elementary second-derivative estimate, partial summation, and the
trivial bound give uniformly for literal support intersections

$$
 |B_{p,n}|\ll_\varepsilon \beta X^\varepsilon
 \min\left\{H,H\sqrt{D/K}+\sqrt{K/D}\right\}
 \ll_\varepsilon \beta X^\varepsilon
 \min\{H,\sqrt{D/L}\}.
\tag{125.R9}
$$

Summing the $O(LK)$ rows and block positions with $C_H\asymp L$
proves the endpoint-complete estimate

$$
 \boxed{
 \mathcal E_{\rm eq}
 \ll_\varepsilon X^\varepsilon
 \min\left\{\frac XD,\frac{D^2}{L}\right\}
 =X^{1/2+\varepsilon}\min\{H,Q\}.}
\tag{125.R10}
$$

Here

$$
 Q=\frac{D^2}{L\sqrt X}\to\infty,\qquad H\to\infty.
$$

Thus (125.R10) is a genuine complete bound but not the square target. The
often quoted $Q$-deficit applies only when $Q\le H$, equivalently
$K/D\ge1$ or $3\delta\le1+\ell$. In the complementary regime the
original $H$-term triangle is better. The uniform elementary deficit is
$\min\{H,Q\}$, not always $Q$.

## Reciprocal principal packet and corrected alias

On a fixed central block interior, Poisson in $k$ has saddles

$$
 x_{p,d}=\frac{Mp}{4d^2},\qquad
 f_p(x_{p,d})-dx_{p,d}=\frac{Mp}{4d},\qquad
 f_p''(x_{p,d})=-\frac{2d^3}{Mp}.
$$

The existing $e(-1/8)$ and the negative Gaussian unit combine with the
Hessian amplitude to give exactly $-2i/p$, and the moving profile becomes
$W(Xd/(DM))q_L((X/M)p)$. Hence the central principal packet is

$$
 B_{p,n}^{\rm prin}=-\frac{2i}{p}q_L((X/M)p)
 \sum_{d\in I_{p,n}}W\!\left(\frac{Xd}{DM}\right)
 e\!\left(\frac{Mp}{4d}\right),
 \qquad |I_{p,n}|\asymp Q.
\tag{125.R11}
$$

When $K/D<1$, these are $Q>H$ continuous dual labels, not $Q$
nonempty primal lattice cells. A second strict-interior B-process returns
the original phase, coefficient, profile, and selector. The reciprocal
diagonal has capacity $KQ=X^{1/2}$, reciprocal Cauchy loses $Q$, and
primal Cauchy loses $H$. These are capacity diagnostics, not lower
bounds.

For a $d,d'$ pair put $\Delta=d'-d$. Since the subsequent mode sum is
over odd $p$, coherence is modulo $\tfrac12\mathbb Z$. If $A$ is a
nearest integer to $M\Delta/(2dd')$ and

$$
 E_d^*=M\Delta-2Add',
$$

then

$$
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 =(-1)^A e\!\left(\frac{pE_d^*}{4dd'}\right),
 \qquad
 (M-2Ad)(M+2Ad')-M^2=2AE_d^*.
\tag{125.R12}
$$

The former $4a$ lattice sees only even $A$ and is rejected. More
decisively, at fixed $(n,d,d')$ the literal saddle selectors leave a
$p$-interval of length

$$
 \asymp D^2H/X\asymp1/H,
\tag{125.R13}
$$

not $L$. Summing $n$ first creates the moving floor multiplier

$$
 \#\{n:n<x_{p,d},x_{p,d'}<n+H\},
\tag{125.R14}
$$

whose faces and aggregate error are not target-safe in the supplied
argument. Therefore the proposed far summation and nonzero-near defect
survivor are not proved. Formula (125.R11) itself also lacks an aggregate
hard-face, Fresnel-transition, inactive-mode, and remainder ledger, so it
is promoted only as a strict-interior method diagnostic.

## Seam adjudication

| Seam | Decision |
|---|---|
| Exact Fejer and full-character energies | Green, endpoint-complete, independently reproduced. |
| Negative off-product side | Green and target-safe by positivity plus the diagonal. |
| Positive upper side | Open; exactly (125.R6). |
| Separate equal/unequal sectors | Red as a necessary decomposition; coefficient-blind versions are overstrong by $H$. |
| Complete fixed-row elementary bound | Green at $X^{1/2+\varepsilon}\min(H,Q)$, not at target. |
| Curvature and crossing regimes | Green after distinguishing dual labels from nonempty primal cells. |
| Principal saddle constant and profile | Green on fixed interiors only. |
| Second B-process | Green as a strict-interior self-return, not a complete transform. |
| Second-stage alias lattice | Green only after the half-integer correction (125.R12). |
| Fixed-$(n,d,d')$ $p$-sum | Red: its length is $O(1/H)$, not $L$. |
| Moving overlap and endpoints | Open; no target-safe aggregate ledger. |
| Capacity | Green as an unsigned diagnostic only. |
| Downstream scope | Green: one flat-smooth strict-UNBAL owner only. |

## First remaining gap and route decision

The exact parked survivor is (125.R6) with every character, moving
profile, block face, entry, exit, and zero-extended value retained before
the modulus. No smaller endpoint-complete sector or reciprocal defect
functional is target-equivalent.

Round 125 was the final bounded continuation authorized for this UNBAL
mechanism. It produced a strict sign localization and a sharp
sectorization no-go, but no upper contraction. Re-Poissonization,
cellwise Cauchy, a separate positive-row norm, the $4a$ defect, and a
predetermined sectorwise target are parked. Reopen this lane only with a
genuinely joint actual-character inequality for (125.R6), or an
endpoint-complete stronger inverse theorem.

The strategy now rotates to hard TOP or BAL. The flat-smooth strict-UNBAL
estimate, all other UNBAL owners, hard TOP, BAL, complete M9-M2, both M1
routes, endpoint uniformity, M9, the quarter theorem, and every exponent
improvement remain open.

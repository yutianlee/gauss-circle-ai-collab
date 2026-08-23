# Round 125 synthesis: the UNBAL survivor is one positive actual-character energy

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

## Frozen objective

The round tested the exact Round-124 dual off-product aggregate

$$
 \mathcal S_{\rm off}
 =\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
$$

at the square target $X^{1/2+\varepsilon}$, with the literal moving
profiles, exact Fejer triangle, zero extension, both shift signs, ordered
conjugates, and $\chi_4(p)\chi_4(q)$ retained.

## Exact one-sided reduction

Let

$$
 B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a},\qquad
 \mathcal E_{\rm eq}=C_H\sum_{p,n}|B_{p,n}|^2,
$$

$$
 \mathcal E_\chi=C_H\sum_n
 \left|\sum_{p>0\atop p\text{ odd}}\chi_4(p)B_{p,n}\right|^2.
$$

Exact finite expansion gives

$$
 \mathcal E_{\rm eq}=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0},
 \qquad
 \mathcal E_\chi=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 +\mathcal S_{\rm neq}.
\tag{125.1}
$$

Therefore

$$
 \mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0,
 \qquad
 \mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}.
\tag{125.2}
$$

Since $\mathcal E_\chi\ge0$ and
$\mathcal D_0\ll X^{1/2}$, the negative side of
$\mathcal S_{\rm off}$ is already target-safe. The full target is
equivalent to the single positive upper estimate

$$
 \boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.3}
$$

The Round-124 physical connector now simplifies to

$$
 \mathcal V_{M,H}=\mathcal E_\chi-\mathcal Q_{\rm safe}+O(1),
 \qquad
 \mathcal Q_{\rm safe}\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{125.4}
$$

Thus every fixed-power physical violation is positive and is precisely a
fixed-power excess of (125.3), modulo proved packages. All three reports
independently reproduce the endpoint-complete block algebra.

## Sectorization is coefficient-blindly overstrong

The identity
$\mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}$
shows that the entire positive fixed-mode energy can cancel between the
two named sectors. The blind report makes this sharp. Two identical
zero-extended rows on opposite $\chi_4$-classes can satisfy

$$
 |\mathcal S_{\rm eq}^{\ne0}|\gg H\mathcal D_0,
 \qquad
 |\mathcal S_{\rm neq}|\gg H\mathcal D_0,
 \qquad
 \mathcal S_{\rm off}=-\mathcal D_0.
\tag{125.5}
$$

This is an exact smooth coefficient adversary, not a counterexample to the
literal physical array. It proves that separate target bounds cannot
follow from Fejer positivity, coefficient sizes, support, zero extension,
or character magnitudes alone. The actual phase/profile interaction must
be used before any sectorwise norm.

## Best elementary positive-row bound

For $f_p(k)=\sqrt{Mpk}$, one has
$|f_p''|\asymp D/K$. The trivial and elementary second-derivative
estimates, with the literal amplitude variation, give the complete bound

$$
 \boxed{
 \mathcal E_{\rm eq}
 \ll_\varepsilon X^\varepsilon
 \min\left\{\frac XD,\frac{D^2}{L}\right\}
 =X^{1/2+\varepsilon}\min\{H,Q\}.}
\tag{125.6}
$$

Both $H$ and $Q=D^2/(L\sqrt X)$ tend to infinity. Thus (125.6)
does not reach the target. It corrects the regime ledger: the reciprocal
$Q$-loss is best only for $Q\le H$; for $Q>H$, the original
$H$-term triangle is smaller.

## Principal reciprocal packet and fatal seams

On fixed block interiors, the $k$-B-process has

$$
 x_{p,d}=\frac{Mp}{4d^2},\qquad
 f_p(x_{p,d})-dx_{p,d}=\frac{Mp}{4d},
$$

and exact principal coefficient $-2i/p$. The returned profile is
$W(Xd/(DM))q_L((X/M)p)$, so

$$
 B_{p,n}^{\rm prin}=-\frac{2i}{p}q_L((X/M)p)
 \sum_{d\in I_{p,n}}W\!\left(\frac{Xd}{DM}\right)
 e\!\left(\frac{Mp}{4d}\right),
 \qquad |I_{p,n}|\asymp Q.
\tag{125.7}
$$

A second strict-interior B-process returns the original block. When
$Q>H$, the $Q$ dual labels are not $Q$ nonempty primal lattice
cells. The reciprocal diagonal is target-sized, but Cauchy loses $Q$;
the primal chart loses $H$. Inversion supplies no estimate.

The proposed second-stage lattice also required correction. For
$\Delta=d'-d$, odd-$p$ coherence is modulo
$\tfrac12\mathbb Z$. With $A$ nearest
$M\Delta/(2dd')$ and $E_d^*=M\Delta-2Add'$,

$$
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 =(-1)^Ae\!\left(\frac{pE_d^*}{4dd'}\right),
 \qquad
 (M-2Ad)(M+2Ad')-M^2=2AE_d^*.
\tag{125.8}
$$

The former $4a$ variables omit every odd half-integer alias. Even after
this repair, fixing $(n,d,d')$ leaves a $p$-window of length
$D^2H/X\asymp1/H$, not $L$. Summing $n$ first introduces a
moving floor overlap whose hard faces and aggregate error remain
uncontrolled. Hence neither far summation nor a complete nonzero-near
defect survivor is proved. Formula (125.7) itself remains a
strict-interior principal module, not an endpoint-complete transform.

## Decision and full-proof status

Promote the exact one-sided energy reduction, the complete elementary
positive-row bound, and the scoped sectorization/reciprocal-packet no-go.
Reject the $4a$ alias, a universal $Q$-only deficit, a fictitious
length-$L$ fixed-$(n,d,d')$ sum, an endpoint-complete packet claim,
and any inference from separate positive rows to the actual target.

The exact parked UNBAL survivor is (125.3). Round 125 supplies no upper
contraction, so the August 21 stop rule activates: rotate to hard TOP or
BAL and reopen this UNBAL lane only for a genuinely joint actual-character
inequality or an endpoint-complete stronger inverse theorem.

The flat-smooth strict-UNBAL estimate remains open, and all nonflat, hard,
sharp, clipped, starred, arithmetic-owner, and transition UNBAL packets
remain separate. Hard TOP, BAL, complete M9-M2, both direct M1 parents,
the lower GAR alternative, endpoint uniformity, M9, and the pointwise
quarter theorem remain open.

The internal global exponent remains $1/3$. The audited external
benchmark remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
$$

Round 125 proves no global exponent improvement.

Resulting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`.

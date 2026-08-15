# Round 52 synthesis: the height floor is discrete, not an alpha seam

## 1. Result

Round 52 closes the first undefined object isolated in Round 51.  The
Vaaler height (H_j=\lfloor D_jX^{-1/4}\rfloor) is fixed while the contour
heights move and hence has zero alpha/beta contour velocity.  It creates no
moving-face delta in the alpha Cauchy--Green ledger.

For the exact family

\[
 a_H(h)=\mathbf1_{1\le h\le H}\Phi\!\left(\frac h{H+1}\right),
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\]

the lawful discrete comparison is

\[
 a_{H+1}(h)-a_H(h)=
 \begin{cases}
 \Phi(h/(H+2))-\Phi(h/(H+1)),&h\le H,\\
 \Phi((H+1)/(H+2)),&h=H+1,\\
 0,&h>H+1.
 \end{cases}
\]

Every nonzero term is positive and

\[
 \sum_h|a_{H+1}(h)-a_H(h)|=\frac12,
 \qquad
 \sum_h\frac{|a_{H+1}(h)-a_H(h)|}{h}
 \sim\frac1{H+1}.
\]

The new endpoint is (\asymp H^{-2}); the bulk retuning of old
frequencies supplies almost all of the unweighted mass.  More generally,
the discovery report proves the sharp pointwise bound

\[
 a_{H+1}(h)-a_H(h)asymp
 \frac{h^2(H+2-h)}{(H+1)^4}
\]

and the full power-weighted norm law.

## 2. Actual-scale obstruction

An adjacent dyadic block does not change (H) by one.  Exactly,

\[
 H_{j+1}=\left\lfloor\frac{H_j}{2}\right\rfloor.
\]

For integers (K,H\), monotonicity and
(sum_{h\le H}a_H(h)=H/2) give

\[
 \|a_K-a_H\|_1=\frac{|K-H|}{2}.
\]

Thus the coefficient-only part of an actual dyadic change is
(\asymp H_j) unweighted and (\asymp1) after (1/h).  The complete
difference also changes (D_j), the dyadic profile, support, equality star,
Mellin scale powers, radial factors, and external normalization.  At finite
height, ((H+1)^v) supplies an additional bulk obstruction.  No accepted
signed partial-sum theorem controls this coupled family.

## 3. State decision

Promote:

1. zero contour velocity and the no-floor-connector conclusion;
2. the exact adjacent-height identity, endpoint taper, and sharp weighted
   norms;
3. the exact dyadic height relation and long-height capacity obstruction.

Reject:

1. treating (H_j) as a moving alpha-contour seam;
2. using the (O(H^{-1})) unit increment as the size of an actual dyadic
   change;
3. inferring alpha lattice cancellation from coefficient-only height
   variation.

The connector-completed alpha transition, outside-height limit, global
arithmetic sum, GAR, M9-M1, M9, and the Gauss-circle target remain open.

## 4. Next interface

Freeze the exact coupled difference between two neighboring physical
dyadic scales on a common positive-line alpha antecedent.  Construct one
owner table for both profiles, supports, stars, height factors, radial
terms, and external normalization.  Then prove a signed scale-partial-sum
bound or a sharp capacity obstruction.  Do not return to continuous seam
incidence for the floor.

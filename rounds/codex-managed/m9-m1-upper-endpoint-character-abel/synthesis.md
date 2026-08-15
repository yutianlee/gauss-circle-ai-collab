# Round 23 synthesis: period-four Abel summation closes the physical upper endpoint

Campaign: `m9-m1-upper-endpoint-character-abel`  
Round type: upper-endpoint character Abel  
Graph SHA-256 before patch: `eca71399b98ecaf53de8b04594af6046f07d0bbcd0c3683b6b57c51c8bc3cf7b`

## Conductor decision

Promote the fixed-scale sampled-BV lemma, the period-four character-Abel
estimate, and the resulting target-sized physical upper radial endpoint.
All three reports independently agree on the character variable, support,
top jump, product star, height floors, scale sum, and external
\(X^{1/4}\) normalization. Retain arbitrary finite top Mellin truncations,
the recombined \(R_1\) arithmetic residue, both diagonal transition traces,
GAR, M9-M1, M9-M2, M9, and the Gauss-circle target as open.

This round used no numerical experiment and no external theorem. Its effort
allocation was 100 percent analytical/algebraic.

## Exact physical endpoint

Let

\[
 y=\lfloor\sqrt X\rfloor,\qquad D_j=2^{-j}y,\qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor,\qquad
 N=N_X=\lfloor16\sqrt X\rfloor.
\]

For the active scales, put

\[
 Q_j(h)=\frac{Xh}{D_j^2},\qquad
 t_{j,h}(q)=2\sqrt{\frac{Q_j(h)}q}.
\]

The accepted symmetric physical-profile limit of the upper endpoint is,
up to the unimodular phase \(e(\sqrt{XN})\),

\[
 \mathcal U_X=
 \sum_j\sum_{1\le h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)h^{-3/4}
 \sum_{q\ge1}\chi_4(q)a_{j,h}(q),
 \tag{23.1}
\]

where

\[
 a_{j,h}(q)=q^{-3/4}W(t_{j,h}(q))\kappa_N(hq)
 \begin{cases}
  \kappa_0(t_{j,h}(q)),&j=0,\\
  1,&j\ge1,
 \end{cases}
 \tag{23.2}
\]

\(\kappa_N(n)=1,1/2,0\) according as \(n<N,n=N,n>N\), and
\(\kappa_0(t)=0,1/2,1\) according as \(t>1,t=1,t<1\).
Thus (23.2) retains both independent stars and the hard top
\(d=y\) convention.

## Fixed-scale sampled variation

For \(j\ge1\), the uncut profile is supported on

\[
 \frac94Q_j(h)\le q\le16Q_j(h),
\]

while the hard top restricts this to

\[
 4Q_0(h)\le q\le16Q_0(h).
\]

Because \(D_j\le y\), one has \(Q_j(h)\ge h\ge1\). On the smooth part,
the change of variables \(r=q/Q_j(h)\) writes the sequence as
\(Q_j(h)^{-3/4}\psi(r)\), with a fixed compactly supported BV profile.
Sampling a monotone argument cannot increase continuum variation. The top
projector and product projector are each monotone sequences of variation
one, and their possible half ties change the bound only by the size of one
sample. Consequently

\[
 \boxed{
 \|a_{j,h}\|_{\ell^\infty}
 +\sum_{q\ge1}|a_{j,h}(q+1)-a_{j,h}(q)|
 \ll_W Q_j(h)^{-3/4}.}
 \tag{23.3}
\]

The product support is in fact automatic away from its possible tie: on
profile support,

\[
 q\le16Q_j(h),\qquad h\le D_jX^{-1/4}
 \quad\Longrightarrow\quad hq\le16\sqrt X,
\]

and integral \(hq\) is therefore at most \(N_X\).

## Character Abel estimate and complete sum

Period four gives

\[
 \sup_T\left|\sum_{q\le T}\chi_4(q)\right|\le1.
\]

Discrete Abel summation with (23.3) proves

\[
 \boxed{
 \sum_{q\ge1}\chi_4(q)a_{j,h}(q)
 \ll_W Q_j(h)^{-3/4}.}
 \tag{23.4}
\]

Since the fixed Vaaler profile \(\Phi\) is bounded,

\[
 \begin{aligned}
 |\mathcal U_X|
 &\ll_W X^{-3/4}\sum_jD_j^{3/2}
       \sum_{h\le H_j}h^{-3/2}\\
 &\ll_W X^{-3/4}y^{3/2}\sum_{j\ge0}2^{-3j/2}
 \ll_W1.
 \end{aligned}
 \tag{23.5}
\]

Restoring the exact active-M1 factor gives

\[
 -\frac4\pi X^{1/4}\operatorname{Re}
 \{e(1/8)e(\sqrt{XN})\mathcal U_X\}
 =O_W(X^{1/4}).
 \tag{23.6}
\]

Thus the physical upper endpoint is target-sized, and in fact has no
logarithmic loss beyond the external normalization.

## Scope and hostile controls

The proof uses the actual placement \(\chi_4(q)\). Replacing the character
by unsigned coefficients changes a fixed-scale mass from
\(O(Q^{-3/4})\) to capacity \(\asymp Q^{1/4}\); hence the argument does not
prove the known-false unsigned analogue. It also does not move the character
to the height variable.

At finite top Mellin height, the inverse transform of the one-sided top
profile has noncompact Perron tails, and no uniform sampled-BV theorem for
that intermediate kernel has been proved. Promotion is therefore confined
to the accepted physical symmetric-profile limit. For each fixed \(X\),
that limit is already licensed and the resulting sums are finite.

## State effect

- promote the fixed-scale sampled-BV and \(\chi_4\)-Abel lemma;
- promote the physical upper radial endpoint-prefix estimate;
- reject automatic extension of the estimate to arbitrary finite top
  Mellin truncations;
- record that both physical radial endpoints are now target-safe;
- retain the recombined \(R_1\) arithmetic residue and both diagonal
  transition traces as the unresolved endpoint/vector package;
- isolate that residue as `M9-M1-R1-arithmetic-residue`, the next exact
  proof obligation;
- leave GAR, M9-M1, M9-M2, M9, and the final target open.

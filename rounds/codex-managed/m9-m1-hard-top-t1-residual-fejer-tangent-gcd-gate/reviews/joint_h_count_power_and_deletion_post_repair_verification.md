# Round 185 post-repair joint-\(h\), power, and deletion verification

## 1. Result / verdict

**Verdict: GREEN.**

The repaired candidate has the exact hash frozen in the brief.  The
repaired exact control also has its frozen hash.  Independently
recomputing (185.C13)--(185.C31) and (185.C38)--(185.C39) confirms every
counting power, both cross orientations, the primitive-domain
conditions, affine-row multiplicity, polylogarithmic coefficient
rebudgeting, and the explicit \(\gamma^{-1}\) and \(\delta^{-1}\)
dependence.  The canonical representatives and oriented index sets in
(185.C32)--(185.C36) exactly repair the prior row-duplication and
orientation-contamination defects without changing any count.

The stronger tuple \((103,7,1,99,14)\) was reproduced by exact integer
arithmetic and is correctly located at canonical plus indices
\(t=14,15\).  Its conclusion is limited, as required, to failure of
automatic no-pair arithmetic-support invariance.

## 2. Exact statement and hypotheses

Fix \(X\geq2\), a nonempty literal middle or lower hard-M1 shell
\(L\geq2\), \(\sigma\in\{\pm1\}\), and
\(R_0=\lceil L\rceil\).  At an opened positive even shift
\(r=2q<R_0\), write

\[
 N=dm,\qquad N+r=d'm',
\]

where a nonzero pair of zero-extended \(\lambda\)'s enforces positivity,
oddness of \(d,d'\), squarefreeness of both products, coprimality of the
two original allocations, the hard cone, shell, selector, profile, and
all endpoint predicates.  On support,
\(d,d',m,m'\asymp L\), and each endpoint coefficient is
\(O_\varepsilon(X^\varepsilon)\).

For an opposing incidence, the repaired primitive outer label is

\[
 \mathfrak f=(\kappa,g,h,U,v),
\]

subject to

\[
 \kappa,g,h,U,v\in\mathbb Z_{>0},\quad
 \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad (U,h)=1,\quad
 0<2\kappa gh<R_0.
\]

For each orientation there is exactly one canonical affine base
representative, and its row is restricted to

\[
 I_{\mathfrak f,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0, w_{t,\omega}>0\}.
\]

The claims verified are: fixed-\(g\) and fixed-\(\kappa\) tails;
\(g=(d,d')=(u,s)=(u,n)\); \(r=2\kappa gh\); the
\(O(L^2/(\kappa g))\) fixed-\((\kappa,g,h)\) count; the
\(O(HL^2\log^2(2L))\) bounded-\(h\) count; (185.C30)--(185.C31);
the exact oriented complement; and the row-capacity controls
(185.C38)--(185.C39).

## 3. Proof or line audit

### Original gcd and inward cross gcd

For \(g=(d,d')\), writing \(d=gu\), \(d'=gv\) gives
\((u,v)=1\) and

\[
 vm'-um=\frac rg.
\]

At fixed \(g\), there are \(O((L/g)^2)\) choices of \((u,v)\),
\(O(L/g)\) choices of \(r/g\), and \(O(g)\) solutions in the physical
\((m,m')\)-box because the homogeneous step is \((v,u)\asymp L/g\).
Thus the count is \(O(L^3/g^2)\), and

\[
 \sum_{g\geq G}O(L^3/g^2)=O(L^3/G).
\]

For \(a=2s>0>b=-2w\), the plus cross gcd
\(\kappa=(d,m')\) gives

\[
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad
 r=2\kappa(sv-wu).
\]

For \(a=-2s<0<b=2w\), the minus cross gcd
\(\kappa=(d',m)\) gives

\[
 d'=\kappa u,\quad d=\kappa u+2s,\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad
 r=2\kappa(uw-sv).
\]

Both gcd definitions force \((u,v)=1\) and recover the parameters
uniquely.  At fixed \(\kappa\), the choices of \((u,v,n)\) contribute
\(O((L/\kappa)^3)\), while a solution line has \(O(\kappa)\) physical
sites.  Hence the fixed-\(\kappa\) count is
\(O(L^3/\kappa^2)\) and its tail is \(O(L^3/K)\).  The plus and minus
sign patterns are disjoint, so the factor for both orientations is
constant.

### Joint gcd and primitive domain

In the plus orientation, a prime dividing both \(\kappa\) and \(s\)
would divide both factors of the squarefree upper product
\((\kappa u+2s)\kappa v\).  In the minus orientation the same argument
uses the lower product.  Since \(\kappa\) is odd,
\((\kappa,s)=1\).  Therefore

\[
 (d,d')=(\kappa u,\kappa u+2s)=(u,s).
\]

Using \((u,v)=1\) in either determinant gives

\[
 (u,n)=(u,s),
\]

so (185.C20) follows.  With
\(u=gU\), \(s=gS\), and \(n=gh\), the two equations become

\[
 Sv-wU=h,\qquad Uw-vS=h,
\]

and \(r=2\kappa gh\).

The repaired primitive conditions are both necessary and sufficient
for multiplicity.  From a live incidence, \((u,v)=1\) gives
\((gU,v)=1\), while \(g=(u,n)\) gives \((U,h)=1\).  Conversely,
\((gU,v)=1\) makes the declared \(\kappa\) the actual inward cross gcd,
and \((U,h)=1\), together with either primitive equation, forces
\((U,S)=1\); hence the declared \(g\) is the actual original gcd on
every live term.  Any additional squarefree, allocation-coprime, or
literal restriction is correctly left to the zero-extended
coefficients.

### Canonical row and exact complement

Because \((U,v)=1\), for \(U>1\) the plus congruence
\(S_0v\equiv h\pmod U\) and the minus congruence
\(S_0v\equiv-h\pmod U\) each have one least-residue solution.  The
displayed formulas in (185.C32) then give integral \(w_0\) and satisfy
the appropriate primitive equation.  For \(U=1\), the separate bases
\((0,-h)\) and \((0,h)\) also satisfy those equations and avoid an
undefined modular inverse.

Every solution in either orientation is uniquely
\((S_0+Ut,w_0+vt)\).  Restricting to
\(S_t>0,w_t>0\) is exactly equivalent to \(s,w>0\), so it retains only
the requested opposing sign pattern before any square root is evaluated.
It neither reinserts the monotone sector nor crosses into the other
orientation.  Conversely, a physical opposing incidence determines
\(\kappa,g,h,U,v\), its orientation, and then a unique canonical
integer \(t\).  Thus (185.C36) is a bijective opening.

Since \(g,U\) are odd,

\[
 \chi_4(d')\chi_4(d)=(-1)^s=(-1)^S
 =(-1)^{S_{0,\omega}+t},
\]

which accounts for the two displayed signs in (185.C36).  The two
\(\lambda\)'s handle every remaining literal domain restriction, so no
additional tangent-domain indicator is missing.

### Bounded \(h\), coefficient power, and fixed-proportion tails

At fixed \((\kappa,g,h)\), support supplies

\[
 O\!\left(\frac{L}{\kappa g}\right)\text{ choices of }U,\qquad
 O\!\left(\frac{L}{\kappa}\right)\text{ choices of }v.
\]

The increments in \(s=gS\) and \(w\) are respectively
\(gU\asymp L/\kappa\) and \(v\asymp L/\kappa\), while their physical
ranges have length \(O(L)\).  Hence each oriented row has
\(O(\kappa)\) sites, proving

\[
 O\!\left(\frac{L^2}{\kappa g}\right)
\]

per fixed triple and orientation.  Because the integer
\(r<R_0=\lceil L\rceil\) satisfies \(r<L\),
\(\kappa g<L/(2h)\).  Therefore

\[
 \sum_{h\leq H}\sum_{\kappa g<L/(2h)}
 \frac{L^2}{\kappa g}
 \ll HL^2\log^2(2L).
\]

For \(H=H_B\), the fixed powers of \(\log(2X)\) and \(\log(2L)\),
together with the product of the two endpoint coefficient bounds, are
absorbed by epsilon rebudgeting in the inherited nonempty M1 shell
range.  This proves the asserted \(L^2X^\varepsilon\) absolute
contribution.

Finally, the two tail estimates with \(G=\gamma L\) and
\(K=\delta L\) give exactly

\[
 \gamma^{-1}L^2X^\varepsilon,\qquad
 \delta^{-1}L^2X^\varepsilon.
\]

Also \(2\kappa gh<L\) puts the first tail inside
\(h<(2\gamma)^{-1}\) and the second inside
\(h<(2\delta)^{-1}\), verifying the containment asserted after
(185.C31).

### Row capacity

At fixed \((\kappa,g)\), the counts of \(U,v,h\) are respectively
\(O(L/(\kappa g))\), \(O(L/\kappa)\), and
\(O(L/(\kappa g))\).  Thus the number of canonical primitive rows is

\[
 O\!\left(\frac{L^3}{\kappa^3g^2}\right).
\]

Even an assumed \(O(1)\) bound per row positively recombines only to

\[
 O\!\left(L^3\sum_{\kappa,g\geq1}
 \frac1{\kappa^3g^2}\right)=O(L^3),
\]

so (185.C38) has the correct power.  In (185.C39), the triangle
inequality gives the upper bound \(|I|\), while
\(B(t)=(-1)^t\) attains it.  A constant sequence on
\(M\asymp L^2\) sites has \(\asymp M\) correlation for
\(\asymp L\) even shifts, hence \(\asymp L^3\) Fejer capacity.

## 4. First doubtful or unproved step

There is no doubtful step in the assigned post-repair seam.  The first
remaining unproved mathematical relation is (185.C37), the explicitly
open global signed estimate over dyadic \(h\)-blocks.  The candidate
does not claim to prove it, and neither the row count nor the finite
control supplies the required global factor \(Y\).

## 5. Controls and outcomes

The frozen hashes were checked before the mathematical audit:

- candidate:
  `74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65`;
- exact control:
  `2531efad2e40c77b61985e0e694c11a9683088abc9d82a0a287a676772606999`.

For the plus label \((\kappa,g,h,U,v)=(103,1,1,7,1)\), the canonical
anchor is

\[
 S_{0,+}=[1]_7=1,\qquad w_{0,+}=(1-1)/7=0.
\]

Thus \(t=14\) gives \((S,w)=(99,14)\), and \(t=15\) gives
\((106,15)\), exactly matching the local sites in the control.  Exact
integer recomputation gives

\[
\begin{array}{c|c|c|c}
t&(d,d',m',m)&(N,N')&r\\ \hline
14&(721,919,103,131)&(94451,94657)&206\\
15&(721,933,103,133)&(95893,96099)&206.
\end{array}
\]

At \(t=14\),

\[
 94451=7\cdot103\cdot131,\qquad
 94657=103\cdot919,
\]

both products are squarefree, and both allocations are coprime.  The
exact hard-cone inequalities are

\[
 524<721<2096,\qquad 412<919<1648.
\]

All primes \(7,103,131,919\) are \(3\pmod4\), so no pair of distinct
prime factors has \(\chi_4\)-product \(-1\); both residual masks equal
one independently of selector choice.  The character product is
\(-1\).

At \(t=15\),

\[
 95893=7^2\cdot19\cdot103,\qquad
 96099=3\cdot103\cdot311.
\]

The inequalities remain

\[
 532<721<2128,\qquad 412<933<1648.
\]

Here \((721,133)=7\), so the lower product is not squarefree; the upper
product remains squarefree and allocation-coprime.  At both sites
\(g=(d,d')=1\) and \(h=(sv-wu)/g=1\).  The character product changes
from \(-1\) to \(+1\).

The licensed conclusion is exactly that adjacent bare character
alternation need not preserve squarefree, coprime, no-pair hard-cone
arithmetic support.  It therefore cannot by itself justify automatic
literal adjacent-pair cancellation.  Forbidden conclusions are
nonvanishing of either opaque literal amplitude for specified
\((L,X,\sigma)\), any density or lower-mass assertion, failure of
(185.C37), failure of a parent theorem, or any exponent consequence.
The control text observes all of these restrictions.

## 6. Exact artifacts used

- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/joint_h_count_power_and_deletion_post_repair_verification.md`;
- `protocol.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/conductor_round185_exact_fibre_deletion_control.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/joint_h_count_power_and_deletion_seam_review.md`; and
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`.

No other repository artifact, web source, external theorem, or
floating-point computation was used.  The finite control was reproduced
only with exact integer products, gcds, factorizations, residue classes,
and inequalities.

## 7. Recommended state effect

Accept the repaired joint-\(h\), multiplicity, power, complement, and
finite-control seam as verified evidence for the strict physical
opened-incidence sector (185.C30) and exact complement (185.C36).  This
review authorizes no direct state edit and no claim for the complete
\(t=1\) residual: (185.C37), all remaining hard-M1 owners, parent
obligations, bridges, endpoint uniformity, the target theorem, and all
exponent claims remain open.

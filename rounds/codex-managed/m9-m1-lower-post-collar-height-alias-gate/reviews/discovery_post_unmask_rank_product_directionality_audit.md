# 1. Result

**GREEN.**

The conductor candidate and the blind report agree on every mathematical
seam assigned to this review:

\[
 \operatorname{rank}\nabla^2_{h,s}
 \sqrt{Nh(4h+s)}=1,\qquad
 \det\nabla^2_{h,s}\sqrt{Nh(4h+s)}=0;
\]

the fourth-power ray used by the candidate has both unit radical phase
and the correct \(\chi_4\)-sign; grouping by \(m=hr\) gives exactly the
incomplete divisor coefficient \(A_{\rho_2}(m)\); its prime-square fibre
can contain \(a\) same-sign divisors; the coefficient-blind absolute
capacity is \(R^{3/2+o(1)}\); the exact radical channel is
\(O_\varepsilon(RD^{-3/4}X^\varepsilon)\); the second Legendre phase is
the original reciprocal phase; and the reduction changes only the
unsquared scalar interface.

All three requested repairs are present. The odd restrictions in
(140.C4), the sentence following (140.C14), and (140.C25) now contain
clean \({\rm odd}\) commands and there are no standalone carriage-return
bytes. Equations (140.C27a)--(140.C27b) provide the matching \(h=1\)
\(R^{3/2}\) lower absolute-capacity control. The prime-square statement
is restricted to sufficiently large odd fourth-power centres and a fixed
nonzero profile range, and (140.C28a) states exactly
\(A_{\rho_2}(p^{2a})=a\).

The added rowwise \(B\)-process ledger
(140.C19a)--(140.C19f), (140.C22)--(140.C23) terminates in the same far
survivor (140.C4). It changes neither the phase
\(\sqrt{Nhr}\), the far mask \(r\ge r_{2,h}+2\), the product coefficient
(140.C25), nor any scalar/downstream implication. Its analytic
stationary-remainder seam is assigned elsewhere; it introduces no change
to the rank/product/directionality conclusions certified here.

# 2. Exact statement and hypotheses

The audited survivor is

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_h\sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{R1}
\]

where \(r_{2,h}\) is the least positive odd integer satisfying
\[
 r_{2,h}\ge {4Nh\over D_{2,h}^2}.
\tag{R2}
\]
Bounded \(X\), empty rows, and zero profile samples are understood as in
the candidate. The phase geometry is considered only for \(h>0,r>0\).

Under the exact affine coordinate
\[
 r=4h+s,\qquad
 J={\partial(h,r)\over\partial(h,s)}
 =\begin{pmatrix}1&0\\4&1\end{pmatrix},
\qquad \det J=1,
\tag{R3}
\]
the relevant phase is
\[
 \Phi(h,s)=\sqrt{Nh(4h+s)}.
\tag{R4}
\]
No nondegenerate two-dimensional Hessian theorem is admissible unless
its hypotheses survive this coordinate change.

Grouping (R1) by \(m=hr\) is over a finite effective range
\(m\ll N/R^2\ll y\). The exact coefficient to audit is
\[
 A_{\rho_2}(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                  r\ge r_{2,h}+2}}\chi_4(r).
\tag{R5}
\]
The radical audit writes
\[
 N=Du^2,\qquad D\ {\rm squarefree}.
\tag{R6}
\]
All capacity statements below use the actual \(N^{1/4}\), the weight
\(m^{-3/4}\), the fixed profile support, and the scalar target
\(RX^\varepsilon\). No square of the scalar is introduced.

# 3. Proof or derivation

For
\[
 F(h,r)=\sqrt{Nhr},
\]
the candidate gives
\[
 H_{h,r}:=\nabla^2F
 ={\sqrt N\over4\sqrt{hr}}
 \begin{pmatrix}-r/h&1\\1&-h/r\end{pmatrix}.
\tag{R7}
\]
Its determinant is zero and it is nonzero for \(h,r>0\), hence has rank
one. Under (R3),
\[
 \nabla^2_{h,s}\Phi=J^{\mathsf T}H_{h,r}J,\qquad
 \det\nabla^2_{h,s}\Phi=(\det J)^2\det H_{h,r}=0.
\tag{R8}
\]
Moreover,
\[
 J\binom hs=\binom h{4h+s}=\binom hr,
\]
so the null vector becomes exactly \((h,s)^{\mathsf T}\). Thus the
rank-one claim is invariant under the required \(r=4h+s\) coordinates,
not merely a statement in the old variables.

The candidate’s coherent ray is character-correct. At an odd
fourth-power centre
\[
 N=M^4,\qquad y=M^2,\qquad R=M,
\]
take
\[
 (h,r)=(\ell,9\ell),\qquad \ell\equiv1\pmod4.
\tag{R9}
\]
Then
\[
 e(\sqrt{Nhr})=e(3M^2\ell)=1,\qquad
 \chi_4(r)=\chi_4(9\ell)=1.
\tag{R10}
\]
For all \(\ell\) beyond a fixed \(\rho_2\)-dependent initial segment,
\(9\ell\ge r_{2,\ell}+2\), because
\(r_{2,\ell}=4\ell+O_{\rho_2}(\sqrt\ell)+O(1)\).
Also
\[
 {R^2hr\over N}={9\ell^2\over M^2},
\]
so a fixed interval \(\ell\le cM\) lies on the profile plateau. The
subray has absolute mass
\[
 \asymp R\sum_{\substack{\ell\le cR\\\ell\equiv1\ (4)}}
 \ell^{-3/2}\asymp R.
\tag{R11}
\]
It is therefore a target-scale coherent control, not a lower bound for
the complete scalar.

Reindexing (R1) by \(m=hr\) is exact:
\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm}).
\tag{R12}
\]
There is no missing height weight: the stationary factor in (R1) is
\((hr)^{-3/4}=m^{-3/4}\), and every admissible factorization appears
once in (R5). Without the far mask,
\[
 \sum_{\substack{h\mid m\\m/h\ {\rm odd}}}\chi_4(m/h)
 =\sum_{r\mid m}\chi_4(r)={r_2(m)\over4}\ge0.
\tag{R13}
\]

The prime-square fibre statement is valid with the qualification stated
in Section 1. Let \(p\equiv1\pmod4\), hence \(p\ge5\), and
\(m=p^{2a}\). Write
\[
 r=p^j,\qquad h=p^{2a-j},\qquad0\le j\le2a.
\]
At a sufficiently large fourth-power centre, \(D_{2,h}\ge3y/4\), so
\[
 {4Nh\over D_{2,h}^2}<8h.
\tag{R14}
\]
If \(j\le a\), then \(r\le h<4Nh/D_{2,h}^2\), hence the divisor is
excluded. If \(j\ge a+1\), then
\[
 {r\over h}=p^{2(j-a)}\ge p^2\ge25,
\]
and consequently \(r-2>8h>4Nh/D_{2,h}^2\). Since \(r-2\) is odd, this
implies \(r\ge r_{2,h}+2\). All \(a\) upper divisors occur and have
\(\chi_4(r)=1\). Therefore
\[
 \boxed{A_{\rho_2}(p^{2a})=a.}
\tag{R15}
\]
To make this a literal scalar control, one additionally takes
\(p^{2a}\) inside a fixed nonzero part of the profile support.

The upper absolute ledger follows from \(|A_{\rho_2}(m)|\le\tau(m)\):
\[
 |\mathcal P_{\rho_2}^{+}|
 \ll N^{1/4}\sum_{m\ll y}m^{-3/4}\tau(m)
 \ll_\varepsilon R^{3/2}X^\varepsilon.
\tag{R16}
\]
There is a matching coefficient-blind lower capacity. On the \(h=1\)
row, the far condition excludes only \(O_{\rho_2}(1)\) initial odd
aliases. On any fixed plateau interval
\[
 C_{\rho_2}\le r\le c\,{N\over R^2}\asymp cR^2,
\]
the sum of term moduli is
\[
 N^{1/4}\sum_{\substack{r\le cR^2\\r\ {\rm odd}}}r^{-3/4}
 \asymp R^{3/2}.
\tag{R17}
\]
Thus \(R^{3/2+o(1)}\) is the actual coefficient-blind absolute capacity,
not only a loose upper estimate.

The exact radical bound is also correct. From (R6),
\[
 Nm\ {\rm is\ a\ square}\quad\Longleftrightarrow\quad m=Dt^2.
\tag{R18}
\]
Using \(|A_{\rho_2}(m)|\le\tau(m)\) and
\(Dt^2\ll N/R^2\ll R^2\),
\[
 \begin{split}
 &N^{1/4}\sum_{\substack{m\ll y\\Nm=\square}}
 m^{-3/4}|A_{\rho_2}(m)|\\
 &\qquad\ll_\varepsilon
 N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
 \end{split}
\tag{R19}
\]
This proves only the exact phase-one channel; it gives no estimate for
near radicals.

Finally, the phase-level self-return is exact. For \(z>0\),
\[
 \Psi(m)=\sqrt{Nm}-{mz\over4}
\]
has
\[
 \Psi'(m)=0
 \quad\Longleftrightarrow\quad
 m_*={4N\over z^2},
\qquad
 \Psi(m_*)={N\over z}.
\tag{R20}
\]
This is the reciprocal phase obtained after the exact \(x=hz\)
normalization. The incomplete coefficient \(A_{\rho_2}(m)\) prevents
calling this a new exact scalar identity, but it also prevents treating a
second transform as an independent gain. Completing the mask gives
(R13), the sum-of-two-squares self-return.

# 4. First doubtful or unproved step

In the patched candidate, none of the audited algebraic seams is
doubtful. The first genuinely unproved statement remains
\[
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.
\tag{R21}
\]
The rank-one Hessian gives no nondegenerate two-variable theorem;
(R15) rules out automatic character cancellation on each product fibre;
(R16)--(R17) show that modulus loses \(R^{1/2}\); (R19) controls only
exact radicals; and (R20) is a phase self-return. Near radicals and the
aggregate of nonsquare incomplete fibres are therefore still the first
signed-cancellation gap.

The blind report correctly leaves the nonprincipal sharp-endpoint owner
open. The conductor candidate’s separate smoothing argument is what
claims to close that owner. This review was deliberately restricted to
rank, product, radical, self-return, and directionality seams, so it
neither re-proves nor weakens the candidate’s smoothing and stationary
remainder ledger.

# 5. Control tests and outcomes

| Audited control | Outcome |
|---|---|
| Hessian after \(r=4h+s\) | GREEN. Equation (R8) proves determinant zero and rank one under the exact affine map; the null direction is \((h,s)\). |
| Character-correct coherent ray | GREEN. Equations (R9)--(R11) retain the far mask, unit radical phase, \(\ell\equiv1\pmod4\), \(\chi_4(r)=1\), and target-scale mass. |
| Product reindexing | GREEN. The three odd restrictions are clean, and equations (R5) and (R12) contain every and only admissible factorization. |
| Complete-fibre comparison | GREEN. Removing the mask gives exactly \(r_2(m)/4\), not a cancellation estimate for \(A_{\rho_2}(m)\). |
| Prime-square fibre | GREEN. The candidate now includes the required centre/profile qualification and exact value \(A_{\rho_2}(p^{2a})=a\); it is explicitly not a lower bound for the whole scalar. |
| \(R^{3/2}\) capacity | GREEN. Candidate equations (140.C27a)--(140.C27b) supply the matching \(h=1\) absolute-capacity lower control. |
| Exact radicals and near radicals | GREEN. Equation (R19) proves the \(RD^{-3/4}X^\varepsilon\) bound and leaves near radicals open. |
| Second-transform self-return | GREEN. Equation (R20) is exact at phase level and is not overstated as a full transform with the incomplete coefficient. |
| Scalar directionality | GREEN. The candidate asserts only target equivalence of unsquared scalars and explicitly retains the collar--tail cross term and lift-splitting obstruction. |
| Downstream scope | GREEN. No lower GAR, direct M1, M9-M1, M2, endpoint, M9, bridge, quarter, or exponent promotion is made. |

No vote, computation, external theorem, or numerical evidence is used.

# 6. Dependencies and exact artifacts used

This post-unmask review used exactly:

- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/blind_height_alias_joint_feasibility.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md.

The primary discovery connector was not used or reviewed. No shared proof
state, synthesis, validation file, sibling review, web source, or
computation was consulted.

# 7. Recommended state effect

Final verdict: **GREEN**. The rank-one \(r=4h+s\) geometry, character-correct ray,
product coefficient \(A_{\rho_2}(m)\), prime-square fibre,
\(R^{3/2+o(1)}\) absolute capacity, exact radical bound, phase
self-return, and scalar/downstream directionality are all mathematically
sound.

Promote only the strict scalar survivor if the independently assigned
endpoint and stationary-remainder seams are also GREEN. Retain (R21) as
open. Record the rank-one, product-fibre, modulus-capacity, near-radical,
and self-return facts as obstructions to the rejected mechanisms, not as
a counterexample or a lower bound for the physical scalar. Make no
tail-square, residual-deletion, downstream theorem, quarter, or exponent
promotion.

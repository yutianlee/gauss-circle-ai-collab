# Round 141 post-unmask review: cone dictionary and quarter mode

Campaign: m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate

Candidate: candidates/conductor_round141_cone_nonresonant_reduction.md

Reviewer seam: floor-to-cone dictionary and statement-only quarter-frequency obstruction

Graph at assignment: 072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

## 1. Verdict and seam status

The conductor's repaired candidate now states the variation range
explicitly. The assigned mathematical seams are correct with no
remaining red condition.

| Seam | Status | Review conclusion |
|---|---|---|
| Least-odd threshold and floor-to-cone dictionary, (141.C12)--(141.C14) | **GREEN** | The odd endpoints partition the cone exactly, the correction sign is \(A_\rho=C-E_N\), and the candidate's effective-support and zero-profile convention supplies the required scope. |
| Correction width and weighted cost, (141.C17)--(141.C18) | **GREEN** | The exact width is \(O_\rho(1+\sqrt h+h/y)\); after \(hr\ll y\) and \(r>4h\), its weighted mass is \(O_{\rho,V}(\log(2X))\), uniformly in \(q\) and the real centre. |
| Cone quarter mode, (141.C29)--(141.C33) | **GREEN** | The odd-row identity and endpoints give \(i\pi M/8\); even rows and all endpoint errors contribute \(O(\sqrt M)\). |
| Transfer from \(C\) to \(A_\rho\), and weighted constant (141.C8)--(141.C9) | **GREEN** | The correction count is \(O_{\rho,c_0}(M^{3/4})\), with the minus sign harmless at that size; Abel summation multiplies \(i\pi/8\) by \(4\), giving \(i\pi/2\). |
| Linear variation, (141.C34) | **GREEN** | The repaired candidate states exactly \(M_0(\rho,c_0)\le M\le c_0y\), which is the range supplied by the quarter-mode asymptotic and summation by parts. |
| Profile-plateau relevance and scalar direction | **GREEN** | \(c_0\) may be chosen inside the literal \(V_{\mathrm{low}}=1\) plateau. The quarter mode disproves low variation and uniform additive cancellation; it is not a lower bound for the square-root-phase scalar. |
| Final downstream scope | **GREEN** | The candidate correctly leaves the nonresonant scalar and every lower-GAR, M1, M2, endpoint, M9, quarter, and exponent owner open. |

The final assigned-seam verdict is

\[
\boxed{\mathsf{GREEN}.}
\]

This review does not certify the nearest-square reduction, quadratic
congruence argument, divisor-pairing identity, source audit, or Mellin
continuation. Those are outside the assigned seams; in particular, the
reviewer does not re-certify its own discovery claims.

## 2. Exact reviewed statements and hypotheses

Retain

\[
N=y^2+q,\qquad 0\le q\le2y,
\qquad
\delta_h=\left\lfloor\frac{\rho y}{\sqrt h}\right\rfloor+1,
\qquad
D_h=y-\delta_h,
\tag{141.R1}
\]

and let \(r_h\) be the least positive odd integer at least

\[
\Theta_h=\frac{4Nh}{D_h^2}.
\tag{141.R2}
\]

For odd \(r\), the reviewed exact endpoint statement is

\[
r\ge r_h+2
\quad\Longleftrightarrow\quad
r-2\ge\Theta_h.
\tag{141.R3}
\]

Since \(\Theta_h>4h\) on an active row, define

\[
\begin{aligned}
C(m)
&=\sum_{\substack{hr=m\\ r\ \mathrm{odd}\\ r>4h}}\chi_4(r),\\
E_N(m)
&=\sum_{\substack{hr=m\\ r\ \mathrm{odd}\\ 4h<r\le r_h}}\chi_4(r).
\end{aligned}
\tag{141.R4}
\]

Then, on every term of the effective scalar support,

\[
\boxed{A_\rho(m)=C(m)-E_N(m).}
\tag{141.R5}
\]

The reviewed quantitative correction is

\[
\sum_m m^{-3/4}|E_N(m)|
\cdot\left|V_{\mathrm{low}}\!\left(\frac{R^2m}{N}\right)\right|
\ll_{\rho,V}\log(2X).
\tag{141.R6}
\]

For the independent quarter-mode rederivation, let \(M\) be an integer
with \(2\le M\le c_0y\), and put

\[
S_C(M)=\sum_{m\le M}C(m)e(m/4),
\qquad
S_A(M)=\sum_{m\le M}A_\rho(m)e(m/4).
\tag{141.R7}
\]

The reviewed asymptotics are

\[
S_C(M)=\frac{i\pi}{8}M+O(M^{1/2}),
\tag{141.R8}
\]

\[
S_A(M)=\frac{i\pi}{8}M+O_{\rho,c_0}(M^{3/4}),
\tag{141.R9}
\]

and

\[
\sum_{m\le M}m^{-3/4}A_\rho(m)e(m/4)
=\frac{i\pi}{2}M^{1/4}+O_{\rho,c_0}(\log(2M)).
\tag{141.R10}
\]

The variation consequence, with its repaired range, is

\[
\boxed{
\sum_{m<M}|A_\rho(m+1)-A_\rho(m)|
\gg_{\rho,c_0}M
\quad
\bigl(M_0(\rho,c_0)\le M\le c_0y\bigr).
}
\tag{141.R11}
\]

Choose \(c_0>0\) sufficiently small in terms of the fixed plateau of
\(V_{\mathrm{low}}\). Since \(Z=N/R^2\) satisfies \(y-1<Z\le y+2\), this
ensures \(V_{\mathrm{low}}(m/Z)=1\) throughout \(m\le c_0y\), once \(X\) is
large. Thus (141.R9)--(141.R11) concern the coefficient on a literal
profile plateau, not a profile-zero range.

## 3. Independent floor-to-cone derivation

Because \(r-2\) is odd, minimality of \(r_h\) proves both directions of
(141.R3):

\[
r\ge r_h+2
\Longrightarrow
r-2\ge r_h\ge\Theta_h,
\]

while \(r-2\ge\Theta_h\) forces the odd integer \(r-2\) to be at least
the least eligible odd integer \(r_h\). Equality is retained. Since
\(r_h\) is odd, the cone aliases have the exact disjoint endpoint
partition

\[
\{r\ \mathrm{odd}:r>4h\}
=
\{r\ \mathrm{odd}:4h<r\le r_h\}
\mathbin{\dot\cup}
\{r\ \mathrm{odd}:r\ge r_h+2\}.
\tag{141.R12}
\]

There is no missing odd alias between \(r_h\) and \(r_h+2\). This proves
the correction sign in (141.R5): the literal far family is the cone
family with the lower correction interval removed, not added.

To see that the partition begins beyond \(4h\), note that on an active
row \(D_h<y\) and \(N\ge y^2\), so

\[
\Theta_h=\frac{4Nh}{D_h^2}>4h.
\tag{141.R13}
\]

On the effective support, every cone or correction pair satisfies
\(hr\ll_Vy\) and \(r>4h\); hence

\[
h\ll_V\sqrt y\asymp R.
\tag{141.R14}
\]

For these rows and sufficiently large \(y\), the floor in \(\delta_h\)
gives \(D_h\asymp_\rho y\). Expanding without approximation,

\[
\Theta_h-4h
=4h\frac{N-D_h^2}{D_h^2}
=4h\frac{q+2y\delta_h-\delta_h^2}{D_h^2}.
\tag{141.R15}
\]

The numerator is nonnegative, and

\[
q\le2y,
\qquad
\delta_h\le\frac{\rho y}{\sqrt h}+1.
\]

Using \(D_h\asymp_\rho y\) in (141.R15) yields

\[
0<\Theta_h-4h
\ll_\rho 1+\sqrt h+\frac{h}{y}.
\tag{141.R16}
\]

The least odd integer above a real number is strictly less than that
number plus two. Consequently

\[
\#\{r\ \mathrm{odd}:4h<r\le r_h\}
\ll_\rho1+\sqrt h+\frac{h}{y}.
\tag{141.R17}
\]

Every such \(r\) is comparable to \(h\). Therefore, with the profile
bounded and (141.R14),

\[
\begin{aligned}
&\sum_m m^{-3/4}|E_N(m)|
\cdot\left|V_{\mathrm{low}}\!\left(\frac{R^2m}{N}\right)\right|\\
&\le
\sum_{h\ll_VR}h^{-3/4}
\sum_{\substack{4h<r\le r_h\\ r\ \mathrm{odd}}}
r^{-3/4}
\left|V_{\mathrm{low}}\!\left(\frac{R^2hr}{N}\right)\right|\\
&\ll_{\rho,V}
\sum_{h\ll_VR}h^{-3/2}
\left(1+\sqrt h+\frac{h}{y}\right)\\
&\ll_{\rho,V}
\sum_{h\ll_VR}(h^{-3/2}+h^{-1})+O(1)\\
&\ll_{\rho,V}\log(2X).
\end{aligned}
\tag{141.R18}
\]

The \(h/y\) contribution in the penultimate line is
\(y^{-1}\sum_{h\ll R}h^{-1/2}=O(1)\). This proves the exact correction
cost uniformly at \(q=0\), \(q=2y\), and every intermediate integer
centre. The real value of \(X\) enters only through the retained profile
and \(R=X^{1/4}\), so no centre averaging is present.

## 4. Independent quarter-frequency derivation

Unfolding the cone coefficient gives the exact finite sum

\[
S_C(M)=
\sum_{4h^2<M}
\sum_{\substack{4h<r\le M/h\\ r\ \mathrm{odd}}}
\chi_4(r)e(hr/4).
\tag{141.R19}
\]

The strict inequality \(4h^2<M\) is correct: at equality the interval
\(4h<r\le M/h=4h\) is empty. Since \(4h\) is even, the first eligible
alias is the odd integer \(4h+1\); the last alias is the greatest odd
integer not exceeding \(M/h\).

If \(h\) is even, \(e(hr/4)\) is constant as \(r\) runs over odd
integers: it is \(1\) for \(h\equiv0\pmod4\) and \(-1\) for
\(h\equiv2\pmod4\). The consecutive odd values of \(\chi_4(r)\)
alternate, so each even row is \(O(1)\), and all even rows contribute
\(O(\sqrt M)\).

If \(h\) and \(r\) are odd, then exactly

\[
e(hr/4)=i\chi_4(h)\chi_4(r).
\tag{141.R20}
\]

Multiplication by the coefficient \(\chi_4(r)\) makes every summand in
the odd \(h\)-row equal to \(i\chi_4(h)\). Let

\[
H_M=\max\{h\in\mathbb N:4h^2<M\}
=\frac{\sqrt M}{2}+O(1).
\]

The number of admissible odd \(r\) in that row is

\[
\#\{r\ \mathrm{odd}:4h<r\le M/h\}
=\frac{M}{2h}-2h+O(1).
\tag{141.R21}
\]

Hence the odd rows contribute

\[
\frac{iM}{2}
\sum_{\substack{h\le H_M\\ h\ \mathrm{odd}}}
\frac{\chi_4(h)}{h}
-2i
\sum_{\substack{h\le H_M\\ h\ \mathrm{odd}}}
\chi_4(h)h
+O(H_M).
\tag{141.R22}
\]

Pairing \(4a+1\) with \(4a+3\) gives

\[
\sum_{\substack{h\le H\\ h\ \mathrm{odd}}}\chi_4(h)h=O(H),
\]

while the alternating harmonic series gives

\[
\sum_{\substack{h\le H\\ h\ \mathrm{odd}}}
\frac{\chi_4(h)}{h}
=L(1,\chi_4)+O(H^{-1})
=\frac{\pi}{4}+O(H^{-1}).
\tag{141.R23}
\]

Substitution into (141.R22), together with the even-row estimate, proves

\[
S_C(M)
=\frac{iM}{2}\frac{\pi}{4}+O(\sqrt M)
=\frac{i\pi}{8}M+O(\sqrt M).
\tag{141.R24}
\]

The correction sign is now important but elementary. From
\(A_\rho=C-E_N\),

\[
S_A(M)=S_C(M)-
\sum_{\substack{hr\le M\\ 4h<r\le r_h\\ r\ \mathrm{odd}}}
\chi_4(r)e(hr/4).
\tag{141.R25}
\]

The number of correction pairs is, by (141.R17),

\[
\begin{aligned}
&\ll_\rho
\sum_{h\ll\sqrt M}
\left(1+\sqrt h+\frac{h}{y}\right)\\
&\ll_\rho
\sqrt M+M^{3/4}+\frac{M}{y}\\
&\ll_{\rho,c_0}M^{3/4}
\qquad(M\le c_0y).
\end{aligned}
\tag{141.R26}
\]

Thus the subtraction changes only the error term and proves (141.R9)
with the same \(i\pi/8\) main constant.

Let \(a_m=A_\rho(m)e(m/4)\). Abel summation gives

\[
\sum_{m\le M}m^{-3/4}a_m
=M^{-3/4}S_A(M)
+\frac34\int_1^M t^{-7/4}S_A(t)\,dt+O(1).
\tag{141.R27}
\]

The main term is

\[
\frac{i\pi}{8}M^{1/4}
+\frac34\frac{i\pi}{8}\cdot4M^{1/4}
=\frac{i\pi}{2}M^{1/4}+O(1),
\tag{141.R28}
\]

and the \(O(t^{3/4})\) error integrates as \(O(\log(2M))\). This proves
(141.R10) and verifies the constant \(i\pi/2\).

For variation, put \(z_m=e(m/4)=i^m\) and
\(Z_u=\sum_{m\le u}z_m\). The sequence \(Z_u\) is bounded because
\(z_m\) has period four and zero period sum. Discrete summation by parts
therefore yields

\[
|S_A(M)|
\ll |A_\rho(M)|
+\sum_{m<M}|A_\rho(m+1)-A_\rho(m)|.
\tag{141.R29}
\]

By (141.R9), \(|S_A(M)|\gg M\) once
\(M\ge M_0(\rho,c_0)\), while
\(|A_\rho(M)|\le\tau(M)\le2\sqrt M\). Equation (141.R11) follows.
This also explains why the discarded small-\(M\) version was false:
before the first admitted far alias, all relevant \(A_\rho(m)\) may
vanish, and so may its variation.

The plateau makes the obstruction relevant to the literal coefficient,
but it does not change its direction. Equations (141.R9)--(141.R10)
use \(e(m/4)\); the target uses \(e(\sqrt{Nm})\). The nonlinear residual
phases from distinct occupied cells can rotate and cancel. A large
Fourier coefficient at \(1/4\) proves neither a lower bound nor a main
term for the fixed-centre square-root-phase scalar. It proves only that
uniform additive cancellation in every frequency and a sublinear
bounded-variation hypothesis are unavailable.

## 5. First doubtful step and control outcomes

The repaired (141.C34) now states
\(M_0(\rho,c_0)\le M\le c_0y\), exactly as required by (141.R11).
The candidate also declares empty rows and zero-profile samples to
contribute zero before a denominator is used, so its floor-to-cone
identity has the needed effective-support scope. There is no remaining
red seam among the assigned equations.

The assigned controls are:

- **GREEN — odd endpoints:** \(4h\) is even, \(r_h\) is odd, the
  correction ends at \(r_h\), and the literal far family begins at
  \(r_h+2\). Equation (141.R12) is disjoint and exhaustive.
- **GREEN — correction sign:** the exact relation is \(A_\rho=C-E_N\).
  The quarter correction is consequently subtracted in (141.R25).
- **GREEN — floor and \(q\) uniformity:** (141.R15)--(141.R18) retain
  every floor and cover \(q=0\) through \(q=2y\).
- **GREEN — correction count and weighted cost:** the unweighted count
  is \(O(M^{3/4})\) on \(M\le c_0y\), while the scalar-weighted global
  correction is \(O(\log X)\).
- **GREEN — quarter constants:** odd-row density contributes \(1/2\),
  \(L(1,\chi_4)=\pi/4\), and hence \(i\pi/8\); Abel summation contributes
  the factor \(4\), hence \(i\pi/2\).
- **GREEN — plateau relevance:** \(c_0\) can be fixed strictly inside
  the \(V_{\mathrm{low}}=1\) region using \(Z\asymp y\).
- **GREEN — variation:** the repaired (141.C34) uses the large-\(M\)
  range (141.R11), and its proof follows from (141.C8) and bounded
  quarter-frequency partial sums.
- **GREEN — fixed-centre directionality:** no quarter-mode capacity is
  treated as a lower bound for the square-root-phase scalar.

The first mathematical step still unproved after these seams is the
candidate's nonresonant fixed-centre scalar estimate (141.C38)/(141.C39).
Neither the logarithmic floor correction nor the quarter-mode
obstruction proves that estimate.

## 6. Dependencies and scope audit

This review used only the exact Round-141 candidate statement, the
active campaign, the protocol, and the Round-140 scalar definitions
already incorporated verbatim into the candidate. The rederivations in
Sections 3--4 are elementary and independent: no sibling review, source
theorem, numerical experiment, centre average, positive energy, or
desired circle estimate is used.

The following candidate components are deliberately outside this
review's certification: (141.C6)--(141.C7), (141.C15)--(141.C28), and
(141.C35)--(141.C41), except where their notation is needed to state the
scope. In particular, this review makes no validation claim about the
reviewer's own nearest-square or divisor-pairing discovery.

The scope paragraph of the candidate is **GREEN**. The floor-to-cone
estimate changes an unsquared scalar by \(O(\log X)\) before the
Round-140 outer factor, which is target-safe. The quarter-frequency
calculation is a coefficient obstruction only. Neither fact supplies
the missing signed bound for the cone survivor, a square identity, a
residual deletion, or a collar-tail cross-term estimate. Therefore no
complete lower-radial estimate, lower GAR, direct blockwise M1 parent,
M9-M1, M2 parent, M9-M2, endpoint-uniformity theorem, M9, conditional
bridge, Gauss-circle quarter result, or exponent improvement follows.

## 7. Recommended effect and final verdict

Recommend **promote** the following narrow assigned-seam facts:

1. the effective-support floor-to-cone identity (141.R3)--(141.R5) and
   its \(O_{\rho,V}(\log X)\) weighted correction (141.R18);
2. the exact cone and incomplete-coefficient quarter-mode asymptotics
   (141.R8)--(141.R10); and
3. the large-\(M\), plateau-range linear variation obstruction
   (141.R11).

The conductor's repair to (141.C34) is sufficient, and the candidate's
existing empty-row/profile-zero convention supplies the support
qualification. The assigned seams are therefore unqualified
**GREEN**. Retain the nonresonant cone scalar as open, and retain every
downstream owner and both exponent records unchanged. This verdict does
not license promotion of the nearest-square, divisor-pairing, source,
Mellin, or canonical-transform seams without their separate independent
reviews.

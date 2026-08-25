# Round 133 discovery report: literal joint scalar versus the Li--Yang/Bombieri--Iwaniec normal form

Campaign: `gc-w7-16-bombieri-iwaniec-two-spacing-source-map`

Task: `literal_joint_scalar_bi_normal_form_map`

Starting graph SHA-256:
`465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`

## 1. Result: exact single-wave phase chart, but a source-level joint-normal-form no-go

The candidate single-wave chart is exact at the phase level.  On a positive
numerator dyadic box,

\[
 h=a,\qquad m=b,\qquad H_{\rm LY}=L,\qquad M_{\rm LY}=D,
 \qquad T_{\rm LY}=c/\kappa_i,\qquad F(z)=z^{-1}
 \tag{133.1}
\]

gives

\[
 {hT_{\rm LY}\over M_{\rm LY}}F\!\left({m\over M_{\rm LY}}\right)
 ={ca\over \kappa_i b}.
 \tag{133.2}
\]

The negative-$a$ box is the conjugate positive-$|a|$ sum, so no change
of the source $F$ or of the sign of its curvature is needed.  Moreover,

\[
 F'=-z^{-2},\qquad F''=2z^{-3},\qquad F'''=-6z^{-4},
 \qquad F'F'''-3(F'')^2=-6z^{-6},                         \tag{133.3}
\]

and therefore both Li--Yang conditions on $F$ hold uniformly on
$[1,2]$.  The sign split, the two values $\kappa_1=1,\kappa_2=4$, and
dyadic endpoint ownership cost only $O(1)$ at this phase-only interface.

The chart does **not** extend to the literal joint scalar.  The terminal
label is

\[
 \boxed{\texttt{source\_level\_no\_go}}.                 \tag{133.4}
\]

There are two independent reasons.

1. Li--Yang's (S) has the rank-one coefficient
   (g(h/H)G(m/M)).  After the Bombieri--Iwaniec dissection, its displayed
   double-large-sieve form has a coefficient on the first-spacing vector
   independent of the derivative-approximant label and places an absolute
   value around each minor-arc inner sum.  The project coefficient is the
   joint matrix

   \[
   C_i(r,r')=A_i(r)B_i(r,r')
   \mathbf 1_{ab'-a'b>0}
   \left(1-{W(ab'-a'b)\over\kappa_i bb'}\right),          \tag{133.5}
   \]

   with primitive lifts, Möbius/Stieltjes profiles, thresholds, quarter or
   (chi_4) carriers, reciprocal aliases, taper, stars, cells, signs, and
   owners still joint.  No permitted source theorem controls an
   owner-preserving BV/projective decomposition of (133.5).  Triangulating
   over rows, SVD terms, minor arcs, or owners changes the absolute-value
   direction into an uncontrolled positive functional.

2. Even if one grants for free a rank-one factorization of (133.5), the
   one-sided/taper projection, every arithmetic owner, and a Li--Yang bound
   for each of the two waves, the sharp source exponent at
   $H/M=T^{-1/3}$ is

   \[
   {S\over H}\ll T^{E_*+\epsilon},\qquad
   E_*={29\over300}+{\sqrt{170}\over60}
       =0.3139734135\ldots .                              \tag{133.6}
   \]

   Since the project ray coefficient has natural size $L^{-1}=H^{-1}$,
   the fictitious two-wave correlation has capacity

   \[
   Y^{2E_*+\epsilon},\qquad
   2E_*={29\over150}+{\sqrt{170}\over30}
       =0.6279468270\ldots={30.1414\ldots\over48}.        \tag{133.7}
   \]

   This is strictly above (27/48), and hence cannot cross the persistence
   threshold, let alone reach (24/48).  This second obstruction is a
   best-case source-capacity obstruction and does not depend on proving a
   lower bound for the actual coefficient matrix.

Thus the exact single-wave phase analogy is valid, but neither one source
(S), a controlled superposition of source (S)'s, nor the displayed
double-large-sieve/two-spacing inequality yields the requested complete
joint estimate.

## 2. Exact statement and hypotheses

Fix

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},\qquad
 c\asymp Y,\qquad \kappa_1=1,\quad\kappa_2=4,            \tag{133.8}
\]

one literal top-shell M1 or M2 block, one moving-symbol stratum, one
orientation, and all its half-open physical owners.  Let
$r=(a,b)$, $r'=(a',b')$ be primitive project rays with
$|a|,|a'|\asymp L$, $b,b'\asymp D$, and

\[
 n=ab'-a'b>0,\qquad 0<n\lesssim {\kappa_i bb'\over W}.
 \tag{133.9}
\]

The literal target is

\[
 \mathfrak O^+_{i,D}(c)
 =\sum_r^{\rm lit}A_i(r)
   \sum_{r'}^{\rm lit}B_i(r,r')
   e\!\left({ca\over\kappa_i b}-{ca'\over\kappa_i b'}\right),
 \tag{133.10}
\]

where (133.9), its taper, and every primitive lift, threshold,
Stieltjes/Möbius atom, character carrier, reciprocal alias, star, cell,
sign, and owner are included in the superscript and in $B_i$.  In the
Hermitian reduced-Farey specialization $B_i(r,r')$ contains
$\overline{A_i(r')}$, but the following obstruction allows the more
general literal joint notation (133.10).

Li--Yang's source sum is

\[
 S=\sum_{H\le h\le2H}g(h/H)
   \sum_{M\le m\le2M}G(m/M)
   e\!\left({hT\over M}F(m/M)\right),                    \tag{133.11}
\]

where $g,G$ are one-variable BV functions and the same $F$ is used for
all $h$.  The argument is homogeneous in the BV weights; write
$\|f\|_{BV,*}=\|f\|_\infty+\operatorname {Var}(f)$ when a coefficient
cost must be exposed.

The exact claim proved in this report is:

* (133.1)--(133.3) map every isolated geometric wave in (133.10) to the
  source phase, after an $O(1)$ sign/dyadic split.
* With $H=L,M=D,T=c/\kappa_i$, all source powers through the
  first- and second-spacing coordinates are those in Section 3 below.
* The project primitive ray $(a,b)$ maps to the **original source
  variables** $(h,m)$; it does not map to the later derivative
  approximant $a_{\rm BI}/r_{\rm BI}$.
* A Li--Yang application to (133.10) would require an additional
  owner-preserving four-variable projective-BV theorem and an aligned-packet
  theorem.  Neither is a source hypothesis or an accepted project lemma.
* Even if these two missing inputs are assigned zero cost, (133.7) is above
  $27/48$.  Therefore the frozen request for a complete exponent below
  $27/48$ has no legal stratum under the present source theorem.

All statements below are upper-bound or applicability statements.  The
same-denominator packets are controls, not lower bounds for the actual
Vaaler family.  No positive energy is substituted for (133.10).

## 3. Proof and derivation

### 3.1 The single-wave map and its exact scope

Substitution in (133.11) proves (133.2).  On $z\in[1,2]$,

\[
 {1\over4}\le |F'|\le1,\qquad
 {1\over4}\le |F''|\le2,\qquad
 {3\over8}\le |F'''|\le6,
 \qquad {3\over32}\le|F'F'''-3(F'')^2|\le6.             \tag{133.12}
\]

Thus, for example, fixed constants $C_1=4,C_2=4,C_3=6$ and
$C_4=32/3$ satisfy Li--Yang's two phase conditions.  If $a<0$, put
$h=-a$; the resulting sum is the conjugate of a positive-$h$ source
sum with conjugated coefficient.  This keeps (F''>0), which is convenient
for the later source definition of (mu).

This verifies only the geometric exponential.  It does not put the M1
denominator-quarter carrier into (133.11): $e(\pm b/4)$ is an additive
linear phase independent of $h$, whereas the source has one phase
$h(T/M)F(m/M)$.  Treating that carrier as $G$ has discrete BV cost
$\asymp D$, or $D/L=Y^{1/3}$ after the natural project normalization.
The normalized M2 numerator character alone has only $L/L=O(1)$ total
variation, but the physical lift and primitive profiles remain joint.
Consequently (133.1) is a phase chart, not a coefficient theorem.

### 3.2 Complete source-parameter power ledger

Put $x=-1/3$, meaning the repaired relation $H=MT^x$.  Constants
$\kappa_i$ and dyadic comparability affect only $Y^{o(1)}$.  The
Li--Yang choice of moment is

\[
 q=q_{-1/3}
 =2+{2\over5\sqrt{5/34}-1}
 =4.1800444846\ldots .                                   \tag{133.13}
\]

The corrected Case-(A) first clause has $M<T^{7/16}$, not the printed
negative exponent.  Here $T^{7/16}<M=T^{1/2}<T^{9/16}$, so both
conditional lower bounds are vacuous, while

\[
 {H\over MT^{-49/164}}=T^{-17/492}.                      \tag{133.14}
\]

Hence Case (A) has a fixed power margin.  Case (B) is unnecessary; its
reduction-to-A upper inequality $H<M^{-9}T^4(\log T)^{171/140}$ fails
at these powers.

Ignoring displayed logarithms only in the $Y$-power column, the entire
source ledger is:

| Source object | Exact definition or range | $Y$-power under (133.1) |
|---|---|---:|
| $T,H,M$ | $T=c/\kappa_i$, $H=L$, $M=D$ | $1,1/6,1/2$ |
| $N=N_A$ | $H(M/H)^{41/25}T^{-49/100}(\log T)^{969/14000}$ | $67/300$ |
| Case-B first (N_B) branch | $M^{7/8}T^{-3/20}H^{-29/40}(\log T)^{969/5600}$ | $1/6$ |
| Case-B second (N_B) branch | $M^2H^{-1/3}T^{-2/3}$ | $5/18$ |
| number of $m$-intervals | $M/N$ | $83/300$ |
| $R$ | $(M^3/(NT))^{1/2}$ | $83/600$, with log power $-969/28000$ |
| major-arc small-denominator edge | $R^2/H$ | $11/100$ |
| major-arc source contribution | $MR\log H/\sqrt{HN}$ | $133/300$ for $S$, $83/300$ for $S/H$ |
| minor denominator $Q$ | $R\le Q\le3H$; write $Q=Y^s$ | $83/600\le s\le1/6$ |
| derivative numerator $A_{\rm BI}$ | $a_{\rm BI}\asymp A_{\rm BI}\le Q$; here $|a_{\rm BI}/r_{\rm BI}|\asymp1$ off bad arcs | $s$ on ordinary arcs |
| $L_{\rm BI}$ | $HQ/R^2$ | $s-11/100$ |
| $K_{\rm BI}$ | $NQ/R^2$ | $s-4/75$ |
| $\eta_{\rm BI}$ | $(Q/R)^2(K_{\rm BI}L_{\rm BI})^{-1}=R^2/(NH)$ | $-17/150$ |
| $Q_2$ | $R(H/R)^{39/119}(\log(2H/R))^{-3/4}$ | $527/3570$ |
| project top local denominator window | $Q_*=D^2/(WL)$ | $19/48$ |
| source intervals per project $Q_*$-window | $Q_*/N$ | $69/400$ |

The Case-B minimum is its first branch, (N_B=Y^{1/6+o(1)}<N_A),
consistent with the failure of the reduction-to-A range noted above.
At the maximizing endpoint $Q=R$, used in Li--Yang's reduction,

\[
 L_{\rm BI}=Y^{17/600+o(1)},\qquad
 K_{\rm BI}=Y^{17/200+o(1)},\qquad
 \eta_{\rm BI}=Y^{-17/150+o(1)},                         \tag{133.15}
\]

and $K_{\rm BI}L_{\rm BI}=1/\eta_{\rm BI}$ in power.  At $Q=H$,

\[
 L_{\rm BI}=Y^{17/300+o(1)},\qquad
 K_{\rm BI}=Y^{17/150+o(1)}=Y^{o(1)}/\eta_{\rm BI}.     \tag{133.16}
\]

Thus $1\le L_{\rm BI}\le K_{\rm BI}\le1/\eta_{\rm BI}\le
K_{\rm BI}L_{\rm BI}$ and $R\le H\ll N$ all hold with power slack
(with equality only at the displayed endpoints in power).

It is safer here to check the primitive first-spacing hypothesis rather
than a later printed simplification.  Li--Yang's condition

\[
 N^{6-q}\gg H^{2q-6}(M^3/T)^{4-q}                       \tag{133.17}
\]

has $Y$-margin

\[
 {102-17q\over300}=0.1031308\ldots>0.                   \tag{133.18}
\]

at (133.13).  Equivalently,

\[
 (M/H)^{(34q-54)/25}T^{(106-51q)/100}\gg1.              \tag{133.19}
\]

There is a literal source-text warning: substituting the same powers into
the displayed purported restatement labelled `condition 1-------`,

\[
 H^{(2q-6)/(6-q)+16/25}M^{34/25}\ll T^{51/100}
 \tag{133.20}
\]

gives left power $1.00279\ldots$, not at most $0.51$.  Direct algebra
from $N_A$ gives (133.19), not (133.20).  The present no-go uses the
primitive green condition (133.17) and, more favorably, grants the final
source bound (133.6), so it is independent of how the source-audit seam
repairs or classifies (133.20).

### 3.3 Variable roles, short intervals, and major/minor arcs

For a source interval centered at $m_0\asymp M$,

\[
 {T\over M^2}F'(m_0/M)=-{T\over m_0^2}\asymp-1.         \tag{133.21}
\]

The sign is removed by the source orientation convention; its magnitude
is approximated by a reduced derivative fraction
$a_{\rm BI}/r_{\rm BI}$.  This immediately separates the variable
roles:

| Project/source item | Range and meaning | Exact map or mismatch |
|---|---|---|
| project $(a,b)$ | primitive ray, $|a|\asymp Y^{1/6}$, $b\asymp Y^{1/2}$, $|a/b|\asymp Y^{-1/3}$ | maps to the original source summation variables $(h,m)$, after sign split |
| source interval $I_{a_{\rm BI}/r_{\rm BI}}$ | a subinterval of the $m=b$ range of length $N=Y^{67/300+o(1)}$ | a proof-internal cut of the project denominator coordinate, not a project cell or lift owner |
| source $a_{\rm BI}/r_{\rm BI}$ | reduced approximation to (133.21), with $r_{\rm BI}\asymp Q\le H$ and normally $|a_{\rm BI}|\asymp r_{\rm BI}$ | not the project ray: its ratio is order one and its denominator is at most $Y^{1/6}$, rather than $Y^{1/2}$ |
| major arcs | short intervals grouped through $r\lesssim R^2/H=Y^{11/100}$, together with the source's grouped large-denominator intervals | no literal project owner; source bounds their total by $MR\log H/\sqrt{HN}$ |
| minor arcs | after Huxley shrinkage, $R\le r_{\rm BI}\le H$, then $r_{\rm BI}\asymp Q$, $a_{\rm BI}\asymp A_{\rm BI}\le Q$ | no bijection with project outer/inner rays; $A_{\rm BI}=0$ also labels source bad intervals |
| source $(k,l)$ | Poisson/Weyl dual variables of sizes $K_{\rm BI},L_{\rm BI}$ | no exact map to project increments $p,q$, determinant $n$, or primitive lifts |

There are $M/N=Y^{83/300+o(1)}$ source short intervals globally, and
$Q_*/N=Y^{69/400+o(1)}$ inside one accepted project top-shell
$b'$-window.  A half-open convention can prevent double counting, but it
does not identify source boundaries with threshold stars, physical cells,
or Möbius/Stieltjes owners.  Applying a triangle inequality after this new
partition would charge the interval pieces; treating the partition as
internal to one source $S$ is legal only after the project coefficient
has first been represented as the source's separated BV weight.  That is
exactly the missing coefficient theorem below.

### 3.4 First-spacing vector, norm, and powers

Li--Yang's first-spacing norm is literally

\[
 G_q=\left\|\sum_{k\asymp K_{\rm BI}}
                 \sum_{l\asymp L_{\rm BI}}a_{kl}
 e(lx_1+klx_2+l\sqrt{k}\,x_3)\right\|_{L^q_\#(
 |x_1|\le1,|x_2|\le1,
 |x_3|\le(\eta L_{\rm BI}\sqrt K_{\rm BI})^{-1})},
 \quad |a_{kl}|\le1.                                    \tag{133.22}
\]

The four-coordinate vector entering the displayed double large sieve is

\[
 \mathbf y_{k,l}=(k,lk,l\sqrt{k},l/\sqrt{k}).             \tag{133.23}
\]

For $Q=Y^s$, its coordinate powers are

\[
\begin{array}{c|c}
\text{coordinate}&Y\text{-power}\\ \hline
k&s-4/75\\
lk&2s-49/300\\
l\sqrt{k}&3s/2-41/300\\
l/\sqrt{k}&s/2-1/12.
\end{array}                                               \tag{133.24}
\]

At $Q=R$ these are respectively
$17/200,17/150,17/240,-17/1200$.  The long $x_3$-side in
(133.22) has power $1/4-3s/2$, equal to $17/400$ at $Q=R$
and $0$ at $Q=H$.

The source permits arbitrary $a_{kl}$ bounded by one, but it does not
permit that coefficient to depend jointly on the approximant
$a_{\rm BI}/r_{\rm BI}$.  The transformed literal coefficient would have
exactly that dependence unless a new separation theorem is proved.  Thus
(133.22)--(133.24) are an exact source ledger, not a project-coordinate
identification.

### 3.5 All four second-spacing coordinates and modular inverses

For one reduced source approximant $a_{\rm BI}/r_{\rm BI}$, let $m_0$
be the associated short-interval center and distinguish the source symbols
from the project centre $c$ and from $\kappa_i\in\{1,4\}$:

\[
\begin{aligned}
 \mu_{\rm BI}&={1\over2}{T\over M^3}F''(m_0/M)
               ={T\over m_0^3}\asymp Y^{-1/2},\\
 \nu_{\rm BI}&={{T\over M^2}F'(m_0/M)-a_{\rm BI}/r_{\rm BI}
                  \over2\mu_{\rm BI}},\qquad |\nu_{\rm BI}|\le1,\\
 c_{\rm BI}&=\left\lfloor r_{\rm BI}{T\over M}F(m_0/M)
                         -\mu_{\rm BI}\nu_{\rm BI}^2\right\rfloor
             \asymp r_{\rm BI}Y^{1/2},\\
 \kappa_{\rm BI}&=\left\{r_{\rm BI}{T\over M}F(m_0/M)
                         -\mu_{\rm BI}\nu_{\rm BI}^2\right\}
             \in[0,1),\\
 a_{\rm BI}\bar a_{\rm BI}&\equiv1\pmod {r_{\rm BI}}.
\end{aligned}                                             \tag{133.25}
\]

The source second-spacing point is

\[
 \mathbf x_{a_{\rm BI}/r_{\rm BI}}
 =\left({\bar a_{\rm BI}\over r_{\rm BI}},
        {\bar a_{\rm BI}c_{\rm BI}\over r_{\rm BI}},
        {1\over\sqrt{\mu_{\rm BI}r_{\rm BI}^3}},
        {\kappa_{\rm BI}\over\sqrt{\mu_{\rm BI}r_{\rm BI}^3}}
   \right).                                               \tag{133.26}
\]

For two such points, the four literal tolerances are

\[
 {1\over K_{\rm BI}L_{\rm BI}},\qquad
 {1\over L_{\rm BI}},\qquad
 {1\over L_{\rm BI}\sqrt K_{\rm BI}},\qquad
 {\sqrt K_{\rm BI}\over L_{\rm BI}}.                   \tag{133.27}
\]

At $Q=Y^s$, their powers, in the order (133.27), are

\[
 {49\over300}-2s,\qquad
 {11\over100}-s,\qquad
 {41\over300}-{3s\over2},\qquad
 {1\over12}-{s\over2}.                                  \tag{133.28}
\]

At $Q=R$ they are
$-17/150,-17/600,-17/240,+17/1200$; at $Q=H$ they are
$-17/100,-17/300,-17/150,0$.  Also
$(\mu r^3)^{-1/2}$ itself has power $1/4-3s/2$, ranging from
$17/400$ down to $0$.

Although the primitive project ray supplies an unrelated inverse
$\bar a\pmod b$, that does not map (133.26): $b\asymp Y^{1/2}$, while
$r_{\rm BI}\le Y^{1/6}$, and $c_{\rm BI}$ is an interval-dependent
integer floor rather than the real project centre.  Likewise the source
$\kappa_{\rm BI}\in[0,1)$ is a fractional part, not the project constant
$\kappa_i=1$ or $4$.  An identification of these symbols would be a
role error, not a change of notation.

The Li--Yang TeX displays the double-large-sieve factor
$V B(A,Q;V)$ and says that $V$ is chosen to minimize it, but gives no
literal formula there for $V$ or $B(A,Q;V)$; it imports the resulting
Huxley/Bourgain--Watt estimate.  Consequently the permitted source itself
provides no additional project value for those two symbols.

### 3.6 Coefficients, projective norms, owners, and absolute-value direction

The accepted project norms are

\[
 \|A_i\|_\infty\ll Y^\epsilon/L,\qquad
 \|A_i\|_2^2\ll Y^\epsilon D/L,\qquad
 \|A_i\|_1\ll Y^\epsilon D,                              \tag{133.29}
\]

with respective powers $-8/48,16/48$ for the squared norm, and
$24/48$.  On the top shell,

\[
 Q_*={D^2\over WL}=Y^{19/48},\qquad
 \lambda={YL\over D^3}=Y^{-16/48},\qquad
 K_D=\min(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2})
     =Y^{11/48+o(1)}.                                    \tag{133.30}
\]

The physical birth-block/curvature theorem gives inner row cost $K_D$
after all $L$ numerator positions are reassembled, and (133.29) then
gives the exact accepted complete cost

\[
 \|A_i\|_1K_D=DK_D=Y^{35/48+o(1)}.                       \tag{133.31}
\]

By contrast, atomizing the matrix before oscillation returns the
coefficient-blind $Y^{43/48+o(1)}$ capacity.  Neither cost is a source
projective-BV norm.

To state the missing interface precisely, define the normalized two-wave
projective cost to be the infimum of

\[
 \mathcal P=\sum_\nu |\lambda_\nu|
 \prod_{j=1}^2
 \bigl(\|g_{\nu,j}\|_{BV,*}\|G_{\nu,j}\|_{BV,*}\bigr)  \tag{133.32}
\]

over exact identities, on the literal lattice and with every owner fixed,

\[
 L^2 C_i(r,r')
 =\sum_\nu\lambda_\nu
 g_{\nu,1}(a/L)G_{\nu,1}(b/D)
 \overline{g_{\nu,2}(a'/L)G_{\nu,2}(b'/D)}.              \tag{133.33}
\]

No accepted estimate bounds (133.32).  The following table locates each
failure rather than suppressing it.

| Literal item | Source receptacle | Outcome/cost |
|---|---|---|
| primitive lift selector and Möbius reassembly | none in (133.11); at most a divisor expansion after physical reassembly | divisor count is $Y^\epsilon$, but variable primitive moduli and $\rho$-dependent profiles remain joint |
| Stieltjes thresholds and sampled profiles | one-variable $g$ or $G$ only after a separable representation | splitting before physical reassembly changes the coefficient and its allowed absolute value |
| M1 denominator quarter carrier | $G$, or an additive $m/4$ phase not present in (133.11) | normalized BV cost $D/L=Y^{1/3}$ if treated as a weight; exact phase insertion makes $F$ depend on $h$ |
| M2 numerator $\chi_4$ carrier | $g$ after a sign split | normalized carrier alone has $O(1)$ BV cost, but lift, primitivity, and pair owners still do not separate |
| reciprocal aliases | source Poisson aliases only after its own short-interval transform | no bijection with the physical project aliases |
| $n>0$ and determinant taper | a four-variable one-sided kernel | absent from one $S$; requires (133.33) or an additional projection theorem |
| stars, cells, threshold equalities, sign and shell faces | half-open $O(1)$ or polylogarithmic families when already separated | cannot be deleted; source interval boundaries are an additional, nonaligned family |
| source inner $a_{kl}$ | one vector coefficient with $|a_{kl}|\le1$ | transformed project coefficient would also depend on the outer approximant label, outside (133.22) |

There is also a direction mismatch.  The source reaches

\[
 \sum_{I_{a_{\rm BI}/r_{\rm BI}}\in\mathcal C(A,Q)}
 \left|\sum_{k,l}e(\mathbf x_{a_{\rm BI}/r_{\rm BI}}
                    \cdot\mathbf y_{k,l})\right|,        \tag{133.34}
\]

and bounds this positive sum by Hölder/double large sieve.  The project
asks for one final modulus of the signed sum (133.10).  Passing from
(133.10) to (133.34) is a legal upper-bound triangle only after the
coefficient has been assigned to source arcs, but it deletes precisely the
cross-ray/arc cancellation needed below $27/48$.  Reversing (133.34) to
recover signed cancellation is not a source conclusion.  A row or SVD
decomposition merely replaces (133.10) by the positive nuclear/row energy
already excluded by the accepted obstruction.

### 3.7 The only direct one-$S$ chart for the joint phase is range-illegal

The determinant identity suggests a second exact phase chart:

\[
 h_{\det}=n,\qquad m_{\det}=bb',\qquad
 H_{\det}\asymp {D^2\over W}=Y^{9/16},\qquad
 M_{\det}\asymp D^2=Y,\qquad T_{\det}=c/\kappa_i,\qquad
 F(z)=z^{-1}.                                             \tag{133.35}
\]

Then $h_{\det}T_{\det}M_{\det}^{-1}F(m_{\det}/M_{\det})$
is exactly $cn/(\kappa_i bb')$.  This does not give a source $S$:
$m_{\det}=bb'$ is a product fibre rather than an independent interval,
$n$ is correlated with it, and the coefficient retains all divisor and
owner multiplicities.  More decisively, $M_{\det}\asymp T$.  Source
Case (B) requires $M\ll T^{1/2}$, while source Case (A), in its
$M>T^{9/16}$ branch, requires

\[
 H\ge M^{11}T^{-6}=T^5,
 \tag{133.36}
\]

which contradicts $H_{\det}=T^{9/16+o(1)}$.  Thus the sole literal
two-variable collapse of the joint phase is source-range illegal even
before its product-fibre coefficient is considered.

### 3.8 $S/H$, aligned packets, and the full capacity ledger

Using the source's optimized $q_x$ in its final $S/H$ formula at
$x=-1/3$ gives (133.6).  A normalized project wave has the factor
$L^{-1}=H^{-1}$, so the most favorable separated two-wave consequence is
(133.7).  Its exact gaps are

\[
\begin{aligned}
 2E_*-{27\over48}
   &={40\sqrt{170}-443\over1200}>0,\\
 2E_*-{24\over48}
   &={5\sqrt{170}-46\over150}>0,\\
 {35\over48}-2E_*
   &={643-40\sqrt{170}\over1200}>0.
\end{aligned}                                             \tag{133.37}
\]

Thus a fictitious free factorization could improve the accepted
$35/48$ capacity, but it cannot supply the frozen strict threshold.
Any actual positive projective, owner, arc, or projection cost only worsens
this comparison.

The exact same-denominator controls show where the source spacing route is
also structurally diagonal.  For M1, take $b'=b,a'=a-t$, so
$n=bt>0$, $1\le t\lesssim D/W$, and the phase is $e(ct/b)$, coherent
at integral $c/b$.  For M2, take $a'=a-2j$, so the character product is
$(-1)^j$ and the phase $e(cj/(2b))$ is coherent at odd-integral
$c/b$.  Both members have the same source $m=b$, hence the same source
short interval and derivative approximant.  Their first/second-spacing
distance is diagonal rather than separated; the positive source norms do
not create a signed estimate for them.

With

\[
 {D\over W}=Y^{3/48},\qquad {WL\over D}=Y^{5/48},
 \qquad K_D=Y^{11/48+o(1)},                               \tag{133.38}
\]

one aligned packet has upper capacity

\[
 D{D/W\over L}K_D=Y^{30/48+o(1)},                        \tag{133.39}
\]

and the full packet cover recovers $Y^{35/48+o(1)}$ only as a
worst-case upper capacity.  The complete ladder is

\[
 \underbrace{Y^{35/48}}_{\text{accepted complete}}
 \longrightarrow
 \underbrace{Y^{31/48}}_{\text{formal square-root residue}}
 \longrightarrow
 \underbrace{Y^{30/48}}_{\text{one aligned packet}}
 \longrightarrow
 \underbrace{Y^{27/48}}_{\text{one term per ray}}
 \longrightarrow
 \underbrace{Y^{24/48}}_{\text{determinant target}}.     \tag{133.40}
\]

The source best case (133.7) lies at $30.1414\ldots/48$, above the
one-term-per-ray threshold.  Equations (133.39)--(133.40) are not lower
bounds; physical amplitudes and outer signs may cancel.

## 4. First doubtful or unproved step

After the exact phase identity (133.2), the first unproved project step is
not a spacing estimate.  It is the coefficient-and-owner assertion
(133.33) with a source-compatible transformation of every term through the
same short intervals, derivative approximants, Poisson variables, and
major/minor arcs, without moving the modulus inside the physical
Möbius/Stieltjes reassembly.

Even a hypothetical version with projective cost $\mathcal P$ would give,
at best,

\[
 |\mathfrak O^+_{i,D}(c)|
 \lesssim Y^{2E_*+\epsilon}\mathcal P.                   \tag{133.41}
\]

To cross $27/48$, (133.41) needs

\[
 \mathcal P\ll
 Y^{-(40\sqrt{170}-443)/1200-\delta};                    \tag{133.42}
\]

to reach $24/48$, it needs

\[
 \mathcal P\ll
 Y^{-(5\sqrt{170}-46)/150}.                              \tag{133.43}
\]

A nonzero rank-one normalized coefficient has natural
$\mathcal P\asymp1$, so (133.42) already asks the coefficient
decomposition itself to contain a new negative power.  Li--Yang's theorem
does not assert such a fact.  The underlying double large sieve does not
repair it: it requires separated first- and second-spacing coefficient
roles and returns the positive absolute-value placement (133.34).

An independent missing hypothesis would still be needed for the aligned
same-$m$ packets, which are diagonal in the source derivative-approximant
space.  Therefore there is no legal positive-margin stratum left after the
first mismatch.  The literal inconsistency (133.17) versus (133.20) is an
additional source-audit warning, not an assumption used to obtain this
no-go.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `single_wave_phase_and_derivative_map` | **Green, phase only:** (133.1)--(133.3) and (133.12) are exact; negative $a$ is handled by conjugation.  The arithmetic carrier is not silently absorbed. |
| `source_parameter_power_ledger` | **Green:** (133.13)--(133.20), the table in Section 3.2, and endpoint values (133.15)--(133.16) compute $q,N,R,Q,K,L,\eta,Q_2$ and all margins.  The printed restatement (133.20) is separately flagged. |
| `project_ray_vs_derivative_approximant_roles` | **Green no-conflation:** project $(a,b)\leftrightarrow(h,m)$; (133.21) proves $a_{\rm BI}/r_{\rm BI}\asymp1$ with $r_{\rm BI}\le L$, so it is not $a/b\asymp Y^{-1/3}$. |
| `joint_coefficient_BV_projective_norm_and_absolute_value_direction` | **Red as an application:** no bound for (133.32)--(133.33); M1 alone has normalized BV carrier cost $Y^{1/3}$, and (133.34) has the wrong positive/arcwise absolute placement for a free signed conclusion. |
| `major_minor_arc_and_short_interval_ownership` | **Red as a project map:** source lengths and thresholds are computed, but its $Y^{83/300}$ interval family and rational-arc owners do not coincide with literal physical owners. |
| `first_spacing_vector_and_norm` | **Green source ledger, red project identification:** (133.22)--(133.24) retain the arbitrary $a_{kl}$ norm and all four vector coordinates; no exact map to $p,q,n$ exists. |
| `second_spacing_four_coordinates_and_modular_inverses` | **Green source ledger, red project identification:** (133.25)--(133.28) retain both modular coordinates, both real coordinates, all tolerances, coprimality, the integer $c_{\rm BI}$, and fractional $\kappa_{\rm BI}$. |
| `same_denominator_M1_M2_aligned_packets` | **Green hostile control:** the M1/M2 packets are source-short-interval and derivative-approximant diagonal, with capacity (133.39); no family lower bound is asserted. |
| `S_over_H_to_Y_capacity` | **Red for the frozen target:** even free two-wave use gives (133.7), $30.1414\ldots/48>27/48$. |
| `capacity_35_27_24_over_48` | **Green:** (133.37)--(133.40) price the accepted, persistence, and determinant levels, including the $31/48$ and $30/48$ controls. |
| `no_positive_energy_or_global_promotion` | **Green:** no Gram, SVD, row energy, or source spacing count is advertised as signed cancellation; no complete exponent or downstream theorem is promoted. |

The work was entirely analytical, algebraic, and source-textual.  No
numerical experiment was used; decimals only display exact radical or
rational-power calculations.

## 6. Dependencies and exact artifacts used

Only the selected context in the task brief was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at SHA-256
   `465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`,
   especially the accepted reduced-Farey norms, complete top-shell
   $Y^{35/48}$ theorem, determinant-residue chart, residue-interlacing
   obstruction, and Round-132 hyperbolic applicability obstruction;
3. `state/active_campaign.yml` for Round 133;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. `sources/li_yang_2023.md`;
6. `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`, especially
   `definition of S`, the two `condition on F` equations, `definition of
   N`, `definitions of parameters`, `definition of Q`, `original form`,
   the displayed double-large-sieve inequality, `x sub a/r`, and
   `con1`--`con4`;
7. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/synthesis.md`;
8. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md`;
9. `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/synthesis.md`; and
10. `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/conductor_round132_hyperbolic_decoupling_adjudication.md`.

No Round-133 sibling report, conductor candidate, unlisted Round-95
artifact, web source, or numerical computation was read.

## 7. Recommended state effect

**Retain** `GC-W7-16-actual-reduced-determinant-correlation` as open and
record this report only as candidate evidence for a scoped
`source_level_no_go`:

* retain the exact phase dictionary (133.1)--(133.3) and the source power,
  first-spacing, and second-spacing ledgers;
* reject the identification of project rays with source derivative
  approximants;
* reject a direct application of Li--Yang $S$ or its displayed
  double-large-sieve inequality to the literal joint coefficient without
  (133.33), correct owner/absolute-value placement, and a separate aligned
  same-denominator estimate;
* record that even a zero-cost two-wave source application has exponent
  $2E_*>27/48$, so this source theorem cannot meet the frozen threshold;
* send the algebraic discrepancy (133.17)--(133.20) to the independent
  source-audit seam rather than using it to alter the accepted external
  theorem in this report.

The complete fixed-block bound remains $Y^{35/48+\epsilon}$.  Make no
M9-M1, M9-M2, endpoint, bridge, M9, external Li--Yang, global exponent, or
quarter promotion.  No shared proof-state or synthesis edit is authorized.

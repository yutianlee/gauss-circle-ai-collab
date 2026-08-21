# Round 92 formalization report: canonical M1 and M2 hard cores

Campaign: `m9-canonical-core-formalization`
Task: `canonical_core_formalization_attack`
Role: formalization constructor
Starting graph SHA-256: `1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5`

## 1. Result

Two graph-ready **open theorem targets** can be stated without promoting an
estimate.

- The M1 target is the actual-symbol, centered, four-row Fejer--Gram
  contribution on the first transition-flattened conductor band.  Its target
  is
  \[
    |\mathcal E_{\rm hard}(U)|
    \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}.
    \tag{1.1}
  \]
  Its full-degree positive capacity exceeds (1.1) by
  \(\Gamma_{\rm Gram}=B^6J^{-11/15}\), hence by \(J^{1/6}\) at
  \(B=J^{3/20}\).  The compulsory Toeplitz square root turns this into the
  distinct pre-Gram deficit \(\Gamma_{82}=B^3J^{-11/30}=J^{1/12}\).
  These are one deficit at two norm levels, not two losses.

- The M2 target is the complete signed top-cone cross-row kernel with the
  metric density and every centered discrepancy mode kept in the same
  coefficient:
  \[
    \sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|
    \ll_\varepsilon L^2X^\varepsilon .
    \tag{1.2}
  \]
  A hard block has positive capacity \(L^2X^\varepsilon\sqrt\rho\),
  \(\rho=AJD^3/L^3\gg1\), so its required relative gain is exactly
  \(\rho^{-1/2}\).  Together with the one-count prior owners, (1.2) implies
  the original endpoint target \(|\mathcal T_{\rm end,L}|\ll_\varepsilon
  L^{3/2}X^\varepsilon\).

There is a lawful common **typed capacity interface**: each lane has an exact
hard owner, its actual signed coefficient, a positive capacity, a target, a
required ratio, and a downstream inequality.  There is no lawful common norm.
M1 is quartic at Fejer--Gram level and returns to its pre-Gram correlation by
a factor \((B/U)^{1/2}\); M2 is quadratic cross-row energy, summed in
dyadic \(\ell^1\), and returns to the endpoint row by a factor \(L^{1/2}\).
Identifying these operators, or identifying either with its original row, is
type-wrong.

The exact owner audit also repairs one shorthand ambiguity: the Round-82
same-residue term is outside \(\mathfrak X_{82}\).  It therefore cannot also
be a summand of \(\mathfrak O_{83:86}\) in an identity whose left side is
\(\mathfrak X_{82}\).  The collision-free owner diagram is recorded below.
No M1 estimate, M2 estimate, component obligation, endpoint obligation, M9
node, bridge, or target theorem is proved here.

## 2. Exact statement and hypotheses

**Global conventions and collision-free dictionary.**  Let \(X\ge2\), put

\[
  J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},
  \qquad e_q(z)=e(z/q),\quad e(z)=e^{2\pi iz}.
  \tag{2.1}
\]

All finite dyadic decompositions and fixed smooth seminorms cost
\(X^\varepsilon\).  The symbol \(D_{\rm den}\) below is reserved for the
original denominator scale.  It is never the M1 dual difference, the M1
Fejer length, or the M2 primitive-ray gap.  The two core namespaces are:

| symbol | exact meaning |
|---|---|
| \(C\), \(B=C/T\) | M1 conductor scale and its modulus/numerator scale |
| \(b\asymp B\) | M1 integer numerator/modulus parameter |
| \(\kappa\in\{1/4,1/2,1\}\), \(g_\kappa=4\kappa\) | one of the three M1 parity classes |
| \(M=4b/g_\kappa\), \(K\) | complete-sum modulus and exact class phase, with \((g_\kappa,M,K)=(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\) |
| \(n,m\) | M1 stationary Fourier indices; they are not the M2 cone coordinate |
| \(d\) | M1 integer dual difference |
| \(U\) | M1 deep dyadic/Fejer length, with \(u\) its integer Fejer shift |
| \(A_{\rm c},B_{\rm c},V_{\rm c}\) | M1 complete physical-cell increments; \(B_{\rm c}\) is the earlier \(B_2\), not the scale \(B\) |
| \(L\) | M2 dyadic top frequency scale |
| \(h,s\) | M2 original odd row frequencies |
| \(m_{\rm cone}\) | M2 original cone lattice coordinate |
| \(a,b,g\) | M2 primitive odd coprime ray and odd lift, \(h=ga,s=gb\); these are unrelated to the M1 \(b\) |
| \((A,D,K,G,R)\) | M2 dyadic scales for \(a\), \(b-a\), reciprocal integer \(k\), odd lift \(g\), and metric resolution; they are typed M2 labels, not M1 variables |
| \(k,r\) | M2 reciprocal Poisson integer and metric Fourier mode |

Stars, equality samples, both frequency signs, height floors, half-open
shells, fixed physical collars, hard endpoints, and zero extension are part
of the objects.  A displayed positive-frequency M2 row carries its conjugate
negative-frequency row and the single outer \(2\Re\) exactly once through
the owner map.

**Open M1 canonical-core theorem.**  Assume

\[
  J^{13/18}<C\le J^{3/4},\qquad B=C/T,qquad M\asymp B,
  \tag{2.2}
\]

and fix one exact transition-flattened smooth nonaxial principal component,
one class \(\kappa\), one alias, one phase sign, and one reflected
orientation.  Let

\[
 S(n,K;M)=\sum_{x\bmod M}^{*}e_M(nx+K\bar x),
 \qquad c_M(d)=\sum_{x\bmod M}^{*}e_M(dx).
 \tag{2.3}
\]

Let \(I_b(n)\) be the Fourier transform of the actual Round-81 globally-BV
principal symbol, including its exact class constants, floors, stationary
entry/exit convention, and zero extension.  Its phase-removed stationary
profile has size

\[
  \mathsf H_{\rm stat}={C\sqrt T\over J},
  \tag{2.4}
\]

and the normalized physical row is

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_{n\in\mathbb Z}I_b(n)e_M(nx)e(n\theta),
 \qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
 \tag{2.5}
\]

For an ordered pair \(P=(x,y)\) of distinct units modulo \(M\), define

\[
 F_{b,P}(\theta)=e_M\!\left(K(\bar x-\bar y)\right)
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
 \tag{2.6}
\]

Put

\[
 D_0=\lfloor J^{17/30}\rfloor,
 \quad D_1=\lfloor J^{87/140}\rfloor,
 \quad E_*=\lfloor Q^2J^{-1/20}\rfloor=\lfloor J^{3/4}\rfloor,
 \tag{2.7}
\]

and let \(\Delta_b\asymp Q^2\) be the exact diameter of the active
stationary support.  For every accepted smooth dyadic multiplier
\(\Pi_{b,U}\) whose zero-extended support lies in

\[
 \mathscr D_{b,U}\subset
 \{d\in\mathbb Z:D_1<|d|<\Delta_b-E_*\},
 \tag{2.8}
\]

set \(f_{b,P}=\Pi_{b,U}F_{b,P}\) and

\[
 H_{b,U}=\sum_{P:x\ne y}f_{b,P}.
 \tag{2.9}
\]

Then the exact coefficient identity is

\[
 \widehat H_{b,U}(d)=\Pi_{b,U}(d){1\over M^2}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
 \tag{2.10}
\]

Let \(D_U(\theta)=\sum_{1\le j\le U}e(j\theta)\) and define

\[
 \mathcal E_U=\sum_{b\asymp B}\int_{\mathbb T}
 |D_U(\theta)|^2|H_{b,U}(\theta)|^2\,d\theta,
 \qquad \mathcal K_U^\circ=|D_U|^2-U.
 \tag{2.11}
\]

For complete cell increments, define the literal four-point trace

\[
\begin{aligned}
 \mathfrak T_M(u,A_{\rm c},B_{\rm c},V_{\rm c})
 :=M\!\sum_{\substack{x\bmod M:\;x,x-A_{\rm c},x-V_{\rm c},
              x-V_{\rm c}-B_{\rm c}\in(\mathbb Z/M\mathbb Z)^\times\\
              A_{\rm c}\not\equiv0,\ B_{\rm c}\not\equiv0\ (M)}}
 e_M\!\left(
 ux+K\left[\bar x-\overline{x-A_{\rm c}}
 -\overline{x-V_{\rm c}}+\overline{x-V_{\rm c}-B_{\rm c}}\right]
 \right).
\end{aligned}
\tag{2.12}
\]

This is the normalization for which \(M^{-5}\mathfrak T_M\) is the
\(M^{-4}\) product of two normalized ordered-pair rows followed by the
complete base-point sum.  Put

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).
 \tag{2.13}
\]

On \(u\ne0\), let \(\mathscr C_{87}\) be the exact same-group set;
on its complement let \(\mathscr C_{88,{\rm coarse}}\) be the shells
\(1<R_*\le\rho_*\); on both complements let
\(\mathscr C_{88,{\rm good}}\) be the certified good-prime set
\(\mathfrak a\ge M^2/\rho_*^2\); and on all earlier complements let
\(\mathscr C_{89,{\rm safe}}\) be the fixed certified complete-cell
union whose cellwise directed-degree sum satisfies the accepted Round-89
condition.  Here

\[
 \rho_*=\min\!\left(M,\lfloor J^{11/30}B^{-2}\rfloor\right).
 \tag{2.14}
\]

The hard cell set is the literal set complement

\[
 \mathscr C_{\rm hard}:=\mathscr C_{\rm all}(u\ne0)
 \setminus(\mathscr C_{87}\sqcup\mathscr C_{88,{\rm coarse}}
 \sqcup\mathscr C_{88,{\rm good}}\sqcup\mathscr C_{89,{\rm safe}}).
 \tag{2.15}
\]

It therefore has \(R_*>\rho_*\) and \(\mathfrak a<M^2/\rho_*^2\), and
retains the residual bad-prime cells, full nonunit union,
affine/full-phase and projection-only periods, shallow good-prime lifts,
aperiodic factors, all signs, all nonzero modulus multiples, and the full
\(2\)-adic branch.  With the factor
\(\Pi_{b,U}(d+u)\overline{\Pi_{b,U}(d)}\) understood literally, define

\[
\begin{aligned}
 \mathcal E_{\rm hard}(U)
 ={}&\sum_{b\asymp B}\sum_{\sigma\in\mathscr C_{\rm hard}}
 \sum_{0<|u|<U}(U-|u|)
 \sum_{d,n,m}^{\rm deep}
 \Pi_{b,U}(d+u)\overline{\Pi_{b,U}(d)}
 {\Omega_{b,d,u}(n,m)\over M^5}\\
 &\hspace{22mm}\times
 e_M(dV_{\rm c}+nA_{\rm c}-mB_{\rm c})
 \mathfrak T_M(u,A_{\rm c},B_{\rm c},V_{\rm c}).
\end{aligned}
\tag{2.16}
\]

The summation label \(\sigma\) includes its complete
\((A_{\rm c},B_{\rm c},V_{\rm c})\)-fibre; `deep` means that both
\(d\) and \(d+u\) lie in the literal zero-extended multiplier supports.
The open theorem is (1.1), uniformly in every displayed choice.  The
finite number of classes, aliases, signs, and orientations is absorbed by
\(X^\varepsilon\).

The corresponding exact one-count owner diagram is

\[
\begin{aligned}
 \mathfrak S_{82}
 &=\mathfrak O_{82,{\rm same}}+\mathfrak X_{82},\\
 \mathfrak X_{82}
 &=\mathfrak O_{83:d=0}+\mathfrak O_{84:0<|d|\le D_0}
   +\mathfrak O_{86:D_0<|d|\le D_1}
   +\mathfrak O_{85:{\rm edge/errors}}
   +\sum_U\sum_{b\asymp B}H_{b,U}(0),\\
 \mathcal E_U
 &=\mathcal E_{U,u=0}+\mathcal E_{87}
   +\mathcal E_{88,{\rm coarse}}+\mathcal E_{88,{\rm good}}
   +\mathcal E_{89,{\rm safe}}+\mathcal E_{\rm hard}(U).
\end{aligned}
\tag{2.17}
\]

Every line is a partition by successive complements.  In particular,
the same-residue owner occurs in the first line only; the integer
\(u=0\) occurs in the last line only; and nonzero \(u\equiv0\pmod M\)
remain in the appropriate nonzero-shift cells.

**Open M2 canonical-core theorem.**  Let
\(D_{\rm den}=\lfloor J\rfloor\) be the top original denominator block,
with its literal Vaaler height floor, and let
\(1\le L\le X^{1/4}=J^{1/2}\) be a dyadic frequency scale inside the
actual finite support.  Define

\[
 \mathcal T_{\rm end,L}
 =\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
  \sum_{\lceil h/4\rceil\le m_{\rm cone}\le h}
  \chi_4(h)a_{\rm end}(h,m_{\rm cone})
  e(\sqrt{Xhm_{\rm cone}}).
 \tag{2.18}
\]

The coefficient \(a_{\rm end}\) is the actual normalized
Vaaler/profile symbol, not a bounded surrogate.  It contains the height
floor, stars/equality convention, the hard affine lower edge
\(m_{\rm cone}=\lceil h/4\rceil\), the upper support edge, and the fixed
profiles.

After the accepted transposed-row Cauchy, write the surviving positive
offsets as

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,qquad
 a<b<4a,qquad a,b,g\ {\rm odd}.
 \tag{2.19}
\]

Put

\[
 q={b-a\over2},\quad v={a+b\over2},\quad
 u={q\over v+\sqrt{v^2-q^2}},\quad
 \Lambda={X(\sqrt b-\sqrt a)^2\over2}=Xqu,
 \tag{2.20}
\]

so the literal open reciprocal interval is

\[
 {Ju\over1-u}<k<{2Ju\over1+u}.
 \tag{2.21}
\]

For \(h=ga,s=gb\),

\[
 \Omega_{h,s,g}:={X(\sqrt s-\sqrt h)^2\over2g}=\Lambda,
 \qquad
 (-1)^q=\chi_4(ga)\chi_4(gb).
 \tag{2.22}
\]

Let \(A^\circ_{h,s}(x)\) be the complete accepted collar-extracted
coefficient.  It retains the exact \(\Phi\), \(q_X\), both fixed
profiles, floors, stars, finite odd-lift support, saddle entry/exit, and
the symmetric pre-collar Poisson convention.  The complete carrier is

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)dx.
 \tag{2.23}
\]

On a residual dyadic block
\(a\asymp A\), \(b-a\asymp D\), \(k\asymp K\),
\(g\asymp G\), let \(W_R\) be the fixed smooth period-one punctured
metric partition member, with its exact tie convention, and write

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad \mu_R\asymp R^{-1}.
 \tag{2.24}
\]

For the literal cutoff \(\omega(k)\), define

\[
\begin{aligned}
 \mathcal K_{R;h,s,g}(x)
 &=\sum_{k\ {\rm in}\ (2.21)}
   \omega(k)W_R(\Omega_{h,s,g}/k)e(kx),\\
 \mathcal K_{r;h,s,g}(x)
 &=\sum_{k\ {\rm in}\ (2.21)}
   \omega(k)e\!\left(kx+{r\Omega_{h,s,g}\over k}\right),\\
 \mathcal K_R&=\mu_R\mathcal K_0+
   \sum_{r\ne0}\widehat W_R(r)\mathcal K_r.
\end{aligned}
\tag{2.25}
\]

The residual ray set consists exactly of primitive odd nonsquare rays
after removal of the square/common-squarefree family, exact nonsquare
centres, all fixed collars and endpoint/equality owners, and the positive
safe blocks.  Let \(\mathcal G_{a,b}\) be the literal finite odd-lift set
remaining after those removals.  The one-count block is

\[
\boxed{
\begin{aligned}
 \mathfrak Q_{A,D,K,G,R}
  ={}&\sum_{\substack{a,b\ {\rm residual}}}
       \sum_{g\in\mathcal G_{a,b}}
       \chi_4(ga)\chi_4(gb)\\
 &\times\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)
 \mathcal K_{R;ga,gb,g}(x)\,dx .
\end{aligned}}
\tag{2.26}
\]

With

\[
 \rho={AJD^3\over L^3},
 \tag{2.27}
\]

the hard index set is the strict-metric side \(\rho\gg1\); the bounded
transition \(\rho\asymp1\) is assigned to the fixed boundary owner.  The
open theorem is exactly (1.2), with density and discrepancy not separated.

For completeness, if

\[
 R_{m_{\rm cone}}=\sum_{\substack{h\ {\rm in\ the\ actual\ odd\ support}\\
                     m_{\rm cone}\le h\le4m_{\rm cone}}}
 \chi_4(h)a_{\rm end}(h,m_{\rm cone})e(\sqrt{Xhm_{\rm cone}}),
 \quad
 \mathcal E_L^{\rm top}=\sum_{m_{\rm cone}}|R_{m_{\rm cone}}|^2,
 \tag{2.28}
\]

then the exact one-count owner diagram, with each later set intersected
with every earlier complement, is

\[
\begin{aligned}
 \mathcal T_{\rm end,L}&=\sum_{m_{\rm cone}}R_{m_{\rm cone}},
 \qquad |\mathcal T_{\rm end,L}|^2\ll L\mathcal E_L^{\rm top},\\
 \mathcal E_L^{\rm top}
 &=\mathcal O_{\rm diag}+\mathcal O_{77}
   +\mathcal O_{78,{\rm square}}
   +\mathcal O_{79,{\rm exact\ ns}}
   +\mathcal O_{79,\rho\lesssim1}
   +\mathcal O_{\rm boundary/profile}
   +2\Re\sum_{\rho\gg1}\mathfrak Q_{A,D,K,G,R}.
\end{aligned}
\tag{2.29}
\]

Here \(\mathcal O_{77}\) owns the fixed collars, full endpoint samples,
zero and positive Poisson modes, wrong-sign/nonstationary tails, equality
modes, and stationary entry/exit errors; \(\mathcal O_{78,{\rm square}}\)
owns the signed square/common-squarefree family including its exact and
metric resonances; \(\mathcal O_{79,{\rm exact\ ns}}\) owns the at-most-one
exact nonsquare ray and its divisor modes; and
\(\mathcal O_{79,\rho\lesssim1}\) owns every positive-safe block.
The boundary/profile packet owns the bounded ratio boundary and every
explicit actual-profile endpoint convention once.

**Typed common interface and capacities.**  For either lane let

\[
 \mathbf I=(\mathscr H,\mathscr O,\mathcal S,
             \operatorname{Cap},\operatorname{Tar},
             \operatorname{Gain},\mathcal D),
 \qquad
 \operatorname{Gain}:={\operatorname{Tar}\over\operatorname{Cap}},
 \tag{2.30}
\]

where \(\mathscr H\) is the hard complement of the one-count owners
\(\mathscr O\), \(\mathcal S\) is the literal signed functional, and
\(\mathcal D\) is its lane-specific downstream inequality.  The lawful
instances are

| lane | norm level and \(\mathcal S\) | positive capacity | target | required gain | downstream map |
|---|---|---:|---:|---:|---|
| M1 | four-row Fejer--Gram; \(\mathcal E_{\rm hard}(U)\) | \(\frac UB\mathsf C_{82}^2\) | \(\frac UB\mathsf T_{82}^2\) | \(\Gamma_{82}^{-2}\) | \(|\sum_bH_{b,U}(0)|^2\ll X^\varepsilon(B/U)\mathcal E_U\) |
| M2 | two-row character energy, dyadic \(\ell^1\); \(\sum|\mathfrak Q|\) | \(L^2\sqrt\rho\) per hard block | \(L^2\) | \(\rho^{-1/2}\) | \(|\mathcal T_{\rm end,L}|^2\ll L\mathcal E_L^{\rm top}\) |

Here

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},\quad
 \mathsf T_{82}=J^2/T=J^{7/5},\quad
 \Gamma_{82}=B^3J^{-11/30}.
 \tag{2.31}
\]

The interface (2.30) is bookkeeping, not a shared analytic theorem.

## 3. Proof or derivation

For M1, summing (2.6) over distinct ordered pairs gives

\[
 \sum_{x\ne y}^{*}e_M\!\left(dx+n(x-y)+K(\bar x-\bar y)\right)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).
 \tag{3.1}
\]

The unrestricted pair sum is the Kloosterman product and the deleted
diagonal \(x=y\) is exactly the Ramanujan sum.  The two normalized rows
supply \(M^{-2}\), proving (2.10).  The R82--R86 exact partitions then
give the first two lines of (2.17); in particular, (3.1) retains negative
\(d\), nonzero multiples of \(M\), and \(c_M(d)\).

Expanding (2.11) gives

\[
 \mathcal E_U^\circ
 =\sum_b\sum_{0<|u|<U}(U-|u|)
   \sum_d\widehat H_{b,U}(d+u)
          \overline{\widehat H_{b,U}(d)}.
 \tag{3.2}
\]

The bijection

\[
 P=(x,x-A_{\rm c}),\qquad
 P'=(x-V_{\rm c},x-V_{\rm c}-B_{\rm c})
 \tag{3.3}
\]

turns the product phase into
\(e_M(dV_{\rm c}+nA_{\rm c}-mB_{\rm c})\) times (2.12), and turns the
four Fourier weights into (2.13).  This proves (2.16) and the final line
of (2.17).  The global \(u=0\) coefficient was removed before the cell
partition; every cell set is then taken on successive complements, so
there is no double ownership.

For a finite coefficient vector, the Toeplitz matrix
\(T_U(i,j)=U-|i-j|\) is positive and satisfies

\[
 \left|\sum_{j=1}^Ua_j\right|^2
 \le {2\over U}\,a^*T_Ua.
 \tag{3.4}
\]

After zero padding, the two signs, the smooth dyadic partition, and
Cauchy over \(b\asymp B\), this yields

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon{B\over U}\mathcal E_U.
 \tag{3.5}
\]

Thus (1.1) plus the already bounded owners in (2.17) gives
\(|\sum_bH_{b,U}(0)|\ll X^\varepsilon J^{7/5}\), after harmless
relabeling of \(\varepsilon\), and hence the Round-82 coefficient target
after summing \(U\).

The row, pair, and Gram normalizations are respectively

\[
 Q^{-5/24},\qquad Q^{-5/12},\qquad Q^{-5/6};
 \tag{3.6}
\]

the last is the product of four rows, not an extra factor on a pair.
For a late directed graph of maximum in/out degree \(\Delta\), the
positive capacity and normalized gap are

\[
 \operatorname{Cap}_{\rm M1}(\Delta)
 =UB^3\Delta T^4Q^{-5/6},\qquad
 {\operatorname{Cap}_{\rm M1}(\Delta)
   \over (U/B)J^{14/5}}
 =\Delta B^4J^{-11/15}.
 \tag{3.7}
\]

At full degree \(\Delta\asymp B^2\),

\[
 \mathsf C_{\rm deep}={U\over B}\mathsf C_{82}^2,
 \quad
 \mathsf T_{\rm deep}={U\over B}\mathsf T_{82}^2,
 \quad
 \Gamma_{\rm deep}=\Gamma_{82}^2=B^6J^{-11/15}.
 \tag{3.8}
\]

At \(B=J^{3/20}\), (3.8) is \(J^{1/6}\), and (3.5) takes its
square root to \(J^{1/12}\).  Complete prime-power descent cannot alter
this ledger: the \(p^{2j}\) trace inflation cancels the quotient-square
normalization and the restricted Fejer shifts keep their total mass.
The exact \(q=8\) cell retains full degree, so it falsifies a strict
capacity gain from local period depth; it is not a signed lower bound.

For M2, (2.28) is an exact transposition of (2.18).  Cauchy gives the
first line of (2.29).  The diagonal is \(O(L^2)\); the accepted R77--R79
owners in the second line are \(O_\varepsilon(L^2X^\varepsilon)\); and
the residual positive-offset energy is the single outer \(2\Re\) of the
sum of (2.26).  Therefore (1.2) implies

\[
 \mathcal E_L^{\rm top}\ll_\varepsilon L^2X^\varepsilon,
 \qquad
 |\mathcal T_{\rm end,L}|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
 \tag{3.9}
\]

which is the required original-to-energy implication.

The complete carrier identity is essential in this derivation.  If
\(\theta=\Lambda/k\), then the pre-carrier coefficient factors as
\(\mathfrak B^\circ(g)=e(g\theta/2)\mathfrak C^\circ(g)\).  For
\(\theta=\ell+\eta\), odd \(g\) gives

\[
 (-1)^{q+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^\circ(g).
 \tag{3.10}
\]

Hence quotient parity cancels pointwise.  The same carrier changes every
apparent half-integral metric frequency back to the integer expansion
(2.25), including \(r=0\).  Poisson applied to \(\mathcal K_0\) returns
the original transposed \(\chi_4(h)\chi_4(s)\) row, so density and
discrepancy cannot lawfully be assigned separate closing estimates.

Finally, the R79 positive block ledger is

\[
 A\sqrt G\sqrt J D^{3/2}
 \asymp L^2\sqrt{AJD^3/L^3}=L^2\sqrt\rho,
 \tag{3.11}
\]

using \(G\asymp L/A\).  Thus \(\rho\lesssim1\) is already safe and the
strict hard side requires the exact factor \(\rho^{-1/2}\), proving the
M2 capacity row of (2.30).

The outside-core scope is as follows.

| lane | already owned but outside the hard core | still separate and open after the core estimate |
|---|---|---|
| M1 | lower fixed-interior conductors; first-band same-residue, \(d=0\), \(|d|\le D_1\), support edge/errors, global \(u=0\), and certified R87--R89 packages; first-band transition errors and axes have their existing scoped owners | the principal main, transitions, and axes on \(J^{3/4}<C\le J\); raw/cone-edge and other radial sectors; alpha/top interfaces; global angular/radial reconciliation; uniform endpoint assembly |
| M2 | diagonal; R77 collars/modes/errors; signed square rays; exact nonsquare centres; \(\rho\lesssim1\) and bounded boundary blocks; exact profile endpoints | every non-top M2 frequency/denominator packet, unresolved character/near-collision interfaces, target-scale pointwise reconciliation, and uniformity over all \(X^{1/4}\le D_{\rm den}\le X^{1/2}\) |

Consequently (1.1) is sufficient only for its first-band smooth nonaxial
pre-Gram packet, and (1.2) is sufficient only for the displayed hard top
M2 cone together with its listed prior owners.  Neither statement alone
is sufficient for M9-M1 or M9-M2.

## 4. First doubtful or unproved step

The first analytic gap in the M1 core is exactly (1.1).  No accepted
estimate supplies the required full-degree Gram gain

\[
 \Gamma_{\rm deep}^{-1}=B^{-6}J^{11/15},
 \tag{4.1}
\]

which is \(J^{-1/6}\) at the top of the band, or equivalently the
post-Toeplitz pre-Gram gain \(J^{-1/12}\).  The only remaining possible
source is joint cancellation across

\[
 (b,d,u,n,m,A_{\rm c},B_{\rm c},V_{\rm c})
 \tag{4.2}
\]

with the actual fourfold stationary symbol.  Local period depth,
completed descent, graph sparsity, and another complete transform have
already returned at equal capacity.

The first analytic gap in the M2 core is exactly (1.2), already for the
single bracket

\[
 \mu_R\mathcal K_0+
 \sum_{r\ne0}\widehat W_R(r)\mathcal K_r.
 \tag{4.3}
\]

No accepted theorem recovers \(\rho^{-1/2}\) while retaining the actual
moving amplitude and \(\chi_4(h)\chi_4(s)\).  Estimating only the
centered modes leaves the ordinary density term; estimating the density
by adjoint Poisson returns to the starting transposed row.

Even proofs of both gaps would leave the outside-core packets in the last
table of Section 3 and their endpoint/pointwise assemblies.  The common
interface (2.30) supplies no estimate; it only prevents a norm mismatch.

## 5. Required controls and outcomes

| required Round-92 control | outcome |
|---|---|
| `variable_dictionary` | **Pass.**  Section 2 reserves \(D_{\rm den}\), separates M1 \(d,U,A_{\rm c},B_{\rm c},V_{\rm c}\) from M2 \((A,D,K,G,R)\), and separates \(\mathsf H_{\rm stat}\) from \(H_{b,U}\). |
| `M1_linear_and_Gram_normalization` | **Pass.**  Equations (3.5)--(3.8) distinguish pre-Gram target \(J^{7/5}\), Gram target \((U/B)J^{14/5}\), and powers \(Q^{-5/24},Q^{-5/12},Q^{-5/6}\). |
| `M1_one_count_owner_map` | **Pass after explicit shorthand repair.**  Equation (2.17) puts the same-residue owner outside \(\mathfrak X_{82}\), owns integer \(u=0\) once, and takes R87--R89 on successive complements. |
| `M1_full_degree_capacity` | **Pass.**  Equation (3.7) gives the degree-dependent capacity; (3.8) gives the full-degree \(J^{1/6}\) Gram gap and \(J^{1/12}\) square-root gap. |
| `M1_outside_core_scope` | **Pass.**  The Section-3 scope table separates the first-band core from upper conductors, raw/cone edges, axes/transitions, other sectors, alpha/top interfaces, and endpoint assembly. |
| `M2_original_to_energy_implication` | **Pass.**  Equations (2.28)--(2.29) and (3.9) prove that the \(L^2\) energy target yields the \(L^{3/2}\) endpoint target. |
| `M2_density_discrepancy_joint_kernel` | **Pass.**  Equations (2.24)--(2.26) keep \(\mu_R\mathcal K_0\) and all \(r\ne0\) modes inside one \(\mathfrak Q\). |
| `M2_one_count_owner_map` | **Pass.**  Equation (2.29) assigns the diagonal, R77, R78, R79, boundary/profile, and hard residual once by successive complements. |
| `M2_hard_ratio_capacity` | **Pass.**  Equations (2.27) and (3.11) identify capacity \(L^2\sqrt\rho\), safe side \(\rho\lesssim1\), hard side \(\rho\gg1\), and required gain \(\rho^{-1/2}\). |
| `M2_outside_core_scope` | **Pass.**  The Section-3 table keeps non-top packets, near-collision/character interfaces, pointwise reconciliation, and full denominator endpoint uniformity separate. |
| `actual_coefficients_characters_endpoints` | **Pass.**  The exact M1 \(I_b\), Kloosterman/Ramanujan algebra, three classes, signs, modulus multiples, zero extension, and four weights remain; the exact M2 \(a_{\rm end}\), \(A^\circ\), \(\chi_4(h)\chi_4(s)\), floors, stars, collars, affine edge, and upper edge remain. |
| `false_shadow_table` | **Pass.**  The rejected shadows are listed immediately below. |
| `source_hypothesis_map` | **Pass with no import.**  The literal mismatch table below shows that no current primary-source theorem is an accepted dependency of either new estimate. |
| `graph_forward_pointer_hygiene` | **Revision required, no status change.**  All 224 obligation IDs and references resolve and the graph hash matches, but a direct two-node dependency cycle exists between `M9-M1-product-wavelet-short-numerator-Kloosterman-reduction` and `M9-M1-residual-upper-conductor-offdiagonal-reduction`; the exact repair is proposed in Section 7.  The two missing estimates also need explicit open nodes rather than living only in `next_action` text. |
| `downstream_scope` | **Pass.**  No M9-M1, M9-M2, M9, endpoint-uniformity, conditional bridge, GC-target, or improvement of the accepted \(1/3+\varepsilon\) theorem is asserted. |

The mandatory false-shadow table is:

| rejected shadow | exact failure/control |
|---|---|
| Replace either actual symbol by arbitrary bounded coefficients. | M1 needs the moving fourfold stationary symbol; M2 carrier cancellation and variation are actual-symbol identities. |
| Take absolute values before the signed interaction. | M1 remains at \(\mathsf C_{\rm deep}\); the M2 square-ray Abel majorant is sharply too large and generic density leaves \(L^2\sqrt\rho\). |
| Identify the M1 pre-Gram row with its Gram square. | Their homogeneities are quadratic and quartic in \(I_b\); (3.5), not equality, is their only lawful interface. |
| Count M1 local period depth, Fourier sparsity, or graph labels as a power saving. | Descent preserves Fejer mass, and the exact \(q=8\) residual retains full directed degree. |
| Delete nonzero modulus multiples, \(c_M(d)\), bad-prime/nonunit cells, or the full \(2\)-part. | Each is a literal summand or residual owner in (2.10)--(2.17). |
| Use M2 nearest-integer quotient parity. | Equation (3.10) cancels it pointwise against the complete carrier. |
| Use an apparent half-frequency gap or estimate discrepancy alone. | The carrier restores integer modes including \(r=0\); (4.3) is indivisible for the target. |
| Classify the ordinary \(1/R\) density as exceptional. | R79 proves sharp ordinary metric population; only excess density could admit an inverse classification. |
| Apply another reciprocal Poisson step. | The M1 complete transform and M2 density adjoint both self-return. |
| Infer pointwise endpoint control from an unquantified moment. | Neither the moving-symbol hypothesis nor a pointwise/large-value implication is supplied. |

The source-hypothesis map is:

| possible source class | literal mismatch with the core |
|---|---|
| ordinary Kloosterman large sieve | loses the full M1 factor \(B\) and does not estimate the centered fourfold varying-modulus trace with its joint moving symbol |
| existing bilinear Kloosterman results, including the Li--Yang guardrail | use separated coefficient sequences or one Kloosterman factor; no exact map to (2.16), its modulus variation, four weights, owner masks, and endpoint support is certified |
| local prime-power rational-sum estimates | control local traces but do not aggregate the physical directed graph; completed descent returns at equal capacity |
| Xiao guardrail | no exact variable, weight, modulus, norm, and endpoint map to (2.16) or (2.26) is certified |
| frequency-separation large sieves | M2 lacks separation at the active metric resolution and lacks a common coefficient sequence |
| quadratic-character large sieves | do not match fixed \(\chi_4(h)\chi_4(s)\) coupled to the radical phase and moving amplitude |
| root-spacing/incidence theorems | reproduce only the sharp positive \(1/R\) population, hence the capacity \(L^2\sqrt\rho\) |
| global moment theorems | require an exact moving-symbol hypothesis audit and an explicit pointwise endpoint consequence, neither of which is presently mapped |

The accepted Bourgain reciprocal theorem is used only inside earlier safe
M1 owners; it is not a dependency for (1.1).  Li--Yang and Xiao remain
guardrails only.  No web search, new source import, or numerical experiment
was used.

## 6. Dependencies and exact artifacts used

The construction used completely and only the selected context:

- `protocol.md`;
- `state/proof_obligations.yml`, at graph hash
  `1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5`;
- `state/best_proof_draft.md`;
- `state/active_campaign.yml`;
- `strategy/conductor_0817_full_proof_strategy.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md`;
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_barrier_attack.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/primitive_ray_parity_energy_attack.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/synthesis.md`;
- `rounds/codex-managed/gc-unconditional-exponent-extraction/synthesis.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/briefs/canonical_core_formalization_attack.md`.

No sibling Round-92 report, unlisted historical artifact, external source
card, or web source was read or used.

## 7. Recommended state effect

**Create, but do not promote, two explicit open obligations.**

- `M9-M1-canonical-hard-actual-symbol-Gram-estimate`: statement (1.1)
  with definitions (2.2)--(2.17), dependencies the accepted R82--R90
  reduction/barrier nodes, and a forward pointer to `M9-M1` (or to a
  separately created first-band assembly node).  Add this open node to the
  dependency list of `M9-M1`; proving it would close only the displayed
  first-band smooth nonaxial packet.
- `M9-M2-top-endpoint-density-discrepancy-energy`: statement (1.2) with
  definitions (2.18)--(2.29), dependencies the accepted transposed-energy
  and R77--R80 owner/obstruction nodes, and forward pointer to
  `M9-M2-top-endpoint-signed-cone`.  Add it as an explicit dependency of
  that open cone node.

**Retain** the accepted M1 square-root self-return barrier, the M2 carrier
cancellation/self-return, all R77--R90 owners, and the unconditional
`GC-partial-one-third` theorem without status change.  **Reject** any graph
node that identifies the M1 linear and Gram norms or that separates the M2
density from discrepancy as a sufficient target.

**Repair graph hygiene without mathematical promotion.**  Remove
`M9-M1-residual-upper-conductor-offdiagonal-reduction` from the dependencies
of `M9-M1-product-wavelet-short-numerator-Kloosterman-reduction`; the former
already depends on the latter, so the present reverse dependency creates a
direct cycle.  Put the forward pointer in the latter node's `implies` field
instead, and point the residual reduction forward to
`M9-M1-global-angular-radial-estimate`.  Refresh the stale R82--R89 and
R77--R80 `next_action` text so that it points to the two new canonical open
nodes rather than to already completed intermediate rounds.

No shared-state edit is made by this report.  No status change is licensed
for `M9-M1`, `M9-M1-global-angular-radial-estimate`, `M9-M2`,
`M9-M2-top-endpoint-signed-cone`, `M9-endpoint-uniformity`, `M9`, the
conditional bridge, or `GC-target`.

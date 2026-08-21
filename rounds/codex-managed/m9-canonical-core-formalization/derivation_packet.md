# Round 92 statement packet: canonical M1 and M2 hard cores

Graph SHA-256 at freeze:
1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5.

This packet is statement-only. It freezes accepted identities and open
targets; it does not assert either missing signed estimate.

## 1. Purpose and common conventions

The conjectural target is

\[
 P(X)\ll_\varepsilon X^{1/4+\varepsilon}.
\tag{92.1}
\]

Round 91 proves the unconditional fallback

\[
 P(X)\ll_\varepsilon X^{1/3+\varepsilon}.
\tag{92.2}
\]

The residual Vaaler term R5 is proved pointwise. The target-scale
problem is now entirely in the fully weighted M1 and M2 main sums,
uniformly through their hard endpoints.

Throughout the canonical-core discussion put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5}.
\tag{92.3}
\]

All dyadic logarithms and fixed smooth seminorms cost
\(X^\varepsilon\). Stars, equality samples, both signs, height floors,
hard physical endpoints, and zero extension are literal owners and may
not be discarded.

The original project uses \(D\) for a denominator scale and several
late M1 reports use \(D\) again for a Fejer shift length. In this packet
the latter is renamed \(U\). A formalization must give a complete
dictionary and must not change any exponent or support condition.

## 2. Canonical M1 coefficient-level row

In the first transition-flattened conductor band,

\[
 J^{13/18}<C\leq J^{3/4},\qquad B=C/T,\qquad M\asymp B.
\tag{92.4}
\]

For each of the three parity classes the exact smooth principal row has
the finite Fourier form

\[
 {1\over M}\sum_{n\in\mathbb Z}S(n,K;M)I_b(n),
\tag{92.5}
\]

where \(S(n,K;M)\) is the corresponding complete Kloosterman sum and
\(I_b(n)\) is the Fourier transform of the actual Round-81 globally-BV
principal symbol. Its phase-removed stationary profile has

\[
 \|I_b\|_{\mathrm{stationary}}\asymp
 H={C\sqrt T\over J},
\tag{92.6}
\]

with one-pass entry and exit and aggregate errors already target-safe.
The normalized physical row has the accepted gain

\[
 Q^{-5/24};
\tag{92.7}
\]

an ordered pair has \(Q^{-5/12}\), and a four-row Gram term has
\(Q^{-5/6}\).

After removal of the same-residue mode, literal \(d=0\), all
\(0<|d|\leq D_1\), and the smooth outer support collar, where

\[
 D_1=\lfloor J^{87/140}\rfloor,
\tag{92.8}
\]

the exact coefficient-level survivor is

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{D_1<|d|<\Delta_b-J^{3/4}}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\tag{92.9}
\]

Negative \(d\), nonzero multiples of \(M\), the centered Ramanujan
term, all parity classes, reflected orientations, and the actual
stationary support are included.

Equivalently, if

\[
 f_{b,P}=\Pi_{b,U}F_{b,P},\qquad
 H_{b,U}=\sum_{P:x\ne y}f_{b,P},
\tag{92.10}
\]

then

\[
 \widehat H_{b,U}(d)
 =\Pi_{b,U}(d){1\over M^2}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\tag{92.11}
\]

The exact linear reassembly is

\[
 \mathfrak X_{82}
 =\mathfrak O_{83:86}
  +\sum_U\sum_{b\asymp B}H_{b,U}(0),
\tag{92.12}
\]

where \(\mathfrak O_{83:86}\) owns the same-residue, literal zero,
small-difference, outer-collar, entry/exit, wrong-sign, stationary,
and nonstationary pieces exactly once.

## 3. Canonical M1 Gram core and target

Put

\[
 \mathcal E_U
 =\sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
 |H_{b,U}(\theta)|^2\,d\theta,
\qquad
 \mathcal K_U^\circ=|D_U|^2-U.
\tag{92.13}
\]

There is one global \(u=0\) owner. On \(u\ne0\), successive
complements give the exact one-count partition

\[
 \mathcal E_U^\circ
 =\mathcal E_{87}
  +\mathcal E_{88,\mathrm{coarse}}
  +\mathcal E_{88,\mathrm{good}}
  +\mathcal E_{89,\mathrm{safe}}
  +\mathcal E_{\mathrm{hard}}.
\tag{92.14}
\]

The hard term has

\[
 R_*>\rho_*,
 \qquad
 \mathfrak a<M^2/\rho_*^2,
 \qquad
 \rho_*=\min\!\left(M,\lfloor J^{11/30}B^{-2}\rfloor\right),
\tag{92.15}
\]

and includes only cells not previously owned. It retains residual
bad-prime cells, the full nonunit union, affine/full-phase and
projection-only periods, shallow good-prime lifts, aperiodic factors,
all signs, all nonzero modulus multiples, and all four actual
stationary weights

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).
\tag{92.16}
\]

Its exact displayed form is

\[
\begin{aligned}
 \mathcal E_{\mathrm{hard}}(U)
 ={}&\sum_{b\asymp B}
 \sum_{\substack{R_*>\rho_*,\
                  \mathfrak a<M^2/\rho_*^2\\
                  \sigma\ {\rm not\ previously\ owned}}}
 \sum_{0<|u|<U}(U-|u|)
 \sum_{d,n,m}^{\mathrm{deep}}
 {\Omega_{b,d,u}(n,m)\over M^5}\\
 &\hspace{18mm}\times
 e_M(dV+nA-mB_2)\,
 \mathfrak T_M(u,A,B_2,V).
\end{aligned}
\tag{92.17}
\]

The open canonical M1 Gram inequality is

\[
 \boxed{
 \mathcal E_{\mathrm{hard}}(U)
 \ll_\varepsilon
 X^\varepsilon {U\over B}J^{14/5}.}
\tag{92.18}
\]

The finite Toeplitz inequality gives

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon {B\over U}\mathcal E_U.
\tag{92.19}
\]

Thus (92.18), together with the already owned terms, yields the
Round-82 coefficient target

\[
 \mathsf T_{82}=J^2/T=J^{7/5}.
\tag{92.20}
\]

The absolute/triangle capacity is

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},
\qquad
 \Gamma_{82}={\mathsf C_{82}\over\mathsf T_{82}}
 =B^3J^{-11/30}.
\tag{92.21}
\]

At \(B=J^{3/20}\), \(\Gamma_{82}=J^{1/12}\). At Gram level,

\[
 \mathsf C_{\mathrm{deep}}={U\over B}\mathsf C_{82}^2,
\qquad
 \mathsf T_{\mathrm{deep}}={U\over B}\mathsf T_{82}^2,
\tag{92.22}
\]

so the \(J^{1/6}\) Gram gap square-roots to the same \(J^{1/12}\)
linear gap. This is an equal-capacity barrier, not a lower bound and
not a linear operator involution.

The exact \(q=8\) full-degree cell shows that local period peeling
cannot force a power gain. The only possible gain in (92.18) is joint
signed cancellation across the actual variables

\[
 (b,d,u,n,m,A,B_2,V).
\tag{92.23}
\]

Even (92.18) would close only this first-band smooth nonaxial core.
Upper conductors \(C>J^{3/4}\), axes, raw transitions, cone edges,
other radial sectors, alpha/top interfaces, and final endpoint
uniformity remain separate M1 owners.

## 4. Canonical M2 top-endpoint row

For a dyadic top frequency scale \(1\leq L\leq X^{1/4}\), the literal
M2 endpoint target is

\[
 \boxed{
 \mathcal T_{\mathrm{end},L}
 =\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
  \sum_{\lceil h/4\rceil\leq m\leq h}
  \chi_4(h)a_{\mathrm{end}}(h,m)e(\sqrt{Xhm})
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{92.24}
\]

The symbol \(a_{\mathrm{end}}\) is the actual normalized Vaaler/profile
symbol. It contains the hard affine lower edge, upper support edge,
stars, and fixed profiles.

After the accepted row Cauchy, gcd-lift decomposition, fixed physical
collars, and symmetric Poisson formula, write primitive odd rays

\[
 h=ga,\qquad s=gb,\qquad (a,b)=1,
\tag{92.25}
\]

and define

\[
 \Lambda={X(\sqrt b-\sqrt a)^2\over2},
\qquad
 \Omega_{h,s,g}={X(\sqrt s-\sqrt h)^2\over2g}=\Lambda.
\tag{92.26}
\]

The literal reciprocal interval is

\[
 {Ju\over1-u}<k<{2Ju\over1+u},
\tag{92.27}
\]

in the exact half-angle coordinate \(u\). The complete collared
coefficient is

\[
 \mathfrak C^\circ(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)dx.
\tag{92.28}
\]

The sign is exactly

\[
 (-1)^{(b-a)/2}=\chi_4(ga)\chi_4(gb).
\tag{92.29}
\]

## 5. Canonical M2 density--discrepancy kernel

On a dyadic hard block \((A,D,K,G,R)\), let the smooth metric window be

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
\qquad \mu_R\asymp R^{-1}.
\tag{92.30}
\]

Define

\[
 \mathcal K_{R;h,s,g}(x)
 =\sum_{k\ {\rm in}\ (92.27)}
 \omega(k)W_R(\Omega_{h,s,g}/k)e(kx),
\tag{92.31}
\]

and

\[
 \mathcal K_{r;h,s,g}(x)
 =\sum_{k\ {\rm in}\ (92.27)}
 \omega(k)e\!\left(kx+{r\Omega_{h,s,g}\over k}\right).
\tag{92.32}
\]

Then

\[
 \mathcal K_R=\mu_R\mathcal K_0+
 \sum_{r\ne0}\widehat W_R(r)\mathcal K_r.
\tag{92.33}
\]

The exact one-count hard kernel is

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
\tag{92.34}
\]

The remaining canonical M2 energy inequality is

\[
 \boxed{
 \sum_{A,D,K,G,R}
 |\mathfrak Q_{A,D,K,G,R}|
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{92.35}
\]

The accepted implication from (92.35), together with all prior owners,
is (92.24).

The positive block capacity is

\[
 L^2X^\varepsilon\sqrt{\rho},
\qquad
 \rho={AJD^3\over L^3}.
\tag{92.36}
\]

Blocks with \(\rho\ll1\) are already safe. The hard region is
\(\rho\gg1\), so a new argument must recover the exact factor
\(\rho^{-1/2}\) relative to the positive ledger while retaining the
complete symbol.

Already owned once are:

1. all fixed collars, zero and positive modes, wrong-sign tails,
   equality modes, and stationary entry/exit errors from Round 77;
2. the signed square/common-squarefree family from Round 78;
3. exact nonsquare centers and every positive block
   \(AJD^3\ll L^3\) from Round 79;
4. the bounded boundary range and the explicit actual-profile endpoint
   owners inherited by the one-count partition.

The density term \(\mu_R\mathcal K_0\) and the centered discrepancy
modes must be estimated together. Poisson on \(\mathcal K_0\) restores
the original transposed two-character row. The complete coefficient
carrier cancels quotient parity and shifts the apparent half-integral
Fourier frequencies back to integers, including \(r=0\).

Even (92.35) closes only the displayed hard top M2 cone. All other M2
packets and target-scale endpoint owners must still be reconciled
before promoting M9-M2.

## 6. False shadows and mandatory controls

The following are rejected shadows and may not be used:

1. replacing the actual M1 or M2 symbols by arbitrary bounded
   coefficients;
2. taking absolute values before the required signed interaction;
3. identifying the M1 linear row with its Gram square;
4. treating local M1 period depth, Fourier support, or graph sparsity
   as a power gain without an actual-symbol estimate;
5. dropping nonzero modulus multiples, Ramanujan terms, bad-prime or
   full \(2\)-adic branches;
6. using M2 quotient parity, a half-frequency spectral gap,
   discrepancy alone, or another reciprocal Poisson step;
7. classifying the ordinary \(1/R\) M2 density as exceptional;
8. inferring pointwise endpoint control from an unquantified global
   moment estimate.

Every proposed standalone theorem must audit:

- variable and scale dictionary;
- coefficient and character algebra;
- one-count owner map;
- diagonal and equality conventions;
- row, pair, Gram, and square-root normalizations;
- hard endpoint and zero-extension support;
- current primary-source hypotheses;
- exact downstream scope.

## 7. Source mismatch data

For M1, the ordinary Kloosterman large sieve loses the full factor
\(B\). Existing bilinear Kloosterman theorems treat separated
coefficient sequences or one Kloosterman factor, not the centered
fourfold varying-modulus trace with the joint moving symbol. Local
prime-power rational-sum theorems do not aggregate the physical graph.
Complete Fourier, Poisson, and descent transforms return at equal
capacity.

For M2, standard frequency-separation large sieves require separation
unavailable at the active metric resolution and a common coefficient
sequence. Quadratic-character large sieves do not match the fixed
\(\chi_4(h)\chi_4(s)\) product with a coupled radical phase. Root-spacing
theorems reproduce only the sharp positive \(1/R\) population.
Moment theorems must be checked for the literal moving symbol and for a
pointwise endpoint consequence.

Li--Yang and Xiao are guardrails only until their exact hypotheses are
mapped to (92.17) or (92.34). No theorem from either source is an
accepted dependency of this packet.

## 8. Round-92 completion rule

The round succeeds if it produces:

1. one self-contained, graph-ready M1 core statement and owner map;
2. one self-contained, graph-ready M2 core statement and owner map;
3. exact capacity and required-gain ledgers in a common notation;
4. a false-shadow and source-mismatch table;
5. an explicit statement of which additional M1/M2 owners remain
   outside the two cores.

Formalization alone does not prove (92.18), (92.24), or (92.35).
No M9-M1, M9-M2, M9, endpoint, bridge, or target promotion is licensed
without a new signed estimate and complete downstream assembly.

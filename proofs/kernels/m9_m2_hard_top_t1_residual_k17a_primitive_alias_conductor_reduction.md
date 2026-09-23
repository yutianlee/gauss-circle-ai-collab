# Kernel: K17a primitive alias-conductor reduction

## Lemma

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\},
\tag{177.K1}
\]

and fix \(0<\delta<1/2\) and \(0<\gamma<1\). Retain the complete literal
Round-176 two-orientation identity on

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa=\kappa_*<\delta L,\qquad
 (u,n)<\gamma L,
\tag{177.K2}
\]

including the exact residual coefficient
\(\lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d)\), both parity branches,
squarefreeness, coprimality, the Fejer factor, opposing-displacement
inequalities, profiles, floors, stars, hard values, endpoint conjugations,
one outer real part, and full-line zero extension.

For every gcd stratum put

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad (n_0,u_0)=1.
\tag{177.K3}
\]

For odd \(m\), let

\[
 c_m(k)=\frac{\widehat E_m(k)}m
       =\frac{2}{m\{1+e(-k/m)\}},
\qquad E_m(a)=(-1)^{[a]_m}.
\tag{177.K4}
\]

Then the following conclusions hold.

1. The anchor reduces exactly to the primitive modulus:

   \[
   E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
   \tag{177.K5}
   \]

   The original aliases fold without a gcd loss:

   \[
   \boxed{
   \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell)
   \qquad(\ell\bmod u_0).}
   \tag{177.K6}
   \]

2. For \(\ell\bmod u_0\), define its reduced additive conductor by

   \[
   q=\frac{u_0}{(\ell,u_0)},
   \tag{177.K7}
   \]

   with \(q=1\) at \(\ell=0\). If \(\ell=(u_0/q)a\) and
   \((a,q)=1\), then

   \[
   c_{u_0}(\ell)=\frac q{u_0}c_q(a),
   \tag{177.K8}
   \]

   and

   \[
   \boxed{
   \sum_{\substack{\ell\bmod u_0\\
                   u_0/(\ell,u_0)=q}}
   |c_{u_0}(\ell)|
   \ll \frac q{u_0}\log(2q).}
   \tag{177.K9}
   \]

3. At fixed \((\kappa,u,u_0)\), the complete literal two-orientation
   \(v,n,t\) capacity is

   \[
   \boxed{O(u_0L).}
   \tag{177.K10}
   \]

   Consequently the coefficient-weighted positive capacity at exact
   reduced conductor \(q\) is

   \[
   \boxed{O\!\left(Lq\log(2q)\right).}
   \tag{177.K11}
   \]

4. For every fixed \(B>0\), put \(Q_B=(\log(2X))^B\). The complete exact
   Fourier subaggregate of (177.K2) with \(q\le Q_B\) satisfies

   \[
   \boxed{
   \left|
   \mathfrak C^{\rm rem}_{\rm low\text{-}\kappa,\,
      {\rm alias\text{-}cond}\le Q_B}
   \right|
   \ll_{B,\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
   \tag{177.K12}
   \]

   In particular, (177.K12) contains the complete physical sector

   \[
   \frac{u}{(u,n)}\le Q_B.
   \tag{177.K13}
   \]

   The exact remaining Fourier complement is

   \[
   \kappa_*<\delta L,\qquad
   q=\frac{u_0}{(\ell,u_0)}>Q_B.
   \tag{177.K14}
   \]

5. On (177.K14), a single reciprocal square-root saving followed by
   positive recombination leaves \(L\sqrt q\) up to logarithms. Exact
   weighted alias \(TT^*\) reconstructs the original physical block
   squared; alias Cauchy and Parseval return residue-bucket energy.
   Positive diagonal or collision closure remains above the local
   \(L\)-target on a power range. This is a route-scoped
   capacity/self-return obstruction, not literal lower mass.

The full high-conductor estimate, complete K17a, the complete residual
scalar, and every downstream owner remain open.

## Exact primitive alias decomposition

Use the Round-176 amplitudes and phases
\(\Lambda^\pm_{\kappa,u,v,n}(t)\) and
\(\Psi^\pm_{\kappa,u,v,n}(t)\). For \(u_0\mid u\), \(g=u/u_0\), and
\((u,n)=g\), define

\[
\begin{aligned}
 \mathcal H_{\kappa,u,u_0,\ell}
 :=\sum_{\substack{v\asymp L/\kappa\\(u,v)=1}}
 \sum_{\substack{n=gn_0\ll L/\kappa\\(n_0,u_0)=1}}
 \sum_{t\in\mathbb Z}\Bigg\{&
 \Lambda^+_{\kappa,u,v,n}(t)
 e\!\left(\Psi^+_{\kappa,u,v,n}(t)+\frac t2+
          \frac{\ell\bar v n_0}{u_0}\right)\\
 &+\Lambda^-_{\kappa,u,v,n}(t)
 e\!\left(\Psi^-_{\kappa,u,v,n}(t)+\frac t2-
          \frac{\ell\bar v n_0}{u_0}\right)
 \Bigg\}.
\end{aligned}
\tag{177.K15}
\]

Every displayed range is shorthand for the exact zero-extended literal
support. Then

\[
\boxed{
 \Re\mathfrak C^{\rm rem}_{\rm low\text{-}\kappa}
 =\Re\sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
       \sum_{u\asymp L/\kappa}\sum_{u_0\mid u}
       \sum_{\ell\bmod u_0}
       c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}.}
\tag{177.K16}
\]

For \(\ell=(u_0/q)a\), the reciprocal phase in (177.K15) is exactly

\[
 e\!\left(\pm\frac{a\bar v n_0}{q}\right).
\tag{177.K17}
\]

Thus \(q\), not \(u\) or \(u_0\), is the final additive conductor.

## Proof of the algebra

Because \(g\) is odd and \(\bar v\) reduces to the inverse of \(v\)
modulo \(u_0\), the canonical residue satisfies

\[
 [\pm\bar v n]_u
 =g[\pm\bar v n_0]_{u_0}.
\tag{177.K18}
\]

Taking parity proves (177.K5). For \(a\bmod u_0\), expand
\(E_u(ga)=E_{u_0}(a)\) at modulus \(u\):

\[
\begin{aligned}
 E_u(ga)
 &=\sum_{k\bmod u}c_u(k)e(ka/u_0)\\
 &=\sum_{\ell\bmod u_0}
   \left\{\sum_{j=0}^{g-1}c_u(\ell+ju_0)\right\}
   e(\ell a/u_0).
\end{aligned}
\tag{177.K19}
\]

Uniqueness of Fourier coefficients modulo \(u_0\) proves (177.K6).
Applying it pointwise to the accepted Round-176 identity proves
(177.K16), with no completion, endpoint error, or gcd multiplicity.

If \(\ell=(u_0/q)a\), direct substitution in (177.K4) proves
(177.K8). Moreover,

\[
 |c_m(k)|=\frac1{m|\cos(\pi k/m)|}.
\tag{177.K20}
\]

The reciprocal-cosine harmonic sum at odd modulus \(q\) gives

\[
 \sum_{\substack{a\bmod q\\(a,q)=1}}|c_q(a)|
 \ll\log(2q),
\tag{177.K21}
\]

and (177.K9) follows. The aliases
\(\ell=(u_0\pm1)/2\) are primitive, have \(q=u_0\), and satisfy
\(|c_{u_0}(\ell)|\asymp1\). They remain in (177.K14) whenever
\(u_0>Q_B\).

## Proof of the capacity and strict sector

Fix \(\kappa,u,u_0\), and put \(U=L/\kappa\). Literal support gives

\[
 u,v\asymp U,\qquad n\ll U,\qquad
 \#\{t:\Lambda^\pm(t)\ne0\}\ll1+\kappa.
\tag{177.K22}
\]

Since \(n=gn_0=(u/u_0)n_0\),

\[
 n_0\ll\frac{Uu_0}{u}\ll u_0.
\tag{177.K23}
\]

There are therefore \(O(u_0)\) determinants, \(O(U)\) values of \(v\),
and \(O(1+\kappa)=O(\kappa)\) fibre sites. Both orientations change only
the constant, and

\[
 u_0U(1+\kappa)\ll u_0L.
\tag{177.K24}
\]

All literal arithmetic and endpoint fields delete or downweight atoms,
so (177.K10) follows without opening any selector or squarefree mask.
Multiplying by (177.K9) proves (177.K11).

For fixed \((\kappa,u)\),

\[
\begin{aligned}
 \sum_{u_0\mid u}
 \sum_{\substack{q\mid u_0\\q\le Q_B}}
 Lq\log(2q)
 &\ll LQ_B\log(2Q_B)\tau(u)^2.
\end{aligned}
\tag{177.K25}
\]

There are \(O(L/\kappa)\) supported \(u\)'s. Hence, after the standard
epsilon rebudgeting,

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{q\le Q_B}\right|
 &\ll
 LQ_B\log(2Q_B)
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
 \sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\eta
 LQ_B\log(2Q_B)X^\eta
 \sum_{\kappa<\delta L}\frac L\kappa\\
 &\ll_\eta
 L^2Q_B\log(2Q_B)\log(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{177.K26}
\]

This proves (177.K12). If \(u_0\le Q_B\), every divisor
\(q\mid u_0\) lies in the safe packet, proving (177.K13).

## Exact energy self-return and the remaining gate

At fixed \((\kappa,u,u_0)\), index the atoms of (177.K15) by \(z\), with
both orientations included, and put

\[
 A_z=\Lambda_z e(\Psi_z+t_z/2),\qquad
 b_z=\begin{cases}
  \bar v n_0\bmod u_0,&z\text{ in the plus orientation},\\
  -\bar v n_0\bmod u_0,&z\text{ in the minus orientation}.
 \end{cases}
\tag{177.K27}
\]

Then

\[
 H_\ell=\sum_zA_ze(\ell b_z/u_0),\qquad
 B_b=\sum_{z:b_z=b}A_z,
\tag{177.K28}
\]

and exact Parseval gives

\[
 \boxed{
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2.}
\tag{177.K29}
\]

Keeping the exact rank-one alias matrix gives only

\[
 \sum_{\ell,\ell'}
 c_{u_0}(\ell)\overline{c_{u_0}(\ell')}
 H_\ell\overline{H_{\ell'}}
 =\left|\sum_bE_{u_0}(b)B_b\right|^2,
\tag{177.K30}
\]

the original physical block squared. Replacing it by alias Cauchy uses
\(\|c_{u_0}\|_2=1\) and yields the right side of (177.K29). Its
coefficient-independent self-diagonal has available square-root capacity

\[
 u_0\sqrt L\,X^\eta,
\tag{177.K31}
\]

which already exceeds \(L\) when \(u_0>\sqrt L\). Positive collision
recombination can return the full \(Lu_0\) capacity. These are upper
capacities of named positive certificates, not literal lower bounds.
More explicitly, the coefficient-independent positive-majorant
self-diagonal and the positive bucket-Cauchy closure satisfy

\[
 D=u_0\sum_z|A_z|^2\ll Lu_0^2X^\eta,
 \qquad \sqrt D\ll u_0\sqrt L\,X^\eta,
\tag{177.K31a}
\]

and, since every residue bucket contains at most \(O(L)\) literal atoms,

\[
 u_0\sum_b|B_b|^2
 \ll u_0L\sum_z|A_z|^2
 \ll L^2u_0^2X^\eta.
\tag{177.K31b}
\]

Neither displayed positive-majorant capacity is a lower bound for the
exact signed energy: cancellation inside a bucket may remove the physical
self-diagonal.

At exact conductor \(q\), (177.K11) shows that a single square-root
reciprocal saving leaves

\[
 L\sqrt q\log(2q)X^\eta.
\tag{177.K32}
\]

This ledger already includes every incomplete lift. Indeed, writing

\[
 h=\frac{u_0}{q},\qquad u=ghq,
\tag{177.K32a}
\]

a fixed ordered residue pair modulo \(q\) has
\(O(gh)\) admissible \(v\)-lifts, \(O(h)\) admissible \(n_0\)-lifts,
and \(O(\kappa)\) fibre sites. Its literal lift multiplicity is therefore

\[
 O(\kappa gh^2)=O(Lh/q),
\tag{177.K32b}
\]

while a fixed inverse-product residue, after summing the \(q\) ordered
residue pairs that yield it, has \(O(Lh)=O(Lu_0/q)\) atoms. Thus a
completion modulo \(q\) may not replace the length-\(u\) ranges by a single
primitive period; the raw capacity (177.K10)--(177.K11) has already paid
for these lifts.

The missing theorem must therefore give a full \(q\)-saving, two coupled
square-root savings, or an equivalent signed average across retained gcd,
alias, modulus, or orientation labels.

The two anchor values are antisymmetric for nonzero residues:

\[
 E_{u_0}(-a)=-E_{u_0}(a)\qquad(u_0>1).
\tag{177.K33}
\]

This does not pair the orientations. The evident interchange
\((u,v,s,w,+)\mapsto(v,u,w,s,-)\) replaces the chosen divisor at each
endpoint by its complementary factor. In the odd--odd branch that
complement lies below the literal upper near-square divisor window; in
the even branch it is even and is not an allowed character-bearing
divisor. Thus no exact cancellation follows from (177.K33).

A sufficient remaining local theorem is

\[
\boxed{
 \left|
 \sum_{u_0\mid u}
 \sum_{\substack{\ell\bmod u_0\\
                 u_0/(\ell,u_0)>Q_B}}
 c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
 \right|
 \ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon}
\tag{177.K34}
\]

uniformly in supported \((\kappa,u)\). A stronger aliaswise sufficient
form is

\[
 \left|\mathcal H_{\kappa,u,u_0,\ell}\right|
 \ll_\varepsilon \frac{u_0}{q}LX^\varepsilon.
\tag{177.K35}
\]

No accepted theorem proves (177.K34) or (177.K35). In particular, the
canonical selected/no-pair field has no proved variation, Fourier norm,
factorization, or residue-bucket cancellation in the required labels.

## Scope

The proved result is exactly the target-safe low-reduced-alias-conductor
packet (177.K12), its physical corollary (177.K13), the exact complement
(177.K14), and the named positive-capacity/self-return limitations
(177.K29)--(177.K33). The latter do not disprove the literal high-conductor
estimate.

Complete K17a, the residual scalar, full displayed \(t=1\), every other
hard-TOP channel, complete hard TOP, both BAL scopes, UNBAL, M9--M2, both
direct M1 parents or GAR, endpoint uniformity, M9, both bridges, the
quarter theorem remain open. This kernel changes no exponent owner or
numerical exponent value: the inherited internal \(1/3\), external
\(0.3144831759740614\ldots\), and target \(1/4\) ledger is unchanged.

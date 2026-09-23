# Round 179 strategy: primitive-conductor orientation-defect gate

## Authoritative starting point

Round 179 starts from graph
e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27.
Round 178 selected exactly the aggregate high-reduced-conductor K17a
estimate (177.K34). The stronger aliaswise estimate (177.K35), K26, every
other hard-TOP channel, BAL, UNBAL, M1, GAR, endpoint assembly, bridges, and
exponent work are outside this round.

The accepted Round-177 reduction gives, for odd \(u_0\),

\[
q=\frac{u_0}{(\ell,u_0)},\qquad
\ell=\frac{u_0}{q}a,\quad (a,q)=1,\qquad
c_{u_0}(\ell)=\frac q{u_0}c_q(a),
\tag{179.S1}
\]

where

\[
c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{179.S2}
\]

At fixed \((\kappa,u,u_0)\), literal atom capacity is \(O(u_0L)\), and
the exact-\(q\) positive coefficient capacity is
\(O(Lq\log(2q))\). Every \(q\le Q_B=(\log(2X))^B\) packet is already
proved. The frozen objective is

\[
\boxed{
\left|
\sum_{u_0\mid u}
\sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)>Q_B}}
c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
\right|
\ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon}
\tag{177.K34}
\]

uniformly for every supported \((\kappa,u)\), with one outer absolute
value after all aliases and both literal orientations are recombined.

## Candidate primitive-conductor parity kernel

For odd \(q\), define

\[
K_q(b)=\sum_{\substack{a\bmod q\\(a,q)=1}}
c_q(a)e(ab/q).
\tag{179.S3}
\]

The candidate exact-conductor projector identity is

\[
K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
\qquad E_d(b)=(-1)^{[b]_d},\quad E_1=1.
\tag{179.S4}
\]

For \(b\in(\mathbb Z/q\mathbb Z)^\times\), every divisor \(d>1\) of
\(q\) is odd and \(E_d(-b)=-E_d(b)\). Hence the candidate parity law is

\[
\boxed{K_q(b)+K_q(-b)=\frac{2\mu(q)}q.}
\tag{179.S5}
\]

This identity must be independently rederived. In particular, the
\(d=1\) term must not be discarded, and the factor \(q/u_0\) from
(179.S1) must be retained.

For fixed \((\kappa,u,u_0,q)\), remove the conductor phase from the two
literal orientations and bucket all remaining amplitudes by
\(b=\bar v n_0\bmod q\):

\[
B^\pm_{q,b}
=\sum_{\substack{z\text{ in the }\pm\text{ orientation}\\
\bar v n_0\equiv b\pmod q}}
\Lambda_z^\pm e(\Psi_z^\pm+t_z/2).
\tag{179.S6}
\]

The accepted primitive fold gives \((n_0,u_0)=1\), and the literal row has
\((v,u)=1\), so every occupied \(b\) is a unit modulo \(q\). If (179.S4)
and all bucket multiplicities are correct, the exact-\(q\) block becomes

\[
\begin{aligned}
\mathcal C_{u_0,q}
&=\frac q{u_0}\sum_{b\in U(q)}
\{K_q(b)B^+_{q,b}+K_q(-b)B^-_{q,b}\}\\
&=\frac q{u_0}\sum_{b\in U(q)}
K_q(b)\{B^+_{q,b}-B^-_{q,b}\}
+\frac{2\mu(q)}{u_0}\sum_{b\in U(q)}B^-_{q,b}.
\end{aligned}
\tag{179.S7}
\]

The second line separates an orientation defect from a primitive trace.
The trace is a candidate target-safe component: the literal fixed-
\((\kappa,u,u_0,q)\) atom count is \(O(u_0L)\), so its absolute capacity
after \(2\mu(q)/u_0\) is \(O(L)\). Summing \(q\mid u_0\) and
\(u_0\mid u\) costs only divisor factors. This must be checked without
double-counting the already proved low-\(q\) packet.

The remaining exact object is

\[
\mathcal D_{\kappa,u}
=\sum_{u_0\mid u}
\sum_{\substack{q\mid u_0\\q>Q_B}}
\frac q{u_0}\sum_{b\in U(q)}
K_q(b)\{B^+_{q,b}-B^-_{q,b}\}.
\tag{179.S8}
\]

Round 179 must determine whether the literal orientation defect in
(179.S8) has a target bound, contains a strict owner-complete sector on
which it vanishes or contracts, or returns the full exact-conductor
capacity after all selectors, lifts, endpoints, and phases are restored.

## Mechanism boundary

The candidate decomposition bypasses the parked full-anchor
antisymmetry argument only by first projecting to an exact primitive
conductor. It does not assume that complementary divisors preserve the
literal selector domain. A proof must exhibit an actual relation between
\(B^+_{q,b}\) and \(B^-_{q,b}\); the notation “orientation defect” supplies
no estimate.

The following do not prove (177.K34):

- replacing \(B^\pm\) by arbitrary bounded arrays and asserting
  cancellation from (179.S5);
- taking absolute values of the defect and paying
  \(Lq\log(2q)\);
- one reciprocal square-root saving, which leaves
  \(L\sqrt q\log(2q)\);
- rank-one \(TT^*\), positive alias Parseval, or bucket Cauchy;
- completion that suppresses physical \(v,n_0,t\) lift multiplicity;
- complementary-divisor orientation exchange outside the selector
  support; or
- proving the stronger aliaswise (177.K35) after the aggregate objective
  fails.

An adversarial bucket array is a false control, not literal lower mass.
Conversely, a literal equality or contraction for a complete selector-
stable sector must include every endpoint, parity, squarefree, no-pair,
and zero-extension field before it can be promoted.

## Exit gates

Close under exactly one label:

1. hard_top_t1_residual_k17a_high_conductor_target if the complete
   aggregate (177.K34) is proved;
2. strict_k17a_symmetric_orientation_conductor_sector if a complete
   nontrivial literal sector of (179.S8) is proved target-safe with its
   exact complement stated; or
3. primitive_conductor_orientation_defect_capacity_or_self_return_no_go
   if (179.S4)--(179.S7) are proved but the first exact selector,
   multiplicity, or capacity obstruction to controlling (179.S8) is
   established.

Even the first label can close only the K17a sufficient residual route
after a separately reviewed connector. No Round-179 result by itself
proves full \(t=1\), complete hard TOP, M9--M2, M9, a bridge, the quarter
theorem, or an exponent improvement.

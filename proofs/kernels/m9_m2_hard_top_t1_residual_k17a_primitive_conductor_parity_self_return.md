# Kernel: K17a primitive-conductor parity, trace, and self-return

## Lemma

Retain the complete literal two-orientation K17a packet and notation of the
accepted cross-gcd and primitive-alias reductions.  Thus

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad (n_0,u_0)=1,
\tag{179.K1}
\]

all of \(u,u_0\) are odd, \((u,v)=1\), and every selector, squarefree and
coprimality field, parity branch, Fejer factor, displacement condition,
profile, floor, star, hard value, endpoint conjugation, phase, and zero
extension remains inside the literal amplitudes.  For \(q\mid u_0\), put

\[
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}},\qquad
 K_q(b)=\sum_{a\in U(q)}c_q(a)e(ab/q).
\tag{179.K2}
\]

For a literal atom \(z\) in either orientation, remove only its
exact-conductor phase and write

\[
 A_z^\pm=\Lambda_z^\pm e(\Psi_z^\pm+t_z/2),\qquad
 \beta_z=\bar v n_0\pmod {u_0}\in U(u_0).
\tag{179.K3}
\]

Define the exact coarsened buckets

\[
 B_{q,b}^\pm
 =\sum_{\substack{z\text{ in the }\pm\text{ orientation}\\
                   \beta_z\equiv b\pmod q}}A_z^\pm,
 \qquad b\in U(q).
\tag{179.K4}
\]

Then the following statements hold.

1. The primitive-frequency projector has the exact divisor formula

   \[
   \boxed{
   K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
   \qquad E_d(b)=(-1)^{[b]_d},\quad E_1=1.}
   \tag{179.K5}
   \]

   If \(b\in U(q)\), then

   \[
   \boxed{K_q(b)+K_q(-b)=\frac{2\mu(q)}q.}
   \tag{179.K6}
   \]

   The entire right side of (179.K6) is the \(d=1\) term in
   (179.K5).

2. Put

   \[
   K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
   \tag{179.K7}
   \]

   On \(U(q)\), \(K_q^\circ(-b)=-K_q^\circ(b)\).  The exact-
   conductor block is

   \[
   \boxed{
   \begin{aligned}
   \mathcal C_{u_0,q}
   ={}&\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
          \bigl(B_{q,b}^+-B_{q,b}^-\bigr)\\
      &+\frac{\mu(q)}{u_0}\sum_{b\in U(q)}
          \bigl(B_{q,b}^++B_{q,b}^-\bigr).
   \end{aligned}}
   \tag{179.K8}
   \]

   The second line is an exact symmetric primitive trace.  Uniformly for
   supported \((\kappa,u)\), its complete high-conductor contribution
   satisfies

   \[
   \boxed{
   \sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
   \left|\frac{\mu(q)}{u_0}\sum_b
     \bigl(B_{q,b}^++B_{q,b}^-\bigr)\right|
   \ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.}
   \tag{179.K9}
   \]

3. For every odd \(u_0>1\) and \(b\in U(u_0)\), reduced modulo each
   \(q\mid u_0\), one has the all-conductor identity

   \[
   \boxed{
   \sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)=E_{u_0}(b).}
   \tag{179.K10}
   \]

   Also \(K_1(0)=1\) and \(K_1^\circ(0)=0\).  Hence (179.K10) is not
   asserted at \(u_0=1\); that stratum has only \(q=1\le Q_B\) and no
   high-conductor contribution.

   Define the original fixed-\(u_0\) literal orientation block by

   \[
   \mathcal O_{u_0}
   =\sum_{z\in+}E_{u_0}(\beta_z)A_z^+
    +\sum_{z\in-}E_{u_0}(-\beta_z)A_z^-.
   \tag{179.K11}
   \]

   If \(\mathcal D^\circ_{\le Q_B}\) and
   \(\mathcal D^\circ_{>Q_B}\) denote the centered defect in (179.K8)
   over the indicated conductor ranges, then

   \[
   \boxed{
   \mathcal D^\circ_{>Q_B}
   =\mathcal O_{u_0}-\mathcal D^\circ_{\le Q_B}.}
   \tag{179.K12}
   \]

   The all-conductor centered trace is zero, with the \(q=1\) term
   essential.  Consequently, for the uncentered exact blocks,

   \[
   \boxed{
   \mathcal C_{>Q_B}=\mathcal O_{u_0}-\mathcal C_{\le Q_B}.}
   \tag{179.K13}
   \]

   Thus primitive-conductor centering exactly reconstructs the original
   literal orientation block after the already-safe low-conductor packet
   is removed.  This is an algebraic self-return, not an estimate or a
   literal lower bound.

4. The centered defect retains full coefficient-uniform conductor
   capacity.  At fixed exact conductor \(q\),

   \[
   \left|\frac q{u_0}\sum_bK_q^\circ(b)
   \bigl(B_{q,b}^+-B_{q,b}^-\bigr)\right|
   \ll_\varepsilon LqX^\varepsilon.
   \tag{179.K14}
   \]

   For every odd prime \(p\),

   \[
   K_p(b)=E_p(b)-\frac1p,\qquad K_p^\circ(b)=E_p(b),
   \qquad b\in U(p),
   \tag{179.K15}
   \]

   while

   \[
   K_{p^2}^\circ(b)=E_{p^2}(b)-\frac1pE_p(b).
   \tag{179.K16}
   \]

   Prime and prime-square artificial bucket arrays respecting the unit
   support and literal bucket-count shadow attain \(\asymp Lq\).  They
   refute a coefficient-uniform contraction derived only from the parity
   kernel and bucket sizes, but they are not realizations of the literal
   selector and phase field and therefore give no lower bound for K17a.

5. Neither evident orientation map closes the defect.  The fixed-
   modulus reflection

   \[
   (s,w)\longmapsto(u-s,v-w)
   \tag{179.K17}
   \]

   maps the plus Diophantine lattice to the minus lattice but is live only
   when \(1\le s\le u-1\) and \(1\le w\le v-1\), at most one site of a
   primitive fibre.  Even on that overlap it reflects the endpoint pair
   rather than preserving it, so no phase, selector, squarefree, profile,
   or endpoint conjugacy follows.  The product-preserving exchange

   \[
   (u,v,s,w,+)\longmapsto(v,u,w,s,-)
   \tag{179.K18}
   \]

   changes the fixed outer row, primitive modulus, conductor, and bucket.
   It also replaces both selected divisors by complementary factors,
   which lie outside the literal upper near-square selector in the odd
   branch and are even in the even branch.  It maps a live selected atom
   to the zero extension, not to a live opposite-orientation atom.

The first unproved estimate remains the complete centered defect bound

\[
\boxed{
\left|
\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
\bigl(B_{q,b}^+-B_{q,b}^-\bigr)
\right|
\stackrel{?}{\ll}_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.}
\tag{179.K19}
\]

By (179.K12), it is the original unresolved literal orientation block
minus an already-safe low-conductor term.  Equations (179.K5)--(179.K18)
therefore do not prove the high-conductor estimate (177.K34).

## Proof

For \(r\mid q\), write \(d=q/r\).  Directly from (179.K2),

\[
c_q(rk)=\frac1r c_d(k).
\tag{179.K20}
\]

Insert

\[
\mathbf 1_{(a,q)=1}=\sum_{r\mid(a,q)}\mu(r)
\tag{179.K21}
\]

into the definition of \(K_q\).  Grouping the frequencies divisible by
\(r\), applying (179.K20), and using Fourier inversion for \(E_d\)
gives

\[
\begin{aligned}
K_q(b)
&=\sum_{r\mid q}\mu(r)
  \sum_{\substack{a\bmod q\\r\mid a}}c_q(a)e(ab/q)\\
&=\sum_{r\mid q}\frac{\mu(r)}r E_{q/r}(b)
 =\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
\end{aligned}
\tag{179.K22}
\]

which proves (179.K5), including \(q=1\).  If \(b\in U(q)\) and
\(d>1\), then \([b]_d\in\{1,\ldots,d-1\}\) and
\([-b]_d=d-[b]_d\).  Since \(d\) is odd,
\(E_d(-b)=-E_d(b)\).  The \(d=1\) values are both one, proving
(179.K6).  Equations (179.K7)--(179.K8) follow by taking the symmetric
and antisymmetric parts of the two kernel coefficients, retaining the
accepted factor \(q/u_0\).

The literal mass of either orientation at fixed
\((\kappa,u,u_0)\) is \(O_\varepsilon(u_0LX^\varepsilon)\).  Hence the
absolute trace at fixed \((u_0,q)\) is \(O_\varepsilon(LX^\varepsilon)\).
Moreover,

\[
\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
\le \tau(u)2^{\omega(u)}\ll_\varepsilon X^\varepsilon,
\tag{179.K23}
\]

which proves (179.K9) without adding any \(q\le Q_B\) alias.

Removing the \(d=1\) term from (179.K5) gives

\[
K_q^\circ(b)=\frac1q
\sum_{\substack{d\mid q\\d>1}}\mu(q/d)dE_d(b).
\tag{179.K24}
\]

For \(u_0>1\), interchange the divisor sums:

\[
\begin{aligned}
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)
&=\frac1{u_0}\sum_{\substack{d\mid u_0\\d>1}}
  dE_d(b)\sum_{r\mid u_0/d}\mu(r)\\
&=E_{u_0}(b).
\end{aligned}
\tag{179.K25}
\]

The bucket in (179.K4) is exactly the reduction of the same primitive
residue \(\beta_z\) modulo \(q\).  Applying (179.K25) atom by atom and
using \(E_{u_0}(-\beta_z)=-E_{u_0}(\beta_z)\) proves (179.K12).  The
unphased bucket total is independent of \(q\), and
\(\sum_{q\mid u_0}\mu(q)=0\), proving trace cancellation and
(179.K13).

Finally,

\[
|K_q^\circ(b)|
\le\frac1q\sum_{\substack{d\mid q\\d>1}}
d|\mu(q/d)|
\le\prod_{p\mid q}\left(1+\frac1p\right)
\ll_\varepsilon q^\varepsilon.
\tag{179.K26}
\]

Combining (179.K26) with the \(O(u_0L)\) literal atom capacity proves
(179.K14).  Equations (179.K15)--(179.K16) follow directly from
(179.K24).  Filling the \(\varphi(q)\asymp q\) unit buckets in the
prime and prime-square controls with phases aligned to \(K_q^\circ\),
at the literal count shadow \(O(Lu_0/q)\) per bucket, gives the stated
artificial \(Lq\) capacity.  The two orientation-map
claims follow by direct substitution in the Diophantine equations and
endpoint products, together with the accepted literal selector support.

## Scope

The proved advance is the exact primitive projector, the target-safe
symmetric trace, and the all-conductor self-return obstruction.  The
closing label is
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`.

The result does not reject the literal estimate (177.K34).  Complete
K17a, the complete residual scalar, all other hard-TOP channels, hard
TOP, BAL, UNBAL, M9--M2, both direct M1 parents or GAR, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent
owner remain at their inherited status.  In particular, the internal
\(1/3\), audited external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent ledger is
unchanged.

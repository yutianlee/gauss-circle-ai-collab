# Round 38 blind report: the actual fixed-(w) beta-slab density has a uniform signed Cauchy tail

Task: blind_beta_slab_height_asymptotic  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation or external theorem

## 1. Result

Choose the lawful terminal line
\[
 c'=\frac54,\qquad b=\frac1{\log(2X)}<\frac14,\qquad
 0<a\le a_b:=\min\{b,\tfrac14-b\}.             \tag{38.1}
\]
Put \(u=a+i\mu\), \(v=b+i\nu\), \(s=c'+it\), and
\(z=u+v\).  On the compact beta share use
\[
 \beta=t-\frac{\mu+\nu}{2},\qquad
 \alpha=t+\frac{\mu+\nu}{2}.                    \tag{38.2}
\]
Then
\[
 t=\frac{\alpha+\beta}{2},\qquad
 \mu=\alpha-\beta-\nu,\qquad
 \left|\frac{\partial(t,\mu,\nu)}
 {\partial(\beta,\alpha,\nu)}\right|=1.          \tag{38.3}
\]
Thus beta localization leaves two unbounded tangent variables; it creates
no Jacobian loss.

Let \(\zeta_0=a+b\).  The exact terminal gamma quotient has the same
power at both tangent ends,
\[
 |K_{u+v}(1-s)|\ll_{b,B_0}(1+|\alpha|)^\kappa,\qquad
 \kappa=c'+\frac{\zeta_0}{2}-\frac12
 =\frac34+\frac{a+b}{2}\le\frac78<1,               \tag{38.4}
\]
while
\[
 \rho=\frac14-s-\frac v2
 =-1-\frac b2-\frac{i}{2}(\alpha+\beta+\nu)       \tag{38.5}
\]
and the full radial numerator is uniformly \(O_X(1)\).  Consequently the
terminal \(R_1\) factor is
\[
 |R_{1,v}(1-s)|\ll_X
 (1+|\alpha+\beta+\nu|)^{-1}.                       \tag{38.6}
\]

The inequality \(\kappa<1\) is decisive.  After the hard-top factor is
taken as the single signed distribution
\[
 \mathcal P(\mu)=\frac12\delta_0(\mu)
 -\frac{i}{2\pi}\operatorname {PV}\frac1\mu,       \tag{38.7}
\]
the terminal tail density is
\[
 O_{X,b}\!\left((1+|\nu|)^{\kappa-2}
 \log(2+|\nu|)\right).                              \tag{38.8}
\]
The separate artificial-residue germ is
\(O_{X,b}((1+|\nu|)^{-3})\).  Both are integrable.  Uniformly in the
finite top height \(U\), radial height \(S\) satisfying the compact-support
separation, and \(V_2\ge V_1\ge2\), the complete normalized positive-\(b\)
tail therefore obeys
\[
 \boxed{
 |\mathfrak T^{\rm ef}_{V_1,V_2;U,S}|
 \le C_{X,b}\,V_1^{\kappa-1}\log(2V_1),}           \tag{38.9}
\]
after harmless enlargement of \(C_{X,b}\).  Since \(\kappa<1\), this
tends to zero uniformly along \(U=V=T\) and
\(S=(2+X+2T+2B_0)^2\).  Hence the Round-37 endpoint-free vector possesses
the prescribed symmetric outside-height limit.  This is an existence
theorem only; it gives no local \(\lambda^{-2}\)/\(\lambda^{-3}\) symbol
estimate and no target-size bound.

## 2. Exact statement and hypotheses

On the fixed terminal line the complete dual density before the top limit is
\[
\begin{aligned}
 \mathcal Q_{j,h,q}(\alpha,\beta,\nu)={}&
 \mathbf1_{hq=m}\chi_4(q)
 \widehat W_j(a+i(\alpha-\beta-\nu))
 \widehat\phi(b+i\nu)
 \left(\frac{D_j}{2\sqrt X}\right)^{a+i\mu}
 (H_j+1)^{b+i\nu}\\
 &\times
 \left(\frac hq\right)^{(a+b+i(\alpha-\beta))/2}
 R_{1,b+i\nu}(1-s)K_{u+v}(1-s)(hq)^{-s}.       \tag{38.10}
\end{aligned}
\]
The variables \(s,u,v\) in (38.10) are recovered by (38.3), and
\(|\beta|\le2B_0\).  The real arithmetic exponents are exactly
\[
 h^{-5/4+(a+b)/2}\qquad\hbox{and}\qquad
 q^{-5/4-(a+b)/2}.                                  \tag{38.11}
\]
Under (38.1), the first is at most \(h^{-9/8}\) and the second at most
\(q^{-5/4}\).  Therefore both series, and the same series with any fixed
power of \(\log h+\log q\), converge absolutely.  This licenses all
coefficient derivatives used below without exploiting character
cancellation.

Write
\[
 f_b(\nu)=\widehat\phi(b+i\nu).                   \tag{38.12}
\]
The actual height profile satisfies, for the orders used here,
\[
 |f_b^{(r)}(\nu)|\le C_{b,r}(1+|\nu|)^{-3-r},\qquad
 C_{b,r}\ll b^{-A_r}.                               \tag{38.13}
\]
Interior \(\widehat W_j\)'s and the regular part of the top transform are
rapidly decreasing in \(\mu\), uniformly for \(0<a\le a_b\).  The hard
top is
\[
 \widehat W_0(a+i\mu)=\frac1{a+i\mu}
 +\widehat W_{0,r}(a+i\mu),                         \tag{38.14}
\]
and the contour measure converts its polar part precisely to (38.7).  The
delta and PV pieces are never estimated separately before their common test
function is formed.

The artificial term must be kept in its original germ, not expanded in the
dual \(h,q\) series.  If \(p(v)=3/4+v/2\), its coefficient is, up to the
fixed oriented residue constant,
\[
 F_{u+v}(p(v))
 =\zeta\!\left(\frac34+\frac u2+v\right)
  L\!\left(\frac34-\frac u2,\chi_4\right),      \tag{38.15}
\]
with mask coordinate
\[
 \beta_\rho=-\frac\mu2-\nu.                         \tag{38.16}
\]
At a collision (38.15) is the one common artificial coefficient; no
separate \(E_1\), \(R_1\), or axial residue is added.  The \(v=0\) residue
and the one joint corner are supported at \(\nu=0\) and do not enter a
tail with \(V_1>0\).

All actual scale factors, \(H_j+1\) floors, hard endpoint convention,
\(\chi_4\), and stars licensed only after symmetric inversion are retained.
The external functional
\[
 -\frac4\pi X^{1/4}\operatorname {Re}\{e(1/8)\,\cdot\}             \tag{38.17}
\]
is applied once to the assembled vector.

## 3. Proof or derivation

### Beta-slab Jacobian and gamma powers

The inverse relations (38.3) give
\[
 \frac{\partial(t,\mu,\nu)}
      {\partial(\beta,\alpha,\nu)}
 =\begin{pmatrix}
  1/2&1/2&0\\ -1&1&-1\\0&0&1
 \end{pmatrix},\qquad \det=1.                 \tag{38.18}
\]
Moreover
\[
 \Im(s-z/2)=\beta,\qquad \Im(s+z/2)=\alpha.   \tag{38.19}
\]
Split the exact quotient as
\[
 K_z(1-s)=X_\zeta(s,z)X_4(s,z),                    \tag{38.20}
\]
\[
 X_\zeta=\pi^{1/2-s+z/2}
 \frac{\Gamma((s-z/2)/2)}
      {\Gamma((1-s+z/2)/2)},\qquad
 X_4=\left(\frac4\pi\right)^{s+z/2-1/2}
 \frac{\Gamma((1+s+z/2)/2)}
      {\Gamma((2-s-z/2)/2)}.                       \tag{38.21}
\]
The first ratio is uniformly smooth and bounded for
\(|\beta|\le2B_0\) and (38.1).  Two-sided Stirling gives, as
\(\alpha\to\pm\infty\),
\[
 X_4(s,z)=C_{c',a,b}
 \left(\frac{|\alpha|}{2}\right)^\kappa
 \exp\!\left(i\operatorname {sgn}(\alpha)
 \left\{|\alpha|\!\left(\log\frac{2|\alpha|}{\pi}-1\right)
       +\frac\pi4\right\}\right)
 \{1+O_{a,b}(|\alpha|^{-1})\}.                     \tag{38.22}
\]
In particular, both signs have power \(\kappa\), and
\[
 |\partial_\alpha K_z(1-s)|
 \ll_{b,B_0}(1+|\alpha|)^\kappa
 \log(2+|\alpha|).                             \tag{38.23}
\]

For the radial factor, (38.5) and compactness of \([1,N_X]\) give
\[
 \left|\partial_\rho^r
 \int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx\right|
 \le \int_1^{N_X}x^{-3/2-b/2}(\log x)^r\,dx
 \ll_{X,r}1.                                       \tag{38.24}
\]
Since \(|\Re\rho|=1+b/2\), (38.24) proves (38.6), including one
\(\mu\)-derivative.  Thus “the radial integral is \(O_X(1)/\rho\)” is
lawful on the terminal line.  It is not a global statement through the
artificial residue \(\rho=0\); that residue is represented separately by
(38.15).

The resulting two-sided power ledger is
\[
\begin{array}{c|c|c|c|c|c}
\text{region}&|K|&|R_1|&\text{top factor}&|f_b(\nu)|
 &\text{complete height capacity}\\ \hline
\alpha\to+\infty&|\alpha|^\kappa&(1+|\alpha+\nu|)^{-1}
 &\mathcal P(\alpha-\beta-\nu)&(1+|\nu|)^{-3}&\text{signed below}\\
\alpha\to-\infty&|\alpha|^\kappa&(1+|\alpha+\nu|)^{-1}
 &\mathcal P(\alpha-\beta-\nu)&(1+|\nu|)^{-3}&\text{same power}\\
\alpha=O(1)&1&(1+|\nu|)^{-1}&O((1+|\nu|)^{-1})
 &(1+|\nu|)^{-3}&(1+|\nu|)^{-5}\\
\mu=0&|\nu|^\kappa&|\nu|^{-1}&\frac12\delta_0
 &|\nu|^{-3}&|\nu|^{\kappa-4}\\
\alpha=-\nu+O(1)&|\nu|^\kappa&O_X(1)&O(|\nu|^{-1})
 &|\nu|^{-3}&|\nu|^{\kappa-4}\\
|\alpha|\gg|\nu|&|\alpha|^\kappa&|\alpha|^{-1}
 &|\alpha|^{-1}&|\nu|^{-3}&|\nu|^{-3}|\alpha|^{\kappa-2}\\
\mathfrak P_\rho[R_1]&|\nu|^{a/2-1/4}\ \text{formally}
 &\text{one residue}&|\nu|^{-1}&|\nu|^{-3}
 &O_{X,b}(|\nu|^{-3}).
\end{array}                                                       \tag{38.25}
\]
The formal gamma exponent in the last row is obtained at
\(s=1/4-v/2\).  Its companion dual series is not absolutely convergent,
so that row is rigorously estimated from the equivalent original germ
(38.15), as shown below.

### Signed hard-top estimate, uniform in \(U\)

After summing (38.11), the scale set, and the bounded beta interval, let
\(G_{\nu,\beta}(\mu)\) denote the terminal coefficient with \(f_b(\nu)\)
and the polar top factor removed.  Put \(R=2+|\nu|\).  Equations
(38.6), (38.22)--(38.24), and convergence of all logarithmic moments in
(38.11) imply
\[
 \sup_{|\mu|\le4R}|\partial_\mu G_{\nu,\beta}(\mu)|
 \ll_{X,b}R^\kappa\log R,\qquad
 |G_{\nu,\beta}(\pm\mu)|\ll_{X,b}\mu^{\kappa-1}
 \quad(\mu>4R).                                     \tag{38.26}
\]
The second estimate uses both the top distance and the \(R_1\) denominator;
it is valid for either tangent sign.

For the PV component, symmetry of the finite top interval gives exactly
\[
 \operatorname {PV}\!\int_{-U}^{U}\frac{G(\mu)}\mu\,d\mu
 =\int_0^U\frac{G(\mu)-G(-\mu)}\mu\,d\mu.          \tag{38.27}
\]
The part \(0<\mu\le4R\) is at most
\(O_{X,b}(R^{\kappa+1}\log R)\) by the difference quotient in
(38.26).  The remaining part is bounded uniformly in \(U\) by
\[
 \int_{4R}^{\infty}\mu^{\kappa-2}\,d\mu
 \ll R^{\kappa-1},                                 \tag{38.28}
\]
which is finite precisely because \(\kappa<1\).  Multiplying by
(38.13) proves (38.8).  The delta surface is
\(\mu=0\), equivalently \(\alpha=\nu+\beta\), and (38.6) gives the
better power \(R^{\kappa-4}\).  Rapid decay of every regular
\(\widehat W_j\) term gives at worst \(R^{\kappa-3}\).  Hence all
terminal pieces are integrable uniformly in \(U\).

This step is genuinely signed.  Replacing (38.27) by
\(\int|G(\mu)|/|\mu|\,d\mu\) is divergent and would destroy the theorem.

### Artificial germ and character placement

On (38.16), set \(\mu=-2(\nu+\beta_\rho)\); the real Jacobian is
\(|d\mu|=2|d\beta_\rho|\).  The two factors in (38.15) become
\[
 \zeta\!\left(\frac34+\frac a2+b-i\beta_\rho\right),\qquad
 L\!\left(\frac34-\frac a2+i(\nu+\beta_\rho),\chi_4\right).
 \tag{38.29}
\]
The zeta argument stays in a compact set a positive \(b\)-dependent
distance from its pole.  Since
\(\sup_Y|\sum_{n\le Y}\chi_4(n)|\le1\), elementary Abel summation gives,
for every \(r>0\),
\[
 |L(r+i\tau,\chi_4)|
 \le 1+\frac{|r+i\tau|}{r}
 \ll_r1+|\tau|.                                    \tag{38.30}
\]
For \(|\nu|>4B_0\), the delta part of (38.7) is disjoint from
\(\operatorname {supp}\psi(\beta_\rho)\), whereas its PV factor is
\(O(|\nu|^{-1})\).  Equations (38.13), (38.29), and (38.30) therefore
give \(O_{X,b}(|\nu|^{-3})\), uniformly in the finite box.  Smooth top
and interior profiles are better.

This also explains the arithmetic-exponent warning.  A formal dual
expansion at the artificial pole would have real powers
\[
 h^{-1/4+a/2+b}\qquad\hbox{and}\qquad
 q^{-1/4-a/2},                                      \tag{38.31}
\]
which are not absolutely summable.  The lawful coefficient is the common
germ (38.15); its high factor is the character \(L\), for which (38.30)
applies.  Moving the character to the bounded factor or taking unsigned
coefficients would invalidate this argument.

Integrating (38.8) and the better rows of (38.25) over
\(V_1<|\nu|\le V_2\) proves (38.9).  Compact beta support makes the radial
sides identically zero for the prescribed \(S\).  Exact finite Stokes has
already reconciled the \(v\)-faces, connector axes, and corner with this
positive-\(b\) density; the \(v=0\) and corner distributions have no
large-\(|\nu|\) support.  Thus no omitted axial share remains.

## 4. First doubtful or unproved step

There is no missing uniform coefficient for the outside-height existence
statement once (38.1) is chosen.  The potentially dangerous coefficient is
the hard-top PV part: pointwise it contains the polynomial gamma growth
\(|\alpha|^\kappa\), and absolute values at \(\mu=0\) fail.  The signed
difference quotient (38.27), the terminal \(R_1\) denominator, and
\(\kappa<1\) give the uniform integrable majorant (38.8).

The next genuinely unproved step is outside this round: a local,
transition-uniform estimate of the limiting endpoint-free symbol, including
saddle entry/exit and the desired \(\lambda^{-2}\)/\(\lambda^{-3}\)
weights.  The coarse bound (38.26) intentionally discards oscillation and
cannot provide that estimate or a target-size theorem.

## 5. Required controls and outcomes

### Beta-slab coordinate and Jacobian

**Pass.**  Equations (38.2)--(38.3) and (38.18) give determinant \(+1\)
in the ordered variables \((t,\mu,\nu)\) and preserve every real part.

### Exact gamma/R1 tangent power table

**Pass.**  Equations (38.22)--(38.25) give both tangent signs, bounded
alpha, the top surface, the \(R_1\)-height seam, the far tangent region,
and the artificial residue.  The allowed \(c'=5/4\) makes
\(\kappa\le7/8<1\).  The radial numerator is uniformly \(O_X(1)\); its
\(1/\rho\) statement is used only where \(\Re\rho=-1-b/2\).

### Signed top delta/PV before absolute values

**Pass.**  Formula (38.7) is applied to the complete test function.
The delta lies on \(\alpha=\nu+\beta\); the PV is the symmetric difference
quotient (38.27).  No \(|1/\mu|\) majorant is used.

### Positive/negative height and rho seams

**Pass.**  The two tangent signs have identical power.  The terminal
\(\alpha=-\nu+O(1)\) seam is harmless because \(\Re\rho\ne0\); the actual
\(\rho=0\) coefficient is handled once by (38.15), and its top delta has
bounded \(\nu\)-support.

### Complete actual profile, character, and coefficient sum

**Pass.**  The terminal \(h,q\) exponents (38.11) are absolutely summable
with logarithmic derivatives.  At the artificial pole those exponents are
not summable, so the proof correctly retains the original germ and uses
the period-four character estimate (38.30).  Constants from
\(f_b\) are at most a fixed power of \(b^{-1}=\log(2X)\); floors, scales,
and the hard top remain actual.

### Uniform tail under joint exhaustion

**Pass.**  Bound (38.9) is independent of \(U,V_2,S\) once the beta slab
is contained and the radial sides are support-separated.  It therefore
applies to the prescribed \(U=V=T\), quadratic \(S(T)\), physical-top net.

### Collision, corner, and normalization scope

**Pass.**  The common artificial germ is counted once; \(v=0\) and the
corner do not meet a positive tail.  The external factor (38.17) is restored
once and only changes the fixed-\(X\) constant.

### No local-symbol or target-bound overreach

**Pass.**  The proof establishes Cauchy existence only.  It asserts no
local symbol decay and no Gauss-circle estimate.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-vector-hankel-kernel/reports/blind_finite_vector_kernel.md`;
4. `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/reports/blind_partial_FE_factorization.md`;
5. `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md`;
6. `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md`.

No proof graph, proof draft, excluded report, Round-38 report, computation,
or web source was read or used.

## 7. Recommended state effect

- **Promote** the exact beta-slab change and unit Jacobian
  (38.2)--(38.3), the two-sided tangent table (38.25), and the exact
  terminal/artificial arithmetic exponent ledger (38.11), (38.31).
- **Promote** the uniform signed Cauchy-tail theorem (38.9), including the
  required order: common fixed-\(w\) germ, complete top distribution,
  coefficient sum, then absolute tail integration.
- **Close**, subject to conductor seam review, the existence and uniqueness
  part of the endpoint-free beta axial-vector limit under the prescribed
  joint exhaustion.
- **Retain open** every local terminal-symbol estimate, beta transition
  size bound, M9-M1, M9, and the Gauss-circle target.

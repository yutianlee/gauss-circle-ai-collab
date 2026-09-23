# Round 164 discovery report: complete residual signed-divisor transport

## 1. Result

The complete literal residual admits an exact ordered-divisor Abel identity,
an exact regulated Stieltjes identity with all hard and point-value jumps, and
an exact unequal-mass monotone-transport normalization.  These identities do
not prove the target.  The terminal label of this report is

\[
 \boxed{\texttt{hard\_top\_t1\_residual\_transport\_no\_go}.}
\tag{164.D1}
\]

More precisely, if a pair \(\{p_N,q_N\}\) is selected, put

\[
 \xi_N(d)={\bf1}_{p_N\mid d}+{\bf1}_{q_N\mid d}
           -2{\bf1}_{p_N\mid d}{\bf1}_{q_N\mid d},
 \qquad \rho_N(d)=1-\xi_N(d),
\tag{164.D2}
\]

and, if no pair is selected, put \(\xi_N(d)=0\) and \(\rho_N(d)=1\).
Thus \(\xi_N\) is exactly the XOR indicator and \(\rho_N\) is exactly
the neither-or-both indicator.  Consequently

\[
 1=\xi_N(d)+\rho_N(d)
\tag{164.D3}
\]

at every physical incidence.  The accepted sector is therefore removed once
and only once; no selected-pair incidence is lost twice, and all no-pair
products remain whole.

For \(N=2^{\epsilon_N}M_N\), with \(M_N\) odd, order the complete
residual odd-divisor universe (including zero-amplitude divisors) as

\[
 \mathscr R_N=\{d\mid M_N:\rho_N(d)=1\}
 =\{d_{N,1}<\cdots<d_{N,r_N}\}.
\tag{164.D4}
\]

With \(\sigma_{N,i}=\chi_4(d_{N,i})\),
\(C_{N,j}=\sum_{i\le j}\sigma_{N,i}\), and
\(A_{N,i}=A_N(d_{N,i})\), one has exactly

\[
 \boxed{
 b_N^{\rm rem}:=\sum_{i=1}^{r_N}\sigma_{N,i}A_{N,i}
 =C_{N,r_N}A_{N,r_N}
  +\sum_{j<r_N}C_{N,j}(A_{N,j}-A_{N,j+1}).}
\tag{164.D5}
\]

For all sufficiently large blocks the last divisor is \(M_N\), it belongs
to \(\mathscr R_N\), and \(A_N(M_N)=0\), on both the odd- and even-\(N\)
branches.  Hence the terminal term in (164.D5) vanishes, but only after this
verification.

The residual sign mass has an exact dichotomy.  It is balanced whenever a
pair is selected, and also on every no-pair product having an odd prime
\(\equiv3\pmod4\).  The only unequal-mass case is a no-pair product all of
whose odd prime factors are \(1\pmod4\); then every residual sign is positive
and the entire divisor universe is unmatched.  Thus an unmatched term cannot
be silently discarded.  Adding the required number of zero-amplitude
cemetery atoms yields equal measures and the usual one-dimensional monotone
\(W_1\) identity.  The cemetery location is auxiliary: raw \(W_1\) records
the resulting total logarithmic displacement, while the exact coefficient
charges only the smooth variation and the support-entry, support-exit, star,
and point-value jumps crossed.  A zero-amplitude stretch has no intrinsic
coefficient cost, and the unmatched term is never discarded.

The literal positive ledger gives only

\[
 \sum_{N\asymp L^2}|c_N^{\rm rem}|\ll_\varepsilon L^2X^\varepsilon,
 \qquad
 \sum_{N\asymp L^2}|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon,
\tag{164.D6}
\]

where
\(c_N^{\rm rem}=\mu^2(N)(L^2/N)^{3/4}b_N^{\rm rem}\) includes the
literal outer shell convention.  Smooth logarithmic differentiation has
size \(O(1+L/H)=O(1)\), not \(O(L^{-1/2})\), and the residual contains
unit-size unmatched or hard-crossing terms.  Hence within-\(N\) positive
transport does not recover the missing \(L^{1/2-o(1)}\).

The outer phase can nevertheless be retained exactly.  Let an integer
interval of \(M_L\asymp L^2\) consecutive sites contain the literal
half-open \(N\)-shell, extend \(c_N^{\rm rem}\) by zero to the rest of
that interval and outside it, put \(R=\lceil L\rceil\), and define the
Fejer correlation energy

\[
 \mathfrak E_R(c^{\rm rem};J)
 :=\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\tag{164.D7}
\]

The exact Fejer/van der Corput inequality, including both zero-extended
ends, gives the sufficient reduction

\[
 \boxed{
 \mathfrak E_R(c^{\rm rem};J)\ll_\varepsilon L^2X^\varepsilon
 \quad\Longrightarrow\quad
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{164.D8}
\]

The off-diagonal in (164.D7) is one signed, actual-coefficient cross-\(N\)
bilinear form.  Because the diagonal is already bounded by (164.D6), it is
enough to bound only the real part of this Fejer-weighted aggregate by
\(L^2X^\varepsilon\).  This is strictly weaker than taking absolute values
shift by shift.  It is the smallest Fejer/vdC frontier at the accepted
energy scale: a shift length \(R=o(L)\) leaves the diagonal upper bound
\(L^4/R\) for the square of the full sum, which is larger than \(L^3\).

The bound in (164.D8) is not proved here.  It is coefficient-sensitive and
is not supplied by exact radical-collision sparsity, a common-test large
sieve, or the accepted rank-one product-collar calculation.  The latter has
positive capacity
\(\sqrt{JL}=L^{3/2}(H/L+O(L^{-1}))\); after comparison with the original
\(L^2\) bound, its favorable positive ledger still misses
\(\min\{L^{1/2},H/L\}\).  The cross-\(N\) form below identifies exactly
where that signed gain would have to occur.  This is a route no-go and an
exact analytic frontier, not a physical lower bound.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H\le J^{1/2}.
\tag{164.D9}
\]

Write \(\mathcal I_L^{\rm lit}\) for the inherited half-open
\(N\asymp L^2\) shell, including its exact endpoint/star convention.  For
each squarefree \(N\in\mathcal I_L^{\rm lit}\), write uniquely

\[
 N=2^{\epsilon_N}M_N,\qquad \epsilon_N\in\{0,1\},\qquad M_N\text{ odd}.
\tag{164.D10}
\]

The character-bearing divisors are precisely the divisors of \(M_N\).
The Round-163 selector is fixed by \((N,L,\kappa)\), not by a divisor
allocation, and selects at most one pair of distinct odd primes \(p_N,q_N\)
with

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\le\kappa L^{-1/2}.
\tag{164.D11}
\]

Equations (164.D2)--(164.D4) define the residual even when no pair is
selected.  The literal zero-extended amplitude is

\[
 A_N(d)=
 {\bf1}^{\rm lit}_{\{\sqrt N\le d\le2\sqrt N\}}
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right),
\tag{164.D12}
\]

where \({\bf1}^{\rm lit}\) retains every inherited cone face, profile
entry and exit, floor, ceiling, star, endpoint value, half-open choice, and
zero-extension convention.  The outer coefficient is

\[
 \omega_L(N)=
 {\bf1}_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4},
 \qquad c_N^{\rm rem}=\omega_L(N)b_N^{\rm rem},
\tag{164.D13}
\]

and the owner is exactly

\[
 \mathcal S_{L,1}^{\rm rem}
 =\sum_Nc_N^{\rm rem}e(J\sqrt N).
\tag{164.D14}
\]

On every common smooth cell, the only regularity used is the accepted
fixed-rescaling bound \(\eta_L'(d)\ll L^{-1}\), bounded \(C^1\) norms
for \(\Phi\) and \(W\), bounded profile values, and \(d\asymp L\) on
physical support.  No literal boundary is smoothed.  The amplitude is
viewed as a regulated finite-cell function of \(u=\log d\); a boundary
value that differs from either one-sided limit is retained as a separate
point-value jump.

No distribution theorem for primes, no lower bound for profile values on a
prime family, and no numerical experiment is used.  In particular, the
semiprime counts quoted in the Round-163 discovery report remain diagnostic
only and are not used to certify a physical residual mass in this report.

## 3. Proof or derivation

**Exact subtraction and divisor universe.**  If a pair is selected, the
accepted incidence indicator is the Boolean XOR

\[
 \xi_N(d)={\bf1}_{p_N\mid d}(1-{\bf1}_{q_N\mid d})
 +(1-{\bf1}_{p_N\mid d}){\bf1}_{q_N\mid d}.
\tag{164.D15}
\]

This is (164.D2), and its complement is

\[
 \rho_N(d)=(1-{\bf1}_{p_N\mid d})(1-{\bf1}_{q_N\mid d})
            +{\bf1}_{p_N\mid d}{\bf1}_{q_N\mid d}.
\tag{164.D16}
\]

Thus the full divisor coefficient is the disjoint sum of the accepted XOR
coefficient and \(b_N^{\rm rem}\).  If no pair is selected, (164.D15) is
zero and (164.D16) is one.  This proves exact one-time subtraction.

For even \(N=2M_N\), every \(d\) in (164.D4) is still odd and divides
\(M_N\); the factor \(2\) remains in \(N/d\).  The selector contains odd
primes only, so neither (164.D15) nor (164.D16) changes that branch.  The
smallest divisor \(1\) belongs to the residual (it contains neither selected
prime), and the largest odd divisor \(M_N\) also belongs to it (it contains
both selected primes, when a pair exists).  For \(N>16\),

\[
 M_N=N>2\sqrt N\quad(N\text{ odd}),\qquad
 M_N=N/2>2\sqrt N\quad(N\text{ even}),
\tag{164.D17}
\]

so \(A_N(M_N)=0\).  This proves the terminal assertion after retaining the
even branch and the literal zero extension.

**Ordered Abel and regulated Stieltjes identities.**  Put \(C_{N,0}=0\).
Expanding the right side of (164.D5), the coefficient of \(A_{N,i}\) is
\(C_{N,i}-C_{N,i-1}=\sigma_{N,i}\), including the first and last
indices.  This proves (164.D5) algebraically.

For the exact continuous notation, let \(u_i=\log d_{N,i}\), let
\(a_N(u)\) be the regulated literal extension of (164.D12), and put

\[
 F_N(u)=\sum_{u_i\le u}\sigma_{N,i},\qquad
 F_N(\beta^-)=\sum_{u_i<\beta}\sigma_{N,i}.
\tag{164.D18}
\]

Let \(\mathcal B_N\) be the finite set of every hard boundary of the
literal amplitude.  At \(\beta\in\mathcal B_N\), define both exact
one-sided increments

\[
 \Delta^-_\beta a_N=a_N(\beta)-a_N(\beta^-),\qquad
 \Delta^+_\beta a_N=a_N(\beta^+)-a_N(\beta).
\tag{164.D19}
\]

The two increments are necessary when a star or endpoint value differs
from both one-sided values.  Splitting every discrete difference
\(A_{N,j+1}-A_{N,j}\) into its smooth integrals and its intervening
increments gives the exact Stieltjes form

\[
\begin{aligned}
 b_N^{\rm rem}
 ={}&C_{N,r_N}A_N(M_N)
 -\int_{u_1}^{u_{r_N}}F_N(u)a'_{N,{\rm sm}}(u)\,du\\
 &-\sum_{\beta\in\mathcal B_N}
 \bigl(
 F_N(\beta^-)\Delta^-_\beta a_N
 +F_N(\beta)\Delta^+_\beta a_N
 \bigr).
\end{aligned}
\tag{164.D20}
\]

Only boundaries between \(u_1\) and \(u_{r_N}\) occur in the sum.  If no
divisor lies at \(\beta\), the two cumulative values agree and the two
increments combine to the ordinary jump.  If \(\beta=u_k\), the incoming
jump is weighted by \(C_{N,k-1}=F_N(\beta^-)\) and the outgoing jump by
\(C_{N,k}=F_N(\beta)\), exactly as in (164.D5).  Thus (164.D20) retains
half-open ties and isolated point values rather than hiding them in a
formal derivative.  By (164.D17), its terminal term is zero.

On a smooth cell, with
\(z=\sqrt{q_X}e^u/(2\sqrt N)\), differentiation gives

\[
\begin{aligned}
 a'_{N,{\rm sm}}(u)
 ={}&e^u\eta_L'(e^u)\Phi\!\left(\frac{e^u}{H+1}\right)W(z)\\
 &+\eta_L(e^u)\Phi'\!\left(\frac{e^u}{H+1}\right)
      \frac{e^u}{H+1}W(z)
 +\eta_L(e^u)\Phi\!\left(\frac{e^u}{H+1}\right)W'(z)z.
\end{aligned}
\tag{164.D21}
\]

Hence

\[
 |a'_{N,{\rm sm}}(u)|\ll 1+L/H\ll1.
\tag{164.D22}
\]

There is no residual-wide \(L^{-1/2}\) factor analogous to the selected
close-prime displacement.

**Exact sign mass, unmatched atoms, and cemetery normalization.**  Let

\[
 m_N=F_N(+\infty)
 =\#\mathscr R_N^+-\#\mathscr R_N^-.
\tag{164.D23}
\]

If no pair is selected, multiplicativity on the full odd divisor cube gives

\[
 m_N=\sum_{d\mid M_N}\chi_4(d)
 =\prod_{\ell\mid M_N}(1+\chi_4(\ell)).
\tag{164.D24}
\]

Thus \(m_N=0\) if some \(\ell\equiv3\pmod4\) divides \(M_N\), while
\(m_N=2^{\omega(M_N)}=r_N\) if all odd prime factors are
\(1\pmod4\).  In the latter case \(\mathscr R_N^-\) is empty.

If \(p_N,q_N\) are selected, write \(M_N=p_Nq_NR_N\).  The residual
divisors are exactly \(a\) and \(p_Nq_Na\), \(a\mid R_N\), and therefore

\[
 m_N=\sum_{a\mid R_N}\chi_4(a)
       \{1+\chi_4(p_Nq_N)\}=0.
\tag{164.D25}
\]

This proves the dichotomy claimed in Section 1.  It also displays why the
obvious selected-pair residual involution is not a small exchange:

\[
 b_N^{\rm rem}
 =\sum_{a\mid R_N}\chi_4(a)
   \{A_N(a)-A_N(p_Nq_Na)\}.
\tag{164.D26}
\]

Since distinct odd opposite-character primes have \(p_Nq_N\ge15\), the
two amplitudes in each brace have disjoint physical supports.  Equation
(164.D26) is an all-leakage identity, not a close-profile estimate.

For the transport formulation, put

\[
 \mu_N^+=\sum_{d\in\mathscr R_N^+}\delta_{\log d},\qquad
 \mu_N^-=\sum_{d\in\mathscr R_N^-}\delta_{\log d}.
\tag{164.D27}
\]

In the balanced case, order both sets increasingly as
\(x_1\le\cdots\le x_P\) and \(y_1\le\cdots\le y_P\).  Then

\[
 b_N^{\rm rem}=\sum_{k=1}^P\{a_N(x_k)-a_N(y_k)\},
 \qquad
 W_1(\mu_N^+,\mu_N^-)
 =\sum_{k=1}^P|x_k-y_k|
 =\int_{\mathbb R}|F_N(u)|\,du.
\tag{164.D28}
\]

The sorted coupling is the monotone minimum for total logarithmic
displacement.  In a general unequal-mass signed set, any partial matching
has the exact additional term

\[
 \sum_{x\in U_N^+}a_N(x)-\sum_{y\in U_N^-}a_N(y).
\tag{164.D29}
\]

For the present residual the only unequal case has \(U_N^+\) equal to the
whole divisor set and \(U_N^-\) empty.  To normalize it without deleting
(164.D29), choose for definiteness \(u_\dagger=\log(2M_N)\) in the zero
extension, so \(a_N(u_\dagger)=0\), and set

\[
 \widetilde\mu_N^-=\mu_N^-+m_N\delta_{u_\dagger},\qquad
 \widetilde F_N(u)=F_N(u)-m_N{\bf1}_{u\ge u_\dagger}.
\tag{164.D30}
\]

Now \(\mu_N^+\) and \(\widetilde\mu_N^-\) have equal mass and

\[
 \int a_N\,d(\mu_N^+-\widetilde\mu_N^-)=b_N^{\rm rem},
 \qquad
 W_1(\mu_N^+,\widetilde\mu_N^-)
 =\int|\widetilde F_N(u)|\,du.
\tag{164.D31}
\]

The cemetery is therefore only a mass normalization.  Moving
\(u_\dagger\) inside the same zero-extension component changes the raw
\(W_1\) distance but changes neither \(b_N^{\rm rem}\) nor its exact
variation pairing.  It does not make the unmatched term free: (164.D29)
remains the raw coefficient contribution, while a path to the cemetery pays
the smooth variation and hard jumps it crosses.  Portions on which
\(a_N\equiv0\) cost zero in that coefficient identity.  A global Lipschitz
bound by \(W_1\) may charge the full logarithmic distance and is only an
upper bound.  Equations (164.D20) and (164.D31) give the literal positive
transport bound

\[
\begin{aligned}
 |b_N^{\rm rem}|
 \le{}&\int |\widetilde F_N(u)|
               |a'_{N,{\rm sm}}(u)|\,du\\
 &+\sum_{\beta\in\mathcal B_N}
 \left(
 |\widetilde F_N(\beta^-)|\,|\Delta^-_\beta a_N|
 +|\widetilde F_N(\beta)|\,|\Delta^+_\beta a_N|
 \right).
\end{aligned}
\tag{164.D32}
\]

This separates smooth displacement, unequal mass/cemetery transport, hard
jumps, and point-value jumps exactly.  It does not assume a perfect matching
before the cemetery atoms are inserted.

**Failure of the positive target ledger.**  Every nonzero residual atom is
one literal ordered factor pair \((d,N/d)\) in a fixed
\(O(L)\times O(L)\) box.  The canonical selector is allocation-independent
and \(\rho_N\in\{0,1\}\), so there is neither multiplicity nor a second
subtraction.  Consequently the total number of physical residual incidences
is \(O(L^2)\), all amplitudes and outer normalizations are bounded, and

\[
 \sum_N|c_N^{\rm rem}|\ll L^2.
\tag{164.D33}
\]

Allowing harmless divisor powers gives the first estimate in (164.D6).
Also \(|b_N^{\rm rem}|\le\tau(M_N)\ll_\varepsilon X^\varepsilon\), so
(164.D33) implies the second estimate in (164.D6), after changing
\(\varepsilon\).

The full monotone cost in (164.D31) is at most
\(O(\tau(M_N)\log L)\) per product, and (164.D32) has
\(O(1)\)-size logarithmic derivative and literal unit-size jumps.  This is
consistent only with the same \(L^{2+o(1)}\) aggregate scale.  There is no
identity forcing an \(L^{-1/2}\) displacement on the residual.  For an
exact one-fibre check, take \(N=pq\) with odd primes
\(p<q<4p\) in the same residue class modulo four.  No opposite-character
pair can be selected, and \(q\) is the unique divisor in the upper
near-square window, so

\[
 b_N^{\rm rem}=\chi_4(q)A_N(q).
\tag{164.D34}
\]

This proves that within-product character transport can have a unit
unmatched or boundary-crossing cost.  It proves no density and no physical
lower bound because the literal profile may vanish there.  In particular,
no unaudited semiprime count is used to promote (164.D34) to aggregate mass.

The restored power ledger is therefore

\[
 \#\{\text{physical residual incidences}\}=O(L^2),\quad
 (L^2/N)^{3/4}\asymp1,\quad
 |\partial_{\log d}A_N|\ll1+L/H\ll1,
\tag{164.D35}
\]

against the target \(L^{3/2}X^\varepsilon\).  The outer phase is constant
inside one \(N\), so (164.D32) cannot use it.  A positive within-\(N\)
argument must therefore establish a new aggregate bound of size
\(L^{3/2}\) for its cumulative discrepancy, cemetery flux, and hard jumps;
the exact algebra supplies no such bound and the literal singleton control
shows why no uniform per-fibre half-power is available.

**Exact cross-\(N\) frontier.**  Let
\(\mathcal J_L=\{A_L+1,\ldots,A_L+M_L\}\), with
\(M_L\asymp L^2\), be a consecutive integer interval containing the exact
literal shell.  Put \(z_N=c_N^{\rm rem}e(J\sqrt N)\) on the shell and
\(z_N=0\) for every other integer.  For \(R=\lceil L\rceil\), define

\[
 Y_n=\sum_{h=0}^{R-1}z_{n+h}
 \qquad(A_L-R+2\le n\le A_L+M_L).
\tag{164.D36}
\]

There are exactly \(M_L+R-1\) such windows.  Every \(z_N\) is counted in
exactly \(R\) windows, including the two zero-extended ends, and hence

\[
 \sum_nY_n=R\sum_Nz_N,
 \qquad
 \sum_n|Y_n|^2=R\mathfrak E_R(c^{\rm rem};J).
\tag{164.D37}
\]

Cauchy therefore gives the exact endpoint-correct Fejer/van der Corput
inequality

\[
 \boxed{
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le \frac{M_L+R-1}{R}\,
       \mathfrak E_R(c^{\rm rem};J).}
\tag{164.D38}
\]

Expanding the second identity in (164.D37) verifies both the Fejer weight
and the absence of an endpoint error:

\[
 \mathfrak E_R(c^{\rm rem};J)
 =\sum_N|c_N^{\rm rem}|^2+2\Re\mathfrak C_{R,J,L}^{\rm rem},
\qquad
 \mathfrak C_{R,J,L}^{\rm rem}
 =\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\tag{164.D39}
\]

The factor \(2\Re\) accounts exactly for the negative shifts.  Since the
diagonal is \(O_\varepsilon(L^2X^\varepsilon)\), the smallest sufficient
signed theorem isolated by this reduction is

\[
 \boxed{
 \Re\mathfrak C_{R,J,L}^{\rm rem}
 \ll_\varepsilon L^2X^\varepsilon,}
\tag{164.D40}
\]

uniformly for the literal range and the prescribed arbitrary real \(J\).
There is no absolute value around an individual shift, divisor pair, or
Möbius opening in (164.D40).

The inner correlations have an exact additive product interpretation.  Put
\(N=dm\) and \(N+r=d'm'\), where \(d,d'\) are the odd
character-bearing divisors and \(m=N/d\), \(m'=(N+r)/d'\).  Then

\[
 \boxed{d'm'-dm=r,\qquad 1\le r<R.}
\tag{164.D41}
\]

Conversely, every literal tuple satisfying (164.D41) occurs once.  Thus the
exact incidence expansion of (164.D39) is

\[
\begin{aligned}
 \mathfrak C_{R,J,L}^{\rm rem}
 ={}&\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{\substack{d,m,d',m'\ge1\\d,d'\equiv1\pmod 2\\
                  d'm'-dm=r\\
                  dm,d'm'\in\mathcal I_L^{\rm lit}\\
                  \mu^2(dm)\mu^2(d'm')=1}}
 \omega_L(d'm')\overline{\omega_L(dm)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right)\\
 &\times\chi_4(d')\chi_4(d)
 \rho_{d'm'}(d')\rho_{dm}(d)
 A_{d'm'}(d')\overline{A_{dm}(d)}.
\end{aligned}
\tag{164.D42}
\]

The zero extensions in \(\omega_L\) and \(A\) impose the exact half-open
shell, squarefreeness, coprimality, cone, profiles, parity, floors, stars,
and endpoint values.  In particular, when \(dm\) is even, \(d\) remains
odd and the factor \(2\) remains in \(m\), and similarly on the primed
side.  Equation (164.D42) retains both selectors and the true multiplicity
one incidence map.  It is an actual-coefficient theorem, not a theorem for
arbitrary arrays.

At the energy level in (164.D6), \(R\asymp L\) is minimal for this Fejer
reduction.  The diagonal part of (164.D38) alone has scale

\[
 \frac{M_L+R-1}{R}\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon \frac{L^4}{R}X^\varepsilon.
\tag{164.D43}
\]

The target square \(L^3X^\varepsilon\) first becomes available at
\(R\asymp L\).

The coefficient sensitivity is necessary.  On the \(Q_L\asymp L^2\)
ambient squarefree rows in the shell, the complex phase-aligned diagnostic
\(a_N=e(-J\sqrt N)\) has \(z_N=1\).  If \(q_n\) counts its rows in the
window in (164.D36), then \(\sum_nq_n=RQ_L\), and hence

\[
 \mathfrak E_R(a;J)=\frac1R\sum_nq_n^2
 \ge\frac{RQ_L^2}{M_L+R-1}\asymp L^3,
\tag{164.D44}
\]

although \(\sum_N|a_N|^2\asymp L^2\).  A real diagnostic has the same
capacity.  For \(a_N^{(c)}=\cos(2\pi J\sqrt N)\) and
\(a_N^{(s)}=\sin(2\pi J\sqrt N)\), the two corresponding window sums
satisfy

\[
 |Y_n^{(c)}|^2+|Y_n^{(s)}|^2\ge q_n^2/2.
\tag{164.D45}
\]

Therefore one of the two global real arrays has Fejer energy
\(\gg L^3\).  These arrays obey the coarse support and energy scales and
falsify every coefficient-uniform inference of (164.D40).  They are not
(164.D42), so they give no physical lower bound.

Finally compare (164.D40) literally with the accepted product-collar
obstruction.  The new correlation is a physical additive near-product
collar (164.D41) of width \(R\asymp L\) around \(d'm'=dm\), with exact
outer phase

\[
 J(\sqrt{dm+r}-\sqrt{dm})
 =\frac{Jr}{\sqrt{dm+r}+\sqrt{dm}}.
\tag{164.D46}
\]

By contrast, write \(Q_0,R_0\) for the two Möbius-opening scales in the
accepted character-Poisson calculation.  Simultaneous Poisson on one smooth
coefficient produces the dual rank-one resonance

\[
 s\ell=XQ_0R_0,\qquad
 |s\ell-XQ_0R_0|\ll Q_0R_0J/L,
\tag{164.D47}
\]

with coefficient scale \(L^{3/2}/(Q_0R_0\sqrt J)\) and positive collar
count \((Q_0R_0J/L+1)X^\varepsilon\).  Their product is

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}(H/L+O(L^{-1}))X^\varepsilon.
\tag{164.D48}
\]

The residual selector changes only the joint coefficient; it does not
remove the radial null direction or prove that the dual collar is sparse.
Taking absolute values in (164.D42), or applying (164.D47) separately to
its two coefficient factors, destroys the Fejer-weighted real aggregate in
(164.D40) and reproduces the accepted adverse positive ledger.  Conversely,
the rank-one collar obstruction is not a disproof of (164.D40): (164.D40)
asks for cancellation between actual residual coefficients subject to the
additive relation \(d'm'-dm=r\) before a positive norm.  Thus the smallest
surviving route is precisely a signed cross-\(N\), actual-coefficient
theorem of the form (164.D40), not another within-product matching or a
termwise positive product-collar estimate.

## 4. First doubtful or unproved step

The algebra through (164.D32), including one-time subtraction, the odd/even
divisor universe, Abel summation, exact sign-mass classification, cemetery
normalization, and hard point-value jumps, is proved.  The first unproved
estimate is the assertion that the positive right side of (164.D32), after
summing over \(N\), is

\[
 O_\varepsilon(L^{3/2}X^\varepsilon).
\tag{164.D49}
\]

The available literal ledger gives only \(L^{2+o(1)}\), the selected-pair
residual involution (164.D26) has disjoint supports, and (164.D34) rules out
a uniform per-fibre small-difference claim.  Therefore (164.D49) must not be
asserted.

After preserving the outer phase, the first unproved analytic statement is
(164.D40), which together with (164.D38) implies (164.D8).  Exact collision sparsity controls only
exact phase coincidences; it supplies no near-collision or actual-direction
bound for (164.D39).  The phase-adapted tests (164.D44)--(164.D45) also show that
support, row mass, and \(L^2\) energy cannot prove it uniformly over
coefficients.  A successful continuation must use the arithmetic of the
literal residual factors in (164.D42), and must fail on those diagnostics.

No primary fixed-modulus prime-distribution source is present in the allowed
context.  Accordingly, no \(L^{2-o(1)}\) semiprime or multiprime count is
used as a proved Round-164 input, and no such count is promoted to physical
mass.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| `residual_exact_subtraction` | **GREEN.** Equations (164.D15)--(164.D16) are disjoint and sum to one; the no-pair branch has \(\rho_N=1\). |
| `ordered_divisor_abel_identity` | **GREEN.** Equation (164.D5) follows coefficient by coefficient, and (164.D20) is its exact regulated Stieltjes form. |
| `odd_divisor_and_even_N_branch` | **GREEN.** Equations (164.D10), (164.D17) retain odd divisors of \(M_N\) and leave the factor \(2\) on the complementary leg. |
| `sign_mass_and_unmatched_atoms` | **GREEN.** Equations (164.D24)--(164.D25) prove balanced mass except for the all-\(1\pmod4\), no-pair case, where every atom is unmatched positive mass. |
| `monotone_transport_normalization` | **GREEN identity, OPEN estimate.** Equations (164.D28)--(164.D31) give exact monotone \(W_1\) and cemetery normalization; no target aggregate bound follows. |
| `profile_jump_and_zero_extension_variation` | **GREEN identity, OPEN estimate.** Equation (164.D20) separates smooth variation, incoming/outgoing hard jumps, star values, and zero-extension crossings exactly. |
| Residual semiprime placement | **GREEN diagnostic.** Equation (164.D34) is an exact residual singleton when its profile is active.  No density or profile lower bound is claimed, and no unaudited prime count is used. |
| `outer_N_phase_preservation` | **GREEN reduction, OPEN theorem.** Equations (164.D36)--(164.D40) retain \(e(J\sqrt N)\) and isolate the exact cross-\(N\) signed form. |
| `rank_one_product_collar_comparison` | **GREEN obstruction scope.** Equations (164.D47)--(164.D48) reproduce the accepted collar powers and show why positive Poisson does not prove (164.D40). |
| `arbitrary_real_centre_phase` | **GREEN scope.** The exact phase difference is retained for the prescribed real \(J\); no exact opposition or unproved modulo-one gap is assumed. |
| `missing_L_half_power` | **GREEN ledger, OPEN saving.** Equations (164.D33)--(164.D35) leave \(L^{1/2-o(1)}\); length-\(L\) Fejer energy control in (164.D8) would recover it. |
| `physical_coefficient_vs_diagnostic` | **GREEN.** Equations (164.D14), (164.D42) are physical; (164.D34) without profile density and (164.D44)--(164.D45) are explicitly diagnostic and give no lower bound. |
| `remaining_few_point_and_downstream_scope` | **GREEN quarantine.** Nothing here treats the other \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels, full hard TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter target, or either global exponent. |
| Numerical experimentation | **NOT USED.** The report is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

Only the following authorized files were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round164_m2_hard_top_t1_residual_signed_divisor_transport_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/candidates/conductor_round164_residual_transport_seed.md`;
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/synthesis.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/literal_near_square_divisor_involution_attack.md`.

The accepted graph facts used are the literal \(t=1\) product grouping,
the Round-163 selector and strict XOR sector, bounded fixed-cell profile
regularity, the odd character factor and even complementary branch, the
hard-TOP coefficient-energy scale, the exact-collision scope, the
coefficient-uniform common-test obstruction, and the rank-one
character-Poisson collar obstruction.  No external source, sibling Round-164
report, shared synthesis, computation, or numerical experiment was used.

## 7. Recommended state effect

**Retain** (164.D2)--(164.D32) as candidate exact residual bookkeeping and
transport algebra, and retain (164.D36)--(164.D40) as the first exact
cross-\(N\), actual-coefficient frontier after within-product positive
transport fails.  Subject them to the required independent Abel/jump and
cross-\(N\) seam reviews before any graph mutation.

**Record only a route-scoped no-go** under
`hard_top_t1_residual_transport_no_go`: the complete residual is not proved
target-safe by positive ordered-divisor transport, cemetery matching,
profile variation, or the accepted positive rank-one collar.  This does not
disprove the residual target; a proof of (164.D40), or a weaker direct
estimate implying (164.D8), would still close it.

**No change** is recommended to the status of the complete \(t=1\) residual,
the remaining few-point channels, either hard-TOP parent, either smooth M2
packet, M9--M2, M9--M1, endpoint uniformity, M9, the conditional bridge, the
Gauss-circle quarter target, or either global exponent.

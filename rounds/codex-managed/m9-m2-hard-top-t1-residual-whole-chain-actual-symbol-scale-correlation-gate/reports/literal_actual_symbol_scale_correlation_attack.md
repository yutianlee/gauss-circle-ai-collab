# Round 175 literal actual-symbol scale-correlation attack

- Campaign: `m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate`
- Round: 175
- Task: `literal_actual_symbol_scale_correlation_attack`
- Role: discovery
- Starting graph: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

No factor-\(L\) property of the literal squarefree/selector/character/profile symbol
survives the exact whole-chain and endpoint restoration using only the
available algebraic identities.  The narrow exact result is a
**whole-chain endpoint-collapse and literal-row noncancellation no-go**.

Let \(\mathcal N_{R,S}\) be exactly (175.4), with both absolute-parity
branches, the character factor \(i/2\), the squared factor \(1/8\), all odd
\(k,k'\), all nonzero ordinary frequencies \(\ell,\ell'\), and one outer
real part.  Then, without taking any modulus,

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 =\mathcal N^{*}_{R_0,M},}
 \tag{175.A1}
\]

where \(\mathcal N^{*}_{R_0,M}\) is the same complete expression with the
single endpoint multiplier \(F_M-F_{R_0}\).  Thus all intermediate stopped
scales disappear algebraically.  When
\(R_{K-1}<M<2R_{K-1}\), the strict final link is retained exactly and is not
rounded; when \(M=2R_{K-1}\), the final link is the exact doubling.  At each
fixed positive physical gap, all adjacent-link
weights are nonnegative and add to

\[
 b_{R_0,M}(r)=
 \begin{cases}
 r(1/R_0-1/M),&0<r<R_0,\\
 1-r/M,&R_0\le r<M,\\
 0,&r\ge M,
 \end{cases}
 \qquad b_{R_0,M}(0)=0.
 \tag{175.A2}
\]

Consequently there is no scale-martingale sign, selector change, character
change, or profile change on which to base a cancellation in the scale index:
the literal coefficient is independent of \(j\), and summing the scale
differences merely returns the endpoint K26 kernel.

Expanding the actual coefficient reveals no missing pointwise mean-zero
identity.  Writing

\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),\qquad
 \omega_L(N)=\mathbf1_{N\in\mathcal I_L^{\rm lit}}
 \mu^2(N)\left(\frac{L^2}{N}\right)^{3/4},
 \tag{175.A3}
\]

the squarefree factor is a nonnegative row projector.  If no pair is
selected, \(\rho_N\equiv1\), and an allowed all-\(1\pmod4\) odd-prime row
has constant character \(\chi_4(d)=1\).  If an opposite-character pair
\(p_N,q_N\) is selected and \(M_N=p_Nq_NR_N\), then the only surviving
incidences are neither and both, and exactly

\[
 c_N^{\rm rem}
 =\omega_L(N)\sum_{a\mid R_N}\chi_4(a)
 \{A_N(a)-A_N(p_Nq_Na)\}.
 \tag{175.A4}
\]

Although the corresponding unit-profile character mass is zero, the two
literal physical supports in each brace are disjoint because
\(p_Nq_N\ge15\).  Hence the apparent selector cancellation pairs a live
incidence with a zero-extended incidence and supplies no \(L^{-1}\) gain.
The exact divisor-Abel formula for the profile has total variation \(O(1)\),
not \(O(L^{-1})\), after its hard endpoints and zero-extension jumps are
restored.

After collective ordinary-zero restoration, (175.A1) is exactly the physical
endpoint K26 form up to \(O_\varepsilon(L^3X^\varepsilon)\).  Any continuation
which now uses only coefficient energy, profile BV, shiftwise Cauchy, or a
coefficient-uniform positive norm has capacity

\[
 M D_L\ll_\varepsilon L^4X^\varepsilon,
 \tag{175.A5}
\]

so the missing factor \(L\) is restored, not saved.  The accepted dechirped
one-parity example attains this order.  This is not literal physical lower
mass and does not disprove K26.

Terminal label recommended for this report:
`whole_chain_actual_symbol_capacity_or_self_return_no_go`.

## 2. Exact statement and hypotheses

Put \(e(t)=e^{2\pi it}\), \(J=\sqrt X\),
\(1\ll L\ll H\le J^{1/2}\), \(R_0=\lceil L\rceil\), and let
\(M=M_L\asymp L^2\) be the exact cardinality of the containing interval.
Write \(N=2^{\nu_N}M_N\), with \(M_N\) odd.  Every coefficient is extended
by zero to the whole containing interval, and a square root is evaluated only
at a positive literal site.  The complete coefficient is

\[
 \begin{aligned}
 c_N^{\rm rem}
 &=\sum_{d\mid M_N}\chi_4(d)\lambda_N(d),\\
 \lambda_N(d)&=\omega_L(N)\rho_N(d)A_N(d),\\
 z_N&=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
 \end{aligned}
 \tag{175.A6}
\]

Here \(A_N(d)\) retains the complete two-adic branch, Vaaler/profile factor,
floors, stars, selected and no-pair support crossings, hard endpoints, point
values, and zero-extension values.  On every nonzero incidence,
\(N\asymp L^2\), \(d,m=N/d\asymp L\), and the opened multiplicity is
\(X^{O(\eta)}\).  If no pair is selected, \(\rho_N(d)=1\).  If
\(p_N,q_N\) are selected, then

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}.
 \tag{175.A7}
\]

Thus \(\rho_N\) is the complement of XOR, not a signed weight.

The stopped chain is minimal and exact:

\[
 R_{j+1}=\min(2R_j,M),\qquad R_K=M.
 \tag{175.A8}
\]

No assumption that \(M/R_0\) is a power of two is made.  Set
\(F_R(\theta)=\sum_{|r|<R}(1-|r|/R)e(r\theta)\) and
\(B_{R,S}=F_S-F_R\).

For the fixed disjoint cardinal bump \(\varphi\), insert (175.A3) into the
literal interpolation:

\[
 \begin{aligned}
 \mathcal W_\epsilon(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ \mathrm{odd}}}
 (-1)^{\epsilon m}\omega_L(dm)\rho_{dm}(d)A_{dm}(d)
 \varphi(x-d)\varphi(y-m),\\
 \mathcal B_{\epsilon,\theta}(x,y)
 &=\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy),\\
 U_{k,\ell}^{(\epsilon)}(\theta)
 &=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
 \end{aligned}
 \tag{175.A9}
\]

All cells, openings, support births/deaths, frequency endpoints, hard
endpoints, transitions, and zero values occur in this single exact
interpolation.  Define only after the complete odd-character recombination

\[
 \begin{aligned}
 Z_{\epsilon,0}(\theta)
 &=\frac i2\sum_{k\ \mathrm{odd}}\chi_4(k)U_{k,0}^{(\epsilon)}(\theta),\\
 Z_{\epsilon,*}(\theta)
 &=\frac i2\sum_{k\ \mathrm{odd}}\chi_4(k)
   \sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}(\theta).
 \end{aligned}
 \tag{175.A10}
\]

The theorem proved here has three exact parts.

1. **Endpoint collapse.** Equation (175.A1) holds with all frozen
   normalizations.
2. **Literal algebraic noncancellation.** Equations (175.A3)--(175.A4), the
   selected-support separation, the no-pair constant-character shadow, and
   the full zero-extended profile-Abel identity show that none of the
   squarefree projector, selector balance, row character, or profile BV
   gives an algebraic \(L^{-1}\) multiplier.
3. **Restored-capacity consequence.** If after these identities one takes a
   coefficient-uniform positive/absolute bound, then the available endpoint
   scale is (175.A5).  No statement is made against a genuinely signed,
   coefficient-sensitive estimate for the complete endpoint form.

## 3. Proof or derivation

### 3.1 Exact character transform and whole-chain telescope

The accepted character--Poisson identity is

\[
 Z_\epsilon(\theta)
 =\frac i2\sum_{k\ \mathrm{odd}}\chi_4(k)
   \sum_{\ell\in\mathbb Z}U_{k,\ell}^{(\epsilon)}(\theta)
 =Z_{\epsilon,0}(\theta)+Z_{\epsilon,*}(\theta).
 \tag{175.A11}
\]

The two values \(\epsilon=0,1\) are the absolute-site parity branches.  Since
\(d\) is odd, \((-1)^{\epsilon N}=(-1)^{\epsilon m}\); this keeps both the
odd--odd branch and the squarefree even--even branch.  In the latter branch
both products are \(2\pmod4\), so every surviving physical gap is a multiple
of four.  No parity branch is identified with the other or deleted.

Expanding \(|Z_{\epsilon,*}|^2\) only after all \(k\) and nonzero \(\ell\)
have been recombined gives, with no inequality,

\[
 \mathcal N_{R,S}
 =\frac12\sum_{\epsilon=0}^1
   \int_0^1 B_{R,S}(\theta)
   |Z_{\epsilon,*}(\theta)|^2\,d\theta.
 \tag{175.A12}
\]

Indeed the parity average contributes \(1/2\), while
\(|i/2|^2=1/4\), giving exactly \(1/8\).  Equation (175.A12) is merely a
factorization of the single outer real part in (175.4); it is not a positive
estimate because \(B_{R,S}\) is signed as a function of \(\theta\).

The functions \(Z_{\epsilon,*}\), including every literal symbol and cell,
do not depend on the Fejer scale.  Absolute convergence from the compact
smooth cardinal interpolation therefore permits the finite sum over links
inside the integral, and

\[
 \sum_{j<K}B_{R_j,R_{j+1}}
 =\sum_{j<K}(F_{R_{j+1}}-F_{R_j})
 =F_M-F_{R_0}.
 \tag{175.A13}
\]

Equations (175.A12)--(175.A13) prove (175.A1).  In particular, a strict last
link \(R_{K-1}<M<2R_{K-1}\) is included with its actual Fejer difference and
cancels only its common \(F_{R_{K-1}}\) endpoint.  There is no rounded Haar
identity at that link.

On physical Fourier coefficients, (175.A13) says

\[
 \sum_{j<K} b_{R_j,R_{j+1}}(r)=b_{R_0,M}(r),
 \tag{175.A14}
\]

and direct subtraction of triangular Fejer coefficients gives (175.A2).
Each summand and the endpoint weight are nonnegative for \(r>0\).  Hence a
fixed physical atom has no alternating or mean-zero scale signature.  Any
cross-link cancellation that remains is exactly cancellation in the final
signed endpoint correlation; it is not an additional martingale difference
of the literal symbol.

### 3.2 Collective ordinary-zero restoration and exact return to K26

Let \(\mathcal Z_{R,S}\) denote the complete transformed sector in which at
least one of \(\ell,\ell'\) is zero, counted once after the full odd-character
recombination.  Then

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =\mathcal N_{R,S}+\mathcal Z_{R,S}.
 \tag{175.A15}
\]

The accepted reverse character identity and one cellwise integration by
parts give

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta L^2J^{-1}X^\eta.
 \tag{175.A16}
\]

Apply this collectively at the single endpoint multiplier.  Since
\(\|F_M-F_{R_0}\|_\infty\le M+R_0\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), \(M\asymp L^2\), and \(L^2\le J\),

\[
 \begin{aligned}
 |\mathcal Z^*_{R_0,M}|
 &\ll (M+R_0)
 \left(D_L^{1/2}\frac{L^2}{J}
       +\frac{L^4}{J^2}\right)X^{O(\eta)}\\
 &\ll_\varepsilon L^3X^\varepsilon.
 \end{aligned}
 \tag{175.A17}
\]

This is one collective estimate over every odd \(k\); it gives no termwise
zero-mode estimate.  It also pays the ordinary-zero sector once for the
whole chain, not once per cell, opening, or frequency.

Put

\[
 C_r=\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
 \tag{175.A18}
\]

Then the physical endpoint difference is exactly

\[
 \Delta_{R_0,M}:=\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 =2\Re\sum_{\substack{0<r<M\\2\mid r}}b_{R_0,M}(r)C_r,
 \tag{175.A19}
\]

and (175.A1), (175.A15), and (175.A17) give

\[
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}
 =\Delta_{R_0,M}-\mathcal Z^*_{R_0,M}.
 \tag{175.A20}
\]

The physical coefficient at \(r=0\) is zero because
\(b_{R_0,M}(0)=0\).  This does not delete any fixed dual diagonal: the two
cardinal variables on such a diagonal remain independent, and their
contribution cancels only inside the complete dual/cell/endpoint/transition
recombination used above.

The accepted once-only short correction satisfies

\[
 T_{26}=\frac12\Delta_{R_0,M}-B_{\rm short},
 \qquad |B_{\rm short}|\ll_\varepsilon L^3X^\varepsilon.
 \tag{175.A21}
\]

Combining (175.A20)--(175.A21),

\[
 \boxed{
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})-\mathcal Z^*_{R_0,M}.}
 \tag{175.A22}
\]

Thus the whole-chain target is exactly K26 modulo two already target-safe
terms.  No second short correction, terminal correction, or zero-mode charge
is present.

### 3.3 Complete literal physical expansion

Substituting (175.A6) into (175.A18) gives the exact endpoint atom before any
modulus:

\[
\begin{aligned}
 C_r=\sum_N&\omega_L(N+r)\omega_L(N)
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\\
 &\times\sum_{d'\mid M_{N+r}}\sum_{d\mid M_N}
 \chi_4(d')\chi_4(d)\,
 \rho_{N+r}(d')\rho_N(d)\,
 A_{N+r}(d')\overline{A_N(d)}.
\end{aligned}
 \tag{175.A23}
\]

Every term with a forbidden product, nonsquarefree product, failed selector,
failed coprimality condition, absent profile, hard support crossing, or
outside-containing-interval value is literally zero in (175.A23).  Every
allowed term appears with multiplicity one.  Equations (175.A2), (175.A19),
and (175.A23) are therefore the complete one-sided physical whole-chain
aggregate.  They retain both product-parity branches, every frequency through
the exact equivalence (175.A20), every cardinal cell and arithmetic opening,
all endpoints and transitions, and the single outer real part.

Crucially, every factor in the second and third lines of (175.A23) is
independent of \(j\).  The scale sum can act only on the scalar Fejer weight,
and (175.A14) exhausts that action.

### 3.4 Selector and character algebra: where the apparent gain fails

Suppose first that \(p_N,q_N\) are selected.  Squarefreeness writes
\(M_N=p_Nq_NR_N\), with \(p_N,q_N\nmid R_N\).  The complement-of-XOR
selector retains exactly

\[
 d=a\quad\hbox{or}\quad d=p_Nq_Na,qquad a\mid R_N.
\]

The selected primes have opposite \(\chi_4\)-characters, so
\(\chi_4(p_Nq_N)=-1\).  Pairing the two formal divisor-cube points proves
(175.A4).  For the unit profile it also proves the ambient identity

\[
 \sum_{d\mid M_N}\chi_4(d)\rho_N(d)=0.
 \tag{175.A24}
\]

However, the accepted literal support separation says that the two profile
values in each brace of (175.A4) cannot both be nonzero: multiplication of
the divisor by \(p_Nq_N\ge15\) moves it outside the paired near-square
physical support.  Therefore, pointwise in \(a\),

\[
 |A_N(a)-A_N(p_Nq_Na)|
 =|A_N(a)|+|A_N(p_Nq_Na)|.
 \tag{175.A25}
\]

Thus (175.A24) is balanced by zero-amplitude/cemetery points.  Restoring the
literal profile removes the putative cancellation completely at the paired
incidence level.  Cancellation across different \(a\), different \(N\), or
different gaps remains possible, but it would be a new signed theorem, not
the selector identity.

If no pair is selected, \(\rho_N\equiv1\) and

\[
 \sum_{d\mid M_N}\chi_4(d)
 =\prod_{p\mid M_N}(1+\chi_4(p)).
 \tag{175.A26}
\]

When every odd prime factor is \(1\pmod4\), (175.A26) equals
\(2^{\omega(M_N)}\) and every divisor character equals \(+1\).  Hence no
rowwise or termwise character cancellation is valid uniformly on the
literal support.  The same obstruction appears in the even-gap cofactor
chart, where the accepted character is frozen along every row; the
squarefree even--even branch is included.

### 3.5 Squarefree, profile, endpoint, and zero-extension audit

On a live row, \(\mu^2(N)=1\) and is common to every divisor incidence.
In (175.A23) the squarefree contribution is the nonnegative projector
\(\mu^2(N+r)\mu^2(N)\).  The identity
\(\mu^2(n)=\sum_{q^2\mid n}\mu(q)\) can introduce a formal signed opening,
but on a squarefree live product it reduces to its \(q=1\) term.  On a
nonsquarefree product the additional terms cancel exactly to restore the
literal zero.  Taking a norm before that restoration loses the coefficient;
performing the restoration returns the projector in (175.A23).  Therefore
the squarefree identity alone yields no algebraic \(L^{-1}\).  A genuinely
signed cross-\(N\) squarefree correlation remains unexcluded.

For ordered surviving divisors \(d_1<\cdots<d_s\), put
\(P_j=\sum_{i\le j}\chi_4(d_i)\), \(a_i=A_N(d_i)\), and
\(a_0=a_{s+1}=0\).  The exact full zero-extended Abel identity is

\[
 \sum_i\chi_4(d_i)a_i
 =-\sum_{j=0}^sP_j(a_{j+1}-a_j),
 \tag{175.A27}
\]

including the incoming and outgoing hard-face increments with their left and
inclusive cumulative values.  The accepted literal total variation is

\[
 V_N:=\sum_{j=0}^s|a_{j+1}-a_j|=O(1),
 \tag{175.A28}
\]

not \(O(L^{-1})\).  Smooth interior increments may be small, but support
births, deaths, point values, selector changes, the squarefree projector, and
the two outer zero-extension jumps restore order-one variation.  Consequently
Abel/BV yields only

\[
 \left|\sum_i\chi_4(d_i)a_i\right|
 \le\frac12\operatorname{osc}(P_N)V_N,
 \tag{175.A29}
\]

with no factor \(L^{-1}\).  This is precisely the place where a proposed
profile derivative gain is restored at the literal boundary.

The smooth scalar part \((L^2/N)^{3/4}\) of \(\omega_L(N)\) also supplies
no scale-index difference: it is fixed throughout the stopped chain.  Any
attempt to difference it in \(N\) must simultaneously difference the
squarefree mask, literal shell, selector, profile crossings, and zero
extension; those have unit-scale jumps and return to the full literal
correlation (175.A23).

### 3.6 Restored power

Fixed-shift Cauchy gives \(|C_r|\le D_L\).  Also

\[
 \sum_{r=1}^{M-1}b_{R_0,M}(r)=\frac{M-R_0}{2},
 \tag{175.A30}
\]

so (175.A19) gives the coefficient-insensitive absolute capacity

\[
 |\Delta_{R_0,M}|
 \le 2D_L\sum_{\substack{0<r<M\\2\mid r}}b_{R_0,M}(r)
 \le (M-R_0)D_L
 \ll_\varepsilon L^4X^\varepsilon.
 \tag{175.A31}
\]

Equivalently, positivity gives
\(\Delta_{R_0,M}\le\mathfrak E_M^{(2)}\le MD_L\).  Since the target is
\(L^3X^\varepsilon\), the endpoint length \(M\asymp L^2\), rather than an
effective length \(O(L)\), restores exactly one factor \(L\).

This capacity is sharp for the coefficient-uniform interface.  On the
accepted diagnostic subfamily \(M=4P\), put \(z_N=1\) on the \(2P\) even
sites.  Then \(D_L=2P\) and the final stopped-chain link
\(2P\to4P\) has increment

\[
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}
 =P^2=\frac18MD_L.
 \tag{175.A32}
\]

All its physical correlations are nonnegative, so the full endpoint
difference is at least this large.  Dechirping by
\(c_N=e(-J\sqrt N)\) realizes this as a lawful-support coefficient-uniform
control.  It is not the literal residual symbol and proves no physical lower
bound, but it rules out extracting the missing factor from the endpoint
telescope, support, parity, energy, or positivity alone.

The complete restored ledger is therefore

| item | exact/proved scale | effect on the factor \(L\) |
|---|---:|---|
| whole nonzero-frequency chain | single endpoint form (175.A1) | no saving; all intermediate scales cancel algebraically |
| physical endpoint coefficient mass | \(MD_L\ll L^4X^\varepsilon\) | restores the missing \(L\) |
| selected-row ambient character balance | zero only for the unit profile | restored by disjoint literal supports, (175.A25) |
| profile derivative/BV | \(V_N=O(1)\) | restored at hard and zero-extension jumps |
| collective ordinary-zero sector | \(O_\varepsilon(L^3X^\varepsilon)\) | target-safe, paid once |
| short correction | \(O_\varepsilon(L^3X^\varepsilon)\) | target-safe, paid once |
| terminal link (strict only when \(R_{K-1}<M<2R_{K-1}\)) | exact in (175.A13) | no rounding cost and no gain |
| desired nonzero endpoint correlation | \(O_\varepsilon(L^3X^\varepsilon)\) | open; requires a genuine literal signed saving |

## 4. First doubtful or unproved step

The first unproved step is the coefficient-sensitive one-sided endpoint
estimate obtained by inserting (175.A23) into (175.A19):

\[
 \boxed{
 \Re\sum_{\substack{0<r<M\\2\mid r}}b_{R_0,M}(r)C_r^{\rm lit}
 \ll_\varepsilon L^3X^\varepsilon.}
 \tag{175.A33}
\]

Equivalently, after the collectively controlled ordinary-zero sector, it is
exactly (175.5).  No accepted identity proves cancellation simultaneously
across \(r,N,d,d'\), the two parity branches, selector choices, squarefree
masks, odd character frequencies, nonzero ordinary frequencies, cells,
openings, endpoints, transitions, and zero-extension pieces.

The first false step in each attempted elementary mechanism is now explicit.

1. **Scale telescope:** claiming a gain from the number of links after
   (175.A13).  The chain has already collapsed to one endpoint kernel.
2. **Selected-pair mean zero:** replacing (175.A4) by the unit-profile identity
   (175.A24).  The paired literal supports are disjoint.
3. **Row character cancellation:** assuming \(\chi_4\) oscillates on every
   surviving row.  No-pair all-\(1\pmod4\) rows and even-shift cofactor rows
   have frozen character.
4. **Squarefree Möbius gain:** taking a norm before nonsquarefree terms
   recombine to the literal zero.  Exact restoration returns the positive
   projector.
5. **Profile derivative gain:** discarding hard point values, support
   births/deaths, or zero-extension jumps.  Their restoration gives
   \(V_N=O(1)\), not \(O(L^{-1})\).
6. **Positive endpoint closure:** applying Cauchy, Parseval, a positive
   transformed norm, or a fixed-mode/cell norm before a literal signed gain.
   Equation (175.A31) restores \(L^4X^\varepsilon\).

Unexcluded routes are exactly: a nonlocal signed theorem for (175.A33); a
cross-\(N\), cross-gap correlation of the literal squarefree and selector
patterns with the square-root phase; collective character cancellation
across different rows and all odd \(k\), rather than within a frozen row; a
profile-sensitive endpoint theorem which includes all hard and zero jumps; a
coupled theorem over all \(k,k',\ell,\ell'\), cells and openings before any
norm; or a coefficient-sensitive positive theorem which first proves an
actual-literal bound stronger than \(MD_L\).  Cross-link cancellation remains
unexcluded only in its exact endpoint realization (175.A33), not as an
independent scale martingale.  A genuinely different tangent mechanism is
also not excluded; the Round-173 first difference, its adjoint, and its
second-Abel return remain parked.

## 5. Control tests and outcomes

| control | outcome |
|---|---|
| literal residual coefficient | **PASS.** Equations (175.A3), (175.A6), (175.A7), (175.A9), and (175.A23) retain \(\omega_L\rho_NA_N\), squarefreeness, coprimality, both selector states, all profiles, floors, stars, endpoints, point values, crossings, and zero extension. |
| one-sided whole chain | **PASS.** Equations (175.A1), (175.A12), and (175.A20) have no absolute value outside the chain. |
| parity transform constants | **PASS.** Both \(\epsilon=0,1\) branches remain; \(i/2\), \(1/8\), odd \(k,k'\), nonzero \(\ell,\ell'\), and one outer real part are preserved. |
| ordinary-zero collective recombination | **PASS.** It is restored only through the complete odd-character sum and bounded once in (175.A17). |
| terminal link | **PASS.** The actual final \(F_M-F_{R_{K-1}}\) occurs in (175.A13).  It is strict only when \(R_{K-1}<M<2R_{K-1}\); if \(M=2R_{K-1}\), it is the exact doubling.  No rounding is introduced. |
| once-only short correction | **PASS.** It appears exactly once in (175.A21)--(175.A22). |
| dechirped one-parity control | **RED for a target proof; PASS for the no-go.** Equation (175.A32) attains order \(MD_L\asymp L^4\), so scale collapse plus positivity does not save \(L\).  It is not asserted to be literal mass. |
| arbitrary-sign control | **RED for coefficient-uniform cancellation.** Choosing \(c_N=e(-J\sqrt N)a_N\) leaves an arbitrary signed array \(z_N=a_N\); the endpoint identity is unchanged.  Any valid target proof must use more than support and energy. |
| constant-character control | **RED for rowwise character gain.** On no-pair rows with every odd prime \(1\pmod4\), \(\chi_4(d)=1\) for every divisor. |
| erased-selector control | **RED for a uniform selector gain.** On every no-pair row the literal selector already equals one.  On selected rows, the only exact zero mass is destroyed by the disjoint literal supports in (175.A25). |
| one-site control | **PASS.** Every physical \(r>0\) correlation and the endpoint bandpass are zero.  Thus a surviving isolated positive dual diagonal is necessarily missing compensating dual/cell/boundary pieces. |
| fixed-dual-diagonal control | **RED for diagonal deletion.** The physical coefficient \(b(0)=0\) does not set a fixed \((k,\ell)=(k',\ell')\) contribution to zero; the proof keeps the full recombination. |
| rank-one peak control | **RED for uniform nondegenerate stationary phase.** The endpoint multiplier retains both centred Fejer peaks, and the accepted product-phase Hessian is rank one at each centre.  No such estimate is used here. |
| squarefree control | **RED for pointwise Möbius saving.** Exact Möbius restoration gives either the live \(q=1\) term or the literal zero; only a new signed cross-product theorem remains possible. |
| profile/endpoint/transition control | **PASS.** The full cardinal interpolation is retained, and (175.A27)--(175.A29) charge every endpoint and zero jump. |
| physical versus fixed dual diagonal | **PASS.** Equation (175.A19) has zero physical diagonal, while Section 3.2 explicitly forbids deleting a fixed dual diagonal. |
| positive-capacity factor \(L\) | **PASS.** The factor is restored precisely in (175.A31): \(M\asymp L^2\) times \(D_L\asymp L^2\) has capacity \(L^4\), against the \(L^3\) target. |
| Round-172 scope | **PASS.** The report proves no physical lower mass and does not rule out a literal positive theorem after a genuine actual-symbol gain. |
| Round-173 scope | **PASS.** No tangent first difference, adjoint, or tautological second Abel transfer is used. |
| residual-only owner scope | **PASS.** The result concerns only the K26 sufficient route to the complete residual scalar. |
| no in-round pivot | **PASS.** No claim is made about K17a, another \(t=1\) channel, full hard TOP, BAL, UNBAL, M1, GAR, endpoint assembly, M9, a bridge, or an exponent. |

The controls locate every possible factor explicitly: no factor \(L\) is
saved in this report; the hoped selector factor is lost at disjoint support,
the hoped profile factor is lost at literal boundary restoration, and the
full missing factor is restored at the positive endpoint bound
\(MD_L\asymp L^4\).

## 6. Dependencies and exact artifacts used

This report used exactly the permitted context:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/round175_m2_hard_top_t1_residual_whole_chain_actual_symbol_strategy.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
7. `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`;
8. `proofs/kernels/m9_m2_hard_top_t1_residual_tangent_fejer_commutator_self_return_obstruction.md`; and
9. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`.

The mathematical dependencies are the accepted Round-164 literal residual
coefficient and Fejer reduction, the Round-165 parity/gcd/scale kernel, the
Round-172 exact cardinal transform and collective ordinary-zero theorem, and
the Round-173 boundary-complete self-return scope.  No external theorem,
web source, numerical experiment, or unlisted artifact is used.

The first doubtful step is (175.A33), as stated in Section 4.  The no-go is
strictly algebraic and capacity-scoped: it certifies endpoint collapse and the
failure of the listed automatic symbol gains, not failure of the literal
signed estimate.

## 7. Recommended state effect

**Recommended effect: retain / no proof-state change.**

If independently verified, this report may be retained as candidate evidence
for the route-scoped obstruction label
`whole_chain_actual_symbol_capacity_or_self_return_no_go`: the stopped scale
chain has no independent algebraic correlation resource because it collapses
to the endpoint kernel, and the available pointwise selector, squarefree,
character, and profile identities do not supply the missing factor before
literal endpoint restoration.

Do not promote (175.5), K26, the complete residual scalar, full \(t=1\), hard
TOP, `M9-M2-top-endpoint-density-discrepancy-energy`,
`M9-M2-top-endpoint-signed-cone`, M9--M2, M9, either bridge, the quarter
theorem, or any exponent.  The exact endpoint signed theorem (175.A33) remains
open, along with every unexcluded coefficient-sensitive route named in
Section 4.

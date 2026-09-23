## Result

The residual algebra can be derived exactly, but the requested
\(L^{3/2}X^\varepsilon\) estimate does **not** follow from the selected-prime
hypothesis by within-product signed transport.

Write
\[
 N=2^\nu n,\qquad \nu\in\{0,1\},\qquad n\ \hbox{odd}.
\]
If no pair is selected, the residual universe is the full divisor lattice
\(\mathcal U_N=\{d:d\mid n\}\).  If \(p=p_N,q=q_N\) are selected and
\(m=n/(pq)\), then
\[
 \boxed{\mathcal U_N=\{a:a\mid m\}\ \dot\cup\
                    \{pqa:a\mid m\}.}                                      \tag{1}
\]
The two pieces in (1) have opposite \(\chi _4\)-sign point by point, so
their *unweighted global* sign masses are equal.  This equality does not
give equality after the one-sided physical window and the other hard
supports are imposed.  With the amplitude zero-extended, that failure is
represented exactly by cumulative sign imbalance at the hard jumps.

The selected-prime closeness is useful only for the deleted XOR universe
\(p\{a:a\mid m\}\dot\cup q\{a:a\mid m\}\), where the sign-changing map
\(pa\leftrightarrow qa\) has logarithmic cost
\(|\log(q/p)|\leq\kappa L^{-1/2}\).  That entire universe has already been
removed.  In the residual universe the corresponding bit-changing map is
\(a\leftrightarrow pqa\), whose logarithmic cost is \(\log(pq)\), not
\(|\log(q/p)|\).  The optimal monotone cost could be smaller because of
other divisors, but no hypothesis in the statement bounds it.  The odd
divisor complement also does not repair this: it need not reverse sign,
and it carries the physical upper window outside itself (farther outside
when \(N\) is even).

Consequently the precise first obstruction is the missing residual
transport-and-edge estimate
\[
 \int |C_N(t)|\,|dF_N(t)|\ll L^{-1/2}X^\varepsilon                 \tag{2}
\]
per product, or an aggregate substitute of total size
\(L^{3/2}X^\varepsilon\).  Here \(C_N\) is the ordered residual signed
divisor discrepancy and \(F_N\) is the literal zero-extended amplitude in
logarithmic divisor coordinates.  The given close-prime condition implies
no version of (2).  Therefore the outer phase must be retained, and the
first missing cross-\(N\) input is the phase-twisted residual Stieltjes
estimate stated below.  No conclusion is obtained for any other
few-point channel or downstream obligation.

## Exact statement and hypotheses

Let
\[
 \iota_p(d)={\bf1}_{p\mid d},\qquad \iota_q(d)={\bf1}_{q\mid d}.
\]
For a selected pair the residual indicator has the exact Boolean form
\[
 \rho_N(d)=(1-\iota_p(d))(1-\iota_q(d))+
             \iota_p(d)\iota_q(d)
          =1-\iota_p(d)-\iota_q(d)+2\iota_p(d)\iota_q(d).          \tag{3}
\]
Thus (3), rather than \(1-\iota_p-\iota_q\), is the formula that avoids
double subtraction: a divisor containing both selected primes has weight
one, not weight minus one.  Formula (1) follows from squarefreeness and
the restriction to odd divisors.  The factor 2, if present in \(N\), is
never a bit in the divisor lattice under consideration.

Put
\[
 t_d=\log\frac d{\sqrt N}.
\]
Let \(F_N(t)\) denote the literal amplitude in this coordinate, including
the inherited half-open cone/window convention and every dyadic support,
profile, floor, star, and endpoint convention, and extended by zero off
that literal support.  On the displayed smooth part it is
\[
 F_N(t)=
 \eta_L(\sqrt N e^t)
 \Phi\!\left(\frac{\sqrt N e^t}{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}e^t}{2}\right),                         \tag{4}
\]
multiplied by all of the just-mentioned literal indicators.  Thus
\(A_N(d)=F_N(t_d)\).  All identities below remain valid if \(A_N\) was
intended as a more detailed inherited amplitude: one simply uses its
literal zero-extension for \(F_N\).

Define the residual signed atomic measure and its right-continuous
cumulative function by
\[
 \sigma_N=\sum_{d\in\mathcal U_N}\chi_4(d)\,\delta_{t_d},\qquad
 C_N(t)=\sigma_N(({-\infty},t])
       =\sum_{\substack{d\in\mathcal U_N\\t_d\leq t}}\chi_4(d).    \tag{5}
\]
The exact physical scalar is
\[
 r_N:=\int F_N\,d\sigma_N
 =\sum_{\substack{d\mid N,\ d\ {\rm odd}}}
       \chi_4(d)\rho_N(d)A_N(d).                                  \tag{6}
\]
It is (6), not the number of selected pairs, the number of semiprimes or
multiprimes, the number of residual products, or the number of physical
incidences, that occurs in the desired sum.

The exact global sign masses are as follows.

* If a pair is selected, then
  \[
   \#\{d\in\mathcal U_N:\chi_4(d)=1\}
   =\#\{d\in\mathcal U_N:\chi_4(d)=-1\}=\tau(m).                  \tag{7}
  \]
* If no pair is selected, let \(D=\tau(n)=2^{\omega(n)}\) and
  \[
   \Delta_N=\sum_{d\mid n}\chi_4(d)
           =\prod_{\ell\mid n}(1+\chi_4(\ell)).                  \tag{8}
  \]
  Then the positive and negative masses are
  \[
   P_N=\frac{D+\Delta_N}{2},\qquad
   Q_N=\frac{D-\Delta_N}{2}.                                      \tag{9}
  \]
  Hence \(P_N=Q_N=D/2\) if at least one odd prime factor of \(n\)
  is \(3\pmod4\).  If every odd prime factor is \(1\pmod4\)
  (including the empty-product case), then \(\Delta_N=D\),
  \(P_N=D\), and \(Q_N=0\).  This is a genuine unmatched branch.

The hypotheses actually supplied are squarefreeness, oddness of the
character-bearing divisor, the deterministic at-most-one-pair rule,
opposite product character, and the logarithmic closeness of the selected
primes.  No numerical size, differentiability, bounded-variation, or
endpoint-vanishing hypotheses for \(\eta_L,\Phi,W\), or for the assembled
\(A_N\), are stated in the blind packet.  The algebraic identities here
need none.  Any numerical profile bound used in the power ledger is
therefore explicitly conditional on the usual scaled-profile bounds and
is not asserted as a consequence of the statement alone.

## Proof or derivation

For a selected pair, every odd divisor of \(N\) has exactly one of the
four selected-prime bit patterns \(00,10,01,11\).  Equation (3) keeps
exactly \(00\) and \(11\), which proves (1).  Since
\(\chi_4(pq)=-1\),
\[
 \chi_4(pqa)=-\chi_4(a),                                          \tag{10}
\]
and (7) follows.  In the no-pair branch, multiplicativity gives (8), and
adding and subtracting the unsigned divisor count gives (9).

For the exact ordered-divisor Abel identity, list the *whole* residual
universe, including the divisors where the zero-extended amplitude is
zero, as
\[
 d_1<d_2<\cdots<d_R,qquad
 \epsilon_i=\chi_4(d_i),\qquad a_i=A_N(d_i),qquad
 S_i=\sum_{j\leq i}\epsilon_j.
\]
Set \(a_{R+1}=0\).  Direct summation by parts gives
\[
 \boxed{
 r_N=\sum_{i=1}^R\epsilon_i a_i
 =\sum_{i=1}^{R-1}S_i(a_i-a_{i+1})+S_Ra_R
 =-\sum_{i=1}^R S_i(a_{i+1}-a_i).}                                \tag{11}
\]
This is the authoritative identity when a floor or star convention makes
an amplitude jump at a divisor.  It also displays the terminal endpoint
term \(S_Ra_R\).  In an equal-global-mass branch \(S_R=0\), but internal
hard jumps remain and can have nonzero \(S_i\).

If \(F_N\) is represented by a compactly supported bounded-variation
extension agreeing with the divisor values, (11) is equivalently the
Stieltjes identity
\[
 \boxed{r_N=-\int_{\mathbb R} C_N(t)\,dF_N(t).}                    \tag{12}
\]
At a common jump of \(C_N\) and \(F_N\), the side convention is the one
induced by (11); this avoids an otherwise ambiguous cross-jump term.  If
there are no common jumps and
\[
 dF_N(t)=f_N(t)\,dt+
          \sum_{b\in\mathcal B_N}\Delta_bF_N\,\delta_b+dF_N^{\rm s}(t),
\]
then
\[
 r_N=-\int C_N(t)f_N(t)\,dt
     -\sum_{b\in\mathcal B_N}C_N(b^\star)\Delta_bF_N
     -\int C_N(t)\,dF_N^{\rm s}(t).                               \tag{13}
\]
Here \(b^\star\) is fixed by (11), not chosen to improve a bound.  For
the usual logarithmic physical window \(0\leq t<\log2\), a nonzero lower
trace produces the jump
\[
 \Delta_0F_N=F_N(0+),\qquad
 \hbox{contribution }-C_N(0^\star)F_N(0+),                         \tag{14}
\]
and a nonzero upper trace produces
\[
 \Delta_{\log2}F_N=-F_N((\log2)-),\qquad
 \hbox{contribution }+C_N((\log2)^\star)F_N((\log2)-).             \tag{15}
\]
Every dyadic edge, cone edge, floor, star, or profile discontinuity is an
additional term of precisely the form in (13).  A claim that merely
bounds the smooth derivative omits (14)--(15).

Now suppose first that the global sign masses are equal, and write the
positive locations in increasing order as \(u_1<\cdots<u_M\) and the
negative locations as \(v_1<\cdots<v_M\).  The one-dimensional monotone
coupling gives the exact identity
\[
 r_N=\sum_{k=1}^M\bigl(F_N(u_k)-F_N(v_k)\bigr).                    \tag{16}
\]
For the normalized probability measures
\[
 \widehat\sigma_N^+=\frac1M\sum_{k=1}^M\delta_{u_k},\qquad
 \widehat\sigma_N^-=\frac1M\sum_{k=1}^M\delta_{v_k},
\]
the exact transport normalization is
\[
 \boxed{
 T_N:=\sum_{k=1}^M|u_k-v_k|
     =M,W_1(\widehat\sigma_N^+,\widehat\sigma_N^-)
     =\int_{\mathbb R}|C_N(t)|\,dt.}                              \tag{17}
\]
Thus omitting the factor \(M\) in front of the probability-normalized
\(W_1\) is incorrect.  If \(F_N\) were globally \(\Lambda_N\)-Lipschitz,
then (16)--(17) would give
\[
 |r_N|\leq \Lambda_NT_N.                                         \tag{18}
\]
For the actual zero-extended amplitude, the correct replacement is
\[
 |r_N|\leq
 \int |C_N(t)|\,|f_N(t)|\,dt
 +\sum_{b\in\mathcal B_N}|C_N(b^\star)|\,|\Delta_bF_N|
 +\int |C_N(t)|\,d|F_N^{\rm s}|(t).                              \tag{19}
\]
Indeed, under monotone matching, the number of matched intervals crossing
a cut \(t\) is exactly \(|C_N(t)|\).  This proves both (17) and the jump
normalization in (19).

If \(P_N\ne Q_N\), take an order-preserving partial matching of
\(\min(P_N,Q_N)\) opposite-sign points and leave
\(|P_N-Q_N|\) majority-sign points \(z_j\) unmatched.  With
\(s={\rm sgn}(P_N-Q_N)\), the exact decomposition is
\[
 r_N=\sum_{\rm matched}\bigl(F_N(u)-F_N(v)\bigr)
       +s\sum_{\rm unmatched}F_N(z_j).                            \tag{20}
\]
The last term is bounded only by
\(|P_N-Q_N|\|F_N\|_\infty\) without further information.  In the
no-pair, all-primes-\(1\pmod4\) branch, there are no negative points and
(20) is entirely unmatched.  Notice also that unequal sign mass on the
*active physical subset* is not an additional error if one uses the
full-universe, zero-extension convention of (11)--(19): it is already
encoded by the hard-edge terms.  Counting it once as active unmatched
mass and once as a boundary jump would double charge the same defect.

The odd/even complement calculation is exact and exposes another seam.
The only complement that stays among odd divisors is
\[
 d^\ast=\frac nd=\frac{N}{2^\nu d},
 \qquad
 t_{d^\ast}=-t_d-\nu\log2,                                       \tag{21}
\]
and
\[
 \chi_4(d^\ast)=\chi_4(n)\chi_4(d).                              \tag{22}
\]
It preserves the residual universe.  It reverses sign only when
\(\chi_4(n)=-1\); for a selected pair this is equivalent to
\(\chi_4(m)=1\), because \(\chi_4(n)=-\chi_4(m)\).  When \(N\) is odd,
the physical interval \(0\leq t<\log2\) is mapped to
\(-\log2<t\leq0\).  When \(N\) is even, it is mapped to
\(-2\log2<t\leq-\log2\).  Thus it does not preserve the literal
one-sided window in either branch.  Using \(N/d\) in the even branch
would instead produce an even divisor, which is not a point of the
odd-divisor signed universe.

The selected-prime condition now shows exactly why the proposed
within-product route stops.  In the deleted XOR sector,
\[
 pa\longleftrightarrow qa,
 \qquad \chi_4(pa)=-\chi_4(qa),
 \qquad |\log(qa/pa)|\leq\kappa L^{-1/2}.                         \tag{23}
\]
In the residual sector the bitwise sign-reversing pairing is instead
\[
 a\longleftrightarrow pqa,
 \qquad |\log(pqa/a)|=\log(pq).                                  \tag{24}
\]
The small number in (23) has disappeared.  A different optimal monotone
pairing might exploit the divisors of \(m\), but proving that it has small
cost, and proving that its pairs do not cross hard edges too often, are
new theorems absent from the hypotheses.

Here is the complete power ledger available from the statement.  Since
\(J=\sqrt X\),
\[
 y=J+O(1),\qquad
 \sqrt{q_X}=\frac Jy=1+O(J^{-1}),\qquad
 H=\left\lfloor\frac y{J^{1/2}}\right\rfloor
   =J^{1/2}+O(1)=X^{1/4}+O(1).                                   \tag{25}
\]
Also
\[
 N\asymp L^2,\qquad d\asymp L,\qquad
 \left(\frac{L^2}{N}\right)^{3/4}\asymp1,qquad
 \#\{N:N\asymp L^2\}\asymp L^2,                               \tag{26}
\]
and, for squarefree \(N\), all divisor multiplicities are
\(\ll_\varepsilon X^\varepsilon\), because
\(N\ll L^2\ll H^2\ll J=X^{1/2}\).  The phase has modulus one for a
within-\(N\) estimate.  Its derivatives, which matter only after the
cross-\(N\) step, have sizes
\[
 \frac d{dN}(J\sqrt N)\asymp\frac JL,
 \qquad
 \frac {d^2}{dN^2}(J\sqrt N)\asymp-\frac J{L^3}.                  \tag{27}
\]

Conditionally on the standard scaled-profile bounds
\(\|F_N\|_\infty\ll1\) and, away from hard edges,
\[
 \|\partial_tF_N\|_\infty
 \ll 1+\frac LH+O(J^{-1})\ll1,                                  \tag{28}
\]
the close-transport target would have the ledger
\[
 \underbrace{L^2}_{\text{products}}
 \underbrace{X^\varepsilon}_{\text{divisor mass}}
 \underbrace{\left(1+L/H+O(J^{-1})\right)}_{\text{log derivative}}
 \underbrace{L^{-1/2}}_{\text{transport}}
 \underbrace{1}_{\text{outer weight}}
 =L^{3/2}X^\varepsilon.                                         \tag{29}
\]
The \(L/H\) term is harmless because \(L\ll H\), and (25) restores the
full \(H,J,X\) dependence.  For the residual universe, the statement
supplies only an \(O(1)\) support-scale cost (and potentially unit hard
jumps), giving instead
\[
 L^2\,X^\varepsilon,                                             \tag{30}
\]
which misses the target by exactly \(L^{1/2}\).  Thus the phase in (27)
cannot be discarded.

The first unproved cross-\(N\) theorem can be stated without replacing
the physical scalar by a raw count.  With the exact conventions of
(5), (11), and (13), it is the uniform residual Stieltjes estimate
\[
 \boxed{
 \begin{aligned}
 &\left|\sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
 \left(
 -\int C_N(t)f_N(t)\,dt
 -\sum_{b\in\mathcal B_N}C_N(b^\star)\Delta_bF_N
 -\int C_N(t)\,dF_N^{\rm s}(t)
 \right)\right|\\
 &\hspace{7cm}\ll_\varepsilon L^{3/2}X^\varepsilon .
 \end{aligned}}                                                  \tag{XN-164}
\]
If any cone or support trace in (14)--(15) is nonzero, the hard-edge
subsum in \((\mathrm{XN\text{-}164})\) is already a necessary first
cross-\(N\) estimate; if every hard trace vanishes, the absolutely
continuous subsum is the first one.  Reindexing \(N=dk\) shows the exact
physical geometry that such a theorem must address:
\[
 k\leq d<4k,\qquad d\ \text{odd},\qquad \mu^2(dk)=1,              \tag{31}
\]
with \(k\) odd for odd \(N\) and even for even \(N\), and with the
literal summand
\[
 \chi_4(d)\rho_{dk}(d)
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}d}{2\sqrt{dk}}\right)
 e(J\sqrt{dk}).                                                   \tag{32}
\]
Thus \((\mathrm{XN\text{-}164})\) is a phase-twisted near-diagonal
divisor theorem, not a semiprime-counting assertion.  It is not proved
here and is not implied by the selected-pair rule.

## First doubtful or unproved step

The first genuinely unproved mathematical step is any assertion that the
residual monotone matching satisfies an \(L^{-1/2}\)-scale bound, including
the hard edges; concretely, one would need a bound of the shape
\[
 \int_{\operatorname{supp}(dF_N^{\rm ac})}|C_N(t)|\,dt
 +\sum_{b\in\mathcal B_N}|C_N(b^\star)|\,|\Delta_bF_N|
 \ll L^{-1/2}X^\varepsilon                                      \tag{33}
\]
after the appropriate derivative normalization.  The only available
\(L^{-1/2}\) datum is (23), and (23) concerns exactly the sector excluded
by \(\rho_N\).  Neither (24) nor the complement formulas (21)--(22)
implies (33).

There is also a statement-level limitation: the blind statement does not
give the actual regularity and trace bounds needed to turn (19) into the
numerical estimate (28).  Therefore (25)--(30) are an exact parameter
ledger with the profile contribution explicitly conditional; they are
not a certification of unstated properties of \(\eta_L,\Phi,W\).

## Required control test and outcome

All controls were exact algebraic controls; no numerical experiment was
used.

1. **Double-subtraction control.**  For bit patterns \(00,10,01,11\),
   (3) has values \(1,0,0,1\).  It therefore reproduces exactly the stated
   residual set.  The tempting \(1-\iota_p-\iota_q\) fails at \(11\),
   where it equals \(-1\).  Outcome: pass, and (3) is necessary.

2. **Constant-amplitude equal-mass control.**  On the full selected-pair
   residual universe, take \(F_N\equiv1\).  Equation (10) gives
   \(r_N=0\); (16) also gives zero term by term.  Outcome: pass.  This
   confirms the sign-mass algebra but says nothing about a truncated
   amplitude.

3. **Hard-step control.**  On any equal-mass signed universe, take
   \(F_N(t)={\bf1}_{t>b}\).  Then
   \(r_N=-C_N(b^\star)\), exactly the jump term in (13).  It need not be
   small even though the total sign mass is zero.  Outcome: pass, and it
   rules out a proof that keeps only the smooth Lipschitz cost.

4. **Selected-pair normalization control.**  With residual base
   \(m=1\), the residual points are \(1,pq\), have opposite signs, and
   their monotone cost is \(\log(pq)\).  Meanwhile the deleted points
   \(p,q\) have cost \(|\log(q/p)|\).  Outcome: pass, directly showing
   that selected-prime closeness does not transfer to the residual bit
   pattern.  The physical amplitude can vanish on the first two points;
   that does not alter the transport no-implication being tested.

5. **Unmatched-sign control.**  In the no-pair branch with every odd
   prime factor \(1\pmod4\), every divisor has sign \(+1\).  Formula
   (20) is entirely unmatched and no signed transport is available.
   Outcome: pass.

6. **Odd/even endpoint control.**  Formula (21) maps the physical log
   interval to \((-\log2,0]\) for odd \(N\), and to
   \((-2\log2,-\log2]\) for even \(N\).  Outcome: pass.  It also confirms
   that the even branch cannot use \(N/d\) while remaining in the odd
   divisor universe.

7. **Power control.**  Replacing the unavailable residual scale by the
   close scale \(L^{-1/2}\) gives (29), exactly the target.  Replacing it
   by the only unconditional support scale \(1\) gives (30), a factor
   \(L^{1/2}\) too large.  Outcome: the ledger is internally consistent
   and locates the first missing saving.

## Dependencies and exact artifacts used

Statement-only isolation is explicitly certified.  I read only:

* `protocol.md`;
* `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/blind_statement.md`.

I did not read the proof graph, active campaign, strategy, conductor seed,
any Round-164 nonblind artifact or sibling report, any Round-163 artifact,
or any earlier divisor-transport work.  I used no web source and performed
no computation.  This report is the only file written.

## Recommended state effect

Retain this as a precise obstruction/no-go result for the proposed
within-product residual transport route; do not promote the
\(L^{3/2}X^\varepsilon\) target.  Promotion would first require either a
proof of the residual transport-and-hard-edge bound (33), with the missing
profile hypotheses supplied, or a proof of the cross-\(N\) theorem
\((\mathrm{XN\text{-}164})\).  Make no change to any other channel or
downstream owner.

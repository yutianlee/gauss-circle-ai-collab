# 1. Result

The carrier algebra, the two endpoint orientations, positivity, the alternating-parity Fourier normalization, and the imprimitive lift are internally correct.  In particular, writing

\[
d_0=\kappa gU,\qquad d_1=\kappa gU+2gS,
\qquad x_0=\kappa v+2w,\qquad x_1=\kappa v,
\]

the plus carrier is \((N,N+r)=(d_0x_0,d_1x_1)\), the minus carrier is \((N,N+r)=(d_1x_1,d_0x_0)\), and in both cases the difference is exactly \(r=2\kappa gh\).  Every positive solution on either carrier occurs once in its stated \(t\)-parametrization, the two orientations are disjoint, and every Fourier mode has the unique coordinates

\[
m=(k,U),\qquad U=mq,\qquad k=ma,\qquad (a,q)=1,quad 1\leq a<q.
\]

Here and below \(Q(k,U)\) in (B188.20) is parsed as the product \(Q\,(k,U)=Qm\), not as an otherwise undefined function.

The requested split is exact:

\[
\mathscr R_{Y,Q}^{\sigma}=\mathscr R_{\geq}^{\sigma}+\mathscr R_{<}^{\sigma},
\qquad
\mathscr R_{\geq}^{\sigma}:=\mathscr R_{Y,Q}^{\sigma}[Qm\geq Y],
\quad
\mathscr R_{<}^{\sigma}:=\mathscr R_{Y,Q}^{\sigma}[Qm<Y].
\]

The second summand is the exact complement, with both orientations and all its modes retained under the one outer real part.

There are two distinct conclusions about the first sector.

* The usual coefficientwise lift estimate, with every divisor multiplicity restored, gives

  \[
  |\mathscr R_{\geq}^{\sigma}|
  \ll_{\eta}X^{2\eta}Q L^2\log ^4(2L).
  \tag{1.1}
  \]

* Completing the primitive \(a\)-sum exactly before taking absolute values improves this to

  \[
  |\mathscr R_{\geq}^{\sigma}|
  \ll_{\eta}X^{2\eta}L^2
  \left\{Q\log ^2(2L)+Q^2\log(2L)\right\}.
  \tag{1.2}
  \]

Thus, if the omitted scale relation \(L\leq X^C\) (or any stated hypothesis allowing all powers of \(\log(2L)\) to be absorbed into \(X^\varepsilon\)) is supplied, the complete first sector is target-safe:

\[
|\mathscr R_{\geq}^{\sigma}|\ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{1.3}
\]

As the packet is written, however, \(L\) and \(X\) are independent.  For fixed \(X\), neither (1.1) nor the sharper (1.2) implies (1.3), and no stated coefficient property cancels the remaining \(L\)-dependent divisor/harmonic factors.  Consequently the claimed first-sector bound, and a fortiori (B188.15), is not derivable from the self-contained hypotheses.  This is a rigorous hypothesis no-go, not a claim that the unspecified literal coefficient fails the estimate.

Even after adding the conventional scale relation, the low-gcd complement remains open: boundedness, support, squarefreeness, the factor \(\rho_N\), completion, and the single outer real part supply no \(Y\)-saving for arbitrary surviving coefficient values.

# 2. Exact statement and hypotheses

Only the hypotheses explicitly contained in the statement packet are used.  In particular, no regularity, density, distribution, translation relation, or norm bound for \(A_{L,X}^{\sigma}\) is assumed.

For a live atom put \(S=S_{t,\omega}\), \(w=w_{t,\omega}\).  The exact endpoint table is

\[
\begin{array}{c|cc}
&N&N+r\\ \hline
+&d_0x_0&d_1x_1\\
-&d_1x_1&d_0x_0 .
\end{array}
\tag{2.1}
\]

Both \(d_0\) and \(d_1\) are odd.  Nonvanishing of the displayed lambda factors imposes all the stated squarefree, divisibility, odd-divisor, literal-support, and deletion predicates separately at these endpoints.  These restrictions may delete atoms but cannot increase any bound below.

For an odd modulus \(U\), the exact Fourier identity used here is

\[
c_U(k)=\frac1U\sum_{j=0}^{U-1}(-1)^j e(-kj/U),
\qquad
(-1)^j=\sum_{k=0}^{U-1}c_U(k)e(kj/U)
\quad(0\leq j<U).
\tag{2.2}
\]

For \(m=(k,U)\), the high-packet restrictions become

\[
U=mq,\quad k=ma,\quad (a,q)=1,quad q>Q,
\quad m|a|_q>Q,
\tag{2.3}
\]

and the two sectors are respectively \(Qm\geq Y\) and \(Qm<Y\).

In lifted coordinates the exact low-gcd complement is

\[
\begin{aligned}
\mathscr R_{<}^{\sigma}
= {}&\sum_{\omega}\sum_{\substack{\mathfrak f\ {\rm as\ in}\ (\mathrm{B188.5})\\
Y<h\leq2Y,\ U>4Q}}
\sum_{\substack{mq=U,\ q>Q,\ Qm<Y}}
\frac1m
\sum_{\substack{a\ ({\rm mod}\ q),\ (a,q)=1\\m|a|_q>Q}}
c_q(a)e(\epsilon_\omega a\bar v h/q)
\sum_{t\in I_{\mathfrak f,\omega}}(-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).
\end{aligned}
\tag{2.4}
\]

The inverse \(\bar v\) in (2.4) is the reduction modulo \(q\) of the inverse modulo \(U\), hence is an inverse modulo \(q\).  The conclusion sought after controlling the first sector is exactly

\[
\Re\mathscr R_{<}^{\sigma}\ll_{B,\varepsilon}L^2X^\varepsilon,
\tag{2.5}
\]

with no absolute values inserted inside (2.4) and no separation of the two orientations.

# 3. Proof or derivation

## Carrier, endpoints, positivity, and phase

Since \((U,v)=1\), the plus congruence has the unique residue
\(S_{0,+}=[\bar vh]_U\), and

\[
vS_{t,+}-Uw_{t,+}=h.
\tag{3.1}
\]

Likewise \(S_{0,-}=[-\bar vh]_U\) and

\[
Uw_{t,-}-vS_{t,-}=h.
\tag{3.2}
\]

Conversely, every integral solution of (3.1), respectively (3.2), has
\(S=S_{0,\omega}+Ut\), and then its \(w\) is forced to be
\(w_{0,\omega}+vt\).  Thus the parametrization has multiplicity one.
Because \((U,h)=1\), neither residue \(S_{0,\omega}\) is zero; with the
least nonnegative residue convention it lies in \(\{1,\ldots,U-1\}\).
Consequently \(S_t>0\) forces \(t\geq0\).  In the minus orientation
\(w_{0,-}>0\); in the plus orientation the further condition \(w_t>0\)
merely removes an initial interval of values of \(t\).  The two orientations
cannot represent the same positive pair \((S,w)\), because their left sides
in (3.1)--(3.2) are negatives and \(h>0\).

Using (3.1),

\[
d_1x_1-d_0x_0
=(\kappa gU+2gS)\kappa v
-\kappa gU(\kappa v+2w)
=2\kappa g(vS-Uw)=2\kappa gh=r.
\tag{3.3}
\]

Using (3.2) gives \(d_0x_0-d_1x_1=r\), proving (2.1) and both
formulae (B188.9), (B188.11).  On \(I_{\mathfrak f,\omega}\), all four
factors \(d_0,d_1,x_0,x_1\) are positive, so both radicands are positive
before the phase is evaluated.  Finally,

\[
\frac r{\sqrt{N+r}+\sqrt N}=\sqrt{N+r}-\sqrt N,
\tag{3.4}
\]

so the displayed phase is exactly
\(e(\sigma\sqrt X(\sqrt{N+r}-\sqrt N))\) in both orientations.

## Parity and Fourier normalization

The finite geometric sum gives, for every \(0\leq k<U\),

\[
\frac1U\sum_{j=0}^{U-1}(-1)^je(-kj/U)
=\frac{1-(-e(-k/U))^U}{U\{1+e(-k/U)\}}
=\frac2{U\{1+e(-k/U)\}}=c_U(k),
\tag{3.5}
\]

because \(U\) is odd.  This proves (2.2).  Since both \(g\) and \(U\)
are odd,

\[
(-1)^{s_t}=(-1)^{gS_t}=(-1)^{S_t}
=(-1)^t(-1)^{S_0}
=(-1)^t\sum_{k=0}^{U-1}c_U(k)e(kS_0/U).
\tag{3.6}
\]

For the plus residue, \(e(kS_0/U)=e(k\bar vh/U)\); for the minus
residue it is \(e(-k\bar vh/U)\).  This is exactly the sign
\((-1)^t\), the two values of \(\epsilon_\omega\), and the Fourier phase
in (B188.14).  No extra factor of \(U\), \(2\), or \((-1)^{S_0}\) is
missing.

## Unique lift and coefficient norm

For \(1\leq k<U\), set \(m=(k,U)\), \(q=U/m\), and \(a=k/m\).
Then \(1\leq a<q\), \((a,q)=1\), and this representation is unique.
Conversely every factorization \(U=mq\) with \(q>1\) and every reduced
residue \(1\leq a<q\) gives exactly one such mode \(k=ma\).  Also

\[
|k|_U=m|a|_q,
\quad
c_U(ma)=\frac1m c_q(a),
\quad
e(\epsilon_\omega ma\bar vh/(mq))
=e(\epsilon_\omega a\bar vh/q),
\tag{3.7}
\]

which verifies (B188.17), including phase and multiplicity one.

Moreover

\[
|c_q(a)|=\frac1{q|\cos(\pi a/q)|}.
\tag{3.8}
\]

Writing \(j=|q-2a|\) and using
\(\sin x\geq2x/\pi\) on \([0,\pi/2]\) gives
\(|c_q(a)|\leq 1/j\), up to an absolute endpoint constant.  Summing
the two possible residues for each odd \(j\) proves

\[
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
\ll\log(2q).
\tag{3.9}
\]

## Endpoint multiplicity

At fixed \((\kappa,u,U,h)\), the value \(g=u/U\) is fixed.  A live
endpoint has \(\kappa v\asymp L\), hence there are \(O(L/\kappa)\)
possible positive integers \(v\).  The other divisor endpoint is

\[
d_1=\kappa u+2g(S_0+Ut)=\kappa u+2gS_0+2ut.
\tag{3.10}
\]

Since \(d_1\ll L\) and \(u\asymp L/\kappa\), positivity gives
\(0\leq t\ll\kappa\).  Thus each orientation has at most
\(O((L/\kappa)\kappa)=O(L)\) live \((v,t)\)-atoms.  Coprimality,
squarefreeness, strict cones, and \(w_t>0\) only delete possibilities.
There are \(O(Y)\) integers \(h\) in the dyadic block, so the two
orientations together have \(O(YL)\) atoms at fixed
\((\kappa,u,U)\).  This is an endpoint count, not a density or
nonemptiness assertion.

This proves multiplicity one for the stated solution coordinates and the
claimed upper multiplicity.  A stronger assertion that the same numerical
endpoint cannot arise from two different outer labels is not encoded by
the packet: no reverse definition of \(\kappa,g,h,U,v\) from an original
atom is supplied.

## The exact split and the first-sector divisor power

The two indicators \(\mathbf1_{Qm\geq Y}\) and
\(\mathbf1_{Qm<Y}\) partition every mode.  After (3.7), they give (2.4)
and the analogous formula with \(Qm\geq Y\).  This proves exactness of
the complement without moving the real part.

For a selected pair in (B188.2), squarefreeness and \(d\mid N\) show

\[
\rho_N(d)=
\begin{cases}
1,&d\text{ contains neither or both selected primes},\\
0,&d\text{ contains exactly one selected prime}.
\end{cases}
\tag{3.11}
\]

Hence \(|\rho_N(d)|\leq1\).  Since \(0<r<R_0\), (B188.3) gives

\[
|B_{\mathfrak f,\omega}^{\sigma}(t)|\ll_\eta X^{2\eta}.
\tag{3.12}
\]

At fixed \(U\), the coefficientwise mass of the first sector is at most

\[
\begin{aligned}
W_{\geq}(U)
&\leq
\sum_{\substack{mq=U,\ q>Q,\ Qm\geq Y}}
\frac1m
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|\\
&\ll \log(2U)
\sum_{\substack{mq=U\\m\geq Y/Q}}\frac1m.
\end{aligned}
\tag{3.13}
\]

Now \(U\mid u\).  Therefore

\[
\begin{aligned}
\sum_{U\mid u}W_{\geq}(U)
&\ll \frac QY\log(2u)
\#\{(m,q):mq\mid u\}\\
&=\frac QY\log(2u)d_3(u).
\end{aligned}
\tag{3.14}
\]

The equality displays the exact divisor multiplicity: a pair \((m,q)\)
is completed by the third ordered factor \(u/(mq)\), so it is \(d_3(u)\),
not one divisor and not a density-one choice.

An elementary triple-divisor summation gives
\(\sum_{n\leq T}d_3(n)\ll T\log^2(2T)\).  A live block has
\(\kappa\ll L/Y\) from \(2\kappa gh<R_0\), and
\(u\asymp L/\kappa\).  Consequently

\[
\sum_{\kappa}\sum_{u\asymp L/\kappa}d_3(u)\log(2u)
\ll L\log^4(2L).
\tag{3.15}
\]

Multiplying (3.14)--(3.15) by the \(O(YL)\) endpoint multiplicity and
(3.12) proves (1.1).

There is a useful exact completion which shows that the obstruction is
not merely the crude \(L^1\) estimate (3.9).  For \((n,q)=1\), Mobius
inversion in the frequency variable gives

\[
F_q(n):=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
c_q(a)e(an/q)
=\sum_{d\mid q}\frac{\mu(d)}d(-1)^{[n]_{q/d}},
\qquad |F_q(n)|\leq\sigma_{-1}(q).
\tag{3.16}
\]

Indeed, the sum over frequencies divisible by \(d\) equals
\(d^{-1}(-1)^{[n]_{q/d}}\) by (2.2).  Since \(U>4Q\), every frequency
removed by \(m|a|_q\leq Q\) lies in \(|a|_q<q/4\); there
\(|c_q(a)|\ll q^{-1}\).  Thus the complete high-gcd Fourier kernel obeys

\[
|K_{\geq}(U;n)|
\ll
\sum_{\substack{mq=U\\m\geq Y/Q}}
\left\{\frac{\sigma_{-1}(q)}m+\frac{Q}{m^2q}\right\}.
\tag{3.17}
\]

For \(T=L/\kappa\) and \(M=Y/Q\), summing (3.17) over
\(u\asymp T\) and \(U\mid u\) is the same as summing over
\(u=bmq\).  The elementary estimates

\[
\sum_{q\leq Z}\sigma_{-1}(q)\ll Z,
\qquad
\sum_{q\leq Z}\frac{\sigma_{-1}(q)}q\ll\log(2Z)
\tag{3.18}
\]

then give

\[
\sum_{u\asymp T}\sum_{U\mid u}|K_{\geq}(U;n)|
\ll \frac{T}{M}\{\log(2T)+Q\}.
\tag{3.19}
\]

Finally, summing \(O(YL)\) atoms for each \((\kappa,u,U)\) and
\(\sum_{\kappa\ll L/Y}\kappa^{-1}\ll\log(2L)\) proves (1.2).

Since \(Q=(\log(2X))^B+O(1)\), all powers of \(Q\) can be absorbed by
retuning \(\eta\) in (3.12).  Powers of \(\log(2L)\) cannot be so
absorbed when \(L\) is independent of \(X\).  This is the precise missing
hypothesis in the claimed first-sector conclusion.

## Why the low sector does not follow

The inner \(t\)-sequence has no stated regularity.  In fact, in either
orientation

\[
N_{t+1}-N_t=2\kappa gUv.
\tag{3.20}
\]

Also no head of one edge is a tail of another edge on the same carrier:
an equality \(N_t+r=N_{t+j}\) would require \(Uvj=h\), impossible for
\(j\in\mathbb Z\) because \((U,h)=1\) and \(U>1\).  Hence, on any
surviving carrier, the endpoint coefficient values occurring at different
\(t\)'s are independent as far as the packet's hypotheses are concerned.
One may assign bounded phases at these disjoint endpoints so that
\((-1)^tB(t)\), including the square-root phase, has one common argument.
Thus the alternating sign supplies no arbitrary-weight cancellation.

The same observation applies after multiplying by a nonzero completed
Fourier kernel.  Reciprocity or determinant transposition merely rewrites
its phase; opening \(\mu^2\) or \(\rho_N\) merely introduces arithmetic
restrictions.  None creates a relation among the literal coefficient
values.  Therefore none of these operations proves (2.5) from the stated
hypotheses.

A concrete sufficient new actual-coefficient input would be a full
\(Y\)-saving reciprocal-frequency correlation estimate.  For example,
with \(g=u/U\), define

\[
\mathcal C_{\kappa,u,U}(a/q)
:=\sum_{\omega\in\{+,-\}}
\sum_{\substack{Y<h\leq2Y\\(U,h)=1}}
\sum_{\substack{v,t\ {\rm live}\text{ for }(\kappa,g,h,U,v,\omega)}}
e(\epsilon_\omega a\bar vh/q)(-1)^t
B_{\mathfrak f,\omega}^{\sigma}(t).
\tag{3.21}
\]

The trivial bound is \(O(YLX^\varepsilon)\) at fixed
\((\kappa,u,U)\).  A proved bound of size
\(O(LX^\varepsilon)\), uniformly (or in the exact weighted average over
the low-gcd \((m,q,a)\)'s in (2.4)), would be the first genuine
actual-coefficient relation with the required factor \(Y\).  It must be
proved for the literal \(A_{L,X}^{\sigma}\); it cannot be replaced by a
positive-energy estimate or an arbitrary bounded-weight theorem.

# 4. First doubtful or unproved step

The first unproved step in the requested first-sector claim is the silent
absorption of \(d_3(u)\), the primitive-frequency harmonic mass, and the
\(\kappa\)-harmonic summation into \(X^\varepsilon\).  The packet supplies
no upper relation between \(L\) and \(X\).  Equations (1.1) and (1.2)
are valid uniformly; deleting their \(\log(2L)\) factors is not.

If a conventional relation such as \(L\leq X^C\) is added, the first
remaining unproved step toward (B188.15) is a factor-\(Y\) signed
correlation estimate for the exact literal coefficient in the low-gcd
sum (2.4), such as (3.21).  No such relation is present.

Separately, only internal carrier multiplicity can be verified from the
packet.  Global multiplicity one relative to an unspecified original
residual, and agreement with the named shell/profile/floor/star/endpoint
predicates, require the missing reverse connector and predicate
definitions.

# 5. Required control test and outcome

1. **Small carrier.**  Take \(U=5,v=1,h=2\).  Then
   \(S_{0,+}=2,w_{0,+}=0\), so the first positive plus solution is
   \((S,w)=(7,1)\); with \(\kappa=g=1\), it gives
   \((N,N+r)=(15,19)\).  In the minus orientation
   \(S_{0,-}=3,w_{0,-}=1\), and \(t=0\) gives
   \((N,N+r)=(11,15)\).  Both differences are \(r=4\), and the parity
   changes exactly by \((-1)^t\).  This checks the algebra only; a literal
   support predicate may delete either example.

2. **Near-half modes.**  For odd \(q\) and
   \(a=(q\pm1)/2\),
   \[
   |c_q(a)|=\{q\sin(\pi/(2q))\}^{-1}\longrightarrow 2/\pi.
   \]
   Hence the lifted coefficient has size asymptotic to
   \(2/(\pi m)\), not \(1/(mq)\).  These modes satisfy the
   \(|k|_U>Q\) cut when \(U>4Q\).  The factor \(1/m\) is therefore the
   sharp generic lift gain.

3. **Prime conductor.**  If \(q=p\) is an odd prime and \((n,p)=1\),
   (2.2) gives the exact complete primitive sum
   \[
   \sum_{a=1}^{p-1}c_p(a)e(an/p)=(-1)^{[n]_p}-1/p.
   \]
   Its magnitude is at least \(1-1/p\).  Thus primitive completion alone
   has no conductor saving, even in the cleanest case.

4. **Arithmetic deletion.**  If a pair \(\{p_N,q_N\}\) is selected,
   direct substitution in (B188.2) gives \(1,0,0,1\) according as
   \(d\) contains neither, only \(p_N\), only \(q_N\), or both.  The
   deletion factor has no negative values and supplies no cancellation.

5. **Endpoint change.**  Replacing \(t\) by \(t+1\) changes
   \(S\) by \(U\), \(w\) by \(v\), both \(N\)'s by
   \(2\kappa gUv\), and the parity by a minus sign.  The hard literal
   predicates and coefficient values may change discontinuously, so no
   summation-by-parts estimate follows.

6. **Terminal block.**  Since \(h>Y\) and
   \(2\kappa gh<R_0\), a nonempty block forces
   \(\kappa g<R_0/(2Y)\).  At the terminal boundary the number of
   admissible \(h\)'s can only decrease; it does not justify averaging a
   block as though all \(O(Y)\) values were present.

7. **Adversarial bounded array.**  On any collection of disjoint
   surviving endpoint edges, assign unit-modulus coefficient phases so
   that the factor \((-1)^t\), the square-root phase, and a chosen nonzero
   Fourier kernel are cancelled.  Every real contribution then has the
   same sign and equals its absolute capacity.  Equation (3.20) and
   \((U,h)=1\) make this construction independent along a single
   carrier.  This falsifies any proposed cancellation theorem whose only
   coefficient hypothesis is boundedness.  It does not assert that the
   fixed, but unspecified, literal coefficient actually has these phases.

All controls pass the algebraic normalization and fail to reveal any
unstated source of the required \(Y\)-saving.

# 6. Dependencies and exact artifacts used

Exactly the following two artifacts were read and used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/blind_statement.md`.

No proof graph, state file, strategy, prior round, sibling report, source,
code, web search, or numerical computation was used.

# 7. Recommended state effect

**Revise.**  Retain the internally verified carrier/Fourier/lift algebra,
the exact split, the divisor multiplicity \(d_3(u)\), and the exact
low-gcd complement (2.4).  Do not promote (B188.15), and do not promote
the requested first-sector target bound from this packet alone.  Either
add an explicit scale hypothesis allowing \(\log L\) to be absorbed into
\(X^\varepsilon\), or record the logarithmic first-sector bounds
(1.1)--(1.2).  After that repair, require a proved actual-coefficient
correlation such as (3.21) before changing the low-gcd or parent proof
state.

# Round 84 analytic report: stationary dual-difference attack

Campaign: `m9-m1-centred-dual-difference-stationary-correlation`  
Task: `stationary_dual_difference_attack`  
Role: discovery  
Starting graph SHA-256: `b744aa885442ec9be13913782471cf65a94cd794579f8c6a8fbb2854ce52e271`

## 1. Result

There is a genuine, target-safe nonzero-difference deletion, although no
fixed power of \(B=C/T\) is proved for the whole centred correlation.
Put

\[
 D_0=\left\lfloor J^{17/30}\right\rfloor
\]

and let \(\mathfrak Y_{\leq D}\) denote (84.9) with the additional
restriction \(0<|d|\leq D\).  Uniformly for all three local classes,
both endpoint orientations, and \(1\leq D\leq D_0\),

\[
 \boxed{
 |\mathfrak Y_{\leq D}^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon\left(
 C^3J^{-17/10}D^{3/2}
 +C^2T J^{-3/2}D^{1/2}
 +{DC^2\over T\sqrt{JQ}}
 +{DB^2\over Q^2}
 \right).}                                                \tag{1.1}
\]

At \(C\leq J^{3/4}\) and \(D=D_0\), the four powers of \(J\) on the
right are at most, respectively,

\[
 J^{7/5},\qquad J^{53/60},\qquad J^{23/30},\qquad
 J^{1/15}.
\]

Since \(J^2/T=J^{7/5}\), the complete family

\[
 0<|d|\leq \lfloor J^{17/30}\rfloor                    \tag{1.2}
\]

is therefore target-safe.  This includes negative differences, every
nonzero multiple of \(M\in\{4b,2b,b\}\) in this range, all Ramanujan
terms, and every prime-power gcd degeneration.  The exact smaller
survivor is

\[
 \boxed{
 \mathfrak Y_{>D_0}^{(\kappa,k)}
 =\sum_{b\asymp B}{1\over M_{\kappa,b}^2}
 \sum_{|d|>D_0}\sum_{n\in\mathbb Z}
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)},}                              \tag{1.3}
\]

where \(M=M_{\kappa,b}\) inside the \(b\)-sum.  Equation (1.3) is an
exact subtraction from (84.9), not a stationary truncation.

The analytic input behind (1.1) is a uniform all-class stationary
normal form.  For orientation \(\eta\in\{1,-1\}\), write

\[
 F_{b,\eta}(x)=V_{b,gx,k}^{(\kappa)}
 e\!\left(-\eta {A_{\kappa,b}\over gx}\right),\qquad
 I_{b,\eta}(n)=\int F_{b,\eta}(x)e\!\left(-{nx\over M}\right)dx.
\]

For \(\eta=-1\), \(V\) in this notation means the conjugated/reflected
principal coefficient furnished by the opposite endpoint orientation;
it has the same support and BV bounds.

The stationary sign is \(\eta n>0\).  If \(m=\eta n>0\), then

\[
 x_{b,m}=\sqrt{{A_{\kappa,b}M\over gm}},\qquad
 c_{b,m}=gx_{b,m}=\sqrt{{A_{\kappa,b}gM\over m}},          \tag{1.4}
\]

\[
 \Delta_{b,m}=\sqrt{{Mx_{b,m}\over2m}}
 ={A_{\kappa,b}^{1/4}M^{3/4}\over
   \sqrt2\,g^{1/4}m^{3/4}},                               \tag{1.5}
\]

and

\[
 I_{b,\eta}(\eta m)
 =e\!\left(-\eta\lambda_b\sqrt m\right)
 \mathcal P_{b,\eta}(m),
 \qquad
 \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b}.             \tag{1.6}
\]

In the stationary interior,

\[
 \mathcal P_{b,\eta}(m)
 =e(-\eta/8)\Delta_{b,m}V_{b,c_{b,m},k}^{(\kappa)}
 +\text{summably smaller terms}.                          \tag{1.7}
\]

At saddle entry and exit, \(e(-\eta/8)\) in (1.7) is replaced by the
exact oriented incomplete Gaussian displayed in Section 3.  Its full
limit is exactly \(e(-\eta/8)\), and its boundary value is the oriented
half Gaussian.  On each progression \(m=r+M\ell\), the exact
phase-removed truncated-Gaussian main profile has

\[
 \|\mathcal W_{b,\eta}\|_\infty+
 \operatorname {Var}_{\ell}\mathcal W_{b,\eta}
 \ll_\varepsilon X^\varepsilon H,\qquad
 H={C\sqrt T\over J}.                                    \tag{1.8}
\]

The aggregate entry/exit, Gaussian-tail, stationary-remainder, and
wrong-sign terms are the last two terms of (1.1).  Thus (1.1) does not
silently discard a saddle collar or a Fourier tail.

## 2. Exact statement and hypotheses

Assume

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5}={J\over Q},
 \qquad B={C\over T},
\]

and

\[
 J^{13/18}<C\leq J^{3/4}.                                \tag{2.1}
\]

Fix one transition-flattened smooth-interior nonaxial principal
component, one alias, a compatible pair with \(k=\rho\sigma>0\), and
one endpoint orientation.  The reflected orientation is represented by
\(\eta=-1\).  For

\[
 \kappa\in\{1/4,1/2,1\},\qquad g=4\kappa,
 \qquad M={4b\over g},
\]

the exact local units are

\[
 u_{\kappa,b,k}(gx)=\zeta_{\kappa,b,k}e_M(K\bar x),
 \qquad
\begin{array}{c|c|c|c}
\kappa&g&M&K\\ \hline
1/4&1&4b&k\\
1/2&2&2b&2[k\bar4]_b\\
1&4&b&[k\bar4]_b.
\end{array}                                               \tag{2.2}
\]

In particular \(gM=4b\) in every row.  The reciprocal phase is

\[
 A=A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2.             \tag{2.3}
\]

The symbol in this report is only Round 81's neighbor-independent
principal coefficient \(V=g_c(0)\), with

\[
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V
 \ll_\varepsilon X^\varepsilon.                          \tag{2.4}
\]

Round 81's pointwise transition remainder, also denoted \(E(c)\) in
that round, is not included in \(F_{b,\eta}\) or \(I_{b,\eta}\).  It
retains its separate accepted owner.  The conductor-authorized exact
integral extension (81.A2)--(81.A3) is used only to justify the
Morse-variable stationary remainders and sampled variation; it is not
used to import an arbitrary new \(c\)-derivative seminorm.

Let

\[
 \mathcal K_{b,d}(n)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).                   \tag{2.5}
\]

Then

\[
 \mathfrak Y_{\leq D}^{(\kappa,k)}
 =\sum_{b\asymp B}{1\over M^2}
 \sum_{0<|d|\leq D}\sum_{n\in\mathbb Z}
 \mathcal K_{b,d}(n)I_b(n+d)\overline{I_b(n)}.           \tag{2.6}
\]

The conclusion is (1.1).  More generally, its first term is target-safe
for \(D\leq J^{31/15}C^{-2}\); (1.2) is the largest simple
\(C\)-independent range furnished by this calculation over the whole
band (2.1).

This lemma is not coefficient-uniform in the Fourier variable.  It uses
the exact reciprocal Fourier transform through (1.6)--(1.8).  It is,
however, uniform in the actual residue coefficient (2.5), because the
only arithmetic norm used is the exact complete Kloosterman Parseval
identity.  No pointwise Weil bound is needed.

## 3. Proof or derivation

### Exact saddle, phase, Gaussian, and amplitude

It suffices first to take \(\eta=1\), so \(n=m>0\).  The phase is

\[
 \Phi_m(x)=-{A\over gx}-{mx\over M}.
\]

Its sole positive critical point is (1.4).  Since

\[
 {A\over g}={m x_{b,m}^2\over M},
\]

one has the exact quadratic identity

\[
 \Phi_m(x)-\Phi_m(x_{b,m})
 =-{m\over M}{(x-x_{b,m})^2\over x}.                     \tag{3.1}
\]

Thus the exact Morse coordinate

\[
 t=t_m(x)=\sqrt{{2m\over Mx}}(x-x_{b,m})                 \tag{3.2}
\]

is strictly increasing for \(x>0\) and gives

\[
 \Phi_m(x)=\Phi_m(x_{b,m})-{t^2\over2},\qquad
 \left.{dx\over dt}\right|_{t=0}=\Delta_{b,m}.          \tag{3.3}
\]

Also

\[
 \Phi_m(x_{b,m})=-2\sqrt{{Am\over gM}}
 =-\left(\sqrt X+{\sqrt{\kappa k}\over b}\right)\sqrt m.
                                                                  \tag{3.4}
\]

The last equality uses \(gM=4b\) and (2.3), so it is exact in all
three classes, not merely an asymptotic replacement of \(A\).

Suppose one connected exact support chart in \(x\) has endpoints
\(x_-<x_+\).  Put

\[
 \tau_\pm(m)=\sqrt{{2m\over Mx_\pm}}(x_\pm-x_{b,m}),
 \qquad
 \mathcal G_\eta(u,v)=\int_u^v e(-\eta t^2/2)\,dt.       \tag{3.5}
\]

Changing variables by (3.2), and using the neighbor-independent smooth
extension supplied by (81.A2)--(81.A3), gives the uniform chart formula

\[
 I_{b,\eta}(\eta m)
 =e(-\eta\lambda_b\sqrt m)
 \left\{
 \Delta_{b,m}\widetilde V_b(c_{b,m})
 \mathcal G_\eta(\tau_-(m),\tau_+(m))
 +\mathcal R_{b,\eta}(m)
 \right\}.                                               \tag{3.6}
\]

Here \(\widetilde V_b\) is the one-sided smooth extension of the
principal \(V\) on this fixed chart; it is not Round 81's transition
remainder.  Summing the fixed number of charts gives the complete
formula.  The exact full and half Gaussian constants are

\[
 \mathcal G_\eta(-\infty,\infty)=e(-\eta/8),\qquad
 \mathcal G_\eta(-\infty,0)
 =\mathcal G_\eta(0,\infty)={1\over2}e(-\eta/8).          \tag{3.7}
\]

For \(\eta=-1\), the stationary Fourier index is \(n=-m\), (3.1) has
the opposite sign, and (3.6)--(3.7) are conjugated.  This proves the
stationary sign and Gaussian in both orientations.

The exact stationary support is

\[
 \mathscr N_b
 =\left\{m>0:c_{b,m}=\sqrt{AgM/m}
 \text{ lies in the exact \(c\)-support of }V\right\}.    \tag{3.8}
\]

Its endpoints are \(AgM/c_\pm^2\), with the inherited half-open
convention, and

\[
 m\asymp {AgM\over C^2}\asymp Q^2.                      \tag{3.9}
\]

Writing \(\Lambda_b=A/C\), one has uniformly

\[
 \Lambda_b\asymp JQ,\qquad
 \Delta_{b,m}\asymp {C\over\sqrt{JQ}}
 ={C\sqrt T\over J}=H.                                  \tag{3.10}
\]

Thus (1.5), rather than a guessed \((C,Q,B)\) monomial, is the exact
stationary amplitude.

### Why (81.A2)--(81.A3) give the required sampled profile control

The delicate point is that only the principal \(V\) has accepted global
BV; the discarded Farey transition does not.  Formula (3.6) uses the
actual principal extension.  In the Morse variable, write the normalized
amplitude as

\[
 G_{b,m}(t)
 =V_{b,gx(t),k}^{(\kappa)}{dx/dt\over\Delta_{b,m}}.
\]

At \(t=0\), \(G_{b,m}(0)=V(c_{b,m})\).  The bounds (81.A2) control the
fixed \(t\)-derivatives after the exact first stationary reduction, while
(81.A3), evaluated at that critical point, gives

\[
 \|V\|_\infty+\int_C^{2C}|dV(c)|
 \ll_\varepsilon X^\varepsilon.                          \tag{3.11}
\]

No supremum for \(V'(c)\) is inserted.  Instead, use the monotone saddle
map

\[
 m={AgM\over c_{b,m}^2},\qquad
 {dc_{b,m}\over dm}=-{c_{b,m}\over2m}.                   \tag{3.12}
\]

The Morse width in \(c\) is \(C/\sqrt{\Lambda_b}\).  Consecutive samples
on one progression \(m=r+M\ell\) move the saddle by
\(\asymp CM/Q^2\).  Hence a fixed point of the \(c\)-support belongs to
at most

\[
 \ll 1+{Q^2\over M\sqrt{\Lambda_b}}                     \tag{3.13}
\]

sampled Morse neighborhoods.  Fubini applied to (3.11) therefore gives
the summed local-amplitude error

\[
 \sup_{r\bmod M}
 \sum_{\substack{m\equiv r\ (M)\\m\asymp Q^2}}
 |\mathcal R_{b,\eta}(m)|
 \ll_\varepsilon X^\varepsilon
 {H Q^2\over M\sqrt{\Lambda_b}}.                        \tag{3.14}
\]

This is the promised derivation from an integrated \(c\)-seminorm; it
does not assume a pointwise derivative not present in the packet.

For an endpoint \(x_e\), (3.5) and (3.12) give

\[
 |\tau_e(m+M)-\tau_e(m)|\asymp {M\sqrt{\Lambda_b}\over Q^2}
\]

while the saddle crosses the entry/exit collar.  Split the incomplete
Gaussian into a truncated transition, equal to the exact
\(\mathcal G_\eta\) for \(|\tau_e|\leq2\) and to its zero or full limit
outside \(|\tau_e|\geq3\), plus its oscillatory tail.  The truncated
transition has total variation \(O(1)\) and is traversed once at each
fixed support edge.  Integration by parts in \(t\) gives

\[
 \mathcal G_\eta-\mathcal G_\eta^{\rm tr}
 \ll {1\over1+|\tau_e|}.
\]

Sampling this last bound along \(m=r+M\ell\) costs

\[
 \ll {Q^2\over M\sqrt{\Lambda_b}}\log(2\Lambda_b),       \tag{3.15}
\]

which is absorbed in \(X^\varepsilon\).  Equations (3.11)--(3.15), the
variation of the explicit factor \(\Delta_{b,m}\), and the finite number
of support charts prove

\[
 \|\mathcal W_{b,\eta}\|_\infty+
 \sum_\ell|\mathcal W_{b,\eta}(r+M(\ell+1))
             -\mathcal W_{b,\eta}(r+M\ell)|
 \ll_\varepsilon X^\varepsilon H.                       \tag{3.16}
\]

Here \(\mathcal W\) is the exact phase-removed truncated-Gaussian
profile: it contains the full interior Gaussian and the exact one-pass
entry/exit transition.  The difference between \(\mathcal P\) and
\(\mathcal W\), including the Gaussian tails and (3.14), satisfies the
sampled product estimate

\[
 \sup_{r,d}
 \sum_{m\equiv r\ (M)}
 \left|
 \mathcal P(m+d)\overline{\mathcal P(m)}
 -\mathcal W(m+d)\overline{\mathcal W(m)}
 \right|
 \ll_\varepsilon X^\varepsilon
 {H^2Q^2\over M\sqrt{\Lambda_b}},                        \tag{3.17}
\]

uniformly for \(|d|\leq D_0=o(Q^2)\).  Shifted support entry and exit
are included because (3.15) is applied to both \(m\) and \(m+d\).

For the wrong stationary sign, or outside a fixed enlargement of
\(\mathscr N_b\), the first-derivative lemma and (2.4) give

\[
 |I_{b,\eta}(n)|
 \ll_\varepsilon X^\varepsilon {M\over Q^2+|n|}          \tag{3.18}
\]

in the wrong-sign range, with the analogous distance-to-
\(\mathscr N_b\) bound on the same-sign exterior.  Since
\(|d|=o(Q^2)\), the product of the two tails is square-summable on every
progression and contributes at most

\[
 \ll_\varepsilon X^\varepsilon {M\over Q^2}              \tag{3.19}
\]

per progression.  This owns negative-frequency tails and the cases in
which \(n\) and \(n+d\) have different signs.  Equations (3.14),
(3.15), and (3.19) are the aggregate stationary-error ledger.

### Exact arithmetic coefficient mass

The coefficient in (2.5) is constant on \(n=r+M\ell\).  Complete
orthogonality, with no hypothesis on \(K\), gives

\[
 \sum_{r\bmod M}|S(r,K;M)|^2=M\varphi(M).                \tag{3.20}
\]

Therefore Cauchy--Schwarz and the trivial exact Ramanujan bound give,
for every integer \(d\),

\[
 \begin{aligned}
 {1\over M^2}\sum_{r\bmod M}|\mathcal K_{b,d}(r)|
 &\leq {1\over M^2}
 \left(\sum_r|S(r+d,K;M)|^2\right)^{1/2}
 \left(\sum_r|S(r,K;M)|^2\right)^{1/2}
 +{|c_M(d)|\over M}\\
 &\leq {\varphi(M)\over M}+1\leq2.                     \tag{3.21}
 \end{aligned}
\]

This retains the Ramanujan subtraction rather than estimating it in a
different object.  It also treats prime powers and \(d\equiv0\pmod M\):
when \(M\mid d\), \(c_M(d)=\varphi(M)\), still within (3.21).  Thus no
pointwise square-root estimate, and no false coefficient-free rational-
sum bound, enters the proof.

### Difference curvature on \(n=r+M\ell\)

In the stationary same-sign bulk, the Gaussian units cancel between the
two factors and the exact phase is

\[
 \Psi_{b,d}(n)=-\lambda_b(\sqrt{n+d}-\sqrt n).            \tag{3.22}
\]

For negative \(d\), use the same formula on \(n+d>0\), or reindex by
the smaller Fourier argument; all estimates below depend on \(|d|\).
Along \(n=r+M\ell\),

\[
 \Psi_{b,d}''(\ell)
 ={M^2\lambda_b\over4}
 \bigl((n+d)^{-3/2}-n^{-3/2}\bigr).                      \tag{3.23}
\]

Since \(0<|d|\leq D_0=o(Q^2)\), \(n,n+d\asymp Q^2\), and
\(\lambda_b\asymp J\), the mean-value theorem gives a constant sign and

\[
 |\Psi_{b,d}''(\ell)|\asymp {M^2J|d|\over Q^5}
 ={M^2|d|\over J}.                                      \tag{3.24}
\]

The exact first derivative may equal an integer, and it may cross many
integers over the progression.  The weighted second-derivative lemma is
uniform at every such crossing: for an interval of length
\(L_\ell\ll Q^2/M\) and a weight of supremum plus variation
\(O(X^\varepsilon H^2)\), (3.16) and (3.24) give

\[
 \begin{aligned}
 \left|\sum_\ell w_{b,d,r}(\ell)e(\Psi_{b,d}(r+M\ell))\right|
 &\ll_\varepsilon X^\varepsilon H^2
 \left({Q^2\over M}\sqrt{{M^2J|d|\over Q^5}}
       +\sqrt{{Q^5\over M^2J|d|}}\right)\\
 &\ll_\varepsilon X^\varepsilon H^2
 \left(J^{3/10}|d|^{1/2}
       +{J^{1/2}\over M|d|^{1/2}}\right).                \tag{3.25}
 \end{aligned}
\]

Thus perfect-square or fourth-power choices of \((X,n,d)\) do not create
a missing case: for \(d\ne0\), the exact curvature (3.23) never vanishes.
The second-derivative estimate, not an irrationality assumption on the
first derivative, controls their integer resonances.

Multiply (3.25) by the normalized residue mass (3.21).  Summing over
the \(O(B)\) values of \(b\), using \(M\asymp B\), and then summing
\(1\leq|d|\leq D\), gives

\[
 \begin{aligned}
 &\ll_\varepsilon X^\varepsilon
 B H^2J^{3/10}D^{3/2}
 +X^\varepsilon H^2J^{1/2}D^{1/2}\\
 &=X^\varepsilon
 \left(C^3J^{-17/10}D^{3/2}
 +C^2T J^{-3/2}D^{1/2}\right),                           \tag{3.26}
 \end{aligned}
\]

because \(H^2=C^2T/J^2\) and \(B=C/T\).

Finally, (3.17), (3.21), and \(\sum_{b\asymp B}M^{-1}\asymp1\)
give

\[
 \ll_\varepsilon X^\varepsilon {DC^2\over T\sqrt{JQ}}  \tag{3.27}
\]

for all incomplete-Gaussian tails and stationary remainders.  The far
tails (3.19) give

\[
 \ll_\varepsilon X^\varepsilon {DB^2\over Q^2}.         \tag{3.28}
\]

Equations (3.26)--(3.28) prove (1.1).

No completion or inverse transform is counted as a saving here.  The
only saving step is the genuine estimate (3.25) for the actual
square-root difference phase after its exact residue-periodic arithmetic
coefficient has been isolated.

## 4. First doubtful or unproved step

The first unproved inequality needed after this report is a signed bound
for the exact survivor (1.3).  In particular, the second-derivative
estimate summed absolutely in \(d\) has first-term capacity

\[
 C^3J^{-17/10}D^{3/2}.
\]

At \(C=J^{3/4}\) it reaches the target exactly at
\(D=J^{17/30}\) and exceeds it beyond that point.  The mesoscopic range

\[
 J^{17/30}<|d|\ll Q^2,
\]

the support-difference edges \(|d|\asymp Q^2\), and all still larger
integer differences therefore remain in (1.3).  The available first
derivative tail bound is enough for the aggregate errors attached to a
fixed small-\(d\) family, but it is not used to delete the infinite
large-\(d\) family absolutely.  Doing so from only the frozen BV input
would be an unjustified extra smoothness assumption.

The first seam inside the proved lemma that deserves independent review
is (3.14): transfer of the integrated \(c\)-seminorm (81.A3) through the
monotone saddle map.  The overlap count (3.13) is what prevents a hidden
pointwise \(V'(c)\) assumption.  If that overlap calculation were
invalid, the stationary-remainder term (3.27), rather than the curvature
bound (3.25), would be the first affected line.

No whole-range \(B^{-\delta}\) gain follows.  Closing (1.3) appears to
require cancellation across different \(d\), moduli, or residue rows,
not a repetition of the one-progression second-derivative estimate.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| External normalization | **Pass.**  The exact \(M^{-2}\) is retained in (2.6).  At \(D_0\), the leading term in (1.1) is \(J^{7/5}=J^2/T\) only at \(C=J^{3/4}\); every other displayed term is smaller. |
| All-class local units | **Pass.**  The three exact \((g,M,K)\) rows are displayed in (2.2).  The stationary algebra uses only the common exact identity \(gM=4b\). |
| Poisson measure | **Pass.**  No factor of \(M\) is introduced after Round 83.  The normalized residue mass is (3.21), and \(\sum_{b\asymp B}M^{-1}\asymp1\) is used only for the summed stationary error. |
| Stationary sign, phase, and Gaussian | **Pass.**  Equations (3.1)--(3.7) give the exact Morse coordinate, phase \(-\eta\lambda_b\sqrt{|n|}\), full Gaussian \(e(-\eta/8)\), and half Gaussian. |
| Saddle support and tails | **Pass.**  The exact support is (3.8); entry/exit is retained by the incomplete Gaussian.  Equations (3.14)--(3.19) give sampled collar, Gaussian-tail, wrong-sign, and far-tail bounds. |
| \(d=0\) removed once | **Pass.**  The restricted sum starts at \(0<|d|\).  No term with \(d=0\) is reintroduced in the arithmetic or stationary decomposition. |
| Nonzero modulus multiples | **Pass without deletion.**  Every \(d=jM\ne0\) with \(|d|\le D_0\) is bounded by the same curvature argument.  Such modes are not confused with literal \(d=0\). |
| Ramanujan subtraction | **Pass.**  The term \(-c_M(d)\) remains inside \(\mathcal K_{b,d}\) and is included in (3.21), including \(c_M(d)=\varphi(M)\) when \(M\mid d\). |
| Prime-power gcd modes | **Pass.**  Complete Parseval (3.20)--(3.21) is exact for every \((M,K,d)\); no false uniform square-root rational-sum estimate is used. |
| Actual-symbol regularity | **Pass with an explicit seam.**  Bulk BV comes from the accepted principal \(V\).  The stationary remainder uses (81.A2)--(81.A3) through the overlap count (3.13), not an assumed pointwise derivative.  Round 81's transition error \(E\) is excluded. |
| Small, mesoscopic, large, and negative differences | **Pass in stated scope.**  Both signs with \(0<|d|\le D_0\) are removed.  Mesoscopic and large differences are retained exactly in (1.3); no unsupported large-\(d\) deletion is claimed. |
| Difference edges | **Pass.**  Intersections of the two stationary supports are split into \(O(1)\) intervals.  Short intersections improve (3.25); shifted entry/exit is included twice in (3.17). |
| Integer first-derivative resonances | **Pass.**  They are allowed.  The exact nonzero curvature (3.23)--(3.24) and the second-derivative lemma already count their stationary contributions. |
| Perfect powers | **Pass.**  Square and fourth-power specializations can make first derivatives integral, but cannot make (3.23) vanish for \(d\ne0\). |
| Phase-conjugating control | **Pass by scope.**  The theorem is not for arbitrary Fourier coefficients.  Its BV weight (3.16) is derived from the actual reciprocal symbol; an arbitrary phase-conjugating sequence need not satisfy it. |
| Complete-transform self-return | **Pass.**  No gain is assigned to Poisson, the Morse change of variables, completion, or inversion.  The saving is precisely the weighted second-derivative estimate (3.25). |
| Transition and axis ownership | **Pass.**  Only the smooth principal \(V\)-row is treated.  Round 81's pointwise transition remainder and both axes retain their accepted estimates. |
| Downstream scope | **Pass.**  The report proves no estimate for (1.3), no new conductor interval, no (C>J^{3/4}), cone edge, other radial sector, full `M9-M1`, `M9`, or Gauss-circle exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The selected context used was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reviews/conductor_round83_dual_normalization.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/inverse_unit_offset_attack.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_residue_normalization.md`;
- `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reviews/conductor_round81_transition_normalization.md`.

At the conductor's explicit direction during the task, I also used the
exact antecedent

- `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/derivation_packet_actual_integral_addendum.md`, specifically (81.A2)--(81.A3).

That addendum is used only in (3.11)--(3.17) to justify the smooth Morse
extension and integrated sampled error.  No sibling Round-84 report,
web source, source card, or numerical computation was read or used.  The
second-derivative lemma, finite Kloosterman Parseval identity, Morse
identity, and exponent ledger are derived in this report.

## 7. Recommended state effect

**Promote after independent seam review** a scoped new reduction:
the complete centred correlation on
\(J^{13/18}<C\le J^{3/4}\) may have every integer difference

\[
 0<|d|\le\lfloor J^{17/30}\rfloor
\]

removed target-safely, in all three local classes and both orientations,
with nonzero modulus multiples and Ramanujan/gcd modes included.  The
authoritative survivor should be revised from (84.9) to the exact
large-difference correlation (1.3).

**Promote after the same review** the uniform stationary interface
(1.4)--(1.8) and (3.5)--(3.17): exact square-root critical phase, exact
Gaussian and prefactor, explicit saddle support, one-pass entry/exit
profile, sampled BV, and aggregate error ledger for the principal
transition-flattened row.

**Retain as open** every whole-survivor \(B^{-\delta}\) estimate, the
mesoscopic/large \(d\) correlation, any conductor extension, full
`M9-M1`, `M9`, endpoint uniformity, and the global exponent.  This round
strictly shrinks the exact signed survivor but proves no new conductor or
Gauss-circle exponent.

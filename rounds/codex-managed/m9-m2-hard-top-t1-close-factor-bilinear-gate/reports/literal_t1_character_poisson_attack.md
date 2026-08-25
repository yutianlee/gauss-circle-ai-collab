# Literal (t=1) character-Poisson attack

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Task: `literal_t1_character_poisson_attack`
- Role: discovery
- Starting graph SHA-256: `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result: a literal character-Poisson, dual-divisor, and positive-differencing no-go

The literal (t=1) scalar admits an exact character-preserving Poisson
opening, but the proposed bare transforms do not prove

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{1.1}
\]

More precisely, the following route-scoped no-go is proved.

1. Squarefreeness and coprimality have the exact separable opening
   \[
   \mu ^2(d_1d_2)
   =\sum_{a^2\mid d_1}\mu(a)
    \sum_{b^2\mid d_2}\mu(b)
    \sum_{c\mid(d_1,d_2)}\mu(c).
   \tag{1.2}
   \]
   If
   \[
     Q=[a^2,c],\qquad R=[b^2,c],
   \tag{1.3}
   \]
   then only (a,c) odd survive, while (b), (R), and hence (d_2)
   may be even.  After (d_1=Qm,d_2=Rn), the character remains
   \(\chi _4(Q)\chi _4(m)\); it is not replaced by a modulus.
2. With
   \(\widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx\), the exact
   character Poisson formula is
   \[
    \boxed{
    \sum_{m\in\mathbb Z}\chi _4(m)g(m)
       ={i\over2}\sum_{s\ {
m odd}}\chi _4(s)\widehat g(s/4).}
   \tag{1.4}
   \]
   Thus the two quarter shifts transfer, rather than destroy, the
   character.  On one opened piece the positive saddle is
   \[
   d_1^*={4XQ^2d_2\over s^2},\qquad
   F(d_1^*/Q)={XQd_2\over s},\qquad JQ\le s\le2JQ,
   \tag{1.5}
   \]
   and its literal Vaaler argument is
   \[
      W\!\left({XQ\over ys}\right).
   \tag{1.6}
   \]
   The normalized saddle factor is exactly
   \[
     2L^{3/2}J^{-1/2}(Qd_2)^{-1}.
   \tag{1.7}
   \]
   Applying (1.4) a second time in the odd dual variable is exactly
   involutive (up to the Fourier reflection, cancelled by the oddness of
   \(\chi _4\)).  At stationary-principal level the two Hessian factors,
   the two Gauss factors, the negative returned frequency, and the two
   Gaussian phases multiply to (1).  Hence a second bare character
   B-process returns the original opened scalar, including its character
   and profiles.
3. Simultaneous Poisson in both variables has rank one.  Its interior
   dual equations are
   \[
      {s\over4Q}={J\over2}\sqrt{d_2/d_1},\qquad
      {\ell\over R}={J\over2}\sqrt{d_1/d_2},
   \tag{1.8}
   \]
   and therefore
   \[
      s\ell=XQR.
   \tag{1.9}
   \]
   Finite radial length (L) gives the proved collar scale
   \[
    \boxed{|s\ell-XQR|\ll QRJ/L.}
   \tag{1.10}
   \]
   The physical cone maps to
   \[
     Q\ell\le Rs\le4Q\ell.
   \tag{1.11}
   \]
   Grouping by (N=s\ell) produces a literal weighted local
   character-divisor window
   \[
     \sum_{\substack{s\mid N,\ s\ {
m odd}\\
       \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
       \chi _4(s)\,\mathcal K_{Q,R}(N;s),
   \tag{1.12}
   \]
   not an isolated two-dimensional stationary point.  For (Q=R=1),
   removing the weights and completing the divisor interval would give
   \(\sum_{s\mid N}\chi _4(s)=r_2(N)/4\); (1.12) is precisely a local
   near-square truncation of that identity.
4. The absolute collar ledger on every opened piece is
   \[
    \left({QRJ\over L}+1\right)X^\varepsilon
      \times {L^{3/2}\over QR\sqrt J}
     \ll \sqrt{JL}\,X^\varepsilon.
   \tag{1.13}
   \]
   The un-opened term (a=b=c=1) is already present.  Combining its
   collar ledger with the physical trivial bound leaves
   \[
      \min\{L^2,\sqrt{JL}\}
      \asymp L^{3/2}\min\{L^{1/2},H/L\},
   \tag{1.14}
   \]
   because (H\asymp\sqrt J).  This is target-sized only at the terminal
   boundary (L\asymp H), not uniformly in the assigned polynomial
   intermediate range (1\ll L\ll H).  For (H\ge L^{3/2}), it restores
   the full missing (L^{1/2}).  Hard boundary and literal endpoint
   families cost at most (L^{3/2+\varepsilon}) in total; they do not
   supply the missing signed saving.
5. Standard van der Corput differencing on the odd (d_1)-lattice also
   cannot be called character-sensitive after a positive norm, because
   \[
     \chi _4(d_1+2h)\chi _4(d_1)=(-1)^h
     \qquad(d_1\ {
m odd}).
   \tag{1.15}
   \]
   The character becomes a constant in each correlation and disappears
   on taking its modulus.  The phase Hessian has a radial null direction,
   so two-variable differencing does not recover an independent curvature
   direction.

Consequently, exact Möbius opening followed by one- or two-variable
Poisson and positive dual summation, a second bare character transform,
or standard positive differencing is a scoped no-go.  A new signed
estimate for (1.12), retaining cancellation between all Möbius openings,
could still prove (1.1).  The result is not a lower bound for the physical
scalar and is not a literature impossibility statement.

## 2. Exact statement and hypotheses

Use (e(t)=e^{2\pi it}) and put

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X={X\over y^2},\qquad H=\lfloor yX^{-1/4}\rfloor.
\tag{2.1}
\]

The assigned block satisfies (1\ll L\ll H\le J^{1/2}).  Since
(y=J+O(1)),

\[
 q_X=1+O(J^{-1}),\qquad H=\sqrt J+O(1),
\tag{2.2}
\]

but no floor is replaced in any transform formula below.

Let \(\mathscr R_L\) denote the exact literal half-open product shell,
dyadic block, and cone, including every entry/exit convention.  Define,
with literal boundary values and zero extension,

\[
 \mathcal A_L(x,z)=\mathbf 1_{\mathscr R_L}(x,z)
 \left({L^2\over xz}\right)^{3/4}
 \eta_L(x)\Phi\!\left({x\over H+1}\right)
 W\!\left(\sqrt{{q_Xx\over4z}}\right).
\tag{2.3}
\]

Then the scalar is exactly

\[
 \mathcal S_{L,1}=
 \sum_{d_1,d_2\ge1}\chi _4(d_1)\mu^2(d_1d_2)
 \mathcal A_L(d_1,d_2)e(J\sqrt{d_1d_2}).
\tag{2.4}
\]

Indeed, \(\mu^2(d_1d_2)=1\) is equivalent to (d_1,d_2) squarefree
and coprime, and \(\chi _4(d_1)=0\) for even (d_1).  The cone in
\(\mathscr R_L\) is (d_2\le d_1\le4d_2); no swapped orientation is
inserted.  When (d_2) is even, its factor (2) is retained.  Both
additive quarter-shift orientations of the character are retained in
(1.4).

For the stationary ledger, split the fixed literal profiles into their
finitely many smooth cells, retaining all jumps as boundary terms.  On a
smooth cell the normalized derivatives have their natural (L^{-j})
scales.  This is the favorable regularity required by the proposed
Poisson mechanism.  If a literal profile has less regularity, the exact
Poisson identities remain valid after bounded-variation approximation,
but its remainder cannot be smaller than the boundary ledger used here.

The no-go class is precise: after the exact arithmetic opening and exact
Poisson identity, it allows stationary phase, integration by parts,
divisor bounds, and positive summation over dual frequencies or Möbius
pieces.  It also includes a second unmodified character B-process and
standard Cauchy/van der Corput differencing followed by moduli.  It does
not include a new signed theorem for the actual dual coefficient
(1.12), nor cancellation between different opening triples before a
positive norm.

## 3. Proof and derivation

### 3.1 Literal coefficient, orientation, and arithmetic opening

The accepted (t=1) incidence has (g=u=v=1).  Thus (d_1,d_2) are
squarefree and coprime, (d_1) is odd, and the ordered cone is exactly
(d_2\le d_1\le4d_2).  This proves (2.4), including its normalization
and the even-(d_2) branch.

Use

\[
 \mu^2(n)=\sum_{a^2\mid n}\mu(a),\qquad
 \mathbf 1_{(u,v)=1}=\sum_{c\mid(u,v)}\mu(c).
\tag{3.1}
\]

Multiplying the three identities gives (1.2).  Put (Q=[a^2,c]) and
(R=[b^2,c]).  A term is nonempty only for (Q,R\ll L).  If (a) or
(c) is even then (Q) is even, so every (d_1) in that term is even
and the term vanishes.  Hence (a,c) may be restricted to odd integers,
but (b) is unrestricted.  With (d_1=Qm,d_2=Rn), complete
multiplicativity gives

\[
\begin{aligned}
 \mathcal S_{L,1}
  =\sum_{\substack{a,b,c\ge1\\a,c\ {
m odd}}}
   &\mu(a)\mu(b)\mu(c)\chi _4(Q)\\
  &\times\sum_{m,n\ge1}\chi _4(m)
  \mathcal A_L(Qm,Rn)e(J\sqrt{QRmn}).
\end{aligned}
\tag{3.2}
\]

This is an exact finite opening on the literal support.  It shows in
particular why writing only \(\sum_{a^2\mid d_1d_2}\mu(a)\) does not
make the coefficient separable.

The absolute multiplicity of (3.2) at one physical pair is

\[
 \left(\sum_{a^2\mid d_1}|\mu(a)|\right)
 \left(\sum_{b^2\mid d_2}|\mu(b)|\right)
 \left(\sum_{c\mid(d_1,d_2)}|\mu(c)|\right)
 \ll_\varepsilon (d_1d_2)^\varepsilon.
\tag{3.3}
\]

Thus positive opening costs (L^{2+\varepsilon}) in the two-dimensional
bulk and (L^{1+\varepsilon}) on any fixed collection of physical
boundary curves.  Rescaling gives side lengths (L/Q,L/R); derivatives
of \(\mathcal A_L(Qx,Rz)\) acquire (Q/L,R/L), exactly cancelling the
shorter side lengths.  There is no uncharged smoothing gain.

For later endpoint sums, let \(\mathfrak O_L\) be the nonempty triples in
(3.2).  Decomposing the primes of (c) according as they divide (a),
(b), both, or neither gives

\[
 \#\mathfrak O_L\ll_\varepsilon L^{1+\varepsilon},\qquad
 \sum_{\mathfrak O_L}{1\over Q}
 +\sum_{\mathfrak O_L}{1\over R}
 \ll_\varepsilon L^{1/2+\varepsilon}.
\tag{3.4}
\]

For example, after writing (c=c_a c_0), with (c_a\mid a) and
((c_0,a)=1), one has (Q=a^2c_0), whence

\[
 \sum_c{1\over Q}\ll {\tau(a)\log(2L)\over a^2};
\tag{3.5}
\]

summing over (a\ll\sqrt L) and the (O(\sqrt L)) possible (b)
proves the first weighted estimate.  For the cardinality estimate, the
part of (c) prime to (ab) is at most
(L/\max(a^2,b^2)), while its part supported on (ab) has
(L^\varepsilon) choices; summing
(L/\max(a^2,b^2)) gives (L^{1+\varepsilon}).

### 3.2 Exact character Poisson and the one-variable saddle

The identity

\[
 \chi _4(m)={e(m/4)-e(-m/4)\over2i}
\tag{3.6}
\]

holds for every integer, including even (m).  Poisson summation gives

\[
 \sum_m\chi _4(m)g(m)
 ={1\over2i}\sum_{\sigma=\pm1}\sigma
   \sum_{k\in\mathbb Z}\widehat g(k-\sigma/4).
\tag{3.7}
\]

Set (s=4k-\sigma).  The (sigma=1) terms have (s\equiv3\pmod4)
and coefficient (+1), while the (sigma=-1) terms have
(s\equiv1\pmod4) and coefficient (-1).  In both cases that
coefficient is (-\chi _4(s)), and (3.7) becomes (1.4).

Apply (1.4) to the (m)-sum in (3.2).  Up to the literal endpoint
correction quantified in Section 3.7, the exact transform is

\[
\begin{aligned}
 \mathcal S_{L,1}={i\over2}
 \sum_{\mathfrak O_L}&\mu(a)\mu(b)\mu(c)\chi _4(Q)
 \sum_{n\ge1}\sum_{s\ {
m odd}}\chi _4(s)\\
 &\times\int_{\mathbb R}
 \mathcal A_L(Qx,Rn)
 e\!\left(J\sqrt{QRnx}-{sx\over4}\right)dx.
\end{aligned}
\tag{3.8}
\]

Write (d_2=Rn).  The phase

\[
 F_s(x)=J\sqrt{Qd_2x}-{sx\over4}
\tag{3.9}
\]

has an interior critical point only for (s>0), and direct calculation
gives

\[
 x_s={4XQd_2\over s^2},\quad
 d_1^*=Qx_s={4XQ^2d_2\over s^2},\quad
 F_s(x_s)={XQd_2\over s},
\tag{3.10}
\]

\[
 |F_s''(x_s)|^{-1/2}
   =\left({32XQd_2\over s^3}\right)^{1/2}.
\tag{3.11}
\]

The cone (1\le d_1^*/d_2\le4) is exactly (JQ\le s\le2JQ).
At the saddle,

\[
 W\!\left(\sqrt{{q_Xd_1^*\over4d_2}}\right)
 =W\!\left({XQ\over ys}\right),
\tag{3.12}
\]

so the floor (y) has not been replaced.  Multiplying (3.11) by the
literal normalization yields the exact simplification

\[
 \left({L^2\over d_1^*d_2}\right)^{3/4}
 |F_s''(x_s)|^{-1/2}
 ={2L^{3/2}J^{-1/2}\over Qd_2}.
\tag{3.13}
\]

Consequently the interior stationary principal family on one opening is

\[
\begin{aligned}
 \mathcal M_{Q,R}={}&e(1/8)L^{3/2}J^{-1/2}{\chi _4(Q)\over Q}
 \sum_{n\ge1}{1\over Rn}
 \sum_{\substack{JQ\le s\le2JQ\\s\ {
m odd}}}^{\star_{\rm lit}}
 \chi _4(s)\\
 &\times \eta_L\!\left({4XQ^2Rn\over s^2}\right)
 \Phi\!\left({4XQ^2Rn\over s^2(H+1)}\right)
 W\!\left({XQ\over ys}\right)
 e\!\left({XQRn\over s}\right),
\end{aligned}
\tag{3.14}
\]

with all remaining shell/profile restrictions understood literally and
with the inherited half-saddle star.  The constant is
((i/2)\cdot2e(-1/8)=e(1/8)).

For one (d_2)-row there are (\asymp JQ) saddles, each of unnormalized
size (\asymp\sqrt{L/J}/Q).  Taking a positive norm over them costs

\[
 (JQ){\sqrt{L/J}\over Q}=\sqrt{JL}
\tag{3.15}
\]

per row, whereas the original row has only (O(L/Q)) points.  Thus
one-variable positive Poisson is worse than the rowwise trivial bound in
the hard range (J\gg L^2).  The phase in (3.14) is reciprocal, but the
character has moved to the odd dual (s); calling this cancellation
would discard the central arithmetic feature of the transform.

For comparison, Poisson first in the noncharacter (d_2)-variable has

\[
 d_2^*={Xd_1\over4\ell^2},\qquad
 F(d_2^*)={Xd_1\over4\ell},\qquad
 W\!\left(\sqrt{{q_Xd_1\over4d_2^*}}\right)=W(\ell/y),
\tag{3.16}
\]

and normalized factor (2L^{3/2}J^{-1/2}/d_1).  Its principal family is
the accepted Round-137 reciprocal hard-TOP carrier

\[
 2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{d_1\ {
m odd}}{\chi _4(d_1)\eta_L(d_1)
 \Phi(d_1/(H+1))\over d_1}
 \sum_{J/2\le\ell\le J}^{\star}W(\ell/y)
 e\!\left({Xd_1\over4\ell}\right),
\tag{3.17}
\]

before its already separated endpoints and remainders.  Formula (3.14)
is the different, character-variable transform; the two are not silently
identified.

### 3.3 Exact involution of the character transform

The self-return is not merely a similarity of phases.  Put
(h(s)=\widehat g(s/4)).  A second use of (1.4) gives

\[
 \widehat h(\xi)=\int_{\mathbb R}\widehat g(s/4)e(-\xi s)\,ds
 =4g(-4\xi).
\tag{3.18}
\]

Hence two character transforms contribute

\[
 \left({i\over2}\right)^2
 \sum_{u\ {
m odd}}\chi _4(u)\,4g(-u)
 =\sum_{u\ {
m odd}}\chi _4(u)g(u),
\tag{3.19}
\]

where \(\chi _4(-u)=-\chi _4(u)\) cancels the Fourier reflection and
the factor (-1).  This is an exact identity for the symmetrized
zero-extended profile; the literal boundary correction is transformed
and returned separately.

The saddle constants show the same fact locally.  Transform the phase
(XQd_2/s) in (3.14) a second time.  The returning dual index is
(-m<0), and

\[
 G(s)={XQd_2\over s}+{ms\over4},\qquad
 s_0=2\sqrt{{XQd_2\over m}},\qquad
 G(s_0)=J\sqrt{Qmd_2}.
\tag{3.20}
\]

At the paired saddles,

\[
 |F''_s(m)|\,G''(s_0)={1\over16}.
\tag{3.21}
\]

Thus the two inverse square-root Hessians multiply to (4).  The two
character-Poisson constants give ((i/2)^2=-1/4), the returned character
gives \(\chi _4(-m)=-\chi _4(m)\), and the Gaussian factors are
(e(-1/8)e(1/8)=1).  Their product is (1), and (d_1^*=Qm), so every
profile in (3.14) returns to its original argument.  A repeated bare
character B-process is therefore an involution, not a contraction.

### 3.4 Rank-one geometry and simultaneous dual equations

For (f(x,z)=J\sqrt{xz}),

\[
 \operatorname{Hess}f={J\over4}
 \begin{pmatrix}
 -\sqrt z\,x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-\sqrt x\,z^{-3/2}
 \end{pmatrix},qquad
 \det\operatorname{Hess}f=0,
\tag{3.22}
\]

and \(\operatorname{Hess}f\,(x,z)^T=0\).  Along
((x,z)\mapsto(\lambda x,\lambda z)), the phase is exactly linear in
\(\lambda\).

After character Poisson in (m) and ordinary Poisson in (n), one
opened term has the exact Fourier integral

\[
 I_{Q,R}(s,\ell)=\iint
 \mathcal A_L(Qx,Rz)
 e\!\left(J\sqrt{QRxz}-{sx\over4}-\ell z\right)dx\,dz,
\tag{3.23}
\]

with multiplier ((i/2)\chi _4(Q)\chi _4(s)).  Put the physical
variables

\[
 u=Qx=tw,\qquad v=Rz=t/w,qquad du\,dv={2t\over w}\,dt\,dw.
\tag{3.24}
\]

Then (3.23) has phase

\[
 t\Psi_{s,\ell}(w),\qquad
 \Psi_{s,\ell}(w)=J-{s\over4Q}w-{\ell\over Rw}.
\tag{3.25}
\]

The angular saddle is

\[
 w_0^2={4Q\ell\over Rs},
\tag{3.26}
\]

and the remaining radial frequency is

\[
 \delta_{Q,R}(s,\ell)
 =\Psi_{s,\ell}(w_0)
 =J-\sqrt{{s\ell\over QR}}.
\tag{3.27}
\]

Equations (1.8)--(1.11) follow immediately.  In particular, the
physical (w\in[1,2]) maps, when (Q=R=1), to

\[
 \ell\le s\le4\ell,qquad J\le s\le2J,qquad J/2\le\ell\le J.
\tag{3.28}
\]

The dual cone has the same close-factor orientation, with the character
on its odd larger factor (s).

### 3.5 The proved collar and the local (r_2)-window

The radial support has length \(\asymp L\).  Therefore its Fourier
transform is unsuppressed only for

\[
 |\delta_{Q,R}(s,\ell)|\ll L^{-1}.
\tag{3.29}
\]

Since (s\ell\asymp XQR), (3.29) is equivalent, up to fixed support
constants, to (1.10).  This proves the collar width; it is not guessed
from the exact hyperbola.

The angular second derivative is negative, and on the collar

\[
 |t\Psi''(w_0)|\asymp LJ.
\tag{3.30}
\]

Using (2.3) and the Jacobian in (3.24), angular stationary phase gives
the leading kernel

\[
\begin{aligned}
 I_{Q,R}(s,\ell)
 ={}&{2e(-1/8)L^{3/2}\over QR\sqrt J}
 W\!\left(\sqrt{{q_XQ\ell\over Rs}}\right)\\
 &\times\int
 \eta_L(tw_0)\Phi\!\left({tw_0\over H+1}\right)
 \mathbf 1_{\mathscr R_L}(tw_0,t/w_0)
 e(t\delta_{Q,R}){dt\over t}
 +\mathcal E_{Q,R}(s,\ell).
\end{aligned}
\tag{3.31}
\]

Thus an individual interior dual pair has scale

\[
 {L^{3/2}\over QR\sqrt J}.
\tag{3.32}
\]

One radial integration by parts gives the literal hard-end decay

\[
 \left|\int\cdots e(t\delta){dt\over t}\right|
 \ll \min\{1,(L|\delta|)^{-1}\}.
\tag{3.33}
\]

Extra smoothness improves (3.33), but is not needed.

Put (N=s\ell).  The scaled cone (1.11) is exactly

\[
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}.
\tag{3.34}
\]

Grouping (3.31) by (N) proves (1.12), with

\[
\begin{aligned}
 \mathcal K_{Q,R}(N;s)={}&
 W\!\left(\sqrt{{q_XQN\over Rs^2}}\right)\\
 &\times\int
 \eta_L(tw_{N,s})\Phi\!\left({tw_{N,s}\over H+1}\right)
 \mathbf 1_{\mathscr R_L}(tw_{N,s},t/w_{N,s})
 e\!\left(t\left[J-\sqrt{{N\over QR}}\right]\right){dt\over t},
\end{aligned}
\tag{3.35}
\]

where \(w_{N,s}=2\sqrt{QN/R}/s\).  All floors and literal profiles remain
in (3.35).  For (Q=R=1), the divisor interval is
(\sqrt N\le s\le2\sqrt N), exactly the near-square upper divisor
window of the accepted truncated \(\chi _4\)-divisor coefficient.  The
identity

\[
 {r_2(N)\over4}=\sum_{s\mid N}\chi _4(s)
\tag{3.36}
\]

shows that completing (3.35) to all divisors returns a localized radial
(r_2)-interface and leaves the complementary divisor window.  It is
not a character-sum estimate for (3.35).

There are at most

\[
 \left({QRJ\over L}+1\right)X^\varepsilon
\tag{3.37}
\]

dual pairs in the collar: there are (O(QRJ/L+1)) possible integers
(N), and each has (O(X^\varepsilon)) divisors in the dual boxes.
Combining (3.32) and (3.37), and summing the logarithmic tails from
(3.33), proves (1.13).  This is a positive capacity, not actual signed
mass.

### 3.6 Differencing loses the character and the null direction survives

Extend \(\chi _4\) by zero to even integers.  Odd shifts of an odd
(d_1) land on the even lattice and give zero correlations; the natural
nontrivial shifts are (2h).  Periodicity modulo (4) gives (1.15).
Thus a one-variable van der Corput inequality followed by absolute values
has correlations with only a constant sign ((-1)^h).  It has discarded
the literal arithmetic sign before obtaining a saving.  Shifts (4h)
erase even that constant.

Two-variable differencing meets the same geometric obstruction.  The
second differential in the radial direction ((x,z)) vanishes by
(3.22), while the mixed and two pure second derivatives satisfy

\[
 f_{xx}f_{zz}=f_{xz}^2.
\tag{3.38}
\]

Opening the two shifted squarefree/coprime indicators duplicates the
Möbius allocations rather than reducing them.  A differencing identity
that kept the signed ((-1)^h) sum before every positive norm could be a
new theorem, but it lies outside standard positive differencing and is
equivalent in difficulty to retaining the signed dual window.

### 3.7 Hard boundaries, floors, openings, and the complete power ledger

Poisson summation of a zero-extended half-open cell uses symmetric jump
values.  The difference from the literal convention is supported on the
finite collection of cone, shell, and profile entry/exit curves.  Each
contains (O(L)) physical lattice points, and (3.3) makes the total
literal correction

\[
 E_{\rm half-open}\ll_\varepsilon L^{1+\varepsilon}.
\tag{3.39}
\]

The cone endpoints (w=1,2), and the analogous profile edges, give
one-dimensional dual boundary rays.  One integration in the normal
direction costs (J^{-1}), the radial edge has length (L), and the
rescaled dual line has (O(JQ+JR)) points.  Therefore one opening costs

\[
 \ll_\varepsilon L/Q+L/R+1.
\tag{3.40}
\]

At a tangency, half-stationary phase gives the same bound.  The literal
stars, zero modes, negative modes, and cell corners are included in
(3.39)--(3.40).  Equations (3.4) imply

\[
 \sum_{\mathfrak O_L}(L/Q+L/R+1)
 \ll_\varepsilon L^{3/2+\varepsilon}.
\tag{3.41}
\]

Thus hard boundaries are target-sized after every Möbius allocation;
they neither invalidate the collar nor create its missing cancellation.

The full power ledger is:

| Interface | Literal scale before a signed theorem |
|---|---:|
| physical coefficient and coefficient-uniform capacity | (L^{2+\varepsilon}) |
| target | (L^{3/2}X^\varepsilon) |
| absolute Möbius bulk / hard boundary | (L^{2+\varepsilon}/L^{1+\varepsilon}) |
| one-character-Poisson modes per (d_2)-row | (JQ\) modes of size (\sqrt{L/J}/Q\), hence (\sqrt{JL}\) |
| two-variable collar on one opening | (QRJ/L) pairs of size (L^{3/2}/(QR\sqrt J)), hence (\sqrt{JL}\) |
| all transformed hard edges | (L^{3/2+\varepsilon}) |
| best base-opening positive bound | (\min\{L^2,\sqrt{JL}\}=L^{3/2}\min\{L^{1/2},H/L\}) |

Taking a positive norm over opening triples before their Möbius signs is
even worse: (3.4) permits (L^{1+\varepsilon}) nonempty transforms,
each with the collar capacity (1.13).  One may cap this by the original
absolute opened bulk (L^{2+\varepsilon}), but that is still above the
target by (L^{1/2-o(1)}).  The base opening (a=b=c=1) already has
the unresolved local divisor window (3.35); the other openings cannot be
discarded, and cancellation among them cannot be claimed after a norm.

## 4. First doubtful or unproved step

The first unproved affirmative step is a signed estimate for the complete
Möbius-weighted family of local dual divisor windows before any absolute
value.  In the notation above, one would need a bound of target strength
for

\[
\begin{aligned}
 {L^{3/2}\over\sqrt J}
 \sum_{\mathfrak O_L}{\mu(a)\mu(b)\mu(c)\chi _4(Q)\over QR}
 \sum_{N\asymp XQR}
 \sum_{\substack{s\mid N,\ s\ {
m odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi _4(s)\mathcal K_{Q,R}(N;s),
\end{aligned}
\tag{4.1}
\]

including the tails and literal boundary terms, with a saving of
\(\min\{H/L,L^{1/2}\}\) over its positive base-opening ledger and with
all Möbius openings still coupled.  No permitted artifact proves (4.1).

The first invalid shortcut is to replace the inner signed divisor window
by its divisor bound and then describe (1.13) as cancellation.  Completing
it to (r_2(N)/4) is also invalid: it adds the complementary divisor
window and returns to the already parked radial/full-divisor interface.
Applying character Poisson once more returns the original scalar exactly,
and positive differencing has already erased \(\chi _4\).  A bespoke
coefficient-sensitive theorem for (4.1) remains possible; this report
does not disprove it or the physical target.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_t1_coefficient_and_orientation` | GREEN: (2.3)--(2.4) retain the normalization, the ordered cone (d_2\le d_1\le4d_2), both quarter-shift signs, and no artificial swap. |
| `squarefree_coprime_even_d2_branch` | GREEN: (1.2)--(3.2) are exact; only (a,c) are forced odd, while (b,R,d_2) may be even. |
| `chi4_preserved_before_positive_norms` | GREEN: (1.4), (3.8), and (3.14) transfer \(\chi _4\) to the odd dual (s).  Positive capacities are labelled only after this formula. |
| `product_phase_rank_one_hessian` | GREEN: determinant zero and radial null vector are explicit in (3.22); no two-curvature determinant is used. |
| `one_variable_character_poisson_self_return` | GREEN no-go: the saddle, reciprocal phase, exact profile, and normalization are (3.10)--(3.14); the second character transform is exactly involutive by (3.18)--(3.21). |
| `two_variable_dual_hyperbola` | GREEN: the exact locus is (s\ell=XQR), reducing to ((k-\sigma/4)\ell=X/4) when (Q=R=1). |
| `dual_product_collar_width_and_mass` | GREEN as a positive ledger: width (QRJ/L), pair count (3.37), pair mass (3.32), and total (\sqrt{JL}X^\varepsilon).  No signed mass or lower bound is asserted. |
| `mobius_opening_and_rescaled_support_cost` | GREEN: exact (Q,R), odd/even rules, bulk/boundary multiplicity, number of openings, weighted edge sums, and rescaled side lengths are in (3.2)--(3.5). |
| `hard_cone_profiles_floors_endpoints` | GREEN for the route ledger: (W(XQ/(ys))), (W(\sqrt{q_XQ\ell/(Rs)})), exact (H+1), cone endpoints, stars, half-open corrections, and zero extension are retained in (3.12), (3.14), (3.31), and (3.39)--(3.41). |
| `missing_L_half_power` | GREEN no-go: (1.14) leaves (\min\{H/L,L^{1/2}\}\); deep blocks restore the full (L^{1/2}), and no uniform strict intermediate sector closes. |
| `physical_coefficient_vs_diagnostic` | GREEN: every large quantity is called a transform/positive capacity.  No phase-aligned array, unrestricted Kronecker alignment, density claim, or physical lower bound is used. |
| `remaining_few_point_and_downstream_scope` | GREEN: the result concerns only the literal (t=1,D\asymp L^2) face and only the named transform/differencing class. |

No numerical, symbolic, or web experiment was used.

## 6. Dependencies and exact artifacts used

This report uses only the permitted context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at graph SHA-256
   `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`;
3. `state/active_campaign.yml`;
4. `strategy/round162_m2_hard_top_t1_close_factor_strategy.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_poisson_seed.md`;
7. `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`;
8. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/synthesis.md`;
9. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md`;
10. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`.

The exact incidence and long-channel boundary come from the accepted
Round-161 kernel.  The distinction between the noncharacter reciprocal
self-return and a coefficient-sensitive fixed-centre theorem comes from
the accepted Round-137 candidate/adjudication and the current graph.  All
character-Poisson signs, opening counts, saddle constants, involution
constants, collar width, local divisor grouping, boundary costs, and
powers in this report were rederived here.

## 7. Recommended state effect

Recommend the Round-162 closing label
`hard_top_t1_close_factor_bilinear_no_go` for this report's narrowly
defined mechanism class.

Retain as candidate evidence, for independent seam review:

1. the exact opening (3.2), including the even-(d_2) branch and its
   bulk/boundary costs;
2. the character-Poisson formula, literal saddle/profile normalization,
   and exact involution (3.8)--(3.21);
3. the rank-one dual hyperbola, proved collar, and local weighted
   \(\chi _4\)-divisor window (3.22)--(3.37); and
4. the positive ledger and differencing obstruction
   (1.13)--(1.15), (3.39)--(3.41).

Do not promote the (t=1) target, a physical lower bound, a literature
impossibility claim, or a strict hard-TOP sector.  The next admissible
statement is a signed theorem for (4.1) that gains before every positive
norm and is not proved by completing to (r_2), repeating the involutive
transform, or discarding the Möbius coupling.  Even such a theorem would
leave all (L\ll D\ll L^2, t\ll\sqrt L) few-point channels, the full
hard-TOP parent, M9--M2, M9, the bridge, and every global exponent open.

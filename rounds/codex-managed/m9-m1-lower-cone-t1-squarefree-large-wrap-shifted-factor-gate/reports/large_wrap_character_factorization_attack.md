# Round 151 discovery report: two-adic shifted-factor recovery and reciprocal endpoint corridors

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Round: 151
- Task: `large_wrap_character_factorization_attack`
- Role: discovery
- Starting graph SHA-256: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Allocation: 100% analytic/algebraic and source-hypothesis checking; 0% numerical
- Terminal label: `strict_large_wrap_character_range`

## 1. Result: an exact transfer, two strict ranges, and one source-conditional corridor

Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le \sqrt M,\qquad
 Q=2\sqrt{ND/E}\asymp \frac{DR^2}{\sqrt M}.
\tag{151.1}
\]

The proposed two-adic character transfer is exact.  If
\(k\ne0\), \(j=\nu _2(|k|)\),

\[
 A=NL_1-khr_1,\qquad B=NL_2+khr_2,
\tag{151.2}
\]

and all \(L_i,h,r_i\) are odd, then

\[
 x:=\frac{NL_1-A}{2^j}=\frac{k}{2^j}hr_1,
 \qquad
 y:=\frac{B-NL_2}{2^j}=\frac{k}{2^j}hr_2
\tag{151.3}
\]

are odd, nonzero, and have the same sign.  Consequently

\[
 \boxed{
 \chi _4(L_1L_2r_1r_2)=\chi _4(L_1L_2xy).}
\tag{151.4}
\]

This holds for both signs of \(k\) and every parity of \(N\).  The
complete inverse map is also exact, but it has a divisor fibre that
must not be suppressed.  If

\[
 g=(|x|,|y|),\qquad \epsilon=\operatorname {sgn}x,
 \qquad r_1=|x|/g,\quad r_2=|y|/g,
\tag{151.5}
\]

then the preimages of \((A,B,j)\) are indexed by the positive odd
divisors \(h\mid g\) that pass the literal support, reducedness,
centering, collar, and packet tests, with

\[
 k=\epsilon 2^j\frac gh,\qquad kh=\epsilon2^jg.
\tag{151.6}
\]

Thus \(r_i\), \(kh\), and \(\rho\) are determined by
\((A,B,j)\), but \(h\) and \(k\) separately are not.  The two
profiles, phase denominator, and packet membership still depend on
the recovered divisor \(h\).  This is the first exact recovery seam.

Two strict positive ranges follow.

1.  **All-scale high-two-adic sparse wraps.**  Uniformly in every
    allowed \(M,D,E,Q\), the large-wrap classes satisfying

    \[
       2^{\nu _2(|k|)}\ge c\frac{N}{R^2}\asymp cR^2
    \tag{151.7}
    \]

    form a set of cardinality
    \(O(1+R^2/Q)\).  The accepted arbitrary-packet fixed-wrap
    theorem therefore gives their complete coefficient-weighted
    absolute contribution as

    \[
       \boxed{O_\varepsilon(R^2D X^\varepsilon).}
    \tag{151.8}
    \]

    This includes every literal prefix, profile, incidence atom,
    common factor, imprimitive denominator, phase, and character.

2.  **Actual-profile TTY low-\(L\) endpoint corridor.**  Before
    expanding the energy, let

    \[
    G_U(d)=
    \sum_{L}\frac{\chi _4(L)B_{d,U}(L)}L
    \sum_{\substack{q\asymp LQ\;\mathrm{odd}\\(L,q)=1}}
       \chi _4(q)\mathscr W_{d,U}(L/q)e(NdL/q).
    \tag{151.9}
    \]

    The actual Round-148 profile has uniformly bounded discrete
    variation in \(q\), after adjoining the already owned boundary
    pieces.  The accepted norm

    \[
       \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
       \ll_\varepsilon X^\varepsilon
    \tag{151.10}
    \]

    and the graph-certified Tao--Trudgian--Yang pair
    \((89/1282,997/1282)\) give a strict low-\(L\) corridor.  If
    \(G_{U,\le L_0}(d)\) denotes (151.9) restricted to
    \(L\le L_0\le E\), then

    \[
       |G_{U,\le L_0}(d)|
       \ll_\varepsilon
       E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon,
    \tag{151.14}
    \]

    and its energy is target-safe under the exact condition

    \[
       \boxed{
       M^{819}\gg R^{1424}D^{1816}L_0^{534}.}
    \tag{151.15}
    \]

    For \(D=1,L_0=1\), this starts at
    \(M\gg R^{1424/819}\), and it bounds the literal compulsory
    \(D=1,L=1\) scalar.  Cross terms with \(L>L_0\) are not included
    in this low-\(L\) claim.

There is also one full-\(L\) **candidate**, conditional on independent
correction of the project's Bourgain source-audit node.  Section 5 of
Bourgain's primary paper does more than state the pair
\((13/84,55/84)\): after Theorem 6 it separately removes the
square-root length restriction by rescaling and the \(B\)-process, and
removes the full-dyadic-interval restriction by extension and partial
sums.  The reciprocal phases below satisfy the stated exponent-pair
function class.  On that primary-source interface, the whole row obeys

\[
 |G_U(d)|\ll_\varepsilon E^{13/84}Q^{55/84}X^\varepsilon
\]

and its energy is target-safe precisely in the corridor

\[
 \boxed{D^{84}R^{52}\ll M^{29}.}
\]

This is not promoted as an accepted graph theorem in this report: the
local source card currently records only Theorem 4's narrower direct
window.  Theorem 4 and Theorem 6 are reconciled exactly in Section 3.8.

The full growing-\(M\) large-wrap collar is not proved.  Outside the
TTY endpoint corridor and, conditionally, the Bourgain full-row
corridor, the first remaining sector is

\[
 k\notin\mathcal K_0,\qquad
 0<|\rho|\le hr_1r_2/D,\qquad
 2^{\nu _2(|k|)}\ll R^2,
\tag{151.16}
\]

with the full recovered \(h\mid g\) fibre retained.  The transfer
(151.4) is algebraically exact but supplies no estimate for this
low-two-adic signed sum by itself.

## 2. Exact statement and hypotheses

All variables \(L_i,q_i,h,r_i\) in the compressed reciprocal row are
positive and odd,

\[
 q_i=hr_i,\qquad (r_1,r_2)=1,qquad
 (L_i,q_i)=1,qquad q_i\asymp L_iQ,qquad L_i\le E
\tag{151.17}
\]

up to the fixed support constants.  The last restriction also follows
directly from a nonzero Round-150 prefix: with
\(L=acs^2\), its progression index is
\(n=au(csv)^2=L\,ucv^2\ge L\), while the literal prefix has
\(n\ll E\).  This observation gives the lower derivative scale
\(E/L\gg1\) required below.

For a pair of cells define

\[
 \delta=L_1r_2-L_2r_1,qquad
 \rho=N\delta-khr_1r_2,qquad
 |\rho|\le \frac{hr_1r_2}{2},
\tag{151.18}
\]

where \(k\) is the unique centered integer.  Since
\(hr_1r_2\) is odd, a centering tie would equate an even integer with
an odd integer and is impossible.  Fix a symmetric accepted packet
\(\mathcal K_0\) with

\[
 |\mathcal K_0|\ll1+R^2/Q.
\tag{151.19}
\]

The frozen residual is the growing-\(M\) part with
\(k\notin\mathcal K_0\) and
\(0<|\rho|\le hr_1r_2/D\).

To make the coefficient literal, write
\(d=\eta m\), \(\eta\in\{1,2\}\), with \(m\) odd squarefree, and
\(L_i=t_is_i^2\).  For \(a_i\mid t_i\), put

\[
 c_i=t_i/a_i,\quad
 n_i=a_iu_i(c_is_iv_i)^2,\quad
 F=[a_1u_1,a_2u_2],\quad
 P=\operatorname {rad}(c_1c_2s_1s_2v_1v_2),
\tag{151.20}
\]

and

\[
 \beta_i=
 \frac{\mu(a_i)\mu(c_i)\mu(s_i)\mu(u_i)\mu(v_i)}
      {c_iu_iv_i^2}.
\tag{151.21}
\]

Here each \(v_i\) is odd squarefree and
\((v_i,c_is_i)=1\).  The exact product coefficient is the finite sum

\[
 \sum_{\mathbf a,\mathbf u,\mathbf v}
 \sum_{z\mid P}
 \beta_1\beta_2\mu(z)
 {\mathbf 1}_{(F,P)=1}{\mathbf 1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2).
\tag{151.22}
\]

Thus the literal large-wrap residual is

\[
\begin{aligned}
 \mathcal C_{\mathrm{LW},U}={}&
 \sum_{\eta=1,2}
 \sum_{\substack{m\ \mathrm{odd\ squarefree}\\\eta m\asymp D}}
 \sum_{\substack{L_i,q_i\ \mathrm{as\ in}\ (151.17)\\
                  k\notin\mathcal K_0\\
                  0<|\rho|\le hr_1r_2/D}}
 \frac{\chi_4(L_1L_2r_1r_2)}{L_1L_2}
 e\!\left(\frac{\eta m\rho}{hr_1r_2}\right)\\
 &\quad\times
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}\\
 &\quad\times
 \sum_{\mathbf a,\mathbf u,\mathbf v,z}
 \beta_1\beta_2\mu(z)
 {\mathbf 1}_{(F,P)=1}{\mathbf 1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2).
\end{aligned}
\tag{151.23}
\]

The innermost sum has exactly the restrictions in (151.20)--(151.22).
Equation (151.23), not an arbitrary coefficient matrix, is the object
to which the shifted-factor coordinates are applied.

The strict TTY reciprocal claim uses the exact pre-energy row (151.9).
Every radial-prefix or cone boundary piece removed before the smooth
Round-148 profile retains its accepted target-safe owner.  A prefix
shorter than its transition collar also retains that owner.  The
claims below apply to the remaining actual profile and, together with
those named boundary owners, are owner-complete in their stated
parameter ranges.

## 3. Proof and derivation

### 3.1 Positivity and the shifted-factor identities

Direct expansion gives

\[
 \boxed{AB=N^2L_1L_2+kh\rho.}
\tag{151.24}
\]

The two one-factor identities are

\[
 r_2A=NL_2r_1+\rho,
 \qquad
 r_1B=NL_1r_2-\rho.
\tag{151.25}
\]

On the collar,

\[
 \frac{|\rho|}{NL_2r_1}
 \le \frac{hr_1r_2}{DNL_2r_1}
 =\frac{q_2}{DNL_2}
 \ll\frac{Q}{DN}\ll R^{-2},
\tag{151.26}
\]

and the symmetric estimate holds for the second identity.  Therefore
\(A,B>0\) for large \(X\), uniformly in both signs of \(k\) and
\(\rho\).  This excludes zero factors even when \(q_i\mid N\).

### 3.2 Exact two-adic and parity ledger

Write

\[
 k=2^j\kappa,\qquad \kappa\in\mathbb Z\ \mathrm{odd}.
\tag{151.27}
\]

Since \(h,r_i\) are odd, (151.3) shows

\[
 \nu_2(NL_1-A)=\nu_2(B-NL_2)=j.
\tag{151.28}
\]

Let \(n=\nu_2(N)\).  Because \(L_i\) are odd,

\[
\begin{array}{c|c}
 \text{relation of }j\text{ and }n&
 (\nu_2(A),\nu_2(B))\\ \hline
 j<n&(j,j)\\
 j>n&(n,n)\\
 j=n&(\ge n+1,\ge n+1).
\end{array}
\tag{151.29}
\]

In particular, if \(N\) is odd, then \(A,B\) are even for \(j=0\)
and odd for \(j\ge1\).  If \(N\) is even, then \(A,B\) are odd for
\(j=0\); the remaining cases are exactly those in (151.29).  Thus a
proof that silently applies \(\chi_4\) to \(A\) or \(B\) is invalid
in several compulsory parity classes.  The lawful character arguments
are the odd quotients \(x,y\).

There is also an exact parity check on the shift.  Since
\(\delta\) is even and \(hr_1r_2\) is odd,

\[
 \rho\ \text{is odd if and only if }j=0.
\tag{151.30}
\]

More precisely, if \(t=\nu_2(\delta)\), with \(t=\infty\) when
\(\delta=0\), then for \(j\ne n+t\)

\[
 \nu_2(\rho)=\min(j,n+t),
\tag{151.31}
\]

while for \(j=n+t\) the valuation is at least \(j+1\).  The
nonexact hypothesis excludes only \(\rho=0\), not any of these parity
classes.

### 3.3 Character transfer for both signs of \(k\)

The two quotients in (151.3) satisfy

\[
 xy=\kappa^2h^2r_1r_2.
\tag{151.32}
\]

For every odd signed integer \(u\),
\(\chi_4(u^2)=1\).  Complete multiplicativity therefore gives

\[
 \chi_4(L_1L_2xy)
 =\chi_4(L_1L_2)\chi_4(\kappa^2h^2)
  \chi_4(r_1r_2)
 =\chi_4(L_1L_2r_1r_2),
\tag{151.33}
\]

which proves (151.4).  If \(k<0\), both \(x,y\) are negative, so
their product remains the positive odd integer in (151.32); no sign
exception occurs.  The proof never uses the parity of \(N\).

### 3.4 Complete inverse recovery and its divisor fibre

Conversely fix \(N,L_1,L_2,A,B,j\), with \(A,B>0\), and impose

\[
 2^j\Vert NL_1-A,qquad
 2^j\Vert B-NL_2,qquad
 xy>0,
\tag{151.34}
\]

where \(x,y\) are defined by (151.3).  Define \(g,\epsilon,r_i\)
by (151.5).  Then \(r_i\) are positive odd and coprime.  Set

\[
 \delta=L_1r_2-L_2r_1,qquad
 \rho=N\delta-\epsilon2^jg r_1r_2.
\tag{151.35}
\]

For every positive divisor \(h\mid g\), define \(k\) by (151.6).
Then \(k\) is an integer with \(\nu_2(|k|)=j\), and

\[
 khr_1=2^jx=NL_1-A,qquad
 khr_2=2^jy=B-NL_2.
\tag{151.36}
\]

Thus (151.2) is recovered exactly, and expanding as in (151.24) gives

\[
 AB-N^2L_1L_2=(kh)\rho=(\epsilon2^jg)\rho.
\tag{151.37}
\]

The divisor \(h\) is admissible if and only if all the following
literal tests hold:

\[
\begin{gathered}
 q_i=hr_i\asymp L_iQ,qquad (L_i,q_i)=1,qquad
 h=(q_1,q_2),\\
 0<|\rho|\le hr_1r_2/D,qquad
 |\rho|\le hr_1r_2/2,qquad
 k\notin\mathcal K_0,
\tag{151.38}
\end{gathered}
\]

together with the exact support of both sampled profiles.  The gcd
identity in (151.38) is automatic once \((r_1,r_2)=1\), but is listed
to make recovery explicit.  Conversely every original admissible
tuple supplies exactly one such recovered record.  Hence this is a
bijection after adjoining the divisor \(h\), and its fibre has size at
most

\[
 \tau(g)\ll_\varepsilon X^\varepsilon.
\tag{151.39}
\]

Crucially, all divisors in the fibre have the same \(kh\), \(r_i\),
\(\delta\), \(\rho\), \(A\), and \(B\), but generally different
\(q_i=hr_i\), phase denominators \(hr_1r_2\), profile samples, and
values of \(k\).  Therefore the fibre cannot be discarded merely
because it is divisor-bounded.

With \(\mathfrak H(A,B,j)\) denoting exactly the divisors passing
(151.38), the low-two-adic residual has the exact joint form

\[
\begin{aligned}
 \sum_{d,L_1,L_2}\sum_{j<J_*}
 \sum_{\substack{A,B>0\\(151.34)}}
 \sum_{h\in\mathfrak H(A,B,j)}
 &\chi_4(L_1L_2xy)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\times
 \mathscr W_{d,U}(L_1/(hr_1))
 \overline{\mathscr W_{d,U}(L_2/(hr_2))}
 e\!\left(\frac{d\rho}{hr_1r_2}\right),
\end{aligned}
\tag{151.40}
\]

with the coefficient in (151.22), squarefree rows, and all exact
prefixes understood literally.  Here \(2^{J_*}\asymp R^2\).  Equation
(151.40) jointly reindexes every remaining shift before absolute
values; it is an identity, not yet an estimate.

### 3.5 The high-two-adic sparse range

The support and centering give

\[
 |k|\ll N/Q.
\tag{151.41}
\]

Indeed \(|\delta|\ll L_1L_2Q/h\), while
\(hr_1r_2\asymp L_1L_2Q^2/h\), and the centered remainder contributes
at most \(1/2\).  Let \(J_*\) be chosen so that

\[
 2^{J_*}\asymp N/R^2\asymp R^2.
\tag{151.42}
\]

The number of nonzero signed integers in (151.41) divisible by
\(2^{J_*}\) is

\[
 \ll1+\frac{N/Q}{2^{J_*}}
 \ll1+\frac{R^2}{Q}.
\tag{151.43}
\]

The condition \(\nu_2(|k|)\ge J_*\) is a subset of these multiples.
Intersecting with the complement of \(\mathcal K_0\) can only reduce
the cardinality.  Round 150 proves an absolute
\(DQX^\varepsilon\) bound per arbitrary fixed wrap, with every
\(d,L_i,h\) and coefficient weight already summed.  Therefore

\[
 DQX^\varepsilon\left(1+\frac{R^2}{Q}\right)
 \ll R^2DX^\varepsilon,
\tag{151.44}
\]

because \(Q\ll R^2\).  This proves (151.8) and names its exact
complement \(j<J_*\).

### 3.6 Uniform bounded variation of the actual reciprocal profile

Write \(q=LQy\) on one fixed compact support component.  The exact
sample is

\[
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{151.45}
\]

The Round-148 derivative ledger says that, as a function of this
normalized \(y\), bulk factors have first derivative \(O(1)\), a
radial transition has derivative \(O(M^{1/2})\) on a set of
\(y\)-length \(O(M^{-1/2})\), and a cone transition has derivative
\(O(D^{1/2})\) on a set of length \(O(D^{-1/2})\).  Thus every named
factor has total variation \(O(1)\).  There are only finitely many
such factors on each inherited component, all have bounded supremum,
and the finite half-open boundaries contribute only bounded jumps.
Consequently

\[
 \boxed{
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_{q}
   \mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon.}
\tag{151.46}
\]

This is a statement about the actual Round-148 product profile.  It
does not follow from pointwise smoothness of an arbitrary function.
The exact floor prefix \(\kappa_{d,U}\) is inside \(B_{d,U}(L)\) and
does not vary with \(q\).  A terminal prefix shorter than the radial
transition was already assigned to the primal collar owner, so it is
not silently included in (151.46).

### 3.7 Coprimality, residue classes, and a general exponent-pair bound

Let \((\kappa,\lambda)\) be a verified exponent pair whose audited
theorem applies at every length and phase parameter occurring in the
family below, and define

\[
 S_{d,L}:=
 \sum_{\substack{q\asymp LQ\;\mathrm{odd}\\(L,q)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q).
\tag{151.47}
\]

Resolve \(\chi_4(q)\) into the two residue classes modulo four and
use

\[
 {\mathbf 1}_{(L,q)=1}=\sum_{c\mid(L,q)}\mu(c).
\tag{151.48}
\]

Since \(L\) and \(c\) are odd, after writing \(q=cm\), the residue
of \(m\) modulo four is fixed.  Put \(m=4n+a\).  The new interval has
length

\[
 Y_c\asymp LQ/c,
\tag{151.49}
\]

and its phase is

\[
 f_c(n)=\frac{NdL}{c(4n+a)}.
\tag{151.50}
\]

For every fixed derivative order \(r\ge1\),

\[
 |f_c^{(r)}(n)|\asymp_r
 \frac{NdL/c}{Y_c^{r+1}}
 =Z_cY_c^{1-r},
 \qquad
 Z_c\asymp \frac{cE}{L},
\tag{151.51}
\]

 uniformly for \(d\asymp D\).  Put

 \[
  \mathcal T_c:=Z_cY_c\asymp \frac{Nd}{Q}.
 \tag{151.51a}
 \]

 The nonempty-prefix restriction \(L\ll E\), with fixed support
 constants, gives \(Z_c=\mathcal T_c/Y_c\ge z_0>0\).  When
 \(\mathcal T_c\ge Y_c\), the exact shifted reciprocal is in the
 audited TTY exponent-pair range on every proper subinterval.  At the
 fixed comparable upper-support edge where \(\mathcal T_c<Y_c\), one
 instead has \(z_0\le Z_c<1\) and the second-derivative estimate gives

 \[
  \sum_{n\in I}e(f_c(n))
  \ll Y_c|f_c''|^{1/2}+|f_c''|^{-1/2}
  \ll_{z_0}Y_c^{1/2}.
 \tag{151.51b}
 \]

 For TTY, \(\lambda=997/1282>1/2\) and \(\kappa\ge0\), so
 \(Y_c^{1/2}\ll_{z_0}Z_c^\kappa Y_c^\lambda\).  Thus this edge obeys
 the same TTY-shaped majorant as the main exponent-pair range.  Abel
 summation using (151.46) gives in both cases

\[
 \sum_{n} \mathscr W_{d,U}(L/(c(4n+a)))e(f_c(n))
 \ll_\varepsilon
 Z_c^\kappa Y_c^\lambda X^\varepsilon.
\tag{151.52}
\]

The divisor factor is

\[
 Z_c^\kappa Y_c^\lambda
 \asymp
 (E/L)^\kappa(LQ)^\lambda c^{\kappa-\lambda}.
\tag{151.53}
\]

 For TTY, the theorem plus (151.51b) covers every divisor
 \(c\mid L\); since \(\lambda>\kappa\), summing those divisors costs
 only \(X^\varepsilon\).  Hence

\[
 \boxed{
 |S_{d,L}|\ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda X^\varepsilon.}
\tag{151.54}
\]

 This derivation retains the exact character and coprimality.  It does
 not replace them with arbitrary denominator coefficients.  The
 second-derivative edge repairs the convention
 \(\mathcal T_c\ge Y_c\) for either exponent pair used below.  For the
 Bourgain pair it is needed only at the fixed comparable edge left
 outside the source convention \(Y_c\le\mathcal T_c\).

### 3.8 Bourgain Theorem 4 versus Theorem 6: a conditional full-\(L\) corridor

The pair under audit is

\[
 (\kappa,\lambda)=
 \left(\frac{13}{84},\frac{55}{84}\right).
\tag{151.55}
\]

Bourgain's Theorem 4 proves the direct estimate

\[
 |S|\ll Y^{1/2}\mathcal T^{13/84+\varepsilon}
 \quad\hbox{only when}\quad
 \mathcal T^{17/42}\ll Y\le \mathcal T^{1/2}.
\tag{151.55a}
\]

That direct window is not uniform in the present Mobius expansion.
Indeed, for \(c=1\) and a possible \(L\asymp E\),
\(Y_1\asymp EQ\asymp\mathcal T_1\), so Theorem 4 alone cannot justify
the full-\(L\) calculation.

The primary source then supplies a genuinely broader interface in
Section 5.  Before stating Theorem 6, its equation (5.1) records the
same bound for every
\(0<\log Y/\log\mathcal T\le1/2\), provided the phase belongs to the
class to which exponent-pair theory applies; the lower cutoff
\(17/42\) from Theorem 4 is absent.  Theorem 6 then states that
(151.55) is an exponent pair, with an arbitrary epsilon perturbation
in both entries.  The paragraphs immediately following it explicitly
handle the two remaining gaps between direct use of (5.1) and the
global exponent-pair assertion:

1. when the summation length exceeds \(\mathcal T^{1/2}\), but does
   not exceed \(\mathcal T\), the near-boundary cases are rescaled to
   phase parameter \(Y^2\), the extreme cases use the
   \((1/2,1/2)\) pair, and the intermediate cases are sent by Poisson
   and partial summation to length \(Y'\asymp\mathcal T/Y\) with
   \(\mathcal T'\asymp\mathcal T\); this is the exponent-pair
   \(B\)-process, and it returns the same pair because
   \(\lambda=\kappa+1/2\); and
2. for a proper subinterval, the phase is extended to the full dyadic
   interval while preserving the Graham--Kolesnik derivative
   conditions, after which Sargos's partial-sum lemma costs only a
   logarithm.

Thus (151.55a) is Theorem 4's direct range, not the range of the
Theorem 6 exponent-pair interface: (5.1) already removes its lower
cutoff, and the ensuing rescaling, \(B\)-process, extension, and
partial-sum argument remove the two remaining restrictions.  This is
the source's stated logic, not an inference merely from the theorem's
name.

It remains to check the function class.  On each of \(O(1)\) fixed
dyadic support pieces, put \(u=x/Y_c\).  From (151.50)--(151.51a),

\[
 f_c(Y_cu)=\mathcal T_cF_{c,a}(u),\qquad
 F_{c,a}(u)=\frac1{4u+a/Y_c},\qquad
 F_{c,a}^{(r)}(u)=
 \frac{(-1)^r r!4^r}{(4u+a/Y_c)^{r+1}}.
\tag{151.55b}
\]

The support keeps \(u\) in a fixed compact subinterval of
\((0,\infty)\), while \(a\in\{1,3\}\) and \(Y_c\gg Q\gg R\).  Hence
all required scaled derivatives have uniform upper and nonzero lower
bounds.  Equivalently,
\[
 f_c'(x)=-\frac{NdL}{4c}\,x^{-2}
 \left(1+\frac{a}{4x}\right)^{-2}
\]
is a reciprocal monomial times the \(C^P\) factor
\(g(x):=(1+a/(4x))^{-2}\).  Its value is \(1+O(Y_c^{-1})\), and its
positive-order normalized
derivatives satisfy \(x^rg^{(r)}(x)=O_r(Y_c^{-1})\) on
\(x\asymp Y_c\).  Its derivative ratios therefore satisfy the standard
Graham--Kolesnik monomial conditions uniformly.  Bourgain's extension
argument applies to every proper prefix produced by the literal
support.

For \(\mathcal T_c\ge Y_c\), Theorem 6 gives the unweighted
partial-sum bound.  For \(z_0\le\mathcal T_c/Y_c<1\), (151.51b) gives
the same shape because \(55/84>1/2\).  Consequently

\[
 \max_{I'\subset I}\left|\sum_{n\in I'}e(f_c(n))\right|
 \ll_\varepsilon
 Z_c^{13/84}Y_c^{55/84}X^\varepsilon
\tag{151.55c}
\]

for every \(c\mid L\).  The actual profile is not inserted into
Bourgain's theorem: (151.55c) is first proved without weights, and only
then does Abel summation with (151.46) yield (151.52).  The epsilon
perturbations and the partial-sum logarithm are absorbed by
\(X^\varepsilon\).  Finally \(c^{\kappa-\lambda}=c^{-1/2}\), so the
complete Mobius sum costs only another \(X^\varepsilon\).

The identity \(\lambda-\kappa=1/2\), (151.54), and (151.10) now give

\[
\begin{aligned}
 |G_U(d)|
 &\le \sum_L\frac{|B_{d,U}(L)|}{L}|S_{d,L}|\\
 &\ll_\varepsilon E^{13/84}Q^{55/84}
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}X^\varepsilon,
\end{aligned}
\tag{151.56}
\]

and, on this conditional interface, after squaring and summing the
\(O(D)\) rows gives

\[
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon
 D E^{13/42}Q^{55/42}X^\varepsilon.
\tag{151.57}
\]

Now

\[
 E^{13/42}Q^{55/42}
 \asymp D R^{55/21}M^{-29/84}.
\tag{151.58}
\]

Comparison with \(R^2\) gives exactly

\[
 \frac{E^{13/42}Q^{55/42}}{R^2}
 =\left(\frac{D^{84}R^{52}}{M^{29}}\right)^{1/84}
\tag{151.59}
\]

up to fixed support constants.  Therefore the primary-source theorem
and the audited reciprocal class produce the candidate strict corridor

\[
 \boxed{D^{84}R^{52}\ll M^{29}.}
\]

At \(D=1\) it begins at \(M\gg R^{52/29}\).  At
\(M\asymp R^2\) it permits \(D\ll R^{1/14}\).  Because the current
project source-audit node scopes the pair only to (151.55a), this report
retains (151.56)--(151.59) as a candidate conditional on an independent
primary-source correction, rather than treating it as an already
accepted graph owner.

### 3.9 Tao--Trudgian--Yang's low-\(L\) corridor

The authoritative graph certifies the global pair

\[
 (\kappa,\lambda)=
 \left(\frac{89}{1282},\frac{997}{1282}\right)
\tag{151.60}
\]

for actual fixed discrete-BV reciprocal profiles.  Here

\[
 \lambda-\kappa-\frac12=\frac{267}{1282}.
\tag{151.61}
\]

For every Mobius divisor with \(\mathcal T_c\ge Y_c\), this is the
direct graph-certified TTY placement.  For the only remaining
comparable edge \(z_0\le\mathcal T_c/Y_c<1\), (151.51b) is
\(O(Y_c^{1/2})\), which is dominated by the same TTY-shaped bound
because \(997/1282>1/2\).  Thus (151.54) is uniform over the complete
coprimality expansion.

Consequently, on \(L\le L_0\), (151.54) gives

\[
\begin{aligned}
 |G_{U,\le L_0}(d)|
 &\ll_\varepsilon E^{89/1282}Q^{997/1282}
 \sum_{L\le L_0}\frac{|B_{d,U}(L)|}{\sqrt L}
 L^{267/1282}X^\varepsilon\\
 &\ll_\varepsilon
 E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon,
\end{aligned}
\tag{151.62}
\]

which proves (151.14).  Its squared ratio to the per-row target is

\[
 \frac{E^{178/1282}Q^{1994/1282}L_0^{534/1282}}{R^2}
 =\left(
 \frac{R^{1424}D^{1816}L_0^{534}}{M^{819}}
 \right)^{1/1282}.
\tag{151.63}
\]

This proves (151.15) after the \(d\)-sum.  The Mobius progression
factor in (151.53) is now
\(c^{-908/1282}\), so coprimality still costs only
\(X^\varepsilon\); no normalization from the existing TTY graph node
has been changed.

At the top \(M\asymp R^2\), the low-\(L\) condition becomes

\[
 D^{1816}L_0^{534}\ll R^{214}.
\tag{151.64}
\]

For \(D=1\), it permits
\(L_0\ll R^{107/267}\); for \(L_0=1\), it permits
\(D\ll R^{107/908}\).  The cross sector in which exactly one of
\(L_1,L_2\) exceeds \(L_0\), and the large-large sector, are named
complements and are not absorbed into (151.62).

### 3.10 The literal \(D=1,L=1\) scalar and the three \(M\)-ranges

At \(D=1,L=1\), the exact scalar is

\[
 S_U(N,Q)=
 \sum_{q\asymp Q}\chi_4(q)
 \mathscr W_{1,U}(1/q)e(N/q),
\tag{151.65}
\]

multiplied by \(B_{1,U}(1)\).  The Fourier identity

\[
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\tag{151.66}
\]

is exact for every integer \(q\); the residue-class proof above is the
equivalent direct exponent-pair placement and retains the same two
branches.  The TTY pair gives

\[
 |S_U(N,Q)|\ll_\varepsilon
 R^{997/641}M^{-819/2564}X^\varepsilon.
\tag{151.67}
\]

Thus \(|S_U|\ll RX^\varepsilon\) when

\[
 M^{819}\gg R^{1424}.
\tag{151.68}
\]

On the primary-source Theorem 6 interface, Bourgain gives

\[
 |S_U(N,Q)|\ll_\varepsilon
 R^{55/42}M^{-29/168}X^\varepsilon,
\tag{151.69}
\]

which becomes target-sized when \(M^{29}\gg R^{52}\).  For comparison,
at \(D=L=1\), the narrower direct Theorem 4 window (151.55a) is
equivalent to

\[
 R^{4/3}\ll M\ll R^{100/59}.
\tag{151.69a}
\]

Since \(52/29>100/59\), Theorem 4 by itself ends before (151.69)
becomes target-sized.  Section 5's Theorem 6 is exactly what removes
that direct-window obstruction.  Hence (151.69) is a primary-source
candidate at \(M\gg R^{52/29}\), conditional on correction of the
narrower project source card.

The complete scale ledger is therefore:

- bounded \(M\): already owned by Round 150;
- intermediate growing \(M\): TTY owns only the low-\(L\) sector
  satisfying (151.15), while the source-conditional Bourgain candidate
  would bound the full row when (151.59) is target-safe;
- \(M\asymp R^2\): TTY gives the low-\(L\) wedge (151.64), while the
  Bourgain candidate would give the full-row wedge
  \(D\ll R^{1/14}\); and
- outside the TTY corridor and the conditional Bourgain corridor, the
  available upper bounds lose the exact factors displayed in
  (151.63) and (151.59).  Neither factor is a signed lower bound.

The reciprocal B-process applied to (151.66) has stationary equation
\(-N/q^2+\sigma/4=m\) and returns square-root phases on
\(4n+\sigma\).  No dual main sum is used as an error here.  Outside the
certified TTY corridor and the source-conditional Bourgain corridor,
estimating that returned square-root wave is a remaining analytic task
rather than an automatic gain.

## 4. First doubtful or unproved step

There is first an acceptance seam: the project's Bourgain source card
must be independently corrected before (151.56)--(151.59) can become
an accepted graph owner.  The primary-source derivation in Section 3.8
supports that correction but this discovery report cannot make it.

Conditional on that source correction, after removing the accepted
packet, the new high-two-adic owner (151.8), the bounded-\(M\) owner,
the certified TTY low-\(L\) corridor, and the Bourgain full-row
candidate, the first unproved object is exactly (151.40) with

\[
 j<J_*,\qquad k\notin\mathcal K_0,qquad
 0<|\rho|\le hr_1r_2/D,
\tag{151.70}
\]

outside (151.15) in the stated low-\(L\) sector and outside (151.59)
for the full row.
The character is now a product of the two odd shifted differences,
but the recovery divisor \(h\mid g\) remains inside both profile
samples, the phase denominator, the support, and the reconstructed
wrap \(k=\epsilon2^jg/h\).  There is no legitimate step that deletes
this fibre or replaces its weights by a fixed divisor coefficient.

Taking absolute values after the bijection gives no saving: it is an
exact reindexing of the original tuples, with at most a divisor-factor
overcount if the recovery restrictions are relaxed.  Separately
summing fixed \((h,k,\rho)\) divisor bounds returns the already rejected
capacity \(NL_1L_2Q/D\), losing at least \(R\).  Therefore the first
analytic gap is a signed estimate for the complete low-two-adic
\((A,B,h)\)-sum (151.40), or a boundary-complete reciprocal B-process
whose square-root dual main sum is itself estimated.

The reciprocal power statements must also be scoped correctly.
Estimate (151.15) uses a graph-certified pair but applies only to the
square of the subrow \(L\le L_0\).  Estimate (151.59) is a
source-conditional candidate for the whole row, not an accepted graph
claim.  At \(D=1\),
the collar is the whole centered nonexact family, so subtracting its
exact and packet owners isolates its large wraps.  At \(D>1\), neither
whole-row cancellation nor the TTY subrow bound by itself bounds the
large-wrap collar term separately from the growing generic term.

## 5. Control tests and outcomes

1. **`literal_large_wrap_residual` -- pass.**  Equation (151.23)
   retains the two exact coefficients through (151.20)--(151.22), both
   profiles, both floor prefixes, every incidence mask, the common
   factor, imprimitive denominators, phase, parity, and character.

2. **`accepted_small_packet_exclusion` -- pass.**  Every new
   shifted-factor formula has \(k\notin\mathcal K_0\).  The high-adic
   set is intersected with that complement; the endpoint deductions
   subtract the accepted packet rather than recounting it.

3. **`two_adic_character_transfer` -- pass.**  Equations
   (151.27)--(151.33) prove the transfer for both signs of \(k\), odd
   and even \(N\), and every relation between \(j\) and \(\nu_2(N)\).
   The character is never applied unlawfully to an even shifted
   factor.

4. **`shifted_factor_positivity_and_recovery` -- pass.**  Positivity
   is (151.25)--(151.26); (151.34)--(151.39) give necessary and
   sufficient divisibility, sign, gcd, support, center, collar, packet,
   and recovery conditions.  The \(h\mid g\) fibre is explicit.

5. **`joint_k_rho_h_summation` -- pass/open split.**  Equation
   (151.40) is the exact joint all-shift reindexing before absolute
   values.  The TTY low-\(L\) subrow is summed before energy expansion,
   and every high-adic wrap is summed absolutely.  The low-adic
   residual outside those ranges remains open.  A Bourgain full-row
   summation is derived only as the source-conditional candidate
   (151.56)--(151.59).

6. **`high_two_adic_sparse_range` -- pass.**  Equations
   (151.41)--(151.44) prove the required all-scale target-safe range
   under the already accepted arbitrary-packet theorem.

7. **`D1_L1_reciprocal_scalar` -- pass/open split.**  The literal
   scalar, actual profile, exact character identity, and certified TTY
   threshold are (151.65)--(151.68).  Equations (151.69)--(151.69a)
   show that Theorem 4's direct window ends before the Bourgain target,
   while Theorem 6's global interface supplies the conditional
   candidate from \(M^{29}\gg R^{52}\).  Below
   \(M^{819}\asymp R^{1424}\), no direct accepted-pair bound here proves
   the scalar target.

8. **`tuple_absolute_signed_separation` -- pass.**  The wrap count
   (151.43) is raw capacity, (151.44) is coefficient-weighted absolute
   mass, and (151.23) and (151.40) are signed sums.  Equation (151.63)
   is a graph-certified-pair upper-bound ratio; (151.59) is a
   primary-source upper-bound ratio conditional on independent source
   correction.  Neither is a signed lower bound.

9. **`all_M_D_E_Q_L_h_k_rho_power_ledger` -- pass.**  The exact
   promoted corridor is (151.15), with its
   bounded/intermediate/top specializations.  Every \(L\le L_0\) is
   summed in (151.62).  Equations (151.55a)--(151.55c) distinguish the
   narrow direct theorem from the global exponent-pair theorem, and
   (151.56)--(151.59) give the exact conditional every-\(L\) corridor.
   The divisor \(h\), wrap \(k\), and shift \(\rho\) are never assigned
   a fictitious independent saving.

10. **`prime_parity_prefix_imprimitive_controls` -- pass.**  Even
    squarefree rows are represented by \(d=2m\); forced and excluded
    odd primes remain in \(F,P,z\); the exact prefixes remain in
    (151.22); common factors and imprimitive fractions remain in
    \(h,r_i\); and denominators dividing \(N\) are covered by the
    positivity argument.  The coprimality Mobius sum in the
    exponent-pair proof is exact.

11. **`generic_tge2_cross_and_downstream_scope` -- pass.**  At
    \(D>1\), the TTY reciprocal corridor is stated as a low-\(L\)
    subrow owner, not as an isolated collar estimate.  It excludes its
    cross and large-\(L\) complement.  The conditional Bourgain
    statement bounds the whole row and is likewise not an isolated
    collar bound at \(D>1\).  Outside the stated strict ranges, the
    growing generic complement, every \(t\ge2\) layer, the independent
    Round-138 cross owner, lower GAR, M9--M1, M9--M2, endpoint
    uniformity, M9, the bridge, the quarter target, and both global
    exponents are unchanged.

12. **Exponent-pair source and normalization control -- pass/open
    split.**  The Tao--Trudgian--Yang pair and fixed-BV
    restriction are already certified in graph nodes
    `M9-M1-TTY-exponent-pair-wedge` and
    `M9-M2-TTY-exponent-pair-wedge`.  It is used directly only when
    \(\mathcal T_c\ge Y_c\); the fixed comparable edge
    \(z_0\le\mathcal T_c/Y_c<1\) is closed by the uniform
    second-derivative bound (151.51b), which is dominated by the TTY
    majorant because \(997/1282>1/2\).  The primary paper's Theorem 4
    has the direct window (151.55a), whereas Section 5's (5.1) removes
    its lower cutoff and Theorem 6 explicitly removes the
    square-root-length and proper-subinterval restrictions by
    rescaling, the \(B\)-process, phase extension, and partial sums.
    Equation (151.55b) verifies the reciprocal derivative class, and
    (151.55c) is unweighted; actual BV enters only afterward through
    Abel.  The edge (151.51b) also fits the Bourgain shape because
    \(55/84>1/2\).  The remaining OPEN part of this control is independent
    correction of
    `Bourgain-2017-reciprocal-exponent-pair-source-audit`; until then
    (151.56)--(151.59) remain candidate rather than promoted.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The local derivation used exactly the selected context authorized by
the brief:

- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M1-lower-cone-t1-squarefree-moving-coefficient-small-wrap-reduction`,
  `M9-M1-lower-cone-t1-squarefree-large-wrap-collar-obstruction`,
  `M9-M1-TTY-exponent-pair-wedge`,
  `M9-M2-TTY-exponent-pair-wedge`, and
  `Bourgain-2017-reciprocal-exponent-pair-source-audit`;
- `state/active_campaign.yml`;
- `strategy/round151_large_wrap_shifted_factor_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/moving_coefficient_two_row_expansion_attack.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/conductor_round150_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/controls/conductor_round150_controls.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`.

For the one external theorem check, the primary source is Jean
Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
JAMS 30 (2017), Theorems 4 and 6 and the explanatory paragraphs in
Section 5, arXiv:1408.5794v2:
<https://arxiv.org/html/1408.5794v2#S5> and
<https://arxiv.org/pdf/1408.5794>.

The accepted inputs are the exact compressed row, the literal
two-row incidence expansion, the half-weight coefficient norm, the
arbitrary-packet fixed-wrap theorem, the Round-148 profile derivative
ledger, boundary ownership, exact-phase ownership, and the two
graph-certified TTY interfaces.  The character transfer,
full parity ledger, inverse recovery theorem, high-adic range,
uniform actual-profile variation deduction, present reciprocal
progression normalization, the TTY corridor power, and the distinction
between Bourgain's direct Theorem 4 range and its global Theorem 6
exponent-pair interface are derived here.

## 7. Recommended state effect

Close this task under

\[
 \boxed{\mathsf{strict\_large\_wrap\_character\_range}.}
\tag{151.71}
\]

Subject to independent algebra, source, and endpoint review, promote
as candidate mathematics:

1. the exact two-adic character identity (151.4), valuation ledger
   (151.28)--(151.31), and complete inverse recovery with its compulsory
   \(h\mid g\) fibre (151.34)--(151.40);
2. the all-scale target-safe high-two-adic wrap range
   (151.41)--(151.44);
3. the actual-profile bounded-variation statement (151.46) and the
   general coprime reciprocal exponent-pair placement
   (151.47)--(151.54);
4. the TTY low-\(L\) corridor
   \(M^{819}\gg R^{1424}D^{1816}L_0^{534}\), including the
   literal \(D=1,L=1\) scalar from
   \(M\gg R^{1424/819}\); and
5. conditional on independent correction of the Bourgain source node,
   the phase-class audit (151.55b)--(151.55c) and full-row corridor
   \(D^{84}R^{52}\ll M^{29}\) from (151.56)--(151.59), including
   \(M\gg R^{52/29}\) at \(D=1\) and \(D\ll R^{1/14}\) at
   \(M\asymp R^2\).

Retain as open the low-two-adic large-wrap sum (151.40) outside these
strict ranges, independent correction of the Bourgain source card, the
\(D>1\) separation of a whole-row bound from the growing generic
complement, the low/high-\(L\) cross complement outside the TTY
subrow, and any required boundary-complete B-process dual estimate.
Do not promote the full all-scale collar, any \(t\ge2\) layer, the
independent Round-138 cross term, lower GAR, M9--M1, M9--M2, endpoint
uniformity, M9, the bridge, the quarter target, or either global
exponent.

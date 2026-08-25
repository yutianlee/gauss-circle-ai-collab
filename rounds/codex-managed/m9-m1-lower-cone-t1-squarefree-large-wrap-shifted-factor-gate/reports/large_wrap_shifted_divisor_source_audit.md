# Round 151 primary-source audit: large wraps, shifted factors, and the reciprocal row

## 1. Result

The exact two-adic character transfer through the shifted factors is valid,
including both signs of (k) and both parities of (N).  It does **not**
remove the factor-level recovery data: after the transfer one must still retain
the exact two-adic valuation, congruences, common divisor, the divisor fibre
which reconstructs (h), the dyadic conditions on (q_i=hr_i), the prefixes,
and both sampled profiles.  Consequently none of the audited quadratic-divisor,
twisted additive-divisor, spectral shifted-convolution, or
Kloosterman-fraction theorems directly estimates the literal isolated
large-wrap residual.

There is, however, a source-verified **whole-row** alternative which is
strictly stronger than the classical ((1/6,2/3)) placement.  Write

\[
 V_{d,L,U}:=
 \|q\mapsto \mathscr W_{d,U}(L/q)\|_\infty+
 \operatorname {Var}_{q\asymp LQ}
       \mathscr W_{d,U}(L/q),
\tag{151.S1}
\]

and let (G_U^{\le L_0}(d)) denote the exact compressed row with (L\le
L_0).  If the **actual**, all-scale profiles satisfy

\[
 V_{d,L,U}\ll_\varepsilon X^\varepsilon
\quad(d\asymp D,\ L\le L_0),
\tag{151.S2}
\]

then Tao--Trudgian--Yang's primary-source exponent pair

\[
 (\kappa,\lambda)=
 \left(\frac{89}{1282},\frac{997}{1282}\right)
\tag{151.S3}
\]

gives

\[
 |G_U^{\le L_0}(d)|
 \ll_\varepsilon
 R^{997/641}D^{454/641}M^{-819/2564}
 L_0^{267/1282}X^\varepsilon
\tag{151.S4}
\]

and hence

\[
 \sum_{d\asymp D}\mu^2(d)|G_U^{\le L_0}(d)|^2
 \ll_\varepsilon R^2D X^\varepsilon
\tag{151.S5}
\]

through the exact power corridor

\[
 \boxed{\quad
 M^{819}\ \ge\ R^{1424}D^{1816}L_0^{534}.
 \quad}
\tag{151.S6}
\]

For a graph-level strict interior one should impose a fixed power of slack
in (151.S6), until the endpoint and profile ledger is printed.  At
(M\asymp R^2), (151.S6) becomes

\[
 D^{1816}L_0^{534}\le R^{214};
\tag{151.S7}
\]

in particular (L_0=1) permits (D\le R^{107/908}).  At (D=L_0=1)
it begins at (M\ge R^{1424/819}).

The corridor proposed by the conductor is therefore **algebraically
confirmed**, and the character and coprimality placements are source-legal.
It remains conditional only at the project-side all-scale BV seam (151.S2),
and it controls the square of the small-(L) row, not an arbitrary signed
subcollection of its expanded pairs.  The (L>L_0) square and the cross term
with (L\le L_0) are a named complement.

For comparison, Bourgain's primary-source pair

\[
 \left(\frac{13}{84},\frac{55}{84}\right)
\tag{151.S8}
\]

matches the inherited coefficient norm for **all** (L) and, subject to the
same all-scale BV statement, gives the narrower all-(L) corridor

\[
 D R^{13/21}\le M^{29/84},
 \qquad
 M\ge R^{52/29}D^{84/29},
 \qquad\Longleftrightarrow\qquad
 D^{84}R^{52}\le M^{29}.
\tag{151.S9}
\]

At (M\asymp R^2) it permits (D\le R^{1/14}).  The classical pair
((1/6,2/3)) gives only

\[
 D R^{2/3}\le M^{1/3},
 \qquad M\ge R^2D^3,
\tag{151.S10}
\]

which, under (M\le R^2) and (D\ge1), reaches only the top endpoint
(D=1,M\asymp R^2) and has no polynomial interior corridor.  No secondary
exponent-pair table is used in these comparisons.

Finally, a boundary-complete reciprocal (B)-process for the compulsory
(D=L=1) scalar returns a dual main sum of absolute capacity
(R M^{1/4}), with phase (e(\sqrt{N\ell})), amplitude
(N^{1/4}\ell^{-3/4}), and the two odd congruence classes recombined as
(\chi_4(\ell)).  Its error is target-safe under (151.S2), but its dual main
sum is the original lower-radial square-root wave and is neither an error nor
a gain.  Thus the literal isolated growing-(M) large-wrap collar remains
open outside the source-verified whole-row corridors above.

## 2. Exact statement and hypotheses

### 2.1 Frozen project object and coefficient interface

Throughout,

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,qquad
 DE\asymp M\le R^2,qquad D\le\sqrt M,
\tag{151.S11}
\]

and

\[
 Q=2\sqrt{ND/E}\asymp \frac{DR^2}{\sqrt M}.
\tag{151.S12}
\]

All supported (L,h,r) are odd.  The exact compressed (t=1) row is

\[
 G_U(d)=
 \sum_L\frac{\chi_4(L)B_{d,U}(L)}{L}
 \sum_{\substack{q\asymp LQ\\(q,L)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q),
\tag{151.S13}
\]

where the exact floor prefix is already contained in (B_{d,U}(L)) and is
constant in (q) once (d,L,U) are fixed.  The inherited coefficient norm is

\[
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}\ll_\varepsilon X^\varepsilon.
\tag{151.S14}
\]

The literal large-wrap atom is the corresponding part of the expansion of
(sum_d\mu^2(d)|G_U(d)|^2), with (q_i=hr_i),
((r_1,r_2)=1),

\[
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
\tag{151.S15}
\]

(k) outside the accepted (O(1+R^2/Q)) packet, and

\[
 0<|\rho|\le \frac{hr_1r_2}{D}.
\tag{151.S16}
\]

It retains both (B)-coefficients, both profiles and prefixes, every
incidence mask, and the signed atom

\[
 \chi_4(L_1L_2r_1r_2)
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
\tag{151.S17}
\]

The distinction used below is essential: (151.S5) bounds a recombined
positive row square.  It does not by itself bound the absolute value of an
arbitrary proper signed subset, such as the large-wrap collar alone.

### 2.2 Primary exponent-pair cards

**Tao--Trudgian--Yang.**  In Terence Tao, Tim Trudgian, and Andrew Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/pdf/2501.16779),
Definition 5 calls (F:[1,2]\to\mathbb R) a model phase when, for some fixed
(\sigma>0),

\[
 F^{(p+1)}(u)-\frac{d^p}{du^p}u^{-\sigma}=o(1)
\quad(p\ge0)
\tag{151.S18}
\]

uniformly in (u).  Definition 11 defines an exponent pair
((\kappa,\lambda)) by the estimate

\[
 \sum_{n\in I}e(TF(n/H))
 \ll (T/H)^{\kappa+o(1)}H^{\lambda+o(1)}
\tag{151.S19}
\]

for every interval (I\subset[H,2H]), every model phase, and
(T\ge H\ge1).  Lemma 12 gives the corresponding non-asymptotic
(\varepsilon)-form under finitely many uniform approximations in
(151.S18).  Theorem 20 states, in the primary paper itself, that
(151.S3) is an exponent pair.  Its coefficients are unit coefficients;
there is no character, modulus, coprimality restriction, main term,
exceptional spectrum, or endpoint term in the theorem.  Arbitrary interval
uniformity is printed in the definition, which is exactly what discrete Abel
summation needs.

For (Y=LQ), (A_0=NdL), and (T=A_0/Y=Nd/Q), the unweighted reciprocal
sum is in the source normalization.  The character may be resolved in either
of two exact ways.

First,

\[
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\quad(q\in\mathbb Z).
\tag{151.S20}
\]

After conjugation the normalized phase is

\[
 F_\pm(u)=-u^{-1}\mp c_Lu,
 \qquad
 c_L=\frac{Y}{4T}=\frac{LD}{dE}\asymp\frac LE.
\tag{151.S21}
\]

The linear twist disappears from all derivatives in (151.S18) with
(p\ge1), but for (p=0) it is an error (c_L).  Thus a naive assertion
that the direct linear twist is always in the Tao--Trudgian--Yang model
class is false when (L\asymp E).  In the small-(L) corridor (151.S6), it
is legal: since (E\asymp M/D),

\[
 \left(\frac{L_0D}{M}\right)^{534}
 \ll \frac{M^{285}}{R^{1424}D^{1282}}
 \le R^{-854},
\tag{151.S22}
\]

so (c_L=o(1)) uniformly for (L\le L_0).

Second, and without needing (151.S22), split (q) into the two residue
classes (1,3\pmod4).  After the coprimality decomposition (q=sn),
(s\mid L), write (n=4m+a), (a\in\{1,3\}), and put
(H=Y/(4s)).  After conjugation the normalized phase is

\[
 F_{s,a}(u)=-\frac1{u+a/(4H)}.
\tag{151.S23}
\]

Here (F_{s,a}'(u)=(u+a/(4H))^{-2}=u^{-2}+o(1)), uniformly because
(H\ge Q/4\gg R).  Hence (151.S23) is a model phase with (\sigma=2),
and this residue-class treatment retains (\chi_4) exactly for every (L).

**Bourgain.**  Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta
function*](https://arxiv.org/pdf/1408.5794), Theorem 6, states directly that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\tag{151.S24}
\]

is an exponent pair.  Section 3 treats smooth phases
(f(m)=TF(m/H)) under nonvanishing second, third, and fourth derivatives;
the reciprocal phase (151.S23) satisfies these hypotheses uniformly.
Section 5 explicitly treats both (H>\sqrt T), by the (B)-process, and
proper subintervals, by extending the phase and applying Sargos's lemma,
with only a logarithmic loss.  Thus the subinterval and Abel-transfer
requirements are printed in the primary paper, not imported from a
secondary exponent-pair table.  In particular, Theorem 4's intermediate
range (T^{17/42}\le H\le T^{1/2}) is **not** a hypothesis of Theorem 6:
Section 5 is precisely the argument that removes that restriction.  Any
local source card or graph node that carries Theorem 4's range into the
Theorem 6 exponent-pair statement must therefore be corrected.

For comparison, the classical (AB(0,1)=(1/6,2/3)) pair is also recorded
in the Tao--Trudgian--Yang primary paper.  Its use below is only a baseline;
no table of exponent pairs is used.

### 2.3 Primary shifted-divisor, spectral, and Kloosterman cards

**Quadratic divisor problem.**  Duke, Friedlander, and Iwaniec,
[*A quadratic divisor problem*, Theorem
1](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf),
Invent. Math. **115** (1994), 209--217, consider, for
(a,b\ge1), ((a,b)=1), and a nonzero shift (s),

\[
 D_f(a,b;s)=\sum_{am\pm bn=s}\tau(m)\tau(n)f(am,bn).
\tag{151.S25}
\]

Their weight is smooth in the two **product variables** and satisfies

\[
 x^iy^jf^{(i,j)}(x,y)
 \ll_{i,j}(1+x/X_0)^{-1}(1+y/Y_0)^{-1}P^{i+j}.
\tag{151.S26}
\]

The theorem supplies an explicit Ramanujan-series main term and error

\[
 O_\varepsilon\!left(
 P^{5/4}(X_0+Y_0)^{1/4}(X_0Y_0)^{1/4+\varepsilon}
 \right).
\tag{151.S27}
\]

Its coefficients are exactly (\tau(m)\tau(n)); it has no printed
(\chi_4), two-adic valuation, factor-recovery, prefix, moving sampled
profile, or many-shift averaging hypothesis.

**Character-twisted additive divisor problem.**  Alex Cowan,
[*A twisted additive divisor
problem*, Theorem 1.1](https://arxiv.org/pdf/2304.12572), assumes a positive
fixed shift (k_0), a rational prime modulus (p_0), even nontrivial
characters (\chi,\psi\pmod {p_0}) with (\chi\psi) nontrivial, nonzero
(u,v) with

\[
 |\Re u|+|\Re v|<\frac12,
\tag{151.S28}
\]

and all these parameters fixed while (Z\to\infty).  It evaluates

\[
 \sum_{n\le Z}
 \frac{\sigma_{2u}(n,\chi)\sigma_{2v}(n-k_0,\psi)}{n^{u+v}}
\tag{151.S29}
\]

as two explicit (L)-function/divisor main terms plus

\[
 O\!\left(
 Z^{1+|\Re u|+|\Re v|-
 \frac{1+2|\Re u|+2|\Re v|}
 {3+|\Re(u+v)|+|\Re(u-v)|}+\varepsilon}
 \right).
\tag{151.S30}
\]

The paper explicitly says the error suppresses dependence on every variable
other than (Z).  The project character (\chi_4) is odd and has composite
modulus (4); the project shifts (kh\rho) vary in sign and over a growing
family; and the project coefficients are not (151.S29).  Thus there is no
legal (R,M,D) power translation of this theorem.

**Spectral shifted convolution.**  Blomer and Harcos,
[*The spectral decomposition of shifted convolution
sums*, Theorem 1](https://arxiv.org/pdf/math/0703246), Duke Math. J.
**144** (2008), take two fixed cuspidal automorphic representations
(\pi_1,\pi_2) of (\mathrm{PGL}_2(\mathbb R)) of level one and weights
(W_1,W_2\) having the printed Sobolev norms (in particular total order
(18+2a+2b+4c)).  For fixed (h>0,Y>0) they give the exact full-spectrum
decomposition

\[
 \sum_{m+n=h}
 \frac{\lambda_{\pi_1}(|m|)\lambda_{\pi_2}(|n|)}{\sqrt{|mn|}}
 W_1(m/Y)W_2(n/Y)
 =\int_{\tau\ne\tau_0}
 \frac{\lambda_\tau(h)}{\sqrt h}W_\tau(h/Y)\,d\tau.
\tag{151.S31}
\]

For compact smooth weights this implies the familiar fixed-shift bound

\[
 \sum_{m\pm n=h}\lambda_{\pi_1}(|m|)\lambda_{\pi_2}(|n|)
 W_1(m/Y)W_2(n/Y)
 \ll h^{7/64}Y^{1/2}(hY)^\varepsilon.
\tag{151.S32}
\]

Remark 2 says arbitrary level introduces additional cusps and possible
complementary-series parameters (0<\nu_\tau\le7/64), together with a
factor ((\ell_1\ell_2)^{1/2+\varepsilon}) for
(\ell_1m\pm\ell_2n=h).  Those pieces are part of the source output and
cannot be deleted.  The project coefficient is not a pair of fixed cuspidal
Hecke sequences, its shifted relation is between products after recovery,
and no printed specialization supplies the odd level-four character,
factor-level weights, or the growing (k,h,\rho) average.

**Kloosterman fractions and determinants.**  Bettin and Chandee,
[*Trilinear forms with Kloosterman
fractions*, Theorem 1](https://arxiv.org/pdf/1502.00769), assume three
independent coefficient sequences on (a\asymp A,m\asymp M_1,n\asymp N_1),
((m,n)=1), and (\vartheta\ne0), and prove

\[
\begin{aligned}
 &\sum_{a,m,n}\nu_a\alpha_m\beta_n
 e(\vartheta a\bar m/n)\\
 &\quad\ll \|\nu\|_2\|\alpha\|_2\|\beta\|_2
 \left(1+\frac{|\vartheta|A}{M_1N_1}\right)^{1/2}
 \Bigl((AM_1N_1)^{7/20+\varepsilon}(M_1+N_1)^{1/4}\\
 &\hspace{52mm}+
 (AM_1N_1)^{3/8+\varepsilon}(AN_1+AM_1)^{1/8}\Bigr).
\end{aligned}
\tag{151.S33}
\]

Theorem 2 inserts a Jacobi symbol, not (\chi_4).  Corollary 1 treats one
fixed nonzero determinant
(m_1n_2-m_2n_1=\Delta), four separated weights, and derivative bounds
(f^{(j)}\ll\eta^jM_1^{-j}),
(g^{(j)}\ll\eta^jM_2^{-j}).  It has an explicit density main term and
error

\[
 O\!\left((\eta\mathcal R)^{3/2}\|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon\right),
\tag{151.S34}
\]

where
(\mathcal R=M_1N_2/(M_2N_1)+M_2N_1/(M_1N_2)).  It prints no aggregate
estimate over (\Delta).  The project profile
(\mathscr W_{d,U}(L/(hr))) already couples (L) and (r), and any formal
choice of an inverse residue from ((L,q)) makes the coefficient
graph-supported rather than (\nu_a\alpha_m\beta_n).

### 2.4 Primary boundary-complete (B)-process card

Lutsko, Sourmelidis, and Technau,
[*Pair correlation of the fractional parts of
\(\alpha n^\theta\)*, Theorem 1.3](https://ems.press/journals/jems/articles/14297682),
J. Eur. Math. Soc. **27** (2025), 4069--4082, state the following half-open
version.  If (\phi\in C^4[A,B)),

\[
 \Lambda\le\phi''(x)<\eta\Lambda,
 \quad |\phi'''(x)|<\frac{\eta\Lambda}{B-A},
 \quad |\phi''''(x)|<\frac{\eta\Lambda}{(B-A)^2},
\tag{151.S35}
\]

(a=\phi'(A)), (b=\phi'(B)), and (x_m) is the unique solution of
(\phi'(x_m)=m), then

\[
 \sum_{n\in[A,B)}e(\phi(n))
 =e(1/8)\sum_{m\in[a,b)}
 \frac{e(\phi(x_m)-mx_m)}{\sqrt{\phi''(x_m)}}
 +\omega_\phi(A,B),
\tag{151.S36}
\]

with

\[
 \omega_\phi(A,B)\ll
 \Lambda^{-1/2}+\eta^2\log(b-a+1).
\tag{151.S37}
\]

The half-open endpoint convention and the full dual main sum are printed in
the theorem.  The theorem is unweighted.  Uniform application to every
prefix of ([A,B)), followed by discrete Abel summation, gives the weighted
version with (151.S37) multiplied by
(\|w\|_\infty+\operatorname {Var}w), and with (w(x_m)) retained in the
dual main sum.  This is exactly where (151.S2) enters.  Olivier Robert's
primary paper [*On van der Corput's (k)-th derivative test for exponential
sums*, Theorem 4](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf)
gives a compatible classical (B)-transform under (C^3) hypotheses, but
its printed (\lambda_3)-error is weaker in the top project range; it is not
used to claim the target-safe error below.

## 3. Proof or derivation

### 3.1 Two-adic transfer, positivity, and recovery

For (k\ne0), put (j=\nu_2(|k|)), (k=2^j\kappa) with (\kappa) odd,
and

\[
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\tag{151.S38}
\]

Expansion and (151.S15) give

\[
 AB=N^2L_1L_2+kh\rho.
\tag{151.S39}
\]

The collar bounds give

\[
 |kh\rho|\ll\frac{NL_1L_2Q}{D},
 \qquad
 \frac{|kh\rho|}{N^2L_1L_2}ll\frac{Q}{DN}\ll1,
\tag{151.S40}
\]

so (A,B>0) for large (X).  Equivalently,

\[
 Ar_2=NL_2r_1+\rho,\qquad
 Br_1=NL_1r_2-\rho,
\tag{151.S41}
\]

which gives the same positivity directly.

Set

\[
 x=\frac{NL_1-A}{2^j}=\kappa hr_1,
 \qquad
 y=\frac{B-NL_2}{2^j}=\kappa hr_2.
\tag{151.S42}
\]

Both (x,y) are odd and have the same sign, including when (k<0).
Since squares of odd residues are (1\pmod4),

\[
\begin{aligned}
 \chi_4(L_1L_2xy)
 &=\chi_4(L_1L_2\kappa^2h^2r_1r_2)\\
 &=\chi_4(L_1L_2r_1r_2).
\end{aligned}
\tag{151.S43}
\]

This proves the proposed identity.  The parity ledger is:

* if (j\ge1), (A\equiv B\equiv N\pmod2);
* if (j=0), (A\equiv B\equiv1-N\pmod2);
* in both cases
  (\nu_2(NL_1-A)=\nu_2(B-NL_2)=j), so the quotients in
  (151.S42) are odd.

Thus the identity is independent of the parity of (N), but the exact
congruence conditions are not.

Recovery is not one-to-one.  From (x,y),

\[
 g=\gcd(|x|,|y|)=|\kappa|h,
 \qquad r_i=|x_i|/g,
\tag{151.S44}
\]

and ((r_1,r_2)=1).  The common sign recovers the sign of (k), but every
odd divisor (h\mid g) is initially possible, with

\[
 \kappa=\operatorname {sgn}(x)g/h,qquad
 k=2^j\kappa,qquad q_i=hr_i.
\tag{151.S45}
\]

For each such candidate one must reimpose (q_i\asymp L_iQ),
((L_i,q_i)=1), the exact profiles and prefixes, and

\[
 \rho=\frac{AB-N^2L_1L_2}{kh}\in\mathbb Z,
 \qquad 0<|\rho|\le hr_1r_2/D.
\tag{151.S46}
\]

This divisor fibre is the first coefficient mismatch in any theorem which
sees only the products (AB) and (L_1L_2).

There is one unconditional sparse two-adic gain.  The number of centered
wraps divisible by a power (2^J\gg R^2) is

\[
 \ll 1+\frac{N}{Q2^J}
 \ll1+\frac{R^2}{Q}.
\tag{151.S47}
\]

It is therefore owned by the accepted arbitrary-packet fixed-wrap theorem.
No shifted-divisor source is needed for that high-two-adic tail.

### 3.2 Character, coprimality, weights, and the exponent-pair corridor

Let

\[
 S_{d,L}(w)=
 \sum_{\substack{q\asymp Y\\(q,L)=1}}
 \chi_4(q)w(q)e(A_0/q),
 \qquad Y=LQ,\quad A_0=NdL.
\tag{151.S48}
\]

Because (L) is odd,

\[
 1_{(q,L)=1}=\sum_{s\mid(q,L)}\mu(s),
 \qquad \chi_4(sn)=\chi_4(s)\chi_4(n).
\tag{151.S49}
\]

For each (s\mid L), put (q=sn), split (n=4m+a) with
(a=1,3), and use (151.S23).  The source length is
(H\asymp Y/s) and its oscillation parameter remains

\[
 T=A_0/Y=Nd/Q.
\tag{151.S50}
\]

On the small-(L) corridor (T/H\asymp sE/L\gg1); for the residue split
the harmless factor (4) only improves this.  More exactly, using
(Q^2=4ND/E), the residue progression has

\[
 \frac{T}{H}=\frac{4sNd}{LQ^2}=\frac{s dE}{LD}
 \asymp \frac{sE}{L}.
 \tag{151.S50a}
\]

Throughout the full source support (L\le E), this is bounded below by a
positive absolute constant.  If the convention (d\asymp D) does not place
(d\ge D), replace (T,F) by (CT,F/C) for one fixed absolute constant (C)
determined only by the dyadic convention; then (CT\ge H), while every required normalized derivative
stays in the same compact nonvanishing class.  This verifies the formal
``(T\ge\hbox{length})'' hypothesis even at (L\asymp E).  Thus Bourgain's
Theorem 6 applies on the **full** (L)-range, not merely the small-(L)
corridor; the
bounded shift (a/(4H)) in (151.S23), arbitrary proper subintervals, and
the subsequent BV/Abel transfer are all uniform there.  The
Tao--Trudgian--Yang
interval estimate gives

\[
 \sum_{m\in I}e\!\left(\frac{A_0}{s(4m+a)}\right)
 \ll_\varepsilon
 (Nd)^\kappa L^{\lambda-\kappa}
 Q^{\lambda-2\kappa}s^{\kappa-\lambda}X^\varepsilon.
\tag{151.S51}
\]

The bound is uniform in every subinterval (I).  Since
(\lambda>\kappa),

\[
 \sum_{s\mid L}s^{\kappa-\lambda}\le\tau(L)\ll_\varepsilon X^\varepsilon.
\tag{151.S52}
\]

Discrete Abel summation therefore gives the exact weighted estimate

\[
 |S_{d,L}(w)|
 \ll_\varepsilon
 (\|w\|_\infty+\operatorname {Var}w)
 (Nd)^\kappa L^{\lambda-\kappa}
 Q^{\lambda-2\kappa}X^\varepsilon.
\tag{151.S53}
\]

This proves all three placement facts requested by the conductor:

1. (\chi_4) is retained exactly, either through (151.S20) in the strict
   small-(L) corridor or, more robustly, by the two residue classes;
2. ((L,q)=1) is inserted **before** the exponent-pair theorem and costs
   (s^{\kappa-\lambda}), not a positive power of (s);
3. weights require only the uniform subinterval theorem and the actual BV
   norm (151.S1); arbitrary bounded weights are not licensed.

Insert (151.S53) into (151.S13) and use (151.S14).  For (L\le L_0),

\[
 \frac{|B_{d,U}(L)|}{L}L^{\lambda-\kappa}
 =\frac{|B_{d,U}(L)|}{\sqrt L}
 L^{\lambda-\kappa-1/2}.
\tag{151.S54}
\]

For the pair (151.S3),

\[
 \lambda-\kappa=\frac{454}{641},\qquad
 \lambda-2\kappa=\frac{819}{1282},\qquad
 \lambda-\kappa-\frac12=\frac{267}{1282}.
\tag{151.S55}
\]

Thus

\[
 |G_U^{\le L_0}(d)|
 \ll_\varepsilon
 (Nd)^{89/1282}Q^{819/1282}
 L_0^{267/1282}X^\varepsilon.
\tag{151.S56}
\]

Using (N\asymp R^4), (d\asymp D), and (151.S12) gives exactly
(151.S4).  Squaring and summing (O(D)) rows gives

\[
 \sum_{d\asymp D}|G_U^{\le L_0}(d)|^2
 \ll_\varepsilon
 R^{1994/641}D^{1549/641}M^{-819/1282}
 L_0^{267/641}X^\varepsilon.
\tag{151.S57}
\]

Dividing by (R^2D) and clearing the denominator (1282) yields precisely
(151.S6).

For a general pair, the same calculation gives

\[
 |G_U^{\le L_0}(d)|
 \ll R^{2\lambda}D^{\lambda-\kappa}
 M^{\kappa-\lambda/2}
 L_0^{\max(0,\lambda-\kappa-1/2)}X^\varepsilon.
\tag{151.S58}
\]

Bourgain has (\lambda-\kappa=1/2), so (151.S14) sums all (L) with no
loss and (151.S58) gives (151.S9).  The classical pair also has
(\lambda-\kappa=1/2) and gives (151.S10).  The Tao--Trudgian--Yang pair
has the positive (L_0^{267/1282}) loss, which is why its stronger
one-dimensional cancellation produces a wider **small-(L)** corridor but
does not by itself replace the all-(L) Bourgain corridor.

### 3.3 Exact translation of the shifted-source interfaces

With (151.S38)--(151.S39), the formal Duke--Friedlander--Iwaniec dictionary
is

\[
 a=1,\quad m=AB,\quad b=N^2,\quad n=L_1L_2,
 \quad s=kh\rho,
\tag{151.S59}
\]

using the minus sign in (151.S25).  Put
(Z=N^2L_1L_2).  Both source product scales are (X_0\asymp Y_0\asymp Z),
so (151.S27) becomes

\[
 P^{5/4}Z^{3/4+\varepsilon}
 =P^{5/4}N^{3/2}(L_1L_2)^{3/4+\varepsilon}.
\tag{151.S60}
\]

Already at (L_1=L_2=1) this is (R^{6+o(1)}), before any shift sum,
whereas (R^2D\le R^3).  More fundamentally, replacing the exact
factorizations by (\tau(AB)\tau(L_1L_2)) would erase (151.S42)--(151.S46),
the transferred character, and both profiles.  The source weight
(f(AB,N^2L_1L_2)) cannot encode these factor-level data while satisfying
(151.S26).  The algebraic dictionary is exact; the coefficient, smoothness,
shift-family, and power hypotheses all fail after it.

Cowan's theorem fails earlier: (\chi_4) is odd of composite modulus, its
generalized divisor coefficients do not equal the project coefficients, and
its shift and every non-(Z) parameter are fixed.  No limiting choice
(u=v=0) is printed in the theorem.  Hence its error exponent cannot be
inserted into the project ledger.

Blomer--Harcos also fails before a power comparison.  There is no legal map
from the recovery-weighted factorizations (A,B,L_1,L_2) to two fixed cusp
Hecke sequences in one additive equation.  At level four the source itself
requires the additional cusps and complementary terms in Remark 2; an odd
(\chi_4) specialization is not printed.  Treating the spectral integral as
an error or suppressing the (h^{7/64}) factor would both be illegal.

For Bettin--Chandee, the real project phase is
(e(d\rho/(hr_1r_2))), with potentially imprimitive numerator and
denominator.  Formally choosing a residue (m) with
(mL\equiv1\pmod q) makes (m) a joint function of ((L,q)); the amplitude
is then supported on a graph rather than a product of the three independent
sequences in (151.S33).  In the determinant formulation, the project ranges
over every (\delta), equivalently every admissible ((k,\rho)), while
Corollary 1 fixes one (\Delta) and has an explicit main term.  The coupled
profile is not one of its two smooth separated weights.  The Jacobi symbol
in Theorem 2 does not repair any of these mismatches and is not the literal
(\chi_4) in (151.S17).

The joint-shift capacity confirms why pointwise source bounds are
insufficient.  Uniformly on the collar,

\[
 |k|\ll N/Q,\qquad
 0<|\rho|\ll \frac{L_1L_2Q^2}{hD},
\tag{151.S61}
\]

and separate divisor recovery at fixed ((L_i,h,k,\rho)), even at
(X^\varepsilon) cost, sums to

\[
 \frac{NL_1L_2Q}{D}X^\varepsilon.
\tag{151.S62}
\]

Its ratio to the trivial (L_1L_2Q^2) denominator-pair capacity is

\[
 \frac{N}{DQ}\asymp\frac{R^2\sqrt M}{D^2}\ge R.
\tag{151.S63}
\]

Similarly, summing the accepted (DQX^\varepsilon) fixed-wrap estimate
over (N/Q) wraps gives (DN=R^4D), a factor (R^2) above target.  These
are positive capacities, not lower bounds for the signed sum.

### 3.4 The exact (D=1,L=1) reciprocal transform

Let

\[
 S=\sum_{q\in[A,B)}\chi_4(q)w(q)e(N/q),
 \qquad A,B\asymp Q,
\tag{151.S64}
\]

where (w(q)=\mathscr W_{1,U}(1/q)) includes the actual dyadic profile.
Using (151.S20), write (S=(S_+-S_-)/(2i)) with

\[
 \phi_\sigma(q)=\frac Nq+\frac{\sigma q}{4},
 \qquad \sigma\in\{1,-1\}.
\tag{151.S65}
\]

On (q\asymp Q),

\[
 \phi_\sigma''(q)=\frac{2N}{q^3},\quad
 \phi_\sigma'''(q)=-\frac{6N}{q^4},\quad
 \phi_\sigma''''(q)=\frac{24N}{q^5}.
\tag{151.S66}
\]

Thus (151.S35) holds with
(\Lambda\asymp N/Q^3) and (\eta\asymp1).  If
(m=\phi_\sigma'(q)), set

\[
 \ell=\sigma-4m>0.
\tag{151.S67}
\]

Then (\ell\equiv\sigma\pmod4), and the critical point, critical action,
and stationary amplitude are

\[
 q_\ell=2\sqrt{N/\ell},\qquad
 \phi_\sigma(q_\ell)-mq_\ell=\sqrt{N\ell},\qquad
 \frac1{\sqrt{\phi_\sigma''(q_\ell)}}
 =2N^{1/4}\ell^{-3/4}.
\tag{151.S68}
\]

Applying (151.S36) uniformly to prefixes and then Abel summation gives

\[
\begin{aligned}
 S={}&e(-1/8)N^{1/4}
 \sum_{\substack{\ell\in(4N/B^2,,4N/A^2]\\\ell\ {
m odd}}}
 \chi_4(\ell)\ell^{-3/4}
 w\!\left(2\sqrt{N/\ell}\right)e(\sqrt{N\ell})\\
 &+O\!\left(
 (\|w\|_\infty+\operatorname {Var}w)
 \left(\frac{Q^{3/2}}{\sqrt N}+\log\left(2+\frac N{Q^2}\right)\right)
 \right).
\end{aligned}
\tag{151.S69}
\]

The unit (e(-1/8)) is exact: the (\ell\equiv1\pmod4) branch has that
unit, while the outer minus sign on the
(\ell\equiv-1\pmod4) branch supplies (\chi_4(\ell)=-1).
The interval in (151.S69) is the image of the source's half-open interval
([\phi'(A),\phi'(B))); no dual endpoint has been silently discarded.

At (D=1), (E\asymp M),

\[
 Q\asymp\frac{R^2}{\sqrt M},\qquad
 \ell\asymp\frac{4N}{Q^2}\asymp M.
\tag{151.S70}
\]

Under (151.S2), the error in (151.S69) is

\[
 \ll_\varepsilon
 \left(RM^{-3/4}+\log(M+2)\right)X^\varepsilon
 \ll_\varepsilon RX^\varepsilon.
\tag{151.S71}
\]

The dual main sum, however, has absolute capacity

\[
 N^{1/4}\sum_{\ell\asymp M}\ell^{-3/4}
 \asymp RM^{1/4}.
\tag{151.S72}
\]

It is the lower-radial square-root phase with the same mod-four character.
At (M\asymp R^2) the original (q)-sum already has length
(Q\asymp R), while (151.S72) is (R^{3/2}); the equality (151.S69)
therefore forces cancellation in the dual main sum rather than making that
main sum an error.  A second transform merely returns the original scale.

### 3.5 Whole-row versus isolated-collar scope

The exponent-pair argument estimates (G_U^{\le L_0}(d)) before the square
is expanded.  Therefore it controls, in one recombined object, all
denominator pairs, all centered wraps, the collar and the generic part of
that **small-(L), (t=1)** row square.  It is a legitimate route to a
parent whole-row obligation if the graph permits that recombination.

It does not imply

\[
 |\mathcal C_U^{\rm lw}|\le
 \sum_d|G_U^{\le L_0}(d)|^2,
\tag{151.S73}
\]

because a proper signed subset of cross terms can be larger than the fully
recombined nonnegative square and cancel against its complement.  Nor does
the Tao--Trudgian--Yang bound control (G_U^{>L_0}) or the cross term
(G_U^{\le L_0}\overline{G_U^{>L_0}}).  Bourgain removes the (L_0)
seam only in its narrower corridor (151.S9).  No result here reaches a
(t\ge2) layer or the independent Round-138 cross owner.

## 4. First doubtful or unproved step

For the source-verified whole-row corridor, the first unproved project step
is the all-scale literal profile statement (151.S2).  The inherited material
records bulk logarithmic derivative scale (O_j(1)), radial-transition
scale (O_j(M^{j/2})) over relative width (O(M^{-1/2})), and
cone-transition scale (O_j(D^{j/2})) over relative width
(O(D^{-1/2})), with finitely many transitions.  Those scales strongly
suggest bounded first variation.  But the permitted reports do not print the
complete factor-by-factor growing-(M) amplitude, the exact number and size
of every hard jump, or the uniform total variation.  The exponent-pair
theorem does not supply this missing coefficient lemma.

After (151.S2), the first seam specific to (151.S6) is the named
(L>L_0) square and small/large-(L) cross term.  If instead the objective
is the literal isolated large-wrap collar rather than the recombined row,
the first remaining step is a joint signed ((h,k,\rho)) estimate which
retains the recovery fibre (151.S44)--(151.S46); none of the shifted sources
audited here supplies it.

For the (B)-process route, (151.S69) is boundary-complete, but the first
unproved step is a target-sized estimate of its dual main sum.  Calling that
sum an error would be the first invalid step.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `literal_large_wrap_residual` | **Pass as identification; open as an estimate.** The object keeps both coefficients, profiles, prefixes, masks, common factors, nonzero (\rho), the phase, and (\chi_4).  No whole-row bound is misreported as a bound for the isolated residual. |
| `two_adic_character_transfer` | **Pass.** Equations (151.S42)--(151.S43) prove the identity for (k>0) and (k<0), (j=0) and (j\ge1), and both parities of (N). |
| `shifted_factor_positivity_and_recovery` | **Pass/open split.** Positivity and (151.S39) pass.  The exact recovery fibre (h\mid g), dyadic conditions, divisibility, and valuation constraints remain and are the first factor-source seam. |
| `joint_k_rho_h_summation` | **Fail for the collar target.** Pointwise divisor recovery sums to (151.S62), and fixed-wrap summation loses (R^2).  No audited source provides the needed aggregate signed saving. |
| `D1_L1_reciprocal_scalar` | **Pass as an exact transform; no gain.** Formula (151.S69) retains the actual weight and produces the capacity (RM^{1/4}). |
| `exact_character_fourier_identity` | **Pass.** Equation (151.S20) holds for every integer, including the automatic zero on even (q).  The direct Tao--Trudgian--Yang phase is legal only when (L/E=o(1)); residue classes give an unconditional exact placement. |
| `boundary_complete_B_process` | **Pass conditional on BV.** The source half-open endpoints, dual main sum, weight, transition error, and stationary amplitude all appear in (151.S69). |
| `actual_profile_derivative_ledger` | **Open at growing (M).** The scale/width data are compatible with (O(X^\varepsilon)) variation, but the complete literal factor and hard-boundary ledger is not present. |
| `dual_self_return_vs_gain` | **Pass as a no-gain diagnosis.** The dual is (e(\sqrt{N\ell})) with (\chi_4(\ell)), and its absolute capacity is (RM^{1/4}). |
| `tuple_absolute_signed_separation` | **Pass.** Equations (151.S62)--(151.S63) and (151.S72) are upper capacities only; no signed lower bound is inferred. |
| `source_theorem_large_wrap_match` | **No direct isolated-collar match.** DFI fails at factor weights and power; Cowan at character, coefficient, modulus, and fixed parameters; Blomer--Harcos at automorphic coefficients and spectral/level terms; Bettin--Chandee at independence, inverse phase, and fixed determinant.  The exponent-pair result is instead a conditional whole-row theorem. |
| `all_M_D_E_Q_L_h_k_rho_power_ledger` | **Pass.** Equations (151.S4)--(151.S10), (151.S40), (151.S47), (151.S57), and (151.S61)--(151.S72) retain every requested scale.  The conductor's (M^{819}) corridor is confirmed exactly. |
| `prime_parity_prefix_imprimitive_controls` | **Pass.** Even squarefree (d), primes in the odd part of (d), either parity of (N), (q\mid N), imprimitive reciprocal fractions, and common (h) are not deleted.  The exact prefix stays in (B_{d,U}(L)), independent of (q). |
| `generic_tge2_cross_and_downstream_scope` | **Pass with narrow recombination scope.** The small-(L) row bound includes the generic (t=1) pairs only in the recombined square; it does not separately estimate them.  Every (t\ge2) layer, the Round-138 cross, lower GAR, M9--M1/M2 completion, the bridge, quarter target, and exponent statements remain untouched. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts used were exactly the task brief and its permitted
context, plus the conductor-directed Tao--Trudgian--Yang source card:

* `protocol.md`;
* `state/proof_obligations.yml`, only for the relevant active records;
* `state/active_campaign.yml`;
* `strategy/round151_large_wrap_shifted_factor_strategy.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/briefs/large_wrap_shifted_divisor_source_audit.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/barrier_packet.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/variable_row_collar_source_audit.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/source_conductor_round150_final.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/squarefree_progression_source_audit.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
* `sources/tao_trudgian_yang_2025.md`.

Primary technical sources inspected were:

* Tao, Trudgian, and Yang,
  [*New exponent pairs, zero density estimates, and zero additive energy
  estimates: a systematic approach*](https://arxiv.org/pdf/2501.16779),
  Definition 5, Definition 11, Lemma 12, and Theorem 20;
* Bourgain,
  [*Decoupling, exponential sums and the Riemann zeta
  function*](https://arxiv.org/pdf/1408.5794), Theorem 6 and Sections 3 and 5;
* Duke, Friedlander, and Iwaniec,
  [*A quadratic divisor problem*](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf),
  Theorem 1;
* Cowan,
  [*A twisted additive divisor problem*](https://arxiv.org/pdf/2304.12572),
  Theorem 1.1;
* Blomer and Harcos,
  [*The spectral decomposition of shifted convolution
  sums*](https://arxiv.org/pdf/math/0703246), Theorem 1 and Remark 2;
* Bettin and Chandee,
  [*Trilinear forms with Kloosterman
  fractions*](https://arxiv.org/pdf/1502.00769), Theorems 1--2 and Corollary 1;
* Lutsko, Sourmelidis, and Technau,
  [*Pair correlation of the fractional parts of
  \(\alpha n^\theta\)*](https://ems.press/journals/jems/articles/14297682),
  Theorem 1.3 and Lemma 1.4;
* Robert,
  [*On van der Corput's (k)-th derivative test for exponential
  sums*](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
  Theorem 4.

No secondary exponent-pair table or secondary technical theorem statement
is used.  No shared proof state, validation matrix, synthesis, or proof draft
was edited.

## 7. Recommended state effect

**Retain and revise; do not mark the isolated large-wrap collar proved.**

1. Retain the exact shifted-factor identity, positivity, two-adic character
   transfer, parity ledger, recovery fibre, and sparse high-two-adic packet as
   candidate mathematics.
2. Record the source-verified analytic implication
   ((151.S2)\Rightarrow(151.S4)\Rightarrow(151.S5)) and the exact
   Tao--Trudgian--Yang corridor (151.S6).  It is the strongest
   primary-source one-dimensional pair audited here for this small-(L)
   reciprocal objective and strictly improves the classical and Bourgain
   small-(L) ranges.
3. Do not promote (151.S5) to an unconditional lemma until the complete
   growing-(M) profile BV proof is supplied.  Name the (L>L_0) square and
   small/large-(L) cross term as the complement of the wider corridor.
4. Separately record Bourgain's narrower all-(L) conditional corridor
   (151.S9).  It avoids the (L_0) complement because
   (\lambda-\kappa=1/2), but it has the same actual-profile BV seam.
5. Retain the DFI, Cowan, Blomer--Harcos, and Bettin--Chandee conclusions
   only as precise direct-specialization no-matches.  They are not a
   literature impossibility theorem.
6. Retain (151.S69) as the boundary-complete (D=L=1) transform and record
   its (RM^{1/4}) dual self-return as a no-gain result.  Do not absorb the
   dual main sum into the error.
7. Leave open the literal isolated growing-(M) large-wrap signed sum, every
   uncombined generic complement, every (t\ge2) layer, the Round-138 cross
   owner, all remaining M9--M1/M2 and downstream obligations, and both final
   exponent statements.

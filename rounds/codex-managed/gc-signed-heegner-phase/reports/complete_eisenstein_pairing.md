# Round228 complete Eisenstein pairing

## 1. Result

Candidate evidence only. Campaign `gc-signed-heegner-phase`, task
`complete_eisenstein_pairing`, NONBLIND discovery role, 2026-09-28.
Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

The ENTIRE continuous component of the reviewed level-one/level-two
Heegner formula satisfies the sufficient raw bound

\[
 \boxed{\left|\mathcal C_{N,T}(R)\right|
 \ll_{\epsilon,J} A_J(N)^2N^{3/2}T^\epsilon.}                 \tag{1}
\]

This includes both level-two cusps, the level-one cusp, every shift,
every two-adic descendant, both spectral signs, all real radii in the
frozen range, and the entire low and high spectral tails. Indeed the
same bound holds with absolute values inside the spectral integral and
outside each shift. This is a component estimate, not a bound for the
whole remainder or a new circle exponent.

The improvement over the previous continuous local-Weyl certificate
comes from the exact CM identities

\[
 E^{(1)}(i,s)=\frac{2\zeta(s)L(s,\chi_4)}{\zeta(2s)},\qquad
 E^{(2)}_\infty(z_2,s)=E^{(2)}_0(z_2,s)
 =\frac{E^{(1)}(i,s)}{1+2^s},\quad z_2=\frac{-1+i}{2},       \tag{2}
\]

and their mean square of order \(U^{1+\epsilon}\), rather than the
generic local-Weyl order \(U^2\). The needed degree-two mean square is
proved below. The one additional primary work supplies only an explicit
reciprocal-zeta bound on the line of real part one.

The ENTIRE remaining cusp component is the exact expression (5) below.
Its inherited positive spectral certificate is \(A^2TN^{2+\epsilon}\);
the original arithmetic identity now caps its total by
\(A^2N^{2+\epsilon}\). Reaching quarter at \(N\asymp T\) still requires
a factor \(T^{1/2}\) beyond that cap. No whole-wave gain is established.

## 2. Exact statement and hypotheses

Use the frozen interface literally: \(T\ge2\), \(cT\le R\le CT\) real,
dyadic \(2\le N\le P<2T^{3/2}\), fixed smooth cutoffs and the actual real
Schwartz function \(\Psi\), which need not be positive. Write
\(A=(1+N/T)^{-J}\) and

\[
 g(x)=(x/N)^{-3/4}\Psi(\sqrt{x/T})w(x/N),\qquad
 W_h(x)=g(x+h)g(x)e(R(\sqrt{x+h}-\sqrt x)),
\]
\[
 H_h(t)=4\pi\int_0^\infty W_h(hu)
                      P_{-1/2+it}(1+2u)\,du,\qquad
 \alpha_h=1-h/(2N).
\]

For \(h=2^kh_0\), \(h_0\) odd, the exact continuous Hecke polynomials are

\[
 L_{1,h}(t)=4\sum_{a=0}^{k-2}(-1)^a
       \sqrt{h/2^{a+2}}\,\eta_t(h/2^{a+2}),\qquad
 L_{2,h}(t)=2\varepsilon_k\sqrt{h_0}\,\eta_t(h_0),           \tag{3}
\]

where the first sum is empty for \(k<2\),
\(\varepsilon_0=1\), \(\varepsilon_k=(-1)^{k-1}\) for \(k\ge1\), and
\(\eta_t(m)=\sum_{ab=m}(a/b)^{it}\). Set
\(V_q^{\rm cts}(t)=\sum_{1\le h<2N}\alpha_hL_{q,h}(t)H_h(t)\).
The complex continuous component in (1) is

\[
 \mathcal C=\frac1{4\pi}\sum_{q=1,2}\sum_{\mathfrak a\ {\rm cusp}}
    \int_{\mathbb R}|E_{\mathfrak a}^{(q)}(z_q,\tfrac12+it)|^2
                          V_q^{\rm cts}(t)\,dt.           \tag{4}
\]

There is one cusp for \(q=1\) and exactly two for \(q=2\).
Eisenstein series have the usual width-one incoming term \(y^s\)
and the spectral measure is \(dt/(4\pi)\), with hyperbolic area measure.
For the cusp zero of level two choose the determinant-one scaling matrix
\(W_2=\bigl(\begin{smallmatrix}0&-1/\sqrt2\\\sqrt2&0\end{smallmatrix}\bigr)\).
This specification matters for the factors in (2).

With the reviewed discrete Hecke polynomials obtained by replacing
\(\eta_t\) in (3) by the corresponding Hecke eigenvalue, define

\[
 \mathcal D=\sum_{q=1,2}\sum_{j\ne0}|u_j^{(q)}(z_q)|^2
       \sum_{1\le h<2N}\alpha_hL_{q,h}(j)H_h(t_j).         \tag{5}
\]

All old and new cusp modes, parities, exceptional parameters if present,
and all spectral heights belong to (5). The already reviewed
whole-functional identity says

\[
 \mathcal D+\mathcal C=
 \sum_{h<2N}\alpha_h(C_h-\rho_h I_h),\qquad
 \mathscr R=2\Re(\mathcal D+\mathcal C).                  \tag{6}
\]

It holds before taking the real part because each underlying orbit and
parity identity applies to complex tests. The constant mode is precisely
\(\rho_h I_h\), and the zero atom vanishes for these tests.

The only new external estimate is the final assertion of Corollary 4
in Nicol Leong, *Explicit estimates for the logarithmic derivative and
the reciprocal of the Riemann zeta function*,
[arXiv:2405.04869v5, 30 January 2026, Section 2.3, PDF page 4](https://arxiv.org/html/2405.04869v5#S2.SS3):
on the line \(\sigma=1\), for real \(v\ge2\),
\(|1/\zeta(1+iv)|\le29.388\log v\).
Here its argument is \(v=2|t|\), so the hypothesis holds for \(|t|\ge1\).
Conjugation handles negative \(t\). No RH premise or estimate to the left
of that line is used. HTML and extracted exact-version PDF agree on this
assertion; no independent audit of the source's entire proof is claimed.

## 3. Proof and derivation

### Exact CM values, cusps, and local factors

Initially let \(\Re s>1\). The standard level-one series is

\[
 E(z,s)=\frac12\sum_{(c,d)=1}\frac{y^s}{|cz+d|^{2s}}.
\]

At \(z=i\), removing the common gcd in all nonzero lattice vectors gives

\[
 E(i,s)=\frac1{2\zeta(2s)}\sum_{n\ge1}r_2(n)n^{-s}
       =\frac{2F(s)}{\zeta(2s)},\qquad
 F(s)=\zeta(s)L(s,\chi_4)=\sum_{n\ge1}a(n)n^{-s},
 \quad a(n)=r_2(n)/4.                                   \tag{7}
\]

This uses the exact identity \(a(n)=\sum_{d\mid n}\chi_4(d)\).
For level two, restricting the primitive lower row to even \(c\) gives
\(E_\infty^{(2)}\). Splitting the primitive rows of \(E(2z,s)\) according
to whether \(d\) is odd or even gives exactly

\[
 E(2z,s)=2^sE_\infty^{(2)}(z,s)
             +2^{-s}\{E(z,s)-E_\infty^{(2)}(z,s)\}.
\]

For even \(d\), \(c\) is odd, and extracting the factor two leaves the
primitive rows with odd lower-left entry. There is no additional gcd
or index multiplicity. Consequently

\[
 E_\infty^{(2)}(z,s)=\frac{2^sE(2z,s)-E(z,s)}{2^{2s}-1},\qquad
 E_0^{(2)}(z,s)=\frac{2^sE(z,s)-E(2z,s)}{2^{2s}-1}.        \tag{8}
\]

The second identity follows by applying \(W_2\), since
\(E(-1/z,s)=E(z,s)\). Now
\(z_2=-1/(i+1)\) and \(2z_2=i-1\), hence
\(E(z_2,s)=E(2z_2,s)=E(i,s)\). Formula (2) follows and continues
meromorphically to the critical line. At that line
\(|1+2^s|\ge\sqrt2-1\), so the cancellation in (8) introduces no pole.

For completeness the full Euler factors in the convergent half-plane are

\[
 E(i,s)=2(1+2^{-s})
           \prod_{p\equiv1\ (4)}\frac{1+p^{-s}}{1-p^{-s}},\qquad
 E_\infty^{(2)}(z_2,s)=E_0^{(2)}(z_2,s)
       =2^{1-s}\prod_{p\equiv1\ (4)}\frac{1+p^{-s}}{1-p^{-s}}. \tag{9}
\]

At inert odd primes the factor from \(F(s)\) is cancelled by
\(1/\zeta(2s)\); at two the factors are exactly those displayed.
These products are not asserted to converge on the critical line.
Their continued forms are (2). The residue check at \(s=1\) is
\(\operatorname{res}E(i,s)=3/\pi\) and
\(\operatorname{res}E_\infty^{(2)}(z_2,s)
=\operatorname{res}E_0^{(2)}(z_2,s)=1/\pi\), agreeing with the
inverse areas \(v_1^{-1}\) and \(v_2^{-1}\).

Writing \(s=1/2+it\), the complete densities are therefore

\[
 B_1(t)=\sum_{\mathfrak a\ {\rm of}\ 1}|E_\mathfrak a^{(1)}(i,s)|^2
       =\frac{4|F(s)|^2}{|\zeta(2s)|^2},\qquad
 B_2(t)=\frac{2B_1(t)}{|1+2^s|^2}.                        \tag{10}
\]

The two cusp values being equal does not remove one cusp from the
spectral measure: the factor two in (10) is essential.

### A self-contained degree-two mean square

For every \(\epsilon>0\) and \(U\ge2\),

\[
 \int_U^{2U}|F(\tfrac12+it)|^2dt\ll_\epsilon U^{1+\epsilon}.
                                                                  \tag{11}
\]

Here is a proof that also records the conductor, root number, dual
length and the gamma transition. Let
\(\vartheta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y}\).
Gaussian Poisson summation gives
\(\vartheta(y)^2=y^{-1}\vartheta(1/y)^2\). Mellin integration, initially
in \(\Re s>1\), followed by splitting at one gives

\[
 \Lambda(s):=\pi^{-s}\Gamma(s)F(s)
 =\frac14\left\{\frac1{s-1}-\frac1s+
    \int_1^\infty(\vartheta(y)^2-1)
                  (y^{s-1}+y^{-s})\,dy\right\}.          \tag{12}
\]

Thus \(\Lambda(s)=\Lambda(1-s)\), with residues \(1/4\) at one and
\(-1/4\) at zero. This is the fixed discriminant \(-4\), degree-two
functional equation, root number \(+1\). Its analytic conductor at
height \(U\) is comparable to \(U^2\); both balanced sums have natural
length comparable to \(U/\pi\), not a conductor-free length.

Take \(G(w)=e^{w^2}\), \(\gamma(s)=\pi^{-s}\Gamma(s)\), and define

\[
 V_s(n)=\frac1{2\pi i}\int_{(2)}
    G(w)\frac{\Gamma(s+w)}{\Gamma(s)}(\pi n)^{-w}\frac{dw}{w},
 \qquad X(s)=\pi^{2s-1}\frac{\Gamma(1-s)}{\Gamma(s)}.       \tag{13}
\]

Shifting the contour in
\((2\pi i)^{-1}\int_{(2)}\Lambda(s+w)G(w)dw/w\) to the line \(-2\),
then substituting \(w\mapsto-w\) and using (12), gives the exact identity

\[
 F(s)=\sum_{n\ge1}a(n)n^{-s}V_s(n)
       +X(s)\sum_{n\ge1}a(n)n^{s-1}V_{1-s}(n)-P(s),       \tag{14}
\]
\[
 P(s)=\frac1{4\gamma(s)}
        \left\{\frac{G(1-s)}{1-s}+\frac{G(s)}s\right\}.
\]

Both pole terms have been retained. On the critical line
\(|X(s)|=1\), and \(P(s)\ll_B(1+|t|)^{-B}\) for each fixed \(B\).
The exponentially decaying \(G\) makes the contour shifts legitimate;
the only poles of \(\Lambda\) crossed are zero and one, together with
the explicit \(1/w\) pole.

For fixed \(b>0\), \(U\le |t|\le2U\), and real \(v\), the elementary
gamma bound, including the region \(t+v\) near zero, is

\[
 \left|\frac{\Gamma(1/2+it+b+iv)}{\Gamma(1/2+it)}\right|
 \ll_b U^b(1+|v|)^b e^{\pi|v|/2}.                       \tag{15}
\]

Indeed Stirling with \(1+|\Im z|\) gives the numerator bound
\(O_b((1+|t+v|)^b e^{-\pi|t+v|/2})\), the denominator has size
comparable to \(e^{-\pi|t|/2}\), and the triangle inequality finishes
the estimate. For bounded \(t+v\) the numerator is bounded because its
real part is positive. Thus no large-argument expansion is imposed at
the gamma transition. The same argument treats \(1-s\) and negative
\(t\). All orders below are fixed as functions of the desired epsilon
or tail accuracy.

Shifting (13) to \(\Re w=B>0\), without crossing a pole, gives
\(V_s(n)\ll_B(U/n)^B\). For any fixed small \(\delta>0\), both sums
in (14) can therefore be truncated at
\(L=\lceil U^{1+\delta}\rceil\), with error \(O_D(U^{-D})\), by choosing
\(B\) sufficiently large. Explicitly the tail is at most
\(O(U^B L^{1/2+\eta-B})\), since \(a(n)\le d(n)\ll_\eta n^\eta\).

For an arbitrary finite polynomial \(Q(t)=\sum_{n\le L}b_nn^{-it}\)
and any real \(a\), direct integration yields

\[
 \int_a^{a+U}|Q(t)|^2dt
 \ll (U+L\log(2L))\sum_{n\le L}|b_n|^2.                 \tag{16}
\]

For the off-diagonal terms use
\(|\int_a^{a+U}(m/n)^{it}dt|\le2/|\log(m/n)|\),
\(1/|\log(m/n)|\le L/|m-n|\), and
\(2|b_mb_n|\le|b_m|^2+|b_n|^2\); the harmonic sum is \(O(\log(2L))\).
This proves (16) without a large-sieve import or any restriction on the
starting point \(a\).

In the finite first sum of (14), use the contour \(\Re w=b\), with
\(b>0\) small. Its polynomial on that contour has coefficients
\(a(n)n^{-1/2-b}\) and parameter \(t+v\). Minkowski, (15), and the
integrability of
\(|G(b+iv)|(1+|v|)^b e^{\pi|v|/2}/|b+iv|\) give its squared mean at most

\[
 \ll_b U^{2b}(U+L\log(2L))
                   \sum_{n\le L}\frac{a(n)^2}{n^{1+2b}}
 \ll_{b,\eta}U^{2b}(U+L\log(2L))L^{2\eta}\log(2L).       \tag{17}
\]

The multiplier depending on \(t\) was bounded pointwise before applying
(16); coefficients were not silently frozen. The dual sum is identical
for this purpose after reversing \(t\), and \(|X(s)|=1\) costs nothing.
Choose \(\delta,b,\eta>0\) with
\(\delta+2b+2\eta(1+\delta)<\epsilon/2\), absorb the logarithms, and
include \(P(s)\) and both tails. This proves (11).

Combining (11), (10), and the precisely matched Leong bound proves

\[
 \int_{U\le |t|\le2U}B_q(t)\,dt\ll_\epsilon U^{1+\epsilon},
 \qquad q=1,2.                                         \tag{18}
\]

The compact range is harmless and does not require another source.
For clarity, the elementary Euler-product inequality
\(\zeta(\sigma)^3|\zeta(\sigma+iv)|^4
|\zeta(\sigma+2iv)|\ge1\), \(\sigma>1\), follows from
\(3+4\cos x+\cos2x=2(1+\cos x)^2\ge0\).
A zero at \(1+iv\), \(v\ne0\), would make its left side tend to zero
as \(\sigma\downarrow1\), a contradiction. Hence the denominators in
(10) have no nonzero critical-line singularity. At \(t=0\),
\(1/\zeta(1+2it)\) vanishes, while \(F(1/2+it)\) is regular. Thus
\(B_q\) is bounded on \([-2,2]\); (18) also holds for \(1\le U\le2\)
after adjusting the constant.

### Entire shift and spectral summation

Set \(\Lambda_h=Rh/\sqrt N\). Uniformly in the frozen range,
\(\Lambda_h\gg T^{1/4}\), with constants depending only on the fixed
radius window. On the support of \(W_h\), put
\(x=h\sinh^2(r/2)\). Then

\[
 \sqrt{x+h}-\sqrt x=\sqrt h e^{-r/2},\qquad
 \sinh r\asymp N/h,
\]

and \(r\ge\log3\) lies in an interval of uniformly bounded length.
The exact transform therefore has the reviewed spherical branches
\(e^{\pm itr}(t\sinh r)^{-1/2}\) with bounded amplitude symbols.
The positive branch is stationary when
\(t=\pi R\sqrt h e^{-r/2}\asymp\Lambda_h\); the negative branch is
nonstationary. Second-derivative estimation and smooth endpoint
vanishing give

\[
 |H_h(t)|\ll_J A^2\sqrt{N/h}\,\Lambda_h^{-1}
       \quad (c_0\Lambda_h\le |t|\le C_0\Lambda_h),       \tag{19}
\]

for fixed sufficiently enlarged constants \(c_0,C_0\). This is the
global bound, including a stationary point at or outside a support
boundary, not an interior asymptotic substituted at every shift.

For real \(t\), \(|\eta_t(m)|\le d(m)\). Moreover every descendant in
(3) has coefficient \(O(\sqrt m)\), and

\[
 \sum_{\text{descendants of }h}\sqrt{m/h}\ll1.            \tag{20}
\]

The level-one terms in this sum form the convergent geometric sum
\(\sum_{a\ge0}2^{-(a+2)/2}\), and the level-two term contributes at most
one. Thus \(|L_{1,h}(t)|+|L_{2,h}(t)|\ll_\eta h^{1/2+\eta}\), uniformly
in \(t\), with every alternating sign and multiplicity first included
in its exact definition.

Cover the stationary interval for one shift by a bounded number of
dyadic bands \(U\asymp\Lambda_h\). Equations (18)--(20) show

\[
 \sum_q\int_{c_0\Lambda_h\le|t|\le C_0\Lambda_h}
       B_q(t)|L_{q,h}(t)H_h(t)|dt
 \ll A^2\sqrt N\,h^\eta\Lambda_h^\eta.                  \tag{21}
\]

In particular the whole shift dyad \(h\asymp M\) costs
\(A^2\sqrt N M T^\epsilon\), since
\(U\asymp TM/\sqrt N\). Summing all dyads through \(2N\) costs
\(A^2N^{3/2}T^\epsilon\). All powers of \(h\) and \(\Lambda_h\)
are absorbed by choosing the input \(\eta\) small: throughout the
range, \(h\ll T^{3/2}\) and \(\Lambda_h\ll T^{7/4}\).

Here are explicit envelopes paying the regions outside (19).
Repeated nonstationary integration in the same exact radial integral
gives, for any fixed \(K\),

\[
 |H_h(t)|\ll_{K,J}A^2\sqrt{N/h}\,|t|^{-1/2}
 \begin{cases}
  \Lambda_h^{-K},&1\le|t|\le c_0\Lambda_h,\\
  |t|^{-K},&|t|\ge C_0\Lambda_h.
 \end{cases}                                           \tag{22}
\]

For \(|t|\le1\), the exact Legendre function, rather than either
large-\(t\) branch, gives

\[
 |H_h(t)|\ll_{K,J}A^2\sqrt{N/h}\log(2N)\Lambda_h^{-K}.   \tag{23}
\]

The logarithm covers the coalescing spherical branches at zero.
Uniformity follows, for example, from the Mehler integral on
\(r\ge\log3\): after extracting \((\sinh r)^{-1/2}\), its bounded
spectral-parameter derivatives in \(r\) cost at most \(1+r\).
The factor \(\sinh r\) in the radial measure leaves the displayed
\(\sqrt{N/h}\). The phase derivative is comparable to \(\Lambda_h\)
on the low bands, and comparable to \(|t|\) on the high bands.
All integrations have zero endpoint contributions because the actual
amplitude is smoothly zero-extended. These are also precisely the
uniform scalar estimates reviewed in the permitted closed227 packet.

Apply (18) on every dyadic tail band. For one shift, (22) costs at most
\(A^2\sqrt N h^\eta\Lambda_h^{1/2+\eta-K}\); (23) costs at most
\(A^2\sqrt N h^\eta\log(2N)\Lambda_h^{-K}\).
After all \(h<2N\), these are \(O_{B,J}(A^2T^{-B})\) for any desired
fixed \(B\), by first fixing a sufficiently large \(K\) and using
\(\Lambda_h\gg T^{1/4}\), \(N\ll T^{3/2}\).
Bounded \(T\), where a band boundary may cross one, is covered by
adjusting the constant. Thus no positive-height tail, zero neighborhood,
or small-shift gamma transition has been discarded.

Finally, \(H_h(-t)=H_h(t)\) by the Legendre parameter symmetry,
\(\eta_{-t}(m)=\eta_t(m)\), and \(B_q(-t)=B_q(t)\).
Both spectral signs have therefore been paid with the correct factor
two, even though \(H_h\) is complex. Since \(0<\alpha_h\le1\), (21)
and the tails prove the stronger absolute-integral version of (1).

### The whole remaining cusp term and the pretrace return

The signed cusp expression (5) is still open at the one-sided target
\(2\Re\mathcal D\ll A^2N^{3/2}T^\epsilon\).
Using the previous, separately stated AH fourth-moment and individual
Hecke-second-moment premises gives on
\(h\asymp M\), \(t_j\asymp U\asymp TM/\sqrt N\),

\[
 \|V_{q,M,U}\|_2\ll A^2M\sqrt N T^\epsilon,\qquad
 \left|\sum_{t_j\asymp U}|u_j(z_q)|^2V_{q,M,U}(j)\right|
 \ll A^2TM^2T^\epsilon.                                \tag{24}
\]

This is the inherited whole-vector positive certificate, including
the parity weights, with all discrete tails already paid. Summing
gives \(A^2TN^{2+\epsilon}\). No malformed printed collective sieve
is used. Even the previously labelled hypothetical fixed-sieve-sized
norm would give \(A^2TN^{3/2+\epsilon}\), leaving a factor \(T\).

There is a better cap for the COMPLETE complex sum of both cusp levels.
The arithmetic right side of (6) has absolute size
\(O(A^2N^{2+\epsilon})\), from the divisor coefficient bound and the
already paid density integral. Subtracting (1) therefore gives

\[
 |\mathcal D|\ll A^2N^{2+\epsilon}.                     \tag{25}
\]

This does not separately assert that each level or each band has that
cap. At \(N=T\), (25) is still larger than the required raw target by
\(T^{1/2}\); (24) is larger by \(T^{3/2}\). These are gaps between
upper certificates, not lower bounds for the actual signed cusp term.

Upon division by \(N^{3/2}\) in the complete Fejer inequality,
the new continuous contribution is \(O(A^2T^\epsilon)\); the remaining
cusp cap still contributes \(O(A^2N^{1/2+\epsilon})\).
The resulting route supplies only complex-wave exponent \(1/4\)
and physical exponent \(3/8\), weaker than the inherited complete
complex \(13/56\) certificate and complete REAL benchmark \(\beta\).
No \(\beta\) estimate has been assigned to complex blocks.
The singleton is \(O(1)\), all dyadic scales through \(P\) are retained,
and the original Schwartz tail after \(P\) has arbitrarily small total
absolute mass at sufficiently large fixed order, exactly as in the
frozen interface. None of these restores a missing cusp saving.

Full pretrace recombination does recreate the original complete
correlation functional. Inverting the exact radial transform returns
the determinant-orbit kernel; the finite recurrence (3) then returns
every actual \(r_2(n+h)r_2(n)W_h(n)\). Restoring the constant term gives
\(\sum_h\alpha_h C_h\), not a shorter independent arithmetic object.
More explicitly, with the original zero-extended vector
\(z_n=r_2(n)g(n)e(R\sqrt n)\) and \(H=2N\),

\[
 \sum_n|z_n|^2+2\Re\sum_{h=1}^{H-1}(1-h/H)C_h
   =\frac1H\sum_{k\in\mathbb Z}
                \left|\sum_{r=0}^{H-1}z_{k+r}\right|^2.  \tag{26}
\]

The count of a pair at separation \(h\) is exactly \(H-|h|\).
Equation (26) is the original Fejer quadratic controlling the circle
wave; it is not itself a saving. The continuous projection alone does
not equal that quadratic, and paying it leaves all of (5). A functional
equation or geometric return cannot be credited with cancellation until
an actual bound for the full surviving signed cusp expression is proved.

## 4. First doubtful or unproved step

Within the stated inherited whole-functional identity and scalar
transform interface, (1) has no further mean-value premise: (7)--(23)
derive all CM factors and prove its required mean square, using only
the exactly sourced reciprocal-zeta assertion. Independent nonauthor
checking of these derivations remains required before acceptance.

The first unproved full-target inequality is the complete signed cusp
bound for (5), with all its shifts, modes, phases, and tails. Since
\(\mathcal C\) is target-sized, it is an equivalent remaining
one-sided sufficient objective up to the harmless target-sized error
in (6). Its phase still includes the actual \(h^{it_j}\) and common
spectral phase inherited from the exact \(H_h\). Neither (24), (25),
nor the return (26) estimates that cancellation at the required scale.

No universal no-go for a signed spectral argument is proved here.

## 5. Controls and outcomes

| Required control | Outcome |
|---|---|
| `actual_full_target` | The exact target remains (6), with complete cusp owner (5). Only its entire continuous component is paid. |
| `all_shifts_parity_and_scales` | All \(h<2N\), the full finite polynomials (3), their bounded geometric mass (20), and every frozen dyadic scale occur. |
| `signed_joint_phase_before_norms` | The exact joint vectors are defined before taking norms. Absolute values are subsequently legal for the continuous estimate alone; no cusp phase cancellation is claimed. |
| `source_and_functional_equation_hypotheses` | One new primary work, Leong v5 Corollary 4, matched at \(v=2|t|\ge2\). The degree-two equation and mean square are derived, with root number, conductor, poles, and both sums explicit. |
| `complete_discrete_and_continuous_spectra` | One plus two continuous cusps remain with their exact factor two. The entire cusp complement, including old/new and any exceptional modes, stays in (5). |
| `gamma_transitions_and_dual_lengths` | Natural balanced length \(U/\pi\), analytic conductor \(\asymp U^2\), truncation \(U^{1+\delta}\) with paid tails. Bound (15) covers \(t+v\) near zero; the radial kernel uses exact Legendre at low height. |
| `literal_endpoints_and_tails` | Smooth zero extension, disappearing overlap, low height, both high tails, all real \(R\), singleton, and the entire original Schwartz tail are accounted for. Discrete-empty overlaps are never assumed to have zero continuous density. |
| `real_complex_scope` | (1) bounds a complex spectral component. The full goal is the real part of (6). The inherited \(\beta\) remains exclusively a complete real-wave estimate. |
| `full_power_restoration` | Continuous raw size \(A^2N^{3/2}\); cusp raw cap \(A^2N^2\); normalized squared-wave remainder \(A^2N^{1/2}\), hence no improved exponent. |
| `certificate_not_actual_lower_bound` | Every deficit in (24)--(25) compares upper certificates. Neither the signed target nor cancellation is disproved. |
| `statement_only_control` | This role is explicitly NONBLIND and has read no current blind packet/report. Independent statement-only work and conductor application are separate owners. |
| `fixed_order_full_goal` | No fixed moment is promoted to quarter. The unbounded family of adequate fixed even moments and all original complete obligations remain open. |

Additional exact controls: at \(s=1\), CM residues reproduce inverse
areas; at two the Euler factors in (9) agree with the two cusp formula;
at \(t=0\) the inverse zeta factor vanishes; at both spectral signs the
integrand is even. The continuous estimate uses the actual oscillatory
radial phase to obtain (19) and (22); it does not establish an analogous
full unsigned-wave bound. Bounding a proper component by absolute values
therefore does not evade the earlier unsigned/adversarial controls.

Zero numerical or symbolic experiments were performed. The calculation
is analytical and algebraic; no sampled value certifies an asymptotic.

## 6. Dependencies and provenance

Exact local context used:

- `protocol.md`;
- `state/proof_obligations.yml` (authoritative target entries and their open status; the graph remains at the starting hash);
- `state/active_campaign.yml`;
- `strategy/round228_signed_heegner_phase.md`;
- `strategy/gauss_circle_strategy_review_2026-09-23.md`;
- `strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md`;
- `rounds/codex-managed/gc-signed-heegner-phase/briefs/complete_eisenstein_pairing.md`;
- `rounds/codex-managed/gc-signed-heegner-phase/briefs/complete_signed_heegner_interface.md`;
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/complete_joint_spectral_interface.md`;
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/heegner_joint_norm_audit.md`, especially (7)--(10), (13), and (15)--(24);
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_heegner_norm_review.md`;
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/joint_shift_spectral_attack.md` and `reviews/independent_spectral_attack_review.md`, for the exact scalar kernel and low/high tail scope;
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/synthesis.md`;
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, for the unchanged complete real-wave/moment scope.

Existing-source interface inspected again:
[Assing--Humphries, arXiv:2607.13518v1](https://arxiv.org/html/2607.13518v1),
the fixed-point fourth moment and its previously audited application
scope. Its printed collective-sieve defects are not repaired or used.
The prior cusp certificate (24) retains the source assumptions already
fenced in the closed227 packet; the new continuous proof does not need
that cusp fourth moment.

Only new primary work imported:
[Leong, arXiv:2405.04869v5](https://arxiv.org/pdf/2405.04869v5),
Corollary 4, last assertion, PDF page 4; exact scope and specialization
are recorded in Section 2. Its stronger off-line assertions, numerical
constants in other regions, and asymptotic refinements are unused.


Provenance repair after initial freeze: replaced unintended standalone carriage-return bytes in LaTeX roman-type commands with literal \rm commands. This byte-only formatting repair changes no mathematical content or source dependency.

No current sibling report, blind report/packet, or conductor control was
read. No authoritative graph, proof draft, validation matrix, synthesis,
or legacy archive was edited. This assigned report is the only written
artifact. The work stays within one bounded attempt, one additional
indispensable primary work, and zero experiments.

## 7. Recommended state effect

**Retain** the complete continuous-component lemma (1), exact cusp/CM
factors, and self-contained degree-two mean-square proof as candidate
evidence requiring the specified nonauthor source, normalization,
transform, tail, and full-power reviews. A narrowly scoped component
promotion is for the conductor to decide after those gates; no whole
parent promotion is justified by this report.

**No change** to the full target, accepted exponents, proof draft,
M1/M2/GAR/endpoints, or moment objectives. The round-level exit remains
`complete_signed_heegner_no_new_bound` unless the separately owned
entire cusp estimate is proved and validated. The remaining owner is
exactly (5), not a new chain of unestimated local sectors.

Freeze this report at its externally recorded SHA256 and stop. Only the
conductor closes Round228 or chooses a successor.

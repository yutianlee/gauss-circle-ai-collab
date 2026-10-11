# Round 210: actual signed bin input with maximum-label prefixes

## 1. Result: a complete paid transfer and a quantitatively insufficient actual input bound

Campaign: gc-signed-near-frequency-cancellation. Task: signed_rational_bins.
Role: selected-context discovery, not blind. Generated: 2026-09-27T15:29:16Z.
Starting graph SHA-256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Candidate evidence only. Effort: entirely analytical/algebraic; no mathematical
experiments, external theorem imports, or successor work.

There are two mechanisms in this report:

1. A phase-preserving smooth-bin transfer, with a single moving prefix after
   grouping fifth products by their largest original quotient label.
2. An estimate of that transfer's actual signed input using the exact
   integer-lattice representation of every fixed prefix, a divisor envelope,
   and the joint second moment of all dyadic label intervals.

The first gives a legal sufficient bound

\[
 \int_J|Q_N(x)|^{10}dx
 \ll X\log(2L+2)\,\mathcal E_N,                           \tag{1}
\]

where the explicitly defined input \(\mathcal E_N\) retains internal
modulation, coefficient derivatives, both arms, every bin, and the sum of
energies over all dyadic intervals of the maximum quotient label. In
particular it is not the unmasked fifth-convolution energy.

The second mechanism proves for this actual input

\[
 \boxed{\mathcal E_N\ll_\epsilon H^9T^\epsilon,\qquad
 \int_J|Q_N|^{10}\ll_\epsilon XH^9T^\epsilon
       =T^{11+\epsilon}N^{-9/2}.}                        \tag{2}
\]

This uses actual character cancellation: the coefficient at the zero
integer of every fixed-prefix lattice representation is
\(4\sum_{d\le D}\chi_4(d)=O(1)\). The nonzero integer coefficients have
divisor size uniformly in the prefix. The argument does not take absolute
values on the individual near-frequency integrals.

Nevertheless (2) recovers only a variance/supremum cost. Its excess over
the required gate \(G=T^{473/65}N^{-1/2}\) is

\[
 T^{242/65}N^{-4}=T^{242/65-4\alpha},
 \qquad N=T^\alpha,                                    \tag{3}
\]

which is a strictly positive power on the entire required band. No
complete moment or pointwise improvement is proved. The complete residual
for this sufficient method is the substantially stronger actual bound

\[
 \mathcal E_N\ll_\epsilon
       T^{343/65+\epsilon}N^{-1/2}
       =H\,T^{278/65+\epsilon}.                         \tag{4}
\]

The logarithm in (1) is absorbed by choosing epsilon before applying (4).
Condition (4) is sufficient, not asserted necessary for the signed target.
In particular neither the new upper cost (2) nor its deficit (3) is a
lower bound for the actual input or for the signed tenth moment.

## 2. Exact statements and hypotheses

Let \(T\ge2\) be real, \(X=T^2\), \(Y=[1/2,3]\), \(J=XY\), and retain
every dyadic

\[
 T^{166/325}<N<T^{242/325},\quad H=T/\sqrt N,\quad
 h(x)=2\sqrt{x}/\sqrt N.
\]

Use the exact real odd Schwartz filter \(F\), Fourier convention, fixed
mollifier, and partition in the supplied Round209 report:

\[
 F(u)=-\int_1^2 t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2)
                        \sin(2\pi tu)\,dt,\qquad
 \widehat F(\xi)=\frac i2\operatorname{sgn}(\xi)
       |\xi|^{-1}\Psi(\sqrt{N/T}\,|\xi|)v(\xi^2).
                                                               \tag{5}
\]

Its Fourier support lies in \([-2,-1]\cup[1,2]\), and all relevant
Schwartz seminorms are uniform. No positivity of \(F\) is assumed or used.
Write \(e(t)=\exp(2\pi it)\), and use Fourier transforms with \(e(-u\xi)\).
Keep the original floor cutoff

\[
 M=\lceil6X\rceil,\quad D=\lfloor\sqrt M\rfloor,\quad
 L=\lfloor M/(D+1)\rfloor,\quad Q=\max(D,4L)\asymp T.
\]

For a fixed real width \(h\asymp H\), introduce the finite rational
polynomials, in a separate real phase variable \(z\),

\[
 A(z;h)=4h\sum_{d\le D}\frac{\chi_4(d)}d
          \sum_{k\in\mathbb Z}\widehat F(hk/d)e(-kz/d),     \tag{6}
\]

\[
 B_\ell(z;h)=\frac{2ih}{\ell}
       \sum_{k\in\mathbb Z}\chi_4(k)
              \widehat F(hk/(4\ell))e(-kz/(4\ell)),        \tag{7}
\]

\[
 S_r(z;h)=A(z;h)+\sum_{1\le\ell\le r}B_\ell(z;h)
       \quad(0\le r\le L),\qquad S_{-1}=0.               \tag{8}
\]

Set \(S_r=S_L\) for \(r>L\). Zero Fourier modes vanish. Formula (7)
has the plus sign appropriate to phase \(e(-kz/(4\ell))\): its finite
character sum is \(\sum_{a\bmod4}\chi_4(a)e(ka/4)=2i\chi_4(k)\).
It is the same arm and orientation as the supplied grouped formula.

The actual rational main term is exactly

\[
 Q_N(x)=S_{p(x)}(x;h(x)),\qquad
 p(x)=\min(L,\lceil x/D\rceil-1).                         \tag{9}
\]

Thus \(\ell<x/D\) remains a strict prefix even when \(x/D\) is an
integer. For the large \(T\) under consideration \(p(x)\ge0\) on \(J\);
bounded \(T\) is absorbed in constants. No moving indicator is
differentiated anywhere below.

Pad labels \(0,\ldots,L\) to a set of size a power of two, setting the
extra label polynomials to zero. Let \(\mathscr I\) contain every
canonical dyadic label interval. The number of levels is
\(K\ll\log(2L+2)\), and each level partitions the padded label set.
Label zero means the entire first arm; positive labels are the original
\(\ell\) in (7). Define

\[
 G_0=S_0^5,\qquad G_\ell=S_\ell^5-S_{\ell-1}^5\quad(\ell\ge1),
 \qquad P_I=S_b^5-S_{a-1}^5\quad(I=[a,b]).               \tag{10}
\]

Each \(G_\ell\) contains exactly the fifth-product terms whose largest
positive label is \(\ell\); \(G_0\) contains the all-first-arm terms.
All ordered multiplicities and mixed-arm products survive. With the
width fixed, aggregate every exact rational-frequency collision in

\[
 P_I(z;h)=\sum_\mu C_{I,\mu}(h)e(-\mu z).                \tag{11}
\]

The frequency sets may be fixed as finite enlarged envelopes for all
\(h\asymp H\). Coefficients are zero outside their actual support.

Choose a real \(\rho\in C_c^\infty((-1,1))\) with
\(\sum_{j\in\mathbb Z}\rho(t-j)=1\) for every real \(t\). It can be
constructed by dividing a nonnegative smooth bump, positive on
\([-1/2,1/2]\) and supported in \((-3/4,3/4)\), by its positive
periodization. This choice also gives \(\rho=1\) on \((-1/4,1/4)\).
These are smoothly
overlapping bins of width \(2/X\) at spacing \(1/X\). Put

\[
 h_y=2H\sqrt y,\qquad
 f_{I,j}(y)=
   \sum_\mu \rho(X\mu-j)C_{I,\mu}(h_y)
                   e\bigl(-y(X\mu-j)\bigr),            \tag{12}
\]

\[
 \mathcal E_N=
   \sum_{I\in\mathscr I}\sum_{j\in\mathbb Z}
       \int_Y\bigl(|f_{I,j}(y)|^2+|f'_{I,j}(y)|^2\bigr)\,dy.
                                                               \tag{13}
\]

This defines the complete input in (1)--(4). The derivative in (13)
includes the exact width variation and the internal phase. The bin
center is used only as an outer modulation:

\[
 P_I(Xy;h_y)=\sum_j e(-jy)f_{I,j}(y).                    \tag{14}
\]

The frequency variable \(\mu\) in (11) includes exact nonpairing fifth
relations, zero total frequency, both signs, and all arms.

## 3. Proof and quantitative cost ledger

### Mechanism one: phase-preserving transfer and the actual prefix

For any finite family \(f_j\in H^1(Y)\), there is an absolute bound

\[
 \int_Y\left|\sum_j e(-jy)f_j(y)\right|^2dy
       \ll\sum_j\int_Y(|f_j|^2+|f'_j|^2)\,dy.           \tag{15}
\]

Here is a proof with no frequency-spacing hypothesis inside a bin.
Reflect an \(H^1\) function across the two endpoints of the fixed
interval \(Y\) on fixed neighboring intervals and multiply by a fixed
smooth cutoff. This gives a compactly supported extension \(E\) with
\(\|Ef\|_{H^1(\mathbb R)}\ll\|f\|_{H^1(Y)}\). The same linear
extension works for every \(j\). Fourier transformation, Cauchy, and
\(\sup_\xi\sum_j(1+|\xi+j|^2)^{-1}<\infty\) give

\[
 \begin{split}
 \left\|\sum_j e(-jy)Ef_j(y)\right\|_2^2
 &\ll \int_{\mathbb R}\sum_j
       (1+|\xi+j|^2)|\widehat {Ef_j}(\xi+j)|^2\,d\xi\\
 &\ll\sum_j\|Ef_j\|_{H^1(\mathbb R)}^2.
 \end{split}
\]

Restricting to \(Y\) proves (15). All normalizing \(2\pi\) factors are
absolute constants. No variable coefficient is silently treated as a
constant.

For each \(x\), decompose the label prefix \([0,p(x)]\) into its canonical
disjoint dyadic intervals. At most \(K\) occur. Telescoping (10) yields

\[
 Q_N(x)^5=\sum_{I\ {\rm selected\ at}\ x}P_I(x;h(x)).
                                                               \tag{16}
\]

Pointwise Cauchy followed by inclusion in the sum over every interval gives

\[
 \int_J|Q_N|^{10}
 \le K\sum_{I\in\mathscr I}\int_J|P_I(x;h(x))|^2dx.
                                                               \tag{17}
\]

The total interval energy on the right is retained; it has not been
replaced by the energy of the unmasked polynomial. Applying (14)--(15)
after \(x=Xy\) proves (1). Grouping by the maximum label costs one outer
logarithm. It avoids a fifth power of the number of scales, but this
accounting simplification supplies no arithmetic saving.

Two elementary controls explain the form of (13).

First, a bin's zero-th coefficient sum can vanish while its modulated
sum does not. With two constant coefficients \(1,-1\), distinct
frequencies in the plateau of one bin, and normalized offsets
\(0,\delta\) with \(0<\delta<1/4\),
the zero-th sum is zero whereas \(1-e(-\delta y)\) is nonzero.
The other smooth bins are identically zero in this control.
This is a control on a proposed general transfer, not an actual-r2
counterexample.

Second, an \(L^2\)-only version of (15) is false. For \(m\) indices,
let \(f_j(y)=e(jy)\). The left side is \(m^2|Y|\), and the proposed
right side without derivatives is \(m|Y|\). Derivative control prevents
this artificial cancellation of the outer modulation. A moving prefix
is discontinuous and does not satisfy that control; (16)--(17), rather
than differentiation of its jumps, is the lawful repair.

### Mechanism two, step one: bin input as physical polynomial averages

The smooth choice of bins permits an elementary reverse estimate useful
for bounding their actual input. If
\(V(z)=\sum_\mu d_\mu e(-\mu z)\) is any finite polynomial and
\(\psi\in C_c^\infty(\mathbb R)\), then for every real \(z_0\)

\[
 \sum_j\left|\sum_\mu
       \psi(X\mu-j)d_\mu e(-\mu z_0)\right|^2
 \ll_{\psi,A}\int_{\mathbb R}(1+|u|)^{-A}
                           |V(z_0-Xu)|^2du             \tag{18}
\]

for any fixed \(A>0\). This includes a genuine phase convolution, not
replacement by the center of a bin.

The normalization in the physical phase variable is explicitly

\[
 \int_{\mathbb R}(1+|u|)^{-A}|V(z_0-Xu)|^2du
 =\frac1X\int_{\mathbb R}
    \left(1+\frac{|z-z_0|}{X}\right)^{-A}|V(z)|^2dz.
                                                               \tag{18a}
\]

Thus an interval norm of size \(XH\) contributes \(H\), not \(XH\),
to the bin energy.

To prove (18), put \(k=\widehat\psi\). Fourier inversion writes the
inner sum as
\(\int_{\mathbb R}k(u)V(z_0-Xu)e(-ju)du\).
Periodize the integrand over \(u\) modulo one and apply Parseval to
its integer Fourier coefficients. Cauchy on the periodizing sum,
using the summable weights \((1+|u|)^{-2}\), bounds the answer by

\[
 C\int_{\mathbb R}(1+|u|)^2|k(u)|^2
                                  |V(z_0-Xu)|^2du.
\]

The Schwartz decay of \(k\) proves (18). The polynomial is bounded
for every fixed coefficient vector, so all periodizations converge
absolutely; there is no omitted tail. This proof does not require
rational frequencies or separation.

For \(P_I\), define its width derivative

\[
 U_I(z;h)=h\,\partial_hP_I(z;h).
\]

Differentiating the smooth expression (12), with
\(h'_y/h_y=1/(2y)\), gives two contributions: the bin with coefficient
polynomial \((2y)^{-1}U_I\), and the bin of \(P_I\) with multiplier
\(-2\pi i\,t\rho(t)\). Applying (18) to \(\rho\) and \(t\rho(t)\)
therefore proves, uniformly for \(y\in Y\),

\[
 \sum_j(|f_{I,j}(y)|^2+|f'_{I,j}(y)|^2)
 \ll_A\int_{\mathbb R}(1+|u|)^{-A}
 \left(|P_I(X(y-u);h_y)|^2+
       |U_I(X(y-u);h_y)|^2\right)du.                    \tag{19}
\]

The center modulation has modulus one. All internal phase derivatives
and the actual square-root width have now been priced.

### Actual static-prefix lattice coefficients

For \(0\le r\le L\), Poisson summation in (6)--(7), with fixed \(h\),
gives exactly the formulas (20)--(22) below. At the zero-prefix boundary
set \(a_{-1}(n)=0\) for every integer \(n\), matching \(S_{-1}=0\);
for padded labels \(r>L\), set \(a_r=a_L\), matching \(S_r=S_L\).

\[
 S_r(z;h)=\sum_{n\in\mathbb Z}a_r(n)F((n-z)/h),          \tag{20}
\]

where for \(n\ne0\)

\[
 a_r(n)=4\sum_{\substack{d\le D\\d\mid n}}\chi_4(d)
       +4\sum_{\substack{\ell\le r\\\ell\mid n}}
                                      \chi_4(n/\ell),   \tag{21}
\]

and

\[
 a_r(0)=4\sum_{d\le D}\chi_4(d)=O(1).                    \tag{22}
\]

The divisors \(d,\ell\) are positive; negative \(n/\ell\) retains its
actual character. In particular \(\chi_4(0)=0\) removes the second
arm's zero term. Formula (22) uses bounded character partial sums
before any absolute values. For \(n\ne0\),
\(|a_r(n)|\le8\tau(|n|)\), uniformly for every integer prefix
\(-1\le r\le L\).

For \(S_r^{[1]}=h\partial_hS_r\), the same formula holds with the
uniformly Schwartz filter

\[
 F_1(v)=-vF'(v).
\]

Its Fourier transform is still smooth and supported in the same
annuli, because it is the Fourier counterpart of differentiating
\(h\widehat F(h\lambda)\). Using the elementary divisor bound and
Schwartz decay in (20) proves, for any fixed \(\eta>0\),

\[
 |S_r(z;h)|+|S_r^{[1]}(z;h)|
       \ll_\eta H(2+|z|+H)^\eta,\qquad h\asymp H.        \tag{23}
\]

For example, split \(n\) into \(|n-z|\le H\) and successive intervals
of length \(H\), apply \(\tau(n)\ll_\eta |n|^\eta\) on each, and choose
the Schwartz order larger than \(\eta+2\). The \(n=0\) term is handled
by (22). Thus (23) is uniform also near and across \(z=0\), for negative
real \(z\), and on the full tails \(z=X(y-u)\) in (19).

This is a substantive actual-coefficient distinction. Replacing
\(\chi_4(d)\) by its absolute value makes (22) of order \(D\), so
the displayed uniform \(O(H)\) lattice envelope cannot be obtained
from the same argument. Arbitrary rational vectors do not have the
integer divisor representation (21) either. The bound does not
pretend to distinguish the remaining signed correlations more sharply
than the stated divisor envelope.

### The entire dyadic-label second moment is paid

Let
\[
 W_I=S_b-S_{a-1},\qquad W_I^{[1]}=h\partial_hW_I
          \quad(I=[a,b]).
\]
At a fixed dyadic level the intervals \(I\) partition the labels.
After grouping exact single-frequency collisions, the first-arm
coefficients have odd reduced denominator \(q\) and are

\[
 \frac{4h\chi_4(q)}q\widehat F(ha/q)
                     \sum_{j\le D/q}\frac{\chi_4(j)}j. \tag{24}
\]

The first arm belongs to the unique interval containing label zero.
The second-arm coefficient at reduced frequency \(a/q\), \(4\mid q\),
\((a,q)=1\), is

\[
 \frac{8ih\chi_4(a)}q\widehat F(ha/q)
       \sum_{\substack{j\ge1\\qj/4\in I\\qj/4\le L}}
                                      \frac{\chi_4(j)}j. \tag{25}
\]

All positive and negative numerators are included. The odd and
four-divisible denominator classes are disjoint. Every active denominator
satisfies \(cH\le q\le Q\); for each \(q\) there are \(O(q/H)\) possible
signed numerators in a fixed enlarged envelope.

For fixed \(a/q\), at one level the sets of \(j\) in (25) are disjoint.
Consequently

\[
 \sum_{I\ {\rm at\ one\ level}}
   \left|\sum_{qj/4\in I}\frac{\chi_4(j)}j\right|^2
 \le\left(\sum_{j\le4L/q}\frac1j\right)^2
 \ll\log^2(2X).                                       \tag{26}
\]

The first-arm alternating sum is bounded. Counting the numerators,
summing \(q\), and then summing the \(K\) levels proves

\[
 \sum_{I\in\mathscr I}\sum_\lambda
       |w_{I,\lambda}(h)|^2\ll H\log^C(2X).             \tag{27}
\]

The same holds for \(W_I^{[1]}\), since its multiplier has the same
support and uniform size \(O(H)\). No factor equal to the number of
intervals has been suppressed: (26) is the joint interval calculation
that pays it.

Distinct reduced frequencies in (24)--(25) are separated by at least
\(Q^{-2}\gg X^{-1}\). Expansion of the square over any interval of
length \(X\) has kernel bounded by
\(\min(X,C/|\lambda-\lambda'|)\). Ordering the frequencies and summing
the harmonic series gives the elementary Schur bound

\[
 \int_{z_0}^{z_0+X}\left|\sum_\lambda b_\lambda
                                      e(-\lambda z)\right|^2dz
 \ll X\log(2X)\sum_\lambda|b_\lambda|^2,                \tag{28}
\]

uniformly in every real \(z_0\). Combining (27)--(28), then summing
unit \(u\)-intervals with a fixed sufficiently decaying weight, yields
for every \(y\in Y\) and fixed \(h\asymp H\)

\[
 \sum_{I\in\mathscr I}\int_{\mathbb R}(1+|u|)^{-A}
 \left(|W_I(X(y-u);h)|^2+
       |W_I^{[1]}(X(y-u);h)|^2\right)du
 \ll H\log^C(2X).                                      \tag{29}
\]

This is valid for all translates, including those outside the original
positive observation window. It is a frozen-width estimate; the next
step applies it separately for each actual \(h=h_y\), which is legitimate
because all constants are uniform.

### Complete actual bin estimate and failure to reach the gate

The elementary factorization

\[
 P_I=W_I\sum_{r=0}^4 S_b^{4-r}S_{a-1}^{r}              \tag{30}
\]

and its width derivative imply, using (23), that at
\(z=X(y-u)\), \(y\in Y\),

\[
 |P_I(z;h_y)|^2+|U_I(z;h_y)|^2
 \ll_\eta H^8X^{8\eta}(1+|u|)^{8\eta}
       \left(|W_I(z;h_y)|^2+
             |W_I^{[1]}(z;h_y)|^2\right).              \tag{31}
\]

The terms where the derivative hits the degree-four factor in (30)
are included: (23) bounds each differentiated \(S_r\) by the same
envelope. There are only a fixed number of product-rule terms.
Take \(A>8\eta+3\) in (19), use (29), sum all intervals, and integrate
over the fixed interval \(Y\). This proves
\(\mathcal E_N\ll H^9T^\epsilon\), after choosing \(\eta\) sufficiently
small and absorbing logarithms. Equation (1) then proves (2).

For comparison, the crude rational coefficient envelope has
\(\ell^1\) mass \(O(Q)\) and separated-frequency second moment of
order \(H\), up to logarithms. The corresponding absolute convolution
price is \(H Q^8\), and after multiplication by \(X\) it is
\(XHQ^8=T^{11}N^{-1/2}\). The actual lattice step replaces \(Q^8\)
by \(H^8\), a factor \(N^{-4}\), without converting a positive
near-majorant lower bound into a signed one. But the improved upper
price (2) is still far larger than the desired gate.

Explicitly, throughout the open required band,

\[
 \frac{242}{325}
   <\frac{242}{65}-4\alpha
   <\frac{546}{325}.                                   \tag{32}
\]

Thus this input certificate cannot prove the desired bound with a
small arbitrary epsilon. The first arm and every possible static prefix
were retained throughout; the insufficiency cannot be repaired by
declaring the interval sum or width derivative harmless without an
additional signed estimate. The old full-moment estimates do not
automatically estimate the stronger interval-and-derivative input (13).

The same upper bound (2) follows directly from the actual complete
shell's divisor supremum and variance. Accordingly this is a fully
priced actual-input calculation for the proposed bins, not a claim of
a new best tenth-moment estimate. The stronger inherited complete
bound remains

\[
 \int_J|Q_N|^{10}\ll_\epsilon
    T^{7+\epsilon}N^{-3/110}
       +T^{6+8\omega+\epsilon},\qquad
 \omega=\min(\alpha/4,\beta,(1-\alpha)/2).               \tag{33}
\]

Both terms are retained. Their deficits relative to \(G\) are
\(1-83/65+26\alpha/55\) and
\(8\omega-83/65+\alpha/2\). The latter is the larger one throughout
the band, with supremum \(7\beta-101/130\) at
\(\alpha=1-2\beta\), as in the supplied reviewed ledger.

### Exact part, errors, endpoints, and physical reconstruction

The supplied Round209 exact estimate, unchanged here, is

\[
 \mathcal D_{10}\ll_\epsilon XHQ^4T^\epsilon
                  =T^{7+\epsilon}N^{-1/2}.              \tag{34}
\]

It includes every exact nonpairing relation. Since
\(\int_J|Q_N|^{10}=\mathcal D_{10}+\mathcal O_{10}\), (4) would imply
the desired bound on the full signed \(|\mathcal O_{10}|\). Conversely
the desired \(\mathcal O_{10}\) estimate controls the full moment using
(34), but it need not imply the stronger bin certificate (4).

The inherited shell error obeys
\(\|R_N\|_\infty\ll1\) and \(\int_J|R_N|^{10}\ll TH\);
all other localization tails are rapidly small. Therefore the fixed
physical bridge gives

\[
 M_{10}(H_N)\ll_\epsilon
  T^{-6}\int_J|Q_N|^{10}dx
   +T^{-4}N^{-1/2}
   +T^{-4+\epsilon}N^{-10}+O_A(T^{-A}).                 \tag{35}
\]

The factor \(T^{-6}\) includes the tenth amplitude power and the
Jacobian. Real \(T,x,z\), strict prefix equality points, partially
intersecting endpoint bumps, and Fourier support endpoints are preserved.
No count is restricted to integer observation points.

If (4), or the desired complete signed bound by another route, were
proved on the whole band, the supplied local reproduction factor
\(N^{1/20}\), the two already controlled outer ranges including their
equalities, the singleton, the infinite Schwartz tail, and sharp
reconstruction would yield the milestone \(102/325\) only. None of
these costs is changed by the present bin transfer.

## 4. First doubtful or unproved step

The first unproved quantitative assertion in this route is (4) for
the actual full input (13). Its \(\sum_I\sum_j\) cannot be deleted,
its derivative cannot be omitted, and \(f_{I,j}\) cannot be replaced
by its zero-th coefficient sum. Our complete proven substitute is
only \(\mathcal E_N\ll H^9T^\epsilon\).

At the last analytic step, (31) uses absolute divisor-size envelopes
for eight of the ten polynomial factors. Replacing that envelope
calculation by a target-size estimate would require further signed
correlation information about the actual static-prefix polynomials,
including all mixed arms, interval differences and width derivatives.
No such information has been established here.

The comparison in (32) diagnoses this certificate's failure; it is
not an impossibility theorem for bins, for the actual input, or for
the complete signed target. It is also not legitimate to transfer
the actual termwise near-integral lower bound to (13): (13) first
aggregates signed coefficients with internal phases.

No new exact-diagonal optimization was attempted. In particular the
squarefull denominator condition for exact equalities has not been
applied to a nonzero relation. No numerator character progression
has been presumed complete inside a constrained frequency bin.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| actual_coefficients | PASS for the proved bounds. Equations (6)--(9) retain the actual two arms and their phases. Equations (20)--(22) exploit the actual integer-divisor coefficients and bounded zero-lattice character sum. No arbitrary-vector theorem is asserted as an actual-coefficient improvement. |
| complete_scales | PASS. Every bound is uniform for all required dyadic \(N\); (32) is positive over their whole band. The missing estimate (4) is stated over that same full range. |
| signed_absolute_distinction | PASS. The signed bin coefficients are aggregated before norms. Absolute values in (23) and (31) provide an upper certificate only. No termwise near integral is estimated individually, and no unsigned lower bound is applied to the signed input. |
| exact_nonpairing_relations | PASS. Full polynomial fifth powers define (10)--(12), with exact rational collisions combined only afterward. All nonpairing relations, including the supplied same-denominator examples, remain present. Bound (34) is used only in its inherited reviewed scope. |
| real_endpoints | PASS. Equation (9) preserves the strict prefix exactly, all Fourier supports are smooth, and all subsequent estimates apply to real arguments. Dyadic decomposition is in integer labels, not observation points. |
| all_costs_restored | PASS. One outer prefix logarithm, the entire dyadic interval sum, internal modulation, both derivative terms, all physical convolution tails, joint interval energies, denominator separation, the full width range, (34)--(35), and both terms in (33) are displayed. |
| full_quarter_scope | PASS. Even the unproved gate would give only \(102/325\). The quarter theorem and every direct M1/M2 parent remain open. |
| statement_only_control | NOT supplied by this selected-context report. The two generic analytic controls test transfer claims only. The independently assigned isolated report and the conductor's later seam review remain separate requirements. |

All controls are analytical. The example disproving omission of the
derivative is not an actual-coefficient counterexample. The bounded
zero-lattice coefficient is exactly where the proof uses character
cancellation that is absent after unsigned replacement; its presence
does not supply the missing high-order cancellation.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were read:

- protocol.md.
- state/proof_obligations.yml, including the open GC-target, M9-M1 and
  M9-M2 scope and the accepted complete square-root large-values bound.
- state/active_campaign.yml, Round210.
- rounds/codex-managed/gc-signed-near-frequency-cancellation/briefs/signed_rational_bins.md.
- strategy/round210_signed_near_frequency_attack.md.
- strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md.
- rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md.
- rounds/codex-managed/gc-complete-signed-tenth-moment/synthesis.md.
- rounds/codex-managed/gc-complete-signed-tenth-moment/reports/signed_fifth_convolution.md.
- rounds/codex-managed/gc-complete-signed-tenth-moment/reviews/independent_rational_tenth_review.md.
- rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md.

The supplied Round209 claimant and independent review provide the
orientation, actual grouped coefficients, threshold error, exact
diagonal and majorant scope. The Round207 ledger supplies the elementary
single-frequency separation and joint-label energy interface, rederived
in (24)--(29). The Round208 materials supply only the already reviewed
complete target, physical bridge and reconstruction costs. The new
bin estimates (15), (18)--(19), maximum-label accounting, and their
actual-input bound are derived above.

The conductor suggested maximum-label grouping in an interim message
while this task was considering the same repair; it has been adopted
with its full interval-energy cost. No sibling report or isolated
packet was read. No external theorem, new source card, mathematical
experiment, or generic-coefficient extrapolation was used.

## 7. Recommended state effect

Retain this as a fully scoped, quantitatively unsuccessful actual-input
calculation: outcome label no_new_bound_precise_open_residual.
The elementary transfer and maximum-label accounting may be retained
as candidate method evidence after independent review, but they do not
justify a new graph parent or an improved complete exponent.

Keep (4) as this method's sufficient open residual and preserve the
original signed target as the weaker objective. The proven bound (2)
recovers a known variance/supremum price and does not improve (33).
No target, M1/M2 parent, pointwise benchmark or quarter claim should be
promoted from this report.

Only this assigned report was written. Shared graph, proof draft,
validation matrices, synthesis, legacy evidence and successor files
were not edited. The assigned research task stops here.

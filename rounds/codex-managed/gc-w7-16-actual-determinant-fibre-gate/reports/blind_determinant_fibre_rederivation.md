# Round 117 statement-only blind determinant-fibre rederivation

## 1. Result: a norm-only determinant-fibre/high-pass no-go

Let

\[
 T_i(a,b):=\sum_{g\geq 1}{\chi _4(g)\over g}U_{i,a,b}(g)\in\mathbb R.
\]

Under precisely the hypotheses in the blind statement, the strongest estimate I can prove is the coefficient-blind Schur bound

\[
 |\mathfrak O_i|
 \ll_\varepsilon {D\over L}
 \left(1+\min\left(DL,{D^2\over W}\right)\right)Y^\varepsilon .
\tag{117.R1}
\]

There is a rigorous no-go for the following precisely scoped proof class: partition the literal correlation into denominator shells, increment strips, determinant fibres, parity progressions, or complete-lift expansions; apply geometric-sum, stationary-phase/van der Corput, Abel, Cauchy, Schur, Möbius, or divisor estimates; but use no cross-ray information about the actual functions \(T_i(a,b)\) beyond (117.B1) and their reality. In this class, the \(M1\) and \(M2\) character high-passes do not yield a certified power saving. The reason is exact, rather than heuristic:

1. the character alternation is long only while the determinant is changing;
2. after fixing the determinant, the congruence forces a progression of step \(2(a,b)\), which has only \(O(1)\) points when \(b,b'\asymp B\);
3. phase cancellation on the transverse progression requires a variation/Fourier norm of the actual two-ray symbol, and no such norm follows from (117.B1) or from BV in the separate lift variable \(g\);
4. Cauchy or absolute variation then restores exactly the pre-transform capacity.

The smallest complete signed survivors are the two one-dimensional sums (117.R18) and (117.R19) below. They retain the primitive masks, the triangular boundary, both numerator signs, and the complete lift transforms. Neither survivor is a constant-amplitude exponential sum.

On the hard region, the off-diagonal power in (117.R1) is

\[
 \min\left(2\delta,\,3\delta-\ell-{7\over16}\right)>{1\over2}.
\tag{117.R2}
\]

Indeed \(3\delta-\ell>15/16\) gives the second inequality, while \(\ell\geq0\) gives \(\delta>5/16\), hence \(2\delta>1/2\). Thus this proof class has no target-safe strict subrange inside the stipulated hard region. At \((\delta,\ell)=(1/2,1/6)\), (117.R1) is \(Y^{43/48+\varepsilon}\). This is a no-go for the named method class, not a disproof of (117.B3) for the literal coefficients.

## 2. Exact statement and hypotheses

Assume \(Y\) is a large real number, \(c\asymp Y\) in a fixed real interval, \(W=Y^{7/16}\), \(d\asymp D\), and \(|h|\asymp L\), with

\[
 Y^{1/4}\leq D\leq Y^{1/2},\qquad 1\leq L\leq DY^{-1/4}.
\]

All moving-symbol data and literal endpoints are fixed. A reduced ray is \((a,b)\), where \(a\neq0\), \(b>0\), and \((|a|,b)=1\). Both signs of \(a\) are retained. The complete lift coefficients are

\[
 A_1(a,b)={2\chi_4(b)\over \pi i a}T_1(a,b),\qquad
 A_2(a,b)=-{4\chi_4(|a|)\over \pi |a|}T_2(a,b),
\tag{117.R3}
\]

with real \(T_i\), and

\[
 |A_i(a,b)|\ll_\varepsilon L^{-1}Y^\varepsilon,qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2
 \ll_\varepsilon {D\over L}Y^\varepsilon.
\tag{117.R4}
\]

Put \(\kappa_1=1\), \(\kappa_2=4\). The open correlation is exactly

\[
 \mathfrak O_i=2\Re\sum_{0<n=ab'-a'b<\kappa_i bb'/W}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left({cn\over \kappa_i bb'}\right)
 \left(1-{Wn\over \kappa_i bb'}\right).
\tag{117.R5}
\]

The equal reduced frequency is the same primitive ray, so the complete \(n=0\) diagonal is already bounded by (117.R4). Nothing below reopens it.

For later use, set \(p=a'-a\), \(q=b'-b\). On \(M1\), \(b,b'\) are odd, so \(q=2r\), and

\[
 A_1(a,b)\overline{A_1(a',b')}
 ={4\over\pi^2}{(-1)^r\over aa'}T_1(a,b)T_1(a',b').
\tag{117.R6}
\]

On \(M2\), \(a,a'\) are odd, so \(p=2s\). For signed characters,

\[
 \chi_4(a)\chi_4(a')=(-1)^s,
\]

whereas the literal absolute-numerator characters satisfy

\[
 \chi_4(|a|)\chi_4(|a'|)
 =\operatorname {sgn}(aa')(-1)^s.
\]

Consequently the sign from a possible opposite-sign pair is not lost; it moves into the signed denominator:

\[
 A_2(a,b)\overline{A_2(a',b')}
 ={16\over\pi^2}{(-1)^s\over aa'}T_2(a,b)T_2(a',b').
\tag{117.R7}
\]

Thus the exact real forms are

\[
 \mathfrak O_1={8\over\pi^2}
 \sum {(-1)^rT_1(a,b)T_1(a',b')\over aa'}
 \cos\!\left({2\pi cn\over bb'}\right)
 \left(1-{Wn\over bb'}\right),
\tag{117.R8}
\]

and

\[
 \mathfrak O_2={32\over\pi^2}
 \sum {(-1)^sT_2(a,b)T_2(a',b')\over aa'}
 \cos\!\left({2\pi cn\over4bb'}\right)
 \left(1-{Wn\over4bb'}\right),
\tag{117.R9}
\]

with the exact literal supports and strict one-sided inequalities from (117.R5). Equations (117.R6)--(117.R9), rather than a character placed on the wrong coordinate or a missing sign of \(aa'\), are the symbol hypotheses used in the no-go.

## 3. Proof and derivation

### 3.1 Determinant, phase, and the two left-anchored strips

Direct expansion gives

\[
 n=a(b+q)-(a+p)b=aq-bp,
\tag{117.R10}
\]

and

\[
 {n\over bb'}={a\over b}-{a+p\over b+q}.
\tag{117.R11}
\]

Hence the orientation \(n>0\) means that the unprimed reduced frequency is larger. It is not an absolute determinant condition.

For fixed \(q\), with \(b'=b+q>0\), the exact \(p\)-strip is

\[
 {aq\over b}-{\kappa_i b'\over W}<p<{aq\over b}.
\tag{117.R12}
\]

Its real width is \(\kappa_i b'/W\). In \(M2\), \(p=2s\), so the corresponding \(s\)-width is exactly \(2b'/W\), not \(b'/W\); this is where the factor four survives the parity restriction. In \(M1\), the restriction instead is \(q=2r\).

For fixed \(p\), put \(t_i=\kappa_i b/W>0\). The exact \(q\)-boundary is

\[
 aq>bp,qquad (a-t_i)q<b(p+t_i).
\tag{117.R13}
\]

The cases are as follows.

| ray orientation | exact open \(q\)-interval before literal support cuts | exact width when finite |
|---|---|---|
| \(a>t_i\) | \(bp/a<q<b(p+t_i)/(a-t_i)\) | \(bt_i a'/[a(a-t_i)]\), necessarily \(a'>0\) |
| \(a=t_i\) | \(q>bp/a\) if \(a'>0\); empty if \(a'\leq0\) | support-limited |
| \(0<a<t_i\) | \(q>\max\{bp/a,b(p+t_i)/(a-t_i)\}\) | support-limited; the window crosses zero |
| \(a<0\) | \(b(p+t_i)/(a-t_i)<q<bp/a\) | \(-bt_i a'/[a(a-t_i)]\), necessarily \(a'<0\) |

Every row is also intersected with \(b+q>0\), the dyadic denominator shell, the numerator shell, both primitive conditions, and the literal endpoints. On a same-sign interior shell \(b,b'\asymp B\), \(|a|,|a'|\asymp A=LB/D\), away from the positive transition \(a=t_i\), the nominal \(q\)-width is

\[
 Q_i\asymp \min\left(B,{\kappa_i B^2\over WA}\right).
\tag{117.R14}
\]

For negative rays the exact expression is comparable to

\[
 {\kappa_iB^2\over WA+\kappa_iB},
\]

which displays the saturation at \(B\). For positive rays close to \(a=t_i\), (117.R14) is not a uniform asymptotic: the finite boundary recedes and the literal shell supplies the cut. This is the determinant-strip boundary that a rectangular replacement would miss.

Opposite signs are possible only in the orientation \(a>0>a'\). They obey

\[
 {a\over b}+{|a'|\over b'}<{\kappa_i\over W}.
\]

Thus they lie in the central frequency window and require, in particular,

\[
 {1\over b}+{1\over b'}<{\kappa_i\over W}.
\]

The orientation \(a<0<a'\) is impossible because it gives \(n<0\). These central pairs are retained by (117.R8)--(117.R9) through the sign of \(aa'\); they are not covered by a same-sign interior-shell conclusion.

### 3.2 Symmetric centre chart

Define

\[
 \alpha={a+a'\over2},\qquad \beta={b+b'\over2}.
\]

Then

\[
 a=\alpha-{p\over2},\quad a'=\alpha+{p\over2},\quad
 b=\beta-{q\over2},\quad b'=\beta+{q\over2},
\]

and the centre identities are

\[
 n=\alpha q-\beta p,qquad bb'=\beta^2-{q^2\over4}.
\tag{117.R15}
\]

The exact parity, character, phase, strip, and phase-norm chart is:

| model | parity and literal character | determinant and one-sided strip | character-conjugated centre phase |
|---|---|---|---|
| \(M1\) | \(q=2r\); \(\beta,r\in\mathbb Z\), \(\beta\pm r\) odd; \(\chi_4(b)\chi_4(b')=(-1)^r\) | \(N_1=2\alpha r-\beta p\), \(0<N_1<(\beta^2-r^2)/W\) | \(\Psi_1(r)=r/2+c(2\alpha r-\beta p)/(\beta^2-r^2)\) |
| \(M2\) | \(p=2s\); \(\alpha,s\in\mathbb Z\), \(\alpha\pm s\) odd; literal character divided by \(|aa'|\) is \((-1)^s/(aa')\) | \(N_2=\alpha q-2\beta s\), \(0<N_2<4(\beta^2-q^2/4)/W\) | \(\Psi_2(s)=c\alpha q/[4bb']+s\{1/2-c\beta/(2bb')\}\) |

Here \(b,b'>0\), so \(|q|<2\beta\), and all primitive and literal masks remain. The \(M2\) phase is exactly linear in \(s\), with geometric frequency

\[
 \theta_{2,\mathrm{ctr}}={1\over2}-{c\beta\over2bb'}.
\tag{117.R16}
\]

For a progression of \(S\) constant amplitudes its geometric norm is

\[
 G_2(S)\ll \min\left(S,\|\theta_{2,\mathrm{ctr}}\|^{-1}\right).
\]

There is no uniform nonresonance: \(c\beta/(bb')\) may be an odd integer because \(c\) is a real parameter in a comparable interval.

For \(M1\), the exact first derivative in symmetric coordinates is

\[
 \Psi_1'(r)={1\over2}+
 {2c\{\alpha(\beta^2+r^2)-\beta pr\}\over(\beta^2-r^2)^2}.
\tag{117.R17}
\]

Stationary or integer-stationary cells \(\Psi_1'(r)\in\mathbb Z\) cannot be excluded uniformly. In left-anchored coordinates, holding \(a,b,p\) fixed, the same high-pass phase has the especially transparent form

\[
 \psi_1(r)={r\over2}+c\left({a\over b}-{a+p\over b+2r}\right),
\]

\[
 \psi_1'(r)={1\over2}+{2c(a+p)\over(b+2r)^2},qquad
 \psi_1''(r)=-{8c(a+p)\over(b+2r)^3}.
\]

Thus, for a constant or controlled-BV amplitude on an interval of length \(R\), \(b+2r\asymp B\), and \(|a+p|\asymp A\), the usual second-derivative diagnostic would give

\[
 H_1(R)\ll \min\left(R,R\lambda^{1/2}+\lambda^{-1/2}\right),qquad
 \lambda\asymp {YA\over B^3}.
\]

This is only a phase norm. Applying it to the literal sum requires a separately charged variation norm of \(T_1(a+p,b+2r)/(a+p)\), the primitive mask, and the moving triangular weight.

For comparison, holding \(a,b,q\) fixed in \(M2\) gives

\[
 \psi_2(s)={caq\over4bb'}+s\left({1\over2}-{c\over2b'}\right),

\]

so the left-anchored geometric frequency is \(1/2-c/(2b')\). This is consistent with, but not identical to, (117.R16), because a centre-fixed progression moves both numerator endpoints while a left-fixed progression moves only the primed numerator.

### 3.3 The smallest complete signed survivors

After every variable except the high-pass coordinate is fixed, the \(M1\) survivor is

\[
 \begin{split}
 \mathcal S_1(\alpha,\beta,p)=
 \sum_{r\in\mathcal I_1}^{\!*}&
 {(-1)^rT_1(\alpha-p/2,\beta-r)
 T_1(\alpha+p/2,\beta+r)\over
 (\alpha-p/2)(\alpha+p/2)}\\
 &\times e\!\left({c(2\alpha r-\beta p)\over\beta^2-r^2}\right)
 \left(1-{W(2\alpha r-\beta p)\over\beta^2-r^2}\right),
 \end{split}
\tag{117.R18}
\]

where the star means: both denominators are positive odd integers; both numerators are nonzero integers; both rays are primitive and in the literal support; and \(0<2\alpha r-\beta p<(\beta^2-r^2)/W\).

The \(M2\) survivor is

\[
 \begin{split}
 \mathcal S_2(\alpha,\beta,q)=
 \sum_{s\in\mathcal I_2}^{\!*}&
 {(-1)^sT_2(\alpha-s,\beta-q/2)
 T_2(\alpha+s,\beta+q/2)\over
 (\alpha-s)(\alpha+s)}\\
 &\times e\!\left({c(\alpha q-2\beta s)\over4(\beta^2-q^2/4)}\right)
 \left(1-{W(\alpha q-2\beta s)\over4(\beta^2-q^2/4)}\right),
 \end{split}
\tag{117.R19}
\]

with the analogous literal, primitive, parity, and strict-strip masks. Factoring its phase turns (117.R19) into a Fourier coefficient at (117.R16), but of the actual nonsmooth two-ray symbol, not of the constant function.

Expanding either \(T_iT_i'\) produces

\[
 \sum_{g,g'\geq1}{\chi_4(g)\chi_4(g')\over gg'}
 U_{i,a,b}(g)U_{i,a',b'}(g').

\]

The determinant phase is independent of \(g,g'\). BV in \(g\) therefore does not imply BV, Fourier decay, or sign correlation in \(r\) or \(s\). Replacing the actual symbol in (117.R18) or (117.R19) by a constant is the first missing theorem, not an algebraic simplification.

### 3.4 GCD congruence, determinant fibres, and multiplicity

For fixed primitive \((a,b)\) and fixed \(n\),

\[
 aq-bp=n\quad\Longleftrightarrow\quad aq\equiv n\pmod b.
\]

There is one residue class \(q\pmod b\). If \((p_0,q_0)\) is one solution, every solution is

\[
 (p,q)=(p_0+at,q_0+bt),\qquad t\in\mathbb Z.
\tag{117.R20}
\]

In \(M1\), \(b\) is odd and \(q\) must be even, so \(t\) has one parity. Writing \(t=t_0+2u\) gives

\[
 (a'_u,b'_u)=(a'_0+2au,b'_0+2bu),qquad
 (-1)^{q_u/2}=\hbox{constant}\cdot(-1)^u.
\]

In \(M2\), \(a\) is odd and \(p\) must be even, so the same parametrisation gives

\[
 (a'_u,b'_u)=(a'_0+2au,b'_0+2bu),qquad
 (-1)^{p_u/2}=\hbox{constant}\cdot(-1)^u.
\]

For either model the character-conjugated fixed-determinant phase is therefore

\[
 \Psi_{i,n}(u)={u\over2}+{cn\over\kappa_i b b'_u},quad
 \Psi_{i,n}'(u)={1\over2}-{2cn\over\kappa_i(b'_u)^2},quad
 \Psi_{i,n}''(u)={8bcn\over\kappa_i(b'_u)^3}.
\tag{117.R21}
\]

When \(b,b'\asymp B\), the step in \(b'\) is \(2b\asymp B\), so a dyadic target shell contains only \(O(1)\) values of \(u\). The apparent long \((-1)^r\) or \((-1)^s\) progression is consequently transverse to the determinant fibres: its determinant changes at every step. For cross-scale shells the fibre can have \(O(1+B'/b)\) points, and that multiplicity must be charged; no comparable-shell conclusion is silently transferred to the whole block.

Primitivity of the primed ray is not automatic. It remains as

\[
 (a'_u,b'_u)=1,
\]

and every common divisor of \(a'_u,b'_u\) divides \(n=ab'_u-a'_ub\). A Möbius expansion of this mask is therefore supported on divisors of \(n\), but taking it absolutely costs \(\tau(n)\), which is only a \(Y^\varepsilon\) loss and supplies no power saving.

There is an equivalent denominator-pair multiplicity chart. Put

\[
 g=(b,b'),\qquad b=gu,quad b'=gv,quad (u,v)=1.

\]

Then solutions require \(g\mid n\), say \(n=gm\), and

\[
 av-a'u=m.
\]

One solution generates

\[
 a=a_0+ut,qquad a'=a'_0+vt.
\tag{117.R22}
\]

For \(|a|,|a'|\asymp A\) and \(b,b'\asymp B\), (117.R22) has

\[
 O\!\left(1+{Ag\over B}\right)

\]

possible values before the two primitive masks, which can only reduce the count. Large multiplicity is thus a genuine large-\((b,b')\) phenomenon and cannot be discarded by saying that a congruence has one residue.

### 3.5 Capacity before and after each norm

On a comparable denominator shell, \(|a|\asymp A=LB/D\), the number of possible primitive rays is

\[
 R_B\ll 1+AB\ll1+{LB^2\over D}.

\]

Distinct reduced fractions with denominators \(\ll B\) are separated by at least a constant multiple of \(B^{-2}\). Hence a one-sided interval of length \(\kappa_i/W\) contains

\[
 \Delta_{i,B}\ll 1+\min\left(R_B,{B^2\over W}\right)
\tag{117.R23}
\]

admissible neighbours, with \(\kappa_i\) and the single parity restriction affecting only the constant. The increment-area chart gives the same result:

| model and orientation | long coordinate | short-strip count | product before support cap |
|---|---:|---:|---:|
| \(M1\), fixed \(q=2r\) | \(\asymp B/2\) choices of \(r\) | \(\asymp B/W\) choices of \(p\) | \(\asymp B^2/(2W)\) |
| \(M1\), fixed \(p\), same-sign interior | \(\asymp A\) choices of \(p\) | \(\asymp B^2/(2WA)\) choices of \(r\) | \(\asymp B^2/(2W)\) |
| \(M2\), fixed \(q\) | \(\asymp B\) choices of \(q\) | \(\asymp2B/W\) choices of \(s\) | \(\asymp2B^2/W\) |
| \(M2\), fixed \(p=2s\), same-sign interior | \(\asymp A/2\) choices of \(s\) | \(\asymp4B^2/(WA)\) choices of \(q\) | \(\asymp2B^2/W\) |

The exact boundary cases in section 3.1 replace one nominal side by the literal support cut, but cannot exceed the total-ray cap in (117.R23).

Let

\[
 E_B=\sum_{(a,b)\ {\rm in\ the\ shell}}|A_i(a,b)|^2.

\]

Then

\[
 E_B\ll_\varepsilon
 \min\left({D\over L},{R_B\over L^2}\right)Y^\varepsilon.

\]

Using \(2|xy|\leq |x|^2+|y|^2\) and (117.R23) gives the shell capacity

\[
 C_{0,B}\ll E_B\left(1+\min\left(R_B,{B^2\over W}\right)\right).
\tag{117.R24}
\]

Summing dyadic shells and using the global energy bound, at most \(DL\) literal rays, and reduced-fraction separation at denominator \(D\), gives (117.R1), with logarithms absorbed by \(Y^\varepsilon\).

The compulsory charges after the proposed norms are:

| operation | formal replacement of the progression length | compulsory symbol or multiplicity charge | lawful capacity with the supplied data |
|---|---|---|---|
| \(M1\) stationary/second derivative | \(R\mapsto H_1(R)\) | endpoint value plus total variation of the actual coefficient, primitive mask, and triangular weight in \(r\) | no cross-ray variation bound; triangle/Cauchy restores \(R\), hence (117.R24) |
| \(M2\) geometric sum | \(S\mapsto G_2(S)\) | the same variation/Fourier norm of the actual two-ray symbol in \(s\) | exact resonances allow \(G_2=S\); otherwise trivial variation again restores \(S\) |
| Abel summation | phase partial-sum norm \(H\) | \(|C_{j_0}|+\sum_j|C_{j+1}-C_j|\) | with only pointwise control this can be \(\asymp S\sup|C|\); taking the minimum with triangle gives the original \(S\sup|C|\) |
| Cauchy in a progression | \(S\mapsto S^{1/2}\) | the second \(S^{1/2}\) appears when the available \(\ell^2\) mass is summed over the unstructured coordinate | (117.R24) |
| fixed determinant | \(O(1)\) fibre length on comparable shells | \(\asymp B^2/W\) determinant values, plus cross-scale fibre multiplicity | (117.R24) |
| Möbius/divisor expansion | primitive congruence classes | absolute \(\tau(n)\ll Y^\varepsilon\) cost | (117.R24), up to \(Y^\varepsilon\) |
| complete-lift expansion | possible \(\chi_4(g)\) cancellation | the phase has no \(g\)-dependence and \(U_{i,a,b}\) changes with the ray | no ray saving beyond (117.R4) |

Multiplication of a coefficient sequence by the unimodular high-pass/phase factor is an isometry on \(\ell^2\) and preserves pointwise magnitudes. Therefore a proof using only those two norms cannot distinguish the actual symbol from a phase-conjugated adversary. In the literal formula the symbols are real, but after taking \(2\Re\), a real sign adversary can align with the cosine on any fixed star. This observation is used only to rule out a norm-only progression lemma; it is not an assertion that the fixed literal \(U_i\) are adversarial.

At the endpoint \(B=D=Y^{1/2}\), \(A=L=Y^{1/6}\), the raw progression degree is \(Y^{27/48}\) and the energy is \(Y^{16/48}\), yielding \(Y^{43/48}\). Even the nonliteral constant-symbol diagnostics are not target-safe:

* for \(M1\), \(R=Y^{19/48}\), \(\lambda=Y^{-16/48}\), and the second-derivative norm is \(H_1\ll Y^{11/48}\), giving the formal capacity \(Y^{16/48}Y^{8/48}Y^{11/48}=Y^{35/48}\);
* for nonresonant \(M2\), replacing the \(s\)-length \(Y^{3/48}\) by \(1\) still leaves \(Y^{16/48}Y^{24/48}=Y^{40/48}\); at resonance it returns to \(Y^{43/48}\).

These two diagnostic numbers do not bound the literal survivors because their missing variation charges have not been proved.

### 3.6 Exact resonant cluster and the scope of its mass

The failure of a uniform \(M2\) geometric norm is visible without approximation. Take \(q=0\), so \(b'=b\), and vary \(p=2s\) with \(s<0\). Then

\[
 n=-2bs,qquad -{2b\over W}<s<0,

\]

and

\[
 (-1)^s e\!\left({cn\over4b^2}\right)
 =e\!\left(s\left({1\over2}-{c\over2b}\right)\right).
\tag{117.R25}
\]

If \(c/b\) is an odd integer, (117.R25) is identically \(1\). Such a value is allowed by uniformity in real \(c\asymp Y\). Choosing, for example, a power-of-two denominator and odd numerators also shows that primitivity need not destroy the progression. This is a phase/congruence control, not a lower bound for the literal correlation: the actual \(T_2\) values can vanish or cancel, and the literal stratum may remove members.

A coherent linear cluster of length \(S\asymp B/W\) has only the pointwise upper mass \(O(SL^{-2}Y^\varepsilon)\) on one star. Turning it into a block contribution requires an independently proved local mass or spectral statement for the actual coefficients. Conversely, neither coherence of one cluster nor a local block estimate supplies the complete all-block local moment implication needed for a pointwise Gauss-circle exponent.

## 4. First doubtful or unproved step

The first unproved step in every route that improves (117.R1) is a bound of the following kind for the actual survivor symbol:

\[
 \left|\sum_{j\in I} C_j e(\Psi(j))\right|
 \leq \hbox{(phase norm smaller than \(|I|\))}
 \times \hbox{(controlled norm of the actual \(C_j\))},

\]

where \(C_j\) includes both complete lift transforms, the signed numerator denominators, both primitive masks, and the triangular boundary. No raywise BV, Fourier, large-sieve, or signed correlation norm for this \(C_j\) is among the hypotheses. BV of each \(U_{i,a,b}\) in \(g\) is in a different variable and does not fill the gap.

Accordingly, the first invalid substitution would be to apply \(H_1\) or \(G_2\) as if \(C_j\) were constant, or to phase-conjugate \(C_j\) and continue to call it the literal coefficient. A lawful advance needs a new theorem that directly controls (117.R18) or (117.R19), or a determinant-fibre large-sieve/variation estimate whose right-hand side is strictly smaller than (117.R24) after every multiplicity is included.

## 5. Control tests and outcomes

| required control | exact input and expected invariant/failure | observed outcome | implication |
|---|---|---|---|
| `literal_reduced_ray_and_equal_lift_diagonal` | Use the complete coefficients (117.R3), both signs, and primitive rays; keep \(n=0\) separate. | Equal reduced frequencies are identical primitive rays, and their energy is already (117.R4). | The report bounds only the open correlation and never double-counts or reopens the lift diagonal. |
| `m1_m2_character_placement_and_factor_four` | Put the \(M1\) character on odd denominators and the \(M2\) character on odd numerators; retain \(\kappa_2=4\). | Equations (117.R6)--(117.R7) give \((-1)^r/(aa')\) and \((-1)^s/(aa')\); the \(M2\) \(s\)-strip has width \(2b'/W\), and its phase is divided by four. | No denominator/numerator swap, opposite-sign loss, or missing factor four occurs. |
| `increment_determinant_and_one_sided_orientation` | Derive from \(p=a'-a,q=b'-b\), without replacing \(n>0\) by \(|n|\). | \(n=aq-bp\), and \(a/b>a'/b'\). Only \(a>0>a'\) can be cross-sign. | All strip and phase formulas have the correct orientation. |
| `character_high_pass_progressions` | Test \(q=2r\) for \(M1\), \(p=2s\) for \(M2\), both transversely and at fixed determinant. | The transverse increments alternate, but (117.R20) plus parity changes the fibre step to \(2(a,b)\), leaving \(O(1)\) comparable-shell points. | A long increment high-pass is not a long determinant-fibre high-pass. |
| `determinant_strip_widths_and_boundary` | Price fixed-\(q\) and fixed-\(p\) strips, positive/negative rays, the centre crossing, and the triangular edge. | (117.R12)--(117.R14) and the four-case table give the exact open boundaries; the nominal \(B^2/(WA)\) width fails at \(a=\kappa_i b/W\) and saturates at literal support. | Rectangular strip replacement is permitted only away from the named transition and after a support cap. |
| `centre_phase_and_stationary_or_geometric_norm` | Pass to \((\alpha,\beta)\), retain \(bb'=\beta^2-q^2/4\), and compute the actual phase norm. | \(M2\) is linear with frequency (117.R16) and admits exact odd-integer resonances; \(M1\) has derivative (117.R17), with stationary cells, and its constant-symbol second-derivative norm carries a missing variation charge. | Neither phase norm is a uniform literal-coefficient saving. |
| `gcd_congruence_and_multiplicity` | Keep both primitive conditions; solve at fixed \((a,b,n)\) and fixed \((b,b',n)\). | Equations (117.R20)--(117.R22) give the exact progressions, \((b,b')\mid n\), multiplicity \(O(1+Ag/B)\), and the divisor cost. | Congruence reorganisation does not erase large-gcd fibres or yield an uncharged saving. |
| `capacity_before_after_each_norm` | Start with shell energy and neighbour degree; charge Abel, Cauchy, fibre count, divisor expansion, and lift expansion. | (117.R23)--(117.R24) and the norm-charge table return (117.R1). Formal phase diagnostics remain above target even before the missing symbol charge. | The stated no-go is quantitative and has no hidden norm or multiplicity gain. |
| `actual_symbol_vs_phase_conjugated_coefficients` | Compare (117.R18)--(117.R19) with a constant or demodulated amplitude. | Demodulation preserves only generic \(\ell^2/\ell^\infty\) norms, not the literal real lift identity; real cosine-aligned adversaries defeat a norm-only lemma. | A proof must identify an actual cross-ray property of \(T_i\), not rename a phase-conjugated sequence. |
| `real_Y_and_endpoint_uniformity` | Keep \(Y,W,c\) real, strict inequalities, real strip endpoints, and the triangular cutoff. | Counts use open intervals with \(+1\) boundary terms; exact resonance is allowed for real \(c\); the endpoint weight vanishes at the excluded upper boundary. | No integrality of \(Y,W,c\), endpoint averaging, or nonresonance is assumed. |
| `linear_cluster_vs_local_mass_vs_pointwise_exponent` | Test the exact \(q=0\) \(M2\) cluster and separate phase coherence, coefficient mass, block assembly, and a final exponent. | (117.R25) can be fully coherent, but its literal mass is unknown; pointwise control only gives a star upper bound. | A linear cluster is neither a lower bound nor a local-moment theorem, and no pointwise exponent follows. |
| `downstream_scope` | Compare the local open-correlation question with any all-block moment or final Gauss-circle conclusion. | The report proves only (117.R1) and the named method-class obstruction. | It does not infer M9, the quarter theorem, an internal \(5/16\) estimate, or a global exponent. |

The broader controls from `state/control_models.md` are also respected: signed and unsigned expressions are not conflated; exact \(n=0\) and near resonance are separated; coefficient adversaries are used only to delimit a norm-only proof class; both signs, primitive degeneracies, dyadic endpoints, and literal support cuts remain explicit. No numerical experiment is used as proof.

## 6. Dependencies and exact artifacts used

Only the following artifacts were used:

1. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/briefs/blind_determinant_fibre_rederivation.md` — task scope, required controls, and report contract.
2. `problems/gauss_circle.md` — problem-level downstream scope.
3. `state/control_models.md` — proof-unit control requirements.
4. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/blind_statement.md` — all mathematical hypotheses, literal coefficients, open correlation, hard region, and target.

No proof graph, strategy file, Round-94/95 artifact, Round-117 derivation packet or candidate, sibling report, web source, or numerical computation was used.

## 7. Recommended state effect

**Retain** this report as candidate evidence for the exact charts and for the narrowly stated norm-only determinant-fibre/high-pass no-go. Do not promote (117.B3), a strict hard-subrange target, or a quantified literal saving from this report. The actionable revision to the mechanism is to require a new, explicitly charged cross-ray signed norm for (117.R18) or (117.R19), or a determinant-fibre estimate that survives the congruence, primitive masks, lift dependence, and capacity audit. Shared proof state should otherwise remain unchanged pending conductor and seam review.

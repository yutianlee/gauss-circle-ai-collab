# Round 148 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate
- Round: 148
- Starting graph SHA-256: bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352
- Terminal label: squarefree_reciprocal_dispersion_no_go

## 1. Decision

Round 148 accepts one exact reciprocal-transform reduction and one
strictly scoped method/source obstruction.

Let \(R=X^{1/4}\), \(N=\lfloor X\rfloor\),
\(DE\asymp M\leq R^2\), \(D\leq\sqrt M\), and retain an inherited
half-open prefix.  After separately pricing a product collar of width
\(O(\sqrt M)\) and a cone collar of width \(O(\sqrt D)\), define the
exact finite progression set

$$
 \mathcal P(d)=\left\{(\alpha,b):
 \begin{array}{l}
 \alpha,b\ {\rm odd},\quad \mu(\alpha)\mu(b)\ne0,\quad b\mid d,\\
 \alpha^2\le e_+\ll E,\quad
 \{n\ge1:\mathscr A(d,[\alpha^2,b]n)\ne0\}\ne\varnothing
 \end{array}\right\}.
$$

Then the retained \(t=1\) box is

$$
 \mathcal S_{D,E,U}
 =\frac{e(1/8)}{N^{1/4}D}\mathcal T_{D,E,U}
 +O_{\varepsilon,V}(X^\varepsilon),
$$

where

$$
\begin{aligned}
 \mathcal T_{D,E,U}={}&
 \sum_d\mu^2(d)\frac Dd
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \mu(\alpha)\mu(b)\frac{\chi_4(\ell)}{\ell}\\
 &\quad\times
 \sum_{\substack{q>0\\q\ {\rm odd}}}
 \chi_4(q)\mathscr W_{d,\ell,U}(q)
 e\!\left(\frac{Nd\ell}{q}\right),
 \qquad \ell=[\alpha^2,b],
\end{aligned}
$$

$$
 \mathscr W_{d,\ell,U}(q)
 =\mathscr A\!\left(d,\frac{4Nd\ell^2}{q^2}\right),
 \qquad
 q\asymp\ell Q,\qquad
 Q=2\sqrt{ND/E}\asymp D\sqrt{N/M}.
$$

The transformed target is

$$
 |\mathcal T_{D,E,U}|\ll_{\varepsilon,V}RD X^\varepsilon.
$$

The target is not proved.

The accepted obstruction concerns only a long interior prefix on which
the individual Mobius progression cells are left unrecombined, weighted
Cauchy is applied to those cells, and the \(d_1=d_2\) diagonal is then
majorized separately by a nonnegative quantity.  On the literal
\(b=1\) subfamily its cell mass is

$$
 \mathscr L\asymp Q\sqrt E,
$$

and every positive Cauchy weighting has diagonal capacity at least

$$
 \sqrt D\,\mathscr L
 \asymp Q\sqrt{DE}
 =\sqrt N\,D
 =R(RD).
$$

Thus that proof placement loses exactly \(R\).  This is an adverse
upper capacity, not a lower bound for the signed scalar.  It says
nothing against pre-Cauchy recombination, signed cross-cell
cancellation, or another joint energy.

No strict owner-complete range, no \(t=1\) target, no downstream
theorem, and no exponent improvement are accepted.

## 2. Exact transform and remainder adjudication

The arithmetic expansion

$$
 \mu^2(e){\bf1}_{(d,e)=1}
 =\sum_{\alpha^2\mid e}\mu(\alpha)
  \sum_{b\mid(d,e)}\mu(b)
$$

is accepted only with the finite set \(\mathcal P(d)\) retained before
Poisson.  The continuous saddle weight alone does not truncate
\(\alpha\).

For
\(\widehat F(\xi)=\int_{\mathbb R}F(x)e(-\xi x)\,dx\),

$$
 \sum_n\chi_4(n)F(n)
 =\frac i2\sum_{\substack{q\in\mathbb Z\\q\ {\rm odd}}}
 \chi_4(q)\widehat F(q/4).
$$

The positive-frequency integral has

$$
 x_0=\frac{4Nd\ell}{q^2},\qquad
 e_0=\frac{4Nd\ell^2}{q^2},\qquad
 \lambda=\frac{Nd\ell}{q},\qquad
 \phi''(x_0)=-\frac{q^3}{32Nd\ell}.
$$

The exact substitution \(x=x_0(1+u)^2\) gives
\(\phi=\lambda(1-u^2)\).  The leading integral is

$$
 \frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 \mathscr A(d,e_0),
$$

and the Poisson factor produces
\(ie(-1/8)=e(1/8)\).  Hence the reciprocal phase sign, global unit,
\(1/(d\ell)\) amplitude, and \(q\asymp\ell Q\) support are accepted.

The repaired \(K=6\) remainder proof uses an even saddle cutoff, an
exact difference convention containing the complementary Taylor
polynomial and extended-domain tail, the finite mass

$$
 \sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q\asymp\ell Q\}
 \ll_\varepsilon DQ\sqrt E\,X^\varepsilon,
$$

and a four-range \(q\)-partition.  In the scaled variable
\(y=\ell x/E\), the tails satisfy

$$
 |\partial_y\phi|
 \gg\sqrt{NM}\left(1+\frac{|q|}{\ell Q}\right).
$$

Six integrations by parts and dyadic tail summation give geometric
factor \(2^{-5v}\).  With
\(\Lambda=\sqrt{NM}=R^2\sqrt M\), the stationary remainder uses

$$
 M^{-1/2}(M/\Lambda)^6,\qquad
 {\bf1}_{M\asymp D^2}D^{-1/2}(D/\Lambda)^6,
$$

while the nonstationary conversion includes the required
\(\Lambda^{1/2}\) factor.  All terms are negative powers after the
leading capacity \(R\sqrt D\), and the complete post-Poisson error is
\(O_{\varepsilon,V}(X^\varepsilon)\).  The target-equivalence is
therefore accepted for every prefix, including the separately owned
short-prefix case.

## 3. Resonance, diagonal, and source adjudication

If \(g=(\ell,q)\), \(L=\ell/g\), and \(q_0=q/g\), then

$$
 e(Nd\ell/q)=e(NLd/q_0),\qquad
 j=NL-Aq_0,\qquad |j|<q_0/2,\qquad q_0\mid NL-j.
$$

The provisional bare coordinate \(j=N-Aq\) is correct only for the
unexpanded \(\ell=1\) cell.  A general \(L=1\) lift uses \(q_0\).
The fully reduced additive denominator is

$$
 q_*=\frac q{(q,\ell N)}=\frac{q_0}{(q_0,N)}.
$$

The \(j=0\) family is target-safe by divisor multiplicity.  The
nonzero-\(j\) signed family remains open.

For the diagonal control, choose a long interior rectangle
\(\mathcal J_d\times\mathcal J_e\) of respective lengths
\(\asymp D,\asymp E\).  Taking \(b=1\), odd squarefree
\(\alpha\) with \(\alpha^2\in\mathcal J_e\), and a fixed interval for
\(q/(\alpha^2Q)\) puts every selected cell in \(\mathcal P(d)\),
gives \(\asymp\alpha^2Q\) frequencies per \(\alpha\), and yields a
common \(d\)-norm \(\gg D\).  This proves the displayed
\(Q\sqrt E\) mass and factor-\(R\) diagonal loss.  A collar-short
prefix is not assigned that lower mass.

Literal equality of reduced fractions is not the only phase alignment:

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}
$$

may create further fibres.  Those fibres and every pre-Cauchy
regrouping are outside the no-go.

The audited pointwise prime, squarefree, and smooth progression
theorems touch only small \(q_*\)-strata already bounded by
\(DYX^\varepsilon\) for \(Y\le R\).  Nunes's variance theorem is a
fixed-modulus residue-class average with its own diagonal.
Schlage--Puchta at the exact reduced denominator gives
\(D^{1+\varepsilon}/q_*+q_*D^\varepsilon\), but exact multiples
already improve the small-\(q_*\) case and the remaining admissible
approximants are not jointly classified.  The source supplies no
varying-\(q\) aggregation theorem for the actual coupled coefficient.
The fixed-modulus inverse-square and inverse-fraction complete sums
have mismatched phases, averages, or diagonals.

The Round-147 powerful \(H\)-index is not termwise
\(\ell=[\alpha^2,b]\), which need not be powerful.  The reciprocal
band \(|j|\ll LQ\) is also a factor \(D\) wider than the formal
\(H\)-band \(|j_H|\lesssim LQ/D\).  Complete identities reconstruct
the same physical box only after all remainders, inverse transforms,
and Euler recombination.

## 4. Evidence adjudication

The discovery report is accepted after repairs for the finite
progression support, exact character-Poisson transform, saddle
constants, uniform remainder, correct reduced resonance coordinate,
long-prefix diagonal construction, and scoped method no-go.

The statement-only report is accepted for the conditional signed-energy
gate, the target-safe literal \(q\)-diagonal in a genuinely joint
energy, the arbitrary-coefficient duality warning, and the proof that
separately triangulating the Mobius expansion supplies no growing-\(D\)
target-safe range.  It prevents the cellwise obstruction from being
misstated as a no-go for every joint dispersion form.

The source report is accepted after repairs for the exact theorem
cards, the small-\(q_*\) count, the direct-specialization limitations,
the separable large-sieve diagnostic, the phase and diagonal
mismatches, and the \(H\)-bandwidth mismatch.

The initial transform and source reviews returned AMBER and forced the
finite-support, Gaussian-remainder, common-rectangle, source-hypothesis,
and scope repairs.  The terminal reviews are:

- source_conductor_round148_final.md: GREEN;
- blind_conductor_round148_candidate_final_v2.md: GREEN.

The conductor independently checked the squarefree expansion, Gaussian
unit, remainder powers, \(Q\sqrt E\) mass, positive-weight inequality,
small-\(q_*\) count, and every \(R,M,D,E,Q\) translation.

## 5. Accepted statements and rejected inferences

The graph may record:

1. the exact finite signed reciprocal transform and complete
   target-safe analytic remainder;
2. the literal support \(q\asymp\ell Q\), reciprocal phase, amplitude,
   profile, and \(RD\) target;
3. the reduced coordinate \(j=NL-Aq_0\), exact divisors, imprimitive
   lifts, and target-safe zero family;
4. the long-prefix factor-\(R\) obstruction for unrecombined
   progression-cell Cauchy followed by a separately positive diagonal;
5. the arbitrary-\(q\)-coefficient countermodel and the fact that the
   absolute squarefree \(Q+D\) analogue remains unresolved;
6. the small-\(q_*\) elementary owner and the exact non-applicability
   of the audited source interfaces; and
7. the non-powerful-index and bandwidth mismatch with the Round-147
   \(H\)-correlation.

Reject the inferences that:

1. the saddle weight alone makes the square-divisor expansion finite;
2. \(j=N-Aq\) parameterizes every expanded progression;
3. arbitrary bounded outer \(q\)-coefficients can replace the actual
   \(\chi_4(q)\mathscr W(q)\);
4. the bare \(Q+D\) lemma or an unproved squarefree analogue gives the
   target;
5. positive reweighting repairs the fixed unrecombined
   progression-cell diagonal;
6. primitive fraction reduction removes all \(N\)-dependent aligned
   fibres;
7. the exact-denominator Schlage--Puchta specialization exhausts that
   theorem;
8. any audited fixed-modulus complete-sum theorem directly matches the
   varying-denominator signed form;
9. \(\ell\) can be identified termwise with the powerful \(H\)-index;
10. a second transform itself gives new cancellation;
11. the adverse diagonal capacity is a signed lower bound; or
12. this round proves \(t=1\), M9--M1, M9--M2, endpoint uniformity,
    M9, the bridge, the quarter target, or an exponent improvement.

## 6. First open owner and downstream scope

The first open arithmetic statement is the coefficient-sensitive joint
bound

$$
 |\mathcal T_{D,E,U}|\ll_{\varepsilon,V}RD X^\varepsilon
$$

with the \((\alpha,b,q)\) cells, common-divisor strata,
\(\chi_4(q)\), coupled profile, and prefixes kept together before any
separately positive diagonal.  An alternative is exact Euler
recombination followed by a signed theorem for

$$
 h_z(k)A_{-z}(kN+j),\qquad
 |j|\lesssim k\sqrt{N/M},
$$

over the actual cone orders.  Neither theorem is proved.

A separate \(t=1\) estimate remains sufficient only for a layerwise
route.  A genuinely joint cross-\(t\) theorem could bypass it.
Every \(t\ge2\) layer and the independent Round-138 cross owner remain
open.

M9--M1, M9--M2, endpoint uniformity, M9, the conditional bridge, and
the Gauss target remain open.  The internal exponent remains \(1/3\);
the separately audited external exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
$$

## 7. Recommended state effect

Create:

1. M9-M1-lower-cone-t1-squarefree-reciprocal-transform-reduction;
2. M9-M1-lower-cone-t1-squarefree-reciprocal-dispersion-obstruction.

Attach both to the exact unmasked small-\(t\) owner and the global
lower-radial signed obligation.  Link the reciprocal obstruction to the
Round-147 \(H\)-obstruction without asserting termwise equivalence.

Retain the signed \(t=1\) target, every strict range, all downstream
owners, the internal exponent, the external audited exponent, and the
quarter target unchanged.

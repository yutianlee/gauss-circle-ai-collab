# Round 148 conductor candidate: exact squarefree reciprocal transform and scoped dispersion no-go

- Campaign: `m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate`
- Round: 148
- Role: conductor-selected proof kernel
- Starting graph SHA-256: `bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352`
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Result and exact scope

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq \sqrt M,
$$

and let (M\leq U\leq B_M\leq2M) be an inherited half-open
prefix.  On a (d\asymp D,e\asymp E) box, the (t=1) face is

$$
 \mathcal S_{D,E,U}=
 \sum_{d,e\geq1}
 \mu^2(de){\bf1}_{e\ {\mathrm{odd}}}\chi_4(e)(de)^{-3/4}
 e(+\sqrt{Nde})\,
 \omega_D(d)\omega_E(e)V_{\rm low}(R^2de/N)
 {\bf1}_{M\leq de<U}{\bf1}_{e>4d}.
\tag{148.C1}
$$

After peeling target-safe radial-prefix collars of product width
(O(\sqrt M)) and a target-safe cone collar

$$
 |e-4d|\ll\sqrt D,
\tag{148.C2}
$$

there is a compact-smooth amplitude
(\mathscr A_{D,E,U}(d,e)), exact on every retained lattice point.
Choose \(e_+\ll E\) so that its \(e\)-support lies in \((0,e_+]\),
and, for each \(d\), put

$$
 \mathcal P(d)=\left\{(\alpha,b):
 \begin{array}{l}
 \alpha,b\ {\mathrm{odd}},\quad \mu(\alpha)\mu(b)\ne0,\quad b\mid d,\\
 \alpha^2\le e_+,\quad
 \{n\ge1:\mathscr A_{D,E,U}(d,[\alpha^2,b]n)\ne0\}\ne\varnothing
 \end{array}\right\}.
\tag{148.C2a}
$$

This is the exact finite progression support inherited from
\(\alpha^2\mid e\); evaluating the continuous weight at a saddle does
not impose it.  With this convention,

$$
 \boxed{
 \mathcal S_{D,E,U}=
 \frac{e(1/8)}{N^{1/4}D}\,\mathcal T_{D,E,U}
 +O_{\varepsilon,V}(X^\varepsilon).}
\tag{148.C3}
$$

Here

$$
\boxed{
\begin{aligned}
 \mathcal T_{D,E,U}={}&
 \sum_d\mu^2(d)\frac Dd
 \sum_{(\alpha,b)\in\mathcal P(d)}\mu(\alpha)\mu(b)
 \frac{\chi_4(\ell)}{\ell}                                      \\
 &\quad\times
 \sum_{\substack{q>0\\q\ {\mathrm{odd}}}}
 \chi_4(q)\mathscr W_{d,\ell,U}(q)
 e\!\left(\frac{Nd\ell}{q}\right),
 \qquad \ell=[\alpha^2,b],
\end{aligned}}
\tag{148.C4}
$$

with

$$
 \mathscr W_{d,\ell,U}(q)=
 \mathscr A_{D,E,U}\!\left(d,\frac{4Nd\ell^2}{q^2}\right),
 \qquad
 q\asymp\ell Q,
 \qquad
 Q:=2\sqrt{ND/E}\asymp D\sqrt{N/M}.
\tag{148.C5}
$$

The factor (2), reciprocal phase sign, global unit, progression
length, (1/\ell), character (\chi_4(q)), and coupled profile are
literal.  In particular the transformed target is

$$
 |\mathcal T_{D,E,U}|\ll_{\varepsilon,V}
 N^{1/4}D X^\varepsilon\asymp RD X^\varepsilon.
\tag{148.C6}
$$

The target (148.C6) is not proved.  No strict owner-complete range is
proved.  The round instead establishes that the proposed
Mobius-progression separation followed by a positive
diagonal/off-diagonal Cauchy ledger loses a factor (R), and that the
audited squarefree-progression and complete-sum theorems do not supply
the missing joint signed estimate.  Thus the selected terminal label is

$$
 \boxed{\mathsf{squarefree\_reciprocal\_dispersion\_no\_go}.}
\tag{148.C7}
$$

This is a method no-go and an adverse upper-capacity statement, not a
lower bound for (148.C4) and not an impossibility theorem for a signed
cross-progression estimate.  It does not supersede the stronger
Round-147 (H)-organization.

## 2. Exact arithmetic and one-sided transform

The arithmetic identity is

$$
 \mu^2(de)=\mu^2(d)\mu^2(e){\bf1}_{(d,e)=1},
\qquad
 \mu^2(e){\bf1}_{(d,e)=1}
 =\sum_{\alpha^2\mid e}\mu(\alpha)
  \sum_{b\mid(d,e)}\mu(b).
\tag{148.C8}
$$

Because (e) is odd, only odd (alpha,b) occur.  Writing
(e=\ell n), (ell=[\alpha^2,b]), retains every Mobius sign and
gives the primitive character-Poisson identity

$$
 \sum_{n\in\mathbb Z}\chi_4(n)F(n)
 =\frac i2\sum_{\substack{q\in\mathbb Z\\q\ {\mathrm{odd}}}}
 \chi_4(q)\widehat F(q/4).
\tag{148.C9}
$$

For the Fourier convention
(\widehat F(\xi)=\int_{\mathbb R}F(x)e(-\xi x)\,dx), the relevant
integral is

$$
 I_{d,\ell,q}=\int_0^\infty(d\ell x)^{-3/4}
 \mathscr A_{D,E,U}(d,\ell x)
 e\!\left(\sqrt{Nd\ell x}-\frac{qx}{4}\right)\,dx.
\tag{148.C10}
$$

For (q>0), it has the unique saddle

$$
 x_0=\frac{4Nd\ell}{q^2},\qquad
 e_0=\ell x_0=\frac{4Nd\ell^2}{q^2},\qquad
 \lambda=\frac{Nd\ell}{q},\qquad
 \phi''(x_0)=-\frac{q^3}{32Nd\ell}.
\tag{148.C11}
$$

The substitution (x=x_0(1+u)^2) makes the phase exactly
(\lambda(1-u^2)).  Its leading Gaussian term is

$$
 I_{d,\ell,q}=
 \frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 \mathscr A_{D,E,U}(d,e_0)+\text{lower symbols and remainder}.
\tag{148.C12}
$$

Multiplication by the Poisson factor (i/2) gives
(ie(-1/8)=e(1/8)), proving the normalization and sign in
(148.C3)--(148.C5).  The dual zero frequency vanishes because the
Gauss transform of (chi_4) is zero at even frequencies; negative
(q) is nonstationary for the positive physical phase.  This does not
remove the distinct zero residue of an optional hard-cone Perron
presentation.

Taylor expansion after the exact quadratic substitution gives, for
fixed (K), the symbol coefficients

$$
 \frac{H_{d,\ell,q}^{(2r)}(0)}{r!(8\pi i\lambda)^r},
 \qquad 0\leq r<K,
\tag{148.C13}
$$

where
(H(u)=(1+u)^{-1/2}\mathscr A(d,e_0(1+u)^2)).  Since
(\lambda\asymp\sqrt{NM}), the bulk (r=1) factor is
(\lambda^{-1}).  A radial transition occupies an
(O(M^{-1/2})) fraction of the (q)-support and contributes the
relative factor (M^{1/2}/\lambda\); a cone transition occurs only for
(M\asymp D^2), occupies an (O(D^{-1/2})) fraction, and contributes
(D^{1/2}/\lambda).  Against the leading absolute capacity, these cost
respectively

$$
 \frac1{R\sqrt E},\qquad \frac{\sqrt D}{R},\qquad \frac1R.
\tag{148.C14}
$$

They are target-safe because (D\leq R).  Here is the exact
remainder convention and the summed estimate used in (148.C3).  Choose
an even cutoff \(\eta\), supported in \(|u|<1/2\) and equal to one in
\(|u|\leq1/4\), and extend \(H\) by zero to \(u\leq-1\).  For \(q>0\)
define \(\mathcal R_K(d,\ell,q)\) by the exact equality

$$
 I_{d,\ell,q}=
 \frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 \sum_{r=0}^{K-1}
 \frac{H_{d,\ell,q}^{(2r)}(0)}{r!(8\pi i\lambda)^r}
 +\mathcal R_K(d,\ell,q).
\tag{148.C14a}
$$

The full Gaussian moments in this definition are obtained by inserting
a damping factor and taking its limit.  In the cutoff proof,
\(\mathcal R_K\) includes the localized Taylor remainder, the
complementary Taylor-polynomial subtraction, and the extended-domain
tail.  For \(q\leq0\) put \(\mathcal R_K=I_{d,\ell,q}\).

Set \(K=6\).  For completeness, partition \(q\) into \(q\leq0\),
\(0<q<c\ell Q\), \(c\ell Q\leq q\leq C\ell Q\), and
\(q>C\ell Q\), with dyadic subdivision in the two tails.  In the middle
range use the exact quadratic coordinate above.  In the tails, use the
scaled coordinate \(y=\ell x/E\).  After the adjacent endpoint buffer,
$$
 |\partial_y\phi|\gg
 \Lambda\left(1+\frac{|q|}{\ell Q}\right).
$$
Six integrations by parts are uniform, and a dyadic \(q\)-tail of
relative size \(2^v\) has geometric factor \(2^{-5v}\).  The amplitude derivative
scales are \(1\) in the bulk, \(M^{j/2}\) on a radial transition, and
\(D^{j/2}\) on a cone transition.  The last two transitions occupy,
respectively, \(O(M^{-1/2})\) and \(O(D^{-1/2})\) of the middle
\(q\)-range.  The finite middle-range mass is
$$
 \sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q:q\asymp\ell Q,\ q\ {\mathrm{odd}}\}
 \ll_\varepsilon DQ\sqrt E\,X^\varepsilon.
\tag{148.C14b}
$$
With \(\Lambda=\sqrt{NM}=R^2\sqrt M\), this mass bound and the
geometric tail sum give the following bound for the literal
post-Poisson error:

$$
 \mathcal E_{\geq1}:=
 \frac12\sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \sum_{\substack{q\in\mathbb Z\\q\ {\mathrm{odd}}}}
 \left|I_{d,\ell,q}
 -{\bf1}_{q>0}
 \frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 H_{d,\ell,q}(0)\right|.
\tag{148.C14c}
$$

Indeed,

$$
 \begin{aligned}
 \mathcal E_{\geq1}
 \ll_{\varepsilon,V}X^\varepsilon R\sqrt D\bigg(
 &\Lambda^{-1}
 +M^{-1/2}\frac{M}{\Lambda}
 +{\bf1}_{M\asymp D^2}D^{-1/2}\frac D\Lambda\\
 &+\Lambda^{-6}
 +M^{-1/2}\left(\frac{M}{\Lambda}\right)^6
 +{\bf1}_{M\asymp D^2}D^{-1/2}
       \left(\frac{D}{\Lambda}\right)^6\\
 &+\Lambda^{1/2}\left[
       \Lambda^{-6}
       +M^{-1/2}\left(\frac{\sqrt M}{\Lambda}\right)^6
       +{\bf1}_{M\asymp D^2}D^{-1/2}
          \left(\frac{\sqrt D}{\Lambda}\right)^6
     \right]
 \bigg)
 \ll_{\varepsilon,V}X^\varepsilon.
 \end{aligned}
\tag{148.C14d}
$$

The first line is exactly
\(1/(R\sqrt E)+\sqrt D/R+1/R\); every higher stationary symbol
gains \(M/\Lambda\leq R^{-1}\), \(D/\Lambda\ll R^{-2}\), or
\(\Lambda^{-1}\).  The second line is the order-six stationary
remainder.  The final bracket, including the \(\Lambda^{1/2}\)
conversion from an unintegrated oscillatory integral to leading
stationary capacity, owns the negative frequencies, positive tails,
endpoint buffer, and complementary polynomial term.  Every displayed
term is a negative power of \(R\) after multiplication by
\(R\sqrt D\).  The same estimate holds for a prefix
shorter than its radial collar because that prefix was already assigned
to the primal owner.  Together with the separately priced collars,
this proves the target-equivalence (148.C3) for every inherited prefix.

## 3. Correct reduced resonance coordinate

The campaign's provisional coordinate (j=N-Aq) is not valid for the
expanded squarefree progressions.  Put

$$
 g=(\ell,q),\qquad L=\ell/g,\qquad q_0=q/g.
$$

Then

$$
 e(Nd\ell/q)=e(NLd/q_0),\qquad (L,q_0)=1,
\tag{148.C15}
$$

and the exact nearest-integer coordinate is

$$
 A=\operatorname{nint}(NL/q_0),\qquad
 j=NL-Aq_0,\qquad |j|<q_0/2.
\tag{148.C16}
$$

There is no tie because (q_0) is odd.  Hence

$$
 q_0\mid NL-j,
\tag{148.C17}
$$

and a fixed nonzero (j) has divisor multiplicity
(O_\varepsilon(X^\varepsilon)), but both the harmonic coordinate and
the modulus depend on (L).  The bare relation with the original
\(q\), \(j=N-Aq\), describes only the unexpanded \(\ell=1\) cell.
On a general \(L=1\) lift the correct formula is \(j=N-Aq_0\).
If squarefreeness of (d) is also expanded, the gcd of
(q) with (gamma^2\ell) creates still more reduced strata; it does
not restore the bare relation.

The exact (j=0) family is target-safe by itself.  From
((L,q_0)=1), (j=0) forces (q_0\mid N), and the remaining lifts
and divisor variables have only divisor-function multiplicity.  The
open difficulty is the complete nonzero-(j) signed family.

## 4. Scoped progression-diagonal obstruction

The obstruction is witnessed on a long retained prefix; no lower mass
is asserted for a prefix already absorbed by the short-prefix collar.
Choose a compact interior rectangle

$$
 \mathcal J_d\times\mathcal J_e,\qquad
 |\mathcal J_d|\asymp D,\quad |\mathcal J_e|\asymp E,
\tag{148.C17a}
$$

on which the cone, radial, dyadic, and prefix profiles have modulus
bounded below.  Such a rectangle is selected away from the owned
collars in any long interior box used for this control.  Take \(b=1\)
and odd squarefree \(\alpha\) with
\(\alpha^2\in\mathcal J_e\).  There are \(\asymp\sqrt E\) such
\(\alpha\).  For every squarefree \(d\in\mathcal J_d\),
\((\alpha,1)\in\mathcal P(d)\) through the literal progression point
\(n=1\).  Restrict \(q/(\alpha^2Q)\) to a fixed compact interval for
which

$$
 e_0(d,\alpha^2,q)\in\mathcal J_e
 \quad(d\in\mathcal J_d).
\tag{148.C17b}
$$

This leaves \(\asymp\alpha^2Q\) odd frequencies for each \(\alpha\).
For \(i=(\alpha,q)\), let

$$
 c_i=\frac{\mu(\alpha)\chi_4(q)}{\alpha^2},
 \qquad q\asymp\alpha^2Q,
 \qquad \alpha\ll\sqrt E\quad(\alpha^2\in\mathcal J_e).
\tag{148.C18}
$$

On a dyadic block (alpha\asymp A), the (q)-count is
(\asymp\alpha^2Q), and therefore

$$
 \sum_{i:\alpha\asymp A}|c_i|^2\asymp Q/A,
 \qquad
 \sum_{i:\alpha\asymp A}|c_i|\asymp QA.
\tag{148.C19}
$$

Thus the complete progression-cell absolute mass is

$$
 \mathscr L:=\sum_i|c_i|\asymp Q\sqrt E.
\tag{148.C20}
$$

Write \(S_i=\sum_{d\in\mathcal J_d}a_{i,d}\), with
\(a_{i,d}\) equal to the actual \(D/d\), profile, character, and phase
factor in (148.C4).  The rectangle and (148.C17b), together with the
positive density of squarefree \(d\), give

$$
 \sum_{d\in\mathcal J_d}|a_{i,d}|^2\geq c_0D
\tag{148.C20a}
$$

uniformly in the selected cells.  Suppose one applies
coefficient-weighted Cauchy to
these unrecombined cells and then replaces the \(d_1=d_2\) part of
each \(|S_i|^2\) by a separate nonnegative majorant.  For arbitrary
positive weights \(\rho_i\), that diagonal contributes at least

$$
 c_0D\left(\sum_i|c_i|\rho_i\right)
  \left(\sum_i|c_i|\rho_i^{-1}\right)
 \geq c_0D\left(\sum_i|c_i|\right)^2.
\tag{148.C21}
$$

After taking square roots, the minimum diagonal capacity is

$$
 \sqrt D\,\mathscr L
 \asymp Q\sqrt{DE}=Q\sqrt M=\sqrt N\,D
 =R\,(RD).
\tag{148.C22}
$$

This proves a factor-(R) loss for precisely this early
progression-cell Cauchy placement on the long interior family.  A
uniform proof menu must in particular handle that family; the argument
makes no diagonal-mass assertion for a collar-short terminal prefix.
Gcd partitioning is a bijective partition and preserves this
norm.  Primitive reduced cells retain the bulk of (148.C20); aligned
fibres \(q=\alpha^2r\) carry only \(O(Q)\) mass and do not account for
the loss.  Equality of two reduced fractions rules out only literal
duplicates.  The actual integer-\(d\) phases can also align when

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}.
\tag{148.C22a}
$$

These \(N\)-dependent fibres, every pre-Cauchy regrouping, and all
signed cross-cell cancellation are expressly outside the no-go.

Equation (148.C22) is not the diagonal of every conceivable joint
dispersion form.  In particular, a (d)-energy that retains the actual
signed sum over all progression cells before forming a positive
quadratic form may have a target-safe literal (q)-diagonal.  Its
cross-((\alpha,b)), common-divisor, and (chi_4(q)) off-diagonal is
exactly the missing theorem.  Therefore (148.C22) must not be promoted
as a lower bound or as a global obstruction to (148.C6).

## 5. False analogues, source obstruction, and the (H)-interface

An arbitrary bounded outer (q)-coefficient is a false analogue.  At
(D=1), choose the coefficient on an interior plateau to align with
(\chi_4(q)\mathscr W(q)e(N/q)).  The scalar is then
(\gg Q), while the target is (R), and (Q>R) whenever
(M<R^2).  The actual character and coupled B-process profile may not
be discarded.

The separate absolute squarefree assertion

$$
 \sum_{q\asymp Q}\left|
  \sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
 \stackrel{?}{\ll}(Q+D)X^\varepsilon
\tag{148.C23}
$$

is neither proved nor refuted.  Expanding (mu^2(d)) and taking
triangle gives only (Q\sqrt D+D).  A positive second moment exposes
the (QD) squarefree diagonal and gives capacity (Q\sqrt D) when
(Q\gg D).  Neither fact is a signed lower bound.

The distinct power placements are:

| Placement | Capacity relative to \(RD\) |
|---|---:|
| bare \(Q+D\) | \(R/\sqrt M+1/R\) |
| expand \(\mu^2(d)\), then use the bare lemma termwise | \(R\sqrt D/\sqrt M+1/R=R/\sqrt E+1/R\) |
| full absolute mass of the \(e\)-progression cells | \(R\sqrt D\) |
| unrecombined progression-cell Cauchy with separately positive \(d\)-diagonal | \(R\) |
| Round-147 \(H\)-menu | \(M^{1/4}\) below \(R^{4/3}\), \(R^{1/2}M^{-1/8}\) above |

Every row is an upper capacity for its stated placement, not a signed
lower bound.  In particular the three losses \(R/\sqrt E\),
\(R\sqrt D\), and \(R\) must not be conflated.

For a fixed progression cell, the reduced additive denominator is

$$
 q_*:=q/(q,\ell N)=q_0/(q_0,N).
\tag{148.C24}
$$

Three pointwise progression theorems cover only special moduli:
Nunes Theorem 1.1 gives prime \(q_*\leq D^{13/19-\varepsilon}\);
the least-squarefree theorem gives squarefree
\(q_*\leq D^{25/36-\varepsilon}\); and Mangerel Theorem 1.1 gives
squarefree smooth \(q_*\leq D^{196/261-\varepsilon}\).
Nunes's variance Theorems 1.1--1.2 allow \(q_*\leq D\), but average
residue-class errors at one fixed modulus and contain a genuine
diagonal main term.  Schlage-Puchta Theorem 3 imposes no special
modulus family but gives only the pointwise additive estimate
(148.C26).  Thus none is the required varying-denominator signed
estimate.  Moreover, the number of cells with
(q_*\leq Y) is (O_\varepsilon(YX^\varepsilon)) for fixed
(ell), and after the exact (1/\ell) and divisor aggregation their
whole contribution is

$$
 O_\varepsilon(DY X^\varepsilon).
\tag{148.C25}
$$

Thus every (Y\leq R), including the published progression ranges,
touches only a stratum already target-safe by elementary counting.
Choosing the exact reduced denominator in Schlage--Puchta Theorem 3
gives the valid pointwise specialization

$$
 \sum_{d\asymp D}\mu^2(d)e(\ell Nd/q)
 \ll_\varepsilon D^{1+\varepsilon}/q_*+q_*D^\varepsilon
\tag{148.C26}
$$

This exact-denominator specialization aggregates, even in a favorable
coprime cell, to (D/\ell+\ell Q^2), or to (QD) after reverting to
the trivial bound.  It is not an exhaustive use of that theorem:
when (q_*\leq\sqrt D), an exact multiple of (q_*) in
([\sqrt D,2\sqrt D]) gives (O(D^{1/2+\varepsilon})), and the other
admissible approximants for larger (q_*) have not been jointly
classified.  The source contains no theorem aggregating those choices
over the varying outer (q).  Fixed-modulus inverse-square Kloosterman
correlations and
inverse Kloosterman-fraction estimates have the wrong phase, averaging
family, or diagonal hypotheses for the varying-denominator linear
reciprocal phase in (148.C4).  Consequently the audited literature does
not prove (148.C6).

The complete identity (148.C3), including collars, lower symbols, and
remainders, and the complete Round-147 identity reconstruct the same
physical box only after all inverse transforms and Euler recombination.
The leading scalar (148.C4) is not independently or termwise identical
to the \(H\)-correlation.  There is no termwise substitution
(k=\ell): the present (ell=[\alpha^2,b]) need not be powerful,
whereas the Round-147 (k) is the powerful Euler-convolution index.
There is also a bandwidth mismatch.  The reciprocal nearest-integer
coordinate has its natural range (|j|\ll LQ), whereas the formal
Round-147 choice (k=L) would retain only
(|j_H|\lesssim LQ/D); no estimate owns the complementary range.
A second canonical
transform of the reciprocal phase returns the original square-root
phase.  It supplies no new cancellation by itself.

## 6. Controls, first open seam, and dependencies

The control outcomes are:

1.  The character-Poisson constant, (e(1/8)), positive reciprocal
    phase, (q\asymp\ell Q), (1/(d\ell)) amplitude, (RD) target,
    collars, prefixes, lower symbols, and nonstationary pieces are
    retained and target-safe.
2.  Squarefreeness of both variables, coprimality, parity,
    (chi_4), the strict cone, fixed (N), and the individual
    positive direction remain literal in (148.C4).
3.  The correct reduced coordinate is (148.C16), with exact divisors,
    common divisors, imprimitive lifts, and the zero family retained.
4.  Arbitrary (q)-coefficients are rejected; the absolute
    squarefree (Q+D) analogue remains open.
5.  The factor-(R) loss is confined to progression separation before
    the positive diagonal.  The stronger Round-147 absolute-(H) losses
    remain (R^{1/3}) at (M=R^{4/3}) and (R^{1/4}) at
    (M=R^2).
6.  The audited source hypotheses do not match the hard reduced-modulus
    range, varying denominator, coupled coefficient, or diagonal.
7.  The (D=1), prime, even-squarefree, exact-radical, slow-frequency,
    top, transition, lower-scale, and terminal-prefix controls create no
    target proof or signed counterexample.
8.  The Round-138 cross owner, every (t\geq2) layer, lower GAR,
    M9--M1, M9--M2, endpoint uniformity, M9, the bridge, the quarter
    target, and the global exponent remain outside this result.

The first unproved step is a coefficient-sensitive joint signed
estimate for (148.C4) which neutralizes the cross-progression diagonal
before it is separately majorized, or an exact Euler recombination and
signed theorem for the Round-147 (H)-correlation.  No allowed source
or report contains that theorem.

The exact evidence is:

- `reports/signed_squarefree_reciprocal_attack.md`;
- `reports/blind_squarefree_reciprocal_feasibility.md`;
- `reports/squarefree_progression_source_audit.md`;
- the Round-147 candidate, reports, adjudication, controls, and
  synthesis named in `state/active_campaign.yml`.

## 7. Recommended state effect

Subject to independent seam review, promote two scoped nodes:

1.  an exact (t=1) squarefree reciprocal-transform reduction,
    consisting of (148.C3)--(148.C17), including the boundary and symbol
    ledger; and
2.  a reciprocal-dispersion obstruction consisting of
    (148.C18)--(148.C26), expressly limited to progression-separated
    positive-diagonal methods and the audited source families.

Retain the signed target, every strict range, M9--M1, M9--M2, endpoint
uniformity, M9, the quarter target, and the global exponent as open.
The next attack should preserve the signed cross-progression energy or
recombine the Euler factors before forming any positive diagonal.

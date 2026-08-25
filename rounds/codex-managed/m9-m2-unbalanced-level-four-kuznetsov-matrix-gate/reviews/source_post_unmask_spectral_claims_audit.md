# Source post-unmask spectral-claims audit (Round 143)

## 1. Result

**The common no-go conclusion survives, but the two reports have different
source status.**  The arithmetic identity

\[
 S^{\chi _4}_{\infty,0}(4N_0,h;2n)
 =\chi _4(n)S(N_0,h;n),\qquad n\ {\rm odd},                 \tag{A.1}
\]

is a valid internal double-coset lemma in the scaling convention used by the
reports.  It is not, by itself, a sourced weight-one switched-cusp
Kuznetsov formula.  Kıral--Young's superficially matching formula (2.20)
belongs to their even-character, weight-zero framework and cannot certify
the odd character \(\chi _4\).  Blomer--Milićević supply a legal
odd-character, \(\kappa=1\) spectral route, but their exact arithmetic
encoding is a standard-cusp level-\(4\) minus level-\(8\) combination and
their theorem has fixed Fourier arguments and one common smooth test.

Accordingly:

1. `level_four_kloosterman_embedding_attack.md` is **revise-and-promote in
   scoped form**.  Its internal arithmetic identity, joint-matrix
   obstruction, zero-frequency treatment, same-sign Linnik-range audit, and
   capacity comparison pass.  Its spectral discussion must more sharply
   separate the conditional pure-level-\(4\) switched-cusp architecture from
   the source-certified level-\(4/8\) standard-cusp architecture.
2. `blind_joint_matrix_spectral_feasibility.md` is **not promotable as an
   exact spectral formula**.  Equations (3.12)--(3.16), including the factors
   \(4\), \(2\pi\), \(-8i\), the denominators
   \(\cosh\pi(t-i/2)\), and the terms \(\mathcal R^\pm\), have no cited or
   derived primary-source normalization.  Its arithmetic and coefficient-
   matrix no-go remains useful after those formulas and their consequences
   are deleted or explicitly downgraded to unsourced placeholders.

Neither report proves the quarter bound.  On the source-certified route the
first exact project failure is still the literal joint
\((n,h)\)-coefficient/common-test seam, followed independently by the
printed Linnik-range restriction.  The recommended campaign label remains
`level_four_spectral_matrix_no_go`.

## 2. Exact source statements and hypotheses

### 2.1 Kıral--Young: matching arithmetic shape, wrong parity

Kıral--Young, [*Kloosterman sums and Fourier coefficients of Eisenstein
series*, arXiv:1710.00914](https://arxiv.org/html/1710.00914), Definition
2.2 and (2.3), define their generalized-cusp sums in the weight-zero
multiplier setting.  Proposition 2.6 and (2.13)--(2.14) give, without a
character,

\[
 \mathcal C_{\infty,1/r}
 =\{c\sqrt s:c\equiv0\pmod r,(c,s)=1\},\qquad
 S_{\infty,1/r}(m,n;c\sqrt s)=S(\bar s m,n;c).              \tag{A.2}
\]

Theorem 2.7, (2.15)--(2.17), explicitly assumes that \(\chi\) is even.
Its special case (2.20), printed p.7, is

\[
 S_{\infty,0}(m,n;c\sqrt N;\chi)
 =\overline{\chi}(c)S(\overline N m,n;c),\qquad (c,N)=1.    \tag{A.3}
\]

At \(N=4\), (A.3) has the same arithmetic shape as (A.1), but
\(\chi _4(-1)=-1\), so Theorem 2.7 does not apply.  The scaling rule (2.7)
changes a generalized sum only by one modulus-independent phase; it cannot
repair this parity failure.  The paper also does not state a weight-one
switched-cusp Kuznetsov formula or its Bessel constants.

### 2.2 Blomer--Milićević: the legal odd-character route

Blomer--Milićević, [*Kloosterman sums in residue classes*, JEMS 17
(2015), 51--69](https://ems.press/content/serial-article-files/32008?nt=1),
equation (2.3), p.55, encode a modulus character into twisted standard-cusp
Kloosterman sums.  For \(q=q_1=4\), \(\chi=\chi _4\),
\(u=(N_0,4^\infty)=2^{v_2(N_0)}\), and \(M_0=N_0/u\), their identity is

\[
 \sum_{n\ {\rm odd}}\chi _4(n)S(N_0,h;n)\omega(n)
 =\frac{\chi _4(M_0)}{\tau(\chi _4)}
 \left(\sum_{4\mid C}-\sum_{8\mid C}\right)
 S_{\chi _4}(M_0,16uh;C)\omega(C/4).                       \tag{A.4}
\]

Thus the source-certified implementation uses standard-cusp levels \(4\)
and \(8\), with the fixed Gauss factor and Möbius sign in (A.4).  It is not
the pure-level-\(4\), \((\infty,0)\) formula (A.1), even though the two
arithmetic representations encode the same modulus sign.

Section 3, p.57, sets \(\kappa=0\) for even \(\chi _1\) and
\(\kappa=1\) for odd \(\chi _1\); hence \(\chi _4\) is spectrally legal in
weight one.  Equations (4.1)--(4.6), pp.61--62, use one common smooth scalar
test and, for \(\kappa=1\), the same-sign transforms

\[
 \dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
 \qquad k=3,5,\ldots,                                      \tag{A.5}
\]

\[
 \widetilde g(t)=\frac{it}{2\sinh(\pi t)}
 \int_0^\infty\{J_{2it}(x)+J_{-2it}(x)\}g(x)\frac{dx}{x}. \tag{A.6}
\]

In that normalization the Maaß and Eisenstein summands have the printed
\(1/\cosh(\pi t)\) spectral factor.  Formula (4.6) and Theorem 4,
pp.67--68, display exactly \(H+M+E\): odd holomorphic weights
\(k=3,5,\ldots\), the full weight-one Maaß basis including real, \(t=0\)
if it occurs, and exceptional parameters, and continuous Eisenstein
integrals over every singular cusp.  No separate \(\mathcal R^\pm\) term
or holomorphic weight-one limit term is printed.

The singular-cusp criterion (5.1), p.64, is
\(4\mid[w,Q/w]\).  At \(Q=4\), the singular cusps are \(\infty,0\), while
\(1/2\) is nonsingular.  At \(Q=8\), all four cusps
\(\infty,0,1/2,1/4\) are singular.  Section 3's bases include newforms and
oldclass shifts.  The primitive conductor-four space has no proper-level
oldspace at level \(4\); the level-\(8\) part of (A.4), however, contains
level-\(8\) newforms and oldforms lifted from level \(4\).

Theorem 1, pp.52--53, and the fixed-character form (2.5) concern fixed
positive arguments and one fixed smooth modulus test.  Their uniform bound
is printed only in the Linnik range

\[
 mn\le C_0^2,                                               \tag{A.7}
\]

with the harmless fixed factor \(q_1^{1/2}\) at \(q_1=4\).  The paper says
that the complementary range would need a different transform analysis; it
does not print a theorem for that range.  It only remarks that opposite
signs may be treated and does not print the convention-matched weight-one
\(K\)-transform needed by the reports.

### 2.3 Opposite sign and common-sequence comparison

Deshouillers--Iwaniec, [*Kloosterman Sums and Fourier Coefficients of Cusp
Forms*, Invent. Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728),
Theorem 1 and (1.23), p.228, print a weight-zero opposite-sign transform
proportional to

\[
 \frac{4}{\pi\cosh(\pi t)}
 \int_0^\infty K_{2it}(x)\phi(x)\frac{dx}{x}.              \tag{A.8}
\]

That formula is not an odd-nebentypus weight-one switched-cusp source and
cannot certify the blind report's (3.14).  Their Theorems 2 and 5,
pp.230,232, also confirm the relevant large-sieve interface: all spectral
pieces use the same coefficient sequence.  They do not accept an arbitrary
joint modulus/frequency matrix.

## 3. Audit of `level_four_kloosterman_embedding_attack.md`

### 3.1 Claims that pass

The following claims are correctly scoped and source-compatible.

1. The double-coset computation (3.1)--(3.5) proves (A.1) internally, with
   positive generalized moduli \(2n\equiv2\pmod4\), ordinary arguments
   \((N_0,h)\), and no modulus-dependent root in the chosen arithmetic
   convention.  This does not require \((N_0,n)=1\).
2. Lines 214--224 correctly state that Kıral--Young (2.20) has an even-
   character hypothesis and that Blomer--Milićević validate odd parity only
   with fixed indices and a common same-sign test.
3. The transforms (3.16)--(3.17) agree exactly with (A.5)--(A.6).  The
   report restricts them to a legal smooth test and \(h>0\).
4. The Linnik audit is source-safe: it uses only fixed positive, same-sign
   arguments and obtains

   \[
    |h|\ll \frac{(R/g)^2}{N_0}
       \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2},
    \qquad \frac{H_{\rm Lin}}{R/g}\asymp\frac1{Dg}.         \tag{A.9}
   \]

   It also uses the correct constant-safe threshold
   \(g\gg\sqrt{K/L}\), rather than a sharp unsupported inequality.
5. It does not print an exact opposite-sign transform or invent a residual
   term.  Its statement that the \(h=0\) class is outside nonzero-index
   Kuznetsov and must be handled as a Ramanujan term is correct.
6. The matrix/common-test obstruction is independent of transform
   normalization and remains valid.  The report does not infer an actual
   lower bound for the literal matrix from its generic nuclear-norm upper
   price.

### 3.2 Mandatory source repairs

The report's spectral inventory at lines 466--486 and its control verdict at
lines 652--658 mix two architectures too closely.  The statements “the
continuous spectrum is attached to \(\infty,0\)” and “the oldspace ... is
empty” are correct only for the conditional **pure-level-\(4\)**
switched-cusp setting.  They are not the full ledger of the source-certified
Blomer--Milićević implementation.  The report must add, adjacent to that
inventory:

> Blomer--Milićević's legal odd-character encoding is (A.4), a level-4
> minus level-8 standard-cusp combination.  Its level-8 component has four
> singular cusps and includes oldforms lifted from level 4; hence the
> two-cusp/empty-oldspace ledger applies only to the internally proposed
> pure-level-4 switched-cusp formula, not to the complete cited route.

Likewise, “source-safe structural spectral inventory” should be changed to
“conditional structural inventory.”  The audited sources do not themselves
state the convention-matched odd-character pure-level-\(4\)
\((\infty,0)\) trace formula.  The internal arithmetic lemma (A.1) does not
derive its Fourier normalizations, Plancherel measure, or all endpoint
terms.

Finally, the negative-\(h\) sentence should not assert as a source-certified
formula that the “full Maaß, exceptional, and Eisenstein spectra remain.”
It may be retained only as a conditional structural expectation, followed
by the report's existing disclaimer that no exact opposite-sign
normalization is supplied.  Alternatively, use representatives
\(1\le h<n\) and keep the source discussion entirely same-sign.  After
these repairs, no other external attribution in this report requires
change.

## 4. Audit of `blind_joint_matrix_spectral_feasibility.md`

### 4.1 Arithmetic and matrix claims that survive

The internal calculations (3.5)--(3.8) establish (A.1), including the
character sign and absence of a modulus-dependent arithmetic phase.  The
parity argument from \(-I\) correctly forces \(\kappa=1\).  The stabilizer
calculation correctly gives singular cusps \(\infty,0\) and nonsingular
cusp \(1/2\) at pure level \(4\).  The zero-frequency Ramanujan estimate,
row Parseval bounds, Hilbert--Schmidt/nuclear upper prices, interpolation
warning, exact Fourier self-return, and positive capacity do not depend on
the disputed spectral constants and survive.

### 4.2 Exact formulas (3.12)--(3.16) fail source audit

The report says that (3.12)--(3.16) “fix the spectral normalization” while
also declaring that it used no external source.  No derivation is supplied
from the stated Whittaker expansion (3.11).  The claims are therefore not
promotion-level formulas.  In particular:

1. Its same-sign transforms contain \(4i^k\) and
   \(2\pi it/\sinh(\pi t)\), whereas the source-certified
   Blomer--Milićević transforms are (A.5)--(A.6).  Overall constants can
   move between a geometric normalization, Fourier coefficients, and
   transforms, but the report gives no calculation reconciling its factors
   with a primary formula.
2. Its spectral denominators
   \(\cosh\pi(t-i/2)=-i\sinh(\pi t)\) are not the
   \(\cosh(\pi t)\) factors printed in the audited weight-one source.  The
   report provides no alternative source or Plancherel derivation for this
   shift.  The artificial singularity at \(t=0\) is then used to motivate
   extra residual language, compounding the unsupported normalization.
3. The opposite-sign transform

   \[
    \check\phi(t)=-8i\cosh(\pi t)
       \int_0^\infty K_{2it}(x)\phi(x)\frac{dx}{x}          \tag{A.10}
   \]

   has no supporting source in the audited corpus.  Blomer--Milićević do
   not print the needed odd-weight formula; the weight-zero formula (A.8)
   cannot be transplanted to justify (A.10).
4. The ad hoc \(\mathcal R^+\) and \(\mathcal R^-\) in (3.15)--(3.16)
   are unsupported.  Blomer--Milićević's exact formula prints \(H+M+E\),
   not \(H+M+E+\mathcal R\).  A custom cross-cusp scattering calculation
   might require special treatment, but none is supplied, so the report may
   neither assert those terms present nor assert them absent.
5. The claimed “possible \(t=0\) limit-of-discrete-series term (including
   any holomorphic weight-one limit term)” must be removed.  In the
   source-certified ledger, a \(t=0\) Maaß cusp form, if present, is already
   in \(M\); the holomorphic tower has \(k>\kappa=1\), hence starts at
   \(k=3\).  There is no separately printed holomorphic weight-one term.

The safe repair is to delete (3.12)--(3.16) and replace them by the sourced
same-sign standard-cusp formulas (A.5)--(A.6) and the conditional statement
that a convention-matched pure-level-\(4\) cross-cusp formula has not been
established in this report.  If exact pure-level-\(4\) or opposite-sign
formulas are desired, they require a primary theorem in the same scaling and
Fourier convention or a complete derivation including Plancherel constants
and scattering terms.

### 4.3 Level, oldclasses, singular cusps, and Linnik scope

The blind report's two-cusp statement is correct for pure level \(4\), but
it cannot be presented as the ledger of the only source-certified odd-
character implementation.  If it invokes Blomer--Milićević, it must replace
the single level-\(4\) basis by the level-\(4/8\) combination (A.4), retain
the level-\(8\) oldforms from level \(4\), and integrate the level-\(8\)
continuous term over all four singular cusps.  The absence of proper-level
oldforms is true only for primitive-character level \(4\).

The blind report does not explicitly invoke a Linnik theorem, so its matrix
obstruction does not fail for that reason.  Any repaired appeal to
Blomer--Milićević's bound must state all of (A.7): fixed positive arguments,
same sign, one common smooth modulus test, and \(mn\le C_0^2\).  It cannot
be applied to all signed representatives or to the literal joint tests.

## 5. First unproved step and project capacity

There are two routes, and their first gaps must not be conflated.

For the pure-level-\(4\) route, (A.1) is only an internal arithmetic
double-coset identity.  The first source gap is the convention-matched
weight-one switched-cusp trace formula itself: Fourier coefficients at both
cusps, same- and opposite-sign transforms, spectral measure, exceptional
parameters, continuous terms, and any scattering residues must all be
derived in one normalization.  Kıral--Young does not fill that gap because
of even parity.

For the legal Blomer--Milićević route, (A.4) and the weight-one spectral
architecture remove the parity/source gap.  The first project failure is
then the scalar/common-test interface.  For each fixed \(g,h\), the literal
coefficient would require nodal values of the form

\[
 \Phi_{g,h}\!\left(\frac{4\pi\sqrt{N_0|h|}}{n}\right)
 =2nW\!\left(\frac{X}{gnD}\right)
   \widehat\gamma_{g,n}(h),                                 \tag{A.11}
\]

where \(\widehat\gamma_{g,n}(h)\) contains the inverse map modulo the very
same modulus \(n\).  Row Parseval controls only

\[
 \sum_h|\widehat\gamma_{g,n}(h)|^2\ll\frac1{RK},\qquad
 \|\widehat\gamma_g\|_{S_2}^2\ll\frac1{gK};               \tag{A.12}
\]

it gives no common smooth test, derivative control, common coefficient
sequence, or saving projective norm.  Exact interpolation has uncontrolled
Bessel bandwidth, while summing all \(h\) first returns the original
reciprocal row.

Even after replacing (A.11) by a legal common test, the printed Linnik range
covers only (A.9), a fraction \(\asymp1/(Dg)\) of the complete frequency
range.  A coefficient-blind row norm gives only

\[
 R\sqrt\Delta=\frac{X}{\sqrt{DL}}
 =X^{1-(\delta+\ell)/2},                                   \tag{A.13}
\]

which exceeds both accepted-envelope branches throughout the strict
polytope and is far above \(X^{1/4+\varepsilon}\).  These failures occur
before any disputed transform constant could create a saving.  They support
the scoped no-go, not an impossibility theorem for a future vector-valued
trace formula.

## 6. Control outcomes and dependencies

1. **Internal double-coset identity -- pass.**  The two reports agree on
   moduli \(2n\), character \(\chi _4(n)\), arguments \((N_0,h)\), and
   arithmetic root \(1\).  It remains an internal lemma, not a citation to
   Kıral--Young.
2. **Even/odd character seam -- pass after attribution boundary.**
   Kıral--Young Theorem 2.7 is unusable for \(\chi _4\); Blomer--Milićević
   Section 3 makes \(\kappa=1\) legal.
3. **Pure level 4 versus legal level 4/8 -- repair required in both
   reports.**  Two singular cusps and empty proper-level oldspace describe
   only pure level \(4\).  The source route also has level \(8\), four
   singular cusps, and level-4 oldclasses.
4. **Same-sign transforms -- pass only in the embedding report.**  Its
   (3.16)--(3.17) match (A.5)--(A.6).  The blind report's constants and
   shifted denominators are unsupported.
5. **Opposite-sign transform -- fail for exact promotion in both reports.**
   The embedding report correctly withholds a normalization but must keep
   its inventory conditional.  The blind report's (3.14), (3.16) fail.
6. **Residual and \(t=0\) ledger -- embedding report pass; blind report
   fail.**  The exact sourced ledger is \(H+M+E\).  A \(t=0\) Maaß form is
   already in \(M\), and no separate \(k=1\) holomorphic term is printed.
7. **Linnik scope -- embedding report pass; blind report must inherit the
   same restrictions if it adds the theorem.**  No source supports the
   long-frequency complement or the literal joint tests.
8. **Common-sequence/matrix interface -- obstruction confirmed.**  The
   no-go survives independently of all disputed spectral normalizations.
9. **Full capacity -- obstruction confirmed.**  Equation (A.13) is the
   owner-complete positive closure currently available.

Exact artifacts audited, without editing them, were:

- `reports/level_four_kloosterman_embedding_attack.md`;
- `reports/blind_joint_matrix_spectral_feasibility.md`;
- `reports/kuznetsov_source_hypothesis_audit.md`;
- `reviews/blind_post_unmask_discovery_seam_audit.md`;
- the Round-143 protocol, proof-obligation, campaign, strategy, and named
  source-map context files already recorded in the source-hypothesis audit.

The primary-source locations used are Kıral--Young Definition 2.2,
Proposition 2.6, Theorem 2.7, and (2.20); Blomer--Milićević Theorem 1,
(2.3)--(2.5), Section 3, (4.1)--(4.11), (5.1), and Theorem 4; and
Deshouillers--Iwaniec Theorems 1, 2, 5 and (1.23).  No numerical experiment
was used.

## 7. Mandatory repairs and promotion verdict

### 7.1 `level_four_kloosterman_embedding_attack.md`

Mandatory repairs before promotion:

1. Insert the exact distinction (A.4) between the internal pure-level-\(4\)
   cross-cusp identity and Blomer--Milićević's level-\(4/8\) standard-cusp
   implementation, including its fixed Gauss/Möbius factors.
2. State that the two-cusp and empty-oldspace ledger is conditional on pure
   level \(4\); add the four level-\(8\) singular cusps and the level-4
   oldclasses required by the complete sourced implementation.
3. Relabel the pure-level-\(4\) switched-cusp spectral inventory as
   conditional, not source-certified by Kıral--Young or
   Blomer--Milićević.
4. Keep the opposite-sign normalization unpromoted and downgrade its
   full-spectrum sentence to a conditional expectation unless a matching
   primary formula is supplied.

After these repairs, **promote only** (A.1) as an internal arithmetic lemma,
the exact coefficient/matrix identities, the target-safe \(h=0\) bound, the
same-sign Linnik obstruction, the self-return, and the positive capacity
(A.13).  Do not promote an exact odd-character pure-level-\(4\)
switched-cusp trace formula.

### 7.2 `blind_joint_matrix_spectral_feasibility.md`

Mandatory repairs before any scoped promotion:

1. Delete or mark as unproved the exact transform and spectral formulas
   (3.12)--(3.16), including all claimed constants and
   \(\cosh\pi(t-i/2)\) denominators.
2. Delete \(\mathcal R^\pm\), the assertion that residual terms are present
   in both signs, and the alleged separate \(t=0\)/holomorphic-weight-one
   limit term.  Replace them by the sourced \(H+M+E\) ledger only on the
   legal same-sign route; leave custom scattering terms undecided.
3. Do not print an exact weight-one opposite-sign \(K\)-transform without a
   convention-matched primary source or derivation.
4. Add the pure-level-\(4\) versus level-\(4/8\) distinction, including
   level-\(8\) oldclasses and all four singular cusps, if the legal source
   route is invoked.
5. State the fixed-positive-argument, common-test, same-sign, Linnik-range
   hypotheses before using any Blomer--Milićević estimate.

The **promotion verdict is `revise` for the first report and `reject the
exact spectral portion, retain after excision` for the blind report**.  The
shared promotable conclusion is only the scoped
`level_four_spectral_matrix_no_go`: the literal nonzero-frequency joint
matrix is not an input to the audited scalar trace formulas or spectral
large sieves, and the available positive capacity misses the target.  Keep
the quarter-bound obligation open; make no shared-state or downstream-owner
change from either sibling report.

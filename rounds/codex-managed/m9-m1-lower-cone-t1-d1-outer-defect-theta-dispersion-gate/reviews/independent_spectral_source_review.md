# Round 155 independent terminal spectral-source review

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate
- Claimant: theta_bilinear_spectral_source_audit.md
- Literal object: (155.CS3), equivalently (155.SA4)
- Primary-source cutoff checked: 25 August 2026
- Terminal verdict: **GREEN**, with two nonfatal source-card clarifications below

## 1. Result and exact scope

The report's source-dependent conclusion is correct.  DFI Lemma 6.1 is an
exact pointwise match for

\[
 K(-v^2,-j;Q),\qquad Q=4N/d\equiv0\pmod4,
\]

including \(v=0\), composite \(Q\), and all imprimitive gcd strata.  DFI
Theorem 2.5 and the Sun/Proskurin formulas have modulus-sum geometric
sides and strictly nonzero shifted-frequency hypotheses.  They do not
bound the literal single-\(Q\), coupled matrix
\(\widehat B_j(2dv)\).  Lam Theorem 2.3, Blomer--Pascadi, and
Shparlinski--Xiao also fail at their exact printed interfaces for the
reasons stated in the report.

The normalization and restored powers reproduce:

\[
 |\mathcal Q_U(V)|\ll_\varepsilon
 (M^{-3/4}V+M^{-1/4})X^\varepsilon
\]

termwise, while the sharper separately priced zero row is

\[
 Z_0(V)\ll
 \left(\frac{V}{\sqrt N\,M^{1/4}}+M^{-1/4}\right)X^\varepsilon.
\]

No cited theorem proves the full target or a positive-power range.  The
proper result is a dated direct-interface no-match, not a lower bound or
an impossibility theorem.

Two exact qualifications should accompany the report:

1. DFI's weakened decay option after Theorem 2.5 retains (2.8),
   \(g(0)=g'(0)=0\), together with (2.28)--(2.29).
2. Sun's same-sign Proskurin formula, Theorem 3.3, is stated directly for
   \(k=1/2\) or \(3/2\); the negative-weight case is handled elsewhere in
   Sun by conjugation and the raising/lowering comparison.

Neither qualification changes the no-match or any power in the report.

## 2. DFI multiplier, theorem hypotheses, and erratum

The primary source is W. Duke, J. B. Friedlander, and H. Iwaniec,
[*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
IMRN 2012, no. 11, 2493--2549,
[doi:10.1093/imrn/rnr112](https://doi.org/10.1093/imrn/rnr112).
Section 6 starts with the theta multiplier

\[
 \vartheta(\gamma)=\overline{\epsilon_d}\left(\frac cd\right)
\]

and, because the general Kloosterman definition uses
\(\overline\vartheta\), obtains in (6.3)

\[
 K(m,n;c)=\sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(m\bar a+na),
 \qquad c\equiv0\pmod4.
\]

Thus (155.SA6) has the correct epsilon factor, argument order, and signs.
Lemma 6.1, (6.8), states

\[
 |K(m,n;c)|\le(m,n,c)^{1/2}c^{1/2}\tau(c),
 \qquad c\equiv0\pmod4,
\]

with no nonzero-argument or primitivity restriction.  It applies exactly
to every \(K(-v^2,-j;Q)\), including \(v=0\), and retains the full odd
imprimitive and two-adic parts.

DFI Theorem 2.5 is different.  It assumes \(m,n\ge1\), a singular cusp at
infinity, and a smooth test function satisfying

\[
 g(0)=g'(0)=0,\qquad g,g',g''\ll(1+x)^{-2-\varepsilon}.
\]

For the theta specialization on \(\Gamma_0(q_0)\), \(4\mid q_0\), it gives

\[
 \gamma_k K_g=L_{\widehat g}+M_{\widehat g}+N_{\check g},\qquad
 K_g=\sum_{c\equiv0\ (q_0)}
 \frac{K(m,n;c)}c
 g\!\left(\frac{4\pi\sqrt{mn}}c\right).
\]

After (2.27), DFI says that (2.9) may be weakened to absolute convergence
provided (2.8) remains and (2.28)--(2.29) hold.  The claimant's
parenthetical “or” must be read in that precise sense.  Its description of
the discrete/residual, continuous, and holomorphic terms is otherwise
correct.

The official
[*Erratum*](https://www.math.ucla.edu/~wdduke/preprints/weylcorr.pdf),
IMRN 2012, no. 11, 2646--2648,
[doi:10.1093/imrn/rnr240](https://doi.org/10.1093/imrn/rnr240),
changes the square condition in Theorem 7.1 and the ensuing argument
around Lemma 9.1.  It does not alter Theorem 2.5, (6.3), or Lemma 6.1.
The report's erratum scope is exact.

## 3. Sun/Proskurin signs, zero frequency, and modulus averaging

The primary versions checked are Q. Sun,
[*Uniform bounds for Kloosterman sums of half-integral weight, same-sign
case*](https://arxiv.org/abs/2309.05233), arXiv:2309.05233v2,
13 April 2025, and
[*Uniform bounds for Kloosterman sums of half-integral weight with
applications*](https://arxiv.org/abs/2305.19651),
arXiv:2305.19651v2, 6 February 2024.

In the same-sign paper, Definition 1.1 requires level lifting and an
average Weil bound only for intervals \(x-y\gg x^{2/3}\); Lemma 1.2
includes the theta multiplier, its quadratic twists, and conjugates.
Theorem 3.3 (Proskurin) is stated for \(k=1/2\) or \(3/2\) and
\(\widetilde m,\widetilde n>0\):

\[
 \sum_{c>0}\frac{S(m,n,c,\nu)}c
 \phi\!\left(\frac{4\pi\sqrt{\widetilde m\widetilde n}}c\right)
 =\mathcal U_k+\mathcal W+
 \sum_{\mathfrak a\ {\rm singular}}\mathcal E_{\mathfrak a}.
\]

These are respectively the holomorphic, Maaß, and Eisenstein pieces.
The claimant's formula is correct subject to the direct weight
qualification above.

Same-sign Theorem 1.3 assumes positive shifted frequencies, with the
negative-negative case obtained by conjugation.  Its exceptional sum and
the \(A_u(m,n)+X^{1/6}\) error in (155.SA10)--(155.SA11) are transcribed
correctly.  The source notes both that
\(A_u(m,n)\ll(\widetilde m\widetilde n)^{1/4}\) in general and that the
\(r=i/4\) coefficient vanishes in one weight/sign configuration.  The
report is therefore right to retain the full exceptional ledger and call
the theta term only “possible”.

For mixed signs, Sun Theorem 6.4 assumes
\(\widetilde m>0,\widetilde n<0\) and \(k=\pm1/2\); its geometric side is
a modulus sum and its spectral side is the full Maaß plus Eisenstein
expression.  Theorem 1.2 has the stated
\(|\widetilde m\widetilde n|^{143/588}+X^{1/6}\) error under its
squarefree-or-coprime lifted-frequency condition.  Theorem 1.4 removes
that condition only by restoring \(A_u(m,n)\), including its
nonnegligible middle terms.  The report quotes these points correctly.

For \(K(-v^2,-j;Q)\), \(v\ne0,j>0\) is negative-negative and enters the
same-sign theory after conjugation; \(v\ne0,j<0\) is mixed sign.  The
row \(v=0\) has first shifted frequency zero for the standard theta cusp
and is outside DFI Theorem 2.5 and both displayed Sun/Proskurin formulas.
DFI Lemma 6.1 still applies pointwise.

All these trace formulas sum the modulus.  A narrow test can formally
localize the identity, but the quoted uniform estimates require a broad
window; delta localization enlarges transform norms and retains every
spectral piece.  Taking a growing group level \(Q\) instead leaves
source constants depending on that level.  Neither device supplies a
uniform theorem for the one fixed \(Q=4N/d\).

## 4. Lam, Blomer--Pascadi, and Shparlinski--Xiao

J. W. C. Lam,
[*A local large sieve inequality for cusp forms*](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.887.pdf),
J. Théorie des Nombres de Bordeaux 26 (2014), Theorem 2.3, assumes
\(4\mid M_0\), one sequence \((a_n)_{N_1\le n\le2N_1}\), holomorphic
half-integral weights

\[
 K_0\le k\le K_0+G,\qquad k-\tfrac12\ {\rm even},\qquad
 1\le G\le K_0^{1-\varepsilon},
\]

and proves exactly

\[
 \sum_k\sum_{f\in B_{k,M_0}}
 \left|\sum_n a_n\rho_f(n)\right|^2
 \ll (M_0K_0N_1)^\varepsilon
 (M_0K_0G+N_1)\sum_n|a_n|^2.
\]

Lam's Maaß Theorem 2.5 is integral weight.  The claimant is correct that
Theorem 2.3 is not a fixed-weight half-integral Maaß-plus-Eisenstein
large sieve for an arbitrary two-dimensional coefficient matrix.

V. Blomer and A. Pascadi,
[*Bilinear forms with Kloosterman sums via quadratic
characters*](https://arxiv.org/abs/2607.24311),
arXiv:2607.24311v1, 27 July 2026, Theorem 1.1, assumes an arbitrary
positive modulus \(c\), \(1\le H\le c\), two intervals of length at most
\(H\), separated sequences, a unit \(a\bmod c\), and \((m,n,c)=1\).
It states

\[
 \sum_{m,n}\alpha_m\beta_nS(am,n;c)
 \ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
 \left(H^{1/8}c^{-3/32}
 +H^{5/16}c^{-3/16}
 +H^{2/3}c^{-7/18}\right).
\]

The gcd restriction disappears only for both initial intervals.  At
\(H=\sqrt c\), the saving is \(c^{-1/32}\).  Theorem 5.5 remains an
ordinary-Kloosterman, separated-coefficient theorem; Theorem 5.7 has
\((m,c)=1\) and the exact factor

\[
 (MN)^{1/2}c^{-3/4}+N^{1/2}c^{-1/2}+M^{1/2}c^{-1/4}.
\]

The dates, formulas, and hypotheses in (155.SA14)--(155.SA16) are exact.
They do not accept the theta multiplier, mandatory zero/imprimitive
strata, or \(A_{j,v}=\widehat B_j(2dv)\).

I. E. Shparlinski and Y. Xiao,
[*Shifted bilinear sums of Salié sums and the distribution of modular
square roots of shifted primes*](https://arxiv.org/abs/2601.10113),
arXiv:2601.10113v1, 15 January 2026, work with a large prime \(q_0\).
Theorem 2.5 assumes separated \(\alpha_m,\beta_n\),
\((a\lambda,q_0)=1\), and proves

\[
 |W_{a,b,\lambda}|
 \ll\|\alpha\|_2\|\beta\|_\infty
 \left(M^{1/2}N^{1/2}+M^{1/2}Nq_0^{-1/4}
 +Nq_0^{1/4}(\log q_0)^{1/2}\right)
\]

for roots of \(x^2\equiv amn+b\pmod{q_0}\).  The report's theorem card is
exact.  Prime modulus, product-plus-shift geometry, and separated weights
prevent specialization to the literal even composite theta family.

## 5. Zero mode and restored-power translation

Put

\[
 q=4N,\qquad Q=q/d,\qquad W=M^{-3/4},\qquad K=\sqrt{NM}.
\]

Apart from \(|1+i|\), one \(d\)-stratum has coefficient

\[
 P_d=\frac{d\sqrt Q}{2Nq}
 =\frac{\sqrt d}{4N^{3/2}}.
\]

DFI contributes \(Q^{1/2}\), and \(dQ=q\) gives exactly

\[
 P_dQ^{1/2}=\frac1{2N}.
\]

There is no residual square-root modulus factor.  For \(v\ne0\), BV
Fourier decay and the gcd expansion yield

\[
 \sum_{v\ne0}
 |\widehat B_j(2dv)|(v^2,j,Q)^{1/2}
 \ll WQX^\varepsilon.
\]

Restoring \(1/(2N)\), every odd \(d\mid N\), both signs, and \(O(V)\)
outer \(j\)'s gives \(WVX^\varepsilon\), or
\(N^{1/2}M^{-1/4}X^\varepsilon\) at \(V=K\).

For \(v=0\),

\[
 |\widehat B_j(0)|\ll KW,\qquad
 \sum_{V<|j|\le2V}(j,Q)^{1/2}
 \ll(V+\sqrt Q)Q^\varepsilon.
\]

Summing all divisor strata gives

\[
 Z_0(V)\ll
 \frac{KW}{N}(V+\sqrt N)X^\varepsilon
 =\left(\frac{V}{\sqrt N\,M^{1/4}}+M^{-1/4}\right)X^\varepsilon.
\]

At \(V=K\), its first term is \(M^{1/4}X^\varepsilon\).  These are upper
capacities, not signed lower bounds.  The report's zero-mode ledger and
all \(N,M,V,d\) translations are exact.

The hypothetical selected-incidence square-root capacity is \(W\sqrt V\),
target-sized exactly for \(V\le M^{3/2}\).  At \(V=K\), this forces
\(M\ge\sqrt N\), only the frozen endpoint.  No source proves that
cancellation, so the report correctly promotes no range.

The half-period calculation (155.SA20) is also normalized correctly:
because \(4\mid Q\), \(e_Q(-\bar a v^2)\) has period \(Q/2\), completing
the square produces one half of \(G(-\bar a,0;Q)\), and its exact
epsilon/Kronecker factor cancels the theta multiplier.  With the outer
\(-i(1+i)/(2Nq)\chi_4(d)d\sqrt Q\), the result is the original
\(-i/(2N)\) quadratic-selector stratum.  Complete \(v\)-resummation is an
inverse-Gauss self-return, not a second gain.

## 6. First unproved step, controls, and cutoff wording

The first source-unproved term is exactly

\[
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d).
\]

If that row is resolved, the next missing theorem is the nonzero,
fixed-\(Q\), coupled \((j,v)\) form.  Replacing fixed \(Q\) by a broad
modulus average, deleting spectral principal/exceptional pieces, changing
the theta kernel to an ordinary one, or replacing
\(\widehat B_j(2dv)\) by separated weights is not source-legal.

| Control | Outcome |
|---|---|
| DFI multiplier and Lemma 6.1 | **PASS.** Exact arguments, all integers, full gcd, composite \(Q\equiv0\pmod4\). |
| DFI Theorem 2.5 and erratum | **PASS with clarification.** \(m,n\ge1\); (2.8) remains with (2.28)--(2.29); erratum is later-scope only. |
| Sun/Proskurin signs and zero mode | **PASS with clarification.** Direct same-sign trace weight is \(1/2\) or \(3/2\); \(v=0\) is excluded. |
| Spectral pieces | **PASS.** Holomorphic/Maaß/Eisenstein and exceptional terms are retained according to sign. |
| Fixed modulus versus average | **PASS / NO-MATCH.** DFI/Sun sum moduli; the quoted bounds do not uniformly delta-localize at growing \(Q\). |
| Lam | **PASS / NO-MATCH.** Holomorphic varying weight and one sequence only. |
| Blomer--Pascadi | **PASS / NO-MATCH.** v1 date, formulas, ordinary kernel, separation, and gcd restrictions verified. |
| Shparlinski--Xiao | **PASS / NO-MATCH.** v1 date, formula, prime modulus, and separated root family verified. |
| Zero mode and powers | **PASS.** \(1/(2N)\), \(WV\), \(Z_0(V)\), and the top powers reproduce exactly. |
| Cutoff wording | **PASS.** The report expressly makes a dated direct-interface check, not an exhaustive-bibliography or impossibility claim. |

The two qualifications are source-card precision corrections only.  They
strengthen the no-match and change no estimate or state recommendation.

## 7. Dependencies and recommended state effect

This review used protocol.md, state/active_campaign.yml, the Round-155
conductor seed, the claimant report, and only the primary texts cited
above, together with the cited primary Fouvry--Iwaniec and Baier pages for
their limited no-match cards.  No claimant report, candidate, graph,
synthesis, validation matrix, or shared state was edited.

Recommended state effect: retain DFI Lemma 6.1 solely as the exact
individual theta-Kloosterman match and retain the accepted termwise bound.
Record the modulus-average, nonzero-frequency, spectral-piece,
growing-level, coefficient, and kernel mismatches; the exact zero row; and
the inverse-Gauss self-return as route-scoped obstructions.  Keep the full
outer-defect target, the zero-row signed estimate, and the nonzero coupled
matrix estimate open.  Promote no \(V\le M^{3/2}\) range and make no
downstream or global-exponent change.

GREEN

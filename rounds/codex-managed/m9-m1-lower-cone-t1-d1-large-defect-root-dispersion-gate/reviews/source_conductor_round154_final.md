# Round 154 terminal primary-source review

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Object reviewed: `conductor_round154_root_dispersion_adjudication.md`
- Review role: independent terminal primary-source and normalization audit
- Source-search cutoff checked: 25 August 2026
- Terminal verdict: **GREEN**, with the dependency and bibliography qualifications recorded below

## 1. Result and exact scope

The source-dependent kernel of the conductor candidate is correct.  In
particular:

1. Duke--Friedlander--Iwaniec (DFI), Section 6 and Lemma 6.1, is an exact
   source match for the theta-multiplier sum in (154.CA22)--(154.CA23).
2. The imprimitive reduction, the modulus (q'=4N/d\equiv0\pmod 4), the
   epsilon/Kronecker multiplier, the even-dual selector, the gcd strata,
   and the Fourier zero mode reproduce (154.CA10), including its
   (M^{-1/4}) second term.
3. Müllner's Theorem 5.3 and Lemma 5.4 are quoted with the correct
   hypotheses and constants.  They support only the auxiliary termwise
   incomplete-Gauss estimate, not a new estimate for (154.CA30).
4. The principal reciprocal self-return in (154.CA25)--(154.CA29) is valid
   only through the already accepted Round-152 ledger (including the
   inherited Round-148 boundary owners and the Round-151 reciprocal row).
   It does **not** follow from, and the candidate does not need, an
   unsupported claim that Vandehey's explicit transform error is small
   enough.
5. No primary theorem checked through the stated cutoff accepts the
   literal nonseparable sum (154.CA30).  This is a direct-interface
   no-match, not a literature-impossibility statement.

The review therefore supports precisely the candidate's route-scoped
promotion and leaves the full strict large-defect estimate open.  It does
not certify any positive-power defect extension or any downstream/global
exponent claim.

## 2. Exact DFI statement and the normalization (154.CA20)--(154.CA23)

The primary source is W. Duke, J. B. Friedlander, and H. Iwaniec,
*Weyl Sums for Quadratic Roots*, **IMRN** 2012, no. 11,
2493--2549, [doi:10.1093/imrn/rnr112](https://doi.org/10.1093/imrn/rnr112).
It was published in the 2012 volume; the DOI record also carries the 2011
online-history date.  DFI (6.1)--(6.3) use

\[
 \epsilon_x=\begin{cases}1,&x\equiv1\pmod4,\\
 i,&x\equiv3\pmod4,
 \end{cases}
 \qquad
 K(m,n;c)=\sum_{x\bmod c}^{*}
 \epsilon_x\left(\frac c x\right)
 e_c(m\bar x+nx),
\]

for (c\equiv0\pmod4).  Here ((c/x)) is DFI's extended
Jacobi/Kronecker symbol with odd lower argument.  Lemma 6.1, equation
(6.8), states for all integers (m,n) and (c\equiv0\pmod4)

\[
 |K(m,n;c)|\le (m,n,c)^{1/2}c^{1/2}\tau(c).
\]

This includes composite (c), imprimitive (m,n), and (m=0); no
primitivity condition suppressed in (154.CA23) is needed.

For the candidate, (q=4N), (h) is odd, and

\[
 d=(h,N)=(h,q),\qquad h=da,\qquad q'=q/d.
\]

Thus (d) is odd, ((a,q')=1), and (q'=4N/d\equiv0\pmod4), exactly the
DFI modulus class.  The standard imprimitive reduction gives zero unless
(d\mid b).  After division by (d), the primitive quadratic Gauss sum
at a modulus divisible by four vanishes unless (b/d) is even.  Writing
(b=2dv) and completing the square gives

\[
 \mathcal G(h,2dv;q)
 =d(1+i)\epsilon_a^{-1}\left(\frac{q'}a\right)
 \sqrt{q'}\,e_{q'}(-\bar a v^2),
\]

which is exactly (154.CA21).  Restoring
\(\chi _4(h)e_q(-hj)\) uses

\[
 \chi _4(h)=\chi _4(d)\chi _4(a),
 \qquad \chi _4(a)\epsilon_a^{-1}=\epsilon_a.
\]

Consequently the normalized (a)-sum is

\[
 (1+i)\chi _4(d)
 \sum_{a\bmod q'}^{*}\epsilon_a
 \left(\frac{q'}a\right)
 e_{q'}(-v^2\bar a-ja)
 =(1+i)\chi _4(d)K(-v^2,-j;q'),
\]

as in (154.CA22).  There is no missing complex conjugate, no interchange
of (m,n), and no sign or factor-of-two error.  The natural variable
(v\bmod q'/2) merely parametrizes the allowed even (b)'s; the displayed
Kloosterman phase is invariant under that parametrization.

The candidate's clarification (154.CA22a) is exactly this normalization:
the primitive multiplier sum (154.CA22) is multiplied by the retained
Gauss prefactor \(d\sqrt{q'}\), finite-Fourier factor \(1/q\), and
quotient-selector factor \(-i/(2N)\).  Thus its full coefficient
\(-i(1+i)\chi_4(d)d\sqrt{q'}/(2Nq)\) is mandatory and agrees with the ledger
below.

DFI also has an official erratum, **IMRN** 2012, no. 11, 2646--2648,
[doi:10.1093/imrn/rnr240](https://doi.org/10.1093/imrn/rnr240).  It concerns
later applications around Theorem 7.1/Lemma 9.1 and does not change (6.3)
or Lemma 6.1.  The source audit should be read together with this erratum;
its omission from the bibliography is nonfatal to the present match.

## 3. Gcd, dual-mode, and zero-mode ledger leading to (154.CA10)

Let

\[
 W=M^{-3/4}X^\varepsilon,
 \qquad \|B_j\|_\infty+\operatorname {Var}(B_j)\ll W,
\]

and recall that the (k)-support has length (O(K)), where
(K=\sqrt{NM}).  Finite Fourier inversion is exactly (154.CA20), with
factor (1/q), and has no completion remainder.  For a fixed odd divisor
stratum (d), DFI contributes a second factor (\sqrt{q'}) after the
Gauss factor (d\sqrt{q'}).  Hence

\[
 \frac1{2N}\frac1q\,d\sqrt{q'}\sqrt{q'}
 =\frac1{2N},
 \qquad dq'=q.
\]

This cancellation is the normalization that must precede every outer
sum; inserting another (q'^{1/2}), or dropping the selector (1/(2N)),
would give a false power.

For (v\ne0), bounded variation gives

\[
 |\widehat B_j(2dv)|
 \ll W\min\!\left(K,\frac{q'}{|2v|_{q'}}\right).
\]

Expanding the gcd in DFI's factor and summing the resulting harmonic
progressions yields, uniformly in (j),

\[
 \sum_{v\ne0}
 |\widehat B_j(2dv)|(v^2,j,q')^{1/2}
 \ll Wq'X^\varepsilon.
\]

After (1/(2N)), summation over the odd (d\mid N), and then over
(V<|j|\le2V), this is

\[
 \ll WVX^\varepsilon;
\]

the divisor sum is absorbed into (X^\varepsilon).  This includes both
defect signs and every imprimitive stratum.

For (v=0), one must not use the nonzero-mode harmonic estimate.
Instead

\[
 |\widehat B_j(0)|\ll KW,
 \qquad
 \sum_{V<|j|\le2V}(j,q')^{1/2}
 \ll (V+\sqrt{q'})q'^\varepsilon.
\]

Therefore the complete zero-mode contribution is

\[
 \ll \frac{KW}{N}\bigl(V+\sqrt N\bigr)X^\varepsilon
 \ll \bigl(WV+WK/\sqrt N\bigr)X^\varepsilon.
\]

The frozen range (M\le R^2\asymp\sqrt N) gives (K/N\le1), while

\[
 WK/\sqrt N=M^{-3/4}\sqrt M=M^{-1/4}.
\]

Combining zero and nonzero modes proves exactly

\[
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\]

Thus (154.CA10) has the correct (N,M,V) powers.  In particular, the
zero mode is not silently discarded, and it is precisely the source of
the second displayed term.

## 4. Müllner, Vandehey, and the accepted self-return dependency

C. Müllner, *The Rudin--Shapiro Sequence and Similar Sequences Are Normal
Along Squares*, **Canadian Journal of Mathematics** 70 (2018), no. 5,
1096--1129, [doi:10.4153/CJM-2017-053-1](https://doi.org/10.4153/CJM-2017-053-1),
states on printed page 30:

- Theorem 5.3: for (a,b\in\mathbb Z), (m\ge1), the complete quadratic
  sum has modulus at most (\sqrt{2m(a,m)}).
- Lemma 5.4: for (a,b,m,N,n_0\in\mathbb Z), (m\ge1), (N\ge0), the
  interval (n_0<n\le n_0+N) is bounded by
  \[
  \left(\frac Nm+1+\frac2\pi\log\frac{2m}{\pi}\right)
  \sqrt{2m(a,m)}.
  \]

The source audit quotes these hypotheses and the logarithm correctly.
Specializing (m=4N), (a=h), followed by BV partial summation, is legal.
This is only the weaker termwise incomplete-Gauss route and is not used to
deduce (154.CA10).

J. Vandehey, *Error term improvements for van der Corput transforms*,
[arXiv:1205.0090v1](https://arxiv.org/abs/1205.0090) (submitted 1 May
2012), Theorem 1.1 assumes a real (C^4) phase with
(f''\asymp T/M^2), the stated (f''' ,f'''') derivative controls, and a
real BV amplitude; it supplies the starred-endpoint transform together
with its explicit error.  The source-audit specialization correctly shows
that this standalone error is not an owner-complete target estimate.

Accordingly, (154.CA25)--(154.CA29) are **not** a fresh consequence of
Vandehey.  Their phase (e(N/a)), stationary point, and principal symbol
are the direct algebraic calculation in the candidate, while the
nonstationary pieces, lower symbols, buffers, transitions, hard top, tails,
and endpoints are supplied by the already accepted Round-152 graph ledger.
That terminal-GREEN Round-152 review in turn records the inherited
Round-148 boundary ledger and the Round-151 reciprocal row.  The correct
state dependency is therefore

\[
 \text{Round-154 principal calculation}
 +\text{accepted Round-152 owner ledger},
\]

not “Vandehey's error is negligible.”  With this explicit dependency, the
candidate's wording “with the already accepted ... ledger” is sound.

## 5. Current-literature no-match boundary and citation checks

The literal object still requiring a theorem is (154.CA30): fixed even
moduli (4N/d), all odd gcd strata, theta multiplier, the square first
argument (-v^2), varying outer argument (-j), both signs and strict
cell endpoints, and a coefficient (\widehat B_j(2dv)) coupled in (j,v).
A theorem for ordinary Kloosterman sums with separated coefficients, for a
prime modulus, or averaged over the modulus is not a literal match.

The cited recent metadata were checked: the Baier preprint is
[arXiv:2605.01635v3](https://arxiv.org/abs/2605.01635), revised 20 July
2026; Kingsbury--Neuschotz is
[arXiv:2509.09885v2](https://arxiv.org/abs/2509.09885), revised 30 June
2026; and the Kerr et al. article appeared online in March 2024 and in
**JIMJ** 24 (2025).  None accepts all of the preceding features.

An independent cutoff search also found relevant papers not listed in the
source-audit bibliography:

1. Blomer--Pascadi,
   *Bilinear forms with Kloosterman sums via quadratic characters*,
   [arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311), 27 July 2026:
   classical Kloosterman sums and separated interval coefficients, not the
   fixed even theta-multiplier/coupled coefficient in (154.CA30).
2. Shparlinski--Xiao,
   *Shifted bilinear sums of Salié sums and applications*,
   [arXiv:2601.10113v1](https://arxiv.org/abs/2601.10113), 15 January
   2026: a large-prime, fixed-polynomial/separated-coefficient interface,
   not arbitrary (4N/d) with all gcd strata and (\widehat B_j(2dv)).
3. Sun,
   *Uniform bounds for Kloosterman sums of half-integral weight with
   applications*, [arXiv:2305.19651v2](https://arxiv.org/abs/2305.19651),
   revised 6 February 2024 and published in 2025: a modulus-sum/uniform
   half-integral-weight interface, not the candidate's fixed-modulus
   signed (j,v) bilinear sum.
4. The August 2026 prime-power product and finite-field small-box results
   returned by the same search concern ordinary Kloosterman products at
   odd prime powers or finite fields; they likewise do not accept the
   even theta multiplier and joint profile here.

These additions repair bibliographic coverage but do not change the
mathematical verdict.  The sentence “current through 25 August 2026” is
valid as a search-cutoff statement; it must not be read as saying the
report's printed bibliography is exhaustive.  After the additional checks,
the candidate's narrower claim remains correct: no audited current theorem
was found that matches every hypothesis of (154.CA30), and that absence is
method evidence only.

## 6. First doubtful step and required controls

The first unproved step is exactly the signed, nonseparable outer-defect
estimate (154.CA30), or the equivalent signed cross-fibre estimate after
(154.CA5).  DFI controls each completed Kloosterman sum but does not sum
the coupled (j,v,d) family with a power saving.  Nothing in Müllner,
Vandehey, or the current no-match sources closes this step.

The terminal controls have the following outcomes:

| Control | Outcome |
|---|---|
| (q'=4N/d\equiv0\pmod4), ((a,q')=1) | **PASS.** Odd (h) forces odd (d), so the full factor (4) remains. |
| Imprimitive and two-adic Gauss reduction | **PASS.** (d\mid b), then (b/d) even; (b=2dv) gives (154.CA21). |
| Epsilon/Kronecker multiplier and signs | **PASS.** \(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\) gives exactly \(K(-v^2,-j;q')\). |
| DFI hypotheses, including (v=0) | **PASS.** Lemma 6.1 allows all integer arguments and composite (c\equiv0\pmod4). |
| Selector/Fourier/Gauss powers | **PASS.** (dq'=q) leaves (1/(2N)); there is no residual square-root modulus factor. |
| Nonzero modes and every gcd stratum | **PASS.** BV plus gcd expansion gives (WVX^\varepsilon). |
| Fourier zero mode | **PASS.** It contributes (WV+M^{-1/4}), not zero. |
| Reciprocal self-return error owner | **PASS with explicit dependency.** Round 152, not Vandehey alone, owns the remainder and endpoint ledger. |
| Current-literature scope | **PASS with bibliography qualification.** Additional 2024--2026 sources are no-matches; no impossibility claim is licensed. |

No source-based correction to (154.CA10), (154.CA20)--(154.CA23), or the
scoped self-return conclusion is required.

## 7. Dependencies, exact artifacts, and recommended state effect

This review used only the assigned project evidence and the primary-source
pages needed to test its source interfaces:

- `protocol.md`;
- `state/active_campaign.yml`;
- `state/proof_obligations.yml` only to verify the accepted Round-152
  dependency;
- `candidates/conductor_round154_root_dispersion_adjudication.md`;
- `reports/quadratic_root_completion_source_audit.md`;
- `reports/large_defect_root_dispersion_attack.md` only for the algebra
  feeding the source match;
- the Round-152 terminal source review and accepted Round-148/151/152 graph
  ledger;
- DFI (6.1)--(6.3), Lemma 6.1, and the official erratum;
- Müllner Theorem 5.3 and Lemma 5.4;
- Vandehey Theorem 1.1 only to delimit what it does **not** own; and
- the current primary papers identified in Section 5.

Recommended state effect: promote the candidate's exact root reduction and
logarithmic collar; record (154.CA20)--(154.CA23), (154.CA10), and the
Round-152-dependent principal self-return as route-scoped obstructions;
retain (154.CA30) and the full strict large-defect estimate as open; make no
positive-power, downstream, endpoint, bridge, quarter-target, or global
exponent change.  Preserve the two qualifications in the accepted reason:
the self-return remainder is inherited from Round 152, and “current” is a
cutoff-checked no-match claim rather than an exhaustive-bibliography or
literature-impossibility claim.

GREEN

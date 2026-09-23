# Round 183 statement-only complete small-t problem

This packet is self-contained.  Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put \(e(z)=e^{2\pi iz}\).  Let \(L\ge2\), \(X>0\),
\(\sigma\in\{+1,-1\}\), and let the fixed coefficient
\(a_{L,X}^{\sigma}(h,n)\in\mathbb C\) be zero outside

\[
 h\asymp L,\qquad n\ \mathrm{odd},\qquad 4h<n<16h.
\]

It is one fixed literal coefficient family, not an arbitrary sequence.  It
contains a dyadic frequency cutoff, a smooth Vaaler taper, a smooth ratio
profile, normalized powers, floors, stars and half weights, strict support
edges, a hard sample, both sign branches, real-parameter crossings, and
endpoint point values.  Define exactly

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ \mathrm{odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\sigma}(h,r/h).
 \tag{B183.1}
\]

Write each positive integer uniquely as \(r=st^2\), with \(s\)
squarefree, and put \(T_L=\lceil\sqrt L\rceil\).  The proposed theorem is

\[
 \boxed{
 \left|
 \sum_{\substack{s>L,\ \mu^2(s)=1\\1\le t<T_L}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})
 \right|
 \ll L^{3/2}\mathcal X,}
 \tag{B183.2}
\]

where \(\mathcal X\) denotes an allowed subpolynomial loss.  Literal
support gives \(st^2\asymp L^2\), and the displayed range includes the
complete \(t=1\) face.  There is one absolute value only after the full
sum.

The complementary sectors \(s\le L\) and
\(s>L,\ t\ge T_L\) have already been paid absolutely at
\(O(L^{3/2}\mathcal X)\).  The task is only (B183.2).

Independently do all of the following:

1. calculate the exact coefficient-insensitive capacity of (B183.2),
   including fixed-\(t\) and \(t=1\) faces;
2. determine whether the target follows from support and boundedness alone,
   using unsigned, complex-dechirped, character-erased, one-site, one-fibre,
   square-centre, and endpoint controls without treating them as literal
   lower mass;
3. expand \(\mu^2(s)\) exactly via \(s=a^2b\), \(u=at\), derive the finite
   divisor kernel with both inequalities retained, and test whether any
   target-scale truncation produces a smaller core or a self-return;
4. derive the exact fixed-row differencing/shifted-correlation statement
   that would imply a three-quarter row estimate, including diagonal,
   shifts, phase difference, coefficient, and restored powers, and state
   whether it is stronger than (B183.2);
5. investigate any genuinely joint-\(t\), divisor-orientation, character,
   or noncentral Mellin relation that keeps the fixed coefficient before
   positivity; and
6. give either a proof of (B183.2), a strict target-safe signed sector with
   its complement, or the narrowest exact mechanism no-go and the first
   additional relation still needed.

A fixed-row or shifted-correlation theorem is a proof mechanism only; it
does not replace (B183.2).  Do not infer a lower bound for the fixed literal
coefficient from an adversarial control.  Computation, if any, is diagnostic
only.

Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

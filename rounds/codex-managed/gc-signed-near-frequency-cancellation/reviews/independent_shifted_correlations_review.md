# Round 210 independent shifted-correlation seam review

## 1. Result and review verdict

GREEN for the precisely scoped finite identities, positive-certificate
obstructions, and sufficient residuals in the two hash-bound artifacts
below. No substantive mathematical repair is required.

Campaign: gc-signed-near-frequency-cancellation. Round: 210.
Role: independent NONBLIND seam reviewer, following completion of the
separate signed_rational_bins assignment. Generated: 2026-09-27T15:40:55Z.
Starting graph SHA-256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Effort: entirely analytical; no mathematical experiment or new source import.

Primary reviewed discovery artifact:
rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/actual_shifted_correlations.md

SHA-256:
657fb00457c9ed8fabf4b3d3ffe71b26fdbeff85e767c35a94ff279aec248168.

Primary reviewed conductor artifact:
rounds/codex-managed/gc-signed-near-frequency-cancellation/controls/conductor_shift_and_bin_ledger.md

SHA-256:
2a7bb78bcbca542e5fbecb4d056412e5e31a92467392564d4f8f396b939cf169.

The verified conclusions are:

- The Fejer moving-sum identity preserves all integer shifts and gives the
  complete \(N/L\) cost.
- The positive separated-diagonal tenth-moment certificate has the stated
  cutoff scale \(L\gtrsim T^{-18/325}N^{3/5}\).
- For actual centered coefficients, a uniform unweighted cumulative-error
  envelope against a continuous main term has a constant atomic floor.
  Absolute Abel variation then has the stated incompatible positive costs.
- The actual CRT expansion contains the asserted singleton family, with
  every support constant, parity condition, and shift multiplicity paid.
  Taking absolute values outside the individual progression estimates
  necessarily retains that family's positive cost.
- The complete signed residuals remain unproved. None of these lower
  bounds is a lower bound for a signed correlation or moment.

The cap needs its precise scope kept visible: the conductor explicitly
grants an optimistic error-only cap, rather than claiming that the
absolute coefficient sum bounds a remainder after subtraction of a
nonzero main term. I use exactly that interpretation below. It is also
consistent with the discovery report's decision to grant the entire
main contribution free for its no-go comparison.

This is not a statement-only review and does not review my own
signed_rational_bins report. The conductor's elementary bin transfer is
checked as a separate finite statement; its actual arithmetic input is
not promoted by this review.

## 2. Exact hypotheses and review boundary

The full required band and moment scale are

\[
 T\ge2,\quad N=T^\alpha,\quad
 \frac{166}{325}<\alpha<\frac{242}{325},\quad
 b=\frac{83}{650},\quad
 \gamma=10b=\frac{83}{65},\quad U=T^\gamma N^{-1/2}.
                                                               \tag{R1}
\]

All asymptotic lower bounds below concern sufficiently large \(T\);
fixed bounded ranges are absorbed in upper-bound constants. The actual
complex finite block is

\[
 F_c(R)=\sum_n c_nf_N(n)e(R\sqrt n),\qquad
 f_N(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),\quad
 I=[T/\sqrt2,\sqrt3T],                                  \tag{R2}
\]

with \(c_n=r_2(n)\) or \(c_n=r_2(n)-\pi\). The mask is real, smooth,
fixed, supported in \([1,4]\), and nonzero. Since \(N/T\to0\)
uniformly over (R1), continuity of \(\Psi\) at zero gives a fixed
positive lower bound for \(\Psi(\sqrt{t/T})\) on the whole block for
large \(T\). A compact sign-definite interval of \(v\) gives a common
interior overlap of length \(\asymp N\) for all
\(1\le h\le\delta N\), after fixing a sufficiently small \(\delta>0\).
Global positivity of \(v\) is unnecessary.

For integer \(1\le L\le N\), the report uses the exact zero-extended
sequence and

\[
 D=\sum_n c_n^2 f_N(n)^2,\quad
 C_h(R)=\sum_n c_nc_{n+h}f_N(n)f_N(n+h)
                           e(R(\sqrt{n+h}-\sqrt n)),
\]
\[
 S_L(R)=2\Re\sum_{1\le h<L}(1-h/L)C_h(R),\qquad
 Q_L=D+S_L.                                            \tag{R3}
\]

The conductor initially restricts \(L\le\delta N\); its sufficient
moment scale lies in that range for large \(T\). The discovery report's
extension of the obstruction to every \(L\le N\) is lawful: one can
always select shifts in a fixed small proportional subrange of
\([1,L]\) that lies below \(\delta N\).

A complex bound for \(F_c\) is sufficient for the associated real
block, not asserted equivalent to its real moment. The centered
alternative also remains separate from the unmodified original shell:
its safe mean wave is restored pointwise after local reproduction.

## 3. Independent derivations and seam checks

### Exact Fejer identity and the complete shift cutoff

Let \(z_n=c_nf_N(n)e(R\sqrt n)\), supported on an ambient integer
interval of length \(K\le3N+2\). For
\(B_m=\sum_{j=1}^Lz_{m+j}\), every original term occurs exactly \(L\)
times in \(\sum_mB_m\), while at most \(K+L-1\) starting indices
can give a nonzero \(B_m\). Therefore

\[
 \sum_mB_m=LF_c,\qquad
 |F_c|^2\le\frac{K+L-1}{L^2}\sum_m|B_m|^2.              \tag{R4}
\]

In the square expansion, a diagonal term occurs \(L\) times; a
correlation at shift \(h\), \(1\le h<L\), occurs \(L-h\) times.
The two orientations are conjugates because \(c_n,f_N(n)\) are real.
Thus exactly

\[
 \frac1L\sum_m|B_m|^2
 =D+2\Re\sum_{1\le h<L}(1-h/L)C_h=Q_L\ge0.             \tag{R5}
\]

Combining (R4)--(R5) gives
\(|F_c|^2\le(K+L-1)Q_L/L\ll(N/L)Q_L\).
The alternative \(j=0,\ldots,L-1\) indexing in the conductor's
ledger is only a translation of \(m\).

This derivation proves there is no missing \(h\ge L\) complement:
the loss \(N/L\) is the complete price of the moving-sum inequality.
It includes nonintegral \(N\), exact support endpoints, all available
short shifts, and \(L=1\).

### Diagonal lower bound and the tenth-moment cutoff

The divisor bound gives \(D\ll_\epsilon N^{-1/2+\epsilon}\).
For centered coefficients,
\[
 |r_2(n)-\pi|\ge4-\pi
\]
at every positive integer, since \(r_2(n)\in4\mathbb Z_{\ge0}\).
On the fixed interior subband \(|f_N(n)|\gg N^{-3/4}\);
there are \(\asymp N\) such integers. Hence \(D\gg N^{-1/2}\).

For the original coefficients, the actual summatory formula gives
\(\sum_{n\ {\rm in\ the\ subband}}r_2(n)\asymp N\).
Cauchy then implies \(\sum r_2(n)^2\gg N\), and the same weighted
lower bound follows. Only a sublinear summatory error is needed;
even the elementary disk-area error \(O(\sqrt N)\) suffices.

Because \(Q_L\ge0\),
\(Q_L\le D+(S_L)_+\), and the fifth power costs at most
\(16(D^5+(S_L)_+^5)\). Consequently

\[
 \int_I|F_c|^{10}\ll_\epsilon
       TN^{5/2+\epsilon}L^{-5}
      +(N/L)^5\int_I(S_L)_+^5.                          \tag{R6}
\]

Here \(D^5\) contributes \(N^{-5/2+\epsilon}\),
the interval length contributes \(T\), and the fifth power of
\(N/L\) contributes \(N^5L^{-5}\). Paying the first term at \(U\)
requires the positive certificate's scale

\[
 L^5\gtrsim T^{1-\gamma}N^3,\qquad
 L\gtrsim T^{-18/325}N^{3/5},                            \tag{R7}
\]

with independently chosen small epsilon losses. The remaining sufficient
input is precisely

\[
 \int_I(S_L)_+^5\ll_\epsilon
            T^{83/65+\epsilon}L^5N^{-11/2}.             \tag{R8}
\]

At the two scale boundaries the exponent of the equality scale in (R7)
is respectively \(408/1625\) and \(636/1625\), both positive.
Its ratio to \(N\) tends to zero uniformly, since
\(-18/325-2\alpha/5<0\). It can therefore be rounded to an integer
and kept below \(\delta N\). It is an available cutoff, not an empty
formal range.

The qualification is essential and correctly present in both sources:
(R7) pays a separated positive diagonal. A direct estimate on \(Q_L^5\)
could exploit negative \(S_L\) and need not satisfy this particular
separated-diagonal criterion.

### Abel transport, its real variation, and the atomic error floor

For a fixed shift let
\[
 d_h(n)=c_nc_{n+h},\quad W_h(t)=f_N(t)f_N(t+h),\quad
 \phi_h(t)=R(\sqrt{t+h}-\sqrt t).
\]
Assume only the proposed unweighted prefix interface
\(\sum_{N\le n\le x}d_h(n)=\mu_h(x-N)+E_h(x)\).
No theorem giving a small \(E_h\) is imported.

An exact derivative calculation is

\[
 \phi_h'(t)=
 -\frac{Rh}{2\sqrt t\sqrt{t+h}(\sqrt t+\sqrt{t+h})},
 \qquad |\phi_h'(t)|\asymp ThN^{-3/2}                  \tag{R9}
\]

on the full overlap for \(1\le h\le N\).
The scaled mask gives
\(\|W_h\|_\infty\ll N^{-3/2}\) and
\(\int|W_h'|\ll N^{-3/2}\).
Its exterior smooth values vanish, including at the boundaries of
the overlap. Stieltjes summation by parts consequently yields the
report's exact formula

\[
 C_h=\mu_h\int W_he(\phi_h)\,dt
            -\int E_h(t)\,d\{W_h(t)e(\phi_h(t))\}.       \tag{R10}
\]

Endpoint convention changes can be included in \(E_h\); no weighted
boundary value survives.

The uniform-error upper certificate has cost

\[
 \mathcal E_h
    \bigl(\|W_he(\phi_h)\|_\infty+
                  \operatorname{Var}(W_he(\phi_h))\bigr)
 \ll \mathcal E_h N^{-3/2}(1+Th/\sqrt N).               \tag{R11}
\]

Its phase-variation part also has the claimed actual lower bound.
Since \(W_h\) is real, its derivative and its phase derivative enter
orthogonal real and imaginary components:

\[
 |(W_he(\phi_h))'|
 =\sqrt{(W_h')^2+4\pi^2W_h^2(\phi_h')^2}.
 \tag{R12}
\]

On the common positive subinterval of length \(\asymp N\),
\(|W_h|\gg N^{-3/2}\). Equations (R9)--(R12) therefore give

\[
 \operatorname{Var}(W_he(\phi_h))\gg ThN^{-2}
              \qquad(1\le h\le\delta N).               \tag{R13}
\]

This lower bound concerns the variation in a supremum-times-variation
certificate. It does not lower-bound the error integral in (R10).

For the continuous mean integral, scaling \(t=Ns\) gives a smooth
amplitude of size \(N^{-1/2}\) and phase parameter \(Th/\sqrt N\).
After dividing by that parameter, all phase derivatives are uniform
for \(0<h/N\le1\), and the first derivative is bounded away from zero
on the compact overlap. Repeated continuous integration by parts gives
\[
 \left|\int W_he(\phi_h)\,dt\right|
 \ll_A N^{-1/2}(1+Th/\sqrt N)^{-A}.
 \tag{R14}
\]
This is not a discrete first-derivative estimate. A polynomially bounded
mean would be harmless, but the failed-certificate test is even more
favorable: it grants the mean's whole contribution zero cost.

For centered coefficients, every atom \(d_h(n)\) has modulus at least
\((4-\pi)^2\). At any interior integer the continuous main term has no
jump, so the two one-sided limits of \(E_h\) differ by that atom.
Their maximum modulus is at least half its modulus:

\[
 \mathcal E_h\ge(4-\pi)^2/2.                             \tag{R15}
\]

The report's supremum over real prefixes is necessary to this argument
and is explicitly specified. All chosen small shifts have many interior
atoms. This floor persists for a shift-dependent envelope and for any
continuous main term; there is no assertion that the actual oscillatory
remainder is large.

For large \(L\le N\), choose fixed constants
\(0<c_1<c_2<\min(\delta,1/2)\) and shifts
\(c_1L\le h\le c_2L\). They lie below \(\delta N\), number \(\asymp L\),
have \(1-h/L\gg1\), and sum to \(\asymp L^2\).
Multiplying (R13)--(R15), summing these shifts, and applying \(N/L\)
therefore gives the positive error budget \(TL/N\).
The exact diagonal separately costs \(N^{1/2}/L\). Thus the two
optimistic certificate costs are

\[
 N^{1/2}/L,\qquad TL/N.                                 \tag{R16}
\]

Making both at most \(T^{2b}\) would require

\[
 N^{1/2}T^{-2b}\lesssim L\lesssim NT^{2b-1},
 \qquad N\gtrsim T^{2-8b}=T^{318/325}.                   \tag{R17}
\]

That is outside (R1). The product of the two costs is \(TN^{-1/2}\);
the uncapped norm certificate has exponent at least
\(1/4-\alpha/8\), exceeding \(b\) by at least \(19/650\) on the
closed required band. Bounded choices of \(L\) already fail at each
fixed interior exponent through the diagonal.

### Cap treatment and the centered mean are scoped correctly

Let \(A_h=\sum_n|c_nc_{n+h}W_h(n)|\), so \(|C_h|\le A_h\).
For centered coefficients on the same interior overlap,
\(A_h\gg N^{-1/2}\). An error-only cap by \(A_h\) after subtraction
of a nonzero mean is not generally a valid remainder bound.

The conductor explicitly grants it only as an optimistic allowance.
Equivalently, a genuine upper certificate
\(\min(A_h,|\mu_h\mathcal I_h|+\mathcal E_h\operatorname{Var})\)
is at least the optimistic
\(\min(A_h,\mathcal E_h\operatorname{Var})\).
Even the latter has the lower cost
\(\min(N^{-1/2},ThN^{-2})\) on the selected shifts.
The proportional shift sum therefore yields

\[
 N^{1/2}/L+\min(N^{1/2},TL/N).                           \tag{R18}
\]

Below the cap transition \(L\asymp N^{3/2}/T\), the incompatibility
(R17) remains. Above it, \(N^{1/2}\) exceeds \(T^{2b}\) at every
fixed interior exponent \(\alpha>4b\).
The capped comparison has no uniform fixed power gap as
\(\alpha\downarrow4b\); neither report needs such a gap to reject a
uniform whole-band theorem from this certificate.

Centering is not a zero-correlation-mean assertion. If a hypothetical
original correlation has continuous mean \(\rho_h(x-N)\), expanding
the centered product gives a continuous mean
\((\rho_h-\pi^2)(x-N)\), along with the original correlation error,
both ordinary shifted summatory errors, and bounded endpoint/floor
corrections. A singular-series formula is neither used nor supplied.
Treating the centered product as one signed object could cancel pieces
that would be lost by separately taking their absolute values.

### Actual CRT singletons: parity, modulus, full support, and shift sum

For original coefficients the exact divisor identity gives

\[
 C_h=16\sum_{d,e\le4N}\chi_4(d)\chi_4(e)
  \sum_{\substack{n\ge1\\n\equiv0\ (d)\\n\equiv-h\ (e)}}
             W_h(n)e(\phi_h(n)).                       \tag{R19}
\]

The cutoff is complete because a nonzero weight has both \(n\le4N\)
and \(n+h\le4N\). A CRT progression exists exactly when
\((d,e)\mid h\), and its step is \([d,e]\). No modulus larger than
the support is thrown away.

Fix \(0<\delta<1/10\) small enough for the common interior subband.
For even \(2\le h\le\delta N\), choose odd \(n_0\) in that subband
and put \(d=n_0,e=n_0+h\). These are allowed positive divisors,
both odd and at most \(4N\). Also
\[
 (d,e)=(n_0,h)\le h,\qquad
 [d,e]=\frac{n_0(n_0+h)}{(n_0,h)}
       \ge\frac{N^2}{h}\ge\frac N\delta>10N.            \tag{R20}
\]
The support of \(W_h\) lies in \([N,4N-h]\) and has length at most
\(3N\). The known solution \(n_0\) is therefore the only point of
its CRT progression anywhere in the full support, not merely the only
point in the selected subband.

The inner progression sum has exact modulus
\(|W_h(n_0)|\gg N^{-3/2}\), uniformly for every real \(R\).
There are \(\asymp N\) admissible odd \(n_0\), giving distinct divisor
pairs. Thus the sum of the exact moduli of these inner sums is
\(\gg N^{-1/2}\) for each selected even shift.
There is no opportunity for a better individual progression estimate
to reduce an already exact singleton modulus.

The character product is
\[
 \chi_4(n_0)\chi_4(n_0+h)
 =(-1)^{(n_0-1)/2+(n_0+h-1)/2}
 =(-1)^{h/2},                                         \tag{R21}
\]
independent of the odd \(n_0\). Its sign may change with the shift,
and the radius phases vary with \(n_0\). This validates the claimed
failure of a same-fibre character average while leaving genuine outer
phase cancellation entirely possible.

To make the positive object explicit, define the absolute outer
certificate by replacing (R19) and the real-part shift sum with
\[
 S_L^{\rm abs}
 =32\sum_{1\le h<L}(1-h/L)
     \sum_{d,e\le4N}|\chi_4(d)\chi_4(e)|
     \left|\sum_{\substack{n\ge1\\d\mid n,\ e\mid n+h}}
                 W_h(n)e(\phi_h(n))\right|.             \tag{R22}
\]
At growing \(L\le N\), the even shifts in the proportional range used
above still number \(\asymp L\). Equations (R20)--(R22) give

\[
 S_L^{\rm abs}\gg LN^{-1/2},\qquad
 (N/L)S_L^{\rm abs}\gg N^{1/2},                         \tag{R23}
\]
\[
 (N/L)^5\int_I(S_L^{\rm abs})^5\,dR\gg TN^{5/2},
 \qquad \frac{TN^{5/2}}U=T^{-18/65}N^3.                \tag{R24}
\]

The last exponent is already \(408/325>0\) at the lower band
boundary. Bounded \(L\) was separately rejected by its diagonal.
Hence every cutoff relevant to this positive closure is covered.
Expanding a centered product into the original product, two linear
pieces and a constant piece and then taking their separate absolute
values retains the obstruction from (R22). A genuinely combined centered
expansion is not refuted.

### Conductor bin transfer and final physical costs

The conductor's bin estimate is also correct as a finite analytic
statement. With \(t=x/X\), multiply each internally modulated bin by
a fixed cutoff supported on the enlarged \(J^*/X\) and equal to one
on \(J/X\). Fourier Cauchy uses
\(\sup_\xi\sum_j(1+|\xi-j|^2)^{-1}<\infty\).
Plancherel gives \(\sum_j(\|g_j\|_2^2+\|g_j'\|_2^2)\).
Multiplication by \(X\) and the chain rule return exactly
\(\sum_j\int_{J^*}(|B_j|^2+X^2|B_j'|^2)\).

Grouping fifth products by their maximum original quotient label
gives \(P_b^5-P_{a-1}^5\) on a fixed label interval, with the all-A
term assigned label zero. A prefix has at most logarithmically many
canonical intervals. Cauchy costs that logarithm and retains the
complete interval-energy sum. Smooth fixed-label polynomials extend
to \(J^*=[X/3,4X]\) through the same Fourier multipliers; no sharp
indicator is differentiated and no physical shell equivalence outside
\(J\) is required. The derivative-free and zero-th-bin countercontrols
in the ledger are valid generic controls, not actual arithmetic
counterexamples.

The inherited physical ledger is retained correctly. The original
complete moment still has both terms
\[
 M_{10}(H_N)\ll_\epsilon
          T^\epsilon(TN^{-3/110}+T^{8\omega}).
 \tag{R25}
\]
The first exceeds the target for \(\alpha>99/169\); deleting the
second does not solve the whole band.

For the complete shell \(Z_N\), rather than the rational main term
with its threshold error removed, the bridge gives
\[
 M_{10}(H_N)\ll T^{-6}K_{10}
          +T^{-4+\epsilon}N^{-10}+O_A(T^{-A}),
\]
\[
 K_{10}\ll T^6M_{10}(H_N)
          +T^{2+\epsilon}N^{-10}+O_A(T^{-A}).             \tag{R26}
\]
The powers follow from \(dx=2R\,dR\), \(R\asymp T\), and the full
tenth power of the explicit bridge error. No threshold term is missing
from (R26), because \(K_{10}\) here is the complete shell moment.
Replacing it by the rational main term separately incurs the inherited
threshold error already paid in the rational interface.

A successful original complex moment would bound the real moment and
therefore the original shell through (R26). A successful centered
moment instead gives its centered pointwise bound by reproduction and
then adds the reviewed discrete mean, of size
\(T^{303/4550+\epsilon}=o(T^b)\). That centered route alone is not
asserted to prove the original tenth moment or its shell equivalent.

The local reproduction factor is \(N^{1/20}\), with a positive window
margin and a global coefficient bound paying its off-window tail.
The outer ranges, equality endpoints, singleton, full infinite tail,
logarithmic recombination, \(\sqrt R\) reconstruction factor and sharp
error are unchanged. Either successful sufficient pointwise route would
give only \(102/325\), not the quarter theorem or an M1/M2 parent.

## 4. First doubtful or unproved step

No mathematical defect was found in the reviewed scoped claims.
The first missing signed input remains (R8), or a sufficient direct
estimate on \(\int Q_L^5\), for the actual coefficient vector throughout
the displaced window and the complete required band.

The first failed substitution in the Abel route would be replacing
the oscillatory error integral by a target-sized bound using only its
unweighted supremum without the variation factor. The first failed
substitution in the CRT route would be a target-sized positive outer
sum of the individual progression estimates. Their precise positive
budgets are refuted by (R16)--(R18) and (R23)--(R24), respectively.

No review statement lower-bounds the signed \(S_L\), \((S_L)_+\),
the actual \(Q_L\), or the actual moment by these budgets.
Negative correlations may cancel the diagonal, and phases may cancel
across the CRT singleton family and its complement. Those are still
unproved possible mechanisms.

The conductor's bin input likewise remains unproved at its target
scale. Its transfer is not an arithmetic estimate, and its sum over
all dyadic label intervals cannot be replaced by the unmasked energy.

## 5. Required controls and outcomes

| Control | Review outcome |
|---|---|
| Actual coefficients | GREEN: exact multiple-of-four jump floor, actual divisor identity, odd divisor pairs, and exact character product. |
| Fejer normalization and complete cutoff | GREEN: (R4)--(R5) include every multiplicity and zero-extension endpoint. No unpriced shift complement. |
| Diagonal and epsilon bookkeeping | GREEN: (R6)--(R8) include \(T\), \(N/L\) to the fifth power, all coefficient powers and integer rounding. |
| Abel transport and jump floor | GREEN: (R9)--(R15) verify the phase derivative, continuous integration by parts, true variation lower bound and real-prefix atom argument. |
| Cap and budget scope | GREEN with the explicitly optimistic interpretation above. The cap is not represented as a bound for a nonzero-main-subtracted error. |
| CRT singleton modulus and support | GREEN: parity, compatibility, \([d,e]>10N>3N\), uniqueness on the complete support, and distinct-pair multiplicity all hold. |
| Sum over shifts and centered expansion | GREEN: even proportional shifts have cardinality \(\asymp L\); bounded cutoffs use the diagonal. Separate absolute centered pieces retain the original-product obstruction, while combined cancellation remains open. |
| Signed versus absolute | GREEN: every lower obstruction is for a specified positive certificate. No signed lower bound or global arithmetic no-go is asserted. |
| Exact nonpairing relations | GREEN: all finite identities retain complete products. The supplied root multisets both sum to \(5m+5\) and give distinct positive square arguments; no pairing deletion occurs. |
| Real endpoints and physical costs | GREEN: real prefix limits, smooth overlap boundaries, actual displaced window, complete shell powers, reproduction and outer endpoints are all paid. |
| Bin-transfer scope | GREEN for the conductor's elementary transfer and maximum-label accounting; no claim of an actual target-sized bin input. |
| Full quarter and independence scope | GREEN: no new complete moment, pointwise exponent, M1/M2 closure or quarter theorem; this review is explicitly nonblind. |

No mathematical numerical control was run or used as certification.

## 6. Exact dependencies, hashes, and provenance

The two primary artifacts and their complete SHA-256 bindings appear
in Section 1. I read both in full and rederived their new finite claims
above. The following supplied dependencies were used only in their
already reviewed scope:

- rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md.
  SHA-256: 8fb9d01885057aa2981da9a746890968212a73103b7a079fcbc65e640d598df9.
  Used for the precise centered-route distinction and safe discrete mean.
- rounds/codex-managed/gc-complete-signed-tenth-moment/reviews/independent_high_values_review.md.
  SHA-256: e491f50df818cb7bac1f2a6d7f6101131345e835b01dab310c5d7875e515d0ca.
  Read in full for the inherited mean/source and endpoint seams.
- rounds/codex-managed/gc-complete-signed-tenth-moment/controls/conductor_tenth_power_ledger.md.
  SHA-256: c41087e887dbae00f8c721eab507588414d33d74202f3eb902b8a901048dbca3.
  Used for the complete two-term moment ledger and its scope.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.
  SHA-256: 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212.
  Inspected its precise unweighted source specialization and relevant
  endpoint/recombination statements; no fresh external source audit or
  arithmetic-weight extension is claimed.
- rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md.
  SHA-256: 6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552.
  Already read during the completed separate task; used for the actual
  local reproduction, physical shell bridge and complete complements.

The previously read protocol, active Round210 manifest, frozen strategy,
Round208 strategy checkpoint, Round209 synthesis and rational exact/near
review establish authority, scope and inherited conventions. The
authoritative starting graph hash is recorded above. None of those files
was edited.

The conductor received a substantive interim report that the Fejer,
cutoff, Abel, cap and CRT checks were passing, with the cap's precise
interpretation identified. This review supplies its own derivations,
not a vote or reliance on the claimant's status label. No sibling
isolated packet was opened. No new external theorem or source card was
imported.

## 7. Recommended state effect and final binding

GREEN: retain the two hash-bound primary artifacts as independently
checked scoped method evidence. The positive Abel-certificate and
outer-absolute CRT closures fail at the displayed powers, while the
actual signed residual remains open.

No complete arithmetic bound, new pointwise exponent, M1/M2 parent or
quarter statement should be promoted. This review supports the existing
no-change mathematical recommendation; graph decisions remain the
conductor's responsibility.

Only this assigned review file was written, apart from the conductor's
explicitly authorized boundary-definition clarification in the completed
signed_rational_bins report: its lattice coefficient formulas apply to
\(0\le r\le L\), with zero coefficients for \(r=-1\) and constant padding
for \(r>L\). That clarification changes no power or conclusion here.
The shifted claimant, conductor ledger, shared state, proof draft,
validation matrices, synthesis, legacy files and successor artifacts
were left unchanged. The review stops here.

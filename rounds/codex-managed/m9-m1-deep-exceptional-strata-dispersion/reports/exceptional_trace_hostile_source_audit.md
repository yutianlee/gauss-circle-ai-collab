# Round 87 hostile/source audit: exceptional trace strata

## 1. Result

**Result — exact pair-congruence classification and no-go for automatic
diagonal absorption or source-stacking.**  The divisor-aligned branches can be
identified exactly, but the frozen hypotheses and the current primary
theorems do **not** certify their aggregate as target-safe.

At every odd prime \(p\mid M\) with \(p\nmid K\), write the two ordered unit
pairs occurring after completion as

\[
 P_1=(x-h_1,x),\qquad P_2=(x-v-h_2,x-v).                 \tag{1.1}
\]

The two reciprocal-pole cancellation branches have the following literal
meaning:

\[
\begin{array}{c|c|c}
\text{branch}&\text{frequency congruences mod }p&
\text{ordered-pair congruence mod }p\\ \hline
A&h_1=h_2=0&P_1=(x,x),\ P_2=(x-v,x-v)\\
B&v=0,\ h_1=h_2&P_1=P_2.
\end{array}                                                     \tag{1.2}
\]

The local phase is constant only after imposing \(u=0\pmod p\) as well.
Thus a squarefree exceptional divisor can have branch \(A\) at some primes
and branch \(B\) at others; at prime powers the same conditions are only the
first residue-layer test and the valuation depth must still be recorded.

The large paired modes are diagonal only in the **completed Fourier index**
\(h_1=h_2\).  They are not the Fejer diagonal \(u=0\), and they are not the
physical diagonal \(n=m\).  Against the actual fourfold weight, the paired
coefficient is

\[
 \widehat\Omega_b(0,h,h)
 =\sum_{d,n,m}\Omega_{b,d,u}(n,m)e_M(h(n-m)),                  \tag{1.3}
\]

so the exact hostile choices \(h=M/p\) and \(h=M/\ell\) give respectively
the low-conductor twists \(e_p(n-m)\) and \(e_\ell(n-m)\), over all physical
pairs \((n,m)\).  A single such character is not a Kronecker delta.  Moreover,
on \(n=m\) the stationary phase is still

\[
 -\eta\lambda_b\bigl(\sqrt{|n+d+u|}-\sqrt{|n+d|}\bigr),       \tag{1.4}
\]

which is nonconstant for \(u>0\).  Hence the exact near-\(M^2\) modes cannot
be charged to the already accepted Fejer diagonal without a new weighted
estimate.

Finally, the post-\(D_1\) scalar \(b\)-phase variation

\[
 {D_1\over QB}={J^{31/140}\over B}\ge J^{1/14}                \tag{1.5}
\]

is numerically ample enough to be interesting, but it cannot lawfully be
multiplied by a pointwise generic trace saving.  The modulus, residue ring,
\(K\), completion frequencies, and exceptional divisor ledger all vary with
\(b\), while the frozen input has no bounded-variation or correlation theorem
for the resulting arithmetic coefficient as a function of \(b\).  A
pointwise bound followed by observation of phase variation gives no signed
cancellation: coefficients of the allowed pointwise size can always carry
the conjugate phase.  None of the primary sources checked below supplies the
missing varying-modulus hybrid theorem.

This is a no-go for the proposed black-box exceptional-stratum program, not
a lower bound for the complete signed aggregate.  The deep survivor remains
open.

## 2. Exact statement and hypotheses

Use the frozen scales

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad B=C/T,
 \qquad J^{11/90}<B\le J^{3/20},                                \tag{2.1}
\]

and

\[
 D_1=\lfloor J^{87/140}\rfloor,
 \qquad E_*=\lfloor Q^2J^{-1/20}\rfloor,
 \qquad \Delta_b\asymp Q^2.                                    \tag{2.2}
\]

For each of the three local classes

\[
 (g,M,K)=(1,4b,k),\quad
 (2,2b,2[k\bar4]_b),\quad
 (4,b,[k\bar4]_b),                                             \tag{2.3}
\]

one has \(gM=4b\) and \(M\asymp B\).  Put

\[
 A_d(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d),
 \qquad
 Z_b(d)=M^{-2}\sum_n A_d(n)I_b(n+d)\overline{I_b(n)},           \tag{2.4}
\]

with \(Z_b(d)=0\) unless \(D_1<|d|<\Delta_b-E_*\).  The requested
claim is

\[
 \mathfrak Y_{\rm deep}
 =\sum_{b\asymp B}\sum_d Z_b(d)
 \ll_\varepsilon X^\varepsilon J^{7/5}.                         \tag{2.5}
\]

A sufficient first A-process input, with its normalization unchanged, is

\[
 \mathcal E_1(D,U)=
 \sum_{b\asymp B}\sum_{1\le u<U}(U-u)
 \left|\sum_d Z_b(d+u)\overline{Z_b(d)}\right|
 \ll_\varepsilon X^\varepsilon
 {U^2\over B(D+U)}J^{14/5}.                                    \tag{2.6}
\]

The diagonal and the Fejer weights \(U-u\) are compulsory.  For \(u>0\),

\[
 \sum_dZ_b(d+u)\overline{Z_b(d)}
 =M^{-4}\sum_{d,n,m}A_{d+u}(n)\overline{A_d(m)}
 \Omega_{b,d,u}(n,m),                                          \tag{2.7}
\]

where zero extension imposes both deep cutoffs and

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}\overline{I_b(m+d)}I_b(m).          \tag{2.8}
\]

On a fixed compatible stationary branch its phase is

\[
 -\eta\lambda_b\bigl(
 \sqrt{|n+d+u|}-\sqrt{|n|}
 -\sqrt{|m+d|}+\sqrt{|m|}\bigr),
 \qquad \lambda_b=J+{\sqrt{\kappa k}\over b}\asymp J.           \tag{2.9}
\]

The hypotheses available for its amplitude are the frozen sampled
supremum/variation bounds in the physical variables; no uniform variation
bound in the modulus variable \(b\) is part of the packet.  The inherited
physical row size is \(TQ^{-5/24}\), hence its energy factor is
\(Q^{-5/12}\).  It must not be silently replaced by a source estimate.

The algebraic conclusions below are unconditional for every modulus in
(2.3).  The prime-local geometric conclusion is restricted to odd
\(p\mid M\) with \(p\nmid K\).  Primes dividing \(2K\), arbitrary higher
prime powers, and the full \(2\)-part are explicitly not absorbed into that
good-prime statement.

## 3. Proof or derivation

**Centered Fourier completion and normalization.**  Let

\[
 G_a(n)=S(n+a,K;M)\overline{S(n,K;M)}.
\]

Opening both Kloosterman sums and summing \(n\bmod M\) gives exactly

\[
 \sum_{n\bmod M}G_a(n)e_M(-hn)=M\mathcal C_{M,K}(a,h),          \tag{3.1}
\]

where

\[
 \mathcal C_{M,K}(a,h)=
 \sum_{\substack{y\bmod M\\ (y(y+h),M)=1}}
 e_M\!\left(a(y+h)+K((y+h)^{-1}-y^{-1})\right).                \tag{3.2}
\]

At \(h=0\), \(\mathcal C(a,0)=c_M(a)\).  Fourier inversion therefore
shows that centering is precisely deletion of the global zero mode:

\[
 A_a(n)=\sum_{\substack{h\bmod M\\h\ne0}}
 \mathcal C(a,h)e_M(hn).                                       \tag{3.3}
\]

This is also an exact bookkeeping of the Ramanujan terms.  If one uses
(3.3), no cross or square term is added separately; if one instead expands
\((G_{d+u}-c_M(d+u))\overline{(G_d-c_M(d))}\), the four-Kloosterman
main, two cross terms, and square term must all be retained exactly once.

For

\[
 \mathfrak T_M(u,v;h_1,h_2)=
 \sum_{a\bmod M}\mathcal C(a+u,h_1)
 \overline{\mathcal C(a,h_2)}e_M(-va),                          \tag{3.4}
\]

Fourier inversion in \(a=d\bmod M\) turns (2.7) into the exact centered
identity

\[
 M^{-5}\sum_{v\bmod M}
 \sum_{\substack{h_1,h_2\bmod M\\h_1\ne0,\ h_2\ne0}}
 \mathfrak T_M(u,v;h_1,h_2)
 \widehat\Omega_b(v,h_1,h_2),                                  \tag{3.5}
\]

where

\[
 \widehat\Omega_b(v,h_1,h_2)
 :=\sum_{d,n,m}\Omega_{b,d,u}(n,m)
 e_M(vd+h_1n-h_2m),                                             \tag{3.6}
\]

and the \(d\)-sum includes the two zero-extended deep cutoffs.  Thus the
external \(M^{-4}\) from the two rows and the further \(M^{-1}\) from
Fourier inversion are both visible.  The raw transform (3.4) itself retains
its outer factor \(M\) below.

**Ordered-pair congruences.**  Expanding (3.4) in variables \(y,z\), the
\(a\)-sum forces

\[
 y+h_1=z+h_2+v.
\]

With \(x=y+h_1\), the first ordered unit pair is
\(P_1=(y,y+h_1)=(x-h_1,x)\), and the second is
\(P_2=(z,z+h_2)=(x-v-h_2,x-v)\).  Orthogonality gives

\[
 \mathfrak T_M(u,v;h_1,h_2)
 =M\!\sum_{\substack{x\bmod M\\
 x,x-h_1,x-v,x-v-h_2\ {\rm units}}}
 e_M\!\left(ux+K\Phi_{h_1,h_2,v}(x)\right),                    \tag{3.7}
\]

with

\[
 \Phi=x^{-1}-(x-h_1)^{-1}-(x-v)^{-1}+(x-v-h_2)^{-1}.           \tag{3.8}
\]

At an odd \(p\nmid K\), the positive pole multiset is
\(\{0,v+h_2\}\) and the negative pole multiset is \(\{h_1,v\}\).
Equality has exactly the two matchings in (1.2).  This proves both the
local cancellation classification and its pair interpretation.  The
remaining phase is \(ux\), so it is constant exactly when \(p\mid u\).

For a squarefree divisor, let \(r_A\) be supported on good primes satisfying

\[
 p\mid u,\quad p\mid h_1,\quad p\mid h_2,                       \tag{3.9}
\]

and let \(r_B\) be supported on good primes satisfying

\[
 p\mid u,\quad p\mid v,\quad p\mid(h_1-h_2).                   \tag{3.10}
\]

Modulo \(r_A\), both ordered pairs are internally diagonal; modulo \(r_B\),
the ordered pairs agree componentwise.  The same prime may satisfy both, and
different primes may choose different branches.  This hybrid CRT possibility
is why a single global label “diagonal” loses information.  For
\(p^\nu\parallel M\), (3.9)--(3.10) are only necessary first-layer
conditions: the valuations of \(u,v,h_1,h_2,h_1-h_2\) determine the reduced
local conductor.

**The actual weight is not the physical diagonal.**  Define

\[
 F_{b,d}(h)=\sum_n I_b(n+d)\overline{I_b(n)}e_M(hn).
\]

On the paired branch \(v=0,h_1=h_2=h\), (3.6) factors exactly as

\[
 \widehat\Omega_b(0,h,h)
 =\sum_d F_{b,d+u}(h)\overline{F_{b,d}(h)}.                     \tag{3.11}
\]

It is a shift-\(u\) autocorrelation of one physical Fourier row.  Cauchy
bounds it by the corresponding fixed-frequency energy, but that observation
does not turn it into the Fejer diagonal: \(u\) is still positive, the large
arithmetic multiplier in (3.7) is still present, and no accepted estimate
sums the resulting fixed-frequency energies with the required \(M^{-5}\),
Fejer, \(b\), and divisor weights.  Nor can one invoke orthogonality in \(h\):
the exceptional term is a selected, divisor-dependent \(h\), and
\(\mathfrak T_M\) is not constant in \(h\).

The exact paired formula is

\[
 \mathfrak T_M(u,0;h,h)
 =M\sum_{\substack{x\bmod M\\ (x(x-h),M)=1}}e_M(ux).             \tag{3.12}
\]

Consequently, for an odd prime \(p\), \(\nu\ge2\), and \(p\nmid\alpha\),

\[
 \mathfrak T_{p^\nu}(p^{\nu-1}\alpha,0;
 p^{\nu-1},p^{\nu-1})=-p^{2\nu-1}.                             \tag{3.13}
\]

Here \(u>0\), \(h=M/p\ne0\pmod M\), so centering does not remove the mode,
and (3.11) contains \(e_p(n-m)\).  Likewise, for
\(M=\ell R\), \((\ell,R)=1\), with \(\ell\) a fixed odd prime,

\[
 \mathfrak T_{\ell R}(R,0;R,R)
 =\ell R\varphi(R)(-1-e_\ell(R)).                              \tag{3.14}
\]

For prime \(R\), this is \(\asymp_\ell M^2\), again at \(u=h=M/\ell<M\),
and its physical multiplier is \(e_\ell(n-m)\).  These identities prove
that prime-power and squarefree near-returns are genuine nonzero centered
modes.  They do not prove that (2.7) is large, because (3.11) may still
cancel after its full signed summation.

**Scale capacity and the \(b\)-phase seam.**  The inherited physical-row
triangle estimate misses the endpoint by

\[
 {C^3\over J^{13/6}}=J^{1/12}=B^{5/9}
 \quad(C=J^{3/4},\ B=J^{3/20}).                                \tag{3.15}
\]

Even optimistically granting a full generic square-root conductor saving
\(B^{-1/2}\) leaves \(B^{1/18}=J^{1/120}\).  On the other hand,

\[
 V_b:={D_1\over QB}={J^{31/140+o(1)}\over B},
 \qquad
 J^{1/14+o(1)}\le V_b<J^{25/252+o(1)}.                          \tag{3.16}
\]

Thus an ideal first-derivative factor \(V_b^{-1}\) would be numerically
more than enough at the endpoint.  This numerical comparison is not an
estimate.  If a theorem gives only \(|a_b|\le A_b\) for the arithmetic
coefficient, then

\[
 \left|\sum_b a_be(\phi_b)\right|\le\sum_b A_b
\]

is all that follows: the admissible extremal choice
\(a_b=A_be(-\phi_b)\) eliminates the observed phase.  To gain from
(3.16), one needs a theorem controlling the signed sequence \(a_b\), for
example bounded variation after a fixed finite stratification or a genuine
correlation/large-sieve estimate.  Here \(M\in\{b,2b,4b\}\), \(K\) is a
\(b\)-dependent residue class, the ring and its unit set change, prime-power
depths and branch assignments jump, and \(\widehat\Omega_b\) itself has no
frozen \(b\)-variation hypothesis.  Therefore a generic local trace bound
and (3.16) cannot be multiplied.

**Literal primary-source hypothesis map, checked through 2026-08-16.**
Normalized trace conventions matter: four normalized Kloosterman factors
correspond to a factor \(p^2\) when restored to the four unnormalized sums
used here.  Rational-phase theorems apply to the inner sum of (3.7); its
outer factor \(M\) remains.

| Primary theorem | Literal hypotheses and result | Map to (2.7)--(3.16) |
|---|---|---|
| Fouvry--Kowalski--Michel, [Corollaries 1.6--1.7 of *A study in sums of products*](https://arxiv.org/html/1405.2293v2) | A bounded-conductor bountiful sheaf over the prime field \(\mathbb F_p\).  Corollary 1.6 gives square-root cancellation when the tuple is normal or the additive twist is nonzero.  Corollary 1.7 additionally assumes equality of arithmetic and geometric monodromy (and the stated special-involution compatibility) and gives the paired non-normal main term. | It supports only the good-prime generic/paired dichotomy after the normalization is restored.  It has no \(p^\nu\), composite ring, \(2\)-adic, varying-\(b\), or archimedean-\(\Omega\) theorem.  The branch \(P_1=P_2\) is precisely the kind of non-normal return for which generic square root is unavailable. |
| Zheng, [Lemmas 2.7--2.8 and 2.10 of *Primes in simultaneous arithmetic progressions*](https://arxiv.org/html/2512.22798v1), and Wu--Xi, [Theorem A.1](https://arxiv.org/html/1603.07060v5) | Lemma 2.7 is prime-only and explicitly loses a factor \(p^{1/2}\) when the twist is zero and all shifts pair.  Lemma 2.8 is squarefree and treats the special four-term parallelogram, with displayed gcd losses.  Lemma 2.10 assumes every prime exponent is at most two.  Wu--Xi's general Theorem A.1 has the factor \(\Xi(c)^{1/2}\); the proof uses the trivial bound on every \(p^\beta\parallel c\) with \(\beta\ge3\). | The sources themselves expose rather than remove the paired/gcd strata.  The present four arguments are not generally Zheng's parallelogram.  For a full high prime power, Wu--Xi gives \(c^{1/2}\Xi(c)^{1/2}=c\) before further gcd losses for the inner sum, hence no saving.  None recombines exceptional divisors against (3.6). |
| Milićević--Zhang, [Theorem 4 of *Distribution of Kloosterman paths to high prime power moduli*](https://arxiv.org/html/2005.08865v1) | One fixed odd prime \(p\); \(p\)-adic square-root phases on a domain invariant under the specified deep translations; coefficient vector of bounded \(\ell^1\)-norm.  The conclusion is either a power saving or a collision of two active shifts modulo \(p^{\lfloor\delta_2n\rfloor}\). | The paired and near-return modes lie in the collision alternative, where no saving is asserted.  The theorem does not vary the prime/modulus, cover \(p=2\), or carry (3.11). |
| Cochrane--Granville, [Theorems 1.1 and 3.1 of *Mixed character sums modulo prime powers*](https://arxiv.org/html/2604.02614v1) | A rational mixed sum modulo \(p^m\).  In the nondegenerate additive case the displayed definition is \(D=\deg(f)+\mathcal Z(f_-g_+g_-)\), and Theorem 1.1 gives \(p^{m(1-1/D)}\), including an explicit \(p=2\) version.  Degeneration to modulus \(p^{m-\ell}\) costs \(p^{\ell/D}\); a constant phase has \(\ell=m\) and no nontrivial estimate. | For generic distinct poles and \(p\nmid uK\), \(f(x)=ux+K\Phi(x)\) has denominator degree \(4\), numerator degree \(5\), and \(D\le9\).  Thus even optimistic direct use saves only \(p^{m/9}\) on the inner sum, not square root and not the required aggregate gain by itself.  On (3.13), the phase has conductor \(p\), exactly the source's degeneration mechanism.  The theorem is pointwise in one \(p^m\), not a CRT, \(b\)-average, or actual-weight theorem. |
| Milićević--Qin--Wu, [Theorem 1.1 of *Bilinear forms with Kloosterman sums and moments of twisted \(L\)-functions*](https://arxiv.org/html/2511.07550v1) | One normalized kernel \(\mathrm{Kl}_2(cmn;q)\), two separated sequences on \([1,M]\), \([1,N]\), and \(M\le Nq^{1/4}\), \(M^{7/5}N<q^{3/2}\), \(MN\le q^{5/4}\).  The saving terms are exactly those displayed in its (1.3). | There is no substitution turning the four coupled kernels and (3.6) into this one kernel with separated coefficients.  Forcing a singleton column leaves the \(M^{-1/2}q^{1/6}\) term and gives no usable saving.  The modulus is fixed inside the theorem. |
| Pascadi, [Theorem 1.1 and Corollary 1.4 of *Non-abelian amplification and bilinear forms with Kloosterman sums*](https://arxiv.org/html/2511.08445v2) | Theorem 1.1 treats one \(S(am,n;c)\) with two coefficient sequences and \(M,N\ll c^{1/2+o(1)}\).  Corollary 1.4 averages \(c\) divisible by a fixed \(q\), but places an absolute value around each single-kernel bilinear form and keeps fixed coefficient sequences. | It does not match the centered four-kernel correlation.  Its modulus average cannot exploit the signed phase (3.16), because the absolute value is taken before the modulus sum and the present coefficients and supports move with \(b\). |
| Blomer--Pascadi, [Theorem 1.1 of *Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/html/2607.24311v1) | One \(S(am,n;c)\), a fixed arbitrary modulus \(c\), two intervals of length at most \(N\le c\), and separated \(\ell^2\) coefficients; the critical saving \(c^{-1/32+o(1)}\) requires both populated variables near \(c^{1/2}\). | Again there is no kernel or coefficient map to (3.5).  The theorem neither averages the changing modulus with a scalar phase nor estimates a fourfold self-return stratum. |
| Kerr--Shparlinski--Wu--Xi, [Lemma 4.1 of *Bounds on bilinear forms with Kloosterman sums*](https://arxiv.org/html/2204.05038v5) | A two-kernel complete correlation with the same varying second argument and fixed first arguments, with explicit gcd dependence, for one modulus \(q\). | The present pair has shifted varying arguments before completion and four kernels after squaring.  Completing it gives (3.7), including the return branches, not the cited two-kernel form. |

The newest prime-power rational theorem therefore improves the source
coverage of generic \(p^m\) and \(2^m\) pieces, but it does not alter the
verdict: its saving is pointwise and weak in the four-pole degree, and its
degenerate case contains exactly the reduced-conductor modes that must be
summed.  The bilinear results are stronger in their own single-kernel
settings but have no literal parameter map to the centered completed object.

## 4. First doubtful or unproved step

After the exact algebra (3.3)--(3.11), the first unproved step is a bound for
the completed exceptional contribution

\[
 M^{-5}\!\sum_{\substack{v,h_1,h_2\\
 \text{some good local factor satisfies (3.9) or (3.10)}}}
 \mathfrak T_M(u,v;h_1,h_2)
 \widehat\Omega_b(v,h_1,h_2),                                  \tag{4.1}
\]

summed with the exact \(b,u,U-u\) and deep-\(d\) structure of (2.6), together
with separate \(p\mid2K\), higher-power, and \(2\)-adic ledgers.  One must
either prove (4.1) target-safe and then prove a quantitatively sufficient
generic remainder, or retain (4.1) as a strictly smaller exact signed
survivor.  Equations (3.13)--(3.14) rule out replacing this by a uniform
\(M^{3/2+\varepsilon}\) coefficient bound, and (3.11) rules out declaring it
the already-paid physical diagonal.

The earliest illegitimate source step would be to assert that a generic
prime-field or prime-power bound supplies a conductor gain coefficientwise
and then multiply it by a saving inferred from (3.16).  None of the mapped
theorems controls the signed arithmetic coefficient while \(M\) varies, and
the packet supplies no \(b\)-variation estimate for that coefficient.  The
same gap remains if the generic estimate is proved separately: the generic
and exceptional decompositions jump with the factorization of \(b\), so a
common smooth \(b\)-amplitude has not been produced.

No calculation here shows that the full actual-symbol sum is large.  The
unproved possibility is genuine cancellation in (4.1), especially through
(3.11); what is ruled out is obtaining that cancellation from diagonal
terminology, pointwise trace estimates, or scalar phase variation alone.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `external_normalization` | **Pass for the identity; open for the estimate.**  Each \(Z_b\) carries \(M^{-2}\), (2.7) carries \(M^{-4}\), and completion in \(d\bmod M\) gives the exact \(M^{-5}\) in (3.5).  The raw transform retains its outer \(M\).  Four normalized prime-field Kloosterman factors require restoration of \(p^2\). |
| `all_class_local_units` | **Pass for the algebra, not a closure.**  The unit pairs (1.1) and identities (3.1)--(3.8) apply to all three classes (2.3).  The good-prime classification requires odd \(p\nmid K\); primes dividing \(2K\) remain separate in every class. |
| `physical_row_energy_factor` | **Fails certification.**  The inherited \(Q^{-5/12}\) is preserved as a requirement but is absent from all mapped source theorems.  Pointwise completion followed by absolute values does not reproduce it. |
| `deep_difference_ownership` | **Pass by scope.**  Only \(D_1<|d|<\Delta_b-E_*\) is used, with both \(d\) and \(d+u\) zero-extended.  The proved small-shift, support-edge, and cubic-shell regions are not reclaimed. |
| `negative_and_modulus_multiple_differences` | **Pass for classification; bound open.**  The residue algebra is independent of the sign representative and allows \(M\mid d\).  Neither family is deleted, and no target bound is claimed for it. |
| `ramanujan_cross_and_square_terms` | **Pass for bookkeeping; estimate open.**  Equation (3.3) encodes centering by deleting exactly the global \(h=0\) mode.  Equivalently, an uncentered expansion must retain the four-Kloosterman main, both cross terms, and the square once.  The hostile modes have \(h\ne0\pmod M\), so centering does not remove them. |
| `prime_power_and_2adic_strata` | **Fails closure.**  Equation (3.13), with the corrected hypothesis \(\nu\ge2\), is an exact high-depth mode.  Cochrane--Granville covers nondegenerate \(2^m\) and \(p^m\) phases only pointwise and weakly; its degenerate mechanism loses the saving here.  No full \(2\)-adic exceptional aggregate is proved. |
| `squarefree_divisor_aligned_modes` | **Fails automatic deletion.**  Equation (3.14) is \(\asymp_\ell M^2\) on the dyadic prime family \(M=\ell R\), at \(u=M/\ell<M\).  Its actual multiplier is the broad twist \(e_\ell(n-m)\), not \(1_{n=m}\). |
| `fejer_prefactor_and_diagonal` | **Pass.**  The \(U-u\) weights, full prefactor, and \(u=0\) diagonal remain compulsory.  The hostile modes have \(u=M/p\) or \(M/\ell>0\) and cannot be debited to that diagonal. |
| `actual_fourfold_stationary_symbol` | **Fails target certification.**  Equations (3.6), (3.11), and (1.4) retain the exact symbol.  They prove frequency-diagonality but disprove physical/Fejer-diagonality.  The required signed estimate is still (4.1). |
| `generic_trace_remainder` | **Open.**  Good-prime square root is available locally after normality/nondegeneracy checks, and Cochrane--Granville gives weaker generic prime-power bounds, but no theorem aggregates the remaining CRT factors and \(\widehat\Omega_b\) at the \(B^{5/9}\) endpoint capacity. |
| `entry_exit_and_error_ownership` | **Pass by scope.**  Zero extension owns the principal support endpoints.  Previously routed entry/exit, stationary-error, wrong-sign, exterior, raw-transition, and axial terms are not reintroduced. |
| `integer_and_perfect_power_resonance` | **Pass as a warning, not a new bound.**  No blanket nonresonance in \(b,n,m\) is used.  Previously isolated perfect-power loci remain separately owned; (3.16) is not promoted to a derivative estimate across them. |
| `complete_transform_self_return` | **Fails as a saving.**  Formula (3.7) is exact, and (3.12)--(3.14) show full and near self-return after completion.  Completion locates the obstruction but does not shrink it. |
| `source_hypothesis_map` | **Pass as a negative audit.**  Every mapped theorem is stated with its modulus type, normalization, kernel shape, length assumptions, exceptional alternative, and missing actual-weight/varying-modulus hypothesis.  None proves (4.1) or a sufficient generic complement. |
| `downstream_scope` | **Pass.**  No claim is made for \(C>J^{3/4}\), the rest of `M9-M1`, `M9-M2`, `M9`, endpoint uniformity, `R5-Full`, or the Gauss-circle exponent. |

No numerical experiment was used.  The controls are exact finite Fourier
identities, CRT/pole algebra, Ramanujan-sum evaluations already frozen in the
packet, scale arithmetic, and literal theorem-hypothesis checks.

## 6. Dependencies and exact artifacts used

Only the permitted selected context was used:

- `protocol.md`;
- `state/active_campaign.yml` at Round 87;
- `state/proof_obligations.yml`, specifically the entries
  `M9-M1`,
  `M9-M1-residual-upper-conductor-offdiagonal-reduction`,
  `M9-M1-centred-dual-difference-small-shift-bound`,
  `M9-M1-centred-dual-difference-support-edge-bound`, and
  `M9-M1-centred-dual-difference-cubic-shell-bound`, plus the relevant
  Round-82--86 rejection ledger;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/derivation_packet.md`,
  including the corrected condition \(\nu\ge2\) in (87.13);
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/four_kloosterman_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_rational_completion.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md`.

The current primary sources used are the exact arXiv versions linked in the
table in Section 3: Fouvry--Kowalski--Michel v2; Wu--Xi v5;
Milićević--Zhang v1; Zheng v1; Kerr--Shparlinski--Wu--Xi v5;
Milićević--Qin--Wu v1; Pascadi v2; Blomer--Pascadi v1; and the new
Cochrane--Granville v1 prime-power rational-sum paper.  No sibling Round-87
report was read.

## 7. Recommended state effect

**Revise the proposed mechanism and retain the deep obligation open.**
Record, subject to conductor verification, the exact centered Fourier
identity (3.3)--(3.6), the ordered-pair divisor interpretation (1.1)--(1.2),
and the no-go statement that paired near-\(M^2\) modes are only
frequency-diagonal, not Fejer/physical-diagonal.  Reject both of the following
as proof steps:

1. absorbing \(v=0,h_1=h_2\) into the accepted A-process diagonal; and
2. multiplying a pointwise generic trace saving by the scalar variation
   \(D_1/(QB)\) without a varying-modulus coefficient theorem.

Do not promote (2.5), (2.6), an exceptional aggregate bound, or a new
conductor range.  The smallest admissible next input is a theorem for the
signed sum (4.1), or a strictly smaller exact survivor, with an explicit
hybrid divisor/valuation ledger, all three classes, the full \(2\)-part,
the centered zero-mode accounting, the actual transform (3.11), and a
quantitatively sufficient generic remainder that preserves \(Q^{-5/12}\).

**Supplemental claimant-specific addendum (2026-08-17; preserving the
original independent verdict above).**  After the original report was
completed, the conductor authorized a focused read of
`rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/aligned_mode_aggregate_attack.md`.
The following supersedes only the earlier statement that no target-safe
aggregate estimate had yet been supplied for the full-factor paired/local-zero
block.  The source-stacking and \(b\)-phase no-go, and the conclusion that the
whole deep survivor is open, remain unchanged.

**Supplemental result: certify the normalized-row \(U=D\) estimate, with
two scope corrections.**  Put

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),\qquad
 L=TQ^{-5/24},
\]

and, for a globally off-diagonal ordered unit pair \(P=(x,y)\),

\[
 F_{b,P}(\theta)=e_M(K(\bar x-\bar y))
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
\]

Direct extraction of the \(d\)-th Fourier coefficient gives

\[
 \widehat F_{b,P}(d)
 ={e_M(dx+K(\bar x-\bar y))\over M^2}
 \sum_n I_b(n+d)\overline{I_b(n)}e_M(n(x-y)).                  \tag{7.A1}
\]

Thus the two \(M^{-1}\) row normalizations supply exactly the external
\(M^{-2}\) in \(Z_b(d)\).  There is no further \(M^{-2}\) outside
\(F_{b,P}\); inserting one would create the false gain \(M^{-4}\).  Passage
between the three classes and the ambient \(4b=gM\) progression can introduce
only the fixed factor \(g\in\{1,2,4\}\), not a power of \(B\).

Factor \(M\) into its full prime-power factors \(q\), and let
\(S(P)=\{q:x_q\ne y_q\pmod q\}\).  Since \(P\) is globally off-diagonal,
\(S(P)\ne\varnothing\).  For two pairs \(P,P'\), at every full factor the
alternative

\[
 \text{both pairs locally diagonal}\quad\hbox{or}\quad
 \text{the two ordered pairs are locally identical}            \tag{7.A2}
\]

holds if and only if

\[
 S(P)=S(P')\quad\hbox{and their active ordered-pair labels agree}. \tag{7.A3}
\]

Indeed, an active factor cannot use the first branch and so must use the
second; an inactive factor uses the first, with its two diagonal units
independent.  If the two diagonal units happen to agree, both descriptions
hold, and assigning that intersection to the first branch counts it once.
The omitted case \(S=\varnothing\) is exactly the globally diagonal pair
deleted by centering.  Consequently the active-set grouping is the exact
one-count version of every mixture of the two **full-\(q\)** branches in the
centered product.

This also settles Ramanujan ownership.  The identity

\[
 A_d(n)=\sum_{x\ne y}^{*}
 e_M\!\left(n(x-y)+dx+K(\bar x-\bar y)\right)
\]

is already \(S\overline S-c_M(d)\).  Its product therefore contains the
four-Kloosterman main, the two cross terms, and the Ramanujan square with
their exact signs; the all-locally-diagonal \(S=\varnothing\) block cancels
and must not be restored on top of the pair grouping.

There is no hidden conductor power in the claimed norm estimate.  For
\(m_S=\prod_{q\in S}q\), \(r_S=M/m_S\), a fixed \(S\) has at most
\(m_S^2\) active labels and at most \(r_S\) inactive diagonal units.  The
sharp interval projection costs \(O(\log J)\), hence

\[
 \sum_\alpha|H_{b,S,\alpha}(\theta)|^2
 \ll_\varepsilon X^\varepsilon m_S^2r_S^2L^4
 =X^\varepsilon M^2T^4Q^{-5/6}.                               \tag{7.A4}
\]

The \(2^{\omega(M)}\) active sets cost only \(M^\varepsilon\),
\(\int_{\mathbb T}|D_U|^2=U\), there are \(O(B)\) values of \(b\), and
\(M\asymp B\).  Therefore

\[
 \boxed{\mathcal P_{\rm exc}(D,U)
 \ll_\varepsilon X^\varepsilon U B^3T^4Q^{-5/6}.}              \tag{7.A5}
\]

The powers in (7.A5) are compulsory: one \(B\) counts moduli and \(B^2\)
counts the pair groups after their inactive sums are squared.  The formerly
suggested \(UT^4Q^{-5/6}/B\) is smaller by \(M^4\) and is false on this
argument.

With \(U=\lfloor D\rfloor\asymp D\), which is permitted and satisfies
\(D\ge D_1\gg M\), the required signed scale is
\((D/B)J^{14/5}\).  Since

\[
 B^4T^4Q^{-5/6}
 \le J^{3/5}J^{12/5}J^{-1/3}
 =J^{8/3}=J^{14/5-2/15},                                      \tag{7.A6}
\]

(7.A5) wins by \(J^{-2/15}\), uniformly in the frozen conductor range.
This uses no cancellation in \(b\).

The Fejer implication is precisely symmetric and signed.  If
\(\mathcal D_{\rm exc}=\sum_{b,S,\alpha,d}|h_{b,S,\alpha}(d)|^2\) and
\(\mathcal O_{\rm exc}\) denotes the positive-shift sum, then

\[
 \mathcal P_{\rm exc}(D,U)
 =U\mathcal D_{\rm exc}+2\Re\mathcal O_{\rm exc}.              \tag{7.A7}
\]

Both \(\mathcal P_{\rm exc}\) and \(U\mathcal D_{\rm exc}\) obey the
right side of (7.A5), so
\(|2\Re\mathcal O_{\rm exc}|\) does as well up to a constant.  This is the
outside-absolute symmetric interface allowed by the packet.  It does **not**
prove \(\sum_u(U-u)|C(u)|\), \(|\mathcal O_{\rm exc}|\), or a bound for any
individual shift.

The argument is characteristic-free physical CRT algebra.  It applies to
all three classes, every full odd prime power, the complete \(2\)-part, and
primes dividing \(K\).  Additional bad-prime or \(2\)-adic coincidences that
do not satisfy (7.A2) remain in the residual.  The large choice \(U=D\)
also includes every same-group term at strides \(u=jM\); no factor \(D/M\)
is missing because those shifts occur inside the single positive norm whose
Dirichlet-kernel mass is \(U\).

Two wording corrections are required.  First, (7.A5) does not remove
**all** stride-\(M\) correlations: cross-group terms at \(u=jM\) remain in
the residual.  It is accurate to say that all stride-\(M\) returns belonging
to the extracted full-factor same-group block are included and bounded.
Second, the cross-group residual is strictly smaller only in the exact
combinatorial sense.  If two group labels differ, some full factor has one
pair active and the other inactive, or two unequal active pairs, so neither
branch in (7.A2) holds there.  This removes every all-full-factor branch
mixture exactly once, but supplies no quantitative saving for the remainder.
Formula (2.13) of the claimant report also retains cross-group \(u=0\)
terms; if the accepted full Fejer diagonal is kept with its former owner,
the residual should instead be written with \(u\ne0\).  Likewise, the
period-depth discussion must be read as a stratification of
**cross-group** local summands, not as saying that every partial period in
the original correlation remains.

**Updated state recommendation.**  Promote after conductor verification
only the scoped lemma (7.A5)--(7.A7): at \(U=D\), the complete centered
same-group aggregate for mixtures of the two full-prime-power branches is
target-safe against the actual fourfold symbol as a symmetric signed Fejer
estimate.  Retain the cross-group correlation as a structurally strict but
analytically unbounded survivor, including partial-depth returns and extra
bad-prime/\(2\)-adic coincidences.  Do not promote (87.2), the per-shift
absolute estimate (87.7), a bound for the cross-group survivor, a claim that
all stride-\(M\) correlations were removed, or any \(b\)-phase saving.

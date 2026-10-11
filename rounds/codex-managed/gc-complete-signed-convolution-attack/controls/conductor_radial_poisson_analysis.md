# Round 203 conductor: radial Poisson and restored powers

Campaign: gc-complete-signed-convolution-attack. Generated: 2026-09-23.
Starting graph SHA256: abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb.
Role: independent conductor analysis, not graph promotion. Context:
protocol.md; state/proof_obligations.yml; active Round203 manifest;
the frozen strategy; the reviewed Round202 signed-tail interface.
No subagent derivation was used for the calculation below.

## 1. Result

Radial Poisson transforms each actual smooth frequency block into an
odd, signed local lattice shell. Taking absolute values on that shell
recovers at best the classical radius exponent 1/6 for the normalized
sum, hence discrepancy exponent 1/3. It supplies no improvement over
the accepted Li--Yang benchmark and no new twelfth-moment bound.
The cancellation required by the full target remains inside a signed
shell sum; the transform has not estimated it.

## 2. Exact statement and hypotheses

Let v be fixed smooth supported in [1,2], T>=2, R in [cT,CT], and
1<=N<=T^(1+alpha) for fixed 0<alpha<1. Set

\[
 b_{N,T}(r)=\Psi(r/\sqrt T)v(r^2/N),\qquad
 H_N(R)=\sum_{n\ge1}r_2(n)n^{-3/4}b_{N,T}(\sqrt n)
                 \cos(2\pi R\sqrt n-3\pi/4),
\]
\[
 L_{N,T}(z)=\int_0^\infty r^{-1}b_{N,T}(r)\sin(2\pi zr)\,dr.
\]

All constants may depend on v, Psi, c,C, alpha and epsilon. The
Schwartz seminorms of b after rescaling r=sqrt(N)t are bounded
uniformly, including N>T. Thus L is odd and

\[
 |L_{N,T}(z)|\ll_A(1+\sqrt N|z|)^{-A}.
\]

The complete block formula is

\[
 H_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}
                L_{N,T}(R-\sqrt m)
       +O_\epsilon(T^{-1/2+\epsilon}N^{-1})+O_K(T^{-K}). \tag{P1}
\]

The constants in the last error depend also on K. This is an
oscillatory summation identity, not a moment estimate.

## 3. Derivation and complete power accounting

Apply two-dimensional Poisson to the compactly supported smooth
radial function

\[
 f(x)=|x|^{-3/2}b_{N,T}(|x|)\cos(2\pi R|x|-3\pi/4).
\]

It vanishes near zero. The exact transform at a dual vector of length
s is

\[
 2\pi\int_0^\infty r^{-1/2}b_{N,T}(r)
       \cos(2\pi Rr-3\pi/4)J_0(2\pi sr)\,dr. \tag{P2}
\]

For R/2<=s<=2R use the fixed-order real positive argument expansion
of J0 through its first correction. Its leading term is
(pi sqrt(sr))^(-1) cos(2 pi sr-pi/4); the next term has size
O((sr)^(-3/2)); after that the remainder is O((sr)^(-5/2)).
The exact reference is [DLMF 10.17.3 and 10.17(iii)](https://dlmf.nist.gov/10.17),
checked 2026-09-23. The polar identity in (P2) follows from
[DLMF 10.9.1](https://dlmf.nist.gov/10.9.E1).

The leading product of cosines is exactly

\[
 s^{-1/2}\int r^{-1}b_{N,T}(r)
 \{\sin(2\pi(R-s)r)-\cos(2\pi(R+s)r)\}\,dr. \tag{P3}
\]

In particular, replacing the sine by a cosine, or using a positive
kernel at s=R, would lose the actual phase. The second term in (P3)
is arbitrarily small after radial integration by parts.

For s~T, the first correction is bounded by

\[
 C_A T^{-3/2}N^{-1/2}
    (1+\sqrt N|R-s|)^{-A}+O_K(T^{-K}).
\]

The elementary divisor bound and the spacing of integer m imply

\[
 \sum_{m: \sqrt m\asymp T}r_2(m)
       (1+\sqrt N|R-\sqrt m|)^{-A}
 \ll_\epsilon T^\epsilon(1+T/\sqrt N)
 \ll_\epsilon T^{1+\epsilon}N^{-1/2}. \tag{P4}
\]

To check (P4), split |R-s| into intervals of length N^(-1/2),
each containing O(1+T/sqrt(N)) possible integer squared lengths,
and sum the decaying interval weights. The last inequality uses
N<T^2. The correction therefore totals O(T^(-1/2+epsilon)N^(-1)).
The pointwise remainder in (P2) is O(T^(-5/2)N^(-1)); summing
over O(T^2) dual lattice points gives the same error.

For 0<=s<R/2, use the angular integral for J0 and integrate in r:
the two phases have radial derivative at least R/2 in modulus.
The transform is O_A(N^(1/4)(T sqrt(N))^(-A)). There are O(T^2)
such dual points. For s>2R, scale x=sqrt(N)y and integrate the
full two-dimensional phase: its gradient has modulus at least
sqrt(N)(s-R)>=sqrt(N)s/2. The resulting bound
O_A(N^(1/4)(s sqrt(N))^(-A)) is summable. These contributions,
including the zero vector, are O_K(T^(-K)). The same decay permits
extending the main sum in (P3) to every nonzero dual lattice point.
This proves (P1), with a complete summable remainder.

Applying (P4) to (P1) gives

\[
 |H_N(R)|\ll_\epsilon T^{1/2+\epsilon}N^{-1/2}+O(T^{-1/2+\epsilon}).
\]

The original block also gives |H_N|<<N^(1/4+epsilon), so the
complete elementary estimate is

\[
 |H_N(R)|\ll_\epsilon T^\epsilon
       \min\{N^{1/4},T^{1/2}N^{-1/2}\}+O(T^{-1/2+\epsilon}). \tag{P5}
\]

The worst intersection is N=T^(2/3), with size T^(1/6).
Use a smooth dyadic partition for n>=2U. The remaining sharp-cutoff
block U<n<4U costs O(U^(1/4+epsilon)). Truncate at
V=T^(1+alpha); the actual Schwartz upper tail is O_K(T^(-K))
in l1 by increasing the fixed seminorm order. Sum the O(log T)
blocks. Since U=floor(T^(1/2047)), the sharp-cutoff block is
smaller than T^(1/6). This restores the *entire* actual tail and
gives the classical bound O(T^(1/6+epsilon)), with no missing band.
It is weaker than the inherited T^(beta+epsilon), beta=2theta-1/2.

Using the inherited residual L2 bound with the new elementary
supremum only yields

\[
 \int\chi(R/T)^2|B(R)|^{12}dR
 \ll T^{8/3+\epsilon}U^{-1/2},
 \qquad \|K_T*\mu^{*6}\|_2\ll T^{4/3+\epsilon}U^{-1/4}.
\]

This does not compete with the inherited norm exponent
1/2+(12-q0)beta/2=0.648072478..., and is far from 29/50.

## 4. First unproved step

One needs an estimate for the complete signed shell sums in (P1)
and their cross-block products, strong enough to make the actual
twelfth moment T^(29/25+epsilon). Bound (P4) removes precisely that
cancellation. Knowing that L is odd gives no arithmetic bound for
the discrete, non-symmetric lattice radii. Replacing r2 by its area
density makes a smooth integral small but leaves the full arithmetic
discrepancy. Neither operation proves the target.

## 5. Controls

- Exact phase: cos(Rr-3pi/4) times cos(sr-pi/4) produces the odd sine
  at R-s and the negative cosine at R+s. L(0)=0.
- Exact arithmetic multiplicity: dual vectors are grouped with r2(m).
- Tails: far dual vectors are nonstationary; high original frequencies
  use Schwartz decay; the hard lower cutoff is bounded explicitly.
- Real R and T: interval counting includes endpoints and the +1 term
  before using N<T^2. No integer-radius restriction appears.
- No numerical experiment. All bounds are analytical.
- No full signed moment lower bound, no exponent gain, and no graph
  promotion follow from the shell representation.

## 6. Dependencies and exact artifacts

The context is listed at the top. The only primary formula check is
DLMF 10.9.1, 10.17.3 and its real-argument remainder statement.
This note imports no new number-theoretic theorem. The residual L2
and inherited exponent comparison are the reviewed Round202 evidence,
with their original graph/source status retained.

## 7. State effect

No change. Archive the complete Poisson calculation as an unsuccessful
bounded analytic attempt. Keep the stronger inherited bound and the
full signed target open. This is not a no-go for exploiting the
remaining signed arithmetic shell cancellation by a stronger method.

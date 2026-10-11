# 1. Result: the smooth actual norm-tail estimate holds

- Campaign: `round231_balanced_cancellation`; task: `blind_hankel_tail`.
- Role/status: statement-only independent analytic rederivation; candidate proof, not an accepted graph mutation.
- Generated: 2026-10-11T07:24:55Z.
- Graph hash: deliberately unavailable under the isolation brief; no graph or historical report was read.
- Context: exactly the three local files listed in Section 6, plus the primary Bessel references listed there.
- Effort: analytical/algebraic; no numerical experiment.

The proposed estimate is valid. In fact, its lower cutoff restriction is unnecessary: for every epsilon > 0, uniformly for real T >= 2, T/2 <= R <= 2T, and **1 <= Y <= T**, the actual sum satisfies

\[
 |F_{T,Y}(R)|\ll_{\rho,\eta,\varepsilon}
 T^\varepsilon\sqrt{T/Y}.
 \tag{1}
\]

This implies the requested bound throughout T^(2/5) <= Y <= T. The proof uses exact two-dimensional Poisson summation, two terms of the real J_0 expansion, and the permitted pointwise bound on r_2. It accounts for zero frequency, both resulting phases, and all dual lattice indices. The sine at the difference phase removes a potential logarithm, but no additional power saving from cancellation between distinct dual norms is asserted.

# 2. Exact statement and hypotheses

Let rho be the fixed real, nonnegative, radial C-infinity function compactly supported in the unit disk, with integral 1, and put

\[
 e(t)=e^{2\pi i t},\qquad
 \Psi(s)=\int_{\mathbb R^2}\rho(y)e(-s y_1)\,dy.
\]

Let eta be fixed and C-infinity on (0,infinity), zero for t <= 1, one for t >= 2, with 0 <= eta <= 1. Let r_2(n) count all ordered signed integer pairs of squared norm n, for n >= 1. Define the absolutely convergent sum

\[
 F_{T,Y}(R)=\sum_{n\ge1}r_2(n)n^{-3/4}
 \Psi(\sqrt{n/T})\eta(n/Y)
 \cos(2\pi R\sqrt n-3\pi/4).
 \tag{2}
\]

Then (1) holds in the real parameter range stated in Section 1. Constants may depend on the fixed rho and eta, and on epsilon, but not on T, R, Y, their fractional parts, or the distance from R^2 to an integer. Only the following nonlocal inputs are used: Poisson summation for Schwartz functions, r_2(n) <<_delta n^delta for each delta > 0, and the specifically cited real-argument Bessel identities. No circle-discrepancy or moment estimate is used.

# 3. Proof and complete error ownership

## 3.1. Uniform amplitude bounds

Write

\[
 A=\sqrt Y,\qquad B=\sqrt T,\qquad
 w(u)=\Psi(u/B)\eta(u^2/A^2)\quad (u>0).
 \tag{3}
\]

Thus 1 <= A <= B. Differentiation under the defining integral for Psi, followed by integration by parts in y_1, gives

\[
 |\Psi^{(j)}(s)|\le C_{j,N}(1+|s|)^{-N}
 \quad(j,N\ge0).
 \tag{4}
\]

Compact support and smoothness of rho justify all these integrations. Radiality makes Psi real and even, and nonnegativity and normalization give |Psi| <= 1. No assertion that Psi itself is nonnegative is used.

The function w vanishes for u <= A, and its derivatives vanish at u=A. Put E(t)=eta(t^2). Every positive-order derivative of E is supported in [1,sqrt(2)]. Using (4) in the product rule gives, for u >= A,

\[
 |w^{(j)}(u)|\le C_j u^{-j}.
 \tag{5}
\]

Indeed B^(-l)|Psi^(l)(u/B)| <= C_l u^(-l), and on the support of a positive-order derivative of E(u/A) one has u comparable to A. These constants are independent of B/A. For each fixed A,B all amplitudes below decay rapidly at infinity.

Set a_p(u)=u^(-p)w(u), extended by zero to u <= A. Product differentiation yields

\[
 \|a_p^{(k)}\|_{L^1(A,\infty)}
 \le C_{p,k}A^{1-p-k}\qquad(p+k>1).
 \tag{6}
\]

This is the elementary integral of u^(-p-k), not a bound with an omitted upper-tail dependence.

For p=1 define

\[
 S(s)=\int_A^\infty a_1(u)\sin(2\pi su)\,du,
 \qquad
 C(s)=\int_A^\infty a_1(u)\cos(2\pi su)\,du.
\]

For every integer K >= 1,

\[
 |S(s)|\le C_K(1+A|s|)^{-K}\quad(s\in\mathbb R),
 \tag{7}
\]

and

\[
 |C(s)|\le C_K(A|s|)^{-K}\quad(s\ne0).
 \tag{8}
\]

To prove the uniform size assertion in (7), S(0)=0. For s nonzero put U=max(A,1/|s|). On [A,U], if nonempty, use |sin(2 pi s u)| <= 2 pi |s|u and |w| <= 1; the integral is O(|s|U)=O(1). On [U,infinity), one integration by parts, (5), and |a_1(U)| <= C/U give O(1/(|s|U))=O(1). For high frequency, integrate K times using (6) with p=1. There are no endpoint terms, since all derivatives vanish at A and at infinity. This gives O((A|s|)^(-K)) and proves (7). The same repeated integration proves (8). No boundedness of C(0) independent of B/A is claimed or needed.

For p=2 let C_2 and S_2 denote the corresponding cosine and sine integrals. The L^1 estimate (6) with k=0, combined with repeated integration by parts, gives

\[
 |C_2(s)|+|S_2(s)|
 \le C_K A^{-1}(1+A|s|)^{-K}
 \quad(s\in\mathbb R).
 \tag{9}
\]

## 3.2. Exact Poisson normalization and zero frequency

Define on R^2, with the value zero near the origin,

\[
 f(x)=|x|^{-3/2}w(|x|)
       \cos(2\pi R|x|-3\pi/4).
\]

For every fixed T,Y,R this is Schwartz: it is smooth and identically zero on |x| <= A, and (4) supplies rapid decay at infinity. With Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R^2}f(x)e(-x\cdot\xi)\,dx,
\]

Poisson therefore applies directly and exactly:

\[
 F_{T,Y}(R)=\sum_{k\in\mathbb Z^2}f(k)
          =\sum_{m\in\mathbb Z^2}\widehat f(m).
 \tag{10}
\]

The zero primal term is zero. Grouping nonzero primal vectors by their squared norm gives exactly r_2(n), with no extra factor or coefficient replacement.

The angular identity

\[
 \int_0^{2\pi}e^{-iz\cos\theta}\,d\theta=2\pi J_0(z)
\]

follows from [DLMF 10.9.1](https://dlmf.nist.gov/10.9.E1) by symmetry. Hence, for v=|m| > 0,

\[
 \widehat f(m)=2\pi\int_A^\infty u^{-1/2}w(u)
 \cos(2\pi Ru-3\pi/4)J_0(2\pi vu)\,du.
 \tag{11}
\]

At zero frequency the Bessel factor is 1. Two integrations by parts using (6), p=1/2 and k=2, give the explicit uniform bound

\[
 |\widehat f(0)|\le C R^{-2}A^{-3/2}.
 \tag{12}
\]

Thus the zero dual mode has been retained and estimated, not discarded by an oscillation heuristic.

## 3.3. Two Bessel terms, both phases, and a summable remainder

For x>0 the order-zero expansion with its real-argument remainder is

\[
 J_0(x)=\sqrt{\frac2{\pi x}}
 \left\{\cos(x-\pi/4)+\frac{\sin(x-\pi/4)}{8x}\right\}
 +\mathcal R(x),
\]

\[
 |\mathcal R(x)|\le\sqrt{\frac2{\pi x}}
 \left(\frac9{128x^2}+\frac{75}{1024x^3}\right).
 \tag{13}
\]

This specialization uses [DLMF 10.17.1--10.17.3](https://dlmf.nist.gov/10.17#i) and its [real-order error bound, Section 10.17(iii)](https://dlmf.nist.gov/10.17#iii): nu=0, one retained term in each even/odd series, and x>0. Both required truncation inequalities hold with ell=1. In this application x=2 pi v u >= 2 pi, because v>=1 and u>=A>=1, so the remainder is O((vu)^(-5/2)).

The normalized version used in (11) is

\[
 J_0(2\pi vu)=\frac{\cos(2\pi vu-\pi/4)}{\pi\sqrt{vu}}
 +\frac{\sin(2\pi vu-\pi/4)}{16\pi^2(vu)^{3/2}}
 +O((vu)^{-5/2}).
 \tag{14}
\]

Put phi=2 pi R u-3 pi/4 and theta=2 pi v u-pi/4. The exact product identities are

\[
 2\cos\phi\cos\theta
   =\sin(2\pi(R-v)u)-\cos(2\pi(R+v)u),
\]

\[
 2\cos\phi\sin\theta
   =\cos(2\pi(R-v)u)-\sin(2\pi(R+v)u).
 \tag{15}
\]

Consequently (11) becomes

\[
 \widehat f(m)=v^{-1/2}\{S(R-v)-C(R+v)\}
 +\frac{v^{-3/2}}{16\pi}
      \{C_2(R-v)-S_2(R+v)\}+E_m,
 \tag{16}
\]

with

\[
 |E_m|\le C v^{-5/2}\int_A^\infty u^{-3}|w(u)|\,du
           \le C v^{-5/2}A^{-2}.
 \tag{17}
\]

This is valid for every nonzero dual lattice vector, with no upper restriction on v. In dimension two,

\[
 \sum_{m\in\mathbb Z^2\setminus\{0\}}|m|^{-5/2}<\infty:
\]

dyadic boxes contain O(2^(2j)) lattice points while their summands are O(2^(-5j/2)). Therefore

\[
 \sum_{m\ne0}|E_m|\le C A^{-2}.
 \tag{18}
\]

Keeping the second Bessel term is essential to this simple error treatment: a one-term expansion would leave a v^(-3/2) remainder whose absolute lattice sum diverges. No derivatives of the Bessel remainder, and no integration by parts inside that remainder, have been assumed.

## 3.4. Uniform summation over all dual norms

Fix 0<delta<=1/8 and take K=4 (any sufficiently large fixed integer works). For q in {1/2,3/2}, define

\[
 D_q=\sum_{n\ge1}r_2(n)n^{-q/2}
 \left\{(1+A|R-\sqrt n|)^{-K}
              +(A(R+\sqrt n))^{-K}\right\}.
\]

For all real R>=1 and A>=1,

\[
 D_q\le C_{\delta,K}R^{-q+2\delta}(1+R/A).
 \tag{19}
\]

Here is a direct proof, including the tails. In the central region R/2 <= sqrt(n) <= 2R,

\[
 |R-\sqrt n|=\frac{|R^2-n|}{R+\sqrt n}
                  \ge\frac{|R^2-n|}{3R}.
\]

Using r_2(n) <= C_delta n^delta and the elementary shifted-grid bound

\[
 \sum_{j\in\mathbb Z}(1+\lambda|j-x|)^{-K}
       \le C_K(1+\lambda^{-1})
       \quad(\lambda>0,\ x\in\mathbb R)
 \tag{20}
\]

gives the right side of (19) for the central difference phase. To verify (20), split the integers to the two sides of a nearest integer to x and compare the decreasing tails with the integral of (1+lambda t)^(-K). This proof is uniform at integral, half-integral, and arbitrary real x.

For sqrt(n)<R/2 the difference is at least R/2. Since q<2 and delta>0, the corresponding contribution is at most

\[
 C(AR)^{-K}\sum_{n\le R^2/4}n^{\delta-q/2}
       \le C A^{-K}R^{2-q-K+2\delta}.
 \tag{21}
\]

For sqrt(n)>2R the difference is at least sqrt(n)/2. The entire infinite tail is at most

\[
 C A^{-K}\sum_{n>4R^2}n^{\delta-(q+K)/2}
       \le C A^{-K}R^{2-q-K+2\delta}.
 \tag{22}
\]

The exponent in this series is strictly less than -1 for the stated choices. For the R+sqrt(n) phase, split at sqrt(n)=2R: use R+sqrt(n)>=R below the split and R+sqrt(n)>=sqrt(n) above it. This gives the same bound as (21)--(22). Finally,

\[
 A^{-K}R^{2-q-K+2\delta}
 \le R^{-q+2\delta}(R/A),
\]

because A,R>=1 and K>=1. This proves (19). Only the actual pointwise multiplicities of norm squares and their integral spacing enter; no average estimate for r_2 is invoked.

## 3.5. Assembly and endpoints

Combining (7)--(9), (12), (16), (18), and (19), and noting that (1+x)^(-K) <= x^(-K) for x>0, gives the explicit unsimplified bound

\[
 \begin{split}
 |F_{T,Y}(R)|\le C_\delta\big[&
 R^{-1/2+2\delta}(1+R/A)
 +A^{-1}R^{-3/2+2\delta}(1+R/A)\\
 &+A^{-2}+R^{-2}A^{-3/2}\big].
 \end{split}
 \tag{23}
\]

The four terms own, respectively, the leading Bessel contribution including both phases; its first correction including both phases; the full Bessel remainder over every nonzero dual vector; and zero frequency. The leading and correction series are absolutely summable by (19), so summing (16) is justified independently of conditional rearrangement.

Since R is comparable to T, 1<=A<=sqrt(T), and T>=2, every term on the right of (23) is

\[
 O_\delta(T^{2\delta}\sqrt T/A).
\]

For example A^(-2)<=1<=sqrt(T)/A, and R^(-1/2)(1+R/A) is bounded by a constant times sqrt(T)/A. Choose delta=min(epsilon/2,1/8). Then 2 delta <= epsilon, proving (1).

All uses of A and R are inequalities or smooth rescalings. Neither parameter is rounded, no discontinuous norm cutoff is introduced, and the proof covers both endpoints of the original range. In particular, Y=T yields O_epsilon(T^epsilon), and Y=T^(2/5) yields O_epsilon(T^(3/10+epsilon)). The rapid decay of Psi was never replaced by a hard cutoff, so there is no omitted primal tail beyond n=T.

# 4. First doubtful or unproved step

No unproved step remains in the stated isolated estimate relative to the permitted basic inputs. The delicate points are explicitly resolved rather than assumed: the sign of the difference phase in (15), the special sine bound (7), the non-summability of a one-term Bessel error, and uniformity of the shifted norm-square grid (20).

This report does **not** prove a power saving beyond (1), a statement for arbitrary coefficients of size r_2(n), or an estimate after replacing the cosine by its absolute value. It does not claim any downstream implication or graph promotion; those are outside the isolated context. Any such extension is an additional, unproved step.

# 5. Required control tests and outcomes

These are exact analytic controls, not floating-point evidence.

1. **Exact dual resonance.** Set R=sqrt(n_0) for any represented norm n_0. The n_0 difference-phase contribution in the leading term is S(0)=0, while the correction contains C_2(0)/(16 pi R^(3/2)), which need not vanish. Outcome: pass. Formula (16) does not incorrectly erase the whole resonant mode or divide by R-sqrt(n_0).

2. **Both phase signs and normalization.** Substitute phi and theta directly into the elementary product formulas: phi-theta=2 pi(R-v)u-pi/2 and phi+theta=2 pi(R+v)u-pi. This gives exactly the two identities (15); combining the angular factor 2 pi with the two coefficients in (14) gives 1 and 1/(16 pi) in (16). Outcome: pass. The leading near phase is sine, not cosine.

3. **Arbitrary real radius and cutoff.** In (20), take x=k+alpha for any integer k and any alpha in [0,1], without changing its constant; A=sqrt(Y) remains any real number >=1 in (5)--(9). Outcome: pass. Integral and nonintegral R^2 and Y have the same bounds.

4. **All large dual indices.** Equation (22) is an explicit bound for the complete infinite tail sqrt(n)>2R; equation (18) sums every Bessel error by a convergent two-dimensional lattice zeta sum. Outcome: pass. A first-term-only expansion would fail this control, which is why it was not used.

5. **Scale separation and both requested endpoints.** The bound for S uses a split at 1/|s| and is independent of B/A; no logarithm of B/A is hidden in its constant. Substitution into (23) gives T^epsilon at Y=T and T^(3/10+epsilon) at Y=T^(2/5). Outcome: pass. Also the zero mode is at most R^(-2)Y^(-3/4) in both cases.

6. **Actual-coefficient and unsigned-surrogate control.** The equality (10) uses one radial Schwartz function summed over the integer lattice, and hence exactly r_2(n). Replacing those multiplicities by arbitrary bounded coefficients removes that equality. Replacing the oscillatory cosine by an absolute value also removes the phase decomposition (15) and the zero-mode integration in (12). Outcome: the proof does not propagate to either surrogate, as required; no artificial coefficient model is substituted for the actual sum.

No computational asymptotic certification is claimed. The controls check structural seams and exact endpoint bounds within the analytic proof.

# 6. Dependencies and exact artifacts used

Local reads, and only local reads:

| Artifact | SHA256 |
| --- | --- |
| `protocol.md` | `F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A` |
| `strategy/round231_balanced_cancellation/briefs/blind_hankel_tail.md` | `2DDFD24DCE000B9DF886CC80A97D9A0642BAE04BAD621D342BE627A234B8A25C` |
| `strategy/round231_balanced_cancellation/briefs/isolated_hankel_statement.md` | `94BC32E3DD2E4E0F060B1385388EBE5CC12932263F9E75F308CB401772F1BC2A` |

Primary references, inspected on 2026-10-11:

- NIST Digital Library of Mathematical Functions, [10.9.1, Bessel's integral](https://dlmf.nist.gov/10.9.E1). Applied only to the real positive argument 2 pi v u to derive the angular Fourier normalization in (11).
- NIST DLMF, [10.17.1](https://dlmf.nist.gov/10.17.E1), [10.17.2](https://dlmf.nist.gov/10.17.E2), and [10.17.3](https://dlmf.nist.gov/10.17.E3), together with [Section 10.17(iii)](https://dlmf.nist.gov/10.17#iii). Specialization: real order nu=0, positive x, ell=1 in each of the even and odd series. The explicit coefficients are a_1(0)=-1/8, a_2(0)=9/128, a_3(0)=-75/1024; the first omitted even and odd terms give (13). No complex-order or unverified uniform-order extension is used.

Poisson for Schwartz functions and r_2(n) <<_delta n^delta are expressly allowed by the isolated statement. All remaining derivative, lattice-grid, tail, and endpoint estimates are derived in Section 3. No graph, campaign state, sibling report, historical round, source-audit file, or outside application was read.

# 7. Recommended state effect

**Promote the isolated analytic lemma (1), subject to the conductor's required seam/source review and valid State Patch.** The original suggested bound needs no correction; the proven range is slightly wider, 1<=Y<=T, and the additive 1 is redundant in this range.

The report is evidence only. It recommends no downstream theorem promotion, does not modify shared state, and does not initiate a subsequent round.

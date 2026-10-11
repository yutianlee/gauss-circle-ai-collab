# Round215 conductor ledger: actual spatial and radius kernel controls

## 1. Result

Campaign:gc-complete-localized-wave-moment. Date:2026-09-28.
Role:conductor analytical control, NONBLIND. Graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

For the actual coefficients in the entire frozen critical band, the
spatial weight does not supply a power saving to either of two complete
absolute Fourier-kernel certificates. Taking absolute values separately
in each radius window costs at least c T N^2. Summing the center phases
first and then taking each complete two-five-tuple kernel in modulus
still costs at least c N^(5/2). The latter exceeds the frozen target on
every fixed interior power scale. These are actual-coefficient lower
bounds on positive upper certificates, never lower bounds on the signed
momentC(T,N), the physical wave, or the circle discrepancy.

The conductor independently derived these facts before receiving the
matching isolated analyst interim. The report is nevertheless NONBLIND
and must receive a final-hash independent seam. All work is analytical.

## 2. Exact hypotheses and definitions

For a self-contained actual-coefficient binding, let T>=2 and
T^(166/325)<N<T^(242/325). Let v be a fixed nonzero nonnegative smooth
real function supported in [1,4]. Let Psi be the fixed real radial
mollifier transform; in particular it is continuous and Psi(0)=1. Set

    c_m=|m|^(-3/2)Psi(|m|/sqrt(T))v(|m|^2/N), m in Z^2\{0},
    F_N(x,R)=sum_m c_m e(x.m+R|m|), e(t)=exp(2pi i t).

The support has sqrt(N)<=|m|<=2sqrt(N). Put a=1/sqrt(2),
d=sqrt(3)-a, J=ceil(dT/sqrt(N)), R_j=aT+j sqrt(N) for 0<=j<=J,
and I=[aT,sqrt(3)T]. Fix real Schwartz functions phi on R^2 and
eta on R with small compact Fourier support and phi(0)=eta(0)=1.
Their moduli are bounded below on [-1,1]^2 and [-1,1], respectively,
as made explicit in the cutoff-normalization clarification. Define

    W(y)=C_A(1+|y|^2)^(-100),
    f_j(y,u)=phi(y/N)eta(u/N)F_N(y/sqrt(N),R_j+u/sqrt(N)),
    C(T,N)=sum_(j=0)^J integral_(R^3) W(y)|f_j(y,u)|^10 dydu.

These are the frozen215 definitions; the explicit formula here does not
enlarge their class. All constants may depend on the fixed functions.
Lower statements hold for sufficiently largeT. For the strict target
failure, fix166/325<alpha<242/325 and putN=T^alpha.

Let a five-tuple M=(m_1,...,m_5)
have weightb_M=product_i c_(m_i), vectorv_M=sum_i m_i and radial
frequencys_M=sum_i |m_i|. Set Δv=v_M-v_Q and Δs=s_M-s_Q. Define

    W_N(y)=W(y)|phi(y/N)|^10,
    A_N(z)=integral_(R^2) W_N(y)e(y.z)dy,
    q(t)=|eta(t)|^10, B(z)=integral_R q(t)e(tz)dt,
    S_J(z)=sum_(j=0)^J e(R_j z).

The two exact positive certificates are

    P_sep=N(J+1) sum_(M,Q) b_M b_Q
                      |A_N(Δv/sqrt(N)) B(sqrt(N)Δs)|,
    P_joint=N sum_(M,Q) b_M b_Q
                      |A_N(Δv/sqrt(N)) B(sqrt(N)Δs)S_J(Δs)|.

Coefficients are nonnegative at the largeT where these lower controls
apply. Exactly C<=P_joint<=P_sep. We prove

    P_sep >= c T N^2,        P_joint >= c N^(5/2).             (1)

No converse inequalityC>=cP is asserted. In particular signs in the
true expansion are not disposed of by saying that C is a moment.

## 3. Proof and normalization

### A. Bind the mass hypotheses to the actual physical coefficients

On the support, |m|/sqrt(T)<=2sqrt(N/T)<=2T^(-83/650).
Continuity andPsi(0)=1 makePsi>=1/2 there for sufficiently largeT,
uniformly throughout the open critical band. Thus c_m>=0 and
c_m<=C N^(-3/4). The annulus containsO(N) integer vectors, giving
sum c_m<=C N^(1/4).

Becausev is nonzero and nonnegative, it is bounded below on a fixed
closed interval strictly inside its support. The corresponding annulus
contains cN+O(sqrt(N)) lattice vectors. To see this without an asymptotic
circle theorem, compare its area with unit squares centered at the
lattice points: only squares meeting either boundary can differ, and
they lie in strips of fixed width and areaO(sqrt(N)). Each retained
coefficient is at least cN^(-3/4). Consequently

    sum_m c_m comparable to N^(1/4),
    sum_M b_M=(sum_m c_m)^5 comparable to N^(5/4).             (2)

This uses every actual lattice representation; no independent divisor
model or average correlation theorem is assumed.

### B. Exact expansion and all window tails

The wave is a finite sum. Expanding its tenth power and applying Fubini
is justified by Schwartz decay of the cutoffs and integrability ofW.
Substituteu=Nt in the radius integral. The exact identity is

    C=N sum_(M,Q) b_M b_Q A_N(Δv/sqrt(N))
                                  B(sqrt(N)Δs)S_J(Δs).     (3)

It is real and nonnegative because it equals the original moment, but
its individual kernels need not be nonnegative. No phase has been erased.

Alternatively, set h(R)=sum_j q((R-R_j)/sqrt(N)). Then exactly

    C=sqrt(N) integral_R h(R)
            integral_(R^2) W_N(y)|F_N(y/sqrt(N),R)|^10 dy dR,
    integral h=(J+1)sqrt(N)integral q comparable to T,
    integral h(R)e(Rz)dR=sqrt(N)B(sqrt(N)z)S_J(z).            (4)

The full realR axis is present. The center grid and all tails remain
in h; neither (3) nor (4) makes a compact-window approximation. Absolute
values at the two stated locations in (3) give exactly P_joint,P_sep.

### C. The spatial Fourier factor is positive in the limiting scale

For A=100, the gamma integral gives

    (1+|y|^2)^(-A)=Gamma(A)^(-1)
              integral_0^infinity t^(A-1)e^(-t)e^(-t|y|^2)dt.

The two-dimensional Fourier transform of the Gaussian is
(pi/t)exp(-pi^2|z|^2/t), for the statede convention. Tonelli/Fubini,
or integrable Gaussian truncation followed by dominated convergence,
shows that the transform ofW is strictly positive and continuous for
every realz. Therefore it has a positive minimum on|z|<=20.

Sincephi is bounded andphi(y/N)->1 pointwise,
||W_N-W||_1->0 by dominated convergence. Hence A_N converges uniformly
to the transform ofW. It follows that, for all sufficiently largeN,

    |A_N(z)|>=c>0 for |z|<=20.                              (5)

No assertion of global positivity for finiteN is needed or made; phi
need not be even, and A_N need not be real. Uniform nonvanishing in
modulus on this compact region suffices. All actual differences satisfy
|Δv|/sqrt(N)<=20, because each vector norm is at most2sqrt(N).

Similarly B(0)=integral q>0, so |B(z)|>=c for |z|<=c_0 by continuity.
No global sign condition onB is assumed.

### D. Separate-window positive certificate

The five-fold radial sums lie in[5sqrt(N),10sqrt(N)]. Partition this
interval intoO(N) bins of width at mostc_0/sqrt(N). LetM_l be the total
weightb_M in binl. Pairs in the same bin satisfy the lower bounds in(5)
and forB. Cauchy--Schwarz and(2) give

    sum_l M_l^2 >= (sum_l M_l)^2/(number of bins)
                           >= c N^(5/2)/N=c N^(3/2).

Keeping just these nonnegative terms inP_sep gives
P_sep>=cN(J+1)N^(3/2). SinceJ+1 comparable toT/sqrt(N), this is
cTN^2. This is a lower bound on the actual positive certificate, not
an inference from a generic coefficient upper bound.

### E. Combine the actual center phases before taking modulus

There is a fixedc_1>0 such that, for |z|<=c_1/T,

    |S_J(z)|>=c(J+1).

Indeed remove the common phasee(R_0z). The remaining arguments have
absolute size at most2pi Jsqrt(N)c_1/T, bounded by a small fixed angle
when c_1 is chosen small; all their real parts are then at least1/2.
The ceiling is harmless becauseJsqrt(N)<=dT+sqrt(N)<=C T.
Also |B(sqrt(N)z)|>=c on this range, as sqrt(N)/T<=1.

Partition the same radial-sum interval intoO(Tsqrt(N)) bins of width
at mostc_1/T. Their squared mass sums to at least
cN^(5/2)/(Tsqrt(N))=cN^2/T. InP_joint this yields

    P_joint>=cN(J+1)N^2/T>=cN^(5/2).

This second bound preserves the exact center sum before the final
modulus. It is therefore stronger as a diagnostic of the proposed use
of window interference than repeating the first bound alone.

### F. Target comparison and physical trace

AtN=T^alpha, the first certificate has target deficit
2alpha-18/65, already242/325 at the lower comparison endpoint.
The second has deficit(5/2)alpha-83/65, strictly positive at every
fixed interioralpha and zero at the excluded lower endpoint166/325.
For any epsilon smaller than that strict deficit, the corresponding
positive certificate cannot beO(T^(83/65+epsilon)). No uniform power
gap is asserted whenalpha approaches the lower endpoint withT.

The spatial Fourier support off_j(.,u) lies in a fixed disk. A fixed
Schwartz reproducing kernelk followed by Holder bounds
|f_j(0,u)|^10 byC integralW(y)|f_j(y,u)|^10dy; chooseC_A large
enough thatW dominates|k|. The cutoffs are bounded below on each
assigned central window at y=0. Since dR=N^(-1/2)du, summing the
cover proves

    integral_I |F_N(0,R)|^10dR <= C N^(-1/2) C(T,N).

Thus the frozen sufficient implication is intact. The certificate
failures do not invalidate that implication or disprove its hypothesis.

## 4. First doubtful or unproved step

The actual signed sum(3), equivalently C(T,N), is not estimated at the
required power. Neither positive certificate can establish the target
on fixed interior scales. The amplitude-dependent envelope method may
retain information before those moduli; this ledger does not decide it.
The complete signed tenth gate and all full-quarter parents remain open.

## 5. Controls and outcomes

- Actual mass and positivity: proved uniformly fromPsi near1 and an
  elementary lattice-annulus count. No enlarged-array counterexample.
- Fourier factors: scalesN andsqrt(N), all centers and full tails retained.
- Spatial factor: uniform lower bound in modulus on the relevant compact
  domain only; no false finiteN/global positivity assertion.
- Both modulus orders: different complete certificates and different
  lower scales explicitly distinguished.
- Real parameters and ceilings: absorbed in uniform bin and window counts.
- Signed distinction: C<=P_joint<=P_sep gives no converse lower bound.
- Endpoint scope: strict failures are fixed-interior statements only.
- Zero experiments; pigeonholing and Fourier identities are analytical.

## 6. Dependencies and exact artifacts

- protocol.md, authoritative graph and frozen215 manifest.
- strategy/round215_complete_localized_wave_attack.md.
- strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md.
- Closed214 harmonic source report and its independent seam for context
  and the already established sufficient trace normalization.

All estimates above are derived here; no new external theorem is imported.
The independent statement-only report receives only the isolated packet.
Its subsequent nonblind seam must not be described as additional blind work.

## 7. Recommended state effect

Retain accepted graph and proof draft. Archive the actual-coefficient
positive-certificate limitations and exact normalization after review.
No signed moment, pointwise exponent or full-goal parent is promoted.

# Conductor: complete-source operator and power control

- Round/campaign: 200 / m9-m1-t1-complete-source-coefficient-mask-analysis.
- Role: independent conductor analysis, candidate evidence only.
- Generated: 2026-09-23.
- Starting raw graph SHA-256: 2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5.
- Context: protocol.md; relevant nodes of state/proof_obligations.yml;
  state/active_campaign.yml; Round-184 and Round-185 durable kernels;
  strategy/gauss_circle_strategy_review_2026-09-23.md.
- Numerical evidence: none.

## 1. Result: lemma or no-go result

The most immediate complete-source bilinear coordinates already have
product coefficients, but their unmasked all-vector operator costs a full
factor R, even with the exact square-root phase. Consequently, the
interval-mask lemma by itself cannot improve this particular interface.
This is a property of the universal operator estimate, not a disproof of
the desired estimate for the actual arithmetic vector.

## 2. Exact statement and hypotheses

Let R be a positive integer and z be finitely supported on Z. Set

\[
 k_R(j)=\mathbf1_{2\mid j}(1-|j|/R)_+,
 \quad (K_Rz)_n=\sum_m k_R(n-m)z_m,
 \quad D=\sum_n|z_n|^2.
\]

For the actual source z_N=c_N exp(2 pi i sigma sqrt(XN)), extended by
zero outside the positive product support, the exact identity is

\[
 \langle z,K_Rz\rangle=D+2\Re C_{\rm even}.
\tag{200.O1}
\]

With inner product conjugate-linear in the first entry, either orientation
of the correlation gives the same real part. The full-line l2 operator norm is

\[
 \|K_R\|_{2\to2}=
 \begin{cases}R/2,&R\text{ even},\\(R+R^{-1})/2,&R\text{ odd}.\end{cases}
\tag{200.O2}
\]

For R=1 this formula gives 1. The off-diagonal correlation vanishes.
For R=2 it also vanishes, with K_R=I. The asymptotic statements below
concern the live large-shell regime R comparable to L.

## 3. Proof or derivation

Pair the terms j and -j to obtain (200.O1). The Fourier multiplier is

\[
 \widehat k_R(\theta)=\tfrac12\{F_R(\theta)+F_R(\theta+1/2)\},
 \qquad F_R(\theta)=R^{-1}\left|\sum_{j=0}^{R-1}e(j\theta)\right|^2.
\]

It is nonnegative. Since all coefficients k_R(j) are nonnegative,
the multiplier attains its maximum at theta=0. Here F_R(0)=R and
F_R(1/2) is zero for even R and 1/R for odd R. This proves the upper
norm and, by continuity or long constant test sequences, its equality.

For a finite interval of M sites, a constant sequence has quotient

\[
 1+2\sum_{0<j<R,\ 2\mid j}(1-j/R)(1-j/M)_+.
\]

For M>=R this equals \(\widehat k_R(0)-O(R^2/M)\).
Thus even restriction to M comparable to L^2 sites with R comparable to L
still has norm comparable to L. This control uses arbitrary vectors solely
to test the proposed all-vector theorem. It does not assert that the
physical c_N is a constant or a phase-conjugated vector.

Multiplication by e(sigma sqrt(XN)) is diagonal unitary on positive
indices (extend it by 1 elsewhere). Conjugation by this unitary leaves
the norm unchanged. In product coordinates (N,N'), the oscillatory factor
e(sigma sqrt(X)(sqrt(N')-sqrt(N))) is exactly a product of a row phase and
a column phase. It cannot create an improved uniform all-vector estimate.

On the actual support |c_N| << X^epsilon by divisor counting and the
literal coefficient bound, and there are O(L^2) sites. Hence D << L^2
X^epsilon after epsilon rebudgeting. The universal bound yields only
|Re C_even| << L^3 X^epsilon. The sufficient target is Re C_even << L^2
X^epsilon. Equivalently the actual-vector quadratic estimate needed is

\[
 \langle c,D_\sigma^* K_{R_0}D_\sigma c\rangle
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil.
\tag{200.O3}
\]

It is enough to prove this upper bound; an absolute bound on each shift
or component is stronger and is not silently required. The connector
E_R <= 2D+4 Re C_even and the O(L) scalar prefactor then give
|sum_N z_N| << L^(3/2) X^epsilon. Using the universal norm instead gives
only L^2 X^epsilon. Thus the full correlation loses L, or L^(1/2) after
scalar reconstruction. The subsidiary high-h block loss Y and the P2
packet loss min(Y,D_L)/(H_B m kappa) belong to different restricted
interfaces and cannot be substituted for this whole-source deficit.

## 4. First doubtful or unproved step

(200.O3) is unproved for the actual c_N. A divisor-coordinate arithmetic
kernel might avoid this all-vector obstruction, but its exact transform,
mixed-amplitude norm, exceptional terms and reconstruction costs have to
be established. No Kloosterman identity or modulus follows from (200.O1).
This analysis does not claim an essential new reduction or exponent gain.

## 5. Control tests and outcomes

- Constant finite vectors reproduce norm comparable to R: analytical
  control only, not an actual-coefficient lower bound.
- Phase conjugation preserves the norm exactly: oscillatory notation
  alone cannot improve the all-vector interface.
- Even/odd R and the R=1,2 endpoints agree with the empty even-shift sum.
- The finite-interval quotient uses (1-j/M)_+, including when R exceeds
  the support length. The O(R^2/M) comparison above is used only for M>=R.
- P_cl+P1+P2=1 before any operator implies exact complete-source
  recombination. It does not make different sector transports identical.
- The full t=1 residual scalar target closes only t=1 when combined with
  the accepted Round-184 XOR sector; all other parents remain protected.

## 6. Dependencies and artifacts used

K184.4--7 define the residual; K185.1--12 give the literal coefficients,
parity connector and diagonal bound. Fourier multiplier and finite-vector
arguments above are elementary and self-contained. No external theorem,
source import, numerical experiment, or subagent report is used here.

## 7. Recommended state effect

Retain open status. Archive this as a quantified interface control, not
as another new rejected proof route or accepted theorem. No graph or proof
draft mutation is justified by this calculation alone.

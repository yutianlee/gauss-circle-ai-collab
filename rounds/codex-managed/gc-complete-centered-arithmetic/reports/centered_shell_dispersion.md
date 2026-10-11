# Round 213: centered shell dispersion with a paid radius transfer

Campaign: `gc-complete-centered-arithmetic`. Task: `centered_shell_dispersion`.
Role: discovery, selected-context, nonblind. Generated: 2026-09-28.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: entirely analytical; zero experiments and
zero external theorem imports. Only this assigned report is written.

## 1. Result: a complete signed radius gate and a centered certificate no-go

The complete actual arithmetic bound remains open. Two precise results
are obtained, with every shift and model term retained.

First, a weaker, averaged arithmetic input suffices after a proved
radius-to-supremum passage. Let `q=2^j`, let `Omega_j` be the complete
product shell `q<Lambda<=2q` inside the residual `Omega`, and set

\[
 Q_j^2=\frac1{T|\Omega_j|}\int_{T/2}^{2T}
              \sum_{(h,k)\in\Omega_j}|E_{h,k}(R)|^2\,dR.
\]

The **unproved signed radius input**

\[
 Q_j\ll_\epsilon T^\epsilon
           \bigl(\sqrt N+Nq^{-3/2}\bigr)
 \quad\text{for every nonempty complete shell}
 \tag{R}
\]

would imply the frozen complete centered target. The actual transfer
cost is `sqrt(q)`, plus an explicit Schwartz tail. Full shell summation
then gives

\[
 \sup_{R\in[T/\sqrt2,\sqrt3T]}
 \frac1{LK}\sum_\Omega|E_{h,k}(R)|
 \ll_\epsilon T^\epsilon
       \left(\sqrt{N\Lambda_*}+\frac N{\Lambda_*}\right)
 \ll_\epsilon T^{166/325+\epsilon}.
 \tag{1}
\]

The first term has upper-band power `159/325`, hence `7/325` margin;
the second has power at most `166/325`. The enlarged radius interval
is essential to the stated proof. No free mean-to-supremum passage is
used. Input (R) can equivalently be stated for the uncentered `D`, with
the same harmless `Nq^(-3/2)` allowance: the smooth model is rapidly
decaying on this enlarged interval. This equivalence supplies no
arithmetic cancellation.

Second, there is a scoped **centered** no-go beyond the uncentered test
in Round 212. Replace only the discrete-discrete radius kernel by its
modulus, while keeping the exact signed mixed and continuous-continuous
model terms. This nonnegative upper certificate still costs at least
`N/sqrt(Lambda_*)`. Moreover, after the proved bandwidth transfer, its
complete shell certificate costs at least `cN` on every fixed interior
power scale. Thus exact model cross terms cannot rescue this specified
absolute discrete-discrete mechanism. These are lower bounds on
certificates, not on the signed energy, the centered target, or the
circle discrepancy.

## 2. Exact statements and hypotheses

Use the frozen real parameters and exact integer cutoffs:

\[
 b=83/650,\quad T\ge2,\quad T^{166/325}<N<T^{242/325},
\]
\[
 L=\max(2,\lceil\sqrt N T^{-2b}\rceil),\qquad
 K=\max(2,\lceil NT^{-4b}\rceil).
\]

The actual fixed real smooth masks give

\[
 g(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\quad
 W(t)=g(t)g(t+h)g(t+k)g(t+h+k),
\]
\[
 \psi(t)=\sqrt{t+h+k}-\sqrt{t+k}-\sqrt{t+h}+\sqrt t,
\]
\[
 a(n)=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k).
\]

Here and below suppressed subscripts are always the same ordered pair
`(h,k)`. All functions and sequences are zero extended from their
actual overlap `[N,4N-h-k]`; internal zeros and mask signs remain.
The inherited smooth bounds are `W^(r)=O_r(N^(-r))` with compact smooth
support. The actual divisor envelope gives `a(n)<<T^epsilon`.
For distinct shifts use exactly the constructed candidate

\[
 \rho=\rho^{\rm loc}_{h,k}
   =\pi^4\prod_p\int_{\mathbb Z_p}
       \prod_{s\in(0,h,k,h+k)}\lambda_p(x+s)\,dx,
 \qquad 0\le\rho\ll_\epsilon T^\epsilon.
\]

No integer mean property of this product is assumed. Define

\[
 D(R)=\sum_n a(n)W(n)e(R\psi(n)),\quad
 I(R)=\int W(t)e(R\psi(t))\,dt,\quad E=D-\rho I.
 \tag{2}
\]

Put `U=N^(3/2)/T`, `Lambda=hk/U`, `Lambda_*=LK/U`, and

\[
 \Omega=\{1\le h<L,\ 1\le k<K:\ h\ne k,\ \Lambda>1\},
\quad
 \Omega_j=\{(h,k)\in\Omega:2^j<\Lambda\le2^{j+1}\}.
\]

Empty shells are omitted; `m_j=|Omega_j|`, `delta_j=m_j/(LK)`, and
`q=2^j`. In particular powers of two occur in exactly one shell.
The exact ceilings imply, uniformly even with bounded cutoffs,

\[
 LK\asymp N^{3/2}T^{-6b},\qquad
 \Lambda_*\asymp T^{76/325},\quad
 \delta_j\ll\min\left(1,\frac{q\log(2L)}{\Lambda_*}\right),
 \quad\sum_j\delta_j\le1.
 \tag{3}
\]

Write `I_0=[T/sqrt(2),sqrt(3)T]` and `J=[T/2,2T]`. For a vector
indexed by a shell, its Hilbert norm is the normalized Euclidean norm
`||z||_j^2=m_j^(-1)sum|z_(h,k)|^2`. Thus
`Q_j^2=T^(-1)integral_J ||E(R)||_j^2 dR`.

All upper and conditional bounds are uniform throughout the open band
and for real endpoints. The certificate lower bounds use each fixed
interior scale `N asymp T^alpha`, `166/325<alpha<242/325`. They are not
claimed uniformly as `alpha` approaches the lower endpoint with `T`.

## 3. Proof and derivation

### 3.1 The exact centered energy, including all three types of term

At a fixed real `R`, direct expansion of (2) gives

\[
\begin{split}
 |E(R)|^2={}&\sum_{n,m}a(n)a(m)W(n)W(m)
                  e(R[\psi(n)-\psi(m)])\\
 &-2\rho\Re\sum_n a(n)W(n)\int W(t)
                  e(R[\psi(n)-\psi(t)])\,dt\\
 &+\rho^2\iint W(t)W(u)e(R[\psi(t)-\psi(u)])\,dt\,du.
\end{split}
 \tag{4}
\]

The double discrete term contains all eight actual `r2` factors.
Neither its off-diagonal nor either integral is deleted. In particular
the mixed term is not a sum over a fictitious continuous arithmetic
coefficient.

Let

\[
 \mathcal K(y)=\int_{1/2}^{2}e(vy)\,dv.
\]

Define `X_(h,k),Y_(h,k),Z_(h,k)` by replacing the exponential in the
three lines of (4), respectively, by
`K(T[psi(first)-psi(second)])`, without the exterior coefficients
`-2rho Re` and `rho^2`. Equivalently,

\[
 X=\frac1T\int_J|D|^2,\qquad
 Y=\frac1T\int_JD\overline I,\qquad
 Z=\frac1T\int_J|I|^2\ge0.
\]

The signed radius energy is exactly

\[
 Q_j^2=\frac1{m_j}\sum_{\Omega_j}
                 (X-2\rho\Re Y+\rho^2 Z).
 \tag{5}
\]

The discrete diagonal in `X` equals
`(3/2)sum_n a(n)^2 W(n)^2<<N T^epsilon`. Thus a sufficient explicit
arithmetic form of (R) is the **one-sided signed** bound

\[
 \frac1{m_j}\sum_{\Omega_j}
   \bigl(X^{\rm off}-2\rho\Re Y+\rho^2Z\bigr)
 \ll_\epsilon T^\epsilon(N+N^2q^{-3}).
 \tag{6}
\]

The left side is real, by conjugate pairing. Its negative mixed term
is retained exactly, and it is not bounded by summing absolute values
of individual kernel or divisor contributions. Formula (6) is an
unproved arithmetic hypothesis, not a consequence of its expansion.

### 3.2 Frequency support and the paid supremum transfer

The exact second-difference formula is

\[
 \psi(t)=-\frac14\int_0^h\int_0^k
                         (t+u+v)^{-3/2}\,dv\,du.
 \tag{7}
\]

Whenever `W(t)` is nonzero, all four arguments lie in `[N,4N]`.
Consequently

\[
 -\frac{hk}{4N^{3/2}}\le\psi(t)
       \le-\frac{hk}{32N^{3/2}}.
\]

On shell `q<Lambda<=2q`, the exact `R`-frequency support of `E` is
therefore contained in `[-q/(2T),-q/(32T)]`, a width `O(q/T)` interval.
This assertion holds for the discrete and continuous parts together:
`E` is the Fourier transform of the pushforward under `psi` of

\[
 d\mu(t)=\sum_n a(n)W(n)\,\delta_n(dt)-\rho W(t)\,dt.
\]

Its total variation is `O_epsilon(N T^epsilon)`. Thus
`|E(R)|<<N T^epsilon` for **every** real `R`, including outside `J`.
This global envelope is used only for the explicit tail below.

Choose a fixed Schwartz function `kappa` whose Fourier transform is
one on `[-1,1]` and has compact support in `[-2,2]`. With convention
`hat kappa(xi)=integral kappa(x)e(-x xi)dx`, put

\[
 K_q(x)=\frac qT\kappa(qx/T).
\]

The frequency inclusion proves the exact identity `E=K_q*E`, coordinate
by coordinate. Finite spectral variation and integrability of `K_q`
justify exchanging the integrals; no global square integrability of
`E` is asserted.

For `R in I_0`, split the convolution at `s in J`. Hilbert-space
Cauchy on the inner part gives

\[
 \left\|\int_JK_q(R-s)E(s)\,ds\right\|_j
 \le\|K_q\|_2\left(\int_J\|E(s)\|_j^2ds\right)^{1/2}
 \ll\sqrt q\,Q_j.
\]

The distance from `I_0` to the complement of `J` is at least
`dT`, where `d=min(1/sqrt(2)-1/2,2-sqrt(3))>0`. Schwartz decay and
the global envelope therefore give, for every fixed `B>0`,

\[
 \sup_{R\in I_0}\|E(R)\|_j
 \ll \sqrt q\,Q_j+C_{B,\epsilon}NT^\epsilon q^{-B}.
 \tag{8}
\]

This is the full radius-to-supremum cost. A mean square on an interior
subinterval or against a weight vanishing near a required endpoint
would not supply the displayed `Q_j` without another argument.

### 3.3 All product-shell weights and every restored power

Cauchy within a complete shell, followed by (8), gives

\[
 \sup_{I_0}\frac1{LK}\sum_\Omega|E(R)|
 \ll\sum_j\delta_j\sqrt q\,Q_j
       +C_{B,\epsilon}NT^\epsilon\sum_j\delta_jq^{-B}.
 \tag{9}
\]

For `B>1`, (3) bounds the tail sum by
`O(log(2L)/Lambda_*)`. Under (R),

\[
 \sum_j\delta_j\sqrt q\,Q_j
 \ll_\epsilon T^\epsilon\left(
       \sqrt N\sum_j\delta_j\sqrt q+
       N\sum_j\delta_j/q\right)
 \ll_\epsilon T^\epsilon
       (\sqrt{N\Lambda_*}+N/\Lambda_*).
 \tag{10}
\]

The final sum uses the full shell density; its logarithms are absorbed
by smaller initial epsilon budgets. One unrestricted Cauchy across
all shifts could lose this price for the small-product end.
The exact powers are

\[
 \sqrt{N\Lambda_*}\le C T^{(242+76)/(2\cdot325)}
                  =C T^{159/325},\qquad
 N/\Lambda_*\le C T^{(242-76)/325}=C T^{166/325}.
\]

The already paid sectors `h=k` and `hk<=U` cost respectively
`T^epsilon N/K` and `T^epsilon N U log(2L)/(LK)`, both at most
`T^(166/325+epsilon)`. The full smooth model contribution has the
same safe price, proved next. Thus no discarded sector is implicit
in (1). This would yield only the inherited fixed-parameter
`102/325` milestone, not the quarter theorem.

### 3.4 What smooth scalar centering can and cannot change

On the enlarged positive interval `J`, differentiating (7) gives
`|(R psi)'(t)| asymp Lambda/N` on support; the normalized higher
derivatives have the usual corresponding bounds. Repeated integration
by parts with the compact smooth amplitude therefore gives, uniformly
for every fixed `A`,

\[
 \sup_{R\in J}|\rho I(R)|
       \ll_{A,\epsilon}T^\epsilon Nq^{-A}.
 \tag{11}
\]

All exterior boundary terms vanish because the actual smooth masks
are zero extended; the same argument works across internal zeros.
No real endpoint is replaced by an integer endpoint in the integral.

Writing `Q_j(D)` for the radius norm with `D` in place of `E`, Minkowski
and (11) give the two-sided displacement estimate

\[
 |Q_j(D)-Q_j(E)|\ll_{A,\epsilon}T^\epsilon Nq^{-A}.
 \tag{12}
\]

Hence (R) is equivalent for `D` and `E`, with changed constants and
epsilon budgets. Its allowance `Nq^(-3/2)` pays the smooth term.
In the exact squared expansion, the elementary bounds also give

\[
 |\rho Y|\ll_{A,\epsilon}N^2T^\epsilon q^{-A},\qquad
 0\le\rho^2Z\ll_{A,\epsilon}N^2T^\epsilon q^{-2A}.
 \tag{13}
\]

Thus the mixed and continuous terms are indeed present, but on large
product shells they cannot supply a polynomial reduction in a large
discrete-discrete radius norm by themselves. The full model `L1` cost
is `O_epsilon(T^epsilon N/Lambda_*)` by (3) and (11), including its
small-product continuation as recorded in the prior synthesis. This
is a cost estimate and norm equivalence, not evidence that the local
candidate is the true arithmetic mean.

### 3.5 A centered certificate still fails when only DD is absolutized

For each pair set

\[
 B_n=|a(n)W(n)|,\quad M=\sum_nB_n,\quad
 G=\sum_{n,m}B_nB_m
       |\mathcal K(T[\psi(n)-\psi(m)])|.
\]

Now retain the model terms exactly and define the **specified centered
upper certificate**

\[
 C_{h,k}=G-2\rho\Re Y+\rho^2 Z.
 \tag{14}
\]

Because `G>=X`, (5) gives
`C=(G-X)+T^(-1)integral_J|E|^2>=0`. Thus this certificate is valid
even though the mixed term is signed. It is not the total variation
of a centered discrete sequence and not an assumption that its
mixed term has a favorable sign.

The continuity of `K` and `K(0)=3/2` give a fixed neighborhood of zero
on which `|K|` is bounded below. Since

\[
 |\psi'(t)|\ll hkN^{-5/2},
\]

partitioning the full overlap into `O(1+Lambda)` real consecutive
bins of length at most `cN/(1+Lambda)` gives

\[
 G\ge c\sum_{\rm bins}\left(\sum_{n\text{ in bin}}B_n\right)^2
   \ge c\frac{M^2}{1+\Lambda}.
 \tag{15}
\]

The inherited actual-mass lemma in the permitted Round-212
oscillatory report proves `sum_Omega M>=cLKN` at each fixed interior
power scale, using the elementary circle first moment and two finite
moving-sum inequalities. It assumes no four-point mean.

Choose a fixed `eta` with `0<eta<76/325` and restrict temporarily to
shells `q>=q_0=T^eta`. Removing all smaller shells removes at most
`O(q_0 U log(2L))` pairs. Their actual absolute mass is at most
`O_epsilon(N T^epsilon q_0 U log(2L))=o(LKN)`, after choosing
epsilon small enough. Thus

\[
 \sum_{\Omega:\,q\ge q_0}M\ge cLKN.
 \tag{16}
\]

This restriction is used only to prove a lower bound for a positive
certificate; it is not a deletion in the upper target.
Equations (13)--(14) and `C>=0` imply

\[
 \sqrt C\ge\sqrt G-C_{A,\epsilon}NT^\epsilon q^{-A/2}.
 \tag{17}
\]

With sufficiently large fixed `A`, (15)--(17) first give

\[
 \frac1{LK}\sum_\Omega\sqrt C
       \gg N/\sqrt{\Lambda_*}
       \asymp NT^{-38/325}.
 \tag{18}
\]

The correction over `q>=q_0` is negligible after choosing
`A eta/2>38/325` with room for epsilon. This already exceeds the
target at fixed `alpha>204/325`, now with the mixed and continuous
terms retained exactly.

More strongly, the shell certificate actually supplied to (9) is

\[
 \mathcal P_{\rm band}
 =\sum_j\delta_j\sqrt q
           \left(\frac1{m_j}\sum_{\Omega_j}C_{h,k}\right)^{1/2}.
\]

Concavity of the square root, followed by (15), gives

\[
 \mathcal P_{\rm band}
 \ge\frac1{LK}\sum_{\Omega:\,q\ge q_0}\sqrt q\sqrt C
 \ge\frac c{LK}\sum_{\Omega:\,q\ge q_0}M
       -C_{A,\epsilon}NT^\epsilon q_0^{-(A-1)/2}
 \gg N.
 \tag{19}
\]

Here `q<Lambda<=2q` makes `sqrt(q/(1+Lambda))` bounded below.
Choose `A>1` sufficiently large to make the displayed correction
`o(N)`. Consequently this fully priced, partially signed centered
certificate exceeds the target by the fixed power
`alpha-166/325` everywhere on the fixed interior band. Its supremal
upper-edge deficit is `76/325`; the open endpoint is not attained.

The defect is specific: taking the absolute value of the DD kernel
loses the cancellation required by (6). Treating the model terms
exactly does not repair that loss. Equation (19) is not a lower bound
for the true signed radius energy or for the left side of (1).

## 4. First doubtful or unproved step

The first missing arithmetic assertion is (R), equivalently the
sufficient signed bound (6), on the enlarged radius interval `J`
for every complete shell and the entire real parameter band. The
proofs of the bandwidth lemma, shell prices, smooth-model estimates,
and scoped certificate obstruction do not establish it.

The actual diagonal is `O(N T^epsilon)`, but this fact does not bound
the signed eight-factor off-diagonal. The candidate density is bounded
and locally constructed; it is not an established integer mean. There
is no independent-character, independent-shift, or local-discrepancy
assumption hidden in (6). An estimate for a signed total over all
shifts is also insufficient for the separate complete shell norms.

Input (R) is a genuinely weaker sufficient target than requiring a
diagonal-sized fixed-radius shell energy, because its radius bandwidth
loss is explicitly affordable. It remains an input, not a theorem.
The no-go (19) rejects only its specified absolute-DD certificate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_four_point_coefficients` | Passed in all identities and certificate lemmas. The exact four `r2` factors, and eight factors in DD, remain. Actual surviving mass is used, not a surrogate coefficient vector. |
| `complete_shifts_overlap` | Passed. Every residual pair lies in one shell; repeated and small-product sectors have their inherited complete prices. All support overlaps, internal zeros and mask signs remain. The high-shell restriction is only a positive-certificate lower-bound device. |
| `local_global_discrepancy` | No discrepancy theorem is presumed. The binning in (15) proves only a certificate lower bound. The radius hypothesis controls complete shell energies, with its exact interval and norm stated. |
| `density_hypotheses` | Only the established nonnegativity and `T^epsilon` bound of the candidate product are used. No true-mean identification, short-interval asymptotic or density replacement is inferred. |
| `real_endpoints` | Passed. The cutoff comparisons include bounded exact ceilings. The masks and all sums retain real support conventions. The positive distance between `I_0` and the boundary of `J` explicitly pays convolution tails. |
| `all_restored_powers` | Passed. Shell fractions, exact frequency width, `sqrt(q)` passage, tails, smooth integrals, paid sectors, exponents `159/325` and `166/325`, and certificate deficits are displayed. |
| `signed_absolute_distinction` | Passed. (4)--(6) keep DD, mixed and CC signs. Only (14) replaces DD's Fourier kernel by its modulus. Its nonnegativity and the scope of its lower bounds are proved. |
| `full_quarter_scope` | Passed. Even (R) would provide only the frozen `102/325` milestone. No moment, M1, M2, endpoint parent, GAR complement, tenth gate or quarter theorem is promoted. |
| `statement_only_control` | Not claimed by this selected-context discovery report. No sibling, blind packet or blind report was opened. The conductor must route the important transfer and centered-certificate seams independently. |

Additional analytical controls: on the known congruence-zero sector,
both `a` and `rho` vanish, hence all displayed terms vanish. The
repeated sector is excluded from the distinct-density definition and
paid directly. Arbitrary mask signs are carried through (4), and only
the deliberately positive `G` uses absolute coefficients. The global
spectral envelope, not an unjustified global `L2` integral, controls
the reproducing-kernel tails. No numerical test was run.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its listed context were read. The graph
was inspected at its authority preamble and the relevant nodes
`GC-target`, `M9-M1`, `M9-M2`, and
`GC-complete-square-root-large-values-moment-bound`. Paths cited inside
those artifacts were not opened. No external source is a dependency.

| Artifact | SHA-256 at inspection |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71` |
| `state/active_campaign.yml` | `b5affd6815848adda7748b40be7bf0e20c09c814db65851cba564370c1953b3b` |
| `strategy/round213_complete_centered_arithmetic_attack.md` | `d81a7690d27968f1843b4a2d3efb6c6b8b4cc483f83ff56e910c3d27acf89aae` |
| `rounds/codex-managed/gc-complete-four-point-correlation/synthesis.md` | `5ae97f52664c3da3c938031785bd743e820956b49810e82e0e7a1ab1056a780b` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_local_arithmetic.md` | `6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md` | `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f` |
| `rounds/codex-managed/gc-complete-centered-arithmetic/briefs/centered_shell_dispersion.md` | `65f247a295031fc62b693d3d0cc088f0b3d4ae84529e1c63363406df64341303` |

The local-arithmetic report supplies the candidate density size and
actual congruence control. The prior oscillatory report supplies the
reviewed complete sector prices, shell counts and actual residual
absolute-mass lemma used in (16). Its mass proof was inspected; its
uncentered no-go was not silently applied to `E`. Equations (4)--(19)
derive the new centered treatment, enlarged-window transfer, relaxed
radius gate and fully priced centered certificate obstruction here.
The prior synthesis supplies only the stated conditional milestone
and unresolved full-goal scope. No external theorem audit was needed.

## 7. Recommended state effect

**Retain**, after independent seam review, the complete paid transfer
(8)--(10), the precise signed arithmetic gate (6)/(R), and the centered
absolute-DD certificate no-go (14)--(19). **Reject** any claim that
exact scalar-model cross terms alone rescue this specified positive
DD transport. **No change** to accepted arithmetic estimates, moments,
exponents, M1/M2 parents, endpoint obligations or the proof draft.

The arithmetic exit remains `complete_signed_remainder_still_open`,
with an additional `scoped_centered_certificate_obstruction`. An
identity or the conditional gate must not be promoted as a saving.
No shared-state, synthesis, validation, legacy, sibling or successor
file is edited. This bounded task stops after the report.

# Round 30 discovery report: beta log kernel at the two signed saddles

## 1. Result

The finite-section logarithm is not the term that threatens the accepted local
\(q^{-2}\) power. On the separated post-endpoint \(R_1\) branch, the exact
identity
\[
A=\rho _0-i\alpha,\qquad y=L-\nu,\qquad
{1\over y(A+iy/2)}
={1\over A\,y}-{i\over 2A(A+iy/2)}
\tag{1.1}
\]
shows that the coefficient of the only genuine face logarithm is
\(f_b(L)/A\). At either saddle \(\alpha=\pm\lambda\), and when the face
\(L=\pm V\) coalesces with that saddle, this coefficient is
\(O_b(\lambda^{-4})\), not \(O_b(\lambda^{-2})\). In the normalized
Round-27 ledger its contribution is therefore
\[
{D_j\over q}\lambda\,
O_b\!\left(\lambda^{-4}\log(2+\lambda)\right)
=
O_b\!\left(
{D_j\log(2+\lambda)\over q^4\theta_j(x)^3}
\right),
\qquad \lambda=q\theta_j(x).
\tag{1.2}
\]
Thus the logarithmic face term has local \(q^{-4}\), up to one necessary
logarithm.

The \(q^{-2}\) term is instead the regular finite part left after (1.1). If
that finite part has the scale-normalized BV bound stated in Section 2, its
ordinary two-saddle Fresnel estimate gives
\[
{D_j\over q}\lambda\,O_b(\lambda^{-2})
=
O_b\!\left({D_j\over q^2\theta_j(x)}\right).
\tag{1.3}
\]
Both signs have the same magnitude. The positive saddle has Hessian
\(+1/\lambda\), and the negative saddle has Hessian \(-1/\lambda\).

I prove below a uniform moving-logarithm Fresnel lemma, including
saddle-face and saddle-endpoint coalescence. It loses at most
\(\log(2+\lambda)\), and this loss is sharp. I also give an exact
polytope/Plemelj decomposition. These results settle the singular kernel
locally. They do **not** prove the complete beta theorem: the first
unproved actual-profile statement is the required uniform, scaled BV bound
for the regular finite part of the fully recombined numerator. The named
artifacts contain a fixed-\(b\) size estimate but not this moving-boundary
variation estimate. Height exhaustion, finite outside sides, and the
complete \(h,D_j,x\), radial, floor/star, and profile sums remain downstream
open seams.

## 2. Exact statement and hypotheses

Put
\[
I_{U,V}(L)=[-V,V]\cap[L-U,L+U],
\quad
A(L)=\max(-U,L-V),\quad B(L)=\min(U,L+V),
\tag{2.1}
\]
and write \(\mu=L-\nu\). For a finite box, define the distribution-first
kernel
\[
{\cal C}_{U,V}H(L)
=
\pi{\bf1}_{|L|<V}H(L,L)
-i\,\operatorname {PV}\!\int_{I_{U,V}(L)}
{H(L,\nu)\over L-\nu}\,d\nu .
\tag{2.2}
\]
Endpoint values of the indicator are immaterial for integration.

### Lemma 2.1 (exact finite-section decomposition)

Let \(h_0(L)=H(L,L)\), and define, with continuous extension at \(\mu=0\),
\[
\Delta_H(L,\mu)
={H(L,L-\mu)-H(L,L)\over\mu}.
\tag{2.3}
\]
Then, whenever the displayed quantities exist,
\[
{\cal C}_{U,V}H(L)=h_0(L)J_{U,V}(L)+R_{U,V}(L),
\tag{2.4}
\]
where
\[
J_{U,V}(L)
=
\pi{\bf1}_{A(L)<0<B(L)}
-i\log { |B(L)|\over |A(L)|},
\qquad
R_{U,V}(L)=-i\int_{A(L)}^{B(L)}\Delta_H(L,\mu)\,d\mu .
\tag{2.5}
\]
The logarithm in (2.5) is interpreted by the one-sided limit at a zero
endpoint. Formula (2.4), rather than either term separately at the face, is
the finite-section boundary value.

The only pole-face logarithms occur at \(L=\pm V\). The faces
\(|L-\nu|=U\) only switch the affine endpoint formulas or terminate the
section; the section collapses at \(L=\pm(U+V)\). Uniformly in \(U\),
\[
|\,\Im J_{U,V}(L)\,|
\leq
C\left[
1+\log\!\left(1+{|L|+V\over ||L|-V|}
\right)\right]
\tag{2.6}
\]
away from \(L=\pm V\), with the evident limiting interpretation. In
particular, if a face meets a saddle with \(|L|\asymp V\asymp\lambda\),
the singular part is a smooth coefficient times
\(\log(\lambda/|L\mp V|)\). There is no independent \(\log U\) loss.

For the regular term, a sufficient exact hypothesis is
\[
\begin{split}
{\mathfrak B}(H;U,V;{\cal P})
:={}&
\sup_{L\in{\cal P}}\int_{A(L)}^{B(L)}
\bigl(|\Delta_H(L,\mu)|
      +|\partial_L\Delta_H(L,\mu)|\bigr)\,d\mu\\
&+
\sum_{\gamma=A,B}
\int_{\cal P}
|\Delta_H(L,\gamma(L))|\,dL <\infty ,
\end{split}
\tag{2.7}
\]
where the endpoint traces are taken only on the finitely many affine pieces
on which they exist. Then \(R_{U,V}\) is BV on \({\cal P}\), with
\[
\|R_{U,V}\|_\infty+\operatorname {Var}_{\cal P}R_{U,V}
\ll {\mathfrak B}(H;U,V;{\cal P}).
\tag{2.8}
\]

### Lemma 2.2 (moving-logarithm Fresnel bound)

Let \({\cal P}\) be a fixed compact interval. Suppose
\(\phi\in C^3({\cal P})\) has at most one critical point \(s\) in a fixed
enlargement of \({\cal P}\), that the critical point is nondegenerate, and
that, uniformly on the patch,
\[
|\phi'(t)|\asymp |t-s|,\qquad
0<c\leq|\phi''(s)|\leq C,\qquad
\|\phi\|_{C^3}\leq C.
\tag{2.9}
\]
Let \(g\in W^{1,1}({\cal P})\), \(\Lambda\geq2\), \(0<a\leq1\), and
\(1\leq\tau\leq\Lambda^M\) for fixed \(M\). For every subinterval
\({\cal Q}\subseteq{\cal P}\) and every moving point \(t_0\) in a fixed
enlargement of \({\cal P}\),
\[
\left|
\int_{\cal Q}g(t)\Log(a+i\tau(t-t_0))
e^{\,\pm i\Lambda\phi(t)}\,dt
\right|
\leq
C_M\Lambda^{-1/2}\log(2+\Lambda)
\bigl(\|g\|_\infty+\|g'\|_1\bigr).
\tag{2.10}
\]
The constant is uniform when \(t_0\) crosses \(s\) or an endpoint of
\({\cal Q}\), and for either Hessian sign. If \(t_0\) is allowed to move
arbitrarily far away, (2.10) must instead contain
\(\log(2+\tau\operatorname {dist}(t_0,{\cal P}))\); the unrestricted
version with a constant independent of \(t_0\) is false.

The same estimate applies after an exact Morse change of coordinate to a
factor \(\Log(a+i\tau(L(t)-L_0))\), because
\[
\log|L(t)-L_0|
=
\log|t-t_0|
+
\log\left|{L(t)-L(t_0)\over t-t_0}\right|
\tag{2.11}
\]
and the second term is a uniformly smooth amplitude. A Heaviside delta
trace is handled by splitting the interval and costs only the ordinary
\(O(\Lambda^{-1/2})\) Fresnel bound.

### Corollary 2.3 (conditional separated-\(R_1\) two-saddle estimate)

On a fixed-\(b>0\), post-endpoint separated \(R_1\) patch, assume the exact
local factor is
\[
H(L,\nu)={f_b(\nu)\over
\rho_0-i(\nu+\alpha+\beta)/2},
\qquad L=\alpha-\beta,
\tag{2.12}
\]
with \(|\rho_0|\) separated from its residue seam as required by that patch.
Assume, uniformly for \(|\alpha|\asymp\lambda\geq2\),
\[
f_b(L)=O_b(\lambda^{-3}),\qquad
|A|=|\rho_0-i\alpha|\asymp\lambda,
\tag{2.13}
\]
and that the regular part in (3.10) below has scale-normalized BV
\(O_b(\lambda^{-2})\), uniformly for the exact moving endpoints (2.1).
Then the complete finite-section kernel at each of
\(\alpha=\pm\lambda\) obeys the local normalized ledger (1.2)--(1.3).
The assertion is uniform when a \(v\)-face or an integration endpoint meets
either saddle.

This corollary is deliberately local. It does not assume or assert that
the fully recombined
\(\omega G+(1-\omega)R_1-\omega E_1\), connector terms, axial terms, or
all height tails satisfy (2.7).

## 3. Proof and derivation

### 3.1 Distribution first and the exact polytope

For \(a>0\), the physical top variable gives
\[
\int_{-V}^{V}\int_{-U}^{U}
{F(\mu,\nu)\over a+i\mu}\,d\mu\,d\nu.
\tag{3.1}
\]
Taking this finite-box limit in \(\mu\) first gives
\[
\pi\int_{-V}^{V}F(0,\nu)\,d\nu
-i\int_{-V}^{V}\operatorname {PV}
\int_{-U}^{U}{F(\mu,\nu)\over\mu}\,d\mu\,d\nu .
\tag{3.2}
\]
With \(L=\mu+\nu\), a fixed \(L\) section is exactly (2.1). Replacing
\(\nu=L-\mu\) in (2.2), adding and subtracting \(H(L,L)\), and using
\[
\operatorname {PV}\int_A^B{d\mu\over\mu}
=\log {|B|\over|A|}
\tag{3.3}
\]
proves (2.4)--(2.5), including the sign
\(\pi-i\,\mathrm{PV}\). Thus the delta and logarithm are two boundary
values of the same Plemelj object and must not be estimated in an order
that separates absolute values before the distributional limit.

The formulas for \(A,B\) are maxima/minima of affine functions. Their only
zeros inside a nonempty section are \(A(V)=0\) and \(B(-V)=0\). Switching
between a top face and a \(v\)-face introduces a kink but no pole. The
section is empty beyond \(|L|=U+V\). Direct comparison of the two
distances from the pole gives, for \(|L|<V\),
\[
{ \min(U,V+L)\over \min(U,V-L)}
\quad\hbox{and its reciprocal}
\ \leq\ {V+|L|\over V-|L|};
\tag{3.4}
\]
for \(L>V\), the nonempty section has
\[
1\leq{B(L)\over A(L)}
\leq {L+V\over L-V},
\tag{3.5}
\]
and \(L<-V\) is symmetric. This proves (2.6). Differentiating the
integral defining \(R\) on every affine endpoint piece and summing its
boundary traces proves (2.8). This is a BV statement about the integral,
not the false pointwise \(C^2\) statement for the full face amplitude.

### 3.2 Moving logarithm through a saddle

The exact Morse lemma reduces a nondegenerate patch to
\(\phi(t)=\phi(s)+\varepsilon(t-s)^2/2\),
\(\varepsilon=\pm1\), with a uniformly \(C^2\) diffeomorphism. The
Jacobian is absorbed into \(g\). Put \(r=\Lambda^{-1/2}\). On
\(|t-s|\leq Cr\), absolute integration and local integrability of the
logarithm give
\[
\int_{|t-s|\leq Cr}
|\Log(a+i\tau(t-t_0))|\,dt
\ll r\log(2+\Lambda+\tau),
\tag{3.6}
\]
uniformly in \(a\downarrow0\) and when \(t_0=s\) or is at an endpoint.

Decompose the complement into shells
\(R\leq|t-s|\leq2R\), \(R=2^kr\). If the shell does not meet \(t_0\),
one integration by parts with
\((i\Lambda\phi')^{-1}d/dt\) gives
\[
O\!\left({\log(2+\Lambda+\tau)\over\Lambda R}\right)
(\|g\|_\infty+\|g'\|_1).
\tag{3.7}
\]
If it meets \(t_0\), remove
\(|t-t_0|\leq\delta=(\Lambda R)^{-1}\). The removed interval is bounded
absolutely by
\[
O\!\left({\log(2+\Lambda+\tau)\over\Lambda R}\right).
\tag{3.8}
\]
On the two remaining pieces, integration by parts is legitimate; integrating
\(|d\Log(a+i\tau(t-t_0))/dt|\) only from \(\delta\), rather than through
the singular point, gives the same bound with the displayed logarithm.
The geometric sum of (3.7)--(3.8) is dominated by the first shell and is
\(O(\Lambda^{-1/2}\log(2+\Lambda))\). Restricting to a moving subinterval
only creates boundary terms of this size. This proves (2.10) for both
signs and all saddle/face/endpoint incidences.

The logarithm cannot in general be removed: for
\(\phi(t)=t^2/2\), \(t_0=0\), and \(g(0)\ne0\), the substitution
\(u=\sqrt{\Lambda}\,t\) contains
\[
-{1\over2}\Lambda^{-1/2}\log\Lambda
\int e^{iu^2/2}g(0)\,du
\tag{3.9}
\]
in its leading local term. Hence one logarithm is the correct uniform
price when its coefficient does not vanish.

### 3.3 The actual separated profile and the two saddles

For (2.12), set \(y=L-\nu\). Since
\(\nu+\alpha+\beta=2\alpha-y\), its denominator is
\(A+iy/2\), where \(A=\rho_0-i\alpha\). Identity (1.1) is verified by
putting the right side over the common denominator. Consequently
\[
{f_b(L-y)\over y(A+iy/2)}
=
{f_b(L)\over A\,y}
-{i f_b(L)\over2A(A+iy/2)}
+{f_b(L-y)-f_b(L)\over y(A+iy/2)} .
\tag{3.10}
\]
The first term, together with the delta trace, is exactly
\((f_b(L)/A)J_{U,V}(L)\). The final two terms are regular at \(y=0\);
their integral is the finite part whose moving-endpoint BV norm is required
in Corollary 2.3.

At a face-saddle incidence, (2.13) gives
\[
{f_b(L)\over A}=O_b(\lambda^{-4}).
\tag{3.11}
\]
This is valid for \(\alpha=+\lambda\) and \(\alpha=-\lambda\); only the
argument of \(A\) changes. The exact phase derivative is
\[
{d\Psi\over d\alpha}
=\log {|\alpha|D_j\over\pi q\sqrt{Xx}},
\tag{3.12}
\]
so both \(\alpha=\pm\lambda\) are stationary, with
\(\Psi''(+\lambda)=+1/\lambda\) and
\(\Psi''(-\lambda)=-1/\lambda\). Lemma 2.2 is invariant under this sign
change. Combining (3.11) with the accepted post-endpoint stationary
numerator \((D_j/q)\lambda\) gives (1.2). Applying the ordinary BV
Fresnel estimate to an \(O_b(\lambda^{-2})\) regular finite part gives
(1.3).

Thus the two signed saddle phases may differ, but no cancellation between
them is needed for the local power count. Summing the singular pieces in
\(q\) is harmless:
\(\sum q^{-4}\log(2+q\theta)<\infty\) for fixed remaining parameters.
Likewise the local regular ledger has the accepted absolutely summable
\(q^{-2}\). These observations do not execute the remaining scale and
profile sums.

## 4. First doubtful or unproved step

The first exact survivor is
\[
\boxed{\quad
\|R_{U,V}\|_\infty+
\operatorname {Var}_{|\alpha|\asymp\lambda}R_{U,V}
\ll_b\lambda^{-2}
\quad}
\tag{4.1}
\]
uniformly in the exact moving section, for the **complete recombined**
post-endpoint numerator and through every artificial and physical seam.
Here \(R_{U,V}\) means the regular finite part after the explicit diagonal
Plemelj term has been removed as in (3.10), with the appropriate complete
profile in place of \(f_b/(A+iy/2)\).

Round 27 supplies a fixed-\(b\) size estimate of order
\(O_b(\alpha^{-2})\) for the separated PV coefficient. It does not supply
the two-variable difference-quotient and endpoint-trace estimate (2.7),
nor its scaled derivative in \(\alpha\). In particular, the named
artifacts do not justify (4.1) across
\[
\omega G+(1-\omega)R_1-\omega E_1,
\]
the artificial \(\rho\)-cutoff transition, connector/Cauchy--Green area
terms, the \(v=0\) axial seam, or the double-bounded share. Applying a
pointwise \(C^2\) stationary lemma here would simply repeat the false step
identified in Round 29.

Even after (4.1), the following are not discharged:

1. uniform \(U,V,S\) exhaustion and the finite outside-\(u,v\) sides;
2. the height tails (the high-\(|\alpha|\) top tail was previously not
   absolutely integrable before stationary analysis);
3. the full \(q,h,D_j,x\), radial, floor/star, and profile sums; and
4. transfer from the normalized local coefficient to the external
   \(-(4/\pi)X^{1/4}\Re\{e(1/8)(\cdots)\}\) normalization.

Thus the logarithmic singularity has been isolated and controlled, but the
complete beta stationary-transition theorem is not proved.

## 5. Required control tests and outcomes

### Signed-vs-unsigned

**Pass locally; no global signed gain claimed.** The limit was taken as
\(\pi\delta-i\,\mathrm{PV}\) before any absolute value. Taking absolute
values in (3.1) first would recreate the spurious \(\log(1/a)\). Lemma
2.2 is coefficient-adversarial and therefore cannot by itself provide a
character or \(\chi_4\) cancellation for the complete \(M_1\) sum.

### Support and degeneracy

**Pass for the exact finite polytope.** The section is (2.1). Only
\(\nu=\pm V\), equivalently \(L=\pm V\), creates a pole-face logarithm.
The top faces \(|L-\nu|=U\) give affine switches/endpoints, and
\(L=\pm(U+V)\) gives section collapse. Lemma 2.2 is uniform when a
saddle, a \(v\)-face, and an interval endpoint coalesce. Degenerate
non-Morse phases are outside its hypotheses and have not been silently
included.

### Residue and normalization

**Pass for the separated local branch.** The Plemelj sign and delta
coefficient in (2.2)--(2.5) are retained. Identity (1.1) introduces no
new \(\rho\)-residue. The exact omega split is not altered. Equations
(1.2)--(1.3) are on the accepted Round-27 normalized local scale; the
external \(X^{1/4}\) and real-part normalization remain explicitly
downstream.

### Endpoint uniformity

**Pass for the abstract singular integral.** A saddle at a moving
endpoint gives a half-Fresnel term. If the log point also meets that
endpoint, its bound is still
\(O(\Lambda^{-1/2}\log(2+\Lambda))\). No exact leading half-Fresnel
constant is asserted or needed for the bound.

### Order of limits

**Pass at finite height; exhaustion open.** The order used is: finite-box
\(\mu\) Plemelj limit first, exact section decomposition second, signed
stationary analysis third, absolute \(q\)-summation fourth, and height
exhaustion last. Interchanging the first and last operations has not been
used.

### Coefficient adversary

**Pass as a robustness test, and it limits the conclusion.** Lemma 2.2
holds for arbitrary \(W^{1,1}\) amplitude, so the local logarithmic bound
does not hide a sign assumption. Precisely for that reason it proves no
arithmetic signed saving. The \(q^{-4}\) diagonal count follows from the
actual profile decay, while the \(q^{-2}\) finite-part count remains
conditional on (4.1).

### \(q\)-power, face, tail, and normalization ledger

| Piece | Before stationary numerator | After \((D_j/q)\lambda\) | Status |
|---|---:|---:|---|
| diagonal delta/log at \(L=\pm V\) | \(O_b(\lambda^{-4}\log(2+\lambda))\) | \(O_b(D_jq^{-4}\theta_j^{-3}\log(2+\lambda))\) | proved on separated \(R_1\) patch |
| regular finite part | \(O_b(\lambda^{-2})\), scaled BV required | \(O_b(D_jq^{-2}\theta_j^{-1})\) | first survivor |
| top-face switches and section endpoints | ordinary BV/Fresnel | no worse than regular ledger | conditional on the same traces |
| smooth top remainder/interior \(W\) pieces | no Hilbert log | ordinary Fresnel ledger | requires their accepted profile norms |
| outside-\(u,v\) sides and height tails | not estimated here | not summed | open |
| complete scale/profile sum and external \(X^{1/4}\) | not applicable locally | not executed | open |

## 6. Dependencies and exact artifacts used

No web source and no numerical or symbolic experiment was used. The
derivation is entirely analytic. The exact artifacts consulted were:

1. protocol.md;
2. state/proof_obligations.yml, at graph SHA-256
   23a3c1929047ab40a0a67d07a4de96a7943ce3b83a8beec35ff433d933038be2;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md;
5. rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/synthesis.md;
6. rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/synthesis.md;
7. rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/reviews/conductor_finite_section_analysis.md;
8. the Round-30 brief
   rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/briefs/beta_log_kernel_attack.md.

The imported facts are the accepted local \(R_1\) denominator and
\(q^{-2}\) ledger, the exact two-saddle phase derivative, the
distribution-first finite-section formula, and the Round-29 rejection of
pointwise scaled \(C^2\) at a height face. Equations (1.1), (2.4)--(2.10),
and the sharpening of the diagonal logarithmic coefficient to
\(O_b(\lambda^{-4})\) are derived in this report.

## 7. Recommended state effect

**Promote, with restricted scope:**

1. the exact finite-section decomposition (2.4)--(2.8);
2. the uniform moving-logarithm Fresnel lemma (2.10), including both
   Hessian signs and saddle/face/endpoint coalescence;
3. the exact identity (1.1) and the conclusion that the separated-\(R_1\)
   diagonal face logarithm is \(q^{-4}\) up to one logarithm on the
   normalized local ledger.

**Retain open / revise:** replace the idea that the face logarithm is the
local \(q^{-2}\) bottleneck by the precise survivor (4.1), the scaled BV
estimate for the regular finite part of the complete recombined numerator.

**Do not promote:** any claim that Round 30 closes height exhaustion,
finite outside sides, the full actual-profile sum, coefficient-sensitive
gain, or the complete beta theorem. No shared proof-state file should
change merely from this candidate report.

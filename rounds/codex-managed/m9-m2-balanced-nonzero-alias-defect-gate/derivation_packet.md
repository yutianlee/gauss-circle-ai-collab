# Round 116 derivation packet

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Evidence status: the facts in Sections 1--2 are accepted graph content.
Section 3 is a conductor calculation to be audited, not an accepted lemma.

## 1. Accepted literal object

For one persistent (j=1) balanced block,

\[
 a_B^{<}(h,k)=\chi_4(h)
 \eta\!\left({(h,k)\over \sqrt L/2}\right)A_B(h,k),
\]

with (h,k\asymp L), (R=\sqrt X\asymp L^3). Both (A_B) copies,
both gcd weights, the fixed block, and every literal support crossing remain.
The actual double-far energy is

\[
 E_{B,\mathrm{df}}
 =\sum_{\substack{|h'k'-hk|>L\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}
 e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right).
\tag{116.D1}
\]

The phase-free counterpart (M_B^{(0)}) is accepted at
(O_\varepsilon(L^3X^\varepsilon)). Thus (116.D1) has the target if and
only if the Round-115 zero-subtracted remainder has the target, modulo this
already-owned term.

## 2. Accepted increment facts and barriers

With (h'=h+p), (k'=k+q),

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
\]

Nonzero character factors force (p=2s), and

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s=e(s/2).
\tag{116.D2}
\]

The character is constant on a fixed shift and shifts rather than removes
Poisson aliases. Plain shortened Fejer amplifies the already
target-saturating corridors. A one-variable outer B-process is critical and
capacity-preserving. Real Hessian size alone is not a discrete alias bound.
None of these facts is a lower bound for the actual signed sum.

## 3. Conductor alias calculation requiring audit

Fix (h,k), put (k'=k+q), (h'=h+2s=x), and consider the oscillatory
part of the (s)-sum. Ignoring for the moment the arithmetic and sharp-gate
legality problem, Poisson with integer frequency (m) gives phase

\[
 \Phi_m(s)=R\sqrt{hk}-R\sqrt{(h+2s)k'}+{s\over2}-ms.
\]

Set the positive half-integer alias

\[
 \lambda={1\over2}-m.
\]

At an interior stationary point,

\[
 \lambda=R\sqrt{k'/x},\qquad
 x={Xk'\over\lambda^2}.
\tag{116.D3}
\]

The stationary phase is

\[
 \Psi(h,k,q;\lambda)
 =R\sqrt{hk}-{X(k+q)\over2\lambda}-{\lambda h\over2}.
\tag{116.D4}
\]

If

\[
 \lambda_0=R\sqrt{k/h},
\]

then (116.D4) has the exact square completion

\[
 \Psi
 =-{h(\lambda-\lambda_0)^2\over2\lambda}
 -{Xq\over2\lambda}.
\tag{116.D5}
\]

The stationary second derivative in the (s)-variable is

\[
 \Phi_m''(s)=R\sqrt{k'}\,x^{-3/2}\asymp L^2,
\]

so a single interior stationary integral has natural amplitude
(L^{-1}). The active alias interval has length (asymp L^3).

At (116.D3), the determinant gate is exactly

\[
 \rho
 =hk'-xk
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2).
\tag{116.D6}
\]

Put

\[
 \lambda_r={Rk'\over\sqrt{hk}}.
\]

The radial-product gate is exactly

\[
 \Delta
 =xk'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\tag{116.D7}
\]

On critical support, (116.D6)--(116.D7) convert the two width-(L)
corridors into width-(L^2) alias neighborhoods of (lambda_0) and
(lambda_r), respectively. This comparison needs constants and boundary
audit; the exact formulas, not the comparison, are the proposed invariant.

The reciprocal (q)-frequency in (116.D5) is (X/(2\lambda)). Its
near-integral set is a near-hyperbola lattice problem

\[
 |X-2j\lambda|\lesssim L^2,
 \qquad j,\lambda\asymp L^3.
\tag{116.D8}
\]

Counting (116.D8) alone is not yet a bound for the signed alias family.

## 4. Norm and capacity gate

The unscaled formal dual family has (L^2) choices of (h,k), (L)
choices of (q), (L^3) aliases, and stationary amplitude (L^{-1}).
Aliaswise absolute values therefore have (L^5) capacity, one power worse
than the original (L^4) sum. B-process inversion recovers that lost power
but supplies no saving.

A lawful success must keep the alias family jointly signed and prove a
new inequality. One sufficient but potentially overstrong candidate is a
diagonal-scale local energy. Define

\[
 T_{h,k}
 =\sum_{\substack{h',k'\asymp L\\
 |h'k'-hk|>L,\ |hk'-h'k|>L}}
 \overline{a_B^{<}(h',k')}e(-R\sqrt{h'k'}).
\tag{116.D9}
\]

Then

\[
 E_{B,\mathrm{df}}
 =\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk})T_{h,k},
\]

and Cauchy gives the exact implication

\[
 \sum_{h,k}|T_{h,k}|^2
 \ll_\varepsilon L^4X^\varepsilon
 \quad\Longrightarrow\quad
 |E_{B,\mathrm{df}}|
 \ll_\varepsilon L^3X^\varepsilon,
\tag{116.D10}
\]

because (sum|a_B^{<}|^2\ll L^2X^\varepsilon). The diagonal after
squaring (116.D9) is already of size at most (L^4X^\varepsilon), so
(116.D10) asks for off-diagonal control at diagonal scale. It also erases
the outer character and may be strictly stronger than the scalar target.
The round must validate, replace, or reject this norm rather than silently
assuming it.

## 5. Required decision

Either prove a literal version of (116.D10), supply a different explicit
signed inequality closing the complete alias family, prove a target-safe
subrange or positive-power saving, or give a rigorous scoped no-go for the
one-alias/reciprocal-frequency mechanism and name the smallest survivor.


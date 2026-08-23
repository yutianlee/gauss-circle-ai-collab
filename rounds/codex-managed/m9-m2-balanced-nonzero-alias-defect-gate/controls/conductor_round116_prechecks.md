# Conductor Round 116 prechecks

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Evidence status: exact algebra and capacity diagnostics. No estimate for the
open remainder is asserted.

## 1. Literal divisor-progression alias lattice

Fix an outer odd (h), (k), and an inner (k'=k+q). Expand the second
gcd weight exactly as

\[
 \eta((h',k')/G_0)
 =\sum_{d\mid h',\ d\mid k'}\gamma_d,
\qquad
 \gamma_d=\sum_{e\mid d}\mu(e)\eta((d/e)/G_0).
\]

Only odd (d) can contribute to the character. For every such (d\mid k'),
choose the unique (s_d\pmod d) with

\[
 h+2s_d\equiv0\pmod d,
\]

and write (s=s_d+dt). Since (d) is odd,

\[
 (-1)^s=(-1)^{s_d}(-1)^t.
\]

Thus Poisson in (t), not unconstrained Poisson in (s), is the literal
one-dimensional transform after the divisor expansion. Put

\[
 x=h+2s=h+2s_d+2dt.
\]

For Poisson frequency (m\in\mathbb Z), define

\[
 \mu={1\over2}-m,
 \qquad
 \lambda={\mu\over d}.
\]

An interior stationary point satisfies

\[
 \lambda=R\sqrt{k'/x},
 \qquad
 x={Xk'\over\lambda^2}.
\tag{116.P1}
\]

The alias lattice has spacing (1/d) and length (asymp L^3), hence
(asymp dL^3) aliases for this divisor. The second derivative in (t) is

\[
 d^2R\sqrt{k'}x^{-3/2}\asymp d^2L^2,
\]

so the stationary amplitude is (asymp(dL)^{-1}). Its squared mass is

\[
 (dL^3)(dL)^{-2}\asymp L/d,
\]

which matches the (L/d) primal progression length. This is the exact
Plancherel-scale self-return; aliaswise absolute values instead have mass
(asymp L^2), inflating the primal ℓ1 capacity by (dL).

## 2. Dual phase with the progression residue

At (116.P1), the stationary phase, including the progression residue, is

\[
 \Psi_d
 =R\sqrt{hk}-{Xk'\over2\lambda}-{\lambda h\over2}
 +s_d\left({1\over2}-\lambda\right).
\tag{116.P2}
\]

The final term is a genuine root-of-unity progression phase on the alias
lattice and cannot be discarded. Apart from it, if

\[
 \lambda_0=R\sqrt{k/h},
\]

then

\[
 \Psi_d-s_d(1/2-\lambda)
 =-{h(\lambda-\lambda_0)^2\over2\lambda}
 -{Xq\over2\lambda}.
\tag{116.P3}
\]

## 3. Exact gate images

At the stationary point,

\[
 \rho=hk'-xk
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2).
\tag{116.P4}
\]

Put

\[
 \lambda_r={Rk'\over\sqrt{hk}}.
\]

Then

\[
 \Delta=xk'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\tag{116.P5}
\]

On (h,k,k'\asymp L) and (lambda,\lambda_0,\lambda_r\asymp L^3),
the two strict width-(L) gates remove width-(asymp L^2) alias
neighborhoods of (lambda_0) and (lambda_r), up to fixed support
constants. Equations (116.P4)--(116.P5), rather than this comparison, are
the exact statements.

## 4. Reciprocal (q)-frequency after the divisor restriction

Because (d\mid k'), write (k'=dv), so (q=dv-k) and (v\asymp L/d).
The (v)-linear part of (116.P2) is

\[
 -{Xd\over2\lambda}v
 =-{Xd^2\over2\mu}v.
\tag{116.P6}
\]

Even perfect cancellation in this (v)-sum saves at most its length
(L/d). That compensates one part of the aliaswise Poisson inflation but
does not alone supply the extra factor (L) required by the primal
(L^4\to L^3) target. A further signed cancellation in aliases and outer
variables remains mandatory.

Near integral reciprocal frequency means that for some integer
(j\asymp dL^3),

\[
 \left|{Xd\over2\lambda}-j\right|\lesssim {d\over L},
\]

equivalently

\[
 |Xd^2-2j\mu|\lesssim d^2L^2.
\tag{116.P7}
\]

This is a near-hyperbola resonance count. A count for (116.P7) is not a
signed bound for the remaining alias family.

## 5. Positive local-energy candidate is overstrong

Let

\[
 S_B=\sum_{h',k'}\overline{a_B^{<}(h',k')}e(-R\sqrt{h'k'})
\]

and let (C_{h,k}) be the same inner sum restricted to the union of the two
Round-114 corridors relative to ((h,k)). Then the row in the proposed
local energy satisfies exactly

\[
 T_{h,k}=S_B-C_{h,k}.
\tag{116.P8}
\]

The corridor row has absolute mass (O_\varepsilon(LX^\varepsilon)), so
over (O(L^2)) outer pairs,

\[
 \|C\|_2\ll_\varepsilon L^2X^\varepsilon.
\]

Consequently

\[
 \|T\|_2
 \ge cL|S_B|-O_\varepsilon(L^2X^\varepsilon)
\tag{116.P9}
\]

on a nondegenerate fixed block with (asymp L^2) outer pairs. The proposed
bound

\[
 \sum_{h,k}|T_{h,k}|^2\ll L^4X^\varepsilon
\]

would therefore force the stronger scalar estimate

\[
 |S_B|\ll_\varepsilon LX^\varepsilon,
\]

not merely the required (L^{3/2}X^\varepsilon). This does not prove the
local energy false for the actual symbol, but it proves that it is a much
stronger Gram target and cannot be treated as an equivalent reformulation.

## 6. Two-transform return diagnostic

At exact (v)-frequency resonance (Xd/(2\lambda)=j\in\mathbb Z), the
(v)-phase in (116.P6) disappears. Substituting

\[
 \lambda={Xd\over2j}
\]

into (116.P2) gives

\[
 R\sqrt{hk}+{s_d\over2}
 -{Xd(h+2s_d)\over4j}.
\tag{116.P10}
\]

Since (h+2s_d) is divisible by (d), this is again a reciprocal
one-variable phase on the progression data. A second Poisson/B-process in
(j) returns to the original progression variable. This is an algebraic
self-return diagnostic. It does not rule out a genuinely signed joint
large-sieve theorem, but it rules out claiming a gain from the two
invertible transforms alone.

There is a sharper exact reciprocal calculation before localizing the
(v)-frequency. Put

\[
 \ell_d={h+2s_d\over d}.
\]

Using \(\mu=d\lambda\) and \(k'=dv\), equation (116.P2) becomes, up to the
constant \(R\sqrt{hk}+s_d/2\),

\[
 -{Xd^2v\over2\mu}-{\ell_d\mu\over2}.
\tag{116.P11}
\]

If a second B-process in the half-integer variable \(\mu\) introduces
integer frequency \(n\), its stationary equation is

\[
 \mu^2={Xd^2v\over \ell_d+2n},
\]

and the Legendre phase is exactly

\[
 -dR\sqrt{v(\ell_d+2n)}.
\tag{116.P12}
\]

This is the original square-root phase on

\[
 k'=dv,\qquad h'=d(\ell_d+2n).
\]

The full second dual range has \(O(L/d)\) frequencies, exactly the original
progression length. Keeping only its zero frequency would be invalid; paying
all frequencies restores the primal capacity. Thus the two successive
one-variable B-processes are algebraically involutive on every literal
divisor progression.

## 7. Current smallest lawful gate

The identities above make the alias geometry literal. They do not prove the
required scalar bound. A successful continuation must prove a joint signed
estimate before aliaswise or outer-row absolute values. The positive row
local energy is overstrong, reciprocal (q)-cancellation alone only repays
the Poisson inflation, and exact two-transform completion returns to the
primal progression.

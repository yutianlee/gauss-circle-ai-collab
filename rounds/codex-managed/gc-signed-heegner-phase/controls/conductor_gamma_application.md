# Round228 conductor gamma and conditional transform control

## 1. Result

The exact gamma ratio has two transitions and a uniformly controlled
resonant expansion. After the specified common phase is multiplied in,
the large phase reduces to exp(2it log R), while the small gamma ratio
remains. This is a scalar identity and conditional functional-equation
calculation, not a cancellation estimate or a truncated dual-sum theorem.
At the critical line its modulus is exactly one.

## 2. Exact hypotheses

Use the isolated packet: eta<=sigma<=1-eta with fixed0<eta<1/2,
delta in{0,1}, t>=2, v real, s=sigma-it+iv. All powers of positive
numbers use the real logarithm. Let Q_delta be the packet's gamma
ratio and E_R=exp(2it[1+log(pi R/t)]) for R>0. Put
a=(sigma+delta)/2, b=(1-sigma+delta)/2, w=t-v/2,
d=1/2-sigma, c_delta=pi(delta/2-1/4), and
S_delta(sigma,v)=Gamma(b-iv/2)/Gamma(a+iv/2).
The conditional application in Section3 assumes an L-function with
the explicitly stated functional equation; it does not establish one
for the actual old/new spectral basis.

## 3. Independent derivation and conditional application

Direct substitution gives the exact factorization
\[
Q_delta(s,t)=pi^{2sigma-1}e^{2i(v-t)log pi}
 {Gamma(b+iw)\over Gamma(a-iw)} S_delta(sigma,v).       \tag{1}
\]
The real parts a,b stay in a fixed positive compact interval. Uniform
vertical Stirling for |y|>=1 and continuity on |y|<=1 therefore give,
with two-sided constants depending only on eta,
\[
|Q_delta(s,t)|\asymp_eta
 [(1+|v|)(1+|2t-v|)]^{1/2-sigma}.                    \tag{2}
\]
Each pair has equal imaginary magnitude, so its exponential factors
cancel. The centers are v=0 and v=2t. No large-argument formula is used
at either center. At sigma=1/2 the numerator gamma factors are exactly
the conjugates of the denominator factors, so the modulus is1.
More generally Q(s,t)Q(1-s,t)=1 and conjugate Q(s,t)=Q(conjugate s,t).
Thus on the critical line Q(t,2t-v)=conjugate Q(t,v)=Q(t,v)^(-1).

For |v|<=2t/3, w>=2t/3. This covers the requested half window and
the entire |v|<=t^(1/3) window for t>=2. The large pair alone has expansion
\[
 {Gamma(b+iw)\over Gamma(a-iw)}
 =w^d\exp(i[2w(log w-1)+c_delta])\,[1+r(w)],
 \quad r^{(j)}(w)=O_{eta,j}(w^{-1-j}).               \tag{3}
\]
To see the constant, the numerator contributes (2b-1)pi/4 and division
by the negative-imaginary denominator contributes (2a-1)pi/4. Their
sum is (a+b-1)pi/2=c_delta, independent of sigma. The remainder and
its derivatives follow by differentiating the uniform log-Gamma
Stirling remainder and exponentiating on this fixed vertical sector.

Combine (1),(3) with E_R. Without any Taylor approximation in v,
\[
E_R Q=pi^{2sigma-1}w^d S_delta(sigma,v)
 \exp(i[2t log R+v log(pi^2/t)+c_delta+Psi_t(v)])
 [1+r(w)],                                         \tag{4}
\]
where
\[
Psi_t(v)=2(t-v/2)log(1-v/(2t))+v.                   \tag{5}
\]
The logarithm is real on this window. Its first two derivatives are
Psi_t'=-log(1-v/(2t)) and Psi_t''=(2t-v)^(-1).
For j>=2, Psi_t^{(j)}=(j-2)!(2t-v)^{1-j}.
Consequently
\[
Psi_t(v)=v^2/(4t)+v^3/(24t^2)+O(v^4/t^3),
\quad Psi_t(v)-v^2/(4t)=O(|v|^3/t^2).               \tag{6}
\]
For the last difference, v-derivative orders j=0,1,2,3 are bounded
by C_j |v|^{3-j}/t^2 (with |v|^0=1 at j=3); for j>=4 the bound is
C_j t^{1-j}. These follow directly from (5), including v=0.
Mixed t derivatives follow by differentiating the same rational/log
form, so no hidden near-zero gamma Stirling estimate is required.

For |v|<=t^(1/3), replace Psi_t by v^2/(4t) in (4) with multiplicative
error O(t^-1+|v|^3/t^2)=O(t^-1). Keep w^d exactly: replacing it by
t^d would instead cost O(|v|/t), as large as t^-2/3 on this window.
For |v|<=t/2 the cubic phase error can be order t; formula(4), not
its quadratic reduction, is the applicable approximation. Fixed v
derivatives of S are controlled by its polynomial modulus times powers
of log(2+|v|), since a,b remain positive. Near v=0 it is smooth with
S(sigma,0)=Gamma(b)/Gamma(a). At that center,
\[
E_R Q=pi^{2sigma-1}t^d {Gamma(b)\over Gamma(a)}
e^{i(2t log R+c_delta)}[1+O_eta(t^-1)].              \tag{7}
\]
These statements also distinguish the exact small factor from the
common large spectral phase: neither has been discarded in (4).

Here is a conditional application with all variable factors explicit.
Suppose a primitive Hecke series L(s)=sum lambda(n)n^-s satisfies
\[
L(s)=omega q^{1/2-s}Q_delta(s,t)L(1-s),\quad |omega|=1. \tag{8}
\]
For a test on a coefficient scale M0, Mellin inversion of
sum lambda(m)m^{it}a(m/M0) initially pairs M0^z ahat(z)L(z-it).
If a shift to Re(z)=1/2 is justified, set z=1/2+iv and use (8).
The scalar prefactor is exactly
omega q^{it-iv} E_R Q(1/2-it+iv,t).
In the near-transition window, (4) reduces this to a factor
omega exp(it log(q R^2)) times
exp(iv log(pi^2/(q t))) S_delta(1/2,v), with the curvature phase
Psi_t(v), constant c_delta and Stirling remainder all retained.
If a dual coefficient n is subsequently expanded under a justified
contour procedure, L(1-s) supplies n^(-1/2-it+iv). Its combined
oscillation is therefore
\[
 e^{it log(q R^2/n)}
 e^{iv log(pi^2 M0 n/(q t))},                       \tag{9}
\]
in addition to the retained factors. If the original variable is h=Dm,
then h^(it) contributes D^(it), and M0=M/D. The first factor becomes
exp(it log(q D R^2/n)); the second has M0=M/D. This shows the algebraic
resonant scale n~q t/M0. It does NOT prove a sharp support restriction,
a subpower bound for the transformed weight, a justified dual-series
expansion on the critical line, or a summation bound over spectral t.
The remaining small gamma factor has its own Fourier/Mellin transform.
At v outside the local window, both transition centers and all tails
must still be paid. Actual spectral coefficients, old/new changes,
root numbers and CM-point weights must be supplied by a separate audit.

For the round's actual sizes t~TM/sqrt(N), this formal dual scale is
qD T/sqrt(N), including every parity descendant D. It can be shorter
than M0 but its coefficients and common spectral phase are different.
No bound for the entire signed cusp expression follows just from this
scale computation. The complete continuous partner also remains a
separately owned part of the round's full target.

## 4. First doubtful or unproved step

No full signed arithmetic estimate is claimed. The first unsupported
extension would be replacing the exact small gamma factor by Stirling
at v=0, replacing Psi by a quadratic throughout |v|<=t/2, declaring
the formal resonant scale to be uniform dual support, or inferring
cancellation from the exact critical-line unit modulus. In application,
the contour move, dual expansion, transformed test bounds and actual
spectral pairing remain to be justified by the assigned attack.

## 5. Required controls and outcome

Exact factorization and critical-line modulus: PASS by conjugation.
Inversion symmetry: PASS by swapping s and1-s, equivalent to v and2t-v.
Transition centers: PASS by inspecting the four imaginary arguments.
Constant phase: PASS by summing both Stirling constants; delta0 gives
-pi/4 and delta1 gives pi/4. v=0 size and phase: PASS by (7).
Quadratic range: PASS; cubic remainder is small on t^(1/3) but can
grow on the larger window. Differentiated remainders: PASS from (3),(5).
Conditional level/parity descendant phases: PASS algebraically in (9),
with actual coefficient identification and all contour work ungranted.
No mathematical experiment or numerical asymptotic evidence was used.

## 6. Dependencies and provenance

Conductor-authored control, Round228, campaign gc-signed-heegner-phase.
Inputs: protocol, frozen isolated gamma statement, frozen full Heegner
interface, closed227 spectral/Heegner reports and reviews, checkpoint226,
and the accepted complete-wave bridge. Gamma calculations were derived
in the conductor's reasoning before receiving the blind role's progress
message reporting the two centers and cubic Taylor order. The present
file was written after that message; this timing is disclosed. No blind
report was read before the initial version of this file. After reading
the completed blind report, the conductor explicitly enlarged the
large-pair window to2t/3 to cover the small bounded-t overlap between the
two requested windows. No substantive formula changed. The conditional functional equation(8)
is an explicit hypothesis, not an external-source import or an asserted
identity for the actual oldspace. A separate nonauthor application review
must bind these exact bytes before closure.

## 7. Recommended state effect

Retain as a scoped elementary and conditional application control after
nonauthor review. No graph, proof-draft, complete bound, moment or exponent
change follows. Full quarter and all complete owners remain open.

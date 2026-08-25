# Round 151 statement-only blind report: the \(D=1,\ L=1\) reciprocal \(B\)-process

## 1. Result: source-hypothesis no-go and exact self-return

**Result.** The character split is exact and determines the prospective dual
main sum without any parity hypothesis on \(N\). Put

\[
w_U(q):=\mathscr A_{1,M,U}\!\left(1,{4N\over q^2}\right),\qquad
f_\sigma(q):={N\over q}+{\sigma q\over4},\qquad
\sigma\in\{1,-1\}.
\]

On each smooth portion \(I\) of the literal \(q\)-support, Poisson summation
and stationary phase give the interior dual main sum

\[
\boxed{
 {e(1/8)N^{1/4}\over i}
 \sum_{\substack{\ell>0\ {\rm odd}\\ \ell\in 4N/I^2}}
 \chi _4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}) .}
\tag{1.1}
\]

Here \(4N/I^2\) is the interval with reversed endpoints. Section 3 retains
the literal lattice corrections, truncated Fresnel endpoint terms, and
stationary and nonstationary remainders rather than hiding them in (1.1).
The dual length is \(\asymp M\); before the actual profile is inserted, one
dual term has size

\[
N^{1/4}M^{-3/4}\asymp RM^{-3/4},
\]

so its coefficient-weighted absolute capacity is \(RM^{1/4}\), not \(R\),
when the actual profile has unit-scale size.

The transform is algebraically involutive. A second stationary-phase
transform of its square-root phase returns \(N/q+\sigma q/4\), returns the
original amplitude exactly, and cancels the two Maslov factors. Thus a
second \(B\)-process gives no new power saving. Absolute summation of (1.1)
is row-target-sized only for bounded \(M\). At \(M\asymp R^2\), the direct
\(q\)-count is already target-sized because \(Q\asymp R\). The growing
intermediate range remains open.

There is a prior exact source-hypothesis obstruction. The permitted files
name the actual profile but provide neither its formula nor its amplitude,
derivative, one-sided endpoint, transition-count, jump-variation, or
clipped-prefix bounds. Hence the endpoint and transition remainders cannot
be estimated, and even the size of
\(\mathscr A_{1,M,U}(1,\ell)\) in (1.1) cannot be audited. This is not a
replacement of the actual profile by an arbitrary bounded smooth function,
and it is not a counterexample to that actual profile. It shows that the
statement-only packet does not contain the hypotheses needed for a
boundary-complete estimate. Even if a later source audit supplied
\(X^\varepsilon\)-sized profile norms and transition errors, (1.1) would
still require a new signed square-root-wave estimate for growing
intermediate \(M\).

Accordingly, this report proves no new strict owner-complete growing-\(M\)
range and does not prove the complete large-wrap target. It proves the exact
dual shape, its congruence and signs, the exact self-return obstruction, and
the first missing source hypothesis.

## 2. Exact statement and hypotheses

Throughout, \(e(z)=e^{2\pi iz}\). The following proposition separates the
unconditional algebra from the profile data that must be supplied.

**Proposition 2.1 (boundary-complete formal transform and obstruction).**
Let \(I\subset[cQ,CQ]\) be a finite union of bounded intervals. Suppose, only
for the purpose of forming a \(B\)-process, that the literal lattice profile
\(w_U(q)\) is accompanied by a specified compactly supported, piecewise
\(C^4\) continuation \(w_U(x)\) on \(I\), with specified one-sided values at
every transition. Define

\[
T_\sigma=\sum_{q\in\mathbb Z}^{\rm literal}w_U(q)e(f_\sigma(q)),
\qquad
S_U={T_+-T_-\over2i}.
\tag{2.1}
\]

Then:

1. Equation (2.1) is exactly the original character-twisted sum, including
   its restriction to odd \(q\).
2. The exact Fejer--Poisson identity (3.3) contains an explicit correction
   at every integer transition. A stationary frequency \(n\in\mathbb Z\)
   has
   \[
   \lambda={\sigma\over4}-n>0,\qquad
   x_{\sigma,n}=\sqrt{N/\lambda}.
   \tag{2.2}
   \]
   An interior stationary point gives (1.1). A stationary point at, or
   within one stationary scale of, an endpoint gives the truncated Fresnel
   factor (3.5), not a full Gaussian factor.
3. On a smooth piece on which
   \(w_U(x)=\mathscr A_{1,M,U}(1,4N/x^2)\), the logarithmic derivatives obey
   the exact chain rule
   \[
   (x\partial_x)^j w_U(x)
   =(-2y\partial_y)^j\mathscr A_{1,M,U}(1,y),
   \qquad y={4N\over x^2}.
   \tag{2.3}
   \]
   At the stationary point indexed by the odd integer \(\ell\), one has
   \(y=\ell\) exactly. Thus every dyadic, cone, radial, or clipped-prefix
   transition at an integral \(y\) can be a stationary endpoint. It cannot
   be smoothed away or assigned an average value without a source check.
4. The interior transform is self-returning, as shown in
   (3.10)--(3.13).

The following data are necessary to turn Proposition 2.1 into a uniform
estimate, but none is supplied in the permitted statement:

- the exact finite \(q\)-support, including whether each endpoint is open,
  closed, or half weighted;
- a partition containing all dyadic, cone, radial, and clipped-prefix
  transition points, uniformly in \(M,U,N\);
- the literal value and both one-sided values at every transition that can
  be an integer \(q\), or that can map to an integer \(y=4N/q^2\);
- bounds for the number of pieces, total jumps, and total variation;
- on every smooth piece, bounds for
  \[
  \sup_{y\asymp M}\left|(y\partial_y)^j
  \mathscr A_{1,M,U}(1,y)\right|,\qquad 0\leq j\leq4,
  \tag{2.4}
  \]
  together with the analogous bounds for every cutoff factor;
- a uniform rule for a clipped prefix whose clipping index varies with
  \(y\), including the possibility that it changes at every integer sampled
  in (1.1).

No assumption that an endpoint derivative stays away from an integer is
made here; such an assumption would not be uniform. The Fresnel factor below
retains the exact transition when \(f_\sigma'(a)\) or \(f_\sigma'(b)\) is an
integer.

If a later source ledger proved that all the norms, piece counts, and jump
variations above were \(O_\varepsilon(X^\varepsilon)\), the remaining
interior assertion needed for a row of size \(R\) would be

\[
\left|
\sum_{\substack{\ell\asymp M\\ \ell\ {\rm odd}}}
\chi_4(\ell)\ell^{-3/4}
\mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell})
\right|
\ll_\varepsilon X^\varepsilon.
\tag{2.5}
\]

For a unit-size profile this asks for a factor \(M^{1/4}\) beyond absolute
summation, equivalently an unweighted square-root-wave bound of size
\(M^{3/4}X^\varepsilon\). Proposition 2.1 supplies no such signed estimate.

## 3. Proof and derivation

### 3.1 Exact character algebra

For every integer \(q\), not merely every odd integer,

\[
{e(q/4)-e(-q/4)\over2i}
=\sin(\pi q/2)=\chi_4(q).
\tag{3.1}
\]

For even \(q\) both sides vanish. Extending the original odd-\(q\) sum to
all integers therefore introduces no term, and

\[
S_U={1\over2i}\sum_qw_U(q)e(N/q+q/4)
-{1\over2i}\sum_qw_U(q)e(N/q-q/4).
\tag{3.2}
\]

This uses no parity condition on \(N\), no coprimality of \(N\) and \(q\),
and no reduction of the fraction \(N/q\).

### 3.2 Literal endpoints and the exact Poisson identity

Let \(\mathcal T\) be the transition set of a supplied piecewise
continuation. Write \(w(t-),w(t+)\) for its one-sided values, taking the
exterior value to be zero at a support endpoint, and let
\(w^{\rm lit}(t)\) be the value used by the literal finite prefix. Set

\[
C_\sigma:=
\sum_{t\in\mathcal T\cap\mathbb Z}
\left(w^{\rm lit}(t)-{w(t-)+w(t+)\over2}\right)e(f_\sigma(t)).
\]

Fejer summation of the Fourier series of the periodization of the compactly
supported piecewise \(C^1\) function \(w(x)e(f_\sigma(x))\) gives the exact
identity

\[
T_\sigma=C_\sigma+
\lim_{H\to\infty}
\sum_{|n|<H}\left(1-{|n|\over H}\right)
\sum_{J=(a,b)}\int_a^b
w_J(x)e(f_\sigma(x)-nx)\,dx .
\tag{3.3}
\]

The correction \(C_\sigma\) changes the Fourier-series average at an
integer discontinuity into the literal prefix value. Thus a hard clipped
endpoint has not been replaced by a smooth or half-weighted endpoint.

On one piece \(J=(a,b)\), the phase in the \(n\)-th integral has

\[
f_\sigma'(x)-n=-{N\over x^2}+{\sigma\over4}-n,\qquad
f_\sigma''(x)={2N\over x^3}>0,
\]
\[
f_\sigma'''(x)=-{6N\over x^4},\qquad
f_\sigma^{(4)}(x)={24N\over x^5}.
\tag{3.4}
\]

It has at most one stationary point, namely (2.2). Let

\[
\Delta_{\sigma,n}:=f_\sigma''(x_{\sigma,n})^{-1/2},\qquad
\alpha={a-x_{\sigma,n}\over\Delta_{\sigma,n}},\qquad
\beta={b-x_{\sigma,n}\over\Delta_{\sigma,n}},
\]
\[
\Phi(\alpha,\beta):=\int_\alpha^\beta e(t^2/2)\,dt.
\]

When \(x_{\sigma,n}\in[a,b]\), the boundary-complete leading stationary
term is

\[
\mathcal M_{\sigma,n,J}:=
w_J(x_{\sigma,n})\Delta_{\sigma,n}
e(2\sqrt{N\lambda})\Phi(\alpha,\beta),
\qquad \lambda={\sigma\over4}-n.
\tag{3.5}
\]

Indeed, Taylor expansion at \(x_{\sigma,n}\), followed by
\(x-x_{\sigma,n}=\Delta_{\sigma,n}t\), produces (3.5). Define its remainder
to be the exact difference between the integral in (3.3) and (3.5).
Integrals with no stationary point are retained as nonstationary endpoint
terms. With these definitions, (3.3) is an exact decomposition: no dual
main sum has been called an error.

For a stationary point far from both endpoints on the stationary scale,

\[
\Phi(-\infty,\infty)=e(1/8).
\tag{3.6}
\]

At an exact single endpoint, with the other endpoint remote on that scale,
the value is \(e(1/8)/2\). Within \(O(\Delta)\) of an endpoint it is the
displayed nonconstant Fresnel transition. The error in replacing the finite
Fresnel integral by (3.6), the Taylor remainder, and the nonstationary
integrals depend on precisely the missing derivative norms, jump ledger,
and number and location of pieces. Thus (3.5), not an unqualified full
Gaussian, is compulsory for the actual clipped prefix.

### 3.3 Congruence, sign, and amplitude of the interior dual wave

Put \(m=-n\) and

\[
\ell=4m+\sigma=\sigma-4n.
\]

The positivity condition in (2.2) is exactly \(\ell>0\). For the plus branch
\(\ell\equiv1\pmod4\), while for the minus branch
\(\ell\equiv-1\pmod4\). Moreover,

\[
\lambda={\ell\over4},\qquad
x_{\sigma,n}=2\sqrt{N/\ell},\qquad
2\sqrt{N\lambda}=\sqrt{N\ell},
\tag{3.7}
\]

and

\[
f_\sigma''(x_{\sigma,n})^{-1/2}
=2N^{1/4}\ell^{-3/4}.
\tag{3.8}
\]

The actual reciprocal profile is sampled at

\[
{4N\over x_{\sigma,n}^2}=\ell
\tag{3.9}
\]

exactly, not merely up to dyadic comparability. Combining (3.6)--(3.9) in
\((T_+-T_-)/(2i)\) gives (1.1): the difference between the two residue
classes is exactly multiplication by \(\chi_4(\ell)\). This proves the
mod-four congruence, both signs, and the amplitude. The positivity
restrictions are \(m\geq0\) for \(\sigma=1\) and \(m\geq1\) for
\(\sigma=-1\). No parity of \(N\) enters.

### 3.4 Exact self-return of the main transform

Retain the unit-spaced variable \(m\). For either sign put

\[
\lambda=m+{\sigma\over4}>0,\qquad
q(m)=\sqrt{N/\lambda},\qquad
g_\sigma(m)=2\sqrt{N\lambda}.
\tag{3.10}
\]

Then

\[
g_\sigma'(m)=q(m),\qquad
g_\sigma''(m)=-{\sqrt N\over2\lambda^{3/2}}<0.
\tag{3.11}
\]

A second Poisson transform with integer frequency \(p>0\) has stationary
point

\[
m_p={N\over p^2}-{\sigma\over4},
\]

and its Legendre phase is

\[
g_\sigma(m_p)-pm_p
={2N\over p}-{N\over p}+{\sigma p\over4}
={N\over p}+{\sigma p\over4}=f_\sigma(p).
\tag{3.12}
\]

The first amplitude in the \(m\)-normalization and the second stationary
factor multiply to one:

\[
\left({N^{1/4}\over\sqrt2}\lambda^{-3/4}\right)
\left(\sqrt2N^{-1/4}\lambda^{3/4}\right)=1.
\tag{3.13}
\]

The first curvature is positive and contributes \(e(1/8)\); the second is
negative and contributes \(e(-1/8)\). These factors cancel. Endpoints map
in reverse order and retain their Fresnel transitions. The main
\(B\)-process is therefore an involution: the second transform returns the
original reciprocal wave rather than an independent power gain.

### 3.5 All-\(M\) power ledger

At \(D=1\), the relation \(DE\asymp M\) gives \(E\asymp M\). Since
\(N\asymp X=R^4\),

\[
Q=2\sqrt{N/E}\asymp R^2M^{-1/2},\qquad
{N\over Q^2}\asymp M,
\]
\[
f''(q)\asymp {M^{3/2}\over R^2},\qquad
\Delta\asymp RM^{-3/4}.
\tag{3.14}
\]

There are \(O(1+M)\) stationary frequencies, and the dual \(\ell\)-interval
has length \(\asymp M\). The supplied coefficient inequality does give the
literal endpoint coefficient bound

\[
|B_{1,U}(1)|\leq
\sum_L {|B_{1,U}(L)|\over\sqrt L}
\ll_\varepsilon X^\varepsilon.
\]

Thus the \(B\)-coefficient causes no power loss. If the missing actual-profile
norms were also \(O_\varepsilon(X^\varepsilon)\), the two elementary row
capacities would be

\[
|S_U|\ \lesssim\
\min\{R^2M^{-1/2},\,RM^{1/4}\}X^\varepsilon.
\tag{3.15}
\]

The first quantity is the original \(q\)-count; the second is absolute
summation of (1.1). Equation (3.15) is a capacity comparison, not a signed
lower bound and not a substitute for the absent endpoint estimates.

For an endpoint pair, a target \(R^2X^\varepsilon\) naturally asks for a
uniform row size \(RX^\varepsilon\). The regimes are:

| \(M\)-regime | \(Q\) | Better elementary row capacity | Consequence for row target \(R\) |
|---|---:|---:|---|
| \(M=O(1)\) | \(\asymp R^2\) | \(RM^{1/4}\asymp R\), dual | Target-sized, but bounded \(M\) is already excluded/owned |
| \(1\ll M\ll R^{4/3}\) | \(R^2M^{-1/2}\) | \(RM^{1/4}\) | Loses \(M^{1/4}\) |
| \(M\asymp R^{4/3}\) | \(\asymp R^{4/3}\) | \(\asymp R^{4/3}\) | Loses \(R^{1/3}\) |
| \(R^{4/3}\ll M\ll R^2\) | \(R^2M^{-1/2}\) | \(R^2M^{-1/2}\), original | Still exceeds \(R\) |
| \(M\asymp R^2\) | \(\asymp R\) | \(\asymp R\), original | Target-sized directly; dual capacity is \(R^{3/2}\) |

Thus the \(B\)-process itself gives no strict polynomial growing-\(M\)
range. It is useful at bounded \(M\), while the top dyadic range is already
short enough before transformation. A second-derivative estimate on the
dual square-root phase only reflects (3.15). Indeed,

\[
{d^2\over d\ell^2}\sqrt{N\ell}\asymp R^2M^{-3/2}.
\]

The standard two-term curvature capacity for its unweighted sum is
\(RM^{1/4}+R^{-1}M^{3/4}\). Multiplication by \(RM^{-3/4}\) gives
\(R^2M^{-1/2}+1\), the original-side scale. This quantitative reflection
agrees with the exact involution (3.12).

### 3.6 Relation to \(h,k,\rho\) at the endpoint

For odd \(q_1,q_2\asymp Q\), set \(h=(q_1,q_2)\) and \(q_i=hr_i\). Then
\(h,r_i\) are odd and \((r_1,r_2)=1\), uniquely. With
\(\delta=r_2-r_1\), choose a centered integer \(k\) and put

\[
\rho=N(r_2-r_1)-khr_1r_2.
\]

No imprimitive fraction is discarded, because

\[
e\!\left(N\left({1\over q_1}-{1\over q_2}\right)\right)
=e\!\left({N(r_2-r_1)\over hr_1r_2}\right)
=e\!\left({\rho\over hr_1r_2}\right),
\tag{3.16}
\]

and

\[
\chi_4(q_1q_2)=\chi_4(h^2r_1r_2)=\chi_4(r_1r_2).
\tag{3.17}
\]

The tie convention for centered \(k\) affects the label but not (3.16).
Since \(D=1\), centering gives

\[
|\rho|\leq {hr_1r_2\over2}\leq {hr_1r_2\over D};
\]

therefore every nonexact endpoint pair lies in the stated collar. Also,

\[
1\leq h\ll Q,\qquad r_i\asymp Q/h,\qquad
|\delta|\ll Q/h,
\]
\[
|k|\ll N/Q+1\asymp R^2\sqrt M,\qquad
|\rho|\ll Q^2/h.
\tag{3.18}
\]

For two profiles \(U,V\), the full unmasked pair is the corresponding
product \(S_U\overline{S_V}\), and (3.16) recovers its wrap phase without
discarding common factors or denominators dividing \(N\). Consequently, a
proved uniform row bound \(S_U\ll RX^\varepsilon\), together with the
accepted exact-\(\rho\) and packet estimates, would control the
\(D=1,L=1\) large-wrap residual by subtraction. The packet scale is
consistent with the target:

\[
{R^2\over Q}\asymp\sqrt M,\qquad
Q\left(1+{R^2\over Q}\right)\ll R^2.
\tag{3.19}
\]

This invokes the accepted packet theorem; it does not sum the unselected
fixed shifts absolutely. In the intermediate ranges, (3.15) does not prove
the needed row bound, so this subtraction cannot complete the residual.

## 4. First doubtful or unproved step

The **first** unproved step is the construction and audit of the continuum
profile needed already in (3.3). The permitted files do not state the
formula for \(\mathscr A_{1,M,U}\), its literal support, its one-sided
values, or any bound in (2.4). Because stationary phase samples
\(4N/q^2=\ell\) exactly, an integral clipped-prefix transition may occur at
every dual stationary value. Nothing in the permitted packet shows that
there are only \(O(X^\varepsilon)\) transition terms, that their jumps have
bounded total variation, or that the stationary remainders are target-safe.

This obstruction precedes any disputed cancellation estimate. If a
source-complete derivative and transition ledger is later supplied and its
boundary errors are proved target-safe, the next unproved step is (2.5), or
an equally strong signed estimate that exploits the actual sampled profile.
The self-return calculation (3.10)--(3.13) shows that another reciprocal
\(B\)-process does not prove it.

No arbitrary profile has been substituted for the actual profile, and the
absolute capacities in (3.15) are not asserted as signed lower bounds.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_large_wrap_residual | **Structurally passed; estimate open.** Equations (3.16)--(3.18) recover every \(D=1,L=1\) pair, and centered nonexact pairs exhaust the collar. The intermediate row estimate needed for subtraction is unproved. |
| accepted_small_packet_exclusion | **Passed.** The packet contains \(O(1+R^2/Q)=O(1+\sqrt M)\) wraps, and its supplied fixed-wrap owner has total scale \(Q(1+R^2/Q)\ll R^2\). No outside wrap is summed absolutely. |
| D1_L1_reciprocal_scalar | **Passed algebraically.** The literal scalar is exactly (3.2), with the actual profile retained symbolically. |
| exact_character_fourier_identity | **Passed.** Equation (3.1) holds for every integer and kills even \(q\) automatically. |
| boundary_complete_B_process | **Obstructed at source.** Equation (3.3), the literal corrections, and the Fresnel factor (3.5) give the required form, but no uniform remainder estimate follows without the missing profile ledger. |
| actual_profile_derivative_ledger | **Failed/absent.** The formula, smooth pieces, jumps, endpoint values, prefix changes, and derivative norms are absent. Equation (2.3) records exactly what must be checked. |
| dual_self_return_vs_gain | **Passed as a no-go.** Equations (3.10)--(3.13) prove the phase, amplitude, congruence, sign, and Maslov self-return. Dual absolute summation is target-sized only for bounded \(M\); direct length is target-sized at the top dyadic range. |
| tuple_absolute_signed_separation | **Passed.** The raw dual count is \(O(M)\), its weighted absolute capacity is \(RM^{1/4}\), and its signed value is (1.1). No adverse capacity is made into a lower bound. The endpoint-pair raw count \(Q^2\asymp R^4/M\) is separate from either row capacity and from the accepted coefficient-weighted fixed-wrap mass. |
| all_M_D_E_Q_L_h_k_rho_power_ledger | **Passed within the assigned endpoint.** Here \(D=L=d=1,\ E\asymp M,\ Q\asymp R^2M^{-1/2}\); (3.14), the regime table, and (3.18) give the remaining scales. No claim is made for \(D>1\) or \(L>1\). |
| prime_parity_prefix_imprimitive_controls | **Parity and imprimitive checks passed; prefix check obstructed.** There are no \(d_o\)-prime issues at \(d=1\); even \(q\) vanish exactly; \(N\) may have either parity; \(q\mid N\) is retained; and common factors are retained in (3.16)--(3.17). The literal prefix cannot be audited without its missing definition. |
| generic_tge2_cross_and_downstream_scope | **Passed as a scope check.** This report treats only \(D=1,L=1\) and the reciprocal scalar. It asserts nothing about \(D>1\), \(L>1\), shifted-factor two-adic transfer, any \(t\geq2\) layer, the independent cross owner, the growing-\(M\) generic complement, or downstream assembly. |

## 6. Dependencies and exact artifacts used

This statement-only derivation used exactly:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/blind_statement.md;
3. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/briefs/blind_d1_reciprocal_bprocess_feasibility.md.

No proof graph, strategy file, prior nonblind artifact, sibling report, web
source, or numerical experiment was inspected or used. The only inherited
mathematics used without reproof is the statement's accepted fixed-wrap,
selected-packet, exact-\(\rho\), and bounded-\(M\) control.

## 7. Recommended state effect

**Recommended effect: retain as an exact obstruction; no target promotion.**
Retain (1.1), the literal endpoint identity (3.3)--(3.5), the exact sampling
identity (3.9), and the self-return calculation (3.10)--(3.13) as candidate
evidence. Record the omitted actual-profile derivative and transition ledger
as the first source-hypothesis obstruction. Reject any claim that the
reciprocal \(B\)-process alone proves a new growing-\(M\) endpoint range:
after the source seam is repaired, a genuinely new signed estimate for
(1.1), with the literal sampled profile and every boundary term, is still
required.

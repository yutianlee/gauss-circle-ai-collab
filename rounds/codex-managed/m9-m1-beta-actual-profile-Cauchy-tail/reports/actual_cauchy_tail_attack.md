# Round 38 discovery report: the actual beta-slab Cauchy tail converges

## 1. Result

**Actual Cauchy-tail theorem.** Fix \(X\) sufficiently large, put
\(b=1/\log(2X)\), take \(0<a<a_0\) with \(a+2b<1/2\), and choose the
legal terminal abscissa

\[
 c'=\frac54,\qquad
 \kappa:=c'+\frac{a+b}{2}-\frac12
 =\frac34+\frac{a+b}{2}<1.                         \tag{38.1}
\]

For the complete fixed-\(w\), endpoint-free positive-\(b\) density of
Round 37, first take the signed hard-top limit \(a\downarrow0\), then use

\[
 t=\frac{\mu+\nu}{2}+\beta                             \tag{38.2}
\]

before applying an absolute value. Along

\[
 U=V=T,\qquad S_T=(2+X+2T+2B_0)^2,                   \tag{38.3}
\]

the resulting terminal plus oriented artificial-pole vector has a unique
limit. More precisely, its complete positive-line density satisfies

\[
 \boxed{
 |{\cal F}^{\rm ef}_{b;U,S}(\nu)|
 \le C_X(1+|\nu|)^{\kappa-4}\log(2+|\nu|)
      +C_X(1+|\nu|)^{-3},}                          \tag{38.4}
\]

uniformly in \(U\) and every \(S\) containing the beta slab. Consequently
the normalized Round-37 tail obeys

\[
\boxed{
 |{\mathfrak T}^{\rm ef}_{V_1,V_2;U,S}|
 \le C_X X^{1/4}
 (1+V_1)^{\kappa-3}\log(2+V_1)
 +C_X X^{1/4}(1+V_1)^{-2}\longrightarrow0 .}       \tag{38.5}
\]

The same majorant makes the \(U\)-tail Cauchy, while compact beta support
makes the \(S\)-limit eventually constant. Thus the prescribed joint
outside-height/profile net defines the endpoint-free,
connector-completed beta axial vector. The proof is absolute only **after**
the full delta/PV Plemelj operator has been formed. It uses no local
\(\lambda^{-2}\), \(\lambda^{-3}\), \(q^{-2}\), or target-size estimate;
the constant \(C_X\) is not claimed to have target-safe growth.

## 2. Exact statement and hypotheses

Use the Round-37 terminal density, with \(m=hq\),

\[
\begin{aligned}
 Q_{\rm ef}(s,u,v;h,q,m)
 ={}&{\bf1}_{hq=m}\chi_4(q)
 \sum_j\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
 \left(\frac hq\right)^{(u+v)/2}\\
 &\times R_{1,v}(1-s)K_{u+v}(1-s)m^{-s},           \tag{38.6}
\end{aligned}
\]

together with its single oriented artificial coefficient
\(\mathfrak P_\rho[R_1]\). Here

\[
 u=a+i\mu,\quad v=b+i\nu,\quad s=c'+it,\quad z=u+v, \tag{38.7}
\]

\[
 K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
 \frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
 {\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)},         \tag{38.8}
\]

and

\[
 R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}I_1(\rho),
 \quad
 I_1(\rho)=\int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx,
 \quad
 \rho=\frac14-s-\frac v2.                          \tag{38.9}
\]

The artificial germ is interpreted through the common identity

\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1              \tag{38.10}
\]

before any combined artificial/axial coefficient is extracted. No
separate arithmetic residue or endpoint prefix remains after the
Round-36 module subtraction.

The actual profiles satisfy

\[
 f_b(\nu):=\widehat\phi(b+i\nu),\qquad
 |f_b^{(r)}(\nu)|\ll_{b,r}(1+|\nu|)^{-3-r},          \tag{38.11}
\]

and

\[
 \widehat W_0(u)=u^{-1}+\widehat W_{+,r}(u),         \tag{38.12}
\]

where \(\widehat W_{+,r}\) and every interior
\(\widehat W_j\) are rapidly decreasing on vertical lines. Constants in
(38.11) cost at most a fixed power of \(b^{-1}=\log(2X)\). All
\(D_j,H_j+1\) floors, top conventions, \(\chi_4\), and the original
finite equality conventions remain attached.

The signed top operator is kept intact:

\[
 {\bf P}_U H
 =\frac12H(0)-\frac{i}{2\pi}{\rm PV}
 \int_{-U}^{U}\frac{H(\mu)}{\mu}\,d\mu.             \tag{38.13}
\]

The claim is that the full terminal/artificial vector obtained from
(38.6)--(38.13), including all finite Stokes images and the one-corner
convention, satisfies (38.4)--(38.5).

## 3. Proof or derivation

### 3.1 Exact beta-slab coordinates and coefficient phase

Set

\[
 p=\mu+\nu,\qquad
 t=\frac p2+\beta,\qquad dt=d\beta.                 \tag{38.14}
\]

This is a unit-Jacobian change in the original fixed-\(w\) coordinates;
it does not freeze the moving variable \(w-3/4-v/2\). On the beta support,
\(|\beta|\le2B_0\), and (38.3) contains the whole beta interval for every
\(|\mu|,|\nu|\le T\). Hence the \(S\)-truncation disappears exactly.

Put

\[
\begin{aligned}
 A&=s-\frac z2=A_0+i\beta,
 &A_0&=c'-\frac{a+b}{2},\\
 B&=s+\frac z2=B_0+i\alpha,
 &B_0&=c'+\frac{a+b}{2},\\
 \alpha&=p+\beta,
 &\eta&=\frac\mu2+\nu+\beta,\\
 \rho&=\rho_0-i\eta,
 &\rho_0&=\frac14-c'-\frac b2=-1-\frac b2 .
\end{aligned}                                             \tag{38.15}
\]

The exact tangent phase of the coefficient in (38.6) simplifies:

\[
 \left(\frac hq\right)^{ip/2}(hq)^{-i(p/2+\beta)}
 =q^{-ip}(hq)^{-i\beta}.                            \tag{38.16}
\]

Thus no hidden \(h\)-phase grows in the tangent direction. Its absolute
coefficient is

\[
 h^{-c'+(a+b)/2}q^{-c'-(a+b)/2}.                    \tag{38.17}
\]

For \(c'=5/4\), both exponents are strictly greater than one because
\(a+b<1/2\). Therefore the \(h,q,m\) sum, and the same sum with one
\(\log q\), is absolutely convergent. The character \(\chi_4(q)\) and
its zeros are retained, although no character cancellation is needed for
existence.

### 3.2 Exact tangent power table

Since \(A\) ranges over a compact set, uniform Stirling in the \(B\)
quotient gives

\[
 |K_z(1-s)|\ll_{a,b,B_0}(1+|\alpha|)^\kappa,
 \qquad
 |\partial_\mu K_z(1-s)|
 \ll (1+|\alpha|)^\kappa\log(2+|\alpha|).           \tag{38.18}
\]

For \(|\alpha|\to\infty\), the large quotient has phase

\[
\begin{aligned}
 \arg\frac{\Gamma((1+B)/2)}{\Gamma((2-B)/2)}
 ={}&\operatorname {sgn}(\alpha)
 \left\{|\alpha|
 \left(\log\frac{|\alpha|}{2}-1\right)+\frac\pi4\right\}
 +O(|\alpha|^{-1}),                                \tag{38.19}
\end{aligned}
\]

for both signs. The powers \(2^{2s+z-1}\pi^{1-2s}\) and the bounded
\(A\)-quotient supply their exact displayed elementary and bounded phases;
none changes the power \(\kappa\).

Because \(\rho_0=-1-b/2\),

\[
 |I_1(\rho)|+|\partial_\eta I_1(\rho)|\ll1,\qquad
 |R_{1,v}(1-s)|+|\partial_\mu R_{1,v}(1-s)|
 \ll_X(1+|\eta|)^{-1}.                              \tag{38.20}
\]

The first inequality follows directly from
\(\int_1^\infty x^{-3/2-b/2}(1+\log x)\,dx<\infty\).
The exact radial phase is

\[
 -\eta\log x+2\pi\sqrt{Xx}.                         \tag{38.21}
\]

It has a stationary point only when
\(\eta=\pi\sqrt{Xx}\), \(1\le x\le N_X\). This finite stationary band
and the strip \(|\eta|\ll1\) are covered by the uniform \(O_X(1)\)
part of (38.20); outside them one has at least the displayed
\((1+|\eta|)^{-1}\), and beyond the finite radial band one further
integration by parts gives \(O_X(|\eta|^{-2})\) for \(R_1\).

The exhaustive magnitude table is therefore:

| tangent region, either sign | \(K_z\) | \(R_1\) | hard-top factor on the top share | combined with \(f_b(\nu)\) |
|---|---:|---:|---:|---:|
| \(|\alpha|\asymp|\eta|\asymp R\) | \(R^\kappa\) | \(R^{-1}\) | signed Plemelj | controlled by (38.25) below |
| \(|\alpha|\ll1,\ |\eta|\asymp R\) | \(1\) | \(R^{-1}\) | \(|\mu|^{-1}\asymp R^{-1}\) off the delta | \(O_b(R^{-5})\) per bounded cell |
| \(|\eta|\ll_X1,\ |\alpha|\asymp R\) | \(R^\kappa\) | \(O_X(1)\) | \(|\mu|^{-1}\asymp R^{-1}\) | \(O_X(R^{\kappa-4})\) |
| finite radial stationary band | \(R^\kappa\) | \(O_X(1)\) | \(|\mu|^{-1}\asymp R^{-1}\) | \(O_X(R^{\kappa-4})\) |
| \(\mu=0\) delta | \(R^\kappa\) | \(R^{-1}\) | \(1/2\) | \(O_X(R^{\kappa-4})\) |
| both \(\alpha,\eta\) bounded | bounded | bounded | bounded | no height tail, since then \(\nu\) is bounded |

This table is unchanged for \(\nu\to+\infty\) and
\(\nu\to-\infty\). It also shows why a local saddle estimate is
unnecessary for the existence question.

### 3.3 The hard-top delta/PV convolution

After the \(t\)-integral is changed to beta coordinates, let
\(g_\nu(\mu)\) denote the complete beta integral of the top coefficient,
with the singular \(1/u\) removed but every factor in (38.6) retained.
The beta interval is now fixed and \(\psi(\beta)\) is independent of
\(\mu\); differentiating \(g_\nu\) therefore creates no omitted mask or
moving-\(t\)-endpoint term. This is exactly where using (38.14) before
asymptotics matters.
Equations (38.11), (38.17)--(38.20), including the logarithms from
differentiating (38.16) and the scale phases, give

\[
 |g_\nu(0)|\ll_X |f_b(\nu)|(1+|\nu|)^{\kappa-1},    \tag{38.22}
\]

\[
 \sup_{|\mu|\le1}|g_\nu'(\mu)|
 \ll_X |f_b(\nu)|(1+|\nu|)^{\kappa-1}
 \log(2+|\nu|).                                    \tag{38.23}
\]

For \(0<\kappa<1\), the elementary tangent convolution satisfies,
uniformly in \(U\),

\[
\int_{1<|\mu|\le U}
\frac{(1+|\mu+\nu|)^\kappa}
{|\mu|\{1+|\mu/2+\nu|\}}\,d\mu
\ll (1+|\nu|)^{\kappa-1}\log(2+|\nu|).              \tag{38.24}
\]

To prove (38.24), split into
\(|\mu|\le(1+|\nu|)/4\), the middle annulus
\((1+|\nu|)/4<|\mu|<4(1+|\nu|)\), and its complement.
The first region gives the harmonic logarithm times
\((1+|\nu|)^{\kappa-1}\). In the middle region put
\(y=\mu/2+\nu\); \(1/|\mu|\ll(1+|\nu|)^{-1}\), and
\(\int_{|y|\ll1+|\nu|}(1+|y|)^{-1}dy\ll\log(2+|\nu|)\).
The last region is
\(\int_{|\mu|\gg|\nu|}|\mu|^{\kappa-2}d\mu\), which converges exactly
because \(\kappa<1\).

In the symmetric PV, the constant \(g_\nu(0)\) integrates to zero.
Use (38.23) for \(|\mu|\le1\), and (38.24) outside. Together with the
delta term this proves

\[
 |{\bf P}_U g_\nu|
 \ll_X |f_b(\nu)|(1+|\nu|)^{\kappa-1}
 \log(2+|\nu|)
 \ll_X(1+|\nu|)^{\kappa-4}\log(2+|\nu|).            \tag{38.25}
\]

This is an absolute estimate only after the signed subtraction inherent
in (38.13); taking \(|a+i\mu|^{-1}\) before that step would reintroduce
the false \(\log(1/a)\).

For the smooth top remainder and every interior scale, rapid
\(\mu\)-decay gives

\[
\int_{\mathbb R}|\widehat W_j(i\mu)|
\frac{(1+|\mu+\nu|)^\kappa}
{1+|\mu/2+\nu|}\,d\mu
\ll (1+|\nu|)^{\kappa-1}.                           \tag{38.26}
\]

The possible rho seam \(\mu=-2\nu+O_X(1)\) lies where a smooth
\(\widehat W_j\) is rapidly small; for the hard top it was already
included in (38.24). Equations (38.25)--(38.26) are uniform in \(U\),
and their right sides are integrable in \(\nu\).

### 3.4 Actual scale, radial, and coefficient sums

At the chosen lines, the absolute sum in (38.17), with one logarithm, is
finite. Also

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\le1,\qquad
 (H_j+1)^b\ll1
 \quad\text{for }b=\frac1{\log(2X)},                \tag{38.27}
\]

and the actual active scale set has \(O(\log X)\) members. The norms of
the fixed smooth \(W_j\)'s are uniform. Thus all \(j,h,q,m,x\) sums and
integrals may be carried through (38.25)--(38.26), at a constant
\(C_X\). This proves the first term of (38.4). The proof is valid even
after replacing \(\chi_4\) by coefficients of modulus one; it therefore
proves existence, not the later signed target estimate.

### 3.5 Oriented artificial coefficient and axial seams

At \(\rho=0\), the \(s\)-residue of (38.9) is, with the already accepted
orientation,

\[
 \operatorname {Res}_{s=1/4-v/2}R_{1,v}(1-s)
 =\pi i\sqrt X\,I_1(0).                              \tag{38.28}
\]

The remaining completed product returns exactly

\[
 F_z\!\left(\frac34+\frac v2\right)
 =
 \zeta\!\left(\frac34+\frac u2+v\right)
 L\!\left(\frac34-\frac u2,\chi_4\right).           \tag{38.29}
\]

On this cell,

\[
 \beta_\rho=-\frac\mu2-\nu.
\]

Thus compact beta support forces
\(\mu=-2\nu+O(B_0)\). For large \(|\nu|\), the top delta is absent and
the PV factor is an ordinary \(O(|\nu|^{-1})\). The zeta factor in
(38.29) has bounded height and stays away from its pole because
\(a/2+b<1/4\). Period-four partial summation gives the elementary bound

\[
 \left|L\!\left(\frac34-\frac a2+i\tau,\chi_4\right)\right|
 \ll_{a}(1+|\tau|),                                \tag{38.30}
\]

so (38.11) yields

\[
 |{\cal F}_{\rho}^{\rm ef}(\nu)|
 \ll_X (1+|\nu|)^{-3}.                              \tag{38.31}
\]

The smooth \(u\)-profiles are better because they are sampled at
\(\mu=-2\nu+O(1)\). Formula (38.31) also applies with
\(\psi',\psi''\). A collision with \(u=0\) or \(v=0\) has bounded
\(\nu\), and the joint corner has \(\nu=0\); none contributes a
\(V\)-tail. All such coefficients are extracted once from (38.10).

### 3.6 Joint exhaustion and moving faces

Equations (38.25), (38.26), and (38.31) give an
\(L^1(d\nu)\) majorant independent of \(U\). They also dominate the
\(\mu\)-tail, so \(U\to\infty\) and \(V\to\infty\) form a joint Cauchy
net. Once (38.3) holds, changing \(S\) changes no beta-supported
terminal cell, while all beta radial sides are already zero.

Finite Stokes reassembles the ordinary faces, axes, connector faces,
connector axes, mixed area, and one corner into the positive-\(b\)
functional estimated above. Alternatively, in sectioned coordinates the
moving-face logarithm has coefficient bounded by the right side of
(38.25), and its additional \(\log(2+|\nu|)\) remains integrable.
It is not counted a second time. Dominated convergence now proves
(38.4)--(38.5) and independence of every cofinal exhaustion satisfying
the stated support separation. Licensed symmetric inversion then
introduces the hard-top and equality stars; no finite-height star was
used in the proof.

## 4. First doubtful or unproved step

There is no unproved step in the actual Cauchy-tail existence theorem
once the accepted profile decay (38.11), finite vector formula, and
common artificial-residue convention are admitted.

The first remaining analytic step lies strictly downstream: form the
limiting endpoint-free axial-subtracted terminal kernel and prove its
weighted local value and \(L\)-derivative estimates. Nothing in
(38.4) controls the \(X\)-dependence sharply enough for that purpose.
In particular, (38.4) does not imply a local \(q^{-2}\) gain or the
Gauss-circle target.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| beta-slab coordinate/Jacobian | Pass. Equation (38.14) has unit Jacobian, keeps real parts fixed, and is made on the original \(w\)-path. |
| gamma/R1 tangent powers | Pass. Equations (38.18)--(38.21) and the table cover both height signs, generic, bounded-alpha, rho-seam, radial-stationary, and bounded cells. |
| signed top before absolute values | Pass. The proof first uses (38.13), cancels the constant in the symmetric PV, and only then applies (38.23)--(38.24). |
| actual profiles and sums | Pass. Equations (38.11), (38.16)--(38.17), and (38.27) retain every profile, floor, scale, coefficient, and \(\chi_4\); the sums converge absolutely. |
| joint exhaustion | Pass. The majorant (38.4) is independent of \(U,S\) under (38.3) and is \(L^1\) in \(\nu\). |
| artificial/collision/corner | Pass. Equations (38.28)--(38.31) retain the oriented artificial coefficient; combined collisions occur once and have no tail. |
| moving faces and optional sides | Pass. They are finite-Stokes images of the same positive line, or log traces dominated by (38.4), and are not double counted. |
| actual rather than counterfunctional | Pass. Every bound begins from (38.6), the exact gamma quotient, \(R_1\), and the actual Mellin profiles; no model envelope is used to infer convergence. |
| normalization | Pass. The tail is multiplied exactly once by \(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\), as displayed in (38.5). |
| no local/target overreach | Pass. \(C_X\) is unrestricted; no terminal-symbol or target-size estimate is claimed. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The exact selected artifacts were:

1. 'protocol.md';
2. 'state/proof_obligations.yml', graph SHA-256
   'da69e58e4abbfdf5bc16207c4f3b7411e29661cc8d43c07769c4c2adf28ff0bf';
3. 'state/active_campaign.yml';
4. 'rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/reports/endpoint_free_axial_limit_attack.md';
5. 'rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md';
6. 'rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md';
7. 'rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/synthesis.md';
8. 'rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md';
9. 'rounds/codex-managed/m9-m1-partial-functional-equation-transitions/reports/blind_partial_FE_factorization.md';
10. the Round-38 task brief.

The imported accepted facts are the fixed finite vector, endpoint-free
module subtraction, compact-beta radial-side annihilation, exact
delta/PV operator, profile decay, and common residue ownership. The
beta-slab power table, tangent convolution (38.24), full tail majorant,
and artificial-coefficient tail are derived here.

## 7. Recommended state effect

**Promote after the required blind and hostile audits** the actual
beta-slab Cauchy-tail theorem (38.4)--(38.5), including the legal
\(c'=5/4\) choice, exact phase identity (38.16), tangent convolution
(38.24), and artificial-residue tail (38.31).

Close 'M9-M1-beta-endpoint-free-axial-Cauchy-tail' and use it to close
'M9-M1-beta-endpoint-free-axial-remainder-limit'. This supplies the unique
limiting endpoint-free connector-completed beta axial vector and closes
the remaining limit interface in mask--endpoint--axial compatibility.

Reject any proof that takes absolute values before Plemelj subtraction,
uses only compact-mask Fourier decay, omits the rho-seam or artificial
coefficient, freezes an off-centred path, double counts moving faces, or
infers a target-size estimate from the unrestricted constant \(C_X\).
The next round may define the limiting axial-subtracted terminal symbol;
its local weighted bound, beta transition, M9-M1, M9, and the Gauss target
remain open.

# Round 37 discovery report: the endpoint-free finite complement and its first tail survivor

## 1. Result

**Scoped no-go with an exact finite reduction.** The fixed-\(w\)
endpoint-free complement is well defined at every finite stage:

\[
 {\mathfrak V}_{\rm ef}^{\rm fin}(a,b;U,V,S)
 =
 {\mathfrak V}_{\rm pre}^{\rm fin}(a,b;U,V,S)
 -
 {\mathfrak M}_{\rm fin}(a,b;U,V,S).                 \tag{37.1}
\]

The common endpoint/arithmetic module is subtracted once, only after its
Round-36 global routing. Compact beta support deletes every renormalized
radial-side cell when
\[
 S>(U+V)/2+2B_0.                                    \tag{37.2}
\]
At fixed \(U,V,S\), the hard-top limit \(a\downarrow0\) of (37.1) exists
as a signed delta/PV distribution. In sectioned coordinates its moving
face singularities are only locally integrable logarithms; neither a
finite-\(V\) logarithmic divergence nor an additional radial side
survives.

The complete \(v\)-face, \(v=0\)-axis, connector, connector-axis, mixed,
and corner package must then be recombined by finite Stokes before
exhausting \(V\). It equals the original endpoint-free positive-\(b\)
fixed-\(w\) vertical. Thus optional \(v\)-horizontal sides are not a
second object and need not cancel a logarithm term by term.

The selected artifacts do **not**, however, prove the Cauchy convergence
of this complete positive-\(b\) vertical as \(V\to\infty\), uniformly in
the simultaneous \(U,S\) exhaustion and the actual \(j,h,q,m\) sums.
The first exact survivor is the normalized signed tail

\[
\boxed{
\begin{aligned}
 {\mathfrak T}^{\rm ef}_{V_1,V_2;U,S}
 :={}&-\frac4\pi X^{1/4}\Re\!\left\{
 e(1/8)\frac1{2\pi}
 \int_{V_1<|\nu|\le V_2}
 {\cal F}^{\rm ef}_{b;U,S}(\nu)\,d\nu\right\}.
\end{aligned}}                                             \tag{37.3}
\]

The density \({\cal F}^{\rm ef}_{b;U,S}\) is written explicitly below.
No theorem in the selected context shows

\[
 \lim_{V_1,V_2\to\infty}
 {\mathfrak T}^{\rm ef}_{V_1,V_2;U,S}=0
 \quad\text{uniformly along the prescribed }U,S
 \text{ exhaustion}.                                      \tag{37.4}
\]

Therefore existence and uniqueness of the limiting endpoint-free axial
vector remain open. This is a limit obstruction, not a terminal-symbol
or target-size obstruction.

## 2. Exact statement and hypotheses

Use the original reflected coordinate \(w=1-s\), held fixed when the
outside \(u\)- and \(v\)-rectangles are displaced. Put

\[
 u=a+i\mu,\qquad v=b+i\nu,\qquad s=c'+it,\qquad z=u+v,
 \qquad \beta=t-\frac{\mu+\nu}{2},                         \tag{37.5}
\]

with \(a>0\), fixed \(b>0\), \(|\mu|\le U\),
\(|\nu|\le V\), and \(|t|\le S\). Let

\[
 {\cal A}_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,\qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor .                         \tag{37.6}
\]

For \(m=hq\), define the common endpoint-free terminal density

\[
\begin{aligned}
 {\cal Q}_{\omega}(u,v,s;h,q,m)
 :={}&{\bf1}_{hq=m}\chi_4(q)
 \sum_j{\cal A}_j(u,v)\left(\frac hq\right)^{z/2}\\
 &\times{\cal R}_{\omega,v}(1-s)
 K_z(1-s)m^{-s},                                          \tag{37.7}
\end{aligned}
\]

where the complete gamma quotient is

\[
 K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
 \frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
 {\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)},                \tag{37.8}
\]

and the artificial-pole-safe radial combination is

\[
\begin{aligned}
 {\cal R}_{\omega,v}(w)
 :={}&\omega(\rho)G_v(w)
 +(1-\omega(\rho))R_{1,v}(w)-\omega(\rho)E_{1,v}(w)\\
 ={}&R_{1,v}(w),\qquad
 \rho=w-\frac34-\frac v2 .                                \tag{37.9}
\end{aligned}
\]

The second equality is meromorphic and is used only under identical
masks, domains, endpoints, and residue ownership. Formula (37.9) must
not be split when a rho divisor meets an axial or arithmetic divisor.

Separate the actual top transform as

\[
 \widehat W_0(u)=\frac1u+\widehat W_{+,r}(u).               \tag{37.10}
\]

Let \({\cal B}_{\rm top}(u,v,s)\) be the sum of (37.7) with the
\(j=0\) factor \(\widehat W_0(u)\) replaced by \(1\), and let
\({\cal B}_{\rm reg}\) contain the \(j=0\)
\(\widehat W_{+,r}\) term and all \(j\ge1\) terms. Both include
\(\psi(\beta)\), every \(h,q,m\) sum, (37.8), and (37.9). For a function
\(H(\mu)\), define the normalized signed top operator

\[
 {\bf P}_U H
 :=\frac12H(0)-\frac{i}{2\pi}{\rm PV}
       \int_{-U}^{U}\frac{H(\mu)}{\mu}\,d\mu .              \tag{37.11}
\]

This is exactly the limit of
\((2\pi)^{-1}\int_{-U}^{U}H(\mu)/(a+i\mu)\,d\mu\) as
\(a\downarrow0\). The complete positive-\(b\), fixed-\(w\),
physical-top density appearing in (37.3) is

\[
\boxed{
\begin{aligned}
 {\cal F}^{\rm ef}_{b;U,S}(\nu)
 :={}&\frac1{2\pi}\int_{-S}^{S}
 \bigg[
 {\bf P}_U\!\left\{
 {\cal B}_{\rm top}(i\mu,b+i\nu,c'+it)\right\}\\
 &\hspace{26mm}
 +\frac1{2\pi}\int_{-U}^{U}
 {\cal B}_{\rm reg}(i\mu,b+i\nu,c'+it)\,d\mu
 \bigg]dt .
\end{aligned}}                                             \tag{37.12}
\]

Here \({\cal B}_{\rm top}(i\mu,\cdot)\) in (37.12) denotes the coefficient
after the singular \(1/u\) has been removed, so (37.11) supplies the
entire hard-top delta/PV contribution. The aggregate module
\({\mathfrak M}_{\rm fin}=\sum_{\xi}D_\xi+
{\mathfrak R}^{\rm ar}[R_1]\) has already been removed in the passage to
(37.7); it is not subtracted again from (37.12).

The prescribed candidate exhaustion can be fixed concretely as

\[
 a\downarrow0\ \text{at fixed }U,V,S;\qquad
 U=V=T\to\infty,\qquad
 S=(2+X+2T+2B_0)^2,                                      \tag{37.13}
\]

followed by only the already licensed physical profile interpretation of
the limiting Mellin inversions. Other cofinal symmetric exhaustions are
not asserted to agree unless (37.4) and its \(u,s\) analogues are proved.

## 3. Proof or derivation

### 3.1 Exact finite complement and inventory

Round 36 gives (37.1) from one common fixed-\(w\) antecedent. Subtraction
removes the aggregate finite endpoint prefixes and the recombined
\(R_1\)-arithmetic residue. It does not separately delete any masked
face, connector, or Perron tail. Applying the complete beta transfer to
the remaining terminal density gives exactly the following inventory:

1. the terminal \(u,v\) vertical carrying \(\psi(\beta)\);
2. pure \(u\)- and \(v\)-horizontal faces, including their four products;
3. filtered \(u=0\) and \(v=0\) axis families;
4. one joint \(u=v=0\) corner under full-axis inclusion--exclusion;
5. both positive area connectors carrying \(\psi'(\beta)/2\);
6. both connector-boundary families;
7. both connector-axis families;
8. the positive mixed product area carrying \(\psi''(\beta)/4\);
9. combined artificial/axial/arithmetic collision germs; and
10. the two beta-masked renormalized radial-side families.

Every item contains the actual factors in (37.6)--(37.9). Item 10 is
identically zero under (37.2), including all of its restrictions and
collision germs. None of items 1--9 is deleted by compact support.

### 3.2 Signed top limit and moving logarithmic faces

At fixed \(U,V,S\), all nonsingular factors are smooth on each compact
cell after common collision excision. The distribution identity

\[
 (0^++i\mu)^{-1}=\pi\delta_0(\mu)
 -i\,{\rm PV}\frac1\mu                                  \tag{37.14}
\]

therefore gives (37.11)--(37.12), including the factor \(1/2\) arising
from the normalized Mellin measure. This half is the hard-top symmetric
inversion value; it is not a half-weight on an endpoint
integration-by-parts coefficient.

Under \(L=\mu+\nu\), the finite rectangle becomes

\[
 |\nu|\le V,\qquad |L-\nu|\le U.                           \tag{37.15}
\]

The \(\nu\)-section is
\([-V,V]\cap[L-U,L+U]\). When the PV pole meets a moving face, the
section coefficient has the form \(\log|L-L_0|\), which is locally
integrable in \(L\). The accepted moving-logarithm Fresnel lemma adds at
most one logarithm locally and is uniform at saddle/face/endpoint
coalescence. Hence the finite physical top limit exists. That lemma
supplies no majorant in \(\nu\) for (37.12), and so it does not prove
(37.4).

### 3.3 Why optional outside sides are not the survivor

For fixed finite boxes, the one-axis Cauchy--Green identity is

\[
 V_b=V_{b'}+H_+-H_-+2\pi iR_v+{\cal A}_v,                 \tag{37.16}
\]

and its second-axis transfer retains all induced boundary, axis, mixed,
and corner terms. Apply (37.16) to the complete endpoint-free density,
not to an isolated logarithmic coefficient. Finite Stokes then
reassembles all \(v\)-faces, \(v=0\) residues, connector faces,
connector-axis residues, and their corner into the original
positive-\(b\) vertical. Therefore (37.12) is the exact aggregate
representative.

The upper and lower \(v\)-horizontal segments sample analytic
continuations on different real abscissae; their values are not
determined by the coefficient of a vertical moving-face logarithm.
There is no universal termwise cancellation, and none is required.
Failure of (37.4) could equivalently appear as nonvanishing outside
horizontal cells in a shifted representation, but counting both would
double count one finite Stokes package.

### 3.4 The first unproved tail

The decay of \(\widehat\phi(b+i\nu)\) alone does not prove (37.4).
Inside (37.12), \(\nu\) is coupled to \(\mu,t\) through
\(\psi(t-(\mu+\nu)/2)\), the gamma quotient (37.8), the radial factor
(37.9), and \((h/q)^{i(\mu+\nu)/2}\). The PV part additionally needs
control of a \(\mu\)-difference quotient. A sufficient theorem would be
an \(L^1_\nu\) majorant \(g_b\), independent along (37.13), such that

\[
\begin{aligned}
 &\int_{-S}^{S}
 \bigg(
 |{\cal B}_{\rm top}(0,b+i\nu,c'+it)|\\
 &\qquad+
 \int_{-U}^{U}
 \left|\frac{{\cal B}_{\rm top}(i\mu,b+i\nu,c'+it)
 -{\cal B}_{\rm top}(0,b+i\nu,c'+it)}{\mu}\right|d\mu
 +\int_{-U}^{U}|{\cal B}_{\rm reg}|\,d\mu
 \bigg)dt
 \le g_b(\nu),\qquad g_b\in L^1(\mathbb R).                \tag{37.17}
\end{aligned}
\]

Equivalently, one could prove the signed Cauchy criterion (37.4)
directly. The selected artifacts prove neither (37.17) nor a substitute
exploiting the full oscillation and \(\chi_4\). They contain local
fixed-box Plemelj/logarithm control and separated saddle estimates, but
no uniform joint \(t,\mu,\nu\) majorant or derivative estimate after the
actual profile and coefficient sums. This proves the scoped no-go.

### 3.5 Audit of the right-chamber/Fourier shortcut

There is a tempting exact route, but it stops at the same tail. On the
right chamber one may expand

\[
 F_{-z}(s)=\sum_{m\ge1}\sum_{hq=m}\chi_4(q)
 \left(\frac hq\right)^{z/2}m^{-s},                         \tag{37.18}
\]

absolutely for the fixed real lines, and one may write

\[
 \psi\!\left(t-\frac{\mu+\nu}{2}\right)
 =\int_{\mathbb R}\widehat\psi(r)
 e^{ir t-ir\mu/2-ir\nu/2}\,dr,                              \tag{37.19}
\]

with \(\widehat\psi\) Schwartz. These identities justify termwise
algebra on each finite box. They do not justify the prescribed infinite
height limit.

The reason is structural. Schwartz decay in (37.19) is in the auxiliary
Fourier variable \(r\), not in either unbounded direction tangent to the
slab \(t-(\mu+\nu)/2=O(1)\). After (37.19), the factors
\({\cal R}_{\omega,v}(1-s)K_z(1-s)\) still couple \(t,\mu,\nu\).
The top term is still the distribution
\({\rm PV}\,d\mu/\mu+\pi\delta_0\), not an absolutely integrable Mellin
factor. Therefore neither Tonelli nor dominated convergence permits the
Dirichlet sum, the \(r\)-integral, and the symmetric
\(\mu,\nu,t\) exhaustions to be interchanged.

In particular, the accepted hard-top Perron inversion applies to the
isolated physical profile after its coefficient is a licensed test
function. Here that coefficient depends on \(\mu\) through (37.8)--(37.9)
and on the moving beta slab. One would need uniform control of its
\(\mu\)-difference quotient together with an integrable \(\nu\)-tail,
precisely (37.17), or a distributional Mellin theorem proving convergence
of these particular symmetric truncations. Absolute convergence of
(37.18) on fixed vertical lines is uniform in the phases but supplies no
height-integrable majorant after the \(s,u\) integrations and the actual
sum. Thus Fourier inversion of the compact mask does not close (37.4).

## 4. First doubtful or unproved step

The first unproved step is exactly (37.4), with
\({\cal F}^{\rm ef}_{b;U,S}\) given by (37.12). At fixed boxes the
finite complement, its collision convention, the signed top limit, and
the local logarithmic faces are all defined. What is missing is uniform
Cauchy convergence of the full positive-\(b\) density as the outside
heights grow.

The survivor is deliberately the complete signed tail, not the absolute
tail of one factor and not an optional \(v\)-horizontal segment. The
available evidence does not show that it is nonzero or divergent; it
shows only that its vanishing is the first theorem still required.
Without it, two cofinal choices in (37.13) are not proved to yield the
same endpoint-free axial vector.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| fixed-\(w\) complement | Pass. Equation (37.1) uses the common original \(w\)-path. Freezing \(r=w-3/4-v/2\) would move the \(w\)-path and omit boundary traces. |
| complete post-module inventory | Pass. Terminal, ordinary faces, both axes, both first connectors, connector boundaries/axes, mixed area, one corner, collisions, and radial sides are listed once. |
| boundary-module count | Pass. \({\mathfrak M}_{\rm fin}\) is subtracted once in (37.1); neither its endpoint prefixes nor its arithmetic residue is removed again from (37.12). |
| compact beta support | Pass only for radial sides. Condition (37.2) makes those cells exactly zero and is not used on terminal or physical-module cells. |
| signed Plemelj and moving faces | Pass at every fixed box. Equations (37.11), (37.14), and (37.15) retain the delta and PV signs; moving logs are locally integrable. |
| outside-height limit | Open. The exact survivor is (37.3). Decay of \(\widehat\phi\) alone gives no proved uniform bound for the coupled \(s,u\) integral and its PV difference quotient. |
| Dirichlet/Fourier shortcut | Fails at the limit interchange. The right-chamber series and (37.19) are exact on finite boxes, but Schwartz decay is only in the auxiliary Fourier variable and does not majorize the two unbounded slab directions or the hard-top PV coefficient. |
| optional \(v\)-horizontals | Pass as a scope test. They belong to (37.16) and reassemble the positive-\(b\) vertical; they are not added to (37.3). |
| collision/artificial ownership | Pass finitely. Equation (37.9) is kept common before combined coefficient extraction; the one-corner convention is unchanged. |
| profiles, stars, character, floors | Pass as a ledger. \(D_j,H_j+1,W_j,\phi,\chi_4,h,q,m\) remain in (37.7). No finite-height product or top star is inserted; the hard-top half appears only through (37.11), and physical equality stars arise only after licensed inversion. |
| normalization | Pass. Equation (37.3) carries the external \(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) exactly once. |
| no symbol overreach | Pass. No \(\lambda^{-2}\), \(\lambda^{-3}\), \(q^{-2}\), or target-size estimate is asserted. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The exact selected artifacts were:

1. 'protocol.md';
2. 'state/proof_obligations.yml', graph SHA-256
   'e60df4442ad731d8efe193e8a224934b27bfd12cc3842bfab581a452904f32cb';
3. 'state/active_campaign.yml';
4. 'rounds/codex-managed/m9-m1-vector-hankel-kernel/reports/blind_finite_vector_kernel.md';
5. 'rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/reports/outside_v_cancellation_attack.md';
6. 'rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/synthesis.md';
7. 'rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reports/actual_axial_connector_ledger_attack.md';
8. 'rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md';
9. 'rounds/codex-managed/m9-m1-beta-physical-module-transfer/reports/physical_endpoint_arithmetic_transfer_attack.md';
10. 'rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md';
11. the Round-37 task brief.

The imported facts are the finite reflected vector, complete finite
two-axis ledger, physical-top Plemelj/polytope identity, local
moving-logarithm lemma, compact-beta side annihilation, and aggregate
module routing. Equations (37.3), (37.12), and the reduction of all
optional \(v\)-cells to this one tail are the new conclusions.

## 7. Recommended state effect

**Retain open / revise.** Promote, after independent audit, only the
finite fixed-\(w\) complement definition, the post-module one-count
inventory, the fixed-box signed top limit, and the identification of
(37.3) as the first lawful outside-height survivor.

Do not close 'M9-M1-beta-endpoint-free-axial-remainder-limit'. Replace its
next action by proving the signed Cauchy criterion (37.4), or the
sufficient uniform majorant/difference-quotient theorem (37.17), for the
complete actual positive-\(b\) density. Reject termwise outside-side/log
cancellation, use of \(\widehat\phi\) decay without a uniform coupled
majorant, frozen off-centred \(r\)-paths, early stars, or a second
subtraction of the boundary module.

Retain the limiting endpoint-free axial vector, mask compatibility,
axial-subtracted terminal symbol, beta transition, M9-M1, M9, and the
Gauss target as open.

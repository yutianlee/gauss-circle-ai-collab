# Actual-vector parity projection attack

## 1. Result

**Exact reduction lemma, with a no-go conclusion.** On the part of the
literal hard complement for which the full class modulus is

\[
M=8N,\qquad N\ \mathrm{odd},
\]

and \(A,B_2,V\) all have residue \(2\pmod 8\), the complete local
\(8\)-part is an intact four-lift orbit. It annihilates \(4\nmid u\),
deletes the already-owned literal \(u=0\), and retains both families

\[
u\equiv4\pmod8,
\qquad
u\equiv0\pmod8,\quad u\ne0.
\]

After CRT and the canonical \(M^{-5}\mathfrak T_M\) normalization, its
opened local factor is exactly

\[
{4\over M^4}={1\over2^{10}N^4},
\]

with a sign \((-1)^{u/4}\) and the literal actual fourfold symbol still
attached. Equivalently, before the odd trace is opened,

\[
M^{-5}\mathfrak T_M
={(-1)^{u/4}\over2^{10}N^5}\mathfrak T_N
\quad(4\mid u),
\]

up to the displayed CRT outer linear characters below.

The four local lifts diagonalize only in their local base coordinate. For
generic odd-cofactor labels the result is a cross-projection

\[
{1\over4}\sum_{k\bmod4}e_4(k)
 \widehat F_k^a(y)\overline{\widehat G_k^c(y-v)},
\]

not a square. The only aligned case \(c=a,\ v=0\) has exact return period
\(R_*=4\), hence lies in the prior Round-88 coarse owner for large \(J\).
Thus the nonempty hard \(q=8\) residue is a strictly smaller scalar sum of
actual-row cross-projections. The local factor gives only constant savings,
so it proves neither a target-safe estimate nor a nonzero actual-vector lower
bound.

## 2. Exact statement and hypotheses

Use exactly

\[
J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
B=C_{\mathrm{cond}}/T,
\]

with \(M\asymp B\), the actual transition-flattened symbols \(I_b\), the
actual signed multiplier \(\Pi_{b,U}\), and the literal successive hard
complement after the unique global \(u=0\) owner and the Round-87--89 owners.
No stationary symbol is substituted for \(I_b\).

Fix a hard atom with \(M=8N\), with \(N\) odd. Put

\[
\alpha N\equiv1\pmod8,\qquad 8\beta\equiv1\pmod N.
\]

Write the CRT components as

\[
A=(2,a),\qquad B_2=(2,c),\qquad V=(2,v).
\]

Rename the second Fourier index \(\mu\), so that

\[
\Omega_{b,d,u}(n,\mu)
=I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(\mu+d)}I_b(\mu).
\]

Let \(h_{b,U}(a,c,v;u,d,n,\mu,\ldots)\) be the indicator of the **literal**
hard tuple, including its class, sign, alias, reflection, nonunit \(K\),
modulus-multiple, Ramanujan, prime-power, deep-support, and entry/exit data.
Then the exact \(q=8\) paired scalar survivor is

\[
\begin{aligned}
\mathcal S_8(U)
={}&{1\over2^{10}}
\sum_{\substack{b\asymp B\\M_b=8N,\ N\ \mathrm{odd}}}
\sum_{a,c,v,\ldots}
\sum_{\substack{0<|u|<U\\4\mid u}}
(U-|u|){(-1)^{u/4}\over N^4}\\
&\times\sum_{d,n,\mu}^{\mathrm{deep}}
h_{b,U}\,\Omega_{b,d,u}(n,\mu)
e_8\!\left(2\alpha(d+n-\mu)\right)
e_N\!\left(\beta(dv+na-\mu c)\right)\\
&\times
\sum_{\substack{y\bmod N\\
y,y-a,y-v,y-v-c\in(\mathbb Z/N\mathbb Z)^\times}}
e_N\!\left(\beta\{uy+K\Phi_{a,c,v}(y)\}\right),
\end{aligned}
\tag{2.1}
\]

where

\[
\Phi_{a,c,v}(y)=
\bar y-\overline{y-a}-\overline{y-v}+\overline{y-v-c}.
\]

All sums over classes and involutive mates remain inside (2.1), and the
outer conductor sum is taken before an absolute value. Formula (2.1), not
the isolated number \(32\), is the fixed-actual-vector projection to be
estimated against

\[
X^\varepsilon{U\over B}J^{14/5}.
\]

This statement concerns the exact two-primary component \(8\). Moduli with
\(v_2(M)\ne3\) are not coprime products \(8N\) and remain in the complementary
full-two-part problem.

## 3. Proof and derivation

CRT gives, for every integer \(z\),

\[
e_M(z)=e_8(\alpha z)e_N(\beta z).
\]

For \(A_8=B_{2,8}=V_8=2\), every allowed \(x_8\) is odd, all four shifted
arguments remain odd, and every odd residue is self-inverse modulo \(8\).
Consequently

\[
\Phi_{2,2,2}(x_8)=0,
\qquad
\sum_{x_8\bmod8}^{*}e_8(\alpha u x_8)=c_8(u),
\]

because multiplication by the odd number \(\alpha\) does not change
\(c_8\). Hence

\[
\mathfrak T_M
=\underbrace{8c_8(u)}_{\mathfrak T_8}
\underbrace{N\!\sum_y^{\mathrm{four\ units}}
e_N\!\left(\beta\{uy+K\Phi_{a,c,v}(y)\}\right)}_{\mathfrak T_N}.
\tag{3.1}
\]

Here \(c_8(u)=4(-1)^{u/4}\) if \(4\mid u\), and it is zero otherwise. No
coprimality condition on \(K\) was used. The remaining outer phase has
local components

\[
dV+nA-\mu B_2
=2(d+n-\mu)\pmod8,
\quad
=dv+na-\mu c\pmod N.
\]

Substitution into the canonical atom proves (2.1).

The normalization can be checked in three exactly equivalent forms:

\[
M^{-5}\mathfrak T_M
=M^{-3}{\mathfrak T_M\over M^2}
=M^{-4}\sum_x^{\mathrm{four\ units}}e_M(ux+K\Phi(x)).
\tag{3.2}
\]

On the paired \(8\)-cell,

\[
{\mathfrak T_8\over8^2}={c_8(u)\over8}
={(-1)^{u/4}\over2},
\]

so the completed-trace form of (3.2) is

\[
M^{-5}\mathfrak T_M
={(-1)^{u/4}\over2^{10}N^5}\mathfrak T_N.
\tag{3.3}
\]

Opening \(\mathfrak T_N=N\sum_y\) instead gives

\[
{(-1)^{u/4}\over2^{10}N^4}\sum_y.
\tag{3.4}
\]

Thus \(2^{-10}N^{-4}\) is the opened four-row factor, whereas
\(\mathfrak T_8/8^2=\pm1/2\) is the normalized completed local trace. They
must not be interchanged. There are exactly four full-modulus lifts for
each admissible \(y\), not \(4^4\): all four row bases share the same local
base \(x_8\).

For the physical interpretation, let \(\Delta\pmod M\) be the unique class

\[
\Delta\equiv2\pmod8,\qquad \Delta\equiv0\pmod N.
\]

It has exact additive order \(4\), and translation by \(\Delta\) preserves
units. Write a unit as \(x_{j,y}\), with
\(j\in\mathbb Z/4\mathbb Z\), so that
\(x_{j,y}\equiv r+2j\pmod8\) and \(x_{j,y}\equiv y\pmod N\). With the
actual pair phases, multiplier, stars, and zero extension included, set

\[
\begin{aligned}
F_j^a(y)&=f_{b,(x_{j,y},x_{j-1,y-a}),U},\\
G_j^c(z)&=f_{b,(x_{j,z},x_{j-1,z-c}),U},\\
\widehat F_k&=\sum_{j\bmod4}e_4(-kj)F_j,
\qquad
\widehat G_k=\sum_{j\bmod4}e_4(-kj)G_j.
\end{aligned}
\]

Then plain Fourier inversion on \(\mathbb Z/4\mathbb Z\) gives the exact
cross-projection

\[
\sum_{j\bmod4}F_j^a(y)\overline{G_{j-1}^c(y-v)}
={1\over4}\sum_{k\bmod4}e_4(k)
\widehat F_k^a(y)\overline{\widehat G_k^c(y-v)}.
\tag{3.5}
\]

This is a literal actual-row identity. Indeed, expanding \(F_j\) shows
that \(\widehat F_k\) retains only the actual two-row terms whose frequency
difference \(\delta\) obeys

\[
\alpha\delta\equiv k\pmod4,
\]

and supplies a factor \(4M^{-2}\). In the Gram product the two differences
are \(d+u\) and \(d\); equality of their \(k\)-modes forces \(4\mid u\).
The factor \((1/4)(4M^{-2})(4M^{-2})=4M^{-4}\) in (3.5) is precisely
(3.4). This independently reconciles the physical-row and completed-trace
normalizations.

For \(c=a,\ v=0\), one has \(G=F\) as a four-cycle family, and

\[
2\Re\sum_jF_j\overline{F_{j-1}}
={1\over2}\left(|\widehat F_0|^2-|\widehat F_2|^2\right).
\tag{3.6}
\]

The \(k=1,3\) terms are purely imaginary. This aligned four-cycle has
exact \(R_*=4\). Since

\[
\rho_*=\min\!\left(M,\lfloor J^{11/30}B^{-2}\rfloor\right),
\qquad B\le J^{3/20},
\]

one has \(\rho_*\ge\min(M,J^{1/15}+O(1))>4\) for large \(J\). Therefore
(3.6) belongs to the already-owned Round-88 coarse shell. The hard
cross-group residue has \(F\ne G\) and remains (3.5), not a difference of
squares.

## 4. First doubtful or unproved step

The first unavailable estimate is the fixed scalar bound for (2.1), or
equivalently for the hard sum of the cross-projections (3.5). Nothing in
the selected context proves orthogonality or a relative phase between
\(\widehat F_k^a(y)\) and \(\widehat G_k^c(y-v)\) for generic hard cofactor
labels. In particular, (3.6) cannot be reintroduced: it is both an
indefinite difference and a prior-owned aligned configuration.

The hard indicator is outside the complete \(x\)-trace in the canonical
formula, so it is constant on the four \(j\)-lifts of each surviving atom;
the local orbit projector is preserved atomwise. It is not a CRT product
in the remaining labels. The successive owners select a non-product subset
of \((a,c,v,u,d,n,\mu,\ldots)\), so globally the projector is fragmented
into cross-projections indexed by the surviving odd-cofactor data. Round
90's residual \(q=8\) cell prevents declaring the whole family deleted, but
gives no relation among its actual cross-projections.

The unique global \(u=0\) owner is enforced by \(0<|u|<U\). Replacing the
centered Fejer kernel by a positive square would reinsert \(u=0\), and taking
absolute values before the \(b\)-sum would destroy the only location where
conductor cancellation can occur.

## 5. Required controls and outcomes

1. **Literal actual vector:** pass. Equations (2.1) and (3.5) retain all
   four \(I_b\) factors; no arbitrary coefficient vector is substituted.
2. **CRT and lift multiplicity:** pass. \(M=8N\) gives one lift per pair
   \((x_8,y)\), exactly four local bases per admissible \(y\), and the factor
   \(4/M^4=2^{-10}N^{-4}\).
3. **One-count owners:** pass. The package is the intersection with the
   literal successive complement. The aligned \(R_*=4\) square is routed
   to Round 88, and literal \(u=0\) is absent. Nonzero \(8\mid u\) shifts
   remain alongside \(u\equiv4\pmod8\).
4. **Nonunit \(K\), full two-part, entry/exit:** pass. The \(8\)-phase is
   independent of \(K\) because \(A_8=B_{2,8}\); the odd trace retains
   \(\beta K\), including nonunits. Other two-parts remain outside this
   package. \(I_b\) and \(\Pi_{b,U}\) retain transitions, stars, hard
   endpoints, and zero extension, so the identity has transition cost
   exactly \(1\), not an unrecorded error term.
5. **Fejer density:** hostile control fails as a saving. If
   \(L=\lfloor(U-1)/4\rfloor\), the absolute local mass is
   \[
   2\sum_{h=1}^{L}(U-4h)=2LU-4L(L+1)\asymp U^2.
   \]
   The \(q=8\) restriction changes only a constant density. The alternating
   sign cannot be summed without controlling the \(u\)-dependent actual
   symbol and hard mask.
6. **Capacity and conductor ledger:** no target-safe gain. The actual row
   envelope is \(X^\varepsilon TQ^{-5/24}\), hence four rows carry
   \(X^\varepsilon T^4Q^{-5/6}\). The coefficient-blind Gram capacity is
   \[
   \mathsf C_U={U\over B}
   (B^3T^2Q^{-5/12})^2
   =UB^5T^4Q^{-5/6}.
   \]
   The desired ratio is
   \[
   {{(U/B)J^{14/5}}\over\mathsf C_U}
   ={J^{11/15}\over B^6},
   \]
   equal to \(J^{-1/6}\) at \(B=J^{3/20}\). The factors \(2^{-10}\), one
   quarter of the \(u\)-classes, and four Fourier modes do not alter this
   power. The \(b\asymp B\) sum therefore remains a scalar sum before the
   absolute value; a direct-sum norm cannot use it.
7. **False lower-bound shadows:** rejected. The local value
   \(\mathfrak T_8=-32\) at \(u\equiv4\pmod8\), full directed degree, paired
   trace cycles, or a post-absolute-value norm does not show that (2.1) is
   nonzero. No dense comparable archimedean plateau is proved.

## 6. Dependencies and exact artifacts used

- protocol.md.
- state/proof_obligations.yml, restricted to the three Round-100 target
  obligations and the accepted Round-89, Round-90, and Round-99 controls.
- state/active_campaign.yml.
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/briefs/actual_vector_parity_projection_attack.md.
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/derivation_packet.md.
- rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md.
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/synthesis.md.
- rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md.
- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/candidates/conductor_joint_four_row_self_return.md.
- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/synthesis.md.

No external theorem, web source, numerical experiment, or unselected
Round-100 report was used.

## 7. Recommended state effect

**Promote only the exact reduction; retain the analytic obligation open.**
Record (2.1), the normalization reconciliation (3.2)--(3.4), and the
generic cross-projection identity (3.5) as a strictly smaller
fixed-actual-vector survivor. Record also the no-go statement that the
aligned difference-of-squares mode has \(R_*=4\) and is already owned, while
the hard generic mode is a cross-projection and receives no power saving
from local trace size, lift sparsity, parity density, or paired cycles.

Do not promote a target-safe coherent package or an actual-vector
obstruction. Keep the canonical hard actual-vector directional estimate,
the canonical hard Gram estimate, the rest of GAR, blockwise M9-M1, M9-M2,
endpoint uniformity, M9, and the quarter theorem open.

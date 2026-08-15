# Round 17 synthesis: exact local reflection, but no pole or profile cancellation

Campaign: `m9-m1-local-reflection-eigenspaces`  
Round type: local reflection eigenspace attack  
Graph SHA-256 before patch: `7b1a14fc8a3b883b776da17467afd1a0895b744c36d3509988e912eb8bcf961c`

## Conductor decision

Promote the exact coefficient reflection cocycle, its normalized odd-part
eigenspaces, and the exact matching-profile projection. Promote the scoped
no-go that these eigenspaces remove neither generic arithmetic poles nor the
separate hard-top/height Mellin axes and do not manufacture the absent
reflected profile. Retain the maximal actual-profile angular-sign kernel and
GAR as open.

The proposed high-(2)-adic absolute tail has correct divisor algebra but
received conflicting seam verdicts. It depends on a pointwise definition
and uniform bound for the post-residue kernel (mathcal H_{T,X}) that Round
16 recorded only schematically. The conductor therefore retains that tail
as a conditional candidate rather than accepted mathematics. This avoids
silently replacing the open maximal correlation by a termwise bounded
Perron/BV kernel.

No numerical experiment or external theorem was used. No exponent region
and no theorem-level claim is promoted.

## Exact local reflection algebra

For

\[
 a_z(n)=\sum_{hq=n}\chi_4(q)(q/h)^{z/2},
 \qquad n=2^k m,\quad m\text{ odd},
\]

the condition (chi_4(q)\ne0) forces every factor (2^k) into (h).
Therefore

\[
 a_z(2^km)=2^{-kz/2}a_z(m).
\]

For odd (m), divisor exchange gives

\[
 a_{-z}(m)=\chi_4(m)a_z(m),
\]

and hence the exact cocycle

\[
 \boxed{a_{-z}(2^km)=\chi_4(m)2^{kz}a_z(2^km).}
\]

Equivalently, the normalized coefficients

\[
 b_z(2^km):=2^{kz/2}a_z(2^km)=a_z(m)
\]

satisfy

\[
 \boxed{b_{-z}(2^km)=\chi_4(m)b_z(2^km).}
\]

Thus ((b_z+b_{-z})/2) is supported on odd part (m\equiv1\pmod4),
and ((b_z-b_{-z})/2) on (m\equiv3\pmod4). Without this normalization,
the prime (2) rotates the two eigenspaces on (z=it); it supplies no
decay.

For odd (p), (epsilon_p=\chi_4(p)),

\[
 a_z(p^r)=p^{-rz/2}\sum_{j=0}^r(\epsilon_pp^z)^j,
 \qquad a_z(2^r)=2^{-rz/2}.
\]

These formulas independently verify multiplicativity, all prime powers,
and the ramified factor. The full Dirichlet series remains

\[
 F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4).
\]

The symmetric and antisymmetric series (F_z\pm F_{-z}) are sums of two
Euler products, not new Euler products in general.

## Pole and zero-mode verdict

For (z\ne0), (F_z\pm F_{-z}) have two distinct generic poles,

\[
 s=1-z/2,\qquad s=1+z/2,
\]

with residues (L(1-z,\chi_4)) and
(\pm L(1+z,\chi_4)), up to the chosen factor (1/2) in the projection.
Neither reflection eigenspace structurally cancels both poles. At (z=0),

\[
 a_0(n)=\sum_{q\mid n}\chi_4(q)=r_2(n)/4,
\]

the antisymmetric coefficient vanishes, and the symmetric coefficient is
the full Hardy return with its nonzero residue.

Near the double Mellin origin, the antisymmetric coefficient is
(O(u+v)), while the two endpoint transforms behave as (1/(uv)). Hence
only the joint double residue vanishes; the remaining expression is
(O(1/u+1/v)), so both axial poles survive. In particular, the hard
(u=0) residue samples (a_v^-\), which is not identically zero.

## Exact actual-profile projection

Write the Round-16 finite maximal kernel schematically as

\[
 \mathfrak M_T(X)=\sum_{hq\le N_X}\chi_4(q)(hq)^{-3/4}
 e(\sqrt{Xhq})\mathcal H_{T,X}(h,q).
\]

Since (q) is odd, write (h=2^kr), (m=rq), with (r,q,m) odd, and
put

\[
 \mathcal H^{[\epsilon]}_{T,k}(r,q)
 =\frac12\bigl(\mathcal H_{T,X}(2^kr,q)
 +\epsilon\mathcal H_{T,X}(2^kq,r)\bigr).
\]

Divisor exchange proves exactly

\[
 \sum_{rq=m}\chi_4(q)\mathcal H_{T,X}(2^kr,q)
 =\sum_{rq=m}\chi_4(q)
 \mathcal H^{[\chi_4(m)]}_{T,k}(r,q).
\]

The opposite profile eigenspace is identically invisible. This is an exact
algebraic projection, but it has norm one and therefore does not itself
save a power. Its surviving kernel is

\[
 \boxed{
 \sup_T\left|\sum_{k\ge0}2^{-3k/4}
 \sum_{\substack{m\le N_X/2^k\\m\text{ odd}}}
 m^{-3/4}e(\sqrt{2^kXm})
 \sum_{rq=m}\chi_4(q)
 \mathcal H^{[\chi_4(m)]}_{T,k}(r,q)
 \right|\ll_\varepsilon X^\varepsilon.}
\]

Exact reflection of the second profile would require

\[
 D'=2^k\frac{4X}{D}\ge2^k4\sqrt X,
\]

which is absent from the actual (D\le\sqrt X) family. The height divisor,
floor, (Phi), spatial profile, and endpoint convention also change.

## Conditional high-(2)-adic tail candidate

If one separately proves

\[
 B_X:=\sup_{T,h,q}|\mathcal H_{T,X}(h,q)|\ll\log X
\]

for a fully specified post-residue, symmetrically truncated BV/Perron
kernel, then elementary divisor summation gives

\[
 |\mathfrak M_T^{k\ge K}|
 \ll B_XN_X^{1/4}2^{-K}\log(2N_X).
\]

Thus (K=\lceil\log_2(2X^{1/8})\rceil) would make the tail
(O(\log^2X)). The exponent (2^{-K}) is validated. The required uniform
kernel bound, however, is not an accepted Round-16 lemma: one review derives
it from symmetric sine-integral/BV inversion, while the blind seam notes
that the schematic (mathcal H) has not been defined finely enough to
audit every remainder, residue subtraction, and abscissa uniformly. The
tail remains `derived_under_assumptions`, not `proved_internal`.

## State effect

- promote the local (2)-adic reflection cocycle and normalized support
  eigenspaces;
- promote the exact matching-profile projection and norm-one/no-pole no-go;
- retain the high-(2)-adic tail only under an explicit pointwise kernel
  hypothesis;
- retain the low/all-(2)-adic maximal kernel, GAR, M9-M1, M9-M2, M9, and
  the target as open.


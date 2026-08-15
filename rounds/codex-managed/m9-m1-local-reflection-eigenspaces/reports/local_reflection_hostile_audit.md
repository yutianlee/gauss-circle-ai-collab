# Local reflection hostile audit

## 1. Result

There is a promotable **local reflection cocycle**, but no global reflection eigenspace for the actual coefficients. If $n=2^k m$ with $m$ odd, then, for every $z\in\mathbb C$,

\[
\boxed{a_z(2^k m)=\chi_4(m)2^{-kz}a_{-z}(2^k m).}
\]

Thus odd $n$ are genuine reflection eigenvectors with eigenvalue $\chi_4(n)$, whereas the prime $2$ contributes a nonconstant factor. After the exact normalization

\[
b_z(2^k m):=2^{kz/2}a_z(2^k m),
\]

one has $b_z(n)=\chi_4(m)b_{-z}(n)$. Hence $(b_z+b_{-z})/2$ is supported on odd part $m\equiv1\pmod4$, and $(b_z-b_{-z})/2$ on $m\equiv3\pmod4$. This arithmetic splitting neither cancels the polar terms nor respects the actual M1 scale/height/profile operator.

## 2. Exact statement and hypotheses

Let

\[
a_z(n)=\sum_{hq=n}\chi_4(q)(q/h)^{z/2},\qquad
F_z(s)=\sum_{n\ge1}a_z(n)n^{-s}.
\]

Positive real powers use the real logarithm. The coefficients are multiplicative. For every prime power,

\[
a_z(p^r)=p^{-rz/2}\sum_{j=0}^r(\chi_4(p)p^z)^j.
\]

For $p\equiv1\pmod4$, $a_z(p^r)=a_{-z}(p^r)$. For $p\equiv3\pmod4$, $a_z(p^r)=(-1)^r a_{-z}(p^r)$. For $p=2$,

\[
a_z(2^r)=2^{-rz/2},\qquad a_{-z}(2^r)=2^{rz/2}.
\]

In the common absolute-convergence region, the Euler factors are

\[
F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4),
\]
\[
E_{2,z}=(1-2^{-s-z/2})^{-1},\qquad
E_{p,z}=\frac1{(1-p^{-s-z/2})(1-\chi_4(p)p^{-s+z/2})}\quad(p\text{ odd}).
\]

At $p\equiv3\pmod4$, $(E_{p,z}+E_{p,-z})/2$ contains exactly the even prime-power coefficients and the difference contains exactly the odd powers. At $p=2$, both projections are generally nonzero.

## 3. Proof or derivation

Because $\chi_4(q)=0$ for even $q$, writing $n=2^km$ gives

\[
a_z(2^km)=2^{-kz/2}a_z(m),\qquad
a_{-z}(2^km)=2^{kz/2}a_{-z}(m).
\]

For odd $m$, divisor exchange $h\leftrightarrow q$, together with
$\chi_4(h)\chi_4(q)=\chi_4(m)$, gives

\[
a_z(m)=\chi_4(m)a_{-z}(m).
\]

Combining these proves the boxed identity and the normalized projections. The prime-power and Euler-factor formulas follow by taking $q=p^j$.

The polar audit is hostile to cancellation. Since $L(s,\chi_4)$ is entire,

\[
\operatorname*{Res}_{s=1-z/2}F_z(s)=L(1-z,\chi_4),\qquad
\operatorname*{Res}_{s=1+z/2}F_{-z}(s)=L(1+z,\chi_4).
\]

For $z\ne0$, wherever these values are nonzero, $(F_z\pm F_{-z})/2$ has residues $L(1-z,\chi_4)/2$ and $\pm L(1+z,\chi_4)/2$ at the two distinct poles. At $z=0$, the antisymmetric part is zero but the symmetric part has residue $L(1,\chi_4)=\pi/4$. There is no structural zeta-pole cancellation; intact gamma factors add no separate residues beyond their trivial-zero cancellations.

For an incidence $hq=n$, the actual M1 symbol contains

\[
A_D(h,q)^u\Bigl(\frac{H_D+1}{h}\Bigr)^v,\qquad
A_D=\frac{D}{2\sqrt X}\sqrt{q/h}.
\]

Coefficient reflection instead produces

\[
A_{4X/D}(h,q)^{-u}\Bigl(\frac{H_D+1}{q}\Bigr)^v.
\]

It therefore requires $D\mapsto4X/D$, swaps the height variable, and changes the floor, $\Phi$, spatial profile, and endpoint star. Since actual $D\le\sqrt X$, the reflected scale is at least $4\sqrt X$ and is absent.

## 4. First doubtful or unproved step

The local lemma has no doubtful step. The first unproved leap is to move its symmetric/antisymmetric projection through the outside $(u,v,D)$ measure and treat that measure as reflection-invariant. It is not: doing so also crosses the zeta, height, and top $1/u$ Perron residues and replaces the actual profile by an absent one.

## 5. Required control test and outcome

All controls are exact.

* $n=2$: $a_z(2)=2^{-z/2}$ and $a_{-z}(2)=2^{z/2}$, refuting any global fixed-sign identity.
* $a_z(5)=5^{-z/2}+5^{z/2}$, while $a_z(7)=7^{-z/2}-7^{z/2}$; even among odd integers both eigensigns occur.
* The full $n=5$ coefficient is symmetric, but actual M1 contains the incidence $(h,q)=(1,5)$ and not its swap: their spatial locations are $2\sqrt{X/5}<\sqrt X$ and $2\sqrt{5X}>\sqrt X$. Thus coefficient symmetry does not imply profile symmetry.
* At $z=0$, the surviving residue $\pi/4$ is an exact counterexample to pole cancellation closing the radial problem.

Outcome: all proposed global cancellations fail; the local cocycle passes.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`, and the syntheses for `m9-m1-angular-mellin-separation`, `m9-m1-reflected-mode-correlation`, and `m9-combined-top-cones`. No other Round-17 artifact, external theorem, or numerical experiment was used.

## 7. Recommended state effect

Promote the boxed $2$-adically normalized local reflection lemma, including its prime-power/Euler-factor proof and support projections. Reject any implication that it cancels zeta/L residues, identifies an actual reflected M1 or M2 sector, or bounds the maximal angular-sign kernel. Retain GAR, top Perron correlation, M9-M1, M9, and the Gauss target as open.

## Addendum: tail lemma audit — PROMOTE

Promote the following scoped statement: for integers $K\ge0$, after all Round-16 residues have been removed and with the Perron truncation taken symmetrically,

\[
\sup_T\left|\sum_{\substack{hq\le N_X,\ q\ {\rm odd}\\v_2(hq)\ge K}}
\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})\mathcal H_{T,X}(h,q)\right|
\ll N_X^{1/4}2^{-K}\log^2(2X).
\]

Indeed the hard Perron piece is, up to its bounded half residue,
\[
\mathcal P_T(y)=\frac1\pi\int_0^T\frac{\sin(ty)}t\,dt,
\]
so $\sup_{T,y}|\mathcal P_T(y)|\ll1$; absolute integration of $1/u$ is neither needed nor valid uniformly in $T$. The fixed smooth Mellin remainders have uniform vertical $L^1$ norm. Any height remainder retaining a compensating $1/v$ tail must instead be kept as its symmetric BV inverse, which has the same uniform Dirichlet bound. There are $O(\log X)$ actual scales. Height floors merely switch incidences on or off, $\Phi$ and the fixed profiles are bounded, and endpoint stars have magnitude at most one. Consequently
\[
\sup_T|\mathcal H_{T,X}(h,q)|\ll\log(2X)
\]
uniformly, including equality at the hard spatial endpoint. This conclusion requires symmetric truncation and the post-residue/BV grouping; it would be false if justified by $\int_{-T}^T|du/u|$.

Finally $q$ is odd, hence $v_2(hq)\ge K$ is exactly $2^K\mid h$. Taking absolute values only in this tail,
\[
\begin{aligned}
\sum_{\substack{2^K\mid h\\hq\le N_X,\ q\ {\rm odd}}}(hq)^{-3/4}
&\ll N_X^{1/4}\sum_{\substack{h\le N_X\\2^K\mid h}}\frac1h\\
&\ll N_X^{1/4}2^{-K}\log(2N_X).
\end{aligned}
\]
Multiplication by the pointwise kernel bound proves the claim. If $2^K>N_X$ the tail is empty. Floors and endpoint conventions can only reduce this absolute majorant.

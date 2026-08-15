# Blind signed-packet rederivation

Campaign: `m9-endpoint-kernel-validation`  
Task: `blind_packet_rederivation`  
Role: statement-only blind rederiver  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`  
Generated: `2026-08-12T10:34:48+08:00`

## 1. Result and verdict

Write (e(t)=e^{2\pi i t}), and extend the real primitive character
modulo (4) by

\[
 \chi _4(n)=0\quad(2\mid n),\qquad
 \chi _4(n)=(-1)^{(n-1)/2}\quad(2\nmid n).
\]

Let (A\in C_c^\infty((0,\infty)^2)) be fixed and put

\[
 \mathcal T_A(R,L)=
 \sum_{h,k\geq 1}\chi _4(h)A(h/L,k/L)e(R\sqrt{hk}),
 \qquad 1\leq L\leq R^{1/2}.
 \tag{1.1}
\]

Thus (a(h,k)=A(h/L,k/L)) in the statement. If the project variable is
(X), then (R=\sqrt X), and an (R^\varepsilon) loss is interchangeable
with an (X^\varepsilon) loss after renaming (\varepsilon).

All four finite reductions in the brief are valid, with the following
qualification on the fourth one: a fixed smooth dyadic partition in the
gcd variable is required for the clean, rapidly localized packet formula.
A sharp gcd cutoff is possible only if its endpoint terms and non-absolutely
summable Fourier tails are retained; it does not give the packet formula
below for free.

More precisely:

1. For the unweighted product multiplicity (r_L(m)) defined in (2.1),
   \(\sum_m r_L(m)^2\ll_A L^2\log(2L)\).
2. Exact square products, and the larger-looking set
   \(\operatorname {dist}(\sqrt{hk},\mathbb Z)\leq R^{-1}\), have total
   absolute contribution (O_{A,\varepsilon}(L^{1+\varepsilon})). In the
   stated range, all nonsquare members of the latter set disappear once
   (L) exceeds a constant depending only on the support of (A).
3. The sector \((h,k)\geq L^{1/2}\), where here \((h,k)) denotes the gcd,
   has absolute contribution (O_A(L^{3/2})).
4. On a smooth shell (g=(h,k)\asymp G<L^{1/2}), writing
   (h=gu,k=gv,(u,v)=1), Poisson summation gives the exact signed difference
   of the (3/4)- and (1/4)-packets in (4.8). The order and factor are
   \(G(\mathcal Q_{3/4}-\mathcal Q_{1/4})/(2i)\).
5. The first unproved step is the fixed-shell signed packet estimate (5.3),
   or the direct \(\ell^1\)-aggregate condition (5.2). No estimate for the
   unsigned packet is proved or needed.

**Verdict:** promote/retain as internally proved finite infrastructure the
product energy, square/near-square disposal, large-gcd disposal, and exact
smooth signed-packet identity. Retain the target packet bound as open. These
reductions do not prove the endpoint estimate or (M9\)-(M2).

No external theorem and no numerical experiment are used.

## 2. Product energy

Choose fixed (0<c<C<\infty) such that the support of (A) is contained
in \([c,C]^2\), and define the enveloping multiplicity

\[
 r_L(m)=\#\{(h,k)\in\mathbb N^2:cL\leq h,k\leq CL,\ hk=m\}.
 \tag{2.1}
\]

Then

\[
 \sum_m r_L(m)^2
 =\#\{h_1k_1=h_2k_2:\ h_i,k_i\in[cL,CL]\}.
 \tag{2.2}
\]

Put (d=(h_1,h_2)), (h_1=du,h_2=dv), with ((u,v)=1). The equality in
(2.2) becomes (uk_1=vk_2), so coprimality gives

\[
 k_1=vn,\qquad k_2=un
 \tag{2.3}
\]

for some positive integer (n). If (M=\max(u,v)), both (d) and (n)
have (O(1+L/M)) possibilities. There are (O(M)) ordered pairs
((u,v)) with maximum (M), even before imposing coprimality. Therefore

\[
\begin{aligned}
 \sum_mr_L(m)^2
 &\ll_A\sum_{M\ll_A L}M(1+L/M)^2\\
 &\ll_A L^2+L^2\sum_{M\leq C_A L}\frac1M
 \ll_A L^2\log(2L).
 \tag{2.4}
\end{aligned}
\]

The same estimate holds for a weighted product coefficient
(r_{A,L}(m)=\sum_{hk=m}A(h/L,k/L)), with absolute square on the left,
because \(|r_{A,L}(m)|\leq\|A\|_\infty r_L(m)\).

## 3. Square, near-square, and large-gcd sectors

### 3.1 Exact squares

Let (s(n)) denote the squarefree kernel of (n). The product (hk) is a
square exactly when (s(h)=s(k)). It then has the unique form

\[
 h=su^2,\qquad k=sv^2,
 \tag{3.1}
\]

with (s) squarefree. For fixed (s\ll_A L), the number of possible
(u), and likewise (v), is (O_A(1+\sqrt{L/s})). Hence

\[
 \#\{h,k\in[cL,CL]:hk\text{ is a square}\}
 \ll_A\sum_{s\ll_A L}(1+L/s)
 \ll_A L\log(2L).
 \tag{3.2}
\]

Since \(|\chi _4(h)A(h/L,k/L)|\leq\|A\|_\infty\), their contribution is
(O_{A,\varepsilon}(L^{1+\varepsilon})) absolutely.

### 3.2 The (R^{-1}) near-square window

Let (m=hk\asymp_A L^2), and take (n\in\mathbb Z) nearest to
(\sqrt m). If

\[
 |\sqrt m-n|\leq R^{-1},
 \tag{3.3}
\]

then, using (R\geq L^2),

\[
 |m-n^2|=(\sqrt m+|n|)|\sqrt m-n|
 \ll_A L/R\leq C_A/L.
 \tag{3.4}
\]

For (L>C_A), the integer on the left is therefore zero, so (m=n^2).
For bounded (L), the whole sum has (O_A(1)) terms. Thus (3.2) proves
the same (O_{A,\varepsilon}(L^{1+\varepsilon})) absolute bound for the
near-square set. There is no hidden nonsquare near-resonant family at this
scale.

### 3.3 Gcd at least (L^{1/2})

The number of pairs in the support with ((h,k)\geq L^{1/2}) is at most

\[
 \sum_{g\geq L^{1/2}}^{CL}
 \#\{h\in[cL,CL]:g\mid h\}
 \#\{k\in[cL,CL]:g\mid k\}.
 \tag{3.5}
\]

Bounding each count by (O_A(1+L/g)) gives

\[
 \sum_{L^{1/2}\leq g\ll_A L}(1+L/g)^2
 \ll_A L^{3/2}+L\log(2L)+L
 \ll_A L^{3/2}.
 \tag{3.6}
\]

This proves the asserted absolute contribution. The same argument absorbs
any transition shell (g\asymp L^{1/2}) created by the smooth partition
below.

## 4. Exact smooth quarter-packet identity

Fix a smooth inhomogeneous dyadic partition on (g>0): apart from one
fixed (G=1) initial piece, its pieces have the form
(\Psi_G(g)=\Psi(g/G)), (G=2^j\), where
(\Psi\in C_c^\infty((1/2,2))). Arrange

\[
 \sum_G\Psi_G(g)=1\qquad(g\in\mathbb N).
 \tag{4.1}
\]

All shells meeting (g\gg L^{1/2}) are assigned to the already bounded
large-gcd sector. Thus the remaining shells satisfy (G<c_0L^{1/2}), for
a fixed (c_0>0), and carry no sharp truncation at (L^{1/2}).

On such a shell write uniquely

\[
 h=gu,\qquad k=gv,\qquad (u,v)=1.
 \tag{4.2}
\]

Complete multiplicativity, including the zero values on even integers,
gives

\[
 \chi _4(h)=\chi _4(g)\chi _4(u).
 \tag{4.3}
\]

In particular, the formula itself enforces that both (g) and (u) are
odd; there is no parity restriction on (v) beyond ((u,v)=1).

For fixed (u,v,G), set

\[
 F_{u,v;G}(t)=\Psi(t)
 A\!\left(\frac{Gtu}{L},\frac{Gtv}{L}\right).
 \tag{4.4}
\]

It is a compactly supported smooth function. On its nonempty range
(u,v\asymp_A L/G), its (C^j) norms are uniform in (u,v,G,L) for every
fixed (j). Use the Fourier normalization

\[
 \widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt
 \tag{4.5}
\]

and define a quarter packet by

\[
 \mathcal Q_{\alpha,G}[F](\theta)
 =\sum_{n\in\mathbb Z}\widehat F\bigl(G(n+\alpha-\theta)\bigr),
 \qquad \alpha\in\{1/4,3/4\}.
 \tag{4.6}
\]

The sums in (4.6) converge absolutely and rapidly. They are localized to
(\theta\) lying within (O(G^{-1})) of the shifted lattice
\(\mathbb Z+\alpha\).

The character identity and Poisson formula are

\[
 \chi _4(g)=\frac{e(g/4)-e(3g/4)}{2i},\qquad
 \sum_{g\in\mathbb Z}f(g)e(g\theta)
 =\sum_{n\in\mathbb Z}\widehat f(n-\theta).
 \tag{4.7}
\]

Applying (4.7) to (f(x)=F_{u,v;G}(x/G)), whose Fourier transform is
(G\widehat F_{u,v;G}(G\xi)), gives the exact formula

\[
\boxed{
\begin{aligned}
 &\sum_{g\in\mathbb Z}\chi _4(g)
 F_{u,v;G}(g/G)e(g\theta)\\
 &\qquad=\frac{G}{2i}
 \left(
 \mathcal Q_{3/4,G}[F_{u,v;G}](\theta)
 -\mathcal Q_{1/4,G}[F_{u,v;G}](\theta)
 \right).
\end{aligned}}
 \tag{4.8}
\]

To check the order of the shifts directly, the first term before
reindexing is
\(\widehat F(G(n-\theta-1/4))\), which becomes the (3/4)-packet after
(n\mapsto n+1); the (3/4) character exponential similarly becomes the
(1/4)-packet. Hence the sign in (4.8) is
(\mathcal Q_{3/4}-\mathcal Q_{1/4}), not the reverse.

Let a dagger on a sum over (u,v) mean that ((u,v)=1), that the support
in (4.4) is nonempty, and that (uv) is not a square. The last condition
removes exactly the already-treated square products, because (g^2uv) is
a square exactly when (uv) is a square (and, under coprimality, exactly
when (u) and (v) are separately squares). Define

\[
\begin{aligned}
 \mathscr P_G(R,L)=\sum_{u,v}^{\dagger}\chi _4(u)
 \bigl(&\mathcal Q_{3/4,G}[F_{u,v;G}](R\sqrt{uv})\\
       &-\mathcal Q_{1/4,G}[F_{u,v;G}](R\sqrt{uv})\bigr).
 \tag{4.9}
\end{aligned}
\]

Then the nonsquare part of the original (G)-shell is exactly

\[
 \boxed{\mathcal T_G(R,L)=\frac{G}{2i}\mathscr P_G(R,L).}
 \tag{4.10}
\]

Every factor (G), sign, parity restriction, and Fourier normalization in
the requested packet is explicit in (4.3)--(4.10).

## 5. Exact target scale and shell summation

After first disposing of squares/near-squares and then the large-gcd and
transition sectors, the decomposition yields

\[
 |\mathcal T_A(R,L)|
 \ll_{A,\varepsilon}L^{1+\varepsilon}+L^{3/2}
 +\sum_{G<c_0L^{1/2}}|\mathcal T_G(R,L)|.
 \tag{5.1}
\]

By (4.10), a sufficient estimate with no cancellation assumed between gcd
scales is

\[
 \boxed{
 \sum_{G<c_0L^{1/2}}G\,|\mathscr P_G(R,L)|
 \ll_{A,\varepsilon}L^{3/2}X^\varepsilon.}
 \tag{5.2}
\]

Up to the harmless factor (1/2), (5.2) is the weakest direct
\(\ell^1\)-in-shell packet statement. A convenient fixed-shell version is

\[
 \boxed{
 |\mathscr P_G(R,L)|
 \ll_{A,\varepsilon}\frac{L^{3/2}}G X^\varepsilon,
 \qquad 1\leq G<c_0L^{1/2}.}
 \tag{5.3}
\]

There are (O(\log(2L))) shells, and this logarithm is absorbed into
(X^\varepsilon), so (5.3) implies (5.2) with the conventional renaming of
(\varepsilon). The factor (G^{-1}) in (5.3) is forced by the leading
factor (G) in (4.10).

For clarity, the literally weakest aggregate signed assertion would be

\[
 \left|\sum_G\frac{G}{2i}\mathscr P_G(R,L)\right|
 \ll L^{3/2}X^\varepsilon,
 \tag{5.4}
\]

which allows cancellation between different (G). It is not equivalent to
(5.2): always

\[
 \left|\sum_G\mathcal T_G\right|
 \leq\sum_G|\mathcal T_G|,
 \tag{5.5}
\]

and the reverse inequality is false in general. The fixed-(G) research
interface requested by the brief is (5.3); it deliberately does not spend
unproved inter-shell cancellation.

No bound in (5.2)--(5.4) is proved here. They are exact formulations of the
first remaining analytic step.

## 6. Sharp-cutoff audit

The smoothness of (\Psi) is not cosmetic. With it,
(\widehat F(\xi)\ll_{A,J}(1+|\xi|)^{-J}) for every (J), uniformly on
active (u,v,G), so each expression in (4.6) is a genuine localized packet
and Poisson summation is termwise legitimate.

If (\Psi) is replaced by the sharp indicator of a gcd interval, the
resulting (F) has jumps. Its Fourier transform has boundary terms of size
(1/|\xi|), the dual sum is not absolutely convergent, and Poisson requires
an endpoint convention or a symmetric limiting prescription. Such a sharp
decomposition can be used in principle, but only after adding and estimating
those boundary/tail terms. Therefore a clean use of (4.8)--(5.3) requires a
fixed smooth gcd partition. No target-scale sharp-to-smooth transfer is
inferred here.

## 7. Required controls

### 7.1 Parity and sign control: passed

For (g\bmod 4=0,1,2,3), the numerator
(e(g/4)-e(3g/4)) is respectively (0,2i,0,-2i). Thus (4.7) is exactly
(2i\chi _4(g)): even (g) vanish, (g\equiv1\pmod4) has sign (+), and
(g\equiv3\pmod4) has sign (-). Together with complete
multiplicativity, this checks (4.3) and the sign in (4.8).

### 7.2 Signed versus unsigned control: passed

The two packets must remain inside one signed difference and the outer
(\chi _4(u)) must remain in (4.9). Taking absolute values packet by
packet or term by term is a strictly stronger, character-blind problem.
If (\chi _4(g)) is replaced by the unsigned coefficient (1), Poisson
gives a single integer packet

\[
 G\sum_n\widehat F(G(n-R\sqrt{uv})),
 \tag{7.1}
\]

not the quarter-packet difference. For arbitrary signs in (g), no fixed
two-packet formula exists at all. Hence the identity does not prove an
unsigned or adversarial analogue.

### 7.3 Square control: passed

The elementary squarefree-kernel count gives the requested absolute square
bound independently of any packet cancellation. Under ((u,v)=1), the
square condition is exactly (u=U^2,v=V^2), so the dagger restriction in
(4.9) removes precisely the already-counted class. No square term is lost
or counted as evidence for the packet estimate.

### 7.4 Proves-too-much control: passed

The proof uses only the prescribed periodic character and fixed smooth
symbol. It does not establish (5.3) for arbitrary bounded coefficients,
for the unsigned sum, or for a sharp gcd shell. In particular, rapid packet
localization comes from the fixed smooth partition, while signed
cancellation can come only from the exact (1/4,3/4) difference and the
outer (\chi _4(u)).

### 7.5 Shell-sum control: passed

Equation (5.5) records the one permissible implication. A bound on the
combined signed shell sum cannot be silently promoted to the
sum-of-absolute-shells estimate (5.2).

## 8. First doubtful or unproved step

For fixed (A) and the smooth partition above, the derivations through
(4.10) are finite counting or exact Poisson identities. The first unproved
analytic statement is the signed small-gcd packet estimate (5.3), or (5.2)
if one wants the weakest no-inter-shell-cancellation formulation.

If a sharp gcd cutoff is insisted upon, an earlier doubtful seam appears:
one must prove a target-scale bound for its endpoint terms and (1/|\xi|)
Fourier tails. That seam is absent for the fixed smooth partition.

## 9. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-endpoint-kernel-validation/briefs/blind_packet_rederivation.md`
- `rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md`

The Round-6 claimant report was not read. No web source, external theorem,
or computational artifact was used.

## 10. Recommended state effect

- **Promote or retain as proved internal:** (2.4), the square and
  (R^{-1})-near-square absolute bound, (3.6), and the exact smooth packet
  identity (4.8)--(4.10), subject to an independent seam comparison.
- **Retain open:** the signed packet target (5.3)/(5.2), endpoint uniformity,
  and the full (M9\)-(M2) estimate.
- **Reject as unsupported:** replacing the signed packet by its unsigned
  absolute majorant, reversing (\sum_G|\mathcal T_G|) and
  \(|\sum_G\mathcal T_G|), or using a sharp gcd cutoff while discarding
  its boundary and Fourier-tail terms.

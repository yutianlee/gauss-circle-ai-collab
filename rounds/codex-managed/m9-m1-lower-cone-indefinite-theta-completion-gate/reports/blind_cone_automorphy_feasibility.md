# 1. Result: lemma or no-go result

**Lemma (completed one-sided cone, scalar transform, and fixed-centre survivor).** Put \(q=e(\tau)\). The series in (144.B1) is not by itself a scalar holomorphic modular form. Its exact status is

\[
F(\tau)+\frac14
=\frac12\sum_{n\in\mathbb Z}\frac{q^{4n^2+n}}{1+q^{2n}},
\tag{1.1}
\]

the holomorphic part of a weight-one completed signature-\((1,1)\) theta function on \(\Gamma_0(4)\) with character \(\chi_4\). The \(1/4\) is the forced rational-isotropic-boundary term. The completion is

\[
\widehat H(\tau)=F(\tau)+\frac14+\mathcal R(\tau),
\tag{1.2}
\]

where, for \(y=\Im\tau\),

\[
\mathcal R(\tau)
=\frac14\sum_{\substack{h,r\in\mathbb Z\\r\ {\rm odd}}}
\chi_4(r)
\left\{
E\!\left(\frac{(r-4h)\sqrt y}{2}\right)
-\operatorname {sgn}(r-4h)
\right\}q^{hr},
\qquad
E(u)=2\int_0^u e^{-\pi t^2}\,dt.
\tag{1.3}
\]

It obeys

\[
\widehat H\!\left(\frac{a\tau+b}{c\tau+d}\right)
=\chi_4(d)(c\tau+d)\widehat H(\tau)
\quad
\left(\begin{matrix}a&b\\c&d\end{matrix}\right)\in\Gamma_0(4).
\tag{1.4}
\]

Thus the scalar level is \(4\), the weight is \(1\), and the multiplier is exactly the nebentypus \(\chi_4(d)\), with no eta multiplier. If one insists that the holomorphic part be exactly \(F\), then \(F+\mathcal R\) has the affine law

\[
(F+\mathcal R)(\gamma\tau)
=\chi_4(d)(c\tau+d)(F+\mathcal R)(\tau)
+\frac{\chi_4(d)(c\tau+d)-1}{4}.
\tag{1.5}
\]

The precise classification is therefore: a boundary-subtracted indefinite theta/Appell--Lerch series whose boundary-restored version is a weight-one mixed mock modular form, namely the holomorphic part of (1.2). It is not a holomorphic modular form and not merely a unary false theta. At roots of unity the Lambert denominators can vanish, so no unregularized global quantum-modular classification follows.

The strongest scalar-closed coefficient transform furnished by this automorphy is the exact heat identity (2.14) below. It keeps one complex additive direction and contains both the cusp constant and \(\mathcal R\); deleting either is unlawful.

For the application, the hard mask is affordable. Uniformly for \(M\ll R^2\asymp N^{1/2}\),

\[
\#\{m\in[M,2M):|k_m^2-Nm|\leq\sqrt M\}
\ll_\varepsilon M^{1/2}N^\varepsilon.
\tag{1.6}
\]

Consequently, for the usual disjoint dyadic convention,

\[
\mathfrak T_N=\mathcal S_N^++O_{\varepsilon,V}(N^\varepsilon),
\tag{1.7}
\]

where the strictly smaller, owner-complete survivor is

\[
\boxed{
\mathcal S_N^+
:=\sum_{1\leq m\leq M_*}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(+\sqrt{Nm})
}
\tag{1.8}
\]

or, equivalently,

\[
\mathcal S_N^+
=\sum_{\substack{h\geq1,\ r>4h,\ r\ {\rm odd}\\hr\leq M_*}}
\chi_4(r)(hr)^{-3/4}V_{\rm low}(R^2hr/N)e(+\sqrt{Nhr}).
\tag{1.9}
\]

No estimate \(\mathcal S_N^+\ll N^\varepsilon\) is proved. The first exact obstruction is that the modular transform of the holomorphic coefficients is not coefficient-only: it contains the mixed-shadow term \(\mathcal R\), whose uniform absolute capacity at coefficient-extraction height \(y\asymp M^{-1}\) is \(O(M)\), enough to reproduce the trivial normalized block capacity \(M^{1/4}\). Replacing the \(+\) direction by a real part would be a second independent gap.

# 2. Exact statement and hypotheses

Let

\[
L=\mathbb Z^2,\qquad
Q(h,r)=hr,\qquad
B((h,r),(h',r'))=hr'+rh'.
\tag{2.1}
\]

The Gram matrix is \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), so \(L\) is the even unimodular hyperbolic plane of signature \((1,1)\). Set

\[
c_1=(1,-4),\qquad c_0=(0,-1),\qquad b_0=(1/4,0).
\tag{2.2}
\]

Then

\[
Q(c_1)=-4,\quad Q(c_0)=0,\quad
B(c_1,(h,r))=r-4h,\quad B(c_0,(h,r))=-h,
\tag{2.3}
\]

and

\[
\chi_4(r)
=\frac{e(B((h,r),b_0))-e(-B((h,r),b_0))}{2i}.
\tag{2.4}
\]

Thus (2.4) imposes both odd \(r\) and its sign. Equivalently, with \(L_4=\mathbb Z\times4\mathbb Z\), it is the signed difference of the cosets \((0,1)+L_4\) and \((0,3)+L_4\).

Use \(\operatorname {sgn}(0)=0\), and define

\[
\kappa_0(h,r)
=\frac12\{\operatorname {sgn}h+\operatorname {sgn}(r-4h)\}
-\frac12\mathbf 1_{h=0}\operatorname {sgn}r.
\tag{2.5}
\]

The exact lattice/coset realization is

\[
F(\tau)
=\frac12\sum_{a\in\{1,3\}}\chi_4(a)
\sum_{x\in(0,a)+L_4}\kappa_0(x)e(Q(x)\tau).
\tag{2.6}
\]

The unsubtracted sign kernel

\[
\rho(h,r)
=\frac12\{\operatorname {sgn}h+\operatorname {sgn}(r-4h)\}
=\frac12\{\operatorname {sgn}B(c_1,x)-\operatorname {sgn}B(c_0,x)\}
\tag{2.7}
\]

is understood on \(h=0\) by radial/Abel regularization. Its signed theta is \(2F+1/2\), hence half of it is \(F+1/4\). There is no \(r=4h\) lattice boundary because \(r\) is odd.

The correction (1.3) converges absolutely and locally uniformly. Its mixed unary shadow is

\[
\frac{\partial}{\partial\overline\tau}\widehat H(\tau)
=\frac{i}{16\sqrt y}
\sum_{\mu\in\{1,3,5,7\}}
\Theta_\mu(\tau)\overline{G_\mu(\tau)},
\tag{2.8}
\]

where

\[
\Theta_\mu(\tau)=\sum_{n\equiv\mu\ (8)}q^{n^2/16},
\qquad
G_\mu(\tau)=\chi_4(\mu)\widetilde G_\mu(\tau),
\qquad
\widetilde G_\mu(\tau)=\sum_{n\equiv\mu\ (8)}nq^{n^2/16}.
\tag{2.9}
\]

The \(\Theta_\mu\) form the weight-\(1/2\) Weil vector for the finite quadratic module
\((\mathbb Z/8\mathbb Z,\mu\mapsto\mu^2/16)\), of level \(16\):

\[
\Theta_\mu(\tau+1)=e(\mu^2/16)\Theta_\mu(\tau),
\qquad
\Theta_\mu(-1/\tau)
=\frac{\sqrt{-i\tau}}{\sqrt8}
\sum_{\nu\ (8)}e(-\mu\nu/8)\Theta_\nu(\tau).
\tag{2.10}
\]

The full vector \((\widetilde G_\mu)_{\mu\ (8)}\) is the corresponding Jacobi-derivative unary vector of weight \(3/2\), with its standard metaplectic Weil multiplier and level \(16\). The \(G_\mu\) in (2.8) are its fixed \(\chi_4(\mu)\)-weighted contraction over odd components, not four independent scalar forms. Formula (2.8), including \(y^{-1/2}\), is the complete mixed shadow; there is no additional holomorphic unary correction.

At infinity,

\[
F(iy)=O(e^{-10\pi y}),\qquad
\mathcal R(iy)=O(y^{-1/2}e^{-\pi y/4}),\qquad
\widehat H(iy)=\frac14+O(y^{-1/2}e^{-\pi y/4}).
\tag{2.11}
\]

At the other cusps \(0\) and \(1/2\), the constant terms of the appropriate weight-one slash transforms are zero and the transforms decay exponentially. Indeed, \((0,\pm b_0)\) becomes \((\pm b_0,0)\) under \(S\), and \((\pm2b_0,\pm b_0)\) under \(\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)\); neither shifted pair has a surviving isotropic constant. Thus \(\widehat H\) has moderate growth at all cusps. At a cusp \(a/c\) equivalent to infinity, with \(c>0\), \(4\mid c\), its exact leading term is

\[
\widehat H(a/c+iy)
=\frac{i\chi_4(d)}{4cy}
+O\!\left(\frac1{cy}(c^2y)^{1/2}e^{-\pi/(4c^2y)}\right),
\quad ad\equiv1\pmod c,\quad y\downarrow0.
\tag{2.12}
\]

There is no elliptic residue at this specialization: \(1+q^{2n}\neq0\) in the upper half-plane, and the \(n=0\) denominator is \(2\). The latter is exactly the isotropic \(1/4\) boundary contribution after halving.

For \(m=2^\alpha n\) with \(n\) odd,

\[
C(m)=
\sum_{\substack{d\mid n\\2^{\alpha+2}d^2<n}}
\chi_4(n/d),
\qquad |C(m)|\leq d(n)\leq d(m).
\tag{2.13}
\]

Finally, let \(a,b,c,d\in\mathbb Z\), \(c>0\), \(4\mid c\), and \(ad-bc=1\). Expanding (1.4) at \(a/c\) gives the exact individual-direction summation formula

\[
\begin{aligned}
\sum_{m\geq1}C(m)e(am/c)e^{-2\pi my}
={}&\frac{i\chi_4(d)}{cy}
\sum_{n\geq1}C(n)e(-dn/c)e^{-2\pi n/(c^2y)}\\
&+\frac{i\chi_4(d)}{4cy}-\frac14\\
&+\frac{i\chi_4(d)}{cy}
\mathcal R\!\left(-\frac dc+\frac{i}{c^2y}\right)
-\mathcal R\!\left(\frac ac+iy\right).
\end{aligned}
\tag{2.14}
\]

This is scalar-closed exactly for \(4\mid c\). At the other cusp classes, the lawful formula is vector-valued and involves the shifted characteristic components above; replacing them by \(C(n)\), or by a real/conjugate combination, is invalid. Smooth transforms follow from (2.14) by justified Laplace/Mellin superposition, but all four right-hand terms must remain.

# 3. Proof or derivation

## 3.1 Cone, opposite cone, and boundary

For \(h\neq0\), \(\rho\) is \(1\) on \(h>0,r>4h\), \(-1\) on \(h<0,r<4h\), and zero on the other sectors. Under \((h,r)\mapsto(-h,-r)\), the second cone maps to the first, while both \(\rho\) and \(\chi_4(r)\) change sign. Their product is unchanged, so the strict cones contribute two copies of \(F\). At \(h=0\), \(\rho(0,r)=\tfrac12\operatorname {sgn}r\); subtracting this gives (2.5)--(2.6).

Insert \(t^{|r|}\) on the isotropic line. Its paired boundary is

\[
\sum_{r\ {\rm odd}}\frac12\chi_4(r)\operatorname {sgn}(r)t^{|r|}
=\sum_{\substack{r\geq1\\r\ {\rm odd}}}\chi_4(r)t^r
=\frac{t}{1+t^2}\longrightarrow\frac12.
\tag{3.1}
\]

Thus the canonical sign theta is \(2F+1/2\), proving the \(1/4\) in (1.1)--(1.2).

## 3.2 Lambert/Appell realization

Write \(r=4h+s\) in the positive cone. Then \(s>0\) is odd and \(\chi_4(r)=\chi_4(s)\), so

\[
F(\tau)
=\sum_{h\geq1}q^{4h^2}
\sum_{\substack{s\geq1\\s\ {\rm odd}}}\chi_4(s)q^{hs}
=\sum_{h\geq1}\frac{q^{4h^2+h}}{1+q^{2h}}.
\tag{3.2}
\]

The summand is invariant under \(h\mapsto-h\), and its \(h=0\) value is \(1/2\), proving (1.1). If

\[
A_4(u,v;\sigma)
=e(2u)\sum_{n\in\mathbb Z}
\frac{e(\sigma)^{2n(n+1)}e(nv)}
{1-e(u)e(\sigma)^n},
\tag{3.3}
\]

then the bilateral series is exactly \(A_4(1/2,-3\tau;2\tau)\). This is the torsion-specialized level-four Appell realization; the lattice argument fixes its easily missed isotropic constant.

## 3.3 Completion, modularity, shadow, and cusps

The negative vector \(c_1\) is completed by replacing
\(\operatorname {sgn}B(c_1,x)\) with
\(E(B(c_1,x)\sqrt{y/(-Q(c_1))}) )\). Since \(-Q(c_1)=4\), this gives (1.3). The rational isotropic vector \(c_0\) remains a sign kernel, regularized by (3.1). Halving the two-cone theta gives (1.2).

The correction is absolutely convergent. The bound

\[
|E(u)-\operatorname {sgn}u|\leq e^{-\pi u^2}
\tag{3.4}
\]

is enough, because

\[
e^{-\pi y(r-4h)^2/4}|q^{hr}|
=\exp\{-\pi y(r^2/4+4h^2)\}.
\tag{3.5}
\]

It follows uniformly in \(x\) that

\[
|\mathcal R(x+iy)|\ll
\begin{cases}
y^{-1},&0<y\leq1,\\
y^{-1/2}e^{-\pi y/4},&y\geq1.
\end{cases}
\tag{3.6}
\]

Direct Poisson summation for this completed kernel on the even unimodular plane gives weight \(1\). The twist is the difference of characteristic pairs \((0,b_0)\) and \((0,-b_0)\). Under
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), a pair transforms as
\((\alpha,\beta)\mapsto(a\alpha+c\beta,b\alpha+d\beta)\). If \(4\mid c\), then \(cb_0\in L\), while \(db_0\equiv\pm b_0\pmod L\) with sign \(\chi_4(d)\). Since \(Q(b_0)=0\), no further phase occurs. This proves (1.4). The denominator of \(b_0\) is exactly \(4\), and \(S\) sends it to a nontrivial shift, so this component has no lower scalar congruence level.

Differentiating (1.3) gives

\[
\partial_{\bar\tau}\widehat H
=\frac{i}{16\sqrt y}
\sum_{\substack{h\in\mathbb Z\\r\ {\rm odd}}}
\chi_4(r)(r-4h)e^{-\pi(r-4h)^2y/4}q^{hr}.
\tag{3.7}
\]

Write \(r=4(h+j)+s\), \(s=\pm1\), and \(a=4j+s\). Since

\[
4h^2+ah=4(h+a/8)^2-a^2/16,
\tag{3.8}
\]

(3.7) factors as

\[
\frac{i}{16\sqrt y}
\sum_{\mu\ {\rm odd}\ (8)}
\left(\sum_{n\equiv\mu(8)}q^{n^2/16}\right)
\overline{
\left(\sum_{a\equiv\mu(8)}\chi_4(a)a q^{a^2/16}\right)},
\tag{3.9}
\]

which is (2.8). This is a genuine mixed unary shadow, not the shadow of a scalar harmonic Maass form, and accounts for all nonholomorphic/unary terms.

Only the original \(h=0\) characteristic has the Abel constant (3.1). The shifts at \(0\) and \(1/2\) kill it, yielding the cusp assertions. There are no Appell poles at the chosen specialization, hence no residue term.

## 3.4 Coefficients and exact scalar summation

If \(m=2^\alpha n\), \(n\) odd, and \(hr=m\) with \(r\) odd, then \(h=2^\alpha d\), \(d\mid n\), and \(r=n/d\). The cone inequality is \(n/d>4\cdot2^\alpha d\), proving (2.13).

For (2.14), set

\[
z=-\frac dc+\frac{i}{c^2y}.
\tag{3.10}
\]

Then \(\gamma z=a/c+iy\) and \(cz+d=i/(cy)\). Insert these into (1.4), expand \(\widehat H=F+1/4+\mathcal R\) at both points, and use the \(q\)-series for \(F\). No conjugation or real part is taken: the dual direction is exactly \(e(-dn/c)\) with factor \(i\chi_4(d)/(cy)\).

## 3.5 Mask, endpoints, and the \(R\)-\(M\)-\(N\) ledger

The bounded range \(0<X<2\) is absorbed into the implied constant (and is empty when \(M_*<1\)); hence assume \(X\geq2\), so \(N\asymp X=R^4\).

Let

\[
\mathcal E_M=\{m\in[M,2M):|k_m^2-Nm|\leq\sqrt M\}.
\tag{3.11}
\]

For \(m\in\mathcal E_M\), set \(A=k_m^2-Nm\). Then \(|A|\leq\sqrt M\), while \(k_m\) lies in an interval of length \(O(\sqrt{NM})=o(N)\). For \(A\neq0\), the prime-power square-root bound and the Chinese remainder theorem give

\[
\#\{k\pmod N:k^2\equiv A\pmod N\}
\ll d(N)\sqrt{(A,N)}.
\tag{3.12}
\]

Also

\[
\sum_{1\leq|A|\leq\sqrt M}\sqrt{(A,N)}
\ll \sqrt M\sum_{d\mid N}d^{-1/2}
\ll_\varepsilon\sqrt M N^\varepsilon.
\tag{3.13}
\]

For \(A=0\), \(N\mid k^2\) is equivalent to
\(\prod_{p^v\parallel N}p^{\lceil v/2\rceil}\mid k\). This modulus is at least \(\sqrt N\), so the same \(k\)-interval contains \(O(1+\sqrt M)\) such integers. This proves (1.6).

Since \(|C(m)|\leq d(m)\) and \(V_{\rm low}\) is bounded, restoring the resonant set on one block costs

\[
\ll_{\varepsilon,V}
M^{-3/4}M^{1/2}N^\varepsilon
=M^{-1/4}N^\varepsilon.
\tag{3.14}
\]

This is summable over dyadic \(M\). The half-open dyadic intervals recombine exactly, so there is no hidden endpoint variation. Changing an endpoint convention affects \(O(1)\) integers per block and also costs \(O(N^\varepsilon)\). This proves (1.7).

The complete scale ledger, with \(N\asymp R^4\) and \(M\leq R^2\), is:

| item on \(m\asymp M\) | exact scale or lawful upper capacity |
|---|---:|
| absolute coefficient block after \(m^{-3/4}\) | \(M^{1/4+\varepsilon}\), at most \(R^{1/2+\varepsilon}=X^{1/8+\varepsilon}\) |
| restored hard-mask complement | \(M^{-1/4}N^\varepsilon\), dyadically summable |
| profile derivatives | \((R^2/N)^j\asymp R^{-2j}\) |
| phase derivative | \(\phi'(m)\asymp\sqrt{N/M}=R^2M^{-1/2}\) |
| phase curvature | \(|\phi''(m)|\asymp\sqrt N\,M^{-3/2}=R^2M^{-3/2}\) |
| formal stationary dual frequencies | \(K_M\asymp M|\phi''|\asymp R^2M^{-1/2}\) |
| one stationary integral after \(m^{-3/4}\) | \(M^{-3/4}|\phi''|^{-1/2}\asymp R^{-1}\) |
| raw absolute stationary capacity | \(K_M/R\asymp RM^{-1/2}\), equal to \(1\) only for \(M\asymp R^2\) |
| completion at \(y\asymp M^{-1}\) | \(|\mathcal R|\ll M\) |
| isotropic cusp term in (2.14) | \(1/(cy)\asymp M/c\) |

Thus the mask and dyadic boundaries are not the obstruction. The first automorphic obstruction occurs before any coefficient-only Voronoi estimate: (2.14) contains \(-\mathcal R(a/c+iy)\) with absolute capacity \(M\) at \(y\asymp M^{-1}\). Its cancellation against the holomorphic and transformed-shadow pieces is part of the missing theorem. Dropping it produces a false coefficient-only formula. Even after controlling it, the stationary ledger leaves a secondary small-\(M\) issue unless the support of \(V_{\rm low}\) is known to stay in \(M\asymp R^2\).

Finally, \(C(m)\) and \(V_{\rm low}\) are real, so \(\mathcal S_N^-=\overline{\mathcal S_N^+}\). A bound on \(2\Re\mathcal S_N^+\) does not bound \(|\mathcal S_N^+|\). Formulas (1.8) and (2.14) therefore retain one complex direction.

# 4. First doubtful or unproved step

The first unproved assertion needed for (144.B4) is

\[
\mathcal S_N^+\ll_{\varepsilon,V}N^\varepsilon.
\tag{4.1}
\]

The automorphic classification does not prove (4.1). Deriving it from (2.14) requires a justified complex Laplace/Fourier decomposition of
\(m^{-3/4}V_{\rm low}(R^2m/N)e(+\sqrt{Nm})\) and a joint estimate for both occurrences of \(\mathcal R\), including their mixed unary shadow (2.8). The first invalid shortcut is to discard \(\mathcal R\) as “nonholomorphic error”: (3.6) shows full trivial capacity at \(y\asymp M^{-1}\). The next invalid shortcut is to combine \(+\) and \(-\) and bound only a cosine/real part.

Thus (144.B4) remains open, but it is reduced to the mask-free, endpoint-free, exact signed survivor (1.8), with every boundary and completion liability explicitly assigned.

# 5. Required control tests and outcomes

1. **Coefficient/Lambert control — passed.** Direct enumeration gives \(C(5)=1,C(7)=-1,C(9)=1,C(18)=1\), agreeing with (3.2). The bilateral identity (1.1) was checked at \(\tau=0.13+0.7i\) to floating error below \(6\times10^{-26}\).

2. **Isotropic-boundary control — passed.** The Abel boundary is exactly \(t/(1+t^2)\to1/2\), forcing \(+1/4\) after halving. Omitting it gives the affine defect (1.5).

3. **Scalar modular controls — passed diagnostically.** Truncating (1.3) with stable complementary-error-function evaluation at \(\tau=0.13+0.7i\) gave

   \[
   |\widehat H(\tau/(4\tau+1))-(4\tau+1)\widehat H(\tau)|<1.2\times10^{-16},
   \]

   and for \(\gamma=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)\),

   \[
   |\widehat H(\gamma\tau)+(4\tau+3)\widehat H(\tau)|<5.3\times10^{-16},
   \]

   matching \(\chi_4(3)=-1\). These are diagnostic only; the proof is the Poisson/characteristic derivation.

4. **Other-cusp control — passed diagnostically.** Weight-one slash transforms at \(0\) and \(1/2\) numerically tend to \(0\), matching the shifted-characteristic proof of vanishing constants.

5. **Near-square control — passed.** The proof (3.12)--(3.14) is uniform for squareful \(N\). Enumerations for \(N=10007,10000,65536\) stayed within the \(O(\sqrt M)\) scale; square \(N\) realizes that scale, so it cannot be replaced by \(O(1)\).

6. **Unsigned/adversarial control — correctly fails.** Replacing \(\chi_4(r)\) by \(1\) makes both the two opposite cones and the symmetrically Abel-regularized isotropic line cancel, so the completed signed theta is zero rather than twice the desired one-sided unsigned cone. If one instead forces a one-sided/absolute boundary to prevent that cancellation, its mass is
   \(\sum_{r\geq1,\ r\ {\rm odd}}t^r=t/(1-t^2)\), which diverges as \(t\uparrow1\). Arbitrary signs also lack the finite characteristic (2.4), so level-four scalar stabilization fails.

7. **Individual-direction control — passed as a no-go check.** Formula (2.14) carries \(e(+am/c)\) to \(i\chi_4(d)e(-dn/c)/(cy)\), not to a real/conjugate average. Since \(2\Re z\) can vanish for nonzero \(z\), a cosine bound cannot certify (4.1).

# 6. Dependencies and exact artifacts used

Only these local artifacts were read:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/blind_statement.md.

No proof graph, campaign state, prior round, sibling report, claimant derivation, strategy file, or other local artifact was inspected. No external source was used. The finite numerical checks in Section 5 were generated independently from the displayed definitions and were not used as proof.

# 7. Recommended state effect

**Promote** the exact lattice/coset realization (2.6), the forced \(1/4\) boundary, the completion (1.2)--(1.4), the mixed unary shadow (2.8), the cusp/heat formula (2.14), and the near-square count (1.6), subject to an independent seam check of the completed-kernel Poisson normalization.

**Revise** any statement that \(F\) itself is a homogeneous scalar modular form or an ordinary coefficient-only mock modular form: the homogeneous object is \(F+1/4+\mathcal R\), while \(F+\mathcal R\) has the affine defect (1.5).

**Retain open** (144.B4). Give the next analytic owner the individual-direction survivor (1.8)/(1.9) together with the mandatory mixed-shadow liability in (2.14). **Reject** any route that drops \(\mathcal R\), ignores the \(1/4\) cusp term, silently identifies other-cusp vector components with the same \(C(n)\), or proves only a real/conjugate combination.

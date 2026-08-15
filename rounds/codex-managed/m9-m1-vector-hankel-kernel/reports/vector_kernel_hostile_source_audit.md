# Vector Hankel kernel hostile source audit

## 1. Result

**Promote only the exact completed functional equation and finite vector-kernel normalization; reject every bounded-shift extrapolation.** For
\[
F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4),
\]
the completion in Round 15 has conductor (4), root number (+1), and sends ((z,s)\mapsto(-z,1-s)). After radial reflection the non-residue term necessarily has a new dual index (m) and the coupled multiplier (G_v(1-s)K_z(1-s)). Neither audited primary source proves uniform large-(|\Im z|) control, removal of finite horizontal sides, or the hard-Perron maximal bound. No nonempty new uniform sector is source-certified.

## 2. Exact statement and hypotheses

Put
\[
C_z(s)=\pi^{-(s+z/2)/2}\Gamma\!\left(\frac{s+z/2}{2}\right)
\left(\frac4\pi\right)^{(s-z/2+1)/2}
\Gamma\!\left(\frac{s-z/2+1}{2}\right).
\]
Then (\Lambda_z=C_zF_z) satisfies
\[
\Lambda_z(s)=\Lambda_{-z}(1-s),\qquad
F_z(s)=K_z(s)F_{-z}(1-s),\quad
K_z(s)=\frac{C_{-z}(1-s)}{C_z(s)}.
\]
Thus, after (s\mapsto1-s), the exact reflected multiplier is (K_z(1-s)=C_{-z}(s)/C_z(1-s)), not its reciprocal. Initially expand only where
\(\Re s>1+|\Re z|/2\):
\[
F_{-z}(s)=\sum_{m\ge1}a_{-z}(m)m^{-s}.
\]
Every contour identity is first on finite (u,v,s) rectangles; zeta, height, spatial-Perron, and radial endpoint residues stay outside the vector remainder.

## 3. Proof or derivation

The standard zeta completion has sign (+1). Since (\chi_4) is primitive odd modulo (4), (\tau(\chi_4)=2i), so its root number (\tau(\chi_4)/(i\sqrt4)=1). Multiplication gives the displayed (C_z), with archimedean heights
\[
t+\Im z/2,\qquad t-\Im z/2.
\]
Hence gamma decay and phase change at the transition planes (t=\pm\Im z/2); fixed-order Stirling cannot be made uniform merely by assuming (z) bounded during a derivation and then integrating over unbounded (u+v).

For radial transform (G_v), the finite FE term is
\[
\sum_m a_{-z}(m)\frac1{2\pi i}\int
G_v(1-s)K_z(1-s)m^{-s}\,ds,
\]
plus finite horizontal sides. It is vector-valued in (m). The square-root phase and its (\pm\pi/4)-type stationary branches arise only after inverting the *complete* gamma/Bessel combination; choosing a single branch before this inversion can lose constants, signs, or the odd-character factor (i). Root number (+1) does not mean the individual oscillatory branches have equal positive phase.

Banerjee--Khurana Theorems 4.3--4.4 exactly match the odd primitive character and divisor coefficient, but require nonintegral finite endpoints, a test function analytic inside a closed contour containing the interval, and (0<\Re\nu<1/2). Their (J_\nu,Y_\nu,K_\nu) formula is fixed-order and gives no estimate uniform in (\Im\nu); it does not accept the hard top jump. Kiral--Zhou Theorem 1.3 requires its full Hecke system, moderate growth, and precise primitive-twist functional equations/analytic continuation. Its main proof is degree (N\ge3), degree (2) is a separate remark, and the present ramified polar Eisenstein product requires separate local and residue derivations. It supplies no three-height operator estimate.

## 4. First doubtful or unproved step

The first unproved step is replacing the finite (s)-rectangle by an infinite Hankel integral uniformly in (u,v), while discarding horizontal sides. Gamma decay is nonuniform near (\Im s=\pm\Im(u+v)/2); (G_v) also carries the hard radial cutoff. This precedes any claimed saddle localization in (m).

## 5. Required control test and outcome

Set (z=0). The completion becomes self-dual and (a_0=r_2/4), so the correctly normalized kernel must return the classical Hardy--Voronoi phase, not a smaller estimate. **Pass** for the gamma/root normalization; **fail** for any claim that bounded-shift localization proves GAR. Letting (|\Im z|\to\infty) then forces the two transition planes apart, exactly falsifying uniform extrapolation from a compact (z)-set.

## 6. Dependencies and exact artifacts used

Used the protocol, graph, active campaign; Round-15, 16, and 18 syntheses; the Round-15 hostile source audit; the Banerjee--Khurana and Kiral--Zhou source cards and local primary PDFs; and the assigned brief. No other Round-19 report or numerical experiment was used.

## 7. Recommended state effect

Promote the exact (C_z,K_z), root number, contour orientation, initial expansion chamber, dual-index necessity, and finite-horizontal-side scope as normalization infrastructure. Record a no-go against fixed-order/bounded-shift source import. Retain `M9-M1-post-FE-vector-kernel`, the high-(2)-adic reflected tail, maximal angular correlation, GAR, and all downstream targets as open.

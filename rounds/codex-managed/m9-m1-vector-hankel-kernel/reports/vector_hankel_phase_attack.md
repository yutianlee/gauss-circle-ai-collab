# Finite reflected vector Hankel phase attack

## 1. Result

At finite contour heights the post-functional-equation remainder has an
exact new dual index \(m\), and its vertical kernel is

\[
 \mathscr V_{j,\mathbf T}(m)=\frac1{(2\pi i)^3}
 \int_{\Gamma_u}\int_{\Gamma_v}\int_{\Gamma_s}
 A_j(u,v)G_v(1-s)K_{u+v}(1-s)m^{-s}\,ds\,dv\,du, \tag{V}
\]

with the finite \(s\)-horizontal sides retained separately. Here
\(A_j=\widehat W_j(u)\widehat\phi(v)
(D_j/(2\sqrt X))^u(H_j+1)^v\), and

\[
 K_z(1-s)=\frac{A_{-z}(s)}{A_z(1-s)},\qquad
 A_z(w)=2^{w+1-z/2}\pi^{-w-1/2}
 \Gamma\!\frac{w+z/2}{2}\Gamma\!\frac{w-z/2+1}{2}.
\]

All zeta, \(u=0\), \(v=0\), and radial endpoint residues remain outside
(V). For bounded \(|\Im z|\), stationary phase recovers the accepted two
degree-two waves \(e(\pm\sqrt{mx})\); only the minus wave can meet the
physical \(e(\sqrt{Xx})\), localizing
\[
 m=X+O(\sqrt{X/N})
\]
on a smooth radial shell \(x\asymp N\). This is the old near-product return,
not a saving.

For large \(\eta=\Im z\), uniform Stirling has transition lines
\(t=\pm\eta/2\), where \(s=\sigma+it\). Away from them, the conductor is
\[
 \mathcal C(t,\eta)=4(1+|t+\eta/2|)(1+|t-\eta/2|),
\]
and the phase depends on both factors separately. There is no uniform
replacement of the bounded-shift wave by \(e(\pm\sqrt{mx})\).
No target-sized nonempty sector follows without also bounding the outside
\((u,v)\) operator and finite horizontal sides.

## 2. Exact statement and hypotheses

Take finite symmetric lines
\(\Gamma_u=[a-iT_u,a+iT_u]\),
\(\Gamma_v=[b-iT_v,b+iT_v]\), \(a,b>0\), and initially
\(\Gamma_s=[c-iT_s,c+iT_s]\), with
\(c>1+|\Re(u+v)|/2\). Put
\[
 g_v(x)=x^{-3/4-v/2}e(\sqrt{Xx})\mathbf1_{1\le x\le N_X}^{*},
\quad G_v(w)=\int_0^\infty g_v(x)x^{w-1}\,dx.
\]
After shifting the radial rectangle and expanding
\(F_{-(u+v)}(s)=\sum_{m\ge1}a_{-(u+v)}(m)m^{-s}\),
the non-residue term is \(\sum_m a_{-z}(m)\mathscr V_{j,\mathbf T}(m)\).
The exact additional terms are the arithmetic residue
\(G_v(1-z/2)L(1-z,\chi_4)\), any radial-cutoff half residue, and the two
\(s\)-horizontal integrals connecting the original and terminal vertical
lines. Moving \(u\) or \(v\) later adds their already-recorded residues.

## 3. Proof and phase diagram

The completed functional equation gives (V) algebraically. Write
\(s=\sigma+it\), \(z=\zeta+i\eta\). Uniform Stirling is classical only when
\[
 |t+\eta/2|\gg1,\qquad |t-\eta/2|\gg1. \tag{S}
\]
In (S), each gamma ratio has its own Stirling phase; its logarithmic
derivative is, up to bounded errors,
\[
 \partial_t\arg K_z(1-s)
 =\log\!\left(\frac{\pi^2}
 {4\sqrt{|t+\eta/2|\,|t-\eta/2|}}\right)+O(\mathcal C^{-1/2}).
\]
Thus Mellin stationarity against \(m^{-s}x^{s-1}\) is controlled by the
product \(|t^2-\eta^2/4|\), while the sign chambers
\[
 t>\!|\eta|/2,\quad |t|<|\eta|/2,\quad t<-\!|\eta|/2
\]
choose different branches. For \(|\eta|=O(1)\), eliminating \(t\) yields
the two familiar Hankel phases \(e(\pm\sqrt{mx})\). Composing the minus
branch with \(e(\sqrt{Xx})\) gives phase
\[
 2\pi(\sqrt X-\sqrt m)\sqrt x+\theta_z,
\]
so repeated integration by parts outside
\(|\sqrt m-\sqrt X|\ll N^{-1/2}\), equivalently
\(|m-X|\ll\sqrt{X/N}\), proves rapid decay for smooth shells and bounded
\(z\).

There are three large-shift regimes:

1. **Outer Stirling:** both distances in (S) are large. The saddle and
amplitude vary with \(\eta\); bounded-shift localization is not uniform.
2. **Single transition:** \(|t-\eta/2|\lesssim1\) or
\(|t+\eta/2|\lesssim1\). One gamma factor is bounded-argument while the
other is large. Ordinary two-factor Stirling fails; the transition has
width \(O(1)\) in \(t\) and must be kept as a separate kernel.
3. **Double bounded:** possible only for \(|\eta|=O(1)\); this is covered
by fixed-order Hankel analysis.

Because the \(u\)-top is symmetrically maximal and \(\eta=\Im u+\Im v\),
the single-transition strips sweep every large \(u\)-height. They cannot be
discarded as a fixed compact error.

The horizontal \(s\)-sides contain \(G_v(1-\sigma\mp iT_s)\) times gamma
factors at \(T_s\pm\eta/2\). Smooth radial shells make them rapidly small
only when \(T_s\) stays uniformly separated from both transition lines and
dominates \(|\eta|\). No such domination is uniform as \(T_u\to\infty\);
the hard top \(1/u\) supplies no absolute decay. Hence finite sides must
remain part of the vector operator.

## 4. First doubtful or unproved step

No uniform transition estimate is proved that couples the swept strips
\(t\approx\pm\eta/2\) to the symmetric \(1/u\) maximal integral and then
sums the reflected coefficients. That is the first missing analytic step;
bounded-shift stationary phase cannot justify it.

## 5. Required control test and outcome

At \(\eta=0\), \(\mathcal C=4(1+|t|)^2\), the two branches reduce to
\(e(\pm\sqrt{mx})\), and the minus branch returns
\(m=X+O(\sqrt{X/N})\): pass. At \(t=\eta/2\), one archimedean height is
zero, directly falsifying a uniform use of large-argument Stirling in both
gamma factors. No numerical test was used.

## 6. Dependencies and exact artifacts used

Used only the Round-19 authorized packet: protocol, proof graph, active
campaign, Round-15 radial attack and synthesis, Round-16 synthesis/reports,
Round-18 synthesis, and the assigned brief. No web source was used.

## 7. Recommended state effect

Promote (V), its residue/horizontal-side ledger, the bounded-shift
near-product localization, and the three-regime conductor diagram as
finite-kernel infrastructure. Retain the swept single-transition operator
plus its horizontal sides as the smallest unestimated vector component.
Do not promote a target-sized sector, the high-\(2\)-adic tail, GAR, M9-M1,
or M9.

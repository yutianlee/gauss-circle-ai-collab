# Round 139 conductor candidate: exact curvature collar and quadratic-completion obstruction

## 1. Result

The Round-139 scalar has a strict, owner-complete displacement reduction.
Fix a sufficiently small absolute \(\rho>0\), put

\[
 L_h=\left\lfloor {\rho y\over\sqrt h}\right\rfloor ,
\qquad R=X^{1/4},\quad y=\lfloor\sqrt X\rfloor,\quad
N=\lfloor X\rfloor=y^2+q,
\tag{139.C1}
\]

and split the literal scalar into \(0\leq v\leq L_h\) and \(L_h<v<y\).
For either scalar sign, the first piece is

\[
 \mathcal C_N^\pm\ll R\log(2X).
\tag{139.C2}
\]

Consequently

\[
 \boxed{\mathcal F_N^\pm=\mathcal S_N^\pm+O(R\log(2X)),}
\tag{139.C3}
\]

where \(\mathcal S_N^\pm\) is the exact complementary scalar.  The
\(RX^\varepsilon\) target for \(\mathcal F_N^\pm\) is therefore equivalent
to the same target for \(\mathcal S_N^\pm\).  Combined only at the level of
logical target equivalence with Round 138, it is also equivalent to the
\(yX^\varepsilon\) bound for the accepted cross-denominator residual.

This does not estimate or delete a positive subpiece of the Round-138
square.  The displacement cutoff depends on the unreduced height and
splits lift aggregates; its square has an uncontrolled collar--tail cross
term.  The tail still has \(y^{1+o(1)}\) absolute scalar capacity.

The fixed-modulus Taylor core supplies a second, smaller target-safe
window, but not the full bound.  On the complement its exact correction
has polynomial variation; retaining that correction turns completion
into an invertible Fourier correlation, while taking moduli returns the
known \(y\) or \(R^{3/2}\) excess capacities.  The round should therefore
close under \(\mathsf{strict\_displacement\_quadratic\_reduction}\), with
the full quadratic-completion route recorded as obstructed.

## 2. Exact statement and hypotheses

Let \(X\geq2\) be real and let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,\qquad q=N-y^2.
\tag{139.C4}
\]

Then \(q\) is an integer and \(0\leq q\leq2y\).  Let
\(V_{\rm low}\) be the fixed real smooth lower profile with its literal
endpoint samples and zero extension.  There is a fixed \(C_V\) such that
a nonzero term forces

\[
 h\leq C_V{y-v\over R}\leq C_VR .
\tag{139.C5}
\]

For \(\sigma\in\{+1,-1\}\), define

\[
 \mathcal F_N^\sigma
 =\sum_{h\geq1}{1\over h}\sum_{0\leq v<y}
 \chi_4(y-v)
 V_{\rm low}\!\left({4R^2h^2\over(y-v)^2}\right)
 e\!\left(\sigma h{q+v^2\over y-v}\right).
\tag{139.C6}
\]

The map \(d\leftrightarrow v=y-d\) is a bijection between
\(1\leq d\leq y\) and \(0\leq v<y\).  Even \(y-v\) terms vanish.  On
the surviving parity lattice,

\[
 v=p_y+2n,\qquad p_y\equiv y-1\pmod2,
\tag{139.C7}
\]

and the complete phase is

\[
 \Psi_{\sigma,h}(v)
 =\sigma h{q+v^2\over y-v}+{y-v-1\over4}.
\tag{139.C8}
\]

Let \(\mathcal C_N^\sigma\) be (139.C6) restricted to
\(0\leq v\leq L_h\), including the literal integer endpoint, and let
\(\mathcal S_N^\sigma\) be its exact complement \(L_h<v<y\).  No profile
sample or boundary is omitted.  The negative scalar is the conjugate of
the positive scalar.

## 3. Proof of the exact curvature-collar estimate

Put

\[
 g(v)={q+v^2\over y-v}={N\over y-v}-y-v .
\tag{139.C9}
\]

The identity is exact and gives

\[
 g'(v)={N\over(y-v)^2}-1,\qquad
 g''(v)={2N\over(y-v)^3}.
\tag{139.C10}
\]

On \(0\leq v\leq L_h\), one has \(v\leq\rho y\) and hence
\(y-v\asymp_\rho y\).  Along (139.C7),

\[
 {d^2\over dn^2}\Psi_{\sigma,h}(p_y+2n)
 =\sigma {8hN\over(y-p_y-2n)^3},
\qquad
 \left|{d^2\over dn^2}\Psi_{\sigma,h}\right|
 \asymp_\rho {h\over y}.
\tag{139.C11}
\]

The second derivative has constant sign and bounded ratio on the whole
collar.  The elementary second-derivative lemma says that, if an interval
has length \(M\), \(f''\) has constant sign, and
\(\lambda\leq|f''|\leq A\lambda\leq A\), then

\[
 \sup_J\left|\sum_{n\in J}e(f(n))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2}.
\tag{139.C12}
\]

This follows by isolating the monotone derivative aliases and applying
the first-derivative lemma off intervals of radius
\(\lambda^{-1/2}\).  Abel summation preserves (139.C12) for an amplitude
with bounded supremum plus sampled variation.

For fixed \(h\), the profile amplitude in (139.C6) has uniformly bounded
sampled variation on the collar: its argument is monotone, the profile is
fixed and smooth, and literal zero extensions and the artificial collar
cut contribute only bounded endpoint jumps.  The number \(M_h\) of
allowed parity points satisfies

\[
 M_h\leq1+{L_h\over2}\ll1+{y\over\sqrt h},
\qquad \lambda\asymp {h\over y}.
\]

Equations (139.C11)--(139.C12) give

\[
 \left|\sum_{\substack{0\leq v\leq L_h\\y-v\ {\rm odd}}}
 V_{\rm low}\!\left({4R^2h^2\over(y-v)^2}\right)
 e(\Psi_{\sigma,h}(v))\right|
 \ll \sqrt y+\sqrt{y/h}+\sqrt{h/y}
 \ll \sqrt y+\sqrt{y/h}.
\tag{139.C13}
\]

The last absorption uses \(h\ll R\ll y\) outside a bounded range.
By (139.C5), only \(h\ll R\) occur.  Since \(\sqrt y\leq R\),

\[
 |\mathcal C_N^\sigma|
 \ll\sum_{h\ll R}{1\over h}
 \left(\sqrt y+\sqrt{y/h}\right)
 \ll R\log(2X).
\tag{139.C14}
\]

This proves (139.C2)--(139.C3), uniformly in \(q\), both parities, all
literal endpoints, and both signs.  It is a genuine estimate of the
unsquared scalar collar, not an aliaswise modulus on the survivor.

For a dyadic height block \(h\asymp H\), the deleted collar has weighted
absolute capacity \(yH^{-1/2}\), whereas (139.C13), after the
\(H\) heights and their \(H^{-1}\) weights cancel, costs
\(R+RH^{-1/2}\).  A generalized rowwise collar must retain the same
fixed top factor,
\(L_{\alpha,H}=\rho yH^{-\alpha}\), so that \(y-v\asymp_\rho y\);
the same method would then cost

\[
 R H^{1/2-\alpha}+R H^{-1/2}.
\tag{139.C15}
\]

Thus \(\alpha=1/2\) is the last power scale returned to \(R\) by this
rowwise curvature ledger.  A full top row at \(H=R\) costs
\(R^{3/2}\), in agreement with the accepted half-integer-alias capacity.

## 4. Exact quadratic core, legal Taylor window, and obstruction

The exact prescribed-centre decomposition is

\[
 {q+v^2\over y-v}
 ={q\over y}+{v^2\over y}
 +{v(q+v^2)\over y(y-v)},
\qquad
 E_{h,q,y}(v)=h{v(q+v^2)\over y(y-v)}.
\tag{139.C16}
\]

For \(v\leq y/2\),

\[
 0\leq E_{h,q,y}(v)
 \ll {hv\over y}+{hv^3\over y^2}.
\tag{139.C17}
\]

Hence, with a sufficiently small fixed constant,

\[
 \ell_h\asymp \min\left\{y,\left({y^2\over h}\right)^{1/3}\right\},
\tag{139.C18}
\]

the correction has bounded phase variation on \(0\leq v\leq\ell_h\);
the first term in (139.C17) is also bounded because \(h\ll\sqrt y\).
The literal Taylor-window scalar is target-safe by exact quadratic
completion.

Indeed, on \(v=p_y+2n\), the nonconstant core is

\[
 {8hn^2+(8hp_y-y)n\over2y}.
\tag{139.C19}
\]

Finite completion modulo \(2y\), including every gcd case and every
boundary frequency, gives complete quadratic Gauss sums bounded by

\[
 |G_{2y}(8h,C)|\leq\{2y(16h,2y)\}^{1/2}
 \ll \{y(h,y)\}^{1/2}.
\tag{139.C20}
\]

The bounded variation in (139.C17) gives only logarithmic completion
loss.  The actual height weight closes the gcd ledger:

\[
 \sum_{h\ll R}{(h,y)^{1/2}\over h}
 \leq \log(2y)\sum_{g\mid y}g^{-1/2}
 \ll_\varepsilon X^\varepsilon.
\tag{139.C21}
\]

Thus the Taylor window costs \(O_\varepsilon(RX^\varepsilon)\).  This is
strictly contained in the larger exact-curvature collar and is not the
reason (139.C2) holds.

The Taylor completion fails globally at its coefficient seam.  At the
fourth-power centres \(X=N=M^4\), \(R=M\), \(y=M^2\), \(q=0\),

\[
 E_{1,0,y}(v)={v^3\over y(y-v)}.
\tag{139.C22}
\]

Write \(v=ty\).  Then \(E=yF(t)\), where \(F(t)=t^3/(1-t)\).
Choose a fixed compact interval \(I\subset(0,1)\) on which
\(1/20\leq F'(t)\leq1/12\).  For the allowed parity step \(v\mapsto
v+2\), the mean-value theorem gives

\[
 {1\over10}\leq E(v+2)-E(v)\leq {1\over6}
\tag{139.C23}
\]

through a subinterval containing \(\asymp y\) samples, once \(M\) is
large.  Here the literal \(h=1\) profile is on its near-zero plateau.
Therefore

\[
 \operatorname{Var}\bigl(e(E_{1,0,y})\bigr)\gg y.
\tag{139.C24}
\]

So the exact correction is not a bounded-variation coefficient on the
full displacement range.  To state exact completion, put \(M=2y\), let
\(I_h\) be the literal allowed parity interval under discussion, and set

\[
 \begin{aligned}
 w_h(n)&={\bf1}_{p_y+2n\in I_h}
 V_{\rm low}\!\left({4R^2h^2\over(y-p_y-2n)^2}\right)
 e(E_{h,q,y}(p_y+2n)),\\
 \widehat w_h(k)&=\sum_{n\bmod M}w_h(n)e(-kn/M),\\
 C_h&={hq\over y}+{hp_y^2\over y}-{p_y\over4}+{y-1\over4}.
 \end{aligned}
\tag{139.C25a}
\]

The sequence is zero-extended modulo \(M\).  If the correction is retained
as a coefficient, exact completion is

\[
 e(C_h)\sum_{n\bmod M}w_h(n)
 e\!\left({8hn^2+(8hp_y-y)n\over M}\right)
 ={e(C_h)\over M}\sum_{k\bmod M}\widehat w_h(k)
 G_M(8h,8hp_y-y+k).
\tag{139.C25}
\]

The sign of \(k\) changes with the Fourier convention.  Coefficient-blind
\(L^2\) gives \(O(y)\) on a full active interval.  The raw
Fourier-\(\ell^1\) estimate may be worse when (139.C24) is inserted, so it
must be minimized with the trivial \(O(y)\) bound.  In either case there
is no improvement over the original \(y^{1+o(1)}\) scalar capacity.  If
the correction is instead retained as part of the oscillatory phase,
(139.C16) recombines exactly to \(hN/(y-v)\) modulo the discarded integer
\(h(y+v)\).  Fourier inversion returns the original reciprocal scalar.

There is no Salié sum at this seam.  The complete object in (139.C25) is
an additive quadratic Gauss sum; the varying reciprocal denominator,
the \(q\)-dependence, the literal profile, and the hard boundary remain
inside \(w_h\).  Exact character-Poisson retains all half-integer aliases,
the hard half-endpoint, transition terms, and nonstationary owners.  Its
principal-family absolute ledger remains \(R^{3/2}\log(2X)\), and a
second Legendre step returns the reciprocal phase.

## 5. First doubtful or unproved step

The first open estimate is

\[
 \boxed{|\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.}
\tag{139.C26}
\]

The survivor contains \(v>L_h\), hence all displacement sectors in which
the rowwise curvature term in (139.C15) would exceed the target.  Its
absolute capacity remains \(y^{1+o(1)}\).  A continuation must prove joint
signed cancellation across heights and physical half-integer aliases, or
estimate the exact Round-138 signed cross-denominator residual directly.

The Round-138 relation

\[
 |\mathcal F_N|^2=\mathcal R_{y^{-2}}
 +O_\varepsilon(yX^\varepsilon)
\tag{139.C27}
\]

and (139.C3) imply the chain of target equivalences

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{139.C28}
\]

They do not imply
\(|\mathcal S_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon)\):
the collar--tail cross term is not independently controlled.  In reduced
variables \(h=ag,d=bg\), the cutoff \(y-bg\leq L_{ag}\) depends on the
lift \(g\) and splits the exact \(L_\chi(y/b)\) coefficient.  This is the
precise directionality limit of the promoted reduction.

## 6. Required controls, dependencies, and outcomes

The exact \(q\)-range, the two-way displacement dictionary, both
\(y\)-parities, the mod-four carrier, both scalar signs, literal profile
support, zero extension, hard and terminal endpoints, and all real
centres are retained in (139.C4)--(139.C14).  The proof uses no numerical
experiment and no centre average.

The exact correction is retained in (139.C16); \(q=0\), \(q=2y\), the
fourth-power packet, the perturbative window, and terminal displacement
are separated.  Equations (139.C19)--(139.C25) record the modulus, gcd,
boundary-frequency, completion, variation, and self-return costs.
Equations (139.C15) and (139.C25) reproduce the \(R^{3/2}\) aliaswise and
\(y\) coefficient-blind capacities rather than converting them into
signed lower bounds.

The exact artifacts used are:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md;
- the Round-138 synthesis and conductor adjudication;
- the three primary Round-139 reports;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md.

The only analytic inputs are the elementary first- and second-derivative
lemmas and finite quadratic Gauss summation, each with its exact range and
cost displayed above.  No external theorem, symbolic experiment, or
desired circle estimate is imported.

## 7. Recommended state effect

After independent post-unmask verification, create one proved reduction:
the exact collar (139.C1)--(139.C3) is target-safe and leaves the literal
tail (139.C26), with only the scalar-level target equivalence
(139.C28) to the Round-138 residual.

Create or update one obstruction recording: the prescribed-centre Taylor
core has the target-safe window (139.C18), but the full correction has
the variation obstruction (139.C24); exact quadratic completion is the
invertible correlation (139.C25), while coefficient-blind or aliaswise
moduli retain \(y\) or \(R^{3/2}\) capacity.  Do not promote a Salié sum,
a full displacement bound, or a residual sub-square deletion.

Retain as open the lower-radial signed estimate, lower GAR, both direct
M1 parents, M9-M1, every M2 parent, endpoint uniformity, M9, the
conditional quarter theorem, and the target.  The strongest internally
proved exponent remains \(1/3\).

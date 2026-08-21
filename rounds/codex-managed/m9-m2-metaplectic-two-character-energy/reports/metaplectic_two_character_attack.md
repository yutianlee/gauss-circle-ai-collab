# Round 108 discovery report: metaplectic two-character attack

## 1. Result: exact factorization and a scoped equal-capacity no-go theorem

The Gaussian step can be completed exactly, with the metric density and all
metric discrepancies in one operator, but it supplies no power of \(\rho\).
The outcome is the following scoped no-go theorem.

Let \(e(z)=\exp(2\pi i z)\), and let \(F_a(q)\) be the literal zero-extended
Round-96 row, with \(b=a+2q\), \(h=ga\), \(s=gb\), every primitive and prior
owner, the open reciprocal interval, both orientations, all floors, stars,
physical collars, entry/exit samples and the complete metric window retained.
For \(\alpha\ne0\), put

\[
 K_\alpha(z)=
 {e(\operatorname {sgn}(\alpha)/8)\over\sqrt{2|\alpha|}}
 e\!\left(-{z^2\over4\alpha}\right),
 \qquad K_0=\delta_0,
\]

and let \(T_\alpha f=K_\alpha*f\).  With the Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(t)e(-t\xi)\,dt,
\]

one has, in tempered distributions,

\[
 \widehat K_\alpha(\xi)=e(\alpha\xi^2),\qquad
 T_\alpha^{-1}=T_{-\alpha},\qquad
 \|T_\alpha f\|_2=\|f\|_2,qquad K_\alpha\longrightarrow\delta_0
 \quad(\alpha\to0).
\]

For a literal configuration \(\xi=(a,q,g,k,\iota)\), where \(\iota\)
records the orientation and all finite profile labels, set

\[
 c_\xi={X\over2gk},\qquad y_\xi=\sqrt s-\sqrt h,
 \qquad c_\xi y_\xi^2={\Lambda_q\over k},
\]

and define the exact physical Fourier density

\[
 f_\xi(\beta)= {2\beta\over X}\,\omega_\xi
 A^\circ_{h,s}(\beta^2/X)
 e\!\left(k{\beta^2\over X}\right)
 \mathbf 1_{\{\beta^2/X\in[s/4,h]\}} .
\]

The indicator in this display carries the literal endpoint convention; the
amplitude carries the accepted flat collars and all transition samples.  Put

\[
 \mathcal M_{c,R}
   =\mu_R T_0+\sum_{r\ne0}\widehat W_R(r)T_{rc},
 \qquad \Psi_\xi=\mathcal M_{c_\xi,R}f_\xi .
\]

Then the complete density-plus-discrepancy factorization is

\[
 \boxed{
 F_a(q)=\mathbf P_{\rm lit}(a,q)
 \sum_{g,k,\iota}\operatorname {Os}\!\int_{\mathbb R}
 \Psi_\xi(\tau)e(\tau\sqrt h)e(-\tau\sqrt s)\,d\tau . }
\]

Here \(\mathbf P_{\rm lit}\) is the literal successive-complement owner,
not a smoothed substitute.  The oscillatory integral is defined by the Abel
regularization in Section 3.  The two characters enter the signed linear
vector exactly, because

\[
 \chi_4(h)\chi_4(s)=\chi_4(a)\chi_4(b)=(-1)^q.
\]

Thus \((-1)^qF_a(q)\) is an exact pairing of
\(\chi_4(h)e(\tau\sqrt h)\) and
\(\chi_4(s)e(-\tau\sqrt s)\), with the complete moving actual symbol
\(\Psi_\xi\) between them.

The representation is capacity preserving.  Exactly,

\[
 \widehat{\mathcal M_{c,R}f}(\eta)
   =W_R(c\eta^2)\widehat f(\eta),
\]

and hence

\[
 \boxed{
 \|\mathcal M_{c,R}f\|_2^2
 =\int_{\mathbb R}|W_R(c\eta^2)|^2|\widehat f(\eta)|^2\,d\eta,
 \qquad
 \|\mathcal M_{c,R}\|_{2\to2}=\|W_R\|_\infty . }
\]

The right side is the original metric-window capacity, not a new saving.
Modewise inversion gives back every original chirp, and Fourier inversion of
the summed operator gives back the original multiplier
\(W_R(\Lambda_q/k)\).  The density is \(T_0=I\); it is neither exceptional
nor removable.

There is a second exact obstruction in the fixed-\(a\) Gram.  If
\(\varepsilon_{a,q}=\chi_4(a)\chi_4(a+2q)=(-1)^q\) and
\(B_a(q)=\varepsilon_{a,q}F_a(q)\), then

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|\sum_{0\le j<H}B_a(n+j)\right|^2.
\]

On a shift \(v\), the multiplier that would be advertised as two-character
cancellation is identically

\[
 (-1)^v\,
 \varepsilon_{a,q+v}\varepsilon_{a,q}=1.
\]

Consequently the primitive character has constant autocorrelation in the
positive fixed-\(a\) Gram.  A direct signed linear two-character estimate and
the fixed-\(a\) Gram are different problems.

No complete Gram estimate and no fixed positive-power hard subrange follows.
The smallest surviving actual-vector inequality is the following
**complete owner-retaining square-root-vector Gram**:

\[
 \boxed{
 \sum_{a,n}\left|\sum_{0\le j<H}B_a(n+j)\right|^2
 \ll_\varepsilon X^\varepsilon {H^2L^4\over AD},
 \qquad 1\le H\le D, }
 \tag{TCG}
\]

where each \(B_a(q)\) is the displayed metaplectic pairing with all literal
owners still inside it.  Proving (TCG) requires a new correlation estimate
for the actual vector; Gaussian separation, Mellin separation, character
Poisson and Plancherel alone return at equal capacity.

## 2. Exact statement, hypotheses, and variable/owner dictionary

The hypotheses are the frozen residual hard top block:

\[
 J=X^{1/2},\quad b=a+2q,\quad h=ga,\quad s=gb,
 \quad \delta_q=\sqrt b-\sqrt a,
 \quad \Lambda_q={X\delta_q^2\over2},
\]

\[
 a\asymp A,\qquad q\asymp D,qquad
 k\asymp K\asymp {JD\over A},\qquad
 |\mathcal G_{a,b}|\asymp G\asymp {L\over A},
\]

\[
 E_0\asymp LJD^2,qquad
 \rho={AJD^3\over L^3}>1,qquad
 {E_0\over\rho}\asymp {L^4\over AD}.
\]

The primitive base ray consists of odd coprime \(a<b<4a\); \(g\) is an odd
member of the literal finite lift set.  The reciprocal fibre is the open
integer interval

\[
 I_{a,q}=\left({J(\sqrt b-\sqrt a)\over2\sqrt a},
               {J(\sqrt b-\sqrt a)\over\sqrt b}\right).
\]

The following dictionary fixes every new variable and operator.

| symbol | exact owner or meaning |
|---|---|
| \(a,b,q\) | primitive odd base ray, \(b=a+2q\); half-open \(A,D\) dyadic ownership and zero extension are literal |
| \(g,h,s\) | odd lift and physical indices \(h=ga,s=gb\); the finite lift floor, star and lift entry/exit conventions remain in \(\omega_\xi\) |
| \(k\) | integer reciprocal mode in the literal open fibre \(I_{a,q}\), with its half-open \(K\)-owner and equality samples |
| \(x\) | physical variable on the exact interval \([s/4,h]\), with \(A^\circ_{h,s}\), both fixed collars and all one-sided transition modules |
| \(\beta\) | physical square-root Fourier variable \(\beta=J\sqrt x\), so \(dx=(2\beta/X)d\beta\) |
| \(y\) | radical difference \(y=\sqrt s-\sqrt h=\sqrt g(\sqrt b-\sqrt a)\) |
| \(r\) | complete metric Fourier index; \(r=0\) is density and \(r\ne0\) are discrepancies, with both signs retained |
| \(c,\alpha_r\) | \(c=X/(2gk)>0\), \(\alpha_r=rc\), so \(\alpha_r y^2=r\Lambda_q/k\) |
| \(\tau\) | full real metaplectic variable; it is not restricted to a saddle neighbourhood |
| \(\iota\) | orientation/conjugation label; the second orientation is retained before the one outer \(2\Re\) |
| \(n,j,H\) | zero-extended fixed-\(a\) Fejer base, shift and length, with \(1\le H\le D\) |

The owner \(\mathbf P_{\rm lit}\) means the accepted one-count order: the
Round-75 diagonal, Round-77 full physical endpoints, collars, original
Poisson zero/positive/equality and negative nonstationary modes, Round-78
primitive square rays, Round-79 exact nonsquare metric centres and
positive-safe blocks, and every earlier profile/boundary term are owned once;
the displayed row is their literal successive complement.  The residual
projection also includes primitivity, dyadic half-open boundaries, the
finite lift set, floors, stars, the open reciprocal fibre and zero extension.
Nothing is point-evaluated after transformation.

There are three precise separation statements.

First, Gaussian separation is exact for the complete literal coefficient,
with the \(r=0\) atom and every \(r\ne0\) mode summed in
\(\mathcal M_{c,R}\).

Second, the accepted Round-77 smooth physical amplitude does factor at
fixed \((g,u)\), \(x=gu\): its endpoint factors have the form
\(E_{a,b}=E_a\overline{E_b}\), its profile factor has the form
\(P_{a,b}=L^3u^{-3/2}P_a\overline{P_b}\), and the two flat collars split.
The smooth difference cutoff has the exact Fourier separation

\[
 w\!\left({b-a\over D}\right)
 =\int_{\mathbb R}\widehat w(\lambda)
 e(\lambda b/D)e(-\lambda a/D)\,d\lambda,
 \qquad \|\widehat w\|_1=O_w(1),
\]

and primitivity is algebraically separated by
\(\mathbf1_{(a,b)=1}=\sum_{d\mid a,b}\mu(d)\).  In the natural
length-normalized \(\ell^2\times\ell^2\) ledger, the latter has harmonic
cost \(\sum_{d\le A}d^{-1}=O(\log(2A))\), not a power loss.  This produces a
literal oscillatory direct integral of two character sums after the lawful
linear completion described below; it does not make the \(\tau\)-kernel a
finite-total-variation measure.

Third, the sharp reciprocal ratio owner is different.  If
\(z=k/J\) and \(t=\sqrt{b/a}\), then its exact condition is

\[
 {1\over1-z}<t<1+2z,\qquad 0<z<1/2.
\]

Writing \(v=\log t\), its Mellin/Fourier coefficient is

\[
 \widehat C_z(\xi)
 =e\!\left(-\xi{\ell_z+u_z\over2}\right)
 {\sin(\pi\xi(u_z-\ell_z))\over\pi\xi},
 \quad
 \ell_z=-\log(1-z),\quad u_z=\log(1+2z).
\]

Thus \(\int_{\mathbb R}|\widehat C_z(\xi)|d\xi=\infty\).  The literal
sharp ratio band has no finite exact Mellin projective norm.  A smooth band
has \(O(1)\) norm, and a frequency truncation has \(O(\log(2+T))\) norm, but
making that truncation exact uniformly for real \(X\) requires a separate
endpoint/prefix-owner estimate: an integer ratio may equal, or lie
arbitrarily close to, either moving boundary.

At the signed linear block only, the accepted prior-owner and Round-77
nonstationary/equality totals may be reinserted and subtracted once at total
cost \(O_\varepsilon(L^2X^\varepsilon)\).  One may then sum \(k\) over a
fixed dyadic \(K\), independent of \((a,b)\), and the sharp ratio owner
disappears.  This lawful linear completion gives the advertised separated
two-character oscillatory pairing.  It is not lawful inside the positive
fixed-\(a\) Gram: a target-sized signed linear total gives no bound for the
sliding \(\ell^2\) norm of the reinserted vector.

## 3. Proof and derivation

For \(\alpha\ne0\), the standard Fresnel calculation with the stated
Fourier convention gives

\[
 \int_{\mathbb R}e\!\left(-{t^2\over4\alpha}-t\xi\right)dt
 =\sqrt{2|\alpha|}\,e(-\operatorname {sgn}(\alpha)/8)
 e(\alpha\xi^2).
\]

Multiplication by the prefactor in \(K_\alpha\) proves
\(\widehat K_\alpha(\xi)=e(\alpha\xi^2)\).  Therefore

\[
 \widehat{T_\alpha f}(\xi)=e(\alpha\xi^2)\widehat f(\xi),
\]

which proves unitarity, the group law
\(T_\alpha T_\beta=T_{\alpha+\beta}\), and inversion by \(T_{-\alpha}\).
It also proves \(K_\alpha\to\delta_0\) in \(\mathcal S'(\mathbb R)\), since
\(e(\alpha\xi^2)\to1\) boundedly against every Schwartz Fourier transform.
Thus the exact density operator is \(T_0=I\).

For a pointwise version, put \(B=J\sqrt x\).  The required regularization is

\[
 \operatorname {Os}\!\int K_\alpha(B-\tau)e(-\tau y)d\tau
 :=\lim_{\eta\downarrow0}\int K_\alpha(B-\tau)e(-\tau y)
 e^{-\pi\eta(B-\tau)^2}\,d\tau .
\]

Changing variable \(t=B-\tau\) and using the Fresnel formula gives exactly

\[
 \operatorname {Os}\!\int K_\alpha(B-\tau)e(-\tau y)d\tau
 =e(-By)e(\alpha y^2).
\]

For the complete metric series, first take the symmetric partial sum
\(|r|\le M\), next take \(\eta\downarrow0\), and finally take
\(M\to\infty\).  Since \(W_R\) is smooth,
\(\sum_r|\widehat W_R(r)|<\infty\); the operator series converges in
\(L^2\)-operator norm.  This ordering justifies all finite sum/integral
interchanges without assigning a false total variation to a Fresnel kernel.

Now substitute \(\beta=J\sqrt x\).  By construction,

\[
 \widehat f_\xi(y)
 =\omega_\xi\int_{s/4}^{h}A^\circ_{h,s}(x)
 e(kx-Jy\sqrt x)\,dx.
\]

Since \(\alpha_r y^2=r\Lambda_q/k\), the \(r\)-th metric mode is

\[
 e(r\Lambda_q/k)\widehat f_\xi(y)
 =\widehat{T_{rc_\xi}f_\xi}(y).
\]

Summing \(r\), including \(r=0\), proves

\[
 W_R(\Lambda_q/k)\widehat f_\xi(y)
 =\widehat{\mathcal M_{c_\xi,R}f_\xi}(y).
\]

Fourier inversion, in the preceding Abel sense at a hard endpoint, gives the
boxed factorization in Section 1, because
\(e(-\tau y)=e(\tau\sqrt h)e(-\tau\sqrt s)\).  This proves the exact
two-square-root phase separation without extending any integer owner to a
nonintegral saddle.

Plancherel gives the capacity identity

\[
 \|\mathcal M_{c,R}f\|_2^2
 =\int|W_R(c\eta^2)|^2|\widehat f(\eta)|^2d\eta.
\]

Moreover, \(c\eta^2\) runs through a full period of the period-one window as
\(\eta\) varies, so
\(\|\mathcal M_{c,R}\|_{2\to2}=\|W_R\|_\infty\).  There is no
\(\rho\)-dependent operator norm.  If the metric modes are kept as a labeled
direct sum, there is the additional exact identity

\[
 \sum_{r\in\mathbb Z}
 \|\widehat W_R(r)T_{rc}f\|_2^2
 =\left(\sum_r|\widehat W_R(r)|^2\right)\|f\|_2^2
 =\|W_R\|_{L^2(\mathbb T)}^2\|f\|_2^2.
\]

Recombining the modes restores all cross terms and exactly the multiplier
\(W_R(c\eta^2)\).  Hence density and discrepancies must remain joint; a
separate estimate is a different and generally larger object.

For every labeled mode, applying \(T_{-rc}\) returns the original physical
density.  On a finite zero-extended configuration Hilbert space, let
\(U=\bigoplus_{\xi,r}T_{rc_\xi}\).  Any literal owner projection \(P_E\)
transforms as

\[
 \widetilde P_E=UP_EU^{-1}.
\]

Thus norm, rank, idempotency, complements, orthogonality and one-count are
preserved.  Owners selecting complete \(\beta\)-fibres commute with \(U\).
A sharp physical collar or entry/exit projection becomes a nonlocal Fresnel
kernel.  A subsequent exact discrete character/Poisson transform similarly
conjugates the primitive, ratio and prior-owner masks.  Point evaluation of
any of these masks at a stationary noninteger is not the exact conjugation.

For the character algebra, oddness of \(g,a,b\) gives

\[
 \chi_4(h)\chi_4(s)=\chi_4(g)^2\chi_4(a)\chi_4(b)
 =\chi_4(a)\chi_4(a+2q)=(-1)^q.
\]

This proves the two-character factorization of the signed linear row.  But
expanding the fixed-\(a\) Gram gives

\[
 \mathcal G_H^{\rm act}
 =H\sum_{a,q}|F_a(q)|^2
 +2\Re\sum_{1\le v<H}(H-v)(-1)^v
   \sum_{a,q}F_a(q+v)\overline{F_a(q)}.
\]

Writing \(F_a(q)=\varepsilon_{a,q}B_a(q)\) and using
\((-1)^v\varepsilon_{a,q+v}\varepsilon_{a,q}=1\) changes this to the
positive sliding Gram of \(B\).  Therefore the two characters give no
oscillating \(q\)-autocorrelation in (TCG).

It remains to audit whether a direct linear two-character process could do
better.  At fixed odd \(g\), its base phase is

\[
 e(\tau\sqrt{ga})=e(T_g\sqrt a),\qquad T_g=\tau\sqrt g.
\]

Using
\(\chi_4(a)=(e(a/4)-e(3a/4))/(2i)\), exact Poisson produces odd dual
phases \(T_g\sqrt x-rx/4\).  A strict saddle satisfies

\[
 x_*={4T_g^2\over r^2}.
\]

On a local dyadic piece \(|\tau|\asymp J\sqrt L\), with
\(g\asymp G=L/A\), the dual length is

\[
 |r|\asymp {|T_g|\over\sqrt A}\asymp JG,
\]

not \(J\sqrt G\).  The stationary coefficient and the frequency Jacobian
preserve total squared coefficient mass \(\asymp A\).  Thus even the
correctly normalized one-character process has no spare square-root factor.
Also, \(|K_\alpha(B-\tau)|=(2|\alpha|)^{-1/2}\) is constant in \(\tau\):
the range \(|\tau|\asymp J\sqrt L\) is only a local calculation, not a
lawful global truncation.  Remote \(\tau\)-ranges cannot be summed by total
variation.

The exact composition explains the return.  If a paired scalar transform
produces a quadratic factor \(e(\vartheta\tau^2)\), put
\(\gamma=1-4\alpha\vartheta\).  Completing the square gives, for
\(\gamma\ne0\),

\[
 \boxed{
 \int_{\mathbb R}K_\alpha(B-\tau)e(\vartheta\tau^2)d\tau
 =\epsilon(\alpha,\gamma)|\gamma|^{-1/2}
 e\!\left({B^2\vartheta\over\gamma}\right), }
\]

\[
 \epsilon(\alpha,\gamma)
 =e\!\left({\operatorname {sgn}(\alpha)
 (1-\operatorname {sgn}(\gamma))\over8}\right).
\]

Indeed the quadratic coefficient is \(-\gamma/(4\alpha)\); the Fresnel
modulus is \(|\gamma|^{-1/2}\), the displayed unit is the product of the two
Gaussian units, and the completed phase is
\(B^2\vartheta/\gamma=Xx\vartheta/\gamma\).  When \(\gamma=0\), the
quadratic coefficient vanishes and the Abel limit is a Fourier delta
constraint, a metaplectic caustic rather than a saving.  Thus the family of
chirps closes under the proposed character B-process.  Its Jacobian balances
the factor \(|\gamma|^{-1/2}\), exactly as required by metaplectic
unitarity.

Finally, the exponent ledger is decisive:

\[
 {H^2E_0\over\rho}\asymp {H^2L^4\over AD}.
\]

The accepted fixed-row estimate gives
\(\sum_{a,q}|F_a(q)|^2\ll X^\varepsilon DL^4/A\), and rowwise Cauchy gives
\(\mathcal G_H^{\rm act}\ll X^\varepsilon H^2DL^4/A\), an exact
\(D^2\) deficit against (TCG).  The metaplectic operators, character
multipliers, exact owner conjugations and locally normalized character
Poisson maps all have equal \(L^2\) capacity.  They cannot change this
ledger or furnish \(\rho^{-1}\) in energy.  Their operator norms are
independent of \(\rho\), so no strict positive-power hard subrange is proved.

## 4. First doubtful or unproved step

The first unproved step is not the Gaussian constant, density limit,
two-character algebra, smooth amplitude factorization or inversion.  It is a
genuinely new estimate for the complete moving actual vector (TCG), after
the primitive character has constant autocorrelation.

Equivalently, one must control the nonzero-shift form

\[
 2\Re\sum_{1\le v<H}(H-v)
 \sum_{a,q}B_a(q+v)\overline{B_a(q)}
\]

jointly with its diagonal, where both entries retain different moving
reciprocal fibres, lift sets, \(c_\xi\), complete metric operators,
physical transition vectors, primitive and prior owners.  Plancherel only
relabels this form.  The accepted linear bounds for reinserted owner pieces
do not control their contribution to this positive Gram.

For a direct linear route, the first unsupported step is a
character-sensitive inequality that beats
\(\|\mathcal M_{c,R}\|=\|W_R\|_\infty\) by \(\rho^{-1/2}\) on the actual
factorized theta vectors while retaining the full oscillatory \(\tau\)
integral.  A finite-total-variation \(\tau\) measure does not exist before
physical integration, and the exact sharp ratio mask has a \(1/|\xi|\)
Mellin tail.  If the ratio mask is not lawfully removed at linear level, a
new endpoint/prefix-owner lemma is required before any \(X^\varepsilon\)
projective claim.  No such Gram or prefix theorem is proved here.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| `gaussian_constant_and_density_limit` | **Pass.** The unit is \(e(\operatorname{sgn}\alpha/8)\), the modulus is \((2|\alpha|)^{-1/2}\), \(\widehat K_\alpha=e(\alpha\xi^2)\), and \(K_\alpha\to\delta_0\) in \(\mathcal S'\). |
| `metric_density_discrepancy_jointness` | **Pass.** The complete operator is \(\mathcal M_{c,R}=\sum_r\widehat W_R(r)T_{rc}\), whose multiplier is exactly \(W_R(c\xi^2)\). Removing \(r=0\) changes the coefficient and destroys its cross-mode cancellations. |
| `two_character_factorization` | **Pass with a sharp scope split.** The signed linear row factors as \(\chi_4(h)e(\tau\sqrt h)\,\chi_4(s)e(-\tau\sqrt s)\). In the fixed-\(a\) Gram, \((-1)^v\varepsilon_{q+v}\varepsilon_q=1\), so there is no character autocorrelation gain. |
| `actual_symbol_vs_arbitrary_coefficients` | **Pass.** The Round-77 factorization, split collars and Möbius/smooth-difference separations are actual-symbol properties. Conversely \(\|\mathcal M_{c,R}\|=\|W_R\|_\infty\), and an arbitrary Fourier density concentrated where \(|W_R|\) is maximal saturates the operator norm. Thus no coefficient-blind \(\rho\)-gain is claimed. |
| `signed_vs_unsigned_and_adversarial` | **Pass.** No absolute value is taken before the signed linear pairing. The positive Gram is treated separately, and phase-aligned/adversarial densities show that Gaussian unitarity cannot prove its false arbitrary-coefficient analogue. |
| `primitive_and_prior_owner_one_count` | **Pass.** All earlier owners remain the literal successive complement. Möbius separation is used only algebraically. Reinsertion is licensed only for the signed linear total and is explicitly forbidden as an unproved Gram step. |
| `sharp_owner_conjugation_and_interpolation` | **Pass.** Exact owners transform as \(UP_EU^{-1}\), preserving projection data and one-count. No owner is evaluated at a nonintegral saddle; any later B-process must retain its full conjugated transition kernel. The sharp ratio band has infinite exact Mellin total variation. |
| `physical_collars_entry_exit_and_zero_extension` | **Pass.** They are contained in \(f_\xi\), \(\omega_\xi\), \(\iota\), and \(\mathbf P_{\rm lit}\). Empty and singleton reciprocal fibres are handled termwise by zero extension. Both conjugate orientations and the one outer \(2\Re\) remain. |
| `q1_Pell_near_square_and_fourth_power` | **Pass.** The formula is valid for \(q=1\), including empty/singleton \(k\)-fibres. Pell and near-square rows with bounded \(D\) and unbounded \(\rho\) rule out reliance on a growing shift or dual length. The coherent fourth-power family is carried isometrically to another coherent vector; variation is not converted into cancellation. Primitive square rays and exact centres remain prior owners. |
| `transform_inversion_and_capacity` | **Pass.** Modewise \(T_{-rc}T_{rc}=I\); recombination and Fourier inversion return \(W_R(\Lambda/k)\) exactly. Both the summed multiplier norm and labeled-mode energy are computed explicitly. The character B-process composition closes in the same metaplectic family, with the caustic retained. |
| `rho_power_and_endpoint_ledger` | **Pass as a no-go.** The target is \(X^\varepsilon H^2L^4/(AD)\), the accepted row/Cauchy bound misses by \(D^2\), and every transform used here has \(\rho\)-independent capacity. No \(\rho^{-1}\) energy gain and no fixed positive-power subrange is asserted. Sharp endpoints require a prefix owner rather than a silent smoothing. |
| `downstream_and_exponent_scope` | **Pass.** The result concerns only the proposed Gaussian/two-character mechanism on the residual hard top block. It proves neither (TCG), the hard signed cone, the balanced or unbalanced smooth packets, \(M9\!-!M2\), endpoint uniformity, \(M9\), nor a new circle exponent. |

No numerical experiment is used.  The proof is algebraic/analytic; the
q=1, Pell, near-square and fourth-power checks are structural controls, not
numerical evidence for an asymptotic theorem.

## 6. Dependencies and exact artifacts used

The report uses only the assigned brief and permitted context:

1. `protocol.md` for graph authority, no-go promotion and scope rules.
2. `state/proof_obligations.yml` for the exact open fixed-\(a\) Gram, joint
   density-discrepancy target, character, carrier, q-dispersion, fixed-q and
   dual-square owner nodes.
3. `state/active_campaign.yml` for Round 108 scales, controls and exit gate.
4. `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/derivation_packet.md`
   for the frozen row, target and candidate Gaussian identity.
5. `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/candidates/conductor_metaplectic_two_character_core.md`
   for the density atom, proposed theta pairing and quantitative gate.
6. `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`
   for the literal M2 one-count block, owner order and hard-block capacity.
7. `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`
   for the complete collar-extracted actual symbol and entry/exit-uniform
   variation.
8. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`
   for density restoration, carrier cancellation and adjoint-Poisson return.
9. `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md`
   for the fixed-\(a\) Gram, q=1/Pell controls and prior equal-capacity
   obstruction.
10. `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/synthesis.md`
    for the uniform actual row theorem, collapsing fibres and exact \(D^2\)
    Gram deficit.
11. `rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/synthesis.md`
    for exact owner conjugation, interpolation independence and the ban on a
    scalar stationary gain.
12. The Round-108 task brief
    `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/briefs/metaplectic_two_character_attack.md`
    and the conductor's in-round seam corrections supplied to this task: the
    fixed-\((g,u)\) Round-77 factorization, character cancellation in the
    Gram, the sharp ratio band, the correct \(JG\) character-dual scale, the
    nonlocal \(\tau\) warning, and the exact metaplectic composition check.

No external theorem, web source, sibling Round-108 report or unpermitted
historical derivation is used.  There is no new source dependency.

## 7. Recommended state effect

**Promote a scoped internal obstruction, not the target.**  The promotable
kernel is:

1. the exact Abel-regularized kernel \(K_\alpha\), its constant, density
   limit, unitary group law and inverse;
2. the complete operator identity
   \(\mathcal M_{c,R}=\sum_r\widehat W_R(r)T_{rc}\) and multiplier
   \(W_R(c\xi^2)\), with the exact summed and labeled-mode capacities;
3. the literal two-character factorization of the signed linear row and the
   exact cancellation of primitive-character autocorrelation in the
   fixed-\(a\) Gram;
4. the distinction between lawful linear reinsertion and unlawful Gram
   reinsertion, together with the \(1/|\xi|\) sharp-ratio Mellin obstruction;
5. the corrected one-character dual scale \(JG\), preservation of squared
   mass, and the exact Gaussian/chirp composition formula, including its
   caustic.

Create or retain (TCG) as the strictly smallest open actual-vector survivor.
It must be proved before the fixed-\(a\) Gram can close.  Retain the canonical
joint density-discrepancy energy, hard signed cone, all smooth M2 packets,
\(M9\!-!M2\), endpoint uniformity, \(M9\), the conditional bridge and the
quarter target as open.

Reject claims that a finite-total-variation Fresnel measure, deletion of the
density, a generic theta/large-sieve square root, a sharp Mellin separation
without a prefix owner, a character B-process, Plancherel, or Gaussian
inversion supplies the missing \(\rho^{-1/2}\) linear gain.  The obstruction
is scoped: it is not a lower bound for the actual M2 vector and does not rule
out a new directional estimate proving (TCG).

# Round 140 hostile audit: the post-collar height--alias scalar

## 1. Result

**strict_height_alias_reduction, with a sharp-endpoint principal-value
no-go.**

The literal sharp-cutoff character-Poisson formula is exact only with
its half-endpoint and its prescribed symmetric ordering.  It is not an
absolutely separable family of dual owners.  In fact, for every active
row whose upper endpoint lies on the lower-profile plateau, each remote
dual integral has a nonzero term of size (1/|r|).  Thus a split into a
closest alias and absolutely summed far aliases is invalid at the sharp
endpoint.

There is, however, a lawful repair using only the already proved Round
139 collars.  Choose fixed

\[
 0<\rho_1<\rho_2<1/8
\tag{140.H1}
\]

(one may take \(\rho_1=\rho\), \(\rho_2=2\rho\) after choosing
\(\rho<1/16\)).  Smooth the tail indicator only across the displacement
band between the two collars.  The physical difference is
\(O(R\log(2X))\) by the exact curvature estimate, while the smoothed
amplitude has no hard endpoint.  Its Poisson series is absolutely
separable after the standard stationary/nonstationary partition.  The
whole smoothing-transition alias band, the closest clean alias, all
nonstationary modes, and all stationary remainders are
\(O(R\log^C(2X))\) for a fixed harmless \(C\).  Consequently the literal
tail is target-equivalent to the clean bulk principal family

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
  \sum_{h\ge1}
  \sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
  \chi_4(r)(hr)^{-3/4}
  V_{\rm low}\!\left({R^2hr\over N}\right)
  e\!\left(\sqrt{Nhr}\right),
\tag{140.H2}
\]

where \(r_{2,h}\) is the least positive odd integer at least
\(4Nh/D_{2,h}^2\), and profile-zero terms are literal zeros.  More
precisely,

\[
 \boxed{\mathcal S_{N,\rho_1}^{+}
        =\mathcal P_{\rho_2}^{+}
         +O(R\log^C(2X)),\qquad
        \mathcal S_{N,\rho_1}^{-}
        =\overline{\mathcal S_{N,\rho_1}^{+}}.}
\tag{140.H3}
\]

This is a strict owner-complete reduction, not the target estimate.  The
bulk family (140.H2) still has \(R^{3/2+o(1)}\) absolute capacity.  Its
phase has Hessian determinant zero both in \((h,r)\) and after
\(r=4h+s\); product-fibre grouping returns an incomplete
sum-of-two-squares divisor coefficient.  No target bound, lower GAR,
blockwise M1 statement, M9-M1, M2 statement, endpoint theorem, M9,
quarter theorem, or exponent improvement follows.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y.
\tag{140.H4}
\]

The fixed real lower profile is the inherited smooth compactly
supported profile, equal to one near zero.  Only its fixed derivative
bounds, bounded variation, and the literal implication
\(V_{\rm low}(4R^2h^2/d^2)\ne0\Rightarrow h\ll d/R\) are used.  Bounded
\(X\) is absorbed into the implied constant.  For \(i=1,2\), put

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,
 \qquad D_{i,h}=y-L_{i,h}-1.
\tag{140.H5}
\]

Rows with \(D_{i,h}<1\) are empty before any division by \(D_{i,h}\).
The literal positive tail at \(\rho_1\) is

\[
 \mathcal S_{N,\rho_1}^{+}
 =\sum_{h\ge1}{1\over h}
  \sum_{1\le d\le D_{1,h}}\chi_4(d)
  V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(Nh/d).
\tag{140.H6}
\]

For the sharp formula define

\[
 A_h(x)={1\over h}V_{\rm low}\!\left({4R^2h^2\over x^2}\right),
 \qquad
 I_{h,r}^{\sharp}=\int_0^{D_{1,h}}A_h(x)
 e\!\left({Nh\over x}+{rx\over4}\right)\,dx.
\tag{140.H7}
\]

The zero extension makes \(A_h\) identically zero near \(x=0\).
Poisson summation with the dual integer symmetrized separately in the
two mod-four branches gives the exact identity

\[
 \begin{split}
 \mathcal S_{N,\rho_1}^{+}
 ={}&E_{\sharp}
 +{1\over2i}\sum_{\tau=\pm1}\tau\sum_{h\ge1}
 \lim_{K\to\infty}\sum_{|k|\le K}
 I_{h,\tau-4k}^{\sharp},\\
 E_{\sharp}={}&{1\over2}\sum_{h\ge1}{\chi_4(D_{1,h})\over h}
 V_{\rm low}\!\left({4R^2h^2\over D_{1,h}^2}\right)
 e(Nh/D_{1,h}).
 \end{split}
\tag{140.H8}
\]

Empty rows contribute neither term.  The endpoint owner is target-safe:

\[
 |E_{\sharp}|\ll\sum_{h\ll R}{1\over h}\ll\log(2X).
\tag{140.H9}
\]

For \(r>0\), the phase

\[
 \phi_{h,r}(x)={Nh\over x}+{rx\over4}
\tag{140.H10}
\]

has its unique stationary point at

\[
 x_*=2\sqrt{Nh/r},\quad
 \phi(x_*)=\sqrt{Nhr},\quad
 \phi''(x_*)={r^{3/2}\over4(Nh)^{1/2}}.
\tag{140.H11}
\]

Writing \(r=4h+s\), the closed sharp-endpoint condition is exactly

\[
 s\ge T_{1,h}:={4h(N-D_{1,h}^2)\over D_{1,h}^2}.
\tag{140.H12}
\]

Equality in (140.H12) is an endpoint stationary point, not a full
interior Gaussian.  The least admitted closed alias is the least odd
\(s\) at least \(T_{1,h}\), because \(r\), hence \(s\), is odd.  All
congruence information is retained by
\(\tau=\chi_4(r)\).

For the smooth repair let

\[
 \Delta_h=D_{1,h}-D_{2,h}+1=L_{2,h}-L_{1,h}+1
 \asymp_{\rho_1,\rho_2}{y\over\sqrt h}
\tag{140.H13}
\]

on active rows, and choose a fixed \(C^\infty\) function
\(\eta\) which is zero on \(( -\infty,0]\), one on \([1,\infty)\),
and flat at both endpoints.  Put

\[
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right).
\tag{140.H14}
\]

Then \(W_h=1\) for \(x\le D_{2,h}\), \(W_h=0\) for
\(x\ge D_{1,h}+1\), and

\[
 \|W_h^{(j)}\|_\infty\ll_j\Delta_h^{-j}.
\tag{140.H15}
\]

Define \(\widetilde A_h=A_hW_h\) and the corresponding smoothed
physical scalar \(\widetilde{\mathcal S}_N^+\).  Whole-line Poisson is
now exact without any half-endpoint:

\[
 \widetilde{\mathcal S}_N^+
 ={1\over2i}\sum_{\tau=\pm1}\tau
  \sum_{h\ge1}\sum_{k\in\mathbb Z}
  \int_0^\infty\widetilde A_h(x)
  e\!\left({Nh\over x}+{(\tau-4k)x\over4}\right)dx.
\tag{140.H16}
\]

The series in (140.H16) admits the absolute owner decomposition used
below; unlike (140.H8), it has no endpoint harmonic tail.

## 3. Proof or derivation

First, the displacement dictionary is exact.  The complement of
\(v\le L_{1,h}\) is \(v\ge L_{1,h}+1\), and with \(d=y-v\) this is
precisely \(1\le d\le y-L_{1,h}-1=D_{1,h}\).  This proves (140.H6),
including the floor, equality, parity zeros, and empty rows.  Since the
profile and character are real, the negative scalar is its conjugate.

For each fixed row, apply the Dirichlet-convention finite Poisson
formula to each of
\(A_h(x)e(Nh/x\pm x/4)\).  The value at zero is zero, while the value at
the inclusive integer endpoint is counted with half weight by the
Fourier integral and therefore needs the explicit other half.  Combining
the two branches by

\[
 \chi_4(d)={e(d/4)-e(-d/4)\over2i}
\tag{140.H17}
\]

gives (140.H8).  A nonzero endpoint sample forces
\(h\ll D_{1,h}/R\le y/R=R\), proving (140.H9).

The sharp formula cannot be split by absolute values.  For a fixed
active row with \(A_h(D_{1,h})\ne0\), integration by parts at large
\(|r|\) gives

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})
 e(Nh/D_{1,h}+rD_{1,h}/4)
  \over2\pi i\{r/4-Nh/D_{1,h}^2\}}
 +O_h(r^{-2}).
\tag{140.H18}
\]

The lower boundary vanishes.  For \(h=1\) and large \(y\), the endpoint
profile argument tends to zero, so the inherited plateau makes the
numerator in (140.H18) nonzero.  Hence

\[
 \sum_{r\ {\rm odd}}|I_{h,r}^{\sharp}|=\infty.
\tag{140.H19}
\]

The symmetric branch ordering and the half-endpoint in (140.H8) carry
the cancellation of this boundary series.  Dropping them, or moving a
modulus through them, is not a harmless error.

Next audit the floor and \(q\) in the stationary offset.  Let
\(m_h=L_{1,h}+1\), so \(D_{1,h}=y-m_h\), and write

\[
 m_h={\rho_1y\over\sqrt h}+\vartheta_h,qquad
 0<\vartheta_h\le1.
\tag{140.H20}
\]

Then exactly

\[
 T_{1,h}
 =4h{2ym_h-m_h^2+q\over(y-m_h)^2}.
\tag{140.H21}
\]

On literal support \(h\ll R\), while
\(m_h/y\le\rho_1+1/y\).  Expanding only inside this fixed compact
range gives, uniformly for \(0\le q\le2y\),

\[
 T_{1,h}=8\rho_1\sqrt h+O_{\rho_1}(1+h/y)
          =8\rho_1\sqrt h+O_{\rho_1}(1),
 \qquad T_{1,h}\asymp_{\rho_1}\sqrt h.
\tag{140.H22}
\]

Thus the phrase "order \(\sqrt h\)" is valid only after (140.H21), not
as a replacement for it.  The hard endpoint transition parameter is

\[
 {\phi'_{h,r}(D_{1,h})\over
  \sqrt{\phi''_{h,r}(D_{1,h})}}
 \asymp (r-4Nh/D_{1,h}^2)\sqrt{y/h}.
\tag{140.H23}
\]

Its dual width is \(O(\sqrt{h/y})<1\) on active rows.  There is at most
one odd closest alias.  Since
\(\phi''(x)=2Nh/x^3\gg h/y\) for \(x\le D_{1,h}\), the BV
second-derivative estimate gives its exact integral the bound

\[
 |I_{h,r}^{\sharp}|\ll {1\over h}\sqrt{y/h}
 =Rh^{-3/2}.
\tag{140.H24}
\]

Summing (140.H24) is \(O(R)\).  But (140.H24) does not repair the remote
boundary series (140.H18).

The two-collar smoothing does.  At integer points the difference
between the sharp indicator and \(W_h\) is supported exactly in

\[
 L_{1,h}<v\le L_{2,h}.
\tag{140.H25}
\]

Its sampled variation is \(O(1)\).  The complete phase on this band has
the same constant-sign curvature \(\asymp h/y\) as in Round 139 because
\(v\le L_{2,h}\) and \(\rho_2<1/8\).  Thus one row costs
\(O(\sqrt y+\sqrt{y/h})\), and restoring \(h^{-1}\) yields

\[
 \mathcal S_{N,\rho_1}^{+}
 =\widetilde{\mathcal S}_N^++O(R\log(2X)).
\tag{140.H26}
\]

This estimate is signed and made before Poisson, so it does not change
scalar direction.

The derivative ledger for the smoothed Poisson amplitude is

\[
 \|\widetilde A_h\|_\infty+\|\widetilde A_h'\|_1\ll h^{-1},
 \qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.H27}
\]

The profile terms follow after the monotone substitution
\(4R^2h^2/x^2\); the cutoff terms follow from (140.H15), and the mixed
term is smaller than their sum.  All boundary values and derivatives
vanish.

The stationary points lying in the smoothing ramp have aliases in the
exact interval

\[
 {4Nh\over(D_{1,h}+1)^2}
 \le r\le\ {4Nh\over D_{2,h}^2}.
\tag{140.H28}
\]

Equations (140.H13) and (140.H4) show that (140.H28) contains
\(O(1+\sqrt h)\) odd integers, uniformly in \(q\).  Applying (140.H24)
to these exact integrals gives

\[
 \sum_h\sum_{r\ {\rm in}\ (140.H28)}
 |\widetilde I_{h,r}|
 \ll\sum_{h\ll R}Rh^{-3/2}(1+\sqrt h)
 \ll R\log(2X).
\tag{140.H29}
\]

Therefore \(r_{1,h}+2\) is not yet the beginning of a clean bulk: the
whole interval up to the \(\rho_2\) threshold belongs to the smoothing
ramp.  The least clean odd alias \(r_{2,h}\) itself also costs only
\(O(Rh^{-3/2})\), so it may be retained with (140.H29); the far family
starts at \(r_{2,h}+2\).

For a far stationary pair set \(m=hr\),
\(\lambda=\sqrt{Nm}\), and \(x=x_*u\).  Its integral becomes

\[
 2\sqrt{N/m}\int
 V_{\rm low}\!\left({R^2m\over Nu^2}\right)
 W_h(x_*u)
 e\!\left({\lambda\over2}(u+u^{-1})\right)du.
\tag{140.H30}
\]

At \(u=1\), \(W_h=1\), and the next odd alias is already many Gaussian
widths inside the plateau.  Local stationary phase gives

\[
 \widetilde I_{h,r}
 =2e(1/8)N^{1/4}(hr)^{-3/4}
  V_{\rm low}(R^2hr/N)e(\sqrt{Nhr})
 +\mathcal E_{h,r}.
\tag{140.H31}
\]

The local Taylor remainder is
\(O(N^{-1/4}(hr)^{-5/4})\).  On the complement of a stationary
neighborhood, integration by parts in (140.H30), using total variation
rather than a support length, gives \(O(r^{-1})\) uniformly down to the
first far alias.  Away from the cutoff ramp it improves to
\(O((hr)^{-1})\).  Hence the deliberately coarse uniform ledger is

\[
 \sum_{\substack{h,r\ {\rm far}\\hr\ll y}}
 |\mathcal E_{h,r}|
 \ll N^{-1/4}\sum_m\tau(m)m^{-5/4}
     +\sum_{h\ll R}\sum_{h\ll r\ll y/h}{1\over r}
 \ll R\log(2X).
\tag{140.H32}
\]

The modes with no stationary point require no principal term.  Below
the hard-entry image, one derivative and dyadic distance from the image
give \(O(h^{-1}\log(2h))\) per row.  For negative aliases and aliases
beyond the compact profile image, two integrations by parts are needed;
one integration would reproduce a harmonic series.  Because all smooth
boundary values vanish, summing the twice-integrated bounds first over
the aliases uses (140.H27) and gives \(O(R\log^C(2X))\), with room
to spare against the scalar target, over all active rows.  In particular the terms have denominators
quadratic in the distance from the derivative image; the factors
\(\Delta_h^{-1}\) and \((Rh)^{-1}\) in (140.H27) are gains, not losses.
This closes every smooth nonstationary and remainder owner.  Combining
(140.H16), (140.H29)--(140.H32), and
\(e(1/8)/i=e(-1/8)\) proves (140.H2)--(140.H3).

The remaining geometry supplies a no-go for a generic two-dimensional
curvature estimate.  For
\(F(h,r)=\sqrt{Nhr}\),

\[
 \nabla^2F={\sqrt N\over4\sqrt{hr}}
 \begin{pmatrix}-r/h&1\\[2pt]1&-h/r\end{pmatrix},
 \qquad \det\nabla^2F=0,
 \qquad \nabla^2F\binom h r=0.
\tag{140.H33}
\]

The change \((h,s)\mapsto(h,r)=(h,4h+s)\) is invertible and linear, so
its Hessian is the congruence transform of (140.H33) and still has
determinant zero.  Equivalently,
\(\sqrt{Nh(4h+s)}\) is homogeneous of degree one.  Along a primitive
ray \((h,s)=(bt,ct)\),

\[
 \sqrt{Nh(4h+s)}=t\sqrt{Nb(4b+c)}.
\tag{140.H34}
\]

When \(c,t\) are odd, the actual character is
\(\chi_4((4b+c)t)=\chi_4(c)\chi_4(t)\); thus it shifts the linear
frequency by a quarter on the odd \(t\)-lattice.  Exact radical rays do
not automatically reinforce the character, but near quarter-resonant
rays have no curvature protection.  Ignoring the character here would
be an incorrect coherent-ray lower-bound claim.

Grouping (140.H2) by \(m=hr\) gives exactly

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
  \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)e(\sqrt{Nm})
  A_{\rho_2}(m),
\tag{140.H35}
\]

\[
 A_{\rho_2}(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                  r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.H36}
\]

Without the cone truncation, the fibre is
\(\sum_{r\mid m}\chi_4(r)=r_2(m)/4\); the clean tail has the
corresponding incomplete divisor fibre.  Thus product grouping collapses
the apparent two-dimensional phase back to the circle coefficient
rather than creating a new curvature direction.

The actual \(h^{-1}\) has already become the factor
\((hr)^{-3/4}\).  On every nonempty dyadic height range
\(h\asymp H\), a modulus gives

\[
 N^{1/4}\sum_{h\asymp H}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \asymp R^{3/2+o(1)},
\tag{140.H37}
\]

against target \(R\).  Removing the \(O(\sqrt h)\) entry aliases costs
only \(O(R\log X)\) and does not alter (140.H37).

Finally write \(N=Da^2\) with \(D\) squarefree.  The phase in
(140.H35) is exactly one precisely when

\[
 m=Dt^2.
\tag{140.H38}
\]

Using \(|A_{\rho_2}(m)|\le\tau(m)\), the whole exact radical channel has
absolute mass

\[
 \ll_\varepsilon N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{140.H39}
\]

This is target-safe.  Near radicals, incomplete product fibres, and the
aggregate over rank-one rays remain open.  A second Legendre transform
reverses (140.H31) to the reciprocal phase, while completing the full
fibre returns the sum-of-two-squares interface; neither is a signed
gain.

## 4. First doubtful or unproved step

For the literal sharp cutoff, the first false step is treating the
dual integrals after (140.H8) as independent absolutely summable owners.
Equations (140.H18)--(140.H19) disprove that step.  Keeping only the
least stationary alias does not help: it is target-safe by (140.H24),
but the remote principal-value boundary series is still present.  A
sharp principal-only identity is therefore not licensed.

The two-collar smoothing repairs precisely that seam and yields the
strict reduction (140.H3).  After the repair, the first genuinely
unproved estimate is

\[
 \boxed{|\mathcal P_{\rho_2}^{\pm}|
        \ll_\varepsilon RX^\varepsilon.}
\tag{140.H40}
\]

No nondegenerate two-dimensional second-derivative theorem applies
because of (140.H33).  Taking product-fibre moduli gives (140.H37), and
using the complete divisor fibre imports the sum-of-two-squares
coefficient.  Exact radicals are not the obstruction by (140.H39); the
missing input is simultaneous signed control of the incomplete product
fibres and near-quarter/radical rays across all dyadic heights.  No such
estimate is proved in the supplied artifacts.

## 5. Control tests and outcomes

| Required control | Outcome | Status |
|---|---|---|
| Exact tail cutoff, floors, empty rows, both signs | \(v>L_{1,h}\) is exactly \(1\le d\le D_{1,h}\); empty rows are removed before division and the negative sign is the conjugate. | Green. |
| Mod-four character-Poisson branches | Equation (140.H8) keeps \(\tau=\pm1\) with separate symmetric \(k\)-limits; \(r=\tau-4k\) and \(\tau=\chi_4(r)\) for positive odd \(r\). | Green. |
| Hard endpoint, half weight, zero extension | The endpoint is exactly \(E_\sharp\), bounded by (140.H9).  The raw integrals have the harmonic boundary term (140.H18); absolute separation is red. | Green identity; sharp absolute split rejected. |
| Stationary entry and exact offset | Equations (140.H20)--(140.H22) retain every floor and \(q\); the least \(s\) is the least odd integer at least the exact threshold. | Green. |
| Equality and incomplete-Fresnel transition | Equality is not counted as a full Gaussian.  Its dual width is below one and its sole closest alias has total cost \(O(R)\). | Green. |
| Profile entry, exit, and crossings | They remain inside the literal factor \(V_{\rm low}(R^2hr/N)\).  Fixed smoothness makes the profile-exterior modes and local remainders summable; no sharp profile replacement is made. | Green after smoothing. |
| Nonstationary and remainder owner ledger | The sharp version fails (140.H19).  The flat two-collar cutoff has derivative ledger (140.H27); ramp aliases cost (140.H29), bulk errors cost (140.H32), and twice-integrated exterior tails are target-safe. | Green only for the repaired connector. |
| Joint Hessian and rational rays | Determinant zero is exact in both \((h,r)\) and \((h,s)\).  The actual character quarter-shift is retained on rays. | Green obstruction. |
| Product fibres, exact and near radicals | Equations (140.H35)--(140.H39) prove the exact radical upper control; incomplete fibres and near radicals remain open. | Exact channel green; near channel open. |
| Height weight and dyadic capacity | The \(h^{-1}\) is included in (140.H31).  Entry and ramp owners are target-safe, but every bulk dyadic height range has the \(R^{3/2+o(1)}\) modulus ledger (140.H37). | Green obstruction; target open. |
| Fourth powers \(q=0\) and maximal \(q=2y\) | At \(q=0\), (140.H21) is exact and (140.H38) has \(D=1\); its mass is \(O(RX^\varepsilon)\).  At \(q=2y\), the extra offset is \(O(h/y)\) in (140.H22), uniformly negligible on active rows. | Green. |
| Transform self-return and downstream direction | The repair changes the scalar by a signed \(O(R\log X)\) band before transforming.  A second transform returns the reciprocal phase; no tail square or residual deletion is inferred. | Green direction; target open. |

## 6. Dependencies and exact artifacts used

This report is entirely analytical.  It uses exactly:

- `protocol.md`;
- `state/proof_obligations.yml`, restricted to the active lower-radial
  nodes and their stated downstream scope;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reports/farey_scalar_self_return_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/reviews/conductor_round139_displacement_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/blind_statement.md`;
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/briefs/tail_alias_hostile_directionality_audit.md`.

No sibling report, numerical experiment, web source, centre average,
arbitrary-coefficient theorem, or desired circle estimate is used.  The
finite Poisson, integration-by-parts, stationary normalization, and
divisor-fibre calculations are derived in the displayed equations.

## 7. Recommended state effect

Promote only the following strict reduction after an independent seam
review reproduces the smoothing and B-process ledgers:

1. the sharp height-dependent Poisson identity (140.H8), endpoint bound
   (140.H9), exact offset (140.H21), and sharp principal-value
   obstruction (140.H18)--(140.H19);
2. the lawful two-collar smoothing equivalence (140.H26), with
   derivatives (140.H27), complete ramp cost (140.H29), and clean bulk
   reduction (140.H3);
3. the rank-one Hessian, character-correct rational-ray, product-fibre,
   dyadic-capacity, and exact-radical controls
   (140.H33)--(140.H39).

Reject a closest-alias-only repair at the sharp endpoint, any claim that
\(r_{1,h}+2\) is already outside the smoothing transition, any
absolute summation of (140.H8), any nondegenerate two-dimensional
curvature gain, any coefficient-blind product-fibre modulus, and any
principal-only claim before (140.H26)--(140.H32) are present.

Retain (140.H40), the complete lower-radial signed estimate, lower GAR,
both blockwise M1 parents, M9-M1, every M2 parent, endpoint uniformity,
M9, the conditional bridge, and the quarter target as open.  Retain the
internally proved exponent \(1/3\) and the separately audited external
Li--Yang exponent unchanged.  No graph or shared-state file was edited.



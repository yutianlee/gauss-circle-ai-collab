# Round 140 synthesis: the post-collar tail is a clean far-alias scalar

Campaign: m9-m1-lower-post-collar-height-alias-gate

Starting graph SHA-256:
a9f766ddfc55c1aa9dd0561d8a406996627ac8701313af063c90e2422cf54eaa

## Decision

Close under
\(\mathsf{strict\_height\_alias\_reduction}\).  With

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\]

fix \(0<\rho_1<\rho_2<1/8\), put

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,\qquad
 D_{i,h}=y-L_{i,h}-1,
\]

and let \(r_{2,h}\) be the least positive odd integer at least
\(4Nh/D_{2,h}^2\) on every nonempty row.  Then the literal sharp
Round-139 tail satisfies

\[
 \boxed{
 \mathcal S_{N,\rho_1}^{\pm}
 =\mathcal P_{\rho_2}^{\pm}
 +O(R\log^C(2X)),}
\tag{140.S1}
\]

where

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_h\sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\qquad
 \mathcal P_{\rho_2}^{-}=\overline{\mathcal P_{\rho_2}^{+}}.
\tag{140.S2}
\]

Thus the lower scalar target is equivalent to

\[
 \boxed{|\mathcal P_{\rho_2}^{\pm}|
 \ll_\varepsilon RX^\varepsilon.}
\tag{140.S3}
\]

Equation (140.S3) is not proved.

## Why smoothing is necessary and sufficient

The exact sharp character-Poisson formula includes a half-endpoint and
a branchwise symmetric dual limit.  For every row with a nonzero upper
sample, its remote integrals have

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})e(Nh/D_{1,h}+rD_{1,h}/4)
   \over2\pi i(r/4-Nh/D_{1,h}^2)}
 +O_h(r^{-2}),
\tag{140.S4}
\]

so their absolute odd-\(r\) sum diverges.  A closest-alias or
principal-only sharp reduction is therefore invalid.

The lawful repair smooths only across the band between the two accepted
curvature collars:

\[
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over
 D_{1,h}-D_{2,h}+1}\right).
\]

Sharp minus smooth is supported exactly on
\(L_{1,h}<y-d\le L_{2,h}\) and costs \(O(R\log X)\) by the
Round-139 exact-curvature lemma.  The smoothed amplitude has flat
endpoints and derivative ledger

\[
 \|\widetilde A_h\|_\infty+\|\widetilde A_h'\|_1\ll h^{-1},
\qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.S5}
\]

On a dyadic physical block \(x\asymp Z\), the stationary-alias count,
Gaussian width, and cubic parameter are

\[
 P={Nh\over Z^2},\qquad
 w=\left({Z^3\over Nh}\right)^{1/2},\qquad
 \epsilon_3=\sqrt{Z\over Nh}.
\]

The counted cubic and fixed-profile errors are both \(O(h^{-1})\).
The cutoff derivative is localized to \(O(\sqrt h)\) ramp aliases, for
which

\[
 \sqrt h\,{w^2\over h\Delta_h}\ll h^{-1}.
\tag{140.S6}
\]

Two integrations close the infinite negative and remote positive tails.
The smooth rowwise error is \(O(h^{-1}\log^2 X)\), hence
\(O(\log^3 X)\) over all heights.  The ramp and the first clean alias
cost \(O(R\log X)\).  Starting at \(r_{2,h}+2\), every saddle is many
Gaussian widths inside \(W_h=1\), and its exact leading coefficient is
the one in (140.S2).  This proves (140.S1) with no unowned endpoint,
transition, profile, nonstationary, or remainder term.

## Arithmetic form and surviving obstruction

Grouping by \(m=hr\) gives

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm}),
\tag{140.S7}
\]

\[
 A_{\rho_2}(m)
 =\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                   r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.S8}
\]

This is an exact incomplete divisor coefficient.  Its
coefficient-blind upper bound is \(R^{3/2+o(1)}\), and the \(h=1\)
profile plateau has matching absolute capacity.  The joint phase
\(\sqrt{Nhr}\) has Hessian determinant zero and rank one, also after
the exact linear change \(r=4h+s\).

The mask does not force character cancellation.  On suitable
fourth-power profile fibres with \(p\equiv1\pmod4\),

\[
 A_{\rho_2}(p^{2a})=a.
\tag{140.S9}
\]

This is an internal fibre control, not a signed scalar lower bound.
If \(N=Du^2\), \(D\) squarefree, the exact radical channel
\(m=Dt^2\) has total absolute mass
\[
 O_\varepsilon(RD^{-3/4}X^\varepsilon),
\]
so it is target-safe.  Near radicals and nonsquare incomplete fibres
are the first open cancellation problem.  A second Legendre transform
returns the reciprocal phase \(N/z\), while completion of the fibre
returns \(r_2(m)/4\); neither is an independent gain.

## Direction and proof status

Round 140 proves a strict scalar transform reduction only.  It does not
produce a tail-square identity, control the collar--tail cross term, or
delete a Round-138 residual sub-square.  The exact open estimate is

\[
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.
\tag{140.S10}
\]

The complete lower-radial signed estimate, lower GAR, both direct
blockwise M1 parents, and M9-M1 remain open.  Every required M2 owner,
M9-M2, endpoint uniformity, M9, the conditional bridge, and the
Gauss-circle quarter target also remain open.

The strongest internally proved exponent remains
\[
 {1\over3}.
\]

The separately audited external Li--Yang benchmark remains
\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

Round 140 proves no exponent improvement.

Resulting graph SHA-256:
072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

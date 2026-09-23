# Round 169 source/spectral/power review of the conductor self-return candidate

## 1. Result

**Verdict: PASS.**

The candidate
`candidates/conductor_round169_joint_fe_double_poisson_self_return.md`
is source-clean and power-correct for the reduction it claims.

More precisely:

1. Equations (169.C1)--(169.C25) use finite coefficient algebra, the
   exact physical convolution, character Poisson, ordinary Poisson,
   Mellin functional-equation kernels, elementary integration by parts,
   and stationary equations.  No shifted-convolution, Kuznetsov,
   spectral-large-sieve, reciprocity, or weighted-moment theorem is
   imported into those internal identities.
2. The correction
   \(E_0=Z_{\mathrm{phys}}-R_\zeta\) is necessary: the finite physical
   zero mode is not the full Mellin residue.  The candidate separates
   them with the correct sign and proves both are
   \(O(L^2/J)\) (or, using only the accepted headline bound,
   \(O_\varepsilon(L^2J^{-1}X^\varepsilon)\)).  Either form is far below
   the \(L^{3/2}X^\varepsilon\) target throughout \(L\ll H\).
3. The exact double-Poisson identity genuinely returns the complete
   scalar to the collapsed Round-162 signed family, and returns
   \(\mathcal I_\eta\) to it up to \(E_0\).  It does not prove the
   nonzero-frequency bound.
4. The restored favorable smooth-interior capacity remains
   \(\sqrt{JL}X^\varepsilon\), a factor
   \(\sqrt J/L=H/L+O(L^{-1})\) above the target on intermediate blocks.
   The literal cardinal array cannot inherit the length-\(L\) smooth
   scale cellwise.
5. After the exact finite transform is granted, the surviving source
   obstruction is only the missing coefficientwise map from the moving
   product collar with outer \(g(Q,R)/(QR)\) to the integral
   additive/Kloosterman data of a trace or reciprocity theorem, with a
   target-safe bound preserving the signed outer aggregate.  The review
   does not use absence of a dual transform as an obstruction.

The PASS is for an exact inconclusive reduction and scoped source no-go.
It is not a PASS for the target estimate.

## 2. Exact statement and hypotheses reviewed

The review takes the accepted literal regime

\[
 J=\sqrt X,\qquad H=\sqrt J+O(1),\qquad 1\ll L\ll H,
\]

the exact disjoint-cardinal interpolant \(\mathcal B\), supported away
from the axes and extended by zero outside the positive quadrant, and the
two-variable Euler series

\[
 G(s_1,s_2)=\sum_{Q,R\ge1}g(Q,R)Q^{-s_1}R^{-s_2}.
\]

The candidate proves the local table

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p&1&-1&-1&-\chi_4(p)&1&\chi_4(p)
\end{array}
\]

for odd \(p\), with the separate two-adic coefficients
\((0,0)\mapsto1\) and \((0,2)\mapsto-1\).  Its collapsed law is

\[
 g(Q,R)=\chi_4(Q)
 \sum_{\substack{u,v,c\ge1; u,c\ \mathrm{odd}\\
 [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c).
\tag{2.1}
\]

All outer \((Q,R)\)-sums in the physical identity are finite because a
nonzero term has \(Q\le M_x\), \(R\le M_z\), the positive support
diameters of \(\mathcal B\).  With the Fourier convention fixed by the
sine/cosine form (169.C5), the candidate's exact identity is

\[
 \mathcal S_{L,1}
 =\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}(k/(4Q),\ell/R).
\tag{2.2}
\]

Writing \(Z_{\mathrm{phys}}\) for the \(\ell=0\) term and retaining the
accepted full Mellin residue \(R_\zeta\), the exact remainder is

\[
 \mathcal I_\eta=E_0+\frac i2
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\ne0}\widetilde{\mathcal B}(k/(4Q),\ell/R),
 \qquad E_0=Z_{\mathrm{phys}}-R_\zeta.
\tag{2.3}
\]

The only favorable positive interior stationary branch has

\[
 k\ell=XQR,\qquad Q\ell\le Rk\le4Q\ell,
\tag{2.4}
\]

and a recombined smooth radial block of physical length \(L\) broadens
this to

\[
 |k\ell-XQR|\ll QRJ/L.
\tag{2.5}
\]

The review treats (2.2)--(2.3), not the favorable model (2.5), as the
literal theorem.  It also retains the distinction between the finite
physical outer sum in (2.2) and the infinite \(R\)-sum in the residue.

## 3. Proof and derivation audit

### 3.1 No external source theorem enters the internal identity

The candidate's dependency chain for the equality is

\[
 \text{local Euler algebra}
 \longrightarrow \text{collapsed Möbius identity}
 \longrightarrow \text{finite physical convolution}
 \longrightarrow \text{two exact Poisson formulae}.
\]

At an odd prime, the eight binary states of \((u,v,c)\) in (2.1) give
the six nonzero local pairs in the displayed table; the two
\((2,2)\)-states cancel.  At \(2\), the restrictions \(u,c\) odd leave
only the two required states.  This proves the coefficient law without
any analytic source.

Substitution into the finite lattice support gives

\[
 \mathcal S_{L,1}=
 \sum_{Q,R}^{\mathrm{phys}}g(Q,R)
 \sum_{m,n\in\mathbb Z}\chi_4(m)\mathcal B(Qm,Rn).
\tag{3.1}
\]

The character formula

\[
 \sum_m\chi_4(m)f(m)=\frac i2
 \sum_{k\ \mathrm{odd}}\chi_4(k)\widehat f(k/4)
\]

has the correct constant because \(\tau(\chi_4)=2i\); ordinary Poisson
in the second variable and Fourier scaling give exactly the
\((QR)^{-1}\) in (2.2).  Pairing \(k,-k\) and \(\ell,-\ell\) gives the
factor \(2\), sine \(\sin(\pi kx/(2Q))\), and cosine
\(\cos(2\pi\ell z/R)\) in (169.C5).  Hence there is no suppressed
normalization or parity factor.

The completed GL(1) equations are used only to identify these same
rank-one Fourier kernels and the lawful contour organization.  The
candidate explicitly forbids the invalid alternative of shifting an
infinite, absolutely expanded \(G\)-series to the left.  The proof of
(2.2) instead occurs after the physical coefficient convolution has
made the \((Q,R)\)-sum finite.  In particular, none of the primary
theorems listed in the hostile source report is needed to prove
(169.C1)--(169.C25).

The only imported mathematical *evidence* in the power paragraph is the
already accepted Round-162 smooth-interior coefficient scale and divisor
count.  The candidate labels their product a route capacity, not a bound
for the literal cardinal scalar.  This use is within the accepted graph
dependency and is not a hidden spectral theorem.

### 3.2 Finite zero mode versus full residue

Before character Poisson, the finite physical zero mode is

\[
 Z_{\mathrm{phys}}=
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{3.2}
\]

The full Mellin residue is instead

\[
 R_\zeta=
 \sum_{Q\le M_x}\sum_{R\ge1}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{3.3}
\]

The infinite \(R\)-tail in (3.3) cannot be deleted termwise: for a
physical block beyond the \(z\)-support, its zero and nonzero Poisson
modes cancel.  Consequently the candidate is correct not to identify
(3.2) with (3.3), and the sign in (2.3) follows directly from
\(\mathcal S_{L,1}=R_\zeta+\mathcal I_\eta\).

At \(x=Qm\), cell disjointness leaves one \(x\)-cell.  There are
\(O(L/Q)\) possible \(m\)'s, \(O(L)\) supported \(z\)-cells, and on
each such cell

\[
 \partial_z(2\pi J\sqrt{xz})=\pi J\sqrt{x/z}\asymp J.
\]

One integration by parts therefore gives

\[
 |Z_{\mathrm{phys}}|
 \ll\frac{L^2}{J}
 \sum_{Q,R}\frac{|g(Q,R)|}{QR}
 \ll\frac{L^2}{J},
\tag{3.4}
\]

because the Euler mass at \((\sigma_1,\sigma_2)=(1,1)\) converges.
Exactly the same argument applied to (3.3), with the convergent full
\(R\)-sum, gives \(|R_\zeta|\ll L^2/J\).  Thus

\[
 |E_0|\le |Z_{\mathrm{phys}}|+|R_\zeta|\ll L^2/J.
\tag{3.5}
\]

This direct argument justifies the no-\(X^\varepsilon\) version in
(169.C4b).  If synthesis cites only the weaker accepted headline
\(R_\zeta\ll_\varepsilon L^2J^{-1}X^\varepsilon\), then (3.5) may be
weakened by \(X^\varepsilon\) with no change to the result.

Finally,

\[
 \frac{L^2/J}{L^{3/2}}=\frac{\sqrt L}{J}
 \le J^{-3/4+o(1)}
\]

for \(L\ll H\asymp J^{1/2}\).  The correction is therefore decisively
target-safe and cannot hide the missing collar gain.

### 3.3 Phase and restored-power audit

For the double-negative Fourier branch the phase is

\[
 J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R}.
\]

Its two stationary equations multiply to \(k\ell=XQR\), and their
ratio maps the literal cone to \(Q\ell\le Rk\le4Q\ell\).  In radial
coordinates the residual frequency is
\(J-\sqrt{k\ell/(QR)}\), yielding (2.5) only for a *recombined smooth
radial block of length \(L\)*.

The accepted interior scale and factor-pair count are

\[
 \frac{L^{3/2}}{QR\sqrt J},\qquad
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon.
\]

Their positive product is

\[
 \sqrt{JL}X^\varepsilon
 =L^{3/2}\left(\frac{\sqrt J}{L}\right)X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{3.6}
\]

Thus the candidate restores, rather than suppresses, the unpaid power.
It also correctly refuses to apply the length-\(L\) scale to one unit
cardinal cell or to sum transformed \((Q,R)\)-blocks absolutely.

### 3.4 Surviving source seam

Once (2.2)--(2.5) are granted, the hostile source audit leaves one exact
source question: can the signed aggregate with outer
\(g(Q,R)/(QR)\), moving arbitrary-real centre \(XQR\), product width
\(QRJ/L\), literal cardinal weight, common-prime and two-adic branches,
and complete main/continuous/exceptional pieces be mapped into a primary
trace or reciprocity theorem with target-safe norms?

The audited answer is no for the dated theorem set:

- Blomer--Harcos and Blomer--Jana--Nelson require fixed integral
  *additive* shifts and fixed cuspidal GL(2) coefficient systems.
- Kuznetsov starts with an already derived integral Kloosterman sum at a
  fixed level and cusps; a product collar is not a modular inverse.
- Pascadi's moving-level Kloosterman bounds require coprime integral
  level factors, smooth modulus weights, Assumption 14, and finish with a
  positive outer \(\ell^2\) norm.
- Blomer--Khan and Motohashi-type formulas act on complete
  one-parameter automorphic moments and retain mandatory main and
  continuous terms.

These theorem hypotheses are not used in the internal proof.  They are
used only to justify the narrow negative source-placement conclusion.
Accordingly, the source no-go begins at the collar-to-trace-formula map,
not at the existence of a finite dual transform.

## 4. First doubtful or unproved step

The first open step after this candidate is exactly the nonzero-frequency
estimate

\[
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}(k/(4Q),\ell/R)
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{4.1}
\]

or an endpoint-lawful equivalent.  The target-safe \(E_0\) may be
discarded only after (3.5), as the candidate does.

For a source attack, the first missing interface is not Poisson or
functional-equation dualization.  It is an exact coefficientwise
construction of integral levels, cusps, Fourier indices, moduli, modular
inverses, smooth Bessel weights, and derivative norms from the moving
product collar, while keeping the single signed \((Q,R,k,\ell)\)
aggregate through all main, continuous, and exceptional terms.  No
audited theorem performs this construction.

The favorable capacity (3.6) is only a route ledger.  It neither proves a
lower bound nor excludes a future bespoke signed theorem.

## 5. Control tests and outcomes

| Control | Outcome | Reviewer finding |
|---|---|---|
| Internal identity imports no spectral source | **PASS** | (169.C1)--(169.C25) follow from finite algebra, Poisson, Mellin kernels, and elementary analysis.  The source report is used only negatively. |
| Local \(G\) table and \(p=2\) | **PASS** | The eight odd-prime states and two two-adic states reproduce the exact Euler coefficients; the \((2,2)\) pair cancels. |
| Weighted \(G\)-mass | **PASS** | The \(\eta^{-3}\) law is correct, and the only absolute mass used after Poisson is the convergent \((1,1)\) mass for the harmless zero term. |
| Character-Poisson constant and parity | **PASS** | \(\tau(\chi_4)=2i\) gives \(i/2\), only odd \(k\), and the paired sine normalization in (169.C5). |
| Ordinary-Poisson normalization | **PASS** | Scaling supplies \((QR)^{-1}\); pairing nonzero \(\ell\) gives the stated cosine and factor \(2\). |
| Finite physical outer sum | **PASS** | It is obtained before contour displacement; no infinite post-shift resummation of \(G\) occurs. |
| Finite zero mode is not the full residue | **PASS** | (169.C23) has finite \(R\), while (169.C23a) has the full \(R\)-sum; (2.3) has the correct correction and sign. |
| Zero/residue correction harmless | **PASS** | Equations (3.4)--(3.5) prove \(E_0\ll L^2/J\), which is below target. |
| Completed functions, gamma parity, and contour orientation | **PASS** | The zeta pole, entire odd-character completion, sine/cosine kernels, pole-zero cancellation at zero, and reversed orientations are all retained. |
| Exact Round-162 self-return | **PASS** | Substitution of (2.1) into (2.2) restores the Möbius signs, character, \(p=2\), moduli, and both Fourier frequencies coefficientwise. |
| Literal endpoints versus smooth model | **PASS** | The exact identity uses the cardinal array; the candidate explicitly marks the length-\(L\) collar as favorable smooth-interior evidence only. |
| Restored collar power | **PASS** | Equation (3.6) preserves the \(H/L\) deficit and does not credit a fictitious spectral square root. |
| Exact source applicability | **PASS as a narrow no-go** | No audited primary theorem accepts the moving product collar and exact signed outer weight.  This is the sole surviving source seam. |
| False unsigned/aligned/\(G=1\) controls | **PASS** | The candidate observes that the rank-one transform alone also survives these controls, so it claims no cancellation from dualization. |
| Target theorem | **FAIL / correctly left open** | Equation (4.1) is not proved.  This failure is the claimed conclusion, not a defect in the reduction. |
| Downstream quarantine | **PASS** | No other channel, parent, bridge, theorem, or exponent is promoted. |

No repair is required for the source or power conclusion.  A
non-blocking synthesis clarification is to cite (3.3)--(3.5), rather
than only the weaker headline Round-168 residue bound, when retaining the
candidate's no-\(X^\varepsilon\) display for \(E_0\).

## 6. Dependencies and exact artifacts used

The review used:

- `candidates/conductor_round169_joint_fe_double_poisson_self_return.md`;
- `reports/signed_spectral_reciprocity_source_hostile_audit.md`;
- `proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `strategy/round169_m2_hard_top_t1_joint_functional_equation_spectral_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/barrier_packet.md`;
- the Round-169 source-auditor brief and the repository protocol.

For source applicability, the exact primary theorem set and URLs are
recorded in the hostile source report: Blomer--Harcos;
Blomer--Jana--Nelson; Deshouillers--Iwaniec; Pascadi; Blomer--Khan;
Topacogullari; and Kwan.  No primary theorem from that list is invoked to
prove the candidate's internal identities.

The starting graph hash is
`a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`.
This review made no numerical experiment and edited no state, synthesis,
validation, or candidate file.

## 7. Recommended state effect

**Recommended state effect: PASS the source/spectral/power seam review.**

Subject to the other independent seam and graph-scope reviews, the
candidate may be promoted only as one `proved_internal` *reduction* node
containing:

- the exact local and collapsed \(g\)-law;
- the finite physical double-Poisson identity;
- the finite-zero/full-residue correction \(E_0\);
- the completed-function/Fourier-kernel ledger; and
- the scoped coefficientwise self-return to the Round-162 signed family.

It must remain inconclusive evidence below the open signed-cone owner.
Do not promote (4.1), a strict polynomial sector, the full \(t=1\)
scalar, or any downstream theorem or exponent.

The closing source statement should be exactly: the finite dual transform
exists, its zero/residue mismatch is target-safe, and the current audited
literature does not supply the exact collar-to-trace-formula placement
needed to exploit the signed \(g(Q,R)/(QR)\) aggregate.  The appropriate
scoped mechanism label remains
`t1_joint_FE_spectral_self_return_no_go`.

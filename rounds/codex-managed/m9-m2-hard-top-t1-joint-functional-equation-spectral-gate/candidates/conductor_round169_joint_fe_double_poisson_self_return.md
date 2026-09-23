# Round 169 conductor candidate: exact joint-FE double-Poisson self-return

- Campaign: `m9-m2-hard-top-t1-joint-functional-equation-spectral-gate`
- Starting graph: `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`
- Role: conductor-selected candidate
- Evidence status: candidate only until all seam reviews pass

## 1. Result

Let \(\mathcal B\) be the exact disjoint-cardinal interpolant in the
accepted Round-168 kernel, extended by zero outside the positive quadrant,
and use

\[
 \widetilde{\mathcal B}(\xi,\nu)
 :=\iint_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\nu z)\,dx\,dz.
\tag{169.C0}
\]

Write

\[
 G(s_1,s_2)=\sum_{Q,R\geq1}\frac{g(Q,R)}{Q^{s_1}R^{s_2}}.
\tag{169.C1}
\]

The coefficients \(g\) admit an exact prime-by-prime law, an exact
collapsed-Mobius law, and a finite physical double-Poisson transform.  In
particular,

\[
 \boxed{
 g(Q,R)=\chi _4(Q)
 \sum_{\substack{u,v,c\geq1;\ u,c\ \mathrm{odd}\\
                  [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c).}
\tag{169.C2}
\]

If \(\sum^{\rm phys}_{Q,R}\) denotes the canonical finite outer sum
obtained from the physical convolution (equivalently, take the finite
rectangle bounded by the positive support suprema of \(\mathcal B\);
any extra pre-Poisson block in that rectangle is identically zero), then

\[
 \boxed{
 \mathcal S_{L,1}
 =\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
   \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi _4(k)
   \sum_{\ell\in\mathbb Z}
   \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.C3}
\]

Let \(Z_{\mathrm{phys}}\) be the \(\ell=0\) term of (169.C3).  It is a
finite physical truncation of, but is not literally equal to, the
accepted cardinal zeta residue \(R_\zeta\).  Put

\[
 E_0:=Z_{\mathrm{phys}}-R_\zeta.
\tag{169.C4a}
\]

The exact residue correction is target-safe:

\[
 Z_{\mathrm{phys}}\ll L^2/J,
 \qquad E_0\ll L^2/J.
\tag{169.C4b}
\]

Hence the exact Round-168 signed two-height remainder is

\[
 \boxed{
 \mathcal I_\eta
 =E_0+\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
   \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi _4(k)
   \sum_{\ell\ne0}
   \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.C4}
\]

Equivalently,

\[
 \mathcal I_\eta
 =E_0+2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
   \sum_{\substack{k\geq1\\k\ \mathrm{odd}}}\chi _4(k)
   \sum_{\ell\geq1}\iint \mathcal B(x,z)
   \sin\!\frac{\pi kx}{2Q}\cos\!\frac{2\pi\ell z}{R}\,dx\,dz.
\tag{169.C5}
\]

The only positive interior stationary branch has phase

\[
 J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R},
\tag{169.C6}
\]

and therefore

\[
 \boxed{k\ell=XQR},\qquad
 \boxed{Q\ell\leq Rk\leq4Q\ell}.
\tag{169.C7}
\]

Substitution of (169.C2) into (169.C3) is coefficientwise exactly the
accepted Round-162 Mobius opening followed by character Poisson in the
first variable and ordinary Poisson in the second.  Thus bare joint
application of the two GL(1) functional equations is an exact collapsed
self-return of the full scalar to the pre-stationary Round-162 signed
family.  For \(\mathcal I_\eta\), the return holds up to the explicit
target-safe correction \(E_0\).  It supplies no estimate for the
nonzero-frequency aggregate in (169.C4).

On a favorable recombined smooth interior block only, radial support of
length \(L\) broadens (169.C7) to

\[
 |k\ell-XQR|\ll QRJ/L.
\tag{169.C8}
\]

The accepted coefficient scale and divisor count then give the same
termwise-positive capacity \(\sqrt{JL}X^\varepsilon\) as Round 162,
whose ratio to \(L^{3/2}X^\varepsilon\) is
\(H/L+O(L^{-1})\).  Absolute summation over the outer blocks is not
target-safe.  For the literal cardinal array, the \(O(L^2)\) unit-cell
complexity prevents importing this favorable length-\(L\) radial model
without a separately proved recombination theorem.

Round 169 therefore closes this mechanism only under
`t1_joint_FE_spectral_self_return_no_go`.  The full polynomial-range
\(t=1\) scalar, the signed two-height estimate, and every parent and
global exponent remain open.

## 2. Exact coefficient and completed-function statement

For every odd prime \(p\), the nonzero local coefficients are

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p&1&-1&-1&-\chi _4(p)&1&\chi _4(p),
\end{array}
\tag{169.C9}
\]

and at \(2\) they are \((0,0)\mapsto1\) and \((0,2)\mapsto-1\).
Consequently \(Q\) is odd and both variables are cube-free on the
support.  For \(\sigma_1,\sigma_2>1/2\),

\[
\begin{aligned}
 \sum_{Q,R}\frac{|g(Q,R)|}{Q^{\sigma_1}R^{\sigma_2}}
 ={}&(1+2^{-2\sigma_2})\prod_{p>2}
 \bigl(1+p^{-2\sigma_1}+p^{-2\sigma_2}
 +p^{-\sigma_1-\sigma_2}\\
 &\hspace{35mm}+p^{-2\sigma_1-\sigma_2}
 +p^{-\sigma_1-2\sigma_2}\bigr).
\end{aligned}
\tag{169.C10}
\]

At \(\sigma_1=\sigma_2=1/2+\eta\), uniformly for
\(0<\eta\leq1/4\), this is

\[
 (1+2^{-1-2\eta})\prod_{p>2}
 (1+3p^{-1-2\eta}+2p^{-3/2-3\eta})
 \asymp\zeta(1+2\eta)^3\asymp\eta^{-3}.
\tag{169.C11}
\]

The completed functions are

\[
 \Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \Lambda_\zeta(s)=\Lambda_\zeta(1-s),
\tag{169.C12}
\]

and

\[
 \Lambda_4(s)=\left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi _4),
 \qquad \Lambda_4(s)=\Lambda_4(1-s).
\tag{169.C13}
\]

Zeta has even parity, conductor and root number one, and its completion
has poles at zero and one.  The primitive character \(\chi_4\) has
conductor four, odd parity, Gauss sum \(2i\), root number one, and entire
completion.  Equivalently,

\[
 \zeta(s)=X_\zeta(s)\zeta(1-s),\qquad
 X_\zeta(s)=\pi^{s-1/2}
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
\tag{169.C14}
\]

\[
 L(s,\chi _4)=X_4(s)L(1-s,\chi _4),\qquad
 X_4(s)=\left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)}.
\tag{169.C15}
\]

The exact kernel identities

\[
 X_\zeta(s)=2^s\pi^{s-1}\Gamma(1-s)\sin(\pi s/2),
\qquad
 X_4(s)=\left(\frac\pi2\right)^{s-1}
 \Gamma(1-s)\cos(\pi s/2)
\tag{169.C16}
\]

are respectively the Mellin kernels of \(2\cos(2\pi u)\) and
\(\sin(\pi u/2)\).  They explain the cosine and odd-character sine
transforms in (169.C5).

## 3. Proof and exact self-return

### 3.1 Euler coefficients and Mobius collapse

For odd \(p\), put \(x=\chi_4(p)p^{-s_1}\) and \(y=p^{-s_2}\).  Then

\[
 G_p=(1+x+y)(1-x)(1-y)
 =1-x^2-y^2-xy+x^2y+xy^2,
\tag{169.C17}
\]

which proves (169.C9).  The factor \(G_2=1-2^{-2s_2}\) gives the
two-adic table.  Taking absolute values locally proves (169.C10), and
comparison of local logarithms with \(\zeta(1+2\eta)^3\) proves
(169.C11).

To prove (169.C2), expand the exact projector

\[
 \mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1}
 =\sum_{u^2\mid d_1}\mu(u)
  \sum_{v^2\mid d_2}\mu(v)
  \sum_{c\mid(d_1,d_2)}\mu(c).
\tag{169.C18}
\]

Set \(Q=[u^2,c]\), \(R=[v^2,c]\).  The character forces \(u,c,Q\)
odd, and \(\chi_4(Qm)=\chi_4(Q)\chi_4(m)\).  At an odd prime the eight
binary states of \((v_p(u),v_p(v),v_p(c))\) produce

\[
\begin{array}{c|rrrrrrrr}
(u,v,c)&000&100&010&001&110&101&011&111\\ \hline
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,2)&(2,1)&(1,2)&(2,2)\\
\chi_4(Q)\mu(u)\mu(v)\mu(c)&1&-1&-1&-\chi_4(p)&1&1&\chi_4(p)&-1.
\end{array}
\tag{169.C19}
\]

The two \((2,2)\) contributions cancel.  At \(p=2\),
\(v_2(u)=v_2(c)=0\) while \(v_2(v)=0\) or \(1\), giving precisely
the two-adic table.  This proves (169.C2) prime by prime.

Equivalently, for every positive pair,

\[
 \chi_4(d_1)\mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1}
 =\sum_{Q\mid d_1}\sum_{R\mid d_2}
 g(Q,R)\chi_4(d_1/Q).
\tag{169.C20}
\]

### 3.2 Lawful joint transform, pole, and contours

Applying (169.C20) at the finitely many lattice points in the support of
\(\mathcal B\) gives

\[
 \mathcal S_{L,1}
 =\sum_{Q,R}^{\rm phys}g(Q,R)
   \sum_{m,n\in\mathbb Z}\chi_4(m)\mathcal B(Qm,Rn).
\tag{169.C21}
\]

The exact character and ordinary Poisson formulae are

\[
 \sum_m\chi_4(m)f(m)
 =\frac i2\sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}
 \chi_4(k)\widehat f(k/4),
 \qquad
 \sum_n h(n)=\sum_{\ell\in\mathbb Z}\widehat h(\ell).
\tag{169.C22}
\]

Fourier scaling by \(Q,R\) proves (169.C3).  Before character Poisson,
its \(\ell=0\) part is

\[
 Z_{\mathrm{phys}}=\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{169.C23}
\]

The finite \(R\)-range here matters.  If \(M_x\) is the positive
\(x\)-support diameter, the Round-168 residue is instead

\[
 R_\zeta=\sum_{Q\leq M_x}\sum_{R\geq1}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{169.C23a}
\]

Its one-variable Dirichlet series is \(L(s,\chi_4)G(s,1)\), including
\(G_2(s,1)=3/4\).  The \(Q\)-sum is finite because \(Qm\) must meet the
positive \(x\)-support, but the residue contains the full \(R\)-sum.
Thus \(Z_{\mathrm{phys}}\neq R_\zeta\) in general.

This mismatch is nevertheless target-safe.  At \(x=Qm\), disjointness
of the cardinal cells leaves only the cell centred at that integer.
Each supported \(z\)-cell has phase derivative \(\asymp J\), so one
integration by parts gives \(O(J^{-1})\).  There are \(O(L/Q)\)
possible \(m\)'s and \(O(L)\) possible \(z\)-cells.  Therefore

\[
 |Z_{\mathrm{phys}}|
 \ll\frac{L^2}{J}\sum_{Q,R}\frac{|g(Q,R)|}{QR}
 \ll\frac{L^2}{J}.
\tag{169.C23b}
\]

The last Euler product is (169.C10) at
\(\sigma_1=\sigma_2=1\).  Combining (169.C23b) with the accepted
Round-168 bound for \(R_\zeta\) proves (169.C4a)--(169.C4b).
Subtracting \(R_\zeta\) from (169.C3) proves (169.C4), and pairing
\(k\) with \(-k\) and \(\ell\) with \(-\ell\) proves (169.C5).

Equivalently, one may extend the physical \(R\)-blocks to all
\(R\geq1\) before splitting frequencies.  Blocks beyond the positive
\(z\)-support are zero only after their zero and nonzero Poisson modes
cancel.  In block-grouped order their full zero-mode sum is (169.C23a),
and their nonzero modes supply exactly \(E_0\).  This is why a finite
zero mode cannot be silently identified with the Mellin residue.

Equations (169.C12)--(169.C16) give the Mellin derivation of the same
two summation kernels.  For the intact factorization \(L\zeta G\), the
initial displacement of the zeta contour from \(\Re s_2>1\) to
\(1/2+\eta\) crosses only \(s_2=1\), producing the full residue
(169.C23a); the character contour crosses no pole.  Separately, for each
block of the finite physical convolution (169.C21), the same displacement
produces that block's share of \(Z_{\mathrm{phys}}\), after which the
remaining contours may be shifted coefficientwise to
\(\Re s_j=-\delta\), where the dual Dirichlet series converge.  Summing
these finite block identities gives the nonzero-frequency term in
(169.C4); the difference between the two contour organizations is exactly
\(E_0\).  The
apparent zeta singularity at zero cancels inside
\(X_\zeta(s)\zeta(1-s)=\zeta(s)\), and reversing
\(w_j=1-s_j\) restores upward orientation without a residual sign.

It would be illicit to expand the infinite \(G\)-series on the
\(1/2+\eta\) lines and then resum it absolutely after this left shift:
the factors \(Q^{-s_1}R^{-s_2}\) grow there, and (169.C11) no longer
applies.  The finite physical convolution (169.C21), followed by exact
Poisson, is the lawful order and proves that no contour or coefficient
reordering is hidden in (169.C3)--(169.C5).

### 3.3 Phase, collar, and restored power

Only the double-negative branch of (169.C5) can be stationary in the
positive quadrant.  Its stationary equations are

\[
 \frac J2\sqrt{z/x}=\frac{k}{4Q},\qquad
 \frac J2\sqrt{x/z}=\frac{\ell}{R},
\tag{169.C24}
\]

which prove (169.C7), including the exact image of the physical cone.
Writing \(x=rw\), \(z=r/w\), angular stationarity leaves radial phase

\[
 r\left(J-\sqrt{\frac{k\ell}{QR}}\right).
\tag{169.C25}
\]

It vanishes identically at exact resonance.  On a favorable global
smooth radial block of length \(L\), (169.C25) gives (169.C8).  The
accepted Round-162 stationary coefficient and factor-pair count are

\[
 \frac{L^{3/2}}{QR\sqrt J},\qquad
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon,
\tag{169.C26}
\]

so their positive product is \(\sqrt{JL}X^\varepsilon\), with the
unpaid factor \(H/L+O(L^{-1})\).  Substituting (169.C2) into (169.C3)
recovers every Round-162 opening sign, character, normalization,
two-adic branch, and frequency.  The gamma parities have become exactly
the sine and cosine kernels.  The finite zero mode is (169.C23), the full
Mellin residue is (169.C23a), and their difference is target-safe.
Hence this is an exact coefficientwise self-return of the full scalar,
and a self-return up to a proved safe term for \(\mathcal I_\eta\), not
an analogy.

The calculation (169.C26) remains a smooth-interior route capacity, not
an estimate for the exact cardinal array.  A unit cardinal cell has
unit radial bandwidth rather than length-\(L\) bandwidth, and summing
cellwise bounds pays the cardinal complexity.  No endpoint-lawful
recombination theorem or new signed estimate is proved here.

## 4. First doubtful or unproved step

The first open implication is exactly

\[
 E_0+\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{169.C27}
\]

Because \(E_0\) is target-safe, the open part is the complete signed
Round-162 Mobius--Poisson family in collapsed coordinates.  The
functional equations, coefficient
algebra, and rank-one phase supply no cancellation among \((Q,R)\),
nearby products \(k\ell\), or cardinal cells.  A successful next theorem
must act on that single signed aggregate before positive norms.

This is a scoped no-go for bare joint-FE dualization and the named
termwise-positive placements.  It is not a physical lower bound, not a
universal impossibility theorem, and not a rejection of a future bespoke
signed spectral or reciprocity estimate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact \(G\) law and \(p=2\) | Pass: (169.C9), (169.C17), (169.C19). |
| Weighted \(\ell^1\) and epsilon order | Pass: (169.C10)--(169.C11); the cost is finite for fixed post-\(\varepsilon\) \(\eta\), but is not used after the transform. |
| Completed functions, gamma parity, roots, poles | Pass: (169.C12)--(169.C16), (169.C23). |
| Contour direction and summation order | Pass with the explicit prohibition following (169.C23). |
| Literal cardinal/endpoints | Pass as an exact identity; fail as an unproved smooth recombination. |
| Finite zero mode versus full residue | Pass: (169.C23)--(169.C23b) give the exact target-safe correction. |
| Dual constants, phase, lengths | Pass: (169.C3)--(169.C8), (169.C24)--(169.C26). |
| No early positive norm or common height | Pass.  Both independent kernels remain signed through the phase calculation. |
| Exact Round-162 comparison | Pass coefficientwise by (169.C2) and (169.C21)--(169.C26). |
| False unsigned, aligned, and \(G=1\) controls | Pass as route falsifiers: the rank-one collar survives each, so the transform alone distinguishes none of them. |
| Target gain | Open: (169.C27) is not proved. |
| Source applicability | No audited primary theorem accepts the moving product collar, literal cardinal weight, and signed outer \(g(Q,R)\)-aggregate with target-safe restored powers.  No external theorem is used in the internal identities. |
| Downstream scope | Pass: no parent, bridge, theorem, or exponent is promoted. |
| Round 170 scheduling | Pass: the mandatory strategy/current-literature review remains next. |

No numerical experiment is used; the candidate is 100% analytic and
algebraic.

## 6. Dependencies and exact artifacts used

The candidate uses the accepted Round-168 Mellin--Euler/cardinal kernel,
the accepted Round-162 character-Poisson/collar kernel, the Round-169
barrier packet, the Round-169 discovery report, and the independent blind
rederivation.  The hostile source report is used only for the dated
source-interface no-go.  The local coefficient table, Mobius collapse,
exact finite double-Poisson identity, finite-zero/full-residue correction,
and functional-equation kernel ledger are internal.

No external source theorem is used to prove (169.C1)--(169.C27), and no
computation is used as mathematical evidence.

## 7. Recommended state effect

After independent coefficient/gamma, literal-transform, source/power,
and graph-scope reviews, create one `proved_internal` reduction node for
the exact coefficient law, weighted mass, Mobius collapse, completed-
function kernel, double-Poisson identity, finite-zero/full-residue
correction, and scoped
joint-FE self-return.  Add it only as inconclusive evidence below the open
hard-TOP signed-cone owner.

Reject only the claims that bare joint functional equations, an infinite
post-shift absolute resummation of \(G\), the favorable smooth collar, or
the named positive placements prove the signed target.  Keep the full
\(t=1\) scalar and residual, every other hard-TOP channel, hard TOP, BAL,
UNBAL, M9--M2, both direct M1 parents, GAR, endpoint uniformity, M9, both
bridges, the quarter theorem, and both exponent ledgers unchanged.

# Independent coefficient, gamma, residue, and transform seam review

- Campaign: `m9-m2-hard-top-t1-joint-functional-equation-spectral-gate`
- Round: 169
- Role: independent seam reviewer, not claimant
- Candidate reviewed: `candidates/conductor_round169_joint_fe_double_poisson_self_return.md`
- Verdict: **PASS**

## 1. Result

**PASS.**  The audited mathematical seam is correct.  In particular:

1. the six odd-prime coefficients of \(G\), the exceptional \(p=2\) branch, and the \(\eta^{-3}\) absolute coefficient mass are exact;
2. the collapsed Möbius formula for \(g(Q,R)\) reproduces those local coefficients, including cancellation of the two \((2,2)\) states;
3. both completed functions, root numbers, gamma quotients, sine/cosine Mellin kernels, Fourier scalings, and the factor \(i/2\) in character Poisson are normalized correctly;
4. the conductor candidate correctly distinguishes the finite physical ordinary-Poisson zero mode \(Z_{\mathrm{phys}}\) from the full Mellin residue \(R_\zeta\);
5. both \(Z_{\mathrm{phys}}\) and \(R_\zeta\), and hence
   \(E_0=Z_{\mathrm{phys}}-R_\zeta\), are \(O(L^2/J)\) for the accepted disjoint-cardinal interpolant;
6. subtracting \(R_\zeta\) from the full finite double-Poisson formula gives exactly (169.C4), and pairing signs gives exactly (169.C5);
7. the only positive interior stationary branch has
   \(k\ell=XQR\), and the physical cone is exactly
   \(Q\ell\leq Rk\leq4Q\ell\).

Thus the finite-zero/full-residue correction repairs the only delicate normalization seam without changing the nonzero-frequency obstruction.  The candidate proves an exact reduction/self-return, not the target bound.  Its first open step remains the signed estimate (169.C27).

For complete self-containment, the candidate should continue to interpret
\(\widetilde{\mathcal B}\) with the convention

\[
 \widetilde{\mathcal B}(\xi,\nu)
 :=\iint_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\nu z)\,dx\,dz
\tag{R169.1}
\]

and \(\sum^{\mathrm{phys}}\) as a fixed finite rectangular block range bounded by the positive support maxima.  These conventions are already forced by (169.C21)--(169.C22); spelling them out would be editorial, not a mathematical repair.

## 2. Exact statement and hypotheses reviewed

This review checks the Round-169 candidate against the accepted Round-168 disjoint-cardinal kernel under the following exact hypotheses.

1. \(J=\sqrt X\), \(H=\sqrt J+O(1)\), and \(1\ll L\ll H\).
2. \(\mathcal B\) is precisely
   \[
   \mathcal B(x,z)=e(J\sqrt{xz})
   \sum_{n,m}A_{L,X}(n,m)\psi(x-n)\psi(z-m),
   \]
   where \(\psi\in C_c^\infty((-1/3,1/3))\), \(\psi(0)=1\), the cells are disjoint, the amplitude is uniformly bounded, and the function is extended by zero outside the positive quadrant.
3. Every physical shell, cone edge, star, floor, profile point value, transition value, parity convention, and zero extension is encoded in the finite values \(A_{L,X}(n,m)\); none is smoothed or altered in the Poisson calculation.
4. The physical outer sum is finite.  One may take all
   \(Q\leq M_x\), \(R\leq M_z\), where \(M_x,M_z\) are positive support maxima; blocks having no physical lattice point vanish only after their full Poisson modes are combined.
5. Fourier transformation uses (R169.1).  The two variables and both dual frequencies remain independent and signed until the stationary equations are derived.

The verdict covers the coefficient, gamma, Möbius, residue, exact-transform, and stationary-phase normalization seams.  It does not review an external source theorem, prove a smooth-cardinal recombination, or certify a downstream graph implication.

## 3. Proof and independent derivation

### 3.1. Euler coefficients, two-adic branch, and \(\eta\)-mass

For an odd prime let \(x=\chi_4(p)p^{-s_1}\),
\(y=p^{-s_2}\).  Then

\[
(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2.
\tag{R169.2}
\]

Since \(\chi_4(p)^2=1\), the coefficient table is

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p&1&-1&-1&-\chi_4(p)&1&\chi_4(p).
\end{array}
\tag{R169.3}
\]

At two, \(G_2=1-2^{-2s_2}\), so the only states are
\((0,0)\mapsto1\) and \((0,2)\mapsto-1\).  Hence \(Q\) is odd and both \(Q,R\) have local exponents at most two.

Taking local absolute values gives, for
\(\sigma_1,\sigma_2>1/2\),

\[
(1+2^{-2\sigma_2})\prod_{p>2}
\left(1+p^{-2\sigma_1}+p^{-2\sigma_2}
+p^{-\sigma_1-\sigma_2}
+p^{-2\sigma_1-\sigma_2}
+p^{-\sigma_1-2\sigma_2}\right).
\tag{R169.4}
\]

At \(\sigma_1=\sigma_2=1/2+\eta\), this is

\[
(1+2^{-1-2\eta})\prod_{p>2}
(1+3p^{-1-2\eta}+2p^{-3/2-3\eta}).
\tag{R169.5}
\]

Multiplication by the local factor
\((1-p^{-1-2\eta})^3\) cancels the only nonsummable first-order term; the remaining logarithm is
\(O(p^{-3/2-3\eta}+p^{-2-4\eta})\).  Therefore (R169.5) is comparable, uniformly for \(0<\eta\leq1/4\), to
\(\zeta(1+2\eta)^3\asymp\eta^{-3}\).  Equations (169.C9)--(169.C11) pass exactly.

### 3.2. Independent check of the collapsed Möbius law

The elementary projector is

\[
\mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1}
=\sum_{u^2\mid d_1}\mu(u)
 \sum_{v^2\mid d_2}\mu(v)
 \sum_{c\mid(d_1,d_2)}\mu(c).
\tag{R169.6}
\]

On the nonzero character support, \(d_1,u,c\) are odd.  Put
\(Q=[u^2,c]\), \(R=[v^2,c]\).  Writing
\(d_1=Qm\) extracts
\(\chi_4(Q)\chi_4(m)\), so collapse over triples gives

\[
g(Q,R)=\chi_4(Q)
\sum_{\substack{[u^2,c]=Q,\ [v^2,c]=R\\u,c\ \mathrm{odd}}}
\mu(u)\mu(v)\mu(c).
\tag{R169.7}
\]

At an odd prime the eight binary states of \((u,v,c)\) give, in order,

\[
\begin{array}{c|cccccccc}
(u,v,c)&000&100&010&001&110&101&011&111\\ \hline
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,2)&(2,1)&(1,2)&(2,2)\\
\text{weight}&1&-1&-1&-\chi_4(p)&1&1&\chi_4(p)&-1.
\end{array}
\tag{R169.8}
\]

The two \((2,2)\) weights cancel, leaving exactly (R169.3).  At two, only \(v_2(v)=0,1\) is possible, giving weights \(1,-1\) at \((0,0),(0,2)\).  This proves (169.C2) and the divisor convolution (169.C20), including all multiplicities and signs.

### 3.3. Completed functions and exact Fourier constants

The even zeta completion and the odd primitive-character completion are

\[
\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Lambda_4(s)=\left(\frac4\pi\right)^{(s+1)/2}
\Gamma((s+1)/2)L(s,\chi_4).
\tag{R169.9}
\]

For \(\chi_4\), \(\tau(\chi_4)=2i\), its parity is one, and
\(\tau(\chi_4)/(i\sqrt4)=1\).  Thus both root numbers are one and

\[
\begin{aligned}
X_\zeta(s)&=\pi^{s-1/2}
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)},\\
X_4(s)&=\left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)}.
\end{aligned}
\tag{R169.10}
\]

Duplication and reflection give

\[
X_\zeta(s)=2^s\pi^{s-1}\Gamma(1-s)\sin(\pi s/2),
\quad
X_4(s)=\left(\frac\pi2\right)^{s-1}
\Gamma(1-s)\cos(\pi s/2).
\tag{R169.11}
\]

With (R169.1), ordinary Poisson and the Gauss-sum calculation give

\[
\sum_{n\in\mathbb Z}h(n)=\sum_{\ell\in\mathbb Z}\widehat h(\ell),
\qquad
\sum_{m\in\mathbb Z}\chi_4(m)f(m)
=\frac i2\sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}
\chi_4(k)\widehat f(k/4).
\tag{R169.12}
\]

Indeed the Gauss sum is
\(\sum_{a\bmod4}\chi_4(a)e(ak/4)=2i\chi_4(k)\), and division by the conductor gives \(i/2\).  Scaling
\((x,z)=(Qm,Rn)\) contributes exactly \(1/(QR)\).  This proves

\[
\mathcal S_{L,1}
=\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac\ell R\right),
\tag{R169.13}
\]

with no missing conductor, sign, or scale.  The gamma identities
(R169.11) are exactly the Mellin kernels of
\(2\cos(2\pi u)\) and \(\sin(\pi u/2)\), so the Mellin and finite Poisson derivations agree.

### 3.4. Finite physical zero mode versus the full Mellin residue

Taking only \(\ell=0\) in the finite physical formula gives, before character Poisson,

\[
Z_{\rm phys}
=\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{R169.14}
\]

By contrast, expanding \(G(s,1)\) in the accepted Round-168 Mellin residue gives

\[
R_\zeta
=\sum_{Q\leq M_x}\sum_{R\geq1}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{R169.15}
\]

The \(Q\)-sum is physically finite because \(Qm\) must meet the positive \(x\)-support.  The \(R\)-sum is not physically truncated: setting \(s_2=1\) integrates the second variable and leaves the full coefficient
\(G(s_1,1)\).  In particular its two-adic factor is
\(1-2^{-2}=3/4\).  Therefore identifying (R169.14) with (R169.15) would be false.

The correction has the claimed strength.  At an integer
\(x=Qm\), disjointness of the cardinal cells selects only the cell with first centre \(Qm\).  For each supported second cell,

\[
\frac d{dz}\bigl(2\pi J\sqrt{Qm\,z}\bigr)
=\pi J\sqrt{Qm/z}\asymp J.
\tag{R169.16}
\]

One integration by parts against the fixed compactly supported \(\psi(z-n)\) is consequently \(O(J^{-1})\), uniformly in every literal centre and endpoint value.  There are \(O(L/Q)\) eligible values of \(m\) and \(O(L)\) second cells.  Hence

\[
\left|\sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz\right|
\ll\frac{L^2}{QJ}.
\tag{R169.17}
\]

Since

\[
\sum_{Q,R\geq1}\frac{|g(Q,R)|}{QR}
=(1+2^{-2})\prod_{p>2}(1+3p^{-2}+2p^{-3})<\infty,
\tag{R169.18}
\]

(R169.17) applies both to the finite \(R\)-sum in (R169.14) and the full \(R\)-sum in (R169.15), yielding

\[
Z_{\rm phys}\ll L^2/J,\qquad
R_\zeta\ll L^2/J,\qquad
E_0:=Z_{\rm phys}-R_\zeta\ll L^2/J.
\tag{R169.19}
\]

This independently supplies the no-\(X^\varepsilon\) form of the correction claimed in (169.C4b); it is slightly stronger than the displayed target-safe Round-168 residue statement and follows from the same accepted cellwise integration by parts.

Now split (R169.13) into \(\ell=0\) and \(\ell\ne0\), and use
\(\mathcal I_\eta=\mathcal S_{L,1}-R_\zeta\).  This gives exactly

\[
\mathcal I_\eta
=E_0+\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac\ell R\right).
\tag{R169.20}
\]

Pairing \(k\) with \(-k\) uses \(\chi_4(-k)=-\chi_4(k)\), while pairing \(\ell\) with \(-\ell\) is even.  The factors are

\[
\frac i2\bigl(e(-A)-e(A)\bigr)=\sin(2\pi A),
\qquad e(-B)+e(B)=2\cos(2\pi B),
\tag{R169.21}
\]

so (R169.20) becomes precisely

\[
\mathcal I_\eta
=E_0+2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\geq1\\k\ \mathrm{odd}}}\chi_4(k)
 \sum_{\ell\geq1}\iint\mathcal B(x,z)
 \sin\!\frac{\pi kx}{2Q}
 \cos\!\frac{2\pi\ell z}{R}\,dx\,dz.
\tag{R169.22}
\]

This verifies both the sign of \(E_0\) and every Fourier constant in (169.C4)--(169.C5).  It also explains why blocks outside the finite physical \(R\)-range cannot be discarded mode by mode: their zero and nonzero ordinary-Poisson modes cancel only after recombination.

### 3.5. Stationary product and cone equations

After expanding the sine and cosine, only the branch

\[
\Phi(x,z)=J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R},
\qquad k,\ell>0,
\tag{R169.23}
\]

can have an interior critical point.  Its equations are

\[
\frac J2\sqrt{z/x}=\frac{k}{4Q},
\qquad
\frac J2\sqrt{x/z}=\frac\ell R.
\tag{R169.24}
\]

Multiplication gives

\[
k\ell=J^2QR=XQR.
\tag{R169.25}
\]

Division gives

\[
\frac{x}{z}=\frac{4Q\ell}{Rk}.
\tag{R169.26}
\]

The literal cone \(z\leq x\leq4z\) is therefore equivalent to

\[
Q\ell\leq Rk\leq4Q\ell.
\tag{R169.27}
\]

With \(x=rw\), \(z=r/w\), angular stationarity leaves

\[
r\left(J-\sqrt{\frac{k\ell}{QR}}\right).
\tag{R169.28}
\]

It vanishes along the radial direction at (R169.25), proving the exact rank-one self-return.  On a granted smooth radial block of length \(L\), the condition for non-negligible radial transform is

\[
\left|J-\sqrt{k\ell/(QR)}\right|\ll L^{-1},
\]

which is equivalent in the stationary range to

\[
|k\ell-XQR|\ll QRJ/L.
\tag{R169.29}
\]

Thus (169.C6)--(169.C8) pass.  The later multiplication of the inherited scale
\(L^{3/2}/(QR\sqrt J)\) by the inherited factor-pair capacity
\((QRJ/L+1)(XQR)^\varepsilon\) has leading size
\(\sqrt{JL}X^\varepsilon\), and
\(\sqrt{JL}/L^{3/2}=\sqrt J/L=H/L+O(L^{-1})\).  This arithmetic is correct, while the candidate properly labels it a favorable smooth-block capacity rather than a literal-cardinal estimate.

### 3.6. Contour and self-return check

The Mellin contour initially crosses only the simple pole of \(\zeta(s_2)\) at \(s_2=1\); \(L(s_1,\chi_4)\) is entire.  For each fixed physical \((Q,R)\) block, after its zeta residue is removed, both contours may be moved left until the dual Dirichlet series converge.  The apparent pole of \(\zeta(1-s_2)\) at \(s_2=0\) is canceled by the zero of \(X_\zeta(s_2)\), and \(w_j=1-s_j\) restores upward orientation without a sign.  The candidate correctly refuses to resum the infinite \(G\)-series absolutely after this shift.

Substitution of (R169.7) into the finite formula (R169.13) is exactly the original squarefree/coprime Möbius opening followed by character Poisson and ordinary Poisson.  Thus the asserted coefficientwise self-return follows internally.  Matching its historical name to every line of the separately accepted Round-162 artifact is outside this seam, but no additional coefficient or normalization is needed for the identity proved here.

## 4. First doubtful or unproved step

No doubtful step remains in the audited seam.  The first unproved implication is exactly the candidate's (169.C27): bounding the complete nonzero-frequency signed aggregate in (R169.20) by
\(L^{3/2}X^\varepsilon\).  The functional equations and double Poisson formula expose a radial phase that is constant at
\(k\ell=XQR\); they do not yield cancellation among nearby products, outer \((Q,R)\)-blocks, Möbius signs, character signs, or the \(O(L^2)\) cardinal cells.

Replacing the exact cardinal array by one favorable length-\(L\) smooth radial block would be a second unproved step unless accompanied by an endpoint-lawful recombination theorem with quantified corrections.  The candidate states this limitation correctly.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| Odd-prime \(G\) coefficients | **PASS**: direct expansion gives exactly (169.C9). |
| Exceptional \(p=2\) branch | **PASS**: only \((0,0)\) and \((0,2)\), with weights \(1,-1\); \(G_2(s,1)=3/4\). |
| Weighted \(G\)-mass at \(1/2+\eta\) | **PASS**: exact product (R169.5), uniformly \(\asymp\eta^{-3}\). |
| Collapsed Möbius coefficients | **PASS**: all eight odd-prime states and both two-adic states reproduce the Euler table coefficientwise. |
| Completed functions and roots | **PASS**: zeta is even with conductor/root \(1\); \(\chi_4\) is odd, conductor \(4\), Gauss sum \(2i\), root \(1\). |
| Gamma-to-Fourier constants | **PASS**: \(2\cos(2\pi u)\), \(\sin(\pi u/2)\), character factor \(i/2\), and scaling \(1/(QR)\) all agree. |
| Finite physical zero mode | **PASS**: (R169.14) is the exact \(\ell=0\) term of the finite double-Poisson identity. |
| Full Mellin residue | **PASS**: (R169.15) retains the full \(R\geq1\) coefficient sum and is not identified with \(Z_{\rm phys}\). |
| Correction size | **PASS**: (R169.17)--(R169.19) prove \(Z_{\rm phys},R_\zeta,E_0\ll L^2/J\). |
| Exact \(\mathcal I_\eta\) formula | **PASS**: subtracting the full residue gives the sign and modes in (169.C4), and pairing gives (169.C5). |
| Contour order | **PASS**: finite physical collapse precedes the left shift; no invalid post-shift absolute resummation of \(G\) occurs. |
| Stationary product | **PASS**: \(k\ell=XQR\). |
| Stationary cone | **PASS**: \(Q\ell\leq Rk\leq4Q\ell\). |
| Near-collar width | **PASS**, conditional on the explicitly favorable smooth block: \(|k\ell-XQR|\ll QRJ/L\). |
| Literal cardinal endpoints | **PASS** for the exact identity; correctly left open for smooth recombination. |
| Positive-norm/unsigned control | **PASS** as a route obstruction: no positive norm is used to manufacture signed cancellation. |
| Downstream scope | **PASS**: the target and every parent/global exponent remain open. |

No numerical or external-source control was needed for this exact algebraic seam.

## 6. Dependencies and exact artifacts used

The review used only:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md` (the accepted Round-168 kernel supplied for this review);
3. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/candidates/conductor_round169_joint_fe_double_poisson_self_return.md`.

No sibling report, Round-169 blind report, source audit, barrier packet, strategy file, proof graph, synthesis, state patch, or shared proof-state file was read.  No web source or computation was used.

## 7. Recommended state effect

**PASS the conductor candidate on the independent coefficient/gamma/residue/transform seam.**  Subject to the other required reviews, the exact local coefficient law, \(\eta\)-mass, collapsed Möbius law, completed-function kernels, finite double-Poisson identity, finite-zero/full-residue correction, and stationary product/cone self-return are suitable for a scoped internal reduction node.

Do not promote (169.C27), the polynomial-range \(t=1\) target, a literal-cardinal smooth estimate, any parent obligation, or any exponent.  This review makes no shared-state edit.

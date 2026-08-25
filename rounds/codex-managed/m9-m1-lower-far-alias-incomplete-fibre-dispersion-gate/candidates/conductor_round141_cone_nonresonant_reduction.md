# Round 141 conductor candidate: cone reduction, microscopic cells, and incomplete-fibre no-go

## 1. Result

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad 0\le q\le2y,
\tag{141.C1}
\]

fix \(0<\rho<1/8\), and retain the exact Round-140 coefficient

\[
 A_\rho(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
 r\ge r_h+2}}\chi_4(r),
\qquad
 r_h=\min\left\{r\ge {4Nh\over D_h^2}:r\ \mathrm{positive\ odd}\right\},
\tag{141.C2}
\]

where

\[
 D_h=y-\left\lfloor{\rho y\over\sqrt h}\right\rfloor-1.
\tag{141.C3}
\]

Define the floor-free cone coefficient

\[
 C(m)=\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\tag{141.C4}
\]

On the disjoint dyadic blocks

\[
 \mathcal I_M=[M,2M)\cap[1,M_*],\qquad
 M_*=C_VN/R^2\asymp R^2,
\tag{141.C5}
\]

put

\[
 k_m=\left\lfloor\sqrt{Nm}+{1\over2}\right\rfloor,
 \qquad j_m=k_m^2-Nm,
\tag{141.C6}
\]

with the lower nearest-integer endpoint included.  Then the frozen
Round-141 scalar has the strict owner-complete reduction

\[
 \boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{141.C7}
\]

Thus every floor correction, every exact radical, and every nonzero
microscopic nearest-square cell \(0<|j_m|\le\sqrt M\) is target-safe.
The survivor in (141.C7) is not proved to be \(O(X^\varepsilon)\).

The failure is now sharply localized.  Exact divisor pairing returns a
complete \(r_2/4\) twist, an owner-sized central band, and an untouched
negative-character far sector.  Moreover the literal incomplete
coefficient has a full additive Fourier resonance:

\[
 \sum_{m\le M}A_\rho(m)e(m/4)
 ={i\pi\over8}M+O_{\rho,c_0}(M^{3/4})
 \qquad(2\le M\le c_0y),
\tag{141.C8}
\]

and hence

\[
 \sum_{m\le M}m^{-3/4}A_\rho(m)e(m/4)
 ={i\pi\over2}M^{1/4}+O_{\rho,c_0}(\log(2M)).
\tag{141.C9}
\]

The round should close under
\(\mathsf{incomplete\_fibre\_dispersion\_no\_go}\), while promoting
(141.C7)--(141.C9) and the exact pairing identity below as narrow proved
facts.  No lower-GAR, M1, M2, endpoint, M9, quarter, or exponent claim
follows.

## 2. Exact hypotheses, cells, and floor-to-cone dictionary

The fixed real function \(V_{\rm low}\) is smooth, compactly supported,
flat at its support boundary, and equal to one near zero.  Choose a
fixed \(C_V\) containing its positive support.  Since

\[
 Z={N\over R^2},\qquad y-1<Z\le y+2,
\tag{141.C10}
\]

the effective range is \(m\le M_*=C_VZ\ll_Vy\).  Empty rows and zero
profile samples contribute zero before a denominator is used.  Bounded
\(X\) is absorbed in the implied constants.

Put

\[
 \delta_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor+1,
 \qquad D_h=y-\delta_h.
\tag{141.C11}
\]

For an odd integer \(r\), least-odd minimality gives the exact
equivalence

\[
 r\ge r_h+2
 \quad\Longleftrightarrow\quad
 r-2\ge {4Nh\over D_h^2}
 \quad\Longleftrightarrow\quad
 (r-2)D_h^2\ge4Nh.
\tag{141.C12}
\]

In particular an exact far pair satisfies \(r>4h\), since
\(N\ge y^2>D_h^2\).  Define the literal correction

\[
 E_N(m)=
 \sum_{\substack{hr=m,\ r\ {\rm odd}\\4h<r\le r_h}}\chi_4(r).
\tag{141.C13}
\]

Then, with every floor retained,

\[
 A_\rho(m)=C(m)-E_N(m).
\tag{141.C14}
\]

There are no nearest-integer ties in (141.C6): an equality
\(\sqrt{Nm}=k+1/2\) would force the even integer \(4Nm\) to equal an
odd square.  Thus the half-open real cell with label \(k\) is exactly

\[
 \mathcal C_k=
 \left[{(k-1/2)^2\over N},{(k+1/2)^2\over N}\right),
 \qquad |\mathcal C_k|={2k\over N}.
\tag{141.C15}
\]

On \(m\le M_*\), one has \(k\ll_VN/R\), and hence
\(|\mathcal C_k|\ll_VR^{-1}<1\) for large \(X\).  Every such phase cell
therefore contains at most one integer \(m\).  Finally,

\[
 e(\sqrt{Nm})
 =e\!\left(-{j_m\over k_m+\sqrt{Nm}}\right),
\tag{141.C16}
\]

so \(0<|j_m|\le\sqrt M\) on \(m\asymp M\) is a genuine phase window
of width \(O(N^{-1/2})\).  The complement in (141.C7) retains every
endpoint and every dyadic scale, including \(M=1\).

## 3. Proof of the target-safe reductions

From \(N=y^2+q\), \(0\le q\le2y\), and
\(\delta_h\le\rho y/\sqrt h+1\),

\[
 {4Nh\over D_h^2}-4h
 =4h{q+2y\delta_h-\delta_h^2\over D_h^2}
 \ll_\rho \sqrt h+{h\over y}+1.
\tag{141.C17}
\]

The least odd integer above a real threshold is less than that
threshold plus two.  On the support, \(r>4h\) and \(hr\ll y\) imply
\(h\ll_V\sqrt y\asymp R\).  Therefore

\[
\begin{aligned}
 \sum_m m^{-3/4}|E_N(m)|
       |V_{\rm low}(R^2m/N)|
 &\ll_{\rho,V}
 \sum_{h\ll_VR}h^{-3/4}
 \sum_{\substack{4h<r\le r_h\\r\ {\rm odd}}}r^{-3/4}\\
 &\ll_{\rho,V}
 \sum_{h\ll_VR}(h^{-3/2}+h^{-1})
 \ll_{\rho,V}\log(2X).
\end{aligned}
\tag{141.C18}
\]

This proves the floor-to-cone replacement uniformly in \(q\), in the
real centre, and in the phase.

For the phase cells, let

\[
 \rho_N(j)=\#\{k\pmod N:k^2\equiv j\pmod N\}.
\tag{141.C19}
\]

For every nonzero integer \(j\), prime-power lifting and the Chinese
remainder theorem give

\[
 \rho_N(j)\le4^{\omega(N)+1}\sqrt{(N,j)}
 \ll_\varepsilon N^\varepsilon |j|^{1/2}.
\tag{141.C20}
\]

Indeed, if \(p^a\Vert N\) and \(v_p(j)=2s<a\), a solution has
\(v_p(k)=s\), and after division there are at most two unit roots for
odd \(p\), at most four for \(p=2\), with \(p^s\) lifts.  An odd
valuation below \(a\) gives no roots.  If \(p^a\mid j\), the zero-root
count is \(p^{\lfloor a/2\rfloor}\).

Throughout the effective range \(k_m<N\) for large \(X\).  For a fixed
\(j\), the map \(m\mapsto k_m\) is injective into the roots in
(141.C19), because \(m=(k_m^2-j)/N\).  Hence

\[
 \#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
 \ll_\varepsilon
 N^\varepsilon\sum_{1\le j\le\sqrt M}j^{1/2}
 \ll_\varepsilon N^\varepsilon M^{3/4}.
\tag{141.C21}
\]

Using \(|A_\rho(m)|\le\tau(m)\ll_\varepsilon X^\varepsilon\), the
weighted contribution of (141.C21) is \(O_\varepsilon(X^\varepsilon)\)
on each block; logarithmically many blocks are absorbed by epsilon
renaming.  If \(j_m=0\), write uniquely \(N=Du^2\) with \(D\)
squarefree.  Then \(Nm\) is a square exactly when \(m=Dt^2\), and

\[
 \sum_{j_m=0}m^{-3/4}|V_{\rm low}A_\rho(m)|
 \ll_\varepsilon
 D^{-3/4}X^\varepsilon\sum_{t\ge1}t^{-3/2}
 \ll_\varepsilon X^\varepsilon.
\tag{141.C22}
\]

Removing (141.C21)--(141.C22) from the exact scalar and then applying
(141.C18) to the surviving terms proves (141.C7).

The congruence ledger is scale-sharp for this elementary argument.  A
window \(0<|j|\le J\) gives at most
\(N^\varepsilon J^{3/2}\) points and weighted cost
\(M^{-3/4}J^{3/2}X^\varepsilon\); it is target-safe at
\(J=\sqrt M\), but it supplies no bound for the wider complement.
Because (141.C15) is a singleton cell, relabeling by \(k\) creates no
intra-cell cancellation there.

## 4. Exact pairing, additive resonance, and source-level barriers

Write \(m=2^\nu n\) uniquely with \(n\) odd.  For \(dr=n\), put

\[
 F_\nu(d,r)=\mathbf1_{\{r\ge r_{2^\nu d}+2\}},
 \qquad
 A_\nu(n)=\sum_{dr=n}\chi_4(r)F_\nu(d,r),
\tag{141.C23}
\]

with an empty row assigned value zero.  Equation (141.C12) implies

\[
 F_\nu(d,r)=1\Longrightarrow r>4\,2^\nu d,
\tag{141.C24}
\]

so \(F_\nu(d,r)F_\nu(r,d)=0\).  Define

\[
 B_\nu(n)=\sum_{dr=n}\chi_4(r)
 \{1-F_\nu(d,r)-F_\nu(r,d)\},
 \qquad
 \sigma_{\chi_4}(n)=\sum_{r\mid n}\chi_4(r).
\tag{141.C25}
\]

After swapping \(d,r\), the second far sector is
\(\chi_4(n)A_\nu(n)\).  Therefore the exact fibre identity is

\[
 \boxed{
 \sigma_{\chi_4}(n)
 =(1+\chi_4(n))A_\nu(n)+B_\nu(n),}
\tag{141.C26}
\]

or equivalently

\[
 \boxed{
 A_\nu(n)={1\over2}\sigma_{\chi_4}(n)
 -{1\over2}B_\nu(n)
 +\mathbf1_{\{\chi_4(n)=-1\}}A_\nu(n).}
\tag{141.C27}
\]

For \(\chi_4(n)=-1\), both \(\sigma_{\chi_4}(n)\) and
\(B_\nu(n)\) vanish by the divisor involution, leaving a tautology.  For
\(\chi_4(n)=1\), pairing introduces

\[
 \sigma_{\chi_4}(n)={r_2(2^\nu n)\over4}
\tag{141.C28}
\]

and the exact central band.  The full radial coefficient, the raw central
incidences, and the raw untouched negative-character far incidences each
retain the top-scale \(R^{1/2+o(1)}\) modulus capacity of the unscaled scalar.
This is a complete-fibre/central self-return, not a target-safe split.
For controls, a supported large \(p\equiv3\pmod4\) has
\(A_0(p)=-1\) while \(\sigma_{\chi_4}(p)=B_0(p)=0\); and the accepted
\(p\equiv1\pmod4\) prime-square fibre has
\(A_0(p^{2a})=a\), \(\sigma_{\chi_4}(p^{2a})=2a+1\), and
\(B_0(p^{2a})=1\).

The cone also exposes a literal bad additive mode.  With

\[
 S_C(M)=\sum_{m\le M}C(m)e(m/4),
\tag{141.C29}
\]

unfolding \(m=hr\) gives

\[
 S_C(M)=
 \sum_{4h^2<M}\ \sum_{\substack{4h<r\le M/h\\r\ {\rm odd}}}
 \chi_4(r)e(hr/4).
\tag{141.C30}
\]

Even \(h\)-rows are \(O(1)\), because \(e(hr/4)\) is constant on odd
\(r\) while \(\chi_4(r)\) alternates.  For odd \(h,r\),

\[
 e(hr/4)=i\chi_4(h)\chi_4(r),
\tag{141.C31}
\]

so every summand on an odd row equals \(i\chi_4(h)\).  If
\(H\asymp\sqrt M\), the row contains \(M/(2h)-2h+O(1)\) admissible odd
integers.  Since

\[
 \sum_{\substack{h\le H\\h\ {\rm odd}}}{\chi_4(h)\over h}
 ={\pi\over4}+O(H^{-1}),
 \qquad
 \sum_{\substack{h\le H\\h\ {\rm odd}}}\chi_4(h)h=O(H),
\tag{141.C32}
\]

one obtains

\[
 S_C(M)={i\pi\over8}M+O(M^{1/2}).
\tag{141.C33}
\]

For \(M\le c_0y\), the unweighted number of correction pairs in
(141.C13) is \(O_{\rho,c_0}(M^{3/4})\), by summing
\(O(1+\sqrt h+h/y)\) over \(h\ll\sqrt M\).  Equations
(141.C14) and (141.C33) prove (141.C8), and Abel summation proves
(141.C9).  For some fixed \(M_0=M_0(\rho,c_0)\), summation by parts against the
bounded partial sums of \(e(m/4)\) also yields

\[
 \sum_{m<M}|A_\rho(m+1)-A_\rho(m)|\gg_{\rho,c_0}M
 \qquad(M_0\le M\le c_0y).
\tag{141.C34}
\]

Thus neither uniform additive cancellation nor low coefficient
variation is available.  This is an obstruction, not a lower bound for
(141.C7): nonlinear residual phases from distinct cells can still
rotate and cancel the quarter-frequency direction.

There is nevertheless an exact analytic representation.  On
\(h\asymp H\), smoothing \(\mathbf1_{r>4h}\) across relative ratio
width \(H^{-1/2}\) changes \(O(\sqrt H)\) values of \(r\) per height
and costs \(O(1)\) in the weighted scalar.  After dyadic localization
in \(h,r\), write \(u=hr\), \(v=r/(4h)\), and absorb all smooth radial,
ratio, and dyadic factors into \(\Psi(u,v)\).  Double Mellin inversion
is exact on an initial absolute-convergence contour and has arithmetic
factor

\[
 4^{-t}\zeta(s+t)L(s-t,\chi_4),
\tag{141.C35}
\]

after \(t\mapsto-t\).  The sharp Perron step itself would require
height \(T\gg H\), since the nearest odd ratio has
\(|\log(r/(4h))|\asymp h^{-1}\); only the proved smoothing licenses
rapid ratio-Mellin decay at \(|\Im t|\lesssim H^{1/2}X^\varepsilon\).

The audited primary-source routes do not close the target.  At the
balanced block \(H\asymp K\asymp R\), Robert--Sargos gives
\(R^{1/2+\varepsilon}\) only after the target-safe ratio smoothing
separates the two long coefficient slots; inserting the exact joint mask
directly in its arbitrary joint slot gives only
\(R^{3/4+\varepsilon}\).  The genuine Sargos--Wu Theorem 9 admits the
square-root monomial with separated coefficients but gives only
\(R^{2/5+\varepsilon}\) after the same smoothing.  The adjacent
general-domain lemma permits a joint staircase domain but excludes this
rank-one phase through \(\alpha+\beta-1=0\).  The valid
Tao--Trudgian--Yang exponent pair
\((89/1282,997/1282)\) gives

\[
 R^{2\kappa+\lambda-1/2+\varepsilon}
 =R^{267/641+\varepsilon};
\tag{141.C36}
\]

and the corresponding complete radial cosine combination in Popov plus
Li--Yang returns only

\[
 R^{4\theta_*-1+\varepsilon}
 =R^{(50\sqrt{1717}-297)/6881+\varepsilon}.
\tag{141.C37}
\]

before the outer \(N^{1/4}\asymp R\) is restored.  This comparison does
not bound an individual complex exponential branch merely from the real
circle discrepancy; it is already insufficient even in the radial
combination to which the cited formula applies.

Banerjee--Khurana has the complete coefficient and a strict
\(0<\Re\nu<1/2\) hypothesis; Kaczorowski--Perelli treats a fixed twist
parameter and diagnoses the complete represented centre as spectral;
the available subconvex and moment inputs control absolute or quadratic
Mellin functionals, not the required centre-dependent signed linear
functional.  Even an ideal shifted mean square followed by Mellin
Plancherel and Cauchy--Schwarz gives \(R^{1+\varepsilon}\), so a new
oscillatory correlation theorem, not a stronger pointwise bound alone,
would be required.

## 5. First doubtful or unproved step

The first open estimate is precisely

\[
 \boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.}
\tag{141.C38}
\]

A sufficient dyadic form, after the actual floor correction is restored
or removed by (141.C18), is

\[
 \sup_{M\le U\le2M}
 \left|\sum_{\substack{M\le m<U\\|k_m^2-Nm|>\sqrt M}}
 A_\rho(m)e(\sqrt{Nm})\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{141.C39}
\]

Neither (141.C20), (141.C26), (141.C34), nor an audited source theorem
implies (141.C39).  The nearest-square cells are singletons; the
quadratic-congruence count exhausts its target-safe power at
\(|j|=\sqrt M\); divisor pairing is blind on \(\chi_4(n)=-1\) and
self-returns otherwise; the coefficient has a linear quarter-frequency
partial sum and linear total variation; and the valid rowwise exponent
pair remains polynomially above target.

The canonical transform also remains invertible.  For

\[
 \Phi_z(m)=\sqrt{Nm}-{mz\over4},
\tag{141.C40}
\]

the critical point and value are

\[
 m_z={4N\over z^2},\qquad \Phi_z(m_z)={N\over z}.
\tag{141.C41}
\]

Resolving the divisor incidence before applying this transform returns
the reciprocal family; a second stationary transform returns the
square-root phase.  Completing the fibre returns (141.C27)--(141.C28).
No noninvertible signed gain has been proved.

## 6. Required controls, dependencies, and outcomes

The exact mask, least-odd threshold, every floor, parity, empty row,
profile support, \(q=0\), \(q=2y\), and real-centre uniformity are
retained in (141.C1)--(141.C18).  The dyadic partition includes the
smallest block and the literal terminal support.  The nearest-square
endpoint convention, tie exclusion, physical cell width, singleton
multiplicity, congruence multiplicity, exact radical channel, and full
weighted ledger are explicit in (141.C15)--(141.C22).

The complete-fibre comparison retains the \(2\)-adic valuation,
character direction, exact swapped mask, central band, negative
character sector, prime control, and prime-square control in
(141.C23)--(141.C28).  The quarter-frequency main term is proved for
the exact coefficient in (141.C29)--(141.C34), rather than inferred
from a generic heuristic.  Its role is limited to falsifying uniform
additive cancellation and low variation.  It is not promoted to a
fixed-centre lower bound.

The repaired source audit retains theorem coefficient classes,
smoothing, lengths, fixed-centre uniformity, absolute-value placement,
strict hypotheses, and the complete \(R\)-power ledger in
(141.C35)--(141.C37): Robert--Sargos gives \(R^{1/2}\) only in the
smoothed separated specialization and \(R^{3/4}\) for the direct joint
mask; Sargos--Wu gives \(R^{2/5}\) in its separated theorem while its
general-domain companion excludes rank one.  Sharp Perron truncation, a
nondegenerate rank-two theorem, rowwise exponent pairs as closure,
coefficient completion, fixed-parameter standard twists, pointwise
subconvexity by absolute inversion, and moment estimates by Cauchy are
all quantitatively or structurally insufficient.  No desired circle
estimate, centre average, positive energy, numerical experiment, or
arbitrary-array surrogate is used.  The allocation is 100 percent
analytical/source verification.

Exact evidence consists of the three Round-141 primary reports, the
Round-140 accepted candidate/adjudication/synthesis, the Round-137
hard-TOP synthesis, the active proof graph and campaign, and the
primary-source links and theorem cards recorded in the Round-141 source
audit.  The floor-to-cone lemma was independently derived by the blind
and source lanes; the phase-cell lemma and exact pairing were derived by
the discovery lane; the additive resonance was derived under
statement-only isolation.

The new facts change only the unsquared grouped far scalar.  They do
not prove the complete lower-radial signed estimate, lower GAR, either
direct blockwise M1 parent, M9-M1, any M2 parent, M9-M2, endpoint
uniformity, M9, the conditional bridge, or the quarter theorem.  The
strongest internally proved exponent remains \(1/3\).  The separately
audited external exponent remains

\[
 \theta_*={3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots.
\tag{141.C42}
\]

## 7. Recommended state effect

After independent post-unmask verification, create one proved reduction
recording (141.C7): the exact far scalar is target-equivalent to the
floor-free cone scalar with exact and microscopic nearest-square cells
removed, while the nonresonant complement remains open.

Create one proved obstruction recording (141.C15),
(141.C20)--(141.C21), (141.C26)--(141.C28),
(141.C33)--(141.C35), and (141.C36)--(141.C41): nearest-square cells
are singleton; the elementary congruence method closes only the
microscopic window; divisor pairing self-returns or is blind; the exact
coefficient has a full quarter-frequency resonance and linear
variation; the exact Mellin factorization requires an oscillatory
shifted-\(L\) correlation absent from the audited literature; and the
canonical transform self-returns.

Update the Round-140 smoothed far-alias reduction and the global lower
signed owner with (141.C7), leaving (141.C38) as their next action.
Update the Round-140 rank-one/product-fibre obstruction with the exact
pairing, quarter-mode, source, and phase-cell barriers.  Reject every
claim that discards the wider nonresonant complement, the central band,
or the negative-character sector, or that treats a capacity control as
a signed lower bound.

Make no change to M9-M1, M9-M2, endpoint uniformity, M9, the
conditional bridge, the Gauss-circle target, the internally proved
exponent \(1/3\), or the separately audited Li--Yang exponent.

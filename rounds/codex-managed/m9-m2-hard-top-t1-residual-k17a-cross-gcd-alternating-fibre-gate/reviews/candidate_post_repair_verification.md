# Round 176 candidate post-repair verification

## Verdict

**GREEN.** The repaired candidate resolves every mandatory mathematical
and owner-scope issue identified in
candidate_mathematical_scope_review.md.  No further repair is required
before promoting the candidate at its stated subordinate scope.

The verification is GREEN only for the exact two-orientation reduction,
the fibre-stable original-gcd identity, the Fourier-anchor identities, the
fixed-proportion strict cross-gcd sector, and the explicitly limited
positive-recombination no-go.  Formula (176.C29) remains an unproved
sufficient theorem.  The full K17a target and every parent remain open.

## Repaired exact aggregate and orientation checks

Equations (176.C4a) and (176.C10a)--(176.C10e) now give a complete
multiplicity-one identity.

For the plus orientation,

\[
 N_t^+=\kappa u(\kappa v+2w_t),\qquad
 N_t^++2\kappa n=\kappa v(\kappa u+2s_t),
\]

so the lower divisor is \(\kappa u\) and the upper divisor is
\(\kappa u+2s_t\).  Equation (176.C10b) therefore has the correct ordered
coefficient product

\[
 \lambda_{N_t^++2\kappa n}(\kappa u+2s_t)
 \overline{\lambda_{N_t^+}(\kappa u)}.
\]

For the minus orientation,

\[
 N_t^-=\kappa v(\kappa u+2s_t),\qquad
 N_t^-+2\kappa n=\kappa u(\kappa v+2w_t),
\]

so (176.C10d) correctly places divisor \(\kappa u+2s_t\) at the lower
endpoint and divisor \(\kappa u\) at the upper endpoint.  Both amplitudes
contain exactly

\[
 \left(1-\frac{2\kappa n}{R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}
 \mathbf1_{s_t\ge1,w_t\ge1}.
\]

Thus the Fejer factor, exact nonpolylogarithmic complement, original
low-gcd cutoff, and displacement positivity are explicit.  Zero extension
is used only for the remaining literal endpoint conditions; it is no
longer asked to enforce the orientation.  Equation (176.C10e) includes
both disjoint orientations and retains exactly one real part outside the
complete incidence sum.  The definitions of
\(\Lambda^\pm,\Psi^\pm\), and the allowed \(t\)-set used later in
(176.C29) are now unambiguous.

The convention for \(u=1\) is harmless.  For \(u>1\),
\(s_0=[\bar vn]_u\) and \(s_0=[-\bar vn]_u\) give the plus and minus
anchors respectively; all solutions are
\((s,w)=(s_0,w_0)+t(u,v)\).  The explicit inequalities
\(s_t,w_t\ge1\) select precisely the claimed opposing orientation, and
the two endpoint products both advance by \(2\kappa uv\).

## Gcd, parity, and Fourier checks

The original-gcd identity remains exact.  On a nonzero plus atom,
squarefreeness of \((\kappa u+2s)\kappa v\) gives
\((\kappa,s)=1\), whence

\[
 (d,d')=(\kappa u,\kappa u+2s)
 =(\kappa u,s)=(u,s)=(u,n).
\]

The lower squarefree product gives the identical result in the minus
orientation.  Thus (176.C11) is correct with the
orientation-dependent \(\kappa_*\), and the original cutoff is
fibre-stable rather than a source of variation.

The added two-adic paragraph is correct.  In the even-even squarefree
branch \(v=2v_1\) with \(v_1\) odd.  Both products are \(2\bmod4\), so
\(4\mid r=2\kappa n\) and \(n\) is even.  Either primitive equation then
forces \(w\) even.  The increment \(w\mapsto w+v\) preserves this parity,
whereas \(s\mapsto s+u\) flips parity because \(u\) is odd.  After the
factor two is separated, all squarefree Möbius progressions have odd
modulus and preserve \((-1)^t\).  The odd branch is \(v\) odd.  Hence
both original parity branches and the exact half-frequency are retained.

Equations (176.C12)--(176.C13) remain correct.  The new primitive-modulus
identity (176.C13a) is also exact.  If
\(g=(u,n)\), \(u=gu_0\), \(n=gn_0\), then reduction of
\(\bar v\) modulo \(u_0\) is still the inverse of \(v\), and

\[
 [\pm\bar v n]_u
 =g[\pm\bar v n_0]_{u_0}.
\]

Because \(g\) is odd,
\((-1)^{g[\pm\bar v n_0]_{u_0}}=(-1)^{[\pm\bar v n_0]_{u_0}}\), proving
(176.C13a).
With \(c_m(k)=\widehat E_m(k)/m\), unnormalized Parseval gives
\(\sum_k|c_m(k)|^2=1\), while the near-half coefficient gives
\(\|c_m\|_\infty\asymp1\).  These additions neither lose a power nor
claim cancellation.

The coordinate reconciliation (176.C20)--(176.C21) remains correct:

\[
 g=(u,n),\quad a=\frac{\kappa u}{g},\quad
 k=\frac{s}{g},\quad m_0=\kappa v,\quad
 K=\frac{\kappa n}{g},\quad (a,m_0)=\kappa.
\]

It gives translation step \(2\kappa uv\).  The blind primitive step is
\(u/g\), which is odd, so its character law is the same half-frequency.

## Strict-sector count

The repaired hyperbola count is valid and slightly more robust than the
earlier box count.  Put \(Y=L/\kappa\).  The inward cross product
\(\kappa^2uv\) is smaller than either supported endpoint product, so
\(uv\ll Y^2\), while \(r=2\kappa n<R_0\) gives \(n\ll Y\).  A row with
common product increment \(2\kappa uv\) has at most

\[
 O\!\left(1+\frac{L^2}{\kappa uv}\right)
\]

sites in a product shell of length \(O(L^2)\).  Therefore

\[
\begin{aligned}
 C_\kappa
 &\ll X^\varepsilon
 \sum_{uv\ll Y^2}\sum_{n\ll Y}
 \left(1+\frac{L^2}{\kappa uv}\right)\\
 &\ll X^\varepsilon
 \left(Y^3\log(2Y)+
       \frac{L^2Y}{\kappa}\log^2(2Y)\right)
 \ll \frac{L^3}{\kappa^2}X^\varepsilon .
\end{aligned}
\]

The first term is \(O(L^3\kappa^{-3}\log L)\), and the second is
\(O(L^3\kappa^{-2}\log^2L)\); the logarithms are legitimately absorbed
by choosing the auxiliary exponent below the final one.  Consequently

\[
 \sum_{\kappa\ge K}C_\kappa
 \ll \frac{L^3}{K}X^\varepsilon.
\]

At \(K=\delta L\), fixed \(0<\delta<1/2\), this proves (176.C14).
Both orientations add only a constant, and every literal restriction
deletes atoms.  If \(\delta\) varies, the displayed \(\delta^{-1}\) cost
is correctly retained.  In fact the sector is exactly empty for
\(\delta\ge1/2\), since the integer inequality \(r<R_0=\lceil L\rceil\)
implies \(r<L\); the candidate's weaker “eventually empty” wording is
harmless and does not affect the stated theorem.

## Phase and route-capacity checks

The phase definition is now correct:

\[
 x(t)=N_0+2\kappa uv\,t,\qquad
 \Phi(t)=J(\sqrt{x(t)+2\kappa n}-\sqrt{x(t)})+\frac t2.
\]

On a fixed-relative full fibre \(T\asymp\kappa\), and direct
differentiation gives

\[
 \Phi''(t)\asymp\frac{2Jn}{\kappa L},\qquad
 |\Phi'''(t)|\asymp\frac{2Jn}{\kappa^2L},\qquad
 F\asymp\frac{2Jn\kappa}{L}.
\]

The derivative image has length \(2Jn/L\).  Absolute stationary-mode
recombination therefore has size
\(\sqrt F+T/\sqrt F\), which is not power-smaller than \(T\); taking
the minimum with the trivial row bound returns no power saving.  The raw
tail and hypothetical constant-row tail are respectively

\[
 \frac{L^3}{K}\quad\text{and}\quad\frac{L^3}{K^2}.
\]

At \(K=L^{1/2}\), these are \(L^{5/2}\) and \(L^2\), exactly as stated.

The added two-variable transform calculation correctly supplies the proof
previously missing from the candidate.  On a fixed-relative cell,
\(\Theta_{ss}\asymp-J/L\), \(\Theta_{ww}\asymp J/L\), so
\(|\det\operatorname{Hess}\Theta|\asymp J^2/L^2\).  The primitive vector
\((v,-u)\) extends to an integral unimodular basis.  The
\((n,t)\)-rectangle has area
\((L/\kappa)\kappa=O(L)\), hence the gradient image has area
\(O(J^2/L)\).  One stationary coefficient has scale \(L/J\), so
positive dual recombination has \(O(J)\) capacity.  The better physical
certificate is \(O(L)\) per \((\kappa,u,v)\), and

\[
 \sum_{\kappa\ll L}(L/\kappa)^2L\ll L^3.
\]

The candidate explicitly limits this statement to smooth fixed-relative
cells and termwise positive dual summation.  It does not claim to have
executed Poisson on the discontinuous literal symbol, and it leaves signed
dual and inter-orientation cancellation open.  The no-go is therefore
properly scoped and is not a physical lower bound.

The constant-anchor family, arbitrary-support masks, dechirped arrays,
and raw capacities remain explicitly quarantined.  The candidate neither
asserts literal density for those controls nor turns transform capacity
into physical mass.

## Sufficient open estimate and owner scope

Formula (176.C29) now refers to the fully defined
\(\Lambda^\pm\) and \(\Psi^\pm\), sums over every integer \(t\), and
keeps the nonpolylogarithmic range, low-gcd condition, displacement
positivity, squarefree rows, selector, Fejer weight, endpoints, hard
values, and zero extension inside the amplitude.

If (176.C29) held for every \(k\bmod u\), Fourier inversion would cost

\[
 \frac1u\sum_{k\bmod u}|\widehat E_u(k)|
 \ll\log(2u).
\]

There are \(O((L/\kappa)^2)\) actual anchor pairs, and the proposed local
bound is \(O(\kappa X^\varepsilon)\).  Hence

\[
 \sum_{\kappa\ll L}(L/\kappa)^2\kappa
 \ll L^2\log L.
\]

The Fourier logarithm and this harmonic logarithm are absorbed after
auxiliary-\(\varepsilon\) renaming.  Thus (176.C29) genuinely implies the
full nonpolylogarithmic K17a estimate.  No accepted theorem proves it, and
the candidate correctly identifies selector-aware signed joint
inverse-residue cancellation as the first open step.

The terminal no-go rejects only fibrewise automatic alternation, Abel
without selector control, and rowwise or joint transforms whose dual
modes are recombined positively.  It does not reject a signed joint
inverse-residue theorem, cancellation between orientations, or another
literal coefficient-sensitive method.

## Controls, dependencies, and recommended state effect

All required controls are GREEN:

- exact literal residual coefficient and one outer real part;
- exact nonpolylogarithmic complement;
- both opposing orientations and displacement positivity;
- multiplicity one;
- cross gcd versus the original fibre-stable gcd;
- odd and even-even two-adic branches;
- half-frequency character law;
- odd squarefree Möbius progressions;
- selected and no-pair rows without invented regularity;
- short cross-gcd fibres;
- canonical-anchor DFT and its large alias;
- rowwise phase aliases and positive dual-mode restoration;
- full two-variable positive-transform restoration at its stated scope;
- endpoints, hard values, and zero extension;
- constant-anchor, arbitrary-support, and dechirped controls quarantined
  from physical lower mass;
- the complete \(L^3\)-to-\(L^2\) ledger; and
- residual-only downstream scope.

This verification used the repaired conductor candidate, the earlier
candidate mathematical-scope review, and all three Round-176 reports
authorized by the brief.  It used no external theorem or numerical
experiment and edited no candidate, report, graph, kernel, synthesis,
control, or shared-state artifact.

**Recommended state effect:** promote the repaired candidate exactly at
its stated subordinate scope: the two-orientation parametrization,
(176.C11), (176.C12)--(176.C13a), (176.C14), and the route-scoped
positive-recombination no-go.  Retain (176.C29), the complete K17a target,
the residual scalar, every hard-TOP parent, BAL, UNBAL, M9--M2,
M9--M1/GAR, endpoint uniformity, M9, both bridges, the quarter theorem,
and every exponent as open.

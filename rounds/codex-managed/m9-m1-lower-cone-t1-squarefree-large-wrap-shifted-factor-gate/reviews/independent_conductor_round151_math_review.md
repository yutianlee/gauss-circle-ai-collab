# Round 151 independent conductor mathematics review

- Campaign: m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate
- Round: 151
- Reviewed candidate: candidates/conductor_round151_character_ranges_and_bprocess_boundary.md
- Role: independent terminal mathematics reviewer
- Starting graph SHA-256: 521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f
- Allocation: 100% analytic, algebraic, and source-hypothesis checking; 0% numerical
- Terminal verdict: **GREEN**
- First mathematically failed line: **none**

## 1. Result

The conductor candidate's substantive proof kernel is correct.  Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
\]

The following conclusions survive an independent derivation.

1. For every nonzero centered wrap, removing the full two-adic part of
   the wrap transfers the mod-four character exactly to the two odd
   shifted differences.  The inverse map has precisely the stated
   positive-divisor fibre \(h\mid g\); it is a bijection only after all
   support, gcd, centeredness, collar, profile, and packet tests are
   reapplied.
2. The wraps with \(\nu _2(|k|)\geq J_*\), where
   \(2^{J_*}\asymp N/R^2\), occupy
   \(O(1+R^2/Q)\) wrap classes.  The accepted Round-150 fixed-wrap
   theorem therefore gives their complete absolute weighted
   contribution as \(O_\varepsilon(R^2D X^\varepsilon)\).
3. The accepted Round-148 factorization and transition-width ledger do
   imply uniform sampled bounded variation of the actual retained
   profile at every \(M\).  This is a theorem for the actual finite
   product profile after its owned hard collars, not for an arbitrary
   smooth or bounded weight.
4. Mobius inversion, the two odd residue classes modulo four, and Abel
   summation place both audited exponent pairs lawfully.  Bourgain's
   global pair gives

   \[
    |G_U(d)|\ll_\varepsilon
    E^{13/84}Q^{55/84}X^\varepsilon
   \]

   and the full-row corridor

   \[
    \boxed{M^{29}\gg R^{52}D^{84}}.
   \]

   The Tao--Trudgian--Yang pair gives

   \[
    |G_{U,\leq L_0}(d)|\ll_\varepsilon
    E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon
   \]

   and the low-row corridor

   \[
    \boxed{M^{819}\gg
      R^{1424}D^{1816}L_0^{534}}.
   \]

5. The \(D=L=1\) reciprocal transform has the stated square-root phase,
   character, leading amplitude, and constant.  The actual compact
   smooth profile has a boundary-complete transform with target-sized
   error.  A second stationary transform returns the phase and
   principal symbol, but no claim is made that every lower symbol and
   endpoint term composes identically.  The elementary capacity remains

   \[
    \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon,
   \]

   so a bare iteration gives no intermediate-scale gain.

The row/collar distinction is correct.  For \(D>1\), the exponent-pair
bounds own a recombined full row or low subrow, not an arbitrarily
isolated collar subset.  For \(D=1\), every centered nonexact pair is a
collar pair; there the full-row Bourgain bound, after subtracting the
already owned exact and fixed-wrap pieces, owns the complete large-wrap
collar in its stated range.  The TTY result owns only the low-low
component unless its named high-row square and cross term are separately
controlled.

## 2. Exact statement and hypotheses

All \(L,q,h,r\) are positive odd integers, \(q_i=hr_i\), and
\((r_1,r_2)=1\).  The retained saddle support is

\[
 q\asymp LQ,\qquad (L,q)=1,\qquad L\ll E.
\]

The hard product-prefix collars of width \(O(\sqrt M)\) and, when
present, the cone collar of width \(O(\sqrt D)\) retain their accepted
primal owners.  A prefix shorter than its radial collar is wholly in that
owner.  On the remaining lattice points the Round-148 amplitude is
compact smooth and is the exact retained amplitude.

For the literal two-row coefficient, write \(d=\eta m\), where
\(\eta\in\{1,2\}\) and \(m\) is odd squarefree, and write
\(L_i=t_i s_i^2\), where \(t_i,s_i\) are odd squarefree and
\((t_i,s_i)=1\).  The candidate now explicitly retains
\(a_i\mid t_i\), \(c_i=t_i/a_i\), \(u_i\geq1\), and odd squarefree
\(v_i\) with \((v_i,c_i s_i)=1\).  With

\[
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname {rad}(c_1c_2s_1s_2v_1v_2),
\]

the row mask is exactly

\[
 {\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m}.
\]

Thus (151.C12) is the literal large-wrap part of the accepted energy
expansion.  The candidate also now states explicitly that the displayed
\(B\)-product in (151.C27) is shorthand for the exact expansion
(151.C10), not an additional multiplier.

For each pair put

\[
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq hr_1r_2/2,
\]

with the unique centered integer \(k\).  The isolated residual has
\(k\notin\mathcal K_0\) and
\(0<|\rho|\leq hr_1r_2/D\), where
\(|\mathcal K_0|\ll1+R^2/Q\).

The one-dimensional claims use exactly the accepted compressed row

\[
 G_U(d)=\sum_L\frac{\chi_4(L)B_{d,U}(L)}L
 \sum_{\substack{q\asymp LQ\ {\rm odd}\\(L,q)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q)
\]

and the accepted prefix-uniform norm

\[
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.
\]

No regularity of \(B_{d,U}(L)\) in \(L\), no arbitrary denominator
coefficient, and no cancellation between different \(d\)-rows is
assumed.

## 3. Proof and derivation

### 3.1 Residual identity, positivity, and parity

For \(k\ne0\), set \(j=\nu _2(|k|)\), write
\(k=2^j\kappa\) with \(\kappa\) signed odd, and define

\[
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\]

Direct multiplication gives

\[
 AB=N^2L_1L_2+kh\rho.
\]

The stronger one-factor identities are

\[
 r_2A=NL_2r_1+\rho,\qquad
 r_1B=NL_1r_2-\rho.
\]

On the collar,

\[
 \frac{|\rho|}{NL_2r_1}
 \leq\frac{q_2}{DNL_2}
 \ll\frac{Q}{DN}\ll R^{-2},
\]

and symmetrically for \(B\).  Hence both shifted factors are positive
for large \(X\), with no exception when a denominator divides \(N\).

Now

\[
 x=\frac{NL_1-A}{2^j}=\kappa hr_1,\qquad
 y=\frac{B-NL_2}{2^j}=\kappa hr_2.
\]

Both are odd, nonzero, and have the same sign.  Since
\(xy=\kappa^2h^2r_1r_2\), complete multiplicativity gives

\[
 \chi_4(L_1L_2xy)=\chi_4(L_1L_2r_1r_2).
\]

This proof uses neither the sign of \(k\) nor the parity of \(N\).

Let \(n=\nu _2(N)\).  Comparing the unequal valuations in
\(NL_i\) and \(2^j\kappa hr_i\) yields

\[
 (\nu_2(A),\nu_2(B))=
 \begin{cases}
 (j,j),&j<n,\\
 (n,n),&j>n,\\
 (\geq n+1,\geq n+1),&j=n.
 \end{cases}
\]

Since \(\delta\) is even and \(hr_1r_2\) is odd, \(\rho\) is odd
exactly when \(j=0\).  If \(t=\nu _2(\delta)\), with the now explicit
convention \(\nu _2(0)=+\infty\), unequal valuations give

\[
 \nu _2(\rho)=\min(j,n+t)\quad(j\ne n+t),
\]

and equality gives valuation at least \(j+1\).  This exhausts all
parity classes without applying \(\chi_4\) to \(A\) or \(B\).

### 3.2 Inverse divisor fibre

Conversely, impose

\[
 2^j\Vert NL_1-A,\qquad
 2^j\Vert B-NL_2,\qquad xy>0,
\]

and let

\[
 g=(|x|,|y|),\qquad \epsilon=\operatorname {sgn}x,\qquad
 r_1=|x|/g,\quad r_2=|y|/g.
\]

Then the \(r_i\) are positive odd and coprime.  The quantities

\[
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-\epsilon2^jg r_1r_2
\]

are fixed by \((A,B,j,L_1,L_2)\).  Every original preimage has

\[
 h\mid g,\qquad
 k=\epsilon2^j g/h,\qquad
 kh=\epsilon2^jg,\qquad q_i=hr_i.
\]

Conversely, every positive divisor \(h\mid g\) which passes

\[
 q_i\asymp L_iQ,\quad (L_i,q_i)=1,\quad
 |\rho|\leq hr_1r_2/2,\quad
 0<|\rho|\leq hr_1r_2/D,\quad k\notin\mathcal K_0,
\]

and both literal profile supports gives one original tuple.  Since
\((r_1,r_2)=1\), it automatically has \((q_1,q_2)=h\).  The fibre
size is at most \(\tau(g)\ll_\varepsilon X^\varepsilon\), but the
fibre cannot be discarded: \(q_i\), \(k\), both profile samples, and
the phase denominator vary with \(h\).  This proves the bijection and
also confirms that it supplies no cancellation by itself.

### 3.3 High-two-adic count

The support gives

\[
 |\delta|\ll L_1L_2Q/h,\qquad
 hr_1r_2\asymp L_1L_2Q^2/h.
\]

Centering therefore implies \(|k|\ll N/Q\).  Choose a power of two
with \(2^{J_*}\asymp N/R^2\).  The number of nonzero signed multiples
of \(2^{J_*}\) in this range is

\[
 O\!\left(1+\frac{N}{Q2^{J_*}}\right)
 =O(1+R^2/Q).
\]

The condition \(\nu_2(|k|)\geq J_*\) is a subset of those multiples.
Round 150 costs \(DQX^\varepsilon\) for each arbitrary fixed wrap
after all rows, \(L_i\), gcds, and coefficient weights are summed.
Hence this entire family costs

\[
 DQ(1+R^2/Q)X^\varepsilon
 \ll R^2D X^\varepsilon,
\]

because \(Q\ll R^2\).  The exact complement is \(j<J_*\).

### 3.4 All-scale variation of the actual profile

Write \(q=LQy\).  The physical sample is exactly

\[
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\]

The supported \(y\)-set is fixed and separated from zero.  In the
actual Round-148 factorization, the dyadic, lower-radial, and other
bulk factors have bounded supremum and \(O(1)\) first derivative in
\(y\).  A retained long radial or prefix transition has derivative
\(O(M^{1/2})\) on total normalized width \(O(M^{-1/2})\).  A cone
transition, present only when \(M\asymp D^2\), has derivative
\(O(D^{1/2})\) on width \(O(D^{-1/2})\).  Each transition therefore
contributes \(O(1)\) to variation.

There are only finitely many factors and components in one inherited
box.  For bounded factors, product variation is bounded by the sum of
each factor's variation times the suprema of all the other factors.
Thus the product has \(O_\varepsilon(X^\varepsilon)\) total
variation.  The actual retained amplitude is compact smooth after the
hard collars are peeled, so its zero extension has no uncontrolled
lattice jumps; even a half-open bookkeeping decomposition adds only
finitely many bounded one-sided jumps.

The floor-valued nonempty-progression indicator in \(B_{d,U}(L)\) is
constant in \(q\), and a collar-short prefix remains with its prior
owner.  Sampling on any increasing progression cannot increase
variation.  Therefore

\[
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_q\mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon
\]

uniformly at every allowed scale.  This closes the project-side seam
that the source report correctly left conditional.

### 3.5 Coprimality, residue classes, and exponent-pair normalization

For fixed \(d,L\), resolve coprimality before estimating:

\[
 {\bf1}_{(L,q)=1}=\sum_{c\mid(L,q)}\mu(c).
\]

Since \(c\mid L\) is odd, write \(q=cm\), use
\(\chi_4(cm)=\chi_4(c)\chi_4(m)\), split
\(m\equiv1,3\pmod4\), and put \(m=4n+a\).  On each proper support
interval,

\[
 H_c\asymp LQ/c,\qquad
 f_c(n)=\frac{NdL}{c(4n+a)},\qquad
 \mathcal T_c\asymp Nd/Q,
\]

and

\[
 \mathcal T_c/H_c\asymp cE/L.
\]

The suppressed factors \(4\) and \(d/D\) stay between fixed positive
constants.  The shifted reciprocal has the required uniform derivative
class because \(H_c\geq Q\gg R\), so the residue shift is
\(O(H_c^{-1})\).  On \(\mathcal T_c\geq H_c\), either verified
exponent pair \((\kappa,\lambda)\) gives

\[
 \sup_I\left|\sum_{n\in I}e(f_c(n))\right|
 \ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda
 c^{\kappa-\lambda}X^\varepsilon.
\]

The finite support gives \(L\leq C E\) for a fixed \(C\).  Thus, at
the only edge where \(\mathcal T_c<H_c\), their ratio is still bounded
below by a fixed positive constant.  There
\(|f_c''|\asymp H_c^{-1}\), and the second-derivative estimate is
\(O(H_c^{1/2})\).  Since both pairs have \(\lambda>1/2\), this is no
larger than the same exponent-pair-shaped majorant.  No source theorem
is invoked outside its \(\mathcal T\geq H\) convention.

Abel summation is legal by Section 3.4, and
\(\sum_{c\mid L}c^{\kappa-\lambda}\leq\tau(L)\) because
\(\lambda>\kappa\).  Hence

\[
 |S_{d,L}|\ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda X^\varepsilon.
\]

Bourgain's Theorem 6 is a global exponent-pair statement for this
standard derivative class.  The narrower
\(\mathcal T^{17/42}\ll H\ll\mathcal T^{1/2}\) window belongs to the
direct Theorem-4 argument, not to the final exponent-pair interface.
Section 5 supplies both the \(B\)-process extension and the
proper-subinterval device.  The corrected source card now records the
right scope.

### 3.6 Power algebra

For Bourgain,

\[
 (\kappa,\lambda)=(13/84,55/84),\qquad
 \lambda-\kappa=1/2.
\]

The half-weight norm therefore gives

\[
 |G_U(d)|\ll_\varepsilon E^{13/84}Q^{55/84}X^\varepsilon.
\]

After squaring and summing \(O(D)\) rows, the ratio to \(R^2D\) is

\[
 \frac{E^{13/42}Q^{55/42}}{R^2}
 =\left(\frac{D^{84}R^{52}}{M^{29}}\right)^{1/84}.
\]

This proves (151.C3).  At \(M\asymp R^2\), it is exactly
\(D\ll R^{1/14}\).

For Tao--Trudgian--Yang,

\[
 (\kappa,\lambda)=
 (89/1282,997/1282),\qquad
 \lambda-\kappa-1/2=267/1282.
\]

Restricting \(L\leq L_0\) and using the same half-weight norm gives the
candidate's row bound.  Its squared ratio to the per-row target is

\[
 \frac{E^{178/1282}Q^{1994/1282}L_0^{534/1282}}{R^2}
 =\left(
 \frac{R^{1424}D^{1816}L_0^{534}}{M^{819}}
 \right)^{1/1282}.
\]

Thus every exponent in (151.C4)--(151.C6) is correct.  In particular,
\(D=L_0=1\) starts at \(M\gg R^{1424/819}\), and at
\(M\asymp R^2\) the condition is
\(D^{1816}L_0^{534}\ll R^{214}\).

### 3.7 Reciprocal transform and scope

For \(D=d=L=1\), the literal row component is
\(\widetilde S_U=B_{1,U}(1)S_U\), where the candidate now explicitly
writes

\[
 S_U=\sum_{q>0}\chi_4(q)
 \mathscr A_{1,M,U}(1,4N/q^2)e(N/q)
\]

and extends the compact positive-support weight by zero before Poisson
summation.  The identity

\[
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\]

is exact on all integers.  At Poisson frequency \(n\), the branch
\(N/x+\sigma x/4-nx\) has a saddle precisely when
\(\ell=\sigma-4n>0\).  Its data are

\[
 x=2\sqrt{N/\ell},\qquad
 F(x)=\sqrt{N\ell},\qquad
 F''(x)^{-1/2}=2N^{1/4}\ell^{-3/4}.
\]

The two residue classes combine with the outer \(1/(2i)\) to give
\(e(-1/8)\chi_4(\ell)\).  The actual-profile transform is therefore

\[
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
\]

with \(P_U\) exactly as in (151.C52a).  The coefficient
\(B_{1,U}(1)\) is bounded by the accepted half-weight norm and is
retained in every pair deduction.

For the second principal transform,
\(g_\sigma(m)=2\sqrt{N(m+\sigma/4)}\) has saddle
\(m=N/p^2-\sigma/4\) and Legendre phase
\(N/p+\sigma p/4\).  Its stationary amplitude is the reciprocal of
the first one, and the curvature units \(e(1/8)\) and \(e(-1/8)\)
cancel.  Thus the phase and principal symbol self-return exactly.  The
candidate correctly leaves lower symbols, nonstationary pieces, and
endpoints in the accepted boundary ledger.

Finally, a bound for the recombined square is not a bound for an
arbitrary signed subset of its cross terms.  The Bourgain result is a
full-row owner; the TTY result is a low-row-square owner with the
\(L>L_0\) square and low-high cross term excluded.  Only at \(D=1\),
where centeredness makes every nonexact pair a collar pair, can the
accepted exact and packet owners be subtracted from the full-row
estimate to isolate the large-wrap collar.

## 4. First doubtful or unproved step

There is no failed mathematical step in the stated strict ranges.  The
first unproved continuation is the low-two-adic residual (151.C27),
with

\[
 j<J_*,\qquad k\notin\mathcal K_0,\qquad
 0<|\rho|\leq hr_1r_2/D,
\]

outside the Bourgain all-row corridor, or outside the TTY corridor for
the low-row component.  The transferred character does not remove the
\(h\mid g\) fibre, and taking absolute values after recovery returns
the rejected all-shift capacity.  At \(D=L=1\), the equivalent first
missing input is a target-sized signed estimate for \(P_U\); another
bare \(B\)-process does not provide it.

The five literalization issues raised during review have all been repaired
in the current candidate: the full \(t_i,s_i,u_i,v_i\) restrictions,
the convention \(\nu_2(0)=+\infty\), the nonduplicating interpretation
of (151.C10) in (151.C27), positive-\(q\) support and zero extension
before Poisson, and the corrected source-card versus graph-node wording.
No further repair is required by this mathematics review.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal residual | **GREEN.**  Character, phase, profiles, prefixes, incidence masks, common gcd, imprimitive denominator, and the exact coefficient expansion are retained. |
| positivity and factor identity | **GREEN.**  The one-factor identities prove positivity uniformly, including denominator-divides-\(N\). |
| parity and valuation ledger | **GREEN.**  Both signs of \(k\), both parities of \(N\), all relations of \(j\) to \(\nu_2(N)\), and \(\delta=0\) are covered. |
| character transfer | **GREEN.**  It is applied only to the odd quotients \(x,y\), never unlawfully to \(A,B\). |
| inverse \(h\mid g\) bijection | **GREEN.**  Support, reducedness, gcd, centering, collar, packet, and profile tests are all reimposed. |
| high-two-adic sparse range | **GREEN.**  The count and the accepted arbitrary fixed-wrap owner match exactly. |
| actual-profile all-scale BV | **GREEN.**  Bulk, radial/prefix, cone, products, components, zero extension, and prefix ownership are controlled. |
| Mobius and residue normalization | **GREEN.**  Coprimality is resolved first, the character costs two classes, and \(c^{\kappa-\lambda}\) is summable over divisors. |
| proper intervals and \(\mathcal T<H\) edge | **GREEN.**  Source interval uniformity is used when legal; the fixed comparable edge is covered by the second-derivative estimate. |
| Bourgain source and powers | **GREEN.**  Theorem 6 is global in the exponent-pair class, and (151.C41)--(151.C43) are arithmetically exact. |
| TTY source and powers | **GREEN.**  The shifted reciprocal is a uniform model phase, and (151.C45)--(151.C46) yield exactly \((1424,1816,534;819)\). |
| boundary-complete \(D=L=1\) transform | **GREEN.**  The actual compact profile has no uncontrolled every-integer jump, and the transform error is target-sized. |
| dual self-return versus gain | **GREEN.**  Only phase and principal symbol are called involutive; the capacity is not turned into a signed lower bound. |
| row versus isolated collar | **GREEN.**  Full-row, low-row, \(D=1\), and \(D>1\) scopes are distinguished, and the high-row square and cross term are named. |
| downstream scope | **GREEN.**  The low-adic residual, complements outside the row corridors, every \(t\geq2\) layer, Round-138 cross owner, M9--M1, M9--M2, endpoint assembly, M9, bridge, quarter target, and global exponents remain open. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The review used:

1. protocol.md;
2. state/active_campaign.yml;
3. state/proof_obligations.yml, only for the exact accepted Round-148--150
   nodes and the TTY/Bourgain interfaces;
4. the reviewed conductor candidate;
5. the three Round-151 reports:
   large_wrap_character_factorization_attack.md,
   blind_d1_reciprocal_bprocess_feasibility.md, and
   large_wrap_shifted_divisor_source_audit.md;
6. preliminary_tty_corridor_review.md and, only after the independent
   derivation, independent_bprocess_endpoint_review.md for seam
   reconciliation;
7. sources/tao_trudgian_yang_2025.md and the corrected
   sources/bourgain_2017_exponent_pair.md.

The exact inherited mathematical artifacts inspected were:

1. the Round-148 conductor reciprocal-transform candidate;
2. the Round-148 signed_squarefree_reciprocal_attack.md report, only for
   the explicit factor and transition ledger cited by its candidate;
3. the Round-149 conductor gcd-lift compression candidate;
4. the Round-150 conductor small-wrap and large-wrap-boundary candidate;
5. the Round-150 conductor adjudication.

No unrelated historical strategy, numerical computation, or unaccepted
theorem was used as a proof dependency.

## 7. Recommended state effect

**Promote.**  The recommended accepted kernel is:

1. the exact shifted-factor identity, positivity, full parity ledger,
   mod-four transfer, and inverse divisor fibre;
2. the all-scale high-two-adic target-safe wrap family;
3. the actual-profile all-scale sampled-BV lemma;
4. the source-legal Bourgain full-row corridor
   \(M^{29}\gg R^{52}D^{84}\);
5. the source-legal TTY low-row corridor
   \(M^{819}\gg R^{1424}D^{1816}L_0^{534}\);
6. the boundary-complete \(D=L=1\) transform, principal-symbol
   self-return, and no-gain capacity ledger.

Revise the narrower Bourgain graph source node in the same mechanically
validated State Patch that records the new corridor; the corrected source
card alone does not mutate the authoritative graph.

Do not promote a complete isolated collar theorem for \(D>1\).  Promote
the complete \(D=1\) large-wrap collar only in the Bourgain full-row range
after explicit subtraction of the accepted exact and fixed-wrap owners.
Record the TTY statement as a low-row-square component with its high-row
square and low-high cross term open.  Retain every downstream obligation
named in Section 5 as open.

Final decision: **GREEN**.

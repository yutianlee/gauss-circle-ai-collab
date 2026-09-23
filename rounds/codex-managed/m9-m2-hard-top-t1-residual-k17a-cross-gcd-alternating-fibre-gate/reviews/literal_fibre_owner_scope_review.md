# Round 176 review: literal fibre owner and scope

## 1. Review verdict

**Overall finding: PASS WITH NARROW REPAIRS.**

The literal discovery report correctly derives both opposing cross-gcd
coordinates, multiplicity one, the character half-frequency, the
fibre-stable original gcd, and the exact canonical Fourier expansion.  Its
fixed-proportion cross-gcd estimate is a genuine owner-complete theorem for
the stated literal subaggregate.  It includes both orientations, the full
non-polylogarithmic shift range, squarefree atoms, both selector statuses,
all endpoints and zero extensions, the Fejer weight, and the outer real
part.  It is a counting theorem and needs no relative-interior or phase
hypothesis.

The promotable strict statement should be restated as follows.  Define the
orientation-dependent cross gcd on every opposing incidence by

\[
 \kappa_*=
 \begin{cases}
  (d,m'),&d'>d, m'<m,\\
  (d',m),&d'<d, m'>m.
 \end{cases}
\tag{176.R1}
\]

For every **fixed** \(0<\delta<1/2\), independently of (X,L,H,J),

\[
 \boxed{
 \left|\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,,2,\,{\rm opp},
 (d,d')<\gamma L,\,\kappa_*\ge\delta L}\right|
 \ll_{\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{176.R2}
\]

The restriction \(\delta<1/2\) is needed only to make the sector
potentially nonempty: every incidence has \(r=2\kappa_*n<R_0\), hence
\(\kappa_*<R_0/2\).  For fixed \(\delta\ge1/2\), the displayed sector is
eventually empty, apart from immaterial ceiling-edge possibilities.  No
relation between \(\delta\) and \(\gamma\) is needed.  If \(\delta\) is
allowed to shrink with (L), (176.R2) is no longer a target-scale theorem;
the actual ledger is \(O(L^2\delta^{-1}X^\varepsilon)\).

The full K17a target remains unproved.  The discovery report's transform
obstruction is correctly route-scoped: it rules out positive fibrewise or
dual-mode recombination, not a signed joint theorem and not the literal
aggregate itself.

## 2. Exact seams and hypotheses

Retain the statement-only range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\tag{176.R3}
\]

with fixed \(0<\gamma<1\) and

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.R4}
\]

All claims below concern nonzero literal endpoint atoms, so the two
products are squarefree and the full coefficient, selector, parity branch,
profile, hard value, endpoint, and zero-extension conventions remain in
force.  The fibre-stable original-gcd identity depends on this squarefree
support and must not be promoted as an identity for arbitrary geometric
quadruples outside it.

In the plus orientation, put

\[
 d=\kappa u,\quad m'=\kappa v,\quad
 d'=\kappa u+2s,\quad m=\kappa v+2w,\quad
 sv-wu=n>0.
\tag{176.R5}
\]

In the minus orientation, put

\[
 d'=\kappa u,\quad m=\kappa v,\quad
 d=\kappa u+2s,\quad m'=\kappa v+2w,\quad
 uw-sv=n>0.
\tag{176.R6}
\]

In either case, ((u,v)=1), \(\kappa,u\) are odd,

\[
 r=2\kappa n,\qquad
 (s,w)=(s_0,w_0)+(u,v)t,\qquad
 \chi_4(d')\chi_4(d)=(-1)^{s_0}(-1)^t,
\tag{176.R7}
\]

and both endpoint products advance by \(2\kappa uv\).  These formulas
cover the two opposing orientations disjointly and with multiplicity one.

The blind report uses the original-gcd coordinates

\[
 G=(d,d'),\quad d_{\rm lo}=Ga,\quad
 d_{\rm hi}=G(a+2k),\quad m_{\rm lo}=b,\quad
 m_{\rm hi}=b+2w,
\tag{176.R8}
\]

with signed determinant (K=kb-aw).  Put

\[
 \eta=(a,b),\qquad a=\eta a_0,\qquad b=\eta b_0,\qquad
 K=\eta K_0.
\tag{176.R9}
\]

On a literal atom, squarefreeness of the endpoint containing
(G(a+2k)b) gives ((G,b)=1).  Therefore the cross gcd in (176.R1) is

\[
 \boxed{\kappa_*= (Ga,b)=(a,b)=\eta.}
\tag{176.R10}
\]

The exact dictionary from the blind variables to the cross variables is

\[
 \kappa_*=\eta,\qquad u=Ga_0,\qquad v=b_0,\qquad
 n={G|K|\over\eta}=G|K_0|,\qquad s=Gk.
\tag{176.R11}
\]

For every admitted solution, ((a,k)=1) and
(b_0k-a_0w=K_0).  Since ((a_0,b_0)=1), this implies

\[
 (a_0,K_0)=1.
\tag{176.R12}
\]

Consequently

\[
 (u,n)=(Ga_0,G|K_0|)=G,
\tag{176.R13}
\]

which is exactly the discovery formula ((d,d')=(u,n)).  The blind
common-translation step and character also agree:

\[
 {2Gab\over\eta}=2\eta uv,\qquad
 (-1)^k=(-1)^{Gk}=(-1)^s,
\tag{176.R14}
\]

because (G) is odd.  Thus the discovery and blind parametrizations are
not competing decompositions; they are the same fibres with
\(\kappa_*=(a,b)\) on the blind side.

## 3. Independent derivations

### 3.1 Multiplicity and original-gcd seam

Every opposing incidence has exactly one of the two strict sign patterns
in (176.R1).  The chosen cross gcd then uniquely determines
(u,v), and \(n=r/(2\kappa_*)\).  The primitive equation in (176.R5) or
(176.R6) has the complete solution set
((s,w)=(s_0,w_0)+(u,v)t).  A canonical representative for \(s_0\pmod u\)
makes (t) unique.  Conversely these data reconstruct the four endpoint
factors and their orientation.  This verifies injectivity, surjectivity,
and disjointness of the two orientations.

For (176.R5), squarefreeness of
\((\kappa u+2s)\kappa v\) gives
\((\kappa u+2s,\kappa v)=1\), hence \((\kappa,s)=1\).  Therefore

\[
 (d,d')=(\kappa u,\kappa u+2s)
       =(\kappa u,s)=(u,s)=(u,n),
\tag{176.R15}
\]

where the last equality uses (sv-wu=n) and ((u,v)=1).  In (176.R6),
the squarefree lower product gives the same \((\kappa,s)=1\), and
(uw-sv=n) proves the same result.  Thus the low original-gcd cutoff is
constant in (t), but remains distinct from \(\kappa_*\).

### 3.2 Canonical DFT and normalized norms

For odd modulus (m), define

\[
 E_m(x)=(-1)^{[x]_m},\qquad
 \widehat E_m(j)=\sum_{x=0}^{m-1}E_m(x)e(-jx/m).
\tag{176.R16}
\]

The finite geometric series is exact:

\[
 \widehat E_m(j)={2\over1+e(-j/m)}
 ={e(j/(2m))\over\cos(\pi j/m)}.
\tag{176.R17}
\]

Let \(c_m(j)=\widehat E_m(j)/m\) be the normalized inverse-transform
coefficient.  Then

\[
 \|c_m\|_{\ell^1(\mathbb Z/m\mathbb Z)}\asymp\log(2m),
 \qquad
 \|c_m\|_{\ell^2(\mathbb Z/m\mathbb Z)}=1,
\tag{176.R18}
\]

and

\[
 \|c_m\|_{\ell^\infty}
 ={1\over m\sin(\pi/(2m))}\asymp1,\qquad c_m(0)={1\over m}.
\tag{176.R19}
\]

The \(\ell^2\) identity is Parseval; the \(\ell^1\) estimate is the
harmonic sum of reciprocal distances to (m/2).  Thus the canonical
sawtooth has logarithmic algebra cost but no power contraction.

The discovery expansion with modulus (u) is correct, but the blind seam
gives a smaller exact modulus.  Let (G=(u,n)), (u=Gu_0), and
(n=Gn_0).  The canonical cross residue is a multiple of (G), and

\[
 E_u(\bar v n)=E_{u_0}(\bar v n_0).
\tag{176.R20}
\]

Under (176.R11), (u_0=a_0), and the cross anchor (s_0=Gk_0).
Therefore the minimal Fourier expansion is modulo the blind primitive
modulus (a_0=u/(u,n)), with norms (176.R18)--(176.R19).  The report's
use of modulus (u) loses only a logarithm and is not an error, but the
primitive modulus should be recorded in any promoted kernel.

### 3.3 Recomputed strict-sector capacity

The shift condition gives

\[
 1\le n<{R_0\over2\kappa_*},\qquad
 \kappa_*<{R_0\over2}.
\tag{176.R21}
\]

For fixed \(\kappa_*\), the endpoint scale gives

\[
 \#u\ll {L\over\kappa_*},\qquad
 \#v\ll {L\over\kappa_*},\qquad
 \#n\ll {L\over\kappa_*}.
\tag{176.R22}
\]

The geometric (t)-interval has

\[
 \#t\ll1+\kappa_*:
\tag{176.R23}
\]

one step changes the moving divisor and cofactor by
\(2u,2v\asymp L/\kappa_*\), while their allowed ranges have length
\(O(L)\).  Literal squarefree conditions, selectors, profiles, endpoints,
and zero extension only delete sites from this interval.

Using \(|1-r/R_0|\le1\), bounded endpoint coefficients, and unit phase,
then summing both orientations, gives for \(K\ge1\)

\[
 \begin{aligned}
 \left|\mathfrak C^{\rm rem}_{\kappa_*\ge K}\right|
 &\ll_\varepsilon X^\varepsilon
 \sum_{\substack{\kappa_*\ge K\\\kappa_*<R_0/2}}
 \left({L\over\kappa_*}\right)^3(1+\kappa_*)\\
 &\ll_\varepsilon {L^3\over K}X^\varepsilon.
 \end{aligned}
\tag{176.R24}
\]

Taking \(K=\delta L\) proves (176.R2).  This bounds the modulus of the
complete complex subaggregate, so it is stronger than the required bound
for its outer real part.  The lower cutoff \(R_{\log}<2\kappa_*n\), the
original-gcd cutoff, squarefree support, selectors, both parity branches,
hard values, endpoints, and the Fejer factor have all been imposed before
the majorization and only delete or downweight incidences.  Hence the
sector is owner-complete, and its exact complement is
\(\kappa_*<\delta L\).

The same count is visible in the blind coordinates.  By (176.R10), the
strict sector is \(\eta=(a,b)\ge\delta L\).  Write
\(a=\eta a_0\), \(b=\eta b_0\), and \(K=\eta K_0\).  The endpoint and
shift ranges force \(G,a_0,b_0,K_0=O_\delta(1)\); the common-translation
fibre has \(O_\delta(1+\eta)\) sites.  Summing this over
\(\delta L\le\eta<R_0/2\) gives \(O_\delta(L^2)\), in agreement with
(176.R24).

No estimate in (176.R21)--(176.R24) uses (J,H), a phase derivative, a
smooth cell, or a relative-interior lower bound.  Thus the strict theorem
is uniform throughout (176.R3).  By contrast, the report's
\(T\asymp\kappa_*\) and stationary-phase asymptotics apply only on full
fixed-relative interior fibres; they support the stated route-capacity
audit, not the strict-sector proof.

## 4. First unproved step and required repairs

The first unproved affirmative step remains the literal signed joint
inverse-residue estimate after the canonical DFT, with the square-root
phase, selected/no-pair field, squarefree recombination, endpoints, and
both orientations retained before every positive norm.  Neither report
proves that estimate.  In particular, short \(\kappa_*=O(1)\) fibres have
only (O(1)) internal sites but collectively retain (L^3) incidence
capacity, so an internal alternating estimate cannot close the complement
of (176.R2).

The following repairs are required before promotion:

1. State \(\kappa_*\) piecewise as in (176.R1), so the strict sector is a
   literal partition of both orientations.
2. Quantify \(\delta\) as fixed independently of (X,L,H,J).  Use
   \(0<\delta<1/2\) for a nonvacuous strict sector; for
   \(\delta\ge1/2\), explicitly call the result vacuous.  Do not insert a
   hidden relation \(\delta<\gamma\).
3. Scope ((d,d')=(u,n)) to nonzero squarefree atoms.  Its proof uses
   endpoint coprimality and is not a statement about filter-erased
   geometric arrays.
4. Record the primitive canonical modulus
   (u/(u,n)=a_0) and the normalized norms
   (176.R18)--(176.R19).  The modulus-(u) expansion is valid but not
   minimal.
5. Replace any bare finite-(L) phrase \(J\ge L^2\) by the asymptotic
   consequence (L^2=o(J)) of \(L\ll H\le J^{1/2}\), and keep every
   \(T\asymp\kappa_*\) derivative assertion restricted to full
   fixed-relative interior fibres.
6. Preserve the no-go's present route scope.  Positive dual capacity,
   constant-sign canonical families, arbitrary-support masks, and
   dechirped arrays are controls against a mechanism, not physical lower
   bounds.

No repair to the exponent (L^2), the owner boundary, the nonpolylog shift
range, or the literal endpoint coverage of (176.R2) is required.

## 5. Findings and controls

| Seam or control | Finding | Review outcome |
|---|---|---|
| Both opposing orientations | (176.R5)--(176.R7) give disjoint plus/minus maps; the sign of the blind determinant gives the same split. | **PASS** |
| Multiplicity | Orientation, cross gcd, primitive solution, and canonical residue reconstruct every ordered incidence once. | **PASS** |
| Original gcd | On nonzero squarefree atoms, ((d,d')=(u,n)) in both orientations. | **PASS WITH SCOPE REPAIR** |
| Blind compatibility | The exact dictionary is (176.R10)--(176.R14); blind ((a,b)) is the cross gcd. | **PASS** |
| Character law | The cross law \(E_u(\pm\bar v n)(-1)^t\) equals the blind law ((-1)^{k_0+t}). | **PASS** |
| Canonical DFT | Formula (176.R17) is exact; normalized \(\ell^1,\ell^2,\ell^\infty\) norms are (176.R18)--(176.R19). | **PASS WITH PRIMITIVE-MODULUS REPAIR** |
| Parity and even branch | \(\kappa_*,u\) are odd and \(r=2\kappa_*n\); the retained even branch only deletes or further restricts the count. | **PASS** |
| Strict-sector row count | \(O((L/\kappa_*)^3(1+\kappa_*))\) at fixed cross gcd. | **PASS** |
| Global strict-sector count | \(O(L^3/K)\), hence \(O_\delta(L^2)\) for fixed \(K=\delta L\). | **PASS** |
| Owner completeness | Both orientations, all nonpolylog shifts, literal fields, Fejer weight, endpoints, and the outer real part are owned. | **PASS** |
| \(\delta\) quantifier | Nonvacuous only for fixed \(0<\delta<1/2\); shrinking \(\delta\) costs \(\delta^{-1}\). | **REVISE STATEMENT** |
| \(\gamma\) quantifier | No relation with \(\delta\) is required; the cutoff only deletes atoms. | **PASS** |
| \(H,J\) quantifiers | Strict counting is independent of them; phase asymptotics use \(L^2=o(J)\) and relative interior. | **PASS WITH WORDING REPAIR** |
| Short fibres | They prevent an automatic full-target inference; no physical mass conclusion follows. | **PASS AS ROUTE OBSTRUCTION** |
| Squarefree/selector/endpoints | Retained literally for the strict count; no unsupported smoothness is used. | **PASS** |
| Constant-sign and dechirped controls | They falsify coefficient-blind cancellation only and are explicitly quarantined. | **PASS** |
| Full target | No owner-complete bound for \(\kappa_*<\delta L\) is proved. | **FAIL / REMAINS OPEN** |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This independent review used exactly:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/blind_statement.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/literal_cross_gcd_alternating_fibre_attack.md`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/blind_k17a_variable_determinant_rederivation.md`; and
5. the assigned review brief
   `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/briefs/literal_fibre_owner_scope_review.md`.

No active-state file, proof graph, strategy, sibling hostile report,
candidate, source card, web source, or computation was used.  No report or
shared-state artifact was edited.

## 7. Promotion recommendation

**Promote, after the statement repairs in Section 4, only the exact
two-orientation fibre identities, their compatibility dictionary, the
primitive canonical DFT, and the strict theorem (176.R2).**

The strict theorem should have a named complement
\(\kappa_*<\delta L\) and should be recorded only for fixed
\(0<\delta<1/2\).  It is stronger than a real-part estimate on its sector
because (176.R24) bounds the full modulus.  It changes no parent owner and
does not close K17a.

Retain the positive-transform self-return and the constant-sign canonical
families only as route-scoped obstruction evidence.  Do not promote any
geometric, arbitrary-support, selector-erased, or dechirped control to
physical lower mass.  The full non-polylogarithmic K17a aggregate, complete
residual scalar, all hard-TOP parents, BAL, UNBAL, M9--M2, M9--M1/GAR,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent owner remain open.

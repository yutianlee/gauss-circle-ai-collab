# Round 176 candidate mathematical and scope review

## 1. Verdict

**Verdict: AMBER, repairable to GREEN without changing the mathematical
conclusion.**

The candidate's principal algebra is correct: both cross-gcd
parametrizations are multiplicity one; the character is the claimed
half-frequency; the literal squarefree support gives
((d,d')=(u,n)); the reconciliation with the statement-only coordinates
is correct; the finite Fourier formulas and logarithmic algebra norm are
correct; the fixed-proportion cross-gcd sector is target-safe; and the
local estimate (176.C29), once its symbols are defined literally, closes
the full \(L^2X^\varepsilon\) ledger.

Promotion should wait for four mandatory repairs:

1. write the exact two-orientation aggregate and define
   \(I^\pm,\Lambda^\pm,\Psi^\pm\), including \(s_t,w_t\ge1\), rather than
   asking zero extension to enforce the opposing orientation;
2. correct the malformed definition of (x(t)) before (176.C25);
3. add the explicit even-even two-adic ledger; and
4. either prove the asserted full two-variable positive-Poisson
   self-return or remove that mechanism from the formal no-go's scope.

The remaining repairs below are precision repairs.  The target, every
parent, and every exponent owner must remain open.

## 2. Formula-by-formula audit of (176.C1)--(176.C30)

| Formula | Verdict | Audit |
|---|---|---|
| (176.C1) | GREEN | The frozen relation \(1\ll L\ll H\le J^{1/2}\), \(R_0=\lceil L\rceil\), and fixed \(\gamma\) is correct. |
| (176.C2) | GREEN | The polylogarithmic cutoff is exact and is removed only once later through \(R_{\log}<2\kappa n<R_0\). |
| (176.C3) | GREEN with precision repair | The literal atom and all named fields are correct.  The authorized packet gives \(|\lambda|\ll1\); weakening this to \(X^\varepsilon\) is harmless only after choosing the auxiliary exponent smaller than the final exponent at the two endpoints.  State that renaming explicitly. |
| (176.C4) | AMBER | The restrictions are correct and the prose retains one outer real part, but no exact displayed aggregate follows.  This omission is material because the Fejer factor, positivity of the half-gaps, endpoint ordering, and conjugation are otherwise never simultaneously visible. |
| (176.C5) | GREEN | In the plus orientation, \(\kappa=(d,m')\), \(d=\kappa u\), \(m'=\kappa v\), and ((u,v)=1) are exact. |
| (176.C6) | GREEN | From (p=2s,q=2w), one gets \(r=2\kappa(sv-wu)=2\kappa n\), with (n>0). |
| (176.C7) | GREEN | \(s_0=[\bar v n]_u\) and (w_0=(s_0v-n)/u) solve the primitive equation.  For (u=1), specify the harmless convention (s_0=0). |
| (176.C8) | AMBER, mandatory repair | The complete solution lattice is correct, but zero-extended endpoint coefficients do **not** enforce (s_t,w_t>0): both endpoints can be valid while the tuple belongs to a different displacement sector.  The permitted (t)-set must explicitly include \(s_t\ge1,w_t\ge1\) in each orientation. |
| (176.C9) | GREEN | Direct substitution gives the common step \(2\kappa uv\) at both products. |
| (176.C10) | GREEN | Since (u) is odd, \((-1)^{s_0+ut}=E_u(\bar v n)(-1)^t\).  The mirror sign \(E_u(-\bar v n)(-1)^t\) is also correct. |
| (176.C11) | GREEN | On a nonzero squarefree plus atom, ((d',m')=1) and \(\kappa\mid m'\) imply \((\kappa,s)=1\).  Hence \((d,d')=(\kappa u,s)=(u,s)=(u,n)\).  The lower squarefree product proves the same identity in the minus orientation. |
| (176.C12) | GREEN | The geometric-series transform is exact for odd (u): \(2/(1+e(-k/u))=e(k/(2u))/\cos(\pi k/u)\). |
| (176.C13) | GREEN | Fourier inversion and the normalized \(O(\log(2u))\) \(\ell^1\)-norm follow from the reciprocal-cosine harmonic sum.  The modes \(k=(u\pm1)/2\) have size \(\asymp u\). |
| (176.C14) | GREEN with endpoint wording repair | The strict-sector estimate is correct.  Replace “empty when \(\delta\ge1/2+o(1)\)” by the exact condition \(\delta L\ge R_0/2\), or simply state the nonempty fixed range \(0<\delta<1/2\); \(r=2\kappa n<R_0\) is the reason. |
| (176.C15) | GREEN as a positive-transform capacity statement | For \(T\asymp\kappa\), \(F\asymp2Jn\kappa/L\), so \(F/T^2\asymp2Jn/(\kappa L)\).  Since \(2\kappa n<R_0\asymp L\), \(n\ge1\), and \(J\gg L^2\), this is bounded below by a positive constant (and in the intended separated range is large).  It does not give an actual row lower bound. |
| (176.C16) | GREEN only after scope repair | The label is appropriately route-scoped and is explicitly not physical lower mass.  The rowwise positive-transform part is proved.  The full two-variable positive-Poisson claim must either receive the Hessian/dual-volume proof or be deleted from the mechanisms covered by the candidate. |
| (176.C17) | GREEN | The determinant identity is exact. |
| (176.C18) | GREEN | For odd \(\kappa u\), translating it by (2s) changes \(\chi_4\) by ((-1)^s). |
| (176.C19) | GREEN | Every equality is justified: oddness removes the factor (2), squarefreeness removes \(\kappa\), and ((u,v)=1) converts ((u,s)) to ((u,n)). |
| (176.C20) | GREEN | These are exactly the blind rederivation's original-gcd coordinates for the plus orientation. |
| (176.C21) | GREEN | With (g=(u,n)), one has \(a=\kappa u/g\), (k=s/g), \(m_0=\kappa v\), \(K=\kappa n/g\), and \((a,m_0)=\kappa\).  Thus \(2gam_0/(a,m_0)=2\kappa uv\).  The blind step (a/(a,m_0)=u/g) is odd, so its character also flips once per physical translation. |
| (176.C22) | GREEN | Since (u) is odd, ((-e(-k/u))^u=-1), giving numerator (2). |
| (176.C23) | GREEN | Literal support gives \(u,v\asymp L/\kappa\), and \(2\kappa n<R_0\) gives \(n\ll L/\kappa\). |
| (176.C24) | GREEN | Expanding \(1+\kappa\) gives tails (L^3/K^2) and (L^3/K).  At \(K=\delta L\), both are \(O_\delta(L^2)\) or smaller. |
| (176.C25) | RED as written, mandatory typographical repair | “\(x=N_0+2\kappa uv,t\)” does not define a (t)-dependent product.  It must read \(x(t)=N_0+2\kappa uv\,t\).  Without this correction, (176.C26)--(176.C27) do not follow. |
| (176.C26) | GREEN after repairing (176.C25) | Taylor expansion at \(x\asymp L^2\), with step \(2\kappa uv\asymp L^2/\kappa\) and gap \(2\kappa n\), gives the displayed second- and third-derivative scales. |
| (176.C27) | GREEN with wording repair | The absolute stationary-mode ledger is \(\sqrt F+T/\sqrt F\).  Because \(F/T^2\gg1\), it is not power-smaller than (T); the trivial estimate wins.  Say “is \(\gg T\)” or “gives no power saving,” rather than the literal word “exceeds,” which is not licensed by \(\asymp\)-constants. |
| (176.C28) | GREEN | The \(1+\kappa\) term gives \(L^3/K+L^3/K^2\ll L^3/K\) for \(K\ge1\).  The hypothetical (O(1)) row tail is (L^3/K^2); at (K=L^{1/2}) the two ledgers are (L^{5/2}) and (L^2). |
| (176.C29) | AMBER, mandatory definition repair | The estimate is genuinely sufficient, but \(I^\pm,\Lambda^\pm,\Psi^\pm\) are undefined in the candidate.  They must be defined by an exact two-orientation identity including the Fejer factor, exact nonpolylog range, \((u,n)<\gamma L\), \(s_t,w_t\ge1\), both endpoint coefficients with the correct conjugation, and zero extension. |
| (176.C30) | GREEN | \(\sum_{\kappa\ll L}(L/\kappa)^2\kappa=L^2\sum_{\kappa\ll L}1/\kappa\ll L^2\log L\).  Combining this with (176.C13) costs at most a second logarithm, absorbed into \(X^\varepsilon\). |

## 3. Literal coefficient, orientation, parity, and endpoint seams

The candidate correctly keeps the literal coefficient in (176.C3), names
the selector, both parity branches, endpoints, hard values, and zero
extension, and states that the real part stays outside.  It nevertheless
needs an exact identity, not only prose.  A sufficient repair is to define
for the plus orientation

\[
 \begin{aligned}
 N_t^+&=\kappa u(\kappa v+2w_t),\\
 N_t^++2\kappa n&=\kappa v(\kappa u+2s_t),\\
 \Psi^+(t)&=J(\sqrt{N_t^++2\kappa n}-\sqrt{N_t^+}),
 \end{aligned}
\]

and

\[
 \begin{aligned}
 \Lambda^+(t)={}&
 \left(1-{2\kappa n\over R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}
 \mathbf1_{s_t,w_t\ge1}\\
 &\times
 \lambda_{N_t^++2\kappa n}(\kappa u+2s_t)
 \overline{\lambda_{N_t^+}(\kappa u)}.
 \end{aligned}
\tag{R176.1}
\]

For the minus orientation it should define

\[
 N_t^-=\kappa v(\kappa u+2s_t),\qquad
 N_t^-+2\kappa n=\kappa u(\kappa v+2w_t),
\]

with

\[
 \Lambda^-(t)=
 \left(1-{2\kappa n\over R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}
 \mathbf1_{s_t,w_t\ge1}
 \lambda_{N_t^-+2\kappa n}(\kappa u)
 \overline{\lambda_{N_t^-}(\kappa u+2s_t)}.
\tag{R176.2}
\]

Then the exact pre-DFT aggregate is one real part outside

\[
 \sum_{\kappa,u,v,n,t}
 E_u(\bar vn)(-1)^t\Lambda^+(t)e(\Psi^+(t))
 +
 \sum_{\kappa,u,v,n,t}
 E_u(-\bar vn)(-1)^t\Lambda^-(t)e(\Psi^-(t)).
\tag{R176.3}
\]

Equations (R176.1)--(R176.3) also repair the undefined notation in
(176.C29), preserve the correct conjugation, and make the Fejer and
outer-real-part seams mechanically checkable.

The two-adic ledger should be added explicitly.  In the odd-product branch
(v) is odd.  In the even-even squarefree branch, \(\kappa,u\) remain odd,
(v=2v_1) with (v_1) odd, \(4\mid r\), hence (n) is even.  The equations
(n=sv-wu) or (n=uw-sv) then force (w) even; because
(w_t=w_0+vt), that parity is fibre-stable.  Thus both products remain
\(2\pmod4\), while (s_t=s_0+ut) still flips parity at every step.  After
this branch split all squarefree Möbius progressions have odd modulus, so
they preserve ((-1)^t).

## 4. Recomputed strict-sector and route-capacity ledgers

Let \(U=L/\kappa\).  For fixed \(\kappa\), the multiplicity-one coordinate
has (O(U^2)) choices of ((u,v)), (O(U)) determinants (n), and
\(O(1+\kappa)\) geometric (t)-sites.  Therefore

\[
 \sum_{\kappa\ge K}U^3(1+\kappa)X^\varepsilon
 \ll \left({L^3\over K^2}+{L^3\over K}\right)X^\varepsilon.
\tag{R176.4}
\]

This proves (176.C14) at \(K=\delta L\).  Both orientations merely add a
factor two, and all literal restrictions delete atoms; no selector or
squarefree regularity is used.

If one had an \(O(X^\varepsilon)\) estimate for every complete fibre, the
tail would instead be

\[
 \sum_{\kappa\ge K}U^3X^\varepsilon
 \ll {L^3\over K^2}X^\varepsilon,
\tag{R176.5}
\]

which reaches \(L^2X^\varepsilon\) at (K=L^{1/2}).  The actual positive
B-process ledger has (1+2Jn/L) modes, saddle scale
\((\kappa L/(2Jn))^{1/2}\), and hence
\(\sqrt F+T/\sqrt F\), no better than \(T\asymp\kappa\).  Its tail is the
first term of (R176.4), (L^3/K), giving (L^{5/2}) at (K=L^{1/2}).

After the anchor DFT, one optimistic square-root saving in the (v)-sum
has capacity

\[
 \sum_\kappa
 (L/\kappa)_{u}(L/\kappa)_{n}\,\kappa_t
 (L/\kappa)^{1/2}_{v}
 \ll L^{5/2},
\tag{R176.6}
\]

so that route still needs a second joint saving.  This is a positive
capacity, not physical lower mass.

The candidate's full two-variable Poisson assertion is not proved in its
present text.  To retain it, add the phase

\[
 \Theta(s,w)=J\{\sqrt{\kappa v(\kappa u+2s)}
 -\sqrt{\kappa u(\kappa v+2w)}\}+s/2,
\]

for which the diagonal Hessian entries have sizes (J/L), the physical
((s,w))-strip has area (O(L)), the gradient-image volume is
(O(J^2/L)), and one stationary coefficient has scale (L/J).  Positive
dual recombination has (O(J)) capacity per anchor; taking the minimum
with the physical (O(L)) count and then summing
\((L/\kappa)^2\) anchors gives (O(L^3)).  Without this derivation, delete
full two-variable Poisson from the no-go in (176.C15)--(176.C16).

Finally, (176.C29) really is sufficient once (R176.1)--(R176.3) are in
place.  Its \(O(\kappa X^\varepsilon)\) bound, the normalized DFT
\(\ell^1\)-cost \(O(\log u)\), \(O((L/\kappa)^2)\) anchor pairs, and
(176.C30) give \(O(L^2(\log L)^2X^\varepsilon)\), which is
\(O(L^2X^{2\varepsilon})\) and hence the target after exponent renaming.

## 5. No-go scope, controls, and first unproved step

The no-go is correctly quarantined from physical lower mass.  The
constant-sign family (v=(u+1)/2,s=2n,w=n) proves only that the canonical
anchor does not force determinant alternation on an incomplete interval.
It does not prove literal squarefree-selector density or phase alignment.
Likewise, arbitrary one-parity masks and dechirped arrays falsify only
coefficient-uniform mechanisms.

The following controls are correctly handled, subject to the mandatory
repairs above:

- both opposing orientations and multiplicity one;
- the nonpolylogarithmic complement and the Fejer weight;
- cross gcd versus the fibre-stable original gcd;
- the half-frequency and its exact logarithmic-cost DFT;
- fixed-proportion and (L^{1/2}) cross-gcd ledgers;
- short fibres;
- odd squarefree Möbius progressions;
- selected and no-pair rows with no invented regularity;
- constant-amplitude, arbitrary-support, and dechirped controls;
- endpoint births, deaths, hard values, and zero extension;
- rowwise Abel, B-process, and positive dual recombination; and
- quarantine of every raw capacity and adversarial array from literal
  lower mass.

After the formal repairs, the first genuinely unproved mathematical step
is exactly (176.C29): a selector-aware signed joint inverse-residue and
square-root estimate, uniform also for the large near-half Fourier mode,
with all determinants and fibre sites retained before absolute values.
The candidate correctly leaves cancellation between orientations and a
different literal coefficient-sensitive joint theorem unexcluded.

## 6. Mandatory and optional repairs

### Mandatory before promotion

1. Add an exact identity equivalent to (R176.1)--(R176.3), define every
   symbol in (176.C29), and explicitly impose \(s_t,w_t\ge1\).
2. Replace the text before (176.C25) by
   \(x(t)=N_0+2\kappa uv\,t\).
3. Add the even-even branch ledger (v=2v_1), (n,w_t) even,
   \(4\mid r\), and explain why only odd square-progressions remain after
   the branch split.
4. Add the two-variable Hessian/dual-volume calculation above or narrow
   (176.C15)--(176.C16) to the rowwise positive-transform mechanisms that
   are actually proved.

### Precision repairs

5. Replace the empty-sector phrase by the exact inequality
   \(\delta L\ge R_0/2\).
6. State the auxiliary-\(\varepsilon\) renaming for two endpoint
   coefficients and the two logarithms in the implication from
   (176.C29).
7. Replace “exceeds (T)” in the discussion of (176.C27) by “is
   \(\gg T\) and therefore gives no power saving.”
8. Optionally add the mirrored version of (176.C20)--(176.C21); the plus
   version is already correct and sufficient to verify the coordinate
   reconciliation.

## 7. Dependencies and recommended state effect

This review used exactly:

- `protocol.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/blind_statement.md`;
- all three files in
  `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/candidates/formalized_cross_gcd_alternating_fibre_reduction.md`.

No candidate, report, proof graph, kernel, synthesis, control, or shared
state was edited.

**Recommended state effect after the mandatory repairs:** promote only the
two-orientation multiplicity-one reduction, (176.C11), (176.C12)--(176.C13),
the fixed-proportion strict sector (176.C14), and the explicitly scoped
positive-recombination no-go.  Retain (176.C29) as the first open analytic
step.  Do not promote the base-residue family, dechirped controls, or any
capacity ledger as literal lower mass.  Leave the complete K17a target,
the residual scalar, every hard-TOP parent, BAL, UNBAL, M9--M2, M9--M1/GAR,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent open.

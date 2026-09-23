# Blind post-unmask scaled-orientation verification

## Verdict: PASS

The formal candidate follows from its stated live physical facts
\(d,m,d',m'\asymp L\), the multiplicity-one primitive physical interface,
and the accepted linear Round-192 core decomposition.  The candidate's
main double-close estimate is an absolute physical-incidence count and
does not rely on the narrower \(k=1,\ r\equiv2\pmod4\) involution or on
coefficient cancellation.

No mathematical repair is required.  Promotion, if any, must retain the
candidate's strict-sector scope and still undergo the other required seam
and graph reviews.

## Artifact identity and review access

- Candidate:
  `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/candidates/formalized_hard_m1_t1_rho_large_gcd_scaled_close_sector.md`
- Candidate SHA-256:
  `ac9998ee1ac18a51993a26c2f6f20f9d711fa829f056878fa25e6c5e71e72f30`
- Repaired blind report:
  `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reports/blind_scaled_orientation_involution_rederivation.md`
- Blind-report SHA-256:
  `bce7e8be7f7d55d5bc6bbc3ef7c580742a48160881215da2e135127134f63c3d`
- Candidate-declared starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`

Only the candidate and repaired blind report were read for this post-unmask
comparison.  The graph hash above is the candidate's declared provenance;
it was not independently recomputed in this restricted review.

## Exact algebraic comparison

### Tuple order, products, and operator coefficient order

Both artifacts use the physical ordered tuple

\[
 (d,m,d',m'),\qquad N=dm,\qquad N+r=d'm',
\]

and the same map

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g).
\]

Thus the lower endpoint remains the lower endpoint and the upper endpoint
remains the upper endpoint.  Both products, \(r\), the Fejer factor, and
the square-root phase are unchanged.  The candidate's commutator

\[
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}
 -
 \lambda_{N+r,\sigma}(gm')\overline{\lambda_{N,\sigma}(gm)}
\]

has exactly the upper/nonconjugated and lower/conjugated order obtained in
the blind derivation.  The factor \(1/2\) in the candidate is correct when
the sum ranges over both members of every two-element orbit.

### Gcd, parity, involution, and character sign

On \(k=(m,m')=1\), even \(r\) and odd \(d,d'\) force \(m,m'\) to be odd.
Both artifacts then give

\[
 (gm,gm')=g,\qquad (d/g,d'/g)=1,\qquad \tau_g^2=1.
\]

The close mask is invariant because its two distances are merely negated.
On \(r\equiv2\pmod4\), the character product reverses sign.  The candidate
correctly confines this assertion to the narrower swapped sector and does
not use it in the absolute main estimate.

### Primitive coordinate map

The apparent tuple-order difference is only notational.  The blind report
orders the auxiliary variables as \((U,S,v,w)\) and obtains

\[
 (U,S,v,w)\mapsto(v,w,U,S).
\]

The candidate lists its primed tuple as \((U',v',S',w')\) and writes

\[
 (U',v',S',w')=(v,U,w,S).
\]

These are identical assignments:
\(U'=v,\ S'=w,\ v'=U,\ w'=S\).  The plus chart maps to the canonical
minus chart and preserves the positive determinant \(h\).  The candidate's
additional conclusions \((gv,U)=1\), \((v,w)=1\), and hence \((v,h)=1\)
use live squarefreeness and primitive coprimality facts that were absent
from the statement-only packet; they are compatible with, and strengthen,
the blind cross-gcd check.

## Count, floors, and determinant seam

The blind derivation supplied the floor-exact narrow-sector relations

\[
 F_g=\left\lfloor\frac{D_L}{2g}\right\rfloor,\qquad
 |\kappa j-w|\le F_g,\qquad
 |\kappa j+S|\le F_g,
\]

including \(F_g=0,1\), \(U=1\), small \(U\), and \(D_L\ge U\).  These
imply the candidate's coarser uniform bounds

\[
 S+w\ll D_L/g,\qquad |\kappa(U-v)|\ll D_L/g.
\]

The candidate never assumes \(D_L<U\).  Its \(1+\) choice bounds in
(193.C15) therefore cover every small-variable and floor endpoint seen
in the blind count.

The decisive post-unmask improvement is the live determinant ledger.
The blind derivation independently found

\[
 r=2\kappa gh,\qquad 0<r<L.
\]

The candidate uses the equivalent strict range \(0<r<R_0=\lceil L\rceil\)
to confine \(S\), at fixed \((\kappa,g,U,v,w)\), to an interval of length

\[
 \frac{R_0}{2\kappa gv}=O(1),
\]

because the live fact \(\kappa v=m'\asymp L\) is now available.  The other
live comparabilities give \(g=O(1)\), \(U=O(1+L/\kappa)\), only
\(O(1+D_L/\kappa)\) choices of \(v\) near \(U\), and \(O(1+D_L)\) choices
of \(w\).  Consequently

\[
 \sum_{\kappa\ll L}
 (1+L/\kappa)(1+D_L/\kappa)(1+D_L)
 \ll LD_L\log(2L)+LD_L^2.
\]

With \(D_L=\lceil L^{1/2}\rceil\), this is
\(O_\eta(L^2X^\eta)\).  The plus and minus orientations differ only by a
constant factor.  Heights, core predicates, coprimalities, selectors, and
literal support conditions delete atoms and introduce no extra \(Y\)
multiplicity because \(h\) is determined by \((U,v,S,w)\).

This argument does not use \(k=1\) or \(r\equiv2\pmod4\).  That agrees with
the blind report's explicit finding that those conditions are structural
for the canonical involution and sign reversal, not inputs to the raw
close count.  The candidate's stronger no-\(k\)/no-\(r\) absolute count is
therefore valid once the live multiplicity-one coordinates and
comparability facts are unmasked.

## Linear operator, bracket, and complement

The candidate correctly defines

\[
 \mathscr R_{\rm core}[P_{\rm cl}]
 =\mathscr R_{\rm core}(P_{\rm cl}W),
\]

meaning that the physical source is masked before Fourier expansion and
height differencing.  It does not commute a scalar mask through an already
formed Abel difference.  Formula (193.C19b) retains the exact mask
commutator, as well as transported sites, births, deaths, and zero
extensions.

Under the unmasked accepted linear identity

\[
 \mathscr H(W)=\mathscr S_{\le192}(W)+\mathscr R_{\rm core}(W),
\]

the whole masked physical source is bounded by the absolute incidence
count, while the previously safe pieces remain safe under physical
deletion by their positive counting/Fourier-mass ledgers and exact
zero-extended Abel inversion.  Hence

\[
 \mathscr R_{\rm core}(P_{\rm cl}W)
 =\mathscr H(P_{\rm cl}W)-\mathscr S_{\le192}(P_{\rm cl}W)
\]

has the claimed target bound.  The convention also handles \(T=0\):
the Farey projector remains zero and the entire inherited rho-large
remainder is present before applying the new physical split.

The complement is exact and disjoint:

\[
 1=P_{\rm cl}
 +\mathbf1_{|d-gm|>D_L}
 +\mathbf1_{|d-gm|\le D_L}\mathbf1_{|d'-gm'|>D_L}.
\]

Linearity therefore gives the three corresponding core terms.  The
candidate proves only the first and leaves both first-failure complements
open.

The blind report's common-cell/BV warning is not contradicted.  It showed
that involution algebra alone cannot compare arbitrary coefficient arrays.
The candidate bypasses that issue for the main theorem by absolutely
counting the entire physical double-close sector.  Its common-cell/BV
discussion is explicitly subsidiary and has the compatible
square-root-scale power ledger.

## Scope and independence qualification

The candidate's scope is correct: only the exact double-close core sector
and subsidiary finite involution identities are claimed.  It does not
close either complement, the rho-large core, complete \(t=1\), any
\(t\ge2\) range, an M1 or M2 parent, endpoint uniformity, M9, a bridge, the
quarter theorem, or any exponent.

This must **not** be described as a pristine fresh-context blind run.  Before
Round 193 launched, the blind reviewer performed a proof-status audit
through Round 192 and therefore had prior high-level graph context.  No
Round-193 strategy, claimant report, candidate, review, control, or sibling
conclusion was received before the blind report was completed.  The first
Round-193 claimant content seen was the candidate during this expressly
post-unmask stage.  Accordingly this is a disclosed, qualified
claimant-blind rederivation with pre-existing Round-192 context, not a
pristine-context blind review.

## Recommended state effect

**PASS** the blind-post-unmask seam for the exact strict double-close
sector.  Retain the no-cancellation control for arbitrary arrays and the
square-root-width method boundary.  Any State Patch must create at most the
subordinate strict-sector node described by the candidate and leave all
parents, bridges, theorem nodes, and exponent records unchanged.

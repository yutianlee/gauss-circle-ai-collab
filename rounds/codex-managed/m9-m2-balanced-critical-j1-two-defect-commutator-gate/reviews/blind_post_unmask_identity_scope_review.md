# Post-unmask review: blind two-defect identity, real symmetry, and no-go scope

- Campaign: m9-m2-balanced-critical-j1-two-defect-commutator-gate
- Reviewed task: blind_balanced_two_defect_rederivation
- Role: independent post-unmask identity and scope reviewer
- Graph reviewed: 4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac
- Verdict: **REPAIR**

## 1. Result and verdict

The report's coordinate algebra, defect transformations, swap invariance,
bilinear projection argument, local Abel identity, and gate product rules are
correct.  It rigorously disproves the naive identity which replaces the
complete zero-subtracted scalar by its double-antisymmetric independent-swap
projection.

The post-unmask audit nevertheless finds four material scope repairs.

1. The literal coefficient \(a_B^<(h,k)\) is real.  Hence
   \(\tau_h\tau_kW=W\), so the \((+-)\) and \((-+)\) weight projections
   vanish.  There is one parity complement, the \((++)\) term, not three.
2. The accepted literal amplitude is zero-extended.  On a global
   four-corner rectangular domain the support-crossing term is absorbed
   exactly into the projected weights; it is not an invariant extra
   boundary obstruction.
3. The genuine geometric sectors \(p=0\) and \(q=0\) are already
   \(O_\varepsilon(L^3X^\varepsilon)\) by a direct three-variable count.
   They disprove the naive identity but do not obstruct the target power.
4. The no-go applies only to the independent swap projection and to
   coefficient-uniform or scalar Abel implementations without a new
   actual-coefficient theorem.  It cannot reject every weighted, twisted,
   or coefficient-adapted commutator or every summation-by-parts route.

After these repairs, one nontrivial \((++)\) complement remains with only
the \(L^4X^\varepsilon\) positive ledger and no accepted \(L^3\) estimate.
Thus the route-specific no-go survives, while \((171.B1)\) remains open.

## 2. Coordinate bijection and the correct global domain

The map

\[
 ((h,k),(h',k'))\mapsto(h,k,p,q)
 =(h,k,h'-h,k'-k)
\]

has inverse

\[
 (h,k,p,q)\mapsto((h,k),(h+p,k+q))
\]

and multiplicity exactly one.  The defect identities

\[
 \Delta=hq+pk+pq,\qquad \rho=hq-pk
\]

and

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q)
\]

are exact.

The report's restricted-domain decomposition
\(\mathcal D=\mathcal D_\square\sqcup\mathcal D_\times\) and its
indicator (2.2) are mathematically valid.  Post-unmask, however, they are
not canonical.  Let \(I_h,I_k\) be finite integer intervals containing the
literal block support, extend \(a\) by zero, and sum on

\[
 \Omega=\{(h,k,p,q):h,h+p\in I_h,\ k,k+q\in I_k\}.
\]

Every point of \(\Omega\) has all four ambient corners, and \(\Omega\) is
invariant under

\[
 \tau_h(h,k,p,q)=(h+p,k,-p,q),\qquad
 \tau_k(h,k,p,q)=(h,k+q,p,-q).
\]

The original scalar is unchanged because
\(W=a(h,k)a(h+p,k+q)\) vanishes whenever either diagonal endpoint is
outside the literal support.  Cross-corner support failures now appear as
zeros in \(\tau_hW\) and \(\tau_kW\); there is no separate
\(\mathcal D_\times\) sum.  Thus the report may retain (2.2) as one exact
bookkeeping representation, but it must not promote a support-crossing
boundary as an unavoidable obstruction.

## 3. Gate invariance and the repaired two-projection identity

Under the two swaps,

\[
 \tau_h:(\Delta,\rho)\mapsto(\rho,\Delta),\qquad
 \tau_k:(\Delta,\rho)\mapsto(-\rho,-\Delta),
\]

and their product sends \((\Delta,\rho)\) to
\((-\Delta,-\rho)\).  Hence the strict double-far gate \(G\) is invariant.
There are no gate-boundary terms in the swap identity.

The report is correct that projecting \(W\) and \(H\) separately is valid
after summation.  For

\[
 \langle U,V\rangle_G=\sum_\Omega GUV,
\]

each swap is a self-adjoint permutation:

\[
 \langle\tau_hU,V\rangle_G=\langle U,\tau_hV\rangle_G,
 \qquad
 \langle\tau_kU,V\rangle_G=\langle U,\tau_kV\rangle_G.
\]

The four \(P_{\epsilon\eta}\) are mutually annihilating self-adjoint
idempotents whose sum is the identity.  Therefore

\[
 \langle W,H\rangle_G
 =\sum_{\epsilon,\eta}
   \langle P_{\epsilon\eta}W,P_{\epsilon\eta}H\rangle_G.
\]

No complex conjugation is missing: this is deliberately a bilinear pairing,
because the conjugation belonging to the original energy is already inside
\(W\).

Now use the unmasked fact that \(a\) is real.  With

\[
 a_{ij}=a(h+ip,k+jq),\qquad
 z_{ij}=e\!\left(\sqrt X\sqrt{(h+ip)(k+jq)}\right),
\]

one has

\[
 W=a_{00}a_{11},\quad
 \tau_hW=\tau_kW=a_{10}a_{01},\quad
 \tau_h\tau_kW=W.
\]

Consequently

\[
 P_{+-}W=P_{-+}W=0,
\]

\[
 P_{++}W=\frac12(a_{00}a_{11}+a_{10}a_{01}),\qquad
 P_{--}W=\frac12(a_{00}a_{11}-a_{10}a_{01}).
\]

Writing \(A=z_{00}\overline{z_{11}}\) and
\(B=z_{01}\overline{z_{10}}\), the phase projections are

\[
 P_{++}H
 =\frac12(\Re A+\Re B-2)
 =-\frac14\bigl(|z_{00}-z_{11}|^2+|z_{01}-z_{10}|^2\bigr),
\]

\[
 P_{--}H=\frac12(\Re A-\Re B)
 =\frac14D_hD_kH.
\]

Thus the exact global identity is

\[
 \boxed{
 \langle W,H\rangle_G
 =\langle P_{++}W,P_{++}H\rangle_G
 +\frac1{16}\langle D_hD_kW,D_hD_kH\rangle_G.}
\]

The blind report's factor \(1/16\) is correct, but its “three parity
complements plus support crossing” description must be replaced by this
single \((++)\) complement.  The remaining complement is not algebraically
zero.  For nonnegative erased-structure weights,
\(P_{++}W\ge0\) while \(P_{++}H\le0\); hence the complement can accumulate
with one sign.  This is a false-control/capacity observation, not a lower
bound for the literal signed coefficient.

## 4. Character and the actual axial bound

On nonzero character support \(p=2s\), and

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s.
\]

This is constant on every fixed-\(p\) fibre, so the report correctly rejects
an alleged cancellation in \(h,k,q\) after \(p\) has been frozen.  It does
alternate when \(s\) itself is summed; this is the character cancellation
used by the accepted Round-115 phase-free lemma.

The axial formulas are also correct:

\[
 p=0:\quad \Delta=\rho=hq,\qquad
 q=0:\quad \Delta=pk,\ \rho=-pk.
\]

They show that \(D_hD_kH=0\) while \(H\) and both far gates can be nonzero,
so they are valid pointwise counterexamples to the naive double-commutator
identity.  They are nevertheless target-safe.  In the persistent critical
block \(h,h'\asymp L\), \(k,k'\asymp K\asymp L\),
\(|a|\ll_\varepsilon X^\varepsilon\), and \(|H|\le2\).  Hence

\[
 \sum_{p=0}G|WH|
 \ll_\varepsilon LK^2X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon,
\]

\[
 \sum_{q=0}G|WH|
 \ll_\varepsilon L^2KX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\]

Their intersection is not double-far.  This agrees with Round 115's
accepted coherent \(p=0\) sector of target-sized \(L^3\) mass.  The report
must remove the true axes from the \(L^4\) obstruction ledger.

There is a distinct correct warning in (3.6).  The terms \(H_{s,0}\) and
\(H_{0,q}\) are evaluated for every original \((s,q)\), not only on
\(q=0\) and \(s=0\).  They are replicated anchored complements, not
geometric axial sectors, and their trivial ledger can still be \(L^4\).

## 5. Abel, gate, prefix, and adversarial controls

The two-dimensional Abel formula (3.8) has the correct corner, edge, and
mixed-interior signs.  The shifts

\[
 \Delta(s+1,q)=\Delta+2(k+q),\quad
 \rho(s+1,q)=\rho-2k,
\]

\[
 \Delta(s,q+1)=\Delta+h+2s,\quad
 \rho(s,q+1)=\rho+h
\]

verify the two gate-difference formulas in (3.9).  The displayed four-term
\(\delta_s\delta_qG\), the product rule (3.10), and zero extension include
every gate and support entry/exit term.

Post-unmask, the assertion that only a trivial prefix estimate is known is
too strong.  Round 115 expands the second gcd mask and uses bounded
\(\chi_4\) partial sums against the literal bounded-variation slanted
amplitude and the two gate intervals.  Adding one prefix endpoint gives,
for fixed \(h,k,q\),

\[
 \sum_{s\le i}b_{s,q}\ll_\varepsilon X^\varepsilon.
\]

After a trivial \(q\)-prefix sum this gives at best
\(|B_{i,j}|\ll_\varepsilon LX^\varepsilon\).  It still does not close
(3.8): the available bounds for
\(\delta_sH,\delta_qH,\delta_s\delta_qH\) are only \(O(1)\), and no accepted
joint estimate prices the two edges, mixed interior, gate jumps, and support
jumps at \(L^3\).  The conclusion “no current Abel proof” survives, but its
ledger must acknowledge the accepted one-direction cancellation.

The constant-character and erased-structure controls remain valid.  The
repaired \((++)\) formula makes their limitation especially explicit: for a
nonnegative constant-character shadow, \(P_{++}H\) is negative
semidefinite pointwise and is not killed by the swap commutator.

The report's complex phase-adapted choice
\(a_x=c_x\overline{z_x}\) also gives, after ordered-pair symmetrization,

\[
 \sum_{x,y:\,\mathrm{df}}c_xc_y
 \bigl[1-\cos(\arg z_x-\arg z_y)\bigr]\ge0.
\]

This correctly refutes methods uniform over arbitrary complex bounded
coefficients.  Post-unmask it must be labelled as outside the real literal
coefficient class; by itself it cannot refute a method that essentially uses
reality.  The nonnegative real \((++)\) shadow above is the relevant control
for the repaired projection identity.  Neither control is a physical lower
bound.

## 6. Fixed-\(Q\) rulings, no-go scope, and owner quarantine

The report's blind-access declaration is consistent.  Its result is
compatible with, but does not independently rederive, the Round-136
fixed-\(Q\) ruling obstruction.  The global zero extension and real
two-projection reduction do not remove those rulings: they remain inside the
\((++)\) and \((--)\) weights with the literal gcd/slanted amplitudes.
Phase-free subtraction also does not delete them.  Because the blind packet
did not expose the divisor-progressive \(Q\)-coordinates, the fixed-\(Q\),
alias-restoration, and gauge-sensitive seams require separate Round-171
evidence.

The exact theorem supported by this report is narrow:

> The complete real zero-subtracted scalar is not its independent
> \(h\)-swap/\(k\)-swap double-commutator term.  It also contains the exact
> \((++)\) complement displayed above.  Coordinate averaging, bounded scalar
> differences, positive norms, and the currently supplied prefix information
> do not estimate that complement and all Abel corrections at
> \(L^3X^\varepsilon\).

This does not exclude a weighted involution, a twisted commutator adapted to
\(\chi_4\), an identity exploiting the gcd/slanted coefficient, or a new
signed two-variable prefix/correlation theorem.  It does not disprove the
literal target.

The owner quarantine is green.  Everything is restricted to the persistent
critical \(j=1\) fixed block.  No remaining BAL label, full BAL, hard TOP,
UNBAL, M9--M2, M1/GAR, endpoint, bridge, quarter theorem, or exponent follows.

## 7. Required repair and recommended state effect

Verdict: **REPAIR**.

Before this report is used as round-closing evidence:

1. replace the restricted support-crossing presentation by the global
   zero-extended identity, or explicitly state that the former is only an
   equivalent bookkeeping choice;
2. use reality to delete the \((+-)\) and \((-+)\) projections and display
   the exact surviving \((++)\) complement;
3. insert the direct \(O_\varepsilon(L^3X^\varepsilon)\) bounds for the
   genuine \(p=0\) and \(q=0\) sectors;
4. distinguish those sectors from the replicated anchored complements in
   (3.6);
5. acknowledge the accepted one-direction Round-115 prefix cancellation and
   state that the missing theorem is joint and two-dimensional; and
6. narrow the no-go to the independent-swap/coefficient-uniform or
   bounded-difference implementation actually falsified.

After repair, retain the exact two-projection identity as a route-specific
obstruction and retain \((171.B1)\) as unresolved.  Do not reject all
commutators or summation-by-parts methods, and make no status or exponent
promotion.

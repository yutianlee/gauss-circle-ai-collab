# Reciprocal-energy attack: corrected symbol and transposed-row survivor

- Campaign: `m9-m2-top-endpoint-near-product-energy`
- Round: 75
- Task: `reciprocal_energy_attack`
- Role: discovery
- Starting graph SHA-256: `b5aa6150a62e1ecc21045c21bcb4af9ede4ab164545b43a93756e53fcc402bd2`
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

The diagonal-scale estimate (75.16) is not proved, and no new polynomial
intermediate \(L\)-range is claimed.  Two exact conclusions and one
correction are obtained.

First, (75.7)--(75.10), with the angular amplitude merely evaluated at
the saddle, is not an exact identity with an
\(O_A(L^{3/2}X^{-A})\) remainder.  If \(A_{\tau}(x,t)\) denotes the
complete angular amplitude and \(t_0=J/(2l)\), the first omitted term in
the Gaussian bracket is

\[
 \frac{\partial_t^2A_{\tau}(x,t_0)}{8\pi i\,xl}.                \tag{1.1}
\]

For the narrowest \(B=\lceil\sqrt L\rceil\) collar,
\(\partial_t^2A_\tau\ll L X^\varepsilon\), while \(xl\asymp LJ\).
Thus (1.1) is \(O(J^{-1}X^\varepsilon)\) on the normalized unit-symbol
scale (pointwise ratios are not asserted where the leading symbol
vanishes).
It is target-safe after absolute summation, but it is not
\(O_A(X^{-A})\).  An all-orders moving symbol repairs the transform to
arbitrary order; retaining only the leading symbol gives instead the
valid aggregate error

\[
 O_\varepsilon(L^{3/2}J^{-1/2}X^\varepsilon).                  \tag{1.2}
\]

Second, independently of that transform, the exact cone has a
character-preserving transposed-row energy reduction.  Regrouping by
\(m\), rather than applying Cauchy in \(h\), leaves the character inside
each row.  Its off-diagonal has the exact sign

\[
 \chi_4(h)\chi_4(h+2r)=(-1)^r.                                \tag{1.3}
\]

The resulting signed even-offset aggregate in (2.4) below is the
smallest exact survivor found in this task.

Third, Parseval for the corrected moving dual symbol is an overlap
identity for all integral translates of narrow \(l\)-spikes, not just an
unshifted \(L^2\)-integral.  Its off-diagonal has the same alternating
offset structure.  The active Poisson frequencies have negative sign,
and the principal B-process return is

\[
 S_{-m}^{(0)}
 =e(-1/8)\sqrt{J/L}\,R_m^{\mathrm{int}}+\text{stationary corrections}.
                                                                    \tag{1.4}
\]

Consequently (75.16), at principal-symbol level, is exactly the
diagonal-scale transposed-row problem.  A second Poisson/B-process loop
is an adjoint self-return, not a new source of cancellation.

## 2. Exact statement and hypotheses

Put \(J=\sqrt X\), \(y=\lfloor J\rfloor\),
\(q_X=X/y^2\), \(H=\lfloor yX^{-1/4}\rfloor\), and let
\(1\leq L\leq H\) be dyadic.  Let \(a(h,m)\) be exactly (75.1), with
the actual \(\eta_L,\Phi,W\), and define

\[
 \mathcal H_m=
 \{h\in\mathbb Z:\ h\text{ odd},\ h\in\operatorname{supp}\eta_L,
                    \ m\leq h\leq4m\},                         \tag{2.1}
\]

\[
 R_m=\sum_{h\in\mathcal H_m}
       \chi_4(h)a(h,m)e(J\sqrt{hm}).                            \tag{2.2}
\]

The ceiling causes no approximation: for integral \(m\),
\(\lceil h/4\rceil\leq m\) is equivalent to \(h\leq4m\).  Hence

\[
 \mathcal T_L=\sum_mR_m,
 \qquad
 |\mathcal T_L|^2\ll L\mathcal E_L^\top,
 \qquad
 \mathcal E_L^\top:=\sum_m|R_m|^2.                            \tag{2.3}
\]

Writing \(h'=h+2r\) gives the exact expansion

\[
 \begin{aligned}
 \mathcal E_L^\top
  ={}&\sum_m\sum_{h\in\mathcal H_m}|a(h,m)|^2\\
   &+2\Re\sum_{r\geq1}(-1)^r
      \sum_m\!\sum_{\substack{h\in\mathcal H_m\\h+2r\in\mathcal H_m}}
       a(h,m)\overline{a(h+2r,m)}\\
   &\hspace{42mm}\times
       e\!\left(J\sqrt m(\sqrt h-\sqrt{h+2r})\right).
                                                               \tag{2.4}
 \end{aligned}
\]

The diagonal is \(O(L^2)\).  Therefore the signed bound

\[
 \Re\sum_{r\geq1}(-1)^r C_r\ll_\varepsilon L^2X^\varepsilon,
                                                               \tag{2.5}
\]

where \(C_r\) is the inner double sum in (2.4), implies
\(\mathcal T_L\ll_\varepsilon L^{3/2}X^\varepsilon\).  Each fixed
\(r\)-shell is individually \(O(L^2)\) absolutely, but there are
\(O(L)\) shells; (2.5) is a genuinely signed union estimate.

For the corrected dual interface, sum the layer symbols before taking
the energy and put

\[
 \mathscr F_j(\lambda)=\sum_\tau F_{\tau,j}(\lambda),
 \qquad
 G(\lambda)=\sum_{j\ {\rm odd}}\chi_4(j)\mathscr F_j(\lambda).
                                                               \tag{2.6}
\]

With the exact Fourier convention in (75.13),
\(S_k=L\widehat G(k)\).  Smooth zero extension and compact support then
give the exact periodized Parseval identity

\[
 \begin{aligned}
 \sum_{k\in\mathbb Z}|S_k|^2
 &=L^2\sum_{n\in\mathbb Z}
      \int_{\mathbb R}G(\lambda)
             \overline{G(\lambda+n)}\,d\lambda\\
 &=L^2\sum_{r\in\mathbb Z}(-1)^r
   \sum_{\substack{j\ {\rm odd}\\j+2r\ {\rm admissible}}}
   \sum_{n\in\mathbb Z}
    \int\mathscr F_j(\lambda)
       \overline{\mathscr F_{j+2r}(\lambda+n)}\,d\lambda .
                                                               \tag{2.7}
 \end{aligned}
\]

Uniform Schwartz bounds for the complete moving symbol imply

\[
 \sum_n\left|\int\mathscr F_j(\lambda)
 \overline{\mathscr F_{j'}(\lambda+n)}d\lambda\right|
 \ll_{A,\varepsilon}\frac{X^\varepsilon}{L}
 \left(1+L\left\|\frac Xj-\frac X{j'}\right\|\right)^{-A}.
                                                               \tag{2.8}
\]

Thus the \(r=0,n=0\) diagonal is \(O_\varepsilon(LJX^\varepsilon)\),
and all other terms in (2.7) are the exact actual-symbol overlap
survivor.  The tails \(|k|>LX^\varepsilon\) are negligible after taking
the Schwartz order large, so the full energy controls (75.16).

## 3. Proof or derivation

The support of \(h\asymp L\) and
\(\lceil h/4\rceil\leq m\leq h\) contains \(O(L)\) possible \(m\)'s.
The equivalence following (2.2) proves
\(\mathcal T_L=\sum_mR_m\), and Cauchy gives (2.3).  Expanding
\(|R_m|^2\), two admissible odd frequencies differ by \(2r\).  Direct
inspection modulo four gives (1.3), and pairing \(r\) with \(-r\)
proves (2.4).  No smoothing, collar insertion, or stationary
approximation is used in this argument, so both moving affine edges and
the exact \(q_X\)-profile remain present.

For (2.7), (75.13) gives

\[
 S_k=L\sum_{j\ {\rm odd}}\chi_4(j)\widehat{\mathscr F_j}(k)
     =L\widehat G(k).
\]

Expanding \(\sum_k|\widehat G(k)|^2\) and applying Poisson to the
difference variable gives

\[
 \sum_k|\widehat G(k)|^2
 =\sum_n\int G(\lambda)\overline{G(\lambda+n)}d\lambda.
\]

Expansion in \(j,j'\), followed by \(j'=j+2r\), gives the second line
of (2.7).  Each \(\mathscr F_j\) is a spike of width \(L^{-1}\), centred
at \(X/j\), because

\[
 \frac d{d\lambda}
 \frac{L(X-j\lambda)}{4\lambda}
 =-\frac{LX}{4\lambda^2}\asymp-L.
\]

Convolution of the two uniform Schwartz envelopes proves (2.8).  It
also proves the \(LJ\) diagonal.  Even granting the natural
\(J^2/L\) absolute near-collision capacity, absolute summation in
(2.7) has size \(J^2X^\varepsilon\), whereas the target is
\(LJX^\varepsilon\); the alternating \((-1)^r\) union must save the
factor \(J/L\).  A fixed \(r\)-shell is target-safe, but summing the
shells absolutely is not.

It remains to justify the correction asserted in Section 1.  After
\(m=xt^2\), write the angular integral on a layer as

\[
 \int A_\tau(x,t_0+v)e(-xlv^2)dv,
 \qquad t_0=\frac J{2l}.
\]

The Gaussian moments in the convention \(e(z)=e^{2\pi iz}\) give

\[
 \begin{aligned}
 \int A_\tau(x,t_0+v)e(-xlv^2)dv
  =\frac{e(-1/8)}{\sqrt{2xl}}
  \left\{A_\tau(x,t_0)
  +\frac{\partial_t^2A_\tau(x,t_0)}{8\pi i\,xl}
  +\cdots\right\}.                                  \tag{3.1}
 \end{aligned}
\]

Indeed, differentiating the zeroth Gaussian moment gives
\(\int v^2e(-xlv^2)dv=(4\pi ixl)^{-1}
\int e(-xlv^2)dv\).  An additive collar of width \(B\) has angular
width \(B/L\), so its \(2q\)-th derivatives cost at most
\((L/B)^{2q}\ll L^q\).  The \(q\)-th Gaussian correction is therefore
\(O(J^{-q}X^\varepsilon)\) in the corresponding normalized symbol
seminorm.
Rapid radial decay gives at most \(O(1)\) effective \(l\)'s for each
\(j\), hence the \(q=1\) correction contributes at most
\(O_\varepsilon(L^{3/2}J^{-1/2}X^\varepsilon)\) after restoring the
factor in (75.7).  Keeping \(N\) correction wavelets leaves
\(O(L^{3/2}J^{1/2-N}X^\varepsilon)\); choosing \(N\) in terms of \(A\)
recovers an arbitrary-order remainder.  This is an all-orders moving
symbol, not the frozen leading wavelet of (75.8).

Finally, the sign and the return constant can be checked without
freezing \(\mathcal K_{\tau,l}\).  For the leading radial symbol, write
\(x=Lz\) before the second Poisson step.  The character comb is

\[
 \sum_{j\in\mathbb Z}\chi_4(j)e(-jx/4)
 =-2i\sum_{h\ {\rm odd}}\chi_4(h)\delta(x-h).         \tag{3.2}
\]

Positive \(k\) has no stationary point.  Put \(k=-m<0\).  After (3.2)
the remaining phase in the \(l\)-integral is
\(hX/(4l)+ml\), with

\[
 l_*={1\over2}\sqrt{hX/m},\qquad
 f(l_*)=\sqrt{Xhm},qquad
 {e(1/8)\over\sqrt{f''(l_*)}}
 ={e(1/8)(hX)^{1/4}\over2m^{3/4}}.                  \tag{3.3}
\]

Multiplication by the comb coefficient gives
\((-2i)e(1/8)/2=e(-1/8)\).  Since the leading radial factor sampled at
\(x=h\) is \(L\eta_L(h)\Phi(h/(H+1))/h\), and

\[
 W(l_*/y)=W\!\left(\sqrt{q_Xh/(4m)}\right),
\]

(3.3) yields exactly the principal term in (1.4).  The omitted terms in
(3.1) and in the second stationary expansion are its adjoint correction
symbols.  Thus the packet's leading energy is an asymptotic return to
the transposed rows; it is not an exact equality for a frozen
\(\mathcal K\).  Full Fourier inversion with the complete symbol returns
to the antecedent instead of producing a new estimate.

## 4. First doubtful or unproved step

The first false step in the proposed route is the claim that evaluating
the angular amplitude at \(t_0\) leaves an arbitrary-order error.  The
explicit nonzero correction (1.1) occurs before the reciprocal-energy
estimate.  It is harmless at the cone target but must be included in the
moving symbol, or recorded as the weaker error (1.2).

After that repair, the first unproved analytic step is either of the
equivalent signed aggregates

\[
 \Re\sum_{r\geq1}(-1)^rC_r\ll_\varepsilon L^2X^\varepsilon           \tag{4.1}
\]

or

\[
 L^2\Re\sum_{r\ne0}(-1)^r
 \sum_{j,n}\int\mathscr F_j(\lambda)
       \overline{\mathscr F_{j+2r}(\lambda+n)}d\lambda
 \ll_\varepsilon LJX^\varepsilon.                                \tag{4.2}
\]

No argument in the permitted packet controls the complete alternating
\(r\)-union.  Fixed-offset estimates, exact-product divisor bounds, and
the \(J^2/L\) absolute near-collision ledger do not imply (4.1) or
(4.2).  A second Poisson or B-process merely produces the adjoint return
(1.4).  This is the first genuinely open step.

## 5. Control tests and outcomes

1. **External normalization and conjugate ownership -- pass.**  The
   accepted top transform contributes
   \(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\) once; the negative frequency is
   the conjugate.  The correction changes the symbol, not this leading
   physical normalization.
2. **Hard and flat boundary collars -- pass for the exact replacement;
   revise for (75.7).**  Equations (2.1)--(2.4) retain both boundaries
   exactly.  In the transform route the two \(2B\)-strips remain
   absolutely target-safe, but derivatives of their complementary
   collars cause the \(J^{-1}\) correction (1.1).
3. **Actual \(q_X\) and layer ownership -- pass.**  The direct rows keep
   \(W(\sqrt{q_Xh/(4m)})\).  The all-orders repair sums the one-count
   layers before Parseval; no fixed angular cutoff replaces an additive
   collar.
4. **Quarter shift, odd dual index, Gaussian constant, and Jacobian --
   pass after correction.**  Equations (3.1)--(3.3) give both Gaussian
   units and the return constant \(e(-1/8)\).  The character comb is
   supported on the two odd quarter lattices.
5. **Complete moving \(l\)-symbol -- fail for the frozen formula; repaired
   asymptotically.**  The symbol must include every even angular
   derivative in (3.1).  Its first omitted term is (1.1).
6. **Aliases, layers, and localization -- pass only in the corrected
   interface.**  The \(O(\log L)\) layers are summed before the energy,
   and (2.7) retains every integer translate \(n\).  Leading-only
   localization has error (1.2), not the error asserted in (75.7).
7. **Poisson measure -- pass.**  The exact normalization is
   \(S_k=L\widehat G(k)\); discrete Parseval is the periodized overlap
   formula (2.7).  Replacing it by \(L^2\int|G|^2\) would omit aliases.
8. **Tail and diagonal -- pass.**  Uniform Schwartz bounds make
   \(|k|>LX^\varepsilon\) negligible.  Spike width \(L^{-1}\) gives the
   diagonal \(L^2\cdot J\cdot L^{-1}=LJ\).
9. **Signed off-diagonal -- open and isolated.**  Its exact sign is
   \((-1)^r\) in both (2.4) and (2.7).  Taking absolute values has
   capacity \(J^2\), rather than \(LJ\), on the dual side.
10. **Character self-return -- pass as a no-go.**  Both terms of the comb
    (3.2) are necessary.  The active sign is \(k<0\), and (1.4) returns
    to the character-bearing transposed rows.  It supplies no saving.
11. **Perfect powers, exact products, and adversarial coefficients --
    pass as controls, not estimates.**  The packet's
    \(O_\varepsilon(L^{1+\varepsilon})\) primal exact-square capacity,
    divisor-bounded \(jl=X\) fibers, and fourth-power anti-diagonal all
    remain subtarget.  They do not control the signed union.  Arbitrary
    \(b_{\tau,j,k}\) can phase-conjugate an \(S_k\); (2.7) is valid and
    potentially useful only with the actual coupled moving symbol.
12. **Downstream scope -- pass.**  The result proves neither (4.1),
    (4.2), the top cone, full \(M2\), \(M9\), endpoint uniformity, nor the
    Gauss-circle exponent.  Bounded and epsilon-trivial \(L\), and the
    inherited terminal slice, remain the only closed ranges.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/briefs/reciprocal_energy_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reports/m2_affine_cone_attack.md`
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`

No sibling Round-75 report, proof draft, external source, or
computational artifact was used.

## 7. Recommended state effect

**Revise and retain; do not promote the reciprocal-energy estimate or
the cone bound.**  Replace the claimed exact frozen-wavelet identity
(75.7)--(75.10) by an all-orders moving-symbol expansion, or retain only
its leading term with the target-safe error (1.2).  Record (2.7)--(2.8)
as the corrected actual-symbol overlap interface.

After independent seam review, promote the purely algebraic
transposed-row reduction (2.1)--(2.5) as a scoped internal reduction.  It
is exact, preserves \(\chi_4\), includes the hard affine boundaries, and
isolates the alternating even-offset survivor.  Also record the no-go
that the reciprocal energy's principal B-process is the adjoint return
(1.4), so iteration alone cannot prove the missing bound.  Keep
`M9-M2-top-endpoint-signed-cone`, `M9-M2-sign-preserving-poisson-voronoi-route`,
`M9-M2`, `M9`, endpoint uniformity, and the global exponent open.

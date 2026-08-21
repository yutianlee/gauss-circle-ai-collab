# Blind fixed-q rederivation

## 1. Result

**No-go result, with the maximal statement-only consequence.**  The
displayed reciprocal geometry can be derived exactly, but the claimed
uniform estimate

\[
 |F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}
\]

does not follow from the statement-only packet.  The first missing
actual-symbol input is a definition and norm bound for
\(A^\circ_{ga,g(a+2q)}\); moreover, the packet gives only a verbal, not
an algebraic, definition of the weighted mode/lift sum \(F_a(q)\).

There is also no uncancelled reciprocal curvature in the complete
carrier-weighted centered integral.  If

\[
 C_{a,q,k}(g):=e\!\left(-{g\Lambda_{a,q}\over2k}\right)
                 \mathfrak B^\circ_{a,q,k}(g),
\]

then the reciprocal phase in the carrier cancels the reciprocal phase
created by completing the square, and \(C_{a,q,k}(g)\) is an ordinary
integer Fourier sample.  The sharp coefficient-free conclusion is the
periodized Fourier-energy estimate in Section 2, expressed in terms of
the still-unknown \(L^2\) mass of the literal amplitude.

Conditionally, if the displayed pointwise estimate for the actual
\(F\) is supplied by some separate actual-symbol lemma, then

\[
 \sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {D L^4\over A},
 \qquad
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon {H^2D L^4\over A}.
\]

This misses the required hard-block target by the factor \(D^2\).
Thus pointwise control without signed \(q\)-correlation reaches the
target only for \(D=X^{o(1)}\) (in particular fixed or
polylogarithmic \(D\)); it reaches no range \(D=X^\theta\) with fixed
\(\theta>0\).

## 2. Exact statement and hypotheses

Use only the hypotheses in the packet, and set

\[
 r=\sqrt{b/a}\in(1,2),\qquad
 T=a-{b\over4}={4a-b\over4}>0,
\]

\[
 \kappa_-={J\delta_{a,q}\over2\sqrt a},\qquad
 \kappa_+={J\delta_{a,q}\over\sqrt b},\qquad
 \mathcal K_{a,q}=\mathbb Z\cap(\kappa_-,\kappa_+),
 \qquad N_{a,q}=\#\mathcal K_{a,q}.
\]

Then

\[
 \delta_{a,q}=\sqrt a\,(r-1)={2q\over\sqrt a+\sqrt b},
 \qquad
 \Lambda_{a,q}={2J^2q^2\over a(r+1)^2}
 \asymp {J^2D^2\over A},
\]

\[
 \kappa_-={Jq\over a(r+1)},\qquad
 \kappa_+={2Jq\over ar(r+1)},
 \qquad \kappa_\pm\asymp {JD\over A}=K,
\]

but the **number of sampled \(k\)'s is governed by the short shell**:

\[
 \kappa_+-\kappa_-
 ={J(r-1)(2-r)\over2r}
 ={4JqT\over a^2r(r+1)(r+2)}
 \asymp {JD\,T\over A^2},
\]

\[
 N_{a,q}=\left\lceil\kappa_+\right\rceil
          -\left\lfloor\kappa_-\right\rfloor-1,
 \qquad
 \max(0,|I_{a,q}|-1)\le N_{a,q}\le |I_{a,q}|+1.
\]

Since \(b-a\ge2\), \(4a-b\ge1\), and their product is minimized at
one of the two discrete endpoints,

\[
 q(4a-b)\ge a,
 \qquad |I_{a,q}|\ge {J\over24a}.
\]

Consequently, if the odd lift set is nonempty, then
\(g\asymp G=L/A\) forces \(A\ll L\le J^{1/2}\), and the uncollared
\(k\)-fibre is nonempty (indeed large) for asymptotic \(J\).  The exact
ceiling/floor formula is still required for small parameters, empty
lift/mask fibres, and collared shells.

For \(k\in\mathcal K_{a,q}\), put

\[
 u_k=\left({J\delta_{a,q}\over2k}\right)^2
     ={\Lambda_{a,q}\over2k^2}.
\]

The map \(k\mapsto u_k\) is decreasing and maps the open real interval
\((\kappa_-,\kappa_+)\) exactly onto \((b/4,a)\), with

\[
 {du_k\over dk}=-{\Lambda_{a,q}\over k^3}
 \asymp-{A^2\over JD}.
\]

For a fixed permitted odd lift \(g\), let

\[
 V_g=(gb/4,ga),\qquad W_g=|V_g|=gT,
\]

and, whenever the displayed literal amplitude is in \(L^2(V_g)\), set

\[
 f_g(v)=\mathbf 1_{V_g}(v)A^\circ_{ga,gb}(v)
        e\!\left(-J\delta_{a,q}\sqrt{gv}\right),
\]

\[
 P_g(x)=\sum_{m\in\mathbb Z}f_g(x+m),\qquad 0\le x<1.
\]

The exact Fourier and energy conclusions are

\[
 C_{a,q,k}(g)=\int_{V_g}f_g(v)e(kv)\,dv
             =\int_0^1P_g(x)e(kx)\,dx,
\]

\[
 |\mathfrak B^\circ_{a,q,k}(g)|=|C_{a,q,k}(g)|
 \le \int_{V_g}|A^\circ_{ga,gb}(v)|\,dv,
\]

\[
 \sum_{k\in\mathcal K_{a,q}}|C_{a,q,k}(g)|^2
 \le \int_0^1|P_g(x)|^2\,dx
 \le \lceil W_g\rceil\int_{V_g}|A^\circ_{ga,gb}(v)|^2\,dv,
\]

and hence

\[
 \left|\sum_{k\in\mathcal K_{a,q}}C_{a,q,k}(g)\right|^2
 \le N_{a,q}\lceil gT\rceil
       \int_{gb/4}^{ga}|A^\circ_{ga,gb}(v)|^2\,dv. \tag{2.1}
\]

Thus, on a generic shell \(T\asymp A\), the coefficient-free factor in
(2.1) is \(\ll KL\); on a short shell it is instead

\[
 \ll
 \left(1+{JD\,T\over A^2}\right)
 \left(1+{L T\over A}\right).
\]

No bound purely in \(A,D,J,L\) follows until the literal amplitude and
all weights used to assemble \(F_a(q)\) are specified.

## 3. Proof or derivation

The identities for \(\delta,\Lambda,\kappa_\pm\) follow from
\(b=ar^2=a+2q\).  The width identity follows by combining

\[
 q={a(r-1)(r+1)\over2},\qquad
 T={a(2-r)(2+r)\over4}.
\]

The exact integer count uses the openness of both endpoints.  Also,
\(u_{\kappa_-}=a\), \(u_{\kappa_+}=b/4\), and differentiation gives
the reciprocal sample spacing.  More exactly,

\[
 u_k-u_{k+1}
 ={\Lambda_{a,q}(2k+1)\over2k^2(k+1)^2}
 \asymp {A^2\over JD}.
\]

The complete curvature ledger is obtained before estimating anything:

\[
 gk\left(\sqrt u-{J\delta_{a,q}\over2k}\right)^2
 =gku-gJ\delta_{a,q}\sqrt u+{g\Lambda_{a,q}\over2k}. \tag{3.1}
\]

Write

\[
 \phi_-(k)=-{g\Lambda_{a,q}\over2k},\qquad
 \phi_+(k)=+{g\Lambda_{a,q}\over2k}.
\]

For every \(j\ge1\), their derivatives have opposite signs and equal
magnitudes,

\[
 |\phi_\pm^{(j)}(k)|
 ={g\Lambda_{a,q}\over2}{j!\over k^{j+1}}
 \asymp_j L\left({A\over JD}\right)^{j-1}.
\]

In particular,

\[
 |\phi_\pm''(k)|\asymp {AL\over JD}
 =\left({AD\over L\sqrt\rho}\right)^2,
 \qquad
 |\phi_\pm'''(k)|\asymp {A^2L\over J^2D^2}.
\]

Taken alone, \(\phi_-\) has derivative

\[
 \phi_-'(k)={g\Lambda_{a,q}\over2k^2}=g u_k,
\]

whose exact image is \((gb/4,ga)\).  A formal Fourier mode
\(m\in(gb/4,ga)\) would have stationary point

\[
 k_m=\sqrt{g\Lambda_{a,q}\over2m},\qquad
 |\phi_-''(k_m)|={2m\over k_m}\asymp {AL\over JD},
\]

and reciprocal stationary width \(\asymp\sqrt{JD/(AL)}\).  This is only
the carrier ledger.  Equation (3.1) shows that \(\phi_+\), already
inside the complete centered integral, cancels \(\phi_-\) to every
derivative order.  After the change of variables \(v=gu\),

\[
 e(\phi_-(k))\mathfrak B^\circ_{a,q,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(v)
   e\!\left(kv-J\delta_{a,q}\sqrt{gv}\right)\,dv, \tag{3.2}
\]

so the remaining \(k\)-phase is linear.  Any van der Corput gain based
on \(|\phi_-''|\) while treating \(\mathfrak B^\circ\) as an unrelated
bounded coefficient double-counts the completion-of-square phase.

Periodizing the integrand in (3.2) gives the first Fourier identity in
Section 2 because \(e(km)=1\) for integral \(k,m\).  Parseval gives the
first energy inequality.  At each \(x\), at most \(\lceil W_g\rceil\)
translates \(x+m\) lie in the open interval \(V_g\), so Cauchy--Schwarz
gives the second energy inequality.  A final Cauchy--Schwarz over the
\(N_{a,q}\) sampled frequencies proves (2.1).

For the conditional row consequence, the dyadic block contains
\(O(AD)\) possible pairs \((a,q)\), irrespective of the parity and
coprimality deletions.  Squaring the assumed pointwise estimate and
renaming \(2\varepsilon\) as \(\varepsilon\) gives

\[
 E_F:=\sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}. \tag{3.3}
\]

With the stated zero extension, Cauchy--Schwarz and a change of index
give

\[
 \begin{aligned}
 \mathcal G_H^{\rm act}
 &\le H\sum_{a,n}\sum_{0\le h<H}|F_a(n+h)|^2\\
 &=H^2\sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {H^2DL^4\over A}. \tag{3.4}
 \end{aligned}
\]

The ratio of (3.4) to the target is exactly \(D^2\).  If
\(D=X^{o(1)}\), this ratio can be absorbed after reserving part of the
arbitrary \(X^\varepsilon\) loss.  If \(D=X^\theta\), \(\theta>0\), the
unabsorbed ratio is \(X^{2\theta}\).  Coherent arrays such as
\(F_a(q)=(-1)^qL^2/A\) saturate the scale in (3.4), so no stronger Gram
bound is a consequence of pointwise size alone.

## 4. First doubtful or unproved step

The first missing input occurs inside the first displayed integral:
the packet supplies no formula, support regularity, normalization, or
\(L^1/L^2\) estimate for
\(A^\circ_{ga,g(a+2q)}(v)\).  Consequently even one summand has no
parameter-only upper bound.  Multiplying a nonzero admissible-looking
integrand by an arbitrary scalar preserves every displayed geometric
hypothesis while multiplying the integral by that scalar; the packet
contains no hypothesis that rules this out.

Even after an amplitude norm were supplied, proving the stated estimate
for \(F_a(q)\) would require the exact algebraic summation formula:
weights, cardinalities, signs, primitive/prior-owner masks, profile and
floor/star conventions, orientations, collars, entry/exit terms, and
the placement of the carrier.  These are named but not defined.  The
first unjustified step in any proof of the pointwise bound from this
packet would therefore be inserting an unstated actual-symbol norm (or
replacing the literal coefficient by an arbitrary bounded one).  The
status of the pointwise estimate is **undetermined**, not proved and not
disproved for the intended external definition.

## 5. Required control tests and outcomes

The tests below are algebraic; no numerical experiment is being used as
proof.

| Control | Exact input | Expected failure or invariant | Observed result | Implication |
|---|---|---|---|---|
| Empty fibres | \(\mathcal K_{a,q}=\mathbb Z\cap(\kappa_-,\kappa_+)\), the odd lift set, masks, and collars | A central scale \(K\) must not be mistaken for a cardinality | Exactly \(N=\lceil\kappa_+\rceil-\lfloor\kappa_-\rfloor-1\).  Discreteness gives \(|I|\ge J/(24a)\), so a live uncollared odd lift (which forces \(A\ll L\le\sqrt J\)) has many \(k\)'s asymptotically.  An empty lift/mask set or a collar deleting the physical shell still gives a zero fibre | Empty fibres contribute zero, but nonemptiness may be used only after the displayed lower-bound check, never from \(K\) alone |
| Endpoint equality | Integral \(k\)-endpoint equality, and formal carrier modes \(m\in(gb/4,ga)\) | Open endpoints must not be counted as interior stationary points | Integral \(k=\kappa_\pm\) is excluded.  In the dual ledger \(ga\in\mathbb Z\) is always the upper endpoint stationary mode, whereas \(gb/4\notin\mathbb Z\) for odd \(g,b\) | Endpoint terms require their own treatment; an interior stationary-phase formula is not uniform there |
| Fixed physical collars | Remove fixed \(u\)-widths from the shell of length \(T\) | A fixed collar need not remove only \(O(1)\) sampled \(k\)'s | Since \(|dk/du|\asymp JD/A^2\), a collar of width \(c\) changes the sample count by \(\asymp cJD/A^2\); if \(T=O(1)\), it can empty the shell | Exact collar locations and entry/exit terms are indispensable |
| \(G\asymp1\) | An odd lift set with \(g\asymp1\) | No averaging or large-mode asymptotic in \(g\) is available | There are only \(O(1)\) lifts and \(W_g=gT\) may be \(O(1)\); the bound (2.1) remains valid with ceilings | Any gain requiring many lifts or many density modes fails this control |
| Pell or near-square rows | \(ab=m^2+\nu\) with small \(|\nu|\), including \(\nu=0\) | Irrationality of \(\sqrt{ab}\) must not be assumed uniformly | \(\Lambda=J^2(a+q-m)-J^2\nu/(\sqrt{ab}+m)\).  If \(\nu=0\), coprimality forces \(a,b\) separately to be squares; for small \(\nu\) no modular phase separation follows from the packet | Reciprocal cancellation cannot be justified by generic Diophantine behaviour |
| Fourth powers | \(a=s^4,b=t^4\), coprime odd \(s,t\), \(1<t/s<\sqrt2\) | Exact algebraic resonance and endpoint equality must remain allowed | \(\delta=t^2-s^2\) is integral and \(\Lambda=J^2(t^2-s^2)^2/2\).  Taking \(J\) a sufficiently large common multiple of \(2s^2t^2\) makes both \(\kappa_\pm\) integral while preserving \(L\le J^{1/2}\); the open interval still excludes them | No uniform proof may assume nonintegral endpoints or an irrational carrier |
| Density/discrepancy modes | Periodization \(P_g(x)=\sum_m f_g(x+m)\) and the packet's verbally named mode sums | Mode counts and cross terms must be explicit | A physical support of length \(gT\) has up to \(\lceil gT\rceil\) aliases; \(\int|P_g|^2\) contains their cross terms.  The additional metric/discrepancy mode weights are absent | Parseval alone does not bound the full \(F\); exact mode orthogonality or weighted norms are required |
| Arbitrary phase-conjugated coefficient | Replace a centered coefficient by \(c_k=e(+g\Lambda/(2k))\), or choose \(F_a(q)=(-1)^qM\) | A proof using only the visible carrier curvature should fail | The first choice cancels the carrier exactly and makes a \(k\)-sum coherent; the literal centered integral itself contains precisely this conjugate reciprocal factor.  The second choice makes the alternating \(q\)-sum have size \(HM\) | Curvature of the carrier and pointwise size alone cannot yield either sampled-\(k\) or signed-\(q\) cancellation |
| Fixed/polylogarithmic versus polynomial \(D\) | Compare (3.4) with the target | The exact loss should be quantified | Loss \(D^2\): it is absorbable for \(D=X^{o(1)}\), but equals \(X^{2\theta}\) for \(D=X^\theta\) | The largest epsilon-convention range without signed correlation is subpolynomial \(D\) |
| `raw-vs-weighted` | Raw counts versus the unspecified literal weights and lift multiplicities in \(F\) | No raw exponent may transfer without a coefficient sum | The packet provides no coefficient ledger, and this report makes no such transfer | The pointwise theorem cannot be promoted from a weight-blind count |
| `signed-vs-unsigned` | True external factor \((-1)^h\), absolute values, random signs, and the coherent adversary \(F(q)=(-1)^qM\) | Only an actual structural signed identity could improve (3.4) | Cauchy gives the same upper scale for all variants, while the coherent adversary saturates it; the internal \(\chi_4\)-type data are not supplied | A signed \(q\)-correlation lemma must identify structure absent from the packet |
| `known-lower-bound-families` | UNC, TS, and W-1 controls named in `state/control_models.md` | Any unsigned near-collision claim must be audited against them | Their statements, parity ranges, and coefficient envelopes are not in the permitted statement-only inputs; no unsigned near-collision claim is made here | This isolation cannot certify any lemma that would require those audits |
| `dyadic-endpoints` | \(D=X^{1/4},X^{3/8},X^{1/2}\) | A subendpoint argument must not hide a power loss | The respective target losses \(D^2\) are \(X^{1/2},X^{3/4},X\) | None of the three polynomial endpoints follows from pointwise control alone |
| `real-vs-complex-pairing` | Real or complex \(A^\circ,F\), symmetric or asymmetric weights | No \(\operatorname{Re}\) shortcut is allowed without conjugacy | (2.1), (3.3), and (3.4) use modulus, Parseval, and Cauchy only, hence are valid for complex data; no pairing identity is asserted | The no-go survives every pairing variant, while any stronger claim still needs the actual symmetry ledger |
| `exact-vs-near-resonance` | Exact square/fourth-power rows and \(ab=m^2+\nu\) with small nonzero \(\nu\) | Exact and near resonance must stay separate | Exact rows can have integral endpoints and rational carriers; near rows have only the displayed correction \(-J^2\nu/(\sqrt{ab}+m)\), with no supplied lower bound modulo one | Exact energy cannot be extended to near bands from this packet |
| `coefficient-adversary` | Same-magnitude coefficients with phases conjugating the carrier and/or the external alternation | A coefficient-robust curvature proof should fail | Both cancellations can be flattened coherently as described above | Any valid stronger result must use the fixed literal profile and sign structure |
| `support-and-degeneracy` | Open sharp shell, possible smooth/collared variants, \(u=b/4,a\), common lift \(g\), masks, and zero extension | Boundary, repeated-lift, and ownership cases must be explicit | The displayed shell has \(u>0\), and the open endpoints and zero extension are handled above.  Smooth collars, repeated-denominator ownership, and primitive/prior-owner masks are not defined | The exact geometry is retained, but no full-coefficient estimate is certified |

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read and used:

- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/briefs/blind_fixed_q_rederivation.md`;
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/blind_statement.md`;
- `problems/gauss_circle.md`;
- `state/control_models.md`.

No proof graph, proof draft, strategy file, claimant/reviewer report,
earlier derivation, web source, or computation was used.  The derivation
is entirely algebraic.  Equations (2.1)--(3.4) depend only on the packet
plus the explicitly stated conditional assumption
\(A^\circ_{ga,gb}\in L^2(V_g)\) where Parseval is invoked.

## 7. Recommended state effect

**Retain** the exact reciprocal map, short-shell sample count, Fourier
periodization bound, and full curvature-cancellation ledger as
statement-local evidence.  **Reject promotion** of the uniform
\(|F_a(q)|\) estimate and of the hard-block Gram target from this packet;
their status should remain unchanged until the literal amplitude norm,
the complete algebraic formula for \(F\), and a signed \(q\)-correlation
mechanism are supplied and audited.  No shared state change is made by
this report.

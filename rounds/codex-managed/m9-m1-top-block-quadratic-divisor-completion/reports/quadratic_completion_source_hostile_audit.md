# Round 59 independent quadratic-completion source/hostile audit

## 1. Result

The finite additive projector is exact, and an interior one-dimensional
B-process produces the reciprocal phase \(Xh/r\) with the expected
\(\chi _4(r)\) and normalized size \(R^{-1/2}\) when
\(X\asymp R^4,\ h\asymp R,\ r\asymp R^2\).  After the shear
\(r=4Kh+s\), however, the exact Hessian calculation does not have an
anisotropic \(R,R^{-1}\) spectrum: a cancellation in the \(hh\) entry
leaves all non-small entries of order one and
\(\det \nabla ^2\Phi=-X^2/r^4\asymp-1\).  Nonzero Hessian determinant
alone cannot imply lattice cancellation; the exact lattice phase \(uv\)
is a strict counterexample.

The saddle identity does return the dual phase and scales to the already
accepted terminal M1 reciprocal block, but it does not return its
coefficient class.  A short radial interval becomes an \(h\)-dependent
strip in \(r\), whereas the accepted terminal theorem has a separable
frequency BV coefficient and an \(h\)-independent denominator weight.
The actual profiles, hard edges, floor branches, and stars have not been
shown to admit a lossless decomposition into that class.  Consequently
this is a phase-level Hardy/M1 return, not a new closure of the full
high shell.

No primary theorem located in the audited literature applies to the
actual character-weighted, sharply truncated, moving reciprocal strip
with the required raw \(O_\varepsilon(RX^\varepsilon)\) bound.  The
narrow lawful conclusion is therefore: retain the projector, saddle,
normalization, and exact Hessian identities as infrastructure; reject a
Hessian-only completion and do not promote the high-shell estimate.

## 2. Exact statement and hypotheses

Let \(e(t)=\exp(2\pi i t)\), let \(\chi _4\) be extended by zero on even
integers, and let
\[
 g_h(n)=\mathbf 1_{h\mid n}\chi _4(n/h).
\]
For every pair of integers \(h\ge1,n\),
\[
 g_h(n)=-{i\over2h}\sum_{a\bmod 4h}\chi _4(a)e(an/(4h)).
 \tag{59.H1}
\]
This identity is pointwise and requires no smoothing.

For a fixed \(h,a\), put
\[
 f_{h,a}(n)=\sqrt{Xn}+{an\over4h},\qquad r=4hk-a.
\]
On an interval whose amplitude is sufficiently smooth, whose stationary
point is uniformly separated from both endpoints and all symbol seams,
and for a dual integer \(k\) for which \(r>0\), the stationary point and
Legendre phase are
\[
 n_*={4Xh^2\over r^2},\qquad
 f_{h,a}(n_*)-kn_*={Xh\over r}.
 \tag{59.H2}
\]
For a negative-curvature interior saddle, the leading normalized term
after (59.H1) is
\[
 2\sqrt2\,i\,e(-1/8)\,
 \chi _4(r){X^{1/2}h^{1/2}\over r^{3/2}}
 e(Xh/r),
 \tag{59.H3}
\]
multiplied by the original amplitude evaluated at \(n_*\).  Formula
(59.H3) is not asserted at endpoint saddles or across a hard/profile
seam.

In a shear cell \(r=4Kh+s\), define
\[
 \Phi_K(h,s)={Xh\over4Kh+s}.
\]
Then, exactly,
\[
\begin{aligned}
 \Phi_{hh}&=-{8KXs\over(4Kh+s)^3},\\
 \Phi_{hs}&={X(4Kh-s)\over(4Kh+s)^3},\\
 \Phi_{ss}&={2Xh\over(4Kh+s)^3},\\
 \det\nabla^2\Phi_K&=-{X^2\over(4Kh+s)^4}.
\end{aligned}
\tag{59.H4}
\]
Thus, under the Round-59 critical scaling
\[
 X\asymp R^4,\quad h,K,s\asymp R,\quad r\asymp R^2,
 \tag{59.H5}
\]
the entries have sizes \(1,1,R^{-1}\), the determinant has size one,
and the two eigenvalues have opposite signs and sizes comparable to one.
At \(s=0\), \(\Phi_{hh}=0\), but the mixed entry remains comparable to
one and the same conclusion holds.  These statements assume
\(4Kh+s\asymp R^2\), away from the pole.

The estimate needed after (59.H3) is a raw bound
\[
 \sum_{\substack{h\asymp R\\r=4Kh+s,\ |s|\ll R}}
 \chi _4(r)\,A_X(h,r)\,e(Xh/r)
 \ll_\varepsilon RX^\varepsilon
 \tag{59.H6}
\]
for the actual transformed symbol \(A_X\), including its moving
stationary selector, every inherited profile/floor edge, and all endpoint
stars.  Since the prefactor in (59.H3) is \(R^{-1/2}\), (59.H6) is
exactly the required \(O_\varepsilon(\sqrt R\,X^\varepsilon)\) primal
scale.

## 3. Proof and derivation

Splitting \(a=\rho+4b\), with \(\rho\in\{1,3\}\) and \(b\bmod h\),
gives
\[
\begin{aligned}
\sum_{a\bmod4h}\chi _4(a)e(an/(4h))
&=\sum_{\rho=1,3}\chi _4(\rho)e(\rho n/(4h))
  \sum_{b\bmod h}e(bn/h)\\
&=h\mathbf1_{h\mid n}
 \{e((n/h)/4)-e(3(n/h)/4)\}\\
&=2ih\,\mathbf1_{h\mid n}\chi _4(n/h).
\end{aligned}
\]
This proves (59.H1), including the vanishing when \(n/h\) is even.

Poisson in \(n\) introduces \(f_{h,a}(n)-kn\).  Its derivative is
\[
 {\sqrt X\over2\sqrt n}-{r\over4h},
\]
which yields (59.H2).  Also
\[
 f''_{h,a}(n)=-{\sqrt X\over4n^{3/2}},\qquad
 |f''_{h,a}(n_*)|^{-1/2}
 ={2n_*^{3/4}\over X^{1/4}}
 ={4\sqrt2\,X^{1/2}h^{3/2}\over r^{3/2}}.
\]
Negative curvature contributes \(e(-1/8)\).  The congruence
\(a\equiv-r\pmod{4h}\) gives
\(\chi _4(a)=-\chi _4(r)\); multiplication by
\(-i/(2h)\) proves (59.H3).  At the critical scale its magnitude is
\[
 X^{1/2}h^{1/2}r^{-3/2}\asymp R^{-1/2}.
\]

Differentiating \(Xh/(4Kh+s)\) after the shear, rather than before it,
gives
\[
 \Phi_h={Xs\over r^2},\qquad \Phi_s=-{Xh\over r^2}.
\]
A second differentiation gives (59.H4).  In particular the two apparent
order-\(R\) pieces in \(\Phi_{hh}\) cancel.  Substitution of (59.H5)
then gives the scale ledger stated above.  Since the determinant is
negative, the real Hessian is nonsingular and indefinite, but this is
only a real-variable curvature fact.

Indeed, the blanket lattice implication
\[
 |\det\nabla^2Q|\asymp1
 \quad\Longrightarrow\quad
 \sum_{u,v\asymp R}e(Q(u,v))\ll R
\]
is false: \(Q(u,v)=uv\) has Hessian determinant \(-1\), while
\(e(uv)=1\) on \(\mathbb Z^2\), so the sum has size comparable to
\(R^2\).  Thus a proof of (59.H6) must use modulo-one arithmetic of the
actual reciprocal phase and the \(\chi _4\) coefficient, not merely
(59.H4).

The exact saddle relation can also be written
\[
 2h\sqrt{X/n_*}=r.
 \tag{59.H7}
\]
It places \(h\asymp R=X^{1/4}\) and
\(r\asymp R^2=\sqrt X\), and (59.H2) is precisely the reciprocal phase
\(hX/r\) in the accepted terminal M1 block with \(L=h\) and \(D=r\).
The accepted terminal theorem bounds a separable expression with a
one-variable coefficient \(u_L(h)\) satisfying
\(\|u_L\|_\infty+\sum|\Delta u_L|\ll1/L\), and a bounded
\(h\)-independent denominator profile \(w_D(r)\), by
\(O_\varepsilon(X^\varepsilon(1+D/L))=O_\varepsilon(RX^\varepsilon)\).

But the saddle selector for a short radial window \(J=[A,B]\) is
\[
 A\le {4Xh^2\over r^2}\le B,
 \qquad\text{equivalently}\qquad
 2h\sqrt{X/B}\le r\le2h\sqrt{X/A}.
 \tag{59.H8}
\]
This is a moving strip of \(r\)-length \(O(R)\) inside a shell of
radius \(R^2\), and its boundaries depend on \(h\).  The remaining actual
symbol is also evaluated at \(n_*(h,r)\).  Therefore (59.H8) is not the
coefficient class of the accepted terminal theorem.  The identity
(59.H7) proves a return of the phase and scale only.  It neither proves
an exact one-count equality with that terminal block nor controls the
new moving boundaries.

## 4. First doubtful or unproved step

The first unproved step is the replacement of the sharp, actual
\(n\)-sum by the interior saddle main term uniformly in \((h,a,k)\).
The packet has not supplied a partition on which the amplitude has the
smoothness required by a B-process while preserving all floors, hard
edges, and profile stars.  If a saddle lands on \(A\), \(B\), or an
internal symbol seam, the stationary contribution has an endpoint
half-weight; if two starred selectors collide, the resulting weight
cannot be guessed by copying a single star.  Nonstationary and endpoint
errors must be summed over \(h\), not estimated as an isolated
\(O(1)\) per transform.

Even granting an exact B-process ledger, the next unproved step is
(59.H6).  A nonzero real Hessian determinant supplies no modulo-one
spacing.  Conversely, the exact phase match to terminal M1 does not
verify separability: the indicator (59.H8), the pulled-back actual
profile, and its one-count/star convention depend jointly on \(h,r\).
An Abel or bounded-variation reduction would need an explicit uniform
decomposition whose total variation costs no more than
\(X^\varepsilon\); none is presently proved.

The fourth-power regime is especially unsuitable for a coefficient-free
argument.  If \(X=L^4\) and \(n=L^2+t\), then
\[
 \sqrt{Xn}
 =L^3+{L\over2}t-{t^2\over8L}
  +O(t^3/L^3).
\]
The linear term is integral or half-integral according to the parity of
\(L\), and the quadratic term is on the critical length-\(L\) Gauss
scale.  This does not by itself disprove the desired square-root bound,
but it proves that rational phase and \(\chi _4\) interactions must be
audited; curvature size alone is not a proof.

## 5. Required control tests and outcomes

| Control | Required check | Outcome |
|---|---|---|
| Projector normalization | Test divisibility, odd quotient, even quotient, and the sign of \(-i/(2h)\). | Passed exactly by the residue-class calculation proving (59.H1). |
| Stationary normalization | Recompute \(n_*\), Legendre phase, curvature factor, Maslov phase, and character sign. | Passed for an interior smooth saddle.  The exact magnitude before the projector is \(4\sqrt2 X^{1/2}h^{3/2}r^{-3/2}\), giving (59.H3). |
| Product range and names | Keep primal radial \(n\), original divisor \(h\), projector residue \(a\), Poisson frequency \(k\), dual odd variable \(r=4hk-a\), cell slope \(K\), and offset \(s=r-4Kh\) distinct. | Passed.  The critical range is \(n\asymp R^2,\ h\asymp R,\ r\asymp R^2,\ |s|\ll R\); \(k\) and \(K\) are not interchangeable. |
| Exact Hessian | Differentiate after shear and check the determinant algebra. | Passed with a correction to the proposed anisotropic ledger: entries are \(O(1),O(1),O(R^{-1})\), determinant \(\asymp-1\), eigenvalues both \(O(1)\). |
| Lattice resonance | Test a phase with identical Hessian size on the integer lattice. | Failed for Hessian-only closure: \(Q(u,v)=uv\) gives a full \(R^2\) coherent sum. |
| Terminal M1 return | Match \(D,L\), phase, character, amplitude class, moving support, and normalization. | Phase/scale/character pass: \(D=r\asymp R^2,\ L=h\asymp R\), raw terminal size \(O(R)\), and (59.H3) restores \(\sqrt R\).  Coefficient/support hypotheses fail: (59.H8) and the actual symbol are jointly moving. |
| Endpoint and star ledger | Track artificial \(J\)-endpoints, inherited profile edges, hard top, floor edges, endpoint saddles, and collisions. | Not supplied; no lawful full B-process identity is yet available. |
| Primary-source applicability | Locate a theorem allowing a \(\chi _4\)-twisted reciprocal phase on a sharp \(R\)-wide moving strip, with actual BV/seam data, at raw size \(O(RX^\varepsilon)\). | No exactly applicable theorem was located. |

The controls establish the algebraic infrastructure and a strict no-go
for determinant-only reasoning.  They do not establish (59.H6).

## 6. Dependencies and exact artifacts used

The repository evidence used was exactly: protocol.md;
state/proof_obligations.yml; state/active_campaign.yml;
rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/derivation_packet.md;
rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/synthesis.md;
rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md; and
rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/reports/hyperbola_floor_source_hostile_audit.md.

The following primary sources were checked for an import.

- S. W. Graham and G. Kolesnik, “Two Dimensional Exponential Sums,”
  Chapter 6 of Van der Corput's Method of Exponential Sums,
  https://doi.org/10.1017/CBO9780511661976.006.  This is general
  two-dimensional van der Corput machinery; no theorem was found there
  whose stated coefficient and boundary hypotheses include the
  jointly moving, sharp actual strip (59.H8).

- U. M. A. Vorhauer and E. Wirsing, “Three two-dimensional Weyl steps
  in the circle problem I. The Hessian determinant,” Acta Arith. 91
  (1999), 43–55,
  https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9112.pdf.  Its Hessian
  analysis concerns third differences of the two-dimensional Euclidean
  norm and is one component of a multi-step Weyl argument together with
  separate exponential-integral estimates.  It is not a
  determinant-only theorem for \(Xh/(4Kh+s)\).

- M. N. Huxley, “Exponential Sums and Lattice Points,” Proc. London
  Math. Soc. (3) 60 (1990), 471–502,
  https://doi.org/10.1112/plms/s3-60.3.471.  Its results are formulated
  for smooth curved geometry and associated spacing problems; the
  required sharp character-weighted reciprocal strip with moving
  symbol and collision stars is not an instance verified here.

- M. Jutila, Lectures on a Method in the Theory of Exponential Sums,
  TIFR Lectures 80 (1987),
  https://mathweb.tifr.res.in/sites/default/files/publications/ln/tifr80.pdf.
  The transformation formulae require specified smooth/analytic phase
  and weight hypotheses and explicitly transform weights and
  endpoints.  They justify the need for the missing B-process seam
  ledger, not its omission.

- W. Duke, J. Friedlander, and H. Iwaniec, “Bilinear forms with
  Kloosterman fractions,”
  https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf.  Its
  modular-inverse/copime Kloosterman-fraction setting is not the real
  reciprocal phase \(Xh/r\) on (59.H8); no hypothesis map to the actual
  symbol was found.

This is a non-importability finding for these audited theorems, not a
claim that no relevant theorem exists anywhere in the literature.

## 7. Recommended state effect

Retain, without promoting the target estimate:

1. the exact projector (59.H1);
2. the interior saddle, character, phase, and normalization
   (59.H2)–(59.H3);
3. the exact post-shear Hessian identity (59.H4), with the corrected
   order-one eigenvalue ledger;
4. the strict counterexample to any Hessian-determinant-only lattice
   bound; and
5. the exact phase-and-scale return (59.H7) to terminal M1.

Reject any assertion that the two-dimensional Hessian by itself proves
square-root cancellation, and revise any statement assigning
\(\Phi_{hh}\asymp R\) or eigenvalues \(R,R^{-1}\) under (59.H5).
Retain the full high-shell twisted-divisor estimate, GAR/M1, and the
Gauss-circle exponent obligation as open.  A promotable next lemma would
have to be either (i) a uniform starred B-process plus a lossless
separable/BV decomposition of (59.H8) into the accepted terminal-M1
coefficient class, or (ii) a genuinely arithmetic proof of (59.H6)
that keeps \(\chi _4\), the moving actual symbol, and all endpoints
inside the signed sum.

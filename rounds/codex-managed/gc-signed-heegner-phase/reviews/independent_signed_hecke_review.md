# 1. Result

Round228, campaign gc-signed-heegner-phase. NONAUTHOR review by the
temporary complete_eisenstein_pairing role, 2026-09-28. Starting graph:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

Target: reports/signed_hecke_functional_attack.md, verified SHA256
f0d2507ef603e8ce1dac149994e52feb660ec9ccf27cf070a1ee83079b6d55dd.

**GREEN, narrowly scoped to the exact reductions, the fully priced
positive certificate, and the stated no-new-bound conclusion.** This
review supplies an explicit proof of the claimant's coefficient envelope
(21) at small as well as large dual indices. The small-index proof
requires two residues; rapid decay at large indices alone would not
justify that envelope. It also verifies the actual stationary symbol
by a change of radial coordinate that fixes the critical point.

The surviving root numbers, level-two oldspace factor, prime-two
depletion, exact functional-equation transform, cosine constant, resonant
length \(qt/(\pi^2L)\), and remaining spectral phase are correct. All
dual tails are paid by the exact transform bound proved here. The resulting
entire cusp certificate is
\[
 A^2T^{3/2+\epsilon}N^{5/4}.
\]
It remains weaker than the original complete arithmetic cap throughout
the frozen range. No complete circle exponent or signed cusp gain follows.

# 2. Exact statement and review hypotheses

The target's original definitions, area normalization, complete shift
range \(1\le h<2N\), all dyadic \(2\le N\le P<2T^{3/2}\), and every
real \(cT\le R\le CT\) are retained. Its \(\mathcal C\) denotes the entire
cuspidal component, while its \(\mathcal E\) denotes the entire continuous
component; this review follows those names. My separately frozen
continuous report used different letters.

The primitive functional equation is applied only after separating
conductor-one oldforms from conductor-two newforms and imposing the
pointwise parity/Fricke vanishings. The nonzero modes have reflection
parity zero and root number \(+1\). The uniform transform estimates below
concern \(t\ge1\); the original scalar kernel handles finite low and
exceptional spectrum before this transformation.

The scalar Legendre symbol and low/high spectral tails are the permitted,
reviewed closed227 interface, not an unproved arbitrary-test consequence
of a disk smoothing theorem. The source moment premises remain precisely
[Assing--Humphries 2607.13518v1, Theorem 1.2 and equation (8)](https://arxiv.org/html/2607.13518v1):
fixed levels one and two, their actual discriminant-minus-four CM points,
and Hecke indices coprime to the level. The second premise extends to the
needed even conductor-two newform indices through their explicit
ramified recurrence, as checked below. The probability-to-area changes
are fixed factors \((\pi/3)^{-2}\) or \(\pi^{-2}\) in fourth moments.
This review does not certify the entire source proof and does not repair
its defective collective-sieve display.

For the transform lemma, \(a=a_t\) is smooth with support in a fixed
compact interval of positive numbers and, after removing its declared
size, has uniformly bounded derivatives of every fixed order needed.
Consequently its Mellin transform \(\widehat a_t(\sigma+iv)\) decays
faster than any prescribed fixed power of \(1+|v|\), uniformly in \(t\)
on each fixed vertical line. The actual radial weight satisfies this
hypothesis by the argument in Section 3.

# 3. Independent derivation and seam checks

## CM symmetries, oldspace, and local two-factor

The reflections and Fricke maps satisfy
\[
 Ji=i,\qquad Jz_2=z_2+1,\qquad W_2z_2=z_2+1.
\]
Thus reflection-odd values vanish at both points, and Fricke-minus
values vanish at \(z_2\). Simultaneous diagonalization is lawful:
reflection and Fricke commute with the odd Hecke operators and preserve
the relevant eigenspaces.

Let \(u\) have area norm one at level one, and lift it to \(F(z)=u(z)\),
\(G(z)=u(2z)\) at level two. The index is three, and the unitary
Fricke involution interchanges \(F,G\), so both squared norms are three.
Tracing \(G\) to level one gives
\[
 u(2z)+u(z/2)+u((z+1)/2)=\sqrt2\,T_2u.
\]
Therefore the cross inner product is \(\sqrt2\lambda_u(2)\). At \(z_2\),
both lifts have value \(u(i)\). The plus vector has norm squared
\(6+2\sqrt2\lambda_u(2)\) and point value \(2u(i)\); its squared
normalized value is exactly
\[
 \frac{2}{3+\sqrt2\lambda_u(2)}\,|u(i)|^2.                 \tag{R1}
\]
The minus vector vanishes. The inherited fixed-prime bound
\(|\lambda_u(2)|\le2^\theta+2^{-\theta}\), with \(\theta<1/2\),
makes the denominator bounded away from zero. The equality
\(2^{1/2}(2^{1/2}+2^{-1/2})=3\) explains why the strict inequality
on \(\theta\) suffices. Hence no hidden oldspace norm is omitted.

For a level-two newform, trace to level one is zero. Using the cosets
\(I,S,ST\), the trace is
\[
 f+w_f\{f(z/2)+f((z+1)/2)\}
   =f+w_f\sqrt2\,U_2f.
\]
Thus \(\lambda_f(2)=-w_f/\sqrt2=-1/\sqrt2\) for the surviving forms.
This checks the local sign, not merely its absolute size.

Removing the Euler factor at two gives the coefficientwise identity
\[
 \sum_{m\ {\rm odd}}\lambda_f(m)F(m)
 =\sum_m\lambda_f(m)
  \{F(m)-\lambda_f(2)F(2m)+{\bf1}_{q=1}F(4m)\}.           \tag{R2}
\]
For example, the coefficient at \(m=2^kn\), \(n\) odd, is zero for
\(k\ge1\) by the degree-two unramified recurrence at conductor one and
the geometric recurrence at conductor two. At \(k=0\) it is unchanged.
The rescaled arguments retain their \(\ell^{it}\) and square-root
factors. There is no change of primitive conductor for an oldform.

## Primitive functional equation and exact dual identity

For an even primitive form, integrating its paired positive and negative
Fourier terms on the imaginary axis gives
\[
 \int_0^\infty f(iy)y^{s-3/2}\,dy
 =\frac{\rho_f(1)}2\pi^{-s}
   \Gamma((s+it)/2)\Gamma((s-it)/2)L(s,f).
\]
Here \(\int_0^\infty K_{it}(2\pi ny)y^{s-1}dy\) contributes
\(\pi^{-s}n^{-s}\Gamma((s+it)/2)\Gamma((s-it)/2)/4\);
pairing the two Fourier signs supplies the factor two.
The substitution \(y=1/(qv)\) and Fricke produce
\(\Lambda(s,f)=w_f\Lambda(1-s,f)\) with the claimant's completion.
For reflection-odd forms, differentiating in the real variable gives
\[
 f_x(i/(qy))=-w_f qy^2 f_x(iy),
\]
so the analogous Mellin integral has root number \(-w_f\) and the
gamma shifts by one. This also verifies the stated general parity
formula, although those modes contribute zero at the CM points.

Cuspidality makes these completed Mellin integrals entire. Starting
with \(\Re s>1\) for \(L(s-it,f)\), shifting to \(\Re s=-B\) crosses
no pole of that entire \(L\)-function. Applying its functional equation
and only then expanding the dual Dirichlet series gives exactly
the target's (12), with
\[
 G(s,t)=
 \frac{\Gamma((1-s+2it)/2)\Gamma((1-s)/2)}
      {\Gamma(s/2)\Gamma((s-2it)/2)}.                    \tag{R3}
\]
The powers of the conductor and \(\pi\) are
\((q/\pi^2)^{1/2+it}(\pi^2Ln/q)^s n^{-1-it}\).
The Mellin decay makes each contour shift legitimate; fixed-\(t\)
identities are established before taking uniform bounds. This does
not rely on a spectral interchange with a regularized theta vector.

## Both gamma transitions and the cosine constant

On a fixed line avoiding numerator poles,
\[
 |G(\sigma+iv,t)|
 \ll_\sigma
 [(1+|v|)(1+|v-2t|)]^{1/2-\sigma}.                     \tag{R4}
\]
The exponential gamma factors cancel exactly in the two numerator/
denominator pairs. At \(\sigma=1/2\), the numerator product is the
complex conjugate of the denominator product, so the modulus is
exactly one. In particular both \(v=0\) and \(v=2t\) are included;
neither transition grants exponential decay.

For \(|v|\le t^\kappa\), \(\kappa<1/2\), apply Stirling only to the
large pair. If \(A=(1-s)/2\), \(B=s/2\), then \(A+B=1/2\) and
\(A-B=1/2-s\). Consequently
\[
 \frac{\Gamma(A+it)}{\Gamma(B-it)}
 =t^{1/2-s}e^{\,i(2t(\log t-1)-\pi/4)}
   \left(1+O_\sigma((1+|v|)^2/t)\right).                 \tag{R5}
\]
The small quotient \(\Gamma((1-s)/2)/\Gamma(s/2)\) is left exact.
Fixed higher terms are polynomials in \(s\) times inverse powers of
\(t\); differentiating the logarithmic Stirling expansion gives the
corresponding fixed-order controls on a smaller window. The parity-one
constant is shifted by \(\pi/2\), consistent with the target.

For \(0<\Re s<1\), and then by continuation,
\[
 \int_0^\infty\cos(2y)y^{-s}\,dy
 =\frac{\sqrt\pi}{2}
       \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]
Mellin inversion therefore gives
\[
 \frac1{2\pi i}\int\widehat a(s)x^s
       \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}\,ds
 =\frac{2x}{\sqrt\pi}\int_0^\infty a(y)\cos(2xy)\,dy.     \tag{R6}
\]
The factor \(x\) is essential. Taking \(x=\pi^2Ln/(qt)\) in the
leading transform yields exactly the coefficient \(2\sqrt\pi L/\sqrt{qt}\)
in the target's (16). This verifies the scale \(K=qt/(\pi^2L)\) and
the constant \(e^{-i\pi/4}\), without conflating the small gamma factor
with a second large factor.

## Exact coefficient envelope, including small dual indices

This is the main extra proof supplied by the review. Put
\[
 I_t(x)=\frac1{2\pi i}\int_{(-B)}
                  \widehat a_t(s)x^sG(s,t)\,ds,\qquad x>0.
\]
All implied constants below depend only on finitely many fixed
seminorms of \(a_t\) and the selected fixed decay order.
For every fixed admissible \(\sigma\), (R4) and Mellin decay give
\[
 \int_{\mathbb R}|\widehat a_t(\sigma+iv)G(\sigma+iv,t)|\,dv
       \ll_\sigma t^{1/2-\sigma},\qquad t\ge1.           \tag{R7}
\]
To verify uniformity, split at \(|v|=t\). On \(|v|\le t\),
\(1+|v-2t|\asymp t\), and the remaining factor is integrable after
Mellin decay. On \(|v|>t\), arbitrarily many fixed powers of Mellin
decay pay any polynomial factor from (R4), including a neighborhood
of \(v=2t\). This also covers negative \(v\) of arbitrary size.

If \(x\ge t\), stay on the negative line:
\[
 |I_t(x)|\ll_B x^{-B}t^{B+1/2}
              =\sqrt t\,(x/t)^{-B}.                   \tag{R8}
\]
For \(0<x\le t\), shift this individual transform to \(\Re s=2\).
The two crossed poles are exactly
\[
 s=1,\qquad s=1+2it.
\]
They come from the two numerator gamma factors. Their residues in \(G\)
are respectively
\[
 r_0(t)=-\frac{2\Gamma(it)}{\sqrt\pi\,\Gamma(1/2-it)},
 \qquad
 r_2(t)=-\frac{2\Gamma(-it)}{\sqrt\pi\,\Gamma(1/2+it)},    \tag{R9}
\]
both \(O(t^{-1/2})\) in modulus. No poles occur on the new line, and
the next numerator poles have real part three. Keeping the orientation,
\[
 I_t(x)=\frac1{2\pi i}\int_{(2)}
             \widehat a_t(s)x^sG(s,t)\,ds
       -r_0(t)\widehat a_t(1)x
       -r_2(t)\widehat a_t(1+2it)x^{1+2it}.              \tag{R10}
\]
The residue at \(s=1\) must not be discarded. The residue at \(1+2it\)
has the additional bound
\(\widehat a_t(1+2it)\ll_D t^{-D}\) for any fixed \(D\).
By (R7) on the line two, the remaining integral is
\(O(x^2t^{-3/2})\). Thus
\[
 |I_t(x)|\ll x/\sqrt t,\qquad 0<x\le t.                 \tag{R11}
\]
The contour identity is first valid for each fixed \(t\); the horizontal
segments tend to zero by Mellin decay. Equations (R7)--(R11) then provide
uniform constants, including the second moving gamma transition. This
avoids an unjustified uniform contour limit.

The \(n\)-th coefficient in the exact dual series, omitting its
unit-modulus phase, has size a fixed \(q\)-factor times
\(n^{-1}|I_t(\pi^2Ln/q)|\). Equations (R8)--(R11) yield, for any chosen
fixed \(D\),
\[
 \boxed{\quad
 |b_n(t)|\ll_D \frac{L}{\sqrt t}
       \left(1+\frac{n}{K}\right)^{-D},
 \qquad K=\frac{qt}{\pi^2L}.\quad}                      \tag{R12}
\]
For large \(n\), increase the negative contour order once if needed;
the extra \(n^{-1}\) only improves decay. For small \(n\), the pole
terms supply precisely the uniform \(L/\sqrt t\) size.
Multiplication by the actual symbol size \(c_{d,U}\) gives target (21).
This is a bound for the exact transformed coefficient, with every
correction and tail included. It needs no claim that a finite
Stirling remainder itself has a cosine transform.

For completeness, the displayed leading asymptotic can also be used
with a fully summed small error. On \(\Re s=-B\), choose \(B\) large
enough for absolute convergence of the dual coefficient sum. Outside
\(|v|\le t^\kappa\), (R4) and Mellin decay give any fixed negative power
of \(t\), after paying the fixed polynomial \(t^{B+1/2}\). Inside,
expand (R5) to a fixed order sufficiently larger than \(B\) and the
desired error exponent. The remainder is controlled by a fixed higher
Mellin seminorm; its entire \(n\)-sum converges with the factor
\(n^{-1-B}\). The parameter ranges \(t\ll T^{7/4}\), \(L\gg1\) for
nonempty integer sums, and the fixed polynomial moment bounds permit
an error \(O(A^2T^{-D})\) after all modes, shifts, and descendants.
The exact estimate (R12) is stronger for the purpose of the norm ledger
and avoids assigning an unproved separate envelope to each remainder.

## Actual stationary symbol and smooth endpoints

The symbol hypothesis is valid for the actual compact weight, not just
an arbitrary leading stationary value. On a shift dyad \(h\asymp M\)
and its enlarged stationary band \(t\asymp U\), put
\[
 r_*(h,t)=2\log(\pi R\sqrt h/t),\qquad v=r-r_*.
\]
The positive spherical branch then has exact phase
\[
 2\pi R\sqrt h e^{-r/2}+tr
   =tr_*+t\{2e^{-v/2}+v\}.                              \tag{R13}
\]
The critical point in \(v\) is fixed at zero. All relevant \(v\)-supports
lie in a fixed bounded interval because \(h\asymp M\) and \(t\asymp U\).
The original support is smoothly zero-extended away from \(r=0\).
Furthermore
\[
 x(h,t,v)=\frac{\pi^2R^2h^2e^v}{4t^2}
             -\frac h2+\frac{t^2e^{-v}}{4\pi^2R^2}.      \tag{R14}
\]
Every fixed scaled \(h\)-derivative of \(x,x+h\) is \(O(N)\) on this
enlarged region. Thus differentiating the \(g\)-factors costs their
fixed scaled seminorms, with no \(t\) loss after extracting the phase
\(\exp(i(tr_*+2t))\).

In the radial measure, the spherical prefactor is
\(t^{-1/2}\sqrt{\sinh r}\); after multiplication by \(\sqrt m\),
\(h=dm\), its size is \(t^{-1/2}\sqrt{N/d}\).
Stationary integration in \(v\), with curvature \(t/2\), supplies
another \(t^{-1/2}\). Differentiation in \(h\) acts on the uniformly
smooth amplitude in (R13), so the resulting symbol and every fixed
scaled derivative have size
\[
 c_{d,U}\ll A^2\sqrt N/(U\sqrt d).                      \tag{R15}
\]
Smoothly vanishing endpoints make this true when the critical point
meets or leaves the actual support; no boundary value is added.
For the other spherical branch, phase differentiation is uniformly
nonzero on this band. After the same extraction, any finitely many
scaled \(h\)-derivatives may introduce fixed powers of \(t\); sufficiently
many integrations by parts pay them. This supplies the same symbol
conclusion with arbitrary fixed savings for that branch.

Equivalently, one may use a finite parameter stationary expansion and
take enough terms to pay the full error as just described. Either
implementation justifies applying the exact transform estimate (R12)
to the actual symbol. Treating only \(g(x_*)g(x_*+h)\) as the exact
weight would not have sufficed; (R13)--(R15) supply the missing uniform
argument.

The original common phase and the leading large-gamma phase combine as
\[
 e^{i2t(1+\log(\pi R/t))}d^{it}
 e^{i(2t(\log t-1)-\pi/4)}(q/\pi^2)^{it}n^{-it}
   =e^{-i\pi/4}(qdR^2/n)^{it}.                          \tag{R16}
\]
The local terms in (R2) replace \(d\) by \(d\ell\) and \(L\) by
\(L/\ell\). Their bounded factors and phases remain. Deep descendants
therefore have \(K\asymp qTd/\sqrt N\), as the claimant states.
No integration by parts in a discrete spectral sum is licensed by (R16).

## Complete norm price and restoration

The individual Hecke second moment gives
\[
 \|\lambda_f(n)\|_{\ell^2(t_f\asymp U)}
 \ll_\epsilon (nU)^\epsilon(U+n^{1/4}).
\]
At conductor two, write \(n=2^kn_0\), \(n_0\) odd. The exact recurrence
\(\lambda_f(n)=(-1/\sqrt2)^k\lambda_f(n_0)\) bounds the primitive newform
sum by the allowed odd-index moment. At conductor one all indices are
already permitted. Bounded local coefficients and (R1) cost fixed
constants.

Using (R12), Minkowski is applicable even though the coefficients depend
on \(t_f\): their absolute envelopes are uniform for each \(n\).
For \(K\ge1\),
\[
 \sum_{n\ge1}(1+n/K)^{-B}(U+n^{1/4})
       \ll_B UK+K^{5/4}\ll UK,                          \tag{R17}
\]
when \(B>2\) and \(K\ll U\). The last inequality uses \(U\ge1\).
In the frozen range \(K\gg T^{1/4}\), up to fixed constants, so any
remaining bounded \(T\) case is absorbed in the constant. The bound
\(K\ll U\) follows from \(L\gg1\) for every nonempty original integer
sum. Empty such sums are exactly zero; this does not remove continuous
density from the separate original correlation problem.

Equation (R17) includes the entire \(n\gg K\) region, including
\(n\gg U^4\) where the individual second moment is no longer dominated
by \(U^2\). That region is paid by the \(n^{1/4}\) term and the
polynomial dual decay, not silently truncated.
Thus
\[
 \|V_{d,M,U}\|_2
 \ll_\epsilon T^\epsilon c_{d,U}\frac L{\sqrt U}\,UK
 \ll_\epsilon T^\epsilon c_{d,U}U^{3/2}.
\]
The point fourth moment supplies a further \(U^{1+\epsilon}\) by
Cauchy. Substituting (R15) gives
\[
 |\text{pairing}_{d,M,U}|
 \ll A^2T^\epsilon\sqrt N\,U^{3/2}/\sqrt d.              \tag{R18}
\]
The actual \(d\)'s are powers of two, whose \(d^{-1/2}\) sum converges.
The shift dyads have \(U\asymp TM/\sqrt N\), and their \(M^{3/2}\)
sum is dominated by \(M\asymp N\). All inherited nonstationary spectral
tails are paid before this estimate. Therefore (R18) yields exactly
the target's complete cusp certificate
\[
 |\mathcal C|\ll A^2T^{3/2+\epsilon}N^{5/4}.              \tag{R19}
\]

At \(N=T\), this is \(A^2T^{11/4+\epsilon}\), a factor \(T^{5/4}\)
larger than the sufficient raw quarter target. Relative to the full
arithmetic cap \(A^2N^{2+\epsilon}\), the ratio is
\(T^{3/2}N^{-3/4}\gg T^{3/8}\) in the frozen range. These are comparisons
of upper certificates and do not imply an actual lower bound. The
claimant correctly keeps the continuous partner explicit, rather than
calling (R19) a complete bound.

The inverse pretrace transform, exact determinant identity and parity
recurrence recover the original signed correlations with their original
test. Restoring every component, diagonal, density, singleton, shell and
Schwartz tail therefore leaves the previous complete fallback exponent.
The independently paid continuous component from my prior assignment
does not estimate the entire cusp target and is not needed to validate
this claimant's no-new-bound conclusion.

# 4. First doubtful or unproved step

No unresolved error remains in the scoped identities or the positive
certificate after the exact envelope proof (R7)--(R12) and actual
symbol proof (R13)--(R15). These derivations are part of this review's
evidence; the short assertion of rapid large-\(n\) decay in the claimant
would not alone justify small-\(n\) control.

The first unproved full inequality remains the target's (5), or its
entire cuspidal expression (24) if the continuous component is separately
paid. Neither the shortened dual scale nor the explicit smooth spectral
phase supplies cancellation among the actual discrete spectral points.
The proof supplies no whole-wave gain, lower bound, or impossibility
statement.

# 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Frozen target | Exact assigned SHA verified before and during review. |
| CM reflection/Fricke | Point symmetries prove the claimed vanishings. |
| Oldspace and area | Full Gram matrix gives (R1); its denominator is uniformly positive. |
| Primitive FE/local prime two | Both conductors and root signs checked; (R2) retains every local argument and factor. |
| Cosine constants | Mellin inversion includes the essential \(x\) factor in (R6). |
| Both gamma transitions | Global envelope (R4); exact modulus one on the critical line; moving second transition included in (R7). |
| Small dual indices | Shift to real part two crosses and retains both residues (R9)--(R10). |
| Large dual indices | Original negative contour proves (R8), with the entire tail summed in (R17). |
| Actual symbol and endpoints | Fixed-critical-point radial coordinate (R13) proves scaled derivative bounds uniformly, including vanishing support edges. |
| Finite expansion remainder | Exact envelope controls the full transform; a finite expansion can also have its entire remainder paid at fixed order. |
| Spectral norm hypotheses | Individual moments only; no fixed-coefficient collective sieve receives a moving vector. Even newform indices are handled by their local recurrence. |
| All ranges and full powers | Every parity depth, shift dyad, low/high spectrum, original singleton and Schwartz tail retained. |
| Signed versus positive | Phase identified before norms; discarded only in the priced positive procedure. No spectral cancellation from smoothness is asserted. |
| Real/complex and full goal | Inherited \(\beta\) remains a whole real-wave bound; fixed moments do not prove quarter. |
| Experiments | None. All checks are analytical/algebraic or exact source inspection. |

# 6. Dependencies and provenance

This reviewer authored the separate complete continuous-component report.
Its initial frozen hash was
105b2fb292d1e32fff401d92292a20590f5a1185a55a58815d0a77bb15f645c6.
During this review the conductor expressly authorized correction of two
unintended standalone carriage-return bytes in its LaTeX roman-type
commands and a provenance note. That byte-only repair changed no
mathematical content; its replacement frozen hash is
cf92b16e42ad85d900a532a66f1df33cb8aa2be175c7f0f4d8013501a4112d1f.
That report is not the present review target and has not otherwise been
edited. This is a NONAUTHOR review, not a statement-only or fresh-history
review.

Available prior context is disclosed in that report: protocol, relevant
authoritative graph entries and active manifest, Round228 strategy and
interface, the September23 review and closed226 checkpoint, the permitted
closed227 reports/reviews/synthesis, and the complete square-root
large-values moment kernel. Prior knowledge included the exact Heegner
geometry, scalar Legendre phases and tails, and the open full target.

New reads for this review were only the assigned frozen signed-Hecke
report and its already cited
[AH2607.13518v1](https://arxiv.org/html/2607.13518v1), specifically the
individual Hecke moment equation (8) and normalization context. No
additional primary theorem or work was imported. No current blind
packet/report, conductor control, or sibling review was read.
The small-index contour, residues, actual-symbol coordinate change,
and full-tail summation were rederived independently here.

The conductor's review brief identified the small-dual-index envelope
as a required seam. I reported the exact residue-based resolution while
working; I received no hidden calculation, blind result, or sibling
review. Only this assigned review was written, apart from the expressly
authorized byte-only repair to my own frozen report. No graph, draft,
matrix, synthesis, legacy or closed-round artifact changed.

# 7. Recommended state effect and stopping rule

Retain the target as **GREEN candidate evidence at the exact reviewed
hash**, together with this review's explicit uniform envelope and symbol
derivations. No mathematical repair to the target is requested. The
conductor should preserve the two-residue argument in any future use
of its coefficient envelope.

No promotion of the full target, signed cusp estimate, complete exponent,
moment claim, M1/M2/GAR/endpoints, or quarter theorem is justified.
The complete signed Heegner objective remains open despite the useful
exact reformulation and the separately paid continuous component.

Freeze this review at its externally recorded SHA256 and stop. Only the
conductor decides Round228 closure or subsequent work.


# Round 84 blind rederivation: exact stationary normalization and self-return

## 1. Result

**Result (exact normalization and completion-only no-go).**  For the
orientation in the packet, the stationary sign is \(n>0\).  After the
change \(c=gx\), every one of the three local classes has the exact
Gaussian normal form

\[
 I_b(n)={h_{b,n}\over g}
 e\!\left(-\lambda_b\sqrt n\right)\mathcal G_b(n),
 \qquad n>0,                                                \tag{R84.1}
\]

where

\[
 c_{b,n}=\sqrt{{4bA_{\kappa,b}\over n}},\qquad
 \lambda_b=\sqrt{{A_{\kappa,b}\over b}}
 =\sqrt X+{\sqrt{\kappa k}\over b},\qquad
 h_{b,n}=\sqrt{{2bc_{b,n}\over n}},                       \tag{R84.2}
\]

and \(\mathcal G_b(n)\) is the exact truncated-Gaussian profile defined
in (R84.6) below.  In stationary bulk it is bounded by
\(X^\varepsilon\) using only the accepted \(L^\infty+BV\) control.  A
replacement of it by
\(e(-1/8)V_{b,c_{b,n},k}^{(\kappa)}\) with a power-saving error does
*not* follow from that control.

For \(m=n+d>0\), (R84.1) gives the exact phase

\[
 e\!\left(-\lambda_b(\sqrt m-\sqrt n)\right),              \tag{R84.3}
\]

but a complete use of this oscillation is involutive.  If

\[
 P_b(a)=\sum_{\ell\in\mathbb Z}F_b(a+M\ell),\qquad
 L_b=\sum_{a\bmod M}^{*}e_M(K\bar a)P_b(a),                \tag{R84.4}
\]

then the full \(d\ne0\) expression for a fixed \(b\) is exactly

\[
 {1\over M^2}\sum_{m\ne n}
 \bigl(S(m,K;M)\overline{S(n,K;M)}-c_M(m-n)\bigr)
 I_b(m)\overline{I_b(n)}
 =|L_b|^2-\sum_{a\bmod M}^{*}|P_b(a)|^2-{D_b\over M^2},    \tag{R84.5}
\]

with
\(D_b=\sum_n(|S(n,K;M)|^2-\varphi(M))|I_b(n)|^2\).
The last term is target-safe in absolute value after summing over
\(b\asymp B\).  Thus the first exact signed survivor is the physical
rank-one projection
\(|L_b|^2-\sum_a^*|P_b(a)|^2\), or, for an upper bound, the actual-symbol
quantity \(|L_b|^2\).  This is precisely the pre-dual progression sum,
not a new cancellative transform.

Consequently no fixed \(B^{-\delta}\) gain is proved from the frozen
hypotheses.  More strongly, any proposed proof whose only new step is
complete summation of the stationary square-root phase returns exactly
to (R84.5), so that route is circular.  This is a no-go for the
completion-only mechanism, not a counterexample to the desired
actual-symbol estimate.

## 2. Exact statement and hypotheses

Fix one allowed \((\kappa,g,M,K)\):

\[
 (\kappa,g,M,K)=
 \begin{cases}
 (1/4,1,4b,k),\\
 (1/2,2,2b,2[k\bar4]_b),\\
 (1,4,b,[k\bar4]_b).
 \end{cases}                                               \tag{R84.6a}
\]

Here \(k>0\), \(gM=4b\), \(b\asymp B=C/T\),
\(J^{13/18}<C\le J^{3/4}\), and the parity and gcd support of the chosen
class is retained exactly.  Write
\(W_b(c)=V_{b,c,k}^{(\kappa)}\), extended by zero off its exact
smooth-interior support in \([C,2C]\), and assume only

\[
 \|W_b\|_\infty+\operatorname {Var}W_b\ll_\varepsilon X^\varepsilon.
\]

For \(n>0\), put

\[
 p_{b,n}=\sqrt{{A_{\kappa,b}n\over4b}}
 ={\lambda_b\sqrt n\over2},\qquad
 z={u\over\sqrt{2p_{b,n}}},
\]

\[
 t_{b,n}(u)=\left({z+\sqrt{z^2+4}\over2}\right)^2,
 \qquad
 j_{b,n}(u)={2t_{b,n}(u)^{3/2}\over1+t_{b,n}(u)},
\]

and define the exact profile

\[
 \boxed{\displaystyle
 \mathcal G_b(n)=\int_{\mathbb R}
 W_b\!\left(c_{b,n}t_{b,n}(u)\right)
 j_{b,n}(u)e(-u^2/2)\,du .}                               \tag{R84.6}
\]

Then (R84.1) is an identity, including a saddle at or near a support
edge.  The exact saddle-support condition is
\(c_{b,n}\in\operatorname {supp}W_b\); the containing interval is

\[
 {N_b\over4}\le n\le N_b,qquad
 N_b={4bA_{\kappa,b}\over C^2}
 ={A_{\kappa,b}Mg\over C^2}\asymp Q^2.                  \tag{R84.7}
\]

If the normalized distance from the saddle to both support edges tends
to infinity and suitable symbol regularity on the length \(h_{b,n}\)
is separately proved, (R84.6) has leading value
\(e(-1/8)W_b(c_{b,n})\).  At an entry or exit it is instead the
corresponding truncated Fresnel profile.  The opposite orientation is
the conjugate formula, has stationary sign \(n<0\), Gaussian
\(e(+1/8)\), and the reversed square-root phase.

The precise stationary-positive part of the centred correlation is
therefore

\[
 \sum_{b\asymp B}{1\over M^2}
 \sum_{\substack{m,n>0\\m\ne n}}
 \mathcal C_M(m,n){h_{b,m}h_{b,n}\over g^2}
 \mathcal G_b(m)\overline{\mathcal G_b(n)}
 e\!\left(-\lambda_b(\sqrt m-\sqrt n)\right),            \tag{R84.8}
\]

where
\(\mathcal C_M(m,n)=S(m,K;M)\overline{S(n,K;M)}-c_M(m-n)\).
The edge profiles and all tails not belonging to this positive-positive
stationary sector remain separate.

## 3. Proof and derivation

Changing variables \(c=gx\) and using \(gM=4b\) gives

\[
 I_b(n)={1\over g}\int W_b(c)
 e\!\left(-{A_{\kappa,b}\over c}-{nc\over4b}\right)dc.   \tag{R84.9}
\]

For \(n>0\), its phase has the unique critical point \(c_{b,n}\) in
(R84.2).  At that point

\[
 \phi(c_{b,n})=-\lambda_b\sqrt n,qquad
 \phi''(c_{b,n})=-{n\over2bc_{b,n}},qquad
 |\phi''(c_{b,n})|^{-1/2}=h_{b,n}.                        \tag{R84.10}
\]

Set \(c=c_{b,n}t\).  Since the two phase summands agree at the
critical point,

\[
 -{A\over c}-{nc\over4b}=-p_{b,n}(t+t^{-1})
 =-2p_{b,n}-p_{b,n}{(t-1)^2\over t}.                     \tag{R84.11}
\]

The monotone substitution
\(u=\sqrt{2p_{b,n}}(\sqrt t-1/\sqrt t)\) makes the last term
\(-u^2/2\), while

\[
 dc={c_{b,n}\over\sqrt{2p_{b,n}}}
 {2t^{3/2}\over1+t}\,du=h_{b,n}j_{b,n}(u)\,du.
\]

This proves the exact identity (R84.1).  It also fixes the stationary
sign and the Gaussian: with \(e(y)=e^{2\pi iy}\),

\[
 \int_{\mathbb R}e(-u^2/2)du=e^{-\pi i/4}=e(-1/8).        \tag{R84.12}
\]

When \(c_{b,n}\asymp C\), the \(t\)-support lies in a fixed compact
subset of \((0,\infty)\).  The function
\(W_b(c_{b,n}t(u))j_{b,n}(u)\) has bounded supremum and total variation.
Splitting at \(|u|=1\) and applying the first-derivative bound to the two
Gaussian tails gives

\[
 |\mathcal G_b(n)|\ll_\varepsilon X^\varepsilon,qquad
 |I_b(n)|\ll_\varepsilon X^\varepsilon {h_{b,n}\over g}. \tag{R84.13}
\]

For \(n\le0\), or for positive \(n\) a fixed factor outside the interval
in (R84.7), the original phase derivative in (R84.9) does not vanish.
The BV first-derivative estimate gives, with the evident distance from
the stationary frequency interval,

\[
 |I_b(n)|\ll_\varepsilon {X^\varepsilon\over g}
 \left(\inf_{c\in[C,2C]}
 \left|{A\over c^2}-{n\over4b}\right|\right)^{-1}.        \tag{R84.14}
\]

Using (R84.13) on a fixed enlargement of (R84.7) and (R84.14) outside
it yields the useful energy ledger

\[
 \sum_{n\in\mathbb Z}|I_b(n)|^2
 \ll_\varepsilon X^\varepsilon BC.                       \tag{R84.15}
\]

Indeed, the enlarged stationary interval has \(O(N_b)\) integers and
\(h_{b,n}^2/g^2\asymp BC/Q^2\); the two nonstationary tails contribute
\(O_\varepsilon(X^\varepsilon b^2/N_b)\).  A bounded number of entry and
exit frequencies is already covered by the exact profile.

For the arithmetic normalization, expand the two Kloosterman sums.
The Ramanujan term is exactly their equal-residue part, so

\[
 \mathcal C_M(m,n)=
 \sum_{\substack{a,q\bmod M\;*\\a\ne q}}
 e_M\!\left(ma-nq+K(\bar a-\bar q)\right).               \tag{R84.16}
\]

Let \(Z_b(a)=\sum_n I_b(n)e_M(an)\).  Exact Poisson summation with the
measure in the packet gives

\[
 Z_b(a)=M\sum_{\ell\in\mathbb Z}F_b(a+M\ell)=MP_b(a).     \tag{R84.17}
\]

Summing (R84.16) over all ordered \((m,n)\), applying (R84.17), and then
removing the literal diagonal \(m=n\) exactly once proves (R84.5).
Moreover

\[
 \sum_{a\ne q}^{*}e_M(K(\bar a-\bar q))P_b(a)\overline{P_b(q)}
 =\left|\sum_a^*e_M(K\bar a)P_b(a)\right|^2-
 \sum_a^*|P_b(a)|^2.                                     \tag{R84.18}
\]

Finally, the trivial bound \(|S(n,K;M)|\le M\), (R84.15), and
\(M\asymp B\) imply

\[
 \sum_{b\asymp B}{|D_b|\over M^2}
 \ll_\varepsilon X^\varepsilon B^2C
 ={X^\varepsilon C^3\over T^2}
 \le X^\varepsilon J^{21/20}
 \ll X^\varepsilon {J^2\over T}.                         \tag{R84.19}
\]

Thus the diagonal bookkeeping term is safely below the target.  In the
stationary range,

\[
 {h_{b,m}h_{b,n}/g^2\over M^2}
 \asymp {BC/Q^2\over B^2}={C\over BQ^2}={T\over Q^2},     \tag{R84.20}
\]

which records the external \(M^{-2}\) and shows that stationary
normalization alone supplies no hidden power of \(B\).

## 4. First doubtful or unproved step

The first unavailable step is not the critical phase; it is a uniform
description of the actual normalized profile \(\mathcal G_b(n)\), or an
equivalent estimate for the actual rank-one projection \(L_b\).
Specifically, the frozen hypotheses do not prove either

\[
 \mathcal G_b(n)=e(-1/8)W_b(c_{b,n})+o(1)
\]

uniformly through the bulk and edges, or the needed aggregate bound

\[
 \sum_{b\asymp B}|L_b|^2
 \ll_\varepsilon X^\varepsilon {J^2\over T}.              \tag{R84.21}
\]

The derivative gap is genuine at the level of the packet.  In a fixed
bulk saddle, take a smooth function \(w\) of bounded variation and set
\(W_b(c)=w((c-c_{b,n})/h_{b,n})\) inside the support.  Its supremum and
total variation are uniformly bounded, but (R84.6) tends to
\(\int w(u)e(-u^2/2)\,du\), which can differ by a nonzero constant from
\(e(-1/8)w(0)\).  Hence the asserted leading replacement can have error
of the same size as the stationary term.  This is an insufficiency of
the stated hypotheses, not a claim that the fixed antecedent symbol has
this adversarial form.

There is also no generic first-derivative escape.  On
\(n=r+M\ell\), the derivative of the product phase can meet integers;
subtracting such an integer multiple of \(\ell\) changes no exponential.
For the one-factor completion in (R84.17), its stationary equation is

\[
 {\lambda_b\over2\sqrt n}=q+{a\over M}.
\]

Using \(n=4bA/c^2\) shows exactly
\(\lambda_b/(2\sqrt n)=c/(4b)=x/M\), so its integer resonance is
\(x=a+qM\), the original physical lattice point.  Thus completing the
dual stationary phase proves (R84.17) and returns to \(L_b\); it does
not prove (R84.21).  An additional actual-symbol estimate that breaks
this self-return is the first missing mathematical input.

## 5. Control tests and outcomes

1. **External normalization and Poisson measure.**  The factor is
   exactly \(M^{-2}\).  The Fourier sum is \(Z_b(a)=MP_b(a)\), not
   \(P_b(a)\); the two factors \(M\) cancel the external \(M^{-2}\) in
   (R84.5).  The stationary prefactor is \(h_{b,n}/g\), and (R84.20)
   is the resulting target ledger.

2. **All local classes.**  The three rows in (R84.6a) were kept
   separately.  Their common analytic reduction uses only \(gM=4b\).
   The unit-modulus local constant cancels against its conjugate, while
   \(K\), parity support, and \((K,M)=O_k(1)\) remain in the arithmetic
   factor.  Empty classes contribute zero only by exact support.

3. **Stationary sign, phase, and Gaussian.**  The present orientation
   has \(n>0\), critical phase \(-\lambda_b\sqrt n\), curvature negative,
   and Gaussian \(e(-1/8)\).  The reflected orientation has the reversed
   sign and conjugate Gaussian.  Formula (R84.11) verifies the exact
   phase rather than only its scale.

4. **Saddle support, entry/exit, tails, and symbol regularity.**  The
   containing stationary interval is (R84.7).  Entry and exit are the
   exact truncated profile (R84.6); they were not assigned the full
   Gaussian constant.  Nonstationary signs and distant frequencies are
   controlled by (R84.14).  Only \(L^\infty+BV\) was used.  The smooth
   rescaled-bump test in Section 4 falsifies a uniform leading-symbol
   remainder based on BV alone.

5. **Literal and modular differences.**  The literal \(d=0\) is
   subtracted once in passing from all \((m,n)\) to (R84.5).  If
   \(d=hM\ne0\), periodicity gives the exact surviving coefficient

   \[
   S(n+hM,K;M)\overline{S(n,K;M)}-c_M(hM)
   =|S(n,K;M)|^2-\varphi(M),
   \]

   so these modes are not deleted.  Negative \(d\) is obtained by
   interchanging \(m,n\); it is not identified with the residue
   representative \(M-d\).  For two stationary saddles,
   \(m,n\asymp N_b\), hence small, mesoscopic, large, negative, and
   near-edge differences all occur with \(|d|=O(N_b)\).  When one index
   leaves this range its entry/exit or nonstationary profile must be
   used.

6. **Ramanujan and gcd-degenerate modes.**  Equation (R84.16) proves
   that \(c_M(d)\) removes only the equal physical residues, for every
   literal \(d\).  No division by \(d\), \(n\), or a prime-power gcd was
   made.  Zero Ramanujan frequency, prime-power offsets, and all
   gcd-degenerate nonzero frequencies therefore remain in (R84.5).
   In particular the nonzero multiples in the preceding control are
   an explicit surviving family.

7. **Progression integer resonances.**  For \(d>0\), on
   \(n=r+M\ell\),

   \[
   \Psi'(\ell)={M\lambda_b\over2}
   \left(n^{-1/2}-(n+d)^{-1/2}\right),\quad
   \Psi''(\ell)={M^2\lambda_b\over4}
   \left((n+d)^{-3/2}-n^{-3/2}\right).
   \]

   The signs reverse with \(d\).  For small \(d\), the first derivative
   is about \(M\lambda_b d/N_b^{3/2}\); for larger \(d\) it crosses
   integer values, so a bound in terms of \(|\Psi'|\) rather than its
   distance to \(\mathbb Z\) fails.  The exact resonance-to-lattice
   calculation in Section 4 and (R84.17) pass the wraparound control by
   showing what those resonances return to.

8. **Perfect-square and fourth-power tests.**  Exact coherent phases
   occur in an admissible subcase.  Take the \(\kappa=1\) class,
   \(k=q^2\), \(X=J^2\) with integral \(q,J\), and \(b\) in a compatible
   gcd class.  For \(n=s^2\) and \(m=(s+hb)^2\),

   \[
   e\!\left(-\lambda_b(\sqrt m-\sqrt n)\right)
   =e(-Jhb-qh)=1,
   \]

   while \(m-n\) is a nonzero multiple of \(M=b\).  Taking
   \(s=u^2\) and \(s+hb=(u+b)^2\) gives the same test with both \(m,n\)
   fourth powers.  These sparse families do not disprove the aggregate
   target, but they do disprove uniform nonresonance of the stationary
   phase and force retention of the modular-multiple survivor.

9. **Phase-conjugating and complete-transform controls.**  The first
   term in (R84.5) is the rank-one form (R84.18).  Arbitrary data
   \(P_b(a)\propto e_M(-K\bar a)\) saturate its positive direction, but
   no claim is made that such data come from the actual symbol.
   Equation (R84.17) is the exact self-return control: completing the
   stationary Fourier side recovers the original progression sum.
   Therefore an arbitrary-coefficient large sieve or a second blind
   completion cannot supply the claimed \(B\)-power.

10. **Sources and downstream ownership.**  No external theorem or web
    source was invoked, so there are no unaudited hypotheses at
    \(M\asymp B\), \(n\asymp Q^2\).  The conclusion concerns only the
    fixed transition-flattened, smooth-interior, nonaxial M1 component,
    orientation, alias, and dual pair in the frozen band.  It says
    nothing about transition errors, axes, cone edges, other sectors,
    \(C>J^{3/4}\), full M9-M1, M9, or the Gauss-circle exponent.

## 6. Dependencies and exact artifacts used

The derivation used only:

- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/briefs/blind_dual_difference_rederivation.md`.

No strategy file, state file, prior-round artifact, sibling report,
source card, web source, or numerical computation was read or used.

## 7. Recommended state effect

**Revise.**  Retain (R84.1), (R84.5), and the target-safe estimate
(R84.19) as candidate evidence after checking, but do not promote a
range or a \(B^{-\delta}\) gain.  Reject a completion-only stationary
correlation route: it self-returns to the actual-symbol rank-one sum.
The next mechanism must directly control (R84.21), exploit the negative
energy in (R84.18), or prove additional scale-sensitive regularity of
the exact antecedent symbol.  No shared proof-state change is justified
by this blind report alone.

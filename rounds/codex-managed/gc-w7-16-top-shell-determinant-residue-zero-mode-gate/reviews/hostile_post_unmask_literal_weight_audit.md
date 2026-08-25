# Round 131 post-unmask hostile audit: the arithmetic mask is valid, but the full physical factorization is not yet proved

Campaign: gc-w7-16-top-shell-determinant-residue-zero-mode-gate  
Role: hostile post-unmask source/seam reviewer  
Starting graph SHA-256:
23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825  
Status: candidate review evidence only; no shared proof state is changed.

## 1. Result

The conductor's fixed-\(p\) **primitive support-mask Fourier kernel is
correct**, after two terminology corrections:

1. its displayed periods \(4M\) for M1 and \(|m|\) for M2 are valid
   periods but are generally not primitive periods; the primitive
   periods use the radical of the inner numerator; and
2. the nonzero M2 “zero mode” is the \(k=0\) Fourier coefficient of the
   fixed-\(p\), \(q\)-arithmetic mask.  It is not the determinant
   diagonal \(n=0\), and it is not the mode of the full \(p\)-interlaced
   \(n\)-weight.

The discovery report overstates two other seams.

First, its bare identity
\[
 \sum_{\rho\mid(m,b')}\mu(\rho)=\mathbf1_{(m,b')=1}
 \tag{131.P1}
\]
does not factor the weighted reassembly (discovery (131.6)), because
\(T_{i;r,p,\rho,D}^{\rm lit}(b'/\rho)\) and its star/owner data depend on
\(\rho\).  Either physical primitivity must be invoked as an already
proved support condition, or one must prove the missing weighted
reassembly identity.  Equation (131.P1) alone does not make
discovery (131.9) an exact periodic-mask-times-envelope formula.

Second, \(O(1+WL/D)\) windows of length \(D/W\) give a covering
**capacity**
\[
 (1+WL/D)(D/W)\ll L,
 \tag{131.P2}
\]
not a lower count of nonempty coherent physical windows.  Thus
\(DK_D\) is the worst-case triangle capacity of that cover, not proved
resonant mass.

The M1 Gauss-times-Ramanujan computation survives these corrections.
For M2, the fixed-\(p\) primitive \(q\)-kernel is valid for both odd and
even \(b\).  The odd-\(b\) condition appears only when one tries to
encode the varying numerator character as one scalar character of
\(n\bmod4|a|\).  If \(b\) is even, that encoding is impossible; an
explicit repair has period growing with \(v_2(b)\), so it is not a
harmless modulus-\(4|a|\) correction.

No corrected arithmetic identity supplies a scalar bank or a physical
family-level lower bound.  The terminal verdict remains
\[
 \boxed{\texttt{degenerate}}.
 \tag{131.P3}
\]

## 2. Exact statement and hypotheses

Fix a primitive outer ray \(r=(a,b)\), put \(A=|a|\), fix one physical
increment \(p\), and set
\[
 m=a+p,\qquad b'=b+q,\qquad n=aq-bp.
 \tag{131.P4}
\]
Assume, as a separate support hypothesis, that the physical inner ray is
primitive:
\[
 (m,b')=1.
 \tag{131.P5}
\]
Let
\[
 R_m=\operatorname {rad}(|m|),\qquad
 R_m^{\rm odd}=\operatorname {rad}(|m|_{\rm odd}).
 \tag{131.P6}
\]

Then the primitive arithmetic masks have the following minimal periods
in \(q\):
\[
\begin{array}{c|c|c}
 &\text{mask}&\text{primitive }q\text{-period}\\ \hline
\mathrm{M1}
 &\chi_4(b+q)\mathbf1_{(m,b+q)=1}
 &4R_m^{\rm odd}\\
\mathrm{M2}
 &\epsilon_{\rm sgn}\chi_4(|m|)
   \mathbf1_{(m,b+q)=1}
 &R_m .
\end{array}
\tag{131.P7}
\]
Consequently their minimal fixed-\(p\) periods in the supported
\(n\)-progression are \(4AR_m^{\rm odd}\) and \(AR_m\), respectively.
The conductor's \(4A|m|_{\rm odd}\) and \(A|m|\) are valid overperiods
and may be used for Fourier inversion.

This statement concerns only the arithmetic support mask.  To multiply
it by a physical analytic envelope and use Abel summation, one also
needs an extension \(\mathcal E_{i;r,p}(q)\), defined on the complete
residue progression, such that
\[
 \mathcal W_{i;r,p}(q)
 =w_{i,m}(q)\mathcal E_{i;r,p}(q)
 \tag{131.P8}
\]
and with all threshold, taper, star, shell, sign, reciprocal-alias, and
half-open owner variation quantitatively bounded.  Neither reviewed
artifact proves (131.P8) from the displayed \(\rho\)-dependent
pre-reassembly pieces.

Finally, every analytic interval remains one-sided:
\[
 n=aq-bp>0.
 \tag{131.P9}
\]
The point \(n=0\) is removed before any off-diagonal estimate and
retained once by the accepted determinant-diagonal owner.  Fourier
\(k=0\) and determinant \(n=0\) are distinct notions.

## 3. Proof or derivation

### 3.1 The weighted Möbius seam

The discovery report defines, schematically,
\[
\mathcal H(m,b')
=\sum_{\substack{\rho\mid m\\\rho\mid b'}}
 \mu(\rho)\,
 T_{\rho}^{\rm lit}(b'/\rho)\,\mathcal P^{\rm lit}(m,b'),
\tag{131.P10}
\]
where the common Stieltjes threshold becomes \(g\le t/b'\), but
\(T_{\rho}^{\rm lit}(b'/\rho)\), the \(v\)-star, and their owners still
depend on \(\rho\).  From (131.P1) one may conclude
\[
\sum_{\rho\mid(m,b')}\mu(\rho)\,E(m,b')
=\mathbf1_{(m,b')=1}E(m,b')
\tag{131.P11}
\]
only when the factor \(E\) is common to every \(\rho\).  No such equality
is displayed for (131.P10).  The missing exact identity is
\[
\sum_{\substack{\rho\mid m\\\rho\mid b'}}
\mu(\rho)T_{\rho}^{\rm lit}(b'/\rho)\mathbf1_\rho^{*}
=\mathbf1_{(m,b')=1}T_{\rm phys}^{\rm lit}(m,b'),
\tag{131.P12}
\]
with equality cases, stars, cells, and owners matched on both sides.

If (131.P5) is already accepted as the definition of the physical ray
support, the conductor's mask is a correct support mask.  Even then,
the analytic coefficient is known only on primitive \(b'\).  Fourier
separation requires a controlled extension to imprimitive residues;
different extensions have different variation and Fourier data.
Therefore the arithmetic kernel is exact, while the claimed full
physical factorization remains conditional on (131.P8) or (131.P12).

### 3.2 Primitive periods and the M1 transform

Coprimality depends only on primes dividing \(m\), hence on \(R_m\), not
on prime powers.  In M1, \(\chi_4(b')=0\) for even \(b'\), so the
two-part of \(m\) is already excluded and the minimal combined period is
\(4R_m^{\rm odd}\).  This proves (131.P7).  Using the conductor's valid
overperiod \(4M\), \(M=|m|_{\rm odd}\), CRT gives more precisely
\[
\widehat w_{1,m}(k)
=\frac{e(kb/(4M))}{4M}\,
G_4(k\overline M^{(4)})\,c_M(k\overline4^{(M)}).
\tag{131.P13}
\]
Because multiplication by \(\overline4^{(M)}\) does not change
\((M,k)\),
\[
c_M(k\overline4^{(M)})=c_M(k),
\tag{131.P14}
\]
so the conductor's abbreviated Gauss-times-Ramanujan formula is exact.
The fixed modulus-four factor vanishes for even \(k\) and has magnitude
\(2\) for odd \(k\).  Hence
\[
 |\widehat w_{1,m}(M)|
 =|\widehat w_{1,m}(3M)|
 =\frac{\varphi(M)}{2M}.
\tag{131.P15}
\]
Under \(q=(n+bp)/a\), these two labels give the physical quarter
frequencies \(\pm1/(4a)\).  The other odd Ramanujan modes remain.  This
is a linear fixed-\(4\) Gauss factor times a Ramanujan sum, not a
quadratic Gauss or Salié sum.

The normalized Fourier \(\ell^1\) cost is divisor-sized.  Indeed
\[
\sum_{k\bmod M}|c_M(k)|\le M\tau(M),
\tag{131.P16}
\]
and the four lifts from \(M\) to \(4M\), together with the factor
\(2/(4M)\), give \(O(\tau(M))\).  This licenses the support-mask
expansion but supplies no saving.

### 3.3 M2 fixed-\(p\), interlaced-\(p\), and even-\(b\) modes

For fixed \(p\), the signed numerator character is constant in \(q\).
Fourier inversion with the valid overperiod \(|m|\) gives
\[
\widehat w_{2,m}(k)
=\frac{\epsilon_{\rm sgn}\chi_4(|m|)}{|m|}
 e(kb/|m|)c_{|m|}(k),
\qquad
\widehat w_{2,m}(0)
=\epsilon_{\rm sgn}\chi_4(|m|)
 \frac{\varphi(|m|)}{|m|}.
\tag{131.P17}
\]
This is correct for even as well as odd \(b\).  It is a \(q\)-mask
average, not a statement about the full \(p\)-interlaced determinant
coordinate.

When \(p\) varies through active M2 numerators, \(p=2s\), and the outer
and inner signed character product is
\[
\chi_4(a)\chi_4(a+p)=e(p/4)=(-1)^s.
\tag{131.P18}
\]
If \(b\) is odd and \(q\bmod4\) is fixed, (131.P18) is a character of
\(n\bmod4A\), yielding the shifted modes recorded in the discovery
report.  Thus its odd-\(b\) shifted mode and the conductor's fixed-\(p\)
zero mode are different coordinate statements, not competing answers.

If \(b\) is even, write \(b=2^\nu b_0\), \(\nu\ge1\), \(b_0\) odd.  A
character \(e(kn/(4A))\) that changes sign when \(p\mapsto p+2\) would
require
\[
 bk\equiv-A\pmod {2A},
\tag{131.P19}
\]
which has no solution because the left side is even and \(A\) is odd.
The discovery no-go modulo \(4A\) is therefore exact.

There is an explicit larger-modulus repair.  On a sector
\(q\equiv q_0\pmod {2^{\nu+2}}\),
\[
 aq-n=bp=2^{\nu+1}b_0s,
\qquad
(-1)^s=e\!\left(\frac{aq-n}{2^{\nu+2}}\right).
\tag{131.P20}
\]
Thus the interlaced character can be represented with combined
\(n\)-period \(2^{\nu+2}A\), or by retaining one extra two-adic lift
coordinate.  Since \(2^{\nu+2}\) is not uniformly \(Y^\varepsilon\),
this refinement has no free completion cost.  It cannot be silently
folded into modulus \(4A\).

### 3.4 BV, packets, windows, and one-sided ownership

On a fixed \(p,\rho\), half-open support chart, the ordinary faces in the
discovery ledger are compatible with BV: \(1/m\) is fixed, the
determinant taper is monotone, and each Stieltjes threshold equality is
owned once.  Two global costs remain unproved:

1. the envelope extension/factorization (131.P8); and
2. the variation created when the \(O(1)\) active \(p\)-lifts interlace
   in determinant order.

The discovery report itself allows \(O(L)\) chart switches.  Therefore
its “green” BV conclusion is only cellwise; it is not a bounded-cost BV
decomposition of the full \(n\)-weight.

The same-denominator controls are exact after imposing \(n>0\).  For M1,
\(q=0,p=-t\) requires \(t\ge1\), and the taper sum for
\(t<D/W\) is
\[
\sum_{1\le t<D/W}\left(1-\frac{Wt}{D}\right)
\asymp \frac DW.
\tag{131.P21}
\]
For M2, \(q=0,p=-2j\) requires \(j\ge1\), and the phase at
\(c=(4h+1)b\) is cancelled by
\(\chi_4(a)\chi_4(a-2j)=(-1)^j\); its taper mass is likewise
\(\asymp D/W\).  The omitted \(t=0\) or \(j=0\) term is exactly
\(p=q=n=0\) and belongs to the separate determinant diagonal.

One such interior packet has the upper capacity
\[
D\frac{D/W}{L}K_D=Y^{30/48+o(1)}.
\tag{131.P22}
\]
Covering a \(p\)-span \(O(L)\) by intervals of length \(D/W\) uses at
most \(O(1+WL/D)\) intervals and recovers the raw upper capacity
\(DK_D\).  This proves neither that all covering cells are resonant nor
that their physical amplitudes are nonzero and same-signed.  At a fixed
common centre \(c\), exact packet alignment also imposes
\(c/b\in\mathbb Z\) for M1 or \(c/b\) odd for M2, so the per-ray packet
does not furnish a family-summed lower bound.

Finally, the \(k=0\) term in (131.P17) is supported throughout the
one-sided incomplete \(q\)-interval.  It neither inserts nor cancels the
single physical point \(n=0\).  Any completion must keep the lower
half-open face \(n>0\), subtract the diagonal once if it was introduced,
and retain the determinant-taper endpoint separately.

## 4. First doubtful or unproved step

The first doubtful step is discovery (131.6)--(131.9) as an **exact
factorized physical reassembly**.  The weighted \(\rho\)-sum contains
\(\rho\)-dependent \(T\), star, and owner data, so the bare Möbius
identity (131.P1) does not prove (131.P8) or (131.P12).  This precedes
the BV estimate, the Fourier expansion of the full weight, and every
mode estimate.

If physical primitivity is taken as an accepted support axiom, the first
remaining analytic gap is a controlled complete-progression extension
and a cross-lift BV/interlacing lemma.  After that, the first genuinely
estimative gap is still the actual family scalar
\[
\sum_r A_i(r)
\sum_{\substack{n>0\\\text{literal owners}}}
\mathcal W_{i,r}(n),
\tag{131.P23}
\]
not a positive energy and not a single fixed-\(p\) Fourier coefficient.

## 5. Required control tests and outcomes

| Seam | Hostile test | Outcome |
|---|---|---|
| physical reassembly | Try to factor (131.P10) using only \(\sum\mu\). | **Not proved.** The \(\rho\)-dependent \(T\), star, and owner require (131.P12). |
| primitive period | Remove prime powers from the conductor periods. | **Strict correction.** Minimal periods are (131.P7); the conductor moduli are valid overperiods. |
| M1 Gauss×Ramanujan | Perform CRT with both unit inverses. | **Pass.** Equations (131.P13)--(131.P16) certify the abbreviated formula and its divisor-sized \(\ell^1\) cost. |
| M1 shifted modes | Test \(k=M,3M\) and pull through \(n=aq-bp\). | **Pass on a fixed \(p\)-progression.** The full factor also has the remaining odd Ramanujan modes. |
| M2 fixed-\(p\) zero mode | Average the primitive \(q\)-mask. | **Pass with terminology correction.** It is an arithmetic Fourier average, not determinant \(n=0\). |
| odd-\(b\) interlaced M2 mode | Encode \(e(p/4)\) using fixed \(q\bmod4\). | **Pass.** It is a different coordinate statement from the fixed-\(p\) zero mode. |
| even-\(b\) M2 parity | Solve (131.P19), then enlarge the parity sector. | **No mode modulo \(4A\).** Repair (131.P20) costs period \(2^{v_2(b)+2}A\) or an extra two-adic coordinate. |
| BV ledger | Assemble fixed charts in determinant order. | **Cellwise pass; global fail/open.** Extension and \(O(L)\) interlacing variation remain. |
| M1/M2 same denominator | Start at \(t,j=1\), not zero. | **Pass per ray.** The excluded zero term is the separately owned diagonal. |
| window count and mass | Distinguish a cover upper bound from occupied coherent windows. | **Scope correction.** (131.P22) is per-window capacity; \(DK_D\) is a worst-case cover capacity, not a lower mass. |
| Salié interpretation | Inspect the complete arithmetic phase. | **No-go.** Only a fixed-\(4\) linear Gauss factor and Ramanujan sum occur; no quadratic or modular-inverse phase appears. |
| scalar versus energy | Attempt to infer a lower bound from a nonzero Fourier coefficient. | **Rejected.** The incomplete envelope and actual outer scalar can cancel; no Gram or operator norm is substituted. |
| per-ray versus cross-ray | Sum special-centre packets over the actual outer family. | **Open.** Their centres and coefficients vary with \(b\); no family saving or obstruction follows. |
| terminal verdict and scope | Test bank, obstruct, and global propagation. | **degenerate survives.** No fixed-block, global, M9, endpoint, bridge, or quarter promotion is licensed. |

No computation or external theorem was used.

## 6. Dependencies and exact artifacts used

This post-unmask review used only:

1. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md;
2. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/candidates/conductor_primitive_residue_fourier_kernel.md; and
3. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/resonant_packet_cross_ray_hostile_audit.md.

The accepted chart, scales, and owner scopes used here are exactly those
quoted in those three artifacts.  No sibling report, web source,
numerical experiment, or external theorem was used.  The audit was
100% analytical/algebraic.

## 7. Recommended state effect

**Revise before promotion.**

- Retain the conductor's fixed-\(p\) M1 and M2 primitive support-mask
  Fourier transforms, with “valid overperiod” replacing “natural
  period,” and with “arithmetic \(k=0\) coefficient” replacing
  “physical zero mode.”
- Retain the M1 quarter coefficients and the fixed-\(4\)
  Gauss-times-Ramanujan interpretation.  Explicitly reject any Salié or
  growing quadratic-Gauss interpretation.
- Retain the odd-\(b\) interlaced M2 mode and the exact even-\(b\)
  obstruction, but record the \(2^{v_2(b)+2}A\) repair or the extra
  two-adic coordinate and do not price it as \(Y^\varepsilon\).
- Do not promote discovery (131.6)--(131.9) as an exact factorized
  physical weight until (131.P12), the complete-progression envelope,
  and its owner-compatible BV extension are proved.
- Record the packet/window statements only as per-ray upper capacities.
  They prove neither a physical family lower bound nor an actual-family
  saving.
- Keep \(n=0\) under its separate diagonal owner and keep every Fourier
  \(k=0\) statement inside the one-sided \(n>0\) off-diagonal scope.

The Round-131 terminal label should remain **degenerate**, with the
actual signed family scalar (131.P23) as the first residual.  Make no
change to the accepted \(Y^{35/48}\) fixed-block bound, any global
exponent, M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge,
or the quarter target.

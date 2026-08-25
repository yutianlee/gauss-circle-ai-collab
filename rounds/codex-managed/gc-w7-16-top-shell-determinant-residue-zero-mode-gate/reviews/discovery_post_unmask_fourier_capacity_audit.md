# Round 131 post-unmask audit: primitive Fourier kernel, M2 modes, and capacity

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Review: `discovery_post_unmask_fourier_capacity_audit`

Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`

Status: independent review evidence only; no shared proof state is changed.

## 1. Result

The conductor's fixed-\(p\) primitive Fourier calculation is correct,
including its Gauss-times-Ramanujan factorization and normalized
Fourier-\(\ell^1\) cost.  It sharpens, but does not contradict, the
variable-modulus formula in the discovery report.

Fix an outer ray \((a,b)\), one physical increment \(p\), and put
\(m=a+p\), \(b'=b+q\).  For M1, with \(M=|m|_{\rm odd}\), the exact
physical arithmetic kernel

\[
 w_{1,m}(q)=\chi _4(b+q)\mathbf 1_{(M,b+q)=1}              \tag{131.R1}
\]

has period \(4M\) in \(q\), hence period \(4|a|M\) on its determinant
progression.  Its normalized DFT is

\[
 \widehat w_{1,m}(k)
 ={e(kb/(4M))\over4M}G_{4,M}(k)c_M(k),                    \tag{131.R2}
\]

where \(G_{4,M}\) is the fixed modulus-four Gauss factor and \(c_M\) is
the Ramanujan sum.  The zero mode vanishes, while

\[
 |\widehat w_{1,m}(M)|=|\widehat w_{1,m}(3M)|
 ={\varphi(M)\over2M}.                                    \tag{131.R3}
\]

These are the two natural quarter modes, but the remaining odd
Ramanujan modes are also present.

For M2, active \(m\) is odd and the exact fixed-\(p\) arithmetic kernel is

\[
 w_{2,m}(q)=\epsilon_{\rm sgn}\chi _4(|m|)
             \mathbf1_{(|m|,b+q)=1}.                      \tag{131.R4}
\]

It has a generically nonzero physical zero mode

\[
\widehat w_{2,m}(0)=\epsilon_{\rm sgn}\chi _4(|m|)
 {\varphi(|m|)\over|m|}.                                  \tag{131.R5}
\]

This corrects the discovery report's presentation of two M2 shifted
branches as the primary fixed-\(p\) modes.  On the active parity class
those two exponential representations coincide up to constants.  The
single quarter shift \(e(p/4)\) appears only after changing from fixed
\(p\), natural \(q\)-order to the interlaced \(p\)-coordinate.  If
\(b\) is odd and \(q\pmod4\) is fixed, it becomes the determinant mode
\(-|a|\bar b\pmod {4|a|}\); if \(b\) is even, no universal such mode
exists.

The modulus reconciliation is exact:

* the M1 carrier alone has period \(4|a|\) in \(n\);
* physical primitivity for fixed \(m\) has a period involving \(m\),
  minimally \(|a|\operatorname {rad}(|m|)\) and conveniently
  \(|a||m|\);
* their M1 product has minimal valid period
  \(|a|\operatorname {lcm}(4,\operatorname {rad}(|m|))\), while the
  conductor's \(4|a|M\) is a valid convenient common period;
* after physical reassembly and a subsequent Möbius re-expansion, a
  fixed divisor atom has the valid period
  \(|a|\operatorname {lcm}(4,\rho)\) used in the discovery report;
  for fixed-\(p\) M2 the factor \(4\) is unnecessary unless the
  interlaced numerator quarter character is also exposed.

Thus the discovery formula was a valid componentwise, sometimes
nonminimal period; the conductor formula is the recombined fixed-\(p\)
DFT.  Neither yields a single \(4|a|\)-periodic full interlaced physical
weight because \(m=a+p\) varies with \(p\).

The exact aligned-packet and capacity arithmetic is also correct after
one scope correction.  One packet has length \(R=D/W=Y^{3/48}\) and
outer-triangle capacity \(DK_DR/L=Y^{30/48+o(1)}\).  At most
\(C=1+WL/D=Y^{5/48+o(1)}\) product-window cells of length \(R\) cover a
total length \(O(L)\), so their **worst-case capacity** is the full
\(DK_D=Y^{35/48+o(1)}\).  This is not a theorem that all \(C\) cells are
simultaneously resonant and is not a lower bound for the actual family.

The promotable result is therefore the scoped fixed-\(p\) arithmetic DFT,
the exact M1/M2 mode distinction, the aligned-packet mass, and the
capacity/no-sparse-count ledger.  A full physical periodic/BV separation,
an actual resonant family estimate, a Salié sum, and any exponent gain
remain candidate-only.  The terminal Round-131 verdict remains

\[
 \boxed{\texttt{degenerate}}.                              \tag{131.R6}
\]

## 2. Exact statement and hypotheses

Let \((a,b)=1\), \(A=|a|\), fix one physical \(p\), and set

\[
 m=a+p,\qquad b'=b+q,\qquad n=aq-bp,qquad
 q={n+bp\over a}.                                          \tag{131.R7}
\]

All statements in this review are made after the Möbius atoms have
reassembled the physical primitive condition \((m,b')=1\).  No
threshold, taper, profile, reciprocal phase, or outer coefficient is
included in \(w_{i,m}\); these remain in the analytic envelope.

For M1 put \(M=|m|_{\rm odd}\).  Because \(\chi_4(b')=0\) for even
\(b'\), the two-adic part of \((m,b')=1\) is automatic on the support of
the character, giving (131.R1).  Define

\[
 \widehat w_{1,m}(k)={1\over4M}\sum_{q\bmod4M}
 w_{1,m}(q)e(-kq/(4M)).                                    \tag{131.R8}
\]

If \(\bar M_4M\equiv1\pmod4\), set

\[
 G_{4,M}(k)=\sum_{u\bmod4}\chi_4(u)
 e(-k\bar M_4u/4),
 \qquad
 c_M(k)=\sum_{\substack{v\bmod M\\(v,M)=1}}e(kv/M).      \tag{131.R9}
\]

The sign in the definition of \(c_M\) is immaterial because
\(c_M(-k)=c_M(k)\).

For M2, active \(m\) is odd and
\(\epsilon_{\rm sgn}\chi_4(|m|)=\chi_4(m)\).  With

\[
 \widehat w_{2,m}(k)={1\over|m|}\sum_{q\bmod |m|}
 w_{2,m}(q)e(-kq/|m|),                                    \tag{131.R10}
\]

the claim is

\[
 \widehat w_{2,m}(k)
 ={\chi_4(m)\over|m|}e(kb/|m|)c_{|m|}(k).                 \tag{131.R11}
\]

The interlaced M2 quarter-mode identity has additional hypotheses:
the outer and inner numerators are odd, \(p\) is therefore even,
\(b\) is odd, and one fixes \(q\equiv\gamma\pmod4\).  It is a change of
coordinate from (131.R10), not an additional fixed-\(p\) DFT mode.

For the capacity audit retain the frozen scales

\[
 W=Y^{7/16},\quad D=Y^{1/2},\quad L=Y^{1/6},\quad
 K_D=Y^{11/48+o(1)},\quad R={D\over W}=Y^{3/48},\quad
 C={WL\over D}=Y^{5/48}.                                  \tag{131.R12}
\]

The exact packet masses require an interior support chart; they assert
alignment of the displayed carrier, phase, and taper, not positivity or
nonvanishing of the remaining physical profile.

## 3. Proof and derivation

### 3.1 Verification of the Gauss-times-Ramanujan DFT

Shift \(x=b+q\) in (131.R8).  The Chinese remainder representation
modulo \(4M\) gives

\[
\begin{aligned}
 \widehat w_{1,m}(k)
 ={}&{e(kb/(4M))\over4M}
 \sum_{\substack{x\bmod4M\\(x,M)=1}}
 \chi_4(x)e(-kx/(4M))\\
 ={}&{e(kb/(4M))\over4M}
 \left[\sum_{u\bmod4}\chi_4(u)e(-k\bar M_4u/4)\right]
 \left[\sum_{v\bmod M}^{*}e(-k\bar4_Mv/M)\right],       \tag{131.R13}
\end{aligned}
\]

where \(4\bar4_M\equiv1\pmod M\).  Multiplication of reduced residues
by \(-\bar4_M\) permutes them, so the second bracket is \(c_M(k)\).
This proves (131.R2).

Only \(u=1,3\) contribute to the first bracket.  Directly,

\[
 G_{4,M}(k)=0\quad(k\ \text{even}),
 \qquad |G_{4,M}(k)|=2\quad(k\ \text{odd}).              \tag{131.R14}
\]

Since \(M\) and \(3M\) are odd and
\(c_M(M)=c_M(3M)=\varphi(M)\), (131.R3) follows.  The normalized
Fourier mass is harmless:

\[
\begin{aligned}
 \sum_{k\bmod4M}|\widehat w_{1,m}(k)|
 &={1\over M}\sum_{h\bmod M}|c_M(h)|\\
 &\le {1\over M}\sum_{d\mid M}d\,{M\over d}
 =\tau(M)\ll_\varepsilon Y^\varepsilon.                  \tag{131.R15}
\end{aligned}
\]

Here each class modulo \(M\) has exactly two odd lifts modulo \(4M\),
which supplies the first equality.  Formula
\(c_M(h)=\sum_{d\mid(M,h)}d\mu(M/d)\) supplies the inequality.

Under (131.R7), a Fourier factor \(e(kq/(4M))\) becomes a constant times
\(e(kn/(4aM))\).  Hence \(k=M,3M\) give the two quarter frequencies
\(1/(4a)\) and \(3/(4a)\), with the orientation sign carried by \(a\).
This verifies the conductor's M1 mode statement exactly.  It does not
delete the other odd \(k\)'s in (131.R2).

For M2, the same shift gives

\[
 \widehat w_{2,m}(k)
 ={\chi_4(m)e(kb/|m|)\over|m|}
 \sum_{x\bmod|m|}^{*}e(-kx/|m|),                          \tag{131.R16}
\]

which is (131.R11).  At \(k=0\) it gives (131.R5).  The same divisor
calculation gives normalized Fourier \(\ell^1\)-mass
\(O_\varepsilon(Y^\varepsilon)\).

### 3.2 Reconciliation of the moduli

On a fixed \(p\)-progression, \(n\mapsto n+aR_0\) sends
\(q\mapsto q+R_0\).  Therefore every valid \(q\)-period \(R_0\) gives
the \(n\)-period \(A R_0\).  The following periods are all exact, but
they refer to different factorizations.

1. The carrier \(\chi_4(b+q)\) has \(q\)-period \(4\), hence
   \(n\)-period \(4A\).
2. The primitive indicator has minimal \(q\)-period
   \(\operatorname {rad}(|m|)\), and \(|m|\) is a convenient period.
3. Their M1 product has minimal period
   \(\operatorname {lcm}(4,\operatorname {rad}(|m|))\).
   The conductor uses the nonminimal period \(4M\), needed only as a
   convenient CRT modulus for (131.R13).
4. If, after physical reassembly, one re-expands
   \(\mathbf1_{(m,b')=1}=\sum_{\rho\mid m}\mu(\rho)
   \mathbf1_{\rho\mid b'}\), then the M1 \(\rho\)-atom has period
   \(\operatorname {lcm}(4,\rho)\) in \(q\), hence
   \(A\operatorname {lcm}(4,\rho)\) in \(n\).  This is the discovery
   report's formula.  Even \(\rho\)-atoms vanish after multiplication by
   \(\chi_4(b')\).
5. The fixed-\(p\) M2 primitive kernel has no denominator-quarter
   carrier, so \(A\operatorname {rad}(|m|)\) is minimal and
   \(A|m|\) is the conductor's convenient period.  The discovery
   report's \(A\operatorname {lcm}(4,\rho)\) is still a valid common
   period but is nonminimal for this fixed-\(p\) M2 kernel.

The full sum is interlaced over \(p\), hence over different
\(m=a+p\).  There is no common period \(4A\) for the physical primitive
kernel.  Taking a formal least common multiple of all \(m\)'s would not
produce a useful Fourier/BV separation and would not control the
interlaced analytic envelope.

This also reconciles the discovery report's variation counterexample.
If primitivity is left in a putative \(4A\)-periodic envelope, its
variation can be linear on a \(q\)-interval.  Equations (131.R2) and
(131.R11) show the correct repair: put the fixed-\(p\) primitive factor
into a variable-modulus arithmetic kernel.  They do not repair the
variation of the remaining interlaced thresholds, profiles, aliases,
and lift owners.

### 3.3 The exact M2 zero/shifted-mode distinction

In the literal one-sided scalar, the active inner M2 factor is
\(\epsilon_{\rm sgn}\chi_4(|m|)=\chi_4(m)\).  For fixed \(p\), it is
constant in \(q\), which is why (131.R5), not a shifted quarter mode, is
the natural fixed-\(p\) Fourier coefficient.

If the outer numerator \(a\) and inner numerator \(m=a+p\) are active,
then both are odd and \(p\) is even.  On that parity class,

\[
 \chi_4(m)=\chi_4(a)(-1)^{p/2}=\chi_4(a)e(p/4).            \tag{131.R17}
\]

Thus the two formal exponentials used to represent \(\chi_4(m)\) do not
give two independent M2 modes: on even \(p\), \(e(p/4)=e(-p/4)\).
This is the precise correction to the two-branch statement in the
discovery report.

Now assume \(b\) is odd and fix \(q\equiv\gamma\pmod4\).  Since
\((a,b)=1\) and active M2 has odd \(a\), \(b\) is a unit modulo \(4A\).
From (131.R7),

\[
 p\equiv\bar b(a\gamma-n)\pmod {4A}.                       \tag{131.R18}
\]

Substitution in (131.R17) gives a constant on the \(\gamma\)-sector
times

\[
 e(-\bar b n/4)
 =e(h_2n/(4A)),\qquad h_2\equiv-A\bar b\pmod {4A}.         \tag{131.R19}
\]

This is the conditional interlaced shifted mode.  It is compatible with
the fixed-\(p\) zero mode because the two formulas Fourier-expand in
different orders.

If \(b\) is even, a determinant character giving the sign change under
\(p\mapsto p+2\) would require

\[
 bk\equiv-A\pmod {2A},                                     \tag{131.R20}
\]

which is insoluble because \(A\) is odd while
\(\gcd(b,2A)\) is even.  Hence there is no universal M2 mode modulo
\(4A\) in the even-\(b\) branch; the missing two-adic lift bit must be
retained.

The sign convention is exact algebraically:
\(\epsilon_{\rm sgn}\chi_4(|m|)=\chi_4(m)\).  It does not create a
top-shell sign-crossing packet.  If \(a\) and \(m\) have opposite signs
and \(|a|,|m|\asymp L\), \(b,b'\asymp D\), then

\[
 |ab'-mb|\asymp LD,
 \qquad {LD\over D^2/W}={WL\over D}=Y^{5/48},              \tag{131.R21}
\]

so the packet lies outside the determinant support.  The crossing at
\(m=0\) is a separately owned support face or lower numerator cell.

### 3.4 Variation and interlacing seam

The fixed-\(p\) arithmetic Fourier inversion is exact and (131.R15)
shows that it loses only \(Y^\varepsilon\).  This does not establish the
full separation

\[
 w_r(n)=\sum_\lambda \mathcal P_{r,\lambda}(n)
                         \mathcal V_{r,\lambda}(n)          \tag{131.R22}
\]

with a useful sum of Fourier \(\ell^1\)-mass times zero-extended BV norm.
The exact variation quantity that remains to be bounded is

\[
 \mathfrak B_r=
 \sum_\lambda\|\widehat{\mathcal P}_{r,\lambda}\|_1
 \left(\|\mathcal V_{r,\lambda}\|_\infty+
 \sum_n|\Delta\mathcal V_{r,\lambda}(n)|\right).           \tag{131.R23}
\]

The explicit determinant taper is monotone on a fixed sign/lift chart,
and a single displayed Stieltjes cutoff has one weighted birth/death.
Those local observations are sound.  The selected placeholders \(P\) and
\(T\), however, do not give the complete pullback of every frequency
floor, threshold star, reciprocal-alias boundary, moving support face,
and half-open owner.  Accordingly, the discovery report's asserted
\(O(Y^\varepsilon/L)\) total for all such physical faces is
candidate-only, not independently certified here.

There is also a genuine interlacing cost.  Natural numerator order and
determinant order are related by

\[
 p\equiv-\bar b n\pmod A.                                  \tag{131.R24}
\]

A profile whose natural \(p\)-order total variation is \(O(L^{-1})\)
can acquire \(\asymp L\) determinant-order jumps of size
\(O(L^{-1})\), hence variation \(O(1)\).  In unnormalized selector units
this is the \(O(L)\) switching count noted in the discovery report; after
the physical \(L^{-1}\) coefficient normalization it is \(O(1)\), which
still erases the desired full \(L\)-gain.  Retaining natural \(p\)-order
instead returns the aligned product-window resonances.

Thus fixed-\(p\) arithmetic completion is promotable, but the full
physical periodic/BV separation is not.

### 3.5 Aligned packets and the capacity ledger

For M1 take \(q=0\), \(p=-t\), \(n=bt\), and \(c/b\in\mathbb Z\).  The
phase and denominator-character product align, and the exact taper mass
is

\[
 \sum_{1\le t<R}\left(1-{t\over R}\right)
 ={R\over2}+O(1).                                          \tag{131.R25}
\]

For M2 take \(q=0\), \(p=-2j\), and \(c/b\) an odd integer.  Then
the determinant phase and numerator-character product are both
\((-1)^j\), so their product is one, and

\[
 \sum_{1\le j<2R}\left(1-{j\over2R}\right)
 =R+O(1).                                                   \tag{131.R26}
\]

These are exact compatibility and mass controls, not lower bounds after
the remaining physical amplitudes or outer coefficients are inserted.

One \(p\)-lift has post-inner scale \(K_D/L\).  Therefore

\[
\begin{array}{c|c|c}
\text{mechanism} & \text{capacity} & \text{exponent}\\ \hline
\text{no residue gain} & DK_D & 35/48\\
\text{formal square-root residue gain} & DK_D/\sqrt L & 31/48\\
\text{one aligned length-}R\text{ packet} & DK_DR/L & 30/48\\
\text{one term per ray} & DK_D/L & 27/48\\
\text{determinant target} & D & 24/48.
\end{array}                                                 \tag{131.R27}
\]

The accepted cell count gives at most \(C\) cells of length at most
\(R\), and \(CR=L\).  Summing their capacities without cancellation
returns \(DK_D\).  This is a worst-case capacity identity, not proof that
all cells are resonant.

The hostile continuous-window check is also correct.  A coherent packet
requires a width \(O(R^{-1})\) in \(c/b\); since \(c\asymp D^2\) and
\(b\asymp D\), each corresponding real \(b\)-window has length
\(O(R^{-1})\).  There are \(O(D)\) possible integral centre labels, so
their total continuous measure is \(O(D/R)=O(W)\); multiplication by the
packet mass \(R\) returns order \(D\).  On the integer \(b\)-lattice
each window is shorter than one, so occupancy and actual outer signs are
unresolved.  Neither a sparse-error saving nor a physical lower bound
follows.

Even if every ray were reduced to one term, outer Cauchy gives only
\(DK_D/L=Y^{27/48+o(1)}\).  A strict persistence improvement requires an
additional cross-ray power, and the determinant target needs the further
factor \(Y^{-3/48}=Y^{-1/16}\).

### 3.6 Exact complete-sum class

Equation (131.R2) is an exact **fixed-modulus-four Gauss factor times a
Ramanujan sum**.  It should be promoted with that wording.  It is not a
growing quadratic-Gauss sum: the Gauss factor has length four, and the
variable-modulus factor is linear Ramanujan arithmetic.  It is also not a
Salié sum.  The analytic phase retains the real reciprocal
\(c/(b+q)\); no fixed modulus, unit inverse \(\bar x\), integral additive
arguments, or boundary completion turns it into
\(e((ux+v\bar x)/Q)\).

Thus the prior blanket phrase “no Gauss sum” should be revised to “no
growing quadratic-Gauss or Salié bank.”  The elementary
Gauss-times-Ramanujan DFT is real and useful structural information, but
its natural M1 quarter coefficients and M2 zero coefficient prevent it
from supplying cancellation by character mean alone.

## 4. First doubtful or unproved step

The first unproved step is a quantitative version of (131.R22)--(131.R23)
for the complete physically reassembled and interlaced weight.  It must
simultaneously retain:

1. the variable primitive modulus \(m=a+p\) and its fixed-\(p\) DFT;
2. the permutation (131.R24) between natural numerator order and
   determinant order;
3. all Stieltjes thresholds, floors, stars, reciprocal aliases, taper
   faces, sign sectors, cells, and half-open owners; and
4. the real reciprocal phase outside the BV envelope.

Even if that separation is proved and gives an ideal per-ray collapse,
the next exact residual is still the actual signed family coefficient

\[
 \mathfrak R_i^{\rm res}(c)
 =\sum_{r=(a,b)}^{\rm lit}A_i(r)R_{i,r}^{\rm phys}(c),      \tag{131.R28}
\]

where \(R_{i,r}^{\rm phys}\) is the complete reassembled M1 quarter-mode
or M2 zero/interlaced-mode block.  No supplied statement gives either

\[
 |\mathfrak R_i^{\rm res}(c)|
 \ll DK_DY^{-\delta}
\]

or a matching lower bound for the actual coefficients.  This is the
first unavailable family-level identity and preserves the terminal
`degenerate` verdict.

## 5. Required controls and promotion audit

| Statement/control | Audit outcome | State scope |
|---|---|---|
| fixed-\(p\) M1 physical kernel (131.R1) | Exact after physical reassembly. | **Promotable.** |
| Gauss\(\times\)Ramanujan formula (131.R2) and \(\ell^1\) bound (131.R15) | Independently derived by CRT and divisor expansion. | **Promotable.** |
| M1 zero and quarter modes | Zero vanishes; \(k=M,3M\) have size \(\varphi(M)/(2M)\); other odd modes remain. | **Promotable.** |
| fixed-\(p\) M2 Ramanujan DFT and zero mode | (131.R11) is exact and (131.R5) is generically nonzero. | **Promotable.** |
| carrier modulus \(4A\) versus primitive modulus | Different factors; the exact common periods are listed in Section 3.2. | **Promotable clarification.** |
| discovery divisor modulus \(A\operatorname {lcm}(4,\rho)\) | Valid componentwise after physical reassembly; nonminimal for fixed-\(p\) M2. | **Promotable with scope correction.** |
| universal shifted M2 mode | False.  The fixed-\(p\) kernel has a zero mode; (131.R19) needs odd \(b\) and fixed \(q\pmod4\); even \(b\) leaves a parity bit. | **Reject universal claim; retain conditional identity.** |
| two independent M2 shifted branches | They coincide on active even \(p\). | **Revise to the single mode (131.R19).** |
| full physical periodic/BV ledger | Explicit local faces are plausible, but \(P,T\) pullback and interlacing cost are not proved. | **Candidate-only.** |
| same-denominator packet masses | (131.R25)--(131.R26) are exact on an interior chart. | **Promotable as controls, not lower bounds.** |
| opposite-sign M2 top-shell packet | Excluded by (131.R21), despite the algebraic sign identity. | **Promotable obstruction.** |
| one-window capacity \(30/48\) and ladder (131.R27) | Arithmetic is correct. | **Promotable capacity ledger.** |
| all-window \(35/48\) statement | Correct only as the worst-case \(CR=L\) capacity, not simultaneous resonance or a lower bound. | **Promotable with scope correction.** |
| Salié/growing quadratic-Gauss claim | No such form occurs.  Only fixed-modulus-four Gauss\(\times\)Ramanujan occurs. | **Promotable no-go.** |
| actual cross-ray saving or obstruction | Neither follows from marginal norms or aligned packets. | **Open; candidate residual only.** |
| global/M9 implication | None. | **No promotion.** |

All checks were analytical/algebraic.  No numerical experiment or
external theorem was used.

## 6. Dependencies and exact artifacts used

This post-unmask review compared:

1. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/candidates/conductor_primitive_residue_fourier_kernel.md`;
2. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md`;
3. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/resonant_packet_cross_ray_hostile_audit.md`;
4. the Round-131 `blind_statement.md`, active campaign, and the accepted
   Round-130 top-shell chart, support, and capacity scopes already cited
   by those three artifacts.

No sibling conclusion was accepted by vote.  Every DFT, modulus, mode,
and exponent calculation used in this review was independently checked.

## 7. Recommended state effect

Promote only the exact fixed-\(p\) primitive arithmetic kernel:

* M1 Gauss\(\times\)Ramanujan DFT (131.R2), its
  \(O_\varepsilon(Y^\varepsilon)\) normalized Fourier mass, vanishing
  zero mode, and natural quarter coefficients (131.R3);
* M2 Ramanujan DFT (131.R11) and nonzero physical zero mode (131.R5);
* the exact modulus reconciliation in Section 3.2;
* the conditional single M2 interlaced shift (131.R19), even-\(b\)
  parity no-go (131.R20), aligned-packet masses, sign-crossing exclusion,
  and the scoped capacity ledger.

Retain the full physical separation, useful interlaced BV estimate,
actual family-summed resonant bound, and any lower obstruction as open.
Close the round under `degenerate`, with (131.R28) as the first
family-level residual.  Make no complete fixed-block, global exponent,
M9-M1, M9-M2, endpoint, M9, bridge, or quarter promotion.

# Blind review: signed-inverse transport sector

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Role: strictly statement-only independent reviewer
- Graph hash: deliberately unavailable under the isolation instruction
- Context used: `protocol.md`; `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/review_packets/signed_inverse_transport_sector_statement_only.md`
- Date: 2026-08-29

## 1. Result

The five claims have the following verdicts.

1. **Verified for the full integer determinant fibres.** The proposed
   transport lowers the oriented determinant from \(h\) to \(h-1\),
   the canonical affine index changes by
   \(t\mapsto t+\nu_\omega(h)\), one has
   \(\nu_\omega(h)\in\{-1,0,1\}\), and the affine parity acquires
   \((-1)^{\nu_\omega(h)}\). This does not say that positivity or any
   literal selector is preserved; those restrictions can create
   births, deaths, and mask changes.

2. **Verified only after adding the stated oddness condition on \(U\),
   and refuted mode by mode.** Before Fourier splitting, the complete
   parity changes by the orientation-independent constant
   \((-1)^\varrho\). A lifted Fourier mode \(b=ma\), however, changes
   by
   \[
     (-1)^{\nu_\omega(h)}
     e\!\left(-\frac{\epsilon_\omega a\varrho}{q}\right)
   \tag{1.1}
   \]
   for the \(e(bS_0/U)\) convention, not generally by
   \((-1)^\varrho\). The constant identity is restored only by the
   complete Fourier reconstruction. The enumerated packet hypotheses
   do not separately state that \(U\) is odd; without odd \(U\), even
   the equality \((-1)^{S_0+t}=(-1)^S\) is false.

3. **The fixed-parameter small-signed-inverse sector is verified and is
   actually smaller than the proposed target, but the claimed final
   divisor-ledger consequence is not statement-only justified.** At
   fixed \((\kappa,u,m,q)\), after summing the retained Fourier modes
   absolutely, its size is
   \[
     O_\varepsilon\!\left(Q\kappa uX^\varepsilon
       \log(2q)\right)
     =O_\varepsilon(Qm\kappa uX^\varepsilon),
   \tag{1.2}
   \]
   with the logarithm absorbed in the permitted \(X^\varepsilon\).
   The empty and saturated cases obey the same estimate, both
   orientations cost only a constant, and the \(m^{-1}\) Fourier lift
   has been retained. However, no ranges or weights for summing
   \(\kappa,u,m,q\), no relation of those ranges to \(L\), and no
   divisor multiplicity ledger appear in the statement-only packet.
   Thus an \(O_{B,\varepsilon}(L^2X^\varepsilon)\) global conclusion
   cannot be audited or promoted from this packet.

4. **The two bare interval terminals and the isolated Fejer-difference
   component are locally target-safe, with qualifications made exact
   below.** A projective band contains
   \(O(uJ/q)\) supported integers \(v\). Each interval terminal therefore
   costs \(O(\kappa uX^\varepsilon)\) after the \(q/J\) Abel factor.
   Factoring the complete row as \(W(h)=F(h)A(h)\), the Fejer component
   can be written with the old complete row \(A(h-1)\); the harmonic
   sum of \(|F(h)-F(h-1)|/F(h-1)\) is
   \(O(1+\log(2L))\). It consequently costs
   \(O(\kappa uX^\varepsilon\log(2L))\) after the band count and Abel
   factor, hence is target-safe whenever the intended fixed-logarithm
   absorption is available. This proves nothing about coprimality,
   selector, positivity, carry, or affine-site terminals. The precise
   projective-band definition and the relation allowing
   \(\log(2L)\ll X^\varepsilon\) are also not explicitly written in the
   review packet; they must be present in the literal packet for the
   final simplified notation.

5. **No remaining cancellation is proved.** Fibre transport is a
   bijective algebraic relabelling, and the complete parity identity is
   not a termwise identity for a retained Fourier mode. Nothing stated
   relates transported endpoint coefficients, literal masks,
   square-root phases, or effective live-site sets. Before the Abel
   factor, the available pointwise scale for any unresolved component
   on a projective band is
   \[
      Y\kappa u\frac{J}{q}X^\varepsilon,
   \tag{1.3}
   \]
   whereas the required scale is
   \[
      Qm\kappa u\frac{J}{q}X^\varepsilon.
   \tag{1.4}
   \]
   The exact deficit is \(Y/(Qm)>1\). Equivalently, after multiplication
   by \(q/J\), the available and required scales are
   \(Y\kappa uX^\varepsilon\) and
   \(Qm\kappa uX^\varepsilon\). The first missing input is a signed
   common-range transport estimate for the actual endpoint/mask/phase
   product, including the carry factor (1.1) and all effective
   births/deaths.

The net review verdict is therefore **partial validation with a decisive
open seam**: Claims 1, the complete-reconstruction part of Claim 2, the
local part of Claim 3, and the narrowly isolated terms in Claim 4 are
valid. They do not imply the desired estimate for the complementary
transported packet.

## 2. Exact statement and hypotheses

The algebraic transport uses only

\[
 U=mq\mid u,\qquad (u,v)=1,\qquad
 \varrho v-\gamma U=1,\qquad
 |\varrho|\le (U-1)/2.
\tag{2.1}
\]

In particular, \(v\) is a unit modulo both \(U\) and \(q\). The
canonical representatives satisfy
\(0\le S_{0,\omega}(h)<U\). No positivity assumption is needed for the
full fibre calculation.

The parity conclusion additionally requires

\[
 U\ \text{odd}.
\tag{2.2}
\]

Condition (2.2) occurs in the wording of proposed Claim 2 but not in the
packet's initial list of hypotheses. It must be made an explicit literal
hypothesis. If \(U\) is even, then
\((-1)^{S_0+Ut}=(-1)^{S_0}\), not generally
\((-1)^{S_0+t}\).

The local sector estimate uses exactly these quantitative inputs from
the packet:

- a \(v\)-support contained in an interval of length \(O(u)\);
- \(|W_{v,\omega}(h)|\ll_\varepsilon\kappa X^\varepsilon\);
- at most \(O(Y)\) integer heights in the block;
- \(c_{mq}(ma)=m^{-1}c_q(a)\) and
  \(\sum_{(a,q)=1}|c_q(a)|\ll\log(2q)\);
- \(T_\varrho\le QmU/Y\).

For the projective-band calculations in Claim 4, the needed definition
is that the band is cut out by
\(J\le |a\bar v_q|_q<2J\), with \((a,q)=1\), or by an equivalent permutation of
\(O(J)\) unit residues modulo \(q\). This definition is referred to but
not displayed in the packet; the coefficient-mass formula strongly
suggests the unit restriction on \(a\), but the initial hypothesis list
does not state it separately. Under these conditions, the band count in
Section 3.4 is exactly justified.

For the Fejer calculation, write

\[
 F(h)=1-\frac{2\kappa gh}{\lceil L\rceil},
 \qquad
 \delta:=\frac{2\kappa g}{\lceil L\rceil},
 \qquad F(h)-F(h-1)=-\delta,
\tag{2.3}
\]

on the literal positive Fejer support. The argument below treats the
rest of the **complete** row as one object \(A(h)\), so that the
inherited bound controls \(F(h)A(h)\); it does not move an absolute value
inside the affine-site sum.

No hypothesis in the packet supplies a cross-height identity for an
endpoint coefficient, a literal mask, or a square-root phase. No ranges
for the final divisor summations are given. Those absences delimit the
verified conclusions.

## 3. Proof or derivation

### 3.1 Claim 1: determinant transport, index, and parity

For \(\omega=+\), put
\((S',w')=(S-\varrho,w-\gamma)\). Then

\[
 S'v-Uw'=Sv-Uw-(\varrho v-\gamma U)=h-1.
\tag{3.1}
\]

For \(\omega=-\), put
\((S',w')=(S+\varrho,w+\gamma)\). Then

\[
 Uw'-vS'=Uw-vS-(\varrho v-\gamma U)=h-1.
\tag{3.2}
\]

These are the proposed unified shifts
\((S',w')=(S-\epsilon_\omega\varrho,
w-\epsilon_\omega\gamma)\). Their inverses add the same shift, so they
are bijections between the full integer determinant fibres.

Because the two canonical representatives solve the corresponding
congruences,

\[
 S_{0,\omega}(h)-\epsilon_\omega\varrho
 -S_{0,\omega}(h-1)=U\nu_\omega(h)
\tag{3.3}
\]

for an integer \(\nu_\omega(h)\). The numerator in (3.3) has absolute
value strictly below \(3U/2\): the difference of the two canonical
representatives has absolute value at most \(U-1\), and
\(|\varrho|\le(U-1)/2\). Since it is divisible by \(U\),

\[
 \nu_\omega(h)\in\{-1,0,1\}.
\tag{3.4}
\]

If \(S=S_{0,\omega}(h)+Ut\), then

\[
 S'=S_{0,\omega}(h-1)+U(t+\nu_\omega(h)).
\tag{3.5}
\]

Thus the affine index is \(t'=t+\nu_\omega(h)\), and

\[
 (-1)^{t'}=(-1)^t(-1)^{\nu_\omega(h)}.
\tag{3.6}
\]

The corresponding equality for \(w\) follows either directly from
\(\varrho v-\gamma U=1\), or from uniqueness of \(w\) once \(S\) and
the determinant are fixed.

Equations (3.1)--(3.6) concern full integer fibres. If a literal site
requires \(S>0\), \(w>0\), an endpoint shell, or another selector, its
image need not satisfy that condition. Extending Claim 1 to the
positive or literal live subsets would therefore be an error.

### 3.2 Claim 2: complete parity versus a retained Fourier mode

Assume \(U\) odd. Since
\(S=S_{0,\omega}(h)+Ut\),

\[
 (-1)^S=(-1)^{S_{0,\omega}(h)+t}.
\tag{3.7}
\]

Under transport, \(S'=S-\epsilon_\omega\varrho\), whence

\[
 \frac{(-1)^{S'}}{(-1)^S}
 =(-1)^{-\epsilon_\omega\varrho}=(-1)^\varrho.
\tag{3.8}
\]

This is independent of orientation. The same result follows from the
canonical data: (3.3) gives

\[
 S_{0,\omega}(h-1)-S_{0,\omega}(h)
 =-\epsilon_\omega\varrho-U\nu_\omega(h),
\]

so the exponent change in complete affine parity is

\[
 -\epsilon_\omega\varrho-(U-1)\nu_\omega(h),
\]

whose second term is even.

Now Fourier-expand the anchor function on \(\mathbb Z/U\mathbb Z\).
For one character \(e(bS_0/U)\), the transported character times affine
parity has ratio

\[
 (-1)^{\nu_\omega(h)}
 e\!\left(\frac{b(S_{0,\omega}(h-1)-S_{0,\omega}(h))}{U}\right)
 =(-1)^{\nu_\omega(h)}
 e\!\left(-\frac{\epsilon_\omega b\varrho}{U}\right).
\tag{3.9}
\]

For the lifted mode \(b=ma\) and \(U=mq\), (3.9) is exactly (1.1).
It depends on the carry and on the retained mode, and is not generally
\((-1)^\varrho\). Summing every Fourier mode reconstructs the function
\((-1)^{S_0}\), at which point (3.8) again applies. Therefore a proof
may use the constant transport identity before the split or after full
reconstruction, but not for one retained mode.

### 3.3 Claim 3: signed-inverse sector count and local target

Inversion permutes the unit classes modulo \(U\), and choosing signed
least representatives is injective. Hence

\[
 \#\{v\bmod U:(v,U)=1,\ 0<|\varrho_U(v)|\le T\}\le2T.
\tag{3.10}
\]

An interval of length \(O(u)\) contains
\(O(u/U+1)=O(u/U)\) representatives of each class modulo \(U\), since
\(U\mid u\). Thus the number of supported integers \(v\) in the small
sector is

\[
 O\!\left(T_\varrho\frac{u}{U}\right).
\tag{3.11}
\]

There are \(O(Y)\) heights, two orientations, and each fixed row is
\(O_\varepsilon(\kappa X^\varepsilon)\). Including the exact lift and
summing the Fourier coefficient mass therefore gives

\[
\begin{aligned}
 |\mathcal S_{\rm small}|
 &\ll_\varepsilon
 Y\kappa X^\varepsilon
 \left(T_\varrho\frac{u}{U}\right)
 \frac1m\sum_{(a,q)=1}|c_q(a)|\\
 &\ll_\varepsilon
 Y\kappa X^\varepsilon
 \left(\frac{QmU}{Y}\frac{u}{U}\right)
 \frac{\log(2q)}m\\
 &\ll_\varepsilon Q\kappa uX^\varepsilon\log(2q).
\end{aligned}
\tag{3.12}
\]

At a fixed \(a\), replace the coefficient mass in the first line by
\(|c_q(a)|\); the same target follows because
\(|c_q(a)|\le\sum|c_q(a)|\). Since \(m\ge1\), (3.12) is within
\(Qm\kappa uX^\varepsilon\) after the stated logarithmic absorption.

If \(\lfloor QmU/Y\rfloor=0\), then \(T_\varrho=0\) and the sector is
empty. If the first entry in the minimum is selected, then
\(T_\varrho=(U-1)/2\le QmU/Y\); hence the same calculation already
covers the saturated sector. The fact that a unit inverse is never zero
covers the apparent lower endpoint. Both orientations were included as
a factor of two in the implicit constant.

Nothing in (3.10)--(3.12) counts the number of admissible tuples
\((\kappa,u,m,q)\), their weights, or their divisor multiplicities.
Those data are indispensable for a final \(L^2\) ledger, so that part
of proposed Claim 3 is not a consequence of the review packet.

### 3.4 Claim 4: projective-band count and interval terminals

Assume the projective band is
\(J\le|a\bar v_q|_q<2J\). Inversion followed by multiplication by the
unit \(a\) permutes the unit classes modulo \(q\), so the band contains
\(O(J)\) residue classes. An interval of length \(O(u)\) contains
\(O(u/q+1)=O(u/q)\) integers in each class because \(q\mid u\). Hence

\[
 \#\{v\text{ in the projective band}\}\ll \frac{uJ}{q}.
\tag{3.13}
\]

The complementary signed-inverse condition can only reduce this count.

The indicator of a nonempty integer interval has exactly one entry and
one exit under \(\Delta^-\). At either terminal the inherited row bound
is \(O_\varepsilon(\kappa X^\varepsilon)\). Therefore each of the two
terminals, summed over the band and multiplied by the Abel factor, is

\[
 \ll_\varepsilon
 \frac qJ\left(\frac{uJ}{q}\right)
 \kappa X^\varepsilon
 \ll_\varepsilon\kappa uX^\varepsilon.
\tag{3.14}
\]

Two orientations and the exact Fourier lift/coefficient mass only add a
constant and an \(m^{-1}\log(2q)\) factor. Thus the bare interval
terminals are safely inside the proposed target. This argument applies
only to the two changes of \(\mathbf1_{Y<h\le2Y}\), not to holes or
boundaries made by other literal predicates.

### 3.5 Claim 4: exact Fejer difference

On the positive Fejer support write the complete row as

\[
 W(h)=F(h)A(h).
\tag{3.15}
\]

Use the exact product difference

\[
 F(h)A(h)-F(h-1)A(h-1)
 =F(h)(A(h)-A(h-1))
  +(F(h)-F(h-1))A(h-1).
\tag{3.16}
\]

This choice is important: the isolated Fejer term contains the complete
old row \(A(h-1)\), not an separately absolutized subset of affine
sites. From the inherited bound,

\[
 |A(h-1)|\ll_\varepsilon
 \frac{\kappa X^\varepsilon}{F(h-1)}.
\tag{3.17}
\]

Let \(d=2\kappa g\) and
\(D_{h-1}=\lceil L\rceil-d(h-1)>0\). Whenever both consecutive Fejer
rows are live, \(D_{h-1}\ge d+1\), and

\[
 \frac{|F(h)-F(h-1)|}{F(h-1)}
 =\frac d{D_{h-1}}.
\tag{3.18}
\]

As \(h\) varies, the positive denominators form a subset of an
arithmetic progression of step \(d\). Integral comparison gives

\[
 \sum_h\frac d{D_{h-1}}\ll1+\log(2L).
\tag{3.19}
\]

Thus the isolated Fejer term has total size
\(O_\varepsilon(\kappa X^\varepsilon\log(2L))\) per
\((v,\omega)\). Applying (3.13) and \(q/J\) yields

\[
 O_\varepsilon(\kappa uX^\varepsilon\log(2L)),
\tag{3.20}
\]

before the harmless lift/coefficient mass. Under the intended
fixed-logarithm absorption, this is target-safe. Formula (3.16) leaves
the entire transported difference \(F(h)(A(h)-A(h-1))\); no part of
that remainder is estimated by (3.19).

### 3.6 Claim 5: unresolved terms and exact deficit

For one projective band, (3.13) gives \(O(uJ/q)\) rows. A remaining
component controlled only by the fixed-row bound can occupy \(O(Y)\)
heights. Its pre-Abel absolute capacity is therefore (1.3). To obtain
the claimed target after multiplication by \(q/J\), one needs (1.4).
Their quotient is exactly

\[
 \frac{Y\kappa u(J/q)}{Qm\kappa u(J/q)}=\frac{Y}{Qm}.
\tag{3.21}
\]

The hypothesis \(Qm<Y\) makes this a genuine loss. Claims 1--4 remove
neither this height factor nor its source. In particular:

- transport maps coefficient arguments to different endpoint data, but
  no relation between their values is stated;
- an inner literal mask may differ at the two transported sites;
- (1.1), not the constant \((-1)^\varrho\), is the multiplier of a
  retained Fourier mode;
- algebraic transport need not preserve positivity, so effective affine
  births and deaths remain;
- no derivative or Lipschitz estimate is stated for the full
  square-root phase together with the coefficient/mask product.

The first estimate that would close the seam is a signed bound of the
form

\[
 \left|\sum_{v\ {\rm in\ band}}\sum_h
       \sum_{t\ {\rm common}}
       \bigl(\mathcal A_{h,v,\omega}(t)
       -R_{h,v,\omega}\mathcal A_{h-1,v,\omega}(t+\nu_\omega(h))\bigr)
       z_{v,\omega}^{\,h}\right|
 \ll_\varepsilon Qm\kappa u\frac JqX^\varepsilon,
\tag{3.22}
\]

where \(R_{h,v,\omega}\) contains the exact modewise carry (1.1) and
\(\mathcal A\) contains the actual endpoint coefficients, masks, and
square-root phase. Separate estimates of the same total scale are also
needed for effective births and deaths. Equation (3.22), or an
equivalent direct signed Fourier estimate, is absent.

## 4. First doubtful or unproved step

The first invalid inference would be to replace the modewise factor
(1.1) by the complete-parity constant \((-1)^\varrho\). Fourier
reconstruction and selecting one mode do not commute with this pointwise
translation identity. Even if that error is avoided, the first missing
analytic estimate is (3.22): the packet supplies only pointwise row
control and hence misses the factor \(Y/(Qm)\).

There are three later, independently exact statement gaps:

1. Oddness of \(U\) must be explicit for Claim 2.
2. The projective-band definition and a relation making
   \(\log(2L)\) absorbable into \(X^\varepsilon\) must be explicit for
   the simplified form of Claim 4.
3. The summation ranges, weights, and divisor multiplicities needed for
   the final \(O_{B,\varepsilon}(L^2X^\varepsilon)\) ledger are absent,
   so the local sector estimate (3.12) cannot certify that global scale.

None of these gaps may be repaired by separately absolutizing the two
orientations or the common affine-site sum.

## 5. Required control test and outcome

### 5.1 Exact determinant control

Substitution in (3.1) and (3.2) gives \(h-1\) in both orientations.
The control passes. It also shows the limitation: if
\(0<S\le|\varrho|\) in the plus orientation with \(\varrho>0\), then
\(S'=S-\varrho\le0\). Thus fibre transport does not preserve the
positive cone.

### 5.2 Single-mode versus reconstruction control

Take \(U=5\), \(v=2\), whose signed least inverse is
\(\varrho=-2\), and use the plus orientation at \(h=1\). The canonical
representatives are \(S_0(1)=3\), \(S_0(0)=0\), so
\(\nu_+(1)=1\). Complete parity changes by
\((-1)^{-2}=1\), as (3.8) states. The single character \(b=1\), however,
changes by

\[
 -e(2/5)\ne1.
\tag{5.1}
\]

The control refutes termwise preservation and passes after summing the
complete Fourier reconstruction.

### 5.3 Empty and saturated sector controls

If \(QmU/Y<1\), then \(T_\varrho=0\) and (3.12) gives zero. If
\(T_\varrho=(U-1)/2\), then by definition
\((U-1)/2\le QmU/Y\), so the identical upper bound in (3.12) applies to
all unit inverse classes. Both controls pass; no separate endpoint loss
occurs.

### 5.4 Fejer-endpoint control

At the last pair of consecutive positive Fejer rows, write
\(D_h=\lceil L\rceil-2\kappa gh\ge1\). Then
\(D_{h-1}=D_h+2\kappa g\), and the last ratio in (3.18) is

\[
 \frac{2\kappa g}{D_h+2\kappa g}<1.
\tag{5.2}
\]

Thus there is no hidden \(1/F(h)\) blow-up when the product difference
is oriented as in (3.16); the full series is the harmonic sum (3.19).
This control passes for the isolated Fejer term.

### 5.5 Adversarial operator-class control

For each supported row in one projective band, let an abstract unresolved
height array be

\[
 W_{v,\omega}(h)=\kappa X^\varepsilon
                  \overline{z_{v,\omega}^{\,h}}
\]

on all allowed heights and zero elsewhere. Its normalized Abel/Fourier
sum has full positive mass at every coordinate, attaining the scale
\(Y\kappa uJ/q\) before the \(q/J\) factor. The outcome is a sharp
failure of a saving based only on the fixed-row norm.

This is solely an operator-class insufficiency test. It is not asserted
to satisfy the fixed literal endpoint formula, and it is not a lower
bound for the fixed literal coefficient. Its role is only to show that
pointwise boundedness plus transport cannot prove (3.22).

## 6. Dependencies and exact artifacts used

Only these artifacts were read:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/review_packets/signed_inverse_transport_sector_statement_only.md`.

No proof graph, proof draft, campaign file, strategy, Round-191 report,
control, candidate, kernel, sibling review, or earlier kernel was read.
No external source and no numerical computation was used.

## 7. Recommended state effect

**Revise; do not promote the complementary-packet estimate.** Subject to
independent seam checking, retain the full-fibre transport lemma,
\(\nu_\omega\in\{-1,0,1\}\), the complete-reconstruction parity
identity, the fixed-parameter small-inverse sector estimate, and the
narrow interval-terminal/Fejer estimates. Explicitly reject any
modewise replacement of (1.1) by \((-1)^\varrho\), any claim that fibre
transport preserves the literal positive support, and any inference of
the final \(L^2X^\varepsilon\) ledger without the omitted summation data.

The state should continue to record an open common-range transport
obligation with exact deficit \(Y/(Qm)\). Promotion requires a literal
proof of (3.22), including endpoint coefficients, masks, carry,
effective affine births/deaths, and square-root phase, plus the missing
global divisor ledger. None of the reviewed facts proves a parent,
bridge, quarter theorem, or global exponent.

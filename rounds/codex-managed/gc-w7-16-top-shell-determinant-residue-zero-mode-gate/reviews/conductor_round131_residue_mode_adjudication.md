# Conductor Round 131 adjudication: exact primitive modes, terminal interlacing seam

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`

Status: conductor adjudication; proof state changes only through the separately
validated State Patch.

## 1. Result

Round 131 closes under the unique label

\[
\boxed{\texttt{degenerate}}.
\tag{131.C1}
\]

There is a promotable finite support-mask kernel. Fix one primitive outer ray
\((a,b)\), one physical increment \(p\), put \(m=a+p\), and write
\(b'=b+q\), \(n=aq-bp\). After physical Möbius reassembly, M1 is an exact
fixed-modulus-four Gauss factor times a Ramanujan sum; its naive zero mode
vanishes but its two quarter modes have natural density. Fixed-\(p\) M2 is a
Ramanujan kernel with a generically nonzero \(q\)-arithmetic zero coefficient.
This coefficient is not the determinant point \(n=0\). Both transforms have
normalized Fourier \(\ell^1\)-mass \(Y^{o(1)}\).

This kernel gives no bank. The primitive modulus depends on \(m=a+p\), so the
full interlaced physical weight is not periodic modulo \(4|a|\). Moving
primitivity into a putative BV envelope creates linear variation; splitting it
arithmetically gives variable divisor moduli. The remaining physical lift
selector, thresholds, profiles, aliases, and owners have no proved low-cost
variation after the determinant-order permutation of \(p\).

Nor is there a physical obstruction. Exact one-sided same-denominator packets
show that character mean cannot force per-ray cancellation and that a resonant
packet has polynomial mass, but their centres depend on the outer denominator
and the retained physical amplitudes need not be nonzero or sign-aligned. No
family lower bound follows.

The first unresolved object is therefore the actual signed family sum of the
complete variable-modulus resonant ray blocks. The internal per-ray graded lane
is parked. A continuation must be a genuinely cross-ray theorem, with its
source and hypotheses audited separately.

## 2. Exact statement and hypotheses

Retain the frozen scales

\[
W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},\qquad
K_D=Y^{11/48+o(1)}.
\tag{131.C2}
\]

Fix one literal top shell \(b,b'\asymp D\), one moving-symbol stratum, one
orientation, and one M1 or M2 sign sector. Form every Stieltjes and Möbius
piece into the physical coefficient before introducing

\[
a'=a+p,\qquad b'=b+q,\qquad n=ab'-a'b=aq-bp.
\tag{131.C3}
\]

For each fixed outer ray, let \(\Lambda_{i,r}(n)\) be the actual set of
admissible \(p\)-lifts after all thresholds, taper, stars, cells, signs, and
half-open owners are imposed. Then \(\#\Lambda_{i,r}(n)=O(1)\), and the exact
one-sided scalar has the form

\[
\mathfrak O_{i,D}^{+}
=\sum_r^{\rm lit}A_i(r)
  \sum_{n>0}^{\rm lit}\sum_{p\in\Lambda_{i,r}(n)}
  H_{i;r,p}(n)C_{i;r,p}(n)
  e\!\left({cn\over\kappa_i b b'_{r,p}(n)}\right),
\tag{131.C4}
\]

where \(H\) is the exact reassembled non-character amplitude,
\(b'_{r,p}(n)=\{b(a+p)+n\}/a\), \(\kappa_1=1\), \(\kappa_2=4\), and

\[
C_{1;r,p}(n)=\sum_{\sigma=\pm1}\sigma e(\sigma b'/4),
\qquad
C_{2;r,p}(n)=\epsilon_{\rm sgn}\chi_4(|a+p|).
\tag{131.C5}
\]

Formula (131.C4) is an interface identity, not an estimate. In particular, the
bare identity \(\sum_{\rho\mid(a',b')}\mu(\rho)=\mathbf1_{(a',b')=1}\)
does not factor the \(\rho\)-dependent profiles, stars, or owners inside \(H\).
The equal-ray diagonal \(n=0\) is excluded and remains with its separate
accepted owner.

For a fixed \(p\), let \(M=|m|_{\rm odd}\). Once primitive support is taken as
the accepted physical-ray condition, the stripped support-character masks are

\[
w_{1,m}(q)=\chi_4(b+q)\mathbf1_{(M,b+q)=1},
\qquad
w_{2,m}(q)=\epsilon_{\rm sgn}\chi_4(|m|)
            \mathbf1_{(|m|,b+q)=1},
\tag{131.C6}
\]

with M2 restricted to active odd \(m\). No threshold, reciprocal phase,
profile, taper, \(\rho\)-weighted amplitude, star, owner, or outer coefficient
is included in (131.C6). Thus (131.C6) is not by itself a factorization of
\(H\).

## 3. Proof and derivation

### 3.1 Fixed-lift Fourier kernel

With normalized transforms, Chinese remaindering gives

\[
\widehat w_{1,m}(k)=
{e(kb/(4M))\over4M}G_{4,M}(k)c_M(k),
\tag{131.C7}
\]

where

\[
G_{4,M}(k)=\sum_{u\bmod4}\chi_4(u)
e\!\left(-{k\overline M^{(4)}u\over4}\right).
\]

The mod-four factor is zero for even \(k\) and has magnitude two for odd
\(k\). Hence

\[
\widehat w_{1,m}(0)=0,
\qquad
|\widehat w_{1,m}(M)|=|\widehat w_{1,m}(3M)|
={\varphi(M)\over2M}.
\tag{131.C8}
\]

Under \(q=(n+bp)/a\), these two modes give determinant frequencies
\(1/(4a)\) and \(3/(4a)\), up to constants. A convenient full period on
the zero-extended fixed-\(p\) determinant progression is \(4|a|M\), not
generally \(4|a|\).

For M2,

\[
\widehat w_{2,m}(k)=
{\epsilon_{\rm sgn}\chi_4(|m|)\over|m|}
e\!\left({kb\over|m|}\right)c_{|m|}(k),
\tag{131.C9}
\]

and therefore

\[
\widehat w_{2,m}(0)=
\epsilon_{\rm sgn}\chi_4(|m|){\varphi(|m|)\over|m|}.
\tag{131.C10}
\]

The divisor identity for Ramanujan sums gives

\[
\sum_{k\bmod R}|c_R(k)|\le R\tau(R),
\tag{131.C11}
\]

so both normalized expansions cost only \(Y^{o(1)}\). They provide no
saving because the coefficients in (131.C8) and (131.C10) are natural.

### 3.2 Exact modulus and M2 coordinate reconciliation

The M1 carrier alone has determinant period \(4|a|\). Primitivity for fixed
\(m\) has a period involving \(\operatorname{rad}(|m|)\); their product has
valid period

\[
|a|\operatorname {lcm}(4,\operatorname {rad}(|m|)).
\tag{131.C12}
\]

Equivalently, after physical reassembly and a subsequent Möbius re-expansion,
an M1 support atom \(\rho\mid m\) has valid determinant period

\[
|a|\operatorname {lcm}(4,\rho),
\tag{131.C13}
\]

while the weakest fixed-\(p\) M2 support-atom period is \(|a|\rho\). These
support identities do not remove any \(\rho\)-dependence from the weighted
physical amplitude.

Thus the carrier-level \(4|a|\) statement and the primitive variable-modulus
statement refer to different factors and are compatible. Since \(m=a+p\)
varies across the interlaced physical sum, neither statement supplies a
single useful modulus for (131.C4).

For active M2, \(a\) and \(m\) are odd, \(p\) is even, and

\[
\chi_4(a)\chi_4(m)=e(p/4).
\tag{131.C14}
\]

At fixed \(p\), (131.C10) is the natural \(q\)-arithmetic zero coefficient.
If instead \(b\) is odd
and \(q\pmod4\) is fixed, then the interlaced character in (131.C14) becomes
one determinant mode

\[
h_2\equiv-|a|\overline b\pmod {4|a|}.
\tag{131.C15}
\]

For even \(b=2^\nu b_0\), the determinant congruence leaves a two-adic lift
bit and no universal character of \(n\pmod {4|a|}\) exists. On a fixed
\(q\pmod {2^{\nu+2}}\) sector one may represent it using determinant period
\(2^{\nu+2}|a|\), or retain the extra lift bit. Since this two-adic factor can
be a power of \(Y\), it is not a free \(Y^\varepsilon\) repair. Thus there is
no coordinate-independent M2 shifted mode at the proposed modulus.

### 3.3 Physical variation seam

If primitivity is placed in the envelope, already a factor
\(\mathbf1_{3\nmid b+q}\) has variation \(\gg Q\) on a \(q\)-interval of
length \(Q\). Splitting primitivity by (131.C13) repairs this arithmetic
piece, but not the full envelope. Natural numerator order and determinant
order are related by

\[
p\equiv-\overline b,n\pmod {|a|}.
\tag{131.C16}
\]

A numerator profile of natural-order variation \(O(L^{-1})\) can incur
\(O(L)\) determinant-order switches of size \(O(L^{-1})\), hence total
variation \(O(1)\). This erases the desired full \(L\)-gain. The selected
record does not prove a smaller ledger after every threshold, star, floor,
alias, support face, and owner in (131.C4) is pulled back.

### 3.4 Aligned controls and capacity

Put

\[
R={D\over W}=Y^{3/48},
\qquad C=1+{WL\over D}=Y^{5/48+o(1)},
\qquad CR\asymp L.
\tag{131.C17}
\]

For M1, \(q=0\), \(p=-t\), \(n=bt\), and \(c/b\in\mathbb Z\) give an
aligned phase/carrier packet with taper mass \(R/2+O(1)\). For M2,
\(q=0\), \(p=-2j\), and odd integral \(c/b\) make the phase and
numerator-character product both \((-1)^j\), with taper mass \(R+O(1)\).
These are legal \(n>0\) controls on an interior positive-numerator chart.
Opposite top-size numerator signs are outside determinant support by the
factor \(WL/D=Y^{5/48}\).

The capacity ladder is

\[
\begin{array}{c|c}
\text{mechanism}&\text{capacity}\[1mm]\hline
\text{none}&DK_D=Y^{35/48+o(1)}\\
\sqrt L\text{ per ray}&DK_D/\sqrt L=Y^{31/48+o(1)}\\
\text{one length-}R\text{ packet}&DK_DR/L=Y^{30/48+o(1)}\\
\text{one term per ray}&DK_D/L=Y^{27/48+o(1)}\\
\text{target}&D=Y^{24/48}.
\end{array}
\tag{131.C18}
\]

The \(C\) cells recover \(DK_D\) only as a worst-case capacity identity;
it is not a theorem that every cell is simultaneously resonant. Conversely,
real resonant windows have total phase-space mass of order \(D\), so they
cannot be declared sparse without estimating their integer occupancy and
actual signs. The aligned centres vary with \(b\), so the packets are not a
family lower bound.

Even ideal one-term-per-ray collapse stops at \(Y^{27/48}=Y^{9/16}\), the
persistence threshold. A strict global improvement needs a further actual
cross-ray power. Reaching the determinant target needs the specific additional
factor \(Y^{-3/48}=Y^{-1/16}\).

### 3.5 Complete-sum classification

Formula (131.C7) is accurately described as fixed-modulus-four
Gauss\(\times\)Ramanujan arithmetic. It is not a growing quadratic-Gauss
bank. The analytic phase still contains the real reciprocal
\(c/(b+q)\); no fixed complete unit system, integral inverse phase, or
controlled boundary completion turns it into
\(e((ux+v\bar x)/M)\). Hence no Salié sum or Weil saving follows.

## 4. First doubtful or unproved step

The first unavailable assertion is an owner-compatible weighted reassembly or
complete-progression extension that factors the stripped mask (131.C6) from
the \(\rho\)-dependent physical amplitude in (131.C4). The bare Möbius
incidence identity does not prove this. Even conditional on such an extension,
one still needs a quantitative physical separation with total ledger

\[
\sum_\lambda\|\widehat{\mathcal P}_{r,\lambda}\|_1
\left(\|\mathcal V_{r,\lambda}\|_\infty+
\sum_n|\Delta\mathcal V_{r,\lambda}(n)|\right)
\tag{131.C19}
\]

small enough to preserve a power gain after variable primitive moduli and
the permutation (131.C16) are included. Even if (131.C19) gave the ideal
per-ray collapse, the next unresolved scalar would be

\[
\mathfrak R_i^{\rm res}(c)=
\sum_{r=(a,b)}^{\rm lit}A_i(r)R_{i,r}^{\rm phys}(c),
\tag{131.C20}
\]

where \(R_{i,r}^{\rm phys}\) is the complete reassembled M1 quarter-mode or
M2 zero/interlaced-mode block. No estimate or lower bound for (131.C20) is
proved.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal dictionary and physical reassembly | Pass for (131.C4) and the stripped support mask; a factorization of the weighted \(\rho\)-sum remains unproved. |
| fixed-lift support-mask Fourier algebra | Pass: (131.C7)--(131.C11) were independently rederived; no weighted-envelope factorization is inferred. |
| periodic/BV before Fourier | Refuted for one common \(4|a|\) modulus; variable-modulus arithmetic is exact, full physical BV is open. |
| shifted M1 mode | Pass: naive zero vanishes and natural quarter modes remain. |
| M2 mode | Pass with correction: the fixed-\(p\) arithmetic zero coefficient is nonzero; (131.C15) is conditional; even \(b\) retains a parity bit with a potentially large two-adic repair. |
| one-sided diagonal ownership | The blind \(p=q=n=0\) model is rejected from this target. The accepted equal-ray diagonal is separate and target-safe. |
| blind \(4\mid|a|\) M2 subcase | Algebraically conditional but physically inactive: the outer M2 character vanishes for even \(a\). It is not evidence for the actual M2 sector. |
| M1/M2 aligned packets | Pass only for the nonzero-determinant packets in Section 3.4; they are controls, not lower bounds. |
| resonant-window mass | Pass with scope: one window is \(30/48\); all cells recover \(35/48\) only as worst-case capacity. |
| scalar versus energy | Pass: neither a positive Gram nor a coefficient-blind operator substitutes for (131.C20). |
| Salié identification | No-go: only Gauss\(\times\)Ramanujan arithmetic is exact. |
| downstream scope | No fixed-block exponent, global exponent, M9 component, endpoint, bridge, or quarter promotion. |

The blind report's carrier-level M1 Fourier coset, generic BV warning, and
Salié no-go are retained. Its diagonal family and even-\(a\) M2 subcase are
not promoted. All calculations in this adjudication are analytical/algebraic;
no numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This adjudication uses:

1. `protocol.md` and the starting accepted graph;
2. `strategy/conductor_0823_full_proof_strategy.md`;
3. the Round-131 blind statement and three task reports;
4. `candidates/conductor_primitive_residue_fourier_kernel.md`;
5. `proofs/kernels/gc_w7_16_primitive_residue_fourier.md`;
6. the Round-131 post-unmask reviews; and
7. the accepted Round-130 synthesis and conductor adjudication.

No external source is imported.

## 7. Recommended state effect

Promote the exact fixed-\(p\) primitive Fourier kernel and a scoped
variable-modulus/interlacing method obstruction. Update the top-shell chart
and actual determinant-correlation nodes with the precise first residual
(131.C20).

Reject a common \(4|a|\)-periodic full weight, a low-BV primitivity envelope,
the naive M1 zero-mode test, a universal M2 shifted mode, character-forced
\(L\)-saving, a Salié interpretation, a sparse-resonance claim, the blind
diagonal obstruction inside the one-sided target, and any per-ray-to-cross-ray
inference.

Keep the complete fixed-block bound at \(Y^{35/48+\varepsilon}\), the
internally proved global exponent at \(1/3\), and every M9, endpoint, bridge,
and quarter obligation unchanged. Close this internal lane; the next eligible
step is an exact source-audited cross-ray mechanism map.

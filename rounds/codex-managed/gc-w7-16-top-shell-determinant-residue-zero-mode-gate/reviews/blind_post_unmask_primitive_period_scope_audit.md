# Round 131 post-unmask review: primitive-period and scope audit

## 1. Result

The fixed-\(p\) primitive Fourier kernel in the conductor candidate is
algebraically correct, including its normalized coefficients, its
Fourier \(\ell^1\) cost, the nonzero M1 quarter coefficients, and the
nonzero M2 zero coefficient. It is promotable only as a Fourier
expansion of the **stripped primitive-character kernel after physical
Möbius reassembly**. It is not a Fourier expansion of the complete
physical coefficient \(\mathcal H_{i;r,p}\), and it does not supply a
signed estimate.

Four scope corrections are required.

1. A common period \(4|a|\) applies only to the bare M1
   incidence/quarter carrier. Physical primitivity introduces the inner
   numerator \(m=a+p\). For a divisor atom \(\rho\mid m\), the M1
   determinant modulus is
   \[
   |a|\operatorname {lcm}(4,\rho).
   \]
   For M2, where there is no denominator-quarter carrier, the
   corresponding fixed-\(p,\rho\) modulus is the smaller
   \[
   |a|\rho.
   \]
   The first modulus is a safe common modulus for both branches, but is
   not the weakest M2 modulus.
2. The candidate moduli \(4M\) for M1, with \(M=|m|_{\rm odd}\), and
   \(|m|\) for M2 are legal completion moduli, not generally the
   fundamental periods. The radical periods are
   \(4\operatorname {rad}(M)\) and
   \(\operatorname {rad}(|m|)\) in \(q\), respectively. Their legal
   determinant completion moduli are \(4|a|M\) and
   \(|a||m|\).
3. The \(p=q=n=0\) diagonal model in the blind report is outside the
   frozen scalar. The exact physical scalar is
   \(\sum_{n>0}\mathcal W_{i,r}(n)\); the equal-ray \(n=0\) term is
   separately owned by the accepted diagonal. Therefore the blind
   report's claimed diagonal family obstruction at \(DK_D/L\) must be
   withdrawn. Nonzero same-denominator packets remain valid per-ray
   coherence controls, but they do not prove a family lower bound.
4. The blind report's M2 subcase \(4\mid |a|\) is vacuous in the active
   M2 sector. The actual M2 outer numerator \(A=|a|\) is odd. For odd
   \(b\), a fixed \(q\bmod4\) sector has the two shifted determinant
   modes described below; for even \(b\), no character of
   \(n\bmod4A\) represents the numerator alternation. At fixed \(p\),
   by contrast, the M2 numerator character is constant and the
   primitive kernel has a generically nonzero zero mode.

After these corrections, the Round-131 verdict remains
\(\boxed{\texttt{degenerate}}\): exact arithmetic transforms exist, but
the first unavailable statement is still a signed estimate for the
complete, interlaced, variable-modulus physical scalar. The capacity
ladder \(35/48\to31/48\to27/48\to24/48\) is correct, but none of its
intermediate entries is a physical lower bound.

## 2. Exact statement and hypotheses

Fix a primitive outer ray \(r=(a,b)\), write

\[
 A=|a|,\qquad s_a={a\over A},\qquad m=a+p\ne0,\qquad b'=b+q,
\qquad n=aq-bp,
\]

and first form the physical coefficient at the pair \((m,b')\). Only
after the \(\rho\)-pieces have been physically reassembled may its bare
primitive incidence be written

\[
 \mathbf1_{(m,b')=1}
 =\sum_{\rho\mid m}\mu(\rho)\mathbf1_{\rho\mid b'}.
 \tag{R131.1}
\]

Any \(\rho\)-dependent \(T\), Stieltjes threshold, star, floor, taper,
cell, sign, or owner remains attached to its physical atom. Formula
(R131.1) does not make those factors disappear.

### 2.1 Exact fixed-\(p\) M1 kernel

Put \(M=|m|_{\rm odd}\). Since \(\chi _4(b')=0\) for even \(b'\), the
primitive-character kernel is

\[
 w_{1,m}(q)=\chi _4(b+q)\mathbf1_{(M,b+q)=1}.
 \tag{R131.2}
\]

It has fundamental \(q\)-period \(4\operatorname {rad}(M)\) and admits
the legal completion modulus \(R_1=4M\). With

\[
 \widehat w_{1,m}(k)
 ={1\over4M}\sum_{q\bmod4M}w_{1,m}(q)e\!\left(-{kq\over4M}\right),
 \tag{R131.3}
\]

choose \(\alpha M\equiv1\pmod4\). Then

\[
 \widehat w_{1,m}(k)
 ={e(kb/(4M))\over4M}\,
 G_{4,M}(k)c_M(k),
 \qquad
 G_{4,M}(k)=\sum_{u\bmod4}\chi _4(u)e\!\left(-{k\alpha u\over4}\right).
 \tag{R131.4}
\]

Consequently

\[
 G_{4,M}(k)=0\quad(2\mid k),\qquad
 |G_{4,M}(k)|=2\quad(2\nmid k),
 \tag{R131.5}
\]

and

\[
 |\widehat w_{1,m}(M)|
 =|\widehat w_{1,m}(3M)|
 ={\varphi(M)\over2M}.
 \tag{R131.6}
\]

The inverse expansion has legal positive determinant modulus \(4AM\).
The two displayed indices contribute the determinant frequencies
\(1/(4a)\) and \(3/(4a)\); the remaining odd Ramanujan modes also
remain.

### 2.2 Exact fixed-\(p\) M2 kernel

In the active M2 sector \(A\) and \(m\) are odd. Put

\[
 \gamma_m=\epsilon_{\rm sgn}\chi _4(|m|)=\chi _4(m).
 \tag{R131.7}
\]

The primitive kernel is

\[
 w_{2,m}(q)=\gamma_m\mathbf1_{(|m|,b+q)=1}.
 \tag{R131.8}
\]

It has fundamental \(q\)-period \(\operatorname {rad}(|m|)\) and legal
completion modulus \(R_2=|m|\). Its transform is

\[
 \widehat w_{2,m}(k)
 ={\gamma_m\over|m|}
 e\!\left({kb\over|m|}\right)c_{|m|}(k),
 \tag{R131.9}
\]

so

\[
 \widehat w_{2,m}(0)
 =\gamma_m{\varphi(|m|)\over|m|}
 \ne0.
 \tag{R131.10}
\]

The corresponding legal positive determinant completion modulus is
\(A|m|\).

### 2.3 What is not included

Equations (R131.2)--(R131.10) contain only primitivity and the displayed
physical character. The reciprocal centre phase, exact profile,
Stieltjes cutoffs, lift selector, taper, support faces, and outer
coefficient remain outside. A useful physical separation requires fixed
\((r,p,\rho)\) divisor/lift/support charts, the accepted zero-extended
profile variation on each chart, all endpoint prices, and the reciprocal
exponential retained as the oscillatory phase. There is no single
\(4A\)-periodic/BV factorization of the interlaced full weight.

## 3. Proof and derivation

### 3.1 Physical Möbius order and exact periods

The discovery formula forms

\[
 \mathcal H_{i;r,p}(m,b')
 =\sum_{\substack{\rho\mid m\\\rho\mid b'}}
 \mu(\rho)T_{i;r,p,\rho,D}^{\rm lit}(b'/\rho)
 \sum_t c_{i,t}\sum_{g\le t/b'}^*
 {\chi _4(g)\over g}P_{i,m}(g)
 \tag{R131.11}
\]

before changing to determinant residues. This is the required physical
order. The identity (R131.1) is the bare incidence inside
(R131.11); it is not permission to replace the full \(\rho\)-weighted
sum by an unweighted primitive indicator. The candidate passes this
seam because it explicitly strips profiles, thresholds, taper, centre
phase, and outer coefficients from its Fourier kernel. Any future use
must preserve that scope.

For a fixed \(p,\rho\), increasing \(n\) by \(A\rho\) increases \(q\)
by \(s_a\rho\), so \(\mathbf1_{\rho\mid b+q}\) is invariant. The M1
quarter carrier requires an additional \(q\)-period \(4\). Hence the
divisor-atom determinant periods are

\[
 P_{1,p,\rho}=A\operatorname {lcm}(4,\rho),
 \qquad
 P_{2,p,\rho}=A\rho.
 \tag{R131.12}
\]

An even-\(\rho\) M1 atom is in fact zero because its \(b'\) is even;
the displayed M1 period is nevertheless a safe exact modulus. Summing
the primitive atoms gives the radical periods

\[
\begin{array}{c|c|c}
 &\text{\(q\)-period}&\text{positive \(n\)-period on fixed \(p\)}\\ \hline
\mathrm{M1}&4\operatorname {rad}(M)&
4A\operatorname {rad}(M)\\
\mathrm{M2}&\operatorname {rad}(|m|)&
A\operatorname {rad}(|m|)
\end{array}
 \tag{R131.13}
\]

and the conductor candidate uses the legal multiple moduli
\(4M,|m|\) in \(q\), hence \(4AM,A|m|\) in \(n\).

This also proves the failure of a common \(4A\) period. For example, if
\(3\mid m\), an admissible \(b'\) divisible by \(3\) becomes
\(b'+4s_a\), which is not divisible by \(3\), under
\(n\mapsto n+4A\). The primitive indicator changes. If primitivity is
put into the envelope instead, the sequence
\(\mathbf1_{3\nmid b'}\) has variation linear in the \(q\)-interval
length. Thus neither periodicity nor low BV is recovered.

### 3.2 Recheck of both DFTs

In M1, shift \(x=b+q\). The Chinese remainder representation modulo
\(4M\) gives

\[
 x\equiv uM\alpha+v4\beta\pmod {4M},
 \qquad
 \alpha M\equiv1\pmod4,\quad4\beta\equiv1\pmod M.
\]

Therefore the complete sum factors as

\[
 \sum_{u\bmod4}\chi _4(u)e(-k\alpha u/4)
 \sum_{\substack{v\bmod M\\(v,M)=1}}e(-k\beta v/M).
\]

The second factor is \(c_M(k\beta)=c_M(k)\), since \(\beta\) is a unit
modulo \(M\). This proves (R131.4). Directly summing \(u=1,3\) proves
(R131.5), while \(c_M(M)=c_M(3M)=\varphi(M)\) proves (R131.6).

The normalized Fourier \(\ell^1\) price is also correct. For each
residue modulo \(M\), exactly two of its four lifts modulo \(4M\) are
odd and each has \(|G_{4,M}|=2\). Hence

\[
 \sum_{k\bmod4M}|\widehat w_{1,m}(k)|
 ={1\over M}\sum_{k\bmod M}|c_M(k)|
 \le\tau(M).
 \tag{R131.14}
\]

For M2, the same shift gives (R131.9) immediately, and

\[
 \sum_{k\bmod|m|}|\widehat w_{2,m}(k)|
 ={1\over|m|}\sum_{k\bmod|m|}|c_{|m|}(k)|
 \le\tau(|m|).
 \tag{R131.15}
\]

Thus both completions cost only \(Y^{o(1)}\), but neither gives a
saving: M1 has natural-size shifted coefficients and M2 has a
natural-density zero coefficient.

### 3.3 M1 and M2 physical modes

For the bare fixed-\(p\) M1 carrier on \(n\bmod4A\), the blind report's
calculation is correct:

\[
 k\equiv\sigma s_a\pmod4,\qquad \sigma=\pm1.
 \tag{R131.16}
\]

After primitivity is included, the correct fixed-\(p\) modulus is
variable in \(m\), and the strong quarter indices are \(k=M,3M\) modulo
\(4M\) in \(q\). Along the physical progression their frequencies are
\(1/(4a)\) and \(3/(4a)\). The exact one-step \(q\)-phase difference is

\[
 {cm\over b'(b'+1)}+{\sigma\over4}.
 \tag{R131.17}
\]

This, including its integer aliases, is the physical shifted M1
resonance.

For M2, the fixed-\(p\) statement is (R131.10): the numerator character
is constant and the primitive kernel has a nonzero zero mode. A
different statement results only after interlacing \(p\) in determinant
order. On a fixed sign sector \(s'=\operatorname {sgn}(m)\), with odd
\(b\) and fixed \(q\equiv q_0\pmod4\), the two branches of
\(\chi _4(|m|)\) have

\[
 k_{2,\tau}\equiv-\tau s'\bar b\,A\pmod {4A},
 \qquad \tau=\pm1,\qquad b\bar b\equiv1\pmod4.
 \tag{R131.18}
\]

The \(q_0\)-sector indicator is a separate arithmetic factor; it may
broaden the Fourier support of the complete sector weight. At fixed
\(b'\), the corresponding \(p\)-increment phase is

\[
 -{c\over4b'}+{\tau s'\over4}.
 \tag{R131.19}
\]

If \(b\) is even, changing the active numerator position by \(2\)
changes its character sign and changes \(n\) by \(-2b\). A character
\(e(kn/(4A))\) could represent this only if

\[
 bk\equiv-A\pmod {2A}.
 \tag{R131.20}
\]

Because active M2 has \(A\) odd while \(\gcd(b,2A)\) is even, (R131.20)
has no solution. This confirms the even-\(b\) no-go.

The blind report's \(4\mid A\) computation was algebraically consistent
in an artificial parity class, but that class is absent from active M2
and must not be cited. Its general warning that no universal M2 shifted
mode follows was correct; the correct active replacement is the
fixed-\(p\) zero mode together with the odd-\(b\)/even-\(b\) interlacing
split above.

The unmasked sign convention also resolves the blind uncertainty:

\[
 \epsilon_{\rm sgn}\chi _4(|m|)=\chi _4(m)
 \quad(m\ne0\text{ odd}).
 \tag{R131.21}
\]

Thus sign crossing continues the actual character. It neither supplies
a cancellation bonus nor permits the two signs to be paired without the
profiles and reciprocal phases.

### 3.4 Correction of the diagonal model and capacity

The physical Round-131 scalar is

\[
 \mathfrak O_{i,D}^{+}
 =\sum_r^{\rm lit}A_i(r)\sum_{n>0}^{\rm lit}\mathcal W_{i,r}(n).
 \tag{R131.22}
\]

Therefore \(p=q=0\) has \(n=0\), belongs to the separately accepted
equal-ray diagonal owner, and is outside (R131.22). The blind report's
Sections 1 and 3.6 and its same-denominator control row incorrectly used
this diagonal as a support-matched obstruction to the frozen target.
That conclusion is retracted. In particular, it does not prove a
family-summed \(DK_D/L\) lower bound or obstruction.

The correct nonzero same-denominator controls are:

\[
\begin{array}{c|c|c}
 & (q,p,n)&\text{coherence condition}\\ \hline
\mathrm{M1}&(0,-t,bt),\ t>0&
e(ct/b)\text{ coherent when }c/b\in\mathbb Z\\
\mathrm{M2}&(0,-2j,2bj),\ j>0&
\chi_4(a)\chi_4(a-2j)=(-1)^j,\quad
e(cj/(2b))=(-1)^j\text{ when }c/b\text{ is odd}
\end{array}
 \tag{R131.23}
\]

with the literal sign owners retained and \(m=0\) separately excluded.
These packets prove that character zero mean does not force per-ray
vanishing. They do not align the actual outer coefficients and do not
prove a family lower bound.

The capacity ledger survives, but only as capacity:

\[
 R_D={D\over W}=Y^{3/48},\qquad
 C_D={WL\over D}=Y^{5/48},\qquad C_DR_D=L.
 \tag{R131.24}
\]

One resonant window has outer-triangle capacity

\[
 D R_D{K_D\over L}=Y^{30/48+o(1)},
 \tag{R131.25}
\]

and all \(C_D\) windows recover

\[
 DC_DR_D{K_D\over L}=DK_D=Y^{35/48+o(1)}.
 \tag{R131.26}
\]

Square-root residue cancellation would give \(Y^{31/48+o(1)}\); an
ideal one-term-per-ray estimate would give

\[
 {DK_D\over L}=Y^{27/48+o(1)}=Y^{9/16+o(1)};
 \tag{R131.27}
\]

the target is \(D=Y^{24/48}\). Thus the blind report's exponent
arithmetic was correct, but \(DK_D/L\) is a persistence threshold, not
a diagonal obstruction. Even after a full factor \(L\) per ray, a
further actual-family gain

\[
 {K_D\over L}=Y^{1/16+o(1)}
 \tag{R131.28}
\]

is required across the interlaced blocks and outer rays.

### 3.5 Salié scope

The exact transforms (R131.4) and (R131.9) are a fixed-modulus-four
Gauss factor times a Ramanujan sum, or a Ramanujan sum alone. The inverse
in the CRT factorization is a fixed change of variables; it is not a
summation variable paired with its modular reciprocal. The centre \(c\)
is real, the reciprocal phase is incomplete and variable-modulus, and
no phase \(ux+v\bar x\) on a complete unit group occurs. The blind
report, candidate, and discovery report therefore agree on the exact
Salié no-go.

## 4. First doubtful or unproved step

The first unavailable positive assertion is not an arithmetic DFT. It
is a simultaneous estimate for the complete physical resonant scalar
after:

1. physical Möbius reassembly;
2. variable primitive moduli and their Ramanujan modes;
3. the determinant-order lift selector;
4. the accepted BV profiles and all half-open faces;
5. the reciprocal stationary aliases; and
6. the actual outer coefficients

have all been kept joint.

In the notation of the discovery report, the residual is

\[
 \mathfrak R_i^{\rm res}(c)
 =\sum_{r=(a,b)}^{\rm lit}A_i(r)
   \sum_\nu^{\rm lit}\mathcal R_{i,r,\nu}(c).
 \tag{R131.29}
\]

Only

\[
 |\mathfrak R_i^{\rm res}(c)|
 \ll DK_DY^\varepsilon
 \tag{R131.30}
\]

is available. A fixed power saving requires an actual-vector estimate,
not a positive Gram, an arbitrary outer direction, a per-ray complete
sum, or a norm-only aligned model. The fixed-\(p\) DFT does not control
the \(p\)-interlacing: a profile with small variation in natural
\(p\)-order can have \(O(L)\) switching cost in determinant order.

To improve below the persistence threshold requires a total saving
strictly exceeding \(L=Y^{1/6}\). To reach the determinant target
requires \(Y^{11/48}\), equivalently the further
\(Y^{1/16}\) gain in (R131.28) after the ideal per-ray factor \(L\).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| DFT normalization | Pass: the CRT gives (R131.4) with the shift \(e(kb/(4M))\); the unit \(\beta\) leaves \(c_M(k)\) invariant. |
| M1 Gauss factor | Pass: it vanishes for even \(k\), has magnitude \(2\) for odd \(k\), and gives \(\varphi(M)/(2M)\) at \(M,3M\). |
| M2 Ramanujan factor | Pass: (R131.9) and the nonzero density mode (R131.10) are exact. |
| Fourier \(\ell^1\) price | Pass: (R131.14)--(R131.15) give at most the divisor factor, not a power saving. |
| Exact periods | Revise scope: \(4M,|m|\) are legal completion moduli; radical periods are smaller. In determinant order the moduli acquire \(A\), and divisor atoms have (R131.12). |
| Physical Möbius order | Pass with mandatory scope: form (R131.11) first; the DFT applies only to the stripped primitive-character kernel or to exact post-reassembly divisor charts. |
| Full \(4A\)-periodic/BV separation | Fail: primitivity changes under \(n\mapsto n+4A\), has linear BV if hidden in the envelope, and the lift selector can switch \(O(L)\) times. |
| M1 mode | Pass: bare quarter support is (R131.16), the primitive completion has natural-size \(M,3M\) coefficients, and the physical alias is (R131.17). |
| M2 active parity and modes | Corrected: \(A\) is odd, so the blind \(4\mid A\) subcase is void. Fixed \(p\) has a nonzero zero mode; interlaced odd-\(b\) sectors have (R131.18); even \(b\) has the no-go (R131.20). |
| M2 sign crossing | Pass after unmask: (R131.21) continues \(\chi_4(m)\); no artificial crossing cancellation is available. |
| Equal-ray diagonal | Fail for the blind obstruction: \(n=0\) is outside the one-sided target and separately owned. It must not support any Round-131 family obstruction. |
| Nonzero same-denominator packets | Pass as per-ray controls only: (R131.23) lies in \(n>0\) and shows shifted-mode coherence. |
| Capacity | Pass after reclassification: (R131.24)--(R131.28) are upper-capacity/persistence ledgers, not lower bounds. |
| Scalar versus energy | Pass: the surviving residual is (R131.29); no positive energy replaces it. |
| Salié eligibility | Pass no-go: the exact DFT is Gauss-times-Ramanujan, with no complete variable inverse phase. |
| No global or M9 promotion | Pass: no fixed-block, global, endpoint, bridge, M9 component, M9, or quarter conclusion follows. |

No computation or external source was used.

## 6. Dependencies and exact artifacts used

Only the following post-unmask packet was read:

1. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/blind_residue_mode_feasibility.md;
2. rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/synthesis.md;
3. rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/conductor_round130_post_inner_adjudication.md;
4. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/candidates/conductor_primitive_residue_fourier_kernel.md;
5. rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md.

No proof graph, proof draft, strategy file, sibling hostile report,
external source, or computation was used.

## 7. Recommended state effect

**Promote with scope correction** the conductor candidate's exact
fixed-\(p\) primitive Fourier kernels (R131.2)--(R131.10), including
their divisor-size Fourier \(\ell^1\) cost, the nonzero M1 quarter
coefficients, and the nonzero M2 zero coefficient. Record \(4M\) and
\(|m|\) as legal completion moduli and separately record the radical
periods and the determinant factors \(A\).

**Promote/revise** the physical separation statement only in its
post-reassembly, variable-modulus divisor/lift-chart form. For weakest
moduli, distinguish M1
\(A\operatorname {lcm}(4,\rho)\) from M2 \(A\rho\). Reject a common
\(4A\)-periodic factor with uniformly cheap BV envelope.

**Reject and supersede** the blind report's \(p=q=n=0\) Round-131
obstruction and its \(4\mid A\) M2 subcase. The former belongs to the
separate equal-ray diagonal owner; the latter is absent from active M2
parity. Retain only the corrected nonzero same-denominator controls and
the reclassified capacity ledger.

**Retain open** the actual reduced determinant correlation at terminal
status \(\texttt{degenerate}\), with (R131.29) as the first residual. No
complete exponent, global exponent, endpoint, bridge, M9 component, M9,
or quarter claim should change.

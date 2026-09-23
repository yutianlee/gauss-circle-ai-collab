# Blind tangent--Fejer commutator rederivation

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Task: blind_tangent_fejer_commutator_rederivation
- Role: statement-only independent rederivation and hostile falsification
- Context: protocol.md and the campaign blind_statement.md only
- Graph hash: not supplied in the statement-only packet and not accessed
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

**Result: the tangent chart, parity law, alternating finite-difference
identity, and algebraic decomposition are correct after making the summation
domain explicit. The frozen remainder estimate is false for the coefficient
class stated in the packet.**

The decisive no-go is coefficient-class exact, not merely a failure of one
proof technique. The packet assumes only

\[
\sum_N|c_N|^2\ll_\varepsilon L^2X^\varepsilon
\]

and allows an arbitrary specified divisor weight \(\lambda_N(d)\), with no
regularity across \(N\) or \(d\). Those hypotheses permit a unit-modulus,
single-divisor, phase-dechirped sequence for which one maximal stopped-chain
remainder is \(\gg L^4\), while the proposed bound is
\(L^3X^\varepsilon\). They also permit cancelling divisor openings for
which the physical sequence and its energy stay fixed but
\(\mathcal C_{R,T}\) and \(\mathcal R_{R,T}\) are arbitrarily large with
opposite signs.

Thus the commutator identity does not create cancellation. It transfers the
alternating character factor into the discrete variation
\(G(s)-G(s+1)\). For an allowed adversarial literal weight with
\(G(s)=(-1)^s\), that variation equals \(2(-1)^s\), so the external
\((-1)^s\) disappears and the remainder becomes positive at the full
Fejer capacity.

The asserted auxiliary input

\[
r_{s+1}-r_s=2m'\asymp L
\]

also has only its equality proved by the packet. The comparison
\(m'\asymp L\), an absolute bound for the opened weights, and the required
weighted incidence count are absent. Consequently the claim that the full
commutator is absolutely target-safe cannot be derived from the stated
hypotheses.

The recommended terminal disposition is a scoped
coefficient-class/tautology no-go. No target estimate or downstream theorem
is proved.

## 2. Exact statement and hypotheses

### 2.1 Necessary interpretation and exact chart domain

The divisor-opening line in the supplied packet contains a control
character in the typography of the word “odd.” I interpret it as

\[
c_N=\sum_{\substack{d\mid N\\d\ {\rm odd}}}\chi_4(d)\lambda_N(d),
\tag{2.1}
\]

which is also the only interpretation compatible with the later parity
claim.

After opening an ordered pair, the exact domain is

\[
d,d'\in\mathbb Z_{>0}\ {\rm odd},\qquad
m,m'\in\mathbb Z_{>0},\qquad
N=dm,\quad N'=d'm',\quad N'>N,\quad 2\mid N'-N.
\tag{2.2}
\]

Define

\[
s=\frac{d'-d}{2},\qquad v=m'-m.
\tag{2.3}
\]

Then \(s,v\in\mathbb Z\), \(v\) is even, and the map

\[
(d,m,d',m')\longleftrightarrow(d,m,v,s)
\tag{2.4}
\]

is a bijection on the opened incidence set, provided the reverse map is
required to satisfy

\[
d'=d+2s>0,\qquad m'=m+v>0.
\tag{2.5}
\]

All other tuples are assigned zero weight. The bare displayed sum
\(\sum_{d,m,v,s}\) is therefore correct only with (2.2)--(2.5), the
literal atom support, and \(v\) even understood.

### 2.2 Exact identities that survive rederivation

The product gap is

\[
\begin{aligned}
r_s
&=(d+2s)(m+v)-dm\\
&=dv+2s(m+v),
\end{aligned}
\tag{2.6}
\]

and hence

\[
\boxed{r_{s+1}-r_s=2(m+v)=2m'.}
\tag{2.7}
\]

Because \(d\) and \(d+2s\) are odd,

\[
\boxed{\chi_4(d+2s)\chi_4(d)=(-1)^s.}
\tag{2.8}
\]

For any finitely supported \(H:\mathbb Z\to\mathbb C\),

\[
\begin{aligned}
\sum_s(-1)^sH(s+1)
&=-\sum_s(-1)^sH(s),\\
\therefore\qquad
\sum_s(-1)^s\{H(s)-H(s+1)\}
&=2\sum_s(-1)^sH(s).
\end{aligned}
\tag{2.9}
\]

Taking \(H(s)=\beta_{R,T}(r_s)G(s)\), with full zero extension in
\(s\), proves exactly

\[
\Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\tag{2.10}
\]

with the two quantities displayed in the packet. No endpoint term is
missing: births, deaths, hard point values, and atom-support jumps occur in
\(G(s)-G(s+1)\), while the bandpass endpoints occur in the exact difference
of \(\beta\).

### 2.3 Frozen claim that is falsified

Let \(R_{j+1}=\min(2R_j,M)\), repetitions removed. Under only the packet's
hypotheses, the assertion

\[
\sum_j\mathcal R_{R_j,R_{j+1}}
\ll_\varepsilon L^3X^\varepsilon
\tag{2.11}
\]

is false, even with one outer real part, exact doublings only, unit-modulus
opened weights, a single active divisor per coefficient, and no endpoint
ambiguity.

The strongest valid general conclusion from (2.10) is the identity itself.
Neither summand has a target bound without extra actual-symbol hypotheses.

## 3. Proof or derivation

### 3.1 Multiplicity and parity audit

Since \(d,d'\) are odd, \(N\equiv m\pmod2\) and
\(N'\equiv m'\pmod2\). The even-gap condition makes \(N,N'\) have the
same parity, hence \(m,m'\) have the same parity and \(v=m'-m\) is even.
Conversely, odd \(d,d'\) and even \(v\) make

\[
r_s=dv+2s(m+v)
\]

even. Thus no parity branch is lost.

For a fixed opened ordered incidence \((d,m,d',m')\), (2.3) is unique.
Conversely (2.5) reconstructs the incidence uniquely. This is multiplicity
one at the **opened divisor-pair level**. It is not multiplicity one at the
physical \((N,N')\) level, because a physical integer can have several
active odd divisors; the double divisor opening intentionally retains all
such pairs.

The character check follows from
\(\chi_4(n+2)=-\chi_4(n)\) for odd \(n\). Iterating \(s\) times, including
negative \(s\), gives
\(\chi_4(d+2s)=(-1)^s\chi_4(d)\), and (2.8) follows because
\(\chi_4(d)^2=1\).

### 3.2 Finite identity and endpoint/cusp audit

Extend \(\beta_{R,T}\) to a continuous piecewise-linear function on
\(\mathbb R\) by the same formula. It is continuous at all three special
points:

\[
\beta(0)=0,\qquad
\beta(R^-)=\frac{T-R}{T}=\beta(R^+),\qquad
\beta(T)=0.
\tag{3.1}
\]

Its slopes are

\[
\frac{T-R}{RT},\qquad -\frac1T,\qquad 0.
\tag{3.2}
\]

Because \(R<T\le2R\),

\[
0<\frac{T-R}{RT}\le\frac1T.
\]

Therefore the exact global cusp-safe estimate is

\[
\boxed{
|\beta_{R,T}(x)-\beta_{R,T}(y)|
\le \min\!\left\{1,\frac{|x-y|}{T}\right\}.
}
\tag{3.3}
\]

In particular,

\[
|\beta(r_s)-\beta(r_{s+1})|
\le \min\!\left\{1,\frac{2m'}{T}\right\}.
\tag{3.4}
\]

This remains true when the step crosses \(0\), \(R\), or \(T\), and for
the final non-doubling link. There is no hidden delta mass at the cusp
\(R\).

Equation (2.9) is legitimate because \(G\) and hence \(H\) are finitely
supported after the literal zero extension. Expanding

\[
\beta(r_s)G(s)-\beta(r_{s+1})G(s+1)
\]

as

\[
\{\beta(r_s)-\beta(r_{s+1})\}G(s)
+\beta(r_{s+1})\{G(s)-G(s+1)\}
\tag{3.5}
\]

proves (2.10) with exactly one outer real part. Thus the finite algebra,
including every endpoint birth and death, is GREEN.

There is also an exact self-return after reindexing. Put

\[
S=\Re\sum_s(-1)^s\beta(r_s)G(s)=\frac12\Delta_{R,T},
\qquad
A=\Re\sum_s(-1)^s\beta(r_{s+1})G(s).
\tag{3.5a}
\]

Finite support gives

\[
\Re\sum_s(-1)^s\beta(r_{s+1})G(s+1)=-S.
\tag{3.5b}
\]

Consequently

\[
\boxed{
\mathcal C_{R,T}=S-A,\qquad
\mathcal R_{R,T}=S+A
=\Delta_{R,T}-\mathcal C_{R,T}.}
\tag{3.5c}
\]

Thus even if an independent argument made
\(\mathcal C_{R,T}\) absolutely target-safe, a target estimate for
\(\mathcal R_{R,T}\) would be equivalent, up to that already-paid error,
to the original physical link estimate. The commutator identity alone
does not lower the difficulty of the remainder; it self-returns exactly.
There is no endpoint exception to (3.5b), because the reindexed sum is
finite and zero-extended.

### 3.3 Why the advertised absolute commutator count is unavailable

From (3.4), the only general absolute estimate supplied by the packet is

\[
|\mathcal C_{R,T}|
\le
\sum_{d,m,v,s}
\min\!\left\{1,\frac{2m'}{T}\right\}|G_{d,m,v}(s)|.
\tag{3.6}
\]

The packet does not imply any of the three inputs needed to turn (3.6)
into \(L^3X^\varepsilon\):

1. It does not state \(m'\asymp L\). A sequence on an \(M\)-site interval
   can use the legal divisor \(d'=N'\), for which \(m'=1\), or the legal
   divisor \(d'=1\), for which \(m'=N'\).
2. It gives no pointwise or opened-energy bound for
   \(\lambda_N(d)\). The energy \(D_L\) controls only the already-summed
   coefficients \(c_N\), and arbitrarily large divisor terms may cancel
   inside (2.1).
3. It gives no weighted incidence estimate for
   \(\sum|G|\). A count of physical pairs does not control the absolute
   double divisor opening when its weights are unrestricted.

If one added all of

\[
m'\asymp L,\qquad
|\lambda_N(d)|\ll X^\eta,\qquad
\#\{d:\lambda_N(d)\ne0\}\ll X^\eta,
\tag{3.7}
\]

and assumed that all relevant integers are in a polynomial range in \(X\),
then a link has \(O(MT X^{O(\eta)})\) opened incidences, and (3.4) would
give the conditional ledger

\[
\frac{L}{T}\cdot MT X^{O(\eta)}
\asymp MLX^{O(\eta)}
\asymp L^3X^{O(\eta)}.
\tag{3.8}
\]

That explains the intended incidence-power calculation and shows that the
cusps themselves are harmless. But (3.7) is additional data, not a
consequence of the blind packet. Even (3.8) would bound only
\(\mathcal C\), not the remainder.

### 3.4 Bounded single-divisor counterexample to the frozen remainder

Let \(L=2^n\) with \(n\) large, set

\[
M=L^2,\qquad X=L^8,\qquad J=L^4,\qquad H=L^2,
\tag{3.9}
\]

so all scale inequalities in the packet hold and the stopped chain consists
of exact doublings from \(L\) to \(M\). Put \(P=M/2\), and take the
\(P\) odd sites

\[
N_a=1+2a,\qquad 0\le a<P.
\tag{3.10}
\]

Define

\[
c_{N_a}=e(-J\sqrt{N_a}),\qquad
\lambda_{N_a}(N_a)=\chi_4(N_a)c_{N_a},
\tag{3.11}
\]

and set every other \(\lambda_N(d)\) to zero. This is a legal exact
single-divisor opening because

\[
\chi_4(N_a)\lambda_{N_a}(N_a)=c_{N_a}.
\]

All active opened weights have modulus one, and

\[
D_L=P=\frac{L^2}{2}.
\tag{3.12}
\]

For a base site \(N_a\) and target \(N_{a+s}\), the chart has

\[
d=N_a,\quad m=1,\quad v=0,\quad d'=N_a+2s,\quad m'=1,\quad r_s=2s.
\]

The outer square-root phase is exactly dechirped. After extracting the
character product \((-1)^s\), the remaining opened factor is

\[
\boxed{G_a(s)=(-1)^s}
\tag{3.13}
\]

whenever \(0\le a+s<P\), and is zero otherwise. Consequently, on every
interior step,

\[
G_a(s)-G_a(s+1)=2(-1)^s,
\]

and its contribution to the remainder is

\[
(-1)^s\beta(r_{s+1})
\{G_a(s)-G_a(s+1)\}
=2\beta(2s+2)\ge0.
\tag{3.14}
\]

Birth terms with \(s<0\) have \(\beta(2s+2)=0\), and the final death term
is also nonnegative. Hence every stopped-chain remainder is nonnegative.

Consider the maximal link \(R=P,\ T=2P=M\). For
\(0\le s<P/4\),

\[
\beta_{P,2P}(2s+2)=\frac{s+1}{P}.
\]

For each such \(s\), at least \(P/2\) base sites have both \(G_a(s)\) and
\(G_a(s+1)\) nonzero. Therefore

\[
\begin{aligned}
\mathcal R_{P,2P}
&\ge
\sum_{s=0}^{P/4-1}\frac P2\cdot
2\frac{s+1}{P}\\
&=\sum_{h=1}^{P/4}h
\gg P^2
\asymp L^4.
\end{aligned}
\tag{3.15}
\]

Since all other link remainders are nonnegative,

\[
\sum_j\mathcal R_{R_j,R_{j+1}}\gg L^4.
\tag{3.16}
\]

Choose, for example, \(\varepsilon=1/16\). The claimed right-hand side is

\[
L^3X^{1/16}=L^{7/2}=o(L^4).
\tag{3.17}
\]

This analytically falsifies (2.11). It uses no large divisor weight, no
multiple-divisor cancellation, no non-doubling endpoint, and no numerical
experiment. It also shows the exact tautology: the character alternation
can be inserted into \(G\), and the commutator converts it into a positive
first difference.

### 3.5 Cancelling-opening counterexample to absolute component control

There is a second independent obstruction: \(D_L\) does not control
\(\mathcal C\) or \(\mathcal R\) separately because the divisor opening
may have cancellations invisible in \(c_N\).

Again take \(L=2^n>64\), \(M=L^2\), and the exact doubling chain. Choose an
integer \(q\asymp L^4\), set

\[
J=\frac{q}{\sqrt{15}-1},\qquad X=J^2,
\tag{3.18}
\]

and choose any \(H\) with \(L\ll H\le J^{1/2}\). Then

\[
e(J(\sqrt{15}-1))=1.
\]

Let

\[
\lambda_1(1)=1,\qquad
\lambda_{15}(1)=A,\qquad
\lambda_{15}(3)=A,
\tag{3.19}
\]

with all other opened weights zero and \(A>0\). Since
\(\chi_4(1)=1\) and \(\chi_4(3)=-1\),

\[
c_1=1,\qquad c_{15}=A-A=0,\qquad D_L=1.
\tag{3.20}
\]

The only positive-gap physical pair has zero coefficient, so
\(\Delta_{R,2R}=0\). Its two nonzero opened incidences have common gap
\(14\):

\[
\begin{array}{c|c|c|c|c}
d'&m'&s&r_s&r_{s+1}\\ \hline
1&15&0&14&44\\
3&5&1&14&24.
\end{array}
\tag{3.21}
\]

For every doubling link with \(R\ge L>44\),
\(\beta_{R,2R}(x)=x/(2R)\) at \(x=14,24,44\). The common phase equals
one, so direct substitution gives

\[
\begin{aligned}
\mathcal C_{R,2R}
&=
A\frac{14-44}{2R}
-A\frac{14-24}{2R}\\
&=-\frac{10A}{R}.
\end{aligned}
\tag{3.22}
\]

By the exact identity \(\Delta=\mathcal C+\mathcal R\),

\[
\mathcal R_{R,2R}=\frac{10A}{R}.
\tag{3.23}
\]

Summing the chain,

\[
\sum_j\mathcal R_{R_j,R_{j+1}}
=\frac{20A}{L}\left(1-\frac1L\right).
\tag{3.24}
\]

The energy remains \(1\), while \(A\) is unrestricted by the packet.
Thus the commutator and remainder components can be made arbitrarily
large, with exact cancellation in their physical sum. This disproves any
attempt to obtain absolute component bounds from \(D_L\) and physical
incidence count alone.

### 3.6 Phase and support-jump conclusion

The phase inside \(G(s)-G(s+1)\) changes when

\[
N'=(d+2s)m'
\quad\hbox{is replaced by}\quad
N'+2m'.
\]

The packet supplies no smallness or monotonic cancellation for

\[
e(J\sqrt{N'})-e(J\sqrt{N'+2m'}).
\tag{3.25}
\]

Likewise, zero extension correctly records support jumps but does not make
their total variation small. The examples above use only interior
alternation in (3.15) and exact finite atoms in (3.22), so endpoint
bookkeeping cannot repair the failed estimate.

## 4. First doubtful or unproved step

The first unproved step after the valid finite algebra is the replacement
of the exact identity

\[
r_{s+1}-r_s=2m'
\]

by

\[
r_{s+1}-r_s=2m'\asymp L.
\]

No factor-scale restriction in the blind packet implies \(m'\asymp L\).
Immediately after that, the intended incidence argument also requires
pointwise control and a divisor-incidence bound for the opened weights,
neither of which follows from \(D_L\).

Even if those missing assumptions were inserted so that
\(\mathcal C\) satisfied the conditional ledger (3.8), the first
unproved analytic step would remain a target bound for

\[
G(s)-G(s+1).
\]

The packet explicitly forbids assuming regularity across \(N\) or \(d\).
The unit-modulus counterexample (3.13) shows that this difference can
exactly cancel the external character and produce positive
\(L^4\)-capacity. Therefore the frozen estimate is not merely unsupported;
it is false under the stated hypotheses.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| malformed odd-condition typography | **REPAIR.** Interpret the control-character-corrupted token as \(d\ {\rm odd}\) and repair the source before formal use. |
| tangent-chart bijection | **GREEN with explicit domain.** It is multiplicity one on opened incidences when \(d+2s>0\), \(m+v>0\), \(v\) even, and literal support are retained. |
| even-\(v\) parity | **GREEN.** It follows from odd \(d,d'\) and even \(N'-N\). |
| character law | **GREEN.** \(\chi_4(d+2s)\chi_4(d)=(-1)^s\). |
| gap and step law | **PARTIAL.** \(r_s=dv+2s(m+v)\) and \(r_{s+1}-r_s=2m'\) are exact; \(m'\asymp L\) is not supplied. |
| alternating finite identity | **GREEN.** The factor \(2\), shift sign, and one outer real part are correct for finite zero extension. |
| commutator/remainder split | **GREEN as an identity.** All births, deaths, and endpoint jumps are included in the displayed differences. |
| remainder reindexing | **EXACT SELF-RETURN.** \(\mathcal R=\Delta-\mathcal C\); once \(\mathcal C\) is paid, estimating the remainder is the original link problem up to that paid term. |
| cusp and final-link control | **GREEN.** The bandpass is continuous and globally \(1/T\)-Lipschitz, including \(0,R,T\) and a non-doubling final link. |
| absolute commutator power | **FAIL under stated hypotheses.** The needed \(m'\)-scale, opened-weight bound, and weighted incidence count are absent; (3.19)--(3.24) give unbounded components at fixed \(D_L\). |
| phase-difference saving | **FAIL.** No regularity is assumed, and the dechirped phase in (3.11) makes the difference maximally aligned. |
| support-jump saving | **FAIL as a general inference.** Zero extension accounts for jumps exactly but supplies no small total variation. |
| bounded adversarial coefficient | **FALSIFIES TARGET.** The unit-modulus single-divisor family gives \(\mathcal R_{P,2P}\gg L^4\). |
| cancelling divisor opening | **FALSIFIES COMPONENT CONTROL.** \(D_L=1\) while \(\mathcal C=-\mathcal R\) is arbitrarily large. |
| unsigned/adversarial analogue | **NOT EXCLUDED.** The packet contains no actual Vaaler-profile or residual-selector property that prevents the false dechirped sequence. |
| numerical validation | **Not used.** Both counterexamples and every identity check are exact. |

## 6. Dependencies and exact artifacts used

Exactly two artifacts were read or used:

1. protocol.md, for authority, blind-validation discipline, false controls,
   promotion rules, and the seven-section report contract; and
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/blind_statement.md,
   for every definition and claim tested above.

No graph, state file, strategy, prior round, proof kernel, sibling report,
source card, web result, or computation was accessed or used.

## 7. Recommended state effect

**Recommended effect: retain the finite chart and decomposition after
typographical/domain repair, but reject the frozen remainder claim in the
stated coefficient class.**

Recommended terminal label:

\[
\boxed{\texttt{blind\_tangent\_remainder\_coefficient\_class\_no\_go}.}
\]

The reusable exact content is limited to:

- the opened-incidence bijection with explicit positivity and parity domain;
- \(v\) even;
- \(r_s=dv+2s(m+v)\) and \(r_{s+1}-r_s=2m'\);
- \(\chi_4(d+2s)\chi_4(d)=(-1)^s\);
- the alternating finite identity and exact split
  \(\Delta=\mathcal C+\mathcal R\); and
- the global cusp-safe Lipschitz bound (3.3).

Do not promote the absolute commutator bound or the remainder estimate.
A revised theorem would have to freeze a substantially narrower literal
coefficient class and prove, rather than assume:

1. the supported factor scale \(m'\asymp L\);
2. pointwise/opened-energy and active-divisor bounds for \(\lambda_N(d)\);
3. a complete weighted incidence estimate;
4. a special actual-symbol variation or correlation law controlling
   \(G(s)-G(s+1)\); and
5. a named step that fails for both counterexamples above.

Those additions would define a new statement. They cannot be imported into
the present blind packet after the fact, and no downstream proof or exponent
change follows from the valid finite identities alone.

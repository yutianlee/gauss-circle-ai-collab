# Round 181 statement-only blind rederivation

Campaign: m9-m1-hard-top-high-squarefree-radical-gate
Task: blind_hard_m1_radical_rederivation
Role: statement-only blind rederiver
Graph SHA-256: 6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16
Generated: 2026-08-27T08:01:37.561951+00:00
Status: candidate evidence only

## 1. Result

**No-go result for the displayed hypotheses, with a sharp-power low-radical lemma.**
Let
\[
\mathcal D_L=\{(h,n):h\asymp L,\ n\ {\rm odd},\ 4h<n<16h\},
\]
and let \(\operatorname{sf}(r)\) be the squarefree kernel of \(r\).

1. Grouping by the exact product \(r=hn\) proves (B181.2), retaining every
   sign, boundary condition, and product-fibre multiplicity.  Every positive
   \(r\) has a unique representation \(r=st^2\), with \(\mu^2(s)=1\).
2. For every \(\eta>0\), the complementary incidence count satisfies
   \[
   I_{\le L}:=\#\{(h,n)\in\mathcal D_L:\operatorname{sf}(hn)\le L\}
   \ll_\eta L^{3/2+\eta}.
   \tag{R181.1}
   \]
   The exponent is sharp: on a full standard dyadic shell,
   \(I_{\le L}\gg L^{3/2}\).  Thus the universal low-sector capacity is
   \(L^{3/2+o(1)}\mathcal X\).
3. The high-radical sector has exact arbitrary-coefficient capacity
   \[
   \sup_{|a|\le\mathcal X}
   \left|\sum_{\substack{(h,n)\in\mathcal D_L\\
   \operatorname{sf}(hn)>L}}
   \chi_4(n)a(h,n)e(\sqrt{Xhn})\right|
   =\mathcal X I_{>L}\asymp L^2\mathcal X.
   \tag{R181.2}
   \]
   Hence (B181.3) does not follow from the displayed support and pointwise
   bound.  The missing power is \(L^{1/2}\).
4. This obstruction is already present on the mandatory \(t=1\) face:
   there are \(\gg L^2\) admissible pairs for which \(hn\) is squarefree.
   Complex dechirping makes all of them positive.  Therefore the proposed
   fixed-\(t\) bound \(S_t^{3/4}\mathcal X\) is also false for arbitrary
   coefficients at \(t=1\), where \(S_1\asymp L^2\).
5. If a fixed actual coefficient family supplied those fixed-\(t\) bounds,
   their power summation would be sufficient:
   \[
   \sum_{t\ll\sqrt L}S_t^{3/4}
   \asymp L^{3/2}\sum_{t\ll\sqrt L}t^{-3/2}
   \ll L^{3/2}.
   \tag{R181.3}
   \]
   The first missing input is an actual-family relation producing
   cancellation across distinct squarefree radicals after product-fibre
   aggregation.  A concrete sufficient shifted-correlation relation is
   given in Section 3.7.

The adversarial examples below apply only to the arbitrary coefficient
class.  They imply no lower bound for the unspecified literal arithmetic
coefficient.

## 2. Exact statement and hypotheses

Fix \(L\ge2\), \(X>0\), and \(\mathcal X\ge0\).  Interpret \(h\asymp L\)
as a fixed dyadic-type interval, with endpoints constant multiples of
\(L\).  All upper bounds are uniform in those fixed constants.  The lower
controls are written for the standard convention \(L\le h<2L\); they
rescale to any full dyadic shell containing a fixed interior interval.
The only coefficient hypothesis is
\[
a:\mathcal D_L\longrightarrow\mathbb C,\qquad
|a(h,n)|\le\mathcal X.
\tag{R181.4}
\]
For \(r\ge1\), set
\[
C(r)=\sum_{\substack{h\mid r,\ h\asymp L\\
r/h\ {\rm odd},\ 4h<r/h<16h}}
\chi_4(r/h)a(h,r/h).
\tag{R181.5}
\]

For any subset \(E\subseteq\mathcal D_L\) determined by the product
\(hn\), its exact universal capacity is
\[
\sup_{|a|\le\mathcal X}
\left|\sum_{(h,n)\in E}\chi_4(n)a(h,n)e(\sqrt{Xhn})\right|
=\mathcal X\,\#E.
\tag{R181.6}
\]
Thus any result claimed from (R181.4) alone is an incidence estimate:
arbitrary complex coefficients can erase both the character and the phase
site by site.

The low conclusion (R181.1) contains the conventional harmless
\(L^\eta\) divisor loss.  The packet alone does not prove a naked
constant-only \(I_{\le L}\ll L^{3/2}\) bound.  This distinction does not
affect the power comparison.  The high conclusion (R181.2) is a genuine
\(\Theta(L^2\mathcal X)\) capacity statement.

## 3. Proof or derivation

### 3.1 Exact fibre identity and squarefree split

The sum is finite, so partitioning it by \(r=hn\) gives
\[
\begin{aligned}
\sum_{(h,n)\in\mathcal D_L}\chi_4(n)a(h,n)e(\sqrt{Xhn})
&=\sum_{r\ge1}e(\sqrt{Xr})
  \sum_{\substack{(h,n)\in\mathcal D_L\\hn=r}}
  \chi_4(n)a(h,n)\\
&=\sum_{r\ge1}e(\sqrt{Xr})
  \sum_{\substack{h\mid r,\ h\asymp L\\
  r/h\ {\rm odd},\ 4h<r/h<16h}}
  \chi_4(r/h)a(h,r/h)\\
&=\sum_r C(r)e(\sqrt{Xr}).
\end{aligned}
\tag{R181.7}
\]
The map \((h,n)\mapsto(r=hn,h)\) is a bijection from admissible sites to
the divisor incidences in (R181.5); no multiplicity is collapsed.

If \(r=\prod_p p^{\nu_p}\), define
\[
s=\prod_{\nu_p\ {\rm odd}}p,\qquad
t=\prod_p p^{\lfloor\nu_p/2\rfloor}.
\tag{R181.8}
\]
Then \(r=st^2\), \(s\) is squarefree, and prime-exponent parity proves
uniqueness.  This gives the exact low/high split.

### 3.2 Literal product support

If \(c_0L\le h\le c_1L\), the strict cone gives
\[
4c_0^2L^2<r=hn<16c_1^2L^2.
\tag{R181.9}
\]
Thus, whenever \(r=st^2\) occurs,
\[
s\ll L^2,\qquad t\ll \frac{L}{\sqrt s}.
\tag{R181.10}
\]
In the high sector \(s>L\), this yields \(t\ll\sqrt L\).  At fixed \(t\),
the possible \(s\)'s lie in an interval of length
\[
S_t\asymp \frac{L^2}{t^2}
\tag{R181.11}
\]
before imposing squarefreeness and \(s>L\); intersection with those
conditions can only shorten the interval.  In particular \(t=1\) is not
removable and has \(S_1\asymp L^2\).

### 3.3 Exact coefficient-insensitive capacity

Triangle inequality proves the upper half of (R181.6).  For the reverse
inequality, choose on \(E\)
\[
a(h,n)=\mathcal X\,\chi_4(n)e(-\sqrt{Xhn}),
\tag{R181.12}
\]
and set \(a=0\) off \(E\).  Since \(n\) is odd,
\(\chi_4(n)^2=1\), so every selected summand equals \(\mathcal X\).
This proves (R181.6), and simultaneously gives the character-erasure,
complex-dechirping, and arbitrary-site controls.

### 3.4 Low-radical incidence bound and sharpness

Let \(d(m)\) be the divisor function.  From (R181.9)--(R181.10),
\[
\begin{aligned}
I_{\le L}
&\le
\sum_{\substack{s\le L\\\mu^2(s)=1}}
\sum_{t\ll L/\sqrt s}d(st^2)\\
&\ll_\eta L^\eta
\sum_{s\le L}\left(1+\frac{L}{\sqrt s}\right)
\ll_\eta L^{3/2+\eta}.
\end{aligned}
\tag{R181.13}
\]
Here the exponent in \(d(m)\ll_\eta m^\eta\) is reduced if necessary,
since \(m=st^2\ll L^2\).  Equation (R181.6) gives the same upper bound
for the absolute value of the low-radical sum.

The \(3/2\) exponent cannot be improved universally.  Take integer triples
in the fixed boxes
\[
3\sqrt L\le d\le3.1\sqrt L,\quad
\tfrac13\sqrt L\le u\le0.34\sqrt L,\quad
\tfrac83\sqrt L\le v\le2.7\sqrt L,
\tag{R181.14}
\]
with \(d,v\) odd and \((u,v)=1\), and set \(h=du,\ n=dv\).  Then
\[
L\le h<1.054L,\quad 8L\le n<8.37L,\quad 4<n/h<16,
\tag{R181.15}
\]
and \(n\) is odd.  Since \((u,v)=1\), \(d=(h,n)\), so distinct triples
give distinct pairs, while
\[
\operatorname{sf}(hn)=\operatorname{sf}(d^2uv)
=\operatorname{sf}(uv)\le uv<0.918L<L.
\tag{R181.16}
\]
There are \(\gg\sqrt L\) choices for odd \(d\) and \(\gg L\) coprime
pairs \((u,v)\) in the other boxes.  For the latter, excluding common odd
prime divisors removes a proportion at most
\(\sum_{p\ {\rm odd}}p^{-2}<\sum_{m\ge1}(2m+1)^{-2}<1/4\), apart from
lower-order interval-end errors.  Thus this construction supplies
\(\gg L^{3/2}\) low-radical incidences.

### 3.5 High capacity and the \(t=1\) obstruction

The full cone has \(\asymp L^2\) sites: there are \(\asymp L\) choices
of \(h\), and \(\asymp L\) odd choices of \(n\) for each.  Taking
\(\eta<1/2\) in (R181.1) gives
\[
I_{>L}=\#\mathcal D_L-I_{\le L}\asymp L^2.
\tag{R181.17}
\]
Together with (R181.6), this proves (R181.2).  The capacity ledger is
\[
\begin{array}{c|c|c|c}
\text{sector}&\text{universal capacity}&\text{proposed target}
&\text{missing factor}\\ \hline
s\le L&L^{3/2+o(1)}\mathcal X&L^{3/2}\mathcal X&L^{o(1)}\\
s>L&\Theta(L^2\mathcal X)&L^{3/2}\mathcal X&L^{1/2}.
\end{array}
\tag{R181.18}
\]

There is a direct obstruction wholly on \(t=1\).  Use the interior
rectangle
\[
L\le h\le\tfrac54L,\qquad 8L\le n\le9L.
\tag{R181.19}
\]
Every point obeys \(4h<n<16h\).  First restrict both \(h\) and \(n\) to
be odd; this retains a fixed positive proportion of the rectangle and
eliminates the prime-\(2\) square obstruction.  Within these odd pairs,
exclude \(p^2\mid h\), \(p^2\mid n\), and \(p\mid(h,n)\), for odd primes
\(p\).  An elementary union bound leaves a positive proportion because
the main excluded proportion, relative to the odd sublattice, is at most
\[
3\sum_{p\ {\rm odd}}\frac1{p^2}
<3\sum_{m\ge1}\frac1{(2m+1)^2}<\frac34,
\tag{R181.20}
\]
and interval-end errors are \(o(L^2)\).  Every remaining \(h,n\) is
squarefree and the pair is coprime, so \(r=hn\) is squarefree:
\(s=r\asymp L^2>L,\ t=1\).  There are \(\gg L^2\) such sites.
Applying (R181.12) only there gives a \(t=1\) sum
\(\gg L^2\mathcal X\).

### 3.6 Fixed-\(t\) proposal

At fixed \(t\), divisor incidence gives coefficient-insensitive capacity
\[
\mathcal X
\sum_{\substack{s\ {\rm in\ support}\\s>L,\ \mu^2(s)=1}}
d(st^2)
\ll_\eta S_tL^\eta\mathcal X.
\tag{R181.21}
\]
Thus \(S_t^{3/4}\mathcal X\) asks for a factor \(S_t^{1/4}\) beyond size
and incidence.  At \(t=1\), (R181.19)--(R181.20) show that (R181.21) is
sharp in power, so the stronger estimate is false under (R181.4).
Conversely, if a fixed actual family supplied the stronger estimates,
(R181.3) would sum them to \(O(L^{3/2}\mathcal X)\).  The power summation
is valid; the fixed-direction input is missing.

### 3.7 First additional structural relation

With zero extension outside the fixed-\(t\) support and outside
squarefree \(s>L\), put
\[
z_t(s)=C(st^2)e(t\sqrt{Xs}).
\tag{R181.22}
\]
Writing \(N=S_t\) and \(H=\lfloor N^{1/2}\rfloor\), a concrete first
sufficient actual-family relation is
\[
\sum_{1\le q<H}\left|
\sum_s C((s+q)t^2)\overline{C(st^2)}
e\!\left(t\sqrt X(\sqrt{s+q}-\sqrt s)\right)
\right|
\ll_\eta HN^{1/2}L^\eta\mathcal X^2.
\tag{R181.23}
\]
The divisor estimate already supplies
\[
\sum_s|z_t(s)|^2\ll_\eta NL^\eta\mathcal X^2.
\tag{R181.24}
\]
Van der Corput differencing with \(H\asymp N^{1/2}\) would then give
\[
\left|\sum_s z_t(s)\right|^2
\ll_\eta \frac NH\left(N+HN^{1/2}\right)
L^\eta\mathcal X^2
\ll_\eta N^{3/2}L^\eta\mathcal X^2,
\tag{R181.25}
\]
hence the desired \(N^{3/4}L^\eta\mathcal X\) fixed-direction bound.
Relation (R181.23) is not claimed necessary term by term, but some
cross-radical relation of this kind is indispensable: it must couple
distinct product fibres after insertion of the character and phase, and
must forbid the sitewise twist (R181.12).  Pointwise size, support,
divisor multiplicity, and averaging only over \(t\) do not do so.

## 4. First doubtful or unproved step

There is no doubtful step in the finite universal no-go: the exact
capacity identity, the positive-density \(t=1\) construction, and the
power counts are elementary.

The first unproved step toward the proposed estimate for the fixed literal
coefficient family is (R181.23), or another comparably strong
cross-radical relation yielding the factor \(S_t^{1/4}\).  The packet
contains no literal coefficient formula from which such a relation can be
verified.  It would be invalid either to attribute the adversarial
coefficient to that special family or to assume that its unavailable
weights automatically cancel.  The fixed-family question remains open
under statement-only isolation.

## 5. Required control test and outcome

All controls were analytic; no numerical experiment was used.

| Control | Construction or check | Outcome |
|---|---|---|
| exact_product_fibre_identity | Bijection \((h,n)\leftrightarrow(r=hn,h\mid r)\) in (R181.7). | **Pass.** Exact signs, phases, and multiplicities are retained. |
| unique_squarefree_kernel_decomposition | Prime-exponent parity in (R181.8). | **Pass.** The representation \(r=st^2\) is unique. |
| literal_product_support | (R181.9)--(R181.11). | **Pass.** \(s\ll L^2,\ t\ll L/\sqrt s\), and \(s>L\) implies \(t\ll\sqrt L\). |
| low_radical_incidence_bound | (R181.13), with (R181.14) for sharpness. | **Pass at exponent precision.** \(L^{3/2+o(1)}\) is the sharp universal power; no lossless constant-only claim is made. |
| high_radical_capacity_ledger | (R181.6), (R181.17), and (R181.18). | **Target fails universally.** Capacity is \(\Theta(L^2\mathcal X)\), leaving \(L^{1/2}\). |
| fixed_t_power_summation | Equation (R181.3). | **Pass as an implication.** The fixed-\(t\) targets sum correctly, but are not consequences of the hypotheses. |
| perfect_square_centre_control | Take \(X=M^2\), odd \(h\asymp L\), \(n=9h\), and \(a(h,9h)=\mathcal X\chi_4(9h)\). Then \(r=(3h)^2,\ s=1\), and \(e(\sqrt{Xr})=1\). | **Pass.** A square-centred low-radical family is exactly coherent; the phase alone gives no universal saving. |
| high_radical_t1_control | Positive-density squarefree coprime pairs in (R181.19)--(R181.20). | **Target fails universally at \(t=1\).** Dechirped size is \(\gg L^2\mathcal X\). |
| complex_dechirped_control | Insert \(e(-\sqrt{Xhn})\) as in (R181.12). | **Pass.** The phase is erased exactly for every \(X>0\). |
| arbitrary_coefficient_control | Choose each site independently at the pointwise bound. | **Pass.** The supremum is exactly \(\mathcal X\) times incidence. |
| character_erasure_control | Insert \(\chi_4(n)\); for odd \(n\), \(\chi_4(n)^2=1\). | **Pass.** The character cannot protect the arbitrary complex class. |
| boundary_control | For fixed \(h_0\), the odd neighbors \(4h_0+1,16h_0-1\) are included, while \(4h_0-1,16h_0+1\) are excluded; exact endpoints are excluded by strictness and are even. | **Pass.** Grouping neither closes nor moves a cone edge. |
| one_site_one_fibre_controls | One site gives its unique \(C(h_0n_0)e(\sqrt{Xh_0n_0})\). For a fibre, take odd \(k\) and \(L=5k\): the sites \((5k,63k)\) and \((7k,45k)\) both have \(h\in[L,2L)\), lie strictly in the cone, and have the same product \(315k^2=35(3k)^2\). | **Pass.** A singleton is counted once; the two sites form the exact signed sum in one \(C(315k^2)\). |
| literal_unknown_quarantine | No formula for the literal family or its unavailable weights, floors, stars, signs, and crossings was inferred. | **Pass.** Adversarial lower examples are not attributed to the literal family. |
| downstream_scope | No BAL, UNBAL, smooth-M1, GAR, M2, bridge, assembly, or parent-closure claim is used. | **Pass.** Only the finite displayed implication is decided. |
| exponent_quarantine | The deficit is recorded as \(L^{1/2}\); it is only conditionally \(X^{1/12}\) if a separate regime imposes \(L\asymp X^{1/6}\). | **Pass.** No Gauss-circle exponent or downstream closure is claimed. |

## 6. Dependencies and exact artifacts used

Only these artifacts were read or used:

1. protocol.md.
2. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/blind_statement.md.
3. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/briefs/blind_hard_m1_radical_rederivation.md.

No proof graph, active campaign, strategy file, prior round, sibling
artifact, source, web result, or conductor analysis was used.  No
computation was used.

## 7. Recommended state effect

**Revise/reject the universal mechanism; retain the fixed-family
question.**  Recommend retaining as candidate evidence the exact
product-fibre identity, unique squarefree split, literal support bounds,
the power-sharp \(L^{3/2+o(1)}\mathcal X\) low-sector estimate, and the
fixed-\(t\) power summation.  Recommend rejecting any claim that (B181.3),
or the fixed-\(t\) \(S_t^{3/4}\mathcal X\) estimate, follows from support
plus \(|a|\le\mathcal X\): the \(t=1\) face retains
\(L^2\mathcal X\) capacity.

For the one fixed literal coefficient family, recommend **no promotion
and no rejection** from this report.  Its next admissible proof input must
be an audited actual-direction relation that rules out character/phase
dechirping and gives cross-radical contraction, for example (R181.23).
No shared proof state or downstream claim should change merely from the
adversarial capacity example.

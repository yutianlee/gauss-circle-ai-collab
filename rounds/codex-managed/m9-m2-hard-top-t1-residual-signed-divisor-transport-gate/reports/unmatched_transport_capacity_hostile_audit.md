# Round 164 hostile audit: unmatched residual transport capacity

## Result

The residual sign masses are neither automatically balanced nor
transport-cheap.  The exact conclusion is the route-scoped no-go

\[
 \boxed{\texttt{hard\_top\_t1\_residual\_transport\_no\_go}.}
\]

For a supported squarefree (N=2^{\nu_N}M), with (M) odd and
\(\nu_N\in\{0,1\}\), let \(\rho_N(d)\) be (1) on every odd divisor
when no Round-163 pair is selected and, when
\(\{p_N,q_N\}\) is selected, let

\[
 \rho_N(d)={\bf1}_{\{{\bf1}_{p_N\mid d}={\bf1}_{q_N\mid d}\}}.
\tag{164.H1}
\]

Thus the residual contains precisely the no-pair incidences and the
neither/both incidences.  The XOR sector is removed once, not twice.
Put

\[
 \mathscr R_N=\{d\mid M:\rho_N(d)=1\},\qquad
 b_N^{\rm rem}=\sum_{d\in\mathscr R_N}\chi _4(d)A_N(d),
\tag{164.H2}
\]

where (A_N) is the literal zero-extended amplitude.  Three exact
hostile facts hold.

1. If a pair is selected, the *ambient* unweighted residual character
   masses are equal.  If no pair is selected, their difference is
   \(\prod_{r\mid M,\ r\ {\rm prime}}(1+\chi _4(r))\), which can be
   \(2^{\omega(M)}\).  Ambient balance nevertheless says nothing about
   balance in the upper physical window: zero-amplitude divisors can
   carry all of the balancing mass.
2. Odd semiprimes, even products with odd semiprime part, and odd and
   even four-odd-prime products give exact residual singleton or
   one-unit-discrepancy fibres.  In particular, four-prime families with
   two primes in each odd residue class have residual unit-profile
   coefficient (-1) whether the selector is absent or present.  A
   selected pair removes two XOR partitions and leaves one negative
   neither/both partition.
3. On fixed admissible prime boxes these controls have respectively
   \(\gg L^2/(\log L)^2\) and
   \(\gg L^2/(\log L)^4\) products.  Hence any positive within-(N)
   transport theorem that is uniform over bounded amplitudes with only
   the frozen finite-variation/support information has
   \(L^{2-o(1)}\) capacity and cannot yield the
   \(L^{3/2}X^\varepsilon\) target on polynomial (L)-blocks.

The last assertion is a coefficient-uniform/raw-capacity no-go, not a
lower bound for the literal scalar.  The context supplies no pointwise
lower bound placing the actual product
\(\eta_L\Phi W\) on these prime fibres, and the outer factors
\(e(J\sqrt N)\) may cancel across distinct (N).  The exact surviving
problem is therefore an actual-coefficient cross-(N) correlation (or
its equivalent off-diagonal bilinear form), not another positive
within-product matching.

## Exact statement and hypotheses

Retain

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H\le J^{1/2},
\tag{164.H3}
\]

and every inherited half-open (N\asymp L^2) shell, cone, dyadic
profile, floor, star, endpoint, parity, and zero-extension convention.
For every odd divisor (d\mid M), set

\[
 A_N(d)=
 {\bf1}^{\rm lit}_{\{\sqrt N\le d\le2\sqrt N\}}
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right),
\tag{164.H4}
\]

with value zero outside the literal support.  The residual scalar is

\[
 \mathcal S_{L,1}^{\rm rem}
 =\sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}
 b_N^{\rm rem}e(J\sqrt N).
\tag{164.H5}
\]

The selector is exactly the accepted Round-163 selector: it chooses at
most one pair of distinct odd prime divisors, depends only on
\((N,L,\kappa)\), and can choose a pair only if

\[
 \chi _4(p_Nq_N)=-1,\qquad
 \left|\log(q_N/p_N)\right|\le \kappa L^{-1/2}.
\tag{164.H6}
\]

No selector density or nonemptiness is assumed.

For transport, order

\[
 d_{N,1}<\cdots<d_{N,r_N},\qquad
 \sigma_{N,i}=\chi_4(d_{N,i}),\qquad
 C_{N,j}=\sum_{i\le j}\sigma_{N,i}.
\tag{164.H7}
\]

Let (u_{N,i}=\log d_{N,i}), and let
\(\mathcal A_N(u)=A_N(e^u)\) be the literal real-variable profile with
the same zero extension.  On common smooth cells, the accepted profile
interfaces give

\[
 \left|\frac d{du}\mathcal A_N(u)\right|
 \ll 1+\frac LH\ll1.
\tag{164.H8}
\]

The full variation measure also contains every literal hard jump.
There are only (O(1)) such profile/support faces in one fixed block,
but their jump multiplicities under a transport must be retained.

The capacity families below are stated on fixed compact prime boxes
strictly inside the frozen geometric product shell and the displayed
cone.  This is the exact scope in which the notation
\(N\asymp L^2\) supplies intervals of fixed relative width.  These
boxes are not asserted to lie in a pointwise nonvanishing cell of the
literal amplitude.  The prime-counting input is only the unconditional
fixed-modulus theorem for (q=4), applied to fixed-relative-length
intervals; it is never applied to the shrinking selector window
\(|q-p|=O(1)\).

## Proof or derivation

**Exact subtraction and ambient sign mass.**  Formula (164.H1) is the
complement of the XOR indicator.  Hence, for a selected pair,

\[
 1= {\bf1}_{\rm XOR}+\rho_N
\quad\text{on every odd divisor }d\mid M,
\tag{164.H9}
\]

so (164.H2) is exactly the full coefficient minus the accepted sector,
once and only once.  For the total residual character
\(C_N^{\rm tot}=\sum_{d\in\mathscr R_N}\chi_4(d)\), multiplicativity
gives

\[
 C_N^{\rm tot}=
 \begin{cases}
 \displaystyle\prod_{\substack{r\mid M\\r\ {\rm prime}}}
        (1+\chi_4(r)),&
        \text{no pair selected},\\[6pt]
 \displaystyle(1+\chi_4(p_Nq_N))
 \prod_{\substack{r\mid M,\ r\ {\rm prime}\\r\ne p_N,q_N}}
        (1+\chi_4(r))=0,&
        \text{a pair selected}.
 \end{cases}
\tag{164.H10}
\]

Thus selection forces equality of the two *ambient unit* masses.  With
no selection, the ambient masses are equal as soon as (M) has a
prime (3\pmod4), but all (2^{\omega(M)}) residual divisors have
positive character if every odd prime factor is (1\pmod4).  Neither
case decides the amplitude-bearing mass in (164.H4).

**Exact Abel, Stieltjes, and transport normalization.**  Writing
\(A_i=A_N(d_{N,i})\), direct telescoping gives

\[
 \boxed{
 \sum_{i=1}^{r_N}\sigma_{N,i}A_i
 =C_{N,r_N}A_{r_N}
  +\sum_{j<r_N}C_{N,j}(A_j-A_{j+1}).}
\tag{164.H11}
\]

The largest residual odd divisor is always (M): it belongs to the
no-pair universe and, after selection, contains both selected primes.
For (N>16), (A_N(M)=0): if (N) is odd, (M=N>2\sqrt N), while
if (N=2M), then (M=N/2>2\sqrt N).  The smallest divisor (1) is
also outside the physical window.  Therefore the asymptotic blocks have
the exact Stieltjes form

\[
 b_N^{\rm rem}
 =-\int F_N(u)\,d\mathcal A_N(u),\qquad
 F_N(u)=\sum_{\substack{d\in\mathscr R_N\\\log d\le u}}\chi_4(d),
\tag{164.H12}
\]

where (d\mathcal A_N) includes the hard atoms.  Retaining the boundary
term in (164.H11) handles the finitely many small (N) without any
asymptotic convention.

If the positive and negative ambient masses are equal, write their
ordered logarithmic locations as (x_1\le\cdots\le x_m) and
\(y_1\le\cdots\le y_m).  The monotone coupling is optimal for the
unit-mass logarithmic cost and satisfies

\[
 W_1(\nu_N^+,\nu_N^-)
 =\sum_{i=1}^m|x_i-y_i|=\int_{\mathbb R}|F_N(u)|\,du,
\tag{164.H13}
\]

while the coefficient identity is

\[
 b_N^{\rm rem}=\sum_{i=1}^m
 \{\mathcal A_N(x_i)-\mathcal A_N(y_i)\}.
\tag{164.H14}
\]

For unequal masses, any injection matching opposite signs leaves a set
\(U_N\), and the exact identity and positive cost are

\[
 b_N^{\rm rem}
 =\sum_{(x,y)\in\mathcal M_N}
   \{\mathcal A_N(x)-\mathcal A_N(y)\}
  +\sum_{u\in U_N}\sigma(u)\mathcal A_N(u),
\tag{164.H15}
\]

\[
 \mathfrak T_N(\mathcal M_N)
 =\sum_{(x,y)\in\mathcal M_N}
   |\mathcal A_N(x)-\mathcal A_N(y)|
  +\sum_{u\in U_N}|\mathcal A_N(u)|.
\tag{164.H16}
\]

Equivalently, each unmatched atom can be sent to a cemetery atom with
amplitude zero.  Its *metric* cost is not defined until the cemetery
location and cost are specified; its unavoidable coefficient cost is
the second sum in (164.H16).  On a smooth cell, (164.H8) turns a
matched term into logarithmic displacement.  Across cells, one has
instead

\[
 |\mathcal A_N(x)-\mathcal A_N(y)|
 \le C|x-y|+
 \sum_{\xi\in\mathcal J_N\cap[x,y]}|\Delta\mathcal A_N(\xi)|,
\tag{164.H17}
\]

and the sum over pairs multiplies every jump by the number of transport
arcs crossing it.  Formula (164.H17), including zero-extension entry
and exit, is the required profile-jump ledger.  An (O(1)) number of
jump locations does not imply (O(1)) aggregate jump cost.

The distinction between metric balance and physical cost is already
exact for semiprimes.  For (N=pq), (p<q<4p), the ordered odd
divisors are (1<p<q<pq), and the only geometric physical divisor is
\(q\).  If (p,q\equiv3\pmod4), the ambient signs are
\((+,-,-,+)\), are balanced, and their monotone logarithmic cost is
\(2\log p\), while the unit-window coefficient is the single value
\(-1\).  If the primes have opposite characters and are selected, the
residual ambient set is \(\{1,pq\}\), its monotone cost is
\(\log(pq)\), but both amplitudes vanish and the literal residual
coefficient is exactly zero.  Thus neither a large nor a small raw
\(W_1\) is a physical lower-mass statement.

**Odd and even semiprime controls.**  Let (N=pq) with distinct odd
primes (p<q<4p).  Then

\[
 \{d\mid N:\sqrt N\le d\le2\sqrt N\}=\{q\}.
\tag{164.H18}
\]

The selector and residual are exact:

\[
 \widetilde b_N^{\rm rem}:=
 \sum_{\substack{d\in\mathscr R_N\\\sqrt N\le d\le2\sqrt N}}
 \chi_4(d)
 =\begin{cases}
 0,&\chi_4(pq)=-1\text{ and (164.H6) selects }\{p,q\},\\
 \chi_4(q),&\text{otherwise}.
 \end{cases}
\tag{164.H19}
\]

There is no eligible pair when (p,q) have the same residue class, so
same-(1\) and same-(3) families give respectively positive and
negative residual singletons.  Opposite-residue pairs separated in a
fixed ratio interval away from (1) are also no-selector singletons.
No fixed-modulus PNT claim is made for the selected, additive-(O(1))
prime-gap case.

For the even branch take (N=2pq) with

\[
 2p<q<8p.
\tag{164.H20}
\]

Among the odd divisors, (q) is again the unique member of the upper
window.  Its partner is (d_2=N/q=2p), so the physical second leg is
even exactly as required.  On any fixed ratio subinterval of (164.H20)
bounded away from (1), no pair can satisfy (164.H6) for large (L),
and

\[
 \widetilde b_{2pq}^{\rm rem}=\chi_4(q).
\tag{164.H21}
\]

Thus both parity branches contain exact no-selector residual singleton
fibres of either sign.

**Odd four-prime control, with every selector status.**  Let
\(N=r_1r_2s_1s_2\), where all four primes lie in
\([P,(1+\vartheta)P]\), with fixed (0<\vartheta<1), and

\[
 r_1,r_2\equiv1\pmod4,qquad s_1,s_2\equiv3\pmod4.
\tag{164.H22}
\]

For sufficiently large (P), one-prime divisors are below
\(\sqrt N\), three-prime divisors are above (2\sqrt N\), and in each
of the three complementary two-prime partitions exactly the larger
member lies in \([\sqrt N,2\sqrt N]\).  The same-class partition has
positive character and the two mixed partitions have negative
character.  Hence the geometric physical signs are

\[
 \{+,-,-\}.
\tag{164.H23}
\]

If no pair is selected, all three incidences remain.  If an
opposite-residue pair is selected, the same-class partition separates
the selected primes and is XOR; exactly one mixed partition also
separates them and is XOR; the other mixed partition puts them together
on one side and leaves the physical representative with both or neither.
That sole residual representative has negative character.  Therefore,
independently of selector status,

\[
 (\widetilde m_N^+,\widetilde m_N^-)=
 \begin{cases}(1,2),&\text{no pair selected},\\(0,1),&\text{a pair selected},\end{cases}
 \qquad
 \boxed{\widetilde b_N^{\rm rem}=-1.}
\tag{164.H24}
\]

The ambient residual masses are nevertheless balanced: without a
selector they are (8) and (8); with a selector, (164.H10) and the
eight retained cube vertices give (4) and (4).  Thus (164.H24) is
an exact counterexample to the inference “ambient balance implies no
unmatched physical atom.”

**Even four-odd-prime control.**  Fix (2<C<8), with margins, take
three low primes (r,s_1,s_2\asymp P), a high prime
\(h\asymp CP\), and put

\[
 N=2hrs_1s_2,qquad
 h,r\equiv1\pmod4,qquad s_1,s_2\equiv3\pmod4.
\tag{164.H25}
\]

The prime boxes may be chosen sufficiently short, depending only on
(C), that the only physical odd divisors are

\[
 hr,\quad hs_1,\quad hs_2.
\tag{164.H26}
\]

Indeed, for (u\in\{r,s_1,s_2\}),

\[
 1<\frac{(hu)^2}{N}=
 \frac{hu}{2\prod_{v\ne u}v}<4,
\tag{164.H27}
\]

whereas every low-low product is below \(\sqrt N\), and every
three-prime odd divisor is above (2\sqrt N) for large (P).  The
second leg (N/(hu)) contains the factor (2).  The signs in
(164.H26) are again \(\{+,-,-\}\).  The high prime is a fixed ratio
away from every low prime, so a selected pair, if present, is
\(\{r,s_i\}\).  It removes (hr) and (hs_i) as XOR incidences and
leaves (hs_{3-i}), negative, as a neither incidence.  Consequently
(164.H24) holds verbatim for this even family.  This is a genuinely
multiprime parity control, not an odd-complement substitution.

**Capacity count and source audit.**  The sole external input is
Michael A. Bennett, Greg Martin, Kevin O'Bryant, and Andrew Rechnitzer,
[*Explicit bounds for primes in arithmetic progressions*](https://arxiv.org/abs/1802.00085),
Theorem 1.2.  It states that for integer (q\ge3),
\((a,q)=1\), there are explicit (c_\theta(q),x_\theta(q)>0) such
that

\[
 \left|\theta(x;q,a)-\frac{x}{\varphi(q)}\right|
 <c_\theta(q)\frac{x}{\log x}\qquad(x\ge x_\theta(q)).
\tag{164.H28}
\]

The printed bounds are (c_\theta(q)\le1/840) for
\(3\le q\le10^4\) and (x_\theta(q)\le8\cdot10^9) for
\(3\le q\le10^5\).  Thus for (q=4), (a=1) or (3), and
\(x\ge8\cdot10^9), the weaker endpoint bound with constant (1/840)
is valid.  For every fixed (0<\alpha<\beta), subtraction at
\(\alpha T,\beta T\) gives

\[
 \theta(\beta T;4,a)-\theta(\alpha T;4,a)
 \ge \frac{(\beta-\alpha)T}{2}
 -\frac{\beta T}{840\log(\beta T)}
 -\frac{\alpha T}{840\log(\alpha T)}
 \gg_{\alpha,\beta}\!T.
\tag{164.H29}
\]

Since each prime counted has logarithm at most
\(\log(\beta T)\), (164.H29) yields

\[
 \#\{p\in[\alpha T,\beta T]:p\equiv a\pmod4\}
 \gg_{\alpha,\beta}\frac{T}{\log T}.
\tag{164.H30}
\]

All hypotheses are now explicit: the modulus is the fixed (4), both
residues are coprime to (4), both interval endpoints exceed the
printed threshold for large (T), and interval ratios are fixed.  The
theorem is unconditional.  It supplies no information for a shrinking
interval of additive length (O(1)), so it supplies no density for
(164.H6).

Apply (164.H30) independently in disjoint fixed boxes.  Unique
factorization, with at most a fixed permutation multiplicity, gives

\[
 \#\{\text{odd or even semiprime-part singleton controls}\}
 \gg\frac{L^2}{(\log L)^2},
\tag{164.H31}
\]

and, with (P\asymp\sqrt L),

\[
 \#\{\text{odd or even four-prime controls}\}
 \gg\frac{P^4}{(\log P)^4}
 \asymp\frac{L^2}{(\log L)^4}.
\tag{164.H32}
\]

Repeated-prime diagonals are excluded and are lower order; all retained
products are squarefree.  The normalizing factor
\((L^2/N)^{3/4}\) is bounded above and below on each fixed box.

Give every geometric physical residual atom unit amplitude and every
other divisor amplitude zero.  Equations (164.H19), (164.H21), and
(164.H24) then force one unit of unmatched/variation cost per product.
Consequently

\[
 \sum_N\inf_{\mathcal M_N}\mathfrak T_N(\mathcal M_N)
 \gg\frac{L^2}{(\log L)^4}=L^{2-o(1)}
\tag{164.H33}
\]

for the four-prime family, irrespective of selector status.  The same
statement with \((\log L)^2\) holds on the no-selector semiprime
families.  This falsifies a coefficient-uniform target transport bound
based only on sign balance, monotone optimality, bounded profile size,
and finitely many hard jumps.  It does not assert (164.H33) for the
literal amplitudes (164.H4).

**Power, outer phase, and the exact surviving cross-(N) theorem.**
The target is (L^{3/2}X^\varepsilon), while (164.H33) is
\(L^{2-o(1)}\).  On every polynomial block (L=X^\lambda),
\(\lambda>0\), choosing (\varepsilon<\lambda/2\) exhibits the missing
\(L^{1/2-o(1)}\) positive-route saving.  This is the same missing
half-power identified by the accepted raw product capacity.  It is not
a lower bound for (164.H5), because the actual coefficient is

\[
 a_N^{\rm rem}:=\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}b_N^{\rm rem},
\qquad
 \mathcal S_{L,1}^{\rm rem}=\sum_Na_N^{\rm rem}e(J\sqrt N).
\tag{164.H34}
\]

Every within-(N) exchange factors out (e(J\sqrt N)).  Taking
\(\sum_N|a_N^{\rm rem}|\) discards the only remaining oscillation.
The exact square of the desired scalar is

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 =\sum_N|a_N^{\rm rem}|^2
 +2\Re\!\sum_{N<N'}a_N^{\rm rem}
 \overline{a_{N'}^{\rm rem}}
 e\!\left(J(\sqrt N-\sqrt{N'})\right).
\tag{164.H35}
\]

Thus, after the elementary diagonal
\(\sum_N|a_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon\), the
smallest exact remaining theorem is the actual-coefficient off-diagonal
bound making the right side of (164.H35)
\(O_\varepsilon(L^3X^\varepsilon)\).  A convenient sufficient
normalization is

\[
 \left|\sum_Na_N^{\rm rem}e(J\sqrt N)\right|
 \ll_\varepsilon L^{-1/2}
 \left(\sum_N|a_N^{\rm rem}|^2\right)^{1/2}
 (\#\mathcal N_L)^{1/2}X^\varepsilon,
\tag{164.H36}
\]

because both norm factors have natural scale (L X^\varepsilon).
Equation (164.H36) must be restricted to the actual residual direction:
it is false for arbitrary coefficients, as the phase-aligned choice
\(a_N=e(-J\sqrt N)\) gives (L^2) rather than (L^{3/2}).

The accepted exact-collision result controls only the finitely many
exact same-phase radical relations at one fixed centre.  It does not
control the near-phase off-diagonal in (164.H35).  The accepted
character-Poisson product-collar obstruction likewise shows that a
termwise positive rank-one collar count restores
\(\sqrt{JL}=L^{3/2}(H/L+O(L^{-1}))\) and repays its apparent scaling
gain.  Therefore another positive collar norm cannot substitute for
(164.H35).  What remains possible is genuinely signed cancellation
between distinct (N) at the prescribed arbitrary real (J), using
the literal (a_N^{\rm rem}); no uniform exact phase opposition is
claimed.

## First doubtful or unproved step

The exact residual algebra, odd/even divisor windows, selector case
split, monotone/cemetery normalization, four-prime residual discrepancy,
and fixed-box prime counts above have no unproved step under their stated
hypotheses.  The first unavailable step is any transfer from the raw
unit-profile capacity to a literal physical lower mass.  Such a transfer
would require a proved compact prime box on which the exact sampled
\(\eta_L(d)\Phi(d/(H+1))W(\sqrt{q_X}d/(2\sqrt N))\) is uniformly
nonzero with controlled sign, followed by control of cancellation among
the several literal atoms and across (N).  No such lower-profile
statement is present in the permitted context, and the fixed-modulus
prime theorem alone cannot provide it.

Correspondingly, the first unproved affirmative step is (164.H35), or
a sufficient actual-direction estimate such as (164.H36).  Ambient
sign equality, the optimality of monotone (W_1), and exact-collision
sparsity do not imply it.  The report therefore rules out only a
coefficient-uniform/positive within-(N) transport closure; it neither
disproves the literal residual target nor proves any lower bound for
\(\mathcal S_{L,1}^{\rm rem}\).

## Required control test and outcome

| Required control | Outcome |
|---|---|
| `residual_exact_subtraction` | **GREEN.** (164.H9) partitions every ambient odd divisor into XOR and neither/both exactly once; no-pair products remain whole. |
| `ordered_divisor_abel_identity` | **GREEN.** (164.H11) is exact.  The terminal divisor is (M); its amplitude vanishes for the asymptotic odd and even blocks, while the terminal term remains available for small (N). |
| `odd_divisor_and_even_N_branch` | **GREEN.** The universe is always (d\mid M), (d) odd.  Equations (164.H20)--(164.H21) and (164.H25)--(164.H27) retain (2\mid N/d) and give explicit even controls. |
| `sign_mass_and_unmatched_atoms` | **GREEN obstruction.** (164.H10) classifies ambient imbalance.  (164.H24) has balanced ambient masses but one residual negative physical atom for every selector status. |
| `monotone_transport_normalization` | **GREEN.** Equal mass uses (164.H13)--(164.H14); unequal mass uses the injection/cemetery identity (164.H15) and pays the exact unmatched term in (164.H16). |
| `profile_jump_and_zero_extension_variation` | **GREEN ledger, OPEN estimate.** (164.H17) retains smooth logarithmic displacement and each hard jump with crossing multiplicity.  No global smoothness or free cemetery is assumed. |
| `semiprime_multiprime_capacity` | **GREEN route no-go.** (164.H18)--(164.H27) are exact; the source-audited counts are (164.H31)--(164.H33).  The four-prime control is selector-robust. |
| `outer_N_phase_preservation` | **GREEN scope.** The phase is factored out only within fixed (N) and is retained in (164.H34)--(164.H36). |
| `rank_one_product_collar_comparison` | **GREEN obstruction.** The accepted positive collar capacity does not prove the actual off-diagonal correlation and misses the same target-strength gain on its adverse range. |
| `arbitrary_real_centre_phase` | **GREEN scope.** All within-fibre controls hold for every real (J).  Across (N), only the fixed-centre signed form (164.H35) remains; no phase pairing uniform in (J) is asserted. |
| `missing_L_half_power` | **GREEN no-go.** Raw transport capacity is (L^{2-o(1)}) against (L^{3/2}X^\varepsilon); (164.H36) displays the required (L^{-1/2}) correlation gain relative to Cauchy. |
| `physical_coefficient_vs_diagnostic` | **GREEN quarantine.** Unit amplitudes and prime counts certify raw/coefficient-uniform capacity only.  No literal profile lower bound and no lower bound for the oscillatory scalar is claimed. |
| `remaining_few_point_and_downstream_scope` | **GREEN quarantine.** No conclusion transfers to the other (L\ll D\ll L^2,\ t\ll\sqrt L) channels, full hard TOP, BAL, UNBAL, either smooth M2 packet, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter target, or either exponent. |

No numerical or symbolic experiment was used.

## Dependencies and exact artifacts used

The report used exactly the following repository artifacts authorized by
the task:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at the Round-164 starting graph
   `81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306`;
3. `state/active_campaign.yml`;
4. `strategy/round164_m2_hard_top_t1_residual_signed_divisor_transport_strategy.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/candidates/conductor_round164_residual_transport_seed.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/literal_near_square_divisor_involution_attack.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/prime_toggle_complement_leakage_hostile_audit.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/conductor_round163_adjudication.md`;
10. `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
11. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`; and
12. `rounds/codex-managed/m9-m1-near-product-character-kernel/reports/character_divisor_attack.md`, used only for the prior fixed-modulus source lead and the distinction between coefficient-norm capacity and a physical signed scalar.

The only web lookup was primary-source verification of Bennett--Martin--O'Bryant--Rechnitzer, [*Explicit bounds for primes in arithmetic progressions*](https://arxiv.org/abs/1802.00085), Theorem 1.2.  Its exact hypotheses and the deduction actually used are recorded in (164.H28)--(164.H30).  No source theorem is used for selector density, shrinking intervals, literal profile placement, or oscillatory lower mass.

## Recommended state effect

**Retain** this report as a rigorous
`hard_top_t1_residual_transport_no_go` against coefficient-uniform and
positive within-(N) monotone-transport closure.  The durable content is
the exact residual indicator (164.H1), ambient mass formula (164.H10),
Abel/cemetery ledger (164.H11)--(164.H17), selector-complete odd/even
semiprime and multiprime controls (164.H18)--(164.H27), and the
source-audited (L^{2-o(1)}) raw capacity (164.H31)--(164.H33).

**Do not promote** (164.H33) to a literal physical lower bound, a lower
bound for (164.H5), a density theorem for close opposite primes, or a
disproof of the residual target.  The literal profile may suppress the
diagnostic fibres, and the signed outer phase remains available.

**Revise the next action** to the exact actual-coefficient cross-(N)
frontier (164.H35), or a sufficient normalized correlation such as
(164.H36), retaining the arbitrary real centre, all profiles, hard
jumps, parity, and the accepted residual subtraction before any positive
norm.  Such a theorem must fail on phase-aligned arbitrary arrays and
must improve on the accepted positive rank-one collar ledger.

**No change** to the full (t=1) target, the remaining few-point
channels, hard TOP, BAL, UNBAL, either smooth M2 packet, M9--M2,
M9--M1, endpoint uniformity, M9, the conditional bridge, the quarter
theorem, or either global exponent.

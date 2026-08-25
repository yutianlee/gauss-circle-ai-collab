# Round 163 discovery report: literal near-square divisor involutions

- Campaign: `m9-m2-hard-top-t1-near-square-divisor-involution-gate`
- Task: `literal_near_square_divisor_involution_attack`
- Role: discovery
- Round: 163
- Starting graph SHA-256: `700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`
- Evidence status: candidate evidence only; no shared proof-state edit
- Allocation used: 100% analytic/algebraic, 0% numerical

## 1. Result: a strict close-prime sector and the exact residual leakage

The proposed divisor mechanism has one target-safe strict sector, but it
does not estimate the full physical coefficient.

Put (N=2^{\epsilon_N}M), where \(\epsilon_N\in\{0,1\}\) and (M) is
odd, and zero-extend the literal profile to all odd divisors of (N):

\[
 A_N(d):=
 \mathbf 1^{\rm lit}_{\{\sqrt N\le d\le2\sqrt N\}}
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\tag{163.D1}
\]

Here \(\mathbf 1^{\rm lit}\) includes the inherited cone convention,
hard entries and exits, stars, and zero extension.  The exact
coefficient is

\[
 b_{L,X}(N)=\sum_{d\mid M}\chi_4(d)A_N(d).
\tag{163.D2}
\]

For each (N), choose **at most one** unordered pair of odd prime
divisors

\[
 p_N<q_N,\qquad \chi_4(p_Nq_N)=-1,
 \qquad \left|\log\frac{q_N}{p_N}\right|
 \le \kappa L^{-1/2},
\tag{163.D3}
\]

by any deterministic rule depending only on (N) (for example the
lexicographically first eligible pair).  If there is no eligible pair,
choose none.  Let (b^{\rm cp}_{L,X}(N)) be the part of (163.D2) in
which (d) contains exactly one of \(p_N,q_N\).  Then, uniformly for the
literal range in the brief,

\[
 \boxed{
 \left|\sum_{N\asymp L^2}^{\rm lit}
 \mu^2(N)\left(\frac{L^2}{N}\right)^{3/4}
 e(J\sqrt N)b^{\rm cp}_{L,X}(N)\right|
 \ll_{\kappa} L^{3/2}+L.}
\tag{163.D4}
\]

Thus this complete, canonically selected, exactly-one close-prime
incidence sector is target-safe.  The estimate retains the even-(N)
branch and is uniform in the arbitrary real centre.  It makes no density
claim for eligible products and says nothing about incidences containing
neither or both selected primes.

For the residual full coefficient, all possible divisor exchanges admit
an exact classification.  If (E\mid M), define the squarefree subset
toggle

\[
 T_E(d):=\frac{dE}{(d,E)^2}.
\tag{163.D5}
\]

It is sign-reversing exactly when \(\chi_4(E)=-1\).  Conversely, every
pair of opposite-character physical divisors is (d,T_E(d)) for one
such (E).  Hence the graph containing **all** genuinely
window-preserving multi-prime exchanges is the complete bipartite graph
between

\[
 V_N^\pm:=\{d\mid M:A_N(d)\ne0,\ \chi_4(d)=\pm1\}.
\tag{163.D6}
\]

For every partial matching \(\mathcal M_N\) in that graph,

\[
\begin{aligned}
 b_{L,X}(N)
  ={}&\sum_{(d_+,d_-)\in\mathcal M_N}
       \{A_N(d_+)-A_N(d_-)\}\\
    &+\sum_{d\in U_N^+}A_N(d)
      -\sum_{d\in U_N^-}A_N(d),
\end{aligned}
\tag{163.D7}
\]

where (U_N^\pm) are the unmatched vertices.  Even an unrestricted
matching leaves at least

\[
 \Delta_N:=\bigl|\#V_N^+-\#V_N^-\bigr|
\tag{163.D8}
\]

vertices, and a two-prime matching can leave more.  Cycles and weighted
averages do not improve this ledger: cycles reduce to alternate
matchings, while every sign-reversing toggle has the same exact
self-return identity

\[
 b_{L,X}(N)=\frac12\sum_{d\mid M}\chi_4(d)
 \{A_N(d)-A_N(T_Ed)\}.
\tag{163.D9}
\]

In particular, averaging one-prime (3\pmod4) toggles repeats the
original coefficient coherently and gives no divisor-count gain.  The
remaining unmatched and profile-difference ledger has
(L^{2-o(1)}) diagnostic capacity, against the (L^{3/2}) target.
Consequently the full (t=1) target remains open.  The appropriate
round-closing label for the positive content of this report is

\[
 \boxed{\texttt{strict\_t1\_prime\_toggle\_sector}.}
\]

## 2. Exact statement and hypotheses

The parameters and profiles are exactly those in the brief:

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac X{y^2},\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H\le J^{1/2}.
\tag{163.D10}
\]

The half-open product shell is left literal.  On it, the cone forces
(d_1,d_2\asymp L).  The inherited profile facts used in (163.D4) are
only the following:

1. on each smooth cell, \(\eta_L\) is a fixed dyadic rescaling, so its
   Lipschitz scale is (L^{-1});
2. \(\Phi\in C^1[0,1]\), with bounded derivative, so its scale here is
   ((H+1)^{-1});
3. (W) is a fixed smooth profile on each of its finitely many literal
   cells; and
4. the number of hard cone, dyadic, profile, star, and zero-extension
   boundaries in one fixed block is (O(1)).

No smoothing of a literal hard boundary is made.  An orbit meeting two
different cells, or having only one member in the physical support, is
charged as a boundary orbit.

For the strict sector, the canonical pair rule is part of the
statement.  It depends on (N), not on the factor orientation, so the
same pair is selected at both ends of an exchange.  The pair contains no
factor (2).  Thus for even squarefree (N=2M), the factor (2)
remains on the second physical leg throughout the exchange.

For the no-go statements, no sign or lower bound is assumed for the
literal profiles.  The semiprime and four-prime counts below are
constant-weight diagnostics of unmatched capacity, not lower bounds for
the physical scalar.  Their (L^{2-o(1)}) counts use only the prime
number theorem in the two fixed residue classes modulo four, and are not
used in the proof of (163.D4).

## 3. Proof and derivation

### 3.1 Literal squarefree product grouping

On (t=1), the accepted radical dictionary forces (g=u=v=1).
Therefore (d_1,d_2) are squarefree and coprime, and
(N=d_1d_2) is squarefree.  Conversely, for squarefree (N), choosing
an odd divisor (d=d_1\mid N) determines

\[
 d_2=N/d,\qquad (d_1,d_2)=1.
\]

The cone is exactly

\[
 d_2\le d_1\le4d_2
 \quad\Longleftrightarrow\quad
 \sqrt N\le d_1\le2\sqrt N,
\tag{163.D11}
\]

and

\[
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
 =W\!\left(\frac{\sqrt{q_X}\,d_1}{2\sqrt N}\right).
\tag{163.D12}
\]

This proves (163.D2) and retains the even-(N) branch: if (2\mid N),
then (d_1) is odd and (2\mid d_2).  Since a squarefree (N>1) is
not a square, neither (d=\sqrt N) nor (d=2\sqrt N) can occur as an
integer divisor.  Thus there is no hidden square fixed point on this
(t=1) face.  The outer half-open shell and any outer star are
(N)-dependent and are unchanged by every within-(N) exchange.

### 3.2 Single-prime toggles and coherent self-return

Let (p\mid M), (p\equiv3\pmod4).  The coordinate toggle is
(T_p(d)=pd) if (p\nmid d), and (T_p(d)=d/p) otherwise.  It reverses
the character.  It never has two physical endpoints: if (d) is
physical, then

\[
 p\nmid d\Longrightarrow pd\ge3\sqrt N>2\sqrt N,
 \qquad
 p\mid d\Longrightarrow d/p\le\frac23\sqrt N<\sqrt N.
\tag{163.D13}
\]

Pairing the complete odd divisor cube by the coordinate (p) gives

\[
 \boxed{
 b_{L,X}(N)=
 \sum_{d\mid M/p}\chi_4(d)\{A_N(d)-A_N(pd)\}.}
\tag{163.D14}
\]

This is all leakage, not a thin boundary difference.  Indeed, the two
supports in every brace are disjoint.  Consequently

\[
 \sum_{d\mid M/p}|A_N(d)-A_N(pd)|
 =\sum_{r\mid M}|A_N(r)|,
\tag{163.D15}
\]

and the full-cube version has twice this \(\ell^1\)-mass.

Let \(P_3(M)=\{p\mid M:p\equiv3\pmod4\}\), and (k=\#P_3(M)).
Summing (163.D14) over (p\in P_3(M)) gives exactly

\[
 k b_{L,X}(N)=
 \sum_{p\in P_3(M)}\sum_{d\mid M/p}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.D16}
\]

Every active term \(\chi_4(r)A_N(r)\) occurs with the same sign once for
each (p): it is the first term when (p\nmid r), while for (p\mid r)
it is

\[
 -\chi_4(r/p)A_N(r)=\chi_4(r)A_N(r).
\]

Dividing by (k) therefore returns the original coefficient; no
(k^{-1}) gain is present.  Equivalently, if
(P=k^{-1}\sum_{p\in P_3(M)}U_{T_p}), then on every active divisor

\[
 (I-P)A_N(d)=A_N(d),
\tag{163.D17}
\]

because all one-toggle images are outside the window.  Signed averaging
does not help: weights of total zero give the identity (0=0), and
weights of nonzero total reproduce (163.D16) after normalization.

### 3.3 All multi-prime exchanges, signs, matchings, and cycles

For squarefree (E,d\mid M), (163.D5) is symmetric difference on the
prime subsets.  It satisfies

\[
 T_E^2=1,\qquad
 \chi_4(T_Ed)=\chi_4(E)\chi_4(d).
\tag{163.D18}
\]

Write

\[
 R=\frac d{(d,T_Ed)},\qquad
 S=\frac{T_Ed}{(d,T_Ed)}.
\]

Then (R,S) are the products removed and inserted, respectively, and

\[
 \frac{T_Ed}{d}=\frac SR,\qquad
 \frac{\chi_4(T_Ed)}{\chi_4(d)}=\chi_4(RS).
\tag{163.D19}
\]

If (d=x\sqrt N), both endpoints lie in the physical window exactly
when

\[
 x\in[1,2]\cap[R/S,2R/S].
\tag{163.D20}
\]

This interval can be nonempty only when (1/2\le S/R\le2).  Since all
relevant primes are odd, an addition-only exchange has ratio at least
three and a removal-only exchange has ratio at most one third.  Every
internal exchange therefore removes and inserts nonempty prime sets.

For a two-prime toggle (E=pq), the cases in which (d) contains
neither or both primes have ratios (pq) and ((pq)^{-1}), hence are
never internal.  The only internal case swaps one prime for the other:

\[
 d=gp\longleftrightarrow gq,\qquad
 \frac{d'}d=\frac qp.
\tag{163.D21}
\]

It reverses the character precisely when (p,q) occupy opposite
residue classes modulo four.  A toggle containing (2) maps an odd
physical divisor to an even divisor and is never an internal physical
edge.

This list is exhaustive, including exchanges of three or more primes.
Indeed, if (d,e\in V_N^+\cup V_N^-) have opposite characters, put

\[
 E=\frac{de}{(d,e)^2}.
\]

Then (E\mid M), (T_Ed=e), and \(\chi_4(E)=-1\).  Moreover (d,e)
cannot be comparable, because the quotient of two distinct comparable
odd divisors is at least three whereas two physical divisors have ratio
at most two.  Thus every opposite-sign physical pair is a genuine
remove-and-insert exchange.  This proves that the unrestricted exchange
graph is complete bipartite and proves (163.D7)--(163.D8).

A globally consistent sign-reversing involution is exactly a perfect
matching.  A general sign-reversing permutation has only even cycles.
Taking alternate edges in every even cycle produces a perfect matching
on the same vertices, and its contribution is still a sum of profile
differences.  Thus a cycle cannot cover more vertices or make the
alternating profile sum vanish.  A noninjective rule is not a
reindexing; its preimage multiplicities must be restored, after which it
is a weighted transport between the two sign classes and the unmatched
mass difference remains.

Finally, reindexing the complete odd divisor cube under any fixed
sign-reversing (T_E) gives

\[
 \sum_{d\mid M}\chi_4(d)A_N(T_Ed)=-b_{L,X}(N),
\]

which proves (163.D9).  If \(\lambda_E\) are arbitrary weights on
sign-reversing toggles and \(\Lambda=\sum_E\lambda_E\ne0\), then

\[
 b_{L,X}(N)=\frac1{2\Lambda}
 \sum_E\lambda_E\sum_{d\mid M}\chi_4(d)
 \{A_N(d)-A_N(T_Ed)\}.
\tag{163.D22}
\]

Thus every weighted multi-prime average has the same character
eigenvalue (-1).  It is an exact self-return unless one separately
proves that the displayed physical differences are small.

### 3.4 Proof of the canonical close-prime sector

Fix a selected pair (p=p_N<q=q_N) and put (r=q/p), so

\[
 |\log r|\le\delta,\qquad \delta=\kappa L^{-1/2}.
\tag{163.D23}
\]

The condition that (d) contain exactly one of (p,q) is invariant
under (T_{pq}).  Use the unique representative containing (p) and
not (q).  Its orbit is

\[
 (d_1,d_2)\longleftrightarrow(rd_1,r^{-1}d_2).
\tag{163.D24}
\]

The product (N), squarefreeness, coprimality, oddness of (d_1), the
factor (2\mid d_2) when (N) is even, the outer normalization, and
(e(J\sqrt N)) are all unchanged.  The character reverses.  With zero
extension, each complete orbit contributes exactly

\[
 \chi_4(d_1)\{A_N(d_1)-A_N(rd_1)\}.
\tag{163.D25}
\]

Suppose first that both endpoints lie in one common smooth literal cell.
On support (d_1,d_2\asymp L), and

\[
 |rd_1-d_1|+|r^{-1}d_2-d_2|\ll\delta L.
\tag{163.D26}
\]

The three profile changes are, uniformly,

\[
 \begin{aligned}
 |\eta_L(rd_1)-\eta_L(d_1)|&\ll\delta,\\
 \left|\Phi\!\left(\frac{rd_1}{H+1}\right)
       -\Phi\!\left(\frac{d_1}{H+1}\right)\right|
   &\ll \frac{\delta L}{H}\ll\delta,\\
 \left|W\!\left(\frac{\sqrt{q_X}\,rd_1}{2\sqrt N}\right)
       -W\!\left(\frac{\sqrt{q_X}\,d_1}{2\sqrt N}\right)\right|
   &\ll\delta.
 \end{aligned}
\tag{163.D27}
\]

The exact floor values (H,y) and (q_X) are the same at the two
endpoints.  The product rule and boundedness of the profiles give

\[
 |A_N(d_1)-A_N(rd_1)|\ll\delta
\tag{163.D28}
\]

for a common-cell orbit.

Across all (N\asymp L^2), divisor incidences are ordered integer pairs
((d_1,d_2)) in a fixed (O(L)\times O(L)) box.  Hence there are
(O(L^2)) of them, before imposing squarefreeness, coprimality, parity,
or the canonical-pair condition.  The total common-cell contribution to
(163.D4) is therefore

\[
 O(\delta L^2)=O_\kappa(L^{3/2}).
\tag{163.D29}
\]

It remains to count boundary orbits, rather than smooth them.  A
vertical dyadic/profile boundary has the form (d_1=cL+O(1)); any
(H+1) entry or exit that meets the block is counted in the same way.
Crossing it
under (163.D24) forces (d_1) into an interval of length
(O(\delta L+1)), and there are (O(L)) possible (d_2).  A cone or
(W)-profile boundary has the form (d_1/d_2=c+O(L^{-1})).  For each
(d_2\asymp L), crossing under
(d_1/d_2\mapsto r^2d_1/d_2) again leaves
(O(\delta L+1)) possible (d_1).  Exact star and integer endpoint
sets lie on the same boundary curves and contribute (O(L)).  There
are only (O(1)) literal boundaries, so the entire crossing set has

\[
 O(\delta L^2+L)=O_\kappa(L^{3/2}+L)
\tag{163.D30}
\]

incidences.  This count includes zero-extended partner legs: every orbit
is seeded by a physical (d_1,d_2\asymp L), and (163.D23)--(163.D24)
keep its possibly nonphysical partner in a fixed enlarged
(O(L)\times O(L)) box; membership can change only in one of the counted
strips.  Each crossing incidence has bounded weight.  The product-shell
boundary is not crossed because (N) is fixed.  Equations
(163.D29)--(163.D30), followed
only by the triangle inequality over the already paired differences,
prove (163.D4).  No cancellation across different (N) has been used.

### 3.5 Complementary divisors: both parity branches

If (N) is odd, the physical complement is (e=N/d).  It sends the
upper interval to the excluded lower interval and gives exactly

\[
\begin{aligned}
 b_{L,X}(N)=\chi_4(N)
 \sum_{\substack{e\mid N\\ \sqrt N/2\le e\le\sqrt N}}
 \chi_4(e)&\eta_L(N/e)
 \Phi\!\left(\frac{N/e}{H+1}\right)\\
 &\times W\!\left(\frac{\sqrt{q_X}\sqrt N}{2e}\right),
\end{aligned}
\tag{163.D31}
\]

with the complementary literal endpoint convention.  It reverses the
character only when (N) contains an odd number of (3\pmod4) primes;
with an even number it preserves the character.  In either case the
coefficient has merely been rewritten in a disjoint lower window with a
swapped profile.

If (N=2M), the physical complement (N/d) is even and lies in
([\sqrt N/2,\sqrt N]); it is not an eligible character-supported first
leg.  The character-preserving complement on the odd divisor cube is
instead

\[
 e=M/d=N/(2d),
\]

which maps the upper physical interval to
([\sqrt N/4,\sqrt N/2]) and gives

\[
\begin{aligned}
 b_{L,X}(2M)=\chi_4(M)
 \sum_{\substack{e\mid M\\ \sqrt N/4\le e\le\sqrt N/2}}
 \chi_4(e)&\eta_L(M/e)
 \Phi\!\left(\frac{M/e}{H+1}\right)\\
 &\times W\!\left(\frac{\sqrt{q_X}\sqrt N}{4e}\right).
\end{aligned}
\tag{163.D32}
\]

Thus neither the even physical swap nor the odd-part complement supplies
a second physical upper leg.  This is the same full-minus-complement
self-return logic seen on the accepted M1 analogue, but no M1 estimate
is transferred here.

The full odd-divisor sum is

\[
 \sum_{d\mid M}\chi_4(d)
 =\prod_{p\mid M}(1+\chi_4(p)).
\tag{163.D33}
\]

It vanishes if (P_3(M)\ne\varnothing), but (163.D14) shows that every
physical cancellation partner is outside the upper window.  If
(P_3(M)=\varnothing), every physical character equals (+1), so there
is no sign-reversing divisor exchange at all.  Completing (163.D2) to
(163.D33) therefore leaves an uncontrolled complement in both cases.

### 3.6 Exact semiprime and multi-prime controls

For this subsection only, write

\[
 \widetilde V_N^\pm
 :=\{d\mid M:\sqrt N\le d\le2\sqrt N,
                 \ \chi_4(d)=\pm1\}
\tag{163.D34a}
\]

for the geometric unit-profile diagnostic vertices.  This notation does
not assert that the literal profile is nonzero at every such vertex.

Let (N=pq), with odd primes (p<q<4p).  The only physical divisor is
(q): (p<\sqrt N<q<2\sqrt N), while (1,pq) are far outside.  Hence

\[
 \widetilde V_N^+\cup\widetilde V_N^-=\{q\},\qquad
 b_{L,X}(N)=\chi_4(q)A_N(q).
\tag{163.D34}
\]

This is an exact physical singleton fibre.  If, for example,
(p\equiv1\pmod4) and (q\equiv3\pmod4), the full divisor sum is zero,
but the truncated coefficient is the single term (-A_N(q)).  If both
primes are (1\pmod4), the product lies in the no-toggle sector and the
single term has positive character.

On any fixed compact admissible semiprime box (p,q\asymp L), the prime
number theorem in the two fixed residue classes gives

\[
 \#\{N=pq\}\gg \frac{L^2}{(\log L)^2}=L^{2-o(1)}.
\tag{163.D35}
\]

For constant unit profiles this is an unmatched capacity, not a lower
bound for the actual profiled exponential sum.

There is also an exact genuinely multi-prime control.  Take four odd
primes in a fixed sufficiently short multiplicative interval
([P,(1+\theta)P]), (P\asymp\sqrt L), with two primes in each odd
residue class modulo four.  For (P) large, one-prime divisors are below
(\sqrt N), three-prime divisors are above (2\sqrt N), and exactly one
member of each of the three complementary two-prime partitions lies in
([\sqrt N,2\sqrt N]).  Thus there are exactly three physical divisors.
The partition joining the two (3\pmod4) primes has positive character,
while the two mixed partitions have negative character.  Therefore

\[
 \#\widetilde V_N^+=1,\qquad \#\widetilde V_N^-=2,
\tag{163.D36}
\]

independently of which member of each complementary partition is the
upper one.  Each positive-negative edge swaps exactly one close prime of
each residue class, so all available sign-reversing edges are genuine
window-preserving two-prime exchanges.  The graph is (K_{1,2}), and
every matching leaves one physical divisor.  PNT in the fixed residue
classes supplies

\[
 \gg \frac{P^4}{(\log P)^4}
 \asymp\frac{L^2}{(\log L)^4}=L^{2-o(1)}
\tag{163.D37}
\]

such constant-weight diagnostic products in a fixed admissible box.
This control rules out the inference that allowing all two-prime
exchanges makes the unmatched set polynomially sparse.

### 3.7 Phase and power ledger

Every within-(N) exchange preserves (e(J\sqrt N)) exactly.  Hence it
obtains cancellation only through the divisor coefficient already
displayed in (163.D7); the arbitrary-real centre supplies no extra sign.
Pairing residual divisors across different products would be a different
analytic mechanism.  Uniform exact phase opposition for varying real
(J) is impossible unless the products agree, and at one fixed centre
the accepted radical-collision lemma permits at most one unequal exact
base-phase edge.  Near collisions remain open.

The restored ledger is:

| Item | Size or exact effect |
|---|---:|
| Physical ordered factor capacity | (L^{2+o(1)}) |
| Target | (L^{3/2}X^\varepsilon) |
| Missing divisorwise gain | (L^{1/2-o(1)}) |
| One (3\pmod4) toggle | all active terms cross; no gain |
| Average of (k) one-prime toggles | (k b_N/k=b_N) exactly |
| Canonical close pair, smooth differences | (L^2\cdot L^{-1/2}=L^{3/2}) |
| Canonical close pair, all hard crossings | (O(L^{3/2}+L)) |
| Semiprime unmatched diagnostic | (L^2/(\log L)^2) |
| Four-prime two-exchange unmatched diagnostic | (L^2/(\log L)^4) |

Thus (163.D4) gets exactly the missing half-power on its strict sector.
Outside that sector, matching, completion, cycles, and averaging retain
(L^{2-o(1)}) capacity.  None of these capacities is a physical lower
bound.

## 4. First doubtful or unproved step

The first seam requiring independent verification is that every later
hard-TOP profile entering the literal packet still has the fixed,
finite-cell (C^1) interface stated in Section 2.  The accepted profile
nodes and the conductor candidate use that interface.  If a later packet
introduced an (L)-dependent family of hard transitions, its cardinality
must be inserted into (163.D30); the present proof must not be promoted
until that seam is green.  Subject to that inherited interface, there is
no doubtful algebraic or counting step in (163.D4).

The first unproved extension is to the complementary residual

\[
 b^{\rm rem}_{L,X}(N)
 =b_{L,X}(N)-b^{\rm cp}_{L,X}(N),
\tag{163.D38}
\]

which contains all products with no selected (L^{-1/2})-close
opposite-residue prime pair and all incidences containing neither or both
members of the selected pair.  No polynomial density, and not even a
per-block nonvacuity theorem, for (163.D3) was proved; the strict sector
may be empty for a particular product or block.  Even on products
admitting many exchanges,
(163.D7) leaves the sign-count discrepancy, literal profile transport,
and hard-window crossings.  Across (N), the arbitrary-real radical
phase still requires a genuinely analytic actual-coefficient theorem.

Accordingly, the following remains unproved:

\[
 \left|\sum_{N\asymp L^2}^{\rm lit}
 \mu^2(N)\left(\frac{L^2}{N}\right)^{3/4}
 e(J\sqrt N)b^{\rm rem}_{L,X}(N)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{163.D39}
\]

Neither the strict sector nor the leakage controls imply a lower bound
for (163.D39).

Comparison with the conductor's (163.C1)--(163.C16) formalization finds
no algebraic discrepancy.  The harmless (O(L)) term in (163.D4) is
absorbed by (L^{3/2}); the canonical rule here is slightly more general
but remains (N)-only and multiplicity one.  The three deliberately open
points agree: the later-profile seam above, density/nonvacuity, and the
uncovered incidence complement.  The zero-extended partner-leg count is
made explicit after (163.D30).

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_squarefree_product_grouping` | **GREEN.** The (t=1) bijection and exact upper near-square window are (163.D11)--(163.D12). |
| `odd_divisor_and_even_N_branch` | **GREEN.** (N=2M) is retained, (d_1\mid M) stays odd, and the factor (2) stays on (d_2) under the strict exchange. |
| `full_divisor_vs_truncated_window` | **GREEN obstruction.** (163.D33) does not estimate (163.D2); (163.D14) identifies the full leakage exactly. |
| `single_prime_toggle_domain` | **GREEN obstruction.** (163.D13) proves disjoint physical supports for every one-prime sign reversal. |
| `two_prime_exchange_matching` | **GREEN.** (163.D21) gives the exact ratio and residue condition; (163.D4) proves the close canonical sector; (163.D36) gives an unmatched (K_{1,2}) control. |
| `complementary_divisor_orientation` | **GREEN obstruction.** Odd (N) gives (163.D31); even (N) has an even physical complement and the separate odd-part identity (163.D32). |
| `character_sign_and_parity` | **GREEN.** The sign criterion is (chi_4(E)=-1); factor (2) cannot occur in an internal exchange. Complement reverses only for odd (3\pmod4)-prime parity. |
| `profile_window_and_endpoint_leakage` | **CANDIDATE GREEN for the strict sector, subject to the later-profile finite-cell seam in Section 4; OPEN globally.** Smooth differences and every recorded hard crossing, including zero-extended partner legs, are charged in (163.D27)--(163.D30). General profile transport remains in (163.D7). |
| `representable_sector_density_power` | **GREEN as a route control.** Products with no (3\pmod4) prime have no sign toggle; semiprimes already give (L^{2-o(1)}) diagnostic capacity, not polynomial sparsity. |
| `arbitrary_real_centre_phase` | **GREEN scope.** The strict swap preserves (N) and phase. Cross-product exact matching is unavailable uniformly; near-phase cancellation is not claimed. |
| `missing_L_half_power` | **GREEN for (163.D4), FAIL for the full route.** The close sector gains (L^{-1/2}); unmatched diagnostics retain (L^{2-o(1)}) capacity. |
| `physical_coefficient_vs_diagnostic` | **GREEN.** (163.D4) is a physical sector estimate. Counts (163.D35), (163.D37) are explicitly only constant-weight route diagnostics and not physical lower bounds. |
| `remaining_few_point_and_downstream_scope` | **GREEN quarantine.** No statement is made for the other (t\ll\sqrt L) channels, full hard TOP, smooth M2 packets, M9--M2, M9, the bridge, the quarter theorem, or either exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The derivation used the following selected context exactly:

- `protocol.md`;
- the active Round-163 nodes extracted from `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round163_m2_hard_top_t1_near_square_divisor_involution_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_divisor_involution_seed.md`;
- the conductor-authorized comparison candidate
  `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/synthesis.md`;
- `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`; and
- the conductor-authorized analogue
  `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`.

The accepted graph facts used are the literal (t=1) coefficient,
bounded (C^1) norm of \(\Phi\), fixed-rescaling profile regularity,
the even-(N) branch, and the exact radical-collision scope.  The M1
artifact is used only to compare full-minus-complement self-return; no M1
estimate is imported.  The fixed-modulus prime number theorem is used
only for the diagnostic counts (163.D35), (163.D37), not for the strict
physical estimate or its proposed state effect.

## 7. Recommended state effect

**Promote, after independent seam review, only the strict sector
(163.D4)** under the label
`strict_t1_prime_toggle_sector`.  Its exact owner is the canonical
(L^{-1/2})-close opposite-residue prime-pair, exactly-one-incidence
subsum of the physical (t=1) coefficient, including even (N), all
literal profile differences, and all hard crossings.

**Retain** (163.D5)--(163.D37) as a route-scoped divisor-involution
leakage obstruction: they exhaust one-prime toggles, arbitrary
multi-prime exchanges, complementary divisors, global matchings, cycles,
multiplicities, and weighted toggle averages, but they do not disprove a
different actual-coefficient theorem.

**No change** to the full (t=1) target, remaining few-point channels,
hard TOP, either smooth M2 packet, M9--M2, M9, endpoint assembly, the
conditional bridge, the quarter theorem, or either global exponent.

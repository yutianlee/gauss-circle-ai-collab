# Blind physical near-resonance mass report

- Campaign: gc-strategy-signed-moment-majorant-review
- Round: 202
- Task/role: blind_physical_near_resonance_mass / independent blind rederiver
- Access: statement-only; candidate evidence, not accepted proof state
- Starting graph SHA-256, copied solely from the permitted packet: 682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c
- Generated: 2026-09-23T20:41:58+08:00
- Allocation: 100% analytical/algebraic; no numerical experiments

## 1. Result

**Lemma proved from the exact-resonance bound granted in the packet.**
For the exact physical coefficients in the packet, there are fixed
\(0<a<b\) and \(h,c>0\), depending only on \(\Psi,w\), such that for every
sufficiently large real \(T\),
\[
 T\!\!\sum_{\substack{aT\le n_j\le bT\\
                 0<|\Delta|\le h/T}}
 \left(\prod_{j=1}^{12}a_{n_j}(T)\right)
 \operatorname{Re}\widehat w(-T\Delta)
 \ \ge cT^{5/2}.
\]
Every coefficient in this band is nonnegative. The strict deletion
\(\Delta=0\) is included in the proof.

This gives a no-go result for a termwise absolute Fourier majorant with
target \(O_\epsilon(T^{1+2\eta+\epsilon})\), for every \(\epsilon>0\),
when \(\eta<3/4\). It gives no lower bound for the complete signed
displaced moment or the modulus of its complete aggregate.

## 2. Exact statement and hypotheses

Let
\[
 r_2(n)=\#\{(u,v)\in\mathbb Z^2:u^2+v^2=n\},\qquad
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\quad n\ge1,\ T\ge2.
\]
Here \(\Psi\) is real, even, and Schwartz, with \(\Psi(0)=1\).
The fixed function \(w\in C_c^\infty((0,\infty))\) is nonnegative
and nonzero, and
\[
 \widehat w(\xi)=\int_0^\infty w(u)e^{-2\pi i u\xi}\,du,\qquad
 \Delta=\sum_{j=1}^6\sqrt{n_j}-\sum_{j=7}^{12}\sqrt{n_j}.
\]
Indices are positive integers; all twelve positions are ordered.

Choose \(0<\rho\le1\) so that \(\Psi(x)\ge1/2\) for \(|x|\le\rho\),
and put
\[
 b=\rho^2/4,\qquad a=b/4,\qquad
 W=\int_0^\infty w(u)\,du>0,\qquad
 U=\sup\operatorname{supp}w>0,\qquad h=(6U)^{-1}.
\]
Define
\[
 A_0=\frac{\pi(b-a)}{4b^{3/4}},\qquad
 B=\frac{6(\sqrt b-\sqrt a)}{h}+1,\qquad
 K=\frac{A_0^{12}}{B},\qquad c=\frac{WK}{4}>0.
\]
These choices are independent of \(T\).

The only granted non-elementary input is the packet's uniform weighted
exact-resonance bound. In the precise form used below, for
\[
 \beta_n=4\|\Psi\|_\infty\tau(n)n^{-3/4},
\]
there is a finite constant \(E_{12}\), independent of every cutoff,
bounding the full twelve-index exact-resonance sum over all signs with
weights \(\prod_j\beta_{n_j}\). Its one balanced-sign subsum is therefore
bounded by \(E_{12}\).

## 3. Proof or derivation

### Physical coefficient envelope

The elementary representation formula gives \(r_2(n)\le4\tau(n)\).
For completeness, write
\[
 n=2^e\prod_{p\equiv1\ (4)}p^{e_p}
          \prod_{q\equiv3\ (4)}q^{f_q}.
\]
Unique factorization in the Gaussian integers shows that \(r_2(n)=0\)
if some \(f_q\) is odd, and otherwise
\[
 r_2(n)=4\prod_{p\equiv1\ (4)}(e_p+1).
\]
Indeed, a prime \(q\equiv3\pmod4\) remains prime and its exponent in a
Gaussian integer of norm \(n\) is forced to be \(f_q/2\); the ramified
prime above \(2\) also has a forced exponent. For each split prime
\(p=\pi\overline\pi\), the two exponents have sum \(e_p\), giving
\(e_p+1\) choices, and there are four units. This proves the claimed
envelope. These are the usual elementary Gaussian-integer facts:
the norm Euclidean algorithm follows by rounding both coordinates;
the rational-prime alternatives follow from whether \(-1\) is a
quadratic residue modulo the odd prime.

For \(aT\le n\le bT\), the chosen band lies inside the positive region
of \(\Psi\), so
\[
 0\le a_n(T)\le\beta_n,\qquad
 a_n(T)\ge \tfrac12(bT)^{-3/4}r_2(n).
\]
Thus both positivity and the exact-resonance comparison hold for the
actual coefficients.

### Elementary band mass, uniformly for real \(T\)

Let \(d=\sqrt2/2\), and let \(N(R)\) count lattice points in the closed
disk of radius \(R\). Center a unit square at each lattice point.
These squares tile the plane up to boundaries. The union of squares
with centers in the disk is contained in the disk of radius \(R+d\)
and contains the disk of radius \(\max(R-d,0)\). Hence
\[
 |N(R)-\pi R^2|\le2\pi dR+\pi d^2.
\]
This bound holds for every real \(R\ge0\), without any assumption on
whether the boundary contains lattice points.

Consequently,
\[
 \sum_{aT\le n\le bT}r_2(n)
 \ge N(\sqrt{bT})-N(\sqrt{aT})
 \ge \pi(b-a)T
       -2\pi d(\sqrt b+\sqrt a)\sqrt T-2\pi d^2.
\]
The first inequality deliberately drops any points on the lower
boundary, which is harmless for this lower bound. In particular, for
\[
 T\ge T_{\rm area}:=
 \max\left\{2,\
    \left(\frac{8d(\sqrt b+\sqrt a)}{b-a}\right)^2,\
    \frac{8d^2}{b-a}\right\},
\]
the band count is at least \(\pi(b-a)T/2\). Thus
\[
 A(T):=\sum_{aT\le n\le bT}a_n(T)\ge A_0T^{1/4}.
\]
The integer set in this formula is exactly the closed band, equivalently
\(\lceil aT\rceil\le n\le\lfloor bT\rfloor\).

### Weighted pigeonhole bound for ordered six-root sums

For an ordered six-tuple \({\bf n}\) in the band, put
\[
 s({\bf n})=\sum_{j=1}^6\sqrt{n_j},\qquad
 v({\bf n})=\prod_{j=1}^6a_{n_j}(T)\ge0.
\]
All such sums lie in
\[
 [6\sqrt{aT},6\sqrt{bT}],
\]
whose length is \(6(\sqrt b-\sqrt a)\sqrt T\).
Partition this interval into half-open bins of width \(h/T\), starting
at \(6\sqrt{aT}\), including one final bin to contain the upper endpoint.
The number of bins is
\[
 m=\left\lfloor
       \frac{6(\sqrt b-\sqrt a)}{h}T^{3/2}
    \right\rfloor+1
 \le BT^{3/2}\qquad(T\ge1).
\]
The explicit extra bin makes this valid even when the ratio is an integer.

Let \(V_\ell\) be the sum of \(v({\bf n})\) over six-tuples in bin
\(\ell\). Then
\[
 \sum_{\ell=1}^{m}V_\ell=A(T)^6,\qquad
 \sum_{\ell=1}^{m}V_\ell^2
       \ge \frac{A(T)^{12}}{m}
       \ge KT^{3/2}.
\]
Here the first equality is the expansion of the sixth power of a
finite sum, and the inequality is Cauchy--Schwarz.

Each product counted by \(V_\ell^2\) is an ordered pair of ordered
six-tuples and therefore exactly an ordered twelve-tuple. Its difference
of root sums has \(|\Delta|<h/T\). No factor \(6!\), \(12!\), or symmetry
quotient is introduced. We conclude
\[
 \sum_{\substack{aT\le n_j\le bT\\|\Delta|\le h/T}}
       \prod_{j=1}^{12}a_{n_j}(T)
 \ge KT^{3/2}.
\]

### Removing the exact resonances

Let \(E(T)\) be the same weighted band sum with \(\Delta=0\).
The fixed coefficient envelope and the granted exact-resonance input give
\[
 0\le E(T)\le E_{12}.
\]
In particular, the input is not being applied to an unproved estimate
for near resonances. It is used only to delete \(\Delta=0\).
Subtracting yields
\[
 \sum_{\substack{aT\le n_j\le bT\\0<|\Delta|\le h/T}}
       \prod_{j=1}^{12}a_{n_j}(T)
 \ge KT^{3/2}-E_{12}.
\]
For
\[
 T\ge T_*:=
  \max\{T_{\rm area},(2E_{12}/K)^{2/3}\},
\]
this is at least \(KT^{3/2}/2\). This comparison also removes exact
relations other than matching permutations; their structure is not
being assumed.

### The physical Fourier weight

For \(|\xi|\le h\), every \(u\) in the support of \(w\) satisfies
\(|2\pi u\xi|\le\pi/3\). Since \(w\ge0\),
\[
 \operatorname{Re}\widehat w(\xi)
     =\int w(u)\cos(2\pi u\xi)\,du
     \ge W/2.
\]
Thus all summands in the stated nonzero near-resonance band are
nonnegative. For \(T\ge T_*\),
\[
 T\!\!\sum_{\substack{aT\le n_j\le bT\\0<|\Delta|\le h/T}}
       \left(\prod_j a_{n_j}(T)\right)
       \operatorname{Re}\widehat w(-T\Delta)
 \ge \frac W2 T\cdot\frac K2T^{3/2}
 =cT^{5/2}.
\]
This proves the candidate.

### Exact scope of the absolute-majorant obstruction

For example, define the nonzero-frequency termwise absolute sum
\[
 {\cal M}^{\ne0}_{12}(T)=
 T\sum_{\boldsymbol\varepsilon\in\{\pm1\}^{12}}
 \sum_{\substack{n_1,\ldots,n_{12}\ge1\\
             \sum_j\varepsilon_j\sqrt{n_j}\ne0}}
 \left|\prod_j a_{n_j}(T)\right|
 \left|\widehat w\left(-T\sum_j\varepsilon_j\sqrt{n_j}\right)\right|.
\]
It contains the sign vector with six plus signs followed by six minus
signs. On our band, \(|\widehat w|\ge\operatorname{Re}\widehat w\ge W/2\).
Therefore
\[
 {\cal M}^{\ne0}_{12}(T)\ge cT^{5/2}.
\]
Including exact frequencies only increases this majorant. Fixed
normalizing factors, such as \(2^{-12}\) from expanding twelve cosines,
change the positive constant and not the exponent.

For any fixed \(\eta<3/4\), select
\[
 0<\epsilon<\frac32-2\eta.
\]
Then \(1+2\eta+\epsilon<5/2\), so the displayed majorant cannot be
\(O(T^{1+2\eta+\epsilon})\). Equivalently, a claim with the usual
quantifier “for every \(\epsilon>0\)” is impossible for such \(\eta\).
There is no contradiction for an arbitrarily large fixed \(\epsilon\)
whose exponent is at least \(5/2\).

This argument applies to replacing each Fourier expansion term by its
absolute value. It does not apply to retaining cancellations and then
taking one modulus outside the complete aggregate. Terms outside our
small-frequency band may have negative real part; neither their signed
sum nor its interaction with other sign vectors is controlled here.

### General balanced power and low-order check

For ordered \(k\)-root sums, the identical bin argument has at most
\[
 B_kT^{3/2},\qquad B_k=k(\sqrt b-\sqrt a)/h+1
\]
bins and total \(k\)-tuple weight \(A(T)^k\). Before deleting exact
frequencies, the pair mass is at least
\[
 K_kT^{k/2-3/2},\qquad K_k=A_0^{2k}/B_k.
\]
The granted uniform exact-resonance bound for \(2k\) indices permits
deletion once \(k>3\), giving, for sufficiently large \(T\),
\[
 T\!\!\sum_{\substack{aT\le n_j\le bT\\0<|\Delta_k|\le h/T}}
 \left(\prod_{j=1}^{2k}a_{n_j}(T)\right)
 \operatorname{Re}\widehat w(-T\Delta_k)
 \ge c_kT^{(k-1)/2}\qquad(k\ge4).
\]
Thus the eighth, tenth, and twelfth balanced powers give exponents
\(3/2,2,5/2\), respectively.

For \(k\le3\), this proof does not survive the exact-frequency deletion:
the pre-deletion lower bound is at most constant while the supplied
exact bound is \(O(1)\). In particular it gives no obstruction to an
\(O(T)\) low-order moment. For \(k=1\) there are actually no such
nonzero near resonances at all for large \(T\): if distinct integers
\(n,m\le bT\), then
\[
 |\sqrt n-\sqrt m|
   =\frac{|n-m|}{\sqrt n+\sqrt m}
   \ge\frac1{2\sqrt{bT}}>\frac hT
\]
once \(\sqrt T>2h\sqrt b\). This is a direct control showing why an
argument that neglected exact-frequency deletion would be invalid.

## 4. First doubtful or unproved step

There is no unproved step in the stated lower bound once the packet's
uniform exact-resonance theorem is granted. That theorem is explicitly
an input, not rederived here. The elementary coefficient envelope and
band count are supplied above.

The first unjustified step in any stronger conclusion would be to infer
that the complete signed displaced moment is bounded below by this
positive spectral subsum. Such an inference would require control of
the complementary signed terms, which has not been supplied and is not
asserted. Likewise, this report neither establishes nor excludes a
method that truncates below every fixed positive multiple of \(T\) and
then proves a separate signed tail/reconstruction estimate.

## 5. Control tests and outcomes

- **Physical coefficients / positivity — pass.** The exact
  \(r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\) occurs throughout. Its mass follows
  from an annular lattice count, and \(\Psi\ge1/2\) on the chosen band.
  Global positivity of \(\Psi\) is unnecessary.
- **Fourier support and positivity — pass.** The explicit
  \(h=(6U)^{-1}\) gives \(\operatorname{Re}\widehat w\ge W/2\).
  The fact that \(w\) is supported away from zero causes no difficulty.
- **Ordered multiplicities — pass.** The equality
  \(\sum_\ell V_\ell=A(T)^6\) and its square count ordered tuples
  exactly once in their assigned bin; no permutation quotient is used.
- **Exact/nonzero resonance split — pass.** All exact relations,
  not merely diagonal permutations, cost at most \(E_{12}=O(1)\) before
  the outside factor \(T\). The close-pair mass is \(\gg T^{3/2}\),
  so the deletion leaves a positive lower bound.
- **Real endpoint uniformity — pass.** The disk count is valid for
  every real radius. Closed integer bands and half-open bins include
  both possible boundary coincidences without rounding assumptions.
- **Finite versus infinite source scope — pass.** The proof itself
  uses only finite band sums. For fixed \(T\), Schwartz decay and
  \(\tau(n)\le2\sqrt n\) imply
  \(\sum_{n\ge1}|a_n(T)|<\infty\); for example, for \(n\ge T\), a
  fourth-order Schwartz bound gives
  \(|a_n(T)|\ll_\Psi T^2n^{-9/4}\).
  Since \(|\widehat w|\le W\), the infinite twelve-fold absolute
  expansion also converges for each fixed \(T\).
  A hard cutoff containing the band inherits the lower bound. A
  shorter cutoff is not silently substituted for the full source.
- **Signed/absolute distinction — pass.** Only the termwise absolute
  Fourier sum is obstructed. A positive spectral subsum is not
  declared a lower bound for the total signed moment.
- **All costs restored — pass.** The coefficient mass is
  \(T^{1/4}\), the squared six-tuple mass is \(T^3\), the bin count is
  \(T^{3/2}\), and the outside integration scale is \(T\).
  Their combined power is \(T^{5/2}\). Exact-frequency subtraction
  costs only \(O(T)\) after that outside factor.
- **Independent statement-only control — pass.** No graph,
  campaign manifest, strategy, claimant derivation, sibling report,
  or historical report was read.
- **Current primary hypotheses / withdrawals and versions — not
  applicable to external sources.** No external theorem or literature
  citation is used; there is no unverified current-source import.
  The one granted exact-resonance input is used precisely as stated
  in the isolated packet.
- **Full proof frontier / no parent or exponent overclaim — pass.**
  This proves a lower-bound obstruction, not a global circle exponent,
  a pointwise bridge, a signed moment estimate, or the success of an
  alternative analytic route. The low-order check records the limit
  \(k>3\) of the nonzero-frequency argument.
- **Numerical controls — not used.** Every control above is
  algebraic or analytical, as required.

## 6. Dependencies and exact artifacts used

Only the following files were read:

1. protocol.md
2. rounds/codex-managed/gc-strategy-signed-moment-majorant-review/briefs/blind_physical_mass_statement.md
3. rounds/codex-managed/gc-strategy-signed-moment-majorant-review/briefs/blind_physical_near_resonance_mass.md

Mathematical dependencies are the uniform weighted exact-resonance bound
explicitly granted by item 2; the elementary Gaussian-integer coefficient
formula explained above; unit-square lattice area comparison;
Cauchy--Schwarz; continuity at \(\Psi(0)=1\); and the elementary cosine
bound on the Fourier transform of nonnegative \(w\).
No numerical, web, historical, or sibling evidence was used.

## 7. Recommended state effect

**Promote the isolated physical nonzero near-resonance lower bound after
the conductor's required seam checks, and reject the corresponding
termwise absolute-majorant route below \(\eta=3/4\).**

Retain the complete signed aggregate as a separate unresolved object.
No state change to a global exponent, signed moment, parent theorem,
cutoff-tail argument, or pointwise reconstruction follows from this
report. The conductor alone should perform any authoritative state patch.

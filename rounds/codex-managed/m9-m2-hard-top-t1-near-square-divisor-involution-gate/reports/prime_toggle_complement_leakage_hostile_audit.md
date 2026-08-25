# Round 163 hostile audit: close-prime sector and divisor-involution leakage

## 1. Result: strict_t1_prime_toggle_sector

There is one genuine target-safe sector, but the unrestricted
prime-toggle/complement proposal self-returns.

Fix \(c>0\).  For every squarefree \(N\) in the literal \(t=1\) support,
choose canonically at most one unordered pair
\(\{p_N,q_N\}\) of distinct odd prime divisors of \(N\) such that

\[
 \chi _4(p_N)=-\chi _4(q_N),
 \qquad
 |\log(p_N/q_N)|\le cL^{-1/2};
\tag{163.R1}
\]

for example choose the lexicographically first eligible pair, and choose
none if there is no eligible pair.  Restrict to physical factorizations
\(N=d_1d_2\) in which exactly one of \(p_N,q_N\) divides \(d_1\).
The exchange of \(p_N\) and \(q_N\) between \(d_1,d_2\) is a
fixed-point-free sign-reversing involution.  With every literal shell,
cone, profile, floor, star, endpoint and zero extension retained, its
complete sector satisfies

\[
 \boxed{\left|\mathcal S_{L,1}^{\rm close-prime}(c)\right|
 \ll_c L^{3/2}+L
 \ll_{c,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{163.R2}
\]

The proof uses no prime-density or divisor-distribution theorem.  On the
common interior, the accepted smooth \(\eta_L,W\) profiles and accepted
\(C^1\) Vaaler profile \(\Phi\) change by \(O_c(L^{-1/2})\).
All atoms whose half-open shell, cone, endpoint or zero-extension status
changes lie in finitely many relative \(O_c(L^{-1/2})\) lattice collars,
containing \(O_c(L^{3/2}+L)\) integer pairs.  Canonical selection gives
multiplicity one.

This is a complete conditional sub-sum: it proves no density, nonempty
asymptotic range, or positive proportion for (163.R1).  It therefore
does not estimate the complementary \(t=1\) atoms.

Outside this strict sector, the hostile classification is:

1. A one-prime \(p\equiv3\pmod4\) toggle has no physical edge in
   \([\sqrt N,2\sqrt N]\).  Its exact difference formula is all leakage.
   Averaging over every such prime is an exact self-return, with the
   same positive mass as the original coefficient.
2. Every two/multi-prime exchange is classified by disjoint odd
   squarefree factors \(A,B\), with \(d'=dB/A\).  It reverses sign
   exactly when \(\chi _4(AB)=-1\), and both endpoints can be physical
   only when \(1/2\le B/A\le2\).  The unrestricted internal graph is
   complete bipartite on the two character signs.  A perfect matching
   exists exactly when the sign counts agree; restricted exchange rules
   also require Hall's condition.
3. Every partial matching leaves the exact sum of unmatched profiles and
   paired profile differences.  Every sign-reversing permutation has
   even cycles and gives the same profile-gradient identity.  Graph
   averaging does not erase singleton/same-sign fibres.
4. Odd complementation sends the upper window to the excluded lower
   window.  If \(N=2M\), the factor swap \(N/d\) is even, while the
   character-preserving odd complement \(M/d=N/(2d)\) lies still lower,
   in \([\sqrt N/4,\sqrt N/2]\).  Neither is an upper-window symmetry.
5. Full-divisor vanishing makes the truncation equal to its uncontrolled
   complement; it does not make the truncation small.  The squarefree
   representable sector has only \(+1\) divisor characters and hence no
   sign-reversing edge.

Thus (163.R2) earns only strict_t1_prime_toggle_sector.  The complete
\(t=1\) target remains open.  The exact finite fibres below are controls
on algebraic overclaims, not physical lower bounds.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,\qquad 1\ll L\ll H\le J^{1/2}.
\tag{163.S1}
\]

All inherited half-open supports, cone inequalities, endpoint values,
floors, stars and zero extensions are literal.  For squarefree
\(N>1\) in the actual \(N\asymp L^2\) support define

\[
 \mathscr D_N=
 \{d:d\mid N,\ d\ {\rm odd},\ \sqrt N\le d\le2\sqrt N\},
\tag{163.S2}
\]

\[
 A_N(d)=\mathbf 1_{\mathscr D_N}(d)\,
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right)
\tag{163.S3}
\]

for every odd divisor \(d\mid N\), with value zero off the literal
support.  Then

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\chi _4(d)A_N(d),
\tag{163.S4}
\]

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}
 e(J\sqrt N)b_{L,X}(N).
\tag{163.S5}
\]

The accepted actual-symbol regularity used for (163.R2) is the fixed
scale-normalized smoothness of \(\eta_L\) and \(W\), the bounded
\(C^1([0,1])\) norm of \(\Phi\), and bounded profile size.  Equivalently,
on a common physical cell,

\[
 L\|\eta_L'\|_\infty+\|W'\|_\infty+\|\Phi'\|_\infty\ll1.
\tag{163.S6}
\]

For disjoint odd squarefree \(A,B\mid N\), an \(A\)-to-\(B\) exchange is

\[
 d'=d\frac BA,\qquad A\mid d,\qquad B\mid N/d.
\tag{163.S7}
\]

Every exchange between two odd divisors of squarefree \(N\) has this
form uniquely after setting

\[
 g=(d,d'),\qquad A=d/g,\qquad B=d'/g.
\tag{163.S8}
\]

It obeys

\[
 \frac{\chi _4(d')}{\chi _4(d)}=\chi _4(AB),
\qquad
 d,d'\in\mathscr D_N\Longrightarrow \frac12\le\frac BA\le2,
\tag{163.S9}
\]

and the exact physical-domain condition is

\[
 d\in[\sqrt N,2\sqrt N]\cap
 \left[\frac AB\sqrt N,\frac{2A}B\sqrt N\right].
\tag{163.S10}
\]

No factor \(2\) can occur in \(A\) or \(B\), since both endpoints are
odd.

Let

\[
 \mathscr D_N^\pm=\{d\in\mathscr D_N:\chi _4(d)=\pm1\},
\qquad n_\pm(N)=|\mathscr D_N^\pm|.
\tag{163.S11}
\]

For any partial matching \(M_N\) between opposite signs, oriented from
the positive endpoint \(u\) to the negative endpoint \(v\), with
unmatched set \(U_N\), one has exactly

\[
 \boxed{
 b_{L,X}(N)=
 \sum_{(u,v)\in M_N}\{A_N(u)-A_N(v)\}
 +\sum_{u\in U_N}\chi _4(u)A_N(u).}
\tag{163.S12}
\]

Consequently a matching followed by a positive norm still has to prove

\[
 \sum_{N\asymp L^2}\left(
 \sum_{(u,v)\in M_N}|A_N(u)-A_N(v)|
 +\sum_{u\in U_N}|A_N(u)|
 \right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{163.S13}
\]

The close-prime canonical sector proves (163.S13) for its own atoms.
No comparable estimate is proved for its complement.

## 3. Proof or derivation

### 3.1 Literal product grouping, normalization and parity

In the \(t=1\) scalar, \(d_1,d_2\) are squarefree and coprime.  Hence
\(N=d_1d_2\) is squarefree.  Conversely, squarefree \(N\) and a divisor
\(d=d_1\mid N\) determine \(d_2=N/d\) uniquely and make the factors
squarefree and coprime.  Thus the grouping has multiplicity one.  The
cone gives

\[
 d_2\le d_1\le4d_2
 \Longleftrightarrow N\le d_1^2\le4N
 \Longleftrightarrow \sqrt N\le d_1\le2\sqrt N,
\tag{163.P1}
\]

and

\[
 \sqrt{\frac{q_Xd_1}{4d_2}}
 =\frac{\sqrt{q_X}\,d_1}{2\sqrt N}.
\tag{163.P2}
\]

The outer normalization \((L^2/N)^{3/4}\), the \(N\)-shell and
\(e(J\sqrt N)\) are common to a fibre.  The first factor is odd.  If
\(N\) is even, squarefreeness forces \(2\mid d_2\); this branch survives
the grouping.

For active squarefree \(N>1\), the cone has no hidden fixed point:
\(d=\sqrt N\) would make \(N\) a square, while an odd
\(d=2\sqrt N\) would give \(d^2=4N\).  Exact endpoint conventions still
matter when an exchange crosses a shell or cone face, and remain in
(163.S3).

### 3.2 Proof of the canonical close-prime sector

For \(N\) with a canonical pair \(\{p,q\}\) satisfying (163.R1), define
the swap on ambient factorizations containing exactly one of them in
\(d_1\) by

\[
 T(d_1,d_2)=
 \begin{cases}
 (d_1q/p,d_2p/q),&p\mid d_1,\\
 (d_1p/q,d_2q/p),&q\mid d_1.
 \end{cases}
\tag{163.P3}
\]

Because \(N\) is squarefree, the prime absent from \(d_1\) is present in
\(d_2\).  Hence (163.P3) is integral, preserves \(d_1d_2=N\),
squarefreeness and coprimality, and is an involution.  It has no fixed
point because \(p\ne q\).  Both primes are odd, so oddness of \(d_1\)
and the even-\(d_2\) branch are preserved.  The canonical pair depends
only on \(N\), so applying \(T\) cannot change the choice or create
multiplicity.  Finally,

\[
 \chi _4(d_1')=-\chi _4(d_1).
\tag{163.P4}
\]

Let \(a_{L,X}(d_1,d_2)\) denote the entire literal normalized profile in
(163.S5), including every support indicator but excluding
\(\chi _4(d_1)e(J\sqrt N)\), and extend it by zero.  Pairing complete
ambient \(T\)-orbits gives the exact identity

\[
\begin{aligned}
 \mathcal S_{L,1}^{\rm close-prime}(c)
 =\frac12\sum_{\substack{(d_1,d_2)\\
                         \text{exactly one of }p_N,q_N\mid d_1}}
 &\chi _4(d_1)e(J\sqrt N)\\
 &\times\{a_{L,X}(d_1,d_2)-a_{L,X}(T(d_1,d_2))\}.
\end{aligned}
\tag{163.P5}
\]

The sum may be restricted to the union of the literal support and its
image.  Both lie in a fixed \(O(L)\)-by-\(O(L)\) lattice box.

Put \(\delta=c_1(c)L^{-1/2}\).  From (163.R1),

\[
 \max\{|p/q-1|,|q/p-1|\}\le\delta
\tag{163.P6}
\]

for all sufficiently large \(L\).  On a cell for which both an atom and
its image have the same literal support status, the first coordinate
changes by \(O(\delta L)\), the \(W\)-argument changes multiplicatively
by \(1+O(\delta)\), \(N,H,y,q_X\) stay fixed, and (163.S6) gives

\[
 |a_{L,X}(d_1,d_2)-a_{L,X}(T(d_1,d_2))|
 \ll_c \delta.
\tag{163.P7}
\]

For the Vaaler factor this uses
\[
 \left|\frac{d_1'-d_1}{H+1}\right|
 \ll \frac{\delta L}{H}\le\delta;
\]
there is no replacement of \(H+1\), \(q_X\), a floor, or a star.

It remains to count status changes.  Every hard shell endpoint is a
fixed one-variable boundary at scale \(L\).  Every cone or \(W\)-support
endpoint is a fixed ratio boundary \(d_1=\lambda d_2+O(1)\) at scale
\(L\).  The exchange changes \(\log(d_1/d_2)\) by
\(O(\delta)\).  Thus a crossing atom lies in one of finitely many collars

\[
 |d_1-\lambda d_2|\ll_c\delta L
 \quad\text{or}\quad
 |d_i-\lambda L|\ll_c\delta L.
\tag{163.P8}
\]

For each fixed \(d_2\asymp L\), the first collar contains
\(O_c(\delta L+1)\) possible \(d_1\); the one-variable collars have the
same count after summing the other coordinate.  Hence

\[
 \#\{\text{all crossing atoms}\}
 \ll_c L(\delta L+1)
 \ll_c L^{3/2}+L.
\tag{163.P9}
\]

Exact equality samples, ceiling effects and star changes lie on the
same boundary lines and contribute only the \(O(L)\) term.  The
squarefree, coprime, odd and canonical-prime restrictions only delete
lattice pairs, so no divisor-distribution estimate enters (163.P9).
The \(N\)-shell never crosses because \(N\) is unchanged.

There are \(O(L^2)\) common-interior pairs.  Combining bounded endpoint
weights, (163.P7), (163.P9), and (163.P5) gives

\[
 |\mathcal S_{L,1}^{\rm close-prime}(c)|
 \ll_c L^2\delta+(L^{3/2}+L)
 \ll_c L^{3/2}+L,
\]

which proves (163.R2).  This argument owns the complete selected sector,
including images that leave the physical cone.  It makes no assertion
about how many \(N\) possess an eligible prime pair.

The lack of a density theorem does not invalidate this particular exit
label.  The selected object is an exact invariant incidence sub-sum, not
an exceptional-set estimate whose complement is inferred to be small.
It is also not a formally impossible incidence condition: for example
the opposite-residue primes \(11,13\) meet
\(|\log(13/11)|<16^{-1/2}\), and their allocation in
\(N=143\) gives an exact close-pair orbit on the compatible \(L=16\)
scale (whether a particular literal smooth profile vanishes at one
sample is irrelevant to the definition and upper bound).  What is not
proved is occurrence at every large scale or positive density.  Hence
the result is nonvacuous as a typed strict sector, but it removes no
quantified proportion from the open parent.

### 3.2a Hostile line audit of the conductor candidate C1--C16

The independently supplied conductor candidate is green on its finite
kernel, with the following scope qualifications.

| Candidate item | Hostile finding |
|---|---|
| C1 | Green.  Opposite nonzero residue classes are exactly \(\chi _4(pq)=-1\); the logarithmic threshold is symmetric in the unordered pair. |
| C2 | Green as a sector bound, by (163.P5)--(163.P9).  It is not a bound for the incidence complement. |
| C3--C4 | Green.  These are (163.S4)--(163.S5), with the even-\(N\) branch and zero extension retained. |
| C5--C6 | Green from the accepted state nodes H4-Phi-regularity and M9-M2-top-endpoint-actual-symbol-variation.  The frozen symbol contains only the fixed smooth \(\eta_L,W\) cells and the \(C^1\) \(\Phi\) factor; Round 137 and Round 162 inherit rather than add an \(L\)-dependent transition family.  Every non-smooth cell seam is therefore among the finite faces counted in (163.P8)--(163.P9). |
| C7 | Green.  Lexicographic minimization is unique; labelling by the two different residues removes orientation ambiguity and depends only on \(N\). |
| C8--C9 | Green.  The “exactly one” selector is invariant under exchange, and the literal physical indicator belongs to \(A_N\), not to the ambient divisor domain. |
| C10--C11 | Green.  Squarefreeness makes both quotients integral; product, coprimality, oddness, the even branch and canonical choice are preserved; distinct primes give no fixed point and the character reverses. |
| C12 | Green only with the stated zero extension.  The sum is over the complete ambient exactly-one divisor set.  Terms for which both partners are outside vanish; if at least one partner is physical, closeness places both in one fixed expanded \(O(L)\) box, so no uncounted divisor tail remains. |
| C13--C15 | Green.  Both orientations use \(\pm\theta_N\); \(N,H,y,q_X\) stay fixed, \(W\)'s argument scales by \(e^{\pm\theta_N}\), and \(\Phi\) costs \(|\theta_N|L/H\), with no floor replacement. |
| C16 | Green.  Each ratio or one-variable seam has \(O_\kappa(L^{1/2}+1)\) possible partners per row.  Half-open ties, ceilings and star changes are lattice faces and supply the \(O(L)\) term.  Arithmetic selectors only delete pairs, so no prime/divisor counting hypothesis is hidden. |

This audit supplies the requested profile-interface provenance and
zero-extended partner count.  In particular, C12 would be false if its
ambient domain were silently replaced by physical divisors before
reindexing; the candidate and (163.P5) do not make that replacement.

### 3.3 One-prime toggles and their exact averaging self-return

Let \(p\mid N\) be odd and \(p\equiv3\pmod4\).  Pair full odd divisors as
\((d,pd)\) with \(d\mid N/p\).  Then

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi _4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.P10}
\]

The two profile terms have disjoint physical supports.  If
\(A_N(d)\ne0\), then \(pd\ge3\sqrt N>2\sqrt N\); if
\(A_N(pd)\ne0\), then \(d\le2\sqrt N/p<\sqrt N\).  Therefore

\[
 \sum_{d\mid N/p}|A_N(d)-A_N(pd)|
 =\sum_{\substack{r\mid N\\r\ {\rm odd}}}|A_N(r)|.
\tag{163.P11}
\]

Let
\[
 \mathcal P_3(N)=\{p\mid N:p\equiv3\pmod4\},
 \qquad k_3(N)=|\mathcal P_3(N)|.
\]
Summing (163.P10) yields

\[
 k_3(N)b_{L,X}(N)
 =\sum_{p\in\mathcal P_3(N)}
 \sum_{d\mid N/p}\chi _4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.P12}
\]

For a fixed physical \(r\), a prime \(p\nmid r\) contributes
\(\chi _4(r)A_N(r)\) through the first term.  A prime \(p\mid r\)
contributes
\(-\chi _4(r/p)A_N(r)=\chi _4(r)A_N(r)\) through the second.
Every physical term is therefore reinforced exactly \(k_3(N)\) times,
and, when \(k_3(N)>0\),

\[
 \frac1{k_3(N)}\sum_{p\in\mathcal P_3(N)}
 \sum_{d\mid N/p}|A_N(d)-A_N(pd)|
 =\sum_r|A_N(r)|.
\tag{163.P13}
\]

There is no averaging gain.  If \(p\equiv1\pmod4\), the paired
characters have the same sign.  If \(p=2\), the toggle leaves the odd
divisor lattice.  This exhausts one-prime toggles.

### 3.4 General exchanges, matching consistency and cycles

Equations (163.S8)--(163.S10) prove the complete local classification.
For a two-prime exchange \(A=p,B=q\), the primes must have opposite
nonzero residue classes modulo \(4\), and \(1/2\le q/p\le2\) is
necessary.  In a fixed two-coordinate toggle, divisors containing
neither or both primes change by a factor \(pq\) or \(1/(pq)\), so those
orbits cannot be internally physical; only the genuine one-for-one
exchange state can be.

For any fixed set \(E\) of odd prime coordinates, define

\[
 T_E(d)=d\,
 \frac{\prod_{p\in E,\ p\nmid d}p}
      {\prod_{p\in E,\ p\mid d}p}.
\tag{163.P14}
\]

It is an involution of the full odd-divisor cube and

\[
 \chi _4(T_Ed)=\chi _4(d)\prod_{p\in E}\chi _4(p).
\tag{163.P15}
\]

It reverses sign exactly when \(E\) contains an odd number of
\(3\pmod4\) primes.  Its orbits split into internal profile-difference
pairs, one-sided leakage pairs, and pairs with both terms outside.
Averaging identities over many \(E\) averages exact copies of
\(b_{L,X}(N)\); it gives a gain only if a new aggregate profile-gradient
bound is proved.

If arbitrary multi-prime exchanges are allowed, every opposite-sign
pair \(d,d'\in\mathscr D_N\) defines (163.S8).  Thus the unrestricted
internal graph is

\[
 \mathcal G_N=K_{n_+(N),n_-(N)}.
\tag{163.P16}
\]

A perfect sign-reversing involution exists exactly when
\(n_+(N)=n_-(N)\).  A prescribed exchange subgraph additionally needs
Hall's condition; the existence of some partner for every vertex does
not prove injectivity.  Formula (163.S12) follows by summing each
positive-negative pair.

If \(\pi\) is any sign-reversing permutation of \(\mathscr D_N\), every
cycle is even and

\[
 2b_{L,X}(N)=
 \sum_{d\in\mathscr D_N}\chi _4(d)
 \{A_N(d)-A_N(\pi d)\}.
\tag{163.P17}
\]

This follows by changing variables in the second sum.  Convex graph
averaging is therefore only a transport average of literal profile
gradients; cycles do not telescope the alternating profile sum.

The following exact constant-profile controls falsify universal
combinatorial cancellation claims.  They are not literal-profile lower
bounds.

* \(N=15=3\cdot5\) has \(\mathscr D_N=\{5\}\), while
  \(\sum_{d\mid15}\chi _4(d)=0\).  Full-divisor vanishing and the
  \(p=3\) toggle leave a singleton physical coefficient \(+1\).
* \(N=65=5\cdot13\) has \(\mathscr D_N=\{13\}\).  All odd prime factors
  are \(1\pmod4\), so there is no negative vertex.
* \(N=1365=3\cdot5\cdot7\cdot13\) satisfies
  \(36^2<N<37^2\) and
  \(\mathscr D_N=\{39,65\}\), of signs \(-,+\).
  The valid exchange \(39\leftrightarrow65\) replaces \(3\) by \(5\)
  and has ratio \(5/3\), but the literal coefficient is
  \(A_N(65)-A_N(39)\), not an identity zero.
* \(N=15015=3\cdot5\cdot7\cdot11\cdot13\) satisfies
  \(122^2<N<123^2\) and
  \[
   \mathscr D_N=\{143,165,195,231\},\qquad
   (\chi _4)=(-,+,-,-).
  \tag{163.P18}
  \]
  The positive vertex \(165\) has valid exchanges with all three
  negative vertices, of ratios \(15/13,13/11,7/5\).  Partner existence
  holds, but every matching leaves two negative vertices.  The
  constant-profile truncated sum is \(-2\).
* \(N=23205=3\cdot5\cdot7\cdot13\cdot17\) satisfies
  \(152^2<N<153^2\) and
  \[
   \mathscr D_N=\{195,221,255,273\},\qquad
   (\chi _4)=(-,+,-,+).
  \tag{163.P19}
  \]
  It has perfect matchings and the sign-reversing four-cycle
  \[
   195\longmapsto221\longmapsto255\longmapsto273
   \longmapsto195,
  \tag{163.P20}
  \]
  with successive ratios \(17/15,15/13,91/85,5/7\), whose product is
  \(1\).  The constant-profile sum vanishes, while the literal sum is
  \[
   A_N(221)+A_N(273)-A_N(195)-A_N(255).
  \tag{163.P21}
  \]
  Either perfect matching merely rewrites (163.P21) as two profile
  differences.

The divisor lists follow by exact factor enumeration within the
displayed square bounds.  No numerical search is used.

### 3.5 Odd and even complementation

For odd \(N\), put \(e=N/d\).  Then

\[
 d\in[\sqrt N,2\sqrt N]
 \Longleftrightarrow e\in[\sqrt N/2,\sqrt N],
 \qquad
 \chi _4(d)=\chi _4(N)\chi _4(e),
\tag{163.P22}
\]

so

\[
\begin{aligned}
 b_{L,X}(N)=\chi _4(N)
 \sum_{\substack{e\mid N\\\sqrt N/2\le e\le\sqrt N}}
 &\chi _4(e)\eta_L(N/e)
 \Phi\!\left(\frac{N}{e(H+1)}\right)\\
 &\times W\!\left(\frac{\sqrt{q_XN}}{2e}\right).
\end{aligned}
\tag{163.P23}
\]

This is an excluded lower interval with the literal height and endpoint
profiles evaluated at \(N/e\).

Now let \(N=2M\) be squarefree, with \(M\) odd.  The factor swap \(N/d\)
of a physical odd divisor is even and has no character-supported
physical role.  The odd-divisor involution is
\(e=M/d=N/(2d)\), and

\[
 d\in[\sqrt N,2\sqrt N]
 \Longleftrightarrow e\in[\sqrt N/4,\sqrt N/2],
 \qquad
 \chi _4(d)=\chi _4(M)\chi _4(e).
\tag{163.P24}
\]

Hence

\[
\begin{aligned}
 b_{L,X}(2M)=\chi _4(M)
 \sum_{\substack{e\mid M\\\sqrt N/4\le e\le\sqrt N/2}}
 &\chi _4(e)\eta_L(M/e)
 \Phi\!\left(\frac{M}{e(H+1)}\right)\\
 &\times W\!\left(\sqrt{\frac{q_XM}{8e^2}}\right).
\end{aligned}
\tag{163.P25}
\]

No \(q_X\to1\), \(H+1\to H\), floor or endpoint replacement has been
made.  Applying the odd-part complement again returns (163.S4).

The exact even control \(N=210=2\cdot3\cdot5\cdot7\) has
\(\mathscr D_N=\{15,21\}\), with signs \(-,+\).  Their factor swaps are
\(14,10\), both even, whereas their odd-part complements are \(7,5\)
in \([\sqrt N/4,\sqrt N/2]\).  The valid prime exchange
\(15\leftrightarrow21\) leaves \(A_N(21)-A_N(15)\).  Thus an even
physical-complement symmetry is false, and an odd-prime exchange is
logically separate from complementation.

### 3.6 Full-divisor completion, representable products, and power

Write \(N=2^\nu M\), \(\nu\in\{0,1\}\), \(M\) odd.  Then

\[
 F(N)=\sum_{d\mid M}\chi _4(d)
 =\prod_{p\mid M}(1+\chi _4(p))
 =\frac{r_2(N)}4.
\tag{163.P26}
\]

Thus \(F(N)=0\) if an odd \(3\pmod4\) prime divides \(N\), and
\(F(N)=2^{\omega(M)}\) otherwise.  For the unweighted physical
coefficient \(C_0(N)=\sum_{d\in\mathscr D_N}\chi _4(d)\),

\[
 C_0(N)=F(N)-
 \sum_{\substack{d\mid M\\d\notin\mathscr D_N}}\chi _4(d).
\tag{163.P27}
\]

The \(N=15\) control has \(F(15)=0\) and \(C_0(15)=1\).
For the literal coefficient, inserting the constant full sum gives only

\[
\begin{aligned}
 b_{L,X}(N)=F(N)
 &-\sum_{\substack{d\mid M\\d\notin\mathscr D_N}}\chi _4(d)\\
 &+\sum_{d\in\mathscr D_N}\chi _4(d)\{A_N(d)-1\}.
\end{aligned}
\tag{163.P28}
\]

Completing with the nonconstant literal profile instead destroys the
Euler product in (163.P26).  Thus one pays all omitted scales and
profile differences, or an uncontrolled full weighted divisor sum.
Complementation reorients this error and self-returns on a second
application.  The conductor-authorized M1 analogue confirms the same
full-minus-complement logic, but no M1 estimate is imported here.

When \(F(N)\ne0\), every odd prime divisor is \(1\pmod4\), and every
physical character is \(+1\).  The exchange graph has no negative
vertex.  This sector cannot be discarded by merely calling
sum-of-two-squares products logarithmically sparse: even a hypothetical
count \(L^2/(\log L)^C=L^{2-o(1)}\) misses the target by
\(L^{1/2-o(1)}\).  An exact weighted target count or another signed
estimate is required.

For a general internal exchange \(d'=rd\), all literal profile
arguments scale:

\[
\begin{aligned}
 A_N(rd)-A_N(d)
 ={}&\mathbf1_{\mathscr D_N}(rd)\eta_L(rd)
 \Phi\!\left(\frac{rd}{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,rd}{2\sqrt N}\right)\\
 &-\mathbf1_{\mathscr D_N}(d)\eta_L(d)
 \Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\end{aligned}
\tag{163.P29}
\]

The close-prime sector works because it imposes
\(|\log r|\ll L^{-1/2}\) canonically and proves the complete collar
count.  An arbitrary admissible ratio can be \(5/3\) or \(7/5\), giving
only \(O(1)\) smooth variation, while a hard crossing gives a full
one-sided term.  Existence of some close exchange per divisor, without
a single injective canonical pairing and the collar ledger, is
insufficient.

Every same-\(N\) exchange preserves
\[
 \mu^2(N)(L^2/N)^{3/4}e(J\sqrt N).
\]
Thus the arbitrary-real centre factors out of all within-fibre
identities.  Cancelling residuals across distinct \(N\) is a new
fixed-centre additive-twist theorem.  There is no exact cross-\(N\)
phase identity uniform in real \(J\): equality of
\(e(J\sqrt N)\) and \(e(J\sqrt{N'})\) for every real \(J\) forces
\(N=N'\).

Finally the accepted positive incidence capacity is

\[
 \sum_{N\asymp L^2}\sum_{d\in\mathscr D_N}|A_N(d)|
 \ll L^{2+o(1)}.
\tag{163.P30}
\]

Equations (163.P11)--(163.P13) reproduce it exactly for one-prime
toggles.  Arbitrary matching plus bounded profiles gives only the same
order in (163.S13).  The complete target needs the missing
\(L^{1/2-o(1)}\) saving; (163.R2) obtains it only by imposing the
canonical \(L^{-1/2}\)-close prime exchange.

## 4. First doubtful or unproved step

For the strict sector, no step remains doubtful once the accepted
scale-normalized smoothness (163.S6) is cited: fixed-point-freeness,
multiplicity, profile variation and boundary lattice count are all
proved above.  The sector makes no density claim.  This weakens its
effect on the open parent, but not the validity of the allowed
strict-sector exit: no density or target-safe complement is used in
(163.P5)--(163.P9).

For the unrestricted proposal, the first invalid affirmative step is to
replace “a sign-reversing partner exists” by “the paired literal
contributions cancel.”  A continuation must construct one globally
injective matching/transport and prove (163.S13), including every shell,
cone, profile and endpoint crossing.  One-prime averaging fails by the
exact self-return (163.P12)--(163.P13); the \(N=15015\) fibre defeats
partner-existence without Hall; and the balanced \(N=23205\) cycle
leaves the full profile-gradient sum.

The first open input is therefore a target bound for the complement of
the close-prime sector, or a genuinely signed fixed-centre theorem for
the residual \(N\)-sum before a positive norm.  No eligible-pair density,
general matching-gradient bound, or cross-\(N\) theorem of that strength
is present in the permitted context.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| literal_squarefree_product_grouping | Green: multiplicity-one grouping, exact cone, normalization and \(W\)-argument are (163.P1)--(163.P2). |
| odd_divisor_and_even_N_branch | Green: \(d_1\) stays odd; \(2\mid d_2\) is preserved by every odd-prime exchange. |
| full_divisor_vs_truncated_window | Obstruction: (163.P27)--(163.P28) retain all omitted scales and profile differences; \(N=15\) has full sum zero and truncated constant sum \(1\). |
| single_prime_toggle_domain | No-go: physical supports are disjoint and (163.P11) is full leakage; averaging all \(3\pmod4\) primes is the exact self-return (163.P12)--(163.P13). |
| close-prime canonical sector | Proved: (163.P3)--(163.P9) give a fixed-point-free, multiplicity-one involution, \(O(L^{-1/2})\) interior differences and \(O(L^{3/2}+L)\) complete boundary leakage. |
| two_prime_exchange_matching | Classified by (163.S7)--(163.S10).  Opposite residues and ratio in \([1/2,2]\) are necessary; \(N=1365\) is a valid two-cycle and \(N=15015\) exposes partner collisions. |
| multi-prime exchanges and matching cycles | The unrestricted graph is complete bipartite; restricted graphs require Hall.  \(N=23205\) has an exact four-cycle and perfect matchings, but only profile-gradient identities. |
| complementary_divisor_orientation | Green after parity repair: odd \(N\) uses (163.P23); even \(N=2M\) has even swap \(N/d\) and odd complement \(M/d\in[\sqrt N/4,\sqrt N/2]\), as in (163.P25). |
| character_sign_and_parity | Green: the sign ratio is \(\chi _4(AB)\); \(2\) cannot enter a physical exchange; \(N=210\) separates the even factor swap from the odd complement. |
| profile_window_and_endpoint_leakage | Green for the strict sector by accepted smoothness plus (163.P8)--(163.P9).  Open for arbitrary ratios; (163.P29) retains all literal arguments and crossings. |
| representable_sector_density_power | No promotion: all characters are \(+1\) when the full coefficient is nonzero.  Logarithmic sparsity is not a polynomial saving, and no exact weighted target count is proved. |
| arbitrary_real_centre_phase | Same-\(N\) swaps preserve the phase.  Residual cross-\(N\) cancellation remains the fixed-centre problem. |
| missing_L_half_power | Recovered only on the close-prime sector via \(L^{-1/2}\) profile variation and collar thickness.  Every unrestricted positive ledger remains \(L^{2+o(1)}\). |
| physical_coefficient_vs_diagnostic | Green distinction: (163.R2) is literal.  The small integer fibres use constant profiles only to falsify algebraic overclaims and prove no physical lower mass. |
| remaining_few_point_and_downstream_scope | No transfer: the complementary \(t=1\) atoms, \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels, hard TOP, BAL, UNBAL, M9--M2, M9, bridge and all exponent claims remain open. |

All tests are analytical and exact.  No numerical experiment, symbolic
experiment or web theorem is used.

## 6. Dependencies and exact artifacts used

This report uses only:

1. protocol.md;
2. state/proof_obligations.yml at graph SHA-256
   700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358,
   including the accepted H4-Phi-regularity and
   M9-M2-top-endpoint-actual-symbol-variation profile regularity;
3. state/active_campaign.yml;
4. strategy/round163_m2_hard_top_t1_near_square_divisor_involution_strategy.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/barrier_packet.md;
6. rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_divisor_involution_seed.md;
7. the conductor-authorized
   rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md,
   audited item-by-item at C1--C16 rather than treated as accepted;
8. proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
9. rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/synthesis.md;
10. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md;
11. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md;
12. the conductor-authorized analogue
    rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md,
    used only to audit full-minus-complement and two-adic self-return
    logic, not as an M2 estimate.

No sibling Round-163 report, excluded context, external source or
unlisted computational artifact is used.

## 7. Recommended state effect

Recommend promote after seam review under the sole round label
strict_t1_prime_toggle_sector.

Create a scoped target-safe sector recording the canonical selection
(163.R1), exact involution (163.P3)--(163.P5), accepted-profile
difference (163.P7), complete collar count (163.P8)--(163.P9), and bound
(163.R2).  The statement must explicitly say that it proves neither
eligible-pair density nor coverage of any prescribed polynomial block.

Also retain as route evidence, without a second round label:

* the one-prime full-boundary/all-primes averaging self-return
  (163.P10)--(163.P13);
* the complete exchange and matching classification
  (163.S7)--(163.S12), including Hall, even cycles, unmatched terms and
  profile gradients;
* the parity-correct odd/even complement identities
  (163.P23), (163.P25);
* the full-divisor completion and restored-capacity obstruction
  (163.P26)--(163.P30).

Reject the full \(t=1\) target, a density claim for close opposite-prime
pairs, a universal perfect exchange matching, cancellation from matching
cycles, a gain from averaging one-prime toggles, even-\(N\) complement
symmetry, full-divisor vanishing of the truncation, polynomial saving
from logarithmic representable-sector sparsity, and physical lower
bounds from constant-profile controls.

Keep the complementary \(t=1\) scalar open with next action (163.S13) or
an equivalent actual-coefficient fixed-centre theorem.  Do not change
the remaining few-point channels, full hard TOP, either smooth M2
packet, M9--M2, M9, the bridge, the quarter theorem, or any global
exponent.

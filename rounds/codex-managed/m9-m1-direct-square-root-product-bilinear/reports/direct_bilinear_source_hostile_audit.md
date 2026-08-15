## 1. Result

**No-go at the requested exponent, with a narrower direct bound.** On the
fixed smooth interior sector specified in the packet, put $J=X^{1/2}$. A
lawful two-dimensional Poisson calculation gives

\[
 \boxed{\displaystyle
 \mathcal T_Q\ll_{\varepsilon,\beta,C}
 X^\varepsilon Q^{3/2}J^{-1/2}\left(1+\frac{J}{Q}\right).}
 \tag{H69.1}
\]

At $Q=X^{1/5}$, the second term dominates and

\[
 \mathcal T_Q\ll X^{7/20+\varepsilon}
   =Q^{7/4}X^\varepsilon.
 \tag{H69.2}
\]

This improves the trivial $Q^2=X^{2/5}$, but misses the requested
$Q^{3/2}=X^{3/10}$ by $X^{1/20}=Q^{1/4}$. The Poisson image is exactly,
up to fixed Schwartz weights and the inherited one-sided ratio sector, the
fixed-centre central/truncated near-product discrepancy with product-window
length

\[
 T=\frac{J}{Q}=X^{3/10}.
\]

Its unsigned capacity is $1+T$. Closing (69.5) by this route requires
replacing that capacity by $J^{1/2}=X^{1/4}$, saving $X^{1/20}$. None of
the audited primary-source theorems supplies this fixed-centre signed
saving. No resonance of the actual fixed symbol exceeding $Q^{3/2}$ was
found; the strongest exact character/phase resonance located has total
capacity $O(Q^{1+\varepsilon})$.

## 2. Exact statement and hypotheses

The claim proved here is restricted as follows.

* $\beta\in C_c^\infty((0,\infty))$ and
  $C(y)=y^{3/4}\Xi(2\sqrt y)\in C_c^\infty((0,\infty))$ are fixed. Their
  supports and all seminorms are independent of $X,Q$.
* The support lies a fixed positive distance inside the one-sided cone
  $q>4k>0$. Thus $k\asymp Q$ and $q\asymp Q$ with fixed, possibly
  different, comparison constants. No hard cone edge or full cone is
  included.
* The $q$-sum remains over odd integers and retains the actual primitive
  odd character $\chi_4(q)$. The convention is $e(t)=e^{2\pi i t}$ and
  $\widehat f(\xi)=\int_{\mathbb R}f(y)e(-\xi y)\,dy$.

Under these hypotheses, (H69.1) holds for

\[
 \mathcal T_Q=\sum_k\sum_q
 \chi_4(q)\beta(k/Q)C(k/q)e(J\sqrt{kq}).
 \tag{H69.3}
\]

After character Poisson in $q$ and ordinary Poisson in $k$, all
non-negligible dual indices satisfy $m,n>0$, $m,n\asymp J$, and a fixed
one-sided condition on $m/n$. If $L\geq1$, the angular stationary
expansion has the form

\[
 I_{m,n}=Q^{3/2}(mn)^{-1/4}
 \sum_{\ell=0}^{L-1}(Q\sqrt{mn})^{-\ell}
 \mathcal K_\ell\!\left(\frac{m}{n},Q(J-\sqrt{mn})\right)+R_{L;m,n},
 \tag{H69.4}
\]

where every $\mathcal K_\ell(\rho,z)$ is uniformly Schwartz in $z$ on
the fixed ratio support, and

\[
 \sum_{m,n\asymp J}|R_{L;m,n}|
 \ll_L Q^{3/2-L}J^{3/2-L}.
 \tag{H69.5}
\]

At the benchmark relation $J=Q^{5/2}$, a sufficiently deep finite
expansion makes (H69.5) $O_A(Q^{-A})$. More importantly, the first
correction in (H69.4) has the same radial Schwartz localization as the
leading term. Consequently, after auditing the remainder with $L=2$, the
single displayed leading term is already aggregate-safe; Section 4 gives
the corrected ledger.

Grouping the original sum by $r=kq$ gives the exact coefficient

\[
 A_Q(r)=\sum_{\substack{kq=r\\q\ \mathrm{odd}}}
 \chi_4(q)\beta(k/Q)C(k/q),\qquad
 \mathcal T_Q=\sum_r A_Q(r)e(J\sqrt r).
 \tag{H69.6}
\]

This is a moving central/truncated divisor coefficient. It is neither an
arbitrary sequence nor the complete convolution
$(1*\chi_4)(r)=r_2(r)/4$.

## 3. Proof or derivation

**Normalization.** The packet has $b_k=Q^{-1}\beta(k/Q)$ and
$S_k=\mathfrak u(J/k)^{1/2}P_k+E_k$. Since $k\asymp Q$, absorbing the
fixed factor $(Q/k)^{1/2}$ into $\beta$ gives

\[
 \sum_k b_kS_k\big|_{\mathrm{main}}
 =\mathfrak u\,\frac{1}{Q}\sqrt{\frac{J}{Q}}\,\mathcal T_Q
 =\mathfrak u\,\frac{\sqrt J}{Q^{3/2}}\,\mathcal T_Q.
 \tag{H69.7}
\]

Thus $Q^{3/2}$, not $Q$ or $Q^2$, is the exact direct target.

**Two-dimensional Poisson and its constants.** Periodicity and ordinary
Poisson give

\[
 \sum_{q\in\mathbb Z}\chi_4(q)f(q)
 =\frac{i}{2}\sum_{n\in\mathbb Z}\chi_4(n)\widehat f(n/4).
 \tag{H69.8}
\]

Consequently,

\[
 \mathcal T_Q=\frac{i}{2}\sum_{m,n\in\mathbb Z}\chi_4(n)I_{m,n},
 \quad
 I_{m,n}=\iint a(x,y)e\!\left(J\sqrt{xy}-mx-\frac{ny}{4}\right)dx\,dy,
 \tag{H69.9}
\]

with $a(x,y)=\beta(x/Q)C(x/y)$. Set

\[
 x=\frac{Qu}{v},\qquad y=Quv,\qquad
 dx\,dy=\frac{2Q^2u}{v}\,du\,dv.
\]

The phase becomes

\[
 Qu\left(J-\frac{m}{v}-\frac{nv}{4}\right).
 \tag{H69.10}
\]

The angular saddle in the relevant positive sector is

\[
 v_0=2\sqrt{m/n},\qquad
 J-\frac{m}{v_0}-\frac{nv_0}{4}=J-\sqrt{mn},
 \tag{H69.11}
\]

and

\[
 \left.\frac{d^2}{dv^2}
 \left(J-\frac{m}{v}-\frac{nv}{4}\right)\right|_{v=v_0}
 =-\frac{n^{3/2}}{4m^{1/2}}.
\]

Before the factor $i/2$ in (H69.9), the leading stationary term is

\[
 \begin{aligned}
 I_{m,n}^{(0)}={}&2e(-1/8)Q^{3/2}(mn)^{-1/4}\\
 &\times\int_0^\infty u^{1/2}
 a(Qu/v_0,Quv_0)e\!\left(Qu(J-\sqrt{mn})\right)du.
 \end{aligned}
 \tag{H69.12}
\]

This verifies the $n/4$ dual frequency, the $i/2$ character-Poisson
prefactor, the saddle phase $Qu(J-\sqrt{mn})$, and the scale
$Q^{3/2}(mn)^{-1/4}\asymp Q^{3/2}J^{-1/2}$. Repeated stationary phase
gives (H69.4); fixed smooth support makes every radial kernel Schwartz.

Since $m,n\asymp J$,

\[
 Q|J-\sqrt{mn}|\asymp \frac{|mn-X|}{T},
 \qquad T=\frac{J}{Q}.
 \tag{H69.13}
\]

For $A>2$, grouping by $r=mn$ and using
$d(r)\ll_\varepsilon r^\varepsilon$ yields

\[
 \sum_{m,n\asymp J}
 \left(1+Q|J-\sqrt{mn}|\right)^{-A}
 \ll_\varepsilon X^\varepsilon(1+T).
 \tag{H69.14}
\]

Equations (H69.4), (H69.5), and (H69.14) prove (H69.1). In particular,
this reproduces the accepted inverse-transform plus $k$-Poisson return
bound

\[
 Q^{3/2}J^{-1/2}\left(1+\frac{J}{Q}\right).
 \tag{H69.15}
\]

Grouping the leading term by $r=mn$ produces

\[
 \sum_r K\!\left(\frac{r-X}{T}\right)
 \sum_{mn=r}\chi_4(n)W(m/n),
 \tag{H69.16}
\]

with fixed smooth $W$ on a one-sided central ratio sector and fixed
Schwartz $K$, or a finite fixed family of such kernels. Thus the
two-dimensional Poisson route exactly returns the fixed-centre near-product
discrepancy rather than bypassing it.

## 4. First doubtful or unproved step

The first genuinely unproved step is the signed fixed-centre estimate

\[
 \boxed{\displaystyle
 \sum_{m,n\asymp J}\chi_4(n)W(m/n)
 K\!\left(\frac{mn-X}{T}\right)
 \ll_\varepsilon J^{1/2}X^\varepsilon,
 \qquad T=\frac{J}{Q}.}
 \tag{H69.17}
\]

At $Q=X^{1/5}$, the left side has lawful absolute capacity
$T=X^{3/10}$, whereas (H69.17) asks for $J^{1/2}=X^{1/4}$. This is
exactly the missing $X^{1/20}=Q^{1/4}$ fixed-centre gain. It is not a
consequence of an unsigned root-spacing count, a centre-averaged short
interval theorem, or a Voronoi identity.

The previous all-pairs estimate for the first omitted stationary term was
an overcount: it took an absolute value before the compact $u$-integral
and thereby discarded the Schwartz factor in
$z=Q(J-\sqrt{mn})$. By (H69.4) and (H69.14), the aggregate first
correction is

\[
 \ll_\varepsilon
 Q^{3/2}J^{-1/2}(QJ)^{-1}(1+T)X^\varepsilon.
 \tag{H69.18}
\]

At $T=J/Q$, this is $(QJ)^{-1/2}X^\varepsilon$. Expanding through that
correction and bounding the $L=2$ terminal remainder by (H69.5) contributes
another $O(Q^{-1/2}J^{-1/2})$. Hence the error after the single leading
term (H69.12) is aggregate-safe on the fixed smooth interior. A deeper
finite expansion remains available for arbitrary power decay, but it is
not needed to obtain (H69.1). This correction removes the false
stationary-ledger obstruction; it does not prove (H69.17). No implication
to cone edges, a radial interval, M9-M1, M9, or the final exponent is
asserted.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Direct prefactor | Pass: (H69.7) is exactly $\sqrt J/Q^{3/2}$. |
| Odd lattice and character | Pass: $\chi_4$ is retained; (H69.8) has dual frequency $n/4$ and prefactor $i/2$. |
| One-sided cone | Pass: $q>4k$ becomes $v>2$, hence at the saddle a fixed one-sided condition $m/n>1$; it is never replaced by a full symmetric cone. |
| Fixed versus moving symbols | Pass: Mellin inversion of fixed $C$ has bounded Schwartz $L^1$-mass. A phase-conjugating symbol depending on $X$ would give $Q^2$, but is outside the hypotheses. |
| Stationary aliases | Pass: $v_0=2\sqrt{m/n}$, phase $Qu(J-\sqrt{mn})$, scale $Q^{3/2}(mn)^{-1/4}$, and localization $|mn-X|\lesssim J/Q$. |
| Stationary remainder | Pass: the first correction retains radial Schwartz localization, giving (H69.18); the $L=2$ remainder is also aggregate-small. |
| Product coefficient | Pass: (H69.6) is central/truncated and is not silently completed to $r_2/4$. |
| Inverse-transform return | Pass: the exact lawful bound is (H69.15), identical in size to (H69.1). |
| Fixed-centre capacity | Fail as a closure: (H69.14) gives $1+T$, while the target requires (H69.17). |

There is an actual-symbol character/phase resonance, but it is too small
to disprove the target. Take $J=N+1/4$ and write a square-product pair as

\[
 k=db^2,\qquad q=da^2,
\]

with $d$ squarefree, $d,a,b$ odd, and $a/b$ in the fixed one-sided ratio
support. Since $e(t/4)=i\chi_4(t)$ for odd $t$,

\[
 \chi_4(q)e(J\sqrt{kq})=i\chi_4(ab),
 \tag{H69.19}
\]

which is constant in $d$ on each rational ray. Nevertheless,

\[
 \#\{(k,q):k,q\asymp Q,\ kq\ \text{is a square}\}
 \ll Q\sum_{b\ll\sqrt Q}\sum_{a\asymp b}\frac{1}{a^2}
 \ll Q\log Q.
 \tag{H69.20}
\]

Thus even complete coherence on all square-product rays is
$O(Q^{1+\varepsilon})<Q^{3/2}$. Fourth-power fibres are a subset and are
smaller. Exact rational angular saddles have the same nondegenerate second
derivative and give no extra multiplicity. On the dual side, the exact
centre $mn=X$ contains at most $d(X)\ll X^\varepsilon$ pairs. Hence no
actual fixed-symbol perfect-power or rational-saddle obstruction above the
target was found. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The only repository artifacts used were protocol.md,
state/proof_obligations.yml, state/active_campaign.yml, the Round-69
derivation packet and assigned brief, and the permitted Round-68
hostile/source report and conductor adjudication. No other Round-69 report
was read.

The primary-source audit was as follows.

* **Bilinear monomial theorem.** Lemma 1 on p. 5 of
  [Kumchev, *A Diophantine Inequality Involving Prime Powers*, Acta Arith.
  89 (1999)](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8942.pdf) states,
  for $|a(m)|,|b(n)|\leq1$ and
  $\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0$, the bound

  \[
  \begin{aligned}
  (FMN)^{-\eta}|S|\ll{}&
  (F^4M^{31}N^{34})^{1/42}+(F^6M^{53}N^{51})^{1/66}
  +(F^6M^{46}N^{41})^{1/56}\\
  &+(F^2M^{38}N^{29})^{1/40}+(FM^9N^6)^{1/10}
  +(F^2M^7N^6)^{1/10}\\
  &+(FM^6N^6)^{1/8}+M^{1/2}N+MN^{1/2}+F^{-1/4}MN.
  \end{aligned}
  \tag{H69.21}
  \]

  Kumchev explicitly attributes this to Theorem 9 of Sargos--Wu; the
  published source is
  [Sargos--Wu, Acta Math. Hungar. 87 (2000), 333--354](https://doi.org/10.1023/A:1006777803163),
  not a Fouvry--Iwaniec theorem. Here Mellin inversion lawfully separates
  $C(k/q)$, $\chi_4$ is a bounded $q$-coefficient, and
  $M=N=Q$, $F=JQ=X^{7/10}$, $\alpha=\beta=1/2$. The ten displayed
  exponents of the project parameter $X$ are

  \[
  \frac{79}{210},\ \frac{25}{66},\ \frac{27}{70},\
  \frac{37}{100},\ \frac{37}{100},\ \boxed{\frac{2}{5}},\
  \frac{31}{80},\ \frac{3}{10},\ \frac{3}{10},\ \frac{9}{40}.
  \tag{H69.22}
  \]

  Because (H69.21) is a sum of positive terms and contains the exactly
  trivial $X^{2/5}$ term, it gives no nontrivial estimate here. Omitting
  that term would be unlawful.

* **Fouvry--Iwaniec architecture/double large sieve.** Theorem 1 of
  [Robert--Sargos, *Three-dimensional exponential sums with monomials*,
  J. reine angew. Math. 591 (2006)](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
  is the paper's completed “expected Fouvry--Iwaniec” bound. It allows
  arbitrary separated bounded coefficients and gives
  $(HNM)^{1+\varepsilon}\{(F/(HNM^2))^{1/4}+(HN)^{-1/4}
  +M^{-1/2}+F^{-1/2}\}$. Taking the lawful singleton $H=1$,
  $M=N=Q$, and $F=JQ$ produces the four $X$-exponents

  \[
  \frac{17}{40},\quad \frac{7}{20},\quad
  \frac{3}{10},\quad \frac{1}{20}.
  \tag{H69.23}
  \]

  The first is worse than the trivial $2/5$; hence the theorem as a whole
  is nonclosing. This is the exact applicable Fouvry--Iwaniec-method
  mapping; the methodological analogy alone cannot delete its first term.

* **Current one-variable exponent pair.** Definition 11 and Theorem 20 of
  [Tao--Trudgian--Yang, *New exponent pairs, zero density estimates, and
  zero additive energy estimates*](https://arxiv.org/abs/2501.16779) apply
  after splitting $q\bmod4$ and partial summation of the fixed smooth
  amplitude. A row has length $Q$ and phase parameter $JQ$, so an exponent
  pair $(\kappa,\lambda)$ gives
  $Q^{1+\lambda}J^\kappa X^\varepsilon$. Of their four new pairs, the
  best for this audited objective is
  $(10769/351096,609317/702192)$, giving

  \[
  X^{1/5+\kappa/2+\lambda/5+\varepsilon}
   =X^{227559/585160+\varepsilon}
   =X^{0.388883\ldots+\varepsilon}.
  \tag{H69.24}
  \]

  This is lawful but weaker than (H69.2) and far above the target.

* **Short divisor intervals and Voronoi/Hankel.** Theorem 1 of
  [Ivić--Zhai, *On the Dirichlet divisor problem in short intervals*](https://arxiv.org/abs/1209.0872)
  concerns the complete $d(n)$-coefficient and proves pointwise bounds
  $x^{1/4+\varepsilon}U^{1/4}$ and
  $x^{2/9+\varepsilon}U^{1/3}$. At $U=T=X^{3/10}$, these are
  $X^{13/40+\varepsilon}$ and $X^{29/90+\varepsilon}$, both worse than
  the elementary $UX^\varepsilon$; its stronger results average the
  centre. It therefore neither matches the coefficient in (H69.16) nor
  improves its fixed-centre $T$-capacity. The B-process and Voronoi
  transformations in
  [Jutila, *Lectures on a Method in the Theory of Exponential Sums*](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf)
  are transformation formulae, not the missing estimate; here the direct
  transform demonstrably returns (H69.16). General Voronoi formulae such
  as [Kiral--Zhou](https://arxiv.org/abs/1508.01985) concern complete
  $L$-function coefficient sequences and likewise do not provide a
  fixed-centre bound for the additional one-sided central divisor cutoff.

Thus every cited statement either fails numerically, has the wrong
coefficient/averaging hypothesis, or is a transform without a new capacity
estimate. Analogy was not counted as applicability.

## 7. Recommended state effect

**Retain the direct target as open; do not promote (69.5).** Record
(H69.1)--(H69.16) as a fixed-smooth-interior no-go/reduction: direct
two-dimensional Poisson gives the genuine improvement
$X^{7/20+\varepsilon}$, but exactly returns the length-$T$ fixed-centre
near-product discrepancy and the accepted
$Q^{3/2}J^{-1/2}(1+J/Q)$ bound. Record the corrected aggregate-safe
stationary ledger (H69.18), the exact nonclosing source mappings
(H69.22)--(H69.24), and the harmless actual-symbol resonance
(H69.19)--(H69.20).

The smallest admissible next analytic objective is (H69.17), or a genuine
actual-symbol counterexample. No state effect beyond retaining/revising
the direct candidate is recommended, and no full-cone, radial-interval,
M9-M1, M9, or exponent claim is licensed.

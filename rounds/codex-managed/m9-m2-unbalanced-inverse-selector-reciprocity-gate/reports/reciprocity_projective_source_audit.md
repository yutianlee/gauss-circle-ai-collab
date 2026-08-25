# Round 160 reciprocity projective source audit

Campaign: m9-m2-unbalanced-inverse-selector-reciprocity-gate

Task: reciprocity_projective_source_audit

Role: primary-source and hostile power auditor

Starting graph SHA-256:
4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d

Generated at: 2026-08-25T18:40:28+08:00

## 1. Result

**Scoped no-go, under the exit label
`inverse_selector_projective_capacity_no_go`.**  Additive reciprocity is
exact, including for even (j), but it does not turn the literal centered
matrix into an input of any audited scalar trace formula, spectral large
sieve, or Kloosterman-fraction theorem at an owner-saving cost.

The new exact obstruction is the following.  For fixed (j), let

\[
 F_j(a,h)=e(h\bar a_j/j),\qquad
 a\in(\mathbb Z/j\mathbb Z)^*,\quad 1\leq h\leq j-1.
\]

Then

\[
 F_jF_j^*=jI_{\varphi(j)}-\mathbf 1\mathbf 1^*,                 \tag{1.1}
\]

so

\[
 \|F_j\|_{S_2}=\{\varphi(j)(j-1)\}^{1/2},\qquad
 \|F_j\|_{S_1}=(\varphi(j)-1)\sqrt j+\sqrt{j-\varphi(j)}.     \tag{1.2}
\]

Consequently every canonical scalar common-test decomposition across the
(n\bmod j) classes and the nonzero (h\bmod j) frequencies pays the
sharp projective-versus-Hilbert inflation

\[
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
   =\sqrt{\varphi(j)}\,(1+o(1))=j^{1/2-o(1)}.                 \tag{1.3}
\]

This is already present in the primitive (g=1) stratum, where
(j\asymp K).  Writing (a=\delta-\ell), the resulting
(K^{1/2-o(1)}) scalarization price is pointwise at least the entire
missing boundary power:

\[
 \frac{1-\delta-a}{2}>a-\frac14\quad(1/4<a\leq1/3),\qquad
 \frac{1-\delta-a}{2}>\frac{1-2a}{4}\quad(1/3\leq a<1/2).    \tag{1.4}
\]

At (a=1/3) it is strictly larger than (1/12).  The inequalities have
no extra uniform margin as the open boundary (delta=1/2) is approached.

The exact source audit reinforces (1.1)--(1.4).

* Keeping the inverse-residue factor as an arithmetic modulus weight in
  Blomer--Milićević costs its full normalized (q)-Mellin (L^1)-norm.
  For an odd prime (p=j) and (p\nmid h), that norm is
  (\asymp p), not (O(1)) or (O(p^{1/2})).
* Expanding it additively gives coefficients
  (S(h,-t;j)/j).  For prime (j), every (o(j))-sized low-(t) band
  carries (o(1)) of the row (L^2)-mass.  The remaining modes have
  normalized modulus frequency (t(R/g)/j\asymp R/g), so the apparent
  arithmetic saving reappears as Sobolev/Mellin/Bessel bandwidth.
* Encoding the residue weight spectrally does not stay at levels (4) and
   (8).  For (j=p) prime it introduces, among others, levels
   (4p,8p,4p^2,8p^2) and their complete holomorphic, Maaß,
   exceptional, Eisenstein, newform, and oldclass ledgers.  The principal
   \(p\)-character is odd and also produces levels \(4,8,4p,8p\);
   both parities occur across the nonprincipal conductor-\(4p\) family,
   not at the pure levels \(4\) and \(8\).
* Bettin--Chandee and Wright accept the bare phase
  (e(h\bar n_j/j)), but not the simultaneous joint coefficient
  (S(N_0,h;n)) with its moving (n,j) support.  Even a deliberately
  favourable rank-one, Weil-normalized surrogate gives printed bounds
  larger than the already accepted divisor capacity by fixed powers.
* The sourced Linnik range covers only
  (h\ll K/(Lg^2)), a proportion at most (1/(Dg)) of the literal
  (1\leq h<n) range.  The long complement cannot be deleted: complete
  (h)-summation reconstructs the original reciprocal row exactly.

Thus none of the audited **canonical scalar** direct, residue-class,
common-test, fixed-level trace, or common-sequence large-sieve routes proves
the target or a strict owner-complete range.  This is not a signed lower
bound and does not exclude a bespoke vector-valued theorem that treats the
full weighted (n,j,h) coefficient together with the Kloosterman spectrum
before scalarization.

## 2. Exact statement and hypotheses

Put

\[
 X=N_0+\xi,\quad D=X^\delta,\quad L=X^\ell,\quad
 R=X/D,\quad K=XL/D^2,\quad \Delta=R/K=D/L,
\]

under the frozen strict region

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\]

For fixed (g), write

\[
 C_g=R/g,\qquad J_g=K/g,
\]

so (n\asymp C_g), (j\asymp J_g), and (C_g/J_g=\Delta>1).
The exact centered scalar after reciprocity is

\[
\begin{split}
 \mathscr R^\circ_{D,L}(X)
  ={}&\sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
  \chi_4(g)W\!\left(\frac{X}{gnD}\right)
  \sum_{1\leq h<n}\frac1n
  \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
  \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n) \\
 &\hspace{34mm}\times
 e\!\left(\frac{h\bar n_j}{j}-\frac{h}{jn}\right)
 S^{\chi_4}_{\infty0}(4N_0,h;2n).                           \tag{2.1}
\end{split}
\]

Equivalently, using the accepted internal identity

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)=\chi_4(n)S(N_0,h;n),        \tag{2.2}
\]

the literal modulus sign is (\chi_4(g)\chi_4(n)).  No
coprimality between (N_0) and (n) is assumed.

The scoped capacity statement proved here has the following precise
meaning.

1. A **canonical scalar common-test decomposition** first isolates the
   finite residue-frequency kernel (F_j), or an equivalent additive or
   multiplicative Fourier expansion of it, and then applies a theorem whose
   input has one fixed Fourier index and one scalar smooth modulus test.
   Its optimal Hilbert projective price is the Schatten-one norm in (1.2).
2. If, for a fixed (j), the literal moving support contains a flat
   (n)-interval of length (\asymp C_g), every unit class modulo (j)
   occurs (\asymp C_g/j\asymp\Delta) times (with a factor (1/2) when
   the odd-(n) condition doubles the period).  Hence the full row set of
   (F_j) is genuinely present on that interior.  If the literal moving
   support does not supply such an interval, the full-class lower price is
   not asserted; instead the required common smooth extension and its
   endpoint Sobolev/Bessel norm are unproved.  No endpoint is silently
   discarded in either branch of this dichotomy.
3. The no-go concerns the canonical scalar routes and the exact printed
   theorems below.  It does not assert a lower bound for (2.1), a universal
   nonfactorization theorem for the fully weighted matrix, or a no-go for a
   new vector trace formula.

### Source theorem cards and literal maps

**Bettin--Chandee.**  Theorem 1 of arXiv:1502.00769v1 accepts independent
dyadic sequences in

\[
 \sum_{a,m,n}\alpha_m\beta_n\nu_a
 e(\vartheta a\bar m_n/n),\qquad(m,n)=1,                     \tag{2.3}
\]

with one absolute value outside the complete trilinear sum and the two
terms printed in its (1.2).  Remark 1 permits only the stated (C^1)
perturbation.  The post-reciprocity dictionary is

\[
 (a,m,n,\vartheta;A,M,N)_{\rm source}
 =(h,n_{\rm phys},j,1;C_g,C_g,J_g).                          \tag{2.4}
\]

The coprimality condition is exact.  The source does not accept
(S(N_0,h;n_{\rm phys})) as a joint ((a,m))-coefficient.

**Wright.**  Theorem 2.1 of arXiv:2604.25177v2 has the same independent
coefficient interface with phase
(e(\vartheta a\bar m/(nR_0))), assumes
(M\ll N^2), (R_0\ll M^A), and integral
(\vartheta\ne0).  The owner-complete primitive map has (R_0=1) and
the dictionary (2.4).  It is available only when

\[
 C_g\ll J_g^2;                                               \tag{2.5}
\]

at (g=1), this is the exponent condition
(\delta+2(\delta-\ell)\leq1).  Outside (2.5) the theorem is inapplicable;
inside it the same joint-Kloosterman coefficient mismatch remains.

**Blomer--Milićević.**  Theorem 1 and Corollary 2 of JEMS 17 (2015),
51--69, bound

\[
 \sum_{(c,q)=1}\frac{S(m,n;c)}{\sqrt c}
 f(c)f_\infty(c/C)                                          \tag{2.6}
\]

for fixed positive (m,n,q), one arithmetic weight
(f:(\mathbb Z/q\mathbb Z)^*\to\mathbb C), and one smooth compactly
supported scalar test, uniformly only in the Linnik range (mn\leq C^2).
Theorem 1 costs (C^{1/2+2\theta}\|\widehat f\|_1); Corollary 2 costs
(C^{1/2+2\theta}q^{1/2}) for one primitive residue class.  For fixed
(g,j,h), the exact map is

\[
 c=n_{\rm phys},\quad (m,n)_{\rm source}=(N_0,h),\quad
 q=q_j={\rm lcm}(4,j),                                      \tag{2.7}
\]

\[
 f_{j,h}(c)=\chi_4(c)e(h\bar c_j/j),\qquad
 f_{\infty,j,h}(c/C_g)
 =c^{-1/2}W\!\left(\frac{X}{gcD}\right)
 \frac{q_L(4Xj/(gc^2))}{gj}e(\xi j/c-h/(jc)),               \tag{2.8}
\]

with literal zero extension.  Formula (2.8) is a legal scalar test only
after every moving endpoint has been supplied with the required uniform
smooth extension.  Theorem 4 expands (2.6) over every character modulo
(q_j), every squarefree (d\mid q_j), and the complete (H+M+E)
spectrum at level (dq_1), where (q_1) is the primitive conductor.

**Deshouillers--Iwaniec and Assing--Blomer--Li.**  Deshouillers--Iwaniec,
Invent. Math. 70 (1982), Theorems 2 and 5, use one fixed cusp and the same
one coefficient sequence in each holomorphic, Maaß, Eisenstein, and
exceptional quadratic form.  They are not a large sieve for a family of
(h)-dependent arithmetic weights (f_{j,h}) and varying levels
(dq_1).  Assing--Blomer--Li, arXiv:2005.13915, Theorem 2.4, accepts

\[
 \sum_{(c,r)=1}\frac1c\sum_m\alpha_mF(m,c)
 S(m\bar r,\pm n;sc)                                       \tag{2.9}
\]

with one sequence (\alpha_m), fixed (n,r,s), a jointly smooth
(F), all printed derivative bounds with parameter (Z), and
((Mn/(s^2rC^2))^{1/2}\ll Z).  The closest map is

\[
 (m,c,n,r,s)_{\rm source}=(h,n_{\rm phys},N_0,1,1),\qquad
 M\asymp C\asymp C_g,                                      \tag{2.10}
\]

but the coefficient in (2.1) is not (\alpha_hF(h,c)), and the inverse
residue expansion forces the additional derivative price recorded below.
Moreover, (2.9) has no \(\chi_4(c)\) modulus twist.  Encoding that
factor inside a scalar test costs normalized frequency \(\asymp C_g\),
so it is not a free fixed-level insertion.

## 3. Proof or derivation

### 3.1 Reciprocity, centering, and exact self-return

Choose (u=\bar j_n) and (v=\bar n_j).  Since
(ju+nv\equiv1\pmod n) and modulo (j), coprimality gives

\[
 ju+nv\equiv1\pmod{jn}.
\]

Therefore

\[
 \frac{u}{n}+\frac{v}{j}\equiv\frac1{jn}\pmod1,
\]

which proves, with the exact sign,

\[
 e(-h\bar j_n/n)=e(h\bar n_j/j-h/(jn)).                     \tag{3.1}
\]

No parity assumption on (j) enters this proof.

Use the convention

\[
 S(N_0,h;n)=\sum_{x\bmod n}^{*}
 e((N_0x+h\bar x_n)/n).
\]

Then for every allowed (g,n,j), with arbitrary ((N_0,n)),

\[
\begin{split}
 &\sum_{h\bmod n}e(h\bar n_j/j-h/(jn))S(N_0,h;n)\\
 &\quad=\sum_{x\bmod n}^{*}e(N_0x/n)
 \sum_{h\bmod n}e(h(\bar x_n-\bar j_n)/n)
 =n e(N_0j/n).                                               \tag{3.2}
\end{split}
\]

The factor (1/n) in (2.1) cancels, and (e(\xi j/n)) restores
(e(Xj/n)).  Thus the complete (h)-sum is exactly the original
reciprocal row.  The (h=0) Ramanujan row is the already accepted
target-safe term and is removed once; (2.1) is complete minus precisely
that row.  In particular, for any cutoff (H<n), the hostile complement
satisfies the exact identity

\[
 \sum_{H<h<n}(\cdots)
 =n e(N_0j/n)-S(N_0,0;n)-\sum_{1\leq h\leq H}(\cdots).       \tag{3.3}
\]

No estimate for the short slice alone estimates the complement.

### 3.2 Residue classes and the exact projective price

For a fixed (j), inversion permutes the unit group.  Hence

\[
 (F_jF_j^*)(a,b)
 =\sum_{h=1}^{j-1}e(h(\bar a_j-\bar b_j)/j)
 =\begin{cases}j-1,&a=b,\\-1,&a\ne b.\end{cases}
\]

This is (1.1).  On the orthogonal complement of the constant vector its
eigenvalue is (j), with multiplicity (\varphi(j)-1); on the constant
vector it is (j-\varphi(j)).  Taking square roots proves (1.2).
The Schatten-one norm is the infimum of
(\sum_r\|u_r\|_2\|v_r\|_2) over every rank-one scalar decomposition,
so (1.2) is an optimal price, not merely the cost of one chosen expansion.
Multiplying rows by (\chi_4(a)) or unit phases, or adding zero rows for
nonunits, does not change the nonzero singular values.

The actual (h)-range contains (1\leq h\leq j-1), because
(j\asymp J_g<C_g\asymp n).  Coordinate compression is contractive in
(S_1), so adjoining the long-frequency columns cannot lower the
projective norm forced by this block.  Likewise, duplicating every residue
class (\asymp\Delta) times in the physical (n)-interval multiplies both
the (S_1) and (S_2) scales by the same square-root repetition factor;
it does not remove the ratio (1.3).

The literal class count is also explicit.  For an (n)-interval (I),

\[
 \#\{n\in I:n\equiv a\pmod j, n\ {\rm odd}\}
 =\begin{cases}|I|/j+O(1),&2\mid j,\ a\in(\mathbb Z/j\mathbb Z)^*,\\
 |I|/(2j)+O(1),&2\nmid j,
 \end{cases}                                                \tag{3.4}
\]

for every unit (a).  Thus an interior interval of length
(\asymp C_g) contains all (\varphi(j)) unit classes with
(\asymp\Delta) representatives.  Summing the (O(1)) entry/exit errors
over classes itself costs (O(\varphi(j))); it cannot be declared free.

### 3.3 Boundary-power comparison in the primitive stratum

At (g=1), (j\asymp K) and

\[
 K=X^{1+\ell-2\delta}=X^{1-\delta-a}.
\]

For (a\leq1/3),

\[
 \frac{1-\delta-a}{2}-\left(a-\frac14\right)
 =\frac{3/2-\delta-3a}{2}>0,                                \tag{3.5}
\]

because (\delta<1/2) and (a\leq1/3).  For (a\geq1/3),

\[
 \frac{1-\delta-a}{2}-\frac{1-2a}{4}
 =\frac{1-2\delta}{4}>0.                                    \tag{3.6}
\]

Equations (3.5)--(3.6) prove (1.4).  Since (g=1) carries
(\chi_4(g)=1), no outer-(g) cancellation can repay this cost.

### 3.4 Multiplicative and additive source expansions

Take (j=p) an odd prime and (1\leq h\leq p-1).  On
((\mathbb Z/p\mathbb Z)^*), put (f_h(a)=e(h\bar a_p/p)).  With the
normalized Mellin convention of Blomer--Milićević,

\[
 \widehat f_h(\chi)=\frac1{\sqrt{p-1}}
 \sum_{a\bmod p}^{*}\bar\chi(a)e(h\bar a_p/p)
 =\frac1{\sqrt{p-1}}\sum_{b\bmod p}^{*}\chi(b)e(hb/p).
\]

The principal term has magnitude (1/\sqrt{p-1}), and every one of the
(p-2) nonprincipal characters has magnitude
(\sqrt{p/(p-1)}).  Therefore

\[
 \|\widehat f_h\|_1
 =(p-2)\sqrt{\frac p{p-1}}+\frac1{\sqrt{p-1}}\asymp p.       \tag{3.7}
\]

Including (\chi_4) at period (4p) tensors (3.7) with the one
nonzero mod-(4) Mellin coefficient and changes it only by a fixed factor.
Thus Theorem 1, applied to (2.8), pays (\asymp j).  Expanding into
individual residue classes instead invokes Corollary 2 at price
(j^{1/2}) per class and costs (\asymp j^{3/2}) after the scalar
class triangle.  Grouping the classes before the theorem improves that to
(3.7), but does not make it (O(1)).

The exact additive expansion is

\[
 e(h\bar a_j/j)\mathbf1_{(a,j)=1}
 =\sum_{t\bmod j}\frac{S(h,-t;j)}j e(ta/j).                 \tag{3.8}
\]

For prime (p), Parseval and Weil give, for every (h\ne0\pmod p),

\[
 \sum_{t\bmod p}\left|\frac{S(h,-t;p)}p\right|^2
 =\frac{p-1}{p},                                            \tag{3.9}
\]

and for a set (T) of (B) nonzero frequencies, together with (t=0),

\[
 \sum_{t\in T\cup\{0\}}
 \left|\frac{S(h,-t;p)}p\right|^2
 \leq\frac{4B}{p}+\frac1{p^2}.                              \tag{3.10}
\]

Hence an (o(p))-sized low-frequency set contains (o(1)) of the row
mass.  Moving (e(tn/p)) into a smooth test on (n=C_gx) gives

\[
 \partial_x^\nu e(tC_gx/p)\ll_\nu
 (1+|t|C_g/p)^\nu.                                          \tag{3.11}
\]

The mass in (3.10) forces (|t|\asymp p), hence a Sobolev/Mellin
bandwidth (\asymp C_g).  In the Assing--Blomer--Li map (2.10), the
printed derivative hypothesis therefore requires (Z\gg C_g) on this
mass; even the zero-frequency comparison already requires

\[
 Z\gg\sqrt{C_gN_0/C_g^2}=\sqrt{Dg}.                          \tag{3.12}
\]

Thus additive Fourier transfer exchanges the arithmetic conductor for an
archimedean/Bessel conductor; it does not produce a low-Sobolev common
test.

There is an additional Assing--Blomer--Li character seam.  Theorem 2.4
has no \(\chi_4(c)\) modulus twist.  One legal comparison sets
\(r=2\), \(s=1\), and source \(m=2h\); then \((c,r)=1\) restricts to
odd \(c\) and Kloosterman symmetry gives
\(S(2h\overline2,N_0;c)=S(N_0,h;c)\).  But on odd moduli

\[
 \chi_4(c)=e((c-1)/4),
\tag{3.12a}
\]

so absorbing the character into the smooth test costs normalized
frequency \(\asymp C_g\), hence again \(Z\gg C_g\).  It is not a free
fixed-level factor.

### 3.5 Spectral levels forced by the residue weight

The fixed (q=4) identity used in Round 143 has levels (4) and (8)
only because its arithmetic weight is just (\chi_4).  For (j=p) an
odd prime, (2.8) has period (q=4p).  Its Mellin expansion contains

\[
 \chi=\chi_4\psi,\qquad \psi\pmod p.
\]

For principal (\psi), the primitive conductor is (q_1=4), and the
nonzero Möbius divisors (d\mid4p) give the levels

\[
 4,\ 8,\ 4p,\ 8p.                                           \tag{3.13}
\]

For every nonprincipal (\psi), the conductor is (q_1=4p), and the
same divisors give

\[
 4p,\ 8p,\ 4p^2,\ 8p^2.                                     \tag{3.14}
\]

The principal component in (3.13) is odd.  Across the nonprincipal
\(\psi\)-family in (3.14), both values of \(\psi(-1)\) occur for
\(p\ge5\), hence both source parities occur there.  At every compatible
level Blomer--Milićević Theorem 4 retains the complete (H+M+E) ledger,
with all compatible holomorphic weights, real and exceptional Maaß
parameters, every singular-cusp Eisenstein integral, and the full new/old
basis.  Its Fourier arguments are

\[
 m_0=\frac{N_0}{(N_0,q^\infty)},\qquad
 n_0q_1^2=h(N_0,q^\infty)q_1^2,                              \tag{3.15}
\]

so arbitrary gcds with (N_0) also vary the sequence with (j).

For general even or odd (j), the exact statement is the same with
(q_j={\rm lcm}(4,j)): every character with nonzero Mellin coefficient,
its primitive conductor (q_1\mid q_j), every squarefree
(d\mid q_j), level (dq_1), and parity (\chi(-1)) must be kept.
Thus one has an exact dichotomy.  Keeping only levels (4/8) leaves the
rough (n\bmod j) coefficient outside the scalar common-test theorem;
encoding that coefficient legally creates the growing-level ledger above.

### 3.6 Direct, vector, and long-frequency capacity ledgers

The direct Kloosterman-fraction map (2.4) fails first at the joint factor
(S(N_0,h;n_{\rm phys})).  Opening it introduces another inverse modulo
(n_{\rm phys}); summing the complete (h)-range then gives the exact
self-return (3.2), not an independent trilinear tensor.

There is also a useful favourable numerical screen.  Grant all moving
((n,j)) amplitudes projective mass (O(1)), grant the normalized matrix
(S(N_0,h;n)/\sqrt{C_g}) a rank-one decomposition of unit cost, and retain
only its unavoidable Weil scale (\sqrt{C_g}).  The product of the three
source (\ell^2)-norms together with the physical coefficient
((C_gK)^{-1}\sqrt{C_g}) is

\[
 \frac{\sqrt{C_gJ_g}}K.                                     \tag{3.16}
\]

Bettin--Chandee Theorem 1 then prints the two capacities

\[
 \frac{C_g^{29/20}J_g^{17/20}}K,\qquad
 \frac{C_g^{3/2}J_g^{7/8}}K.                                \tag{3.17}
\]

At (g=1), their ratios to the divisor capacity (\Delta=R/K) are

\[
 R^{9/20}K^{17/20}
   =X^{(26-43\delta+17\ell)/20}>X^{9/40},                   \tag{3.18}
\]

\[
 R^{1/2}K^{7/8}
   =X^{11/8-9\delta/4+7\ell/8}>X^{1/4}.                     \tag{3.19}
\]

Wright Theorem 2.1, when (2.5) holds, already contains the second quantity
in (3.17) from its first bracket term; outside (2.5) it is unavailable.
Thus even this deliberately easier product surrogate is not an improving
source specialization.  Equations (3.16)--(3.19) are a source-capacity
screen, not a claim that the literal Kloosterman matrix is rank one.

For scalar modulus summation, (2.6)--(2.8) have amplitude
(\asymp(K\sqrt{C_g})^{-1}), so Blomer--Milićević Theorem 1 gives, for
one fixed (j,h),

\[
 \ll K^{-1}C_g^{2\theta+\varepsilon}
 \|\widehat f_{j,h}\|_1.                                   \tag{3.20}
\]

On the prime block (3.7), this costs (j/K) before any (j)- or
(h)-aggregation.  The theorem is scalar and supplies no cancellation
among the (h)-dependent weights (f_{j,h}).

Its Linnik condition is

\[
 N_0h\leq C_g^2,\qquad
 h\ll H_{\rm Lin}(g)=\frac{C_g^2}{X}
 \asymp\frac{K}{Lg^2}.                                      \tag{3.21}
\]

Relative to one (j)-period and the full physical row,

\[
 \frac{H_{\rm Lin}(g)}{J_g}\asymp\frac1{Lg},\qquad
 \frac{H_{\rm Lin}(g)}{C_g}\asymp\frac1{Dg}.               \tag{3.22}
\]

For (Lg>1), the sourced range does not even contain the complete
(1\leq h<j) obstruction block.  When (L=g=1), it can contain that
first block but still omits the remaining (\asymp\Delta) periods.
Equation (3.3) proves only that this complement cannot be deleted or
controlled by formal Fourier reasoning; it does not give a quantitative
lower bound for the signed complement.

Finally, any coefficient-blind Hilbert/row large-sieve closure remains the
accepted positive capacity

\[
 R\sqrt\Delta\,X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon}.                         \tag{3.23}
\]

It exceeds the quarter target by more than (3/8) in exponent at every
strict point and exceeds either accepted envelope branch by more than
(1/4).  Reciprocity changes phases and residue coordinates but not this
Hilbert ledger.  Scalarizing the exact residue-frequency block then adds
the inflation (1.3); none of the printed common-sequence large sieves
absorbs it.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in (3.1), (3.2), or the finite matrix
identity (1.1), and the source theorem maps above are literal.  The first
unproved step of any positive continuation is a theorem for the **fully
weighted** matrix which, before a positive modulus norm, simultaneously
couples

\[
 \chi_4(n),\quad e(h\bar n_j/j),\quad e(-h/(jn)),\quad
 S(N_0,h;n),\quad q_L(4Xj/(gn^2)),
\]

with the moving (j)-support and all (1\leq h<n), and has projective or
vector cost smaller than the canonical (K^{1/2-o(1)}) inflation.  No
audited theorem states such an estimate.

This is also the exact scope limit of the no-go.  The Schatten computation
is a sharp obstruction to decomposing the isolated residue-frequency
kernel into scalar common tests.  It is not a proof that multiplication by
the literal Kloosterman matrix and all moving weights cannot create a new,
bespoke vector structure.  Proving such a structure, including its
long-frequency and endpoint norms and its complete growing-level spectral
ledger, is the first unresolved step.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_inverse_selector_reciprocity` | **Pass.** Equation (3.1) has the exact sign and representative-independent phase; it uses only ((j,n)=1) and includes even (j). |
| `centered_h_nonzero_once` | **Pass.** The report uses (1\leq h<n); the target-safe (h=0) Ramanujan row is subtracted exactly once. |
| `full_h_self_return` | **Pass.** Equation (3.2) reconstructs (n e(N_0j/n)), and the outside (1/n) plus (e(\xi j/n)) restores the original reciprocal row. |
| `primitive_g1` | **Pass.** Equations (3.5)--(3.6) are in the (g=1) stratum, where no outer-(g) cancellation is available. |
| `chi4_before_positive_norm` | **Pass with obstruction.** (\chi_4(n)) remains in (2.8). Multiplicative-character triangle, Schatten-one scalarization, or a row large sieve is invariant under its unit row sign and therefore does not extract its cancellation. |
| `moving_j_support_and_zero_extension` | **Pass as a source dichotomy.** Interior class repetition is priced by (3.4). If the literal entries/exits prevent such an interior common test, its smooth extension and endpoint norm remain an unproved source hypothesis; no endpoint is deleted or declared negligible. |
| `n_mod_j_class_price` | **Pass.** Whenever a full normalized flat interval is present, all (\varphi(j)) unit classes occur; classwise Corollary 2 costs (j^{3/2}), while grouped Mellin encoding still costs (j) for prime (j). |
| `projective_Sobolev_Bessel_norms` | **Pass.** Equations (1.1)--(1.3) give the exact optimal projective norm. Equations (3.8)--(3.12) show that low additive bandwidth misses almost all (L^2)-mass and high bandwidth forces (Z\gg C_g). |
| `long_h_complement` | **Fail for every audited scalar source.** The coverage ratios are (3.22); the exact complement identity is (3.3). |
| `level_four_eight_spectral_ledger` | **Fail if only levels (4/8) are retained.** Legal residue encoding forces (3.13)--(3.15) and all compatible (H+M+E), cusp, exceptional, new, and old pieces.  The principal component is odd; both parities occur across the nonprincipal conductor-\(4p\) family. |
| `boundary_power_saving` | **Pass as a no-go.** The scalar projective inflation is at least the required missing power by (3.5)--(3.6); the favourable direct-source screens (3.18)--(3.19) are already worse than (\Delta). |
| `source_theorem_literal_match` | **Fail for a positive theorem.** BC/Wright reject the joint Kloosterman coefficient; BM is fixed-(h,j), Linnik-range, and pays (3.7); DI requires one fixed-level sequence; ABL requires (\alpha_hF(h,n)), has no \(\chi_4(n)\) modulus twist, and pays the derivative bounds forced by the high-(t) and mod-\(4\) frequencies. |
| `flat_owner_and_downstream_scope` | **Pass.** The conclusion is confined to the one frozen flat-smooth strict-UNBAL owner and the canonical scalar routes. |
| even/odd (j), two-adic classes, and arbitrary gcds | **Pass as an audit.** The finite identity holds for every (j); the exact arithmetic period is (q_j={\rm lcm}(4,j)), and (3.15) retains every ((N_0,q_j^\infty)). The prime odd subcase already supplies the hostile projective and spectral-level obstruction; even classes are not discarded. |

All work was analytical and source-comparative.  No numerical experiment
was used.

## 6. Dependencies and exact artifacts used

The permitted local artifacts read and used were:

* `protocol.md`;
* `state/proof_obligations.yml`, in particular the five Round-160 target
  obligations and the accepted Round-135/143 obstruction nodes;
* `state/active_campaign.yml`;
* `strategy/round160_m2_unbalanced_inverse_selector_reciprocity_strategy.md`;
* `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
* `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
* `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md`;
* `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md`;
* `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/source_post_unmask_discovery_formula_audit.md`; and
* `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`.

Primary sources checked for the present theorem maps were:

1. S. Bettin and V. Chandee,
   [*Trilinear forms with Kloosterman fractions*, arXiv:1502.00769v1](https://arxiv.org/html/1502.00769v1),
   Theorem 1 and Remark 1.
2. T. Wright,
   [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177v2](https://arxiv.org/html/2604.25177v2),
   Theorem 2.1.  The weaker printed (A^{-1/20}) term, rather than the
   stronger exponent in the proof, is the accepted source statement.
3. V. Blomer and D. Milićević,
   [*Kloosterman sums in residue classes*, JEMS 17 (2015), 51--69](https://ems.press/content/serial-article-files/32008?nt=1),
   normalized Mellin transform (1.2), Theorem 1, Corollary 2, the encoding
   (2.3)--(2.5), transforms (4.1)--(4.6), spectral estimates
   (4.9)--(4.11), singular-cusp condition (5.1), and Theorem 4.
4. J.-M. Deshouillers and H. Iwaniec,
   [*Kloosterman Sums and Fourier Coefficients of Cusp Forms*, Invent.
   Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728),
   Theorems 1, 2, and 5, as source-card audited in the permitted Round-143
   report.
5. E. Assing, V. Blomer, and J. Li,
   [*Uniform Titchmarsh divisor problems*, arXiv:2005.13915](https://arxiv.org/html/2005.13915),
   Theorem 2.4.

The withdrawn arXiv:2601.00292 supplied no theorem.

## 7. Recommended state effect

**Promote only the scoped obstruction after independent seam review, and
retain the owner target open.**  The promotable kernel is (1.1)--(1.4),
together with the exact Mellin/additive-frequency and growing-level source
maps (3.7)--(3.15).  Record the exit label
`inverse_selector_projective_capacity_no_go` for canonical scalar
common-test, residue-class, fixed-level trace, common-sequence large-sieve,
and direct BC/Wright realizations.

Do not promote `M9-M2-smooth-unbalanced-three-quarter-estimate`, a strict
positive range, complete UNBAL, M9-M2, M9, endpoint uniformity, the quarter
bound, or a universal impossibility theorem.  A genuinely new vector-valued
literal-matrix estimate which preserves (\chi_4) before positive norms,
covers all long frequencies and moving endpoints, and audits every level
and spectral piece remains outside this no-go and is still open.

# Round 155 primary-source audit: the joint theta-bilinear spectral interface

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Role: primary-source auditor
- Literature checked through: 25 August 2026
- Starting graph: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

### Direct-interface source no-go, with one exact termwise match

Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM},
 \qquad J_A<V\le K.
\tag{155.SA1}
\]

For the literal fixed-modulus, nonseparable family in the brief, the
primary-source audit has a decisive answer.

1. Duke--Friedlander--Iwaniec (DFI), Section 6 and Lemma 6.1, is an
   **exact match for each individual completed sum**
   \(K(-v^2,-j;4N/d)\).  It permits all integer arguments, an arbitrary
   composite modulus divisible by four, the full gcd factor, and
   \(v=0\).  With the selector, Fourier, and Gauss factors restored, this
   is exactly the already accepted termwise bound
   \[
      |\mathcal Q_U(V)|\ll_\varepsilon
      \bigl(M^{-3/4}V+M^{-1/4}\bigr)X^\varepsilon.
   \tag{155.SA2}
   \]
2. DFI's half-integral-weight Kuznetsov formula and the current uniform
   theorems of Sun have the correct theta-multiplier spectral setting,
   but their geometric side sums over moduli.  They do not give a bound
   for one fixed \(q_d=4N/d\), and their nonzero-frequency statements
   exclude the actual \(v=0\) row.  Their spectral sides explicitly
   retain holomorphic, Maaß, Eisenstein, residual, or exceptional terms,
   according to the sign.  No one of those terms can be silently deleted.
3. The closest fixed-modulus bilinear theorem, Blomer--Pascadi Theorem
   1.1 (and its unequal-length Theorems 5.5 and 5.7), treats the ordinary
   Kloosterman sum with separated coefficients.  It does not treat the
   theta multiplier or the matrix coefficient
   \(A_{j,v}=\widehat B_j(2dv)\).  Shparlinski--Xiao likewise treats
   separated shifted Salié/root sums only for a large odd prime.  Neither
   theorem accepts the zero and imprimitive strata of \(4N/d\).
4. The available half-integral spectral large sieve closest to the
   requested interface, Lam Theorem 2.3, is a holomorphic, varying-weight,
   one-sequence inequality.  It is not a fixed-weight Maaß/continuous
   theta-spectrum large sieve for an arbitrary two-dimensional
   coefficient matrix.
5. Complete resummation in \(v\bmod(q_d/2)\) is not a new cancellation.
   Exact completion of the \(v\)-square returns the original quadratic
   selector stratum; see (155.SA20) below.  A useful transform would have
   to truncate or split the dual frequencies and then control both the
   retained part and the complementary self-return.  No audited theorem
   does this with the literal coefficient.
6. At fixed \(k\asymp K\), the selected phase \(e(-j/(2k))\) has only
   \(O(V/K)\le O(1)\) total archimedean variation across a dyadic
   \(j\)-block.  Thus a generic smooth-\(j\) Poisson or Kuznetsov placement
   has no source-legal nonstationary saving.  Its zero/near-zero reciprocal
   frequency, principal or exceptional term, profile transitions, and
   hard endpoints may survive.

Consequently no audited primary theorem proves the full
\(X^\varepsilon\) target or a strict owner-complete positive-power range
beyond the accepted polylogarithmic collar.  The exact source match is
**DFI Lemma 6.1, term by term only**.  The literal joint fixed-modulus
\((j,v)\) interface is a **no-match**.  This is a cutoff-checked
direct-interface conclusion, not a claim that no future theorem or
coefficient-sensitive argument can work.

## 2. Exact statement and hypotheses

### 2.1 Literal project object and normalization

The selected linearized block is

\[
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac{j}{2k}\right).
\tag{155.SA3}
\]

The exact pre-linearization ambient completion is

\[
 \mathcal T_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q_d}
 \sum_{v\bmod(q_d/2)}
 \widehat B_j(2dv)K(-v^2,-j;q_d),
 \quad q=4N,\quad q_d=\frac qd.
\tag{155.SA4}
\]

Here

\[
 \widehat B_j(b)=\sum_{x\bmod q}B_j(x)e_q(-bx).
\tag{155.SA5}
\]

The coefficient \(B_j\) contains the literal asymmetric cell
\(-k\le j\le k-1\), zero extension, all actual profile components and
transitions, the strict dyadic mask, both defect signs, and the exact
residual phase.  It is not permissible to replace
\(\widehat B_j(2dv)\) by bounded separated weights.  The external
\(B_{1,U}(1)\) factor is not part of (155.SA4) and remains an assembly
seam.

The DFI theta sum is

\[
 K(m,n;c)=\sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)
 e_c(m\bar a+na),\qquad c\equiv0\pmod4,
\tag{155.SA6}
\]

where \(\epsilon_a=1\) for \(a\equiv1\pmod4\),
\(\epsilon_a=i\) for \(a\equiv3\pmod4\), and the symbol is DFI's
extended Jacobi/Kronecker symbol.  Formula (155.SA4) contains exactly
\(K(-v^2,-j;q_d)\), with no conjugation or interchange of the arguments.

### 2.2 Exact theta-multiplier pointwise card: DFI Lemma 6.1

In W. Duke, J. B. Friedlander, and H. Iwaniec,
[*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
Section 6, equations (6.1)--(6.3) identify (155.SA6) as the Kloosterman
sum for the classical weight-one-half theta multiplier.  Lemma 6.1,
equation (6.8), states, for \(c\equiv0\pmod4\),

\[
 |K(m,n;c)|\le (m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{155.SA7}
\]

It applies to all integer \(m,n\), including \(m=0\), and to arbitrary
composite \(c\).  The proof factors the odd part into a Salié sum and
handles the full two-adic part separately.  It therefore retains, rather
than suppresses, all imprimitive gcd and two-adic strata.  The official
[DFI erratum](https://doi.org/10.1093/imrn/rnr240) does not alter Section
6 or Lemma 6.1.

This card is an exact match for a single \(K(-v^2,-j;q_d)\), but it has
no joint coefficient-sensitive \((j,v)\) conclusion.

### 2.3 Half-integral Kuznetsov and uniform modulus-sum cards

DFI Theorem 2.5 assumes \(m,n>0\) and a smooth \(g\) on
\([0,\infty)\) with
\[
 g(0)=g'(0)=0,\qquad g(x),g'(x),g''(x)\ll(x+1)^{-2-\varepsilon}
\]
The weakened option after the theorem still retains
\(g(0)=g'(0)=0\), while replacing the displayed decay by the
absolute-convergence conditions (2.28)--(2.29).
For the theta multiplier on \(\Gamma_0(q_0)\), \(4\mid q_0\), it writes

\[
 \gamma_k K_g(m,n)
   =L_{\widehat g}(m,n)+M_{\widehat g}(m,n)+N_{\check g}(m,n),
\quad
 K_g(m,n)=\sum_{c\equiv0\ (q_0)}
 \frac{K(m,n;c)}{c}\,g\!\left(\frac{4\pi\sqrt{mn}}c\right).
\tag{155.SA8}
\]

Thus even the exact theta-multiplier trace formula has a **modulus
average**.  Its right side is the complete discrete/residual,
continuous, and holomorphic spectral resolution; the diagonal cancels
only inside the complete formula, not by deleting individual pieces.

Sun's same-sign paper,
[*Uniform bounds for Kloosterman sums of half-integral weight, same-sign
case*](https://arxiv.org/html/2309.05233v2), makes the same distinction
especially explicit.  Definition 1.1 requires an admissible
weight-\(\pm1/2\) multiplier on \(\Gamma_0(N_0)\): level lifting and an
average Weil bound on modulus intervals \([y,x]\) only when
\(x-y\gg x^{2/3}\).  Lemma 1.2 includes the theta multiplier and its
quadratic twists.  Theorem 3.3 (Proskurin), directly for weight
\(k=1/2\) or \(3/2\) and \(\widetilde m,\widetilde n>0\), is

\[
 \sum_{c>0}\frac{S(m,n,c,\nu)}c
 \phi\!\left(\frac{4\pi\sqrt{\widetilde m\widetilde n}}c\right)
 =\mathcal U_k+\mathcal W+
   \sum_{\mathfrak a\ {\rm singular}}\mathcal E_{\mathfrak a},
\tag{155.SA9}
\]

where \(\mathcal U_k\), \(\mathcal W\), and \(\mathcal E_{\mathfrak a}\)
are respectively the holomorphic, Maaß, and Eisenstein pieces.  Sun
handles the negative-weight comparison elsewhere by conjugation and
raising/lowering.  Theorem 1.3 states

\[
 \sum_{N_0\mid c\le X}\frac{S(m,n,c,\nu)}c
 =\sum_{r_\ell\in i(0,1/4]}
   \tau_\ell(m,n)\frac{X^{2s_\ell-1}}{2s_\ell-1}
 +O_{\nu,\varepsilon}\!\left(
   (A_u(m,n)+X^{1/6})(\widetilde m\widetilde nX)^\varepsilon
 \right),
\tag{155.SA10}
\]

with the exact level-supported square-part factor

\[
 A_u(m,n)=
 (\widetilde m^{131/294}+u_m)^{1/8}
 (\widetilde n^{131/294}+u_n)^{1/8}
 (\widetilde m\widetilde n)^{3/16},
\tag{155.SA11}
\]

which is only \(\ll(\widetilde m\widetilde n)^{1/4}\) in general.
The exceptional sum in (155.SA10), including a possible
\(r=i/4\) theta term in the applicable weight, is part of the theorem.

For mixed signs, Sun,
[*Uniform bounds for Kloosterman sums of half-integral weight with
applications*](https://arxiv.org/html/2305.19651v2), Theorem 6.4 assumes
\(\widetilde m>0,\widetilde n<0\) and gives a modulus-sum geometric side
equal to a Maaß sum plus Eisenstein terms.  Theorem 1.2, under its
squarefree-or-coprime lifted-frequency hypotheses, gives

\[
 \sum_{N_0\mid c\le X}\frac{S(m,n,c,\nu)}c
 =\sum_{r_\ell\in i(0,1/4]}
  \tau_\ell(m,n)\frac{X^{2s_\ell-1}}{2s_\ell-1}
 +O_{\nu,\varepsilon}\!\left(
 (|\widetilde m\widetilde n|^{143/588}+X^{1/6})
 |\widetilde m\widetilde nX|^\varepsilon\right).
\tag{155.SA12}
\]

Its Theorem 1.4 removes those factor restrictions only by restoring the
level-supported square-part expression \(A_u(m,n)\); the paper warns that
the resulting middle terms are not negligible.

For the project, \(v\ne0,j>0\) gives two negative arguments and belongs,
after conjugation, to the same-sign formula; \(v\ne0,j<0\) is mixed sign.
The row \(v=0\) has first argument zero and lies outside every displayed
Poincaré/Kuznetsov hypothesis.  More fundamentally, all of
(155.SA8)--(155.SA12) average \(c\), whereas (155.SA4) fixes
\(c=q_d\).

### 2.4 Half-integral spectral large-sieve card

Jonathan W. C. Lam,
[*A local large sieve inequality for cusp forms*](https://doi.org/10.5802/jtnb.887),
Theorem 2.3, assumes \(M_0\equiv0\pmod4\), a sequence
\((a_n)_{N_1\le n\le2N_1}\), and a short interval of half-integral
holomorphic weights \(K_0\le k\le K_0+G\), with
\(k-\tfrac12\) even and \(1\le G\le K_0^{1-\varepsilon}\).  It proves

\[
 \sum_{\substack{K_0\le k\le K_0+G\\k-1/2\ {\rm even}}}
 \sum_{f\in B_{k,M_0}}
 \left|\sum_{N_1\le n\le2N_1}a_n\rho_f(n)\right|^2
 \ll (M_0K_0N_1)^\varepsilon(M_0K_0G+N_1)
 \sum|a_n|^2.
\tag{155.SA13}
\]

This is a one-sequence large sieve for holomorphic forms while the weight
varies.  Lam's Maaß theorem in the same paper is integral weight.  Hence
(155.SA13) is not a fixed-weight half-integral Maaß-plus-Eisenstein large
sieve for the arbitrary matrix \((\widehat B_j(2dv))_{j,v}\).

### 2.5 Fixed-modulus bilinear cards

Blomer--Pascadi,
[*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/html/2607.24311v1),
define the ordinary Kloosterman sum

\[
 S(m,n;c)=\sum_{x\bmod c}^{*}e_c(mx+n\bar x).
\tag{155.SA14}
\]

Their Theorem 1.1 assumes \(1\le H\le c\), two intervals of length at
most \(H\), arbitrary **separated** sequences \(\alpha_m,\beta_n\), a
unit \(a\pmod c\), and \((m,n,c)=1\).  It proves

\[
 \sum_{m,n}\alpha_m\beta_nS(am,n;c)
 \ll \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
 \left(H^{1/8}c^{-3/32}+H^{5/16}c^{-3/16}
       +H^{2/3}c^{-7/18}\right).
\tag{155.SA15}
\]

Only when both intervals are the initial intervals
\(\{1,\ldots,H\}\) can the gcd restriction be removed.  At
\(H=\sqrt c\), (155.SA15) is
\(\|\alpha\|_2\|\beta\|_2c^{1-1/32+o(1)}\).  Theorem 5.5 supplies an
explicit unequal-length factor \(H(M_1,N_1,c)\), still for ordinary
\(S\), separated coefficients, and the displayed gcd restriction.
Theorem 5.7 similarly proves

\[
 \sum_{\substack{m,n\\(m,c)=1}}
 \alpha_m\beta_nS(am,n;c)
 \ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
 \left((M_1N_1)^{1/2}c^{-3/4}
       +N_1^{1/2}c^{-1/2}+M_1^{1/2}c^{-1/4}\right).
\tag{155.SA16}
\]

These theorems do allow a fixed arbitrary modulus.  They fail the other
literal hypotheses: (155.SA6) has a theta multiplier; its first argument
is the sparse quadratic image \(-v^2\); \(v=0\) and many gcd strata are
mandatory; and \(\widehat B_j(2dv)\) is not \(\alpha_v\beta_j\).

Shparlinski--Xiao,
[*Shifted bilinear sums of Salié sums and the distribution of modular
square roots of shifted primes*](https://arxiv.org/html/2601.10113v1),
work throughout with a large odd prime \(q_0\).  Their Theorem 2.5 treats

\[
 W_{a,b,\lambda}=\sum_{m\le M_1}\sum_{n\le N_1}
 \alpha_m\beta_n
 \sum_{x^2\equiv amn+b\ (q_0)}e_{q_0}(\lambda x)
\tag{155.SA17}
\]

and proves, when \((a\lambda,q_0)=1\),

\[
 |W_{a,b,\lambda}|\ll
 \|\alpha\|_2\|\beta\|_\infty
 \left(M_1^{1/2}N_1^{1/2}+M_1^{1/2}N_1q_0^{-1/4}
       +N_1q_0^{1/4}(\log q_0)^{1/2}\right).
\tag{155.SA18}
\]

Prime modulus, the fixed product/shift congruence, and separated weights
are all essential parts of this card.  It does not specialize to the
arbitrary even composite \(q_d\), theta multiplier, or actual coefficient
in (155.SA4).

### 2.6 Closest modular-root cards

The modular-root sources do not repair the preceding mismatch.
Fouvry--Iwaniec, [*Gaussian primes*](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7935.pdf),
Lemma 2 averages \(8D<c\le9D\) and all roots of the fixed congruence
\(\nu^2+1\equiv0\pmod c\).  For every complex sequence \(\alpha_n\), it
states
\[
 \sum_{8D<c\le9D}\ \sum_{\nu^2+1\equiv0\ (c)}
 \left|\sum_{n\le T}\alpha_ne(\nu n/c)\right|^2
 \le72(D+T)\sum_{n\le T}|\alpha_n|^2.
\]
It does not hold at one fixed \(N\) with a varying right side \(j\).

Baier,
[*Partial progress towards the large sieve for square moduli*](https://arxiv.org/html/2605.01635v3),
Theorem 6 assumes separated coefficients, includes every modular root,
and requires an odd squarefree modulus \(r\) (with a separate
prime-square case), \((r,j)=1\),
\(r^\varepsilon\le L_0,M_0\le r^{1-\varepsilon}\),
\(|f'|\le F\le L_0^{-1}\), and
\(r^\varepsilon\le H\le\min\{(L_0F)^{-1},M_0\}\).  Its squarefree
conclusion is

\[
 \Sigma_f\ll
 \left(H^{-1/2}L_0^{1/2}M_0
       +L_0^{1/2}M_0^{1/2}r^{1/4}+M_0\right)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon
\tag{155.SA19}
\]

under the theorem's support and derivative hypotheses.  The completion
modulus \(4N/d\) is even and generally imprimitive, while the literal
cell selects a real representative and makes the quotient profile and
residual phase depend jointly on that representative and \(j\).  Thus
neither modular-root card accepts (155.SA4).

## 3. Proof or derivation

### 3.1 Complete half-period resummation is an inverse-Gauss self-return

Fix an odd \(d\mid N\), put \(Q=q_d=q/d\), and fix
\(a\in(\mathbb Z/Q\mathbb Z)^*\).  From (155.SA5),

\[
 \widehat B_j(2dv)=\sum_{x\bmod q}B_j(x)e_Q(-2vx).
\]

Completing the square, using \(a\bar a\equiv1\pmod Q\), gives the exact
identity

\[
\begin{split}
 &\sum_{v\bmod(Q/2)}\widehat B_j(2dv)e_Q(-\bar a v^2)\\
 &\quad=\sum_{x\bmod q}B_j(x)e_Q(ax^2)
       \sum_{v\bmod(Q/2)}e_Q(-\bar a v^2)\\
 &\quad=\frac12G(-\bar a,0;Q)
       \sum_{x\bmod q}B_j(x)e_Q(ax^2),
\end{split}
\tag{155.SA20}
\]

where \(G(b,0;Q)=\sum_{y\bmod Q}e_Q(by^2)\).  Indeed,
\(-\bar a v^2-2vx=-\bar a(v+ax)^2+ax^2\), and the quadratic summand has
period \(Q/2\) because \(4\mid Q\).  The half-period sum is therefore
exactly half of the complete Gauss sum.  For odd \(a\),
\(|G(-\bar a,0;Q)|=\sqrt{2Q}\).

Expanding \(K(-v^2,-j;Q)\), inserting (155.SA20), and then summing over
\(a\) cancels the same Gauss multiplier used to obtain (155.SA4) and
returns the original \(h=da\) quadratic-selector stratum.  Thus complete
\(v\)-resummation is algebraically invertible; it is not an independent
square-root gain.  A truncated transform remains conceivable, but it
must price the cutoff, the complementary frequencies, and the returned
principal/endpoint terms.

### 3.2 Normalization, zero row, and restored powers

Write \(W=M^{-3/4}\), with harmless \(X^\varepsilon\) factors suppressed.
Apart from the fixed \(|1+i|\), the coefficient of one \(d\)-stratum in
(155.SA4) is

\[
 P_d=\frac{d\sqrt Q}{2Nq}=\frac{\sqrt d}{4N^{3/2}}.
\tag{155.SA21}
\]

After applying (155.SA7), its \(Q^{1/2}\) factor satisfies the exact
normalization

\[
 P_dQ^{1/2}=\frac{dQ}{2Nq}=\frac1{2N}.
\tag{155.SA22}
\]

There is no residual square-root modulus gain or loss after this point.
Bounded variation of the literal \(B_j\) gives

\[
 |\widehat B_j(0)|\ll KW,
 \qquad
 |\widehat B_j(2dv)|\ll
 W\min\!\left(K,\frac Q{|2v|_Q}\right).
\tag{155.SA23}
\]

For \(v\ne0\), the full gcd expansion in (155.SA7) yields the accepted
harmonic estimate

\[
 \sum_{v\ne0}|\widehat B_j(2dv)|(v^2,j,Q)^{1/2}
 \ll WQX^\varepsilon.
\tag{155.SA24}
\]

Restoring (155.SA22), all odd \(d\mid N\), and \(O(V)\) values of \(j\)
gives \(WVX^\varepsilon\).

The zero row must be computed separately.  Since

\[
 \sum_{V<|j|\le2V}(j,Q)^{1/2}
 \ll (V+Q^{1/2})Q^\varepsilon,
\]

its complete source-legal capacity is

\[
 Z_0(V)\ll
 \frac{KW}{N}(V+\sqrt N)X^\varepsilon
 =\left(\frac{V}{\sqrt N\,M^{1/4}}+M^{-1/4}\right)X^\varepsilon.
\tag{155.SA25}
\]

At \(V=K\), the first term in (155.SA25) is \(M^{1/4}\), while the
nonzero termwise capacity is

\[
 WV=N^{1/2}M^{-1/4}.
\tag{155.SA26}
\]

Both can exceed \(X^\varepsilon\).  Equations (155.SA25)--(155.SA26)
are upper capacities, not lower bounds for either signed contribution.
They show exactly why omitting \(v=0\), or quoting only a nonzero spectral
formula, cannot prove the literal target.

A hypothetical square-root gain over the \(O(VX^\varepsilon)\) selected
incidences would give \(WV^{1/2}\).  It is target-sized precisely when

\[
 W\sqrt V\le1\quad\Longleftrightarrow\quad V\le M^{3/2}.
\tag{155.SA27}
\]

This is only a power-capacity calculation.  None of the source cards
proves that signed square-root incidence estimate.  At \(V=K\), condition
(155.SA27) forces \(M\ge N^{1/2}\), the boundary case of the frozen
range, and hence cannot supply the general all-scale result.

### 3.3 Why the spectral and bilinear cards do not translate

For a Kuznetsov placement, the first geometric mismatch is

\[
 \text{one fixed }c=Q
 \quad\not=\quad
 \sum_{c\equiv0\ (N_0)}c^{-1}S(m,n,c,\nu)\phi(\cdots/c).
\tag{155.SA28}
\]

An exact trace formula can be fed a very narrow smooth bump, but none of
the quoted uniform bounds permits replacing its required broad modulus
window by a delta at \(Q\).  Sun's admissibility estimate itself requires
window length \(\gg x^{2/3}\).  Delta localization also enlarges the
Bessel-transform/derivative norms and still leaves every Maaß,
Eisenstein, holomorphic, residual, and exceptional term shown in
(155.SA9)--(155.SA12).

There is then an independent coefficient mismatch.  On the spectral side
the two frequencies occur as products such as
\(\overline{\rho_\ell(-v^2)}\rho_\ell(-j)\).  To use a separated
large-sieve estimate on
\(A_{j,v}=\widehat B_j(2dv)\), one must first prove an exact decomposition

\[
 A_{j,v}=\sum_r\sigma_r u_r(j)\overline{w_r(v)}
\tag{155.SA29}
\]

and restore the total nuclear norm \(\sum_r|\sigma_r|\), not merely the
Frobenius/Parseval norm.  No audited card bounds the actual matrix directly
or supplies a target-sized ledger for (155.SA29).  The same replacement
by \(\alpha_v\beta_j\) is the first coefficient-illegal step in applying
Blomer--Pascadi or Shparlinski--Xiao.  Before any power from those
theorems can be translated, their ordinary/prime kernel and gcd
hypotheses also fail.

Finally, at fixed \(k\asymp K\),

\[
 \frac{d}{dj}\left(-\frac{j}{2k}\right)=-\frac1{2k},
 \qquad
 \operatorname{Var}_{V<|j|\le2V}\!\left(-\frac{j}{2k}\right)
 \asymp\frac VK\le1.
\tag{155.SA30}
\]

The exact pre-linearization residual phase has the same leading scale.
Therefore smoothness of the \(j\)-coefficient is not itself oscillation:
zero/near-zero Poisson frequency and reciprocal stationary or principal
terms are allowed.  The actual profile transitions, strict mask,
asymmetric cell endpoints, and external \(B_{1,U}(1)\) seam prevent
replacing the block by a globally smooth endpoint-free model.

## 4. First doubtful or unproved step

The first source-unproved term in every nonzero-frequency spectral route
is the literal \(v=0\) row.  It has \(m=0\), so DFI Lemma 6.1 applies
pointwise but the Sun/Proskurin nonzero-frequency formulas do not.  The
best audited source-legal restoration is (155.SA25), which is
\(M^{1/4}X^\varepsilon\) at the top block.  A target proof therefore first
needs a signed fixed-modulus outer-\(j\) estimate or exact principal-term
evaluation for

\[
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d),
\tag{155.SA31}
\]

uniformly in every odd \(d\mid N\), both signs, the literal profile, and
the endpoints.

If (155.SA31) is resolved separately, the next and central unproved step
is a target-sized estimate for the nonzero coupled fixed-modulus form

\[
 \sum_{V<|j|\le2V}
 \sum_{v\bmod(Q/2)}^{v\ne0}
 \widehat B_j(2dv)K(-v^2,-j;Q),
 \qquad Q=4N/d,
\tag{155.SA32}
\]

after the exact factor \(P_d\), all \(d\), exceptional/principal terms,
the complementary part of any truncated \(v\)-transform, and all
endpoints are restored.

For the Kuznetsov route, the first source-illegal inference is to replace
the fixed \(Q\) in (155.SA31)--(155.SA32) by a broad modulus average (or
to assert that a delta-localized trace formula has the broad-window bound)
and then omit spectral principal/exceptional pieces.  For the
fixed-modulus bilinear route, it is to replace the theta kernel and
\(\widehat B_j(2dv)\) by an ordinary Kloosterman kernel and separated
weights.  No source-legal \(N,M,V,d\) power can be assigned after either
replacement.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_outer_defect_block` | **PASS.** Equations (155.SA3)--(155.SA4) retain the exact selected and ambient objects; no post-selection row identity is transferred to the ambient completion. |
| `exact_Bj_and_nonseparable_coefficient` | **PASS / SOURCE NO-MATCH.** The actual cell, zero extension, profile, mask, and exact residual phase remain in \(B_j\). No theorem card accepts \(A_{j,v}=\widehat B_j(2dv)\); (155.SA29) records the missing total-norm ledger. |
| `mod4N_selector_and_full_normalization` | **PASS.** The factor \(-i/(2N)\), Fourier factor \(1/q\), Gauss factor \((1+i)d\sqrt Q\), and \(dQ=q\) give (155.SA21)--(155.SA22). |
| `all_gcd_two_adic_and_multiplier_strata` | **PASS.** Every odd \(d\mid N\), arbitrary composite \(Q\equiv0\pmod4\), DFI multiplier, and \((v^2,j,Q)^{1/2}\) factor are retained. Prime/primitive models are rejected. |
| `zero_mode_and_exceptional_terms` | **PASS AS AUDIT / SOURCE NO-MATCH.** The zero row is (155.SA25) and lies outside the nonzero Kuznetsov hypotheses. Sun's exceptional sum and the full holomorphic/Maaß/Eisenstein pieces are printed, not discarded. |
| `complete_vs_truncated_v_transform` | **PASS.** The complete half-period identity (155.SA20) is an inverse-Gauss self-return. No source controls a useful truncation plus its complement with the literal coefficient. |
| `positive_negative_defect_and_cell_endpoints` | **PASS.** Positive defect invokes the same-sign spectral geometry after conjugation; negative defect invokes mixed sign. The asymmetric cell and its hard endpoints remain in \(B_j\). |
| `N_M_V_d_power_ledger` | **PASS.** The stratum prefactor, exact \(1/(2N)\) cancellation, nonzero capacity \(WV\), sharp zero capacity (155.SA25), and top powers (155.SA26) are restored. |
| `actual_profile_transitions_and_B11` | **PASS.** Transitions and hard support boundaries are retained. \(B_{1,U}(1)\) remains an external assembly seam and is not absorbed into a smooth surrogate. |
| `fixed_modulus_vs_modulus_average_source_match` | **PASS / NO-MATCH.** DFI/Sun spectral bounds average the modulus; Blomer--Pascadi is fixed-modulus but ordinary and separated. Neither is the literal interface. |
| `square_root_range_V_le_Mthreehalves` | **PASS AS CAPACITY ONLY.** Equation (155.SA27) gives exactly \(V\le M^{3/2}\). No cited theorem proves the needed signed square-root incidence estimate, so no range is promoted. |
| `absolute_capacity_vs_signed_sum` | **PASS.** Equations (155.SA25)--(155.SA27), Parseval/nuclear norms, and positive theorem right sides are explicitly upper capacities, never signed lower bounds. |
| `D_L_generic_tge2_cross_and_downstream_scope` | **PASS.** Nothing here proves \(D>1\), \(L>1\), generic \(t=1\), an original \(t\ge2\) layer, the Round-138 cross owner, another M1 owner, M2, endpoint assembly, M9, the bridge, either target, or a global exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

### Project context read

Every context artifact permitted by the brief was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round155_d1_outer_defect_theta_dispersion_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/candidates/conductor_round155_outer_defect_seed.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/source_conductor_round154_final.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`.

### Primary sources audited

1. W. Duke, J. B. Friedlander, H. Iwaniec, *Weyl Sums for Quadratic
   Roots*, IMRN 2012, no. 11, 2493--2549, Theorems 1.1, 1.2, 2.5,
   Section 6 and Lemma 6.1,
   [DOI](https://doi.org/10.1093/imrn/rnr112),
   [author PDF](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
   together with the [official erratum](https://doi.org/10.1093/imrn/rnr240).
2. Q. Sun, *Uniform bounds for Kloosterman sums of half-integral weight
   with applications*, arXiv:2305.19651v2, Definition 1.1, Theorems
   1.2--1.4 and 6.4,
   [primary arXiv HTML](https://arxiv.org/html/2305.19651v2),
   [journal DOI](https://doi.org/10.1515/forum-2023-0201).
3. Q. Sun, *Uniform bounds for Kloosterman sums of half-integral weight,
   same-sign case*, arXiv:2309.05233v2, Definition 1.1, Lemma 1.2,
   Theorems 1.3, 1.5, and 3.3,
   [primary arXiv HTML](https://arxiv.org/html/2309.05233v2),
   [journal DOI](https://doi.org/10.1016/j.jnt.2024.11.012).
4. J. W. C. Lam, *A local large sieve inequality for cusp forms*, Journal
   de Théorie des Nombres de Bordeaux 26 (2014), Theorem 2.3,
   [DOI and journal text](https://doi.org/10.5802/jtnb.887).
5. V. Blomer, A. Pascadi, *Bilinear forms with Kloosterman sums via
   quadratic characters*, arXiv:2607.24311v1 (27 July 2026), Theorems
   1.1, 5.5, and 5.7,
   [primary arXiv HTML](https://arxiv.org/html/2607.24311v1).
6. I. E. Shparlinski, Y. Xiao, *Shifted bilinear sums of Salié sums and
   the distribution of modular square roots of shifted primes*,
   arXiv:2601.10113v1 (15 January 2026), Theorem 2.5,
   [primary arXiv HTML](https://arxiv.org/html/2601.10113v1).
7. E. Fouvry, H. Iwaniec, *Gaussian primes*, Acta Arithmetica 79 (1997),
   Lemma 2,
   [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7935.pdf).
8. S. Baier, *Partial progress towards the large sieve for square moduli*,
   arXiv:2605.01635v3 (20 July 2026), Theorem 6 and Corollary 7,
   [primary arXiv HTML](https://arxiv.org/html/2605.01635v3).

The search cutoff is a direct-interface check, not an assertion that the
printed bibliography exhausts all related literature.  The only workspace
edit made by this task is this assigned report.

## 7. Recommended state effect

**Recommendation: retain the full outer-defect target as open; record a
route-scoped source no-go and no new positive-power range.**

More precisely:

1. retain DFI Lemma 6.1 as the exact individual theta-Kloosterman match
   and retain the accepted bound (155.SA2), with no stronger joint
   interpretation;
2. record that current half-integral Kuznetsov/uniform estimates are
   modulus averages with explicit spectral principal/exceptional pieces,
   while the literal problem fixes \(q_d\);
3. record (155.SA20), subject to independent algebra review, as the exact
   reason complete unrestricted \(v\)-resummation self-returns rather
   than supplies a second Gauss gain;
4. retain (155.SA31) as the first source-unproved step and (155.SA32) as
   the next nonzero coupled-matrix step;
5. retain \(V\le M^{3/2}\) only as the threshold for a hypothetical
   square-root selected-incidence estimate, not as a proved range; and
6. make no change to the \(M^{449}\asymp R^{780}\) owner boundary, any
   endpoint or downstream obligation, either target, or either global
   exponent.

The proper route label is
`theta_bilinear_spectral_direct_interface_no_go`.  It must not be
paraphrased as an impossibility theorem for future fixed-modulus
theta-bilinear or coefficient-sensitive arguments.

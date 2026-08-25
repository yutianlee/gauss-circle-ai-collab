# Round 157 primary-source audit: the centered nonzero theta matrix

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Role: primary-source auditor
- Literature checked through: 25 August 2026
- Starting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

### Cutoff-dated source-interface no-go, not a mathematical impossibility

Put

\[
 q=4N,\qquad c=\frac{4N}{d},\qquad H=\frac c2,\qquad
 d\mid N\ \mathrm{odd},\qquad W=M^{-3/4},\qquad K=\sqrt{NM},
\]

and let \(M^{3/4}(\log(2X))^A<V\le K\). The literal open object is

\[
 \mathcal T_{\ne0,U}(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod H\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{157.SA1}
\]

The audit found **no primary theorem, as of the stated cutoff, that
accepts (157.SA1) or its exactly centered physical form and proves the
target or a strict owner-complete positive-power range beyond the
already accepted fixed-polylogarithmic collar**. The conclusions are more
specific than a generic “spectral methods do not work” statement.

1. Duke--Friedlander--Iwaniec (DFI), Lemma 6.1, exactly matches each
   individual theta-multiplier sum \(K(-v^2,-j;c)\), for arbitrary
   composite \(c\equiv0\pmod4\) and all gcd strata. It yields only the
   already known termwise nonzero capacity
   \[
      |\mathcal T_{\ne0,U}(V)|
      \ll M^{-3/4}V X^\varepsilon,
   \tag{157.SA2}
   \]
   whose top value is \(N^{1/2}M^{-1/4}X^\varepsilon\). This is an upper
   capacity, not a signed lower obstruction.
2. There is no audited direct theorem for the centered discrepancy of
   the two affine root families
   \(x^2\equiv j+N,j+3N\pmod{4N}\), with \(j\) in one signed interval,
   \(x\) in one short interval, and one fixed arbitrary even composite
   modulus. Existing modular-root theorems either average the modulus,
   fix the right-hand discriminant, require a prime/odd-squarefree
   modulus, or retain separated weights.
3. The newest fixed-modulus results were checked explicitly. Pascadi's
   paper published on 21 August 2026, Blomer--Pascadi (27 July 2026), and
   Milićević--Qin--Wu treat the **ordinary** Kloosterman kernel and
   separated row/column sequences. Shparlinski--Xiao and Baier treat
   prime or odd-squarefree/prime-square Salié or modular-root kernels and
   again require separated sequences. None treats the theta multiplier
   at \(c=4N/d\), none takes the literal entrywise coefficient
   \[
     A^{(d)}_{j,v}=\widehat B_j(2dv),
   \tag{157.SA3}
   \]
   and none supplies a nuclear-norm estimate for this matrix.
4. The exact half-integral Kuznetsov formula has the correct theta
   multiplier and, after the proved removal of \(v=0\), its nonzero
   frequency condition is no longer the problem. Its geometric side
   nevertheless averages moduli. DFI, Sun, and Andersen--Duke do not
   provide a delta-localized bound at the one growing modulus \(c=4N/d\),
   and all Maaß, holomorphic, Eisenstein, residual/principal, and
   exceptional pieces required by their formulas remain.
5. Half-integral spectral large sieves such as Lam's Theorem 2.3 are
   one-sequence, holomorphic, varying-weight results. The exceptional
   Maaß large sieves appended to the 2026 ordinary-Kloosterman papers are
   integral-weight applications and likewise do not accept (157.SA3).

There is, however, a sharply identified sufficient theorem. The selected
block has the internally verified support count

\[
 L(V)\ll \min(M,V)X^\varepsilon.
\tag{157.SA4}
\]

A genuine signed square-root incidence estimate for the literal selected
phases would therefore give

\[
 W\sqrt{L(V)}
 \ll M^{-3/4}\min(M,V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon
\tag{157.SA5}
\]

uniformly for **every** selected \(V\). No audited source proves that
signed estimate. Equation (157.SA4) counts support; it is not itself
cancellation. In particular, the older ambient calculation
\(W\sqrt V\le1\iff V\le M^{3/2}\) is not the correct selected-incidence
ledger once (157.SA4) is used.

## 2. Exact statement and hypotheses

### 2.1 Literal centered and theta interfaces

The theta sum is DFI's weight-one-half sum

\[
 K(m,n;c)=\sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(m\bar a+na),
 \qquad c\equiv0\pmod4.
\tag{157.SA6}
\]

Both the multiplier and the order of the arguments in
\(K(-v^2,-j;c)\) are literal. The coefficient (157.SA3) contains the
actual profile, residual phase, asymmetric cell, zero extension,
transitions, hard endpoints, and both signed \(j\)-blocks. It is not
permissible to replace it by \(\alpha_v\beta_j\). The external
\(B_{1,U}(1)\) factor is not part of (157.SA1); it remains a separate
assembly seam and no source estimate below absorbs it.

With

\[
 G_N(t)=\mathbf{1}_{N\mid t}\chi_4(t/N),\qquad
 A_j=\widehat B_j(0),\qquad
 B_j^\circ(x)=B_j(x)-\frac{A_j}{q},
\]

the exact physical form is

\[
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}
 B_j^\circ(x)G_N(x^2-j),
 \qquad \sum_{x\bmod q}B_j^\circ(x)=0.
\tag{157.SA7}
\]

Since

\[
 G_N(x^2-j)=
 \mathbf{1}_{x^2\equiv j+N\ (4N)}
 -\mathbf{1}_{x^2\equiv j+3N\ (4N)},
\tag{157.SA8}
\]

the rectangular source target is exactly

\[
 \mathscr D_N(I,J)=
 \sum_{j\in J}\sum_{x\in I}G_N(x^2-j)
 -\frac{|I|}{q}\sum_{j\in J}\mathscr S_N(j),
 \qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\tag{157.SA9}
\]

The finite projector

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}
 \chi_4(h)e_q(ht)
\tag{157.SA10}
\]

also gives the exact fixed-modulus incomplete-quadratic form

\[
 \mathscr D_N(I,J)=
 -\frac{i}{2N}\sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}\chi_4(h)
 \left\{\sum_{x\in I}e_q(hx^2)
 -\frac{|I|}{q}\sum_{x\bmod q}e_q(hx^2)\right\}
 \sum_{j\in J}e_q(-hj).
\tag{157.SA11}
\]

Thus a purported incomplete quadratic-root theorem must keep the
centered complete-Gauss subtraction in braces, the odd-character weight,
all gcd strata of \(4N\), both affine root signs in (157.SA8), and the
joint \(h,x,j\) sum. A pointwise incomplete Gauss estimate followed by
absolute \(h\)-summation is not the requested theorem.

### 2.2 Exact pointwise theta card

In W. Duke, J. B. Friedlander, and H. Iwaniec,
[*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
Section 6 identifies (157.SA6) with the theta multiplier. Lemma 6.1,
equation (6.8), states for all integers \(m,n\) and every
\(c\equiv0\pmod4\),

\[
 |K(m,n;c)|\le (m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{157.SA12}
\]

Its proof factors the odd Salié component and treats the full two-adic
part, so arbitrary composite \(c\), imprimitive gcd strata, and both
signs are legal. The [DFI erratum](https://doi.org/10.1093/imrn/rnr240)
does not alter Section 6. This is the only audited theorem with a literal
kernel match; it is pointwise rather than matrix-sensitive.

### 2.3 Fixed-modulus modular-root cards

The closest direct root theorems have the following exact interfaces.

**Dunn--Kerr--Shparlinski--Zaharescu, Theorem 1.7.** For a prime \(p\),
nonzero \(a,h\pmod p\), \(M_0,N_0\le p/2\), and separated weights on
dyadic intervals, define

\[
 W_{a,p}=\sum_{m\sim M_0}\sum_{n\sim N_0}\alpha_m\beta_n
 \sum_{x^2=amn\ (p)}e_p(hx).
\]

The first of their two bounds is

\[
 |W_{a,p}|\le
 \|\alpha\|_2\|\beta\|_\infty^{1/3}\|\beta\|_1^{2/3}
 p^{1/8+o(1)}M_0^{7/24}N_0^{1/8}
 \left(1+M_0^{7/48}p^{-1/16}\right)
 \left(1+N_0^{7/48}p^{-1/16}\right),
\tag{157.SA13}
\]

and the second replaces the norm factor by
\(\|\alpha\|_2\|\beta\|_1^{3/4}\|\beta\|_\infty^{1/4}\), the powers
\(M_0^{7/24}N_0^{1/8}\) by \(M_0^{5/16}N_0^{1/16}\), and
\(7/48,1/16\) by \(3/16,1/8\). The modulus is prime, the right side is
the multiplicative product \(amn\), the additive root mode is fixed,
and the weights are separated.

**Shparlinski--Xiao, Theorem 2.5.** Their 2026 paper works with a large
odd prime \(p\). For separated \(\alpha_m,\beta_n\) and
\((a\lambda,p)=1\), it bounds the shifted-root form

\[
 \sum_{m\le M_0}\sum_{n\le N_0}\alpha_m\beta_n
 \sum_{x^2\equiv amn+b\ (p)}e_p(\lambda x)
\]

by

\[
 \|\alpha\|_2\|\beta\|_\infty
 \left(M_0^{1/2}N_0^{1/2}+M_0^{1/2}N_0p^{-1/4}
 +N_0p^{1/4}(\log p)^{1/2}\right).
\tag{157.SA14}
\]

The shift \(b\) does not remove the prime-modulus or separated-weight
hypotheses.

**Baier, Theorem 6 and Corollary 7.** For

\[
 \Sigma_f=\sum_{|\ell|\le L_0}\sum_{m\le M_0}
 \alpha_\ell\beta_m e_r(\ell\sqrt{jm})e(\ell f(m)),
\]

Theorem 6 assumes \((r,j)=1\),
\(r^\varepsilon\le L_0,M_0\le r^{1-\varepsilon}\),
\(|f'|\le F\le L_0^{-1}\), and
\(r^\varepsilon\le H_0\le\min((L_0F)^{-1},M_0)\). For odd squarefree
\(r\),

\[
 \Sigma_f\ll
 \left(H_0^{-1/2}L_0^{1/2}M_0
 +L_0^{1/2}M_0^{1/2}r^{1/4}+M_0\right)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon.
\tag{157.SA15}
\]

There is a separate prime-square formula with an additional
\(H_0^{-1/2}L_0^{1/2}M_0^{1/2}r^{3/8}\) term. Corollary 7, \(f=0\),
has the squarefree right side

\[
 \left(L_0^{1/2}M_0^{1/2}r^{1/4}+M_0\right)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon.
\tag{157.SA16}
\]

It is still a product-root theorem with separated coefficients. The
literal \(r=c=4N/d\) is even, and the complete \(v\)-family has length
\(H=c/2\), outside \(r^{1-\varepsilon}\).

DFI Theorem 1.1 and the root large sieve of Fouvry--Iwaniec are not
fixed-modulus replacements. DFI fixes a positive odd fundamental
discriminant \(D\), smooths \(Y\le y\le2Y\), and averages congruence
moduli \(c\equiv0\pmod{q_0}\); its bound is

\[
 W_h(D)\ll h^{1/4}(Y+h\sqrt D)^{3/4}
 D^{1/8-1/1331}.
\tag{157.SA17}
\]

Here \(j\) varies and is generally signed and nonfundamental while the
modulus \(4N\) is fixed. Fouvry--Iwaniec, *Gaussian primes*, Lemma 2,
states

\[
 \sum_{8D<c\le9D}\ \sum_{\nu^2+1\equiv0\ (c)}
 \left|\sum_{n\le T}\alpha_ne(\nu n/c)\right|^2
 \le72(D+T)\sum_{n\le T}|\alpha_n|^2,
\tag{157.SA18}
\]

again averaging \(c\) and fixing the congruence \(\nu^2+1=0\).

### 2.4 The 2026 fixed-modulus ordinary-Kloosterman cards

All three arbitrary-modulus results below use the ordinary kernel

\[
 S(m,n;c)=\sum_{x\bmod c}^{*}e_c(mx+n\bar x),
\tag{157.SA19}
\]

not the theta kernel (157.SA6).

**Pascadi, Theorem 1.1 (published 21 August 2026).** If
\(M_0,N_0\ll c^{1/2+o(1)}\), \(a\in(\mathbb Z/c\mathbb Z)^*\), and
\(\alpha_m,\beta_n\) are arbitrary separated sequences, then

\[
 \mathop{\sum_{m\le M_0}\sum_{n\le N_0}}_{(m,n,c)=1}
 \alpha_m\beta_n S(am,n;c)
 \ll \|\alpha\|_2\|\beta\|_2c^{1-1/700+o(1)}.
\tag{157.SA20}
\]

If \(|\alpha_m|\le1\), his second estimate removes \(m\) from the gcd
restriction and replaces the right side by
\(M_0^{1/2}\|\beta\|_2c^{1-1/276+o(1)}\). Proposition 4.10 calls a
matrix a “Kloosterman matrix”, but its entries are exactly

\[
 \psi_1(m)\psi_2(n)S(m,n;c)\nu_{(m,n,c_1)}
 \mathbf{1}_{(m,n,c_2)=1},
\tag{157.SA21}
\]

where \(c_1\) is squarefree and \(c_2\) square-full. The proposition
bounds its **operator norm**. Neither the theorem nor the proposition
pairs this kernel entrywise with an arbitrary matrix \(A_{m,n}\), and
the paper supplies no nuclear-norm estimate for (157.SA3).

**Blomer--Pascadi, Theorem 1.1 (27 July 2026).** If two integer
intervals have lengths at most \(H_0\le c\), the weights are separated,
\(a\) is a unit, and \((m,n,c)=1\), then

\[
 \sum_{m,n}\alpha_m\beta_nS(am,n;c)
 \ll \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
 \left(H_0^{1/8}c^{-3/32}+H_0^{5/16}c^{-3/16}
 +H_0^{2/3}c^{-7/18}\right).
\tag{157.SA22}
\]

Only for the two initial intervals may the gcd condition be dropped.
At \(H_0=\sqrt c\), (157.SA22) is
\(\|\alpha\|_2\|\beta\|_2c^{1-1/32+o(1)}\). The title's “quadratic
characters” describe the proof method; the theorem kernel remains the
ordinary \(S\) in (157.SA19).

**Milićević--Qin--Wu, Theorem 1.1.** Their normalization is

\[
 \mathrm{Kl}_2(a;c)=c^{-1/2}\sum_{x\bmod c}^{*}e_c(ax+\bar x).
\tag{157.SA23}
\]

For separated sequences on \([1,M_0]\), \([1,N_0]\), a unit \(a\), and

\[
 1\le M_0\le N_0c^{1/4},\qquad
 M_0^{7/5}N_0<c^{3/2},\qquad M_0N_0\le c^{5/4},
\]

they prove

\[
 \left|\sum_{m\le M_0}\sum_{n\le N_0}
 \alpha_m\beta_n\mathrm{Kl}_2(amn;c)\right|
 \ll c^\varepsilon\|\alpha\|_2\|\beta\|_2(M_0N_0)^{1/2}
 \left(M_0^{-1/2}c^{1/6}
 +M_0^{-3/25}N_0^{-3/10}c^{1/5}
 +(M_0N_0)^{-3/16}c^{11/64}\right).
\tag{157.SA24}
\]

For an unnormalized ordinary \(S\), a factor \(c^{1/2}\) must be
restored. The kernel depends on the product \(mn\), the weights are
separated, and neither the theta multiplier nor the sparse first
argument \(-v^2\) is present.

### 2.5 Quadratic large-sieve, Kuznetsov, and half-integral spectral cards

Liu's explicit form of the Heath--Brown quadratic large sieve assumes
odd squarefree character moduli and odd squarefree summation variables.
Writing
\[
 \mathcal B(Q_0,L_0)=
 \sup_{\|a\|_2\ne0}
 \frac{\displaystyle\sum_{m\sim Q_0}^{*}
 \left|\sum_{n\sim L_0}^{*}a_n\left(\frac nm\right)\right|^2}
 {\|a\|_2^2},
\]
Theorem 1 states that an absolute \(C>0\) exists such that, for every
\(\varepsilon>0\),

\[
 \mathcal B(Q_0,L_0)\le
 \exp_4(C\varepsilon^{-1})(Q_0L_0)^\varepsilon(Q_0+L_0).
\tag{157.SA25}
\]

The gain is an average over quadratic characters/moduli \(m\). It has
no additive root coordinate \(x\), no fixed \(4N\), no quotient
\(\chi_4((x^2-j)/N)\), and no two-dimensional coefficient (157.SA3).
The explicit constants do not change this interface. Equations
(157.SA18) and (157.SA25) therefore do not become fixed-modulus
dispersion theorems by freezing their outer variable.

DFI Theorem 2.5 assumes \(m,n\geq1\), a singular cusp at infinity, and
a smooth \(g\) satisfying its condition (2.8), in particular

\[
 g(0)=g'(0)=0,\qquad g,g',g''\ll(1+x)^{-2-\varepsilon},
\]

The stronger decay condition (2.9) may be weakened only while retaining
(2.8) together with the transform estimates (2.28)--(2.29). Its
geometric side is

\[
 \sum_{c\equiv0\ (q_0)}\frac{K(m,n;c)}c
 g\!\left(\frac{4\pi\sqrt{mn}}c\right).
\tag{157.SA26}
\]

Its spectral side is the complete discrete/residual, continuous, and
holomorphic resolution. Sun assumes an admissible weight-\(\pm1/2\)
multiplier on \(\Gamma_0(N_0)\), with nonzero shifted frequencies
\(\widetilde m,\widetilde n\). His same-sign Proskurin formula has
geometric side

\[
 \sum_{c>0}\frac{S(m,n,c,\nu)}c
 \phi\!\left(\frac{4\pi\sqrt{\widetilde m\widetilde n}}c\right)
 =\mathcal U_k+\mathcal W+
 \sum_{\mathfrak a\ \mathrm{singular}}\mathcal E_{\mathfrak a},
\]

so holomorphic, Maaß, and every singular-cusp Eisenstein piece remain.
His uniform partial-sum theorem also prints the exceptional main sum and
an error

\[
 O_{\nu,\varepsilon}\!\left(
 (A_u(m,n)+X_0^{1/6})
 (\widetilde m\widetilde nX_0)^\varepsilon\right),
\]

where \(A_u\) is the paper's level-supported square-part expression
\[
 A_u(m,n)=
 (\widetilde m^{131/294}+u_m)^{1/8}
 (\widetilde n^{131/294}+u_n)^{1/8}
 (\widetilde m\widetilde n)^{3/16},
\]
with \(u_m,u_n\) the source's level-supported square-part parameters
(only \(A_u\ll(\widetilde m\widetilde n)^{1/4}\) in general). The
admissibility input controls modulus windows only when their length is
\(\gg X_0^{2/3}\), not a singleton modulus. In the mixed-sign paper the
trace formula retains Maaß and Eisenstein pieces. Its restricted
frequency theorem has error
\[
 O_{\nu,\varepsilon}\!\left(
 (|\widetilde m\widetilde n|^{143/588}+X_0^{1/6})
 |\widetilde m\widetilde nX_0|^\varepsilon\right)
\]
under its squarefree-or-coprime lifted-frequency hypotheses; the general
version restores the level-supported square-part factors rather than
discarding them.

Andersen--Duke's plus-space Kuznetsov formula retains holomorphic, Maaß,
and Eisenstein pieces. Their Theorem 1.3 assumes positive indices with
the stated signed fundamental-discriminant decompositions and gives a
sum over \(4\mid c\le x\), not one \(c\):
\[
 \sum_{4\mid c\le x}\frac{S_k^+(m,n;c)}c
 \ll \left(x^{1/6}+(dd')^{2/9}(vw)^{1/3}\right)
 (mnx)^\varepsilon.
\]

In (157.SA1), \(j>0\) gives two negative arguments and hence the
same-sign side after conjugation; \(j<0\) gives mixed signs. Since
\(v\ne0\) and \(|j|>V\), all frequencies are now nonzero. The fatal
mismatch is the modulus average and then the coupled matrix, not a
recycled zero-frequency objection. Ahlgren--Andersen's mean values use
the eta multiplier rather than the theta multiplier and also average
moduli, so they do not change this conclusion.

Lam, [*A local large sieve inequality for cusp forms*](https://doi.org/10.5802/jtnb.887),
Theorem 2.3, assumes \(4\mid M_0\), holomorphic half-integral weights in
\(K_0\le k\le K_0+G\), \(k-1/2\) even, and one sequence \(a_n\). It gives

\[
 \sum_k\sum_{f\in B_{k,M_0}}
 \left|\sum_{L_0\le n\le2L_0}a_n\rho_f(n)\right|^2
 \ll (M_0K_0L_0)^\varepsilon(M_0K_0G+L_0)\sum|a_n|^2.
\tag{157.SA27}
\]

Lam's Maaß theorem is integral weight. Equation (157.SA27) is not a
fixed-weight half-integral Maaß-plus-Eisenstein large sieve for an
arbitrary \(j,v\) matrix. The 2026 exceptional-spectrum large sieves of
Pascadi and Blomer--Pascadi are also integral-weight consequences of the
ordinary kernel (157.SA19), not theta-multiplier replacements.

## 3. Proof or derivation

### 3.1 Exact normalization and the only source-legal bound

Apart from the fixed factor \(|1+i|\), the exterior coefficient of one
\(d\)-stratum in (157.SA1) is

\[
 P_d=\frac{d\sqrt c}{2Nq}=\frac{\sqrt d}{4N^{3/2}}.
\tag{157.SA28}
\]

After (157.SA12), its square-root-modulus factor cancels exactly:

\[
 P_dc^{1/2}=\frac{dc}{2Nq}=\frac1{2N}.
\tag{157.SA29}
\]

The accepted Fourier/BV estimates are

\[
 |\widehat B_j(0)|\ll KW X^\varepsilon,
 \qquad
 |\widehat B_j(2dv)|\ll
 W\min\!\left(K,\frac c{|2v|_c}\right)X^\varepsilon,
\tag{157.SA30}
\]

and the complete gcd expansion gives

\[
 \sum_{\substack{v\bmod H\\v\ne0}}
 |\widehat B_j(2dv)|(v^2,j,c)^{1/2}
 \ll WcX^\varepsilon.
\tag{157.SA31}
\]

Equations (157.SA29)--(157.SA31) give \(O(W/d)\) per \(d,j\), hence
\(O(WVX^\varepsilon)\) after every odd \(d\mid N\) and every \(j\).
This proves (157.SA2). The zero row is not included in (157.SA31); its
independently proved \(M^{-1/4}X^\varepsilon\) bound has been subtracted
exactly once in (157.SA7).

### 3.2 Correct signed-incidence target

Let \(\mathcal I_V\) be the selected physical incidences in one block,
and let \(j_n\) be the literal nearest-cell defect attached to \(n\).
The internal unique-\(k\)-per-\(n\) argument together with the applicable
root count gives (157.SA4). Consequently a theorem of the literal form

\[
 \sup_{\substack{I\subset\{n\asymp M\}\\I\ \mathrm{interval}}}
 \left|\sum_{\substack{n\in I,\ n\ \mathrm{odd}\\
 V<|j_n|\le2V}}
 \chi_4(n)e(\sqrt{Nn})\right|
 \ll L(V)^{1/2}X^\varepsilon
\tag{157.SA32}
\]

with the actual signs, cells, transitions, and interval maxima would be
stronger than the raw \(M^{3/4}X^\varepsilon\) discrepancy target:
\(\sqrt{L(V)}\le\sqrt M X^\varepsilon\). After a literal layer-cake or
mixed-variation cost \(W\), it gives (157.SA5). The mixed-variation
reduction itself belongs to the analytical task and is not certified by
this source audit.

None of (157.SA13)--(157.SA27) asserts (157.SA32). In particular, a
large-sieve second moment, an operator norm against rank-one weights, or
the cardinality bound (157.SA4) is not a signed square-root theorem.

### 3.3 Corrected power translation of the closest root theorem

Even before its illegal prime-modulus substitution, Theorem 1.7 of
Dunn--Kerr--Shparlinski--Zaharescu does not have the square-root
\(L(V)^{1/2}\) dependence. Give it the most favorable toy placement:
one \(m\), an ambient \(j\)-interval of length \(V\), a \(1\)-bounded
\(\beta\) supported on \(L=L(V)\) selected points, and a prime
\(p\asymp N\). The two source right sides in (157.SA13) become

\[
 N^{1/8+o(1)}V^{1/8}L^{2/3}
 \left(1+V^{7/48}N^{-1/16}\right)
\tag{157.SA33}
\]

and

\[
 N^{1/8+o(1)}V^{1/16}L^{3/4}
 \left(1+V^{3/16}N^{-1/8}\right).
\tag{157.SA34}
\]

After the literal amplitude \(W\), at the top \(V=K\) and with
\(L\le M\), their worst-case capacities are respectively

\[
 N^{3/16+o(1)}M^{-1/48}
 \left(1+K^{7/48}N^{-1/16}\right),
 \qquad
 N^{5/32+o(1)}M^{1/32}
 \left(1+K^{3/16}N^{-1/8}\right).
\tag{157.SA35}
\]

Neither is target-sized in the frozen \(M\le N^{1/2}\) cone. This is
only a hostile **prime toy-model capacity**: the actual modulus is the
even composite \(4N\), (157.SA8) has two affine right sides and a
\(\chi_4\) sign, and the selected archimedean phase is not the fixed
\(e_p(hx)\) input. Therefore (157.SA35) supplies no legal range.

Under the analogous singleton placement, Shparlinski--Xiao
(157.SA14) retains the term \(Vp^{1/4}(\log p)^{1/2}\), independent of
the sparse support size because its norm is \(\|\beta\|_\infty\). At
\(V=K\), multiplying this term by \(W\) gives

\[
 N^{3/4}M^{-1/4}(\log N)^{1/2},
\tag{157.SA36}
\]

again before the prime/even-composite, separated/coupled, and root-phase
mismatches. For Baier, the substitution \(r=c=4N/d\) already violates
the theorem's odd-squarefree or prime-square hypothesis; the literal
\(v\)-length \(c/2\) also violates \(M_0\le r^{1-\varepsilon}\). Thus
there is no source-legal \(N,M,V,d\) right side to restore from
(157.SA15) or (157.SA16).

### 3.4 Matrix/operator/nuclear-norm translation

Write

\[
 A^{(d)}=(\widehat B_j(2dv))_{j,v},\qquad
 \Theta^{(d)}=(K(-v^2,-j;c))_{j,v}.
\]

Under the standard sesquilinear Frobenius convention, the desired
nonconjugated entrywise sum is
\(\langle\overline{A^{(d)}},\Theta^{(d)}\rangle_F\). A theorem that only bounds
\(\alpha^*\Theta\beta\) controls \(\|\Theta\|_{\mathrm{op}}\), not this
pairing. The valid duality step is

\[
 |\langle\overline A,\Theta\rangle_F|
 \le \|\overline A\|_*\|\Theta\|_{\mathrm{op}}
 =\|A\|_*\|\Theta\|_{\mathrm{op}},
\tag{157.SA37}
\]

where \(\|A\|_*\) is the nuclear norm. Replacing it by the Frobenius
norm is illegal; the generic bound is

\[
 \|A^{(d)}\|_*
 \le \sqrt{\min(V,H)}\,\|A^{(d)}\|_F.
\]

Sampled Parseval and the physical support size \(K\) give the generous
upper capacity

\[
 \|A^{(d)}\|_F^2\le VqKW^2X^\varepsilon,
 \qquad
 \|A^{(d)}\|_*
 \le W\sqrt{\min(V,H)VqK}\,X^\varepsilon.
\tag{157.SA38}
\]

Suppose, purely formally, that an ordinary-Kloosterman operator estimate
\(\|\Theta\|_{\mathrm{op}}\ll c^{1-\delta}\) applied. Restoring (157.SA28)
and \(c=4N/d\), (157.SA37)--(157.SA38) would give one \(d\)-capacity

\[
 WN^{-\delta}d^{-1/2+\delta}
 \sqrt{VK\min(V,N/d)}\,X^\varepsilon.
\tag{157.SA39}
\]

For \(d=1,V=K\le N\), this is

\[
 WN^{-\delta}K^{3/2}=N^{3/4-\delta}X^\varepsilon.
\tag{157.SA40}
\]

Thus the generic nuclear transfer is not target-sized even with
\(\delta=1/32\) from the strongest square-root-length ordinary theorem;
Pascadi's uniform \(\delta=1/700\) is weaker. More importantly,
(157.SA39) is not a legal application at all:

- the actual kernel is theta-multiplier \(K(-v^2,-j;c)\), not ordinary
  \(S(am,n;c)\);
- \(v\mapsto-v^2\) is a folded sparse quadratic image, not a linear
  interval of first arguments;
- the mandatory \(v\)-range has length \(H=c/2\), while (157.SA20)
  requires both lengths \(\ll c^{1/2+o(1)}\), and splitting into
  \(\gg\sqrt c\) blocks loses more than \(c^{-1/700}\) or \(c^{-1/32}\);
- the gcd restrictions exclude mandatory imprimitive strata; and
- (157.SA3) is not separated, while no source bounds its nuclear norm.

For Milićević--Qin--Wu, taking the literal first-index length \(c/2\)
in the most generous linearized model makes
\(M_0^{7/5}N_0<c^{3/2}\) force the other length below \(c^{1/10}\).
This already misses the top \(V=K\), before restoring the \(c^{1/2}\)
normalization in (157.SA23), the quadratic fold, and the theta
multiplier. Consequently none of the 2025--2026 ordinary operator
theorems gives a source-legal strict \(N,M,V,d\) range.

### 3.5 Why modulus-average spectral and dispersion results do not translate

The first geometric mismatch is literal:

\[
 \{c=4N/d\}
 \quad\ne\quad
 \sum_{c\equiv0\ (q_0)}c^{-1}K(m,n;c)g(4\pi\sqrt{|mn|}/c).
\tag{157.SA41}
\]

None of the quoted uniform theorems permits a unit-width delta bump at a
growing \(c\) with constants independent of the bump derivatives. Such
a localization also leaves every spectral term listed in Section 2.5.
Similarly, freezing the outer modulus in (157.SA18) or (157.SA25)
removes the orthogonality that produces the large-sieve right side.
There is therefore no theorem right side whose \(N,M,V,d\) powers can be
legally substituted after freezing: the hypotheses fail before the
power ledger starts.

On a spectral side the frequencies factor as products such as
\(\overline{\rho_\ell(-v^2)}\rho_\ell(-j)\). An SVD of (157.SA3) again
restores exactly the nuclear norm in (157.SA37), while Lam's
one-sequence inequality does not sum the required fixed-weight Maaß,
Eisenstein, holomorphic, residual, and exceptional pieces. Hence a
Kuznetsov placement does not bypass the matrix mismatch.

## 4. First doubtful or unproved step

The first source-unproved step is the signed joint estimate itself. It
may be stated in either of two desired interfaces:

1. a centered fixed-composite root discrepancy of size
   \(O(M^{3/4}X^\varepsilon)\) for (157.SA9), with the literal mixed
   variation; or
2. the stronger selected signed square-root estimate (157.SA32), which
   would close every \(V\) by (157.SA4)--(157.SA5).

The support count (157.SA4) does not prove (157.SA32). On the theta
side, the same first unproved step is a fixed-\(c\) operator or entrywise
matrix theorem for \(K(-v^2,-j;c)\) that accepts
\(A_{j,v}=\widehat B_j(2dv)\), all folds and gcd strata, and has a
target-sized nuclear/structural norm. No audited primary theorem has
this interface.

There is a separate internal seam: this report does not prove that the
literal two-variable Abel/layer-cake decomposition of \(B_j^\circ\),
including its global constant tail, costs only \(WX^\varepsilon\).
That is owned by the analytical task. Even if that seam is green, the
external signed theorem remains absent.

This is a dated source no-match. It is **not** a proof that the centered
discrepancy estimate is false, that no internal argument can prove it,
or that no future theorem can match it. Equations (157.SA2),
(157.SA35), (157.SA36), and (157.SA40) are upper capacities of specified
methods, never signed lower bounds or literature-impossibility claims.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| literal coefficient remains coupled | **PASS / NO MATCH.** Every fixed-modulus 2025--2026 bilinear card uses separated \(\alpha_m\beta_n\). Pascadi's operator-norm formulation still requires the nuclear norm (157.SA37) for the entrywise coefficient (157.SA3). |
| zero row removed exactly once | **PASS.** All theta sums in (157.SA1) have \(v\ne0\); the already proved zero row is represented only by the centering subtraction in (157.SA7). No nonzero theorem is charged for it. |
| fixed modulus not replaced by average | **PASS / NO MATCH.** DFI/Sun/Andersen--Duke Kuznetsov cards and DFI/Fouvry--Iwaniec root cards are recorded as modulus averages and are not delta-specialized. |
| 2026 kernel check | **PASS / NO MATCH.** Pascadi, Blomer--Pascadi, and Milićević--Qin--Wu use ordinary \(S\) or normalized \(\mathrm{Kl}_2\). Shparlinski--Xiao and Baier use prime or odd-squarefree/prime-square root/Salié kernels. All retain separated weights; none is the arbitrary-composite theta kernel with (157.SA3). |
| all divisor strata and normalization | **PASS.** Equations (157.SA28)--(157.SA31) restore \(d\sqrt c/(2Nq)\), \(c=4N/d\), the \(1/(2N)\) cancellation, and the sum over every odd \(d\mid N\). |
| nonzero modes, complements, and folds | **PASS.** The audited object keeps all \(v\bmod c/2\), \(v\ne0\). The quadratic fold \(v\mapsto-v^2\), complementary representatives, and large-\(d\) collisions are explicit mismatches, not discarded rows. |
| signs and endpoints | **PASS.** Positive \(j\) is same-sign after conjugation; negative \(j\) is mixed-sign. Root signs \(j+N,j+3N\), strict blocks, cell/profile transitions, and the centering tail remain literal. |
| external assembly seam | **PASS.** The external \(B_{1,U}(1)\) factor is not folded into a theorem norm or counted as part of (157.SA1). |
| spectral pieces retained | **PASS.** Maaß, holomorphic, Eisenstein/continuous, residual/principal, and exceptional pieces are all retained according to the quoted formula. |
| theorem right sides normalized | **PASS.** DFI's raw \(K\), ordinary raw \(S\), root sums, and Milićević--Qin--Wu's normalized \(\mathrm{Kl}_2=c^{-1/2}S(\cdot,1;c)\) are distinguished; (157.SA24) requires a restored \(c^{1/2}\) for raw \(S\). |
| corrected selected incidence ledger | **PASS.** The current support is \(L(V)\ll\min(M,V)X^\varepsilon\), so a genuine square-root theorem closes all \(V\) as in (157.SA5). The obsolete ambient-only \(V\le M^{3/2}\) capacity is not used. |
| source no-match is not impossibility | **PASS.** Every failure is attached to a printed theorem hypothesis or right side. No downstream exponent or universal impossibility is asserted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

### Repository evidence

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round157_d1_nonzero_theta_matrix_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_centered_seed.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/theta_bilinear_spectral_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_spectral_source_review.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_source_round156_final.md.

The corrected support count (157.SA4) was supplied by the conductor from
the independent selected-block derivation. This report uses it only for
the conditional power translation (157.SA5), not as an external theorem.

### Primary sources

1. W. Duke, J. B. Friedlander, and H. Iwaniec,
   [*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
   IMRN 2012, Theorems 1.1, 1.2, 2.5 and Lemma 6.1; DOI
   [10.1093/imrn/rnr112](https://doi.org/10.1093/imrn/rnr112), and
   [erratum](https://doi.org/10.1093/imrn/rnr240).
2. Alexandru Pascadi,
   [*Non-Abelian Amplification and Bilinear Forms with Kloosterman Sums*](https://link.springer.com/article/10.1007/s00039-026-00746-0),
   Geometric and Functional Analysis, published 21 August 2026,
   Theorems 1.1--1.2 and Proposition 4.10.
3. Valentin Blomer and Alexandru Pascadi,
   [*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/html/2607.24311v1),
   arXiv:2607.24311v1, Theorem 1.1 and the unequal-length results cited
   there.
4. Djordje Milićević, Xinhua Qin, and Xiaosheng Wu,
   [*Bilinear forms with Kloosterman sums and moments of twisted \(L\)-functions*](https://arxiv.org/html/2511.07550v1),
   arXiv:2511.07550v1, Theorem 1.1.
5. Igor E. Shparlinski and Yixiu Xiao,
   [*Shifted bilinear sums of Salié sums and the distribution of modular square roots of shifted primes*](https://arxiv.org/html/2601.10113v1),
   arXiv:2601.10113v1, Theorem 2.5.
6. Stephan Baier,
   [*Partial progress towards the large sieve for square moduli*](https://arxiv.org/html/2605.01635v3),
   arXiv:2605.01635v3, Theorem 6 and Corollary 7.
7. Alexander Dunn, Bryce Kerr, Igor E. Shparlinski, and Alexandru
   Zaharescu,
   [*Bilinear forms in Weyl sums for modular square roots and applications*](https://arxiv.org/html/1908.10143v3),
   Theorem 1.7.
8. Étienne Fouvry and Henryk Iwaniec,
   [*Gaussian primes*](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7935.pdf),
   Acta Arithmetica 79 (1997), Lemma 2.
9. Zihao Liu,
   [*Explicit quadratic large sieve inequality*](https://arxiv.org/abs/2505.09637),
   Acta Arithmetica 223 (2026), Theorem 1.
10. Qihang Sun,
    [same-sign](https://arxiv.org/html/2309.05233v2) and
    [mixed-sign](https://arxiv.org/html/2305.19651v2) uniform
    half-integral Kloosterman papers, especially the trace formulas and
    partial-sum theorems cited in the prior source audit.
11. Nickolas Andersen and William Duke,
    [*Modular invariants for real quadratic fields and Kloosterman sums*](https://arxiv.org/abs/1801.08174),
    Theorems 1.3--1.4.
12. Jonathan W. C. Lam,
    [*A local large sieve inequality for cusp forms*](https://doi.org/10.5802/jtnb.887),
    Theorem 2.3.
13. Scott Ahlgren and Nickolas Andersen,
    [*Kloosterman sums and Maass cusp forms of half integral weight for the modular group*](https://arxiv.org/abs/1510.05191),
    for the eta-multiplier modulus-mean comparison.

## 7. Recommended state effect

Recommend **no proof-state promotion from the literature audit**.
Retain DFI Lemma 6.1 only as the exact pointwise input leading to
(157.SA2), and retain the already proved zero-row removal unchanged.

Record the following as the precise missing external input:

> A fixed-arbitrary-even-composite centered quadratic-root discrepancy,
> or equivalently a theta-multiplier matrix theorem, which keeps the
> literal coefficient \(A_{j,v}=\widehat B_j(2dv)\), all odd divisor
> strata, nonzero folds, gcd strata, signs, and endpoints, and which
> yields either the raw \(M^{3/4}X^\varepsilon\) discrepancy bound or the
> signed square-root estimate (157.SA32).

The corrected incidence count shows that the latter would close every
selected \(V\), but no audited source supplies it. If the conductor must
assign a route label on source evidence alone, use
**outer_defect_centered_discrepancy_no_go only in the qualified sense
“no matching primary theorem through 25 August 2026.”** Do not interpret
that label as a mathematical impossibility or transfer it to any other
owner, M9, the bridge, the quarter theorem, or a global exponent.

**Verdict: cutoff-dated SOURCE NO-MATCH; no source-legal strict range;
not an impossibility theorem.**

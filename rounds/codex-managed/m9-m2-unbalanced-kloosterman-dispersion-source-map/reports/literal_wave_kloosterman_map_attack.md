# Literal prescribed-centre wave versus Kloosterman-fraction machinery

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`

Task: `literal_wave_kloosterman_map_attack`

Role: discovery, owner-repaired after the post-unmask source and completion audits

Starting graph SHA-256: `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## 1. Result

**Scoped `source_level_no_go`, with two exact inverse-phase embeddings, two
distinct exact completion orders, and one exact determinant map.**  Put

\[
 R=\frac{X}{D},\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac{D}{L}=\frac{R}{K},\qquad
 F=\frac{XK}{R}=\frac{XL}{D},                                  \tag{1.1}
\]

and split every real centre as

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor\in\mathbb Z_{>0},
 \qquad 0\leq\xi<1.                                            \tag{1.2}
\]

On one frozen flat smooth packet, the full moving coefficient, including
(e(\xi k/r)), has an exact log-Fourier/Mellin separation with uniformly
bounded projective mass.  All classical source phases may therefore use the
integer frequency (N_0), for every real (X), without changing any source
length, coefficient norm, or exponent.

The loss-minimizing direct Bettin--Chandee/Wright dictionary is

\[
       a=k,\qquad m=1,\qquad n=r,\qquad \vartheta=N_0,
       \qquad \overline 1=1.                                   \tag{1.3}
\]

The separated coefficient contains (e(\xi k/r)), so (1.3) represents the
complete reciprocal packet and not only its coprime part.  It retains
(\chi_4(r)) in the (n)-coefficient, but loses every nontrivial
(m)-average.  Bettin--Chandee Theorem 1 gives the two powers

\[
 E_{\mathrm{BC},1}=\frac{29}{20}+\frac{7\ell}{20}
                    -\frac{13\delta}{10},\qquad
 E_{\mathrm{BC},2}=\frac32+\frac\ell2-\frac{3\delta}{2}.       \tag{1.4}
\]

Both exceed the already proved absolute capacity exponent
(\delta-\ell) by a fixed power throughout the strict flat-UNBAL
polytope.  Wright Theorem 2.1, with the only owner-complete fixed factor
(R_0=1), is worse still: its dominant fifth term has exponent

\[
 E_{\mathrm{W},\mathrm{dir}}
 =\frac{13}{8}+\frac\ell4-\frac{13\delta}{8},
 \qquad
 E_{\mathrm{W},\mathrm{dir}}-(\delta-\ell)>\frac{5}{16}.       \tag{1.5}
\]

There is also a genuinely nonconstant inverse connector, valid for every
real (X) after the same fractional-centre separation:

\[
       a=j^2,\qquad j=m=k,\qquad n=r,
       \qquad a\overline m\equiv k\pmod r                       \tag{1.6}
\]

on ((k,r)=1).  The correlated diagonal (j=m) is not an independent
source tensor.  Its optimal rank-one integral decomposition has projective
cost (asymp1), a sharp factor (K^{1/2}) above the direct (k^{-1})
coefficient norm, and forces (A\asymp K^2).  The resulting
Bettin--Chandee and Wright terms again exceed (\Delta) by fixed powers.

Completion has two different exact meanings, and they must not be
conflated.

- **Smooth-weight first.**  Fourier expansion of the original smooth
  (k)-weight gives Ramanujan sums on the coprime part and an ordinary
  additive delta on the full row.  The exact aggregate is
  (\Delta X^\varepsilon).  This recovers, but does not improve, the
  accepted absolute capacity.
- **Inverse selector first.**  Reindexing by (m=\overline k\pmod r) and
  then Fourier expanding in (m) gives genuine Kloosterman sums with a
  rough, (r)-dependent coefficient matrix.  Parseval plus a uniform
  gcd-sensitive Weil closure costs

  \[
       R\sqrt{R/K}=R\sqrt\Delta
       =X^{1-(\delta+\ell)/2},                                  \tag{1.7}
  \]

  whose exponent exceeds (\delta-\ell) by more than (1/4).  The
  original trivial row bound (R) is smaller than (1.7), so (1.7) is a
  diagnostic of the rough inverse-selector completion, not a best bound for
  the wave.

The physical form does shift to the fixed integral residue

\[
 r\mid s,\quad s=N_0+t
 \qquad\Longleftrightarrow\qquad
 t\equiv-N_0\pmod r,                                           \tag{1.8}
\]

with core localization (|t-\xi|\ll\Delta).  This is nevertheless one
short, coefficient-coupled residue per self-modulus, not Wright's
independent convolution dispersion object; coprimality, range, principal
subtraction, and absolute-value placement also mismatch.

Finally, for each fixed nonzero integer
(\tau=N_0-dr), Bettin--Chandee Corollary 1 has the exact dictionary

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 m_1n_2-m_2n_1=-\tau.                                          \tag{1.9}
\]

Its main term is (O_\varepsilon(X^\varepsilon)) for one (\tau), but
its error is

\[
       X^{3/5+\varepsilon}R^{17/20}.                            \tag{1.10}
\]

The error already has exponent (>41/40).  The corollary treats only one
determinant, so triangulating the (O(\Delta X^\varepsilon)) effective
nonzero levels costs another (\Delta); the assembled main terms merely
return (\Delta X^\varepsilon).  The excluded zero determinant is directly
divisor-bounded.

Thus the supplied Bettin--Chandee and Wright statements neither prove the
(X^{1/4+\varepsilon}) target nor reduce the packet to a smaller
owner-complete survivor.  This is an upper-bound capacity obstruction to
these literal imports, not a lower bound for the signed wave and not a
no-go for a new fixed-centre, coefficient-matrix, sign-preserving theorem.

## 2. Exact statement and hypotheses

Let (X\geq2) be real and

\[
 D=X^\delta,\qquad L=X^\ell,\qquad R=X^{1-\delta},\qquad
 K=X^{1+\ell-2\delta},\qquad \Delta=X^{\delta-\ell},            \tag{2.1}
\]

where

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.                                      \tag{2.2}
\]

Consider only one frozen flat smooth component of

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\asymp R\\ r\text{ odd}}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \sum_{k\asymp K}\frac{q_L(4Xk/r^2)}{k}e(Xk/r),               \tag{2.3}
\]

equivalently

\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\ r\text{ odd}}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(X-s)}{4X}\right).               \tag{2.4}
\]

The normalized supports of (k/K) and (r/R) lie in fixed compact
subsets of ((0,\infty)), and the scaled profiles have uniform fixed-order
smooth seminorms.  All implied constants may depend on these seminorms.
The usual (X^\varepsilon) loss and a constant number of dyadic support
subdivisions are allowed.

The imported statements are Bettin--Chandee,
arXiv:1502.00769v1, Theorem 1 and Corollary 1, and Wright,
arXiv:2604.25177v2, Theorem 2.1, with the hypotheses verified in the
post-unmask source audit.  In particular:

- the trilinear source frequency is the nonzero integer (N_0), not the
  real number (X);
- source coefficient sequences are independent and dyadically supported,
  with only the displayed source coprimality allowed;
- Wright has (M\ll N^2), a fixed denominator factor
  (R_0\ll M^C), and no printed perturbation clause;
- the weaker printed Wright term (A^{-1/20}), rather than the stronger
  term appearing at the end of its proof, is used; and
- Corollary 1 is applied only to a fixed nonzero determinant, with the
  printed smoothness, support, main-term, and error normalizations.

The real centre is always treated by (1.2) and exact absorption of
(e(\xi k/r)) into the smooth coefficient tensor before a source theorem or
completion is invoked.  Direct Bettin--Chandee could equivalently use its
Remark 1 with perturbation (f_{a,N_0}(m,n)=\xi a/n); rational lifting is
neither needed nor used.

> **Proposition (exact source-interface obstruction).**  After the exact
> uniformly bounded real-centre separation just specified, the
> loss-minimizing literal direct independent-tensor specialization of
> (2.3) is (1.3).  Its Bettin--Chandee and Wright bounds exceed
> (\Delta X^\varepsilon) by fixed powers throughout (2.2).  On the
> coprime stratum, the nonconstant connector (1.6) has the sharp
> projective-norm cost (asymp1), source lengths
> ((A,M,N)\asymp(K^2,K,R)), and again exceeds (\Delta).  Smooth-first
> completion exactly returns (\Delta X^\varepsilon); inverse-first
> completion gives the joint Kloosterman matrix and the diagnostic cost
> (1.7).  Formula (2.4) gives the exact fixed residue (1.8), but not the
> independent convolution problem in Wright.  The legal fixed-determinant
> map (1.9) has error (1.10) per nonzero determinant and aggregate main
> terms of size (\Delta X^\varepsilon).  Hence these source statements
> alone imply neither
> (|\mathscr R_{D,L}(X)|\ll X^{1/4+\varepsilon}) nor a strict reduction
> below the accepted flat-wave envelope.

No sharp, clipped, starred, hard, arithmetic-owner, stationary-entry,
transition, remainder, BAL, TOP, complete-UNBAL, M9-M2, M9-M1, M9,
endpoint, or global assertion is included.

## 3. Proof or derivation

### 3.1 Exact separation of the coupled profile and the real centre

Write (k=Ku), (r=Rv), and use (X=N_0+\xi).  On the frozen flat
packet, (u,v) stay in fixed compact subsets of ((0,\infty)), and

\[
 \frac{4Xk}{r^2}=4L\frac{u}{v^2},\qquad
 \frac{X}{rD}=\frac1v,\qquad
 \frac{k}{r}=\frac1\Delta\frac{u}{v}.                           \tag{3.1}
\]

After the standard scaling of (q_L), include (K/k), the cutoff, and the
fractional phase in

\[
 G_{\xi,\Delta}(u,v)
 =G(u,v)e\!\left(\frac{\xi}{\Delta}\frac{u}{v}\right).         \tag{3.2}
\]

Since (0\leq\xi<1) and (\Delta>1), every fixed normalized derivative of
(3.2) is uniformly bounded on the support.  After a buffered extension,
Fourier inversion in ((\log u,\log v)) gives exactly

\[
 G_{\xi,\Delta}(u,v)
 =\iint_{\mathbb R^2}\widehat G_{\xi,\Delta}(t_1,t_2)
   u^{it_1}v^{it_2}\,dt_1dt_2,
 \qquad
 \iint_{\mathbb R^2}|\widehat G_{\xi,\Delta}(t_1,t_2)|
 \,dt_1dt_2\ll1.                                               \tag{3.3}
\]

Thus each fibre has independent direct coefficients with norms

\[
       \|\alpha\|_2\asymp1,\qquad
       \|\nu_k\|_2\asymp K^{-1/2},\qquad
       \|\beta_r\|_2\asymp R^{1/2},                            \tag{3.4}
\]

where (\alpha) is the singleton (m=1) sequence and (\beta_r) contains
(\chi_4(r)).  Integration of a uniform source estimate over (3.3) loses
no power.  In the common source normalization

\[
 C_2=\|\alpha\|_2\|\nu\|_2\|\beta\|_2(AMN)^{1/2},
\]

the literal direct wave has (C_2=R), not (\Delta).  The value
(C_2=\Delta) used elsewhere as an optimistic impossibility screen is not
the literal coefficient normalization.

### 3.2 Direct (m=1) specialization

Take

\[
        A=K,\qquad M\asymp1,\qquad N=R,\qquad
        \vartheta=N_0.                                         \tag{3.5}
\]

Then (a=k,m=1,n=r) supplies (e(N_0k/r)), while (3.2) supplies
(e(\xi k/r)).  The source coprimality is automatic.  Since

\[
 1+\frac{N_0A}{MN}\asymp\frac{XK}{R}=F
 =X^{1+\ell-\delta},                                           \tag{3.6}
\]

Bettin--Chandee Theorem 1 and (3.4) give

\[
 |\mathscr R_{D,L}(X)|
 \ll X^\varepsilon\Delta^{1/2}F^{1/2}
 \left((KR)^{7/20}R^{1/4}+(KR)^{1/2}\right).                  \tag{3.7}
\]

The two exponents are (1.4).  Put (a_0=\delta-\ell).  Direct subtraction
gives

\[
 \begin{aligned}
 E_{\mathrm{BC},1}-a_0
 &=\frac{29}{20}+\frac{27\ell}{20}-\frac{23\delta}{10}
   >\frac3{10},\\
 E_{\mathrm{BC},2}-a_0
 &=\frac32+\frac{3\ell}{2}-\frac{5\delta}{2}
   >\frac14.
 \end{aligned}                                                  \tag{3.8}
\]

For Wright, the varying moduli have no common nontrivial owner-complete
factor, so (R_0=1).  The conditions (M\ll N^2) and
(R_0\ll M^C) hold.  The fifth summand dominates because (R>K>1), and
gives

\[
 R^{11/8}F^{1/4}=X^{E_{\mathrm{W},\mathrm{dir}}},\qquad
 E_{\mathrm{W},\mathrm{dir}}-a_0
 =\frac{13}{8}+\frac{5\ell}{4}-\frac{21\delta}{8}
 >\frac5{16}.                                                   \tag{3.9}
\]

Both calls are legal for every real (X): the source frequency is the
integer (N_0), and all fractional dependence lies in (3.2).  Direct
Bettin--Chandee also admits the equivalent Remark 1 perturbation
(\xi a/n), whose parameter is (Y\asymp K) and whose oscillation factor
is still (F^{1/2}).

A fixed singleton (m=c), with (a=ck), gives the same integral-frequency
phase on ((c,r)=1).  It has no (m)-average, enlarges source lengths by
(c), and requires restoration of rows with ((c,r)>1).  Thus (c=1) is
the loss-minimizing owner-complete member of the constant-(m) family.

### 3.3 The exact (a=m^2) connector and its sharp diagonal cost

On ((k,r)=1), let (\overline k) be an inverse modulo (r).  Then

\[
 k^2\overline k=k+c_{k,r}r,\qquad
 e\!\left(N_0\frac{k^2\overline k}{r}\right)e(\xi k/r)
 =e(Xk/r).                                                       \tag{3.10}
\]

Thus an ordinary fraction can be encoded by a modular inverse: take
(a=j^2), detect (j=m=k), and put (n=r).  The obstruction is not
algebraic; it is the correlated diagonal (a=m^2).

For (a=j^2), use

\[
       \mathbf 1_{j=m}=\int_0^1e(t(j-m))\,dt.                   \tag{3.11}
\]

For each (t), set

\[
 \alpha_m(t)=m^{-1/2}e(-tm),\qquad
 \nu_{j^2}(t)=j^{-1/2}e(tj),\qquad
 \nu_a(t)=0\quad(a\ne j^2).                                  \tag{3.12}
\]

Both source norms in (3.12) are (O(1)), and (3.11) recovers exactly the
factor (1/m).  This projective cost is sharp.  Indeed

\[
 C_{j,m}=m^{-1}\mathbf 1_{j=m}                                 \tag{3.13}
\]

has singular values (m^{-1}), so

\[
 \|C\|_*=\sum_{m\asymp K}m^{-1}\asymp1,
 \qquad
 \sum_\lambda\|\alpha^{(\lambda)}\|_2
                  \|\nu^{(\lambda)}\|_2\geq\|C\|_*\asymp1. \tag{3.14}
\]

The square map (j\mapsto j^2) merely gives a sparse source coefficient,
which the theorems permit.  Compared with
(\|k^{-1}\|_2\asymp K^{-1/2}) in the direct map, the diagonal-rank
inflation is exactly (K^{1/2}).  A detector over all
(a\asymp K^2) that pays an additional (K^{1/2}) is legal but not sharp.

After a constant number of subdivisions of the square image,

\[
          A=K^2,\qquad M=K,\qquad N=R,                           \tag{3.15}
\]

and the oscillation factor is still (F).  Bettin--Chandee gives

\[
 F^{1/2}\left(K^{21/20}R^{11/10}+K^{11/8}R\right),             \tag{3.16}
\]

whose two exponents are

\[
 \begin{aligned}
 E_{\mathrm{BC},\mathrm{sq},1}
 &=\frac{53}{20}+\frac{31\ell}{20}-\frac{37\delta}{10},\\
 E_{\mathrm{BC},\mathrm{sq},2}
 &=\frac{23}{8}+\frac{15\ell}{8}-\frac{17\delta}{4}.
 \end{aligned}                                                  \tag{3.17}
\]

Their excesses over (a_0) satisfy

\[
 \begin{aligned}
 E_{\mathrm{BC},\mathrm{sq},1}-a_0
 &=\frac{53}{20}+\frac{51\ell}{20}-\frac{47\delta}{10}
   >\frac3{10},\\
 E_{\mathrm{BC},\mathrm{sq},2}-a_0
 &=\frac{23}{8}+\frac{23\ell}{8}-\frac{21\delta}{4}
   >\frac14.
 \end{aligned}                                                  \tag{3.18}
\]

Wright's dominant fifth term is

\[
 KR^{11/8}F^{1/4}=X^{21/8+5\ell/4-29\delta/8},                 \tag{3.19}
\]

and its exponent exceeds (a_0) by
(21/8+9\ell/4-37\delta/8>5/16).

The connector covers the coprime stratum.  For the full row, writing
(k=gj,r=gn,(j,n)=1) introduces (g), the factor (1/g), and the moving
profile (q_L(4Xj/(gn^2))W(X/(gnD))).  Neither named trilinear theorem has
this fourth coefficient.  Applying a theorem separately on (g)-pieces
and triangulating cannot improve on its already non-saving (g=1) right
hand side.  This is a certification failure of the stated theorems, not a
lower bound or a denial of cancellation across gcd strata.

### 3.4 Smooth-weight-first completion: Ramanujan and additive return

For a fixed (r\asymp R), put

\[
 b_r(k)=\frac{q_L(4Xk/r^2)}{k}W\!\left(\frac{X}{rD}\right),
 \qquad v_r(k)=b_r(k)e(\xi k/r),                                \tag{3.20}
\]

and extend (v_r) by zero to (\mathbb Z/r\mathbb Z).  Define the
normalized Fourier coefficients

\[
 \gamma_r(h)=\frac1r\sum_{t\bmod r}v_r(t)e(-ht/r),\qquad
 v_r(t)=\sum_{h\bmod r}\gamma_r(h)e(ht/r).                     \tag{3.21}
\]

The support has length (K), its values are (O(K^{-1})), and its scaled
finite differences are uniformly smooth.  Repeated summation by parts gives,
for every fixed (B>0),

\[
 |\gamma_r(h)|\ll_B\frac1r
 \left(1+\frac{\|h-\xi\|_r}{\Delta}\right)^{-B},              \tag{3.22}
\]

where (\|\cdot\|_r) is distance modulo (r).  Consequently

\[
 \sum_{h\bmod r}|\gamma_r(h)|\ll\frac{\Delta}{r}=\frac1K,
 \qquad
 \sum_{h\bmod r}|\gamma_r(h)|^2
 =\frac1r\sum_{t\bmod r}|v_r(t)|^2\ll\frac1{rK}.              \tag{3.23}
\]

On the coprime part, reindexing (t=\overline m) only permutes the reduced
residues.  Therefore the complete inverse-only inner sum is exactly

\[
 \begin{aligned}
 S_r^\times
 &=\sum_{m\bmod r}^{*}v_r(\overline m)e(N_0\overline m/r)\\
 &=\sum_{h\bmod r}\gamma_r(h)
   \sum_{m\bmod r}^{*}e((N_0+h)\overline m/r)\\
 &=\sum_{h\bmod r}\gamma_r(h)\mathfrak c_r(N_0+h).
 \end{aligned}                                                  \tag{3.24}
\]

Here (\mathfrak c_r) is the Ramanujan sum; the inner sum is not a
two-frequency Kloosterman sum.  Choose the signed representative of each
(h\bmod r) near (\xi).  Since

\[
 |\mathfrak c_r(n)|\leq(r,n),\qquad
 \sum_{r\asymp R}\frac{(r,n)}r
 \leq\sum_{d\mid n}\frac{\varphi(d)}d
 \ll_\varepsilon X^\varepsilon,                               \tag{3.25}
\]

(3.22), followed by the (h)-sum, gives

\[
 \sum_{r\asymp R}\left|S_r^\times\right|
 \ll_\varepsilon\Delta X^\varepsilon.                         \tag{3.26}
\]

The full row, including noncoprime (k), is just as direct.  From (3.21),

\[
 \sum_{t\bmod r}v_r(t)e(N_0t/r)
 =\sum_{h\bmod r}\gamma_r(h)
   r\mathbf 1_{r\mid N_0+h}.                                  \tag{3.27}
\]

For each effective signed (h), the number of (r\asymp R) dividing
(N_0+h) is (O_\varepsilon(X^\varepsilon)); the factor (r) cancels
the (r^{-1}) in (3.22), and the weighted (h)-mass is (O(\Delta)).
Thus (3.27) again gives (3.26).  Smooth-weight-first completion is an exact
equal-capacity return.  It neither gives a strict saving nor creates an
independent source tensor, because (\gamma_r(h)) remains joint in
((r,h)).

### 3.5 Inverse-selector-first completion: a rough Kloosterman matrix

On the coprime part, first set

\[
 g_r(m)=
 \begin{cases}
 v_r(\overline m),& (m,r)=1,\\
 0,&(m,r)>1,
 \end{cases}
 \qquad
 \widehat g_r(h)=\frac1r\sum_{m\bmod r}g_r(m)e(-hm/r).         \tag{3.28}
\]

Fourier inversion in the rough variable (m) gives

\[
 S_r^\times
 =\sum_{h\bmod r}\widehat g_r(h)S(N_0,h;r),\qquad
 S(a,b;r)=\sum_{m\bmod r}^{*}e((a\overline m+bm)/r).           \tag{3.29}
\]

Here

\[
 \widehat g_r(h)=\frac1r
 \sum_{\substack{k\asymp K\\(k,r)=1}}
 b_r(k)e(\xi k/r)e(-h\overline k/r),                            \tag{3.30}
\]

so the completed coefficient is itself an incomplete inverse-fraction sum
depending jointly on ((r,h)).  The inverse permutation destroys the
ordinary Fourier smoothness used in (3.22).  Parseval and Cauchy give only

\[
 \sum_h|\widehat g_r(h)|^2\ll\frac1{rK},\qquad
 \sum_h|\widehat g_r(h)|\ll K^{-1/2}.                           \tag{3.31}
\]

This gcd issue can be handled uniformly.  Put (d=(N_0,r)).  Weil's bound
and Cauchy--Schwarz give

\[
 |S_r^\times|
 \ll r^{1/2+\varepsilon}
 \left(\sum_h|\widehat g_r(h)|^2\right)^{1/2}
 \left(\sum_{h\bmod r}(d,h)\right)^{1/2}.                      \tag{3.32}
\]

Because (d\mid r),

\[
 \sum_{h\bmod r}(d,h)
 =\frac rd\sum_{h\bmod d}(d,h)
 \leq r\tau(d).                                                \tag{3.33}
\]

Combining (3.31)--(3.33) yields

\[
 |S_r^\times|\ll_\varepsilon\sqrt{r/K}\,X^\varepsilon
 \asymp\sqrt\Delta\,X^\varepsilon.                           \tag{3.34}
\]

The positive outer (r)-triangle is therefore (1.7), and

\[
 \left(1-\frac{\delta+\ell}{2}\right)-(\delta-\ell)
 =1-\frac{3\delta}{2}+\frac\ell2>\frac14.                      \tag{3.35}
\]

Since the original row has the trivial bound (O(1)), (3.34) is itself
looser than the trivial row estimate when (\Delta>1).  Its value is to
locate the exact failure: inverse-selector-first completion produces a
rough joint matrix, and positive Weil closure cannot recover signed
cross-modulus cancellation.  Treating (\widehat g_r(h)) as an independent
(h)-coefficient would repeat the same coefficient error as the original
sparse inverse image.

For reference, every coprime completion must be restored to the full owner.
The exact gcd decomposition is

\[
 \sum_{\substack{g,n\text{ odd}\\gn\asymp R}}\chi_4(g)\chi_4(n)
 W\!\left(\frac{X}{gnD}\right)
 \sum_{\substack{gj\asymp K\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}e(Xj/n).                            \tag{3.36}
\]

Neither (3.24) nor (3.29) is owner-complete unless these gcd strata are
retained.  The full additive completion (3.27), in contrast, already
includes them.

### 3.6 Physical fixed residue and fixed determinant

Set (s=N_0+t).  Formula (2.4) becomes, up to rapidly decaying tails,

\[
 \sum_{|t-\xi|\ll\Delta X^\varepsilon}
 \sum_{\substack{r\asymp R,\ r\text{ odd}\\
                  t\equiv-N_0\pmod r}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(\xi-t)}{4X}\right).             \tag{3.37}
\]

The residue (-N_0) is fixed and integral.  This exact repair does not make
the expression a Wright convolution-dispersion problem:

1. (t) is one short integer, not a product of two independently weighted
   dyadic variables.
2. The modulus (r) both selects the divisor and appears in the joint
   kernel; there is no second independent modulus average.
3. The residue is not uniformly coprime to (r), and the fixed integer
   (|N_0|\asymp X) is outside the relevant short-convolution residue scale.
4. The coefficient remains joint in ((r,t)), even though its fractional
   centre is perfectly legitimate.
5. Wright's dispersion interface subtracts a reduced-residue principal term
   and places absolute values inside the modulus sum.  The project needs one
   absolute value outside the full (\chi_4(r))-weighted scalar.  Moving it
   rowwise erases the only actual character sign and creates a new principal
   term that still needs control.

There is, however, an exact non-inverse determinant interface.  Fix
(\tau=N_0-dr\ne0) and use

\[
 m_1=d,\qquad n_2=r,\qquad m_2=1,\qquad n_1=N_0,
 \qquad \Delta_{\mathrm{det}}=-\tau.                            \tag{3.38}
\]

Choose smooth selectors for (d\asymp D) and the singleton (m_2=1),
take the (n_1)-coefficient to be a unit mass at (N_0), and put

\[
 \beta_r^{(\tau)}=\chi_4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(\xi+\tau)}{4X}\right).           \tag{3.39}
\]

Then

\[
 (M_1,M_2,N_1,N_2)\asymp(D,1,X,R),\qquad
 \|\alpha\|_2=1,\qquad \|\beta^{(\tau)}\|_2\ll R^{1/2},      \tag{3.40}
\]

and the aspect ratio is (asymp1) because (DR=X).  Corollary 1 gives
the error

\[
 R^{1/2}(XR)^{7/20}X^{1/4}X^\varepsilon
 =X^{3/5+\varepsilon}R^{17/20}.                                \tag{3.41}
\]

Its exponent is

\[
 \frac{29}{20}-\frac{17\delta}{20}>\frac{41}{40}.              \tag{3.42}
\]

For one determinant, the main-term integral has length (O(X)), while the
printed prefactor contributes ((N_0,r)/(N_0r)).  Consequently

\[
 \sum_{r\asymp R}\frac{(N_0,r)}r
 \leq\sum_{g\mid N_0}\frac{\varphi(g)}g
 \ll_\varepsilon X^\varepsilon.                               \tag{3.43}
\]

Thus one main term is (O_\varepsilon(X^\varepsilon)).  The effective
kernel restricts (|\tau+\xi|\ll\Delta X^\varepsilon), and the corollary
contains no signed average over determinant levels.  Triangulating the
main terms returns (\Delta X^\varepsilon), whereas triangulating the
errors appends a factor (\Delta) to (3.41).  The excluded level
(\tau=0) is a single divisor level and is
(O_\varepsilon(X^\varepsilon)).

### 3.7 Full-polytope conclusion

Condition (2.2) implies

\[
             \frac14<a_0=\delta-\ell<\frac12.                  \tag{3.44}
\]

The absolute product capacity is (X^{a_0+\varepsilon}).  The accepted
curvature envelope is strictly smaller only in its curvature-saving region;
there smooth-first completion merely returns the larger absolute capacity.
The direct and square-connector excesses in (3.8), (3.9), (3.18), and
(3.19), and the inverse-first excess (3.35), use only
(\ell\geq0) and (\delta<1/2).  They therefore hold on the entire strict
residual polytope, including (178\ell+1638\delta>463).  The determinant
error (3.42) is much larger still.

Accordingly:

- smooth-weight-first completion reaches exactly (\Delta X^\varepsilon)
  and no lower;
- every literal trilinear source import priced here is larger than
  (\Delta X^\varepsilon) by a fixed power;
- inverse-selector-first positive Kloosterman closure is larger than
  (\Delta X^\varepsilon) by more than (X^{1/4-o(1)}); and
- fixed-determinant main terms return (\Delta X^\varepsilon), while the
  source errors dominate.

None improves the accepted envelope or reaches (X^{1/4+\varepsilon}).

## 4. First doubtful or unproved step

There is no remaining doubtful source normalization, real-centre step, or
completion identity in the scoped no-go.  The first unproved positive step
is a new estimate for one of the following equivalent owner-complete signed
objects:

\[
 \sum_{k\asymp K}\frac1k\sum_{r\asymp R}
 \chi_4(r)G_{\xi,\Delta}(k/K,r/R)e(N_0k/r),                     \tag{4.1}
\]

\[
 \sum_{r\asymp R}\chi_4(r)
 \sum_{h\bmod r}\gamma_r(h)
 r\mathbf 1_{r\mid N_0+h},                                    \tag{4.2}
\]

or the fully gcd-restored version of the Kloosterman matrix
(3.29)--(3.36).  It must keep (\chi_4(r)) before the final scalar absolute
value, retain the joint coefficient family and every gcd stratum, and save
below the accepted envelope uniformly for real (X).  The smooth-first
form (4.2) already has exact absolute capacity (\Delta); the inverse-first
form has only the rough Parseval ledger (3.31).  Neither named source theorem
supplies the needed cross-modulus signed gain.

This report does not prove that these signed objects are large, rule out a
new tailored double-large-sieve or fixed-centre theorem, or control any
omitted endpoint or downstream owner.

## 5. Required control test and outcome

1. **Integral source frequency and real centre -- pass after repair.**
   Every source call uses (N_0\in\mathbb Z).  Equation (3.2) absorbs
   (e(\xi k/r)) into a uniformly smooth tensor, so the direct maps, the
   square connector, and both completion orders are exact for every real
   (X).  The failure is quantitative or coefficient-geometric, not an
   irrational-frequency obstruction.
2. **Direct phase and literal normalization -- pass.**  With (m=1),
   (\overline1=1), and the separated fractional factor, the phase is
   exactly (e(Xk/r)).  The literal source normalization is (C_2=R), not
   the optimistic screen (C_2=\Delta).
3. **Moving-profile separation -- pass.**  Equation (3.3) separates the
   complete flat profile with (O(1)) integrated projective mass.  No
   coupled profile was frozen or deleted.
4. **Nonconstant inverse connector -- pass with capacity failure.**
   Equations (3.10)--(3.14) verify (a=j^2, j=m=k, n=r), detect the
   correlated diagonal, and prove the optimal projective cost (asymp1),
   equivalently the sharp (K^{1/2}) inflation relative to the direct
   coefficient norm.  Equations (3.16)--(3.19) fail the capacity test.
5. **Smooth-weight-first completion -- pass, exact equal-capacity return.**
   The normalized coefficient has size (r^{-1}),
   \(\ell^1\)-mass (O(K^{-1})), and squared \(\ell^2\)-mass
   (O((rK)^{-1})).  The complete inverse-only inner sum is Ramanujan on
   the coprime part; full additive orthogonality includes all gcd rows.
   Both give (\Delta X^\varepsilon).
6. **Inverse-selector-first completion -- pass with capacity failure.**
   It gives the genuine Kloosterman matrix (3.29)--(3.30), not the
   Ramanujan form.  Parseval is (3.31), the gcd-uniform rowwise Weil cost is
   (\sqrt\Delta X^\varepsilon), and the positive outer cost is
   (R\sqrt\Delta X^\varepsilon).  The ordinary row triangle (R) is
   smaller, so this is diagnostic rather than an advertised improvement.
7. **Divisibility, gcd, and fixed residue -- pass.**  Formula (3.36)
   restores every gcd stratum, and (3.37) has the exact fixed residue
   (-N_0).  No bad-gcd rows were discarded and no modulus-dependent or
   nonintegral residue obstruction is claimed.
8. **Physical Wright interface -- fail as a source match.**  The missing
   independent convolution, uniform coprimality, residue range, separated
   kernel, principal subtraction, and compatible absolute-value placement
   are all explicit in Section 3.6.
9. **Character placement -- pass.**  In every legal trilinear map
   (\chi_4(r)) remains in the modulus coefficient until the source norm or
   final positive triangle.  No modulus-by-modulus absolute value is
   substituted for the project's signed outer scalar.
10. **Fixed-determinant source seam -- pass with capacity failure.**  The
    dictionary, supports, nonzero determinant, aspect ratio, coefficient
    norms, main term, error, and determinant triangle in
    (3.38)--(3.43) have all passed the post-unmask primary-source audit.
    The zero determinant is separately divisor-bounded.
11. **Full-polytope and scope controls -- pass.**  The exponent comparisons
    are uniform on the strict flat-UNBAL region.  No endpoint, omitted
    owner, M9-M2, M9-M1, M9, or global claim is changed.

The report allocation was 100% analytical/source-algebraic and 0%
numerical.

## 6. Dependencies and exact artifacts used

The derivation and owner repair used the following repository artifacts as
scoped inputs, without altering shared state:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular
  `M9-M2-smooth-unbalanced-three-quarter-estimate`,
  `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`, and
  `M9-M2-unbalanced-flat-wave-curvature-envelope`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_hb_kpoisson_return.md`;
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/reviews/conductor_round118_square_sector_seam.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/blind_statement.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/source_post_unmask_discovery_formula_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/discovery_post_unmask_blind_completion_audit.md`.

The primary source statements used are Bettin--Chandee
arXiv:1502.00769v1, Theorem 1, Remark 1, and Corollary 1, and Wright
arXiv:2604.25177v2, Theorem 2.1.  Their exact hypotheses and normalizations
were checked in the post-unmask source audit.  The withdrawn
arXiv:2601.00292 was not used.

## 7. Recommended state effect

**Promote after this owner repair** the Section 2 proposition with the
terminal label `source_level_no_go`.  The promoted content is narrowly:

- the exact direct (m=1) and sharp square-supported (a=m^2) encodings
  are legal for all real centres after (N_0+\xi) preprocessing, but the
  supplied trilinear bounds are quantitatively non-saving;
- smooth-weight-first completion is the exact Ramanujan/additive
  equal-capacity return (\Delta X^\varepsilon), whereas
  inverse-selector-first completion is the rough joint Kloosterman matrix
  with diagnostic positive cost (R\sqrt\Delta X^\varepsilon);
- the physical residue is exactly (-N_0), but the remaining Wright
  dispersion interfaces fail; and
- the exact fixed-determinant Corollary 1 map has passed its source seam but
  its errors are far above capacity.

The smallest owner-complete survivor remains the whole flat wave, or an
exact fully gcd-restored completion equivalent to it.  Retain
`M9-M2-smooth-unbalanced-three-quarter-estimate` and every downstream
obligation as open.  No quarter estimate, complete-UNBAL, BAL, TOP, M9-M2,
M9-M1, endpoint, M9, internal global-exponent, or Gauss-circle claim is
changed.

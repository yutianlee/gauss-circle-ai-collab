# Actual-character Fejer-majorant attack

Round 134, discovery report.  The allocation is 100% analytic and 0% numerical.  Throughout, \(e(x)=e^{2\pi i x}\), all sequences are extended by zero before translation, and the scope is only the literal flat-smooth strict-UNBAL owner in the frozen statement.

## 1. Result: an order-optimal bandwidth/zeroth-mode obstruction

**Result (order-optimal trigonometric-majorant no-go).**  Put

\[
 F_H(\alpha)=\left|\sum_{0\leq a<H}e(a\alpha)\right|^2,
 \qquad N=\Delta+1.
\]

For \(0\leq\Delta\leq H-1\), let

\[
 \mu(H,\Delta)=\inf\left\{t_0:T(\alpha)=\sum_{|r|\leq\Delta}t_re(r\alpha)
 \text{ is real and }T\geq F_H\right\}.
\]

Write \(H=qN+s\), \(0\leq s<N\), and set

\[
 \mathsf S_N(H)=(N-s)q^2+s(q+1)^2
 =\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).
\]

Then

\[
 \boxed{\frac{H^2}{\Delta+1}\leq \mathsf S_{\Delta+1}(H)
 \leq \mu(H,\Delta)
 \leq \frac{9\pi^2}{2}\frac{H^2}{\Delta+1}.}
 \tag{1.1}
\]

The lower bound is exact at the two endpoints: \(\mu(H,0)=H^2\) and
\(\mu(H,H-1)=H\).  For every \(\Delta\geq H-1\), in fact
\(\mu(H,\Delta)=H\), attained by \(T=F_H\).  Thus a degree-\(\Delta\)
majorant with \(N\ll H\) has compulsory zeroth-mode and \(L^1\)-excess

\[
 \frac{t_0}{H}\geq \frac{H}{N},
 \qquad
 \int_{\mathbb T}(T-F_H)=t_0-H
 \geq \frac{H^2}{N}-H.
 \tag{1.2}
\]

There is a lawful explicit majorant attaining this order.  With
\(\beta=(2N)^{-1}\),

\[
 T^{\rm 2grid}_{H,N}(\alpha)
 =\frac{9\pi^2}{4}\left(\frac HN\right)^2
 \{F_N(\alpha)+F_N(\alpha+\beta)\}
 \tag{1.3}
\]

has degree \(N-1\), is nonnegative, and pointwise majorizes \(F_H\).
Its zeroth coefficient is

\[
 t_0^{\rm 2grid}=\frac{9\pi^2}{2}\frac{H^2}{N},
 \qquad
 \sum_{|r|<N}|t_r^{\rm 2grid}|\leq \frac{9\pi^2}{2}H^2.
 \tag{1.4}
\]

The exact inequality for the literal family is therefore lawful, but it is
only

\[
 \mathcal E_\chi\leq
 C_H\sum_{|r|<N}t_{-r}
 \sum_{p,q>0\ {\rm odd}}\chi_4(p)\chi_4(q)
 \sum_k b_{p,k+r}\overline{b_{q,k}}.
 \tag{1.5}
\]

This keeps the actual character before every modulus, but it supplies no
estimate of its right side.  A fixed-power bandwidth contraction forces the
factor \(H/N\) in every universal diagonal or positive-row closure.  If
\(N\leq HX^{-\eta}\), this is at least \(X^\eta\), and its \(X\)-capacity is

\[
 X^{1/2+\eta+o(1)}.
 \tag{1.6}
\]

Equivalently, if \(N\leq H^{1-\kappa}\), then the surviving factor and
capacity are

\[
 \Gamma_0=H^\kappa=X^{\kappa(1/2-\delta)+o(1)},
 \qquad
 X^{1/2+\kappa(1/2-\delta)+o(1)}.
 \tag{1.7}
\]

Taking the modulus of the nonzero lags in (1.5) is worse: (1.4) has total
Fourier mass of order \(H^2\), hence the universal one-row ledger returns
the full factor \(H\).  Taking \(N\asymp H\) avoids the power loss but gives
no fixed-power bandwidth contraction; \(N=H\) is exactly the already-known
Fejer multiplier.

This is a no-go for the proposed majorant **as a standalone contraction
mechanism**, not a disproof of the literal estimate.  The literal array may
have cancellation between the enlarged zeroth term and the nonzero signed
lags of (1.5).  Proving precisely that cancellation would be a new
actual-family theorem, not a consequence of one-sided majorization.

**Close label: `majorant_no_go`.**

## 2. Exact statement, hypotheses, order, and capacity table

The hypotheses are exactly those of the blind packet:

\[
 M\asymp X,\quad D=X^\delta,\quad L=X^\ell,\quad
 K=XL/D^2,\quad H=\lceil X^{1/2}/D\rceil,\quad K\asymp LH^2,
\]

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,
\]

and

\[
 Q=\frac{D^2}{L\sqrt X}=X^{2\delta-\ell-1/2}\longrightarrow\infty.
\]

The literal rows are

\[
 b_{p,k}=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p)e(\sqrt{Mpk}),
\]

for positive odd \(p\), with zero extension before every shift, and

\[
 A(k)=\sum_{p>0\ {\rm odd}}\chi_4(p)b_{p,k},\qquad
 \mathcal E_\chi=C_H\sum_n\left|\sum_{0\leq a<H}A(n+a)\right|^2.
\]

The exact relevant order is **pointwise Fourier-multiplier order**
\(T-F_H\geq0\).  For all finitely supported complex sequences, it is
equivalent to the Toeplitz positive-semidefinite order

\[
 C_H\int_{\mathbb T}(T-F_H)|\widehat A|^2\geq0.
 \tag{2.1}
\]

Coefficientwise order of Fourier coefficients or of a physical window is
not this order.

In the table, “zeroth capacity” means the compulsory one-row/delta-sequence
ledger \((t_0/H)\mathcal D_0\); it is a universal-method control, not a
literal lower bound for (134.B1).  “Lagwise capacity” is what remains after
the nonzero signed correlations are put inside moduli.

| Majorant type | Exact direction/order | Fourier support | Zeroth coefficient | Endpoint/error ledger | Capacity consequence |
|---|---|---:|---:|---|---|
| Exact Fejer \(T=F_H\) | Equality of multiplier and quadratic form | \(|r|<H\) | \(H\) | Zero; zero extension is exact | Exactly \(\mathcal E_\chi\); no reduction.  Modulus of its lags has factor \(H\). |
| Any real degree-\(\Delta\), \(T\geq F_H\) | Pointwise multiplier, hence PSD | \(|r|\leq\Delta\) | \(t_0\geq\mathsf S_{\Delta+1}(H)\geq H^2/(\Delta+1)\) | Zero at the multiplier stage | Zeroth-mode factor at least \(H/(\Delta+1)\); fixed-power contraction is above target by that factor. |
| Two-grid Fejer (1.3) | Pointwise multiplier, hence PSD | \(|r|<N=\Delta+1\) | \((9\pi^2/2)H^2/N\) | Zero before any saddle truncation | Order-optimal zeroth factor \(H/N\); lagwise modulus has factor \(H\), since \(\sum|t_r|\ll H^2\). |
| Constant \(T=H^2\) | Pointwise multiplier, hence PSD | \(r=0\) | \(H^2\) | Zero | \(H\mathcal D_0\), i.e. \(X^{1-\delta+o(1)}\) on a target-sized diagonal ledger. |
| Physical coefficientwise \(w_a\geq1_{[0,H)}(a)\) | Only coefficientwise cutoff order | Depends on \(w\) | Not relevant | No valid block-square inequality | Invalid for complex cross terms unless \(w=c(1,\ldots,1)\), \(|c|\geq1\). |
| Rank-one physical block-square majorant | Loewner order \(ww^*\geq vv^*\) | Original block support | \(w=cv\), \(|c|\geq1\) | Zero | No shortening; only a scalar enlargement of the original Fejer form. |
| Exact character \(p\)-Poisson after lawful \(T\) | Equality/invertible reindexing after (1.5) | The same \(|r|<N\) | The same \(t_0\) | Zero in the exact integral formula; all saddle remainders retained | Returns the reciprocal shifted actual-character Gram with the same \(H/N\) zeroth price; no independent power. |

The before/claimed/survivor ledger is

\[
 \Gamma_{\rm before}=\min(H,Q)
 =X^{\min(1/2-\delta,\,2\delta-\ell-1/2)+o(1)},
 \qquad \Gamma_{\rm claimed}=1.
 \tag{2.2}
\]

For \(N\leq HX^{-\eta}\), even the optimistic ledger which grants all
nonzero majorant lags for free leaves

\[
 \Gamma_{\rm majorant}=H/N\geq X^\eta.
 \tag{2.3}
\]

If one is allowed to choose the better of the old coefficient-blind route
and this optimistic diagonal closure, the displayed surviving factor is

\[
 \Gamma_{\rm survivor}^{\rm optimistic}
 :=\min\{H,Q,H/N\}
 \geq X^{\min(1/2-\delta,\,2\delta-\ell-1/2,\,\eta)+o(1)}>1.
 \tag{2.4}
\]

Equation (2.4) is deliberately optimistic: (1.5) itself is still an open
signed actual-character correlation and does not furnish an upper bound
with factor \(H/N\).

## 3. Proof and derivation

### 3.1 Literal block square, Parseval, and the lawful order

Zero extension gives, without a boundary correction,

\[
 \sum_n\left|\sum_{0\leq a<H}A(n+a)\right|^2
 =\int_{\mathbb T}F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
\]

Thus \(T\geq F_H\) pointwise proves (2.1).  Conversely, if (2.1) holds
for every finitely supported \(A\), use translated long Dirichlet kernels
so that their normalized squared moduli form an approximate identity at
an arbitrary \(\alpha_0\).  It follows that
\(T(\alpha_0)-F_H(\alpha_0)\geq0\).
Hence universal PSD domination and pointwise multiplier domination are
equivalent here.  Coefficientwise inequalities between \(t_r\) and
\(H-|r|\) neither imply nor are implied by this pointwise order.

### 3.2 Zeroth-coefficient uncertainty bound

Since \(T\geq F_H\geq0\), \(T\) is a nonnegative trigonometric polynomial
of degree at most \(\Delta\).  Fejer--Riesz factorization gives

\[
 T(\alpha)=\left|\sum_{j=0}^{\Delta}c_je(j\alpha)\right|^2,
 \qquad t_0=\sum_{j=0}^{\Delta}|c_j|^2.
\]

At \(\alpha=0\), Cauchy--Schwarz gives

\[
 H^2=F_H(0)\leq T(0)
 =\left|\sum_{j=0}^{\Delta}c_j\right|^2
 \leq(\Delta+1)t_0.
\]

This proves the lower bound in (1.1).  Integration also gives \(t_0\geq H\),
but for \(N\leq H\) it is already contained in \(t_0\geq H^2/N\).
There is a slightly stronger exact sampling bound.  Since \(T\) has degree
at most \(N-1\), for every \(\theta\)

\[
 t_0=\frac1N\sum_{j=0}^{N-1}T\!\left(\frac{j+\theta}{N}\right).
\]

At \(\theta=0\), pointwise domination and the expansion of \(F_H\) give

\[
 t_0\geq\frac1N\sum_{j=0}^{N-1}F_H(j/N)
 =\#\{(a,b):0\leq a,b<H,\ a\equiv b\pmod N\}
 =\mathsf S_N(H).
 \tag{3.0}
\]

This is the middle lower bound in (1.1); it differs from \(H^2/N\) by at
most \(N/4\) and does not alter the power-capacity obstruction.
Moreover

\[
 \int_{\mathbb T}(T-F_H)=t_0-H,
\]

which proves the exact excess in (1.2).  When \(\Delta=0\), \(T\) is a
constant and \(T\geq F_H\) forces \(t_0\geq H^2\).  When
\(\Delta\geq H-1\), \(T=F_H\) and the integral lower bound give
\(\mu(H,\Delta)=H\).

### 3.3 An order-optimal explicit majorant

Let \(t=\|\alpha\|_{\mathbb T}\), choose a representative in
\([-1/2,1/2]\), and put \(\beta=1/(2N)\).  The numerators of the two Fejer
kernels in (1.3) are complementary:

\[
 \sin^2(\pi N(\alpha+\beta))=\cos^2(\pi N\alpha).
\]

Since both denominators have absolute value at most
\(\pi(t+\beta)\),

\[
 F_N(\alpha)+F_N(\alpha+\beta)
 \geq \frac{1}{\pi^2(t+\beta)^2}.
 \tag{3.1}
\]

For \(t\leq1/N\), the right side is at least
\(4N^2/(9\pi^2)\).  For \(t\geq1/N\), it is at least
\(4/(9\pi^2t^2)\).  On the other hand,

\[
 F_H(\alpha)\leq\min\{H^2,(2t)^{-2}\}.
\]

Multiplication of (3.1) by \((9\pi^2/4)(H/N)^2\) proves (1.3).
Each Fejer kernel has zeroth coefficient \(N\), giving (1.4).  Its
Fourier coefficients are explicitly

\[
 t_r^{\rm 2grid}
 =\frac{9\pi^2}{4}\left(\frac HN\right)^2
 (N-|r|)\{1+e(r/(2N))\},\qquad |r|<N.
 \tag{3.2}
\]

Using \(|1+e(r/(2N))|\leq2\) and
\(\sum_{|r|<N}(N-|r|)=N^2\) proves the last assertion in (1.4).

### 3.4 The exact actual-character finite Fourier survivor

With

\[
 R_r(A)=\sum_k A(k+r)\overline{A(k)},
\]

Fourier inversion gives

\[
 C_H\int_{\mathbb T}T|\widehat A|^2
 =C_H\sum_{|r|\leq\Delta}t_{-r}R_r(A).
\]

Substituting the literal \(A\), without a modulus, proves (1.5).  More
explicitly, its inner correlation is

\[
 \begin{aligned}
 R_r(A)=M^{1/2}\!\sum_{p,q>0\ {\rm odd}}&\chi_4(p)\chi_4(q)(pq)^{-3/4}
 \sum_k ((k+r)k)^{-3/4}\\
 &\times W\!\left(\frac{X}{2D}\sqrt{\frac{p}{M(k+r)}}\right)
 \overline{W\!\left(\frac{X}{2D}\sqrt{\frac{q}{Mk}}\right)}\\
 &\times q_L((X/M)p)\overline{q_L((X/M)q)}
 e\!\left(\sqrt{Mp(k+r)}-\sqrt{Mqk}\right).
 \end{aligned}
 \tag{3.3}
\]

The \(k\)-sum in (3.3) is over the literal intersection on which both
zero-extended profiles are present.  Thus every moving entry and exit is
already included, and no endpoint term has been discarded.

### 3.5 The exact capacity control and what it does not prove

Take a universal one-row control with one nonzero character row and one
nonzero \(k\)-entry.  Then \(A(k)=a\mathbf 1_{k=k_0}\), and

\[
 \mathcal E_\chi=C_HH|a|^2=\mathcal D_0,
 \qquad
 C_H\int T|\widehat A|^2=C_Ht_0|a|^2.
\]

Therefore every universal inference from the majorant to a diagonal or
positive-row ledger has unavoidable ratio

\[
 \frac{t_0}{H}\geq\frac{H}{N}.
 \tag{3.4}
\]

This control respects the block square and zero extension, but it is not
claimed to be an instance of the literal smooth formula for \(b_{p,k}\).
It falsifies a universal majorant inference, not the desired literal
theorem.

It is also essential that (3.4) is **not** a lower bound for the right side
of (1.5) on the literal family.  The terms with \(r\ne0\) can have either
sign and can cancel the \(r=0\) term.  A literal proof is still possible
only if it establishes this actual-family cancellation.  If instead the
lags are put in moduli, (1.4) restores Fourier mass \(H^2\), hence a factor
\(H\) relative to the target diagonal scale.

### 3.6 Why physical Beurling--Selberg or coefficientwise windows do not dominate the complex square

For one physical block let \(v=(1,\ldots,1)\in\mathbb C^H\).  A replacement
window \(w\) gives universal domination only if

\[
 |v^*z|^2\leq|w^*z|^2\quad\hbox{for all }z\in\mathbb C^H,
\]

equivalently \(ww^*-vv^*\succeq0\).  If \(z\perp w\), positivity forces
\(v^*z=0\), so \(v\) is parallel to \(w\).  Consequently

\[
 ww^*-vv^*\succeq0
 \quad\Longleftrightarrow\quad w=cv\text{ with }|c|\geq1.
 \tag{3.5}
\]

There is no support shortening in (3.5).  The elementary phase-adapted
control \(v=(1,1)\), \(w=(1,2)\), \(z=(2,-1)\) has
\(w^*z=0\) but \(v^*z=1\), although \(w\geq v\) coefficientwise.  A sum of
several replacement squares can define a valid frame majorant, but after
translation its exact condition is again a PSD/multiplier majorant and is
subject to (1.1).

### 3.7 Character controls

If two otherwise identical rows lie in opposite \(\chi_4\)-classes, their
contribution to \(A\) and \(\mathcal E_\chi\) is zero, while every separated
positive-row norm is nonzero.  Thus no modulus may be taken before the
\(p\)-sum in (1.5).  Conversely, the abstract multiplier inequality depends
only on the combined sequence \(A\); it is unchanged if \(\chi_4\) is
replaced by \(|\chi_4|\), random signs, or arbitrary phases.  Hence
majorization itself extracts no special cancellation from the true
character.  The true \(\chi_4\) can enter only through a new estimate of
the signed \((p,q,r,k)\)-sum (3.3).

### 3.8 Exact character \(p\)-Poisson and the returned survivor

For fixed positive \(k\), define the zero-extended smooth function

\[
 f_k(x)=x^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac{x}{Mk}}\right)q_L((X/M)x).
\]

Primitive character Poisson modulo \(4\) gives the exact identity

\[
 A(k)=\frac{i}{2}e(-1/8)M^{1/4}k^{-3/4}
 \sum_{u\ {\rm odd}}\chi_4(u)I_u(k),
 \tag{3.6}
\]

where

\[
 I_u(k)=\int_0^\infty f_k(x)
 e\!\left(\sqrt{Mkx}-\frac{ux}{4}\right)\,dx.
 \tag{3.7}
\]

No endpoint has been removed in (3.6)--(3.7).  For \(u>0\), the stationary
point is

\[
 x_*=\frac{4Mk}{u^2},\qquad
 \phi(x_*)=\frac{Mk}{u},\qquad
 \phi''(x_*)=-\frac{u^3}{32Mk}.
\]

The literal stationary principal term is therefore

\[
 I_u(k)=2e(-1/8)(Mk)^{-1/4}
 W\!\left(\frac{X}{Du}\right)
 q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u)
 +\operatorname{Rem}_u(k).
 \tag{3.8}
\]

The Gauss factor, the two \(e(-1/8)\) factors, and the stationary amplitude
cancel exactly in (3.6).  Thus the principal row is

\[
 \mathcal R(k)=\frac1k\sum_{u>0\ {\rm odd}}\chi_4(u)
 W\!\left(\frac{X}{Du}\right)
 q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u),
 \tag{3.9}
\]

with \(u\asymp X/D\) and \(k\asymp K\).  Substitution into the lawfully
majorized form returns the endpoint-complete reciprocal Gram principal
survivor

\[
 \begin{aligned}
 \mathcal Q_{T}^{\rm recip}=C_H\sum_{|r|<N}t_{-r}
 \sum_{u,v>0\ {\rm odd}}&\chi_4(u)\chi_4(v)
 W\!\left(\frac{X}{Du}\right)
 \overline{W\!\left(\frac{X}{Dv}\right)}\\
 \times\sum_k&\frac{q_L(4X(k+r)/u^2)
 \overline{q_L(4Xk/v^2)}}{(k+r)k}
 e\!\left(\frac{M(k+r)}u-\frac{Mk}v\right).
 \end{aligned}
 \tag{3.10}
\]

All terms containing \(\operatorname{Rem}_u\), nonstationary signs, support
entries, exits, and transition pieces form an explicit remainder
\(\mathcal P_T\); it is retained.  In the exact integral form (3.6)--(3.7)
the endpoint error is zero.  Dropping \(\mathcal P_T\) after stationary
phase would require a new ledger weighted by \(t_r\); the old Fejer ledger
cannot automatically be reused because (1.4) may amplify lagwise errors to
Fourier mass \(H^2\).

Even if \(\mathcal P_T\) is granted at zero cost, (3.10) is the original
shifted reciprocal actual-character Gram, with no spare stationary factor
and with the same \(t_0/H\asymp H/N\) zeroth price.  Character Poisson is
therefore an exact return, not a second saving.

## 4. First doubtful or unproved step

The first unproved step is now exact.  After the lawful inequality, one
would have to prove, for some fixed-power \(N\ll H\),

\[
 C_H\sum_{|r|<N}t_{-r}
 \sum_{p,q>0\ {\rm odd}}\chi_4(p)\chi_4(q)
 \sum_k b_{p,k+r}\overline{b_{q,k}}
 \ll_\varepsilon X^{1/2+\varepsilon},
 \tag{4.1}
\]

with every moving profile and zero-extension face retained.  Equivalently,
after exact \(p\)-Poisson, one must prove the same estimate for
\(\mathcal Q_T^{\rm recip}+\mathcal P_T\) in (3.10).

Neither pointwise majorization, Fejer--Riesz, character Poisson, nor a
coefficientwise window estimate proves (4.1).  A positive-row or lagwise
modulus loses the actual character and encounters (3.4), while a
stationary truncation must additionally price \(\mathcal P_T\) with the
inflated Fourier mass.  Possible cancellation of the zeroth term by the
nonzero actual lags is precisely the missing new theorem.  This is why the
coefficient adversaries above are route controls rather than literal
counterexamples.

## 5. Required controls and outcomes

| Control | Outcome | Exact conclusion |
|---|---|---|
| `literal_Echi_block_square_and_parseval` | PASS | Zero extension gives (B2) and (B6) exactly, with no boundary correction. |
| `majorant_order_relation` | PASS / restricted | Pointwise \(T\geq F_H\) is equivalent to universal PSD Toeplitz order.  Coefficientwise order is insufficient. |
| `Fejer_already_bandlimited` | PASS | \(F_H\) has degree \(H-1\), \(t_0=H\), and already gives the exact energy. |
| `zeroth_coefficient_uncertainty_bound` | PASS | \(t_0\geq H^2/(\Delta+1)\), with an order-matching two-grid construction. |
| `bandwidth_and_L1_excess_capacity` | FAILS claimed contraction | \(t_0-H\geq H^2/N-H\); a fixed-power contraction leaves \(H/N\), and lagwise modulus restores factor \(H\). |
| `complex_cross_term_domination` | FAIL for coefficientwise windows | Universal rank-one domination forces \(w=cv\), \(|c|\geq1\); the phase-adapted two-entry control is explicit. |
| `actual_chi4_before_modulus` | PASS in (1.5), (3.3), and (3.10) | Both character factors remain inside the complete signed sum.  Opposite-character identical rows falsify separated positive norms. |
| `moving_profiles_zero_extension_and_endpoints` | PASS at exact Fourier/Poisson level | (3.3), (3.6), and (3.10) retain support intersections, entries, exits, and zero extension. |
| `Poisson_only_after_lawful_one_sided_inequality` | PASS | Poisson is applied only to the right side of (1.5).  It returns (3.10) and supplies no power. |
| `Gamma_before_claimed_survivor` | FAILS claimed \(1\) | \(\Gamma_{\rm before}=\min(H,Q)\), \(\Gamma_{\rm claimed}=1\), while fixed-power bandwidth leaves \(H/N\); the optimistic combined survivor is (2.4). |
| `flat_smooth_owner_and_downstream_scope` | PASS | No hard, sharp, clipped, starred, arithmetic-owner, nonflat, transition, M9, endpoint-assembly, or exponent conclusion is made. |

Additional prescribed controls have the following outcomes.

- One-row coherent/delta sequence: exposes the exact factor \(t_0/H\), but
  is not asserted to be literal (134.B1).
- Two identical rows in opposite \(\chi_4\)-classes: the actual energy
  cancels while separated positive rows do not.
- True \(\chi_4\), \(|\chi_4|\), and random signs: the abstract majorant is
  indifferent to the choice; only the signed correlation can distinguish
  them.
- Phase-adapted complex coefficients: disprove coefficientwise
  physical-window domination.

## 6. Dependencies and exact artifacts used

No external theorem or web source is used.  No numerical or symbolic
experiment is used.  The analytic derivation uses exactly the permitted
artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. `strategy/A2_0823_1.md`;
6. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/blind_statement.md`;
7. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/synthesis.md`;
8. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reviews/conductor_round125_dual_sector_adjudication.md`;
9. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md`;
10. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/briefs/actual_character_fejer_majorant_attack.md`.

The Fejer--Riesz factorization, Cauchy--Schwarz, the two-grid construction,
and character-Poisson normalization are derived explicitly above rather
than imported as black boxes.

## 7. Recommended state effect

**Recommendation: retain the accepted \(\mathcal E_\chi\) survivor and
reject the fixed-power one-sided-majorant mechanism as a standalone route;
record the quantitative obstruction as candidate evidence.**

The promotable mathematical content, subject to seam review, is the
universal extremal law (1.1)--(1.2), the lawful order-optimal construction
(1.3), and the exact actual-character survivors (1.5) and (3.10).  They
show that:

1. degree \(H-1\) with \(t_0=H\) is already the exact Fejer form;
2. degree \(N-1\ll H\) forces zeroth and \(L^1\) price \(H/N\);
3. a modulus before the actual character loses the only cancellation that
   could repay that price; and
4. \(p\)-Poisson returns the reciprocal Gram with no spare factor and with
   a newly weighted endpoint/remainder ledger if it is truncated.

No target bound, strict target-safe smaller survivor, flat-UNBAL theorem,
complete UNBAL theorem, M9-M2 theorem, or Gauss-circle exponent improvement
is proved.

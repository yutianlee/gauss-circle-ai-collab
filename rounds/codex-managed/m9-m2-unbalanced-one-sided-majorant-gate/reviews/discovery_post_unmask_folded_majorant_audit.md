# Post-unmask audit: the exact folded majorant at the literal \(E_\chi\) surface

- Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`
- Round: 134
- Review role: discovery-side post-unmask seam audit
- Allocation: 100% analytic, 0% numerical
- Status: candidate evidence only

## 1. Result

**Verdict: confirm the blind report's sharp finite extremal theorem, with one
important qualification about its use on the literal character family.**
Let \(1\leq N\leq H\), write

\[
 H=mN+s,\qquad m\geq1,\qquad 0\leq s<N,
\]

and put

\[
 P^*_{H,N}(\alpha)=mD_N(\alpha)+D_s(\alpha),\qquad
 T^*_{H,N}(\alpha)=|P^*_{H,N}(\alpha)|^2.
\]

Then the exact minimum zeroth coefficient among all real trigonometric
polynomials of degree at most \(N-1\) which pointwise majorize
\(F_H=|D_H|^2\) is

\[
 \boxed{\mu(H,N-1)=\mathsf S_N(H)
 =(N-s)m^2+s(m+1)^2
 =\frac{H^2}{N}+s\left(1-\frac{s}{N}\right),}
 \tag{1.1}
\]

and \(T^*_{H,N}\) attains it.  The blind pointwise factorization is correct.
An equivalent, manifestly nonnegative form is

\[
 \boxed{
 |1-z|^2\bigl(T^*_{H,N}(\alpha)-F_H(\alpha)\bigr)
 =|1-z^N|^2
 \sum_{a=0}^{m-1}(m-a)|1-z^{s+aN}|^2,
 \quad z=e(\alpha).
 }
 \tag{1.2}
\]

For \(z\ne1\), (1.2) proves the pointwise majorization; at \(z=1\) both
polynomials equal \(H^2\).  In particular, the earlier discovery report's
sampling lower bound is the exact answer, while its two-grid construction is
only an order-sharp, nonextremal comparison.

The exact folded majorant is algebraically stronger than the two-grid
majorant: it gives the least possible zeroth mass and a strict
\(N\)-shift representation.  It is **not** stronger than the already
band-limited Fejer form in target capacity.  Its cost is exactly

\[
 \rho(H,N):=\frac{\mathsf S_N(H)}{H}
 =\frac{H}{N}+\frac{s}{H}\left(1-\frac{s}{N}\right)
 \geq\frac{H}{N}.
 \tag{1.3}
\]

Thus \(N=H\) returns \(T^*=F_H\), while every fixed-power shortening forces
a fixed-power zeroth-mode loss.  Applying finite Fourier inversion or exact
character Poisson after this lawful inequality preserves the same
\(\mathsf S_N(H)\) zeroth coefficient and returns the same shifted
actual-character Gram.  It creates no independent \(X\)-saving.

The qualification is that (1.3) is an exact universal one-row or
positive-row ledger obstruction, not a literal lower bound for
\(E_\chi\).  On the actual family the zeroth term still contains all
signed cross-\(p\) terms, and it can cancel against them and against the
nonzero lags.  That cancellation is possible only through a new
actual-family theorem; it is not supplied by the majorant.

## 2. Exact statement and hypotheses

Use the literal flat-smooth strict-UNBAL data

\[
 M\asymp X,\quad D=X^\delta,\quad L=X^\ell,\quad
 K=\frac{XL}{D^2},\quad
 H=\left\lceil\frac{X^{1/2}}D\right\rceil
 =X^{1/2-\delta+o(1)},
\]

\[
 Q=\frac{D^2}{L\sqrt X}
 =X^{2\delta-\ell-1/2}\longrightarrow\infty,
\]

with the parameter restrictions in the Round-134 brief.  Form the literal
zero-extended rows \(b_{p,k}\) and only then form

\[
 A(k)=\sum_{\substack{p>0\\p\ {\rm odd}}}\chi_4(p)b_{p,k},\qquad
 \mathcal E_\chi
 =C_H\int_{\mathbb T}F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
 \tag{2.1}
\]

For \(1\leq N\leq H\), define

\[
 n_j=\begin{cases}
 m+1,&0\leq j<s,\\
 m,&s\leq j<N.
 \end{cases}
 \qquad
 P^*_{H,N}(\alpha)=\sum_{j=0}^{N-1}n_je(j\alpha).
 \tag{2.2}
\]

The audited conclusions are:

1. \(T^*=|P^*|^2\) has degree at most \(N-1\), satisfies \(T^*\geq F_H\),
   and has zeroth coefficient \(\sum_jn_j^2=\mathsf S_N(H)\).
2. Every real degree-\((N-1)\) majorant \(T\geq F_H\) has
   \(t_0\geq\mathsf S_N(H)\), so (1.1) is exact.
3. The physical inequality is

   \[
   \sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
   \leq
   \sum_n\left|\sum_{j=0}^{N-1}n_jA(n+j)\right|^2.
   \tag{2.3}
   \]

4. Writing \(T^*=\sum_{|r|<N}t_r^*e(r\alpha)\), its coefficients are real
   and nonnegative.  For \(0\leq r<N\),

   \[
   t_r^*
   =m^2(N-r)+m\min(s,N-r)+(m+1)(s-r)_+,
   \tag{2.4}
   \]

   with \(t_{-r}^*=t_r^*\).  Hence

   \[
   t_0^*=\mathsf S_N(H),\qquad
   \sum_{|r|<N}|t_r^*|
   =\sum_{|r|<N}t_r^*
   =T^*(0)=H^2.
   \tag{2.5}
   \]

5. At the literal surface the exact lawful inequality is

   \[
   \mathcal E_\chi\leq
   C_H\sum_{|r|<N}t_{-r}^*
   \sum_{\substack{p,q>0\\p,q\ {\rm odd}}}
   \chi_4(p)\chi_4(q)
   \sum_k b_{p,k+r}\overline{b_{q,k}},
   \tag{2.6}
   \]

   with zero extension imposed before the shifts.  No modulus, profile
   replacement, or endpoint deletion is present in (2.6).

The order in (2.6) is pointwise Fourier-multiplier order, equivalently
universal Toeplitz positive-semidefinite order.  Coefficientwise order on a
physical selector is not sufficient.  A universal single-square physical
replacement has \(ww^*-vv^*\succeq0\) only when \(w=cv\), \(|c|\geq1\);
therefore that placement cannot shorten the Fejer block.

## 3. Proof and derivation

### 3.1 Exact lower bound by sampling

Let \(T(\alpha)=\sum_{|r|<N}t_re(r\alpha)\) and \(T\geq F_H\).  Exact
\(N\)-point quadrature gives

\[
 t_0=\frac1N\sum_{j=0}^{N-1}T(j/N)
 \geq\frac1N\sum_{j=0}^{N-1}|D_H(j/N)|^2.
 \tag{3.1}
\]

At an \(N\)-th root of unity, folding the interval
\(\{0,\ldots,H-1\}\) by residue class modulo \(N\) gives

\[
 D_H(j/N)=\sum_{a=0}^{N-1}n_ae(aj/N).
\]

Finite discrete Parseval therefore yields

\[
 \frac1N\sum_{j=0}^{N-1}|D_H(j/N)|^2
 =\sum_{a=0}^{N-1}n_a^2
 =(N-s)m^2+s(m+1)^2.
 \tag{3.2}
\]

This proves the lower bound in (1.1).  It also shows why an extremizer must
touch \(F_H\) at all \(N\)-th roots.  The folded candidate does:
\(P^*(j/N)=D_H(j/N)\).

### 3.2 Independent audit of the pointwise factorization

Let

\[
 z=e(\alpha),\quad w=z^N,\quad v=z^s,\quad
 A_0=1-w,\quad B_0=1-v,\quad
 G=\sum_{a=0}^{m-1}w^a,
\]

and set

\[
 S_m(\bar w)=\sum_{a=0}^{m-1}(m-a)\bar w^a.
\]

For \(z\ne1\),

\[
 (1-z)P^*=mA_0+B_0,\qquad
 (1-z)D_H=A_0G+w^mB_0.
 \tag{3.3}
\]

Two elementary identities are

\[
 m-\bar w^mG=(1-\bar w)S_m(\bar w)
 \tag{3.4}
\]

and

\[
 2\operatorname{Re}S_m(\bar w)=m+|G|^2.
 \tag{3.5}
\]

Expanding the two squares in (3.3), using (3.4), and then using (3.5)
gives

\[
 \begin{aligned}
 |1-z|^2(T^*-F_H)
 &=|A_0|^2\left(
 m(m+1)-2\operatorname{Re}\{\bar vS_m(\bar w)\}\right)\\
 &=|1-z^N|^2
 \sum_{a=0}^{m-1}(m-a)|1-z^{s+aN}|^2.
 \end{aligned}
 \tag{3.6}
\]

The second line follows from
\(2(1-\operatorname{Re}\zeta)=|1-\zeta|^2\) for \(|\zeta|=1\).
This verifies both the blind algebra and its sign.  It also covers
\(s=0\); when \(N=H\), \(m=1,s=0\), the right side vanishes identically
and \(T^*=F_H\).  Consequently the candidate attains (3.2), proving exact
optimality with no appeal to an unproved extremal theorem.

### 3.3 Fourier coefficients, endpoint completeness, and placement

Equation (2.4) follows directly from

\[
 t_r^*=\sum_{j=0}^{N-1-r}n_{j+r}n_j\qquad(0\leq r<N).
\]

All \(n_j\) are nonnegative, proving (2.5).  Parseval applied to
\(P^*\widehat A\) proves (2.3), and expanding \(A\) only after that step
proves (2.6).  Since every row was zero-extended first, the \(k\)-sum in
(2.6) is automatically the exact moving support intersection for
\(b_{p,k+r}\) and \(b_{q,k}\).  There is no boundary term at this stage.

No alternative placement improves this universal conclusion:

- majorizing each \(p\)-row separately loses the cross-\(p\)
  \(\chi_4\)-correlations;
- coefficientwise physical majorization does not order a complex block
  square;
- a valid rank-one physical Loewner majorant is only a scalar enlargement
  of the original selector;
- applying the multiplier after exact character Poisson merely conjugates
  the same quadratic form into reciprocal variables.

Thus the folded form is the strongest prescribed-bandwidth universal
majorant in zeroth mass, but it has no character sensitivity of its own.

### 3.4 Zeroth, \(L^1\), lagwise, and \(X\)-capacity

The exact excess is

\[
 \int_{\mathbb T}(T^*-F_H)
 =\mathsf S_N(H)-H
 =Nm(m-1)+2ms.
 \tag{3.7}
\]

Relative to the original Fejer zeroth coefficient \(H\), the forced
factor is (1.3).  Therefore:

\[
 N\leq HX^{-\eta}
 \quad\Longrightarrow\quad
 \rho(H,N)\geq X^\eta,
 \tag{3.8}
\]

so a target-sized diagonal ledger \(X^{1/2+o(1)}\) is enlarged to the
displayed capacity

\[
 X^{1/2+\eta+o(1)}.
 \tag{3.9}
\]

Likewise, if \(N\leq H^{1-\kappa}\), then

\[
 \rho(H,N)\geq H^\kappa
 =X^{\kappa(1/2-\delta)+o(1)}.
 \tag{3.10}
\]

If shortening alone is asked to remove

\[
 \Gamma_{\rm before}=\min(H,Q)
 =X^{g+o(1)},\qquad
 g=\min\!\left(\frac12-\delta,\,2\delta-\ell-\frac12\right)>0,
\]

then it requires \(N\leq H/\Gamma_{\rm before}\), and (1.3) gives

\[
 \rho(H,N)\geq\Gamma_{\rm before}=X^{g+o(1)}.
 \tag{3.11}
\]

The lag-count gain and the zeroth-mass loss are therefore the same scale.
If every nonzero lag is put in modulus, (2.5) instead gives the exact
Fourier-mass factor \(H^2/H=H\), with displayed target ledger
\(X^{1-\delta+o(1)}\).

There is an essential literal-family qualification.  The \(r=0\) part of
(2.6) is

\[
 C_H\mathsf S_N(H)\sum_k
 \left|\sum_p\chi_4(p)b_{p,k}\right|^2,
 \tag{3.12}
\]

not
\(\rho(H,N)\mathcal D_0\), where
\(\mathcal D_0=C_HH\sum_{p,k}|b_{p,k}|^2\).  The ratio \(\rho(H,N)\)
is exact for the prescribed one-row impulse control and for a closure
which first replaces the character norm by positive rows.  It is not a
lower bound for (3.12) on the fixed literal array.  Hence (3.8)--(3.11)
rigorously obstruct a universal majorant/diagonal or lag-count-only
argument, but they do not disprove cancellation in (2.6).

### 3.5 Audit of the character-Poisson survivor

For fixed \(k>0\), exact primitive-character Poisson modulo \(4\) gives

\[
 A(k)=\frac{i}{2}e(-1/8)M^{1/4}k^{-3/4}
 \sum_{\substack{u\in\mathbb Z\\u\ {\rm odd}}}\chi_4(u)I_u(k),
 \tag{3.13}
\]

\[
 I_u(k)=\int_0^\infty x^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac{x}{Mk}}\right)
 q_L((X/M)x)
 e\!\left(\sqrt{Mkx}-\frac{ux}{4}\right)\,dx.
 \tag{3.14}
\]

This exact form has no endpoint error.  For \(u>0\), the stationary point,
phase, and curvature are

\[
 x_*=\frac{4Mk}{u^2},\qquad
 \phi(x_*)=\frac{Mk}{u},\qquad
 \phi''(x_*)=-\frac{u^3}{32Mk}.
\]

The principal term is

\[
 2e(-1/8)(Mk)^{-1/4}
 W\!\left(\frac{X}{Du}\right)
 q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\]

The constants do cancel:
\(i\,e(-1/4)=1\).  Thus the principal row is

\[
 \mathcal R(k)=\frac1k
 \sum_{\substack{u>0\\u\ {\rm odd}}}\chi_4(u)
 W\!\left(\frac{X}{Du}\right)
 q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
 \tag{3.15}
\]

Substitution into the sharp folded form gives the principal survivor

\[
 \begin{aligned}
 \mathcal Q_{T^*}^{\rm recip}
 =C_H\sum_{|r|<N}t_{-r}^*
 \sum_{\substack{u,v>0\\u,v\ {\rm odd}}}
 &\chi_4(u)\chi_4(v)
 W\!\left(\frac{X}{Du}\right)
 \overline{W\!\left(\frac{X}{Dv}\right)}\\
 {}\times\sum_k&
 \frac{q_L(4X(k+r)/u^2)\,
 \overline{q_L(4Xk/v^2)}}{(k+r)k}\\
 &\times e\!\left(\frac{M(k+r)}u-\frac{Mk}v\right).
 \end{aligned}
 \tag{3.16}
\]

Here \(u,v\asymp X/D=X^{1-\delta}\),
\(k\asymp K=X^{1+\ell-2\delta}\), and \(|r|<N\).  All stationary
remainders, nonstationary signs, and moving support faces remain in a
separate term \(\mathcal P_{T^*}\); none may be dropped without a new
weighted endpoint estimate.  Equations (2.5) and (3.16) show that Poisson
preserves the zeroth price \(\mathsf S_N(H)\), while a lagwise remainder
closure sees total weight \(H^2\).  The reciprocal transform therefore
returns the same open actual-character Gram and supplies no spare power of
\(X\).

## 4. First doubtful or unproved step

There is no doubtful step in the finite extremal theorem, the factorization
(1.2), the coefficient formula (2.4), or the exact Parseval reduction.

The first unproved step toward the literal target is the estimate

\[
 C_H\sum_{|r|<N}t_{-r}^*
 \sum_{\substack{p,q>0\\p,q\ {\rm odd}}}
 \chi_4(p)\chi_4(q)
 \sum_k b_{p,k+r}\overline{b_{q,k}}
 \ll_\varepsilon X^{1/2+\varepsilon}
 \tag{4.1}
\]

for some fixed-power \(N\ll H\), with every moving profile and
zero-extension face retained.  After character Poisson, the same first gap
is a joint estimate for
\(\mathcal Q_{T^*}^{\rm recip}+\mathcal P_{T^*}\).

In particular, the zeroth term (3.12) may not be replaced by the accepted
separate-row diagonal without a cross-\(p\) estimate, and the nonzero lags
may not be discarded or put in modulus without paying (2.5).  Possible
cancellation of (3.12) against the signed nonzero lags is precisely the
missing actual-family theorem.

## 5. Required controls and outcomes

| Control | Audit outcome | Consequence |
|---|---|---|
| Report byte hygiene | PASS: strict UTF-8; no C0 byte other than permitted line endings, and no orphan carriage return | The discovery report's corrupted `\beta`, `\rm`, and `\theta` tokens were sanitized without changing another artifact. |
| Exact sampling lower bound | PASS: \(N\)-point quadrature plus finite Parseval gives (3.2) | \(\mathsf S_N(H)\) is a necessary zeroth coefficient. |
| Folded pointwise factorization | PASS: independent expansion gives the sum of squares (1.2) | \(T^*\geq F_H\) pointwise and the sampling lower bound is attained. |
| Endpoint cases | PASS: \(N=1\) gives \(T^*=H^2\); \(N=H\) gives \(T^*=F_H\) | The sharp formula interpolates exactly between the constant and Fejer endpoints. |
| Bandwidth and Fourier mass | PASS: degree \(N-1\), \(t_0^*=\mathsf S_N(H)\), \(\sum|t_r^*|=H^2\) | Fixed-power shortening pays \(H/N\); lagwise modulus pays \(H\). |
| Literal \(E_\chi\) and actual character | PASS in (2.6) | Both \(\chi_4\)-factors and all cross-\(p\) terms remain before every modulus. |
| Moving profiles and endpoints | PASS at exact finite-Fourier and exact-Poisson levels | Zero extension supplies the exact intersections; stationary truncation still requires \(\mathcal P_{T^*}\). |
| Majorant placement | PASS as a no-go | Rowwise placement loses character correlations; physical coefficientwise placement is invalid; post-Poisson placement is the same PSD form. |
| \(\Gamma_{\rm before}\) versus claimed \(1\) | FAIL for a lag-count-only proof: (3.11) returns \(\Gamma_{\rm before}\) | The folded optimum does not close the target by itself. |
| Literal-capacity qualification | PASS | \(\rho\) is a universal closure obstruction, not a literal lower bound for \(E_\chi\). |

No numerical, symbolic-computation, or web experiment was used.

## 6. Dependencies and exact artifacts used

This post-unmask audit used:

1. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/briefs/actual_character_fejer_majorant_attack.md`;
2. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/actual_character_fejer_majorant_attack.md`;
3. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/blind_bandlimited_quadratic_majorant_feasibility.md`.

The literal data and capacity parameters are those already frozen in the
brief and carried by the discovery report from its permitted Round-134
context.  The factorization, Fourier coefficients, endpoint cases, and
capacity comparison above were rederived directly.  No shared proof state,
campaign state, synthesis, plan, graph, control file, or external source
was used or edited.

## 7. Recommended state effect

**Promote as candidate finite evidence** the exact equality
\(\mu(H,N-1)=\mathsf S_N(H)\), the folded extremizer
\(T^*=|mD_N+D_s|^2\), the sum-of-squares factorization (1.2), and the
endpoint-complete physical inequality (2.3).

**Revise the mathematical assessment of the discovery construction:** its
sampling lower bound was sharp, but its two-grid majorant should not be
called the strongest construction.  The folded majorant replaces it with
the exact optimum.  No edit to that report beyond the requested byte
sanitation was made in this review task.

**Retain the no-go and keep the literal target open.**  Reject any inference
that prescribed-bandwidth one-sided majorization alone changes
\(\Gamma_{\rm before}\) to \(1\).  Qualify the factor
\(\rho(H,N)\) as a universal diagonal/positive-row or lag-count capacity
obstruction, not as a lower bound for the fixed literal character family.
The first required new result remains (4.1), equivalently the reciprocal
estimate (3.16) together with its complete remainder ledger.  No shared
state change follows from this candidate review alone.

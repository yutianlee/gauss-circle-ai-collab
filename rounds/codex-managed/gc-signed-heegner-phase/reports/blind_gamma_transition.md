# Round228: independent gamma-ratio transition derivation

Campaign: `gc-signed-heegner-phase`  
Task/role: `blind_gamma_transition`, fresh statement-only rederivation  
Generated: 2026-09-27 23:56:20 UTC  
Graph hash: deliberately unavailable; no graph was supplied or accessed.  
Status: bounded analytic report, not an accepted graph claim.

## 1. Result

The ratio has two transition centers, **v = 0 and v = 2t**, corresponding to the two gamma-factor pairs whose imaginary arguments vanish. Each transition is regular: the gamma factors there must be retained exactly. A uniform two-sided modulus envelope holds on the entire real v axis.

Near v = 0, a single large-argument gamma ratio carries the phase. Multiplication by the specified E_R cancels its leading t-logarithmic oscillation and leaves the explicit constant phase below. A quadratic phase is uniformly valid with relative error O_eta(t^-1) for |v| <= t^(1/3), if the low-frequency gamma ratio and the elementary amplitude are retained. It is **not** a uniform relative o(1) approximation on |v| <= t/2. An exact elementary phase restores uniformity on that larger window.

Use the following notation throughout:

\[
 a=\frac{1-\sigma+\delta}{2},\quad
 b=\frac{\sigma+\delta}{2},\quad
 k=a-b=\frac12-\sigma,\quad T=t-\frac v2,
\]
\[
 H(x)=\frac{\Gamma(a+ix)}{\Gamma(b-ix)},\qquad
 G(v)=H(-v/2)=\frac{\Gamma(a-iv/2)}{\Gamma(b+iv/2)}.
\]

The exact factorization, valid for every real v, is

\[
 \boxed{q(v):=Q_\delta(\sigma-it+iv,t)
 =\pi^{2\sigma-1}e^{2i(v-t)\log\pi}G(v)H(T).}
 \tag{1}
\]

For the transition asymptotics define

\[
 c_\delta=\frac{\delta\pi}{2}-\frac\pi4,
 \qquad
 d=\frac{B_2(a)+B_2(b)}2
   =\frac{(\sigma-1/2)^2}{4}-\frac1{48},
\]
\[
 h=\frac{B_3(a)-B_3(b)}6
   =\frac{(\sigma-1/2)\sigma(1-\sigma)}{24}.
 \tag{2}
\]

Here B_2(x) = x^2 - x + 1/6 and B_3(x) = x^3 - 3x^2/2 + x/2. In particular d and h do not depend on delta.

There is an exact logarithmic remainder r(T), defined in Section 3, for which

\[
 H(T)=T^k\exp\{i[2T(\log T-1)+c_\delta]+r(T)\},
\]
\[
 r(T)=-\frac{id}{T}+\frac h{T^2}
       +O_\eta(T^{-3}),\qquad
 \Re r(T)=\frac h{T^2}+O_\eta(T^{-4}),
 \quad
 \Im r(T)=-\frac dT+O_\eta(T^{-3}).
 \tag{3}
\]

All three remainders are symbols: any fixed j derivatives in T improve their indicated bound by T^-j.

Let

\[
 \Psi_t(v)=2t\left[\left(1-\frac v{2t}\right)
           \log\left(1-\frac v{2t}\right)+\frac v{2t}\right].
 \tag{4}
\]

Whenever T > 0, (1) and the definition of r give the exact identity

\[
 \boxed{
 E_R(t)q(v)=e^{ic_\delta}R^{2it}
 \pi^{2\sigma-1}T^kG(v)
 \left(\frac{\pi^2}{t}\right)^{iv}
 e^{i\Psi_t(v)}e^{r(T)}.}
 \tag{5}
\]

For q alone, replace R^(2it) in (5) by

\[
 \exp\{2it[\log(t/\pi)-1]\}.
 \tag{6}
\]

In particular, if g(v) is the continuous argument of G(v) specified below, the leading amplitude and the more precise phase of E_R q are

\[
 \mathcal A(v)=\pi^{2\sigma-1}T^k|G(v)|
       \exp\{h/T^2+O_\eta(T^{-4})\},
\]
\[
 \Theta_R(v)=2t\log R+c_\delta+g(v)
       +v\log(\pi^2/t)+\Psi_t(v)-d/T+O_\eta(T^{-3}).
 \tag{7}
\]

Equations (3), (5), and (7) are uniform for |v| <= t/2. They are also uniform for |v| <= t^(1/3), including 2 <= t < 2 sqrt(2), when the latter window is slightly larger than the former. A common valid domain for these two assertions is |v| <= 2t/3, where T is comparable to t.

On the whole real axis there are constants 0 < C_1(eta) <= C_2(eta) such that

\[
 \boxed{
 C_1\pi^{2\sigma-1}
 \left[(1+|v|/2)(1+|2t-v|/2)\right]^k
 \le |q(v)|=|E_Rq(v)|
 \le C_2\pi^{2\sigma-1}
 \left[(1+|v|/2)(1+|2t-v|/2)\right]^k.}
 \tag{8}
\]

At sigma = 1/2 the modulus is exactly 1, rather than merely bounded by (8).

## 2. Exact hypotheses and conventions

Fix 0 < eta < 1/2. The parameters range over

\[
 \eta\le\sigma\le1-\eta,\quad
 \delta\in\{0,1\},\quad t\ge2,\quad v\in\mathbb R,\quad R>0,
\]

and s = sigma - it + iv. Constants in uniform estimates depend only on eta and the finitely many derivative or expansion orders explicitly indicated. They do not depend on R. Statements about derivatives in t hold with R fixed where R occurs.

Every power of a positive real number uses its real logarithm. The function log Gamma on the right half-plane is the analytic branch that is real on the positive real axis. Since a and b belong to the compact interval [eta/2, 1 - eta/2], all gamma factors used along the specified real v axis are finite and nonzero. Continuous arguments below are obtained from this branch, not from pointwise principal arguments reduced modulo 2 pi.

Specifically,

\[
 \ell_G(v)=\log\Gamma(a-iv/2)-\log\Gamma(b+iv/2),
 \qquad g(v)=\Im\ell_G(v),
\]

so g(0) = 0. The exact small-argument factor G(v) is retained in every transition formula. There is no assumption that v stays away from zero.

This report proves scalar gamma-ratio statements only. There is no arithmetic coefficient, external sum, or conclusion about cancellation in such a sum.

## 3. Proof and derivative control

### 3.1 Exact algebra and large-argument expansion

Substitution of s gives the numerator arguments a + i(t-v/2), a - iv/2 and the denominator arguments b + iv/2, b - i(t-v/2). This proves (1) directly.

We use the following precise form of shifted Stirling. For c in a compact positive real interval, every fixed integer N >= 1, and |z| >= 1 in the closed sector |arg z| <= 3 pi/4,

\[
 \log\Gamma(c+z)
 =(z+c-\tfrac12)\log z-z+\tfrac12\log(2\pi)
 +\sum_{n=1}^{N}
 \frac{(-1)^{n+1}B_{n+1}(c)}{n(n+1)z^n}
 +\mathcal R_{N,c}(z),
 \tag{9}
\]

with, on any slightly smaller closed subsector,

\[
 \partial_z^j\mathcal R_{N,c}(z)
 =O_{N,j,c\text{-compact}}(|z|^{-N-1-j}).
 \tag{10}
\]

This is the ordinary logarithmic Stirling expansion with its sectorial remainder, after expanding log(z+c) in inverse powers of z; the resulting coefficients are the displayed Bernoulli polynomials. Derivative bounds follow from the analytic remainder and Cauchy's estimate on disks of radius proportional to |z| lying within a slightly larger sector. For z = +/- iT the disks of radius T/4 suffice. A bounded initial range of T is absorbed by compactness. Thus (9)-(10) apply uniformly to the a and b here. This explicitly avoids the negative real axis and the gamma poles.

For T > 0 set

\[
 L(T)=\log\Gamma(a+iT)-\log\Gamma(b-iT),
\]
\[
 r(T)=L(T)-k\log T-i[2T(\log T-1)+c_\delta].
 \tag{11}
\]

Using log(iT) = log T + i pi/2 and log(-iT) = log T - i pi/2 in (9) gives

\[
 L(T)=k\log T+i[2T(\log T-1)+c_\delta]
 -\frac{i[B_2(a)+B_2(b)]}{2T}
 +\frac{B_3(a)-B_3(b)}{6T^2}
 +\frac{i[B_4(a)+B_4(b)]}{12T^3}
 +O_\eta(T^{-4}).
 \tag{12}
\]

All derivatives of the last remainder have the symbol bounds (10). The coefficients of the odd inverse powers in this difference are imaginary and those of the even inverse powers are real. Consequently (12) proves every bound in (3), including the improved real-part error. For example, writing

\[
 \varepsilon(T)=r(T)+id/T-h/T^2
\]

gives |epsilon^(j)(T)| <= C_(eta,j) T^(-3-j). The corresponding real-part remainder has bound C_(eta,j) T^(-4-j).

For completeness, put q_0 = sigma - 1/2 and m = delta/2 + 1/4. Then a = m - q_0/2 and b = m + q_0/2. Substitution into B_2 and B_3 yields (2); both choices m = 1/4 and m = 3/4 yield the same d and h. The constant phase is pi(a+b-1)/2 = c_delta, which records the dependence on delta.

### 3.2 The exact elementary phase and its quadratic reduction

The identity

\[
 2T(\log T-1)
 =2t(\log t-1)-v\log t+\Psi_t(v)
 \tag{13}
\]

is algebraic. Combining it with (1), (11), and

\[
 E_R(t)=\exp\{2it[1+\log(\pi R/t)]\}
\]

proves (5)-(7), with no asymptotic manipulation of G.

Uniformly for |v| <= 2t/3, the absolutely convergent series is

\[
 \Psi_t(v)
 =\sum_{n\ge2}\frac{v^n}{n(n-1)2^{n-1}t^{n-1}}
 =\frac{v^2}{4t}+\frac{v^3}{24t^2}
      +O\left(\frac{|v|^4}{t^3}\right).
 \tag{14}
\]

Let D_t(v) = Psi_t(v) - v^2/(4t). The useful derivative statements, valid on the same domain, are

\[
 |\partial_v^j D_t(v)|\le C_j
 \begin{cases}
 |v|^{3-j}/t^2,&0\le j\le2,\\
 t^{1-j},&j\ge3.
 \end{cases}
 \tag{15}
\]

They follow either by the convergent series or from the exact formulas

\[
 \Psi_t'(v)=-\log(1-v/(2t)),\qquad
 \Psi_t^{(j)}(v)=\frac{(j-2)!}{(2t-v)^{j-1}},\quad j\ge2.
 \tag{16}
\]

If S_t(v) = D_t(v) - v^3/(24t^2), the sharper omitted-term bounds are

\[
 |\partial_v^j S_t(v)|\le C_j
 \begin{cases}
 |v|^{4-j}/t^3,&0\le j\le3,\\
 t^{1-j},&j\ge4.
 \end{cases}
 \tag{17}
\]

Define the explicit quadratic approximation

\[
 P_{\rm quad}(v)=e^{ic_\delta}R^{2it}\pi^{2\sigma-1}T^kG(v)
       (\pi^2/t)^{iv}e^{iv^2/(4t)}.
 \tag{18}
\]

Since it is nonzero, the ratio to the exact expression is unambiguous, and it has the specified logarithm

\[
 \frac{E_Rq(v)}{P_{\rm quad}(v)}
 =\exp\{iD_t(v)+r(T)\},
\]
\[
 iD_t(v)+r(T)
 =i\left[\frac{v^3}{24t^2}-\frac dT\right]
       +\frac h{T^2}
       +O_\eta\left(\frac{|v|^4}{t^3}+t^{-3}\right).
 \tag{19}
\]

The derivative bounds for this omitted logarithmic correction are precisely (10), (15), and (17), after the linear substitution T = t - v/2. These are stronger and more informative than asserting derivative bounds for an unspecified relative error after differentiating the oscillatory factors.

On |v| <= t^(1/3), |D_t(v)| <= C |v|^3/t^2 <= C/t, hence

\[
 E_Rq(v)=P_{\rm quad}(v)
 \left[1+O_\eta\left(t^{-1}+\frac{|v|^3}{t^2}\right)\right]
 =P_{\rm quad}(v)[1+O_\eta(t^{-1})].
 \tag{20}
\]

The first omitted phase terms are the cubic v^3/(24t^2) and the Stirling correction -d/T. The first omitted logarithmic modulus term is h/T^2. If both phase terms are retained, the remaining relative error is

\[
 O_\eta\left(t^{-2}+|v|^4/t^3\right),
\]

and if h/T^2 is retained as well, it is O_eta(t^-3 + |v|^4/t^3). These estimates are valid on the small window, where the displayed logarithmic errors are small.

Keeping T^k in (18) matters to the stated O(t^-1) precision. Replacing it by t^k introduces a separate relative error O_eta(|v|/t), which can be O_eta(t^-2/3) on this window. The exact elementary factor can alternatively be written t^k(1-v/(2t))^k; its fixed j-th v derivative after division by t^k is O_(eta,j)(t^-j).

On |v| <= t/2, use the exact Psi_t(v), giving from (3) and (5) a relative O_eta(t^-1) approximation with the leading gamma correction omitted. Its normalized gamma remainder satisfies

\[
 \partial_v^j\{e^{r(t-v/2)}-1\}=O_{\eta,j}(t^{-1-j}).
 \tag{21}
\]

After including exp(-id/T+h/T^2), its normalized relative remainder has derivatives O_(eta,j)(t^-3-j). Any fixed mixed t and v derivatives of those normalized gamma remainders satisfy the corresponding bound with the total derivative order; this follows because T depends linearly on t and v. No such derivative improvement is asserted for the unnormalized oscillatory expression.

The retained exact G also has controlled derivatives. Uniformly on the whole real axis,

\[
 |\ell_G'(v)|\le C_\eta\log(2+|v|),\qquad
 |\ell_G^{(j)}(v)|\le C_{\eta,j}(1+|v|)^{1-j}\quad(j\ge2),
 \tag{22}
\]
\[
 |G^{(j)}(v)|\le C_{\eta,j}|G(v)|
                  [1+\log(2+|v|)]^j.
 \tag{23}
\]

For |v| bounded these follow from analyticity on the compact range of positive real parts, and for |v| large they follow by differentiating (9). Thus the transition factors have not been hidden in an uncontrolled amplitude.

### 3.3 The second transition

The pair G(v) has zero imaginary arguments exactly at v = 0. The pair H(t-v/2) does so exactly at v = 2t. Their small-argument zones have bounded width in v. There are no poles or further small-imaginary-argument centers on the stated real line.

For u = v - 2t and T_+ = t + u/2, direct factorization gives

\[
 q(2t+u)=\pi^{2\sigma-1}e^{2i(t+u)\log\pi}
                G(u)H(-T_+).
 \tag{24}
\]

Because H(-x) is the complex conjugate of H(x), the second transition is uniform by the same expansion. Its amplitude and phase for |u| <= 2t/3 are

\[
 \pi^{2\sigma-1}T_+^k|G(u)|
       \exp\{h/T_+^2+O_\eta(T_+^{-4})\},
\]
\[
 2(t+u)\log\pi+g(u)-2T_+(\log T_+-1)-c_\delta
              +d/T_++O_\eta(T_+^{-3}).
 \tag{25}
\]

Multiplying by E_R adds its exact phase to (25). Equivalently, the exact conjugation relation in Section 5 transfers every expansion at zero to this center, including all derivative estimates. In particular there is no need to approximate G(u) at u = 0.

### 3.4 Global modulus envelope

For c in [eta/2, 1-eta/2], Stirling for |y| >= 1 and compactness for |y| <= 1 prove

\[
 |\Gamma(c+iy)|\asymp_\eta
        (1+|y|)^{c-1/2}e^{-\pi|y|/2}.
 \tag{26}
\]

Both inequalities are uniform because gamma has neither zeros nor poles on the compact small-y set. In the quotient H(y), the exponential factors cancel exactly in the envelope, and (26) gives

\[
 |H(y)|\asymp_\eta(1+|y|)^k.
\]

Apply this twice to (1); the exponential prefactor has modulus 1. This proves (8). E_R also has modulus 1 for positive real R, so it has precisely the same envelope. For orientation, the envelope has scale t^k at either transition, t^(2k) when both |v| and |2t-v| are comparable to t, and |v|^(2k) when |v| is much larger than t. These are scalar sizes, with no implication for any sum.

## 4. First gap or unsupported extension

There is no unresolved step in the scalar results above, conditional only on the explicitly permitted sectorial Stirling formula (9)-(10). No theorem about an external quantity is being asserted.

The first false extension would be to use the quadratic phase with a uniform relative o(1) error on the entire window |v| <= t/2. Indeed at v = t/2,

\[
 D_t(t/2)=Ct,\qquad
 C=\sum_{n\ge3}\frac{(1/2)^n}{n(n-1)2^{n-1}}>0.
 \tag{27}
\]

The constant is strictly positive by its convergent positive series. Along t_n = (2n+1)pi/C, the ratio in (19) tends to -1, since r(3t_n/4) tends to zero. Its relative difference from 1 therefore tends to 2. This is a proof of failure, not a numerical diagnosis. The exact phase (4) is the remedy within the already stated scalar problem.

A second invalid extension is to apply large-argument Stirling to G(v) uniformly through v = 0. For k != 0, its putative leading modulus (|v|/2)^k would tend to zero or infinity, whereas G(0) = Gamma(a)/Gamma(b) is positive, finite, and nonzero. The exact factor resolves that obstruction. At sigma = 1/2 the modulus obstruction disappears, but it still does not justify a large-argument phase expansion at zero.

Finally, a phase factorization does not establish cancellation or smallness of any external sum. Such an implication would require additional hypotheses and proof absent from this task.

## 5. Required controls and outcomes

All controls in this section are exact or analytic. No numerical or symbolic experiment was run.

**Critical-line modulus.** At sigma = 1/2 one has a = b. Therefore H(x) = Gamma(a+ix)/overline{Gamma(a+ix)} and similarly G(v) has modulus 1. The pi amplitude is 1. Thus

\[
 |q(v)|=|E_Rq(v)|=1
\]

for every real v, exactly. In (2), h = 0, in agreement with this identity. **Outcome: passes.**

**Meromorphic inversion and conjugation.** For real t, inspection of the defining ratio gives

\[
 Q_\delta(s,t)Q_\delta(1-s,t)=1,
 \qquad Q_\delta(\bar s,t)=\overline{Q_\delta(s,t)},
 \qquad Q_\delta(s,-t)=Q_\delta(s,t).
 \tag{28}
\]

The first is a meromorphic identity, interpreted away from zeros and poles as an ordinary product. On the critical line 1-s = conjugate(s), hence it implies the exact modulus again. In v coordinates, retaining sigma in the notation where needed,

\[
 q_\sigma(2t-v)=\overline{q_\sigma(v)},\qquad
 q_\sigma(v)q_{1-\sigma}(2t-v)=1,
 \qquad q_{1-\sigma}(v)=\frac1{\overline{q_\sigma(v)}}.
 \tag{29}
\]

At sigma = 1/2 these specialize to q(2t-v) = conjugate(q(v)) = 1/q(v), and q(t) = 1. The general q_sigma(t) is positive real, as can also be seen directly from its products of conjugate gamma factors. **Outcome: passes.**

The E_R multiplier must be tracked when testing symmetries. If p_sigma(v) = E_R q_sigma(v), then

\[
 p_\sigma(2t-v)=E_R^2\overline{p_\sigma(v)},\qquad
 p_\sigma(v)p_{1-\sigma}(2t-v)=E_R^2.
 \tag{30}
\]

Thus a bare reflected-v inversion for p would generally be false. On the critical line 1/p(v) = conjugate(p(v)) still holds pointwise because its modulus is 1. Also p(t) = E_R there. **Outcome: passes with the multiplier correctly retained.**

**Direct zero-center control.** At v = 0, direct substitution, with no approximation to the small factors, gives

\[
 q(0)=\pi^{2\sigma-1}\frac{\Gamma(a)}{\Gamma(b)}
                 e^{-2it\log\pi}\frac{\Gamma(a+it)}{\Gamma(b-it)}.
 \tag{31}
\]

Consequently its size is

\[
 |q(0)|=\pi^{2\sigma-1}\frac{\Gamma(a)}{\Gamma(b)}t^k
                 \exp\{h/t^2+O_\eta(t^{-4})\},
 \tag{32}
\]

and its continuous phase is

\[
 2t[\log(t/\pi)-1]+c_\delta-d/t+O_\eta(t^{-3}).
 \tag{33}
\]

For E_R q(0), (33) becomes

\[
 2t\log R+c_\delta-d/t+O_\eta(t^{-3}).
 \tag{34}
\]

Equations (32)-(34) agree exactly with (7) at v = 0, since Psi_t(0) = g(0) = 0. On sigma = 1/2 the leading amplitude equals 1 and d = -1/48, so the phase in (34) is

\[
 2t\log R+c_\delta+1/(48t)+O(t^{-3}),
\]

with c_0 = -pi/4 and c_1 = pi/4. The modulus is exactly 1 even before expansion. **Outcome: passes.**

**Second center and global envelope.** Formula (29) gives q(2t) = conjugate(q(0)), matching (24)-(25); (8) gives the same transition scale at both endpoints. The center v = t has both large imaginary arguments and satisfies the positive-real control above. **Outcome: passes.**

**Large-window falsification control.** The explicit sequence following (27) refutes the uniform quadratic-only approximation on |v| <= t/2, while retaining Psi_t gives the uniform symbol bounds. **Outcome: quadratic-only extension fails as required; exact-phase formulation passes.**

## 6. Dependencies and exact isolation disclosure

The only pre-existing files read were:

1. `protocol.md`.
2. `rounds/codex-managed/gc-signed-heegner-phase/briefs/blind_gamma_transition_statement.md`.

No graph, campaign manifest, history, generated sibling brief, claimant report, strategy, source card, root control, or sibling report was read. No literature lookup was made. No computational experiment was performed. The supplied statement and the two permitted files comprise the complete task context used; the graph hash is intentionally unknown.

Mathematical inputs are the supplied definition, elementary complex conjugation of gamma, positivity and absence of poles or zeros for gamma on the positive real axis/right-half-plane lines used here, and the permitted logarithmic Stirling formula with the remainder and sectors explicitly recorded in (9)-(10). The asymptotic deductions and all tests are derived in this report. No arithmetic application is present.

The sole written artifact is this report at the task-assigned path. Its SHA256 is to be returned to the conductor after writing, externally to the report to avoid a self-referential hash. This task does not edit any authoritative state or synthesis artifact and does not select subsequent work.

## 7. Recommended state effect

**No direct state change by this role.** Retain this report as independent evidence for the exact factorization, both transition centers, the global modulus envelope, and the qualified small-window asymptotics. Reject any proposed uniform quadratic-only relative o(1) extension to |v| <= t/2, or any use of these scalar formulas alone to infer an external cancellation bound.

Any promotion is the conductor's decision after the required matching, seam checks, source requirements where applicable, and graph validation. The present report neither claims that those gates have been completed nor carries a result into a later round.

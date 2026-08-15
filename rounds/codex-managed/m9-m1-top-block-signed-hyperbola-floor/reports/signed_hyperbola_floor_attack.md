# Round 58 discovery report: exact hyperbola-floor expansion and its surviving signed core

## 1. Result: target-safe endpoint Fourierization, but no square-root proof

Let

\[
 \mathcal I_R=\{h\in\mathbb Z:R/4<h\leq R/2\},\qquad
 \ell=B-A+1\leq R,
\]

and absorb only the inherited independent radial star into the actual
angular amplitude:

\[
 \widetilde{\mathcal A}_X(h,q)
 :=\omega_{\rm rad}(hq)\mathcal A_X(h,q).
\]

Thus artificial membership in \([A,B]\) is still a full cutoff.  Put

\[
 L_h={A+h-1\over2h},\qquad U_h={B+h\over2h},\qquad
 m_h=\lfloor L_h\rfloor,
\]

\[
 q_h=2m_h+1,\qquad
 \nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor\in\{0,1,2\}.
\tag{1.1}
\]

With

\[
 I_1(v)={v(3-v)\over2},\qquad I_2(v)={v(v-1)\over2},
 \qquad \varepsilon(t)=(-1)^{\lfloor t\rfloor},
\tag{1.2}
\]

the complete starred high-shell sum has the exact floor representation

\[
\boxed{
 P_J=\sum_{h\in\mathcal I_R}\varepsilon(L_h)
 \left\{I_1(\nu_h)F_h(q_h)-I_2(\nu_h)F_h(q_h+2)\right\},}
\tag{1.3}
\]

where

\[
 F_h(q)=\widetilde{\mathcal A}_X(h,q)e(\sqrt{Xhq}).
\]

Formula (1.3) includes empty, singleton, and adjacent-pair rows without
adding a half weight at either artificial window endpoint.

There is also an exact finite Vaaler--Fejer decomposition.  For every
integer Fourier height \(T\geq1\), a finite trigonometric expression
\(P_{J,T}^{\sharp}\), defined in Section 2, satisfies

\[
 \boxed{P_J=P_{J,T}^{\sharp}+\mathcal R_{J,T},\qquad
 |\mathcal R_{J,T}|
 \ll_\epsilon X^\epsilon\left({R\over T}+1\right).}
\tag{1.4}
\]

Consequently \(T=\lceil\sqrt R\rceil\) makes the entire endpoint and
integer-jump residual target-sized.  The odd-character factor has exactly
zero Fourier mean, while the count selector has the indispensable zero
mode \(\ell/(2h)\).  No endpoint term is lost.

The nonzero finite core does not, however, become a smooth long
one-variable sum.  Every term retains

\[
 q_h=2\left\lfloor{A+h-1\over2h}\right\rfloor+1
\]

inside both the actual amplitude and the radial phase.  A branch with
fixed \(q_h\) contains only \(O(1)\) possible \(h\)'s, and actual fixed-
\(q\) product fibres contain at most one point.  Thus branchwise derivative
estimates and termwise Fourier absolute values retain \(R\) capacity.
The Round-57 strict fourth-power family continues to realize that capacity.

This is a sharp scoped no-go, not a signed counterexample.  The endpoint
Fourier residual is harmless; the first surviving theorem is a genuinely
signed cross-\(h\) estimate for the exact floor-radial core.  No such
estimate, and hence no new exponent, is proved here.

## 2. Exact statement and hypotheses

Assume \(Y=R^2\asymp\sqrt X\),
\([A,B]\cap\mathbb Z\subset[cY,CY]\), and \(1\leq\ell\leq R\).  The
amplitude \(\widetilde{\mathcal A}_X\) is the exact actual top-block
amplitude: all height floors, angular profiles, the one-sided hard top,
angular equality stars, and the independent radial star are retained.  It
is uniformly bounded.  Only \(h\in\mathcal I_R\) is owned.

Use the floor-compatible sawtooth

\[
 \psi_F(t)=t-\lfloor t\rfloor-\frac12,\qquad \psi_F(n)=-\frac12.
\tag{2.1}
\]

Then (1.1) is equivalently

\[
 m_h=L_h-\psi_F(L_h)-\frac12,
\]

\[
 \boxed{\nu_h={\ell\over2h}+\psi_F(L_h)-\psi_F(U_h),}
\tag{2.2}
\]

and the exact parity square wave is

\[
 \boxed{\varepsilon(t)
 =2\left\{\psi_F\left({t+1\over2}\right)
             -\psi_F\left({t\over2}\right)\right\}.}
\tag{2.3}
\]

For \(0<u<1\), let

\[
 \Phi_V(u)=\pi u(1-u)\cot(\pi u)+u,
\]

and define the audited finite Vaaler polynomial and Fejer kernel by

\[
 V_T(t)=\sum_{0<|r|\leq T}v_{r,T}e(rt),\qquad
 v_{r,T}=-{\Phi_V(|r|/(T+1))\over2\pi i r},
\tag{2.4}
\]

\[
 K_T(t)=\sum_{|r|\leq T}\left(1-{|r|\over T+1}\right)e(rt)
 ={1\over T+1}
 \left({\sin\pi(T+1)t\over\sin\pi t}\right)^2,
\]

\[
 \kappa_T(t)={K_T(t)\over2T+2},\qquad
 \rho_T(t)=\psi_F(t)-V_T(t).
\tag{2.5}
\]

The floor-compatible conclusion, including integers, is

\[
 |\rho_T(t)|\leq\kappa_T(t).
\tag{2.6}
\]

In particular, at an integer \(n\), \(V_T(n)=0\),
\(\rho_T(n)=-1/2\), and \(\kappa_T(n)=1/2\); the endpoint jump is not
silently replaced by its midpoint.

Define

\[
 \lambda_h={\ell\over2h},\qquad
 M_{h,T}=\lambda_h+V_T(L_h)-V_T(U_h),
\tag{2.7}
\]

\[
 E_{h,T}=2\left\{V_T\left({L_h+1\over2}\right)
                    -V_T\left({L_h\over2}\right)\right\}.
\tag{2.8}
\]

The finite main term in (1.4) is

\[
\boxed{
 P_{J,T}^{\sharp}
 =\sum_{h\in\mathcal I_R}E_{h,T}
 \left\{I_1(M_{h,T})F_h(q_h)
       -I_2(M_{h,T})F_h(q_h+2)\right\}.}
\tag{2.9}
\]

For an exact remainder identity, put

\[
 \eta_{h,T}=\rho_T(L_h)-\rho_T(U_h),
\]

\[
 \zeta_{h,T}=2\left\{\rho_T\left({L_h+1\over2}\right)
                         -\rho_T\left({L_h\over2}\right)\right\}.
\tag{2.10}
\]

Since \(\nu_h=M_{h,T}+\eta_{h,T}\) and
\(\varepsilon(L_h)=E_{h,T}+\zeta_{h,T}\), one has

\[
\begin{split}
 \mathcal R_{J,T}=\sum_{h\in\mathcal I_R}\bigg[&
 \zeta_{h,T}
 \{I_1(\nu_h)F_h(q_h)-I_2(\nu_h)F_h(q_h+2)\}\\
 &+E_{h,T}\{[I_1(\nu_h)-I_1(M_{h,T})]F_h(q_h)\\
 &\hspace{54mm}-[I_2(\nu_h)-I_2(M_{h,T})]F_h(q_h+2)\}\bigg].
\tag{2.11}
\end{split}
\]

Equations (2.9)--(2.11) are an exact finite Fourier/sawtooth identity,
not an asymptotic replacement.

## 3. Proof and derivation

### 3.1 Exact odd-lattice geometry

The first odd integer \(q\) satisfying \(hq\geq A\) is

\[
 q_h=2\left\lfloor{A+h-1\over2h}\right\rfloor+1.
\tag{3.1}
\]

The last odd integer satisfying \(hq\leq B\) is

\[
 2\left\lfloor{B+h\over2h}\right\rfloor-1.
\]

Their odd-lattice count is therefore

\[
 \nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor.
\]

Because three odd integers span product length \(4h>R\geq\ell\), this
count is \(0,1\), or \(2\).  The polynomials in (1.2) satisfy

\[
 (I_1(v),I_2(v))=(0,0),(1,0),(1,1)\qquad(v=0,1,2).
\]

Moreover

\[
 \chi_4(q_h)=\chi_4(2m_h+1)=(-1)^{m_h},\qquad
 \chi_4(q_h+2)=-\chi_4(q_h).
\]

These facts prove (1.3).  Substitution of
\(\lfloor t\rfloor=t-\psi_F(t)-1/2\) proves (2.2).  Directly checking
the two half-intervals in each period, including their integer left
endpoints, proves (2.3).

For a point window \(A=B=N\), (1.1) gives

\[
 \nu_h=1\quad\Longleftrightarrow\quad
 h\mid N,\qquad N/h\ {\rm odd}.
\tag{3.2}
\]

In that case \(q_h=N/h\) and \(I_2(\nu_h)=0\).  Thus (1.3) reproduces
the exact signed divisor incidence and does not manufacture an adjacent
partner.

### 3.2 Character projector and both zero-mode ledgers

On all integers, including even ones,

\[
 \boxed{\chi_4(q)={e(q/4)-e(3q/4)\over2i}.}
\tag{3.3}
\]

Hence the character itself has only the two nonzero modes
\(1/4\) and \(-1/4\), and its zero Fourier coefficient is exactly zero.
The same statement is visible in (2.3): the square wave
\(\varepsilon\) has zero mean over its period two.

There is nevertheless a nonzero selector zero mode.  Equation (2.2)
shows that it is exactly

\[
 \lambda_h={\ell\over2h}.
\tag{3.4}
\]

It is order one on the high shell and may not be discarded.  It enters
both \(I_1(M_{h,T})\) and \(I_2(M_{h,T})\).

There is also no hidden boundary zero mode in summation by parts.  If

\[
 C(N)=\sum_{1\leq q\leq N}\chi_4(q)
 ={1\over2}+{1\over2}\sin{\pi N\over2}
              -{1\over2}\cos{\pi N\over2},
\tag{3.5}
\]

then for any sequence \(G(q)\),

\[
\begin{split}
 \sum_{q=a}^{b}\chi_4(q)G(q)
 ={}&C(b)G(b)-C(a-1)G(a)\\
 &+\sum_{q=a}^{b-1}C(q)\{G(q)-G(q+1)\}.
\tag{3.6}
\end{split}
\]

The contribution of the constant \(1/2\) in (3.5) is

\[
 {G(b)-G(a)\over2}
 +{1\over2}\sum_{q=a}^{b-1}\{G(q)-G(q+1)\}=0.
\]

Thus the true odd-character zero mode cancels with its two full boundary
owners, whereas the geometric count mode (3.4) remains.

### 3.3 Fejer residual summed over the hyperbola

The elementary kernel bound is

\[
 \kappa_T(t)\ll
 \min\left(1,{1\over T^2\|t\|^2}\right).
\tag{3.7}
\]

Each of the four endpoint arguments in (2.10) has the form

\[
 t_h={N+ch\over dh},
\tag{3.8}
\]

where \(d\in\{2,4\}\), \(c\) is fixed, and
\(N\in\{A-1,B\}\asymp R^2\).  For \(0<\delta\leq1/2\), if
\(\|t_h\|\leq\delta\), then for some integer \(k\),

\[
 |N-(dk-c)h|\ll\delta R.
\]

For each integer error \(s=N-(dk-c)h\) with
\(|s|\ll\delta R\), the integer \(h\) divides \(N-s\).  The elementary
divisor bound therefore gives

\[
 \#\{h\in\mathcal I_R:\|t_h\|\leq\delta\}
 \ll_\epsilon X^\epsilon(\delta R+1).
\tag{3.9}
\]

Dyadically decomposing \(\|t_h\|\) at scales \(2^j/T\), and using
(3.7)--(3.9), yields

\[
 \boxed{
 \sum_{h\in\mathcal I_R}\kappa_T(t_h)
 \ll_\epsilon X^\epsilon\left({R\over T}+1\right).}
\tag{3.10}
\]

This estimate includes exact integer arguments, where the individual
residual is \(1/2\); such arguments are divisor incidences and are already
covered by the \(+1\) term in (3.9).

Since \(|\psi_F|\leq1/2\), \(\kappa_T\leq1/2\), and (2.6) holds,
one has \(|V_T|\leq1\).  Hence \(M_{h,T}\), \(E_{h,T}\), and the
derivatives of \(I_1,I_2\) on the relevant bounded interval are all
uniformly bounded.  Applying (3.10) to \(L_h,U_h,L_h/2\), and
\((L_h+1)/2\) in the exact remainder (2.11) proves (1.4).
In fact, if \(\mathcal R_{J,T}=\sum_h r_{h,T}\) is split according to
the summands displayed in (2.11), the proof gives the stronger bound

\[
 \sum_{h\in\mathcal I_R}|r_{h,T}|
 \ll_\epsilon X^\epsilon\left({R\over T}+1\right).
\tag{3.10a}
\]

### 3.4 Exact nonzero modes and their phase

The parity polynomial (2.8) contains only odd Fourier indices:

\[
 E_{h,T}
 =\sum_{\substack{0<|r|\leq T\\r\ {\rm odd}}}
 b_{r,T}
 e\left({r(A-1)\over4h}\right),
\]

\[
 b_{r,T}={2\Phi_V(|r|/(T+1))\over\pi i r}e(r/4).
\tag{3.11}
\]

The count polynomial is

\[
 M_{h,T}={\ell\over2h}
 +\sum_{0<|s|\leq T}v_{s,T}(-1)^s
 \left\{e\left({s(A-1)\over2h}\right)
             -e\left({sB\over2h}\right)\right\}.
\tag{3.12}
\]

Expanding the quadratic \(I_j(M_{h,T})\) in (2.9) gives a finite sum
of terms of the form

\[
 c_{\tau,j}w_\tau(h)\widetilde{\mathcal A}_X(h,q_h+2j)
 e\left(\sqrt{Xh(q_h+2j)}+{\Gamma_\tau\over h}\right),
 \qquad j\in\{0,1\},
\tag{3.13}
\]

where \(w_\tau(h)\) is one of \(1,\ell/h,(\ell/h)^2\), or a bounded
linear combination of these, and

\[
 4\Gamma_\tau=r(A-1)+2sE_s+2tE_t,
\tag{3.14}
\]

with \(r\) nonzero and odd, \(|r|\leq T\), at most two indices
\(s,t\) with \(|s|,|t|\leq T\), and
\(E_s,E_t\in\{A-1,B\}\).  A missing selector mode is represented by
an index zero.  Moreover

\[
 \sum_{\tau,j}|c_{\tau,j}|\ll(\log(2T))^3.
\tag{3.15}
\]

The character parity prevents a regenerated zero endpoint frequency at
the target truncation.  Writing \(B=(A-1)+\ell\), (3.14) becomes

\[
 4\Gamma_\tau=(r+2s+2t)(A-1)+O(T\ell).
\tag{3.16}
\]

The first coefficient is an odd nonzero integer.  For
\(T=\lceil\sqrt R\rceil\), \(A\asymp R^2\), and \(\ell\leq R\),

\[
 \boxed{|\Gamma_\tau|\gg R^2.}
\tag{3.17}
\]

Thus no literal zero Fourier mode was discarded.  But (3.17) is a real
size statement, not a discrete derivative gap modulo one.

### 3.5 Why the finite core is still the original hard sum

The exact floor in (3.13) is highly discontinuous.  For an odd \(q>2\),

\[
 q_h=q
 \quad\Longleftrightarrow\quad
 {A-1\over q}<h\leq{A-1\over q-2}.
\tag{3.18}
\]

The length of this interval is

\[
 {2(A-1)\over q(q-2)}\asymp1
\tag{3.19}
\]

because \(A\asymp R^2\) and \(q\asymp R\).  Hence a smooth branch of
the phase in (3.13) contains only \(O(1)\) lattice points.  Conversely,
actual support gives \(q\geq4h>R\), so for fixed \(q\), two distinct
products in a length-\(R\) window would differ by more than the whole
window.  Every actual fixed-\(q\) fibre is therefore a singleton.

It is unlawful to differentiate (3.13) through the jumps of \(q_h\).
The radial phase change across an adjacent odd jump is

\[
 \sqrt{Xh(q+2)}-\sqrt{Xhq}\asymp hR,
\]

and need not be small modulo one.  The actual profile difference is small
on smooth pieces, but hard-profile and equality-star seams remain, and
the phase jump alone can have order one.  Consequently the sampled
variation of the complete factor in (3.13) can have \(R\) capacity.

Reindexing by the product makes the equivalence transparent:

\[
 \boxed{
 P_J=\sum_{n=A}^{B}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ h\in\mathcal I_R\\n/h\ {\rm odd}}}
 \chi_4(n/h)\widetilde{\mathcal A}_X(h,n/h).}
\tag{3.20}
\]

Thus endpoint Fourierization reduces the problem to a short, actual-
symbol, twisted divisor sum; it does not supply its estimate.  Applying
a derivative test separately to the \(O(R)\) branches in (3.18), or
taking absolute values term by term in (3.13), gives \(O(RX^\epsilon)\),
not \(O(X^\epsilon\sqrt R)\).

### 3.6 Fourth-power and signed exponent ledger

Let \(X=K^4\), \(R=K\).  Near \(n=K^2\), writing \(n=K^2+s\) gives

\[
 \sqrt{Xn}
 =K^3+{K\over2}s-{s^2\over8K}
 +O\left({|s|^3\over K^3}\right).
\tag{3.21}
\]

The linear term is integral or half-integral on integer \(s\), depending
on \(K\); it gives no uniform first-derivative gap.  The quadratic scale
would yield square-root cancellation for a smooth bounded symbol, but
the exact divisor/floor symbol in (3.20) has no proved target-sized BV or
Fourier norm.

For the inherited strict Round-57 fourth-power windows, there are
\(\gg R\) unmatched, star-free, top-plateau rows of amplitude at least
\(1/2\).  On them \(\nu_h=1\), so (1.3) is exactly one full term.  With
\(T=\lceil\sqrt R\rceil\), (1.4) has total residual
\(R^{1/2+o(1)}\); hence the finite main (2.9) still has rowwise absolute
mass \(\gg R\).  This rigorously rules out taking absolute values after
the endpoint Fourier expansion.  It does not prove that the signed sum
is large.

The unweighted ledger is:

| component or method | rigorous size | comparison with target |
|---|---:|---:|
| original high-shell absolute capacity | \(R X^\epsilon\) | loses \(\sqrt R\) |
| count-selector zero mode \(\ell/(2h)\) before character cancellation | \(R\) | must be retained |
| total Fejer residual at height \(T\) | \(X^\epsilon(R/T+1)\) | safe for \(T\geq\sqrt R\) |
| Fourier coefficient \(\ell^1\) mass | \(O((\log(2T))^3)\) | harmless |
| branchwise/trivial finite core | \(R X^\epsilon\) | loses \(\sqrt R\) |
| required signed finite core | \(X^\epsilon\sqrt R\) | open |

Restoring \((hq)^{-3/4}\asymp R^{-3/2}\), the residual and desired row
bound become \(R^{-1}=Y^{-1/2}\).  The unresolved \(R\)-capacity core
becomes \(R^{-1/2}=Y^{-1/4}\), leaving the same missing factor
\(\sqrt R=Y^{1/4}\).

## 4. First doubtful or unproved step

The first unproved step is a signed estimate for the complete finite core
at \(T=\lceil\sqrt R\rceil\):

\[
 \left|\sum_{j=0}^{1}\sum_{\tau}c_{\tau,j}
 \sum_{h\in\mathcal I_R}w_\tau(h)
 \widetilde{\mathcal A}_X(h,q_h+2j)
 e\left(\sqrt{Xh(q_h+2j)}+{\Gamma_\tau\over h}\right)\right|
 \ll_\epsilon X^\epsilon\sqrt R.
\tag{4.1}
\]

The outer \(\tau\)-sum in (4.1) is signed; taking absolute values before
the \(h\)-sum is not licensed as a proof of the target.  Equation (3.17)
removes a literal zero endpoint frequency, but it supplies neither a
modulo-one derivative gap nor sampled BV for the exact floor-radial
factor.  Equations (3.18)--(3.20) show that ordinary one-variable
curvature on smooth branches is empty of length.

Equivalently, one must prove square-root cancellation in the short
twisted-divisor sum (3.20), with the actual \(X\)-dependent angular
symbol and all stars.  No strict signed obstruction to that theorem has
been found.  Even if (4.1) were proved, only \(R/4<h\leq R/2\) would
close; the lower sector, alpha transfer, full M9-M1, and M9 would remain
separate.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| `exact_floor_selector` | Pass. Equations (1.1)--(1.3) exactly encode empty, singleton, and adjacent-pair rows. |
| `zero_mode` | Pass. The character zero mode cancels with full boundary ownership in (3.3)--(3.6); the geometric zero mode \(\ell/(2h)\) is retained in (2.7). |
| `fourier_truncation` | Pass. Equations (2.4)--(2.11) retain the exact Fejer residual, and (3.10) gives total \(X^\epsilon(R/T+1)\). |
| `character_projector` | Pass. Both the exact two-mode projector (3.3) and the floor-compatible parity square wave (2.3) are retained. |
| `cross_h_phase` | Exact but open. Every finite mode has phase (3.13)--(3.14); the surviving \(q_h\) sawtooth has only \(O(1)\)-point smooth branches. |
| `actual_amplitude` | Pass as an ownership ledger. The complete actual amplitude is never replaced by an envelope or smooth surrogate. |
| `endpoint_and_stars` | Pass. \(A-1\) and \(B\) encode full artificial edges; Vaaler integer residuals are retained; inherited angular and radial stars remain local. |
| `perfect_fourth_power` | Pass. Equation (3.21) forbids a derivative-gap assumption; the Round-57 family forces \(R\) post-expansion absolute capacity but is not promoted to a signed lower bound. |
| `target_ledger` | Pass. The endpoint residual is target-safe at \(T=\sqrt R\); the signed finite core alone retains the missing \(\sqrt R\). |
| `downstream_scope` | Pass. No lower-shell, alpha, M9-M1, M9, or exponent promotion is asserted. |

The point-window control also passes by (3.2): the formula becomes the
exact odd-quotient divisor incidence and contains no artificial pair.

## 6. Dependencies and exact artifacts used

Only the task-authorized artifacts were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md`;
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.

The Vaaler formula used in (2.4)--(2.6) is the already audited H4
interface recorded in the authorized graph.  The only arithmetic input in
the residual summation is the elementary divisor bound.  No web source,
unlisted artifact, or numerical experiment was used.  The work is 100%
analytical/algebraic.

## 7. Recommended state effect

Promote after independent validation the exact complete-row floor identity
(1.1)--(1.3), the two distinct zero-mode ledgers (3.3)--(3.6), and the
finite floor-compatible Vaaler identity (2.9)--(2.11).  Promote also the
endpoint Fejer residual estimate (3.10): truncation height
\(T=\lceil\sqrt R\rceil\) makes every endpoint and integer-jump residual
target-sized.

Promote only the scoped no-go for the remaining mechanism.  Endpoint
Fourierization followed by termwise absolute values or branchwise
one-variable derivative tests cannot prove the square-root target: the
actual fourth-power family has \(R\) post-expansion absolute capacity, and
every smooth floor branch has only \(O(1)\) lattice points.  Do not promote
a signed counterexample.

Retain the signed finite-core estimate (4.1), equivalently the short
actual-symbol twisted-divisor estimate (3.20), as open.  Retain the lower
shell, full residual core, alpha connectors, M9-M1, M9, and the final
Gauss-circle exponent open.

# Round231: independent full harmonic-pooling proof

- Task: `blind_harmonic_pooling`.
- Role: statement-only independent rederiver; selection phase only.
- Supplied graph provenance tag: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` (not inspected).
- Generated: 2026-10-11 03:00:40 UTC.
- Status: complete; no shared-state modification.

## 1. Result: the asserted lower bound follows

Under the supplied hypotheses,

\[
 C_{\rm harm}(T)\ge c_{\Psi,w}T^{5/2}
\]

for every sufficiently large real \(T\). The proof uses the actual fully pooled functions throughout. A Gram-matrix lower bound for sixfold products supplies the required absolute mass. Its effective dimension is \(O(T^{3/2})\). The contribution of pairs of six-tuples sharing a squarefree label is \(O(T^{2+\epsilon})\), so removing every repeated label preserves the lower bound.

This avoids any assertion that a selected fundamental resonance survives harmonic pooling. No microresonance equidistribution theorem is needed. All common harmonic multiples and mixed harmonic vectors remain in the full Gram matrix. The infinite harmonic sum is paid both in the lower-bound approximation and, separately, in the repeated-label upper bound.

## 2. Exact statement and hypotheses

Use exactly the supplied definitions

\[
 f_d(R)=d^{-3/4}\sum_{s\ge1}c(d,s)s^{-3/2}
 \Psi(s\sqrt{d/T})\cos(2\pi Rs\sqrt d-3\pi/4),
 \qquad c(d,s)=r_2(ds^2),
\]

and the ordered, pairwise-distinct squarefree-label sum \(C_{\rm harm}(T)\) from the isolated statement. In particular:

- \(\Psi\) is continuous and real on the real axis, \(\Psi(0)=1\), and \(|\Psi|\le1\). It may change sign away from zero.
- \(w\ge0\) is smooth, supported in \([1/2,2]\), with \(W=\int w>0\).
- \(0\le c(d,s)\le r_2(d)\tau(s^2)\), and \(c(d,1)=r_2(d)\).
- \(r_2(d)\ll_\eta d^\eta\) for each fixed \(\eta>0\).
- Every fixed positive interval \([uT,vT]\) has squarefree \(r_2\)-mass at least \(c_{u,v}T\) for all sufficiently large real \(T\).
- \(B:=\sum_{s\ge1}\tau(s^2)s^{-3/2}<\infty\).

The entire-function and Schwartz assumptions on \(\Psi\), and the supplied global first-moment upper bound for \(r_2\), are stronger than this proof needs. No supplementary arithmetic hypothesis is imported.

## 3. Proof and derivation

### 3.1 Fixed boxes and normalized full functions

By continuity, choose an open interval \(J\subset(0,\infty)\) on which \(\Psi(x)\ge3/4\). For a label with \(r_2(d)>0\), put

\[
 a_d=r_2(d)d^{-3/4},\qquad h_d=f_d/a_d,
\]

and let \(h_{d,H}\) denote its restriction to \(1\le s\le H\). With

\[
 B_H=\sum_{s>H}\tau(s^2)s^{-3/2},
\]

we have uniformly in every parameter

\[
 |h_d|,|h_{d,H}|\le B,\qquad |h_d-h_{d,H}|\le B_H.
\tag{1}
\]

If \(r_2(d)=0\), the coefficient bound makes \(f_d=0\), so such labels can be omitted without loss.

Set

\[
 \kappa_0=W(9/32)^6,\qquad \kappa=\kappa_0/2.
\]

Choose one fixed integer \(H\), sufficiently large that

\[
 6B^5B_H\sqrt W\le\sqrt\kappa/8.
\tag{2}
\]

This choice precedes all subsequent choices and is independent of \(T\).

Choose six distinct numbers \(x_1,\ldots,x_6\in J\) outside the finite union of hyperplanes

\[
 \sum_{j=1}^6 n_jx_j=0,
 \qquad 0\ne n\in\mathbb Z^6,\quad |n_j|\le2H.
\]

Choose sufficiently small disjoint closed intervals \(J_j\subset J\) around them. Their squares are disjoint positive intervals \(I_j=[u_j,v_j]\), and some \(\gamma>0\) satisfies

\[
 \left|\sum_jn_jy_j\right|\ge\gamma
 \quad(y_j\in J_j,;0\ne n\in\mathbb Z^6,;|n_j|\le2H).
\tag{3}
\]

Let \(D_j(T)\) consist of squarefree \(d\in I_jT\) with \(r_2(d)>0\). All these labels exceed \(\lfloor T^{2/5}\rfloor\) for sufficiently large real \(T\). The supplied interval-mass lower bound gives

\[
 \sum_{d\in D_j(T)}a_d
 \ge(v_jT)^{-3/4}\sum_{d\in D_j(T)}r_2(d)
 \ge c_jT^{1/4}.
\tag{4}
\]

For a six-tuple \(q=(d_1,\ldots,d_6)\in\mathcal Q:=\prod_jD_j(T)\), write

\[
 A_q=\prod_ja_{d_j},\qquad
 g_q(R)=\prod_jh_{d_j}(R),\qquad
 g_{q,H}(R)=\prod_jh_{d_j,H}(R).
\]

The six entries in each \(q\) are already distinct, because the boxes are disjoint. From (1),

\[
 |g_q|,|g_{q,H}|\le B^6,\qquad
 |g_q-g_{q,H}|\le6B^5B_H.
\tag{5}
\]

### 3.2 Uniform positive norm of the finite approximation

Work in \(\mathcal H_T=L^2(w(R/T)\,dR)\), with its usual complex Hilbert-space extension when needed. Set

\[
 b_{d,s}=\frac{c(d,s)}{r_2(d)}s^{-3/2}\Psi(s\sqrt{d/T}).
\]

For labels in our boxes, \(b_{d,1}\ge3/4\). In the finite trigonometric expansion of \(g_{q,H}^2\), the coefficient with zero frequency in every one of the six formal coordinates is exactly

\[
 \prod_{j=1}^6\left(\frac12\sum_{s\le H}b_{d_j,s}^2\right)
 \ge(9/32)^6.
\tag{6}
\]

This identity squares the real coefficients and is unaffected by any signs of \(\Psi(s\sqrt{d/T})\). Every other frequency has the form \(\sum_jn_j\sqrt{d_j}\), with the nonzero integer vector covered by (3), and therefore has absolute value at least \(\gamma\sqrt T\). The total absolute coefficient sum is at most \(B^{12}\).

For \(e(z)=\exp(2\pi iz)\), smoothness of \(w\) gives, for any fixed \(N>1\),

\[
 \left|\int w(R/T)e(\lambda R)\,dR\right|
 \le C_{N,w}T(1+T|\lambda|)^{-N}.
\tag{7}
\]

Consequently (6), (7), and (3) imply, uniformly in \(q\),

\[
 \|g_{q,H}\|_{\mathcal H_T}^2
 \ge\kappa_0T-O_{H,w}(T(1+\gamma T^{3/2})^{-N})
 \ge\kappa T
\tag{8}
\]

for sufficiently large real \(T\). All parameters in the error bound are fixed.

### 3.3 A subspace of dimension \(O(T^{3/2})\) retains positive full-function energy

Here is an explicit elementary bandwidth construction, including its approximation error. Rescale \(R=Tx\), and choose \(\chi\in C_c^\infty((0,3))\) equal to one on \([1/2,2]\). Every exponential in \(g_{q,H}(Tx)\) has frequency

\[
 \theta=T\sum_{j=1}^6\epsilon_js_j\sqrt{d_j},
 \qquad |\theta|\le F T^{3/2},
\]

where \(F=6H\max_j\sqrt{v_j}\) is fixed. For the periodic Fourier expansion on \([0,3]\), the coefficients of \(\chi(x)e(\theta x)\) obey

\[
 |\widehat{\chi e(\theta\cdot)}(k)|
 \le C_L(1+|k/3-\theta|)^{-L}
\tag{9}
\]

for any fixed \(L\), uniformly in \(\theta\). Take

\[
 K=\left\lceil6(F+1)T^{3/2}\right\rceil,
 \qquad
 V_T=\operatorname{span}\{e(kR/(3T)):|k|\le K\}
 \subset\mathcal H_T.
\]

Its dimension \(D\le2K+1\ll_HT^{3/2}\). For \(|k|>K\), the frequency distance in (9) is at least \(|k|/6\). Thus truncating this Fourier series at \(K\) has uniform error \(O_L(K^{1-L})\). The total absolute exponential coefficient sum in \(g_{q,H}\) is at most \(B^6\), so

\[
 \operatorname{dist}_{\mathcal H_T}(g_{q,H},V_T)
 \le C_LB^6K^{1-L}\sqrt{WT}=o(\sqrt T)
\tag{10}
\]

uniformly in \(q\). This argument does not require smoothness of \(\sqrt w\).

Let \(P_T\) be the orthogonal projection onto \(V_T\). Equations (2) and (5) give

\[
 \|g_q-g_{q,H}\|_{\mathcal H_T}\le\sqrt\kappa\sqrt T/8.
\]

For sufficiently large \(T\), (10) is bounded by the same quantity. By (8) and the triangle inequality,

\[
 \|P_Tg_q\|\ge\|g_{q,H}\|
   -\|(1-P_T)g_{q,H}\|-\|P_T(g_q-g_{q,H})\|
 \ge\tfrac34\sqrt{\kappa T}.
\]

In particular, with the fixed constant \(\rho=\kappa/4>0\),

\[
 \|P_Tg_q\|^2\ge\rho T.
\tag{11}
\]

The functions in (11) are the full infinite harmonic products. A fixed small tail is sufficient because it is used to retain single-vector projection energy, not subtracted after summing all matrix entries.

### 3.4 Weighted Gram inequality gives the \(T^{5/2}\) mass

Define

\[
 I_{q,q'}=\int w(R/T)g_q(R)g_{q'}(R)\,dR,
 \qquad S_{\rm all}=\sum_{q,q'\in\mathcal Q}A_qA_{q'}|I_{q,q'}|.
\]

These are real inner products of the actual full harmonic functions. Form the finite Gram matrix \(G\) of the vectors \(\sqrt{A_q}g_q\). If \(G_P\) and \(G_\perp\) are the Gram matrices of their projected and perpendicular parts, then

\[
 G=G_P+G_\perp,\qquad G_P,G_\perp\succeq0,
 \qquad\operatorname{rank}G_P\le D.
\]

Positive semidefiniteness gives

\[
 \operatorname{tr}G^2\ge\operatorname{tr}G_P^2
 \ge\frac{(\operatorname{tr}G_P)^2}{D}
 \ge\frac{\rho^2T^2}{D}\left(\sum_qA_q\right)^2.
\tag{12}
\]

For clarity, the first inequality follows by expanding \(\operatorname{tr}(G_P+G_\perp)^2\), since \(\operatorname{tr}(G_PG_\perp)\ge0\). Thus no unjustified entrywise comparison of full and truncated Gram matrices occurs.

On the other hand,

\[
 \operatorname{tr}G^2=\sum_{q,q'}A_qA_{q'}|I_{q,q'}|^2,
 \qquad |I_{q,q'}|\le B^{12}WT.
\]

Combining this with (12),

\[
 S_{\rm all}
 \ge\frac{\rho^2T}{B^{12}WD}\left(\sum_qA_q\right)^2.
\tag{13}
\]

By (4),

\[
 \sum_qA_q=\prod_{j=1}^6\sum_{d\in D_j(T)}a_d
 \gg T^{6/4}=T^{3/2}.
\]

Since \(D\ll T^{3/2}\), (13) proves

\[
 S_{\rm all}\gg T^{5/2}.
\tag{14}
\]

This is an absolute-entry estimate. It does not assert a corresponding lower bound on a signed sum over twelve-tuples.

### 3.5 Remove every repeated label, using every harmonic

Let \(S_{\rm overlap}\) be the part of \(S_{\rm all}\) where \(q=(d_1,\ldots,d_6)\) and \(q'=(e_1,\ldots,e_6)\) share at least one label. The boxes are disjoint, so a shared label can occur only as \(d_j=e_j\). Fix its exact nonempty equality pattern

\[
 E=\{j:d_j=e_j\},\qquad m=12-|E|\le11.
\]

There are \(m\) distinct label variables, each in a fixed interval comparable to \(T\). Expand all twelve full cosine series, using the absolute coefficient bound and (7). For a fixed harmonic vector \((s_1,\ldots,s_6,t_1,\ldots,t_6)\) and cosine signs, the frequency is

\[
 \Lambda=\sum_j\sigma_js_j\sqrt{d_j}+\sum_j\tau_jt_j\sqrt{e_j}.
\]

For a shared label its resulting integer coefficient is \(\sigma_js_j+\tau_jt_j\); otherwise its coefficient is one of the nonzero signed harmonics. For any fixed \(\eta>0\), the absolute amplitude before integration is bounded by

\[
 C_\eta T^{-9+12\eta}
 \prod_{j=1}^6\bigl(\tau(s_j^2)s_j^{-3/2}\bigr)
                   \bigl(\tau(t_j^2)t_j^{-3/2}\bigr).
\tag{15}
\]

Here the power \(-9\) includes all twelve factors \(d^{-3/4}\), even when labels coincide.

If at least one resulting label coefficient is a nonzero integer \(k\), freeze the other \(m-1\) variables. For this active variable \(n\), consecutive values of \(T(k\sqrt n+\beta)\), with \(n\asymp T\), are separated by at least \(c|k|\sqrt T\ge c\sqrt T\). Therefore, for \(N>1\),

\[
 \sum_{n\text{ in its interval}}
 (1+T|k\sqrt n+\beta|)^{-N}\le C_N,
\tag{16}
\]

uniformly in every real \(\beta\), every nonzero integer \(k\), and all sufficiently large real \(T\). The sum over squarefree or noncolliding allowed labels is smaller than this unrestricted integer sum. Summing (7) over all labels therefore costs at most \(CT^m\): \(T^{m-1}\) for the frozen variables, a bounded quantity in (16), and the outer factor \(T\) from the integral.

If all resulting coefficients vanish, necessarily \(d_j=e_j\) for every \(j\), since an unshared label has a nonzero harmonic coefficient. Thus \(m=6\). This exceptional case has at most \(O(T^6)\) label choices and integral at most \(WT\).

Finally sum every harmonic and every sign. By the given convergent series, the total harmonic weight in (15) sums to \(B^{12}\). It is independent of the harmonic frequencies in (16), so large harmonics and arbitrarily large common multiples incur no loss. The finitely many equality patterns consequently give

\[
 S_{\rm overlap}
 \ll_\eta T^{2+12\eta}+T^{-2+12\eta}.
\tag{17}
\]

Taking, for example, \(\eta=1/48\) makes (17) \(O(T^{9/4})=o(T^{5/2})\).

### 3.6 Conclude for the specified ordered distinct-label sum

For \(q,q'\) without overlap,

\[
 A_qA_{q'}I_{q,q'}
 =\int w(R/T)\prod_{j=1}^6f_{d_j}(R)\prod_{j=1}^6f_{e_j}(R)\,dR.
\]

Each such pair injects into the ordered, pairwise-distinct twelve-tuples in the definition of \(C_{\rm harm}\). Therefore (14) and (17) yield

\[
 C_{\rm harm}(T)\ge S_{\rm all}-S_{\rm overlap}
 \ge cT^{5/2}-CT^{9/4}\ge\tfrac c2T^{5/2}
\]

for every sufficiently large real \(T\). All choices and thresholds are fixed in the proof; none selects a subsequence of real windows.

## 4. First doubtful or unproved step

No unproved step remains relative to the supplied hypotheses. The substantial hypothesis used without rederivation is precisely the supplied squarefree interval-mass lower bound, invoked in (4); its proof was explicitly outside this isolated task.

Two tempting shortcuts would have been gaps but are not used here: pointwise positivity of a chosen near-resonant twelve-tuple after pooling; and subtracting a fixed tail error after summing all \(O(T^{12})\) pairs. The actual proof replaces both by positive semidefinite Gram control, where a fixed tail only needs to preserve each vector's projected norm.

## 5. Required controls and outcomes

All controls below are analytic; no numerical experiment was performed.

1. **Sign-changing \(\Psi\): pass.** Only its fundamental coefficient in the fixed boxes is chosen positive. Every other coefficient may have either sign. Equation (6) uses squares; the Gram argument uses full real functions and absolute inner products.
2. **Full infinite tail: pass.** Equation (2) and the telescoping product bound (5) control the complete tail uniformly for the retained projected energy. Equation (17) separately sums all twelve infinite harmonic series for overlaps. No fixed-tail error is summed over all tuple pairs.
3. **Common multiples: pass.** All common multiples, whether small or arbitrarily large, occur in the full Gram matrix. In the overlap estimate their resulting integer coefficient is either zero, handled explicitly, or has magnitude at least one, covered uniformly by (16).
4. **Mixed harmonic vectors: pass.** Finite mixed vectors enter the exact expansion proving (8). Every full mixed vector enters (12) and is covered by the absolute harmonic sum in (17). No mixed vector is assumed harmless by sign.
5. **Exact repeated-label degeneracy: pass.** The fully zero-frequency repeated-label contribution has only six free labels and is \(O(T^{-2+12\eta})\). Partly repeated configurations have at most eleven labels and satisfy the spacing estimate, giving \(O(T^{2+12\eta})\).
6. **Scaling: pass.** Each box has normalized amplitude mass \(\asymp\) at least \(T^{1/4}\); six boxes give \(T^{3/2}\). The Gram estimate is \(T(T^{3/2})^2/T^{3/2}=T^{5/2}\). The overlap exponent is strictly smaller.
7. **Real windows and cutoff: pass.** The hypotheses, spacing estimate, Fourier bounds and rank bound hold for all sufficiently large real \(T\). Fixed positive boxes eventually lie above \(\lfloor T^{2/5}\rfloor\).
8. **Signed versus absolute target: pass.** The step \(|I|^2\le B^{12}WT|I|\) is indispensable. It does not produce a lower bound for the signed distinct-label sum.
9. **No use of an unavailable fine-scale count: pass.** The only lower count is the stated macroscopic interval-mass estimate. Frequency-space dimension supplies the collision mass globally, while elementary one-variable spacing supplies the required upper control for overlaps.

## 6. Dependencies and isolation disclosure

Exact files read:

1. `protocol.md`.
2. `strategy/round231_harmonic_admission/briefs/blind_harmonic_pooling.md` (own brief).
3. `strategy/round231_harmonic_admission/briefs/blind_harmonic_statement.md` (isolated statement).

No graph file, active campaign, historical artifact, source report, sibling report, proof draft, or external literature was read. The brief explicitly replaced the usual research-context reads with statement-only isolation. No additional arithmetic assertion or external theorem is needed beyond the supplied hypotheses. Elementary Fourier integration by parts, finite-dimensional positive semidefinite matrix algebra, and an integer spacing estimate are derived in the report.

The conductor received short progress messages describing the developing method; no mathematical context was received from the conductor or siblings after assignment. Work was entirely analytical/algebraic, with zero numerical experimentation. The only written artifact is this assigned report.

## 7. Recommended state effect and stopping point

**Recommended effect: promote this precise fully harmonic-pooled lower bound, conditional on the explicitly supplied hypotheses, after conductor-controlled seam review and graph validation.** The independently established result is the absolute certificate lower bound only. It makes no claim about any signed twelve-tuple sum or about an unsupplied downstream implication.

No state file, proof draft, validation matrix, or synthesis was edited. This task stops after freezing this report and supplying its SHA256; no next round is designed.

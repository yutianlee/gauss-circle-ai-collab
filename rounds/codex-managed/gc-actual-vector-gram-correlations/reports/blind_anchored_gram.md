# Round221 isolated fixed-vector Gram report

## 1. Result

**Verdict: GREEN for the exact finite identities and characterizations below. They supply no analytic estimate without an additional bound on the fixed-vector quantity.**

For every integer \(k\geq1\),

\[
 \boxed{a_k=b^*M^kb=f^*G^{k-1}f,\qquad
        a_1^k\leq B^{k-1}a_k.}
 \tag{1}
\]

The constant in the inequality is sharp. If \(B>0\) and \(k>1\), equality holds exactly when the spectral support of \(b\) lies in one eigenspace of \(M\), including its zero eigenspace.

For independently specified \(f\) and real budget \(B\), with \(G=UU^*\) fixed, the exact bordered-positivity condition is

\[
 \boxed{
 \begin{pmatrix}B&f^*\\f&G\end{pmatrix}\succeq0
 \quad\Longleftrightarrow\quad
 f\in\operatorname{ran}G,\quad f^*G^\dagger f\leq B.
 }
 \tag{2}
\]

These conditions are also necessary and sufficient for the existence of some \(c\) with \(Uc=f\) and \(\|c\|^2\leq B\). They do not identify that \(c\) with a separately prescribed \(b\).

In the exponential example, a simultaneous translation of all sample times leaves \(G\) invariant but replaces \(f=Ub\) by \(UD_hb\), where \(D_h\) is a diagonal unitary matrix. An exact example with nonnegative fixed \(b\) changes \(f\) from \((2,2)\) to zero while \(G\) and \(B\) remain unchanged.

## 2. Exact hypotheses and conventions

Let \(U\in\mathbb C^{J\times n}\), \(b\in\mathbb C^n\), and

\[
 B=b^*b,\qquad f=Ub,\qquad
 G=UU^*,\qquad M=U^*U.
 \tag{3}
\]

Both \(G\) and \(M\) are Hermitian positive semidefinite. The star denotes conjugate transpose. The norm of a matrix below is its Euclidean operator norm.

The moment identities and inequalities in (1) concern this prescribed vector \(b\), not a supremum over coefficient vectors. When discussing (2) as a characterization, \(f\) and \(B\) may instead be treated as candidate data independent of a prescribed \(b\); this distinction is always stated.

The Moore--Penrose inverse of a positive semidefinite matrix is defined by finite spectral decomposition:
\[
 G=\sum_{\gamma>0}\gamma P_\gamma,\qquad
 G^\dagger=\sum_{\gamma>0}\gamma^{-1}P_\gamma,
 \tag{4}
\]
with zero on \(\ker G\). No inverse is taken on a zero eigenspace.

The high-value consequence assumes \(J\geq1\) and \(|f_j|\geq v>0\) for every row. If zero-dimensional matrices are permitted, the identities have their usual empty-sum meanings; no consequence divides by an empty row count.

In the translation example, \(\mu_\nu\geq0\), \(\lambda_\nu,t_j,h\) are real, and
\[
 U_{j,\nu}=\sqrt{\mu_\nu}\,e(t_j\lambda_\nu),\qquad
 e(x)=\exp(2\pi i x).
 \tag{5}
\]
The coefficient vector \(b\) is fixed and real there, and the explicit control will have \(b\geq0\).

## 3. Proof and exact finite content

### Chain identity, with the fixed endpoints displayed

For every \(k\geq1\),
\[
 U^*(UU^*)^{k-1}U=(U^*U)^k.
 \tag{6}
\]
This follows by associative multiplication, or by induction starting with \(U^*U=M\). Multiplication on the left and right by \(b^*,b\) proves the first identity in (1).

With row indices \(j_1,\ldots,j_k\), its exact row-Gram expansion is

\[
 a_k=
 \sum_{j_1,\ldots,j_k=1}^J
 \overline{f_{j_1}}\,
 \left(\prod_{r=1}^{k-1}G_{j_r,j_{r+1}}\right)
 f_{j_k}.
 \tag{7}
\]

For \(k=1\), the product is empty and equals one, so (7) is
\(\sum_j|f_j|^2\). Substituting both fixed-vector endpoints and every Gram entry gives the fully indexed expression

\[
 \boxed{
 a_k=
 \sum_{\alpha_0,\ldots,\alpha_k=1}^n
 \overline{b_{\alpha_0}}b_{\alpha_k}
 \sum_{j_1,\ldots,j_k=1}^J
 \prod_{r=1}^k
 \overline{U_{j_r,\alpha_{r-1}}}U_{j_r,\alpha_r}.
 }
 \tag{8}
\]

Equivalently, before expanding the column Gram kernels,

\[
 a_k=\sum_{\alpha_0,\ldots,\alpha_k}
 \overline{b_{\alpha_0}}
 \left(\prod_{r=1}^kM_{\alpha_{r-1},\alpha_r}\right)
 b_{\alpha_k},
 \qquad
 M_{\alpha,\beta}=\sum_j\overline{U_{j,\alpha}}U_{j,\beta}.
 \tag{9}
\]

Equations (7)--(9) retain the complex phases and the prescribed endpoint coefficients. Individual summands need not be real or nonnegative. Nonnegativity of the complete \(a_k\) comes from the positive semidefinite matrix \(M^k\).

### Sharp moment inequality and equality

Choose an orthonormal eigenbasis \(v_r\) of \(M\), with eigenvalues \(\theta_r\geq0\), and write \(b=\sum_r\beta_rv_r\). Then

\[
 B=\sum_r|\beta_r|^2,\qquad
 a_k=\sum_r|\beta_r|^2\theta_r^k.
 \tag{10}
\]

If \(B>0\), put \(p_r=|\beta_r|^2/B\). These are nonnegative weights summing to one, including any mass in the zero eigenspace. Convexity of \(x\mapsto x^k\) on \([0,\infty)\) gives

\[
 \left(\frac{a_1}{B}\right)^k
 =\left(\sum_rp_r\theta_r\right)^k
 \leq\sum_rp_r\theta_r^k
 =\frac{a_k}{B}.
 \tag{11}
\]

This proves (1). For \(k=1\), it is an identity for every \(b\). For \(k>1\), strict convexity shows equality precisely when all \(\theta_r\) with \(\beta_r\ne0\) have the same value \(\theta\). Equivalently,
\[
 Mb=\theta b\quad\hbox{for some }\theta\geq0.
 \tag{12}
\]

If \(B=0\), then \(b=0\), \(f=0\), and every \(a_k=0\). For \(k=1\) read the assertion simply as \(a_1=a_1\); no expression \(0^0\) is needed. For \(k>1\), both sides of the inequality are zero.

The constant one is optimal: for a scalar matrix \(U=(\sqrt\theta)\) and a scalar \(b\), one has \(a_k=B\theta^k\), giving equality. Rank deficiency causes no change to the proof.

If \(|f_j|\geq v>0\) for all \(J\geq1\) rows, then \(B>0\) and

\[
 \boxed{
 (Jv^2)^k\leq a_1^k\leq B^{k-1}a_k,
 \qquad
 J\leq\frac{B^{1-1/k}a_k^{1/k}}{v^2}.
 }
 \tag{13}
\]

For \(k>1\), equality throughout requires both \(|f_j|=v\) for every row and (12). For \(k=1\), only the first condition is needed. If \(B=0\), the positive-level hypothesis is impossible for a nonempty row set.

### Bordered positivity in singular as well as invertible cases

First, \(\ker G=\ker U^*\), because
\(x^*Gx=\|U^*x\|^2\). Finite-dimensional orthogonal complements therefore give

\[
 \operatorname{ran}G=(\ker G)^\perp
                     =(\ker U^*)^\perp
                     =\operatorname{ran}U.
 \tag{14}
\]

Consider candidate data \(f\in\mathbb C^J\) and real \(B\), and put
\(\mathcal H=\left(\begin{smallmatrix}B&f^*\\f&G\end{smallmatrix}\right)\).
If \(\mathcal H\succeq0\), then \(f\) is orthogonal to \(\ker G\). Otherwise choose \(x\in\ker G\) with \(f^*x\ne0\); the quadratic form on \((1,tx)\) is \(B+2\operatorname{Re}(t f^*x)\), which becomes negative for a suitable \(t\). Thus \(f\in\operatorname{ran}G\) is necessary.

Assuming this range condition, define
\[
 g=G^\dagger f,\qquad \tau=f^*G^\dagger f\geq0.
 \tag{15}
\]
Then \(Gg=f\), and exact completion of the square gives, for \(z\in\mathbb C\), \(x\in\mathbb C^J\),

\[
 \begin{pmatrix}z\\x\end{pmatrix}^{\!*}
 \mathcal H
 \begin{pmatrix}z\\x\end{pmatrix}
 =(x+zg)^*G(x+zg)+(B-\tau)|z|^2.
 \tag{16}
\]

This proves (2), including \(G=0\): in that case \(f=0\) is necessary and sufficient apart from \(B\geq0\).

The same formula shows, for positive semidefinite \(\mathcal H\),
\[
 \operatorname{rank}\mathcal H
 =\operatorname{rank}G+\mathbf1_{\{B>\tau\}}.
 \tag{17}
\]
At the equality boundary \(B=\tau\), its kernel consists of
\((z,-zG^\dagger f+h)\) with \(h\in\ker G\). If \(B>\tau\), the kernel consists of \((0,h)\), \(h\in\ker G\).

Equivalently, (2) says that \(B\geq0\) and
\[
 |x^*f|^2\leq B\,x^*Gx\quad\hbox{for every }x.
 \tag{18}
\]
Indeed, on the positive eigenspaces this is Cauchy--Schwarz between \(G^{1/2}x\) and \(G^{\dagger/2}f\). The optimal squared ratio in (18) is \(\tau\), attained by \(x=G^\dagger f\) when \(f\ne0\). Components in \(\ker G\) must first vanish, as above; they cannot be ignored by the pseudoinverse.

### Some preimage, the minimal preimage, and the prescribed vector

By (14), \(Uc=f\) has a solution exactly when \(f\in\operatorname{ran}G\). In that case define
\[
 c_0=U^*G^\dagger f.
 \tag{19}
\]
Then \(Uc_0=GG^\dagger f=f\), and
\[
 \|c_0\|^2
 =f^*G^\dagger GG^\dagger f
 =f^*G^\dagger f=\tau.
 \tag{20}
\]

The vector \(c_0\) belongs to \(\operatorname{ran}U^*=(\ker U)^\perp\). Every solution is uniquely
\[
 c=c_0+z,\qquad z\in\ker U,\qquad
 \|c\|^2=\tau+\|z\|^2.
 \tag{21}
\]
This proves the requested necessary and sufficient conditions for existence with norm at most \(B^{1/2}\), and the uniqueness of the minimum-norm solution, without assuming full rank.

For the original data \(f=Ub\), (21) becomes
\[
 c_0=P_{(\ker U)^\perp}b,\qquad
 B-\tau=\|P_{\ker U}b\|^2.
 \tag{22}
\]
Thus bordered positivity is automatic for those original data. Equality \(B=\tau\) holds precisely when the prescribed \(b\) is the minimum-norm preimage, or equivalently \(b\perp\ker U\).

For candidate data, (2) supplies some vector \(c\); it does not prove \(c=b\), nor \(f=Ub\) for a previously specified \(b\) known only through its norm. Even an exact-norm preimage need not be that prescribed vector. If exact norm \(\|c\|^2=B\), rather than at most \(B\), were requested, (21) shows the extra distinction: either \(B=\tau\), or \(B>\tau\) and \(\ker U\ne\{0\}\). The packet requests the at-most condition, for which (2) is exactly sufficient.

### What generic norm bounds discard

The positive nonzero eigenvalues of \(M\) and \(G\) agree: if \(Mv=\theta v\) with \(\theta>0\), then \(Uv/\sqrt\theta\) is a unit eigenvector of \(G\), and the reverse map is \(U^*/\sqrt\theta\). Therefore
\(\|M\|=\|G\|\), including the zero-matrix case. From (10),
\[
 a_k\leq B\|G\|^k.
 \tag{23}
\]

Combining only (23) with (1) yields exactly
\[
 a_1\leq B\|G\|,\qquad Jv^2\leq B\|G\|
 \tag{24}
\]
under the high-value hypothesis. Increasing \(k\) supplies no improvement through this generic bound. It has replaced the spectral distribution of the fixed \(b\) by concentration on the top eigenspace.

Likewise, replacing the endpoints \(\overline b_{\alpha_0},b_{\alpha_k}\) in (8)--(9) by generic Cauchy bounds removes their orientation and phase correlation with the chain. An operator-norm closure gives (23); additional termwise absolute values can give still weaker bounds. Such operations are valid upper estimates when justified, but they no longer exploit the prescribed vector.

The bordered matrix itself is the Gram matrix
\[
 \begin{pmatrix}b^*\\U\end{pmatrix}
 \begin{pmatrix}b^*\\U\end{pmatrix}^{\!*}
 =\begin{pmatrix}B&f^*\\f&G\end{pmatrix}.
 \tag{25}
\]
The added row is \(b^*\), with the conjugation required by the stated convention. Its positivity gives the generic bounds
\[
 |f_j|^2\leq BG_{jj},\qquad
 f^*G^\dagger f\leq B,\qquad
 \|f\|^2\leq B\|G\|.
 \tag{26}
\]
Thus PSD does give these Cauchy-type upper bounds. Adding the row does not give a stronger cancellation estimate for its new off-diagonal entries without an additional estimate: those entries are exactly the unknown fixed-vector sums \(f_j\).

### Simultaneous translation and the fixed coefficient vector

For (5), define
\[
 D_h=\operatorname{diag}(e(h\lambda_1),\ldots,e(h\lambda_n)).
 \tag{27}
\]
Translating every \(t_j\) by \(h\) gives
\[
 U(h)=UD_h,\qquad
 G(h)=UD_hD_h^*U^*=G,\qquad
 M(h)=D_h^*MD_h,
 \tag{28}
\]
while the prescribed \(b\) and \(B\) stay fixed and
\[
 f(h)=UD_hb.
 \tag{29}
\]
In coordinates,
\[
 G_{j,l}=\sum_\nu\mu_\nu e((t_j-t_l)\lambda_\nu),\qquad
 f_j(h)=\sum_\nu\sqrt{\mu_\nu}b_\nu
                         e(h\lambda_\nu)e(t_j\lambda_\nu).
 \tag{30}
\]

The row Gram depends only on time differences; the fixed-vector sum retains the absolute translated phase. Correspondingly,
\[
 a_k(h)=b^*D_h^*M^kD_hb
       =f(h)^*G^{k-1}f(h).
 \tag{31}
\]
There is no reason for this to be translation invariant.

One could preserve \(f\) by changing the coefficient vector to \(D_h^*b\) along with the translation. That is a different prescribed vector, generally complex even when the original \(b\) is real and nonnegative. It is not an invariance available while keeping the packet's \(b\) fixed.

## 4. First unproved or unsupported step in a prospective use

The finite statements above have no remaining gap. A prospective analytic use still needs an actual upper estimate for the fixed-vector \(a_k\), retaining its coefficient endpoints or otherwise controlling their loss. Neither the identity nor PSD proves such an estimate.

Three unsupported transitions would be:

1. replacing the prescribed \(b\) by an existential preimage produced from bordered positivity;
2. inferring a gain at large \(k\) after using only \(a_k\leq B\|G\|^k\);
3. treating a simultaneous translation as preserving \(f\) because it preserves \(G\).

The exact controls below show these are substantive distinctions, not issues of notation. No analytic or arithmetic theorem is inferred from the finite PSD statements.

## 5. Exact controls, including singular and zero cases

**Fixed nonnegative coefficients and translation.** Take \(J=n=2\),
\[
 \mu_1=\mu_2=1,\quad \lambda_1=0,\quad\lambda_2=1,\quad
 (t_1,t_2)=(0,1),\quad b=(1,1)^{\mathsf T}.
\]
Initially
\[
 U=\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
 G=\begin{pmatrix}2&2\\2&2\end{pmatrix},\quad
 B=2,\quad f=(2,2)^{\mathsf T}.
\]
After translating both times by \(h=1/2\),
\[
 U(h)=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\quad
 G(h)=G,\quad B(h)=2,\quad f(h)=0.
 \tag{32}
\]
The coefficient vector remains nonnegative and unchanged. The original moments are \(a_k=2\cdot4^k\), while all translated moments vanish. Both bordered matrices are PSD: initially every entry is \(2\), whereas after translation the top row/column has zero off-diagonal entries and the lower block is the same \(G\). Thus \(G\) and \(B\) alone permit both the Cauchy maximum in this example and zero.

**Range condition cannot be omitted.** Take
\[
 U=\operatorname{diag}(1,0),\quad G=\operatorname{diag}(1,0),\quad
 f=(0,1)^{\mathsf T}.
\]
Then \(f^*G^\dagger f=0\), but no \(c\) solves \(Uc=f\). The bordered matrix is not PSD for any finite \(B\): its principal block using the top coordinate and the second row is
\(\left(\begin{smallmatrix}B&1\\1&0\end{smallmatrix}\right)\), with determinant \(-1\). The range condition in (2) is essential.

**Existence does not identify the fixed vector.** Take \(U=(1,0)\) and prescribed \(b=(1,0)^{\mathsf T}\), so \(B=1\) and the actual \(Ub=1\). The candidate value \(f=0\) still satisfies (2), and \(c=(0,1)^{\mathsf T}\) even has exact norm \(1\) and solves \(Uc=0\). It is not the prescribed \(b\).

| Further control | Outcome |
|---|---|
| \(k=1\) | The chain reduces to \(b^*Mb=\|Ub\|^2\), and the moment inequality is an identity. |
| \(B=0\) | Necessarily \(b=f=0\), all \(a_k=0\), and a positive high-value condition on a nonempty row set is impossible. |
| \(U=0\), \(B>0\) | \(G=M=0\), \(f=0\), all \(a_k=0\), \(\tau=0\), and the border is \(\operatorname{diag}(B,0)\). |
| Nonzero \(b\in\ker U\) | The moment inequality is an equality at zero. The whole norm \(B\) lies in the nullspace slack in (22). |
| Repeated or zero eigenvalues | The spectral proof uses orthogonal eigenspaces and includes zero spectral mass. No inverse or division by an eigenvalue zero occurs. |
| Positive-level equality | A one-eigenvalue coefficient vector gives equality in the moment step; equality in the full high-value chain additionally requires every \(|f_j|=v\). |
| Generic norm loses orientation | For \(M=\operatorname{diag}(L,0)\), the two norm-\(\sqrt B\) vectors supported respectively on the first and second coordinates give \(a_k=BL^k\) and \(a_k=0\). A bound depending only on \(B,\|G\|\) does not distinguish them. |
| Invertible \(G\) | The range condition is automatic and \(G^\dagger=G^{-1}\), recovering the usual completed-square Schur complement. |
| Full column rank of \(U\) | \(\ker U=0\), so the actual \(b\) is always the minimum-norm preimage. For independently specified data, PSD still expresses a norm budget rather than a claim of exact prescribed norm. |
| Zero column weights \(\mu_\nu\) | They give zero columns of \(U\); a coefficient supported there lies in \(\ker U\). The same zero and slack formulas apply. |
| Empty dimensions, if admitted | Empty sums are zero. The bordered criterion reduces to \(B\geq0\) when there are no rows; no high-value consequence divides by \(J=0\). |

All controls are exact finite algebra. No experiment or numerical evaluation was performed.

## 6. Dependencies and isolation provenance

- Campaign: gc-actual-vector-gram-correlations, round221.
- Task: blind_anchored_gram; current statement-only finite derivation.
- Generated date: 2026-09-28, the supplied session date.
- Only context files read for this assignment:
  - protocol.md, SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
  - rounds/codex-managed/gc-actual-vector-gram-correlations/briefs/blind_anchored_gram_statement.md, SHA256 5e15f8516a2a9c00f278588f59e8f2c0644fbf296bdab383fdfe01e0976389d9.
- No graph hash was supplied in the packet. No generated brief, active campaign, graph, strategy, application, source, or sibling was read.
- Mathematical dependencies: finite matrix multiplication, finite Hermitian spectral decomposition, convexity on \([0,\infty)\), orthogonal kernel/range decompositions, completion of the square, and Cauchy--Schwarz.
- No web access, experiment, new agent, shared edit, or successor work was used. Only the assigned report was written.

**Prior-history disclosure.** This reused agent retains round217--220 research and review context, including its own earlier abstract finite and operator derivations. It is not a fresh history-free agent. This round221 lemma was supplied and solved statement-only: no current claimant derivation or application was inspected, and no previous artifact was reread for this task.

## 7. Recommended state effect

**Recommend promote only the exact finite chain, sharp moment inequality, bordered PSD/preimage characterization, and translation controls, subject to the conductor's normal verification procedures.**

Retain the fixed coefficient vector as part of the mathematical interface. Bordered positivity and all-vector spectral bounds do not replace an estimate for its anchored correlations, and translation invariance of the row Gram does not remove its absolute phases.

No analytic bound, arithmetic conclusion, graph mutation, synthesis, or next-round decision is made. The assigned report ends here.

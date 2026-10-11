# Round222 isolated cross-modulus correlation report

## 1. Result

**GREEN for the exact finite identities and the narrowly scoped near-frequency control.**

For \(L=\operatorname{lcm}(q,r)\), the complete correlation is
\[
 \boxed{\sum_{h=0}^{L-1}S(A,h;q)\overline{S(B,h;r)}
 =\begin{cases}
 0,&q\ne r,\\
 q\,c_q(A-B),&q=r,
 \end{cases}}
 \tag{1}
\]
where \(c_q(k)=\sum_{z\bmod q,\ (z,q)=1}e(kz/q)\). No coprimality assumption on either first argument is needed.

Weighted or incomplete windows instead retain the exact frequency-difference transform below. For the specified distinct odd moduli \(q,q+2\), their two simple unit-frequency rows have zero complete inner product but short-window inner product of magnitude at least \(2H/\pi\) when \(1\le H\le qr/4\). This lower bound concerns those two rows only, not complete Kloosterman sums or an unspecified arithmetic vector.

Constant unit-modulus row factors preserve the Gram spectrum and all-vector norm. That fact supplies no cancellation estimate for a prescribed vector of row coefficients.

## 2. Exact hypotheses and conventions

Let \(e(t)=\exp(2\pi it)\), \(q,r\ge2\) be integers, and \(A,B\in\mathbb Z\). All sums over \(h\) below are over integers. For units \(x\bmod q\), choose any integer inverse \(\bar x\) with \(x\bar x\equiv1\pmod q\), and define
\[
 S(A,h;q)=\sum_{x\bmod q}^{*}e(A\bar x/q+hx/q).
\]
The star restricts to units. Set \(D_w(t)=\sum_h w(h)e(ht)\) for any finitely supported complex sequence \(w\).

A shifted interval is \(I_{m,H}=\{m,m+1,\ldots,m+H-1\}\), where \(m\in\mathbb Z\), \(H\in\mathbb Z_{\ge0}\); it is empty when \(H=0\). Write \(\|t\|\) for distance to the nearest integer. A complex weighted correlation need not be a positive semidefinite Gram form. The unweighted two-row Gram matrix considered below is one.

## 3. Proof and derivation

**Complete common period.** Finite expansion gives
\[
 \sum_{h=0}^{L-1}S(A,h;q)\overline{S(B,h;r)}
 =\sum_{x\bmod q}^{*}\sum_{y\bmod r}^{*}
 e(A\bar x/q-B\bar y/r)
 \sum_{h=0}^{L-1}e(h(x/q-y/r)).
 \tag{2}
\]
Since \(L(x/q-y/r)\in\mathbb Z\), the inner sum equals \(L\) if \(x/q-y/r\in\mathbb Z\), and zero otherwise.

Choose representatives \(1\le x<q\), \(1\le y<r\). Their fractions lie in \((0,1)\) and are reduced, so equality modulo one requires \(x/q=y/r\), hence \(q=r\) and \(x=y\). Equivalently, a unit fraction modulo one has exact additive order its denominator. For equal moduli, inversion permutes the units and (2) becomes \(q c_q(A-B)\), proving (1).

Replacing \(\bar x\) by \(\bar x+kq\) multiplies its summand by \(e(Ak)=1\). Changing a unit representative also changes its frequency by an integer, invisible at integer \(h\). Thus arbitrary representatives and nonprimitive \(A,B\) cause no exception. The same complete identity holds on every shifted interval of length \(L\).

**Arbitrary weights and row weights.** Direct expansion, without any orthogonality assertion, gives
\[
 \boxed{
 \sum_h w(h)S(A,h;q)\overline{S(B,h;r)}
 =\sum_x^{*}\sum_y^{*}
 e(A\bar x/q-B\bar y/r)D_w(x/q-y/r).}
 \tag{3}
\]
For separately prescribed row weights \(u_q(h),v_r(h)\), replace \(D_w\) by
\[
 D_{\,w u_q\overline{v_r}}.
 \tag{4}
\]
Finite support of \(w\) suffices; alternatively the entire product in (4) may be finitely supported.

Even if \(w\) selects a complete common period, the product \(u_q\overline{v_r}\) need not be constant there, so its transform need not vanish at nonzero common-period frequencies. Orthogonality is therefore not preserved automatically. For an exact counterexample, take \(q=3,r=5,A=B=0\), the complete interval \(0\le h<15\), \(u_q(h)=\mathbf1_{\{h=0\}}\), and \(v_r(h)=1\). The weighted correlation equals \(\varphi(3)\varphi(5)=8\), whereas (1) is zero. Taking \(w=\mathbf1_{\{0\}}\) gives the same incomplete-window example.

**Exact interval transform.** Let \(D_{m,H}=D_{\mathbf1_{I_{m,H}}}\). For \(H=0\) it vanishes identically. For \(H\ge1\),
\[
 D_{m,H}(t)=
 \begin{cases}
 H,&t\in\mathbb Z,\\[2mm]
 e(mt)\dfrac{1-e(Ht)}{1-e(t)}
 =e((m+(H-1)/2)t)\dfrac{\sin(\pi Ht)}{\sin(\pi t)},
 &t\notin\mathbb Z .
 \end{cases}
 \tag{5}
\]
The triangle inequality gives \(H\); the geometric quotient gives
\[
 |D_{m,H}(t)|\le \frac1{|\sin(\pi t)|}
 \le \frac1{2\|t\|}\quad(t\notin\mathbb Z).
\]
Consequently
\[
 |D_{m,H}(t)|\le\min\{H,(2\|t\|)^{-1}\},
 \tag{6}
\]
with absolute constant one, interpreting the second entry as infinity at integral \(t\). Formula (3) with (5) retains every weighted zero and nonzero frequency; the zero-frequency contribution must not be discarded.

**Odd near-frequency control.** Let \(q\ge3\) be odd, \(r=q+2\), \(x=(q+1)/2\), \(y=(r+1)/2\). Then
\[
 (q,r)=(q,2)=1,\quad 2x-q=2y-r=1,
 \quad (x,q)=(y,r)=1,
\]
\[
 t=\frac{x}{q}-\frac{y}{r}
 =\frac1{2q}-\frac1{2r}=\frac1{qr}.
 \tag{7}
\]
For the simple rows \(f(h)=e(hx/q)\), \(g(h)=e(hy/r)\),
\[
 \langle f,g\rangle_{I_{m,H}}
 :=\sum_{h\in I_{m,H}}f(h)\overline{g(h)}
 =D_{m,H}(1/(qr)).
 \tag{8}
\]
Over a complete period \(H=qr=L\), this is zero for every shift \(m\), and both squared row norms equal \(L\).

If \(1\le H\le L/4\), then \(\sin(\pi H/L)\ge2H/L\) and \(\sin(\pi/L)\le\pi/L\). Hence
\[
 \boxed{|\langle f,g\rangle_{I_{m,H}}|
 =\frac{\sin(\pi H/L)}{\sin(\pi/L)}
 \ge\frac2\pi H.}
 \tag{9}
\]
The surviving fraction is a magnitude statement, uniform in the interval shift; the complex phase can rotate with \(m\). These frequencies are individual unit terms. A lower bound for one such pair does not lower-bound the sum of all signed pairs in (3).

**Row twists and operator scope.** Let \(F\) be the matrix with these two rows on the interval. With \(C=D_{m,H}(t)\),
\[
 G=FF^*=\begin{pmatrix}H&C\\\overline C&H\end{pmatrix},
 \qquad \operatorname{spec}(G)=\{H+|C|,H-|C|\},
 \qquad \|F\|_{2\to2}^2=H+|C|.
 \tag{10}
\]
Multiplying the rows by fixed \(|\sigma_1|=|\sigma_2|=1\) gives \(F'=DF\), \(D=\operatorname{diag}(\sigma_1,\sigma_2)\), and \(G'=DGD^*\). Spectrum and operator norm are unchanged. But for prescribed row coefficients \(a\),
\[
 \|(F')^*a\|^2=a^*G'a=(D^*a)^*G(D^*a),
 \tag{11}
\]
which depends on their orientation, not just the spectrum. For \(H=1,m=0\), take \(a=(1,1)/\sqrt2\). Originally (11) is \(2\); after the row sign change \(D=\operatorname{diag}(1,-1)\), it is zero, although the all-vector norm stays \(\sqrt2\).

For clarity, a fixed column vector \(z\) does satisfy \(\|F'z\|=\|Fz\|\): the distinction in (11) concerns specified coefficients across rows. Neither norm fact estimates a separately specified signed arithmetic combination.

Factors depending on both row and \(h\) are not this single left unitary. For example, multiplying \(f(h),g(h)\) respectively by \(e(-hx/q),e(-hy/r)\) makes both rows identically one. On a full period their Gram eigenvalues change from \(L,L\) to \(2L,0\). Thus row-dependent varying weights and constant row signs must be distinguished.

## 4. First unsupported application step

The finite statements above have no remaining gap. Unsupported extensions would be: treating (3) or (4) as complete-period orthogonality without checking the weight transform; transferring (9) from simple terms to full Kloosterman rows; or inferring cancellation for a prescribed coefficient vector from the row-twist invariance of an all-vector norm. No such arithmetic conclusion is supplied by this packet.

## 5. Required controls and outcomes

| Control | Exact outcome |
|---|---|
| Nonprimitive \(A,B\), including zero | Formula (1) is unchanged; primitive first arguments were never used. |
| Equal moduli | The correlation is \(q c_q(A-B)\), not automatically zero. For \(A=B\bmod q\), it is \(q\varphi(q)\). |
| Repeated identical rows | Full correlation equals the row norm squared; no distinct-row orthogonality is inferred. |
| Equal moduli, distinct unit frequencies | Simple rows are orthogonal over a full period; equal frequencies instead give that period's length. |
| Empty window | Every correlation and Gram entry is zero, and the operator norm is zero. |
| \(H=1\) | \(D_{m,1}(t)=e(mt)\); for the two unit rows, Gram eigenvalues are \(2,0\). |
| Zero frequency | Equation (5) gives \(H\), including all integral frequency differences. |
| Shifted windows | Only the displayed phase changes; the short-window magnitude bound persists. |
| Distinct odd moduli | Equation (7) proves coprimality and unit status exactly; no even-modulus exception is used. |
| Prescribed row signs | They preserve spectrum, while the fixed-row-coefficient example in (11) exhibits the missing orientation information. |

Every control is finite algebra. No experiment or numerical evaluation was performed.

## 6. Dependencies and statement-only provenance

Campaign: m9-m2-complete-unbalanced-vector, round222. Task: blind_cross_modulus. Date: 2026-09-28. No graph hash was supplied or read. Only these files were read:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/briefs/blind_cross_modulus_statement.md | a91629290c8964e84e08bf7999dfd85fdb10baf189bd515ba509be8631983f8e |

Dependencies are finite expansion, reduced fractions, a geometric progression, elementary sine inequalities and unitary similarity. No external theorem, application, generated brief, graph, manifest, strategy, source or sibling was accessed.

**Reused-agent disclosure:** this agent retains its rounds217--221 research and review history. It is not history-free. Access for this new lemma was statement-only; no current claimant derivation or application was supplied or inspected. Only this assigned report was written. No web, experiment, new agent, shared edit, old-file edit or successor work occurred.

## 7. Recommended state effect

**Recommend retain or promote only the proved finite common-period identity, weighted-window identities, simple-row near-frequency control and row-twist distinction, subject to conductor verification.**

Do not promote an arithmetic vector estimate, an actual Kloosterman lower bound, a complete M9-M2 assertion or the quarter goal from these facts alone. No direct state change is made. This bounded report ends here.

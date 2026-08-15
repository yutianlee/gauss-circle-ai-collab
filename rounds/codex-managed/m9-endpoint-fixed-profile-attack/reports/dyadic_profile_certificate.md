# Dyadic and endpoint profile certificate

## 1. Result

There is an explicit nonnegative partition of the actual finite denominator range

\[
\{1,\ldots,y\},\qquad y=\lfloor X^{1/2}\rfloor,
\]

with the following properties.

1. Every block is supported in one fixed multiplicative shell and has
   \[
   \|w_D\|_\infty+
   \sum_{d\in\mathbb Z}|w_D(d+1)-w_D(d)|\le4. \tag{1.1}
   \]
2. Every active block \(D\ge X^{1/4}\), including the final block ending at \(y\), satisfies for \(X\ge4096\)
   \[
   \sum_{d=1}^{y}|w_D(d)|\ge\frac D8. \tag{1.2}
   \]
3. With the explicit rounding
   \[
   H_D=\left\lfloor DX^{-1/4}\right\rfloor, \tag{1.3}
   \]
   every active block has \(H_D\ge1\) and
   \[
   \frac12DX^{-1/4}\le H_D\le DX^{-1/4}. \tag{1.4}
   \]
4. Every non-endpoint active block is a full fixed \(C_c^\infty\) rescaling and therefore satisfies the hypotheses of the accepted Round-5 Poisson transform.
5. The final block is an explicitly truncated fixed profile. It still satisfies uniform discrete BV, TTY transfer, B1, Fejer, and sampled-\(\ell^1\) hypotheses, but it is not a full smooth rescaling on the whole integer line. Consequently the existing smooth Poisson identity is unconditional for all interior blocks but remains unproved for the final endpoint block.

Thus the normalization blocker is removed for the TTY wedge, B1, and the W-1 weighted obstruction for this chosen decomposition. It is only partially removed for Poisson duality: the hard endpoint profile remains a separate transform seam.

## 2. Explicit fixed cutoff and profiles

Define

\[
\rho(u)=
\begin{cases}
0,&u\le0,\\
e^{-1/u},&u>0,
\end{cases}
\]

and the standard decreasing smooth step

\[
q(u)=\frac{\rho(1-u)}{\rho(u)+\rho(1-u)}.
\]

Then \(q\in C^\infty(\mathbb R)\), \(0\le q\le1\), \(q(u)=1\) for \(u\le0\), \(q(u)=0\) for \(u\ge1\), and \(q\) is nonincreasing. Put

\[
\eta(t)=q(2(t-1)). \tag{2.1}
\]

Hence

\[
\eta(t)=1\quad(t\le1),\qquad
\eta(t)=0\quad(t\ge3/2),\qquad
0\le\eta\le1, \tag{2.2}
\]

and \(\eta\) is fixed, smooth, and nonincreasing. Define the fixed band profile

\[
W(t)=\eta(t)-\eta(2t). \tag{2.3}
\]

Then

\[
W\in C_c^\infty((0,\infty)),\qquad
0\le W\le1,\qquad
\operatorname{supp}W\subset[1/2,3/2]. \tag{2.4}
\]

Moreover,

\[
W(t)=1\qquad(3/4\le t\le1), \tag{2.5}
\]

because \(\eta(t)=1\) there and \(\eta(2t)=0\).

Let

\[
J=\lceil\log_2 y\rceil,\qquad
D_j=2^{-j}y\quad(0\le j\le J). \tag{2.6}
\]

Thus \(1/2<D_J\le1\) when \(y>1\). For \(0\le j<J\), define on the actual denominator set

\[
w_j(d)=
\begin{cases}
W(d/D_j),&1\le d\le y,\\
0,&\text{otherwise}.
\end{cases} \tag{2.7}
\]

Define the bottom remainder

\[
w_{\rm bot}(d)=
\begin{cases}
\eta(d/D_J),&1\le d\le y,\\
0,&\text{otherwise}.
\end{cases} \tag{2.8}
\]

For \(1\le d\le y\), telescoping gives

\[
\begin{aligned}
\sum_{j=0}^{J-1}w_j(d)+w_{\rm bot}(d)
&=\sum_{j=0}^{J-1}
\left[
\eta\!\left(\frac{2^jd}{y}\right)
-\eta\!\left(\frac{2^{j+1}d}{y}\right)
\right]
+\eta\!\left(\frac{2^Jd}{y}\right)\\
&=\eta(d/y)=1. 
\end{aligned} \tag{2.9}
\]

Thus (2.7)--(2.8) are an exact nonnegative partition of unity on the finite integer range. There are \(J+1=O(\log X)\) blocks.

The top block is

\[
w_{\rm end}(d)=w_0(d)
=W(d/y)\mathbf1_{1\le d\le y}. \tag{2.10}
\]

It is the explicit endpoint truncation. Since \(W(1)=1\), it includes \(d=y\) rather than losing the final integer.

For every \(j\ge1\),

\[
\operatorname{supp}W(d/D_j)
\subset[D_j/2,3D_j/2]
\subset(0,3y/4]\subset[1,y]. \tag{2.11}
\]

Therefore the restriction \(d\le y\) in (2.7) is inactive for \(j\ge1\): these are full smooth fixed-profile sums. Only \(j=0\) is endpoint-truncated.

## 3. Uniform upper-bound norms

### 3.1 Fixed smooth blocks

Since \(\eta\) is monotone from \(1\) to \(0\),

\[
\operatorname{Var}_{\mathbb R}(\eta)=1.
\]

Rescaling preserves total variation, so

\[
\operatorname{Var}_{\mathbb R}(W)
\le
\operatorname{Var}(\eta)+\operatorname{Var}(\eta(2\cdot))
=2. \tag{3.1}
\]

For \(j\ge1\), ordered sampling cannot increase total variation. Hence

\[
\sum_{d\in\mathbb Z}
|W((d+1)/D_j)-W(d/D_j)|
\le2, \tag{3.2}
\]

and \(\|w_j\|_\infty\le1\). Thus the left side of (1.1) is at most \(3\) for every full smooth block.

More generally, for each derivative order \(r\ge0\),

\[
\left\|\frac{d^r}{dt^r}W(t/D_j)\right\|_\infty
=D_j^{-r}\|W^{(r)}\|_\infty. \tag{3.3}
\]

All constants depend only on the one fixed function \(W\), not on \(X,j\), or \(D_j\).

### 3.2 Endpoint block

On \(d\le y\), the sampled variation of \(W(d/y)\) is at most \(2\). Extending the sequence by zero past \(y\) adds the single jump

\[
|w_{\rm end}(y+1)-w_{\rm end}(y)|=W(1)=1.
\]

There is no lower-end jump because \(W(t)=0\) for \(t\le1/2\). Therefore

\[
\sum_{d\in\mathbb Z}
|w_{\rm end}(d+1)-w_{\rm end}(d)|
\le3,\qquad
\|w_{\rm end}\|_\infty=1. \tag{3.4}
\]

This proves (1.1) for the endpoint block with constant \(4\).

### 3.3 Bottom remainder

The positive sampled values of \(w_{\rm bot}\) form a nonincreasing sequence. Extension by zero to \(d\le0\) contributes at most one initial jump, and the subsequent decrease contributes at most one. Thus

\[
\|w_{\rm bot}\|_\infty+
\sum_d|w_{\rm bot}(d+1)-w_{\rm bot}(d)|
\le3. \tag{3.5}
\]

This block has scale \(D_J\le1\) and is never active.

### 3.4 Restricted lattices

If \(d_0<d_1<\cdots<d_m\) is any subsequence of integers, then

\[
\sum_{r=0}^{m-1}|w(d_{r+1})-w(d_r)|
\le
\sum_{d\in\mathbb Z}|w(d+1)-w(d)|. \tag{3.6}
\]

Consequently (1.1) gives uniform BV on every sampled \(q\)-lattice and every odd-lift subsequence \(d=gq\). This is the exact weight input needed by the accepted B1 Abel-summation lemma; no extra smoothness assumption is required there.

## 4. Sampled \(\ell^1\) nondegeneracy and \(H_D\)

Declare \(w_j\) active precisely when

\[
D_j\ge X^{1/4}. \tag{4.1}
\]

All remaining \(w_j\), together with \(w_{\rm bot}\), are handled before Fourier expansion. Their union is supported on \(d\ll X^{1/4}\): if \(D_j<X^{1/4}\), then \(w_j\) is supported below \(3D_j/2<3X^{1/4}/2\). Since the weights are nonnegative and sum to one, the total short-range contribution is \(O(X^{1/4})\).

For every active block, define \(H_D\) by (1.3). Since \(DX^{-1/4}\ge1\),

\[
H_D\ge1. \tag{4.2}
\]

For every \(z\ge1\), \(\lfloor z\rfloor\ge z/2\); this gives (1.4). Thus the Fejer scale remains uniformly comparable:

\[
X^{1/4}\le\frac D{H_D}\le2X^{1/4}. \tag{4.3}
\]

Now use the plateau (2.5). For every active interior block,

\[
w_j(d)=1
\qquad
\left(\frac{3D_j}{4}\le d\le D_j\right). \tag{4.4}
\]

The same is true for the endpoint block, and the whole interval in (4.4) lies below \(y=D_0\). Therefore

\[
\begin{aligned}
\sum_{d=1}^{y}|w_j(d)|
&\ge
\#\left([3D_j/4,D_j]\cap\mathbb Z\right)\\
&\ge D_j/4-1.
\end{aligned} \tag{4.5}
\]

If \(D_j\ge8\), then

\[
\sum_d|w_j(d)|\ge D_j/8. \tag{4.6}
\]

For \(X\ge4096\), every active \(D_j\ge X^{1/4}\) is at least \(8\), proving (1.2) with the uniform constant

\[
\lambda=\frac18. \tag{4.7}
\]

The finitely many smaller \(X\) may be absorbed into the final theorem constant. No W-1 lower-bound claim is made for inactive blocks or for \(w_{\rm bot}\).

Every active block is supported in the common shell

\[
[D_j/2,3D_j/2], \tag{4.8}
\]

while the endpoint block has the smaller actual support \([D_0/2,D_0]\). Thus the W-1 transfer may use the fixed shell constants \(a=1/2\), \(b=3/2\), \(\lambda=1/8\), and \(\|w_j\|_\infty\le1\), uniformly over all active blocks.

This proves sampled nondegeneracy directly. It is logically separate from the upper-bound BV estimates in Section 3: the BV argument would also hold for a scale-degenerate profile, whereas (4.5) uses the explicit unit plateau of \(W\).

## 5. Compatibility with accepted analytic transfers

### 5.1 Tao--Trudgian--Yang weighted transfer

The Round-5 transfer requires

\[
\sup_d|w_D(d)|
+\sum_d|w_D(d+1)-w_D(d)|\ll1.
\]

Equations (3.2), (3.4), and (3.5) prove this for every actual block, including the final endpoint truncation. If the primary theorem is stated on a standard shell \([N,2N]\), the fixed shell \([D/2,3D/2]\) is split into at most two overlapping standard shells using one fixed smooth subdivision; each subweight retains a uniform discrete BV norm. Partial summation then transfers the unweighted theorem with an absolute number of pieces.

Therefore the certified TTY estimate and its wedge

\[
178\ell+1638\delta\le463 \tag{5.1}
\]

apply unconditionally to every active block of this explicit decomposition, including \(w_{\rm end}\).

### 5.2 Round-5 smooth Poisson transform

For every \(j\ge1\), equation (2.11) shows that the actual finite sum equals the full smooth sum

\[
\sum_{d\in\mathbb Z}W(d/D_j)e\!\left(\frac{hX}{4d}\right), \tag{5.2}
\]

with the harmless convention that the profile vanishes near \(d=0\). The one fixed profile satisfies

\[
W\in C_c^\infty((a,b))
\]

for any fixed \(a<1/2<3/2<b\), and (3.3) supplies every scale-normalized derivative bound. Thus all non-endpoint active blocks meet the hypotheses of the accepted Poisson and stationary-phase formula, with constants independent of \(j,D_j,X\).

The endpoint block is instead

\[
\sum_{d\le y}W(d/y)e\!\left(\frac{hX}{4d}\right). \tag{5.3}
\]

As a sequence it has normalized discrete BV, but as a continuum profile it is \(W(t)\mathbf1_{t\le1}\), which jumps at \(t=1\) because \(W(1)=1\). It is not in \(C_c^\infty\), so the existing smooth Poisson formula cannot be applied to (5.3) without a new endpoint transform or an explicit boundary term. Merging it with \(w_1\) does not remove the hard endpoint \(d\le y\).

This limitation is structural for an exact finite partition: a sum of globally smooth continuum profiles cannot equal the discontinuous cutoff \(\mathbf1_{d\le y}\) as a continuum identity. The present construction places the entire issue in one normalized endpoint block rather than hiding it in every dyadic scale.

### 5.3 Other accepted transfers

- **B1 signed lift:** unconditional for every active block by (3.6).
- **W-1 absolute weighted obstruction:** unconditional for every active block by (4.2), (4.6), and (4.8), with \(\lambda=1/8\).
- **Fejer residual product count:** boundedness and fixed-shell support hold for every block; the explicit \(H_D\) gives (4.3).
- **T2S terminal estimate:** it needs only bounded denominator weights, so it applies to every block.
- **Exact-\(N=0\) absolute mass modules:** their bounded-weight hypothesis holds with norm \(1\).

## 6. Endpoint, partition, and norm controls

### Endpoint-truncation control

- **Input:** \(D_0=y\), \(w_{\rm end}(d)=W(d/y)\mathbf1_{d\le y}\), and \(W(1)=1\).
- **Expected invariant:** the final integer is covered, BV remains uniform, and lower mass is of order \(y\).
- **Outcome:** \(w_{\rm end}(y)=1\), (3.4) gives BV at most \(3\), and (4.5) gives sampled mass at least \(y/4-1\).
- **Implication:** the endpoint is neither omitted nor a vanishing sliver. Its only unresolved property is smooth-Poisson compatibility.

### Partition-of-unity control

- **Input:** the exact telescoping weights (2.7)--(2.8).
- **Expected invariant:** no gap or overlap error on any integer \(1\le d\le y\).
- **Outcome:** equation (2.9) is an exact identity and every weight is nonnegative.
- **Implication:** the original denominator sum is exactly the sum of these blocks.

### Uniform-BV control

- **Input:** full smooth blocks, the endpoint jump, the bottom remainder, and arbitrary restricted lattices.
- **Expected invariant:** one scale-independent variation constant.
- **Outcome:** (3.2), (3.4), (3.5), and (3.6) give the common bound (1.1).
- **Implication:** TTY partial summation and B1 use actual verified weights, not a generic “bounded smooth” phrase.

### Sampled-\(\ell^1\) control

- **Input:** every active original block on which W-1 is invoked.
- **Expected invariant:** \(\sum_d|w_D(d)|\ge\lambda D\) and \(H_D\ge1\).
- **Outcome:** (4.2) and (4.6) give \(\lambda=1/8\) for \(X\ge4096\), including the endpoint block.
- **Implication:** the weighted W-1 obstruction transfers to every active block of this decomposition. No such claim is made for inactive or bottom blocks.

No numerical experiment was used.

## 7. First remaining seam

The first remaining normalization seam is the endpoint Poisson transform for (5.3). The existing smooth formula is now fully applicable to every interior active block, but it does not cover the hard final endpoint. A future proof must either:

1. derive Poisson/stationary phase with the explicit boundary contribution at \(d=y\);
2. estimate the endpoint block directly through its fixed one-sided profile; or
3. redesign the arithmetic reduction so a smooth extension past \(y\) is paired with an explicitly controlled correction.

This is not a BV or nondegeneracy problem: the endpoint block already has both properties uniformly.

## 8. Dependencies and recommended state effect

### Exact artifacts used

- rounds/codex-managed/m9-endpoint-fixed-profile-attack/briefs/dyadic_profile_certificate.md.
- rounds/codex-managed/m9-endpoint-fixed-profile-attack/plan.json.
- state/best_proof_draft.md.
- state/proof_obligations.yml.
- rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md.
- rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md.

### Recommended state effect

**Promote the explicit infrastructure after conductor validation:** the profiles (2.1)--(2.8), exact partition (2.9), common discrete-BV certificate (1.1), active-block sampled lower bound (1.2), and integer height rule (1.3)--(1.4).

For this chosen decomposition:

- remove the profile-normalization blocker from the TTY wedge, B1, Fejer transfer, and the weighted W-1 obstruction;
- remove the smooth-profile blocker from Poisson duality for every interior active block;
- retain one endpoint-specific blocker for applying the existing smooth Poisson identity to \(w_{\rm end}\).

No M2 endpoint exponential-sum estimate, signed corridor estimate, or final Gauss-circle theorem is claimed.

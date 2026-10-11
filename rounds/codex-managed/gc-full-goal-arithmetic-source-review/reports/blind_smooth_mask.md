# Round220 isolated smooth-phase and interval-mask lemma

## 1. Result

**Verdict: GREEN for the stated multiplier bound under the all-row-vector hypothesis.**

Put \(\kappa=K/A\). For real residual phase parameters \(\delta_i\), the following slightly more general bound holds:

\[
 \boxed{
 \left|\sum_{i,k}u_iv_kH(i,k)M(i,k)\right|
 \leq C S B(1+\kappa)(1+\log(2+n))
       \|u\|_2\|v\|_2,
 }
 \tag{1}
\]

where \(C\) is absolute. In particular \(\kappa\leq1\) proves exactly the proposed estimate, with an absolute constant.

The proof supplies an exact, uniformly absolutely summable product decomposition of the smooth factor and an exact finite product decomposition of the row-dependent interval mask. It requires no regularity in the row index.

The residual phase remains in the identity. Its multiplier norm is controlled; it is not literally deleted. A theorem known only for internal row products \(u_{j,a}=x_jy_a\) cannot be substituted for the hypothesis here. Section 5 gives a finite family refuting that unsupported upgrade, even with a constant-in-\(t\) smooth multiplier and no residual phase.

If the packet's bound on \(\delta_i\) is interpreted as allowing complex values, the claimed \(\kappa\leq1\) result remains true. An explicit controlled extension in that interpretation replaces \(1+\kappa\) in (1) by \(e^{3\pi\kappa}(1+\kappa)\). The linear extension in (1) uses real phases.

## 2. Exact hypotheses and notation

Let \(I\) be any finite row set. Write the ordered column set as

\[
 \mathcal C=\{k_1<\cdots<k_n\}
 =\{k\in\mathbb Z_{>0}:K/2\leq k<2K\},\qquad K\geq1.
 \tag{2}
\]

Thus \(n\geq1\) and \(k/K\in[1/2,2)\). The given bound is

\[
 \left|\sum_{i\in I,k\in\mathcal C}u_iv_kH(i,k)\right|
 \leq B\|u\|_2\|v\|_2
 \quad\hbox{for every }u\in\mathbb C^I,\ v\in\mathbb C^{\mathcal C}.
 \tag{3}
\]

No further factorization is imposed on the entries of \(u\), even if \(i\) itself is a tuple. Complex bilinear products rather than sesquilinear products cause no difficulty: (3) is assumed for every complex pair of vectors, and the proof applies it directly.

For every row, \(a_i\geq A>0\), \(|\delta_i|\leq1/2\), and

\[
 \max_{0\leq r\leq2}\|f_i^{(r)}\|_{L^\infty([1/4,3])}\leq S.
 \tag{4}
\]

The functions may be complex. Write \(w_i(s)\), \(1\leq s\leq n\), for the interval mask in column-rank coordinates. It is zero outside one interval, one in its interior, and may have endpoint weights in \([0,1]\). This slightly enlarged convention includes ordinary endpoints, half-weight endpoints, singleton conventions, and empty intervals.

The desired exact multiplier is

\[
 M(i,k_s)=w_i(s)f_i(k_s/K)e(\delta_i k_s/a_i),
 \qquad e(x)=\exp(2\pi i x).
 \tag{5}
\]

Only the two derivatives in (4) are needed. All other cutoffs used below are fixed once and for all, so their derivative bounds are absolute constants.

## 3. Exact decomposition and proof

### Product multipliers under the given norm

For arbitrary bounded row and column factors \(r_i,t_k\), (3), applied to \(r_iu_i\) and \(t_kv_k\), gives

\[
 \left|\sum_{i,k}u_iv_k r_it_kH(i,k)\right|
 \leq B\|r\|_\infty\|t\|_\infty\|u\|_2\|v\|_2.
 \tag{6}
\]

Therefore any exact decomposition
\(M(i,k)=\sum_\nu r_\nu(i)t_\nu(k)\)
with
\(\sum_\nu\|r_\nu\|_\infty\|t_\nu\|_\infty<\infty\)
transfers (3) with that sum as its multiplier cost. This elementary observation is where availability of all row vectors is used.

### Exact Fourier products for the smooth residual factor

Fix a real smooth cutoff \(\eta\), supported inside \((1/4,3)\), equal to one on \([1/2,2]\), with bounded derivatives. Define

\[
 \alpha_i=\delta_i K/a_i,\qquad |\alpha_i|\leq\kappa/2,
 \tag{7}
\]

and on \([0,4]\) set

\[
 g_i(t)=
 \begin{cases}
 \eta(t)f_i(t)e(\alpha_i t),&1/4\leq t\leq3,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{8}
\]

Extend \(g_i\) with period \(4\). Because \(\eta\) vanishes on neighborhoods of the endpoints of its support, this is a \(C^2\) periodic function; no boundary matching condition on \(f_i\) is needed.

For real \(\alpha_i\), the product rule gives, uniformly in the row,

\[
 \|g_i\|_\infty\leq C S,\qquad
 \|g_i''\|_\infty\leq C S(1+\kappa)^2.
 \tag{9}
\]

Define the explicit Fourier coefficients

\[
 c_i(m)=\frac14\int_0^4g_i(t)e(-mt/4)\,dt,\qquad m\in\mathbb Z.
 \tag{10}
\]

The direct integral bound and two integrations by parts, with zero periodic boundary terms, give

\[
 \sup_i|c_i(m)|
 \leq C S\min\left(1,\frac{(1+\kappa)^2}{m^2}\right)
 \quad(m\ne0),\qquad
 \sup_i|c_i(0)|\leq C S.
 \tag{11}
\]

Splitting the integers at \(|m|\asymp1+\kappa\), the central part has \(O(1+\kappa)\) terms and the tail is a reciprocal-square series. Hence

\[
 \boxed{\sum_{m\in\mathbb Z}\sup_i|c_i(m)|
            \leq C S(1+\kappa).}
 \tag{12}
\]

The Fourier series is absolutely and uniformly convergent, uniformly across all rows. It equals \(g_i\): for example, the Fejér averages converge uniformly to a continuous periodic function, while absolute convergence makes their limit the ordinary Fourier sum. The standard approximate-identity assertion here follows immediately by splitting the Fejér-kernel integral into a small neighborhood, where uniform continuity applies, and its complement, where the kernel mass tends to zero.

At the actual columns \(\eta(k/K)=1\), and consequently the required explicit decomposition is

\[
 \boxed{
 f_i(k/K)e(\delta_i k/a_i)
  =\sum_{m\in\mathbb Z}c_i(m)e(mk/(4K)).
 }
 \tag{13}
\]

Each summand is a row factor times a column factor of modulus one. The cost (12) is uniform despite arbitrary dependence of \(a_i,\delta_i,f_i\) on the row.

If complex \(\delta_i\) are admitted, (8) has
\(|e(\alpha_i t)|\leq e^{3\pi\kappa}\)
on the cutoff support. The same proof multiplies the right sides of (9)--(12) by this factor. This proves the controlled complex-parameter variant stated in section 1, and still gives an absolute constant when \(\kappa\leq1\).

### An exact finite Fourier decomposition of every prefix

Set \(N=2n+1\) and define on the cyclic group \(\mathbb Z/N\mathbb Z\)

\[
 h(s)=\mathbf1_{\{0,\ldots,n-1\}}(s),\qquad
 \widehat h(r)=\frac1N\sum_{s=0}^{n-1}e(-rs/N),
 \quad 0\leq r<N.
 \tag{14}
\]

For \(0\leq t\leq n\) and \(1\leq s\leq n\), the integer \(t-s\) lies in \([-n,n-1]\). Thus no erroneous positive branch appears on reducing modulo \(N\), and

\[
 P_t(s):=\mathbf1_{\{s\leq t\}}
 =h(t-s)
 =\sum_{r=0}^{N-1}\widehat h(r)e(rt/N)e(-rs/N).
 \tag{15}
\]

This includes the empty prefix \(P_0=0\) and the full prefix \(P_n=1\).

The finite geometric sum gives \(\widehat h(0)=n/N\). For \(r\ne0\), with \(d_r=\min(r,N-r)\),

\[
 |\widehat h(r)|
 \leq\min\left(\frac nN,\frac1{N|\sin(\pi r/N)|}\right)
 \leq\min\left(\frac nN,\frac1{2d_r}\right).
 \tag{16}
\]

The last inequality uses
\(\sin(\pi d_r/N)\geq2d_r/N\) for \(0\leq d_r\leq N/2\).
It follows that

\[
 \sum_{r=0}^{N-1}|\widehat h(r)|
 \leq \frac nN+\sum_{d=1}^n\frac1d
 \leq C(1+\log(2+n)).
 \tag{17}
\]

This harmonic sum is the only logarithmic cost.

### Arbitrary row intervals and half endpoints

Extend the row mask by \(w_i(0)=w_i(n+1)=0\), and put

\[
 d_i(t)=w_i(t)-w_i(t+1),\qquad0\leq t\leq n.
 \tag{18}
\]

A nonnegative interval mask with endpoint weights in \([0,1]\) rises from zero to its maximum and then falls to zero. Thus

\[
 \sum_{t=0}^n|d_i(t)|=2\max_s w_i(s)\leq2.
 \tag{19}
\]

Telescoping gives the exact identity
\[
 w_i(s)=\sum_{t=0}^nd_i(t)P_t(s).
\]
Combining this with (15), define

\[
 \Gamma_i(r)=\sum_{t=0}^nd_i(t)e(rt/N),\qquad
 |\Gamma_i(r)|\leq2.
 \tag{20}
\]

Then the exact row-interval decomposition is

\[
 \boxed{
 w_i(s)=\sum_{r=0}^{N-1}
             \widehat h(r)\Gamma_i(r)e(-rs/N).
 }
 \tag{21}
\]

No coherence or regularity of interval endpoints across rows is required. Empty intervals, singletons, adjacent endpoints, and half endpoints all satisfy (18)--(21) without separate limiting arguments. Endpoints originally specified by nonintegral real numbers merely determine a discrete mask of this type.

### Combine the two decompositions

For \(k=k_s\), equations (13) and (21) give the explicit full product expansion

\[
 M(i,k_s)=
 \sum_{m\in\mathbb Z}\sum_{r=0}^{N-1}
 \bigl[c_i(m)\widehat h(r)\Gamma_i(r)\bigr]
 \bigl[e(mk_s/(4K))e(-rs/N)\bigr].
 \tag{22}
\]

The second bracket has modulus one. Equations (12), (17), and (20) imply

\[
 \sum_{m,r}\sup_i
       |c_i(m)\widehat h(r)\Gamma_i(r)|
 \leq C S(1+\kappa)(1+\log(2+n)).
 \tag{23}
\]

Apply (6) term by term. The finite column and row sets, and the summable bound (23), justify interchanging the series and the bilinear sum. Equivalently one may apply (6) to finite Fourier truncations and then pass to their uniform limit. This proves (1), including all complex vectors.

### What phase control actually licenses

Equation (13) represents the exact residual phase; it does not identify it with \(1\). The result licenses transfer of the all-row norm estimate with the explicit multiplier cost in (1). It licenses no assertion that a phase-free fixed-vector sum equals, or has the same cancellation as, its phased counterpart.

There is also a priced perturbative statement. For real phases and \(\kappa\leq1\), replace (8) by
\(\eta(t)f_i(t)(e(\alpha_it)-1)\).
The function and its first two derivatives are \(O(S\kappa)\). The same proof therefore gives

\[
 \left|\sum_{i,k}u_iv_kH(i,k)w_i(k)f_i(k/K)
                 (e(\delta_i k/a_i)-1)\right|
 \leq C S\kappa B(1+\log(2+n))\|u\|_2\|v\|_2.
 \tag{24}
\]

Here \(w_i(k)\) means the mask at the rank of \(k\). Thus deletion can be replaced by an explicitly bounded error if needed. Merely knowing \(\kappa\leq1\) does not make that error asymptotically negligible.

## 4. First doubtful or unproved step

There is no remaining gap in the exact decomposition or the stated all-row-vector bound.

The first unsupported step in a weaker-hypothesis application would be (6): if the available theorem accepts only \(u_{j,a}=x_jy_a\), multiplying this row vector by an arbitrary coefficient \(c_{j,a}(m)\Gamma_{j,a}(r)\) generally destroys that internal product form.

To replace the all-row hypothesis, one would need an additional bound for arbitrary row vectors, or a controlled decomposition of every resulting row multiplier into factors separate in \(j\) and \(a\), together with the corresponding summability cost. Neither follows from the packet's smoothness in the column variable.

Similarly, replacing the residual phase by \(1\) as an exact identity is unsupported; (24) is the available error statement, not an equality.

## 5. Exact controls and unsupported-upgrade examples

All controls are analytical and finite. No experiment, numerical computation, or web source was used.

**Residual-phase deletion changes a fixed-vector sum.** Take \(K=A=a_1=2\), one row, columns \(1,2,3\), full interval, \(f_1=1\), \(\delta_1=1/2\), and

\[
 H(1,1)=1,\quad H(1,2)=-1,\quad H(1,3)=0,\qquad
 u_1=1,\quad v=(1,1,0).
\]

The unphased sum is zero, whereas the exact phased sum is

\[
 e(1/4)-e(1/2)=i+1.
 \tag{25}
\]

The all-row hypothesis holds with \(B=\sqrt2\), and \(\kappa=1\). This is not a counterexample to (1); it is a counterexample to literal phase deletion or preservation of this particular cancellation.

**A separate-row-factor theorem cannot be upgraded.** Let \(q=2^r\), index \(j,a\) by binary vectors in \(\{0,1\}^r\), and set

\[
 \varepsilon_{j,a}=(-1)^{j\cdot a},\qquad
 H((j,a),1)=q^{-1/2}\varepsilon_{j,a}.
 \tag{26}
\]

There is just one column, so \(K=1\). The \(q\times q\) matrix
\(q^{-1/2}(\varepsilon_{j,a})\) is orthogonal: summing the product of two different rows over \(a\) cancels in pairs, and a row has squared norm one. Hence for all complex \(x,y,v_1\),

\[
 \left|\sum_{j,a}x_jy_av_1H((j,a),1)\right|
 \leq \|x\|_2\|y\|_2|v_1|.
 \tag{27}
\]

This is the weaker internal-product row theorem with \(B=1\).

Choose full masks, \(a_{j,a}=A=1\), \(\delta_{j,a}=0\), and the permitted smooth row functions
\(f_{j,a}(t)=\varepsilon_{j,a}\).
They are real constants with \(S=1\). The multiplied entries become \(q^{-1/2}\). For \(x_j=y_a=q^{-1/2}\) and \(v_1=1\), both vector norms are one but the multiplied sum equals

\[
 q^2\cdot q^{-1}\cdot q^{-1/2}=\sqrt q.
 \tag{28}
\]

Thus no absolute-constant version of the proposed transfer can follow from (27), even with \(n=1\), no residual phase, and constant smooth factors. The true all-row operator norm of the original flattened one-column matrix is \(\sqrt q\), so this example fully respects (1) when its actual hypothesis is used.

| Remaining control | Outcome |
|---|---|
| Singleton column set | \(K=1\) gives \(n=1\). The cyclic construction has \(N=3\) and bounded Fourier cost; no logarithmic singularity occurs. |
| Empty row interval | Its mask and every \(d_i(t)\), \(\Gamma_i(r)\) vanish, giving zero contribution. |
| Singleton interval or coincident endpoints | Any weight in \([0,1]\) has total variation at most \(2\), so all half-weight conventions are included. |
| Nonintegral endpoints | Restricting a real interval to the ordered integer columns gives exactly the discrete masks used in (18); no endpoint derivative is taken. |
| Full interval | It is \(P_n\), already covered exactly by (15). |
| Arbitrary row dependence | The proof uses suprema of row Fourier coefficients, never derivatives or variation in the row index. |
| Complex vectors and coefficients | The original hypothesis applies directly to the modified complex vectors in (6). Moduli bound every Fourier term; no reality or positivity assumption is imposed on \(H,u,v,f_i\). |
| Convergence | Two column-variable derivatives give the summable Fourier envelope (11). Uniform absolute convergence and the finite mask expansion justify every product and limit. |
| Vanishing data | If \(S=0\), the multiplier vanishes. If \(B=0\), testing basis vectors in (3) forces \(H=0\). Empty row sets are also trivial. |
| Large real residual parameter | The explicit cost is \(O(S(1+K/A))\), before the mask logarithm; no assertion of a uniform constant for all \(K/A\) is made. |
| Complex residual-parameter interpretation | A factor \(e^{3\pi K/A}\) controls possible exponential growth. The main \(K/A\leq1\) result is still an absolute-constant statement. |

## 6. Exact dependencies and isolation provenance

- Campaign: gc-full-goal-arithmetic-source-review, round220.
- Task and role: blind_smooth_mask, independent statement-only operator derivation.
- Generated date: 2026-09-28, the supplied session date.
- Only files read for this assignment:
  - protocol.md, SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
  - rounds/codex-managed/gc-full-goal-arithmetic-source-review/briefs/blind_smooth_mask_statement.md, SHA256 97c84fcd8befb47401c11076d4afa49c55d5708df31ec9c79dffce9ac3c24459.
- No graph hash was supplied in this packet; no graph, manifest, generated brief, strategy, source, application, or sibling was read.
- Mathematical dependencies: the given bilinear norm, a fixed cutoff, integration by parts twice, elementary Fourier inversion and its Fejér approximate-identity justification, finite cyclic Fourier inversion, a geometric-series formula, harmonic-series bounds, telescoping total variation, and finite binary-character orthogonality.
- No external theorem import, web access, experiment, new agent, shared-state edit, or successor work was performed. Only the assigned report was written.

**Prior-history disclosure.** This agent retains round217 source/frontier and seam-review context, round218 abstract radial and packet-coherence derivations, and round219 exact-anchor and fraction-packing work. It is not a fresh history-free agent. The present round220 lemma was supplied and derived statement-only: no current claimant proof, arithmetic application, or sibling argument was inspected.

## 7. Recommended state effect

**Recommend promote the exact multiplier transfer under the all-row-vector hypothesis, including its explicit smooth-factor and row-mask decompositions, subject to the conductor's normal seam and graph procedures.**

The valid conclusion retains the residual phase and pays its stated multiplier cost. Reject literal phase deletion and an unproved replacement of all row vectors by an internal separate-row-factor theorem; the finite controls establish those limitations.

No application, graph mutation, synthesis, or next-round decision is made. The assigned task ends with this bounded report.

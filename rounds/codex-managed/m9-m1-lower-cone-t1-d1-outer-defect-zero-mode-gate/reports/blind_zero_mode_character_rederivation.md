# 1. Result

For every \(\varepsilon>0\), uniformly in the complete range
\[
 J_A<V\leq K=\sqrt{NM},
\]
the literal zero row in the statement-only packet satisfies the stronger estimate
\[
 \boxed{\ \mathcal Z_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon\ }
 \qquad\text{and hence}\qquad
 \mathcal Z_U(V)\ll_{\varepsilon,A}X^\varepsilon.
\]
The lower bound on \(V\) is not needed for this zero-mode estimate; only \(V\leq K\) is used.

The proof is a genuinely signed estimate.  Its two inputs are (i) the total discrete variation
\[
 \sup_{V<|j|\leq 2V}|\widehat B_j(0)|+
 \operatorname {Var}_{V<|j|\leq2V,\,j>0}\widehat B_j(0)+
 \operatorname {Var}_{V<|j|\leq2V,\,j<0}\widehat B_j(0)
 \ll_\varepsilon K M^{-3/4}X^\varepsilon,
\]
with all literal endpoints included, and (ii) the elementary complete-modulus Fourier bound
\[
 \sup_{I\subset\mathbb Z\text{ consecutive}}
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c).
\]
No unproved character-sum theorem is required.

# 2. Exact statement and hypotheses

I use only (156.BL1)--(156.BL6), including the literal zero extension and the asserted physical support \(x\asymp K\).  Thus a complete residue system modulo \(q=4N\) contains \(O(K)\) integers on which any \(B_j(x)\) can be nonzero.  The notation \(x\asymp K\) is used in its usual uniform sense, with fixed support constants.  No differentiability of \(w_U\) is assumed: its supremum norm and its total variation, including its zero-extension jumps, are the quantities in (156.BL3).

Write
\[
 N=2^\nu n,\qquad n\ \text{odd},\qquad d\mid n,
\]
and, for the fixed divisor \(d\),
\[
 c=\frac{4N}{d}=2^s m,\qquad s=\nu+2\geq2,
 \qquad m=\frac nd.
\]
Let
\[
 m=t u^2,\qquad
 t=\prod_{v_p(m)\ \mathrm{odd}}p
\]
be the squarefree kernel of \(m\), and put
\[
 \eta\equiv s\pmod2,\qquad
 \delta\equiv\frac{t-1}{2}\pmod2.
\]
Thus \(\delta=0\) for \(t\equiv1\pmod4\) and \(\delta=1\) for \(t\equiv3\pmod4\).  I use
\[
 \chi_4(a)=\left(\frac{-1}{a}\right),\qquad
 \chi_8(a)=\left(\frac2a\right),\qquad
 \alpha=\frac{1+i}{2},\qquad \beta=\frac{1-i}{2}.
\]
All Gauss sums below use the same positive additive convention as (156.BL5):
\[
 \tau(\chi)=\sum_{a\bmod f}\chi(a)e_f(a)
\]
for a primitive character of conductor \(f\).  Valuations of the nonzero integers \(j\) in (156.BL6) are the ordinary nonnegative valuations.

# 3. Proof or derivation

**Exact character decomposition and primitive conductors.**  For every unit \(a\bmod c\), \(a\) is odd and
\[
 \epsilon_a=\alpha+\beta\chi_4(a).
\]
Since \(m=t u^2\) and \((a,c)=1\),
\[
 \left(\frac ca\right)
 =\left(\frac2a\right)^s\left(\frac ma\right)
 =\chi_8(a)^\eta\left(\frac ta\right).
\]
Consequently
\[
 \epsilon_a\left(\frac ca\right)
 =\alpha\psi_0(a)+\beta\psi_1(a),
 \qquad
 \psi_0(a)=\chi_8(a)^\eta\left(\frac ta\right),
 \quad \psi_1(a)=\chi_4(a)\psi_0(a).
 \tag{3.1}
\]
These are the restrictions to the units modulo \(c\) of primitive real quadratic characters \(\chi_{D_k}=(D_k/\,\cdot\,)\).  Their exact fundamental discriminants and conductors are
\[
\begin{array}{c|c|c|c|c}
 &t\pmod4&D_0& D_1&(f_0,f_1)\\ \hline
 s\ \mathrm{even}&1&t&-4t&(t,4t)\\
 s\ \mathrm{even}&3&4t&-t&(4t,t)\\
 s\ \mathrm{odd}&1\text{ or }3&8t&-8t&(8t,8t).
\end{array}
\tag{3.2}
\]
Every \(D_k\) in (3.2) is a fundamental discriminant, including \(D_0=1\) when \(t=1\), and \(f_k=|D_k|\mid c\).

For clarity about the local characters, quadratic reciprocity gives
\[
 \left(\frac ta\right)
 =\chi_4(a)^\delta\prod_{p\mid t}\left(\frac ap\right).
\]
Thus the odd local component at each \(p\mid t\) is the primitive Legendre character
\(\lambda_p=(\,\cdot\,/p)\), while the two-primary components are
\[
 \theta_0=\chi_8^\eta\chi_4^\delta,
 \qquad \theta_1=\theta_0\chi_4.
 \tag{3.3}
\]
Explicitly,
\[
\begin{array}{c|c|c|c}
 &\delta&\theta_0&\theta_1\\ \hline
 s\ \mathrm{even}&0&1&\chi_4\\
 s\ \mathrm{even}&1&\chi_4&1\\
 s\ \mathrm{odd}&0&\chi_8&\chi_{-8}=\chi_8\chi_4\\
 s\ \mathrm{odd}&1&\chi_{-8}&\chi_8.
\end{array}
\tag{3.4}
\]
This displays, rather than suppresses, the reciprocity contribution at \(p=2\).

Let \(\chi_{D_k,c}\) denote the character modulo \(c\) induced by the primitive \(\chi_{D_k}\): it equals \(\chi_{D_k}\) on the units modulo \(c\) and is zero elsewhere.  Define
\[
 T_{c,k}(r)=\sum_{a\bmod c}\chi_{D_k,c}(a)e_c(ar).
\]
Then (3.1) gives the exact additive-transform identity
\[
 \boxed{\ K(0,-j;c)=\alpha T_{c,0}(-j)+\beta T_{c,1}(-j).\ }
 \tag{3.5}
\]

There is also a useful exact global formula for each induced transform.  Put \(L_k=c/f_k\).  Möbius inversion of the extra coprimality condition gives
\[
 T_{c,k}(r)=\tau(\chi_{D_k})
 \sum_{\substack{h\mid L_k,\ h\mid r\\(L_k/h,f_k)=1}}
 h\,\mu(L_k/h)\chi_{D_k}(L_k/h)\chi_{D_k}(r/h).
 \tag{3.6}
\]
For example, when \(f_k=1\), (3.6) is exactly the Ramanujan sum
\(\sum_{h\mid(c,r)}h\mu(c/h)\); there is no illicit primitive Gauss-sum estimate in this case.

**Every induced prime-power factor, including \(p=2\).**  The following local computation makes both the support and the value completely explicit.  Let a character modulo \(p^e\) be induced from a primitive local character \(\xi\) of conductor \(p^a\), where \(0\leq a\leq e\), and set
\[
 G_{p^e,\xi}(z)=
 \sum_{v\bmod p^e}^{*}\xi(v)e_{p^e}(zv).
\]
If \(a\geq1\), lifting from \(p^a\) gives
\[
 G_{p^e,\xi}(z)=
 \begin{cases}
 p^{e-a}\overline\xi\!\left(z/p^{e-a}\right)\tau(\xi),
     &v_p(z)=e-a,\\
 0,&v_p(z)\ne e-a.
 \end{cases}
 \tag{3.7}
\]
If \(a=0\), the factor is the principal Ramanujan factor
\[
 G_{p^e,1}(z)=
 \begin{cases}
 0,&v_p(z)\leq e-2,\\
 -p^{e-1},&v_p(z)=e-1,\\
 p^{e-1}(p-1),&v_p(z)\geq e.
 \end{cases}
 \tag{3.8}
\]
Formulas (3.7)--(3.8) are valid without change for \(p=2\), using the primitive characters of conductors \(4\) and \(8\) when \(a=2\) and \(a=3\).

To record the CRT units and hence the exact value, for \(p^e\Vert c\) put \(C_p=c/p^e\) and let \(\overline C_p\) be its inverse modulo \(p^e\).  Factoring both the additive character and (3.3) by CRT yields
\[
 T_{c,k}(-j)=
 \prod_{p^e\Vert c}G_{p^e,\xi_{k,p}}
       \bigl(-j\overline C_p\bigr),
 \tag{3.9}
\]
where \(\xi_{k,p}=\lambda_p\) if \(p\mid t\), is principal at an odd \(p\mid m/t\), and is \(\theta_k\) at \(p=2\).

For an odd prime \(p^e\Vert m\), the common local factor of the two transforms is therefore
\[
 L_{p,e}(j)=
 \begin{cases}
 p^{e-1}\lambda_p\!\left(
   \dfrac{-j\overline C_p}{p^{e-1}}\right)\tau(\lambda_p),
   &e\text{ odd and }v_p(j)=e-1,\\[2mm]
 -p^{e-1},&e\text{ even and }v_p(j)=e-1,\\
 p^{e-1}(p-1),&e\text{ even and }v_p(j)\geq e,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{3.10}
\]
The quotient in the first line is a unit modulo \(p\), so (3.10) is unambiguous.  Put
\[
 L_{\rm odd}(j)=\prod_{p^e\Vert m}L_{p,e}(j).
\]
If
\[
 h=\frac{m}{\operatorname {rad}(m)}=\prod_{p^e\Vert m}p^{e-1},
\]
then the exact odd support is
\[
 \boxed{\ L_{\rm odd}(j)\ne0
 \quad\Longleftrightarrow\quad
 h\mid j\ \text{ and }\ \gcd(j/h,t)=1.\ }
 \tag{3.11}
\]

At \(p=2\), take \(z_2=-j\overline m\pmod {2^s}\).  Besides (3.8), the exact nonprincipal factors are
\[
 R_4(j)=
 \begin{cases}
 2^{s-2}\chi_4(z_2/2^{s-2})\tau(\chi_4),&v_2(j)=s-2,\\
 0,&\text{otherwise},
 \end{cases}
 \tag{3.12}
\]
and
\[
 R_{\pm8}(j)=
 \begin{cases}
 2^{s-3}\chi_{\pm8}(z_2/2^{s-3})\tau(\chi_{\pm8}),&v_2(j)=s-3,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{3.13}
\]
Here
\[
 \tau(\chi_4)=2i,\qquad
 \tau(\chi_8)=\sqrt8,\qquad
 \tau(\chi_{-8})=i\sqrt8.
 \tag{3.14}
\]
Let \(R_1(j)\) be (3.8) with \(p=2,e=s\).  Equations (3.5) and (3.9) now give the exact value
\[
 K(0,-j;c)=L_{\rm odd}(j)\,\mathcal R_{s,\delta}(j).
 \tag{3.15}
\]
When \(s\) is even, define
\[
 \kappa_{\rm pr}=(1-\delta)\alpha+\delta\beta,
 \qquad
 \kappa_4=(1-\delta)\beta+\delta\alpha.
\]
Then
\[
 \mathcal R_{s,\delta}(j)=
 \begin{cases}
 i2^{s-1}\kappa_4\,
   \chi_4\!\left(z_2/2^{s-2}\right),&v_2(j)=s-2,\\
 -2^{s-1}\kappa_{\rm pr},&v_2(j)=s-1,\\
 2^{s-1}\kappa_{\rm pr},&v_2(j)\geq s,\\
 0,&v_2(j)\leq s-3.
 \end{cases}
 \tag{3.16}
\]
Thus the conductor-\(4\) row and the two-principal row are disjoint and neither is discarded.

When \(s\) is odd, put \(j'=j/2^{s-3}\) and
\(u_2=(-j')\overline m\pmod8\).  Directly combining the two terms in (3.4), using (3.14), gives
\[
 \mathcal R_{s,\delta}(j)=
 \begin{cases}
 2^{s-3}\sqrt8\,[1+i(-1)^\delta]\chi_8(u_2),
   &v_2(j)=s-3\ \text{and }\chi_4(u_2)=(-1)^\delta,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{3.17}
\]
Since \(m\equiv t\pmod4\), the congruence in the first line is equivalently
\[
 j'\equiv3\pmod4.
 \tag{3.18}
\]
This extra half-support is the exact cancellation between the \(\chi_8\) and \(\chi_{-8}\) transforms; retaining only their absolute values would miss it.

The exceptional principal case is now transparent.  A primitive principal constituent occurs if and only if
\[
 s\text{ is even and }t=1,
\]
equivalently if and only if \(c=2^s m\) is a perfect square.  In that case
\[
 K(0,-j;c)=\alpha\,c_c(-j)+
 \beta\,T_{c,\chi_{-4}}(-j),
 \tag{3.19}
\]
where
\[
 c_c(-j)=\sum_{r\mid(c,j)}r\mu(c/r)
\]
is the exact Ramanujan sum.  Every even-exponent odd prime in (3.19) contributes the two alternatives in (3.8); it is not replaced by a square-root Gauss factor.

**Variation of the actual zero-mode weight.**  Let
\[
 a_V=\lfloor V\rfloor+1,
 \qquad b_V=\lfloor2V\rfloor,
 \qquad \mathcal J_V=\{a_V,\ldots,b_V\}.
\]
Then the two literal sign ranges in (156.BL6) are exactly \(j=\sigma k\), with
\(\sigma\in\{+1,-1\}\) and \(k\in\mathcal J_V\).  If \(\mathcal J_V\) is empty, there is nothing to prove.  Set
\[
 b_\sigma(k)=\widehat B_{\sigma k}(0).
\]
For a fixed physical integer \(x\asymp K\), the sampled weight
\(w_U((x^2-\sigma k)/N)\) moves monotonically through the zero-extended real profile.  Hence its discrete variation is at most \(\operatorname {Var}w_U\).  The literal indicator
\(-x\leq\sigma k\leq x-1\) contributes its actual boundary jumps, at most two jumps of size \(\|w_U\|_\infty\).  A half-open cell changes at one adjacent pair and is therefore already charged to this discrete variation; no endpoint is smoothed or moved.

For the phase, rationalization gives the exact identity
\[
 \frac{j}{x+\sqrt{x^2-j}}=x-\sqrt{x^2-j}.
\]
Since \(x\) is an integer, its exponential equals
\(e(\sqrt{x^2-j}-x)\), and on \(|j|\leq2V\leq2K\), \(x\asymp K\),
\[
 \left|\frac{d}{dj}\bigl(\sqrt{x^2-j}-x\bigr)\right|
 =\frac{1}{2\sqrt{x^2-j}}\ll K^{-1}.
\]
Thus its variation over either dyadic sign interval is \(O(V/K)=O(1)\).  Product variation now gives, for each fixed \(x\),
\[
 \sup_k|B_{\sigma k}(x)|+
 \sum_{k=a_V}^{b_V-1}|B_{\sigma(k+1)}(x)-B_{\sigma k}(x)|
 \ll \|w_U\|_\infty+\operatorname {Var}w_U.
\]
Summing over the \(O(K)\) physical values of \(x\) in the chosen complete residue system proves
\[
 \boxed{\
 |b_\sigma(b_V)|+
 \sum_{k=a_V}^{b_V-1}|b_\sigma(k+1)-b_\sigma(k)|
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
 \ }
 \tag{3.20}
\]
The same proof also bounds the supremum of \(b_\sigma\).  Notice that (3.20) uses the actual \(\widehat B_j(0)\), not a constant majorant substituted for it.

**Signed partial sums of the arithmetic transform.**  Put
\[
 \gamma_c(a)=\epsilon_a(c/a),\qquad (a,c)=1.
\]
Then \(|\gamma_c(a)|=1\).  For every consecutive integer interval \([A,B]\),
\[
 \sum_{j=A}^{B}K(0,-j;c)
 =\sum_{a\bmod c}^{*}\gamma_c(a)
   \sum_{j=A}^{B}e_c(-aj).
\]
If \(r(a)=\min(a,c-a)\) for \(1\leq a<c\), the geometric sum is at most
\[
 \min\!\left(B-A+1,\frac{c}{2r(a)}\right).
\]
There is no \(a=0\) term, because the outer sum is over units and \(c\geq4\).  Summing the harmonic majorant gives the uniform, length-independent estimate
\[
 \boxed{\
 \sup_{A\leq B}
 \left|\sum_{j=A}^{B}K(0,-j;c)\right|
 \ll c\log(2c).
 \ }
 \tag{3.21}
\]
The same estimate holds with \(j\) replaced by \(-j\).

Apply discrete summation by parts separately to \(j=k\) and \(j=-k\), with the exact endpoint set \(\mathcal J_V\).  Equations (3.20)--(3.21) give, for each odd \(d\mid N\),
\[
 \left|\sum_{V<|j|\leq2V}
 \widehat B_j(0)K(0,-j;c)\right|
 \ll_\varepsilon
 K M^{-3/4}X^\varepsilon\,c\log(2c).
 \tag{3.22}
\]

Restoring \(\chi_4(d)\), every divisor \(d\), both signs, and the normalization \(q=4N\), the complete power ledger is
\[
\begin{array}{c|c}
 \text{factor}&\text{size used}\\ \hline
 |{-i(1+i)}/{(2Nq)}|&\ll N^{-2}\\
 \text{actual weighted variation of }\widehat B_j(0)&
 K M^{-3/4}X^\varepsilon\\
 \text{signed arithmetic partial sum}&c\log(2c)\\
 \text{divisor coefficient}&d\sqrt c\\
 d\sqrt c\,c\quad(c=4N/d)&8N^{3/2}d^{-1/2}.
\end{array}
\]
Therefore
\[
\begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 N^{-2}K M^{-3/4}X^\varepsilon
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d\,c^{3/2}\log(2c)\\
 &\ll_\varepsilon
 N^{-2}K M^{-3/4}X^\varepsilon
 N^{3/2}\sum_{d\mid n}d^{-1/2}\\
 &\ll_\varepsilon
 K M^{-3/4}N^{-1/2}X^\varepsilon
 =M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{3.23}
\]
Here the logarithm and \(\sum_{d\mid n}d^{-1/2}\leq\tau(n)\) are absorbed by initially using a smaller epsilon in (156.BL3).  Since \(1\ll M\), (3.23) proves the claimed \(X^\varepsilon\) bound.

**Signed estimate versus unsigned capacity.**  The valuation formulas show exactly what is lost if the \(j\)-signs are discarded.  Let
\[
 E=\prod_{\substack{p^e\Vert m\\e\ \mathrm{even}}}p.
\]
On the odd support (3.11), writing \(j=hy\), (3.10) has magnitude
\[
 h\sqrt t\prod_{\substack{p\mid E\\p\mid y}}(p-1).
\]
Expanding the last product and counting multiples gives
\[
 \sum_{V<|j|\leq2V}|K(0,-j;c)|
 \ll_\varepsilon X^\varepsilon
 \left(V\sqrt t+\frac{c}{\sqrt t}\right).
 \tag{3.24}
\]
Indeed, the main counting term is bounded by
\(V\sqrt t\,2^{\omega(E)}\), and the endpoint term is
\(2^s h\sqrt t\operatorname {rad}(E)=c/\sqrt t\), up to an absolute two-adic constant from (3.16) or (3.17).  Inserting (3.24), rather than (3.21), yields only
\[
 |\mathcal Z_U(V)|_{\rm unsigned\ capacity}
 \ll_\varepsilon
 \left(\frac{K M^{-3/4}V}{N}
       +\frac{K M^{-3/4}}{\sqrt N}\right)X^\varepsilon
 \ll_\varepsilon (M^{1/4}+M^{-1/4})X^\varepsilon.
 \tag{3.25}
\]
Thus the positive \(M^{1/4}\) capacity is not the proved estimate.  It is removed by the signed partial sum (3.21) together with the bounded variation (3.20).  An arbitrary sign attached separately to each \(j\) would destroy (3.21), while an arbitrary bounded sequence in place of the literal Vaaler profile would destroy (3.20).  Hence this argument does not prove the false unsigned or independently adversarial analogue.

# 4. First doubtful or unproved step

There is no remaining unproved arithmetic or analytic step under the literal hypotheses of the packet, and consequently no external weighted partial-sum theorem is still needed.  The exact weighted theorem required here is (3.22), and it has been proved from (3.20) and the elementary geometric-series estimate (3.21).

The first seam that should nevertheless be checked when this report is reattached to a larger proof is the meaning of the packet's phrase “physical support \(x\asymp K\).”  The proof uses precisely two consequences: there are \(O(K)\) physical integer values of \(x\) in one residue system, and \(x^2-j\asymp K^2\) for \(|j|\leq2K\).  Both are the standard literal consequences of the stated support condition.  If an inherited definition allowed support constants depending on \(X,M,V\), then (3.20), rather than any character calculation, would be the first step needing revision.

# 5. Required control test and outcome

Three exact algebraic controls were applied; no numerical certification was used.

1. **Perfect-square/principal control.**  Set \(t=1\) and take \(s\) even.  Then (3.2) gives conductors \(1\) and \(4\), and (3.6) gives exactly (3.19), with the conductor-one transform equal to the Ramanujan sum.  Its local support is \(v_p(j)\geq e_p-1\) at every prime, with the two values in (3.8).  Outcome: pass; the dangerous principal constituent is present and explicitly retained.

2. **Two-adic cancellation control.**  For odd \(s\), insert \(\tau(\chi_8)=\sqrt8\) and \(\tau(\chi_{-8})=i\sqrt8\) into (3.5).  The bracket is \(\alpha[1+\chi_4(u_2)]\) when \(\delta=0\), and \(\beta[1-\chi_4(u_2)]\) when \(\delta=1\).  This is exactly (3.17), and the surviving congruence reduces to \(j/2^{s-3}\equiv3\pmod4\).  Outcome: pass; the \(p=2\) half-support and its phase are not inferred from an absolute-value bound.

3. **False-unsigned control.**  Replace the signed Abel step by the exact local absolute values.  The resulting ledger is (3.24)--(3.25), whose main term is \(M^{1/4}X^\varepsilon\), not \(X^\varepsilon\).  Outcome: pass; the proof's saving is demonstrably signed and cannot survive arbitrary \(j\)-wise signs.

# 6. Dependencies and exact artifacts used

The only artifacts read were:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/blind_statement.md`.

No graph, campaign state, strategy, seed, prior report, sibling report, proof draft, synthesis, validation matrix, computation, or web source was read or used.  The derivation depends only on (156.BL1)--(156.BL6), elementary quadratic reciprocity, the primitive Gauss identity, Möbius inversion, CRT, a geometric-series bound, and discrete summation by parts.

# 7. Recommended state effect

**Promote**, subject only to a seam check that the inherited literal phrase \(x\asymp K\) has the fixed-constant meaning recorded in Section 4.  The report proves the complete stated range, handles every induced local factor and the conductor-one square case, restores all divisor and endpoint factors, and yields the strict gain \(M^{-1/4}\).

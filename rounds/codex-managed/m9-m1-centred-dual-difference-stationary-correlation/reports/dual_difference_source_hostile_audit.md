# Round 84 hostile/source audit: centred dual differences

## 1. Result

**Scoped result certified; global route not certified.**  For the principal Round-81 coefficient \(V=g_c(0)\), the range

\[
0<|d|\le D,\qquad D=J^{17/30},
\]

is target-safe in every local class.  More precisely, the exact residue Cauchy bound, a uniform one-dimensional stationary formula for the \(c\)-Fourier transform, and the second-derivative estimate on \(n=r+M\ell\) give

\[
 \mathcal Y^{(V)}_{0<|d|\le D}
 \ll_\varepsilon X^\varepsilon
 \left(B^3J^{1/10}D^{3/2}+B^2J^{3/10}D^{1/2}\right)
 \ll_\varepsilon X^\varepsilon J^{7/5}.
 \tag{84.H1}
\]

The first term reaches \(J^{7/5}\), but does not exceed it, at the simultaneous endpoints \(B=J^{3/20}\) and \(D=J^{17/30}\).  There is no hidden factor of \(B\), \(M\), \(d\), \((d,M)\), or the prime-power part of \(M\).  Negative \(d\), nonzero \(d\equiv0\pmod M\), all three values of \(\kappa\), the \(n\)-support edges, nonstationary tails, and stationary remainders are included.

The certification is deliberately narrow.  It removes a \(d\)-range; it supplies neither a further \(B\)-power nor a conductor saving.  No audited current primary theorem estimates the remaining actual shifted product with its joint square-root weight for arbitrary \(M=b,2b,4b\).  In addition, explicit prime-power Fourier modes disprove the uniform local square-root transform estimate that a naive completion argument would require.

## 2. Exact statement and hypotheses

Write

\[
 A_{M,K,d}(r)=S(r+d,K;M)\overline{S(r,K;M)}-c_M(d),
 \qquad r\pmod M,
 \tag{84.H2}
\]

and, with \(e(z)=e^{2\pi iz}\),

\[
 I_b(n)=\int_0^\infty V_b(x)
 e\!\left(-\frac{A_b}{g x}-\frac{nx}{M}\right)\,dx,
 \quad
 A_b=\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2.
 \tag{84.H3}
\]

The three local classes are exactly

\[
\begin{array}{c|c|c|c}
\kappa&g&M&K\\ \hline
1/4&1&4b&k\\
1/2&2&2b&2[k\bar4]_b\\
1&4&b&[k\bar4]_b,
\end{array}
\qquad gM=4b,\qquad (K,M)=O_k(1).
\tag{84.H4}
\]

Here \(J=X^{1/2}\), \(Q=J^{2/5}\), \(T=J^{3/5}\), \(B=C/T\),

\[
J^{13/18}<C\le J^{3/4},\qquad
J^{11/90}<B\le J^{3/20},\qquad b\asymp B.
\tag{84.H5}
\]

The Round-81 dependency is used in its literal accepted form: \(V_b=g_c(0)\) is the neighbor-independent principal coefficient, contains the smooth dyadic conductor cutoff, has a compactly supported smooth extension on \(x\asymp C\), and, for a fixed sufficiently large \(R\),

\[
 \max_{0\le j\le R}\sup_x |(C\partial_x)^jV_b(x)|
 \ll_{R,\varepsilon}X^\varepsilon.
 \tag{84.H6}
\]

This is the finite derivative hierarchy asserted by the Round-81 exact-integral addendum and normalization review when they say that each \(c\)-derivative costs one \(C^{-1}\) on the dyadic block.  It is stronger than merely knowing \(\|V\|_\infty+\operatorname{Var}V\ll X^\varepsilon\).  The raw incomplete-Gaussian Farey transition belongs to the pointwise remainder \(E\) in (81.N1); it is **not** part of the Round-84 component audited here.

Define

\[
 P_b=\frac{A_b}{gC}\asymp JQ=J^{7/5},\qquad
 N_b=\frac{A_bM}{gC^2}\asymp Q^2,\qquad
 x_n=\sqrt{\frac{A_bM}{gn}}.
\tag{84.H7}
\]

Then the uniform stationary lemma needed for (84.H1) is

\[
 I_b(n)=
 \frac{A_b^{1/4}M^{3/4}}{\sqrt2\,g^{1/4}n^{3/4}}
 V_b(x_n)
 e\!\left(-\lambda_b\sqrt n-\frac18\right)
 +O_\varepsilon\!\left(X^\varepsilon\frac{C}{P_b}\right),
 \tag{84.H8}
\]

uniformly for \(n>0\) in a fixed enlarged band \(n\asymp N_b\), with \(V_b(x_n)=0\) when the saddle is outside its support, where

\[
 \lambda_b=2\sqrt{\frac{A_b}{gM}}
 =\sqrt X+\frac{\sqrt{\kappa k}}{b}.
 \tag{84.H9}
\]

Outside that enlarged band, and for the wrong sign \(n\le0\), repeated integration by parts gives an arbitrarily summable bound.  The reflected endpoint orientation is the conjugate statement with the stationary sign of \(n\) reversed.  After division by \(M\), the main coefficient in (84.H8) has size and total variation \(O_\varepsilon(X^\varepsilon J^{-1/10})\), while the normalized error is

\[
 e_0:=\frac{C}{MP_b}\asymp\frac{T}{JQ}=Q^{-2}=J^{-4/5}.
 \tag{84.H10}
\]

The statement certified is therefore

\[
 \sum_{b\asymp B}\ \sum_{0<|d|\le D}\ \sum_{n\in\mathbb Z}
 A_{M,K,d}(n\bmod M)
 \frac{I_b(n+d)}M\frac{\overline{I_b(n)}}M
 \ll_\varepsilon X^\varepsilon J^{7/5},
 \tag{84.H11}
\]

with the literal \(d=0\) term absent but every nonzero multiple of \(M\) retained.

## 3. Proof and hostile derivation

**Arithmetic normalization.**  Orthogonality in the first Kloosterman argument gives, without any coprimality assumption on \(K\),

\[
 \sum_{r\bmod M}|S(r,K;M)|^2=M\varphi(M),
\tag{84.H12}
\]

and hence Cauchy gives the exact shifted bound

\[
 \sum_{r\bmod M}|S(r+d,K;M)S(r,K;M)|\le M\varphi(M).
\tag{84.H13}
\]

Since \(|c_M(d)|\le\varphi(M)\),

\[
 \sum_{r\bmod M}|A_{M,K,d}(r)|
 \le 2M\varphi(M)\le2M^2.
\tag{84.H14}
\]

Also

\[
 \sum_{r\bmod M}S(r+d,K;M)\overline{S(r,K;M)}=Mc_M(d),
\quad \sum_{r\bmod M}A_{M,K,d}(r)=0.
\tag{84.H15}
\]

Thus the Ramanujan subtraction is exactly normalized.  If \(d=tM\ne0\), then \(c_M(d)=\varphi(M)\) and

\[
 A_{M,K,d}(r)=|S(r,K;M)|^2-\varphi(M),
\tag{84.H16}
\]

so (84.H14) still applies.  The argument never replaces “\(d=0\)” by “\(d\equiv0\pmod M\).”

**Uniform Fourier stationary phase.**  Put \(x=Cy\).  On the support of \(V_b(Cy)\), (84.H3) has the form

\[
 C\int W_b(y)e\!\left(-P_b/y-(nC/M)y\right)\,dy,
 \qquad \|(\partial_y)^jW_b\|_\infty\ll X^\varepsilon.
\tag{84.H17}
\]

For \(n\asymp N_b\) its two phase parameters are comparable to \(P_b\), it has the unique saddle \(x_n\), and

\[
 \Phi_b(x_n)=-2\sqrt{\frac{A_bn}{gM}}=-\lambda_b\sqrt n,\qquad
 \Phi_b''(x_n)=-\frac{2A_b}{gx_n^3}.
\tag{84.H18}
\]

A fixed-support Morse change of variable, followed by one integration by parts in the term vanishing at the saddle, gives the full Gaussian main term (84.H8) and the conservative error \(O(CP_b^{-1})\).  Its natural saddle width is

\[
 h_b=C P_b^{-1/2},\qquad h_b/C=P_b^{-1/2}=J^{-7/10}.
\tag{84.H19}
\]

This is also the relative size of the conservative remainder compared with the leading \(CP_b^{-1/2}\asymp MJ^{-1/10}\).  It is far smaller than the relative \(J^{-1/15}\) that an absolute cross-error ledger would require.  Because \(V_b\), not the Round-81 remainder \(E\), is transformed, there is no sharp moving Farey endpoint and no truncated half-Gaussian.  Extending the smooth cutoff by zero makes (84.H8) uniform as \(x_n\) enters or leaves support.  Away from the enlarged saddle band, \(|\Phi_b'|\gg P_b/C\) and (84.H6) gives arbitrarily rapid decay.  Thus neither support edges nor nonstationary tails create a \(B/M/d\) loss.

The nonoscillatory coefficient in (84.H8), divided by \(M\), has supremum \(O(J^{-1/10}X^\varepsilon)\).  As \(n\) varies, \(x_n\) is monotone; composition with \(V_b\), multiplication by \(n^{-3/4}\), translation by \(d\), and taking a product therefore give

\[
 \|w_{b,d}\|_\infty+\operatorname{Var}(w_{b,d})
 \ll_\varepsilon X^\varepsilon J^{-1/5}
\tag{84.H20}
\]

for the product main weight, uniformly for \(|d|\le D=o(N_b)\).  No subdivision into \(O(d/M)\) pieces is needed.

**Difference-phase cancellation.**  On \(n=r+M\ell\asymp N_b\asymp Q^2\), the product phase is

\[
 F_{b,d}(\ell)=-\lambda_b
 \left(\sqrt{r+M\ell+d}-\sqrt{r+M\ell}\right).
\tag{84.H21}
\]

For \(0<|d|\le D\ll Q^2\), its second derivative has constant sign and

\[
 |F_{b,d}''(\ell)|\asymp
 \frac{M^2J|d|}{Q^5}=\frac{M^2|d|}{J}.
\tag{84.H22}
\]

The progression length is \(L\asymp Q^2/M\).  The second-derivative estimate, uniformly on every subinterval, is

\[
 \sup_I\left|\sum_{\ell\in I}e(F_{b,d}(\ell))\right|
 \ll \sqrt{T|d|}+\frac{J^{1/2}}{M\sqrt{|d|}}.
\tag{84.H23}
\]

Here \(M^2D/J\le J^{-2/15}<1\) at the worst endpoint, so no hidden large-curvature case is being suppressed.  Abel summation using (84.H20), followed by (84.H14), gives for each \(b,d\)

\[
 \ll_\varepsilon X^\varepsilon M^2J^{-1/5}
 \left(\sqrt{T|d|}+\frac{J^{1/2}}{M\sqrt{|d|}}\right).
\tag{84.H24}
\]

Summing \(b\asymp B\), both signs of \(d\), and \(1\le|d|\le D\), with \(M\asymp B\), yields (84.H1).  Explicitly,

\[
 B^3J^{1/10}D^{3/2}\le
 J^{9/20+1/10+17/20}=J^{7/5},
\tag{84.H25}
\]

and the second term is strictly smaller.

**Stationary errors.**  Absolute summation of one main factor and one normalized error from (84.H10) costs at most

\[
 B^2ND\,J^{-1/10}e_0
 \ll J^{23/30+\varepsilon},
\tag{84.H26}
\]

at the upper endpoint; the error-error term is \(O(J^{1/15+\varepsilon})\).  Rapid nonstationary tails are smaller after choosing a fixed number of integrations by parts.  Even the weaker hypothetical pointwise bound \(e_0\le J^{-1/6+\varepsilon}\) would suffice for the cross term; the actual \(e_0=J^{-4/5}\) has ample margin.

For \(d<0\), put \(m=n+d\).  The term becomes the conjugate of the corresponding \(-d>0\) term after interchanging \(m,n\); the support and curvature estimates are identical.  Since \(D/Q^2=J^{-7/30}\), neither sign approaches \(n=0\) inside the stationary bulk.

## 4. First doubtful or unproved step

The first unproved step is **after** the certified range: estimating

\[
 J^{17/30}<|d|\ll Q^2
\tag{84.H27}
\]

for arbitrary \(b\asymp B\).  The scoped argument cannot simply be iterated.  If

\[
 H=\frac{Q^3}{MJ}=\frac{J^{1/5}}M,
\tag{84.H28}
\]

then \(|F'|\asymp |d|/H\), and the number of integral derivative crossings grows with \(d\).  At \(d\asymp Q^2\) it is \(Q^2/H=MJ/Q=MT\asymp C\).  Moreover, once \(d\gtrsim HL=J/M^2\), the raw second-derivative estimate is no better than the trivial progression length.  The endpoint \(D=J^{17/30}\) lies safely below this threshold, but the unresolved interval does not.

Completion does not repair this by itself.  Fourier inversion of \(A_{M,K,d}\), followed by the dual stationary transform of the square-root weight, reconstructs the original residue off-diagonal unless one proves a genuinely new joint bound for the arithmetic Fourier coefficient and the dual \(h,d,b\) sum.  The explicit prime-power mode in Section 5 shows why a uniform coefficientwise square-root estimate is false.  Thus a claimed full-\(d\) proof whose next line is merely “Poisson/B-process and Weil” has returned to the starting object.

There is one documentation seam worth making explicit in any State Patch: (84.H8) uses the finite pointwise derivative hierarchy (84.H6), not only the displayed BV conclusion in (81.N1).  The authorized Round-81 review states that hierarchy in prose through its smooth normalized \(c/C,Tb/c,c/J\) variables.  If the graph dependency records only BV, it should cite that derivative sentence or add (84.H6) as the exact interface.  This is not a mathematical obstruction under the dependency authorized for this audit.

## 5. Required control tests and outcomes

1. **All local classes:** pass.  The stationary formula uses only \(gM=4b\), and \(g\in\{1,2,4\}\) is fixed.  The residue energy identity does not require \((K,M)=1\), so the even class \(K=2[k\bar4]_b\) is not treated as a parity analogue of an odd class.

2. **Ramanujan subtraction:** pass.  Equation (84.H15) proves exact zero mean.  The subtraction removes only the \(h=0\) arithmetic Fourier mode; it does not remove \(d\equiv0\pmod M\) or any \(h\ne0\) mode.

3. **Nonzero multiples of \(M\):** pass for the scoped lemma.  Equation (84.H16) and (84.H14) remain valid, while the real square-root phase still has curvature (84.H22).  Such shifts are not discarded as diagonal.

4. **Negative \(d\):** pass by conjugate reindexing.  The intersection of the two saddle bands changes endpoints but has the same bounded variation and \(n\asymp Q^2\).

5. **Fourier entry/exit and support edges:** pass for \(V\), fail if one silently substitutes the raw Round-81 transition.  The latter may have variation \(\asymp\sqrt{J/C}\) and is assigned to \(E\) in (81.N1).  The principal \(V=g_c(0)\) has a smooth dyadic cutoff; its new Fourier saddle has width (84.H19), and (84.H8) is uniform through entry and exit.

6. **Stationary errors and tails:** pass.  The conservative relative stationary error is \(P_b^{-1/2}=J^{-7/10}\), versus the required \(J^{-1/15}\).  Equations (84.H26) and the repeated-integration tail bound close absolutely.

7. **Prime powers and gcd:** hostile failure of a global local-transform shortcut.  For

\[
 \widehat A_d(h)=\sum_{r\bmod M}A_{M,K,d}(r)e_M(-hr),\qquad h\not\equiv0\pmod M,
\]

opening the Kloosterman sums gives the exact formula

\[
 \widehat A_d(h)=M\,\mathcal C_{M,K}(d,h),
\quad
 \mathcal C_{M,K}(d,h)=
 \sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
 e_M\!\left(d(y+h)+K((y+h)^{-1}-y^{-1})\right).
\tag{84.H29}
\]

Let \(M=q=p^\nu\), \(p\) odd, \(\nu\ge2\), \(p\nmid K\), take a nonzero integer \(d=tq\), and \(h=p^{\nu-1}\alpha\), \(p\nmid\alpha\).  Then

\[
 \mathcal C_{q,K}(0,h)
 =p^{\nu-1}\sum_{z\bmod p}^{*}e_p(-K\alpha z^2)
 =p^{\nu-1}(G_p(-K\alpha)-1),
\tag{84.H30}
\]

so

\[
 |\widehat A_d(h)|\ge q\,p^{\nu-1}(\sqrt p-1)
 \asymp q^2p^{-1/2}=q^{2-1/(2\nu)}.
\tag{84.H31}
\]

The Ramanujan constant has zero \(h\ne0\) transform and does not cancel this.  Every actual class can contain such an odd \(p^\nu\)-factor with \(p\nmid2k\); CRT transfers the bad local mode.  This confirms the earlier \(q^{3/4}\) normalized loss at \(\nu=2\), \(q^{7/8}\) at \(\nu=4\), and rules out a modulus-uniform \(q^{-1/2}\) gain.  It does not affect (84.H1), which uses (84.H14), not (84.H29).

8. **Perfect powers and exact real-phase resonance:** pass for the scoped lemma, no global shortcut.  If \(J\in\mathbb Z\), \(\sqrt{\kappa k}=s\in\mathbb Z\), \(n=u^2\), \(n+d=v^2\), and \(b\mid(v-u)\), then \(\lambda_b(\sqrt{n+d}-\sqrt n)\in\mathbb Z\).  Thus “the derivative/phase is never integral” is false.  The second-derivative theorem remains valid in the presence of these isolated resonances.  Isolating square \(b\)'s gives only the cardinality gain \(B^{-1/2}\), insufficient for the full-band \(B^{-5/9}\) need; fourth powers give \(B^{-3/4}\) and are harmless by count, but do not cover the positive-density nonsquarefree moduli.

9. **Transform self-return:** failure confirmed as a proposed saving, irrelevant to the scoped proof.  Substituting (84.H29) and then inverting the complete \(h\)-sum exactly returns \(A_d(r)\).  A second stationary transform of the square-root phase changes representation but supplies no norm decrease without an independent joint correlation theorem.

## 6. Dependencies, exact artifacts, and primary-source map

No sibling Round-84 report was read.  The exact project artifacts used were:

- protocol.md, state/proof_obligations.yml, and state/active_campaign.yml;
- the Round-84 brief briefs/dual_difference_source_hostile_audit.md and derivation_packet.md in this campaign;
- Round 83 reviews/conductor_round83_dual_normalization.md and reports/offset_trace_source_hostile_audit.md;
- Round 82 reports/kloosterman_energy_source_hostile_audit.md;
- the conductor-authorized Round-81 derivation_packet_actual_integral_addendum.md and reviews/conductor_round81_transition_normalization.md.

The source search used primary author manuscripts only, with the following literal theorem map.

| Primary source and exact version | What the theorem actually supplies | Why it does not prove the remaining Round-84 survivor |
|---|---|---|
| Fouvry--Kowalski--Michel, [*A study in sums of products*, arXiv:1405.2293v2](https://arxiv.org/abs/1405.2293), 17 January 2015 | Corollary “Bountiful sums of products”: for prime \(p\), a self-dual bountiful trace function, and a tuple of projective transforms, the complete product sum is \(O(\sqrt p)\) if the tuple is normal or the additive twist \(h\ne0\).  Even-rank normalized hyper-Kloosterman sums, including rank two, are covered. | For \(p\nmid K\), it maps literally to \(\sum_rS(r+d,K;p)S(r,K;p)e_p(-hr)\ll p^{3/2}\) whenever \((d,h)\not\equiv(0,0)\pmod p\), up to the finitely many singular trace values.  CRT gives a squarefree odd-modulus bound with a factor \((d,h,M)^{1/2}\), but the theorem is prime-field, unweighted, and says nothing uniform at \(p^\nu\), at the 2-part, or about the joint square-root Fourier weight. |
| Milićević--Zhang, [*Distribution of Kloosterman paths to high prime power moduli*, arXiv:2005.08865v1](https://arxiv.org/abs/2005.08865) | Theorem “Moments of shifted Kloosterman sums” and the underlying sums-of-products theorem: fixed odd \(p\), depth \(p^n\to\infty\), bounded total multiplicity, domains invariant under \(p^{\lfloor\delta_2n\rfloor}\), and power saving unless active shifts collide modulo that depth. | Constants are in a fixed-\(p\) depth aspect; colliding shifts are an explicit exceptional alternative; the stated theorem has no arbitrary additive \(h\)-twist, no 2-adic factor, no varying arbitrary \(b\), and no Round-84 weight.  In particular it does not cover \(d\equiv0\pmod{p^\nu}\). |
| Ricotta--Royer, [*Kloosterman paths of prime powers moduli*, arXiv:1609.03694v4](https://arxiv.org/abs/1609.03694) | Proposition “Moments of shifted Kloosterman sums”: fixed exponent \(n\ge2\), \(p\to\infty\), shifts distinct modulo \(p\), and \(p>\max(M,2n-5)\), with error \(p^{-4(n-1)/2^n+\varepsilon}\). | It excludes colliding shifts, has no arbitrary additive twist or nonlinear external weight, and is not uniform in exponent or arbitrary composite \(M\). |
| Blomer--Milićević, [*The second moment of twisted modular L-functions*, arXiv:1404.7845v1](https://arxiv.org/abs/1404.7845), Theorem 5 | Bounds a variable-\(m\) sum of \(S(m,n_1;r)S(m,n_2;r)\) under its divisor \(s\mid r\), coprimality, and factorization hypotheses. | The two second Kloosterman arguments \(n_1,n_2\) are fixed; the Round-84 kernel shifts the first argument as \(S(n+d,K)S(n,K)\), includes nonunits and a joint square-root weight, and varies the modulus.  Splitting the long \(n\)-range into short intervals does not change that mismatch. |
| Xi--Zheng, [*On the Brun--Titchmarsh theorem. II*, arXiv:2504.12692v3](https://arxiv.org/abs/2504.12692), 24 November 2025 | Large prime \(q\); specially separated quintilinear/quadrilinear Kloosterman structures produced by a shifting argument and high moments. | Prime-only and structurally separated; it is not an arbitrary composite shifted product with one joint weight. |
| Pascadi, [*Non-abelian amplification and bilinear forms with Kloosterman sums*, arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445) | Bilinear forms with a single fixed-modulus Kloosterman kernel, with explicit interval, factorization, and coefficient norms. | It does not contain the correlated kernel \(S(n+d,K;M)\overline{S(n,K;M)}\), the \(d\)-sum, or the varying-modulus square-root product weight. |
| Blomer--Pascadi, [*Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311) | All-modulus bilinear bounds for a single Kloosterman kernel; in the square-root-length regime the stated saving is \(c^{-1/32}\). | “All moduli” does not mean shifted products: its variables and weights are separated bilinear coefficients for one kernel at a fixed modulus.  There is no literal substitution yielding (84.H11) for the remaining \(d\)-range. |

Thus the only literal primary theorem map found for the arithmetic correlation is the prime-field Fouvry--Kowalski--Michel map above.  It is useful on squarefree local factors but cannot be promoted to an all-class theorem for the actual Round-84 object; (84.H31) gives a direct obstruction.

## 7. Recommended state effect

**Promote the scoped lemma (84.H11)**, with the dependency and scope written literally:

- principal Round-81 coefficient \(V=g_c(0)\) only;
- derivative hierarchy (84.H6), not raw BV alone;
- all three local classes and both endpoint orientations;
- every \(0<|d|\le J^{17/30}\), including negative \(d\) and nonzero \(d\equiv0\pmod M\);
- target \(O_\varepsilon(X^\varepsilon J^{7/5})\), with no claimed power saving at the simultaneous top endpoint.

**Retain the full stationary dual-difference survivor as open.**  Reject any state effect asserting that completion, a generic Kloosterman large sieve, the prime-field trace theorem, or a uniform rational square-root transform closes \(J^{17/30}<|d|\ll Q^2\).  Record (84.H31) as the hostile prime-power control and record transform self-return as a no-saving warning.  This round should reduce the unresolved \(d\)-range, not claim a \(B\)-power or conductor gain.

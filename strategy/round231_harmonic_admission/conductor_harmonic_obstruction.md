# Full harmonic pooling at fixed squarefree labels: a scoped obstruction

Conductor candidate, 11 October 2026. Phase: user-requested Round231 admission, not an analytic campaign or graph promotion. Starting graph SHA256: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. The conductor independently derived the shell union bound and a fixed-cutoff/sign-coherence proof. The sharper common-harmonic coefficient majorant below was supplied by the discovery agent and independently checked by the conductor; it replaces the unnecessary sign-coherence restriction. A separate statement-only rederivation and nonauthor seam review are required before final disposition.

## 1. Result

Let the full actual class waves be

\[
f_d(R)=\sum_{s\ge1}r_2(ds^2)(ds^2)^{-3/4}
\Psi(s\sqrt{d/T})\cos(2\pi R s\sqrt d-3\pi/4).
\]

For ordered, pairwise distinct squarefree labels \(d_1,\ldots,d_{12}>Q=\lfloor T^{2/5}\rfloor\), define

\[
J_{\boldsymbol d}(T)=\int w(R/T)\prod_{j=1}^{12}f_{d_j}(R)\,dR,
\qquad \mathcal C_{\rm harm}(T)=\sum_{\boldsymbol d}|J_{\boldsymbol d}(T)|.
\]

There are constants \(c,T_0>0\), depending only on the fixed functions, such that

\[
\boxed{\mathcal C_{\rm harm}(T)\ge cT^{5/2}\quad(T\ge T_0).}
\tag{H}
\]

The full infinite harmonic sum and every cosine sign are pooled before each modulus. Thus this is a fresh obstruction at the ordering of operations requested by the user. It is not inferred from the earlier fixed-norm certificate. It gives no lower bound on \(I_{12}=\sum_{\boldsymbol d}J_{\boldsymbol d}\), or on the complete moment.

## 2. Exact hypotheses

Use the fixed nonnegative real radial smooth unit-mass mollifier supported in the unit disk, \(\Psi(s)=\widehat\rho(se_1)\), and the fixed nonnegative smooth window \(w\), supported in \([1/2,2]\) and with positive integral \(W\). Hence \(\Psi\) is real, even and Schwartz, \(\Psi(0)=1\), and \(|\Psi|\le1\); it is allowed to change sign. The Fourier convention is \(\widehat w(\xi)=\int w(u)e(-u\xi)du\). All \(T\) are real. Coefficients are the actual \(r_2(n)=4\sum_{k\mid n}\chi_4(k)\).

The proof uses the elementary disk-area count, the elementary divisor bound, and absolutely convergent harmonic coefficient series. No squarefree density theorem, equidistribution assumption, prime-number estimate, arbitrary-coefficient upper bound or source transfer is used.

## 3. Proof

### A. A positive mass of actual squarefree base norms

For every fixed \(0<u<v\),

\[
\sum_{\substack{uT\le d\le vT\\d\ {m squarefree}}}r_2(d)
\ge \frac{\pi(v-u)}{24}T-O_{u,v}(\sqrt T\log(2T)).
\tag{1}
\]

Indeed, the prime-factor formula gives \(r_2(4m)=r_2(m)\) and \(r_2(p^2m)\le3r_2(m)\) for each odd prime, including zero coefficients. Apply the area count on every rescaled interval \([uT/p^2,vT/p^2]\). Its error is \(O(\sqrt T/p+1)\), including real endpoints. Sum this over all primes \(p\le\sqrt{vT}\), bounding primes by integers, for total error \(O(\sqrt T\log(2T))\). The entire nonsquarefree main mass costs at most

\[
\frac14+3\sum_{p\text{ odd}}p^{-2}
\le\frac14+3\sum_{j\ge3,\ j\text{ odd}}j^{-2}
\le\frac14+3\left(\frac19+\frac18\right)=\frac{23}{24}.
\]

The \(1/8\) bound follows by telescoping \((2k+1)^{-2}\le[4k(k+1)]^{-1}\) for \(k\ge2\). Subtracting from the whole interval count proves (1). Every square divisor and its accumulated error is paid. The separate isolated arithmetic report independently proves the same inequality with explicit error constants.

Choose a fixed small \(c_0>0\) so that \(\Psi(\sqrt x)\ge1/2\) on \([c_0,2c_0]\). On the squarefree shell \(\mathcal D_T=[c_0T,2c_0T]\), retain labels with \(r_2(d)>0\), and put

\[
b_d=r_2(d)d^{-3/4}\Psi(\sqrt{d/T}),\qquad
M=\sum_{d\in\mathcal D_T}b_d,\qquad b_* =\max b_d.
\]

For sufficiently large \(T\), all these labels exceed \(Q\), and

\[
M\asymp T^{1/4},\qquad b_*\ll_\eta T^{-3/4+\eta},
\qquad \sum_d b_d^2\le b_*M.
\tag{2}
\]

The lower bound uses (1); the upper bound uses the full shell lattice count. The selected labels really are squarefree base norms, not squarefree parts with hidden harmonics.

### B. Actual arithmetic makes common harmonic multiples small

Define

\[
g(s)=\prod_{p\equiv1\ (4)}(2v_p(s)+1).
\]

For retained squarefree \(d\), the exact local factors imply

\[
0\le\frac{r_2(ds^2)}{r_2(d)}\le g(s).
\tag{3}
\]

At split primes dividing \(d\), the ratio is \(v_p(s)+1\), and otherwise it is \(2v_p(s)+1\). Prime 2 and inert primes contribute one. There is no division by zero because zero base coefficients were excluded; their full class waves vanish anyway.

Write

\[
f_d(R)=b_d\sum_{s\ge1}q_d(s)\cos(2\pi R s\sqrt d-3\pi/4),
\quad q_d(1)=1,
\quad |q_d(s)|\le \ell_s:=2g(s)s^{-3/2}.
\tag{4}
\]

The signs of \(\Psi\) at higher harmonics are retained in \(q_d\). Since \(g(s)\le\tau(s^2)\le\tau_3(s)\),

\[
K:=\sum_s\ell_s<\infty,\qquad R_H:=\sum_{s>H}\ell_s\longrightarrow0.
\tag{5}
\]

The following sharper twelfth-product estimate is the useful arithmetic control:

\[
S:=\sum_{h\ge2}g(h)^{12}h^{-18}<\frac1{200000}.
\tag{6}
\]

For its proof, \(2e+1\le3^e\) and \(3^4<5^3\) imply \(g(h)\le h^{3/4}\), because every split prime is at least 5. Also \(g(2)=g(3)=g(4)=1\). Hence, by a decreasing-integrand tail bound,

\[
S\le 2^{-18}+3^{-18}+4^{-18}+5^{-9}+\frac1{8\cdot5^8}
<\frac1{200000}.
\tag{7}
\]

The last comparison is an exact rational inequality, not a decimal experiment. It implies

\[
2^{-12}-2S>2^{-13}.
\tag{8}
\]

### C. Fix the complete harmonic-tail and Fourier-tail budgets

Choose a sufficiently large fixed integer \(H\ge2\), before \(T\), so that

\[
12K^{11}R_H\le2^{-16}.
\tag{9}
\]

Let \(f_d^{\le H}\) be the finite harmonic truncation. Telescoping products and (4)--(5) give, for each shell label tuple,

\[
\left|J_{\boldsymbol d}-\int w(R/T)\prod_j f_{d_j}^{\le H}(R)dR\right|
\le 2^{-16}TW\prod_j b_{d_j}.
\tag{10}
\]

This controls the whole infinite mixed tail, including all tuples with at least one large harmonic. It is a relative bound for each label tuple, not a truncation of the definition of the target. The bound follows from \(|f_d|,|f_d^{\le H}|\le Kb_d\) and \(|f_d-f_d^{\le H}|\le R_Hb_d\).

Fix \(\delta>0\), for example any \(\delta\le1/12\), so that \(\operatorname{Re}\widehat w(\xi)\ge W/2\) for \(|\xi|\le\delta\). Choose a fixed \(\Lambda>\delta\) with

\[
\sup_{|\xi|>\Lambda}|\widehat w(\xi)|\le\frac{W}{2^{16}K^{12}}.
\tag{11}
\]

Existence follows from smooth Fourier decay. \(H,\delta,\Lambda\) and all their constants remain fixed as \(T\) tends to infinity.

### D. Retain many near-resonant label tuples

Let \(\sigma=(1,1,1,1,1,1,-1,-1,-1,-1,-1,-1)\). Binning weighted ordered sixfold root sums into intervals of width \(\delta/T\), in a range of length \(O(\sqrt T)\), gives product mass

\[
\gg \frac{M^{12}}{T^{3/2}}\gg T^{3/2}
\tag{12}
\]

with \(|\sum_j\sigma_j\sqrt{d_j}|\le\delta/T\). At this stage repetition is allowed. For any fixed equal-label pair, leave one other coordinate for last. The near relation confines that last root to an interval of length \(O(1/T)\), so it allows at most one integer norm for large \(T\). The repeated-pair weight is at most

\[
\left(\sum_d b_d^2\right)M^9b_*\le M^{10}b_*^2
\ll_\eta T^{1+2\eta}.
\tag{13}
\]

The union over 66 pairs removes every repeat and costs \(o(T^{3/2})\) when \(\eta<1/4\).

Now consider every integer vector \(\boldsymbol t\) with \(1\le|t_j|\le H\) which is not proportional to \(\sigma\). Remove tuples also satisfying \(|\sum_jt_j\sqrt{d_j}|\le\Lambda/T\). The two coefficient rows have a nonzero integer 2-by-2 minor. Fixing the other ten norms confines each remaining root to an interval of length \(O_{H,\delta,\Lambda}(1/T)\), hence each norm to an interval of length \(O(T^{-1/2})<1\). At most one ordered pair completes the tuple, so the removed mass for that vector is at most \(M^{10}b_*^2\). There are only \((2H)^{12}\) vectors, a fixed constant. Thus a set \(\mathcal G_T\) of distinct label tuples retains weight

\[
\sum_{\boldsymbol d\in\mathcal G_T}\prod_j b_{d_j}\gg T^{3/2}.
\tag{14}
\]

The remaining bounded harmonic vectors proportional to \(\sigma\) are exactly \(\pm h\sigma\), \(1\le h\le H\). They are deliberately not discarded by the rank-two argument.

### E. The complete pooled integral is positive on these tuples

Expand all finite harmonics and cosine signs in the truncated integral. The vector \(\pm\sigma\) has six plus and six minus signs, phase coefficient one, and normalized harmonic coefficients \(q_d(1)=1\). Its combined contribution is at least

\[
2^{-12}TW\prod_j b_{d_j}.
\tag{15}
\]

For all other proportional vectors \(\pm h\sigma\), even allowing every \(h\ge2\), their combined absolute contribution is at most

\[
\frac{2TW}{2^{12}}\prod_jb_{d_j}
\sum_{h\ge2}\prod_j|q_{d_j}(h)|
\le 2STW\prod_jb_{d_j}.
\tag{16}
\]

This uses (3)--(6), retains the signs of \(\Psi\), and needs no positivity assumption on those higher common harmonics. By (8), the total proportional contribution is greater than \(2^{-13}TW\prod b_d\).

For every nonproportional bounded vector on \(\mathcal G_T\), the Fourier argument exceeds \(\Lambda\). The sum of its absolute normalized Fourier coefficients, including all cosine signs and the factor \(2^{-12}\), is at most \(K^{12}\). By (11), their entire contribution has absolute value at most \(2^{-16}TW\prod b_d\). Adding the already paid full tail (10) leaves

\[
J_{\boldsymbol d}(T)\ge 2^{-14}TW\prod_jb_{d_j}>0
\qquad(\boldsymbol d\in\mathcal G_T).
\tag{17}
\]

Finally sum these positive, fully pooled class integrals inside \(\mathcal C_{\rm harm}\). Equation (14) proves (H).

### F. Completeness and restoration

For fixed \(T\), \(\sum_n|a_n(T)|<\infty\), so all full harmonic series, products and integrated sums in the statement converge absolutely. In fact the area count and Schwartz decay give \(\sum_n|a_n|\ll T^{1/4}\), hence \(\mathcal C_{\rm harm}\ll T^4\). The lower proof selects a positive set of fixed label tuples from this complete nonnegative certificate; it never deletes a complementary term of the signed \(I_{12}\).

The accepted216 reduction still pays the head at \(T^{15/13+\varepsilon}\) and repeated-class error at \(T^{8\beta-1/5+\varepsilon}\). A bound \(\mathcal C_{\rm harm}\ll T^{29/25+\varepsilon}\) would suffice for the desired complete moment, but (H) rules out precisely that proposed bound (indeed for any exponent below \(5/2\)). It does not rule out \(|\sum J_{\boldsymbol d}|\ll T^{29/25+\varepsilon}\), because different squarefree-label tuples may cancel before a final modulus.

## 4. First unproved step

No target-sized signed bound across different squarefree-label tuples is supplied. Pooling harmonics is an exact permissible regrouping, but following it by absolute values at each label tuple still loses essential cancellation. Neither the preferred twelfth moment, a pointwise improvement, nor the quarter theorem follows. The candidate obstruction requires the stated independent checks before being retained as reviewed evidence; graph promotion would require its own protocol gates.

## 5. Controls

The new shell proof checks prime 2 separately; pricing it by three would lose the positive union margin. The coefficient control uses the smallest split prime 5: replacing actual arithmetic by \(\tau(s^2)\) at \(s=2\) would not justify the tiny common-multiple bound. Proportional vectors are retained, never treated as rank two. All fixed cutoffs precede the \(T\) limit, all infinite tails are paid per tuple, \(w\) need not be even, and \(\Psi\) may change sign. Fixed real interval endpoints and zero coefficients are accounted for.

The exact inequalities (7)--(8) and the square-divisibility fraction were checked by Wolfram and independently reproduced with rational arithmetic locally. Those controls are diagnostic; the analytical proof does not rely on finite numerical sampling or a computed asymptotic.

## 6. Dependencies and provenance

Read protocol.md, the selectively parsed accepted graph, state/active_campaign.yml, state/next_round_plan.yml, the accepted216 kernel and previous admission decision/norm-tuple proof. The previous norm-tuple lower bound is a boundary control, not a logical input to (H). The squarefree-shell proof is independently rederived in reports/blind_squarefree_mass.md. The arithmetic bound (7) is from the discovery agent's independent derivation, checked here; the conductor's full proof uses fixed rather than growing harmonic truncation. All complete target constants and implications are from the frozen brief and accepted216/204 nodes. Exact report and control hashes will be bound in the final evidence manifest. No external source is imported.

## 7. Recommended state effect

Retain the reviewed scoped obstruction if all seams pass; do not promote a complete upper bound or alter the accepted graph from this admission screen. Full harmonic pooling followed by per-label-tuple absolute values does not meet Round231's admission gate. Genuine signed cancellation across different squarefree-label tuples remains open. Preserve all previous reports and rounds and the complete pointwise/moment benchmarks.

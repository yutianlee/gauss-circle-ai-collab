# Round 85 hostile/source audit: large dual differences

## 1. Result

**Result: source-audited no-go for the presently available black boxes, together with one narrow direct deletion at the extreme support difference.**  No current primary-source theorem found in the audit literally estimates the large-difference survivor
\[
\mathfrak Y_{>D_0}^{(\kappa,k)}
=
\sum_{b\asymp B}M_b^{-2}
\sum_{\substack{|d|>D_0\\ d\ne0}}\sum_n
A_{M_b,K_b,d}(n)I_b(n+d)\overline{I_b(n)}
\]
for all three local classes, both signs of \(d\), the reflected/conjugate orientations, unrestricted composite \(b\), and the actual \(b,d,n\)-coupled stationary weight, while retaining the accepted physical saving \(Q^{-5/24}\) per row (equivalently \(Q^{-5/12}\) at energy level).  In particular, no interior dyadic conductor range, no shell in \(C\), and no power \(B^{-\delta}\) is supplied by the literature.

There is, however, a direct support-edge lemma independent of those sources.  Let \(\Delta_b\) be the diameter of the actual principal stationary \(n\)-support for the relevant local class.  For every fixed \(\delta>0\), the outer range
\[
 |d|\ge \Delta_b-Q^2J^{-\delta}
\]
is target-safe for this smooth-principal component: in the inner collar the two main symbols are flat at opposite support endpoints, outside \(\Delta_b\) there is no main–main overlap, and the uniform Round-84 pointwise stationary remainder plus nonstationary tails close absolutely over the whole outer range.  This assertion requires normalized derivative bounds through a finite order \(R=R(\delta)\), and is not uniform as \(\delta\to0\).  It does not apply to the separately owned raw Round-81 transition remainder.

After that deletion, the literal \(A\)-process in \(d\) has a target-safe diagonal for the remaining principal stationary term.  Its off-diagonal is, however, a four-Kloosterman correlation with the full physical weight.  That is the first exact unsupported estimate.  Standard bilinear theorems concern one Kloosterman kernel; the closest four-product theorem located is squarefree-modulus only and has explicit gcd exceptional factors.  Prime-power modulus multiples furnish large nonzero Fourier modes, and perfect-square/fourth-power values of \(n\) furnish exact large-\(d\) phase coherence.  These facts invalidate coefficientwise square-root and blanket nonresonance shortcuts.  The exact perfect-power lattice is sparse enough to be removed absolutely from the principal main term, but that does not estimate its complement.

Thus the useful outcome is a rigorous outer-collar deletion, a route-specific no-go on the remaining interior, and an exact statement of what a future theorem must prove.  It is not a whole-range bound for \(\mathfrak Y_{>D_0}^{(\kappa,k)}\).

## 2. Exact statement and hypotheses

The audit fixes the packet's one transition-flattened smooth nonaxial principal component, one compatible nonzero pair \(k=\rho\sigma>0\), and one endpoint orientation (with its reflected/conjugate analogue).  It uses only the frozen Round-85 regime
\[
J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
B=C/T,\qquad J^{13/18}<C\le J^{3/4},
\]
so
\[
J^{11/90}<B\le J^{3/20},\qquad N:=Q^2=J^{4/5},
\qquad D_0=\lfloor J^{17/30}\rfloor .
\]
For a fixed \(b\asymp B\), the three local triples are
\[
(g,M,K)=(1,4b,k),\quad
(2,2b,2[k\bar4]_b),\quad
(4,b,[k\bar4]_b),
\]
hence \(gM=4b\) and \(M\asymp B\).  No coprimality assumption \((d,M)=1\), no squarefreeness assumption on \(M\), and no restriction to \(d>0\) is permitted.  In particular, nonzero \(d\equiv0\pmod M\) belong to the survivor.

The arithmetic coefficient and its exact complete transform are
\[
A_{M,K,d}(n)
=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d),
\]
\[
\sum_{r\bmod M}A_{M,K,d}(r)=0,\qquad
M^{-2}\sum_{r\bmod M}|A_{M,K,d}(r)|\le2,
\]
and, for \(h\ne0\bmod M\),
\[
\widehat A_{M,K,d}(h)
=M\mathcal C_{M,K}(d,h),
\]
\[
\mathcal C_{M,K}(d,h)
=\sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
e_M\!\left(d(y+h)+K\big((y+h)^{-1}-y^{-1}\big)\right).
\]
The Ramanujan subtraction contributes only to the zero Fourier mode.

On the principal stationary branch,
\[
I_{b,\eta}(\eta m)
=e(-\eta\lambda_b\sqrt m)\mathcal P_{b,\eta}(m),
\qquad
\lambda_b=J+\frac{\sqrt{\kappa k}}b .
\]
Writing \(w_b=I_b/M_b\), the supplied principal profile has
\[
\|w_b\|_\infty+\operatorname{Var}(w_b)\ll X^\epsilon J^{-1/10}
\]
on each relevant progression, while \(n,n+d\asymp N\) away from transition tails.  More precisely, for the accepted Round-81 principal cutoff \(V_b\), let
\[
x_{b,-}:=\inf\operatorname{supp}V_b,\qquad
x_{b,+}:=\sup\operatorname{supp}V_b,
\]
and use the monotone saddle map
\[
m_b(x)=\frac{A_bM_b}{g x^2},\qquad
A_b:=\left(\sqrt{bX}+\sqrt{\frac{\kappa k}{b}}\right)^2,\qquad
P_b:=\frac{A_b}{gC}\asymp JQ.
\]
Thus
\[
\frac{A_bM_b}{gC^2}\asymp N.
\]
The unsigned stationary main support is contained in
\[
\mathcal S_b=[\alpha_b,\beta_b]
:=[m_b(x_{b,+}),m_b(x_{b,-})],\qquad
\Delta_b:=\beta_b-\alpha_b\asymp N.
\]
The reflected orientation replaces \(\mathcal S_b\) by \(-\mathcal S_b\), without changing \(\Delta_b\).  The extension of \(V_b\) by zero is compactly supported \(C^\infty\), and for every fixed order needed below,
\[
\sup_x |(C\partial_x)^jV_b(x)|\ll_{j,\epsilon}X^\epsilon.
\tag{2.1}
\]
The stationary expansion has normalized pointwise remainder
\[
e_0:=\frac{C}{M_bP_b}\asymp J^{-4/5}
\tag{2.2}
\]
through a fixed enlarged \(m\asymp N\) band, and is arbitrarily summable outside that band and on the wrong stationary sign.  Equations (2.1)–(2.2) concern the Fourier transform of \(V_b\), not the separately owned raw Round-81 transition remainder \(E\).

The physical rows satisfy
\[
|R_b(r)|\ll X^\epsilon TQ^{-5/24},
\qquad
R_b(r)=
\sum_{\substack{c\asymp C\\c\equiv r\ (4b)}}
V_{b,c,k}^{(\kappa)}e(\pm A_{\kappa,b}/c).
\]
Any acceptable dual estimate must retain this factor, or its square \(Q^{-5/12}\), rather than replace the row by a coefficient-blind norm.

For a dyadic interval \(\mathcal D\subset\{d:D_0<|d|\ll N\}\) of length \(D\), set
\[
Z_b(d):=M_b^{-2}\sum_n A_{M_b,K_b,d}(n)
I_b(n+d)\overline{I_b(n)}.
\]
The required block target is
\[
\sum_{b\asymp B}\sum_{d\in\mathcal D}Z_b(d)
\ll X^\epsilon J^2/T=X^\epsilon J^{7/5}.
\]
Logarithmically many blocks are absorbed by \(X^\epsilon\).  The source audit asks whether a published theorem supplies this estimate with the hypotheses above; it does not.

## 3. Proof or derivation

**Normalization and the \(A\)-process diagonal.**  For the principal stationary term, \(I_b=M_bw_b\), and therefore
\[
Z_b(d)=\sum_n A_{M_b,K_b,d}(n)
w_b(n+d)\overline{w_b(n)}.
\]
Splitting \(n\) into residue classes modulo \(M_b\), using the exact periodic \(L^1\) bound and \(N/M_b+O(1)\) available points per class, gives
\[
|Z_b(d)|
\ll X^\epsilon J^{-1/5}\frac{N}{M_b}
\sum_{r\bmod M_b}|A_{M_b,K_b,d}(r)|
\ll X^\epsilon M_bN J^{-1/5}.
\tag{3.1}
\]
This calculation is where the original \(M_b^{-2}\) normalization is spent; using an unnormalized Kloosterman theorem without restoring it changes the power of \(B\).

Extend \(Z_b(d)\) by zero outside \(\mathcal D\).  For \(1\le H\le D\), the literal Fejér/van-der-Corput inequality and then Cauchy in \(b\) give
\[
\left|\sum_{b\asymp B}\sum_{d\in\mathcal D}Z_b(d)\right|^2
\le
B\,\frac{D+H}{H^2}
\left(
H\mathcal E_0+2\mathcal E_1
\right),
\tag{3.2}
\]
where
\[
\mathcal E_0=\sum_{b\asymp B}\sum_{d\in\mathcal D}|Z_b(d)|^2
\]
and one may take
\[
\mathcal E_1=
\sum_{b\asymp B}\sum_{1\le h<H}(H-h)
\left|\sum_d Z_b(d+h)\overline{Z_b(d)}\right|.
\tag{3.3}
\]
The factors \(B(D+H)H^{-2}\), \(H\), and \(H-h\) are all compulsory.  With \(H=D\), (3.1) makes the square root of the diagonal contribution at most
\[
X^\epsilon B^2D^{1/2}NJ^{-1/5}
\le X^\epsilon J^{13/10},
\tag{3.4}
\]
because \(B\le J^{3/20}\) and \(D\le N=J^{4/5}\).  Thus the principal diagonal is below \(J^{7/5}\).  The stationary errors are aggregated separately below.

The off-diagonal expands exactly as
\[
\sum_d Z_b(d+h)\overline{Z_b(d)}
=M_b^{-4}\sum_{d,n,m}
A_{d+h}(n)\overline{A_d(m)}
I_b(n+d+h)\overline{I_b(n)}
\overline{I_b(m+d)}I_b(m).
\tag{3.5}
\]
Opening the two \(A\)'s produces a four-Kloosterman main term plus both Ramanujan cross terms and the Ramanujan-square term.  The variables \(b,d,h,n,m\) remain coupled through support, endpoints, \(\lambda_b\), and the stationary amplitudes.  To reach the target through (3.2), a sufficient literal missing estimate is
\[
\boxed{\quad
\mathcal E_1
\ll X^\epsilon
\frac{H^2}{B(D+H)}J^{14/5},
\quad}
\tag{3.6}
\]
with (3.5), all local classes and orientations, negative differences, modulus multiples, and the actual main/error decomposition.  No audited source has (3.6) as a theorem or a specialization.

**Prime-power control.**  Let \(q=p^\nu\), where \(p\) is odd, \(\nu\ge2\), and \(p\nmid K\).  Take a surviving nonzero modulus multiple \(d=tq\), and take
\[
h=p^{\nu-1}\alpha,\qquad p\nmid\alpha .
\]
Since \(h^2\equiv0\pmod{p^\nu}\),
\[
(y+h)^{-1}-y^{-1}\equiv-p^{\nu-1}\alpha y^{-2}
\pmod{p^\nu},
\]
and \(y+h\) is a unit exactly when \(y\) is.  Consequently
\[
\mathcal C_{q,K}(tq,h)
=p^{\nu-1}\sum_{z\bmod p}^{*}
e_p(-K\alpha z^{-2})
=p^{\nu-1}\bigl(G_p(-K\alpha)-1\bigr),
\tag{3.7}
\]
where \(G_p\) is the quadratic Gauss sum.  Hence
\[
|\mathcal C_{q,K}(tq,h)|\asymp p^{\nu-1/2}
=q^{1-1/(2\nu)}
\]
and
\[
|\widehat A_{q,K,tq}(h)|
\asymp q^2p^{-1/2}=q^{\,2-1/(2\nu)}.
\tag{3.8}
\]
For \(\nu=2\) and \(4\), these are respectively \(q^{7/4}\) and \(q^{15/8}\).  The centering \(c_q(tq)\) does not alter (3.8), because \(h\ne0\).  Choosing \(b=q\) in the \(M=b\) class gives a literal member of the family; CRT gives the same local obstruction inside \(b,2b,4b\), subject only to compatible bounded \(2\)-adic factors.  Multiples \(tM\) exist between \(D_0\) and a fixed fraction of \(N\), since \(M\asymp B\ll D_0\ll N\).  The same calculation applies to negative \(t\).  Thus a uniform coefficientwise bound \(|\widehat A(h)|\ll M^{3/2+\epsilon}\), or any argument that silently declares \(d\equiv0\pmod M\) harmless after centering, is false.

**Perfect-power phase control.**  A uniform nonresonance assertion also fails.  It suffices to take an allowed subsequence with \(J\in\mathbb Z\) and \(\sqrt{\kappa k}=s\in\mathbb Z\).  If
\[
n=u^2,\qquad n+d=v^2,\qquad b\mid(v-u),
\]
then
\[
\lambda_b(\sqrt{n+d}-\sqrt n)
=J(v-u)+s(v-u)/b\in\mathbb Z.
\tag{3.9}
\]
There are such points with \(u,v\asymp Q\) and \(|d|>D_0\).

There is also an explicit fourth-power family throughout the frozen \(B\)-range.  Choose \(a\asymp J^{1/5}\) and put
\[
n=a^4,\qquad n+d=(a+b)^4.
\]
Then \(n,n+d\asymp N\),
\[
\sqrt{n+d}-\sqrt n=(a+b)^2-a^2=b(2a+b),
\]
so (3.9) is again integral, while
\[
d=(a+b)^4-a^4\asymp J^{3/5}B,
\]
which lies strictly between \(D_0=J^{17/30}\) and \(N=J^{4/5}\) because
\(J^{11/90}<B\le J^{3/20}\).  Swapping the two fourth powers gives negative \(d\).  Thus first-derivative arguments must isolate resonant points rather than assume they do not occur.

This exact lattice is not itself too large for the principal main term.  For each \(b\), the number of ordered square-square pairs in the support is \(O(Q^2)=O(N)\).  The trivial bounds \(|A_d(n)|\ll M^2\) and
\(|w_b(n+d)w_b(n)|\ll X^\epsilon J^{-1/5}\) give
\[
\sum_{b\asymp B}\!
\sum_{\substack{n,n+d\ {\rm squares}\\n,n+d\asymp N}}
|A_d(n)w_b(n+d)\overline{w_b(n)}|
\ll X^\epsilon B^3NJ^{-1/5}
\le X^\epsilon J^{21/20}.
\tag{3.10}
\]
Fourth-fourth pairs are fewer, \(O(Q)\) per \(b\).  Therefore exact perfect-power points may be removed absolutely from the principal term, but (3.10) supplies no cancellation for the non-perfect-power complement.  The large-\(d\) error budget is checked separately in (3.16).

**Extreme stationary-support-difference collar.**  This is a direct check of the conductor fallback, not an application of any source in the table below.  Fix \(\delta>0\), independently of \(X\), and put
\[
W:=NJ^{-\delta}.
\]
It is enough to treat \(0<\delta\le4/5\); for larger \(\delta\), the collar is a subset of the one with \(\delta=4/5\).

Suppose first that \(d>0\) and
\[
\Delta_b-W\le d\le\Delta_b.
\tag{3.11}
\]
If both stationary main symbols are nonzero, then \(n\in\mathcal S_b\) and \(n+d\in\mathcal S_b\).  With
\[
s_d:=\Delta_b-d,
\]
this forces
\[
0\le n-\alpha_b\le s_d,\qquad
0\le\beta_b-(n+d)\le s_d.
\tag{3.12}
\]
Because \(m_b(x)\) is monotone and \(|m_b'(x)|\asymp N/C\) on \(x\asymp C\), (3.12) places the two saddles within
\(O(Cs_d/N)\) of the opposite endpoints of \(\operatorname{supp}V_b\).  A compactly supported \(C^\infty\) function extended by zero has every derivative zero at an extreme support endpoint.  Taylor's theorem and (2.1) therefore give, for every fixed \(R\),
\[
\left|\frac{I_b^{\rm main}(n)}{M_b}
\frac{I_b^{\rm main}(n+d)}{M_b}\right|
\ll_{R,\epsilon}
X^\epsilon J^{-1/5}
\left(\frac{s_d+1}{N}\right)^{2R}.
\tag{3.13}
\]
Here the harmless \(+1\) accommodates the integer lattice.  The same assertion holds for \(d<0\) after interchanging the two variables, and for the reflected orientation after replacing \(\mathcal S_b\) by \(-\mathcal S_b\).  The constants \(g=1,2,4\) only change the endpoints by bounded factors.

For any interval of \(L\) consecutive integers, periodicity and the exact residue \(L^1\) bound give
\[
\sum_{n\ {\rm in\ the\ interval}}|A_{M,K,d}(n)|
\ll M L+M^2.
\tag{3.14}
\]
Using (3.12)–(3.14), summing the at most \(O(W+1)\) admissible integer values of \(d\), both signs, and \(b\asymp B\), yields
\[
\mathfrak Y_{\rm collar}^{\rm main-main}
\ll_{R,\epsilon}X^\epsilon
\left(B^2J^{-1/5}W^2+B^3J^{-1/5}W\right)
\left(\frac{W+1}{N}\right)^{2R}.
\tag{3.15}
\]
When \(W\ge1\), the two displayed contributions are at most
\[
X^\epsilon
\left(
J^{17/10-(2R+2)\delta}
+J^{21/20-(2R+1)\delta}
\right).
\]
Choosing a finite \(R=R(\delta)\) with
\[
(2R+2)\delta>3/10
\]
makes (3.15) \(O(X^\epsilon J^{7/5})\), with room to absorb endpoints.  When \(W<1\), the integer collar has \(O(1)\) elements and Taylor flatness at scale \(N^{-1}\) gives an even smaller bound.  This proves the main–main collar claim for every fixed \(\delta>0\), but not uniformly in \(\delta\).  It also shows the precise dependency seam: a graph interface recording only one preassigned finite derivative order does not imply the assertion for arbitrarily small \(\delta\); the normalized \(C^\infty\) hierarchy through \(R(\delta)\) must be cited.

The pointwise stationary remainder is sufficient for the exact, rather than main-only, deletion.  Over all \(O(N)\) effective differences—not merely the collar—the main–error and error–error contributions are, by (2.2) and (3.14),
\[
\begin{aligned}
\mathfrak Y^{\rm main-error}
&\ll X^\epsilon B^2N^2J^{-1/10}J^{-4/5}
\ll X^\epsilon J^1,\\
\mathfrak Y^{\rm error-error}
&\ll X^\epsilon B^2N^2J^{-8/5}
\ll X^\epsilon J^{3/10}.
\end{aligned}
\tag{3.16}
\]
The \(M^2\) remainder in (3.14) is smaller because \(M\ll N\).  Outside the fixed enlarged stationary band, repeated integration by parts may be taken to a fixed order larger than the polynomial number of \(b,d,n\) choices; the wrong-sign and nonstationary tails are then \(O(J^{-A})\) after summation.  For \(|d|>\Delta_b\), the main–main product is identically zero, so (3.16) and those tails own the entire term.

Consequently the exact smooth-principal survivor may be reduced, for any one fixed \(\delta>0\), to
\[
D_0<|d|<\Delta_b-NJ^{-\delta}.
\tag{3.17}
\]
This is a target-safe range deletion, not a \(B\)-power gain and not a bound for the interior survivor.  It uses no physical/dual Cauchy step, so it does not discard the accepted \(Q^{-5/24}\) row estimate from the remaining problem.

**Literal primary-source map.**

| Primary source and exact usable object | Literal applicability verdict |
|---|---|
| Blomer–Pascadi, [Bilinear forms with Kloosterman sums via quadratic characters, Theorem 1.1, arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311), treats one fixed modulus \(c\) and a bilinear form \(\sum_{m,n}\alpha_m\beta_nS(am,n;c)\); its critical saving requires two genuinely populated variables. | Not (3.5): one Kloosterman kernel, two separated coefficient sequences, and no shifted product or \(b,d,n\)-coupled stationary symbol.  Compressing the present \(n\)-sum modulo \(M\) leaves a full residue interval against a singleton, not the critical two-variable regime. |
| Pascadi, [Non-abelian amplification and bilinear forms with Kloosterman sums, arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445), proves Type-II estimates for a single fixed-modulus Kloosterman kernel, with a controlled varying-modulus corollary. | Not a theorem for a shifted product \(S(n+d,K;M)\overline{S(n,K;M)}\), still less the four-product (3.5).  Its modulus averaging does not import the physical row factor. |
| Milićević–Qin–Wu, [Bilinear forms with Kloosterman sums and moments of twisted \(L\)-functions, Theorem 1.1, arXiv:2511.07550v1](https://arxiv.org/abs/2511.07550), bounds \(\sum_{m\le M,n\le N}\alpha_m\beta_n\mathrm{Kl}_2(cmn;q)\) for arbitrary \(q\), under stated length inequalities. | The actual fixed-column specialization has one variable of length \(1\); the theorem's displayed factor contains \(M^{-1/2}q^{1/6}\), hence is not saving there.  Its kernel is one normalized \(\mathrm{Kl}_2\), not \(A_d\) or (3.5). |
| Fouvry–Kowalski–Michel, [A study in sums of products, Corollaries 1.6 and 3.3, arXiv:1405.2293v2](https://arxiv.org/abs/1405.2293), gives square-root cancellation for normal tuples of bounded-conductor bountiful trace functions over a prime field. | Useful only for prime local models after checking tuple normality.  It excludes prime powers and the \(2\)-part, and (3.7) is exactly an exceptional aligned tuple.  The real stationary weight depending on \(X,b,d\) is not a bounded-conductor finite-field trace function. |
| Milićević–Zhang, [Distribution of Kloosterman paths to high prime power moduli, arXiv:2005.08865v1](https://arxiv.org/abs/2005.08865), treats complete products at powers of one fixed odd prime and separates \(p\)-adically colliding/power-aligned configurations. | It supplies no uniform square-root estimate in the aligned case (3.7), no varying arbitrary composite modulus, no \(2\)-adic component, and no physical stationary weight. |
| Zheng, [Primes in simultaneous arithmetic progressions, Lemma 2.8, arXiv:2512.22798v1](https://arxiv.org/abs/2512.22798), has the closest arithmetic shape: for squarefree \(q\), a four-shift product \(Y(t)\) has \(\widehat Y(v)\ll q^{2+\epsilon}(\ell_1,v,q)^{1/2}(\ell_2,v,q)^{1/2}(\xi,\ell_1,\ell_2,q)^{3/2}\). | Not all classes: \(M=b,2b,4b\) is unrestricted and has prime-power and \(2\)-adic factors.  The displayed gcd losses include precisely the hostile aligned shifts.  The lemma is complete and unweighted; it neither estimates (3.5) with its joint symbol nor preserves \(Q^{-5/12}\). |
| Kerr–Shparlinski–Wu–Xi, [Bounds on bilinear forms with Kloosterman sums, Lemma 4.1, arXiv:2204.05038v5](https://arxiv.org/abs/2204.05038), proves an arbitrary-\(q\), gcd-sensitive complete identity/bound for \(q^{-1}\sum_t\mathscr K_q(x,t)\mathscr K_q(y,t)e_q(-zt)\). | The two kernels share the same varying second argument \(t\), with fixed \(x,y\).  The present pair has shifted first arguments \(n+d,n\) and fixed \(K\) (or, after symmetry, shifted second arguments).  There is no literal substitution; further completion returns \(\mathcal C(d,h)\) with (3.7). |
| Blomer–Milićević, [The second moment of twisted modular \(L\)-functions, Theorem 5, arXiv:1404.7845v1](https://arxiv.org/abs/1404.7845), bounds incomplete sums \(\sum_m S(m,n_1;r)S(m,n_2;r)\) with fixed \(n_1,n_2\) and factorability data. | The actual two first arguments are \(n+d\) and \(n\), so they do not share the theorem's common summation argument.  The factorability and fixed-weight hypotheses also do not encode the \(b,d,n\)-dependent symbol. |
| Xi–Zheng, [On the Brun–Titchmarsh theorem II, arXiv:2504.12692v3](https://arxiv.org/abs/2504.12692), obtains a specialized shifting estimate for quintilinear Kloosterman structures at a large prime modulus. | Prime modulus and source-specific separated variables; not arbitrary \(b,2b,4b\), not (3.5), and no physical-row preservation statement. |
| Lin–Michel, [On algebraic twists with composite moduli II, arXiv:2605.06363v1](https://arxiv.org/abs/2605.06363), treats \(\mathrm{GL}_3\) automorphic coefficients against factored composite-modulus trace functions. | Its coefficients, modulus factorization, and separated smooth weight are not those of (3.5).  It is not a four-Kloosterman correlation theorem. |

The claimed improvement in Dong–Robles–Zeindler, [Bilinear forms with Kloosterman fractions and applications, arXiv:2601.00292v2](https://arxiv.org/abs/2601.00292), cannot be used: the authors withdrew it and state that a missing \(L^2\) factor destroys the claimed improved bound.  The accepted Kuznetsov/large-sieve route already audited in Round 82 remains coefficient-blind at capacity \(BQ^2T=BJ^2/T\); it loses a factor \(B\) and does not preserve the physical \(Q^{-5/12}\) energy gain.

**Self-return and actual errors.**  Fourier completion of \(A_d\) is not a simplification: it returns the complete correlation \(\mathcal C_{M,K}(d,h)\), and (3.7) shows that its exceptional modes can be nearly of trivial size.  Differencing instead returns the four-product (3.5).  A second completion therefore alternates between equivalent shifted-product objects; none of the source theorems removes the coupled real weight.

The Round-84 promoted statement aggregated stationary errors only for \(0<|d|\le D_0\), so it could not simply be quoted at large differences.  Equation (3.16) is the required independent re-audit: the uniform normalized pointwise error \(e_0=J^{-4/5}\), periodic residue \(L^1\), \(O(N)\) effective \(n\)'s, and \(O(N)\) effective \(d\)'s give total exponents \(1\) and \(3/10\), both below \(7/5\).  Repeated integration by parts owns the complement.  Therefore these errors may be removed before applying the \(A\)-process; the unresolved (3.5) may be stated with all four \(I_b\)'s replaced by their principal stationary mains.  This conclusion does not include the raw Round-81 transition remainder \(E\), which is outside the frozen smooth-principal component.

## 4. First doubtful or unproved step

The minimal unsupported step in any naked difference-dispersion proof is the signed off-diagonal estimate
\[
\mathcal V_{D,H}:=
\sum_{b\asymp B}\sum_{1\le h<H}(H-h)\,
\Re\sum_d M_b^{-4}\!\sum_{n,m}
A_{d+h}(n)\overline{A_d(m)}
I_b^{\rm main}(n+d+h)\overline{I_b^{\rm main}(n)}
\overline{I_b^{\rm main}(m+d)}I_b^{\rm main}(m)
\stackrel{?}{\ll}
X^\epsilon\frac{H^2J^{14/5}}{B(D+H)}.
\tag{4.1}
\]
It must hold uniformly on dyadic blocks of the \(b\)-dependent interior
\[
D_0<|d|<\Delta_b-NJ^{-\delta},
\]
for some effective \(1\le H\le D\), all three \(M\)-classes, both signs, reflected/conjugate phases, and \(d\equiv0\pmod M\).  Here \(I_b^{\rm main}\) denotes the principal stationary main; (3.16) has already removed every stationary-remainder term.  Bounding each \(b,h\) correlation absolutely gives the stronger sufficient envelope (3.3)–(3.6), but that extra absolute value is not claimed to be logically necessary.  Even the signed form (4.1) is absent from the audited sources.  It must also retain the physical \(Q^{-5/24}\) row factor or \(Q^{-5/12}\) energy factor.

The earliest invalid shortcut toward (4.1) is one of the following, depending on presentation:

1. replacing \(\widehat A_d(h)\) by \(O(M^{3/2+\epsilon})\) uniformly, contradicted by (3.8);
2. invoking a prime/squarefree four-trace theorem for unrestricted \(M=b,2b,4b\);
3. deleting the factors \(B(D+H)H^{-2}\), \(H\), or \(H-h\) in (3.2);
4. asserting the square-root phase has no integral/near-integral large-\(d\) locus, contradicted by (3.9);
5. applying a single-Kloosterman bilinear theorem after Cauchy while treating the remaining Kloosterman factor and the stationary profile as harmless coefficients; those coefficients depend on the same summation variables and the physical row saving has then been discarded;
6. applying the endpoint-flatness argument to the raw Round-81 transition remainder \(E\), or assuming that one finite derivative order proves the collar simultaneously for \(\delta\to0\).

Any one of these breaks the proof before a new \(C\)-range can be claimed.

## 5. Required control test and outcome

The required hostile controls and their outcomes are:

| Control | Outcome |
|---|---|
| Restore the \(M^{-2}\) normalization before estimating. | Passed algebraically: \(w=I/M\) gives (3.1).  Any source bound must state whether it uses classical \(S\) or normalized \(\mathrm{Kl}_2\). |
| Keep the complete differencing prefactor and diagonal. | Passed algebraically: (3.2) is the required form.  With \(H=D\), the principal diagonal is target-safe by (3.4); only the off-diagonal is unresolved. |
| Check the extreme support-difference collar using the actual class/orientation support. | Passed narrowly: the saddle map defines \(\Delta_b\) separately for \(M=b,2b,4b\); (3.12) forces opposite endpoint collars for both signs and both reflected orientations.  Equations (3.13)–(3.17) delete \(|d|\ge\Delta_b-NJ^{-\delta}\) for each fixed \(\delta>0\). |
| Check flatness transfer and its derivative ownership. | Passed if (2.1) is available through \(R(\delta)\): \(x_m'=O(C/N)\) transfers an \(n\)-collar of width \(s\) to an \(x\)-collar of width \(Cs/N\).  Not uniform as \(\delta\to0\), and not justified by BV alone or by one derivative order frozen independently of \(\delta\). |
| Test nonzero modulus multiples and prime powers. | Failed for uniform square-root claims: (3.7)–(3.8) give explicit large nonzero modes.  Centering removes only \(h=0\). |
| Test square/fourth-power phase coherence for both signs. | Failed for blanket nonresonance: (3.9) and the fourth-power construction give exact large-\(d\) coherence.  Passed as an isolation control for the principal term: the complete square-square lattice is bounded by (3.10). |
| Count exceptional moduli rather than call them negligible. | Perfect-square \(b\) contribute \(O(B^{1/2})\) rows, only a \(B^{-1/2}\) counting gain.  The endpoint requires \(B^{-5/9}\), so this does not close \(C=J^{3/4}\).  Perfect-fourth-power moduli are sparser, but removing them does not control the remaining prime-power or general composite rows. |
| Audit all local classes and orientations. | Passed for the direct collar: \(g\in\{1,2,4\}\) changes only bounded support constants, and reflection changes \(\mathcal S_b\) to \(-\mathcal S_b\).  Failed for the proposed literature route: prime/squarefree theorems do not cover \(b,2b,4b\) uniformly, and sign/conjugation does not remove the modulus-multiple obstruction. |
| Preserve the accepted physical row factor. | Failed for the literature route: none of the mapped theorems includes \(R_b(r)\) or proves (4.1) with \(Q^{-5/24}\) per row or \(Q^{-5/12}\) in energy.  The collar is instead bounded absolutely below target before any physical/dual Cauchy step, so it does not spend or replace the row estimate on the remaining survivor. |
| Aggregate stationary remainders and wrong-sign/nonstationary tails for \(D_0<|d|\ll N\). | Passed for the frozen smooth-principal transform: the independently recounted bounds (3.16) are \(O(X^\epsilon J)\) and \(O(X^\epsilon J^{3/10})\), and fixed-order integration by parts owns the tails.  This does not own the separately scoped raw transition remainder \(E\). |
| Check the scale gain independently. | Even an optimistic net \(B^{-1/2}\) gain reaches only \(C\le J^{56/75}\).  Closing \(C=J^{3/4}\) requires at least \(B^{-5/9}\), with all row and error factors retained. |

No numerical experiment was used.  The controls are exact algebraic calculations, counting arguments, and literal theorem-hypothesis checks.

## 6. Dependencies and exact artifacts used

Campaign: \(m9\)-\(m1\)-large-dual-difference-joint-dispersion.  Research round: 85.  Audited graph SHA-256:
\[
\texttt{942453c8d45068875932507e8ca84ed87bcb2187ee141029a27eb0c0642bf60f}.
\]

The exact repository artifacts used were:

- protocol.md;
- state/proof_obligations.yml, for the active target and the recorded Round-80–84 rejected routes;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/briefs/large_difference_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/derivation_packet.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/synthesis.md;
- rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reports/dual_difference_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/offset_trace_source_hostile_audit.md.

The exact external primary sources are linked in the theorem map in Section 3, with arXiv versions current as checked on 2026-08-16.  No sibling Round-85 report was read.  No shared state, synthesis, validation matrix, or proof draft was edited.

The conductor additionally supplied, as an explicitly unaccepted fallback claim rather than evidence, the proposed extreme support-difference collar.  Equations (3.11)–(3.17) are this report's independent hostile derivation and ownership audit of that claim.

## 7. Recommended state effect

**Promote, after the derivative-interface seam is checked, only the outer support-difference deletion (3.17) and the global stationary-remainder budget (3.16).  Retain the interior survivor and the endpoint \(C\le J^{3/4}\) as open.**  No \(B\)-gain and no new \(C\)-shell is proved.

The resulting exact smooth-principal survivor, for any fixed chosen \(\delta>0\), is
\[
\frac1{M_b^2}\sum_{b\asymp B}
\sum_{D_0<|d|<\Delta_b-NJ^{-\delta}}\sum_n
A_{M_b,K_b,d}(n)
I_b^{\rm main}(n+d)\overline{I_b^{\rm main}(n)}.
\]
The quantified statement “for every fixed \(\delta>0\)” should be promoted only if the dependency records normalized derivative bounds for every fixed order.  If the graph records merely one finite order, select one explicit \(\delta\) and verify that its required \(R(\delta)\) lies within that hierarchy.

Retain the following route information:

- the principal \(A\)-process diagonal is target-safe when the full prefactor is retained;
- the exact remaining interface is the weighted four-Kloosterman estimate (4.1);
- prime-power modulus multiples force the large modes (3.8);
- exact square/fourth-power phase resonances exist but their literal perfect-power lattice is absolutely target-safe in the principal term;
- current single-kernel, prime-field, squarefree four-product, prime-power fixed-\(p\), and generic spectral theorems do not literally prove (4.1) or preserve the physical row saving;
- the raw Round-81 transition remainder remains outside the scope of the collar lemma.

Recommended status: **promote the scoped outer deletion; retain the interior obstruction**.  A future round should proceed only if it proves (4.1) with explicit prime-power/gcd exceptional terms and the physical \(Q^{-5/12}\) energy factor, or finds a different exact survivor whose target budget is verified after all prefactors.

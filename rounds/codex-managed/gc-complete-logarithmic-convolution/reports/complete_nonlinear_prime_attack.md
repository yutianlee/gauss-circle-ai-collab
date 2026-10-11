# 1. Result

Campaign gc-complete-logarithmic-convolution, round225; discovery report, 2026-09-28. **Terminal recommendation: complete_logarithmic_convolution_no_new_bound.**

The logarithmic identity and one literal Vaughan family are valid for both character branches, with all prime powers. Their complete signed contraction has an especially restrictive feature: convolution with \(f=1*\chi_4\) cancels the full inverse factor, returning the original two-factor divisor/logarithm sum. This is an exact identity, not a cancellation estimate.

The complete bounds obtained here are:

- Bounding all expanded terms with their actual divisor-size norms gives the complex bound \(T^{1/4+\epsilon}\), uniformly in the cutoffs.
- Recombining before applying the inherited complete classical envelope gives the real bound \(T^{1/6+\epsilon}\).
- Neither improves the inherited **complete real** bound \(T^{\beta+\epsilon}\), \(\beta=2\theta_{\rm LY}-1/2=0.1289663519\ldots\).

A legal bilinear estimate is better in certain unbalanced ranges. At \(N=T^{2/3}\), its optimally placed factor has exponent \(16/189\) and gives \(T^{47/378+\epsilon}\). Literal Vaughan cutoffs do not grant this factor range to all terms. Moreover, even the optimistic grant that every scale has its best factor split, combined with the classical envelope, has worst exponent \(81/614>\beta\). These are comparisons of upper-bound certificates, not lower bounds for the arithmetic wave or impossibility results for other signed estimates.

# 2. Exact statement and hypotheses

Use the fixed accepted radial mollifier and its real even Schwartz transform \(\Psi\), with \(\Psi(0)=1\), \(|\Psi|\le1\), and possible sign changes. Let \(T\ge2\) be real and \(cT\le R\le CT\), for fixed positive \(c,C\). Set
\[
 B_T(R)=4\sum_{n\ge1}f(n)n^{-3/4}\Psi(\sqrt{n/T})
             \cos(2\pi R\sqrt n-3\pi/4),\qquad f=1*\chi_4.
\]
For \(n\ge2\),
\[
 F(n)=\frac{n^{-3/4}\Psi(\sqrt{n/T})e(R\sqrt n)}{\log n},
 \qquad F(1)=0.
\]
The original singleton is
\[
 B_{\{1\}}=4\Psi(T^{-1/2})\cos(2\pi R-3\pi/4)=O(1).
\]
All convolutions below are Dirichlet convolutions. For \(\psi=1,\chi_4\), put
\[
 a_\psi=\psi,\quad g_\psi=\mu\psi,\quad
 b_\psi=\Lambda\psi,\quad c_\psi=\psi\log.
\]
The same family uses real \(U,V\ge1\), with literal restrictions \(d\le U\), \(r\le V\) and their strict complements. They may be chosen separately for a dyadic product scale \(N\), depending on \(T,N\), not on a favorable radius.

The exact complete target is
\[
 \left|4\Re\left(e(-3/8)
     \sum_{\psi=1,\chi_4}\langle
       f*b_{\psi,\le V}
       +f*g_{\psi,\le U}*c_\psi
       -f*g_{\psi,\le U}*a_\psi*b_{\psi,\le V}
       +f*g_{\psi,>U}*a_\psi*b_{\psi,>V},F\rangle\right)\right|
 \ll_\epsilon T^\epsilon.                                      \tag{1}
\]
Here \(\langle h,F\rangle=\sum_nh(n)F(n)\), with a product-block restriction when cutoffs vary by block. Adding the singleton restores \(B_T\). An intermediate improvement must bound this entire real expression with exponent strictly smaller than \(\beta\).

# 3. Proof, signed attempt, and complete cost ledger

**Arithmetic identities and valuations.** Complete multiplicativity, including the zeros of \(\chi_4\), gives
\[
 a_\psi*g_\psi=\delta_1,\qquad a_\psi*b_\psi=c_\psi,\qquad
 g_\psi*c_\psi=b_\psi.
\]
The product rule for logarithmic differentiation of a convolution, or its finite divisor proof, gives
\[
 f\log=f*((1+\chi_4)\Lambda)=f*(b_1+b_{\chi_4}).             \tag{2}
\]
No prime power is replaced by a prime. The logarithmic coefficient is
\[
 b(2^j)=\log2,\quad b(p^j)=2\log p\ (p\equiv1\bmod4),\quad
 b(p^j)=(1+(-1)^j)\log p\ (p\equiv3\bmod4).
\]
For example, on split \(p^k\), (2) is
\(k(k+1)\log p=2\sum_{j=1}^k(k-j+1)\log p\).
On inert odd powers both sides vanish; on inert even powers the even \(j\)'s contribute \(k\log p\). At \(2^k\), \(k\) identical contributions give \(k\log2\). These checks include repeated powers and the ramified prime.

Write \(g=g_{\le U}+g_{>U}\) in \(g*c\), then \(c=a*b\) in its second part and split \(b\) at \(V\). Since \(g_{>U}*a=\delta_1-g_{\le U}*a\),
\[
 b_\psi=b_{\psi,\le V}+g_{\psi,\le U}*c_\psi
 -g_{\psi,\le U}*a_\psi*b_{\psi,\le V}
 +g_{\psi,>U}*a_\psi*b_{\psi,>V}.                          \tag{3}
\]
Thus the four contractions in (1) are respectively the literal sums
\[
\begin{split}
 &\sum_{kr=n,\ r\le V}f(k)b_\psi(r),\\
 &\sum_{kdl=n,\ d\le U}f(k)g_\psi(d)c_\psi(l),\\
 &-\sum_{kdlr=n,\ d\le U,\ r\le V}
                         f(k)g_\psi(d)a_\psi(l)b_\psi(r),\\
 &\sum_{kdlr=n,\ d>U,\ r>V}
                         f(k)g_\psi(d)a_\psi(l)b_\psi(r).
\end{split}                                                   \tag{4}
\]
In particular, the long term has \(d>U,r>V\), not merely \(dr>UV\); no coprimality or disjoint-prime condition is present.

**Complete signed contraction before norms.** Define
\[
 \alpha_{\psi,\le U}=f*g_{\psi,\le U},\quad
 \alpha_{\psi,>U}=f*g_{\psi,>U},\quad
 \beta_{\psi,\le V}=a_\psi*b_{\psi,\le V},\quad
 \beta_{\psi,>V}=a_\psi*b_{\psi,>V}.
\]
Let
\[
 \ell_V(n)=\sum_{\substack{r\mid n\\r\le V}}\Lambda(r).
\]
Then, exactly,
\[
 \beta_{\psi,\le V}(n)=\psi(n)\ell_V(n),\quad
 \beta_{\psi,>V}(n)=\psi(n)(\log n-\ell_V(n)),\quad
 0\le\ell_V(n)\le\log n.                                  \tag{5}
\]
The latter vector vanishes for \(n\le V\). Most significantly,
\[
 d_1:=f*g_1=\chi_4,\qquad d_{\chi_4}:=f*g_{\chi_4}=1,       \tag{6}
\]
including even integers. For \(n\le U\), \(\alpha_{\psi,\le U}(n)=d_\psi(n)\); the complementary vector is zero there, and everywhere
\(\alpha_{\psi,>U}=d_\psi-\alpha_{\psi,\le U}\).

Keeping the minus sign in (4), its middle pair is
\(\alpha_{\psi,\le U}*\beta_{\psi,>V}\). Adding the long term gives
\(d_\psi*\beta_{\psi,>V}\). Also \(f=d_\psi*a_\psi\), so the first term is \(d_\psi*\beta_{\psi,\le V}\). The whole branch is therefore
\[
 d_\psi*c_\psi,\qquad
 \sum_\psi d_\psi*c_\psi=\chi_4*\log+1*(\chi_4\log)=f\log. \tag{7}
\]
This is the strongest exact signed cancellation used here. It prevents charging a truncated inverse as if it were the full bounded vector (6), but supplies no new estimate for the phase \(R\sqrt{ml}\).

The real pairing is taken only after the sum of all terms. Equivalently its two signs are
\(2e(-3/8)S+2e(3/8)\overline S\). Neither a nonconjugated channel nor a cosine sign is discarded. The phase factor never becomes a linear phase in a factor variable.

**Actual norms, including the short term.** On a dyadic interval of length comparable to \(M\),
\[
 |f(m)|\le\tau_2(m),\qquad
 |\alpha_{\psi,\le U}(m)|,\ |\alpha_{\psi,>U}(m)|
       \le\tau_3(m),
\]
uniformly in \(U\). For \(\psi=1,\chi_4\), both \(c_\psi,\beta_{\psi,\le V},\beta_{\psi,>V}\) have modulus at most \(\log m\); \(b_{\psi,\le V}\) also has modulus at most \(\log m\). Consequently each left and right vector in the four bilinear groupings
\[
 (f,b_{\psi,\le V}),\quad
 (\alpha_{\psi,\le U},c_\psi),\quad
 (\alpha_{\psi,\le U},\beta_{\psi,\le V}),\quad
 (\alpha_{\psi,>U},\beta_{\psi,>V})
\]
satisfies
\[
 \|v\|_1\ll_\epsilon M^{1+\epsilon},\qquad
 \|v\|_2\ll_\epsilon M^{1/2+\epsilon}.                    \tag{8}
\]
For the logarithmic vectors the explicit versions are \(M\log(2M)\) and \(\sqrt M\log(2M)\). These estimates follow from fixed divisor bounds; they require no prime-number theorem, Möbius cancellation, or source for multiplicative exponential sums. In particular, \(d\le U\) does not make \(\alpha_{\psi,\le U}\) supported on \(m\le U\): the unrestricted \(f\)-factor survives.

For \(n\asymp N\), put \(\mathcal F=R\sqrt N\) and
\(A_J(N)=(1+N/T)^{-J}\). The smooth multiplier in \(F\), without its oscillation, and its scaled first derivative have size
\[
 \ll_J N^{-3/4}(\log(2N))^{-1}A_J(N).
\]
Schwartz seminorms with larger fixed orders absorb derivatives of \(\Psi(\sqrt{n/T})\). This argument does not assume \(\Psi\ge0\). Absolute summation of each of (4), or (8) with all product multiplicities, gives
\[
 \ll_{\epsilon,J} A_J(N)N^{1/4+\epsilon}.                 \tag{9}
\]
The number of factor blocks is only a fixed power of \(\log(2N)\). This pays every short/long transition, rather than naming a Type-I or Type-II term without estimating it.

**Legal nonlinear row and bilinear estimates.** For the plain \(c_1(l)=\log l\) factor, the accepted unweighted exponent-pair bound, followed by Abel summation, gives the Type-I certificate
\[
 \ll T^\epsilon A_J(N)N^{1/4}
           \min\{1,\mathcal F^{13/84}L^{-1/2}\},\quad ML\asymp N.
                                                               \tag{10}
\]
This is not asserted for an arbitrary weighted or character row. A plain factor can also be exposed by opening \(f=1*\chi_4\) in the short term; its other factors and norms must then be summed.

For all four actual bilinear groupings, a bound valid without deleting either character is
\[
 \boxed{\ |S_{N;M,L}|\ll_{\epsilon,J}T^\epsilon A_J(N)N^{1/4}
 \min\{1,\ L^{-1/2}+\mathcal F^{13/168}M^{-1/4}\}\ .\ }    \tag{11}
\]
Choose the orientation with \(M\ge L\) if desired. The coefficient bounds (8), rather than a source for weighted rows, justify this estimate.

Here is the full kernel calculation. Temporarily normalize away the smooth amplitude. Cauchy in \(m\) leaves, for \(l\ne l'\), an unweighted \(m\)-sum with phase
\(R(\sqrt l-\sqrt{l'})\sqrt m\). The literal restrictions \(N<ml\le2N\) and \(N<ml'\le2N\) intersect in one interval inside the ambient \(m\)-block. Abel summation of the product of the two smooth amplitudes has bounded normalized variation on that interval. If \(h=|l-l'|\),
\[
 |u|\asymp Rh/\sqrt L,\qquad
 |K_M(u)|\ll T^\epsilon |u|^{13/84}M^{97/168}
 \ll T^\epsilon\mathcal F^{13/84}(h/L)^{13/84}\sqrt M.
\]
For \(N\le Z=T^{3/2}\),
\[
 |u|/\sqrt M\gg Rh/\sqrt N\gg T^{1/4},
\]
so the accepted large-parameter, proper-interval monomial interface applies for sufficiently large \(T\). Its parameter is polynomially bounded by \(T\), so the source epsilon losses remain \(T^\epsilon\). The bounded remaining \(T\)-range is absorbed into constants. No arithmetic weight is inserted into this kernel.

The diagonal contributes \(M\|\beta\|_2^2\). For every displacement,
\(\sum_l|\beta(l)\beta(l+h)|\le\|\beta\|_2^2\); summing \(h\) costs \(L\). Thus
\[
 |S_{\rm unweighted\ amplitude}|^2
 \ll T^\epsilon\|\alpha\|_2^2\|\beta\|_2^2
          \{M+\mathcal F^{13/84}\sqrt M\,L\}
 \ll T^\epsilon\{M^2L+\mathcal F^{13/84}M^{3/2}L^2\}.
\]
Restoring \(N^{-3/4}/\log(2N)\), its variation, and the actual vector logarithms proves (11). All product masks and the entire Gram diagonal have been paid. Passing to this bound loses the prescribed Möbius/character cross-correlations; nothing says those correlations are intrinsically large.

**Cutoff and all-scale optimization.** At \(N=T^\nu\), write the shorter factor \(L=T^k\), \(0\le k\le\nu/2\). Ignoring logarithms, the two terms of (11) have exponents
\[
 E_1=\nu/4-k/2,\qquad E_2=13/168+13\nu/336+k/4.            \tag{12}
\]
Their intersection is
\[
 k_*=(71\nu-26)/252,\qquad
 \gamma_*=(55\nu+26)/504.                                \tag{13}
\]
For \(\nu<26/71\), the constrained/trivial envelope is instead \(\nu/4\). At \(\nu=2/3\), (13) is \(k_*=16/189\), \(\gamma_*=47/378<\beta\). But balanced \(M=L=\sqrt N\) at this scale gives
\(\mathcal F^{13/168}M^{-1/4}\asymp N^{5/168}>1\);
(11) is then capped by (9). The plain-row bound (10) also gives no saving for the balanced range.

No literal \(U,V\) has been shown to place all nonzero factors near \(k_*\). For every \(V\ge2\), the first branch contains the actual \(r=2\) summand
\[
 (\log2)\sum_k f(k)F(2k).
\]
Opening \(f\) retains balanced \(a,b\asymp\sqrt N\), \(k=ab\), with the actual \(\chi_4(b)\) and phase \(R\sqrt{2ab}\). The divisor-logarithm denominator saves at most a logarithm in this certificate. There is no \(U\)-cutoff in this short term. When \(1\le V<2\), every \(b_{\psi,\le V}\) is zero and \(\beta_{\psi,>V}=c_\psi\); the entire pair of inverse cutoffs contracts to (7), again retaining the balanced divisor sum. These statements identify the failure of termwise factor certificates, not a lower bound for an isolated signed summand or for the full sum. Cancellation across the displayed terms remains possible and unproved.

The complete absolute certificate (9) is independent of \(U,V\), so optimizing it changes no power. Recontracting (7) before estimation permits the inherited real classical envelope
\[
 T^\epsilon\min\{N^{1/4},T^{1/2}N^{-1/2}\},               \tag{14}
\]
with the Schwartz multiplier retained. Its complete maximum is \(T^{1/6+\epsilon}\).

There is a second, stronger diagnostic even before enforcing the actual factor restrictions. Suppose optimistically that every block could use its best split (13). Combining that hypothetical certificate with (14) gives its largest exponent at
\[
 (55\nu+26)/504=(1-\nu)/2,\qquad
 \nu=226/307,\qquad \gamma=81/614>\beta.                  \tag{15}
\]
The small-scale branch \(\nu/4\) and the decreasing large-scale branch do not exceed this maximum. Thus even that optimistic two-envelope menu does not improve the complete benchmark. Equation (15) is not an established improved estimate for the actual decomposition, since the grant of all optimal splits is unsupported; it is an upper-certificate comparison. Nor does it rule out a stronger signed estimate.

**Complete infinite sum and physical restoration.** Take \(Z=T^{3/2}\). Each expanded coefficient in (4) is bounded uniformly in \(U,V\) by \(n^\eta\log(2n)\) times an \(\eta\)-dependent constant. For any required fixed \(A\), Schwartz decay of fixed order \(D\) gives
\[
 \sum_{n>Z}n^{-3/4+\eta}|\Psi(\sqrt{n/T})|
 \ll_D T^{D/2}Z^{1/4+\eta-D/2}
 =T^{3/8+3\eta/2-D/4}\ll_A T^{-A}.                       \tag{16}
\]
This pays the expanded tail as well as the recombined one. Between \(2\) and \(Z\), include every dyadic block and partial last block. Summing (9) with \(A_J(N)\) yields the complete complex \(T^{1/4+\epsilon}\); summing the re-contracted real (14) yields \(T^{1/6+\epsilon}\). No mixed scale or sign is replaced by a favorable block. The singleton was paid before division by \(\log n\).

The accepted sharp identity, including real-radius jumps, is
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+O_\epsilon(T^{1/2+\epsilon}).
\]
A complete real exponent \(\gamma\ge0\) would therefore give
\(P(X)\ll X^{1/4+\gamma/2+\epsilon}\). The two obtained prices restore to \(3/8\) and \(1/3\), while the retained \(\beta\) restores to \(\theta_{\rm LY}\). Even the hypothetical (15) restores only to \(97/307>\theta_{\rm LY}\). No complete improvement follows.

# 4. First doubtful or unproved step

The first missing estimate is a stronger bound for the **entire real expression (1)**, after the exact cancellations (5)–(7), with all actual vectors and every product scale. Equations (10)–(11) do not supply such a bound below \(\beta\).

A false shortcut would treat \(\alpha_{\psi,\le U}\) as a short bounded vector because \(g_{\psi,\le U}\) is short; the unrestricted \(f\)-factor makes this incorrect. Another unsupported step would apply the favorable \(k_*\) range to the short term, the other character branch, or all intermediate scales. Finally, a bound for the complete real wave cannot be inserted as a bound for a complex component or for an arbitrary truncated factor sum.

There is no actual arithmetic counterexample and no general theorem excluding logarithmic convolution. The exact inverse cancellation and the priced certificates explain why this bounded attempt gives no new complete inequality.

# 5. Controls and outcomes

| Required control | Outcome |
|---|---|
| Logarithmic identity; both branches | Equations (2), (5)–(7) include the zero values of \(\chi_4\) and the full signed contraction. |
| Literal Vaughan cutoffs | Equation (4) retains separate \(d\le U\), \(r\le V\), all complements and product masks, for real cutoffs. |
| Prime powers and \(2\) | All valuations explicitly checked; no prime-only substitution or PNT used. |
| Singleton/log division | \(n=1\) is paid as an original cosine; \(F(1)=0\). |
| Actual norms; every Type-I/II range | Equations (8)–(11) cover all four terms. A short inverse factor is not a short convolution with \(f\). |
| Real radii; masks; phase | Every estimate is uniform for real \(R\in[cT,CT]\). The product phase and common intervals remain literal. |
| Cosine/complex scope | Two signs restored by the single real pairing. The inherited exponent is used only for complete real \(B_T\). |
| Infinite tail and mixed scales | Equation (16), every block through \(Z\), smooth transition, and fixed seminorms are included. |
| Full quantitative comparison | Local \(47/378\) is not a complete gain. Even optimistic all-scale optimization gives \(81/614>\beta\). |
| Actual versus generic | Kernel Cauchy explicitly loses the arithmetic correlations. Its unfavorable certificate is not a signed lower bound. |
| Source scope | Only the already accepted monomial proper-interval interface is used, on unweighted sums. No new source audit. |
| Physical restoration/full goal | All costs restored. M1, M2, GAR, endpoints and the whole-moment alternatives remain open. |

The accepted complete distribution remains
\(D(V)\ll T^\epsilon(V^{-2}+TV^{-136/13})\).
For \(p>136/13\), both ceiling contributions
\(W^{p-2}\) and \(TW^{p-136/13}\), \(W\ll T^{\beta+\epsilon}\), remain; the accepted complete bound is
\[
 M_p(B_T)\ll_{p,\epsilon}T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}.
\]
The complete distinct-class twelfth target remains unproved and, even if proved, is only the \(102/325\) milestone. The separate unbounded-fixed-order quarter route is not discharged. Zero mathematical experiments were performed.

# 6. Dependencies, exact artifacts, and provenance

This is selected-context discovery, **not statement-only isolation**. The reused agent retains rounds217–224 history and authored the frozen round224 report complete_signed_prime_attack.md (SHA256 \(0d734e579ccee82e08f6af9183a3246683b317eb395eafca2bead509be8251cd\)). That earlier GAR coefficient is different from the actual \(f\) here; it is not silently replaced by \(f\). I also authored the listed round223 multiplicative-source report; citing it is not independent validation of my own claims.

No current sibling report, blind packet, review, or unlisted control was read. The finite identities and kernel calculation above were derived for this report. The conductor independently checked the critical exponent, corrected an initially misstated general optimization formula in correspondence, and supplied the all-scale comparison idea; (12)–(15) were then rederived algebraically. Their provenance is collaborative, not claimed independent of that intervention. No external browsing or new theorem import was used; the round's optional primary audit was not consumed.

Exact SHA256 values at reading/hash time:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 96ee2e0899a9b7e9d75aa276b7c098f0fbf1748850e94b5c6941733f856344fe |
| strategy/round225_complete_circle_logarithmic_convolution.md | 64be6a3fb32b2f33deea69cef87b846ec06732e002ffd2f5156f21f7ea8c878b |
| current briefs/conductor_complete_circle_wave.md | 6adcf15bf5850f080aefd63c00d83d3482f6c244f5244c340b4206c47c46e0ef |
| current briefs/complete_nonlinear_prime_attack.md | 1b1fa73937f6cec066814841a1b3fac707986329ade1a1075bf41cdb53c8bea1 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |
| rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md | 6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| rounds/codex-managed/gc-full-goal-signed-source-review/reports/multiplicative_wave_sources.md | db7d52b2ebd266a9e92ae347444f6b1c0dbd99258194df07404b39c16b21ed86 |
| rounds/codex-managed/gc-actual-radical-high-values/synthesis.md | 72ca1bcc9cad3657b7ad123533342fa1458beb6dc19ff518472fd681b8a61212 |

The graph supplies the qualified Li–Yang benchmark with all five application repairs. Accepted204 supplies the actual smoothing, sharp bridge, tail method and legal square-root exponent-pair specialization; closed203 supplies only its recorded complete classical envelope. Historical source failures223 and the distinct-class reduction216 retain their stated scope. No archived assertion is upgraded by this report.

# 7. Recommended state effect

**No change** to the graph, accepted exponents, moment bounds, M1/M2/GAR, endpoints, or quarter status. Retain the exact finite identities and this complete cost audit as scoped candidate evidence. Reject the unsupported transfers from a favorable factor interval to all terms, or from a local improvement to the complete wave.

The one complete missing inequality is (1) at \(T^{\gamma+\epsilon}\) for some \(\gamma<\beta\), ultimately \(T^\epsilon\), with exactly the stated terms and complements. This report neither starts another method nor assigns a successor. Stop after freezing this report.


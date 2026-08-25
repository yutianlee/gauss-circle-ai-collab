# Round 146 terminal mathematical seam verdict

- Campaign: `m9-m1-lower-cone-three-variable-hessian-dispersion-gate`
- Candidate: `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`
- Reviewer role: independent terminal mathematical seam review
- Starting graph SHA-256: `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`

## 1. Result

\[
\boxed{\mathsf{GREEN}}
\]

No mathematical correction remains in the candidate's promoted kernel. The
two-owner unmasking, both coefficient parametrizations, capacity and Hessian
algebra, short-face ledger, \(t\)-difference split, phase-level Legendre
return, dual-alias upper ledger, source-power calculations, first-open
estimate, and downstream no-claim scope all check independently.

The correct terminal label is

\[
\boxed{\mathsf{three\_variable\_dispersion\_no\_go}}.
\]

This is only a no-go for the explicitly listed Hessian-only,
coefficient-blind, audited direct-source, one-difference-without-correlation,
and transform-followed-by-modulus mechanisms. It is not a lower bound for the
signed scalar and not an impossibility theorem for a future sign-sensitive
estimate.

## 2. Exact owner and coefficient seams

Put \(T_M=\lceil M^{1/4}\rceil\) and \(J_M=M^{3/4}\). For integral
\(t\), the ambient squarefree-kernel support is exactly

\[
 \{t<T_M,\ |j|>J_M\}\ \dot\cup\
 \{t<T_M,\ |j|\leq J_M\}\ \dot\cup\
 \{t\geq T_M\}.
\]

The first set is \(\mathfrak S_N^{<,>}\). The second is a restriction
of the accepted Round-144 absolute cell owner, including its separately
accepted exact-radical channel. The third is the accepted Round-145
*unmasked* large-\(t\) owner. Hence

\[
 \mathfrak S_N^{<,>}=\mathfrak U_N^{<}
   +O_{\varepsilon,V}(X^\varepsilon),
 \qquad
 \mathfrak T_N=\mathfrak S_N^{<,>}
   +O_{\varepsilon,V}(X^\varepsilon).
\]

The two errors lie on disjoint pieces of this exact partition. The strict
\(>\), complementary \(\leq\), ceiling, half-open blocks, terminal
truncation, and exact radicals leave no gap or double charge. The per-block
large-\(t\) price is

\[
 M^{-3/4}X^\varepsilon
 \sum_{t\geq T_M}\frac{M}{t^2}\ll X^\varepsilon,
\]

and the logarithmic block assembly is absorbable by epsilon renaming.

For fixed ordered \(d,e\), the candidate's coefficient is exactly

\[
\begin{aligned}
\kappa_t(d,e)={}&\mathbf1_{\{\mu^2(de)=1\}}
 \mathbf1_{\{e\ {\rm odd}\}}\chi_4(e)
 \sum_{\substack{\gamma\mid t\;\gamma\ {\rm squarefree,odd}\\
                   (\gamma,de)=1}}\chi_4(\gamma)
 \sum_{\substack{ab=t/\gamma\;b\ {\rm odd}\\
                   eb^2>4da^2}}1.
\end{aligned}
\]

The inverse map

\[
 h=\gamma da^2,\qquad r=\gamma eb^2,\qquad
 s=de,\qquad t=\gamma ab
\]

is multiplicity one. Here \(\gamma,d,e\) are pairwise coprime and
squarefree, \(\gamma,e,b\) are odd, no coprimality involving \(a,b\)
may be added, and the character and cone are exactly

\[
 \chi_4(r)=\chi_4(\gamma)\chi_4(e),\qquad
 r>4h\iff eb^2>4da^2.
\]

The full-gcd formula with \(G=(h,r)\), \(Gab=t\),
\((da,eb)=1\), and \(Geb\) odd is equivalent and correctly imposes no
extra coprimality on \(G\). Finally,

\[
 |\kappa_t(d,e)|\leq\sum_{\gamma ab=t}1
 =\tau_3(t)\ll_\varepsilon t^\varepsilon.
\]

Thus (146.C9)--(146.C14) are exact inherited coefficient algebra, while
(146.C2)--(146.C8) are the genuinely new unmasking fact.

## 3. Hessian, capacity, aspects, and short faces

For \(f(t,d,e)=\sqrt N\,t\sqrt{de}\), direct differentiation gives

\[
 f^{-1}\operatorname{diag}(t,d,e)\nabla^2f\operatorname{diag}(t,d,e)
 =\begin{pmatrix}
 0&1/2&1/2\\
 1/2&-1/4&1/4\\
 1/2&1/4&-1/4
 \end{pmatrix}.
\]

Its eigenvalues are \(-1/2,1/\sqrt2,-1/\sqrt2\), its determinant is
\(1/4\), and

\[
 \det\nabla^2f=\frac{f^3}{4t^2d^2e^2}.
\]

On a nonempty \(T,D,E\) box, \(T^2DE\asymp M\), so the literal
coefficient envelope gives

\[
 |\mathfrak U_{M,T,D,E}|
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.
\]

Consequently every fixed \(T=M^\theta\), \(\theta<1/4\), still
requires a signed saving \(M^{1/4-\theta}\); only an
epsilon-equivalent terminal shell is already safe.

If a factor tuple contributes, then

\[
 \frac ab=\frac{\gamma a^2}{t}\geq\frac1t,
 \qquad
 \frac ed>\frac4{t^2},
 \qquad d^2<\frac m4,
 \qquad e^2>\frac{4m}{t^4}.
\]

This proves \(D\ll\sqrt M\) and \(E\gg\sqrt M/T^2\). The resulting
face ledger is exact:

- \(t=1\) is mandatory, has the displayed \(\kappa_1(d,e)\), and
  leaves the singular rank-one \(d,e\) Hessian with owner-sized
  capacity.
- \(D=1\) is structurally present; the \(t=d=1,e=p>4\) prime corner
  has \(C(p)=\chi_4(p)\ne0\). The candidate correctly does not claim
  that every clipped \(D=1\) box has nonzero net coefficient.
- \(E=1\) is empty, while fixed bounded \(E\) forces a terminal
  target-safe \(T\)-shell. A growing short-\(E\) range is not thereby
  discharged.
- The upper product level \(t^2de=B_M\) is excluded from the current
  half-open block; one actual product layer is safe, whereas a wide
  radial collar is not free.
- Cone equality is empty by parity. A fixed lattice-width cone collar
  costs at most \(M^{-3/4}TDX^\varepsilon\ll X^\varepsilon\); a
  relative-width collar is not automatically safe.

Equation (146.C33) is valid as the prefix-uniform interface for a route
that owns the \(t=1\) layer separately and then restores \(s^{-3/4}\)
by partial summation. It is not used to exclude a genuinely joint theorem;
the candidate explicitly preserves possible cancellation between
different \(t\)-layers.

## 4. Difference and stationary-transform seams

With zero extension in \(t\), the exact identity is

\[
 \left|\sum_tA_{t,d,e}e(\sqrt N\,t\sqrt{de})\right|^2
 =\sum_{h\in\mathbb Z}e(\sqrt N\,h\sqrt{de})
   \sum_tA_{t+h,d,e}\overline{A_{t,d,e}}.
\]

The \(h=0\) contribution is the constant-phase diagonal. Every
\(h\ne0\) contribution has the singular rank-one \(d,e\) phase and
retains two exact factor counts, two cones, and their correlated
squarefree, coprimality, profile, and endpoint conditions. No accepted
correlation estimate saves a power, so one coefficient-robust difference
does not close the problem.

For the ideal bare phase \(c\,t\sqrt{de}\), the critical point of
\(c\,t\sqrt{de}-ut-vd-we\) is

\[
 t_*=\frac{2\sqrt{vw}}c,\qquad
 d_*=\frac uc\sqrt{\frac wv},\qquad
 e_*=\frac uc\sqrt{\frac vw},
\]

and the critical value is \(-2u\sqrt{vw}/c\). Thus
\(c\mapsto-2/c\mapsto c\) is correct only at the phase-monomial level
after the second alias-orthant reversal; it is not an amplitude-level
two-step identity.

Writing \(F=\sqrt{NM}\) and \(V_3=TDE\), the dual side lengths are
\(F/T,F/D,F/E\), all long on the retained support. The elementary
supported bounding-box count is

\[
 \#\{\text{aliases}\}\ll
 (1+F/T)(1+F/D)(1+F/E)\ll\frac{F^3}{V_3}.
\]

One stationary integral has modulus \(\asymp V_3/F^{3/2}\), so the
available aliaswise triangle upper ledger is \(F^{3/2}\), or
\(N^{3/4}\) after the physical weight. This is explicitly only an
adverse upper ledger, not a lower bound and not a substitute for a signed
dual-alias theorem.

## 5. Source-power algebra and first doubtful step

The candidate now includes every exact source-card mapping previously
requested. For Cao--Zhai Theorem 6 the unique placement up to swapping
\(d,e\) is

\[
 (m,m_1,m_2)=(d,t,e),\qquad
 (\alpha,\beta,\gamma)=(1/2,1,1/2),
\]

with \((M_0,M_1,M_2)=(D,T,E)\), \(A=\sqrt N\), and
\(F\asymp\sqrt{NM}\gg D\). Its literal separated coefficient
hypothesis fails. Even granting an \(R^\varepsilon\)-norm separation,
the fourteen normalized balanced exponents recompute to

\[
\begin{aligned}
 &\frac38-\frac{5\tau}8,\quad
 \frac38-\tau,\quad
 \frac{11}{29}-\frac{43\tau}{58},\quad
 \frac{41}{108}-\frac{41\tau}{54},\\
 &\frac{37}{98}-\frac{37\tau}{49},\quad
 \frac{11}{29}-\frac{23\tau}{29},\quad
 \frac{127}{336}-\frac{125\tau}{168},\quad
 \frac{115}{304}-\frac{115\tau}{152},\\
 &\frac{127}{336}-\frac{131\tau}{168},\quad
 \frac{33}{100}-\frac{181\tau}{200},\quad
 \frac{123}{368}-\frac{167\tau}{184},\\
 &\frac{33}{100}-\frac{19\tau}{20},\quad
 \frac13-\frac{5\tau}{6},\quad
 \frac14-\frac{9\tau}{8}.
\end{aligned}
\]

At the formal endpoint \(\tau=1/2\), terms \(1,3,7\) remain positive,
with exponents \(1/16,1/116,1/168\). Term 1 becomes target-sized only
for \(\tau\geq3/5\), outside the strict small-\(t\) range. This is a
limitation of that displayed upper bound, not a lower bound.

The independent comparison powers also check:

\[
 \text{Robert--Sargos: }R^{1/2-\tau/2},\qquad
 \text{Sargos--Wu: }R^{2/5-3\tau/10},
\]

both leaving \(R^{1/4}\) at the formal endpoint. Cao--Zhai Theorem 7
has the stronger coefficient mismatch and its second well-defined term
leaves \(R^{7/8}\). The candidate now records the exact
Robert--Sargos and Sargos--Wu variable/scale mappings and the
multidimensional-transform scale and domain hypotheses, so the prior
source-card omissions are closed.

The first genuinely unproved step is therefore a sign-sensitive estimate
or bounded-projective-norm decomposition for the literal coefficient,
uniform over all clipped boxes and short faces. The candidate does not
claim such a result.

## 6. First-open estimate and downstream scope

The exact first open estimate is

\[
 \boxed{\mathfrak U_N^{<}\ll_{\varepsilon,V}X^\varepsilon},
\]

with \(\mathfrak U_N^{<}\) given equivalently by (146.C3) or the
multiplicity-one expansion (146.C9)--(146.C10). The nearest-square mask
has been removed, and only that mask has been removed. Squarefree and
coprimality support, factor multiplicity, parity, character, strict cone,
product profile, half-open endpoints, individual positive direction, and
fixed centre remain literal.

The independent Round-138 collar-tail cross owner remains unchanged. The
candidate proves neither the complete lower-radial estimate, lower GAR,
either direct M1 parent, M9-M1, any M2 owner, M9-M2, endpoint uniformity,
M9, the bridge, nor the quarter theorem. It makes no global-exponent
improvement.

## 7. Controls, dependencies, and recommended state effect

This review read `protocol.md`, the final conductor candidate, all three
Round-146 reports, the blind/discovery cross-reviews, both final candidate
audits, and the conductor controls. It also checked the accepted Round-144
cell and Round-145 squarefree-tail owner statements in
`state/proof_obligations.yml`. All assigned mathematical and source-power
artifacts pass the forbidden-control-byte scan.

Recommended state effect:

1. promote the exact unmasking reduction (146.C2)--(146.C8), depending
   on the inherited coefficient interface (146.C9)--(146.C14);
2. promote only the scoped three-variable dispersion obstruction;
3. retain \(\mathfrak U_N^{<}\) as open;
4. reject determinant-only cancellation, arbitrary-coefficient or smooth
   tensor substitution, short-face disposal, direct use of the audited
   monomial bounds, and transform-followed-by-modulus as completed target
   proofs;
5. make no downstream theorem or exponent change.

Terminal verdict: **GREEN; no further candidate correction is required.**

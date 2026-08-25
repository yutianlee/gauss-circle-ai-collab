# Round 156 terminal independent source and legal-method review

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Task: terminal source/legal-method review
- Role: independent source reviewer
- Literature checked through: 25 August 2026
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Status: review evidence only; no shared proof state was edited

## 1. Result

### GREEN: the full zero-row target is elementary once the literal BV lemma is proved

The new claimant evidence proves, throughout

\[
 M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM},
\]

the complete literal zero-row estimate

\[
 \boxed{\mathcal Z_U(V)\ll_{\varepsilon,A}
 M^{-1/4}X^\varepsilon\ll_{\varepsilon,A}X^\varepsilon.}
\tag{156.IS1}
\]

There are two valid closures.

1. The blind fixed-\(d\) closure is entirely elementary after the inherited
   profile hypotheses. Opening the definition of \(K(0,-j;c)\), bounding
   each nonzero additive frequency by a finite geometric series, and summing
   the harmonic majorant gives
   \[
    \sup_I\left|\sum_{j\in I}K(0,-j;c)\right|
    \ll c\log(2c).
   \tag{156.IS2}
   \]
   Discrete Abel summation against the proved literal
   \(j\)-bounded-variation norm, followed by the exact \(d\)-normalization,
   gives (156.IS1). It uses no primitive Gauss phase, induced-character
   formula, Pólya--Vinogradov theorem, Burgess theorem, or conductor-lowering
   theorem.

2. The local report's fully recombined closure is also a finite,
   source-independent argument. Its exact recombination
   \[
    \mathcal Z_U(V)=\frac1{4N}
      \sum_{V<|j|\le2V}\widehat B_j(0)\mathscr S_N(j)
   \tag{156.IS3}
   \]
   and finite Fourier transform give
   \[
    \sup_{|I|\le4N}
    \left|\sum_{j\in I}\mathscr S_N(j)\right|
    \ll \sqrt N\,\tau(N)\log(2N).
   \tag{156.IS4}
   \]
   All steps are orthogonality, a finite quadratic Gauss identity, a
   geometric-series bound, and a divisor estimate. No analytic
   character-sum theorem enters.

The exact primitive phases, induced transforms, Ramanujan branch, and all
two-adic values printed in the claimant reports are correct. They are
corroborated by the standard sources listed in Section 6 and, in the
two-adic cases, by direct finite sums. Pólya--Vinogradov is legal in the
conductor candidate, but it is only an optional fallback.

The initial source audit's direct no-match was correctly limited to finding
an external theorem that accepts an otherwise uncontrolled coefficient.
The new reports prove that the actual coefficient is controlled: adjacent
variation contracts to every induced progression. Thus the earlier
strict-range/source-no-match conclusion is superseded for \(v=0\). Its
warning against importing arbitrary-weight or maximal-unweighted theorems
remains relevant only when attacking the nonzero matrix and other broader
routes; it is not an obstruction to the zero row.

## 2. Exact statement, hypotheses, and theorem-dependency audit

Put

\[
 q=4N,\qquad c=\frac{4N}{d}\quad(d\mid N,\ d\text{ odd}),\qquad
 A_j=\widehat B_j(0).
\tag{156.IS5}
\]

The frozen row is

\[
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,A_jK(0,-j;c).
\tag{156.IS6}
\]

The internal hypotheses used by both elementary closures are exactly:

- the real profile is zero-extended and
  \[
   \|w_U\|_\infty+\operatorname {Var}(w_U)
   \ll_\varepsilon M^{-3/4}X^\varepsilon;
  \tag{156.IS7}
  \]
- the physical \(x\)-support has \(O(KX^\varepsilon)\) integer
  representatives in one residue system, lies at \(x\asymp K\), and has no
  wrapping;
- the exact cell is \(-x\le j\le x-1\), the phase is
  \(e(\sqrt{x^2-j}-x)\), and the two integer blocks are
  \(V<j\le2V\) and \(-2V\le j<-V\);
- \(V\le K\), and the inherited range has \(K<4N=q\).

These yield the literal coefficient norm

\[
 \mathcal A_I:=\sup_{j\in I}|A_j|
 +\sum_{j,j+1\in I}|A_{j+1}-A_j|
 \ll_\varepsilon K M^{-3/4}X^\varepsilon
 =\sqrt N\,M^{-1/4}X^\varepsilon
\tag{156.IS8}
\]

on each signed block \(I\).

The dependency classification is:

| Step | External theorem needed? | Audit outcome |
|---|---|---|
| literal \(A_j\) BV | No literature theorem; inherited profile hypotheses plus elementary variation | Valid, including zero extension, cell, phase, signs, and endpoints |
| blind fixed-\(d\) interval bound (156.IS2) | No | Finite geometric series and a harmonic sum |
| full \(d\)-recombination | No analytic theorem | Finite Fourier inversion and the exact even quadratic Gauss identity |
| recombined interval bound (156.IS4) | No | Finite Fourier inversion, orthogonality, geometric series, and divisor grouping |
| primitive quadratic conductors and phases | Not needed for (156.IS1); standard-source corroboration available | Correct |
| induced-character formula | Not needed for the elementary closure; also directly derivable by inclusion-exclusion | Correct |
| exact \(p=2\) factors | Not needed for the elementary closure; direct finite evaluation | Correct |
| Pólya--Vinogradov | Optional fallback in the conductor route only | Hypotheses match |
| Burgess, maximal sums, analytic conductor lowering | No | Irrelevant to the proved zero-row route |

## 3. Proof and source verification

### 3.1 The new literal BV proof fills the old seam

For fixed physical \(x\), the map

\[
 j\longmapsto \frac{x^2-j}{N}
\]

is monotone on either signed block. Sampling a zero-extended BV function
along a monotone sequence cannot increase its total variation. This charges
every profile component and transition without assuming a bounded component
count.

The exact phase satisfies

\[
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x,\qquad
 \left|\frac{d}{dj}(\sqrt{x^2-j}-x)\right|
 =\frac1{2\sqrt{x^2-j}}\ll K^{-1}.
\tag{156.IS9}
\]

The cell gives \(x^2-j\ge x^2-x+1\asymp K^2\), including at the positive
endpoint; the negative block only enlarges the radicand. Hence the phase
variation is \(O(V/K)=O(1)\). The asymmetric cell has at most one jump on
each signed block, and Abel's endpoint term is charged by the supremum.
Summing the fixed-\(x\) bound over \(O(KX^\varepsilon)\) representatives
proves (156.IS8). This is internal algebra/analysis, not an appeal to an
external weighted-character theorem.

Moreover, if \(j_1<\cdots<j_R\) is any ordered subsequence of a block, then

\[
 \sum_{r<R}|A_{j_{r+1}}-A_{j_r}|
 \le \sum_{u\text{ between }j_1\text{ and }j_R}|A_{u+1}-A_u|.
\tag{156.IS10}
\]

The intervening adjacent intervals are disjoint. The two endpoint values
cost at most \(2\sup_I|A_j|\). Consequently the progression-variation norm
\(\mathcal A_\ell(I)\) from the initial source audit is
\(O(\mathcal A_I)\) for every \(\ell\). Thus the previously missing input
(156.SA23) is now proved, not supplied by a source.

### 3.2 Blind fixed-\(d\) closure: no character theorem occurs

For a fixed \(c\equiv0\pmod4\), write directly from the definition

\[
 K(0,-j;c)=\sum_{a\bmod c}^{*}\gamma_c(a)e_c(-aj),\qquad
 \gamma_c(a)=\epsilon_a\left(\frac ca\right),\qquad
 |\gamma_c(a)|=1.
\tag{156.IS11}
\]

For a consecutive integer interval \(I=[A,B]\cap\mathbb Z\), let
\(r(a)=\min(a,c-a)\) for the representative \(1\le a<c\). The exact
finite geometric series gives

\[
 \left|\sum_{j\in I}e_c(-aj)\right|
 \le \min\left\{|I|,\frac{2}{|1-e_c(-a)|}\right\}
 \ll \min\left\{|I|,\frac c{r(a)}\right\}.
\tag{156.IS12}
\]

There is no zero frequency because \(a\) is a unit and \(c>1\). Therefore

\[
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \le\sum_{a\bmod c}^{*}
 \left|\sum_{j\in I}e_c(-aj)\right|
 \ll c\sum_{r\le c/2}\frac1r
 \ll c\log(2c),
\]

which is (156.IS2) for intervals of any length. This proves the requested
source independence: it is a finite identity plus the triangle inequality.

Discrete Abel summation on the positive and negative blocks separately now
gives

\[
 \left|\sum_{V<|j|\le2V}A_jK(0,-j;c)\right|
 \ll_\varepsilon
 K M^{-3/4}cX^\varepsilon.
\tag{156.IS13}
\]

Restoring the literal normalization and every odd \(d\mid N\),

\[
\begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 N^{-2}K M^{-3/4}X^\varepsilon
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}d\,c^{3/2}\\
 &\ll_\varepsilon
 N^{-2}K M^{-3/4}N^{3/2}
 \sum_{d\mid N}d^{-1/2}X^\varepsilon\\
 &\ll_\varepsilon M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{156.IS14}
\]

Here \(c=4N/d\), so \(d c^{3/2}=8N^{3/2}d^{-1/2}\); logarithms and divisor
factors are absorbed into \(X^\varepsilon\). This route alone certifies the
full target.

### 3.3 Fully recombined finite-Fourier closure

Define

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N),\qquad
 \mathscr S_N(j)=\sum_{x\bmod4N}G_N(x^2-j).
\tag{156.IS15}
\]

The exact finite Fourier projector is

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ {\rm odd}}}
 \chi_4(h)e_{4N}(ht).
\tag{156.IS16}
\]

Indeed, writing \(h=r+4k\) first forces \(N\mid t\); the remaining two-term
sum modulo four is \(2i\chi_4(t/N)\). Partitioning odd \(h\) by
\(d=(h,N)\), writing \(h=da\), and observing that \(x\bmod4N\) gives \(d\)
copies of \(x\bmod c=4N/d\), yields the local report's exact identity

\[
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).
\tag{156.IS17}
\]

The finite quadratic identity used here is

\[
 \sum_{x\bmod c}e_c(ax^2)
 =(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c,
 \qquad 4\mid c,\quad(a,c)=1.
\tag{156.IS18}
\]

This is an elementary complete Gauss evaluation, not an asymptotic theorem.
It follows by CRT from the odd-prime and \(2\)-power base sums and the
recurrences \(G(a;p^e)=pG(a;p^{e-2})\), with the two \(2\)-power base cases
handled separately. Quadratic reciprocity combines the CRT phases into the
right side of (156.IS18). The same normalization appears in
Duke--Friedlander--Iwaniec, Section 6; that citation corroborates rather
than supplies an analytic input. Since
\(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), (156.IS17) and then (156.IS3)
follow with the stated signs and factors.

Now use

\[
 \widetilde{\mathscr S}_N(h)
 =\sum_{j\bmod q}\mathscr S_N(j)e_q(hj),\qquad q=4N.
\]

Changing variables \(t=x^2-j\) gives

\[
 \widetilde{\mathscr S}_N(h)=
 \left(\sum_{r\bmod4}\chi_4(r)e_4(-hr)\right)
 \left(\sum_{x\bmod q}e_q(hx^2)\right).
\tag{156.IS19}
\]

The first factor vanishes for even \(h\) and equals
\(-2i\chi_4(h)\) for odd \(h\); hence the zero coefficient vanishes. For
odd \(h\), put \(d=(h,N)\), \(c=q/d\), and \(a=h/d\). Then

\[
 |\widetilde{\mathscr S}_N(h)|=2\sqrt{2qd}.
\tag{156.IS20}
\]

Only the magnitude is needed. It has the especially short direct proof

\[
\begin{aligned}
 \left|\sum_{x\bmod c}e_c(ax^2)\right|^2
 &=\sum_{u\bmod c}e_c(au^2)
   \sum_{y\bmod c}e_c(2auy)\\
 &=c\{1+e_c(ac^2/4)\}=2c,
\end{aligned}
\tag{156.IS21}
\]

because \(c\mid2u\) forces \(u=0,c/2\), and \(4\mid c\). Thus the interval
estimate does not rely even on the phase in (156.IS18).

Fourier inversion, (156.IS20), and the same geometric-series bound give,
for \(|I|\le q\),

\[
\begin{aligned}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 &\ll \sqrt q\sum_{1\le h\le q/2}\frac{(h,N)^{1/2}}h\\
 &\le \sqrt q\sum_{g\mid N}g^{1/2}
       \sum_{k\le q/(2g)}\frac1{gk}\\
 &\ll \sqrt N\,\tau(N)\log(2N).
\end{aligned}
\tag{156.IS22}
\]

This proves (156.IS4) using only finite algebra. Since each signed block
has length \(O(V)\le K<q\), Abel summation with (156.IS8) and (156.IS3)
gives

\[
 |\mathcal Z_U(V)|
 \ll \frac1N
 (K M^{-3/4}X^\varepsilon)\sqrt N\,X^\varepsilon
 =M^{-1/4}X^\varepsilon.
\tag{156.IS23}
\]

### 3.4 Independent checks of the optional character apparatus

Let \(s=\operatorname{sf}(m)\), including \(2\) when its valuation in \(m\)
is odd. The claimant discriminants

\[
 \Delta_+=\begin{cases}s,&s\equiv1\pmod4,\\4s,&s\not\equiv1\pmod4,
 \end{cases}
 \qquad
 \Delta_-=\begin{cases}-s,&s\equiv3\pmod4,\\-4s,&s\not\equiv3\pmod4
 \end{cases}
\tag{156.IS24}
\]

are exactly the fundamental discriminants of \(s\) and \(-s\). Their
Kronecker characters have conductors \(f_\pm=|\Delta_\pm|\mid4m\), and
the only principal case is \(\Delta_+=1\). Montgomery--Vaughan,
Theorems 9.13 and 9.17, confirm both the classification and

\[
 \tau(\chi_\Delta)=
 \begin{cases}\sqrt\Delta,&\Delta>0,\\i\sqrt{|\Delta|},&\Delta<0.
 \end{cases}
\tag{156.IS25}
\]

In particular

\[
 \tau((\cdot/p))=\begin{cases}\sqrt p,&p\equiv1\pmod4,\\
 i\sqrt p,&p\equiv3\pmod4,
 \end{cases}
 \quad
 \tau(\chi_4)=2i,\quad
 \tau(\chi_8)=\sqrt8,\quad
 \tau(\chi_{-8})=i\sqrt8.
\tag{156.IS26}
\]

The last three values also follow immediately by summing over the two or
four odd residue classes, so there is no phase ambiguity.

For primitive \(\chi\bmod f\), \(c=fL\), the claimant formula

\[
 G_{c,\chi}(n)=\tau(\chi)
 \sum_{\substack{r\mid R_f\\L/r\mid n}}
 \mu(r)\chi(r)\frac Lr\,
 \overline\chi\!\left(\frac{n}{L/r}\right),\qquad
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p,
\tag{156.IS27}
\]

is exact. Inclusion-exclusion of the unit conditions at primes outside
\(f\) proves it directly. With \(\ell=L/r\), it is precisely
Kıral--Zhou Lemma 2.2 and is equivalent to their Lemma 2.3 and
Montgomery--Vaughan Theorem 9.12. For \(f=1\) it is the Ramanujan sum.

The printed local consequences are also exact. If \(p^e\Vert c\) and the
primitive local conductor is \(p^a\), \(a>0\), then

\[
 \sum_{u\bmod p^e}^{*}\xi(u)e_{p^e}(zu)=
 \begin{cases}
 p^{e-a}\overline\xi(z/p^{e-a})\tau(\xi),
       &v_p(z)=e-a,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{156.IS28}
\]

For \(a=0\) this is \(c_{p^e}(z)\), with values \(0,-p^{e-1}\), and
\(p^{e-1}(p-1)\) on valuations \(\le e-2,e-1,\ge e\), respectively.
At \(2\), (156.IS28) with conductors \(4\) and \(8\), together with
(156.IS26), gives exactly the claimant factors: conductor \(4\) has support
\(v_2(z)=e-2\) and magnitude \(2^{e-1}\); conductors \(8\) have support
\(v_2(z)=e-3\) and magnitude \(2^{e-3/2}\). The reported two-adic
recombination of \(\chi_8\) and \(\chi_{-8}\) selects
\[
 \frac{j}{2^{v_2(m)-1}}\equiv3\pmod4
\]
when \(v_2(m)\) is odd, and its two-adic magnitude is
\(2^{v_2(m)+1}\). Direct substitution of the four residue values verifies
both the phase and the half-support.

The local report's physical two-adic root table is also exact. For
\(t=2^v u\) modulo \(2^e\), the number of roots of \(x^2\equiv t\pmod{2^e}\)
is \(2^{\lfloor e/2\rfloor}\) when \(v\ge e\), is zero when \(v<e\) is
odd, and, for \(v=2a<e\), is \(2^a g_{e-2a}(u)\), where
\[
 g_1(u)=1,\qquad
 g_2(u)=2{\bf1}_{u\equiv1\ (4)},\qquad
 g_k(u)=4{\bf1}_{u\equiv1\ (8)}\quad(k\ge3).
\]
This follows by writing \(x=2^a y\) and using the elementary classification
of odd squares modulo \(2,4,\) and \(2^k\) for \(k\ge3\).

Finally, Montgomery--Vaughan Theorem 9.18 gives

\[
 \sum_{M<n\le M+H}\chi(n)\ll\sqrt f\log f
\tag{156.IS29}
\]

for a nonprincipal character modulo \(f\). Every \(f_\pm>1\) constituent
in the candidate is primitive and nonprincipal, so its use after subsequence
BV and Abel summation is legal; the logarithm is absorbed into
\(X^\varepsilon\). The conductor-one constituent is separately treated by
the exact Ramanujan formula. This validates the Pólya--Vinogradov fallback,
but (156.IS11)--(156.IS14) show that it is unnecessary.

## 4. First doubtful or unproved step

There is no source or legal-method defect in the frozen \(v=0\) theorem
under the inherited literal-profile hypotheses. The most audit-sensitive
input is (156.IS8), but the blind derivation and hostile endpoint review prove
it component-independently from (156.IS7), the \(O(K)\) physical support,
the exact phase, and the exact cell.

The initial source report's former first open step, its progression-BV bound
(156.SA23), is now a corollary of (156.IS8) and (156.IS10). Accordingly,
the earlier statement that no audited external theorem controls an arbitrary
coefficient remains true but no longer bears on this fixed coefficient or on
the zero-row conclusion.

The first unresolved object after the present result is the nonzero matrix

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{156.IS30}
\]

The fixed-\(d\) zero-frequency geometric argument and the fully recombined
root/Fourier identity do not extend to this coupled \(j,v,x,a\) object.
The earlier source-interface cautions remain applicable to proposed
nonzero-matrix continuations. Nothing here changes any broader owner.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| blind_fixed_d_geometric_interval | **GREEN.** Equation (156.IS12) is an exact finite geometric-series estimate; summing nonzero unit frequencies proves (156.IS2) without a theorem. |
| recombined_finite_Fourier_interval | **GREEN.** Equations (156.IS15)--(156.IS22) use only finite orthogonality, the complete quadratic magnitude, a geometric series, and divisor grouping. |
| exact_recombination_phase_and_normalization | **GREEN.** Equations (156.IS16)--(156.IS18) reproduce the factor \(-i(1+i)/(2N)\), every odd \(d\), \(d\sqrt c\), and the remaining \(q^{-1}\). |
| literal_profile_BV | **GREEN.** Monotone sampling, zero-extended real variation, exact phase derivative, asymmetric cell, and \(O(K)\) representatives prove (156.IS8). |
| progression_BV_contraction | **GREEN.** Equation (156.IS10) proves the initial audit's formerly missing norm for every induced subsequence. |
| primitive_conductors_and_phases | **GREEN.** Fundamental-discriminant classification and (156.IS25) match Montgomery--Vaughan Theorems 9.13 and 9.17. |
| induced_character_and_Ramanujan | **GREEN.** Equation (156.IS27) is direct inclusion-exclusion and matches Kıral--Zhou Lemmas 2.2--2.3 / Montgomery--Vaughan Theorem 9.12. |
| exact_two_adic_values | **GREEN.** Direct residue sums give \(2i,\sqrt8,i\sqrt8\); lifting gives the printed supports, phases, magnitudes, principal strata, half-support, and the physical root counts. |
| Polya_Vinogradov_fallback | **GREEN / OPTIONAL.** The constituents with \(f>1\) are primitive nonprincipal; the \(f=1\) Ramanujan branch is separate. |
| full_N_M_V_d_power_ledger | **GREEN.** Both (156.IS14) and (156.IS23) yield \(M^{-1/4}X^\varepsilon\) with no residual \(V,d,f\), squareful, or endpoint power. |
| earlier_source_no_match_reconciliation | **GREEN.** It was route-scoped and is superseded for \(v=0\) by the literal BV proof; no false universal weighted theorem is asserted. |
| nonzero_and_downstream_scope | **GREEN.** Equation (156.IS30), all broader owners, M9, bridge, target, and global exponent remain open. |

No numerical or symbolic experiment was used.

## 6. Dependencies, artifacts, and sources used

### Claimant and review artifacts

- protocol.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_local_factor_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/blind_zero_mode_character_rederivation.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_target.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_character_source_audit.md.

### Authoritative source checks

1. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I:
   Classical Theory*, Chapter 9, especially Theorems 9.12, 9.13, 9.17,
   and 9.18,
   [author-hosted Cambridge chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/13.0_pp_282_325_Primitive_characters_and_Gauss_sums.pdf).
2. E. M. Kıral and F. Zhou, *The Voronoi formula and double Dirichlet
   series*, Algebra & Number Theory 10 (2016), Definition 2.1 and
   Lemmas 2.2--2.3,
   [journal PDF](https://msp.org/ant/2016/10-10/ant-v10-n10-s.pdf).
3. W. Duke, J. B. Friedlander, and H. Iwaniec, *Weyl Sums for Quadratic
   Roots*, Section 6,
   [author PDF](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf).

The sources corroborate exact finite identities and the optional
Pólya--Vinogradov fallback. Neither elementary proof of (156.IS1) depends
on a literature theorem.

## 7. Recommended state effect

Promote **outer_defect_zero_mode_target** with the stronger bound
\(M^{-1/4}X^\varepsilon\), the literal coefficient BV lemma, and either
elementary closure; preferably retain both as independent seams. Retain the
exact character/conductor/local tables as verified arithmetic detail, but do
not present Pólya--Vinogradov as necessary.

Replace the initial source audit's terminal label
**strict_outer_defect_zero_mode_range** by the full zero-mode result. Preserve
that audit only as a route-scoped record: external arbitrary-weight,
maximal-unweighted, and analytic conductor-lowering results did not match the
uncontrolled coefficient, but the coefficient is now controlled internally.

Remove only the \(v=0\) row from the missing-input list. Keep the nonzero
matrix (156.IS30), the selected signed cross-fibre seam, every \(D>1,L>1\),
generic and \(t\ge2\) owner, M2, endpoint assembly, M9, bridge, final target,
and global exponent unchanged.

**Verdict: GREEN. First defect: none.**

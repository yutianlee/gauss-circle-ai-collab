# Round 156 primary-source audit: the theta zero row as induced quadratic-character Fourier transforms

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Task: zero_mode_character_source_audit
- Role: primary-source auditor
- Literature checked through: 25 August 2026
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

### Exact arithmetic evaluation, a source-legal strict zero-row range, and a coefficient-interface no-match

Put

\[
 q=4N,\qquad J_A=M^{3/4}(\log(2X))^A,\qquad
 K=\sqrt{NM},\qquad J_A<V\le K,
\]

and, for every odd \(d\mid N\), put

\[
 m=\frac Nd,\qquad c=4m.
\]

The literal row is

\[
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi _4(d)d\sqrt c\,
 \widehat B_j(0)K(0,-j;c).
\tag{156.SA1}
\]

The source audit gives five conclusions.

1. The zero-frequency multiplier is exactly a sum of two induced real
   character transforms.  If
   \[
     s=\operatorname{sf}(m)=\prod_{v_p(m)\ {\rm odd}}p
   \]
   is the squarefree kernel of \(m\), define the two fundamental
   discriminants
   \[
   \Delta_+(s)=
   \begin{cases}s,&s\equiv1\pmod4,\\4s,&s\not\equiv1\pmod4,\end{cases}
   \qquad
   \Delta_-(s)=
   \begin{cases}-s,&s\equiv3\pmod4,\\-4s,&s\not\equiv3\pmod4.\end{cases}
   \tag{156.SA2}
   \]
   Let \(\chi_\pm(n)=(\Delta_\pm/n)\) be the primitive quadratic
   characters of conductors \(f_\pm=|\Delta_\pm|\).  Then \(f_\pm\mid c\)
   and
   \[
   K(0,-j;c)=\frac{1+i}{2}T_+(j;c)
             +\frac{1-i}{2}T_-(j;c),
   \quad
   T_\pm(j;c)=\sum_{a\bmod c}^{*}\chi_\pm(a)e_c(-aj).
   \tag{156.SA3}
   \]
   There is no squarefree, odd-\(N\), or primitive-modulus assumption in
   (156.SA3).

2. Kıral--Zhou Lemmas 2.2--2.3, equivalently Montgomery--Vaughan
   Theorem 9.12, evaluate each \(T_\pm\) exactly.  If
   \(g=(c,j)\), \(r=c/g\), and \(f=f_\pm\), then
   \[
   T_\pm(j;c)=0\quad\text{if }f\nmid r,
   \tag{156.SA4}
   \]
   while, if \(f\mid r\),
   \[
   T_\pm(j;c)=
   \tau(\chi_\pm)
   \frac{\phi(c)}{\phi(r)}
   \mu\!\left(\frac r f\right)
   \chi_\pm\!\left(\frac r f\right)
   \chi_\pm\!\left(\frac{-j}{g}\right).
   \tag{156.SA5}
   \]
   Formula (156.SA5), including zeros of the character factors, is the
   complete induced-modulus, Ramanujan, squareful, and valuation-support
   formula.  The Gauss phase is exact:
   \[
     \tau(\chi_{\Delta})=
     \begin{cases}\sqrt{\Delta},&\Delta>0,\\
                   i\sqrt{|\Delta|},&\Delta<0.
     \end{cases}
   \tag{156.SA6}
   \]

3. The already source-audited DFI pointwise theorem proves the strict
   owner-complete zero-row range
   \[
   \boxed{\quad
   J_A<V\le
   \min\{\sqrt{NM},\,\sqrt N\,M^{1/4}\}
   \quad\Longrightarrow\quad
   \mathcal Z_U(V)\ll_{\varepsilon,A}X^\varepsilon .
   \quad}
   \tag{156.SA7}
   \]
   Indeed, uniformly on the whole frozen range,
   \[
   |\mathcal Z_U(V)|
   \ll_\varepsilon
   \left(\frac{V}{\sqrt N\,M^{1/4}}+M^{-1/4}\right)X^\varepsilon.
   \tag{156.SA8}
   \]
   Since \(M\le N^{1/2}\), the upper endpoint in (156.SA7) exceeds
   \(J_A\) by
   \(\sqrt{N/M}/(\log(2X))^A\), a fixed positive power for large \(X\).
   This is a theorem only for the zero row; it was not a range for the
   full zero-plus-nonzero matrix in Round 155.

4. The exact character formulas show that classical character cancellation
   would in fact be strong enough for the complete zero-row range if one
   first proved the literal profile-variation estimate (156.SA23) below.
   Under that missing estimate, Pólya--Vinogradov gives
   \[
     \mathcal Z_U(V)\ll_\varepsilon M^{-1/4}X^\varepsilon
     \quad(J_A<V\le K),
   \tag{156.SA9}
   \]
   and the \(r=2\) Burgess bound gives, at the worst endpoint,
   \[
     \mathcal Z_U(K)\ll_\varepsilon N^{-1/16}X^\varepsilon
   \tag{156.SA10}
   \]
   for all nonprincipal pieces, with the principal Ramanujan piece handled
   separately.  Every conductor, support progression, \(d\)-stratum, and
   exterior factor is restored in Section 3.5.

5. No audited primary theorem supplies (156.SA23) for the actual
   \(\widehat B_j(0)\).  Pólya--Vinogradov and Burgess are unweighted
   interval theorems.  Heath-Brown's maximal theorem maximizes an
   unweighted interval endpoint and averages well-spaced starting points;
   it does not accept a deterministic complex coefficient sequence.
   Adamczewski--Treviño treats one prescribed triangular weight, not the
   literal cell/profile/residual-phase weight.  Analytic
   conductor-lowering theorems such as Sun--Zhao are global smoothed
   automorphic statements with prime-power conductor and do not specialize
   to (156.SA1).  This is a direct source-interface no-match.  A saving
   uniform over arbitrary bounded complex weights is genuinely impossible:
   choosing a weight conjugate to the surviving character phase removes all
   cancellation.  That impossibility does **not** apply to the actual
   \(\widehat B_j(0)\), whose special variation remains an internal open
   question.

Thus this report supports the route label
strict_outer_defect_zero_mode_range, with (156.SA7) as the strict range.
It does not support outer_defect_zero_mode_target on the entire range and
does not establish an arithmetic impossibility theorem.

## 2. Exact statement, hypotheses, and primary theorem cards

### 2.1 Literal coefficient and endpoint hypotheses

The two sign intervals are kept separately:

\[
 I_+(V)=\{j\in\mathbb Z:V<j\le2V\},\qquad
 I_-(V)=\{j\in\mathbb Z:-2V\le j<-V\}.
\tag{156.SA11}
\]

Write \(A_j=\widehat B_j(0)=\sum_{x\bmod q}B_j(x)\).  The inherited
source-legal bound is

\[
 |A_j|\ll_\varepsilon K M^{-3/4}X^\varepsilon
 =\sqrt N\,M^{-1/4}X^\varepsilon.
\tag{156.SA12}
\]

Here \(B_j\) is the ambient, pre-linearization coefficient.  It retains
the asymmetric cell, zero extension, literal profile components and
transitions, strict dyadic mask, both defect signs, exact residual phase,
and hard endpoints.  The selected linearization is not inserted into
\(A_j\).  The external \(B_{1,U}(1)\) factor is not part of
\(\mathcal Z_U(V)\) and remains an assembly seam.

### 2.2 Primitive quadratic conductor and Gauss-phase card

Montgomery--Vaughan,
[*Multiplicative Number Theory I*, Chapter 9, Theorems 9.13 and
9.17](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/13.0_pp_282_325_Primitive_characters_and_Gauss_sums.pdf),
classifies primitive quadratic characters as the Kronecker characters
\(\chi_\Delta=(\Delta/\cdot)\) attached uniquely to quadratic
discriminants \(\Delta\), and evaluates their Gauss sums as (156.SA6).
The definition permits exactly the discriminants in (156.SA2): an odd
squarefree \(\Delta\equiv1\pmod4\), or
\(\Delta=4D\) with squarefree \(D\equiv2,3\pmod4\).

This card determines rather than assumes the conductors \(f_\pm\).  In
particular,

\[
\begin{array}{c|cc}
s\bmod4 & f_+ & f_-\\ \hline
1 & s & 4s\\
3 & 4s & s\\
2 & 4s & 4s
\end{array}
\tag{156.SA13}
\]

where the last line means \(s\) is even squarefree.  The case \(s=1\)
makes \(\chi_+\) the primitive principal character of conductor \(1\);
\(\chi_-\) is never principal.

### 2.3 Induced-character Fourier-transform and Ramanujan card

Kıral--Zhou,
[*The Voronoi formula and double Dirichlet
series*](https://msp.org/ant/2016/10-10/ant-v10-n10-s.pdf),
Definition 2.1 and Lemmas 2.2--2.3, define

\[
 g(\chi^*,c,n)=\sum_{a\bmod c}^{*}\chi^*(a)e_c(an)
\]

when the character modulo \(c\) is induced from the primitive
\(\chi^*\bmod f\), and prove

\[
 g(\chi^*,c,n)=
 \tau(\chi^*)\!
 \sum_{\ell\mid(n,c/f)}
 \ell\,\chi^*\!\left(\frac{c}{f\ell}\right)
 \overline{\chi^*}\!\left(\frac n\ell\right)
 \mu\!\left(\frac{c}{f\ell}\right).
\tag{156.SA14}
\]

Their equivalent Lemma 2.3 is exactly (156.SA4)--(156.SA5).  The source
allows arbitrary \(c\) divisible by \(f\), arbitrary integer frequency
\(n\), a principal primitive inducing character, and imprimitive
modulus.  It therefore matches \(n=-j\), \(c=4N/d\), and both
\(\chi_\pm\) exactly.  Kıral--Zhou Lemma 2.4 also records the induced
Gauss sums as the Ramanujan-factor generating series; no analytic
continuation or infinite series is needed here.

### 2.4 Zero-argument theta/Salié card

Duke--Friedlander--Iwaniec,
[*Weyl Sums for Quadratic
Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
Section 6, equations (6.3)--(6.8), define

\[
 K(u,v;c)=\sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(u\bar a+va),
 \qquad 4\mid c,
\]

factor its odd part through a Salié sum, evaluate the two-adic part, and
prove in Lemma 6.1

\[
 |K(u,v;c)|\le (u,v,c)^{1/2}c^{1/2}\tau(c)
\tag{156.SA15}
\]

for arbitrary integers \(u,v\) and arbitrary composite \(c\equiv0\pmod4\).
Thus \(u=0\) is explicitly legal.  The official
[*erratum*](https://doi.org/10.1093/imrn/rnr240) does not alter Section 6.
This card proves (156.SA8), but it is a pointwise upper bound and contains
no signed outer-\(j\) conclusion.  DFI's later Weyl identities
(6.9)--(6.11) impose a discriminant \(D\equiv1\pmod4\) and do not replace
the exact arbitrary-\(m\) evaluation (156.SA3)--(156.SA5).

### 2.5 Pólya--Vinogradov, Burgess, and maximal cards

For a primitive \(\chi\bmod f\), Bordignon,
[*Partial Gaussian sums and the Pólya--Vinogradov inequality for primitive
characters*](https://arxiv.org/pdf/2001.05114), proves uniformly in the
endpoint

\[
 \max_H\left|\sum_{1\le n\le H}\chi(n)\right|
 \ll \sqrt f\log f,
\tag{156.SA16}
\]

with explicit parity-dependent constants.  Taking a difference of two
initial sums gives the same order for an arbitrary interval.  It assumes
a primitive character and unit coefficient; it does not include
\(A_{\ell n}\).

Heath-Brown,
[*Burgess's Bounds for Character
Sums*](https://arxiv.org/pdf/1203.5219), equation (1), records, uniformly
in the starting point,

\[
 \sum_{M<n\le M+H}\chi(n)
 \ll_{\varepsilon,r}
 H^{1-1/r}f^{(r+1)/(4r^2)+\varepsilon},
\tag{156.SA17}
\]

when \(\chi\) is nonprincipal, provided \(f\) is cube-free or \(r\le3\).
We use only \(r=2\), so every fundamental discriminant conductor in
(156.SA13), including its full factor \(8\), is legal.  The paper's
maximal theorem assumes a primitive character, \(H\le f\), starting
points separated by at least \(H\), and bounds

\[
 \sum_{\nu=1}^{J}
 \max_{h\le H}|S(N_\nu;h)|^{3r}
 \ll_{\varepsilon,r}
 H^{3r-3}f^{3/4+3/(4r)+\varepsilon}
\tag{156.SA18}
\]

provided either \(r=1\), or
\(H\ge f^{1/(2r)+\varepsilon}\) together with \(r\le3\), or
\(H\ge f^{1/(2r)+\varepsilon}\) together with cube-free \(f\).
Lemma 3 similarly gives moments of
\(\max_{h\le H}|S(n;h)|\) averaged over every \(n\bmod f\): its
second-moment estimate is valid for all \(f\), and its \(2r\)-moment
estimate assumes cube-free \(f\) or \(2\le r\le3\).  Neither result
inserts arbitrary deterministic weights.

The closest primary weighted theorem located is
Adamczewski--Treviño,
[*The Smoothed Pólya--Vinogradov
Inequality*](https://campus.lakeforest.edu/trevino/SmoothedPV.pdf),
Theorem 1.  It assumes primitive \(\chi\bmod f>1\),
\(0<H\le f\), and the particular triangular weight
\[
 W(n)=\max\{0,1-|n-M|/H\},
\]
and proves a bound \(<\sqrt f\).  Its imprimitive corollaries retain this
same prescribed weight.  The actual \(A_j\) is not triangular, and no
source-legal representation with target-sized total coefficient norm is
available.

### 2.6 Analytic conductor-lowering card

Sun--Zhao,
[*Bounds for \(GL_3\) \(L\)-functions in depth
aspect*](https://arxiv.org/abs/1803.10973), Theorem 1 and Section 3.1,
assume a fixed \(GL_3\) Hecke--Maaß form, a primitive character of
prime-power conductor \(p^\kappa\), a smooth \([1,2]\)-supported
approximate-functional-equation weight, and insert
\(n\equiv m\pmod{p^\lambda}\) before a circle method, Poisson, Voronoi,
and Cauchy--Schwarz argument.  This is not a theorem for one finite
Fourier transform, arbitrary composite \(4N/d\), a conductor varying
with \(d\), or the coefficient \(A_j\).  The only conductor lowering
that applies literally here is the exact finite induction formula
(156.SA14); importing a global subconvex theorem does not supply an
outer-\(j\) estimate.

## 3. Proof and derivation

### 3.1 Exact two-character decomposition and primitive conductors

For odd \(a\),

\[
 \epsilon_a=\frac{1+i}{2}+\frac{1-i}{2}\chi_4(a),
\tag{156.SA19}
\]

because the right side is \(1\) for \(a\equiv1\pmod4\) and \(i\) for
\(a\equiv3\pmod4\).  On units modulo \(4m\),

\[
 \left(\frac ma\right)=\left(\frac sa\right)
 =\chi_{\Delta_+}(a),\qquad
 \chi_4(a)\left(\frac ma\right)
 =\left(\frac{-s}{a}\right)=\chi_{\Delta_-}(a).
\]

The classification of quadratic discriminants proves (156.SA2),
(156.SA3), and (156.SA13), including \(s=1\) and the full two-adic
conductor.  This is a derivation, not a primitive-character assumption.

Because \(\Delta_+>0\) and \(\Delta_-<0\), \(T_+\) is real and \(T_-\)
is purely imaginary.  If \(T_+=A\) and \(T_-=iB\), \(A,B\in\mathbb R\),
then

\[
 K(0,-j;c)=\frac{1+i}{2}(A+B).
\tag{156.SA20}
\]

This permits cancellation only through the exact signed local values
\(A+B\).  It is not a general two-piece cancellation theorem.

### 3.2 Complete prime-power and two-adic local table

Let \(p^e\Vert c\), let \(p^\kappa\Vert f_\pm\), and let
\(\chi_{\pm,p}\) be the primitive \(p\)-primary factor.  Under CRT put
\[
 C_p=c/p^e,\qquad u_pC_p\equiv1\pmod{p^e}.
\]
The exact local transform is
\[
 T_{\pm,p}(j)=
 \sum_{a\bmod p^e}^{*}
 \chi_{\pm,p}(a)e_{p^e}(-ju_pa).
\]
If \(\kappa>0\), then
\[
 T_{\pm,p}(j)=
 \begin{cases}
 p^{e-\kappa}\tau(\chi_{\pm,p})
 \chi_{\pm,p}(-ju_p/p^{e-\kappa}),
       &v_p(j)=e-\kappa,\\
 0,&\text{otherwise},
 \end{cases}
\tag{156.SA21}
\]
and the surviving magnitude is \(p^{e-\kappa/2}\).  If \(\kappa=0\),
then
\[
 T_{\pm,p}(j)=c_{p^e}(j)=
 \begin{cases}
 0,&v_p(j)\le e-2,\\
 -p^{e-1},&v_p(j)=e-1,\\
 p^{e-1}(p-1),&v_p(j)\ge e.
 \end{cases}
\tag{156.SA22}
\]

For an odd \(p\), \(e=v_p(m)\).  If \(e\) is odd, then
\(\kappa=1\) for both signs, support is exactly
\(v_p(j)=e-1\), and the magnitude is \(p^{e-1/2}\).  If \(e\ge2\)
is even, then \(\kappa=0\) for both signs and (156.SA22) is the
squareful Ramanujan degeneration.  In the odd-exponent case the local
character is the Legendre symbol modulo \(p\), with
\(\tau(\chi_p)=\sqrt p\) for \(p\equiv1\pmod4\) and
\(\tau(\chi_p)=i\sqrt p\) for \(p\equiv3\pmod4\); (156.SA21)'s
\(\chi_p(-ju_p/p^{e-1})\) is the remaining exact phase.

At \(p=2\), put \(\nu=v_2(m)\), so \(e=\nu+2\).

- If \(\nu\) is even, \(s\) is odd.  One sign has \(\kappa=0\) and
  support \(v_2(j)\ge e-1\) with the two exact Ramanujan values in
  (156.SA22); the other has \(\kappa=2\), support
  \(v_2(j)=e-2\), magnitude \(2^{e-1}\), local character \(\chi_4\),
  and Gauss phase \(\tau(\chi_4)=2i\).  Which sign is principal at
  \(2\) is given by (156.SA13): it is \(+\) when \(s\equiv1\pmod4\)
  and \(-\) when \(s\equiv3\pmod4\).  The two supports are disjoint.
- If \(\nu\) is odd, then \(\kappa=3\) for both signs, support is
  exactly \(v_2(j)=e-3=\nu-1\), and the magnitude is
  \(2^{e-3/2}\).  The primitive local character is one of
  \(\chi_8,\chi_{-8}\), determined uniquely by \(\Delta_\pm\), with
  Gauss phase respectively \(\sqrt8\) or \(i\sqrt8\).  Formula
  (156.SA21), including the CRT unit \(u_2\), gives the exact sign.

The global transform is \(\prod_{p^e\Vert c}T_{\pm,p}(j)\).
Equivalently, (156.SA5) supplies its exact phase without any CRT
convention.  These formulas include \(j=0\), principal local factors,
all repeated prime powers, and both signs of \(j\).  For example, when
\(m=1\), \(f_+=1\), \(f_-=4\), so the Ramanujan and primitive
two-adic transforms occupy complementary parities; no stratum is lost.

### 3.3 The \(d\)-strata cannot be merged before evaluation

For every odd \(d\mid N\),
\[
 m=N/d,\quad s=\operatorname{sf}(N/d),\quad
 f_\pm=f_\pm(d),\quad c=4N/d.
\]
Removing an odd prime factor through \(d\) can change the parity of its
remaining valuation and hence move that prime between the primitive
conductor and a Ramanujan factor.  The two-adic exponent
\(v_2(c)=v_2(N)+2\) is fixed because \(d\) is odd, but which
two-adic primitive character occurs depends on the squarefree kernel of
\(N/d\).  Thus there is no common conductor or common support
progression across all \(d\).

Finite interchange of the \(d,\ell,j\) sums in (156.SA14) is legal.
Calling it “divisor switching” does not by itself save a power: the
conductor, support progression, profile value \(A_j\), sign interval,
and endpoint all still depend on the switched variables.

### 3.4 Restored absolute range

Apart from the harmless fixed factor \(|1+i|\), the exterior size of a
single \(d\)-stratum is

\[
 P_d=\frac{d\sqrt c}{2Nq}
     =\frac{\sqrt d}{4N^{3/2}},
\qquad
 P_d\,c^{1/2}=\frac1{2N}.
\]

DFI (156.SA15), (156.SA12), and
\[
 \sum_{V<|j|\le2V}(j,c)^{1/2}
 \ll_\varepsilon(V+\sqrt c)c^\varepsilon
\]
give
\[
\begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 \frac{\sqrt N\,M^{-1/4}}{N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 (V+\sqrt{4N/d})X^\varepsilon\\
 &\ll_\varepsilon
 \left(\frac{V}{\sqrt N\,M^{1/4}}+M^{-1/4}\right)X^\varepsilon,
\end{aligned}
\]
which proves (156.SA7)--(156.SA8).  Both sign intervals, every
\(d\), all gcd and two-adic strata, and the literal endpoints are
present.  At \(V=K\), the first term is \(M^{1/4}\); this is an upper
capacity, not a lower bound.

### 3.5 Literal weighted partial-summation seam and restored powers

For \(I=I_+(V)\) or \(I_-(V)\) and \(\ell\ge1\), list
\(I\cap\ell\mathbb Z=\{j_1<\cdots<j_R\}\) and define the exact
endpoint-inclusive progression variation

\[
 \mathcal A_\ell(I)=
 \begin{cases}
 |A_{j_1}|+\displaystyle\sum_{r=1}^{R-1}|A_{j_{r+1}}-A_{j_r}|
              +|A_{j_R}|,&R\ge1,\\
 0,&R=0.
 \end{cases}
\]

Thus both jumps to the zero extension are charged.  The missing internal
profile lemma is

\[
 \boxed{\quad
 \mathcal A_\ell(I_\pm(V))
 \ll_\varepsilon
 \sqrt N\,M^{-1/4}X^\varepsilon
 \quad\text{for every }d,\ \pm,\ 
 \ell\mid c/f_\pm .
 \quad}
\tag{156.SA23}
\]

The first and last terms in this norm price the strict mask, zero
extension, and hard endpoints; every internal jump prices an actual
profile or cell transition.  No symmetry between \(I_+\) and \(I_-\)
is assumed.

Assume (156.SA23) only for the following power translation.  Put
\(L=c/f\).  From (156.SA14),

\[
 \sum_{j\in I}A_jT_\pm(j;c)
 =\tau(\chi_\pm)
 \sum_{\substack{\ell\mid L\\\ell\le2V}}
 \ell\chi_\pm(L/\ell)\mu(L/\ell)
 \sum_{\substack{j\in I\\\ell\mid j}}
 A_j\chi_\pm(-j/\ell).
\tag{156.SA24}
\]

The restriction \(\ell\le2V\) is exact because the inner progression is
empty otherwise.  When it is nonempty, its length is at most
\(V/\ell+1\le3V/\ell\), so the hard endpoints do not create an omitted
unit term in the estimates below.

When \(f>1\), Abel summation and Pólya--Vinogradov give
\[
 \left|\sum_{j\in I}A_jT_\pm(j;c)\right|
 \ll_\varepsilon
 (\sqrt N\,M^{-1/4})\,
 f\log f\sum_{\ell\mid L}\ell
 \ll_\varepsilon
 (\sqrt N\,M^{-1/4})cX^\varepsilon.
\tag{156.SA25}
\]

When \(f=1\), \(T_\pm=c_c\).  Directly,
\[
 \sum_{A<n\le A+H}c_c(n)
 =\sum_{\ell\mid c}\ell\mu(c/\ell)
   \left(\left\lfloor\frac{A+H}{\ell}\right\rfloor
        -\left\lfloor\frac A\ell\right\rfloor\right)
 =O\!\left(\sum_{\ell\mid c}\ell|\mu(c/\ell)|\right)
 \ll_\varepsilon c^{1+\varepsilon},
\]
because the main term is
\(H\sum_{\ell\mid c}\mu(c/\ell)=0\) for \(c=4m>1\).  Abel summation
gives the same final right side as (156.SA25).  Restoring the exact
character-piece coefficient
\(P_d\), for which the factors \(|1+i|\) and
\(|(1\pm i)/2|\) cancel, gives
\[
 P_d\,(\sqrt N\,M^{-1/4})c
 =(\sqrt N\,M^{-1/4})\frac{\sqrt c}{2N}
 =\frac{M^{-1/4}}{\sqrt d}.
\]
Summing every odd \(d\mid N\) proves the conditional bound (156.SA9).

For Burgess with \(r=2\), the inner interval in (156.SA24) has length
\(\ll V/\ell+1\).  Abel summation gives
\[
 \left|\sum_{j\in I}A_jT_\pm(j;c)\right|
 \ll_\varepsilon
 (\sqrt N\,M^{-1/4})
 V^{1/2}c^{1/2}f^{3/16}X^\varepsilon.
\tag{156.SA26}
\]
After \(P_dc^{1/2}=1/(2N)\), all \(d\), and
\(f_\pm(d)\le c=4N/d\),
\[
 |\mathcal Z_U(V)|_{\rm nonprincipal}
 \ll_\varepsilon
 (\sqrt N\,M^{-1/4})V^{1/2}N^{-13/16}X^\varepsilon.
\tag{156.SA27}
\]
At \(V=K=\sqrt{NM}\), this is \(N^{-1/16}X^\varepsilon\),
which is (156.SA10).  The conductor-one Ramanujan piece is covered by
the separate argument immediately after (156.SA25).  These are
conditional theorem capacities, not proved
bounds, because (156.SA23) is not available.

### 3.6 Why direct interchange and maximal theorems do not bypass the seam

Interchanging \(j\) and \(a\) in (156.SA3) is a legal finite identity,
but it leaves
\[
 \sum_{j\in I_\pm(V)}A_je_c(-aj),
\]
the incomplete Fourier transform of the literal coefficient.  No
audited theorem bounds this uniformly with the needed gain.  Replacing
\(A_j\) by a constant, a triangle, a globally smooth bump, or a
separated coefficient changes the problem.

Heath-Brown's maximum is over the endpoint \(h\) of an unweighted
character interval and its gain is averaged over starting points with a
spacing hypothesis.  There is only one prescribed weighted interval
for each \((d,\ell,\pm)\), and these starts are not a new averaging
family.  Sun--Zhao conductor lowering introduces a congruence inside a
smoothed automorphic bilinear sum; it is not an operator that lowers
\(f_\pm(d)\) in (156.SA24) while preserving \(A_j\).  Consequently the
first source-illegal step in each proposed continuation is the deletion
or unpriced replacement of \(\mathcal A_\ell(I_\pm)\).

The claimed limitation for arbitrary bounded weights is exact.  For a
nonprincipal primitive character \(\chi\bmod f\), choose
\(w_n=\overline{\chi(n)}\) on an interval.  Then \(|w_n|\le1\) and
\[
 \sum_{n\in I}w_n\chi(n)=\#\{n\in I:(n,f)=1\}.
\]
Thus a Pólya--Vinogradov- or Burgess-sized estimate cannot hold
uniformly for every bounded deterministic weight on long intervals.
Likewise one may align with the phase of a surviving induced local
transform.  This construction says nothing adverse about the one fixed
sequence \(A_j=\widehat B_j(0)\).

## 4. First doubtful or unproved step

The primitive conductors, induced-modulus transforms, Ramanujan factors,
all odd and two-adic local supports, exact phases, the \(d\)-sum, and the
strict range (156.SA7) are source-legal.

The first unproved continuation to the full range is exactly
(156.SA23), or a weaker aggregate substitute strong enough to make,
for each of the two character signs with \(f_\pm(d)>1\),

\[
 \sum_{\substack{d\mid N\\d\ {\rm odd}\\f_\pm(d)>1}}
 P_d\sqrt{f_\pm(d)}
 \sum_{\substack{\ell\mid c/f_\pm(d)\\\ell\le2V}}
 \ell\,\mathcal A_\ell(I_\pm)
 \min\!\left\{
 1+\frac V\ell,\,
 \sqrt{f_\pm}\log f_\pm,\,
 \left(1+\frac V\ell\right)^{1/2}f_\pm^{3/16+\varepsilon}
 \right\}
 \ll X^\varepsilon
\tag{156.SA28}
\]

after both character signs and both defect signs are added.  Here the
subscript on the \(d\)-sum means that only its \(f_\pm(d)>1\) strata
occur.  The conductor-one strata instead require the separate
Ramanujan aggregate
\[
 \sum_{\substack{d\mid N,\ d\ {\rm odd}\\f_\pm(d)=1}}
 P_d\,c^{1+\varepsilon}\mathcal A_1(I_\pm)\ll X^\varepsilon,
\]
as in the paragraph following (156.SA25).  The
available context supplies only the supremum (156.SA12), not the
progression-variation norms.  No primary theorem audited here supplies
them from the literal asymmetric cell, residual phase, profile
transitions, zero extension, and endpoints.

This is a direct no-match for current source theorems, not an
impossibility theorem for the actual profile.  The only impossibility
statement is narrower and exact: no saving can hold uniformly for all
bounded complex weights, because a weight can align with the conjugate
of the surviving local character transform.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_zero_mode_row | **PASS.** Equation (156.SA1) retains the exact factor, every odd \(d\), both \(j\)-signs, and the ambient \(\widehat B_j(0)\). |
| exact_epsilon_two_character_decomposition | **PASS.** Equations (156.SA19) and (156.SA3) are exact for every odd unit. |
| primitive_conductor_and_induced_modulus | **PASS.** Equations (156.SA2), (156.SA4)--(156.SA5), and (156.SA13) derive both fundamental conductors and the full imprimitive transform. |
| all_prime_power_two_adic_local_factors | **PASS.** Equations (156.SA21)--(156.SA22) and the following tables include every odd prime power, \(\kappa=0,1,2,3\), the CRT phase, and exact magnitude. |
| valuation_support_and_squareful_strata | **PASS.** Odd exponent gives exact valuation \(e-1\); even exponent gives the two Ramanujan valuations; all two-adic alternatives and the conductor-one case are printed. |
| d_sum_and_full_normalization | **PASS.** \(P_d=\sqrt d/(4N^{3/2})\), \(P_dc^{1/2}=1/(2N)\), \(c=4N/d\), and \(\sum d^{-1/2}\) are restored. |
| actual_Bhat0_j_variation | **OPEN / FIRST OBSTRUCTION.** The exact required norm is (156.SA23).  The source context gives only (156.SA12); no surrogate weight is inserted. |
| positive_negative_defect_and_endpoints | **PASS.** \(I_+\) and \(I_-\) remain separate, and the seminorm includes entries, exits, strict inequalities, and internal transitions. |
| N_M_V_d_conductor_power_ledger | **PASS.** Equations (156.SA8), (156.SA25)--(156.SA27) restore all powers; the proven strict endpoint is \(V=\sqrt N M^{1/4}\), and the absolute top loss is \(M^{1/4}\). |
| source_theorem_zero_mode_match | **PASS / PARTIAL MATCH.** DFI matches pointwise; Kıral--Zhou matches the exact induced transform; Pólya--Vinogradov and Burgess match only after the missing profile-variation lemma.  Maximal, triangular-weight, and analytic conductor-lowering cards are direct no-matches. |
| upper_capacity_vs_signed_sum | **PASS.** Local support counts, DFI, Pólya--Vinogradov, Burgess, and (156.SA27) are upper capacities.  No large right side is called a lower bound. |
| nonzero_and_downstream_scope | **PASS.** Nothing here estimates the nonzero \(v\)-matrix, \(D>1\), \(L>1\), generic \(t=1\), original \(t\ge2\), the cross owner, M2, endpoint assembly, M9, the bridge, the quarter target, or a global exponent. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

### Project context

Every context artifact named in the task brief was used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round156_d1_outer_defect_zero_mode_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_seed.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/theta_bilinear_spectral_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_spectral_source_review.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md.

### Primary sources audited

1. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I:
   Classical Theory*, Chapter 9, Theorems 9.7, 9.12, 9.13, 9.17, and
   9.18, [author-hosted Cambridge chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/13.0_pp_282_325_Primitive_characters_and_Gauss_sums.pdf).
2. E. M. Kıral and F. Zhou, *The Voronoi formula and double Dirichlet
   series*, Algebra & Number Theory 10 (2016), 2267--2286,
   Definition 2.1 and Lemmas 2.2--2.4,
   [journal PDF](https://msp.org/ant/2016/10-10/ant-v10-n10-s.pdf).
3. W. Duke, J. B. Friedlander, and H. Iwaniec, *Weyl Sums for Quadratic
   Roots*, IMRN 2012, Section 6 and Lemma 6.1,
   [author PDF](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
   with the [official erratum](https://doi.org/10.1093/imrn/rnr240).
4. M. Bordignon, *Partial Gaussian sums and the Pólya--Vinogradov
   inequality for primitive characters*, arXiv:2001.05114v1,
   [primary PDF](https://arxiv.org/pdf/2001.05114).
5. D. R. Heath-Brown, *Burgess's Bounds for Character Sums*,
   Proceedings of the Steklov Institute of Mathematics 296 (2017),
   equation (1), the main theorem, and Lemmas 1--4,
   [primary arXiv PDF](https://arxiv.org/pdf/1203.5219).
6. D. A. Burgess, *On character sums and primitive roots*, Proc. London
   Math. Soc. (3) 12 (1962), 179--192,
   [primary record and scan](https://www.mathnet.ru/eng/mat267).
7. K. Adamczewski and E. Treviño, *The Smoothed
   Pólya--Vinogradov Inequality*, Integers 15 (2015), A20, Theorem 1
   and imprimitive corollaries,
   [author PDF](https://campus.lakeforest.edu/trevino/SmoothedPV.pdf).
8. Q. Sun and R. Zhao, *Bounds for \(GL_3\) \(L\)-functions in depth
   aspect*, Forum Mathematicum 31 (2019), Theorem 1 and Section 3.1,
   [primary arXiv text](https://arxiv.org/abs/1803.10973).

The literature conclusion is a dated direct-interface audit, not a claim
that this bibliography exhausts every related character-sum paper.  The
only workspace edit made by this task is this assigned report.

## 7. Recommended state effect

**Recommendation: record the strict zero-row range (156.SA7), retain the
full zero-row target as open, and record the exact coefficient-variation
source seam without promoting an impossibility claim.**

More precisely:

1. retain (156.SA2)--(156.SA6) as the exact primitive/induced
   character evaluation, subject to independent mathematical seam review;
2. record (156.SA7) as a source-legal, owner-complete positive-power
   range for the zero row only;
3. retain (156.SA8) and its top \(M^{1/4}\) term as an upper capacity,
   not a signed lower bound;
4. record (156.SA23), or the aggregate (156.SA28), as the first
   unproved input needed by Pólya--Vinogradov or Burgess;
5. record that maximal unweighted, prescribed triangular-weight, and
   analytic conductor-lowering theorems do not accept the literal
   \(A_j\), while a theorem uniform in arbitrary bounded weights is
   impossible by phase alignment;
6. do not alter the nonzero matrix, any broader owner, M9, the bridge,
   either global target, or either global exponent.

The source-audit label is strict_outer_defect_zero_mode_range.  The
remaining all-\(V\) conclusion is a direct source no-match at the
profile-variation interface, not
outer_defect_zero_mode_arithmetic_no_go.

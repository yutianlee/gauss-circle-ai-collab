# Round 144 post-unmask source and seam review

## 1. Result

The completion seam is green at the structural level and red at the
coefficient-estimate level.

Let

\[
 \mathcal H(\tau)=\frac12\widehat A_4
       \!\left(\frac12,-3\tau;2\tau\right)
 =F(\tau)+\frac14+\sum_{k=0}^3\mathcal R_k(\tau)
\tag{144.P1}
\]

be the source-normalized completed Appell section in the source audit.
The blind report's error-function correction

\[
 \mathcal R_{\rm cone}(\tau)
 =\frac14\sum_{\substack{h,r\in\mathbb Z\\r\ {\rm odd}}}
 \chi _4(r)
 \left[
 E\!\left(\frac{(r-4h)\sqrt y}{2}\right)
 -\operatorname {sgn}(r-4h)
 \right]e(hr\tau)
\tag{144.P2}
\]

is **exactly**, not merely up to a holomorphic or unary term,

\[
 \boxed{\mathcal R_{\rm cone}=\sum_{k=0}^3\mathcal R_k.}
\tag{144.P3}
\]

Consequently the blind error-function completion, its mixed
theta--theta \(\bar\partial\)-image, the four-term completed Appell
convention, the scalar law

\[
 \mathcal H(\gamma\tau)
 =\chi _4(d)(c\tau+d)\mathcal H(\tau)
 \qquad(\gamma\in\Gamma _0(4)),
\tag{144.P4}
\]

and the forced infinity-cusp constant \(1/4\) are one and the same
object.  The other two cusp slash constants are zero.  For
\(4\mid c\), the blind report's Abel/heat identity follows exactly
from (144.P4).  This identity preserves an individual complex
additive direction and retains the correction at both points.

This does **not** make a source-legal Voronoi or mock-coefficient
estimate for the literal square-root test.  The heat identity is one
pointwise Abel-kernel identity.  Passing from it to an arbitrary
compactly supported square-root oscillatory test requires a proved
superposition and uniform control of both transformed correction
terms.  No audited source supplies either.  The independent Round-63
character-Poisson identity is lawful for a smooth
\(C_c^\infty((0,\infty))\) test after global mask restoration, but its
principal family returns the accepted Round-140 reciprocal owner.

There is also one valid new algebraic sharpening.  For

\[
 \mathcal E_M(D)=
 \{m\in[M,2M):|k_m^2-Nm|\leq D\},
\tag{144.P5}
\]

uniformly for \(M\ll N^{1/2}\) and \(1\leq D<N/2\),

\[
 \boxed{\#\mathcal E_M(D)
 \ll_\varepsilon (D+\sqrt M+1)N^\varepsilon.}
\tag{144.P6}
\]

Taking \(D=M^{3/4}\) and using \(|C(m)|\ll_\varepsilon m^\varepsilon\)
shows that the whole enlarged window
\(|k_m^2-Nm|\leq M^{3/4}\) has normalized cost
\(O_\varepsilon(N^\varepsilon)\) per disjoint dyadic block and
globally.  Hence the original \(\sqrt M\)-masked scalar, the smooth
full cone, and the stricter survivor with
\(|k_m^2-Nm|>M^{3/4}\) are target-equivalent.  This is only an
algebraic owner reduction.  It does not remove derivative-stationary
arcs, estimate a correction pairing, or improve the \(R\)-capacity.

The terminal outcome remains

\[
 \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}.}
\tag{144.P7}
\]

No signed upper or lower bound follows from the capacity comparisons.

## 2. Exact statement and hypotheses

### 2.1 Completion equivalence

Use the precise definitions in Bringmann--van Ittersum--Kaszian,
equations (2.12)--(2.15):

\[
\begin{aligned}
 \mathcal R_k(\tau)
  =\frac{i}{4}(-1)^k
  \vartheta\!\left((2k-3)\tau+\frac32;8\tau\right)
  R_{\rm Zw}\!\left(\frac12+(3-2k)\tau;8\tau\right),
 \quad 0\leq k<4.
\end{aligned}
\tag{144.P8}
\]

Here

\[
 \vartheta(z;\tau)=
 \sum_{n\in\mathbb Z+1/2}e\!\left(n(z+1/2)\right)e(\tau)^{n^2/2},
\tag{144.P9}
\]

and \(R_{\rm Zw}\) is equation (2.13) of that source with
\(E(x)=2\int_0^x e^{-\pi t^2}\,dt\).  The specialization is pole-free:
\(1/2\notin 2\tau\mathbb Z+\mathbb Z\).  Formula (144.P3) is an
algebraic expansion of (144.P8), so it does not invoke the
nonintegral-isotropic-characteristic hypotheses that fail for a direct
application of Zwegers's Chapter 2 cone theorem.

The mixed shadow is

\[
 \frac{\partial\mathcal H}{\partial\bar\tau}
 =\frac{i}{16\sqrt y}
 \sum_{\mu\in\{1,3,5,7\}}
 \Theta_\mu(\tau)\overline{G_\mu(\tau)},
\tag{144.P10}
\]

where

\[
 \Theta_\mu(\tau)=\sum_{n\equiv\mu\ (8)}e(n^2\tau/16),
 \qquad
 G_\mu(\tau)=
 \sum_{a\equiv\mu\ (8)}\chi _4(a)a\,e(a^2\tau/16).
\tag{144.P11}
\]

This is the four-component contraction of weight-\(1/2\) and
weight-\(3/2\) unary Weil vectors.  It is not a newly established
scalar holomorphic shadow.  In particular, the audited data do not
place \(\mathcal H\) in the harmonic-Maass hypotheses used by the
summation sources in the source report.

### 2.2 Multiplier and cusp constants

For
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma _0(4)\), put

\[
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix},\qquad
 m_1=\frac c4,\quad r_1=\frac{d-1}{2},\quad
 m_2=-\frac{3(a-1)}2,\quad r_2=-3b.
\tag{144.P12}
\]

The source elliptic and modular factors cancel in their
\(\tau\)-dependent parts; the remaining factor is
\((-1)^{m_2}=\chi _4(d)\).  Thus (144.P4) is genuinely scalar on
\(\Gamma _0(4)\), while the full modular group moves among
characteristic components.

At infinity,

\[
 F(iy)=O(e^{-10\pi y}),\qquad
 \mathcal R_{\rm cone}(iy)
 =O(y^{-1/2}e^{-\pi y/4}),
\tag{144.P13}
\]

and hence

\[
 \boxed{\mathcal H(iy)=\frac14+
 O(y^{-1/2}e^{-\pi y/4}).}
\tag{144.P14}
\]

The \(1/4\) is half of the bilateral Appell zero term \(1/2\), or
equivalently half of the Abel value
\(\sum_{r>0,\ r\ {\rm odd}}\chi _4(r)t^r\to1/2\).
At the cusps \(0\) and \(1/2\), the transformed first characteristic
is respectively \(\pm(1/4,0)\) and \(\pm(1/2,0)\); it never meets the
isotropic wall \(h=0\), and on the other isotropic ray the two wall
signs agree.  Thus the appropriate weight-one slash transforms have
zero constant.

For a reduced cusp \(a/c\) in the infinity orbit, \(c>0\) and
\(4\mid c\), choose \(d\) with \(ad\equiv1\pmod c\).  Then

\[
 \mathcal H(a/c+iy)
 =\frac{i\chi _4(d)}{4cy}
 +O\!\left(
 \frac{(c^2y)^{1/2}}{cy}
 e^{-\pi/(4c^2y)}
 \right).
\tag{144.P15}
\]

### 2.3 Exact heat identity and its scope

Putting \(z=-d/c+i/(c^2y)\) in (144.P4) gives
\(\gamma z=a/c+iy\) and \(cz+d=i/(cy)\).  Therefore

\[
\begin{aligned}
 \sum_{m\geq1}C(m)e(am/c)e^{-2\pi my}
={}&\frac{i\chi _4(d)}{cy}
 \sum_{n\geq1}C(n)e(-dn/c)e^{-2\pi n/(c^2y)}\\
 &+\frac{i\chi _4(d)}{4cy}-\frac14\\
 &+\frac{i\chi _4(d)}{cy}
 \mathcal R_{\rm cone}\!\left(-\frac dc+\frac{i}{c^2y}\right)
 -\mathcal R_{\rm cone}\!\left(\frac ac+iy\right).
\end{aligned}
\tag{144.P16}
\]

This is an exact individual-direction identity for the Abel test and
is scalar-closed only in the infinity cusp class \(4\mid c\).  It is
not, without a further theorem, an identity for an arbitrary
\(C_c^\infty\) test and is not an estimate.

### 2.4 Displacement-count hypotheses

For (144.P6), \(k_m=\lfloor\sqrt{Nm}+1/2\rfloor\), the blocks are
half-open and disjoint, \(M\ll N^{1/2}\), and \(D<N/2\).  These
conditions ensure that all relevant \(k_m\) lie in an interval of
length \(O(\sqrt{NM})<N\).  The application
\(D=M^{3/4}\) satisfies \(D<N/2\) for all sufficiently large \(N\);
the bounded remainder is absorbed in the implied constant.

## 3. Proof and seam derivations

### 3.1 Expanding the four Appell corrections

In the \(k\)-th term of (144.P8), let
\(n,t\in\mathbb Z+1/2\) be respectively the theta and
\(R_{\rm Zw}\) indices.  Because

\[
 (-1)^{t-1/2}e(-t/2)=-i,
\tag{144.P17}
\]

the factor \(i/4\) in (144.P8) becomes \(1/4\).  Set

\[
 h=n+t,\qquad
 r=4(n-t)+2k-3,\qquad
 s=8t+3-2k.
\tag{144.P18}
\]

Then

\[
 r-4h=-s,\qquad
 4n^2+(2k-3)n-4t^2-(3-2k)t=hr,
\tag{144.P19}
\]

and

\[
 \chi _4(r)=(-1)^k,\qquad
 \operatorname {sgn}t=\operatorname {sgn}s.
\tag{144.P20}
\]

For each pair \(h\in\mathbb Z\), \(r\) odd, exactly one
\(k\in\{0,1,2,3\}\) makes the inverse values \(n,t\) half-integral;
thus (144.P18) is a bijection after summing over \(k\).
The summand in (144.P8) becomes

\[
 \frac14\chi _4(r)
 \left[
 E\!\left(\frac{(r-4h)\sqrt y}{2}\right)
 -\operatorname {sgn}(r-4h)
 \right]e(hr\tau).
\tag{144.P21}
\]

Summation proves (144.P3), with no residual holomorphic constant.  The
constant \(1/4\) belongs instead to the bilateral Appell zero term in
the holomorphic part.

### 3.2 Mixed shadow

Only the error function in (144.P2) is nonholomorphic.  Since
\(\partial_{\bar\tau}=\frac12(\partial_x+i\partial_y)\),
differentiation gives

\[
 \frac{\partial\mathcal H}{\partial\bar\tau}
 =\frac{i}{16\sqrt y}
 \sum_{\substack{h\in\mathbb Z\\r\ {\rm odd}}}
 \chi _4(r)(r-4h)
 e^{-\pi(r-4h)^2y/4}e(hr\tau).
\tag{144.P22}
\]

Put \(a=r-4h\).  Then

\[
 hr=4h^2+ah=\frac{(8h+a)^2}{16}-\frac{a^2}{16},
\tag{144.P23}
\]

and the Gaussian multiplying the last factor turns it into
\(\overline{e(a^2\tau/16)}\).  Grouping \(a\) modulo \(8\) gives
(144.P10)--(144.P11).  This proves that the blind mixed-shadow formula
is exactly the \(\bar\partial\)-image of the four Appell corrections.
It also shows why treating it as one disposable unary error is
incorrect.

### 3.3 Multiplier, cusps, and heat identity

Substitution of (144.P12) in the exact elliptic law (2.14) and modular
law (2.15) of the source gives an elliptic exponential

\[
 (-1)^{m_2}e\!\left(\frac{c(c+3a)}4\tau\right)
\]

and a modular exponential

\[
 (c\tau+d)e\!\left[
 -\frac c4\{(c+3a)\tau+d+3b\}
 \right].
\]

The variable terms cancel, and the constant exponential is one
because \(4\mid c\).  This proves (144.P4).  Equations
(144.P13)--(144.P15) then follow from the exact \(1/4\) constant and
the Gaussian estimate for (144.P2).  Expanding (144.P4) at the two
points in Section 2.3 proves (144.P16), including its signs, factor
\(i/(cy)\), two correction occurrences, and individual dual direction
\(e(-dn/c)\).

### 3.4 What coefficient summation is lawful

There are two distinct lawful identities:

1. Equation (144.P16) is the completed modular identity for a single
   Abel kernel.  It contains every completion owner.
2. The accepted Round-63 character-Poisson identity is an elementary
   coefficient formula for every
   \(w\in C_c^\infty((0,\infty))\).  After the Round-141 mask is
   restored globally and a smooth dyadic partition is inserted, the
   positive square-root direction belongs to that test class.

The second identity is not a consequence of merely writing
(144.P16), and neither identity supplies a cancellation estimate.
In the Round-63 formula the positive stationary family is exactly

\[
 e(1/8)N^{-1/4}
 \sum_{h,j>0}\frac{\chi _4(j)}h
 V_{\rm low}\!\left(\frac{4R^2h^2}{j^2}\right)
 \psi_M\!\left(\frac{4Nh^2}{j^2}\right)e(Nh/j),
\tag{144.P24}
\]

with half-boundary, subtraction, negative aliases, crossings,
transition, and remainders retained.  Owner-complete reassembly gives
the accepted Round-140 reciprocal scalar, not a smaller automorphic
survivor.  The blind sentence that general smooth transforms follow
from (144.P16) by “justified Laplace/Mellin superposition” is therefore
not established by the displayed argument and should not be promoted.

### 3.5 Gcd-averaged displacement count

For a nonzero integer \(A\), prime-power lifting gives

\[
 \#\{k\bmod N:k^2\equiv A\pmod N\}
 \ll_\varepsilon N^\varepsilon\sqrt{(A,N)}.
\tag{144.P25}
\]

Indeed, if \(p^\alpha\Vert A\) with \(\alpha<v_p(N)\), solutions vanish
for odd \(\alpha\), while for \(\alpha=2s\) there are at most a fixed
number of unit roots and \(p^s\) lifts; if \(p^{v_p(N)}\mid A\), there
are \(p^{\lfloor v_p(N)/2\rfloor}\) roots.  The Chinese remainder
theorem contributes only \(N^\varepsilon\).

The \(k_m\)-interval has length below \(N\), so each residue root
occurs at most once.  Also

\[
\begin{aligned}
 \sum_{1\leq |A|\leq D}\sqrt{(A,N)}
 &\leq
 \sum_{1\leq |A|\leq D}
 \sum_{d\mid(A,N)}\sqrt d\\
 &\ll D\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon DN^\varepsilon.
\end{aligned}
\tag{144.P26}
\]

For \(A=0\), the congruence \(N\mid k^2\) forces

\[
 \prod_{p^v\Vert N}p^{\lceil v/2\rceil}\mid k.
\tag{144.P27}
\]

This modulus is at least \(\sqrt N\), so the relevant \(k\)-interval
contains \(O(1+\sqrt M)\) such integers.  Equations
(144.P25)--(144.P27) prove (144.P6), including squareful \(N\).

With \(D=M^{3/4}\),

\[
\begin{aligned}
 \sum_{m\in\mathcal E_M(M^{3/4})}
 m^{-3/4}|C(m)|
 \left|V_{\rm low}(R^2m/N)\right|
 &\ll_\varepsilon
 M^{-3/4}(M^{3/4}+\sqrt M)N^\varepsilon\\
 &\ll_\varepsilon N^\varepsilon.
\end{aligned}
\tag{144.P28}
\]

There are \(O(\log N)\) disjoint dyadic blocks, which is absorbed into
\(N^\varepsilon\).  This proves the enlarged-window target
equivalence.  The exponent \(3/4\) is the endpoint delivered by this
count plus termwise divisor control; it is not a lower barrier for a
signed argument.

### 3.6 Capacity and downstream seam

The exact equivalence (144.P3) does not change the capacity ledger.
At \(y\asymp M^{-1}\), the pointwise estimate
\(\mathcal R_{\rm cone}\ll M\) is only an envelope, not a bound or
lower bound for its pairing with the square-root extraction kernel.
The lawful holomorphic Cauchy--Parseval capacity remains
\(M^{1/4+o(1)}\), hence \(R^{1/2+o(1)}\) at \(M\asymp R^2\); the
owner-complete reciprocal principal family has absolute normalized
capacity \(N^{1/4}=R\).  Widening the phase-value deletion from
\(\sqrt M\) to \(M^{3/4}\) does not exclude rational derivative arcs
or alter either number.

## 4. First doubtful or unproved step

There is no remaining doubtful seam in the equivalence of the
error-function correction and the four Appell terms, the mixed-shadow
normalization, the scalar \(\Gamma _0(4)\) multiplier, the \(1/4\)
infinity-cusp constant, or the Abel/heat identity.

The first unsupported inference is:

> convert (144.P16) into a uniform coefficient summation estimate for
> the literal square-root test while controlling both correction
> evaluations, or discard the corrections as nonholomorphic errors.

No primary theorem audited in the source report has the required
combination of coefficient, test, weight, direction, and completion
hypotheses.  The explicit mixed shadow does not repair this mismatch;
it confirms that \(\mathcal H\) is not being supplied as an ordinary
harmonic-Maass input.  The independent smooth character-Poisson formula
also does not close the estimate because it self-returns to the
Round-140 owner.

At the algebraic-mask seam, (144.P6)--(144.P28) are proved.  The first
unsupported next step would be to infer from
\(|k_m^2-Nm|>M^{3/4}\) any derivative separation, Appell-pole
separation, correction cancellation, or improved reciprocal
capacity.  None follows.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| error_function_versus_four_R_terms | **Pass.** The bijection (144.P18)--(144.P21) proves exact equality, including \(i/4\), all signs, modulus \(8\tau\), and no residual term. |
| mixed_shadow_normalization | **Pass.** Direct differentiation and the completed square give (144.P10) with \(i/(16\sqrt y)\) and the four odd classes modulo \(8\). |
| scalar_level_character_and_full_group_scope | **Pass.** The exact source elliptic shifts give weight one and \(\chi _4(d)\) on \(\Gamma _0(4)\); outside it, characteristic components move and the package is vector-valued. |
| cusp_constant_and_boundary | **Pass.** Infinity has the forced constant \(1/4\); slash constants at \(0,1/2\) vanish; (144.P15) has the exact \(i\chi _4(d)/(4cy)\) leading term. |
| heat_identity_direction_and_owners | **Pass algebraically.** Equation (144.P16) retains the \(+\) input, \(-d/c\) dual direction, constant terms, and both total corrections. |
| source_legal_coefficient_inference | **Fail at the estimate.** The Abel identity is not a general test theorem.  Harmonic-Maass and complete-divisor summation sources do not match, and the separate Round-63 formula self-returns. |
| gcd_averaged_displacement_count | **Pass.** Prime-power roots, the gcd average, the \(A=0\) squareful case, and the short \(k\)-interval prove (144.P6). |
| M_three_quarters_window | **Pass only algebraically.** Equation (144.P28) is target-safe globally, but supplies no slope or automorphic gain. |
| complex_direction_and_conjugate | **Pass as a prohibition.** No real part or cosine replaces the individual complex branch. |
| capacity_and_downstream_scope | **Pass/no-go.** The \(M^{1/4}\), top \(R^{1/2}\), and reciprocal \(R\) capacities remain owner ledgers, not signed bounds.  No downstream claim is made. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The seam review read in full:

* rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/blind_cone_automorphy_feasibility.md;
* rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_lattice_completion_attack.md;
* rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_source_hypothesis_audit.md.

The source normalization checked in the last report was used exactly:

* Bringmann--van Ittersum--Kaszian, equations (2.12)--(2.15),
  https://arxiv.org/abs/2401.02820;
* Semikhatov--Taormina--Tipunin, definition (1.1) and Theorem 1.1,
  https://arxiv.org/abs/math/0311314;
* Zwegers, Lemma 1.8 and the Chapter 2 isotropic-domain conditions,
  https://arxiv.org/abs/0807.4834.

The accepted Round-140--142 and Round-63 identities were used only
through the three reviewed reports.  No graph, campaign, synthesis,
validation, plan, proof draft, or shared-state file was edited.

## 7. Recommended state effect

**Promote after conductor review:** the exact identity
\(\mathcal R_{\rm cone}=\sum_{k=0}^3\mathcal R_k\), the mixed-shadow
factorization, scalar weight-one \(\Gamma _0(4)\) law with
\(\chi _4\), forced \(1/4\) infinity constant, zero constants at the
other two cusps, and the owner-complete Abel identity (144.P16).
These are structural/completion statements only.

**Promote as an algebraic reduction:** the uniform displacement lemma
(144.P6) and the resulting target-equivalence after enlarging the
deleted window to \(M^{3/4}\).  Record explicitly that it is global
over the original disjoint dyadic blocks and must precede any
correction, rational-mode, or Poisson-branch split.

**Revise or reject:** do not promote the claim that arbitrary smooth
transforms follow from the heat identity without a proved
superposition and uniform correction bounds; do not label the mixed
shadow an ordinary scalar harmonic-Maass shadow; and do not turn the
pointwise \(O(M)\) correction envelope into a coefficient estimate.

**Retain the no-go and all downstream open nodes:** neither completion
nor the \(M^{3/4}\) deletion proves the fixed-centre signed scalar.
Make no promotion for the collar-tail cross term, complete lower GAR,
either direct-M1 parent, M9--M1, any M2 owner, endpoint, M9, the
quarter exponent, or the global theorem.

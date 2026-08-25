# Round 132 statement-only packet

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

This packet is self-contained for the statement-only feasibility task. It
states the source inequality and the target scalar, but supplies no proposed
map and no claimant derivation.

## 1. Source theorem statement

The primary source is Ciprian Demeter and Shukun Wu, *Restriction and
decoupling estimates for the hyperbolic paraboloid in R^3*,
[arXiv:2505.09037v2](https://arxiv.org/abs/2505.09037), dated 14 April 2026.
Let

\[
 \mathbb H=\{(\xi,\eta,\xi\eta):(\xi,\eta)\in\mathbb R^2\}.
\]

For a rectangle \(\tau\subset[-1,1]^2\), write \(\mathbb H_\tau\) for
the corresponding surface patch and \(f_\tau\) for Fourier restriction in
the first two frequency coordinates.

Definition 1.2 calls two squares \(\tau_1,\tau_2\) transverse when, for
every \((\xi_j,\eta_j)\in\tau_j\),

\[
 |\xi_1-\xi_2|\asymp1,
 \qquad |\eta_1-\eta_2|\asymp1.                 \tag{132.S1}
\]

Thus separation in only one coordinate is not transverse. Equivalently, the
line between the two patches stays quantitatively transverse to both
coordinate directions; no line contained in \(\mathbb H\) meets both
patches.

For \(0<\delta<1\) and \(R\ge1\), Definition 1.3 lets
\(C(\delta,R)\) be the least constant such that, for transverse
\(\delta\)-squares \(\tau_1,\tau_2\), functions \(f_j\) with Fourier
support in \(N_{1/R}(\mathbb H_{\tau_j})\), and the partition into
\(R^{-1/2}\)-squares \(\theta_j\),

\[
 \int_{\mathbb R^3}|f_1f_2|^2
 \le C(\delta,R)
 \prod_{j=1}^2
 \left(\sum_{\theta_j}
       \|f_{\theta_j}\|_{L^4(\mathbb R^3)}^2\right).       \tag{132.S2}
\]

Theorem 1.6 states

\[
 C(1,R)\ll_\varepsilon R^\varepsilon.                       \tag{132.S3}
\]

The paper notes that Fourier support permits a localized version on a ball
of radius \(R\), with smooth spatial cutoff.

For refined decoupling, Definition 1.9 takes transverse squares
\(\tau_1,\tau_2\), a union \(X\) of pairwise disjoint
\(R^{1/2}\)-balls inside \(B_R\), and scale-\(R\) wave-packet sums
\(f_j=\sum_{T\in\mathbb T_j}f_T\) supported in
\(N_{1/R}(\mathbb H_{\tau_j})\). If every \(R^{1/2}\)-ball in \(X\)
meets at most \(M_j\) tubes from \(\mathbb T_j\), the defining inequality
is

\[
 \int_X|f_1f_2|^2
 \le C(R)(M_1M_2)^{1/2}
 \prod_{j=1}^2
 \left(\sum_{T\in\mathbb T_j}\|f_T\|_4^4\right)^{1/2}.
                                                               \tag{132.S4}
\]

Theorem 1.10 states \(C(R)\ll_\varepsilon R^\varepsilon\).
These are bilinear integral inequalities. The statement contains no theorem
about a single fixed-centre value of a signed arithmetic exponential sum.

## 2. Literal target scalar

Fix

\[
 W=Y^{7/16},\quad D=Y^{1/2},\quad L=Y^{1/6},\quad c\asymp Y.
                                                               \tag{132.S5}
\]

The outer and inner primitive rays satisfy
\(|a|,|a'|\asymp L\), \(b,b'\asymp D\), and

\[
 n=ab'-a'b>0,
 \qquad n\ll D^2/W=Y^{27/48}.                               \tag{132.S6}
\]

For \(i\in\{1,2\}\), put \(\kappa_1=1\), \(\kappa_2=4\). The centre
phase is

\[
 e\!\left(\frac{cn}{\kappa_i bb'}\right)
 =e\!\left(\frac{ca}{\kappa_i b}
            -\frac{ca'}{\kappa_i b'}\right).                \tag{132.S7}
\]

After physical Mobius and Stieltjes reassembly, the exact one-sided scalar
has the schematic but literal form

\[
 \mathfrak O_{i,D}^{+}(c)
 =\sum_{r=(a,b)}^{\rm lit} A_i(r)
   \sum_{n>0}^{\rm lit}\sum_{p\in\Lambda_{i,r}(n)}
   H_{i;r,p}(n)C_{i;r,p}(n)
   e\!\left(\frac{cn}{\kappa_i b b'_{r,p}(n)}\right).        \tag{132.S8}
\]

Here \(\#\Lambda_{i,r}(n)=O(1)\). The superscript `lit` retains all
primitive lift conditions, moving moduli, frequency floors, thresholds,
Stieltjes and Mobius signs, M1 quarter carriers or the M2 \(\chi_4\)
factor, reciprocal aliases, tapers, stars, cells, sign sectors, and half-open
owners. No modulus is inserted inside the physical coefficient.

The available outer data are

\[
 \sum_r|A_i(r)|\ll D Y^\varepsilon,
 \qquad \sum_r|A_i(r)|^2\ll (D/L)Y^\varepsilon.              \tag{132.S9}
\]

No sharper \(\ell^2\) norm for the fully reassembled inner coefficients in
(132.S8) is supplied.

Writing \(\Phi_i(u,v)=-cu/(\kappa_i v)\), one has

\[
 \det \nabla^2\Phi_i(u,v)
 =-\left(\frac{c}{\kappa_i v^2}\right)^2\asymp-1           \tag{132.S10}
\]

on \(u\asymp L\), \(v\asymp D\). This curvature identity alone does not
specify an affine normalization, a Fourier thickness, a physical radius
\(R\), or cap dimensions.

## 3. Capacity and hostile controls

The current complete fixed-block bound, ideal per-ray floor, and determinant
target are respectively

\[
 Y^{35/48+\varepsilon},\qquad
 Y^{27/48+\varepsilon}=Y^{9/16+\varepsilon},\qquad
 Y^{24/48+\varepsilon}.                                    \tag{132.S11}
\]

A strict improvement of the current global exponent requires a complete
bound strictly below \(27/48\). Even an ideal one-term-per-ray collapse
therefore needs a further cross-ray power; the determinant target needs
\(Y^{-1/16}\) beyond that floor.

The following controls are mandatory.

1. The source requires separation in both surface coordinates. A pair of
   patches separated in only one coordinate is a narrow/ruling pair.
2. The literal family contains legal same-denominator, nonzero-determinant
   M1 and M2 packets of length \(D/W\) on which the quarter or character
   carrier is coherent for one fixed outer ray. They refute automatic
   per-ray cancellation but are not lower bounds for the full scalar.
3. A bound for \(\int|f_1f_2|^2\), an \(L^4\) norm, or a positive square
   function is not a bound for the signed scalar (132.S8) at one prescribed
   value of \(c\) unless an explicit bridge, with its full localization
   cost, is proved.
4. Any broad estimate must be accompanied by a separately priced narrow
   term. Discarding aligned packets is not a broad--narrow decomposition.
5. Arbitrary phase-adapted coefficients are a false control: a proposed
   coefficient-uniform argument must not be credited with arithmetic sign
   cancellation absent from its hypotheses.
6. No result of this task changes a global exponent or any M9, endpoint,
   bridge, or quarter obligation.

The task is to derive the weakest legal implication of (132.S1)--(132.S4)
for (132.S8), or to identify the first exact missing hypothesis and quantify
its cost where the supplied data permit.


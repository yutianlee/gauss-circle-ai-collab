# Round 147 strategy: mandatory \(t=1\) squarefree cone

Starting graph SHA-256:
1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5.
This is a strategy report only; it makes no proof-state claim.

## 1. Result

The \(t=1\) face is an exact, mandatory, and materially cleaner next
interface. It is

\[
\mathfrak U_N^{(1)}
=\sum_{M:\,1<M^{1/4}}
 \sum_{\substack{s\in\mathcal I_M\\s\ {\rm squarefree}}}
s^{-3/4}V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns}),
\tag{147.1}
\]

where

\[
C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi_4(e).
\tag{147.2}
\]

The Round-146 nearest-square mask is absent. The strict cone, profile,
clipped half-open product blocks, fixed centre \(N=\lfloor X\rfloor\),
and individual positive complex direction remain literal.

The proposed Mellin identity is correct after one necessary \(2\)-adic
repair:

\[
Z(w,z)=\zeta(w+z)L(w-z,\chi_4)H(w,z),
\tag{147.3}
\]

with \(H\) absolutely convergent for \(\Re w>1/2\) when \(z\) is
imaginary, but

\[
H_2(w,z)=1-2^{-2w-2z},
\tag{147.4}
\]

not \(1\).

The proposed Voronoi opportunity is only partly valid. For the bare
\(\zeta L\) factor at fixed order, the conductor-four kernel has one
dual resonance near \(m=N\), not \(N/4\). At \(M\asymp R^2\) its width
is \(O(R)\) and its one-term amplitude is \(O(R^{-1})\), hence it is
target-sized. For the actual squarefree coefficient, expanding \(H\)
creates powerful-number indices \(k\) and a family

\[
m=kN+O(kR),\qquad \hbox{amplitude }O(R^{-1}k^{-1}).
\tag{147.5}
\]

Absolute aggregation costs one unit per \(k\) on the top block. This is
the first full power obstruction after granting uniform complex-order
Voronoi.

Recommendation: freeze Round 147 on the exact \(t=1\) face, but ask for
a signed theorem for the full \(H\)-family, an owner-complete top-scale
reduction, or a precise no-go. Applying ordinary generalized-divisor
Voronoi to the bare \(\zeta L\) model is not sufficient.

## 2. Exact statement and hypotheses

Let \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\leq2M\), with the inherited
disjoint terminal clipping and \(M\ll_VR^2\). A sufficient dyadic
target, uniform in every clipped product prefix, is

\[
\left|
\sum_{\substack{s\in\mathcal I'_M\\s\ {\rm squarefree}}}
V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})
\right|
\ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\tag{147.6}
\]

Partial summation then restores \(s^{-3/4}\).

Write \(s=2^\nu n\), \(\nu\in\{0,1\}\), with \(n\) odd squarefree.
Putting \(d=2^\nu a\) gives the multiplicity-one expansion

\[
\begin{aligned}
\mathfrak U_N^{(1)}
=\sum_M\sum_{\nu=0}^1
\sum_{\substack{a,e\geq1\ {\rm odd}\\
\mu^2(ae)=1\\e>2^{\nu+2}a\\
2^\nu ae\in\mathcal I_M}}
&(2^\nu ae)^{-3/4}V_{\rm low}(R^2 2^\nu ae/N)\\
&\times\chi_4(e)e(+\sqrt{2^\nu Nae}).
\end{aligned}
\tag{147.7}
\]

Here \(\mu^2(ae)=1\) says that \(a,e\) are squarefree and coprime. If
the prime \(2\) occurs, it is forced into \(d\). No cosine, centre
average, arbitrary-coefficient estimate, or unsigned bound substitutes
for (147.6). The accepted exact-radical owner may be invoked explicitly,
but not silently.

## 3. Proof and maximal simplification of \(C(s)\)

Put

\[
c_\nu=2^{1+\nu/2},\qquad
A_\nu(n)=C(2^\nu n).
\]

The cone in (147.2) is equivalent to \(e^2>2^{\nu+2}n\), so

\[
\boxed{A_\nu(n)=
\sum_{\substack{e\mid n\\e>c_\nu\sqrt n}}\chi_4(e).}
\tag{147.8}
\]

Define

\[
B_\nu(n)=
\sum_{\substack{e\mid n\\
c_\nu^{-1}\sqrt n<e<c_\nu\sqrt n}}\chi_4(e),
\qquad
\sigma_{\chi_4}(n)=\sum_{e\mid n}\chi_4(e).
\tag{147.9}
\]

No divisor lies on either boundary because \(e^2\) is odd whereas
\(2^{\nu+2}n\) is even. Pairing \(e\) with \(n/e\), and using
\(\chi_4(n/e)=\chi_4(n)\chi_4(e)\), gives

\[
\boxed{\sigma_{\chi_4}(n)
=(1+\chi_4(n))A_\nu(n)+B_\nu(n).}
\tag{147.10}
\]

A sign-retaining equivalent formula is

\[
\boxed{
A_\nu(n)=\frac12\sum_{e\mid n}\chi_4(e)
\left(
\mathbf1_{e>c_\nu\sqrt n}
+\chi_4(n)\mathbf1_{e<c_\nu^{-1}\sqrt n}
\right).}
\tag{147.11}
\]

Thus:

1. If \(s\) is odd and \(\chi_4(s)=+1\), then
   \[
   C(s)=\frac{r_2(s)}8-\frac12B_0(s).
   \tag{147.12}
   \]
   If \(s\) contains an even positive number of primes \(3\bmod4\),
   then \(r_2(s)=0\), so the central band remains compulsory.
2. If \(s\) is odd and \(\chi_4(s)=-1\), then
   \(\sigma_{\chi_4}(s)=B_0(s)=0\), but \(C(s)\) survives as the exact
   antisymmetric tail
   \[
   C(s)=\frac12\left(
   \sum_{\substack{e\mid s\\e>2\sqrt s}}\chi_4(e)
   -\sum_{\substack{e\mid s\\e<\sqrt s/2}}\chi_4(e)\right).
   \tag{147.13}
   \]
   In particular \(C(p)=\chi_4(p)=-1\) for
   \(p\equiv3\bmod4\), \(p>4\).
3. If \(s=2n\) is even, then \(\chi_4(s)=0\), and the relevant sign is
   \(\chi_4(n)\). For \(\chi_4(n)=+1\),
   \[
   C(2n)=\frac{r_2(2n)}8-\frac12B_1(n),
   \tag{147.14}
   \]
   while for \(\chi_4(n)=-1\) the two tails in (147.13) are replaced
   by \(e>2\sqrt{2n}\) and \(e<\sqrt n/(2\sqrt2)\).
   The control \(C(2p)=\chi_4(p)\) holds for odd primes \(p>8\).
4. \(C(1)=C(2)=0\); the divisor \(1\) is central.

This is maximal under divisor pairing: the positive sector introduces a
complete coefficient and a central band, while the negative sector is
invisible to the complete coefficient but retains an antisymmetric far
tail.

## 4. Sign-sensitive route and \(R,M,D,E\) power ledger

Before inserting the cone, define

\[
\begin{aligned}
Z(w,z)
&=\sum_{\substack{d,e\geq1\\e\ {\rm odd}\\\mu^2(de)=1}}
\frac{\chi_4(e)}{d^{w+z}e^{w-z}}\\
&=(1+2^{-w-z})
\prod_{p\ {\rm odd}}
\left(1+p^{-w-z}+\chi_4(p)p^{-w+z}\right).
\end{aligned}
\tag{147.15}
\]

At an odd prime let \(x=p^{-w-z}\) and
\(y=\chi_4(p)p^{-w+z}\). Direct multiplication gives

\[
H_p=(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2.
\tag{147.16}
\]

Together with (147.4), this proves (147.3). If \(z=i\tau\) and
\(\sigma=\Re w>1/2\), then \(H_p=1+O(p^{-2\sigma})\), uniformly in
\(\tau\).

More precisely,

\[
H_p=1+A_p(z)p^{-2w}+B_p(z)p^{-3w},
\tag{147.17}
\]

where

\[
A_p(z)=-(p^{-2z}+p^{2z}+\chi_4(p)),\qquad
B_p(z)=\chi_4(p)p^{-z}+p^z.
\]

Hence the Dirichlet coefficients \(h_z(k)\) of \(H\) are supported on
powerful integers and satisfy
\(|h_{i\tau}(k)|\ll_\varepsilon k^\varepsilon\).

The hard cone is not a bounded-height Mellin factor. Although

\[
\mathbf1_{e>4d}
=\lim_{T\to\infty}\frac1{2\pi i}
\int_{\eta-iT}^{\eta+iT}
\left(\frac e{4d}\right)^z\frac{dz}{z},
\tag{147.18}
\]

the nearest odd \(e\) can have \(|e-4d|=1\), so a pointwise truncation
on \(d\asymp D\) needs \(T\gg D\). There is an owner-complete repair.
Only \(E\asymp D\) boxes meet the boundary, where \(M\asymp D^2\).
A collar \(|e-4d|\leq L\) contains \(O(D(L+1))\) pairs and costs

\[
M^{-3/4}D(L+1)\ll (L+1)D^{-1/2}.
\tag{147.19}
\]

Taking \(L\asymp\sqrt D\) is target-safe, and the smoothed ratio
transform is effectively restricted to
\(|\Im z|\lesssim D^{1/2}X^\varepsilon\). Uniform complex-order
Voronoi remains necessary.

On a \(t=1\) box,

\[
DE\asymp M,\qquad D\ll\sqrt M,\qquad E\gg\sqrt M.
\tag{147.20}
\]

There are \(O(M)\) incidences, the weight is \(M^{-3/4}\), and the raw
target is \(M^{3/4}\); the required saving is \(M^{1/4}\). Writing

\[
M=R^\mu,\quad D=R^\delta,\quad E=R^{\mu-\delta},
\quad0\leq\mu\leq2,\quad0\leq\delta\leq\mu/2,
\]

gives

\[
F=\sqrt{NM}=R^{2+\mu/2},\qquad
\#\mathcal B\asymp R^\mu,\qquad
\hbox{raw target }R^{3\mu/4}.
\tag{147.21}
\]

In the smooth character-Poisson model, transforming \(e\) gives an odd
dual length

\[
Q\asymp F/E=D\sqrt{N/M}=R^{2-\mu/2+\delta}
\tag{147.22}
\]

and reciprocal phase \(e(Nd/q)\). After the physical weight, the dual
sum must satisfy

\[
|\mathcal T_{D,Q}|\ll RD\,X^\varepsilon.
\tag{147.23}
\]

Since \(Q\leq R^2\), square-root cancellation in the actual
\(\chi_4(q)\)-weighted \(q\)-sum would suffice:
\(DQ^{1/2}\leq RD\). This is genuinely sign-sensitive; no such theorem
is presently owned for the transformed squarefree coefficient.

For the bare generalized-divisor factor, the conductor-four kernel has
argument \(4\pi\sqrt{mx/4}=2\pi\sqrt{mx}\). Its opposite branch
therefore resonates at

\[
m=N,\qquad |m-N|\ll\sqrt{N/M},
\tag{147.24}
\]

not at \(N/4\). The weighted amplitude per term is
\(N^{-1/4}=R^{-1}\), so the optimistic fixed-order dual price is

\[
\frac R{\sqrt M}.
\tag{147.25}
\]

At \(M\asymp R^2\) this is target-sized. Across all \(M\), the best
bare-model ledger is

\[
\min(M^{1/4},R/\sqrt M),
\tag{147.26}
\]

which peaks at \(M=R^{4/3}\) with value \(R^{1/3}\). Thus even the ideal
model closes only the top scale and does not improve the global
\(1/3\) barrier.

For the actual coefficient, write
\(H(w,z)=\sum_kh_z(k)k^{-w}\). The \(k\)-term has original length
\(M/k\), phase parameter \(Nk\), and transformed window

\[
m=kN+O(k\sqrt{N/M}),
\qquad\hbox{weighted amplitude }R^{-1}k^{-1}.
\tag{147.27}
\]

Its absolute resonant price is
\(|h_z(k)|R/\sqrt M\). At the top this is \(|h_z(k)|\). Absolute
convergence of \(H\) for \(\Re w>1/2\) does not make
\(\sum_k|h_z(k)|\) finite.

Powerful support gives

\[
\sum_{\substack{k\geq K\\k\ {\rm powerful}}}
\frac{|h_z(k)|}{k}\ll_\varepsilon K^{-1/2+\varepsilon}.
\tag{147.28}
\]

Thus the primal \(k\geq K\) tail costs
\(M^{1/4+\varepsilon}K^{-1/2}\). At \(M=R^2\), choosing \(K=R\)
makes this tail target-safe, but the remaining \(k\leq R\) contain
\(O(R^{1/2+\varepsilon})\) powerful indices and lose that full factor
under triangle inequality.

## 5. First doubtful or unproved step

The first literal source seam is a prefix-safe generalized-divisor
Voronoi formula uniform for

\[
|\Im z|\lesssim D^{1/2}X^\varepsilon,
\]

including all \(J,Y,K\) branches, polar terms, gamma normalizations,
cone-collar errors, and product endpoints. The audited Banerjee--Khurana
result is a fixed-parameter identity and does not state the required
large-imaginary-order bound. This unresolved source point must be the
first doubtful step in a Round-147 proof attempt.

Even granting that seam, the first full power obstruction is the
powerful-index family. The required top-scale signed estimate has the
schematic form

\[
R^{-1}
\sum_{\substack{k\leq R\\k\ {\rm powerful}}}
\frac{h_{i\tau}(k)}k
\sum_{|m-kN|\ll kR}
a_{-i\tau}(m)\,
\mathcal W_{k,\tau}\left(\frac{m-kN}{kR}\right)
\ll_\varepsilon R^\varepsilon,
\tag{147.29}
\]

uniformly in the allowed \(\tau\), profiles, and prefixes. Here
\(a_{-i\tau}\) is the reflected generalized-divisor coefficient.
Triangle inequality gives \(R^{1/2+\varepsilon}\). No result in
Rounds 141--146 proves or refutes (147.29).

This route bypasses those no-go results only if it proves (147.29), or
an equivalent exact signed correlation. Replacing \(H\) by \(1\),
using fixed-order Voronoi under a growing ratio integral, bounding each
window absolutely, or applying a second self-return transform does not
qualify.

## 6. Required controls, outcomes, and dependencies

Control outcomes:

1. Exact \(t=1\) coefficient, parity, coprimality, cone, and
   multiplicity: PASS by (147.7)--(147.8).
2. Odd/even and \(\chi_4\) cases: PASS by
   (147.10)--(147.14); the negative sector survives.
3. Euler product: PASS after repairing the compulsory factor (147.4).
4. Absolute convergence of \(H\): PASS for \(\Re w>1/2\) and imaginary
   \(z\).
5. Hard Perron truncation: FAIL without repair; PASS only after the
   target-safe \(\sqrt D\)-collar reduction.
6. Single resonance near \(N/4\): REJECTED. The bare centre is \(N\);
   the actual coefficient has the family (147.27).
7. Bare top-block power: PASS as a model only. The actual \(H\)-family
   and growing-order transform remain open.
8. All-scale target: FAILS for the displayed capacity/Voronoi menu;
   (147.26) retains the \(R^{1/3}\) intermediate-scale barrier.
9. Fixed centre, positive direction, exceptional slow-frequency
   control, and downstream scope: retained. No signed lower bound or
   exponent claim is made.

Exact artifacts used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- the Round-145 squarefree-kernel conductor candidate;
- the Round-146 synthesis, conductor candidate, adjudication, and
  controls;
- the Round-141 cone nonresonant conductor candidate;
- the Round-144 indefinite-theta synthesis;
- the Round-15 Mellin synthesis and hostile Voronoi source audit;
- sources/banerjee_khurana_2023.md.

No numerical experiment or new web search was used.

## 7. Recommended state effect

This memo recommends no immediate graph mutation. Round 147 should freeze
the exact \(t=1\) squarefree cone with the objective:

> Prove the full \(t=1\) target, prove an owner-complete target-safe
> top-scale range by a uniform character-sensitive Voronoi transform
> retaining \(H\), or identify the first exact complex-order,
> powerful-index correlation, polar, boundary, or power obstruction.

The round should use three orthogonal tasks:

1. blind coefficient and Euler-product rederivation, including \(p=2\);
2. uniform complex-order Voronoi/stationary analysis with an independent
   check of the centre and the family (147.27);
3. hostile source and power audit of the collar, Perron height, polar
   terms, powerful tail, all \(M,D,E\) aspects, and the
   \(M=R^{4/3}\) barrier.

Suitable terminal labels are
\(\mathsf{t1\_target\_bound}\),
\(\mathsf{strict\_top\_t1\_voronoi\_reduction}\), and
\(\mathsf{squarefree\_H\_resonance\_no\_go}\).

Promotion must require the exact transformed coefficient and signed
aggregation, not the bare \(\zeta L\) model. Even success on the top
\(t=1\) block leaves lower \(t=1\) scales, every \(t\geq2\) layer, the
independent Round-138 cross owner, and all downstream M1, M2, endpoint,
M9, bridge, and exponent obligations open.

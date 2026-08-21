# Conductor candidate: exact moving-block second moment and almost-all corollary

This is candidate evidence pending the Round-93 moving-coefficient and hostile gates.

## 1. Fixed partition on a moving interval

Fix \(Y\geq 2\), put \(D_j=2^{-j}\sqrt Y\), and let

\[
 W(u)=\eta(u)-\eta(2u),
\]

where the accepted profile has \(0\leq W\leq1\), support in
\([1/2,4/3]\), and bounded variation. Choose \(J\) maximal with
\(D_J\geq(2Y)^{1/4}\). Since \(d/(2\sqrt Y)\leq1/\sqrt2<1\) whenever
\(d\leq\sqrt t\) and \(Y\leq t\leq2Y\), the telescoping identity gives

\[
 \mathbf1_{d\leq\sqrt t}
 =\mathbf1_{d\leq\sqrt t}
  \left\{\sum_{j=0}^{J}W(d/(2D_j))+\eta(d/(2D_{J+1}))\right\}.
 \tag{1.1}
\]

The last term is supported on \(d\ll Y^{1/4}\) and is therefore handled
before Fourier expansion. All active denominator profiles \(W(d/(2D_j))\)
are fixed as \(t\) varies; the only moving denominator datum is the exact
prefix \(d\leq\lfloor\sqrt t\rfloor\).

For one active scale \(D=D_j\), set

\[
 H_D(t)=\lfloor Dt^{-1/4}\rfloor.
 \tag{1.2}
\]

Our choice \(D\geq(2Y)^{1/4}\) ensures \(H_D(t)\geq1\) throughout
\([Y,2Y]\). Applying Vaaler's identity separately after the exact fixed
partition (1.1) is legitimate: the approximation order is allowed to
depend on the fixed block \(D\) and on \(t\).

## 2. Frozen separated-frequency lemma

Let

\[
 F(t)=\sum_{\lambda\in\Lambda}c_\lambda e(\lambda t),
 \qquad |\lambda-\lambda'|\geq\delta\quad(\lambda\ne\lambda').
\]

The triangular-kernel proof gives, on any interval \(I\) of length \(V\),

\[
 \int_I|F(t)|^2dt
 \ll (V+\delta^{-1})\sum_{\lambda}|c_\lambda|^2.
 \tag{2.1}
\]

For the frozen M2 block, reduce \(h/d=a/b\). Distinct frequencies
\(a/(4b)\) are \(\gg D^{-2}\)-separated and the exact equality-class
coefficient satisfies

\[
 |A_{a,b}|\ll |a|^{-1},
 \qquad
 \sum_{a,b}|A_{a,b}|^2\ll D.
 \tag{2.2}
\]

Therefore

\[
 \int_I|S_{D,H,w}(t)|^2dt\ll(V+D^2)D.
 \tag{2.3}
\]

Both frequency signs and the exact \(\chi_4(h)\) factor remain inside the
equality-class coefficient. The same lemma holds for M1: its spatial
\(\chi_4(d)\) has modulus one and its frequencies \(h/d\) have the same
separation.

## 3. Exact height increments and a maximal-prefix lemma

Extend the M2 coefficient \(\beta_{h,r}\) by zero for \(|h|>r\), set
\(\beta_{h,0}=0\), and define

\[
 \gamma_{h,r}=\beta_{h,r}-\beta_{h,r-1}.
\]

The explicit \(C^1\) Vaaler profile, including \(\Phi(1)=0\), gives

\[
 |\gamma_{h,r}|\ll r^{-2}\mathbf1_{0<|h|\leq r}.
 \tag{3.1}
\]

For \(|h|\leq r-1\), the two profile arguments differ by
\(|h|/[r(r+1)]\), which cancels the outside \(1/|h|\). For \(|h|=r\),
\(\Phi(r/(r+1))\ll r^{-1}\). This also covers \(r=1\) after enlarging the
absolute constant. Exactly,

\[
 \beta_{h,H_D(t)}
 =\sum_{r\geq1}\gamma_{h,r}
   \mathbf1_{t\leq(D/r)^4}.
 \tag{3.2}
\]

Fix \(r\), and restrict the denominator to any interval
\(\mathcal J\) containing \(N\) integers in the fixed \(D\)-shell. After
grouping equal reduced frequencies, Cauchy's inequality within each class
and the fact that a class has at most \(r\) representatives give

\[
 \sum_{a,b}|A^{(r,\mathcal J)}_{a,b}|^2
 \leq r\sum_{0<|h|\leq r}\sum_{d\in\mathcal J}|\gamma_{h,r}|^2
 \ll \frac{N}{r^2}.
 \tag{3.3}
\]

Let \(F_{r,n}(t)\) be the corresponding sum over the prefix \(d\leq n\)
of the ordered denominator shell. A prefix is a disjoint union of at most
one canonical dyadic interval at each of \(O(\log(2D))\) tree levels.
Pointwise Cauchy followed by (2.1), summed over all tree nodes, gives the
maximal estimate

\[
 \int_{I'}\max_n|F_{r,n}(t)|^2dt
 \ll (\log(2D))^2(V'+D^2)\frac{D}{r^2}
 \tag{3.4}
\]

for every interval \(I'\) of length \(V'\). At each tree level the nodes
partition the denominator shell, so (3.3) sums to \(O(D/r^2)\); there is no
factor equal to the number of prefixes.

Apply (3.4) on

\[
 I'_r=[Y,2Y]\cap(-\infty,(D/r)^4].
\]

Since \(d\leq\lfloor\sqrt t\rfloor\) is exactly the prefix condition
\(d^2\leq t\), (3.2), Minkowski's inequality, and
\(\sum_{r\leq D Y^{-1/4}}r^{-1}\ll\log(2Y)\) prove

\[
 \boxed{
 \int_Y^{2Y}|S_{2,D}^{\mathrm{mov}}(t)|^2dt
 \ll_\varepsilon Y^\varepsilon(Y+D^2)D.}
 \tag{3.5}
\]

Only logarithms are suppressed. The M1 coefficient has the same increment
bound, and multiplication by \(\chi_4(d)\) does not change (3.3), so

\[
 \boxed{
 \int_Y^{2Y}|S_{1,D}^{\mathrm{mov}}(t)|^2dt
 \ll_\varepsilon Y^\varepsilon(Y+D^2)D.}
 \tag{3.6}
\]

No moving smooth factor is needed: the fixed partition (1.1) leaves only
the literal hard prefix.

## 4. Exceptional set and exact assembly

Every active \(D\ll\sqrt Y\), so (3.5)--(3.6) are
\(O_\varepsilon(Y^{1+\varepsilon}D)\). For fixed \(\eta>0\), Chebyshev gives

\[
 \left|\left\{t\in[Y,2Y]:
 |S_{i,D}^{\mathrm{mov}}(t)|>Y^{1/4+\eta}\right\}\right|
 \ll_\varepsilon D Y^{1/2-2\eta+\varepsilon},
 \qquad i\in\{1,2\}.
 \tag{4.1}
\]

The active \(D\)'s form a geometric family with
\(\sum_D D\ll\sqrt Y\). Hence the union over both main sums and all fixed
blocks has measure

\[
 |\mathcal E_Y(\eta)|
 \ll_\varepsilon Y^{1-2\eta+\varepsilon}.
 \tag{4.2}
\]

Outside this set, the blockwise main sums total
\(O_\varepsilon(Y^{1/4+\eta+\varepsilon})\). The bottom term in (1.1)
costs \(O(Y^{1/4})\) before Fourier expansion. The accepted pointwise
Fejer product-count argument applies to every fixed-shell bounded profile
with the literal prefix and \(H_D(t)\asymp Dt^{-1/4}\), and its dyadic sum
is \(O_\varepsilon(Y^{1/4+\varepsilon})\). Moreover,
\(\sum_D\sqrt D\ll Y^{1/4}\), so Minkowski and (3.5)--(3.6) give

\[
 \left\|\sum_D
 (S_{1,D}^{\mathrm{mov}}+S_{2,D}^{\mathrm{mov}})
 \right\|_{L^2[Y,2Y]}
 \ll_\varepsilon Y^{3/4+\varepsilon}.
\]

Inserting the accepted exact sawtooth identity therefore proves the
candidate global moment

\[
 \boxed{
 \int_Y^{2Y}|P(t)|^2\,dt
 \ll_\varepsilon Y^{3/2+\varepsilon}.}
 \tag{4.3}
\]

Chebyshev gives the candidate almost-all theorem

\[
 \boxed{
 \left|\left\{t\in[Y,2Y]:
 |P(t)|>Y^{1/4+\eta+\varepsilon}\right\}\right|
 \ll_\varepsilon Y^{1-2\eta+\varepsilon}.}
 \tag{4.4}
\]

For every fixed \(\eta>0\), choosing the displayed \(\varepsilon<2\eta\)
makes this a density-one statement for real \(t\).

## 5. Sharpness and controls

For the actual Vaaler profile,

\[
 |\beta_{1,H}|\geq\frac1{2\pi}.
\]

On a fixed full shell with nontrivial denominator \(\ell^2\)-mass, the
primitive \(h=\pm1\) frequencies in the no-multiplicity top zone already
give coefficient mass \(\gg D\). Thus the \(VD\) diagonal scale in (2.3)
is sharp for the actual coefficient class. At threshold \(Y^{1/4}\) and
\(D\asymp\sqrt Y\), a second moment alone gives no exceptional-measure
saving.

The moving proof retains:

- both signs and the exact frequency or spatial character;
- every height floor, including \(r=1\);
- the hard endpoint \(d=\lfloor\sqrt t\rfloor\) with no half-weight;
- partial denominator shells and every equality-class multiplicity;
- only polylogarithmic maximal-prefix and height-telescope costs.

The theorem concerns the original moving main blocks, not the transformed
Round-92 top-cone density--discrepancy energy. It neither estimates that
canonical energy nor supplies a pointwise bound.

## 6. First unproved gate

The analytic proof of (3.5)--(3.6) is complete once the accepted \(C^1\)
Vaaler profile and fixed partition are admitted. Before state promotion,
the hostile gate must verify the exact assembly claim in Section 4:

1. the fixed-in-\(Y\) partition (1.1) may replace the historical
   \(t\)-anchored partition without changing the exact sawtooth owners;
2. the accepted pointwise Fejer proof applies to these fixed shells with a
   moving hard prefix;
3. all constants, signs, and bottom terms in the H1--H4 assembly are
   retained.

Failure of one of these is an assembly seam, not a failure of the moving
second-moment theorem itself.

## 7. Scope

Even if every gate passes, (4.4) is an almost-everywhere theorem in the
real variable \(t\). It does not imply a bound at every real \(t\), at
integer \(t\), or at circle-problem jump points. It therefore does not
promote `M9-M1`, `M9-M2`, `M9-endpoint-uniformity`, `M9`, or `GC-target`,
and it does not improve the accepted uniform exponent \(1/3\).

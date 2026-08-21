# Conductor candidate: persistence, discrete sampling, and the local bridge

## 1. Exact one-sided persistence

Since \(N(\sqrt t)\) is nondecreasing, for \(u\ge0\),

\[
 P(x+u)\ge P(x)-\pi u.
\]

Also

\[
 P(x-u)=P(x)-\{N(\sqrt x)-N(\sqrt{x-u})\}+\pi u
 \le P(x)+\pi u.
\]

Thus a positive value persists to the right and a negative value persists
to the left.  If \(M=|P(x)|\ge2\pi H\), then \(|P|\ge M/2\) throughout a
favorable adjacent interval of length \(H\).  The inclusive jump convention
causes no sign reversal because every jump of \(N\) is nonnegative.

## 2. Quantitative local-moment implication

Suppose every interval \(I\subset[Y/2,3Y]\) of length \(H\) satisfies

\[
 \int_I|P(t)|^2\,dt
 \ll HY^{1/2+\varepsilon}+E(Y,H).
\]

Let \(Q=HY^{1/2+\varepsilon}+E(Y,H)\).  Persistence on a segment of
length \(\min(H,M/(2\pi))\) gives

\[
 {M^2\over4}\min\!\left(H,{M\over2\pi}\right)\le Q.
\]

Consequently

\[
 M\ll Q^{1/3}+(Q/H)^{1/2}
 \ll H^{1/3}Y^{1/6+\varepsilon/3}
 +Y^{1/4+\varepsilon/2}
 +E(Y,H)^{1/3}
 +\left({E(Y,H)\over H}\right)^{1/2}.
 \tag{94.C1}
\]

In particular, the expected local mean square with
\(H=Y^{1/4+o(1)}\) proves the uniform quarter exponent.  At fixed
\(H=Y^{1/4+\sigma}\) it yields
\(Y^{1/4+\sigma/3+o(1)}\); a strict quarter conclusion on that longer
window requires the stronger total bound \(Q\ll Y^{3/4+o(1)}\).  At
\(H=1\), the
same persistence shows that a uniform unit-window \(L^2\) bound is
equivalent, up to constants and an \(O(1)\) term, to the pointwise bound.
By contrast, the accepted fallback gives only
\(Q\ll HY^{2/3+\varepsilon}\); inserting this in (94.C1) returns exactly
the exponent \(1/3\) for every \(H\le Y^{1/3}\).  There is no automatic
bootstrap.

## 3. One-separated sampling

For integers there is a stronger exact identity.  On
\(t\in[n,n+1)\), the counting function is constant and

\[
 P(t)=P(n)-\pi(t-n).
\]

Therefore

\[
 \int_n^{n+1}|P(t)|^2\,dt
 =P(n)^2-\pi P(n)+{\pi^2\over3}
 =\left(P(n)-{\pi\over2}\right)^2+{\pi^2\over12}.
 \tag{94.C2}
\]

Thus the integer sampling theorem follows directly by summing exact unit
cells.  It also shows that uniform unit-cell \(L^2\) and the pointwise
integer theorem are literally equivalent up to an absolute additive
constant; every real \(t\) is then within one linear cell of an integer.

For each \(x\) in a one-separated set, orient a unit interval toward the
favorable persistence side.  These intervals have bounded overlap.  When
\(|P(x)|\ge2\pi\), their integrals are \(\gg|P(x)|^2\); smaller samples
contribute only \(O(\#\mathcal X)\).  The Round-93 moment on a constant
number of comparable dyadic intervals therefore yields

\[
 \sum_{x\in\mathcal X}|P(x)|^2
 \ll_\varepsilon Y^{3/2+\varepsilon}.
 \tag{94.C3}
\]

Taking \(\mathcal X=[Y,2Y]\cap\mathbb Z\) proves the integer exceptional
count (94.7).  This is a new discrete density-one consequence, not a
uniform integer theorem.

## 4. First analytic obstruction

The global moment does not localize.  On the natural target window
\(H=Y^{1/4+\sigma}\), the separated-frequency error at
\(D\asymp Y^{1/2}\) is \(Y^{3/2}\), while (94.C1) needs an additive error
at most \(Y^{3/4+\sigma+o(1)}\).  The missing statement is therefore an
actual-coefficient signed rational-frequency cluster estimate, not another
Chebyshev or persistence argument.

## 5. Candidate state effect

Promote (94.C2) and the integer exceptional-set theorem after blind and
hostile gates.  Record the local-moment implication and unit-window
equivalence as a bridge/no-go lemma.  Do not promote endpoint uniformity,
M9-M1, M9-M2, M9, or the uniform exponent unless the signed cluster bound
is actually proved.

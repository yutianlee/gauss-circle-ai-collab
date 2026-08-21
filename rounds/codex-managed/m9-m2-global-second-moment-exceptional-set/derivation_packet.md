# Round 93 statement-only packet: frozen M2 moment and exceptional set

This packet is self-contained.  It states one candidate theorem and its
exact transfer question.  It does not assert that the candidate is proved.

## 1. Frozen actual coefficient

Let \(Y\ge2\), let \(I\subset\mathbb R\) be an interval of length \(V\),
and let \(1\le H\le D\).  Let
\(\mathscr D_D\subset[c_0D,c_1D]\cap\mathbb Z_{>0}\), where
\(0<c_0<c_1<\infty\) are fixed, and let \(|w_D(d)|\le1\).

For \(0<|h|\le H\), define the exact frozen M2 coefficient

\[
 \beta_{h,H}=-{\Phi(|h|/(H+1))\over\pi|h|}
 \chi_4(|h|)\mathbf1_{2\nmid h},
\]

and put \(\beta_{h,H}=0\) otherwise.  Here \(0\le\Phi\le1\), so
\(|\beta_{h,H}|\le(\pi|h|)^{-1}\).  The coefficient is real and even;
the \(\chi_4\) sign is part of it and must not be erased from the exact
expansion.

Define the frozen block

\[
 S_{D,H,w}(t)=\sum_{0<|h|\le H}\beta_{h,H}
 \sum_{d\in\mathscr D_D}w_D(d)e\!\left({ht\over4d}\right).
 \tag{93.1}
\]

The word *frozen* means that \(H,\beta_{h,H},\mathscr D_D,w_D\) do not
change with \(t\in I\).  They may be chosen to equal the literal M2 data at
one reference point \(X_0\asymp Y\).

## 2. Candidate global second moment

The candidate theorem is

\[
 \boxed{
 \int_I|S_{D,H,w}(t)|^2\,dt
 \ll (V+D^2)D.
 }
 \tag{93.2}
\]

The constant may depend on \(c_0,c_1\), but not on \(Y,V,D,H\) or the
particular bounded weight.  Logarithms may be absorbed into \(Y^\varepsilon\)
in a project statement.

For \(I=[Y,2Y]\) and \(D\le Y^{1/2}\), (93.2) becomes

\[
 \int_Y^{2Y}|S_{D,H,w}(t)|^2\,dt\ll YD.
 \tag{93.3}
\]

## 3. Proposed elementary proof interface

Group all pairs \((h,d)\) by the reduced rational \(h/d=a/b\), with
\((a,b)=1\) and \(b>0\).  Write

\[
 A_{a,b}=\sum_{\substack{k\ge1:\,ka\ne0,\ |ka|\le H\\
                         kb\in\mathscr D_D}}
          \beta_{ka,H}w_D(kb).
 \tag{93.4}
\]

Then

\[
 S_{D,H,w}(t)=\sum_{a,b}A_{a,b}e\!\left({at\over4b}\right).
 \tag{93.5}
\]

Because \(kb\asymp D\), the \(k\)-sum lies in a fixed-ratio interval and

\[
 |A_{a,b}|\ll {1\over|a|},
 \qquad
 \sum_{a,b}|A_{a,b}|^2\ll D.
 \tag{93.6}
\]

Distinct reduced frequencies \(a/(4b)\) have spacing
\(\gg D^{-2}\).  A continuous separated-frequency large-sieve/Hilbert
inequality would therefore give (93.2).  A report must either prove that
inequality inside the report or cite and audit an exact primary theorem.

## 4. Exceptional-set consequence

For \(\eta>0\), define

\[
 \mathcal B_{D,H,w}(Y;\eta)
 =\{t\in[Y,2Y]:|S_{D,H,w}(t)|>Y^{1/4+\eta}\}.
\]

Chebyshev and (93.3) would give

\[
 |\mathcal B_{D,H,w}(Y;\eta)|
 \ll D Y^{1/2-2\eta}.
 \tag{93.7}
\]

For a fixed family of \(O(\log Y)\) dyadic blocks with
\(\sum_D D\ll Y^{1/2}\), the union would have measure

\[
 \ll Y^{1-2\eta+\varepsilon}.
 \tag{93.8}
\]

This is a density-one frozen-coefficient statement.  At \(\eta=0\) and
\(D\asymp Y^{1/2}\), it has no measure saving.

## 5. Sharpness and transfer seam

The diagonal size \(YD\) is expected to be sharp for a full actual shell:
the \(h=1\), \(d>D\) reduced fractions already give \(\gg D\) coefficient
\(\ell^2\)-mass when the weight has nontrivial \(\ell^2\)-mass.

The candidate does **not** by itself control the moving block in which

\[
 H=\lfloor Dt^{-1/4}\rfloor,
 \qquad \beta_{h,H}=\beta_{h,H(t)},
\]

and the top denominator support or profile may also move with \(t\).  A
valid transfer must prove a variable-amplitude large sieve, a bounded-basis
decomposition with no fatal multiplicity, or an exact freeze/unsmoothing
lemma.  Applying (93.2) separately to every floor interval can lose a power
at \(D\asymp Y^{1/2}\).

## 6. Required decisions

The round must decide all of the following.

1. Is (93.2) correct with the exact two-sided \(\chi_4\) coefficient?
2. Is the coefficient \(\ell^2\) bound (93.6) exact at every support edge?
3. What is the sharp exceptional-set statement, including an all-dyadic
   union?
4. Can the actual moving Vaaler height and top profile be included at the
   same power, or what is the first exact unsmoothing loss?
5. Does the theorem touch either Round-92 canonical hard core, or is it only
   a frozen global-moment deliverable?
6. Why does it not imply pointwise M9-M2, endpoint uniformity, M9, or the
   one-quarter theorem?

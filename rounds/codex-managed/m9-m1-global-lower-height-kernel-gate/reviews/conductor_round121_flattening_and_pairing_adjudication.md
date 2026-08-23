# Round 121 conductor adjudication: lower profile flattening and pairing gate

Campaign: `m9-m1-global-lower-height-kernel-gate`

Starting graph SHA-256:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

## 1. Decision

Round 121 proves a new target-scale equivalence for the complete lower
radial owner, but it does not prove that owner.  After two repairs, the
literal floor-perturbed profile sum may be replaced at cost
\(O_\varepsilon(RX^\varepsilon)\) by one flat sharp denominator cone;
the real phase may then be integerized at cost \(O(R)\); and the resulting
cone has an exact sharp truncated-character divisor-discrepancy
representation.

The same round proves that adjacent mod-four pairing is not the missing
inequality.  Its amplitude seam is polylogarithmic, but its phase-increment
kernel is target-equivalent to the original lower owner.  On an explicit
fourth-power family, disjoint half-integer resonance tubes have total
post-tube-modulus capacity \(\gg R^{3/2}\), compared with the target
\(RX^\varepsilon\).  This is an obstruction to local/tubewise norms, not a
lower bound for the fully signed sum.

Accordingly, the reduction and scoped obstruction are promoted.  The node
`M9-M1-global-lower-radial-signed-estimate` remains open.

## 2. Literal antecedent and normalization

Put \(R=X^{1/4}\), \(Y=\sqrt X\), \(y=\lfloor Y\rfloor\),
\(D_j=2^{-j}y\), and \(H_j=\lfloor D_j/R\rfloor\), omitting empty
height sets.  The exact positive reciprocal antecedent is

\[
 \mathcal B_{\rm low}^+
 =\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\tag{121.J1}
\]

Finite profile-first summation preserves every floor, the one-sided hard
sample, profile stars, and zero-extended boundary.  The accepted
coefficientwise character transform gives

\[
 \mathcal B_{\rm low}^+
 ={e(1/8)\over i}R\,G_{\rm low}(X)+O_{s_0}(\log^2(2X)).
\tag{121.J2}
\]

Thus the reciprocal target is \(O_\varepsilon(RX^\varepsilon)\), with
exactly one external factor \(R\).  Real coefficients make the negative
frequency its conjugate.

## 3. Corrected full-profile flattening theorem

Let the accepted inactive bottom be supported in \(d\leq C_bR\).  Choose
the already-permitted fixed lower cutoff so that

\[
 {3\sqrt{2s_0}\over4}<\frac12,
 \qquad {2\over\sqrt{2s_0}}>C_b,
\tag{121.J3}
\]

with \(V_{\rm low}=1\) on \([0,s_0]\) and zero on
\([2s_0,\infty)\).  Define

\[
 \mathcal B_{\rm flat}^+
 =\sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\tag{121.J4}
\]

On joint radial/profile support,

\[
 {hR\over D_j}\leq{3\sqrt{2s_0}\over4}<\frac12.
\tag{121.J5}
\]

Hence \(h\leq H_j\) with the literal floor and
\(h/(H_j+1)<1/2\).  Nonvanishing also forces
\(d>2R/\sqrt{2s_0}>C_bR\), so the inactive bottom vanishes.  The active
profiles sum exactly to \({\bf1}_{d\leq y}\), including the hard top
sample.  Replacing \(\Phi\) by one therefore gives (121.J4) exactly.

For the error, the explicit accepted Vaaler profile satisfies

\[
 |\Phi(u)-1|\ll u^2,\qquad |\Phi'(u)|\ll u
 \quad(0\leq u\leq1/2).
\tag{121.J6}
\]

On \(h\asymp L\), its height coefficient has sampled sup plus variation

\[
 \ll {1\over L}(L/H_j)^2.
\tag{121.J7}
\]

The coupled radial factor is not separated by a bare two-dimensional
\(C^1\) claim.  With \(u=h/L\), \(v=d/D_j\), and
\(\lambda=RL/D_j\), a fixed smooth extension of
\(V_{\rm low}(4\lambda^2u^2/v^2)\) has uniform high derivatives and
Fourier coefficients satisfying

\[
 \sum_{r,s}|c_{r,s}(\lambda)|(1+|r|)(1+|s|)\ll_{s_0}1.
\tag{121.J8}
\]

This weighted Wiener norm prices both modulated sampled variations.  The
accepted frequency-first theorem gives

\[
 E_{j,L}\ll_{\varepsilon,s_0}X^\varepsilon
 (L/H_j)^2(1+D_j/L).
\tag{121.J9}
\]

Since \(D_j/R<H_j+1\leq2H_j\), dyadic height summation costs
\(O(RX^\varepsilon)\) per profile, and the logarithmic profile count is
absorbed into \(X^\varepsilon\).  Therefore, for both signs,

\[
 \boxed{\mathcal B_{\rm low}^{\pm}
 =\mathcal B_{\rm flat}^{\pm}+O_{\varepsilon,s_0}(RX^\varepsilon).}
\tag{121.J10}
\]

This is the genuinely new result of the round.  It covers the whole fixed
lower cutoff, including the part above the Round-62 small-angle threshold.

## 4. Integer phase and exact discrepancy completion

Let \(N=\lfloor X\rfloor\), changing only the phase and retaining the
original \(R\), \(y\), and radial multiplier.  Since
\(|e(hX/d)-e(hN/d)|\ll h/d\) and a fixed \(d\) supports
\(O_{s_0}(d/R)\) heights,

\[
 \mathcal B_{\rm flat}^+(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O_{s_0}(R).
\tag{121.J11}
\]

Fix \(\eta\in C^\infty\) with \(\eta=0\) on \(( -\infty,1/2]\) and
\(\eta=1\) on \([1,\infty)\), and put on the small positive arc

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t},
\tag{121.J12}
\]

extended smoothly by zero and periodically.  Every supported nonzero
sample \(t=h/d\), \(d\leq y\), has \(t\geq1/y\), so this interpolant is
sample-exact.  Let

\[
 \widehat J(k)=\int_0^1J(t)e(-kt)\,dt,
 \quad A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),
 \quad c_y=\sum_{d\leq y}{\chi_4(d)\over d},
\tag{121.J13}
\]

for all \(m\in\mathbb Z\), with every positive \(d\) dividing zero.
Modulo-\(d\) Fourier completion gives the exact sign \(d\mid N+k\):

\[
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}\widehat J(k)A_y(N+k).
\tag{121.J14}
\]

Since \(J(0)=0\), \(\sum_k\widehat J(k)=0\).  Define, for every
\(k\in\mathbb Z\),

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right).
\tag{121.J15}
\]

Then \(D_N(0)=0\) and
\(D_N(k)-D_N(k-1)=A_y(N+k)-c_y\) for all integers \(k\).  Exact Abel
summation yields

\[
 \boxed{\mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)
 \{\widehat J(k)-\widehat J(k+1)\}.}
\tag{121.J16}
\]

All interchanges and boundaries are valid for fixed \(X\), because
\(\widehat J\) is Schwartz.  Its seminorms grow with \(y\), however, so
fixed-\(X\) smoothness supplies no uniform target bound.  Equations
(121.J10)--(121.J16) are a target-scale equivalence, not a solution.

## 5. Exact mod-four pair and scoped no-go

With the profile-first coefficient \(b_X(h,d)\) zero-extended at every
physical edge, pairing \(d\equiv1\pmod4\) with \(d+2\equiv3\pmod4\)
gives

\[
 \mathcal B_{\rm low}^+=\mathcal E_{\rm amp}+\mathcal K_X,
\tag{121.J17}
\]

where

\[
 \mathcal E_{\rm amp}
 =\sum_{d\equiv1(4)}\sum_h{b_X(h,d)-b_X(h,d+2)\over h}e(hX/d)
 \ll_{s_0}\log^2(2X),
\tag{121.J18}
\]

and

\[
 \mathcal K_X=\sum_{d\equiv1(4)}\sum_h{b_X(h,d+2)\over h}e(hX/d)
 \left\{1-e\!\left(-{2hX\over d(d+2)}\right)\right\}.
\tag{121.J19}
\]

For the flat coefficient the amplitude seam is \(O_{s_0}(\log(2X))\).
The narrow integer-increment set
\(\|2hX/(d(d+2))\|\leq R^{-1}\) costs
\(O(R\log X)\), hence is target-safe.  The complement remains open.

For infinitely many fourth powers \(X=R^4\), choose a fixed interval
\(d\asymp R^2\), and \(R^{4/5}\leq h\leq cR\) inside the flat lower
support.  Around every half-integer solution

\[
 {2hR^4\over d(d+2)}=k+\frac12
\]

take a tube of width \(\asymp R/\sqrt h\).  There are \(\asymp h\)
disjoint tubes for each \(h\); the bracket has fixed nonzero sign and the
outer phase lies in a fixed sector on each sufficiently narrow tube.
Consequently each tube has modulus \(\gg R/h^{3/2}\), and

\[
 \sum_{h,k}|\mathcal K_X[T_{h,k}]|\gg R^{3/2}.
\tag{121.J20}
\]

The corresponding stationary radial variable is \(n\asymp h^2\), so
this obstruction reaches \(n\geq X^{2/5}\).  Equation (121.J20) rejects
termwise, pairwise, or resonance-tubewise absolute closure.  It does not
rule out cancellation jointly across tubes, resonance labels, and heights,
and it is not a signed lower bound for \(\mathcal K_X\).

## 6. Reconciliation of the three reports

The statement-only rederivation first found the exact amplitude/phase pair
and the joint phase-transport survivor.  Its second-stage line audit
verified the floor, Fourier sign, \(d\mid0\), all-integer floor formula,
and Abel shift.  The selected-context formalizer independently proved the
complete profile flattening and identified the critical singleton-height
one-third capacity.  The hostile report supplied the half-integer
resonance-tube obstruction and caught both candidate defects.

The two repairs are now explicit:

1. replace the unsupported two-dimensional \(C^1\)-summability sentence
   by the high-regularity weighted estimate (121.J8); and
2. state bottom separation invariantly through the certified constant
   \(C_b\), rather than relying on an uncited numerical support edge.

All three reviews agree after these repairs.  No vote is used: the promoted
claim is the common line-by-line theorem that passed each seam.

## 7. Scope and state effect

Promote the target-scale equivalence (121.J10)--(121.J16), the amplitude
seams, and the scoped local-pairing/resonance-tube obstruction.  Record that
the discrepancy representation is a sharp global version of the accepted
Round-64/65 product-wavelet and unmatched-crossing return; it does not
supply a smaller norm.

Retain open:

- `M9-M1-global-lower-radial-signed-estimate` and therefore GAR;
- both direct blockwise M1 parents and `M9-M1`;
- hard TOP, balanced, and unbalanced M2 parents and `M9-M2`;
- endpoint uniformity, `M9`, the quarter theorem, and every improved
  pointwise exponent.

The lawful next M1 question is one genuinely joint signed inequality for
(121.J16) or (121.J19).  A further local character pair, derivative-only
resonance count, fixed-\(X\) Fourier norm, Appell/Poisson inversion, or
outside absolute value duplicates a proved no-gain route.


# Blind rederivation: absolute beta-weighted nonzero bands

## 1. Result

### Lemma (definition-level weighted upper bound)

Adopt

\[
\mathcal D_D=\{d\in\mathbb N:D\le d<2D\},\qquad n_D=|\mathcal D_D|,
\]

and define

\[
L_H=\sum_{\substack{1\le |h|\le H\\2\nmid h}}\frac1{|h|}
=2\sum_{\substack{1\le h\le H\\2\nmid h}}\frac1h,
\quad
C_{\Phi,H}=\frac1\pi\max_{1\le m\le H}
\left|\Phi\!\left(\frac m{H+1}\right)\right|.
\]

For optional dyadic weights let
\(W_D=\sup_{d\in\mathcal D_D}|w_D(d)|\).  For the coefficient-only mass in the
frozen distinctions, set \(w_D\equiv1\) and \(W_D=1\).  Put

\[
\begin{split}
N={}&h_1d_2d_3d_4-h_2d_1d_3d_4
+h_3d_1d_2d_4-h_4d_1d_2d_3,\\
\mathcal M_{\rm abs}(D,H;K)={}&
\sum_{d_1,\ldots,d_4\in\mathcal D_D}
\sum_{\substack{1\le |h_i|\le H\\0<|N|\le K}}
\prod_{i=1}^4 |w_D(d_i)\beta_{h_i,H}|,
\end{split}
\]

where

\[
\beta_{h,H}=-\Phi\!\left(\frac{|h|}{H+1}\right)
\frac{\chi_4(h)\mathbf 1_{2\nmid h}}{\pi h}.
\]

Then, for \(D,H\ge1\) and \(K\ge0\),

\[
\boxed{
\mathcal M_{\rm abs}(D,H;K)
\le (W_DC_{\Phi,H})^4(n_DL_H)^3
\min\!\left\{n_DL_H,\ (1+\log2)
\left(1+\frac{8K}{D^2}\right)\right\}.}
\tag{1}
\]

If \(0\le K<1\), the mass is exactly zero because \(N\) is an integer.  For the
phase-scale band \(K=\kappa D^4/X\), (1) gives

\[
\mathcal M_{\rm abs}(D,H;\kappa D^4/X)
\ll_\kappa (W_DC_{\Phi,H})^4D^3(1+\log(1+H))^3
\left(1+\frac{D^2}{X}\right).
\tag{2}
\]

Thus the Farey-packing factor is \(O_\kappa(1)\) throughout
\(D\le X^{1/2}\).  There is no polynomial transition at \(D=X^{3/8}\) in this
absolute weighted upper bound.  The proof uses no \(\chi_4\) cancellation.  It also
bounds the true signed mass by the triangle inequality, but provides no signed
cancellation theorem.

Without assumptions beyond the frozen definitions, (1) is the strongest bound
established here: it keeps the trivial total-mass cap, the nonzero-integrality
cutoff, all harmonic sums, every lift and Fourier truncation, and the spacing gain
for the fourth reduced fraction.

## 2. Exact statement and hypotheses

The only analytic hypothesis in (1) is finiteness of the displayed
\(C_{\Phi,H}\).  No smoothness, sign, or lower bound for \(\Phi\) is used.
If included, \(w_D\) need only obey \(|w_D|\le W_D\).  A different standard
half-open convention for \(d\asymp D\) changes only \(n_D\) and endpoint constants.

The specialization (2) is explicitly for
\(0<|N|\le\kappa D^4/X\).  Formula (1) is the statement to use for any other band
width.  The frozen brief does not define \(H_D\); one can set \(H=H_D\) in (1),
retaining its dependence in \(L_{H_D}\) and \(C_{\Phi,H_D}\).

## 3. Proof and derivation

### 3.1 Exact coefficient normalization

Even \(h\) contribute zero.  For odd \(h\), \(|\chi_4(h)|=1\), hence

\[
|\beta_{h,H}|\le\frac{C_{\Phi,H}}{|h|}.
\tag{3}
\]

The total one-coordinate mass therefore satisfies

\[
A(D,H):=\sum_{d\in\mathcal D_D}\sum_{1\le|h|\le H}
|w_D(d)\beta_{h,H}|
\le W_DC_{\Phi,H}n_DL_H.
\tag{4}
\]

Here \(L_H\le2(1+\log(1+H))\); it is the complete two-sided odd harmonic sum.
The unrestricted bound is

\[
\mathcal M_{\rm abs}(D,H;K)\le A(D,H)^4.
\tag{5}
\]

### 3.2 Reduced fractions and every lift

For each supported \((h,d)\), write uniquely

\[
g=(|h|,d),\qquad h=ga,\qquad d=gq,\qquad
a\in\mathbb Z\setminus\{0\},\quad q\in\mathbb N,\quad (|a|,q)=1.
\]

For a fixed reduced signed fraction \(a/q\), its permitted lifts are exactly

\[
\mathcal I_{a,q}=
\{g\in\mathbb N:D\le gq<2D,\ g|a|\le H,\ ga\ {\rm odd}\}.
\tag{6}
\]

This displays both truncations: \(D/q\le g<2D/q\) and \(g\le H/|a|\).
Nonemptiness implies

\[
q<2D,\qquad \frac{|a|}{q}=\frac{|h|}{d}\le\frac HD.
\tag{7}
\]

The absolute mass of all lifts is

\[
\begin{split}
\Lambda(a,q)
&:=\sum_{g\in\mathcal I_{a,q}}|w_D(gq)\beta_{ga,H}|\\
&\le\frac{W_DC_{\Phi,H}}{|a|}
\sum_{g\in\mathcal I_{a,q}}\frac1g
\le\frac{(1+\log2)W_DC_{\Phi,H}}{|a|}.
\end{split}
\tag{8}
\]

Indeed, if \(D/q<1\), the dyadic interval contains at most \(g=1\).  If
\(D/q\ge1\), the reciprocal sum over the factor-two interval is at most its first
term plus the corresponding integral, hence at most \(1+\log2\).  The
\(H/|a|\) cutoff and odd parity only delete terms.  In particular,

\[
\Lambda(a,q)\le(1+\log2)W_DC_{\Phi,H}.
\tag{9}
\]

Uniqueness of reduction gives the exact regrouping

\[
\sum_{(a,q)=1}\Lambda(a,q)=A(D,H).
\tag{10}
\]

This is the raw-versus-weighted seam: \(a/q\) can have \(\asymp D/q\) raw lifts,
whereas its beta-weighted lifts form a dyadic harmonic sum
\(O(1/|a|)\), not \(O(D/q)\).

### 3.3 Integer band to reduced-fraction packing

For four reduced pairs,

\[
\frac{N}{d_1d_2d_3d_4}
=\frac{a_1}{q_1}-\frac{a_2}{q_2}
+\frac{a_3}{q_3}-\frac{a_4}{q_4}.
\tag{11}
\]

Thus \(0<|N|\le K\) and \(d_i\ge D\) imply

\[
0<\left|\frac{a_1}{q_1}-\frac{a_2}{q_2}
+\frac{a_3}{q_3}-\frac{a_4}{q_4}\right|
\le\eta,\qquad \eta=\frac K{D^4}.
\tag{12}
\]

This enlargement may admit extra lifts, so it is valid for an upper bound.

Fix the first three reduced fractions.  The fourth lies in an interval of length
\(2\eta\).  Two distinct reduced signed fractions with positive denominators
\(q,r<2D\) satisfy

\[
\left|\frac aq-\frac br\right|=\frac{|ar-bq|}{qr}>
\frac1{4D^2}.
\tag{13}
\]

Therefore the interval contains at most

\[
P(D,K):=1+\lfloor8\eta D^2\rfloor
\le1+\frac{8K}{D^2}
\tag{14}
\]

eligible reduced fractions.  Restrictions (7) only reduce this count.  Their
combined fourth-coordinate lift mass is at most

\[
(1+\log2)W_DC_{\Phi,H}P(D,K).
\tag{15}
\]

Summing the first three coordinates through (10) gives

\[
\mathcal M_{\rm abs}(D,H;K)
\le A(D,H)^3(1+\log2)W_DC_{\Phi,H}
\left(1+\frac{8K}{D^2}\right).
\tag{16}
\]

Taking the smaller of (5) and (16), then using (4), proves (1).  No factor
\(H\), \(D/q\), or raw lift multiplicity is hidden.

### 3.4 Natural scale and endpoint calculation

For \(K=\kappa D^4/X\), (14) is
\(P(D,K)\le1+8\kappa D^2/X\).  Up to fixed constants, while retaining \(L_H\),
the three endpoint values are

\[
\begin{array}{c|c|c}
D&1+D^2/X&\text{upper-bound scale}\\ \hline
X^{1/4}&1+X^{-1/2}&X^{3/4}L_H^3\\
X^{3/8}&1+X^{-1/4}&X^{9/8}L_H^3\\
X^{1/2}&2&X^{3/2}L_H^3.
\end{array}
\]

The packing factor changes only by constants on this interval.  Hence an
\(X^{3/8}\) transition in a weight-blind count does not survive this
definition-level absolute-mass calculation.  Any later transition must enter
through data absent here, such as a specific \(H_D\), an external prefactor, or a
genuinely signed estimate.

## 4. First doubtful or unproved step

There is no unproved step in the conditional lemma (1).  The first unavailable
specialization is external to it: the frozen brief does not supply the exact
intended band width, \(H_D\), a bound or lower envelope for \(\Phi\), or a
definition of \(w_D\).  Therefore (2) is explicitly a specialization, not an
assertion that the campaign uses no other band convention.

The permitted artifacts name the accepted families “UNC”, “TS”, and “W-1” but do
not define them.  Identifying one of the tuple families below with those labels, or
claiming an exhaustive named-family check, would not be rigorous under the
statement-only boundary.  The universal upper bound applies to every family, but
label-specific adjudication is unavailable from the permitted context.

## 5. Control tests and outcomes

### Raw versus weighted

**Input.** The same nonzero integer band, first with unit tuple weights and then
with \(\prod_i|\beta_{h_i,H}|\).

**Raw calculation.** Fix \(d_1,\ldots,d_4,h_1,h_2,h_3\).  Consecutive values of
\(N\) as \(h_4\) varies differ by \(d_1d_2d_3\ge D^3\).  Thus there are at most
\(1+2K/D^3\) possible \(h_4\).  If

\[
Q_H=|\{h:1\le|h|\le H,\ 2\nmid h\}|,
\]

the supported weight-blind count obeys

\[
\mathcal R(D,H;K)\le n_D^4Q_H^3
\left(1+\frac{2K}{D^3}\right).
\tag{17}
\]

This has three full \(H\)-sized sums.  Equations (6)–(10) explicitly replace raw
lift multiplicities by reciprocal sums and those frequency sums by \(L_H^3\).

**Outcome.** The control passes for (1).  No exponent from (17), or another raw
tuple count, transfers to the absolute mass without the coefficient and lift
summation.

### Dyadic endpoints

**Input.** \(K=\kappa D^4/X\) at
\(D=X^{1/4},X^{3/8},X^{1/2}\).

**Outcome.** The table in Section 3.4 has no \(X^{3/8}\) change.  At the lower
endpoint the band is empty if \(\kappa D^4/X<1\).  At the upper endpoint the
packing factor remains \(O_\kappa(1)\); the proof does not cross
\(D=X^{1/2}\).

### Known lower-bound families

The definitions of “UNC”, “TS”, and “W-1” are absent from the permitted files, so
the named controls cannot be instantiated without breaching the blind boundary.
Two explicit algebraic controls nevertheless test the relevant absolute claim.

**Constant-\(N\), small odd-frequency family.** Let

\[
(h_1,h_2,h_3,h_4)=(1,1,3,3),\qquad
(d_1,d_2,d_3,d_4)=(t-10,t-7,t-8,t-9).
\tag{18}
\]

All frequencies are odd, \(H\ge3\) suffices, and \(D-O(1)\) values of \(t\)
put all denominators in \([D,2D)\).  Exact algebra gives

\[
N=6.
\tag{19}
\]

For verification, set \(u=(-10,-7,-8,-9)\) and signs \((+,-,+,-)\).
The signed moments \(\sum_i s_ih_i u_i^j\) vanish for \(j=0,1,2\), while the
\(j=3\) moment is \(-6\).  The degree-three numerator in (11) is therefore the
constant \(6\).

This family is present for \(K\ge6\), and it controls genuine absolute
coefficient-weighted mass.  If

\[
\phi_*=\min\left\{
\left|\Phi\!\left(\frac1{H+1}\right)\right|,
\left|\Phi\!\left(\frac3{H+1}\right)\right|\right\}>0,
\]

each tuple has beta mass at least \(\phi_*^4/(9\pi^4)\), so the contribution is
\(\gg\phi_*^4D\).  With \(w_D\), one additionally needs a lower envelope for
\(|w_D|\) on (18).  At the phase scale the family enters once
\(\kappa D^4/X\ge6\), a constant multiple of \(X^{1/4}\), not
\(X^{3/8}\).  Its \(\chi_4\) factors have product \(+1\); removing them does not
destroy the family, although a signed lower bound would also need sign information
on \(\Phi\).

**All-\(h=1\) family.** Let

\[
h_1=h_2=h_3=h_4=1,\qquad
(d_1,d_2,d_3,d_4)=(t,t+1,t+2,t+1).
\tag{20}
\]

Then \(N=2(t+1)\), parity is admissible, and \(D-O(1)\) choices lie in one
dyadic block.  Given a lower envelope at \(h=1\), this contributes an absolute
weighted mass of order \(D|\beta_{1,H}|^4\), not merely a raw count.  In the
phase-scale band it appears when \(D^3\gg X\), around \(X^{1/3}\), with no
distinguished \(X^{3/8}\) event.

**Outcome.** These controls do not falsify (1).  They do falsify any universal
claim that narrowing the band automatically gives a proportional \(K/D^4\) gain
in absolute mass.  The constant-\(N\) family persists as soon as the band contains
6.  Exact comparisons with named “UNC”, “TS”, and “W-1” artifacts remain
unadjudicated until their statements are supplied within the access boundary.

## 6. Dependencies and exact artifacts used

Only these artifacts were read:

1. rounds/codex-managed/m9-weighted-mass-adjudication/briefs/blind_weighted_upper_bound.md;
2. problems/gauss_circle.md;
3. state/control_models.md.

The proof otherwise uses integer reduction, harmonic-sum bounds, and elementary
separation of reduced fractions.  Two small integer substitutions were used only
to diagnose and check the explicit construction path; (19) is certified above by
exact algebra.  No computation certifies an asymptotic claim.  No claimant report,
proof graph, campaign plan, legacy Round 9 material, proof draft, web source, or
other task report was read.

## 7. Recommended state effect

**Promote** the conditional lemma (1) as candidate evidence for the absolute
beta-weighted mass.  **Reject or revise** any transfer of a weight-blind
tuple-count exponent, including an \(X^{3/8}\) transition, to this mass without
the lift and harmonic sums.  Make no claim of signed improvement: the lemma is
sign-blind and uses \(\chi_4\) only through \(|\chi_4(h)|=1\) on odd frequencies.
Named-family status should remain unchanged because their definitions were absent
from the permitted statement-only context.

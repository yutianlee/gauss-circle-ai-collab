# Conductor independent analysis: B1 proof and capacity

## Preliminary split verdict

The B1 pointwise lift envelope is correct for sharp cutoffs and for uniformly bounded-variation sampled profiles.  It is false for arbitrary bounded weights.  Even when B1 is valid, the envelope alone cannot imply a small signed fat-band energy: it provides size control for individual reduced fractions but no cancellation between distinct reduced fractions or pair sums.

## Exact B1 proof

Let \((p,q)=1\), \(q>0\), and

\[
A_\chi(p/q)=
\sum_{\substack{gq\in[D,2D)\\1\le|gp|\le H}}
\beta_{gp,H}w_D(gq).
\]

If \(p\) is even, then \(gp\) is even and the audited beta formula gives \(A_\chi(p/q)=0\).

Suppose \(p\) is odd.  Only odd \(g\) contribute, and

\[
\beta_{gp,H}
=-\frac{\chi_4(p)\chi_4(g)}{\pi |p|g}
\Phi\!\left(\frac{g|p|}{H+1}\right).
\]

Hence

\[
A_\chi(p/q)
=-\frac{\chi_4(p)}{\pi|p|}
\sum_{g\in\mathcal G}\chi_4(g)a_g,
\qquad
a_g=\frac1g\Phi\!\left(\frac{g|p|}{H+1}\right)w_D(gq),
\]

where \(\mathcal G\) is the integer interval cut out by

\[
D/q\le g<2D/q,
\qquad
g\le H/|p|.
\]

The partial sums of \(\chi_4(g)\) are uniformly bounded.  If the sampled sequence \(g\mapsto w_D(gq)\) has uniformly bounded supremum and total variation on every such interval, then discrete partial summation gives

\[
\left|\sum_{g\in\mathcal G}\chi_4(g)a_g\right|
\ll \sup_{\mathcal G}|a_g|+\operatorname{Var}_{\mathcal G}(a).
\]

On a nonempty interval, \(g\ge D/q\), so \(g^{-1}\le q/D\).  The audited \(\Phi\) is bounded and monotone on \([0,1]\).  Product variation therefore yields

\[
\sup|a_g|+\operatorname{Var}(a_g)
\ll \frac qD,
\]

including a one-point or short interval created by the cutoff \(g\le H/|p|\).  Thus

\[
\boxed{|A_\chi(p/q)|\ll\frac{q}{D|p|}}
\]

for odd \(p\), while \(A_\chi=0\) for even \(p\).  A fixed profile \(w_D(d)=W(d/D)\) with \(W\) of bounded variation supplies the needed discrete variation uniformly in \(D,q\).  A sharp interval cutoff is also uniformly BV.

The estimate is false under boundedness alone.  For example, take \(p=1\), choose an integer \(q_0\asymp2D/H\), and on the multiples \(d=gq_0\in[D,2D)\) set \(w_D(gq_0)=\chi_4(g)\) (extend it boundedly elsewhere).  The contributing lift interval contains \(g\asymp H\), the two character factors cancel, and

\[
|A_\chi(1/q_0)|\asymp\sum_{H/2\ll g\le H\atop g\text{ odd}}\frac1g\asymp1,
\]

whereas B1 would give \(O(q_0/D)=O(H^{-1})\).  The total variation of this adversarial weight along the sampled lift progression is \(\asymp H\), exactly the missing hypothesis.

## Exact signed global form

Let \(\mathcal R_D\) be the reduced fractions occurring in the lift decomposition and write \(A(r)=A_\chi(p/q)\) for \(r=p/q\).  Then

\[
S_2(D;t)=\sum_{r\in\mathcal R_D}A(r)e(tr/4).
\]

Choose a real smooth compactly supported \(\Omega\), normalize \(\int\Omega=1\), and define

\[
\mathfrak M_4(D;X)
=\frac1X\int_{\mathbb R}|S_2(D;t)|^4\Omega(t/X)\,dt.
\]

With Fourier transform \(\widehat\Omega(\xi)=\int\Omega(u)e(u\xi)\,du\), exact expansion gives

\[
\mathfrak M_4(D;X)
=\sum_{r_1,r_2,r_3,r_4}
A(r_1)\overline{A(r_2)}A(r_3)\overline{A(r_4)}
\widehat\Omega\!\left(\frac X4(r_1-r_2+r_3-r_4)\right).
\]

One unambiguous signed off-diagonal normalization is therefore

\[
c_\chi(D;X)=\frac1{D^2}
\sum_{r_1-r_2+r_3-r_4\ne0}
A(r_1)\overline{A(r_2)}A(r_3)\overline{A(r_4)}
\widehat\Omega\!\left(\frac X4(r_1-r_2+r_3-r_4)\right).
\]

The proposed global target is \(|c_\chi(D;X)|\ll_\epsilon X^\epsilon\).  Even this would remain a global-moment input, not a pointwise M2 estimate.

## Capacity of B1 alone

Existence of a lift forces, up to fixed dyadic constants,

\[
q\le2D,qquad |p|\le Hq/D.
\]

Summing only the B1 envelope gives

\[
\sum_{r\in\mathcal R_D}|A(r)|
\ll
\sum_{q\le2D}\frac qD
\sum_{1\le|p|\ll Hq/D}\frac1{|p|}
\ll D\log(2H),
\]

and

\[
\sum_{r\in\mathcal R_D}|A(r)|^2
\ll
\sum_{q\le2D}\frac{q^2}{D^2}
\sum_{p\ne0}\frac1{p^2}
\ll D.
\]

These scales allow the natural \(D^2\) exact fourth-moment diagonal, but they do not control the off-diagonal signed form.  Taking absolute values in the full kernel yields at best the fourth power of the \(\ell^1\) bound, while an exact additive-energy estimate from Young's inequality still permits

\[
\|A*A\|_2^2\le\|A\|_1^2\|A\|_2^2
\ll D^3\log^2(2H),
\]

which after division by \(D^2\) is a power loss near the endpoint.

More decisively, B1 admits an envelope-saturating countermodel.  Put

\[
A(1/q)=1\quad(D\le q<2D),
\qquad A(r)=0\quad\text{otherwise}.
\]

This satisfies \(|A(1/q)|\ll q/D\), but the same reciprocal pair-window argument as W-1 produces a nonnegative fat-band contribution \(\gg D^5/X\).  This is not merely abstract: for a nonnegative actual dyadic profile and \(q\asymp D\), the lift \(g=1\) gives \(A_\chi(1/q)=\beta_{1,H}w_D(q)\), a constant-sign family of this size.

The full true signed form may cancel that family, but B1 supplies no relation forcing the cancellation.  Therefore a proof using only the pointwise envelope would work equally for an adversarial coefficient system with no such cancellation, violating the `proves-too-much` control.

## Missing lemma

After B1, the next necessary input is not a better individual bound of the same type.  It is a signed correlation or energy statement across distinct reduced fractions, for example a bound on the kernel-weighted convolution

\[
\sum_s
\left(\sum_{r_1+r_3\approx s}A(r_1)A(r_3)\right)
\overline{
\left(\sum_{r_2+r_4\approx s}A(r_2)A(r_4)\right)}
\]

that exploits the actual \(\chi_4\)-generated phases and fails for the unsigned/adversarial control.  Its normalization and the later average-to-pointwise bridge must remain separate obligations.

# Round 12 synthesis: offset reflection is algebraically neutral

Campaign: `m9-m1-cross-product-offset-pairing`  
Round type: cross-product pairing attack  
Graph SHA-256 before patch: `476fcf1786eb8d91bdf7ff37e8aed557c6e10575aab1b60f3caaeb2cb274049f`

## Conductor decision

Promote the half-lattice centering lemma and the exact paired-offset
identity. Promote the scoped no-go: opposite product offsets have disjoint
nearest-product divisor fibers, so oddness supplies no termwise
cancellation. Retain a fully signed shifted-divisor correlation as open.

No point of the residual corridor \(\mathcal U_1\) is closed. The broader
possibility of cancellation between different denominators is not rejected.
All three reports agree on this scope; the hostile report explicitly
withholds a stronger mismatch-norm lower bound that would require an
unproved simultaneous shifted-prime statement.

## Half-lattice centering

Write the exact two-sided M1 block as

\[
 \mathcal M_{1,L}(D;X)
 =\sum_d\chi_4(d)w_D(d)\mathcal V_{L,H}(X/d),
\]

where \(\mathcal V\) is periodic, odd,
\(\|\mathcal V\|_\infty\ll1\), and
\(\|\mathcal V'\|_\infty\ll L\). Choose

\[
 c\in\tfrac12\mathbb Z,\qquad |X-c|\le\tfrac14.
\]

Keeping the actual spatial profile and hard endpoint fixed,

\[
 \boxed{
 \mathcal M_{1,L}(D;X)
 =\sum_d\chi_4(d)w_D(d)\mathcal V_{L,H}(c/d)
 +O_w(L+X^\varepsilon).}
\]

Indeed, away from changed nearest-integer assignments the total Lipschitz
cost is

\[
 L|X-c|\sum_{d\asymp D}\frac{|w_D(d)|}{d}\ll L.
\]

If an assignment changes, integrality forces
\(d\mid2c\) and \(2c/d\) odd, so only
\(O_\varepsilon(X^\varepsilon)\) denominators occur. Since
\(L\le H\asymp DX^{-1/4}\le X^{1/4}\), the error is target-sized. The
argument does not move or smooth the top cutoff.

## Exact paired-offset identity

For positive offsets \(u\) on the integer lattice when \(c\in\mathbb Z\)
and on the half-integer lattice when \(c\in\mathbb Z+1/2\), define

\[
 \mathcal F_-(u)=
 \{d:w_D(d)\ne0,\ d\mid c-u,\ d>2u\},
\]

\[
 \mathcal F_+(u)=
 \{d:w_D(d)\ne0,\ d\mid c+u,\ d>2u\}.
\]

The equality case in the upper nearest-integer convention can be omitted
because \(\mathcal V(1/2)=0\). Then

\[
 \mathcal M_{1,L}(D;X)
 =\sum_{u>0}\left(
 \sum_{d\in\mathcal F_-(u)}\chi_4(d)w_D(d)\mathcal V(u/d)
 -\sum_{d\in\mathcal F_+(u)}\chi_4(d)w_D(d)\mathcal V(u/d)
 \right)
 +O_w(L+X^\varepsilon).
\]

The two fibers are exactly disjoint. A common denominator would divide
\(2u\), but the lower nearest-product condition requires \(d>2u\).
Moreover divisibility gives

\[
 d\mid c-u\Rightarrow \mathcal V(u/d)=\mathcal V(c/d),
\qquad
 d\mid c+u\Rightarrow \mathcal V(u/d)=-\mathcal V(c/d).
\]

Thus the displayed outer minus sign on the upper fiber cancels the second
kernel sign. In the original \(c/d\) coordinate the two incidences
reinforce and reconstruct the centered M1 sum. Offset pairing is therefore
an exact reindexing, not a cancellation mechanism.

## Precise surviving correlation

For \(U<u\le2U\), put

\[
 \lambda_U=\min\left(\frac{LU}{D},1,\frac{D}{LU}\right),
 \qquad G_U(u,d)=\lambda_U^{-1}\mathcal V(u/d),
\]

and

\[
 \begin{aligned}
 \mathscr Q_U(c;D,L)=\sum_{U<u\le2U}\Big(&
 \sum_{d\in\mathcal F_-(u)}\chi_4(d)w_D(d)G_U(u,d)\\
 &-\sum_{d\in\mathcal F_+(u)}\chi_4(d)w_D(d)G_U(u,d)\Big).
 \end{aligned}
\]

A sufficient annular estimate is

\[
 \boxed{
 |\mathscr Q_U(c;D,L)|
 \ll_\varepsilon X^{1/4+\varepsilon}\lambda_U^{-1}.}
 \tag{PSC}
\]

After multiplying by \(\lambda_U\) and summing logarithmically many
annuli, PSC proves the M1 target. At the critical annulus \(U=D/L\), the
trivial divisor estimate is \(O_\varepsilon((D/L)X^\varepsilon)\), while
PSC asks for \(O_\varepsilon(X^{1/4+\varepsilon})\): the missing factor is
exactly \(H/L\). The same accounting persists on outer annuli. PSC retains
the actual character, actual spatial and Vaaler profiles, both fibers, and
the divisor-dependent symbol; it is not an estimate of either fiber norm.

## Rejected shortcuts and surviving control

The following mechanisms have zero demonstrated capacity:

- reflecting products about generic real \(X\) without first moving to the
  half-lattice;
- matching the same denominator across opposite offsets;
- rank-pairing or comparing the two divisor sets by symmetric-difference
  cardinality;
- applying separate fiberwise absolute values or a large sieve that sees
  only their disjoint supports.

Prime-product singleton examples falsify deterministic pairing, but they do
not prove a lower bound for the complete signed sum at every center. The
exact-square family from Round 11 remains a positive control: cancellation
can occur across distinct offsets and distinct denominators through ordered
\(\chi_4\)-alternation. Hence the next round should study the ordered
denominator mechanism rather than another reflection of product fibers.

M9-M1, M9-M2, M9, and the Gauss-circle target remain open. No numerical
experiment or external theorem was used.

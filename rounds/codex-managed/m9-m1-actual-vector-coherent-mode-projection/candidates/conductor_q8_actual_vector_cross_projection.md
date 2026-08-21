# Conductor candidate: exact \(q=8\) actual-vector cross-projection

Campaign: m9-m1-actual-vector-coherent-mode-projection.

Starting graph SHA-256:
6aebb7ada9edb65dc6a1605ac0741b8a0e750bc50317b78061cfe39ce382aa6e.

## Statement

Work on the literal Round-92 canonical hard complement, after the unique
global \(u=0\) owner and the successive Round-87--89 owners. Restrict to

\[
 M=8N,\qquad N\ \mathrm{odd},\qquad
 A\equiv B_2\equiv V\equiv2\pmod 8.
\]

Let \(\alpha N\equiv1\pmod8\) and \(8\beta\equiv1\pmod N\). Then the
completed trace factors exactly as

\[
 \mathfrak T_M
 =\mathfrak T_8(\alpha u,2,2,2;\alpha K)
  \mathfrak T_N(\beta u,A_N,B_{2,N},V_N;\beta K),
\]

and

\[
 {\mathfrak T_M\over M^2}
 ={c_8(u)\over8}
  {\mathfrak T_N(\beta u,A_N,B_{2,N},V_N;\beta K)\over N^2}.
\tag{C100.1}
\]

Here

\[
 {c_8(u)\over8}=
 \begin{cases}
  +\tfrac12,&8\mid u,\\
  -\tfrac12,&u\equiv4\pmod8,\\
  0,&4\nmid u.
 \end{cases}
\tag{C100.2}
\]

This includes nonunit \(K\). The canonical normalization is

\[
 M^{-5}\mathfrak T_M
 =M^{-3}{\mathfrak T_M\over M^2}.
\tag{C100.3}
\]

After the odd trace is opened, the four common local lifts contribute
\(4/M^4=2^{-10}N^{-4}\); they are not \(4^4\) independent row lifts.

For one odd-cofactor base \(y\), write the actual pair sequences on the
local order-four orbit as \(F_j^a(y)\) and \(G_j^c(y-v)\), \(j\bmod4\),
including the literal \(I_b\)-rows, multiplier, signs, entry and exit,
stars, and zero extension. With unnormalized transforms

\[
 \widehat F_k=\sum_{j\bmod4}e_4(-kj)F_j,\qquad
 \widehat G_k=\sum_{j\bmod4}e_4(-kj)G_j,
\]

the exact local coupling is

\[
 \sum_{j\bmod4}F_j^a(y)\overline{G_{j-1}^c(y-v)}
 ={1\over4}\sum_{k\bmod4}e_4(k)
 \widehat F_k^a(y)\overline{\widehat G_k^c(y-v)}.
\tag{C100.4}
\]

Generic hard odd-cofactor labels therefore give a cross-projection. The
only structural alignment \(c=a,\ v=0\) makes \(G=F\) and gives

\[
 2\Re\sum_jF_j\overline{F_{j-1}}
 ={1\over2}\bigl(|\widehat F_0|^2-|\widehat F_2|^2\bigr).
\tag{C100.5}
\]

In that aligned case the physical ordered pairs coincide modulo \(2N\),
so the first coarse quotient is \(R_*=M/(2N)=4\). Since
\(\rho_*\geq\min(M,J^{1/15}+O(1))>4\) for large \(J\), this slice belongs
to the accepted Round-88 coarse owner and is absent from the hard
complement.

Consequently the literal \(q=8\) hard package is the scalar
\(\mathscr C_8(U)\) obtained by inserting (C100.1)--(C100.4) into the
canonical energy, summing \(0<|u|<U\) with \(4\mid u\), retaining the odd
completed trace and all actual rows, and taking the conductor sum before
the absolute value. Its desired estimate is still

\[
 |\mathscr C_8(U)|
 \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}.
\tag{C100.6}
\]

No estimate of (C100.6), reverse lower bound, or power saving is asserted.

## Proof

CRT factorizes the unit mask, the four inverse phases, and the additive
character. Because every odd residue is self-inverse modulo \(8\), the
four-pole phase is zero modulo \(8\) when
\(A_8=B_{2,8}=V_8=2\). The local sum is therefore \(c_8(u)\), proving
(C100.1)--(C100.3).

The class \(\delta=\operatorname{CRT}(2,0)\pmod M\) has additive order four
and cycles all four odd local bases while fixing the odd coordinate. The
four row locations have local indices \(j,j-1,j-1,j-2\). Fourier
inversion on \(\mathbb Z/4\mathbb Z\) proves (C100.4). Alignment gives
(C100.5). Reduction modulo \(2N\) then identifies the aligned ordered
pairs, proving \(R_*=4\) and the prior ownership claim.

The hard indicator is outside the completed base sum, so each retained
tuple keeps its full four-cycle. It is nevertheless a nonproduct condition
in the odd labels and conductor row. Thus it fragments the family into
cross-projections and does not define a global commuting eigenspace.

## Scope

The result is exact only for \(v_2(M)=3\). If \(v_2(M)>3\), the full
\(2\)-power factor must be treated before CRT with the odd part; a mod-\(8\)
quotient is not a coprime CRT factor. The unique global \(u=0\) owner does
not delete nonzero \(u\equiv0\pmod8\), and it does not delete the
\(u\equiv4\pmod8\) branch. Local trace size, full directed degree, paired
trace words, and a difference-of-squares shadow do not imply a fixed-vector
lower bound. The canonical hard estimate and every downstream theorem
remain open.

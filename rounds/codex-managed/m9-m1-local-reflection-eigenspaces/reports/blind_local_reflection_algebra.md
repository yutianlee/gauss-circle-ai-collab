# Blind local reflection algebra

## 1. Result

Let
\[
a_z(n)=\sum_{hq=n}\chi_4(q)(q/h)^{z/2},\qquad n=2^k m,\quad m\text{ odd}.
\]
Then, as identities of entire functions of \(z\),
\[
\boxed{a_z(2^k m)=2^{-kz/2}a_z(m)},\qquad
\boxed{a_{-z}(2^k m)=\chi_4(m)2^{kz}a_z(2^k m)}.
\]
Thus reflection is a character eigenrelation on the odd part, but the prime \(2\) mixes those odd eigenspaces. This local identity does not cancel either generic arithmetic poles or the actual hard Perron residue.

## 2. Exact statement and hypotheses

Use \(\chi_4(2)=0\), \(\chi_4(p)=1\) for \(p\equiv1\pmod4\), and \(\chi_4(p)=-1\) for \(p\equiv3\pmod4\), with \(p^z=e^{z\log p}\). The coefficients are multiplicative, and for \(r\ge0\)
\[
a_z(2^r)=2^{-rz/2},
\]
while, for odd \(p\) and \(\epsilon_p=\chi_4(p)\),
\[
a_z(p^r)=p^{-rz/2}\sum_{j=0}^r(\epsilon_p p^z)^j.
\]
Consequently, where \(\Re(s\pm z/2)>1\),
\[
F_z(s):=\sum_{n\ge1}a_z(n)n^{-s}
=\frac1{1-2^{-s-z/2}}
\prod_{p\ {\rm odd}}
\frac1{(1-p^{-s-z/2})(1-\chi_4(p)p^{-s+z/2})}
=\zeta(s+z/2)L(s-z/2,\chi_4).
\]
The reflected eigencoefficients are \(a_z^\pm(n):=a_z(n)\pm a_{-z}(n)\). They obey \(a_{-z}^\pm=\pm a_z^\pm\), but their Dirichlet series \(F_z\pm F_{-z}\) are sums of Euler products, not themselves Euler products in general.

## 3. Proof or derivation

Since a nonzero \(\chi_4(q)\) forces \(q\) odd, every \(2\)-power in \(n=2^km\) lies in \(h\), giving the first boxed formula. For odd \(m\), swap \(h\) and \(q\):
\[
a_{-z}(m)=\sum_{hq=m}\chi_4(h)(q/h)^{z/2}
=\chi_4(m)\sum_{hq=m}\chi_4(q)(q/h)^{z/2},
\]
because \(\chi_4(h)=\chi_4(m)\chi_4(q)\). This proves the second formula and the Euler factors.

Writing \(b_z(m)=a_z(m)\), one gets the exact eigenspaces
\[
\boxed{a_z^\pm(2^km)=b_z(m)\bigl(2^{-kz/2}\pm\chi_4(m)2^{kz/2}\bigr).}
\]
For \(k=0\), \(a_z^+\) is supported on \(m\equiv1\pmod4\), and \(a_z^-\) on \(m\equiv3\pmod4\), apart from intrinsic coefficient zeros. If \(t=kz\log2/2\), the two rows are
\[
\begin{array}{c|cc}
&a_z^+&a_z^-\\ \hline
\chi_4(m)=1&2b_z(m)\cosh t&-2b_z(m)\sinh t\\
\chi_4(m)=-1&-2b_z(m)\sinh t&2b_z(m)\cosh t.
\end{array}
\]
Hence the odd congruence projection is lost once \(k>0\).

For \(p^r\Vert m\), a local coefficient vanishes exactly when
\[
(\chi_4(p)p^z)^{r+1}=1\quad\text{and}\quad \chi_4(p)p^z\ne1.
\]
There are no \(2\)-local zeros. Apart from these, for \(k>0\), \(a_z^+(2^km)=0\) exactly when \(2^{kz}=-\chi_4(m)\), and \(a_z^-(2^km)=0\) exactly when \(2^{kz}=\chi_4(m)\). At \(z=0\),
\[
a_0(n)=\sum_{q\mid n}\chi_4(q)=r_2(n)/4;
\]
it vanishes exactly when some \(p\equiv3\pmod4\) has odd valuation, and \(a_0^-\equiv0\), while \(a_0^+=2a_0\).

The series \(F_z^\pm=F_z\pm F_{-z}\) generically has two distinct poles. At \(s=1-z/2\) its residue is \(L(1-z,\chi_4)\); at \(s=1+z/2\) the residue is respectively \(+L(1+z,\chi_4)\) or \(-L(1+z,\chi_4)\). Thus neither eigenspace cancels a pole for \(z\ne0\), except if an independent \(L\)-zero removes it. At \(z=0\), only the tautological odd eigenspace vanishes; the even pole doubles.

The hard factor \(\widehat W_+(u)=1/u+\widehat W_{+,r}(u)\) is external to this coefficient algebra. Since \(z=u+v\), its \(u=0\) residue samples \(a_v^\pm\), which is not zero in general. At the joint mode \(u=v=0\), the odd eigencoefficient is identically zero; for general \(v\) there is no coefficientwise identity removing the residue. An antisymmetric *profile* pairing \(A\leftrightarrow A^{-1}\) can cancel paired endpoint half-residues, whereas the symmetric pairing completes them; that requires the global reflected profile absent from the actual M1 scale family and is not implied by \(a_z^\pm\).

## 4. First doubtful or unproved step

There is no doubtful step in the finite coefficient algebra. The first unproved step would be to infer a bound or Perron cancellation from it: such an inference needs exact scale/height/profile matching and a maximal contour estimate.

## 5. Required control test and outcome

Exact symbolic controls pass: \(n=2^k\) gives the two inverse monomials; odd \(p^r\) gives \(a_{-z}(p^r)=\chi_4(p)^r a_z(p^r)\); and \(z=0\) gives the classical \(r_2/4\) Euler factors and \(a_0^-=0\). No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only protocol.md, state/proof_obligations.yml, rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md, and rounds/codex-managed/m9-m1-reflected-mode-correlation/synthesis.md were used. The derivation depends on the stated definition of \(a_z\), the primitive character \(\chi_4\), and the Round-15/16 Mellin and Perron conventions.

## 7. Recommended state effect

Promote the boxed local reflection/eigenspace lemma and the scoped no-go: coefficient reflection alone removes no generic arithmetic pole or hard Perron residue. Retain the maximal angular-profile correlation and GAR as open; reject any claim that the odd coefficient eigenspace by itself supplies the missing global cancellation.

## Addendum: high-2-adic tail seam

**Verdict: REVISE (the asserted bound is presently unproved as stated).**

Put
\[
B_X:=\sup_{T,h,q}\lvert\mathcal H_{T,X}(h,q)\rvert .
\]
Because \(\chi_4(q)\ne0\) forces \(q\) odd, writing \(n=2^km\) gives \(q\mid m\), hence exactly \(d(m)\) possible incidences. Absolute summation therefore gives
\[
\begin{aligned}
\lvert{\rm tail}_{\ge K}\rvert
&\le B_X\sum_{k\ge K}2^{-3k/4}
 \sum_{\substack{m\le N_X/2^k\\m\ {\rm odd}}}d(m)m^{-3/4}\\
&\ll B_XN_X^{1/4}2^{-K}\log(2N_X),
\end{aligned}
\]
using partial summation from \(\sum_{m\le M}d(m)\ll M\log(2M)\). Thus the \(2^{-K}\), rather than \(2^{-3K/4}\), is correct: the shrinking range \(m\le N_X/2^k\) supplies the additional \(2^{-k/4}\). Conditional on \(B_X\ll\log X\), the proposed \(N_X^{1/4}2^{-K}\log^2X\) bound follows, and \(K=\lceil\log_2(2X^{1/8})\rceil\) makes it \(O(\log^2X)\).

Round 16, however, defines \(\mathcal H_{T,X}\) only as the exact scale sum containing floors, \(\Phi\), endpoint stars, smooth remainders, and a truncated Perron kernel; it records no uniform pointwise majorant. Such a majorant needs a separate lemma proving: \(O(\log X)\) active scales; uniformly bounded scale/height factors; uniformly \(L^1\) smooth remainders; and
\[
\sup_T\left|\frac1{2\pi i}\int_{(a),\,|\Im u|\le T}\frac{A^u}{u}\,du\right|\ll1
\]
uniformly for every occurring \(A\), with the actual symmetric truncation and an abscissa \(a\) satisfying \(A^a=O(1)\). The non-\(L^1\) \(1/u\) tail makes this last point nonautomatic. Until those exact profile hypotheses are checked, only the displayed conditional tail estimate is justified.

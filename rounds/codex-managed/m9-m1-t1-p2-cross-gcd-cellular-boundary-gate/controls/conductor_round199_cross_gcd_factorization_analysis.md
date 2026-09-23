# Conductor provisional cross-gcd factorization analysis

This is an independent algebraic control prepared while the three Round-199
reports are running. It is not an adjudication or theorem promotion.

## Exact eight-factor chart

Put

\[
 A=G_{00},\qquad B=G_{10},\qquad C=G_{01},\qquad E=G_{11}.
\]

Squarefreeness gives unique positive integers \(x,u,y,v\) such that

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv,
\tag{199.K1}
\]

and all eight factors \(A,B,C,E,x,u,y,v\) are pairwise coprime. In this
chart the recomputed character-leg gcd is \(g=A\), and the \(P_2\) defects
are exactly

\[
 A|Cx-BEu|\le D_L,\qquad A|By-CEv|>D_L.
\tag{199.K2}
\]

This proves the proposed four-state factorization, independently of any
cellular conclusion.

## Three exact same-\(A\) involutions

There are three natural scaled allocation complements which preserve both
products and the two absolute defects in (199.K2).

When \(B=1\), the lower complement is

\[
 L:(ACx,Eu,Ay,CEv)\longmapsto(AEu,Cx,Ay,CEv).
\tag{199.K3}
\]

It swaps \(C\leftrightarrow E\), \(x\leftrightarrow u\), fixes \(A\), and
has actual character quotient

\[
 p=\chi_4(CE xu)=\chi_4(\alpha m).
\tag{199.K4}
\]

When \(C=1\), the upper complement is

\[
 U:(Ax,BEu,ABy,Ev)\longmapsto(Ax,BEu,AEv,By).
\tag{199.K5}
\]

It swaps \(B\leftrightarrow E\), \(y\leftrightarrow v\), fixes \(A\), and
has actual character quotient

\[
 t=\chi_4(BEyv)=\chi_4(\beta m').
\tag{199.K6}
\]

When \(E=1\), the simultaneous complement is

\[
 D:(ACx,Bu,ABy,Cv)\longmapsto(ABu,Cx,ACv,By).
\tag{199.K7}
\]

It swaps \(B\leftrightarrow C\), swaps both unique-factor pairs, fixes
\(A\), and has actual character quotient

\[
 z=\chi_4(xuyv).
\tag{199.K8}
\]

Each map is a literal involution only on its stated domain. These formulas
also show why the old lower/upper square requires \(B=C=E=1\): after one
partial complement, the domain condition of the other must still hold.

## The \(B\)-\(E\)-\(C\) triangle

Let one nontrivial odd factor \(q>1\) occupy successively the \(B,E,C\)
states. The exact three vertices are

\[
\begin{aligned}
 V_B&=(Ax,qu,Aqy,v),\\
 V_E&=(Ax,qu,Av,qy),\\
 V_C&=(Aqu,x,Av,qy).
\end{aligned}
\tag{199.K9}
\]

They form the closed cycle

\[
 V_B\xrightarrow{U}V_E\xrightarrow{L}V_C\xrightarrow{D}V_B
\tag{199.K10}
\]

and all three retain the same \(P_2\) defects

\[
 A|x-qu|\le D_L,\qquad A|qy-v|>D_L.
\tag{199.K11}
\]

Put

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\tag{199.K12}
\]

Then the three edge quotients are \(t,p,pt\), since
\(pt=\chi_4(xuyv)\). The local-system product around the cycle is \(1\), as
required, but this alone supplies no cancellation of vertex weights.

Write

\[
 \ell_0=\overline{\lambda_{N,\sigma}(Ax)},\quad
 \ell_1=\overline{\lambda_{N,\sigma}(Aqu)},\quad
 u_0=\lambda_{N+r,\sigma}(Aqy),\quad
 u_1=\lambda_{N+r,\sigma}(Av).
\tag{199.K13}
\]

After extracting the common radical/Fejer scalar and the character at
\(V_B\), the complete triangle is

\[
 u_0\ell_0+t u_1\ell_0+tp u_1\ell_1.
\tag{199.K14}
\]

The lower sign at \(V_E,V_C\) is \(p\), while \(V_B\) is always a
\(B=q>1\) gcd-failure vertex. Hence:

- if \(p=-1\) and the lower code is common, only \(V_B\) is in the
  Round-199 complement and the other two vertices are the accepted
  common-cell difference;
- if \(p=-1\) and the code changes, all three vertices are in the joint
  gcd/literal-boundary complement;
- if \(p=+1\), all three are in the joint gcd/sign-failure complement.

In the constant endpoint shadow the actual signed augmentation is

\[
 1+t+tp=
 \begin{cases}
 1,&p=-1,\\
 1+2t\in\{-1,3\},&p=+1.
 \end{cases}
\tag{199.K15}
\]

Thus the triangle's incidence signs do not themselves cancel the joint bad
vertices.

## Missing \(G_{00}\) corner

The fourth product corner is

\[
 V_A=(Aqu,x,Aqy,v).
\tag{199.K16}
\]

Its recomputed gcd is \(Aq\), and its relative character sign is \(p\).
Adding it gives the exact rectangle

\[
 u_0\ell_0+t u_1\ell_0+tp u_1\ell_1+p u_0\ell_1
 =(u_0+t u_1)(\ell_0+p\ell_1).
\tag{199.K17}
\]

For \(p=-1\), (199.K17) restores the desired lower difference, but it does
not make a literal sharp-code jump small. Moreover, \(V_A\) is not a same-
\(A\) corner. Its lower defect is

\[
 |Aqu-Aq x|=Aq|u-x|.
\tag{199.K18}
\]

Together with \(A|x-qu|\le D_L\), \(q\ge3\), and the live shell lower bound
\(qu\gg L\), (199.K18) is \(>D_L\) for all sufficiently large shells. Thus
the completing \(G_{00}\) corner lies in the unproved lower-far \(P_1\)
owner; bounded shells alone do not supply an asymptotic completion.

Even if that corner were admitted, the aligned \(p=-1\) literal-face case
retains the full lower sharp-code difference in (199.K17), while the upper
leg is the inherited far allocation. The accepted \(D_L/L\) common-cell
calculus therefore does not follow from the cellular incidence alone.

## Provisional interpretation

The new factorization and triangle are genuine algebraic progress over a
cross-coprime four-corner chart. The provisional first self-return is that
the three live same-\(A\) corners have nonzero twisted augmentation, while
their endpoint mixed-difference completion requires the changed-\(A\)
\(G_{00}\) corner and still does not smooth an aligned literal jump. The
reports must determine whether any actual-coefficient repair avoids both
facts. No lower mass or failure of the literal Round-199 theorem is asserted
here.

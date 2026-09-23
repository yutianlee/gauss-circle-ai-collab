# Round 185 conductor exact no-pair fibre-deletion control

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Task: conductor_round185_exact_fibre_deletion_control
- Role: conductor reproduction of a bounded exact falsification control
- Generated: 2026-08-28T01:29:56.2384012+08:00
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Evidence class: diagnostic_only; not asymptotic theorem evidence
- Arithmetic engine: local WolframScript, exact integers only

## Question and pass rule

Test whether the primitive tangent step, which flips the bare
\(\chi_4\)-product, necessarily preserves the squarefree, coprime,
no-pair hard-M1 arithmetic endpoint support.  Automatic arithmetic
pairing fails if two adjacent geometric fibre sites have the same
positive shift and stay in both hard ratio cones, while the first has
two live no-pair endpoints and the second loses an endpoint through an
arithmetic deletion.

The test does not inspect opaque profile, floor, star, half-weight,
hard-sample, crossing, or endpoint amplitudes.  Passing it disproves
only automatic arithmetic support invariance.

## Parameters and canonical location

Use the plus orientation with the local fibre site

\[
 \kappa=103,\qquad u=7,\qquad v=1,\qquad
 (s_\star,w_\star)=(99,14).
\]

Here

\[
 n=s_\star v-w_\star u=1,\qquad
 g=(u,n)=1,\qquad h=n/g=1,\qquad U=u/g=7.
\]

The canonical plus anchor is

\[
 S_{0,+}=[\bar v h]_U=1,\qquad
 w_{0,+}=(S_{0,+}v-h)/U=0.
\]

Consequently the local sites \((99,14)\) and \((106,15)\) are the
canonical fibre indices \(t=14\) and \(t=15\), respectively.

## Exact calculation

At the first site,

\[
 (d,d',m',m)=(721,919,103,131),\qquad
 N=94451,\quad N'=94657,\quad r=N'-N=206.
\]

The exact factorizations are

\[
 N=7\cdot103\cdot131,\qquad
 N'=103\cdot919.
\]

Both products are squarefree and both displayed allocations are
coprime.  The hard-cone checks are

\[
 4(131)<721<16(131),\qquad
 4(103)<919<16(103).
\]

Every odd prime \(7,103,131,919\) is \(3\bmod4\).  Thus neither
endpoint possesses a pair of distinct prime factors with
\(\chi_4(pq)=-1\), so both Round-184 residual masks equal one
independently of the canonical selector.  The character product is

\[
 \chi_4(919)\chi_4(721)=-1.
\]

At the adjacent tangent site,

\[
 (d,d',m',m)=(721,933,103,133),\qquad
 N=95893,\quad N'=96099,\quad r=N'-N=206.
\]

The exact factorizations are

\[
 N=7^2\cdot19\cdot103,\qquad
 N'=3\cdot103\cdot311.
\]

Both hard-cone checks still hold:

\[
 4(133)<721<16(133),\qquad
 4(103)<933<16(103).
\]

But \((721,133)=7\), so the lower product contains \(7^2\) and is
deleted.  The upper product remains squarefree and coprime.  The
character product is

\[
 \chi_4(933)\chi_4(721)=+1.
\]

Thus the shift and hard cones survive while the arithmetic support is
not invariant under the adjacent character flip.

## Exact Wolfram reproduction

The conductor ran the following Wolfram Language expression through
the locally installed WolframScript.  It uses only exact integer
arithmetic, factorization, gcd, residue classes, and inequalities.

    k=103;u=7;v=1;s0=99;w0=14;
    ch[n_]:=If[Mod[n,4]==1,1,-1];
    row[t_]:=Module[{s=s0+u t,w=w0+v t,d,dp,m,mp,n,np,pairs,pairsp},
      d=k u;dp=k u+2s;mp=k v;m=k v+2w;n=d m;np=dp mp;
      pairs=Select[Subsets[First/@FactorInteger[n],{2}],
        ch[#[[1]]] ch[#[[2]]]==-1&];
      pairsp=Select[Subsets[First/@FactorInteger[np],{2}],
        ch[#[[1]]] ch[#[[2]]]==-1&];
      {t,{d,dp,mp,m},np-n,FactorInteger[n],FactorInteger[np],
       CoprimeQ[d,m],CoprimeQ[dp,mp],SquareFreeQ[n],SquareFreeQ[np],
       4m<d<16m,4mp<dp<16mp,ch[dp]ch[d],pairs,pairsp}];
    InputForm[{row[0],row[1]}]

The exact output was

    {{0,{721,919,103,131},206,
      {{7,1},{103,1},{131,1}},{{103,1},{919,1}},
      True,True,True,True,True,True,-1,{},{}},
     {1,{721,933,103,133},206,
      {{7,2},{19,1},{103,1}},{{3,1},{103,1},{311,1}},
      False,True,False,True,True,True,1,{}, {}}}

## Outcome and limitation

The control passes as a falsification of automatic no-pair arithmetic
support invariance.  It is stronger than the earlier
\((101,7,1,8,1)\) example because the first site is provably no-pair
at both endpoints, independently of the selector threshold and choice.

The example does not prove that either opaque literal coefficient is
nonzero for a specified \(L,X,\sigma\).  It proves no density,
coefficient-weighted lower bound, asymptotic obstruction, failure of the
desired correlation, parent theorem, or exponent statement.  Its sole
licensed use is to block promotion of bare tangent alternation to an
automatic literal adjacent-pair cancellation.

## Dependencies and exact artifacts

This control uses only the algebraic plus-orientation parametrization in
the Round-185 candidate and the Round-184 definition of an eligible
opposite-character prime pair.  No web source, external theorem,
floating-point calculation, random experiment, or numerical asymptotic
evidence is used.

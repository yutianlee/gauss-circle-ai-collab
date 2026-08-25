# Conductor candidate: single-wave BI parameter map and source-condition seam

Campaign: `gc-w7-16-bombieri-iwaniec-two-spacing-source-map`

Starting graph SHA-256:
`465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`.

This is an independent conductor derivation.  It proves a single-wave phase
and parameter identity and exposes one printed source-condition seam.  It
makes no claim that the joint project scalar satisfies the source theorem.

## 1. Exact single-wave map

Split the project numerator sign and dyadic endpoints into \(O(1)\) pieces.
For a positive branch, put

\[
 h=a,\qquad m=b,\qquad H_{\rm LY}=L,\qquad M_{\rm LY}=D,\qquad
 T_{\rm LY}={c\over\kappa_i},\qquad F(z)={1\over z}.       \tag{133.C1}
\]

Then

\[
 {hT_{\rm LY}\over M_{\rm LY}}F(m/M_{\rm LY})
 ={a(c/\kappa_i)\over D}{D\over b}
 ={ca\over\kappa_i b}.                                   \tag{133.C2}
\]

For the negative branch, put \(h=-a>0\) and conjugate the positive-\(F\)
sum, or make an equivalent genuine phase reversal.  A coefficient sign
alone does not reverse an exponential phase.  Thus the phase of one
unrestricted ray wave is exactly in the Li--Yang standard form after this
finite sign split.

For \(1\le z\le2\),

\[
 F'=-z^{-2},\qquad F''=2z^{-3},\qquad F'''=-6z^{-4},       \tag{133.C3}
\]

and

\[
 F'F'''-3(F'')^2=-6z^{-6}.                               \tag{133.C4}
\]

Both source phase conditions therefore hold with fixed constants.

This proves only the phase and derivative dictionary.  The source weights
are separable BV functions \(g(h/H)G(m/M)\); no such factorization of the
actual ray coefficient, still less the pair coefficient, follows from
(133.C1).

## 2. Exact source powers at the project critical block

At \(c\asymp Y\),

\[
 T_{\rm LY}\asymp Y,\qquad
 M_{\rm LY}=Y^{1/2},\qquad
 H_{\rm LY}=Y^{1/6},\qquad
 {H_{\rm LY}\over M_{\rm LY}}\asymp T_{\rm LY}^{-1/3}.    \tag{133.C5}
\]

The conditional lower clauses of Case A are inactive at
\(M=T^{1/2}\): neither \(M<T^{7/16}\) nor \(M>T^{9/16}\) holds.  Its
upper clause is satisfied because

\[
 {1\over6}<{1\over2}-{49\over164}={33\over164}.           \tag{133.C6}
\]

The Case-A short length is

\[
 N_A\asymp H(M/H)^{41/25}T^{-49/100}
 =Y^{67/300+o(1)}.                                        \tag{133.C7}
\]

Indeed \(1/6+41/75-49/100=67/300\).  Hence

\[
 R=(M^3/(N_AT))^{1/2}=Y^{83/600+o(1)}.                   \tag{133.C8}
\]

At the extremal dyadic spacing scale \(Q=R\),

\[
 L_{\rm BI}={H\over R}=Y^{17/600+o(1)},\qquad
 K_{\rm BI}={N_A\over R}=Y^{17/200+o(1)},                \tag{133.C9}
\]

and

\[
 \eta={R^2\over N_AH}=Y^{-17/150+o(1)}.                 \tag{133.C10}
\]

Thus \(K_{\rm BI}L_{\rm BI}=\eta^{-1}\) at \(Q=R\).
These \(L_{\rm BI},K_{\rm BI}\) are source spacing variables and must not
be confused with the project numerator length \(L\) or inner curvature
cost \(K_D\).

With the source final choice at \(x=-1/3\),

\[
 {2\over q-2}=5\sqrt{5/34}-1,
 \qquad q=2+{2\over5\sqrt{5/34}-1}
 ={250+10\sqrt{170}\over91}.                              \tag{133.C11}
\]

The final source exponent formula specializes exactly to

\[
 \Phi(-1/3)= {8\over75}+{51\over200}
 -{1\over200}\left(\sqrt{34/3}-5\sqrt{5/3}\right)^2.     \tag{133.C12}
\]

Equivalently,

\[
 \Phi(-1/3)={29+5\sqrt{170}\over300}
 =0.313973413506755\ldots .                               \tag{133.C12a}
\]

Even a valid estimate for one separably weighted \(S\) would give
\(|S|\ll Y^{1/6+\Phi(-1/3)+\varepsilon}\).  This is not yet a bound for
the determinant-restricted pair scalar.

## 3. Printed equation (4.9) is not the substitution of (4.6) and (4.8)

The official v2 source's exact Lemma-4.1 condition (4.6) is

\[
 N^{6-q}\gg H^{2q-6}(M^3/T)^{4-q}.                       \tag{133.C13}
\]

With the Case-A definition of \(N\) in source equation (4.8),

\[
 N_A=H(M/H)^{41/25}T^{-49/100}(\log T)^{969/14000},       \tag{133.C14}
\]

direct substitution gives, apart from the displayed logarithm,

\[
 (H/M)^{(54-34q)/25}T^{(106-51q)/100}\gg1.               \tag{133.C15}
\]

Equivalently,

\[
 (H/M)^{(34q-54)/(25(6-q))}
 \ll T^{(106-51q)/(100(6-q))}(\log T)^{969/14000}.        \tag{133.C16}
\]

The source instead prints the purported substituted condition as equation
(4.9):

\[
 H^{(2q-6)/(6-q)+16/25}M^{34/25}
 \ll T^{51/100}(\log T)^{969/14000}.                     \tag{133.C17}
\]

Equations (133.C16) and (133.C17) are not algebraically equivalent.  At
the project substitution \(H=T^{1/6}\), \(M=T^{1/2}\), the printed
condition (133.C17) fails already from its \(M^{34/25}\) factor, whereas
(133.C13) has positive fixed-power slack for the source choice (133.C11).

This does not by itself break the narrow final Li--Yang theorem.  With
\(H=MT^x\), the exact logarithm-free exponent condition (133.C13) is

\[
 {x(54-34q)\over25}+{106-51q\over100}\ge0.               \tag{133.C18}
\]

Li--Yang's later displayed check

\[
 {7x/25-1/50\over41x/25+49/100}< {q-2\over q-4}           \tag{133.C19}
\]

has both numerator and denominator negative on the final range.  Multiplying
with the correct sign shows that (133.C19) is exactly (133.C18):

\[
 (216x+106)-q(136x+51)>0.                                \tag{133.C20}
\]

Thus the final proof may be repaired by using (133.C19) directly to verify
the original Lemma condition (133.C13), bypassing the false printed
intermediate (133.C17).  An independent source audit must reproduce this
repair before any update to the accepted Li--Yang source card.

## 4. First project normal-form mismatch

The candidate project rays \((a,b)\) are the **summation variables**
\((h,m)\) in (133.C1).  In the Bombieri--Iwaniec proof, the reduced
fractions \(a_{\rm BI}/r_{\rm BI}\) are instead Dirichlet approximants to

\[
 {T\over M^2}F'(m_0/M)                                   \tag{133.C21}
\]

on short \(m\)-intervals of length \(N_A\), with
\(r_{\rm BI}\asymp Q\) and \(R\le Q\le H\).  Here
\[
 {a_{\rm BI}\over r_{\rm BI}}\asymp {T\over M^2}\asymp1,
 \qquad {a\over b}\asymp {L\over D}=Y^{-1/3},             \tag{133.C22}
\]

and \(r_{\rm BI}\le H=Y^{1/6}\), while the project ray denominator is
\(b\asymp D=Y^{1/2}\).  They are different roles, ratios, and scales.

Therefore the small project determinant

\[
 ab'-a'b                                                   \tag{133.C23}
\]

does not automatically furnish any of the source second-spacing conditions
on \(\bar a_{\rm BI}/r_{\rm BI}\),
\(\bar a_{\rm BI}c_0/r_{\rm BI}\), \(\mu r_{\rm BI}^3\), or
\(\kappa_0\).  An exact map would have to be derived after the source's
short-interval and derivative-approximation construction, not by renaming
the project ray.

Moreover, the literal pair coefficient

\[
 C_i^{\rm pair}(r,r'):=A_i(r)B_i(r,r')
 =A_i(r)H_{i;r,p}(n)C_{i;r,p}(n)                         \tag{133.C24}
\]

is joint and determinant-restricted.  A theorem for one separably weighted
\(S\) does not estimate its pair correlation.  Row decomposition supplies
one source-like inner sum per outer ray only after inserting a moving
determinant wedge and outer-dependent primitive owners; neither separated
BV weight nor an affordable sum of source norms has been proved.

## 5. Required controls

| Control | Conductor outcome |
|---|---|
| single-wave phase | Exact: (133.C1)--(133.C4). |
| source powers | Exact: (133.C5)--(133.C10). |
| source Case A | Phase-scale tuple meets the conditional Case-A size clauses. |
| printed (4.9) | Fails algebraic substitution; must be bypassed by (133.C13), (133.C18)--(133.C20). |
| project ray versus approximant | Different roles and denominator scales \(Y^{1/2}\) versus at most \(Y^{1/6}\). |
| joint coefficient | No separated BV/projective norm supplied. |
| S/H direction | One-S bound only; no literal pair-scalar connector. |
| capacity | No \(35/48\to<27/48\) implication has been obtained. |

No numerical experiment was used.

## 6. Dependencies and artifacts used

This derivation used the official local arXiv v2 TeX source, the accepted
Round-95 source card and repair review, the Round-133 blind source statement,
and the accepted Round-131/132 literal scalar and chart statements.  It did
not use any Round-133 subagent report.

## 7. Recommended provisional effect

Retain (133.C1)--(133.C12) as a candidate exact single-wave dictionary.
Send (133.C13)--(133.C20) to an independent source seam audit; do not yet
change the accepted external theorem node.  Treat (133.C21)--(133.C24) as
the first candidate project mismatch and require the discovery and blind
tasks to derive or refute a lawful connector.  No exponent or graph promotion
is presently justified.

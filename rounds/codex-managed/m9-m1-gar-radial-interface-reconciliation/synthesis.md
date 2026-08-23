# Round 120 synthesis: terminal-height completion of the GAR radial interface

Campaign: `m9-m1-gar-radial-interface-reconciliation`

Starting graph SHA-256:
`daa3c03b4b08ab062fa78724813fd2beff02ad92df8bf25d32407b1ce7f91177`

Resulting graph SHA-256 after the validated State Patch:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

## Frozen objective

The round asked for the exact sharp radial/interface parent remaining after
one fixed lower--critical--upper partition of

\[
 G_X=\sum_{n\leq N_X}^{*}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn}),
 \qquad N_X=\lfloor16\sqrt X\rfloor,
\]

and for a coefficientwise audit against the proved compact critical,
physical endpoint, boundary, and \(R_1\) modules.

The endpoint-prefix deletion proposed in the blind statement is not by
itself sufficient: its constant endpoint phase is not the original radial
collar phase.  The round instead found and proved a new terminal-height
aggregate which bounds the whole nonlower radial complement directly.

## Terminal-height theorem

Put \(R=X^{1/4}\), \(Y=\sqrt X\),
\(D_j=2^{-j}\lfloor Y\rfloor\), and
\(H_j=\lfloor D_j/R\rfloor\).  Fix \(0<s_0<8\), set
\(\kappa=\sqrt{s_0}/4\), and choose a real smooth \(\vartheta\) with

\[
 \vartheta(u)=0\quad(u\leq\kappa/2),\qquad
 \vartheta(u)=1\quad(u\geq\kappa).
\tag{120.S1}
\]

Insert \(\vartheta(h/H_j)\) into every active literal \((j,h)\)-atom of
\(\mathcal C_X^*(n)\), omitting the empty scales \(H_j=0\), and call the
result \(\mathcal C_{T,X}^*(n)\).  The exact positive reciprocal antecedent
has frequency weight

\[
 u_{j,T}(h)={\bf1}_{h\leq H_j}\vartheta(h/H_j)
 {\Phi(h/(H_j+1))\over h}.
\]

It is supported on \(h\asymp_{s_0}H_j\) and satisfies

\[
 \|u_{j,T}\|_\infty+\sum_h|\Delta u_{j,T}(h)|
 \ll_{s_0}H_j^{-1}.
\tag{120.S2}
\]

For every nonempty active scale,

\[
 {D_j\over2R}\leq H_j\leq{D_j\over R},
\tag{120.S3}
\]

so the proved terminal divisor theorem bounds the total positive antecedent
by \(O_{\varepsilon,s_0}(RX^\varepsilon)\).  The accepted smooth interior
and one-sided hard character transforms are coefficientwise in \(h\).
Consequently

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})+O_{s_0}(\log^2(2X)).
\tag{120.S4}
\]

The lower \(\vartheta\)-interface costs only (120.S2).  The transform
remainder is absolute at
\(\sum_{h\asymp H_j}h^{-1}\log(2+h)\), and the hard cotangent boundary has
terminal \(h^{-1}\)-mass \(O_{s_0}(1)\).  Thus no deleted-height
cancellation or hidden \(R\)-factor occurs.  Dividing (120.S4) by \(R\)
proves the complex bound

\[
 \boxed{
 \sum_{n\leq N_X}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_{\varepsilon,s_0}X^\varepsilon.}
\tag{120.S5}
\]

The negative frequency is its real-coefficient conjugate, so the accepted
paired physical normalization is retained.

## Exact radial geometry

For a nonzero atom put \(s=n/Y\) and

\[
 t={2h\sqrt{X/n}\over D_j}={2hR\over D_j\sqrt s}.
\]

The certified closed profile support is

\[
 {1\over2}\leq t\leq{3\over2};
\tag{120.S6}
\]

there is no uniform closed constant smaller than \(3/2\).  Since

\[
 {hR\over D_j}={t\sqrt s\over2},
\tag{120.S7}
\]

the upper floor inequality in (120.S3) gives, atom by atom,

\[
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)
 \qquad(n/Y\geq s_0).
\tag{120.S8}
\]

Conversely, \(\vartheta(h/H_j)\ne0\), the lower floor inequality, and
\(t\leq3/2\) imply

\[
 {n\over Y}>{\kappa^2\over9}={s_0\over144}=:c_T>0.
\tag{120.S9}
\]

Also \(h\leq H_j\leq D_j/R\) and \(t\geq1/2\) give \(n/Y\leq16\).
All internal stars, the outer half tie, the hard sample, and the exact
floors survive these coefficientwise identities.

## Localized terminal subtraction

Choose one fixed smooth lower cutoff

\[
 V_{\rm low}(s)=1\quad(s\leq s_0),\qquad
 V_{\rm low}(s)=0\quad(s\geq2s_0).
\tag{120.S10}
\]

Because \(V_{\rm low}\) is not compactly supported away from zero, support
of the transformed coefficient alone is not enough to invoke Mellin
transfer.  The required repair is antecedent-level.  Choose
\(\psi\in C_c^\infty((0,16))\) equal to one on
\([c_T,2s_0]\).  On the joint support of
\(\vartheta(h/H_j)w_j(d)\), the exact profile shell and floor bounds give

\[
 {4R^2h^2\over d^2}>c_T.
\]

Thus replacing \(V_{\rm low}(z)\) by
\(W_0(z)=\psi(z)V_{\rm low}(z)\) changes no reciprocal summand.  Mellin
inversion produces frequency BV

\[
 O_{s_0}\left({1+|t'|\over H_j}\right),
\]

and the denominator mode remains bounded.  The same accepted terminal
theorem and coefficient-preserving smooth/hard transforms, with
\(4R^2h^2/d_*^2=hq/Y\), prove

\[
 \sum_{n\leq N_X}^{*}V_{\rm low}(n/Y)
 \mathcal C_{T,X}^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,s_0}X^\varepsilon.
\tag{120.S11}
\]

Equations (120.S8) and (120.S10) give the exact coefficient identity

\[
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)
 =(1-V_{\rm low}(n/Y))\mathcal C_{T,X}^*(n).
\tag{120.S12}
\]

Subtracting (120.S11) from (120.S5) yields the stronger whole-complement
theorem

\[
 \boxed{
 \sum_{n\leq N_X}^{*}(1-V_{\rm low}(n/Y))
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,s_0}X^\varepsilon.}
\tag{120.S13}
\]

## One-count interface implication

For the Round-98 partition

\[
 1=V_{\rm low}+\sum_{a=1}^A V_a+U,
\]

where every \(V_a\) is fixed and compact inside \((0,16)\), the old sharp
interface multiplier is \(U\).  Equation (120.S13) contains both those
compact critical cells and \(U\); it is not definitionally the old
interface.  The exact lawful subtraction is

\[
 G_X[U]=G_X[1-V_{\rm low}]-\sum_{a=1}^A G_X[V_a].
\tag{120.S14}
\]

The first term is proved by (120.S13), and every compact term is proved by
the accepted critical transfer.  Hence the sharp radial/interface parent
is target-safe.  Equivalently, one may use the exact two-piece partition
\(V_{\rm low}+(1-V_{\rm low})=1\).

The physical upper endpoint prefix has constant phase
\(e(\sqrt{XN_X})\), while the collar has the varying phase
\(e(\sqrt{Xn})\).  They are not identified.  The endpoint-boundary and
\(R_1\) modules belong to a different transformed architecture and have
multiplicity zero in (120.S13)--(120.S14).  They are not hard-transform
errors.  No \(C\uparrow16\) limit, shrinking cutoff, arbitrary finite
Mellin height, alpha connector, or additional flat owner is used.

## Report reconciliation and controls

The statement-only report correctly proved that the endpoint-prefix and
fixed-critical hypotheses alone do not imply a collar estimate; it
isolated their exact coefficient mismatch.  Its follow-up correctly
identified (120.S4) and (120.S11) as the missing seams.  It was not allowed
the accepted terminal and coefficientwise transform artifacts needed to
prove them.

The literal formalization, hostile scope audit, and conductor adjudication
then independently verified those seams.  Before acceptance the following
repairs were made:

1. \(C_W<3/2\) was replaced everywhere by the certified
   \(C_W=3/2\), giving \(c_T=s_0/144\);
2. the auxiliary compact multiplier was inserted before transform;
3. the whole nonlower complement was distinguished from the old interface;
4. endpoint/\(R_1\) modules were assigned multiplicity zero on this route;
5. empty \(H_j=0\) scales were excluded before forming \(h/H_j\).

Every campaign control passes after those corrections: literal coefficient,
external \(X^{1/4}\), fixed one-count partition, compact-transfer scope,
endpoint-prefix nonidentification, boundary/\(R_1\) routing, collar, support
flatness, floors/stars/hard sample, physical versus finite height, alpha
nonduplication, lower-parent disjointness, and downstream scope.  No
numerical computation or new external source was used.

## Decision and proof status

Round 120 promotes the terminal-height whole-nonlower theorem and the sharp
radial/interface parent.  Under the proved Round-98 radial assembly, the
only remaining analytic parent of GAR is now
`M9-M1-global-lower-radial-signed-estimate`.

GAR itself remains open.  The two direct blockwise M1 parents remain open
at their separate one-third menu frontier; complete GAR would control only
the total active M1 aggregate and would not prove blockwise `M9-M1`.
`M9-M2` still has its independent hard TOP, balanced, and unbalanced
parents, and endpoint uniformity remains separate.  Thus Round 120 changes
neither the internal exponent \(1/3\) nor the audited external benchmark

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

The next rigorous M1 campaign should attack the exact lower-radial signed
aggregate as one global owner, starting from the literal reciprocal
antecedent and preserving the floor-perturbed height symbol.  Another
endpoint-prefix, finite-height, or invertible-return round is not warranted.

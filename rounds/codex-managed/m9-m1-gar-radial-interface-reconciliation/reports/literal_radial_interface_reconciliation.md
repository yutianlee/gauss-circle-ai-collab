# Round 120 formalization: terminal-height completion of the sharp radial interface

Campaign: m9-m1-gar-radial-interface-reconciliation  
Task: literal_radial_interface_reconciliation  
Role: formalizer  
Starting graph SHA-256: daa3c03b4b08ab062fa78724813fd2beff02ad92df8bf25d32407b1ce7f91177  
Status: candidate evidence only; this report changes no shared proof state.

## 1. Result: the interface closes by a terminal-height aggregate

There is a target-safe aggregate which agrees coefficientwise with the
entire nonlower radial sum. This closes the Round-98 sharp
radial/interface parent after one exact subtraction of the already proved
fixed compact critical pieces.

More precisely, put \(R=X^{1/4}\), \(Y=\sqrt X\),
\(y=\lfloor Y\rfloor\), \(D_j=2^{-j}y\),
\(H_j=\lfloor D_j/R\rfloor\), and
\(N=N_X=\lfloor16Y\rfloor\). Insert one fixed smooth factor
\(\vartheta(h/H_j)\), supported where \(h/H_j\) is bounded below, into
every literal \((j,h)\)-atom of \(\mathcal C_X^*(n)\), and call the result
\(\mathcal C_{T,X}^*(n)\). Then, in complex modulus,

\[
 \sum_{n\le N}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})\ll_\varepsilon X^\varepsilon .
 \tag{1.1}
\]

For a fixed lower cutoff \(V_{\rm low}\) chosen below,
\(\mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)\) wherever
\(1-V_{\rm low}(n/Y)\ne0\). A fixed compact-cutoff version of (1.1)
therefore gives the exact identity and estimate

\[
 \boxed{
 \mathcal G_X[1-V_{\rm low};\mathcal C_X^*]
 =\mathcal G_X[1;\mathcal C_{T,X}^*]
  -\mathcal G_X[V_{\rm low};\mathcal C_{T,X}^*]
 \ll_\varepsilon X^\varepsilon ,}
 \tag{1.2}
\]

where

\[
 \mathcal G_X[F;\mathcal C]
 :=\sum_{n\le N}^{*}F(n/Y)\mathcal C(n)n^{-3/4}
 e(\sqrt{Xn}).
\]

If the frozen Round-98 one-count partition is

\[
 1=V_{\rm low}+\sum_{a=1}^{A}V_a+U,
 \qquad V_a\in C_c^\infty((c_a,C_a)),\quad C_a<16,
 \tag{1.3}
\]

then \(U\) is its sharp upper/interface multiplier and

\[
 \boxed{
 \mathcal G_X[U;\mathcal C_X^*]
 =\mathcal G_X[1-V_{\rm low};\mathcal C_X^*]
   -\sum_{a=1}^{A}\mathcal G_X[V_a;\mathcal C_X^*]
 \ll_\varepsilon X^\varepsilon .}
 \tag{1.4}
\]

Thus M9-M1-global-radial-interface-estimate has a complete candidate
proof. The conductor candidate (120.C1)--(120.C8), together with the
localized transform proof (120.J5)--(120.J25), passes analytically,
with two necessary wording corrections: (120.C8) is the whole nonlower
complement, not literally the pre-existing Round-98 interface summand
until (1.4) is displayed; and the endpoint/\(R_1\) modules are not Poisson
transform errors in this proof. They have multiplicity zero here and
remain counted once in their own transformed boundary routing.

A separate direct flat-edge calculation also proves every polynomially
shrinking collar \(16Y-n\ll Y^{1-\eta}\), for fixed \(\eta>0\). Flatness
alone does not bound a fixed-proportion collar; the terminal-height
aggregate is what completes the interface without an \(X\)-dependent
cutoff-seminorm extrapolation.

## 2. Exact statement and hypotheses

The literal normalized radial sum is

\[
 G_X=\sum_{n\le N}^{*}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn}),
 \tag{2.1}
\]

with

\[
 \mathcal C_X^*(n)
 =\sum_{\substack{hq=n\\q\ {\rm odd}}}\chi_4(q)\Omega_X^*(n,h),
 \qquad
 \Omega_X^*(n,h)
 =\sum_j\mathbf1_{h\le H_j}
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^* .
 \tag{2.2}
\]

All stars in (2.1)--(2.2) are the accepted literal ones: the outer radial
half weight at \(n=N\), the product/profile equality value, and the
one-sided hard \(j=0\) sample. No floor is smoothed. The exact active-M1
normalization is

\[
 \mathcal M_{1,{\rm active}}^{\rm stat}(X)
 =-{4\over\pi}R\,\Re\{e(1/8)G_X\}+O_W(\log^2X).
 \tag{2.3}
\]

The certified normalized spatial profiles have the closed support bound
\(C_W=3/2\): for every nonzero atom,

\[
 {1\over2}\le
 t:={2h\sqrt{X/n}\over D_j}
 ={2hR\over D_j\sqrt{s}}\le {3\over2},
 \qquad s={n\over Y}.
 \tag{2.4}
\]

The sole continuum jump is the hard top at \(t=1\); the lower support edge
\(t=1/2\) is a fixed \(C^\infty\) flat edge for the interior and hard
profiles.

Choose fixed \(s_0>0\) with \(2s_0<16\), set

\[
 \kappa={\sqrt{s_0}\over4},
\]

and choose \(\vartheta\in C^\infty([0,\infty))\) with
\(\vartheta(u)=0\) for \(u\le\kappa/2\) and
\(\vartheta(u)=1\) for \(u\ge\kappa\). Define

\[
 \Omega_{T,X}^*(n,h)
 :=\sum_j\mathbf1_{h\le H_j}\vartheta(h/H_j)
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
 \tag{2.5}
\]

and define \(\mathcal C_{T,X}^*\) from (2.2) with
\(\Omega_X^*\) replaced by \(\Omega_{T,X}^*\). Only active \(j\), for
which \(H_j\ge1\), occur.

Finally choose fixed \(V_{\rm low}\in C^\infty([0,\infty))\) with

\[
 V_{\rm low}(s)=1\quad(s\le s_0),
 \qquad V_{\rm low}(s)=0\quad(s\ge2s_0).
 \tag{2.6}
\]

Under exactly these hypotheses, (1.1)--(1.4) hold for every sufficiently
large real \(X\). Their physical contribution is
\(O_\varepsilon(X^{1/4+\varepsilon})\) by (2.3), and the complex estimate
simultaneously controls the paired positive and negative frequency signs.

The auxiliary collar statement is: for any fixed \(\eta>0\), any bounded
multiplier \(A_X(s)\) supported on
\(16-2Y^{-\eta}\le s\le16\) satisfies

\[
 \mathcal G_X[A_X;\mathcal C_X^*]\ll_{\varepsilon,\eta}X^\varepsilon.
 \tag{2.7}
\]

No smoothness or cutoff-seminorm bound on \(A_X\) is needed for (2.7).

## 3. Proof and coefficientwise one-count derivation

### Terminal-height estimate and exact transform

The positive reciprocal antecedent of (2.5) is exactly

\[
 \mathcal B_T^+
 =\sum_j\sum_{h\le H_j}
 {\vartheta(h/H_j)\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)e(hX/d).
 \tag{3.1}
\]

On the support of \(\vartheta\), \(h\asymp_{s_0}H_j\). A fixed-BV
partition makes (3.1) a bounded number of shells \(h\asymp L\) with
\(L\asymp H_j\). On each shell the frequency coefficient has

\[
 \|u\|_\infty+\sum_h|u(h+1)-u(h)|\ll_{s_0}{1\over L};
 \tag{3.2}
\]

this follows from the fixed smooth \(\vartheta\), the accepted \(C^1\)
regularity of \(\Phi\), and \(h\asymp L\). The proved frequency-first
bound therefore gives

\[
 \mathcal B_{T,j}^+
 \ll_\varepsilon X^\varepsilon(1+D_j/H_j).
\]

For every active scale,

\[
 {D_j\over2R}\le H_j\le {D_j\over R},
 \tag{3.3}
\]

so \(D_j/H_j\le2R\). There are \(O(\log X)\) active scales. After
reducing the epsilon used in the block theorem,

\[
 \mathcal B_T^+\ll_\varepsilon RX^\varepsilon.
 \tag{3.4}
\]

Both the accepted interior stationary transform and the accepted
one-sided hard-top transform are linear in the \(h\)-coefficient.
Multiplication by \(\vartheta(h/H_j)\) therefore gives, without changing
any stationary coefficient, star, or hard sample,

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\le N}^{*}\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})+O_\varepsilon(X^\varepsilon).
 \tag{3.5}
\]

For the hard scale the separated cotangent denominators remain separated;
the extra factor is bounded and leaves their weighted contribution
polylogarithmic. The transform remainders are likewise polylogarithmic
after the \(1/h\) terminal weight and the logarithmic scale sum. Thus the
error displayed in (3.5) is valid after absorption into \(X^\varepsilon\).
Dividing (3.5) by \(R\) and using (3.4) proves (1.1).

### Exact support and the nonlower complement

Put \(A_j=D_j/R\). From (2.4),

\[
 {h\over A_j}={t\sqrt s\over2}.
 \tag{3.6}
\]

If an original atom is nonzero and \(s\ge s_0\), then \(t\ge1/2\), so

\[
 {h\over H_j}\ge {h\over A_j}
 ={t\sqrt s\over2}\ge {\sqrt{s_0}\over4}=\kappa.
\]

Consequently \(\vartheta(h/H_j)=1\), atom by atom, proving

\[
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)
 \quad(n/Y\ge s_0).
 \tag{3.7}
\]

Conversely, if a terminal atom is nonzero, then \(h/H_j>\kappa/2\).
The lower inequality in (3.3) gives

\[
 {h\over A_j}={h\over H_j}{H_j\over A_j}>{\kappa\over4}.
\]

Using \(t\le3/2\) in (3.6),

\[
 s\ge c_T:={\kappa^2\over9}={s_0\over144}>0.
 \tag{3.8}
\]

Also \(h\le H_j\le A_j\) and \(t\ge1/2\) give \(s\le16\). To apply the
fixed compact transfer to the \(V_{\rm low}\)-weighted terminal sum,
choose a fixed smooth \(\lambda\) which is zero on
\([0,c_T/2]\) and one on \([c_T,\infty)\). Coefficientwise,

\[
 V_{\rm low}(n/Y)\mathcal C_{T,X}^*(n)
 =\lambda(n/Y)V_{\rm low}(n/Y)\mathcal C_{T,X}^*(n),
 \tag{3.9}
\]

and \(\lambda V_{\rm low}\in C_c^\infty((0,16))\), with upper support
below \(2s_0<16\). Mellin separation of this fixed radial multiplier
leaves the \(h\)-coefficient

\[
 \vartheta(h/H_j)\Phi(h/(H_j+1))h^{-1+2it},
\]

whose sup-plus-variation norm is
\(O_{s_0}((1+|t|)/H_j)\). The denominator coefficient remains bounded.
The same terminal theorem, followed by the same exact smooth/hard
transforms, therefore proves

\[
 \mathcal G_X[V_{\rm low};\mathcal C_{T,X}^*]
 \ll_\varepsilon X^\varepsilon.
 \tag{3.10}
\]

Because \(1-V_{\rm low}=0\) on \(s\le s_0\), (3.7) gives the pointwise
coefficient identity

\[
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)
 =(1-V_{\rm low}(n/Y))\mathcal C_{T,X}^*(n).
 \tag{3.11}
\]

Equations (1.1), (3.10), and (3.11) prove (1.2). Subtracting the already
proved compact functions in the exact partition (1.3) proves (1.4).

### Direct flat-edge collar control

Let \(\sigma_n=16Y-n\ge0\). On a nonzero atom in a fixed neighborhood of
the upper edge, \(h\le H_j\le A_j\) and (2.4) give

\[
 0\le t-{1\over2}
 \le {2\over\sqrt{s}}-{1\over2}
 \ll {\sigma_n\over Y}.
 \tag{3.12}
\]

Uniform \(C^\infty\)-flatness at the lower spatial support edge gives, for
every fixed integer \(K\ge0\),

\[
 \left|[w_j(D_jt)]^*\right|
 \ll_K(t-1/2)_+^K.
 \tag{3.13}
\]

The hard \(t=1\) projector is bounded by one and is disjoint from this
lower-edge issue. There are \(O(\log X)\) active scales, \(\Phi\) is
bounded, and the number of factorizations \(hq=n\) is at most
\(\tau(n)\). Hence

\[
 |\mathcal C_X^*(n)|
 \ll_{K,\varepsilon}X^\varepsilon
 \left({\sigma_n\over Y}\right)^K.
 \tag{3.14}
\]

For \(S=Y^{1-\eta}\), (3.14) and \(n\asymp Y\) yield

\[
 \sum_{16Y-n\ll S}^{*}
 |\mathcal C_X^*(n)|n^{-3/4}
 \ll_{K,\varepsilon}
 X^\varepsilon Y^{-3/4}\sum_{\sigma\ll S}
 (\sigma/Y)^K
 \ll X^\varepsilon Y^{1/4-\eta(K+1)}.
 \tag{3.15}
\]

Choosing \(K+1>1/(4\eta)\) proves (2.7), with every equality star bounded
in its literal location. If instead \(S\asymp Y\), the right side is of
capacity \(Y^{1/4}\) for every fixed \(K\). Therefore flatness does not
license \(C\uparrow16\) in the fixed-\(V\) theorem without a separate
uniform cutoff-seminorm statement.

### Coefficientwise one-count table

For one literal atom write

\[
 b_{j,h,q}:=\kappa_N(hq)\chi_4(q)(hq)^{-3/4}
 \mathbf1_{h\le H_j}\Phi(h/(H_j+1))
 [w_j(2h\sqrt{X/(hq)})]^*,
\]

where \(\kappa_N\) is the outer radial star. The table records the exact
multiplier of \(b_{j,h,q}\).

| Piece | Atom multiplier | Owner and one-count disposition |
|---|---|---|
| Lower radial | \(V_{\rm low}(hq/Y)e(\sqrt{Xhq})\) | Excluded from this task; multiplicity \(0\) here; remains open. |
| Fixed compact critical \(a\) | \(V_a(hq/Y)e(\sqrt{Xhq})\) | Proved by the critical terminal transfer; subtracted exactly once in (1.4). |
| Terminal-height aggregate | \(\vartheta(h/H_j)e(\sqrt{Xhq})\) | Auxiliary proved aggregate (1.1), used once; it is not an additional flat radial partition cell. |
| Terminal compact subtraction | \(V_{\rm low}(hq/Y)\vartheta(h/H_j)e(\sqrt{Xhq})\) | Proved once by (3.9)--(3.10) and subtracted once in (1.2). |
| Whole nonlower complement | \((1-V_{\rm low}(hq/Y))e(\sqrt{Xhq})\) | Equals the preceding terminal complement coefficientwise by (3.11); target-safe. |
| Round-98 sharp interface | \(U(hq/Y)e(\sqrt{Xhq})\) | Equals nonlower complement minus the fixed compact critical cells; target-safe by (1.4). |
| Flat radial collar | \(A_X(hq/Y)e(\sqrt{Xhq})\) | A refinement inside \(U\), not an extra owner; (2.7) closes polynomially shrinking collars. |
| Physical upper endpoint prefix | \(e(\sqrt{XN})\), independent of \(hq\), on the full starred prefix | Same \(\mathcal C_X^*\), hard sample, and stars only after the accepted physical limit, but not the radial-interface multiplier; multiplicity \(0\) in (1.2)--(1.4). |
| Lower endpoint prefix | The accepted \(-e(\sqrt X)\) original-sector prefix at \(\xi=1\) | Target-safe transformed boundary owner; not a radial partition cell; multiplicity \(0\) here. |
| Recombined \(R_1\) residue | The accepted continuous \(y\)-integral with lower-minus-upper phase | Target-safe after aggregate physical routing; it is not a discrete \(b_{j,h,q}\) subtotal; multiplicity \(0\) here. |
| Endpoint boundary operator | Lower prefix \(+\) upper prefix \(+\mathfrak R^{\rm ar}[R_1]\), after artificial-pole cancellation | Target-safe in its transformed route and excludes both diagonal transition traces; it is not reinserted here. |
| Beta transition | Connector-completed beta-bounded transformed vector | Already target-safe, but alternative/nested; multiplicity \(0\) in the radial partition. |
| Alpha transition | Connector-completed alpha-bounded transformed vector | Still open and alternative/nested; neither added to nor subtracted from the physical interface. |

In particular, if

\[
 \mathcal U_X=e(\sqrt{XN})
 \sum_{n\le N}^{*}\mathcal C_X^*(n)n^{-3/4}
\]

is the accepted physical upper prefix, its atom multiplier is
\(e(\sqrt{XN})\), whereas the interface multiplier is
\(U(n/Y)e(\sqrt{Xn})\). These agree at most on the single radial endpoint
when \(U=1\); they do not agree on a collar. Thus no integration-by-parts
prefix has been mistaken for an original radial collar.

## 4. First doubtful or unproved step

The first seam in the conductor candidate was (120.C2): whether the
accepted positive-frequency transforms remain exact after inserting
\(\vartheta(h/H_j)\), especially at the one-sided hard top. This seam is
discharged in (120.J5)--(120.J12): the transforms are coefficientwise
linear in the \(h\)-weight, the accepted per-frequency remainder is
absolute \(O(\log(2+h))\), the terminal sum of
\(\log(2+h)/h\) is \(O_{s_0}(\log(2+H_j))\), and the hard cotangent
boundary is pointwise \(O(1)\) against terminal \(h^{-1}\)-mass
\(O_{s_0}(1)\). The scale sum is therefore \(O_{s_0}(\log^2X)\).

The localized seam is also discharged in (120.J19)--(120.J24). On the
joint terminal/profile support the reciprocal radial argument lies above
\(s_0/144\); when \(V_{\rm low}\ne0\) it lies below \(2s_0\). Hence the
fixed compact multiplier \(W_0=\psi V_{\rm low}\) changes no antecedent.
Its normalized denominator derivatives are uniformly bounded, its Mellin
modes have height variation \(O((1+|t|)/H_j)\), and the same absolute
interior/hard remainder ledger applies. I find no invalid step in
(120.J5)--(120.J25). The first invalid assertion in the earlier candidate
was instead a claimed strict support bound below \(3/2\); the adjudication
correctly repairs it to the certified closed bound \(C_W=3/2\).

The first statement that does require revision is the sentence following
(120.C8) that calls (120.C8) exactly the Round-98 interface parent.
Equation (120.C8) is exactly the whole nonlower complement. For the frozen
three-owner partition it contains the already proved compact critical
cells as well as the sharp interface. The exact lawful implication is
(1.4). This is a wording/owner correction, not an analytic gap.

The second revision is that the physical endpoint prefix, aggregate
endpoint/\(R_1\) operator, and beta transition are not errors in (3.5).
They arise only in the alternative Mellin/Hankel boundary architecture.
Their correct count in the present proof is zero; their accepted theorems
remain intact in their own route.

No estimate for the lower-radial signed aggregate is proved. The direct
flatness argument also leaves a fixed-proportion collar unproved if used
without the terminal-height aggregate.

## 5. Required control tests and outcomes

### Hostile check of (120.C1)--(120.C8)

| Candidate line | Verdict | Check |
|---|---|---|
| (C1) terminal antecedent and bound | Pass | The \(\vartheta\Phi/h\) weight has the required \(L^{-1}\) sup-plus-variation norm on \(O_{s_0}(1)\) shells, and (3.3) gives \(D_j/H_j\le2R\). |
| (C2) exact transform | Pass | Linearity preserves the exact stationary coefficient, both stars, and hard sample. Hard cotangent and transform errors remain polylogarithmic after the terminal \(1/h\) weight. |
| (C3) normalized terminal estimate | Pass | Divide (3.4)--(3.5) by \(R\); the complex modulus is obtained before sign pairing. |
| (C4) support identity | Pass | It is the algebraic rearrangement \(hR/D_j=t\sqrt s/2\). |
| (C5) equality with \(\mathcal C_X^*\) | Pass | \(H_j\le D_j/R\) and \(t\ge1/2\) force \(h/H_j\ge\kappa\) for every nonzero atom with \(s\ge s_0\). |
| (C6) lower radial support | Pass with clarification | \(H_j\ge D_j/(2R)\) and the exact \(t\le3/2\) give \(s>s_0/144\). The interval \([s_0/144,16]\) itself is not compactly inside \((0,16)\), but only its \(V_{\rm low}\)-weighted part is sent to the compact transfer; (3.9) supplies the exact fixed compact cutoff. |
| (C7) complement identity | Pass | \(1-V_{\rm low}\) vanishes where (C5) is unavailable, so the identity is literal at each integer \(n\), including the endpoint star. |
| (C8) estimate | Pass; owner wording revised | It follows from (1.1) and (3.10). It is the nonlower complement and implies, rather than literally equals, the Round-98 interface through (1.4). |

### Audit of (120.J5)--(120.J25)

| Equations | Verdict | Hostile check |
|---|---|---|
| (J5)--(J8) | Pass | Both zero-extension jumps are \(O(H_j^{-1})\); \(\vartheta\Phi/h\) has total sampled variation \(O_{s_0}(H_j^{-1})\); and \(\lfloor D_j/R\rfloor\ge D_j/(2R)\) on every nonempty active scale. |
| (J9)--(J10) | Pass | The amplitude identity is exact, and the \(h\)-only multiplier commutes with each interior or one-sided hard \(d\)-transform. It reconstructs precisely \(\mathcal C_{T,X}^*\), not an endpoint-prefix coefficient. |
| (J11)--(J12) | Pass | The accepted per-frequency remainder is absolute before the outer Vaaler weight. Terminal support turns its sum into \(O_{s_0}(\log H_j)\) per scale. The hard cotangent term is pointwise \(O(1)\) and its terminal \(1/h\)-mass is \(O_{s_0}(1)\). Thus the complete error is \(O_{s_0}(\log^2X)\) without deleted-height cancellation. |
| (J13)--(J18) | Pass | The exact closed bound \(1/2\le t\le3/2\) gives both coefficient equality above \(s_0\) and terminal support above \(s_0/144\), with all floors and stars untouched. |
| (J19)--(J20) | Pass | A fixed \(\psi\in C_c^\infty((0,16))\) exists because \(0<s_0/144<2s_0<16\). The inequalities show that \(W_0=\psi V_{\rm low}\) changes no reciprocal antecedent atom. |
| (J21)--(J23) | Pass | Mellin modes have the required \(O((1+|t|)/H_j)\) height norm; normalized \(d\)-derivatives are fixed because \(hR/D_j\asymp_{s_0}1\); and the saddle identity is exactly \(4R^2h^2/d_*^2=hq/Y\). |
| (J24) | Pass | The fixed compact multiplier preserves the accepted interior and hard transform hypotheses. Polynomial Mellin-frequency losses are integrable against its Schwartz transform, and the same absolute remainder/cotangent ledger yields the localized normalized bound. |
| (J25) | Pass | It is coefficientwise wherever \(1-V_{\rm low}\ne0\), including the outer star. Full terminal minus localized terminal is exactly the nonlower complement. |

There is no invalid mathematical step in (J5)--(J25). The remaining
corrections are the owner wording after (C8)/(J4), handled by (1.4), and
the rule that endpoint/\(R_1\) modules have multiplicity zero on this
route.

### Campaign controls

| Required control | Outcome |
|---|---|
| literal_global_radial_coefficient | Pass: (2.1)--(2.2) retain the exact \(h q=n\), odd-\(q\), \(\chi_4(q)\), \(H_j+1\), and profile coefficient. |
| external_X_one_quarter_normalization | Pass: normalized \(X^\varepsilon\) becomes physical \(X^{1/4+\varepsilon}\) only through (2.3). |
| fixed_radial_partition_one_count | Pass after (1.4): lower, every fixed compact cell, and \(U\) sum exactly to one; no auxiliary terminal aggregate is treated as a fourth flat cell. |
| compact_critical_transfer_scope | Pass: only fixed \(V_a\) and the fixed \(\lambda V_{\rm low}\) are passed to compact Mellin transfer; neither reaches \(16\). |
| upper_endpoint_prefix_coefficient | Pass as a nonidentification: the physical prefix has the same \(\mathcal C_X^*\) and stars but constant phase \(e(\sqrt{XN})\), so it is not deleted from \(U\). |
| endpoint_boundary_and_R1_routing | Pass: lower prefix, upper prefix, and recombined \(R_1\) are counted once only in their accepted transformed boundary operator; the two transition traces remain excluded from that operator. |
| radial_collar_vs_boundary_prefix | Pass: the collar has \(A_X(n/Y)e(\sqrt{Xn})\), not the prefix multiplier \(e(\sqrt{XN})\). |
| flat_support_edge_and_cutoff_seminorms | Pass: (3.12)--(3.15) price lattice length and arbitrary-order flatness; no unsupported \(C\uparrow16\) or shrinking-cutoff critical theorem is used. |
| floor_star_product_tie_hard_sample | Pass: (3.3), (3.7), and (3.11) are atomwise with \(H_j=\lfloor D_j/R\rfloor\); all half weights are unchanged and bounded only in (3.15). |
| physical_limit_vs_finite_height | Pass: no endpoint theorem is extended to finite top height. The terminal proof uses the accepted physical stationary transforms; the endpoint and \(R_1\) results retain their symmetric-limit scope. |
| alpha_route_nonduplication | Pass: alpha and beta are assigned multiplicity zero in the physical radial partition. |
| lower_parent_disjointness | Pass: \(V_{\rm low}\mathcal C_X^*\) is never estimated; only the auxiliary, compactly supported \(V_{\rm low}\mathcal C_{T,X}^*\) is bounded and subtracted. |
| downstream_scope | Pass: the result closes only the interface parent; it proves neither GAR nor any blockwise M1/M2 or endpoint-uniformity theorem. |

No numerical experiment and no new literature theorem were used. The
control work was entirely analytical/algebraic.

## 6. Dependencies and exact artifacts used

Mathematical dependencies from the accepted graph are:

- M9-M1-global-angular-recombination for (2.1)--(2.3);
- M9-M1-terminal-frequency-divisor-bound for (3.2)--(3.4);
- M9-M1-top-endpoint-transform and the accepted smooth positive-frequency
  transform for (3.5), including the hard cotangent boundary;
- M9-M2-dyadic-weight-nondegeneracy for the exact active profiles,
  (3.3), and the unique hard sample;
- H4-Phi-regularity for the height-weight variation;
- M9-M1-smooth-critical-radial-terminal-transfer for the fixed compact
  pieces and its Mellin-separated terminal proof;
- M9-M1-global-radial-one-count-assembly for the exact implication
  (1.4);
- M9-M1-upper-radial-endpoint-prefix,
  M9-M1-endpoint-boundary-operator, and
  M9-M1-R1-arithmetic-residue only for the coefficient/owner
  reconciliation, not as estimates inserted into (1.2).

Exact artifacts read and used were:

- AGENTS.md;
- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0821_full_proof_strategy.md;
- rounds/codex-managed/m9-m1-route-interface-assembly/synthesis.md;
- rounds/codex-managed/m9-m1-route-interface-assembly/reviews/conductor_round98_partition_and_route_scope.md;
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/synthesis.md;
- rounds/codex-managed/m9-m1-upper-endpoint-character-abel/synthesis.md;
- rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md;
- rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/derivation_packet.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md;
- rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/reviews/conductor_round120_terminal_height_adjudication.md.

No Round-120 sibling report, unlisted strategy artifact, numerical output,
or external source was used.

## 7. Recommended state effect

Promote, after the two wording corrections in Section 4. The recommended
patch is:

1. promote the terminal-height aggregate (1.1), its support identities
   (3.7)--(3.8), and the exact nonlower-complement identity (1.2) as a new
   proved internal lemma;
2. promote M9-M1-global-radial-interface-estimate using the exact
   subtraction (1.4), not by identifying (120.C8) literally with the
   Round-98 interface;
3. optionally promote the polynomially shrinking flat-collar lemma (2.7)
   as a subsidiary finite-support statement, while retaining the rejection
   of unpriced \(C\uparrow16\) compact-cutoff limits;
4. leave the proved upper prefix, endpoint boundary operator, and
   recombined \(R_1\) nodes unchanged and retain their physical-limit-only
   scope;
5. leave M9-M1-global-lower-radial-signed-estimate open. It becomes the
   sole remaining analytic parent of GAR under the Round-98 radial
   assembly.

Nothing in this report proves GAR itself, the alternative total-M1 bridge,
blockwise M9-M1, any of the three open M9-M2 parents, endpoint uniformity,
M9, or the Gauss-circle quarter target. The internal \(1/3\) exponent and
the separately audited external benchmark therefore remain unchanged.

# Round 165 focused kernel review: parity normalization and maximal scale

## 1. Result

**GREEN after four exact textual repairs; no mathematical repair is
required.**

The current terminal kernel correctly incorporates the earlier repairs:

1. equation (165.K7a) has the exact odd-\(R\) parity normalization;
2. \(g=(d,d')\) is explicitly the character-divisor gcd,
   \(s=(m,m')\) is the cofactor gcd, and \(G_0\) is used only as a
   numerical high-gcd threshold;
3. the high-gcd owner is explicitly the opened divisor-incidence sector,
   not a unique partition of product rows; and
4. equation (165.K17a) is the correct combined even-shift,
   opposite-tangent, low-divisor-gcd open frontier.

The maximal-scale implication is also correct. At \(R=M_L\), the
parity connector removes all odd medium/long shifts, (165.K25) pays the
short even shifts, and (165.K26) pays exactly the remaining even
medium/long aggregate. Consequently,

\[
 \mathfrak E_{M_L}^{(2)}\ll_\eta L^3X^\eta,\qquad
 \mathfrak E_{M_L}\le 2\mathfrak E_{M_L}^{(2)},
\tag{165.Q1}
\]

and the accepted sliding inequality gives the residual scalar target
after applying the energy estimates with \(\eta=2\varepsilon\).

Four textual repairs remain:

1. define \(Y_s^{(\epsilon)}\) explicitly by absolute site parity
   \(s+j\equiv\epsilon\pmod2\);
2. state (165.K7a) only for \(R=2S+1\ge3\), or define the zero-length
   convention, and write its inner sum as \(j=0,\ldots,T-1\);
3. exclude the open equation (165.K17a) from the status paragraph's
   range of equations said to be proved internally; and
4. replace the phrase “standard epsilon relabelling” by the explicit
   maximal-scale chain and \(\eta=2\varepsilon\).

The earlier malformed \(\mathfrak E_{M_L}^{(2)}ll\) text has already
been repaired. The present \(g,s,G_0\) notation is unambiguous and should
be retained.

## 2. Exact statement and hypotheses

Let \(z=(z_N)_{N\in\mathbb Z}\) be any finitely supported complex
sequence and \(R\ge1\) an integer. Define

\[
 Y_s=\sum_{j=0}^{R-1}z_{s+j},\qquad
 Y_s^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j}
 \quad(\epsilon=0,1),
\tag{165.Q2}
\]

\[
 \mathfrak E_R={1\over R}\sum_s|Y_s|^2,\qquad
 \mathfrak E_R^{(2)}={1\over R}\sum_s
 \left(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\right).
\tag{165.Q3}
\]

Then

\[
 \mathfrak E_R^{(2)}
 =D_L+2\Re\sum_{1\le q<R/2}
 \left(1-{2q\over R}\right)\sum_Nz_{N+2q}\overline{z_N},
\tag{165.Q4}
\]

and

\[
 \mathfrak E_R\le2\mathfrak E_R^{(2)}.
\tag{165.Q5}
\]

For \(T\ge1\), put

\[
 \mathcal E_T(w)={1\over T}\sum_{k\in\mathbb Z}
 \left|\sum_{j=0}^{T-1}w_{k+j}\right|^2.
\tag{165.Q6}
\]

If \(x_n=z_{2n}\), \(y_n=z_{2n+1}\), and \(R=2S+1\ge3\), then

\[
\boxed{
 \mathfrak E_{2S+1}^{(2)}
 ={S+1\over2S+1}
   \{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}
 +{S\over2S+1}
   \{\mathcal E_S(x)+\mathcal E_S(y)\}.}
\tag{165.Q7}
\]

For \(R=2S\),

\[
 \mathfrak E_{2S}^{(2)}
 =\mathcal E_S(x)+\mathcal E_S(y).
\tag{165.Q8}
\]

The kernel's current arithmetic notation is safe:

\[
\begin{aligned}
 &g=(d,d'),\quad d=gu,\quad d'=gv,\quad r=gh
 &&\text{(character-divisor gcd)},\\
 &s=(m,m'),\quad m=su,\quad m'=sv,\quad r=sh
 &&\text{(cofactor gcd)},\\
 &G_0
 &&\text{(numerical threshold only)}.
\end{aligned}
\tag{165.Q9}
\]

Thus (165.K17) is precisely

\[
 |\mathfrak C_{R_0,g\ge G_0}^{\rm rem}|
 \ll_\eta {L^3\over G_0}X^\eta
 \qquad(1\le G_0<R_0).
\tag{165.Q10}
\]

At maximal scale, write \(M=M_L\), \(R_0=\lceil L\rceil\), and

\[
 \mathfrak C_M^{(2)}
 =\mathfrak C_{M,<R_0}^{(2)}
  +\mathfrak C_{M,\ge R_0}^{(2)}.
\tag{165.Q11}
\]

Equation (165.K26) is exactly the open hypothesis

\[
 \Re\mathfrak C_{M,\ge R_0}^{(2)}
 \ll_\eta L^3X^\eta.
\tag{165.Q12}
\]

## 3. Proof or derivation

### 3.1 Odd-\(R\) parity normalization

Let \(R=2S+1\). A window starting at \(2k\) contains a length-\(S+1\)
window \(x_k,\ldots,x_{k+S}\) and a length-\(S\) window
\(y_k,\ldots,y_{k+S-1}\). A window starting at \(2k+1\) contains a
length-\(S+1\) window \(y_k,\ldots,y_{k+S}\) and a length-\(S\) window
\(x_{k+1},\ldots,x_{k+S}\). Every subsequence-window start occurs once.
Therefore

\[
\begin{aligned}
 \sum_s\left(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\right)
 ={}&(S+1)\{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}\\
 &+S\{\mathcal E_S(x)+\mathcal E_S(y)\}.
\end{aligned}
\tag{165.Q13}
\]

Dividing by \(2S+1\) proves (165.Q7). A subsequence pair at gap
\(q<S\) has coefficient

\[
 {S+1-q\over2S+1}+{S-q\over2S+1}
 =1-{2q\over2S+1}.
\tag{165.Q14}
\]

The terminal pair \(q=S\), corresponding to the original even gap
\(2S=R-1\), occurs only in the length-\(S+1\) energy and has exact
weight \(1/(2S+1)=1/R\). Hence the current (165.K7a) is normalized
correctly.

The sole endpoint defect is textual: the current statement says “for odd
\(R=2S+1\)” while defining \(\mathcal E_T\) only by division by \(T\).
At \(R=1\), it therefore prints \(0\cdot\mathcal E_0\), with
\(\mathcal E_0\) undefined. Replacing the phrase by
“for odd \(R=2S+1\ge3\)” resolves the issue; (165.K7)--(165.K9)
themselves remain valid at \(R=1\).

Equation (165.Q5) follows pointwise from

\[
 Y_s=Y_s^{(0)}+Y_s^{(1)},\qquad
 |A+B|^2\le2(|A|^2+|B|^2).
\tag{165.Q15}
\]

This uses parity of the absolute site \(s+j\), not parity of the local
window index \(j\). The current proof says “absolute even and odd sites,”
but the definition before (165.K7) should print (165.Q2) explicitly.

### 3.2 Gcd roles and the combined low-gcd frontier

The current notation distinguishes the exact equations

\[
 g(vm'-um)=r
\tag{165.Q16}
\]

and

\[
 s(vd'-ud)=r.
\tag{165.Q17}
\]

They are different reindexings: the divisor-gcd row has frozen character
\(\chi_4(uv)\), while the cofactor-gcd row has the parity-dependent law
in (165.K21). Using \(G_0\) only for the threshold prevents either gcd
from being confused with the cutoff. No renaming is now needed.

The proof of (165.K17) is unchanged. For fixed \(g\), there are
\(O(L/g)\) choices for each of \(u,v,h\) and \(O(g)\) points on the row.
Thus the contribution is \(O(L^3/g^2)\), and summation over
\(g\ge G_0\) gives \(O(L^3/G_0)\). The current kernel also correctly says
that this is owner-complete for opened divisor incidences rather than a
unique partition of product rows.

To verify the newly inserted (165.K17a), decompose the even-shift
correlation at \(R_0\) after the literal opening:

\[
\begin{aligned}
 \Re\mathfrak C_{R_0}^{(2)}
 ={}&\Re\mathfrak C_{R_0,2,\rm mon}^{\rm rem}
 +\Re\mathfrak C_{R_0,2,\rm opp,\,g\ge\gamma L}^{\rm rem}\\
 &+\Re\mathfrak C_{R_0,2,\rm opp,\,g<\gamma L}^{\rm rem}.
\end{aligned}
\tag{165.Q18}
\]

The negative monotone and one-zero negative tangent sectors are empty.
Equation (165.K12) bounds the first displayed term in modulus by \(O(L^2)\);
(165.K17) bounds the second in modulus by
\(O_{\gamma,\eta}(L^2X^\eta)\); and (165.K17a) is the asserted one-sided
bound for the third. Therefore (165.K17a) implies the complete even-shift
bound, then (165.K9), (165.K8), and (165.K6) imply the residual scalar
target. The combined frontier is correct and remains open.

### 3.3 Maximal-scale parity plus short payment

For every fixed shift, zero-extended Cauchy gives

\[
 \left|\sum_Nz_{N+r}\overline{z_N}\right|\le D_L.
\tag{165.Q19}
\]

Since every Fejer weight is between zero and one, (165.K25) implies the
more precise even short payment

\[
 |\mathfrak C_{M,<R_0}^{(2)}|
 \le\sum_{\substack{1\le r<R_0\\2\mid r}}
 \left(1-{r\over M}\right)
 \left|\sum_Nz_{N+r}\overline{z_N}\right|
 \le(R_0-1)D_L
 \ll_\eta L^3X^\eta.
\tag{165.Q20}
\]

Assuming (165.K26), equivalently (165.Q12), the exact parity energy is

\[
\begin{aligned}
 \mathfrak E_M^{(2)}
 &=D_L+2\Re\mathfrak C_{M,<R_0}^{(2)}
       +2\Re\mathfrak C_{M,\ge R_0}^{(2)}\\
 &\le D_L+2|\mathfrak C_{M,<R_0}^{(2)}|
       +2\Re\mathfrak C_{M,\ge R_0}^{(2)}
 \ll_\eta L^3X^\eta.
\end{aligned}
\tag{165.Q21}
\]

No odd medium/long term is missing, because

\[
 \mathfrak E_M\le2\mathfrak E_M^{(2)}
 \ll_\eta L^3X^\eta.
\tag{165.Q22}
\]

If \(M\) is odd, (165.K7a) shows explicitly that the final even gap
\(M-1\) is present with weight \(1/M\); it lies in exactly one of the two
ranges in (165.Q11). If \(M\) is even, the largest even gap is \(M-2\),
again covered exactly once. Thus the cutoff loses neither an endpoint nor
a Fejer weight.

At \(R=M\), (165.K6) becomes

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le{2M-1\over M}\mathfrak E_M
 <2\mathfrak E_M
 \ll_\eta L^3X^\eta.
\tag{165.Q23}
\]

Invoke (165.K3), (165.K25), and the hypothesis (165.K26) with
\(\eta=2\varepsilon\) before taking the square root. Then

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{165.Q24}
\]

This verifies the implication of (165.K26), including all factors \(2\),
the parity elimination, odd-\(M\) endpoint, and epsilon bookkeeping.

## 4. First doubtful or unproved step

There is no doubtful step in the current odd-\(R\) formula, the
\(g,s,G_0\) distinction, the high-gcd count, the implication of
(165.K17a), or the implication of (165.K26).

The first unproved statements remain the boxed actual-direction estimates
(165.K17a) and (165.K26). The kernel proves that each is sufficient on its
respective scale; it does not estimate either aggregate.

There is one proof-status contradiction in the current final paragraph.
It says that “Equations (165.K14)--(165.K25)” are proved internally, a
range which syntactically includes the open inserted equation (165.K17a),
and then correctly says two sentences later that (165.K17a) is open.
The exact repair is to write:

“Equations (165.K4)--(165.K12), (165.K14)--(165.K17), and
(165.K18)--(165.K25) are proved internally; the implications from the
boxed open estimates are proved.”

The estimate in (165.K17a) itself must remain explicitly open.

## 5. Control tests and outcomes

| Focused control | Outcome |
|---|---|
| absolute-site parity | **GREEN after definition insertion.** Use \(s+j\equiv\epsilon\pmod2\). |
| odd-\(R\) normalization | **GREEN.** Current (165.K7a) has the correct convex coefficients. |
| \(R=1\) edge of (165.K7a) | **REPAIR.** Restrict that displayed formula to \(R\ge3\) or define \(0\mathcal E_0=0\). |
| odd terminal gap | **GREEN.** Gap \(R-1\) has exact weight \(1/R\). |
| divisor gcd | **GREEN.** Current \(g=(d,d')\) is explicitly character-divisor gcd. |
| cofactor gcd | **GREEN.** Current \(s=(m,m')\) is separate and has its own progression. |
| threshold | **GREEN.** Current \(G_0\) is used only as the numerical cutoff. |
| high-gcd owner | **GREEN.** Current text scopes ownership to opened divisor incidences. |
| combined frontier (165.K17a) | **GREEN implication, OPEN estimate.** Decomposition (165.Q18) proves sufficiency. |
| proof-status range | **REPAIR.** The present (K14)--(K25) range accidentally includes open (K17a). |
| \(R=M_L\) short payment | **GREEN.** (165.K25) is stronger than (165.Q20). |
| (165.K26) range and weights | **GREEN.** Every even \(R_0\le r<M_L\) occurs with \(1-r/M_L\). |
| odd medium/long shifts | **GREEN elimination.** They do not occur in \(\mathfrak E_{M_L}^{(2)}\). |
| maximal-scale factors | **GREEN.** Equations (165.Q21)--(165.Q23) retain both factors \(2\). |
| epsilon relabelling | **GREEN after textual expansion.** Use \(\eta=2\varepsilon\) before square root. |
| downstream scope | **GREEN quarantine.** No parent or exponent is promoted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This focused review used exactly:

1. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/parity_connector_high_gcd_review.md; and
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/variable_scale_fejer_bypass_review.md.

No shared state, sibling report, external source, web lookup, computation,
or numerical experiment was used.

## 7. Recommended state effect

**Retain the current kernel mathematics and apply only these textual
repairs:**

1. replace the prose definition before (165.K7) by the explicit
   absolute-site formula (165.Q2);
2. change “For odd \(R=2S+1\)” to “For odd \(R=2S+1\ge3\)” and define
   \(\mathcal E_T\) with \(0\le j<T\);
3. replace the proved-equation range in the status paragraph by
   (165.K4)--(165.K12), (165.K14)--(165.K17), and
   (165.K18)--(165.K25), thereby excluding open (165.K17a); and
4. replace “standard epsilon relabelling” by the explicit chain
   (165.Q21)--(165.Q24), with \(\eta=2\varepsilon\).

Keep the current \(g,s,G_0\) notation, the incidence-owner sentence, and
the combined open frontier (165.K17a); all are correct.

After these repairs, the parity connector, dual gcd forms, high-gcd
sector, and implications from (165.K17a) and (165.K26) are suitable for
promotion subject to the conductor's remaining graph checks. Keep
(165.K17a), (165.K26), the complete residual, full \(t=1\) face, every
other few-point channel, both hard-TOP parents, BAL, UNBAL, smooth M2,
M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter theorem,
and both global exponents open.

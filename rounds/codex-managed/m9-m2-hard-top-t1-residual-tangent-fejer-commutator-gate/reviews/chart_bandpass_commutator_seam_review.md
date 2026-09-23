# Round 173 chart/bandpass/commutator seam review

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Reviewed candidate: candidates/formalized_tangent_fejer_commutator_self_return_obstruction.md
- Starting graph: 70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Scope: chart, parity, character, bandpass, incidence power, finite split, and reindexing only
- Verdict: **REPAIR**

## 1. Result

The mathematical kernel is correct after one local exact-statement repair.
The opened-incidence chart is a bijection; negative coordinates are lawful;
the odd--odd and squarefree even--even parity ledgers, character sign,
factor \(2\), and one-outer-real-part convention are correct. The bandpass
is continuous at \(0,R,T\) and globally \(1/T\)-Lipschitz, hence also
\(1/R\)-Lipschitz, including a strict terminal non-doubling link. The
repaired literal hypotheses give the claimed
\(O_\varepsilon(L^3X^\varepsilon)\) complete commutator after epsilon
rebudgeting. The finite split and adjacent-sum self-return have exactly the
candidate's constants and signs.

The repair is that the displayed “complete link” uses an unqualified
\(\sum_{d,m,v,s}\), although the even-gap link requires
\(v\in2\mathbb Z\). It also leaves the base domain and the character-free
definition of \(G\) implicit. Read literally, the display includes odd
physical gaps and is false. The repair is local and does not alter the
self-return conclusion.

## 2. Literal hypotheses, chart, parity, and character

The repaired statement-only packet and accepted Round-164/165/172 kernels
supply, on each nonzero atom,

\[
 N=dm\asymp L^2,\qquad d,m\asymp L,\qquad
 |\lambda_N(d)|\ll X^\eta,
\]

with \(X^{O(\eta)}\) active opened divisors. Every selector, no-pair
value, squarefree/coprimality hole, two-adic branch, profile, floor, star,
crossing, endpoint, point value, and zero extension stays in \(\lambda\).
Thus the arbitrary \(d=N,m=1\) and unbounded cancelling-opening examples
in the pre-repair blind report are not literal counterexamples. They
remain valid erased-structure controls.

For an ordered opened incidence,

\[
 N=dm,\quad N'=d'm',\quad
 s=\frac{d'-d}{2},\quad v=m'-m.
\]

Because \(d,d'>0\) are odd, \(s\in\mathbb Z\). Conversely
\(d'=d+2s\), \(m'=m+v\) recovers the incidence uniquely whenever both
factors are positive and literal. The chart is therefore multiplicity one
at the opened-divisor-pair level; divisor multiplicity at the physical
\((N,N')\) level is retained. Negative \(s\) and \(v\) are lawful under
the same positivity and literal-support test.

Direct expansion gives

\[
 r_s=(d+2s)(m+v)-dm=dv+2s(m+v),\qquad
 r_{s+1}-r_s=2(m+v)=2m'.
\]

Moreover

\[
 r_s=d'm'-dm\equiv m'-m=v\pmod2,
\]

so an even gap is equivalent to even \(v\). In the odd--odd branch,
\(m,m'\) are odd and \(v\) is even. In the squarefree even--even branch,
\(m=2u,m'=2u'\) with \(u,u'\) odd, and hence

\[
 4\mid v=2(u'-u),\qquad 4\mid r_s=dv+2sm'.
\]

There is no mixed-product-parity branch at even gap. Finally,

\[
 \chi_4(d+2s)=(-1)^s\chi_4(d),\qquad
 \chi_4(d+2s)\chi_4(d)=(-1)^s,
\]

also for negative \(s\).

## 3. First issue and exact repair

Define, before evaluating any square root,

\[
 G_{d,m,v}(s)=
 \lambda_{(d+2s)(m+v)}(d+2s)
 \overline{\lambda_{dm}(d)}
 e\!\left(J\left(\sqrt{(d+2s)(m+v)}-\sqrt{dm}\right)\right)
\]

when both opened atoms are positive and literal, and define it as \(0\)
otherwise. The character is excluded from \(G\), since it has already
become \((-1)^s\). The candidate's complete-link display should be
replaced by

\[
 \boxed{
 \Delta_{R,T}=2\Re
 \sum_{\substack{d>0\ \mathrm{odd},\ m\ge1\\
                  v\in2\mathbb Z,\ s\in\mathbb Z}}
 (-1)^s\beta_{R,T}(r_s)G_{d,m,v}(s).}
\]

This fixes the first issue. The factor \(2\) comes from the positive-gap
real correlation, opening the coefficients introduces no additional
factor, and the real part remains outside the complete signed sum.

## 4. Bandpass and terminal-link audit

For \(R<T\le2R\), the two nonzero slopes are

\[
 \frac{T-R}{RT}=\frac1R-\frac1T,\qquad -\frac1T.
\]

The values match at every gate:

\[
 \beta(0)=0,\quad
 \beta(R^-)=\frac{T-R}{T}=1-\frac RT=\beta(R^+),\quad
 \beta(T)=0.
\]

Since \(T\le2R\), \((T-R)/(RT)\le1/T\). Therefore

\[
 |\beta_{R,T}(x)-\beta_{R,T}(y)|
 \le\frac{|x-y|}{T}\le\frac{|x-y|}{R}
\]

globally, including steps crossing \(0,R,T\). On nonzero literal support,
\(m'\asymp L\), so

\[
 |\beta(r_s)-\beta(r_{s+1})|
 \le\frac{2m'}T\ll\frac LR.
\]

No doubling identity was used, so this is valid for the strict final link
\(R<T<2R\).

## 5. Incidence count and epsilon rebudget

If \(G(s)\ne0\) and
\(\beta(r_s)-\beta(r_{s+1})\ne0\), at least one of
\(r_s,r_{s+1}\) lies in \((0,T)\). Since
\(r_{s+1}-r_s=2m'=O(L)\) and \(R\ge R_0\asymp L\),

\[
 -O(L)<r_s<T.
\]

This is an \(O(R)\)-length signed-gap interval. There are \(O(L^2)\)
possible base product sites, hence \(O(RL^2)\) relevant ordered physical
pairs, including negative-starting-gap atoms created by the split. The
two divisor openings and two opened weights contribute only
\(X^{C_0\eta}\) for some fixed \(C_0\). Thus

\[
 \sum_{\beta(r_s)\ne\beta(r_{s+1})}|G_{d,m,v}(s)|
 \ll RL^2X^{C_0\eta}
\]

and

\[
 |\mathcal C_{R,T}|
 \ll \frac LR\,RL^2X^{C_0\eta}
 \ll L^3X^{C_0\eta}.
\]

There are \(O(\log L)\) stopped-chain links. Since
\(L\le H\le X^{1/4}\), choose \(\eta\) sufficiently small in terms of
the requested \(\varepsilon\), then absorb \(\log L\) into another
arbitrarily small power of \(X\). Consequently

\[
 \sum_j|\mathcal C_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon.
\]

The power conclusion is sound. Adding the signed-gap interval and this
explicit rebudget to the candidate would make the proof self-contained.

## 6. Finite split and reindexing constants

Literal zero extension makes \(H_s=\beta(r_s)G(s)\) finitely supported.
Hence

\[
 2\sum_s(-1)^sH_s
 =\sum_s(-1)^s(H_s-H_{s+1}).
\]

Expanding gives, with no endpoint term,

\[
 \Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\]

\[
 \begin{aligned}
 \mathcal C_{R,T}
 &=\Re\sum_s(-1)^s(\beta_s-\beta_{s+1})G_s,\\
 \mathcal R_{R,T}
 &=\Re\sum_s(-1)^s\beta_{s+1}(G_s-G_{s+1}).
 \end{aligned}
\]

Reindexing only the \(G_{s+1}\) term by \(t=s+1\) gives

\[
 \begin{aligned}
 \mathcal R_{R,T}
 &=\Re\sum_s(-1)^s\beta_{s+1}G_s
   -\Re\sum_t(-1)^{t-1}\beta_tG_t\\
 &=\boxed{\Re\sum_s(-1)^s(\beta_s+\beta_{s+1})G_s}.
 \end{aligned}
\]

Thus the sign is plus, there is no factor \(1/2\), and

\[
 \mathcal C_{R,T}+\mathcal R_{R,T}
 =2\Re\sum_s(-1)^s\beta_sG_s=\Delta_{R,T}.
\]

The accepted identity
\[
 T_{26}=\frac12\sum_j\Delta_{R_j,R_{j+1}}-B_{\rm short}
\]
then yields exactly
\[
 \sum_j\mathcal R_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})
  -\sum_j\mathcal C_{R_j,R_{j+1}}.
\]

The candidate's factor \(2\), sign of \(B_{\rm short}\), single outer real
part, and self-return conclusion all pass.

## 7. Control matrix and proposed disposition

| Seam/control | Ruling |
|---|---|
| repaired literal near-square class | **GREEN** |
| opened-incidence bijection and negative coordinates | **GREEN** |
| odd--odd and squarefree even--even parity | **GREEN** |
| character sign | **GREEN** |
| factor \(2\) and one outer real part | **GREEN** |
| displayed link domain | **REPAIR:** write \(v\in2\mathbb Z\) and the full base domain |
| character-free definition of \(G\) | **REPAIR for exactness** |
| beta slopes, cusps, and global Lipschitz | **GREEN** |
| strict terminal non-doubling link | **GREEN** |
| complete incidence count | **GREEN after the explicit ledger above** |
| epsilon rebudget | **GREEN** |
| finite split and birth/death accounting | **GREEN** |
| adjoint reindexing constants | **GREEN** |

**Proposed repair:** insert the definition and boxed sum from Section 3;
optionally add the signed-gap incidence line and state that \(\eta\) is
chosen after \(\varepsilon\). After those local edits this seam is GREEN.
No downstream state-scope issue was found within the assigned audit.

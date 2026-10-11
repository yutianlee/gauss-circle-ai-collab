# Round 225: isolated scalar-envelope rederivation

## 1. Result

The infimum is attained uniquely, and
\[
 \boxed{
 C_*(\nu)=
 \begin{cases}
 (26+13\nu)/336,&0\le\nu\le26/71,\\
 (26+55\nu)/504,&26/71\le\nu\le3/2.
 \end{cases}}
 \tag{1}
\]
The scalar envelope has unique global maximizer and value
\[
 \boxed{\nu_{\max}=226/307,\qquad
 \max_{0\le\nu\le3/2}H(\nu)=81/614.}
 \tag{2}
\]
For every fixed \(1/8<\beta<27/208\),
\[
 \boxed{
 \max_\nu\min(\beta,H(\nu))=\beta,\qquad
 \{\nu:H(\nu)>\beta\}
 =\left(\frac{504\beta-26}{55},\,1-2\beta\right).}
 \tag{3}
\]
The interval in (3) is nonempty.

This is an independent current statement-only derivation by a reused agent. Earlier roles and the prior finite-convolution report remain in retained history; this is not history-free work. For this task I read only the assigned scalar packet and protocol, and the prior report remains unchanged. No application or conductor derivation was read.

## 2. Exact hypotheses

For real \(0\le\nu\le3/2\) and \(0\le k\le\nu\), the supplied functions are
\[
 A(\nu)=\nu/4,\qquad D(\nu)=(1-\nu)/2,
\]
\[
 C(\nu,k)=\max\left(\nu/4-k/2,\,
                 13/168+13\nu/336+k/4\right),
\quad
 H(\nu)=\min(A(\nu),D(\nu),C_*(\nu)).
\]
There is no positivity truncation of \(D\) or \(H\), and none is inserted. Every optimization is over the stated closed interval. The parameter \(\beta\) is fixed and lies in the stated open interval.

## 3. Proof and crossover derivation

### The minimization in \(k\)

The first affine function of \(k\) has slope \(-1/2\); the second has slope \(1/4\). Their intersection is
\[
 k_0(\nu)=\frac{71\nu-26}{252}.
 \tag{4}
\]
For \(\nu<26/71\), the intersection is negative. Already at \(k=0\) the increasing branch dominates, and it continues to dominate for all \(k\ge0\). The unique minimum is therefore \(k=0\).

For \(\nu\ge26/71\), \(k_0\ge0\), and
\[
 \nu-k_0=\frac{181\nu+26}{252}>0.
\]
Thus the intersection is admissible and never crosses the upper boundary \(k=\nu\). Below \(k_0\) the maximum is the decreasing branch, and above it the maximum is the increasing branch. Consequently
\[
 k_*(\nu)=
 \begin{cases}
 0,&0\le\nu\le26/71,\\
 (71\nu-26)/252,&26/71\le\nu\le3/2.
 \end{cases}
 \tag{5}
\]
Substitution gives (1). At the shared endpoint the values agree:
\[
 C_*(26/71)=13/142=A(26/71).
\]
Continuity and compactness also show directly that the requested infimum is a minimum.

### The lower envelope in \(\nu\)

For \(0\le\nu\le26/71\),
\[
 C_*(\nu)-A(\nu)=\frac{26-71\nu}{336}\ge0.
\]
For \(\nu\ge26/71\),
\[
 A(\nu)-C_*(\nu)=\frac{71\nu-26}{504}\ge0.
\]
The crossing of \(A\) and \(D\) is \(\nu=2/3\), which is greater than \(26/71\). Hence \(A\) controls the envelope on the whole first regime.

In the second regime,
\[
 D(\nu)-C_*(\nu)=\frac{226-307\nu}{504}.
\]
Its unique zero is \(\nu=226/307\), within that regime. Thus
\[
 \boxed{
 H(\nu)=
 \begin{cases}
 \nu/4,&0\le\nu\le26/71,\\
 (26+55\nu)/504,&26/71\le\nu\le226/307,\\
 (1-\nu)/2,&226/307\le\nu\le3/2.
 \end{cases}}
 \tag{6}
\]
The two increasing slopes are positive, and the last slope is negative. This proves the unique maximum (2). At the maximizer,
\[
 k_*=32/307,\qquad
 A=113/614,\qquad C_*=D=81/614.
\]

The crossing \(A=D\) at \(2/3\) is not a controlling crossover: \(C_*\) is strictly smaller there. Equating \(D\) with the first formula for \(C_*\) gives the formal value \(142/181\), outside that formula's regime, so it creates no additional crossover. The only controlling switches of \(H\) are \(26/71\) and \(226/307\).

### The fixed cap \(\beta\)

The exact comparisons
\[
 \frac{13}{142}<\frac18<\frac{27}{208}<\frac{81}{614}
 \tag{7}
\]
place every allowed \(\beta\) above the first crossover height and below the global maximum. For the last comparison, \(81=3\cdot27\) and \(3\cdot208=624>614\).

The increasing branch reaches \(\beta\) at
\[
 \ell_\beta=\frac{504\beta-26}{55},
\]
and the decreasing branch reaches it at
\[
 r_\beta=1-2\beta.
\]
The condition from \(A>\beta\) is weaker: indeed
\[
 \ell_\beta-4\beta=\frac{284\beta-26}{55}>0
\]
because \(\beta>13/142\). Moreover,
\[
 r_\beta-\ell_\beta=\frac{81-614\beta}{55}>0.
 \tag{8}
\]
Equations (6)--(8) prove that \(H>\beta\) exactly on the open interval in (3), and \(H\ge\beta\) exactly on its closure. The capped envelope attains its maximum \(\beta\) at every point of \([\ell_\beta,r_\beta]\), and nowhere else.

## 4. First unproved step and scope

There is no unproved step in this scalar optimization. No mathematical quantity other than the supplied functions has been estimated.

If an unprovided quantity has upper bounds whose exponents are this menu, (2) describes the menu's optimized worst exponent and (3) describes the same menu after the additional fixed cap. It does not prove a lower bound for that quantity, show that any upper bound is attained, or exclude a better estimate using information absent from the packet. In particular, an interval where \(H>\beta\) is a limitation of these scalar expressions, not an actual-value lower bound.

## 5. Exact controls and outcomes

At the requested control point,
\[
 \nu=\frac23,\qquad k_*=\frac{16}{189},\qquad
 C_*=\frac{47}{378},\qquad A=D=\frac16.
 \tag{9}
\]
Thus \(H(2/3)=47/378\), and
\[
 \frac{47}{378}<\frac18<\beta<
 \frac{27}{208}<\frac{81}{614}.
 \tag{10}
\]
The first inequality is \(47\cdot8=376<378\). Hence this one value does not locate the global maximum or determine the capped worst value.

The limiting intervals at the two specified \(\beta\)-endpoints are
\[
 \begin{array}{c|c|c}
 \beta&(\ell_\beta,r_\beta)&r_\beta-\ell_\beta\\ \hline
 1/8&(37/55,\ 3/4)&17/220\\
 27/208&(205/286,\ 77/104)&27/1144.
 \end{array}
 \tag{11}
\]
Both widths are positive. The formulas would therefore remain valid at those two endpoints if the allowed \(\beta\)-range were closed. Within the specified open range, the intervals shrink as \(\beta\) increases and always contain \(226/307\). Their left endpoints exceed \(2/3\), since already \(37/55>2/3\). At the different limiting value \(\beta=81/614\), the strict-superlevel interval would become empty and the maximizing set would reduce to \(226/307\); that value is outside the requested \(\beta\)-range.

Other endpoint controls are
\[
 \begin{array}{c|c|c|c}
 \nu&k_*&C_*&H\\ \hline
 0&0&13/168&0\\
 26/71&0&13/142&13/142\\
 226/307&32/307&81/614&81/614\\
 1&5/28&9/56&0\\
 3/2&161/504&217/1008&-1/4.
 \end{array}
 \tag{12}
\]
In particular the negative terminal value is retained. The function \(C_*\) itself is increasing and reaches \(217/1008\) at \(3/2\); this is distinct from the global maximum of \(H\) in (2).

All controls are exact rational calculations and monotonicity arguments. No plots, decimal sampling or experiments were used.

## 6. Exact inputs and provenance

Campaign: gc-complete-logarithmic-convolution. Round: 225. Role: independent_envelope_rederivation. This is a new statement-only scalar task after the prior finite report was frozen.

Exactly two input files were read:

| Input | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/gc-complete-logarithmic-convolution/briefs/blind_envelope_statement.md | 5007a095cdbc780a2ada7063438bcaf74f85f72d8a988264c150ec3ebfbbf815 |

Prior agent history is disclosed in Section 1. No application, graph, other report, conductor derivation or external source was read. No prior artifact was edited. All reasoning is analytical, and this review is the sole output.

## 7. Recommended state effect

Retain (1)--(3) and their exact controls as independently rederived scalar evidence. No application estimate, actual lower bound, analytic promotion or successor follows. Preserve the prior frozen report and all shared state. Stop after freezing this review.

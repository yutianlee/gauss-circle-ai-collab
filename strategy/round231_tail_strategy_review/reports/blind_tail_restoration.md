# Round231: isolated distribution-to-moment audit

## 1. Result

**Conditional lemma, with sharp abstract exponent.** Put
\[
p=136/13,\quad q=12-p=20/13,\quad
b=\frac{50\sqrt{1717}-297}{13762},\quad
K_0=10b,\quad K_1=1+qb.
\]
Here \(b=0.128966351948\ldots\), \(K_0=1.289663519481\ldots>K_1=1.198409772228\ldots\).
For nonnegative savings \(a,d\), the exact complete-moment exponent supplied by the hypotheses is
\[
\boxed{\alpha(\gamma,a,d)=\max\{m(\gamma),\,10b-a,\,1+qb-d\}.}
\]
Thus \(M_{12}(B)\ll_\varepsilon T^{\alpha+\varepsilon}\). This is an upper-bound theorem; it does not assert that any specific arithmetic function attains this exponent.

## 2. Exact statement and hypotheses

Take fixed real \(\gamma\), fixed \(a,d\ge0\), \(T\ge2\), measurable \(F,E\), \(B=F+E\), and a nonnegative measure \(\mu_T\) with \(\mu_T(\Omega)\ll T\). Assume, for every \(\eta>0\), with constants independent of \(T,V\),
\[
D_F(V)\ll_\eta T^\eta(V^{-2}+TV^{-p})\quad(V\ge1),
\qquad \|F\|_{L^\infty(\mu_T)}\ll_\eta T^{b+\eta},
\]
\[
M_{12}(E)\ll_\eta T^{m(\gamma)+\eta},\qquad
m(\gamma)=\max(1,10\gamma,1+q\gamma),
\]
and the conjectured strengthened estimate
\[
D_F(V)\ll_\eta T^\eta(T^{-a}V^{-2}+T^{1-d}V^{-p})
\quad(V\ge T^\gamma).
\]
If negative \(a,d\) are allowed, replace the boxed exponent by
\[
\max\{m(\gamma),\min(K_0,\max(K_0-a,K_1-d))\}.
\]
No arithmetic assertion that the strengthened estimate holds is assumed proved.

## 3. Proof and derivation

Let \(H=\max(1,T^\gamma)\) and \(S=C_\eta T^{b+\eta}\) be an essential ceiling. Layer cake gives
\[
M_{12}(F)=12\int_0^\infty V^{11}D_F(V)\,dV.
\]
The part below 1 is \(O(T)\). Up to \(\min(H,S)\), the original estimate gives at most
\[
O_\eta\bigl(T^\eta(H^{10}+TH^q)+T\bigr)
\ll_\eta T^{m(\gamma)+\eta}.
\]
Above \(H\), if this interval is nonempty, the strengthened estimate integrates to
\[
O_\eta\left(T^{\eta-a}S^{10}+T^{1+\eta-d}S^q\right).
\]
The exact primitives are \((S^{10}-H^{10})/10\) and \((S^q-H^q)/q\); both powers are positive, so there is no logarithmic endpoint. Independently, the original estimate bounds this same integral by
\(O_\eta(T^\eta S^{10}+T^{1+\eta}S^q)\). Taking the better estimate proves the general formula in section 2. For \(a,d\ge0\), the minimum is redundant because \(K_0>K_1\).

If \(H\ge S\), the upper integral vanishes. In particular, \(\gamma>b\) offers no improvement over the ceiling bound for \(F\); the displayed complete exponent remains valid since \(m(\gamma)\ge K_0\). At \(\gamma=b\), the possible \(T^\eta\) ceiling strip is covered by the same estimates. Constants in \(S\) contribute only fixed multiplicative constants.

For an actual truncated moment, the exact identity is
\[
\int_{|F|>H}|F|^{12}\,d\mu_T
=H^{12}D_F(H)+12\int_H^\infty V^{11}D_F(V)\,dV.
\]
The boundary term is at most
\(O_\eta(T^\eta(H^{10}+TH^q))\), already absorbed by \(m(\gamma)\). Omitting it is invalid when identifying a truncated moment with a tail integral.

Given a requested final \(\varepsilon\), use all input estimates with \(\eta=\varepsilon/30\); the largest ceiling loss is \(11\eta\). Finally,
\(M_{12}(B)\le2^{11}(M_{12}(F)+M_{12}(E))\).

For any target \(r\ge m(\gamma)\), this also proves the **moment upper-bound equivalence**
\[
M_{12}(B)\ll_\varepsilon T^{r+\varepsilon}
\iff M_{12}(F)\ll_\varepsilon T^{r+\varepsilon},
\]
using \(F=B-E\) for the reverse implication. Literal distribution bounds do not transfer unchanged: only
\[
D_B(V)\le D_F(V/2)+2^{12}V^{-12}M_{12}(E)
\]
is automatic, with the strengthened \(F\)-bound available there for \(V\ge2T^\gamma\). The reverse inequality has the analogous error term.

## 4. First doubtful or unproved step

The sole new unproved premise is the strengthened tail estimate itself. The integration proves its conditional consequence, not its arithmetic validity. No conclusion about the actual open tail bound is made.

## 5. Required controls and outcomes

For a target \(r\ge1\), the necessary and sufficient exponent conditions within these abstract assumptions are
\[
\gamma\le\min\{r/10,13(r-1)/20\},\quad
a\ge(K_0-r)_+,\quad d\ge(K_1-r)_+.
\]

| Target | Largest threshold exponent | Minimum \(a\) | Minimum \(d\) | First term alone? |
|---|---:|---:|---:|---|
| \(32/25\) | \(16/125\) | \(10b-32/25=0.009663519481\ldots\) | 0 | Yes |
| \(29/25\) | \(13/125\) | \(10b-29/25=0.129663519481\ldots\) | \(20b/13-4/25=0.038409772228\ldots\) | No |

The requested triples pass:
\[
\alpha(16/125,1/100,0)
=\max(1.28,1.279663519481\ldots,1.198409772228\ldots)=32/25,
\]
\[
\alpha(13/125,13/100,1/25)
=\max(1.16,1.159663519481\ldots,1.158409772228\ldots)=29/25.
\]

**Sharpness control (analytic).** The \(m(\gamma)\) obstruction is attained by \(F=0\), \(\mu_T(\Omega)=T\), and constant \(E=T^{(m(\gamma)-1)/12}\). When the tail exponent dominates \(m(\gamma)\), necessarily \(\gamma<b\). Set \(x=cT^b\), put \(F=x\) on an atom of mass
\[
w=\min\{x^{-2}+Tx^{-p},\ T^{-a}x^{-2}+T^{1-d}x^{-p}\},
\]
and \(F=0\) on a remainder of mass \(T\), with \(E=0\). Monotonicity in \(V\) verifies both tail estimates, and \(x^{12}w\) has precisely the stated tail exponent. Thus neither savings minimum can be reduced from these assumptions alone. In particular \(d=0\) permits the second-term obstruction \(K_1>29/25\), regardless of the first-term saving.

**Weaker sufficient target.** For any admissible \(\gamma\) with \(m(\gamma)\le r\), it suffices to prove only
\[
\boxed{\int_{T^\gamma}^{\infty}V^{11}D_F(V)\,dV
\ll_\varepsilon T^{r+\varepsilon}.}
\]
Together with the baseline below the threshold and the boundary bound, this gives the complete moment. It requires no separate pointwise savings in the two summands.

## 6. Dependencies and exact artifacts used

Role: statement-only independent rederivation; campaign: pending Round231; task: blind_tail_restoration. Supplied graph hash: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Generated UTC: `2026-10-11T14:58:48.8473108Z`.

Read only `protocol.md` and `strategy/round231_tail_strategy_review/briefs/blind_tail_restoration.md`; graph/manifest reads were explicitly waived for isolation. Dependencies are solely the hypotheses in section 2. No sources or sibling reports used. Numerical work: one bounded PowerShell evaluation of the displayed radical and savings; illustrative only. All controls and conclusions are analytical.

## 7. Recommended state effect

**Retain** the conditional restoration arithmetic, with the ceiling, boundary, and transfer qualifications above. **No change** to the status of any actual arithmetic tail estimate or downstream target. This report supplies isolated evidence for conductor review, not a graph promotion.

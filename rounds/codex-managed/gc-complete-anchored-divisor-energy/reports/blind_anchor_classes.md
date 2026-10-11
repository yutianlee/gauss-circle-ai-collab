# Round219 statement-only anchored radical classes

## 1. Result

**Verdict: GREEN for the exact classification and energy identities below. No character cancellation follows from the supplied hypotheses alone.**

The correct relation on anchors is

\[
 j\sim k\quad\Longleftrightarrow\quad R_j^2/R_k^2\in\mathbb Q_{>0}.
 \tag{1}
\]

Every equivalence class has a unique primitive integer representation

\[
 R_j=S_{\mathcal A}\sqrt{q_j}\quad(j\in\mathcal A),\qquad
 q_j\in\mathbb Z_{>0},\qquad \gcd_{j\in\mathcal A}q_j=1.
 \tag{2}
\]

Within that anchor class, the exact frequency groups are indexed by the common integer label \(\ell=q_jd\). Different anchor classes cannot share a frequency.

The full exact energy is

\[
 \boxed{
 E=\sum_{\mathcal A}\sum_{\ell\geq1}
 \left(
  \sum_{\substack{j\in\mathcal A\\q_j\mid\ell\\\ell/q_j\in D}}
  b_j\chi_4(\ell/q_j)h_{j,\ell/q_j}
 \right)^2.
 }
 \tag{3}
\]

All sums are finite after zero terms are discarded. In particular, in the special odd-integer representation supplied in the packet,

\[
 \boxed{
 E=\sum_{\substack{\ell\geq1\\\ell\ {\rm odd}}}
 \left(
  \sum_{\substack{j\\q_j\mid\ell\\\ell/q_j\in D}}
  b_j\chi_4(q_j)h_{j,\ell/q_j}
 \right)^2.
 }
 \tag{4}
\]

The \(\ell\)-dependent character is a common sign before squaring. It does not create cancellation inside that square. General even \(q_j\) admit an equally exact decomposition by their \(2\)-adic valuations, given in (13).

An elementary coherence control attains \(E=J^2\) while \(\sum_{j,d}c_{j,d}^2=J\). Thus a character-based improvement to a diagonal-size energy bound is impossible for arbitrary coefficients in this statement.

## 2. Exact hypotheses and conventions

Let \(J\geq1\), \(R_1,\ldots,R_J>0\), and let \(D\subset\mathbb Z_{>0}\) be finite. The real coefficients \(b_j\) and \(h_{j,d}\) are arbitrary, with

\[
 c_{j,d}=b_j\chi_4(d)h_{j,d}.
 \tag{5}
\]

Here \(\chi_4(d)=0\) for even \(d\), is \(+1\) for \(d\equiv1\pmod4\), and is \(-1\) for \(d\equiv3\pmod4\). It is completely multiplicative, including on even integers, and

\[
 \chi_4(d)^2=\mathbf1_{\{d\ {\rm odd}\}}.
 \tag{6}
\]

The anchor index \(j\) is a label. Repeated numerical anchors are allowed and remain different indices. For a given \(j\), distinct \(d\)'s give distinct frequencies.

An anchor equivalence class in (1) describes which anchors can share frequencies for some positive integer labels. Actual common frequencies for the specified finite set \(D\) require the divisibility and membership conditions in (3); commensurable anchors need not have a collision for a particular \(D\).

The word primitive in (2) means only that the joint gcd of the integers \(q_j\) is one. It does not mean that the \(q_j\) are squarefree or pairwise coprime. Every energy and character formula also holds in a nonprimitive integer representation, provided its common scale and integer labels are used consistently.

Since all coefficients are real, the squared absolute values in the question equal the ordinary squares appearing in (3)--(4). No limit, approximation, cancellation assumption, or size restriction on these finite data is used.

## 3. Proof and complete character algebra

### Anchor classes and their primitive representation

For any two positive integer labels \(d,e\),

\[
 R_j\sqrt d=R_k\sqrt e
 \quad\Longleftrightarrow\quad
 R_j^2/R_k^2=e/d.
 \tag{7}
\]

Thus a collision implies (1). Conversely, if \(R_j^2/R_k^2=u/v\) in lowest positive integer terms, then \(d=v\), \(e=u\) give a collision when these labels are allowed. Positive rational ratios of the squared anchors form an equivalence relation.

Fix one class and an anchor \(R_*\) in it. Write \(R_j^2/R_*^2=u_j/v_j\) in lowest terms and set \(L=\operatorname{lcm}_j v_j\). Then \(Q_j=Lu_j/v_j\) are positive integers, and

\[
 R_j=(R_*/\sqrt L)\sqrt{Q_j}.
 \tag{8}
\]

If \(g=\gcd_jQ_j\), put \(q_j=Q_j/g\) and \(S_{\mathcal A}=R_*\sqrt{g/L}\). This proves existence in (2).

For uniqueness, two primitive integer representations would have \(q'_j=tq_j\) for a common positive rational \(t=a/b\) in lowest terms. Integrality forces \(b\) to divide every \(q_j\), so \(b=1\). The gcd condition on the \(q'_j\) then forces \(a=1\). The integers and the positive scale therefore agree.

At a common frequency within this class,

\[
 R_j\sqrt d=S_{\mathcal A}\sqrt{q_jd}.
 \tag{9}
\]

Hence its exact labels are \(\ell\in\bigcup_{j\in\mathcal A}q_jD\), and its participating pairs are precisely those in (3). If two different anchor classes shared a frequency, (7) would put their participating anchors in the same class, a contradiction. Summing the squares of the class coefficients proves (3).

### Gcd-sensitive pair parametrization

For \(j,k\) in a common class, let

\[
 g_{jk}=\gcd(q_j,q_k),\qquad
 A_{jk}=q_k/g_{jk},\qquad B_{jk}=q_j/g_{jk}.
 \tag{10}
\]

Then \(\gcd(A_{jk},B_{jk})=1\), and

\[
 q_jd=q_ke
 \quad\Longleftrightarrow\quad
 d=A_{jk}t,\quad e=B_{jk}t,\quad t\in\mathbb Z_{>0}.
 \tag{11}
\]

The common label is
\(\ell=\operatorname{lcm}(q_j,q_k)t=q_jq_kt/g_{jk}\).
No coprimality of \(q_j,q_k\) themselves was assumed.

Expanding the squares in (3) and using complete multiplicativity gives the equivalent exact ordered-pair identity

\[
 \boxed{
 E=\sum_{\mathcal A}\sum_{j,k\in\mathcal A}
 b_jb_k\chi_4(A_{jk}B_{jk})
 \sum_{\substack{t\geq1,\ t\ {\rm odd}\\
                 A_{jk}t\in D,\ B_{jk}t\in D}}
 h_{j,A_{jk}t}h_{k,B_{jk}t}.
 }
 \tag{12}
\]

Indeed,
\(\chi_4(A_{jk}t)\chi_4(B_{jk}t)
 =\chi_4(A_{jk}B_{jk})\chi_4(t)^2\).
The sum over \(j,k\) is ordered, so cross terms already have their correct multiplicity. When \(j=k\), \(A_{jk}=B_{jk}=1\), and (12) gives the exact diagonal
\(\sum_jb_j^2\sum_{d\in D,\ d\ {\rm odd}}h_{j,d}^2\).

### Even integer labels and the exact valuation split

Write \(q_j=2^{v_j}u_j\), where \(u_j\) is odd. For a common label write \(\ell=2^v m\), with \(m\) odd. A participating coefficient can be nonzero only if

\[
 v=v_j,\qquad u_j\mid m,\qquad d=m/u_j\in D.
\]

If \(v>v_j\), the label \(d=\ell/q_j\) is even and its character is zero. If \(v<v_j\), divisibility fails.

In the nonzero case, complete multiplicativity on odd integers gives
\(\chi_4(m/u_j)=\chi_4(m)\chi_4(u_j)\).
Therefore the general energy is exactly

\[
 \boxed{
 E=\sum_{\mathcal A}\sum_{v\geq0}
       \sum_{\substack{m\geq1\\m\ {\rm odd}}}
 \left(
  \sum_{\substack{j\in\mathcal A\\v_j=v\\u_j\mid m\\m/u_j\in D}}
  b_j\chi_4(u_j)h_{j,m/u_j}
 \right)^2.
 }
 \tag{13}
\]

This explains precisely how even anchor labels are handled. One must not divide by \(\chi_4(q_j)\) or replace an even \(q_j\)'s contribution by zero: its odd quotient \(d\) can have nonzero character.

Equivalently, in (12) the cross term vanishes identically when \(v_j\ne v_k\), since \(A_{jk}B_{jk}\) is then even. If \(v_j=v_k\), both reduced integers are odd and
\(\chi_4(A_{jk}B_{jk})=\chi_4(u_j)\chi_4(u_k)\).
Thus (12) and (13) give the same exact split.

### Special odd-integer anchors

Now assume the packet's special representation \(R_j=S\sqrt{q_j}\) with all \(q_j\) positive odd integers, not necessarily primitive or coprime. For every integer \(\ell\) divisible by \(q_j\),

\[
 \chi_4(\ell/q_j)=\chi_4(\ell)\chi_4(q_j).
 \tag{14}
\]

For odd \(\ell\), this follows by multiplying
\(\chi_4(\ell)=\chi_4(q_j)\chi_4(\ell/q_j)\)
by \(\chi_4(q_j)\). For even \(\ell\), both sides of (14) are zero. Thus the coefficient at \(S\sqrt\ell\) is

\[
 C_\ell
 =\chi_4(\ell)
   \sum_{\substack{j\\q_j\mid\ell\\\ell/q_j\in D}}
     b_j\chi_4(q_j)h_{j,\ell/q_j}.
 \tag{15}
\]

Squaring (15) proves (4).

A common odd divisor causes no alteration of this identity. If all \(q_j=gq'_j\) with \(g\) odd and \(\ell=g\ell'\), then
\(\chi_4(\ell)\chi_4(q_j)
 =\chi_4(\ell')\chi_4(q'_j)\),
because \(\chi_4(g)^2=1\).
Thus reducing a nonprimitive odd representation and replacing the scale by \(S\sqrt g\) preserves every coefficient.

### Rational ratios of the anchors themselves

If \(R_j/R_k=a/b\) with coprime positive integers \(a,b\), then the exact integer solutions to the collision equation are

\[
 d=b^2t,\qquad e=a^2t,\qquad t\geq1.
 \tag{16}
\]

If \(a,b\) are both odd, then

\[
 \chi_4(b^2t)=\chi_4(a^2t)=\chi_4(t).
 \tag{17}
\]

Thus the two character factors are identical at every collision; their product is \(+1\) for odd \(t\). Cancellation could still come from the arbitrary real \(b_jh_{j,d}\), but does not come from these character factors.

If one of \(a,b\) is even, one of \(d,e\) is even at every collision, so the character-weighted cross term is zero. There can still be geometric collisions.

Conversely, irrational anchor ratios do not imply noncommensurability: \(1\) and \(\sqrt3\) have irrational ratio but rational squared ratio, and share the frequency \(\sqrt3\) at labels \(3\) and \(1\).

### What a character-cancellation hypothesis would need to say

For an odd common label define the active signed weights

\[
 W_{j,\ell}=b_jh_{j,\ell/q_j}
             \mathbf1_{\{q_j\mid\ell,\ \ell/q_j\in D\}},
\quad
 A_+(\ell)=\sum_{q_j\equiv1\ (4)}W_{j,\ell},
\quad
 A_-(\ell)=\sum_{q_j\equiv3\ (4)}W_{j,\ell}.
\]

Then the exact inner sum in (4) is

\[
 A_+(\ell)-A_-(\ell).
 \tag{18}
\]

Exact cancellation at that frequency is equivalent to
\(A_+(\ell)=A_-(\ell)\).
A sufficient quantitative cancellation hypothesis, beyond the packet, would be a uniform weighted balance such as

\[
 |A_+(\ell)-A_-(\ell)|
 \leq \delta\sum_j|W_{j,\ell}|,
 \qquad 0\leq\delta<1,
 \tag{19}
\]

or a corresponding square-summed imbalance bound over \(\ell\). When the weights are nonnegative, (19) is an explicit weighted equidistribution condition between the two odd residue classes, after imposing the exact divisibility and \(D\)-membership conditions. Counting residue classes without controlling these weights would not suffice. The appropriate general even-anchor version applies separately to each valuation stratum and to the odd parts \(u_j\) in (13).

No condition of this kind follows from arbitrary \(b_j,h_{j,d}\). In fact, for odd \(q_j\), replacing the arbitrary \(b_j\) by \(b_j\chi_4(q_j)\) is a bijection on the space of real coefficient vectors. The fixed anchor signs can therefore always be absorbed into unrestricted coefficients. The common factor \(\chi_4(\ell)\) disappears in the energy.

### A sharp elementary energy comparison

Let \(J_*=\max_{\mathcal A}|\mathcal A|\). At any frequency there is at most one label \(d\) for each anchor \(j\), hence at most \(J_*\) contributing pairs. Cauchy--Schwarz at each frequency gives

\[
 0\leq E\leq J_*\sum_{j,d}c_{j,d}^2
       =J_*\sum_jb_j^2\sum_{\substack{d\in D\\d\ {\rm odd}}}h_{j,d}^2.
 \tag{20}
\]

The coherence control below attains this factor. A lower bound by the diagonal mass is false in general, as the balanced \(q=1,3\) control also shows.

## 4. First doubtful or unproved step

There is no remaining gap in the finite identities, classification, or controls above.

The first unsupported step in any further character-cancellation claim would be to treat \(\chi_4(\ell/q_j)\) as an independently oscillating factor across the active anchors at a fixed common frequency. Equation (14) instead expresses it as one common sign times fixed anchor signs. A weighted balance or orthogonality assertion such as (19), suitably quantified for the desired conclusion, would require an additional hypothesis and proof.

No application, spacing estimate, near-resonance estimate, or limiting energy bound was supplied or inferred.

## 5. Required controls and outcomes

All controls are exact algebraic arguments. No experiment or numerical computation was performed.

**Coherence with positive coefficients and rational anchors.** Choose distinct positive odd integers \(k_1,\ldots,k_J\), with \(k_1=1\), and let \(Q=\operatorname{lcm}(k_1,\ldots,k_J)\). Set

\[
 R_j=k_j,\qquad
 d_j=(Q/k_j)^2,\qquad
 D=\{d_1,\ldots,d_J\},\qquad
 b_j=1,\qquad h_{j,d}=\mathbf1_{\{d=d_j\}}.
\]

Every \(d_j\) is an odd square, so \(c_{j,d_j}=1\), and
\(R_j\sqrt{d_j}=Q\) for every \(j\).
All nonzero coefficients lie at this one frequency. Thus

\[
 E=J^2,\qquad \sum_{j,d}c_{j,d}^2=J.
 \tag{21}
\]

The primitive integer representation is \(q_j=k_j^2\), \(S=1\), and the common label is \(\ell=Q^2\). This exhibits exact character coherence without using signed \(b_j\) or negative \(h_{j,d}\).

**Noncommensurable anchors.** Take \(R_1=1\), \(R_2=2^{1/4}\). Their squared ratio is irrational, since it is \(1/\sqrt2\). No positive integer \(d,e\) can give \(R_1\sqrt d=R_2\sqrt e\). For any finite \(D\) and any real coefficients,

\[
 E=b_1^2\sum_{\substack{d\in D\\d\ {\rm odd}}}h_{1,d}^2
   +b_2^2\sum_{\substack{d\in D\\d\ {\rm odd}}}h_{2,d}^2.
 \tag{22}
\]

This is exact diagonal energy, not an estimate.

| Additional control | Outcome |
|---|---|
| Irrational ratio but commensurable squared ratio | \(R_1=1,R_2=\sqrt3\), labels \(3,1\), give the same frequency \(\sqrt3\). Restricting anchor classes to rational ratios would miss this collision. |
| Actual cancellation under extra balance | In the preceding \(q_1=1,q_2=3\) example, take \(b_j=1\) and only \(h_{1,3}=h_{2,1}=1\) nonzero. The two coefficients are \(-1,+1\), so \(E=0\) despite diagonal mass \(2\). Changing \(b_2\) to \(-1\) gives \(E=4\). |
| Nontrivial common odd divisor | In the valid nonprimitive representation \(q_1=3,q_2=15\), the common label \(\ell=15\) uses \(d_1=5,d_2=1\). With only these coefficients active and \(b_j=h_{j,d_j}=1\), both characters are \(+1\), giving energy \(4\). The reduced pair labels are \(5t,t\), not \(15t,3t\). |
| Even \(q_j\) with nonzero coefficients | Take the primitive representation \(q=(1,2,10)\), common label \(\ell=10\), and labels \(d=(10,5,1)\). With these active weights all equal to \(1\), the coefficients are \(0,1,1\), and the energy is \(4\). Substituting \(\chi_4(q_j)=0\) for the even anchors would be incorrect. |
| Unequal \(2\)-adic valuations | For \(q_1=1,q_2=2\), a common label uses \(d_1=2t,d_2=t\); the cross character product is always zero. This agrees with both (12) and the separate strata of (13). |
| Rational ratio with odd numerator and denominator | Formula (17) gives identical characters at all collisions. Character coherence is exact; signs of the external real coefficients remain unrestricted. |
| Rational ratio with an even numerator or denominator | Formula (16) forces at least one even label at every collision; its coefficient is zero. This is a character-weighted vanishing, not absence of geometric collisions. |
| Repeated anchors | Equal anchors have equal primitive \(q_j\). The coefficients for each identical \(d\) sum inside one square. They do not become separate diagonal terms merely because their indices differ. |
| Finite set excludes a collision | Even when the squared anchor ratio is rational, there is no contribution from a parameter \(t\) unless both labels in (11) belong to \(D\). |
| Empty or zero data | If \(D\) is empty or every coefficient is zero, all displayed formulas give \(E=0\). Even labels alone also give zero energy. |

## 6. Exact dependencies and provenance

- Campaign: gc-complete-anchored-divisor-energy, round219.
- Task: blind_anchor_classes; statement-only independent derivation of the finite anchored radical lemma.
- Generated date: 2026-09-28, the supplied session date.
- Only context files read for this assignment:
  - protocol.md, SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
  - rounds/codex-managed/gc-complete-anchored-divisor-energy/briefs/blind_anchor_statement.md, SHA256 2182389e0e5d8a8a3630b3ef0b88d016061c68aaa9e7fc7f7e999a32c0de1187.
- No graph hash was supplied in this isolated statement, and no graph, generated brief, manifest, strategy, application, sibling, or historical artifact was read.
- Mathematical dependencies: squaring positive radical equalities, reduction of positive rational numbers, gcd/lcm divisibility, complete multiplicativity of the explicitly defined character modulo \(4\), \(2\)-adic valuation, and finite Cauchy--Schwarz.
- No web search, application access, external theorem, experiment, new agent, shared-state edit, or successor work was used. Only the assigned report was written.

**Prior-history disclosure.** This agent retains prior round217 source/frontier and seam-review context and its own prior round218 abstract radial and packet-coherence work. It is not a fresh history-free agent. For this round219 lemma it had statement-only access: none of the current claimant's derivation, intended application, or sibling work was supplied or inspected. The proof above is derived directly from the stated finite data.

## 7. Recommended state effect

**Recommend promote only the exact anchor classification, label and character-energy identities, and the explicit coherence/noncommensurability controls, subject to the conductor's normal verification procedures.**

Reject any inference that the character alone supplies cancellation for these arbitrary coefficients. Such a conclusion requires an additional weighted balance or orthogonality hypothesis within the precise common-label classes.

No implication for an application, graph mutation, synthesis, or next-round decision is made. The assigned task ends with this report.

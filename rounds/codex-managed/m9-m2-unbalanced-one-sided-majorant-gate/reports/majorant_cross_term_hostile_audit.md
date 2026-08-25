# Hostile audit of the one-sided-majorant/cross-term seam

## 1. Result: majorant_no_go

The proposed mechanism has a lawful placement, but that placement does not by itself produce a bandwidth contraction with surviving factor \(1\). The maximal safe conclusion is this scoped no-go.

> **Scoped majorant no-go.** Let
>
> \[
> F_H(\alpha)=\left|\sum_{0\leq a<H}e(a\alpha)\right|^2
> \]
>
> and let \(T_\Delta\) be a real trigonometric polynomial of degree at most \(\Delta\) satisfying the genuine one-sided order \(T_\Delta(\alpha)\geq F_H(\alpha)\) for every \(\alpha\). If \(t_0=\int_0^1T_\Delta\), then
>
> \[
> t_0\geq \max\left(H,\frac{H^2}{\Delta+1}\right),
> \qquad
> \sum_{|r|\leq\Delta}|t_r|\geq H^2.
> \]
>
> Hence a fixed-power bandwidth contraction, for example \(\Delta+1\leq HX^{-\eta}\), forces diagonal capacity at least \(X^\eta D_0\); a shiftwise absolute-value treatment has coefficient capacity at least \(HD_0\). The only zero-excess case \(t_0=H\) is \(T_\Delta=F_H\), which requires \(\Delta\geq H-1\) and is the original identity. Consequently no proof consisting of a universal one-sided multiplier comparison followed by a positive-diagonal or coefficientwise-absolute closure can establish the claimed survivor \(\Gamma=1\).

This does **not** show that the literal flat-smooth strict-UNBAL energy is large, and it does **not** exclude a new inequality proved only for the literal coefficient family while preserving all signed \(\chi_4\)-cross terms. The surviving mechanism would have to be an actual-family signed theorem: either a target-scale estimate of the lawful P1 right-hand side or a restricted P11 comparison followed by such an estimate. Neither is supplied by universal-majorant terminology, and both are presently unproved.

The relevant notions of order must be kept separate:

1. **Universal PSD order:** domination for every finitely supported complex sequence. For translation-invariant quadratic forms this is equivalent to pointwise multiplier domination \(T_\Delta\geq F_H\).
2. **Coefficientwise cutoff order:** inequalities between individual Fourier coefficients \(t_r\) and \(H-|r|\). This is not quadratic-form order and fails on two complex coordinates (indeed, on two real coordinates).
3. **Actual-family-only order:** an inequality evaluated only at \(A(k)=\sum_p\chi_4(p)b_{p,k}\). It may conceivably hold without universal PSD order, but it must be proved from the displayed phase, character, profiles, zero extension, and endpoints. Universal adversarial tables do not refute it.

### Placement pass/fail matrix

Here “pass” means that the indicated inequality is a valid upper comparison, not that it proves the target.

| ID | Placement of the proposed majorant | Exact order status | Complex cross terms and \(\chi_4\) | Bandwidth/capacity status | Endpoint, owner, and Poisson status | Gate verdict |
|---|---|---|---|---|---|---|
| P1 | In frequency, directly on \(F_H|\widehat A|^2\), after \(A=\sum_p\chi_4(p)b_p\) is formed and before any modulus in \(p\) | **Pass iff** \(T_\Delta\geq F_H\) pointwise (for universal order) | Preserved exactly | \(t_0/H\geq H/(\Delta+1)\); fixed-power degree contraction has a fixed-power diagonal deficit. Absolute modes cost at least \(H\) | Parseval is endpoint-complete under zero extension. Later Poisson still needs a full endpoint ledger | Lawful placement, but **fails as a \(\Gamma=1\) diagonal/absolute closure** |
| P2 | Coefficientwise domination or cutoff of the Fourier coefficients \(H-|r|\) | **Fail**; entrywise coefficient order is not Loewner order | Cross terms can reverse the proposed inequality | No capacity argument can repair the false first inequality | Subsequent Poisson is irrelevant because the input order already fails | **Reject** |
| P3 | Delete high Fejer modes and add coefficientwise corrections | **Fail** unless the corrected polynomial is proved pointwise above \(F_H\), in which case this is P1 | Deleting modes changes signed correlations | A valid pointwise correction is subject to the same \(t_0\) and \(\ell^1\) bounds | Same as P1 after a valid correction | **Reject as a distinct shortcut; reduce to P1 if repaired** |
| P4 | Inside each block square, replace \(1_{[0,H)}(a)\) by a pointwise larger scalar window before summing in \(a\) | **Fail** for complex data unless the new rank-one window is proportional to the old one | Internal cross terms are changed before their modulus | The proportional case has no support/bandwidth gain; diagonal Cauchy domination pays the usual \(H\) | Moving entries/exits must still be retained | **Reject**, except for a gainless scalar rescaling |
| P5 | Outside the square, replace an \(n\)-selector by a nonnegative pointwise majorant | **Pass** as scalar order because the block square is already nonnegative | The already-formed \(\chi_4\)-sum is retained | It enlarges the set/weight of \(n\) and does not contract the internal Fejer bandwidth | New outer tails and endpoints need owners; no automatic Poisson saving | **Lawful but does not address the gate** |
| P6 | Entrywise majorization of the pair kernel in \(a,b\), or of the Toeplitz shift kernel | **Fail** entrywise; **pass only** under Loewner/PSD domination | Off-diagonal complex phases make entrywise order meaningless | Translation-invariant Loewner order is P1. A general high-rank PSD majorant has its own trace/capacity cost | Endpoint restrictions prevent silently replacing the finite kernel by a periodic one | **Reject entrywise; PSD version reduces to an already-audited case** |
| P7 | Majorize \(D_H\), only its main arc, or a level-set approximation | Order on the complex quantity \(D_H\) is undefined. **Pass only** if one proves a global \(T\geq |D_H|^2\) | Partial-arc domination leaves uncontrolled cross-energy in the complement | A global squared multiplier is P1 and obeys the uncertainty bound | Arc tails and transition pieces cannot be dropped without estimates and owners | **Reject partial/unsquared versions; global version is P1** |
| P8 | After expanding in \(p,q\), but before retaining the joint character square | **Fail** if applied separately to entries or signs; **pass only** for a joint PSD operator on the full character-weighted vector | Separate treatment destroys the \(\chi_4(p)\overline{\chi_4(q)}\) cancellation | A translation-invariant joint operator acting only through \(A\) is P1; a genuinely family-specific joint operator is P11 | Arithmetic and endpoint ownership must remain attached to each pair | **Reject separated versions** |
| P9 | After sectorwise modulus, \(p\)-wise triangle/Cauchy, \(E_{\rm eq}\), or the positive-row norm | The scalar inequalities can be valid, but they bound a strictly stronger object | Actual character cancellation has already been erased | The known surviving factor is \(\Gamma_{\rm before}=\min(H,Q)\to\infty\) | Poisson cannot restore discarded signs | **Fail for the claimed survivor** |
| P10 | On reciprocal cutoffs, dual aliases, or stationary packets only after a Poisson rewrite | **Fail** unless the transformed full quadratic form and its order are first justified | Modewise modulus again loses signed character/shift cancellation | Exact Poisson is invertible; triangle costs the coefficient budget, and the strict-interior second transform returns to the primal scale | Principal stationary packets alone are not endpoint-complete | **No independent gain; reject as a substitute for a prior lawful inequality** |
| P11 | A restricted inequality \(Q_{F_H}(A_{\rm lit})\leq Q_T(A_{\rm lit})\) proved only for the literal coefficient family | **Conditional/open**; universal pointwise order is sufficient but not necessary for a single vector/family | Can retain the actual \(\chi_4\)-cross terms if never separated | Must prove a new signed saving cancelling the zeroth/\(\ell^1\) capacity; no such estimate is present | Must include zero extension, moving profiles, all endpoints, and the flat-smooth strict-UNBAL owner | **Only surviving route, presently unproved** |

## 2. Exact statement and hypotheses

Write \(e(x)=e^{2\pi i x}\). Let \(H\geq2\), let \(A:\mathbb Z\to\mathbb C\) be finitely supported, and put

\[
D_H(\alpha)=\sum_{a=0}^{H-1}e(a\alpha),\qquad
F_H(\alpha)=|D_H(\alpha)|^2
=\sum_{|r|<H}(H-|r|)e(r\alpha).
\]

For a real integrable multiplier \(G\), define

\[
Q_G(A)=\int_0^1G(\alpha)|\widehat A(\alpha)|^2\,d\alpha,
\qquad
\widehat A(\alpha)=\sum_k A(k)e(k\alpha).
\]

The literal sequence in this round is

\[
A(k)=\sum_{\substack{p>0\\p\ {\rm odd}}}\chi_4(p)b_{p,k},
\]

where \(b_{p,k}\) is exactly the frozen flat-smooth strict-UNBAL coefficient and is zero-extended before every shift. Then

\[
E_\chi=C_HQ_{F_H}(A).
\]

Let

\[
T_\Delta(\alpha)=\sum_{|r|\leq\Delta}t_re(r\alpha),
\qquad t_{-r}=\overline{t_r},
\]

be real of degree at most \(\Delta\). The following claims are exact.

**Lemma A (universal Toeplitz order).** The inequality

\[
Q_{F_H}(A)\leq Q_{T_\Delta}(A)
\tag{2.1}
\]

for every finitely supported complex \(A\) holds if and only if

\[
T_\Delta(\alpha)\geq F_H(\alpha)
\quad(\alpha\in\mathbb R/\mathbb Z).
\tag{2.2}
\]

For a single fixed finite support, the exact condition is positivity of the corresponding finite Toeplitz matrix; pointwise order remains sufficient but need not be necessary. Thus Lemma A is deliberately a universal statement, while P11 is not.

**Lemma B (zeroth-coefficient uncertainty).** Under (2.2),

\[
t_0=\int_0^1T_\Delta(\alpha)\,d\alpha
\geq \max\left(H,\frac{H^2}{\Delta+1}\right).
\tag{2.3}
\]

Moreover \(t_0=H\) is possible if and only if \(T_\Delta=F_H\); in particular it requires \(\Delta\geq H-1\).

**Lemma C (coefficient capacity).** Under (2.2),

\[
\|t\|_{\ell^1}:=\sum_{|r|\leq\Delta}|t_r|
\geq T_\Delta(0)\geq H^2.
\tag{2.4}
\]

Consequently:

- if \(\Delta+1\leq HX^{-\eta}\), then \(t_0/H\geq X^\eta\);
- if \(\Delta+1\leq H^{1-\sigma}\), then \(t_0/H\geq H^\sigma=X^{\sigma(1/2-\delta)+o(1)}\);
- a termwise absolute treatment of all Fourier modes has raw coefficient capacity at least \(\|t\|_1/H\geq H\) relative to \(D_0=C_HH\sum_{p,k}|b_{p,k}|^2\).

The third assertion concerns a closure that discards all cancellation between shift modes. It is not a lower bound for a genuinely signed estimate of the literal family.

**Lemma D (rank-one internal-window order).** For \(u,v\in\mathbb C^H\),

\[
|\langle u,z\rangle|^2\leq|\langle v,z\rangle|^2
\quad\hbox{for every }z\in\mathbb C^H
\tag{2.5}
\]

holds if and only if \(u=\lambda v\) with \(|\lambda|\leq1\). Therefore pointwise domination of the entries of an internal block window does not dominate the resulting complex block square.

All asymptotic consequences use only the frozen range

\[
M\asymp X,\quad D=X^\delta,\quad L=X^\ell,\quad
H=\lceil X^{1/2}/D\rceil,\quad
Q=\frac{D^2}{L\sqrt X}\to\infty,
\]

with \(1/4\leq\delta<1/2\), \(0\leq\ell<\delta-1/4\), and \(178\ell+1638\delta>463\). The conclusion applies only to the flat-smooth strict-UNBAL owner. No assertion is made about hard, sharp, clipped, starred, arithmetic-owner, nonflat, or transition packets.

## 3. Proof and derivation

### 3.1 Literal block square and Parseval

Zero extension is imposed before shifting. Hence, with no boundary convention left implicit,

\[
\sum_p\chi_4(p)B_{p,n}
=\sum_{a=0}^{H-1}\sum_p\chi_4(p)b_{p,n+a}
=\sum_{a=0}^{H-1}A(n+a).
\]

The sequence is finite, so ordinary Parseval gives

\[
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
=\int_0^1F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
\tag{3.1}
\]

This identity already contains every entry and exit of the moving block. No periodic wraparound and no common fixed rectangle may be inserted later without an additional boundary term.

### 3.2 Universal PSD order is pointwise multiplier order

If \(T_\Delta-F_H\geq0\) pointwise, (2.1) follows immediately because \(|\widehat A|^2\geq0\).

Conversely suppose (2.1) holds for every finitely supported complex \(A\). Set \(g=T_\Delta-F_H\). For any \(\alpha_0\), the normalized translated Fejer approximate identity

\[
K_N(\alpha-\alpha_0)
=\frac1N\left|\sum_{j=0}^{N-1}e(j(\alpha-\alpha_0))\right|^2
\]

is \(|\widehat A_N(\alpha)|^2\) for a finitely supported \(A_N\). Universal quadratic-form positivity gives \(\int gK_N\geq0\). Since \(g\) is continuous and \(K_N\) is an approximate identity, letting \(N\to\infty\) yields \(g(\alpha_0)\geq0\). This holds for every \(\alpha_0\), proving (2.2).

This also locates the exact distinction with an actual-family statement: the approximate-identity test vectors are arbitrary coefficient tables and need not occur among the literal \(b_{p,k}\).

### 3.3 Coefficientwise order fails on the first cross term

Expanding a multiplier gives, with the stated Fourier convention,

\[
Q_{T_\Delta}(A)
=\sum_{|r|\leq\Delta}t_r\sum_k A(k)\overline{A(k+r)}.
\tag{3.2}
\]

The inner correlations are complex and have no fixed sign. Increasing an individual real coefficient is therefore not an order operation on the quadratic form.

An explicit two-coordinate falsifier is

\[
T(\alpha)=F_H(\alpha)+\varepsilon(e(\alpha)+e(-\alpha)),
\qquad \varepsilon>0.
\]

The coefficients at \(r=\pm1\) have been increased. Take \(A(0)=1\), \(A(1)=-1\), and \(A(k)=0\) otherwise. Then

\[
Q_T(A)-Q_{F_H}(A)
=2\varepsilon\Re(A(0)\overline{A(1)})
=-2\varepsilon<0.
\tag{3.3}
\]

Thus coefficientwise cutoff order fails before any asymptotic issue, character sum, or endpoint estimate arises. The same example disproves entrywise domination of a Toeplitz pair kernel. The correct replacement is Loewner order; for universal translation-invariant forms, Lemma A identifies it with pointwise multiplier order.

Even a separate requirement that \(T\geq0\) does not rescue coefficientwise order. Put

\[
g(\alpha)=\frac{\varepsilon}{2}+2\varepsilon\cos(2\pi H\alpha),
\qquad T=F_H+g.
\]

The Fourier increments \(g_0=\varepsilon/2\) and \(g_{\pm H}=\varepsilon\) are all nonnegative. At every zero \(j/H\) of \(F_H\), one has \(g(j/H)=5\varepsilon/2>0\). The closure of the set on which \(g<0\) is disjoint from those zeros, so \(F_H\) has a positive minimum there; choosing \(\varepsilon\) sufficiently small makes \(T\geq0\) everywhere. Nevertheless, for \(A(0)=1,A(H)=-1\),

\[
Q_T(A)-Q_{F_H}(A)
=2\left(\frac{\varepsilon}{2}\right)-2\varepsilon
=-\varepsilon<0.
\]

Thus nonnegativity of the proposed polynomial and nonnegative coefficient increments together still do not imply domination of the complex quadratic form.

### 3.4 The zeroth-coefficient uncertainty bound

Under (2.2), \(T_\Delta\geq F_H\geq0\). By Fejer--Riesz factorization there are \(c_0,\ldots,c_\Delta\) such that

\[
T_\Delta(\alpha)
=\left|\sum_{j=0}^{\Delta}c_je(j\alpha)\right|^2.
\]

Consequently

\[
t_0=\sum_{j=0}^{\Delta}|c_j|^2,
\qquad
T_\Delta(0)=\left|\sum_{j=0}^{\Delta}c_j\right|^2
\leq(\Delta+1)t_0.
\]

But \(T_\Delta(0)\geq F_H(0)=H^2\), so

\[
t_0\geq\frac{H^2}{\Delta+1}.
\]

Integrating \(T_\Delta\geq F_H\) separately gives \(t_0\geq\int F_H=H\), proving (2.3). If \(t_0=H\), the continuous nonnegative function \(T_\Delta-F_H\) has integral zero and is therefore identically zero. Since the coefficient of \(e((H-1)\alpha)\) in \(F_H\) is \(1\), its degree is exactly \(H-1\). Conversely \(T_\Delta=F_H\) attains equality whenever the allowed degree is at least \(H-1\).

Thus \(F_H\) is already band-limited at precisely the only zero-excess degree. Lowering the degree by a fixed power is possible only by raising the average, and hence the zeroth correlation coefficient, by the reciprocal fixed power.

### 3.5 Diagonal and \(\ell^1\) capacity

At the frequency origin,

\[
\sum_{|r|\leq\Delta}|t_r|
\geq\left|\sum_{|r|\leq\Delta}t_r\right|
=T_\Delta(0)\geq H^2,
\]

which proves (2.4). For comparison, the Fejer coefficients themselves have

\[
\sum_{|r|<H}(H-|r|)=H^2.
\]

Therefore even the uncontracted exact multiplier has \(\ell^1\)-mass \(H^2\): its useful size \(H\) comes from retaining the signed correlation structure, not from a termwise estimate.

The diagonal normalization in the frozen problem is

\[
D_0=C_HH\sum_{p,k}|b_{p,k}|^2.
\]

After expansion in \(p,q\), the \(r=0,p=q\) part of \(C_HQ_T(A)\) has size

\[
C_Ht_0\sum_{p,k}|b_{p,k}|^2
=\frac{t_0}{H}D_0.
\tag{3.4}
\]

The other \(p,q,r\) terms can be signed and can cancel (3.4); hence (3.4) is not a lower bound for the literal \(Q_T(A)\). It is, however, an exact capacity obstruction for a closure that keeps the positive diagonal and takes absolute values of the remaining correlations. It is also forced by the universal one-row control, in which all \(p\ne q\) terms vanish. If \(\Delta+1\leq HX^{-\eta}\), such a closure begins with \(X^\eta D_0\), which cannot prove an \(X^\varepsilon D_0\) bound for every \(\varepsilon>0\).

Similarly, a modewise triangle estimate that assigns each shift correlation its natural diagonal scale has coefficient budget

\[
\frac{\|t\|_1}{H}D_0\geq HD_0.
\tag{3.5}
\]

Equation (3.5) does not forbid a signed joint estimate of the modes. It proves that “band-limit and then take moduli mode by mode” contains no saving.

### 3.6 Internal and external physical selectors

For Lemma D, suppose (2.5) holds. Any \(z\) orthogonal to \(v\) must also be orthogonal to \(u\); hence \(\ker v^*\subseteq\ker u^*\), so \(u=\lambda v\). Substitution into (2.5) gives \(|\lambda|\leq1\). The converse is immediate.

Apply this with \(u=(1,\ldots,1)\), representing the literal block sum, and \(v\) a proposed internal majorant window. Coordinatewise inequalities such as \(v_a\geq u_a\) do not imply proportionality. If \(v\) is not proportional to \(u\), one can choose \(z\perp v\) but \(\langle u,z\rangle\ne0\); the proposed majorant square is then zero while the literal square is positive. If \(v\) is proportional, the change is only a scalar enlargement and cannot shorten support or bandwidth. A high-rank diagonal domination obtained from Cauchy--Schwarz is lawful, but it pays the familiar factor \(H\) and eliminates the cross-term mechanism under investigation.

By contrast, after the square is formed, \(1_I(n)\leq m(n)\) with \(m\geq0\) lawfully gives

\[
\sum_n1_I(n)|S_n|^2\leq\sum_nm(n)|S_n|^2.
\]

This enlarges an outer selector; it neither changes \(D_H\) nor lowers its degree. It is therefore irrelevant to the requested internal bandwidth contraction unless supplemented by another theorem, and all newly admitted outer tails require endpoint ownership.

### 3.7 Character retention and adversarial coefficient controls

P1 retains the character because the order is applied only after

\[
A(k)=\sum_p\chi_4(p)b_{p,k}
\]

has been formed. Any triangle inequality in \(p\), any replacement by \(|\chi_4(p)|\), or any passage to separate positive rows occurs too early and destroys the very \(p\ne q\) terms that might cancel the capacity in (3.4).

Two analytic coefficient-table controls show why this distinction is necessary.

- **Opposite-character rows.** Choose odd \(p_+\equiv1\pmod4\) and \(p_-\equiv3\pmod4\), and set \(b_{p_+,k}=b_{p_-,k}=c_k\), all other rows zero. Then \(A(k)=c_k-c_k=0\) and \(E_\chi=0\), while separate row block energies are nonzero and, for a long constant plateau \(c_k\), are of order \(HD_0\).
- **Single coherent row.** Keep only one row and take \(c_k\) constant on a long interval. Away from the two ends, each block sum is \(Hc\), so \(E_\chi\asymp HD_0\).

These are deliberately adversarial coefficient tables, **not** instances of the frozen oscillatory \(b_{p,k}\). The first proves that a character-erasing norm can be much larger than the target; the second proves that positivity plus the accepted diagonal estimate cannot give a coefficient-uniform \(\Gamma=1\) theorem. Neither asserts that the literal family realizes either extreme. Random-sign intuition is likewise only a heuristic: it cannot replace a deterministic estimate for the displayed \(\chi_4\)-weighted phase.

### 3.8 Poisson is not the missing noninvertible step

The exact finite Fourier expansion is

\[
C_HQ_T(A)
=C_H\sum_{|r|\leq\Delta}t_r
  \sum_kA(k)\overline{A(k+r)}.
\tag{3.6}
\]

Poisson summation applied to a complete smooth sum inside (3.6) is an equality once all dual frequencies, endpoint pieces, and remainder terms are retained. It does not turn the larger quadratic form into a smaller one and it does not erase the capacity in \(t_0\). For \(T=F_H\), (3.6) is exactly the original Fejer identity. The accepted Round 125 strict-interior analysis further records that the reciprocal principal packet returns to the primal one after the second \(B\)-process: it is a change of variables, not a noninvertible saving.

There are only two ways a later step can cease to be invertible here:

1. take absolute values or Cauchy bounds, in which case the \(\ell^1\), diagonal, or \(\min(H,Q)\) capacity reappears; or
2. truncate dual modes or discard endpoints, in which case a new error theorem and exact owner ledger are required.

Zero extension makes the support of the \(r\)-correlation in (3.6) the exact intersection of the original support with its \(r\)-translate. The factor \(W((X/(2D))\sqrt{p/(M(k+r))})\) is evaluated at the shifted variable, and any reindexing in \(p\) also moves the \(q_L((X/M)p)\) profile. Entry/exit intervals, endpoint stationary or Fresnel regimes, nonstationary tails, dual truncation errors, and Poisson remainders cannot be replaced by one fixed rectangular range. The permitted Round 125 evidence certifies the principal strict-interior self-return, not an endpoint-complete new upper bound for (3.6).

### 3.9 Surviving-factor ledger

The genuinely different outcomes are:

| Closure | Surviving factor forced or known |
|---|---:|
| Separate positive-row / character-erasing elementary estimate | \(\Gamma_{\rm before}=\min(H,Q)\to\infty\) |
| Universal direct majorant of degree \(\Delta\), then positive diagonal/absolute cross-term closure | \(\Gamma\geq H/(\Delta+1)\); in particular \(\Gamma\geq X^\eta\) if \(\Delta+1\leq HX^{-\eta}\) |
| Shiftwise modulus/triangle after any lawful direct majorant | raw coefficient capacity \(\Gamma\geq H\) |
| \(T=F_H\), degree \(H-1\) | \(\Gamma=1\) only as the original identity, with no contraction or new estimate |
| New actual-family joint signed correlation theorem | \(\Gamma=1\) is logically possible but currently unproved |

Both \(H=X^{1/2-\delta+o(1)}\) and \(Q=X^{2\delta-\ell-1/2}\) tend to infinity in the frozen strict range. Thus the pre-existing character-erasing factor cannot be relabelled as \(1\).

## 4. First doubtful or unproved step

For coefficientwise, entrywise-kernel, internal-window, partial-arc, or post-character-separation proposals, the **first step is false**: the asserted one-sided order is not an order on the exact complex quadratic form.

For the only universally lawful placement P1, the first unproved step comes immediately after the comparison. One would need a joint signed estimate of

\[
C_H\sum_{|r|\leq\Delta}t_r
\sum_{k,p,q}\chi_4(p)\overline{\chi_4(q)}
b_{p,k}\overline{b_{q,k+r}}
\tag{4.1}
\]

at \(X^{1/2+\varepsilon}\) scale that:

- retains the actual \(\chi_4(p)\overline{\chi_4(q)}\) signs before every modulus;
- recovers the reciprocal \(t_0/H\) or \(\|t\|_1/H\) capacity created by the low bandwidth;
- handles the \(r=0\), \(p=q\) term together with, rather than separately from, the signed cross terms;
- uses the literal square-root phase and moving \(W,q_L\) profiles;
- includes zero-extension entries/exits, stationary and nonstationary endpoints, all dual modes and remainders; and
- stays inside the flat-smooth strict-UNBAL owner.

No such estimate appears in the permitted artifacts. Calling (4.1) “Poisson” does not prove it, since complete Poisson is reversible and the known strict-interior reciprocal calculation self-returns. If instead the intended assertion is only \(Q_{F_H}(A_{\rm lit})\leq Q_T(A_{\rm lit})\) for the displayed literal family without pointwise \(T\geq F_H\), then that restricted inequality itself is the first unproved step. It cannot be justified by universal PSD language, coefficientwise cutoff order, or the adversarial controls above.

## 5. Required control tests and outcomes

All controls below are analytic. “Adversarial” means a coefficient-table falsifier of a universal claim, not an assertion about the literal oscillatory family.

| Required control | Type | Outcome |
|---|---|---|
| literal_Echi_block_square_and_parseval | Literal identity | **Pass.** Zero extension gives \(E_\chi=C_H\sum_n|\sum_{a<H}A(n+a)|^2=C_HQ_{F_H}(A)\) with no wraparound. |
| majorant_order_relation | Universal analytic test | **Pass only for pointwise/PSD order.** For all finite complex sequences, \(Q_T\geq Q_F\) iff \(T\geq F\) pointwise. A fixed finite support only requires its finite Toeplitz matrix to be PSD. |
| Fejer_already_bandlimited | Exact algebra | **Obstruction confirmed.** \(F_H\) has degree \(H-1\), integral \(H\), and coefficient \(1\) at the top frequency. \(T=F_H\) is the unique zero-integral-excess majorant. |
| zeroth_coefficient_uncertainty_bound | Universal analytic theorem | **Pass.** Fejer--Riesz plus Cauchy gives \(t_0\geq H^2/(\Delta+1)\), while integration gives \(t_0\geq H\). |
| bandwidth_and_L1_excess_capacity | Universal analytic theorem | **Fail for the proposed gain.** \(\|t\|_1\geq T(0)\geq H^2\); fixed-power contraction forces fixed-power diagonal excess, and modewise modulus has at least \(H\) raw excess. |
| complex_cross_term_domination | Adversarial two-coordinate control | **Fail for coefficientwise/entrywise order.** With \(T-F=2\varepsilon\cos(2\pi\alpha)\) and \(A=(1,-1)\), the quadratic-form difference is \(-2\varepsilon\). |
| actual_chi4_before_modulus | Literal structural audit | **Pass only in P1/P11.** Forming \(A=\sum_p\chi_4(p)b_p\) before the multiplier retains the character. \(p\)-wise triangle, \(E_{\rm eq}\), or sectorwise positive norms do not. |
| opposite_character_and_single_row_controls | Adversarial, nonliteral coefficient tables | **Universal shortcut falsified.** Opposite identical rows give \(E_\chi=0\) but large separate norms; one coherent row gives \(E_\chi\asymp HD_0\). These do not disprove an actual-family theorem. |
| moving_profiles_zero_extension_and_endpoints | Literal support audit | **Incomplete after any naive fixed-rectangle rewrite.** Exact shifted supports and moving profiles must be retained; no permitted artifact supplies a complete new endpoint estimate for the majorized form. |
| Poisson_only_after_lawful_one_sided_inequality | Logical/analytic audit | **Required.** Without prior PSD or actual-family order, Poisson cannot repair the inequality. With complete data it is an equality; strict-interior iteration self-returns. |
| Gamma_before_claimed_survivor | Capacity ledger | **Claimed \(1\) not obtained.** Character erasure leaves \(\min(H,Q)\); contracted universal PSD plus diagonal closure leaves \(H/(\Delta+1)\); modewise absolute closure leaves at least \(H\); \(1\) occurs only for the identity or an unproved signed theorem. |
| flat_smooth_owner_and_downstream_scope | Scope audit | **Pass only under strict restriction.** The report addresses the flat-smooth strict-UNBAL survivor and makes no transfer to hard, sharp, clipped, starred, arithmetic-owner, nonflat, or transition packets. No downstream claim is certified. |

## 6. Dependencies and exact artifacts used

The derivation used only the following permitted artifacts, all read in full:

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/conductor_0823_full_proof_strategy.md
- strategy/A1_0823_2.md
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/synthesis.md
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reports/blind_dual_offproduct_sector_rederivation.md
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/reviews/conductor_round125_dual_sector_adjudication.md
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/briefs/majorant_cross_term_hostile_audit.md

The accepted inputs used from those artifacts are the frozen literal formulas and owner range; the exact \(E_\chi/E_{\rm eq}/D_0\) bookkeeping; the safe negative side and target equivalence; the elementary separate-row factor \(\min(H,Q)\); and the Round 125 strict-interior reciprocal self-return with its stated endpoint incompleteness. The uncertainty, order, rank-one, and \(\ell^1\) lemmas are proved directly above.

No web source, numerical experiment, symbolic computation, or unlisted artifact was used. The research allocation was \(100\%\) analytic/algebraic and \(0\%\) numerical/experimental.

## 7. Recommended state effect

**Recommended state effect: revise the proposed mechanism and promote only the scoped no-go lemma.**

- **Promote** the exact universal facts: pointwise multiplier order is equivalent to universal Toeplitz PSD order; \(t_0\geq\max(H,H^2/(\Delta+1))\); \(\|t\|_1\geq H^2\); equality \(t_0=H\) forces \(T=F_H\).
- **Reject** coefficientwise Fourier cutoff order, entrywise pair-kernel order, nonproportional internal-window majorization, partial-arc domination, and any post-Poisson majorant that lacks a prior lawful quadratic-form inequality.
- **Reject as a route to \(\Gamma=1\)** every placement after \(p\)-wise modulus, \(E_{\rm eq}\), or separate positive-row norms, because it has already lost the actual character cancellation and retains \(\min(H,Q)\).
- **Retain open** the literal target \(E_\chi\ll_\varepsilon X^{1/2+\varepsilon}\). The adversarial controls do not show the literal family is large.
- **Retain as the only possible continuation within this gate** a new actual-family joint signed correlation theorem applied before modulus, with a complete endpoint/owner ledger. It may estimate the lawful P1 majorized form or establish and use a restricted P11 comparison. This is an unproved replacement mechanism, not an accepted consequence of one-sided-majorant terminology.

No proof-draft, downstream packet, or global theorem should be changed on the strength of the proposed majorant alone.

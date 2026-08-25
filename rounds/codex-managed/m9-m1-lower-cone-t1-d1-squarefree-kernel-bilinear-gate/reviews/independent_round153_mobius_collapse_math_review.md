# Round 153 independent Mobius-collapse mathematical review

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Role: independent terminal algebra and seam reviewer
- Starting graph SHA-256: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Candidate reviewed: `candidates/conductor_round153_mobius_boundary_collapse.md`
- Verdict: **GREEN**
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

The conductor candidate is mathematically **GREEN**. Its exact identity

$$
 P_U^*=\sum_{b\ {\rm odd}}F_U(b)
 +\sum_{\substack{r\ge S\\r\ {\rm odd}}}
 C_S(r)\sum_{b\ {\rm odd}}F_U(r^2b),
 \qquad S=\lceil M^{1/4}\rceil,
\tag{R153.1}
$$

is correct with the literal character, profile, support, nearest-integer
convention, strict defect mask, parity, and endpoint data retained. The
$r\ge S$ term is absolutely $O_\varepsilon(X^\varepsilon)$ with the displayed
$M$ powers in the candidate. The accepted Round-152 exact- and small-defect
owners then give

$$
 P_U^*=P_U+O_\varepsilon(X^\varepsilon).
\tag{R153.2}
$$

Thus complete squarefree Mobius inversion and complete recombination return
the original open scalar up to an already safe boundary. This supports only
the candidate's scoped method obstruction: it does not prove the scalar
target, a strict new range, a signed lower bound, or an impossibility theorem
for a future coefficient-sensitive bilinear argument.

There are **no mandatory mathematical edits** to the conductor candidate.

## 2. Exact statement and hypotheses

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,\qquad J=M^{3/4},\qquad
 S=\lceil M^{1/4}\rceil,
\tag{R153.3}
$$

in the residual range below the accepted boundary
$M^{449}\asymp R^{780}$. Let $A_U$ be the inherited actual profile,
extended by zero, supported on its inherited
$O_\varepsilon(X^\varepsilon)$ components inside a fixed dilation of
$[M,2M]$, with $\|A_U\|_\infty\ll_\varepsilon X^\varepsilon$. Put

$$
 F_U(n)={\bf1}_{n>0\ {\rm odd}}
 {\bf1}_{|k(n)^2-Nn|>J}
 \chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
\tag{R153.4}
$$

where $k(n)=\lfloor\sqrt{Nn}+1/2\rfloor$ is the unique nearest integer.
For odd $r$, define

$$
 C_S(r)=\sum_{\substack{a\mid r\\r/a<S}}\mu(a).
\tag{R153.5}
$$

Then the exact Round-152 survivor satisfies (R153.1) and

$$
 \left|
 \sum_{\substack{r\ge S\\r\ {\rm odd}}}
 C_S(r)\sum_{b\ {\rm odd}}F_U(r^2b)
 \right|\ll_\varepsilon X^\varepsilon.
\tag{R153.6}
$$

No condition $(\tau,s)=1$, $(a,b)=1$, or $(a,s)=1$ is present. All variables
created by the inversion are positive and odd. The coefficient
$B_{1,U}(1)$ is external to $F_U$, $P_U$, and $P_U^*$ and retains its accepted
$O_\varepsilon(X^\varepsilon)$ bound.

## 3. Proof and line audit

### Literal weight and character

The candidate correctly keeps $\chi_4(n)$ inside $F_U(n)$. If
$n=\tau s^2$ with $\tau,s$ odd, complete multiplicativity gives

$$
 \chi_4(n)=\chi_4(\tau)\chi_4(s)^2=\chi_4(\tau),
 \qquad e(\sqrt{Nn})=e(s\sqrt{N\tau}).
\tag{R153.7}
$$

Neither identity requires $(\tau,s)=1$. Hence the candidate's equation
(153.C3) is exactly the Round-152 survivor, including its compulsory $s=1$
layer.

### Exact Mobius inversion and absence of a false gcd

The legal order is first to replace the squarefree restriction by

$$
 {\bf1}_{\tau\ {\rm squarefree}}=\mu^2(\tau)
 =\sum_{a^2\mid\tau}\mu(a)
\tag{R153.8}
$$

while summing over all positive odd $\tau$, and only then to put
$\tau=a^2b$. This gives

$$
 P_U^*=\sum_{\substack{s<S\\s\ {\rm odd}}}
 \sum_{a,b\ {\rm odd}}\mu(a)F_U((as)^2b).
\tag{R153.9}
$$

The integer $b$ may share prime factors with $a$; for example, an exponent at
least three in $\tau$ produces precisely such a term. The candidate inserts
no false coprimality condition and retains the $a=1$ term with sign $+1$.

### The $r=as$ fibres and truncated divisor coefficient

For a fixed positive odd $r$, the preimages of $r=as$ in (R153.9) are exactly

$$
 a\mid r,\qquad s=r/a<S.
\tag{R153.10}
$$

Their signed coefficient is therefore exactly (R153.5). If $r<S$, every
divisor passes the strict cutoff and

$$
 C_S(r)=\sum_{a\mid r}\mu(a)={\bf1}_{r=1}.
\tag{R153.11}
$$

This proves (R153.1). The cancellation for $1<r<S$ is between different
$a$- and $s$-preimages of the same integer; it would be destroyed by assigning
independent ownership to those pieces.

Odd parity is preserved throughout: odd $s$ and odd $a$ give odd $r$, and
odd $r,b$ give the original odd argument $r^2b$. The ceiling is also exact.
The original condition is $s<S$, so when an odd equality case $r=S$ exists it
belongs to the boundary sum; when $S$ is even there is simply no odd
$r=S$. No equality case is missing.

All rearrangements are finite. The zero-extended profile permits only
finitely many $n$, and for each such $n$ there are only finitely many triples
$(a,s,b)$ with $n=(as)^2b$. No convergence or conditional-reordering issue
arises.

### The $r\ge S$ boundary and all $M$ powers

If $F_U(r^2b)\ne0$, fixed-dilate support gives
$r^2b\asymp M$, hence $r\ll\sqrt M$, at most
$O(1+M/r^2)$ possible positive odd $b$, and

$$
 |F_U(r^2b)|\ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{R153.12}
$$

Also $|C_S(r)|\le d(r)\ll_\varepsilon X^\varepsilon$, since
$r\ll\sqrt M\le X^{1/4}$ in the project range. Dropping oddness and the
defect mask only enlarges this absolute upper bound, so

$$
\begin{aligned}
 |E_S|
 &\ll_\varepsilon M^{-3/4}X^\varepsilon
 \sum_{S\le r\ll\sqrt M}\left(1+\frac M{r^2}\right)\\
 &\ll_\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon,
\end{aligned}
\tag{R153.13}
$$

because $S\ge M^{1/4}$. If the support is counted componentwise, its
$O_\varepsilon(X^\varepsilon)$ component count merely introduces another
harmless factor that is absorbed by renaming $\varepsilon$. More directly,
the union of all components lies in one fixed dilation, so the displayed
$b$-count already bounds the union. Thus the candidate's support-component
and exponent bookkeeping is complete.

### Nearest integer, $N$ parity, and the defect mask

A nearest-integer tie would imply
$4Nn=(2m+1)^2$, impossible modulo four. This is independent of the parity or
prime-power structure of $N$. Every reindexing leaves the underlying integer
$n=r^2b$ unchanged, so both $k(n)$ and the strict inequality
$|k(n)^2-Nn|>M^{3/4}$ are evaluated at exactly the original argument. The
boundary estimate uses only that the mask is bounded by one; it never smooths,
moves, or deletes the mask inside a signed exponential sum.

### The $B_{1,U}(1)$ seam and the inference back to $P_U$

The external coefficient $B_{1,U}(1)$ never enters the Mobius algebra. It
remains attached to the surrounding transformed row exactly as in Round 152,
and its accepted $X^\varepsilon$ size is compatible with the usual
renaming of $\varepsilon$.

Let $P_U^{\rm LD}=\sum_{b\ {\rm odd}}F_U(b)$. By unique squarefree-kernel
decomposition, the complete large-defect wave splits as

$$
 P_U^{\rm LD}=P_U^*+P_{\mathcal L_2},
\tag{R153.14}
$$

where $P_{\mathcal L_2}$ is the accepted $s\ge S$ owner. Comparison with
(R153.1) even gives the exact cross-check $E_S=-P_{\mathcal L_2}$. Round 152
also proves

$$
 P_U=P_{\mathcal L_0}+P_{\mathcal L_1}+P_U^{\rm LD},
 \qquad
 |P_{\mathcal L_0}|+|P_{\mathcal L_1}|+|P_{\mathcal L_2}|
 \ll_\varepsilon X^\varepsilon.
\tag{R153.15}
$$

Equations (R153.14)--(R153.15) prove (R153.2), with the same conclusion also
following immediately by reversing the accepted additive-error identity
$P_U=P_U^*+O_\varepsilon(X^\varepsilon)$. There is no sign defect in the
big-$O$ inference.

### Reconciliation of the blind mask-removal seam

The blind report correctly warns that one cannot pass from a masked Cauchy
correlation to an unmasked geometric sum merely by deleting indicators:
deleting summands can increase the absolute value of an exponential sum. That
warning remains valid for a blockwise post-Cauchy argument.

It is not an obstruction to the conductor candidate. The candidate retains
the mask throughout (R153.9)--(R153.13). Moreover, the input unavailable to
the statement-only blind derivation is already supplied by Round 152:
$\#\mathcal L_1\ll_\varepsilon M^{3/4}X^\varepsilon$ with actual weight
$M^{-3/4}X^\varepsilon$, together with the separately safe exact ray. Thus
the mask may be split off at the scalar level, before Cauchy or positivity.
If one performs this split after formal Mobius expansion but still before
Cauchy, a fixed $n$ has at most

$$
 \sum_{r^2\mid n}d(r)\ll_\varepsilon X^\varepsilon
\tag{R153.16}
$$

preimages $n=(as)^2b$; the accepted correction therefore remains
$O_\varepsilon(X^\varepsilon)$ after renaming $\varepsilon$. What Round 152
does not license is the false term-deletion inequality inside an individual
masked correlation. Hence the blind seam is resolved exactly where the
candidate uses it and remains a valid restriction on any future Type-II
argument.

## 4. First doubtful or unproved step

There is no doubtful step in the candidate's finite inversion, fibre
coefficient, small-$r$ cancellation, boundary estimate, or Round-152 seam.
The first unproved estimate remains

$$
 \left|\sum_{b\ {\rm odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon
 \qquad (M^{449}\ll R^{780}),
\tag{R153.17}
$$

equivalently $|P_U^*|\ll_\varepsilon X^\varepsilon$ or
$|P_U|\ll_\varepsilon X^\varepsilon$ after the accepted owners are restored.
A future bilinear proof is not ruled out, but it must preserve signed
cross-block cancellation and cannot regard the artificial $a$-blocks as
separate owners. The conductor candidate already states this restricted
scope, so no repair is required.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Literal $F_U$ and survivor | GREEN. $\chi_4(n)$, the actual profile, zero extension, strict mask, endpoints, and $s=1$ are retained. |
| Exact $\mu^2$ inversion | GREEN. The squarefree restriction is replaced over all odd $\tau$ before $\tau=a^2b$; every $a$ and $\mu(a)$ remains. |
| False-gcd test | GREEN. No coprimality among $\tau,s,a,b$ is inserted. |
| $r=as$ fibres and $C_S(r)$ | GREEN. The preimages are exactly $a\mid r$, $r/a<S$, yielding the stated truncated divisor sum. |
| Odd parity and ceiling equality | GREEN. Only odd fibres occur, and an admissible $r=S$ equality lies in the boundary term. |
| Finite reordering | GREEN. Zero-extended compact support makes all relevant sums finite. |
| Boundary support and powers | GREEN. The raw count, component factor, $M^{-3/4}$ weight, $M^{-1/4}$ term, and $M^{1/4}/S$ term are correct. |
| $N$ parity, nearest integer, and mask | GREEN. The no-tie proof is all-parity, the argument of $k$ is unchanged, and the mask is only dropped in a positive upper bound. |
| Blind mask-removal seam | GREEN/reconciled. Round 152 supplies the missing scalar small-defect owner; it does not authorize deletion inside a masked correlation. |
| $B_{1,U}(1)$ | GREEN. It stays external with its accepted bound. |
| $P_U^*=P_U+O$ | GREEN. It follows both from the disjoint owner ledger and by symmetry of the accepted additive-error identity. |
| Downstream scope | GREEN. The result is a scoped recombination obstruction only, with no strict range or broader M1/M2 conclusion. |

All controls are analytic. No numerical experiment or computational
certification is used.

## 6. Dependencies and exact artifacts used

This review used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/candidates/conductor_round153_mobius_boundary_collapse.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reports/squarefree_mobius_bilinear_attack.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reports/blind_squarefree_kernel_typeii_feasibility.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/conductor_round152_adjudication.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/controls/conductor_round152_controls.md`.

No external source theorem is needed for the reviewed collapse.

## 7. Recommended state effect

Recommend **promote** for the narrow algebraic kernel, under the terminal label
`squarefree_kernel_bilinear_no_go` understood in its method-scoped sense:

- record (153.C3)--(153.C7) as the exact complete-Mobius recombination and
  absolutely safe boundary;
- record (153.C8) only as the already owner-supported equivalence with the
  Round-152 scalar;
- retain the one-variable large-defect character wave as open below
  $M^{449}\asymp R^{780}$; and
- make no strict-range, target, downstream-owner, or exponent mutation.

Mandatory edits to the conductor candidate: **none**.

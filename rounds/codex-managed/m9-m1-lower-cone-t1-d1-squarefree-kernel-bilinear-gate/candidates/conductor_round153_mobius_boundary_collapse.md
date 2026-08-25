# Round 153 conductor candidate: exact Mobius boundary collapse

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Round: 153
- Role: conductor-selected algebraic kernel
- Starting graph SHA-256: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Allocation: 100% analytic and algebraic; 0% numerical
- Proposed terminal label: `squarefree_kernel_bilinear_no_go`

## 1. Result

Complete squarefree Mobius inversion followed by exact divisor
recombination is an exact self-collapse: its dyadic Type-I/Type-II pieces
are not independent owners.  Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad S=\lceil M^{1/4}\rceil,
\tag{153.C1}
$$

and define the literal direct large-defect weight

$$
F_U(n)={\bf1}_{n\ \mathrm{odd}}
{\bf1}_{|k(n)^2-Nn|>J}
\chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
\tag{153.C2}
$$

where $A_U$ is extended by zero with every inherited support component
and endpoint convention.  Since $s$ is odd,
$\chi_4(\tau s^2)=\chi_4(\tau)$.  Then the exact Round-152 survivor is

$$
 P_U^*=\sum_{\substack{s<S\\s\ \mathrm{odd}}}
 \sum_{\substack{\tau\ge1\\\tau\ \mathrm{odd}}}
 \mu^2(\tau)F_U(\tau s^2).
\tag{153.C3}
$$

Define

$$
 C_S(r)=\sum_{\substack{a\mid r\\r/a<S}}\mu(a)
 \qquad(r\ \mathrm{odd}).
\tag{153.C4}
$$

Exact Mobius inversion and the change $r=as$ give

$$
 \boxed{
 P_U^*=\sum_{b\ \mathrm{odd}}F_U(b)
 +\sum_{\substack{r\ge S\\r\ \mathrm{odd}}}
 C_S(r)\sum_{b\ \mathrm{odd}}F_U(r^2b).}
\tag{153.C5}
$$

The second term is target-safe:

$$
 \sum_{\substack{r\ge S\\r\ \mathrm{odd}}}
 C_S(r)\sum_{b\ \mathrm{odd}}F_U(r^2b)
 \ll_\varepsilon X^\varepsilon.
\tag{153.C6}
$$

Consequently

$$
 \boxed{P_U^*=\sum_{b\ \mathrm{odd}}F_U(b)
 +O_\varepsilon(X^\varepsilon).}
\tag{153.C7}
$$

The sum in (153.C7) is the original all-odd wave restricted only by the
large-defect mask.  Round 152 already prices its complementary exact and
small-nonzero-defect sectors, so

$$
 \boxed{P_U^*=P_U+O_\varepsilon(X^\varepsilon).}
\tag{153.C8}
$$

Thus exact squarefree inversion followed by complete recombination returns
the same open scalar.  It gives no new range and no exponent change.
This does not rule out a future coefficient-sensitive signed estimate of
the unrecombined identity; such an estimate would also prove the original
direct wave and is precisely the missing theorem.

## 2. Exact statement and hypotheses

The only project-side inputs are:

1. $A_U$ is supported on $O_\varepsilon(X^\varepsilon)$ actual
   components in a fixed dilation of $[M,2M]$, is extended by zero, and
   satisfies $\|A_U\|_\infty\ll_\varepsilon X^\varepsilon$;
2. the direct weight retains the literal odd character $\chi_4(n)$,
   and $k(n)$ is the unique nearest integer to $\sqrt{Nn}$;
3. all variables in (153.C3) are positive and odd;
4. every odd $\ell$ has the unique form $\ell=\tau s^2$ with $\tau$
   squarefree and $s$ odd; and
5. Round 152 proves the exact-square and
   $0<|k(n)^2-Nn|\le M^{3/4}$ sums are
   $O_\varepsilon(X^\varepsilon)$.

No smooth replacement of the defect mask, no coprimality between the
squarefree kernel and square factor, and no source theorem is used.
The external coefficient $B_{1,U}(1)$ remains outside the scalar and has
$O_\varepsilon(X^\varepsilon)$ size.

## 3. Proof of the collapse

Because $\tau$ is odd,

$$
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a).
\tag{153.C9}
$$

Writing $\tau=a^2b$ gives

$$
 \chi_4(a^2bs^2)=\chi_4(b),\qquad
 e(s\sqrt{Na^2b})=e(as\sqrt{Nb}),
\tag{153.C10}
$$

and, more importantly, the complete summand depends on $(a,s)$ only
through $r=as$:

$$
 F_U(a^2bs^2)=F_U(r^2b).
\tag{153.C11}
$$

All sums are finite after zero extension, so they may be reordered
without a convergence argument.  Equations (153.C3) and (153.C9) give

$$
\begin{aligned}
 P_U^*
 &=\sum_{\substack{s<S\\s\ \mathrm{odd}}}
   \sum_{a,b\ \mathrm{odd}}\mu(a)F_U((as)^2b)\\
 &=\sum_{r\ \mathrm{odd}}
   \left(\sum_{\substack{a\mid r\\r/a<S}}\mu(a)\right)
   \sum_{b\ \mathrm{odd}}F_U(r^2b).
\end{aligned}
\tag{153.C12}
$$

For $r<S$, every divisor $a\mid r$ passes $r/a<S$.  Hence

$$
 C_S(r)=\sum_{a\mid r}\mu(a)
 =\begin{cases}1,&r=1,\\0,&1<r<S.
 \end{cases}
\tag{153.C13}
$$

Splitting (153.C12) at $S$ proves (153.C5).  This is exact for the
ceiling $S=\lceil M^{1/4}\rceil$; there is no missing equality case.

## 4. Boundary estimate

The coefficient in (153.C4) satisfies

$$
 |C_S(r)|\le d(r)\ll_\varepsilon X^\varepsilon.
\tag{153.C14}
$$

If $F_U(r^2b)\ne0$, then $r^2b\asymp M$ on one of the finitely many
literal support components.  Therefore $r\ll\sqrt M$, there are
$O(1+M/r^2)$ possible positive odd $b$, and

$$
 |F_U(r^2b)|\ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{153.C15}
$$

The defect mask and endpoint tests only delete candidates.  Thus

$$
\begin{aligned}
 \left|\sum_{r\ge S}C_S(r)\sum_bF_U(r^2b)\right|
 &\ll_\varepsilon
 M^{-3/4}X^\varepsilon
 \sum_{S\le r\ll\sqrt M}\left(1+\frac M{r^2}\right)\\
 &\ll_\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{153.C16}
$$

This proves (153.C6).  The same estimate holds componentwise and is
uniform in every parity of $N$ because it never divides by $N$ or invokes
a root count.

## 5. Type-I/Type-II implication and first open step

On a formal dyadic block $a\asymp A$, $b\asymp B$ with fixed outer $s$,

$$
 A^2Bs^2\asymp M,\qquad
 as\sqrt{NB}\asymp\sqrt{NM}.
\tag{153.C17}
$$

But the separate $A$ blocks are artificial pieces of (153.C12).  For
every $1<r<S$ their complete divisor sum cancels exactly by (153.C13).
Taking absolute values before recombination, or applying Cauchy and then
discarding the surviving correlation sign, forfeits the exact divisor
cancellation at that step.  This obstructs only that positive majorant.
A coefficient-sensitive signed Cauchy or bilinear theorem remains logically
possible and, by (153.C7)--(153.C8), would also prove the direct wave.
After lawful recombination only the $r=1$ direct wave and the target-safe
boundary remain.

The first open estimate is therefore unchanged:

$$
 \left|\sum_{b\ \mathrm{odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon,
\tag{153.C18}
$$

equivalently $|P_U^*|\ll_\varepsilon X^\varepsilon$ by (153.C7), or
$|P_U|\ll_\varepsilon X^\varepsilon$ by (153.C8).  A theorem for the
isolated $s=1$ squarefree layer would still be a separate partial owner,
but it is not obtained by the complete-$s$ collapse and would not alone
bound the remaining $s$ layers.

## 6. Required controls and review gate

The conductor has reproduced:

1. the literal direct weight (153.C2) and exact survivor (153.C3);
2. Mobius inversion with all odd $a$, including $a=1$;
3. $\chi_4(a^2b)=\chi_4(b)$ and the exact $r=as$ dependence;
4. the ceiling-sensitive coefficient $C_S(r)$;
5. the complete cancellation for $1<r<S$;
6. the target-safe $r\ge S$ boundary with all support components and
   endpoints; and
7. the equivalence to the original large-defect and full waves.

The label `squarefree_kernel_bilinear_no_go` records only exact
complete-Mobius recombination to the direct large-defect wave plus an
absolutely safe boundary; it is not an impossibility theorem for future
signed bilinear estimates of the unrecombined identity.

For this literal $D=d=L=1$ wave, Round 152 owns the complete
actual-profile absolute mass of the exact and
$0<|k^2-Nn|\le M^{3/4}$ sectors.  The expanded representation
multiplicity is divisor-bounded, so these sectors may be removed at
$O_\varepsilon(X^\varepsilon)$ before Cauchy.  This does not license
deleting masks inside a correlation and supplies no generic masked
estimate.

Before graph mutation, independent review must attack the finite
reordering, odd parity, ceiling equality, support count, divisor bound,
defect mask, actual profile, $B_{1,U}(1)$ seam, and the inference from
(153.C7) to (153.C8).  The source audit must decide whether any current
theorem directly estimates the isolated $s=1$ layer or the unrecombined
signed Mobius family without contradicting the exact collapse.  No raw
capacity is treated as a lower bound.

## 7. Dependencies and recommended state effect

Dependencies:

- `M9-M1-lower-cone-t1-d1-square-root-wave-strict-range-reduction`;
- `M9-M1-lower-cone-t1-d1-square-root-wave-method-obstruction`;
- the Round-152 conductor candidate, adjudication, and controls; and
- the literal Round-148 profile and zero-extension ledger inherited by
  those accepted nodes.

Recommended state effect, subject to terminal review:

- create a scoped obstruction recording the exact Mobius boundary
  collapse (153.C5)--(153.C8);
- retain the isolated $s=1$ squarefree wave only as an open subproblem,
  unless a separate report proves it;
- reject claims that dyadic Mobius blocks are independent owners, that
  the $a=1$ block may be discarded, that diagonal-scale bilinear energy
  follows without cross-block cancellation, or that complete squarefree
  inversion itself creates a new range; and
- make no downstream theorem or exponent change.

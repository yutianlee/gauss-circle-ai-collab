# Round 152 hostile review: arithmetic square-root pruning

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Round: 152
- Task: `hostile_square_root_pruning_review`
- Role: hostile seam reviewer
- Starting graph SHA-256: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Generated: `2026-08-25T08:08:24+08:00`
- Reviewed kernel: (152.C7)--(152.C10)
- Allocation: 100% analytic/algebraic, 0% numerical
- Decisive verdict: **GREEN for the strict pruning only**

## 1. Result

I tried to falsify the proposed pruning by attacking the rounding map, every
prime-power root count, the passage from residue classes to the actual
$k$-interval, the two parities of the exact ray, the rounded square-factor
cut, the endpoint partition, and the placement of the actual weight and
$B_{1,U}(1)$.  None of those attacks breaks the proof.

Under the actual-profile hypotheses stated in the barrier packet and the
candidate, the following restricted conclusion is valid.  For sufficiently
large $X$, put

$$
 N=\lfloor X\rfloor,\qquad R=X^{1/4},\qquad
 1\ll M\le R^2,
$$

and suppose that the retained support is contained in a fixed dilation
$[cM,CM]$, with

$$
 A_U(\ell)=\mathscr A_{1,M,U}(1,\ell),\qquad
 w_U(\ell)=\ell^{-3/4}A_U(\ell),\qquad
 \|w_U\|_\infty\ll_\varepsilon M^{-3/4}X^\varepsilon.
$$

With $k(\ell)$, $j(\ell)$, $\ell=\tau s^2$, and the four sets
$\mathcal L_0,\mathcal L_1,\mathcal L_2,\mathcal L_*$ defined in
(152.C5)--(152.C7),

$$
 |P_{\mathcal L_0}|+|P_{\mathcal L_1}|+|P_{\mathcal L_2}|
 \ll_\varepsilon X^\varepsilon,
$$

and hence

$$
 P_U=P_U^*+O_\varepsilon(X^\varepsilon)
$$

with $P_U^*$ exactly as in (152.C10).  This is an owner-complete support
reduction, not a new $M$-interval estimate and not a proof that
$P_U^*\ll X^\varepsilon$.

There is one literal defect outside this proof kernel: (152.C33) omits the
additive sign before its error term.  The displayed transform must read

$$
 P_U=e(1/8)N^{-1/4}
 \sum_{\substack{q>0\\q\ \mathrm{odd}}}
 \chi_4(q)A_U(4N/q^2)e(N/q)
 +O_\varepsilon(X^\varepsilon).
$$

As printed, (152.C33) is not an exact equality.  This transcription error is
not used in the proof of (152.C7)--(152.C10), so it does not turn the pruning
gate RED; it should not be copied verbatim into state.

## 2. Exact statement and hypotheses

The GREEN verdict has exactly the following scope.

1. $N$ is a positive integer with $N\asymp X$, $M\le X^{1/2}$, and the
   asymptotic is taken for large $X$.  No identity $R^2=N^{1/2}$ is needed;
   only $R^2\asymp N^{1/2}$ is true when $N=\lfloor X\rfloor$.
2. The actual retained profile is zero-extended, is supported on a fixed
   finite union contained in $[cM,CM]$, and obeys the stated supremum bound.
   Smoothness and variation are needed for the adjacent and transform
   discussions, but the arithmetic pruning itself uses only support and
   supremum.
3. Every retained $\ell$ is positive and odd.  Its unique squarefree-kernel
   factorization is $\ell=\tau s^2$ with both $\tau$ and $s$ odd and $\tau$
   squarefree.
4. The thresholds are literal real thresholds
   $J_M=M^{3/4}$ and the literal integer threshold
   $S_M=\lceil M^{1/4}\rceil$.  Since $s$ is integral,
   $s\ge S_M$ is equivalent to $s\ge M^{1/4}$, while
   $s<S_M$ is equivalent to $s<M^{1/4}$.
5. The coefficient $B_{1,U}(1)$ is external to $P_U$ and satisfies
   $|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon$.  It is not part of
   $A_U$, $w_U$, the root count, or the square-factor count.

No source-theorem applicability claim is reviewed here, and no conclusion is
made for any complementary $D,L,t$ sector or downstream obligation.

## 3. Proof and hostile rederivation

### 3.1 Nearest-integer uniqueness

For $y=\sqrt{N\ell}$ the only possible ambiguity in
$\lfloor y+1/2\rfloor$ would be $y=m+1/2$.  That would imply

$$
 4N\ell=(2m+1)^2,
$$

whose left side is divisible by $4$ and whose right side is odd.  Hence no
tie exists, for either parity of $N$, and $k(\ell)$ and $j(\ell)$ are
single-valued.

### 3.2 Local roots, including $p=2$ and $p^\alpha\mid j$

Let $p^\alpha\Vert N$, set
$v=\min(v_p(j),\alpha)$, and denote the local root count by
$\rho_{p^\alpha}(j)$.  There are three exhaustive cases.

- If $v=\alpha$, then $j\equiv0\pmod {p^\alpha}$.  The solutions are
  precisely the residues divisible by $p^{\lceil\alpha/2\rceil}$, so

  $$
  \rho_{p^\alpha}(j)=p^{\lfloor\alpha/2\rfloor}
  \le p^{v/2}.
  $$

  This includes nonzero $j$ divisible by $p^\alpha$, not just $j=0$.

- If $v<\alpha$ is odd, valuation parity makes a square impossible, so
  $\rho_{p^\alpha}(j)=0$.

- If $v=2b<\alpha$, every solution has $x=p^by$ with $y$ a unit, and

  $$
  y^2\equiv j/p^{2b}\pmod {p^{\alpha-2b}}.
  $$

  Each unit root modulo $p^{\alpha-2b}$ has exactly $p^b$ lifts for $y$
  modulo $p^{\alpha-b}$.  For odd $p$ the unit congruence has at most two
  roots.  For $p=2$ it has at most one root at modulus $2$, at most two at
  modulus $4$, and at most four at every higher power.  Therefore

  $$
  \rho_{p^\alpha}(j)\le
  \begin{cases}
   2p^{v/2},&p\text{ odd},\\
   4\,2^{v/2},&p=2.
  \end{cases}
  $$

Chinese remaindering now gives the deliberately loose but uniform bound

$$
 \rho_N(j)=\prod_{p^\alpha\Vert N}\rho_{p^\alpha}(j)
 \le 4\,2^{\omega(N)}\sqrt{(|j|,N)}.
\tag{R152.H1}
$$

Thus the candidate does not lose a special family when $j$ is divisible by
one or more full prime powers of $N$, and the $2$-adic cases are covered.

### 3.3 Summation over all nonzero small defects

For any real $J\ge1$, the integer sum means
$1\le |j|\le\lfloor J\rfloor$.  From (R152.H1), positivity, and
$\sqrt g\le\sum_{d\mid g}\sqrt d$,

$$
\begin{aligned}
 \sum_{1\le |j|\le J}\rho_N(j)
 &\ll 2^{\omega(N)}
   \sum_{1\le |j|\le J}\sum_{d\mid (|j|,N)}\sqrt d\\
 &\ll J\,2^{\omega(N)}\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{R152.H2}
$$

The two signs of $j$ cost only an absolute factor.  The last estimate is the
standard divisor-size bound and is uniform in the prime-power structure of
$N$.

### 3.4 The actual $k$-interval has only $O(1)$ representatives

If $A_U(\ell)\ne0$, then $cM\le\ell\le CM$.  Rounding enlarges the
corresponding $k$-interval by at most a fixed additive constant, so its
length is

$$
 |I_k|\le C_0\sqrt{NM}+O(1).
$$

Moreover

$$
 \frac{|I_k|}{N}\ll\sqrt{M/N}+N^{-1}
 \ll X^{-1/4}.
$$

It is therefore $<1$ for sufficiently large $X$.  A residue class modulo
$N$ has at most one representative in the containing interval (and in any
case $O(1)$ if the finitely many profile components are counted
separately).  For fixed $j$ and $k$, the value

$$
 \ell=(k^2-j)/N
$$

is fixed.  Integrality, positivity, oddness, membership in the exact
half-open retained support, and the nearest-integer test can only remove
candidates.  Combining this observation with (R152.H2) and taking
$J=M^{3/4}$ gives

$$
 \#\mathcal L_1\ll_\varepsilon M^{3/4}X^\varepsilon,
 \qquad
 \sum_{\ell\in\mathcal L_1}|w_U(\ell)|
 \ll_\varepsilon X^\varepsilon.
\tag{R152.H3}
$$

Here $M^{3/4}<N$ follows for large $X$ from $M\le X^{1/2}$.

### 3.5 The exact $j=0$ ray for both parities

Write uniquely

$$
 N=a^2n_0,\qquad n_0\ \text{squarefree}.
$$

For $\ell=\tau s^2$,

$$
 N\ell=(as)^2n_0\tau
$$

is a square if and only if $n_0\tau$ is a square.  Since $n_0$ and
$\tau$ are squarefree, this is equivalent to $\tau=n_0$.  The ray is
admissible among odd $\ell$ exactly when $n_0$ is odd, equivalently when
$\nu_2(N)$ is even.  If $\nu_2(N)$ is odd, $\mathcal L_0$ is empty.  If
$\nu_2(N)$ is even, then

$$
 \sqrt{N\ell}=asn_0\in\mathbb Z,\qquad
 \chi_4(\ell)=\chi_4(n_0),
$$

and the phase is one along the entire ray.  Actual support forces
$s\asymp(M/n_0)^{1/2}$ whenever the ray is nonempty, whence

$$
\begin{aligned}
 |P_{\mathcal L_0}|
 &\le n_0^{-3/4}
   \sum_{s\asymp(M/n_0)^{1/2}}s^{-3/2}|A_U(n_0s^2)|\\
 &\ll_\varepsilon
 n_0^{-3/4}(M/n_0)^{-1/4}X^\varepsilon
 =M^{-1/4}n_0^{-1/2}X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{R152.H4}
$$

Thus neither parity supplies a missing exact-square obstruction.

### 3.6 The exact ceiling cut and the support endpoints

Put $S_M=\lceil M^{1/4}\rceil$.  For fixed integer $s\ge S_M$, the
support condition $cM\le\tau s^2\le CM$ leaves an interval of length
$O(M/s^2)$ for $\tau$, hence $O(1+M/s^2)$ integral candidates.  Oddness
and squarefreeness only reduce this number.  Also $s\ll\sqrt M$ on the
actual support.  Therefore

$$
\begin{aligned}
 \#\{\ell=\tau s^2\ \text{retained}:s\ge S_M\}
 &\ll\sum_{S_M\le s\ll\sqrt M}
       \left(1+\frac M{s^2}\right)\\
 &\ll M^{1/2}+\frac M{S_M-1}
 \ll M^{3/4}.
\end{aligned}
\tag{R152.H5}
$$

For the growing range, $S_M-1\asymp M^{1/4}$; the finitely many smaller
values are already in the bounded-$M$ owner.  Half-open support endpoints
change an interval count by at most one and are already covered by the
displayed $1+M/s^2$.  Intersecting this set with
$|j|>M^{3/4}$ only deletes terms.  Thus

$$
 |P_{\mathcal L_2}|\le
 \sum_{\ell\in\mathcal L_2}|w_U(\ell)|
 \ll_\varepsilon X^\varepsilon.
\tag{R152.H6}
$$

### 3.7 Disjointness, coverage, the survivor, and $B_{1,U}(1)$

Every retained $\ell$ has exactly one $j(\ell)$ and one pair $(\tau,s)$.
It first lies either in $j=0$, in $0<|j|\le M^{3/4}$, or in
$|j|>M^{3/4}$.  In the last case, the integral $s$ lies exactly one of
$s\ge\lceil M^{1/4}\rceil$ and
$s<\lceil M^{1/4}\rceil$.  Hence the four sets in (152.C7) are pairwise
disjoint and cover the complete actual support, with no endpoint gap.

On the survivor, $s<M^{1/4}$ and $\ell\ge cM$, so

$$
 \tau=\ell/s^2>cM^{1/2}.
$$

Moreover $s$ is odd, so $\chi_4(\ell)=\chi_4(\tau)$, and
$e(\sqrt{N\ell})=e(s\sqrt{N\tau})$.  This proves the literal formula
(152.C10).

Finally, $B_{1,U}(1)$ is applied only after the scalar relation.  From

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
 \qquad \widetilde S_U=B_{1,U}(1)S_U,
$$

the pruning gives, after harmless renaming of $\varepsilon$,

$$
 \widetilde S_U=
 B_{1,U}(1)e(-1/8)N^{1/4}P_U^*
 +O_\varepsilon(RX^\varepsilon).
\tag{R152.H7}
$$

Thus the row coefficient is retained in its actual position and does not
alter any lattice multiplicity or weight bound.

## 4. Adjacent pairing, one $A$-process, and scale-power audit

The adjacent identity (152.C14)--(152.C16) is correct.  In particular,

$$
 \Delta_2f(x)=\frac{2\sqrt N}{\sqrt{x+2}+\sqrt x}
 \asymp R^2M^{-1/2},
$$

and the multiplier $1-e(\Delta_2f(x))$ cannot be replaced by a derivative
of $w_U$.

For a shift $h$ in the odd-index variable, the original shift is $2h$ and

$$
 \chi_4(\ell+2h)\chi_4(\ell)=(-1)^h.
$$

The shifted phase has
$g_h''(x)\asymp R^2hM^{-5/2}$, while the product weight has supremum plus
variation $O_\varepsilon(M^{-3/2}X^\varepsilon)$.  The standard
second-derivative estimate gives

$$
 |C_h|\ll_\varepsilon
 Rh^{1/2}M^{-7/4}+R^{-1}h^{-1/2}M^{-1/4},
$$

and finite differencing gives exactly the three powers in (152.C19).  For
that termwise procedure to be target-sized one needs

$$
 H\gg M^{1/2},\qquad
 H\ll M^{3/2}/R^2,\qquad
 H\gg M^{3/2}/R^2.
$$

The first two are incompatible for $M<R^2$.  This validates the scoped
one-$A$-process no-go; it does not rule out a new joint estimate that keeps
cancellation among the outer $(-1)^h$ signs.

The derivative/exponent ledger also recomputes correctly:

$$
 |P_U|\ll_\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon.
$$

It yields $(R^{52}/M^{29})^{1/168}$ for
$(13/84,55/84)$ and
$(R^{1424}/M^{819})^{1/2564}$ for
$(178/641,365/641)$.  The latter is exactly target-sized at
$M^{819}=R^{1424}$ and loses below it.  The displayed second- and
third-derivative powers (152.C39)--(152.C40) are also algebraically
correct.  The elementary capacities meet at $M=R^{4/3}$ with size
$R^{1/3}$.

This audit checks only algebraic translations of the inputs stated in the
permitted artifacts.  It does not certify the source-applicability or
source-exhaustion sentence near the end of candidate Section 4, because
source literature was expressly excluded from this review.

## 5. First failed, doubtful, or unproved step

**First failed step in the strict pruning: none.**  The first genuinely
unproved mathematical step after the valid reduction is

$$
 |P_U^*|\ll_\varepsilon X^\varepsilon.
$$

In particular the $s=1$ squarefree layer remains, so no absolute argument
has acquired the missing $M^{1/4}$ cancellation.

**First literal defect elsewhere in the candidate:** (152.C33), where the
`+` before $O_\varepsilon(X^\varepsilon)$ is absent.  A second minor exactness
issue is the prose identity $R^2=N^{1/2}$ in the justification following
(152.C26); with $N=\lfloor X\rfloor$ it must be $R^2\asymp N^{1/2}$.  The
needed strict interval inequality still follows with room to spare.  Neither
defect is a dependency of the pruning proof.

The first dependency that this isolated review cannot independently prove is
the inherited assertion that the actual Round-148 profile really has the
fixed-dilation support and $M^{-3/4}X^\varepsilon$ supremum used above.  That
assertion is explicit in the candidate and discovery report and is summarized
by the barrier packet, but its underlying ledger was outside the allowed
context.  Promotion must therefore attach the accepted actual-profile node as
a dependency rather than treating this review as a new audit of that ledger.

## 6. Required controls and outcomes

| Control | Outcome |
|---|---|
| Nearest-integer uniqueness | **GREEN.** A half-integer tie contradicts parity modulo $4$. |
| Odd-prime local roots | **GREEN.** Zero, odd-valuation, and $v=2b<\alpha$ cases give respectively $p^{\lfloor\alpha/2\rfloor}$, $0$, and at most $2p^b$. |
| $p=2$ local roots | **GREEN.** Unit-root multiplicities $1,2,4$ at exponents $1,2,\ge3$, followed by $2^b$ lifts, cover every case. |
| $j$ divisible by full prime powers | **GREEN.** It is the $v=\alpha$ zero-congruence case and was not omitted. |
| Sum over $0<|j|\le M^{3/4}$ | **GREEN.** Both signs and the real-to-integer cutoff are covered by (R152.H2). |
| Actual $k$ interval modulo $N$ | **GREEN.** Its containing interval has length $O(\sqrt{NM})=o(N)$, so every root class has $O(1)$ representatives. |
| Exact $j=0$ ray | **GREEN.** It is empty when $\nu_2(N)$ is odd and is exactly $\tau=n_0$ when $\nu_2(N)$ is even; its full mass is target-safe. |
| Exact ceiling $\lceil M^{1/4}\rceil$ | **GREEN.** Integer equivalence gives a gap-free split, and $S_M-1\asymp M^{1/4}$ in the growing range. |
| Square-factor tail endpoints | **GREEN.** The $1+M/s^2$ count includes both support endpoints and totals $O(M^{3/4})$. |
| Disjointness and coverage | **GREEN.** The ordered $j$ split followed by the $s$ split is a literal partition. |
| Actual weight placement | **GREEN conditional on the inherited profile ledger.** Only $\|w_U\|_\infty\ll M^{-3/4}X^\varepsilon$ is used in the pruning. |
| $B_{1,U}(1)$ placement | **GREEN.** It multiplies $S_U$ after the $P_U$ reduction and costs only a renaming of $\varepsilon$. |
| Adjacent pairing | **GREEN/no-go.** The whole oscillatory finite difference is retained. |
| One legal $A$-process | **GREEN/no-go.** Even shifts erase the variable character and the three powers in (152.C19) are correct. |
| Boundary and exponent powers | **GREEN algebraically.** The $R^{4/3}$ capacity crossing and $M^{819}=R^{1424}$ boundary are correct. |
| Transform display (152.C33) | **RED as typeset, nonblocking for pruning.** Insert the missing additive `+`. |
| Absolute capacity versus signed estimate | **GREEN.** The survivor and its $s=1$ layer remain explicitly open. |

No numerical experiment was performed.

## 7. Dependencies and recommended state effect

I read exactly the artifacts authorized by the review brief:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/barrier_packet.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_character_wave_attack.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/blind_square_root_wave_feasibility.md`; and
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`.

I did not read proof-state conclusions, source literature, source cards,
strategy files, earlier-round candidates, validation matrices, synthesis, or
any other mathematical artifact.  The derivation uses only elementary
valuation theory, the Chinese remainder theorem, divisor summation, interval
counting, unique squarefree-kernel factorization, the stated profile bounds,
and the stated adjacent/differencing formulas.

**Recommended state effect: promote only the strict arithmetic reduction
(152.C7)--(152.C10), with the accepted actual-profile ledger recorded as an
explicit dependency.**  Retain $|P_U^*|\ll X^\varepsilon$ and hence the full
$P_U$ target as open.  Retain the adjacent-pair and one-$A$-process results
only as scoped method obstructions.  Correct (152.C33) before carrying its
transform formula into any durable statement.  Do not promote a new
$M$-interval, a source-exhaustion theorem, or any downstream obligation.

## 8. Terminal recheck after conductor corrections

- Rechecked: `2026-08-25T08:10:51+08:00`.
- (152.C33) now contains the required additive
  $+O_\varepsilon(X^\varepsilon)$ after the reciprocal main sum.
- The $k$-support paragraph now correctly states
  $M\le R^2\asymp N^{1/2}$ rather than identifying $R^2$ and $N^{1/2}$
  exactly.

Both corrections agree with the derivations in this review.  They change no
threshold, root multiplicity, interval length, endpoint, owner, or error
power, and introduce no regression.  The earlier two textual caveats are
therefore discharged and superseded by this terminal note.  The decisive
verdict remains **GREEN for the strict pruning (152.C7)--(152.C10) only**;
$|P_U^*|\ll_\varepsilon X^\varepsilon$ remains open.

# Round 155 conductor candidate: complete dual resummation is exact Gauss inversion

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Round: 155
- Role: conductor algebraic candidate pending independent review
- Starting graph: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Allocation: 100% algebraic; 0% numerical

## 1. Result: exact route-scoped self-return

Fix an odd divisor $d\mid N$, put

$$
 q=4N,\qquad c=q/d\equiv0\pmod4,
\tag{155.CI1}
$$

and retain the literal finite coefficient

$$
 \widehat B_j(2dv)=
 \sum_{x\bmod q}B_j(x)e_c(-2vx).
\tag{155.CI2}
$$

If the theta Kloosterman sum is expanded and the complete
$v\bmod(c/2)$ family is resummed, the result is exactly the original
$d=(h,N)$ quadratic-selector stratum. Thus complete dual resummation after
the Round-154 Gauss completion is its inverse, not a new cancellation
step.

## 2. Exact statement and hypotheses

For $a\bmod c$ a unit, use the DFI normalization

$$
 K(-v^2,-j;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)
 e_c(-\bar a v^2-aj).
\tag{155.CI3}
$$

Then, for every finitely supported $B_j$ on $\mathbb Z/q\mathbb Z$,

$$
\begin{aligned}
 &\sum_{v\bmod(c/2)}
 \widehat B_j(2dv)K(-v^2,-j;c)\\
 &\quad=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
\end{aligned}
\tag{155.CI4}
$$

No smoothness, support length, parity of $N$, or asymptotic estimate is
used. The only hypotheses are $d\mid N$, $d$ odd, and the exact Fourier,
Gauss, and theta-multiplier conventions above.

## 3. Proof or derivation

Expand (155.CI2)--(155.CI3) and interchange finite sums. The inner dual
sum is

$$
 H_c(a,x)=\sum_{v\bmod(c/2)}
 e_c(-\bar a v^2-2vx).
\tag{155.CI5}
$$

Because $c=4m$, its summand is periodic modulo $c/2$: shifting
$v$ by $c/2=2m$ changes the exponent by the integer
$-\bar a v-\bar a m-x$. Hence $H_c(a,x)$ is one half of the complete
quadratic Gauss sum with quadratic coefficient
$A\equiv-\bar a\pmod c$ and linear coefficient $-2x$.

The accepted all-parity Gauss evaluation gives

$$
 H_c(a,x)=\frac{1+i}{2}\epsilon_A^{-1}
 \left(\frac cA\right)\sqrt c\,e_c(ax^2).
\tag{155.CI6}
$$

Indeed $\bar A\equiv-a\pmod c$, so the completed-square phase is
$e_c(ax^2)$. Also $\bar a\equiv a\pmod4$, whence
$A\equiv-a\pmod4$, and quadratic-character inversion gives

$$
 \epsilon_a\left(\frac ca\right)
 \epsilon_A^{-1}\left(\frac cA\right)
 =-i\chi_4(a).
\tag{155.CI7}
$$

To see the symbol identity in (155.CI7), note that the real quadratic
character $u\mapsto(c/u)$ is nonzero on units,
$(c/A)=(c/(-\bar a))=(c/\bar a)=(c/a)$, while the two possible residues
$a\equiv1,3\pmod4$ give respectively $-i$ and $i$ for the epsilon
product. Substituting (155.CI6)--(155.CI7) proves (155.CI4).

Finally insert (155.CI4) into the exact normalized $d$-stratum:

$$
 -\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c
 \sum_v\widehat B_j(2dv)K(-v^2,-j;c).
\tag{155.CI8}
$$

Since $(1+i)(1-i)=2$ and $dc=q$, (155.CI8) becomes

$$
 -\frac{i}{2N}\chi_4(d)
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)),
\tag{155.CI9}
$$

which is exactly the original selector contribution from
$h=da\bmod q$ with $(h,N)=d$.

## 4. First doubtful or unproved step

Identity (155.CI4) gives no estimate for a truncated or weighted
$v$-family, and it gives no cancellation after different $d$-strata or
defect blocks are coupled. The first open step is a decomposition that
uses the literal decay and $j$-dependence of $\widehat B_j(2dv)$ before
complete inverse resummation, with a total norm small enough to beat the
accepted termwise DFI bound. The $v=0$ contribution must be separated.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| Half-period | PASS. The summand in (155.CI5) has exact period $c/2$. |
| Gauss phase | PASS. $A=-\bar a$ and linear term $-2x$ give $e_c(ax^2)$. |
| Multiplier | PASS. Equation (155.CI7) checks both unit classes modulo four. |
| Imprimitive factor | PASS. The outside $d\sqrt c$ is retained until $dc=q$. |
| Fourier normalization | PASS. The factor $1/q$ and selector factor $1/(2N)$ remain in (155.CI8). |
| Literal coefficient | PASS. No smoothness, separation, or absolute value is inserted. |
| Zero mode | OPEN/separate. It is included in the exact inversion but not independently estimated. |
| Downstream scope | PASS. The identity is a route obstruction, not a bound for the outer-defect wave. |

## 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/source_conductor_round154_final.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/candidates/conductor_round155_outer_defect_seed.md`.

## 7. Recommended state effect

Subject to independent normalization review, record complete
theta-multiplier expansion followed by complete $v$-resummation as an
exact inverse-Gauss self-return. Reject it as a standalone source of
cancellation. Retain partial-frequency, zero-mode, coefficient-sensitive
joint transforms and direct selected cross-fibre estimates as open, with
no owner, scale, theorem, or exponent promotion from this identity alone.

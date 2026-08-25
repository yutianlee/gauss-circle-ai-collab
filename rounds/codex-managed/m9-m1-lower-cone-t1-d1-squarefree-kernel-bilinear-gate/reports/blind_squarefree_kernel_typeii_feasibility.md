# Round 153 blind squarefree-kernel Type-II feasibility report

## Isolation declaration

This is a statement-only independent derivation. I read only `protocol.md` and
`rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/blind_statement.md`.
I did not read the claim graph, the best proof draft, a strategy file, any
Round-148--153 nonblind artifact, or a sibling report. I used no web source and
no numerical experiment or numerical certification. The work below is 100%
analytic. This report is the only artifact I edited.

## 1. Result

The exact Mobius inversion does **not** leave a genuine middle Type-II problem.
It collapses algebraically after the variables `a` and `s` are recombined.
Write

\[
 S=\lceil M^{1/4}\rceil,
 \qquad
 D(n)={\bf 1}_{\{|k(n)^2-Nn|>M^{3/4}\}}.
\]

Define the truncated divisor coefficient

\[
 c_S(t)=\sum_{\substack{s\mid t\\s<S}}\mu(t/s).
\tag{1.1}
\]

Then the exact identity is

\[
 \mathcal P^*
 =\sum_{\substack{t,b\geq 1\\t,b\ \mathrm{odd}}}
 c_S(t)\chi_4(b)(t^2b)^{-3/4}A(t^2b)D(t^2b)
 e(t\sqrt{Nb}).
\tag{1.2}
\]

Moreover,

\[
 c_S(1)=1,
 \qquad c_S(t)=0\quad(1<t<S).
\tag{1.3}
\]

Consequently

\[
 \mathcal P^*=\mathcal P_0+\mathcal E_{\geq S},
\tag{1.4}
\]

where

\[
 \mathcal P_0=
 \sum_{\substack{b\geq1\\b\ \mathrm{odd}}}
 \chi_4(b)b^{-3/4}A(b)D(b)e(\sqrt{Nb})
\tag{1.5}
\]

and, with the usual convention that logarithms and divisor-function losses are
absorbed by an `X^epsilon` allowance,

\[
 \mathcal E_{\geq S}\ll_\varepsilon X^\varepsilon.
\tag{1.6}
\]

More literally from only the displayed hypotheses, the right side in (1.6) is
`X^epsilon M^{o(1)}` (or `X^epsilon log(2M)` by an average divisor bound).
As usual, relabelling epsilon gives (1.6) when the parameters have the standard
polynomial relation to the ambient `X`. If no relation at all between `X` and
`M,N` is intended, the notation in (153.BL2) itself needs that convention made
explicit.

Thus (153.BL2) is, up to the rigorously bounded tail (1.6), equivalent to the
single masked `a=s=1` estimate

\[
 \boxed{
 \left|\sum_{b\ \mathrm{odd}}
 \chi_4(b)A(b)D(b)e(\sqrt{Nb})\right|
 \ll_\varepsilon X^\varepsilon M^{3/4}.}
\tag{1.7}
\]

I do not prove (1.7). I obtain the following first rigorous method-specific
obstruction instead.

> **No-go for the squarefree Type-II gate by itself.** After exact Mobius
> recombination, every putative middle bilinear range `1<t<S` cancels, the
> range `t>=S` is absolutely summable, and the only unowned term has
> `a=s=1`. It has no `a`-variable on which a Type-II Cauchy argument can act.
> If one refuses to recombine and instead takes Cauchy followed by absolute
> modular-spacing energy, then even in the more favorable *unmasked* model
> the pigeonhole-capacity term can own only
> \[
> A_0^3s^4\gtrsim M^{1/2}.
> \tag{1.8}
> \]
> It loses `M^{1/4}` at `A_0=s=1`. With the required exact mask, the usual
> geometric-correlation estimate is not even available without a new
> near-defect count or a sign-sensitive masked-correlation lemma.

This is a no-go for that method, not a counterexample to (153.BL2). In
particular, neither the pigeonhole floor nor the exact-collision model below is
a signed lower bound for the original sum.

## 2. Exact statement and hypotheses of the established result

Assume exactly the hypotheses in the blind statement: `N` is a positive
integer, `R` is comparable with `N^{1/4}`, `1 << M <= R^2`,
`M^{449} << R^{780}`, `A` has fixed-dilate support, is extended by zero, and
has supremum norm plus total variation `<< X^epsilon`. All variables in the
kernel decomposition are positive and odd. The nearest integer `k(n)` is
unique: the square root of an integer cannot be a strict half-integer.

The proved conclusions are:

1. the exact identities (1.1)--(1.5), with the Mobius sign, `chi_4(b)`, the
   exact mask at `t^2b`, finite support, and all strict endpoints retained;
2. the absolute tail estimate (1.6), up to the harmless-power convention just
   stated;
3. equivalence of (153.BL2) with the one-variable seam (1.7), modulo that
   tail;
4. the precise limitation (1.8) of a Cauchy-plus-absolute-spacing proof;
5. invalidity of replacing the exact masked correlation by an unmasked
   geometric sum unless a separate mask-removal estimate is first proved.

No assertion is made that (153.BL2) is false, and no signed lower bound is
claimed.

## 3. Proof and complete derivation

### 3.1 Exact squarefree inversion

Because `A` is zero off a finite interval, all rearrangements below are finite.
The unique squarefree decomposition can first be written as

\[
 \mathcal P^*
 =\sum_{\substack{s<S\\s\ \mathrm{odd}}}
 \sum_{\substack{\tau\geq1\\\tau\ \mathrm{odd}}}
 \mu^2(\tau)\chi_4(\tau)(\tau s^2)^{-3/4}
 A(\tau s^2)D(\tau s^2)e(s\sqrt{N\tau}).
\tag{3.1}
\]

Insert, without truncating any term,

\[
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),
 \qquad \tau=a^2b.
\]

Since `a` is odd, `chi_4(a^2b)=chi_4(b)`. This gives

\[
 \begin{split}
 \mathcal P^*
  ={}&\sum_{\substack{s<S\\s\ \mathrm{odd}}}
     \sum_{\substack{a,b\geq1\\a,b\ \mathrm{odd}}}
 \mu(a)\chi_4(b)(a^2bs^2)^{-3/4}A(a^2bs^2)D(a^2bs^2)\\
 &\hspace{42mm}\times e(as\sqrt{Nb}).
 \end{split}
\tag{3.2}
\]

This retains `s=1`, `a=1`, every Mobius term, and the mask at the original
integer `a^2bs^2`. There is no coprimality condition between `a` and `b` after
the substitution; adding one would make the inversion false.

### 3.2 Recombination of `a` and `s`

Put `t=as`. For a fixed odd `t`, the allowed factorizations are exactly
`s|t`, `s<S`, and `a=t/s`. Equation (3.2) becomes (1.2), with coefficient
(1.1). If `1<t<S`, every divisor `s` of `t` satisfies `s<=t<S`, so

\[
 c_S(t)=\sum_{s\mid t}\mu(t/s)=\sum_{a\mid t}\mu(a)=0.
\]

For `t=1` the same divisor sum is one. This proves (1.3) and identifies (1.5)
exactly. Notice that the cancellation for `1<t<S` occurs **between different
`s`-layers and different `a`-terms**. It is therefore lost if the `a=1` term
or each fixed `s` layer is estimated separately.

Let the fixed dilate supporting `A` be contained in `[cM,CM]`, with fixed
positive `c,C`. For `t>=S`, only `t<=C^{1/2}M^{1/2}` can contribute, and for
each `t` there are

\[
 O(M/t^2+1)
\]

possible integers `b`. Also `|c_S(t)|<=d(t)`. Hence

\[
 \begin{split}
 |\mathcal E_{\geq S}|
 &\ll X^\varepsilon M^{-3/4}
 \sum_{S\leq t\ll M^{1/2}}d(t)(M/t^2+1)\\
 &\ll X^\varepsilon M^{o(1)}
 \left(M^{1/4}S^{-1}+M^{-1/4}\right)
 \ll X^\varepsilon M^{o(1)}.
 \end{split}
\tag{3.3}
\]

The ceiling and strict inequality are favorable: `S>=M^{1/4}`, while the
uncancelled boundary `t=S` (when it exists and is odd) is included in the
tail. The exact mask was never smoothed or moved in this estimate; only
`0<=D<=1` was used. This proves the reduction.

### 3.3 Dyadic block and full power dictionary

It is still useful to audit the unrecombined bilinear proposal, because it
pinpoints what Cauchy and spacing can and cannot own. Fix `s`, and restrict
`a` and `b` to dyadic intervals of lengths/comparable sizes `A_0` and `B`.
After factoring out `M^{-3/4}`, write the block as

\[
 T_s(A_0,B)=\sum_{a\asymp A_0}\sum_{b\asymp B}
 \mu(a)\chi_4(b)W_s(a,b)e(as\sqrt{Nb}),
\tag{3.4}
\]

where `W_s` contains the exact support, zero extension, normalized smooth
weight, and exact `D(a^2bs^2)`. It satisfies `|W_s| << X^epsilon`, but no
uniform bounded-variation assertion in `a` or `b` follows after insertion of
`D`.

The support imposes

\[
 A_0^2Bs^2\asymp M.
\tag{3.5}
\]

For a power ledger put

\[
 M=R^\rho,\qquad A_0=M^\alpha,\qquad s=M^\sigma.
\]

Ignoring fixed constants and endpoint `M^{o(1)}` factors, the complete basic
dictionary is

| quantity | `M,A_0,s` form | `R`-power form |
|---|---:|---:|
| allowed exponents | `0<=sigma<=1/4`, `alpha+sigma<=1/2` | `rho<=780/449` |
| `B` | `M/(A_0^2s^2)` | `R^{rho(1-2alpha-2sigma)}` |
| number of `(a,b)` terms | `A_0B=M/(A_0s^2)` | `R^{rho(1-alpha-2sigma)}` |
| unnormalized target | `M^{3/4}` | `R^{3rho/4}` |
| trivial normalized block | `M^{1/4}/(A_0s^2)` | `R^{rho(1/4-alpha-2sigma)}` |
| phase scale `F=(A_0s sqrt(N))sqrt(B)` | `R^2M^{1/2}` | `R^{2+rho/2}` |
| near-defect angular width | `delta_0 asy M^{1/4}/R^2` | `R^{rho/4-2}` |

At the boundary `rho=780/449`, these specialize to

\[
 F=R^{1288/449},\qquad
 M^{3/4}=R^{585/449},\qquad
 \delta_0\asymp R^{-703/449}.
\tag{3.6}
\]

The trivial `A_0=s=1` loss is `M^{1/4}`, equal to `R^{195/449}` at that
boundary.

### 3.4 Type-I ledger

First discard the mask only provisionally and suppose the remaining amplitude
has bounded variation. The identity

\[
 \chi_4(b)=\frac{e(b/4)-e(-b/4)}{2i}
\tag{3.7}
\]

shows that a fixed-`a` Type-I sum has phases

\[
 f_\pm(b)=as\sqrt{Nb}\mathbin\pm b/4.
\]

The linear twist does not change derivatives of order at least two. On a block
of length `B`, the derivative scale is `F/B`, with
`F asy R^2M^{1/2}` by (3.5).

If an exponent-pair estimate `(kappa,lambda)` of the standard form

\[
 \sum_{b\asymp B}v(b)e(f_\pm(b))
 \ll X^\varepsilon F^\kappa B^{\lambda-\kappa}
\tag{3.8}
\]

is valid for the *unmasked* bounded-variation weight `v`, summing it over the
`A_0` values of `a` gives the normalized block bound

\[
 E_{\rm I}(A_0,s)
 \ll X^\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}
 A_0^{1-2\lambda+2\kappa}s^{-2\lambda+2\kappa}.
\tag{3.9}
\]

In `R`-power variables this is

\[
 R^{\,2\kappa+\rho\{
 \lambda-\kappa/2-3/4
 +\alpha(1-2\lambda+2\kappa)
 -2\sigma(\lambda-\kappa)\}}.
\tag{3.10}
\]

The sign of `1-2lambda+2kappa` is pair-dependent. For the relevant BD pair

\[
 (\kappa,\lambda)=(195/796,235/398),
 \qquad \lambda-\kappa=275/796<1/2,
\]

the `A_0` exponent is

\[
 1-2\lambda+2\kappa=123/398>0.
\]

If the `s`-variable is restricted to a dyadic block `s asy S_0` and summed
absolutely, its `S_0` terms turn the fixed-`s` factor in (3.9) into

\[
 A_0^{123/398}S_0^{1-275/398}
 =(A_0S_0)^{123/398}.
\tag{3.10a}
\]

This factor is minimized at the compulsory `A_0=S_0=1` seam. A uniform proof
must include that seam, and setting `A_0=s=1` in (3.9) gives the necessary
condition

\[
 M^{\eta}\gtrsim R^{2\kappa},
 \qquad
 \eta=3/4-\lambda+\kappa/2>0.
\tag{3.11}
\]

This necessary `A_0=s=1` seam condition is a **lower** bound on `M` relative
to `R`. The hypothesis `M^{449} << R^{780}` is an upper-cone boundary and, by
itself, goes in the opposite direction for (3.11). At `rho=780/449`, the
`A_0=s=1` specialization of (3.8) closes only if

\[
 2\kappa\leq (780/449)\eta;
\tag{3.12}
\]

even then it worsens as `M` is taken smaller.

For example, the elementary third-derivative/exponent-pair ledger
`(kappa,lambda)=(1/6,2/3)` gives

\[
 E_{\rm I}\ll X^\varepsilon R^{1/3}M^{-1/6}s^{-1},
\tag{3.13}
\]

which needs `M>=R^2`; at the displayed lower-cone boundary it still loses
`R^{59/1347}`. The second-derivative estimate gives, including its dual term,

\[
 E_{\rm I,2}\ll X^\varepsilon
 \left(\frac{A_0R}{M^{1/2}}+\frac1{A_0s^2R}\right),
\tag{3.14}
\]

and its first term loses `R^{59/449}` at `A_0=s=1` on the same boundary.
These calculations are not assertions that every possible sign-sensitive
Type-I theorem must fail. They show exactly why the standard smooth derivative
estimates do not supply (1.7) in the stated lower cone.

Most importantly, (3.8)--(3.14) are not yet legal for (3.4), because the exact
mask has not been removed.

### 3.5 Cauchy, diagonal, and absolute-spacing ledger

Let

\[
 \theta_b=s\sqrt{Nb}\pmod 1.
\]

Cauchy in `a`, used to remove the Mobius coefficient, gives

\[
 |T_s|^2\leq A_0
 \sum_{b_1,b_2}\chi_4(b_1)\chi_4(b_2)
 \sum_{a\asymp A_0}
 W_s(a,b_1)\overline{W_s(a,b_2)}
 e(a(\theta_{b_1}-\theta_{b_2})).
\tag{3.15}
\]

If the mask were absent and the inner amplitude had uniformly bounded
variation, taking absolute values would lead to the kernel

\[
 K=\sum_{b_1,b_2}
 \min\!\left(A_0,\|\theta_{b_1}-\theta_{b_2}\|^{-1}\right).
\tag{3.16}
\]

Let

\[
 P(\delta)=\#\{(b_1,b_2):
 \|\theta_{b_1}-\theta_{b_2}\|\leq\delta\}.
\]

Even an ideal spacing estimate of the shape

\[
 P(\delta)\ll X^\varepsilon(B^2\delta+B+C^2)
\tag{3.17}
\]

would yield, by dyadic integration,

\[
 K\ll X^\varepsilon(B^2+A_0B+A_0C^2),
\tag{3.18}
\]

with logarithms absorbed. Here `C` counts points in an off-diagonal exact
collision class. Equations (3.15)--(3.18) yield the three raw terms

\[
 |T_s|\ll X^\varepsilon
 \bigl(A_0^{1/2}B+A_0B^{1/2}+A_0C\bigr).
\tag{3.19}
\]

Their normalized power ledger is

| source | raw bound | normalized bound |
|---|---:|---:|
| pigeonhole/capacity pairs | `A_0^{1/2}B` | `M^{1/4}/(A_0^{3/2}s^2)` |
| diagonal `b_1=b_2` | `A_0B^{1/2}` | `M^{-1/4}/s` |
| exact off-diagonal class, unmasked | `A_0C` | at most `M^{-1/4}(s^{-1}q^{-1/2}+s^{-1})` |

Here `q` is the squarefree kernel of `N`; the exact-collision calculation is
proved in the next subsection. Summing the diagonal over `s<S` costs only a
logarithm. The capacity term is summable in `s` but is power-saving only in
the owner range

\[
 A_0^{3/2}s^2\gtrsim M^{1/4},
 \quad\hbox{equivalently}\quad
 A_0^3s^4\gtrsim M^{1/2}.
\tag{3.20}
\]

In exponent variables its normalized size is

\[
 M^{1/4-3\alpha/2-2\sigma}
 =R^{\rho(1/4-3\alpha/2-2\sigma)}.
\tag{3.21}
\]

The condition (3.20) is not an artifact of a weak upper count. Partition the
circle into `O(A_0)` arcs of length at most `1/A_0`. Cauchy on the occupancies
gives

\[
 P(1/A_0)\gg B^2/A_0
\tag{3.22}
\]

(with the diagonal separately stronger when `B<A_0`). Thus the nonnegative
absolute kernel (3.16) necessarily has `K>>B^2`, in addition to its diagonal
`K>=A_0B`. This proves that the majorant generated by absolute spacing cannot
beat the first two terms of (3.19). It does **not** prove that the signed sum
in (3.15), much less the original sum, is large.

Cauchy in the opposite direction reaches the same barrier by a different
seam. Its `a_1=a_2` diagonal is exactly

\[
 A_0B^2
\]

inside the squared estimate, giving `A_0^{1/2}B` after taking a square root.
The off-diagonal terms then require Type-I estimates with frequencies
`(a_1-a_2)s sqrt(Nb)` and the same exact masks. Hence merely reversing Cauchy
does not remove (3.20).

At `A_0=s=1`, the absolute-spacing capacity loss is `M^{1/4}`
(`R^{195/449}` at the boundary), whereas the diagonal is harmless
`M^{-1/4}`. This isolates the seam correctly: the obstruction is not the
ordinary diagonal.

### 3.6 Exact collisions

Suppose `b_1 ne b_2` and

\[
 s\sqrt N(\sqrt{b_1}-\sqrt{b_2})\in\mathbb Z.
\tag{3.23}
\]

Then `sqrt(Nb_1)-sqrt(Nb_2)` is rational. If two square roots of integers have
a nonzero rational difference, squaring once shows that each square root is
rational, hence integral. Therefore both `Nb_1` and `Nb_2` are squares. If
`N=qv^2` with `q` squarefree, this is equivalent to

\[
 b_i=qu_i^2.
\tag{3.24}
\]

There are no odd such `b_i` if `q` is even; if `q` is odd, their number in a
dyadic `B`-interval is

\[
 C\ll (B/q)^{1/2}+1.
\tag{3.25}
\]

This proves the exact-collision entry of the preceding table in the unmasked
control.

For the actual problem there is a stronger conclusion. For (3.24),

\[
 as\sqrt{Nb_i}\in\mathbb Z,
\]

so `k(a^2b_is^2)^2=Na^2b_is^2` and

\[
 D(a^2b_is^2)=0.
\tag{3.26}
\]

Thus every off-diagonal exact collision is annihilated by the required
large-defect mask. The ordinary diagonal `b_1=b_2` remains for nonexact
points and has precisely the harmless size already recorded.

### 3.7 Near collisions and the exact-mask seam

For `n=a^2bs^2 asy M`, put

\[
 y=as\sqrt{Nb}\asymp R^2M^{1/2}.
\]

Since `k` is the nearest integer,

\[
 |k^2-y^2|=|k-y|(k+y).
\]

Consequently the omitted small-defect condition is exactly a nearest-integer
condition with a slightly varying endpoint and, uniformly on the fixed
support, is comparable to

\[
 \|as\sqrt{Nb}\|\ll \delta_0,
 \qquad \delta_0=\frac{M^{1/4}}{R^2}.
\tag{3.27}
\]

The exact expression remains `|k^2-Na^2bs^2|<=M^{3/4}`; (3.27) is used only
to display its scale.

The inner correlation actually occurring in (3.15) contains

\[
 D(a^2b_1s^2)D(a^2b_2s^2).
\tag{3.28}
\]

As a function of `a`, (3.28) is a product of two cutoff rotation sequences.
The hypotheses on `A` give no uniform bounded-variation bound for this
sequence. In particular, the implication

\[
 \left|\sum_a D(a^2b_1s^2)D(a^2b_2s^2)e(a\Delta)\right|
 \stackrel{\rm invalid}{\ll}
 \min(A_0,\|\Delta\|^{-1})
\tag{3.29}
\]

does not follow by deleting the masks: deleting terms from an exponential sum
can increase its absolute value.

There are two legitimate ways past (3.29), neither supplied by the blind
statement:

1. prove a sign-sensitive correlation estimate with both exact masks kept; or
2. write `D=1-E`, apply a smooth estimate to the full sum, and prove a
   sufficiently strong bound for every resulting near-defect term.

For the second option, an absolute treatment at the dyadic level naturally
introduces

\[
 Z_s(A_0,B)=\#\{(a,b):a\asymp A_0, b\asymp B,
 |k(a^2bs^2)^2-Na^2bs^2|\leq M^{3/4}\}.
\tag{3.30}
\]

The safe order is to split `D=1-E` in (3.1), **before** Mobius inversion. The
near correction then still has the unique squarefree representation and no
artificial factorization multiplicity. A sufficient global input would be an
estimate of the schematic strength

\[
 \#\{\ell\asymp M:\ell=\tau s^2,\ \tau\ \mathrm{squarefree},\ s<S,
 |k(\ell)^2-N\ell|\leq M^{3/4}\}
 \ll X^\varepsilon M^{3/4}.
\tag{3.31}
\]

No such bound has been derived here. If instead the mask is split after
inversion, the Mobius sum must be recombined before absolute values are taken;
replacing it by `|mu(a)|` introduces nonsquarefree factorizations not counted
by (3.31). An upper capacity for possible near pairs is not a substitute for
(3.31) or for a signed correlation bound. This is the first analytic seam at
which the standard masked Type-I/Type-II argument becomes unproved.

### 3.8 Why the exact recombination is stronger than a blockwise split

In the power notation above, `t=as=M^{alpha+sigma}`. All blocks with

\[
 0<\alpha+\sigma<1/4
\]

do not merely admit an estimate: their complete coefficient is exactly zero
after blocks with the same `t` are recombined. All `t>=M^{1/4}` blocks are
summable by (3.3). The exceptional point `alpha=sigma=0`, namely `t=1`, is
exactly (1.7). Thus a Type-I/Type-II partition that estimates fixed `s` and
fixed `a` blocks before respecting (1.1) both loses an exact cancellation and
still cannot touch the surviving endpoint.

## 4. First doubtful or unproved step

The first unproved mathematical statement needed for (153.BL2) is (1.7), the
exact masked `a=s=1` estimate. Squarefree inversion supplies no second
variable for this term.

Within the proposed Cauchy/spacing mechanism, the first invalid transition is
(3.29): applying an unmasked geometric-sum bound to a correlation containing
the exact large-defect masks. If the mask is first split off, the first missing
input becomes the near-defect estimate (3.31), together with its correlation
versions. Even after granting that input, absolute spacing has the rigorous
capacity floor (3.20), so it cannot own `A_0=s=1`. A new estimate for (1.7)
must therefore be genuinely `chi_4`-sensitive (or exploit another arithmetic
mechanism); the generic smooth derivative bounds (3.13)--(3.14) have the wrong
power direction in the stated lower cone.

## 5. Required control tests and outcomes

1. **Exact squarefree inversion — pass.** Every `a`, including `a=1`, is
   present in (3.2); `mu(a)`, `chi_4(b)`, the original argument of the mask,
   and all endpoints are retained. No false coprimality was inserted.

2. **`s=1` and `a=1` seam — pass.** The surviving term is exactly
   `a=s=t=1`. It is not declared sufficient on its own: the full Mobius sum is
   recombined first and its complementary `t>=S` part is proved small.

3. **Mobius-sign control — pass and essential.** For `1<t<S`, cancellation is
   `sum_{a|t} mu(a)=0`. Replacing `mu(a)` by `|mu(a)|` changes the coefficient
   to `sum_{a|t}|mu(a)|`, which is generally nonzero. The proof therefore does
   not also prove the adversarial or unsigned Mobius analogue.

4. **Character control — unresolved exactly where it must be.** `chi_4(b)` is
   retained in (1.7). Every absolute-spacing estimate erases its sign and so
   cannot, by itself, distinguish a false unsigned-character control. Formula
   (3.7) records the only legitimate initial character split; a proof still
   needs cancellation after that split.

5. **Diagonal control — pass.** The Cauchy diagonal is
   `M^{-1/4}/s` after normalization and is logarithmically summable. It is not
   the obstruction.

6. **Exact-collision control — pass.** Exact off-diagonal collisions are
   classified by (3.24), have the stated unmasked capacity, and are identically
   removed by the exact defect mask (3.26).

7. **Near-collision/pigeonhole control — pass as a no-go, not as a lower
   bound.** The unavoidable `B^2/A_0` pair capacity proves only the limitation
   of the nonnegative absolute-energy majorant. It is not used as a signed
   lower bound. The needed upper/correlation input (3.31) remains unproved.

8. **Endpoint and power control — pass.** The strict `s<S`, the ceiling in
   `S`, the uncancelled `t=S` boundary, `t=1`, `B` near one, fixed support
   endpoints, zero extension, and the boundary `M^{449}=R^{780}` are all
   included in (3.3), (3.5), and (3.6). No numerical evidence was used.

## 6. Dependencies and exact artifacts used

The only dependencies are:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/blind_statement.md`.

No external theorem beyond elementary Mobius inversion, divisor bounds,
Cauchy--Schwarz, geometric-sum summation, and elementary square-root algebra
is promoted. The exponent-pair formulas are explicitly conditional method
ledgers, not imported claims used to prove the target. The graph hash was not
read because statement-only isolation forbade access to the claim graph.

## 7. Recommended state effect

**Revise.** Do not promote (153.BL2) from the squarefree Type-II proposal. The
exact collapse (1.2)--(1.6) and the method-specific no-go (1.8), after seam
review, are suitable candidate state effects: replace the purported bilinear
gate by the single owner obligation (1.7), retaining its exact defect mask and
`chi_4` sign. Any next attempt should prove a masked, sign-sensitive
one-variable estimate for (1.7), or prove a mask-removal/near-defect lemma and
then supply an estimate whose power direction genuinely covers
`M^{449} << R^{780}`.

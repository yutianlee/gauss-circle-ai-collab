# Round 152 conductor candidate: arithmetic pruning of the D=1 square-root wave

- Campaign: m9-m1-lower-cone-t1-d1-square-root-wave-gate
- Round: 152
- Role: conductor-selected proof kernel
- Starting graph SHA-256: d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical
- Proposed terminal label: strict_square_root_character_range

## 1. Result and exact scope

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,\qquad M^{819}\ll R^{1424},
\tag{152.C1}
$$

and retain the literal compact-smooth Round-148 profile

$$
 A_U(\ell)=\mathscr A_{1,M,U}(1,\ell),\qquad
 w_U(\ell)=\ell^{-3/4}A_U(\ell),
\tag{152.C2}
$$

extended by zero with its inherited half-open endpoint convention.  The
Round-151 scalar is

$$
 P_U=\sum_{\substack{\ell>0\\\ell\ \operatorname{odd}}}
 \chi _4(\ell)w_U(\ell)e(\sqrt{N\ell}),
\tag{152.C3}
$$

and

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon).
\tag{152.C4}
$$

The external row coefficient $B_{1,U}(1)$ remains attached to $S_U$ and
satisfies $|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon$.

Round 152 proves a new disjoint arithmetic pruning of (152.C3).  Let

$$
 k(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,\qquad
 j(\ell)=k(\ell)^2-N\ell,
\tag{152.C5}
$$

and write uniquely

$$
 \ell=\tau s^2,\qquad
 \tau\ \operatorname{odd\ and\ squarefree},\qquad s\ \operatorname{odd}.
\tag{152.C6}
$$

With $J_M=M^{3/4}$ and $S_M=\lceil M^{1/4}\rceil$, partition the actual
retained support, in this order, into

$$
\begin{aligned}
 \mathcal L_0&=\{\ell:j(\ell)=0\},\\
 \mathcal L_1&=\{\ell:0<|j(\ell)|\le J_M\},\\
 \mathcal L_2&=\{\ell:|j(\ell)|>J_M,\ s\ge S_M\},\\
 \mathcal L_*&=\{\ell:|j(\ell)|>J_M,\ s<S_M\}.
\end{aligned}
\tag{152.C7}
$$

Then, uniformly for every parity and prime-power structure of $N$,

$$
 |P_{\mathcal L_0}|+|P_{\mathcal L_1}|+
 |P_{\mathcal L_2}|\ll_\varepsilon X^\varepsilon.
\tag{152.C8}
$$

Consequently

$$
 \boxed{P_U=P_U^*+O_\varepsilon(X^\varepsilon),}
\tag{152.C9}
$$

where

$$
 P_U^*=
 \sum_{\substack{\ell=\tau s^2\ \operatorname{retained}\\
                  |k(\ell)^2-N\ell|>M^{3/4}\\
                  1\le s<\lceil M^{1/4}\rceil}}
 \chi _4(\tau)(\tau s^2)^{-3/4}
 A_U(\tau s^2)e(s\sqrt{N\tau}).
\tag{152.C10}
$$

On this survivor $\tau\gg M^{1/2}$, and the compulsory $s=1$ layer
remains.  Formula (152.C10) is a strict owner-complete support reduction,
not a bound for $P_U^*$.

Round 152 also proves a new source-legal scale range.  Sargos's
$D$-process applied to Bourgain's pair, followed by the $B$-process,
gives

$$
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right),
\qquad
 BD\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{152.C10a}
$$

The latter pair proves

$$
 \boxed{
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 X^\varepsilon.}
\tag{152.C10b}
$$

Thus

$$
 \boxed{M^{449}\gg R^{780}}
\tag{152.C10c}
$$

is target-safe.  Since

$$
 \frac{780}{449}<\frac{1424}{819},
\tag{152.C10d}
$$

this adds the nonempty range between the new boundary and the older TTY
boundary; the overlap with the Round-151 owner is subtracted exactly once.
Below (152.C10c), the arithmetic pruning (152.C9)--(152.C10) remains the
strict structural progress.

The other required routes close as rigorous method obstructions.
Adjacent pairing leaves a full oscillatory finite difference; one legal
$A$-process makes the character product the constant $(-1)^h$; and the
Mellin functional equation has spectral scale $\sqrt{NM}$, root number
$+1$, and unbalanced dual length $\sqrt{N/M}$, reconstructing (152.C4).
The boundary-optimal audited exponent-pair estimate is (152.C10b); it
does not assert pointwise dominance over every older pair at every scale.  Thus the target
$|P_U|\ll_\varepsilon X^\varepsilon$ remains open only below
$M^{449}\asymp R^{780}$ after the bounded owner is removed.

No $D>1$, $L>1$, growing-$M$ generic, original $t\ge2$, Round-138 cross,
full M9--M1, M9--M2, endpoint, M9, bridge, quarter-target, or global
exponent conclusion follows.

## 2. Exact character algebra

The accepted actual-profile ledger gives finitely many support components
inside a fixed dilation of $[M,2M]$ and

$$
 \|A_U\|_\infty+\operatorname {Var}A_U
 \ll_\varepsilon X^\varepsilon,\qquad
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{152.C11}
$$

The raw absolute capacity and the character-only mass are different:

$$
 \sum_{\ell\ \operatorname{odd}}|w_U(\ell)|
 \ll_\varepsilon M^{1/4}X^\varepsilon,
\tag{152.C12}
$$

whereas bounded partial sums of $\chi _4$ and (152.C11) give

$$
 \left|\sum_{\ell\ \operatorname{odd}}\chi _4(\ell)w_U(\ell)\right|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{152.C13}
$$

Put $F(x)=w_U(x)e(\sqrt{Nx})$, with zero extension.  Since
$\chi _4(4n+1)=1$ and $\chi _4(4n+3)=-1$,

$$
 P_U=\sum_{n\in\mathbb Z}\{F(4n+1)-F(4n+3)\}.
\tag{152.C14}
$$

For $x=4n+1$,

$$
\begin{aligned}
 F(x)-F(x+2)
 ={}&[w_U(x)-w_U(x+2)]e(\sqrt{Nx})\\
 &+w_U(x+2)e(\sqrt{Nx})
 \{1-e(\Delta_2f(x))\},
\end{aligned}
\tag{152.C15}
$$

where

$$
 \Delta_2f(x)=
 \sqrt N(\sqrt{x+2}-\sqrt x)
 =\frac{2\sqrt N}{\sqrt{x+2}+\sqrt x}
 \asymp R^2M^{-1/2}.
\tag{152.C16}
$$

The first line of (152.C15) has total mass
$O_\varepsilon(M^{-3/4}X^\varepsilon)$ by (152.C11).  The multiplier
in the second line is not uniformly small modulo one.  Thus adjacent
pairing is target-equivalent to a new signed phase kernel; replacing the
whole finite difference by a derivative of the smooth profile is
unlawful.

For the legal $A$-process index the odd integers by $\ell=2n+1$.  A shift
$h$ in $n$, equivalently $2h$ in $\ell$, gives exactly

$$
 \chi _4(\ell+2h)\chi _4(\ell)=(-1)^h.
\tag{152.C17}
$$

Hence every shifted correlation is untwisted:

$$
 C_h=(-1)^h
 \sum_{\ell\ \operatorname{odd}}
 w_U(\ell+2h)\overline{w_U(\ell)}
 e\!\left(\sqrt N(\sqrt{\ell+2h}-\sqrt\ell)\right).
\tag{152.C18}
$$

For $1\le H\ll M$, van der Corput differencing and the
second-derivative estimate give

$$
 |P_U|^2\ll_\varepsilon X^\varepsilon
 \left\{
 \frac{M^{1/2}}H+
 R M^{-3/4}H^{1/2}+
 R^{-1}M^{3/4}H^{-1/2}
 \right\}.
\tag{152.C19}
$$

Indeed the shifted phase has

$$
 g_h''(x)\asymp R^2hM^{-5/2},
\tag{152.C20}
$$

and the product weight has supremum plus variation
$O_\varepsilon(M^{-3/2}X^\varepsilon)$.  A target-sized value in
(152.C19) would require simultaneously

$$
 H\gg M^{1/2},\qquad
 H\ll M^{3/2}/R^2,\qquad
 H\gg M^{3/2}/R^2.
\tag{152.C21}
$$

The first two conditions are compatible only when $M\gg R^2$.  Thus this
termwise one-$A$-process closes no point in (152.C1).  Cancellation in
the outer signs $(-1)^h$ would be a new joint theorem, not a consequence
of the $A$-process.

## 3. Exact-square, near-square, and square-factor owners

The nearest integer in (152.C5) is unique.  A tie would give
$4N\ell=(2m+1)^2$, impossible because the left side is divisible by four
and the right side is odd.

Write

$$
 N=a^2n_0,\qquad n_0\ \operatorname{squarefree}.
\tag{152.C22}
$$

Then $N\tau$ is a square if and only if $\tau=n_0$.  Since $\ell$ is
odd, this exact ray is present only when $n_0$ is odd.  Its phase is one,
and its complete mass is

$$
\begin{aligned}
 |P_{\mathcal L_0}|
 &\le n_0^{-3/4}
 \sum_{\substack{s\ \operatorname{odd}\\n_0s^2\ \operatorname{retained}}}
 s^{-3/2}|A_U(n_0s^2)|\\
 &\ll_\varepsilon M^{-1/4}n_0^{-1/2}X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{152.C23}
$$

For nonzero $j$, put

$$
 \rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}.
\tag{152.C24}
$$

For every $N$ and $j$,

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)}.
\tag{152.C25}
$$

To prove (152.C25), take $p^\alpha\Vert N$ and let
$v=\min\{v_p(j),\alpha\}$.  If $v=\alpha$, the zero congruence has
$p^{\lfloor\alpha/2\rfloor}$ roots.  If $v<\alpha$ is odd, it has no
roots.  If $v=2b<\alpha$, write $x=p^by$; there are at most two unit
roots for odd $p$, at most four for $p=2$, and $p^b$ lifts.  The Chinese
remainder theorem gives (152.C25), including every parity of $N$.

Consequently, for $1\le J<N$,

$$
\begin{aligned}
 \sum_{1\le|j|\le J}\rho_N(j)
 &\ll 2^{\omega(N)}
 \sum_{1\le|j|\le J}\sqrt{(|j|,N)}\\
 &\ll J\,2^{\omega(N)}
 \sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JX^\varepsilon.
\end{aligned}
\tag{152.C26}
$$

The actual $k$-support has length $O(\sqrt{NM})<N$ for large $X$ because
$M\le R^2\asymp N^{1/2}$.  Thus each root class modulo $N$ contributes only
$O(1)$ possible $k$, and fixed $(j,k)$ determines
$\ell=(k^2-j)/N$.  All support, oddness, nearest-integer, profile, and
endpoint tests only delete candidates.  Taking $J=M^{3/4}<N$ in
(152.C26) proves

$$
 \#\mathcal L_1\ll_\varepsilon M^{3/4}X^\varepsilon,\qquad
 |P_{\mathcal L_1}|\ll_\varepsilon X^\varepsilon.
\tag{152.C27}
$$

Finally, for fixed $s\ge S_M$, actual support $\tau s^2\asymp M$
permits $O(1+M/s^2)$ integers $\tau$.  Hence

$$
 \#\{\ell=\tau s^2\ \operatorname{retained}:s\ge S_M\}
 \ll\sum_{S_M\le s\ll\sqrt M}\left(1+\frac M{s^2}\right)
 \ll M^{3/4}.
\tag{152.C28}
$$

Intersecting this owner with $|j|>M^{3/4}$ makes it disjoint from the
first two owners and only decreases its mass.  Equations
(152.C11) and (152.C28) prove

$$
 |P_{\mathcal L_2}|\ll_\varepsilon X^\varepsilon.
\tag{152.C29}
$$

This proves (152.C8)--(152.C10).  It is essential that (152.C26) counts
the integral square defect.  The weaker geometric bound on the inner
$s$-progression has no saving when $\tau\asymp M$ and $s=1$.

## 4. Mellin conductor, duality, and derivative powers

Let

$$
 T:=\sqrt{NM}\asymp R^2M^{1/2},\qquad
 Q=2\sqrt{N/M}\asymp R^2M^{-1/2}.
\tag{152.C30}
$$

After scaling $\ell=My$, Mellin inversion places the transform on
$|t|\asymp T$, in a band of width $\asymp T$, with stationary size
$T^{-1/2}$ at unit profile scale.  The primitive odd character
$\chi _4$ has completed function

$$
 \Lambda(s,\chi _4)=
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi _4),
 \qquad
 \Lambda(s,\chi _4)=\Lambda(1-s,\chi _4),
\tag{152.C31}
$$

because $\tau(\chi _4)=2i$ and its root number is
$2i/(i\sqrt4)=+1$.  The analytic conductor is $\asymp T$ and a balanced
approximate functional equation has length $T^{1/2}\asymp RM^{1/4}$.
Pointwise or mean-square absolute integration loses $R$ even under a
hypothetical Lindelof bound.

Using the functional equation without absolute values gives the
unbalanced dual length

$$
 T/M\asymp\sqrt{N/M}\asymp Q.
\tag{152.C32}
$$

Equivalently, exact character Poisson and stationary phase give

$$
 P_U=e(1/8)N^{-1/4}
 \sum_{\substack{q>0\\q\ \operatorname{odd}}}
 \chi _4(q)A_U(4N/q^2)e(N/q)
+O_\varepsilon(X^\varepsilon),
\tag{152.C33}
$$

with $q\asymp Q$.  This is (152.C4) solved for $P_U$.  The actual
Round-148 ledger owns the lower symbols, nonstationary terms, stationary
buffers, transitions, tails, and endpoints.  Applying the principal
transform again returns the original phase and principal symbol; the
functional equation and the $B$-process are the same self-return in
different coordinates.

The elementary capacities are

$$
 |P_U|\ll_\varepsilon
 \min\{M^{1/4},RM^{-1/2}\}X^\varepsilon.
\tag{152.C34}
$$

They meet at $M=R^{4/3}$ with loss $R^{1/3}$ and are target-sized only at
the bounded or top endpoints.

For the square-root derivative class an exponent pair
$(\kappa,\lambda)$ gives

$$
 |P_U|\ll_\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon
\tag{152.C35}
$$

after the two mod-four classes are resolved, the unweighted interval
estimate is applied, and the actual profile is inserted by Abel
summation.  Bourgain's pair gives

$$
 |P_U|\ll_\varepsilon
 \left(\frac{R^{52}}{M^{29}}\right)^{1/168}
 X^\varepsilon.
\tag{152.C36}
$$

The $B$-dual of the Tao--Trudgian--Yang pair is

$$
 B\!\left(\frac{89}{1282},\frac{997}{1282}\right)
 =\left(\frac{178}{641},\frac{365}{641}\right),
\tag{152.C37}
$$

and gives

$$
 |P_U|\ll_\varepsilon
 \left(\frac{R^{1424}}{M^{819}}\right)^{1/2564}
 X^\varepsilon.
\tag{152.C38}
$$

This is target-sized exactly at the already owned TTY boundary.  It has
a positive power loss below that boundary.  The new audited improvement
uses Sargos's $D$-process before duality.  Tao--Trudgian--Yang Lemma 14
and Table 1 give

$$
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right);
\tag{152.C38a}
$$

Lemma 15 and $B(k,\lambda)=(\lambda-1/2,k+1/2)$ give the global pair in
(152.C10a).  The maximum in the $D$-process causes no hidden gap: on
$0\le\alpha\le1/2$,

$$
 \left(\frac{18}{199}+\frac{521}{796}\alpha\right)
 -\left(\frac1{12}+\frac23\alpha\right)
 =\frac{17-29\alpha}{2388}>0.
\tag{152.C38aa}
$$

Thus the explicit Lemma-14 maximum check (152.C38aa) makes the $D$-line
control the lower half of the $\beta$ interval; the Lemma-15 symmetry
bridge controls the upper half, and the two lines meet at
$\alpha=1/2$.  Lemma 15 then licenses both $D$ and $BD$ as global
exponent pairs.  Substitution into (152.C35) gives

$$
 |P_U|\ll_\varepsilon
 R^{390/796}M^{-449/1592}X^\varepsilon
 =
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 X^\varepsilon.
\tag{152.C38b}
$$

In the source's exponent-sum coordinates, the relevant Table-1 line is

$$
 \beta(\alpha)\le
 \frac{18}{199}+\frac{521}{796}\alpha
 \quad
 \left(
 \frac{1508}{3825}\le\alpha<
 \frac{62831}{155153}
 \right).
\tag{152.C38c}
$$

It meets the required reciprocal line
$\beta(\alpha)\le(1+\alpha)/4$ at

$$
 \alpha=\frac{127}{322},\qquad
 M=R^{780/449}.
\tag{152.C38d}
$$

This is the exact audited exponent-pair boundary; for smaller $M$ the
printed Table-1 envelope is above the required line.  Direct second- and
third-derivative estimates give respectively

$$
 |P_U|\ll_\varepsilon
 (RM^{-1/2}+R^{-1})X^\varepsilon,
\tag{152.C39}
$$

$$
 |P_U|\ll_\varepsilon
 (R^{1/3}M^{-1/6}+R^{-1/3}M^{1/6})X^\varepsilon,
\tag{152.C40}
$$

so neither reaches the target below $M\asymp R^2$.  The audited mixed
Burgess, pointwise Dirichlet-$L$, higher Voronoi, and fixed-parameter
nonlinear-resonance sources do not accept or improve the literal
coefficient, growing square-root twist, actual weight, and endpoint class.

## 5. First open step and source boundary

After subtracting bounded $M$ and (152.C10c), the first unproved estimate
is exactly

$$
 |P_U^*|\ll_\varepsilon X^\varepsilon
\tag{152.C41}
$$

for (152.C10).  Already its $s=1$ layer is

$$
 \sum_{\substack{\tau\asymp M\\
                  \tau\ \operatorname{odd\ and\ squarefree}\\
                  |k(\tau)^2-N\tau|>M^{3/4}}}
 \chi _4(\tau)\tau^{-3/4}A_U(\tau)e(\sqrt{N\tau}),
\tag{152.C42}
$$

with absolute capacity $M^{1/4}X^\varepsilon$.  There is no inner
square-factor sum on this layer.  A proof needs cancellation across
$\tau$, joint cancellation among the untwisted correlations (152.C18),
or an equivalent signed reciprocal-wave theorem.  A second principal
transform and the beta functional equation merely return the same
interface.

The exact source conclusion is intentionally narrow: Bourgain together
with the source-printed $D$ and $B$ processes gives (152.C10b), while the
older Bourgain and TTY placements give (152.C36) and (152.C38).
Pointwise or mean-square $L$-function estimates lose the oscillation in
the Mellin kernel, while using that oscillation through the functional
equation gives (152.C33).  A direct theorem with a different
coefficient, a complete average, a conjugate pair, a varying centre, or
a hard-endpoint-free weight is not a theorem for (152.C41).

## 6. Required controls and review gate

The conductor has reproduced:

1. the endpoint-complete adjacent pairing (152.C14)--(152.C16);
2. the exact character loss (152.C17), shifted phase, and powers
   (152.C19)--(152.C21);
3. the all-parity prime-power root count (152.C24)--(152.C27);
4. the exact square ray and disjoint square-factor tail
   (152.C23), (152.C28)--(152.C29);
5. the Mellin scale, root number, and reciprocal dual length
   (152.C30)--(152.C33);
6. the Bourgain, TTY, $D$, and $BD$ exponent-pair translations
   (152.C36)--(152.C38d); and
7. the owner split between a target-safe absolute sector and the open
   signed survivor.

The terminal mathematical and hostile reviews verify the prime-power
root multiplicity, the $k$-interval modulo-$N$ placement, rounding at
$M^{1/4}$, absence of owner overlap, the actual profile and
$B_{1,U}(1)$ seam, and every exponent.  The terminal source review
verifies the $D$-process maximum, the Remark-16/Lemma-15 global inference,
$B$ placement, Table-1 cell, model-phase normalization, and every source
no-match.  All three terminal verdicts are GREEN.  An absolute capacity
is never treated as a signed lower bound.

## 7. Recommended state effect

With those reviews GREEN:

- create a proved reduction for the exact disjoint decomposition
  (152.C7)--(152.C10), including the target-safe exact-square,
  nonzero-small-defect, and large-square-factor sectors;
- promote the strict source-legal scale range
  $M^{449}\gg R^{780}$ from (152.C10a)--(152.C10d), crediting only its
  previously unowned sliver below the TTY boundary;
- create or update a scoped obstruction recording adjacent-pair
  character loss, one-$A$-process character erasure, Mellin and
  principal-$B$ self-return, elementary capacities, and the exact
  exponent-pair boundary;
- update the Round-151 reciprocal self-return and large-wrap frontier so
  that the first $D=L=1$ survivor is (152.C10) below
  $M^{449}\asymp R^{780}$;
- reject claims that adjacent pairing differentiates only the smooth
  weight, that even-shift differencing preserves a variable character,
  that exact squares or the square-factor tail obstruct the target, that
  the beta functional equation supplies an independent saving, that a
  source theorem with mismatched coefficients or endpoints applies, or
  that a capacity is a signed lower bound; and
- make no downstream theorem or exponent change.

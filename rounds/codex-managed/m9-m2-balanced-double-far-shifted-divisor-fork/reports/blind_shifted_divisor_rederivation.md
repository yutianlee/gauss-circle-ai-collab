# 1. Result: exact charts and a dispersion no-go at the supplied level

Let

\[
 H={\sqrt L\over2},\qquad
 W(h,k)=\eta\!\left({(h,k)\over H}\right)A(h,k),
 \qquad \mathcal S=\{(h,k)\in\mathbb N^2:A(h,k)\ne0\}.
\]

There are exact bijective divisor-pair and increment charts for the supplied
sum, given below.  On every nonzero increment term one has

\[
 h\ \hbox{odd},\qquad p=h'-h\ \hbox{even},\qquad
 \chi _4(h)\chi _4(h+p)=(-1)^{p/2}.
\]

Thus the character is constant on a fixed shift.  It cannot provide a power
saving inside a fixed \((n,r)\)-fibre, whose cardinality is in any case at
most \(\tau(n)\tau(n+r)\ll_\varepsilon L^\varepsilon\).  The generic
double-far increment chart still has \(L^4\) capacity.  The two coordinate
boundary branches \(p=0\) and \(q=0\) have \(L^3\) capacity and no hidden
extra saving is needed from them.

There is an important distinction between two kinds of zero mode.  The
literal two-dimensional coefficient zero mode satisfies

\[
 \left|\sum_{|r|>L}\sum_n C(n,r)\right|
 \ll_\varepsilon L^3X^\varepsilon .
\]

In contrast, the zero-*difference* (self-diagonal) term created by squaring a
dispersion norm is

\[
 D_{\rm df}
 =\sum_{\substack{(h,k),(h',k')\in\mathcal S\\
 |h'k'-hk|>L,\ |hk'-h'k|>L}}
 |a(h,k)|^2|a(h',k')|^2
 =M_2^2+O(L^3),
 \qquad M_2=\sum_{(h,k)\in\mathcal S}|a(h,k)|^2.
\]

Consequently, if the actual block has its natural nondegenerate mass
\(M_2\asymp L^2\), this dispersion diagonal has equal \(L^4\) capacity and
the character has disappeared from it.  The blind statement does not give a
lower bound for \(M_2\), so it does not by itself prove that the particular
physical block has this main term.

The sharp uniform bound obtainable here for the original oscillatory generic
branch is therefore only

\[
 |E_{\rm df}|\ll L^4.
\]

The target \(L^3X^\varepsilon\) is not derived.  What is rigorously ruled out
is a claimed factor \(L\) coming merely from the visible \(\chi _4\) signs,
from pointwise divisor-fibre cancellation, or from a coefficient-blind
dispersion that pays its self-diagonal separately.  A further outer
shift/mode cancellation theorem could still save the factor, but it is not a
consequence of the supplied hypotheses.

# 2. Exact statement and hypotheses

The conclusions use only the following supplied data.

* \(L\ge16\), \(R\asymp L^3\), and \(K/L\) lies in a fixed compact subset of
  \((0,\infty)\).
* \(A\) is real, smooth, supported on \(h\asymp L\), \(k\asymp K\), and has
  uniformly bounded rescaled derivatives (including order zero).
* The fixed cutoff \(\eta\) is bounded on the range in which it is evaluated.
  This is the only analytic property of \(\eta\) used in the zero-mode bound;
  its gcd argument is never removed or replaced.
* All four endpoint variables are positive.  Both endpoint pairs must remain
  in the same fixed support \({\cal S}\).  No separate physical blocks or
  pre-existing gcd shells are combined.  The zero-mode proof decomposes the
  one literal gcd weight exactly and explicitly pays the resulting harmonic
  sums.
* Put \(n=hk\), \(n+r=h'k'\), and \(\rho=hk'-h'k\).  Only
  \(|r|>L\), \(|\rho|>L\) are included.

The estimate for the dispersion diagonal is a capacity statement unless the
additional normalization \(M_2\asymp L^2\) is verified for the actual block.
No such lower normalization is part of the blind statement.

# 3. Proof and derivation

## 3.1 Exact finite chart I: full products to divisor pairs

For \(n>0\), \(r\in\mathbb Z\), and \(n+r>0\), define

\[
 \rho(n,r;h,h')
 ={h(n+r)\over h'}-{h'n\over h}
 ={h^2(n+r)-h'^2n\over hh'}.
\]

The divisor-pair coefficient is exactly

\[
\begin{aligned}
 C(n,r)=
 \sum_{\substack{h\mid n,\ h'\mid n+r\\
 (h,n/h)\in{\cal S},\ (h',(n+r)/h')\in{\cal S}\\
 |\rho(n,r;h,h')|>L}}
 &\chi _4(h)\chi _4(h')
 \eta\!\left({(h,n/h)\over H}\right)
 \overline{\eta\!\left({(h',(n+r)/h')\over H}\right)}\\
 &\times A(h,n/h)A(h',(n+r)/h').
\end{aligned}
\]

(For the usual real cutoff the conjugation on the second \(\eta\) may be
deleted.)  Hence

\[
 E_{\rm df}=\sum_{\substack{r\in\mathbb Z\\|r|>L}}
 \sum_{\substack{n>0\\n+r>0}}
 e\!\left(R(\sqrt n-\sqrt{n+r})\right)C(n,r).
\]

This is an identity: divisibility recovers uniquely \(k=n/h\) and
\(k'=(n+r)/h'\).  In particular, the determinant gate is the displayed
rational-looking integer \(\rho(n,r;h,h')\); it cannot be dropped after the
substitution.

For a finite sign chart, put \(u=h'/h>0\) and \(v=k'/k>0\).  Since \(n=hk\),

\[
 r=n(uv-1),\qquad \rho=n(v-u).
\]

Thus the four allowed sign sectors are exactly

| sector | product condition | determinant condition | gates |
|---|---:|---:|---:|
| \(r>0,\rho>0\) | \(uv>1\) | \(v>u\) | \(n(uv-1)>L,\ n(v-u)>L\) |
| \(r>0,\rho<0\) | \(uv>1\) | \(v<u\) | \(n(uv-1)>L,\ n(u-v)>L\) |
| \(r<0,\rho>0\) | \(uv<1\) | \(v>u\) | \(n(1-uv)>L,\ n(v-u)>L\) |
| \(r<0,\rho<0\) | \(uv<1\) | \(v<u\) | \(n(1-uv)>L,\ n(u-v)>L\) |

The support also forces \(n,n+r\asymp LK\asymp L^2\), so
\(L<|r|\ll L^2\) and \(L<|\rho|\ll L^2\).  Negative shifts retain the
separate condition \(n+r>0\).

## 3.2 Exact finite chart II: endpoint increments

Set

\[
 h'=h+p,\qquad k'=k+q,
\]

where \(p,q\in\mathbb Z\), \(h+p>0\), and \(k+q>0\).  Then exactly

\[
 r=hq+kp+pq,
 \qquad
 \rho=hq-kp,
\]

and also

\[
 r-\rho=p(k+k'),\qquad r+\rho=q(h+h').
\]

Consequently

\[
\begin{aligned}
E_{\rm df}
=\sum_{\substack{h,k\ge1,\ p,q\in\mathbb Z\\
(h,k),(h+p,k+q)\in{\cal S}\\
|hq+kp+pq|>L,\ |hq-kp|>L}}
&\chi _4(h)\chi _4(h+p)
\eta\!\left({(h,k)\over H}\right)
\overline{\eta\!\left({(h+p,k+q)\over H}\right)}\\
&\times A(h,k)A(h+p,k+q)\\
&\times e\!\left(R\left(\sqrt{hk}-\sqrt{(h+p)(k+q)}\right)\right).
\end{aligned}
\]

The parity/character chart is

| parity | \(p\bmod4\) | \(\chi _4(h)\chi _4(h+p)\) |
|---|---:|---:|
| \(h\) even | any | \(0\) |
| \(h\) odd | \(0\) | \(+1\) |
| \(h\) odd | \(2\) | \(-1\) |
| \(h\) odd | \(1\) or \(3\) | \(0\) |

Thus on the nonzero support \(h\) is odd, \(p\) is even, and

\[
 \chi _4(h)\chi _4(h+p)=(-1)^{p/2}
 =\cos(\pi p/2)
 ={e(p/4)+e(-p/4)\over2}.
\]

In particular a Fourier transform in \(p\) does not destroy a zero mode: it
translates it to the two quarter frequencies \(\pm1/4\) (or to frequency
\(1/2\) after writing \(p=2s\)).

The exact sign and boundary chart following from \(r\pm\rho\) is

| \(p\) | \(q\) | exact sector |
|---:|---:|---|
| \(>0\) | \(>0\) | \(r>|\rho|\) |
| \(>0\) | \(<0\) | \(\rho<-|r|\) |
| \(<0\) | \(>0\) | \(\rho>|r|\) |
| \(<0\) | \(<0\) | \(r<-|\rho|\) |
| \(=0\) | \(\ne0\) | \(r=\rho=hq\) |
| \(\ne0\) | \(=0\) | \(r=-\rho=kp\) |
| \(=0\) | \(=0\) | \(r=\rho=0\), excluded |

Every row is still subject to positivity, both exact support indicators, both
gcd weights, and the two strict far gates.

## 3.3 The shifted-divisor fibre and where cancellation can occur

For fixed \(r,h,h'\), let \(d=(h,h')\), \(h=du\), and \(h'=dv\), with
\((u,v)=1\).  The product equation is

\[
 h'k'-hk=r\quad\Longleftrightarrow\quad vk'-uk=r/d.
\]

It has no solutions unless \(d\mid r\).  Given one solution
\((k_0,k'_0)\), all solutions are

\[
 k=k_0+vt,qquad k'=k'_0+ut,qquad t\in\mathbb Z.
\]

Along this fibre

\[
 n=du(k_0+vt)=n_0+duv\,t,
\]

and the determinant gate remains

\[
 \left|d(uk'_0-vk_0)+d(u^2-v^2)t\right|>L.
\]

The two gcd weights remain
\((du,k_0+vt)\) and \((dv,k'_0+ut)\); replacing them by a function only of
\(d\), or smoothing away their residue dependence, is not an identity.  If
the character is nonzero, its value on this whole \(t\)-fibre is the single
constant

\[
 \chi _4(h)\chi _4(h')=\chi _4(u)\chi _4(v)=(-1)^{(h'-h)/2}.
\]

There are \(O(1+d)\) admissible \(t\)'s.  Summing over
\(h,h'\) gives the rigorous coefficient-blind bound

\[
 \#\{(h,k,h',k')\hbox{ in the block}:h'k'-hk=r\}
 \ll L^2\tau(|r|)\ll_\varepsilon L^{2+\varepsilon}.
\]

Indeed, for each \(d\mid r\) there are
\(O((L/d+1)^2)\) endpoint pairs and \(O(1+d)\) points on each fibre.  Thus a
fixed-shift zero mode still has \(L^2\) capacity; summing its absolute value
over the \(O(L^2)\) possible shifts retains \(L^4\) capacity.

At fixed \((n,r)\) the outer phase is constant and the divisor chart contains
at most \(\tau(n)\tau(n+r)\ll_\varepsilon L^\varepsilon\) terms.  It follows
that a power \(L\) cannot be attributed to pointwise inner-fibre
cancellation.  It must come from an outer signed sum over \(n,r\), or from a
joint transform that keeps that signed structure.

## 3.4 Zero modes and dispersion diagonals

First consider the genuine two-dimensional zero Fourier coefficient of
\(C\), namely the phase-free sum over both \(n\) and \(r\).  Put

\[
 S_0=\sum_{h,k}a(h,k).
\]

Partition by \(g=(h,k)\), write \(h=gu,k=gv\), and insert
\(1_{(u,v)=1}=\sum_{d\mid u,v}\mu(d)\).  By multiplicativity of \(\chi _4\),

\[
 S_0=\sum_{g,d}\chi _4(g)\eta(g/H)\mu(d)\chi _4(d)
 \sum_{s,t}\chi _4(s)A(gds,gdt),
\]

where the support makes \(gd\ll L\).  For fixed \(g,d,t\), bounded partial
sums of \(\chi _4\) and summation by parts give

\[
 \sum_s\chi _4(s)A(gds,gdt)\ll1.
\]

This remains valid for a slanted smooth symbol: along the \(s\)-line its
total variation is \(O(1)\) by the rescaled derivative hypothesis.  There are
\(O(1+K/(gd))\) possible \(t\)'s.  Therefore

\[
 |S_0|
 \ll \sum_{g\ll L}\sum_{d\ll L/g}\left(1+{K\over gd}\right)
 \ll L\log^2(2L).
\]

Without the two far gates, the phase-free pair sum is \(|S_0|^2\).  The raw
number of pairs in either deleted corridor is \(O(L^3)\): after choosing
\(h,k,h'\), either inequality restricts \(k'\) to an interval of length
\(O(L/h')=O(1)\) or \(O(L/h)=O(1)\).  Hence

\[
 \left|\sum_{|r|>L}\sum_n C(n,r)\right|
 \ll L^2\log^4(2L)+L^3
 \ll_\varepsilon L^3X^\varepsilon.
\]

This use of the already-owned corridors is only a zero-mode audit; it is not
counted as a new saving for the oscillatory generic branch.

Now square a coefficient dispersion norm.  The equality-pair diagonal in
\(\sum_{n,r}|C(n,r)|^2\) is exactly \(D_{\rm df}\) from Section 1.  The same
corridor count gives

\[
 0\le M_2^2-D_{\rm df}\ll L^3.
\]

Thus this zero-difference mode is \(\asymp L^4\) whenever the actual block
has \(M_2\asymp L^2\).  Since it contains \(|\chi _4(h)|^2|\chi _4(h')|^2\),
the proposed character cancellation is absent.  An upper-bound argument
which pays this diagonal separately has not saved the required factor.

For comparison, in a formally smooth outer \(n\)-transform, with

\[
 \psi_r(n)=R(\sqrt n-\sqrt{n+r}),
\]

the support gives

\[
 |\psi'_r(n)|\asymp |r|,
 \qquad
 |\psi''_r(n)|\asymp {|r|\over L^2}.
\]

The ordinary dual frequency zero is nonstationary for \(|r|>L\).  There are
\(O(|r|)\) possible stationary dual modes, each with smooth stationary-phase
capacity \(O(L/\sqrt{|r|})\).  Paying them in \(\ell^1\) gives

\[
 \sum_{L<|r|\ll L^2} |r|{L\over\sqrt{|r|}}
 \asymp L^4.
\]

Thus an invertible Poisson/B-process plus absolute values reproduces equal
capacity.  The first scale at which the missing factor could lawfully enter
is cancellation among these outer stationary modes (or jointly across
shifts).  Applying this smooth calculation to the literal \(C(n,r)\) is not
lawful without a theorem handling its divisor jumps, both gcd weights, the
determinant gate, endpoint crossings, both signs of \(r\), and all
\(L<|r|\ll L^2\) uniformly at \(R\asymp L^3\).

## 3.5 Capacity table

| branch or mode | exact character/main term | capacity | conclusion |
|---|---|---:|---|
| \(h\) even or \(p\) odd | identically zero | \(0\) | parity deletion only |
| generic \(p,q\ne0\), \(h\) odd, \(p\) even | \((-1)^{p/2}\), constant in \(h,k\) at fixed \(p\) | \(L^4\) | required factor still missing |
| \(p=0,q\ne0\) | \(+1\), \(r=\rho=hq\) | \(L^3\) | allowed double-far boundary; already at target |
| \(q=0,p\ne0\) | \((-1)^{p/2}\), \(r=-\rho=kp\) | \(L^3\) | allowed double-far boundary; already at target |
| \(|r|\le L\) or \(|\rho|\le L\) | prior-owned corridor | \(L^3\) raw | excluded, not a new saving |
| fixed \((n,r)\) divisor fibre | at most \(L^\varepsilon\) signs; phase constant | \(L^\varepsilon\) per fibre, \(L^4\) total raw | no fibrewise power saving |
| fixed-\(r\), zero \(n\)-frequency coefficient sum | character is constant on each \(p\)-shift | at most \(L^{2+\varepsilon}\) per \(r\), hence \(L^4\) in shiftwise \(\ell^1\) | unresolved main-term family |
| joint \((n,r)\) coefficient zero mode | actual smooth \(A\) and both gcd weights retained | \(O_\varepsilon(L^3X^\varepsilon)\) | zero mode itself is not an equal-capacity obstruction |
| \(p\)-Fourier rational modes | mass moved to \(\pm1/4\) | same power capacity as the corresponding untwisted mode | character translates spectrum; it does not erase it |
| dispersion zero-difference diagonal | \(M_2^2+O(L^3)\) | \(L^4\) if \(M_2\asymp L^2\) | equal-capacity obstruction to diagonal-paying proofs |
| formal smooth outer dual zero | nonstationary for \(|r|>L\) | negligible only in the smooth model | not directly applicable to arithmetic \(C\) |
| formal generic outer stationary modes | \(O(|r|)\) modes of size \(O(L/\sqrt{|r|})\) | \(L^4\) in \(\ell^1\) | an additional noninvertible cancellation theorem is required |

# 4. First doubtful or unproved step

The first failed seam is the inference

\[
 \text{``two visible }\chi _4\text{ factors''}
 \quad\Longrightarrow\quad
 \text{a factor }L\text{ inside }C(n,r).
\]

After the exact increment substitution those factors are the single constant
\((-1)^{p/2}\) on every surviving shift, while a fixed divisor fibre has only
\(L^\varepsilon\) terms.  That inference is therefore false as a power-count
argument.

The next, genuinely unproved step would be a signed outer dispersion estimate
which produces cancellation among the fixed-shift or stationary dual modes
without paying the \(L^4\) self-diagonal.  No such transform, normalization,
large-sieve inequality, or shifted-divisor theorem is contained in the blind
statement.  In addition, the exact physical formula and a lower/upper
normalization for its \(M_2\) are absent, so the conditional equal-capacity
diagonal cannot be promoted to an unconditional statement about that block.

# 5. Control tests and outcomes

| required control | exact test | outcome and implication |
|---|---|---|
| `literal_full_product_to_divisor_pair_identity` | substitute \(k=n/h\), \(k'=(n+r)/h'\) with divisibility and positivity | Passed exactly; there is no lost multiplicity or Jacobian. |
| `determinant_gate_after_divisor_substitution` | multiply \(\rho\) by \(hh'\) | Passed: \(hh'\rho=h^2(n+r)-h'^2n\); the strict gate remains. |
| `increment_chart_and_parity_character` | compute \(r,\rho,r\pm\rho\) and all residues of \(p\bmod4\) | Passed; nonzero terms have odd \(h\), even \(p\), and constant sign \((-1)^{p/2}\). |
| `gcd_cutoff_and_slanted_symbol_retention` | trace both endpoints through both charts | Passed; the arguments remain \((h,k)\) and \((h+p,k+q)\), and the proof of the joint zero mode uses only linewise variation of the full slanted \(A\). |
| `inner_vs_outer_cancellation` | freeze \((n,r)\) | Failed for the proposed inner power saving: the phase is constant and the fibre has only \(L^\varepsilon\) terms.  Any power saving must be outer. |
| `zero_frequency_and_main_term` | separate joint coefficient zero, fixed-shift zero, quarter-frequency character modes, and squared zero-difference diagonal | Joint zero is \(O(L^3X^\varepsilon)\); fixed-shift \(\ell^1\) and the dispersion diagonal retain equal capacity; none may be conflated. |
| `shift_range_and_conductor_uniformity` | use both endpoint supports before estimating derivatives | Passed as an audit: \(L<|r|\ll L^2\), \(n,n+r\asymp L^2\), \(|\psi'_r|\asymp|r|\), \(|\psi''_r|\asymp|r|/L^2\).  No cited theorem was assumed uniform on this full range. |
| `linear_vs_energy_capacity` | compare \(L^2\to L^{3/2}\) for a linear block and \(L^4\to L^3\) for its energy | The generic chart stays at \(L^4\); parity changes constants only. |
| `actual_symbol_vs_phase_adapted_control` | compare the retained real smooth \(A\) with coefficients multiplied by \(e(-R\sqrt{hk})\) | The phase-adapted adversary would remove the outer phase and expose \(L^4\), but it violates the real rescaled-smooth symbol hypothesis (its first derivatives have conductor about \(R\)).  It is a falsification control, not a counterexample to the stated object.  The dispersion diagonal, however, already uses the actual \(|A|^2\). |
| `double_far_owner_and_corridor_scope` | keep both strict gates in every chart | Passed; corridor counts are used only to audit zero modes and are not advertised as new progress on the generic branch. |
| `fixed_block_and_no_shellwise_l1` | inspect every summation in the derivation | Passed with an explicit cost: one \({\cal S}\), one \(A\), and the literal two gcd factors are retained.  The exact-\(g\) decomposition in the joint zero-mode proof is made only after the one-count identity and its harmonic \(\ell^1\) cost \(O(\log^2L)\) is displayed; no physical blocks or pre-existing shells are merged. |
| `critical_j1_and_exact_square_j2_boundary` | compare scope with the supplied object | The report concerns only the persistent \(j=1\) object.  It neither imports nor re-estimates the separately owned exact-square \(j=2\) contribution. |
| `downstream_scope` | test whether the result implies the requested energy estimate or the Gauss-circle goal | It does not.  It supplies exact charts, a zero-mode bound, and a no-go for three insufficient mechanisms only. |

The signed/unsigned control is decisive: replacing the character product by
absolute values leaves \(L^4\) generic capacity, while the true sign becomes
a shift character rather than an inner-variable character.  No numerical
test was used.

# 6. Dependencies and exact artifacts used

The following files were read completely and were the only mathematical
context used:

* `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/briefs/blind_shifted_divisor_rederivation.md`
* `problems/gauss_circle.md`
* `state/control_models.md`
* `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/blind_statement.md`

No proof graph, strategy file, derivation packet, conductor candidate,
Round-114 report, sibling report, web source, or numerical computation was
used.

# 7. Recommended state effect

**Revise.**  Retain the two exact charts, the character/quarter-frequency
classification, the rigorous joint zero-mode bound, and the conditional
\(M_2^2\) dispersion-diagonal obstruction.  Do not promote a factor-\(L\)
shifted-divisor estimate from this evidence.  Any successor must state an
explicit noninvertible outer transform and prove its normalization,
off-diagonal control, actual-symbol main-term evaluation, and uniformity for
all \(L<|r|\ll L^2\) before the \(L^3X^\varepsilon\) target can be claimed.

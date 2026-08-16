## Result

**Source-audited no-go for every proposed black-box route; retain (82.4)
open.** Under the hypotheses actually stated in the Round-82 packet, the
ordinary Deshouillers--Iwaniec/Kuznetsov large sieve, Pascadi's current
non-abelian amplification theorem, and Blomer--Pascadi's current
quadratic-character theorem do not imply

\[
 \mathfrak E_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon J^2/T
 \qquad (J^{13/18}<C\leq J^{3/4}).                 \tag{1.1}
\]

The ordinary large sieve has exactly the packet's capacity

\[
 BQ^2T=CQ^2=B\,{J^2\over T},                       \tag{1.2}
\]

and therefore loses the factor $B=C/T$. The two recent bilinear theorems
concern one fixed modulus and a single Kloosterman kernel $S(am,n;c)$.
The Round-82 energy instead varies the modulus $4b$, has one fixed
Kloosterman argument $k$, has an $n$-interval of length and magnitude
$Q^2\gg B$, and, after squaring, contains a product of two Kloosterman
sums with a joint $b,n_1,n_2$ symbol. Their literal fixed-column
specializations give no power saving.

Pascadi's modulus-average corollary also does not help: its common divisor
parameter is $q=4$, not $q\asymp B$, and its bound has the unsaved $B^2$
capacity. The exceptional-spectrum large-sieve applications in both
papers have automorphic level $4$ and coefficient magnitude $N=Q^2$ in
the literal Kuznetsov map. Their admissible exceptional amplification
parameter is then $X_{\rm exc}=1+o(1)$, and in any event they do not
replace the regular Maass, holomorphic, or Eisenstein large sieve that
causes (1.2).

There is a source-level normalization warning in packet section 4. The
odd Kuznetsov formula is taken on $\Gamma_0(4)$, but its spectrum contains
newforms and oldforms whose underlying conductor $N_f$ can divide $4$.
Assing--Corbett's Voronoi formula for one underlying newform datum, with
nebentypus conductor $M_f\mid N_f$ and additive denominator $q_0=1$, has
dual Hankel argument

\[
 {m\over[q_0^2,M_fq_0,N_f]}={m\over L_f},
 \qquad L_f=[1,M_f,N_f]=N_f.                       \tag{1.3}
\]

Its positive oscillatory branch is $e(+2\sqrt{mn/L_f})$, and it resonates
with $e(-J\sqrt n)$ at

\[
 m={L_fX\over4}+O(T).                              \tag{1.4}
\]

Thus a level-one component has center $X/4$, a level-two component has
center $X/2$, and a level-four new component has center $X$, before the
finite oldform-dilation bookkeeping. Packet section 4 states only the
first center and does not prove that the other spectral data vanish. The
source-correct statement is a finite family of conductor- and
dilation-dependent centers, not one universal $X/4$. This correction
does not improve the estimate: exact Voronoi returns at every center to a
$T$-term short Hecke sum and retains the known factor
$J^{1/10}=X^{1/20}$ deficit.

This is a non-applicability theorem for the audited imports, not a
counterexample to the actual chirped energy. The smallest surviving
analytic input is still a phase-sensitive **product-Kloosterman** large
sieve for (82.13), with the actual local unit and a full factor-$B$
energy gain. No audited source supplies it.

## Exact statement and hypotheses

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},
 \qquad B={C\over T}.
\]

Writing $C=J^\gamma$, the frozen band gives

\[
 {13\over18}<\gamma\leq {3\over4},\qquad
 B=J^\delta,\quad {11\over90}<\delta\leq {3\over20}. \tag{2.1}
\]

For the odd class, fix a nonzero compatible $k=O(1)$, one orientation,
and the retained stationary sign. The exact leading transform in the
packet is

\[
 S_b^{\rm lead}
 =\sum_{n\asymp Q^2}a_{b,n}S(n,k;4b),              \tag{2.2}
\]

\[
 a_{b,n}=J^{1/2}n^{-3/4}
 e\!\left(-J\sqrt n-\frac{\sqrt{kn}}{2b}\right)V_{b,n},
 \qquad
 \sum_{n\asymp Q^2}|a_{b,n}|^2
 \ll_\varepsilon X^\varepsilon T.                 \tag{2.3}
\]

The sign-reflected alias has the reflected stationary $n$-range. Under
the packet's hypotheses, the following precise claims hold.

1. With geometric moduli $c_{\rm geom}=4b\asymp B$, fixed automorphic
   level $q_{\rm lev}=4$, coefficient magnitude and length
   $N_{\rm DI}=Q^2$, fixed second argument $k$, and spectral width
   $K^2\ll Q/B$, the ordinary Kuznetsov large sieve is dominated by its
   $N_{\rm DI}$ term. It yields (1.2), not (1.1).

2. Pascadi, arXiv:2511.08445v2, Theorem 1.1 applies to a single modulus
   $c_{\rm src}$, a unit $a\bmod c_{\rm src}$, and two separated
   coefficient sequences on intervals of lengths
   $M,N\ll c_{\rm src}^{1/2+o(1)}$, subject to
   $(m,n,c_{\rm src})=1$. Its general Theorem 7.1 permits
   $1\leq N\leq M\leq c_{\rm src}$ but, for
   $c_{\rm src}=dd'e$, has factor

   \[
   c_{\rm src}^{1+o(1)}
   \left(
     {dM^3N\over c_{\rm src}^3}
     +{fM^2\over c_{\rm src}^2}
     +{f\over d^2}
   \right)^{1/6},                                  \tag{2.4}
   \]

   where $d'\mid d$, $(d,e)=1$, and $f^2\mid c_{\rm src}d$ is maximal.
   The literal fixed-column map is $c_{\rm src}=4b\asymp B$,
   $M\asymp B$, $N=1$, after periodic compression of the $Q^2$-long
   $n$-sum. Formula (2.4) has no negative power of $B$ in this map.

3. Pascadi's Corollary 7.9 permits a modulus average
   $c_{\rm src}\asymp C_{\rm src}$, $q_{\rm com}\mid c_{\rm src}$, and
   separated coefficients
   $\alpha_m(c_{\rm src})\beta_n(c_{\rm src})$ dominated by fixed
   envelopes, with $(m,n,q_{\rm com})=1$. Here

   \[
      C_{\rm src}=B,\qquad q_{\rm com}=4,\qquad
      M\asymp B,\quad N=1.                         \tag{2.5}
   \]

   All factorization parameters of $q_{\rm com}$ are $O(1)$, so the
   corollary's leading $C_{\rm src}^{2+o(1)}/q_{\rm com}$ is
   $B^{2+o(1)}$. It neither saves $B$ nor accepts the product kernel in
   (82.13).

4. Blomer--Pascadi, arXiv:2607.24311v1, Theorem 1.1 states, for one
   modulus $c_{\rm src}$, intervals of lengths at most
   $L\leq c_{\rm src}$, a unit $a\bmod c_{\rm src}$, and
   $(m,n,c_{\rm src})=1$,

   \[
   \sum_{m,n}\alpha_m\beta_nS(am,n;c_{\rm src})
   \ll \|\alpha\|\|\beta\|c_{\rm src}^{1+o(1)}
   \left(
     {L^{1/8}\over c_{\rm src}^{3/32}}
     +{L^{5/16}\over c_{\rm src}^{3/16}}
     +{L^{2/3}\over c_{\rm src}^{7/18}}
   \right).                                        \tag{2.6}
   \]

   The $c_{\rm src}^{-1/32}$ saving occurs at
   $L=\sqrt{c_{\rm src}}$ with both variables genuinely available. In
   the literal Round-82 fixed-column map
   $c_{\rm src}\asymp B$, $M\asymp B$, $N=1$. The unbalanced Theorem 5.5
   has no saving there; padding both intervals to length $B$ also puts
   (2.6) outside its useful range.

5. The exceptional large-sieve theorems in both papers are not an energy
   estimate for (2.2). In the actual Kuznetsov map their source level is
   $q_{\rm src}=4$, their Fourier-index magnitude is
   $N_{\rm src}=Q^2$, and the geometric moduli $4b\asymp B$ occur in the
   trace-formula kernel rather than as varying automorphic levels.
   Pascadi's Theorem 9.4 and Blomer--Pascadi's Theorem 1.6 consequently
   allow only $X_{\rm exc}=O(1)$ here.

6. Assertions 1--5 concern only the odd standard Kloosterman family. The
   packet gives no explicit generalized Kloosterman formula, cusp pair,
   scaling matrix, character, or modulus set for $\kappa=1/2$ or $1$.
   Hence none of the sources has a literal all-class map. No parity or
   sign inference repairs this omission.

## Proof or derivation

**Odd Poisson normalization.** For $q=4b$, the stationary equation in

\[
 I_{b,n}=\int W_b(x)
 e\!\left(-{A_{1/4,b}\over x}-{nx\over q}\right)dx
\]

is $n=qA_{1/4,b}/x^2$. Since $x\asymp C$, $b\asymp B=C/T$, and
$A_{1/4,b}\asymp bX$,

\[
 n\asymp {B^2X\over C^2}={X\over T^2}=Q^2.         \tag{3.1}
\]

At the critical point,

\[
 -2\sqrt{A_{1/4,b}n/q}
 =-J\sqrt n-\frac{\sqrt{kn}}{2b},                  \tag{3.2}
\]

because $A_{1/4,b}/(4b)=(J/2+\sqrt{k}/(4b))^2$. The stationary amplitude
is

\[
 q^{-1/4}A_{1/4,b}^{1/4}n^{-3/4}
 \asymp J^{1/2}n^{-3/4},                           \tag{3.3}
\]

which verifies (2.2)--(2.3). Thus the modulus, $n$-length, and secondary
chirp used here are literal.

**Ordinary Deshouillers--Iwaniec capacity.** Pascadi's current
restatement of the regular spectral large sieve gives, for coefficients
at magnitude $N$ and spectral range $|t|\leq K$, the cost

\[
 (K^2+\mu(\mathfrak a)N^{1+\varepsilon})\|a\|_2^2. \tag{3.4}
\]

For the fixed level-four cusp in the odd transform,
$\mu(\mathfrak a)\asymp1$. The Bessel argument is

\[
 {4\pi\sqrt{nk}\over4b}\asymp {Q\over B}=:R.       \tag{3.5}
\]

The phase-matched calculation in the permitted Round-73 audit gives
$K^2\ll R$. Even the weaker generic allowance $K\ll R$ would give
$K^2\ll R^2\ll Q^2$ throughout (2.1). Thus the $N=Q^2$ term dominates
in either case, so (3.4) costs $Q^2T$. Restoring
the unnormalized geometric Kloosterman row, whose Kuznetsov normalization
is $S(n,k;4b)/(4b)$, gives the accepted ledger $BQ^2T$. Since $QT=J$,

\[
 {BQ^2T\over J^2/T}=B.                             \tag{3.6}
\]

The theorem is coefficient-blind: inserting the phase in (2.3) does not
alter $\|a\|_2$. It cannot supply the missing gain.

**Pascadi 2511.08445.** Before periodic compression, the variable length
$Q^2$ violates $M,N\leq c_{\rm src}$ for
$c_{\rm src}=4b\asymp B$. After compression, define

\[
 \alpha_{b,r}:=
 \sum_{\substack{n\asymp Q^2\\n\equiv r\ ({\rm mod}\ 4b)}}a_{b,n},
 \qquad
 S_b^{\rm lead}=\sum_{r\ ({\rm mod}\ 4b)}
 \alpha_{b,r}S(r,k;4b).                            \tag{3.7}
\]

This is a full residue interval against a singleton column. In Theorem
7.1, $M=c_{\rm src}$, $N=1$ makes the first two terms inside (2.4)
$d$ and $f$. Since $d,f\geq1$, the theorem gives at best

\[
 |S_b^{\rm lead}|\ll c_{\rm src}^{1+o(1)}
 \|\alpha_b\|_2,                                   \tag{3.8}
\]

the Fourier-theoretic fixed-column bound. The square-root-length
Theorem 1.1 does not apply to the full residue interval. Splitting it
into $B^{1/2}$ intervals of length $B^{1/2}$ and using Cauchy to glue the
results costs $B^{1/4}$, more than its general $B^{-1/700}$ saving or the
special-factorization $B^{-1/12}$ saving.

Corollary 7.9 cannot be given a large common divisor: the moduli are all
$4b$, so only $q_{\rm com}=4$ is uniform. Substituting (2.5) in its
displayed formula leaves $B^{2+o(1)}$. Moreover, it bounds a linear
modulus average of one Kloosterman sum with a separated coefficient
product. The expanded energy (82.13) is a product of two Kloosterman sums
and contains the joint symbol $\mathcal W_b(n_1,n_2)$. No identity in the
source changes one object into the other.

Pascadi's composite-level exceptional theorem has a second parameter
failure. Its automorphic level is $q_{\rm src}$, coefficient magnitude is
$N_{\rm src}$, and its extra factor $X_{\rm exc}^{2\theta}$ is harmless
only in the explicit range

\[
\begin{split}
 X_{\rm exc}\ll{}&1+{q_{\rm src}\over N_{\rm src}}
 +\min\left\{
 {q_{\rm src}^2\over d^{1/3}N_{\rm src}^{7/3}},
 {q_{\rm src}^{3/2}\over f^{1/4}N_{\rm src}^{3/2}},
 {q_{\rm src}d^{1/3}\over f^{1/6}N_{\rm src}}
 \right\}\\
 &+\min\left\{
 {q_{\rm src}^{7/4}\over d^{1/4}N_{\rm src}^{2}},
 {q_{\rm src}^{7/5}\over f^{1/5}N_{\rm src}^{7/5}},
 {q_{\rm src}d^{2/5}\over f^{1/5}N_{\rm src}}
 \right\}.                                         \tag{3.9}
\end{split}
\]

With $q_{\rm src}=4$ and $N_{\rm src}=Q^2$, this is $O(1)$. Mapping
$q_{\rm src}$ to $B$ instead is not a Kuznetsov identity--the level
remains four--and would still give $O(1)$ because $Q^2\gg B$. Finally,
(3.9) treats only the exceptional Maass spectrum, not the regular
capacity in (3.4).

**Blomer--Pascadi 2607.24311.** The literal fixed-column map is again
$c_{\rm src}=4b\asymp B$, $M\asymp B$, $N=1$. Their general Theorem 5.5
specializes to no improvement over (3.8). For example, its factor
contains

\[
 {M^{1/3}+N^{1/3}\over c_{\rm src}^{1/5}},
\]

which is $B^{2/15}+o(1)$ at $M=B,N=1$; one must fall back to the trivial
fixed-column bound. Padding the singleton to a full interval does not
change its $\ell^2$-norm but changes the theorem's interval parameter to
$L=B$, where every term in (2.6) is non-saving. At the advertised
$L=\sqrt B$, a single application saves only $B^{-1/32}$ in norm, versus
the required $B^{-1/2}$, and gluing the $B^{1/2}$ blocks loses $B^{1/4}$.

Their Theorem 1.6 gives the exceptional parameter

\[
 X_{\rm exc}=1+{q\over N}
 +\min\left\{
 {q^{18/11}\over N^{23/11}},
 {q^{16/13}\over N^{18/13}},
 {q^{32/29}\over N^{33/29}}
 \right\}
 +{q^2\over N^3}.                                  \tag{3.10}
\]

At $q=4$, $N=Q^2$, equation (3.10) is $1+o(1)$. It is not a
regular-spectrum large sieve and does not estimate (82.13).

**Exact Kuznetsov--Voronoi return.** In the odd model, the positive
large-argument Kuznetsov branch has phase

\[
 e\!\left(+{2\sqrt{kn}\over4b}\right)
 =e\!\left(+{\sqrt{kn}\over2b}\right),             \tag{3.11}
\]

which cancels the secondary term in (3.2). Granting the unproved common
smooth test and cusp bookkeeping, this leaves spectral sums of the form

\[
 V_f=\sum_{n\asymp Q^2}\lambda_{f,\mathfrak a}(n)
 W_f(n/Q^2)e(-J\sqrt n).                           \tag{3.12}
\]

For an underlying newform datum of conductor $N_f$ and character
conductor $M_f\mid N_f$, Assing--Corbett Corollary 6.3 puts the dual
Hankel argument at $m/L_f$, where $L_f=[1,M_f,N_f]=N_f$. The positive
dual phase is

\[
 e\!\left(+2\sqrt{mn/L_f}\right).                  \tag{3.13}
\]

Equations (3.12)--(3.13) localize at

\[
 \left|2\sqrt{m/L_f}-J\right|Q\ll1,\qquad
 \left|m-\frac{L_fX}{4}\right|\ll T,               \tag{3.14}
\]

where the fixed factor $L_f$ is harmless in the width. Oldform dilations
and switched-cusp coefficients add a finite local rescaling which must
be derived separately; they do not create one universal center.

The Hankel amplitude has size $Q^{3/2}J^{-1/2}$ up to fixed local
constants, so each returned newform component has the shape

\[
 V_f={Q^{3/2}\over J^{1/2}}
 \sum_{\left|m-L_fX/4\right|\ll T}
 \lambda_{f,\mathfrak b}(m)
 \Psi_{f,C}\!\left({m-L_fX/4\over T}\right)
 +\text{tails}.                                    \tag{3.15}
\]

The lossless spectral ledger needs the short coefficient sum in (3.15)
to be $O_\varepsilon(J^{1/2+\varepsilon})$. Its length bound $T$ misses
by

\[
 {T\over J^{1/2}}=J^{1/10}=X^{1/20}.               \tag{3.16}
\]

Thus Voronoi is an involutive diagnosis of the remaining resonance, not
a second saving. Packet section 4 records the $L_f=1$ center but not the
$L_f=2,4$ components, oldform dilations, or continuous spectrum.

**All-class and transformed-error seam.** Equation (82.3) gives a
globally BV coefficient in the original $c$-variable. It does not state
the repeated $b$- and $n$-derivative bounds needed for a common
Kuznetsov test, a two-variable Fourier separation of
$\mathcal W_b(n_1,n_2)$, or uniform summation of all stationary lower
terms. Nor does it identify the two even local units with exact cusp
Kloosterman sums. The odd calculation therefore cannot be promoted to
$\kappa=1/2,1$, the reflected alias, zero frequency, or all lower terms.

For fixed nonzero $k$, gcds can only involve divisors of $k$, but the
required divisor reduction changes the modulus and coefficient sequences
and must be written. At zero index the standard positive-index
Kuznetsov and bilinear hypotheses fail and Ramanujan or twisted Gauss
sums can carry large gcds. These terms are not disposed of by any source
above.

## First doubtful or unproved step

For the ordinary large sieve there is no doubtful normalization: its
literal result is (1.2), which is insufficient. The first false upgrade
would be to assert that the chirp in (2.3) reduces the right-hand side of
the coefficient-blind inequality (3.4). The theorem depends on the
coefficients only through their $\ell^2$-mass and supplies no such gain.

For Pascadi or Blomer--Pascadi, the first false step is replacing the
varying-modulus product kernel

\[
 S(n_1,k;4b)\overline{S(n_2,k;4b)}
\]

by the single fixed-modulus kernel $S(am,n;c)$. There is no identity in
either source that does this. The legal fixed-column specialization
exists only after periodic compression (3.7), and it gives no power
saving. The legal modulus-average theorem has common divisor $4$ and
therefore no $B$-aspect saving.

For the Kuznetsov route, the first packet-level seam is earlier than
Voronoi: one needs an exact common smooth $b$-test and the level-four
cusp/character realization of the actual local unit. Even granting that
ideal odd reduction, the first missing analytic theorem is the uniform
short-coefficient estimate

\[
 \sum_{|m-m_f|\ll T}\lambda_{f,\mathfrak b}(m)
 \Psi_{f,C}\!\left({m-m_f\over T}\right)
 \ll_\varepsilon J^{1/2+\varepsilon},              \tag{4.1}
\]

at every conductor- and dilation-dependent center $m_f\asymp X$, for
every Maass, holomorphic, oldform, and Eisenstein datum produced by the
level-four trace formula. No audited source proves (4.1). Before using
any such claim, the spectral decomposition underlying the packet's
single $X/4$ center must also be supplied.

For the full Round-82 target, the first all-class gap is the absence of
the two even generalized Kloosterman transforms and of transform-norm
bounds for all lower stationary terms and tails. An odd leading-term
estimate alone would not satisfy the completion rule.

## Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | **Pass.** $B=C/T$, $n\asymp Q^2$, $\sum_n|a_{b,n}|^2\ll T$, and target $J^2/T$ give the exact ratio $B$ in (3.6). |
| Odd inverse local unit | **Pass for the packet's leading model.** The standard family is $S(n,k;4b)$, the stationary phase is (3.2), and the positive Kuznetsov branch cancels exactly as in (3.11). |
| Even cusp classes | **Fail.** No cusp pair, scaling matrix, character, modulus set, or generalized Kloosterman formula is supplied for $\kappa=1/2,1$. Neither recent fixed-modulus theorem licenses inference by parity or sign. |
| Transition flattening scope | **Pass with restriction.** Round 81 gives original-$c$ BV for the main coefficient and a separately safe pointwise transition error in this band. It does not give the joint $b,n$ transform seminorms needed here. |
| Stationary $n$-range | **Pass.** The exact equation gives $n\asymp Q^2$, independently of $C$, and the reflected alias reverses the sign. |
| Complete stationary errors | **Open.** The sources do not sum the lower stationary terms, moving $n$-support, nonstationary tails, opposite-sign Bessel transform, or endpoint pieces at energy level. |
| Energy diagonal | **Pass as inherited.** The original diagonal is $BC=C^2/T\leq J^2/T$. None of the source failures changes this. |
| Ordinary large-sieve capacity | **Fail to close, exactly.** It is $BQ^2T=CQ^2=BJ^2/T$, with no hidden normalization gain. |
| Phase-sensitive off-diagonal | **Open.** The needed factor-$B$ estimate is for a product-Kloosterman kernel with joint actual symbol; all audited bilinear theorems concern one Kloosterman kernel. |
| Pascadi 2511.08445 current version | **Fail to apply for closure.** v2 is current as of 2026-08-16. The fixed-modulus map is $M=B,N=1$ after compression and has no saving; the modulus-average map has common divisor $4$; the exceptional theorem has $q=4,N=Q^2,X_{\rm exc}=O(1)$. |
| Blomer--Pascadi 2607.24311 current version | **Fail to apply for closure.** v1 is current as of 2026-08-16. The $B^{-1/32}$ saving requires two square-root-length variables at one fixed modulus; the actual map is a full residue interval and a singleton, and Theorem 1.6 is exceptional-spectrum only with $X_{\rm exc}=1+o(1)$. |
| Short-Hecke self-return | **Fail to close.** Exact Voronoi produces a finite family of centers $m_f\asymp X$, including $X/4$, $X/2$, and $X$ before oldform rescaling, and reproduces the $J^{1/10}$ deficit at each. The packet does not justify one universal center. |
| Gcd and zero modes | **Open.** Positive fixed $k$ permits only a finite divisor decomposition, but it is not executed. Zero indices are outside the positive-index source hypotheses and can have large gcd factors. |
| Smooth weights | **Fail for transformed closure.** Fixed-modulus bilinear bounds accept arbitrary separated sequences, but the actual energy weight is joint. Kuznetsov/Voronoi needs common smooth tests and repeated derivatives not contained in (82.3). |
| Perfect squares and fourth powers | **Pass as a hostile control.** Since $T<J$, each window $m=m_f+O(T)$ contains at most $O(1)$ squares at scale $m_f\asymp X$, and still fewer fourth powers. One exact center is not the source of the $T$-term deficit. |
| Phase-conjugating coefficients | **Pass as a no-go control.** A coefficient-blind source permits phases that conjugate the chirp, so its stated $\ell^2$ bound cannot by itself certify chirp cancellation. Any gain must use additional actual-symbol structure absent from the theorem statement. |
| Downstream scope | **Pass.** No conclusion is drawn for $C>J^{3/4}$, axes outside their accepted band, cone edges, other radial sectors, full $M9\!-\!M1$, $M9\!-\!M2$, $M9$, or the Gauss-circle exponent. |

## Dependencies and exact artifacts used

The repository artifacts used were exactly:

* protocol.md;
* state/proof_obligations.yml;
* state/active_campaign.yml;
* rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/derivation_packet.md;
* rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reviews/conductor_round81_transition_normalization.md;
* rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md;
* rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/briefs/kloosterman_energy_source_hostile_audit.md.

No sibling Round-82 report was read.

The primary sources checked were:

* Alexandru Pascadi, [*Non-abelian amplification and bilinear forms with
  Kloosterman sums*, arXiv:2511.08445v2](https://arxiv.org/pdf/2511.08445v2),
  Theorems 1.1, 1.2, 7.1, 9.3, and 9.4, Corollaries 1.4 and 7.9, and
  Proposition 9.2. Version 2, revised 21 June 2026, is current. The audit
  checked the fixed modulus, interval lengths, factorization parameters,
  common-divisor modulus average, coefficient dependence, coprimality,
  cusp, and exceptional-only scope.

* Valentin Blomer and Alexandru Pascadi, [*Bilinear forms with
  Kloosterman sums via quadratic characters*,
  arXiv:2607.24311v1](https://arxiv.org/pdf/2607.24311v1), Theorems 1.1,
  1.6, 5.2, 5.5, and 5.7 and Remark 5.8. Version 1, submitted 27 July
  2026, is current. The audit checked its single fixed modulus, the two
  interval lengths, fixed unit multiplier, triple-gcd condition,
  initial-interval exception, unbalanced formula, and exceptional-spectrum
  application.

* Jean-Marc Deshouillers and Henryk Iwaniec, [*Kloosterman sums and
  Fourier coefficients of cusp forms*, Invent. Math. 70 (1982),
  219--288](https://doi.org/10.1007/BF01390728), Theorem 2, using the
  exact modern restatement as Lemma H in Alexandru Pascadi,
  [*Large sieve inequalities for exceptional Maass forms and the greatest
  prime factor of $n^2+1$*,
  arXiv:2404.04239v3](https://arxiv.org/pdf/2404.04239v3), Forum Math. Pi
  14 (2026), e8. The regular-spectrum cost is
  $K^2+\mu(\mathfrak a)N^{1+\varepsilon}$, and its Kuznetsov formula
  retains the exact cusp and $S/c$ normalization.

* Edgar Assing and Andrew Corbett, [*Voronoï summation via switching
  cusps*, arXiv:1904.02025](https://arxiv.org/pdf/1904.02025), Monatsh.
  Math. 194 (2021), 657--685,
  [DOI 10.1007/s00605-021-01537-5](https://doi.org/10.1007/s00605-021-01537-5),
  Theorem 6.2, Corollary 6.3, and Hankel formulae (38)--(39). The literal
  dual argument $m/[q_0^2,M_fq_0,N_f]$ forces the conductor-dependent
  centers in (1.4), and the coefficients occur at the switched cusp.

Every source was checked at the actual modulus or automorphic level,
variable magnitude and length, fixed versus varying Kloosterman argument,
coprimality, coefficient separation, smooth-test requirement, spectral
components, local cusp data, and claimed factor-$B$ gain.

## Recommended state effect

**Retain (82.4) and the first residual band open.** Promote no new
conductor range from any audited source. Record as negative/source-audited
evidence that:

1. the ordinary Deshouillers--Iwaniec/Kuznetsov large sieve has exact
   capacity $BQ^2T$ and loses $B$;
2. Pascadi 2511.08445v2 gives no saving in the literal fixed-column map,
   no $B$-aspect saving when its common modulus divisor is $4$, and no
   regular-spectrum improvement;
3. Blomer--Pascadi 2607.24311v1 requires two square-root-length variables
   for its $c^{-1/32}$ saving and does not estimate the varying-modulus
   product energy;
4. exact Voronoi returns to a finite family of centers $m_f\asymp X$ and
   the same $X^{1/20}$ short-Hecke deficit.

Revise packet section 4 so that $m=X/4+O(T)$ is not presented as a
universal center. An exact newform/oldform, dilation, cusp, and continuous
spectrum decomposition is required; for an underlying newform conductor
$N_f$ its raw Assing--Corbett center is $N_fX/4+O(T)$. Retain the desired
new input as a named phase-sensitive product-Kloosterman large sieve for
(82.13), requiring a full factor-$B$ energy gain with the actual joint
symbol.

Keep the two even cusp transforms, reflected alias, gcd decompositions,
zero modes, complete stationary lower terms, and transform tails open.
Make no change to the accepted transition and axis ownership in
$J^{13/18}<C\leq J^{3/4}$, and no downstream change to full
$M9\!-\!M1$, $M9\!-\!M2$, $M9$, or the global exponent.

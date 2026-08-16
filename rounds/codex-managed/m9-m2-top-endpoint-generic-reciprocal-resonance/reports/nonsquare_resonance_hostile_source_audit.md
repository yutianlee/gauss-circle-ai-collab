# 1. Result: lemma or no-go result.

There are two rigorous conclusions.

First, exact nonsquare resonances are rigid but are not confined to the
removed square family. If

\[
 \omega(a,b,k):={(\sqrt b-\sqrt a)^2\over 2k},
\]

then a rational ratio between two primitive nonsquare frequencies forces
the same primitive ray; equality also forces the same \(k\). Consequently,
for a fixed \(X\), exact resonances on distinct primitive nonsquare rays
cannot coexist. Nevertheless every individual primitive nonsquare ray has
strict-interior exact resonances for suitable real \(X\). Thus the lawful
exact structured branch is “one primitive ray, possibly several divisor
modes”, not “\(ab\) is a square”.

Second, the analogous classification is false for metric resonances.
On every uniformly populated geometric block there is an unavoidable
random-density term \(\#\mathcal T/R\), obtained simply by averaging the
real parameter \(X\). On a fixed-ratio block with \(P\) primitive
nonsquare rays and
\(\asymp J\) admissible \(k\)'s per ray, some \(X\) has

\[
 \mathcal I_{\mathcal T}(X;R)\gg {PJ\over R}.
\]

At the accepted coefficient scale this has positive capacity

\[
 {PJ\over R}\cdot R\sqrt{L/J}=P\sqrt{JL}.
\]

If the actual lift support supplies the expected \(P\asymp B^2\) rays,
this is \(B^2\sqrt{JL}\). The near-square block
\((a,b)=(a,a+2)\), \(a\asymp A\), similarly has incidence
\(\gg J/R\) and coefficient capacity \(\asymp\sqrt{JAL}\).
Therefore an inverse theorem can classify only **excess above the metric
baseline**, not every point of (79.7). Even the baseline capacity is far
too large to be the signed-energy estimate.

Perfect powers do not repair this failure. Rational \(X\), hence square or
fourth-power integral \(X\), has no exact nonsquare resonance, but finite
arbitrary collections recur metrically along perfect squares; collections
with independent quadratic kernels recur along fourth powers. An explicit
actual-range fourth-power control is furnished by the Pell family
\(a=s^2,\ b=3t^2=a+2\), \(s^2-3t^2=-2\).

The audited primary radical-spacing, determinant, large-sieve, and
decoupling theorems do not have hypotheses matching the normalized modular
frequency, the moving \(k\)-interval, the real prescribed \(X\), and the
complete Round-77 coefficient. No source import is justified.

# 2. Exact statement and hypotheses.

Retain all hypotheses and notation of the derivation packet. In
particular, \(J=\sqrt X\), \(1\le L\le H\le J^{1/2}\), \(a<b<4a\) are odd
and coprime, \(ab\ne\square\), \(k\) lies in the open interval (79.2), and
\(1\le R\le N_{a,b}\ll G_{a,b}\asymp L/b\). Put

\[
 m={a+b\over2},\qquad q={b-a\over2},\qquad
 v=\sqrt{m^2-q^2}=\sqrt{ab},
\]

and

\[
 u={q\over m+v}
   ={\sqrt b-\sqrt a\over\sqrt b+\sqrt a}.
\]

Then \((m,q)=1\), \(m,q\) have opposite parity, and the exact normalized
geometry is

\[
 \boxed{\Lambda=Xqu},\qquad
 \boxed{{Ju\over1-u}<k<{2Ju\over1+u}}.                 \tag{A}
\]

The factor \(1/2\) is included: \(qu=(\sqrt b-\sqrt a)^2/2\).

Write uniquely

\[
 a=d_1s^2,\qquad b=d_2t^2,\qquad
 D=d_1d_2>1,\qquad r=st,
\]

where \(d_1,d_2\) are squarefree. Coprimality makes \(D\) squarefree, and

\[
 ab=Dr^2,\qquad m^2-Dr^2=q^2,
\qquad \omega(a,b,k)={m-r\sqrt D\over k}={qu\over k}. \tag{B}
\]

The following statements are proved below.

**Exact ray rigidity and spacing.** For two primitive nonsquare triples
\(\tau=(a,b,k)\) and \(\tau'=(a',b',k')\),

\[
 {\omega(\tau)\over\omega(\tau')}\in\mathbb Q
 \quad\Longrightarrow\quad (a,b)=(a',b').             \tag{C}
\]

In that case the rational ratio equals \(k'/k\). Hence
\(\omega(\tau)=\omega(\tau')\) also gives \(k=k'\). If
\(a,b,a',b'\asymp B\), \(k,k'\asymp K\), and the triples are distinct, then

\[
 |\omega(\tau)-\omega(\tau')|
 \gg
 \begin{cases}
   K^{-3}B^{-1},&D=D',\\
   K^{-5}B^{-3},&D\ne D'.
 \end{cases}                                           \tag{D}
\]

The constants are absolute after the fixed dyadic ratios are fixed.

**Exact existence and rational-\(X\) exclusion.** Fix any geometric
primitive nonsquare ray. For every sufficiently large integer \(k\), choose an
integer \(\ell\) with

\[
 {bk\over2}<\ell<2ak
\]

and set

\[
 X={2\ell k\over(\sqrt b-\sqrt a)^2}.                  \tag{E}
\]

Then \(k\) lies strictly in (79.2) and \(\Lambda/k=\ell\). Its accepted
local coefficient scale is

\[
 \widetilde{\mathcal V}_{a,b,k}
 ={J(\sqrt b-\sqrt a)\sqrt G\over k^{3/2}}
 ={\sqrt{2\ell G}\over k}\asymp\sqrt{aG/k}.            \tag{F}
\]

Conversely, if \(X\in\mathbb Q_{>0}\), no primitive nonsquare triple is
exactly resonant. For \(X=2M/(\sqrt b-\sqrt a)^2\), all exact modes on the
fixed ray are precisely the divisors \(k\mid M\) in

\[
 {\sqrt{2M}\over2\sqrt a}<k<{\sqrt{2M}\over\sqrt b};   \tag{G}
\]

there are at most \(\tau(M)\ll_\varepsilon M^\varepsilon\).
On a \(k\asymp K\) divisor block their total dyadic coefficient capacity is

\[
 \ll_\varepsilon
 M^\varepsilon R\,{\sqrt{MG}\over K^{3/2}}
 \asymp
 M^\varepsilon R\,a^{3/4}\sqrt G\,M^{-1/4}
 \quad\left(K\asymp\sqrt{M/a}\right).                  \tag{G1}
\]

Thus the exact branch is structurally sharp but is not, by itself, a
target-scale obstruction.

**Geometric metric-baseline theorem.** Let \(Y\) be large,
\(J_0=\sqrt Y\), and \(L\le Y^{1/4}\). Fix \(\eta>0\), and let
\(\mathcal P\) be any collection of primitive nonsquare rays satisfying

\[
 a\asymp B,\qquad 1+\eta\le {b\over a}\le2-\eta.
\]

For every ray take all integer \(k\) in the common strict interval

\[
 {\sqrt{2Y}(\sqrt b-\sqrt a)\over2\sqrt a}
 <k<
 {\sqrt Y(\sqrt b-\sqrt a)\over\sqrt b},               \tag{H}
\]

shrunk by one integer at each end, and call the resulting triple set
\(\mathcal T\). These \(k\)'s belong to (79.2) for every \(X\in[Y,2Y]\),
and

\[
 \#\mathcal T\asymp (\#\mathcal P)J_0.                 \tag{I}
\]

Let \(0<c/R\le1/2\), where \(c\) is the constant in (79.7). Then

\[
 {1\over Y}\int_Y^{2Y}
 \#\left\{(a,b,k)\in\mathcal T:
 \left\|{X(\sqrt b-\sqrt a)^2\over2k}\right\|
 \le {c\over R}\right\}\,dX
 = {2c\over R}\#\mathcal T
   +O_\eta\!\left({\#\mathcal T\over BJ_0}\right).     \tag{J}
\]

If \(R\ll L/B\le Y^{1/4}/B\), the error is smaller than the main term.
Thus some \(X\in[Y,2Y]\) has \(\gg\#\mathcal T/R\) geometric metric
resonances. For \(c/R<1/2\) each has a unique nearest integer \(\ell\)
(and it is positive in this block), so this is also a quadruple incidence
count. If the literal complete lift support is uniform on the averaging
interval, has \(R\le N_{a,b}\), and contains \(\asymp B^2\) such rays,
square excision removes only \(O(B)\) of them and

\[
 \mathcal I_{\rm ns}\gg {B^2J_0\over R}.               \tag{K}
\]

On this block \(K\asymp J_0\), \(G\asymp L/B\), and

\[
 \widetilde{\mathcal V}\asymp\sqrt{L/J_0}.             \tag{L}
\]

The trivial incidence is \(O(B^2J_0)\), its trivial coefficient capacity is
\(O(B^2R\sqrt{J_0L})\), and (K) saves exactly \(R\), leaving

\[
 \boxed{B^2\sqrt{J_0L}}.                               \tag{M}
\]

For the terminal choice \(B\asymp L\), this is
\(L^2\sqrt{J_0L}\), larger than the desired \(L^2\) energy scale by
\(\sqrt{J_0L}\). It remains only a positive proxy capacity, not an actual
coefficient lower bound.

The statement with \(\#\mathcal P\) is an unconditional geometric
statement. Its interpretation inside (79.10) requires the stated literal
support hypotheses.

**Near-square baseline.** For \(a\asymp A\) odd and \(b=a+2\), the rays
are primitive and nonsquare, the common \(k\)-interval has
\(\asymp J_0/A\) integers, and the same averaging gives on the geometric
block

\[
 \mathcal I_{\rm near}\gg {J_0\over R},\qquad
 \widetilde{\mathcal V}\asymp\sqrt{AL/J_0},\qquad
 \mathcal A_{\rm near}(R)\asymp_{\rm capacity}\sqrt{J_0AL}. \tag{N}
\]

At \(A\asymp L\), the last quantity is \(L\sqrt{J_0}\), whose ratio to
\(L^2\) is \(\sqrt{J_0}/L\ge1\).

This applies uniformly at \(R=1\), intermediate \(R\), and \(R\asymp G\)
when the literal support supplies \(R\le N_{a,a+2}\); without that support
statement it remains geometric.

**Perfect-power metric recurrence.** Fix any finite set of geometric
nonsquare triples at a base integral \(J_1\), with integers
\(\kappa_i\in\mathcal K_{a_i,b_i}(J_1^2)\). There are arbitrarily large
integers \(t\) for which

\[
 X=(tJ_1)^2,\qquad k_i=t\kappa_i,\qquad
 \left\|{X(\sqrt{b_i}-\sqrt{a_i})^2\over2k_i}\right\|
 \le {c\over R}\quad(1\le i\le M).                    \tag{O}
\]

Thus arbitrary finite ray collections recur at square \(X\). If
\(J_1=w^2\) and the chosen squarefree kernels \(D_i\) are distinct, then
there are infinitely many \(n\) giving the same conclusion with

\[
 X=(nw)^4,\qquad k_i=n^2\kappa_i.                      \tag{P}
\]

At the accepted scale the \(i\)-th square recurrence contributes
\(R\,t^{-1/2}\widetilde{\mathcal V}_{i,0}\), and the fourth-power
recurrence contributes \(R\,n^{-1}\widetilde{\mathcal V}_{i,0}\). These
are logical counterexamples to a metric algebraic classification, not an
energy lower bound.

**Explicit Pell/fourth-power control.** The equation

\[
 s^2-3t^2=-2
\]

has infinitely many odd solutions. For every solution after \((1,1)\), set
\(a=s^2,\ b=3t^2=a+2\). Then the ray is primitive, odd, nonsquare, and has
constant squarefree kernel \(D=3\). For an integer \(h\ge1\), put

\[
 X=(6ah)^4,\qquad J=36a^2h^2,\qquad k=27ah^2.           \tag{Q}
\]

This \(k\) is strictly inside (79.2), and

\[
 \left\|{X(\sqrt b-\sqrt a)^2\over2k}\right\|
 \ll {h^2\over a}.                                    \tag{R}
\]

Taking \(L\asymp ah\le X^{1/4}\) gives \(G\asymp h\). Hence, whenever
the actual lift support has \(N\asymp G\), the full metric range
\(R\asymp h\) survives for \(h^3\ll a\). Its one-mode coefficient scale is

\[
 \widetilde{\mathcal V}\asymp h^{-1/2},
 \qquad R\widetilde{\mathcal V}\asymp h^{1/2}.         \tag{S}
\]

This is a genuine nonsquare, near-square, perfect-fourth-power,
strict-interior control, but the fixed-\(D\) Pell sequence is only
logarithmically numerous up to a given height.

# 3. Proof or derivation.

From \(a=m-q,\ b=m+q\), odd coprimality gives \((m,q)=1\) and opposite
parity. Rationalization gives

\[
 u={q\over m+\sqrt{m^2-q^2}}
   ={\sqrt b-\sqrt a\over\sqrt b+\sqrt a},
\quad
 qu=m-\sqrt{m^2-q^2}={\delta^2\over2}.
\]

Also

\[
 {\delta\over\sqrt a}={2u\over1-u},\qquad
 {\delta\over\sqrt b}={2u\over1+u},
\]

which proves (A), including the orientation, the factor \(1/2\), and the
open endpoints. Formula (B) follows from the squarefree decompositions and
\(m^2-ab=q^2\).

For (C), suppose \(\omega/\omega'=c\in\mathbb Q_{>0}\). If \(D\ne D'\),
linear independence of \(1,\sqrt D,\sqrt{D'}\) over \(\mathbb Q\) makes the
identity impossible. If \(D=D'\), comparison of rational and irrational
parts yields

\[
 m=\lambda m',\qquad r=\lambda r',\qquad q=\lambda q'
\]

for one positive rational \(\lambda\). Therefore
\(a=\lambda a'\) and \(b=\lambda b'\). Writing \(\lambda\) in lowest terms
and using \((a,b)=(a',b')=1\) forces \(\lambda=1\). The remaining ratio is
\(c=k'/k\). This also proves exact-ray ownership at a fixed \(X\), since
two exact resonances would have \(\omega/\omega'=\ell/\ell'\in\mathbb Q\).

For (D), clear the denominator \(kk'\). If \(D\ne D'\),

\[
 z=k'(m-r\sqrt D)-k(m'-r'\sqrt{D'})
\]

is a nonzero algebraic integer in a biquadratic field. Its three other
conjugates are \(O(KB)\), while its norm is a nonzero integer. Thus
\(|z|\gg(KB)^{-3}\), and division by \(kk'\asymp K^2\) gives
\(K^{-5}B^{-3}\). In one quadratic field there is one other conjugate,
giving \(K^{-3}B^{-1}\). This separation is much too weak in the actual
range \(K\asymp J\), and, more importantly, it is separation in
\(\mathbb R\), not separation of \(X\omega\pmod1\). For arbitrary real
\(X\), even exact modulo-one collisions can be prescribed. Even if \(X\)
is an integer and \(n\) is the nearest integer to
\(X(\omega-\omega')\), then either an exact modulo-one collision occurs
(which is possible when a same-field difference is rational), or the same
norm argument applied to \(Xz-nkk'\) gives only

\[
 \|X(\omega-\omega')\|\gg
 \begin{cases}
 X^{-1}K^{-3}B^{-1},&D=D',\\
 X^{-3}K^{-5}B^{-3},&D\ne D'.
 \end{cases}
\]

At \(X=J^2,\ K\asymp J\), the second bound is
\(J^{-11}B^{-3}\), vastly below the allowed window
\(1/R\ge B/L\ge B/J^{1/2}\). Thus algebraic injectivity supplies no useful
large-sieve spacing at the accepted scale.

For (E), note that \(J\delta=\sqrt{2\ell k}\). The two strict inequalities
in (79.2) become respectively \(\ell<2ak\) and \(\ell>bk/2\). Such an
\(\ell\) exists for all large \(k\) because \(b<4a\). Formula (F) is direct.
The irrationality of \(m-r\sqrt D\) proves the rational-\(X\) exclusion.
For fixed \(\Lambda=M\in\mathbb Z\), exactness is \(k\mid M\), and (G)
is again (79.2).

For the metric average, write

\[
 \gamma_{a,b,k}={(\sqrt b-\sqrt a)^2\over2k}.
\]

If \(\rho=b/a\in[1+\eta,2-\eta]\), the length of (H) is

\[
 J_0(\sqrt\rho-1)
 \left({1\over\sqrt\rho}-{1\over\sqrt2}\right)
 \asymp_\eta J_0,
\]

which proves (I) and checks the open interval uniformly in \(X\). Moreover
\(\gamma\asymp_\eta B/J_0\). Over any interval of length \(Y\), the periodic
set \(\{x:\|\gamma x\|\le c/R\}\) has measure

\[
 {2cY\over R}+O(\gamma^{-1}).
\]

Summing and dividing by \(Y=J_0^2\) proves (J). The coefficient computation
is

\[
 {J_0\sqrt B\sqrt{L/B}\over J_0^{3/2}}
 =\sqrt{L/J_0},
\]

which gives (M). Primitive odd pairs have positive density in a fixed
two-dimensional inner cone, while primitive square rays have
\(a=s^2,b=t^2\) and number only \(O(B)\); this proves the raw pair-count
claim. Certification that this whole raw set lies in the literal complete
lift support is separated in Section 4.

For \(b=a+2\), the product is
\((a+1)^2-1\), hence is never a square. The common \(k\)-interval has length
\(\asymp J_0/A\), \(\gamma\asymp J_0^{-1}\), and there are \(\asymp A\)
candidate rays. This gives \(\#\mathcal T\asymp J_0\) and (N). Empty and
singleton intervals occur only when \(Jq/m=O(1)\); they carry no structural
implication and are not used in the lower-capacity block.

For (O), scaling \(J_1\mapsto tJ_1\) and
\(\kappa_i\mapsto t\kappa_i\) preserves the strict \(k\)-interval, while the
phase becomes \(t\beta_i\), with

\[
 \beta_i={J_1^2(\sqrt{b_i}-\sqrt{a_i})^2\over2\kappa_i}.
\]

Simultaneous Dirichlet approximation supplies arbitrarily accurate returns
of the finite vector \(t(\beta_1,\ldots,\beta_M)\) to zero modulo one. For
(P), the phase is \(n^2\beta_i\). With distinct \(D_i\), every nonzero
integer linear combination of the \(\beta_i\) is irrational. Weyl's
criterion and one van der Corput differencing step give equidistribution of
\(n^2(\beta_1,\ldots,\beta_M)\) on the torus. This proof is elementary and
does not import a source theorem.

Finally, multiplying \(s+t\sqrt3\) by \(2+\sqrt3\) produces infinitely many
odd solutions to \(s^2-3t^2=-2\). They give \(b-a=2\), coprimality, and
\(ab=3(st)^2\). With \(\delta=\sqrt{a+2}-\sqrt a\), (Q) gives

\[
 {J\delta/(2\sqrt a)\over k}={2\over3}\sqrt a\,\delta<1,
\qquad
 {J\delta/\sqrt b\over k}={4\over3}{a\delta\over\sqrt b}>1
\]

for \(a\ge25\), so the interval is strict. Put

\[
 E=a^2(a+1-\sqrt{a(a+2)})-{a-1\over2}.
\]

Taylor expansion with an absolute remainder gives

\[
 E={5\over8a}-{7\over8a^2}+O(a^{-3}),
\quad
 48aE=30-{42\over a}+O(a^{-2}).
\]

The phase in (Q) equals

\[
 48ah^2a^2(a+1-\sqrt{a(a+2)})
 =24a(a-1)h^2+30h^2+O(h^2/a),
\]

proving (R). Substitution into (79.13) proves (S).

# 4. First doubtful or unproved step.

The first unproved step in turning the strongest geometric obstruction into a literal
lower bound for \(\mathcal A_{\rm ns}\) is a lower-support statement absent
from the permitted packet: it is not stated there that a positive proportion
of the \(\asymp B^2\) primitive inner-cone pairs has nonempty complete lift
support, nor that \(N_{a,b}\asymp G_{a,b}\). The packet gives
\(N_{a,b}\ll G_{a,b}\) and \(G_{a,b}\asymp L/b\) only after membership in
\(\mathscr P_L\). The packet also does not explicitly state that this
literal support is unchanged while \(X\) runs through \([Y,2Y]\).
Accordingly, (J) is a rigorous geometric incidence theorem, but the
specialization \(P\asymp B^2\) inside (79.10), and the Pell choice
\(R\asymp G\), require an independent uniform literal-support lower bound.

There is a second, deliberate limitation: (79.13) is the accepted local
coefficient scale, not a pointwise lower bound for the complete centred
integral. Floors, stars, collars, and the two moving profiles can make an
individual coefficient small or zero. Thus (M), (N), and (S) are exact
coefficient **capacities**, as requested, but not lower bounds for the actual
signed energy. No conclusion here takes absolute values and then claims a
bound for that energy.

# 5. Control tests and outcomes.

- **Factor \(1/2\) and orientation — pass.** The audit uses
  \(qu=\delta^2/2\), hence \(\Lambda=Xqu\), and obtains
  \(|\Lambda-\ell k|\le ck/R\), never the reversed quotient.

- **Parity and primitivity — pass.** Odd \(a,b\) give integral \(m,q\) of
  opposite parity and \((m,q)=1\). The Pell family has odd \(s,t\), primitive
  \((s^2,3t^2)\), and \(b-a=2\). No parity condition is imposed on \(k\) or
  \(\ell\), where none exists.

- **Open \(k\)-interval — pass.** Formula (A) is exact. The averaged block
  uses the intersection over all \(X\in[Y,2Y]\), possible precisely because
  \(b<2a\), and then removes one integer at each end. The Pell mode is a
  fixed positive proportion away from both endpoints.

- **Lift support — qualified pass.** Every theorem is stated for selected
  actual rays and \(R\le N_{a,b}\). The expected \(B^2\) and \(N\asymp G\)
  lower bounds are explicitly not certified from the permitted context.

- **Square-family excision — pass.** In the primitive setting the removed
  rays are \(a=s^2,b=t^2\), only \(O(B)\) in a \(B\)-block. The families
  \(b=a+2\) and \(ab=3(st)^2\) have nonsquare product.

- **Exact versus metric — pass and decisive.** Exact resonances are owned
  by one primitive ray and exist at real quadratic \(X\); they are absent for
  rational \(X\). Metric resonances have the full density \(1/R\) and recur
  at square and fourth-power \(X\). Counting exact divisors alone misses
  (J), (N), (O), and (P).

- **\(R=1\), \(R\asymp G\), and intermediate windows — pass.** If
  \(c/R\ge1/2\), the window is all of the circle. Otherwise (J) is uniform.
  The error/main ratio is \(O(R/(BJ_0))\) in the fixed-ratio block and
  \(O(R/J_0)\) in the near-square block, both \(o(1)\) throughout the allowed
  range.

- **One-point and empty intervals — pass.** Formula (A) shows their scale
  directly. A singleton can be made exactly resonant using (E), so it cannot
  support a high-multiplicity inverse conclusion. The quantitative baseline
  uses long strict intervals and does not hide a singleton endpoint.

- **Complete actual coefficient — limited, not discarded.** All incidence
  bounds are carried through
  \(J\delta\sqrt G/k^{3/2}\). Nothing replaces the centred integral by its
  first saddle value. The literal profile can only be handled in the later
  signed estimate.

- **Coefficient adversary — fail for every coefficient-blind closure.** A
  phase-conjugated coefficient with the same local magnitudes converts the
  capacities (M) and (N) into positive mass. The accepted actual coefficient
  forbids that replacement, so an incidence theorem alone is not a signed
  theorem.

- **Endpoint stars, collars, and saddle transitions — pass in scope.** The
  geometric modes are strict interior modes. The complete coefficient may
  still cross a physical collar; this is why only its accepted variation
  scale, not a lower value, is asserted. Already-owned endpoint samples and
  fixed collars remain \(O(L^2X^\varepsilon)\).

- **Exact frequency injectivity — pass, quantitative separation too weak.**
  (C) and (D) are rigorous. In the actual \(K\asymp J\) range the global
  spacing \(J^{-5}B^{-3}\) is negligible, and multiplication by arbitrary
  real \(X\) destroys even that as modulo-one spacing.

- **Rank-one self-return — fail as a new saving.** None of the constructions
  changes the accepted homogeneous radial null direction. A reciprocal
  B-process can return the original square-root phase and cannot be counted
  as cancellation beyond the random metric density.

- **Downstream scope — pass.** The report proves an exact rigidity lemma and
  a metric inverse no-go. It proves no complete signed primitive-ray energy,
  no top cone, no \(M9\!-\!M2\), no endpoint uniformity, and no exponent.

# 6. Dependencies and artifacts used.

Only the permitted artifacts were read:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/derivation_packet.md;
- rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/briefs/nonsquare_resonance_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reviews/conductor_round76_adjudication.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_adjudication.md.

No sibling Round-79 report was read. The core proofs above are elementary
and import no external theorem. The following primary sources were audited
only for applicability:

1. O. Robert and P. Sargos, [*Three-dimensional exponential sums with
   monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
   Theorem 2. For fixed real \(\alpha\ne0,1\), \(M\ge2\), and
   \(\Delta>0\), it counts \(m_i\in(M,2M]\) satisfying
   \(|m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|\le
   \Delta M^\alpha\), with bound
   \(\ll_{\alpha,\varepsilon}M^{2+\varepsilon}+
   \Delta M^{4+\varepsilon}\). Even at \(\alpha=1/2\), the actual object
   \((m-r\sqrt D)/k\) has two arithmetic variables, a moving reciprocal
   denominator, an integer translate \(\ell/X\), and many quadratic fields.
   The theorem has no exact variable map. The same paper's double-large-
   sieve lemma reduces a sum to pair-spacing counts but supplies no bound for
   this normalized modular spacing.

2. H. L. Montgomery and R. C. Vaughan, [*The large
   sieve*](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf),
   Theorem 1. It assumes distinct points \(x_r\pmod1\) with
   \(\delta=\min_{r\ne s}\|x_r-x_s\|>0\), and gives
   \(\sum_r|\sum_{M<n\le M+N}a_ne(nx_r)|^2
   \le(N+\delta^{-1})\sum|a_n|^2\). Here
   \(x_r=X\omega(a,b,k)\) can coincide or cluster within \(1/R\) for
   prescribed real \(X\); (J), (O), and (P) explicitly exhibit this failure.
   Moreover the complete lift coefficient is ray- and \(k\)-dependent, not
   one common sequence \(a_n\).

3. E. Bombieri and J. Pila, [*The Number of Integral Points on Arcs and
   Ovals*](https://people.maths.ox.ac.uk/pila/Ovals.pdf), Theorem 5. It
   counts exact integral points on one absolutely irreducible plane algebraic
   curve of fixed degree inside a square. The present relation is a thick
   modular inequality in \((a,b,k,\ell)\), with real \(X\), varying quadratic
   field and varying curve after any squaring. Fixing all but two variables
   and summing the resulting curves loses the desired saving. No determinant
   estimate in this source applies to (79.8) as stated.

4. J. Bourgain and C. Demeter, [*The proof of the \(l^2\) Decoupling
   Conjecture*](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n1-p09-p.pdf),
   Theorem 1.1 (and its discrete Theorem 2.2). The hypotheses are a fixed
   compact \(C^2\) hypersurface with positive definite second fundamental
   form, Fourier support in a \(\delta\)-neighborhood, separated caps or
   points, and an \(L^p\) spatial average. Their Theorem 1.2 also treats a
   fixed truncated cone, with \(1\times\delta\times\delta^{1/2}\)-type
   sectors and again an \(L^p\) average; thus the radial null direction alone
   is not the mismatch. The normalized arithmetic frequencies here are not
   separated, no fixed cone parametrization with uniform caps and the
   complete moving symbol has been supplied, and the goal is pointwise at a
   prescribed \(X\). These theorems are structural analogies and give
   neither (79.10) nor the signed energy.

# 7. Recommended state effect.

**Retain and revise.** Retain (A)--(G) as candidate exact nonsquare
rigidity evidence and promote it only after an independent seam review.
Record (J)--(N) as a route no-go: a future inverse theorem must be formulated
for excess over the unavoidable \(\#\mathcal T/R\) metric baseline (with the
literal actual support), not as a classification of every metric resonance.
Retain the Pell/common-squarefree-kernel branch as a mandatory structured
control, but do not treat its logarithmically sparse fixed-\(D\) family as an
energy obstruction.

Reject direct import of the four audited sources. The smallest remaining
problem is still a coefficient-preserving signed large-sieve/\(TT^*\) or
primitive-ray correlation estimate after subtracting or absorbing the
random metric baseline and separately handling any excess common-field
clusters. Make no status change to the signed cone, transposed energy,
\(M9\!-\!M2\), \(M9\), endpoint uniformity, or the Gauss-circle exponent.

# Round 138 post-unmask seam review: scalar fibres and stationary scope

## 1. Result

The current conductor candidate passes the post-unmask seam audit after
the repairs already incorporated into that candidate.  The rigorously
promotable statement is the strict reduction

\[
 |\mathcal F_N|^2=\mathcal R_{y^{-2}}
 +O_\varepsilon(yX^\varepsilon),
 \tag{1.1}
\]

where \(\mathcal R_{y^{-2}}\) is the conjugation-closed, signed sum over
different denominators for which both the ordinary phase
\(Na/b\) and the character-adjusted physical carrier
\(Na/b+(b-1)/4\) are separated from their partners by more than
\(y^{-2}\).  The deleted owners are the complete same-denominator block
and the union of the two microscopic collision collars.  Their total
absolute cost is \(O_\varepsilon(yX^\varepsilon)\).

No estimate for \(\mathcal R_{y^{-2}}\) is proved.  Its coefficient-blind
capacity remains \(y^{2+o(1)}\), against target \(y^{1+o(1)}\).  The
Poisson square-root expression is only an interior stationary principal
family; the exact hard-endpoint formula has additional owners.  The
unique squarefree-radical phase-one channel is target-safe only inside
that principal family and does not imply the scalar target.

## 2. Exact lift identity, small-arc owner, and complete rows

The exact object corresponding to the Farey scalar is the integerized
Round-121 cone \(\mathcal B_{\rm flat}^{(N)}(X)\), not the cone with
phase \(e(hX/d)\).  Round 121 separately owns

\[
 \mathcal B_{\rm flat}^{+}(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O(R).
 \tag{2.1}
\]

On the certified literal small positive arc one has \(1\le h<d\le y\).
This certification, rather than the asymptotic inequality
\(h/d\ll R^{-1}\) alone, owns the strict inequality \(h<d\) for every
allowed \(X\).  Since \(yh/d\ge y/d\ge1\), \(\eta(yh/d)=1\), and

\[
 \frac1hV_{\rm low}(4R^2h^2/d^2)
 =\frac1dJ_{R,y}(h/d).
 \tag{2.2}
\]

Reduce \(h/d=a/b\) uniquely, with \(h=ag,d=bg,(a,b)=1\).  Then

\[
 \sum_{g\le y/b}\frac{\chi_4(bg)}{bg}
 =\frac{\chi_4(b)}bL_\chi(y/b)=\lambda_b.
 \tag{2.3}
\]

This is the complete lift multiplicity.  Even lifts vanish inside the
character sum, no extra factor of \(a,b,d\), or \(g\) occurs, and all
lifts are aggregated before a norm.  The only \(b=1\) completion class
is the zero residue and is killed exactly by \(J_{R,y}(0)=0\).  Thus
(138.C2)--(138.C3) are termwise exact for
\(\mathcal B_{\rm flat}^{(N)}(X)\); the opposite scalar sign is its
conjugate.

Put

\[
 c_{a,b}=\frac{L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2),\qquad
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}.
 \tag{2.4}
\]

Then \(\mathcal F_N=\sum c_{a,b}e(\phi_{a,b})\),
\(|c_{a,b}|\ll a^{-1}\), and the literal support gives
\(a\ll b/R\).  Consequently

\[
 \sum_{a,b}|c_{a,b}|\ll y\log(2X),
 \qquad
 \sum_{a,b}|c_{a,b}|^2\ll y.
 \tag{2.5}
\]

For \(F_b=\sum_a c_{a,b}e(\phi_{a,b})\), the complete
same-denominator owner is the nonnegative row square

\[
 \sum_b|F_b|^2
 \le \sum_{b\le y}
 \left(\sum_{a\ll b/R}\frac1a\right)^2
 \ll y\log^2(2X).
 \tag{2.6}
\]

This includes the equality diagonal and every unequal-numerator term.
If the unequal-numerator subtotal is displayed separately, it need not
be positive; its absolute value is bounded by (2.6) plus the
\(O(y)\) equality diagonal.  The promoted candidate correctly uses the
whole row square and makes no positivity claim about that subtotal.

## 3. Carrier fibres, microscopic packing, and the exact residual

Let

\[
 \theta_{a,b}=Na/b\pmod1.
\]

If \(g=(N,b)\), \(q=b/g\), and \(N=gn\), then
\((n,q)=1\) and the reduced ordinary phase is \(na/q\).  Conversely a
fixed reduced fibre \(u/q\) consists only of

\[
 b=qg,\qquad g\mid N,\qquad (N/g,q)=1,
 \qquad (N/g)a\equiv u\pmod q,
 \tag{3.1}
\]

with \(q,g\) odd, plus the literal support and primitive-numerator
restrictions.  For a fixed admissible \(g\), the numerator is in one
residue class modulo \(q\), and

\[
 \sum_{\substack{a\ll qg/R\\a\equiv a_0\ (q)}}\frac1a
 \ll 1+\frac1q\log(2X).
 \tag{3.2}
\]

There are at most \(\tau(N)\) choices of \(g\).  The same calculation
for \(q=1\) includes exactly the odd divisor denominators \(b\mid N\).
Thus, if \(M_\theta(z)\) is the absolute coefficient mass in an exact
ordinary fibre,

\[
 \max_zM_\theta(z)\ll\tau(N)\log(2X),
 \qquad
 \sum_zM_\theta(z)\ll y\log(2X).
 \tag{3.3}
\]

For odd \(b\), \(\chi_4(b)=e((b-1)/4)\).  A fixed adjusted fibre
\(\phi=z\) is the union of at most two restricted ordinary fibres:
\(\theta=z\) for \(b\equiv1\pmod4\), and
\(\theta=z-1/2\) for \(b\equiv3\pmod4\).  Hence (3.3), up to an
absolute factor, also holds for \(M_\phi\).

Distinct reduced \(\theta\)-values have denominators at most \(y\), so
their circular spacing is at least \(y^{-2}\).  Adding a half-integer
carrier gives reduced denominator at most \(2y\), so distinct
\(\phi\)-values have spacing at least \((4y^2)^{-1}\).  Therefore, for
either carrier and \(0\le\delta\le1/2\),

\[
 \begin{aligned}
 \sum_{\|z-z'\|\le\delta}M(z)M(z')
 &\le \left(\sum_zM(z)\right)
       \max_zM(z)\,O(1+\delta y^2)\\
 &\ll y\tau(N)\log^2(2X)(1+\delta y^2).
 \end{aligned}
 \tag{3.4}
\]

At \(\delta=y^{-2}\), (3.4) is
\(O_\varepsilon(yX^\varepsilon)\) for both \(\theta\) and \(\phi\).

The exact square is \(\sum c_{a,b}\overline{c_{a',b'}}
e(\phi_{a,b}-\phi_{a',b'})\).  Partition its ordered pairs into the
complete \(b=b'\) owner, the cross-row union where at least one of the
two carrier distances is at most \(y^{-2}\), and the complement.  The
complement is exactly \(\mathcal R_{y^{-2}}\); all three conditions are
symmetric under reversing the pair, so it is real.  Equations
(2.6) and (3.4), with a union bound for the two collars, prove (1.1).
Conversely, the scalar target and the residual target imply one another
after the standard renaming of \(\varepsilon\).  No separated
Fourier-index norm enters this partition.

## 4. Determinant aspect loss, Poisson normalization, and the radical channel

For different denominators put

\[
 b=Gr,qquad b'=Gs,qquad (r,s)=1,qquad
 \Delta=G\delta_0,qquad \delta_0=as-a'r.
 \tag{4.1}
\]

All solutions on one determinant fibre are
\(a=a_0+r\ell,a'=a'_0+s\ell\).  Both
\(e(N\delta_0/(Grs))\) and
\(\chi_4(Gr)\chi_4(Gs)=\chi_4(rs)\) are constant in \(\ell\).  The
identity

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right)
 \tag{4.2}
\]

therefore has no oscillatory companion.  Summing it safely retains the
first-point/aspect terms \(r/a_{\min}+s/a'_{\min}\); they cannot be
replaced by logarithms alone.  An admissible odd counterexample is

\[
 r=1,\qquad s=S\ {\rm odd},\qquad a=a'=1,\qquad
 \delta_0=S-1.
 \tag{4.3}
\]

Choose odd \(G\asymp R^{3/2}\), odd \(S\asymp R^{1/2}\), and
\(GS\le y\).  Both fractions lie in the small-arc chart, while the
displayed reciprocal kernel has a one-point contribution \(1\), but
\(\log(2X)/|\delta_0|\to0\).  Thus (4.2) alone cannot give an
aspect-free \(1/|\delta_0|\) contraction.  The discovery report and the
current conductor candidate now use the parity-correct variable odd-\(S\)
example (4.3).  The parity-invalid \(r=1,s=100\) line occurred only in
an earlier hostile working draft; it was superseded by (4.3), and the
hostile primary has now been mechanically repaired.

For the Poisson seam, let

\[
 a_h(x)=\frac1hV_{\rm low}(4R^2h^2/x^2).
\]

With \(\widehat f(\xi)=\int f(x)e(-x\xi)\,dx\), symmetric Poisson
summation of the inclusive hard interval gives the complete formula

\[
 \begin{aligned}
 \sum_{d\le y}\chi_4(d)a_h(d)e(Nh/d)
 ={}&\frac12\chi_4(y)a_h(y)e(Nh/y)\\
 &+\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \lim_{K\to\infty}\sum_{|k|\le K}
 \int_0^y a_h(x)
 e\!\left(\frac{Nh}{x}+(\sigma/4-k)x\right)dx.
 \end{aligned}
 \tag{4.4}
\]

The half-endpoint repairs Fourier inversion at \(d=y\); omitting it
would make the purported full transform false.  For an interior
stationary mode set \(r=\sigma-4k>0\).  Then \(r\) is odd,
\(\sigma=\chi_4(r)\), and

\[
 x_*=2\sqrt{Nh/r},\qquad
 \Phi(x_*)=\sqrt{Nhr},\qquad
 \Phi''(x_*)=\frac{r^{3/2}}{4(Nh)^{1/2}}.
 \tag{4.5}
\]

The branch factor \(\chi_4(r)/(2i)\), the Gaussian factor \(e(1/8)\),
and \(\Phi''(x_*)^{-1/2}=2(Nh)^{1/4}r^{-3/4}\) combine, including
the outside \(1/h\), to

\[
 \boxed{
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr})},
 \qquad e(-1/8)=-i\,e(1/8).
 \tag{4.6}
\]

This verifies the constant and both odd branches.  It does not turn
(4.6) into a full identity.  The hard endpoint and its incomplete-Fresnel
transition, nonstationary modes, profile-boundary and stationary
entry/exit crossings, remainders, small heights, floors, and conjugate
sign remain separate owners in (4.4).  Modewise modulus in the possible
stationary range costs

\[
 N^{1/4}\sum_{h\ll R}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \ll R^{3/2}\log(2X),
 \tag{4.7}
\]

which is above the target \(R\).  A second Legendre transform returns
the reciprocal phase, so this is a self-return diagnostic.

Finally write uniquely \(N=Ds^2\), with \(D\) squarefree.  The variable
stationary phase satisfies

\[
 e(\sqrt{Nhr})=1
 \quad\Longleftrightarrow\quad hr=Dt^2.
 \tag{4.8}
\]

There is only this one radical channel.  With every bounded principal or
incomplete-Fresnel weight retained, its absolute principal mass is

\[
 N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
 \tag{4.9}
\]

The fixed factor \(e(-1/8)\) in (4.6) is common to this channel; “phase
one” in (4.8) refers to the variable radical phase.  Equation (4.9) is
target-safe but controls neither near radicals nor any owner outside the
principal family.

## 5. Repairs and overclaim audit

- The current conductor candidate correctly distinguishes the exact
  integerized cone from the original \(X\)-phase cone and prices their
  accepted \(O(R)\) seam.  Earlier unqualified wording “the flat cone”
  needed this repair.

- The exact lift uses the certified small-arc fact \(h<d\).  A bound
  \(h/d<C/R\) with an unspecified fixed \(C\) is not, by itself, a
  uniform proof of \(h<d\) for the finitely many smallest \(X\).  The
  current candidate names the correct owner.

- The fibre converse now states that \(q,g\) are odd.  The discovery
  report has been repaired to the variable odd-\(S\) example (4.3), as
  has the conductor candidate.  The parity-invalid \(r=1,s=100\) line
  occurred only in an earlier hostile working draft; it was superseded,
  and `farey_scalar_self_return_hostile_audit.md` has now been
  mechanically repaired.

- The complete same-denominator owner is promoted as a row square.  No
  separate positivity is attributed to its unequal-numerator subtotal.

- Both ordinary and character-adjusted collars are required for the
  stated residual (not merely exact ordinary collisions), and their
  union is deleted only at the proved scale \(y^{-2}\).  No wider
  resonance collar is claimed.

- The clean Poisson term is normalized by \(e(-1/8)\), not by an
  uncombined \(e(1/8)\) with its branch factor forgotten.  More
  importantly, it is explicitly scoped as an interior principal family.
  The blind report's schematic grouped stationary sum and any clean
  square-root formula in a primary report must not be promoted as a full
  transform of the hard finite scalar.

- The radical calculation has exactly one channel \(D=\operatorname{sf}(N)\)
  and only proves the upper bound (4.9) for the principal family.  It is
  neither a scalar lower bound nor a proof of the nonsquare/near-radical
  estimate.

- Round 122's complementary-divisor map and the second stationary
  transform are invertible self-returns.  Round 127 already rejects the
  stronger separated \(k\)-energy.  The current candidate invokes
  neither as a gain, proves no target estimate, and makes no direct M1,
  M2, M9, endpoint, quarter-scale, or exponent claim.

After these exclusions, no full-transform or target overclaim remains in
the conductor candidate.

## 6. Dependencies and exact artifacts used

This review independently recomputed the seams using:

- the three Round-138 primary reports
  `blind_reduced_fraction_scalar_feasibility.md`,
  `literal_signed_farey_scalar_attack.md`, and the mechanically repaired
  `farey_scalar_self_return_hostile_audit.md`;
- the final clean conductor candidate
  `conductor_round138_scalar_rows_and_resonance_fibres.md`;
- the Round-121 synthesis
  `m9-m1-global-lower-height-kernel-gate/synthesis.md`;
- the Round-122 synthesis
  `m9-m1-near-square-complementary-divisor-gate/synthesis.md`;
- the Round-127 synthesis
  `full-proof-frontier-inequality-selection-gate/synthesis.md`;
- the frozen Round-138 statement and the previously supplied control
  models.

The hostile report was reread after its final mechanical repair.  No
numerical experiment, symbolic computation, web source, arbitrary
coefficient replacement, separated \(k\)-energy, or centre average was
used.  No shared state or artifact other than this review was edited.

## 7. Recommended state effect and verdict

Promote only the exact integerized flat-cone/Farey identity, the complete
same-denominator bound, the ordinary and adjusted fibre classification,
the \(y^{-2}\) collision packing, and the strict residual identity
(1.1).  Retain the determinant and Poisson calculations as obstruction
and normalization evidence.  Keep \(|\mathcal R_{y^{-2}}|\), the lower
signed scalar, lower GAR, both direct blockwise M1 parents, all M2
parents, endpoint uniformity, M9, the quarter theorem, and both global
exponents open.

GREEN

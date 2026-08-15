# Hostile audit of the alpha high-pass log-dilation commutator

## 1. Result

**Scoped adversarial no-go and seam rejection.**  The zero of
(1-\psi(\beta)) at \(\beta=0\) gives a correct zero-mass kernel only in
the Mellin-normalized logarithmic variable.  It does **not** give a
target-sized difference operator on the actual alpha branch.  If
(\operatorname {supp}\psi\subset[-M,M]), \(\lambda=\mu+\nu\), and

\[
 m_\lambda(\beta)=(1-\psi(\beta))\psi(\beta+\lambda),
\]

then, for every \(|\lambda|>2M\),

\[
 \boxed{m_\lambda(\beta)=\psi(\beta+\lambda).}                 \tag{50.1}
\]

Thus on the separated high-beta/bounded-alpha slices the purported
high-pass commutator is exactly the bounded-alpha low-pass packet: the
factor \(1-\psi(\beta)\) is identically one on its support.  Its inverse
kernel has zero mass by oscillation, but its \(L^1\) norm is fixed and
nonzero.  A single arithmetic lattice atom keeps exactly that absolute
packet mass, and a single hard floor/product-star jump keeps fixed total
variation.  Consequently, neither zero mass, vanishing moments, nor a
BV estimate applied packet by packet supplies any negative power of
(X\) or of the outside height.

This is an actual-interface obstruction to the proposed mechanism, not a
signed lower bound for the whole alpha operator.  The low character
factor, radial integral, connectors, and signed Plemelj/height operation
could still cancel collectively, but proving that would be a new theorem.
The known all-absolute capacities therefore remain
(X^{1/8+o(1)}\) on the normalized lattice scale and
(U^{c'-1/2-\operatorname {Re}z/2}\) on the height scale.  Restoring the
sole external \(X^{1/4}\) gives physical capacity
(X^{3/8+o(1)}\), not the target \(X^{1/4+\varepsilon}\).

## 2. Exact statement and hypotheses

Use the accepted common finite antecedent and put

\[
 A=c+i\beta,\qquad B=A+z,\qquad
 \alpha=\beta+\mu+\nu.
\]

Let \(\psi\in C_c^\infty(\mathbb R)\), with \(\psi=1\) on a
neighbourhood of zero, and choose \(M\) with
\(\operatorname {supp}\psi\subset[-M,M]\).  No evenness or positivity of
\(\psi\) is assumed.  Adopt the Fourier convention

\[
 \widehat f(\beta)=\int_{\mathbb R}f(y)e^{i\beta y}\,dy,
 \qquad
 \check g(t)=\frac1{2\pi}\int_{\mathbb R}g(\beta)e^{-i\beta t}\,d\beta.
                                                               \tag{50.2}
\]

Set \(k=\check\psi\) and \(K=\delta_0-k\).  Then

\[
 \check{(1-\psi)}=K,
 \qquad \int_{\mathbb R}k(t)\,dt=\psi(0)=1,
 \qquad \int K=0.                                             \tag{50.3}
\]

For a Mellin datum \(F\), define

\[
 \mathscr I_cF(Y)=\frac1{2\pi i}\int_{(c)}F(A)Y^{-A}\,dA,
 \qquad
 G_c(y)=e^{cy}\mathscr I_cF(e^y).
\]

All formulas below are first distributional formulas against compact
smooth tests, or formulas on the finite Abel-regularized antecedent.  In
particular, no raw infinite comb is put under an unjustified absolute
integral.  With \(\lambda=\mu+\nu\), define

\[
 g_\lambda(t)=e^{i\lambda t}k(t),\qquad
 p_\lambda=K*g_\lambda
 =\check{\{(1-\psi(\beta))\psi(\beta+\lambda)\}}.              \tag{50.4}
\]

The no-go assertion has three exact parts.

1. If \(|\lambda|>2M\), then (50.1) holds and
   \[
   p_\lambda(t)=e^{i\lambda t}k(t),\qquad
   \int p_\lambda=0,qquad
   \|p_\lambda\|_1=\|k\|_1\geq1.                             \tag{50.5}
   \]
2. For a finite normalized log-lattice atom
   \(a\delta_{y_0}\),
   \[
   \|p_\lambda*(a\delta_{y_0})\|_1
   =|a|\|k\|_1\quad (|\lambda|>2M).                           \tag{50.6}
   \]
3. Let \(S_a^*\) be a unit hard step at \(a\), with the equality
   value \(1/2\).  Then
   \[
   \operatorname {Var}_{\mathbb R}(p_\lambda*S_a^*)
   =\|k\|_1\quad (|\lambda|>2M),                              \tag{50.7}
   \]
   while \(K*S_a^*=S_a^*-k*S_a^*\) retains the original unit
   jump before the bounded-alpha convolution.

The complete alpha operator still means the bulk term, the
Cauchy--Pompeiu area connector (or both sharp strip edges), finite
\(s\)-sides, the oriented \(u/v\) faces, positive axes, connector axes,
mixed connector, one joint corner, the signed top Plemelj operation, the
joint outside-height limit, the radial \(R_1\) factor, and the actual
\(j,h,q,x\) profiles, \(H_j+1\) floors, and product stars, all before the
single external \(X^{1/4}\).  Equations (50.1)--(50.7) obstruct a generic
high-pass/BV proof of its estimate; they do not delete any of those
terms.

## 3. Proof or derivation

Parametrizing the upward Mellin line by \(A=c+i\beta\) gives

\[
 \mathscr I_cF(Y)
 =\frac1{2\pi}\int_{\mathbb R}F(c+i\beta)Y^{-c-i\beta}\,d\beta.
\]

Therefore (50.2), with \(y=\log Y\), gives the exact normalization

\[
 e^{cy}\mathscr I_c[(1-\psi)F](e^y)
 =(K*G_c)(y)
 =G_c(y)-\int k(t)G_c(y-t)\,dt.                               \tag{50.8}
\]

In the unnormalized multiplicative variable the same sign and dilation
are

\[
 \mathscr I_c[(1-\psi)F](Y)
 =\mathscr I_cF(Y)
  -\int k(t)e^{-ct}\mathscr I_cF(Ye^{-t})\,dt.                \tag{50.9}
\]

Thus the inverse kernel is \(\delta_0-k\), not \(k-\delta_0\), and the
dilation is \(Y\mapsto Ye^{-t}\) with the displayed Mellin-line weight.
The zero moment in (50.3) belongs to the normalized log amplitude
\(G_c\).  Treating it as an unweighted zero-mass finite measure on the
raw amplitude is unjustified; although \(k\) is Schwartz,
\(e^{-ct}k(t)\) need not be integrable on both tails.  Compact testing or
the finite antecedent is essential.

The bounded-alpha factor cannot be frozen.  Since
\(\alpha=\beta+\lambda\),

\[
 \check{\psi(\,\cdot+\lambda)}(t)=e^{i\lambda t}k(t),
\]

which proves (50.4).  If \(|\lambda|>2M\) and
\(\psi(\beta+\lambda)\ne0\), then
\(|\beta|\geq|\lambda|-M>M\), so \(\psi(\beta)=0\).  This proves
(50.1), hence (50.5).  Notice that \(p_\lambda\) has not merely zero
mass: because its multiplier vanishes on a neighbourhood of zero, all
of its formal polynomial moments vanish.  Nonetheless its \(L^1\) norm
is the fixed number \(\|k\|_1\).  The vanishing moments are cancellation
inside a modulated packet, not a small operator norm.

For the accepted comb on a line \(c>0\),

\[
 C(Y)=\sum_{n\geq1}\delta(Y-n)-1
     =2\sum_{h\geq1}\cos(2\pi hY)
\]

against compact tests.  Its normalized logarithmic lattice part is

\[
 e^{cy}\sum_{n\geq1}\delta(e^y-n)
 =\sum_{n\geq1}n^{c-1}\delta(y-\log n).                       \tag{50.10}
\]

At finite truncation, (50.6) follows immediately by translating
\(p_\lambda\).  Hence an all-absolute summation over lattice packets
pays the same arithmetic mass up to the fixed factor \(\|k\|_1\); zero
mass can help only after a genuinely signed interaction between
different packets and the remaining low/radial factors.
The equivalent Abel harmonic control is still

\[
 C_\varrho(N)=2\sum_{h\geq1}\varrho^h\cos(2\pi hN)
 =\frac{2\varrho}{1-\varrho}
 \quad(N\in\mathbb Z,\ 0<\varrho<1).                          \tag{50.10a}
\]

Thus the identity-delta part of \(K\) cannot be discarded
coefficientwise.  The bounded-alpha convolution replaces this point
spike by the moving packet (50.5); equation (50.6), rather than a
pointwise Abel divergence, is the stable absolute obstruction after that
coupling.

For the star-step control, point values do not alter the distributional
derivative and

\[
 (S_a^*)'=\delta_a,qquad
 (p_\lambda*S_a^*)'=p_\lambda(\,\cdot-a).
\]

This proves (50.7).  Before bounded-alpha smoothing,

\[
 (K*S_a^*)'=\delta_a-k(\,\cdot-a),                            \tag{50.11}
\]

so the atomic jump is unchanged.  A floor is a sum of such hard steps,
and a product-star equality case is locally one such half-weighted step.
Thus packetwise BV accounting pays one fixed packet per nonzero jump.
The value \(1/2\) at equality changes neither (50.11) nor the one-sided
jump.  More quantitatively, for distinct \(y_j\) and

\[
 F_N(y)=\sum_{j=1}^N a_jS_{y_j}^*(y),
\]

the singular and absolutely continuous parts of the derivative are
mutually singular, and hence

\[
 \begin{aligned}
 D(K*F_N)
 &=\sum_{j=1}^Na_j\delta_{y_j}
   -\sum_{j=1}^Na_jk(\,\cdot-y_j)\,dy,\\
 \operatorname {Var}(K*F_N)
 &\geq\sum_{j=1}^N|a_j|.                                     \tag{50.11a}
 \end{aligned}
\]

After bounded-alpha coupling on a separated slice,

\[
 D(p_\lambda*F_N)=\sum_{j=1}^Na_jp_\lambda(\,\cdot-y_j),
 \qquad
 \sum_{j=1}^N\|a_jp_\lambda(\,\cdot-y_j)\|_1
 =\|k\|_1\sum_{j=1}^N|a_j|.                                 \tag{50.11b}
\]

The second equality is the exact all-absolute capacity.  Moreover, for
each fixed finite \(N\) the \(y_j\) can be chosen sufficiently separated
that the \(L^1\) norm of the sum in (50.11b) is arbitrarily close to its
right side.  Thus this is also a genuine scoped \(N\)-jump adversary, not
merely a loose upper bound.  Taking
\(N=X^{1/8+o(1)}\) reproduces the size of the accepted normalized
absolute benchmark.  The actual floor locations need not enjoy this
separation, so (50.11b) is not asserted as a lower bound for the full
actual signed sum.

For a general actual weight \(W_X(y)\), the exact commutator is

\[
 K*(W_XG_c)-W_X(K*G_c)
 =\int k(t)\{W_X(y)-W_X(y-t)\}G_c(y-t)\,dt.                  \tag{50.12}
\]

At an \(H_j\)-floor or product-star boundary the brace in (50.12) is
order one on one side of arbitrarily small \(t\); it is not controlled
by a uniform classical derivative.  The \(H_j+1\) convention fixes the
coefficient normalization but does not remove the floor jump.  The
actual coefficient packet from the permitted Round-14 synthesis is

\[
 \Omega_X^*(n,h)=\sum_j\mathbf1_{h\leq H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{\frac Xn}\right)\right]^*.          \tag{50.12a}
\]

Every factor in (50.12a) must remain inside (50.12); commuting \(K\)
past it creates its actual floor/profile/star difference, not a smooth
surrogate.  The
Round-14 actual-profile control \(X=y^2,n=7\), where the active
\((h,q)=(1,7)\) row is nonzero and the complementary row is absent,
also shows that the actual profiles and character do not annihilate
every lattice row.  That control is not used as a row-by-row identity
for the masked alpha projection, which has not been proved.

Finite connectors do not supply an independent floor counterterm.  On
the common antecedent, Cauchy--Pompeiu and the outside-axis formulas are
linear identities applied to each fixed actual profile row.  A jump
\(\Delta W_X\) therefore multiplies the connector-completed response of
that same row on both sides of the contour identity.  Connectors may
redistribute its trace among a fundamental line, area/edge pieces, faces,
axes, and the corner; they cancel it only if the **entire signed row
response** is zero.  No finite-connector identity in the permitted
context proves such rowwise vanishing.  In particular, smooth mask
derivatives cannot by themselves erase the singular part in (50.11a),
and after bounded-alpha smoothing their possible cancellation of the
moving packets in (50.11b) is exactly part of the still-unproved global
signed estimate.

The arithmetic residue and the log-kernel delta must not be conflated.
The functional equation gives

\[
 X_\zeta(A)\zeta(A)=\zeta(1-A),\qquad
 \operatorname*{Res}_{A=0}\zeta(1-A)=-1.                    \tag{50.13}
\]

Moving the upward inverse-Mellin line from left of zero to right of zero
therefore gives \(I_{\rm right}-I_{\rm left}=-1\).  By contrast, the
\(\delta_0\) in \(K\) is the identity in the log-dilation variable; it is
not (50.13), not an arithmetic lattice delta, and not the delta part of
the top Plemelj formula.  Splitting these three deltas into separate
owners is invalid.

The point \(A=1\) is removable in the recombined arithmetic factor.  The
artificial radial pole \(A=C=1/4-u/2-v\) is separate from (50.13) and is
not crossed when the shifted line is kept at a fixed \(\delta>1/4\).
If the \(u\)- and \(v\)-lines are subsequently moved, the common finite
ownership identity has the form

\[
 I_{a,b}=I_{0,0}+R_{u=0}+R_{v=0}+R_{u=v=0}
          +H_u+H_v+H_{uv},                                   \tag{50.13a}
\]

with the joint corner once and every signed finite outside face retained.
Neither (50.3) nor (50.13) deletes a term in (50.13a).

For connector ownership, write
\(\Theta_\alpha=(1-\psi(\beta))\psi(\alpha)\).  The
\(A\)-strip density contains

\[
 \partial_{\bar A}\Theta_\alpha
 =\frac i2\bigl((1-\psi(\beta))\psi'(\alpha)
                  -\psi'(\beta)\psi(\alpha)\bigr),            \tag{50.14}
\]

and an outside \(u\)- or \(v\)-height derivative uses
\(D=\tfrac12(\partial_\alpha-\partial_\beta)\), so

\[
 D\Theta_\alpha
 =\frac12\bigl((1-\psi(\beta))\psi'(\alpha)
                 +\psi'(\beta)\psi(\alpha)\bigr),             \tag{50.15}
\]

\[
 D^2\Theta_\alpha
 =\frac14\bigl((1-\psi(\beta))\psi''(\alpha)
 +2\psi'(\beta)\psi'(\alpha)-\psi''(\beta)\psi(\alpha)\bigr).
                                                               \tag{50.16}
\]

At \(A=0\), \(\beta=0\), flatness of \(\psi\) makes (50.14)--(50.16)
and \(\Theta_\alpha\) vanish, so alpha owns no new \(A=0/R_1\)
residue.  On the separated slices of (50.1), however, these densities
reduce respectively to \(\tfrac i2\psi'(\alpha)\),
\(\tfrac12\psi'(\alpha)\), and \(\tfrac14\psi''(\alpha)\): the
bounded-alpha connectors remain fully present.  Therefore the
fundamental-line term, area connector or both strip edges, finite sides,
axes, mixed connector, and corner cannot be removed by the high-pass
identity.

Finally, \(1-\psi(\beta)=1\) on the high tail.  It supplies no decay in
\(|\beta|\), so the accepted absolute height capacity

\[
 U^\gamma,qquad
 \gamma=c'-\frac12-\frac{\operatorname {Re}z}{2}>\frac12,     \tag{50.17}
\]

is unchanged.  Likewise (50.5)--(50.7) contain no \(X\)-dependent small
parameter and do not alter the actual \(h,q,j,x\) powers.  The normalized
all-absolute lattice benchmark remains \(X^{1/8+o(1)}\); the sole
external factor makes it \(X^{3/8+o(1)}\).  A target proof must therefore
obtain both the full signed height gain and the missing normalized
\(X^{-1/8+o(1)}\) gain from the complete coupled operator, not from the
zero moment alone.

## 4. First doubtful or unproved step

The first unproved step is a uniform signed estimate and Cauchy-tail
theorem for the **entire connector-completed finite alpha antecedent**.
It must combine the \(\delta_0\) and \(-k\) log-dilation pieces, the
bounded-alpha convolution, the \(A\)-strip connector, all finite
\(s,u,v\) faces, the positive and connector axes, mixed connector and
unique corner, and the radial/profile operator before taking an absolute
value.  The top variable

\[
 \mu=\alpha-\beta-\nu
\]

couples the modulating parameter \(\lambda=\mu+\nu\) to both the high
beta height and the Plemelj denominator.  Thus (50.5) may participate in
signed \(\mu,\nu\) cancellation, but it may not be estimated absolutely
or frozen before the delta-plus-principal-value Plemelj combination.

At fixed finite \(U,V,S\), the common Abel regularization and every face
must first be assembled, the physical real part and signed Plemelj
operation formed, and only then may one take the Abel limit and the
prescribed symmetric cofinal outside-height limit.  If the alpha support
is contained in \([-M,M]\), finite \(s\)-sides vanish by support only
after the stronger enclosure \(S>(U+V)/2+M\); otherwise they remain part
of the Cauchy tail.  No permitted artifact proves the required
\(U^{-\gamma}\) recovery from (50.17), the normalized
\(X^{-1/8+o(1)}\) recovery, or the exchange of the lattice comb with this
ordered Plemelj/height limit.

Accordingly, (50.1)--(50.12) rigorously refute the proposed generic
zero-mass/BV saving, but they do not refute the possibility of a new
global signed theorem for the fully coupled actual operator.

## 5. Control tests and outcomes

- **fourier_mellin_normalization — pass only in normalized log
  coordinates.**  Equations (50.8)--(50.9) fix the sign, the
  \(Y\mapsto Ye^{-t}\) dilation, and the Mellin weight.  Omitting
  \(e^{-ct}\), reversing \(\delta_0-k\), or applying unweighted zero mass
  to the raw comb fails.

- **zero_mass_commutator — algebra passes; proposed saving fails.**
  \(\int K=0\), and the fully coupled kernel even has all polynomial
  moments zero.  Equations (50.5)--(50.7) show that its absolute packet
  norm and star-step variation are nevertheless fixed.

- **bounded_alpha_coupling — independent-factor treatment fails.**
  The exact multiplier is \(m_\lambda(\beta)\), not a beta high-pass
  followed by a scalar \(\psi(\alpha)\).  For \(|\lambda|>2M\), the
  high-pass is exactly the identity on the bounded-alpha support.

- **connector_and_residue_ownership — pass only with the complete
  finite ledger.**  Equations (50.14)--(50.16) retain the area/edge,
  axis, and mixed connectors.  All vanish at \(A=0\), so alpha owns no
  new arithmetic residue.  The log-kernel delta, arithmetic residue, and
  Plemelj delta are distinct.

- **lattice_floor_star_adversary — generic BV route is falsified.**
  A lattice atom obeys (50.6); a hard equality-star obeys (50.7); the
  unsmoothed high-pass preserves every jump atom by (50.11).  Floors are
  sums of these jumps, and (50.11a)--(50.11b) quantify the resulting
  \(N\)-jump and packetwise lattice capacities.  Finite connectors only
  redistribute each actual row and do not imply rowwise annihilation.
  This is a scoped obstruction, not a signed lower bound after all
  actual packets are recombined.

- **signed_plemelj_order — open as an estimate.**  Delta and
  principal-value pieces must be combined on the same finite antecedent
  before absolute values.  No permitted result licenses termwise
  absolute integration or an early infinite-comb exchange.

- **height_cauchy_limit — fails by absolute control and remains open
  signed.**  The high tail is unchanged, leaving (50.17).  Finite faces
  remain until the joint cofinal enclosure and a signed Cauchy-tail
  estimate are proved.

- **radial_and_external_power_ledger — no hidden gain.**  The radial
  \(R_1\) bracket, actual profiles, \(H_j+1\) floors, stars, scale sum,
  and \(h,q,x\) weights remain inside.  The normalized
  \(X^{1/8+o(1)}\) capacity becomes \(X^{3/8+o(1)}\) after exactly one
  external \(X^{1/4}\).

- **downstream_scope — no implication.**  The no-go rejects one proof
  mechanism only.  It proves neither the alpha estimate nor its
  negation, and gives no closure of the swept operator, post-FE vector
  kernel, M9-M1, M9, or the Gauss-circle target.

No numerical experiment, symbolic computation, or web source was used.

## 6. Dependencies and exact artifacts used

This report used only the task brief and its permitted context:

- `rounds/codex-managed/m9-m1-alpha-highpass-log-commutator/briefs/alpha_commutator_hostile_audit.md`
- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/synthesis.md`
- `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/reports/blind_alpha_kernel_rederivation.md`
- `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/reports/alpha_trace_hostile_audit.md`
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`

The exact accepted dependencies used were the masked cosine-comb
reduction, the sign \(\operatorname {Res}_{A=0}\zeta(1-A)=-1\), zero
alpha residue ownership, the diagonal relation
\(\alpha-\beta=\mu+\nu\), connector derivatives, the finite-face and
Plemelj ownership rules, the actual GAR profile/floor/star ledger, and
the accepted absolute height and normalized lattice capacities.  No
other Round-50 report was read.

## 7. Recommended state effect

**Retain the alpha bound as open and reject the proposed zero-mass/BV
closure.**  Record a scoped no-go lemma consisting of (50.1)--(50.7): on
separated bounded-alpha slices the high-pass is exactly one, its inverse
packet has fixed \(L^1\) norm despite all vanishing moments, and lattice
atoms and hard floor/star jumps receive no packetwise BV gain.  Also
record (50.8)--(50.9) as the required Fourier/Mellin normalization and
the three-delta ownership distinction following (50.13).

Do not promote `M9-M1-alpha-bounded-zeta-high-transition-bound`.  Any
next candidate must prove a signed, connector-completed estimate on one
finite antecedent that gains the whole \(U^\gamma\) height capacity and
the normalized \(X^{1/8+o(1)}\) lattice capacity while preserving the
ordered Plemelj and outside-height limits.  Leave the swept transition,
post-FE vector kernel, M9-M1, M9, and the Gauss-circle target open.

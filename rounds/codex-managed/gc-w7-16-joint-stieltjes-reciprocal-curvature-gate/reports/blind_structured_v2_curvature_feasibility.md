# Blind structured \(V^2\) reciprocal-curvature feasibility report

## 1. Result: no-go lemma

Write

\[
 \Lambda=\lambda_B\rho^2,
 \qquad
 \mathcal E(N,\Lambda)
 =\min\{N,\,N\sqrt\Lambda+\Lambda^{-1/2}\}.
\]

The proposed estimate with factor \(\mathcal E(N_\rho,\Lambda)\) is
**false for the stated Stieltjes-character threshold class**.  There is
an admissible real, nonnegative triangular \(w\), an admissible one-point
profile \(P\), and a reciprocal phase having an integer first-derivative
crossing at the centre of the triangle for which

\[
 \frac{\left|\sum_v^*U(v)e(f(v))\right|}
      {\|U\|_{V^2(I)}\mathcal E(N_\rho,\Lambda)}
 \gg Y^{1/48}.
\]

Thus the estimate fails even after a factor \(Y^\varepsilon\), by taking
any fixed \(\varepsilon<1/48\).  The counterexample uses the actual
threshold superposition and is not a generic phase-adapted coefficient
sequence.

For arbitrary amplitudes, the exact dual norm is the standard deviation
of all prefix sums, including the two endpoint coordinates.  Consequently
partial summation from a uniform unweighted curvature estimate has an
unavoidable generic factor \(N^{1/2}\).  A universally valid repaired
statement is

\[
 \left|\sum_{v\in I}^*U(v)e(f(v))\right|
 \ll_\varepsilon
 \|U\|_{V^2(I)}N_\rho^{1/2}
 \mathcal E(N_\rho,\Lambda)Y^\varepsilon.
\]

The exact best replacement is the dual prefix-variance norm given below.

There is a transcription issue in `blind_statement.md`: its displayed
second entry is written as the product
\(N_\rho\sqrt\Lambda\,\Lambda^{-1/2}=N_\rho\), whereas the task brief and
the reciprocal-curvature question use the sum
\(N_\rho\sqrt\Lambda+\Lambda^{-1/2}\).  The no-go result concerns the
intended sum.  The literal product reduces the displayed minimum to
\(N_\rho\) and contains no curvature gain.

## 2. Exact statement and hypotheses

### 2.1 Exact generic \(V^2\) dual

Let \(I=\{v_1<\cdots<v_n\}\) be consecutive integers and put

\[
 z_j={\bf1}_{v_j\text{ is in }*}\,e(f(v_j)),\qquad
 Z_0=0,\qquad Z_r=\sum_{j=1}^r z_j\quad(1\le r\le n),
\]

and \(\overline Z=(n+1)^{-1}\sum_{r=0}^n Z_r\).  For

\[
 \|u\|_{V^2}^2
 =|u_1|^2+\sum_{j=1}^{n-1}|u_{j+1}-u_j|^2+|u_n|^2,
\]

one has the exact identity

\[
 \sup_{u\ne0}
 \frac{|\sum_{j=1}^n u_jz_j|}{\|u\|_{V^2}}
 =\mathfrak D_I(z),
 \qquad
 \mathfrak D_I(z)^2
 =\sum_{r=0}^n|Z_r-\overline Z|^2.                    \tag{2.1}
\]

Equivalently, if \(L\) is the \(n\)-by-\(n\) tridiagonal matrix with
diagonal entries \(2\) and adjacent entries \(-1\), then

\[
 \mathfrak D_I(z)^2=z^*L^{-1}z,
 \qquad
 (L^{-1})_{jk}
 ={\min(j,k)(n+1-\max(j,k))\over n+1}.               \tag{2.2}
\]

If every subinterval sum of \(z\) has modulus at most \(A\), then

\[
 \mathfrak D_I(z)\le \sqrt{n+1}\,A.                 \tag{2.3}
\]

The exponent \(1/2\) is sharp for generic sequences: for \(z_j=1\),

\[
 \mathfrak D_I(z)^2={n(n+1)(n+2)\over12},
 \qquad
 \max_{r<s}|Z_s-Z_r|=n.                              \tag{2.4}
\]

### 2.2 Structured no-go family

For integers \(M=2^s\to\infty\), take

\[
 Y=M^6,\quad D=B=M^3,\quad L=M,\quad
 W=M^{21/8},\quad \rho=1,\quad a'=M,
\]

and

\[
 \kappa=1,\qquad \vartheta=0,\qquad c=M^6,
 \qquad v_0=M^3.
\]

Then

\[
 Q_B=M^{19/8},\quad N_\rho\asymp M^{19/8},\quad
 J_B=1+M^{-5/8},\quad \lambda_B=\Lambda=M^{-2}.
                                                               \tag{2.5}
\]

Choose an interval centred at \(v_0\), of length comparable to and at
most \(Q_B\).  Put \(H=\lfloor M/100\rfloor\), and define

\[
 w(t)=\left(1-{|t-v_0|\over H}\right)_+,
 \qquad P(1)=1,\quad P(g)=0\ (g\ne1),
\]

and let \(\tau=1\) on \(I\), zero-extended outside it.  These data obey
all support, supremum, and discrete-variation hypotheses.  In particular,
\(\sum_t|w(t)-w(t+1)|=2\), and \(g=1\asymp D/B\) is an odd character
input with \(\chi_4(1)=1\).

If the star is the customary condition \((v,a'/\rho)=1\), the choice
\(M=2^s\) makes the starred points precisely the odd \(v\)'s.  The same
lower bound below then holds with an absolute constant loss.  If the star
has a different meaning, it must be stated before the theorem is
well-defined.

## 3. Proof and derivation

### 3.1 Derivation of the exact dual norm

Define

\[
 Du=(u_1,u_2-u_1,\ldots,u_n-u_{n-1},u_n).
\]

The image of \(D\) is the hyperplane

\[
 y_n-y_0-\sum_{r=1}^{n-1}y_r=0.
\]

A vector \(h\in\mathbb C^{n+1}\) with \(D^*h=z\) has the form

\[
 h=(\alpha,\alpha-Z_1,\ldots,\alpha-Z_{n-1},Z_n-\alpha).
\]

Therefore the dual norm is the least Euclidean norm of such an \(h\):

\[
 \mathfrak D_I(z)^2
 =\min_{\alpha\in\mathbb C}\sum_{r=0}^n|Z_r-\alpha|^2.
\]

The minimizer is \(\alpha=\overline Z\), proving (2.1).  Since
\(D^*D=L\), inversion gives (2.2).  Taking \(\alpha=Z_0\) proves (2.3).
Formula (2.4) follows by summing \((r-n/2)^2\) for \(0\le r\le n\).
This calculation includes, rather than discards, both endpoint terms.

For the reciprocal phase,

\[
 f''(v)=-{2ca'\over\kappa\rho v^3},
 \qquad |f''(v)|\asymp\lambda_B\rho^2=\Lambda.
\]

Its relative variation on \(I\) is \(O(Q_B/B)\).  Splitting according
to every integer crossing of the monotone derivative, using the trivial
bound on the pieces where \(\|f'\|\le\sqrt\Lambda\), and discrete first-
derivative summation on the complementary pieces gives, uniformly on
every subinterval,

\[
 \left|\sum e(f(v))\right|
 \ll N\sqrt\Lambda+\Lambda^{-1/2}.                   \tag{3.1}
\]

Indeed there are \(O(N\Lambda+1)\) derivative crossings, each central
piece has length \(O(\Lambda^{-1/2})\), and on the remaining monotone
pieces summation by parts gives the same total order.  Quarter-linear
terms translate the crossings but do not change this count.  Under the
customary coprimality star, expanding its indicator into divisor
progressions replaces \((N,\Lambda)\) on a progression of step \(d\) by
\((N/d,d^2\Lambda)\); its first term remains \(N\sqrt\Lambda\) and its
second is at most \(\Lambda^{-1/2}\).  Summing the divisor progressions
costs only the displayed \(Y^\varepsilon\).

Combining (2.3) and (3.1), and also using the trivial interval bound,
proves the repaired generic estimate with \(N^{1/2}\).  No generic
partial-summation argument can delete this factor because of (2.4).

### 3.2 Exact Stieltjes recombination

For finitely supported \(w\), telescoping gives

\[
 \sum_t(w(t)-w(t+1))\,\mathbf 1_{t\ge \rho vg}=w(\rho vg).
\]

Consequently every supplied amplitude has the exact alternative form

\[
 U(v)={\tau(v)\over a'}
 \sum_g{\chi_4(g)\over g}P(g)w(\rho vg).             \tag{3.2}
\]

This also shows why the abstract class has no hidden rigidity.  One may
choose an odd \(g_0\asymp D/B\), take \(P\) to be a point mass at
\(g_0\), and prescribe a bounded-variation profile on the progression
\(t=\rho g_0v\).  After a harmless scalar normalization, (3.2) realizes
any real bounded-variation profile in \(v\).  Homogeneity cancels that
normalization in the proposed inequality.

For the family in Section 2, (3.2) is simply

\[
 U(v)={w(v)\over M}.                                  \tag{3.3}
\]

Equivalently, each individual threshold is
\(U_t(v)=M^{-1}{\bf1}_{v\le t}\), including its literal endpoint, and
their exact superposition is (3.3).

### 3.3 Structured stationary-window contradiction

For \(v=v_0+h\), exact division gives

\[
 f(v_0+h)
 =-M^4+Mh-{h^2\over M^2(1+h/M^3)}.                  \tag{3.4}
\]

The first two terms are integers.  On \(|h|\le H\), the absolute value
of the last term is at most \(2\cdot10^{-4}\) for large \(M\).  Hence
all nonzero summands in (3.3) lie in one fixed open half-plane.  Moreover,

\[
 f'(v_0)=M\in\mathbb Z,qquad
 f''(v_0)=-2M^{-2},
\]

so this is exactly one reciprocal stationary-lattice crossing; the next
crossing is at distance \(\asymp M^2\), much farther than \(H\asymp M\).
It follows that

\[
 \left|\sum_{v\in I}^*U(v)e(f(v))\right|
 \gg {1\over M}\sum_{|h|\le H}^*w(v_0+h)
 \gg {H\over M}\gg1.                                \tag{3.5}
\]

For the customary coprimality star, only odd \(h\) occur, and their
triangular mass is \(H/2+O(1)\), so (3.5) is unchanged in order.

Both endpoint values of \(U\) vanish because the triangle is strictly
inside \(I\).  Every one of its \(2H\) nonzero increments has modulus
\(1/(MH)\), and therefore

\[
 \|U\|_{V^2(I)}={1\over M}\sqrt{2\over H}
 \asymp M^{-3/2}.                                    \tag{3.6}

This is also safely below the already proved bound
\(J_B^{1/2}/L\asymp M^{-1}\).

On the other hand,

\[
 \mathcal E(N_\rho,\Lambda)
 \asymp M^{19/8}M^{-1}+M
 \asymp M^{11/8}.                                    \tag{3.7}
\]

Thus the proposed right side is

\[
 \ll_\varepsilon
 M^{-3/2}M^{11/8}M^{6\varepsilon}
 =M^{-1/8+6\varepsilon},                             \tag{3.8}
\]

which tends to zero for every fixed \(\varepsilon<1/48\), contradicting
(3.5).  The failure ratio is \(M^{1/8}=Y^{1/48}\).

The same construction also survives the M1 quarter aliases.  For
\(\vartheta=\pm1/4\), replace \(c\) by

\[
 c_\vartheta={(M-\vartheta)v_0^2\over a'}\asymp Y.
\]

Then the constant and linear terms at \(v_0+h\) are
\(-Mv_0+2\vartheta v_0\) and \(Mh\), both integral because \(M=2^s\),
and the remainder is again \(-(M-\vartheta)h^2/(v_0+h)\).  For
\(\kappa=4\), multiplying this choice of \(c_\vartheta\) by \(4\)
does the same.  Thus the quarter-linear branches do not repair the
failure.

## 4. First doubtful or unproved step

There is no unproved step in the counterexample once the intended plus
sign and the customary meaning of the star are fixed.  The first defect
in the supplied theorem statement itself is the missing plus sign noted
in Section 1.  The second is that \(\sum^*\) is not defined in the blind
statement.  The construction explicitly handles the usual condition
\((v,a'/\rho)=1\); a different restriction must be specified and audited.

The first invalid step in any attempted proof is to combine the
thresholds by Minkowski and then replace the resulting
\(\sum_t|c_t|\|U_t\|_{V^2}\) by the much smaller norm of their
superposition.  Here

\[
 \sum_t|c_t|\|U_t\|_{V^2}\asymp M^{-1},
 \qquad
 \left\|\sum_t c_tU_t\right\|_{V^2}\asymp M^{-3/2}.
\]

The missing factor is \(H^{1/2}\asymp M^{1/2}\).  No cancellation from
\(\chi_4\) is available because an admissible \(P\) isolates \(g=1\).

## 5. Control tests and outcomes

1. **`generic_V2_dual_countermodel` — failed as required.**  Equations
   (2.1)--(2.4) give the exact dual norm and the sharp generic
   \(N^{1/2}\) loss.

2. **`single_threshold_birth_phase` — obstruction found.**  With
   \(P=\delta_1\), one has exactly
   \(U_t(v)=M^{-1}{\bf1}_{v\le t}\).  All relevant birth endpoints occur
   inside the coherent phase cone (3.4); literal threshold endpoints do
   not generate cancellation.

3. **`character_before_modulus` — obstruction found.**  The character is
   evaluated before any modulus manipulation, but the allowed profile
   isolates \(g=1\), where \(\chi_4(1)=1\).  Character cancellation is
   therefore absent within the stated class.

4. **`M1_quarter_phase_aliases` — no repair.**  The explicit retuning of
   \(c\) after (3.8) makes both quarter branches have the same coherent
   stationary window.  The \(\kappa=4\) normalization is absorbed by a
   constant-factor change in \(c\asymp Y\).

5. **`reciprocal_second_derivative_and_stationary_lattice` — passed.**
   The exact crossing is \(f'(v_0)=M\), the curvature is
   \(-2M^{-2}\), and adjacent derivative-integer crossings are
   \(\asymp M^2\) away.  The triangular window has width only
   \(H\asymp M=\Lambda^{-1/2}\).

6. **`threshold_superposition_and_Minkowski` — falsified.**  Exact
   telescoping gives (3.2), while Minkowski loses \(H^{1/2}\).  The
   actual \(V^2\) norm cannot replace the sum of the threshold norms.

7. **`V2_endpoint_terms` — passed.**  Formula (2.1) derives the dual with
   both endpoint coordinates.  In the structured counterexample both
   literal endpoint values are exactly zero.

8. **`actual_vs_phase_adapted_coefficients` — actual counterexample.**
   The coefficient is a real nonnegative triangle.  It does not use
   \(e(-f(v))\) or any pointwise phase adaptation.  One may choose the
   triangle first and tune the allowed reciprocal parameter \(c\) so
   that its centre is a stationary-lattice point.

9. **`N_rho_square_root_stop_rule` — stop.**  The exact generic theorem
   has the factor \(N_\rho^{1/2}\).  More strongly, the actual class
   already violates the no-loss claim by \(Y^{1/48}\).  The supplied
   BV/Stieltjes hypotheses do not justify deleting the square-root loss.

10. **`theta_two_thirds_capacity_threshold` — not reached.**  At
    \(B=D\), a coherent stationary triangle has normalized capacity
    \(H^{3/2}=Y^{1/4}\), whereas the proposed curvature factor has only
    capacity \(Y^{11/48}\).  The shortfall is \(Y^{1/48}\), so no
    downstream two-thirds-capacity conclusion has a valid premise.

11. **`no_exponent_or_M9_promotion` — passed.**  The result is only a
    no-go for this local mechanism.  It gives no Gauss-circle exponent,
    M9 statement, quarter theorem, or promotion of the conditional
    \(73/96\) block estimate.

## 6. Dependencies and exact artifacts used

No numerical computation, web source, external theorem, nonblind report,
strategy file, or shared proof-state file was used.  The exact artifacts
used were:

- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/briefs/blind_structured_v2_curvature_feasibility.md`;
- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/blind_statement.md`;
- `problems/gauss_circle.md`;
- `state/control_models.md`.

## 7. Recommended state effect

**Reject** the no-\(N_\rho^{1/2}\) reciprocal-curvature inequality for
the stated abstract Stieltjes-character threshold class.  Retain the
previously proved coefficient norm only; it is consistent with (3.6) but
does not imply the oscillatory claim.  If a successor theorem is wanted,
either use the exact dual factor \(\mathfrak D_I(z)\), retain the safe
\(N_\rho^{1/2}\) loss, or add a genuinely stronger hypothesis excluding
stationary-scale concentration of \(w(\rho vg)\) and point-mass profiles
\(P\).  Mere bounded variation, character placement, threshold
telescoping, or quarter-phase splitting is insufficient.  Make no graph
or shared-state edit and do not promote any exponent.

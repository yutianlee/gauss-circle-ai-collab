# Round 180 blind row-Gram rederivation

## 1. Result

The finite algebra gives a no-go result for the proposed universal off-row
estimate.

For \(h\in\mathbb Z\), the exact cell kernel is

\[
K_{\nu,M}(h):=\int_{I_\nu}e(h\theta)\,d\theta
=\begin{cases}
M^{-1},&h=0,\\[2mm]
e(h\nu/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0.
\end{cases}
\tag{1.1}
\]

The best universal row-diagonal estimate from the displayed support and
energy assumptions is

\[
\frac12\sum_{\epsilon=0}^1\sum_{d\ {\rm odd}}
\int_{I_\nu}|R_{\epsilon,d}(\theta)|^2\,d\theta
\ll \frac{L}{M}\sum_{d,m}|\lambda_{d,m}|^2
\ll \frac{L^3}{M}\mathcal X\asymp L\mathcal X.
\tag{1.2}
\]

This power is sharp. Gram positivity supplies a universal lower capacity for
the signed off-row form, but no row-count-free upper capacity. Thus it is the
wrong one-sided sector for the desired estimate.

If one separately assumes

\[
\frac12\sum_\epsilon\mathcal O_{\epsilon,\nu}\ll L\mathcal X
\tag{1.3}
\]

on all displayed near cells, the nonnegative total cell mass is
\(O(L\mathcal X)\), and the Fejer weights sum to a near-arc bound
\(O(ML\mathcal X)=O(L^3\mathcal X)\). On the far arcs, the stated Fejer
estimate gives the pointwise factor \(M/L\), tail integral \(O(L^{-1/2})\),
and a row-diagonal contribution \(O(L^{5/2}\mathcal X)\). It gives no bound
for the full off-row contribution, because (B180.1) does not control the
unweighted full row sum.

The claimed \(O(L\mathcal X)\) signed off-row upper bound is false for the
abstract coefficient class. It already fails with one site in each row and
can be made arbitrarily large through exact product collisions. Realness and
the fixed character \(\chi_4\) do not prevent the failure, because allowed
real coefficient signs can absorb \(\chi_4\). No nondegenerate target-safe
strict sign sector follows from the displayed hypotheses alone. The first
missing coefficient-specific relation is a twisted product-fiber
Bessel/anticorrelation bound; its kernel-weighted near-product extension
would still have to be proved.

## 2. Exact statement and hypotheses

Assume exactly (B180.1)--(B180.4), with finite support, at most \(CL\) sites
per odd row, \(M\asymp L^2\), and real coefficients. Implied constants below
may depend on the constants in those displayed hypotheses and in
\(M\asymp L^2\), but on no support parameter.

Put

\[
\begin{aligned}
D_{\epsilon,\nu}
&:=\sum_{d\ {\rm odd}}\int_{I_\nu}|R_{\epsilon,d}(\theta)|^2\,d\theta,\\
\overline D_\nu&:=\frac12\sum_\epsilon D_{\epsilon,\nu},\\
\overline O_\nu&:=\frac12\sum_\epsilon\mathcal O_{\epsilon,\nu},\\
A_\nu&:=\frac12\sum_\epsilon\int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta.
\end{aligned}
\tag{2.1}
\]

Then

\[
A_\nu=\overline D_\nu+\overline O_\nu,
\qquad
\overline D_\nu\ll L\mathcal X.
\tag{2.2}
\]

Writing \(h=dm-d'm'\), the exact averaged off-row form is

\[
\overline O_\nu
=2\Re\sum_{d<d'}\chi_4(d)\chi_4(d')
 \sum_{\substack{m,m'\\m\equiv m'\pmod2}}
 \lambda_{d,m}\lambda_{d',m'}
 e\!\left(J(\sqrt{dm}-\sqrt{d'm'})\right)
 K_{\nu,M}(h).
\tag{2.3}
\]

No modulus has been placed around the row-pair sum. If \(r\) is the number
of active rows, Gram positivity and Hilbert-space Cauchy--Schwarz give the
complete universal capacity ledger

\[
-\overline D_\nu\le \overline O_\nu
\le (r-1)\overline D_\nu.
\tag{2.4}
\]

Thus \(\overline O_\nu\gg-L\mathcal X\) uniformly. The upper bound is useless
at the requested scale because (B180.1) does not bound \(r\).

Let

\[
S(\theta):=\frac12\sum_\epsilon|Z_\epsilon(\theta)|^2,
\qquad
\mathfrak N:=\bigcup_{|\nu|\le\lceil\sqrt L\rceil}I_\nu.
\tag{2.5}
\]

Under the extra hypothesis (1.3),

\[
\int_{\mathfrak N}F_M(\theta)S(\theta)\,d\theta
\ll ML\mathcal X\asymp L^3\mathcal X.
\tag{2.6}
\]

For

\[
\mathfrak F:=\{\theta\in\mathbb T:M\|\theta\|\ge\sqrt L\},
\tag{2.7}
\]

the stated Fejer majorant gives exactly

\[
F_M(\theta)\ll\frac ML\quad(\theta\in\mathfrak F),
\qquad
\int_{\mathfrak F}F_M(\theta)\,d\theta\ll L^{-1/2},
\tag{2.8}
\]

and hence

\[
\int_{\mathfrak F}F_M(\theta)
 \left(\frac12\sum_\epsilon\sum_d|R_{\epsilon,d}(\theta)|^2\right)d\theta
\ll L^{5/2}\mathcal X.
\tag{2.9}
\]

For the full sum one gets only

\[
\int_{\mathfrak F}F_M(\theta)S(\theta)\,d\theta
\ll\frac ML\int_{\mathfrak F}S(\theta)\,d\theta;
\tag{2.10}
\]

the last integral has no bound in terms of \(L,\mathcal X\) under the
displayed hypotheses.

For the first missing structural relation, define

\[
T_q:=\sum_{\substack{d\mid q\\d\ {\rm odd}}}
 \chi_4(d)\lambda_{d,q/d},
\qquad
E_q:=\sum_{\substack{d\mid q\\d\ {\rm odd}}}|\lambda_{d,q/d}|^2.
\tag{2.11}
\]

A scale-correct first requirement for a literal coefficient theorem is, for
example, the twisted fiber Bessel relation

\[
\sum_q|T_q|^2\ll L\sum_qE_q.
\tag{2.12}
\]

At minimum its one-fiber consequence is necessary for a homogeneous theorem
uniform under restriction and rescaling. Relation (2.12) caps the positive
exact-collision budget at \(O(L^3\mathcal X)=O(ML\mathcal X)\), hence at
\(O(L\mathcal X)\) after the factor \(K_{\nu,M}(0)=M^{-1}\). It is not
implied by (B180.1), and it is not sufficient for the nonzero-difference
part of (2.3); a literal theorem would also need a signed, kernel-weighted
near-product extension retaining \(\chi_4\) and the actual coefficient
relations.

## 3. Proof or derivation

### Exact cell kernel and parity projection

Integrate over the real lift
\([(\nu-1/2)/M,(\nu+1/2)/M)\). For \(h\ne0\), direct
antidifferentiation gives

\[
\int e(h\theta)\,d\theta
=e(h\nu/M)\frac{e(h/(2M))-e(-h/(2M))}{2\pi i h}
=e(h\nu/M)\frac{\sin(\pi h/M)}{\pi h}.
\tag{3.1}
\]

For \(h=0\), the integrand is \(1\), so the value is exactly \(M^{-1}\).
Equivalently,

\[
K_{\nu,M}(h)=M^{-1}e(h\nu/M)\operatorname{sinc}(h/M),
\quad
\operatorname{sinc}(x)=\frac{\sin(\pi x)}{\pi x},
\quad \operatorname{sinc}(0)=1.
\tag{3.2}
\]

Because \(h\) is integral, \(e(h\theta)\) is one-periodic. Splitting a
wrapped cell at \(0\) gives the same value as the real lift. Half-open
endpoints have measure zero and make adjacent cells disjoint. Also,
\(K_{\nu,M}(h)=0\) for every nonzero multiple of \(M\), whereas
\(K_{\nu,M}(0)=M^{-1}\); conflating these cases erases the exact-collision
obstruction.

Expanding a row pair gives

\[
\int_{I_\nu}R_{\epsilon,d}\overline{R_{\epsilon,d'}}
=\sum_{m,m'}(-1)^{\epsilon(m-m')}
 \lambda_{d,m}\lambda_{d',m'}
 e\!\left(J(\sqrt{dm}-\sqrt{d'm'})\right)
 K_{\nu,M}(dm-d'm').
\tag{3.3}
\]

The identity

\[
\frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
=\mathbf 1_{m\equiv m'\pmod2}
\tag{3.4}
\]

proves (2.3).

### Row diagonal and universal Gram capacity

Let \(n_d\le CL\) be the number of sites in row \(d\). Pointwise
Cauchy--Schwarz gives

\[
|R_{\epsilon,d}(\theta)|^2
\le n_d\sum_m|\lambda_{d,m}|^2
\le CL\sum_m|\lambda_{d,m}|^2.
\tag{3.5}
\]

Integrating over a cell of length \(M^{-1}\), summing \(d\), and using
(B180.1) proves

\[
D_{\epsilon,\nu}\ll\frac{L}{M}L^2\mathcal X
=\frac{L^3}{M}\mathcal X\asymp L\mathcal X.
\tag{3.6}
\]

The power is optimal uniformly over the stated class. Along an integer
sequence take \(M=L^2\), one row \(d=1\), \(n\asymp L\) consecutive
positive sites, equal coefficients, and \(J=L^{-2}>0\). On \(I_0\), all
phase differences are \(O(L^{-1})\), so the row sum has magnitude comparable
to the sum of coefficient magnitudes throughout the cell. Normalizing the
energy to \(\asymp L^2\mathcal X\) makes the cell diagonal
\(\asymp L\mathcal X\).

For capacity, regard
\(v_{\epsilon,d}=\chi_4(d)R_{\epsilon,d}\) as vectors in \(L^2(I_\nu)\).
Then

\[
\left\|\sum_dv_{\epsilon,d}\right\|_2^2
=D_{\epsilon,\nu}+\mathcal O_{\epsilon,\nu}\ge0,
\tag{3.7}
\]

which gives the lower bound in (2.4). If there are \(r\) active rows,

\[
\left\|\sum_dv_{\epsilon,d}\right\|_2^2
\le r\sum_d\|v_{\epsilon,d}\|_2^2,
\tag{3.8}
\]

which gives the upper bound. Averaging in \(\epsilon\) preserves both
inequalities. Equal row vectors attain the order of the upper capacity,
while two opposite equal row vectors attain the lower endpoint. Since \(r\)
is unbounded, only the lower endpoint is uniform.

### Near and far Fejer ledger

By (2.2), the hypothetical bound (1.3) implies

\[
0\le A_\nu\ll L\mathcal X.
\tag{3.9}
\]

On the near-origin lift of \(I_\nu\),

\[
\sup_{\theta\in I_\nu}F_M(\theta)\ll\frac{M}{1+\nu^2}.
\tag{3.10}
\]

For \(\nu=0\) this is the peak bound \(M\); for \(|\nu|\ge1\) it follows
from \(M\|\theta\|\ge|\nu|-1/2\). Consequently

\[
\int_{\mathfrak N}F_MS
\le\sum_{|\nu|\le\lceil\sqrt L\rceil}
 \left(\sup_{I_\nu}F_M\right)A_\nu
\ll ML\mathcal X\sum_{\nu\in\mathbb Z}\frac1{1+\nu^2}
\ll ML\mathcal X.
\tag{3.11}
\]

This uses positivity of \(S\) after recombining diagonal and signed off-row
pieces. An unweighted signed cell integral by itself could not be multiplied
by a varying positive weight.

On \(\mathfrak F\), the threshold gives \(F_M\ll M/L\). With
\(a=\sqrt L/M\), the empty-far-set case being trivial,

\[
\int_{\mathfrak F}F_M(\theta)\,d\theta
\ll\frac2M\int_a^{1/2}t^{-2}\,dt
\ll L^{-1/2}.
\tag{3.12}
\]

The pointwise version of (3.5), summed over rows and averaged over
\(\epsilon\), is \(O(L^3\mathcal X)\). Multiplication by (3.12) proves
(2.9). For \(S\), only (2.10) follows.

Collecting equal product frequencies gives the exact global identity

\[
Z_\epsilon(\theta)
=\sum_q e(J\sqrt q+q\theta)(-1)^{\epsilon q}T_q,
\qquad
\int_{\mathbb T}|Z_\epsilon(\theta)|^2\,d\theta
=\sum_q|T_q|^2.
\tag{3.13}
\]

The parity factor is constant on a product fiber because \(d\) is odd, hence
\(q/d\equiv q\pmod2\). Parseval proves the second identity. Energy controls
\(\sum_qE_q\), not \(\sum_q|T_q|^2\), exposing the missing relation (2.12).

### Exact-product no-go construction

Fix \(L,M,J,\mathcal X\) and choose an odd integer \(q\) having \(N\) odd
divisors, where \(N\) may be arbitrarily large. For every \(d\mid q\), put
\(m=q/d\) and

\[
\lambda_{d,q/d}=a\chi_4(d),
\tag{3.14}
\]

with all other coefficients zero. Every row has one site, every \(m\) is
odd, and the energy is \(Na^2\). Moreover,

\[
\chi_4(d)R_{\epsilon,d}(\theta)
=(-1)^\epsilon a\,e(J\sqrt q+q\theta),
\tag{3.15}
\]

so for every cell

\[
D_{\epsilon,\nu}=\frac{Na^2}{M},
\qquad
\mathcal O_{\epsilon,\nu}=\frac{N(N-1)a^2}{M}.
\tag{3.16}
\]

Choose \(a^2=cL^2\mathcal X/N\), with fixed \(c>0\) small enough for
(B180.1). Then

\[
\overline O_\nu
=c\frac{(N-1)L^2}{M}\mathcal X\asymp N\mathcal X.
\tag{3.17}
\]

Odd integers have unbounded divisor count, so \(N/L\) is unbounded. No
constant in \(\overline O_\nu\ll L\mathcal X\) can therefore depend only on
the displayed hypotheses. This also shows why the zero-difference kernel and
coefficient-character sign relation cannot be omitted.

## 4. First doubtful or unproved step

The first genuinely unproved step needed for a literal theorem is (2.12), or
an equivalent coefficient-specific statement preventing rowwise signs from
neutralizing \(\chi_4\) on exact product fibers. Nothing in
(B180.1)--(B180.4) relates coefficients in different rows. Realness and
\(\chi_4(d)\in\{\pm1\}\) are insufficient: (3.14) uses both facts and still
aligns every row.

Even a proof of (2.12) would close only the \(dm=d'm'\) seam. The next
unproved step would be its signed kernel-weighted extension for
\(0<|dm-d'm'|\lesssim M\), with the phase
\(e(J(\sqrt{dm}-\sqrt{d'm'}))\), parity projection, and cell phase retained.
Taking an absolute value around the row-pair sum would erase the only
possible signed mechanism and would also prove false constant-character and
adversarial controls.

There is likewise no passage from the diagonal far-arc estimate (2.9) to a
full far-arc estimate: (3.13) shows that the missing full \(L^2\) capacity is
another form of the same coefficient-fiber problem.

## 5. Required control test and outcome

1. **Zero difference — pass.** Direct integration gives
   \(K_{\nu,M}(0)=M^{-1}\). It is not zero, even though every nonzero multiple
   of \(M\) has kernel zero. The exact-collision test (3.14)--(3.17) fails
   the proposed off-row theorem precisely through this value.

2. **Wraparound and half-open cells — pass.** Periodicity for integral
   frequencies makes the wrapped integral equal to the lifted integral.
   Half-open endpoints change no integral and prevent double counting.

3. **Row-diagonal power — pass and sharp.** Cauchy--Schwarz gives
   \(L^3/M\asymp L\), and the coherent one-row construction following (3.6)
   attains this order. No smaller power follows uniformly from the packet.

4. **Far-arc Fejer power — pass with a strict limitation.** The threshold
   gives \(F_M\ll M/L\asymp L\), its far tail integrates to
   \(O(L^{-1/2})\), and the diagonal far contribution is
   \(O(L^{5/2}\mathcal X)\). The full row sum remains uncontrolled. If one
   additionally had an \(O(L\mathcal X)\) total-mass bound on every far
   cell, summing \(M/\nu^2\) for \(|\nu|\ge\sqrt L\) would also give
   \(O(L^{5/2}\mathcal X)\), but that is not an assumption in the packet.

5. **Complex dechirping — false-positive control fails.** Fix a cell center
   \(\theta_0=\nu/M\), choose \(N\le M/8\) odd rows \(d_j=2j+1\), and put
   \(m_j=1\). If complex coefficients were admitted, set

   \[
   c_j=a\chi_4(d_j)e(-J\sqrt{d_j}-d_j\theta_0).
   \tag{5.1}
   \]

   Then every character-weighted row is
   \(a e(d_j(\theta-\theta_0))\), up to the common parity sign. Since
   \(|d_j-d_k|\le2N<M/2\), all pair kernels after recentering are real and
   \(\gg M^{-1}\). Thus the off-row form is
   \(\gg a^2N(N-1)/M\). With \(Na^2\asymp L^2\mathcal X\) and
   \(L\ll N\ll M\), this exceeds \(L\mathcal X\). This array is outside the
   real class and shows that a magnitude-only proof cannot work.

6. **Real cosine dechirping — literal control fails.** The complex failure
   is not repaired merely by realness. With the same rows, put
   \(\alpha_j=J\sqrt{d_j}+d_j\theta_0\) and, for
   \(t\in\mathbb R/\mathbb Z\), take the admitted real coefficients

   \[
   \lambda_{d_j,1}(t)
   =a\chi_4(d_j)\cos(2\pi(\alpha_j-t)).
   \tag{5.2}
   \]

   If \(x=\theta-\theta_0\), the character-weighted row sum is

   \[
   \frac a2\left[
     e(t)\sum_j e(d_jx)
     +e(-t)\sum_j e(2\alpha_j)e(d_jx)
   \right],
   \tag{5.3}
   \]

   up to a common parity sign. Averaging its squared \(L^2(I_\nu)\) norm over
   \(t\) removes the mixed term and leaves at least one quarter of the
   squared norm of \(\sum_j e(d_jx)\). The latter is \(\gg N^2/M\), because
   every recentered pair kernel is \(\gg M^{-1}\). The averaged diagonal is
   only \(Na^2/(2M)\). Hence some \(t\) has off-row form
   \(\gg a^2N^2/M\). Since
   \(\sum_j|\lambda_{d_j,1}(t)|^2\le Na^2\), normalization as above gives a
   valid real counterexample of size \(\gg N\mathcal X\). Thus realness alone
   supplies no strict sector.

7. **Arbitrary real signs — fail.** With fixed \(\chi_4\), the allowed
   choice \({\rm sgn}(\lambda_{d,q/d})=\chi_4(d)\) cancels the character on
   an exact product fiber. More generally, if row weights are replaced by
   any prescribed signs \(\sigma_d\in\{\pm1\}\), choosing coefficient signs
   \(\sigma_d\) aligns the rows. Opposite choices on two identical rows
   attain the negative Gram endpoint. Thus the hypotheses force neither sign
   of the off-row form.

8. **Constant character — fail.** Replacing \(\chi_4\) by the constant
   character \(1\) and taking \(\lambda_{d,q/d}=a\) gives exactly
   (3.16)--(3.17). Any argument using only \(|\chi_4(d)|=1\), or first taking
   absolute values, cannot distinguish the literal problem from this false
   unsigned analogue.

9. **One row and one site — degenerate pass; one site per row — fail.**
   With one active row, or one active coefficient globally, the row-pair sum
   is empty and \(\overline O_\nu=0\). This is not evidence for a cross-row
   theorem. With one site in each of arbitrarily many rows, both the
   real-cosine and exact-product constructions violate the desired bound.

10. **Exact product collisions — decisive fail.** Equations
    (3.14)--(3.17) are an admitted real, fixed-\(\chi_4\), one-site-per-row
    counterexample on every cell. They saturate the \(r\)-dependent upper
    Gram capacity and show that product multiplicity cannot be treated as a
    raw count divorced from coefficient-character cancellation.

11. **Universal capacity versus literal coefficient theorem — distinction
    confirmed.** Equations (2.4) and (3.6) are universal Hilbert-space
    facts and give only a uniform negative floor. Relation (2.12) would be a
    new theorem about the literal coefficient family; it cannot be inferred
    from universal Gram geometry, support size, energy, realness, or the
    character modulus.

12. **Downstream/exponent control — no conclusion.** This report proves only
    the finite identities, conditional Fejer ledger, and no-go statement in
    the isolated packet. It supplies no downstream implication and no
    exponent conclusion.

No numerical experiment was used; all controls are exact analytic
constructions.

## 6. Dependencies and exact artifacts used

This was a statement-only independent rederivation. The only artifacts read
were:

- protocol.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/briefs/blind_row_gram_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/blind_statement.md.

No proof graph, active campaign, proof draft, strategy, prior round, sibling
artifact, source, synthesis, or conductor analysis was read. The starting
graph hash was withheld by design. No external theorem or computation is a
dependency.

## 7. Recommended state effect

**Reject** the claim that (B180.1)--(B180.4) alone imply the desired
\(O(L\mathcal X)\) signed off-row upper bound, and record the exact-product
collision as a rigorous obstruction. Retain the exact kernel, parity
projection, sharp row-diagonal bound, Gram-capacity ledger, and conditional
near/far Fejer bookkeeping as finite candidate lemmas subject to conductor
seam review. Any revised literal theorem must add and verify a
coefficient-specific twisted fiber relation such as (2.12), followed by its
nonzero-difference kernel-weighted extension. Do not infer or patch any
downstream proof or exponent claim from this report.
